---
title: "The State of the Internet Operating System"
person: tim-oreilly
section: by
type: blog-post
year: 2010
date: 2010-03-29
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/2010/03/state-of-internet-operating-system.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# The State of the Internet Operating System

## Full text

_I've been talking for years about "[the internet operating system](http://www.google.com/search?q=internet+operating+system+tim+o'reilly&ie=UTF-8&oe=UTF-8)", but I realized I've never written an extended post to define what I think it is, where it is going, and the choices we face. This is that missing post. Here you will see the underlying beliefs about the future that are guiding my [publishing program](http://www.oreilly.com) as well as the rationale behind conferences I organize like the [Web 2.0 Summit](http://web2summit.com) and [Web 2.0 Expo](http://web2expo.com), the [Where 2.0 Conference](http://en.oreilly.com/where20), and even the [Gov 2.0 Summit](http://gov2summit.com) and [Gov 2.0 Expo](http://gov2expo.com). _

Ask yourself for a moment, what is the operating system of a Google or Bing search? What is the operating system of a mobile phone call? What is the operating system of maps and directions on your phone? What is the operating system of a tweet? 

On a standalone computer, operating systems like Windows, Mac OS X, and Linux manage the machine's resources, making it possible for applications to focus on the job they do for the user. But many of the activities that are most important to us today take place in a mysterious space _between_ individual machines. Most people take for granted that these things just work, and complain when the daily miracle of instantaneous communications and access to information breaks down for even a moment. 

But peel back the covers and remember that there is an enormous, worldwide technical infrastructure that is enabling the always-on future that we rush thoughtlessly towards. 

When you type a search query into Google, the resources on your local computer - the keyboard where you type your query, the screen that displays the results, the networking hardware and software that connects your computer to the network, the browser that formats and forwards your request to Google's servers - play only a small role. What's more, they don't really matter much to the operation of the search - you can type your search terms into a browser on a Windows, Mac, or Linux machine, or into a smartphone running Symbian, or PalmOS, the Mac OS, Android, Windows Mobile, or some other phone operating system. 

The resources that are critical to this operation are mostly somewhere else: in Google's massive server farms, where proprietary Google software farms out your request (one of millions of simultaneous requests) to some subset of Google's servers, where proprietary Google software processes a massive index to return your results in milliseconds. 

