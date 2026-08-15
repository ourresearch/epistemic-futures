---
title: "Dean Krafft on the Linked Data for Libraries project"
person: david-weinberger
section: by
type: blog-post
year: 2014
date: 2014-03-18
venue: "Joho the Blog (hyperorg.com)"
authors: "David Weinberger"
source_url: https://hyperorg.com/2014/03/18/dean-krafft-on-the-linked-data-for-libraries-project/
retrieved: 2026-08-13
content: full-text
notes: "Post from Joho the Blog (hyperorg.com), Weinberger's personal blog. Retrieved via the site's WordPress REST API; HTML converted to plain text."
---

# Dean Krafft on the Linked Data for Libraries project

## Full text

Dean Krafft, Chief Technology Strategist for Cornell University Library, is at Harvard to talk about the Mellon-funded Linked Data for Libraries (LD4L) project he leads. The grantees include Cornell, Stanford, and the Harvard Library Innovation Lab (which is co-sponsoring the talk with ABCD). (I provide nominal leadership for the Harvard team working on this.)

NOTE: Live-blogging. Getting things wrong. Missing points. Omitting key information. Introducing artificial choppiness. Over-emphasizing small matters. Paraphrasing badly. Not running a spellpchecker. Mangling other people’s ideas and words. You are warned, people.

Dean will talk about the LD4L project by talking about its building blocks. [Dean had lots of information and a lot on the slides. I did a particularly bad job of capturing it.]

Ld4L

Mellon last December put up $1M for a 2-year project that will end in Dec. 2015. The participants are Cornell, Stanford, and the Harvard Library Innovation Lab.

Cornell: Dean Krafft, Jon Corso-Rickert, Brian Lowe, Simeon Warner

Stanford: Tom Cramer, Lynn McRae, Naomi Dushay, Philip Schreur

Harvard: Paul Deschner, Paolo Ciccarese, me

Aim: Create a Scholarly Resource Semantic Info Store model that works within and across institutions to create a network of Linked Open Data to capture the intellectual value that librarians and other domain experts add to info, patterns of usage, and more.

Ld4L wants to have a common language for talking about scholarly materials. – Outcomes: – Create a SRSIS ontology sufficiently expressive to encompass catalog metadata and other contextual elements – Create a SRSIS semantic editing display, and discovery system based on Vitro to support the incremental ingest of semantic data from multiple info sources – Create a Project Hydra-compatible interface to SRSIS, an active triples software component to facilitate easy use of the data

Why use Linked Data?

LD puts the emphasis on the relationships. Everything is related.

Benefits: The connections have meaning. And it supports “many dimensions of nearness”

Dean explains RDF triples. They connect subjects with objects via a consistent set of relationships.

A nice feature of LOD is that the same URL that points to a human-readable page can also be taken as a query to show the machine-readable data.

There’s commonality among references: shared types, shared relationships, shared instances defined as types and linked by relationships.

LOD is great for sharing data. There’s a startup cost, but as you share more data repositories and types, the costs/effort goes up linearly, not at the steeper rate of traditional approaches.

Dean shows the mandatory graphic of a cloud of LOD sources.

Building Blocks

VIVO: Vivo was the inspiration for LD4L. It makes info about researchers discoverable. It’s software, data, a standard, and a community. It connects scientists and scholars through their research and scholarship. It provides self-describing data via shared ontologies. It provides search results enhanced by what it knows. And it does simple reasoning.

Vivo is built on the VIVO/Vitro platform. It has ingest tools, ontology editing tools, instance editing tools, and a display system. It models people, organizations, grants, etc., the relationships among them, and links to URIs elsewhere. It describes people in the process of doing research. It’s discipline-neutral. It uses existing domain terminology to describe the content of research. It’s modular, flexible, and extensible.

VIVO harvests much of its data automatically from verified sources.

It takes a complexity of inputs and makes them discoverable and usable.

All the data in VIVO is public and visible.

Dean shows us a page, and then traverses the network of interrelated authors.

He points out that other institutions are able to mash up their data with VIVO. E.g., the ICTS has info about 1.2M publications that they’ve integrated with VIVO’s data. E.g., you can see research papers created with federal funding but not deposited in PubMed Central.

VIVO is extensible. LASP extended VIVO to include spacecraft. Brown U. is extending it to support the humanities and artistic works, adding “performances,” for example.

The LD4L ontology will use components of the VIVO-ISF ontology. When new ontologies are needed, it will draw upon VIVO design patterns. The basis for SRSIS implementations will be Vitro plus LD4L ontologies. The multi-institution LD4L demo search will adapt VIVOsearch.org.

