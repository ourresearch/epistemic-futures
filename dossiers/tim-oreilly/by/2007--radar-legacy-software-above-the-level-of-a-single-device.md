---
title: "Software Above the Level of a Single Device"
person: tim-oreilly
section: by
type: blog-post
year: 2007
date: 2007-11-28
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/archives/2007/11/software_above_single_device.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# Software Above the Level of a Single Device

## Full text

In February of 2003, [Dave Stutz](http://www.synthesist.net/), who had been one of Microsoft's leading internal open source advocates, wrote a remarkable parting letter to the company, entitled [Advice to Microsoft regarding commodity software](http://www.synthesist.net/writing/onleavingms.html). This essay made an indelible impression on me, and led me to write a talk (and later a paper) called [The Open Source Paradigm Shift](http://tim.oreilly.com/articles/paradigmshift_0504.html), which put together Dave's thoughts on software commoditization with my conviction that one of the unexpected but inevitable outcomes of open source software was that it was driving a the emergence of a new, proprietary platform layer on the web. The fuller explication of the nature of that platform was, of course, the talk and paper [What is Web 2.0?](http://www.oreillynet.com/go/web2). 

Anyone interested in the evolution of the computer industry should re-read Dave's letter from time to time. But in this post, I want to bring specific attention to Dave's closing paragraphs, and in particular, to the line I've highlighted in italics below: 

> Why be distracted into looking backwards by the commodity cloners of open source? Useful as cloning may be for price-sensitive consumers, the commodity business is low-margin and high-risk. There is a new frontier, where software "collectives" are being built with ad hoc protocols and with clustered devices. Robotics and automation of all sorts is exposing a demand for sophisticated new ways of thinking. Consumers have an unslakable thirst for new forms of entertainment. And hardware vendors continue to push towards architectures that will fundamentally change the way that software is built by introducing fine-grained concurrency that simply cannot be ignored. There is no clear consensus on systems or application models for these areas. _Useful software written above the level of the single device will command high margins for a long time to come._
> 
> Stop looking over your shoulder and invent something! 

I made "software above the level of a single device" one of the key principles in my Web 2.0 talks. Nonetheless it seems to me that this is still one of the principles that is not properly understood, or is understood only in the most obvious sense. 

And that obvious sense is this: by definition, every web application is software above the level of a single device. At minimum, these applications use a client on a local computer and one or more server computers. In the case of applications like Google, the server end may consist of hundreds of thousands of machines, and, of course, the data held on those servers is gathered from literally hundreds of millions of other computers. So clearly, this is software above the level of a single device. 

Yet, in my Web 2.0 talks, I always use Apple's iTunes as my paradigmatic example for this principle. Why? 

It seems to me that iTunes highlights the potential of a new application model beyond the web browser, where the personal computer acts as a control and management station for a handheld device, mediating and managing that device's access both to personal computer data and the internet cloud. Other Apple applications have some of the same characteristics (for example, iPhoto manages your camera and access to various .Mac-based photo services), but it's in iTunes, where Apple controls all levels of the user experience, that you really see the power of the model. 

Imagine, for a moment, if your smart phone worked like your iPod? (Well, actually, now it is starting to do so, since for many of us, our iPod has become our smart phone. But I'm talking about other manufacturers' phones.) Instead of working through tiny, confusing configuration menus on the phone, you'd have a much richer management console on your PC. You'd have the [Address Book 2.0](http://radar.oreilly.com/archives/2007/02/social_network_1.html) that I've been looking for, with direct [lookup into your cell carrier's call history database](http://radar.oreilly.com/archives/2007/05/what_would_goog.html) as well as various directory services. You could annotate that data on your phone still, but how much more easily could you manage it on your PC? 

I'm surprised to see how few companies have really searched out the possibilities of this three-tier model, with the PC providing management and configuration services (as well as useful standalone services on the PC itself), enabling much cleaner, more powerful services on the portable device, and full access to various kinds of internet services. 

As the iPod/iTunes combination has morphed into the iPhone/iTunes combination, we can begin to see the real power of this approach. Because of course, it isn't just about managing music. It's about managing all of my digital assets, and making them available to me where I want them. And those assets are increasingly "above the level of a single device." 

Even Apple still has a long way to go, of course: 

  * There really ought to be an iPhone app (or iPhone functionality in iTunes) that would allow me to make VoIP calls from the PC. (Maybe Apple could take Skype off ebay's hands :-) 

  * Apple hasn't really embraced the address book as a first class application. There's an enormous opportunity to turn our address book into a personal CRM system, pulling in additional data from the phone company's databases, from internet social networking services, and from other communication applications like IM and email. 

  * iTunes needs to work together more seamlessly with other applications like iPhoto, and the internet-enabled address book I keep hoping for. Right now, when you sync your phone, you have both applications open up, competing for your attention. As more data needs to be synced to the phone, you don't want this to turn into a cacophony. 

But I don't want you to think that this is a post about iTunes per se. It's about the _idea_ of iTunes, and how it could be applied to build new and powerful applications. My GPS (which will eventually be and integral part of my phone and camera) should sync with my PC _and_ and with Google maps, and supply a management application with which I can annotate my travels, find online photos of places I'm going so I know what I'm looking for, easily forward directions to other people, view my photos by location, generate mileage calculations for expense reports, and perhaps even build location-based games. A lot of these things would be possible on a portable device (and in fact, the [Dash shows](http://radar.oreilly.com/archives/2007/10/dash_web2summit_openmoko.html) just how powerful an internet-connected GPS can be), but the interfaces become richer, and the possibilities greater, when you are not limited to the device itself for data input, management and configuration. 

Incidentally, the [Chumby](http://www.chumby.com) (in which [O'Reilly AlphaTech Ventures](http://www.oatv.com) is an investor) uses another version of this device management model. Rather than a standalone PC client for managing the Chumby, you use the web browser and your account at chumby.com. But the concept is the same. Rather than building complex configuration menus into the device itself, you manage the data channels that will be streamed to the device in a separate application, with a much bigger screen and a keyboard for input. 

I can't wait till more device manufacturers realize that you don't need to build the application for managing a device into the device itself. The game is richer than that. Let the device do what it does best; let the internet do what it does; and use the PC to help manage the relationship between the two.
