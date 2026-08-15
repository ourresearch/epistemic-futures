#!/usr/bin/env python3
"""Collect attendees' X timelines into the camera-raw corpus.

Design constraints (from Jason, 2026-08-13):
  * NO keyword filtering. Filtering at the camera-raw stage bakes in a compression
    bias we can't undo later. The only reduction is a uniform recency cap.
  * ONE cap for everybody (default 4,290 = the median post count across the roster),
    so the method is insulated from outliers like @anildash (246k posts). The only
    bias this introduces is more recency skew for prolific people, which is fair.
  * Hard spend ceiling. X charges $0.005 per post read; the script stops before
    exceeding --max-spend rather than discovering the overage on a bill.

Uses /2/tweets/search/all (full archive) rather than /2/users/:id/tweets, which is
capped at the most recent ~3,200 posts. NOTE: search/all silently returns zero
results without an explicit start_time — hence ARCHIVE_START below.

Resumable: state lives in <out>/_state.json. Re-running continues where it stopped.

    export X_BEARER_TOKEN=...
    python3 scripts/collect_x.py --cap 4290 --max-spend 300
    python3 scripts/collect_x.py --dry-run          # cost estimate only
"""

import argparse
import json
import os
import pathlib
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

COST_PER_POST = 0.005
ARCHIVE_START = "2006-03-21T00:00:00Z"  # Twitter's first tweet
PAGE_SIZE = 500  # max_results ceiling for search/all
TWEET_FIELDS = (
    "created_at,text,public_metrics,referenced_tweets,conversation_id,"
    "in_reply_to_user_id,entities,lang,possibly_sensitive,source"
)

# slug -> handle. From dossiers/00-social-census.md. Identity confirmed by bio;
# see that file's "Decoys" table before adding anyone.
ROSTER = {
    "anil-dash": "anildash",
    "tim-oreilly": "timoreilly",
    "ivan-oransky": "ivanoransky",
    "katherine-maher": "krmaher",
    "peter-pomerantsev": "peterpomeranzev",
    "kenneth-cukier": "kncukier",
    "david-weinberger": "dweinberger",
    "benjamin-bratton": "bratton",
    "esther-dyson": "edyson",
    "selena-deckelmann": "selenamarie",
    "adam-becker": "FreelanceAstro",
    "geoffrey-bilder": "gbilder",
    "sherry-turkle": "STurkle",
    "nick-vincent": "nickmvincent",
    "peter-salib": "petersalib",
    "blaise-aguera-y-arcas": "blaiseaguera",
    "amy-brand": "amy_brand",
    "james-evans": "profjamesevans",
    "mike-caulfield": "holden",
    # Added 2026-08-14 by the published-roster reconciliation. Same cap, same
    # no-filtering rule as everyone else (Jason's approval, 2026-08-14).
    "ramon-alvarado": "ramonalvaradoq",
    "kara-miller": "karaemiller",
}
# Removed 2026-08-14: "sanmi-koyejo": "sanmikoyejo" — not on the published attendee
# list; his dossier (including the collected social/) was deleted. See
# dossiers/00-roster.md "Roster history".

# Known post counts (census 2026-08-13), for cost estimation only.
KNOWN_COUNTS = {
    "anildash": 246339, "timoreilly": 47120, "ivanoransky": 32840, "krmaher": 28886,
    "peterpomeranzev": 21428, "kncukier": 18514, "dweinberger": 18480, "bratton": 11085,
    "edyson": 8077, "selenamarie": 4929, "FreelanceAstro": 3652, "gbilder": 3003,
    "STurkle": 2410, "nickmvincent": 1837, "petersalib": 1224, "sanmikoyejo": 1003,
    "blaiseaguera": 973, "amy_brand": 688, "profjamesevans": 532, "holden": 93,
    # 2026-08-14 additions; counts from the free cdn.syndication.twimg.com endpoint,
    # not the paid API.
    "ramonalvaradoq": 2880, "karaemiller": 4410,
}


class BillingWall(Exception):
    """Account-level spend stop (402 credits depleted / 403 monthly spend cap).

    Distinct from a per-account error: nothing else will succeed until a human
    adds credits or raises the cap in console.x.com -> Billing, so the run aborts.
    """


