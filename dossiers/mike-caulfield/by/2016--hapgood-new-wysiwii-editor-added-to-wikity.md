---
title: "New WYSIWII Editor Added to Wikity"
person: mike-caulfield
section: by
type: blog-post
year: 2016
date: 2016-05-23
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2016/05/23/new-wysiwii-editor-added-to-wikity/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# New WYSIWII Editor Added to Wikity

## Full text

One of the ways we kill reusability is through layout and markup. In fact, this was one of the realizations that started me on this path eight years ago. Looking at the practical barriers to remix it became clear that highly formatted web pages, PowerPoints, and Word documents were not really remixable, because of the work required to strip formatting and rebuild the text in a form and style that suited your course.

What you really wanted was something that had nothing but the bare minimum of semantic tags. And that’s when I got infatuated with the idea that Markdown and Textile and other simple markup formats might point the way to greater reusability. These formats allow you to do a few semantic things in human readable markup:

> You can **bold**, _italicize_, and [link](<http://example.com>). You can
> 
> ## Make Headings
> 
> and
> 
> * make a  
>  * list  
>  * of items

and it comes out like HTML:

The thing Markdown _stops_ you from doing, however, are things like specifying font type or size, or doing table layouts, or making complicated float-left or z-index rules for your content.

You can add some rules to your platform to deal with these things, but they don’t live in your document source code. This makes your document portable in a way very little else is. It also makes it accessible, since you can use these codes without having to use a ribbon bar, or select text, or use complicated key combinations (all of which reduce accessibility). For these same reasons, a Markdown based system is quick and easy to use on a phone.

So when I started Wikity, I decided to go Markdown source as format. And that’s worked out for me. The speed with which I can put together a Wikity card makes this WordPress dashboard editor feel like concrete shoes. I’ve written 924 cards since November, because the Markdown always-there system we have in place makes writing a card as easy as tweeting (and forking it nearly easy as retweeting). About 20% of those have been posted from my phone, which I would not have thought a possible percentage.

That said, people get intimidated by the blank box. They needed the training wheels of the ribbon bar. So after a few botched attempts, I finally found a WYSIWII (What You See Is What It Is) editor for Markdown that could hook up easily to some Wikity events. I think we’re going to get the best of both worlds here, but check out this video, and let me know what you think:
