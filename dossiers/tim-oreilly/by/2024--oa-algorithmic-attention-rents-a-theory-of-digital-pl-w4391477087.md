---
title: "Algorithmic attention rents: A theory of digital platform market power"
person: tim-oreilly
section: by
type: journal-article
year: 2024
date: 2024-01-01
venue: "Data & Policy"
authors: "Tim O’Reilly, Ilan Strauss, Mariana Mazzucato"
source_url: https://doi.org/10.1017/dap.2024.1
retrieved: 2026-08-13
content: full-text
notes: "Full text retrieved via the OpenAlex Content API (content.openalex.org); GROBID TEI XML extraction validated as prose."
---

# Algorithmic attention rents: A theory of digital platform market power

## Full text

INSTITUTE FOR INNOVATION
AND PUBLIC PURPOSE

Algorithmic Attention
Rents: A theory of digital
platform market power

Tim O’Reilly
Founder, CEO, and Chairman of O’Reilly Media
| Visiting Professor of Practice at UCL Institute for Innovation and Public Purpose
Ilan Strauss
Senior Research Associate
| UCL Institute for Innovation and Public Purpose
Mariana Mazzucato
Director and Professor in the Economics of Innovation and Public Value
| UCL Institute for Innovation and Public Purpose

WORKING PAPER
2023/10

About the Institute for Innovation and Public Purpose
The Institute for Innovation and Public Purpose (IIPP) at University College London (UCL)
aims to develop a new framework for creating, nurturing and evaluating public value in order to
achieve economic growth that is more innovation-led, inclusive and sustainable. This requires
rethinking the underlying economics that has informed the education of global civil servants and
the design of government policies. Our work feeds into innovation and industrial policy, financial
reform, institutional change and sustainable development. A key pillar of IIPP’s research is its
understanding of markets as outcomes of the interactions between different actors. In this
context, public policy should not be seen as simply fixing market failures, but also as actively
shaping and co-creating markets. Re-focusing and designing public organisations around
mission-led, public purpose aims will help tackle the grand challenges facing the 21st century.
IIPP is a department within UCL - and part of The Bartlett, which consistently ranks in the top
two faculties for architecture and the built environment in the world.

ISSN 2635-0122

This working paper can be referenced as follows:
O’Reilly, T., Strauss, I. and Mazzucato, M. (2023). Algorithmic Attention Rents: A theory of digital
platform market power. UCL Institute for Innovation and Public Purpose, Working Paper Series
(IIPP WP 2023-10). Available at: https://www.ucl.ac.uk/bartlett/public-purpose/wp2023-10

Algorithmic Attention Rents: A theory of digital platform market
power
Tim O’Reilly, Ilan Strauss, and Mariana Mazzucato∗
November 2023

Abstract
We outline a theory of algorithmic attention rents in digital aggregator platforms. We explore the
way that as platforms grow, they become increasingly capable of extracting rents from a variety of
actors in their ecosystems – users, suppliers, and advertisers – through their algorithmic control over
user attention. We focus our analysis on advertising business models, in which attention harvested
from users is monetized by reselling the attention to suppliers or other advertisers, though we believe
the theory has relevance to other online business models as well. We argue that regulations should
mandate the disclosure of the operating metrics that platforms use to allocate user attention and
shape the “free” side of their marketplace, as well as details on how that attention is monetized.

∗ Tim O’Reilly is the Founder, CEO, and Chairman of O’Reilly Media and Visiting Professor of Practice at the UCL Institute
for Innovation and Public Purpose, Ilan Strauss is a Senior Research Associate at the UCL IIPP and Mariana Mazzucato is the
founding Director and Professor in the Economics of Innovation and Public Value at UCL IIPP. Corresponding Author: Tim O’Reilly
(tim@oreilly.com), 11 Montague St, London WC1B 5BP, United Kingdom. We acknowledge the helpful comments from Jennifer
Pahlka, Bill Janeway, Greg Linden, Betsy Masiello, and Derek Slater. All errors are our own. We thank the Omidyar Network for
its generous funding of this research. This paper draws on Strauss et al. (2023).

Contents
1 Introduction

2

2 A Theory of Rents in Digital Markets
2.1 How the Limits of Human Cognition Enable Algorithmic Authority . . . . . . . . . . . .
2.2 How Algorithmic Authority Enables Attention Rents . . . . . . . . . . . . . . . . . . . .
2.3 How Attention Rents Become Pecuniary Rents . . . . . . . . . . . . . . . . . . . . . . .

7
9
12
13

3 Harms from Algorithmic Rents
3.1 Google Search: The Market Shaping Power of Attention Allocations . . . . . . . . . . .
3.2 Amazon Marketplace: Advertising as Extractive Rent . . . . . . . . . . . . . . . . . . .
3.3 Social Media: Engagement Is a Two-Edged Sword . . . . . . . . . . . . . . . . . . . . .

19
20
21
23

4 Measuring Algorithmic Attention Rents

23

5 Some Possible Regulatory Interventions
5.1 Regulations of Algorithmic Output and Preferences . . . . . . . . . . . . . . . . . . . . .
5.2 The Need for Regular, Mandated, Disclosures of Operating Metrics . . . . . . . . . . . .
5.3 Some Recommended Reportable Operating Metrics . . . . . . . . . . . . . . . . . . . . .

26
26
27
28

6 Conclusion: AI and Attention

30

1

1

Introduction

The dominant policy narrative that guides regulation of internet platforms today focuses on user data
and privacy (Albrecht 2016; Srinivasan 2019). Platforms are said to abuse their market power by taking
data from consumers (or “users”) without their permission and using it to manipulate their behaviour
through personalization. Zuboff (2019) calls this surveillance capitalism.
We argue instead that it may be more productive to understand platform market power and to
regulate its possible abuses by measuring the ways that internet platforms control and monetize the
attention of their users. The fairness or unfairness of the algorithmic systems by which platforms allocate
user attention affect not only users but an entire ecosystem of third-party suppliers (such as websites,
content creators, or app developers), as well as advertisers.
As Simon (1971) noted, an abundance of information leads to a scarcity of attention. In the face of
increasing information abundance, he predicted that we would use machines to help us better allocate
our time and attention. And so it has transpired: information has become so abundant that it defies
manual curation. Instead, powerful, proprietary algorithmic systems use the data they collect to match
users with the answers, news, entertainment, products, applications, and services they seek.
Tirole (2017, Chapter 14) echoed Simon’s idea decades later, noting: “We suffer from too much
choice, not too little. Our problem now is how best to allocate time and attention to this plethora of
potential activities, trades, and relationships [. . . ] The more the other costs (transportation, customs
duties, listing) fall, the more important costs associated with signalling, reading, and selecting become,
and the more we need sophisticated platforms to match the buyers and sellers.”
Each of the dominant internet platforms is an attention gatekeeper of one kind or another, matching
requests from billions of consumers to content, services, and products from millions of suppliers. Despite
their differences, these platforms have risen to prominence because each has developed an effective way
to efficiently allocate user attention to the most relevant information, products, and services. Google
and other search engines promise to find the most relevant web pages from millions of possibilities for
each user query; e-commerce sites promise to find the best products available at the best price; social
media sites promise to generate a unique, personalised feed of updates from friends; music and video
recommendation services promise to deliver a feed that matches a user’s taste; on-demand transportation
services promise to find the closest driver. And so on. And these platforms make a corresponding promise
to the suppliers of content, products, or services (web sites, app developers, merchants, creators, and
2

even other users) on the other side of what is typically a two-sided or three-sided marketplace consisting
of consumers (“users”), producers (“suppliers”), and advertisers: that if the supplier provides the most
relevant information, they will be rewarded with consumer attention.
In many cases, these information matching marketplaces have proven to be remarkably efficient.
Complex, data-driven algorithmic systems act as a kind of proprietary “invisible hand”, making use of
immense amounts of consumer, producer, and advertiser information to efficiently match supply with
demand. When the algorithms are fair, they deliver services to consumers that were previously unthinkable, saving them time and effort in making better choices by providing extraordinarily relevant results
despite an overwhelming number of competing options. Suppliers and advertisers find new customers
and the ability to transact with existing ones. But these markets have proven to be “winner takes most”
(Wu 2013; Petit 2020), or sometimes “winner takes all”, leaving them ripe for abuse. Once a platform
establishes dominance, it is in a position to extract additional time and attention from its users, and
economic rents from its supplier marketplace or advertisers, by controlling that flow of attention.
Economists and policymakers have long been concerned about the power of dominant companies to
extract economic rents, and there is a growing body of research arguing that an increase in rents is a
major contributor to increased inequality, less vibrant entrepreneurial ecosystems, and lower levels of
productivity growth and investment in modern economies (Piketty 2014; Standing 2016; Ryan-Collins
et al. 2017; Mazzucato 2018; Stiglitz 2019; Christophers 2020; Kurz 2023).
Rents typically reflect control over a scarce factor of production. This control allows its holder to
extract profits above a “normal” rate achievable in a competitive market. These profits are not the result
of productive improvements that grow the economic pie; they are a reallocation of economic value from
one party to another as a result of some kind of market power.
Not all rents represent abuse of power, though. As noted by Schumpeter (2013), innovation —
whether protected by patents, trade secrets, or just by moving faster and more capably than the competition — provides an opportunity to receive a disproportionate share of profits until the innovation is
spread more widely. A company that continues to innovate can earn disproportionate profits for a long
time, especially in a growing market.
During the expansive period of a new technology cycle, market leaders do emerge through innovation,
solving new problems and creating new value not only for consumers but also for a rich ecosystem of
suppliers, intermediaries, and even competitors. These market leaders can reach astonishing levels of
Schumpeterian profit as they lay waste to incumbents and dominate the new market. But once the
3

growth of the market as a whole slows, they can no longer rely on the rising tide of new user adoption
and their own innovations to maintain that level of profit. At that point, they may turn to more
traditional extractive techniques, using their market power to maintain or increase their now-customary
level of profits in the face of macroeconomic factors and competition that ought to be eating them
away.1
Companies like Amazon, Apple, Google, and Microsoft have been innovators and much of the value
they have received has been well earned as a return on their investments. But they are also increasingly
the beneficiaries of economic rents. But what is the scarce factor of production that allows them to
extract these rents? And how do you measure rents in a market where services are offered for free?
This paper argues that the scarce factor of production is the attention of users, and that rents can be
identified by deviations from the best possible attention allocations of which a platform is capable.2
These are represented by what in the search engine literature are referred to as “organic” results; that
is, by the results chosen as best by the platform’s own search or recommendation algorithms before any
self-serving distortions.
These “algorithmic attention rents” are rents in the classical sense. Attention is a factor of production
that is limited in supply3 and can see its value appropriated by others than those who supply it.4 By
virtue of a platform’s dominance in a given attention market, it is able to appropriate an increasing
share of the return to “attention” – including by providing lower-quality results, by charging a higher
price than what the attention may be worth to those buying it, by forcing ecosystem participants to
pay for visibility, or by trying to monopolise vertical product or service markets.
In allocating user attention, the platform is also shaping the allocation of economic value between
competing stakeholders on the platform, including itself, its users, its third-party supplier ecosystem, and
its advertisers. A platform’s third-party producers compete with each other, and advertisers compete
with these producers and other advertisers, for a fixed quantum of user attention. Not only is a user’s
attention finite, so too is the narrow window onto abundant information provided by the screen, whose
interface design is controlled by the platform. Every user attention allocation can thus lead to a pecuniary
1 For evidence on this cycle for Google and Search see United States of America v. Google LLC (2020).
2 To be clear, there is no single result that is best for every user, which is why Google, for example, traditionally offered ten results

for the user to choose from. But what we see today is the shrinkage of the range of options offered to users, with the platform making
more of the choices for them, often dictated by commercial considerations, not user benefit.
3 Invariant to changes in prices (vertical supply curve), for overview see: Alchian (2017) and Mazzucato (2018).
4 Rents may simply reflect the returns received by a factor (Alchian 2017). But rents can also reflect a deviation from what a factor
contributes to production versus what it receives. See for example, Samuelson and Nordhaus (2010) showing the deviation between
wage and marginal revenue product of each worker. For discussion of Neoclassical rent as “excess over opportunity cost” and its
reliance on theories of profit see Blaug (1997, p. 439).

