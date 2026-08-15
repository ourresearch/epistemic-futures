---
title: "Ryan Carson Is a One-Person Code Factory"
person: tim-oreilly
section: by
type: blog-post
year: 2026
date: 2026-05-13
venue: "O'Reilly Radar"
authors: "Tim O'Reilly"
source_url: https://www.oreilly.com/radar/ryan-carson-is-a-one-person-code-factory/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the oreilly.com/radar WordPress REST API (people_taxonomy=tim-oreilly); HTML converted to markdown."
---

# Ryan Carson Is a One-Person Code Factory

## Full text

Ryan Carson has built companies for 25 years, including Treehouse, which taught over a million people to code. He knows what it takes to grow a team. So when he told me he’d raised $2 million in seed funding for his latest company, Untangle, an AI-powered divorce assistant, and had no plans to hire anyone, I wanted to understand what that actually looks like.

Ryan stopped writing code professionally around 2008. He’d essentially been “abstracted away” from it by the responsibilities of running a funded startup, as he put it. Following the acquisition of Treehouse and inspired by the arrival of large language models, he decided to teach himself to code again with ChatGPT. Ryan learned Next.js, a framework he’d never touched, using AI as a tutor that was wrong often enough to keep him honest but patient enough that he could go as slowly as he needed.

He shipped something. It didn’t work commercially, so he moved on, but he still learned a lot about iterating on AI products in the process. A few years later, when he had an idea for a divorce tool born out of watching his family members struggle through difficult splits, he was ready to build a real MVP, and he did it all by himself (with a little design help along the way).

