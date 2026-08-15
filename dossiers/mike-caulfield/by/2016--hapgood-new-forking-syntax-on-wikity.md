---
title: "New Forking Syntax on Wikity"
person: mike-caulfield
section: by
type: blog-post
year: 2016
date: 2016-03-06
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2016/03/06/new-forking-syntax-on-wikity/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# New Forking Syntax on Wikity

## Full text

Courtesy of Floyd’s coffee shop in downtown Portland, which hasn’t kicked me out yet, we bring you the latest Wikity Weekend Code update.

This weekend’s addition is pretty cool actually. So you know the wiki syntax within Wikity is to use double brackets around the page title to create a link, right, like so:

> [[Poor Sleep and the Munchies]]

But what if you want to link to a remote page? The Wikity way to do that has been to go out, find the page, fork it, and then link to it from the other page. That’s a drag!

So we’ve added a new feature to the syntax. If you put a remote site in the double brackets, and that site returns valid Wikity JSON, the server will go out, copy the remote Wikity page for you, pull the title off of the JSON, and replace the link in your page with the title.

Here we enter the link to a remote site:

And then when we submit, the page looks like this:

As you can see, it’s gone and fetched the title from the JSON and fixed it. But even better, if we click it we can see the page has been ported to our site:

Now if you think this through, you realize we’ve also made mass-forking easier. I can now put together a playlist of multiple URLs from all sorts of different sites, submit it, and Wikity will go to work grabbing the copies it needs.

More on that later, they are kicking me out now, and I need to catch a ride out of here anyway. But good times…