4

gain or harm for a firm, website owner, or content creator on another side of the platform. Attention
allocations drive value allocations.
This understanding shifts the analysis of a platform’s abuse of market power away from prices. A
platform’s dominance can be measured by its ability to shape user attention independently of user
preferences,5 user inputs, and the relevance of its third-party ecosystem’s information.
Our approach differs from the Surveillance Capitalism view that “Big Tech” algorithms extract a
“behavioural surplus” from users as excess data (beyond service improvement) to manipulate them
(Zuboff 2019). While it is true that platforms collect enormous amounts of data on their users, profit
from it, and use it not only for their users’ benefit but for the benefit of their advertisers, this narrative
misses the mark in several important ways. Data is an essential raw material that is aggregated and
made useful by internet services; and personalisation is often experienced as a benefit by consumers
rather than a harm. Drawing a bright line between permissible and impermissible uses of data and
personalisation is often difficult. Data is ultimately a means to more effective attention allocations, not
an end in itself.
In our framing, it is attention that can be extracted in excess of that needed by the platform to earn
a normal return on capital. And once that excess attention has been extracted from the consumer, it can
be redirected to extract pecuniary rents from suppliers or advertisers – or to allocate more value to the
platform’s own information. A Surveillance Capitalism paradigm ignores that platforms are multi-sided,
such that every sub-optimal allocation or action impacts not just users but the other platform sides
too.6
Our emphasis on non-pecuniary attention rents being extracted from users in order to extract pecuniary rents from suppliers is in-line with the predictions of Rochet and Tirole’s benchmark economic
models of platforms (Rochet and Tirole 2003, 2006). These predict that a monopolist will charge users
zero pecuniary prices to maximise profits, if cross-side network effects are large (such that each advertiser benefits considerably from each additional user.)7 Our paper elaborates on what happens next: a
monopolist charging users zero pecuniary prices can increase profits further by degrading the quality
of attention allocations to users below a competitive level without a loss of revenue that would make
5 See, for example, Ricks and McCrosky (2022) on the ineffectiveness of YouTube’s user preference controls.
6 Hovenkamp (2020, p. 1961) notes: “power assessment on two-sided platforms requires considering the reactions that occur on the
opposite side”.
7 Rochet and Tirole (2006) note: “a factor that is conducive to a high price on one side, to the extent that it raises the platform’s
margin on that side, tends also to call for a low price on the other side as attracting members on that other side becomes more
profitable.”

5

such a strategy unprofitable (Begent and Collyer 2013). Unsurprisingly, this is what is widely observed
today: such platforms have become more focused on attracting advertisers than on providing a good
user experience, in order to extract excessive profits from advertisers or their producer ecosystems.
Doctorow (2023) calls this “enshittification.”
Why don’t users, suppliers, and advertisers switch to other platforms? One answer is that it is difficult
to assemble what Amazon famously called the “flywheel”, in which a critical mass of algorithmically
curated content from suppliers draws users, and more users draws more suppliers, in a virtuous circle
through which the marketplace provider is able to continuously improve its services.8 Data does play a
role here. The more users that a platform has, the more data that it can collect about them and the
better its algorithmic results can be. That means in practice that the market leaders are sufficiently far
enough ahead of the competition that, once they have established market power, they have headroom
to worsen the product in other ways without losing users to competitors.
A critical part of the monopolist’s toolkit is also to raise switching costs by reducing frictions
internally, and raising them externally. For example, free shipping with Amazon Prime encourages
users not to shop around, and Amazon’s “most favoured nation” pricing contracts with its suppliers
make it unlikely that lower prices will be found elsewhere (Graham 2023). While this is not a focus
of our analysis, it is a backdrop to any understanding of how a marketplace platform can reduce the
quality of results without losing participants.
The identification of a dominant platform’s pecuniary rents as being extracted via algorithmicallymanipulated attention makes it possible to better understand several different types of platform harms,
including self-preferencing, excessive advertising, exploitation of third-party ecosystems, and exploitation of user click behaviour. A major implication of this work is the need for greater disclosure, to allow
regulators, investors, and the public to better observe, measure, and ultimately regulate potential harms
stemming from how user attention is allocated.
Our primary goal here is to articulate a theory of platform market power and its abuses in the
digital age that serves as a foundation for future work. In a companion paper, “Amazon’s Algorithmic
Rents” (Strauss et al. 2023), we take a deeper look at the legal and policy application of these ideas
to Amazon’s third-party Marketplace. And in “Behind the Clicks: Can Amazon allocate user attention
as it pleases?” (Rock et al. 2023), we demonstrate one approach to measuring algorithmic attention
8 In Wilkes (2012), Amazon executive Jeff Wilkes explains in an internal presentation to Amazon staff how Jeff Bezos first came

up with this idea. There is now an extensive management literature explaining the concept.

6

rents in Amazon’s marketplace. This research is part of a broader effort to map modern economic rents
(Mazzucato, Ryan-Collins, et al. 2023).

2

A Theory of Rents in Digital Markets

Economists see prices as the coordinator of economic activity: they are the sinews of the market’s invisible hand. Prices are thought to optimally allocate resources among competing ends when they reflect
the dynamic information (preferences and scarcities) contained in the billions of daily decentralised interactions between demand and supply. As Hayek (1945, p. 1) notes, decentralised price formation solves
“the problem of the utilisation of knowledge which is not given to anyone in its totality.” Market-driven
price formation is superior to any centralised mechanism of coordination of economy activity because it
ensures that “fuller use will be made of the existing knowledge” contained in the economy (ibid., p. 2).
In neoclassical (marginalist) theory, perfect information exists, such that prices are optimal because
they reflect the subjective utility evaluations of consumers.9 By contrast, in Simon’s view of decision
making and in more recent work in behavioural economics, perfect information does not exist. Instead,
consumers and producers make decisions that are shaped not only by human limits and biases but
by the institutions that shape the information that is available to decision-makers (Simon 1997). And
today, what makes information imperfect is often not that there is too little of it, but too much, and
the institutions that help us manage that abundance have extraordinary power to shape our decisions.
Internet platforms change the institutional context and challenge the conventional view of decision
making in markets in several ways:
1. In informationally complex markets, platforms transfer much of the work of decision making
from humans to machines. Internet search, e-commerce search, social media feeds, and other
algorithmically managed recommendation engines are examples of such machines.
2. These algorithmic machines are often used to match supply and demand for non-priced goods and
services, or those that are not individually priced. For example, in a free, ad-supported service
such as Google Search or Facebook, or a subscription service such as Netflix or Spotify, consumers
are matched with suppliers of information without considering price as a factor. Matching instead
9 Foley (2008, p. 160) notes that in neoclassical economic theory, “the quantity of the various commodities available to society has

to be taken as given, so that their relative scarcities can determine marginal utilities and hence price.” Market prices then are “exactly
analogous to the ratios of marginal utilities that an individual equalizes in making a rational allocation of resources.” Continuing
(ibid., p. 171): “The idea that the goal of economic activity is the satisfaction of individual consumers is deeply rooted in the structure
of marginalist thought, which sees subjective utility evaluation as the regulating factor of price and value.”

7

relies on other non-price factors to gauge the objectives and preferences of the consumer, the
quality of the products or services on offer from suppliers, and even the reliability and reputation
of the suppliers themselves. As Google founders Larry Page and Sergey Brin noted (Brin 1998), a
platform such as Google Search offers objective rankings based on something as seemingly subjective
as optimising for “relevancy”.10 Much like the decentralised markets celebrated by Hayek, platforms
work their allocative magic by processing signals based on millions of decisions taken by other
users on the internet and in real life, combined with data, both expressed and implied, on the user’s
personal preferences.11 Collecting more data is an essential part of what makes these systems work.
But in processing this data to produce a relevancy ranking for user search or recommendations,
the algorithmic system takes on the role of the invisible hand and works either to preserve the
competitive process or to distort it.
3. Even when price is a factor, as in e-commerce or an advertising marketplace, the platform’s
proprietary matching algorithms internalise and centralise the otherwise decentralised market
mechanism. Furthermore, this internalised and centralised market is opaque. Rather than providing explicit information to consumers about the basis for the ranking of products and services,
an algorithmically generated ranking implies much of that information, with the user expected
to trust the rank ordering provided by the platform. The platforms control the presentation of
information, and their algorithmically-populated interface designs become the context for user
decision-making.
Algorithmic attention allocations thus supplement – and at times supplant – traditional markets
as the key institutional mechanism coordinating economic activity and shaping the terms on which
exchange takes place online. The resulting algorithmic systems decide the winner among different producers whose information is competing for the user’s attention. They not only facilitate the effective
delivery of the platform’s information services to users but the monetization between platform sides
(advertisers and users for example).
Because internet platforms have effectively internalised the market mechanism, their algorithmic
allocations tend to reflect the degree of competitiveness within and between platforms. In a competitive
10 At the core of PageRank, the search quality algorithm developed by Google founders Larry Page and Sergey Brin when they were
graduate students at Stanford, was the belief that although “the importance of a Web page is an inherently subjective matter”, an
algorithm could “objectively and mechanically” rank them through “effectively measuring the human interest and attention devoted
to them” (Brin 1998).
11 For a view of this process at Amazon, see Sorokina and Cantu-Paz (2016). While the actual algorithms described in the paper
have undoubtedly been updated since the paper was written, it gives an invaluable view of the algorithmic training process.

8

market, the platform has a strong incentive for its algorithms to be fair; once they have market power,
platforms are liable to make allocations that are self-serving.
Attention allocations involve design choices and trade-offs because attention is finite and consumable.12 For example, a platform allocating more top screen space to advertising information can prevent
the user from spending attention on more relevant organic results, leading to poorer choices. A platform providing information directly in response to a query rather than directing traffic to a third party
website might yield benefit to its users even as it reduces benefit to third party suppliers.
Internet platforms are in a unique position to explore and optimise these trade-offs for their own
benefit due to their access to real-time data on the participants from all platform sides. With millions
of users repeating the same search, or responding to the same recommendations, the platform is able
to run statistically meaningful A/B tests on thousands of different algorithmic weightings and design
options. In 2022, Google claims to have run more than 800,000 search experiments, which led to more
than 4,000 changes to Search (Google 2023a).

2.1

How the Limits of Human Cognition Enable Algorithmic Authority

Simon’s (1978a, 1995) information processing paradigm focuses on how humans make decisions in the
real world: “compatible with the access to information and the computational capacities that are actually
possessed by organisms, including man, in the kinds of environments in which such organisms exist”
(Simon 1955, p. 99).
Human computational capacities are limited, as is their time.13 These “hardware” limits help explain
real world behaviours, which tend to follow heuristics – informational shortcuts and strategies that allow humans to make reasonable choices in everyday complex environments (Simon 1978b, p. 12, 2017).
Heuristics reflect human “satisficing behaviour” which aims for “good enough” outcomes,14 based on
many unknowns. This contrasts with the economic assumption that humans “optimise” to achieve the
“best” solution, based on known outcomes from every action. Simon’s emphasis on the decision making process contrasts strongly with the Neoclassical focus on (equilibrium) outcomes by unconstrained
actors.
Simon’s insights are echoed by contemporary behavioural economics. Kahneman (2011), and Tversky
12 Notes Kahneman (2011): “The often-used phrase ’pay attention’ is apt: you dispose of a limited budget of attention that you can
allocate to activities, and if you try to go beyond your budget, you will fail.” Competition & Markets Authority, CMA (2022) outlines
how online choice architectures can lead to user harm.
13 Simon (1978b, p. 12) “the scarce resource is computational capacity – the mind”
14 For Sen (2017), satificing is “a target level of achievement” but can be interpreted as optimising.

9

