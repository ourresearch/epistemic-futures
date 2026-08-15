---
title: "[liveblog] AI Advance opening: Jonathan Zittrain and lightning talks"
person: david-weinberger
section: by
type: blog-post
year: 2017
date: 2017-05-15
venue: "Joho the Blog (hyperorg.com)"
authors: "David Weinberger"
source_url: https://hyperorg.com/2017/05/15/liveblog-ai-advance-opening-jonathan-zittrain-and-lightning-talks/
retrieved: 2026-08-13
content: full-text
notes: "Post from Joho the Blog (hyperorg.com), Weinberger's personal blog. Retrieved via the site's WordPress REST API; HTML converted to plain text. Live-blogged notes taken during another speaker's talk or panel — the summarized content is the speaker's, the framing and commentary are Weinberger's."
---

# [liveblog] AI Advance opening: Jonathan Zittrain and lightning talks

## Full text

I’m at a day-long conference/meet-up put on by the Berkman Klein Center‘s and MIT Media Lab‘s “AI for the Common Good” project.

NOTE: Live-blogging. Getting things wrong. Missing points. Omitting key information. Introducing artificial choppiness. Over-emphasizing small matters. Paraphrasing badly. Not running a spellpchecker. Mangling other people’s ideas and words. You are warned, people.

Jonathan Zittrain gives an opening talk. Since we’re meeting at Harvard Law, JZ begins by recalling the origins of what has been called “cyber law,” which has roots here. Back then, the lawyers got to the topic first, and thought that they could just think their way to policy. We are now at another signal moment as we are in a frenzy of building new tech. This time we want instead to involve more groups and think this through. [I am wildly paraphrasing.]

JZ asks: What is it that we intuitively love about human judgment, and are we willing to insist on human judgments that are worse than what a machine would come up with? Suppose for utilitarian reasons we can cede autonomy to our machines — e.g., autonomous cars — shouldn’t we? And what do we do about maintaining local norms? E.g., “You are now entering Texas where your autonomous car will not brake for pedestrians.”

“Should I insist on being misjudged by a human judge because that’s somehow artesinal?” when, ex hypothesis, an AI system might be fairer.

Autonomous systems are not entirely new. They’re bringing to the fore questions that have always been with us. E.g., we grant a sense of discrete intelligence to corporations. E.g., “McDonald’s is upset and may want to sue someone.”

[This is a particularly bad representation of JZ’s talk. Not only is it wildly incomplete, but it misses the through-line and JZ’s wit. Sorry.]

Lightning Talks

Finale Doshi-Velez is particularly interested in interpretable machine learning (ML) models. E.g., suppose you have ten different classifiers that give equally predictive results. Should you provide the most understandable, all of them…?

Why is interpretability so “in vogue”? Suppose non-interpretable AI can do something better? In most cases we don’t know what “better” means. E.g., someone might want to control her glucose level, but perhaps also to control her weight, or other outcomes? Human physicians can still see things that are not coded into the model, and that will be the case for a long time. Also, we want systems that are fair. This means we want interpretable AI systems.

How do we formalize these notions of interpretability? How do we do so for science and beyond? E.g., what is a legal “right to explanation

” mean? She is working with Sam Greshman on how to more formally ground AI interpretability in the cognitive science of explanation.

Vikash Mansinghka leads the eight-person Probabilistic Computing project at MIT. They want to build computing systems that can be our partners, not our replacements. We have assumed that the measure of success of AI is that it beats us at our own game, e.g., AlphaGo, Deep Blue, Watson playing Jeopardy! But games have clearly measurable winners.

His lab is working on augmented intelligence that gives partial solutions, guidelines and hints that help us solve problems that neither system could solve on their own. The need for these systems are most obvious in large-scale human interest projects, e.g., epidemiology, economics, etc. E.g., should a successful nutrition program in SE Asia be tested in Africa too? There are many variables (including cost). BayesDB, developed by his lab, is “augmented intelligence for public interest data science.”

Traditional computer science, computing systems are built up from circuits to algorithms. Engineers can trade off performance for interpretability. Probabilisitic systems have some of the same considerations. [Sorry, I didn’t get that last point. My fault!]

John Palfrey is a former Exec. Dir. of BKC, chair of the Knight Foundation (a funder of this project) and many other things. Where can we, BKC and the Media Lab, be most effective as a research organization? First, we’ve had the most success when we merge theory and practice. And building things. And communicating. Second, we have not yet defined the research question sufficiently. “We’re close to something that clearly relates to AI, ethics and government” but we don’t yet have the well-defined research questions.

The Knight Foundation thinks this area is a big deal. AI could be a tool for the public good, but it also might not be. “We’re queasy” about it, as well as excited.

Nadya Peek is at the Media Lab and has been researching “macines that make machines.” She points to the first computer-controlled machine (“Teaching Power Tools to Run Themselves“) where the aim was precision. People controlled these CCMs: programmers, CAD/CAM folks, etc. That’s still the case but it looks different. Now the old jobs are being done by far fewer people. But the spaces between doesn’t always work so well. E.g., Apple can define an automatiable workflow for milling components, but if you’re student doing a one-off project, it can be very difficult to get all the integrations right. The student doesn’t much care about a repeatable workflow.

Who has access to an Apple-like infrastructure? How can we make precision-based one-offs easier to create? (She teaches a course at MIT called “How to create a machine that can create almost anything.”)

Nathan Mathias, MIT grad student with a newly-minted Ph.D. (congrats, Nathan!), and BKC community member, is facilitating the discussion. He asks how we conceptualize the range of questions that these talks have raised. And, what are the tools we need to create? What are the social processes behind that? How can we communicate what we want to machines and understand what they “think” they’re doing? Who can do what, where that raises questions about literacy, policy, and legal issues? Finally, how can we get to the questions we need to ask, how to answer them, and how to organize people, institutions, and automated systems? Scholarly inquiry, organizing people socially and politically, creating policies, etc.? How do we get there? How can we build AI systems that are “generative” in JZ’s sense: systems that we can all contribute to on relatively equal terms and share them with others.

Nathan: Vikash, what do you do when people disagree?

Vikash: When you include the sources, you can provide probabilistic responses.

Finale: When a system can’t provide a single answer, it ought to provide multiple answers. We need humans to give systems clear values. AI things are not moral, ethical things. That’s us.

Vikash: We’ve made great strides in systems that can deal with what may or may not be true, but not in terms of preference.

Nathan: An audience member wants to know what we have to do to prevent AI from repeating human bias.

Nadya: We need to include the people affected in the conversations about these systems. There are assumptions about the independence of values that just aren’t true.

Nathan: How can people not close to these systems be heard?

JP: Ethan Zuckerman, can you respond?

Ethan: One of my colleagues, Joy Buolamwini, is working on what she calls the Algorithmic Justice League, looking at computer vision algorithms that don’t work on people of color. In part this is because the tests use to train cv systems are 70% white male faces. So she’s generating new sets of facial data that we can retest on. Overall, it’d be good to use test data that represents the real world, and to make sure a representation of humanity is working on these systems. So here’s my question: We find co-design works well: bringing in the affected populations to talk with the system designers?

[Damn, I missed Yochai Benkler‘s comment.]

Finale: We should also enable people to interrogate AI when the results seem questionable or unfair. We need to be thinking about the proccesses for resolving such questions.

Nadya: It’s never “people” in general who are affected. It’s always particular people with agendas, from places and institutions, etc.
