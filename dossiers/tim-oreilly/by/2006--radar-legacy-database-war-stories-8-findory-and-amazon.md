---
title: "Database War Stories #8:  Findory and Amazon"
person: tim-oreilly
section: by
type: blog-post
year: 2006
date: 2006-05-04
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/archives/2006/05/database_war_stories_8_findory_1.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# Database War Stories #8:  Findory and Amazon

## Full text

Once Greg Linden had pinged me about BigTable (leading to yesterday's entry), it occurred to me to ask Greg for his own war stories, both at [Findory](http://www.findory.com) and Amazon. We hear a recurrent theme: the use of flat files and custom file systems. Despite the [furor that ensued in the comments](http://radar.oreilly.com/archives/2006/04/database_war_stories_2_bloglin.html) when Mark Fletcher and Gabe Rivera noted that they didn't use traditional SQL databases, Web 2.0 applications really do seem to have different demands, especially once they get to scale. But history shows us that custom, home-grown solutions created by alpha geeks point the way to new entrepreneurial opportunities... 

Greg wrote: 

> There are a couple stories I could tell, one about the early systems at Amazon, one about the database setup at Findory. 
> 
> On Findory, our traffic and crawl is much smaller than sites like Bloglines, but, even at our size, the system needs to be carefully architected to be able to rapidly serve up fully personalized pages for each user that change immediately after each new article is read. 
> 
> Our read-only databases are flat files -- Berkeley DB to be specific -- and are replicated out using our own replication management tools to our webservers. This strategy gives us extremely fast access from the local filesystem. We make thousands of random accesses to this read-only data on each page serve; Berkeley DB offers the performance necessary to be able to still serve our personalized pages rapidly under this load. 
> 
> Our much smaller read-write data set, which includes information like each user's reading history, is stored in MySQL. MySQL MyISAM works very well for this type of non-critical data since speed is the primary concern and more sophisticated transactional support is not important. While it has not been necessary yet, our intention is to scale our MySQL database with horizontal partitioning, though we may also experiment with MySQL Cluster as well. 
> 
> For both read-only and read-write data, we have been careful to keep the data formats compact to ensure that the total active data set can easily fit in main memory. We attempt to avoid as much disk access as we can. 
> 
> After all of this, Findory is able to serve fully personalized pages, different for each reader, that change immediately when each person reads a new article, all in well under 100ms. People don't like to wait. We believe getting what people need quickly and reliably is an important part of the user experience. 
> 
> [Regarding Amazon], as it turns out, I have already written up a fairly detailed description of [Amazon's early (1997) systems](http://glinden.blogspot.com/2006/02/early-amazon-splitting-website.html) on my weblog. An excerpt from that post: ... [We] were going to take Amazon from one webserver to multiple webservers. 
> 
> There would be two staging servers, development and master, and then a fleet of online webservers. The staging servers were largely designed for backward compatibility. Developers would share data with development when creating new website features. Customer service, QA, and tools would share data with master. This had the added advantage of making master a last wall of defense where new code and data would be tested before it hit online. 
> 
> Read-only data would be pushed out through this pipeline. Logs would be pulled off the online servers. For backward compatibility with log processing tools, logs would be merged so they looked like they came from one webserver and then put on a fileserver. 
> 
> Stepping out for a second, this is a point where we really would have liked to have a robust, clustered, replicated, distributed file system. That would have been perfect for read-only data used by the webservers. 
> 
> NFS isn't even close to this. It isn't clustered or replicated. It freezes all clients when the NFS server goes down. Ugly. Options that are closer to what we wanted, like CODA, were (and still are) in the research stage. 
> 
> Without a reliable distributed file system, we were down to manually giving each webserver a local copy of the read-only data.

_**More entries in the database war stories series:[Second Life](http://radar.oreilly.com/archives/2006/04/web_20_and_databases_part_1_se.html), [Bloglines and Memeorandum](http://radar.oreilly.com/archives/2006/04/database_war_stories_2_bloglin.html), [Flickr](http://radar.oreilly.com/archives/2006/04/database_war_stories_3_flickr.html), [NASA World Wind](http://radar.oreilly.com/archives/2006/04/database_war_stories_4_nasa_wo.html), [Craigslist](http://radar.oreilly.com/archives/2006/04/database_war_stories_5_craigsl.html), [O'Reilly Research](http://radar.oreilly.com/archives/2006/05/database_war_stories_6_oreilly.html), [Google File System and BigTable](http://radar.oreilly.com/archives/2006/05/database_war_stories_7_google.html), [Brian Aker of MySQL Responds](http://radar.oreilly.com/archives/2006/05/brian_aker_of_mysql_responds.html)**_.
