---
title: "Database War Stories #2:  bloglines and memeorandum"
person: tim-oreilly
section: by
type: blog-post
year: 2006
date: 2006-04-27
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/archives/2006/04/database_war_stories_2_bloglin.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# Database War Stories #2:  bloglines and memeorandum

## Full text

In [Monday's installment](http://radar.oreilly.com/archives/2006/04/web_20_and_databases_part_1_se.html), Cory Ondrejka of [Second Life](http://www.secondlife.com) said "flat files don't cut it", but Mark Fletcher of [bloglines](http://www.bloglines.com) and Gabe Rivera of [memeorandum.com](http://tech.memeorandum.com) apparently don't agree.

Gabe wrote: "I didn't bother with databases because I didn't need the added complexity... I maintain the full text and metadata for thousands of articles and blog posts in core. Tech.memeorandum occupies about 600M of core. Not huge."

Mark wrote: "The 1.4 billion blog posts we've archived since we went on-line are stored in a data storage system that we wrote ourselves. This system is based on flat files that are replicated across multiple machines, somewhat like the system outlined in [the Google File System paper](http://labs.google.com/papers/gfs-sosp2003.pdf)."  

Here's what Mark had to say in full:

> The subject of databases is either a favorite topic of mine or something I want nothing to do with. Obviously my mood is dependent upon the state of Bloglines' various databases that particular day. In either case, I've done a lot of thinking about them... 
> 
> Bloglines has several data stores, only a couple of which are managed by "traditional" database tools (which in our case is Sleepycat). User information, including email address, password, and subscription data, is stored in one database. Feed information, including the name of the feed, description of the feed, and the various URLs associated with feed, are stored in another database. The vast majority of data within Bloglines however, the 1.4 billion blog posts we've archived since we went on-line, are stored in a data storage system that we wrote ourselves. This system is based on flat files that are replicated across multiple machines, somewhat like the system outlined in the Google File System paper, but much more specific to just our application. To round things out, we make extensive use of memcached to try to keep as much data in memory as possible to keep performance as snappy as possible.
> 
> As evidenced by our design, traditional database systems were not appropriate (or at least the best fit) for large parts of our system. There's no trace of SQL anywhere (by definition we never do an ad hoc query, so why take the performance hit of a SQL front-end?), we resort to using external (to the databases at least) caches, and a majority of our data is stored in flat files. Sure, we could have just gone with Oracle running on a big SAN, but that would have been very expensive overkill, both on the hardware and on the software licenses (and features, for that matter). And relational databases oftentimes are not the most efficient mechanism to store data, so we'd still most likely have to resort to using memcacheds.

Here's Gabe:

> I didn't bother with databases because I didn't need the added complexity... I maintain the full text and metadata for thousands of articles and blog posts in core. Tech.memeorandum occupies about 600M of core. Not huge. 
> 
> About the flat files: Only if I'm doing a cold start (usually because of a new version) do I need to load the recent history. So I just maintain a flat file with the new data for each hour the system runs and eval the most recent few weeks of hourly files.
> 
> eval and Data::Dumper (a sort of "reverse eval" for data) are a handy way to read / write data certain kinds of data when you're not using a database. I do wish eval ran a little faster though. I wonder how much optimization effort has been put into that.

_**More entries in the database war stories series:[Second Life](http://radar.oreilly.com/archives/2006/04/web_20_and_databases_part_1_se.html), [Flickr](http://radar.oreilly.com/archives/2006/04/database_war_stories_3_flickr.html), [NASA World Wind](http://radar.oreilly.com/archives/2006/04/database_war_stories_4_nasa_wo.html), [Craigslist](http://radar.oreilly.com/archives/2006/04/database_war_stories_5_craigsl.html), [O'Reilly Research](http://radar.oreilly.com/archives/2006/05/database_war_stories_6_oreilly.html), [Google File System and BigTable](http://radar.oreilly.com/archives/2006/05/database_war_stories_7_google.html), [Findory and Amazon](http://radar.oreilly.com/archives/2006/05/database_war_stories_8_findory_1.html), [Brian Aker of MySQL Responds](http://radar.oreilly.com/archives/2006/05/brian_aker_of_mysql_responds.html)**_.
