---
title: "Open Protocols Can Prevent AI Monopolies"
person: tim-oreilly
section: by
type: essay
year: 2025
date: 2025-07-30
venue: "AI Frontiers (Guest Commentary)"
authors: "Isobel Moure; Tim O'Reilly; Ilan Strauss"
source_url: https://ai-frontiers.org/articles/open-protocols-prevent-ai-monopolies
retrieved: 2026-08-13
content: full-text
notes: "Retrieved from ai-frontiers.org; openly readable. Companion to the SSRC AI Disclosures Project working paper \"Protocols and Power\". Trailing site chrome and related-article list removed."
---

# Open Protocols Can Prevent AI Monopolies

## Full text

# Open Protocols Can Prevent AI Monopolies

## With model performance converging, user data is the new advantage — and Big Tech is sealing it off.

Jul 30, 2025

[Isobel Moure](</author/isobel-moure>)

[Tim O'Reilly](</author/tim-oreilly>)

[Ilan Strauss](</author/ilan-strauss>)

Guest Commentary

Can we head off AI monopolies before they harden? As AI models become commoditized, incumbent Big Tech platforms are racing to rebuild their moats at the application layer, around **context:**__ the sticky user- and project-level data that makes AI applications genuinely useful. With the right context-aware AI applications, each additional user-chatbot conversation, file upload, or coding interaction improves results; better results attract more users; and more users mean more data. This **context flywheel** — a rich, structured user- and project-data layer — can drive up switching costs, creating a lock-in effect that effectively traps accumulated data within the platform.

‍**Protocols prevent lock-in.** We argue that open protocols — exemplified by Anthropic’s Model Context Protocol (MCP) — serve as a powerful [rulebook](<https://asimovaddendum.substack.com/p/disclosures-i-do-not-think-that-word>), helping to keep API-exposed context fluid and to prevent Big Tech from using data lock-in to extend their monopoly power. However, as an [API wrapper](<https://www.reddit.com/r/mcp/comments/1kglwnk/mcp_as_api_wrapper/>), MCP can access only what a particular service (such as GitHub or Slack) happens to expose through its API.  
To fully enable open, healthy, and competitive AI markets, we need complementary measures that ensure protocols can access the full spectrum of user context, including through: 

1\. Guaranteed access, for authorized developers, to user-owned data, through open APIs at major platforms.   
2\. Portable memory that separates a user’s agentic memory from specific applications.   
3\. Guardrails governing how AI services can leverage user data.

Drawing on the example of open-banking regulations, we show that security and data standards are required for any of these proposals to be realized. 

Architecting an open, interoperable AI stack through the protocol layer is about supporting broad value creation rather than value capture by a few firms. Policy efforts such as [the EU’s General-Purpose AI Code of Practice](<https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai>) do matter; but, ultimately, it is software architecture that most immediately and decisively shapes market outcomes. **Protocols** — the shared standards that let different systems communicate with one another — function as a deeper _de facto_ law, [enabling](<https://asimovaddendum.substack.com/p/disclosures-i-do-not-think-that-word>) independent, decentralized, and secure action in digital markets.

## From Commoditized Models to Context-Rich Applications 

**From models to services.** In a fevered race to blitzscale its way to AI dominance, OpenAI took an early lead. ChatGPT became the fastest-growing application in history, and it was easy to assume that the next step was to turn it into a platform. OpenAI [attempted to become](<https://www.understandingai.org/p/how-ai-agents-got-good-at-using-tools>) a developer platform, first with plugins and then with its GPT Store. 

But it hasn’t all gone according to plan. OpenAI’s models don’t seem so special anymore. Open-source models like [Kimi K2](<https://github.com/MoonshotAI/Kimi-K2>) (by Moonshot AI) have competitive capabilities and are free to use. Sensing the turning tide, application-specific companies like Perplexity struck gold by taking off-the-shelf models from multiple providers, scaffolding them for specific uses, and charging for premium access while avoiding vendor lock-in. Cursor, an AI‑first code editor, went from $0 to [over](<https://techcrunch.com/2025/06/05/cursors-anysphere-nabs-9-9b-valuation-soars-past-500m-arr/>) $100 million ARR in 18 months, proof that context‑driven retrieval-augmented generation (RAG), with a native AI design, can beat incumbents sitting on more user data. Front-end users can now easily choose their preferred model within these applications. And, using platforms like [OpenRouter](<https://openrouter.ai/>), developers can even switch models dynamically in response to pricing or features. 

**Context rising.** As foundation models commoditize, competition is shifting up the stack, to the application layer, where proprietary user and project data — known as context — is the secret sauce. Tech giants are [racing to enclose](<https://news.bloomberglaw.com/us-law-week/ai-companies-are-charting-a-path-to-lock-users-in-for-life>) and own this context exclusively: conversation histories, memory stores, workspaces, codebases, documents, and anything else that helps their agents predict and assist better. OpenAI, Google, and other model vendors lean on chatbot interaction logs as sources of persistent memory, while application specialists like Anysphere (which makes Cursor) and Perplexity similarly harness project and user data to boost their models’ usefulness.

This forces a crucial decision on the market: will AI applications grow based on closed standards that let a few gatekeepers dictate terms and extract outsized rents, or on open standards that keep context portable and architecture permissionless?

**The early open web.** The stakes are high. [Born on open protocols](<https://en.wikipedia.org/wiki/Code:_Version_2.0>), the web evolved into ecosystems of applications dominated by Amazon, Google, and Meta. At first, they beat rivals simply by working better. Google was the best at matching searchers with information and ads; Amazon surfaced the best products at low prices; and Facebook matched its users with a unique feed crafted only from content shared by their friends and people they chose to follow.

**From innovation to extraction.** But success conferred durable power that was abused. As growth slowed, the winning companies shifted from creating value to extracting it. In [our past work](<https://www.ucl.ac.uk/bartlett/public-purpose/research-institute-innovation-and-public-purpose/digital-technology-and-artificial-intelligence/algorithmic-attention-rents>), we described this process using the language of economic rents: winners first gain “Schumpeterian rents” for innovation, but, once markets mature, these turn into extractive rents aimed at preserving dominance and squeezing users and developers. The author, blogger, and tech activist Cory Doctorow frames this process vividly as “[enshittification](<https://en.wikipedia.org/wiki/Enshittification>).” AI’s enshittification could involve weaker safety guardrails, higher prices, less user privacy, and lower-quality information or agentic assistance. In short, when commercial incentives go unchecked, models get tuned to serve providers’ interests over those of users.

Attempts by OpenAI to build a platform by locking in developers and users resemble Facebook’s failed attempt to build a platform. But, as Bill Gates is [said](<https://stratechery.com/2018/the-bill-gates-line/>) to have commented: “ _This isn’t a platform. A platform is when the economic value of everybody that uses it exceeds the value of the company that creates it. Then it’s a platform_.” That kind of platform is almost always enabled by open standards. By contrast, when a company blocks others from linking compatible products to its ecosystem, it incentivizes customers to use several services at once (“multi-homing”), and invites extra scrutiny from regulators.

**The promise of protocols.** Anthropic has taken a different route, developing MCP as an open protocol, a shared set of rules that anyone can use for free. MCP standardizes how AI applications request information and actions from external services, thereby facilitating equitable developer access to external tools and data context _._ This is how networked markets grow: by enabling [an architecture of participation](<https://www.oreilly.com/radar/an-architecture-of-participation-for-ai/>) through which every new entrant makes the market more valuable for everyone else.

/inline-pitch-cta

MCP’s take-up has been explosive. Today there are well over [5,000 MCP](<https://www.pulsemcp.com/servers>) [servers that](<https://www.pulsemcp.com/servers>) can connect to the [hundreds](<https://www.pulsemcp.com/clients>) of AI apps that have integrated MCP. Faced with rapid adoption by third-party developers, AI model developers like OpenAI and Google have announced that they too will support MCP. But these same incumbents are already pushing back.

## How User Context Is Powering a New Era of Tech Monopolies — and Competition

**How context creates value for users.** AI systems thrive on context: the user data that lets an AI system tailor its behavior to users, their requests, and the tasks at hand. When [properly mined](<https://www.theinformation.com/articles/data-is-the-new-sand?rc=7em78a>), this user data allows for personalized and efficient predictions. Think of a context-free, factory-settings AI model as a borrowed phone: the hardware is powerful, but, without your contacts, messages, location, and logins, it can’t really help you. 

Context has many layers: _across time,_ as a living “state,” such that each user prompt builds on what came before; and _across people_ ,__ as a multi-user setting (say, in a Slack thread or collaborative document). We emphasize two layers: _micro-context_ captures whom the system is helping right now (associated with their preferences, language, and current query). On the other hand, _macro-context_ covers the task environment, as the external frame that shapes what a sensible answer looks like. This includes project files and live data feeds. 

**The allure of user lock-in.** Big AI companies are using context to grow their moats and [lock in users](<https://news.bloomberglaw.com/us-law-week/ai-companies-are-charting-a-path-to-lock-users-in-for-life>) through at least two approaches.

The first is through product bundling. Examples include OpenAI’s push into search, research, and coding (including through [acquisitions](<https://www.theverge.com/news/703114/openai-io-jony-ive-sam-altman-ai-hardware>)); Google’s threading Gemini into Workspace; Microsoft’s embedding Copilot across its 365 productivity apps. Bundling aggregates the data surface and raises switching costs.

The second approach is through building context as a central product feature. OpenAI now offers persistent memory that stores personal details (e.g., “has a child” or “diagnosed with ADHD”) to shape future replies. Meta has announced it will collect cross-site user data to personalize its AI assistants. Google now remembers your writing style, so it can tune its AI-generated Gmail replies. By binding the app and its context to the model, companies lock in users and starve rivals. Such bundling is fertile ground for enshittification.

Importantly, this process relies on Big AI companies’ gathering __**explicit __** user signals __ — their prompts, docs, API calls — and distilling them into an **inferred** , implicit __ preferences __ profile that lets their model deliver more relevant, efficient predictions inside each user’s unique workspace. 

## Can Protocols Create a Level Playing Field? 

**How MCP works.** Anthropic’s MCP standardizes how AI applications request tools, data, and actions from external services through a universal adapter. Instead of custom integrations for each pairing (Cursor → GitHub; Claude → Google Drive), any AI app (each one an MCP client) can use any MCP-compatible service (**or** MCP server), making models more interchangeable. MCP also creates an agentic interface that allows an AI agent to decide _what_ to do, based on the language of tasks, not endpoints. This reduces the MxN [integration tax](<https://news.ycombinator.com/item?id=44063141>), allows small firms to rent rather than build tooling, and weakens vertical exclusives.

Because MCP is client-agnostic, any AI app can use any external service, which in turn makes switching between models far easier — either by switching between model service providers that support MCP, or by building an independent MCP client and using any model service. When an AI app’s context is portable, models become more interchangeable.

_MCP is the ultimate_** _unbundler_** _of context_ : any compatible AI app can reach any service that exposes an MCP server, allowing an enriched prompt to then be sent to the model. But services must still opt in, by making their content available through [APIs](<https://systemsapproach.substack.com/p/why-apis-matter>).

This shifts the competitive gravity “up the stack,” away from the model developers and to the application that develops the winning context flywheel. App-level data portability and governance — including pricing, permissioning, and any [preferential](<https://techcrunch.com/2025/04/15/anthropics-claude-now-read-your-gmail/>) access into Big Tech-controlled data sources — then becomes the new battleground. 

Although MCP reduces integration friction, interoperability alone doesn’t ensure market competition. We’ve seen this before: open protocols like HTTP (for web browsing) and SMTP (for email) enabled permissionless entry of new applications, yet markets still tipped. Google is now the dominant email and browser provider because of its superior products and cross-app integrations.

## MCP’s Impact on the AI Market So Far 

**Users prefer AI-native tools.** Incumbents have rushed to insert AI into every legacy product: the quickest go-to-market strategy with the shallowest integration. Meta surfaces an assistant in nearly every app. This has only made building cleaner, MCP-enabled applications far more attractive. AI-native tools like Perplexity offer further encouragement to developers, showing that users will pick a customized experience over a retrofitted one (like the AI-layered Google Search).

/odw-inline-subscribe-cta

Unsurprisingly, the number of new MCP servers has rocketed, as we [noted earlier](<https://www.pulsemcp.com/servers>). However, such integrations may also be boosting usage of incumbent model developers’ chatbots as they gain access to more tools. MCP’s impact has been impeded by its [weak](<https://auth0.com/blog/an-introduction-to-mcp-and-authorization/>) security. The external [authentication and authorization](<https://news.ycombinator.com/item?id=44063141>) of MCP servers remains a stubborn MxN integration problem. Moreover, for [repeated production workflows](<https://lucumr.pocoo.org/2025/7/3/tools/>), code-based frameworks may be more efficient than an inference‑only workflow.

**Incumbents resist interoperability.** Lastly, there are early signs that AI model developers may resist interoperability more broadly, despite the increased usage it generates for them, if it ends up reinforcing the context moats for application developers. Anthropic temporarily [cut off](<https://techcrunch.com/2025/06/05/anthropic-co-founder-on-cutting-access-to-windsurf-it-would-be-odd-for-us-to-sell-claude-to-openai/>) the coding application Windsurf’s direct (first-party) access to its high-performing Claude models. Windsurf was growing too popular and was set to be acquired by OpenAI, a [direct competitor](<https://techcrunch.com/2025/06/05/anthropic-co-founder-on-cutting-access-to-windsurf-it-would-be-odd-for-us-to-sell-claude-to-openai/>) to Anthropic.

## MCP vs. Walled Gardens: The API Gatekeeping Problem

APIs are gateways through which MCP clients — the AI applications — access third-party data and tools, thereby breaking down a platform’s “walled garden” of proprietary services and datasets. MCP can liberate context only when a third-party service offers a sufficiently rich API (and keeps it open). Because platform owners control those APIs, they have an incentive to constrain what MCP can touch, to protect their competitive edge. This manifests in two ways:

1\. **Access risk.** Services can simply shut off API access entirely, or they can greatly degrade access. Recent API paywalls and shutdowns at Reddit, Twitter, and Meta show how access can vanish overnight. Enterprise services like Salesforce (which owns Slack), Atlassian, and Notion are [now limiting](<https://www.theinformation.com/articles/corporate-data-wars-intensify>) API access by Glean (a context platform) even as they launch competing products. Meanwhile, Slack’s [new API ](<https://www.reddit.com/r/Slack/comments/1ldwc5n/slack_api_updates_coming_in_september/>)changes (supposedly to limit how LLMs are able to access the app) will harm developers in general.  

2\. **Context-depth risk (the “personalization gap”)**.**** Platform APIs expose posts and files but rarely the behavioral profiles that power their own personalization, leaving newcomers with a cold‑start handicap. Meta, for example, [personalizes its own chatbot](<https://techcrunch.com/2025/01/27/meta-ai-can-now-use-your-facebook-and-instagram-data-to-personalize-its-responses/>) with Facebook and Instagram history, but it offers third parties neither its Graph API to fetch that full profile nor access to detailed aspects of users’ explicit and implicit (inferred) profiles. Similarly, OpenAI’s “memory” feature is [confined](<https://community.openai.com/t/how-do-i-enable-or-disable-memory-in-api/703964?utm_source=chatgpt.com>) to ChatGPT. OpenAI does not allow developers to access a user’s “memories” via an API, even with the user’s prior consent.

## To Save AI from Enshittification, Support Protocol-Level Interventions

**Improving protocols for the AI age.** To break API gatekeeping in AI markets, we need an architecture that supports user-sanctioned data [portability](<https://dtinit.org/blog/2025/02/11/future-of-AI-portability>) in order to enhance third-party developer access. Here, portability means end users’ ability to read and transfer their data across platforms - _or to allow other developers to do so on their behalf_. When portability is universal, developers can access the same context (through MCP or any API) without negotiating bespoke deals. To operationalize this approach for AI markets, we recommend:

**1\. Open API access for major platforms**.**** If the data comes from the user, the user (and any developer the user authorizes) should be able to take it elsewhere. We recommend requiring that, with user consent, major platforms expose this user-owned contextual data through APIs to accredited developers with user consent, at zero cost. We propose starting with the platforms that control the most user context: “gatekeepers” designated by EU criteria, plus major AI model providers. 

Such an approach could draw inspiration from the EU’s open-banking law (specifically, its Second Payment Services Directive, or PSD2), which holds that banks must provide licensed fintechs with free, real-time access to core account data and payment functions. Authorized developers must first obtain a license by showing proper security and data standards. Unlike banking’s standardized records, though, AI context spans code repositories, conversations, behavioral patterns, and preferences. In the case of AI, markets and regulators would need to come up with a way of defining “core user context” for these various data types and platforms.

**2\. Memory as a portable service**. Users’ AI “memory” should be accessible across platforms via APIs, with market-driven security standards embedded in the technical architecture. Such MCP servers [already](<https://mem0.ai/openmemory-mcp>) [exist](<https://mcp.supermemory.ai/>), even if AI applications don’t support it.

The challenge is less technical than socio-economic. Memory is deeply personal and requires secure data-handling, yet AI markets currently lack standards and accreditation in these areas.

A market-driven approach would be to embed these security standards into technical architecture, as is done with the [FDX API standard](<https://financialdataexchange.org/>) for US open banking. Such embedding allows for secure and standardized sharing of financial data between banks and third-party developers. Security requirements like end-to-end encryption, [OAuth-controlled](<https://www.reddit.com/r/mcp/comments/1lgfgc6/new_mcp_update_just_dropped_heres_what_the_oauth/>) access to client-side keys, and granular topic-by-topic permissions are currently beyond [MCP’s scope](<https://auth0.com/blog/an-introduction-to-mcp-and-authorization/>). But FDX’s secure and universal API shows what is possible.

**3\. Safe personalization, without data exploitation**. Open APIs depend on users’ trusting developers to handle shared context responsibly. Industry-specific data usage rules would also weaken incumbents’ advantages while creating safer technologies. Such usage rules could start with:

  * _Data firewalls_. We recommend protecting intimate user conversations from commercial targeting. An AI application leveraging a known user preference like “is vegetarian” for restaurant recommendations is beneficial; but exploiting therapy-like conversations for manipulative advertising must be prevented.
  * _Erasure rights_. Users should be able to review, edit, or delete their preference profiles and memories at any time. ChatGPT [already](<https://help.openai.com/en/articles/8983136-what-is-memory>) largely offers this.
  * _Privacy defaults_. For sensitive queries, we recommend that AI services default to a private mode, without long-term memory enabled or ad targeting, unless users explicitly opt in to these settings for such queries. 

Ultimately, control over user context — not raw model power — will decide who wins the AI commercial race. Open protocols can keep context fluid between competitors, but they are only as effective as the data they can securely access. The choice is ours: design competitive AI markets around open principles, or accept a new generation of platform monopolies.

_Thanks to Alex Komoroske, Chris Riley, David Soria Parra, Guangya Liu, Benjamin Mathes, and Andrew Trask for reading and/or commenting on this article. Any errors are ours._

‍

** _See things differently?_**_AI Frontiers welcomes expert insights, thoughtful critiques, and fresh perspectives._[_Send us your pitch._](<https://ai-frontiers.org/publish?utm_source=aif_article>)

Footnotes

Written by

### [Isobel MoureIsobel Moure is a Researcher at the AI Disclosures Project (SSRC). She studied Cognitive Science and Computer Science at Barnard College and was a research assistant for Dr. Robert Remez.](</author/isobel-moure>)

### [Tim O'ReillyTim O’Reilly is the Principal Investigator and Co-Director of the AI Disclosures Project (SSRC). He is the founder, CEO, and Chairman of O’Reilly Media and is known for coining terms such as “Open Source” and “Web 2.0.”](</author/tim-oreilly>)

### [Ilan StraussDr. Ilan Strauss is Co-Director of the AI Disclosures Project (SSRC). He is an Honorary Senior Fellow at the UCL Institute for Innovation and Public Purpose and Visiting Associate Professor at the University of Johannesburg. He holds a Ph.D in economics from the New School for Social Research (NYC).](</author/ilan-strauss>)

Image: Chris Yang / Unsplash

Continue reading

[](</articles/ai-content-must-now-carry-a-label-cameras-are-next>)### [AI Content Must Now Carry a Label. Cameras Are Next.](</articles/ai-content-must-now-carry-a-label-cameras-are-next>)

New EU and California laws require AI companies, and eventually camera makers, to sign their media outputs. It’s our best chance to tell what’s real.

[Eddan Katz](</author/eddan-katz>)

Aug 13, 2026

[](</articles/agi-will-set-off-an-industrial-explosion>)### [AGI Will Set Off an Industrial Explosion](</articles/agi-will-set-off-an-industrial-explosion>)

If AI reaches the point where it can do the cognitive work humans do, robots will proliferate. Standard data on US industry implies a fully automated economy could double its output roughly every year, with no further breakthroughs required.

[Damon Binder](</author/damon-binder>)

Aug 11, 2026
