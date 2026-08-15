---
title: "Web 2.0 and Cloud Computing"
person: tim-oreilly
section: by
type: blog-post
year: 2008
date: 2008-10-26
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/2008/10/web-20-and-cloud-computing.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# Web 2.0 and Cloud Computing

## Full text

A couple of months ago, Hugh Macleod [created a bit of buzz](http://technorati.com/posts/lv3vwaZ9hbuGSZx_jQseIqaVSlj29LQGjWyRkNoZ4b0%3D?reactions) with his blog post [The Cloud's Best Kept Secret](http://www.gapingvoid.com/Moveable_Type/archives/004638.html). Hugh's argument: that cloud computing will lead to a huge monopoly. Of course, a couple of weeks ago, Larry Ellison [made the opposite point](http://www.forbes.com/2008/10/10/ellison-cloud-computing-tech-enter-cx_wt_1010oracle.html), arguing that salesforce.com is "barely profitable", and that no one will make much money in cloud computing. 

In this post, I'm going to explain why Ellison is right, and yet, for the strategic future of Oracle, he is dangerously wrong. 

First, let's take a look at Hugh Macleod's argument: 

> ...nobody seems to be talking about Power Laws. Nobody's saying that one day a single company may possibly emerge to dominate The Cloud, the way Google came to dominate Search, the way Microsoft came to dominate Software. 
> 
> Monopoly issues aside, could you imagine such a company? We wouldn't be talking about a multi-billion dollar business like today's Microsoft or Google. We're talking about something that could feasibly dwarf them. We're potentially talking about a multi-trillion dollar company. Possibly the largest company to have ever existed. 
> 
> I imagine many of my friends who work for the aforementioned companies know all about this, and know how VAST the stakes are. 
> 
> Windows vs Apple? Who cares? Kid's stuff. There's a much bigger game going on... And for some reason, its utter enormity seems to be a very well-kept secret, at least to non-combatants like myself.

The problem with this analysis is that it doesn't take into account what causes power laws in online activity. Understanding the dynamics of increasing returns on the web is the essence of what I called Web 2.0. Ultimately, on the network, applications win if they _get better the more people use them_. As I [pointed out back in 2005](http://www.oreillynet.com/go/web2</a), Google, Amazon, ebay, craigslist, wikipedia, and all other other Web 2.0 superstar applications have this in common. 

Cloud computing, at least in the sense that Hugh seems to be using the term, as a synonym for the infrastructure level of the cloud as best exemplified by Amazon S3 and EC2, doesn't have this kind of dynamic. (More on different types of cloud computing later.) 

Of course, it is true that the bigger players will have economies of scale in the cost of equipment, and [especially in the cost of power](http://radar.oreilly.com/2006/07/operations-the-new-secret-sauc.html), that are not available to smaller players. But there are quite a few big players -- Google, Microsoft, Amazon -- to name a few, that are already at that scale, with or without a cloud computing play. What's more, economies of scale are not the same as increasing returns from user network effects. They may be characteristic of a commoditizing marketplace that does not actually give outsize economic leverage to the winners. 

I can't vouch for the authenticity of the following remark, since I heard it secondhand, but it was from a thoughtful, informed source: Jeff Bezos is reported to have said that he welcomes cloud competition from Google and Microsoft, because they'll subsidize their cloud services with profits from other part of their business, while Amazon will always have to make it pay. "We're good at commodity businesses," Jeff is reported to have said, and the facts bear him out. 

If cloud computing is a commodity business, then the outsize profits that Hugh envisioned are not going to be there. This is a business that will be huge, but it may be more similar to the web hosting and ISP markets, which are also huge, but not hugely profitable. (See [Rackspace's numbers](http://finance.yahoo.com/q/ks?s=RAX) for a taste.) 

But because one of my goals at Radar is to help people think about the future, I wanted to spend some time on the possible futures and strategies that could turn cloud computing into the kind of massive monopoly that Hugh envisioned. 

**Types of Cloud Computing**

Since "cloud" seems to mean a lot of different things, let me start with some definitions of what I see as three very distinct types of cloud computing: 

  1. **Utility computing.** Amazon's success in providing virtual machine instances, storage, and computation at pay-as-you-go utility pricing was the breakthrough in this category, and now everyone wants to play. Developers, not end-users, are the target of this kind of cloud computing. 

This is the layer at which I don't presently see any strong network effect benefits (yet). Other than a rise in Amazon's commitment to the business, neither early adopter [Smugmug](http://www.smugmug.com) nor any of its users get any benefit from the fact that thousands of other application developers have their work now hosted on AWS. If anything, they may be competing for the same resources. 

That being said, to the extent that developers become committed to the platform, there is the possibility of the kind of developer ecosystem advantages that once accrued to Microsoft. More developers have the skills to build AWS applications, so more talent is available. But take note: Microsoft took charge of this developer ecosystem by building tools that both created a revenue stream for Microsoft and made developers more reliant on them. In addition, they built a deep -- very deep -- well of complex APIs that bound developers ever-tighter to their platform. 

So far, most of the tools and higher level APIs for AWS are being developed by third-parties. In the offerings of companies like [Heroku](http://www.heroku.com), [Rightscale](http://www.rightscale.com), and [EngineYard](http://www.engineyard.com) (not based on AWS, but on their own hosting platform, while sharing the RoR approach to managing cloud infrastructure), we see the beginnings of one significant toolchain. And you can already see that many of these companies are building into their promise the idea of independence from any cloud infrastructure vendor. 

In short, if Amazon intends to gain lock-in and true competitive advantage (other than the aforementioned advantage of being the low-cost provider), expect to see them roll out their own more advanced APIs and developer tools, or acquire promising startups building such tools. Alternatively, if current trends continue, I expect to see Amazon as a kind of foundation for a Linux-like aggregation of applications, tools and services not controlled by Amazon, rather than for a Microsoft Windows-like API and tools play. There will be many providers of commodity infrastructure, and a constellation of competing, but largely compatible, tools vendors. Given the momentum towards [open source and cloud computing](http://radar.oreilly.com/2008/07/open-source-and-cloud-computing.html), this is a likely future. 

  2. **Platform as a Service**. One step up from pure utility computing are platforms like Google [AppEngine](http://code.google.com/appengine/) and Salesforce's [force.com](http://www.force.com), which hide machine instances behind higher-level APIs. Porting an application from one of these platforms to another is more like porting from Mac to Windows than from one Linux distribution to another. 

The key question at this level remains: are there advantages to developers in one of these platforms from other developers being on the same platform? force.com seems to me to have some ecosystem benefits, which means that the more developers are there, the better it is for both Salesforce and other application developers. I don't see that with AppEngine. What's more, many of the applications being deployed there seem trivial compared to the substantial applications being deployed on the Amazon and force.com platforms. One question is whether that's because developers are afraid of Google, or because the APIs that Google has provided don't give enough control and ownership for serious applications. I'd love your thoughts on this subject. 

  3. **Cloud-based end-user applications.** Any web application is a cloud application in the sense that it resides in the cloud. Google, Amazon, Facebook, twitter, flickr, and virtually every other Web 2.0 application is a cloud application in this sense. However, it seems to me that people use the term "cloud" more specifically in describing web applications that were formerly delivered locally on a PC, like spreadsheets, word processing, databases, and even email. Thus even though they may reside on the same server farm, people tend to think of gmail or Google docs and spreadsheets as "cloud applications" in a way that they don't think of Google search or Google maps. 

This common usage points up a meaningful difference: people tend to think differently about cloud applications when they host individual user data. The prospect of "my" data disappearing or being unavailable is far more alarming than, for example, the disappearance of a service that merely hosts an aggregated view of data that is available elsewhere (say Yahoo! search or Microsoft live maps.) And that, of course, points us squarely back into the center of the Web 2.0 proposition: that users add value to the application by their use of it. Take that away, and you're a step back in the direction of commodity computing. 

Ideally, the user's data becomes more valuable because it is in the same space as other users' data. This is why a listing on craigslist or ebay is more powerful than a listing on an individual blog, why a listing on amazon is more powerful than a listing on Joe's bookstore, why a listing on the first results page of Google's search engine, or an ad placed into the Google ad auction, is more valuable than similar placement on Microsoft or Yahoo!. This is also why every social network is competing to build its own social graph rather than [relying on a shared social graph utility](http://radar.oreilly.com/2008/08/social-networking-for-books.html). 

This top level of cloud computing definitely has network effects. If I had to place a bet, it would be that the application-level developer ecosystems eventually work their way back down the stack towards the infrastructure level, and the two meet in the middle. In fact, you can argue that that's what force.com has already done, and thus represents the shape of things. It's a platform I have a strong feeling I (and anyone else interested in the evolution of the cloud platform) ought to be paying more attention to. 

**The Law of Conservation of Attractive Profits**

A lot of my [thinking about web 2.0](http://www.oreillynet.com/go/web2) grew directly out of my thinking about open source. My argument in [The Open Source Paradigm Shift](http://tim.oreilly.com/articles/paradigmshift_0504.html) was that what we learned from the history of the IBM personal computer -- a commodity platform built from off-the-shelf parts -- was that it drained value out of the hardware ecosystem, turning it into a low-margin business. But profits didn't go away. Instead, through something that Clayton Christensen calls "the law of conservation of attractive profits," value migrated elsewhere, from hardware to software, from IBM to Microsoft. Christensen: 

> When attractive profits disappear at one stage in the value chain because a product becomes modular and commoditized, the opportunity to earn attractive profits with proprietary products will usually emerge at an adjacent stage.

I believe strongly that open source and open internet standards are doing the same to traditional software. And value is migrating to a new kind of layer, which we now call Web 2.0, which consists of applications driven not just by software but by network-effects databases driven by explicit or implicit user contribution. 

So when Larry Ellison says that cloud computing and open source won't produce many hugely profitable companies, he's right, but only if you look at the pure software layer. This is a lot like saying that the PC wouldn't produce many hugely profitable companies, and looking only at hardware vendors! First Microsoft, and now Google give the lie to Ellison's analysis. The big winners are those who best grasp the rules of the new platform. 

So here's the real trick: cloud computing is real. Everything is moving into the cloud, in whole or in part. The utility layer of cloud computing will be just that, a utility, without outsized profits. 

But the cloud platform, like the software platform before it, has new rules for competitive advantage. And chief among those advantages are those that we've identified as "Web 2.0", the design of systems that harness network effects to get better the more people use them. 

If Oracle isn't playing that game, they will one day be doomed to irrelevance. Perhaps, like hardware giants of the past - Compaq, say - they will be absorbed by a bigger company. Or perhaps, like Unisys, they will linger on in specialized markets, too big to go away but no longer on the cutting edge of anything. Or they will understand that it's not the database _software_ that matters, but the data that it holds, and the services that can be built against that data. 

The company that creates the right _platform_ for network effects in data may well achieve the scale that Hugh Macleod envisioned. 

P.S. I will be doing two panels on cloud computing at the [Web 2.0 Summit](http://en.oreilly.com/web2008/public/content/home) in San Francisco the week after next, one on the application layer, and one on the infrastructure layer. Panelists include Paul Maritz (CEO of VMware, who, by the way _totally gets_ what I'm talking about here), Russ Daniels (CTO for cloud services at HP), Padmasree Warrior (CTO at Cisco), the inimitable Marc Benioff of Salesforce.com, Kevin Lynch, CTO of Adobe, and Dave Girouard, who is in charge of Google Apps for the Enterprise. Should be some interesting conversations on the subjects raised in this post!
