---
title: "Choosing reference sets: good compared to what?"
person: jason-priem
section: by
type: blog-post
year: 2012
date: 2012-09-13
venue: "Impactstory blog"
authors: "Jason Priem"
source_url: https://blog.openalex.org/31461657926/
retrieved: 2026-08-13
content: full-text
notes: "Byline from WordPress author field (user 'jason') on the merged Impactstory/OurResearch/OpenAlex blog. Originally published on blog.impactstory.org."
---

# Choosing reference sets: good compared to what?

## Full text

\

In the previous post we assumed we had a list of 100 papers to use as baseline for our percentile calculations. But what papers should be on this list? 

It matters: not to brag, but I’m probably a 90th-percentile chess player compared to a reference set of 3rd-graders. The news isn’t so good when I’m compared to a reference set of Grandmasters. This is a really important point about percentiles: they’re sensitive to the reference set we pick.

The best reference set to pick depends on the situation, and the story we’re trying to tell. Because of this, in the future we’d like to make the choice for total-impact reference sets very flexible, allowing users to define custom reference sets based on query terms, doi lists, and so on.

For now, though, we’ll start simply, with just a few standard reference sets to get going.  Standard reference sets should be:

- meaningful
- easily interpreted
- not too high impact nor too low impact, so gradations in impact are apparent
- applicable to a wide variety of papers
- amenable to large-scale collection
- available as a random sample if large

For practical reasons we focus first on the last three points.  Total-impact needs to collect reference samples through automated queries.  This will be easy for the diverse products we track: for Dryad datasets we’ll use other Dryad datasets, for GitHub code repositories we’ll use other GitHub repos.  But what about for articles?  

Unfortunately, few open scholarly indexes allow queries by scholarly discipline or keywords… with one stellar exception.  PubMed.  If only all of research had a PubMed!  [PubMed’s eUtils API](http://www.ncbi.nlm.nih.gov/books/NBK25500/) lets us query by MeSH indexing term, journal title, funder name, all sorts of things.  It returns a list of PMIDs that match our queries.  The api doesn’t return a random sample, but we can fix that ([code](https://github.com/total-impact/total-impact-core/blob/master/extras/random_pmids.py)).  We’ll build ourselves a random reference set for each publishing year, so a paper published in 2007 would be compared to other papers published in 2007.

What specific PubMed query should we use to derive our article reference set?  After thinking hard about the first three points above and doing some experimentation, we’ve got a few top choices:

- any article in PubMed
- articles resulting from NIH-funded research, or
- articles published in Nature,

All of these are broad, so they are roughly applicable to a wide variety of papers.  Even more importantly, **people have a good sense for what they represent —** knowing that a metric is in the Xth percentile of NIH-funded research (or Nature, or PubMed) is a meaningful statistic.  

There is of course one huge downside to PubMed-inspired reference sets: they focus on a single domain.  Biomedicine is a huge and important domain, so that’s good, but leaving out other domains is unhappy.  We’ll definitely be keeping an eye on other solutions to derive easy reference sets (a PubMed for all of Science?  An open social science API?  Or hopefully Mendeley will include query by subdiscipline in its api soon?).  

Similarly, Nature examines only on a single publisher—and one that’s hardly representative of all publishing. As such, it may feel a bit arbitrary.

Right now, **we’re leaning toward using NIH-funded papers as our default reference set**, but we’d love to hear your feedback. What do you think is the most meaningful baseline for altmetrics percentile calculations?

*(This is part 5 of a series on how total-impact will give context to the altmetrics we report.)*
