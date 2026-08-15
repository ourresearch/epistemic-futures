---
title: "What Developers Actually Need to Know Right Now"
person: tim-oreilly
section: by
type: blog-post
year: 2026
date: 2026-02-19
venue: "O'Reilly Radar"
authors: "Tim O'Reilly"
source_url: https://www.oreilly.com/radar/what-developers-actually-need-to-know-right-now/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the oreilly.com/radar WordPress REST API (people_taxonomy=tim-oreilly); HTML converted to markdown."
---

# What Developers Actually Need to Know Right Now

## Full text

> _The following article includes clips from a recent_ Live with Tim O’Reilly _interview. You can watch[the full version](<https://learning.oreilly.com/videos/live-with-tim/0642572305529/>) on the O’Reilly Media learning platform._

[Addy Osmani](<https://addyosmani.com/>) is one of my favorite people to talk with about the state of software engineering with AI. He spent 14 years leading Chrome’s developer experience team at Google, and recently moved to Google Cloud AI to focus on Gemini and agent development. He’s also the author of numerous books for O’Reilly, including [_The Effective Software Engineer_](<https://learning.oreilly.com/library/view/the-effective-software/9798341638167/>) (due out in March), and my cohost for [O’Reilly’s AI Codecon](<https://www.oreilly.com/AI-Codecon/>). Every time I talk with him I come away feeling like I have a better grip on what’s real and what’s noise. Our [recent conversation on _Live with Tim O ’Reilly_](<https://www.oreilly.com/live/live-with-tim/>) was no exception.

Here are some of the things we talked about.

## ****The hard problem is coordination, not generation****

Addy pointed out that there’s a spectrum in how people are working with AI agents right now. On one end you have solo founders running hundreds or thousands of agents, sometimes without even reviewing the code. On the other end you have enterprise teams with quality gates, reliability requirements, and long-term maintenance to think about.

Addy’s take is that for most businesses, “the real frontier is not necessarily having hundreds of agents for a task just for its own sake. It’s about orchestrating a modest set of agents that solve real problems while maintaining control and traceability.” He pointed out that frameworks like Google’s [Agent Development Kit](<https://docs.cloud.google.com/agent-builder/agent-development-kit/overview>) now support both deterministic workflow agents and dynamic LLM agents in the same system, so you get to choose when you need predictability and when you need flexibility.

The ecosystem is developing fast. [A2A](<https://github.com/google/A2A>) (the agent-to-agent protocol Google contributed to the Linux Foundation) handles agent-to-agent communication while MCP handles agent-to-tool calls. Together they start to look like the TCP/IP of the agent era. But Addy was clear-eyed about where things stand: “Almost nobody’s figured out how to make everything work together as smoothly as possible. We’re getting as close to that as we can. And that’s the actual hard problem here. Not generation, but coordination.”

## ****The “Something Big Is Happening” debate****

In response to one of the audience questions, we spent some time on [Matt Shumer’s viral essay](<https://shumer.dev/something-big-is-happening>) arguing that the current moment in AI is like just before the COVID-19 epidemic hit. Those in the know were sounding the alarm, but most people weren’t hearing it.

Addy’s take was that “it felt a little bit like somebody who hadn’t been following along, just finally getting around to trying out the latest models and tools and having an epiphany moment.” He thinks the piece lacked grounding in data and didn’t do a great job distinguishing between what AI can do for prototypes and what it can do in production. As Addy put it, “Yes, the models are getting better, the harnesses are getting better, the tools are getting better. I can do more with AI these days than I could a year ago. All of that is true. But to say that all kinds of technical work can now be done with near perfection, I wouldn’t personally agree with that statement.”

I agree with Addy, but I also know how it feels when you see the future crashing in and no one is paying attention. At O’Reilly, we started working with the web when there were only 200 websites. In 1993, we built [GNN](<https://en.wikipedia.org/wiki/Global_Network_Navigator>), the first web portal, and the web’s first advertising. In 1994, we did the first large-scale market research on the potential of advertising as the web’s future business model. We went around lobbying phone companies to adopt the web and (a few years later) for bookstores to pay attention to the rise of Amazon, and nobody listened. I’m a big believer in “something is happening” moments. But I’m also very aware that it always takes longer than it appears.

Both things can be true. The direction and magnitude of this shift are real. The models keep getting better. The harnesses keep getting better. But we still have to figure out new kinds of businesses and new kinds of workflows. AI won’t be a tsunami that wipes everything away overnight.

> _Addy and I will be cohosting the_[ _O ’Reilly AI Codecon: Software Craftsmanship in the Age of AI_](<https://www.oreilly.com/AI-Codecon/>) _on March 26, where we ’ll go much deeper on orchestration, agent coordination, and the new skills developers need. We’d love to see you there._ [_Sign up for free here_](<https://www.oreilly.com/AI-Codecon/>) _._
> 
> _And if you’re interested in presenting at AI Codecon, our CFP is open through this Friday, February 20. Check out what we’re looking for and_[ _submit your proposal here_](<https://www.oreilly.com/AI-Codecon/cfp.html>) _._

## ****Feeling productive vs. being productive****

There was a great line from a post by Will Manidis called “[Tool Shaped Objects](<https://minutes.substack.com/p/tool-shaped-objects>)” that I shared during our conversation: “The market for feeling productive is orders of magnitude larger than the market for being productive.” The essay is about things that feel amazing to build and use but aren’t necessarily doing the work that needs to be done.

Addy picked up on this immediately. “There is a difference between feeling busy and being productive,” he said. “You can have 100 agents working in the background and feel like you’re being productive. And then someone asks, What did you get built? How much money is it making you?”

This isn’t to dismiss anyone who’s genuinely productive running lots of agents. Some people are. But a healthy skepticism about your own productivity is worth maintaining, especially when the tools make it so easy to feel like you’re moving fast.

## **Planning is the new coding**

Addy talked about how the balance of his time on a task has shifted significantly. “I might spend 30, 40% of the time a task takes just to actually write out what exactly is it that I want,” he said. What are the constraints? What are the success criteria? What’s the architecture? What libraries and UI components should be used?

All of that work to get clarity before you start code generation leads to much-higher-quality outcomes from AI. As Addy put it, “LLMs are very good at grounding things in the lowest common denominator. If there are patterns in the training data that are popular, they’re going to use those unless you tell them otherwise.” If your team has established best practices, codify them in Markdown files or MCP tools so the agent can use them.

I connected the planning phase to something larger about taste. Think about Steve Jobs. He wasn’t a coder. He was a master of knowing what good looked like and driving those who worked with him to achieve it. In this new world, that skill matters enormously. You’re going to be like Jobs telling his engineers “no, no, not that” and giving them a vision of what’s beautiful and powerful. Except now some of those engineers are agents. So management skill, communication skill, and taste are becoming core technical competencies.

## **Code review is getting harder**

One thing Addy flagged that doesn’t get enough attention: “Increasingly teams feel like they’re being thrashed with all of these PRs that are AI generated. People don’t necessarily understand everything that’s in there. And you have to balance increased velocity expectations with ‘What is a quality bar?’ because someone’s going to have to maintain this.”

Knowing your quality bar matters. What are the cases where you’re comfortable merging an AI-generated change? Maybe it’s small and well-compartmentalized and has solid test coverage. And what are the cases where you absolutely need deep human review? Getting clear on that distinction is one of the most practical things a team can do right now.

## **Yes, young people should still go into software**

We got a question about whether students should still pursue software engineering. Addy’s answer was emphatic: “There has never been a better time to get into software engineering if you are someone that is comfortable with learning. You do not necessarily have the burden of decades of knowing how things have historically been built. You can approach this with a very fresh set of eyes.” New entrants can go agent first. They can get deep into orchestration patterns and model trade-offs without having to unlearn old habits. And that’s a real advantage when interviewing at companies that need people who already know how to work this way.

The more important point is that in the early days of a new technology, people basically try to make the old things over again. The really big opportunities come when we figure out what was previously impossible that we can now do. If AI is as powerful as it appears to be, the opportunity isn’t to make companies more efficient at the same old work. It’s to solve entirely new problems and build entirely new kinds of products.

I’m 71 years old and 45 years into this industry, and this is the most excited I’ve ever been. More than the early web, more than open source. The future is being reinvented, and the people who start using these tools now get to be part of inventing it.

## **The token cost question**

Addy had a funny and honest admission: “There were weeks when I would look at my bill for how much I was using in tokens and just be shocked. I don’t know that the productivity gains were actually worthwhile.”

His advice: experiment. Get a sense of what your typical tasks cost with multiple agents. Extrapolate. Ask yourself whether you’d still find it valuable at that price. Some people spend hundreds or even thousands a month on tokens and feel it’s worthwhile because the alternative was hiring a contractor. Others are spending that much and mostly feeling busy. As Addy said, “Don’t feel like you have to be spending a huge amount of money to not miss out on productivity wins.”

I’d add that we’re in a period where these costs are massively subsidized. The model companies are covering inference costs to get you locked in. Take advantage of that while it lasts. But also recognize that a lot of efficiency work is yet to be done. Just as JavaScript frameworks replaced everyone hand-coding UIs, we’ll get frameworks and tools that make agent workflows much more token-efficient than they are today.

## **2028 predictions are already here**

One of the most striking things Addy shared was that a group in the AI coding community that he is part of had put together predictions for what software engineering would look like by 2028. “We recently revisited that list, and I was kind of shocked to discover that almost everything on that list is already possible today,” he said. “But how quickly the rest of the ecosystem adopts these things is on a longer trajectory than what is possible.”

That gap between capability and adoption is where most of the interesting work will happen over the next few years. The technology is running ahead of our ability to absorb it. Figuring out how to close that gap, in your team, your company, and your own practice, is the real job right now.

## **Agents writing code for agents**

Near the end we answered another great audience question: Will agents eventually produce source code that’s optimized for other agents to read, not humans? Addy said yes. There are already platform teams having conversations about whether to build for an agent-first world where human readability becomes a secondary concern.

I have a historical parallel for this. I wrote the manual for the first C compiler on the Mac, and I worked closely with the developer who was hand-tuning the compiler output at the machine code level. That was about 30 years ago. We stopped doing that. And I’m quite confident there will be a similar moment with AI-generated code where humans mostly just let it go and trust the output. There will be special cases where people dive in for absolute performance or correctness. But they’ll be rare.

That transition won’t happen overnight. But the direction seems pretty clear. You can help to invent the future now, or spend time later trying to catch up with those who do.

* * *

__This conversation was part of my ongoing series of discussions with innovators,_ _[Live with Tim O’Reilly](<https://www.oreilly.com/live/live-with-tim/>) __. You can explore past episodes[on the O’Reilly learning platform](<https://learning.oreilly.com/playlists/536ae66a-50ad-4ebe-9771-ac87d984542b/>).__