and Kahneman (1974, 1981), posited that humans have two decision-making modes: what they called
System 1, for decisions that need to be made quickly, and System 2, for those that depend on careful
rational analysis. According to Kahneman (2011), 98% of human decision making relies on System 1.
While these two systems are appropriate for different types of activity (immediate response to a threat,
for instance, versus long-term planning), they may be applied inappropriately. System 1 is particularly
subject to various cognitive biases, such as anchoring bias, by which the first piece of information
presented to us frames our judgement of additional information.
Studies of actual human behaviour on internet platforms bear out the predictions of both Simon’s
“information abundant/attention scarce” model and behavioural economics. The majority of clicks tend
to go to the first few results displayed near the top left of the screen (Craswell et al. 2008; Keane and
O’Brien 2006) – even if they will vary by some unknown amount as these results deteriorate in relevancy.
This is called positional bias (Joachims et al. 2017).15 This is a form of anchoring bias that has been
well documented by search engine optimization consultants. For example, a 2022 study of more than
4 million Google search results pages found that more than 54% of clicks go to the first three organic
results. Only 0.63% of users click through to the second page of results (Dean 2023). A 2018 report
from web tracking firm Jumpshot (2018), based on a large sample of users, noted the same behaviour
on Amazon: user clicks are concentrated on the first few rows of product results. In our own study, we
found that 78% of the most clicked product listings are positioned within the first two rows of search
results (Rock et al. 2023). Perhaps even more strikingly, in 2022, a study by e-commerce consulting firm
Feedvisor (2022) reported that 32% of shoppers simply opted to buy the first product listed on a search
results page.
The value proposition and business model of the modern internet is thus entirely in line with the
premise that users are not perfect “hedonic calculators” (Robinson 2001). And this is why users are able
to benefit from intermediators such as Google or Amazon. Time savings accrue to users when they click
on algorithmically ranked results based on position, trusting that the platform has done the work for
them, rather than having to evaluate intrinsic and latent product qualities themselves. This behavioural
heuristic saves users enormous amounts of time and cognition in decision making. Following a platform’s
algorithm can lead the user to make better choices, since it effectively secures what Simon (1997) calls
a degree of expertise in the decision making process.
The impact of that expertise is borne out by actual observed user behaviour. Clicks go to the top
15 For the other main theoretical model of clicks, the cascade model, see Craswell et al. (2008). For critique see: Wang et al. (2018).

10

results not just because of human positional bias, but also because the platforms have traditionally
worked very hard to make the top results the best results. Google went so far as to patent a ranking
factor that it called “the long click” (Lopatenko et al. 2015). The patent posited that a “short click” (i.e.,
when a user clicks on a result and comes right back and clicks on another result) indicates dissatisfaction
with the result, while a long click (when the user goes away and doesn’t come back) represents success.
Along with countless other factors measured across millions of searches, long clicks could be used to
raise or lower the rank of search results, with the goal that the first result gets the long click.16 The
success of these systems is precisely why they have gained the trust of users, and why that trust, once
earned, can be abused.
A platform’s power to get users to click on its algorithmic outputs is imperfect, since clicks and
views are also influenced by the broader relative prominence and attractiveness of the results as a whole
(Yue et al. 2010), including their relative informativeness (Keane and O’Brien 2006; Craswell et al.
2008). Yet the power that trusted platforms have to drive user attention, and in turn clicks or views, is
immense. Attention directed to new information, including advertising, can lead to immediate, almost
frictionless action. A purchase, a view of an addictive TikTok, YouTube, or Facebook video, a path
down a rabbit hole of attention consumption, is just a click away. In feed recommendation systems such
as those offered by social media systems, even clicks may not be necessary, as platforms increasingly
use autoplaying videos to capture user attention, which thus becomes “opt out” rather than “opt in.”
The attention-shaping power of online platforms is a reminder of Simon’s key assertion that organisations or institutions – he often used the terms interchangeably – shape individual behaviour by
determining “the environments of information in which decisions are taken” (Simon 1997). Institutions
help consumers make decisions by establishing a division of labour in “the process of deciding,” which
is just as important as a division of labour in the processes of “doing,” argues Simon. He elaborates
on these ideas in Administrative Behaviour (ibid., Chapter 7), focusing on the concept of authority in
securing an effective division of labour in decision making within the organisation:
“‘Authority’ may be defined as the power to make decisions which guide the actions of
another. [. . . ] That is, he holds in abeyance his own critical faculties for choosing between
alternatives and uses the formal criterion of the receipt of a command or signal as his basis
for choice.”
16 Perhaps because of the focus by regulators on harms from the collection of user clickstream data, Google denies that such data
has been used as a formal ranking factor. In any case, it now notes that improvements in full text analysis with AI makes user
clickstream data less important. See Goodwin (2023).

11

This passage could be read today as applying to algorithmic recommendations made by a dominant
digital platform to a user, just as much as a recommendation coming from a senior manager or expert
to a worker, as outlined by Simon.

2.2

How Algorithmic Authority Enables Attention Rents

Attention rents occur when a platform abuses its algorithmic authority and exploits its role as a trusted
intermediator to direct user attention (clicks or time spent) to suboptimal – often sponsored – information. At its core, these rents exploit users’ positional bias in how they click, or what they view, by
placing this suboptimal information in users’ core attentional zone. This positional bias relies heavily
on the suboptimal information trying to replicate, or leverage, the authority of a platform’s organic
algorithmic result (so-called “trust bias”) (Keane and O’Brien 2006; Keane, O’Brien, and Smyth 2008).
The information may be embedded between the optimal organic results, or increasingly, may displace
them.
One implication of this algorithmic power in allocating user attention is that it provides the platform
with considerable leverage over both parties (suppliers and advertisers) looking to access user attention
– the platform’s core commodity. The platform can ensure that paid (advertising) and organic results
directly compete with one another for user attention (especially when placed “above the fold” as it was
called in the days of newspapers, but today might be called “before the scroll.”)17 The attention rent
is levied on the users – to get them to allocate attention to more profitable content for the platform
– in order to extract a pecuniary rent from the supplier or advertiser side of the dominant platform’s
multi-sided market. This rent can help create an above-normal return for the platform, especially when
combined with other charges and fees already placed on its ecosystem.
Thus, greater monetization of users entails a double-sided process, impacting not just a platform’s
users but also third-party firms and advertisers, as the nature of content shown to users changes.
Information from some third-party firms gets demoted by the additional paid or addictive content, and
the demoted content must adjust to the new algorithmic optimization to survive. Potential advertisers
receive more priority attention space and in turn greater incentive to advertise. And users must consume
more paid-for content. What happens on one side of the platform impacts the other(s) (Hovenkamp
17 Petrescu (2014): “We found that on average, the presence of ads on a search results page caused the organic CTR of the first
position to drop by 30% — from 25.7% organic CTR in the absence of ads to 17.9% CTR when ads are displayed.” This effect is likely
even more significant today, when ads have become much more prominent, occupying the positions most likely to draw attention,
and less clearly marked as advertisements.

12

2020) – not necessarily from network effects,18 but by virtue of the fixed screen space (i.e., attention
sphere) over which the platform sides compete.

2.3

How Attention Rents Become Pecuniary Rents

Contemporary theories of platforms focus mostly on externalities arising from network effects. This
helps explain why platforms provide services to users for free, in order to generate network effects
and/or economies of scale. This also explains pricing structures on platforms, i.e., how the pricing
burden falls between the two sides of the platform. For Rochet and Tirole (2006), the optimal price
structure on platforms is set indirectly to optimise total profits from both sides. This means that pricing
on one side of the platform should take into account the impact it would have on participation – and
in turn profits – on the other side of the platform.19 This tends to create a highly imbalanced pricing
structure, whereby users pay no pecuniary price for the platform and the price burden instead falls on
third-party firms or advertisers. Because advertisers value an additional user considerably, and because
users prefer free services to paying directly for them, it is often more profitable for the platform to
charge users indirectly, through their attention.20
But this theory says less about what mature platforms, which have for some time been charging
users zero (or low) prices, do next. When users face zero pecuniary prices, and their attention is monetized on the other side of the market, increasing profits initially come from gaining more users. But
over time, as user growth slows, increasing profits from user participation become a function of the
quantity of advertising. Weyl (2010, p. 1643) goes so far as to see “the platform’s problem as [first]
choosing participation rates on the two sides rather than the prices supporting this allocation”. User
responsiveness to advertising, often measured in real time by the platform, becomes key for determining the optimal business model mix such that (Behringer and Filistrucchi 2015, p. 293): “In two-sided
markets, quantities on one market side are functions of prices on that market side and quantities on the
other market side.”
It follows that algorithms coordinate platform sides not just by setting the price level as Tirole
18 Same-side or cross-platform.
19 Though they only take into account indirect network effects, rather than within-side network effects.
20 Rochet and Tirole (2006) note: “a factor that is conducive to a high price on one side, to the extent that it raises the platform’s

margin on that side, tends also to call for a low price on the other side as attracting members on that other side becomes more
profitable.” The dynamics are similar to those in a competitive bottleneck model, as discussed in Jullien et al. (2021). Users on one
side of the market primarily engage with just one platform (“single-home”), while users on the other side use multiple platforms
(“multi-home”). Once a platform has successfully attracted the single-homing side, it has greater market power when dealing with
the multi-homing side, and that’s typically where it aims to monetize or profit. Advertisers (multi-home) place ads on multiple search
engines, but users typically use one search engine (single-home) for most of their queries.

13

notes, but by controlling attention allocations. If the participation of sides is relatively fixed (due to
user stickiness and third-party lock-in), then extracting monopoly rents from one-side of the platform
requires adjusting attention allocations on the other side(s), since users must consume greater quantities
of the more profitable content.21
In a multi-sided digital platform, increasing profits or profitability for the platform thus tends to
require changing the information content shown to users on the screen (Behringer and Filistrucchi
2015): What information outputs a platform’s organic algorithms optimise for (such as recommendation
algorithms optimising for more sustained engagement); and/or the algorithmic mix of outputs (such
as more advertising and fewer organic outputs), are essential ingredients to a platform increasing user
monetization and extracting more profits from its ecosystem of firms or advertisers. Without changing
the type of content shown to users, the opportunities for user monetization by the platform’s thirdparty firms or advertisers are limited to the traditional solution of raising prices (e.g., for advertising,
subscriptions, or other fees).
These changes in information can impact value allocations if the platform chooses to algorithmically
allocate more attention to paid or otherwise self-serving content. This is done constantly, by changes in
the relative screen presentation of results, by changes to the underlying algorithmic ranking systems,
and, as asserted in the US Department of Justice complaint against Google, by internal controls that
“tweak” the results to get the desired outcome (United States of America v. Google LLC 2020). Measured
user behaviour provides a rich stream of data by which the platform can assess the impact of changes
and make further adjustments to reach its objectives (“operating metrics”).
In traditional markets, in which goods and services are directly traded for money, prices persistently
higher than “normal” are seen as a sign of excess market power and rent extraction. In attention markets, the primary expression of algorithmic market power is the ability of the platform to profitably direct
user attention, and to produce information allocations, that are to an appreciable degree independent
of consumer preferences, competitor information relevance, and its users’ explicit search inputs. Algorithmic rent is part of a platform’s wider exertion of market power when it can make inferior attention
allocations without losing sufficient sales, or users and third-party suppliers, to make such an allocation
unprofitable (Begent and Collyer 2013; Federal Trade Commission, et al. v. Amazon.Com, Inc. 2023).
A core notion explored in our research is that an attention rent exists when there is a deviation
21 For Newman (2015): “customers of zero-price products paying for those products, primarily by exchanging their attention,
information, or both”. For critical discussion see Strandburg (2013).

14

