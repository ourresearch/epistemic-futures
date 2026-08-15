---
title: "Teaching LLMs Iterative Search Technique to Achieve Greater Accuracy"
person: mike-caulfield
section: by
type: blog-post
year: 2025
date: 2025-05-21
venue: "Mike Caulfield's Substack (mikecaulfield.substack.com)"
authors: "Mike Caulfield"
source_url: https://mikecaulfield.substack.com/p/teaching-llms-iterative-search-technique
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Teaching LLMs Iterative Search Technique to Achieve Greater Accuracy

*Using the "another round" function in SIFT Toolbox*

## Full text

So I picked this example out as a test prompt a while back:

[](<https://substackcdn.com/image/fetch/$s_!47rw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9a8b18d8-2a14-456d-a2b3-6858cd4d247b_1001x893.png>)

Thanks for reading The End(s) of Argument! Subscribe for free to receive new posts and support my work.

Unbeknownst to me, most LLMs get this wrong. When asked if it is true, they say yes. Here’s a portion of Gemini 2.5 Flash response:

> Yes, the information in the image is true.
> 
> Pope Francis did receive a custom Lamborghini Huracán in November 2017… The car sold for around $950,000 (though some reports vary slightly on the exact amount, it was in that range), and the proceeds were indeed donated to various charitable causes…

Here’s Claude 3.7 Sonnet:

> The Pope blessed and signed the car, but instead of keeping it, he decided to auction it off for charity.
> 
> The vehicle was auctioned by Sotheby's in Monaco in May 2018 and sold for $970,000 (or about €809,000), which was significantly higher than its pre-auction estimated price range of $300,000 to $450,000. 

Except… the Lamborghini was never truly sold. 

Someone _bid_ that much. But then the sale fell through. As a Plan B, the car was then raffled off, although sources conflict on how much was raised. Of course, as often happens, the big initial story gets picked up by global media (“Pope signs Lambo!”, “Lambo auctioned to rental car company!”) and is covered by outlets like CNN. The story of the sale falling through and subsequent raffle gets covered by outlets like the _[Catholic Herald](<https://thecatholicherald.com/popes-white-lamborghini-up-for-raffle-winner-gets-trip-to-rome/>)_. This makes it a difficult search for an amateur — and apparently a difficult question for an LLM.

How to address this? I have in [SIFT Toolbox](<https://checkplease.neocities.org/>) (a prompting layer for LLMs anyone can use) a command where you can ask for “another round”, and the LLM tries to do this:

> When prompted for "another round," find if possible:
> 
> \- One source that conflicts with the majority view  
> \- One source that supports the majority view  
> \- One source with a completely different answer  
> \- Update the table with these new sources  
> \- A pattern where low quality sources say one thing and high another is worth noting

I’ve recently updated the prompting layer to make “another round” a bit more analytical, and of course in the SIFT Toolbox instructions there are something like 1,000 words on how to evaluate evidence.

So if we’ve loaded SIFT Toolbox, after we get that initial answer in Claude 3.7 ($20/mo version only) we can type “another round”. And when we do, we get this!

* * *

### Post-round update (#1)

The additional research has revealed some important new information and discrepancies that significantly impact our understanding of the Pope's Lamborghini story:

  1. **Conflicting auction information** : There appears to be a major discrepancy regarding the outcome of the May 12, 2018 auction in Monaco. While Lamborghini, RM Sotheby's, and several news sources reported a successful sale (with varying amounts from €715,000 to €809,375 or approximately $812,000 to $970,000), multiple Catholic news sources from December 2018 ([Catholic Herald](<https://thecatholicherald.com/popes-white-lamborghini-up-for-raffle-winner-gets-trip-to-rome/>), [Maitland-Newcastle Catholic News](<https://mnnews.azurewebsites.net/church/2018/36153-the-popes-lamborghini/>)) report that the final bidder actually failed to complete the purchase and the $800,000 sale fell through.

  2. **Subsequent raffle** : According to these December 2018 sources, after the auction sale fell through, Lamborghini organized a charity raffle (minimum $10 donation to enter) with the winner to receive the car and a trip to Rome to meet the Pope.

  3. **Exact donation date** : The original Lamborghini source states Pope Francis received the car on November 27, 2017, while other sources like Vatican News state November 15, 2017.

  4. **Spanish rental company** : Some sources claim a Spanish rental car agency called Rent Car Deluxe purchased the Lamborghini at auction and planned to donate rental proceeds to charity as well.

  5. **Misinformation debunking** : Recent articles from 2025 (after Pope Francis's death) have had to debunk false claims that the Pope kept the Lamborghini as a personal possession.

These conflicting accounts raise interesting questions about what actually happened to the car. If the auction sale did indeed fall through (as the Catholic news sources from December 2018 claim), then reports about the Spanish rental company and the specific amounts raised may be inaccurate. The subsequent raffle information adds a compelling additional chapter to the story that was not present in the original fact check.

* * *

# One more round brings it fully into focus

So we ask for a second round, and here is the result of that:

* * *

### Post-round update (#2)

Our additional research has revealed a fascinating twist in the story of Pope Francis's Lamborghini that significantly changes our understanding of what happened. The most important findings:

  1. **The auction sale did fall through** : Multiple reliable Catholic news sources from December 2018 confirm that despite the initial reports from RM Sotheby's and Lamborghini about a successful auction in May 2018, the winning bidder (who had reportedly bid between €715,000-809,375 or approximately $800,000-970,000) failed to complete the purchase. This explains the contradictory reports we found earlier.

  2. **The car was subsequently raffled** : After the auction sale fell through, Lamborghini organized a charity raffle through the Omaze fundraising platform in December 2018. Entry tickets started at $10, and the raffle was scheduled to end on January 30, 2019, according to Car and Driver magazine.

  3. **Similar charity benefits** : The raffle proceeds were directed to the same causes originally intended to benefit from the auction, including rebuilding villages in Iraq's Nineveh Plain, assisting victims of human trafficking, and providing medical care in Africa.

  4. **Prize details unchanged** : The raffle winner was to receive not just the Lamborghini but also a trip to Rome, accommodations in a four-star hotel, and a private ceremony to receive the car keys directly from Pope Francis and Lamborghini CEO Stefano Domenicali.

  5. **Still no confirmation of winner** : Despite extensive searching, we haven't found any information about who ultimately won the raffle or whether the handover ceremony with Pope Francis actually took place. This is a notable gap in our knowledge of the story's conclusion.

This unexpected development in the story highlights the importance of reviewing multiple sources spanning different time periods. The initial reports from the auction house and Lamborghini announcing a successful sale were widely reported, but the fact that the sale later fell through and led to a charity raffle instead was much less publicized. This could explain why some sources (including the original post we were fact-checking) still refer to the auction sale as if it was completed successfully.

# It could improve answers, sure… but it’s also just fun?

* * *

In the above excerpts from the responses, I’m skipping over the links provided and the summaries. You can read them all here:

<https://claude.ai/share/8853a529-9623-49c9-b7a0-21bf7c80f338>

The results on the page have the normal SIFT Toolbox sources table, and all the other features.

[](<https://substackcdn.com/image/fetch/$s_!uDUW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F84e9be52-6890-4738-8a62-17d1ed1c884c_1388x727.png>)

I suppose people might think stories like this Pope one are rare in their complexity. They’re not. Maybe I have a bit of an eye for these things, but I can scan a page of new Facebook posts, pull ten stories, and at least one of them will have this sort of complexity (and get mangled by an LLM). They are hard for LLMs for the same reasons they are hard for people, which is why in general it’s good to read synthesis from people who are good at searching, rather than things from people (or models) that are not.

The SIFT Toolbox was designed for iterative human-in-the-loop searching, but I do find it interesting that just blindly typing “another round” seems to get a better result on these sorts of stories than most LLMs. Seems like something that these models could adopt in there core behavior? I’ve tested it as well on instances where the first answer is correct, and [it doesn’t seem to degrade solid answers](<https://claude.ai/share/2a76a01f-1bd5-451f-a0c9-60e5e95ee5ba>), just reaffirm them, partially because of that last line about source quality, and partially because of the thousand or so words in the prompt that explain how to evaluate evidence.

Also, I have to say — there’s something just really _fun_ about when another round turns up something new. It feels less like [an answer machine](<https://www.theatlantic.com/technology/archive/2025/05/sycophantic-ai/682743/>), and more like a journey.

As always the (slightly) new code is at the [SIFT Toolbox site](<https://checkplease.neocities.org/>). This new modification just makes explicit what the “another round” move found:
    
    
    After showing the sources table after "another round" summarize what new information has come to light and if/how if changes how we view the issue or question. If it has not discovered ANYTHING new, admit it is mostly reinforcing previous searches. Call it "Post-round update".

Try it out!

Thanks for reading The End(s) of Argument! Subscribe for free to receive new posts and support my work.
