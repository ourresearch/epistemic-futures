---
title: "MarkMail Provides Amazing Search Capabilities"
person: tim-oreilly
section: by
type: blog-post
year: 2008
date: 2008-01-07
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/archives/2008/01/markmail-provides-amazing-sear.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# MarkMail Provides Amazing Search Capabilities

## Full text

I've been meaning to write for a while about [MarkLogic](http://www.marklogic.com)'s awesome new search tool for trolling through open source mailing lists, [MarkMail](http://www.markmail.org). 

Let's face it. While there may be a new generation that thinks that email is for old fogies, for many of us, email is a primary online tool, at least as important to us as the web. Many of us no longer file documents or attachments -- we just search for them again in our email. Perhaps most importantly, email is a primary collaboration tool--and as many of us have figured out, collaboration is one of the internet's killer apps. Searching our shared memory in a collaborative space is REALLY useful -- with open source mailing lists being a great example. 

Despite its importance, very little has been done to improve on email. The clients we use today are not radically different from what we used ten years ago (except perhaps in being web-based). This is why there was so much excitement when [xobni](http://www.xobni.com) showed how useful it is to expose the social network hidden in email. 

MarkMail does something equally powerful. Imagine a tool that lets you see trends across thousands of email messages, saved over years. Imagine being able to find who is the most prolific poster on a given topic, and explore the histogram of their entire message history. Imagine being able to do instantaneous data mining against millions of stored messages, with a response time better than you get looking at your local mailbox. 

MarkMail provides all this and more. MarkLogic has stored approximately 5.5 million email messages across over 700 plus open source mailing lists -- all of the Apache, MySQL, Mozilla, and PHP lists, plus a smattering of others, with more to be added over time (hopefully soon) -- and provided an interface that beats Googling. It's as fast or faster, but more importantly, you have built-in data mining capabilities that, I trust, will eventually make their way into more traditional email systems. 

Let me show you a sample search. I might be looking for actual message content -- the answer to a question -- but I might be interested in the big picture. As a publisher, my editors are often looking for trend data to tell us whether interest in a topic is increasing or declining. So, for example, let's say we were thinking of publishing a book on [lucene](http://lucene.apache.org/java/docs/). (This is for example only -- there's already a good book from Manning, [Lucene in Action](http://www.amazon.com/exec/obidos/ASIN/1932394281).) But let's take a look at what MarkMail shows us: 

[](http://radar.oreilly.com/MarkMail_Lucene.html)

I can immediately see that there's a _lot_ of growth in mailing list traffic for Lucene. Sounds promising. And I can see who are the most prolific posters. Possible authors? Well, Erik Hatcher, the top poster, is the author of that Manning book I already mentioned. But a few drill-down clicks show whether other top posters are still involved or not. (For an example where someone dropped out, search on Struts and then view the [drill-down histogram for Craig McClanahan](http://markmail.org/search/?q=struts+order%3Arelevance#query:struts%20order%3Arelevance%20from%3A%22Craig%20R.%20McClanahan%22+page:1+state:facets).) And of course, I can drill into the messages themselves to see who expresses ideas concisely and powerfully. (Yes, we do troll mailing lists for authors and conference speakers!) 

And in a feature that old command-line junkies will love, once you want to drill into actual messages, just type "n" to pop into message viewing mode, with "n" and "p" moving you forward and back through the message stream. It's a really slick mail reading interface. As Jason Hunter from MarkLogic put it, their UI model was: 

> 1\. Search with a minimal constraint   
>  2\. Refine interactively until you've narrowed things sufficiently   
>  3\. Hit "n" to peruse the results 

OK, so maybe most of you wouldn't use this tool for trend analysis. But just imagine if you could use a tool like this for searching your own mail? I love the way MarkMail gives me a bunch of drill-down choices in the UI, and as I choose them, rewrites the command-line in the search box. I'd love to see features like this in my other mail packages. With Mail.app on Mac OS X, for example, it's impossible to do a complex search. You can search for a text string in the from field, the subject line, or the entire message, but what if you want to say "I want a message on x, from Joe, to Mary, sent between April and June of 2006." Even on Gmail, where I can do this kind of search with Search Options, I have to go to another whole screen, out of the search flow, to do it. You can construct that kind of a search in MarkMail just by navigating around. Yumm. How long before regular mail vendors start doing this kind of thing? This is a really sweet search interface. 

Where MarkMail really shines is in managing large mail archives. And that's why, of course, MarkLogic has put up MarkMail for free. They know that there are potential corporate clients who have huge mail archives that they want to mine. And the performance of their existing systems (not to mention their interfaces) just won't cut it.