def api_get(url, token, retries=5):
    """GET with backoff on 429/5xx. Returns parsed JSON."""
    for attempt in range(retries):
        req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", "replace")[:200]
            if e.code == 429:
                wait = min(60 * (attempt + 1), 300)
                print(f"    429 rate limited; sleeping {wait}s", flush=True)
                time.sleep(wait)
                continue
            if 500 <= e.code < 600:
                wait = 5 * (attempt + 1)
                print(f"    HTTP {e.code}; retry in {wait}s", flush=True)
                time.sleep(wait)
                continue
            # 402 credits-depleted / 403 spend-cap are account-level walls, not
            # per-account failures: every subsequent request will fail identically.
            # Signal the caller to abort the whole run instead of grinding through
            # the remaining roster collecting one error per account.
            if e.code in (402, 403):
                raise BillingWall(f"HTTP {e.code}: {body}")
            raise RuntimeError(f"HTTP {e.code}: {body}")
        except Exception as e:
            wait = 5 * (attempt + 1)
            print(f"    {type(e).__name__}: {e}; retry in {wait}s", flush=True)
            time.sleep(wait)
    raise RuntimeError("exhausted retries")


def load_state(path):
    if path.exists():
        return json.loads(path.read_text())
    return {"done": {}, "spent_posts": 0}


def save_state(path, state):
    path.write_text(json.dumps(state, indent=2))


