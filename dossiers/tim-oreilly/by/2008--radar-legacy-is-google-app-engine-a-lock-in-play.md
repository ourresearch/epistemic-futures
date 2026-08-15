---
title: "Is Google App Engine a Lock-in Play?"
person: tim-oreilly
section: by
type: blog-post
year: 2008
date: 2008-04-14
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/archives/2008/04/is-google-app-engine-a-lockin.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# Is Google App Engine a Lock-in Play?

## Full text

Venture capitalist Brad Feld just put up an intriguing post [ comparing Google App Engine to Amazon EC2](http://www.feld.com/blog/archives/2008/04/what_exactly_is.html). The meat of the entry is from an analysis by Brad's friend Scott Moody. Here are the juiciest bits, pro and con: 

> With EC2, you still have to set-up load balancers, configure multiple replicated database servers, implement scalability hacks if things grow too fast (such as distributed caching of data via memcached), keep distros and apps up-to-date, etc. Bottom Line: EC2-based companies still require sys admins, AppEngine companies don't. That will certainly change as more companies begin offering EC2 server management services. 
> 
> Google provides a non-relational datastore and that's the only datastore available (no traditional file system, no relational databases). With EC2, people generally use MySQL or Postgresql. Amazon offers a non-relational datastore called SimpleDB, but it's a bit *too* simple. For example, it does not support sorting of results sets. Huh? That makes it non-workable in my opinion. There's also an issue with using EC2 virtual machines for your database servers -- Amazon says that when a virtual machine crashes, all the data managed by it disappears, so virtual machine crash = hard drive crash. 
> 
> With EC2, programmers can use any (non-Microsoft) language to develop their apps. AppEngine users must code in Python. Also, Google does not support sockets at this time. All cross-app communication must be done via HTTP. 
> 
> At *this* moment in time, it would be difficult to move apps off of AppEngine. Doing that in EC2 is trivial. This, to me, is the biggest issue, as I believe it could make startups less-interesting from an acquisition perspective by anyone other than Google. This will most likely change as people develop compatibility layers. However, Google has yet to provide any information about how to migrate data from their datastore the best I can tell. If you have a substantial amount of data, you can't just write code to dump it because they will only let any request run for a short period before they terminate it. 

This last point is really very serious. I've been [warning for some time](http://radar.oreilly.com/archives/2007/08/my-tonguelashing-from-eben-mog.html) that the first phase of Web 2.0 is the acquisition of critical mass via network effects, but that once companies achieve that critical mass, they will be tempted to consolidate their position, leading ultimately to a replay of the personal computer industry's sad decline from an open, energetic marketplace to a controlled economy. 

Now it may be that this is a temporary oversight, and that Google does intend, long term, to make it easy for developers to export their applications. After all, Eric Schmidt says he reminds his employees all the time, "[Don't fight the internet](http://radar.oreilly.com/archives/2006/07/levels-of-the-game-the-hierarc.html)." But it's also possible that this is one more sign that one of the big guys is forgetting the principles -- the internet as a platform (not "my company as a platform"), harnessing the power of user contribution (which as [John Musser pointed out](http://radar.oreilly.com/research/web2-report.html) means that you always "pay the user first"), small pieces loosely joined-- that brought their success in the first place. 

Keeping the internet as an open platform is a choice. We didn't understand what was happening to the PC ecosystem, but we've seen this movie before, so we should recognize and fight this plot line when we see it happen on the internet. We need to keep our cloud services vendors honest, and tell them we want an open, interoperable platform, not one based on lock-in. 

Of course, as some wag said, "the only thing we learn from history is that people don't learn from history." 

P.S. There's some further good discussion on the lock-in issue in a [Q&A about AppEngine put together by Stephen O'Grady](http://redmonk.com/sogrady/2008/04/09/clouds-rolling-in-the-google-app-engine-qa/).
