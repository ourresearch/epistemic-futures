---
title: "Concurrent Programming:  Erlang, Haskell...and XSLT"
person: tim-oreilly
section: by
type: blog-post
year: 2007
date: 2007-03-03
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/archives/2007/03/concurrent_prog_1.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# Concurrent Programming:  Erlang, Haskell...and XSLT

## Full text

Dave Thomas' [announcement on ruby-talk](http://groups.google.com/group/comp.lang.ruby/browse_thread/thread/ad3c5d7527c62cce/85da973e24f542a8#85da973e24f542a8) that the [Pragmatic Programmers](http://www.pragmaticprogrammer.com) are about to publish [a book on Erlang](http://www.pragmaticprogrammer.com/titles/jaerlang/) sparked some interesting back-chatter on the O'Reilly editors' list. But first, Dave's announcement:

> I love Ruby--I've done all my serious (and most of my not-so-serious) work in Ruby since 2000. 
> 
> But that doesn't mean that I think it's the only solution--the universal language. There are always going to be areas where other tools excel.
> 
> One of those areas is concurrent programming. As the world moves to multi-core processors, and as we start to write applications distributed across intra- and internets, we need to find better ways to exploit all this extra power. If you've ever tried to write concurrent programs in Java, or even Ruby, you know the challenges.
> 
> Erlang is designed from the ground up to help programmers create highly concurrently (read thousands or processes), highly reliable (read 99.99999% uptime) applications. It's a real world language--it is used to write telephone switches, banking applications, trading systems...you name it.
> 
> I like it for that reason. I also like it because it's different--very different. It makes me think about problems in a totally different way.
> 
> We were lucky to get Joe Armstrong, one of the inventors of Erlang, to write our latest beta book, [Programming Erlang](http://www.pragmaticprogrammer.com/titles/jaerlang/).
> 
> The book isn't being officially announced until next week, but I thought the Ruby community might appreciate an early look.

First off, I'm really glad the Prags are doing this. I totally agree with Dave about the future importance of concurrent programming. There was some debate over whether Erlang was going to be the language of choice for this kind of application. But whether it's something old, or something new, the fundamental paradigms of programming are going to be challenged as systems and processors scale up. (See Nat's recent post, [Threads Considered Harmful](http://radar.oreilly.com/archives/2007/01/threads_conside.html).)

[Alexaholic shows](http://www.alexaholic.com/haskell.org+erlang.org+ruby-lang.org) the increase of traffic to erlang.org and haskell.org over the past few years, with ruby-lang.org included for comparison:

[](http://radar.oreilly.com/erlanghaskellruby.html)

Keith Fahlgren wrote: 

> I think the first publisher to get somebody both involved enough to know what the latest and greatest is but not writing for an academic audience should be able to capture this nascent (but, I'm sure growing) market.

What was also interesting was the way the conversation segued over to XSLT and XQuery, both of which our tools group uses heavily. Andrew Savikas wrote about the difficulty of getting used to the programming model of these languages:

> And of course, XSLT and XQuery are both functional languages -- I suspect the former is in heavier use than Lisp, Scheme, and Haskell combined. I think one of the reasons XSLT gets a bad rap is because developers try to use it like a procedural language, and discover (surprise!) that lots of for-each and if/then choose statements are annoying and clunky and maddening to debug -- not to mention amounting to fighting the recursive descent parsing built into the language, which is what makes it so powerful to begin with. Surrendering to declarative xpath matches carries its own gotchas, but is sufficently rewarding (and with the right vim bindings, the verbosity argument is a non-starter -- many complete stylesheets I've written involve maybe 20-30 keystrokes.) 
> 
> But as Keith points out, most of the coverage of functional programming is _way_ too academic to be useful. Without an undergrad Scheme class, I feel like I'm feeling my way through the dark trying to grok the functional way to do things in XSLT and XQuery. Case in point, there's a crazy (in a good way) chapter in [XSLT Cookbook](http://www.oreilly.com/catalog/xsltckbk/) about using XSLT for "traditional" functional programming: I've read that chapter at least 5 different times in the past 2 years, and still have no idea how to apply that stuff.
