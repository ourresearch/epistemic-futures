---
title: "Distributing references via Crossref"
person: "geoffrey-bilder"
section: "by"
type: "blog-post"
year: 2016
date: 2016-06-17
venue: "Crossref blog"
authors: "Geoffrey Bilder"
source_url: "https://www.crossref.org/blog/distributing-references-via-crossref/"
retrieved: "2026-08-13"
content: "full-text"
notes: "Crossref blog post. DOI 10.64000/2716c-59p23."
---

# Distributing references via Crossref

## Full text

**3 minute read.**

## Distributing references via Crossref

## Known unknowns

If you follow this blog, you are going to notice a theme over the coming months- Crossref supports the deposit and distribution of [a lot more kinds of metadata](/blog/beyond-the-doi-to-richer-metadata/) than people usually realise.

We are in the process of completely revamping our web site, help documentation, and marketing to better promote our metadata distribution capabilities, but in the mean time we think it would be useful highlight one of our most under-promoted functions- the ability to distribute references via Crossref.

One of the questions we most often get from members is- “can we distribute references via Crossref?” The answer is an emphatic **yes**. But to do so, you have to take an extra and hitherto obscure step to enable reference distribution.
*[EDIT 6th June 2022 - all references are now open by default with the March 2022 board vote to remove any restrictions on reference distribution].*

## How?

Many members deposit references to Crossref as part of their participation in Crossref’s [Cited-by](http://www.crossref.org/Cited-by/index.html) service. However - for historical reasons too tedious to go into - participation in Cited-by does not automatically make references available via Crossref’s standard APIs. In order for publishers to distribute references along with standard bibliographic metadata, publishers need to either:

* Contact Crossref [support](mailto:support@crossref.org) and ask them to turn on reference distribution for all of the prefixes they manage.
* Set the [`reference_distribution_opt`](http://data.crossref.org/reports/help/schema_doc/4.4.1/schema_4_4_1.html#reference_distribution_opts.att) element to `any` for each content item registered where they want to make references openly available.

Either of these steps will allow references for the affected member DOIs to be distributed without restriction through all of Crossrefs APIs and bulk metadata dumps.

Note that by doing this, you are **not** enabling the open querying of your Cited-by data- you are simply allowing the references that you already deposit to be redistributed to interested parties via our public APIs.

## Who?

So who does this now? Well, at the moment not many members have enabled this feature. How could they? They probably didn’t know it existed.  At the time of writing this 29 publishers have enabled reference distribution for at least some of their DOIs.

But that’s why we are writing this post. Given the interest expressed by our members, we expect the list to start growing quickly over the next few months. Particularly now that they know they **can** do it and have clear instructions on **how** to do it. 🙂

If you are of a geeky persuasion and want to see the list of publishers who are doing this, you can check via our API.

The following query will just show you the total number of members who are distributing references for at least some of their DOIs.

https://api.crossref.org/v1/members?filter=has-public-references:true&rows=0

And this query will allow you to page through the member records and see who is distributing references.

https://api.crossref.org/v1/members?filter=has-public-references:true

That cool, but can you see how many total DOIs have reference distribution enabled? No, but will will be adding that capability to our API soon.

## OMG! OMG! OMG! Does this mean I can get references from api.crossref.org?

~~Yep. But before you get too excited- note above that not many of our members are doing this yet and that our API is still being updated to allow you to better query this information. At the moment references are not included in our JSON representation- they are only included in our XML representation. You can get the XML for a Crossref DOI either through [content negotiation](http://www.crosscite.org/cn/), or by using the following incantation on our API (using an [eLife](https://elifesciences.org/) DOI as an example):~~

~~`https://api.crossref.org/v1/works/10.7554/eLife.10288.xml`~~

~~As we update our API to better support querying DOIs that include references, you will see the new functionality reflected in our documentation at:~~

**Yes.** 🤗. See the API docs below.

[`https://api.crossref.org`](https://api.crossref.org)
