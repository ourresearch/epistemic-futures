---
title: "Everyone’s an Engineer Now"
person: tim-oreilly
section: by
type: blog-post
year: 2026
date: 2026-04-30
venue: "O'Reilly Radar"
authors: "Tim O'Reilly"
source_url: https://www.oreilly.com/radar/everyones-an-engineer-now/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the oreilly.com/radar WordPress REST API (people_taxonomy=tim-oreilly); HTML converted to markdown."
---

# Everyone’s an Engineer Now

## Full text

Cat Wu leads product for Claude Code and Cowork at Anthropic, so she’s well-versed in building reliable, interpretable, and steerable AI systems. And since 90% of Anthropic’s code is now written by Claude Code, she’s also deeply familiar with fitting them into routine day-to-day work. Last month, Cat joined Addy Osmani at [AI Codecon](<https://www.oreilly.com/AI-Codecon/>) for a fireside chat on the future of agentic coding and, equally important, agentic code review, how Anthropic actually uses the tools they’re building, and what skills matter now for developers.

## The feedback loop is itself a product

Boris Cherny initially built Claude Code as a side project to test Anthropic’s APIs. Then he shared the tool in a notebook, and within two months the entire company was using it. That organic growth, Cat said, was part of what convinced the team it was worth releasing externally.

But what really made that internal adoption visible was the response on Anthropic’s internal “dog-fooding” Slack channel. The Claude Code channel gets a new message every 5 to 10 minutes around the clock, and this feedback directly and immediately informs the product experience. Cat described it this way:

> We hire for people who love polishing the user experience. And so a lot of our engineers actually live in this channel and find when there’s issues with new features that they’ve worked on and they proactively lay out the fixes.

The team ships new versions of Claude Code to internal users many times a day. The feedback loop is tight enough that it functions as a continuous integration system for product quality, not just code quality.

Cat told Addy how she once accidentally introduced a small interaction bug between prompts and auto-suggestions. But by the time she started working on a solution, she found another team member had already beaten her to it. It turns out, he had set up a scheduled task in Claude Code to scan the feedback channel for anything that hadn’t been responded to in 24 hours and open a PR for it. Since Cat hadn’t gotten to it yet (whoops!), her teammate’s Claude saw the unaddressed issue and fixed it for her. And Cat only found out when “[her own] Claude noticed that his Claude had already landed a change.”   

The infrastructure for rapid improvement, in other words, is now partly automated. The agents are writing the code, then monitoring the feedback and closing the loop.

## The bottleneck has shifted to review

There’s no question that AI-assisted coding has created a boom in output. Anthropic engineers are producing roughly 200% more code than they were a year ago, Cat noted. Today the main constraint is reviewing all that code to ensure it’s production-ready.

Cat’s team concluded that you can buy a lot of additional robustness for not that much extra cost. 

> We opted for the heaviest, most robust version [of code review]. We actually plot how many agents and how comprehensive of a review Claude does and then how many bugs does it recall. And we picked a number of very high recall and decided we should ship this, because if you really want AI code review to be a load-bearing part of your process, you actually probably just want the most comprehensive possible review.

The review agent doesn’t just look at the diff. It traces code across multiple files and catches bugs in adjacent code that has nothing to do with the change in question. Cat gave two examples. One was a ZFS encryption refactor where the agent found a key cache invalidation bug that wasn’t related to the author’s change at all but would have invalidated it. The other was a routine auth update that turned out to have a bad side effect, caught premerge. In both cases, engineers manually reviewing the code likely would have missed the bugs.

The human review that remains is deliberately small in scope. For most PRs, the human reviewer skims for design principle violations and obvious problems and assumes functional correctness has been handled. Five to ten agents run in parallel, each given slightly different tasks, returning independently and then deduplicating what they found.

The cultural shift that made this work, though, was ownership. The team moved to a model where the engineer who authors a PR owns it end to end, including postdeploy bugs, and doesn’t lean on peer reviewers to catch mistakes. “Otherwise,” as Cat pointed out, “you have situations where junior engineers put out a bunch of PRs and then your senior engineers are like drowning in AI-generated stuff where they’re not sure how thoroughly it’s been tested.”

Full ownership meant the AI review had to actually be trustworthy, which drove the decision to go for high recall rather than a lighter touch. That said, engineers are still expected to understand every line of code an agent creates. . .for now. As Cat explained, it’s the only way to truly prevent “unknown security vulnerabilities and to be able to quickly respond to incidents if they are to happen.” 

## Everyone’s kind of an engineer now

Cowork, Anthropic’s agent tool for nontechnical users, is the company’s attempt to take what Claude Code does for engineers and bring it to knowledge work more broadly. Cat sketched a picture of someone looking at five or six agent tasks running simultaneously in a side panel, managing a fleet of agents the way a senior engineer manages a PR queue.

In the nearer-term, she’s keeping tabs on the shift toward people using Claude Code to build things for themselves, their teams, or their families that wouldn’t have justified professional development effort or “otherwise been possible.” The prototype is the garage project, the family expense tracker, the tool that a small team actually needs but that no SaaS product quite addresses. Cat’s goal and hope is that Claude Code helps people “solve their own problems for themselves” and “stewards a new future of personal software.”

## Product taste as the new technical skill

More people building more software is unambiguously good. Boris Cherny has even floated the idea that coding as we know it is “[solved](<https://x.com/lennysan/status/2024896611818897438>).” But what does that mean for the craft of software engineering? Cat’s read of the current moment is more nuanced:

> I think pre-AI, the skills that were very important were being able to take a spec and implement it well. And I think now the really important skill is product taste. Even for engineers. Can you use code to ingest a massive amount of user feedback? Do you have good intuition about which feature to build to address those needs, because it’s often different than exactly what users are asking you for? And then, when Claude builds it, are you setting up the right bar so that what you ship people actually love?

Cat’s not alone in highlighting the importance of taste in a world where code is a commodity. [Steve Yegge](<https://www.oreilly.com/radar/steve-yegge-wants-you-to-stop-looking-at-your-code/#:~:text=the%20new%20Amish.%E2%80%9D-,Taste%20is%20the%20moat,-Another%20of%20the>), [Wes McKinney](<https://www.oreilly.com/radar/the-mythical-agent-month/#:~:text=Design%20and%20taste%20as%20our%20last%20foothold>), and many others, [myself included](<https://www.oreilly.com/radar/betting-against-the-bitter-lesson/#:~:text=Even%20if%20the,taste%20and%20curation>), see taste and judgment as a uniquely human value. This has practical implications for how engineers should spend their time now, and for what the next generation needs to learn.   

For junior engineers specifically, Cat described a progression: Start by using Claude Code to understand the codebase (ask all the “dumb questions” without embarrassment), take those answers to a senior engineer for calibration, and then close the loop by updating the CLAUDE.md with whatever was missing.

> Think of Claude Code as your intern that you’re trying to level up. Like, teach it back to Claude. Add a `/verify` slash command. Put it in the CLAUDE.md or the agent README. Approach this as senior engineers helping you level up, and then you helping Claude and other agents level up.

The improvement process, in other words, should be bidirectional. Engineers get better at using the tools and the tools get better through the engineers’ accumulated knowledge. And significantly, this process keeps humans firmly in the loop, playing a role that’s “[active, continuous, and skilled](<https://www.oreilly.com/radar/software-craftsmanship-in-the-age-of-ai/>).”

> _You can[watch Cat and Addy’s full chat](<https://learning.oreilly.com/videos/ai-codecon-software/0642572305581/>), plus everything else from AI Codecon on the O’Reilly learning platform. Not a member? [Sign up for a free 10-day trial](<https://www.oreilly.com/start-trial/?type=individual>), no strings attached. _
