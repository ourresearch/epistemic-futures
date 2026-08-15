---
title: "[liveblog] Neil Gaikwad Human-AI Collaboration for Sustainable Market Design"
person: david-weinberger
section: by
type: blog-post
year: 2018
date: 2018-04-05
venue: "Joho the Blog (hyperorg.com)"
authors: "David Weinberger"
source_url: https://hyperorg.com/2018/04/05/liveblog-neil-gaikwad-human-ai-collaboration-for-sustainable-market-design/
retrieved: 2026-08-13
content: full-text
notes: "Post from Joho the Blog (hyperorg.com), Weinberger's personal blog. Retrieved via the site's WordPress REST API; HTML converted to plain text. Live-blogged notes taken during another speaker's talk or panel — the summarized content is the speaker's, the framing and commentary are Weinberger's."
---

# [liveblog] Neil Gaikwad Human-AI Collaboration for Sustainable Market Design

## Full text

I’m at a ThursdAI talk (Harvard’s Berkman Klein Center for Internet & Society and MIT Media Lab) being given by Neil Gaikwad (Twitter: @neilthemathguy, a Ph.D. at the MediaLab, in the Space Enabled Group.

NOTE: Live-blogging. Getting things wrong. Missing points. Omitting key information. Introducing artificial choppiness. Over-emphasizing small matters. Paraphrasing badly. Not running a spellpchecker. Mangling other people’s ideas and words. You are warned, people.

Markets and institutions are parts of complex ecosystem, Neil says. His research looks at data from satellites that show how the Earth is changing: crops, water, etc. Once you’ve gathered the data, you can use machine learning to visualize the changes. There are ecosystems, including of human behavior, that are affected by this. It affects markets and institutions. E.g., a drought may require an institutional response, and affect markets.

Traditional markets, financial markets, and gig economies all share characteristics. Farmers markets are complex ecosystems of people with differing information and different amounts of it, i.e. asymmetric info. Same for financial markets. Same for gig economies.

Indian markets have been failing; there have been 300,000 suicides in the last 30 years. Stock markets have crashed suddenly due to blackbox marketing; in some cases we still don’t know why. And London has banned Uber. So, it doesn’t matter which markets or institutions we look at, they’re losing our trust.

An article in New Scientist asked what we can do to regain this trust. For black box AI, there are questions of fairness and equity. But what would human-machine collaboration be like? Are there design principles for markets.?

Neil stops for us to discuss.

Q: How do you define the justice?

A: Good question. Fairness? Freedom? The designer has a choice about how to define it.

Q: A UN project created an IT platform that put together farmers and direct consumers. The pricing seemed fairer to both parties. So, maybe avoid intermediaries, as a design principle?

Neil continues. So, what is the concept of justice here?

1. Rawls and Kant: Transcendental institutionalism. It’s deontological: follow a principle for perfect justice. Use those principles to define a perfect institution. The properties are defined by a social contract. But it doesn’t work, as in the examples we just saw. What is missing. People and society. [I.e., you run the institution according to principles, but that doesn’t guarantee that the outcome will be fair and just. My example: Early Web enthusiasts like me thought the Web was an institution built on openness, equality, creative anarchy, etc., yet that obviously doesn’t ensure that the outcome will share those properties.]

2. Realized-focused institutionalism (Sen

2009): How to reverse this trend. It is consequentialist: what will be the consequences of the design of an institution. It’s a comparative assessment of different forms of institutions. Instead of asking for the perfectly justice society, Sen asks how justice can be advanced. The most critical tool for evaluating any institution is to look at how it actually realizes how people’s lives change.

Sen argues that principles are important. They can be expressed by “niti,” Sanskrit for rules and institutions. But you also need nyaya: a form of social arrangement that makes sure that those rules are obeyed. These rules come from social choice, not social contract.

Example: Gig economies. The data comes from mechanical turk, upwork, crowdflower, etc. This creates employment for many people, but it’s tough. E.g., identifying images. Use supervised learning for this. The Turkers, etc., do the labelling to train the image recognition system. The Turkers make almost no money at this. This is the wicked problem of market design: The worker can have identifications rejected, sometimes with demeaning comments.

“The Market for Lemons” (Akerlog, et al., 1970): all the cars started to look alike and now all gig-workers look alike to those who hire them: there’s no value given to bringing one’s value to the labor.

So, who owns the data? Who has a stake in the models? In the intellectual property?

If you’re a gig worker, you’re working with strangers. You don’t know the reputation of the person giving me data. Or renting me the Airbnb apartment. So, let’s put a rule: reputation is the backbone. In sharing economies, most of the ratings are the highest. Reputation inflation. So, can we trust reputation? This happens because people have no incentive to rate. There’s social pressure to give a positive rating.

So, thinking about Sen, can we think about an incentive for honest reputation? Neil’s group has been thinking about a system [I thought he said Boomerang, but I can’t find that]. It looks at the workers’ incentives. It looks at the workers’ ratings of each other. If you’re a requester, you’ll see the workers you like first.

Does this help AI design?

MoralMachine has had 1.3M voters and 18M pairwise comparisons (i.e., people deciding to go straight or right). Can this be used as a voting based system for ethical decision making (AAAI 2018)? You collect the pairwise preferences, learn the model of preference, come to a collective preference, and have voting rules for collective decision.

Q: Aren’t you collect preferences, not normative judgments? The data says people would rather kill fat people than skinny ones.

A: You need the social behavior but also rules. For this you have to bring people into the loop.

Q: How do we differentiate between what we say we want and what we really want?

A: There are techniques, such as “Bayesian Truth Serum”nomics.mit.edu/files/1966”>Bayesian Truth Serum.

Conclusion: The success of markets, institutions or algorithms, is highly dependent on how this actually affects people’s lives. This thinking should be central to the design and engineering of socio-technical systems.
