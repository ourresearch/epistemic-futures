---
title: "The Elmer's Glue Pizza Error Is More Fascinating Than You Think"
person: mike-caulfield
section: by
type: blog-post
year: 2024
date: 2024-05-25
venue: "Mike Caulfield's Substack (mikecaulfield.substack.com)"
authors: "Mike Caulfield"
source_url: https://mikecaulfield.substack.com/p/the-elmers-glue-pizza-error-is-more
retrieved: 2026-08-13
content: full-text
notes: ""
---

# The Elmer's Glue Pizza Error Is More Fascinating Than You Think

*The places where AI summary strikes out are often due to a mismatch between search quality and answer quality*

## Full text

You’ve probably heard that Google’s AI summary told people to put [Elmer’s glue on pizza to keep the cheese from sliding off](<https://www.theverge.com/2024/5/23/24162896/google-ai-overview-hallucinations-glue-in-pizza>). That’s bad advice, obviously. But like a lot of AI Summary errors its failure is much more interesting than your average ChatGPT hiccup, because it shows some of the tension between “search quality” (what forms a good result set for a prompt) and “answer quality” (what forms a good synthesis of a response). 

Let’s start with the basics of search. As Sam Wineburg and I talk about in [Verified](<https://www.amazon.com/Verified-Straight-Better-Decisions-Believe/dp/0226822060>), search cannot read your mind. By and large, the context of your information need is obscure to it. And that’s good, actually. We’ve decided quite rightly as a culture that we don’t want big companies recording us 24/7 so they can better understand what led us to Google “Do spiders give you acne?” at 3 a.m. There are some context clues that are minimally used — search history, location — but on the whole the core of intent has to be derived from the query. 

Thanks for reading The End(s) of Argument! Subscribe for free to receive new posts and support my work.

Since intent can’t always be accurately read,1 a good search result for an ambiguous query will often be a bit of a buffet, pulling a mix of search results from different topical domains. When I say, for example, “why do people like pancakes but hate waffles” I’m going to get two sorts of results. First, I’ll get a long string of conversations where the internet debates the virtues of pancakes vs. waffles. Second, I’ll get links and discussion about a famous Twitter post about the the hopelessness of conversation on Twitter:

[](<https://substackcdn.com/image/fetch/$s_!sTqP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcbea5d3c-81a6-4d1c-abab-2a4bb90f03a2_640x734.jpeg>)

For an ambiguous query, this is a _good result set_. If you see a bit of each in the first 10 blue links you can choose your own adventure here. It’s hard for Google to know what matches your intent, but it’s trivially easy for you to spot things that match your intent. In fact, the wider apart the nature of the items, the easier it is to spot the context that applies to you. So a good result set will have a majority of results for what you’re probably asking and a couple results for things you might be asking, and you get to choose your path.

Likewise, when you put in terms about cheese sliding off pizza, Google _could_ restrict the returned results to recipe sites, advice which would be relatively glue-free. But maybe you want advice, or maybe you want to see discussion. Maybe you want to see jokes. Maybe you are looking for a very specific post you read, and not looking to solve an issue at all, in which case you just want relevance completely determined by closeness of word match. Maybe you’re looking for a [movie scene you remember](<https://www.reddit.com/r/nostalgia/comments/bb9wrb/pizza_scene_was_my_favorite_part_in_a_goofy_movie/>) about cheese sliding off pizza. 

In the beforetimes, it would be hard to imagine a user getting upset that the cheese sliding query pulls up a joke on Reddit as well as some recipe tips. The user can spot, quite easily, that these are two different sorts of things. 

The problem comes when the results get synthesized into a common answer. To some extent, this is a form of “context collapse”, where the different use contexts (jokes, movies, recipes, whatever) get blended into a single context. 

And (with the caveat that I’m just guessing like the rest of us) — that seems to be what’s going on here. And it’s why AI summary seems to be failing in ways that differ from the normal ChatGPT errors. For instance a person putting “how many rocks to eat a day” into Google is almost certainly looking for the famous _Onion_ article that talks about that — it makes sense that that would be the top result, followed by a number of results saying, by the way, don’t eat rocks. A good **result set** has both. But when these get synthesized into a single **answer** , the result is [bizarre](<https://x.com/heshiebee/status/1793810016199197097>):

[](<https://substackcdn.com/image/fetch/$s_!-2iF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F55b99398-8955-4d99-8d08-3c1df491f63a_945x2048.jpeg>)

This is not the sort of output that you would expect if you prompted ChatGPT with a similar prompt, because ChatGPT is producing text off of the statistical likelihoods derived from a whole corpus, not a result set. (ChatGPT fails in other equally bad ways, for example, by just making things up — but it looks a bit different). Google is failing in a specific and different way here, and the new weirdness of the way it is failing is capturing the attention of people who have gotten used to “hallucinations” but haven’t seen anything quite like this.

What’s the answer to this? My guess is in the short term it comes down. Longer term the challenge is to figure out whether it is going to build on the strengths of the chorus of voices found in its result sets or continue to purée those results into something increasingly strange. As I mentioned in a previous post, that might mean leaning further into the summary as being a [summary of results](<https://mikecaulfield.substack.com/p/google-searchs-ai-is-or-should-be?utm_source=profile&utm_medium=reader2>) — describing what’s in the result set, complete with nods to sourcing, rather than trying to turn results answering vastly different questions into a single answer. Or maybe it means something else. But the feature probably can’t survive in this current form.

1

I realize of course that intent isn’t “read”, but rather the way the outputs are produced is designed to respond to the likely intent of the user _without_ understanding the intent, but that seems a level too deep for this post.
