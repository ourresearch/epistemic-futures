---
title: "Improving Uber’s Surge Pricing"
person: tim-oreilly
section: by
type: blog-post
year: 2015
date: 2015-09-15
venue: "Medium"
authors: "Tim O'Reilly"
source_url: https://medium.com/the-wtf-economy/improving-uber-s-surge-pricing-3fd2fe108bd6
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the r.jina.ai reader proxy over the live Medium page (Medium blocks direct requests). Authorship confirmed by the byline on the page."
---

# Improving Uber’s Surge Pricing

## Full text

Harnessing the Power of Markets and Multi-factor Algorithms

_Companies want a bigger share of the pie than their competitors, capital wants a bigger share than labor (and labor wants right back), countries want a bigger share than their rivals, but true wealth comes when we make a bigger pie for everyone. Well run markets are a proven way to do that._

Surge pricing is one of Uber’s most interesting labor innovations. [Faced with the problem that they don’t have enough drivers in particular neighborhoods or at particular hours](http://abovethecrowd.com/2014/03/11/a-deeper-look-at-ubers-dynamic-pricing-model/), they use market mechanisms to bring more drivers to those areas. If they need more drivers, they raise the price to consumers until enough drivers are incented by the possibility of higher earnings to fill the demand. Pricing is not set arbitrarily. It is driven algorithmically by pickup time — the goal is to have enough cars on the road that a passenger will get a car within 3–5 minutes. ([Lyft’s Prime Time pricing](https://drivers.lyft.com/customer/portal/articles/1366676-prime-time)is a similar system.) Uber keeps raising the price until the pickup time falls into the desired range.

[Uber’s demand graph for surge pricing on New Year’s Eve 2014, NYC](http://newsroom.uber.com/2014/12/happy-new-year-from-uber/)

This is clearly an imperfect system. In one case, [surge pricing gouged customers during a crisis](http://www.slate.com/blogs/moneybox/2014/12/15/uber_sydney_hostage_crisis_it_s_time_for_uber_to_re_evaluate_how_it_prices.html), and even in more prosaic situations like bad weather, the end of a sporting event, or a holiday evening, customers can see enormous price hikes. This uncertainty undercuts the fundamental promise of the app, of cheap, on-demand transportation. If you don’t know how much the ride will cost, can you rely on it?

But consider the alternative — no transportation is available at all. We’ve all experienced that moment in the rain, or in the morning rush, when every cab is taken, and there’s nothing to do but wait and hope. And because surge prices are marked in the app, users can choose simply to wait till the surge ends, to walk to an area outside the surge (which is often very local), or take alternative transportation. Just last week, faced with Lyft’s Prime Time price to La Guardia Airport from midtown Manhattan, after a quick Google Maps check of the time difference between driving and public transit, I hopped on the MTA instead. The ultimate check on Surge or Prime Time pricing is consumer acceptance. If prices surge too high, drivers may be incented but customers are disincented to participate, and the market, in theory, finds the correct equilibrium. It’s a textbook case of [Supply and Demand](http://www.investopedia.com/university/economics/economics3.asp).

Even more problematic, though, [surge pricing doesn’t always work that well for drivers](http://disinfo.com/2014/12/gouge-away-ubers-surge-pricing-drivers-perspective/). Some report that they don’t even bother rushing to a surge area, because by the time they get there, the surge may be over, or they are competing with too many other drivers for the same passengers.

Other potential problems include those raised by some city officials, that too many [cars cruising the streets looking for passengers can increase congestion](http://www.nytimes.com/2015/07/28/upshot/blame-uber-for-congestion-in-manhattan-not-so-fast.html?_r=0). (Logic would dictate, however, that cars directed to pick up a passenger by an app, and able to seek out passengers in out of the way locations, is far less likely to cause congestion than traditional taxis, which must simply cruise the busiest streets looking for street pickups.)

Yet it is a mistake to think that current surge pricing algorithms are the end of the algorithmic management story. Rather than simply take into account pickup time, the algorithms could be tuned to take into account congestion (which affects trip time and thus customer satisfaction), number of available passengers vs. the number of available drivers and their distance from the surge, the length of time the surge is in operation, and many other factors that might improve the system.

[**Attend the Next:Economy Summit**](http://conferences.oreilly.com/next-economy/?cmp=ex-na-invite-home-ec15_medium_post)**to learn more about the evolution of 21st century business.**

A good analogy is Google search. Google began with PageRank — a single brilliant innovation in search algorithms — yet as it grew, it took into account hundreds of other factors to improve its search results. Similarly, Google’s Ad Auction took a simple innovation — Overture’s pay per click, rather than per impression — and added sophisticated auction mechanisms to improve its performance. In each case, a single innovative algorithm became the basis for a rapidly evolving set of goal driven algorithms, and ultimately, an industry transformation.

In this regard, it is worth contrasting the algorithms used by scheduling systems used to manage low wage service sector work in retail and fast food, which I wrote about at length in my piece [Workers in a World of Continuous Partial Employment](https://medium.com/the-wtf-economy/workers-in-a-world-of-continuous-partial-employment-4d7b53f18f96). The goal of these algorithms is primarily to reduce labor costs for the company. They use fine-grained employee monitoring, expected measures of output per hour worked, and detailed top-down scheduling to reduce labor to the bare minimum needed to get the job done. The better the algorithm gets, the worse things get for workers, and often, for consumers as well.

The surge pricing algorithm, by contrast, is fundamentally customer facing. Despite the complaints, its goal is to improve user experience. And rather than using top-down micromanagement to match supply and demand, it uses market mechanisms, which, in theory, will find the perfect equilibrium between what workers are willing to accept and customers are willing to pay.

[A vision of the “Perpetual Ride”](http://abovethecrowd.com/2015/01/30/ubers-new-bhag-uberpool/)

UberPool is another great example of how algorithmic markets can continue to improve, offering new products for consumers, increasing utilization (and therefore driver income), as well as further transforming modern transportation. Like [Lyft Line](http://blog.lyft.com/posts/introducing-lyft-line), which preceded it by a few months, this is a system for matching up passengers going in the same direction. Travis Kalanick, Uber’s co-founder and CEO, has referred to this as “[the perpetual ride](http://abovethecrowd.com/2015/01/30/ubers-new-bhag-uberpool/),” in which fares are low but driver income is still high, because the driver always has at least one passenger on board, picking up and dropping off new passengers in a complex algorithmic dance that lets everyone go just where they want, on demand, but finds the best route to accommodate others going in the same direction.

## Get Tim O'Reilly’s stories in your inbox

Join Medium for free to get updates from this writer.

Remember me for faster sign in

Venture Capitalist Bill Gurley (who is an investor in Uber and sits on its Board of Directors) has done a great job of laying out the business rationale behind [Uber’s quest for passenger and driver volume to provide enough market liquidity](http://abovethecrowd.com/2015/01/30/ubers-new-bhag-uberpool/) that will make products like this successful:

> To make a concept like UberPool work [you need a really high amount of base liquidity in the system](http://jobs.aol.com/videos/advice/travis-kalanick-says-services-like-uberpool-will-need-massive-sc/518405812/) — tons of cars and tons of riders. Otherwise, you will not have enough people moving in the same direction at the same time.

Gurley points out that even with a great deal of liquidity, this is a difficult algorithmic challenge, and one that is far from completely solved:

> The idea of UberPool may seem simple, but the implementation is unquestionably not. If you previously studied combinatorial optimization in theoretical computer science or operations research you may be familiar with the “traveling salesman problem,” or TSP. TSP problems require computationally intensive integer linear programming techniques to find exact solutions. Since there are too many permutations for these problems to be accurately solved, sophisticated heuristic approximation methods have to be developed. It turns out that writing the algorithms for UberPool is quite a bit more complex than a simple TSP, because (1) you have many more than one “salesman,” (2) the destinations are dynamic, (3) new “salesmen” are constantly entering and leaving the system, (4) vehicles have limited seating capacity, and (5) new requests for rides are continually streaming in. This is not just closer to the dynamic mTSP (multiple TSP) problem, which falls under the intimidating classification of “NP-hard,” but moreso under the broader and even more formidable VRP (Vehicle Routing Problem). The math department has plenty to do.

Uber’s seeming intransigence in the face of various regulatory requests is not just obstinacy. It is rooted in a deep vision of how markets work. They believe that lowering prices to increase passenger volume, a large pool of drivers making independent, market-based decisions on when and where to drive, and smarter and smarter algorithms are the recipe for a fundamental transformation of on-demand transportation.

If Uber has faith in their algorithmic approach, they should go all in.

**_Uber should be exploring whether algorithmic pricing should be the norm, rather than the exception_**_._ Again, there are important lessons from Google, whose auction based mechanisms based on performance transformed advertising. If the real-time market based pricing that is operative during the surge is truly more effective, why isn’t it being used all the time to find the “right” price, just as Google does with Adwords? It could even become a true auction, with customers indicating their willingness to pay a higher price for quicker service.

In addition, **_Uber should invest in better mechanisms to help drivers take advantage of algorithmic pricing_**. Ideally, drivers should be empowered to understand when it is to their advantage to go to a surge. It’s a simple extension of the fundamental promise of the app to drivers: rather than having you drive aimlessly waiting for a fare, or having you wait at a highly trafficked location like a hotel or airport, Uber, Lyft, and other on-demand marketplaces should be working constantly to provide better tools for workers to maximize their income and minimize their time. There are already third-party tools like [SherpaShare](https://www.sherpashare.com/) and [Hurdlr](http://hurdlr.com/#/home) that help drivers understand their utilization and earnings and estimate tax liabilities; on-demand marketplaces should integrate and support these tools.

**_Better affordances for workers can be as progressive and labor-friendly as restrictive labor protections, while supporting the entrepreneurial spirit and the freedom to work that make these on-demand jobs attractive in the first place._**

Policy makers need to understand that a market-based approach like this fundamentally relies on the ability of drivers to act independently. Make drivers employees rather than independent contractors, and you put all of the burden on Uber and Lyft to estimate demand and match it with supply. As I have previously discussed in “Workers in a World of Perpetual Partial Employment,” using top-down micromanagement to match supply and demand has been a disaster for workers.

However, **_Uber should consider limiting the impact on consumers, particularly at higher surge rates, by scaling back their own percentage as the rates go up_**. Drivers may need an additional incentive to work late hours or in certain neighborhoods; Uber itself does not. In addition, they should take into account [risks of discriminatory pricing in poor neighborhoods](http://www.theatlantic.com/business/archive/2014/03/redlining-for-the-21st-century/284235/). (If drivers are less willing to do pickups in poorer neighborhoods, there is a risk that the very neighborhoods that most need lower prices may see a permanent surge price.)

All of these problems, though, can potentially be addressed by thoughtful tuning of the algorithms.

Algorithmic, market-based solutions to wages in on-demand labor markets provide a potentially interesting alternative to minimum wage mandates as a way to increase worker incomes. **_Policy makers, academics, and mainstream companies should be exploring how to apply this approach to other kinds of jobs._**

**_Uber and other on-demand companies should open up more data to academics as well as to regulators trying to understand the impact of on-demand transportation on cities, and on worker income and lifestyle._**Studies like [the one that Uber did with economist Alan Krueger of Princeton](https://s3.amazonaws.com/uber-static/comms/PDF/Uber_Driver-Partners_Hall_Kreuger_2015.pdf) are only the beginning. Rather than a one-time study, everyone would benefit from real-time data disclosure. [Uber’s algorithm is a kind of regulatory system](http://beyondtransparency.org/chapters/part-5/open-data-and-algorithmic-regulation/) for on-demand transportation, and the rest of society has some reasonable expectation of transparency about how it works.

In a fascinating post, Nick Grossman argues that [open data may in fact be the solution to Uber’s many debates with regulators](http://www.nickgrossman.is/2015/07/23/heres-the-solution-to-the-uber-and-airbnb-problems-and-no-one-will-like-it/). He writes:

> 1) Regulators need to accept a new model where they focus less on making it hard for people to get started. That means things relaxing licensing requirements and increase the freedom to operate. This is critical for experimentation and innovation.
>
>
> 2) In exchange for that freedom to operate, companies will need to share data with regulators — un-massaged, and in real time, just like their users do with them. AND, will need to accept that that data may result in forms of accountability.

In addition to possibly helping with regulatory issues, open data could also help lay to rest other persistent questions about Uber’s market-based approach. In addition to surge-based pricing and UberPool, Uber has also tried other interventions into the supply-demand graph, most notably radically lowering prices in order to drive up utilization.

Uber claims that this does not affect driver income (and in fact, when introducing price cuts in new markets, has [guaranteed minimum driver pay](http://blog.uber.com/PriceCut2015)), but drivers say that they have to work more in order to make the same amount. This shouldn’t be a matter of claim and counter-claim. Open data is a great way for everyone to understand better how well the system is working.

Subscribe to the Next:Economy newsletter for news, ideas, and insights on how technology is transforming the nature of work, life, and society.

**_Join the discussion. Should other types of industries be exploring algorithmic supply-demand labor markets? Are there other markets besides taxis where you’d pay more if you didn’t have to wait?_**
