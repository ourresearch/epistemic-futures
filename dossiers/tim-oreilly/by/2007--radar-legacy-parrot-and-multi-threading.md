---
title: "Parrot and Multi-threading"
person: tim-oreilly
section: by
type: blog-post
year: 2007
date: 2007-09-29
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/archives/2007/09/parrot_and_mult.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# Parrot and Multi-threading

## Full text

Over on the O'Reilly Network, [Kevin Farnham](http://www.oreillynet.com/pub/au/2168) has [an interesting blog post](http://www.oreillynet.com/linux/blog/2007/09/open_source_thoughts_parrot_an_1.html) about the connection between [Parrot](http://www.parrotcode.org/) and the arrival of multi-core processors ([Radar posts](http://www.google.com/search?client=safari&rls=en&q=site:radar.oreilly.com+multicore&ie=UTF-8&oe=UTF-8).) Kevin makes a number of good points, especially how changing fundamentals can help a technology to "arrive." (Think of how Ruby on Rails made Ruby suddenly the language of choice after ten years as a second-stringer, or how multicore is [renewing interest in languages like Erlang and Haskell](http://radar.oreilly.com/archives/2007/03/concurrent_prog_1.html).) Kevin is also absolutely right about how multi-core will affect even home computing. 

> Sometimes a technology is invented, and the time simply isn’t right, the need at the moment for solutions that apply that technology is nearly non-existent, though many people readily admit it’s a “wonderful” technology. I wonder if this might apply to a certain extent to Parrot prior to the age of many-core computing? 
> 
> In a few years, inexpensive PCs will have 8, 16, or more processing cores. Some people doubt that the average home or office user is going to have any use for all these cores. I think that’s like saying “no one will ever need more than 640K of RAM.” Once it’s possible for the average home or office user to apply algorithms and image analysis and video processing and stock market simulators that were previously available only on high-end workstations in data centers, you cannot tell me they won’t want to do this. 
> 
> ... 
> 
> I doubt that applying conventional low-level threads is going to be an efficient way to accomplish this in terms of programming time (I’ve worked at this level for a long time). But on the other side: no one is going to want to convert the mass of existing software platforms/applications that could potentially apply these computation libraries, into C++ or C. A convenient means to enable a broad spectrum of languages to call multithreaded C++, C, and Fortran libraries is going to be needed. Otherwise, again we face enormous software development inefficiency, as a separate interface has to be constructed for each library for each calling language. That’s not a solution that is going to fly, in my opinion. 
> 
> It seems to me that Parrot is an excellent candidate for addressing this problem. If this is the case, the Parrot team may soon find itself lent increasing support from independent developers, and possibly from companies who recognize the need for this capability with respect to their own applications. 
> 
> I don’t think this need was really there when PC performance could be improved simply through ever-increasing clock speeds. Single-threaded software that did a few simple calculations was fine then. Multicore, however, changes everything. As highly-scalable multithreaded computation / simulation libraries become available, and people realize they want them, and developers realize they need to be able to call these libraries from every language platform, Parrot’s time may arrive. 

Kevin's suggestion that Parrot may solve a big problem for multi-core programming also suggests that the wait for Perl 6 may not have been in vain. (I've always hesitated to count out Larry Wall, one of the true geniuses of programming, and he's backed up by some other great programmers.) 

Disclosure: a couple of people on the Parrot team, including Allison Randal and chromatic, work for O'Reilly.