from the best attention allocations of which the platform is capable, and on whose promise the platform
drew its users in the first place. In a competitive market, platforms win by providing the best possible
results to consumers. Deviations from this standard generally occur once the platform has cemented
its dominance and hold over user attention. Because it is extremely difficult and costly to deliver high
quality search or recommendation results, the market leaders are frequently far more capable than their
competitors, which gives them additional room to worsen their results without losing customers.
Algorithmically driven attention allocations by the platform, matching users to sub-optimal information, can create rents in the sense of “returns” to a factor of production – here “attention” (proxied
by screen space and user time) – which is fixed in supply, largely invariant to changes in prices, and
exploited for the platform’s own profit (Blaug 1997; Alchian 2017). A platform is increasing profits
not from better matches (productivity improvements), but from information matches that are more
profitable for itself, or from higher matching fees.
This pattern of rent extraction by exploiting the relative proportion and position of advertising and
organic results is exactly what has been observed in practice. In its earlier years, Google search result
pages consisted of a list of ten organic search results (often referred to as the “ten blue links”) and a
snippet of content from the destination site. These organic links were framed by ads:22 three above the
organic results, with additional ads in a column to the right of the organic results. The ads were clearly
differentiated from the organic results in a distinct colour block. A remarkable series of screenshots
recorded by Dutch search engine consultant Blacquière (2014) - updated by Marvin (2020) - shows how
ads took over more of the Search screen and became increasingly hard to distinguish from organic search
results on Google Search.
In 2016, the right hand column of ads was removed completely (Kim 2016), and today, ads are
nearly indistinguishable from organic results, interspersed between the organic results, and far more of
the most favoured space at the top of the page is given over to ads. Additional space is taken up by
Google’s own content, often displayed in a carousel of images, or in an informational panel that Google
refers to as a “OneBox” (O’Reilly 2019), or most recently, in an AI-generated answer to the user’s query.
Clearly, internet platforms are well within their rights to monetize their offerings. When services
are free to users, someone has to pay the bills. The question, though, is what level of monetization
is justified to recover costs and earn a fair return on investment, and when does it become excessive?
When is advertising of value to the supplier ecosystem and to users, and when does it become a source
22 On pages of interest to advertisers – a large percentage of Google search result pages carry no ads at all.

15

of extractive rents? It is not always easy to determine the answers.
At Amazon, however, the answer to the question of whether monetization has become extractive
appears unambiguous. Almost all organic recommendations,23 which helped make Amazon’s digital
marketplace revolutionary, have been replaced by purely paid-for recommendations or hybrid recommendations, e.g. “Trending now - Sponsored”, or “Highly rated - Sponsored” (Kaziukėnas 2021). Ecommerce research firm Marketplace Pulse estimates that of the first twenty products a shopper sees
when searching on Amazon, only four are now organic results (Kaziukėnas 2022). Because of how paid
results are placed, it can sometimes take scrolling past three browser windows worth of search results
to get to the fifth organic result (Kaziukėnas 2021).
Our own analysis of Amazon’s ability to allocate value (i.e., clicks) between competing products in
its third-party marketplace through the algorithmic arrangement of search results shows that a product
listing shifted to a sufficiently higher “attention share” position will receive more clicks, regardless of
its relevance or price. A product listing in the bottom 10 for relevance, but the highest percentile for
“attention share,” is as likely to be clicked as a top 5 most relevant product in an average position. This
dynamic enables Amazon to trade-off the relevance of a search-result for its screen-position, through
advertising, while maintaining a high-click-through rate (Rock et al. 2023).
Users may be harmed when a platform replaces organic results with advertising because they may see
fewer relevant options and may be directed away from better products or lower prices. Organic outputs
and advertising both aim to be clicked on or looked at, but the ranking of the former is optimised for
intrinsic relevance among all eligible information sources, while the latter optimises directly for clicks
among those firms that bid for user attention. While the most relevant ads can be as useful to consumers
as the organic results, showing more ads means diving deeper into the inventory of ads and potentially
showing worse ads that are not as useful.
The harms to Amazon’s marketplace suppliers from replacing organic content with ads are far more
immediate. In a world where gatekeepers’ principal benefit to consumers is algorithmically curated
access to a rich ecosystem of suppliers, and where their benefit to suppliers is algorithmically curated
access to a huge market of end users, organic search results are the coin of the realm and fairness is of
the essence. Paid results standing in for (rather than supplementing) organic results are the equivalent
of a debased currency. When advertising replaces organic search results, the supplier ecosystem must
now pay for visibility that it once earned through product quality and reputation signals.
23 “Customers who bought this item also bought”, “Customers who viewed this item also viewed”, “Frequently bought together”.

16

As advertising dominates more of the screen, it has become a barrier to entry24 for merchants
wanting to sell on Amazon – a tax on top of referral and fulfilment fees (Morrison 2021). “There’s fewer
organic search results on the Amazon marketplace page, so that increasingly means the only way to
get on the page is to buy your way on there,” said Jason Goldberg, chief commerce strategy officer at
advertising mega-firm Publicis (Palmer 2021).25 The result, according to Quartile (2018), a major AIpowered advertising platform, is that Amazon is now a “pay to play” platform for top screen positions.
Three-quarters of all sellers on Amazon now “choose” to advertise (Mileva 2022). For small and medium
sized sellers the figure is 79% (Jungle Scout 2022).
This is not advertising like that offered by Google or Facebook or traditional media, which rides as
a passenger on a current of attention focused on information or entertainment, but a kind of Hunger
Games-like competition between merchants to capture the purchases of people who are already looking to
buy. It is a zero-sum transfer of attention and value between sellers (Gornyi 2023), which simultaneously
increases revenue for Amazon but without “necessarily growing the sales volume” (Kaziukėnas 2021).
An attention boost to one seller necessarily comes at the expense of another.
What’s more, unlike in traditional media advertising, these ads appear in the actual decision-making
interface with an almost identical appearance to the organically recommended product choices. The majority of Amazon marketplace ads simply duplicate the organic listings and appear on the same page,
often adjacent to them, offering no additional information to consumers. And with ads and organic listings competing for user attention on the same search results screen, Amazon exploits users’ positional
bias, and puts the ad rather than the organic result in the position most likely to be clicked on, thus
extracting a fee from the supplier while providing no added benefit.26 This behaviour demonstrates
exactly what we mean when we say that Amazon uses attention rents extracted from users to extract
corresponding pecuniary rents from its supplier ecosystem.
Through this zero-sum competition, Amazon has fostered both higher ad prices and lower return
from ad spend (Jungle Scout 2022; Soper 2023), leading to a rent transfer from third-party firms to the
platform itself. By 2022, advertising had become a highly profitable $37.7 billion business for Amazon
24 For Petit and Teece (2020) “Once they have led ecosystem partners to a strong, steady adoption outcome, platform leaders might
be tempted to tweak the contractual or technological rules to their own advantage.”
25 What’s more, (though Amazon denies this) since sales volume for a product is one of Amazon’s organic ranking factors, failure
to advertise may drive down the organic rank as well (Mitchell 2023)
26 In Rock et al. (2023) we find that 95% of the top three most clicked ads are simply duplicates of product listings.

17

(Amazon.com 2022, p. 67).27 Meanwhile, the average cost per click on Amazon ads doubled from $0.56
in 2018 to $1.2 in 2021 (Business of Apps 2022). Average cost of spend (ACOS) was 30% according to
Adbadger, meaning that 30 cents now has to be spent on ads to drive $1 of sales (The Badger 2023).
Interestingly, as TikTok begins to mount an e-commerce challenge to Amazon, it is relying on new
forms of algorithmic earned attention to attract and engage users. As with its social feed product, it
uses viral cascades of user attention to surface popular content. In the case of e-commerce, that’s the
discovery of so-called “dupes,” lower-cost products that have the same or better features than higher
cost branded products (Barinka 2023). That is, TikTok is demonstrating once again that finding new
signals that provide better organic algorithmic results provides a competitive advantage in acquiring
and retaining users, and that algorithmic rents tend to be extracted by platforms only once they have
cemented their dominance.
Distortion of the best algorithmically chosen results can also be seen in social media systems. Facebook, X (formerly Twitter), and Instagram all began by matching users with a unique feed of content
from other users that they have chosen to follow, whether they be friends, celebrities, or news sources.
During the growth period, when user acquisition is the paramount goal, these platforms align their
algorithmic selections with this user promise.
In this early stage, sorting of posts in the feed is typically in reverse chronological order (newest to
oldest), or through a social graph (from friends). Later, other possible arrangements are tried, such as
sorting by posts with the most engagement. Eventually, the sorting is fully given over to the algorithmic
recommendations. At first, users are given some control, allowing them to revert, for example, to a
chronological sort, or to preference posts from those marked as friends, or from those the user has
chosen to follow. Over time, these expressions of user preference are made harder to find or disappear
entirely. Meanwhile, the ad load goes up, also making it harder to find and enjoy the posts that the
user originally signed up for. What’s more, “dark patterns,” such as automatically switching the user
to a feed of recommended videos (e.g., Instagram Reels) as soon as they finish viewing a video posted
by a friend, are also used to help override the user’s preferences. From there, it is a slippery slope to
27 To put this information in context, it should be understood that Amazon reports its total e-commerce business in two different
ways. In its original “first party” model, it purchases inventory from suppliers at a discount and resells it to consumers, profiting
from the spread between cost and selling price, less its own operating costs, including warehousing, fulfilment, and delivery, just like
other retailers. In its “third party marketplace,” suppliers pay a fee to have their product listed on Amazon, and additional fees for
warehousing and fulfilment (a total of $117.7 billion in 2022), but continue to hold the inventory risk. Starting in 2014, advertising
was added as a new line of business. Advertising is not reported as revenue from third party seller service, but as a separate business
line. However, most observers attribute the vast majority of Amazon’s advertising revenue to the third party marketplace as Amazon
has replaced organic recommendations and search results with paid-for advertising results. In private conversations with one of the
authors, the best that Amazon insiders could say of other sources of advertising, such as from Amazon Prime TV, was that they were
“small, but growing.”

18

shaping the content shown in such a way as to extract additional attention from users by showing them
whatever content will drive the most engagement.
While we have not done empirical research to measure algorithmic attention rents in social media,
we believe that the notion of algorithmic attention rents provides fruitful avenues for further research
and analysis of social media and other recommendation systems as well as for search-based systems.

3

Harms from Algorithmic Rents

While it is harm to consumers or to competitors that is most likely to draw the eye of regulators, many
of the harms from algorithmic attention rents may fall more heavily on the supply side of a platform’s
ecosystem.
Thompson (2014, 2023) notes that in order to provide ranked results or recommendations to its
users, a platform must aggregate information – pooling and digitising supply, and commoditising it in
the process. This aggregation reduces the power of the platform’s suppliers, and makes them dependent
on the fairness of the algorithmic rankings provided by the platform.28 It is these suppliers, not just
consumers, who are harmed when information allocations are distorted from their optimally relevant
competitive level.
To understand why clearly defining the role of the platform as intermediator and aggregator matters,
it is important to take an ecosystem view of the total investment in value creation, rather than attributing all of the value creation to the platform. Any notion of fairness depends on this ecosystem view:
without websites, there would be no need for Google search; without merchants, no Amazon; without
app developers, no App Stores; without users creating content as well as consuming it, no social media.
When suppliers are harmed, users too will be harmed over the long run.
These ecosystems of value creators depend on the platform’s algorithms for what in the industry is
called “earned attention.”29 When the platform exempts its own competitive content or services from
its own algorithms, or when it displaces organic results with paid results, the ecosystem suffers a loss
28 Thompson’s “aggregation theory” makes a distinction between what he calls aggregators, which collect and manage information

and access to a marketplace, and true platforms, which provide capabilities that provide a foundation that third parties can build
on. For example, Apple’s iPhone App Store is an aggregator, while its iOS operating system is a platform. Amazon’s e-commerce
marketplace is an aggregator, but Amazon Web Services is a platform. Fulfilment by Amazon, Amazon’s suite of services for third
party merchants can also be considered a platform, but the Marketplace itself is an aggregator. Google Maps is a platform, while
Google search is an aggregator. While this is an exceedingly useful distinction, the term “platform” is so widely used in the literature
that we have adopted it here.
29 Hugonenc (2022) notes: “Earned attention is far more effective at delivering results than when attention has been acquired by
force. When consumers voluntarily view an ad, there is a significantly higher impact on brand metrics than ads that have been forced
upon them, whatever the length of time they view the ad for.”

19

