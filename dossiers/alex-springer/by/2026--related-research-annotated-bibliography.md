---
title: "Related research — annotated bibliography of independent AI-retrieval and citation studies"
person: "alex-springer"
section: "by"
type: "report"
year: 2026
venue: "OpenAttribution (Research)"
authors: "OpenAttribution (no personal byline; see notes)"
source_url: "https://openattribution.org/research/related/"
retrieved: "2026-08-13"
content: "full-text"
notes: "Curated, annotated bibliography: each entry summarises an external study and adds a 'Why it matters for OpenAttribution' commentary. No personal byline; attributed to OpenAttribution, whose sole public author is Alex Springer (see 2026--measuring-content-influence-in-ai-assistants.md notes). Undated page; year from site."
---

# Related research — annotated bibliography of independent AI-retrieval and citation studies

## Full text

# Related research
Independent academic and industry work that informs or extends the OpenAttribution
research programme. Each entry is summarised with what it measured, what it found, and
where it fits with the open standards work.
13 May 2026 · Washington University in St. Louis · arXiv:2605.14021

## Measuring Google AI Overviews: Activation, Source Quality, Claim Fidelity, and Publisher Impact
Haofei Xu, Umar Iqbal, Jacob M. Montgomery
Forty-day longitudinal audit of Google AI Overviews. 55,393 trending queries across 19 topical categories produced 7,583 AIOs, which the authors then decomposed into 98,020 atomic factual claims and verified against the full text of every cited reference page. The first large-scale measurement study to simultaneously characterise AIO activation, source selection, claim fidelity, and publisher economic exposure on a naturalistic, sustained query sample.

### Key findings

- — Overall AIO activation is 13.7%, but rises to 64.7% for question-form queries and falls as low as 7.5% for Politics and 9.6% for Law & Government - non-uniform suppression that is not publicly documented.

- — 29.8% of AIO-cited domains do not appear on the corresponding first-page SERP at all (28.5% at the URL level). The retrieval pool is a separate selection mechanism from Google’s own ranking algorithm.

- — AIO-cited domains are systematically more credible than co-displayed first-page results (+0.087 on the PC1 credibility scale), contradicting prior work that found AIOs draw on lower-quality sources.

- — 11.0% of atomic claims are unsupported by their cited references, dominated by silent omission (7.0%) rather than active contradiction (2.7%) - a failure mode no reader of the AIO can detect.

- — 50.6% of AIO-cited publisher pages carry display advertising, and Google’s own sponsored search ads continue to appear on the same SERP, in some cases above the AIO. The deployment is asymmetric: it suppresses publisher click-throughs while preserving Google’s ad capture.

### Why it matters for OpenAttribution
Independent academic confirmation of the OpenAttribution thesis on the one large AI surface our own May 2026 audit cannot reach (our API-based audit uses Gemini’s developer grounding tool, not the consumer AIO surface). The 29.8% off-SERP citation finding is a direct empirical case for treating retrieval as an event distinct from ranking - which is exactly what the content_retrieved event in the OA event vocabulary captures. The 50.6% ad-bearing finding gives the publisher-leverage argument in §3.3 a quantified economic exposure number. The 11.0% unsupported-claim rate, with omission as the dominant failure mode, is the kind of grounded-vs-cited gap a content_grounded ↔ content_cited correlation would let publishers and regulators detect at scale.
Cited in our May 2026 working paper: §3.3 The publisher leverage problem, §4.5 What this audit cannot see .
Read the source 22 October 2025 · EBU / BBC · EBU MIS report

## News Integrity in AI Assistants
European Broadcasting Union and BBC, coordinated across 22 Public Service Media organisations
The largest coordinated audit of AI-assistant news accuracy to date. 22 Public Service Media organisations across 18 countries and 14 languages evaluated 2,709 responses from the free versions of ChatGPT, Microsoft Copilot, Perplexity, and Google Gemini against editorial criteria covering accuracy, sourcing, distinguishing fact from opinion, and providing context.

