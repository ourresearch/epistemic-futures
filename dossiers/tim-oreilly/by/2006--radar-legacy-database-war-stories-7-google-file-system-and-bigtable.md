---
title: "Database War Stories #7:  Google File System and BigTable"
person: tim-oreilly
section: by
type: blog-post
year: 2006
date: 2006-05-03
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/archives/2006/05/database_war_stories_7_google.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# Database War Stories #7:  Google File System and BigTable

## Full text

Greg Linden of [Findory](http://www.findory.com) wrote: "I've been enjoying your series on O'Reilly Radar about database war stories at popular startups. I was thinking that it would be fantastic if you could get Jeff Dean or Adam Bosworth at Google to chat a little bit about their database issues. As you probably know, Jeff Dean was involved designing [BigTable](http://glinden.blogspot.com/2005/09/googles-bigtable.html) and the [Google File System](http://labs.google.com/papers/gfs.html). Adam Bosworth wrote a much discussed [post about the need for better, large scale, distributed databases](http://www.adambosworth.net/archives/000038.html)."

I followed up with mail to Jeff and Adam. Jeff wrote back briefly about BigTable: "Interesting discussion. I don't have much to add. I've been working with a number of other people here at Google on building a large-scale storage system for structured and semi-structured data called BigTable. It's designed to scale to hundreds or thousands of machines, and to make it easy to add more machines the system and automatically start taking advantage of those resources without any reconfiguration. We don't have anything published about it yet, but there's a public talk about BigTable that I gave at University of  
Washington last November available on the web (try some [searches for bigtable](http://www.google.com/search?q=bigtable) or [view the talk](http://www.uwtv.org/programs/displayevent.asp?rid=2787))."

So no new war stories here, but I thought the links were well worth passing along. BigTable sounds a lot like what Ian Wilkes of Second Life [is wishing for](http://radar.oreilly.com/archives/2006/04/web_20_and_databases_part_1_se.html). What do you think the chances are that Google will release this through [Google Code](http://code.google.com/projects.html)?

_**More entries in the database war stories series:[Second Life](http://radar.oreilly.com/archives/2006/04/web_20_and_databases_part_1_se.html), [Bloglines and Memeorandum](http://radar.oreilly.com/archives/2006/04/database_war_stories_2_bloglin.html), [Flickr](http://radar.oreilly.com/archives/2006/04/database_war_stories_3_flickr.html), [NASA World Wind](http://radar.oreilly.com/archives/2006/04/database_war_stories_4_nasa_wo.html), [Craigslist](http://radar.oreilly.com/archives/2006/04/database_war_stories_5_craigsl.html), [O'Reilly Research](http://radar.oreilly.com/archives/2006/05/database_war_stories_6_oreilly.html), [Findory and Amazon](http://radar.oreilly.com/archives/2006/05/database_war_stories_8_findory_1.html), [Brian Aker of MySQL Responds](http://radar.oreilly.com/archives/2006/05/brian_aker_of_mysql_responds.html)**_.