of incentive and reward for continuing to produce value. Eventually, this loss of value affects both users
and the platform itself, as the whole virtuous circle of creation, aggregation, and curation breaks down.
That which has been earned is appropriated by the platform.
Advertisers can also provide value to consumers, especially when ads are well targeted to their interests. This value too can be algorithmically misappropriated by the platform. Targeted advertising
commoditizes attention, personalised by demographics, location, and interests, to be auctioned off at
scale and algorithmically matched billions of times per day with content viewed by consumers. Advertisers bid for that attention, but what they get may not be what they pay for if the platform places
ads near inappropriate brand-damaging content (Internet Advertising Bureau 2020), places display ads
(which advertisers pay for by a count of impressions (i.e., inclusion in pages being displayed) rather
than clicks) in locations far below the scroll where they are unlikely actually to be seen by users, or
doesn’t properly police problems such as click fraud, viewing by bots rather than humans, autoplaying
videos that are not actually chosen by the user, and so on. Hwang (2020) calls this ad quality problem
“the subprime attention crisis.”30
A fair reward for value created is a useful framework within which to evaluate harms from algorithmic
allocations. When considering algorithmic attention allocations, it is helpful to ask who wins, who loses,
and who decides.31 This can be a complex calculus. Examples from Google Search, Amazon Marketplace,
and social media feeds, which we explore below, show the range of questions that can be explored using
the analysis of algorithmic attention rents in ad-based businesses.

3.1

Google Search: The Market Shaping Power of Attention Allocations

Google does make a substantial effort to find the most relevant advertisements (Google 2023b).32 In the
pay-per-click (PPC) ad system used in Google search (“Adwords”), the company has strong incentives
to find the ads that are most likely to draw clicks. In display advertising formats (pay per view, or
PPV), in which Google is a player through its algorithmic placement of ads on third party websites and
its control of the ad exchanges in which advertisements are algorithmically bought and sold, Google’s
30 There are many types of algorithmic rents that can be extracted from advertisers that are not attention rents, but purely
extraction of revenue via unfair manipulation of a platform’s algorithms. For example, per the 2023 United States Department of
Justice complaint against Google, the company has “designed its ad auction algorithms to include adjustable variables internally
known as “pricing knobs”; Google then tunes the variables to increase advertiser prices.” The discovery process during the trial
uncovered damaging emails showing that Google used these pricing knobs to make up a shortfall in Google’s revenue projections due
to a decline in search volume. See Trial Exhibit - UPX0522: (United States of America v. Google LLC 2020).
31 This is also the framework adopted in environmental economics. See Boyce (2022).
32 Its ad auction takes into account various measures of ad quality before allowing participation, though it admits that ad quality is
not actually considered in the auction. Instead, a low ad quality score may mean that an advertiser is prohibited outright, or charged
more to win the auction. See (Google 2023b).

20

incentives are less clearly aligned with those of its advertisers.
Even in the PPC system of Adwords, though, the pool of possible results comes from those willing
and able to pay. And that strongly favours some firms over others. A good example may be found in
a search such as “buy new tires.” In current designs, ads populate the best screen positions, and those
ads typically come from large national chains and online sellers (O’Reilly 2022). Local merchants are
shown on a map far down the page, requiring scrolling to see them. The map does provide unpaid
business listings that allow users to learn more about each of the merchants, including their opening
hours, address, and phone number. This is valuable to both users and to merchants even though it does
not take the form of a traditional web link. But this information is far harder to find today than it was
ten years ago. This imposes a time cost on users and a visibility penalty on suppliers, such that they
must now advertise to gain attention that they had previously earned by signals such as quality and a
location convenient to the user.
Note the market shaping power on display. As consumers increasingly rely on search engines to find
products, Google is essentially deciding that those most willing and able to pay are more deserving
of consumer attention than those that relevancy factors such as location or reputation suggest. This
example highlights the responsibility of platforms to think deeply about the consequences of their
attention allocations. In short, the trade-offs are not always obvious, and weighing the harms to any
party requires careful analysis.

3.2

Amazon Marketplace: Advertising as Extractive Rent

While celebrated by shareholders and analysts as a triumph of business strategy, earning the company
enormous profits, Amazon’s Marketplace advertising business seems to provide little benefit to either
users or suppliers (who, in the case of Amazon’s third party marketplace, are also its advertisers.) Users
see fewer of the results that Amazon’s own algorithms have calculated as an ideal match for their search,
and instead see ads, whose relevance is often lower.
In Rock et al. (2023), we compared the organic rank of a search result with the ad rank of the same
result. 33 We found that on average an ad boosted the visibility of a possibly inferior (by the judgement
of Amazon’s algorithms) product by between five and 50 positions, with a median boost of 17 positions.
33 Note that in some systems, such as in Google search results, the ordinal position is easy to determine. On Amazon, which uses
a grid format for results, ordinality is more complex. It can be read left to right and top to bottom, but it may be more productive
to develop an attention-weighted model of the spots most likely to be viewed and clicked on by the user, on the assumption that
Amazon has made a similar estimation of the relative value of each spot. This is the approach we take in Rock et al. (2023), for
products that have an identical listing.

21

We also found that occupying high value screen positions is more important for sponsored than organic
listings, suggesting that users are not finding the most relevant products in the top ranking spots.
There may be some benefit from advertising to merchants trying to raise the visibility of new high
quality products (which may have fewer reviews and less history of being clicked on and purchased),
but for the most part Amazon’s ad business appears simply to be an additional fee levied on merchants
rather than providing added value to them. It raises their cost of doing business, which may be passed
along to consumers in the form of higher prices. We found that the top-3 most clicked advertised
products are about 17% more expensive than organic ones ($19.3 vs. $16.5) and one-third less relevant
(organic rank of 4 vs. 3.)
Why do sellers put up with this behaviour? As outlined in the recent United States Federal Trade
Commission complaint against Amazon (Graham 2023),34 the company has used contractual requirements to raise switching costs and to prevent sellers from offering lower prices on competing marketplaces, or even on their own sites. Additional techniques involve punishing sellers who don’t purchase
services such as fulfilment and advertising from Amazon by sentencing them to virtual algorithmic
invisibility. We explore this subject in greater detail in the companion paper, “Amazon’s Algorithmic
Rents” (Strauss et al. 2023).
Why do users put up with it? It is quite possible that they do not, but just not in sufficient numbers
to affect Amazon’s calculus about the overall profitability of its strategy. According to Stone (2021),
“When sponsored ads were prominently displayed, there was a small, statistically detectable short-term
decline in the number of customers who ended up making a purchase... But while he [Bezos] cautioned
against alienating customers by serving too many ads, he opted to vigorously move forward, saying that
any deleterious long-term consequences would have to be implausibly large to outweigh the potential
windfall and the investment opportunities that could result from it.”
The damage to Amazon may be a gradual downslope or a sudden cliff. When does brand and
reputation damage accumulate to the point that consumers start trusting Amazon less, shopping at
Amazon less, and expending the effort of trying alternatives? If Amazon is experiencing slow, incremental
costs from what it is doing, there’s more hope that it will change its behaviour35 than if it is experiencing
no costs unless regulators impose them.
34 The full text of the complaint can be found in Federal Trade Commission, et al. v. Amazon.Com, Inc. (2023).
35 Describing research on long-term vs. short term impacts of excessive advertising at Google, Hohnhold et al. (2015), note “Reducing

the mobile ad load strongly improved the user experience but was a substantially short-term revenue negative change...the long-term
revenue impact was shown to be neutral. Thus, with the user satisfaction improvement, this change was a net positive for both
business and users.”

22

3.3

Social Media: Engagement Is a Two-Edged Sword

Assessing optimality for social media platforms, which may be used either for utility or entertainment,
is more difficult than it is for utility platforms like search or e-commerce. If the user is simply looking
to be entertained, an algorithmic feed optimised for engagement may arguably be what the user wants,
as the success of TikTok demonstrates. And especially when informed by personalized data, ads can be
highly relevant and add information value to consumers. But while higher engagement and time spent
on a social media site can, on the surface, be seen as a sign that users are finding more value on it,
there are also harms, starting with addictive behaviour, and when engagement is driven by posts fueling
anger, self-doubt, misinformation, or controversy.
Social media feed recommendations, which contain advertising directly in the feed, give platforms an
incentive to extract attention rents via increased engagement. More time spent on the platform means
more surface area for advertising. Thus consumers may see a higher proportion of stories optimised for
“bad” forms of engagement, including those that are divisive, titillating, contain misinformation, or are
otherwise harmful to consumers. As Stray (2021) notes, over the long term, companies have incentives
to manage for “good” engagement so that users don’t leave, but over the short-term, they can profit
even from “bad” engagement.
Advertisers too are harmed when their ads are algorithmically matched to inappropriate content
(Internet Advertising Bureau 2020). Only the platform benefits, which is why we consider these systems
ripe for attention rents. More research is needed.

4

Measuring Algorithmic Attention Rents

Today’s platforms are data-rich environments, where harms can be measured and estimated directly.
Antitrust regulatory bodies now include data teams (Hunt 2022), though they remain hampered by
platforms not providing regular operating and data disclosures (Section 5.2).
Measuring the extent to which sponsored listings have displaced organic search results is one way to
understand whether or not these platforms are abusing their market power. We make the assumption
that if, as the platforms have both promised and demonstrated, their algorithms aim to make the best
possible attention allocations, the deviation between organic and paid results provides evidence of rents
and harms. Using this approach, the presence of algorithmic attention rents can be inferred by:

23

1. Comparing the organic ranking of a product with its paid ranking to determine the
extent to which the platform is preferencing results that its organic algorithm shows are inferior.
For example, on Amazon, paid advertising results often rank a product higher – sometimes far
higher – than the organic listing for the same product, and to other superior organically ranked
products (Rock et al. 2023).
2. Examining whether ads bring additional information to consumers. For example, on
Amazon, the organic listing for a product and an identical paid listing (ad) for the same product
often appear side by side. This duplication reduces variety. No new information is provided. Instead
net new information is taken away.
3. Comparing the quality of a dominant platform’s organic algorithmic results with the
organic allocations offered by other less dominant platforms that do face competitive
pressures. For example, it is possible to compare Amazon’s product search results on its Marketplace with those from Google Shopping; or Google Travel results with those from a site such as
TripAdvisor. This entails an assessment of the relative quality of the organic results, which may
be a very data intensive and complex task.
4. Examining whether or not the information (including information quality) that a business
or consumer could reasonably expect to find in a competitive market is available (Areeda
and Hovenkamp 2023).36 For example, in a competitive market a consumer would expect to find
the total (and unit) price of a good or service displayed to aid in shopping comparisons. Yet this is
often hidden from view online. Airbnb, for example, only recently started showing total prices of
accommodation (including cleaning fees) (Airbnb 2022). So-called “drip pricing” (Fletcher 2012),
only showing part of the price to the consumer initially, is widespread, but may be more common
on platforms with greater market power.37
In another example, companies such as Yelp and TripAdvisor have complained that Google’s
Travel listings do not make the same efforts as these smaller platforms to filter out review spam
— reflecting Google’s added market power (Hawkins 2018).38 The information degraded could
also be the quality of advertising results (and disclosures) that an advertiser could reasonably
36 ¶2023. Agreements Pertaining to Advertising and Related Dissemination of Product Information.
37 To regulate this behaviour, the FTC is considering requiring platforms to display “all-in pricing” (FTC 2023; US Federal Trade
Commission 2022). The UK CMA and Department for Business and Trade has made similar recommendations (Hollinrake 2023).
38 Harsher regulation of fake reviews is under consideration in both the UK (U.S. Federal Trade Commission 2023; Hollinrake 2023)
and the U.S.

24

