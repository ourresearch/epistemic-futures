---
title: "Linking data and publications"
person: "geoffrey-bilder"
section: "by"
type: "blog-post"
year: 2014
date: 2014-09-21
venue: "Crossref blog"
authors: "Geoffrey Bilder"
source_url: "https://www.crossref.org/blog/linking-data-and-publications/"
retrieved: "2026-08-13"
content: "full-text"
notes: "Crossref blog post. DOI 10.64000/4hghg-ada86."
---

# Linking data and publications

## Full text

**3 minute read.**

## Linking data and publications

Do you want to see if a Crossref DOI (typically assigned to publications) refers to DataCite DOIs (typically assigned to data)? Here you go:

<https://web.archive.org/web/20150121025249/http://api.labs.crossref.org/graph/doi/10.4319/lo.1997.42.1.0001>

Conversely, do you want to see if a DataCite DOI refers to Crossref DOIs? Voilà:

<https://web.archive.org/web/20150321190744/http://api.labs.crossref.org/graph/doi/10.1594/pangaea.185321>

### Background

“How can we effectively integrate data into the scholarly record?” This is the question that has, for the past few years, generated an unprecedented amount of handwringing on the part researchers, librarians, funders and publishers. Indeed, this week I am in Amsterdam to attend the 4th RDA plenary in which this topic will no doubt again garner a lot of deserved attention.

We hope that the small example above will help push the RDAs agenda a little further. Like the recent [ODIN](http://odin-project.eu) project, It illustrates how we can simply combine two existing scholarly infrastructure systems to build important new functionality for integrating research objects into the scholarly literature.

Does it solve all of the problems associated with citing and referring to data? Can the various workgroups at RDA just cancel their data citation sessions and spend the week riding bikes and gorging on croquettes? Of course not. But my guess is that by simply integrating DataCite and Crossref in this way, we can make a giant push in the right direction.

There are certainly going to be differences between traditional citation and data citation. Some even claim that citing data isn’t “as simple as citing traditional literature.” But this is a caricature of traditional citation. If you believe this, go off an peruse the MLA, Chicago, Harvard, NLM and APA citation guides. Then read [Anthony Grafton’s, *The Footnote*](http://www.hup.harvard.edu/catalog.php?isbn=9780674307605)? Are you back yet? Good, so let’s continue…

Citation *of any sort* is a complex issue- full of subtleties, edge-cases exceptions, disciplinary variations and kludges. Historically, the way to deal with these edge-cases has been social, not technical. For traditional literature we have simply evolved and documented citation practices which generally make contextually-appropriate use of the same technical infrastructure (footnotes, endnotes, metadata, etc.). I suspect the same will be true in citing data. The solutions will not be technical, they will mostly be social. Researchers, and publishers will evolve new, contextually appropriate mechanisms to use existing infrastructure deal with the peculiarities of data citation.

Does this mean that we will never have to develop new systems to handle data citation? Possibly But I don’t think we’ll know what those systems are or how they should work until we’ve actually had researchers attempting to use and adapt the tools we have.

### Technical background

About five years ago, Crossref and DataCite explored the possibility of exposing linkages between DataCite and Crossref DOIs. Accordingly, we spent some time trying to assemble an example corpus that would illustrate the power of interlinking these identifiers. We encountered a slight problem. We could hardly find any examples. At that time, virtually nobody cited data with DataCite DOIs and, if they did, the Crossref system did not handle them properly. We had to sit back and wait a while.

And now the situation has changed.

This demonstrator harvests DataCite DOIs using their OAI-PMH API and links them in a graph database with Crossref DOIs. We have exposed this functionality on the “labs” (i.e. experimental) version of our REST API as a graph resource. So…

Now you can get a list of Crossref DOIs that refer to DataCite DOIs using [Event Data](https://www.crossref.org/services/event-data/).

### Caveats and Weasel Words

* We have not finished indexing all the links.
* The API is currently a very early labs project. It is about as reliable as a devolution promise from Westminster.
* The API is run on a pair of raspberry-pi’s connected to the internet via bluetooth.
* It is not fast.
* The representation and the API is under active development.Things will change. Watch the Crossref Labs site for updates on this collaboration with DataCite
