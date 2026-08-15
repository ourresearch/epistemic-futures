---
title: "Embedded Journalism"
person: anil-dash
section: by
type: blog-post
year: 2008
date: 2008-03-14
venue: "anildash.com"
authors: "Anil Dash"
source_url: https://anildash.com/2008/03/14/embedded-journalism/
retrieved: 2026-08-13
content: full-text
notes: "tags: web standards"
---

# Embedded Journalism

## Full text

I want you to place the text of this blog post on your own site. But I don’t want you to do it just by copying and pasting it into your own blogging tool. I think there might be a different way to do it.

Now, I probably obsess over embedded objects and copying and pasting even more than most geeks. When I attended the recent [Graphing Social Patterns](<https://web.archive.org/web/20080316034528/http://en.oreilly.com/gspwest2008/public/content/home>) conference, one of my great frustrations is that people are talking about platforms like Facebook and OpenSocial and MySpace and widgets, but they’re leaving out fundamentals like _copy and paste_. It’s a basic capability, but none of these platforms address even basic interoperability for the applications that are built on top of them.

I don’t know how we get there; I’ve written in the past about [reinventing copy and paste](</2006/03/05/reinventing-cop/>), [Live Clipboard](</2006/03/copy-and-paste>), [Ajax Linking and Embedding](</2006/04/even-more-on-co>), and more.

Despite all these developments, what’s actually taken off with real users is the plain old browser and operating system’s copy-and-paste, combined with or tags to pull in content from other sites. It’s powered the rise of YouTube and many of the biggest widget providers. (APIs are of course a big part of this, too; Flickr and Delicious propagated themselves by posting directly to blogs using standard APIs.) But regular people on the web have settled on copying inscrutable, nonstandard HTML markup as a pretty effective way of getting the functionality they want.

But we’ve only been using this stuff for the most complicated parts of the web, like rich media. What about text?

My blog is mostly text, with some bits of video and images embedded. So, I’ve created a javascript embed tag at the bottom of every post on my blog, to let you embed the title, an excerpt of the post, and a list of commenters on the post in your own blog or site.

What use is that? I have no idea. Obviously, you could copy and paste the raw text to excerpt it. And certainly, pulilng in a javascript from my site to live on your site means you’ve got to trust my content, unless it’s sandboxed somehow.

But there seems to me to be something really interesting, some kind of potential, to including our posts (or parts of our posts) in other blogs that way, and while I’m no great coder, making the Movable Type templates to do this took about five minutes. I’m hoping something even more interesting comes from the world of compound objects or compound embeds, with a text post containing a video clip or image, and then being included on another page.

So: Has someone done this before? I’ve made blog templates that output widgets before, but what if we assume every blog post is a widget? How could we address the security issues? What does it mean that the included text and content can be updated remotely? What purpose does this serve, or is it just a really complicated way of copying and pasting text?
