---
title: "lift/scala for web apps"
person: tim-oreilly
section: by
type: blog-post
year: 2007
date: 2007-05-04
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/archives/2007/05/liftscala_for_w.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# lift/scala for web apps

## Full text

[Ben Bangert](http://groovie.org/) wrote on the O'Reilly editors mailing list: 

> Not to be left out in the "doing cool things on the web", is a fairly new framework for [Scala](http://www.scala-lang.org/) (another highly functional language with some similar features to Erlang and Smalltalk) called [lift](http://liftweb.net/). There's [an interesting post by the author](http://blog.circleshare.com/index.php?/archives/55-Prance-with-the-Horses,-Skittr-with-the-Mice.html) showing a twittr clone he claims can scale to handle twittr's traffic with only 2 machines thanks to message persistence with the Actor based model. 
> 
> The neat thing about the code examples shown is that they look substantially easier to follow and maintain than code I've seen for Haskell, plus with Scala you can use existing Java classes and libraries.

This looks really interesting! From the [lift web site](http://liftweb.net/): 

> lift is yet another web development framework. lift runs inside a Java web container and uses the Scala programming language for coding. lift stresses security, developer productivity, ease of deployment, ease of maintainability, performance, and compatibility with existing systems. 
> 
> lift borrows from the best of existing frameworks including [Seaside](http://seaside.st/)'s highly granular sessions and security, [Rails](http://www.rubyonrails.com/) fast flash-to-bang, [Django](http://www.djangoproject.com/)'s "more than just CRUD is included", and [Erlyweb](http://erlyweb.org/)'s scalability for Comet-style applications. 
> 
> lift is built on Scala, a hybrid Functional and O-O language that compiles code down to the Java Virtual Machine. Scala code can call any Java code and make use of all Java classes. Java code can call some Scala code. lift applications are packaged as WAR files and can be deployed on any Servlet 2.4 engine (e.g., Tomcat 5.5.xx, Jetty 6.0, etc.) 
> 
> lift code is as clean and brief as Rails, yet performs 6 times faster and is multithreaded. Additionally, because Scala is strongly typed, the compiler catches type errors. 

In followup discussion about the Java VM as a target for multithreaded languages, [Keith Fahlgren](http://kfahlgren.com/blog/) wrote: "The JVM is steamrolling everything! Just ran across a [JVM-backed GHC-based Haskell translator](http://www.cs.rit.edu/~bja8464/lambdavm/). (via [Philip Wadler](http://www.oreillynet.com/pub/au/2440), the guy who wrote our [Java Generics](http://www.oreilly.com/catalog/javagenerics/index.html) book.)" 

As you may know if you've been following this blog, we're seeing an upsurge in interest in functional programming languages, based in part on the rise of multi-core and other parallel programming architectures. On that note, I should mention this Wednesday's lecture in [Dennis Allison's class at Stanford](http://www.stanford.edu/class/ee380/), [Multi-core, Multiprocessor, and Memory Hierarchies: An Application Developer's View of Next Generation Systems Enablement](http://www.stanford.edu/class/ee380/Abstracts/070509.html)

Keith went to a related talk last week, and noted:

> Yeah, the one last week from the same series was quite good and well attended (70 , I think). "[Taking Concurrency Seriously: New Directions in Multiprocessor Synchronization](http://www.stanford.edu/class/ee380/Abstracts/070502.html)" mainly dealt with a harnessing (Software) Transactional Memory and existing (potentially lock-based) low-level concurrent collections (in Java, written by "experts") into a higher-level transactional model (which he called Transactional Boosting).

Keith also reminded me of Dave Patterson's talk in the winter, [Computer Architecture is Back: The Berkeley View of the Parallel Computing Research Landscape](http://www.stanford.edu/class/ee380/Abstracts/070131.html).

Related posts: [Concurrent Programming](http://radar.oreilly.com/archives/2007/03/concurrent_prog_1.html), [Threads Considered Harmful]()
