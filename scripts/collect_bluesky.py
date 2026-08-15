#!/usr/bin/env python3
"""Collect attendees' Bluesky feeds into the camera-raw corpus.

Bluesky's public API is free and unauthenticated, so unlike the X collector there is
no cap and no budget — every account is pulled in full. That matters for two people:

  * Anil Dash — 246k posts on X (an outlier no uniform cap handles well); his 44.2k
    Bluesky posts are complete and cost nothing.
  * Henry Farrell — his X account is SUSPENDED. Bluesky is his only live feed.

Resumable: state in <out>/_bsky_state.json.

    python3 scripts/collect_bluesky.py
    python3 scripts/collect_bluesky.py --only himself.bsky.social
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

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from slim_bluesky import slim

API = "https://public.api.bsky.app/xrpc"
PAGE_SIZE = 100

# slug -> handle. From dossiers/00-social-census.md.
ROSTER = {
    "anil-dash": "anildash.com",
    "henry-farrell": "himself.bsky.social",
    "adam-becker": "adambecker.bsky.social",
    "blaise-aguera-y-arcas": "blaiseaguera.bsky.social",
    "david-weinberger": "davidweinberger.bsky.social",
    "nick-vincent": "nickmvincent.bsky.social",
    "tim-oreilly": "timoreilly.bsky.social",
    "peter-pomerantsev": "peterpomerantsev.bsky.social",
    "peter-salib": "petersalib.bsky.social",
    "sherry-turkle": "sturkle.bsky.social",
    "amy-brand": "amybrand.bsky.social",
    "kenneth-cukier": "kncukier.bsky.social",
    # Added 2026-08-14 by the published-roster reconciliation.
    "ramon-alvarado": "ramonalvarado.bsky.social",
    # These two have accounts with 0 posts as of the census; included so a later
    # run picks them up if they start posting before the summit.
    "katherine-maher": "krmaher.bsky.social",
    "leslie-chan": "lesliechan.bsky.social",
}
# Removed 2026-08-14 (no longer on the published attendee list, dossiers deleted):
#   "sanmi-koyejo": "sanmikoyejo.bsky.social"  -- had 20 posts collected
#   "clara-collier": "claracollier.bsky.social"  -- account existed, 0 posts


def api_get(path, params, retries=5):
    url = f"{API}/{path}?" + urllib.parse.urlencode(params)
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code == 429 or 500 <= e.code < 600:
                wait = 10 * (attempt + 1)
                print(f"    HTTP {e.code}; retry in {wait}s", flush=True)
                time.sleep(wait)
                continue
            raise RuntimeError(f"HTTP {e.code}: {e.read()[:200]!r}")
        except Exception as e:
            wait = 5 * (attempt + 1)
            print(f"    {type(e).__name__}; retry in {wait}s", flush=True)
            time.sleep(wait)
    raise RuntimeError("exhausted retries")


def collect_one(slug, handle, out_root):
    person_dir = out_root / slug / "social"
    person_dir.mkdir(parents=True, exist_ok=True)
    jsonl = person_dir / "bluesky-timeline.jsonl"
    if jsonl.exists():
        jsonl.unlink()

    fetched, cursor, pages = 0, None, 0
    started = time.time()
    with jsonl.open("w") as fh:
        while True:
            params = {"actor": handle, "limit": PAGE_SIZE, "filter": "posts_with_replies"}
            if cursor:
                params["cursor"] = cursor
            d = api_get("app.bsky.feed.getAuthorFeed", params)
            feed = d.get("feed", [])
            if not feed:
                break
            if pages == 0 and feed:
                author = (feed[0].get("post", {}) or {}).get("author")
                if author:
                    (person_dir / "bluesky-author.json").write_text(
                        json.dumps(author, indent=1, ensure_ascii=False))
            for item in feed:
                # Store normalized, not raw: getAuthorFeed repeats the author profile on
                # every post and inlines whole parent/root posts on replies, which pushed
                # the raw Dash timeline to 240 MB (over GitHub's 100 MB limit).
                fh.write(json.dumps(slim(item), ensure_ascii=False) + "\n")
            fh.flush()
            fetched += len(feed)
            pages += 1
            if pages % 10 == 0 or len(feed) < PAGE_SIZE:
                rate = fetched / max(time.time() - started, 0.1)
                print(f"    {fetched:,} posts ({rate:.0f}/s)", flush=True)
            cursor = d.get("cursor")
            if not cursor:
                break
            time.sleep(0.15)

    if fetched:
        lines = jsonl.read_text().strip().split("\n")

        def when(line):
            return (json.loads(line).get("record") or {}).get("createdAt", "?")

        print(f"  {handle}: {fetched:,} posts, {when(lines[-1])[:10]} → {when(lines[0])[:10]}")
    else:
        print(f"  {handle}: 0 posts")
        jsonl.unlink(missing_ok=True)
    return fetched


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="dossiers")
    ap.add_argument("--only", nargs="*")
    args = ap.parse_args()

    roster = {s: h for s, h in ROSTER.items() if not args.only or h in args.only}
    out_root = pathlib.Path(args.out)
    out_root.mkdir(parents=True, exist_ok=True)

    total = 0
    results = {}
    for slug, handle in roster.items():
        print(f"@{handle} ({slug})")
        try:
            n = collect_one(slug, handle, out_root)
            results[handle] = n
            total += n
        except Exception as e:
            print(f"  ERROR {type(e).__name__}: {e}")
            results[handle] = f"ERROR: {e}"

    (out_root / "_bsky_state.json").write_text(json.dumps(results, indent=2))
    print(f"\nDONE. {total:,} Bluesky posts collected, cost $0.")


if __name__ == "__main__":
    main()
