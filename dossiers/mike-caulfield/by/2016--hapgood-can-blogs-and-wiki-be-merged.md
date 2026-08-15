---
title: "Can Blogs and Wiki Be Merged?"
person: mike-caulfield
section: by
type: blog-post
year: 2016
date: 2016-02-22
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2016/02/22/can-blogs-and-wiki-be-merged/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Can Blogs and Wiki Be Merged?

## Full text

I’ve been thinking lately about the architecture underlying blogs and wiki, how different these architectural choices are (RSS, revision histories, title-as-slug, etc), and whether it’s worthwhile to imagine a world where data flows seamlessly across them. It might not be. They are very different things, with different needs.

Wiki and blogs have two different cultures, two different idioms, two different sets of values.

Blogs are, in many ways, the child of BBS culture and mailing lists. They are a unique innovation on that model, allowing each person to control their part of the conversation on their own machine and software while still being tied to a larger conversation through linking, backlinks, tags, and RSS feeds.

Blogs value a separation of voices, the development of personalities, new posts over revision of old posts. They are read serially, and the larger meaning is created out of a narrative that expands and elaborates themes over time, becoming much more than the sum of its parts to the daily reader.

Through reading a good blogger on a regular basis, one is able to watch someone of talent think through issues, to the point that one is able to reconstruct the mental model of a blogger as a mini Turing machine in one’s head. I have been reading people like Jim Groom, Josh Marshall, Digby, Atrios, and Stephen Downes for years, watching how they process new information, events, and results. And when thinking through an issue, I can, at this point, conjure up a rough facsimile of how they would go about analyzing a thing.

Wiki is perhaps the only web idiom that is _not_ a child of BBS culture. It derives historically from _pre_ -web models of hypertext, with an emphasis on the _pre_. The immediate ancestor of wiki was a Hypercard stack maintained by Ward Cunningham that attempted to capture community knowledge among programmers. Its philosophical godfather was the dead-tree hypertext A Pattern Language written by Christopher Alexander in the 1970s.

Alexander’s  _A Pattern Language_ used bolded, numbered in-text links to connect “patterns” that were related ideas. The sections were formed around these patterns and written to be approached from many different directions.

What wiki brought to these models, which were personal to start with, was collaboration. Wiki values are often polar opposites of blogging values. Personal voice is meant to be minimized. Voices are meant to be merged. Rather than serial presentation, wiki values treating pages as nodes that stand outside of any particular narrative, and attempt to be timeless rather than timebound reactions.

Wiki iterates not through the creation of new posts, but through the refactoring of old posts. It shows not a mind in motion, but the clearest and fairest description of what that mind has (or more usually, what those  _minds have)_ arrived at. It values reuse over reply, and links are not pointers to related conversations but to related ideas.

These are, in many ways, as different as two technologies can be.

Yet, the recent work of Ward Cunningham to create [federated wiki communities](<https://www.youtube.com/watch?v=FV0bXEnqxnU>) moves wiki a bit more towards blogging. Voices are still minimized in his new conception, but control is not shared or even negotiated. I write something, you make a copy, and from that point on I control my copy and you control yours. In Federated Wiki (the current coding project) what you fork can be anything: data, code, calculations, and yes, text too.

As I’ve been working on Wikity (my own federated wiki inspired project) I’ve been struggling with this question: to what extent is there value in breaking down the wall between blogging and wiki, and to what extent are these two technologies best left to do what they do best?

The questions aren’t purely theoretical. Ward has designed a data model perfectly suited for wiki use, which represents the nature and necessities of multiple, iterative authorship. Should Wikity adopt that as the model it consumes from other sites?

Or should Wikity tap into the existing community of bloggers and consume a souped up version of RSS, even though blog posts make lousy wiki pages?

Should Wikity follow the wiki tradition of supplying editable  _source_ to collaborators? Or the web syndication model of supplying  _encoded content_. (Here, actually, I come down rather firmly on the source side of the equation — encoded content is a model suited for readers, not co-authors).

These are just two of many things that come up, and I don’t really have a great answer to these questions. In most cases I’d say it makes sense for these to remain two conceptually distinct projects, except for the big looming issue which is with the open web shrinking it might helpful for these communities to join common cause and solve some of the problems that have plagued both blogging and wiki in their attempt to compete with proprietary platforms.

Again, no firm answers here. Just wanted to share the interesting view I’ve found at the intersection of these two forms.
