---
title: "AI is not search"
person: "alex-springer"
section: "by"
type: "blog-post"
year: 2026
date: "2026-02-10"
venue: "OpenAttribution blog"
authors: "Alex Springer"
source_url: "https://openattribution.org/blog/ai-is-not-search"
retrieved: "2026-08-13"
content: "full-text"
notes: "Bylined 'By Alex Springer' on the page. openattribution.org is his own organisation's site."
---

# AI is not search

## Full text

← Blog · 10 February 2026 · 4 min read

# AI is not search
LLM conversations are not just 'search with more words.' The way value flows from content is fundamentally different, and we do not have frameworks to support that.
By Alex Springer industry policy

Search is a really smart index. It points you to content. You type a query, get a list of links, and click through to the source. The publisher gets a visit. The value chain, however imperfect, is at least legible.
AI is something different. It digests content, repurposes it, then delivers the value as if it is its own.
The underlying content is the same but the way value flows from it — and the way that value is paid back to the owners and creators of the content — is fundamentally different. Right now we do not have frameworks to support that.

## The stretching that got us here #
Google has been stretching its use of publisher content for years. Content previews, AMP pages, featured snippets. Each one made Google’s own products stickier and more valuable at the expense of publishers. AI features are the next step in that direction, but a much bigger one, and not just for Google.
How AI systems use, cite, and return value for the content they depend on is a question that applies to OpenAI, Anthropic, Perplexity, and every other player building on top of web content.

## What is missing #
Three things, fundamentally:

- No identity. When an AI agent requests content, publishers have no standard way to verify who it is, what it is licensed to access, or whether it will respect licensing terms.

- No measurement. There is no standardised way to track which content was retrieved and cited in the conversation that led to an outcome. Without measurement, attribution is impossible.

- No value return. Without identity and measurement, there is no mechanism for value to flow back to the people who created the content that made the AI response useful.

## Why this matters now #
Without measurement, the rational response from creators is to restrict AI access to their content. And many are doing exactly that — blocking AI crawlers, putting content behind paywalls, or simply producing less.
This threatens the content supply chain that the entire AI ecosystem depends on. The AI systems that consume content need that content to be produced, maintained, and updated. The people who produce it need to see some return. This is not a philosophical position — it is a market sustainability question.

## What OpenAttribution is building #
We are building two open standards to address this:

- AIMS (AI Manifest Standard) — DID-based agent identity with licensing provenance. So publishers can verify who is requesting their content and what it is licensed to do.

- Content Telemetry — Content attribution telemetry. Session-based tracking of what content was retrieved, cited, and what outcomes resulted. So there is a measurement layer that makes attribution possible.

Together with source-side licensing standards like RSL , these create a complete chain: publishers declare terms, agents prove identity, and usage is tracked. The frameworks that the AI content ecosystem needs to be sustainable.
Both standards are Apache 2.0 licensed, community-governed, and open for contribution .
