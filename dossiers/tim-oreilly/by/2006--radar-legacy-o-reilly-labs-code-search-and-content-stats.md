---
title: "O'Reilly Labs:  Code Search and Content Stats"
person: tim-oreilly
section: by
type: blog-post
year: 2006
date: 2006-08-25
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/archives/2006/08/oreilly_code_search.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# O'Reilly Labs:  Code Search and Content Stats

## Full text

As part of our [SafariU](http://www.safariu.com) platform (which allows professors or trainers to build custom books using the entire corpus of books from [Safari](http://safari.oreilly.com) as a resource, mixing in their own materials at will), we've build a [MarkLogic](http://www.marklogic.com) xquery database containing the source for all of our books.

So Ryan Grimm and Andy Bruno started asking themselves what else they could do with all that content. A couple of their initial projects are up on our new [O'Reilly Labs](http://labs.oreilly.com) site. The first, [Code Search](http://labs.oreillynet.com/code.xqy), lets you search through the more than 2.6 million lines of example code from almost 700 O'Reilly books. You can limit your search to a particular book, a particular category (e.g. Perl, or Java), or a particular author.

[Documentation on the search syntax ](http://wiki.labs.oreillynet.com/index.php/Code_Search)can be found on the [Labs Wiki](http://wiki.labs.oreillynet.com/).

The [Content Stats](http://labs.oreillynet.com/stats.xqy) is probably less immediately useful except perhaps to content wonks, but is even cooler. Want to know how many total pages there are in all O'Reilly books? (309,647) How many examples? (123,439) Do our Java books or our Perl books have more lines of code per page, on average? (Java) How many lines? (14.76 vs. 10.97 for Perl.) How many index entries are there in an average O'Reilly book? (1,783) The stats are linked to the search box, so changing the search refigures the stats for the books matching the search result. There's also a cool tag cloud of the most commonly appearing technical terms across all O'Reilly books... and clicking on a term takes you to a listing of all the books containing the term. From there, you can click to a content statistics page for each book.

We're noodling ideas on how to build some of this into [Safari](http://safari.oreilly.com), as well as [oreilly.com](http://www.oreilly.com). We'd love your ideas on other applications of these tools.
