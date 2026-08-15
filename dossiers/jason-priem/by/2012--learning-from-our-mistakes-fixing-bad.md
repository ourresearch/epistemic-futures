---
title: "Learning from our mistakes: fixing bad data"
person: jason-priem
section: by
type: blog-post
year: 2012
date: 2012-08-21
venue: "Impactstory blog"
authors: "Jason Priem"
source_url: https://blog.openalex.org/29870682155/
retrieved: 2026-08-13
content: full-text
notes: "Byline from WordPress author field (user 'jason') on the merged Impactstory/OurResearch/OpenAlex blog. Originally published on blog.impactstory.org."
---

# Learning from our mistakes: fixing bad data

## Full text

\

Total-impact is in early beta.  We’re releasing early and often in this rapid-push stage, which means that we (and our awesome early-adopting users!) are finding some bugs.

As a result of early code, a bit of bad data had made it into our total-impact database.  It affected only a few items, but even a few is too many.  We’ve traced it to a few issues:

- our wikipedia code called the wikipedia api with the wrong type of quotes, in some cases returning partial matches
- when pubmed can’t find a doi and the doi contains periods, it turns out that the pubmed api breaks the doi into pieces and tries to match any of the pieces.  Our code didn’t check for this.
- a few DOIs were entered with null and escape characters that we didn’t handle properly

We’ve fixed these and redoubled our unit tests to find these sorts of bugs earlier in the future…. but how to purge the bad data currently in the database?

Turns out that the data architecture we had been using didn’t make this easy.   A bad pubmed ID propagated through our collected data in ways that were hard for us to trace.  Arg!  We’ve learned from this, and taken a few steps:

- deleted the problematic Wikipedia data
- deleted all the previously collected PubMed Central citation counts and F1000 notes
- deleted 56 items from collections because we couldn’t rederive the original input string
- updated our data model to capture provenance information so this doesn’t happen again!

What does this mean for a total-impact user?  You may notice fewer Wikipedia and PubMed Central counts than you saw last week if you revisit an old collection.  Click the “update” button at the top of a collection and accurate data will be re-collected.

It goes without saying: we are committed to bringing you Accurate Data (and radical transparency on both our successes and our mistakes 🙂 ).
