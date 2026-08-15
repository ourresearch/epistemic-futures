# Epistemic Futures Corpus

### What the Epistemic Futures Summit's attendees have written and said, in their own words

This is a text corpus assembled ahead of the [Epistemic Futures Summit](https://epistemicfuturessummit.pubpub.org/)
(MIT, September 23–24, 2026): for each attendee, everything I could find that they have
**written or said and published openly on the internet** — papers, books, blog posts, op-eds,
interviews, talks, and their public social-media posts — collected as plain text, one file per item,
with the source URL on every file. It also includes a clean markdown copy of the summit's public
website (concept note, schedule, attendee list).

This README, like the whole corpus, was created by Jason's Claude, with some help from Jason.

## What's it for?

I built it to prepare for the summit, and I'm sharing it because it seems useful for anyone
attending — and interesting to experiment with. Some things you could do with it:

- **Read it.** Brush up on what the other people in the room have been thinking about.
- **Ask a language model about it.** Summarize someone's positions on a question; find where two
  attendees agree and disagree; draft yourself a reading list.
- **Prepare your own session or unconference topic** with the actual arguments people have made,
  in front of you.
- **Simulate the workshop** and see what the simulated workshop produces. Do it before the real
  one and you have a natural experiment: compare what the simulation predicted with what actually
  happened. That's my plan.

## What's here, what's not

**Here:** each attendee's own words, and only their own words, published from 2005 onward — for
all 33 people on the [published attendee list](https://epistemicfuturessummit.pubpub.org/attendees).
Full text where the text is openly available; where a source is paywalled, only the abstract or
publisher summary, labeled as such.

| Type | Items | Full text openly available | Words |
|---|---:|---:|---:|
| Blog posts | `7,558` | `100%` | `5,252,112` |
| Journal articles | `992` | `65%` | `5,987,515` |
| Essays | `540` | `93%` | `1,247,407` |
| Op-eds | `354` | `98%` | `375,791` |
| Book chapters | `243` | `31%` | `539,440` |
| News pieces | `242` | `100%` | `177,328` |
| Interviews | `219` | `94%` | `862,134` |
| Talk transcripts | `163` | `96%` | `1,029,368` |
| Reports | `136` | `90%` | `1,054,909` |
| Books | `86` | `9%` | `659,578` |
| Conference papers | `77` | `92%` | `562,524` |
| Preprints | `38` | `71%` | `284,198` |
| Other | `88` | `75%` | `363,835` |
| **All written items** | **`10,736`** | **`93%`** | **`18,396,139`** |
| Social posts | `111,255` | — | `2,620,863` |
| Talk/podcast transcripts | *in progress* | — | — |

"Full text openly available" is the share of items whose complete text was published openly and is
included here; the rest are abstract- or summary-only. Words are counted from the saved text.

**Not here:** anything written *about* an attendee by someone else, and no commentary or opinion
of ours about anyone — this is evidence, not evaluation.

## Methods

The short version; the full recipe is in [`methods.md`](methods.md).

1. **Start from the summit's [published attendee list](https://epistemicfuturessummit.pubpub.org/attendees).**
2. **One AI agent per person** (Claude, working to the written spec in
   [`dossiers/CONVENTIONS.md`](dossiers/CONVENTIONS.md)) collects everything that person has
   written or said, published 2005 or later, in this order:
3. **Scholarly record via [OpenAlex](https://openalex.org)** — resolve and disambiguate the author,
   list their works with open-access locations and abstracts, and pull hosted full text from
   OpenAlex's Content API where it exists.
4. **Their own sites** — blog archives, sitemaps, feeds, CVs and bibliographies they publish
   themselves.
5. **Outlets and publishers** — author pages at every venue they write for; then web search for
   interviews, op-eds and transcripts; then the Wayback Machine for anything dead or moved.
6. **Save every item as plain text** with its source URL and a label saying whether it is full
   text, an excerpt, or only an abstract. Nothing is ever synthesized; a failed fetch is listed as
   pending, not reconstructed.
7. **Audit passes over every dossier** — re-probe abstract-only items for open full text, OCR
   scanned PDFs, retry failed archive fetches, sweep outlet author pages for recall, de-duplicate
   cross-posts.
8. **Social posts** — pull each person's public X and Bluesky posts through the platforms' APIs;
   Bluesky in full, X capped at the same 4,290 most-recent posts per person, no keyword filtering.
9. **Talks, podcasts and panels** — inventory them in `video.md`, transcribe with speaker
   diarization, name the attendee's speaker track with an LLM pass, file in `av/`.
10. **Record the frontier** — each `INDEX.md` says what was searched and where the search stopped,
    so anyone can pick it up.

## Layout

```
dossiers/<person>/
  INDEX.md         manifest: bio, corpus summary, item list, coverage notes
  by/              their writing and speaking, one markdown file per item (YAML frontmatter)
  social/          their public X and Bluesky posts (JSONL)
  av/              speaker-attributed transcripts of talks and interviews (as they land)
  video.md         inventory of their video/audio appearances
  *.tsv            enumeration indexes (e.g. their OpenAlex works, blog archives)
dossiers/00-roster.md         who's here, with published affiliations and summit roles
dossiers/CONVENTIONS.md       the collection spec
dossiers/PILOT-LESSONS.md     method notes and gotchas from collecting
methods.md                    how the corpus was built, in enough detail to redo it
LICENSE, LICENSE-MIT          CC0 for the corpus's own contributions; MIT for scripts/
CITATION.cff, codemeta.json   citation + machine-readable metadata
scripts/                      collectors (X, Bluesky) and helpers
summit/website/               the summit's public website as markdown
```

## Use, accuracy, and takedowns

This corpus is provided for research purposes, as is, without warranty of any kind. It was
assembled largely by automated tools: text was extracted from PDFs and web pages by software,
social posts came from platform APIs, and the talk transcripts are machine-generated (automatic
speech recognition plus a model that assigns speaker names). Every one of those steps makes
mistakes — dropped or garbled passages, misattributed speakers, an item filed under the wrong
person. Treat everything here as a pointer to a source, not as the source: **before quoting or
attributing anything to anyone, check it against the `source_url` on the item.** Don't rely on
it for anything where an error would matter.

Everything here was openly published by its author or their publisher, and each item links to
where it lives. If you're an author and would prefer something of yours not be included, email
support@openalex.org (subject "Epistemic Futures corpus") and I'll take it down.

## License

The texts collected here belong to their authors and publishers and keep whatever rights and
licenses they were published under; nothing about that changes by their being gathered here.
What we made — the selection and arrangement, the metadata and indexes, the transcripts, and the
notes — is released under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)
([`LICENSE`](LICENSE)): use it however you like, no attribution required. The code in `scripts/`
is under the MIT license ([`LICENSE-MIT`](LICENSE-MIT)).

## Citing

If you use the corpus, cite it — GitHub's "Cite this repository" button reads
[`CITATION.cff`](CITATION.cff); machine-readable metadata is also in [`codemeta.json`](codemeta.json).
