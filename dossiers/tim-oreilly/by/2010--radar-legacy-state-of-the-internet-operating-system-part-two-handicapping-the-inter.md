---
title: "State of the Internet Operating System Part Two: Handicapping the Internet Platform Wars"
person: tim-oreilly
section: by
type: blog-post
year: 2010
date: 2010-04-30
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/2010/04/handicapping-internet-platform-wars.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# State of the Internet Operating System Part Two: Handicapping the Internet Platform Wars

## Full text

_This post is Part Two of my**State of the Internet Operating System**. If you haven't read [Part One](http://radar.oreilly.com/2010/03/state-of-internet-operating-system.html), you should do so before reading this piece._

As I wrote last month, it is becoming increasingly clear that the internet is becoming not just a platform, but an operating system, an operating system that manages access by devices such as personal computers, phones, and other personal electronics to cloud subsystems ranging from computation, storage, and communications to location, identity, social graph, search, and payment. The question is whether a single company will put together a single, vertically-integrated platform that is sufficiently compelling to developers to enable the kind of lock-in we saw during the personal computer era, or whether, Internet-style, we will instead see services from multiple providers horizontally integrated via open standards. 

There are many competing contenders to the Internet Operating System throne. Amazon, Apple, Facebook, Google, Microsoft, and VMware all have credible platforms with strong developer ecosystems. Then there is a collection of players with strong point solutions but no complete operating system offering. Let's take them in alphabetical order. 

# Amazon

