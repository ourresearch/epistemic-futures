---
title: "Database War Stories #9 (finis):  Brian Aker of MySQL Responds"
person: tim-oreilly
section: by
type: blog-post
year: 2006
date: 2006-05-05
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/archives/2006/05/brian_aker_of_mysql_responds.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# Database War Stories #9 (finis):  Brian Aker of MySQL Responds

## Full text

Brian Aker of MySQL sent me a few email comments about this whole "war stories" thread, which I reproduce here. Highlight -- he says: "Reading through the comments you got on your blog entry, these users are hitting on the same design patterns. There are very common design patterns for how to scale a database, and few sites really turn out to be all that original. Everyone arrives at certain truths, flat files with multiple dimensions don't scale, you will need to partition your data in some manner, and in the end caching is a requirement." 

I agree about the common design patterns, but I _didn't_ hear that flat files don't scale. What I heard is that some very big sites are saying that traditional databases don't scale, and that the evolution isn't from flat files to SQL databases, but from flat files to sophisticated custom file systems. Brian acknowledges that SQL vendors haven't solved the problem, but doesn't seem to think that anyone else has either. 

Here are Brian's comments in full:

> While at the conference I spoke to an outfit who had stuck around a terabyte of data into just one table. The table had tiny little rows, and the primary key was not native to the database, aka they derived it from an external application and it was not really database friendly. They were looking for a solution to the table problem when in reality they needed a solution to their usage problem. 
> 
> Predictably the solution was to partition the database with one master database for lookups to find out where the actual database holding the real data was. AKA I suggested that they partition their data, and as is often the case their data partitioned quite easily. This is the sort of use case I see over and over again. There is a talk I've been giving for years on how people lay out their database environment, its been interesting to watch what the converging use cases are, and every time I give the talk I find new insights on how people are creating clusters/creating scale out.
> 
> Reading through the comments you got on your blog entry, these users are hitting on the same design patterns. There are very common design patterns for how to scale a database, and few sites really turn out to be all that original. Everyone arrives at certain truths, flat files with multiple dimensions don't scale, you will need to partition your data in some manner, and in the end caching is a requirement.
> 
> Its also obvious that no one has fulltext done in a manner which is really right yet. The Lucene approach is "shove it all in, hope you can find it" method, which is no better then google with different weighting. Contextual relational environments are needed, but I am not seeing any SQL yet that make me think the database vendors have the solved the problem. The technology is there, but no one has found the common language that is required to make this work just yet.

_**More entries in the database war stories series:[Second Life](http://radar.oreilly.com/archives/2006/04/web_20_and_databases_part_1_se.html), [Bloglines and Memeorandum](http://radar.oreilly.com/archives/2006/04/database_war_stories_2_bloglin.html), [Flickr](http://radar.oreilly.com/archives/2006/04/database_war_stories_3_flickr.html), [NASA World Wind](http://radar.oreilly.com/archives/2006/04/database_war_stories_4_nasa_wo.html), [Craigslist](http://radar.oreilly.com/archives/2006/04/database_war_stories_5_craigsl.html), [O'Reilly Research](http://radar.oreilly.com/archives/2006/05/database_war_stories_6_oreilly.html), [Google File System and BigTable](http://radar.oreilly.com/archives/2006/05/database_war_stories_7_google.html), [Findory and Amazon](http://radar.oreilly.com/archives/2006/05/database_war_stories_8_findory_1.html)**_.
