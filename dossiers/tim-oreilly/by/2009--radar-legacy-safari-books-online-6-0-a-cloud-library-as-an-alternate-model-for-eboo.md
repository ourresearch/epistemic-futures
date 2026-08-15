---
title: "Safari Books Online 6.0: A Cloud Library as an alternate model for ebooks"
person: tim-oreilly
section: by
type: blog-post
year: 2009
date: 2009-10-28
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/2009/10/safari-books-online-60-a-cloud.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# Safari Books Online 6.0: A Cloud Library as an alternate model for ebooks

## Full text

There has been a lot of attention paid to ebooks lately, and for good reason. Electronic books are portable, searchable, and more affordable than print books. The web has accustomed readers to having the latest information at their fingertips; we all ask why books should be any less available "on demand."

Amazon’s [Kindle](http://amazon.com/kindle) has received the most mainstream attention (with new entries like Barnes & Noble's [Nook](http://www.BarnesandNoble.com/Nook) making dedicated ebook readers into the latest competitive horse-race), but ebooks are taking off even faster on the iPhone and other smart phones. Ebooks are one of the most popular classes of iPhone application. Recent releases of O'Reilly ebooks as iPhone applications have even [outsold the same books in print](http://toc.oreilly.com/2009/08/the-app-store-and-the-long-tail-the-real-drm.html). Direct sales of the [ebook bundles we offer from oreilly.com](http://oreilly.com/ebooks) (PDF, epub, or mobi files) also exceed our direct sales of print books from the site.

Yet our most popular ebook offering by far is often not even thought of as an ebook. [Safari Books Online](http://my.safaribooksonline.com/?portal=oreilly&cid=200910-orm-timblog-60) is an online book and video subscription service, launched in partnership with the [Pearson Technology Group](http://www.informit.com/index.aspx) in 2001. It contains more than 10,000 technical and business books and videos from more than 40 publishers. It has more than 15 million users (including the number of concurrent seats available through libraries and universities); it is now the second largest reseller of O’Reilly books, exceeded only by Amazon.com, and its revenue dwarfs our sales of downloadable ebooks. It's also the most affordable of our ebook offerings for those who are regular consumers of technical content. The average Safari Books Online subscriber uses at least seven books a month, and many use dozens (or even more), yet the monthly price ([depending on the subscription plan](http://my.safaribooksonline.com/subscribe?portal=oreilly&cid=200910-orm-timblog-60subscribe)) ranges from little more than the price of a single downloadable ebook to no greater than that of two or three.

Here’s the rub: most people thinking about ebooks are focused on creating an electronic recreation of print books, complete with downloadable files and devices that look and feel like books. This is a bit like pointing a camera at a stage play and concluding that was the essence of filmmaking!

At O’Reilly, we’ve tried to focus not on the form of the book but on the job that it does for our customers. It teaches, it informs, it entertains. How might electronic publishing help us to advance _those_ aims? How might we create a more effective tool that would help our customers get their job done?

It was by asking ourselves those questions that we realized the advantages of an online library available by subscription. One of the best things about online technical books is the ability to search the full text of a book. How much better would it be to be able to search across thousands of books? Safari Books Online was our answer.

And it just got better. [Safari Books Online 6.0](http://safaribooksonline.com), [released yesterday](http://www.safaribooksonline.com/Corporate/NewsEvents/pressReleaseDetail.php?page=2009_10_27&cid=200910-6dot0-pressrelease-timoreillyblog), brings a new level of ease of use. It’s a complete, bottom-to-top revamping of the original service. The old UI was, to say the least, getting long in the tooth. 

The new UI is slicker and faster, with the kind of drag-and-drop goodness that people expect from a modern web application. In addition, we’ve added some long-requested features, including:

**Improved Interactivity** \-- With 6.0 you can make inline notes, in the actual text you are reading. You can dog-ear or bookmark specific pages. You can highlight text and associate it with notes. When you are done you can print those pages with both your highlights and notes on them. You can scroll non-stop through the pages of a book without any page refresh, or scan a block of pages in thumbnail view to spot the page you are looking for.

**Personalized Folders** \- Rather than having thousands of books and videos organized by us in a single technology topic taxonomy, you can now put together your own organization, grouping books in the categories most useful to you. You can restrict searches to only the books you’ve chosen, and can search within the results of a saved search.

**Collaboration** \- Even better, if you’re a corporate subscriber, you can share your categorization with other members of your company or workgroup. Not only can team members share folders, they can share book reviews, notes and highlights. 

**Smart Folders** \- New books, videos and articles are being added to Safari Books Online all the time. Searches saved as "smart folders" make it easy to keep up with the latest content in your area of interest. We have also improved our search user interface to allow you to search inside the book or in other books without leaving the page you are reading. Switch pages only when you find what you want.

[](http://radar.oreilly.com/upload/2009/10/SafariSmartFolder.png)

  
As you can see, many of these features take advantage of the online medium in ways that aren’t possible with standalone ebooks. To be sure, there are times you want your own offline copy, and in Safari Books Online, you can indeed download books or chapters for offline use. But especially given the rise of the smartphone as an access device, the times when we are truly "offline" are becoming few and far between. The vision with which we started Safari, that of always-on access to a _library_ of technical content, not just to individual ebooks, is now within reach. Safari Books Online can be used on a desktop or laptop computer or [in the browser on a mobile phone](http://m.safaribooksonline.com). Everything is always in sync because your library is in the cloud.

An ebook cloud works the same way the web itself works. It provides ubiquitous access and shared experience.

# Lessons Learned from the development of Safari Books Online

As I outlined above, Safari adopted a "cloud library" model rather than downloadable ebooks as its fundamental design metaphor. I thought it might be worthwhile to understand how we arrived at that decision, as well as some of the other lessons we’ve learned over what is now 22 years of ebook publishing experience. (O’Reilly published its first ebook, _Unix in a Nutshell for Hypercard_ , back in 1987!) With that, a few reflections on lessons learned:

**Embrace and encourage standards.**

In the late 1980s, O'Reilly had developed a series of books on a technology called the X Window System, which was used by all of the large computer workstation vendors (and still remains an important part of Linux.) Many of these vendors were shipping our books as their documentation, and many of them said, "We'd like to do away with printed documentation. We want to ship only online documentation."

They came to us with what they thought was a wonderful value proposition. "Just put your books into our _fill-in the blank_ platform" -- each one of them had its own proprietary system: IBM Info-Explorer, Sun AnswerBook, HP LaserROM. We replied, "This doesn't sound like a very good business to us. We'll find ourselves always chasing all these different formats. We have a better idea. We want to come up with a common format for technical books. You guys all learn to read it." So, we started working with several of the vendors and came up with an open-standards SGML format for technical manuals called [Docbook](http://www.docbook.org/whatis). (SGML was a precursor to XML.)

Perhaps most importantly, working with SGML led us to the World Wide Web. We decided early on that we wanted our ebook strategy to be a web strategy. We built a set of XML to HTML workflows that allowed us to produce multiple output formats from the same source files - a long, painful, and hotly debated process that took far longer to pay off than we expected, as the rest of the industry was slower to adopt ebooks than we were. In the late 1990s, we even offered HTML-based books on CD-ROM, a product line that we called "CD Bookshelves." (These products, which put 5 to 7 related books onto a single CD, were a precursor to Safari Books Online's original "bookshelf" business model.)

Eventually, we realized that we'd have to encourage downloadable ebook standards as well. Recently, we've seen the same format fragmentation that we saw in the early 1990s, where publishers are being asked to support multiple proprietary ebook formats. The XML publishing systems we've built at O'Reilly make it relatively easy to produce multiple formats; other publishers are not so lucky. But more importantly, multiple formats create a real tax on the reader, as ebook vendors work to create customer lock-in.

While we can't control the actions of ebook resellers or other publishers, we can set a good example. That's why O’Reilly today offers downloadable books as [bundles of three popular formats](http://oreilly.com/ebooks), PDF, [epub](http://en.wikipedia.org/wiki/EPUB) (an open XML standard), and mobi (convertible to Kindle.) Currently, Safari Books Online only supports PDF downloads. We’d like to see them offer ebook bundles as well. But more importantly, we’d like to see all vendors supporting epub.

**Work with your competitors.**

One of our mottos at O’Reilly is to "[create more value than you capture](http://radar.oreilly.com/2009/01/work-on-stuff-that-matters-fir.html)." When we launched Safari Books Online, we knew we were working to build an entire industry, not just a new product. 

With this in mind, we reached out to the [Pearson Technology Group](http://informit.com), our biggest competitor, creating Safari Books Online as a joint venture between the two companies. Safari went live with the entire library of O’Reilly and Pearson books. (Pearson imprints include Addison-Wesley, Prentice-Hall, Peachpit, Sams, Que, Cisco Press, and Adobe Press.) Since then, Safari Books Online has added books and videos from nearly every other computer book publisher, including Microsoft Press, Wiley, APress. The Pragmatic Programmers, Manning, and many others.

While we still compete fiercely with Pearson in acquiring new authors and titles, and in selling those books to the public, we cooperate in coming up with new features that we think will help to make Safari Books Online a better product. We each have our own skunkworks for new features (in O'Reilly's case, [labs.oreilly.com](http://labs.oreilly.com)), but once we understand that something works, we encourage Safari to adopt it.

It also turns out that while we cooperate on the technology and design of Safari Books Online, the cloud library model provides ample room for competition at the content level. One of the advantages of Safari Books Online as a separate joint venture is that it is a level playing field for all participating publishers. Remuneration to publishers and authors is based on actual usage of books and videos. This has led to some interesting side-effects, in particular, deeper usage of books that are out of print or in limited availability, [confirming Chris Anderson's long tail theory](http://radar.oreilly.com/2006/05/long-tail-evidence-from-safari.html).

**Electronic publishing requires an ecosystem**

The other key insight that led us to develop Safari was that we realized that for ebooks to succeed, they would need a distribution infrastructure. In 1995, early in the commercialization of the internet, I wrote a paper entitled [Publishing Models for Internet Commerce](http://tim.oreilly.com/articles/pubmod.html). In it, I wrote:

> [Here] are some of the characteristics of the print publishing market that make me think it provides some of the best models for the commercial Internet I'd like to see developed: 
> 
>   * **Barriers to entry are low.** Especially with the advent of desktop publishing, almost anyone can produce a book, a magazine, a newsletter.
> 
>   * **Niches abound.** Over 50,000 books are published each year in the U.S. alone. A major bookselling chain such as Borders keeps literally hundreds of thousands of unique titles in inventory. And despite major industry consolidation,and focus on a small number of bestsellers, there are still thousands of publishers, ranging in size from those who publish only a single book to those who publish thousands. What's more, there are about 3500 general circulation magazines and tens of thousands of newsletters and other limited circulation publications. 
> 
>   * **So do business models.** Books are sold "by the piece." They are also available for free in the library, though in limited circulation. Magazines and newspapers may be had for free (perhaps subsidized by advertising or membership), for a single-copy newsstand price, or for a recurring subscription fee. Prices range from a few dollars to hundreds or even thousands of dollars for specialized newsletters.
> 
>   * **No one "owns" the market, or needs to.** A bestselling book might sell a million copies or so. The largest circulation magazine in the country, the AARP's membership magazine, has a circulation of about 7 million, _Reader's Digest_ about 5 million. No one else comes close. It's possible to have a successful book selling only a few thousand copies, a newsletter a few hundred, and a four color magazine a few tens of thousands.
> 
>   * **The same technology is available to everyone.** No one publisher has a "proprietary edge." No one has a proprietary format. In some cases (consider Bible publishing), the publisher doesn't even have proprietary content!
> 
>   * **There is a rich ecology of mutually successful players.** Authors sell to publishers. Publishers screen material, edit and produce it to add value, develop a marketing campaign, and build a network of distribution relationships to get the book to the ultimate consumer. Publishers may sell books directly to the consumer, through major retailers, and through wholesalers to smaller retailers whom they don't serve directly. Other wholesalers service libraries and corporations--some of whom also order directly. No one has to do it all, and there are opportunities for many players to work together, each making a profit by performing services in a value chain that stretches from the author to the reader.
> 
>   * **Access is universal and non-exclusive.** You don't have to belong to the local bookstore to shop there, and even if you usually buy your books there, you can go across the street if Borders or Barnes & Noble has a better deal. Distribution is spotty--you can't find every book in every store--but with special orders, you can get virtually anything within a few days. You don't find many books that you can only buy through a special outlet.
> 
> 

> 
> These principles continue to guide my thinking about how to commercialize online content. (Despite its age, the whole paper is still worth a read.)
> 
> But I want to focus in on one point from the list above "There is a rich ecology of mutually successful players." In a world where many players are trying to cut others out of the value chain, it's worth remembering that vibrant industries have a rich ecosystem, not a monoculture. And distribution is an important part of that ecosystem. 
> 
> In 2000, I gave a talk entitled [The ecology of ebook publishing](http://tim.oreilly.com/articles/drmtalk.html). I talked about my experiences as a print and online publisher, and what I'd learned about ebooks as a result:
>
>> Even now the web is not a fully developed ecosystem, but you can see that seven years after we started doing commercial Web sites, there is a rich ecology of players who help each other to succeed. There are companies that do analysis of your site traffic. There are companies that serve your ads. There are companies that understand to buy the ads. There are companies that follow the market and track who's got market share. There are people who resell ads on behalf of other people and ad networks. So, over time we developed in the Web space a mini analog to what we had earlier in the print space, which was lots of different companies working together in a kind of business ecology. 
>> 
>> So, with all this as backdrop, I want to just talk a little bit about where we are right now with e-books. I don't know how long all of you have been working with e-books, but I'm now tracing my work in trying to get this puppy to fly, for 12 to 13 years. Actually, 14. Our first e-book was in 1986. And I see that the biggest problem is the lack of an ecology. And ecology is a really good metaphor for thinking about how marketplaces develop.
>> 
>> When you look at, say, ecological reclamations, for example what happened around Mt. St. Helens when it exploded, you have this gradual resurgence of species. One species makes way for another. So primitive plants will break down the rock and gradually make some soil so that something else can take root. There really isn't time to grow mature forests on, say, the bed of just-cool lava. This is also the way ecosystems develop in business. You have to say, "Okay, you've got to break this thing down."
>> 
>> And we're still in that stage for e-books. I know this doesn't really give us a great deal of guidance about what works in the e-book space, but it does give us a lot of guidance about what will not work.
>> 
>> What I think will not work are approaches that try to go it alone....
>> 
>> I believe that distribution systems exist for the same reason that we have alveoli in our lungs. They create surface area. Any of you who have been in publishing know that there are two classes of customers. There are the people who already know that they want your product, who can come to you directly, and then there's the people who are going to encounter your product by chance. For most of book publishing and certainly for most of trade book publishing, the people who are going to encounter your product by chance are far greater in number than the people who are going to seek it out.
>> 
>> Now, I'm in a fortunate end of the business where, for example, a book like [Programming Perl](http://oreilly.com/catalog/9780596000271) is the only book by the author of a program that's very widely used and so people say, "Oh, there's a book out by Larry Wall" and they look for it. There are tens of thousands to buy it and there's a ready-made direct audience. And, certainly, you have people like Stephen King, or Prince, who has done this in the music world, who have already built up an audience over time and who can say, "Hey, come to me directly."
>> 
>> But, for the most part, digital publishing and online publishing systems are going to have to re-create the kind of richness of distribution networks that we see in the print world. 
>> 
>> So, the systems that we provide have to allow for the kinds of behaviors that have supported our print marketplaces. So when you're evaluating an e-book distribution system, you have to ask yourself questions like "Does it have pricing and mechanisms that support pass-through by multiple layers of wholesalers or retailers or distributors?" because you can't assume that you will have a direct relationship with everyone who might want to sell your books. Is there a mechanism for someone to pick up part of the margin? What does pricing look like? If you haven't thought that through, we don't have a viable system, or we have a viable system that will support only direct to consumer sales.  
> 
> 
> As a result of these convictions, we developed a portal strategy that allowed Safari to be skinned and "resold" by each of the participating publishers. We built a direct corporate sales force to call on Fortune 500 companies. We also developed reseller relationships with library wholesalers, training companies, and others who could increase our reach into the marketplace. We even tried (without success) to have Safari subscriptions resold by book retailers like Amazon, Barnes & Noble, and Borders.
> 
> More than 60% of Safari revenue now comes from corporate and library sales; 40% from direct customer sales via the various publisher portals like the ones at [O’Reilly](http://safari.oreilly.com), Pearson’s [InformIT](http://safari.informit.com) and [Peachpit](http://peachpit.safari.com), and [Safari’s own consumer portal](http://safaribooksonline.com)
> 
>   
>  **What Job Do Your Books Do?**
> 
> In order to understand how to succeed with ebooks, it helps to ask the right questions. As I mentioned earlier, the first question is this: what _job_ does a book do? This is not the same for all publishers. If you publish bird identification guides, [WhatBird.com](http://www.whatbird.com/) shows how much more easily you can do your job online, and how you can [do it even better on an iPhone](http://itunes.apple.com/WebObjects/MZStore.woa/wa/viewSoftware?id=308018823&mt=8). If you publish maps and atlases, Google Maps clearly does the same job, and does it better, than a print book.
> 
> Most publishers exploring the ebook market think of so called [ludic reading](http://www.cyberartsweb.org/cpace/111/MDWeb/nellcov.html), that feeling of getting lost in a good book. Jeff Bezos explicitly called this out as one of the [goals of the Kindle](http://www.newsweek.com/id/70983/output/print).
>
>> "The key feature of a book is that it disappears."
> 
> But this isn’t the only reason we read. Years ago, I heard Harvard Business School professor Clayton Christenson explain how different products do different jobs for different customers at different times. He gave an example of a Harvard study done of McDonalds’ milkshakes. Peak sales in the morning were to solitary commuters, whiling away a long commute. Peak sales in the afternoon were to soccer moms hurrying up a pack of kids who’d gotten a visit to McDonalds for a treat after practice. Two different jobs, perhaps two different products: In the morning, thick and slow is good; in the afternoon, a bit quicker to drink might make mom a bit happier.
> 
> I've applied this kind of thinking to our publishing strategy, both in print and online. Our books are used to learn about new technology, to search for task-relevant information, and to a much lesser extent, for entertainment. As a result, you'll see a clear bifurcation in our publishing program between books that are primarily used for reference, like the [Cookbook series](http://cookbooks.oreilly.com), versus those that are used for learning, like the [Head First series](http://headfirst.oreilly.com), or those that are read for fun, like [Make: magazine](http://makezine.com). And in online publishing, we built Safari Books Online for reference and just-in-time learning, and [the O'Reilly School of Technology](http://www.oreillyschool.com) for structured online learning with live instructors.  
>    
> 
> 
> # Where do we go from here?
> 
> One more important feature being added to Safari is a new, lighter-weight development model. The Safari team has been working with Eric Ries of [the Lean Startup](http://startuplessonslearned.com) fame to adopt the kind of constant improvement that characterizes the best web applications. From here on out, we’ll be adding new features and functionality, and improving the interface, on an ongoing basis rather than in massive stair-stepped releases.
> 
> And yes, there are lots of features I’d like to see, including:
> 
>   * More cross-book links provided by publishers (and the ability for readers to make their own links across the site) 
> 
>   * An improved version of the commenting features in [Rough Cuts](http://my.safaribooksonline.com/roughcuts), Safari Books Online’s early access program for books under development. (You can see one experimental system, O’Reilly’s [Open Feedback Publishing System](http://labs.oreilly.com/ofps.html) at [O’Reilly Labs](http://labs.oreilly.com).) 
> 
>   * Support for multi-format downloadable ebooks. Right now, Safari Books Online users can download PDFs. I’d like to see Safari support epub and mobi (Kindle) file formats as well. In addition, I’d like to make the purchase of offline copies less cumbersome than provided by the current token system. (Subscribers receive a certain number of free tokens each month and can purchase additional tokens. Each publisher sets its own price in tokens for downloads.)
> 

> 
> Please leave your own suggestions for improvements in the comments.
> 
>   
>
