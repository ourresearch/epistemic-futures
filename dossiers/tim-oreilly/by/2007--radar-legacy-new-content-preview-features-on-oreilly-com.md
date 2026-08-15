---
title: "New Content Preview Features on oreilly.com"
person: tim-oreilly
section: by
type: blog-post
year: 2007
date: 2007-04-06
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/archives/2007/04/new_content_pre_1.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# New Content Preview Features on oreilly.com

## Full text

Allen Noren, our director of online marketing, just let us know that the [Copyright Clearance Center](http://www.copyright.com)'s RightsLink feature is now live on oreilly.com. While this feature is designed to make it easier for us to handle reprint requests via user self-service, the same tools we used to provide the preview for RightsLink purchasers also makes it easy for our readers to browse much more of our books online before deciding to make a purchase.

Allen wrote a bit about the CCC and RightsLink on an internal O'Reilly mailing list:

> The CCC was established by the Library of Congress to facilitate the clearance of copyrighted content, and publishers sign up for their services. The CCC has a website, [copyright.com](http://www.copyright.com), where anyone interested in reusing publisher's content can clear and pay to reuse material. It's a 20th century process, however, where someone has to have our content in-hand, know that the CCC exists and that they have a website, and that copyright can be cleared. RightsLink is different because it's implemented on our site. For example, go to any one of the following books' online Table of Contents page 
> 
> [CSS: The Missing Manual](http://www.oreilly.com/catalog/csstmm/toc.html)  
> [The Rails Cookbook](http://www.oreilly.com/catalog/9780596527310/toc.html)  
> [Learning Perl](http://www.oreilly.com/catalog/learnperl4/toc.html)
> 
> and you'll see that, along with the ability to purchase a book in print or pdf (if that's available), or view it on Safari, a customer can now purchase the rights to reuse chapters, recipes, hacks, and images. A typical customer for this will be corporations, teachers, magazines, and websites that want to reuse our content on their intranets, newsletters, print and online publications, and course packs. 

The Table of Contents link on the catalog page for each book now lets you preview top level sections in each chapter, as shown in the screen shot below:

[](http://radar.oreilly.com/csstdg.html)

The previewing ability we've added is driven by an internal application we refer to as the content "deli", an Xquery database that allows us to serve up all our content in alternate forms. The RightLink preview implementation is the first of many new features we expect to be rolling out now that we have this infrastructure in place. (It's a generalization of the tools we built for [SafariU](http://www.safariu.com) last year.) Stay tuned!

P.S. This is a good chance to give some public props to the folks at O'Reilly (in addition to Allen) who made this happen. Allen wrote: "Many people helped with this project. Laura Baldwin [our CFO/COO] backed it from the crazy idea stage. CJ Rayhill [our CIO] and Laurie Petrycki [publisher for our Missing Manuals, Head First, and Dynamic Media publishing programs] helped with the early pricing models. Pascal Honscher helped define and drive the implementation, and came up with a number of innovative processes that surprised the CCC folks. Charles Greer, Ben Bangert, and Jeff Boyd harnessed the power of the MarkLogic database to generate the dynamic TOC pages. John Haren, Eric Parker, Laura Adair, Julie Delany, and Mace Bergmann were instrumental in making this work programatically." I'll also add Ryan Grimm and Andy Bruno, as well as Jason Hunter at MarkLogic, who developed a lot of the original SafariU code that made this possible. Nice work, guys.