expect from the platform. The DoJ argued in its 2023 trial against Google that it degraded the
ad quality in Search results by making changes to its keyword matching. This reflects Google’s
monopoly over “when and where” an ad appears (United States of America v. Google LLC 2020,
p. 6).
5. Examining whether ads have increased (and organic output declined) beyond the level
reasonably required for the platform to earn a competitive return on capital invested.
Estimating a reasonable level of return is always difficult, especially in a new industry where norms
have not been widely established, and network effects create high levels of concentration. However,
a historical view of the platform’s operating and financial metrics can provide some perspective.
For example, if profit per user (or per search, per session, or other relevant measure of service
delivered) continues to increase once user growth has levelled off, without demonstrated reductions
in costs or commensurate ecosystem benefits, this would suggest increased monetization above the
level that was previously considered sufficient to deliver the service. This profit-driven monetization
growth would need to be linked to the platform’s overall level of profit margins or profit growth
for it to be found to be exploitative, or above normal.39
Advertising needs to be looked at in combination with the other platform fees and prices a platform
charges in order to assess its reasonableness. For example, Apple justifies the 30% commission it
charges for purchases on its App Store by relating it to various investments and user benefits
such as privacy and quality (Epic Games v. Apple Inc. 2021). Yet in addition, Apple charges
app developers for visibility on its App Store by reserving prime display and result spots for
advertising. These two fees combined – advertising and commission – are significantly above 30%
(Kuriata 2022). Financial disclosures by the company, which put the two revenue sources in
different categories, help obscure the total cost to app developers.
Much of the data for these assessments can be found in an extensive literature from the Search
Engine Optimization community, social media marketing consultants, e-commerce consultants, and
the like, which provides some understanding of the ranking factors that guide algorithmic rankings
and recommendations. The platforms themselves drop tantalising clues in their announcements, blog
posts, conference presentations, and annual shareholder letters (O’Reilly et al. 2023). In addition, there
are numerous one-time studies by academics, consultants, marketplace or advertising data firms, and
39 For exploitation in EU law see: Whish and Bailey (2021, p. 201-202).

25

occasionally, regulators. These studies usually consist of statistical analysis of a snapshot of web-scraped
data at a specific time. For example, from a study of 1.4 billion searches by 28 million UK citizens
(Goodwin 2012), we know that in 2011, 94% of Google clicks were organic and only 6% went to ads.
But we have no idea what the ratio was in different countries, what that ratio is today, or how it changed
in the intervening years as Google has updated its algorithms and screen designs.
While information from studies such as this is useful, it points at a gaping hole in the regulatory
apparatus: the lack of regular, mandated disclosures by platform companies of the operating metrics
that actually guide the design of their algorithms, measure their results, and ultimately control the
monetization of user attention.

5

Some Possible Regulatory Interventions

The theory of algorithmic rents and data available from studies such as the one we have done suggest
some relatively straightforward regulatory interventions.

5.1

Regulations of Algorithmic Output and Preferences

For search based algorithmic systems, including App Stores and e-commerce, regulators could impose
the following requirements:
• A percentage of the screen positions receiving the top share of attention could be reserved for
organic results.
• When ads duplicate organic results and provide no additional information (as in the Amazon
Marketplace), regulations could require that the organic result appear first, in the position most
likely to be clicked on.
• When there is an exact match for a user query (as in a search for a product by brand name in the
Amazon marketplace), the exact match organic result must be the first result.
For feed based algorithmic systems, such as TikTok, Twitter, and Instagram:
• Platforms could be required to offer “sticky” preferences to users, rather than requiring them to
repeatedly assert their wishes. (For example, in Instagram, it is possible for the user to choose to
see posts only from those they follow or have marked as favourites, but the feed almost immediately
reverts to the platform’s own algorithmic feed preferences.) In general, when users opt out of a

26

new behaviour offered by the platforms, that preference should be persistent.
• Attention-hijacking patterns such as autoplaying videos could require an opt-in expression of
preference.
However, these interventions suffer from several flaws:
1. Platform behaviour is a moving target, with new features, constant algorithm updates, and design
changes.
2. Regulatory interventions are likely to be countered by the platforms, much as they counter attempts by users and marketplace participants to “game” their algorithms.
3. Over-specified regulations could inadvertently strangle legitimate innovations that would benefit
not only the platforms but also their users and marketplace participants.
The more fundamental problem that regulators need to address is that the mechanisms by which
platforms measure and manage user attention are poorly understood. Effective regulation depends on
enhanced disclosures.

5.2

The Need for Regular, Mandated, Disclosures of Operating Metrics

The platforms themselves collect numerous and detailed operating metrics to judge and manage the
performance of their own systems for directing user attention. They know how many users they have,
how much time those users spend on each of the platform’s services, how they are monetized, and the
impact of new services and designs on their usage and monetization. They know the ad load. They know
the ratio of organic clicks to ad clicks. They know much traffic is sent on to outside sites, by market
segment. They know the gross merchandise volume of an e-commerce marketplace or app store, and they
know what percentage they collect in fees. And they know how each of these measurements compares
to prior periods – and how those changes result from updates of their interface designs and algorithms
– just as well as they know their personnel costs, their capital equipment costs, their revenue and their
profit. But only the financial metrics are reported regularly and consistently, and those financial reports
are almost completely disconnected from the operating metrics that are used to actually manage so
much of the business (O’Reilly et al. 2023).
The lack of disclosure of operating metrics for the free side of internet aggregators is a gaping hole
in the regulatory apparatus. Costs, revenue, profit, and other financial metrics may be sufficient to
understand a business based on tangible inputs and outputs, but are not fit to purpose for information
27

businesses whose assets and activities are largely intangible and whose market power is exercised through
delivery of services that are free to consumers (Mazzucato, Strauss, et al. 2023).
Given the size of the major internet companies, these metrics need to be highly disaggregated, both
on a geographical and product basis. Google parent Alphabet alone has more than nine free products
with more than a billion users, yet it reports only one major business – “advertising.” The connection
between its revenues and the underlying free products and services is completely opaque. Meta too
discloses little disaggregated information about products such as Facebook, Instagram, WhatsApp, and
Messenger, each with billions of users. This pattern is repeated across the industry.
Even the products that are directly monetized often are not required to be broken out in detail, due
to outdated segment reporting rules. US securities regulations require companies to break out financial
detail for any business operation (or “segment”) that represents more than 10% of revenue or profit, yet
in practice, they allow for management discretion in what segments are reported. This allowed Amazon
to hide the remarkable growth and profitability of its Amazon Web Services business for years, and for
Apple to claim in response to a lawsuit from Epic Games that it didn’t actually know the profitability
of its App Store (ibid.). But perhaps more importantly, it allows them to hide the workings of the free
side of the products that underpin their enormous market power.
The most important first step is to understand how much is left out of the picture when market power
is measured purely in financial terms. We live in an attention economy. A product like Google Maps,
with over a billion users, has insignificant revenue relative to Alphabet’s total (perhaps $3 billion out of
$289 billion), yet it is unquestionably the most powerful player in its competitive segment, offering free
products that cap the growth and opportunities for smaller mapping companies like ESRI or Garmin
with more traditional business models. Segment reporting rules should be triggered by the number of
active users a product has, not just by its contribution to company revenue or profit.

5.3

Some Recommended Reportable Operating Metrics

Understanding what operating metrics need to be reported for free products and services is in its infancy.
In contrast to the financial metrics required on the money side of businesses, which are rooted in systems
of accounting dating back to the 13th century, the metrics that are used to govern algorithmic attention
businesses are at best a few decades old. Nonetheless, we must make a start.
All metrics should be reported quarterly, with more detail annually, as part of the existing financial
disclosures required of public companies. And because a historical view would be useful, to whatever
28

extent possible, the introduction of such reporting should require a backward look for at least several
years, and ideally much longer. As noted above, metrics should also be disaggregated by product, with
reporting required for any product having more than 100 million monthly users. They should also be
disaggregated by country, and by device type (desktop or mobile.)
Here are some of the metrics that would be useful for examining attention rents monetized through
advertising:
• Ad load. Because not every page has the same number of ads – on Google, for example, many
search engine results pages are non-commercial, and carry no ads at all – ad load should be
reported by decile, or some other framework that highlights the ad concentration on the most
highly monetised pages.
• Ratio of organic clicks to ad clicks. Again, by decile or other weighted format.
• Average click through rate of the first organic result. The proportion of users who visit
the page who click on the first organic result.
• Average click through rate of the first ad. The proportion of users who visit the page who
click on the first ad.
• Amount of traffic sent on to third party sites. This should be bucketed by market segment,
such as news, entertainment, commerce, travel, local search, and so on.
• Amount of traffic sent to the company’s own other products and services. This could be
further detailed by traffic source. For example, it would be useful to know how many users come
to Google search from Chrome on Apple devices vs.Chrome on Android, vs.from other browsers
such as Firefox.
• Gross Merchandise Volume (for e-commerce platforms). Without this information, it is
impossible to determine the percentage of all fees levied on third party marketplace participants.
• Gross fee revenue, including advertising from marketplace participants (for e-commerce
platforms and app stores).
• A monetization narrative: that explains the relationship between these various metrics describing the free side of their platform and their monetization on other platform sides.
Ideally, regulators, working with cooperative industry players, would define reportable metrics based
on those that are actually used by the platforms themselves to manage search, social media, e-commerce,
29

and other algorithmic relevancy and recommendation engines. These metrics should then be standardised and required. There may be some metrics that can legitimately be considered trade secrets, but
there are many that are common to most if not all internet businesses of the same type.
Note also that the operating metrics of big tech players are a moving target, constantly updated
as the platforms continue to innovate. So this is also an opportunity to update the standards-setting
process by which required reporting metrics are defined, mandating updated and timely reporting of
any meaningful change in operating metrics.
Platforms will claim, with some justice, that disclosure will harm their businesses, as it will allow
third parties to game their systems more easily. But this is akin to the old approach to cybersecurity,
of “security through obscurity.” We have learned that it is far better to find and fix vulnerabilities than
to hide them.
This is particularly important as we enter the age of large language models and generative AI, the
next generation of attention management machines foretold by Herbert Simon. You can’t regulate what
you don’t understand (O’Reilly 2023). It is not enough to rely on the assurances of powerful players that
they are doing their best. Regular, reportable metrics will allow investors, the public, regulators, and the
platforms themselves to better understand and operate truly free markets, which, as classical economists
such as Adam Smith and David Ricardo believed, are not markets free of government intervention, but
markets free of rents (Mazzucato 2018).

6

Conclusion: AI and Attention

While this paper focuses on the present state of algorithmic attention rents, we are far from done with the
changing institutional context of human decision making online. Today’s large language models (LLMs)
don’t provide ranked choices but answers. They do not (at present) send traffic or other compensation
to third party content, sites, or apps; nor do they depend on clicks and views. They do not (yet) have
an advertising-based business model. Yet they are quite consistent with the thrust of this paper, since
they depend on users accepting the increasing penetration of algorithmic authority (Choudhury and
Shamszare 2023), not just into everyday decision making but increasingly, into everyday thinking.
Attention and cognition conserving heuristics help explain much about the present trajectory of
today’s LLMs and other “frontier” AI systems. Newell and Simon (1975) viewed both human and
artificial intelligence inextricably bound up with the use of context and selectivity to create more
30

efficient, guided, approximate solutions – for humans and machines.40
As platforms evolve, AI may not only guide and replace human decision making but human thinking
(cognition.) LLMs can make use of existing information by creating new or summarised outputs from
that information, not through the ranking of it. As AI improves, those outputs may become increasingly
original, perhaps transcending their inputs and creating new knowledge and new possibilities. But even
today:
• The model can save users enormous cognitive costs and time. It demands little by way of users’
attention and so improves upon the net time saving provided to users by existing productivity
platforms and services. But at the same time, it takes even greater trust by users in the reliability
and fairness of the model and of the platform providing it.
• The model produces a probabilistic service for its users. It does so by consuming information
inputs in a production process (“training”) to produce outputs that may vary each time. In the
same way, an orchestra will train to gain skills, and then each performance may vary depending
on the occasion. This makes it even harder to measure bad behaviour from the outside, making
the need for pre-emptive disclosures even more urgent.
• While the first generation of LLMs were not updated in real time through interaction with users,
suppliers, and advertisers, that is coming. The early instantiations of today’s web applications
were also relatively static captures of a moment in time, and only became rapidly updated as the
technology progressed. But even today, these models depend on content created by humans – the
vast corpus of human knowledge and creativity on which they have been trained.
Despite, and perhaps because of, all these differences between current search, recommendation, and
feed algorithms and LLMs, the need for disclosure is paramount. Like their predecessors, these LLM
systems internalise and centralise a vast marketplace of human knowledge and experience. As presently
implemented, AI systems pass through neither attention nor remuneration to the providers of content
used to train the model. As in present systems, human inputs are regarded as raw materials that can be
appropriated by the developer of the system. If history is any guide, control over these raw materials by
frontier AI platforms will eventually lead to the quest for a business model that allows for the extraction
of monopoly rents.
Looking back at what we know now about present platforms, we can only wish there had been a
40 Newell and Simon (1975, p. 13): notes: “The task of intelligence, then, is to avert the ever-present threat of the exponential
explosion of search.”

