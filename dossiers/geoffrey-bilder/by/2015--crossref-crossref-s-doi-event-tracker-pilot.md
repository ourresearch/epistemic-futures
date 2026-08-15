---
title: "Crossref’s DOI Event Tracker Pilot"
person: "geoffrey-bilder"
section: "by"
type: "blog-post"
year: 2015
date: 2015-03-02
venue: "Crossref blog"
authors: "Geoffrey Bilder"
source_url: "https://www.crossref.org/blog/crossrefs-doi-event-tracker-pilot/"
retrieved: "2026-08-13"
content: "full-text"
notes: "Crossref blog post. DOI 10.64000/pehk0-2ap79."
---

# Crossref’s DOI Event Tracker Pilot

## Full text

**11 minute read.**

## Crossref’s DOI Event Tracker Pilot

## TL;DR

Crossref’s “DOI Event Tracker Pilot”- 11 million+ DOIs & 64 million+ events. You can play with it at: <http://goo.gl/OxImJa>

## Tracking DOI Events

So have you been wondering what we’ve been doing [since we posted about the experiments we were conducting using PLOS’s open source ALM code](/blog/many-metrics-such-data-wow/)? A lot, it turns out. About a week after our post, we were contacted by a group of our members from [OASPA](http://oaspa.org/) who expressed an interest in working with the system. Apparently they were all about to conduct similar experiments using the ALM code, and they thought that it might be more efficient and interesting if they did so together using our installation. Yippee. Publishers working together. That’s what we’re all about.

So we convened the interested parties and had a meeting to discuss what problems they were trying to solve and how Crossref might be able to help them. That early meeting came to a consensus on a number of issues:

* The group was interested in exploring the role Crossref could play in providing an open, common infrastructure to track activities around DOIs, they were not interested in having Crossref play a role in the value-add services of reporting on an interpreting the meaning of said activities.
* The working group needed representatives from multiple stakeholders in the industry. Not just open access publishers from OASPA, but from subscription based publishers, funders, researchers and third party service providers as well.
* That it was desirable to conduct a pilot to see if the proposed approach was both technically feasible and financially sustainable.

And so after that meeting, the “experiment” graduated to becoming a “pilot.” This Crossref pilot is based on the premise that the infrastructure involved in tracking common information about “DOI events” can be usefully separated from the value-added services of analysing and presenting these events in the form of qualitative indicators. There are many forms of events and interactions which may be of interest. Service providers will wish to analyse, aggregate and present those in a range of different ways depending on the customer and their problem. The capture of the underlying events can be kept separate from those services.

In order to ensure that the Crossref pilot is not mistaken for some sub rosa attempt to establish new metrics for evaluating scholarly output, we also decided eschew any moniker that includes the word “metrics” or synonyms. So the “ALM Experiment” is dead. Long live the “”DOI Event Tracker” (DET) pilot. Similarly PLOS’s [open source “ALM software”](https://github.com/articlemetrics/lagotto) has been resurrected under the name “[Lagotto](http://en.wikipedia.org/wiki/Lagotto_Romagnolo).”

## The Technical Issues

Crossref members are interested in knowing about “events” relating to the DOIs that identify their content. But our members face a now-classic problem. There are a large number of sources for scholarly publications (3k+ Crossref members) and that list is still growing. Similarly, there are an unbounded number of potential sources for usage information. For example:

* Supplemental and grey literature (e.g. data, software, working papers)
* Orthogonal professional literature (e.g. patents, legal documents, governmental/NGO/IGO reports, consultation reports, professional trade literature).
* Scholarly tools (e.g. citation management systems, text and data mining applications).
* Secondary outlets for scholarly literature (institutional and disciplinary repositories, A&I services).
* Mainstream media (e.g. BBC, New York Times).
* Social media (e.g. Wikipedia, Twitter, Facebook, Blogs, Yo).

Finally, there is a broad and growing audience of stakeholders who are interested in seeing how the literature is being used. The audience includes publishers themselves as well as funders, researchers, institutions, policy makers and citizens.

Publishers (or other stakeholders) could conceivably each choose to run their own system to collect this information and redistribute it to interested parties. Or they can work with a vendor to do the same. But either case, they would face the following problems:

* The N sources will change. New ones will emerge. Old ones will vanish.
* The N audiences will change. New ones will emerge. Old ones will vanish.
* Each publisher/vendor will need to deal with N source’s different APIs, rate limits, T&Cs, data licenses, etc. This is a logistical headache for both the publishers/vendors and for the sources.
* Each audience will need to deal with N publisher/vendor APIs, rate limits, T&Cs, data licenses, etc. This is a logistical headache for both the audiences and for the publishers.
* If publishers/vendors use different systems which in turn look at different sources, it will be difficult to compare or audit results across publishers/vendors.
* If a journal moves from one publisher to another, then how are the metrics for that journal’s articles going to follow the journal?

And then there is the simple issue of scale. Most parties will be interested in comparing the data that they collect for their own content, with data about their competitors. Hence, if they all run their own system, they will each be querying much more than their own data. If, for example, just the commercial third-party providers were interested in collecting data covering the formal scholarly literature, they would *each* find themselves querying the same sources for the same 80 million DOIs. To put this into perspective, to refresh the data for 10 million DOIs once a month, would require sources to support ~ 14K API calls an hour. 60 million DOIs would require 100K API calls an hour. Current standard API caps for many of the sources that people are interested in querying hover around 2K per hour. We may see these sources lift that cap for exceptional cases, but they are unlikely to do so for many different clients all of whom are querying essentially the same thing.

These issues typify the “multiple bilateral relationships” problem that Crossref was founded to try and ameliorate. When we have many organisations trying to access the exact same APIs to process the exact same data (albeit to different ends), then it seems likely that Crossref could help make the process more efficient.

## Piloting A Proposed Solution

The Crossref DET pilot aims to show the feasibility of providing a hub for the collection, storage and propagation of DOI events from multiple sources to multiple audiences.

### Data Collection

* **Pull**: DET will collect DOI event data from sources that are of common interest to the membership, but which are unlikely to make special efforts to accommodate the scholarly communications industry. Examples of this class of source include large, broadly popular services like FaceBook, Twitter, VK, Sina Weibo, etc.
* **Push**: DET will allow sources to send DOI event data directly to Crossref in one of three ways:
  + Standard Linkback: Using standards that are widely used on the web. This will automatically enable linkback-aware systems like WordPress, Moveable Type, etc. to alert DET to DOI events.
  + Scholarly Linkback: A to-be-defined augmented linkback-style API which will be optimized to work with scholarly resources and which will allow for more sophisticated payloads including other identifiers (e.g. ORCIDs, FundRefs), metadata, provenance information and authorization information. This system could be used by tools designed for scholarly communications. So, for example, it could be used by publisher platforms to distribute events related to downloads or comments within their discussion forums. It could also be used by third party scholarly apps like Zotero, Mendeley, Papers, Authorea, IRUS-UK, etc. in order to alert interested parties in events related to specific DOIs.
  + **Redirect**: DET will also be able to serve as a service discovery layer that will allow sources to push DOI event data directly to an appropriate publisher-controlled endpoint using the above scholarly linkback mechanism. This can be used by sources like repositories in order to send sensitive usage data directly to the relevant publishers.

### Data Propagation

Parties may want to use the DET in order to propagate information about DOI events. The system will support two broad data propagation patterns:

* **one-to-many**: DOI events that are commonly harvested (pulled) by the DET system from a single source will be distributed freely to anybody who queries the DET API. Similarly, sources that push DOI events via the standard or scholarly linkback mechanisms, will also propagate their DOI events openly to anybody who queries the DET API. DOI events that are propagated in either of these cases will be kept and logged by the DET system along with appropriate provenance information. This will be the most common, default propagation model for the DET system.
* **one-to-one**: Sources of DOI events can also report (push) DOI event data directly to owner of the relevant DOI *if* the DOI owner provides & registers a suitable end-point with the DET system. In these cases, data sources seeking to report information relating to a DOI, will be redirected (with a suitable 30X HTTP status and relevant headers) to the end-point specified by the DOI owner. The DET system will not keep the request or provenance information. One-to-one propagation model is designed to handle use cases where the source of the DOI event has put restrictions on the data and will only share the DOI events with the owner (registrant) of the DOI. This use case may be used, for example, by aggregators or A&I services that want to report confidential data directly back to a publisher. The advantage of the redirect mechanism is that Crossref is not put into the position of having to secure sensitive data as said data will never reside on Crossref systems.

Note that the two patterns can be combined. So, for example, a publisher might want to have public social media events reported to the DET and propagated accordingly, but to also to private third parties report confidential information directly to the publisher.

## So Where Are We?

So to start with, the DET Working Group has grown substantially since the early days and we have representatives from a wide variety of stakeholders. The group includes:

* Cameron Neylon, PLOS
* Chris Shillum, Elsevier
* Dom Mitchell, Co-action Publishing
* Euan Adie, Altmetric
* Jennifer Lin, PLOS
* Juan Pablo Alperin, PKP
* Kevin Dolby, Wellcome Trust
* Liz Ferguson, Wiley
* Maciej Rymarz, Mendeley
* Mark Patterson, eLife
* Martin Fenner, PLOS
* Mike Thelwell, U Wolverhampton
* Rachel Craven, BMC
* Richard O’Beirne, OUP
* Ruth Ivimey-Cook, eLife
* Victoria Rao, Elsevier

As well as the usual contingent of Crossref cat-herders including: Geoffrey Bilder, Rachael Lammey & Joe Wass.

When we announced the then-DET experiment, we said that one of the biggest challenges would be to create something that scaled to industry levels. At launch, we only loaded in about 317,500+ Crossref DOIs representing publications from 2014 and we could see the system was going to struggle. Since then Martin Fenner and Jennifer Lin at PLOS have been focusing on making sure that the Lagotto code scales appropriately and now it is currently humming along with just over 11.5 million DOIs for which we’ve gathered over 64 million “events.” We aren’t worried about scalability on that front any more.

We’ve also shown that third parties should be able to access the API to provide value added reporting and metrics. As a demonstration of this, [PLOS configured a copy of its reporting software “Parascope”](https://web.archive.org/web/20150924184918/http://parascope.crowdometer.org/) to point at the Crossref DET instance. The next step we’re taking is to start testing the “push” API mechanism and the “point-to-point redirect” API mechanism. For the push API, we should have a really exciting demo available to show within the next few days. And on the point-to-point redirect, we have a sub-group exploring how the point-to-point redirect mechanism could potentially be used for reporting [COUNTER](http://www.projectcounter.org/about.html) stats as a compliment to the [Sushi](http://www.niso.org/workrooms/sushi) initiative.

The other major outstanding task we have before us is to calculate what the costs will be of running the DET system as a production service. In this case we expect to have some pretty accurate data to go on as we will have had close to half a year of running the pilot with a non-trivial number of DOIs and sources. Note that the work group is concerned to ensure that the underlying data from the system remains open to all. Keeping this raw data open as seen as critical to establishing trust in the metrics and reporting systems that third parties build on the data. The group has also committed to leaving the creation of value-add services to third parties. As such we have been focusing on exploring business models based around service-level-agreement backed versions of the API to complement the free version of the same API. The free API will come with no guarantees of uptime, performance characteristics or support. For those users that depend on the API in order to deliver their services, we will offer paid-for SLA-backed versions of the free APIs. We can then configure our systems so that we can independently scale these SLA-backed APIs in order to meet SLA agreements.

Our goal is to have these calculations complete in time for the working group to make a recommendation to the Crossref board meeting in July 2015.

Until then, we’ll use CrossTech as a venue for notifying people when we’ve hit new milestones or added new capabilities to the DET Pilot system.
