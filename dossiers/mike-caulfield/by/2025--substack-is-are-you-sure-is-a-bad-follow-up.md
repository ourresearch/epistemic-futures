---
title: "Is \"Are you sure?\" a bad follow-up prompt?"
person: mike-caulfield
section: by
type: blog-post
year: 2025
date: 2025-09-09
venue: "Mike Caulfield's Substack (mikecaulfield.substack.com)"
authors: "Mike Caulfield"
source_url: https://mikecaulfield.substack.com/p/is-are-you-sure-is-a-bad-follow-up
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Is "Are you sure?" a bad follow-up prompt?

*A very minimal test with some fairly clear results. (The answer is yes, it's bad)*

## Full text

One of the responses I saw a couple of times to my [post on iteration and prompting](<https://mikecaulfield.substack.com/p/is-the-llm-response-wrong-or-have>) went something like this: “When I use to use LLMs and got bad results, I would ask if it was sure and it would _just double down_. So no, ‘iteration’ doesn’t help.”1

It’s telling that that’s what a lot of people assumed I meant by iteration. My point wasn’t _simply_ “say something after the first response” but rather “try following up with _balanced statements_ that focus on _evidence_ and the _discourse environment_ ”. I provided a list!

[](<https://substackcdn.com/image/fetch/$s_!uPMM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcdf718fa-5812-430b-bd21-ee784bc929a2_974x575.png>)

Further, I _share_ the opinion that “Are you sure?” is a particularly bad follow-up prompt. My experience with it has been very similar to what the critics of my post alleged about it. I agree with them. When I use “Are you sure?” the system responds kind of like a person challenged in this way, giving me a list of _reasons why it’s sure_. It does feel _defensive_. It was in part my frustration with these sorts of “are you sure” prompts that led me to design the sorting prompts2 I now recommend. 

That said, I like to test my assumptions. So I decided to run a little mini-assessment.

## Is “Are you sure?” a bad prompt?

It’s quite hard to test and demonstrate this for the same reason testing and demonstrating any of this is hard. To test something like this I have to get the LLM to generate an clear error consistently enough to generate multiple runs, then use follow-up prompts on each of the runs. When I do what I’m about to do now, and demonstrate the behavior online, the demonstration enters the search record which then (usually) fixes the error, and I can no longer use the example for tests or demonstrations. I call this process “burning” my examples, and it _hurts me_ , because it’s actually very time consuming to find interesting errors about textual claims that can be consistently generated, and I hate to lose them.3

But I think it’s worth it for this one. So let’s burn an example for the greater good.

Here’s our challenge. I discovered last week that when we ask AI Mode for quotes on honesty from Douglas Adams, author of Hitchhiker’s Guide to the Galaxy, we will often see a specific bad quote in there: 

> “To give real service you must add something which cannot be bought or measured with money, and that is sincerity and integrity”

[](<https://substackcdn.com/image/fetch/$s_!6rZ7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd80f1610-73b9-4f81-838a-ba181b8b38d0_881x245.png>)

That quote _is_ broadly attributed to Douglas Adams on the web. The LLM is not hallucinating. It is, however, repeating dumb stuff found on the internet that it should be able to see is dumb. The vast majority of humans get this wrong too, of course, but it’s not a hard call.

The quote actually comes from _Donald_ Adams, as noted by Forbes, [Quote Investigator](<https://quoteinvestigator.com/2020/09/17/integrity/>), and a number of other reliable sources.

[](<https://substackcdn.com/image/fetch/$s_!0g2B!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3ba14ced-7de7-452b-bbb5-e08ece31e493_1761x761.png>)

That Adams is known not for writing novels and radio plays, but for rising to the presidency of Rotary International in [June of 1925](<https://www.nytimes.com/1925/06/20/archives/new-haven-man-heads-rotary-international-donald-allison-adams-vice.html?unlocked_article_code=1.kk8.h_My.UiKppSLVy8FJ&smid=url-share>):

[](<https://substackcdn.com/image/fetch/$s_!570z!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F68c64357-64fd-4f33-bf96-0066b6c6e3c1_808x534.png>)

More at [Quote Investigator](<https://quoteinvestigator.com/2020/09/17/integrity/>), which tracks it down to the August 1926 issue of _The Rotarian_ magazine.

That makes a bit more sense, right? So lets see if we can generate ten instances of this attribution error in AI Mode and see how “Are you sure?” competes against a sorting prompt, five runs apiece.

Ok, ten bad responses generated. We’re going to randomly assign them a variation of the “Are you sure” prompt or the balanced evidence prompt. _On y va_!

# Round 1: “Are You Sure?” Test

Using the follow-up “**are you sure about these attributions**?” we are able to push 40% of our initially bad responses to the truth or close to it. The majority do not get significantly better and 20% get worse. (Sorry for doing percentages on such a low _n_ — but I do want to highlight that one out of five getting worse is pretty bad).

## Improved: 2

These results either lean towards the correct answer (and identify the Donald Adams counterclaim) or get the correct answer.

[](<https://substackcdn.com/image/fetch/$s_!AbFA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1168fec8-c66d-4c5c-ac95-fbbeacd4e189_803x185.png>)

[](<https://substackcdn.com/image/fetch/$s_!2N7h!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F50705f11-59bc-401a-94dd-54f2267838cd_824x302.png>)

## Doubles-down or no significant improvement: 2

[](<https://substackcdn.com/image/fetch/$s_!H7CF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff474ed19-e5ef-49eb-bf60-ce4e98092f03_807x228.png>)

[](<https://substackcdn.com/image/fetch/$s_!-BDL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fab3f92eb-0856-4f9b-9289-154737abc3f2_793x212.png>)

## Gets Worse: 1

This is a bit concerning — in this case the follow-up makes the situation worse. It is now credited to an unnamed “novel”.

[](<https://substackcdn.com/image/fetch/$s_!5koL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5108a6fc-bd9b-48c8-872c-f49b9653cbf2_842x218.png>)

# Round 2: Sorting Prompt Test

We try a sorting prompt here, to see if it improves results. It does! Dramatically! In this case the responses improve 80% of the time, and 20% of the time there’s no improvement.

Our sorting prompt is:

> _what is the evidence for and against each above quote's attribution?_

## Improved: 4

[](<https://substackcdn.com/image/fetch/$s_!e459!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F56726c6a-5b5a-4db9-8320-1eacb2b41c4b_837x543.png>)

[](<https://substackcdn.com/image/fetch/$s_!Jzst!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd5f87846-cc85-4f9a-b159-14ccc005605f_826x364.png>)

[](<https://substackcdn.com/image/fetch/$s_!vlyz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6ca7df61-bf54-4898-ace7-239a08b2b15b_827x450.png>)

[](<https://substackcdn.com/image/fetch/$s_!MWha!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe8f2efde-5b73-4602-9581-4c1100c239c0_876x608.png>)

## No Significant Improvement: 1

[](<https://substackcdn.com/image/fetch/$s_!RiP8!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7aa52b19-ba93-4595-85cb-39356ca4cb39_850x294.png>)

# Conclusion: Stop saying “are you sure” as a follow-up prompt and use a sorting prompt instead.

Sorry this post is a bit of a mess — I’d love this to be a whitepaper with carefully formatted screenshots, a nice appendix, and a couple more examples. I’d love to set up a rubric, compute statistical significance, get everything rated by three raters after a norming session.

I plead “having a day job”. 

Lucky for us, even with small run sizes the pattern is clear. 

I used a simple standard for improvement. To qualify as significantly improved, the treatment had to either:

  1. Find its way to the _Donald_ A. Adams citation, or

  2. State the quote is most likely falsely attributed (not just say it’s hard to source).

With that standard, the results showed a clear split:

  1. The “are you sure” prompt improves some responses. But even if _mostly harmless_4 it did produce in one of the five cases a worse answer, one that went from attributing it to Douglas Adams to claiming it was _in a Douglas Adams novel_ — an attribution that does not even show up in the search results. 

  2. The evidence sorting prompt performs dramatically better, improving 80% of responses, while not making the remaining response significantly worse.

Do I wish that we could run each of these 50 times, and add other variations? Sure. Every time I sit down and run my little tests on prompting technique I think of the immortal words of Jerry Garcia:

> “Someone has to do something. It’s just incredibly pathetic it has to be us.”

I’m _embarrassed_ it’s a run of just five, even if that’s four more tests than most people run. We should be scaling up tests like this. Instead we’re just getting a lot of AI influencers stating what they _feel_ works, and we’re going to end up basing curricula on vibes, I guess.

How do we get beyond me doing this at night while watching British crime dramas to something we take seriously? How do we create a long-term, research-driven program to help students get better at prompting the way SIFT was a research-driven approach to them getting better at search?

I don’t know! But I think we need to get there.

In the meantime, however, stop asking LLMs if “they are sure” and try some evidence and argument focused follow-ups, [as detailed in the previous post](<https://mikecaulfield.substack.com/p/is-the-llm-response-wrong-or-have>). Better follow-ups make for better responses, and they aren’t that hard to learn.

1

This recreation removes significant swearing and insults.

2

Sorting prompts are defined in previous posts, but in summary they ask the system to put different bits of evidence or sources in different “buckets”, like “list the evidence for and against this claim.” What I’ve found is that process makes them better at coming to well-grounded conclusions. Somehow explicitly asking them to categorize evidence, sources, types of publications, whatever, seems to dramatically improve the overall judgments they provide vs. just asking them to make those judgments directly.

3

For the record it’s very easy to generate bad responses to images, but good textual claim screwups are harder.

4

Yes, this is a HHGTTG joke.
