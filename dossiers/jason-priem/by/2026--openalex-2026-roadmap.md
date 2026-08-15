---
title: "OpenAlex 2026 Roadmap"
person: jason-priem
section: by
type: blog-post
year: 2026
date: 2026-01-16
venue: "OpenAlex blog"
authors: "Jason Priem"
source_url: https://blog.openalex.org/openalex-2026-roadmap/
retrieved: 2026-08-13
content: full-text
notes: "Byline from WordPress author field (user 'jason') on the merged Impactstory/OurResearch/OpenAlex blog. Originally published on blog.openalex.org."
---

# OpenAlex 2026 Roadmap

## Full text

We just wrapped up our Q1 2026 Town Hall. You can [watch the full recording here](https://www.youtube.com/watch?v=q9KF_eARJaY), but this post covers the highlights: what we shipped last quarter, what’s coming this quarter, and why we think 2026 is a pivotal year for open science.

## What we shipped in Q4

The Walden rewrite is done. OpenAlex now runs on a modern Databricks infrastructure that lets us ship faster and iterate on data quality in days instead of months.

We added 192 million new works from DataCite and repositories. OpenAlex now indexes 477 million works—the largest connected repository of scholarship ever published.

On funders and awards: we created Awards as a first-class entity, extracted 27 million funder links from fulltext PDFs, and integrated 15 new funders directly.

## What’s coming in Q1

**For enterprise users:** Credit-based API pricing launches this month. Different calls cost different amounts:

- a singleton (/works/w123) is 1 credit,
- a list (/works?filter=foo:bar) is 10,
- PDF content (coming this month!) is 100,
- vector search is 1,000. (coming soon! email steve@ourresearch.org for early access!)

We’re also launching a sync service so you can pull daily updates in one chunk instead of polling millions of records.

**For institutions:** Affiliation matching curation launches in February. Members can edit the matching algorithm that links affiliation strings to their institution. Changes propagate to the API within a day—permanently improving the dataset for everyone.

We’re also launching two membership tiers at \$5k and \$20k/year that include ability to curate your own data in OpenAlex, training/consulting, and pro API keys with higher API access for your faculty.

**For researchers:** A complete rewrite of author name disambiguation ships by end of Q1. This has always been the hardest problem in bibliometrics. With today’s AI, we think we can build the most accurate system ever made.

## The bigger picture

There’s a lot more I want to say about why 2026 feels like a pivotal year—why we think the GUI is dead, why open data wins the AI era, and what that means for OpenAlex. I’ll save that for a follow-up post. For now: [watch the town hall](https://www.youtube.com/watch?v=q9KF_eARJaY) to hear the full argument, and [try the vibe-coded demo](https://vibe-coding-examples.vercel.app/research-trends.html) I built live during the talk. And [join our mailing list](https://openalex.org/) to stay up-to-date on all the wild stuff we’re doing this year. It’s going to be, by far, our biggest year ever. You ain’t seen nothing yet.
