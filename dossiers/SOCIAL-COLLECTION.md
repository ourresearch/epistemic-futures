# Social collection — method and state

Companion to `00-social-census.md` (handles, counts, decoys). This file records how the
feeds were collected and where the frontier is.

> **⚠️ 2026-08-14 roster change.** The counts and spend below are the historical record of what was
> collected on the 2026-08-13 roster — left intact, since the money was spent. But **Koyejo,
> Collier and Sands are no longer attendees and their dossiers (including Koyejo's `social/`
> directory of 1,003 X posts and 20 Bluesky posts) were deleted** — recoverable from git history,
> so restore rather than re-buy if he ever reappears. **Three new attendees have no social corpus
> at all**: Ramon Alvarado, Mahzarin Banaji, Kara Miller. Collecting them would cost money on X
> and $0 on Bluesky — **Jason's decision, not an agent's**. See `00-roster.md` § "Roster history".

## Method

**No keyword filtering.** Jason's ruling, 2026-08-13: filtering at the camera-raw stage
bakes in a compression bias later passes can't undo. The only reduction is a **uniform
recency cap** — the same N most-recent posts for everybody, which insulates the method
from outliers like @anildash (246k posts). The only bias it introduces is more recency
skew for prolific people, which is the accepted trade.

Cap set to **N = 4,290** — the median post count across the 20-account X roster.

Retweets, replies, and quote-posts are all kept. Voice is the payload; a retweet is a
signal about what someone amplifies.

Scripts: `scripts/collect_x.py`, `scripts/collect_bluesky.py`. Both resumable.

## Bluesky — COMPLETE, 57,259 posts, $0

Free public API, so no cap was applied: every account pulled in full.

| Person | Posts |
|---|---:|
| Anil Dash | 44,200 |
| Henry Farrell | 10,112 |
| Adam Becker | 1,199 |
| Peter Pomerantsev | 504 |
| Blaise Agüera y Arcas | 451 |
| David Weinberger | 362 |
| Tim O'Reilly | 160 |
| Nick Vincent | 132 |
| Sanmi Koyejo | 54 |
| Peter Salib | 40 |
| Sherry Turkle | 27 |
| Amy Brand | 10 |
| Kenneth Cukier | 8 |

Note the count is ~2× the census estimate because `postsCount` undercounts what
`filter=posts_with_replies` returns (replies and reposts).

Two accounts matter disproportionately and are **free**:
- **Anil Dash** — 44,200 posts here vs. 246k on X. This is the better corpus, at no cost.
- **Henry Farrell** — his X account is **suspended**; Bluesky is his only live feed.

Katherine Maher, Leslie Chan, and Clara Collier have Bluesky accounts with 0 posts. They
stay in the roster so a later run picks them up if they start posting before the summit.

## X — COMPLETE, 47,253 posts, $242.37 total

Every reachable account collected. Three runs, the first two stopped by billing walls:

1. 4,460 posts (~$22) → **HTTP 402 `credits depleted`** (balance).
2. +18,301 posts (~$92) → **HTTP 403 `monthly spend cap reached`** — a *separate* per-cycle
   ceiling (~$115) that adding credits does not raise. Set at console.x.com → Billing.
3. +25,714 posts (~$129) after the cap was raised → **done**.

| Person | Handle | Posts | Status |
|---|---|---:|---|
| Ivan Oransky | @ivanoransky | 4,290 | at cap |
| Tim O'Reilly | @timoreilly | 4,290 | at cap |
| Esther Dyson | @edyson | 4,289 | at cap |
| David Weinberger | @dweinberger | 4,286 | at cap |
| Benjamin Bratton | @bratton | 4,285 | at cap |
| Peter Pomerantsev | @peterpomeranzev | 4,285 | at cap |
| Katherine Maher | @krmaher | 4,282 | at cap |
| Kenneth Cukier | @kncukier | 4,281 | at cap |
| Geoffrey Bilder | @gbilder | 3,249 | complete |
| Sherry Turkle | @STurkle | 2,415 | complete — back to 2009-08 |
| Nick Vincent | @nickmvincent | 1,825 | complete |
| Peter Salib | @petersalib | 1,223 | complete |
| Selena Deckelmann | @selenamarie | 1,015 | complete — see below |
| Sanmi Koyejo | @sanmikoyejo | 1,003 | complete |
| Blaise Agüera y Arcas | @blaiseaguera | 973 | complete |
| Amy Brand | @amy_brand | 685 | complete |
| James Evans | @profjamesevans | 528 | complete |
| Mike Caulfield | @holden | 49 | complete |
| Adam Becker | @FreelanceAstro | — | **PROTECTED — unobtainable** |
| Anil Dash | @anildash | — | **PROTECTED — unobtainable** |

Eight accounts hit the 4,290 cap, meaning their timelines extend further back than we
bought. Everyone else is a complete history.

### Two accounts are protected, and Bluesky covers both

`@FreelanceAstro` and `@anildash` are private accounts (`protected: true`) — their
timelines are not retrievable via the API at any price, by anyone who isn't an approved
follower. Cost: **$0**, because the API returns an empty result rather than an error.

This is the happiest possible version of that problem: **both are among our largest free
Bluesky corpora** (Dash 44,200; Becker 1,199). Dash's own bio says "find me on
mastodon/bluesky/threads." The $21 we'd have spent on four months of his X bought nothing
and needed to buy nothing.

### Selena Deckelmann's 1,015 vs. a claimed 4,929 — resolved, not a gap

Verified as genuine sparsity, not truncated pagination: the collection spans her whole
account life (2009-04-28 → 2024-07-15), and a tweet found by an independent probe of an
older window is already in our file. **990 of the 1,015 are from 2009**, with near-silence
2010–2019 — she appears to have deleted most of a decade. `public_metrics.tweet_count`
counts deleted posts, so 4,929 was never reachable.

**General lesson: `tweet_count` is an upper bound, not a target.** Don't treat a shortfall
against it as a collection failure without checking the date span first.

### Collector bugs these runs exposed (all fixed)

- **Empty first page was treated as success.** A protected account got `complete: true` and
  would have been silently skipped on every future resume — its absence quietly becoming a
  "fact" about the corpus. Now compared against the census count and flagged
  `suspect_empty`. This is what caught both protected accounts.
- **Billing walls were treated as per-account errors.** A 402/403 is account-level, so the
  script ground through the whole remaining roster collecting one identical error each. Now
  raises `BillingWall` and aborts with the fix instructions.
- **At-cap accounts looked unfinished.** Pagination stops when the remaining allowance falls
  below the API's 10-result minimum, so a capped account lands a few short (4,289 of 4,290).
  A resume read that as incomplete and would have re-bought Dyson's and Bratton's entire
  timelines — **~$43 wasted**. Now marked `capped`; the skip was confirmed working on run 3.
- **Summary labelled everything non-`complete` as "(capped)"**, including protected and
  errored accounts. Now prints the real status.
- **`spent_posts` is cumulative across runs.** Reset it to 0 when adding fresh money, or the
  new ceiling is silently reduced by prior spend.

## Fidelity notes

- `search/all` returns fewer posts than `public_metrics.tweet_count` (Caulfield: 49
  retrieved vs. 93 claimed). The gap is deleted/protected content. Not a collection bug.
- `search/all` **silently returns zero results without an explicit `start_time`** — the
  script pins it to 2006-03-21 (Twitter's first tweet). A future maintainer who drops
  that parameter will get an empty corpus and no error.
- Storage is raw API JSON, one object per line, in `dossiers/<slug>/social/`. Lossless on
  purpose: later passes summarize along different axes, so nothing is pre-digested here.
