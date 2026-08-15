# Social media census — X and Bluesky

Handle resolution + post counts for all 30 attendees, done 2026-08-13 to size the social-collection pass (oxjob #774). User lookups cost $0.010 each (~$0.60 total for this census).

> **⚠️ Rosters diverged 2026-08-14.** This census covers the roster as it stood on 2026-08-13. The
> published attendee list has since **removed Sanmi Koyejo, Clara Collier and John Sands** (their
> dossiers were deleted) and **added Ramon Alvarado, Mahzarin Banaji and Kara Miller**, who are
> **not censused here** — their handles are recorded in their own `INDEX.md` § Social instead, and
> **no timelines have been collected for them** (X collection costs money and needs Jason's
> approval). Rows below for the three removed people are kept as the record of what was collected
> and paid for. See `00-roster.md` § "Roster history".

## Addendum — the three attendees added 2026-08-14

Censused and collected the same day, under the same rules (uniform cap N = 4,290, no keyword
filtering; Jason's approval 2026-08-14). Identity verified from first-party surfaces before any
paid call, per the method above.

| Name | X | Posts | Bluesky | Posts | Collected |
|---|---|---:|---|---:|---|
| Ramón Alvarado | @ramonalvaradoq | 2,880 | @ramonalvarado.bsky.social | 553 | **X 2,863 ($14.32, complete — under cap) · Bluesky 647 ($0)** |
| Kara Miller | @karaemiller | 4,410 | *none* | — | **X 4,290 ($21.45, at cap)** |
| Mahzarin Banaji | @banaji | **0** | *none* | — | **nothing to collect ($0)** |

**Added X spend: $35.77.** Cumulative in `_state.json` after this pass: $164.34 (that counter was
reset once when credits were topped up, so it is not the all-time total; the all-time X spend is
$242.37 + $35.77).

**Banaji's account is empty, not protected.** `@banaji` has 2,651 followers and dates from Nov
2008 but `tweet_count: 0`, `protected: false`, no `most_recent_tweet_id` — so this is the
Maher/Chan case (account exists, never used), *not* the @anildash/@FreelanceAstro case (protected,
returns an empty result that looks identical to "no posts"). **Always request `protected` alongside
`public_metrics`** — that one extra field is what separates the two, and getting it wrong records a
real corpus as legitimately empty.

**Decoys rejected this pass:** `ramonalvarado1.bsky.social` (0 posts, no bio);
`muradbanaji.bsky.social` (Murad Banaji, an Oxford mathematician); `x.com/mahzarinbanaji` and
`x.com/mrbanaji` (both 404); and for Miller, `karamiller.bsky.social` — **suspended, ownership
unknown, deliberately not attributed** — plus `karamiller1224` and `karamiller2`, empty shells.

Alvarado's and Miller's counts came from first-party pages and one $0.01 lookup each; no timeline
was fetched before identity was settled.

**Method**: X `/2/users/by` for handles + `public_metrics.tweet_count` + `created_at`; Bluesky `app.bsky.actor.searchActors` + `getProfile` for `postsCount`. Identity confirmed from display name + bio, not handle-guessing alone.

## Confirmed X accounts (20)

| Name | Handle | Tweets | Tweets/yr | Notes |
|---|---|---:|---:|---|
| Anil Dash | @anildash | 246,339 | 12,507 | extreme outlier; also 20,821 on Bluesky (free) |
| Tim O'Reilly | @timoreilly | 47,120 | 2,431 | |
| Ivan Oransky | @ivanoransky | 32,840 | 1,825 | no Bluesky |
| Katherine Maher | @krmaher | 28,886 | 1,615 | Bluesky exists but 0 posts |
| Peter Pomerantsev | @peterpomeranzev | 21,428 | 1,424 | note handle spelling: **-anzev** |
| Kenneth Cukier | @kncukier | 18,514 | 1,194 | |
| David Weinberger | @dweinberger | 18,480 | 952 | |
| Benjamin Bratton | @bratton | 11,085 | 599 | no Bluesky |
| Esther Dyson | @edyson | 8,077 | 449 | no Bluesky |
| Selena Deckelmann | @selenamarie | 4,929 | 261 | no Bluesky |
| Adam Becker | @FreelanceAstro | 3,652 | 225 | |
| Geoffrey Bilder | @gbilder | 3,003 | 152 | no Bluesky |
| Sherry Turkle | @STurkle | 2,410 | 141 | |
| Nick Vincent | @nickmvincent | 1,837 | 203 | |
| Peter Salib | @petersalib | 1,224 | 69 | |
| Sanmi Koyejo | @sanmikoyejo | 1,003 | 84 | |
| Blaise Agüera y Arcas | @blaiseaguera | 973 | 59 | display name points to Bluesky |
| Amy Brand | @amy_brand | 688 | 39 | **not** @amybrand (dormant, 0 posts) |
| James Evans | @profjamesevans | 532 | 71 | |
| Mike Caulfield | @holden | 93 | 5 | 13K followers, 93 tweets — history appears deleted |

**Total: 453,113 tweets.** Median 4,290. P80 22,920.

## Confirmed Bluesky accounts (16) — free public API

| Name | Handle | Posts |
|---|---|---:|
| Anil Dash | @anildash.com | 20,821 |
| Henry Farrell | @himself.bsky.social | 6,495 |
| Adam Becker | @adambecker.bsky.social | 888 |
| Blaise Agüera y Arcas | @blaiseaguera.bsky.social | 429 |
| David Weinberger | @davidweinberger.bsky.social | 341 |
| Nick Vincent | @nickmvincent.bsky.social | 117 |
| Tim O'Reilly | @timoreilly.bsky.social | 105 |
| Peter Pomerantsev | @peterpomerantsev.bsky.social | 75 |
| Peter Salib | @petersalib.bsky.social | 37 |
| Sherry Turkle | @sturkle.bsky.social | 27 |
| Sanmi Koyejo | @sanmikoyejo.bsky.social | 20 |
| Amy Brand | @amybrand.bsky.social | 8 |
| Kenneth Cukier | @kncukier.bsky.social | 4 |
| Katherine Maher | @krmaher.bsky.social | 0 |
| Leslie Chan | @lesliechan.bsky.social | 0 |
| Clara Collier | @claracollier.bsky.social | 0 |

**Total: 29,367 posts, cost $0.**

## No meaningful social presence found

David Krakauer, Tui Shaub, Adrian Johns, Alex Springer, Tamar Gendler, Steven Sloman, Adam Bly, Clara Collier (account exists, empty), Leslie Chan (account exists, empty), Katherine Maher on Bluesky (empty).

For these, the corpus stays on published writing / interviews / video. Absence of a feed is itself a dossier fact — several are deliberate abstainers.

## Decoys — do NOT collect these

Handle-guessing produced several confident-looking wrong people. Verify bio before pulling.

| Wrong account | Actually | Note |
|---|---|---|
| @DavidKrakauer | klezmer clarinetist | **same decoy that contaminated the OpenAlex author record** in the Krakauer pilot |
| @AdamBly | volunteer firefighter, Pennsylvania | |
| @BenjaminBratton | 8th grader | real one is @bratton |
| @amybrand | dormant, 0 posts | real one is @amy_brand |
| @Sherryturkle | "Claudia Visone", 0 posts | real one is @STurkle |
| @Jamesevans | 10 posts | real one is @profjamesevans |
| @bpbratton (Bluesky) | bacterial biophysicist | |
| @AdrianJohns | "AJ", no bio, 29 followers | almost certainly not the U Chicago historian |

## Notable

- **Henry Farrell's X account is suspended** (`User has been suspended: [henryfarrell]`). Bluesky (6,495 posts) is his only live feed. Worth knowing before the summit — and a live example of platform-enclosure risk for Session 3.
- **Mike Caulfield** has 13,116 followers but only 93 tweets — a near-complete deletion. Whatever's left is recent.
- **Anil Dash** at 12,507 tweets/yr is the pathological case for any uniform cap. His Bluesky (20,821, free, complete) is a better corpus than anything the X budget buys.

## Cost model for the X pull (at $0.005/post read, confirmed current pricing)

| Uniform cap N | Posts retrieved | Cost |
|---:|---:|---:|
| 500 | 9,593 | $48 |
| 1,000 | 18,286 | $91 |
| **1,100** | **19,789** | **$99** ← max fitting a $100 budget |
| 1,500 | 25,513 | $128 |
| 2,000 | 32,350 | $162 |
| 3,000 | 44,760 | $224 |
| **4,290 (median)** | 58,325 | **$292** |
| 10,000 | 108,421 | $542 |
| **22,920 (P80)** | 189,608 | **$948** |
| unlimited | 453,113 | $2,266 |

**The $100 budget and the "median or P80" rule are incompatible** — P80 costs ~9.5× the budget, the median ~2.9×. Only N≈1,100 fits $100.

### What N=1,100 actually reaches back to

| Person | Window at N=1,100 |
|---|---|
| Anil Dash | ~1 month |
| Tim O'Reilly | ~5 months |
| Ivan Oransky | ~7 months |
| Katherine Maher | ~8 months |
| Peter Pomerantsev | ~9 months |
| Kenneth Cukier | ~11 months |
| David Weinberger | ~14 months |
| Benjamin Bratton | ~22 months |
| Esther Dyson | ~2.4 years |
| Selena Deckelmann | ~4.2 years |
| Adam Becker | ~4.9 years |
| Geoffrey Bilder | ~7.2 years |
| Sherry Turkle | ~7.8 years |
| Nick Vincent | ~5.4 years |
| Peter Salib | ~16 years (entire) |
| Koyejo, Blaise, Brand, Evans, Caulfield | entire history |

Awaiting Jason's call on budget vs. cap — see oxjob #774 PLAN.md handoff.
