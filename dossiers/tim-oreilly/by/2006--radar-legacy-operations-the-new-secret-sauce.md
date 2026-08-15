---
title: "Operations: The New Secret Sauce"
person: tim-oreilly
section: by
type: blog-post
year: 2006
date: 2006-07-10
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/archives/2006/07/cloudy_with_a_chance_of_server_1.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# Operations: The New Secret Sauce

## Full text

I spoke last week with [Debra Chrapaty](http://www.microsoft.com/presspass/exec/debrac/default.mspx), the VP of Operations for Windows Live, to explore one of the big ideas I have about [Web 2.0](http://www.oreillynet.com/go/web2), namely that once we move to software as a service, everything we thought we knew about competitive advantage has to be rethought. Operations becomes [the elephant in the room](http://en.wikipedia.org/wiki/Elephant_in_the_room). Debra agrees. She's absolutely convinced that what she does is one of the big differentiators for Microsoft going forward. Here are a couple of the most provocative assertions from our conversation:

  1. Being a developer "on someone's platform" may ultimately mean running your app in their data center, not just using their APIs. 

  2. Internet-scale applications are pushing the envelope on operational competence, but enterprise-class applications will follow. And here, Microsoft has a key advantage over open source, because the Windows Live team and the Windows Server and tools team work far more closely together than open source projects work with companies like Yahoo!, Amazon, or Google.

Let me expand on these two points. Did you ever see the children's book, [Cloudy, With a Chance of Meatballs?](http://www.amazon.com/gp/product/0689707495/) I summarize my conversation with Debra as "Cloudy, with a chance of servers." (I started with a pun on the title, but the book description from Amazon is particularly apt: "If food dropped like rain from the sky, wouldn't it be marvelous! Or would it? It could, after all, be messy. And you'd have no choice. What if you didn't like what fell? Or what if too much came? Have you ever thought of what it might be like to be squashed flat by a pancake? " But I digress. Back to Debra.) 

People talk about "cloud storage" but Debra points out that that means servers somewhere, hundreds of thousands of them, with good access to power, cooling, and bandwidth. She describes how her "strategic locations group" has a "heatmap" rating locations by their access to all these key limiting factors, and how they are locking up key locations and favorable power and bandwidth deals. And as in other areas of real estate, getting the good locations first can matter a lot. She points out, for example, that her cost of power at her Quincy, WA data center, soon to go online, is 1.9 cents per kwh, versus about 8 cents in CA. And she says, "I've learned that when you multiply a small number by a big number, the small number turns into a big number." Once Web 2.0 becomes the norm, the current demands are only a small foretaste of what's to come. For that matter, even server procurement is "not pretty" and there will be economies of scale that accrue to the big players.

Her belief is that there's going to be a tipping point in Web 2.0 where the operational environment will be a key differentiator. I mentioned the idea that Web 2.0 has been summed up as "Fail Fast, Scale Fast," and she completely agreed. When it hit its growth inflection point, MySpace was adding a million users every four days -- not at all an easy feat. As these massive apps become the norm, unless you can play in a game where services can be highly stable, geodistributed, etc., you won't be in the game. And that's where she came to the idea that being a developer "on someone's platform" may ultimately mean running your app in their data center. Why did Fedex win in package delivery? They locked up the best locations with access to airports, warehousing, etc. so they had the best network. A similar thing will happen with packet delivery.

Who are the competitors of the future in this market? Microsoft, Google, Yahoo! and the telcos were the folks she called out, with a small nod to Amazon's platform aspirations. (Sure enough, in true [news from the future](http://www.makezine.com/nff) style, into my inbox comes [Jon Udell's review of a new service called OpenFount](http://weblog.infoworld.com/udell/2006/07/07.html#a1483): "Openfount's big idea is that a solo developer ought to be able to deploy an AJAX application to the web without worrying about how to scale it out if it becomes popular. If you park the application's HTML, JavaScript, and static data files on Amazon's S3 storage service, you can make all that stuff robustly available at a cost that competes favorably with conventional hosting.")

Debra also talked about the importance of standardization, so that increasing capacity is as seamless as possible. "We've got to make it like air and water." In that regard, another very interesting point we discussed was [Ian Wilkes' thought that database tools were still weak when it came to operational provisioning](http://radar.oreilly.com/archives/2006/04/web_20_and_databases_part_1_se.html). That was where she came to the second point above, that Microsoft has a key competitive advantage here. Internet-scale applications are really the ones that push the envelope with regard not only to performance but also to deployment and management tools. And the Windows Live team works closely with the Windows Server group to take their bleeding edge learning back into the enterprise products. By contrast, one might ask, where is the similar feedback loop from sites like Google and Yahoo! back into Linux or FreeBSD? 

As Shakespeare said, "The game's afoot." Debra put more servers into production in the last quarter than she put in place in all of the previous year, and she thinks this is just the beginning. Operations used to be thought of as boring. It's now ground zero in the computing wars.

P.S. When I circulated a draft of this message to the Radar team, Nat wrote: "Open source definitely has this. Linux, FreeBSD, Apache, Perl, Python, and Ruby there's a huge crossover between large-scale deployers and core project members. There's been a lot of talk about how the Linux kernel is now really only developed by people employed full-time by big companies. If you look at Yahoo! or Google, they have a ton of kernel and language people working for them. I think there's a pretty tight loop there." 

I replied, "I know this is true on the core of many projects, but is it true with regard to tools for managing _operations_ , which was Debra's point?"

Nat replied: "Deployment tools have _never_ been open source's strong point: OS has always been about the developer, rarely about the deployer. cf the hacker's disdain for IT who get stuck with deployment and management. That said, there are some open source tools like [nagios](http://www.nagios.org) (for system monitoring) and [capistrano](http://wiki.rubyonrails.org/rails/pages/Capistrano) (for rails deployment). The feedback loop there tends to be that the people writing the tools are the ones with the deployment problem. The downside is that if your need isn't met by the tool, it may be hard to get the developer to add it. (That's why [Hyperic](http://www.hyperic.com) is on good terms with Nagios: the Nagios developer will never add the features that Hyperic has.)"

He continued: "The deployment tools tend to be commercial offerings in open source, where Red Hat, IBM, et al. give away the open source operating system and charge like a wounded bull for the management tools. Walking around LinuxWorld Boston two years ago convinced me of this: _everyone_ had management tools. Third party management tools suffer because of the lack of integration. Red Hat at least can pair the management people with the kernel people and get the integration they want. I'm not ready to believe that the Windows server story is 10/10. I'd say the open source story is only 5/10. There's a lot more to be done."

I do think Microsoft has an advantage here over Linux and LAMP stack. But more to Debra's point, it is outmoded to think of a software stack alone as the platform. Microsoft's competition in this arena is not Linux, but Google, and the other Web 2.0 platform players, who have their own operational competencies, and as far as I know, are _not_ releasing them to the open source community. What's more, I'm not even sure that the open source community understands just how important this whole area is going to be, so even if the tools and techniques were released, I'm not sure how strong the uptake would be. 

Your thoughts?
