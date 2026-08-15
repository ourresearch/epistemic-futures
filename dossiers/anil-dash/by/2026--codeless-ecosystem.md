---
title: "A Codeless Ecosystem, or hacking beyond vibe coding"
person: anil-dash
section: by
type: blog-post
year: 2026
date: 2026-01-27
venue: "anildash.com"
authors: "Anil Dash"
source_url: https://anildash.com/2026/01/27/codeless-ecosystem/
retrieved: 2026-08-13
content: full-text
notes: "tags: coding, software, ai"
---

# A Codeless Ecosystem, or hacking beyond vibe coding

## Full text

There's been a [remarkable leap forward](<https://www.anildash.com/2026/01/22/codeless/>) in the ability to orchestrate coding bots, making it possible for ordinary creators to command dozens of AI bots to build software without ever having to directly touch code. The implications of this kind of evolution are potentially extraordinary, as outlined in that first set of notes about what we could call "codeless" software. But now it's worth looking at the larger ecosystem to understand where all of this might be headed.

## "Frontier minus six"

One idea that's come up in a host of different conversations around codeless software, both from supporters and skeptics, is how these new orchestration tools can enable coders to control coding bots that _aren't_ from the Big AI companies. Skeptics say, "won't everyone just use Claude Code, since that's the best coding bot?"

The response that comes up is one that I keep articulating as "frontier minus six", meaning the idea that many of the open source or open-weight AI models are often delivering results at a level equivalent to where frontier AI models were six months ago. Or, sometimes, where they were 9 months or a year ago. In any of these cases, these are still damn good results! These levels of performance are not merely acceptable, they are results that we were amazed by just months ago, and are more than serviceable for a large number of use cases — especially if those use cases can be run locally, at low cost, with lower power usage, without having to pay any vendor, and in environments where one can inspect what's happening with security and privacy.

When we consider that a frontier-minus-six fleet of bots can often run on cheap commodity hardware (instead of the latest, most costly, hard-to-get Nvidia GPUs) and we still have the backup option of escalating workloads to the paid services if and when a task is too challenging for them to complete, it seems inevitable that this will be part of the mix in future codeless implementations.

## Agent patterns and design

The most thoughtful and fluent analysis of the new codeless approach has been [this wonderful essay by Maggie Appleton](<https://maggieappleton.com/gastown>), whose writing is always incisive and insightful. This one's a must-read! Speaking of Gas Town (Steve Yegge's signature orchestration tool, which has catalyzed much of the codeless revolution), Maggie captures the ethos of the entire space:

> We should take Yegge’s creation seriously not because it’s a serious, working tool for today’s developers (it isn’t). But because it’s a good piece of speculative design fiction that asks provocative questions and reveals the shape of constraints we’ll face as agentic coding systems mature and grow.

## Code and legacy

Once you've considered Maggie's piece, it's worth reading over Steve Krouse's essay, "[Vibe code is legacy code](<https://blog.val.town/vibe-code>)". Steve and his team build the delightful [val town](<https://www.val.town>), an incredibly accessible coding community that strikes a very careful balance between enabling coding and enabling AI assistance without overwriting the human, creative aspects of building with code. In many ways (including its aesthetic), it is the closest thing I've seen to a spiritual successor to the work we'd done for many years with [Glitch](<https://en.wikipedia.org/wiki/Glitch,_Inc.>), so it's no surprise that Steve would have a good intuition about the human relationship to creating with code.

There's an interesting point, however to the core point Steve makes about the disposability of vibe-coded (or AI-generated) code: _all_ code is disposable. Every single line of code I wrote during the many years I was a professional developer has since been discarded. And it's not just because I was a singularly terrible coder; this is often the _normal_ thing that happens with code bases after just a short period of time. As much as we lament the longevity of legacy code bases, or the impossibility of fixing some stubborn old systems based on dusty old languages, it's also very frequently the case that people happily rip out massive chunks of code that people toiled over for months or years and then discard it all without any sentimentality whatsoever.

Codeless tooling just happens to embrace this ephemerality and treat it as a feature instead of a bug. That kind of inversion of assumptions often leads to interesting innovations.

## To enterprise or not

As I noted in my original piece on codeless software, we can expect any successful way of building software to be appropriated by companies that want to profiteer off of the technology, _especially_ enterprise companies. This new realm is no different. Because these codeless orchestration systems have been percolating for some time, we've seen some of these efforts pop up already.

For example, the team at Every, which consults and builds tools around AI for businesses, calls a lot of these approaches [compound engineering](<https://every.to/chain-of-thought/compound-engineering-how-every-codes-with-agents>) when their team uses them to create software. This name seems fine, and it's good to see that they maintain the ability to switch between models easily, even if they currently prefer Claude's Opus 4.5 for most of their work. The focus on planning and thinking through the end product holistically is a particularly important point to emphasize, and will be key to this approach succeeding as new organizations adopt it.

But where I'd quibble with some of what they've explained is the focus on tying the work to individual vendors. Those concerns should be abstracted away by those who are implementing the infrastructure, as much as possible. It's a bit like ensuring that most individual coders don't have to know exactly which optimizations a compiler is making when it targets a particular CPU architecture. Building that muscle where the specifics of different AI vendors become less important will help move the industry forward towards reducing platforms costs — and more importantly, empowering coders to make choices based on their priorities, not those of the AI platforms or their bosses.

## Meeting the codeless moment

A good example of the "normal" developer ecosystem recognizing the groundswell around codeless workflows and moving quickly to integrate with them is the Tailscale team _already_ shipping [Aperture](<https://tailscale.com/blog/aperture-private-alpha>). While this initial release is focused on routine tasks like managing API keys, it's really easy to see how the ability to manage gateways and usage into a heterogeneous mix of coding agents will start to enable, and encourage, adoption of new coding agents. (Especially if those "frontier-minus-six" scenarios start to take off.)

I've been on the record [for years](<https://me.dm/@anildash/109719178280170032>) about being bullish on Tailscale, and nimbleness like this is a big reason why. That example of seeing where developers are going, and then building tooling to serve them, is always a sign that something is bubbling up that could actually become signficant.

It's still early, but these are the first few signs of a nascent ecosystem that give me more conviction that this whole thing might become real.
