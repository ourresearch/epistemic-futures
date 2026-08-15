---
title: "Confirmation Bias in LLM Responses and Potential Educational Mitigations"
person: mike-caulfield
section: by
type: blog-post
year: 2025
date: 2025-08-30
venue: "Mike Caulfield's Substack (mikecaulfield.substack.com)"
authors: "Mike Caulfield"
source_url: https://mikecaulfield.substack.com/p/model-hedging
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Confirmation Bias in LLM Responses and Potential Educational Mitigations

*A couple notes on an interesting problem and some possible educational approaches to it*

## Full text

I’ve been interested in to what extent prompt language biases LLM responses, and a bit of a natural experiment fell onto my lap the other day. I thought I’d use it to explore the following questions:

  * Does the information in a prompt cause models to lean into one conclusion vs. another in ways that can be cleanly demonstrated and studied? 

  * Is that behavior keyword-driven or claim-driven?

  * Is that behavior symmetrical? I.e. when leaning into a weakly supported conclusion does it lean as strongly into it as a well-supported conclusion? 

  * Are there ways to mitigate this through prompting technique that can be taught and generally applied?

Anyway, here we go…

## The Example

Back in 2016, a company in Japan raised the price of a popsicle(-ish) treat by 10 yen, roughly 9 cents at the time of the announcement. 