def collect_one(slug, handle, cap, token, out_root, state, budget_posts):
    """Fetch up to `cap` most recent posts for one handle. Returns posts fetched."""
    person_dir = out_root / slug / "social"
    person_dir.mkdir(parents=True, exist_ok=True)
    jsonl = person_dir / "x-timeline.jsonl"

    prior = state["done"].get(handle, {})
    already = prior.get("count", 0)
    if already >= cap or prior.get("complete") or prior.get("capped"):
        why = "complete" if prior.get("complete") else "at cap"
        print(f"  {handle}: already {why} ({already:,}) — skipping")
        return 0

    # Restart this handle cleanly rather than resuming mid-stream: pagination
    # tokens expire, and a partial file with an unknown boundary is worse than
    # a re-fetch. Cost of a redo is bounded by the cap.
    if jsonl.exists():
        jsonl.unlink()

    fetched, token_next, pages = 0, None, 0
    started = time.time()
    with jsonl.open("w") as fh:
        while fetched < cap:
            want = min(PAGE_SIZE, cap - fetched)
            if want < 10:  # API minimum
                break
            params = {
                "query": f"from:{handle}",
                "max_results": want,
                "start_time": ARCHIVE_START,
                "tweet.fields": TWEET_FIELDS,
            }
            if token_next:
                params["next_token"] = token_next
            url = "https://api.x.com/2/tweets/search/all?" + urllib.parse.urlencode(params)

            d = api_get(url, token)
            posts = d.get("data", [])
            if not posts:
                # An empty FIRST page is suspicious, not success. The census says how
                # many posts this account has; if it claims thousands and we got none,
                # something is wrong (rename, protected account, archive gap) and
                # marking it complete would make every future resume skip it silently.
                expected = KNOWN_COUNTS.get(handle, 0)
                if fetched == 0 and expected > 50:
                    state["done"].setdefault(handle, {})["suspect_empty"] = (
                        f"0 posts returned but census says {expected:,} — investigate, not skipped"
                    )
                    print(f"    WARNING: 0 posts but census says {expected:,} — NOT marking complete")
                else:
                    state["done"].setdefault(handle, {})["complete"] = True
                break

            for p in posts:
                fh.write(json.dumps(p, ensure_ascii=False) + "\n")
            fh.flush()

            fetched += len(posts)
            pages += 1
            state["spent_posts"] += len(posts)
            state["done"][handle] = {"count": fetched, "complete": False, "slug": slug}
            save_state(out_root / "_state.json", state)

            rate = fetched / max(time.time() - started, 0.1)
            print(
                f"    page {pages}: +{len(posts)} → {fetched:,}/{cap:,}  "
                f"({rate:.0f}/s, ${state['spent_posts'] * COST_PER_POST:,.2f} spent)",
                flush=True,
            )

            token_next = d.get("meta", {}).get("next_token")
            if not token_next:
                state["done"][handle]["complete"] = True
                break
            if state["spent_posts"] >= budget_posts:
                print("    BUDGET CEILING REACHED — stopping")
                break
            time.sleep(1.1)  # full-archive rate limit courtesy

    # Stopping because we reached the cap is a finished account, not a partial one.
    # The loop exits when the remaining allowance drops below the API's 10-result
    # minimum, so `fetched` lands a few short of `cap` — without this, a resume sees
    # 4,289 < 4,290, decides the account is unfinished, and re-buys the whole timeline.
    if fetched >= cap - PAGE_SIZE:
        state["done"][handle]["capped"] = True
    state["done"][handle]["count"] = fetched
    save_state(out_root / "_state.json", state)

    # Date range, for the sidecar README
    if fetched:
        lines = jsonl.read_text().strip().split("\n")
        newest = json.loads(lines[0]).get("created_at", "?")
        oldest = json.loads(lines[-1]).get("created_at", "?")
        print(f"  {handle}: {fetched:,} posts, {oldest[:10]} → {newest[:10]}")
    return fetched


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cap", type=int, default=4290, help="uniform per-person post cap")
    ap.add_argument("--max-spend", type=float, default=300.0, help="hard USD ceiling")
    ap.add_argument("--out", default="dossiers")
    ap.add_argument("--only", nargs="*", help="limit to these handles")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    roster = {s: h for s, h in ROSTER.items() if not args.only or h in args.only}

    if args.dry_run:
        total = sum(min(KNOWN_COUNTS.get(h, args.cap), args.cap) for h in roster.values())
        print(f"{len(roster)} accounts, cap {args.cap:,}")
        print(f"estimated {total:,} posts → ${total * COST_PER_POST:,.2f}")
        for s, h in sorted(roster.items(), key=lambda kv: -KNOWN_COUNTS.get(kv[1], 0)):
            n = min(KNOWN_COUNTS.get(h, args.cap), args.cap)
            print(f"  @{h:<18} {n:>6,} posts  ${n * COST_PER_POST:>7,.2f}")
        return

    token = os.environ.get("X_BEARER_TOKEN")
    if not token:
        sys.exit("set $X_BEARER_TOKEN")

    out_root = pathlib.Path(args.out)
    out_root.mkdir(parents=True, exist_ok=True)
    state = load_state(out_root / "_state.json")
    budget_posts = int(args.max_spend / COST_PER_POST)

    print(f"cap={args.cap:,}  ceiling=${args.max_spend:,.2f} ({budget_posts:,} posts)")
    print(f"already spent: {state['spent_posts']:,} posts "
          f"(${state['spent_posts'] * COST_PER_POST:,.2f})\n")

    # Cheapest first: guarantees the small accounts land even if budget runs out.
    order = sorted(roster.items(), key=lambda kv: KNOWN_COUNTS.get(kv[1], 0))
    for slug, handle in order:
        if state["spent_posts"] >= budget_posts:
            print(f"\nBUDGET EXHAUSTED — {handle} and later not collected")
            break
        print(f"@{handle} ({slug})")
        try:
            collect_one(slug, handle, args.cap, token, out_root, state, budget_posts)
        except BillingWall as e:
            print(f"\n  STOPPING — {e}")
            print("  Not a per-account failure: add credits or raise the monthly spend")
            print("  cap at console.x.com -> Billing, then re-run to resume.")
            break
        except Exception as e:
            print(f"  ERROR {type(e).__name__}: {e}")
            state["done"].setdefault(handle, {})["error"] = str(e)[:200]
            save_state(out_root / "_state.json", state)

    spent = state["spent_posts"]
    print(f"\nDONE. {spent:,} posts, ${spent * COST_PER_POST:,.2f}")
    for h, v in sorted(state["done"].items(), key=lambda kv: -kv[1].get("count", 0)):
        if v.get("error"):
            flag = f"  ERROR: {v['error'][:60]}"
        elif v.get("suspect_empty"):
            flag = f"  SUSPECT: {v['suspect_empty'][:60]}"
        elif v.get("capped"):
            flag = "  (at cap)"
        elif v.get("complete"):
            flag = "  complete"
        else:
            flag = "  partial"
        print(f"  @{h:<18} {v.get('count', 0):>6,}{flag}")


if __name__ == "__main__":
    main()