### Key findings

- — 45% of responses contained at least one significant issue, and 81% contained an issue of some kind. The result reproduced across languages and countries.

- — Sourcing was the single largest category of significant issue, present in 31% of responses overall - more than accuracy, context, or opinion-handling.

- — Significant-issue rates varied sharply by assistant: Gemini 76%, Copilot 37%, ChatGPT 36%, Perplexity 30%.

- — Significant sourcing issues specifically: Gemini 72%, ChatGPT 24%, Perplexity 15%, Copilot 15%. The per-assistant sourcing problem is not uniform across the market.

- — Sourcing failures counted include claims not supported by the cited source, no source provided, and incorrect sourcing claims - the same failure modes a grounded-vs-cited event correlation would expose deterministically.

### Why it matters for OpenAttribution
The cross-organisation, cross-language design raises the evidentiary bar that any single national-level audit can clear, and the headline finding - that sourcing is the dominant failure mode across the four leading consumer surfaces - is exactly the failure mode the content_grounded and content_cited events in the OA vocabulary are designed to make visible. 22 PSM organisations documenting the same pattern in the same study is the kind of body of evidence that justifies a shared measurement standard rather than per-vendor dashboards.
Cited in our May 2026 working paper: §1 The opaque pipeline .
Read the source 6 March 2025 · Tow Center for Digital Journalism, Columbia Journalism Review · Columbia Journalism Review

## AI Search Has A Citation Problem
Klaudia Jazwinska, Aisvarya Chandrasekar
The reference audit for the first generation of AI search products. 200 article excerpts were drawn from across 20 publishers and queried against 8 generative AI search tools - ChatGPT Search, Perplexity, Perplexity Pro, Gemini, DeepSeek Search, Grok-2, Grok-3, and Microsoft Copilot - for 1,600 total queries. The authors evaluated whether each tool could correctly identify the article, its original publisher, and a working URL.

### Key findings

- — Across all tools, more than 60% of responses were incorrect - either the citation pointed to the wrong source, the URL was fabricated or broken, or the article was misidentified.

- — Paid premium tools were not more accurate. Perplexity Pro and Grok 3 - the most expensive products in the sample - returned higher rates of confidently wrong answers than their free counterparts, because they almost never declined to answer.

- — 5 of the 8 tools accessed and cited content from publishers whose robots.txt explicitly blocked the citing crawler. The opt-out signal was not enforced at the citation layer.

- — Tools rarely refused to answer or hedged when they did not have the source: 154 of 1,600 responses from ChatGPT Search were partially correct or correct with caveats; the rest were assigned full confidence. Confident misattribution was the norm, not an edge case.

- — Citations were frequently to syndicated copies on aggregator sites rather than to the original publisher - the kind of attribution drift that destroys publisher leverage even when a citation slot is technically filled.

### Why it matters for OpenAttribution
The first systematic measurement of the citation surface that the OA event vocabulary is built around. The Tow Center pre-dated almost all of the GEO industry and most of the licensing deals that have since complicated the picture - it is the cleanest baseline against which to measure whether anything has improved in the year since. The robots.txt finding directly parallels OpenAttribution’s May 2026 PolicyCheck audit (§4 of the working paper): citations from blocked domains are not a 2026 invention, they were already documented in March 2025 and have persisted across two model generations. The "confident-misattribution" pattern is the failure mode a paired content_grounded / content_cited record would catch by construction, because the model could no longer cite a source it did not retrieve.
Cited in our May 2026 working paper: §1 The opaque pipeline, Appendix A — Stage 7: Generation with citations .
Read the source

## Suggest a paper
If you have published or come across independent measurement work on AI retrieval,
citation, claim fidelity, publisher economics, or the regulatory surface around any of
these, we would like to read it. Open standards depend on a body of evidence that
travels beyond any one organisation.
Send it to [email protected] or open an issue at github.com/openattribution-org .
