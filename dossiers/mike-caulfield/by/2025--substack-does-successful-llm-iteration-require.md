---
title: "Does successful LLM iteration require previous knowledge of the right answer?"
person: mike-caulfield
section: by
type: blog-post
year: 2025
date: 2025-09-07
venue: "Mike Caulfield's Substack (mikecaulfield.substack.com)"
authors: "Mike Caulfield"
source_url: https://mikecaulfield.substack.com/p/does-successful-llm-iteration-require
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Does successful LLM iteration require previous knowledge of the right answer?

*Answer: No.*

## Full text

My recent post when shared on Bluesky brought the usual dozens of comments I get when I post about AI there. Counterclaims included that I was a “dipshit”, nazi-adjacent, a world-burner whose insistence on doing an additional query was going to result in a dramatic acceleration of global warming, a “lizard” (??), and repeated assertions that I obviously didn’t understand how simple it is to verify things through search (Yes, this said by people that apparently didn’t even click my profile to see the mention of the _book I wrote on the subject_. I am sure they are amazing at search). 

Interesting counterproposals included that I eat shit or be forced to live in a “sleeping bag filled with poop.”1

I actually kind of enjoyed the sleeping bag comment. At least it had some creativity.

In between this were a few comments that were repeated and worth replying to. The biggest was that “iteration” was just a way of saying “shake the 8-ball until it gives you the right answer.” This is a great insight into challenges with information literacy application! It’s also an issue that I already address. I deal with that in more detail here.

## It’s a good worry (but I answered it)

One of the most important pieces of any information-seeking process is what Herbert Simon called a “stopping rule”. And the challenge of stopping rules with verification/contextualization is simple — if you don’t know what the answer is how do you know when you’ve gotten to a verification/contextualization endpoint? 

There are various methods that humans use to do that. One of my favorite is this: As you look at competing theories as to what something is or means, you note which of the theories is accumulating new evidence most easily from the sort of sources that would be “in the know”, and which one has to go into more and more obscure sources for support. In a lot of cases you can see one theory pulling out ahead, and if each round of searching it continues to get further ahead you can use that directionality over time as a signal. 

That’s a heuristic that takes some time to learn. It’s complex, and it’s a bit about a developed feel. But my proposed method in the post wasn’t nearly that complex. It was, in fact, dirt simple: 

  * After the initial response, do a follow-up, every time. 

  * Every time?

  * Yes, every time.2

In other words it wasn’t so much “shake the eight ball until the answer is right” but rather “do a second round every time”. 

The reason I could say that is I spend a lot of time “testing the inverse”, something I learned long ago when developing the search methods that became SIFT. It’s absolutely true that most people when they test fact-checking methods test them only on things which are _wrong_ , which results in the development of faulty advice, since most things you’re likely to check are probably true. It’s one of the reasons that pre-SIFT information literacy training just made a lot of people _more cynical_. You can see how that works, right? If you only test on wrong things, the approach that tests best is simply to believe less of what you see.

Testing only on poor information didn’t work ten years ago with search, and it won’t work now with LLMs. So whenever you see me testing a follow-up prompt on something like this (an insufficient answer):

[](<https://substackcdn.com/image/fetch/$s_!28nJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde5a0239-306a-4fb8-9b75-79b0cc91c827_1521x760.png>)

I’m also testing it on something like this (a sufficient answer):

[](<https://substackcdn.com/image/fetch/$s_!_han!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb8e45276-8915-4282-ad2f-de5d7c07c6a3_1531x786.png>)

And what I am trying to do as I hone my library of prompts is to get a set of prompts that reliably improve the insufficient answers while (at the very least) not making the sufficient answers worse. That’s the target, because if you can develop prompts that do that then you don’t have to make a judgment about whether the first answer is right or wrong, you just run your follow-up every time. For instance, here is a follow-up to an initially correct response. You’ll note that the second round — which uses the same “sorting prompt” I used on the poor response — does not weaken the response:

[](<https://substackcdn.com/image/fetch/$s_!TgeT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2b4ad2d6-828b-4547-9aa4-925759cf7edf_1359x1777.png>)

The second round here does not give you a “different” answer, it gives you a more complete one with lots of supporting evidence. And while lots of follow-ups work, at least one piece of that here (over many claims analyzed) is a focus on categorizing evidence found: “What is the evidence for and against this claim.” 

I did say this multiple times in yesterday’s blog post, and it’s a shame people reading it missed it, because I actually think this strong tendency to preserve correct directionality under both conditions is _one of the most exciting things about these “balanced” follow-ups as a technique_. It’s exciting because there is _not_ a complex “heuristic by feel” that people have to develop; they just have to remember to apply _even-handed second round_ questioning, which will make both good and poor initial answers better. 

That’s not normally how things work with information technology. If the answers you need to a question are on the first two pages of Google results, there’s a not insignificant chance that going to page three will be a distraction or unproductive tangent. If the answers you need are on page three, telling people to stop at page two could do real harm. Generally we do see more concrete tradeoffs. But so far it seems like certain follow-ups have strong benefits with very little cost. Both the right answer and the wrong answer move in the same direction and converge. 

That’s unusual, and the exact _opposite_ of an eight-ball. And again, that’s what makes the follow-up approaches I’ve tested so incredibly intriguing to me.

1

I considered not mentioning the blowback, but I do want people I know in the field on the AI critic side to understand what the experience is of someone just trying to do work in AI literacy. I’m not saying it’s the fault of AI criticism, but be aware that a lot of people are super juiced up about this stuff. I don’t see how that’s going to help anything, especially if they are hell bent on going after anyone who wants to teach people to use AI more effectively.

2

The one exception to this is if the first round surfaces definitive sources (like the Fake History Hunter post, or the original Instagram post in this case). If you can ground the claim in strong external sources that have been surfaced, jump off the LLM train whenever you like.
