---
title: "Capable Clients and the WordPress API"
person: mike-caulfield
section: by
type: blog-post
year: 2016
date: 2016-01-23
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2016/01/23/capable-clients-and-the-wordpress-api/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Capable Clients and the WordPress API

## Full text

**Update:** If you read the comments below you’ll see one of the API developers has responded; there are some issues with private information in short codes being exposed.

I still wish all the smart-quotification, m-dashing, and paragraphing could be more easily disabled, but I’m very grateful for the quick and thoughtful response.

——-

I wasted another afternoon looking for a way that I won’t have to write my own custom WordPress JSON API. After all, the WordPress REST API folks have spent many, many hours producing a core API, and writing my own just seems silly.

But it looks like I will have to write my own, and I thought I’d explain why. Maybe the WordPress API folks will read this and understand a whole set of use cases they have missed.

Here’s the deal. I store Markdown in my WordPress database. Not the processed stuff. Not Markdown that turns to HTML on save. Markdown.

I do this because I believe in what I call “capable clients”. I want anyone else to be able to make their own client and represent my data in the best way they see fit. I want people to be able to fork my source text. I want people to be able to remix my stuff with stuff from other servers.

The same is true about the short codes that go in for things like images. I want my reader’s client to get the source and render it, or move it to their server to render.

I don’t think this is such a weird thing. This is, after all, how the web worked in 1991, before graphic designers and relational database designers mucked the whole thing up with their magazine designs and fifth normal forms. Back in 1991, if you saved a file from Tim Berners-Lee’s NeXT server to your laptop, you had an exact copy of what Tim’s server had. You had the source. It was a level playing field.

APIs + JSON gives us a chance to return to that world, a world of capable clients. A world where clients of my platform can potentially build a better view of my data than I had imagined. A world where I let you fork raw data from my server and reuse it on yours, git-style. A world where people can remix data from multiple servers in new and illuminating ways, the way they did in the early days of RSS.

That’s the real promise of JSON development — the permissionless innovation that characterized the early web, but brought up to date.

So why would you only allow raw content — the unprocessed HTML or Markdown source — to be accessed by people who are logged in as editors?

Is what I typed originally into the text field of the WordPress editor such a secret? I suppose it could be, but why not give people the option to see exactly what I entered into the editor? Why fix it with paragraph tags and smart quotes, when you don’t even know if it’s HTML, or Markdown, or LaTeX stored there? Why run always run the shortcode filters, even when the client wants the data — not the useless processed output?

There’s a huge opportunity here to unleash a level of innovation we haven’t seen for years. But it starts with allowing capable clients to consume clean data, even if they only have read permissions.

In a system that truly values client-side development, clean data is a right, not a privilege. Why not give us that right?
