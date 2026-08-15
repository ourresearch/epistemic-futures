---
title: "[liveblog] Conclusion of Workshop on Trustworthy Algorithmic Decision-Making"
person: david-weinberger
section: by
type: blog-post
year: 2017
date: 2017-12-05
venue: "Joho the Blog (hyperorg.com)"
authors: "David Weinberger"
source_url: https://hyperorg.com/2017/12/05/liveblog-conclusion-of-workshop-on-trustworthy-algorithmic-decision-making/
retrieved: 2026-08-13
content: full-text
notes: "Post from Joho the Blog (hyperorg.com), Weinberger's personal blog. Retrieved via the site's WordPress REST API; HTML converted to plain text. Live-blogged notes taken during another speaker's talk or panel — the summarized content is the speaker's, the framing and commentary are Weinberger's."
---

# [liveblog] Conclusion of Workshop on Trustworthy Algorithmic Decision-Making

## Full text

I’ve been at a two-day workshop sponsored by the Michigan State Uiversity and the National Science Foundation: “Workshop on Trustworthy Algorithmic Decision-Making.” After multiple rounds of rotating through workgroups iterating on five different questions, each group presented its findings — questions, insights, areas of future research.

NOTE: Live-blogging. Getting things wrong. Missing points. Omitting key information. Introducing artificial choppiness. Over-emphasizing small matters. Paraphrasing badly. Not running a spellpchecker. Mangling other people’s ideas and words. You are warned, people.

Seriously, I cannot capture all of this.

Conduct of Data Science

What are the problems?

Who defines and how do we ensure good practice in data science and machine learning?

Why is the topic important? Because algorithms are important. And they have important real-world effects on people’s lives.

Why is the problem difficult?

Wrong incentives.

It can be difficult to generalize practices.

Best practices may be good for one goal but not another, e.g., efficiency but not social good. Also: Lack of shared concepts and vocabulary.

How to mitigate the problems?

Change incentives

Increase communication via vocabularies, translations

Education through MOOCS, meetups, professional organizations

Enable and encourage resource sharing: an open source lesson about bias, code sharing, data set sharing

Accountability group

The problem: How to integratively assess the impact of an algorithmic system on the public good? “Integrative” = the impact may be positive and negative and affect systems in complex ways. The impacts may be distributed differently across a population, so you have to think about disparities. These impacts may well change over time

We aim to encourage work that is:

Aspirationally casual: measuring outcomes causally but not always through randomized control trials.

The goal is not to shut down algorithms to to make positive contributions that generat solutions.

This is a difficult problem because:

Lack of variation in accountability, enforcements, and interventions.

It’s unclear what outcomes should be measure and how. This is context-dependent

It’s unclear which interventions are the highest priority

Why progress is possible: There’s a lot of good activity in this space. And it’s early in the topic so there’s an ability to significantly influence the field.

What are the barriers for success?

Incomplete understanding of contexts. So, think it in terms of socio-cultural approaches, and make it interdisciplinary.

The topic lies between disciplines. So, develop a common language.

High-level triangulation is difficult. Examine the issues at multiple scales, multiple levels of abstraction. Where you assess accountability may vary depending on what level/aspect you’re looking at.

Handling Uncertainty

The problem: How might we holistically treat and attribute uncertainty through data analysis and decisions systems. Uncertainty exists everywhere in these systems, so we need to consider how it moves through a system. This runs from choosing data sources to presenting results to decision-makers and people impacted by these results, and beyond that its incorporation into risk analysis and contingency planning. It’s always good to know where the uncertainty is coming from so you can address it.

Why difficult:

Uncertainty arises from many places

Recognizing and addressing uncertainties is a cyclical process

End users are bad at evaluating uncertain info and incorporating uncertainty in their thinking.

Many existing solutions are too computationally expensive to run on large data sets

Progress is possible:

We have sampling-based solutions that provide a framework.

Some app communities are recognizing that ignoring uncertainty is reducing the quality of their work

