---
title: "Where Is AI on the Enshittification Curve?"
person: tim-oreilly
section: by
type: blog-post
year: 2025
date: 2025-07-15
venue: "O'Reilly Radar"
authors: "Tim O'Reilly"
source_url: https://www.oreilly.com/radar/where-is-ai-on-the-enshittification-curve/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the oreilly.com/radar WordPress REST API (people_taxonomy=tim-oreilly); HTML converted to markdown."
---

# Where Is AI on the Enshittification Curve?

## Full text

After listening to [Andy Jassy’s “lean into AI” comments](<https://youtu.be/X1jpPk8hMVc?si=LjL_qYd0lzs83Fg9&t=375>) to CNBC about using AI to deliver a better experience to customers, I came across [Ford CEO Jim Farley’s comments](<https://www.techspot.com/news/108552-ford-ceo-warns-generative-ai-could-eliminate-half.html>) at the Aspen Ideas Festival predicting massive job losses from AI. It occurred to me that whether AI creates or destroys jobs depends on where companies are in the innovation cycle. Companies in new markets are expansive, both in terms of customer acquisition and in terms of employment; those in mature markets are stable or in decline. AI will have a different effect depending on where you are in this cycle.

As I put it in my post “[Rising Tide Rents and Robber Baron Rents](<https://www.oreilly.com/radar/rising-tide-rents-and-robber-baron-rents/>)“:

> _Disruptive technologies start out by solving new problems, serving new markets, and creating new opportunities.…They are eager to surprise and delight their users; the focus in the early days is always on value creation. Mature and declining companies, by contrast, tend to hobble their products as they focus on value extraction. They lose their ideals and their edge, eventually alienating their customers and their suppliers and opening the door to competition._

If a company tells you that the principal benefit of AI is “efficiency,” they are telling you that they don’t see opportunities to create new value or serve new customers. If you are focused on either of those things, you will be trying to turbocharge your growth with AI, not trying to wring out additional profits from a flat or declining market. At O’Reilly, there are so many things we’ve always wanted to do for our customers but haven’t had the resources to address. Yes, AI may help us be more efficient, but that is freeing up resources to [do more](<https://www.oreilly.com/radar/ai-first-puts-humans-first/>). Efficiency is the icing on the cake. For many companies—those that have stopped serving their customers and are primarily serving themselves—efficiency _is_ the cake.

Jeff Bezos called the expansive phase [Day 1](<https://aws.amazon.com/executive-insights/content/how-amazon-defines-and-operationalizes-a-day-1-culture/>): “Being constantly curious, nimble, and experimental. It means being brave enough to fail if it means that by applying lessons learnt, we can better surprise and delight customers in the future.” And in his [2016 shareholder letter](<https://www.aboutamazon.com/news/company-news/2016-letter-to-shareholders>), he explained Day 2: “Stasis. Followed by irrelevance. Followed by excruciating, painful decline. Followed by death.…To be sure, this kind of decline would happen in extreme slow motion. An established company might harvest Day 2 for decades, but the final result would still come.”

Cory Doctorow has a vivid name for Day 2: [enshittification](<https://www.wired.com/story/tiktok-platforms-cory-doctorow/>). 

> _Here is how platforms die: First, they are good to their users; then they abuse their users to make things better for their business customers; finally, they abuse those business customers to claw back all the value for themselves. Then, they die._

I asked ChatGPT for an illustration of the concept, and it produced a passable first draft:

🟢 **Value to Users** starts high but declines as the platform shifts priorities.  
🟠 **Value to Business Customers** (advertisers, sellers, etc.) increases once user attention is locked in, but then also drops.  
🔴 **Value to the Platform (Shareholders)** rises last, as the platform extracts maximum profit—ultimately degrading the experience for both users and business partners.

I wasn’t satisfied, so I went through a number of iterations trying to get the graph more accurate to my sense of Cory’s framework (e.g., user value doesn’t peak at the beginning and decline right away but starts with a plausible promise and increases during the first, virtuous phase of company expansion; companies that delight their users are often very profitable even during their growth phase, and of course the scales of the _x_ – and _y_ -axes don’t make any sense) before ChatGPT gave up the ghost and started making random changes I wasn’t asking for.

So instead I turned to Gemini, with the inspiration to have it model the graphic on a real company. I chose Twitter/X to start with, but eventually settled on the auto industry as a whole because of Jim Farley’s comments. It shows how far the industry has come from Henry Ford’s revolution. He created a standardized low-cost product to enable a mass market, and along with it, transformed the 20th century. 

Leaving electric vehicles aside, here’s Gemini’s graph of where the auto industry is on its enshittification journey. It has abandoned affordable vehicles and is largely focusing on higher prices, dealer markups, and subscription services. The average price did decline a bit between 2022 and 2024, and affordability climbed as incomes recovered after the pandemic, but the pattern is still striking. (It’s also intriguing that Gemini chose average price and affordability as the two factors to graph. I’d have thought it would have used used the number of vehicles sold. I didn’t specify which parameters to use, and it surprised me in a good way.)

Then I asked about Ford specifically. Gemini’s narrative showed a good understanding of the company’s trajectory: 

> _While a car company like Ford doesn ’t operate a “two-sided market” in the same way an Amazon or Facebook does (where users are the product sold to advertisers), the principles of extracting more value from both direct customers and indirect partners can still apply. In the early days, Ford’s focus was on mass production and making vehicles accessible and reliable. User value was high (a car for the common person, revolutionary assembly lines)….As technology advanced, Ford, like other automakers, started integrating more software and connectivity. Initially, this added significant user value (GPS, entertainment, safety features). However, as the focus shifted to monetizing these features, user value began to plateau or subtly decline….Core functionalities become optional add-ons, and existing features are moved behind paywalls. Prioritizing cost-cutting (e.g., cheaper interior materials, less robust components) to boost profit margins, while simultaneously pushing high-margin software services. Making vehicles increasingly difficult to repair outside of authorized dealerships, effectively locking customers into costly service agreements…_

You get the idea. Enshittification doesn’t just apply to tech platforms. (Henry Farrell and Abe Newman have just made the even more provocative argument that [current US foreign policy adheres to the enshittification narrative](<https://www.programmablemutter.com/p/the-enshittification-of-american>)!)

Many leading tech companies ([including Amazon](<https://www.ucl.ac.uk/bartlett/publications/2023/nov/amazons-algorithmic-rents-economics-information-amazon>), despite Andy Jassy’s Day 1 rhetoric extolling how the company will be using AI for customer benefit) are now also in the value extraction phase, managing established businesses for profit in a market whose growth, before the disruptive onset of AI, had begun to slow. So they themselves are focused on the “efficiencies” possible with AI. They foolishly leave growth to the upstarts. And they are preaching that stale gospel to more traditional enterprises as well.

AI native companies are still in the virtuous early stage of growth, delighting their users, hiring like crazy, and exploring new possibilities. According to Gemini’s analysis, though, even the leading AI platforms are already on their enshittification journey:

> **_AI companies are largely at the end of the first “seduce users” phase and are firmly entering the second “seduce businesses” phase, all while exhibiting clear, early signs of the third “enshittification” phase…._**
> 
> _They still need developers and enterprise clients to be happy, so they haven ’t started aggressively squeezing them…yet. But the free users and the entire ecosystem of online content creators are already feeling the squeeze. The virtuous phase of simply serving the end-user with the best possible product is being replaced by the strategic necessity of serving shareholders and managing astronomical costs, following the enshittification curve with remarkable speed._

I’m a bit more hopeful than Gemini is about the trajectory of the AI industry, but I am concerned. AI has not yet found true product-market fit. The buyers paying for the massive buildout of AI are not yet the individuals or consumers who are using it but rather investors flush with cash who are bellying up to the gaming table. The costs of the AI competition are so high that even insanely profitable companies see the need to jettison employees to keep up with the wild bets of capital markets that are fueling their new competitors. A product that you can’t afford to pay for without preying on others is a recipe for breaking bad.

So what’s the final outcome? Will AI destroy more jobs than it creates? As I wrote in my 2017 book [_WTF?_](<https://www.oreilly.com/tim/wtf-book.html>), it’s up to us:

> _This is my faith in humanity: that we can rise to great challenges. Moral choice, not intelligence or creativity, is our greatest asset. Things may get much worse before they get better. But we can choose instead to lift each other up, to build an economy where people matter, not just profit. We can dream big dreams and solve big problems. Instead of using technology to replace people, we can use it to augment them so they can do things that were previously impossible._

So keep this in mind when you hear talk of the efficiencies from AI. AI can be used to reduce the amount of time that healthcare workers spend on paperwork so they can spend more time with patients, or it can be used by the private equity companies that have been taking over our healthcare system to wring out higher profits and juice stock prices. It can be used to find breakthrough cures and new materials, inventing whole new industries in the process, or it can be used only to save money that will be handed out to shareholders already rich with capital. It can be used to provide customer service that not only improves satisfaction but also creates savings that could be passed on to consumers or used to retrain employees for new AI-adjacent jobs. It can be used to help us manage our scarce attention (as platforms like Amazon, Google, and Facebook once did), finding the best products and the right information, or helping us connect with our unique set of loved ones out of all the billions of people in the world. Or it can be used [to hijack our attention](<https://www.cambridge.org/core/journals/data-and-policy/article/algorithmic-attention-rents-a-theory-of-digital-platform-market-power/D85FE41F6CF99FC57DDFB2B2B63491C5>), creating even more addictive products larded with even more invasive advertising. 

Look around. There are so many unsolved problems! So much to be done. So much opportunity to free up humans to innovate, communicate, learn, care for, and entertain each other.

Yes, there will be disruption. But there’s good disruption and bad disruption. Good disruption displaces incumbents with something better. Bad disruption replaces something that could be made better with something that ends up being worse.

Every time you’re told that AI will destroy more jobs than it creates, remember: It’s up to us.
