---
title: "Wikity Updates (0.4)"
person: mike-caulfield
section: by
type: blog-post
year: 2016
date: 2016-09-20
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2016/09/20/wikity-updates-0-4/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Wikity Updates (0.4)

## Full text

The newest release of Wikity is [up on GitHub](<https://github.com/michaelarthurcaulfield/wikity-zero>). There are a few bugs knocked out, but the major change is a shift from “Path” functionality to “Cardbox” functionality. This shift is partial — mostly about terminology at the moment — but will eventually work a bit different as well.

Paths in Wikity were sort of Bushian (Vannevar, not G. W.). Different cards could be put together in a sequence, and then you could walk through that sequence in a forward/next sort of way.

I found that how I was using Wikity cards in paths really didn’t match that. I was really putting together a set of resources that could be hopped and skipped around. Sequence was less about reading things in the right order than putting things in sort of rough clusters; general stuff first, more niche and tangential stuff at the bottom. “Path” started to feel to me like the “Unread” folder in the old Goggle Reader: it was a term that made me feel like I had to read everything, and that was a drag.

So I decided to move away from the “path” term and move towards the less sequential “card box” term. I think of it like these little boxes my youngest daughter uses to store her index cards:

That is the stuff in it might be ordered, and even tabbed, but it’s not really asking you to read it in sequence. (This, incidentally, was also the metaphor of “fileboxes” in Xerox PARC’s NoteCards project).

So that’s the shift in metaphor. Here’s what we are probably going with it, eventually.

**Cardboxes as Choral Frameworks**

A lot of people think that Wikity is how one can do Choral Explanations. After all, that’s my big deal of the moment, surely the software I write has implemented it, right?

Nope. Wikity was built not for Choral Explanations, but as a Personal Learning Environment. You can’t currently do Choral Explanations in Wikity.

Yet every time I write about Choral Explanations, someone writes me and says — I love this idea, I have to download Wikity! It gets embarrassing.

So we’d like people to be able to at least hack CEs together in Wikity. One thing I’m going to work on is setting up cardboxes as a framework for CE. So, for example, you set up a CardBox called “How do sunflowers follow the sun?” and various people can add their own explanations to the Cardbox. Instead of “previous/next” navigation we’ll just feature these as a large ordered scrollable page.

[](<https://mikecaulfield.wordpress.com/wp-content/uploads/2016/09/screenshot-2016-09-20-at-7-59-01-pm.png>)

It’s not perfect, but at least it will be the end of people downloading Wikity to do choral explanations and finding they can’t.

**Cardboxes as Workspaces**

A little more involved, but worth it: I’d like to create an option where you can pull all the items in a cardbox into catalog view.

This would allow you to edit your entire cardbox at once, getting a sense of what’s there and what’s not, clicking in and editing on card while reading the synopsis of others. This catalog layout has been one of the surprisingly effective things about Wikity, but there’s no way to define a workspace that you can pull up later. Cardboxes might be a solution, a way to save a workspace.

**Cardboxes as Feeds**

Ward Cunningham had the idea a while ago to make a “feed plugin” for Federated Wiki. The idea (somewhat counterintuitive to bloggers) is that you manually add links to the material you want in the feed. The plugin then fetches page links, descriptions, and whatnot and outputs well-formed RSS when called.

As weird as this may sound, it actually makes sense. Wiki is an iterative process, there’s no way an algorithm can tell when something should be pushed out to others. Manually adding items to feeds makes sense. You decide when the article is ready for a certain group, and push it to that feed. You decide if you made a big enough change you want to push it again. You can create multiple feeds for multiple audiences.

My thought is that Cardboxes might output RSS as well. Add new items to the cardbox, and they appear at the top of the Cardbox feed.This will also allow the works to flow into RSS syndication hubs.

**Cardboxes as Trusted Subscriptions**

Unlike federated wiki, Wikity is lacking a coherent community model. I’ve played around with the idea of allowing cards from other trusted sites to flow to your own, so we get content duplicated across many sites.

It occurs to me a Cardbox could be a way of doing that. Everyone subscribes to each other’s Cardboxes, and automatically forks copies of items dropped in the cardbox. People build out the wiki, and at the end, everyone walks away with the full version of the wiki. This seems to me a good solution to class activities as well — as a student you make as many pages as you want, but you share your best ones to the cardbox.

**Anyways ….**

Anyway, these are some of the ideas I’m playing with. For now it’s just playing with new language, but pretty soon we hope to build out some of this functionality. For now, you’re welcome to download it from Github and install it on your own server as a theme. It’s super simple and the instructions are in the distribution readme.
