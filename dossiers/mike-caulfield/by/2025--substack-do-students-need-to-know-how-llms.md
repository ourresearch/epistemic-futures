---
title: "Do students need to know how LLMs work, or to predict how they'll act?"
person: mike-caulfield
section: by
type: blog-post
year: 2025
date: 2025-09-12
venue: "Mike Caulfield's Substack (mikecaulfield.substack.com)"
authors: "Mike Caulfield"
source_url: https://mikecaulfield.substack.com/p/do-students-need-to-know-how-llms
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Do students need to know how LLMs work, or to predict how they'll act?

*A little venting about what educational explanations are for...*

## Full text

Here’s a photo I uploaded to ChatGPT 5 today:

[](<https://substackcdn.com/image/fetch/$s_!0cfM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F99a27d42-42fd-4037-84e9-b312bdeb1138_597x709.png>)

And here is the response which tells me these are soldiers (correct) in remarkable precision (correct) making a human face in profile (nope).

[](<https://substackcdn.com/image/fetch/$s_!W2Yh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdbcaecf6-95aa-4aa5-84b5-beb08c26c001_963x489.png>)

I ran it again using ChatGPT instant and it told me it was soldiers (correct) carefully arranged (correct) in the shape of an arrow (nope).

[](<https://substackcdn.com/image/fetch/$s_!1Oii!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff89bee5d-3eff-440f-a1bf-33928340d990_932x355.png>)

Ran it a third time, it told me, aha! it’s soldiers forming a pipe (but _ceci n'est pas une pipe_):

[](<https://substackcdn.com/image/fetch/$s_!X9dO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F46631131-dfdc-4cbb-a7ad-f3d2c1cf939d_958x453.png>)

As I am aware of no famous “living photograph” of the time that was a pipe, this would qualify as a hallucination.1

So this is weird behavior, and I cannot tell you with any certainty what chain of events _causes_ it.2 I can tell you the way that _I_ _conceptualize it_ , one that allows me to use the platform better. 

There is a party game where you have to describe something but you can’t use certain words. Your partner has to guess what you are describing. 

In my little mental model of this, you can’t use the word “horse” because the system can’t “see” the horse. And so the behavior is the sort of thing you’d get if you said:

> “The men are soldiers in a carefully structured formation seen from above, there are mostly soldiers in dark uniforms, they fill up the right side of the photograph but the left side forms a triangle with a rounded bottom, with the top of the triangle wider than the bottom. There is a streak of soldiers in the center forming something like a ‘K’ or an ‘X’. What is this?

Could that be a pipe? An arrow?

What would you guess?

If you think through that pattern, then the fact that Google’s AI Mode replies to this AI photo

[](<https://substackcdn.com/image/fetch/$s_!X6so!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc84745a7-17e1-4f37-8878-01385b19bb58_600x675.jpeg>)

with this response claiming that the building just _has to be_ that weird “Communist KFC” in Minsk…

[](<https://substackcdn.com/image/fetch/$s_!3dr8!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fef611555-75b1-4fab-b0b5-bb61ad40b96f_1359x702.png>)

Which in reality looks like this…

[](<https://substackcdn.com/image/fetch/$s_!XRS9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F458e5fc0-821f-4962-8295-ee66e3253b42_960x640.jpeg>)

…is more predictable and expected. A student can understand how a verbal description of the AI image gained either from computer vision or related comments (“a concrete KFC, brutalist,3 kind of communist looking”) could lead to someone saying, “oh, you’re talking about that building in Minsk!”

Likewise, a student with this “party game” model of how it acts might realize they could improve performance by giving the model some obvious words that might not be so obvious to it, like mentioning this looks like a horse’s head…

[](<https://substackcdn.com/image/fetch/$s_!6jbt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F97e740a7-866f-4b8b-a335-d4b978c75f8a_595x498.png>)

… so that the model could do (much) better at this game, even on ChatGPT instant mode:

[](<https://substackcdn.com/image/fetch/$s_!Udof!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F76b05f38-f878-45c6-8c9e-bef8456322f1_984x578.png>)

And that’s the point of explanations, at least from the educational side of things.

## Good explanations help you do things

I think there’s an idea among some in AI literacy that we’re going to show everyone 15 hours of videos on embeddings and vector space and that’s going to make them better at prompting or understanding AI outputs. But that’s clearly not the case.

Likewise, I think some people recoil at things like the party game analogy. After all, underneath the hood no process is “guessing” anything; it’s rolling the dice and taking a path through statistical probabilities, but _guessing_ implies a motive or end that can’t possibly exist. The system doesn’t “know” it’s looking at a horse’s head but it also doesn’t “know” it’s looking at soldiers. And obviously it has no concept of a “game” at all.

I’m pretty insistent that we teach students that LLMs are not intelligences in the way we normally think about intelligences. But they also need little ways — mental models — to think about the challenges they hit using these systems. There’s a saying that “all models are wrong, some are useful”4 That is not meant to apply to folk analogies specifically, but the general principle that usefulness is the point of a mental model applies equally well.

Coming from educational research and design, I think about the little toy models and analogies we give students through this lens. Is the “party game” analogy good? i don’t actually know! From an educational standpoint I _can’t_ really know until I use it to teach students and see if it helps them make better decisions about how to query systems and assess the results. What I do know is that the model of “stochastic parrot” — whatever its mechanical validity — is no help at all with these (specific) tasks as it cannot help a user conceptualize productive course of action given an image identification issue. And the same holds true with a deeper knowledge of LLMs. I don’t believe the path to better working around this image issue is “Read Stephen Wolfram’s 2023 explanation and reapproach.”

These explanations are useful for certain types of things. The parrot analogy does other things in terms of expectation setting and dampening LLM mysticism. Wolfram’s explanation is great and helpful in other ways. My point is that neither a very detailed explanation of how LLMs work or analogies about parrots are useful in this _specific_ way, and people need room to propose and refine new analogies that may be educative without people jumping on every thread and explaining that _well, actually_ everything we’re looking at is a set of bits flipping state. 

So next time you see an educator proposing an analogy, consider asking to what extent that analogy might guide more adept use of the technology, and press on _that_ question. Does it help predict? Does it match a range of behavior? Does it undermine performance in other ways?

Good educational analogies are hard to develop and valuable when found; let’s not _well, actually_ them to death.

1

There is a famous living photograph of Woodrow Wilson in profile, which qualifies as a face in profile, but this is a stretch too. Part of what is happening here is that because there are a limited amount of living photographs in 1919, they are almost all noteworthy, which means the concept of famous is pretty tightly tied to the concept of living photographs as a class.

2

As usual, I play down my knowledge here a bit because I don’t think it is central to what I do or argue. Please do not jump in the comments to explain to me how embeddings work.

3

I love brutalism and know that the Soviet building is decidedly _not_ brutalist, but it is the sort of thing people misclassify as brutalism.

4

Quote by statistician George Box, attribution and provenance [here](<https://blogs.sas.com/content/iml/2025/04/02/all-models-are-wrong.html>). Probably more important than the quote is his explanation in the 1976 paper “Science and Statistics”: “In applying mathematics to subjects such as physics or statistics we make tentative assumptions about the real world which we know are false but which we believe may be useful nonetheless. The physicist knows that particles have mass and yet certain results, approximating what really happens, may be derived from the assumption that they do not. Equally, the statistician knows, for example, that in nature there never was a normal distribution, there never was a straight line, yet with normal and linear assumptions, known to be false, he can often derive results which match, to a useful approximation, those found in the real world.” I am aware that Box is mostly talking about parsimony, not analogy. I am not implying “folk” explanations of the sort that I propose have the validity of scientific reductions. I do believe however they have to be judged on usefulness, not the false lure of mechanical accuracy. Models are supposed to help you do things, and I think the same applies to folk analogies.
