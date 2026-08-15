# Methods — how this corpus was built

Detailed enough to redo it for another group of people. The short version is in the
[README](README.md#methods). Dates are 2026 unless noted.

## 1. Who

The population is the summit's own [published attendee list](https://epistemicfuturessummit.pubpub.org/attendees)
(organizers + "Confirmed Participants" — 32 people as of Aug 14), plus Jason Priem's own dossier,
which was built first as a calibration case: the one person whose ground truth he could check
directly, used to validate the conventions before fanning out. An earlier roster inferred from the
invitation materials differed by three names in each direction; when the site went live the corpus
was reconciled to it (three people added and collected; three removed). If the list changes again
before the summit, the corpus should follow it.

## 2. Inclusion criteria

- **Own words only.** Journal articles, books and chapters, preprints, reports, blog posts, essays,
  op-eds, newsletters, published talk transcripts, slides, theses — and **interviews**, on the
  view that an interview is the person's words even though someone else frames it. Third-party
  writing *about* a person (profiles, reviews of their work, news coverage) is out of scope.
- **Published 2005-01-01 or later.** Older items may be listed in an `INDEX.md` for completeness
  but were not fetched.
- **Openly available text only.** If the full text is openly published, it is saved in full
  (whole books included, when the publisher makes them open). If a source is paywalled or closed,
  only the abstract or publisher summary is saved, and the item is labeled `abstract-only` /
  `summary-only`. Paywalls were never circumvented and pirate copies were never used. One ruling
  worth stating: if a publisher's *own* page serves the complete text to anonymous visitors in a
  machine-readable field (schema.org `articleBody` in `ld+json`, a page's preloaded JSON, a
  first-party API), that counts as openly published and was saved as full text, with the field
  named in the item's `notes`.
- **Scholarly and non-scholarly alike.** The aim was everything the person has said in public,
  not a bibliography of their academic work.
- **Social media:** each person's public X and Bluesky posts (see §5).
- **Video and audio:** talks, podcasts, panels and interviews were inventoried per person in
  `video.md` and are being transcribed (see §6).
- **No fabrication.** Only text actually retrieved from a URL was saved; a failed fetch is listed
  as pending in the index, never reconstructed.
- **No evaluation.** Nothing in the corpus records anyone's opinion of the material — neutral
  description in bios and notes only. (Beyond courtesy, an evaluative aside in a corpus that feeds
  agent simulations of these same people would be read as evidence about them.)

## 3. Item format

One markdown file per item, `by/YYYY--short-slug.md`, YAML frontmatter then the text. The
frontmatter carries `title`, `type` (blog-post, journal-article, book, interview, …), `date`,
`venue`, `source_url`, `retrieved`, `content` and `notes`. **`content` is load-bearing:**
`full-text` | `excerpt` | `abstract-only` | `summary-only` | `metadata-only`, mirrored by the
body's heading, so no downstream reader can mistake an abstract for the work. Text only, no
binaries: PDFs were text-extracted (`pdftotext`, or GROBID XML where OpenAlex had it), HTML was
stripped of navigation and boilerplate. Full spec: [`dossiers/CONVENTIONS.md`](dossiers/CONVENTIONS.md).

## 4. Discovery and fetching (written items)

Collection was done by AI agents (Claude, via Claude Code) working from the written spec, one
agent per person, in two waves (Aug 13–14), each writing item files as it went (checkpointing —
a killed agent leaves a usable partial corpus) and updating `INDEX.md` last, from what was on
disk. Every dossier's `INDEX.md` § "Coverage notes & frontier" records exactly which surfaces
were searched, which are exhausted, and where a later pass should resume.

The discovery order, per person:

1. **Scholarly record via [OpenAlex](https://openalex.org).** Resolve the author
   (`/authors?search=<name>`, disambiguated by affiliation — several people had multiple or
   contaminated author IDs; those audits are in the dossier TSVs), then list works
   (`/works?filter=author.id:…,from_publication_date:2005-01-01`) with `open_access`,
   `best_oa_location` and the abstract (reconstructed from `abstract_inverted_index`). For open
   full text, OpenAlex's **Content API** (`/works/<id>/content`) was tried first — it serves a
   hosted PDF and GROBID XML for a large share of open works, with no publisher bot-walls — then
   the landing page, Europe PMC / PMC (JATS), and `best_oa_location.pdf_url`. Each person's full
   OpenAlex works list is saved as `openalex-works-index.tsv`.
2. **Their own sites:** personal site and blog archives (`/archive`, `sitemap.xml`, RSS, WordPress
   and Substack APIs, Medium feeds), CVs and bibliographies they publish themselves — the single
   best enumeration for most people. Complete blog archives were taken in full (one person's runs
   to ~1,700 posts).
3. **Outlets and publishers:** author pages at every outlet they write for (the Monkey Cage /
   Good Authority, HBR, Wired, The Atlantic, Radar, Retraction Watch, STAT, The Economist, …),
   publisher author pages, Edge.org, Big Think, Long Now and similar venues that publish
   official transcripts.
4. **Web search** for `"<name>" interview | op-ed | transcript | keynote`.
5. **The Wayback Machine** for anything dead or moved (CDX enumeration, then `id_` replay).

After the first pass, five audit passes ran over every dossier (Aug 14): a re-probe of every
abstract-only item against the Content API; OCR of scanned PDFs; a consolidated retry of failed
Wayback fetches (most first-pass "content is gone" verdicts turned out to be mechanical fetch
failures — `http` vs `https` to `web.archive.org`, gzip served without a `Content-Encoding`
header, a CDX filter artifact — not missing content); an outlet-by-outlet author-page recall
sweep; and a cross-post de-duplication (one copy kept, with a pointer). Corpus grew from ~9,000
to ~10,700 items and from 91% to 93% full text. Method notes and gotchas from all of this are in
[`dossiers/PILOT-LESSONS.md`](dossiers/PILOT-LESSONS.md).

## 5. Social media

Handles were verified per person (X and Bluesky; several look-alike accounts documented and
excluded — `dossiers/00-social-census.md`). Bluesky was pulled in full through the public AT
Protocol API (`getAuthorFeed`), then slimmed to the post fields (`scripts/slim_bluesky.py`). X was
pulled through the v2 full-archive search API (`scripts/collect_x.py`), with one deliberate
limit: a **uniform recency cap of 4,290 posts per person** — the roster median — and **no
keyword filtering**, on the principle that filtering at the collection stage bakes in a bias no
later pass can undo. Retweets, replies and quotes are kept (what someone amplifies is signal).
Two accounts are protected and could not be collected; one attendee's X account is suspended
(Bluesky covers them). Detail and per-person counts: `dossiers/SOCIAL-COLLECTION.md`.

## 6. Talks, podcasts and panels → transcripts

Each dossier's `video.md` lists the person's video/audio appearances found during discovery —
389 items across the 33 people (261 YouTube, 34 podcasts, 13 Vimeo, ~77 on other hosts). Where an
official human transcript already existed it was saved as a written item; the rest go through a
transcription pipeline (built Aug 14–15, still running as of this writing — transcripts land in
`av/` as they're reviewed):

- **Acquisition** is the hard part. YouTube audio via `yt-dlp` (browser cookies, a PO-token
  provider, the JS challenge solver, `player_client=tv`, VPN rotation when an IP is flagged);
  podcasts via their RSS enclosure rather than Spotify/Apple links; Cloudflare-fronted hosts
  (Big Think, C-SPAN, PBS, …) via a headless-browser fetch to find the page's player manifest,
  then the open CDN. Some hosts remain out of reach (Vimeo-embedded, Spotify-DRM, a few
  broadcaster players).
- **ASR + diarization: ElevenLabs Scribe v2** — the most accurate option measured (2.3% WER vs
  Whisper large-v3's 4.2%) and cheaper than the Whisper API, with diarization included.
- **Speaker naming:** no ASR emits names, so an LLM pass reads the diarized transcript and names
  the attendee's speaker track from context ("thanks for having me, David"); everyone else stays
  `Interviewer` / `Panelist B`. Voice enrollment (`gpt-4o-transcribe-diarize`) is the fallback for
  items where context doesn't settle it. Free YouTube auto-captions were pulled first as a triage
  layer (233 of 261 items had them) but the paid diarized pass is run on everything lacking an
  official transcript, because attributing an interviewer's words to the subject is worse than
  no transcript.
- **Guards:** items with under 50 words of speech (music, B-roll) are dropped; every transcript's
  frontmatter carries a `transcription:` block (engine, model, date, naming method) so a reader
  knows it is machine output.

## 7. Known limitations

- Coverage is "what was findable and openly available in August 2026", not a bibliography.
  Thin public footprints stay thin (a couple of people have single-digit item counts, with the
  surfaces recorded as exhausted). Prolific bloggers dominate the item counts.
- Text extraction is imperfect: PDF→text drops footnotes, tables and equations; some publisher
  pages yielded a stale or wrong document (a handful of cases were caught by a title-overlap
  check; some surely weren't). Check the `source_url` before quoting.
- Transcripts are machine output with model-assigned speaker names; misattribution is possible.
- The X cap under-represents the most prolific posters (one attendee has ~246K posts) and skews
  their sample toward recent months.
- Roster and affiliations follow the summit's published list; several people's affiliations have
  changed since their earlier public bios.

## 8. Reproducing this for another group

Take the published participant list; give each agent `dossiers/CONVENTIONS.md`, a person, and
the discovery order in §4; require checkpointed writes and a frontier note; run the audit passes
in §4 afterward (they were worth ~20% more items); collect social with the collectors in
`scripts/`; inventory AV into `video.md` and transcribe as in §6. Budget: the written corpus cost
agent time only; X collection cost ~$280 for the 20-odd accounts; transcription is estimated at
$100–200 for 300–600 hours of audio.
