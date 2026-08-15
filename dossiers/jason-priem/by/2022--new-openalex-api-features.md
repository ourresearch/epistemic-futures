---
title: "New OpenAlex API features!"
person: jason-priem
section: by
type: blog-post
year: 2022
date: 2022-04-28
venue: "OurResearch blog"
authors: "Jason Priem"
source_url: https://blog.openalex.org/new-openalex-api-features/
retrieved: 2026-08-13
content: full-text
notes: "Byline from WordPress author field (user 'jason') on the merged Impactstory/OurResearch/OpenAlex blog. Originally published on blog.ourresearch.org."
---

# New OpenAlex API features!

## Full text

We’ve got a ton of great API improvements to report! If you’re an API user, there’s a good chance there’s something in here you’re gonna love.

**Search**

You can now search both titles and abstracts. We’ve also implemented [stemming](https://en.wikipedia.org/wiki/Stemming), so [a search for “frogs”](https://api.openalex.org/works?search=frogs) now automatically gets your results mentioning “frog,” too. Thanks to these changes, searches for works now deliver around 10x more results. This can all be accessed using the new [search query parameter](https://docs.openalex.org/api/get-lists-of-entities/search-entity-lists#the-search-parameter).

**New entity filters**

We’ve added support for tons of new filters, which are documented here. You can now:

- get all of a work’s *outgoing* citations (ie, its references section) with a single query. 
- search within each work’s [raw affiliation data](https://docs.openalex.org/about-the-data/work#raw_affiliation_string) to find an arbitrary string (eg a specific department within an organization)
- filter on whether or not an entity has a [canonical external ID](https://docs.openalex.org/about-the-data#canonical-external-ids) (works: has_doi, authors: has_orcid, etc)
- 

**Request multiple records by ID at once**

This has been our most-requested feature and we’re super excited to roll it out! By using the new [OR operator](https://docs.openalex.org/api/get-lists-of-entities/filter-entity-lists#addition-or), you can request up to 50 entities in a single API call. You can use any ID we support–DOI, ISSN, OpenAlex ID, etc.

**Deep paging**

Using cursor-based paging, you can now retrieve an infinite number of results (it used to be just the top 10,000). But remember: if you want to download the entire dataset, please use the snapshot, not the API! The snapshot is the exact same data in the exact same format, but much much faster and cheaper for you and us.

**More groups in group_by queries**

We now return the top 200 groups (it used to be just the top 50).

**New Autocomplete endpoint**

Our new [autocomplete endpoint](https://docs.openalex.org/api/autocomplete-endpoint) dead easy to use our data to power an autocomplete/typeahead widget in your own projects. It works for any of our five entity types (works, authors, venues, institutions, or concepts). If you’ve got users inputting the names of journals, institutions, or other entities, now you can easily let them *choose* an entity instead of entering free text–and then you can store the ID (ISSN, ROR, whatever) instead of passing strings around everywhere. 

**Better docs**

In addition to documenting the new features above, we’ve also added lots of new documentation for existing features, addressing our most frequent questions and requests:

- a new getting-started [tutorial](https://docs.openalex.org/api/api-tutorial) walks you through using the API to find the percent of journal articles from a given institution that are Open Access.
- for each of our [five entity types](https://docs.openalex.org/about-the-data), an overview describing what that entity is and how we get it. 
- more documentation of [the OpenAlex ID](https://docs.openalex.org/about-the-data#the-openalex-id) and of our [Canonical External IDs](https://docs.openalex.org/about-the-data#canonical-external-ids) (DOIs, RORs, etc). 
- a section about using [logical expressions](https://docs.openalex.org/api/get-lists-of-entities/filter-entity-lists#logical-expressions) (inequalities and booleans) with filters.
- lots more explanation and examples on the [group_by page](https://docs.openalex.org/api/get-groups-of-entities).
- a (short) list of community-created [client libraries](https://docs.openalex.org/api#client-libraries)

Thanks to everyone who’s been in touch to ask for new features, report bugs, and tell us where we can improve (also where we’re doing well, we’re ok with that too).\
We’ll continue improving the API and the docs. We’re also putting tons of work into improving the underlying dataset’s accuracy and coverage, and we’re happy to report that we’ve improved a lot on what we inherited from MAG, with more improvements to come. We’ve delayed the launch of the full web UI, but expect that in the summer…we are *so* excited about all the possibilities that’s going to open up.
