---
title: "Does a Crossref DOI identify a “work?”"
person: "geoffrey-bilder"
section: "by"
type: "blog-post"
year: 2010
date: 2010-02-11
venue: "Crossref blog"
authors: "Geoffrey Bilder"
source_url: "https://www.crossref.org/blog/does-a-crossref-doi-identify-a-work/"
retrieved: "2026-08-13"
content: "full-text"
notes: "Crossref blog post. DOI 10.64000/be8jg-xk804."
---

# Does a Crossref DOI identify a “work?”

## Full text

**5 minute read.**

## Does a Crossref DOI identify a “work?”

Tony’s recent thread on [making DOIs play nicely in a linked data world](/blog/doi-what-do-we-got/) has raised an issue I’ve meant to discuss here for some time- a lot of the thread is predicated on the idea that Crossref DOIs are applied at the abstract “work” level. Indeed, that it what it currently says in our guidelines. Unfortunately, this is a case where theory, practice and documentation all diverge.

When the Crossref linking system was developed it was focused primarily on facilitating persistent linking amongst journals and conference proceedings. The system was quickly adapted to handle books and more recently to handle working papers, technical reports, standards and “components”- a catchall term used to refer to everything from individual article images to database records.

In practice the content outside of the core journals and conference proceedings has accounted for relatively low volume. However, we expect that over the next few years this will change and that books and databases will increasingly drive the future growth in Crossref’s citation linking services. Interestingly, these record types all share characteristics that make them substantially different from the journals and conference proceedings that we have hitherto focused on.

Both books and databases introduce new challenges to technology and policies of our citation linking service. The challenges revolved around two areas:

* Structure: Both books and databases can have complex structures and the publishers of this content are likely to require granular identification of these content substructures along with a mechanism for documenting the relationship between these substructures (e.g. this section is part of this chapter which is part of this monograph which is part of this series)
* Versioning: Unlike typical journals and conference proceedings, books and database records sometimes change over time.

When confronted with the issues of structure and versioning publishers are often tempted to take shortcuts and decide to simply assign DOIs at the highest level structure and to the “work” instead of a particular “manifestation” or version of that work. Indeed, section 5.5 of Crossref’s [DOI Name Information and Guidelines][2] recommends this. But this approach could have a negative impact on the integrity of the scholarly citation record that Crossref is attempting to maintain.

Fundamentally, Crossref DOIs are aimed at providing a persistent online citation infrastructure for scholarly and professional publishers. Consequently, decisions about where to apply Crossref DOIs should be guided by common expectations about the way in which citations work. Citations are typically used to credit ideas or provide evidence. A reader follows a citation in order to obtain more detail or to verify that an author is accurately representing the item cited. A rule of thumb is that a reader has a reasonable expectation that when they follow a citation, they will be taken to what the author saw when creating the citation. Any divergent behavior could result in the reader concluding that the author was misrepresenting the item cited. A further implication of this is that any changes to content that are likely to effect the crediting or interpretation of the content should result in that changed content getting a new Crossref DOI.

Typically, this means that Crossref DOIs should be probably assigned at the expression level and different expressions should be assigned different Crossref DOIs. This is because assigning a Crossref DOI at the higher “work” level is generally not granular enough to guarantee that a reader following the citation will see what the author saw when creating the citation. For example, one translation of a work might be substantially different from another translation of the same work. Similarly a draft version of a work might be substantially different from the final published version of the work. In each case, resolving a citation to a different expression of the work than the expression that was originally cited might result in the reader interpreting the content differently than the citing author.

In general, different “equivalent manifestations” of the same work can safely be assigned the same Crossref DOI. So, for instance, the HTML formatted version an article and the PDF formatted version of an article can almost always be assigned the same Crossref DOI. Any differences between the two are unlikely to affect the crediting of, or reader’s interpretation of, the work. But sometimes it is even possible that different manifestations of an expression will differ enough to merit different Crossref DOIs. For instance, a semantically enhanced version of an article might require new crediting (e.g. the parties responsible for adding the semantic information) and the resulting semantic enhancement may conceivably alter the reader’s interpretation of the article.

Unfortunately, there is no hard and fast rule about where and when to assign new Crossref DOIs. Instead there is only a guideline, namely:

> “Assign new Crossref DOIs to content in a way that will ensure that a reader following the citation will see something as close to what the original author cited as is possible.”

The implications of this to publishers are important, especially when they are assigning DOIs to protean records types. For instance, it may mean that:

* Book publishers should be expected to keep old editions of books available for link resolution purposes.
* Publishers of content that can change rapidly (e.g. by the second) should provide facilities for creating frozen, archived snapshots of content for citation purposes.
* All publishers of protean content should issue guidelines instructing researchers on when it is appropriate to cite a work, manifestation or version.

Crossref needs to actively consider these issues as publishers start assigning Crossref DOIs to more dynamic types of content. Minimally, we should be able to provide publishers with recommendations on how to make dynamic content citable. We may even want to consider enshrining certain types of behavior in our terms and conditions so as to ensure the future integrity of the scholarly citation record.

In short, we need to update our guidelines.

[2]: [Crossref DOI display guidelines](https://doi.org/10.13003/5jchdy)
