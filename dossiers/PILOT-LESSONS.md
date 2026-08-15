> **Historical method log** (2026-08-13/14), kept as written. It occasionally refers to an `about/`
> section (third-party coverage) that was part of the working layout at the time and is **not part of
> this repository** — the corpus here is each person's own words only.

# Pilot lessons (running log)

Feed these into CONVENTIONS.md before the full fan-out. One section per pilot as reports arrive.

## Pilot 1: david-krakauer (completed 2026-08-13; ~20 min, 65 tool calls)

**Output**: 138 by/ (61 full-text, 70 abstract-only, 7 book-summary), 6 about/, 23 video noted. 2.3MB. Spot-check: frontmatter + content-labeling conform.

**Conventions ambiguities the agent hit (with proposed resolutions):**
1. **Free-ebook books** (SFI Press gives whole books away): conflicts between "books → summary" and "openly available → full text". Proposed: extract author-written front matter (preface/intro) as full-text items + keep book summary item; whole-book extraction only on request.
2. **Joint interviews** (two attendees interviewed together — e.g. Krakauer + Melanie Mitchell): saved to his by/. Proposed: save once, cross-link from the other person's INDEX.md if they're also an attendee.
3. **"Rough transcripts"** published by podcast hosts: treated as official text → by/ talk-transcript with a notes caveat. Codify.
4. **Abstract-only baseline for the full OpenAlex record**: agent bulk-wrote abstract-only files for every scholarly work ≥2005 (cheap, valuable). Make this the standard recipe, not just an index listing.
5. **Truncation**: no cap existed; agent used 400KB with explicit `[TRUNCATED]` marker + note. Codify (400KB + marker).
6. **Scratchpad collisions**: 28 parallel agents sharing one scratchpad will collide on venvs/downloads. Each agent must use a uniquely-named subdir/venv (e.g. `venv-<slug>`).

**Technique notes that worked:** OpenAlex author record as scholarly backbone (contaminated satellite author ID detected + excluded — klezmer clarinetist); full crawl of personal site resolved to canonical URLs; Wayback Machine beat bot-blocking for Aeon; PMC/EuropePMC/arXiv/PLOS for OA full text.

**Krakauer-specific frontier (recorded in his INDEX.md):** SFI Press free ebooks not pulled (his prefaces = biggest remaining by/ text); ~15 works with no abstract or OA text; pre-2020 essay archive (SFI Bulletin, Edge.org) not enumerated; The Transmitter JS-gated.

## Pilot 2: ivan-oransky (completed 2026-08-13; ~27 min, 121 tool calls)

**Output**: 53 by/ (36 full-text, 9 excerpt, 8 abstract-only), 3 about/ (+5 found-but-blocked pending), 6 video noted. Plus the index-first layer: **3,178 rows enumerated in sidecar TSVs** — all 2,338 Retraction Watch posts under his byline (2010–2026), all 455 Embargo Watch posts, all 104 STAT pieces, all 277 OpenAlex works (A5022367451, disambiguated via Simons/CSI/NYU).

