---
title: "A Google Docs for Markdown"
person: anil-dash
section: by
type: blog-post
year: 2020
date: 2020-12-10
venue: "Glitch blog (blog.glitch.com; formerly Fog Creek)"
authors: "Anil Dash"
source_url: https://blog.glitch.com/post/google-docs-markdown-glitch/
retrieved: 2026-08-13
content: full-text
notes: "Company blog post authored by Dash as CEO"
---

# A Google Docs for Markdown

## Full text

Although Glitch is a really powerful platform where you can build full-stack web apps, I also find that one of its simplest, most straightforward features has some pretty amazing potential.

You can easily create and maintain a group-edited collection of Markdown files on Glitch, almost like a Google Docs for Markdown. Once you do, there's a huge set of possibilities of what you can do with those files

If you're here, you already know what Markdown is — it's a way of formatting plain-text files so that they can consistently be parsed into rich text or HTML if you'd like. I've been using Markdown since John Gruber first created it almost 2 decades ago, and it's been amazing to see it become so ubiquitous that many more technical users just _assume_  it's going to be available wherever they want to write.

## Hitting The Mark #

Markdown also has a few key advantages over the ways that people commonly write together as part of teams or workgroups. In a tool like Google Docs, as good as it is, there are some pretty significant constraints:

  * There's no built-in formatting styles for code, or even for blockquotes.
  * You can't just use HTML even if you know it
  * Copy & paste can still be annoying in the same way that Microsoft Word is frustrating, bringing over unexpected styles or formatting None of these by itself is a _huge_  problem, but all of them together can be really annoying and frustrating. Meanwhile, trying to edit Markdown files alongside other people is... weirdly hard? You could use a whole complex git-based workflow, but that seems like overkill, and we're spoiled by being used to edit together in Google Docs and Figma and all our other tools that let us collaborate in realtime.

So, the answer to easily editing Markdown files while working together on them as easily as sharing a Google Doc? Glitch!

Take the piece that you're reading right now: I wrote it right on Glitch, and then I could easily share it with my coworkers so they could read over it and offer edits or suggestions if they wanted. It works just like sharing in any other app, without having to go through the complexity of git. And now if I don’t want my notes to be readable by everybody on the Internet, I can just [set sharing to be private](<https://blog.glitch.com/post/the-easiest-way-ever-to-control-who-you-share-your-app-with>), and only the people I invited can read what I’ve written.

Now, if I want to undo changes, or go back to an earlier version, I still have git under the hood, automatically saving all my edits as I go. If I want to get _really_  fancy, I can even hook up other tools to my Markdown files on Glitch because it's all accessible as a completely standard git repository. But I don't _have_  to do any of that stuff unless I want to.

And best of all, any people I invite in to share this Glitch project can also create and share their own Markdown files that we all maintain together. If we want to make a knowledge base or a documentation manual together, it's easy enough for a brand new user to jump in, and advanced enough for any coder to feel fully comfortable building on top of. There are even niceties like a fancy little button that will automatically format your file and keep it looking neat and clean.

## What Comes Next #

Of course, since Glitch lets you create and run full-stack apps, the sky's the limit when it comes to using the Markdown files you make on Glitch. If you want, you can build (or import from GitHub) a static site generator, and publish your Markdown files as web pages. You could use the built-in git support to synchronize the repo to another hosting platform or publishing tool. You could write scripts to process your Markdown and output it in any format you want, or to submit it to another platform's APIs. You could even build another Glitch app that uses your documents as data that it works from.

The key thing is, _it's just code_. You can do anything any standard coding environment lets you do, but it's just easier to get started writing and creating and previewing your Markdown files.

So, if you're looking for an easy way to create and share documents together, and Google Docs isn't a good fit because it's not designed for plain text files, keep Glitch in mind as part of your toolkit. (And let us know if you find good uses for it with your team!)