Then there's the IP routing software on each system between you and Google's data center (you didn't think you were directly connected to Google did you?), the majority of it running on Cisco equipment; the mostly open source Domain Name System, a network of lookup servers that not only allowed your computer to connect to google.com in the first place (rather than typing an IP address like 74.125.19.106), but also steps in to help your computer access whatever system out there across the net holds the web pages you are ultimately looking for; the protocols of the web itself, which allow browsers on client computers running any local operating system (perhaps we'd better call it a [bag of device drivers](http://www.google.com/search?q=windows+%22bag+of+device+drivers%22+andreessen&aq=f&aqi=&aql=&oq=&gs_rfai=)) to connect to servers running any other operating system. 

You might argue that Google search is just an application that happens to run on a massive computing cluster, and that at bottom, Linux is still the operating system of that cluster. And that the internet and web stacks are simply a software layer implemented by both your local computer and remote applications like Google. 

But wait. It gets more interesting. Now consider doing that Google search on your phone, using Google's voice search capability. You speak into your phone, and Google's speech recognition service translates the sound of your voice into text, and passes that text on to the search engine - or, on an Android phone, to any other application that chooses to listen. Someone familiar with speech recognition on the PC might think that the translation is happening on the phone, but no, once again, it's happening on Google's servers. But wait. There's more. Google improves the accuracy of its speech recognition by comparing what the speech algorithms think you said with what its search system (think "[Google suggest](http://googleblog.blogspot.com/2009/05/faster-is-better-on-google-suggest.html)") expects you were most likely to say. Then, because your phone knows where you are, Google filters the results to find those most relevant to your location. 

_Your phone knows where you are._ How does it do that? "It's got a GPS receiver," is the facile answer. But if it has a GPS receiver, that means your phone is getting its position information by reaching out to a network of satellites originally put up by the US military. It may also be getting additional information from your mobile carrier that speeds up the GPS location detection. It may instead be using "cell tower triangulation" to measure your distance from the nearest cellular network towers, or even doing a lookup from a database that maps wifi hotspots to GPS coordinates. (These databases have been created by driving every street and noting the location and strength of every Wi-Fi signal.) The iPhone relies on the [Skyhook Wireless](http://www.skyhookwireless.com/) service to perform these lookups; Google has its own equivalent, doubtless created at the same time as it created the imagery for [Google Streetview](http://maps.google.com/help/maps/streetview/). 

But whichever technique is being used, the application is relying on network-available facilities, not just features of your phone itself. And increasingly, it's hard to claim that all of these intertwined features are simply an application, even when they are provided by a single company, like Google. 

Keep following the plot. What mobile app (other than casual games) exists solely on the phone? Virtually every application is a network application, relying on remote services to perform its function. 

Where is the "operating system" in all this? Clearly, it is still evolving. Applications use a hodgepodge of services from multiple different providers to get the information they need. 

But how different is this from PC application development in the early 1980s, when every application provider wrote their own device drivers to support the hodgepodge of disks, ports, keyboards, and screens that comprised the still emerging personal computer ecosystem? Along came Microsoft with an offer that was difficult to refuse: We'll manage the drivers; all application developers have to do is write software that uses the Win32 APIs, and all of the complexity will be abstracted away. 

It was. Few developers write device drivers any more. That is left to device manufacturers, with all the messiness hidden by "operating system vendors" who manage the updates and often provide generic APIs for entire classes of device. Those vendors who took on the pain of managing complexity ended up with a powerful lock-in. They created the context in which applications have worked ever since. 

This is the crux of my argument about the internet operating system. We are once again approaching the point at which the Faustian bargain will be made: simply use our facilities, and the complexity will go away. And much as happened during the 1980s, there is more than one company making that promise. We're entering a modern version of "[the Great Game](http://en.wikipedia.org/wiki/The_Great_Game)", the rivalry to control the narrow passes to the promised future of computing. (John Battelle calls them "[points of control](http://battellemedia.com/archives/2010/03/the_2010_web2_summit_theme_points_of_control)".) This rivalry is seen most acutely in mobile applications that rely on internet services as back-ends. As Nick Bilton of the New York Times described it in [a recent article comparing the Google Nexus One and the iPhone](http://bits.blogs.nytimes.com/2010/01/15/torn-between-two-phones-nexus-one-vs-iphone/): 

> Chad Dickerson, chief technology officer of Etsy, received a pre-launch Nexus One from Google three weeks ago. He says Google's phone feels connected to certain services on the Web in a way the iPhone doesn't. "Compared to the iPhone, the Google phone feels like it's part of the Internet to me," he said. "If you live in a Google world, you have that world in your pocket in a way that's cleaner and more connected than the iPhone." 
> 
> The same thing applies to the iPhone. If you're a MobileMe, iPhoto, iTunes or Safari user, the iPhone connects effortlessly to your pictures, contacts, bookmarks and music. But if you use other services, you sometimes need to find software workarounds to get access to your content. 
> 
> In comparison, with the Nexus One, if you use GMail, Google Calendar or Picasa, Google's online photo storage software, the phone connects effortlessly to these services and automatically syncs with a single log-in on the phone. 
> 
> The phones work perfectly with their respective software, but both of them don't make an effort to play nice with other services. 

Never mind the technical details of whether the Internet really has an operating system or not. It's clear that in mobile, we're being presented with a choice of _platforms_ that goes far beyond the operating system on the handheld device itself. 

With that preamble, let's take a look at the state of the Internet Operating System - or rather, competing Internet Operating Systems - as they exist today. 

# The Internet Operating System is an Information Operating System

Among many other functions, a traditional operating system coordinates access by applications to the underlying resources of the machine - things like the CPU, memory, disk storage, keyboard and screen. The operating system kernel schedules processes, allocates memory, manages interrupts from devices, handles exceptions, and generally makes it possible for multiple applications to share the same hardware. 

[](http://www.web2expo.com/webexsf2010) As a result, it's easy to jump to the conclusion that "cloud computing" platforms like Amazon Web Services, Google App Engine, or Microsoft Azure, which provide developers with access to storage and computation, are the heart of the emerging Internet Operating System. 

Cloud infrastructure services are indeed important, but to focus on them is to make the same mistake as Lotus did when it bet on DOS remaining the operating system standard rather than the new GUI-based interfaces. After all, Graphical User Interfaces weren't part of the "real" operating system, but just another application-level construct. But even though for years, Windows was just a thin shell over DOS, Microsoft understood that moving developers to higher levels of abstraction was the key to making applications easier to use. 

But what are these higher levels of abstraction? Are they just features that hide the details of virtual machines in the cloud, insulating the developer from managing scaling or hiding details of 1990s-era operating system instances in cloud virtual machines? 

The underlying services accessed by applications today are not just device components and operating system features, but _data subsystems_ : locations, social networks, indexes of web sites, speech recognition, image recognition, automated translation. It's easy to think that it's the sensors in your device - the touch screen, the microphone, the GPS, the magnetometer, the accelerometer - that are enabling their cool new functionality. But really, these sensors are just inputs to massive data subsystems living in the cloud. 

When, for example, as an iPhone developer, you use the iPhone's Core Location Framework to establish the phone's location, you aren't just querying the sensor, you're doing a cloud data lookup against the results, transforming GPS coordinates into street addresses, or perhaps transforming WiFi signal strength into GPS coordinates, and then into street addresses. When the Amazon app or Google Goggles scans a barcode, or the cover of a book, it isn't just using the camera with onboard image processing, it's passing the image to much more powerful image processing in the cloud, and then doing a database lookup on the results. 

Increasingly, application developers don't do low-level image recognition, speech recognition, location lookup, social network management and friend connect. They place high level function calls to data-rich platforms that provide these services. 

With that in mind, let's consider what new subsystems a "modern" Internet Operating System might contain: 

## Search

Because the volume of data to be managed is so large, because it is constantly changing, and because it is distributed across millions of networked systems, search proved to be the first great challenge of the Internet OS era. Cracking the search problem requires massive, ongoing crawling of the network, the construction of massive indexes, and complex algorithmic retrieval schemes to find the most appropriate results for a user query. Because of the complexity, only a few vendors have succeeded with web search, most notably Google and Microsoft. Yahoo! and Amazon too built substantial web search capabilities, but have largely left the field to the two market leaders. 

However, not all search is as complex as web search. For example, an e-commerce site like Amazon doesn't need to constantly crawl other sites to discover their products; it has a more constrained retrieval problem of finding only web pages that it manages itself. Nonetheless, search is fractal, and search infrastructure is replicated again and again at many levels across the internet. This suggests that there are future opportunities in harnessing distributed, specialized search engines to do more complete crawls than can be done by any single centralized player. For example, Amazon harnesses data visible only to them, such as the rate of sales, as well as data they publish, such as the number and value of customer reviews, in ranking the most popular products. 

In addition to web search, there are many specialized types of media search. For example, any time you put a music CD into an internet-connected drive, it immediately looks up the track names in [CDDB](http://en.wikipedia.org/wiki/CDDB) using a kind of fingerprint produced by the length and sequence of each of the tracks on the CD. Other types of music search, like the one used by cell phone applications like [Shazam](http://www.shazam.com/music/web/pages/getshazam.html), look up songs by matching their actual [acoustic fingerprint](http://en.wikipedia.org/wiki/Acoustic_fingerprint). Meanwhile, Pandora's "[music genome project](http://en.wikipedia.org/wiki/Music_Genome_Project)" finds similar songs via a complex of hundreds of different factors as analyzed by professional musicians. 

Many of the search techniques developed for web pages rely on the rich implied semantics of linking, in which [every link is a vote](http://en.wikipedia.org/wiki/PageRank), and votes from authoritative sources are ranked more highly than others. This is a kind of implicit user-contributed metadata that is not present when searching other types of content, such as digitized books. There, search remains in the same brute-force dark ages as web search before Google. We can expect significant breakthroughs in search techniques for books, video, images, and sound to be a feature of the future evolution of the Internet OS. 

The techniques of algorithmic search are an essential part of the developer's toolkit today. The O'Reilly book [Programming Collective Intelligence](http://oreilly.com/catalog/9780596529321) reviews many of the algorithms and techniques. But there's no question that this kind of low-level programming is ripe for a higher-level solution, in which developers just place a call to a search service, and return the results. Thus, search moves from application to system call. 

## Media Access

Just as a PC-era operating system has the capability to manage user-level constructs like files and directories as well as lower-level constructs like physical disk volumes and blocks, an Internet-era operating system must provide access to various types of media, such as web pages, music, videos, photos, e-books, office documents, presentations, downloadable applications, and more. Each of these media types requires some common technology infrastructure beyond specialized search: 

  * **Access Control.** Since not all information is freely available, managing access control - providing snippets rather than full sources, providing streaming but not downloads, recognizing authorized users and giving them a different result from unauthorized users - is a crucial feature of the Internet OS. (Like it or not.) 

The recent moves by News Corp to place their [newspapers behind a paywall](http://www.google.com/search?client=safari&rls=en&q=news+corp+paywall&ie=UTF-8&oe=UTF-8), as well as the paid application and content marketplace of the iPhone and iPad suggests that the ability to manage access to content is going to be more important, rather than less, in the years ahead. We're largely past the knee-jerk "keep it off the net" reactions of old school DRM; companies are going to be exploring more nuanced ways to control access to content, and the platform provider that has the most robust systems (and consumer expectations) for paid content is going to be in a very strong position. 

In the world of the App Store, paid applications and paid content are re-legitimizing access control (and payment.) Don't assume that advertising will continue to be the only significant way to monetize internet content in the years ahead. 

  * **Caching**. Large media files benefit from being closer to their destination. A whole class of companies exist to provide [Content Delivery Networks](http://en.wikipedia.org/wiki/Content_delivery_network); these may survive as independent companies, or these services may ultimately be rolled up into the leading Internet OS companies in much the way that Microsoft acquired or "embraced and extended" various technologies on the way to making Windows the dominant OS of the PC era. 

  * **Instrumentation and analytics** Because of the amount of money at stake, an entire industry has grown up around web analytics and search engine optimization. We can expect a similar wave of companies instrumenting social media and mobile applications, as well as particular media types. After all, a video, a game, or an ebook can know how long you watch, when you abandon the product and where you go next. 

Expect these features to be pushed first by independent companies, like [TweetStats](http://tweetstats.com/) or [Peoplebrowsr Analytics](http://analytics.peoplebrowsr.com/) for Twitter, or [Flurry](http://www.flurry.com/) for mobile apps. [GoodData](http://gooddata.com), a cloud-based business intelligence platform is being used for analytics on everything from Salesforce applications to online games. (Disclosure: I am an investor and on the board of GoodData.) But eventually, via acquisition or imitation, they will become part of the major platforms. 

## Communications

The internet is a communications network, and it's easy to forget that communications technologies like email and chat, have long been central to the Internet's appeal. Now, with the widespread availability of VoIP, and with the mobile phone joining the "network of networks," voice and video communications are an increasingly important part of the communications subsystem. 

Communications providers from the Internet world are now on a collision course with communications providers from the telephony world. For now, there are uneasy alliances right and left. But it isn't going to be pretty once the battle for control comes out into the open. 

I expect the communications directory service to be one of the key battlefronts. Who will manage the lookup service that allows individuals and businesses to find and connect to each other? The phone and email address books will eventually merge with the data from social networks to provide a rich set of identity infrastructure services. 

## Identity and the Social Graph

When you use Facebook Connect to log into another application, and suddenly your friends' faces are listed in the new application, that application is using Facebook as a "subsystem" of the new Internet OS. On Android phones, simply add the Facebook application, and your phone address book shows the photos of your Facebook friends. Facebook is [expanding the range of data revealed by Facebook Connect](http://techcrunch.com/2010/03/26/facebooks-plan-to-automatically-share-your-data-with-sites-you-never-signed-up-for/); they clearly understand the potential of Facebook as a platform for more than hosted applications. 

But as hinted at above, there are other rich sources of social data - and I'm not just talking about applications like Twitter that include explicit social graphs. Every communications provider owns a treasure trove of social data. Microsoft has piles of social data locked up in Exchange, Outlook, Hotmail, Active Directory, and Sharepoint. Google has social data not just from Orkut (an also-ran in the US) but from Gmail and Google Docs, whose "sharing" is another name for "meaningful source of workgroup-level social graph data." And of course, now, there's the social graph data produced by the address book on every Android phone... 

The breakthroughs that we need to look forward to may not come from explicitly social applications. In fact, I see "me too" social networking applications from those who have other sources of identity data as a sign that they don't really understand the platform opportunity. Building a social network to rival Facebook or Twitter is far less important to the future of the Internet platform than creating facilities that will allow third-party developers to leverage the social data that companies like Google, Microsoft, Yahoo!, AOL - and phone companies like ATT, Verizon and T-Mobile - have produced through years or even decades of managing user's social data for communications. 

Of course, use of this data will require breakthroughs in privacy mechanism and policy. As Nat Torkington wrote in email after reviewing an earlier draft of this post: 

> We still face the problem of "friend": my Docs social graph is different from my email social graph is different from my Facebook social graph is different from my address book. I want to be able to complain about work to my friends without my coworkers seeing it, and the usability-vs-privacy problem remains unsolved.

Whoever cracks this code, providing frameworks that make it possible for applications to be functionally social without being socially promiscuous, will win. Platform providers are in a good position to solve this problem once, so that users don't have to give credentials to a larger and larger pool of application providers, with little assurance that the data they provide won't be misused. 

## Payment

Payment is another key subsystem of the Internet Operating System. Companies like Apple that have 150 million credit cards on file and a huge population of users accustomed to using their phones to buy songs, videos, applications, and now ebooks, are going to be in a prime position to turn today's phone into tomorrow's wallet. (And as anyone who reaches into a wallet not for payment but for ID knows, payment systems are also powerful, authenticated identity stores - a fact that won't always be lost on payment providers looking for their lock on a piece of the Internet future.) 

PayPal obviously plays an important role as an internet payment subsystem that's already in wide use by developers. It operates in 190 countries, in 24 different currencies (not counting in-game micro-currencies) and it has over 210 million accounts (with 81 million of them active). What's fascinating is the rich developer ecosystem they've built around payment - their recent developer conference had over 2000 attendees. Their challenge is to make the transition from the web to mobile. 

Google Checkout has been a distant also-ran in web payments, but the Android Market has given it new prominence in mobile, and will eventually make it a first class internet payment subsystem. 

Amazon too has a credible payment offering, though until recently they haven't deployed it to full effect, reserving the best features for their own e-commerce site and not making them available to developers. (More on that in next week's post, in which I will handicap the leading platform offerings from major internet vendors.) 

## Advertising

Advertising has been the most successful business model on the web. While there are signs that [e-commerce](http://radar.oreilly.com/2010/02/convergence-advertising-mobile-ecommerce.html) \- buying everything from virtual goods to [a lunchtime burrito](http://radar.oreilly.com/2010/03/three-lessons-from-the-chipotl.html) \- may be the bigger opportunity in mobile (and perhaps even in social media), there's no question that advertising will play a significant role. 

Google's dominance of search advertising has involved better algorithmic placement, as well as the ability to predict, in real time, how often an ad will be clicked on, allowing them to optimize the advertising yield. The [Google Ad Auction](http://googleblog.blogspot.com/2009/03/introduction-to-ad-auction.html) system is the heart of their economic value proposition, and demonstrates just how much difference a technical edge can make. 

And advertising has always been a platform play. Signs that it will be a key battleground of the Internet OS can be seen in the competing [acquisition of AdMob by Google](http://blog.admob.com/2009/11/09/google-to-acquire-admob/) and [Quattro Wireless](http://techcrunch.com/2010/01/04/apple-acquires-quattro-wireless/) by Apple. 

The question is the extent to which platform companies will use their advertising capabilities as a system service. Will they treat these assets as the source of competitive advantage for their own products, or will they find ways to deploy advertising as a business model for developers on their platform? 

## Location

Location is the sine-qua-non of mobile apps. When your phone knows where you are, it can find your friends, find services nearby, and even better authenticate a transaction. 

Maps and directions on the phone are intrinsically cloud services - unlike with dedicated GPS devices, there's not enough local storage to keep all the relevant maps on hand. But when turned into a cloud application, maps and directions can include other data, such as real-time traffic (indeed, traffic data collected from the very applications that are requesting traffic updates - a classic example of "collective intelligence" at work.) 

Location is also the search key for countless database lookup services, from Google's "search along route" to a Yelp search for nearby cafes to the Chipotle app routing your lunch request to the restaurant near you. 

[](http://en.oreilly.com/where2010/) In many ways, Location is the Internet data subsystem that is furthest along in its development as a system service accessible to all applications, with developers showing enormous creativity in using it in areas from augmented reality to advertising. (Understanding that this would be the case, I launched the [Where 2.0 Conference](http://en.oreilly.com/where2.0) in 2005. There are lessons to be learned in the location market for all Internet entrepreneurs, not just "geo" geeks, as techniques developed here will soon be applied in many other areas.) 

## Activity Streams

Location is also becoming a proxy for something else: attention. The [ originally designed for finding spots where people are congregating, quickly became a focus for advertising, as merchants were able to discover and reward their most frequent customers. Now the idea of the check-in being "embraced and extended" to show attention to virtual locations. As John Battelle put it the other day, "](http://foursquare.com/help/<FourSquare)[My location is a box of cereal](http://bit.ly/aaJdPu)." (Disclosure: [O'Reilly AlphaTech Ventures](http://oatv.com) is an investor in Foursquare.) 

We thus see convergence between Location and social media concepts like [Activity Streams](http://wiki.activitystrea.ms/). Platform providers that understand and exploit this intersection will be in a stronger position than those who see location only in traditional terms. 

## Time

Time is an important dimension of data driven services - at least as important as location, though as yet less fully exploited. Calendars are one obvious application, but activity streams are also organized as timelines; stock charts link up news stories with spikes or drops in price. Time stamps can also be used as a filter for other data types (as Google measures frequency of update in calculating search results, or as an RSS feed or social activity stream organizes posts by recency.) 

"Real time" - as in the real-time search provided by Twitter, the "where am I now" pointer on a map, the [automated replenishment of inventory at WalMart, or instant political polling](http://radar.oreilly.com/2008/12/google-walmart-mybarackobama.html) \- emphasizes just how much the future will belong to those who measure response time in milliseconds, or even microseconds, rather than seconds, hours, or days. This [need for speed](http://radar.oreilly.com/operations/) is going to be a major driver of platform services; individual applications will have difficulty keeping up. 

## Image and Speech Recognition

As I've written previously, one of the big differences since I first wrote [What is Web 2.0?](http://www.oreillynet.com/go/web2), my analysis of how the Web as Platform was going to be dominated by data services built by network effects in user-contributed data, is that increasingly, the data is contributed by sensors. (John Battelle and I called this trend [Web Squared](http://www.web2summit.com/web2009/public/schedule/detail/10194)). 

With the advent of smartphone apps like [Google Goggles]() and the [Amazon e-commerce app](), which deploy advanced image recognition to scan bar codes, book covers, album covers and more - not to mention gaming platforms like Microsoft's still unreleased [Project Natal](http://www.xbox.com/en-US/live/projectnatal/) and innovative startups like [Affective Interfaces](http://www.affectiveinterfaces.com/), it's clear that computer vision is going to be an important part of the UI toolkit for future developers. While there are good computer vision packages like [OpenCV](http://oreilly.com/catalog/9780596516130) that can be deployed locally for robotics applications, as well as research projects like those competing in the [DARPA Grand Challenge for automated vehicles](http://en.wikipedia.org/wiki/DARPA_Grand_Challenge), for smartphone applications, image recognition, like speech recognition, happens in the cloud. Not only is there a wealth of compute cycles, there are also vast databases of images for matching purposes. Picasa and Flickr are no longer just consumer image sharing sites: they are vast repositories of tagged image data that can be used to train algorithms and filter results. 

## Government Data

[](http://www.gov2expo.com) Long before recent initiatives like [data.gov](http://data.gov</a), governments have been a key supplier of data for internet applications. Everything from weather, maps, satellite imagery, GPS positioning, and SEC filings to crime reports have played an important role in successful internet applications. Now, government is also a recipient of crowdsourced data from citizens. For example, [FixMyStreet](http://fixmystreet.com) and [SeeClickFix](http://seeclickfix.com) submit 311 reports to local governments - potholes that need filling, graffiti that needs repainting, streetlights that are out. These applications have typically overloaded existing communications channels like email and SMS, but there are now attempts to standardize an [Open311](http://open311.org) web services protocol. 

Now, a new flood of government data is being released, and the government is starting to see itself as a platform provider, providing facilities for private sector third parties to build applications. This idea of [Government as a Platform](http://opengovernment.labs.oreilly.com/) is a key focus of my advocacy about [Government 2.0](http://gov2events.com). 

There is huge opportunity to apply the lessons of Web 2.0 and apply them to government data. Take health care as an example. How might we improve our healthcare system if Medicare provided [a feedback loop about costs and outcomes](http://www.newyorker.com/online/blogs/newsdesk/2009/06/atul-gawande-the-cost-conundrum-redux.html) analogous to the one that Google built for search keyword advertising. 

Anyone building internet data applications would be foolish to underestimate the role that government is going to play in this unfolding story, both as provider and consumer of data web services, and also as regulator in key areas like privacy, access, and interstate commerce. 

# What About the Browser?

While I think that claims that [the browser itself is the new operating system](http://www.google.com/search?client=safari&rls=en&q=browser+operating+system&ie=UTF-8&oe=UTF-8) are as misguided as the idea that it can be found solely in cloud infrastructure services, it is important to recognize that control over front end interfaces is at least as important as back-end services. Companies like Apple and Google that have substantial cloud services and a credible mobile platform play are in the catbird seat in the platform wars of the next decade. But the browser, and with it control of the PC user experience, is also critical. 

This is why Apple's iPad, Google's ChromeOS, and HTML 5 (plus initiatives like Google's [Native Client](http://code.google.com/p/nativeclient/)) are so important. Microsoft isn't far wrong in its cloud computing vision of "[Software Plus Services](http://www.microsoft.com/softwareplusservices/)." The full operating system stack includes back end infrastructure, the data subsystems highlighted in this article, and rich front-ends. 

Apple and Microsoft largely have visions of vertically integrated systems; Google's vision seems to be for open source driving front end interfaces, while back end services are owned by Google. But in each case, there's a major drive to own a front-end experience that favors each company's back-end systems. 

# What's Still Missing

Even the most advanced Internet Operating System platforms are still missing many concepts that are familiar to those who work with traditional single-computer operating systems. Where is the executive? Where is the memory management? 

I believe that these functions are evolving at each of the cloud platforms. Tools like memcache or mapreduce are the rough cloud equivalents of virtual memory or multiprocessing features in a traditional operating system. But they are only the beginning. Werner Vogels' post [Eventually Consistent](http://www.allthingsdistributed.com/2008/12/eventually_consistent.html) highlights some of the hard technical issues that will need to be solved for an internet-scale operating system. There are many more. 

But it's also clear that there are many opportunities to build higher level functionality that will be required for a true Internet Operating System. 

Might an operating system of the future manage when and how data is collected about individuals, what applications can access it, and how they might use it? Might it not automatically synchronize data between devices and applications? Might it do automatic translation, and automatic format conversion between different media types? Might such an operating system do predictive analytics to collect or locally cache data that it expects an individual user or device to need? Might such an operating system do "garbage collection" not of memory pointers but of outdated data or spam? Might it not perform credit checks before issuing payments and suspend activity for those who violate terms of service? 

There is a great opportunity for developers with vision to build forward-looking platforms that aim squarely at our connected future, that provide applications running on any device with access to rich new sources of intelligence and capability. The possibilities are endless. There will be many failed experiments, many successes that will be widely copied, a lot of mergers and acquisitions, and fierce competition between companies with different strengths and weaknesses. 

_Next week, I'll handicap the leading players and tell you what I think of their respective strategies._
