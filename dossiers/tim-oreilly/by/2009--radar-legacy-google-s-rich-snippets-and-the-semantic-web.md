---
title: "Google's Rich Snippets and the Semantic Web"
person: tim-oreilly
section: by
type: blog-post
year: 2009
date: 2009-05-14
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/2009/05/google-rich-snippets-semantic-web.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# Google's Rich Snippets and the Semantic Web

## Full text

There's a long-time debate between those who advocate for [semantic markup](http://en.wikipedia.org/wiki/Semantic%20publishing), and those who believe that [machine learning](http://en.wikipedia.org/wiki/Machine%20learning) will eventually get us to the holy grail of a Semantic Web, one in which computer programs actually understand the meaning of what they see and read. Google has of course been the great proof point of the power of machine learning algorithms. 

Earlier this week, Google made a nod to the other side of the debate, introducing a feature that they call "Rich Snippets." Basically, if you mark up pages with certain [microformats](http://en.wikipedia.org/wiki/Microformat) ( and soon, with[ RDFa](http://en.wikipedia.org/wiki/RDFa)), Google will take this data into account, and will provide enhanced snippets in the search results. Supported microformats in the first release include those for people and for reviews. 

So, for example, consider the snippet for the Yelp review page on the Slanted Door restaurant in San Francisco: 

[](http://radar.oreilly.com/upload/2009/05/slanteddoor.png)

The snippet is enhanced to show the number of reviews and the average star rating, with a snippet actually taken from one of the reviews. By contrast, the Citysearch results for the same restaurant are much less compelling: 

[](http://radar.oreilly.com/upload/2009/05/citysearch.jpg)

(Yelp is one of Google's partners in the rollout of Rich Snippets; Google hopes that others will follow their lead in using enhanced markup, enabling this feature.) 

Rich snippets could be a turning point for the Semantic Web, since, for the first time, they create a powerful economic motivation for semantic markup. Google has told us that rich snippets significantly enhance click-through rates. That means that anyone who has been doing SEO is now going to have to add microformats and RDFa to their toolkit. 

Historically, the biggest block to the Semantic Web has been the lack of a killer app that would drive widespread adoption. There was always a bit of a chicken-and-egg problem, in which users would need to do a lot of work to mark up the data for the benefit of others before getting much of a payoff themselves. But as Dan Bricklin remarked so insightfully in his 2000 paper on Napster, [The Cornucopia of the Commons](http://www.bricklin.com/cornucopia.htm), the most powerful online dynamics are released not by appeals to volunteerism, but by self-interest: 

> What we see here is that increasing the value of the database by adding more information is a natural by-product of using the tool for your own benefit. No altruistic sharing motives need be present... 

(Aside: [@akumar](http://twitter.com/akumar), this is the answer to [your question on Twitter](http://twitter.com/akumar/statuses/1776298307) about why[ in writing up this announcement](http://radar.oreilly.com/2009/05/google-announces-support-for-m.html) we didn't make more of Yahoo!'s prior support for [microformats in searchmonkey](http://developer.yahoo.com/searchmonkey/smguide/semantic_web.html). You guys did pioneering work, but Google has the market power to actually get people to pay attention.) 

What I also find interesting about the announcement is the blurring line between machine learning and semantic markup. 

Machine learning isn't just brute force analysis of unstructured data. In fact, while Google is famous as a machine-learning company, their initial breakthrough with [pagerank](http://en.wikipedia.org/wiki/Pagerank) was based on the realization that there was hidden metadata in the link structure of the web that could be used to improve search results. It was precisely their departure from previous brute force methods that gave them some of their initial success. Since then, they have been diligent in developing countless other algorithms based on regular features of the data, and in particular regular associations between data sets that routinely appear together - implied metadata, so to speak. 

So, for example, people are associated with addresses, with dates, with companies, with other people, with documents, with pictures and videos. Those associations may be made explicitly, via tags or true structured markup, but given a large enough data set, they can be extracted automatically. Jeff Jonas calls this process "[context accumulation](http://jeffjonas.typepad.com/jeff_jonas/2006/08/accumulating_co.html)." It's the way that our own brains operate: over time, we make associations between parallel data streams, each of which informs us about the other. Semantic labeling (via language) is only one of many of those data streams. We may see someone and not remember their name; we may remember the name but not the face that goes with it. We might connect the two given the additional information that we met at such and such conference three years ago. 

Google is in the business of making these associations, finding pages that are about the same thing, and they use every available handle to help them do it. Seen in this way, SEO is already a kind of semantic markup, in which self-interested humans try to add information to pages to enhance their discoverability and ranking by Google. What the [Rich Snippets announcement](http://googlewebmastercentral.blogspot.com/2009/05/introducing-rich-snippets.html) does is tell webmasters and SEO professionals a new way to add structure to their markup. 

The problem with explicit metadata like this is that it's liable to gaming. But more dangerously, it generally only captures what we already know. By contrast, implicit metadata can surprise us, giving us new insight into the world. Consider Flickr's [maps created by geotagged photos](http://code.flickr.com/blog/2009/01/12/living-in-the-donut-hole/), which show the real boundaries of where people go in cities and what they do there. Here, the metadata may be added explicitly by humans, but it is increasingly added automatically by the camera itself. (The most powerful [architecture of participation](http://www.oreillynet.com/pub/a/oreilly/tim/articles/architecture_of_participation.html) is one in which data is provided by default, without the user even knowing he or she is doing it.) 

Google's [Flu Trends](http://www.google.org/flutrends/) is another great example. By mining its search database (what John Battelle calls "[the database of intentions](http://battellemedia.com/archives/000063.php)") for searches about flu symptoms, Google is able to generate maps of likely clusters of infection. Or look at Jer Thorp's fascinating project announced just the other day, [Just Landed: Processing, Twitter, MetaCarta & Hidden Data](http://blog.blprnt.com/blog/blprnt/just-landed-processing-twitter-metacarta-hidden-data). Jer simulated the possible spread of swine flu built by extracting the string "Just landed in..." from Twitter. Since Twitter profiles include a location, and the object of the phrase above is also likely to be a location, he was able to create the following visualization of travel patterns: 

[Just Landed - Test Render (4 hrs)](http://vimeo.com/4583713) from [blprnt](http://vimeo.com/user313340) on [Vimeo](http://vimeo.com).

This is where the rubber meets the road of collective intelligence. I'm a big fan of structured markup, but I remain convinced that even more important is to discover new metadata that is produced, as Wallace Stevens so memorably said, "[merely in living as and where we live](http://www.oreillynet.com/pub/a/oreilly/tim/articles/favebooks_0705.html)." 

P.S. There's some small irony that in its first steps towards requesting explicit structured data from webmasters, Google is specifying the vocabularies that can be used for its Rich Snippets rather than mining the structured data formats that already exist on the web. It would be more "googlish" (in the machine learning sense I've outlined above) to recognize and use them all, rather than asking webmasters to adopt a new format developed by Google. There's an interesting [debate about this irony](http://iandavis.com/blog/2009/05/googles-rdfa-a-damp-squib) over on Ian Davis' blog. I expect there to be a lot more debate in the weeks to come.
