---
title: "Calypso is the Future of Personal Cyberinfrastructure"
person: mike-caulfield
section: by
type: blog-post
year: 2015
date: 2015-11-24
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2015/11/24/calypso-is-the-future-of-personal-cyberinfrastructure/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Calypso is the Future of Personal Cyberinfrastructure

## Full text

OK, so I haven’t used Calypso. I don’t own a Mac, and I’ve been working on other things. But I read Matt Mullenweg’s post on the [introduction of the tool](<http://ma.tt/2015/11/dance-to-calypso/>) and [Ben Werdmüller’s excellent take](<http://werd.io/2015/why-wordpresss-new-calypso-interface-is-genius>) on that post, and ultimately the current experience offered by that tool doesn’t matter. What matters is the  _separation of concerns_ , a separation that will ultimately allow a vastly larger portion of the public to own, manage, and innovate around their own data.

I wrote about this issue in a post in March 2014 called [The Route to Personal Cyberinfrastructure Is Through Storage-Neutral Apps](<http://hapgood.us/2014/03/31/the-route-to-personal-cyberinfrastructure-is-through-storage-neutral-apps/>), and what a difference a year and a half makes. I think people in the ed-tech community back then thought I was a bit utopian (Ryan Brazell [summarized the discussion](<http://ryanbrazell.net/caring-about-the-now/>) back then), or worse, corporatist. But let’s recap:

Right now you have a couple elements to a web application:

  * Your data: the database and file structure, along with the server that serves it up.
  * Your admin interface: the software that allows your to manipulate the data. Add, edit, delete, tweak settings, etc.
  * Your presentation layer: the layer that exposes and shares your stuff to unprivileged users on the web.

And right now these things are bundled together. If I want to own my data, I have to run the admin interface and presentation layer on my own server. This means dealing with updates, hackers, spam, denial of service attacks, etc. It sucks, and only a sliver of the population will ever do it, no matter how nice you make cPanel.

On the other hand, if I want someone to do the heavy lifting around web application maintenance and the the like, I’ve got to move all my data to their server.

As I said last year, this is an incredibly lousy choice, and it’s the real thing that is holding personal cyberinfrastructure back. People want to own their data and their namespace but they don’t want to run servers to do it.

What’s the solution? Separate the elements. Treat your personal server as a BDS (Big Dumb Server), there to answer API calls and file requests. Move the admin interfaces up towards the client, and maintain them centrally the way apps are maintained. Eventually, move the presentation layer towards the client too, allowing readers power over how they consume the data on your server.

This ultimately gives everyone more power.

  * I can host data on Reclaim Hosting without ever having to do any admin or posting through their server front end. I also get out of the software maintenance business.
  * The admin software doesn’t care if I am on a WordPress.com blog or self-hosted blog — it’s just a tool making calls to servers. (This is the storage neutral part of “storage-neutral app”)
  * Ultimately reading (the presentation layer) also becomes separate, and readers get the power to read things in a form that makes sense to them, rather than be beholden to the wishes of writers. (This is less developed in Calypso, but the built-in reader seems like a start).

We give power and responsibility to writers, readers, and software providers over the things that matter to each of them, rather than insist on all or nothing solutions. And if you want to get to broad acceptance of the personal cyberinfrastructure vision, *this* is how it happens.

There are, of course, issues to be addressed, and I can talk about some of those later. But for now, I guess I’m just glad to have an example we can bat around so people can grasp the concept and start thinking about the future we want to have.
