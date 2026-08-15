---
title: "Calculating inflation with ChatGPT"
person: mike-caulfield
section: by
type: blog-post
year: 2023
date: 2023-05-20
venue: "Mike Caulfield's Substack (mikecaulfield.substack.com)"
authors: "Mike Caulfield"
source_url: https://mikecaulfield.substack.com/p/calculating-inflation-with-chatgpt
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Calculating inflation with ChatGPT

*An investigation with help from Katie Caulfield*

## Full text

One of my main interests at the moment is the ways in which AI intersects with sense-making and information seeking. The following is a bit of experimentation to tease out problems that my daughter and I engaged in last night. 

## The Problem: How much did my parents house cost in 1984 in current dollars? 

For a lot of my young life, my parents didn’t have that much money. But when I entered high school my father got a big promotion and a raise, as well as landed an outside lucrative outside consulting gig, and we moved from our hick town in Massachusetts (said lovingly — I don’t deny my hickness, which is rooted deep in my soul) to the suburbs of New Hampshire.

Thanks for reading Mike Caulfield's Hapgood! Subscribe for free to receive new posts and support my work.

The move felt extravagant and the house gigantic for a group of kids who thought going out to the Pizza Hut three towns over twice a year was the height of fancy. We had finally made it. The house has a downstairs half-bathroom, an office for my dad. We still slept me and my two brothers in the same room, but it was a _big_ room. And we moved from having a house that faced a cow pasture to a block that felt like those suburban blocks you saw in films like _E.T._ , and, about the time we moved, _The Goonies_.

At the time that house was about $100,000. So controlling for inflation, how much would that be now? 

This was a real question that came up recently. And it seemed a worthwhile topic to explore.

First, let me say I fully realize the problems that ChatGPT has with computation. I don’t claim this is the best use for ChatGPT. There are plenty of things I use ChatGPT for where it works well — it can be an incredible tool. But as people turn to LLM-based tech for _answers_ it’s important to show where they shine, and where they fail. (Also this will be one in a long series of exploratory walkthroughs, this is not the only test).

## First step: The Google Search Way

So our first step is to try Google Search to get a baseline. I thought two things going into this: first, I thought it would be complex to get this through Google (as opposed to Wolfram Alpha). Second, I thought while it would be at least somewhat difficult, my daughter and I would get the precise answer. Neither of these things were true.

### Finding an answer through Google was easy

First, we formulated our question in a way to give ChatGPT a chance. We know that ChatGPT has no access to data after September 2021 so the question we choose for Google was “How much would 100,000 in 1984 dollars be worth in 2020?” 

We immediately got a featured snippet that gave us a figure:

