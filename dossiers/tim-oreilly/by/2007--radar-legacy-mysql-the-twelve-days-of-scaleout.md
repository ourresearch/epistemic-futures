---
title: "MySQL:  The Twelve Days of Scaleout"
person: tim-oreilly
section: by
type: blog-post
year: 2007
date: 2007-06-15
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/archives/2007/06/mysql_the_twelv.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# MySQL:  The Twelve Days of Scaleout

## Full text

Working to make clear that it is a database for the big boys, [MySQL](http://www.mysql.com) is running a series of posts on their web site called [The Twelve Days of Scale Out](http://www.mysql.com/why-mysql/scaleout/). Each day features a different customer who has taken MySQL to the moon. [Today's feature (Day 5) covers Wikipedia](http://www.mysql.com/why-mysql/scaleout/wikipedia.html). 

The page quotes [Redmonk](http://www.redmonk.com) analyst Steven O'Grady: 

> "The notion persists within many traditional enterprises that once you reach a certain level of application importance, it is necessary to transition to big, expensive boxes running big, expensive databases. However, free-thinking members of their IT staffs are beginning to ask the question: 'What can we learn from Google, Yahoo, and Wikipedia on how to scale for high growth?' "

Here are a few stats from the article. Wikipedia has: 

  * More than 154 million annual visitors 
  * More than 5 million articles 
  * More than 290,000 contributors 
  * Nearly half a million edits each day 
  * 25,000 SQL queries/second 
  * 20 servers, with MySQL replication used to add more as needed 

I was actually a bit surprised by the low server count. I would have expected more, given Wikipedia's traffic.

Disclosure: I am on the board of MySQL and O'Reilly produces the MySQL User Conference for MySQL AB.
