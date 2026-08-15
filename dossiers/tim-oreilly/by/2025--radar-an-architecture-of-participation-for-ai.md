---
title: "An Architecture of Participation for AI?"
person: tim-oreilly
section: by
type: blog-post
year: 2025
date: 2025-05-19
venue: "O'Reilly Radar"
authors: "Tim O'Reilly"
source_url: https://www.oreilly.com/radar/an-architecture-of-participation-for-ai/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the oreilly.com/radar WordPress REST API (people_taxonomy=tim-oreilly); HTML converted to markdown."
---

# An Architecture of Participation for AI?

## Full text

About six weeks ago, I sent an email to Satya Nadella complaining about the monolithic winner-takes-all architecture that Silicon Valley seems to envision for AI, contrasting it with “the architecture of participation” that had driven previous technology revolutions, most notably the internet and open source software. I suspected that Satya might be sympathetic because of [past conversations we’d had](<https://www.linkedin.com/pulse/conversation-satya-nadella-his-new-book-hit-refresh-tim-o-reilly>) when his book [_Hit Refresh_](<https://www.amazon.com/Hit-Refresh-Rediscover-Microsofts-Everyone-ebook/dp/B01HOT5SQA>) was published in 2017.

I made the case that we need an architecture for the AI industry that enables cooperating AIs, that isn’t a winner-takes-all market, and that doesn’t make existing companies in every industry simply the colonial domains of extractive AI conquerors, which seems to be the Silicon Valley vision.

Little did I know that Microsoft already had something in the works that is a demonstration of what I am hoping for. It’s called NLWeb (Natural Language Web), and it’s being announced today. Satya offered O’Reilly the chance to be part of the rollout, and we jumped at it.

## Embracing the Early Stage of Innovation

My ideas are rooted in a notion about how technology markets evolve. We have lived through three eras in computing. Each began with distributed innovation, went through a period of fierce competition, and ended with monopolistic gatekeepers. In the first age (mainframes), it was IBM, in the second (PCs) Microsoft, and in the third (internet and mobile) the oligopoly of Google, Amazon, Meta, and Apple.

The mistake that everyone makes is a rush to crown the new monopolist at the start of what is essentially a wide-open field at the beginning of a new disruptive market. And they envision that monopoly largely as a replacement for what went before, rather than realizing that the paradigm has changed. When the personal computer challenged IBM’s hardware-based monopoly, companies raced to become the dominant personal computer hardware company. Microsoft won because it realized that software, not hardware, was the new source of competitive advantage.

The story repeated itself at the beginning of the internet era. Marc Andreessen’s Netscape sought to replace Microsoft as a dominant software platform, except for the internet rather than the PC. AOL realized that content and community, not software, was going to be a source of competitive advantage on the internet, but they made the same mistake of assuming the end game of consolidated monopoly rather than embracing the early stage of distributed innovation.

Microsoft CTO Kevin Scott announces NLWeb at Microsoft Build 2025.

So here we are at the beginning of the fourth age, the age of AI, and once again, everyone is rushing to crown the new king. So much of the chatter is whether OpenAI or one of its rivals will be the next Google, when it looks to me that they are more likely the next Netscape or the next AOL. DeepSeek has thrown a bomb into the coronation parade, but we haven’t yet fully realized the depth of the reset, or conceptualized what comes next. _That is typically figured out through a period of distributed innovation._

## We Need an Architecture of Participation for AI

The term “[the architecture of participation](<https://www.oreilly.com/pub/a/tim/articles/architecture_of_participation.html>)” originally came to me as an explanation of why Unix had succeeded as a collaborative project despite its proprietary license while other projects failed despite having open source licenses. Unix was designed as a small operating system kernel supporting layers of utilities and applications that could come from anyone, as long as they followed the same rules. Complex behaviors could be assembled by passing information between small programs using standard data formats. It was a protocol-centric view of how complex software systems should be built, and how they could evolve collaboratively. Linux, of course, began as a re-implementation of Unix, and it was the architecture of participation that it inherited, as much as the license and the community, that was the foundation of its success. The internet was also developed as a distributed, protocol-based system.

That concept ran through my web advocacy in the early ’90s, open source advocacy in the late ’90s, and Web 2.0 in the aughts. Participatory markets are innovative markets; prematurely consolidated markets, not so much. The barriers to entry in the early PC market were very low, entrepreneurship high. Ditto for the Web, ditto for open source software and for Web 2.0.  For late Silicon Valley, [fixated on premature monopolization via “blitzscaling”](<https://www.linkedin.com/posts/timo3_the-fundamental-problem-with-silicon-valley-activity-6498637102643843072-9duJ?trk=public_profile_like_view>) (think Uber, Lyft, and WeWork as examples, and now OpenAI and Anthropic), not so much. It’s become [a kind of central planning](<https://www.oreilly.com/radar/ai-has-an-uber-problem/>). A small cadre of deep-pocketed investors pick the winners early on and try to drown out competition with massive amounts of capital rather than allowing the experimentation and competition that allows for the discovery of true product-market fit.

And I don’t think we have that product-market fit for AI yet. Product-market fit isn’t just getting lots of users. It’s also finding business models that pay the costs of those services, and that create value for more than the centralized platform. The problem with premature consolidation is that it narrows the focus to the business model of the platform, often at the expense of its ecosystem of developers.

As Bill Gates famously [told Chamath Palihapitiya](<https://stratechery.com/2018/the-bill-gates-line/>) when he was running the nascent (and ultimately failed) Facebook developer platform, “This isn’t a platform. A platform is when the economic value of everybody that uses it exceeds the value of the company that creates it. Then it’s a platform.” To be clear, that is not just value to end users. It’s value to developers and entrepreneurs. And that means the opportunity to profit from their innovations, not to have that value immediately harvested by a dominant gatekeeper.

Now of course, Sam Altman talks about creating value for developers. In a recent appearance at Sequoia Capital’s AI Ascent event, [he said](<https://www.windowscentral.com/software-apps/openai-subscription-based-operating-system-on-chatgpt>) his hope is to create “like just an unbelievable amount of wealth creation in the world and other people to build on that.” But he uses the language of “an operating system” that others build on top of (and pay OpenAI for the use of) rather than a shared infrastructure co-created by an ecosystem of developers.

That’s why I’ve been rooting for something different. A world where specialized content providers can build AI interfaces to their own content rather than having it sucked up by AI model builders who offer up services based on it to their own users. A world where application developers can offer new kinds of services that enable others in a cooperative cascade.

## We’re Just Getting Started

Anthropic’s Model Context Protocol, an open standard for connecting AI agents and assistants to data sources, is the first step toward a protocol-centric vision of cooperating AIs. It has generated a lot of well-deserved enthusiasm. Google’s A2A takes that further with a vision of how AI agents might cooperate. NLWeb adds to that an easy way for internet content sites to join the party, offering both a conversational front end to their content and an MCP server so that it is accessible to agents.

This is all going to take years to get right. But because it’s a protocol-centric rather than a platform-centric vision, solutions can come from everywhere, not just from a dominant monopolist.

Every new wave of computing has also had a new user interface paradigm. In the mainframe era, it was the teletype terminal; for the PC, the Graphical User Interface; for the internet, the web’s document-centric interface; for mobile, touch screens. For AI (for now at least), it appears to be conversational interfaces.

Companies such as Salesforce and Bret Taylor’s Sierra are betting on conversational agents that are front ends to companies, their services, and their business processes, in the same way that their website or mobile app is today. Others are betting on client-side agents that will access remote sites, but often by calling APIs or even performing the equivalent of screen scraping. MCP, A2A, and other agent protocols point to a richer interaction layer made up of cooperating AIs, able to connect to _any site_ offering AI services, not just via API calls to a dominant AI platform.

All companies need at least a start on an AI frontend today. There’s a fabulous line from C. S. Lewis’s novel [_Till We Have Faces_](<https://en.wikipedia.org/wiki/Till_We_Have_Faces>):__ “We cannot see the gods face to face until we have faces.” Right now, some companies are able to offer an AI face to their users, but most do not. NLWeb is a chance for every company to have an AI interface (or simply “face”) for not just their human users but any bot that chooses to visit.

Microsoft’s Kevin Scott shares a glimpse of O’Reilly’s forthcoming NLWeb demo.

NLWeb is fully compatible with MCP and offers existing websites a simple mechanism to add AI search and other services to an existing web frontend. We put together our demo AI search frontend for O’Reilly in a few days. We’ll be rolling it out to the public soon.

[Give it a try](<https://aka.ms/AAw2etx>)
