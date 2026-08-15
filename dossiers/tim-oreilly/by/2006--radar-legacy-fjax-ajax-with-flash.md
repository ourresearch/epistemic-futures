---
title: "FJAX:  Ajax with Flash"
person: tim-oreilly
section: by
type: blog-post
year: 2006
date: 2006-06-23
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/archives/2006/06/fjax_ajax_with_flash.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# FJAX:  Ajax with Flash

## Full text

O'Reilly editor Brian Sawyer pointed me to this interesting [webmonkey article on FJAX](http://www.webmonkey.com/06/25/index4a.html), a Flash-powered variant of AJAX.

> "Fjax is an alternative method for doing the kind of Web 2.0 builds that are currently done in Ajax. The advantage is that it does it in a fraction of the size, and requires no code forking to work in the different browsers. It's a streamlined way of doing asynchronous content updates with XML...   
> 
> 
> Fjax uses the Flash Player to load a 1 pixel by 1 pixel transparent SWF to simply get XML from the server. Once it has the XML, it parses it into HTML and then lets JavaScript know it's ready. JavaScript then gets the HTML from Flash and DHTMLs it into the web page — it uses JavaScript to write (X)HTML/CSS onto the page. 
> 
> In the end, Fjax gets XML and delivers HTML. It doesn't collaborate with Ajax. It doesn't need to. It doesn't load data visually into a Flash movie for presentation. It could, but that is not the point. It doesn't generate SWFs or require a server side component. It is its own thing. Oh, and did we mention it's only 65 lines of code? And it's free."

This does sound interesting, since Flash is indeed ubiquitous and powerful. Using the Flash engine to enable portability without requiring too much in the way of changed development practices and tools could be interesting. (Although to be fair, Flash Actionscript is really just Javascript with some extensions, and for many uses, many of the constructs that Flash provides for animation, like the timeline, which was a struggle for many developers, are not needed.)

But does it work? I just went to [the Fjax site](http://www.fjax.net/) (using Firefox on a Mac) and got this message (from vbscript no less): Error parsing XML Data Error parsing XML Data Error parsing XML Data [Note: Jay McDonald writes in the comments below that this was an overload on the server host website, and has been fixed. The site now works fine. In any event, not a problem with fjax. The site is quite snappy now.]

Disclosure: I was formerly a director for Macromedia, but since the acquisition by Adobe, I have no relationship to the company beyond those of a publisher on Adobe technologies.
