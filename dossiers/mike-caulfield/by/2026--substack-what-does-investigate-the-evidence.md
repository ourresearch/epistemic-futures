---
title: "What does \"Investigate the evidence\" mean in the SIFT for AI proposal"
person: mike-caulfield
section: by
type: blog-post
year: 2026
date: 2026-03-31
venue: "Mike Caulfield's Substack (mikecaulfield.substack.com)"
authors: "Mike Caulfield"
source_url: https://mikecaulfield.substack.com/p/what-does-investigate-the-evidence
retrieved: 2026-08-13
content: full-text
notes: ""
---

# What does "Investigate the evidence" mean in the SIFT for AI proposal

## Full text

As I discussed at length this past weekend, I am exploring an edit for SIFT currently called “SIFT for AI” that keeps source verification in a _central_ role but pushes it back from its _initial_ role.

[](<https://substackcdn.com/image/fetch/$s_!2Cb0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F45c22fce-4aee-49af-aaab-f8c52f32c470_747x869.png>)

Instead, I have pushed something called “Investigate the evidence” into one of the two initial roles. So what is that, and how does it work?

## Evidence-focused follow-ups are the simple move that make you an expert prompter

Last summer, I worked with Google on the AI Mode update to the _Super Searchers_ curriculum. One of the things I wanted to figure out was what is the simplest move that could improve the relevance, comprehensiveness, and accuracy of AI Mode answers. In my experimentation with over a thousand tests graded by a self-built autorater I found a couple interesting things. 

The first was this: pretty much _any_ neutral follow-up improved answers. (A follow-up is your second prompt after a first one). I don’t have my list in front of me right now, but as long as you don’t lean into bias, follow-ups as simple as “What should a person know about this issue?” led to better answers on average and in some cases dramatically better ones than the first answer given. In a way, this isn’t surprising. At the most basic level, second prompt means more time spent on the issue by the LLM, more accumulated context, and more time and context means a better result. Add to that that the follow up often zeroes in on the relevant bit of the thing you are investigating, and of _course_ the second answer will be better. In fact, if you need something quality, I’d suggest that you don’t even need to read the first result. Consider the first result as the LLM finding its initial way around a domain. Once it has made that initial scan it’s ready to do the _real_ work. 

The second thing I found in my experimentation was that the most useful sort of follow-up for the things I teach was what I call an _evidence-focused_ follow up. Let me show you how that works. 

Here’s a post that just came across my feed.

[](<https://substackcdn.com/image/fetch/$s_!t0cj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F92545f59-68a6-4b23-8251-40785dba6d4c_782x592.png>)

This post raises an interesting question. “Bowling Alone” is both a book and the informal name of an argument that society has deteriorated partially due to the dissolution of things like bowling leagues. The above post proposes that there is a corporate angle to all of this, with mom-and-pop league focused lanes being sucked into a cruel corporation that is actively hostile to them.

So let’s try this.

## First Response (Get it in!)

I put the top text from the tweet into AI Mode:

[](<https://substackcdn.com/image/fetch/$s_!Kv3D!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9132e6d3-3a20-432c-ad93-9fd304c304a9_929x605.png>)

Lots of text comes back. 

Here’s something that might surprise you. I read none of it. 

As far as I am concerned, this is AI Mode _warming up_ , exploring the space. If I saw the answer I needed in the first paragraph and was in the market for a short answer that’s great, I’d stop. Lots of questions are like that. This question isn’t. 

I already know I want a bit of nuance and a bunch of evidence, so I am going to do the “I” in the new SIFT for AI: investigate the evidence!

[](<https://substackcdn.com/image/fetch/$s_!qFb6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb67cda93-89fc-46fb-8977-2083ade39641_610x571.png>)

Here’s that move:

> **Investigate the evidence.** Ask evidence-focused follow-ups. Gather and categorize important context. Get organized and sourced information, not (just) answers.

And here’s what it looks like in practice. As our follow-up we put in

>  _What is the evidence for and against Bowlero being bad for league play?_

And this is what we get. It’s going to be a long answer. Keep in mind we can follow-up by asking it to condense it for us (just use a prompt like “ELI5”).

OK, this is a long answer, skim it, but I want to show you what you get back then say a couple things:

[](<https://substackcdn.com/image/fetch/$s_!mx4T!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F10b39d6c-0da8-4882-aa04-925e3866acc7_911x622.png>)

[](<https://substackcdn.com/image/fetch/$s_!yKgw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F78e129e3-972b-4861-a094-814aa29cfe4e_907x636.png>)

[](<https://substackcdn.com/image/fetch/$s_!I7lZ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6baa9701-9d3e-4985-905a-98040a7f3b3e_946x279.png>)

[](<https://substackcdn.com/image/fetch/$s_!Z4DS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd98c0763-ca7a-4a01-a256-e40e733c75f0_961x538.png>)

## Why we do the two-step 

I suppose you’re wondering why we don’t just ask the question “Is Bowlero bad for league play” to start. Good question. Let me show you why. 

This is what happens if we skip our “Get it in” move where we get the follow-up in, meaning, if we just ask for evidence in step one:

[](<https://substackcdn.com/image/fetch/$s_!xItv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F84cc7fcd-b2f2-41b5-b179-6fd524ff3fc5_968x302.png>)

You see what’s going on there? That’s an answer, but it doesn’t understand the _context of the request_.

So we’re wondering about Robert Putnam’s sociological work and its relationship to public and private equity and AI Mode is walking us through something that is a bit more slanted towards “Should we head down to the Bowlero tonight?” And why shouldn’t it, really? There are more people thinking about heading to the bowling alley right now than are thinking about the relationship of Bowlero to key works of 1990s sociology.

So we set the context with the Get It In move. Now we could stop there, the answer wasn’t bad. But even if you just look at the first paragraph of each answer you’ll see that the evidence-focused follow-up significantly improves the usefulness of the answer to us. Here was the round one starting paragraph:

> The rise of **Bowlero Corp.** (BOWL) represents a significant corporate shift in the social landscape originally described in Robert Putnam's _Bowling Alone_. While Putnam focused on the decline of social capital and "league" membership, Bowlero has industrialized this trend by actively moving away from the traditional, low-margin league model in favor of high-margin entertainment.

This gets the context! Great. But it also largely just restates the thesis of the post. What we wanted to know was what the larger picture was. 

Now let’s look at what we get after the evidence-focused follow-up:

> The debate over **Bowlero Corp.** typically pits corporate financial efficiency against traditional sporting community. While critics argue the company is "killing the soul" of the sport by prioritizing high-margin parties, supporters (and the company itself) argue that its model is the only way for bowling centers to remain financially viable in a modern economy.

And of course after that you do get all that evidence. Even at a scan you find some interesting bits. For instance, it does seem that league fees do go up in many places after a Bowlero takeover. On the other side of things, I found this fact fascinating: 

> Critics often overlook that a single busy Saturday of "open play" can generate as much revenue (approx. $60,000) as a 36-week league generates in an entire year (approx. $50,000). Without this revenue, many centers would likely close permanently.

That’s not quite apples-to-apples, but it is striking. And I don’t know if it undermines the poster’s point. But it does put it in context. The difference in amount of revenue looks very significant.1

And that’s it. That’s the move. After you “get it in”, use an evidence-focused follow-up. You’ll get an answer that tries to give you a 360 degree view of the issue. That gives you a better answer even if you only read some of it. 

## Moving from there

I want to stress this: you can stop there if you want. In seeking context (step one) you did more than 95% of the population. In seeking pro/con evidence you did more than 99% of the population. Don’t let people that don’t check anything at all shame you that you didn’t invest even more time. SIFT has always been additive in value: each step adds value in itself and does not require that you go the entire distance to get benefit from it. 

But if it’s something you plan to share, something with stakes, or something that has made you feel strong emotion, I would suggest trying the other moves. You notice a lot of the citations are Reddit. Can you use the **find better sources** move to get news coverage or expert analysis? Can you **track down** the source of that “$60,000” figure and make sure the source isn’t just “some dude on Reddit”?

You can take this as far as you want. But even doing the above is going to help you. However SIFT evolves, the focus is still “How do we do a little bit of work to get a lot smarter?”; that part will never change.

1

It goes without saying, of course, if we passed the “idle curiosity” phase of this investigation we would dig into that $60,000 figure and comparison, ultimately sourcing it. But the point here is not that you have a bullet-proof fact but that you do understand the argument that is being made.
