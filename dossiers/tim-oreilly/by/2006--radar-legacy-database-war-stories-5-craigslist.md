---
title: "Database War Stories #5:  craigslist"
person: tim-oreilly
section: by
type: blog-post
year: 2006
date: 2006-04-28
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/archives/2006/04/database_war_stories_5_craigsl.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# Database War Stories #5:  craigslist

## Full text

Eric Scheide of craigslist offered me a stream of consciousness summary of the craigslist database setup. At a conference last year, Craig showed a slide (which helped inspire my postings about asymmetric competition [[1](http://radar.oreilly.com/archives/2006/04/purposedriven_media.html), [2](http://radar.oreilly.com/archives/2006/04/shrink_a_market.html), [3](http://radar.oreilly.com/archives/2006/04/what_job_does_a_book_do.html)]) that listed the number of employees at the top ten web sites. Most of them have thousands of employees. Some have tens of thousands. Craigslist, at #7 on the list, has 19. 

Eric's email has that embattled "news from the front" feel that you might expect from a site handling that much traffic with only 19 employees!

First, in response to my question about the craigslist database architecture, Eric wrote:

> "all database machines are on 64 bit linux boxen/ 14 local drives with 16gig of ram. 
> 
> craigslist runs clusters of dbs for each of our various services: 
> 
> forums: 1 master and 1 slave (mostly for backup) myIsam tables everywhere. DataDir size including indexes 17G. Largest table is approaching 42 million rows. 
> 
> classifeds: 1 master and 12 slaves. We have various flavor of slave databases. we have teamreader, longreader, thrashbox, for backups and very long adhoc queries and a few extra boxen. At times we have an offsite slave incase the colo goes dark. Currently this is on hold until we get a bigger pipe to our office location. Current footprint including indexes 114G, 56 million rows in the largest table (it's time to archive some of those oh yes it is) yesterday we wrote 330000 new rows to this table; Myisam everywhere, mostly because it works. 
> 
> ArchiveDB: 1 master 1 slave. holds all craiglsist postings older than about 3 months. Looks very similar to classifieds except bigger. 238Gigs, 96 million rows. Oh yea we use merge tables all over the archive spliting data into more managable chunks. We may do this in production soon. 
> 
> searchdbs: 16 of these in 4 clusters. We take live postings and split them by area/category type (sfbay/housing) and then use myisam full text indexing. each cluster only contains a subset of all positngs. We find the right host/table in software. This runs good, but do not think this solution will scale for much more than year. Indexing is expensive and we have a lot of churn. 
> 
> Authdb: 1 master and 1 slave. smallish. 
> 
> a few smaller "junk" db's that have transient data."

In response to my question about lessons learned in managing the data store, Eric wrote:

> "databases are good at doing some of the heavy lifting, go sort this, give me some of that, but if your database gets hot you are in a world of trouble so make sure can cache stuff up front. Protect your db! 
> 
> you can only go so deep with master -> slave configuration at some point you're gonna need to break your data over several clusters. Craigslist will do this with our classified data sometime this year. 
> 
> Do Not expect FullText indexing to work on a very large table. It's just not fast enough for what user expect on the web and an updating rows will make bad things happen. We want forward facing queries to be measured in a few 100ths of a second. 
> 
> There appears to be such a thing as a keybuffer that is too large even if you aren't swapping. Performance blows. So be careful when you bump up the key buffer. But do find the sweet spot. 
> 
> mysql seems to really love 64 bit boxen. we recently switched to 64 bit, added a few drives and basically took all the mountains out of our load charts."

As to war stories and lessons learned, he wrote:

> "mysql upgrades can be the best thing ever [but can also] make you hate yourself. 
> 
> We upgraded our search clusters to 4.1x a while back and got a huge performance boost from 4.0. there were no notes in the change log that fulltext indexing had been touched but it surely rocked. 
> 
> We once rolled at a minor revision 4.0.x 4.0.x++ and query optimization flipped over on its head, seemed fine in testing. It suddenly was choosing complete different indexes than the prior version. But only in some cases. So it hit the live site and bad things happened."

  
In response to my question about any information on the scale and type of data they manage and its growth, he wrote:  
rates

> "some numbers in the data section above. craigslist tends to have 200% growth yearly both in posting and reading."

  
_**More entries in the database war stories series:[Second Life](http://radar.oreilly.com/archives/2006/04/web_20_and_databases_part_1_se.html), [Bloglines and Memeorandum](http://radar.oreilly.com/archives/2006/04/database_war_stories_2_bloglin.html), [Flickr](http://radar.oreilly.com/archives/2006/04/database_war_stories_3_flickr.html), [NASA World Wind](http://radar.oreilly.com/archives/2006/04/database_war_stories_4_nasa_wo.html), [O'Reilly Research](http://radar.oreilly.com/archives/2006/05/database_war_stories_6_oreilly.html), [Google File System and BigTable](http://radar.oreilly.com/archives/2006/05/database_war_stories_7_google.html), [Findory and Amazon](http://radar.oreilly.com/archives/2006/05/database_war_stories_8_findory_1.html), [Brian Aker of MySQL Responds](http://radar.oreilly.com/archives/2006/05/brian_aker_of_mysql_responds.html)**_.
