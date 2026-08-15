---
title: "Ambient misinformation"
person: mike-caulfield
section: by
type: blog-post
year: 2024
date: 2024-06-28
venue: "Mike Caulfield's Substack (mikecaulfield.substack.com)"
authors: "Mike Caulfield"
source_url: https://mikecaulfield.substack.com/p/ambient-misinformation
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Ambient misinformation

*Even when giving you the "right" answer, LLM output can misinform along the way*

## Full text

One place where LLM output _could_ serve a legitimate role is where questions are fuzzy or involve a couple of research steps. These are cases where getting to the right answer involves keying off of multiple embedded queries.

For instance, I might be looking for the answer to “In what other shows was the actor on LOST who plays the character who sells things in?” That’s actually a _series_ of things that need to be solved:

Thanks for reading The End(s) of Argument! Subscribe for free to receive new posts and support my work.

> in what other shows was (the actor on lost who plays(the character that sells things on LOST)))

It’s got dependencies. 

  * The first question is who is the character on lost who sells things. 

  * The second is who plays him

  * And the third is what shows might I know him from. 

These need to be solved in sequence. If I type a question like “where do I know the actor that plays the guy on lost that sells things from” I am going to get nothing particularly useful. Google doesn’t _just_ use keywords to return searches anymore, but it’s still largely got that engine underneath it. 

[](<https://substackcdn.com/image/fetch/$s_!TRVV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe6e1d976-f710-4176-a6b2-e75b7dc08b3a_711x558.png>)Not so helpful results. 

Now if you know the character’s name is Sawyer, instantly you get a good search result: his name is Josh Holloway, he was in _Colony_ and _Mission Impossible: Ghost Protocol_. But that first step is difficult.

AI results have often been offered as a solution to these dependent queries. Interestingly, for this question the answer that Gemini gives you is _useful, but bad_. It’s useful because it does give you the name Sawyer, and that in turn gives you a decent list of where you might have seen Josh Holloway in two steps:

[](<https://substackcdn.com/image/fetch/$s_!WWCY!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F385eca5a-0368-494e-99de-0b22aa456d78_931x573.png>)Response saying Sawyer, Mr. Eko, and Charlie all might have sold things. The only one that sold things on the island was Sawyer, smuggling isn’t really selling things, and Charlie never sold anything at all.

[](<https://substackcdn.com/image/fetch/$s_!fSXj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0a7c7a0f-1c1c-43b5-b290-1a98eb8923f6_979x599.png>)A decent list of what the actor was in

Along the way, however, it manages to imply — without any evidence — that since the character Charlie Pace was a drug addict _he quite possibly sold drugs_. Note that there is nothing in the series that implies this — the implication here is just “people do drugs are often drug dealers”. I imagine this is in part statistical momentum from the mention of Mr. Eko, the drug smuggler in the previous bullet. Otherwise why not also Locke, who was an assistant manager at a toy store? Or Hurley, who sold chicken? In fact, why is Mr. Eko here for smuggling when those others are not here for actually selling things?

It’s an absolute mess that shows how even when getting you to the right answer LLM output can reinforce harmful stereotypes. 

Note that this isn’t a trick question or a particularly odd one. And its result is not as dramatic as the Elmer’s Glue pizza. But it feels more insidious to me somehow.

## Transparent assistance as an alternative

One thing I’ve been playing around with is AI for transparent assistance with search — that is instead of looking to AI for the result, look to search for the result but have AI help you formulate that search. It’s just one data point, but in this case that works really well. You request a search with the dependencies…

[](<https://substackcdn.com/image/fetch/$s_!6hRL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7b559880-deaf-4558-95b4-16286ec7daef_1127x264.png>)Gemini result of asking for a search reformulation, it suggests Lost actor who plays Sawyer

And then you execute it:

[](<https://substackcdn.com/image/fetch/$s_!9XFI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F33c39a45-b70d-4c3e-b66b-4e01899468bb_1937x1040.png>)Results of the reformulated search. They are pretty good, and answer the question: Colony and Yellowstone.

This actually gets you a pretty high-quality result, and allows you to tap into the richer Google Search interface. In this case it also sidesteps calling drug addicts dealers, which is good.

Of course, this is clunky here, but it’s evidence that were the connection more fluid there might be some use in having this tech formulate such dependent queries or suggest them, rather than provide AI-produced results. 

Thanks for reading The End(s) of Argument! Subscribe for free to receive new posts and support my work.
