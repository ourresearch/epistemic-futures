---
title: "Measuring content influence in AI assistants (working paper)"
person: "alex-springer"
section: "by"
type: "report"
year: 2026
date: "2026-05-21"
venue: "OpenAttribution (Research)"
authors: "OpenAttribution (no personal byline; see notes)"
source_url: "https://openattribution.org/research/measuring-content-influence-in-ai-assistants"
retrieved: "2026-08-13"
content: "full-text"
notes: "Published under an organisational byline ('Published by OpenAttribution' / 'produced by OpenAttribution'), with no personal byline on the page. Filed in by/ because OpenAttribution Limited (UK company 17002582) has one public author: all six of the site's bylined blog posts read 'By Alex Springer', he is its founding director (Companies House, appointed 2026-01-30), and he is the sole listed contributor on every openattribution-org and SPUR-Coalition GitHub repository. Personal authorship is therefore inferred from those facts, not stated on the document itself."
---

# Measuring content influence in AI assistants (working paper)

## Full text

Open Attribution Demo PolicyCheck Docs Research Contact Get started

Research · 21 May 2026 · 35 min read

# Measuring content influence in AI assistants
A working paper on AI visibility, the GEO industry, and event-level reporting.
Published by OpenAttribution Get the PDF

# Measuring content influence in AI assistants #
A working paper on AI visibility, the GEO industry, and event-level reporting.
Published by OpenAttribution. May 2026. Revised August 2026 to align the event vocabulary with the Content Telemetry v1 draft: content_displayed became content_presented , and content_reproduced - verbatim reuse, credited or not - joined the event set.

## Summary #
The AI visibility industry - Generative Engine Optimisation, or GEO - sells prompt-monitoring scores: send the same questions to ChatGPT, Claude, Perplexity and Gemini, count brand mentions and cited URLs in the answers, repeat. The score is a useful presence signal. The retrieval pipeline behind the citation - which pages were used, what was paraphrased without credit, who should be paid - stays opaque.
Part of the missing signal already sits in content owners’ own server logs: which AI bots fetched what, when. The rest sits in the providers’ retrieval and citation logs. No one holds both halves, because there is no common reporting layer for AI retrieval events.
This paper makes the case for one. §1-3 explain how GEO measures today and why it falls short. §4 is the audit data behind the argument. §5 proposes an event model for deterministic measurement.
Three concrete moves for content owners (expanded in §6): instrument the AI bot traffic already hitting your servers - that is the retrieval event, and it is yours to capture; treat GEO scores as the presence proxy they are; push the AI providers for the events only they can see - grounding, reproduction, citation, presentation, engagement.
Disclosure: OpenAttribution publishes the specifications discussed in §5. It is a UK company limited by guarantee operating as a technical standards body.
7.8% → 2.1% AI citations from domains blocking the citing bot, depending on which bot you check 42
14.0% News-category violation rate, the highest of any vertical in the audit
38,065:1 Anthropic's mid-2025 ratio of pages crawled to visitors referred 33
11.9% Share of AI citations explained by backlink metrics, per Profound's own data 25j
1.93% Reddit citation rate, despite Reddit being 67.8% of all non-cited URLs 7
5 events The deterministic vocabulary that would replace prompt-monitoring guesswork

## At a glance #

- §1: The opaque pipeline. Between question and cited answer sits a retrieval pipeline the provider sees in full and everyone else sees in fragments.

- §2: The probabilistic visibility industry. GEO vendors mostly run prompt-monitoring runs - parsing and counting the answers, then selling the score as visibility. The score tracks presence. It does not explain cause, attribution, or who is owed what.

- §3: Four structural problems. Brands pay twice. Publishers negotiate with weak telemetry. Providers benefit from the opacity. The citation surface is easy to manipulate.

- §4: A reproducible audit. OpenAttribution’s May 2026 audit of 24,127 citations across four providers found 7.8% came from domains whose robots.txt blocks the provider’s training crawler. Check the same citations against the live-search bot the provider’s web_search tool actually uses, and the rate falls to 2.1%. The gap is the bot-taxonomy gap: publishers name the training bot in their opt-out and are silent on the live agent.

- §5: What deterministic measurement looks like. A more useful model starts with six events: content_retrieved , content_grounded , content_reproduced , content_cited , content_presented , and content_engaged .

- §6: What this means for content owners. Publishers, brands, and agencies face different decisions. All of them benefit from owning more of the measurement layer.

- §7: Where this goes next. Instrument what is already measurable. Push for a standard for the rest.
If you are only reading one section, start with §3 for the critique or §5 for the proposed measurement model. The appendices cover the full pipeline detail ( A ), glossary ( B ), audit method ( C ), and references ( D ).
Reading guide
- Publisher §3.3 (leverage), §4 (audit), §6 (publishers)

- Brand §3.1 (paying twice), §4 (audit), §6 (brands)

- Agency §2 (the GEO market), §6 (agencies)

- Standards, policy, platform §3 (problems), §5 (events), §7 (next)

## 1. The opaque pipeline #
When ChatGPT, Claude, Perplexity, or Gemini answers a question with citations, a retrieval pipeline runs between prompt and response. None of it is visible to the people whose content made the answer possible.
Figure 1. The retrieval pipeline, from prompt to cited answer. What is RAG? Retrieval-augmented generation. The model is given the user’s question, runs one or more web searches, fetches the most relevant pages, and uses the contents of those pages as context for its answer. The “retrieval” step is the part that touches your content. The “generation” step is where citations are produced.

The model rewrites the user’s question into one or more search queries. ChatGPT reportedly issues several per prompt. Google AI Mode and similar deep-research products reportedly issue dozens, sometimes hundreds. Claude exposes a max_uses parameter 1 that caps how many it can run in a turn. One question becomes many.
Each sub-query is sent to a search index. ChatGPT and Copilot use Microsoft’s Bing API; OpenAI also runs its own crawl via the OAI-SearchBot agent. Gemini uses Google Search. Claude appears to use the Brave Search API, inferred from Anthropic’s subprocessor list updated in March 2025 2 . Perplexity runs its own crawler. The entire industry sits on three or four indexes: Bing, Google, Brave, and Perplexity’s proprietary crawl. The visible competition between AI providers sits on top of those.
Returned URLs are filtered before any page is fetched. Some of the filtering is deterministic: duplicates collapsed, low-quality domains scored down, licensing blocks applied where they exist. Some is policy-driven: safety rules, defamation flags, regional law. None of it is published. From outside, the only signal is the citation that eventually appears.
What is robots.txt? A plain text file at the root of a website ( example.com/robots.txt ) that tells automated crawlers which parts of the site they may or may not access. It is advisory, not legally binding in most jurisdictions, but it is the standard way a website expresses its consent to be crawled. AI providers run multiple bots with different rulebooks, and robots.txt operates per-bot.

The bot identity matters. OpenAI runs three crawlers with different rules: GPTBot for training, OAI-SearchBot for the search index, and ChatGPT-User for live fetches 3 . Anthropic and Perplexity split their crawlers the same way. The live-fetch bot, by design, does not honour robots.txt. OpenAI made this exemption explicit for ChatGPT-User on 9 December 2025 4 . Perplexity’s documentation states that its user-fetcher “generally ignores robots.txt rules.” 5 This is a deliberate design choice.
Surviving URLs are fetched and parsed. None of the major AI crawlers run JavaScript: GPTBot, ClaudeBot, and PerplexityBot fetch raw HTML and bail 6 . Sites that depend on client-side rendering are invisible to AI search. Soft paywalls - HTML loaded but hidden by an overlay - are bypassed automatically. Hard paywalls are not.
Fetched pages are split into chunks, scored for relevance, and only the top-scoring chunks go into the model’s context window. Ahrefs’ April 2026 analysis of 1.4 million ChatGPT prompts collected in February 2025 found half of retrieved URLs end up cited (49.98% across 23.4 million URLs) 7 . Reddit pages are retrieved heavily but cited only 1.93% of the time, and account for 67.8% of all non-cited URLs. They shape answers without getting credit. Most of what is retrieved at the search step is discarded before the model ever uses it.
Reddit pages are cited only 1.93% of the time, and account for 67.8% of all non-cited URLs. They shape answers without getting credit.
Ahrefs, analysis of 1.4 million ChatGPT prompts, April 2026 7
The model generates the answer. Citations are sometimes structurally tied to the source spans they came from - Gemini publishes a groundingSupports model that links spans of the answer to specific chunks 8 . More often, citations are attached to free-text answers post-hoc. The Tow Center’s March 2025 study 9 and the larger BBC/EBU “News Integrity in AI Assistants” study from October 2025 10 both document that those citations are routinely incorrect. The BBC/EBU study found 45% of responses had at least one significant issue and 81% had an issue of some kind. Sourcing was the single largest category, with 31% of responses having significant sourcing problems.
BBC/EBU study, in detail. 22 Public Service Media organisations across 18 countries and 14 languages, evaluating 2,709 responses from the free versions of ChatGPT, Copilot, Perplexity, and Gemini. Significant issues by assistant: Gemini 76%, Copilot 37%, ChatGPT 36%, Perplexity 30%. Significant sourcing issues specifically: Gemini 72%, ChatGPT 24%, Perplexity 15%, Copilot 15%. Sourcing problems counted include claims not supported by the cited source, no source provided, and incorrect sourcing claims.

A final policy pass may modify or refuse the answer. This stage is undocumented at every provider.
No individual stage in this pipeline is broken. The full sequence as a connected chain - which queries led to which retrievals, which feeds which ranking, which fills the citation slot - is visible only to the provider. Provider APIs expose pieces unevenly: retrieval lists from Anthropic, grounding from Gemini, citation arrays from Perplexity. None of it returns as a single connected record a third party could use to reproduce what the model did. The owner of the content that made the answer possible sees fragments.