With the introduction in 2006 of S3, the Simple Storage Service, and EC2, the Elastic Compute Cloud, Amazon electrified the computing world by, for the first time, offering a general-purpose cloud computing platform with a business model that made it attractive to developers large and small. An ecosystem quickly grew up of companies providing developer and system-management tools. Companies like [RightScale](http://rightscale.com) provide higher level management frameworks; [EngineYard](http://www.engineyard.com/) and [Heroku](http://heroku.com) provide Ruby-on-Rails based stacks that make it easy to use familiar web tools to deploy applications against an Amazon back-end; the [Ubuntu Enterprise Cloud](http://www.ubuntu.com/cloud/private) and [Eucalyptus](http://www.eucalyptus.com/) offer Amazon-compatible solutions. 

A number of competitors, including Rackspace, Terremark, Joyent, GoGrid, and AppNexus are [going head to head with Amazon in providing cloud infrastructure services](http://blogs.zdnet.com/BTL/?p=20689). Many analysts are simply handicapping these providers and comparing them to offerings from Microsoft and Google. But to compare only cloud infrastructure providers is to miss the point. It's a bit like leaving out Microsoft while comparing IBM, Compaq, and Dell when handicapping the PC operating system wars. Hardware was no longer king; the competition had moved up the stack. 

The key subsystems of the Internet Operating System are not storage and computation. Those are merely table stakes to get into the game. What will distinguish players are data subsystems. 

Data is hard to acquire and expensive to maintain. Delivering it algorithmically at the speeds applications required for reasonable real-time performance is the province of very few companies. 

In this regard, Amazon has three major subsystems that give it an edge: its access to media (notably books, music, and video); its massive database of user contributed reviews, ratings, and purchase data, and its One-Click database of hundreds of millions of payment accounts. As yet, only one of these, payment, has been turned into a web service, [Amazon Flexible Payment Service.](http://aws.amazon.com/fps/)

Despite having an early lead in internet payment, Amazon reserved its use for too long for competitive advantage for its own e-commerce site, and didn't deploy it as an internet-wide service usable by developers until recently. And even then, Amazon lacks significant payment presence on mobile devices. Amazon has its own Kindle device for ebook sales, and its iPhone and Android apps for e-commerce, but powerful as these apps may be for driving sales to Amazon, they give the company no leverage in supporting third party developers. If anything, they will hinder the development of a mobile e-commerce ecosystem based on Amazon because Amazon is the largest competitor for many potential e-commerce developers. 

Amazon's use of its media database as a back-end for its own proprietary e-reader device, the Kindle, highlights one of the fronts in what I've elsewhere called [the War for the Web](http://radar.oreilly.com/2009/11/the-war-for-the-web.html), namely the use of a dedicated front-end device giving preferential access to a player's back-end services. Apple and Google are in a much stronger position in this regard, with general-purpose smartphones as the device front-ends for their platforms. But Amazon has moved quickly to deploy its Kindle software on iPhone and Android; their compelling library of content may make the use of a proprietary device less important. 

Two other Amazon service worthy of note are the [Mechanical Turk](http://aws.amazon.com/mturk/) service and the [Fulfillment Web Service](http://aws.amazon.com/fws/). 

The Mechanical Turk service allows developers to farm out simple tasks to human participants. This turns out to be a remarkably powerful capability, with applications as divergent as data cleansing, metadata management, and even [crowdsourcing disaster relief](http://radar.oreilly.com/2010/03/how-crowdsourcing-helped-haiti.html). There are many tasks that computers can't do alone, but that humans can help with. I've often made the case that all Web 2.0 applications are in fact systems for [harnessing the collective intelligence of human users](http://radar.oreilly.com/2006/11/harnessing-collective-intellig.html). But most of these applications do it in a single field of endeavor; Mechanical Turk is the leading general-purpose platform for putting people to work on small tasks that are easy for humans but hard for computers to do on their own. 

Amazon's Fulfillment Web Service is another sleeper, whose full significance hasn't yet been realized. I foresee a future in which [phone-based e-commerce](http://radar.oreilly.com/2010/02/convergence-advertising-mobile-ecommerce.html) makes the leap from virtual to physical goods. Right now, there's a huge business in selling songs, applications, ebooks, movies, and games on phones. There's an even bigger explosion coming in buying physical goods on the phone. And Amazon is the only platform player who actually can offer programmatically-driven fulfillment services. This is hugely important. 

Amazon's weaknesses: Search (they have search capabilities with A9 and Alexa, but don't have a business model to support or extend those capabilities to developers at a cost (free) that is going to be required); advertising; location services; speech recognition; social graph. They have a very strong hand, very deep in some areas, but almost completely lacking in others. 

Amazon also is weaker financially than its big three competitors: Apple, Google, and Microsoft. Jeff Bezos argues that this is actually a strength. He has noted more than once that Amazon's core business is retail, a notably low margin business. Cloud computing is a better business for Amazon than the school of hard knocks where it's learned to make a profit. "Commodity businesses don't scare us," [he says](http://www.wired.com/techbiz/it/magazine/16-05/mf_amazon?currentPage=all). "We're experts at them. We've never had 35 or 40 percent margins like most tech companies." 

This idea, of course, applies only to the commodity layers of cloud computing. And that's one more reminder that the outsized profits actually reside in the [data subsystems](http://radar.oreilly.com/2010/03/state-of-internet-operating-system.html#datasubsystems) where lock-in is achievable. 

# Apple

A few years ago, everyone thought that the big industry showdown was between Microsoft and Google. Now, Apple is the company to beat. With over 185,000 applications, the iPhone app store is creating a new information and services marketplace to rival the web itself. While Apple doesn't provide Amazon-like cloud hosting services, they don't have to. iPhone apps don't live on the web per se, though most of them, apart from local games, do rely on internet-based services. 

Apple's strongest Internet OS subsystems are media (the iTunes store), application hosting (the App Store), and payment. Apple has over a hundred million people who are used to buying content with one click. They've given Apple their payment credentials, and use them to buy a wide variety of digital goods: first music, then applications, including games, then books. 

What's next? As physical goods e-commerce takes off on the phone, I expect Apple to try to insert itself into the great money river flowing through its platform. Apple takes a 30% cut from application sales. While this percentage is too high for physical goods, it's not hard to imagine Apple interposing itself as the payment processor for applications ranging from ebay to Chipotle, taking a little bit of a much larger revenue stream. 

Apple's weaknesses are legion. They have no cloud computation platform, they are latecomers to location and advertising, with interesting acquisitions but no clear strategy and nothing like a critical mass of data. (They do, however, have piles of cash, and strategic acquisitions could quickly change those dynamics.) They have great social graph assets in the form of user address books, email stores, and instant messaging friend networks, but they show little sign of understanding how to turn those assets into next generation applications or services. But most strikingly, they don't really seem to understand some key aspects of the game that is afoot. 

If they did, [MobileMe](http://www.apple.com/mobileme/) would be free to every user, not a $99 add-on. Web 2.0 companies know that systems that get better the more people use them are the key to marketplace dominance in the network era. The social graph is one such system, for which Facebook is currently the market leader. Companies that want to dominate the Internet Operating System either need to make a deal with Facebook to integrate their platforms, or have a compelling strategy for building out their own social graph assets. Unless Apple is planning a deal with Facebook, their current MobileMe strategy seems only to indicate that they don't understand the stakes. 

Apple's other weaknesses might well be addressed by an alliance with Microsoft, which has strengths everywhere that Apple is weak. Given [Apple's feud with Google](http://www.nytimes.com/2010/03/14/technology/14brawl.html), this is an increasingly likely scenario. In fact, you can imagine a 3-way alliance between Apple, Facebook, and Microsoft that would make for a very powerful platform. That being said, alliances are relatively weak at coordinated execution, so this opportunity may be stronger in theory than it turns out in fact. 

But all of these weaknesses may be outweighed by the amazing job that Apple has done in creating a new computing paradigm to rival the web itself. As Jim Stogdill wrote in a recent post, [the iPad isn't a computer, it's a distribution channel](http://radar.oreilly.com/2010/04/the-ipad-isnt-a-computer-its-a.html): 

> One interesting twist is how the iPad combines network effects and constrained distribution. The bright shiny object design of the iPad leads to network effects at the app store which in turn drives more consumers back to the device itself. Then to the degree that those two forces hold consumers in thrall of the device, Apple can use the device as the point of sale for content worth more than the device itself. The leverage is linked - the first leads to market presence, and then the market presence makes for stronger monetization opportunities in the device-hosted channel. 
> 
> The other interesting thing is that so many of those "apps" are really just web pages without a URL. Or books packaged as an app. In short, this is content that is abandoning the web to become a monetizable app. 
> 
> History is never completely new and we've seen things like this happen before. Prior to the 1980's essentially all television was broadcast in the clear. An unconstrained distribution channel like broadcast TV could only be monetized through ad sales, but along came cable with its point-to-point wave guides and surprised consumers were suddenly faced with paying for access. 

This is Apple's trump card. 

There are those who point to the lessons of VHS vs Betamax and the commodity PC vs Apple, and see Android as an inevitable winner. However, as Mark Sigal points out in [Five reasons iPhone vs Android isn't Mac vs Windows](http://radar.oreilly.com/2010/04/five-reasons-iphone-v-android.html): 

> It is a truism that in platform plays he who wins the hearts and minds of developers, wins the war. In the PC era, Apple forgot this, bungling badly by launching and abandoning technology initiatives, co-opting and competing with their developers and routinely missed promised milestones. By contrast, Microsoft provided clear delineation points for developers, integrated core technologies across all products, and made sure developer tools readily supported these core initiatives. No less, Microsoft excelled at ensuring that the ecosystem made money. 
> 
> Lesson learned, Apple is moving on to the 4.0 stage of its mobile platform, has consistently hit promised milestones, has done yeomen's work on evangelizing key technologies within the platform (and third-party developer creations - "There's an app for that"), and developed multiple ways for developers to monetize their products. No less, they have offered 100 percent distribution to 85 million iPhones, iPod Touches and iPads, and one-click monetization via same. Nested in every one of these devices is a giant vending machine that is bottomless and never closes. By contrast, Google has taught consumers to expect free, the Android Market is hobbled by poor discovery and clunky, inconsistent monetization workflows. Most damning, despite touted high-volume third-party applications, there are (seemingly) no breakout third-party developer successes, despite Android being around two-thirds as long as the iPhone platform.

And that's only one of the five compelling reasons that Mark puts forward for Apple to win in mobile. (However, see [Chris Lynch's rebuttal](http://www.planetofthepenguins.com/2010/04/26/chris-vs-five-reasons-iphone-vs-android-isnt-mac-vs-windows/) for the corresponding arguments why Android will win.) 

Nonetheless, even if Apple has the dominant mobile platform, they won't have the full recipe for the operating system of the future. A network connection has two ends, and until Apple can offer a complete suite of cloud data services, they can't deliver the kind of lock-in that Microsoft enjoyed in the PC era. This is actually a good thing, and a harbinger of the best outcome for the Internet OS, namely that no one controls enough of it, everyone has to compromise, and interoperability (the internet as "network of networks") continues to play its generative role. 

# Facebook

Archilochus, the Greek fabulist, once said, "The fox knows many things, but the hedgehog knows one big thing." He might well have been talking about Facebook. Their one big thing, the social graph, might look like an incomplete offering, but they have made a great deal of progress based on it. 

Facebook is more than a website. For many people, it is a replacement for the web, the entire platform, the world in which they receive news, communicate with friends, play games, store and share photographs and videos, and use any one of hundreds of thousands of applications. The Facebook Application ecosystem exceeds even the Apple App Store in the number of applications ([500,000](http://www.facebook.com/press/info.php?statistics) to Apple's [187,000](http://www.apple.com/ipad/app-store/)); third party developers like Zynga are [amassing fortunes](http://blogs.reuters.com/mediafile/2009/12/17/facebook-nearing-1-billion-revenue-run-rate-zynga-revenue-triples/) using entirely new social selling dynamics. 

[Facebook Connect](http://developers.facebook.com/connect.php) is well on its way to becoming the universal single-signon for the web - one of the first Internet Operating System subsystems (after Google Maps) to get wide adoption across a range of websites not belonging to the platform provider. Even more importantly, Facebook Connect allows you to [Facebook-enable](http://developers.facebook.com/connect.php?tab=iphone) mobile apps. Clearly, Facebook understands what it means to be a platform provider. 

Their latest announcements, of Facebook's [Graph API](http://developers.facebook.com/docs/api) and [Social Plugins](http://developers.facebook.com/plugins), are taking Facebook beyond its original "walled garden" approach, instead turning Facebook into a social utility for the entire web (including mobile devices.) 

Facebook is testing a payment platform, but perhaps more interestingly, they appear to be [partnering with Paypal](http://www.facebook.com/press/releases.php?p=144261) to increase their capabilities in this area. They are getting better at monetization via advertising, but they haven't yet found the golden path for social advertising that Google found for search. 

Facebook's weaknesses: Location, control over mobile devices, general purpose computing and storage platforms. But these are weaknesses only in the context of the desire to have a vertically-integrated platform from a single vendor. It may instead be that the lack of these capabilities is Facebook's greatest strength, as it will force them into a strategy of horizontal integration. 

# Google

There's no question in my mind that Google's Internet Operating System is the furthest along. Many observers will look first to [Google AppEngine](http://code.google.com/appengine/whyappengine.html) as Google's echo of the Win32 promise. How can anyone who lived through the transition from DOS to Windows not read the following paragraph, and not be struck by the similarity of intent? 

> "For the the first time your applications can take advantage of the same scalable technologies that Google applications are built on, things like BigTable and GFS. Automatic scaling is built in with App Engine, all you have to do is write your application code and we'll do the rest. No matter how many users you have or how much data your application stores, App Engine can scale to meet your needs." 

As Mark Twain once said, "History does not repeat itself, but it does rhyme." 

But to focus too much on AppEngine is to miss the point. If all the Internet Operating System does is provide storage and computation, then Amazon, Microsoft, and VMware are all contenders - and Amazon has the lead. 

Remember, though, that in the future, the subsystems that applications depend on to differentiate themselves will largely be data subsystems. And data at scale is Google's sweet spot. 

Consider a few of the following applications, and ask yourself how many companies could put together all the data and computation assets to deliver on the following promises: 

  * Provide [free turn-by-turn directions](http://radar.oreilly.com/2009/10/google-shrinks-another-market.html) on the phone, with destinations set by natural language search rather than by address, with optional speech recognition to set the destination or to search along the route for items of interest, with real-time traffic information used to calculate your arrival time, and actual Streetview images of turns as well as of your final destination. (The ability to deliver these services directly is a critical advantage. Anyone who has to license one or more of the components from another company has a much harder time giving the service away for free.) 

  * Point your cell phone camera at many common objects - a book cover, a wine label, a work of art in a museum, a famous building or other landmark, a company logo, a business card, a bar code, and even, in an unreleased version, a human face - and return information about that object ([Google Goggles](http://www.google.com/mobile/goggles/#landmark)). (Amazon's e-commerce app for the iPhone and Android does show off some similar capabilities. Bar-code scanning and image recognition allow you to see something in the real world, quickly find it at Amazon, and either order it, or simply remember it on your Amazon wishlist. But the range of objects recognized is less complete, and the use case is Amazon e-commerce, versus Google's more general platform.) 

  * Automatically dial all of your phone numbers until you answer one of them, and if you aren't found, automatically transcribe (even badly) the message that was left for you. 

  * [Translate your speech or document](http://www.nytimes.com/2010/03/09/technology/09translate.html) (even badly) into any one of fifty languages. 

The list goes on. Google has the most impressive set of data assets of any company on the planet, together with the boldness to put them together into a vision of how computing will work in the future. They aren't afraid, any more than Bill Gates was with Windows 1.0, to put out something that is ahead of their current reach, with the persistence to stick with it till it works. 

And that's leaving out Google's stronghold in search and advertising, its dominance via YouTube of internet video, its cloud office suite, its strong email offering, the fact that Google Maps is becoming the lingua franca of mapping across the web, and more. With Android, Google also has the front-end component of the full mobile-to-cloud stack, with an industry adoption strategy (open hardware from multiple manufacturers) that has worked before, for both the VCR and the personal computer. They have a robust application ecosystem, both [for the phone](http://www.android.com/market/) and [for the enterprise](http://www.google.com/enterprise/marketplace/home). A week after its launch, the Google Application Marketplace [had nearly 1500 apps](http://radar.oreilly.com/2010/03/google-marketplace-has-over-a-thousand-apps.html), a faster uptake than even the iPhone. Today, there are [over 50,000 Android Apps](http://erictric.com/2010/04/24/android-market-now-contains-over-50000-applications/). (But as Marc Sigal notes in the analysis linked earlier, Apple has demonstrated much more consistent monetization for developers. According to O'Reilly Research, 24% of iPhone apps are free apps, while 59% of Android apps are free.) 

That being said, Google does have a payment platform. While [Google Checkout](http://checkout.google.com) was an also-ran in the web payment wars, it has renewed significance and opportunity in the mobile era, as every Android Market customer is, by default, now a Google Checkout customer. In this one story you see how having all of the elements together makes each of them stronger than they would be alone. If you have an Android phone, Google Checkout is suddenly the default payment option. It doesn't have to be the best. It's the incumbent. 

Google's weaknesses: they are the one to beat, the new Microsoft that everyone is afraid of. In addition, they lack Apple's sure touch on user experience; even the slickest Android phone lags Apple's fit and finish. They also have yet to come up with a convincing social media subsystem, although they are clearly focused on this opportunity. Their strongest assets are not actually overtly social systems like [Google Wave](http://www.google.com/url?q=http://wave.google.com/about.html) or [Google Buzz](http://buzz.google.com), but the phone itself, and its connection to the Gmail-based cloud address book. 

I continue to believe that the tools we actually use to communicate with each other - our phones, our email, our instant messaging, and our shared documents - are the most powerful measures of our real social network. The company that first cracks the code of reflecting that social network throughout its applications, and giving the user the power to harness that network, will ultimately win. Google has many of the data assets necessary to develop those next-generation applications, but they haven't yet found the way to put them together. 

# Microsoft

Microsoft, like Google, has a strong suite of capabilities across the board: the [Azure](http://www.microsoft.com/windowsazure/) hosting and computation platform, the Bing search engine and advertising platform, a full-featured mapping platform, speech recognition (via the 2007 acquisition of [Tellme](http://www.tellme.com/)). They have made [a promising restart in their mobile platform with Windows Mobile 7](http://www.engadget.com/2010/02/15/windows-phone-7-series-is-official-and-microsoft-is-playing-to/). They have enormous untapped business-oriented social media assets in Microsoft Exchange, Outlook, and Sharepoint. And of course, they have boatloads of cash, and the willingness to spend it to achieve strategic objectives. They understand the game they are playing, and how important it is to their survival. 

That being said, Microsoft's biggest asset right now might just be that they aren't Google, making them the favored white knight of everyone from Apple to Facebook. With rumors flying that [Apple is in talks with Microsoft to make Bing the default search engine on iPhone](http://www.ipodnn.com/articles/10/01/20/growing.split.between.apple.google/), you can see the shape of a possible future in which an alliance between Apple and Microsoft acts as a counter to Google's outsized ambitions. Add in a partnership with Facebook, in which Microsoft is an investor, and you have a powerful combination. 

Microsoft's biggest weaknesses (apart from the fact that the original Windows Mobile platform was a failure, and they are now facing a restart) are the "strategy tax" of continuing to support Windows and Microsoft Office, the very same problem that [kept Microsoft from seizing the internet opportunity in the late 1990s](http://www.breakingwindows.net/). 

Another point of distinction between Microsoft and Google is Microsoft's "software plus services" vision - namely the idea that rich, device-specific client apps will be the front end to web services, versus Google's web-only vision. Microsoft argues that, faced with the success of native apps on smartphones, [even Google is embracing a software-plus-services approach](http://www.theregister.co.uk/2010/02/01/microsoft_on_google_web_apps/). However, the rich clients that are driving the equation are not PC-based; they are native smartphone apps. And barring a successful restart of Microsoft's phone strategy, Google has the advantage there. 

This isn't to say that Microsoft won't continue to be a phenomenally successful company - just as IBM managed to do despite the death of its mainframe monopoly - but the cutting edge of the future is in data-backed mobile services, where they are playing serious catch up. 

Microsoft's greatest opportunity, paradoxically, is to embrace open data services in the same way that IBM embraced Open Source Software, to integrate their offerings with those from Facebook, Nuance, Paypal, and other best of breed data services. The question is whether that's in their DNA or their business model. My bet is that it's Facebook that emerges as the integration point for selected Microsoft services (location and search in particular) rather than the other way around. 

# Nokia

While Nokia is left out of many of the overheated discussions about the future, let's not forget that they are still the dominant phone supplier in the world, that they own significant location and mapping assets via their [purchase of Navteq](http://www.informationweek.com/blog/main/archives/2007/10/nokias_acquisit.html), and that they too have a platform vision in the form of [Ovi](http://www.ovi.com/services/), providing access to music, maps, applications, games, and more on Nokia phones. That being said, it's hard to conceive of Nokia as a first-tier player in the Great Game. 

# PayPal

There is no doubt in my mind that payment will be one of the most important of the Internet OS subsystems. [E-commerce, not advertising, is the killer business model of the mobile world.](http://radar.oreilly.com/2010/02/convergence-advertising-mobile-ecommerce.html)

And payment is hard. Knowing how much credit to extend is one of the problems that is best left to people with algorithmic expertise and massive amounts of data. 

Apple and Google have their own built-in payment solutions (as does Microsoft for some of their platforms, such as Xbox), but what about everyone else? Visa and MasterCard remain sleeping giants; mobile phone carriers too have payment capabilities, but their business culture and systems make it difficult for them to deploy them for cutting edge applications. PayPal is web-native; making the transition to mobile has got to be their highest priority. Startups like Square (and others yet to be announced) are also taking aim at this area. Expect innovation. Expect competition. Expect acquisitions. 

# Salesforce

Salesforce.com also has a strong platform play, with thousands of business-oriented applications built on the [force.com](http://force.com) platform. Salesforce in fact was the first to promulgate the idea of "[platform as a service](http://www.salesforce.com/paas/)" (as distinguished from simply "software as a service" (individual applications) or "[infrastructure as a service](http://www.salesforce.com/paas/)" (the kind of platform that Amazon pioneered.) 

# Twitter

While Twitter is hardly, as yet, in the same league as Apple, Google, Microsoft, or Facebook, their dominance of the real time web has been game changing. They have a large and growing developer ecosystem, and a minimalist mindset that leads to rapid evolution. Twitter is increasingly used as transport for other kinds of data, and Twitter analytics are pointing the way towards other kinds of real-time intelligence. 

# VMware

At first glance, VMware might look like a niche player. Yes, they are the leader in application virtualization, and by virtue of that, a leader in corporate cloud computing. VMware's strategy appears to be based on making it easy for applications to migrate between cloud providers, and creating an easy interface between private and public clouds. 

But is that enough? 

But anyone who knows Paul Maritz knows that this is a man who understands the dynamics of internet data. While at [PiCorp](http://blog.seattlepi.com/venture/archives/132400.asp), the startup he founded after leaving Microsoft in 2000, he was focused on a vision of shared data in the cloud. "Why would you want to have your data in the cloud?" he told me in a private conversation some years ago. "For the same reason you keep your money in the bank rather than under your mattress. It becomes more valuable when it's kept with other people's data." 

And as Scott Yara, founder and chairman of Greenplum, the massively multiprocessor Postgres database (disclosure: I am an advisor) pointed out to me when describing Greenplum's [Chorus](http://www.greenplum.com/products/chorus/) offering, it is not in fact Google that has the world's largest data repository. The New York Stock Exchange, T-mobile, Skype, Fox Interactive Media (MySpace), and many others, host their data in Greenplum. The sum of corporate data (sometimes referred to as "the dark web") is far greater than that in any consumer web company. Hence Chorus, Greenplum's platform to enable data sharing between its corporate customers. 

Put in this light, VMware's management of private clouds may turn out to be an unexpected advantage. As companies far from the consumer web become fuller participants in the cloud data operating system, they will rely on facilities that VMware is already building: facilities that allow them to manage the boundaries between private and public data. This data and service segmentation may turn out to be one of the fundamental Internet OS capabilities. 

In addition, VMware's [acquisition of Zimbra](http://www.zimbra.com/about/vmware-acquires-zimbra.html) might be seen as the first step towards acquiring internet data assets of the kind described in this article. Zimbra is an Exchange-compatible email platform; in the right hands it might be used to unlock Microsoft's business-oriented social graph. 

VMware's [acquisition of SpringSource](http://www.vmware.com/company/news/releases/springsource.html) is even more significant. Roman Stanek, CEO of cloud business-intelligence provider [GoodData](http://gooddata.com) (in which I am an investor and a board member) remarked to me that for corporate cloud developers accustomed to programming in Java, Springsource is a kind of "Goldilocks" solution. Amazon's cloud APIs are too low-level; Google's and Microsoft's too high, with too much buy-in to Google's or Microsoft's systems; VMware's are "just right." 

Maritz' long experience at Microsoft drove home to him the importance of developer tools. He understands how platform advantage is built, brick by brick. You can have the best platform in the world, but developer tools are what makes it stick. 

VMware's weaknesses, of course, are many. They lack assets in media, in search, in advertising, in location based services, in speech recognition, and in many other areas that are going to be the currency of developers in future. 

But that may not matter. Because there's another competitor in the mix. 

# Small Pieces Loosely Joined

In talking about the Internet Operating System, I've long used Tolkien's "[one ring to rule them all](http://en.wikipedia.org/wiki/One_Ring)" as a metaphor for platforms that seek, like Windows before them, to take control of the entire developer ecosystem, to be a platform on which all applications exclusively depend, and which gives the platform developer power over them. But there is another alternative. Both Linux and the World Wide Web are examples of what I call "small pieces loosely joined" (after [David Weinberger's book](http://www.smallpieces.com/) of the same name). That is, these platforms have a simple set of rules that allow applications to interoperate, enabling developers to build complex systems that work together without central control. 

[](http://radar.oreilly.com/assets_c/2009/11/OneRingLooselyJoined.html)

Apple, Google, and Microsoft all seem to be plausible contenders to a one-ring strategy. Facebook too may want to play that game, though they lack the crucial mobile platform that each of the others hopes to control. 

But it seems to me that one of the alternative futures we can choose is a future of cooperating internet subsystems that aren't owned by any one provider, a system in which an application might use Facebook Connect and Open Graph Protocol for user authentication, user photos, and status updates, but Google or Bing maps for location services, Google or Nuance for speech recognition, Paypal or Amazon for payment services, Amazon or Google or Microsoft or VMware or Rackspace for server hosting and computation, and any one of a thousand other developers for features not yet conceived. 

This is a future of horizontal integration, not vertical integration. This integration is already happening at many levels. Consider music. Virtually every device that reads a music CD relies on Gracenote's CDDB to look up the track names; this is one of the net's oldest and most universally deployed data services. [SonicLiving](http://sonicliving.com/about/api) provides sites from Facebook to Pandora and Loopt with the ability for their users to find upcoming live concerts for artists they like - and to add them to their own calendars via "Universal RSVP." 

Now it's certainly possible that Gracenote and SonicLiving (both private companies) might be acquired by someone looking to consolidate their hold on the infrastructure of online music, but evidence is strong that there will be countless "point" solutions like these that will be consumed by developers. 

The Internet Operating System may end up looking more like a Linux distribution than a Microsoft or Apple PC or phone operating system. VMware might perhaps provide a cloud computing "kernel" while Facebook provides a social UI layer, Google or Bing provide alternate search subsystems, Android and iPhone and Nokia and the next generation of Windows Mobile provide mobile phone front-ends, and so on. 

The [VMForce](http://www.vmforce.com/) announcement, which combines elements of VMware and Salesforce's respective offerings into a single developer platform, is a good sign of things to come, as companies who aren't holding on to the vision of a single vertically-integrated platform find it in their interest to work together. 

As Benjamin Franklin [so memorably said](http://www.ushistory.org/valleyforge/history/franklin.html), just before signing the American Declaration of Independence: ""We must, indeed, all hang together, or most assuredly we shall all hang separately." Developers will need to make a choice between adopting any single platform, or pushing for open systems that allow interoperability and choice. 

In the short term, I believe we'll see heightened competition, shifting alliances, and a wave of innovation, as companies fight for advantage in delivering next generation applications, and then use those applications to drive adoption of their respective platforms. 

The key question, to my mind, is which of the "big four" (Apple, Google, Microsoft, and Facebook) will most strongly adopt the horizontal, open strategy. 

Apple is the least likely. They have made a compelling case for vertical integration; what's more, they have made it work. 

Microsoft seems like an unlikely ally of an open internet strategy given their history and heritage, but necessity is a good teacher. 

Facebook has made [selective moves towards openness](http://radar.oreilly.com/2010/04/why-f8-was-good-for-the-open-w.html). As their partnership with SonicLiving demonstrates, they consume web services from others as well as produce them. And while [critics have argued that Facebook's recent open announcements don't go far enough](http://www.facebook.com/Timoreilly?v=wall&story_fbid=421421816116), it's clear to me that Facebook gains more than it loses by cooperating with everyone from PayPal and VMware to Microsoft to strengthen their hand. 

Google has made [strong, public commitments to the values of the open web](http://googleblog.blogspot.com/2009/12/meaning-of-open.html). Critics have pointed out, quite rightly, that [For Google, The Meaning Of Open Is When It's Convenient For Them](http://techcrunch.com/2009/12/22/google-open-when-convenient/). 

But frankly, this is true of any company balancing open and proprietary strategy. Does anyone doubt that IBM's commitment to open source software was gated on corporate advantage? Or that companies from Red Hat to MySQL have added proprietary elements to a core open source strategy? 

In the end, companies make decisions about open versus closed and proprietary on competitive grounds. The art of promoting openness is not to make it a moral crusade, but rather to highlight the competitive advantages of openness, and to knit together the strategies of companies who might otherwise find themselves left out of the game. 

This, by the way, is the backdrop for the discussion at this year's [Web 2.0 Expo](http://www.web2expo.com) and especially [Web 2.0 Summit](http://www.web2summit.com). While the term "Web 2.0" has come to mean many things to many people, for me it's always been the story of what happens when you treat the internet, not any individual computer, as the platform. The Expo focuses on the technical infrastructure of the platform; the Summit focuses on the business models and the business strategy. 

As John Battelle notes in his post [Points of Control](http://battellemedia.com/archives/2010/03/the_2010_web2_summit_theme_points_of_control), "Fifteen years and two recessions into the commercial Internet, it’s clear that our industry has moved into a new competitive phase - a “middlegame” in the battle to dominate the Internet economy. To understand this shift, we’ll use the Summit’s program to map strategic inflection points across the Internet landscape, identifying key players who are battling to control the services and infrastructure of a websquared world." 

# Handicapping the Players

This post provides a conceptual framework for thinking about the strategic and tactical landscape ahead. Once you understand that we're building an Internet Operating System, that some players have most of the pieces assembled, while others are just getting started, that some have a plausible shot at a "go it alone" strategy while others are going to have to partner, you can begin to see the possibilities for future alliances, mergers and acquisitions, and the technologies that each player has to acquire in order to strengthen their hand. 

I'll hope in future to provide a more thorough drill-down into the strengths and weaknesses of each player. But for now, here's a summary chart that highlights some of the key components, and where I believe each of the major players is strongest. 

[](http://radar.oreilly.com/upload/2010/04/Chart%20Illustration%201-4.png)

(Note that this chart is influenced by one that Nick Bilton of the New York Times [put together last January](http://bits.blogs.nytimes.com/2010/01/22/a-big-picture-look-at-google-microsoft-apple-and-yahoo/).) 

The most significant takeaway is that the column marked "other" represents the richest set of capabilities. And that gives me hope.
