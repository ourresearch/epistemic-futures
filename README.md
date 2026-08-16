# Epistemic Futures Corpus

This is a text corpus assembled ahead of the [Epistemic Futures Summit](https://epistemicfuturessummit.pubpub.org/)
(MIT, September 23–24, 2026): for each attendee, everything they've said or written on the
internet. Or at least, everything my agents could find and access.

This README, like the whole corpus, was created by Jason's Claude, with some help from Jason.

## What's it for?

I built it to prepare for the summit, and I'm sharing it because it seems useful for anyone
attending — and interesting to experiment with. Three ways in, in ascending order of weirdness:

- **text:** actually read the things people wrote. because it's 2022 lol.
- **tutor:** point an agent with RAG at it and have it walk you through attendees' positions and
  insights, find the themes, and dive in where you're interested.
- **theater:** have agents imitate attendees and see what a panel might look like — or run the
  whole workshop as a full Sims event (that's my plan). other efforts to do this have been
  disappointing (tl;dr agents play a very flat, stereotyped version of their character), but I'm
  hoping that a huge corpus instead of a short character card improves performance.

## A very short literature review

This section is short because "claude, write me a literature review for
https://github.com/ourresearch/epistemic-futures-corpus/" is the new literature review section.
Five pointers anyway, one per bullet above and two for the weird one:

- [Bird et al. 2008](https://aclanthology.org/L08-1005/) took a research community's own
  proceedings and republished them as a single standardized machine-readable corpus, which then
  became the substrate for a decade of research about that community.
- [Truss 2026](https://arxiv.org/abs/2601.22288) finds that personas which answer only from
  retrieved source text, cite it, and abstain when the corpus is silent work better as research
  instruments than personas that are simply told to act like someone.
- [Park et al. 2023](https://arxiv.org/abs/2304.03442) put 25 agents with memory, reflection, and
  planning in a Sims-like town and got them to organize a Valentine's Day party, which is still
  the closest published thing to simulating a whole event rather than a single conversation.
- [Shi & Haupt 2026](https://arxiv.org/abs/2604.23575) simulated 277 real philosophers from their
  profiles and found the simulated group's disagreement was 2–4× too narrow and organized along
  the wrong axes entirely — that's the disappointing prior work the third bullet refers to.
- [Park et al. 2024](https://arxiv.org/abs/2411.10109) got agents grounded in a two-hour interview
  with the actual person to 83% of that person's own test-retest reliability, versus 74% for
  agents given only demographics — which is the bet this corpus is making, at much greater length.

As far as I can tell, nobody has published a simulation of an entire conference. So that one's
still open.

## What's here, what's not

**Here:** each attendee's own words, and only their own words, published from 2005 onward — for
all 33 people on the [published attendee list](https://epistemicfuturessummit.pubpub.org/attendees).
Full text where the text is openly available; where a source is paywalled, only the abstract or
publisher summary, labeled as such.

| Type | Words | Items | Open access |
|---|---:|---:|---:|
| Papers | `6,834,237` | `1,107` | `67%` |
| Blog posts | `5,252,112` | `7,558` | `100%` |
| [Social posts](methods.md#5-social-media) | `2,620,863` | `111,255` | — |
| [Transcribed audio](methods.md#6-talks-podcasts-and-panels--transcripts) | `2,509,713` | `323` | — |
| Talks & interviews | `1,891,502` | `382` | `95%` |
| Essays, op-eds & news | `1,800,526` | `1,136` | `96%` |
| Books & chapters | `1,199,018` | `329` | `25%` |
| Reports | `1,054,909` | `136` | `90%` |
| Other | `363,835` | `88` | `75%` |
| **Total** | **`23,526,715`** | **`122,314`** | **`99%`** |

"Open access" is the share of items whose complete text was published openly and is included
here; the rest are abstract- or summary-only (social posts all count as open). Words are counted
from the saved text. "Talks & interviews" are published transcripts and written-up interviews;
"Transcribed audio" is our own machine transcription of talks, podcasts and panels that had no
published transcript (243 hours of audio, speaker-attributed).

**Not here:** anything written *about* an attendee by someone else, and no commentary or opinion
of ours about anyone — this is evidence, not evaluation.

## Methods

The short version; the full recipe is in [`methods.md`](methods.md).

1. Start from the summit's [published attendee list](https://epistemicfuturessummit.pubpub.org/attendees).
2. AI agents find and collect each attendee's content since 2005. We look here:
   - Their scholarly work, using the OpenAlex API to find and [download](https://help.openalex.org/access/fulltext/#the-content-endpoint-for-per-work-fetches) content.
   - Their own sites: blogs, feeds, CVs.
   - Outlets they write for, web search, and the Wayback Machine.
3. Convert everything to plain text and save, with metadata.
4. Audit every dossier: retry failures, OCR scans, sweep outlets for misses, de-duplicate.
5. Pull their public X and Bluesky posts.
6. Transcribe their talks and podcasts, with speakers named.
7. Note where each search stopped, so anyone can pick it up.

## Layout

```
dossiers/<person>/
  INDEX.md         manifest: bio, corpus summary, item list, coverage notes
  by/              their writing and speaking, one markdown file per item (YAML frontmatter)
  social/          their public X and Bluesky posts (JSONL)
  av/              speaker-attributed transcripts of their talks, podcasts and panels
  video.md         inventory of their video/audio appearances
  *.tsv            enumeration indexes (e.g. their OpenAlex works, blog archives)
dossiers/00-roster.md         who's here, with published affiliations and summit roles
dossiers/CONVENTIONS.md       the collection spec
dossiers/PILOT-LESSONS.md     method notes and gotchas from collecting
methods.md                    how the corpus was built, in enough detail to redo it
LICENSE, LICENSE-MIT          CC0 for the corpus's own contributions; MIT for scripts/
CITATION.cff                  citation metadata
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

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21956906.svg)](https://doi.org/10.5281/zenodo.21956906)

If you use the corpus, please [cite it](CITATION.cff). Releases are archived on Zenodo; the DOI
above always resolves to the latest version.
