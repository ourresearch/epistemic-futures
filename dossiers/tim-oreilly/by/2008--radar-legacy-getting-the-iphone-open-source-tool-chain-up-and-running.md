---
title: "Getting the iPhone Open Source Tool Chain Up and Running"
person: tim-oreilly
section: by
type: blog-post
year: 2008
date: 2008-04-02
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/archives/2008/04/getting-the-iphone-open-source.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# Getting the iPhone Open Source Tool Chain Up and Running

## Full text

Tomorrow at 10 am pacific time, oreilly.com is hosting a free webcast with [Jonathan A. Zdziarski](http://www.oreillynet.com/pub/au/1861), one of the original hackers of the iPhone and author of [iPhone Open Application Development](http://www.oreilly.com/catalog/9780596518554/). From the announcement: 

> Jonathan will demonstrate how you can use the iPhone open source tool chain to design third-party software that will run on on both today's iPhones, and on iPhones that will soon be running Apple's next version of firmware based on the official SDK. Jonathan will demonstrate on a Mac running Leopard. 
> 
> Introducing Jonathan will be Brian Jepson, executive editor for Make Magazine's Make:Books series, co-author of Mac OS X Tiger for Unix Geeks and a number of other geeky books, and iPhone hacker at large. 
> 
> This is your opportunity to hear expert advice on building applications for the iPhone and ask questions of the experts themselves. 
> 
> [Attendance is limited, so register now](http://oreilly.com/go/webcast-iphone). We'll send you a reminder before the webcast. 
> 
> Date: Thursday, April 3 at 10am PDT (17:00 GMT)   
>  Cost: Free   
>  Duration: 30-45 minutes   
>  Meeting link: [oreilly.com/go/webcast-iphone](http://oreilly.com/go/webcast-iphone)   
>  Teleconference dial-in:   
>  (select the number that is closest to your location)   
>  East Coast US: +1 617 231-0350 and pin 8136507   
>  West Coast US: +1 213-455-0500 and pin 8136507 

Some people might wonder why we published a book on the open source toolchain when an official SDK has already been announced. (I wondered that myself :-) We started the book before Apple had learned from the first hackers that people wanted more out of the phone and announced the open API. But why didn't we just hold off on publishing it, modify it for the official API, and release it when the time comes (supposedly sometime in June) when the official API is open for business? The answer is threefold. 

  1. We believe strongly that hackers mark off the natural paths that official developer programs later pave over and make safe for the less adventurous. Smart companies know this, and pay attention to their hackers. (Google Maps is a great case in point. It became the mapping platform of choice because, rather than shutting down the early mashup hackers, it quickly figured how to pour fuel on the fire that they'd started.) We think that despite the official disapproval, Apple knows that the hacker interest in the iPhone is a great boost to their program and their goals. (Witness the fact that the Apple store in Cambridge MA [allowed Jonathan to present on open iPhone development](http://www.xconomy.com/2008/03/25/jail-breaking-iphones-and-other-tales-from-the-apple-store/) in a meeting at the store.) 

  2. The open API has a great deal of overlap with the official API. So getting up and running with the open toolchain will help developers get a head start. But it's also more powerful than the official toolchain, and will let developers continue to push Apple in interesting new directions. Jonathan [wrote](<a): 

> With the introduction of the Apple SDK, developers gauged its functionality based on a comparison to the unofficial, open source SDK released last August. In the process of building this custom, open source compiler for the iPhone, the development community exposed the many low-level APIs (application programming interfaces) available on the device. Using tools such as class-dump, nm, and just plain old trial-and-error gave developers access to the full breadth of functionality available deep within the iPhone's frameworks. It was used to write applications that could look and act just like Apple's preloaded software, so when Apple announced that their SDK was "the same set of tools," many expected that it would look and feel like the open tool chain. Very few had anticipated the many restrictions they've come to find in the official SDK. While roughly 75% of the two SDKs do overlap, the remaining 25% has shown to be very restrictive, removing the developer's ability to do "the real fun stuff" with their application.

  3. The demand was there. The number of slots in the official API program is far smaller than the apparent demand. We published the book, and it sold out immediately, indicating that we were right. We do plan to update the book with information about the official API as soon as the Apple NDA is lifted, but for now, we are eager to fuel the fire, since we believe that the iPhone is one of the most important new platforms in the market today, and one that developers should be exploring as deeply (and as soon) as possible. 

See also [Jonathan's article on the O'Reilly Network about open API development for the iPhone](http://www.onlamp.com/pub/a/onlamp/2008/03/25/the-apple-sdk-apis-apple-didnt-want-you-to-know-about.html) for more information about the difference between the two APIs, and why developers need to know about both. We're also planning to have a strong [open mobile development track at OScon](http://en.oreilly.com/oscon2008/public/content/open-mobile-exchange).
