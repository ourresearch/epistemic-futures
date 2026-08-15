---
title: "The case for two semantic webs"
person: david-weinberger
section: by
type: op-ed
year: 2006
date: 2006-05-26
venue: "KMWorld ('Perspective on Knowledge' / 'The Weinberger Column')"
authors: "David Weinberger"
source_url: https://weinberger.org/content/kmworld/dw-col-pages/2006-05-26-kmworld.html
retrieved: 2026-08-13
content: full-text
notes: "KMWorld column, republished with permission in the author-hosted KMWorld archive at weinberger.org. Site header/footer navigation stripped."
---

# The case for two semantic webs

## Full text

26 May 2006

The Web is semantic. It has to be because we've written it. It is an endless ocean of words and deliberately created images. Every link in every blog post also has meaning, and almost always that meaning is expressed explicitly or is blindingly clear from context: not simply "Click here and you'll get a surprise" but "Click here to read Glenn's latest bad idea" or "Click here to hear why Shelley thinks the tech conference she was at stacked the deck against women." One way or another, Web pages almost always tell us what the destination of the link is about, and often what we ought to think about it.

So, when Tim Berners-Lee issued the call for the Semantic Web, it wasn't because there weren't enough meaningful phrases online. The problem he saw was that HTML, the syntax of the Web, didn't include enough meaning: The meaning was "trapped" in language, not in code. At the code level, all links are the same----even though that code is almost always embedded in a sentence that contextualizes the link. So, Berners-Lee suggested a syntax that would capture the meaning expressed on pages in a way that computers could process.

Called RDF (for Resource Description Framework), this new syntax is the one thing Semantic Web supporters agree on. RDF expresses the relationship between two terms: Apples are a type of fruit; Homer is the father of Bart. RDF lets a site owner create whatever relationships she wants. All those relationships when put together constitute an ontology. For example, a genealogy site that wants to Semantic Webbify would have an ontology that expresses--in RDF triples--that sons are children, that children have parents, that couples have children, that sisters are female siblings, and so on until every relationship down to illegitimate third cousins twice removed is codified. (Ontologies are expressed in the Semantic Web standard called OWL.)

Beyond this, Semantic Webbers are split. Some want to build comprehensive ontologies for large domains. For example, there are a couple of competing ontologies of the domain of law, each of which has thousands of terms. It's reminiscent of 19th and 20th century attempts to build comprehensive taxonomies. And this approach suffers from the same intractable problems: First, the task is overwhelmingly large. Second, one ontology can't capture all the different ways we think about these domains. Third, they are trying to make explicit what is in fact a largely implicit realm, and doing so inevitably distorts the result.

Other Semantic Webbers take a different approach. Rather than building huge ontologies top down, they hope that if everyone contributes just a little, over time huge ontologies will accrete. Their strategy is to define as few relationships as possible, and to reuse ones already created by others, possibly in other domains. So, if you're Semantic Webbifying a medical research site, you should not define the relationship "papers are authored by writers." Instead, you should point (via a URI) to an existing ontology--such as the Dublin Core--that already has defined that relationship. This not only eases your burden, it also helps to stitch the Semantic Web together: Applications will know that the relationship you're defining is the same one that's used at all the different sites that use the Dublin Core.

True, this means there will be some sloppiness in how the Web overall is Semantified. People may use different ontologies to define the same relationship, complicating the task of applications that want to pull it all together. Timothy Falconer, a Semantic Webber of the Second Kind, refers to the build-it-in-small-pieces approach as "smushy" because it doesn't aim for the comprehensiveness and precision a top-down, created-by-a-single-committee can bring. But, it is more likely to succeed because it is more agile.

There's also disagreement among Semantic Webbers about how transformative the Semantic Web will be. Some talk as if it will save the Web, turning it into a well-functioning machine. Others think it will help where it helps. And some are bipolar on this issue. My experience with SGML leads me to think that the Semantic Web will help where it helps, but that the vast bulk of the semantic stitching of the Web will be done the way we're doing it already and the further ways we will invent--everything from hyperlinks to XML to playlists to buddy lists to reputation systems. In fact, there's basically nothing we do on the Web that doesn't turn it into an evermore semantic Web.
