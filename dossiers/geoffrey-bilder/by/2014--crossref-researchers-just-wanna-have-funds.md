---
title: "♫ Researchers just wanna have funds ♫"
person: "geoffrey-bilder"
section: "by"
type: "blog-post"
year: 2014
date: 2014-04-10
venue: "Crossref blog"
authors: "Geoffrey Bilder"
source_url: "https://www.crossref.org/blog/researchers-just-wanna-have-funds/"
retrieved: "2026-08-13"
content: "full-text"
notes: "Crossref blog post. DOI 10.64000/6fp15-79a77."
---

# ♫ Researchers just wanna have funds ♫

## Full text

**6 minute read.**

## ♫ Researchers just wanna have funds ♫

[photo credit](https://www.flickr.com/photos/59935931@N05/5788184739/)

## Summary

You can use a new Crossref [API](http://en.wikipedia.org/wiki/Application_programming_interface) to query all sorts of interesting things about who funded the research behind the content Crossref members publish.

## Background

Back in May 2013 we launched Crossref’s [FundRef](https://www.crossref.org/services/funder-registry/) service. It can be summarized like this:

* Crossref keeps and manages a [canonical list](https://www.crossref.org/services/funder-registry/) of Funder Names (ephemeral) and associated identifiers (persistent).
* We encourage our members (or anybody, really- the list is available under A [CC-Zero](http://creativecommons.org/choose/zero/) license waiver) to use this list for collecting information on who funded the research behind the content that our members publish.
* We then ask that our members deposit this data in their normal Crossref metadata deposits.

And that was cool.

But then people started asking us awkward questions. Questions like “what can I do with the funder data?” and “how do I query it?”.

Stoopit people.

Can’t you just let us bask for a few minutes in the sunny glow of actually conceiving of and launching a project within a year?

But seriously, funders, were interested to see how they could use the funder metadata being collected in Crossref. In particular, some funding agencies were interested in being able to measure Key Performance Indicators (“KPIs” to management wonks) related to recent mandates such as the February 22nd 2013 OSTP memo, *[Public Access to the Results of Federally Funded Research](http://www.whitehouse.gov/blog/2013/02/22/expanding-public-access-results-federally-funded-research).* Two groups also approached us, [CHORUS](http://chorusaccess.org/) and [SHARE](https://www.arl.org/resources/shared-access-research-ecosystem-share-proposal/). Both are interested in exploring how to build reporting tools for funders, institutions and researchers and each brought us a gigantic hairball of use-cases they were hoping we would be able to meet.

Conveniently, we were in the process of creating a revised, modern Crossref API that is entirely [buzzword-compliant](http://en.wikipedia.org/wiki/Buzzword_compliant), and so we set to work…

We thought people might be interested in seeing what you can do with the Crossref [REST](http://en.wikipedia.org/wiki/Representational_state_transfer) API in relation to funding information and the expectations that are increasingly being attached to them. CHORUS is already using the Crossref REST API heavily and we expect that SHARE will soon start making use of it as well. The feedback from both groups has been very useful, but we are looking for broader feedback as well. The API is still in development, so now is your chance to help us shape it.

## Brief Examples

*Please note*, the following are APIs calls, although you can copy and paste the URIs into your browser, the data is returned in a machine readable representation called [JSON](http://en.wikipedia.org/wiki/JSON). If you want the results to look a little more presentable, we advise you install the JSONView plugin:

* Firefox Users: [JSONView](http://jsonview.com/)
* Chrome Users: [JSONView](https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc)

Also note that publishers have only just started to deposit the metadata needed for these APIs to work, so the data is currently sparse. We know that many of our members are working feverishly to populate more of the needed metadata, but this requires updates to the their manuscript tracking systems, production systems and hosting systems. It takes time.

But for now you can paste the relevant URIs below into your browser and see the results that we do have. Expect these numbers to increase sharply over the next few months

To start with, you might want to know how many articles in Crossref have FundRef metadata:

```
https://api.crossref.org/v1/works?filter=has-funder:true&rows=0
```

You could then be interested in knowing how many works in Crossref use FundRef to credit the United States’ National Science Foundation (NSF) for funding their research? First you need to find out what the FundRef identifier is for the NSF:

```
https://api.crossref.org/v1/funders?query=NSF
```

You can see that there are several entries that match “NSF”, and that the one we are looking for has the identifier `http://dx.doi.org/10.13039/100000001`. Remember, funding agency names can change frequently, the ID provides a persistent link to the funder even if their name changes.

If you are curious, you can see the details for the NSF entry, including its location, parent and child organisations:

```
https://api.crossref.org/v1/funders/10.13039/100000001
```

Notice that the results also lists the `work-count`. This is the number of works in the Crossref metadata that list the US NSF as having funded the research.

So perhaps you would like to see the list of works. The following will list the first twenty:

```
https://api.crossref.org/v1/funders/10.13039/100000001/works
```

You can page through the results with the offset argument:

```
https://api.crossref.org/v1/funders/10.13039/100000001/works?offset=20

https://api.crossref.org/v1/funders/10.13039/100000001/works?offset=40

...
```

How many works that have listed the NSF as a funder have license information:

```
https://api.crossref.org/v1/funders/10.13039/100000001/works?filter=has-license:true&rows=0
```

Lets see the first batch that have license information:

```
https://api.crossref.org/v1/funders/10.13039/100000001/works?filter=has-license:true
```

Lets look at the metadata for one of the DOIs returned:

```
https://api.crossref.org/v1/works/10.1063/1.3593378
```

Interesting, the metadata shows an article published by [AIP](http://www.aip.org/). It includes license information (CC-BY 3.0) as well as a link to the full text. If you follow the link to the full text, you can retrieve it:

```
http://link.aip.org/link/applab/v98/i21/p216101/pdf/CHORUS
```

Wow- A pretty short article. But you can see that it does credit the NSF and that the award number recorded in the text is the same as the award number recorded in the FundRef section of the Crossref metadata. Yay.

You can see in the brief examples above that there is a lot of other metadata you may want to query on and explore. It can include ORCIDS, information about archiving arrangements- even abstracts. It all depends on what the Crossref member has decided to provide.

You can get a simple overview of what a Crossref member has provided by looking at a member summary. Here is an example for [Hindawi](http://www.hindawi.com/):

```
https://api.crossref.org/v1/members?query=hindawi
```

Note again that names are fickle, so the above query can also be accomplished using the member identifier like this:

```
https://api.crossref.org/v1/members/98
```

Groovy init?

If you want more pointers on where you can learn how to use the API, read on…

## More examples and documentation.

We have a draft of the [full documentation for the Crossref REST API](https://api.crossref.org). Note that this is undergoing active revision and we ask that you look at the updated documentation if things that once work cease to. We would also love your feedback and suggestions. Send them to:

We often get asked “what metadata does a publisher need to provide in order to enable this kind of functionality?” To answer that, we have developed a document titled [Crossref metadata best practice to support key performance indicators (KPIs) for funding agencies](https://github.com/CrossRef/rest-api-doc/blob/master/funder_kpi_metadata_best_practice.md). Try saying that ten times very fast.

## The Future of the Crossref REST API.

Our aim is for the Crossref REST API to go into production this Summer (2014). As with most of our newer APIs, there will be a free API for public use and a paid for API for professional use. The only difference between the two will be that the professional version will come with a service level agreement (SLA) covering uptime, response time and support. Naturally, this also means that the professional one will be on dedicated hosting equipment so that we can meet these SLAs, whereas the performance of the free version will be subject to the vicissitudes inherent in using a shared, constrained resource (i.e. the server and network it is running on).

Again, the basics of the API are in place. It should be fairly stable, but we do reserve the right to make changes to it over the next few months. Please send us feedback.

— The Weasel
