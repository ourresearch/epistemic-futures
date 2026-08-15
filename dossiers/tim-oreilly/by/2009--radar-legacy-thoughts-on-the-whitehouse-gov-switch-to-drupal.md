---
title: "Thoughts on the Whitehouse.gov switch to Drupal"
person: tim-oreilly
section: by
type: blog-post
year: 2009
date: 2009-10-25
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/2009/10/whitehouse-switch-drupal-opensource.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# Thoughts on the Whitehouse.gov switch to Drupal

## Full text

Yesterday, the new media team at the White House announced via the Associated Press that [whitehouse.gov is now running on Drupal](http://www.huffingtonpost.com/huff-wires/20091024/us-obama-web-site/), the open source content management system. That Drupal implementation is in turn running on a Red Hat Linux system with Apache, MySQL and the rest of the [LAMP stack](http://en.wikipedia.org/wiki/LAMP_\(solution_stack\)). [Apache Solr](http://lucene.apache.org/solr/) is the new White House search engine. 

This move is obviously a big win for open source. As John Scott of [Open Source for America](http://opensourceforamerica.org/) (a group advocating open source adoption by government, to which I am an advisor) noted in an email to me: "This is great news not only for the use of open source software, but the validation of the open source development model. The White House's adoption of community-based software provides a great example for the rest of the government to follow." 

John is right. While open source is already widespread throughout the government, its adoption by the White House will almost certainly give permission for much wider uptake. 

Particularly telling are the reasons that the White House made the switch. According to the AP article: 

> White House officials described the change as similar to rebuilding the foundation of a building without changing the street-level appearance of the facade. It was expected to make the White House site more secure - and the same could be true for other administration sites in the future.... 
> 
> Having the public write code may seem like a security risk, but it's just the opposite, experts inside and outside the government argued. Because programmers collaborate to find errors or opportunities to exploit Web code, the final product is therefore more secure. 

More than just security, though, the White House saw the opportunity to increase their flexibility. [Drupal has a huge library of user-contributed modules](http://drupal.org/project/Modules) that will provide functionality the White House can use to expand its social media capabilities, with everything from super-scalable live chats to multi-lingual support. In many ways, this is the complement to the [Government as Platform](http://www.techcrunch.com/2009/09/04/gov-20-its-all-about-the-platform/) mantra I've been chanting in Washington. When you build a vibrant, extensible platform, others add value to the foundation you establish; when you join such a platform, you get the benefit of all those features you didn't have to develop yourself. 

Of course, it's easy to imagine that the use of open source software will slash the government's IT budget. After all, this software is freely downloadable. I have a feeling it's quite a bit more complicated than that. 

First off, government has a huge number of special requirements (remember [the flap over President Obama's blackberry](http://www.google.com/search?client=safari&rls=en&q=president+obama's+blackberry&ie=UTF-8&oe=UTF-8)?) Second, don't underestimate the difficulty of doing business in Washington. Procurement is done through a complex ballet understood by few open source companies. Third, a big IT deployment like this requires coordination between many companies, each providing a piece of the puzzle. [According to techpresident.com](http://techpresident.com/blog-entry/whitehousegov-goes-drupal), no fewer than five firms were involved in the switch: prime contractor [General Dynamics Information Systems](http://www.gdit.com/), Drupal specialists [Phase 2](http://www.phase2technology.com/) and [Acquia](http://acquia.com), hosting provider [Terremark](http://www.terremark.com/), and CDN-supplier [Akamai](http://akamai.com). (Disclosure: [O'Reilly AlphaTech Ventures](http://oatv.com) is an investor in Acquia.) 

The special nature of the government marketplace is one of the reasons why I launched the [Gov 2.0 Expo](http://gov2expo.com), which will be held in Washington DC next May. There are huge opportunities for open source, web 2.0, and new media companies in government, but there are also challenges reaching that market. One of my goals for the event is to increase the visibility of cutting edge technology firms not just to government agencies, but also to the prime contractors who are putting together these complex procurements. 

The net-net is that I suspect that simply using open source software won't slash government IT budgets, at least not right away. What it will do is increase the amount of value we get for our money and the speed with which new technology can be adopted. Features that would have cost millions of dollars and years of development to add will now be rolled into the scope of current contracts. 

It's also important to realize that _using_ open source is very different from _contributing_ to open source. Despite the exaggerated claims in the AP story, that "the programming language is written in public view, available for public use and able for people to edit", the White House has not yet released any of the modifications they made to Drupal or its operating environment back to the open source community. The source code for Drupal (and the rest of the LAMP stack) is indeed available, but the modifications that were made to meet government security, scalability, and hosting requirements have not yet been shared. In my conversations with the new media team at the White House, it is clear that they are exploring this option. 

Giving modifications back to the Drupal community is the next breakthrough announcement that I'll be looking for. 

Releasing code is more than just being a good open source community citizen, though. Code sharing is a major cost-saving opportunity for government. There are countless government agencies at the federal level, not to mention at the state and local level, that perform similar functions. Yet each of them does its own development, driving up costs. Federal CIO Vivek Kundra has made a great step forward in web services by creating [data.gov](http://data.gov). I'm eager to see an analogous code.gov portal for government agencies to share their open source software code.
