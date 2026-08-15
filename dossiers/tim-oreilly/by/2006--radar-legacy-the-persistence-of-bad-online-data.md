---
title: "The Persistence of (Bad) Online Data"
person: tim-oreilly
section: by
type: blog-post
year: 2006
date: 2006-10-30
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/archives/2006/10/the_persistence_of_bad_data.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# The Persistence of (Bad) Online Data

## Full text

One of the looming problems in our data-rich yet decentralized future is the difficulty of fixing bad data, once it is released onto the net. We've heard stories of Facebook profiles that turned up in embarrassing circumstances, identity theft, and so on, but I want to focus on a slightly different problem, one that potentially has a technical solution. And that is the question of who or what is the authoritative source of data on a particular topic.

We face this problem all the time with book metadata in our publishing business. Retailers demand notification of upcoming books as much as six months before the book is published. As you can imagine, titles change, page counts change, prices change -- sometimes books are cancelled -- and corralling the old data becomes a game of [whack-a-mole](http://en.wikipedia.org/wiki/Whac-A-Mole). You'd think that the publisher would be an authoritative source of correct data, but this turns out not to be the case, as some wholesalers and retailers have difficulty updating their records, or worse, retailers sometimes overwrite newer, correct data with older bad data from one of the wholesalers who also supply them. 

A particularly trying case of persistent bad data was brought to my attention a few months ago by [Lou Rosenfeld](http://louisrosenfeld.com/home/), co-author of [Information Architecture for the World Wide Web](http://www.oreilly.com/catalog/infoarch3/index.html). We'd been in discussions with Lou to publish a new book on [search analytics](http://www.rosenfeldmedia.com/books/searchanalytics/). The discussions had progressed as far as an editor issuing a contract for discussion, before Lou decided to launch [his own publishing company](http://rosenfeldmedia.com/).

And that's where the problem started. Issuing a contract at O'Reilly results in various data being added to our own internal tracking databases. When Lou decided to publish his own book, we flagged the book as "cancelled" in our own database. But unfortunately, our system sends out automated notice of cancelled titles via an [ONIX](http://www.bisg.org/onix/index.html) feed -- even cancelled titles that have never been announced. That would have been well and good, except for the fact that someone else's automated system noticed a new book in the cancelled book feed, and added the book to their database -- without the cancelled flag!

(Aside: That's a classic bug cascade. As my friend Andrew Singer once noted, debugging is discovering what you actually told your computer to do, rather than what you thought you told it. Unfortunately, you sometimes don't understand what you told your computer to do until some particular corner case emerges.)

From there, it went from bad to worse. Lou and his co-author Rich Wiggins first let us know about the problem in May, and our folks went to work trying to clear bad data out of the channel. We'd get the data cleared out of some accounts, and then it would reappear, as they repopulated their databases from wholesalers who hadn't yet made the fix. By July, Lou and his co-author Rich Wiggins were getting (politely) irate. Lou wrote:

> I know and appreciate that you've tried to rectify the problem, but now that this data [is] out there, it's propagating, and the problem is getting worse. It's [caused me some frustration](http://louisrosenfeld.com/home/bloug_archive/000461.html), and [my co-author is downright angry](http://wigblog.blogspot.com/2006/07/our-book-on-search-analytics-competing.html).   
> 
> 
> In a sense, this is a form of identity theft, however inadvertent, and will likely have a very damaging impact on our ability to sell the book. As many potential readers know that I'm also an O'Reilly author, they may already assume that O'Reilly is our book's publisher. The incorrect data now in many book catalogs will likely confirm this wrong assumption, and will generally confuse the marketplace.

Unfortunately, despite all our efforts, the bad data remains up at bookstores that ought to be able to fix this, including Powells, Amazon Canada, and Kinokuniya. A Google Search still turns up [56 results](<a) for an ISBN that should never have propagated beyond O'Reilly's internal database.

It's frustrating for Lou and Rich -- although here's hoping we can turn lemons into lemonade by giving them some publicity for the book, [Search Analytics for Your Site: Conversations With Your Customers](http://www.rosenfeldmedia.com/books/searchanalytics/), which they expect to publish in January. In addition to this piece, we're going to have to end up creating a page for the book on oreilly.com, which says that we didn't publish it, and sending them to Rosenfeld Media instead. Now that's not all bad -- I'm happy to be giving Lou some link love, and hope we can send some sales his way -- but it's a real shame that it's not possible just to remove the bad data. As Lou said in one email, "the whole story seems to be such a strong illustration of the downsides of connected and linked databases (and therefore very much a Web 2.0 lesson)."

And the lesson seems to be that you can't ever take anything back. What you have to do is to spread correct information, and hope that it bubbles up more strongly than the incorrect information it's competing with.

But I did hint at the possibility of a technical solution. And I want to propose it here, in lazyweb fashion. It seems to me that a critical part of our future distributed database infrastructure is the development of metadata about data integrity and authority. Looking forward, we do want to expect a world in which automated data feeds replace manual processes. But in that world, we'll also expect that some feeds are more authoritative than others, and that especially for unique data items (such as ISBNs), the owner of that data item would be given precedence over others reporting on the status of that item. 

Tags: [books](http://radar.oreilly.com/tag/books) [data](http://radar.oreilly.com/tag/data) [publishing](http://radar.oreilly.com/tag/publishing) [web 20](http://radar.oreilly.com/tag/web_20)

[Sphere It](http://www.sphere.com/search?q=sphereit:http://radar.oreilly.com/archives/2006/10/the_persistence_of_bad_data.html "Related Blogs & Articles")

## Trackback Pings

TrackBack URL for this entry:  
http://blogs.oreillynet.com/mt/trackback/1433