## 2. The probabilistic visibility industry #
Vendors have built a market on the gap between what content owners can see and what they need to see. It goes by Generative Engine Optimisation (GEO) - the most circulated of several competing terms, alongside AEO (Answer Engine Optimisation), AIO (AI Optimisation), LLMO (Large Language Model Optimisation), and the more literal Retrieval Optimisation. We use GEO throughout because it is what the market currently buys; the terminology is not settled.
By May 2026 the field had a recognisable cast: Profound, Peec AI, Otterly.AI, AthenaHQ, Evertune, Promptwatch, Brantial, Ahrefs Brand Radar, and Semrush’s AI Visibility Toolkit, plus over one hundred smaller tools by some counts 14c . Adobe’s $1.9 billion acquisition of Semrush 11 , completed in late April 2026 12 , signals that enterprise software now treats the category as strategic. Microsoft Clarity’s free Bot Activity dashboard, launched in January 2026 13 , and the Citations dashboard that followed in May 2026 13a , point the same way from the opposite end of the market.
Whatever the marketing, the method is the same across vendors. A platform runs a list of prompts - supplied by the user or generated by the tool - against public AI APIs, parses the answers and citations, and reports back on mentions, frequency, position, and competitors.
Used carefully, the method tells you something real. Rand Fishkin’s January 2026 SparkToro study, conducted with Patrick O’Donnell of Gumshoe 17 , ran 12 prompts past 600 volunteers across ChatGPT, Claude, and Google AI, producing 2,961 responses in total. Fishkin started from a sceptical prior and concluded that visibility-percent across many runs is a genuine signal. In the consideration sets that emerged, the top three brands appeared in 55% to 77% of responses. A brand that shows up in 70% of answers to “best running shoes for marathon training” is plainly more present in the model’s consideration set than one that shows up in 4%.
The method also helps with a second question. Some brand mentions in AI answers come from training data, not live retrieval. When ChatGPT recommends Bose alongside Sony for noise-cancelling headphones without citing a source, no retrieval event has fired; the model is recalling rather than retrieving, so there is nothing to instrument. The only way to know whether a brand belongs in the consideration set is to ask the model many times and count the answers. That is close to the role search-keyword data has long played: a probabilistic read on attention that helps decide what to make next.
The method breaks when it is asked to do attribution work. For development and ideation, the question is, “What is in the audience’s head?” For spend, the question is, “Did this specific event drive this specific outcome?” Probabilistic measurement cannot answer the second. Once budgets, compensation, or contractual claims depend on the number, the gap matters.
Even within its proper bounds, the method has limits. Fishkin’s study found that asking ChatGPT or Google’s AI mode the same prompt 100 times produced an identical brand list less than once in 100 runs, and an identical list in the same order less than once in 1,000. An August 2025 Ahrefs analysis of 15,000 prompts 18 found that 80% of LLM citations from ChatGPT, Gemini, Copilot, and Perplexity did not rank anywhere in Google for the original query; only 12% appeared in Google’s top 10. Overlap between the AI systems themselves is similarly thin: SE Ranking finds ChatGPT and Google AI Overviews share around 21% of citations 25h ; Profound has ChatGPT and Perplexity at 11%, and AI Overviews and Copilot at 6 to 10% 25i . A sweep against one provider is a sample from one stack. Platform share can shift materially in a single year, per Similarweb 19 . By May 2026, Digiday was quoting senior agency executives who had reached the same conclusion 16 in practice.
If you use three different tools and give them the same prompts, you get three different answers.
Paul Dyer, CEO of /prompt, an AI-native services agency 16
We don't know enough of these companies to be charging what they're charging. But it's extremely early days.
Joseph Levi, CEO of Noise Media Group
There's really not much an AI tool can do or tell you to do. It's just a benchmarker in my mind.
Ryan Mason, President and COO at Markacy
Vendors have responded to that instability in the usual ways: more prompts, better clustering, cleaner dashboards, more elaborate prompt-generation systems. Profound, Evertune, Ahrefs, and Semrush all shipped versions of this in 2026. Some of the work is worthwhile - probabilistic measurement at scale can say something useful about brand presence, especially when the methodology is disclosed. It is much harder to defend when the same machinery supports claims about causality, incrementality, or compensation. The limits show up in a few recurring kinds of claim.
Stress-testing the 40% claim In December 2025, impact.com announced a partnership with Evertune. The press release quoted Evertune CEO Brian Stempeck 20 : “In our analysis of the top 10,000 sources cited by AI models, over 40% of content either contains affiliate links or is sponsored.”
The claim may be true as stated, but it does not establish what readers are likely to infer from it. If 40% of the top 10,000 cited domains contain affiliate links somewhere on the site, that does not mean 40% of AI answers are commercially influenced. It does not mean affiliate content caused the citation, or that paying for affiliate placement produces measurable returns inside AI answers. It tells us that commerce-content sites are frequently cited, which has been true for years. The press release does not disclose methodology, prompt set, model versions, geography, or sampling. Evertune’s separate March 2026 shopping study 21 discloses all of that. The careful research exists. The headline travels without it.
Stress-testing Profound's Visibility Score Profound is one of the best-known vendors in the category. Its headline product is the Visibility Score, defined on its own blog as “the percentage of mentions out of the total responses tracked.” 25b That is close in form to the visibility-percent metric Fishkin’s research supports for ideation and consideration-set tracking. It does not bear the weight of spend decisions.
Two published claims show the gap. One is the AI Consumer Journey 2025 study, which reports that 79.7% of buyers 25c rely on AI Answer Engines for at least half of their purchase decisions. That figure comes from a Profound-screened US panel of 1,600 people selected from 2,739 screened individuals aged 18 to 99. A panel constructed from people who already qualify as AI Answer Engine users is likely to produce a high share of AI-reliant purchasers by design. The number does not tell us what share of all purchasers behave that way. The other example is a customer case study saying that Ramp “increased AI brand visibility 7x in accounts payable.” 25d A sevenfold rise in Visibility Score may be observable in Profound’s reporting. It does not show that the dashboard caused the rise. Ramp did the content work. Profound measured the result.
AthenaHQ’s “Prompt Volume” feature 14a , which estimates how often each prompt is asked of a given LLM, sits on shakier ground still. AthenaHQ does not publish accuracy data for it. No provider exposes the query logs that would let such an estimator be calibrated from outside.
Vendor on the record: "wildly wrong" prompt-volume numbers In a public r/b2bmarketing thread 14b , Malte Landwehr of Peec AI confirmed that prompt-volume estimators across the category, including Peec AI’s own, are extrapolations from a shared third-party panel rather than provider-supplied query data: “We (Peec AI) are using the same (or at least partially the same) panel.”
His follow-up on the methodological limit is unusually direct for a vendor in the category:
“Absolute numbers are too inaccurate to confidently display them. But on a project-basis, we believe the biases that are very likely in the data to be the same for all prompts. So the relative scale should work well. Other tools have the same limitation. I cannot understand why they opted to display, sometimes wildly wrong, absolute volume numbers.”

Peec AI’s response is to report on a 1-to-5 relative scale rather than absolute volumes. The product positioning is incidental. The relevant admission is that the panel-data extrapolation method has limits that other vendors disguise by quoting precise-looking absolute numbers.
The pressure repeats inside affiliate networks, through a different mechanism. VantagePoint is not a prompt-monitoring tool: rather than sweeping AI models, it uses panel data to derive expected behaviour and engagement, and offers a payment model built on that estimate. A December 2025 Partnerize post claims brands are “undercounting your true incremental influence by 30 to 60%” through its VantagePoint product, with no methodology disclosed 22 . In April 2026 Partnerize followed with the Influence Compensation Lighthouse Program, which pre-funds publisher commissions on conversions its own model identifies as AI-influenced 23 .
Attribution and compensation models of this kind are a separate discipline from measurement, and sit outside the scope of this paper. They still rest on measurement. A compensation layer for AI-influenced sessions is infrastructure the category will need, and Partnerize is among the earliest to build it. That layer needs a shared, reproducible measurement signal underneath it - which is what this paper argues for.
The measurement concern is structural and holds across the category: every commission-taking network has reason to expand the commissionable surface into AI-influenced sessions, and to seek certification for the methodology behind it. Partnerize’s VantagePoint methodology carries certification from the Alliance for Audited Media 23a ; that certification confirms the platform conforms to its own stated methodology, and is not an independent judgement of the methodology itself. The measurement currency that decides what counts should not be set by the parties that take a margin on the count. The January 2026 PartnerStack-Evertune integration 24 and the March 2026 Profound-Partnerize integration 25 sit on the same logic, without a reproducible measure of how often AI is the actual entry point. No prompt sets. No raw data. No reproducibility.
Semrush matters because it moves this methodology into the mainstream marketing stack. Its AI Visibility Toolkit tracks ChatGPT, Google AI, Gemini, and Perplexity, sold standalone or bundled into Semrush One. Adobe’s acquisition makes it harder to treat this as a niche category. The Semrush AI Visibility Index, updated in April 2026 25f , offers the usual mix of headline figures and per-domain citation shares. Its outputs line up closely with numbers published elsewhere in the category. That is what convergence looks like when everyone is sampling the same model behaviour through the same method.
Profound’s own analysis of more than 250 million AI search results found that combined backlink metrics - referring domains, total backlinks, authority scores - explain just 11.9% of AI citations 25j . The vendor itself is publishing evidence that the SEO-adjacent levers most GEO tooling indexes against do not move the answer. Eighty-eight per cent of what shapes an AI citation sits outside those levers, in retrieval ranking, citation-generation policy, and consumer-surface decisions the dashboard does not see.
The comparison with early SEO tooling is helpful up to a point. In Google’s first decade, rank trackers also relied on proprietary samples and produced numbers that did not always agree. What changed was the arrival of Google Search Console, a first-party, deterministic signal from the platform itself. Probabilistic SEO measurement did not disappear after that. It became more useful because it could finally be checked against something real.
AI visibility is now seeing the first half of that arc, unevenly. Microsoft moved Clarity’s Citations dashboard into general availability on 15 May 2026 13a , exposing page-level citation counts, share-of-authority percentages, AI referral traffic as a share of total sessions, and the queries associated with each citation - a first-party signal of the kind GEO vendors have to infer. Google has gone the other way. Its developer-facing AI Optimization Guide 30a reframes the category as “still SEO”, rejects llms.txt and AI-specific schema as unnecessary, and adds no measurement surface for AI-driven traffic on the platform side.
What is emerging is a set of single-vendor windows, each visible only to that vendor’s own surfaces. A brand using two providers cannot compare like with like. A publisher whose content was retrieved still has no record of it across providers. Event-level reporting that flows back to the content owner regardless of which provider made the citation is the thing that does not yet exist. Without it, probabilistic estimates are doing work they cannot support.

## 3. Four structural problems #

