---
title: "Stuffing Six Million Pages Down Google's Throat"
person: tim-oreilly
section: by
type: blog-post
year: 2008
date: 2008-01-21
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/archives/2008/01/limits_google_crawl_markmail.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# Stuffing Six Million Pages Down Google's Throat

## Full text

I got two fascinating emails from [Jason Hunter](http://xqzone.marklogic.com/people/jason_hunter/) over the weekend, both concerning [MarkMail](http://www.markmail.org), the open source mailing list search engine created by Ryan Grimm and Jason over at [MarkLogic](http://www.marklogic.com). I thought I'd share them, with Jason's permission. 

The first was a fairly prosaic announcement: 

> In the last few weeks we loaded the PHP and PEAR mailing lists, a sum total of about 700,000 new messages. Contained within the new load is the php-general list, now statistically our largest list at 266,000 messages, passing by the old king tomcat-users with its 225,000 messages. Third place now goes to the main MySQL list. 

It's great to know that you can now search these lists with the amazing MarkMail tools, which [I wrote about recently on Radar](http://radar.oreilly.com/archives/2008/01/markmail_opensource_search.html). But what really caught my attention was Jason's next message, a bit of backchannel conversation that illuminates just how poorly the big search engines index small sites with large collections of data: 

> I thought you might find this interesting. One of the challenges we face with MarkMail is how to get Google to crawl all 6m (and eventually more) pages we have on our site. You often hear people talking about ways to increase their small site's PageRank, but you don't find many people talking about the challenge of stuffing Google full of (good) content. 
> 
> Observations so far: 
> 
>   * Google is way ahead of the other search engines. Based on doing site:markmail.org queries: Google has indexed 760k pages, Yahoo 19k, and MSN 4k. It's not just the search algorithm that matters, it's also the crawl algorithm, and we have a clear winner here. 
> 
>   * Google started crawling right from the get-go. We peaked at 960k pages indexed about a week ago. The number goes up and down but the 1m line seems a tough one to crack. 
> 
>   * It is definitely possible to crack 1m. My old email archive system on [Servlets.com](http://www.servlets.com) stands at 1.3m pages indexed. [Gmane](http://gmane.org) has 2.5m indexed. 
> 
>   * This may be an impossible challenge. GMane has 2.5m messages indexed by Google but more than 50m messages archived. 
> 
>   * We theorize that Google judges a site on various factors and crawls accordingly. Based on the fast crawl speed in our earliest days, we think "momentum" is a factor besides just raw PageRank. 
> 
>   * We also theorize that faster page response times might help keep the crawl rate up. There's only 86,400 seconds in a day so to have 250k pages crawled means the Googlebot needs to hit your site three times a second. We expect the bot slows down if a site seems sluggish.
> 

> 
> Attached is a picture of the pages crawled each day for the last 50 days (we don't have stats for the first few weeks). It's widely variable. Notice the happy increase this last week. That might be due to your blog entry giving us some extra [whuffie](http://en.wikipedia.org/wiki/Whuffie). Or maybe it's due to the 30x speed optimization we made in response to your post to better handle the traffic. Or maybe it's just random. I wish I knew. [_links added by me_] 

Jason's last point seems particularly insightful. There are only so many seconds in a day, and the larger the number of pages on a site, the harder a crawler would have to hit the site to index them all while keeping reasonably up to date copies. Small sites with lots of pages thus provide an impedance mismatch for crawling. Obviously, with Google showing 58.4 million pages in response to "site:myspace.com", and 73.3 million in response to "site:flickr.com", a high performance site justifies a high performance crawl, so the question is how Google makes the decision how deep to go. (Interestingly, "site:facebook.com" shows only 906K pages, suggesting that a huge proportion of Facebook's pages are still private.) 

It does seem to me, though, that since most of the pages in mail archives are old pages, and not changing, some smarter algorithms that recognize the nature of these sites versus, say dynamic collections of potentially updated pages like flickr or myspace, might figure out how to do a purely incremental crawl, rather than re-crawling the pages over again. After all, archive sites like gmane and markmail have realized that they don't need to keep re-crawling archived mail messages. Why can't the big guys figure this out too, especially when someone else has done the work of collecting all the data? 

Still, I'm reminded of a comment by Ben Bernanke reported in today's New York Times profile, [The Education of Ben Bernanke](http://www.nytimes.com/2008/01/20/magazine/20Ben-Bernanke-t.html?_r=1&bl&ex=1200891600&en=8236dd75f73e1b26&ei=5087%0A&oref=slogin), that he is "a believer in the laws of mathematics." I've become increasingly fascinated by the underlying math of Web 2.0 since [reading Jeremy Liew](http://radar.oreilly.com/archives/2007/03/the_economics_o_3.html)'s post about [the economics of online advertising](http://lsvp.wordpress.com/2007/02/26/three-ways-to-build-an-online-media-business-to-50m-in-revenue/) last year. Limits are, of course, made to be broken. But it's worth thinking about absolute (and temporary) limits to the growth of Web 2.0. What constraints do we take for granted? What constraints are invisible to us? Your thoughts welcome.
