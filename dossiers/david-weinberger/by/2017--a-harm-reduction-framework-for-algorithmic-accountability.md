---
title: "[liveblog][ai] A Harm-reduction framework for algorithmic accountability"
person: david-weinberger
section: by
type: blog-post
year: 2017
date: 2017-11-19
venue: "Joho the Blog (hyperorg.com)"
authors: "David Weinberger"
source_url: https://hyperorg.com/2017/11/19/liveblogai-a-harm-reduction-framework-for-algorithmic-accountability/
retrieved: 2026-08-13
content: full-text
notes: "Post from Joho the Blog (hyperorg.com), Weinberger's personal blog. Retrieved via the site's WordPress REST API; HTML converted to plain text. Live-blogged notes taken during another speaker's talk or panel — the summarized content is the speaker's, the framing and commentary are Weinberger's."
---

# [liveblog][ai] A Harm-reduction framework for algorithmic accountability

## Full text

I’m at one of the weekly Harvard’s Berkman Klein Center for Internet & Society and MIT Media Lab talks. Alexandra Wood and Micah Altman are talking about “A harm reduction framework for algorithmic accountability over personal information” — a snapshot of their ongoing research at the Privacy Tools Project. The PTP is an interdisciplinary project that investigates tools for sharing info while preserving privacy.

NOTE: Live-blogging. Getting things wrong. Missing points. Omitting key information. Introducing artificial choppiness. Over-emphasizing small matters. Paraphrasing badly. Not running a spellpchecker. Mangling other people’s ideas and words. You are warned, people.

Alexandra says they’ve been developing frameworks for assessing privacy risk when collecting personal data, and have been looking at the controls that can be used to protect individuals. They’ve found that privacy tools address a narrow slice of the problem; other types of misuse of data require other approaches.

She refers to some risk assessment algorithms used by the courts that have turned out to be racially biased, to have unbalanced error rates (falsely flagging black defendants as future criminals at twice the rate as white defendents), and are highly inaccurate. “What’s missing is an analysis of harm”What’s missing is an analysis of harm. “Current approaches to regulating algorithmic classification and decision-making largely elide harm,” she says. “The ethical norms in the law point to the broader responsibilities of the algorithms’ designers.”

Micah says there isn’t a lot of work mapping the loss privacy to other harms. The project is taking an interdisciplinary approach to this. [I don’t trust my blogging here. Don’t get upset with Micah for my ignorance-based reporting!]

Social science treats harm pragmatically. It finds four main dimensions of well-being: wealth, health, life satisfaction and the meaningful choices available to people. Different schools take different approaches to this, some emphasizing physical and psychological health, others life satisfaction, etc.

But to assess harm, you need to look at people’s lives over time. E.g., how does going to prison affect people’s lives? Being sentenced decreases your health, life-satisfaction, choices, and loer income. “The consequences of sentencing are persistent and individually catastrophic.”

He shows a chart from ProPublica based on Broward County data that shows that the risk scores for white defendants skews heavily toward lower scores while the scores for black defendants is more evenly distributed. This by itself doesn’t prove that it’s unfair. You have to look at the causes of the differences in those distributions.

Modern inference theory says something different about harm. A choice is harmful if the causal effect of that outcome is worse, and the causal effect is measured by potential outcomes. “The causal impact of smoking is not simply that you may get cancer, but includes the impact of not smoking”The causal impact of smoking is not simply that you may get cancer, but includes the impact of not smoking, such as possibly gaining weight. You have to look at the counter-factuals

The COMPAS risk assessment tool that has been the subject of much criticism is affected by which training data you use, choice of algorithm, the application of it to the individual, and the use of the score in sentencing. Should you exclude information about race? Or exclude any info that might violate people’s privacy? Or make it open or not? And how to use the outcomes?

Can various protections reduce harm from COMPAS? Racial features were not explicitly included in the COMPAS model. But there are proxies for race. Removing the proxies could lead to less accurate predictions, and make it difficult to study and correct for bias. That is, removing that data (features) doesn’t help that much and might prevent you from applying corrective measures.

Suppose you throw out the risk score. Judges are still biased. “The adverse impact is potentially greater when the decision is not informed by an algorithm’s prediction.” A recent paper by John Kleinberg showed that “algorithms predicting pre-trial assessments were less biased than decisions made by human judges”algorithms predicting pre-trial assessments were less biased than decisions made by human judges. [I hope I got that right. It sounds like a significant finding.]

There’s another step: going from the outcomes to the burdens these outcomes put on people. “An even distribution of outcomes can produce disproportionate burdens.” E.g. juvenile defendants have more to lose — more of their years will be negatively affected by a jail sentence — so having the same false positive and negatives for adults and juveniles would impost a greater burden on the juveniles. When deciding it an algorithmic decision is unjust, you can’t just look at the equality of error rates.

A decision is unjust when it is: 1. Dominated (all groups pay a higher burden for the same social benefit); 2. Unprogressive (higher relative burdens on members of classes who are less well off); 3. Individually catastrophic (wrong decisions are so harmful that it reduces the well being of individuals in members of a known class); 4) Group punishment (an effect on an entire disadvantaged class.)

For every decision, theere are unavoidable constraints: a tradeoff between the individual and the social group; a privacy cost; can’t be equally accurate in all categories; can’t be fair without comparing utility across people; it’s impossible to avoid constraints by adding human judgment because the human is still governed by these constraints.

Micah’s summary for COMPAS: 1. Some protections would be irrelevant (inclusion of sensitive characteristics and and protection of indvidual information). Other protections would be insufficient (no intention to discriminate, open source/open data/FCRA).

Micah ends with a key question about fairness that has been too neglected: “Do black defendants bear a relatively higher cost than whites from bad decisions that prevent the same social harms?”
