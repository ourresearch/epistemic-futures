---
title: "Database War Stories #4:  NASA World Wind"
person: tim-oreilly
section: by
type: blog-post
year: 2006
date: 2006-04-27
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/archives/2006/04/database_war_stories_4_nasa_wo.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# Database War Stories #4:  NASA World Wind

## Full text

Patrick Hogan of [NASA World Wind](http://worldwind.arc.nasa.gov/), an open source program that does many of the same things as Google Earth, uses both flat files and SQL databases in his application. Flat files are used for quick response on the client side, while on the server side, SQL databases store both imagery (and soon to come, vector files.) However, he admits that "using file stores, especially when a large number of files are present (millions) has proven to be fairly inconsistent across multiple OS and hardware platforms."

I asked: "Tell me about your database architecture for NASA World Wind." Patrick replied:

> "What appears to the user as a single image of a very large physical range really consists of millions of images. In an application like World Wind, which displays many different kinds of large ranges, the database must hold billions of **images** (Gigaimages) or references to them. Each image, although typically ~20KB can also be megabytes in size. 
> 
> Demand on the image-serving database is bursty and intense. Dozens of images could be needed immediately with each small change in the user's view direction.
> 
> On the client side of World Wind, there is very limited use of traditional SQL-based databases. The client depends mostly on flat-file stores to maintain data. However, on the server side of things, World Wind enabled servers have relied on SQL-based databases to store imagery and will soon in-the near future deliver vector-based data via the WFS protocol. World Wind already delivers data via WMS."

In response to my question about lessons learned in managing their data store, Patrick wrote:

> "[1]Using file stores, especially when a large number of files are present (millions) has proven to be fairly inconsistent across multiple OS and hardware platforms. This method basically relies on the underlying OS to handle the "database", and this leaves room for irregularities, which we have experienced. Moving towards a more efficient and consistent solution, like a light-weight SQL database might solve a couple issues, but could add a level of complexity above and beyond our current system, which enjoys a fairly easy-to-understand structure. 
> 
> [2] An API-centric architecture, with all functionalities as modular components, which is how we are refactoring the implementation, would have saved us some rework. It is interesting to watch the advances being made by the .NET and Java technologies that will allow for much greater speed in the product development cycle.... I guess the biggest news is that we will have a 'shared' architecture of  
>  these implementations (.NET and Java) that will remain structurally identical. The intent is to allow plugins to be used as interchangeably as possible, i.e. via Python. 

When I asked him about the scale and type of data his application manages and its growth rates, Patrick wrote:

> "On our own servers, we serve a couple Terabytes worth of imagery for each Earth dataset (and there are several of these) for just 15-meter coverage. Once you go to the submeter resolution, these numbers quadruple a couple times. Imagery datasets will grow and rather quickly. NASA plans to deliver at least 250 times more Lunar and Mars data from the latest LRO (Lunar Reconnaissance Orbiter) and MRO (Mars Reconnaissance Orbiter) satellites. Elevation datasets will remain relatively small, in the hundreds of MBs."

_**More entries in the database war stories series:[Second Life](http://radar.oreilly.com/archives/2006/04/web_20_and_databases_part_1_se.html), [Bloglines and Memeorandum](http://radar.oreilly.com/archives/2006/04/database_war_stories_2_bloglin.html), [Flickr](http://radar.oreilly.com/archives/2006/04/database_war_stories_3_flickr.html), [Craigslist](http://radar.oreilly.com/archives/2006/04/database_war_stories_5_craigsl.html), [O'Reilly Research](http://radar.oreilly.com/archives/2006/05/database_war_stories_6_oreilly.html), [Google File System and BigTable](http://radar.oreilly.com/archives/2006/05/database_war_stories_7_google.html), [Findory and Amazon](http://radar.oreilly.com/archives/2006/05/database_war_stories_8_findory_1.html), [Brian Aker of MySQL Responds](http://radar.oreilly.com/archives/2006/05/brian_aker_of_mysql_responds.html)**_.
