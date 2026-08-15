---
title: "Get The Research: Impactstory Announces a New Science-Finding Tool for the General Public"
person: jason-priem
section: by
type: interview
year: 2018
date: 2018-11-12
venue: "The Scholarly Kitchen"
authors: "Rick Anderson (interviewer); Jason Priem (interviewee)"
source_url: https://scholarlykitchen.sspnet.org/2018/11/12/get-the-research-impactstory-announces-a-new-science-finding-tool-for-the-general-public/
retrieved: 2026-08-13
content: full-text
notes: "Open access. Live site blocks scripted fetches (Cloudflare); text retrieved from Wayback Machine snapshot (2019). Q&A: Rick Anderson questions in bold-style, answers are Priem's words. Comment thread omitted."
---

# Get The Research: Impactstory Announces a New Science-Finding Tool for the General Public

## Full text

Impactstory recently announced a new tool in development. Called, "Get The Research" and aimed at serving the general public rather than an audience of scholars and specialists, it promises to provide a new level of accessibility (in multiple senses of the term) to published scholarship. I asked Impactstory cofounder Jason Priem a few questions about how this new tool will work.

**Give us a quick overview of what this new tool does and how it does it.**

Get The Research is a website where regular people can find, read, and understand the scholarly research on any topic. It'll be built on the 20 million open access articles in the Unpaywall index, and feature AI-powered tools that help make the content and context of scholarly articles more clear to readers. We won't be dumbing down or interpreting science, but we will be giving motivated readers scaffolding to help them build their understanding.

There are a lot of risks — and commensurate rewards — with a project this ambitious. We're dealing with that by building the system in three levels, each with increasing risk and reward. The idea is that even if the riskiest parts fail, we'll still have something useful to show for our efforts.

- A search engine on the Unpaywall database. It'll allow anyone to search our corpus of 20M OA articles for free. It'll also offer an open API, allowing anyone to leverage our search infrastructure for their own projects, commercial or otherwise.
- Learning tools built on top of the literature. This will include an automatic annotation layer that will flag up difficult jargon, get definitions from Wikipedia, and show them in the margins. We want to build an experience like reading Hamlet for school, where the tough words are explained for you as you read. It'll also include ways to traverse a subject area (e.g., recommended articles, relevant lit reviews, etc.) and categorizations of articles (randomized controlled trial [RCT], non-peer-reviewed, systematic review, etc.).
- Tools that actually translate articles into plain language…something Simple Wikipedia does for regular Wikipedia, but done automatically (we probably wouldn't go full Up Goer 5 but that's another fun example). This is pretty hard, and may not work. We'll certainly be proceeding cautiously here, given the risks of mistranslation.

**How does Get the Research interact with Unpaywall? Does the former replace the latter, or are they complementary tools?**

Unpaywall is an open database of 20M free scholarly articles, harvested from over 50,000 publishers and repositories.

Get The Research will be a free search engine that helps people find and understand papers in the Unpaywall database.

**You've said that one important aspect of Get the Research is that it provides not only access to the content, but also to the context of the research literature. Tell us more about that.**

By "context," we mean the subject matter knowledge that makes an article understandable for a specialist, but hard or impossible to read for everyone else. That includes everything from field-specific jargon, to strategies for skimming to key findings, to knowledge of core concepts like p-values. Specialists have access to that kind of context. Non-specialists don't. This makes reading the scholarly literature like reading Shakespeare without notes: you get glimmers of beauty, but without some help it's mostly just frustrating — unless you've put in the years of study needed to grok the context.

**How (if at all) does Get the Research interact with sites like ResearchGate and Sci-Hub?**

Not at all. We don't use Sci-Hub because it's illegal (more on our thoughts about Sci-Hub here). We don't use ResearchGate (RG) because, unlike credible institutional and disciplinary repositories:

- RG works hard to keep people from indexing or harvesting its "open" content.
- Half of RG content is posted illegally.
- RG makes no effort to ensure persistence of author-uploaded content.

**One of your stated goals with this product is to provide access to "trustworthy research about anything." What are your criteria of trustworthiness, and how do you filter out the stuff that doesn't meet those criteria?**

Someday, it would be cool to try and quantify trustworthiness automatically, using information about authors, the citation graph, clinical guidelines, and so on…there are certainly lots of interesting efforts in automated credibility detection right now, much of it directed at spotlighting fake news.

However, our approach for now is much more modest. Simply by limiting search to peer-reviewed literature, we improve the trustworthiness of content quite a lot, compared to many other free-to-read sources that readers encounter online. We'll also be automatically flagging up articles with characteristics likely to make them extra useful (for instance systematic reviews, meta-studies, large-sample RCTs, and so on). We'll be hiding retracted papers. And importantly, we'll be working to educate readers on why those types of articles are more generalizable than, say, small-scale case studies.

**Does this product rely on any kinds of partnerships with publishers?**

We're exploring that, and have had some promising discussions.

**What kinds of projects are on the horizon for Impactstory?**

Our goal is to build open infrastructure to support the Open Science revolution, and there's certainly no shortage of things to do there. We've got quite a few exciting projects in the pipeline! Here are a few that spring quickly to mind:

- Enlarging the scope of the Unpaywall dataset to include research papers without DOIs, which will add 50M or so new fulltext records.
- Disambiguating all the authors of all scholarly papers, along with their institutions, and then making that dataset available to anyone for free. We'll use ORCID where we can, and AI everywhere else. We think this would be quite useful in many assessment contexts, as well as in building cool tools that interact with academic authorship and identity.
- Using Unpaywall to assess the openness of faculty publishing behaviors (i.e., the percentage of an faculty's papers that are available OA, that are associated with open data and open code, etc.), with the goal of increasing openness over time. Unpaywall data is already being used in national-level assessments by policy bodies in the Netherlands, Switzerland, the UK, and elsewhere. We're building a web-based dashboard to support doing the same at the institutional or departmental level, and are currently trialing this system with the US National Institutes of Mental Health.
- Building a research software citation index, by mining research software mentions and citations from our fulltext records.
- Supporting an easy-to-use, fully-open API for altmetrics, built on the Crossref Event Data system.
