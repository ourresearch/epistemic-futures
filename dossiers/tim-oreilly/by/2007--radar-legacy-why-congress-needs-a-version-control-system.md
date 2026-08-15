---
title: "Why Congress Needs a Version Control System"
person: tim-oreilly
section: by
type: blog-post
year: 2007
date: 2007-07-13
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/archives/2007/07/why_congress_ne.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# Why Congress Needs a Version Control System

## Full text

I've been thinking lately just how much software developers take the existence of version control for granted, and how, with the notable exception of wikipedia, web 2.0 applications don't offer much in the way of version control functionality. (I don't really count the kind of change-tracking that is offered in online office programs, especially ones that offer "accept all changes" in order to create a clean slate.) 

In addition to preventing a collaborating group from overwriting each others' changes, version control allows a group to revert a document to any past state, and to see who made a particular change. These are the capabilities that make wikipedia possible, an innovation even more radical than open source software, in which anyone is trusted to make changes, not just a core group of committers, with the core team moving to a moderation role that is post-commit rather than pre-commit. 

I invited [Karl Fogel](http://www.red-bean.com/kfogel/), one of the core developers of [subversion](http://subversion.tigris.org), now the most widely-used open source version control system, to join me at the [O'Reilly Radar Executive Briefing on Open Source](http://conferences.oreillynet.com/pub/w/58/radar.html) July 24 in Portland. I wrote: 

> Seems to me that Subversion (and the whole idea of version control) is a critical part of virtually everything interesting happening these days, from OSS to wikipedia. I'm wondering if you'd be up for an on-stage interview about the state of subversion... 

Karl replied that he'd like to talk more about "version control generally than about Subversion specifically," with the following list of topics as a starting point: 

> * Why it's important to be able to search the change history for Wikipedia entries (and why it's incredibly cumbersome using today's interface); 
> 
> * Why the U.S. Congress needs real version control tools (and why it's our own fault for not providing them); 
> 
> * Why good version tracking is important in a world where more and more creativity consists of mixing existing things together.

These are really thought-provoking suggestions. I was particularly struck by Karl's suggestion of a version control system for Congress. They say you don't want to see either laws or sausages being made, but I think they are wrong. Imagine how much more transparency and accountability our government would have if it were possible to see what changes were made by whom, who inserted extraneous riders into various bills, and generally to track the influence of various interests by the new visibility into their actual control over the knobs and levers of government! 

I also found Karl's comments about the problems with wikipedia's version control and version control for a remixable world stimulating. I'd love to hear what he has to say about these topics. 

Karl also offered to talk about "insider politics", so to speak: 

> feel free to ask about ... the [recent Slashdot article](http://developers.slashdot.org/article.pl?sid=07/06/03/004214) pointing to [a blog post](http://tinyurl.com/25gofu) in which Linus Torvalds dumps on Subversion pretty harshly, and explains why the style of version control he implemented in GIT is better. 
> 
> Although the presentation itself was rude almost beyond belief, some of his technical points were valid, and the Subversion developer community has been good about separating the style from the substance. 

There definitely is some substance to Linus' comments. He talked about the importance of support for branching and merging of distinct version lines, the possibility of commits _per line of code_ (rather than per file), and the viability of distributed repositories. These are definitely forward-looking ideas -- and as I noted in my recent entry on [the GPL and Software as a Service](http://radar.oreilly.com/archives/2007/07/the_gpl_and_sof_1.html), we need to be thinking hard about the future of software, and not basing our tools, our licenses, and our development practices on that future. 

I often end my talks with a stirring quote from Ray Kurzweil (which I wrote down at one of his talks at the Foresight conference about five years ago): 

> I'm an inventor, and I became interested in long term trends because an invention needs to make sense in the world in which it is finished, not the world in which it was started.

Returning to the topic of version control and our legal system...despite the many successes of our form of government, it's definitely creaking at the seams. The founders, for all their foresight, didn't plan for a nation of 300 million people, most of whom don't care to vote, they didn't foresee the extent to which the bureaucracy would become a fourth seat of power. I don't have any great prescriptions for politics, but I do have prescriptions for technology. We all need to think hard about how the future will not be like the past, focusing our efforts on that future and being willing to change course when faced with discontinuities that render our past thinking obsolete. 

The future we face is one of massive collaborative systems. How we design those systems, and how we build critical freedoms into them, shaping their architecture to support either participation or centralized control, is one of the great challenges facing the technology community today.
