---
title: "An open standard for AI content attribution"
person: "alex-springer"
section: "by"
type: "blog-post"
year: 2026
date: "2026-04-30"
venue: "OpenAttribution blog"
authors: "Alex Springer"
source_url: "https://openattribution.org/blog/open-standard-launch"
retrieved: "2026-08-13"
content: "full-text"
notes: "Bylined 'By Alex Springer' on the page. openattribution.org is his own organisation's site."
---

# An open standard for AI content attribution

## Full text

← Blog · 30 April 2026 · 4 min read

# An open standard for AI content attribution
OpenAttribution publishes its framework for tracking how content is used in AI systems. Retrieval works today. Citation and engagement come as agents adopt the standard.
By Alex Springer launch standards

Updated 11 June 2026: corrected the event model’s provenance and the governance section. The wire format is the neutral Content Telemetry standard ; OpenAttribution’s Technical Steering Committee governs OpenAttribution’s own specifications.
OpenAttribution is now live. We are an independently governed not-for-profit that publishes open specifications and operates free infrastructure for content attribution in AI. Today we are releasing the framework.
The problem is straightforward. When an AI agent retrieves a publisher’s article, a brand’s product page, or a retailer’s review and uses that content in a response, the content owner has no visibility into what happened. CDN logs and web server logs already see AI bot traffic. What’s missing is structure - a standard way to capture those events, correlate them, and eventually see what happens after the retrieval.

## Five events #
The framework builds on the Content Telemetry standard , which defines five events in the AI content lifecycle:

- Retrieval - content is fetched by an AI agent, whether via scraping, APIs, or content marketplaces. Observable at the HTTP layer.

- Grounding - content is loaded into the agent’s context and influences the response.

- Citation - content appears in the AI output as a direct quote, paraphrase, or source link.

- Display - content references are shown to the user in the interface (sources sidebar, citation cards, inline links).

- Engagement - the user interacts with or clicks through to the original source.

## What works today #
Retrieval tracking works without any cooperation from AI platforms. Your CDN, web server, or CMS already sees every AI bot request. We provide open-source integrations that detect AI user agents at that layer and report structured events.
Setup is two things. Add the integration to your existing infrastructure ( Cloudflare today, more platforms in progress). Publish a small text file at /.well-known/content-telemetry.json declaring where telemetry is reported. We operate a free hosted telemetry service, so there is nothing to run. Only bot identity and URL visited are collected - no cookies, no user data, no impression tracking.
Citation and engagement tracking are different. They depend on AI agents adopting the standard, reporting which content they cited, how they used it, and what users did with the response. That is the next layer, and it is where the real value sits.

## How the standard is governed #
No single publisher, brand, or technology provider can solve attribution alone. The standard has to be neutral or it cannot do its job.
OpenAttribution is structured so that no single company controls it. We are a not-for-profit with one-member-one-vote governance. A Technical Steering Committee, independent of the board, owns OpenAttribution’s specifications - the AIMS agent identity standard and the registry model. The event wire format is the Content Telemetry standard , a neutral open standard; OpenAttribution participates in it through public comment and maintains a commerce profile layered on it. Membership fees do not buy specification control.
Over the coming months we will formalise a steering committee composed of publishers, brands, AI platforms, and measurement and analytics providers. Early participants shape the rules that govern how content is tracked and valued across AI systems.

## First supporting members #
A first group of partners has signed on to help us build this: Acceleration Partners, Adtraction, APMA, Awin, CJ, Konverj, MarTech Record, Rakuten Advertising, and Scale Digital.
A few of them on why they are joining:
“AI is often framed as a way to drive the same output with fewer resources. The real opportunity is to reduce operational friction so more time and capability is spent on the strategies and relationships that will drive more valuable outcomes than can be achieved today. To realise this opportunity, we have to be able to effectively measure and fairly attribute value, which means the work that OpenAttribution is doing is critical to the long-term success of the digital ecosystem.”

- Matt Wool, Acceleration Partners

“AI platforms are consuming affiliate content at scale, and that content genuinely helps customers make purchasing decisions. If the partners aren’t recognised and rewarded, they won’t be able to keep creating content, which would be catastrophic for brands, consumers and the channel as a whole. We are working with OpenAttribution to engage with AI platforms as an industry and build a framework so that brands and partners can continue to thrive.”

- John Vickers, Adtraction

“The shift to AI-driven discovery is one of the most significant changes in digital user experiences. AI platforms are generating answers at scale using web content, and ensuring that content is fairly valued and rewarded has never been more important. OpenAttribution is a vital step towards the open infrastructure this industry needs: a shared way for publishers, brands and platforms to measure content’s role in AI-driven journeys and ensure value flows back to the people who made it.”

- James Bentley, Awin

“AI and agentic environments are consuming affiliate content and that genuinely helps customers find information and make purchasing decisions. That being said, if the partners aren’t recognised and rewarded, they won’t be able to keep creating content, which would be not only a problem for brands, but also consumers, and the channel as a whole. We are working with OpenAttribution to engage with AI platforms and help build a trusted framework so that brands and partners can continue to work together in a way that progresses and moves the affiliate and partner marketing industry forward.”

- Ben Cox, Rakuten

## What’s next #
AI platforms rely on high-quality content. Asking for citation and usage data in return is reasonable. Those conversations need measurement infrastructure behind them to be productive, and that infrastructure should be open, not owned by any single vendor.
If you want to start tracking AI retrieval today, the Cloudflare integration is live. WordPress, Vercel, Netlify, Fastly, Akamai, and CloudFront are next.
Join the waitlist to get an API key and your domain set up. If you operate a CDN, analytics platform, content marketplace, or AI agent and want to talk integration, get in touch .
