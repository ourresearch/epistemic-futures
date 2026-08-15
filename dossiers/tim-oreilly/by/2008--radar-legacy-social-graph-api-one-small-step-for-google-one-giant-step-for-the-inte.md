---
title: "Social Graph API:  One small step for Google, one giant step for the Internet Operating System"
person: tim-oreilly
section: by
type: blog-post
year: 2008
date: 2008-02-01
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/archives/2008/02/google_social_graph_api.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# Social Graph API:  One small step for Google, one giant step for the Internet Operating System

## Full text

Google's announcement today of the [Social Graph API](http://code.google.com/apis/socialgraph/) is a major step in the development of what I've called "the Internet Operating System." In a nutshell, what the Social Graph API does is to lower the barrier to re-use of information that people publish about themselves on the web. It's the next step towards the vision that Brad Fitzpatrick and David Recordon outlined in [Thoughts on the Social Graph](http://bradfitz.com/social-graph-problem/). 

How many of us feel frustration when we're asked to recreate the same information for each social network? The Social Graph API allows sites to query public data that Google's crawl has exposed about individuals, so that it can be re-used rather than recreated. More importantly, it is based on a vision consistent with what Dick Hardt calls [user-centric identity](http://identity20.com/?p=61). It uses [XFN](http://www.gmpg.org/xfn/join) and [FOAF](http://www.foaf-project.org/2004/you/index.html), so that you can mark up information that is about you. When other sites contain information that claims to be you, a link from one of your sites that contains an appropriate XFN or FOAF assertion will help the Google crawler to aggregate that information about you. 

Google is also providing a simple demo application that can best be thought of as a kind of Social Graph debugger. It's not live yet as I write, but yesterday Brad Fitzpatrick sent me a copy of a page using me as the root of an Social Graph search. 

[](http://radar.oreilly.com/SocialGraph.html)

As you can see here, Brad put in two sites that he was pretty sure were mine, <http://tim.oreilly.com/> and [twitter.com/timoreilly](twitter.com/timoreilly). The API then returns a list of sites that it infers are also mine, either because I've linked to them in a way that indicates they are, or because someone else has done so. So, for example, it concludes that radar.oreilly.com is also my site because tim.oreilly.com, a "me" site, links to it. 

But other sites shown in the second block below are ones that represent only one-way assertions. They may link to me in a way that suggests that they are mine, but since it's not reciprocal, they aren't yet aggregated as "me." (That's why I called this demo a kind of social graph debugger. It allows you to see what Google knows about your social graph, and then to correct it.) 

To include my alternate repositories of identity in my Google-crawled social graph, all I need to do is link to them from a site that is known to be "me." So, for example, if I want to claim my [Technorati profile](http://www.technorati.com/people/technorati/timoreilly), or my [Berlin Web Expo Crowdvine profile](http://web2berlin.crowdvine.com/profiles/162) as me, all I need to do is to link to them with an XFN "rel=me" tag. Meanwhile, I can also see that Google notes that Sarah Milstein has also linked to radar.oreilly.com, but because she isn't me, I won't confirm that as a "me" link. And of course, I can see that Google doesn't seem to know about my public Flickr photo pool, or my public linkedIn or Facebook profiles, or various private profiles like the ones I have on dopplr or goodreads. 

The Social Graph API cleverly bootstraps around the problem that not many sites use XFN or FOAF markup by allowing the API to assume that the root supplied to the API query is a "me" link. 

Now, this demo application is just the beginning. The real goal is to have a site that is asking me for profile information be able to query the social graph to find out where that information already exists. 

It isn't yet comprehensive enough to give those sites fine-grained access to individual profile elements, but you can imagine that that's where it's going... (It would also be great for it to have mechanisms for querying truly private data. The Unix permissions mechanism of "user," "group," and "world" is a good model -- right now, this service traverses only the world-readable social graph. It would be cool to have mechanisms to rupport "group" and "user" level access as well.) 

[](http://radar.oreilly.com/socialgraph3.html) A bit more detail from Google's site and information they provided (click on the image to enlarge it): 

> The Social Graph API looks for two types of publicly declared connections: 
> 
>   1. It looks for all public URLs that belong to you and are interconnected. This could be your blog (a1), your LiveJournal page (a2), and your Twitter account (a3). 
>   2. It looks for publicly declared connections between people. For example, a1 may link to b's blog while a1 and c link to each other.
> 

> 
> This index of connections enables developers to build many applications including the ability to help users connect to their public friends more easily. For example, in the image below, Brad just joined Twitter but has no friends on it. Using the Social Graph API, Twitter could provide Brad a way to find out that his friend Jane is also on Twitter. Here's how: Brad has linked to his homepage (b3) from his Twitter profile (b1) and also from his homepage (b3) to his LiveJournal blog, Bradfitz (b2). On LiveJournal, Brad is friends with Jane274 (j2), but Brad doesn't know that Jane274 (j2) also has a Twitter profile (j1). Since the Social Graph API has indexed that Brad and Jane already have declared a public friendship on LiveJournal, it can let Brad know that he might want to add Jane (j1) on Twitter as well. 

This is REALLY cool, even though it's just a beginning. As I said in the title, a small step for Google, but a huge step towards the [internet operating system](http://www.oreillynet.com/pub/wlg/1262). Most importantly, it's a step that doesn't put the social graph under the control of any one company, but instead provides mechanisms for the user to control what information about him is available to applications. 

Until now, I thought that Amazon was the only company that understood the difference between application level platform APIs and true internet platform services. (To understand the difference, compare [Amazon web services](http://www.amazon.com/gp/browse.html?node=3435361) like the Amazon Associates Web Services to much broader services like S3 and EC2.) 

Facebook's F8 platform, like other first generation Web platform APIs that have taken the world by storm, such as Google Maps, are too tightly integrated with the originating company's own application to enable true distributed innovation. But a real platform service makes it possible for developers to do things entirely outside the realm of the originating provider's application. Unlike OpenSocial, which [I found disappointing](http://radar.oreilly.com/archives/2007/11/opensocial_social_mashups.html), the Google Social Graph API is a game-changing play in the social networking space. It's a huge step towards open standards and a level playing field in smart social apps, and exposes Google's data and infrastructure in a subtle and powerful way. I can't wait to see what comes next!
