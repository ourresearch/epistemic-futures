---
title: "Yahoo!'s bet on Hadoop"
person: tim-oreilly
section: by
type: blog-post
year: 2007
date: 2007-08-03
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/archives/2007/08/yahoos_bet_on_h.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# Yahoo!'s bet on Hadoop

## Full text

One of the most important announcements at Oscon last week was Yahoo!'s commitment to support [Hadoop](http://www.hadoop.org</a). We've been [writing about Hadoop on radar](http://www.google.com/search?q=site:radar.oreilly.com) for a while, so it's probably not news to you that we think Hadoop is important. 

Yahoo's involvement wasn't actually news either, because Yahoo! had hired [Doug Cutting](http://en.wikipedia.org/wiki/Doug_Cutting), the creator of hadoop, back in January. But [Doug's talk at Oscon]() was kind of a coming out party for Hadoop, and Yahoo! wanted to make clear just how important they think the project is. In fact, I even had a call from David Filo to make sure I knew that the support is coming from the top.

Jeremy Zawodny's [post about hadoop on the Yahoo! developer network](http://developer.yahoo.net/blog/archives/2007/07/yahoo-hadoop.html) does a great job of explaining why Yahoo! considers hadoop important: 

> For the last several years, every company involved in building large web-scale systems has faced some of the same fundamental challenges. While nearly everyone agrees that the "divide-and-conquer using lots of cheap hardware" approach to breaking down large problems is the only way to scale, doing so is not easy. 
> 
> The underlying infrastructure has always been a challenge. You have to buy, power, install, and manage a lot of servers. Even if you use somebody else's commodity hardware, you still have to develop the software that'll do the divide-and-conquer work to keep them all busy. 
> 
> It's hard work. And it needs to be commoditized, just like the hardware has been... 
> 
> To build the necessary software infrastructure, we could have gone off to develop our own technology, treating it as a competitive advantage, and charged ahead. But we've taken a slightly different approach. Realizing that a growing number of companies and organizations are likely to need similar capabilities, we got behind the work of Doug Cutting (creator of the open source Nutch and Lucene projects) and asked him to join Yahoo to help deploy and continue working on the [then new] open source Hadoop project.

Let me unpack the two parts of this news: hadoop as an important open source project, and Yahoo!'s involvement. On the first front, I've been arguing for some time that [free and open source developers need to pay more attention to Web 2.0](http://radar.oreilly.com/archives/2006/08/open_source_licenses_are_obsol.html). Web 2.0 software-as-a-service applications built on top of the LAMP stack now generate several orders of magnitude more revenue than any companies seeking to directly monetize open source. And most of the software used by those Web 2.0 companies above the commodity platform layer is proprietary. Not only that, Web 2.0 is siphoning developers and buzz away from open source. 

But there are open source projects that are tackling important Web 2.0 problems "up the stack." Brad Fitzpatrick's LiveJournal scaling tools memcached, perlbal, and mogileFS come to mind, as well as OpenID. Hadoop is another critical piece of Web 2.0 infrastructure now being duplicated in open source. (I'm sure there are others, and we'd love to hear from you about them in the comments.) 

OK -- but why is Yahoo!'s involvement so important? First, it indicates a kind of competitive tipping point in Web 2.0, where a large company that is a strong #2 in a space (search) realizes that open source is a great competitive weapon against their dominant competitor. It's very much the same reason why IBM got behind Eclipse, as a way of getting competitive advantage against Sun in the Java market. (If you thought they were doing it out of the goodness of their hearts rather than clear-sighted business logic, think again.) If Yahoo! is realizing that open source is an important part of their competitive strategy, you can be sure that other big Web 2.0 companies will follow. In particular, expect support of open source projects that implement software that Google treats as proprietary. (See the long discussion thread on my post about [Microsoft's submission of their shared source licenses to OSI](http://radar.oreilly.com/archives/2007/07/microsoft_to_su_1.html) for my arguments as to why "being on the right side of history" will ultimately drive Microsoft to open source.) 

Supporting Hadoop and other Apache projects not only gets Yahoo! deeply involved in open source software projects they can use, it helps give them renewed "geek cred." And of course, attracting great people is a huge part of success in the computer industry (and for that matter, any other.) 

Second, and perhaps equally important, Yahoo! gives hadoop an opportunity to be tested out at scale. Some years ago, I was on the board of Doug's open source search engine effort, Nutch. Where the project foundered was in not having a large enough data set to really prove out the algorithms. Having more than a couple of hundred million pages in the index was too expensive for a non-profit open source project to manage. One of the important truths of Web 2.0 is that it ain't the personal computer era any more, [Eben Moglen's arguments to the contrary notwithstanding](http://www.linux.com/feature/118201). A lot of really important software can't even be exercised properly without very large networks of machines, very large data sets, and heavy performance demands. Yahoo! provides all of these. This means that Hadoop will work for the big boys, and not just for toy projects. And as Jeremy pointed out in his post (linked and quoted above), today's big boy may be everyday folks a few years from now, as the size and scale of Web 2.0 applications continue to increase. 

BTW, in followup conversations with Doug, he pointed out that web search is not actually the killer app for hadoop, despite the fact that it is in part an implementation of the [MapReduce](http://labs.google.com/papers/mapreduce.html) technique made famous by Google. After all, Yahoo! has been doing web search for years without this kind of general purpose scaling platform. "Where Hadoop really shines," says Doug, "is in data exploration." Many problems, including tuning ad systems, personalization, learning what users need -- and for that matter, corporate or government data mining -- involve finding signal in a lot of noise. Doug pointed me to an interesting article on Amazon Web Services Developer Connection: [Running Hadoop MapReduce on Amazon EC2 and Amazon S3](http://developer.amazonwebservices.com/connect/entry.jspa?externalID=873&categoryID=112). Doug said in email: 

> It provides an example of using Hadoop to mine one's [logfile] data. 
> 
> Another trivial application for log data that's very valuable is reconstructing and analyzing user sessions. If you've got logs for months or years from hundreds of servers and you want to look at individual user sessions, e.g., how often do users visit, how long are their sessions, how do they move around the site, do often do they re-visit the same places, etc. This is a single MapReduce operation over all the logs, blasthing through, sorting and collating all your logs at the transfer rate of all the drives in your cluster. You don't have to re-structure your database to measure something new. It's really as easy as 'grep | sort | uniq'. 
> 
> Also, here are [the slides from my talk](http://wiki.apache.org/lucene-hadoop/HadoopPresentations</a). 

_Update: In response to a comment, I updated this article to clarify what I was talking about regarding open source and the competitive landscape._
