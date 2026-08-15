---
title: "Google Gears and Version Control"
person: tim-oreilly
section: by
type: blog-post
year: 2007
date: 2007-07-14
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/archives/2007/07/google_gears_an.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# Google Gears and Version Control

## Full text

I [posted yesterday about the importance of version control](http://radar.oreilly.com/archives/2007/07/why_congress_ne.html). There was another bit I wanted to work into that post, but ultimately decided against. In our backchannel discussion, Nat had pointed to a fascinating post last month by Dare Obasanjo about [sync being left out of Google Gears](http://www.25hoursaday.com/weblog/2007/06/06/GoogleGearsReplacingOneProblemWithAnother.aspx): 

> I don't consider myself some sort of expert on data synchronization protocols but it seems to me that there is a lot more to figuring out a data synchronization strategy than whether it should be done based on user action or automatically in the background without user intervention. It seems that there would be all sorts of decisions around consistency models and single vs. multi-master designs that developers would have to make as well. And that's just for a fairly straightforward application like Google Reader. Can you imagine what it would be like to use Google Gears to replicate the functionality of Outlook in the offline mode of Gmail or to make Google Docs & Spreadsheets behave properly when presented with conflicting versions of a document or spreadsheet because the user updated it from the Web and in offline mode? 
> 
> It seems that without providing data synchronization out of the box, Google Gears leaves the most difficult and cumbersome aspect of building a disconnected Web app up to application developers.

Karl Fogel replied: 

> Yes, this has relevance to distributed/decentralized version control systems -- though VC systems tend to both have a narrower range of synchronization-requiring scenarios, and to be more conservative about the promises they make to the user regarding the degree to which synchronization can be automated. But it's still basically the same problem: objects that start out as identical copies, then slowly drift apart in isolation, and then need to be reconciled. 
> 
> "Data synchronization is hard; let's go shopping!"

Unfortunately, going shopping is not an option. I like Linus' thinking (referred to yesterday) about the importance of distributed version control with branching and merging. Solving this problem seems very important to me -- and solving it in a way that provides this kind of synchronization as a service -- what Dare was so disappointed to find missing in [Google Gears](http://code.google.com/apis/gears/). 

This is also relevant to the discussion of open source and web 2.0. A new open source version control package -- whether subversion or git -- is still targeted at the old model of producing binary software. Can you imagine version control as a service? Now that would be cool.