### 3.1 Brands are paying twice #
Brands publish a large share of the open web’s most structured factual material. Product specifications, prices, descriptions, comparison tables, support documentation, store locators, return policies, ingredient lists, and sizing charts all come from brand sites. This is the material that allows an AI assistant to answer questions like “what is the battery life of the new Bose QC headphones?” or “does this jacket come in tall sizes?” In most cases it is not licensed. It is simply there to be scraped.
Brands could pull some of this data back, and in the aggregate that would reduce the commercial usefulness of AI assistants. The leverage is real, but it is diffuse.
What often happens instead is a more awkward arrangement. Brands invest in producing the structured content the models depend on, then pay GEO platforms for probabilistic visibility reporting that cannot reliably tell them which of their pages was retrieved, which was discarded, what was paraphrased into the answer without credit, or which competitor’s content actually shaped the response before the citation slot was filled. They can report mentions and cited URLs from a sample of prompts; they cannot reliably connect those to what happened inside the pipeline.
A brand is therefore paying a vendor to infer from public outputs something that could, in part, be observed directly. Most of the companies buying these tools already run CDN logs, web server logs, and bot-detection systems that record AI retrieval as it happens. The signal already exists, but what is missing is a standard way to structure and report it.
Measurement matters here, but most of what brands are buying is the wrong signal sold at a premium.
Most of what brands are buying is the wrong signal sold at a premium.

Figure 3. The scrape and the click are two separate events. After Goldstein, .msg, April 2026. The commercial stakes are already large enough to make this more than a technical complaint. Adobe Digital Insights, drawing on more than one trillion visits to US retail sites, reported in April 2026 that AI traffic to those sites grew 393% year over year 26 in Q1 2026, after a 693% jump during the 2025 holiday season. AI traffic now converts 42% better than non-AI traffic, which is the reverse of where things stood a year earlier. A useful way to frame AI commerce is as two events: the scrape and the click 27 . The scrape determines whether a product is surfaced inside the answer. The click determines whether the retailer sees the revenue. Retailers who make product pages easier for machines to read are improving both at once. Adobe’s own figures support that reading. The best-performing US retail homepages scored 82.5% on machine readability, compared with 54.2% for the weakest performers. That gap has more to do with how pages are structured than with how often someone reruns the prompts.
The scrape determines whether a product is surfaced inside the answer. The click determines whether the retailer sees the revenue.
After Matthew Scott Goldstein, .msg newsletter, April 2026 27

### 3.2 Provider incentives are misaligned #
The current GEO market suits AI providers well. As brands and publishers reshape content to be more structured and easier for machines to parse, they improve the material those systems retrieve and train on. Every prompt a GEO vendor runs is a paid API call to OpenAI, Anthropic, Google, or Perplexity, so measurement is itself a revenue source. Third-party vendors are doing the work of convincing the market it should care about AI visibility - on the providers’ behalf.
A vendor bills the brand for prompt-monitoring runs. The model provider bills the vendor for the API usage behind them. The brand funds both sides. More importantly, the provider sells the system and the only widely available way to probe what the system did. Every extra query used to verify or monitor visibility is revenue for the same company whose outputs remain opaque.
Google’s developer-facing AI Optimization Guide 30a , published in May 2026, sits inside the same logic. The guide tells content owners that optimising for generative AI search is “still SEO”, rejects llms.txt and AI-specific schema as unnecessary, and includes no measurement surface for AI-driven traffic on the platform side. The recommendation is to keep producing the structured factual material the models depend on, on the existing terms, without exposing the events that material is producing. That is a position with a financial preference, framed as documentation.
That incentive structure points toward first-party visibility products, and OpenAI has begun moving in that direction. In early 2026, trade-press reporting indicated that OpenAI had started introducing advertising formats inside ChatGPT 28 and was iterating quickly on how the placements sold 29 . The initial formats included sponsored cards in answers and shopping-style product cards. Free and lower-tier surfaces showed ads; higher-paid subscribers did not.
Once the answering platforms start selling visibility directly, third-party probabilistic tooling looks more like a temporary proxy than a durable layer. The durable question is whether content owners can see what was actually retrieved and cited, in a form that does not depend on which company currently sells the dashboard.

### 3.3 The publisher leverage problem #
Publishers negotiating with AI providers start from a familiar claim: professionally edited, fact-checked reporting is worth more than the undifferentiated open web. That claim has already produced real deals. Press Gazette’s publisher-AI deal tracker, updated to April 2026 31 , lists roughly twenty named OpenAI publisher partners, including Associated Press, Axel Springer, the Financial Times, Vox Media, Time, Le Monde, Prisa, The Atlantic, Dotdash Meredith, News Corp, Hearst, Condé Nast, The Guardian, Schibsted, Axios, The Washington Post, and Future plc, which publishes more than 200 specialist titles. Other providers have built smaller rosters. At the same time, The New York Times’ lawsuit against OpenAI is well into discovery 32 .
That licensing argument is easier to sustain if premium content remains visibly scarce and visibly valuable. GEO complicates that picture. If brand SEO content, affiliate listicles, and synthetic commerce reviews can all be promoted into AI citations through prompt and content engineering, then providers gain a parallel supply of answers that may be good enough for many commercial purposes. The marginal value of any individual publisher’s content becomes harder to defend.
Cloudflare’s crawl-to-refer ratios from mid-2025 33 show how uneven the relationship already is. For every visitor Anthropic referred back, its crawlers had visited 38,065 pages. OpenAI’s ratio was 1,091:1, Perplexity’s 194:1, Google’s 5.4:1. Publishers are supplying thousands, sometimes tens of thousands, of pages for every visitor returned. The same providers are building commercial products that may need less publisher traffic over time.
For every visitor Anthropic referred back, its crawlers had visited 38,065 pages. OpenAI's ratio: 1,091:1. Perplexity's: 194:1. Google's: 5.4:1.
Cloudflare, crawl-to-refer ratios, mid-2025 33
That tension comes through clearly in a Bloomberg Odd Lots interview broadcast on 23 April 2026, where Google’s VP and head of Search Liz Reid 34 described retention rather than referral as Google’s success metric. The goal is to have users return to Google more often, not necessarily to send them out more often. The same interview noted that Google Search now serves ads on less than a quarter of queries, and treated the so-called “bounce click” - where a user lands on a publisher page only long enough to extract a fact - as traffic Google can afford to lose. Without licence-level reporting on what AI surfaces actually did with publisher content, publishers have very little leverage left.
The goal is to have users return to Google more often, not necessarily to send them out more often.
Liz Reid, VP and head of Search at Google, paraphrased from Bloomberg Odd Lots, 23 April 2026 34
Independent academic measurement on the largest AI surface confirms the asymmetry. Xu, Iqbal, and Montgomery’s audit of 55,393 trending Google queries over 40 days in March-April 2026 found that more than half of AI Overview-cited publisher pages (50.6%) carry display advertising - the revenue model the suppressed click would have funded - while Google’s own sponsored search ads continue to appear on the same SERP as the AIO, in some cases above it 34a . AIO deployment is structurally one-sided: it dilutes the publisher revenue model that makes its own sourcing possible, while leaving Google’s ad capture intact. The same study finds AIO-cited domains are systematically more credible than co-displayed first-page results (+0.087 on a normalised 0-1 credibility scale), so the leverage gap is not closing through better sourcing - it is widening, because publishers whose content makes the answer possible are not the publishers whose pages users would have clicked through to.
This is why event-level reporting matters so much in licensing. Without a shared record of what was retrieved, cited, and engaged with, each negotiation rests on the publisher’s evidence, the provider’s accounting, and the publisher’s willingness to trust what it cannot verify.

### 3.4 Citation laundering and content laundering #
The same techniques used in GEO to influence AI answers can be used by actors with no real claim to authority. Schema markup, content seeding, authority-signal stuffing, llms.txt manipulation, and knowledge-graph entries all sit on the same surface. By mid-2026, two distinct laundering problems were visible.
Figure 4. Same prompt. Two failure modes. ChatGPT (top) launders a low-credibility source; Google AI Overview (bottom) cites a publisher that has explicitly opted out. The first is citation laundering at the output layer. In one April 2026 captured ChatGPT response to “sony wh-1000xm5 vs bose qc ultra?” 36 , the model returned a side-by-side comparison whose top citation was wh1000xm5.co.uk , a thin WordPress site presented alongside two Wired articles as though it belonged in the same evidentiary tier. Asked the same question, Google’s AI Overview cited SoundGuys, What Hi-Fi?, RTINGS, Trusted Reviews, and Rolling Stone. Those are recognisable editorial outlets, but Rolling Stone has explicitly blocked GPTBot, ClaudeBot, and Google-Extended in its robots.txt 37 . The two systems fail in different ways. One elevates a low-credibility source. The other cites a source that has already said no.
The second is content laundering at the input side. In March 2026, Ahrefs - whose crawler has enjoyed broad publisher access for SEO analytics for years - launched Firehose 38 , a “real-time data streaming API” marketed as “built for agents (and humans, too)” and offered free during beta. Its documentation included example rules targeting individual publishers, including Reuters, without saying much about publisher consent, licence terms, or attribution flowing back to the original source. The mechanism is straightforward: a third party that already has crawl access can redistribute content to AI agents the publisher never allowed in directly. A publisher’s robots.txt rules against GPTBot or PerplexityBot matter less if the same content remains available through Ahrefs’ crawler, which most publishers are reluctant to block because Ahrefs is a standard part of the SEO stack. Ahrefs’ published research is cited approvingly elsewhere in this paper, and with good reason - its April 2026 and August 2025 studies disclose sample sizes and methodology in more detail than most of the category. Firehose raises a different question about downstream consent. The same boundary between commercial AI search and data laundering is at the centre of Reddit’s October 2025 lawsuit against Perplexity and its co-defendants 39 .
The remedies differ because the problems sit in different parts of the system. Citation laundering is an output problem - providers need to weight authority better and present provenance more clearly in the interface. Content laundering is a data-layer problem - consent signals need to travel with the content through intermediaries, or the publisher’s preferences disappear as soon as the content is rebroadcast.
Both are versions of the same supply-chain weakness, and the techniques work the same whoever uses them. The tools that allow a brand to push itself into an AI citation can also be used by a state-aligned propaganda network for entirely different ends. NewsGuard’s September 2025 audit of ten leading chatbots found that 35% of responses 40 to questions about controversial news topics contained false claims, up from 18% a year earlier, and that the systems had largely stopped refusing such questions. NewsGuard’s March 2025 work traced a meaningful share of those falsehoods to the Russian-aligned Pravda network 41 , a cluster of 150 domains that published 3.6 million articles in 2024 alone, not to persuade human readers directly, but to enter retrieval and training corpora at scale.