31

disclosure regime that would have shown us the state of these systems when their creators were focused
on serving their users and other ecosystem partners, and thus told us when and how they began to turn
from that path to extract self-serving economic rents. Much like their predecessors, these frontier AI
systems are managed by metrics whose details are known only to their creators and disclosed to the
outside world only via generalities and sporadic, often self-serving data points. The time to establish
rules for disclosure of operating metrics for frontier AI systems is now (O’Reilly 2023).
We are still in the early stages of the attention economy, and innovation should be allowed to
flourish. But this places an even greater emphasis on the need for transparency, and the establishment
of baseline reporting frameworks that will allow regulators to measure whether attention allocation
systems, including frontier AI systems, are getting better or worse over time. Greater public visibility
into the operation of these platforms can, in conjunction with more informed policy making, lead to
better behaviour on the part of those who own and manage these systems, more balanced ecosystems
of value creation, and the optimal use of knowledge in society.

32

References
Airbnb (2022). “Airbnb Is Introducing Total Price Display and Updating Guest Checkout.” Airbnb.
Online: https : / / news . airbnb . com / airbnb - is - introducing - total - price - display - and updating-guest-checkout/.
Albrecht, Jan Philipp (2016). “How the GDPR Will Change the World.” European Data Protection Law
Review 2.3, pp. 287–289.
Alchian, Armen A. (2017). “Rent.” The New Palgrave Dictionary of Economics. Ed. by Steven Durlauf
and Lawrence E Blume. Palgrave Macmillan UK, pp. 1–6.
Amazon.com (2022). “Amazon.com 10-K.” US Securities and Exchange Commission. Online: https:
//www.sec.gov/Archives/edgar/data/1018724/000101872423000004/amzn- 20221231.htm#
icc32c5c732854b7f9975929c57cd5bd4_88.
Areeda, Phillip and Herbert Hovenkamp (2023). Antitrust Law: An analysis of antitrust principles and
their application. Wolters Kluwer: Online.
Barinka, Alex (2023). “TikTok Starts US Retail Push with Copycats, Trinkets.” Bloomberg. Online:
https://www.bloomberg.com/news/newsletters/2023- 09- 08/tiktok- starts- us- retailpush-with-copycats-trinkets.
Begent, Carole and Kate Collyer (2013). “OECD Roundtable on the Role and Measurement of Quality
in Competition Analysis (UK Contribution).” Competititon Law Journal 12, p. 452.
Behringer, Stefan and Lapo Filistrucchi (2015). “Areeda–Turner in Two-Sided Markets.” Review of
Industrial Organization 46.3, pp. 287–306.
Blacquière, Eduard (2014). “Steeds meer ruimte AdWords, ten koste van SEO.” EdWords.nl. Online:
https://www.edwords.nl/2014/04/27/steeds-meer-ruimte-adwords-ten-koste-van-seo/.
Blaug, Mark (1997). Economic Theory in Retrospect. 5th ed. Cambridge University Press.
Boyce, James K (2022). “Political Economy of the Environment: A Look Back and Ahead.” The Routledge Handbook of the Political Economy of the Environment. Ed. by Éloi Laurent and Klara Zwickl.
Routledge.
Brin, Sergey (1998). “The PageRank Citation Ranking: Bringing order to the web.” Proceedings of ASIS,
1998 98, pp. 161–172.
Business of Apps (2022). “CPC Rates.” Online: https : / / www . businessofapps . com / ads / cpc /
research/cpc-rates/.
Choudhury, Avishek and Hamid Shamszare (2023). “Investigating the Impact of User Trust on the
Adoption and Use of ChatGPT: Survey Analysis.” Journal of Medical Internet Research 25.
Christophers, Brett (2020). Rentier Capitalism: Who Owns the Economy and Who Pays for It? London:
Wiley.
Competition & Markets Authority, CMA (2022). “Evidence Review of Online Choice Architecture and
Consumer and Competition Harm.” Online: https://www.gov.uk/government/publications/
online-choice-architecture-how-digital-design-can-harm-competition-and-consumers/
evidence-review-of-online-choice-architecture-and-consumer-and-competition-harm.
Craswell, Nick et al. (2008). “An Experimental Comparison of Click Position-Bias Models.” Proceedings
of the 2008 International Conference on Web Search and Data Mining. WSDM ’08. Association for
Computing Machinery, pp. 87–94.
Dean, Brian (2023). “We Analyzed 4 Million Google Search Results. Here’s What We Learned about
Organic CTR.” Backlinko. Online: https://backlinko.com/google-ctr-stats.
Doctorow, Cory (2023). “The ‘Enshittification’ of TikTok.” Wired. Online: https://www.wired.com/
story/tiktok-platforms-cory-doctorow/.
Epic Games v. Apple Inc. (2021). United States District Court Northern District of California. Case
No. 20-cv-05640-YGR. Online: https : / / cand . uscourts . gov / cases - e - filing / cases - of interest/epic-games-inc-v-apple-inc/.
33

Federal Trade Commission, et al. v. Amazon.Com, Inc. (2023). United States District Court for the
Western District of Washington. Case No. 2:23-cv-01495. Online: https://www.ftc.gov/system/
files/ftc_gov/pdf/1910129AmazoneCommerceComplaintPublic.pdf.
Feedvisor (2022). “The 2022 Amazon Consumer Behavior Report.” Feedvisor. Online: https://feedvisor.
com/resources/e-commerce-strategies/the-2022-amazon-consumer-behavior-report/.
Fletcher, Amelia (2012). “Drip Pricing: UK Experience.” US Federal Trade Commission. Online: https:
//www.ftc.gov/sites/default/files/documents/public_events/economics-drip-pricing/
afletcher.pdf.
Foley, Duncan K. (2008). Adam’s Fallacy: A Guide to Economic Theology. Belknap Harvard.
FTC (2023). “FTC Proposes Rule to Ban Junk Fees.” FTC. Online: Phttps://www.ftc.gov/newsevents/news/press-releases/2023/10/ftc-proposes-rule-ban-junk-fees.
Goodwin, Danny (2012). “Organic vs. Paid Search Results: Organic Wins 94% of Time.” Search Engine
Watch. Online: https://www.searchenginewatch.com/2012/08/23/organic-vs-paid-searchresults-organic-wins-94-of-time/.
— (2023). “Former Googler: Google ‘Using Clicks in Rankings’.” Search Engine Land. Online: https:
//searchengineland.com/former-googler-google-using-clicks-in-rankings-432401.
Google (2023a). “Rigorous Testing – How Google Search Works.” Google. Online: https://www.google.
com/intl/en_uk/search/howsearchworks/how-search-works/rigorous-testing/.
— (2023b). “About Ad Quality.” Google Ads Help. Online: https://support.google.com/googleads/answer/156066?sjid=12077254068652264551-NA#QSvAR (visited on 10/05/2023).
Gornyi, Alexander (2023). “Letter: Why Amazon’s Advertising Revenue Is Not What It Seems.” Financial Times. Online: https://www.ft.com/content/e1969f6e-85ce-42aa-9149-ca21a8a895ad.
Graham, Victoria (2023). “FTC Sues Amazon for Illegally Maintaining Monopoly Power.” US Federal
Trade Commission. Online: https://www.ftc.gov/news-events/news/press-releases/2023/
09/ftc-sues-amazon-illegally-maintaining-monopoly-power (visited on 10/05/2023).
Hawkins, Joy (2018). “Yelp vs Google: How They Deal with Fake Reviews.” Search Engine Land. Online:
https://searchengineland.com/yelp-vs-google-how-do-they-deal-with-fake-reviews307332.
Hayek, Friedrich A. (1945). “The Use of Knowledge in Society.” The American Economic Review 35.4,
pp. 519–530.
Hohnhold, Henning, Deirdre O’Brien, and Diane Tang (2015). “Focus on the Long-Term: It’s better
for Users and Business.” Proceedings 21st Conference on Knowledge Discovery and Data Mining.
Sydney, Australia. Online: http://dl.acm.org/citation.cfm?doid=2783258.2788583.
Hollinrake, Kevin (2023). “Government Clampdown on Fake Reviews and Hidden Fees to Help Customers Cut the Costs of Living.” UK Department for Business and Trade. Online: https://www.
gov.uk/government/news/government- clampdown- on- fake- reviews- and- hidden- fees- tohelp-customers-cut-the-costs-of-living.
Hovenkamp, Herbert (2020). “Antitrust and Platform Monopoly.” Yale Law Journal 130.8, pp. 1952–
2051.
Hugonenc, Caroline (2022). “Attention Is the New Metric.” Advertising Week. Online: https : / /
advertisingweek.com/attention-is-the-new-metric/.
Hunt, Stephan (2022). “The Technology-Led Transformation of Competition and Consumer Agencies:
The Competition and Markets Authority’s experience.” UK Competition & Markets Authority. Online: https://www.gov.uk/government/publications/the-technology-led-transformationof-competition-and-consumer-agencies-the-cmas-experience.
Hwang, Tim (2020). Subprime Attention Crisis: Advertising and the time bomb at the heart of the
internet. FSG Originals.

34

Internet Advertising Bureau (2020). “Understanding Brand Safety & Brand Suitability in a Contemporary Media Landscape.” IAB. Online: https://www.iab.com/wp-content/uploads/2020/12/IAB_
Brand_Safety_and_Suitability_Guide_2020-12.pdf.
Joachims, Thorsten, Adith Swaminathan, and Tobias Schnabel (2017). “Unbiased Learning-to-Rank
with Biased Feedback.” Proceedings of the Tenth ACM International Conference on Web Search and
Data Mining, pp. 781–789.
Jullien, Bruno, Alessandro Pavan, and Marc Rysman (2021). “Chapter 7: Two-sided Markets, Pricing,
and Network Effects.” Handbook of Industrial Organization. Ed. by Kate Ho, Ali Hortaçsu, and
Alessandro Lizzeri. Vol. 4, pp. 485–592.
Jumpshot (2018). “The Competitive State of eCommerce Marketplaces: Data Report Q2 2018.” Jumpshot. Online: available%20on%20request.
Jungle Scout (2022). “State of the Amazon Seller.” Jungle Scout. Online: https://www.junglescout.
com/amazon-seller-report/2022-results/.
Kahneman, Daniel (2011). Thinking, Fast and Slow. New York: Farrar, Straus and Giroux.
Kaziukėnas, Juozas (2021). “Everything on Amazon Is an Ad.” Marketplace Pulse. Online: https :
//www.marketplacepulse.com/articles/everything-on-amazon-is-an-ad.
— (2022). “Amazon is Burying Organic Search Results.” Marketplace Pulse. Online: https://www.
marketplacepulse.com/articles/amazon-is-burying-organic-search-results.
Keane, Mark T. and Maeve O’Brien (2006). “Modeling Result-List Searching in the World Wide Web:
The Role of Relevance Topologies and Trust Bias.” Proceedings of the Annual Meeting of the Cognitive
Science Society 28.
Keane, Mark T., Maeve O’Brien, and Barry Smyth (2008). “Are People Biased in their Use of Search
Engines?” Communications of the ACM 51.2, pp. 49–52.
Kim, Larry (2016). “Google Kills off Side Ads: What You Need to Know.” WordStream. Online: https:
//www.wordstream.com/blog/ws/2016/02/22/google-kills-off-right-side-ads.
Kuriata, Gabriel (2022). “Apple Search Ads Cost: CPT, CPA and CR Benchmarks 2022.” SplitMetrics.
Online: https://splitmetrics.com/blog/apple-search-ads-cost/.
Kurz, Mordecai (2023). The Market Power of Technology. New York: Columbia University Press.
Lopatenko, Andrei et al. (2015). “Ranking Search Results Based on Similar Queries.” U.S. pat. Google
LLC. Online: https://patents.google.com/patent/US9009146B1/en.
Marvin, Ginny (2020). “A Visual History of Google Ad Labeling in Search Results.” Search Engine Land.
Online: https://searchengineland.com/search-ad-labeling-history-google-bing-254332.
Mazzucato, Mariana (2018). The Value of Everything: Making and taking in the global economy. Hachette UK.
Mazzucato, Mariana, Josh Ryan-Collins, and Giorgos Gouzoulis (2023). “Mapping Modern Economic
Rents: The good, the bad, and the grey areas.” Cambridge Journal of Economics 47.3, pp. 507–534.
Mazzucato, Mariana, Ilan Strauss, et al. (2023). “Regulating Big Tech: The Role of Enhanced Disclosures.” Oxford Review of Economic Policy 39.1, pp. 47–69.
Mileva, Geri (2022). “Amazon Ad Revenue Statistics That Will Blow Your Mind.” Influencer Marketing
Hub. Online: https://influencermarketinghub.com/amazon-ad-revenue/.
Mitchell, Stacy (2023). “New Research: Amazon’s Monopoly Tollbooth in 2023.” Institute for Local
Self-Reliance. Online: https://ilsr.org/amazonmonopolytollbooth-2023/.
Morrison, Sara (2021). “Amazon’s Strategy to Squeeze Marketplace Sellers and Maximize Its Own
Profits Is Evolving.” Vox. Online: https://www.vox.com/recode/22810795/amazon-marketplaceprime-report.
Newell, Allen and Herbert A. Simon (1975). “Computer Science as Empirical Inquiry: Symbols and
search.” ACM Turing award lectures.
Newman, John M. (2015). “Antitrust in Zero-Price Markets: Foundations.” University of Pennsylvania
Law Review 164.1, pp. 149–206.
35

