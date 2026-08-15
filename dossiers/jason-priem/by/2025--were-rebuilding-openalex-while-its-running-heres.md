---
title: "We’re Rebuilding OpenAlex While It’s Running — Here’s What’s Changing"
person: jason-priem
section: by
type: blog-post
year: 2025
date: 2025-08-09
venue: "OurResearch blog"
authors: "Jason Priem"
source_url: https://blog.openalex.org/were-rebuilding-openalex-while-its-running-heres-whats-changing/
retrieved: 2026-08-13
content: full-text
notes: "Byline from WordPress author field (user 'jason') on the merged Impactstory/OurResearch/OpenAlex blog. Originally published on blog.ourresearch.org."
---

# We’re Rebuilding OpenAlex While It’s Running — Here’s What’s Changing

## Full text

TLDR: Over the next five months we’re migrating OpenAlex to a new, better codebase; our schema won’t change, but some data (5%) will, and we’ll add over 50 million new works.

## Why the change

OpenAlex was written in a big hurry, to fill the gap left when [Microsoft Academic Graph disappeared](https://www.nature.com/nature-index/news/microsoft-academic-graph-discontinued-whats-next). The code was rushed and hacky, and it shows:

- Unpaywall and OpenAlex are awkwardly integrated and sometimes disagree.
- Fixing bugs and adding features takes forever.
- Adding new sources (eg DataCite) and entity types (grants) is nigh impossible.

## The solution

We’re merging the codebases of Unpaywall and OpenAlex, and rebuilding everything atop [Apache Spark](https://spark.apache.org/) hosted on [Databricks](https://www.databricks.com/). This stack is more modern, maintainable, and much much faster.

## What’s changing

Our goal is to fix the code, not change the functionality or data. That said, you’ll inevitably notice some changes, intended and otherwise. It’s like swapping out the engine of your car—while you’re driving. Here’s what will change:

- **50+ million new works**: we’re adding oodles of content from DataCite and institutional repositories, with more coming soon.
- **Unpaywall and OpenAlex will always agree** (though they’ll stay separate apps).
- **You can edit our data**: users will be able curate mistakes and see the curations applied within days.
- **Lots of small data changes** across the whole dataset—for example, some works’ citation counts may grow or shrink, some works will get new OA links, etc. This is impossible to avoid, but our goal is to make sure nothing changes by more than 5%.
- **New topics algo**: works created after the migration will use an updated algorithm but deliver similar results using the same taxonomy.
- **New keywords**: works will get new keywords from a new algorithm based on our concepts algo.

## What’s not changing

- **IDs will stay stable**, so if you request a work/author/etc by OpenAlex ID you’ll get the same thing before and after the migration.
- **Functionality** will stay the same in the API, web UI, and snapshot. It’ll all work like before.
- **The data schema** won’t change.

## Timeline

- ~~**June 1: Unpaywall**~~
  - [Unpaywall migration done](https://groups.google.com/g/unpaywall/c/0nEpQ-ImE-4)
- **Oct 1: Beta launch**
  - *Preliminary* data from the new codebase can be used in the API by adding the `data_version=2` param.
  - Web-based comparison tool launches
  - Beta snapshot of new data is published; you can explore this one.
- **Nov 1: Launch**
  - The API and UI serve data from the new codebase by default.
  - Data from the old codebase deprecated but still available by adding in the API by using the `data_version=1` param.
  - Prod snapshot of new data is published; you should use this one
- **Dec 1: Completion**
  - Data from the old codebase is no longer available in API.
  - Web-based comparison tool retired
  - One last snapshot of the old data is published.

## Stay up to date!

The rewrite is nearing release, but it’s still in very active development and we’re learning as we go. Some things might go worse than expected, some better. We’ll be making regular updates via the [openalex-users Google Group,](https://groups.google.com/g/openalex-users) so sign up there if you want to stay up to date on everything.
