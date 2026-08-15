---
title: "Treemap on Rails"
person: tim-oreilly
section: by
type: blog-post
year: 2006
date: 2006-07-28
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/archives/2006/07/treemap_on_rails.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# Treemap on Rails

## Full text

[Andy Bruno](http://qnot.org/), who developed the treemap code that we use for our [Bookscan data visualizations](http://radar.oreilly.com/archives/2005/04/book_sales_as_a.html), has created a new Rails implementation called [acts_as_treemap](http://code.qnot.org/svn/projects/acts_as_treemap/), according to a report by Rob Orsini, author of [The Rails Cookbook](http://www.oreilly.com/catalog/railsckbk/), who [blogs on Rails-related topics at tupleshop.com](http://blog.tupleshop.com/2006/7/27/treemap-on-rails).

If you're a fan of data visualization, as I am, you'll be excited both about getting your hands on Andy's Ruby treemap code and on Rob's clear description of how it works. And heck, Andy even applied it to an example data set that is fascinating in and of itself: SourceForge projects.

Here's the resulting treemap view:

[](http://www.oreillynet.com/ruby/blog/images/ror/sf-treemap.png)

This visualization uses the SourceForge project name for labeling each region of the treemap; the size of each region is be based on the number of downloads for the current month, and the color of each region conveys information about the rate of change in the number of downloads for each project. While the color-scheme is a bit different than we use for the book visualizations, green means up, red means down, and the paler colors are in-between. There's a bit of overlaid information about categories, but the treemap doesn't really organize the downloads by category like we do with book sales. But it's still pretty interesting to pick out the biggest downloads.

And what's more, if you like this kind of visualization, Andy and Rob have now made it easy for you to apply it to your own data sets.
