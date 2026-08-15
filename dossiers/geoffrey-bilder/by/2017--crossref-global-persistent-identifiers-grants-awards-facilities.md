---
title: "Global Persistent Identifiers for grants, awards, and facilities"
person: "geoffrey-bilder"
section: "by"
type: "blog-post"
year: 2017
date: 2017-12-13
venue: "Crossref blog"
authors: "Ginny Hendricks, Geoffrey Bilder"
source_url: "https://www.crossref.org/blog/global-persistent-identifiers-for-grants-awards-and-facilities/"
retrieved: "2026-08-13"
content: "full-text"
notes: "Crossref blog post. DOI 10.64000/5cfh1-1wa10. Co-authored (2 bylines)."
---

# Global Persistent Identifiers for grants, awards, and facilities

## Full text

**12 minute read.**

## Global Persistent Identifiers for grants, awards, and facilities

Crossref’s [Open Funder Registry](https://gitlab.com/crossref/open_funder_registry) (neé FundRef) now includes over 15 thousand entries. Crossref has over 2 million metadata records that include funding information - 1.7 million of which include an Open Funder Identifier. The uptake of funder identifiers is already making it easier and more efficient for the scholarly community to directly link funding to research outputs, but lately we’ve been hearing from a number of people that the time is ripe for a global grant identifier as well.

To that end, Crossref convened its [funder advisory group](/working-groups/funders/) along with representatives from our collaborator organisations, ORCID and DataCite, to explore the creation of a global grant identifier system.

We thought you might like to know about what we’ve been discussing…

### The First Rule of Grant Identifiers

The first rule of grant identifiers is that they probably should not be called “grant identifiers”. Research is supported in a variety of ways—through grants, endowments, secondments, loans, use of facilities/equipment and even crowd-funding. In any of these cases, it is important to be able to link researchers and research outputs to details about the sources of support. This is true for prosaic reasons—to understand ROI, to map the competitive landscape, to ensure that mandates are fulfilled, to avoid double payment. But it is also true for epistemic reasons; understanding how research was funded can help contextualise that research, and help expose potential conflicts of interest or specific agendas.

The [Open Funder Registry](/services/funder-registry/) which provides a coarse mapping between research outputs and funders, but it is becoming clear that we need more fine-grained mapping directly to information about the kind of support that was provided.

Awkwardly, none of us had any great ideas about alternative nomenclature, so we’ve made the eminently practical decision to continue to use the term “grant identifier” whilst being aware that our aim is to define a system that applies more broadly to any form of funding or support of research. So `+1` for practicality.

### Why do we need an open, global, grant identifier?

With the steady increase in research outputs, and the growing number of active researchers from both academia and industry, research stakeholders find they need to be able to automate workflows in order to scale their systems efficiently. Funders want to be able to track the outputs that arise from research they have funded. As a result, institutions find themselves having to regularly analyse and summarise the research their faculty produces. Faculty, in turn, face increasing accounting bureaucracy in order to meet all the reporting requirements that are cascading through the system. And finally, publishers are seeking to make the manuscript submission and evaluation process more efficient as well as to increase the discoverability and contextual richness of their publications.

Most funders already have local, internal grant identifiers. But there are over 15K funders currently listed in the aforementioned Open Funder Registry. The problem is that each funder has its own identifier scheme and (sometimes) API. It is very difficult for third parties to integrate with so many different systems. Open, global, persistent and machine-actionable identifiers are key to scaling these activities.

We already have a sophisticated open, global, interoperable infrastructure of persistent identifier systems for some key elements of scholarly communications. We have persistent identifiers for researchers and contributors (ORCID iDs), for data and software (DataCite DOIs), for journal articles, preprints, conference proceedings, peer reviews, monographs and standards (Crossref DOIs), and for Funders (Open Funder Registry IDs).

And there are similar systems under active development for [research organisations](/categories/organisation-identifier/), [conferences, projects](https://doi.org/10.64000/skv7b-cef25) and [resources](https://scicrunch.org/resources) reported in the biomedical literature (e.g. antibodies, model organisms). At a minimum, open, persistent identifiers address the inherent difficulty in disambiguating entities based on textual strings (structured or otherwise). This precision, in turn, allows automated cross-walking of linked identifiers through APIs and metadata which enable advanced applications.

For example, the use of identifiers can simplify user interfaces and save users time. Almost everybody in scholarly communications spends a frustrating portion of their lives copying information from one system to another. This process is not just tedious, it is also error-prone. But we are increasingly seeing systems make use of identifiers to eliminate the need for a lot of this manual copying. For example, researchers using an ORCID iD when they submit a manuscript can start to expect that their relevant ORCID biographical data will simply be imported into the manuscript tracking system so that it doesn’t have to be manually copied over. And if said researcher has their manuscript accepted, they can also expect that their ORCID record will automatically be updated with the publication information and that their institution and/or their funder can be automatically notified of the impending publication so that relevant repositories and [CRIS](https://en.wikipedia.org/wiki/Current_research_information_system) systems can be populated automatically.

Additionally, there is a growing list of services that have been built on top of these standard identifiers. Profile systems (e.g. VIVO, Impact Story, Kudos) can automatically retrieve the latest information from a researcher’s ORCID record. Bibliographic management tools (EasyBib, Zotero, Papers) allow researchers to cite content with the latest metadata. And similarity checking services can harvest and index the latest scholarly literature for inclusion in the tools they have developed for detecting plagiarism and fraud. Funder identifiers are already playing an important role in this metadata workflow. As of November 2017, there are 1.7 million Crossref publication DOIs that are explicitly linked to an Open Funder Registry ID. These linkages serve as a foundation for initiatives like SHARE, CHORUS, and the Jisc Publications Router.  But there are another 1+ million records that have funding information without an associated ID and, of course, 90+ million records that have no funding information at all.

> So If we have global funder identifiers and they are already working, why do we need global grant identifiers as well? Don’t we just need to increase uptake of funder identifiers? How will grant identifiers help?

First, global grant identifiers could greatly reduce the UX complexity of gathering funder information. This, in turn, would boost the collection of funding information from researchers and ensure that the information that they provide to publishers, institutions and other funders is accurate and complete.

Second, the introduction of global grant identifiers would further increase the utility of links between research outputs and funding information. A grant identifier provides more granular information about the funding. Instead of just linking to information about the funder, a grant identifier would allow linking research outputs to particular research programs along with the information relating to those programs, such as grant durations, award amounts, etc. It would also allow analysis of relationships between multiple co-funding bodies.

### To DOI or not to DOI?

Clearly, we think DOIs are pretty good things. But we also aren’t zealots. Sometimes DOIs are appropriate and sometimes they are not. For example, we were instrumental in [defining the structure of the ORCID identifier](https://docs.google.com/document/d/1awd6PPguRAdZsC6CKpFSSSu1dulliT8E3kHwIJ3tD5o/edit?usp=sharing) and, in that case, we decided that DOIs were not appropriate.

But in the case of a global grant identifier system, we think there are a number of reasons adopting DOIs would be useful:

1. It is easy to “overlay” the global DOI system onto existing local identifier systems. An organisation does not need to abandon their internal identifier scheme in order to use DOIs. They can instead incorporate their local scheme into the DOI structure via the simple mechanism of prepending their existing identifiers with an assigned DOI prefix and registering relevant metadata with a DOI registration agency like Crossref or DataCite.
2. DOI links are “persist-able”. That is they can resolve to different online locations even if domain names change and/or the DNS system itself is replaced. This characteristic is important for a grant identifier because funding agencies - particularly government funding agencies - tend to undergo frequent reorganisations (e.g. splitting, merging, restructuring) and renaming. An indirectly resolvable identifier like a DOI (or ARK, Handle, etc.) is critical to ensure the long-term integrity of identifiers in these situations.
3. There are 15K+ funders currently listed in the Open funder Registry. Each has their own grant identifier scheme and different levels of technical support for them (APIs, etc.). This makes it very difficult for 3rd parties to build tools that work “generically” with grant identifiers.  But once a local identifier scheme had been “globalised” by making it a DOI, third parties can build tools without having to worry about the differences between individual funder systems.
4. Crossref and DataCite DOIs are deeply embedded in the tools and workflows of scholarly communications. Manuscript tracking systems, bibliographic management systems, metrics systems, CRIS systems, profile systems, etc. often have built-in mechanisms for consuming and making use of DOIs and their associated metadata.
5. Crossref and DataCite DOIs are cross-disciplinary. They are used in the humanities, social sciences, sciences and in a host of communities that frequently interact with the scholarly literature for example- NGOs, IGOs, patent systems, and standards bodies.
6. Crossref and DataCite provide a variety of APIs (e.g. REST, OAI-PMH) and services (e.g. search, Crossmark, Similarity Check, Scholix) built around DOIs.
7. DOI’s have a useful characteristic, which is that the “prefix” of a DOI can be used to determine who originally created the record with which the DOI is associated. In the case of grant identifiers, this means that the prefix of a DOI-based grant identifier could be used to automatically determine the correct funder responsible for the initial grant. This means that the UIs for entering funder/grant information could be both simplified and made more robust—which would likely increase the number of parties that collect and propagate id-based funder information.

But the use of DOIs as the basis for grant identifiers also introduces some potential barriers to adopting a standard funding identifier. For example:

* Funders would need to be able to join a suitable DOI registration agency (e.g. Crossref, DataCite). Some funders (e.g. government agencies) may be restricted in their ability to “join” external organisations.
* Funders would need to be able to create new DOIs and register associated metadata with their chosen registration agency in a timely manner. Some funders may be unable to generate metadata or may not have the technical capacity to automatically register metadata.
* Funders would need to be able to provide an openly available (e.g. not behind access control) online resource to which the DOI would resolve. For example, a landing page describing the grant or a digital copy of the grant itself. Again, some funders may face technical barriers to providing an online resource to resolve to. In other cases there may be privacy or security reasons for not providing an open resource to which a DOI can resolve.

Still, the advisory group consensus has been that these barriers are generally surmountable. Most of the questions they had revolved around understanding what a DOI-based workflow would look like from the funder’s perspective, and so we outlined the steps a funder would need to take in order to adopt DOI-based global identifiers.

### The DOI-based grant identifiers workflow

A funder registering metadata and creating DOIs for grants would need to support the following workflow:

1. When a grant is submitted, the funder would assign their own internal identifier for tracking, etc. For example `00-00-05-67-89`.
2. If the grant is accepted, the funder would:

* generate a global public identifier for the grant based on the DOI. For example, assuming their prefix was `10.4440`, then the global public identifier might become `https://doi.org/10.4440/00-00-05-67-89`.
* create a “landing page” on their website (or wherever they make their grants available online) to which the global public identifier will resolve. The landing page would display a TBD set of metadata describing the grant, as well as a link to the grant itself.
* register the generated DOI and a TBD set of metadata with their registration agency (RA) (e.g. Crossref or DataCite). This metadata would include the URL of the landing page defined above.

3. Once metadata and DOIs are registered with an RA, the funder would have a series of ongoing obligations:

* Update locations: If the location of the landing page changes (for example, because of a site restructuring, merger of split of the funding organisation, etc.), the funder would need to update their metadata records to point the DOI to the new location.
* Update metadata: If metadata becomes out-of-date (e.g. the status of a grant changes, additional grant-related metadata is added, etc.), the funder would update the relevant records.
* Promote the use of the the DOI as the preferred global, public identifier for the grant. That is - the one that people should use when referring to or citing the grant (the funder can continue to use the original local identifier for their internal systems, etc.).

Again, the advisory group thought that this workflow seemed tractable and agreed that the best way to ensure that would be to proceed to creating a working pilot of a global grant identifier system based on the DOI.

### Next steps

Crossref is starting a grant identifier pilot. We will create two sub-groups of the funder advisory group.

#### Group for “Governance, membership, and fees”

This group will look at governance and financial issues raised by the introduction of grant identifiers. For example, it will look at whether Crossref’s membership model works as is or might need to be adjusted in order to accommodate a new constituency. We know, for example, that some funders find it hard to become “members” of organisations. We might need to create other participation categories in order to accommodate these restrictions. Similarly the group will look design a pricing model of DOIs for grants in order to make sure that they cover the costs of modifying and sustaining the system for them, as well as to ensure that the pricing incentivises funders to participate. This sub-group will work closely with Crossref’s membership and fees committee.

#### Group for “Technical and metadata”

This group will look at any technical changes that need to be made to registration process in order to accommodate the new participants. If there are, they are likely to center around specific metadata requirements for grants. As such, the group will likely spend most of its time agreeing to a practical metadata schema for capturing relevant information about the myriad of ways in which organisations *support* research. This group will also liaise with other relevant technical working groups, such as those who are looking at organisational identifiers and conference identifiers.

The two sub-groups will first meet in January and, after a few meetings, will report back the advisory group with recommendations. Using these recommendations, we will develop an implementation plan which will include testing the infrastructure, testing metadata deposits, fee modelling, etc, with a small group of participants.

If you are a funder, and you would like to have somebody from your origanization participate in one of these working groups, please [contact Ginny Hendricks](mailto:ginny@crossref.org). Note that joining the above groups does not commit you to anything other than engaging in the discussion. We want to make sure we create a system that works for a range of funders, not just those who can start testing something right away.
