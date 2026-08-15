---
title: "The Social Network Operating System"
person: tim-oreilly
section: by
type: blog-post
year: 2007
date: 2007-10-12
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/archives/2007/10/social_network_operating_system.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# The Social Network Operating System

## Full text

People have been talking about Facebook as the "social network operating system." At the [Graphing Social Patterns](http://www.graphingsocial.com) conference the other day, I talked a bit about why, for that statement to be true, Facebook will have to focus on interoperability with other providers of social graph data -- and I don't particularly mean other explicit social networking sites like MySpace. 

Every explicit social networking site, which is trying to reconstruct my social network by asking me to invite people and approve their invitations, is crying out for access to my true social network, which (to the extent it exists online) is locked up in applications that don't think of themselves as social networking applications at all. I'm talking about my email (which [Xobni](http://www.xobni.com) is starting to make available), my phone company's call history database, my corporate directory, my address book, my CRM system, and so on. 

Let me make this concrete with the example I gave at the conference. Consider this recent spate of friend confirmation requests from Facebook: 

[](http://radar.oreilly.com/facebookconfirm.html)

Now, why should I have to confirm these requests manually? [geni.com](http://www.geni.com) and [freebase](http://www.freebase.com) both know that Sean O'Reilly is my brother. My company directory could confirm that Laurie Petrycki and Mike Loukides work for O'Reilly. Working with more unstructured data, Google or even Flickr could identify that I know Danese Cooper. She's spoken at many of my conferences, edited books for my company, and worked publicly with me for years on open source related issues. 

The move from manual confirmation to automated recognition is one of the major trends that has allowed the web to scale from early manual web directories like [GNN](http://en.wikipedia.org/wiki/Global_Network_Navigator) to smart search engines like Google. Social networking needs to follow the same path, discovering data about my social relationships, and not just asking me about them. 

This is why I'm excited about the initiative started by Brad Fitzpatrick and David Recordon to push for [social network portability and interoperability](http://bradfitz.com/social-graph-problem/), the "open social network graph," so to speak. The only way we'll get to a truly comprehensive "social network operating system" is by defining protocols that will let everyone who has social networking data, from general purpose friending sites like facebook, to special purpose sites like geni and dopplr, to corporate directories, to interoperate via a set of clearly defined interfaces. 

Such a system might have some of the characteristics of the DNS. Just as each machine has a unique ID, so might a person. (Maybe an email ID is a sufficient handle. Even though many people have multiple email IDs, it seems pretty clear that there's momentum towards an email address being a universal login identifier, whether via OpenID or some other mechanism.) That person could maintain their own identity record -- this is who I am, this is who I'm also known as, this is who has verified information about me -- or they could delegate this to some other provider. That provider should be able to give granular access to known data structures that define a person. (Freebase's people records are a good model.) That way, I can look up information that is guaranteed to be correct (barring spoofing). 

It's also important to recognize that "the social networking operating system" is really just a subsystem of the larger internet operating system that we're building or evolving, and perhaps it's even just a part of the identity subsystem, which also includes other components like payment (Paypal, Google Checkout, Amazon Payments, and of course the credit card ecosystem itself are all potential players here), and various elements of personal history and preference such as my purchase history at Amazon and other online retailers, my search history at Google, etc. 

If I wanted to own the social networking operating system, I wouldn't enter a winner takes all race to own the biggest social graph. Instead, I'd work as hard as I could to make a user-centric set of tools for managing what I want known about me, and who I'm willing to have know it, as well as underlying libraries for discovering and verifying other authorized sources of information about me and who I know, as well as managing access to and authorization to use that information. [Oauth](http://oauth.net/) may be a step in the right direction. 

We're a long way from there, but there's no question in my mind that that's where the technology wants to go.
