---
title: "Tilling the Garden: A different way to use AI to make interesting and useful apps"
person: mike-caulfield
section: by
type: blog-post
year: 2026
date: 2026-06-04
venue: "Mike Caulfield's Substack (mikecaulfield.substack.com)"
authors: "Mike Caulfield"
source_url: https://mikecaulfield.substack.com/p/tilling-the-garden-a-different-way
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Tilling the Garden: A different way to use AI to make interesting and useful apps

*Rebuilding the internet of weird little things one data enrichment at a time*

## Full text

I’ve been talking recently about [Plot.fyi](<https://plot.fyi/>), my new film recommendation site. That’s partially because it’s pretty neat, and has resulted in me finding lots of great films. But the most interesting thing about the site is how it uses (and doesn’t use) LLMs.

[](<https://substackcdn.com/image/fetch/$s_!KDSf!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd1235d79-2a33-4a60-8417-fde25521afd0_1381x861.png>)

Everyone knows the way an AI-driven site is supposed to work. You have a user who asks a question, like “What are 10 films like _The Hateful Eight_?” That question gets taken from the user and embedded behind the scenes into a larger prompt that provides some instructions about values, methods, and sources, and is fed to one of the Big Three LLM models. You get an answer back. If the prompt is good and some well-chosen post processing is used to check and ground it, you hopefully get something useful. As the models get better, you need less of a wrapper and less post-processing, supposedly at least.

With this approach, the core value of the exchange is in the model itself, assisted by the wrapper. But as many people writing these wrapping applications have discovered, if you live and you die by the model you hit a bit of a Catch-22:

  * **If what the model does is expensive** , you pay for each and every request at an unsustainable rate for scaling. You’re the front end for a model, and **you absorb the risk** and the makers of the model make money whether you succeed or not. As they say in the gambling industry, the house always wins. And in this case the LLMs are definitely the house.

  * **If what you’re doing becomes cheap and easy** , you’ve got a different problem, because now **no one needs you at all**. The hope that the cost will come down for your backend functions is a bit of a monkey’s paw wish. If it doesn’t come down you bleed money. If it comes down too much people will just do it in the LLM, which might be even a bigger problem.

The brutal economy of wrapper applications is part of the reason I’ve generally circulated reusable _prompts_ rather than build wrapper sites. At least with prompts I’m not absorbing the risks of investing in something where I’ll pay a tax per user until it’s made irrelevant. 

## Back to the digital garden

Is there a way to avoid this conundrum? For some set of things, yes. You can extract the value _out_ of the LLM and put it into _content you control and cultivate directly_. 

This is a bit of an ask, but I’m going to ask you to go to [Plot.fyi](<https://plot.fyi/>) for moment. Click around it for about half a minute. Thirty seconds. Understanding what the site is — even just having a thirty second understanding — is crucial to understanding my next point.

[](<https://substackcdn.com/image/fetch/$s_!HEL5!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb0aebf1b-efe5-428b-81e1-86d9852e0d4b_800x600.gif>)In case you’re wondering, yes, I do think that the blood-soaked Tarantino film _The Hateful Eight_ is in fact parallel to _Murder On the Orient Express_ in many ways (though a perfect response I think would surface _And Then There Were None_). It’s actually these sorts of connections that excite me. 

Ready? 

If you clicked around, I imagine you think it looks like any number of AI/ML sites that select films by taking an input (a film you like) and find relevant matches by feeding that information with a prompt wrapper to AI. 

In fact, while I _built_ it using AI, the site itself uses no AI at all. 

It doesn’t even use a server. It doesn’t have a database. There is no backend. 

The entire application is HTML and JSON. There is an initial hit to bandwidth in the form of a 1.9MB data file.1 After that the program runs entirely in your browser, consuming the practical equivalent of zero CPU cycles. 

If you want to visualize the size of that data file, here’s a 1990 ad for a 1.4MB floppy drive:

[](<https://substackcdn.com/image/fetch/$s_!rNtO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8483d50c-fefa-4d3c-a2e9-0d498803bea9_850x522.png>)

How is that possible? How can a program act like an AI recommendation engine for over 10,000 films and use no AI?

The key is using modern AI, but using it in ways we used to use AI in the past. I’m not saying the following approach works on everything, but for some subset of things you can apply it. I detail it here 

## An internet of weird little things (without the AI tax)

The way the site works is this. I spent the past two months using Claude Code to tag a dataset of 10,000 films with a variety of tags I invented that flag certain plot elements.

This shouldn’t seem radical. We used to enrich datasets with tags a lot before we got these powerful systems that could synthesize information without needing our own rich, tagged data. (Researchers still do, all the time!)

What’s new is the scale of things you can accomplish with a model the size of Claude Opus. Ask it for the themes of a relatively little known film from the 1940s, and it will spit out fairly accurate bullet points for you without needing to fall back on search. Ask it if any of twenty listed films have a “redemption arc” for the main protagonist, it will, with impressive accuracy, point to the ones that do. Run it through all the romance films, 40 at a time and see if any of your romance tags fit.

[](<https://substackcdn.com/image/fetch/$s_!LhC9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff0c2fa93-3238-4041-91ca-91be68499bba_1172x917.png>)

So that’s what I did. Over almost two months I used Claude Code to run hundreds and hundreds of tags over thousands of films and wrote all those tags to the data files.2

After doing that across about 700 tags for 10,000 films you end up with 10,000 files that look like this. Here’s _The Hateful Eight_.

[](<https://substackcdn.com/image/fetch/$s_!jBHs!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fad4b0e91-d777-4615-9883-af53dd4a5cab_1181x342.png>)

Here’s _The Brother from Another Planet_ :

[](<https://substackcdn.com/image/fetch/$s_!MARO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9637955a-97f0-4d8e-994e-1da790dfa1ec_1142x305.png>)

These files then get spooled out as a dictionary and a series of ID pointers, creating that floppy disk size data runtime:

[](<https://substackcdn.com/image/fetch/$s_!eOl0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F72075e80-3625-4e67-ae5e-6ec38fd28719_1402x628.png>)

When asked about a film like _The Hateful Eight_ , the system tallies up tag intersections across 10,000 records, computed as shown below:

[](<https://substackcdn.com/image/fetch/$s_!gulW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F83645885-f902-480a-8672-5ffd44efbbbd_1493x747.png>)For film buffs I’ll note that the Kubrickesque part of _Hateful Eight_ is mostly the one-point perspective. One thing I learned in this process is you want to set your net pretty broad on these to get better connections (otherwise you lose the connective tissue).

It then uses that computed score to float similar films to the top of the list. It takes less than a tenth of a second of computation, and because once you encode all this stuff in the _data_ , you can actually do the film matching with a little bit of Javascript math. 

## Example 

Let’s take _Overboard_ , the Goldie Hawn/Kurt Russell film from the 1980s that is very creepy when you think about the premise for more than two seconds. As others have noted this isn’t a rom-com, it’s a horror plot!

> **Overboard:** The 1987 film follows a narcissistic heiress who loses her memory after falling from her yacht. A mistreated working-class carpenter takes revenge by convincing her she is his wife and the mother of his unruly children. She navigates chaotic family life, ultimately coming to value many of its attributes.

So maybe there’s something there in that plot that you like, but you would like it without the whole abduction angle. Where else can you get it?

If you ask an LLM, the response is not bad. Here’s what it gives you back:

[](<https://substackcdn.com/image/fetch/$s_!KBy8!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4b74365f-38e5-428c-b49d-fa0bf4bc9ad6_1010x753.png>)

Films mentioned: 

  * The Proposal

  * While You Were Sleeping

  * Maid in Manhattan

  * Sweet Home Alabama

  * Wedding Planner

  * Doc Hollywood

  * Coming to America

  * Kate and Leopold

  * The Prince and Me

Great. It’s about what a good Blockbuster employee would be able to tell you back in the day. Not just the average employee, the one you’d always seek out! Here’s the description of The Proposal. As the LLM has identified it’s got a similar vibe, but replaces false imprisonment with corporate bullying (an improvement!):

> **The Proposal** : The 2009 romantic comedy The Proposal follows an overbearing New York book editor (Sandra Bullock) who, facing deportation to Canada, forces her long-suffering assistant (Ryan Reynolds) to marry her. The charade unravels when the fake couple travels to Alaska to meet his family, forcing them to confront their true feelings.

Now let’s see what we get with our broad simple tags and a search on _Overboard_ :

[](<https://substackcdn.com/image/fetch/$s_!LBYR!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7db754aa-68d9-4b89-9e40-748b48d007f7_937x839.png>)

We get a lot of the same stuff here. In this case, however, it’s generated by the tiniest bit of data. As noted above, this isn’t any billion parameter production. It’s about 11 tag intersections.

[](<https://substackcdn.com/image/fetch/$s_!9vgU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fea96f494-06f9-4fd8-88df-8afd3eb0cecf_1510x867.png>)

This feels very weird to me. How can such a small dataset get you there? But it’s not really the size of the data on the _individual items_ that matters; it’s that when numerous tags that represent as little as 5% of the data set intersect across a database of 10,000 records, interesting stuff floats to the top. That sort of scale of data enrichment used to be out of reach for average people, but now anyone can maintain and enrich a collection that size.

That means a couple things. 

First, as mentioned, we can run the whole site [Plot.fyi](<https://plot.fyi/>) as a serverless HTML page reading JSON data. No AI, no server. Serving results for over 10,000 films. We use the LLM to build the product but escape the LLM tax to run it.

Second, I was able to get what I feel are _better_ responses that I do with an LLM, at least in terms of what I think a good answer is.

[Plot.fyi](<https://plot.fyi/>), for example, identifies _I Married a Witch_ (an old Veronica Lake film) as a parallel. While difficult to explain, this is a) correct, and b) a connection that does not seem to have been made by _anyone online_ before. In _I Married a Witch_ , a witch forms a relationship with a man to extract revenge (like Russell) for mistreatment the target is unaware of (like Hawn) and the witch grows during the course of the revenge to fall in love and value “ordinary” life (like Hawn, in a bit of a switch-up, with the revenger having the realization).3

This is a different sort of match than _The Proposal_. If you search _The Proposal_ and _Overboard_ you’ll find a dozen pages talking about these films having the same vibe:

[](<https://substackcdn.com/image/fetch/$s_!85RT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F18a6bc49-7b12-460d-86a6-565da3d8acd6_941x415.png>)

That’s not surprising; this sort of web text is a lot of what the LLM was trained on after all. In contrast, you will not find a page on the internet that compares _I Married a Witch_ and _Overboard_. There are multiple reasons the JavaScript finds this whereas the LLM does not, but a big one is standard code with well tagged data is better at mapping a _complete_ space than prompting. We can loop over every record in the database and check it against the input film in a way that would take hours and cost hundreds of dollars to do with a prompt. The cost to us with the V8 JavaScript engine in Chrome? Essentially nothing, and less than five _milliseconds_ of processing.

The final thing is this. You _own_ that data. 

I mean, I’ve mucked it a bit here because I’m me and have implemented it in such a way that anyone can grab my Javascript and grab almost two months of my tagging work for their own purposes. I’ve developed openly available prototypes for 30 years, it’s hard to stop.

But that sort of approach is not required. You could build an approach like this into a database that no one can access directly if an open approach is not your thing. It’s up to you: feed the value back out to the community, or keep it as your competitive advantage. Either way the value is not in the model, it’s in the data you enriched with the model.

## Maybe this is temporary, but so what

It’s possible that in six months this post will sound cute. A lot of smarter people than me think what the LLM will be capable of soon will so far outstrip other approaches that building things that don’t primarily rely on request-time AI compute will be silly. Under that view, little experiments like this where we turn AI around and use it to enrich the Commons or try other weird things will be historical footnotes at best.

Maybe. 

But to quote another film, “OK.” 

Maybe we’re on this ride down this slope, and our uselessness in the face of the ever-growing capabilities is pre-determined. Maybe these little schemes are futile.

So what.

We’re here right now, we should live how we want to live. The future will arrive when it arrives. 

I’m not saying what I’ve outlined here is the one right way to use AI. I’m not giving up on writing mega-prompts, or even writing the occasional Node-based wrapper. I haven’t found a new religion. If you’re reading this thinking my point is “all AI use must follow this external content enrichment pattern” you’ve read me wrong.

I’m just saying right now there’s a lot of room for experimentation, and if you’re worried AI will kill our creativity, centralize our cultural infrastructure, and nail shut the casket on the long deceased internet of weird little things, then _get out there and show a different way of doing it_. Show ten different ways of doing it. Explore in public new ways to think about this technology besides treating it as the Star Trek Computer or roach motel for cultural knowledge.

There are a million options between AI refusal and AI complacency, and we should be exploring as many of them as we can. 

Oh, and spend less time doom-scrolling, and more time [watching good movies](<https://plot.fyi/>). It will heal you, I swear.

1

The recommendation file is 1.9MB, but the detail pages you get when you click on a recommendation are another data file which is stored as a small series of 200KB shards, the bulk of which consists of those intro paragraphs to Wikipedia.

2

It took months just because I have a day job so this was something I’d do each evening: come up with a couple tags and have Claude tag my data

3

I’ll note here “ordinary” life consists of living in quite a nice house, but engaging in human non-witch stuff. I think most of us would like that life.
