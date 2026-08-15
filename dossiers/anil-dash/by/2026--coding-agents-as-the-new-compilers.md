---
title: "Coding agents as the new compilers"
person: anil-dash
section: by
type: blog-post
year: 2026
date: 2026-02-11
venue: "anildash.com"
authors: "Anil Dash"
source_url: https://anildash.com/2026/02/11/coding-agents-as-the-new-compilers/
retrieved: 2026-08-13
content: full-text
notes: "tags: coding, software, ai"
---

# Coding agents as the new compilers

## Full text

In each successive generation of code creation thus far, we’ve abstracted away the prior generation over time. Usually, only a small percentage of coders still work on the lower layers of the stack that used to be the space where everyone was working. I’ve been coding long enough that people were still creating code in assembly when I started (though I was never any good at it!), though I started with BASIC. Since BASIC was an interpreted language, its interpreter would write the assembly language for me, and I never had to see exactly what assembly language code was being created.

I definitely _did_ know old-school coders who used to, at first, check that assembly code to see if they liked the output. But eventually, over time, they just learned to trust the system and stopped looking at what happened after the system finished compiling. Even people using more “close to the metal” languages like C generally trust that their compilers have been optimized enough that they seldom inspect the output of the compiler to make sure it was perfectly optimized for their particular processor or configuration. The benefits of delegating those concerns to the teams that create compilers, and coding tools in general, yielded so many advantages that that tradeoff was easily worth it, once you got over the slightly uncomfortable feeling.

In the years that followed, though a small cohort of expert coders who would hand-tune assembly code for things like getting the most extreme performance out of a gaming console, most folks stopped writing it, and very few _new_ coders learned assembly at all. The vast majority of working coders treat the output from the compiler layer as a black box, trusting the tools to do the right thing and delegating the concerns below that to the toolmakers.

We may be seeing that pattern repeat itself. Only this time, the abstraction is happening through AI tools abstracting away _all_ the code. Which can feel a little scary.

## Squashing the stack

Just as interpreted languages took away chores like memory management, and high-level languages took away the tedium of writing assembly code, we’re starting to see the first wave of tools that completely abstract away the writing of code. (I described this in more detail in the piece about [codeless software](<https://www.anildash.com/2026/01/22/codeless/>)recently.

The individual practice of professionalizing the writing of software with LLMs seems to have settled on the term “[agentic engineering](<https://simonwillison.net/2026/Feb/11/glm-5/>)”, as Simon Willison recently noted.

But the next step beyond that is when teams _don’t_ write any of the code themselves, instead moving to an entirely abstracted way of creating code. In this model, teams (or even individual coders):

  * Define the specifications for how the code should work
  * Ensure that the system is provided with enough context at all times that it can succeed in creating code that is successful as often as possible
  * Provide sufficient resources that a redundant and resilient set of code outputs can be created to accommodate failures while in iteration
  * Enforce execution of tests and conformance systems against the code — [including human tests with a named, accountable party](<https://simonwillison.net/2025/Dec/18/code-proven-to-work/>), not just automated software tests

With this kind of model deployed, the software that is created can essentially be output from the system in the way that assembly code or bytecode is output from compilers today, with no direct inspection from the people who are directing its creation. Another way of thinking about this is that we’re abstracting away many different specific programming languages and detailed syntaxes to more human-written Markdown files, created much of the time in **collaboration** with these LLM tools.

Presently, most people and teams who are pursuing this path are doing so with costly commercial LLMs. I would strongly advocate that most organizations, and _especially_ most professional coders, be very fluent in ways of accomplishing these tasks with a fleet of low-cost, locally-hosted, open source/open-weight models contributing to the workload. I don’t think they are performant enough yet to accomplish all of the coding tasks needed for a non-trivial application yet, but there are a significant number of sub-tasks that could reasonably be delegated. More importantly, it will be increasingly vital to ensure that this entire “codeless compilation” stack for agentic engineering works in a vendor-neutral way that can be decoupled from the major LLM vendors, as they get more irresponsible in their business practices and more aggressive towards today’s working coders and creators.

For many, those worries about Big AI are why their reaction to these developments in agentic coding make them want to recoil. But in reality, these issues are exactly why we desperately need to _engage_.

## Seizing the means

Many of the smartest coders I know have a lot of legitimate and understandable misgivings about the impact that LLMs are having on the coding world, especially as they’re often being evangelized by companies that plainly have ill intent towards working coders. It is reasonable, and even smart, to be skeptical of their motivations and incentives.

But the response to that skepticism is not to reject the category of technology, but rather to capture it and seize control over its direction, away from the Big AI companies. This shift to a new level of coding abstraction is exactly the kind of platform shift that presents that sort of opportunity. It’s potentially a chance for coders to be in control of some part of their destiny, at a time when a lot of bosses clearly want to [get rid of as many coders as they can](<https://www.anildash.com/2026/01/06/500k-tech-workers-laid-off/>).

At the very least, this is one area where the people who actually _make things_ are ahead of the big platforms that want to cash in on it.

## What if I think this is all bullshit?

I think a lot of coders are going to be understandably skeptical. The most common concern is, “I write really great code, how could it possibly be good news that we’re going to abstract away the writing of code?”. Or, “How the hell could a software factory be good news for people who make software?”

For that first question, the answer is going to involve some grieving, at first. It may be the case that writing really clean, elegant, idiomatic Python code is a skill that will be reduced in demand in the same way that writing incredibly performant, highly-tuned assembly code is. There _is_ a market for it, but it’s on the edges, in specific scenarios. People ask for it when they need it, but they don’t usually _start_ by saying they need it.

But for the deeper question, we may have a more hopeful answer. By elevating our focus up from the individual lines of code to the more ambitious focus on the overall problem we’re trying to solve, we may reconnect with the “why” that brought us to creating software and tech in the first place. We can raise our gaze from the steps right in front of us to the horizon a bit further ahead, and think more deeply about the problem we’re trying to solve. Or maybe even about the _people_ who we’re trying to solve that problem for.

I think people who create code today, if they have access to super-efficient code-creation tools, will make better and more thoughtful products than the financiers who are currently carrying out mass layoffs of the best and most thoughtful people in the tech industry.

I also know there’s a history of worker-owned factories being safer and more successful than others in their industries, while often making better, longer-lasting products and being better neighbors in their communities. Maybe it’s possible that there’s an internet where agentic engineering tools could enable smart creators to build their own software factories that could work the same way.
