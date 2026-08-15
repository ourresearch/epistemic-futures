---
title: "[liveblog] Nathan Matias on The Social impact of real-time algorithm decisions"
person: david-weinberger
section: by
type: blog-post
year: 2017
date: 2017-10-27
venue: "Joho the Blog (hyperorg.com)"
authors: "David Weinberger"
source_url: https://hyperorg.com/2017/10/27/liveblog-nathan-matias-on-the-social-impact-of-real-time-algorithm-decisions/
retrieved: 2026-08-13
content: full-text
notes: "Post from Joho the Blog (hyperorg.com), Weinberger's personal blog. Retrieved via the site's WordPress REST API; HTML converted to plain text. Live-blogged notes taken during another speaker's talk or panel — the summarized content is the speaker's, the framing and commentary are Weinberger's."
---

# [liveblog] Nathan Matias on The Social impact of real-time algorithm decisions

## Full text

J. Nathan Matias is giving a talk at the weekly AI session held by MIT Media Lab and Harvard’s Berkman Klein Center for Internet & Society. The title is: Testing the social impact of real-time algorithm decisions. (SPOILER: Nate is awesome.) Nathan will be introducing CivilServant.io to us, a service for researching the effects of tech and how it can be better directed to toward the social outcomes we (the civil society “we”) desire. (That’s my paraphrase.)

NOTE: Live-blogging. Getting things wrong. Missing points. Omitting key information. Introducing artificial choppiness. Over-emphasizing small matters. Paraphrasing badly. Not running a spellpchecker. Mangling other people’s ideas and words. You are warned, people.

In 2008, the French government approved a law against Web sites that encourage anorexia and bulimia. In 2012, Instagram responded to pressure to limit hashtags that “actively promote self-harm.” Instagram had 40M users, almost as many as France’s 55M active Net users. Researchers at Georgia Tech several years later found that some self-harm sites on Instagram had higher engagement after Instagram’s actions. “ If your algorithm reliably detects people who are at risk of committing suicide, what next? ” If your algorithm reliably detects people who are at risk of committing suicide, what next? If the intervention isn helpful, your algorithm is doing harm.

Nathan shows a two-axis grid for evaluating algorithms: fair-unfair and benefits-harms. Accuracy should be considered to be on the same axis as fairness because it can be measured mathematically. But you can’t test the social impact without putting it into the field. “I’m trying to draw attention to the vertical axis [harm-benefit].”

We often have in mind a particular pipeline: training > model > prediction > people . Sometimes there are rapid feedback loops where the decisions made by people feed back into the model. A judicial system’s prediction risk scores may have no such loop. But the AI that manages a news feed is probably getting the readers’ response as data that tunes the model.

We have organizations that check the quality of items we deal with: UL for electrical products, etc. But we don’t have that sort of consumer protection for social tech. The results are moral panics, bad policies, etc. This is the gap Nate is trying to fill with CivilServant.io, a project supported by the Media Lab and GlobalVoices.

Here’s an example of one of CivilServant’s projects:

Managing fake news is essential for democracy. The social sciences have been dealing with this for quite a while by doing research on individual perception and beliefs, on how social context and culture influence beliefs … and now on algorithms that make autonomous decisions that affect us as citizens e.g., newsfeeds. Newsfeeds work this way: someone posts a link. People react to it, e.g. upvote, discuss, etc. The feed service watches that behavior and uses it to promote or demote the item. And then it feeds back in.

We’ve seen lots of examples of pernicious outcomes of this. E.g., at Reddit an early upvote can have dramatic impact on its ratings over time.

What can we do to govern online misinfo? We could surveill and censor. We could encourage counter-speech. We can imagine some type of algorithmic governance. We can use behavioral nudges, e.g. Facebook tagging articles as “disputed.” But all of these assume that these interventions change behaviors and beliefs. Those assumptions are not always tested.

