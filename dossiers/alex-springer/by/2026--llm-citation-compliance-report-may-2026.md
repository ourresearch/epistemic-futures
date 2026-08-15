---
title: "LLM Citation Compliance Report — May 2026"
person: "alex-springer"
section: "by"
type: "report"
year: 2026
date: "2026-05-15"
venue: "OpenAttribution (Research)"
authors: "OpenAttribution (no personal byline; see notes)"
source_url: "https://openattribution.org/research/citation-compliance-may-2026/"
retrieved: "2026-08-13"
content: "full-text"
notes: "Published under an organisational byline ('Published by OpenAttribution' / 'produced by OpenAttribution'), with no personal byline on the page. Filed in by/ because OpenAttribution Limited (UK company 17002582) has one public author: all six of the site's bylined blog posts read 'By Alex Springer', he is its founding director (Companies House, appointed 2026-01-30), and he is the sole listed contributor on every openattribution-org and SPUR-Coalition GitHub repository. Personal authorship is therefore inferred from those facts, not stated on the document itself."
---

# LLM Citation Compliance Report — May 2026

## Full text

Open Attribution

Home

PolicyCheck

Blog

# LLM Citation Compliance Report

When developers build AI agents with web search, the foundation model chooses what to cite. How often do those citations come from sources that have asked not to be crawled?

Data collected 15 May 2026 · 24127 citations · 6798 domains

## Headlines

330

Prompts

24127

Citations

6798

Unique domains

7.8%

Blocked by publisher's
AI-training opt-out signal

2.1%

Blocked by publisher's
live-search opt-out signal

11

Categories

