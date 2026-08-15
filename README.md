# Epistemic Futures Corpus

### What the Epistemic Futures Summit's attendees have written and said, in their own words

*Compiled by Jason Priem's AI agent (Claude), with help from Jason Priem · [OpenAlex](https://openalex.org)*

This is a text corpus assembled ahead of the [Epistemic Futures Summit](https://epistemicfuturessummit.pubpub.org/)
(MIT, September 23–24, 2026): for each attendee, everything I could find that they have
**written or said and published openly on the internet** — papers, books, blog posts, op-eds,
interviews, talks, and their public social-media posts — collected as plain text, one file per item,
with the source URL on every file. It also includes a clean markdown copy of the summit's public
website (concept note, schedule, attendee list).

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
  happened. That's what I'm going to do.

Whatever you do with it, I'd like to hear about it.

## What's here, what's not

**Here:** each attendee's own words, and only their own words — 33 people (the [published
attendee list](https://epistemicfuturessummit.pubpub.org/attendees) plus me), 2005 onward. Full
text where the text is openly available; where a source is paywalled, only the abstract or
publisher summary, labeled as such.

| Type | Items | Full text openly available | Words |
|---|---:|---:|---:|
| Blog posts | 7,558 | 100% | 5.3M |
| Journal articles | 992 | 65% | 6.0M |
| Essays | 540 | 93% | 1.2M |
| Op-eds | 354 | 98% | 376K |
| Book chapters | 243 | 31% | 539K |
| News pieces (bylined) | 242 | 100% | 177K |
| Interviews | 219 | 94% | 862K |
| Talk transcripts (published) | 163 | 96% | 1.0M |
| Reports | 136 | 90% | 1.1M |
| Books | 86 | 9% | 660K |
| Conference papers | 77 | 92% | 563K |
| Preprints | 38 | 71% | 284K |
| Other (reviews, theses, newsletters, slides, letters…) | 88 | 75% | 364K |
| **All written items** | **10,736** | **93%** | **18.4M** |
| Social posts (X 53,403 · Bluesky 57,852) | 111,255 | — | 2.6M |
| Talk/podcast transcripts (machine, speaker-attributed) | *in progress* | — | — |

"Full text openly available" is the share of items whose complete text was published openly and is
included here; the rest are abstract- or summary-only. Words are counted from the saved text.

**Not here:** anything written *about* an attendee by someone else, and no commentary or opinion
of ours about anyone — this is evidence, not evaluation.

## Methods (short version — full detail in [`methods.md`](methods.md))

The attendee list is the summit's [published one](https://epistemicfuturessummit.pubpub.org/attendees).
For each person, an AI agent (Claude, working to the written spec in
[`dossiers/CONVENTIONS.md`](dossiers/CONVENTIONS.md)) enumerated their scholarly record through
[OpenAlex](https://openalex.org) — author disambiguation, works list, open-access locations, and
OpenAlex's Content API for hosted full text — then their own websites and blog archives (sitemaps,
feeds, the Wayback Machine), publisher and outlet author pages, and web search for interviews,
op-eds and transcripts. Everything retrieved was saved as plain text with its source URL and a
label saying whether it is full text, an excerpt, or only an abstract; nothing was ever
synthesized. Public X and Bluesky posts were pulled through the platforms' APIs (Bluesky in full;
X capped at the same 4,290 most-recent posts per person, no keyword filtering). Talks, podcasts
and panels listed in each person's `video.md` are being transcribed with speaker diarization and
an LLM pass that names the attendee's speaker track; those land in `av/`. Every dossier's
`INDEX.md` records what was searched and where the search stopped, so anyone can pick it up.

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
notes — is released under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/): use it
however you like, no attribution required (though we'd enjoy hearing about it). The scripts are
MIT-licensed.
