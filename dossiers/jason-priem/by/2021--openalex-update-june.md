---
title: "MAG replacement update: meet OpenAlex!"
person: jason-priem
section: by
type: blog-post
year: 2021
date: 2021-06-13
venue: "OurResearch blog"
authors: "Jason Priem"
source_url: https://blog.openalex.org/openalex-update-june/
retrieved: 2026-08-13
content: full-text
notes: "Byline from WordPress author field (user 'jason') on the merged Impactstory/OurResearch/OpenAlex blog. Originally published on blog.ourresearch.org."
---

# MAG replacement update: meet OpenAlex!

## Full text

Last month, we [announced](https://blog.ourresearch.org/were-building-a-replacement-for-microsoft-academic-graph/) that we’re launching a replacement for Microsoft Academic Graph (MAG) this December–just before MAG itself will be [discontinued](https://www.microsoft.com/en-us/research/project/academic/articles/microsoft-academic-to-expand-horizons-with-community-driven-approach/).  We’ve heard from a *lot* of current MAG users since then. All of them have offered their support and encouragement (which we really appreciate), and all have also all been curious to learn more. So: here’s more! It’s a snapshot of what we know right now.  As the project progresses, we’ll have more details to share, keeping everyone as up-to-date as we can.

# Name

We’ve now got a name for this project: **OpenAlex**. We like that it (a) emphasizes Open, and (b) is inspired by the ancient Library of Alexandria — like that fabled institution, OpenAlex will strive to create a comprehensive map of the global scholarly conversation. We’ll start with MAG data, and we’ll expand over time. Along with the name, we’ve got the beginnings of a webpage at [openalex.org](https://openalex.org), and a Twitter account at [@OpenAlex_org](https://twitter.com/openalex_org).

# Mailing list

We’ve now got a mailing list where you can sign up for more announcements as they happen. You can sign up for the mailing list on the new [OpenAlex homepage.](https://openalex.org)

# Funding

Our nonprofit OurResearch [recently received](https://blog.ourresearch.org/arcadia-2021-grant/) a \$4.5 million grant from the Arcadia Fund, a charitable fund of Lisbet Rausing and Peter Baldwin. This grant has been in the works for some time, and is a big part of why we felt confident in announcing OpenAlex when we did. In the proposal, there was already a plan for a project similar to OpenAlex, so we were able to quickly pivot the grant details to direct about a million dollars to the development of OpenAlex. 

It’s a three year grant, which will give us plenty of time to develop and launch OpenAlex, as well as test and launch a long-term revenue. This model will not be built on selling data (see Openness below), but rather based on selling value-added services and service level agreements. We’ve got experience with this approach: we’re funding [Unpaywall](https://unpaywall.org) this way, and it’s been both open and fully self-sustaining for several years now.

# Openness

We’re passionate about openness. It’s the “Our” in our name–we think research should belong to all of us, as humans.  Openness is the first of [core values](https://ourresearch.org/#values), and it’s a big piece of our recent [public commitment](https://blog.ourresearch.org/posi/) to the [Principles of Open Scholarly Infrastructure (POSI)](https://openscholarlyinfrastructure.org/). A lot of our excitement about OpenAlex comes from the chance to make this rich dataset unprecedentedly open.  Specifically:

- The code will be open source under an MIT license, hosted on our [GitHub account](https://github.com/ourresearch) and backed up by Software Heritage.
- The data will be as openly licensed as possible. Some of the data consists of facts, which have no copyright (see [this Crossref post](https://www.crossref.org/blog/crossrefs-board-votes-to-adopt-the-principles-of-open-scholarly-infrastructure/) for more about that idea). Where copyright is applicable, and where we have the option, we’ll apply the CC0 waiver. Where other rightsholders are involved, we will encourage them to allow a similarly open license.
- The data will be free, as in no cost. It will be available via a free API (more details below) with generous limits, as well as periodic data dumps available at no charge (we may require the downloader to cover the 3rd party data transfer fees if these get heavy).

# Data we are losing (at least to start)

As mentioned in our initial announcement, OpenAlex will be missing some data that MAG currently has–particularly at our launch in 2021, due to the very tight timeline. More accurately, we’ll have this data, but won’t be keeping it up to date. Specifically we won’t have: 

- Conference Series and Conference Instances. Importantly, we’ll continue to bring in the vast majority of conference *papers.* But won’t be keeping track of  new conferences themselves (eg, The 34th Annual Conference of Foo), and with that the ability to link conference papers to those conferences.
- Citation Contexts (the full text of the paragraph where each citation originally appeared)
- Most abstracts. We will however probably have those (minority of) abstracts that publishers send Crossref or PubMed for redistribution.
- Full coverage of DOI-unassigned works:. MAG is particularly good at finding scholarly papers without a DOI. We’ll be less good, especially at first. We *will* include many DOI-unassigned works…just not as many as MAG.

There is some other data that may or may not make it into OpenAlex by December 2021. We are still testing these for feasibility:

- Patents
- Paper recommendations

# Data we are adding

Although we’ll be missing some data, we’ll also be bringing some new data to the party — stuff MAG doesn’t have right now. Specifically will include:

- The Open Access status of papers (via the Unpaywall dataset, which has become [the industry standard](https://unpaywall.org/integrations)). We’ll be able to tell you whether a given paper is OA or not, its copyright license, and where to find it. 
- A more comprehensive list of ISSNs associated with each journal, including the [ISSN-L](https://www.issn.org/understanding-the-issn/assignment-rules/the-issn-l-for-publications-on-multiple-media/), which is helpful for deduplicating journals.
- [ORCID](https://orcid.org/) for author clusters. To start with, this will just be in unambiguous cases, when assignment is clear via the Crossref and ORCID datasets. Over time we may apply fancier, more inferential assignments.
- [ROR IDs](https://ror.org/) for institutions, in addition to GRIDs

Over the long term, our goal with OpenAlex is to create a truly comprehensive map of the global scholarly conversation, so we’ll be continually looking to  expand and enhance the data it includes.

# Data dumps

There will be (at least) two ways to get at the data: data dumps, and the API (below). 

Data dumps will be in the same table/column format as the MAG data, so that the downloads can be a drop-in replacement. There may be some additional tables and additional columns for new data we’re adding, and some data values will be missing (both of these are described above), but if you’re running code to ingest MAG dumps right now, you’ll be able to run pretty much the same code to ingest OpenAlex dumps in December. That’s a really important part of this project for us, because we know it will save a lot of folks a lot of time.

We will release new data dumps every 2 weeks, as either a full dump or an incremental update or both (we’re still looking into that). The data will likely be hosted on AWS S3 rather than Microsoft Azure.

# API 

The other way main to get at the data will be via the API. Here we will be doing it pretty differently than Microsoft. We will *not* be supporting the Microsoft Academic Knowledge API or Microsoft Academic Knowledge Exploration Service (MAKES). Instead, we will host a central, open REST API that anyone can query. This API will have two kinds of endpoints: entity endpoints, and slice-and-dice endpoints. Both will be read-only (GET), deliver data in JSON format, and be rate-limited but with high rate-limits. 

- Entity endpoints will let you quickly retrieve a specific scholarly entity (eg paper, person, journal, etc) by its ID. Signatures will look like ** /doi/:doi** and **/journal/:issn**.
- Slice-and-dice endpoints will let you query the data with filters to return either item lists, or aggregate group counts. An example call might look something like **/query?filter=issn:2167-8359,license:cc-by&groupby=year** (that would give you the annual counts of CC-BY-licensed articles from the journal PeerJ). You could also use the slice-and-dice endpoints to do things like build a faceted scholarly search engine, or an evaluation tool.

# Timeline

We appreciate that having a scheduled beta (or alpha!) release of the API and data dump would be very helpful. And we further realize that the sooner we can let you know that schedule, the better. Unfortunately, we don’t know the timeline for these releases yet. Our current best guess is the early fall. We’ll certainly be doing our best to get something pushed out there as soon as possible. We encourage you to  join the [mailing list](http://eepurl.com/hA8PhL) so we can keep you up to date. 

# Your comments

Finally, we welcome your comments and questions! We’ve gotten oodles of helpful feedback already, and we really appreciate that. We’re especially interested in getting your *current* use-case for MAG…we’re working to prioritize supporting those cases, first and foremost.  You can do that via our [community survey here](https://forms.gle/eRKKsALP8mqHRkNbA), or drop us a line at <team@ourresearch.org>.