[](<https://substackcdn.com/image/fetch/$s_!XF2N!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb7b5ba8c-b5e4-4079-a5cf-1d5e6620fbea_1165x345.png>)

They put out a national commercial apologizing for the increase.

[](<https://substackcdn.com/image/fetch/$s_!ymdA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F22563a9e-f318-48ef-9430-3d99e9814e9b_1055x1037.png>)

This was covered at the time, but also became a popular meme recirculated when inflation was spiraling upward around the world in 2022. People shared the meme as something happening in _2022_ , citing older reports. At _that_ time the exchange rate was a bit different, and some people writing about this and sharing memes computed the US$ equivalent as about 7 cents, based on exchange rates current in 2022. In subsequent years it’s been shared as “new” event multiple times, sometimes with the 9 cent figure, and sometimes with the incorrect 7 cent figure as being the 2016 cost, and sometimes with a note that 10 yen _is_ _currently_ 7 cents, and implying that the event just happened.

[](<https://substackcdn.com/image/fetch/$s_!qtwX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F220d39c1-dae5-4bde-9edb-ed1cf0120f3e_1185x427.png>)

This seems petty, right? I’d point out though that I haven’t found any reporting when it happened in 2016 get this wrong — the 7 cents is clearly an error that comes from not tracing stories to sources. And it’s technically a difference of almost 30% and while the yen does shift a lot, that’s not a trivial difference. 

So it’s a messy information context with both the 9 cent and the 7 cent figure floating around. What happens when we mess with Google’s AI Mode a bit by playing with our query’s assumptions?

## Right figure

First, I tested it by prompting with a query stating the correct figure. I found when the right figure is prompted it reflects it back consistently, and does not reference the seven cent claim at all.

[](<https://substackcdn.com/image/fetch/$s_!14ID!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2b99cd71-12bc-431a-96a9-e01ac48f2f60_1015x460.png>)

[](<https://substackcdn.com/image/fetch/$s_!Q9Pm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F23ada4d9-4955-45de-9c83-cefa29102813_1013x329.png>)

[](<https://substackcdn.com/image/fetch/$s_!P5rC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd45033ea-dae9-4b5e-8286-da536333c8e3_1035x408.png>)

[](<https://substackcdn.com/image/fetch/$s_!MgN2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feb25c402-ced1-4832-8056-6907bea8e3b4_995x434.png>)

[](<https://substackcdn.com/image/fetch/$s_!yHlt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3c236f08-95fb-4a6e-9c26-d3784d359101_986x438.png>)

## Wrong figure in wild prompted

Next I prompted it with the wrong figure — but not just any wrong figure, I used the one that floats around social media (i.e. present “in the wild”). When the wrong figure “in the wild” is prompted it agrees with the wrong figure.

[](<https://substackcdn.com/image/fetch/$s_!g2Bh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd71f6641-e88b-4b95-9f80-818dedadce6e_1035x461.png>)

[](<https://substackcdn.com/image/fetch/$s_!pqtG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff39b32a4-fe52-47ca-8615-e5f73e7ca780_1016x278.png>)

[](<https://substackcdn.com/image/fetch/$s_!99Ry!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0c45740a-5d3e-422a-9e07-8327b68c9613_1036x396.png>)

[](<https://substackcdn.com/image/fetch/$s_!jxZ0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5cb242d4-4dc1-40e5-ad16-a473d1ec198c_1047x335.png>)

[](<https://substackcdn.com/image/fetch/$s_!tzMD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcb5b18a1-830c-4acd-9005-a61579f52ee8_1030x341.png>)

## Wrong figure not in the wild (closer to right one)

So what happens when you give it a wrong figure not in the wild? For this I tried two variations. The first was a wrong figure that overshoots, and is closer to the correct 9 cents than the incorrect 7. 

When you give it a wrong (higher) figure that is not in the wild it correctly tells you you’re wrong, it was 9 cents, not 14. It does not reference the 7 cent figure.

[](<https://substackcdn.com/image/fetch/$s_!4aZt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F852d704c-1337-4d12-aa1a-9912db8e2dff_1054x320.png>)

[](<https://substackcdn.com/image/fetch/$s_!Pf2C!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4e458a58-b206-4483-8cc1-82a34a91a20c_1034x344.png>)

[](<https://substackcdn.com/image/fetch/$s_!SfM7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1136f101-ae75-4cfb-bbb2-941a32300174_1009x385.png>)

[](<https://substackcdn.com/image/fetch/$s_!j0zV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd0f28268-6e84-4a33-84ce-16896308da46_1033x411.png>)

[](<https://substackcdn.com/image/fetch/$s_!cdEs!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0faa0e90-47a0-4366-ac0e-16723c979422_1051x387.png>)

## Wrong figure not in the wild (closer to wrong one)

Next I tried undershooting, with a figure that is closer to the wrong result of 7 cents than the right result of 9 cents. 

This is where it gets really interesting — when you go closer to the wrong figure by shooting _low_ , five out of six responses involve _hedging_.1 It either cites a range (7 to 9 cents) or notes that it’s nine though “some sources” say seven cents. The other time it corrects the user to nine cents.

This is fascinating behavior for a number of reasons. First, it shows that this is not simply a keyword confirmation issue at play here — it operates at the level of the claim. If I had time I could run this query hundreds of times at different distances from the asserted amount in the claim, and we’d have something looking like the _shape_ of confirmation bias of AI Mode. (Someone reading this should do that I think?) But in particular, the asymmetry here is striking! There is clearly a stronger signal for the 9 cent figure than for the 7 cent figure. It puts a thumb on the scale less for the user through hedging.

[](<https://substackcdn.com/image/fetch/$s_!0x0_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc8b907e6-4890-44be-915d-71fd4ba2241f_1021x371.png>)

[](<https://substackcdn.com/image/fetch/$s_!8cQ_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcbb60f21-8a16-4f23-92eb-992c46eae2f7_1031x353.png>)

[](<https://substackcdn.com/image/fetch/$s_!yxAv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3bd62835-131d-48d7-842d-6b0596bf9b39_1037x266.png>)

[](<https://substackcdn.com/image/fetch/$s_!FSLx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F50dd3d0c-3b6f-44ad-ab53-e9f7069132bf_1017x652.png>)

[](<https://substackcdn.com/image/fetch/$s_!AIBc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fafe51e6c-ab9d-4041-809d-0946b7f4d29c_963x339.png>)

[](<https://substackcdn.com/image/fetch/$s_!qzmV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa9ccb809-68f7-4756-8ef2-6f8106343517_966x344.png>)

## Can better prompting get better answers? 

In this case if you ask directly, it will give you the right answer 10 times out of 10. 

[](<https://substackcdn.com/image/fetch/$s_!qc6v!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc75ba8a6-882d-4690-a433-3d222613bf74_1013x390.png>)

This leads to a bit of a dilemma for me. There are very good reasons for people to put a full claim in as a prompt, because that helps surface the questions they don’t think to ask. There’s also a strong propensity argument for that — it’s easier to put in a claim that you copy in than think out a question, and you’re going to be more likely to do that. But there’s also indications here that the choice of claim details can influence the way the process weights various sources.2

The broader piece is that usually someone is not looking for this level of detail when they seek an answer. Usually they do just care that there was an increase. 

One possibility is that the issue could be dealt with through follow-up questions, though some work and some don’t. For instance, if you ask it to SIFT in a follow-up, you get the context. Here’s part of the response to this follow-up:

> “Where did this claim come from? Use the I in SIFT (Investigate the Source) to do a lateral reading analysis of what the various people involved with this tell us about the claim.”

[](<https://substackcdn.com/image/fetch/$s_!2p9x!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F500357b9-e743-4d55-89c2-501b1dc12d97_915x616.png>)

The follow-up “facts and misconceptions about what I posted” also surfaces the hedge, though it misattributes it to fluctuating rates at that time:

[](<https://substackcdn.com/image/fetch/$s_!n4Wz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe6d6fedd-815a-41b0-9529-18036fc9ef8b_923x657.png>)

However, clicking on the citation link gives you three sources to choose from — a Facebook post (which has the wrong figure), a Yahoo Finance page (with the right number), and a Quartz article (with the right figure).

[](<https://substackcdn.com/image/fetch/$s_!s4Uy!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb6d9c07b-b81c-4307-a3a7-98ada9942c97_506x630.png>)

At this point it’s very much a SIFT exercise — choose the source that is the best fit for the question. And I think that could be fine?

## A Non-Conclusion

This is not a typical example, of course. People usually are looking at much more complex claims than this. But it’s such a contained example it’s interesting to explore, because it lays bare some system dynamics and raises questions about what methods students should use to navigate them. What I think I’m coming to is this:

### Reading the “Result Page Vibe” Still Matters

Here’s the correct “9 cent” response:

[](<https://substackcdn.com/image/fetch/$s_!sNcL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9e4f51e1-9475-49a2-bed8-8af07b0433de_1520x702.png>)

And here’s the incorrect “7 cent” response:

[](<https://substackcdn.com/image/fetch/$s_!-ymd!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F05a47f2c-4982-4422-ae1f-d5bfb45642ee_1506x711.png>)

Notice the difference in the sources in the right column? The sidebar for the correct response starts out with Yahoo Finance and The Independent. The second is topped with social media posts.

Notably, if you click on the citation link for the graf that cites 7 cents, the bottom article ends up being a Business Insider article that cites 9 cents — it’s just a bit buried.

So for details like this in AI Mode _this is still search_ , and you’re still using SIFT in a sense, just with a bit of synthesis upfront. There’s a part of my book with Sam Wineburg ([Verified](<https://www.amazon.com/Verified-Straight-Better-Decisions-Believe/dp/0226822060>)) which talks about the “reading the result page vibe” in order to think about what information neighborhood your query has dropped you into, and it turns out that is still very much a necessary skill here. If that sidebar is full of reputable sources maybe you jump over to those. If you see nothing but Facebook in that sidebar you may want to check your assumptions and retweak the query — just as you would in traditional search.

## Follow-ups might be a solution, but research will be key

In some research I’ve done I’ve tested a wide range of carefully constructed follow-up queries, like:

  * Read the room: what do a variety of experts think about the claim I posted?

  * Facts and misconceptions about what I posted

  * Where did this claim I posted come from? Use the I in SIFT (Investigate the Source) to do a lateral reading analysis of what the various people involved with this tell us about the claim.

In general what I found is that many times they lead to better answers, sometimes they don’t, and it’s quite rare that they make things worse. That makes me think that teaching good follow-ups could be a promising intervention. In this particular case many items in my library of follow-ups surfaced the issue the pricing issue when used as follow-ups to the wrong answer.

This is a place where educational research will be important. If students kept such follow-ups in a file, would they use them? Could they apply the right follow-up for the right issue effectively and significantly improve answer quality? And how do follow-ups compare as a strategy to having them jump to direct sources when it comes to getting good context?

Questions it would be great to have some funding to investigate! It’s too bad that research funding seems to have collapsed just as these types of questions are becoming so important. There’s an opportunity here to combine research into model accuracy and layer on top of it projects that take that research and try to turn it into curricula for skills development — and then test those educational interventions. I think that would be to the benefit of platforms, educators, and users. It’d also be a lot of fun, which is something we could all use more of right now.

To wrap up: 

  * Does the information in a prompt cause models to lean into one conclusion vs. another in ways that can be cleanly demonstrated and studied? (Answer: yes.)

  * Is that behavior keyword-driven or claim-driven? (Answer: possibly both, but some of it definitely happens at a higher level of abstraction than keywords.)

  * Is that behavior symmetrical? I.e. when leaning into a weakly supported conclusion does it lean as strongly into it as a well-supported conclusion? (Answer: no, it is definitely asymmetrical). 

  * Are there ways to mitigate this through prompting technique that can be taught and generally applied? (Answer: maybe? That’s a really complex question that needs educational research on it).

Anyway — a bit of a ramble, but I hope you found the weirdness of the results as interesting as I did, and I hope we can all work together to think about what skills people need to navigate these new spaces.

1

I meant to run a consistent five runs here but mucked it by mistake and did six.

2

Yes I know it’s not weighting sources in the traditional sense, but the effect is roughly the same.
