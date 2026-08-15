# Epistemic Futures — a corpus of what the summit's attendees have written and said

This is a text corpus assembled ahead of the [Epistemic Futures Summit](https://epistemicfuturessummit.pubpub.org/)
(MIT, September 23–24, 2026): for each attendee, everything I could find that they have
**written or said and published openly on the internet** — papers, books, blog posts, op-eds,
interviews, talks, and their public social-media posts — collected as plain text, one file per item,
with the source URL on every file. It also includes a clean markdown copy of the summit's public
website (concept note, schedule, attendee list).

I built it to prepare for the summit, and I'm sharing it because I think it's a genuinely useful
resource for anyone attending — and an interesting one to experiment with. I'll be upfront about
what I'm going to try: I want to use it to **simulate the workshop** with AI agents and see what
comes out. But it has plenty of lower-key uses. You could just read it to brush up on what the
other people in the room have been thinking about. You could ask a language model to summarize
someone's positions on a question, or to find where two attendees agree and disagree, or to
draft you a reading list. Whatever you do with it, I'd love to hear about it.

— Jason Priem, OpenAlex

## What is — and isn't — in here

**In:** each attendee's own words, and only their own words. Full text where the text is openly
available; where a source is paywalled, only the abstract or publisher summary, labeled as such.
Every item's frontmatter carries a `content:` field (`full-text` / `excerpt` / `abstract-only` /
`summary-only`) so nothing masquerades as more than it is.

**Not in:** anything written *about* an attendee by someone else (no reviews, profiles, or
coverage), and no commentary, assessment, or opinion of ours about anyone. This is evidence, not
evaluation. It is also not a complete bibliography of anyone — it's what was findable and openly
available in August 2026, and each `INDEX.md` says where the search stopped.

**Provenance:** the collection was done with AI agents working to a written spec
(`dossiers/CONVENTIONS.md`), followed by audit passes; the method log is `dossiers/PILOT-LESSONS.md`
and the collector scripts are in `scripts/`. Text extraction from PDFs and web pages is
imperfect — check the `source_url` before quoting anything.

## Layout

```
dossiers/<person>/
  INDEX.md         manifest: bio, corpus summary, item list, coverage notes
  by/              their writing and speaking, one markdown file per item (YAML frontmatter)
  social/          their public X and Bluesky posts (JSONL)
  av/              speaker-attributed transcripts of talks and interviews (where done)
  video.md         inventory of their video/audio appearances
  *.tsv            enumeration indexes (e.g. their OpenAlex works, blog archives)
dossiers/00-roster.md         who's here, with summit roles
dossiers/CONVENTIONS.md       the collection spec
dossiers/PILOT-LESSONS.md     method notes and gotchas from collecting
scripts/                      collectors (X, Bluesky) and the export script
summit/website/               the summit's public website as markdown
```

## A note on the material

Everything here was openly published by its author or their publisher; each item links to
where it lives. It's gathered for the private, non-commercial use of summit participants and
researchers. If you're an author and would prefer something of yours not be included, tell me and
I'll remove it.

## About this repo

This is a generated export of a private working repository (`export_public.py` in `scripts/` is
the whitelist that produces it). Corrections and additions are welcome — open an issue with the
source URL — but note that edits made directly here will be overwritten by the next export.
