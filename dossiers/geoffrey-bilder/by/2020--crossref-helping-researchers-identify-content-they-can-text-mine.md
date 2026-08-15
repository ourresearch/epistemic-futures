---
title: "Helping researchers identify content they can text mine"
person: "geoffrey-bilder"
section: "by"
type: "blog-post"
year: 2020
date: 2020-04-16
venue: "Crossref blog"
authors: "Geoffrey Bilder"
source_url: "https://www.crossref.org/blog/helping-researchers-identify-content-they-can-text-mine/"
retrieved: "2026-08-13"
content: "full-text"
notes: "Crossref blog post. DOI 10.64000/2dkpt-h4159."
---

# Helping researchers identify content they can text mine

## Full text

**2 minute read.**

## Helping researchers identify content they can text mine

## TL;DR

Many organisations are doing what they can to aid in the response to the COVID-19 pandemic. Crossref members can make it easier for researchers to identify, locate, and access content for text mining. In order to do this, members must include elements in their metadata that:

* Point to the full text of the content.
* Indicate that the content is available under an open access license or that it is being made available for free (gratis).

## How to do it.

### If your content is open access

Make sure the Crossref metadata for all of your open access content includes:

1. The URL of the open access license the content is under.
2. A URL that points to the full text of the content on your site (PDF, XML or HTML).

[Instructions for including license and full text URLs in your metadata.](/education/retrieve-metadata/rest-api/text-and-data-mining-for-members/)

### If you are making subscription content available for text mining (temporarily or otherwise).

Make sure the Crossref metadata for the content you are making freely available for text mining includes:

1. The URL of the publisher license the content is under.
2. A URL that points to the full text of the content where it is being made freely available (PDF, XML or HTML). This might not be on your site.

[Instructions for including license and full text URLs in your metadata.](/education/retrieve-metadata/rest-api/text-and-data-mining-for-members/)

In addition, you need to flag the content that you are making freely available.

3. A “free to read” element in the access indicators section of your metadata indicating that the content is being made available free-of-charge (gratis).
4. An assertion element indicating that the content being made available is available free-of-charge.

[Instructions for flagging your content as “free”](/flagging-free-to-read/)

Note that step #4 is required in order for users to be able to find content marked as “gratis” in Crossref’s REST API.

And if you decide to revoke the free access in the future, you will need to update the data to reflect that restrictions have been reimposed.

## Sounds great. Has anybody else actually done this?

*Yes.*

Over 43 million metadata records already have a license and a full text link. <https://api.crossref.org/works?filter=has-license:true,has-full-text:true&rows=0>

Millions of the above items have one of the [Creative Commons](https://creativecommons.org/) licenses or a dedicated text and data mining license provided by the publisher.

And in the past three weeks (as of the writing of this blog post) over 23,000 articles have been flagged as “free” so they are available for text mining.

<https://api.crossref.org/v1/works?filter=assertion:free,has-full-text:true>
