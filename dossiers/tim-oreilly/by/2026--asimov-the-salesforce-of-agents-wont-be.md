---
title: "The Salesforce of agents won't be Salesforce, The Google of agents won't be Google"
person: tim-oreilly
section: by
type: blog-post
year: 2026
date: 2026-05-13
venue: "Asimov’s Addendum"
authors: "Jesus Rodriguez, Ilan Strauss, Tim O'Reilly"
source_url: https://asimovaddendum.substack.com/p/the-salesforce-of-agents-wont-be
retrieved: 2026-08-13
content: full-text
notes: "Subtitle: “Building software architectures and mechanisms for the agentic economy”. Asimov’s Addendum, the Substack of Tim O’Reilly and Ilan Strauss on AI commercialization risks and governance; published CC BY 4.0. Retrieved from the free public post page."
---

# The Salesforce of agents won't be Salesforce, The Google of agents won't be Google

## Full text

_This post was originally published on[The Sequence](<https://thesequence.substack.com/p/the-sequence-opinion-856-the-salesforce>) by Jesus Rodriguez and is being reposted here with the author’s permission. We provide a brief foreword._

* * *

## Foreword: Thinking about AI market design

The piece below by Jesus Rodriguez makes a compelling case that agents are emerging as a new class of economic actor: a new _delegated_ consumer (or shopper) with native needs around identity, payments, memory, and commerce. We share his view that the internet was built for humans and now must be partly rebuilt for machines.   
  
**MECHANISMS**. We want to add one note of caution about how that rebuilding happens. What Rodriguez describes is, in our language, the “[missing mechanisms](<https://www.oreilly.com/radar/the-missing-mechanisms-of-the-agentic-economy/>)” problem applied to agents. Tim has argued that **markets need mechanisms** _for distributed value creation and[participation](<https://asimovaddendum.substack.com/p/the-architecture-of-participation>)_. _Mechanisms are engineered rules that incentivize self-interested actors to produce honest disclosure and can aim for a market that benefits all actors, rather than a single firm_.__ A mechanism’s rules decide outcomes and payments for things like auctions, voting (no payment), public goods spaces, and more. They can make markets work where otherwise they would not due to agents behaving strategically by hiding information and not wanting to participate (“why license data when you can scrape it”, for example).   
  
**The agent economy is now confronting its own version of this missing markets question** (as Google’s _Search_ and Amazon’s _marketplace_ was once did too): _but it’s missing mechanisms for agents, not for humans_. Delegation, attestation, payment scopes, machine-readable provenance, agent identity, memory boundaries should be internet and AI standards first, that underpin agentic markets, and then innovative competitive product features second. The two can and should exist as compatible conceptualizations of how to build markets online as open publicly beneficial spaces. 

The layers for agentic AI markets Rodriguez describes below will be built. The question remains how to realize them as open, modular infrastructure, rather than as proprietary chokepoints?   
  
The defaults are still soft and the market structures are still fluid. They will not stay that way for long.   
  
_— Tim O’Reilly & Ilan Strauss_

##   
Introduction: Agentic markets

For the first few decades of the internet, software had a reasonably stable assumption baked into it: **the user was a human.**

A human had eyes, a browser, a mouse, a password manager, a credit card, an email address, a tolerance for modal dialogs, and a finite amount of patience. The entire SaaS and consumer internet stack grew around this shape of user. Search engines ranked pages for humans. E-commerce sites optimized funnels for humans. CRMs tracked human sales reps selling to human buyers. Identity systems authenticated humans. Analytics systems measured human clicks, human sessions, human conversions.

[](<https://substackcdn.com/image/fetch/$s_!Gsfj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff87aa450-63b5-4c70-a19c-558493ca715e_2391x1753.jpeg>)Image Source: <https://ledidi.com/academy/missing-data-mechanisms-and-how-to-handle-it>

## Then we started building AI agents

At first, agents looked like toys. A chatbot that could book a calendar invite. A coding assistant that could open a pull request. A browser agent that could navigate a website on your behalf, slowly and somewhat comically. But underneath the awkwardness was something important: software was no longer being used only by people. Software was being used by software that could reason, plan, transact, remember, delegate, and retry.

This is a much bigger shift than “chatbots are the new UI.” It is closer to the emergence of a new economic actor. Not a legal person, not a human replacement, and not magic. But a new kind of consumer.

Agents consume information. Agents consume APIs. Agents consume storage, compute, tools, workflows, credentials, payments, and services. Agents evaluate options, make requests, negotiate constraints, and execute tasks. They are not just another interface to existing software. They are a new demand surface.

Once you see agents as consumers, a lot of the software landscape starts to look strangely misaligned.

The Salesforce for agents may not be Salesforce. The Google for agents may not be Google. The Amazon for agents may not be Amazon. Not because these companies are weak, but because the primitives change when the consumer changes.

A human using Salesforce wants dashboards, contacts, pipeline stages, notes, reminders, and reports. An agent using a CRM wants something else: structured state, task objectives, relationship graphs, permissioned memory, machine-readable sales playbooks, and reliable APIs for updating intent. It does not need a beautiful dashboard. It needs a canonical substrate of customer truth that it can query, mutate, and reason over safely.

A human using Google wants ranked blue links, snippets, maps, videos, and maybe an answer box. An agent using search wants provenance, freshness, confidence intervals, citations, entity resolution, schema alignment, and retrieval interfaces that are stable under automation. It does not want ten links. It wants to know which source is authoritative for a given claim, what changed since the last run, and whether the answer is safe to act on.

A human shopping online wants product photos, reviews, discounts, shipping estimates, and a checkout page. An agent shopping on behalf of a human wants product metadata, compatibility constraints, return policies, vendor reliability scores, payment authorization scopes, fraud guarantees, and receipts that can be parsed by another machine. It does not browse. It solves an optimization problem under constraints.

This is why “just give agents browser access” feels both exciting and obviously temporary. Browser access is backwards compatibility. It is useful in the same way screen scraping was useful before APIs. But if agents become a major class of software user, we should expect agent-native infrastructure to emerge.

The web was designed around human attention. **The agent economy will be designed around machine action.**

## Consider identity

Today, identity on the internet is mostly a ceremony for proving that a human is allowed to do something. We use passwords, passkeys, OAuth, SSO, device fingerprints, CAPTCHAs, and risk engines. These systems assume a human principal somewhere in the loop.

Agents break this model in subtle ways. An agent is not exactly the user. It is also not exactly an employee, a bot, a service account, or an OAuth app. It may act for a person, but only within a certain scope. It may need to buy groceries but not alcohol, schedule meetings but not cancel medical appointments, email customers but not change pricing, deploy code but not rotate production secrets.

So agent identity needs delegation as a first-class primitive. Not “here is my password, go do stuff.” Not “here is a broad API token with terrifying permissions.” Instead: here is an agent, acting on behalf of this principal, for this objective, during this time window, with this budget, using these tools, under these audit requirements.

This implies infrastructure: agent passports, delegated credentials, capability-based access control, revocation systems, policy engines, and audit logs that explain not just what happened, but why the agent believed it was allowed to act.

The “why” matters. A normal API log might say: POST /refunds succeeded. An agent-native audit log should say: the agent issued a refund because the customer met policy condition X, the order was delayed by Y days, the user had previously authorized refunds below Z dollars, and no higher-risk flags were present. This is not just observability. It is accountability.

## Now consider payments

Human payments are optimized around cards, wallets, bank accounts, checkout pages, fraud prevention, and dispute resolution. The system is designed for a human to consciously approve a transaction, even if that approval has become increasingly compressed into one click or one biometric scan.

Agents introduce a different payment pattern: constrained autonomy.

A travel agent might have permission to spend up to $1,500 on flights, but only if the arrival is before 6 p.m., the layover is under two hours, the airline is not on a blocked list, and the fare is refundable. A procurement agent might be allowed to buy cloud credits, office equipment, or data enrichment services within a monthly departmental budget. A coding agent might pay for API calls, benchmark runs, or temporary compute to complete a task.

This requires payment rails that are more programmable than consumer checkout and less heavyweight than enterprise procurement. We will need spending envelopes, machine-readable invoices, pre-authorized budgets, reversible transactions, agent reputation, merchant attestations, and real-time policy checks.

[Share](<https://asimovaddendum.substack.com/p/the-salesforce-of-agents-wont-be?utm_source=substack&utm_medium=email&utm_content=share&action=share>)

A credit card number is a poor interface for an autonomous actor. It is a bearer token with too much authority and too little context. Agent payments will likely look more like signed intents: “Agent A, acting for User B, is authorized to pay Merchant C up to Amount D for Purpose E, subject to Policy F.” The merchant should be able to verify this. The user should be able to revoke it. The system should be able to dispute it. The agent should be able to reason about it before acting.

## E-commerce changes too

Most online stores are persuasion machines. They are designed to convert human uncertainty into purchase behavior. Recommendation modules, scarcity banners, coupon wheels, bundles, sponsored placements, and dark patterns all exist because humans are impressionable, visual, and busy.

Agents are busy too, but in a different way. They are not emotionally moved by a hero image of a backpack on a mountain. They may be vulnerable to other things: poisoned reviews, manipulated metadata, adversarial product descriptions, fake compatibility claims, hidden fees, or vendors that optimize for agent-ranking algorithms.

So agent commerce will need a different trust layer. Product pages become less important than product specs. Reviews become less useful unless they are structured, verified, and resistant to manipulation. Return policies need to be machine-readable. Availability needs to be queryable. Bundles need explicit semantics. “Best laptop for me” becomes a negotiation among constraints: workload, budget, portability, battery, repairability, delivery time, warranty, vendor trust, and user preference memory.

The equivalent of SEO for agents will be fascinating and horrible. Today, companies optimize pages to rank in human search. Tomorrow, they will optimize structured representations to be selected by buyer agents. This will produce new spam, new fraud, new ranking games, and new defensive infrastructure. We should assume every agent-readable marketplace becomes adversarial once enough money flows through it.

## Data storage also changes

Human software treats data as something to display, search, and report. Agent software treats data as working memory. Agents need durable context across tasks: user preferences, prior decisions, organizational policies, project state, personal constraints, and learned patterns. But they also need memory boundaries. Remembering everything is not intelligence. It is liability.

An agent-native storage layer needs multiple kinds of memory. There is episodic memory: what happened during the last task. Semantic memory: stable facts about the user or organization. Procedural memory: how to perform recurring workflows. Policy memory: what is allowed. Source memory: where a belief came from. And scratch memory: temporary reasoning artifacts that should probably expire.

This storage layer must support retrieval, provenance, deletion, summarization, permissioning, and conflict resolution. It must know that “the user prefers morning flights” is not the same kind of fact as “the user authorized a $700 purchase yesterday.” It must distinguish stale preferences from hard constraints. It must expose memory to agents in ways that reduce hallucination rather than amplify it.

In the human internet, data was often collected because it might become useful later. In the agent internet, data becomes directly operational. If an agent remembers incorrectly, it acts incorrectly. Memory bugs become action bugs.

## This brings us to software design itself

A surprising amount of current software is hostile to agents because it was built for humans. Buttons without semantic labels. PDFs instead of structured documents. Emails that require interpretation. Dashboards with charts but no underlying query API. Terms of service written only for lawyers. Error messages that explain nothing. Workflows that require a human to click through five screens because the product team wanted engagement.

_Agents expose the hidden tax of unstructured software._

Agent-friendly software will have different virtues. It will be explicit, inspectable, composable, and transactional. It will provide APIs not as an afterthought, but as the main surface. It will describe capabilities, costs, side effects, and failure modes. It will support dry runs. It will make state changes reversible where possible. It will provide good error messages because the error message is not for a frustrated human anymore; it is for another system deciding what to do next.

The best agent software may look boring to humans. A great agent-native CRM may be mostly a graph, a policy engine, an event log, and a set of tool contracts. A great agent-native search engine may look like a retrieval and verification API. A great agent-native bank may look like programmable authorization plus risk scoring. A great agent-native e-commerce platform may look like a giant constraint solver with trust primitives.

_Thanks for reading Asimov’s Addendum! This post is public so feel free to share it._

[ Share](<https://asimovaddendum.substack.com/p/the-salesforce-of-agents-wont-be?utm_source=substack&utm_medium=email&utm_content=share&action=share>)

This does not mean human interfaces disappear. Humans still set goals, approve high-risk actions, inspect outcomes, and change their minds. But the center of gravity moves. The human becomes more like a principal, supervisor, or exception handler. The agent becomes the high-frequency user.

This distinction matters because incumbents often win interface shifts but lose primitive shifts.

When mobile arrived, many desktop companies successfully made mobile apps. But the biggest mobile-native companies were not just desktop products on smaller screens. They were built around new primitives: GPS, camera, push notifications, contacts, sensors, app stores, and always-on connectivity.

Agents are similar. Adding a chatbot to an old product is not the same as rebuilding the product around agentic use. The winners may be companies that understand the new primitives early: delegation, memory, tool use, verification, policy, agent identity, machine-readable commerce, and autonomous payments.

The phrase “agents are a new consumer” sounds metaphorical, but it is actually quite literal. Consumers create demand. Demand reshapes markets. Markets reward infrastructure that serves the consumer’s native behavior.

_Humans click. Agents call tools._

_Humans browse. Agents query._

_Humans forget. Agents persist memory._

_Humans approve. Agents need delegated authority._

_Humans compare visually. Agents optimize over structured constraints._

_Humans tolerate ambiguity. Agents need executable semantics._

_Humans can be persuaded. Agents can be attacked._

Once agents become common, every software company will face a basic question: is your product merely usable by agents, or is it built for them?

The difference will matter. A website that an agent can painfully navigate is not agent-native. An API that exposes a few endpoints is not agent-native. A chatbot bolted onto a dashboard is not agent-native. Agent-native software treats autonomous actors as first-class users with identity, permissions, memory, budgets, goals, and accountability.

We are early enough that much of this still looks speculative. The agents are unreliable. The standards are immature. The demos break. The economics are unclear. But this is often what new consumers look like at the beginning. Mobile apps were once toys. Cloud workloads were once experiments. Online payments were once scary. Developer APIs were once niche.

Then, slowly, the toy becomes a workflow. The workflow becomes a habit. The habit becomes infrastructure. And the infrastructure becomes invisible.

_**The internet was built for humans, then patched for machines. The next internet may be built for machines, with humans in command**_**.**

_That is the opportunity: not just to build agents, but to build the world they will consume_.

* * *

Thanks for reading Asimov’s Addendum! 

Subscribe

  
Visit _AI Disclosures Project_ for [more information](<https://ai-disclosures.org/>) on our work.
