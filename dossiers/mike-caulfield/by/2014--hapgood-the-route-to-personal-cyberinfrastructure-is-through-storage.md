---
title: "The Route To Personal Cyberinfrastructure Is Through Storage-Neutral Apps"
person: mike-caulfield
section: by
type: blog-post
year: 2014
date: 2014-03-31
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2014/03/31/the-route-to-personal-cyberinfrastructure-is-through-storage-neutral-apps/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# The Route To Personal Cyberinfrastructure Is Through Storage-Neutral Apps

## Full text

Jim’s got a great summary of the [larger idea behind UMW Domains](<http://bavatuesdays.com/reclaim-the-handout/>) ([written by Ryan Brazell](<http://ryanbrazell.net/umw-domains-at-aacu/>)) up on his site. The core idea — personal cyberinfrastructure — is one I buy into, but at the same time the current mechanisms for it (cPanel, personal servers, and the like) seem clunky and not poised for greater adoption (although I watch the [Thali project](<http://thali.codeplex.com/>) with interest).

Rather, the route to personal cyberinfrastructure is likely to run through storage-neutral apps. Briefly, the way most apps work now is that there is a program on your tablet/desktop/phone that is owned by Company A, and then there is often a certain about of web storage used by that used by that app, also owned by Company A. There’s a certain amount of web-based processing, also done on servers owned by Compnay A. This is somewhat different than the PC model, where Adobe sold you software but you owned the disk that held all your image creations, Microsoft sold you MS Word but your computer ran it, etc.

The cPanel-as-infrastructure response to that is to move to an all-web-app where you own the server. Some of the apps have mobile extensions to them, but by and large you avoid the lock-in of both modern web apps (Google Docs, Dropbox, Tumblr) and modern apps by going to open, HTML-based web apps.

This works, but it seems to me an intermediate step. You get the freedoms you want, but the freedoms you care about are actually a pain in the ass to exercise. Klint Finley, in[ a post on what a new open software movement might look like](<http://techcrunch.com/2013/04/06/where-the-free-software-movement-went-wrong-and-how-to-fix-it/>), nicely summarizes the freedoms people actually want from most applications (as opposed to content):

>   * Freedom to run software that I’ve paid for on any device I want without hardware dongles or persistent online verification schemes.
>   * Freedom from the prying eyes of government and corporations.
>   * Freedom to move my data from one application to another.
>   * Freedom to move an application from one hosting provider to another.
>   * Freedom from contracts that lock me in to expensive monthly or annual plans.
>   * [Freedom from terms and conditions that offer a binary “my way or the highway” decision](<http://techcrunch.com/2012/08/13/putting-an-end-to-the-biggest-lie-on-the-internet/>).
> 

You get all those freedoms from the web-app personal cyber infrastructure, but you get them because you do all the work yourself. Additionally, your average user does not care about some of the hard-won freedoms baked into things like WordPress — the ability to hack the code (we care about that very much, but the average person does not). They really just want to use it without being locked forever into a provider to keep their legacy content up.

What I think people want (and what they are not provided) is a means to buy software where others do all this work for you, but you hold on to these freedoms. And assuming we live in a market that tries to match people with products they want (big assumption) the way that will come about is storage neutral net-enabled apps. I’ll own virtual server space and cycles somewhere (Amazon, Google, Microsoft, Squarespace, wherever). I’ll buy apps. But instead of installing software and data on the app-provider’s server, they’ll install to my stack on the web. And because they’ll encrypt that data, the company that runs my server won’t be able to see it either. My subscription to Adobe or Word will operate much like older subscriptions. Subscription will get me updates, but at any given point I stop paying Adobe I can still run my web app on my server in the state it was in when I stopped paying them.

Why is this more possible than the open web app model? None of the major providers have much incentive to go this route. Subscriptions are a lucrative business with undreamed of lock-in potential. I would say there are two reasons. First, companies with a virtual server platform (Microsoft, Google, Amazon) have some incentive to promote this model. Even Apple has a chance here to pair its app store with virtual server space. Second, and more importantly, such a scheme would be a huge boon to small developers and hackers. Knowing that they don’t have to scale up server architecture to sell server-powered apps frees them to focus on the software instead of scalability, the way that API-rich operating systems allowed previous generations of developers to focus on their own core product. And as this broadens out to where everyone’s phone has a slice of supercomputer attached to it, some really neat things become possible: truly federated wikis where pages are spread across multiple personal sites, music software that can write down effect-laden tracks in near real-time using rented processor time, music library apps written in 200 lines of code. That’s the larger win, and that’s where we want to be heading, the place where practical user freedoms and developer capabilities meet.