O’Reilly, Tim (2019). “Antitrust Regulators Are Using the Wrong Tools to Break up Big Tech.” Quartz.
Online: https://qz.com/1666863/why-big-tech-keeps-outsmarting-antitrust-regulators.
— (2022). “Google Shopping Search.” O’Reilly Media. Online: https : / / www . oreilly . com / tim /
antitrust/shoppingsearch.html.
— (2023). “You Can’t Regulate What You Don’t Understand.” O’Reilly Media. Online: https://www.
oreilly.com/content/you-cant-regulate-what-you-dont-understand-2/.
O’Reilly, Tim, Ilan Strauss, and Mariana Mazzucato (2023). “Regulating Big Tech through digital
disclosures.” UCL IIPP Policy Brief No.26 June 2023. Online: https://www.ucl.ac.uk/bartlett/
public-purpose/sites/bartlett_public_purpose/files/oreilly_strauss_mazzucato_2023.
regulating_big_tech_through_digital_disclosures.pdf.
Palmer, Annie (2021). “Amazon is Piling Ads into Search Results and Top Consumer Brands Are Paying
up for Prominent Placement.” CNBC. Online: https : / / www . cnbc . com / 2021 / 09 / 19 / amazon piles-ads-into-search-results-as-big-brands-pay-for-placement.html.
Petit, Nicolas (2020). Big Tech and the Digital Economy: The Moligopoly Scenario. Oxford University
Press.
Petit, Nicolas and David J. Teece (2020). “Taking Ecosystems Competition Seriously in the Digital Economy: A (Preliminary) Dynamic Competition/Capabilities Perspective.” OECD Directorate for Financial and Enterprise Affairs Competition Committee. Online: https://one.oecd.org/document/
DAF/COMP/WD(2020)90/en/pdf.
Petrescu, Philip (2014). “How Ads Influence Organic Click-through Rate on Google.” Search Engine
Land. Online: https://searchengineland.com/different- types- ads- influence- organicctr-google-204676.
Piketty, Thomas (2014). Capital in the 21st Century. Trans. by Arthur Goldhammer. Cambridge MA:
Belknap Press.
Quartile (2018). “New Study Reveals Amazon’s Quiet Shift toward ’pay-to-Play’ Platform - and What
It Means for Brands.” PR Newswire. Online: https://www.prnewswire.com/news-releases/newstudy-reveals-amazons-quiet-shift-toward-pay-to-play-platform--and-what-it-meansfor-brands-300759702.html.
Ricks, Becca and Jesse McCrosky (2022). “Does This Button Work? Investigating YouTube’s Ineffective
User Controls.” Mozilla Foundation. Online: https://foundation.mozilla.org/en/research/
library/user-controls/report/.
Robinson, Joan (2001). The Economics of Imperfect Competition. Palgrave.
Rochet, Jean-Charles and Jean Tirole (2003). “Platform Competition in Two-Sided Markets.” Journal
of the European Economic Association 1.4, pp. 990–1029.
— (2006). “Two-Sided Markets: A Progress Report.” The RAND Journal of Economics 37.3.
Rock, Rufus et al. (2023). “Behind the Clicks: Can Amazon allocate user attention as it pleases?”
UCL IIPP Working Paper Forthcoming. Online: https://www.ucl.ac.uk/bartlett/publicpurpose / research / digital - economy - and - algorithmic - rents / algorithmic - attention rents.
Ryan-Collins, Josh, Toby Lloyd, and Laurie Macfarlane (2017). Rethinking the Economics of Land and
Housing. London: New Economics Foundation.
Samuelson, Paul A. and William D. Nordhaus (2010). Economics. 19th ed. McGraw-Hill Irwin.
Schumpeter, Joseph A (2013). Capitalism, Socialism and Democracy. Routledge.
Sen, Amartya (2017). “Rational Behaviour.” The New Palgrave Dictionary of Economics. Ed. by Steven
Durlauf and Lawrence E Blume. Palgrave Macmillan UK, pp. 1–14.
Simon, Herbert A. (1955). “A Behavioral Model of Rational Choice.” The Quarterly Journal of Economics 69.1, p. 99.
— (1971). “Designing Organizations for an Information-Rich World.” Computers, communications, and
the public interest 72, p. 37.
36

Simon, Herbert A. (1978a). “Information-Processing Theory of Human Problem Solving.” Handbook of
Learning and Cognitive Processes. Ed. by W.K. Estes. NJ: Lawrence Erlbaum Associates, pp. 271–
295.
— (1978b). “Rationality as Process and as Product of Thought.” The American Economic Review 68.2,
pp. 1–16.
— (1995). “The Information-Processing Theory of Mind.” The American Psychologist 50.7.
— (1997). Administrative Behavior: A Study of Decision-Making Processes in Administrative Organizations. 4th ed. Free Press.
— (2017). “Bounded Rationality.” The New Palgrave Dictionary of Economics. Ed. by Steven Durlauf
and Lawrence E Blume. Palgrave Macmillan UK, pp. 1–4.
Soper, Spencer (2023). “Amazon Is Taking Half of Each Sale from Its Merchants.” Bloomberg.com.
Online: https://www.bloomberg.com/news/articles/2023-02-13/amazon-amzn-takes-halfof-each-sale-from-2-million-small-businesses.
Sorokina, Daria and Erick Cantu-Paz (2016). “Amazon Search: The joy of ranking products.” Proceedings
of the 39th International ACM SIGIR conference on Research and Development in Information
Retrieval, pp. 459–460.
Srinivasan, Dina (2019). “The Antitrust Case against Facebook: A Monopolist’s Journey towards Pervasive Surveillance in Spite of Consumers’ Preference for Privacy.” Berkeley Business Law Journal
16.1, pp. 39–101.
Standing, Guy (2016). The Precariat: The new dangerous class. Bloomsbury Academic.
Stiglitz, Joseph E. (2019). People, Power, and Profits: Progressive capitalism for an age of discontent.
London: Penguin UK.
Stone, Brad (2021). Amazon Unbound. New York: Simon and Schuster.
Strandburg, Katherine J. (2013). “Free Fall: The Online Market’s Consumer Preference Disconnect the
Frontiers of Consumer Protection.” University of Chicago Legal Forum 2013, pp. 95–172.
Strauss, Ilan, Tim O’Reilly, and Mariana Mazzucato (2023). “Amazon’s Algorithmic Attention Rents.”
UCL IIPP Working Paper Forthcoming. Online: https://www.ucl.ac.uk/bartlett/publicpurpose / research / digital - economy - and - algorithmic - rents / algorithmic - attention rents.
Stray, Jonathan (2021). “Beyond Engagement: Aligning Algorithmic Recommendations with Prosocial Goals.” Partnership on AI. Online: https : / / partnershiponai . org / beyond - engagement aligning-algorithmic-recommendations-with-prosocial-goals/.
The Badger (2023). “Amazon Advertising Stats.” Ad Badger. Online: https://www.adbadger.com/
blog/amazon-advertising-stats/.
Thompson, Ben (2014). “Economic Power in the Age of Abundance.” Stratechery.com. Online: https:
//stratechery.com/2014/economic-power-age-abundance/.
— (2023). “Commoditizing Suppliers.” Stratechery.com. Online: https://stratechery.com/concept/
aggregation-theory/commoditizing-suppliers/.
Tirole, Jean (2017). Economics for the Common Good. Princeton University Press.
Tversky, Amos and Daniel Kahneman (1974). “Judgment under Uncertainty: Heuristics and Biases.”
Science 185.4157, pp. 1124–1131.
— (1981). “The Framing of Decisions and the Psychology of Choice.” Science 211.4481, pp. 453–458.
U.S. Federal Trade Commission (2023). “Federal Trade Commission Announces Proposed Rule Banning
Fake Reviews and Testimonials.” Online: https : / / www . ftc . gov / news - events / news / press releases/2023/06/federal- trade- commission- announces- proposed- rule- banning- fakereviews-testimonials.
United States of America v. Google LLC (2020). United States District Court for the District of
Columbia. Case No. 1:20-cv-03010-APM. Online: https://cdn.arstechnica.net/wp- content/
uploads/2023/09/US-v-Google-DOJ-Pre-Trial-Brief-9-8-2023.pdf.
37

US Federal Trade Commission (2022). “Unfair or Deceptive Fees Trade Regulation Rule.” R207011.
Online: https://www.federalregister.gov/documents/2022/11/08/2022-24326/unfair-ordeceptive-fees-trade-regulation-rule-commission-matter-no-r207011.
Wang, Xuanhui et al. (2018). “Position Bias Estimation for Unbiased Learning to Rank in Personal
Search.” Proceedings of the Eleventh ACM International Conference on Web Search and Data Mining.
WSDM ’18. Association for Computing Machinery, pp. 610–618.
Weyl, E Glen (2010). “A Price Theory of Multi-Sided Platforms.” American Economic Review 100.4,
pp. 1642–1672.
Whish, Richard and David Bailey (2021). Competition Law. 10th ed. Oxford University Press.
Wilkes, Jeff (2012). “Virtuous Cycle.” YouTube. Online: https : / / www . youtube . com / watch ? v =
5jcDlGn-tZA.
Wu, Tim (2013). “The Oligopoly Problem.” The New Yorker. Online: https://www.newyorker.com/
tech/annals-of-technology/the-oligopoly-problem.
Yue, Yisong, Rajan Patel, and Hein Roehrig (2010). “Beyond Position Bias: Examining Result Attractiveness as a Source of Presentation Bias in Clickthrough Data.” ACM: Proceedings of the 19th
International Conference on World Wide Web, pp. 1011–1018.
Zuboff, Shoshana (2019). The Age of Surveillance Capitalism: The fight for a human future at the new
frontier of power. London: Profile Books.

38

UCL Institute for Innovation and Public Purpose
11 Montague Street, London, WC1B 5BP
@IIPP_UCL
ucl.ac.uk/IIPP