Each citation is checked against two bots per provider: the
training crawler (the one publishers usually
name in robots.txt when they opt out of AI use)
and the live-search bot (the user agent the
provider's web_search tool actually uses at answer time).
Publishers' opt-out signals rarely name the live-search bot,
so the two rates can diverge sharply. Both numbers measure the
same providers, the same prompts, and the same cited URLs.

## Why This Matters

For agent builders and developers

These results come from the same APIs that any developer uses to build AI-powered products — OpenAI's Responses API, Google's Gemini API, Perplexity's Sonar API — all with web search enabled. When you integrate one of these APIs into an agent, app, or workflow, the foundation model decides which sources to cite. You have no visibility into whether those sources have consented to being crawled by that provider.

A publisher sets robots.txt to block GPTBot. You call the OpenAI API with web search. The API returns a citation from that publisher. Your agent surfaces it to the end user. At no point in this chain did anyone check whether the source said yes. You inherit a compliance posture you cannot inspect, from a foundation model you do not control, citing sources whose preferences you have no way to verify.

For brands considering AI search visibility

If you are evaluating publishers as partners, or assessing where your brand appears in AI search results, the compliance status of cited sources matters. A publisher that blocks AI crawlers but still appears in AI-generated answers has an unresolved tension in their content strategy — and any partnership built on that visibility sits on uncertain ground.

Understanding which sources are cited in compliance with their own stated policies, and which are not, helps you make better decisions about where to invest in content partnerships and where AI-driven traffic is sustainable.

For publishers

If you have set robots.txt to block an AI provider's crawler, you have stated your position clearly. This data shows whether that preference is being respected when that provider generates answers with web search. Your content may still be surfaced to users through AI search despite your explicit opt-out.

This is not about whether robots.txt is legally enforceable — it is about whether the signals publishers already use are having their intended effect, and where the gaps are.

## Violation Rate by Provider

A "violation" occurs when an AI search engine cites a domain whose robots.txt blocks the relevant provider bot. Two bots are checked per provider: the training crawler (the bot most publishers name when they opt out of AI use) and the live-search bot (the user agent the provider's web_search tool actually uses). The two rates can diverge sharply because publishers' opt-out signals usually name only the training bot.

Anthropic — training bot: ClaudeBot

14.4%

934/6469 from blocked domains

Live-search bot: Claude-SearchBot

2.4%

154/6469 from blocked domains

Gemini — training bot: Google-Extended

4.2%

274/6454 from blocked domains

Same bot covers both training and live grounding.

OpenAI — training bot: GPTBot

14.5%

517/3576 from blocked domains

Live-search bot: OAI-SearchBot

1.1%

39/3576 from blocked domains

Perplexity — training bot: PerplexityBot

0.1%

6/5764 from blocked domains

Live-search bot: Perplexity-User

0.1%

6/5764 from blocked domains

## Violation Rate by Category

Different content categories show different violation rates. Categories with high-value editorial content (news, health, finance) tend to have higher blocking rates.

## Category Breakdown

Category
Citations
Domains
Checked
Blocked
Rate

Brands |
2227 |
747 |
2077 |
151 |
7.3% |

Consumer Electronics |
2107 |
505 |
2023 |
178 |
8.8% |

Education |
2001 |
655 |
1822 |
149 |
8.2% |

Finance |
2486 |
710 |
2284 |
124 |
5.4% |

Food |
1523 |
457 |
1454 |
69 |
4.7% |

Health |
2730 |
721 |
2360 |
142 |
6.0% |

News |
2417 |
751 |
2164 |
302 |
14.0% |

Shopping |
2226 |
865 |
2093 |
142 |
6.8% |

Sports |
1895 |
365 |
1795 |
125 |
7.0% |

Technology |
2094 |
646 |
1973 |
190 |
9.6% |

Travel |
2421 |
983 |
2218 |
159 |
7.2% |

## Top Cited Domains

The 20 most frequently cited domains across all providers and prompts, coloured by whether the domain blocks the citing provider's bot.

## Citation Rank: Blocked vs Allowed

Do blocked sources appear at higher or lower citation ranks? Lower rank numbers mean the source was cited earlier (more prominently) in the response.

Mean rank for allowed sources: 4.4 . Mean rank for blocked sources: 4.1 .

## Top Violators

Domains that were both frequently cited and block the citing provider's crawler.

Domain
Times cited
Blocks

reddit.com |
259 |
Gemini (Google-Extended), OpenAI (GPTBot) |

espn.com |
127 |
OpenAI (GPTBot) |

medium.com |
106 |
Anthropic (ClaudeBot) |

apnews.com |
86 |
OpenAI (GPTBot) |

skysports.com |
86 |
OpenAI (GPTBot) |

cnn.com |
62 |
Anthropic (ClaudeBot) |

cbsnews.com |
60 |
OpenAI (GPTBot) |

aljazeera.com |
59 |
Anthropic (ClaudeBot), OpenAI (GPTBot) |

### Methodology

Every citation in this report comes directly from the providers' own APIs with their built-in web search tools enabled — not from the consumer web portals (chatgpt.com, gemini.google.com, perplexity.ai). Specifically: OpenAI's Responses API with web_search_preview , Google's Gemini API with google_search grounding, and Perplexity's Sonar API (which includes web search by default). Each prompt was submitted through these official APIs and the cited URLs were extracted programmatically exactly as returned — no scraping, no browser automation, no modification of results.

Each unique cited domain was then checked against the PolicyCheck server, which fetches and parses the domain's robots.txt to determine per-bot access status for 26 known AI crawlers.

A citation is flagged as "blocked" when the cited domain's robots.txt disallows the citing provider's primary crawler: GPTBot for OpenAI, Google-Extended for Gemini, PerplexityBot for Perplexity.

Robots.txt was successfully fetched for 92% of citation lookups (1863 fetch errors). Domains that returned fetch errors are excluded from violation calculations.

This is a point-in-time snapshot. Robots.txt policies and LLM citation behaviour change over time. This report should not be interpreted as evidence of illegality — robots.txt is advisory, not legally binding in all jurisdictions.

## Limitations and Nuance

Robots.txt is a useful public signal, but it does not tell the whole story. Several patterns in this data illustrate why.

Data licensing deals bypass robots.txt

Reddit blocks every crawler with a blanket User-agent: * / Disallow: / . Yet Gemini cited reddit.com 14 times in this dataset — and it was the only provider to do so. OpenAI and Perplexity, who do not have a data deal with Reddit, never cited it.

Google has a reported data licensing agreement with Reddit. The content reaches Gemini through a direct feed, not through crawling. The robots.txt is technically blocking Google-Extended, but that is irrelevant when the data arrives via a commercial API.

This means a "blocked" status in robots.txt does not necessarily mean the provider lacks access. Private data deals create a layer of access that is invisible to any public compliance check. For agent builders and publishers alike, the observable signal (robots.txt) and the actual access (licensed feed) can diverge completely.

Proxy and redirect URLs obscure real sources

Gemini's API sometimes returns citations pointing to vertexaisearch.cloud.google.com/grounding-api-redirect/... instead of the actual source URL. 144 citations in this dataset were redirect URLs rather than real domains. These cannot be meaningfully checked for compliance because they are opaque intermediaries — the real source domain is hidden behind Google's redirect layer.

This is a transparency gap: the agent builder receives a citation but cannot determine the true source without following the redirect. It makes independent compliance verification harder.

Missing citations: not all API calls produce sources

307 API responses in this dataset returned no citations at all despite web search being enabled. 281 of these were from OpenAI, which produced citations for only 4091 of its 4372 responses. By contrast, Gemini and Perplexity almost always returned cited sources.

This does not mean OpenAI's answers were unsourced — the model may have used web search internally but not surfaced the citations in the API response. However, it means the compliance picture for OpenAI is based on a smaller sample of citations relative to the number of queries.

## About

This report was produced by OpenAttribution using PolicyCheck for compliance checking. All data, prompts, and code are published in the research directory for reproducibility.

Source data: output/enriched_citations_20260515_115259.csv

© 2026 OpenAttribution . All rights reserved.

Built with PolicyCheck