## 4. A reproducible audit #
To show what GEO-style measurement looks like when its methodology is disclosed in full, OpenAttribution conducted its own audit in May 2026 42 . The audit asks a single, narrow question: when AI search engines cite a domain, how often is that citation coming from a domain whose robots.txt explicitly blocks the citing provider’s bot?
We submitted 330 prompts across eleven content categories - news, finance, health, shopping, technology, sports, education, consumer electronics, food, travel, and brands - to four production AI search APIs: OpenAI’s Responses API with web_search_preview enabled 45 , Anthropic’s Messages API with the web_search tool enabled, Google’s Gemini API with google_search grounding, and Perplexity’s Sonar API. The consumer products at chatgpt.com, claude.ai, gemini.google.com, and perplexity.ai were not used. Each prompt was run three times against each provider. We extracted 24,127 citations across 6,798 unique cited domains.
For every unique cited domain we used PolicyCheck, OpenAttribution’s open-source robots.txt and licensing scanner 43 , to fetch the domain’s robots.txt and check it against two user agents per provider. The first is the training crawler - the bot publishers most often name when they opt out of AI use: GPTBot, ClaudeBot, Google-Extended, PerplexityBot. The second is the live-search bot - the user agent the provider’s web_search tool actually uses at answer time: OAI-SearchBot, Claude-SearchBot, Google-Extended (Gemini’s grounding tool uses the same agent as training), and Perplexity-User. Robots.txt was fetched successfully for 22,263 of the 24,127 citations (92.3%); the remainder returned fetch errors and were excluded from the calculations.
This is a probabilistic audit. We are sampling the providers’ public output and cross-referencing it against the public consent signals declared by cited domains. We do not see what the model retrieved internally, what it ranked, or what it discarded. What we see is what the GEO industry sees. We publish all of it - methodology, prompts, code, raw data.
Figure 5. Citations from blocked domains, by provider and bot. PolicyCheck, May 2026.

### 4.1 The headline number depends on which bot you check #
Across the 22,263 citations for which robots.txt was successfully fetched, 7.8% came from domains whose robots.txt blocks the provider’s training bot. The same citations, checked against the live-search bot rather than the training bot, give 2.1% . The cited URLs are identical. The publisher’s robots.txt is identical. The 5.7-point gap is the bot-taxonomy gap: publishers named the training crawler in their opt-out and were silent on the live-search agent, so the live agent is permitted by default under RFC 9309.
The gap is concentrated in two providers:
Provider Training-bot blocked Live-search-bot blocked
OpenAI | 14.5% (517 / 3,576) - GPTBot | 1.1% (39 / 3,576) - OAI-SearchBot |
Anthropic | 14.4% (934 / 6,469) - ClaudeBot | 2.4% (154 / 6,469) - Claude-SearchBot |
Gemini | 4.2% (274 / 6,454) - Google-Extended | 4.2% (274 / 6,454) - same bot |
Perplexity | 0.1% (6 / 5,764) - PerplexityBot | 0.1% (6 / 5,764) - Perplexity-User |
Both readings are real. The training-bot rate captures the publisher’s likely intent: when Medium lists eight AI training crawlers including ClaudeBot and sets Disallow: / for all of them, the plain reading is that Medium does not want Anthropic crawling. The live-search-bot rate captures the strict RFC 9309 read: Medium did not name Claude-SearchBot, so Claude-SearchBot is allowed. Anthropic’s web_search tool cited Medium 62 times. Under one read this is a violation; under the other it is permitted. The current public consent layer - robots.txt - cannot tell those reads apart, and most publishers do not appear to know there is a distinction to make.
Gemini does not show a gap because Google-Extended covers both training and Gemini grounding. Perplexity does not show a gap because its training-bot rate is already a floor: Perplexity-User “generally ignores robots.txt rules” per Perplexity’s own documentation 5 , so the audit’s compliance rate for Perplexity is not a measure of compliance.

### 4.2 What licensing deals do to the public signal #
A second source of headline drift is licensing deals. The single largest “violation” group in the dataset is reddit.com, cited 246 times by Gemini and 13 times by OpenAI, all from a domain whose robots.txt blocks Google-Extended and GPTBot. Google announced a Reddit data-licensing agreement worth a reported $60 million per year in February 2024 42a ; OpenAI announced its own Reddit deal in May 2024 42b . AP News appears 81 times in OpenAI’s blocked count and has been licensed to OpenAI since July 2023 42c . Strip Reddit and AP News from the training-bot violation count and the headline drops from 7.8% to 6.2%. Gemini drops from 4.2% to 0.43% - the visible-violation behaviour of Gemini in this dataset is, almost entirely, its Reddit licence. The robots.txt block is a stale signal of consent the contract has overridden, and a third party with no access to the contract cannot tell the difference.
This matters in both directions. Strip the known deals and the picture looks much cleaner. Add the deals nobody has announced and the picture would look messier still. There is no public register of which provider has paid which publisher, and the public consent signal does not move when a contract is signed.

### 4.3 The most-cited and the most-flagged #
Figure 7. Top-20 most-cited domains across all four providers. Red = blocks the citing provider's training bot. YouTube is the most-cited domain (1,086 citations, allowed everywhere); English-language Wikipedia is second (374). The third-most-cited domain in the dataset is reddit.com (259), and the eighth is vertexaisearch.cloud.google.com (144) - a Google-owned proxy URL that obscures the underlying source from any third party looking at Gemini’s citations.
Past the licensing-deal cases, the top training-bot violators, ranked by total citations across all four providers, are ESPN (127; OpenAI cited the blocked domain 5 times), Medium (106; Anthropic cited the blocked domain 62 times), Sky Sports (86; OpenAI cited the blocked domain 19 times), CNN (62; Anthropic cited the blocked domain all 62 times), CBS News (60; OpenAI cited the blocked domain 7 times), and Al Jazeera (59; Anthropic and OpenAI cited the blocked domain 51 times between them). Healthline, WebMD, Consumer Reports, CBS Sports, Lonely Planet, and TripAdvisor all appear repeatedly as cited-while-blocked. None has an announced licensing deal with the citing provider that we are aware of.
Figure 6. Citations from blocked domains, by content category. Training-bot test, May 2026. By content category, news is the highest-violation vertical (14.0%), followed by technology (9.6%), consumer electronics (8.8%), and education (8.2%). The categories with the highest editorial value to publishers are the categories with the widest gap between publisher consent signals and provider behaviour.

### 4.4 Blocked sources rank near the top #
The “violation” citations are not being demoted into the footnotes. Mean citation rank for sources whose robots.txt permits the citing bot is 4.4; for sources whose robots.txt blocks the citing bot, mean rank is 4.1. Lower rank means earlier in the response. Blocked sources are appearing inside the top five citations more often than the compliant sources are. Whatever filtering providers apply at the citation-generation stage is not down-weighting publishers who have asked not to be crawled.
Blocked sources are appearing inside the top five citations more often than the compliant sources are.
OpenAttribution audit, §4.4 finding, May 2026 42

### 4.5 What this audit cannot see #
It does not tell us whether the cited content was actually used in the generated answer or merely linked. It does not capture URLs routed through proxy or redirect mechanisms; the 144 citations to vertexaisearch.cloud.google.com in this sample alone illustrate the size of that blind spot. It does not capture licensing deals other than those we already know about: a publisher’s robots.txt block is read as a current consent signal whether or not a private contract has overridden it. It checks only one live-search user agent per provider; if Anthropic or OpenAI ship multiple live agents, only one is tested. And it is a single point in time. Robots.txt files and provider citation behaviour change continuously.
Parallel academic measurement has begun to characterise the surfaces this audit cannot reach. Xu, Iqbal, and Montgomery’s contemporaneous Google AI Overviews study 34a - 55,393 queries, 7,583 AIOs, 98,020 atomic claims verified against full reference-page content - independently confirms two patterns the deterministic event model is designed to surface: retrieval pools diverge from ranking (29.8% of AIO-cited domains do not appear on the first-page SERP for the same query, and 28.5% at the URL level), and unsupported claims dominated by silent omission run at 11.0% (with active fabrication only 2.7%). A growing list of independent measurement work is summarised in related research .
None of those limitations are answered by running the audit at greater scale. Which content was actually retrieved, which was used to ground the answer, which was rendered to a user and which was engaged with - those questions sit in a different place entirely, inside the providers’ own retrieval and citation logs. The bot-taxonomy gap exposed here is the same problem under a different lens: the public consent surface is too coarse for the choices providers and publishers are actually making. Section 5 describes the open-standard event vocabulary that would let those answers come out without each provider building a separate dashboard.
The full data, prompt list, code, and methodology are published in the OpenAttribution research directory 44 . The rendered report for the May 2026 run is at openattribution.org/research/citation-compliance-may-2026 . Any researcher, journalist, agency, or vendor can reproduce the audit, contest its conclusions, or run a variant on different prompts.
These numbers exist, are reproducible, and can be argued about on the basis of evidence rather than vendor marketing. Most GEO vendors could publish at a comparable level of disclosure if they chose to.

## 5. What deterministic measurement looks like #
Figure 8. Two ways of seeing AI visibility. The audit in Section 4 captures one narrow slice of what a content owner needs to know: did the AI provider cite a source it was asked not to? It does not capture the rest, and no probabilistic audit ever will. Four further questions matter for any brand, publisher, or content marketer trying to act on AI visibility:

- Was my content retrieved? When an AI agent fetches a page from my domain, do I have a record of it - which agent, which URL, when?

- Was my content cited, paraphrased, or used as the basis of an answer? Not just whether the URL appeared in a citation slot, but how the underlying content shaped the response.

- Was the citation rendered to a user? Model-generated citations can be truncated, collapsed behind “show sources”, or filtered by UI policy before reaching the answer surface a user actually reads.

- Did anyone engage with the citation? Did a user click through, read the source, or follow the cited link?
Figure 9. The six deterministic events of the OpenAttribution vocabulary (Content Telemetry v1). OpenAttribution defines six deterministic events that, taken together, answer those questions:

- content_retrieved - an AI agent or crawler fetches content from a domain. Bot identity, requested URL, response status, timing.

