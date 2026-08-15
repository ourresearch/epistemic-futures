---
title: "Meaning-mining Wikipedia"
person: david-weinberger
section: by
type: blog-post
year: 2009
date: 2009-06-09
venue: "Joho the Blog (hyperorg.com)"
authors: "David Weinberger"
source_url: https://hyperorg.com/2009/06/09/meaning-mining-wikipedia/
retrieved: 2026-08-13
content: full-text
notes: "Post from Joho the Blog (hyperorg.com), Weinberger's personal blog. Retrieved via the site's WordPress REST API; HTML converted to plain text."
---

# Meaning-mining Wikipedia

## Full text

DBpedia extracts information from Wikipedia, building a database that you can query. This isn’t easy because much of the information in Wikipedia is unstructured. On the other hand, there’s an awful lot that’s structured enough so that an algorithm can reliably deduce the semantic content from the language and the layout. For example, the boxed info on bio pages is pretty standardized, so your algorithm can usually assume that the text that follows “Born: ” is a date and not a place name. As the DBpedia site says:

The DBpedia knowledge base currently describes more than 2.6 million things, including at least 213,000 persons, 328,000 places, 57,000 music albums, 36,000 films, 20,000 companies. The knowledge base consists of 274 million pieces of information (RDF triples). It features labels and short abstracts for these things in 30 different languages; 609,000 links to images and 3,150,000 links to external web pages; 4,878,100 external links into other RDF datasets, 415,000 Wikipedia categories, and 75,000 YAGO categories.

Over time, the site will get better and better at extracting info from Wikipedia. And as it does so, it’s building a generalized corpus of query-able knowledge.

As of now, the means of querying the knowledge requires some familiarity with building database queries. But, the world has accumulated lots of facility with putting front-ends onto databases. DBpedia is working on something differentL accumulating an encyclopedic database, open to all and expressed in the open language of the Semantic Web.

(Via Mirek Sopek.) [Tags: wikipedia semantic_web everything_is_miscellaneous ]
