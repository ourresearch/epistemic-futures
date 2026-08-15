---
title: "Open Source:  Architecture or Goodwill?"
person: tim-oreilly
section: by
type: blog-post
year: 2006
date: 2006-08-07
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/archives/2006/08/open_source_architecture_or_go.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# Open Source:  Architecture or Goodwill?

## Full text

There are a lot of reasons why people make their code open source. I believe that one of the strongest original motivations has often been overlooked. Our hagiography tells the tale of how it all started with the quest for software freedom. But contemporaneous with [Richard Stallman's story](http://www.oreilly.com/catalog/freedom/index.html), other people were taking the same path (releasing source code) for a very different reason: the architecture of Unix. 

That architecture made two enormous contributions to the founding of the open source movement. First, and perhaps most important, Unix was architected as a communications-oriented system, with the idea of modular, cooperating processes and programs. That architecture meant that it was very easy for an individual or a small group to add a piece to the overall system without having too much coordination with the people adding other pieces. And so, we see a vibrant culture of cooperation and contribution in early Unix development, with many of the most important advances developed outside of ATT Bell Labs, the owner of Unix, even though the license was not open source by any standard.

But second, because Unix was an open system in a world where vendors were competing on the basis of their hardware, with slightly modified versions of Unix as the OS, the Unix platform became incredibly fragmented. You _had_ to distribute source code in order to give someone else the ability to run your program (unless they happened to be on the same hardware as you.) By contrast, standardized platforms like the PC and Mac developed a binary freeware culture, but never an open source culture. While Linux now runs on the standard PC architecture, and thus the _requirement_ for source has faded, it's important to remember the history as a backdrop to the social patterns of open source, because as everyone knows, social patterns persist longer than the circumstances that give rise to them, but do eventually fade away as the world changes.

Understanding this history is critical to framing the recent dustup between Matt Asay and Jeremy Zawodny. Reporting on [the session at OSCON](http://conferences.oreillynet.com/cs/os2006/view/e_sess/9454) that I held with Chris diBona of Google and Jeremy (of Yahoo!) and Jim Buckmaster of Craigslist, Matt wrote his analysis of [Why Google and Yahoo! Can't Be Better Open Source Citizens](http://weblog.infoworld.com/openresource/archives/2006/07/why_google_and.html). [Jeremy was rather put off](http://jeremy.zawodny.com/blog/archives/007112.html) by the spin Matt put on the session, and wondered "how much open source code he's been publishing."

Jeremy had every right to be incensed by the title of Matt's piece, because both Yahoo! and Google have made enormous efforts to give back to the open source community that gave them such a good start in life and is so important a part of their foundation. I think it's fair to say that both companies have contributed far more back to open source than Matt's company, [Alfresco](http://www.alfresco.com), even though the latter flies the flag of being an "open source company." And Jeremy makes some very strong arguments as to why Yahoo! can't release more of its core code. 

But the point I tried to bring out in the session, and that Matt picked up on in his blog, remains: in the PC era, you have to distribute software in order to get other people to use it. You can distribute it in binary form or you can distribute it in source form, but no one escapes the act of distribution. And when software is distributed, open source companies have proven that giving access to the source makes good business strategy.

But in the world of Web 2.0, applications never need to be distributed. They are simply performed on the internet's global stage. What's more, they are global in scope, often running on hundreds or thousands or even hundreds of thousands of servers. They have vast databases, and complex business processes required to keep those databases up to date.

As a result, one of the motivations to share -- the necessity of giving a copy of the source in order to let someone run your program -- is truly gone. Not only is it no longer required, in the case of the largest applications, it's no longer possible.

That's why companies are having to think about new ways to "open source" their product. In the [O'Reilly Radar Executive Briefing](http://conferences.oreillynet.com/pub/w/46/radar.html) at OSCON, we looked at three of those ways:

  1. **Keep the app proprietary but open source the framework used to build it.** Some examples include Basecamp: Ruby on Rails; Ellington: Django; DabbleDB: Seaside. You can also tease apart some of the most important tools originally developed for your app. For example, Livejournal: Memcached. Yahoo! and Google have done a lot of this. But as the argument between Matt and Jeremy illustrates, it's now an act of goodwill rather than an act of necessity. You can also argue that it's an act of forethought, because keeping the open source developer ecosystem healthy is good for the internet giants. It keeps the talent pool strong, and outside-in innovation happening. But because both goodwill and forethought tend to be in shorter supply than necessity, the architectural change in how software is developed may eventually lead to a weakening of the open source culture. These are some of the points that Matt was quite correctly hammering on based on the conversation at the session. 

To the extent possible, this also means that it's good practice for Web 2.0 companies to think about the internal modularity of their code, so it's easy to extract pieces that it makes sense to distribute. In this regard, I strongly recommend reading [an ACM Queue interview with Werner Vogels](http://www.acmqueue.com/modules.php?name=Content&pa=printer_friendly&pid=403&page=1), the CTO of Amazon, from earlier this year. Vogels argues that companies must have a "relentless commitment to a modular computer architecture that makes it possible for the people who build the applications to also be responsible for running and deploying those systems within a common IT framework." Modularity enables participation by outside developers; it also allows swift action by individuals and small internal teams. It's one of the keys to competitive success, especially in an era where traditional PC-based software is so complex that a new release is years in the making.

  2. **Figure out what "open services" mean.** Both Yahoo! and Google are doing a lot of great work here, as the mashup phenomenon attests. As I wrote recently, though, [we need an open services definition](http://radar.oreilly.com/archives/2006/08/open_source_licenses_are_obsol.html) that codifies best practices in the same way that the original [open source definition](http://www.opensource.org/docs/definition.php) did. 

  3. **Adopt the "clonable apps" model pioneered by[Ning](http://www.ning.com).** While Ning is set up as a consumer play, and its source visibility leaves much to be desired in the way of implementation (code is fragmented and hard to get all at once), the _idea_ of small clonable and modifiable open source apps on a web platform seems to me to be a very attractive one. I'd love to see more people playing with this idea.

It's a very interesting time to be in open source. Open source zealots need to realize that open source needs to be reinvented for the new platform architecture, and web 2.0 companies need to remember that open source isn't just goodwill, but an integral part of keeping the developer ecosystem healthy. And everyone needs to experiment with new models, and not believe that the story has already been written.
