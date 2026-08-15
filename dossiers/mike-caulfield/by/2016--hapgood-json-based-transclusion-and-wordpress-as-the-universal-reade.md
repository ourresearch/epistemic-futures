---
title: "JSON-Based Transclusion, and WordPress as the Universal Reader"
person: mike-caulfield
section: by
type: blog-post
year: 2016
date: 2016-01-27
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2016/01/27/json-based-transclusion-and-wordpress-as-the-universal-reader/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# JSON-Based Transclusion, and WordPress as the Universal Reader

## Full text

Dave Winer wrote a recent post on, roughly, how to [reboot the Blogosphere](<http://scripting.com/liveblog/users/davewiner/2016/01/26/0934.html>) with JSON. I read it last night and thought I understood it, then read it again this morning and realized I’d missed the core idea of what he was saying. Here’s the relevant graf:

> But there is another approach, to have WordPress accept as input, the URL of a JSON file containing the source code for a post, and then do its rendering exactly as if that post had been written using WordPress’s editor. That would give us exactly what we need to have the best of all worlds. Widespread syndication and control over our own writing and archive. All at a very low cost in terms of storage and CPU.

Maybe I was just a bit tired last night but it’s worth staying on how this is different from other models. The idea here is that your data doesn’t have to be stored in WordPress at all. Dave Winer can make his editor, Ward Cunningham can make federated wiki — but should they want to publish to WordPress site —

See, that’s not quite it either. Because the idea here as I read it is pull, not push. (Dave, correct me if I misunderstand here). The idea is, given certain permissions and compliance with a WordPress API, a WordPress site I have can go out and fetch Dave or Ward’s content and render it up for me in my own blog dynamically.

I’m not sure Dave is going this far, but imagine this as a scenario — I link to Dave on my WordPress blog, but the link makes a double pass.

First, it sees if it can just grab the JSON and render Dave’s post in my WordPress blog. If it can, great. It renders Dave’s page with the links. Links I click on there also attempt to render in my default WordPress environment.

Sometimes links won’t return nice requests for JSON. Those ask me if I want to go outside my reading environment to someone else’s site. If history is any guide, these sites don’t get much traffic, because the answer to that question is often no.

Links that render into your environment could be acted on by your theme functions. Maybe you take a snapshot of something, repost it, index it, annotate it. Over time, there is a market for themes that play nice with other peoples content, or allow people to make the best sense of it.

And of course if you add in feeds….

What this does is move from a situation where we have a couple online RSS readers to a world where every WordPress theme (and there are tensof thousands of WordPress themes) is potentially an RSS reader of sorts. It moves from a world where every theme is potentially a new Facebook or Twitter as well.

It does this because it solves part of the problem Facebook solved for people — it lets us read other people’s stuff in a clean, stable environment that we control. (There are other things as well, but you have to start somewhere).

So why not try this? Turn themes — the killer feature of WordPress — into a way to read other people’s content, and see what happens. WordPress has already made a stab at being the universal publisher, but it could be the Universal Reader as well, not through providing a single UI, but by supplying an endlessly customizable one.