- content_grounded - retrieved content is loaded into the model’s working context for a session. The point at which a fetch starts to shape an answer, distinct from whether a citation slot is eventually filled.

- content_reproduced - source content appears verbatim or near-verbatim in the output - a quotation, an excerpt, or a full copy, credited or not. The uncredited excerpt delivered through an API is the canonical case: without this event, that use is unreportable. Reproduction and citation are sibling claims about the same output - the material and the credit - and neither implies the other.

- content_cited - grounded content is named in a model response, with the response context and the relationship between the cited content and the generated text.

- content_presented - content or a source reference is made perceivable on the answer surface the user sees - rendered, played, or spoken. Captures whether the citation survived post-generation truncation, summary collapse, or UI filtering, and distinguishes source content itself from a reference to it.

- content_engaged - a user interacts with a presented source, whether by clicking through, expanding a quote, or following a recommended link. Each engagement references the exact presentation occurrence it happened on.
Each is an event with a source and a timestamp, observable by at least one party in the chain - usually by multiple parties whose records can be cross-checked. When more than one party reports the same retrieval - a publisher’s CDN and the agent itself, for example - the records are correlated through a shared Content-Telemetry-ID header. The agent stamps each outgoing fetch with a fresh identifier; the publisher’s CDN logs the same value alongside its normal access record, so the two logs can be matched after the fact without either side trusting the other’s clock. The same event has two independent witnesses rather than one log to take on faith.
Today, the first of these events is fully measurable without any cooperation from AI providers. Every CDN, web server, and hosting platform already logs incoming HTTP requests; AI bots identify themselves through user-agent strings and IP ranges that can be cross-verified against provider-published lists. The open-source Cloudflare Worker shipped by OpenAttribution 48 detects AI bot traffic, structures it into events, and publishes those events to whichever telemetry endpoint the domain has chosen, including a publisher’s own self-hosted endpoint. Integrations for WordPress, Vercel, Netlify, Fastly, Akamai, and CloudFront are in active development. A site owner on Cloudflare who deploys the Worker sees, today, every AI agent that fetches their content.
The remaining five events - grounded, reproduced, cited, presented, engaged - require AI providers to cooperate. Some already do, in part. Google’s grounding metadata exposes which spans of an answer were grounded in which retrieved chunks. Anthropic’s web_search_result blocks return URL, title, and page_age 46 for each result the model considered. Perplexity returns a structured citations array in its API responses 47 . None of these signals are unified across providers, none carry signed timestamps, and none flow back to the source domain by default. The OpenAttribution specifications for content_grounded , content_reproduced and content_cited are designed to wrap and standardise these provider-side signals into an event shape that any provider can emit and any content owner can receive.
content_presented and content_engaged both depend on the consumer surface (chatgpt.com, gemini.google.com, claude.ai, perplexity.ai) reporting what it shows and what users do with it. Presentation covers whether a generated citation reaches the rendered answer at all - citations can be dropped during summary collapse, hidden behind “show sources”, or filtered by UI policy. Engagement covers what the user does next: click through, expand a quote, follow a recommended link. Today neither is reported consistently: Perplexity’s referer headers are precise enough that CDN-level matching is possible; ChatGPT’s referer handling loses the question and citation context. The specification defines a consistent schema that does not depend on referer fidelity.
Outcome attribution - the connection between an AI citation and a downstream business outcome (a purchase, a sign-up, a registered conversion) - is a layer above these six events. The six events have to exist before it can be measured at all.
OpenAttribution has not shipped all six. The standard is mature for content_retrieved , with the Cloudflare integration in production today; the rest is a published specification in active iteration. None of it requires providers to expose ranking weights, model parameters, or proprietary algorithms - only the events that already happen during retrieval and citation, in a structured form that flows back to the affected content owner. All of it requires open standards because the alternative - each provider exposing a different, unaudited dashboard - is a regression towards the same opacity content owners are trying to escape.
A handful of complementary efforts share parts of this surface. The Coalition for Content Provenance and Authenticity (C2PA) defines content credentials 49 and provenance signatures for media. Google’s grounding metadata is a provider-specific implementation of part of content_cited . Cloudflare’s bot management product 50 surfaces a portion of content_retrieved for its own customers. Microsoft Clarity now covers more of the surface than any single-provider tool published to date: the Bot Activity dashboard reports a portion of content_retrieved , and the Citations dashboard added in May 2026 13a reports a portion of content_cited and content_engaged for the AI surfaces Microsoft has visibility into. The shape is right; the scope is one vendor. Source-side licensing standards (RSL 51 , IAB CoMP 52 , Peek-Then-Pay 53 ) and OpenAttribution’s own AIMS (agent identity manifests) 54 sit alongside the telemetry layer rather than overlapping with it: licensing answers what an agent may do, AIMS answers who the agent is, and telemetry answers what it actually did. These are useful and we treat them as building blocks. None of them, individually, gives a content owner the cross-provider, end-to-end picture; an open standard is what makes the building blocks compose.

## 6. What this means for content owners #
Three groups of readers can act on the analysis above.
Do this next week
- Instrument the supply side. Deploy the open-source Cloudflare Worker, or an equivalent server-side hook, so every AI agent fetch from your domains is captured as a content_retrieved event. Free, no provider cooperation required.

- Run your own audit. Pick a prompt set, sweep four providers' APIs, cross-check the cited domains against PolicyCheck. One afternoon of engineering time. Methodology and code are published with §4.

- Add methodology disclosure as a pre-spend gate. For any GEO vendor or paid visibility tool, require prompts, model versions, geographic mix, and raw citations before approval. If they will not share, treat the output as marketing.
For publishers. Every commercial agreement signed with an AI provider should specify which retrieval, citation, and engagement events the provider will report, in what schema, at what frequency, and with what audit rights. The default in 2026 is that licence agreements specify payment terms with little or no telemetry obligation. Publishers are paid a fixed sum and have no way to verify whether the content licensed is the content actually being used. Negotiating event-level reporting alongside the financial terms costs nothing and is a precondition for the next round of contracts being valued accurately. A licence without an event-level reporting clause is incomplete.
The non-licensed retrieval question is the other half. If a provider is fetching a publisher’s content without a licence, the publisher’s CDN logs already record it. Structuring those records into a standard event schema makes them portable across providers and across lawyers. The cost of doing nothing is that next year’s negotiation starts from the same data asymmetry as this year’s.
For brands. Probabilistic visibility tooling has a use - brand-presence checks across many runs, on the lines Fishkin’s research established. Treated as attribution, it is asking the dashboard to do work it cannot do. Treated as the only measurement layer, it leaves the brand’s actual leverage off the table.
That leverage was set out in Section 3.1. The structured factual material AI assistants depend on - specifications, prices, comparison tables, support documentation, store locators, return policies, ingredient lists, sizing charts - comes from brand sites, and almost none of it is licensed. Commerce-grade data is also harder for the provider to substitute than editorial reporting. There are two or three right answers to “best noise-cancelling headphones.” There are many right sources for a news lead. The brand has the better hand and is not playing it.
Two steps change that.
First, run your own audit. The methodology described in Section 4 - prompt monitoring, citation extraction, robots.txt cross-check via PolicyCheck - takes a single afternoon of engineering time and produces results that can be argued about on the basis of evidence. If a vendor will not share the prompts, model versions, geographic mix, and raw citations behind a number they are quoting, treat the number as marketing rather than measurement.
Second, instrument the supply side. The brand’s CDN logs already record what every AI agent fetches from the brand’s website. A content_retrieved event for every GPTBot, ClaudeBot, PerplexityBot, or Google-Extended request gives the brand a primary record of which of its pages are being read by which models. That record is more actionable than any third-party estimate of where the brand was mentioned. It costs nothing to produce. And it is the only basis on which a brand can argue licensing terms, attribution, or compensation from evidence rather than from public outputs alone.
For agencies. AI visibility work has more in common with technical SEO and analytics architecture than with paid media. The most defensible agency role sits where the brand cannot easily replicate the work in-house: forcing vendors to disclose methodology before any spend is approved, helping clients build the data layer on their own infrastructure (CDN integrations, event schemas, dashboards), and connecting the resulting first-party signal to the rest of the marketing stack (CRM, ad platforms, MMP feeds).
The shift mirrors what happened to SEO agencies once Google Search Console arrived. Probabilistic rank-tracker dashboards did not disappear; they became one input among several, and the agencies that did well moved up the stack into technical implementation, analytics instrumentation, and content strategy informed by first-party data. The same arc applies here. The retainer model of “we run prompts, you read the dashboard” is the comparable starting point. The retainer of “we instrument your stack, audit your providers, and run methodology gates on the vendors you use” is the durable one.
The visibility work should not be dropped. Brand-presence reads still matter for ideation, consideration-set tracking, and campaign-level read-outs on Fishkin’s lines. What changes is the size of the bill being asked of clients to fund prompt-monitoring runs alone, and the share of the engagement those runs deserve. A practical transition starts on the next renewal cycle: add a methodology disclosure clause as a pre-spend gate for any GEO vendor in scope; bundle CDN-side content_retrieved instrumentation into the standard onboarding; and shift the reporting layer onto infrastructure the client owns. None of those steps require waiting for a standard to be ratified. They make the eventual standard easier to adopt when it lands.

## 7. Where this goes next #
OpenAttribution is a UK company limited by guarantee (no. 17002582) 55 . It publishes open specifications under Apache 2.0 and operates free telemetry infrastructure. Anyone can use the specifications and infrastructure without joining.
The next working session is on 17 June 2026 in London, hosted with Martech Record at The Drum 56 . It is a closed-door working group covering implementation, governance, and the open questions in the specification. Attendance is limited.
Three concrete actions follow.

- Show up on 17 June. Register at martechrecord.com/upcoming-events/ai-attribution-reception-discussion . The people in that room will decide whether a shared measurement standard exists by 2027. Brands, publishers, platforms, and agencies are all in scope.

- Claim your domain at openattribution.org . The dashboard account is free, public telemetry hosting is free, self-hosting is free; the protocol is the same either way. Joining the standards body as a Steering Committee, working group, or supporting member is a separate decision and a separate fee.

- Implement content_retrieved . The Cloudflare Worker is open source and ships today; specifications and SDKs are at github.com/openattribution-org. It requires no cooperation from AI providers and gives any site owner on Cloudflare a primary record of what is being fetched. WordPress, Vercel, Netlify, Fastly, Akamai, and CloudFront are next.
The longer-term project is everything beyond content_retrieved , and it requires a coalition: content owners, providers, agencies, and platforms agreeing on what an event is, what it contains, and who is allowed to see it. No single vendor can build it. Nor can the parties negotiating licences, without measurement infrastructure underneath them.

