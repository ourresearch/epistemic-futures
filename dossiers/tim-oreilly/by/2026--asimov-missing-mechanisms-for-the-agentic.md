---
title: "Missing Mechanisms for the Agentic Economy"
person: tim-oreilly
section: by
type: blog-post
year: 2026
date: 2026-04-01
venue: "Asimov’s Addendum"
authors: "Tim O'Reilly"
source_url: https://asimovaddendum.substack.com/p/missing-mechanisms-for-the-agentic
retrieved: 2026-08-13
content: full-text
notes: "Subtitle: “From disclosures to protocols to markets”. Asimov’s Addendum, the Substack of Tim O’Reilly and Ilan Strauss on AI commercialization risks and governance; published CC BY 4.0. Retrieved from the free public post page."
---

# Missing Mechanisms for the Agentic Economy

## Full text

_This was originally published on[O’Reilly Radar](<https://www.oreilly.com/radar/the-missing-mechanisms-of-the-agentic-economy/>). _

[](<https://substackcdn.com/image/fetch/$s_!PtlF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1d1eb9d9-81e0-4d77-b753-e45f5b5c71d7_1690x956.png>)

_For the past two years, I’ve been working with economist Ilan Strauss at the[AI Disclosures Project](<https://ai-disclosures.org/>) (joined soon after by computer scientist Sruly Rosenblat). We started out by asking what regulators would need to know to ensure the safety of AI products that touch hundreds of millions of people. We are now exploring the missing mechanisms that are needed to enable the agentic economy._

_This essay traces our path from disclosures through protocols to markets and mechanism design (read more on our new website:[here](<https://ai-disclosures.org/>)). Rather than simply stating our conclusions, I’m sharing our thought process and some of the conversations and historical examples that have shaped it._

_We will be holding a number of[focused convenings](<https://ai-disclosures.org/>) to explore these ideas over the next couple of months, and my hope is that shared context will enable more productive engagement with what is very much a work in progress._

## **The disclosure problem**

Ilan Strauss and I started the [AI Disclosures Project ](<https://ai-disclosures.org/>)in early 2024 with a conviction that most regulators had little idea how AI worked or where it was going. The field was so young that many of the early regulatory proposals were misguided. We thought that regulators and industry should start by agreeing on standards for disclosure, so that we could all learn together as the technology develops. You can’t regulate what you don’t understand.

One of our first insights was that focusing solely on model safety was a mistake, much as if regulators inspected automobiles at the factory but completely ignored their use on the roads. We believed (and still do) that the focus should be on AI _as deployed_. And we believe that disclosures shouldn’t focus just on capabilities but on business models and the operating metrics that AI companies use to shape how their products operate.

Ilan and I had worked together previously with Mariana Mazzucato at University College London on what we called “[algorithmic attention rents](<https://www.cambridge.org/core/journals/data-and-policy/article/algorithmic-attention-rents-a-theory-of-digital-platform-market-power/D85FE41F6CF99FC57DDFB2B2B63491C5>),” studying how platforms like Amazon and Google control user attention to extract economic rents from their suppliers. We observed that organic search at Google and Amazon was a huge advance in market coordination, using hundreds of signals to find the best match for a user’s intent. In effect, both companies had built a better “invisible hand.” And yet after decades of success, [they turned away from that advance](<https://www.oreilly.com/radar/rising-tide-rents-and-robber-baron-rents/>). To use Cory Doctorow’s coinage, they began “[enshittifying](<https://www.versobooks.com/products/3341-enshittification?srsltid=AfmBOooTtLlbEhhK-ia-eHz8YiuKQ610OYjsDzsl1fGjHdPTQk1SVdk_>)” their services by substituting inferior paid results for the top organic search results in order to pad their bottom line.

We’d also watched social media start out with the promise of keeping you in touch with your friends and foster productive conversations, but then instead began to optimize for engagement at the expense of everything else. By the time anyone understood what was happening, the damage had been done. We can see the inflection point in their financial metrics, but neither regulators nor the public can see the changes in operating metrics that drove the financials. What if we could capture what good looks like before it gets enshittified, and identify how that changes over time?

[We also observed](<https://www.ucl.ac.uk/bartlett/sites/bartlett/files/oreilly_strauss_mazzucato_2023.regulating_big_tech_through_digital_disclosures.pdf>) that modern technology companies are completely different from industrial era corporations, where you can understand key elements of the business by tracing the inputs and the outputs through the financial statements. Instead, the business is largely driven by intangibles, which are lumped into one impenetrable black box.

We wanted to learn from that mistake. While the horse was already out of the barn on search and social media, we hoped to get disclosure of operating metrics into AI governance while there was still an appetite for regulation. Unfortunately, that window was very short. The failure turned out to be productive, though, because it forced us to think harder about regulation more broadly and what other leverage points might be found.

_Thanks for reading Asimov’s Addendum! Subscribe for free to receive new posts and support our work._

Subscribe

## **Protocols as functional disclosures**

The first turn in our thinking came when we realized that disclosures aren’t just informational. The most important disclosures are _functional_. We came to see the parallels between disclosures and communications protocols, the agreed-on methods by which networked systems share information. For example, the HTTP protocol that underlies the World Wide Web specifies how a web browser and web server communicate in order to display a web page.

This is a structured communication with rules that must be followed and data that must be exchanged in a particular order. An HTTP request that identifies the user agent as a command line program such as curl rather than a graphical browser such as Chrome triggers a different response from the server. The user-agent string isn’t a report filed with a regulator. It’s an operational signal embedded in the protocol, and it carries a lot of information.

Once you see protocols as a system of functional disclosures, you start noticing that every regulatory system has a kind of communications and control protocol at its heart. Generally Accepted Accounting Principles (GAAP) or IFRS, the European equivalent, are protocols for communication between companies and their accountants, auditors, banks, investors, and tax authorities. Even road markings and road signs are a communications protocol, giving information to drivers about local conditions, laws, and the proper use of the road. These are slow, analog protocols, but they are protocols nonetheless.

Protocols can be inspected. Observability is the key to governance. Police observe speeders on the road; credit card processors and banks watch for credit card fraud on their payment networks; email processors filter spam as it passes through nodes on the network. The [observability](<https://learning.oreilly.com/library/view/observability-engineering/9781492076438/>) points for AI are still emerging, but that’s where regulators should be focused.

Even beyond being a locus for observability and regulability, protocols themselves do an enormous amount of the governing work in modern technology systems. Spanning everything from how packets get from one place to another to what gets displayed, who has permission to see it, and sometimes even what it costs, they ultimately determine who can interoperate with whom. That led us to an even bigger realization.

## **Protocols shape markets**

Think about the early shape of the AI chatbot market. It was a winner-takes-all race to be the dominant platform for AI in the way Windows became the platform for PCs, or iOS and Android for phones. Whoever wins controls the market. Then Anthropic introduced [MCP](<https://www.anthropic.com/news/model-context-protocol>), the Model Context Protocol. All of a sudden, the landscape looked more like a web. There could be many winners. It didn’t matter what model you were running or whose APIs you were calling as long as you followed the protocol. And as the agentic AI market unfolded, the protocol wasn’t just MCP. An AI agent could be a user of the existing internet protocol stacks. Whether MCP itself survives or is superseded by other protocols, the shape of the market was transformed.

This insight reframed our whole project. Protocols are not just technical infrastructure. They are market-shaping mechanisms.

[](<https://substackcdn.com/image/fetch/$s_!y9G4!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff8e61ef2-d328-4ba6-9a55-8dd3cadcf5df_1200x961.jpeg>)DoubleClick logo. Click-based advertising was a core mechanism that aligned competing incentives (at least initially) in the new digital economy and opened up incredible market opportunities on the back of advertising business models.

## **Workflows are also protocols**

I talked last week with some of the folks working on the Long Now Foundation’s partnership with Ethereum’s [Summer of Protocols](<https://summerofprotocols.com/>) project (soon to be: Protocolized magazine), and that widened my lens even further.

When software people hear “protocol,” we think of communication protocols: TCP/IP, HTTP, MCP, or, say, Stripe’s Machine Payment Protocol (MPP).

To this particular protocol research community, a protocol is any standardized way of doing something. Wildfire management teams follow protocols. So do flood response teams, hospital emergency rooms, and air traffic controllers. Atul Gawande’s book _[The Checklist Manifesto](<https://atulgawande.com/book/the-checklist-manifesto/>)_ was an attempt to establish a common protocol for surgical operating theaters. This is a very different definition of protocol, and yet putting the two meanings of the word into the same frame makes a new kind of sense.

In his introduction to the Summer of Protocols’ _[Protocol Reader](<https://summerofprotocols.com/protocol-reader>)_ , Venkatesh Rao cited Ethereum researcher Danny Ryan’s definition of a protocol as a “stratum of codified behavior” enabling coordination. He pointed out that protocols tend to become invisible once adopted. Rao calls this a “Whitehead advance,” after the philosopher Alfred North Whitehead’s observation that civilization advances by extending what we can do without thinking.

But he also made the thought-provoking point that a protocol is an “engineered argument,” in contrast with an API, which he says is an “engineered agreement” enforced by one dominant actor. There’s more to it than just the power asymmetry of enforced agreement, though. In a followup conversation, Venkatesh Rao noted that protocols are “not just codified modes of information exchange, but modes of live, structured, argumentation, often with an active computational element. For example, CSMA/CD (Ethernet) must detect packet collisions and compute and execute a random delay for retransmittal of packets. This is not mere structured communication. This is argumentation with what philosophers call dynamic semantics.”

Rao continued: “The moment you go beyond computing protocols, real-world feedback loops from material consequences become really important. For example, container-shipping is quite close architecturally to TCP/IP (the big difference being that packets can be dropped and retransmitted while lost containers are actually lost), but because it has a materially embodied feedback loop, regulatory mechanisms start to behave more like control systems than communication systems.”

I love the idea of protocols as an engineered argument. The dynamism this suggests is going to be ever more true in a future of agentic protocols. But this notion also triggered another thought, which is that _markets are also engineered arguments_. My bridge to this reformulation was the difference between _de jure_ protocols that arise from a formal standards process, and _de facto_ protocols that arise through market contention.

In the early days of the internet, the Internet Engineering Task Force (IETF) was all about engineered arguments. People had ideas about how the internet ought to work, and to prove their point they had to show up with interoperable implementations. No one had the ability to enforce anything. Agreement had to evolve. As Dave Clark famously put it, “[We reject: kings, presidents, and voting. We believe in: rough consensus and running code](<https://ieeexplore.ieee.org/document/1677461>).” The _de facto_ protocols of the internet that emerged from the IETF ended up significantly outperforming the competing _de jure_ networking protocols that emerged from telecommunications standards bodies. The IETF framed the argument; whoever showed up made their case and won or lost by way of adoption.

It also made me remember another decades old story that I had lived through. Microsoft and Netscape were duking it out in the web server market and were building their own “engineered agreements” for what was up the stack from the base web server functionality. Everyone thought that Apache wasn’t keeping up, but they had a trump card. They provided an extension layer. And that engineered all kinds of productive arguments between a market of competing developers rather than a single engineered agreement imposed by either a dominant player OR a dominant committee.

Rao also noted that protocols spread slowly but become nearly impossible to dislodge once established. For example, SMTP (the protocol for email) dates back to 1982, and has outlasted many competitors. There is a lot of path dependence. And so getting the first steps right is an important part of engineering the argument.

And in his essay “[Standards Make the World](<https://summerofprotocols.com/research/standards-make-the-world>)” for the Summer of Protocols project, David Lang makes the point that technical standards form a third pillar of modern society, alongside private organizations and public institutions. They aren’t the state and they aren’t the market, but they’re essential to both. When they work well, standards become enabling technologies. The internet. The shipping container. Standard time. They are civilizational infrastructure.

In short, we are not just building communication protocols for software agents. We are developing a new way to standardize the best practices and workflows that will shape the human + AI future, allowing humans and agents to cooperate across organizations, industries, and borders.  

[Share](<https://asimovaddendum.substack.com/p/missing-mechanisms-for-the-agentic?utm_source=substack&utm_medium=email&utm_content=share&action=share>)

## **Skills can also be seen as protocols**

Once the _Summer of Protocols_ team (Venkatesh Rao and Timber Schroff) planted in my mind the connection between workflows and protocols, it occurred to me that Agent Skills are also a “stratum of codified behavior,” and perhaps even a set of competing “engineered arguments” for how to do work with AI.

At the simplest level, a Skill is a piece of structured knowledge: here’s how to create a Word document; here’s how to extract the text from a PDF; here’s how to publish on the [Hugging Face Hub](<https://huggingface.co/docs/hub/index>). There can be many Skills that attempt to codify the same knowledge, but some may be better than others. As Skills multiply, how will we find the best ones? This is in many ways analogous to the organic web search problem, which Google solved by aggregating hundreds of useful signals.

And we’re seeing that there is a kind of hierarchy of skills. Jesse Vincent’s [Superpowers](<https://github.com/obra/superpowers>) [framework](<https://blog.fsck.com/2025/10/09/superpowers/>), which has become one of the most widely adopted open source projects in AI-assisted development, doesn’t just give agents individual capabilities. It encodes an entire software development methodology: brainstorm before you build, plan before you code, test before you ship, review before you merge. That’s a standardized workflow. It’s a lot like the kinds of protocol that the _Summer of Protocols_ folks were talking about with us and the _Long Now Foundation_ , expressed in a form that agents can follow.

The existing protocols that the protocol research community talks about, like wildfire management protocols or hospital triage protocols, encode best practices into a repeatable, teachable process for human teams. They have yet to be adapted for agents. And in fact, many of them are never going to be entirely agentic. We will need to build mechanisms for workflows that include both AI agents and humans working together.

Agent skills in some (but not all) areas raise the same questions that industrial standards have always raised: who decides what the best practice is? How do you verify quality? How do you govern updates? We may be talking about skills that encode the workflow for regulatory compliance in a specific industry, or for conducting an environmental impact assessment, or for managing a clinical trial. Are the standards _de jure_ or _de facto_ , the result of an engineered agreement by a committee or an engineered argument that enables a vibrant market?

At O’Reilly, this is something we think about a lot. We’re a company built on codifying expert knowledge. We’ve published books and organized conferences and online training that taught people how to do new things. Now we’re asking “What does it look like to publish the skills that teach agents how to do things? And how do we make sure those skills are discoverable, trustworthy, and monetizable, not just for us but for every domain expert who has knowledge worth encoding?” And how do they emerge from contention in a vibrant market rather than by decree?

We believe we’ll all be better off with an engineered argument than an engineered agreement. And that brings me to mechanism design.

## **The missing mechanisms**

Economists use the term “mechanism design” to describe the engineering of rules and incentive structures that lead self-interested actors to produce outcomes that are good for everyone. It’s sometimes called “reverse game theory.” Rather than analyzing the equilibria that emerge from a given set of rules, you start with the outcome you want and work backward to design the rules that will get you there.

Mechanism design theory got its start in the 1960s when Leonid Hurwicz took up the problem of how a planner can make good decisions when the information needed to make them is scattered among many different people, each of whom has their own interests. His key insight was that people won’t reliably reveal what they know unless it’s in their interest to do so. So how do you design a system that aligns their incentives?

The field that Hurwicz founded and that Eric Maskin and Roger Myerson developed through the 1970s and 80s earned all three the Nobel Prize in Economics in 2007.

I first encountered the field when Jonathan Hall, at the time the Chief Economist at Uber, waved Al Roth’s book _[Who Gets What — and Why](<https://www.amazon.com/Who-Gets-What-Why-Matchmaking/dp/0544705289>)_ at me and said “This is my Bible.” In it, Roth describes his own work on mechanism design, which won him the 2012 Nobel Prize in Economics along with Lloyd Shapley. Roth applied mechanism design to kidney matching markets, markets for college admissions, for law clerks and judges, and for hospitals and medical residents. When I first talked to Jonathan and then Al Roth, my layman’s takeaway about mechanism design was that it was simply the application of economic theory to design better markets.

And I’ve since come to think even more broadly about what mechanism design might mean in a technology context. In my broader framing, packet switching was a breakthrough in mechanism design. So for that matter was TCP/IP, the World Wide Web, and [the protocol-centric architecture of Unix/Linux](<https://en.wikipedia.org/wiki/The_Unix_Programming_Environment>), which enabled open source and the distributed, cooperative software development environment we take for granted today. PageRank and the rest of Google’s organic search system also seems to me to be a kind of mechanism design. So do Pay Per Click advertising and the Google ad auction. All of them are ways of aligning incentives such that self-interested actors produce outcomes that are good for others as well.

So that brings me back to AI. Right now, there’s a problem that makes the AI/human knowledge market less efficient than it could be. The disrespect for IP that has been shown by the AI labs and applications during the training stage, and even now during inference, has led to efforts by content owners to protect their content from AI. Do not crawl. Lawsuits. Reluctance to share information. Even the AI labs are complaining about the theft of their IP and trying to protect their model weights from distillation.

It’s an economy crying out for mechanism design.

The lesson of [YouTube Content ID](<https://support.google.com/youtube/answer/2797370?hl=en>) is worth learning. Twenty-odd years ago, the music industry was in the same position that content creators are in today with AI. In response to unauthorized use of their music by creators, music publishers’ demand to YouTube was “Take it down.” But as Google engineer Doug Eck explained to me, YouTube came up with a better answer: “How about we help you monetize it instead?” I don’t know the details of how that decision was made but I do know the eventual outcome. Aligned incentives led to a vibrant creator economy in which YouTube’s video creators, the music companies, and Google all got to share in the value that was created.

That should give us inspiration for how to solve some of the problems we face now with AI. Whether it’s with Agent Skills, NotebookLM, or other emergent artifacts of the new AI/human knowledge economy, we need to align the incentives. If we can grow the pie, and in a way where no single gatekeeper captures the bulk of the benefit, there’s a way to create a vibrant market. But that requires building mechanisms that don’t exist yet.

What mechanisms are missing from the agentic economy? Here’s a partial list:

**Skills markets.** There’s an enormous economic opportunity for humans to create and trade skills that agents can use. These are not just simple aggregation of context with tool use instructions, but higher-level, industry-specific workflows that encode deep human expertise. At O’Reilly, we’re figuring out how to turn our knowledge and that of our authors into skills, how to make them discoverable, and how to sell them. But as of yet, there’s no way for a broader community of skill creators to participate.

**Quality and governance for skills.** Some skills will need the same kinds of governance that industrial standards have. Who certifies that a medical skills package follows current clinical guidelines? Who updates it when the guidelines change? We haven’t begun to build the institutions that would govern agent skills at that level.

**Registries and discovery.** The MCP community has been working on [a registry protocol](<https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/>), as is [the Ethereum community](<https://eips.ethereum.org/EIPS/eip-8004>).

This isn’t just a technical development but a business opportunity. I still remember when Network Solutions was running the original top level internet domain name registry under contract from the National Science Foundation. When the government said it would end the payments, Network Solutions planned to walk away. Then they realized what they had. On the early internet, domain name registration became a surprisingly big business. Now it’s just boring civilizational infrastructure. Is there something similar for AI models, applications, and agents?

**Organic search for agents.** Google’s first great innovation on the web wasn’t how to make pay per click ads really work with a data-driven ad auction. It was organic search: a way of coordinating a market with hundreds of signals that ignored price and worked independently of whether the destination content was free or paid. _The New York Times_ (or [oreilly.com](<http://oreilly.com>)) is subscription-based, but that isn’t a factor in whether Google shows it to you. Google figured out signals that let them say, “This is the best result for this query.” Sites behind paywalls figured out how to disclose enough for people to decide whether they wanted to take the next step and enter into a transaction. That’s an engineered argument.

We’re going to need the equivalent for skills and agent services. We’ll start with curated marketplaces. Vercel already has one. But we’re a long way from something as effective as Google’s peak in organic search. The search space will be huge, with hundreds of millions, maybe billions of agents seeking the best way to accomplish trillions of distinct tasks. Skills can help them save on inference costs and deliver better results. The question is what signals will drive discovery of the best match.

**Extension architectures.** MCP’s [extension model](<https://modelcontextprotocol.io/extensions/overview\)>) (including the new [Apps Extension](<https://blog.modelcontextprotocol.io/posts/2025-11-21-mcp-apps/>)) is promising. This is the Apache model all over again: keep the core simple, let people layer different approaches on top, and let the market sort out which ones win. It is, in essence, an engineered argument rather than an engineered agreement.

**Payment layers.** Stripe has been working on [agentic commerce](<https://stripe.com/use-cases/agentic-commerce>), but it seems to be focused on traditional e-commerce transactions like booking a ticket or buying a product. What about a payment layer for skills? There have been proposals for monetizing MCP calls, pay per call, pay per token, but none have caught on yet. Coinbase’s [x402 protocol](<https://www.coinbase.com/developer-platform/discover/launches/x402>) may also end up playing a role.

**Progressive access and authentication.**[MCP Server Cards](<https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1649>) promise to let a service specify its terms: here’s what we charge, here’s how you authenticate. That’s a functional disclosure layer that could enable commerce. It could enable progressive privileges: a free O’Reilly subscriber gets one set of tools, a paying subscriber gets a richer set, all on top of the same MCP server. Again, that’s an engineered argument with the market deciding the winners.

**Neutrality in agent routing.** When ChatGPT decides to show you a Booking.com widget instead of an Airbnb widget, who made that choice, and on what basis? OpenAI claims commercial considerations aren’t a factor. That’s hard to take at face value. We need something like the original principle of organic search: surface the best result for the user, not the most profitable one for the platform.

## **We don’t know the future, but we can set ourselves up to shape it for the better**

I’m old enough to remember when UUCP was giving way to the internet, and there was a real debate over whether explicit path routing or domain routing was better. In retrospect, it’s blindingly obvious that path routing wasn’t going to scale. But it’s worthwhile to know that at the time, people weren’t at all clear about that!

The same is true now. Some of what I’ve described will turn out to be the equivalent of explicit path routing: a dead end that was only plausible for a small scale network. Other parts will turn out to be as fundamental as DNS or HTTP. But we’re not trying to pick the winners. We’re trying to engineer the argument.

If we can enable better markets, it will allow a process of discovery. People try different things, most fail, some catch on. The job right now is to build the mechanisms that help the market to evolve.

We need mechanisms that no single gatekeeper can control. Modular, decentralized architectures let people experiment with business models, routing decisions, payment systems, and quality signals. And alongside those markets, we will eventually need institutions (some of which will be protocols) to maintain standards that will become the infrastructure of the next economy.  

Subscribe

* * *

 _This article recapitulates a conversation with Ilan Strauss and Ido Salomon, and a separate conversation on the broader meaning of protocols in the context of industry workflows and civilizational infrastructure with Venkatesh Rao and Timber Schroff of the Ethereum Foundation’s Summer of Protocols program, and Denise Hearn and James Home of the Long Now Foundation. Rao’s_ Protocol Reader _and David Lang’s “Standards Make the World,” published through the Summer of Protocols project, inform the argument about protocols as civilizational infrastructure._
