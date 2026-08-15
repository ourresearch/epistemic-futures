---
title: "How structuring AI-assisted search as a \"narrated exploration\" got better answers and made search fun again"
person: mike-caulfield
section: by
type: blog-post
year: 2025
date: 2025-05-24
venue: "Mike Caulfield's Substack (mikecaulfield.substack.com)"
authors: "Mike Caulfield"
source_url: https://mikecaulfield.substack.com/p/using-unfolding-search-heuristics
retrieved: 2026-08-13
content: full-text
notes: ""
---

# How structuring AI-assisted search as a "narrated exploration" got better answers and made search fun again

*A note on some very enjoyable updates to SIFT Toolbox, courtesy of heuristic theory*

## Full text

A recent update I made to SIFT toolbox turns out to be quite impactful -- I can say this after running ~200 of my favorite fact-checking prompts against it. I'm actually a bit surprised at how well it works. More on that in a minute, but first some background for new readers.

For those that don't know I've made what some people would call a "fact-checking" engine that runs on top of [Claude.ai](<https://claude.ai/>). I call it a "contextualization engine". It's called SIFT Toolbox, and it acts as a "prompting layer" that changes how Claude acts. You can get that prompt for free at [checkplease.neocities.org](<https://checkplease.neocities.org/>) and dump it into Claude. You need a paid account, because it requires the search ability that only paid accounts have currently.

Thanks for reading The End(s) of Argument! Subscribe for free to receive new posts and support my work.

The way I think of this tool is that it makes LLMs act less like the Star Trek Computer, and more like the Memex -- trying to summarize with links the conversation around what you're looking at. 

## The Tool Up To Three Weeks Ago

The part of the tool that’s been in place for a while now works like this. You take a screenshot or a question — like “Can five walnuts a day improve memory?” and feed it to the system.

[](<https://substackcdn.com/image/fetch/$s_!qATd!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3618655b-2a55-4dbd-bd2e-c8355ce0ae37_1222x463.jpeg>)

The prompt then constructs a series of searches and executes them:

[](<https://substackcdn.com/image/fetch/$s_!lwF_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc2836429-9028-409b-9ca0-cb41c507152a_1200x782.jpeg>)

It then produces a set of "verified facts", "errors and corrections", and "potential leads" each cited to a specific source (sorry to my long-time subscribers for this rehash, I’ll make it quick).

[](<https://substackcdn.com/image/fetch/$s_!INan!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe36ee864-54ab-4e6a-a8d8-3c2cd55df249_1234x619.jpeg>)

[](<https://substackcdn.com/image/fetch/$s_!oGgv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F11079362-e336-4e3c-9a9c-6c82f1698d77_1229x684.jpeg>)

[](<https://substackcdn.com/image/fetch/$s_!wxdz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F27fd8ce7-1c0f-4704-9aba-a0b03f16cd7b_1237x426.jpeg>)

## Addition of “Another Round” Mechanism

A few weeks ago (a month ago? My sense is not exact here, I’ll look it up later) I added the “another round” feature. The another round feature does a new set of searches looking for at least three things:

  * conflicting evidence for what it just concluded 

  * added depth to existing conclusions 

  * entirely new angles to the discussion

The core instruction is this:

[](<https://substackcdn.com/image/fetch/$s_!enau!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F56b1ffc3-0397-4b47-9651-09c6bcea48e3_768x245.jpeg>)

I actually pulled this idea from an extension of Herbert Simon's metaphor of information search as berry-picking, at least in a broad sense. Roughly we're foraging for evidence for two contradictory claims here. If as we berry-pick the berries on one side of the equation remain fairly easy to find and high quality and the berries on the other side get harder to find and low quality, that can help provide a "stopping rule". Which is pretty geeky information science stuff, but pretty simple to build into the process.

The "other angles" piece is similar, and plays the same role here. If we look at the question under discussion (the [QUD](<https://en.wikipedia.org/wiki/Question_under_discussion#:~:text=In%20semantics%2C%20pragmatics%2C%20and%20philosophy,discourse%20are%20attempting%20to%20answer.>)) from another angle -- say, funding -- does this strengthen or weaken our existing assessment?

Some people might think this is lightly "Bayesian" in the (somewhat annoying?) way people have come to use that term in conversation, but I think of it really through the lens of Simon and Gigerenzer.

A lot of the ability of people to analyze difficult questions comes from our ability to judge how a situation or search _unfolds over time_.

It’s like the famous [gaze heuristic](<https://en.wikipedia.org/wiki/Gaze_heuristic>) example. To catch a frisbee or flyball by figuring out where it will land is computationally impossible for the human mind (at least in the timeframe needed to move into position). 

[](<https://substackcdn.com/image/fetch/$s_!LZpV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd7b816a4-c083-4f6f-b25c-601c1fc2f9a8_964x501.jpeg>)

What we do instead is adjust our position as the ball is in the air by keeping a fixed angle of gaze and keeping the ball in view by running forward or backward. We track and react to the changes rather than plot the whole course from the start.

[](<https://substackcdn.com/image/fetch/$s_!3Va4!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff8818797-1abf-4382-a79d-a815c3e8d30c_766x529.jpeg>)

Search and catching a ball are very different activities, but both share an important quality. Humans can never have the full set of information they need to make a decision, but in watching closely how a search _unfolds over time_ we gain useful insights.

## Addition of the “Post-Round Update” (or surfacing directional cues in search)

With this in mind, I added the _post-round update_ feature a few days ago. I now explicitly ask the LLM to reflect (or mimic reflection, if that way of speaking bothers you) on what shifted between round one and round two. So, in addition to this:  

> 6\. When prompted for "another round," find if possible:
> 
> \- One source that conflicts with the majority view  
> \- One source that supports the majority view  
> \- One source with a completely different answer  
> \- Update the table with these new sources  
> \- A pattern where low quality sources say one thing and high another is worth noting

I also say _this_ :

> ### When asked for "another round"
> 
> It is OK if individual sources are biased as long as the set of searches together surfaces a range of viewpoints. For instance, a search for "MMT true" can be paired with "MMT false" etc. [hotkey="another round"]
> 
> **After showing the sources table after "another round" summarize what new information has come to light and if/how it changes how we view the issue or question. If the round has not discovered ANYTHING new, admit it is mostly reinforcing previous searches. Call it "Post-round update"**

This has led to a really interesting experience! For instance, the initial round on the walnuts was mostly about individual research findings — but the second round found a different angle. In a word, _funding_ :

[](<https://substackcdn.com/image/fetch/$s_!Gx4d!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbf9b2b87-3c4c-44d2-9daa-a5da95c34327_932x780.jpeg>)

This doesn’t mean that the walnuts and cognition claims are false. In fact, we’ll likely arrive at the heat death of the universe before anyone knows that with mathematical certainty. But it’s a directional cue — as we go deeper into the search, the additional angles are reinforcing the dubiousness of these claims, not finding unexpected support for them. 

Likewise, I reran the Wizard of Oz search I tried a bit ago. This is the one where in the first round it looked from the sources found that it was [nearly certain the snow in Wizard of Oz was made from asbestos](<https://mikecaulfield.substack.com/publish/posts/detail/164058561?referrer=%2Fpublish%2Fposts>), but the second round discovered evidence that the snow might have been crushed gypsum. In this case, as we go further into the question our certainty _dissolves_ and leans towards the opposite finding.

I noticed while I was doing that that I could read the signal — the _trajectory of the search_ — but realized for others it might be hard. In fact, having taught search for a decade and a half I _knew_ it would be hard. 

With the new post-round update however, the user’s attention is drawn directly to _what changed_. Here’s the update after the second round of search:

[](<https://substackcdn.com/image/fetch/$s_!ozvH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa3a1b6ac-b479-417c-964c-f8d5813fdf49_993x776.png>)

This to me feels so _good_. Not only because it is unlocking for many people a key insight in evaluating search, but because it’s _exhilarating_. It captures for me what I love about search — with a question of complexity (which is not all questions, but some!) search is _consumed_ and _processed_ as a _journey_. (There’s some additional rounds to this particular Wizard of Oz adventure that I will share sometime later — it was a real joy).

Of course, there are other cases where the additional information doesn’t change — or even reaffirm — a position on the core question, but adds richer context, as in this case with a search about a heartwarming story that turned out to be significantly misrepresented. The second round identifies interesting related issues:

[](<https://substackcdn.com/image/fetch/$s_!YpUr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F927c2ebd-8f54-40d6-b2a2-5236a5f5baea_1058x674.png>)

Again, these updates don’t have the inline links, but they are summarizing the linked sources in the sources table above:

[](<https://substackcdn.com/image/fetch/$s_!ibBM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fac4cdf16-e0f0-4b94-bb62-434303674596_1110x575.png>)

Anyway — get a paid version of Claude, [try out the prompting layer](<https://checkplease.neocities.org/>), and play around with your own modifications. Search is a journey, and I think we’re only at the very beginning of our journey with this tool as well.

(If you like this post you might also like t[his one](<https://mikecaulfield.substack.com/p/google-searchs-ai-is-or-should-be>) about how AI in search can be about reducing the cognitive load of the search process rather than replacing search altogether, which is sort of how I backed my way into building this tool. [There are other influences too which I can hopefully talk about in time])

Thanks for reading The End(s) of Argument! Subscribe for free to receive new posts and support my work.