As one of the foremost proponents of companies led by a single founder running a team of agents, in some sense, Ryan is a prince from another country. Maybe it’s not immediately apparent how his current workflow is relevant to developers working for big corporations beyond efficiency gains with AI-assisted coding. But thinking bigger picture, what Ryan calls the “[code factory](<https://x.com/ryancarson/status/2023452909883609111>)”—a system where agents write and review the code, run the tests, triage the error reports, and monitor the production environment, under his oversight—may be an early version of what a lot more organizations will look like in five years.

## The loop is the thing

What makes the code factory model possible, Ryan explained, is the ability to set up automations and skills for jobs that you know that you need to be doing every day. In other words, you’re teaching an agent to do a repeatable process. The underlying pattern is the iterative loop, and Ryan was an early [proponent and popularizer](<https://github.com/snarktank/ralph>) of Geoffrey Huntley’s “[Ralph Wiggum](<https://ghuntley.com/ralph/>)” approach.

The name comes from a _Simpsons_ character who is, to put it charitably, not the sharpest. The idea is that you don’t need the agent to be superintelligent. You need it to do one thing, write down what it did and what it learned, stop, and restart with that notebook in hand. As Ryan pointed out, it turns out that pretty good intelligence, a loop, some instructions, and a notebook gets you surprisingly far into complex territory. Or to use another of Ryan’s analogies:

> Think of it as a notebook where it’s like, “Here are the things I’ve done. And here’s the holes I fell into.” It’s like _Memento_ , the movie, where [the main character] tattoos himself or uses notes to remember, like, “What did I do yesterday and what did I learn?” And agents are the same. They don’t have any long-term memory. And so [Geoffrey Huntley] figured out, yeah, this loop actually works shockingly well. It’s very primitive, this idea. And eventually after a number of these iterations, you actually get pretty complex outcomes.

When I heard this I thought of my first exposure to shell programming and how I fell in love with loops. You have a repetitive task and you want to do it many times, and computers are good at that. The language has changed, though; it’s English now instead of Bash. But the logic hasn’t: do something; save the result; do it again.

The [skill](<https://www.oreilly.com/radar/what-mcp-and-claude-skills-teach-us-about-open-source-for-ai/>) I use to generate first drafts of posts like this reads the transcript, summarizes it, and suggests possible video clips to extract. I built it with a different sort of loop, iteratively training Claude to write more like me by rewriting its drafts, asking it to analyze the differences, and then feeding back the differences as a SKILL.md file, repeating until the gap narrowed enough to reduce the amount of time it takes to accurately reflect my own takeaways.

Ryan brought up an important point: skills decay. A Next.js skill from six months ago may conflict with your current component library. Two skills may say opposite things. He told me he’d gladly pay for a system that audits his skills library, flags conflicts, and surfaces what’s gone stale. Anyone can write a skill that’s useful in the moment. The value is in keeping the skill current and coherent as it interacts with the code factory’s complete workflow.

## The code factory in practice

I asked Ryan to show us his daily workflow to give us a peek into the code factory. He shared a screen with 15 active threads running in Devin (at a monthly token burn of $2,000–$3,000). As Ryan explained, having a tool like Devin is the key to the code factory model. He’d started by “hand-cobbling” together a system with a Ralph Wiggum loop and a skill, but it was fragile and things broke or got out of sync. He needed a more durable system to run the cron jobs and nightly automations that keep the factory humming. He picked Devin, but ultimately choosing a direction was more important than the choice itself:

> If you back up and say, How is the modern code factory happening? It’s choosing a tool that allows you to have automations and skills for jobs that you know that you need to be doing every day.

And he’s since expanded that toolset to cover product requirements beyond software engineering, like design.

## What you can automate, and what you can’t

One of the threads Ryan had open was an end-to-end smoke test that signs up for his own app every morning, runs through the full onboarding flow, exercises all 14 tools, and records a video of itself doing it. Every morning he wakes up to a report. The test passed or it didn’t, and if it didn’t, here’s what failed. He has a separate Devin automation that reads [Sentry](<https://sentry.io/>) every morning, and if it finds something problematic, spins up another Devin to fix it.

This is what a CTO does: reads the Datadog and Sentry reports, triages what matters, and points the team at it. Ryan has automated the reading and the triaging. He still decides what to do about the things that matter, but the number of things he has to pay attention to has been compressed dramatically.

Ryan’s figured out how to automate many of the responsibilities he hired for in his previous companies. Another automation runs against his Google Ads, Meta, and X spend, compiles a performance report on cost per click, lead generation, click-through rate. He reads that the way a head of marketing would read it.

There’s one thing he hasn’t been able to automate: what he should build. As we hear [again](<https://www.oreilly.com/radar/everyones-an-engineer-now/#:~:text=Product%20taste%20as%20the%20new%20technical%20skill>) and [again](<https://www.oreilly.com/radar/the-mythical-agent-month/#:~:text=Design%20and%20taste%20as%20our%20last%20foothold>), the efficiency gains in coding, testing, design iteration, and monitoring don’t replace the judgment calls about which problems matter. As Ryan noted, “There isn’t a magic wand still. You can build faster, but whether you’re building the right thing, and doing it better is something [else].”

## Programming isn’t going away

We all need to keep pushing back on the narrative that programming is going away. When I started, I wrote assembly language programs. I was literally moving data from registers, multiplying values, low-level operations that nobody does manually anymore because the compiler handles it all. When we look back on that, we don’t think “programmers became unnecessary.” We understand that programming was just abstracted to a higher level, and became more powerful for it. That’s where we are again.

Ryan used the analogy of a carpenter switching from a handsaw to a Sawzall. It saves a ton of time, but you still need to know which pipes you’re cutting or you’re going to have a bad day. The domain knowledge doesn’t get abstracted away with the tool.

The people who are going to do well are the ones who bring genuine domain expertise to what they’re asking agents to do. Ryan knows divorce law well enough to evaluate whether the output is right. He knows enough about software to catch when the agent has gone off the rails. The agent amplifies what you already know; it can’t supply what you don’t.

## What happened when he pitched an attorney

Ryan’s company is built for people considering or going through a divorce who find the process too expensive and too hard. But he always expected attorneys to have opinions. As he put it, “Either they would hate us and see us as the grim reaper, or they would love us because we’re going to save them costs.” So he had his AI agent, whom he calls R2, find and book meetings with small family law firms to hear them out. The feedback was very positive (from lawyers at least; paralegals may have another opinion). Here’s how one legal business owner responded to his pitch:

> The truth is, I have a lot of overhead from folks that are more in the paralegal space. And it sounds like your tool will do all that work. And I would rather have attorneys on staff that are doing the real legal work and then have all the paralegal work done by AI. I would love to pay you for that.

I expect that’s where most of the near-term displacement happens. Lower-value overhead gets automated and professionals spend more of their hours on actual professional work.

Sometimes there’s an economic tradeoff between job losses (bad for those who lose their jobs) and lower costs that can be passed on to consumers. A lot of people who need legal help with a divorce can’t afford it, so they get stuck in a bad marriage. If the cost of the process comes down because the overhead is lower, some of those people get served who currently aren’t. There’s a big difference in economic impact between a business just saving costs and pocketing the savings and one that passes those savings along to consumers or uses them to radically improve access.

## AI’s supporting role

Late in our conversation, someone asked how you use AI to identify strategic opportunities. Ryan’s answer was practical: build a priority map of the projects and people that matter to you, then run a cron job every 15 minutes to triage your inbox and Slack through that map, surface what’s relevant, and act. Ryan calls it his AI chief of staff, and he’s even open-sourced it as [Clawchief](<https://github.com/snarktank/clawchief>).

My framing is a little different, and it comes from a conversation I had years ago with [Jeff Jonas](<https://www.linkedin.com/in/jeff-jonas/>), who has done data work for national intelligence agencies and casino security systems. His dream was a system where the query lives in the same space as the data. Rather than going looking for things, you define what matters to you and the system watches for it. New data shows up and the query is already there, waiting. Jeff was talking about that long before agents were a concept, but it describes what a well-designed agent loop can do now.

Only you yourself will be able to fully understand the strategic opportunity moments for your company. What AI can do for you is be a scout. It can surface things that you should be paying better attention to. That’s what Jeff and Ryan are both talking about ([Steve Yegge too](<https://www.oreilly.com/radar/steve-yegge-wants-you-to-stop-looking-at-your-code/#:~:text=Everyone%20gets%20a%20chief%20of%20staff>)): an agent that watches the flow and surfaces what deserves your attention rather than one that tries to make decisions for you.

Right now, there’s this incredible opportunity to try things out and see what sticks. As Ryan has shown, it doesn’t take an entire company. Identify your goal and opportunity, then start building. His advice: Don’t worry about trying out every new tool. Just “find an energetic system,” then “pick a lane and invest.”
