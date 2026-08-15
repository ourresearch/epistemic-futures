---
title: "Web 2.0 and Databases Part 1:  Second Life"
person: tim-oreilly
section: by
type: blog-post
year: 2006
date: 2006-04-24
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/archives/2006/04/web_20_and_databases_part_1_se.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# Web 2.0 and Databases Part 1:  Second Life

## Full text

As part of the prep for my keynote on Wednesday at the [MySQL User Conference](http://www.mysqluc.com/), I decided to ask some of my Web 2.0 friends just how they were using databases in their applications. Over the next couple of days, I'm going to post what I heard back. I'm not going to draw any conclusions till the end of the series, but just let people speak for themselves.

In this first installment, a few thoughts from Cory Ondrejka and Ian Wilkes of Linden Labs, creators of [Second Life](http://www.secondlife.com). Cory wrote:

> Your timing is, of course, perfect because we're a) in the midst of converting much of our backend architecture away from custom C++/messaging and into web services and b) we spent yesterday afternoon fighting some database cliff that we just hit.

> Since I'm about to get on a redeye, let me introduce you to Ian Wilkes, our Director of Operations and architect of Second Life's database and asset backends. Ian can give you the 10 cent tour and certainly has some keynote worthy war stories from 4 years of work on Second Life. Probably starting with the time he had to give Philip Rosedale and me the "flat files are not going to cut it"-talk :-) 
> 
> From my end, the worst MySQL moment was when, in the midst of a colo move we decided that we could bring the system back up before we had moved our slave database. After all, what are the odds of the primary going down in the 2 hours it would take to schlep the slave over and bring it up? Apparently the odds were 100%.
> 
> Separately -- in your no doubt copious free time -- you might enjoy getting a brain dump on our move to web services. I don't think anyone really groks what's going to happen when we fully connect to the web this way . . .

(I definitely want that brain dump, and will pass it along when I get it!) Meanwhile, over to Ian:

> Like everybody else, we started with One Database All Hail The Central Database, and have subsequently been forced into clustering. However, we've eschewed any of the general purpose cluster technologies (mysql cluster, various replication schemes) in favor of explicit data partitioning. So, we still have a central db that keeps track of where to find what data (per-user, for instance), and N additional dbs that do the heavy lifting. Our feeling is that this is ultimately far more scalable than black-box clustering. Right now we're still in the transition process, so we remain vulnerable to overload. As Cory mentioned, we're moving to an HTTP-based internal communication model in order to improve our flexibility. 
> 
> I think the biggest lesson we learned is that databases need to be treated as a commodity. Standardized, interchangeable parts are far better in the long run than highly-optimized, special-purpose gear. Web 2.0 applications will require more horsepower with less money than One Database or his big brother One Cluster All Hail The Central Cluster will offer. (After all, a 64-way Mysql Cluster installation is just the budget-friendly version of a Sun E-10000.) Unfortunately, this seems to be the minority view, at least if the dearth of automated db provisioning tools is any indication.
> 
> Our most interesting war stories don't generally involve the database - yes once we lost data and had to roll back the world a few hours, but who else can claim downtime due to grey goo? Perhaps the best illustration of the lesson above is a story of success. Lots of people have memories and/or fears of racing to the colo to fix the one machine that's bringing down the system; we can bring spare dbs on line from the comfort of our own homes, and worry about repairs at our leisure. "I can add database capacity in my underwear!"

_**More entries in the database war stories series:[Bloglines and Memeorandum](http://radar.oreilly.com/archives/2006/04/database_war_stories_2_bloglin.html), [Flickr](http://radar.oreilly.com/archives/2006/04/database_war_stories_3_flickr.html), [NASA World Wind](http://radar.oreilly.com/archives/2006/04/database_war_stories_4_nasa_wo.html).**_
