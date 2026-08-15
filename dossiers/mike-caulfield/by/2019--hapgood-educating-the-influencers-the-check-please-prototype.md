---
title: "Educating the Influencers: The \u201cCheck, Please!\u201d Prototype"
person: mike-caulfield
section: by
type: blog-post
year: 2019
date: 2019-02-13
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2019/02/13/educating-the-influencers-the-check-please-prototype/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Educating the Influencers: The “Check, Please!” Prototype

## Full text

OK, maybe you’re just here for the video. I would be. Watch the demo of Check Please, and then continue downpage for the theory of change behind it.

Watched it? OK, here’s the backstory.  

Last November we won an award from RTI International and the Rita Allen Foundation to work on a “fact-checking tutorial generator” that would generate hyper-specific tutorials that could be shared with “friends, family, and the occasional celebrity.” The idea was this — we talk a lot about media literacy, but the people spreading the most misinformation (and the people reaching the most people with that misinformation) are some of the least likely people to currently be in school. How do we reach them?

I proposed a model: we teach the students that we have, and then give them web tools to teach the influencers. As an example, we have a technique we show students called “Just add Wikipedia”: when confronted with a site of unknown provenance, go up to the omnibar, add “wikipedia” after the domain to trigger a Google search that floats relevant Wikipedia pages to the top, select the most relevant Wikipedia page, and get a bit of background on the site before sharing. 

When teaching students how to do this, I record little demos using Camtasia on a wide variety of examples. Students have to _see  the steps_ and, as importantly, see how easy the steps really are, on a variety of examples. And in particular, they have to see the steps on the particular problem they just tried to solve: even though the steps are very standard, general instruction videos don’t have half the impact of specific ones. When you see the exact problem you just struggled with solved in a couple clicks, it sinks in in a way that no generic video ever will. 

Unfortunately , this leaves us in a bit of a quandary relative to our “have students teach the influencers” plan. I have a $200 dollar copy of Camtasia, a decades worth of experience creating screencasts, and still, for me to demo a move — from firing up the screen recorder to uploading to YouTube or exporting a GIF — is a half-hour process. I doubt we’re going to change the world on that ROI. As someone once said, a lie can make it halfway around the world while the truth is still lacing up its Camtasia dependencies.

But what if we could give our students a website that took some basic information about decisions they made in their own fact-checking process and that website would generate the custom, shareable tutorial for them to share, as long as they were following one of our standard techniques?

I came up with this idea last year — using selenium, a invisible Chrome browser you can run on the server — to walk through the steps of a claim or reputation check while taking screen shots that formed the basis of an automatic tutorial on fact-checking a claim. And I ran it by TS Waterman and after walking through it a bit we decided that — maybe to our surprise (!!) — it seemed rather straightforward. We proposed it to the forum, won the runner-up prize in November, and on January 15 I began work on it. (TS is still involved and will help optimize the program and advise direction as we move forward, as soon as I clean up my embarrassing prototype spaghetti code).

But here’s the thing — it works! The prototype is so so far from finished, and the plan is to launch a public site in April after adding a couple more types of checks and massively refactoring code. But it works. And it may provide a new way to think about stopping the spread of misinformation, not by by generic tools for readers, but by empowering those that enforce social norms with better, more educational tools. 

<https://twitter.com/holden/status/1095823896207450113>

The result.