**Conventions ambiguities (with proposed resolutions):**
1. **Mega-prolific enumeration overflows INDEX.md**: agent put full enumerations in sidecar TSVs at dossier root (`rw-post-index.tsv` etc.), referenced from INDEX. Bless this pattern (INDEX items table = fetched items only; TSVs = full enumeration).
2. **Complete text openly distributed in Crossref/OpenAlex abstract metadata** (2 paywalled editorials whose full text IS the "abstract" field): labeled `content: full-text` + explanatory note. Bless: label by what the text actually is, note the odd provenance.
3. **Openly posted copies of paywalled pieces** (e.g. NYT op-ed PDF on a professor's course site): treated as fetchable, provenance noted. Bless with care: copy must be openly reachable, provenance always in notes.
4. **Minor-author co-authored works**: no threshold in conventions; agent included when relevant. Proposed: include in abstract-only baseline regardless (it's cheap); prioritize full-text fetch only when the person is a lead/senior author or the piece is summit-relevant.
5. **Joint Q&As / roundtables**: filed in by/ per "voice is the payload". Codify.

**Technique notes:** WordPress author-ID archives = reliable byline enumeration; Wayback was 503-down the whole pass (retry later — it unlocks ~10 pending upgrades); RW institutional posts moved to a "staff" byline ~2025 (105 staff posts to skim next pass).

**Oransky-specific frontier (in his INDEX.md):** Wayback retry list (BMJ 2023, Science 2024, AMA J Ethics, 7 STAT excerpts→full, Science 2018 + Chronicle profile for about/); WaPo 2024 hard-paywalled; RW staff-byline posts since 2025 unskimmed.

## Pilot 3: jason-priem (calibration; completed 2026-08-13; ~63 min total incl. a self-spawned blog sub-agent + one resume nudge)

**Output**: 181 by/ (174 full-text — he's an OA advocate, it shows; 5 abstract-only, 1 excerpt, 1 summary-only), 11 about/ (all full-text: Nature ×5, Chronicle ×2, Science, TechCrunch, SPARC, Poynder), 21 video. All 192 files passed frontmatter/label validation.

**✅ CALIBRATION PASSED — Jason graded it 2026-08-13: "My dossier looks perfect. No notes."** He is the one person whose corpus ground truth he can check directly, so this validates both recall and precision of the collection method. **The conventions are approved as-is and the fan-out is GO** — no method changes required before scaling to the remaining attendees.

**Recall wins:** Wayback-archived self-archive (jasonpriem.org/self-archived/) recovered closed 2008/2010 papers as green-OA full text AND surfaced two workshop papers missing from his OpenAlex author profile (SePublica 2012, altmetrics12); `raw_author_name.search` sweep confirmed no other missed works. (Also a product-bug breadcrumb: those two missing works might be worth a look in the AER pipeline.)

**Conventions ambiguities (with proposed resolutions):**
1. **Paywalled-now, open-then**: live-paywalled pieces fully readable in Wayback snapshots → saved `content: full-text` + note. Bless (consistent with Oransky lesson 3: openly reachable copy counts, provenance in notes).
2. **Non-verbatim "interview"** (GiveWell-style conversation notes = paraphrase): keep `type: interview` + explicit paraphrase flag in notes. Codify.
3. **Unofficial community transcripts**: brief said official-only; agent kept one in by/ flagged. Proposed: allow, flagged `notes: "unofficial community transcript"` — it's still his words, and the flag preserves caveat.
4. **Corpus-summary table has no `excerpt` column**: add one (or rename column "not-full-text").
5. **Trivial full-text items** (photo-caption blog posts): `content: full-text` is technically true; fine — no rule change, but INDEX may flag trivial items.

## Decisions locked (2026-08-13, from Jason)
- **PDFs**: text-only extraction stays; no binaries in git. `source_url` + Wayback = re-fetch path.
- **Open books**: fetch the ENTIRE book as full text (exempt from truncation cap); closed books stay summary+excerpts. → CONVENTIONS.md updated.
- **OpenAlex Content API added to the fetch chain** (check first: `/works/<id>/content` → `content_urls` on content.openalex.org, prefer grobid_xml; partial coverage, fall back to landing/PMC/pdf_url). → CONVENTIONS.md updated. NOTE: pilots did NOT use this path — a later upgrade pass could re-probe their abstract-only items against it.

## Upgrade pass lessons (2026-08-13, Content API re-probe)

- **Content API works as a recall lever**: krakauer 20/70 abstract-only items upgraded to full text (all via grobid_xml; PDF fallback never won), priem 3/5. ~932KB new prose for Krakauer alone.
- **Serving gotcha 1 (possible product bug — flag to OpenAlex eng)**: `content.openalex.org/...grobid-xml` responses are gzip bytes (`\x1f\x8b`) with NO `Content-Encoding: gzip` header — clients must sniff and gunzip manually.
- **Serving gotcha 2**: two grobid format vintages in the wild — standard TEI, and lowercase-TEI-wrapped-in-`<html><body>` with divs off `{tei}text` (no body element). Extractors must handle both.
- **SFI Press free books blocker**: all 7 Krakauer books have genuine $0 PDF editions but the ONLY delivery is a Squarespace cart checkout collecting an email ($0 order). Needs Jason's go-ahead to submit with his email; 2-min recipe recorded in his INDEX.md coverage notes.
- **Serving gotcha 3 (MORE serious — escalate): `has_content: true` ≠ usable text.** In the Oransky pass, 3 of 4 content.openalex.org files that claimed content were unusable: W4400054728 (zlib-corrupt text streams, 13 pages → 0 chars), W4390734332 (PDF page tree corrupt, "root has no /Kids array"), W2190159833 (grobid+PDF both extract as garbled encoded-font glyphs). Re-downloads byte-identical → corruption is server-side (stored), not transit. pdfminer/pypdf/pymupdf/pikepdf-repair all fail. Consumers must treat has_content as "maybe" and validate extraction output.
- **Wayback = confirmed working route for STAT's paywalled back catalogue** (snapshots carry complete articles, not lede-only) — relevant for several attendees who write for STAT.
- Oransky post-pass state: by/ 47/53 full-text (was 36), about/ 5/5 full-text. 12/12 frontier Wayback recoveries + 1 bonus.

---

# Fan-out lessons (2026-08-13, 30 attendee corpora)

The 30-dossier fan-out ran as ~30 parallel agents, each given a distilled operating brief built
from CONVENTIONS.md + the three pilots above. What follows is what they collectively learned.
**Sections 1–2 are rulings that should be folded into CONVENTIONS.md; 3–5 are technique;
6 is for OpenAlex eng, not for the corpus.**

## 1. Conventions gaps needing a decision (raised independently by ≥1 agent)

- **The `content:` enum needs a value for "record exists, no text anywhere."** Three agents
  independently invented `metadata-only`; a fourth used `record-only`. Some works have neither an
  abstract nor any reachable copy, so the blessed "abstract-only baseline for every work" recipe
  yields a hollow file. **Two agents instead left them out of `by/` and recorded them in the
  sidecar TSV** — cleaner, and consistent with "only save text you actually retrieved". *Decide:
  new enum value, or TSV-only.*
- **Open-book rule vs. the 2005 window.** *The Cluetrain Manifesto* (2000) is fully open. Proposed:
  **the open-book rule overrides the time window** — a freely available whole book is exactly what
  the corpus wants regardless of date.
- **Where does a CV go?** Two agents split: `by/` item (`type: cv`) vs. dossier-root sidecar
  (`cv.md`, `section: reference`). Unresolved. Whichever wins, **"fetch the CV/bibliography page
  first" should be a standard step for every academic** — it was the single most valuable
  discovery artifact on at least four dossiers, and repeatedly listed works OpenAlex lacked.
- **`type:` additions used in practice**: `talk-slides`, `thesis`, `dissertation`, `cv`,
  `newsletter`. **Length exemption should read "book-length works", not "books"** (a 688 KB
  dissertation was exempted on the book rationale).
- **Corpus-summary table** needs `excerpt` and `metadata-only` columns (pilot 3 already asked).

## 2. Blessed rulings from the fan-out

**Whose voice is it — the rule that protects the downstream simulation**
- **Person as *interviewer*** → `by/` (their questions and framing are their words), flagged.
- **Interview *format* → `by/`; quoted-source article → `about/`**, decided by format, not quote
  density, and **regardless of how the subject's own site labels it**.
- **Multi-guest transcripts / multi-contributor roundups**: save **only the person's segment** as
  `content: excerpt`, noting the rest is other people's words. Saving the whole thing injects
  other voices into a corpus that feeds character simulation.
- **Institutional statements** go in `by/` **only** when attributed to or signed by the person.
- **Collective bylines** ("The Editors"): admissible when other issues are individually bylined,
  but `authors:` must carry the collective name, never the person's, with the published byline
  recorded in `notes:`.
- **Unbylined-but-claimed authorship**: the hedge belongs in the **`authors:` field**, not only in
  `notes:` — downstream reads `authors:` as fact.
- **Sole-public-author organisations** are a carve-out: unbylined org documents are admissible to
  `by/` when the org demonstrably has one public author (contrast: a 49-person foundation's
  unbylined doc stays out).
- **Group-authored declarations/manifestos** the person co-authored → `by/`, relationship stated
  in `notes:`; never fabricate a byline, and never assert a role the source doesn't support.
- **Book reviews written BY the subject** → `by/` `type: review`; `about/` is for reviews *of*
  them.

**What counts as text**
- **Always check for an official transcript before consigning anything to `video.md`.** Big Think,
  TED (`__NEXT_DATA__` → `props.pageProps.transcriptData…`), Open Yale Courses and many podcasts
  publish one. On one dossier this converted 18 "video notes" into ~74 KB of primary text.
- **Author-posted machine transcripts** (an explicitly "unedited Gemini transcript") → `by/` with
  an ASR caveat. Extends the pilot-3 unofficial-transcript ruling.
- **Slide decks**: `content: full-text` when extraction gets the whole deck (with a caveat that
  images/diagrams aren't represented), `excerpt` when image-only.
- **A post whose payload is a video embed** → `video.md`, not `by/`, however much stub text
  surrounds it. **Image-only posts** likewise get no file, just an INDEX row.
- **Book reissues carrying new author material re-enter the fetch window**, dated to the reissue.
- **Openly posted book-preview PDFs** (front matter + endnotes, no body) are `excerpt` items —
  **not** grounds to call the book open.
- **Reprints/translations of pre-window originals**: keep (publication year is in-window) but
  record the composition date in `notes:` so the reprint year isn't read as when it was written.
- **Reprint chains and preprint/VOR pairs**: one copy wins (VOR / longest extraction); the other
  gets a cross-pointer, so a summarizer can't double-count.
- **Cross-posted duplicates** (same essay on Medium + blog + LinkedIn): keep one, note the other
  locations, **dedupe as you go** — one dossier had to delete ~45 files retroactively.
- **Liveblogs** (notes taken during someone else's talk) stay in `by/` with a caveat separating
  summarized speaker content from the person's own commentary.
- **Author-hosted republication archives** ("used with permission") count as openly reachable.

**Boundaries**
- **Pirate ebook sites are OUT.** "Openly reachable copy" means author sites, course sites,
  publisher excerpts and Wayback — not unauthorized upload sites.
- **Browser-rendered ≠ saveable.** Rendering a paywalled article doesn't make reproducing it
  appropriate; prefer a labelled `excerpt` + canonical `source_url`.
- **PII**: redact personal phone numbers etc. from otherwise-public primary documents, and say so
  in `notes:`.
- **Advisor-on-dissertation is not authorship** (MARC records list committee members in the author
  field). **Supplementary-file deposits** (figure captions, prompt lists) are not writing.
- **Unbylined newsletters**: fetchable but unattributable → don't save.
- Thin-footprint subjects: **institutional staff bios are admissible to `about/`** when flagged —
  sometimes they are the entire about-them record. An honest small corpus beats a padded one.

## 3. Discovery — what actually worked

1. **The person's own CV / bibliography page beats everything**, including their OpenAlex record.
2. **WordPress REST API (`/wp-json/wp/v2/`)** is the best enumerator in the playbook.
   `users?search=<name>` is a one-call definitive byline test; category/taxonomy IDs separate a
   person's own posts from press releases quoting them; and it returned *complete* archives with
   full text in one sweep (1,644 and 1,075 posts on two dossiers, no Wayback needed). JS-SPA blogs
   often have one underneath — grep the bundled app JS for `fetch("`.
3. **Rogue Scholar blog-DOIs (`10.59350` / `10.59347`) in an author record reveal unlisted blogs.**
   On one dossier this surfaced the most summit-relevant writing in the corpus.
4. **`raw_author_name.search` sweeps recover works missing from author profiles** — on five
   dossiers now, including one person's *most-cited in-window work*. Accented and unaccented
   spellings return **different** result sets.
5. **Companies House** is a first-class identity oracle for UK subjects (no API key).
6. **iTunes Search API** enumerates podcast appearances without web search.
7. **DSpace 7** stores a plain-text derivative of PowerPoint-only deposits at
   `/server/api/core/bitstreams/{uuid}/content`.
8. **GreaterWrong** mirrors LessWrong, which bot-walls curl *and* `r.jina.ai`.
9. **Substack**: `/api/v1/archive` enumerates, but bodies often must come from post HTML, and an
   archive can be **radically incomplete** when the newsletter mirrors a static site (23 vs 50).

## 4. Extraction — the failure modes that look like success

**The theme: statistical checks (length, alpha ratio) pass all of these. Use structural checks.**

- **Wrong document, clean prose.** See §6 — the detector that works is a **title-content-word
  overlap check against the first ~1,200 chars**.
- **Landing pages** masquerade as full text (one was a 1.1 MB dblp month listing).
- **Cloudflare interstitials** ("Just a moment…", ~5.8 KB, ~0.8 alpha) were briefly saved as full
  text on one dossier. **Paywall stubs** likewise. Sniff for `<!doctype` / `<html` /
  "Just a moment" / "Enable JavaScript", and delete sub-~1.2 KB "articles".
- **Wayback replay chrome** ("N captures / Alexa Crawls / Sign In") contaminates extracted text and
  can make a subscription wall look like an article — use the `id_` replay form.
- **Scanned-image PDFs.** On one dossier **58 of 60** author-hosted PDFs were scans; `pdftotext`
  returned 1–30 bytes and they looked "fetched but empty". **Assert extracted length > ~500 bytes**
  and fall back to OCR (a ~40-line Swift binary using PDFKit + `VNRecognizeTextRequest` compiled
  with the stock `/usr/bin/swiftc` did all 58 at 10–60 s each). Record the OCR engine in `notes:`.
- **`pdftotext` silently returns 0 chars** on Word→pdfHarmony PDFs with non-embedded fonts;
  `pymupdf` handles them. Distinct from genuinely un-OCR'd page images.
- **grobid_xml beats PDF — except for transcripts**, where grobid drops speaker labels and the
  PDF's layout carries the attribution.
- **Literal `\n` inside OpenAlex titles** defeats title-normalizing dedup (leaves a stray `n`
  token); strip it before normalizing, and follow up with a fuzzy near-match sweep.

## 5. Access — bot walls, and what beats them

- **⚠️ `content.openalex.org` REQUIRES the Bearer token on the content fetches, not just on the
  `/works/<id>/content` metadata call.** Unauthenticated fetches **429 forever**, which reads as
  rate-limiting and provokes a useless backoff loop. One agent lost ~20 min; once it added auth,
  **40 of 41 candidates returned usable text on the first try.** *This likely suppressed full-text
  recovery across much of this fan-out — a re-probe pass over `abstract-only` items is warranted.*
  Also: the content URL must come from `content_urls` in the response —
  `content.openalex.org/works/<id>.grobid-xml`, **not** a hand-built `/works/<id>/grobid-xml`.
- **Wayback** (it was the binding constraint all run, partly self-inflicted with ~30 agents on one
  IP): 503s are **transient** — retry 3–8× with backoff. **`curl --compressed` breaks it** (empty
  body). **Parallel workers are counterproductive** — 4 concurrent gave 100% failures where 1
  serial worker at ~60 s pacing succeeded. **`archive.org/wayback/available` under-reports** vs the
  **CDX API**. Resolve a full **14-digit** timestamp — bare-year forms return a 107-byte stub. Use
  `id_` for PDFs (`if_` can return 0 bytes). Large `matchType=domain` CDX crawls time out.
- **`r.jina.ai` is now 403/API-key-gated — treat as dead.** When it worked it also served **stale
  cached WRONG pages**; any use needs a returned-`Title:` check.
- **Full browser header sets on plain `curl`** (`Sec-Fetch-*`, `Accept-Language`,
  `Upgrade-Insecure-Requests`, real UA) defeat many Cloudflare 403s.
- **bepress / Digital Commons** `viewcontent.cgi` returns HTTP 202 + zero bytes to plain curl, but
  serves the PDF if you prime a cookie jar from the landing page, then request with that jar +
  `Referer` + full headers. Unlocked six repositories on one dossier.
- **SSRN**: Cloudflare-walled to curl, WebFetch and jina. The challenge fires on `fetch()`/XHR but
  **not on iframe navigation** — same-origin hidden iframes work.
- **figshare**: `ndownloader.../files/<id>` answers GET with a WAF challenge but HEAD with a 302 to
  a **10-second** signed URL. HEAD → grab `Location` → GET immediately.
- **Knight-style Cloudflare email obfuscation**: addresses render as `[email protected]` and are
  absent from raw HTML; decode the `data-cfemail` hex (`k=int(h[:2],16);
  chr(int(h[i:i+2],16)^k)`). This is what confirmed one attendee's identity.
- **⚠️ `WebFetch` is an ENUMERATION tool, not a capture tool** — it paraphrases and refuses verbatim
  reproduction, so it can never supply corpus text.

## 6. OpenAlex product breadcrumbs (for eng — NOT corpus problems)

This fan-out is an unusually good real-world dedup/quality test set: ~30 known people, each
hand-verified against their own CV and institutional pages.

**Content API — a third and fourth failure mode beyond #779 (gzip header) and #780 (truncation):**
- **Wrong document stored, extracting as clean prose — 6 cases across 4 dossiers.**
  `W4312089995` ("Data blind", *Science*) → an AI-in-education report; `W3015307286` /
  `W3015682900` / `W3016062778` (French *Le Stack* chapters) → an FTC IoT report, a MIRI paper, a
  software-ecosystems paper; `W4411364750` ("AI as Governance") → Morucci & Spirling in **both**
  `.pdf` and `.grobid-xml`; `W7115064348` → an entire journal issue. **The #780 "does it read as
  prose?" validation cannot catch this class.** Working detector: require a majority of the work's
  **title content-words in the first ~1,200 chars** (10/16 scored 5+, the two bad ones scored 0).
- **Index/storage divergence**: `W4387822650` reports `has_content.grobid_xml: true` but fetching
  500s with *"in the content index but missing from storage"* (its PDF is fine). `W2981496525`'s
  grobid-xml URL 404s despite the same flag.
- Stored-corruption (#780) reproduced on `W2319982006`, `W2103432602`.

**Author-record splintering and contamination — systematic, on nearly every scholarly dossier:**
- **Contamination despite a clean ORCID**: `A5076633756` (James Evans) mixes in ≥8 other James
  Evanses; 57 post-2005 works excluded by hand.
- **No usable canonical record at all**: Mike Caulfield is fragmented across ≥8 IDs and the *most
  prominent* record under his exact name (`A5002731625`) is a different person. Nick Vincent's
  **both** SFU-affiliated IDs are merges with a **medieval historian at UEA**.
- **Three people merged into one ID**: `A5019390874` (Weinberger + an OFDT drug-policy researcher +
  a Helmholtz nuclear physicist).
- Splinter counts: Bilder ~24 (and his **ORCID resolves to a different, near-empty ID**), Salib 9,
  Sloman 8, Chan 8+, Koyejo ~50 fragments among 113 same-surname records, Agüera y Arcas 8.
- **A byline parsed into a person**: `A5049130406` = *"Steven Sloman amp Fernbach"* — an HTML-entity
  leak.
- **Genuine splinters left unmerged** while wrong works are merged in (e.g. Gendler's real 1989–90
  RAND papers sit in a separate ID).

**Affiliation matching:**
- `"System, Inc"` → **University of Louisiana System** (propagates to 5 co-authors).
- `"University of Toronto Scarborough"` → **The Scarborough Hospital** — this bogus healthcare
  affiliation is precisely what makes a clinical-namesake collision look plausible.
- Spurious `last_known_institution`s asserted nowhere in the person's biography: **Central
  Intelligence Agency** (Agüera y Arcas), **Tianjin University of Science and Technology** (Johns),
  **University of Haifa** (Gendler), **Martin Luther King, Jr. Multi-Service Ambulatory Care
  Center** (Salib), **Twin Cities Orthopedics** (Hecht), *Institut des Sciences Cognitives* /
  *Hologic (Germany)* (Sloman).

**Metadata:**
- **Works missing from author profiles, recovered by name sweep — on 5 dossiers**, including
  Weinberger's most-cited in-window work (`W2765811634`, 79 cites) and `W4389141708` (Brand). Same
  pattern as the priem calibration: a possible AER-pipeline signal.
- **Title/DOI mismatch**: `W4387355345`'s display_name belongs to a different paper than its DOI,
  abstract, authors and PDF.
- **Reviews attributed to the reviewed author** (`W7165111317`).
- **Chapters credited to a volume's editors** instead of their real authors (3 Gendler records are
  chapters by Chalmers, M.G.F. Martin, et al.).
- ~26 ACM titles truncated at the colon; 43 items missing venue; 3 ICWSM papers mis-dated 2021 via
  the AAAI re-hosted archive; a Gemma-2 mass-authorship false positive.

## 7. Operational notes for the next fan-out

- **Concurrency cap is 20 subagents**, and agents self-spawn children — launch in batches and
  refill from a queue rather than firing 30 at once.
- **WebSearch has a session-wide ~200-call budget shared by all agents.** It was exhausted partway
  through, and it is **the single biggest cap on `about/` recall** across the later dossiers —
  nearly every agent named it as their main gap. Structured enumeration is more complete *and*
  cheaper; save searches for what only search can find. DuckDuckGo via the browser works for a few
  queries then CAPTCHAs; Bing returns unrelated locale results; Mojeek returns empty.
- **The claude-in-chrome tab is shared.** Agents navigated each other's tabs out from under them at
  least twice, and one lost 26 scraped records held in a `window` var when its tab was reaped.
  Create your own tab, pass only your own `tabId`, and **never accumulate state in the browser**.
- **If an agent self-spawns per-surface workers, they must WRITE ONLY and never restore deleted
  files; the lead dedupes once at the end.** One agent's workers and its own dedupe fought for four
  rounds over seven files.
- **Google Books API** is quota-exhausted for this project (429, per-day limit 0).

---

# Cleanup-pass lessons (2026-08-14)

## 8. The Content API re-probe: measure the candidate set before believing a rate

The fan-out handoff called the authed Content API re-probe "likely the single biggest recall win
available," on the strength of one agent going **40 of 41** after it added the Bearer token. Run
corpus-wide, the pass upgraded **13 items**.

The auth finding itself is correct and worth keeping (see §5): `content.openalex.org` requires the
token on the **content fetch**, and returns 429 rather than 401 without it (oxjob #787). What was
wrong was the inference. That agent's 41 candidates were **already screened to `has_content: true`**;
the 40/41 was a *conversion* rate on known-good candidates, not a *recovery* rate over
abstract-only items. Screening all 548 abstract-only items (539 with work ids) against
`select=id,has_content,content_urls`:

| | |
|---|---|
| have stored content at all | **18 / 539** (3.3%) |
| of those, already-filed #786 wrong-document cases | **6** |
| additionally have a `best_oa_location.pdf_url` | 25 |
| upgraded to full text after validation | **13** (+1.05 M chars) |

**The generalizable lesson: a rate quoted from a filtered sample will be read as a rate over the
population unless the filter is stated.** One line in the handoff — "of candidates that already
had `has_content: true`" — would have set the expectation correctly. When recording a recall
result, record the denominator.

Cheap screening technique worth reusing: `has_content` and `content_urls` are selectable on the
plain `/works` endpoint, so **50 works screen in one call** — there is no need to hit
`/works/<id>/content` per item just to find out whether content exists.

## 9. Validation guards that earned their keep

Running all four guards over 43 fetch candidates, the failures broke down as: 7 wrong-document
(#786), 4 zero-char scanned PDFs, 2 stored-truncated (#780), 9 landing-page-instead-of-PDF,
8 hard 403s, 2 legitimately-short-but-valid.

- The **#786 title-overlap check** (a majority of the work's title content-words present in the
  first ~1,200 chars) caught **one case not previously filed** — and it is the only guard that
  can, since all seven fetched as long, clean, high-alpha prose. Length and alpha ratio pass them
  all.
- **It is weakest on non-English and accented titles.** Four of the seven were French *Le Stack*
  chapters whose content words are short and accent-bearing; a human read of the first paragraph
  is the authority there, not the score.
- **A low char count is not a failure signal.** Two items scored a *perfect* title overlap at
  ~800 chars: a Publisher Correction and a one-page comment, which genuinely are that short. Any
  minimum-length threshold will reject real items — pair it with the overlap score before
  discarding.

## 10. Access recipes the cleanup fan-out earned (2026-08-14)

**The single most valuable one: when a publisher 403s, go to Wayback for the publisher's own
free HTML — not for the PDF.** Wiley, OUP, Taylor & Francis, PNAS, AIP/Scitation and the Royal
Society 403 every non-browser client **even with a full browser header set**, because Cloudflare
fingerprints the **TLS handshake**, not the headers. §5's header and cookie-jar recipes cannot
win there and grinding on them is wasted time. What works:

- **Wayback captures of the legacy HighWire/Scitation HTML full-text URL.** The *PDF* URLs
  typically have **zero** captures while the *HTML* ones have dozens. This converted 4 "hopeless"
  items on one dossier, 5 on another and 8 on a third.
- **PMC/EuropePMC JATS via NCBI efetch** — but note `db=pmc` sometimes returns front matter plus
  *"publisher does not allow downloading of the full text in XML form"*; the PMC article **HTML**
  still carries the body.

**⚠️ Wayback `id_` replay returns gzip bytes with no `Content-Encoding` header on many hosts** —
the identical trap to `content.openalex.org` grobid (#779). One agent had **five of eight**
captures come back as mojibake until it sniffed for `\x1f\x8b` and gunzipped manually. This very
likely produced silent failures in the first fan-out that were read as "the capture is garbage."
Always sniff the magic bytes before deciding a capture is unusable.

**Other Wayback mechanics that decided outcomes:**
- **Try more than one capture before calling a URL gone.** Some replay as a few-hundred-byte
  bot-wall page ("Request unsuccessful", Incapsula) while *adjacent captures of the same URL* are
  perfect — including, on one dossier, the exact timestamp a previous pass had recorded before
  writing the URL off.
- **Match the CDX `length` field against the real file size.** A 1 MB capture of a 6 MB PDF is a
  truncated store that extracts to nothing.
- **Never run CDX/availability queries concurrently with the replay fetcher** — connection
  failures and a 429. Do one, then the other.
- Some Wayback-captured PDFs are truncated at the byte level with an invalid xref (neither
  `pdftotext` nor PDFKit opens them); a capture from a different year of the same URL usually is not.

**Enumerators that beat both search and Wayback:**
- **Google News RSS** (`news.google.com/rss/search?q=...`) — free, unauthenticated, and it
  out-performed every WebSearch call one agent made for `about/`. Links are JS-obfuscated;
  recover real URLs via Wikipedia `insource:"<title>"` or by matching the headline on the outlet.
- **`news.<university>.edu/profile/<name>`** carries a reverse-chron list of every campus-news
  story about a faculty member (confirmed on UChicago).
- **A dead publication's successor site may hold the whole back catalogue, live.** The Monkey
  Cage's complete archive — 853 posts including the entire Washington Post era — is on
  `goodauthority.org` under a `news` custom post type, reachable by plain curl. Wayback had only
  ~40 of those posts. **Check for a successor site before mounting an archival recovery.**
- **Google Patents** serves a full patent spec and claims as clean HTML
  (`<section itemprop="description">`), so patents never need OCR.
- **iTunes Search API + `<podcast:transcript>` enclosures** resolves a whole `video.md` to
  known-has-transcript / known-hasn't without spending search budget.

**Extraction gotchas:**
- **Substack `publishedBylines` reports the publication OWNER, not a guest author.** A byline
  sweep must read post *bodies* or it will miss every guest post.
- **Scitation HTML interleaves whole reference entries into the body** as click-to-expand
  `ref-overlay` spans; a naive tag-strip yields unreadable prose. Remove the balanced spans first.
- **figshare's HEAD→`Location`→GET recipe now FAILS** on `ndownloader.figshare.com` (202 + WAF
  challenge, no `Location`), though it still works on institutional instances.

## 11. Two rulings this pass set

- **Granted patents stay out of `by/`** (set on an Agüera y Arcas Microsoft patent, and the text
  *was* successfully retrieved before the call was made). A patent is drafted by counsel, has
  multiple inventors, and reads as attorney boilerplate; ingesting it injects a voice that is not
  the person's into a corpus that feeds character simulation. The retrieval recipe is recorded in
  the INDEX so the ruling is one call to reverse. **Exclusion is the reversible direction.**
- **"Legitimately short" is a real category.** A Publisher Correction, a one-page conference
  abstract and a structured meeting abstract are complete at 800–900 chars. Label them
  `content: full-text` with an explicit `notes:` sentence saying the item genuinely is that
  short — otherwise every future length-based quality gate will flag them forever.

## 11b. ⚠️ The Wayback failure that was never Wayback's fault

**Check `https://` before diagnosing Wayback congestion.** The O'Reilly Radar recovery had been
recorded as a congestion failure — "19 of 164 snapshots reachable, 1 post fetched" — and the
handoff carried it forward as a Wayback-is-flaky problem. It was **`http://` vs `https://`**.
Port 80 to `web.archive.org` is intermittently refused from this host (`curl` exit 7, *"Failed to
connect after 48 ms"*), which looks exactly like rate-limiting and provokes a useless backoff
loop. Over HTTPS the identical CDX queries and `id_` replays answered in ~0.5 s at ~100% success:
**all 164 snapshots, 1,099 of 1,101 posts.**

This is the third mechanical cause this cleanup found for what were logged as *content* failures
(the other two: gzip-without-`Content-Encoding` on `id_` replay, and the
`filter=statuscode:200`+`www.` CDX artifact). **Any "Wayback was down / congested / exhausted"
note from the first fan-out should be re-tested before it is believed.**

**Byline archives can be contaminated.** ~19% of URLs under one person's own author path were
other bloggers on the same platform. Group blogs recycle author paths and templates change over
a decade — find a per-template signal that actually encodes authorship (here, the avatar filename
`photo_<slug>_s.jpg`, the only one stable across four templates 2005–2015) and **require an
affirmative byline before writing an item**. Record the rejects with their real bylines so a later
pass doesn't "recover" them.

## 12. Paywalled-looking captures that aren't (2026-08-14)

**NYT Wayback captures that render as a paywall usually still contain the whole article.** Two
problems stack, and either one alone reads as "the capture is dead":

1. The `id_` response body is **gzip bytes with no `Content-Encoding` header** — the same serving
   gotcha as `content.openalex.org` grobid (#779). Without a manual `\x1f\x8b` sniff and gunzip,
   the extractor sees binary and reports "no paragraphs."
2. Even when the rendered HTML truncates at the wall, **the complete body is in
   `window.__preloadedData`** — walk `ParagraphBlock` / `Heading*Block` nodes and dedupe.

That combination recovered a 15,000-word 2025 profile and a 2018 feature after both captures
looked dead. **WSJ is the instructive contrast**: its `__NEXT_DATA__` carries only a
two-paragraph snippet plus an `encryptedDataHash`, so there genuinely is nothing to recover —
save a labelled `excerpt` rather than leaving it pending forever.

**A CDX filter artifact hides captures.** `filter=statuscode:200` combined with the `www.` host
form returned **0** captures for a NYT URL whose bare host with no filter returns **17**. The same
shape resolved an item a previous pass had recorded as having "no CDX snapshots at all" — there
were three. Combined with the gzip trap above, **some "confirmed gone" verdicts in the first
fan-out are mechanically wrong rather than true**, and are worth re-testing before being believed.

## 13. Enumeration beats search — the free instruments, ranked

Across the cleanup fan-out the agents used **fewer than half** their WebSearch allowance and still
roughly doubled `about/`. What replaced it:

1. **Google News RSS** (`news.google.com/rss/search?q=...`) — free, unauthenticated, ~100 dated
   outlet-labelled items per call. **Caveat: its links are now opaque `AU_yq…`/`CBMi…` ids that do
   NOT base64-decode to a URL** — re-resolve headlines on the outlet (a WordPress
   `/wp-json/wp/v2/posts?search=` call does it in one hop).
2. **Outlet author/byline pages** — `theatlantic.com/author/<slug>/` and friends are plain HTML to
   a browser-header curl. **This is the class of miss the collection pass made**: it never
   enumerated The Atlantic for one person who had two essays there. Outlet author pages beat topic
   searches; build the outlet list from the person's own site and Wikipedia external links, then
   diff the enumeration against what is on disk.
3. **Publisher trade-review sites** — `kirkusreviews.com/book-reviews/<author>/<title>/` and
   `publishersweekly.com/<isbn-13>` serve full review text to plain curl. For an author with a
   forthcoming book these are often the *only* published coverage.
4. **`news.<university>.edu/profile/<name>`** — reverse-chron list of every campus-news story about
   a faculty member. Confirmed on UChicago; **confirmed absent for another UChicago professor**, so
   check rather than assume.
5. **Guardian Content API** (`api-key=test`, `show-fields=bodyText`) resolves *and* fetches in one
   call. Note `bodyText` is an unparagraphed blob — wording survives, structure doesn't; say so.
6. **Open course-catalog APIs** (Yale Course Search JSON, no key) yield first-party primary text —
   a syllabus description is the person's own words about what they currently think.
7. **A dead publication's successor site.** The Monkey Cage's whole 853-post archive is live on
   `goodauthority.org`. Wayback had ~40. **Check for a successor before mounting an archival dig.**

**And a discipline point that showed up twice:** a **person's own media/press index is not an
`about/` list.** On one dossier, 3 of 23 entries were citations-in-a-footnote or coverage that
actually quotes their advisor. On another, the `/press/` page omitted a real interview. Verify each
entry is about the person before filing it.