The 8M items at Cornell have generated billions of triples.

Project Hydra. Hydra is a tech suite and a partnership. You put your data there and can have many different apps. 22 institutions are collaborating.

Fundamental assumption: No single system can provide the full range of repository-based solutions for a given institution’s needs, yet sustainable solutions do require a common repository. Hydra is now building a set of “heads” (UI’s) for media, special collections, archives, etc.

Fundamental assumption: No single institution can build the full range of what it needs, so you need to work with others.

Hydra has an open architecture with many contributors to a common core. There are collaboratively built solution bundles.

Fedora, Ruby on Rails for Blacklight, Solr, etc.

LD4L will create an activeTriples Hyrdra component to mimic ActiveFedora.

Our Lab’s LibraryCloud/ShelfRank is another core element. It provides model for access to library data. Provides concrete example for creating an ontology for usage.

LD4L – the project

We’re now developing use cases. We have 32 on the wiki. [See the wiki for them]

We’re identifying data sources: Biblio, person (VIVO), usage (LibCloud, circ data, BorrowDirect circ), collections (EAD, IRs, SharedShelf, Olivia, arbitrary OAI-PMH), annotations (CuLLR, Stanford DMW, Bloglinks, DBpedia LibGuides), subjects and authorities (external sources). Imagine being able to look at usage across 50 research libraries…

Assembling the Ontology:

VIVO, Open Annotation, SKOS

BibFrame, BIBO, FaBIO

PROV-O, PAV

FOAF, PROVE, Schema.org

CreativeCommons, Dublin Core

etc.

Whenever possible the project will use existing ontologies

Timeline: By the end of the year we hope to be piloting initial ingests.

Workshop: Jan. 2015. 10-12 institutions. Aim: get feedback, make a “sales pitch” to other organizations to join in.

June 2015: Pilot SRSIS instances at Harvard and Stanford. Pilot gather info across all three instances.

Dec. 2015: Instances implemented.

wiki: http://wiki.duraspace.org/display/ld4l

Q&A

Q: Who anointed VIVO a standard?

A: It’s a de facto.

Q: SKOS is considered a great start, but to do anything real with it you have to modify it, and if it changes you’re screwed.

A: (Paolo) I think VIVO uses SKOS mainly for terms, not hierarchies. But I’m not sure.

Q: What are ActiveTriples?

A: It’s a Ruby Gem that serves as an interface for Hydra into a Fedora repository. ActiveTriples will serve the same function for a backend triple store. So you can swap different triple stores into the Fedora repository. This is Simeon Warner’s project.

Q: Does this mean you wouldn’t have to have a Fedora backend to take advantage of Hydra?

A: Yes, that’s part of it.

Q: Are you bringing in GIS linked data?

A: Yes, to the extent that we can and it makes sense to.

A: David Siegel: We have 6M data points from 1.1M Hollis records. LibraryCloud is ingesting them.

Q: What’s the product at the end?

A: We promised Mellon the ontology and instances of LOD based on the ontology at each of the 3 institutions, and search across the three.

Q: Harvard doesn’t have a Fedora backend…

A: We’d like to pull from non-catalog sources. That might well be an OAI-PMH ingest, or some other non-Fedora source.

Q: What is Simeon interested in with regard to Arxiv.org?

A: There isn’t a direct relationship.

Q: He’s also working on ORCID.

A: We have funding to do some level of integration of ORCID and VIVO.

Q: What is the bibliographic scope? BibFrame isn’t really defining items, etc. They’ve pushed it into annotations.

A: We’re interested in capturing some of that. BibFrame is offering most of what we need, but we have to look at each case. Then we communicate with them and hope that BibFrame does most of the work.

Q: Are any of your use cases posit tagging of contents, including by users perhaps with a controlled vocabulary?

A: We’ll be doing tagging at the object level. I’m unsure whether we’re willing to do tagging within the object.

A: [paolo] We assume we don’t have access to the full text.

A: You could always point into our data.

Q: How can we help?

A: We’re accumulating use cases and data sources. If you’re aware of any, let us know.

Q: It’s been hard for libraries to put enough effort into authority control, to associate values comparable across different subject schemes…there’s a lot of work to make things work together. What sort of vocabulary or semantic links will you be using? The hard part is getting values to work across domains.

A: One way to deal with that is to bring together the disparate info. By pulling together enough info, you can sometimes use the network to you figure that out. But in general the disambiguation challenge (and text fields are even worse) is not something we’re going to solve.

Q: Are the working groups institutionally based?

A: No. They’re cross-institution.

[I’m very excited about this project, and about the people working on it.]
