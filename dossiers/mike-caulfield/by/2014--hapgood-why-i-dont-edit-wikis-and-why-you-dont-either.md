---
title: "Why I Don\u2019t Edit Wikis (And Why You Don\u2019t Either, and What We Can Do About That)"
person: mike-caulfield
section: by
type: blog-post
year: 2014
date: 2014-02-09
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2014/02/09/why-i-dont-edit-wikis-and-why-you-dont-either/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Why I Don’t Edit Wikis (And Why You Don’t Either, and What We Can Do About That)

## Full text

Back in the heady days of 2008, I was tempted to edit a Wikipedia article. Tempted. Jim Groom had just released EDUPUNK to the world, and someone had put up a stub on Wikipedia for the term. Given I was involved with the earlier discussions on the term, I thought I’d pitch in.

Of course, what happened instead was a talkpage war on whether there sufficient notability to the term. Apparently the hundred or so blog posts on the term did not provide notability, since they did not exist in print form. Here’s the sort of maddening quote that followed after Jim got on the page and had granted CC-BY status to a photo so Wikipedia could use it. Speaking as a Wikipedia regular, one editor argues vociferously against the idea EDUPUNK deserves a page on the site:

> This is clearly a meme. No one agrees what it means, its nice that a group of educators are so fond of wikipedia but it shouldnt be used for the purpose of promoting a new website and group. Even in this talk page this becomes clear, the poster boy says “Hey Enric, both of these images are already licensed under CC with a 2.0 nc-sa”Attribution-Share Alike 2.0 Generic.” It wouldn’t be very EDUPUNK if they weren’t ” then goes on to change the copyright of his own image to include it in this article, this is not ideology, this is a marketing campaign.

There’s a couple things to note here. First, the person whining above is not wrong, per se. This article is a public billboard of sorts, vulnerable to abuse by marketers, and vigilance makes sense. But ultimately his — and given Wikipedia’s gender bias it’s almost certainly a he — his protestations end up being ridiculous. EDUPUNK ends up a few months later being chosen as one of the words of the year by the New York Times, at the same time Wikipedia is unable to agree if it rises to the dizzying notability heights of [fish finger sandwich](<http://en.wikipedia.org/wiki/Fish_finger_sandwich>).

But the most telling part of that comment is this:

> _**No one agrees what it means,** _its nice that a group of educators are so fond of wikipedia but it shouldnt be used for the purpose of promoting a new website and group.

_**No one agrees what it means**_. Ward Cunningham, the guy who invented wikis, has been [talking a while about the problem with this assumption](<http://www.wired.com/wiredenterprise/2012/07/wiki-inventor/>) — that we must agree immediately on these sorts of sites — and believes it to be the fundamental flaw of wikis. The idea that people should engage with one another and try to come to common understanding is a good thing, absolutely. The flaw, however, is that wiki format pushes you toward  _immediate_ consensus. The format doesn’t give people enough time to develop their own ideas individually or as a subgroup. So an article about fish finger sandwiches can get written (we’re all in agreement, good!) whereas an article on EDUPUNK can’t get written (too many different viewpoints, bad!).

It’s important to note Cunningham’s exact point here. Many people have gone after the  _culture_ of Wikipedia in recent years, a culture which is [increasingly broken](<http://chronicle.com/article/The-Undue-Weight-of-Truth-on/130704/>). Cunningham’s point is that the culture is a product of the tool itself, which doesn’t give folks enough alone time. We need to break off, develop our ideas, and come back and reconcile them. And we need a tool that encourages us to do that.

I’ve been thinking this through for a bit, trying to come up with a solution to this problem that has the spirit of Cunningham’s proposed federated wiki but is easier for people to wrap their heads around. Here’s the the basic idea, mostly carried forward from Cunningham, but eliminating a couple more complex concepts, and simplifying concepts and implementation.

  1. I install a wiki on my server, but it’s not empty. It’s a copy of a reference on online learning (or some other reference of interest to me), with all wiki pages _transcluded._ For the uninitiated, what this means is my wiki “passes through” the existing wiki pages. For the purposes of imagining this, let’s pretend I just pull 2500 articles about learning and networks from Wikipedia, and transclude them on my wiki/server.
  2. I then join a federation. So let’s say I join a federation of a 100 instructional designers and technologists. This changes search for me, because search on my wiki is federated now. I can search _across the federation_ for an article on EDUPUNK. Let’s say it’s 2008 and I’m looking for a quick explanatory link on EDUPUNK to send someone. I pump in that search and find there’s five or six somewhat crappy treatments, and one half decent one by Martin Weller.
  3. I don’t edit it. Or rather, I do, but the minute I edit it, this becomes a fork that only lives on my server. So I fix it up without having to get into long arguments with people about notability, etc. When done, I shoot a link to the person I wanted to send the article to. My selfish needs are met.
  4. Now, however, when anyone goes to their EDUPUNK article in the federation, they see that I’ve written a new version. Some people decide to adopt this as their version. Martin Weller sees my edits, and works about half of them into his version along with some other stuff. Jim comes by and adopt Martin’s new version with some changes. It’s better than my version, so I adopt that one.
  5. Tools start to show a coalescence around the Martin-Me-Martin-Jim version. A wiki gardener in charge of the “hub” version looks at the various versions and pulls them together, favoring the Martin-Me-Martin-Jim version, but incorporating other elements as well. This version will get distributed when new people join the federation, but as before, people can fork it, and existing forks remain intact.

The idea here is that forks preserve information by giving people the freedom to edit egocentrically, but that the system makes reconciliation easy by keeping track of the other versions, so that periodic gardening can bring these versions together back into a more generic whole.

You can think about this from any number of angles — imagine an online textbook, for example, that allowed you to see all the modifications made to that textbook by other instructors — and not edits living on a corporate server owned by Harcourt-Brace, but edits that were truly distributed. Imagine a federated student wiki, where your students could build out their articles in piece during the semester, seeing how other students had forked and modified their articles, but keeping control of their subsite, and not being forced to accept outside edits. The student’s final work would reflect *their* set of decisions about the subject and the critiques of their treatment of it. Or imagine support documentation that kept track of localizations, making it easy to see what things various clients needed to clarify, and making those changes available to all.

Anyway, this is the idea. Encourage forking, but make reconciliation easy. It’s the way things are going, and the implications for both OER production and academic wikis are huge.