How to evaluate and recognize success?

A/B testing can show that decision making is better after incorporating uncertainty into analysis

Statistical/mathematical analysis

Barriers to success

Cognition: Train users.

It may be difficult to break this problem into small pieces and solve them individually

Gaps in theory: many of the problems cannot currently be solved algorithmically.

The presentation ends with a note: “In some cases, uncertainty is a useful tool.” E.g., it can make the system harder to game.

Adversaries, workarounds, and feedback loops

Adversarial examples: add a perturbation to a sample and it disrupts the classification. An adversary tries to find those perturbations to wreck your model. Sometimes this is used not to hack the system so much as to prevent the system from, for example, recognizing your face during a protest.

Feedback loops: A recidivism prediction system says you’re likely to commit further crimes, which sends you to prison, which increases the likelihood that you’ll commit further crimes.

What is the problem: How should a trustworthy algorithm account for adversaries, workarounds, and feedback loops?

Who are the stakeholders?

System designers, users, non-users, and perhaps adversaries.

Why is this a difficult problem?

It’s hard to define the boundaries of the system

From whose vantage point do we define adversarial behavior, workarounds, and feedback loops.

Unsolved problems

How do we reason about the incentives users and non-users have when interacting with systems in unintended ways.

How do we think about oversight and revision in algorithms with respect to feedback mechanisms

How do we monitor changes, assess anomalies, and implement safeguards?

How do we account for stakeholders while preserving rights?

How to recognize progress?

Mathematical model of how people use the system

Define goals

Find stable metrics and monitor them closely

Proximal metrics. Causality?

Establish methodologies and see them used

See a taxonomy of adversarial behavior used in practice

Likely approaches

Security methodology to anticipating and unintended behaviors and adversarial interactions’. Monitor and measure

Record and taxonomize adversarial behavior in different domains

Test . Try to break things.

Barriers

Hard to anticipate unanticipated behavior

Hard to define the problem in particular cases.

Goodhardt’s Law

Systems are born brittle

What constitutes adversarial behavior vs. a workaround is subjective.

Dynamic problem

Algorithms and trust

How do you define and operationalize trust.

The problem: What are the processes through which different stakeholders come to trust an algorithm?

Multiple processes lead to trust.

Procedural vs. substantive trust: are you looking at the weights of the algorithms (e.g.), or what were the steps to get you there?

Social vs personal: did you see the algorithm at work, or are you relying on peers?

These pathways are not necessarily predictive of each other.

Stakeholders build truth through multiple lenses and priorities

the builders of the algorithms

the people who are affected

those who oversee the outcomes

Mini case study: a child services agency that does not want to be identified. [All of the following is 100% subject to my injection of errors.]

The agency uses a predictive algorithm. The stakeholders range from the children needing a family, to NYers as a whole. The agency knew what into the model. “We didn’t buy our algorithm from a black-box vendor.” They trusted the algorithm because they staffed a technical team who had credentials and had experience with ethics…and who they trusted intuitively as good people. Few of these are the quantitative metrics that devs spend their time on. Note that FAT (fairness, accountability, transparency) metrics were not what led to trust.

Temporality:

Processes that build trust happen over time.

Trust can change or maybe be repaired over time. “

The timescales to build social trust are outside the scope of traditional experiments,” although you can perhaps find natural experiments.

Barriers:

Assumption of reducibility or transfer from subcomponents

Access to internal stakeholders for interviews and process understanding

Some elements are very long term

What’s next for this workshop

We generated a lot of scribbles, post-it notes, flip charts, Slack conversations, slide decks, etc. They’re going to put together a whitepaper that goes through the major issues, organizing them, and tries to capture the complexity while helping to make sense of it.

There are weak or no incentives to set appropriate levels of trust

Key takeways:

Trust is irreducible to FAT metrics alone

Trust is built over time and should be defined in terms of the temporal process

Isolating the algorithm as an instantiation misses the socio-technical factors in trust.
