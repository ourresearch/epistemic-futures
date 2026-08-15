---
title: "You Should Be Able to Browse the Web Through Your Own Website"
person: mike-caulfield
section: by
type: blog-post
year: 2016
date: 2016-01-27
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2016/01/27/you-should-be-able-to-browse-the-web-through-your-own-website/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# You Should Be Able to Browse the Web Through Your Own Website

## Full text

Making a quicker pass at the [reply to Dave Winer](<http://hapgood.us/2016/01/27/json-based-transclusion-and-wordpress-as-the-universal-reader/>) below, I want to call out one radical idea that people don’t get: You should be able to browse the web through your own website.

As an example of this, consider my [Wikity interface](<http://rainystreets.wikity.cc/>) when I’m logged in (if you’re not logged in the interface will be missing the edit box):

I use Wikity as a combination social-bookmarking tool and wiki. And I’ve got my site set up in a way that’s efficient for me — I have a Markdown based editor at the top, and then around it I have little Pinterest-like excerpts of my posts. When I want to write something new, or when I read something I want to summarize I usually execute a search to remind me of what I’ve written on it before and then plug stuff into the Markdown box. I scan over these search results and link to them or quote from them as I write.

If I want to alter older posts to link to this, I can quick-edit them on the spot to cross link my new stuff.

I haven’t quite got this part working yet, but the idea is a multi-document editing environment that mimics some of the affordances of federated wiki. Here’s a screenshot of writing an article while updating two other articles to link to the new information (note scroll bars of pages where editing is going on).

But the thing is it’s really lonely in here — the only things I’m working with are the ones I’ve created.

And what I learned from federated wiki is doesn’t have to be like that. If I had a common data format and a set of protocols, I could pull all the articles from my friends into this space, and I could fork them in and work on them, link to them, etc.

In the web as it is, we move, and the data stays put. In a federated web, the data moves and we stay put. Does that make sense?

To me at least, that’s the core dream of federated wiki. But what’s interesting is it’s also the dream of Dave Winer to [reboot the blogosphere](<http://scripting.com/liveblog/users/davewiner/2016/01/26/0934.html>).

You can do some of the above with feeds, of course. But for something like the search-my-network-and-write habits I’ve developed you really need API calls, and if you are going to port things like categories and data and media that are going to be processed by the UI you might as well put it in JSON.