[](<https://substackcdn.com/image/fetch/$s_!gskX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa6856136-fe46-4f23-b623-c25b72bf824c_1120x967.png>)

Katie, however, is a recent college graduate with a demography degree, so she immediately spotted the Bureau of Labor Statistics link downpage. 

[](<https://substackcdn.com/image/fetch/$s_!o2qU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa3f9c929-a9fd-4f14-8595-887c292c7d24_1120x606.png>)

Even if she didn’t have that advantage, the vertical dots would help a browser quickly figure out this was a high-quality source:

[](<https://substackcdn.com/image/fetch/$s_!Pnjl!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8f120df3-65b5-47c7-b37d-ee41a062759e_642x795.png>)

Going there we put data into their calculator:

[](<https://substackcdn.com/image/fetch/$s_!DJB1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F852091f6-498b-47a9-9208-e296408e4ac0_702x467.png>)

The whole process took under a minute. 

So here’s the two surprises here. First, **the process went more quickly** than anticipated. I had forgotten that there were so many custom tools for this sort of thing.

The second observation is **the process was less definitive than I expected**. We got an answer at BLS that can be cited and sourced — so it’s definitive in that way. But even in executing this one minute task we were exposed to two different answers. Out of curiosity, we dug in a bit, but had trouble isolating what the difference in computation was. Our best guess was that playing around with the start months — for instance, doing July to July — shifted it very close to the other figure, but that was only a guess. 

Still, this was the granularity we wanted. It doesn’t deal with the fact that housing is a factor in CPI and a million other things, but it gives a sense that that house was considerably less than the current median house price of ~450,000. It’s also enough to know that the home price significantly outpaced inflation (if Zillow is correct it’s worth over $480,000 now). 

## ChatGPT

Again, I know that ChatGPT is bad at anything with computation because it doesn’t compute. But we wanted to see how close it would get and what it would take to get there.

We used ChatGPT 3.5. We struggled at first, it kept telling us it could not give us a figure for 2020 because it only had BLS data to September 2021. Once we got past that (mainly by arguing it did have the data) it told us the average inflation rate was 1.7% during those years (wrong), and told us the figure was around $180,000 (also wrong and not actually matching the calculation it showed us).

We then asked it to give us an equation that we could put in Google to calculate it, to make sure it used BLS data, and to use that BLS data directly in the calculation. And at that point after 20 minutes of fighting it, it got it in the ballpark:

> I apologize for the confusion in my previous response. To provide you with the accurate CPI value for 1984 according to the U.S. Bureau of Labor Statistics (BLS), I'll provide you with the information.
> 
> According to the BLS, the Consumer Price Index (CPI) for 1984 was 103.9. Please note that CPI values are subject to revision, so it's always best to consult the official sources or the BLS website for the most up-to-date and accurate information.
> 
> Now, using this information, you can compute the value of 100,000 1984 dollars in 2020 using the formula:
> 
> Value in 2020 = (CPI in 2020 / CPI in 1984) * Value in 1984
> 
> Substituting the values, the calculation would be:
> 
> Value in 2020 = (258.81 / 103.9) * 100,000 = 248,780.09
> 
> Therefore, the value of 100,000 dollars in 1984 would be approximately 248,780.09 dollars in 2020, adjusting for inflation based on the CPI.

That seems good, except of course we took the equation it provided and put it in and it turns out that it does not equal 248,780, but rather 249,095.

Those that know ChatGPT know what’s going on here. ChatGPT is doing two things rather separately. It’s telling you the sort of thing a person might say when asked when asked what the inflation adjusted value is. And then it’s telling you the sort of thing a person might say when asked to explain why that is true. But there is a big difference here, because normally when we tell someone how we got to a number we are actually explaining a way that we got to it. Here, the way it got to it is an LLM process that isn’t math. The explanation — the argument — is divorced from its underlying production and the two are out of sync. 

Also notice here how much we had to know to push it towards this correct solution. We had to know about the BLS, we had to spot the 1.7% inflation rate it initially mentioned was wrong. 

As a postscript, while I was putting this together I reran a query in ChatGPT, but this time typed “what **was** the value of 100,000 in 1984 dollars in 2020” instead of “what **is** …” and got a new answer — not 248,780 but 274,652 — well outside the range of other estimates. Of course, since ChatGPT changes answers even with the same prompt, I don’t know if that was the wording or if it it was just an effect of running it again, and the dice rolling a bit differently.

We also used ChatGPT 4. ChatGPT-4 acted much the same when asked about 2020. We did ask about the value of 1984 dollars in 2018, and, citing the BLS calculator, got pretty close on that (information woefully out of date at this point) but even there, where it explicitly cited the BLS calculator as a source we could not replicate the number it provided using any combination of start and end months, suggesting that once again, the number was coming from somewhere else, and it was just _claiming_ it was related to the BLS calculator, because it knows that’s the sort of thing people say when they explain how they got their answer.

## Conclusion

I put this together with Katie for a variety of reasons. First we thought it a fun way to spend an evening. But I think there’s two big takeaways here.

First, this sort of question remains the wrong use for ChatGPT and likely other LLM-based software as well. The Google search process was superior in a number of respects:

  * It gave us a cite-worthy response in under a minute

  * It gave us a reproducible response (e.g. the BLS calculator is not going to give different answers each time)

  * It didn’t force us to fight with it, and the information was up-to-date

  * It required very little knowledge to navigate — for instance, we didn’t have to realize that 1.7% was a ludricrous inflation rate

  * It didn’t provide initially wrong answers

In a point we’ll come back to repeatedly, one of the biggest pieces to watch here is that the process of search provides the user with an explanation of their knowledge that is _evaluable_ : we went to the BLS site and used the calculator. We don’t have to say “Google told me” because Google was a stepping off point to a source, from which the real authority is derived. A person doubting our knowledge can take our description of how we came to it and make their decision about whether that process grounds the knowledge.  
  
In ChatGPT , we get a summary of where the knowledge came from — alternately described as coming from the BLS calculator or from an equation it shows us — but in each case this is a lie. Like the rest of the production, it is merely a simulation of what a person who came to that knowledge in a traditional way might say. It looks like an argument, but is unconnected from both it’s conclusions and process.

The second reason for doing this is to explore its use as a student assignment to better understand ChatGPT. My thoughts on this is this would be a good assignment. It certainly is not the best “test” of ChatGPT, but the particular _way_ ChatGPT fails here — at least at the moment — gives us a glimpse of what’s actually going on underneath the hood, and how different it is from what it appears on the surface. Run it with your students and tell me how it goes.

Thanks for reading Mike Caulfield's Hapgood! Subscribe for free to receive new posts and support my work.