Nate was approached by /r/worldnews at Reddit, a subreddit with14M subscribers and 70 moderators. At Reddit, moderating can be a very time consuming effort. (Nate spoke to a Reddit mod who had stopped volunteering at a children’s hospital in order to be a mod because she thought she could do more good that way.) This subreddit’s mods wanted to know if they could question the legitimacy of an item without causing it to surge on the platform. Fact-checking a post could nudge Reddit’s AI to boost its presence because of the increased activity.

So, they did an experiment asking people to fact check an article, or fact check and downvote if you can’t verify it. They monitored the ranking of the articles by Reddit for 3 months. [Nate now gives some math. Sorry I can’t capture (or understand) it.] The result: to his surprise, “encouraging fact checking reduced the average rank position of an article”encouraging fact checking reduced the average rank position of an article. Encouraging fact checking and down-voting reduced the spread of inaccurate news by Reddit’s algorithms. [I’m not confident I’m getting that right

Why did encouraging fact checking reduce rankings, but fact checking and voting did not? The mods think this might be because it gave users a constructive way to handle articles from reviled sources, reducing the number of negative comments about them. [I hope I’m getting this right.] Also, “reactance” may have nudged people to upvote just to spite the instructions. Also, users may have mobilized friends to vote on the artciles. Also, encouraging two tasks (fact check and then vote) rather than one may have influenced he timing of the algorithm, making the down-votes less impactful.

This is what Nate calls an “AI-Nudge”: a “second-order effect of influencing human behavior on the behavior of an algorithmic system.” It means you have to think about how humans interact with AI.

Often when people are working on AI, they’re starting from computer science and math. The question is: how can we use social science methods to research the effect of AI? Paluck and Cialdini see a cycle of Pilot/Lab experiments > qualitative methods > field experiences > theory / policy / design. In the Reddit example, Nathan spent considerable time with the community to understand their issues and how they interact with the AI.

Another example of a study: identifying and reducing side-effects of automated copyright law enforcement on Twitter. When people post something to Twitter, bots monitor it to see if violates copyright, resulting in a DMCA takedown notice being issued. Twitter then takes it down. The Lumen Project from BKC archives these notices. The CivilService project observes those notices in real time to study the effects. E.g., “a user’s tweets per day tends to drop after they receive a takedown notice … for a 42-day period”a user’s tweets per day tends to drop after they receive a takedown notice, and then continues dropping throughout the 42-day period they researched. Why this long-term decrease in posting? Maybe fear and risk. Maybe awareness of surveillance.

So, how can these chilling effects be reduced? The CivilService project automatically sends users info about their rights and about surveillance. The results of this intervention are not in yet. The project hopes to find ways to lessen the public’s needless withdrawal from social media. The research can feed empirical legal studies. Policymakers might find it useful. Civil rights orgs as well. And the platforms themselves.

In the course of the Q&As, Nathan mentions that he’s working on ways to explain social science research that non-experts can understand. CivilService’s work is with user communities and it’s developed a set of ways for communicating openly with the users.

Q: You’re trying to make AI more fair…

A: I’m doing consumer protection, so as experts like you work on making AI more fair, we can see the social effects of interventions. But there are feedback loops among them.

Q: What would you do with a community that doesn’t want to change?

A: We work with communities that want our help. In the 1970s, Campbell wrote an essay: “The Experimenting Society.” He asked if by doing behavioral research we’re becoming an authoritarian society because we’re putting power in the hands of the people who can afford to do the research. He proposed enabling communities to do their own studies and research. He proposed putting data scientists into towns across the US, pool their research, and challenge their findings. But this was before the PC. Now it’s far more feasible.

Q: What sort of pushback have you gotten from communities?

A: Some decide not to work with us. In others, there’s contention about the shape of the project. Platforms have changed how they view this work. Three years ago, the platforms felt under siege and wounded. That’s why I decided to create an independent organization. The platforms have a strong incentive to protect their reputations.
