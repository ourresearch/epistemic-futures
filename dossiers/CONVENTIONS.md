# Super-dossier conventions

Every attendee gets one directory. The goal is a **camera-raw corpus**: collect the *original text* of everything the person has written or said (openly available, 2005 or later), so later agents can summarize it repeatedly along different axes without re-gathering. Summarization is lossy; this corpus is the negative.

## Directory layout

```
dossiers/<slug>/            # slug = firstname-lastname, lowercase, hyphens
  INDEX.md                       # manifest + bio header + coverage status
  by/                            # THE PERSON'S OWN WORDS
    2019--attention-is-broken.md
  social/                        # their public X / Bluesky posts (slimmed JSONL; see SOCIAL-COLLECTION.md)
  av/                            # speaker-attributed transcripts of talks/interviews (see methods.md)
  video.md                       # video/audio inventory feeding av/
```

### Own words only (the scope rule)

- **by/** = the person in their own words: journal articles, books, book chapters, blog posts, op-eds, essays, transcribed speeches/talks, **and interviews** (an interview is their own words even though a journalist frames it).
- **Out of scope: writing *about* the person** — profiles, biographies, reviews of their work, news coverage of them. This corpus does not collect third-party coverage. When in doubt: if the person's voice is the payload → in; if they're merely the subject → out.

## Item files

One file per item, markdown, named `YYYY--short-slug.md` (year first so files sort chronologically). YAML frontmatter, then the text:

```markdown
---
title: "Attention Is Broken"
person: geoffrey-bilder
section: by            # by | about
type: blog-post        # journal-article | book | book-chapter | blog-post | op-ed |
                       # essay | interview | talk-transcript | report | profile | review | news
year: 2019
date: 2019-03-14       # if known, else just year
venue: "The Scholarly Kitchen"
source_url: https://...
retrieved: 2026-08-13
content: full-text     # full-text | excerpt | abstract-only | summary-only
notes: ""              # paywall status, OA license, caveats
---

# <title>

<the text — or, if content != full-text, a clearly headed section:>

## Abstract (only openly available portion)
...
```

**The `content:` field is load-bearing.** Downstream summarizers must never mistake an abstract for the work itself. Match the body heading to it: `## Full text`, `## Excerpt`, `## Abstract (only openly available portion)`, `## Publisher summary`.

## Scope rules

- **Time window: published 2005-01-01 or later.** Older items may be listed in INDEX.md for completeness but not fetched.
- **Openly available text → save the full text.** Paywalled/closed → save the abstract or publisher summary, labeled as such. Never paste paywalled full text.
- **Publisher-published structured metadata counts as openly available** (ruling 2026-08-14, Jason-delegated; generalizes the Oransky metadata ruling). If the publisher's own site serves the complete text to anonymous clients in a public machine-readable field — schema.org `articleBody` in `ld+json` (hbr.org), `window.__preloadedData` (nytimes.com), a JSON API feeding their own page — that is the publisher openly distributing the text: save it as `content: full-text` and lead `notes:` with a `PROVENANCE` line naming the field it came from. Still forbidden: anything requiring a credential or session, actual paywall circumvention, and third-party pirate copies. First applied to 14 Weinberger HBR items.
- **Text only, no binaries.** Never commit PDFs; extract text (`pdftotext`, or copy from HTML rendering). Strip navigation/boilerplate; keep the actual prose.
- **Video/audio: note, don't transcribe** (separate later pass). In `video.md`: title, venue/channel, year, URL, ~duration, one-line topic. If an official transcript already exists as text, that's text — save it in `by/` as `talk-transcript`.
- **Books**: if the full text is openly available (free publisher ebook like SFI Press, OA monograph, CC-licensed edition), **save the entire book** as one `type: book` item, `content: full-text` — books are exempt from the truncation cap (a whole book is ~1MB of text; fine). If only closed: publisher summary + TOC (`content: summary-only`) plus any open excerpts as separate `excerpt` items.
- **No fabrication.** Only save text actually retrieved from a URL. If a fetch fails, list the item in INDEX.md with status `pending`, don't synthesize.

## Mega-prolific authors (hundreds+ items, e.g. a long-running blog)

Completeness stays the goal, achieved incrementally:
1. **Index first**: enumerate everything feasible (archives, feeds, OpenAlex) into INDEX.md with metadata, even before fetching.
2. **Fetch in priority order**: (a) relevant to summit themes (AI & knowledge, scholarly infrastructure, trust/misinformation, open access, commons/enclosure), (b) most-cited / best-known, (c) most recent.
3. **Record the frontier**: INDEX.md's coverage section says exactly what's fetched vs pending, so the next pass continues instead of restarting.

## Discovery playbook

- **Scholarly work: use OpenAlex (dogfood!).** `curl -s -H "Authorization: Bearer <YOUR_OPENALEX_API_KEY>" "https://api.openalex.org/works?filter=author.id:A...,from_publication_date:2005-01-01&per-page=100&select=id,title,publication_year,doi,type,open_access,best_oa_location,abstract_inverted_index,cited_by_count"` — first resolve the author via `/authors?search=<name>` (check affiliation to disambiguate). `best_oa_location.pdf_url`/`landing_page_url` for full text; reconstruct abstracts from `abstract_inverted_index`. **For OA full text, check the OpenAlex Content API FIRST**: `GET https://api.openalex.org/works/<id>/content` (same Bearer auth) returns `has_content: {pdf, grobid_xml}` + `content_urls` pointing at `content.openalex.org` — our own hosted copy, no publisher bot-walls; prefer `grobid_xml` (structured text) over `pdf` when both exist. Coverage is partial, so fall back in order: landing page HTML → EuropePMC/PMC (JATS via NCBI efetch) → `best_oa_location.pdf_url` + pdftotext. (Content API calls cost 100 credits each on the key above — fine, it's ours; don't hammer it for works where `has_fulltext`/`has_content` is false.)
- **Everything else**: personal site + blog archives (check /archive, sitemap.xml, RSS), Wikipedia (bibliography + External links), publisher author pages, Google Books/publisher blurbs, web search for `"<name>" interview`, `"<name>" op-ed`, `"<name>" transcript`, major outlets they write for.

## INDEX.md template

```markdown
# <Name> — <Affiliation> (summit role: organizer | session N lead | session N participant | participant)

Slug: <slug> · Last pass: 2026-08-13

## Quick bio
2-4 sentences, current role verified against a 2025-26 source (link it).

## Corpus summary
| Section | Items | full-text | abstract/summary-only | pending |
|---------|------:|----------:|----------------------:|--------:|
| by/     |       |           |                       |         |
Video items noted: N

## Items — by/
| Year | Title | Type | Content | File |
|------|-------|------|---------|------|
(newest first; pending items get file "—" and a source_url column note)

## Coverage notes & frontier
What was searched, what's exhausted, what's pending and where the next pass should resume. Known gaps (e.g. "blog archive pre-2012 not yet enumerated").
```

## Ground rules

- Work incrementally: **write each item file as soon as it's fetched** (checkpointing — a killed agent should leave a usable partial corpus).
- Update INDEX.md last, from what's actually on disk.
- **This is a public repository.** Everything in it was openly published by its author or publisher and links back to its source; see the README for what that does and doesn't mean (license, disclaimer, takedowns).

### No opinions in this repo — Jason's or yours

**This corpus is evidence, not evaluation.** Nothing in it may contain Jason's assessments of
these people, and nothing in it may contain *your* assessments either. Two reasons, and the
second is the one that bites:

1. **Respect.** Candid commentary written in a private register is not something anyone should
   have to worry about leaking.
2. **It would poison the simulation.** These dossiers feed character cards that drive agent
   simulations of these same people. An evaluative aside sitting in the corpus gets read as
   source material and contaminates the character it describes — at best noise, at worst a
   caricature laundered into what looks like evidence.

Concretely: no "this argument is weak," no "he's clearly wrong about X," no editorializing in
`notes:` fields, INDEX.md bios, coverage notes, or commit messages. **Neutral descriptive
summary is fine and expected** ("argues that peer review is a poor fraud filter"); judgment of
the argument's quality is not. If an evaluation feels genuinely necessary, it belongs in a
different repo — see the charter. When in doubt, describe rather than assess.