## Appendix A. The pipeline in detail #
This appendix expands the eight-stage pipeline summarised in Section 1, with sourcing for each claim. It is intended for readers who want to inspect or argue with the technical underpinning of the rest of the paper.
Stage 1: Query reformulation. The user’s natural-language question is rewritten by the model into one or more keyword search queries. ChatGPT, Claude, Gemini, Copilot, and Perplexity each implement this differently. Google has publicly described its AI Mode as generating multiple sub-queries by default and many more in extended-research modes 59 . Microsoft has documented Copilot as decomposing one conversational question into multiple Bing queries 60 . Claude’s web search tool exposes a max_uses parameter capping searches per turn. Perplexity does not publish exact counts. A single user prompt becomes a fan of separate retrieval requests, each evaluated independently.
Stage 2: Search retrieval. Each sub-query is sent to a search index. ChatGPT and Copilot rely on Microsoft’s Bing API; OpenAI also runs OAI-SearchBot to populate its own index. Gemini uses Google Search. Claude appears to use Brave Search (inferred from Anthropic’s subprocessor list, March 2025). Perplexity runs its own crawler. The whole industry sits on three or four indexes - Bing, Google, Brave, Perplexity’s own. AI providers compete hard at the product layer and share the same few indexes underneath.
Stage 3: URL filtering. Returned URLs are filtered before any HTTP fetch is made. Filtering includes deduplication, low-quality-domain demotion, content licensing blocklists, safety and legal policy filters, and regional rules. None of these filters are publicly documented in detail. Robots.txt operates per-bot: OpenAI runs three different crawlers with three different rulebooks (GPTBot for training, OAI-SearchBot for the search index, ChatGPT-User for live fetches). Anthropic and Perplexity have similar splits. The “live fetch” bot is the one that, by design, may not honour robots.txt - OpenAI revised the ChatGPT-User documentation on 9 December 2025 to make this exemption explicit; Perplexity’s own documentation states that Perplexity-User “generally ignores robots.txt rules”. Cloudflare’s August 2025 disclosure that Perplexity was running additional, undeclared crawlers (3-6 million requests per day, IP-rotating, Chrome-on-macOS spoofed) led to Perplexity’s delisting as a verified bot 61 .
Stage 4: Page fetch and content extraction. Surviving URLs are fetched and parsed. None of the major AI crawlers run JavaScript: GPTBot, ClaudeBot, and PerplexityBot fetch raw HTML and bail. Sites depending on client-side rendering are functionally invisible. Soft paywalls (HTML loaded but hidden by overlay) are bypassed automatically; hard paywalls are not. Content is extracted using readability heuristics, Markdown conversion, or proprietary parsers. The exact pipeline is not published by any provider.
Stage 5: Reranking and chunk selection. Fetched content is split into chunks, scored against the query, and the top chunks are retained. Industry-standard practice combines a dense embedding retrieval step (top-25 to top-50) with a cross-encoder reranker producing top-3 to top-5. Anthropic’s web_search_20260209 tool variant lets Claude write code to filter results before they enter the context window, a notable departure from a static reranker pattern 62 .
Stage 6: Context window assembly. The surviving chunks are concatenated with the original prompt and a system prompt instructing citation behaviour. Of all URLs ChatGPT retrieves in the Ahrefs April 2026 sample, roughly half (49.98%) end up cited. Reddit content is cited at 1.93%, despite accounting for the majority of non-cited URLs. The number of sources placed in context per response is generally single digits to low double digits.
Stage 7: Generation with citations. The model generates the response and inserts citations referring to in-context sources. Some implementations tie citations structurally to source spans (Gemini’s groundingSupports model). More attach citations post-hoc to free-text answers, which is where fabricated and broken citations originate. The Tow Center’s March 2025 study (200 queries across 8 tools, 1,600 runs) and the BBC/EBU October 2025 study (2,709 evaluated responses across ChatGPT, Copilot, Perplexity, and Gemini, in 18 countries and 14 languages) are the leading documented surveys of citation accuracy in news contexts.
Stage 8: Post-generation safety pass. Generated responses are checked against safety policy and may be modified or refused. This stage is essentially undocumented at every provider.
The audit in Section 4 measures one specific intersection of Stages 3 and 7: when a citation is emitted, does the cited domain’s robots.txt allow the citing bot? PolicyCheck handles the robots.txt half of that intersection; the prompts and citation parsing handle the other half. The other stages remain measurable in principle and largely opaque in practice.

## Appendix B. Glossary #
AEO - Answer Engine Optimisation. A near-synonym for GEO; emphasises optimising for direct AI answers rather than ranked search results.
Brand-presence check - measuring how often a brand is mentioned in AI responses across many runs of similar prompts; useful for trend tracking, less useful for attribution.
ChatGPT-User - OpenAI’s live-fetch user agent, used when a user (or Custom GPT) directs ChatGPT to read a specific URL. Documented as not necessarily honouring robots.txt.
ClaudeBot - Anthropic’s training crawler.
Citation laundering - an output-side pattern: low-credibility content gains apparent authority by being cited inside an AI response, regardless of the underlying source’s quality. The citation slot itself confers the apparent authority.
Content laundering - an input-side pattern: content moves through intermediaries (data brokers, “trusted” crawlers, aggregators, syndication feeds, or fabricated-authority sites) that strip its original consent, licence, or quality signals before it reaches the AI’s training or retrieval corpus. The classic 2026 case is a third party with publisher-granted crawl access redistributing content to AI agents that the publisher has not granted access to.
content_retrieved - an OpenAttribution event capturing the moment an AI agent fetches a page. Bot identity, URL, response status, timing.
content_grounded - an OpenAttribution event capturing the moment retrieved content is loaded into a model’s working context for a session. Distinct from a citation slot being filled.
content_cited - an OpenAttribution event capturing the moment grounded content is named in a generated response.
content_presented - an OpenAttribution event capturing the moment content or a source reference is made perceivable in the consumer answer surface. Distinct from content_cited , which captures generation by the model; presentation captures whether the citation actually reaches the user. Named content_displayed before the Content Telemetry v1 draft.
content_reproduced - an OpenAttribution event capturing source content appearing verbatim or near-verbatim in an output, credited or not. Added in the Content Telemetry v1 draft; the sibling of content_cited - one records the material, the other the credit.
content_engaged - an OpenAttribution event capturing user interaction with a presented source, referencing the exact presentation occurrence acted on.
Content-Telemetry-ID - a header attached to an AI agent’s request that lets the agent’s own retrieval log and the publisher’s CDN log be matched as two observations of the same event.
Fan-out - the process by which a single user prompt is decomposed into multiple sub-queries before retrieval.
GEO - Generative Engine Optimisation. The discipline of trying to influence what AI assistants say about a brand, product, or topic.
Google-Extended - a Google-defined robots.txt token that publishers use to opt out of having their content used to train Gemini and as grounding for Gemini Apps and Vertex AI. It is not itself a separate crawler.
GPTBot - OpenAI’s training crawler. Honours robots.txt.
Grounding - retrieval-augmented generation in Google’s terminology; the act of basing a generated answer on retrieved content.
OAI-SearchBot - OpenAI’s search-index crawler. Honours robots.txt for indexing purposes.
PerplexityBot - Perplexity’s training and indexing crawler.
Perplexity-User - Perplexity’s live-fetch user agent. Documented as not honouring robots.txt by default.
Prompt monitoring - a method that runs many prompts against one or more AI models, then parses and counts the returned answers or citations to estimate visibility or brand presence.
RAG - Retrieval-Augmented Generation. The process by which a model’s answer is conditioned on retrieved documents rather than generated from training weights alone.
robots.txt - a plain text file at a domain’s root ( example.com/robots.txt ) declaring which crawlers may access which paths. Advisory, not legally binding in most jurisdictions, but the standard public consent signal.
Visibility-percent - the share of AI responses (across many runs of similar prompts) in which a given brand is mentioned. The most defensible probabilistic metric, per Fishkin’s January 2026 research.

## Appendix C. Audit methodology #
This appendix describes the methodology behind the audit reported in Section 4, in sufficient detail for an external researcher to reproduce or contest it. The audit combines two components: 330 prompts submitted to four production AI search APIs, and a dual-bot robots.txt compliance check on every cited domain using PolicyCheck, OpenAttribution’s open-source robots.txt and licensing scanner.
Prompt set. 330 prompts across eleven content categories: Brands, Consumer Electronics, Education, Finance, Food, Health, News, Shopping, Sports, Technology, Travel. Approximately 30 prompts per category. The set is a mix of representative consumer queries (“What are the best wireless earbuds for running?”), topical news questions (“What is the current status of the Nord Stream investigation?”), and brand-specific queries added for the Brands category (“Is Patagonia actually as ethical as they claim?”). The full prompt list is published with the dataset.
Provider APIs. Four production AI search APIs, each run with web_search enabled by default:

- OpenAI Responses API with web_search_preview enabled (model: gpt-5-mini).

- Anthropic Messages API with the web_search tool enabled (model: claude-sonnet-4-6).

- Google Gemini API with google_search grounding (model: gemini-3-flash-preview).

