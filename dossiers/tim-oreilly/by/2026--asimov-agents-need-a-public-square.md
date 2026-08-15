---
title: "Agents Need a Public Square"
person: tim-oreilly
section: by
type: blog-post
year: 2026
date: 2026-06-05
venue: "Asimov’s Addendum"
authors: "Sruly Rosenblat, Ilan Strauss, Tim O'Reilly"
source_url: https://asimovaddendum.substack.com/p/agents-need-a-public-square
retrieved: 2026-08-13
content: full-text
notes: "Subtitle: “Why better agent discovery is needed – and why broadcasting may be the answer”. Asimov’s Addendum, the Substack of Tim O’Reilly and Ilan Strauss on AI commercialization risks and governance; published CC BY 4.0. Retrieved from the free public post page."
---

# Agents Need a Public Square

## Full text

[](<https://substackcdn.com/image/fetch/$s_!OH9h!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F24570531-5c4d-4009-9c51-c4264201a5e8_1218x430.png>)An illustration of the difference between broadcasting and one-to-one communication

* * *

The [Agent2Agent](<https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/>) (A2A) protocol was announced by Google a little over a year ago (April 2025). It was built to allow agents to communicate with each other across different sites and to enable any agent to reach out to specialized agents hosted by any company. Since then, it was moved to the Linux Foundation where it was later joined by MCP. The primary alternative to A2A, IBM’s _Agent Communication Protocol_(ACP1), was [quickly folded into the former](<https://github.com/orgs/i-am-bee/discussions/5>).

A2A is [now supported](<https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year>) on multiple cloud platforms, is integrated into LangGraph and CrewAI, gained over 20 thousand stars on GitHub, and has over 150 supporting organizations. **But despite being the only agent communication protocol with any traction, A2A still has almost no publicly deployed agents**. What appears to be the largest [agent registry](<https://a2aregistry.org/>) for A2A has just 100 publicly accessible agents compared to the ~3k remote MCP servers cataloged by [PulseMCP](<https://www.pulsemcp.com/servers>).

A lot of this is likely due to the lack of a true discovery system. A2A has discovery in the sense that if you know what domain an agent is located at, you can fetch its “agent card”2 that tells you what the agent does, how to reach it, and how to authenticate. _But it does little to help you find an agent you have never heard of_.

**There is no native, public space for an agent to ask a question widely and get an answer back.**_We argue that agentic communication that remains one to one is unlikely to meet a user’s needs_. Think how humans broadcast on social media to many when we communicate (and see who responds), or on Facebook Marketplace when we seek buyers. Agentic broadcasting and proper agentic discovery are two sides of the same coin. And it can be done in a way that is not centrally controlled.

-*-  
  
Rather than treating agent communication as a brand-new problem, it helps to look at the apps we already use and the protocols that were already built for human communication. Email, messaging apps, and social media have all dealt with the problems agent communication faces: discovery, privacy, identity, and trust, so a brief sojourn through their architectures is first helpful.

## The Email Protocol (SMTP): one to one communication

The Simple Mail Transfer Protocol (SMTP), launched in 1981, still enables today’s email. Specifically it defines how one domain’s email service communicates with another. When an email is sent from a Yahoo email account to a Gmail account, the message is passed via SMTP. But SMTP is not the whole email stack. It doesn’t define how you find where another domain’s mail server lives (that’s DNS MX records), it doesn’t establish whether an email can be trusted (that’s SPF, DKIM, and DMARC) and it doesn’t define how email clients like Apple Mail retrieve messages from servers (which is instead left to IMAP or POP3).

_Email has another limitation: every recipient needs to be specified individually_. Even in cases where it looks like an email is being broadcast, like with a newsletter going to hundreds of thousands of subscribers, that is not what is happening under the hood. Instead that same email is being sent individually to many addresses at once. Email also has no public ledger. Each message exists only in the inboxes it was delivered to, so there is nothing for non-recipients to look back at. A new subscriber to a newsletter can’t scroll through past emails in a newsletter’s archive, even if this would have been the desired behavior by the newsletter. Platforms like Substack that combine the functionality of blogs and newsletters work around this limitation by posting the article to the Substack on the web at the same time as it is sent out in email. This is a simple workaround, but it is not a solution based on how email works.

## Speaking to the Network: one to many communication

#### **Traditional Social media**

Since the release of email, much of the world’s communication ended up moving away from one to one and towards broadcasting. This opened up many benefits; users were able to communicate with thousands of people at once, asking questions that no one they know has the answer to. Someone with a piano they need to get rid of can post about it and rely on the network to self-sort interested parties.

When you post on Facebook or X / Twitter, you are not messaging many different people individually; you are broadcasting whatever opinion or question you have to everyone on the network (that network may be smaller for a private post). This doesn’t necessarily mean everyone will read your message. In order for a user to see a message, it has to pass whatever filters they have and rank high on their home screen algorithm, but it’s visible to them in the sense that they can see your post if they look for it.

On most platforms this broadcasting is done using the company’s proprietary internal APIs. This makes sense as broadcasting to some extent requires centralization. In order for a ledger of profiles and posts to exist and be shown to users, a server is needed, and servers are usually financed and owned by a single company. But there have been attempts to move this type of interaction away from a centralized server.  

[Share](<https://asimovaddendum.substack.com/p/agents-need-a-public-square?utm_source=substack&utm_medium=email&utm_content=share&action=share>)

#### **Federated / Decentralized Protocols**

[ActivityPub](<https://www.w3.org/TR/activitypub/>) (what Mastodon uses) and the [AT Protocol](<https://atproto.com/>) (what Bluesky runs on) tackle the centralization problem by allowing servers to communicate with each other. In ActivityPub, user accounts are tied to a server, and that server stores and delivers the user’s posts to other servers through federation. AT Protocol also uses servers to host user data, specifically Personal Data Servers, but it separates out other components like feeds and data aggregators (relays) more than ActivityPub does, and it is designed to make accounts more portable. Both systems are similar to traditional social media in that they still require some information to be stored on and transmitted through servers, but they differ in that _they are federated: different servers can communicate with each other, and content posted on one server can be seen from other servers_.

This federation provides the functionality of a traditional social media platform without locking user content to just one server since users could still access content from other servers. _But the power still concentrates with the server providers: they can still choose who to federate (or communicate) with, what content is allowed, and who their users could interact with_. This is perhaps most visible with direct messaging (or DMs). ActivityPub does not support encrypted messages: every “private” message can be read by the server owners where either account is hosted. [Bluesky](<https://bsky.social/about/blog/05-22-2024-direct-messages>) supports direct messaging with no encryption and they do it off protocol with no federation. The AT Protocol does not yet support direct messaging.

[Nostr](<https://nostr.com/>), another distributed social media protocol, takes a slightly different approach to identity and in turn communication. Instead of making a user’s identity something that is tied to a server, it makes identity a cryptographic key pair, meaning the user’s identity itself requires no hardware. The cryptographic keys that they need work the same whether they are stored on a hard drive or drawn on the back of a napkin. Posts are signed using the private key in a way that can be verified using the public key.

Communication still happens over servers (in this case called “relays”), and relays can still be censored, but a piece of content can be broadcast over any number of relays simultaneously, since the user’s identity is defined and enforced in a way that is agnostic to any one relay. If a user is blocked from one relay, other people can continue to follow them by listening to other relays.

In many ways, DMs on nostr function similarly to how they work in the Signal Protocol. Messages are encrypted so that only the recipient can see them. Given the fact that every user already has their own private and public key on nostr, encryption is a natural fit. NIP 17 (or Nostr Implementation Possibility 17)3 implements this by encrypting the message and then “gift wrapping” it to hide the sender’s identity from the public network.4

[Support us](<https://ai-disclosures.org/donate>)

 _Help architect a different AI future by donating to the[AI Disclosures Project](<https://ai-disclosures.org/>) today._

Regardless of the exact differences, the major commonality is that unlike something like Email or Signal, **these protocols are primarily designed for broadcasting**. **Questions sent aren’t meant to be answered by just one person; they are sent to a whole network of people at once**.

It’s not necessary to know who is on the network prior to asking for something. It’s on the recipients (potentially with the aid of the intervening platform) to decide what is relevant to them and what isn’t. Initial screening is done by whatever algorithm their feed uses and after that users choose what posts they respond to by themselves. Discovery is native to the protocols.

## What A2A Brings to the Table

The Agent2Agent protocol was built from the ground up for one-to-one communication between agents. It functions using the infrastructure already built for the web. It provides one agent the ability to reach out to another agent directly. Communication happens over standard HTTPS in a way that is not end-to-end encrypted but is encrypted while in transit.5

Agents can be tied directly to the domain they are hosted on (such as airbnb.com). So an Airbnb agent inherits the trust the website domain already has. This is similar to how an email inherits the trust of the site it is hosted on (e.g., if you receive an email from irs.gov you are likely to trust it). Additionally, if an agent already knows about a site, checking whether that site exposes agents is trivial. It’s worth noting that neither the domain resolution (finding the agent given the domain name) nor the inherited trust is unique to A2A: Nostr (via NIP-05) and Mastodon (via WebFinger) also link accounts to a domain through a file in the domain’s .well-known folder.  

Subscribe

The way an agent advertises itself on A2A is through an “agent card,” a structured document published at a known URL that describes what the agent does, how to reach it, and how to authenticate. _This is similar in many ways to how profiles work on social media but it is also where the protocol’s limits show: accessing an agent card from a website assumes you already have a domain to check_. **An A2A agent not connected to a major site is essentially invisible without a third party registry to rely on**.

[](<https://substackcdn.com/image/fetch/$s_!m4I_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4e4fb41e-1916-4019-826b-c89f7604bec5_1232x500.png>)

## The Costs of One-to-One Agent Communication

Agent communication through A2A closely resembles how email works. Both are primarily one-to-one, both cut out middlemen, identity is simple, and neither requires a third-party server. It is just one IP address reaching out to another and sending messages, the same way one mail server hands a message to another, with nothing sitting in between to be trusted, paid, or asked for permission. In many ways this is ideal: messages are truly private, nothing logs or indexes the exchange, and no platform has control over it (assuming two self-hosted domains). Agents get a persistent identity tied to URLs people already recognize.

_**But that architecture carries the same cost email has always carried: discovery**_. The first place you look for someone’s email address is never the email protocol itself. You search the web, check their publications, or pay a third party. Social media and its federated equivalents don’t have this problem: you broadcast what you offer and interested parties come to you. For agent communication to truly catch on outside of company silos, agents need that same ability to find each other.

One-to-one communication has its place. Once an agent is known it makes sense to keep conversations as private as possible. And introducing any third party server inherently lowers privacy.6 Even encrypted conversations leak some metadata about who is being contacted. But there are also inherent limitations to one to one communication – even if discovery is solved. **One-to-one communication adds unnecessary friction in cases where more than one agent is needed**. 

When looking for a cheap ticket, a person does not visit each individual airline’s site; they visit an aggregator and add their filters. Broadcasting protocols inherently support this type of interaction by just asking the network for the “cheapest airline tickets to Miami under $300” and receiving offers. One to one communication offers no equivalent. An agent that wanted the cheapest ticket would have to know every airline’s agent in advance, contact each one in turn, and assemble the comparison itself.7

That being said, broadcasting opens up new problems. Any public square an agent can broadcast into is also one an attacker can broadcast into — and a social media platform swarming with agents is a large target for prompt injection. MoltBook has already [proven this](<https://substack.com/home/post/p-188763572>). There are also real privacy tradeoffs with a broadcasting model. Every public message sent to the network could be read by everyone on the network and just like any content on the internet, anything public is hard to revoke. There are tradeoffs to different communication protocols and the pros and cons of each approach should be discussed in detail. But agents will eventually need a public square.

_I built out a prototype exploring how agent communication could look on nostr. It’s still pretty early but I would love to hear any feedback you have:<https://github.com/SrulyRosenblat/social_agents_prototype_nostr>  
_

[Support Us](<https://ai-disclosures.org/donate>)

 _Help architect a different AI future by donating to the[AI Disclosures Project](<https://ai-disclosures.org/>) today. Open protocols, enables open markets. _

1

This is only one of several protocols with the acronym ACP. Other protocols include the far more popular [Agent Client Protocol](<https://agentclientprotocol.com/get-started/introduction>) by Zed and the [Agent Commerce Protocol](<https://developers.openai.com/commerce>) by OpenAI.

2

A JSON file at a [well-known](<https://en.wikipedia.org/wiki/Well-known_URI>) path (/.well-known/agent-card.json).

3

In nostr, community additions to the protocol are called [NIPs](<https://github.com/nostr-protocol/nips>), they act as suggestions rather than mandatory implementation details.

4

By default the recipient’s information is always visible, it is recommended that relays only send this data to the user it is supposed to be delivered to but even then the server owners themselves have this information.

5

When the website is owned by the user, it amounts to the same thing in practice. For example if I were to launch an agent on my own server that agent will receive encrypted information that only I can access but if I use a third party agent host that third party will be able to see unencrypted messages.

6

Specifically, even when communicating in an end to end encrypted way over a nostr relay, the user on the receiving end needs a way to find their mail so it becomes very hard to hide the recipient’s public key without breaking communication.

7

Similar ideas have been explored by <https://openmined.org/> and they are a partial inspiration for this piece.
