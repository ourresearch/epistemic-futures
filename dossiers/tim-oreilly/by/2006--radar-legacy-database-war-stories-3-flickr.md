---
title: "Database War Stories #3:  Flickr"
person: tim-oreilly
section: by
type: blog-post
year: 2006
date: 2006-04-27
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/archives/2006/04/database_war_stories_3_flickr.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# Database War Stories #3:  Flickr

## Full text

Continuing my [series](http://radar.oreilly.com/archives/2006/04/web_20_and_databases_part_1_se.html) [of]() queries about how "Web 2.0" companies used databases, I asked Cal Henderson of [Flickr](http://www.flickr.com) to tell me "how the folksonomy model intersects with the traditional database. How do you manage a tag cloud?"

He replied: "lots of the 'web 2.0' feature set doesn't fit well with traditional normalised db schema design. denormalization (or heavy caching) is the only way to generate a tag cloud in milliseconds for hundereds of millions of tags. you can cache stuff that's slow to generate, but if it's so expensive to generate that you can't ever regenerate that view without pegging a whole database server then it's not going to work."

Here's the full text of my exchange with Cal:

The first question I asked was "what's your database architecture?" Here's what Cal had to say about that:

> "started as a big vertically scaled classic replication tree (well, started as a single box) and soon hit against performance walls in terms of writes (repl gives you more reads, same writes as slowest machine in your tree). when we started, we barely knew anything about how mysql works with indexes (the documentation is fairly non-beginner), so months of index wrangling to get better performance ensued.

> eventually there was only so much we could do, so we federated the main dataset into shards, organised by primary object (mainly users), splitting the data up into chunks. we do this in such a way that we can easily move data between shards as we add news ones or start hitting performance problems on old ones. our shards are master-master replication pairs."

Next, I asked about lessons learned in managing the data store, and any particular war stories that would make great illustrations of those lessons learned. Cal replied:

> "be careful with big backup files - writing or deleting several huge backup files at once to a replication filestore can wreck performance on that filestore for the next few hours as it replicates the backup files. doing this to an in-production photo storage filer is a bad idea.

> however much it costs to keep multiple days of backups of all of your data, it's worth it. keeping staggered backups is good for when you discover something gone wrong a few days later. something like 1, 2, 10 and 30 day backups.

I also asked for any information on the scale of data Flickr manages and its growth rates. Cal answered:

> total stored unique data : 935 GB   
>  total stored duplicated data : ~3TB

I also asked Cal: "I'm particularly interested in how the folksonomy model intersects with the traditional database. How do you manage a tag cloud? A lot of ideas about how databases are supposed to look start to go by the wayside..." He replied:

> "tags are an interesting one. lots of the 'web 2.0' feature set doesn't fit well with traditional normalised db schema design. denormalization (or heavy caching) is the only way to generate a tag cloud in milliseconds for hundereds of millions of tags. you can cache stuff that's slow to generate, but if it's so expensive to generate that you can't ever regenerate that view without pegging a whole database server then it's not going to work (or you need dedicated servers to generate those views - some of our data views are calculated offline by dedicated processing clusters which save the results into mysql).

> federating data also means denormalization is necessary - if we cut up data by user, where do we store data which relates to two users (such as a comment by one user on another user's photo). if we want to fetch it in the context of both user's, then we need to store it in both shards, or scan every shard for one of the views (which doesn't scale). we store alot of data twice, but then theres the issue of it going out of sync. we can avoid this to some extent with two-step transactions (open transaction 1, write commands, open transaction 2, write commands, commit 1st transaction if all is well, commit 2nd transaction if 1st commited) but there still a chance for failure when a box goes down during the 1st commit.

> we need new tools to check data consistency across multiple shards, move data around shards and so on - a lot of the flickr code infrastructure deals with ensuring data is consistent and well balanced and finding and repairing it when it's not."

_**More entries in the database war stories series:[Second Life](http://radar.oreilly.com/archives/2006/04/web_20_and_databases_part_1_se.html), [Bloglines and Memeorandum](http://radar.oreilly.com/archives/2006/04/database_war_stories_2_bloglin.html), [NASA World Wind](http://radar.oreilly.com/archives/2006/04/database_war_stories_4_nasa_wo.html), [Craigslist](http://radar.oreilly.com/archives/2006/04/database_war_stories_5_craigsl.html), [O'Reilly Research](http://radar.oreilly.com/archives/2006/05/database_war_stories_6_oreilly.html), [Google File System and BigTable](http://radar.oreilly.com/archives/2006/05/database_war_stories_7_google.html), [Findory and Amazon](http://radar.oreilly.com/archives/2006/05/database_war_stories_8_findory_1.html), [Brian Aker of MySQL Responds](http://radar.oreilly.com/archives/2006/05/brian_aker_of_mysql_responds.html)**_.
