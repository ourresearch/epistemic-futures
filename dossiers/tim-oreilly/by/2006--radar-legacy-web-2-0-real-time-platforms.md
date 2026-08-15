---
title: "Web 2.0:  Real Time Platforms"
person: tim-oreilly
section: by
type: blog-post
year: 2006
date: 2006-08-09
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/archives/2006/08/real_time_platforms.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# Web 2.0:  Real Time Platforms

## Full text

The post that Nat made this morning about Mark Lucovsky and the Google AJAX search API has some wonderful backstory. Mark is just a fascinating guy, and has a unique perspective on how platforms are changing. He's a big thinker, and has a great way of capturing the fundamental differences between developing for a web 2.0 platform like Google vs. a PC platform. I wanted to share some of the comments that Mark made during the email thread that started with his request to "mash up" an OSCON web page with the new Google search APIs.

We first met Mark in 2001, when he keynoted at our [P2P and Web Services Conference](http://conferences.oreilly.com/p2p), speaking about Microsoft's ambitious Hailstorm initiative. (Before leaving Microsoft, Mark wrote a great summary of how, despite its bad rap, [Hailstorm prefigured much of the really great internet-as-platform goodness](http://mark-lucovsky.blogspot.com/2005/05/don-box-and-hailstorm.html) that we're now celebrating as Web 2.0. I've always felt that if it hadn't come from Microsoft at the height of the antitrust brouhaha, Hailstorm would have been a huge success. It had so many of the right ideas.) Last year, Mark went to Google, where he is now building a set of AJAX interfaces and "gadgets" that make it as easy to use all of the Google search apis as it is to build a web page. 

The thread started with a simple request from Mark. "I am speaking at SES this wednesday on search apis. I am not sure everyone really understands the concept of search mashups so I wanted to show a real example, but do it in the context that everyone at the conference would understand... " He wanted to take the OSCON web page, add a Google Map Search widget to it, and use it in a slide at his Search Engine Strategies talk. I thought what he was doing was cool, and asked if I could blog his email. In the course of the ensuing email exchange, though, his infectious enthusiasm for the new platform bubbled over: 

> I tell you, doing platform development, in real time, with no friction is rule changing.... How odd is it that I can just tell you that I will write the code tonight or tommorrow and then whenever I feel like it, push a button that makes it available to the entire world? Have you ever worked with a platform like this before? 

This last comment echoed a conversation that Mark had made when I first met with him about his work at Google a couple of months ago, and which led me to invite him to the [O'Reilly Radar Executive Briefing](http://conferences.oreillynet.com/pub/w/46/radar.html) at OSCON. So now I had to ask if I could blog THAT.

And it kept getting better. Mark is such an articulate spokesman for how the rules of software development are changing! More than anyone else I've talked with, he has a keen sense of contrast between the old world of software development and the new one. He wrote:

> What I am experiencing, and something I have discussed with both of you is the concept of "real time platforms" and what is at the core of that. Its very different from when I was producing kernel32.dll, ntoskrnl.exe, etc. [for Microsoft Windows] In those systems I still wrote code every day, produced countless binaries each day, etc. I just did not have a ship vehicle other than the manufactured CD. Since everyone shared the same CD, and since it was the norm for every piece of code to be tightly bound to every other piece of code, the ship cycles for those CDs were very very long. 
> 
> With real time platforms, you leverage the fact that the most successful and dynamic systems are loosely coupled and operate on well understood standards. You minimize dependencies, OR you stage them in in proper pre-requisite chains. For instance, its not uncommon for me to make a minor protocol enhancement one week, and code that responds to that protocol change the next. Gives me a chance to monitor the protocol change to ensure its doing what's expected, and once I have verified this, I can write the code that responds to the changes. This is one small example of loose coupling in action, but is also an example of the mindset shift that you need to make when delivering platform level functionality in real time. You need to think in terms of "I added a method or property to this object and launched it last night". The packaged software developer has no concept of the "and launched it last night" part of this equation so for him, he thinks in terms of building a major new set of capabilities into a dll, something that might have taken a small team a year or two to build and test. If you asked him to ship something from his team that is production quality every single week he would have to totally re-think how he does his scheduling, "integration testing", manages his build cycle, etc. 
> 
> I certainly don't think that the packaged software model is dead. I think it will be with us for a long time. My blog post from long ago was more about the fact that more and more software that we use is being delivered in a completely different way. Something much more like the real time platform model that I am currently involved in.... I think things have shifted with web2.0 and that shipping software takes on an entirely new meaning with an entirely new set of dynamics.  
> 

Mark's actually been writing about this topic for some time. The February 2005 blog entry he refers to, [Shipping Software](http://mark-lucovsky.blogspot.com/2005/02/shipping-software.html) should be required reading for anyone thinking about modern software development. But he's now coined a meme that's new to me, "real time platforms." This definitely needs to be added to my [Web 2.0 meme map](http://www.oreillynet.com/oreilly/tim/news/2005/09/30/graphics/figure1.jpg), and be part of the core framing for [What is Web 2.0?](http://www.oreillynet.com/go/web2)

In addition, I've often talked about the importance of software modularity to the success of open source (see [The Architecture of Participation](http://www.oreillynet.com/pub/a/oreilly/tim/articles/architecture_of_participation.html), as well as Monday's blog entry, [Open Source: Architecture or Goodwill?](http://radar.oreilly.com/archives/2006/08/open_source_architecture_or_go.html)) Mark's comments make clear the new face of modularity inside massive Web 2.0 applications. If they aren't modular, they lose the agility required for real time platforms.