- Perplexity Sonar API (model: sonar).
Consumer surfaces (chatgpt.com, claude.ai, gemini.google.com, perplexity.ai) were not used. The intent is to measure the developer-facing citation surface, which is the population that downstream products built on these APIs will inherit. Each prompt was run three times against each provider, for a total of 3,960 API calls (330 × 4 × 3).
Citation extraction. Cited URLs were extracted programmatically from the API response payloads. No scraping, browser automation, or manual transcription was used. Each citation was associated with a citing provider, a position rank, the source prompt, and the run number.
Dataset. 24,127 citations across 6,798 unique cited domains. Per-provider citation counts: 4,091 from OpenAI, 6,970 from Anthropic, 6,885 from Gemini, 6,181 from Perplexity. Of the 24,127 citations, robots.txt was fetched successfully for 22,263 (92.3%); the remainder returned network or DNS fetch errors and were excluded from violation calculations.
Dual-bot robots.txt check. Each unique cited domain was checked against the PolicyCheck server, which fetched the domain’s /robots.txt and parsed it for per-bot access rules. PolicyCheck parses rules for 28 known AI crawlers; this audit considers two user agents per provider:
Provider Training crawler Live-search bot
OpenAI | GPTBot | OAI-SearchBot |
Anthropic | ClaudeBot | Claude-SearchBot |
Google | Google-Extended | Google-Extended (same agent covers both) |
Perplexity | PerplexityBot | Perplexity-User |
The training crawler is the user agent the provider’s training pipeline identifies as, and is the bot publishers most commonly name when they opt out of AI use. The live-search bot is the user agent the provider’s web_search tool uses at answer time. Publishers’ robots.txt rules rarely name the live-search bot, so under RFC 9309 the live agent is permitted by default in those cases.
Violation flag. A citation was flagged as a training-bot violation when the cited domain’s robots.txt disallowed the provider’s training crawler at the cited path. A live-search-bot violation was flagged when the cited domain disallowed the provider’s live-search bot. “Violation” is shorthand for “citation in apparent disagreement with the cited domain’s expressed crawler preferences”; it does not imply illegality.
Known sources of bias.

- Data licensing deals between specific providers and specific publishers can supersede robots.txt; the audit cannot distinguish a violation from a licensed exception. Known examples in this dataset: Google-Reddit (Feb 2024), OpenAI-Reddit (May 2024), OpenAI-AP (July 2023).

- Proxy and redirect URLs ( vertexaisearch.cloud.google.com and similar) obscure the underlying source. 144 of Gemini’s citations in this run resolved to that proxy alone.

- Each provider may operate multiple live-search agents; only one was tested per provider. If Anthropic or OpenAI ship additional grounding bots, those are not measured.

- Not all API calls produce sources; some prompts returned empty citation arrays. Empty-citation rows are excluded from per-citation rates but retained in the dataset.

- The audit is a single point in time. Robots.txt files and provider citation behaviour change continuously.
Reproducibility. All prompts, code, and output data are published in the OpenAttribution research directory ( policycheck/research/data/enriched_citations_20260515_115259.csv and adjacent files). The rendered HTML report - with every citation, every domain, and every robots.txt match - is at openattribution.org/research/citation-compliance-may-2026 .

## Appendix D. References #
References are organised by the section in which they first appear. Where a source is paywalled, the URL is given followed by [paywalled] .

### Section 1. The opaque pipeline #

- Anthropic, "Web search tool" (developer documentation), `max_uses` parameter. https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool

- Anthropic, subprocessor list (Brave Search inference). https://trust.anthropic.com/subprocessors

- OpenAI, "Overview of OpenAI Crawlers" (platform documentation). https://platform.openai.com/docs/bots

- OpenAI, ChatGPT-User documentation revision, 9 December 2025. Live page: https://platform.openai.com/docs/bots — coverage of the revision: https://ppc.land/openai-revises-chatgpt-crawler-documentation-with-significant-policy-changes/

- Perplexity, "User-Agents" (developer documentation), Perplexity-User "generally ignores robots.txt rules." https://docs.perplexity.ai/guides/bots

- Vercel, "The rise of the AI crawler" (no-JavaScript crawler claim). https://vercel.com/blog/the-rise-of-the-ai-crawler

- Ahrefs, "Why ChatGPT cites pages" (April 2026 analysis of 1.4 million ChatGPT prompts collected February 2025; 49.98% cited; Reddit 1.93%). https://ahrefs.com/blog/why-chatgpt-cites-pages/

- Google, Gemini grounding metadata (`groundingSupports`). https://ai.google.dev/gemini-api/docs/grounding

- Klaudia Jazwinska and Aisvarya Chandrasekar, "AI Search Has A Citation Problem," Tow Center for Digital Journalism, Columbia Journalism Review, March 2025. https://www.cjr.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php

- European Broadcasting Union and BBC, "News Integrity in AI Assistants," October 2025. https://www.ebu.ch/research/open/report/news-integrity-in-ai-assistants — full PDF: https://www.ebu.ch/files/live/sites/ebu/files/Publications/MIS/open/EBU-MIS-BBC_News_Integrity_in_AI_Assistants_Report_2025.pdf

### Section 2. The probabilistic visibility industry #

- Adobe, "Adobe to Acquire Semrush" (press release), 19 November 2025. https://news.adobe.com/news/2025/11/adobe-to-acquire-semrush

- Adobe, completion announcement, 28 April 2026. https://news.adobe.com/news/2026/04/adobe-completes-semrush-acquisition

- Microsoft Clarity, "AI bot activity in Clarity" (Bot Activity dashboard launch), January 2026. https://clarity.microsoft.com/blog/ai-bot-activity-in-clarity/
13a. Microsoft Clarity, Citations dashboard, general availability announced 15 May 2026. Coverage: Search Engine Land, "Microsoft Clarity citations dashboard rolls out." https://searchengineland.com/microsoft-clarity-citations-dashboard-rolls-out-477663 — product: https://clarity.microsoft.com/
14a. AthenaHQ "Prompt Volume" feature (proprietary estimator of how often each prompt is asked of a given LLM); independent third-party math on methodology: https://llmpulse.ai/blog/athenahq-vs-llm-pulse/ — https://writesonic.com/blog/athenahq-review
14b. Malte Landwehr (Peec AI), public reply in r/b2bmarketing thread "Anyone else skeptical about the 'Exact' Prompt Volumes in GEO tools?" Confirms panel-data extrapolation methodology and critiques absolute-number reporting across the category. https://www.reddit.com/r/b2bmarketing/comments/1pov3fy/anyone_else_skeptical_about_the_exact_prompt/
14c. toolsolved.com, "Evertune vs Profound vs Promptwatch: Three GEO Platforms for Enterprise Teams" (April 2026 vendor comparison; "well over 100 tools claiming to help brands win in AI search"). https://toolsolved.com/guides/evertune-vs-profound-vs-promptwatch-three-geo-platforms-for-enterprise-teams-ranked-on-what-they-actually-do-in-2026

- Digiday, "Marketers question expensive AI visibility tools as inconsistent results fuel skepticism" (anonymous-source ~$1,000/month figure; quotes from Paul Dyer, Joseph Levi, Ryan Mason). https://digiday.com/marketing/marketers-question-expensive-ai-visibility-tools-as-inconsistent-results-fuel-skepticism/ [paywalled]

- Rand Fishkin, "NEW Research: AIs are highly inconsistent when recommending brands or products," SparkToro / Gumshoe, January 2026. https://sparktoro.com/blog/new-research-ais-are-highly-inconsistent-when-recommending-brands-or-products-marketers-should-take-care-when-tracking-ai-visibility/

- Ahrefs, "AI search overlap" (15,000-prompt analysis), August 2025. https://ahrefs.com/blog/ai-search-overlap/

- Similarweb, "First Global AI Tracker of 2026" (12-month visit-share comparison: ChatGPT 86.7% to <65%, Gemini 5.7% to >20%). https://x.com/Similarweb/status/2008805674893939041 — coverage: https://www.searchenginejournal.com/google-gemini-gains-share-as-chatgpt-declines-in-similarweb-data/564690/

- impact.com, Evertune partnership press release (Brian Stempeck quote: "over 40% of content either contains affiliate links or is sponsored"), 16 December 2025. https://impact.com/press-releases/impact-com-evertune-partnership-ai-search/

- Evertune, "The new face of ChatGPT shopping: AI product comparisons" (21,000 ChatGPT shopping responses, 11 categories), March 2026. https://www.evertune.ai/resources/insights-on-ai/the-new-face-of-chatgpt-shopping-ai-product-comparisons

- Partnerize, "The hidden half of affiliate revenue: how zero-click VantagePoint finally reveals true incrementality." https://partnerize.com/resources/blog/the-hidden-half-of-affiliate-revenue-how-zero-click-vantagepoint-finally-reveal-true-incrementality

- Partnerize, "From measurable to compensable: the Influence Compensation Lighthouse Program is here," April 2026. https://partnerize.com/resources/blog/from-measurable-to-compensable-the-influence-compensation-lighthouse-program-is-here
23a. Alliance for Audited Media, "Platform and Compliance" industry certifications (independent certification that a platform conforms to its stated methodology). https://auditedmedia.com/industry-certifications/platform-and-compliance

- Evertune, "Partner Connect expands to B2B SaaS partnerships with PartnerStack," 29 January 2026. https://www.evertune.ai/resources/insights-on-ai/partner-connect-expands-to-b2b-saas-partnerships-with-partnerstack — PartnerStack announcement: https://partnerstack.com/articles/partnerstack-and-evertune-turn-ai-search-into-influence-new-integration

- Profound, "Profound & Partnerize partner to turn AI visibility into verified revenue," March 2026. https://www.tryprofound.com/blog/profound-and-partnerize-partner-to-turn-ai-visibility-into-verified-revenue
25b. Profound, "How to track your visibility in AI search" (Visibility Score definition: "the percentage of mentions out of the total responses tracked"; consumer-panel data sourcing). https://www.tryprofound.com/blog/how-to-track-your-visibility-in-ai-search
25c. Profound, "The AI shopping journey: 2025" study. Quotable figure: 79.7% of buyers say they rely on AI Answer Engines for at least half of their purchase decisions. Sample: 1,600 US adults aged 18-99 (screened from 2,739). https://www.tryprofound.com/blog/ai-shopping-journey-2025
25d. Profound, "Ramp increased AI brand visibility 7x in accounts payable" (customer case study). https://www.tryprofound.com/customers/ramp-case-study
25e. Profound funding (Series A $20M, June 2025, Kleiner Perkins lead): https://www.tryprofound.com/blog/series-a — Series B $35M, August 2025, Sequoia lead: https://fortune.com/2025/08/12/ai-search-startup-profound-raises-35-million-series-b-sequoia/ — Series C $96M, February 2026: https://fortune.com/2026/02/24/exclusive-as-ai-threatens-search-profound-raises-96-million-to-help-brands-stay-visible/ [paywalled]
25f. Semrush AI Visibility Index (April 2026: "62% of brands are technically invisible to generative AI models"; Wikipedia 7.8% of ChatGPT citations). https://ai-visibility-index.semrush.com/
25h. SE Ranking, cross-platform AI citation overlap (ChatGPT vs Google AI Overviews ~21.26%). Cited via Momentic Marketing analysis: https://momenticmarketing.com/blog/geo-aio-aeo-seo
25i. Profound, cross-platform AI citation overlap (ChatGPT vs Perplexity 11%; AI Overviews vs Copilot 6 to 10%). Cited via Momentic Marketing analysis: https://momenticmarketing.com/blog/geo-aio-aeo-seo
25j. Profound, regression analysis of 250M+ AI search results (combined backlink-metric r²=0.119; referring domains r²=0.066, total backlinks r²=0.044, authority scores r²=0.009). Cited via Momentic Marketing analysis: https://momenticmarketing.com/blog/geo-aio-aeo-seo

