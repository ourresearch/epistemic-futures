---
title: "Make Servers Dumb Again"
person: mike-caulfield
section: by
type: blog-post
year: 2017
date: 2017-06-22
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2017/06/22/make-servers-dumb-again/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Make Servers Dumb Again

## Full text

After talking with Jon Udell and re-reading an old post of mine on [storage-neutral web-infrastructure](<https://hapgood.us/2014/03/31/the-route-to-personal-cyberinfrastructure-is-through-storage-neutral-apps/>) I realize I can make an old point much easier. So here goes:

Make Servers Dumb Again.

You’ve heard of the Dumb Terminal, right? The idea that a terminal wouldn’t do anything but display stuff composed on centralized servers?

Well, this is the opposite. I want dumb servers. I want smart front-ends hosted anywhere to make basic data queries to servers. I want those two things — data and display engines — to be run by separate folks, like in the original vision of the web. I store the HTML on my server under my rules. You display it in your browser under yours.

Why do this? Because the marriage of front-ends and data creates lock-in, lousy portability, surveillance models, and crappy incentives for a good user experience.

You can get around that by running your own server, sure. Now you’re still locked into something, but the thing you’re locked into is r _unning your own server forever_ , which is frankly almost as horrifying as being tracked.

I am 100% sure this post will be misunderstood. So I’ll just end with [Klint Finley’s list](<https://techcrunch.com/2013/04/06/where-the-free-software-movement-went-wrong-and-how-to-fix-it/>) of the freedoms _people actually want_.

  * Freedom to run software that I’ve paid for on any device I want without hardware dongles or persistent online verification schemes.
  * Freedom from the prying eyes of government and corporations.
  * Freedom to move my data from one application to another.
  * Freedom to move an application from one hosting provider to another.
  * Freedom from contracts that lock me in to expensive monthly or annual plans.
  * Freedom from terms and conditions that offer a binary “my way or the highway” decision.

You’ll notice that the minute the data provider becomes unhitched from the display and interaction provider all this happens automatically. That makes for a more difficult time programming, but it ultimately gets the people what they want.

Make Servers Dumb Again. There, I said it.
