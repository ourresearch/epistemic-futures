---
title: "CLADDIER Final Report"
person: "geoffrey-bilder"
section: "by"
type: "blog-post"
year: 2008
date: 2008-01-15
venue: "Crossref blog"
authors: "Geoffrey Bilder (unbylined; attributed on internal evidence — see notes)"
source_url: "https://www.crossref.org/blog/claddier-final-report/"
retrieved: "2026-08-13"
content: "full-text"
notes: "Not returned by the crossref.org/authors/geoffrey-bilder/ archive: on the current Crossref site this post is bylined to the generic 'admin' account, which is why the previous pass missed it. Attributed to Bilder on internal evidence — the post says 'one that I talked about briefly (PDF) at the UKSG's Measure for Measure seminar last June' and links to a slide deck filed as PresentationBilder.pdf, and its subject (trust in distributed/linkback citation architectures, Crossref's non-commercial status) is his R&D beat. The attribution is an inference, not a published byline. Text taken from the Crossref blog RSS feed (crossref.org/blog/index.xml), which carries full post bodies; inline link URLs are not preserved."
---

# CLADDIER Final Report

## Full text

I just ran across the final report from the CLADDIER project. CLADDIER comes from the JISC and stands for “CITATION, LOCATION, And DEPOSITION IN DISCIPLINE & INSTITUTIONAL REPOSITORIES”. I suspect JISC has an entire department dedicated to creating impossible acronyms (the JISC Acronym Preparation Executive?)

Anyhoo- the report describes a distributed citation location and updating service based on the linkback mechanism that is widely used in the blogging community.

I think this is an interesting approach and is one that I talked about briefly (PDF) at the UKSG’s Measure for Measure seminar last June. I think that, like most proponents of p2p distributed architectures, they massively underestimate the problem of trust in the network. They fully knowledge the problem of linkback spam, but their hand-wavy-solution(tm) of using whitelists just means the system effectively becomes semi-centralized again (you have to have trusted keepers of the whitelists).

And of course I was mildly exasperated by the report’s characterization of one of the perceived “disadvantages” of the Crossref architectural model being a :

“Centralised service hosting a large persistent store – with the need for a (possibly commercial) business model to justify providing the service.”

Though DOI registries like Bowker and Nielsen Bookdata are commercial, Crossref, the organisation that services the industry that the JISC is concerned with, is *not* a commercial service.

Also if you replaced the phrase “justify providing” with the word “sustain”, the sentence wouldn’t sound like such a “disadvantage.”

But aside from these quibbles, the report makes an interesting (if technical) read.
