---
title: "Your Money or Your MySQL"
person: tim-oreilly
section: by
type: blog-post
year: 2005
date: 2005-10-11
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/archives/2005/10/your_money_or_your_mysql_1.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# Your Money or Your MySQL

## Full text

[Andy Oram](http://www.praxagora.com/andyo/) recently sent around to the O'Reilly editors' list some thoughts on the recent acquisition of InnoDB, MySQL's enterprise component, by Oracle. They are a thought provoking read, even in the version below, which is sanitized of some insider gossip that Andy felt would be better not repeated off O'Reilly's lists. While I've long maintained that licenses are a red herring when it comes to understanding the true importance of open source, there are definitely business implications to the license chosen. As Andy speculates, Oracle's purchase may well be an attempt to use the same dual licensing strategy that MySQL has employed so successfully against them. Here's Andy:

**Your money or your MySQL**

On Friday, October 7, Oracle announced that it bought a key technology behind MySQL: InnoDB. Here is some background, analysis, and rampant speculation. 

**Background**

MySQL is a dual-licensed database engine. The company makes its money by selling licenses to companies that want to incorporate MySQL into commercial products. MySQL is open-source for everybody else, hence its popularity. 

MySQL used to have a single type of database that lacked such features as transactions and row-level locking, features considered so fundamental to databases that for a long time MySQL was called a toy. Several years ago the company took a big leap in offering these features--but rather than develop them in-house, they licensed outside talent. 

(The history of MySQL AB's deals with other companies is interesting: its first attempt to implement transactions took software from SleepyCat, but it fell pretty much into disuse after InnoDB came along. Now MySQL AB is using talent from SAP to add a lot of SQL compliance. In short, a few brilliant coders can't always do it all themselves; they can use help from experienced outsiders--although apparently InnoDB was developed originally by one brilliant coder, Heikki Tuuri. By now MySQL AB is huge, though, so they can probably move more development in-house--and that will save them now.) 

InnoDB is what they ended up with, and it is the center of the "enterprise" features they are now leveraging to become a major vendor. It was dual-licensed to MySQL on the same terms that MySQL was licensed to its users. That InnoDB is the intellectual property of another company is an Achilles heal for MySQL AB, and Paris's arrow has now struck. 

**The buy-out**

There is no indication what the buy-out offers either Oracle or InnoDB. For the developer of InnoDB, Heikki Tuuri, the draw was probably financial. But strangely enough, the next day Tuuri was back on IRC helping random users with questions. So he still has class! 

Oracle and InnoDB claim they'll continue developing the product and offering it to MySQL AB on the same terms. MySQL declares "business as usual" and various other platitudes. But it's really hard to believe that the tiny InnoDB company with their lightweight storage engine had any technology or skill to offer Oracle. 

And look at the timing! Just as MySQL 5.0 becomes official. The moment for FUD couldn't be better. 

**The response**

MySQL's current contract with InnoDB extends another year and a half. They may well find an accommodation and keep on track. (There are many enhancements being planned for InnoDB.) But as I said before, MySQL AB has grown a lot and developed some rich and powerful friends. It probably has the resources in place for replacing InnoDB, should it feel that's necessary. 

**Impact**

I think the adoption of MySQL by new, large enterprises--what MySQL AB is currently gunning for--will be slightly slowed down by the Oracle news, but will continue anyway. 

This incident seems to combine elements of two putative crises in the Linux world: the SCO lawsuits and the BitKeeper incident. 

SCO, like Oracle, used a lightning strike that was both heavy-handed and underhanded to try to leverage its power. I think Oracle has more of a chance of succeeding (it has a stronger position in the industry and knows what it's doing) but ultimately the open-source community will prevail. Paris killed Achilles, remember, but Troy still lost. 

BitKeeper was a proprietary version control package that Linux developers used to maintain kernel code. (MySQL uses it too.) As with MySQL and InnoDB, Linux's reliance on the makers of BitKeeper was a potential risk. When the owners of BitKeeper announced they were withdrawing the free version, scads of commentators announced this was a crisis for Linux. Yet Linus Torvalds and others quickly developed a replacement that the free software community now thinks may be a breakthrough for version control. Once again, the community overcomes the blows of the proprietary world.
