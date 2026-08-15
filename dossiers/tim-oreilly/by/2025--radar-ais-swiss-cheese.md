---
title: "AI’s Swiss Cheese"
person: tim-oreilly
section: by
type: blog-post
year: 2025
date: 2025-08-11
venue: "O'Reilly Radar"
authors: "Tim O'Reilly"
source_url: https://www.oreilly.com/radar/ais-swiss-cheese/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the oreilly.com/radar WordPress REST API (people_taxonomy=tim-oreilly); HTML converted to markdown."
---

# AI’s Swiss Cheese

## Full text

Last month, I spoke with Matthew Prince, cofounder and CEO of Cloudflare, as part of my ongoing series of public conversations, [_Live with Tim O’Reilly_](<https://www.oreilly.com/live/live-with-tim/>). Cloudflare made waves with its [July 1 announcement](<https://www.cloudflare.com/press-releases/2025/cloudflare-just-changed-how-ai-crawlers-scrape-the-internet-at-large/>) that it will block AI crawlers by default and give content owners the ability to decide who can use their material for training AI models. That’s a big deal for anyone who creates original work for the web.

Obviously, I really care about this issue. O’Reilly’s mission is to [share the knowledge of innovators](<https://www.oreilly.com/about/>), and we depend on the ability to reach customers so they can hear directly from those innovators. We’re in the midst of a fundamental shift from the old search-driven web, which rewarded content creators with traffic, to an AI-driven internet where the bots give the answers and the original sources may never be seen. As Matthew put it, “Bots don’t click on ads. They don’t subscribe. And they don’t give you the validation of knowing people are reading your content.” (We don’t advertise, but we do depend on subscribers and à la carte content purchasers.)

It is true that we’re still early in the evolution of the business model for AI, but better business models don’t happen in a vacuum. Cloudflare is giving content creators tools for expressing their preferences. It’s been too easy for AI companies to grab whatever content they can get their hands on without compensation or credit. Cloudflare is starting down the path of building market mechanisms for humans to express our preferences to roving bots. Now, we have to get those deploying those bots to respect not just the wishes of their creators but the wishes of those whose content or services they are consuming.

## **Filling Holes: From the Internet’s Missing Security Layer to AI’s Swiss Cheese**

I kicked things off by asking Matthew to describe Cloudflare’s mission. His short answer for cocktail parties is “serve the internet faster and protect it from bad guys.” But when I asked him to go “more slowly” ([a Proust reference I’ve used before](<https://www.oreilly.com/radar/more-slowly/>)), he said, “When you are sitting down and writing out the protocols for the internet back in the ’60s, ’70s, and ’80s, we had no idea what it was going to become. . . .Cloudflare is trying to go back and fill in those holes—security, privacy, reliability—that should have been there from the beginning.”

He then applied this notion of filling holes to AI. The metaphor he kept returning to is Swiss cheese. It’s full of holes. AI models are too, and they need high-quality content to fill them. The humans who create that content need to be compensated, but the AI companies have just skated right by this issue, much as the original developers of the internet ignored security, with later consequences for all of us.

Matthew walked us through the numbers. Ten years ago, the deal with Google was roughly two pages scraped for every unique visitor sent back. With the rise of “answer boxes” and now AI overviews, that ratio has gone from 2:1 to 18:1. For AI companies like OpenAI and Anthropic, the imbalance is even more extreme: OpenAI’s ratio is around 1,500 to 1. Anthropic’s is around 60,000 to 1. Matthew put it bluntly: “That breaks the business model of the web.”

From the user’s point of view, these direct answers are a convenience. From the creator’s point of view, they remove the link between value creation and value capture. This is another version of what _The New York Times_ called “[AI’s original sin](<https://www.oreilly.com/radar/how-to-fix-ais-original-sin/>).”

## **Avoiding the Medici Future**

Another metaphor that I loved for its historical resonance was what Matthew called the “Medici future” of journalism: “You could imagine five big AI companies, each employing all the journalists and researchers they need. There’s a conservative one, a liberal one. . . .But the decentralizing power of the web could be replaced by massive centralization.”

The flowering of the arts under the Medicis in Renaissance Florence was wonderful, but do we really want to return to that world of artistic patronage dependent on immense wealth inequality? Cloudflare’s first step is requiring what I call Unix-style “user, group, world” permissions for AI crawlers so there can be a functioning market for content. Step two is making sure that the market is fair with a level playing field for big and small AI companies alike.

We found ourselves in fierce agreement here. For too long, platforms have taught us to chase clicks as a proxy for value. I liked Matthew’s take: “Traffic is a bad approximation for value. . . .A better world is one where we identify the holes in the Swiss cheese and reward the people who fill them, both monetarily _and_ with recognition.”

## **AI Security and the Arms Race**

Cloudflare has long used machine learning to detect and block malicious traffic. AI will make attacks more sophisticated, but it can also help build better defenses. “Whoever has the most data tends to win in the world of AI,” he said. “On balance, I think the world becomes more secure because of AI rather than less secure.”

He also described a growing push for cryptographic identification of bots so we can build an “industry spam filter” for AI crawlers. That’s a direction I’d love to see become a standard, much as the anti-spam community developed shared blocklists and reputation systems in the early 2000s.

Matthew ended with a vision I share: This AI disruption could be the moment we build a better web, one that rewards quality and originality instead of sheer volume.

> “If this is the end of the wild, spammy, engagement-driven internet, maybe that’s a good thing. . . .Let’s compensate the people who fill the holes in the Swiss cheese, reward them, celebrate them—and maybe we’ll build a better web.”

That’s exactly the conversation we need to be having now, before the future gets locked in.

_Sorry to have no video excerpts for this chat. Due to technical difficulties, the conversation was audio only._

* * *

_AI tools are quickly moving beyond chat UX to sophisticated agent interactions. Our upcoming AI Codecon event,  **Coding for the Future Agentic World** , will highlight how developers are already using agents to build innovative and effective AI-powered experiences. We hope you’ll join us on September 9 to explore the tools, workflows, and architectures defining the next era of programming. It’s free to attend._  
  
_[Register now to save your seat](<https://www.oreilly.com/AgenticWorld/>)._