### Section 3. Four structural problems #

- Vivek Pandya, "AI traffic surge: retail sites not machine readable" (Adobe Digital Insights, April 2026; 393% YoY Q1 2026; 693% holiday 2025; conversion +42%; machine-readability gap 82.5% vs 54.2%). https://business.adobe.com/blog/ai-traffic-surge-retail-sites-not-machine-readable

- Matthew Scott Goldstein, .msg newsletter (the "two events: scrape and click" framing). https://www.linkedin.com/in/msgmsg/

- Digiday, "OpenAI has quietly launched its ads manager," February 2026. https://digiday.com/marketing/openai-has-quietly-launched-its-ads-manager-as-it-races-to-build-out-its-ads-business/ [paywalled]

- Digiday, "OpenAI turns on cost-per-click ads inside ChatGPT," 21 April 2026. https://digiday.com/marketing/openai-turns-on-cost-per-click-ads-inside-chatgpt/ [paywalled] — companion piece on CPM drift: https://digiday.com/marketing/everything-is-coming-down-chatgpt-ads-are-getting-cheaper/ [paywalled]

- The Information, "OpenAI forecasts advertising to hit $102 billion by 2030." https://www.theinformation.com/articles/openai-forecasts-advertising-hit-102-billion-2030 [paywalled] — Axios scoop: https://www.axios.com/2026/04/09/openai-100-billion-in-ad-revenue
30a. Google Search Central, "AI optimization guide" (developer documentation), May 2026. Explicitly reframes GEO as SEO ("From Google Search's perspective, optimizing for generative AI search is optimizing for the search experience, and thus still SEO"); rejects llms.txt and AI-specific schema; no measurement guidance. https://developers.google.com/search/docs/fundamentals/ai-optimization-guide

- Press Gazette, "News generative AI deals revealed: who is suing, who is signing?" (publisher-AI deal tracker, updated continuously). https://pressgazette.co.uk/platforms/news-publisher-ai-deals-lawsuits-openai-google/

- *In re OpenAI Copyright Litigation* (consolidated MDL combining 16 lawsuits including *NYT v. OpenAI*), SDNY court order, 5 January 2026 (Judge Sidney H. Stein), forcing production of 20 million ChatGPT logs. Bloomberg Law: https://news.bloomberglaw.com/ip-law/openai-must-turn-over-20-million-chatgpt-logs-judge-affirms [paywalled] — National Law Review: https://natlawreview.com/article/openai-loses-privacy-gambit-20-million-chatgpt-logs-likely-headed-copyright

- Cloudflare, "From clicks to crawls: AI bots are dominating training traffic" (crawl-to-refer ratios: Anthropic 38,065:1, OpenAI 1,091:1, Perplexity 194:1, Google 5.4:1), mid-2025. https://blog.cloudflare.com/crawlers-click-ai-bots-training/

- Joe Weisenthal and Tracy Alloway, "Google's Liz Reid on who will own search in a world of AI," *Bloomberg Odd Lots*, 23 April 2026. https://www.bloomberg.com/news/audio/2026-04-23/odd-lots-google-s-liz-reid-on-search-in-an-ai-world-podcast [paywalled]
34a. Haofei Xu, Umar Iqbal, and Jacob M. Montgomery, "Measuring Google AI Overviews: Activation, Source Quality, Claim Fidelity, and Publisher Impact," Washington University in St. Louis, arXiv:2605.14021, 13 May 2026. https://arxiv.org/abs/2605.14021 — see also the [related research summary](/research/related#wustl-google-aio-2026).

- Matthew Scott Goldstein, commentary on the Reid interview, .msg newsletter, late April / early May 2026. https://www.linkedin.com/in/msgmsg/

- Internal capture of ChatGPT response to "sony wh-1000xm5 vs bose qc ultra?" citing wh1000xm5.co.uk alongside Wired, April 2026. Working-paper exhibit, on file with OpenAttribution.

- Rolling Stone, robots.txt (blocks GPTBot, ClaudeBot, Google-Extended). https://www.rollingstone.com/robots.txt

- Ahrefs Firehose, "real-time data streaming API," launched mid-March 2026, free during beta. https://firehose.com/ — API documentation: https://firehose.com/api-docs

- *Reddit, Inc. v. Perplexity AI, Inc., Oxylabs UAB, AWM Proxy LLC, and SerpApi LLC*, SDNY, filed 22 October 2025. Bloomberg coverage: https://www.bloomberg.com/news/articles/2025-10-22/reddit-sues-perplexity-others-over-alleged-data-scraping [paywalled] — SDNY blog summary: https://www.sdnyblog.com/reddit-sues-perplexity-ai-and-data-scrapers-for-industrial-scale-theft-of-valuable-copyrighted-content/

- NewsGuard, "One-year AI audit progress report" (35% false-claim rate vs 18% prior year), 4 September 2025. https://www.newsguardtech.com/press/newsguard-one-year-ai-audit-progress-report-finds-that-ai-models-spread-falsehoods-in-the-news-35-of-the-time/ — ongoing tracker: https://www.newsguardtech.com/ai-false-claims-monitor/

- NewsGuard, "A well-funded Moscow-based global 'news' network has infected Western artificial intelligence tools" (Pravda network: 150 domains, 3.6M articles), March 2025. https://www.newsguardrealitycheck.com/p/a-well-funded-moscow-based-global

### Section 4. A reproducible audit #

- OpenAttribution citation compliance audit, May 2026. Dual-bot prompt-to-citation audit across OpenAI, Anthropic, Google Gemini, and Perplexity, cross-referenced against robots.txt via PolicyCheck. Methodology, prompts, code, and output dataset: https://github.com/openattribution-org/policycheck/tree/main/research — rendered report: https://openattribution.org/research/citation-compliance-may-2026
42a. Reuters, "Reddit signs $60 million content licensing deal with Google" (training and grounding access for Reddit content), 22 February 2024. https://www.reuters.com/technology/reddit-signs-ai-content-licensing-deal-with-google-bloomberg-news-reports-2024-02-22/
42b. OpenAI, "OpenAI and Reddit Partnership" (announcement of content-access agreement for ChatGPT and OpenAI products), 16 May 2024. https://openai.com/index/openai-and-reddit-partnership/
42c. Associated Press, "AP, Open AI agree to share select news content and technology in new collaboration," 13 July 2023. https://www.ap.org/media-center/press-releases/2023/ap-open-ai-agree-to-share-select-news-content-and-technology-in-new-collaboration/

- PolicyCheck (robots.txt, RSL, TDM, Content Signals scanner). https://github.com/openattribution-org/policycheck — live API: https://policycheck-d7wv0g.fly.dev — web UI: https://openattribution.org/policycheck/

- Output dataset for the May 2026 run: `policycheck/research/data/enriched_citations_20260515_115259.csv` and adjacent files.

- Provider APIs used in the audit:
- OpenAI Responses API with `web_search_preview`. https://platform.openai.com/docs/guides/tools-web-search?api-mode=responses
- Google Gemini API with `google_search` grounding. https://ai.google.dev/gemini-api/docs/grounding
- Perplexity Sonar API. https://docs.perplexity.ai/api-reference/chat-completions-post

### Section 5. What deterministic measurement looks like #

- Anthropic, `web_search_result` blocks. Same as ref. 1.

- Perplexity API, `citations` array. https://docs.perplexity.ai/api-reference/chat-completions-post

- OpenAttribution Cloudflare Worker (open source). https://github.com/openattribution-org/cloudflare-worker

- Coalition for Content Provenance and Authenticity (C2PA). https://c2pa.org

- Cloudflare Bot Management. https://www.cloudflare.com/application-services/products/bot-management/

- RSL standard. https://rslstandard.org/

- IAB Tech Lab, Content-Owner Monetisation Protocol (CoMP). https://iabtechlab.com/press-releases/iab-tech-lab-announces-comp-framework-to-ensure-llms-have-commercial-agreements-with-publishers-before-content-crawling/

- Peek-Then-Pay specification. https://peekthenpay.org/

- OpenAttribution AIMS (agent identity manifests). https://github.com/openattribution-org/aims

### Section 7. Where this goes next #

- OpenAttribution Limited, UK CLG no. 17002582, Companies House. https://find-and-update.company-information.service.gov.uk/company/17002582

- OpenAttribution / Martech Record / The Drum London event, 17 June 2026. https://martechrecord.com/upcoming-events/ai-attribution-reception-discussion/

- OpenAttribution dashboard. https://openattribution.org

- OpenAttribution GitHub. https://github.com/openattribution-org

### Appendix A. The pipeline in detail #

- Google, "How Google AI visual search works" (Google AI Mode multi-query behaviour). https://blog.google/company-news/inside-google/googlers/how-google-ai-visual-search-works/

- Microsoft Bing Search Blog, "Introducing Copilot Search in Bing," April 2025. https://blogs.bing.com/search/April-2025/Introducing-Copilot-Search-in-Bing

- Cloudflare, "Perplexity is using stealth, undeclared crawlers to evade website no-crawl directives," August 2025. https://blog.cloudflare.com/perplexity-is-using-stealth-undeclared-crawlers-to-evade-website-no-crawl-directives/

- Anthropic, `web_search_20260209` tool variant. https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool

End matter

## Get the PDF
Print-ready, with the full reference list. We use your email only to send the
paper and notify you about substantive revisions to the audit data.

Work email
Get the PDF The full paper is on this page already — no email required. The PDF is the same
content, formatted for print and offline reading.
← All research

#### Open Attribution
Open standards for AI content transparency.
Runs on OpenAttribution

##### Get started

- Check your domain

- Claim your domain

- How it works

- FAQ

##### Standards

- Documentation

- Content Telemetry standard

- Developer SDKs

##### Resources

- Contact

- GitHub

- Governance

- Service privacy

- Website privacy

- Terms

- Security

© 2026 OpenAttribution. All rights reserved.
