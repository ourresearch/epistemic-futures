---
title: "The Attribution Crisis in LLM Search Results: Estimating Ecosystem Exploitation"
person: tim-oreilly
section: by
type: report
year: 2025
date: 2025-06-27
venue: "arXiv:2508.00838 / AI Disclosures Project, SSRC (published in Data & Policy, Cambridge University Press)"
authors: "Ilan Strauss; Jangho Yang; Tim O'Reilly; Sruly Rosenblat; Isobel Moure"
source_url: https://arxiv.org/abs/2508.00838
retrieved: 2026-08-13
content: full-text
notes: "Open arXiv preprint PDF; text extracted with pdftotext -layout. Journal version: Data & Policy (Cambridge University Press), DOI 10.1017/dap.2026.10064."
---

# The Attribution Crisis in LLM Search Results: Estimating Ecosystem Exploitation

## Full text

The Attribution Crisis in LLM Search Results
                                                                   Estimating Ecosystem Exploitation

                                            Ilan Strauss1,2 , Jangho Yang4 , Tim O’Reilly1,3 , Sruly Rosenblat1 , and Isobel Moure ∗1

                                                              1 AI Disclosures Project (Social Science Research Council)

                                                      2 Institute for Innovation and Public Purpose (University College London)

arXiv:2508.00838v1 [cs.DL] 27 Jun 2025
                                                                                     3 O’Reilly Media

                                                                                 4 University of Waterloo

                                                                                         Abstract

                                                   Web-enabled LLMs frequently answer queries without crediting the web pages they
                                                consume, creating an “attribution gap” – the difference between relevant URLs read and
                                                those actually cited. Drawing on approximately 14,000 real-world LMArena conversa-
                                                tion logs with search-enabled LLM systems, we document three exploitation patterns:
                                                1) No Search: 34% of Google Gemini and 24% of OpenAI GPT-4o responses are gen-
                                                erated without explicitly fetching any online content; 2) No citation: Gemini provides
                                                no clickable citation source in 92% of answers; 3) High-volume, low-credit: Per-
                                                plexity’s Sonar visits approximately 10 relevant pages per query but cites only three
                                                to four. A negative binomial hurdle model shows that the average query answered
                                                by Gemini or Sonar leaves about 3 relevant websites uncited, whereas GPT-4o’s tiny
                                                uncited gap is best explained by its selective log disclosures rather than by better at-
                                                tribution. Citation efficiency – extra citations provided per additional relevant web
                                                page visited – varies widely across models, from 0.19 to 0.45 on identical queries, un-
                                                derscoring that retrieval design, not technical limits, shapes ecosystem impact. We
                                                recommend a transparent LLM search architecture based on standardized telemetry
                                                and full disclosure of search traces and citation logs.

                                                Keywords: LLM Search, citations, content monetization, ecosystem exploitation, large
                                                language models.

                                            ∗
                                             We gratefully acknowledge funding support from The Alfred P. Sloan Foundation, the Omidyar Net-
                                         work, and the Patrick J. McGovern Foundation. We extend our appreciation to the people we have had
                                         conversations with that have shaped our thinking. Contact: istrauss@ssrc.org / ilan@aidisclosures.org. Code
                                         and Data: https://github.com/AI-Disclosures-Project/Ecosystem_Exploitation_In_Search_Results.
Contents
1 Introduction                                                                                1

2 Data and Method                                                                             4
  2.1   Key Variables and Measurement . . . . . . . . . . . . . . . . . . . . . . . . .       5

3 Descriptive Patterns                                                                        6

4 Regression Models                                                                           7
  4.1   Hurdle-Model Specification . . . . . . . . . . . . . . . . . . . . . . . . . . . .    7
  4.2   Head-to-Head Model Comparison Regression . . . . . . . . . . . . . . . . . .          9

5 Regression Findings                                                                        10
  5.1   Attribution Gap Regression Model . . . . . . . . . . . . . . . . . . . . . . .       10
  5.2   Head-to-Head Model Results: Citation efficiency . . . . . . . . . . . . . . . .      12

6 Policy Implications                                                                        14

7 Conclusion                                                                                 16

8 Appendix                                                                                   21
  8.1   Full Hurdle-Model Specification and Diagnostics . . . . . . . . . . . . . . . .      21
  8.2   Detailed Model Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   22
  8.3   Head-to-Head Regressions: Table of results . . . . . . . . . . . . . . . . . . .     25
1         Introduction
          “The misery of being exploited by capitalists is nothing compared to the misery
          of not being exploited at all.” – Joan Robinson, Economic Philosophy, 1962.

        The rapid integration of large language models (LLMs) into information-seeking work-
flows has fundamentally transformed how users access and interact with content on the world
wide web. Search-augmented LLMs, which combine generative capabilities with real-time
web retrieval, promise to deliver more accurate, up-to-date, and comprehensive responses
than traditional chatbots limited to just their training data [13]. But questions have been
raised about source accuracy [25], intellectual property rights, scraping websites without
permission – so-called ‘access violations’ [4, 22], and what we term “ecosystem exploita-
tion”– the gap between relevant web content consumed by the LLM when answering a query
and those sources cited in the model’s output (its response).1
        This attribution gap has serious implications for the digital ecosystem on which AI’s
ongoing utility depends. Content creators, publishers, and knowledge producers rely on
appropriate attribution and licensing agreements when their information is used to answer
queries. When LLMs systematically consume relevant content without adequate citation or
remuneration, they undermine the incentive structures that support high-quality information
production and threaten the economic viability of content creation at scale [18].2 This
systematic lack of attribution of the content sources consumed by LLMs during web search
is a widely known issue [2, 10, 20].3 Yet major LLM vendors reveal little about how their
retrieval-augmented generation (RAG) pipelines choose and ingest web content, and how
they cite appropriate web sources [26].
Research questions: To what extent do search-augmented LLMs exploit the web — using
content without citing it? And what distinguishes today’s best and worst attribution practices?

Method and Data. Using an LMArena dataset of ≈ 14,000 real-world answers to around
7,000 multi-turn queries taken between March and April 2025, we analyze the “attribution
gap” exhibited by 11 LLM search-enabled models across three provider families: OpenAI
(GPT-4o), Perplexity (Sonar), and Google (Gemini). We define the attribution gap as the
number of relevant URLs visited by the LLM system when answering the query minus the
    1
      We use ‘consume’, ‘read’, and ‘search’ interchangeably for a relevant website visit logged by the LLM.
    2
      For previous research empirical research on attribution practices across commercial LLM systems see
Fayyazi et al. [6], Gao et al. [8], Huang et al. [12], Li et al. [16], Profound [19], Yue et al. [27].
    3
      As recently as June 2025 the BBC threatened Perplexity’s search system with legal action for using
its content during search [20]. Perplexity has set-up a revenue-sharing program with some publishers and
increased citation of sources in response to accusations against it [2].

                                                     1
number of URLs cited in the model’s output, providing a direct measure of ecosystem ex-
ploitation. To isolate this quantity, we remove all hallucinated citations (numbered citations
provided in-text that do not have a corresponding source in the search log) and all un-
grounded citations (URL citations provided that do not appear in the search logs but may
link to a valid site). Our statistical model is a negative binomial hurdle model with boot-
strapped confidence intervals. This allows us to quantify both when attribution gaps occur
and how severe they are, while accounting for differences in query type (e.g. ‘Data Science’,
‘Current Affairs’, etc.). In a second regression we leverage the dataset’s head-to-head design,
looking at differences between model citation behavior for the same query.

Key findings:

  1. Search-enabled LLM systems exploit by, surprisingly, not searching at all,
     relying instead on their pre-training data or simply not disclosing relevant search logs
     accurately. Despite the models being in search mode, 15.6% of LLM answers skipped
     web search entirely. This was highest for Google’s Gemini (34%), followed by OpenAI’s
     GPT-4o models (24%).

  2. LLM search systems exploit by providing no citations (zero attribution).
     30% of answers provided no citations. This is driven less by query topic and more by
     model-specific behaviors. Gemini provided no citations for a striking 92% of queries,
     undermining claims that its impact on third-party traffic will be negligible.

  3. Our zero-hurdle statistical model shows that, for a typical query, Google’s Gemini
     models and Perplexity’s Sonar models have sizable attribution gaps: at
     approximately 3 relevant websites visited but not cited. Perplexity exhibits much
     higher volume ecosystem exploitation, visiting ≈10 relevant websites per query, but
     with a similar overall attribution gap to Gemini.

  4. The full extent of ecosystem exploitation may be underestimated because
     models appear to selectively disclose which websites they visit, especially GPT-4o
     models. By design, GPT-4o models appear to have a near perfect correspondence
     between relevant websites drawn on and those cited, leading to a small attribution
     gap.

  5. Refining a search-LLM’s RAG pipeline can almost double the number of
     citations it provides for each extra webpage it consumes. In “head-to-head”
     model regressions, comparing citation differences between model pairs for identical

                                              2
        queries, we find that citation efficiency – the extra citations shown per additional web-
        site visited – ranges from 0.19 to 0.45. This indicates that retrieval design (reasoning
        modules, search context size, and geolocation), rather than technical limits, determines
        AI’s relationship with the world wide web’s ecosystem.

      The classical political economists defined exploitation as a category of production, whereby
an owner-producer appropriates the difference between the cost of an input and its realized
value contribution to output [28]. The classical economists focused exclusively on the labor
input [7, 11], but we can easily extend this framework to the data inputs consumed by LLM
models during inference when producing a relevant response (the output).
Policy implications. Advancing a healthy web ecosystem requires transparent search
telemetry (logs, traces, and metrics). Developers, enterprise buyers, and potentially reg-
ulators should insist that LLM APIs expose a standard trace of every retrieval step and
the sources ultimately cited. The tooling already exists to implement this: observabil-
ity stacks such as LangSmith, Langfuse, Phoenix, and the GenAI semantic-conventions in
OpenTelemetry can record an end-to-end search trace — query, retrieval, re-ranking, and
citation — so long as each web document is tagged with a stable source-ID (typically a URL
hash).4 Per-document relevance scores can travel in the same span [15]. If all providers adopt
common definitions (e.g. llm.retrieval.ids, llm.retrieval.scores), third-parties could
compare across models the exact ratio of “information consumed” to “information cited”;
and equitable business models could be built on top of this.
Limitations. Our study does not explicitly test citation accuracy or relevance, beyond re-
moving hallucinated and ungrounded citations [8]. Additionally, our study does not account
for access violations [4, 22] – whether the LLM had permission to visit specific websites, which
may be governed by licensing agreements. Despite these limitations, our study represents the
first systematic, cross-model audit of attribution behavior in commercial search-augmented
LLM systems, focusing specifically on their search tools. Our goal is to provide a structured
framework for assessing attribution in empirical LLM studies [5].
      Section 2 describes our data and variables; Section 3 details key empirical features of
our data; Section 4 outlines our two regression models; Section 5 presents our core findings
from the regressions; Section 6 discusses policy implications; and Section 7 concludes. Our
Appendix 8 contains more detailed model results.

  4
      See: https://opentelemetry.io/docs/specs/semconv/gen-ai/.

                                                 3
2         Data and Method
We conduct a large-scale empirical audit of attribution practices of commercial search-
augmented LLMs in real-world user interactions. Attribution refers to identifying the source
material or input features that contributed to a model’s generated output or decisions [16].
It emphasizes relevant content “consumed” (read and used) by the LLM when answering,
instead of all websites visited that may not be relevant and therefore not drawn upon. We
assume the search results provided in an LLM’s search log were already determined to be
relevant by the provider. Other forms of exploitation, especially ones involving unauthorized
access are not examined here [4, 18].

Dataset Overview. Our analysis uses LMArena’s search dataset, containing pairs of model
answers to the same user query across 11 major commercial LLMs. Our final sample size
(n) is 13,929 observations. We construct all variables from the raw logs rather than using
the variables provided by LMArena due to various errors and inconsistencies.5
        The initial dataset before filtering contains 14,000 conversations from 3,642 users, cov-
ering 7,000 queries each given to a pair of models between March (44%) and April (56%)
2025. Each query represents a potential multi-turn conversation, including the model’s final
response. Crucially, this dataset captures actual deployment behavior via application pro-
gramming interface (API) calls.

        Model Coverage. We analyze 11 commercial variants grouped by provider:

    • OpenAI : api-gpt-4o-mini-search, api-gpt-4o-search, api-gpt-4o-search-high, api-gpt-4o-
          search-high-loc

    • Perplexity: ppl-sonar-pro, ppl-sonar-reasoning, ppl-sonar, ppl-sonar-pro-high, ppl-sonar-
          reasoning-pro-high

    • Google: gemini-2.0-flash-grounding, gemini-2.5-pro-grounding

        The model configurations are detailed further in the LMArena documentation.6
    5
    See: https://blog.lmarena.ai/blog/2025/search-arena/.
    6
    “For Perplexity and OpenAI, this includes setting the ‘search context size’ parameter to medium, which
controls how much web content is retrieved and passed to the model. We also explore specific features by
changing the default settings: (1) For OpenAI, we test their geolocation feature in one model variant by
passing a country code extracted from the user’s IP address. (2) For Perplexity and OpenAI, we include
variants with ‘search context size’ set to high. ” Gemini model defaults to Google Search Tool enabled. See:
https://blog.lmarena.ai/blog/2025/search-arena/. Accessed: 16 June, 2025.

                                                     4
2.1      Key Variables and Measurement
We do not rely on LMArena’s citation variable construction, which we found didn’t ade-
quately distinguish between search logs and citations for our use case. We instead recon-
struct them from scratch using the model logs in their dataset.

      Ecosystem Exploitation (Attribution Gap). Our primary dependent variable mea-
sures the difference between unique relevant pages visited by the LLM during search and
unique pages actually cited to the user in the API response. This captures the extent to
which a model consumes relevant web content without providing appropriate attribution.
      Citations. We define citations as any in-text URL reference that is grounded in the
model’s search results log, including both explicit URLs and numbered references that link
to specific sources. We exclude “hallucinated citations” (numbered citations, such as [13] ,
that link to an empty source) and “ungrounded citations” (citation of URLs that exist but
are not in the search log). Unique URLs (websites) for citations or attribution are those
seen by the model that do not link to the same web page when stripped of parameters
(e.g., example.com/?tracking_id=23222 is turned into example.com). This amounts to
transforming URLs into their base URL and then checking for duplicates.
      Relevant Sites Visited (Consumed). We define relevant sites visited by the LLM
as those listed in their search log, regardless of whether they were cited in-text or not. We
treat every URL that appears in the search log as relevant, on the understanding that the
provider has already filtered out non-relevant visits. Note, however, that this log may itself
be incomplete: some vendors — OpenAI, in particular — seem to pre-trim their traces,
returning only a subset of the relevant pages the model actually visited.
      Conversation Classification. We categorize all conversations into 12 topic areas us-
ing o4-mini with high reasoning to enable analysis of topic-specific attribution patterns.
This classification covers areas from technical queries (software engineering, data science) to
consumer-oriented topics (shopping, health, finance). We provided the 12 categories to GPT,
drawing on an unsupervised visualization of clusters in the query data on Nomic Atlas.7
      Data Cleaning. After removing conversations with classification failures or misaligned
search traces, our final sample contains 13,929 observations, all successfully classified and
with clean attribution data.
      Pre-filtering of Logs. Most models appear to filter their logs for relevant websites
visited only – rather than all sites visited. But OpenAI appears to filter them more strictly.
Hallucinated citations (numbered citations provided in-text that do not exist in the search
  7
   See        Nomic       Atlas:              https://atlas.nomic.ai/data/srulyrosenblat/
ai-model-search-comparison-dataset/map/2da8af3f-c160-4008-928d-8df37c27b947#x7Nh.

                                              5
log) appear for Gemini and to a lesser extent Sonar.8 Moreover, in terms of citations provided
that do not appear in the search logs (ungrounded citations): 7% of citations by GPT-4o
models were not found in its search logs, indicating either an overly restrictive pre-filtering
of the search logs or simply the model citing from pre-trained knowledge.

3       Descriptive Patterns
Our data show stark differences in attribution practices across model families, highlighting
that design choices, rather than technological limitations, drive model behavior.

The Attribution Crisis. 15.6% of LLM responses involved no website visits despite be-
ing in search mode, yet 30% provided no citations whatsoever – a substantial gap between
content consumption and content recognition. This pattern varies dramatically by provider.
39% of responses show perfect attribution alignment (zero gap), while 61% exhibit some
degree of ecosystem exploitation. For Gemini, a “zero” gap still tends to signals exploitation
though, because the model usually answers without visiting any external site even when its
Google-Search tool is enabled (Table 1).
Provider-Specific Patterns. Table 1 illustrates three distinct patterns of exploitation:
(1) Not visiting relevant sites at all, according to the model’s logs, when answering a
question (exploitation through pre-training reliance) – 24% of GPT search answers and 34%
of Gemini models; (2) Not providing any citations at all – 25% of GPT-4o answers and
92% of Gemini answers; and (3) Having a large relative gap between sites visited and sites
cited – as in Perplexity’s Sonar.

                   Table 1. Attribution Statistics by Model Family

                                                GPT-4o       Gemini   Sonar
                       Median Gap                      0.0      4.0      5.0
                       Median Citations                2.0      0.0      5.0
                       Median Sites Visited            2.0      4.0     10.0
                       Zero Citations                1,309    2,198      663
                       Zero Site Visits              1,242      817      120
                       Sample Size (n)               5,272    2,394    6,263
Note: ‘Gap’ refers to the attribution gap = relevant websites visited (content consumed) minus unique
websites cited.
    8
    They are by definition zero for GPT-4o models since OpenAI’s models do not use numbers in square
brackets for its citations which is what we track for this metric.

                                                 6
    • GPT-4o – Limited disclosure of sites visited: On paper it shows almost perfect
      alignment between relevant pages searched according to its logs and pages cited. But
      this is likely an artifact of aggressive log-filtering. The model seems to disclose only
      those URLs it ultimately cites, omitting any additional relevant pages it read (con-
      sumed). Support for this view comes from its high share of ungrounded citations —
      links that appear in the answer but not in the trace — suggesting that many visits are
      simply withheld from the log.

    • Gemini – No citations provided: Systematic attribution failure with 92% zero-
      citation responses despite some relevant website searches.

    • Sonar – High-volume, low-credit: Extensive crawling (10 median sites) with large
      attribution gaps (5.0 median) despite providing more citations than Gemini or OpenAI.

Topic-Specific Vulnerabilities.         Attribution failures concentrate in economically and
legally sensitive domains, including:

    • Software engineering: 33% zero-citation rate (700 queries), especially for Gemini

    • Games/Creative writing: 40% zero-citation rate (494 queries)

    • Education: 43.6% zero-citation rate (228 queries)

    • Health information: For Mental & Physical Health and Relationships, systematic gaps
      for Gemini (94%) and GPT (26%)

4     Regression Models
4.1     Hurdle-Model Specification
The dependent variable Yi (i = 1, . . . , n) is the attribution gap: the number of relevant
websites a model visits but fails to cite, for query i, where i runs from 1 to n = 13, 929.
Because most answers are perfectly attributed (Yi = 0) while the rest show a skewed count
distribution, we use a hurdle model. It breaks up E[Attribution Gap] = P (Gap >
0) × E[Gap | Gap > 0] into two sequential components:

(a) Hurdle stage: What is the probability that the gap is exactly zero → P (Gap > 0)? This
    is a Bernoulli outcome with probability πi .

                                               7
(b) Count stage: If an attribution gap exists (Yi > 0), how large is the gap: E[Gap | Gap > 0]?
    We model positive counts with a zero-truncated negative binomial distribution, which has
    mean λi and over-dispersion parameter α.9

        Putting the two parts together gives the probability mass function:
                                              
                                              
                                              
                                              
                                               πi ,                                         y = 0,
                                              
                                              
                            Pr(Yi = y | xi ) = 
                                                                                    
                                                              nb  fi      y; λ , α                             (1)
                                              
                                              
                                               (1 − π i )               ,                 y ≥ 1,
                                                           1 − f 0; λ , α
                                              
                                                                      nb        i
                                              

 where:
                                                                                  
                                    Γ y + α−1                            − y+α−1
                      fnb y; λ, α =                    (αλ)y 1 + αλ                      ,        α > 0.       (2)
                                       Γ(α−1 ) y!
 fnb (y; λ, α) is the mean-parameterized negative binomial probability mass function,

 Linear predictors. Each of the two regression stages has its own regression equation with
 predictors, consisting of: model family, the query category or ‘classification’ (e.g. ‘Data
 Science’), the log of LLM output character count, and the number of unique search results.
 This leads to the following two equations:10

                                                                                                                    
 logit(πi ) = γ0 + γ ⊤                         ⊤
                     fam 1{model_familyi } + γ cls 1{classificationi } + γℓ log response_character_counti ,

                                                                                                               (3)

    log λi = β0 + β ⊤                         ⊤
                    fam 1{model_familyi } + β cls 1{classificationi }
                                                                                                          
               + βsr unique_search_results_counti + βℓ log response_character_counti
                                                                     ⊤
               + 1{model_familyi }⊗1{classificationi } β fam×cls
                                                                                            ⊤
               + 1{model_familyi }⊗unique_search_results_counti β fam×sr                                       (4)

        Equation 3 is the logit probability, where exp(γ fam ) represents the odds-ratios for produc-
 ing any attribution gap by model family, exp(γ cls ) represents the odds-ratios by classification
 topic, and exp(γℓ ) is the odds-ratio for answer length. The equation contains only main ef-
 fects (no interactions): the odds of any gap depend separately on model family, topic, and
    9
     If α → 0 the model would reduce to a Poisson hurdle.
   10
     Number of ‘turns’ had poor predictive power in our model, wrong sign in count component, despite some
 correlation to attribution gap for GPT models and especially for Perplexity models.

                                                          8
answer length.11
       Equation 4 is the negative binomial count component whereby exp(β fam ) represents the
multiplicative changes in the expected number of uncited website visits by model family,
given that a gap exists. exp(β cls ) represents the effects by classification topic, and exp(βsr )
is the multiplicative effect of additional search results. A value of 1.30 implies a 30% larger
gap, for example. Equation 4 adds interaction terms β fam×cls , so the effect of a model
family can differ by query topic once a gap exists, and β fam×sr , to account for the varying
impact of searching (number of URLs) on the attribution gap by model family.

4.2       Head-to-Head Model Comparison Regression
To isolate the number of URLs each LLM cites from one additional website search visit,
while controlling for question types, we run a second additional regression model. This
exploits the LMArena head-to-head design, whereby every question is answered by exactly
two model systems. This means that any unobservable query-specific factors driving citation
behavior cancel out. This design also ensures that β1m is not biased by systematically “easy”
or “hard” opponents. We collapse each model pair that answers the same query into a single
observation (focal model − opponent) and run a separate OLS regression for every focal
model m, where i now runs from 1 to n = 6, 951, and m contains 11 focal models.

                                                         X (m)             X (m)
               dim = β0m + β1m ∆sim + β2m ∆ℓim +              γk   Dik +       δj   Oij + εim ,          (6)
                                                          k                j

       In Equation 6, dim denotes the citation-gap advantage – the difference in unique
citations produced by the focal model compared to its ‘opponent’, citationsm − citationsopp .
The term ∆sim captures the search retrieval difference, defined as the gap in unique
URLs visited by the two systems in its logs, while ∆ℓim measures the length difference in
characters between their answers. The vector Dik comprises topic dummies controlling for
the classification of question i (reference category: “Current affairs & factual”), and Oij
contains dummies identifying which rival model the focal system faces (baseline = the first
alphabetic opponent).12
  11
     For example, exp(γℓ ) = 1.4 means a one-unit increase in log(response length) multiplies the odds of a
gap by 1.4.
  12
     Coefficient interpretation is as follows. The slope β1m measures citation efficiency: it is the expected
additional citations that model m produces per additional URL it opens, conditional on topic, verbosity,
and opponent. Thus β1m = 0.40 implies that ten extra retrievals yield roughly four extra citations. The
coefficient β2m captures the effect of answer length (characters) net of retrieval; a significant value would
                                                                                                  (m)
indicate that verbosity itself explains some of the citation edge. Topic dummies enter through γk ; positive
values mean model m out-cites its rival in domain k, whereas negative values signal a systematic shortfall.
                                              (m)
Opponent-specific effects are absorbed by δj , showing how the citation gap changes when m faces rival j

                                                     9
    Each model’s β1m is our key quantity of interest and summarizes model m’s retrieval-to-
citation efficiency or yield: the impact of a marginal website visit on citations.

5     Regression Findings
5.1     Attribution Gap Regression Model
The regression results, transformed into probabilities, show notable differences in attribution
reliability across AI model families (Table 2 and Figure 1).13 The ‘expected attribution gap’ is
the total prediction from our model: E[Attribution Gap] = P (Gap > 0) × E[Gap | Gap >
0]; whereas the first row (‘Probability of a Gap’) is only the first term of this equation,
P (Gap > 0).

             Table 2. Expected Total Attribution Gap by Model Family

                                                             GPT           Gemini           Sonar
          Probability of a Gap (%)                            10.5         70.3         99.3
          Expected Attribution Gap (Total)                    0.18         3.04         3.12
          95% Confidence Interval                     [0.15, 0.23] [2.80, 3.28] [2.99, 3.25]
          Standard Error (SE)                                 0.02         0.12         0.06
Note: Results from negative binomial hurdle model for Current Affairs & Factual Information queries with
median characteristics (5 search results, 2,089 characters, per query), with bootstrapped mean. Confidence
intervals from parametric bootstrap (n=1,000) for total expected attribution gap. Attribution gap is the
missing web page (URL) citations per search query relative to relevant websites consumed, measured as a
web page gap. This pattern holds consistently across all topic classifications (see Appendix, Table 5).

    The GPT-4o models appear to show less exploitative attribution behavior but this is
most likely due to them being more circumspect in their disclosures by not showing the full
extent of their logs.14 OpenAI’s models have only a 10.5% probability of having any citation
gaps and an expected 0.18 missing citations (relative to relevant websites consumed) per
query (Table 2). Sonar exhibits citation gaps in 99.3% of queries with 3.12 expected missing
instead of the baseline opponent. Finally, β0m gives the baseline citation advantage when the question falls
in the reference topic, the opponent is the baseline rival, and retrieval/length differences are zero.
   13
      The hurdle model produces raw odds-ratios that compare each model family to the reference category
(Gemini). However, for policy interpretation, we need actual probabilities and expected values. To obtain
these, we used the fitted model to make predictions for a standardized query: covering Current Affairs &
Factual Information topic classification with median characteristics (5 search results visited, 2,089 character
responses). The model’s ‘hurdle’ component estimates the probability of having any attribution gap (missing
citations & licensing), while the count component estimates the expected gap size when gaps occur. Multi-
plying these components gives us the unconditional expectation – the average number of missing citations
per query for each model family.
   14
      Using OpenAI search in the user interface (UI) shows far more website visits from limited testing.

                                                      10
citations per query in total. Gemini falls somewhere between these extremes with citation
gaps in 70.3% of queries and 3.04 expected missing citations in total per query.
       Sonar’s near-universal citation gap (99.3% of queries) makes it particularly concerning
for applications requiring source transparency. Gemini is arguably relying too heavily on
internal knowledge given that a large portion of its zero attribution gap is due to it having
zero (disclosed) website searches, at 34% of queries.

         Figure 1. Expected Attribution Gaps, Predicted (by Model Family)

                      4.0

                      3.5                            3.12
                                                                            3.04

                      3.0

                      2.5

            E [Gap]   2.0

                      1.5

                      1.0

                      0.5    0.19

                      0.0
                             GPT                    Sonar                  Gemini
                                                AI Model Family

Note: Predicted values for number of citations missing relative to web pages consumed. Based on
negative binomial hurdle model regression coefficients. Bars show the model’s expected citation
gap (websites visited in the logs minus websites cited in the output), estimated at the median
conversation length and median website visits, without interaction effects included. Showing 95%
confidence intervals calculated with the emmeans package in R.

       Lastly, in terms of other factors driving how large the gap is once it appears (the count
component), we can look at the incidence-rate ratio (IRR).15 Longer answers actually shrink
the gap size: When logged response character count doubles (from e.g., 100 to 200 charac-
  15
     In count-data models (Poisson, negative binomial, zero-inflated, hurdle, etc.) the regression is fitted on
a log scale. Exponentiating a coefficient converts it to an incidence-rate ratio (IRR). The IRR tells you the
multiplicative change in the expected count when the predictor increases by one unit, holding everything
else constant.

                                                      11
ters), the expected number of missing citations decreases by about 11% (IRR 0.89 or so).
Reading more web pages from search inflates the gap: every extra page the LLM system
reads raises the expected uncited count by 13% (IRR ≈ 1.13).

5.2       Head-to-Head Model Results: Citation efficiency
In this section, we focus on β1m coefficient from our head-to-head regressions (Equation 6).
This coefficient tells us how many more citations the focal model generates for each additional
search result compared to its opponent. A smaller coefficient signals poorer performance: the
focal model converts each extra relevant page it opens into fewer citations than its comparator
does. For example, if Sonar’s coefficient is 0.4, this means that when it undertakes five
additional relevant web page visits than GPT-4o on a question it is expected to have 5×0.4 =
2 more citations than GPT-4o. 264 coefficients are estimated in total, running a separate
regression for each of the 11 models (24 parameters estimated for each model).16
       We plot β1m in Figure 2 below (Appendix Table 6). Almost all coefficients from the
regression are positive and highly significant.17
       Figure 2 below shows that best-in-class variants (Sonar-reasoning-pro-high, Gemini-flash-
grounding, GPT-4o-search-high-loc) yield ∼ 0.43 citations per extra URL; whereas baseline
variants (ppl-sonar-pro-high) return only ∼ 0.19. This implies that the best model converts
every extra retrieved URL into ≈ 0.45 additional citations (compared to its competitor
models), whereas the weakest model variant converts that same extra URL into ≈ 0.19
citations. The span is therefore about 0.45 − 0.19 ≈ 0.26 citations per URL, showing that
RAG implementation choices can more than double the payoff from each additional page the
model visits. This illustrates just how wide the performance window is, and thus how much
room developers (or regulators) have to raise low performers up to the current best practice.
  16
      1 × Intercept; 11 × topic dummies (classifications), 1 × focal-search-diff (number of web pages), 10 ×
opponent-model dummies, 1 × focal-length-diff.
   17
      Among the 264 coefficients estimated, focal_search_diff is significant (and positive) for every model
– extra retrieval still translates into more citations, although the payoff varies. Answer length matters
(positive) for the GPT-mini, GPT-search, Sonar-pro, Sonar, and Sonar-reasoning families, but not for the
“high” search variants or Gemini models. One notable exception: ppl-sonar-reasoning-pro-high shows
a significant negative length effect (−1.35 × 10−4 , p = 6.75 × 10−3 ), suggesting longer answers actually
hurt citation performance for this model. Topic effects are sparse and model-specific. Mental & Physical
Health lowers citation edge for GPT-4o variants but raises it for basic Sonar-pro. Finance boosts citation
edge for Sonar-pro-high but suppresses it for Sonar-reasoning and Gemini-2.5. Opponent dummies are often
significant and large.

                                                    12
              Figure 2. Focal Model: Citation difference per extra URL visited

ppl−sonar−reasoning−pro−high                                                                                             0.45

           ppl−sonar−reasoning                                                                                       0.44

  gemini−2.0−flash−grounding                                                                                      0.43

 api−gpt−4o−search−high−loc                                                                                       0.43

     api−gpt−4o−search−high                                                                                0.39

                     ppl−sonar                                                                      0.34

   gemini−2.5−pro−grounding                                                                  0.31

            api−gpt−4o−search                                                   0.26

     api−gpt−4o−mini−search                                                   0.25

                ppl−sonar−pro                                     0.2

            ppl−sonar−pro−high                               0.19

                                 0.0         0.1              0.2               0.3                        0.4
                                                     ^
                                                     β1m (citations per extra URL)

                                                         Gemini         GPT          Sonar

  Note: Extra citations gained for each additional URL the focal model opens (differences between models).
  This holds match-up effects constant, isolating technology effects. Regression coefficient β1m shown, pre-
  dicting differences in citations for model pairs, for a given query. See equation above.

          More specifically, our results show that RAG implementation type (technology) is more
  important than model family (e.g., OpenAI vs. Gemini):

      • An ANOVA test shows that within-family variation (the variance) of search coefficients
            β1m is almost 8 times larger than between-family variation. This means that differences
            in model behavior is far greater within model families than between them.18

      • Within Sonar alone, upgrading to the reasoning tier more than doubles efficiency (from
            0.19-0.20 → 0.44-0.45), with Sonar-reasoning (0.44) vs Sonar-pro-high (0.19) = 0.25
     18
      We ran a one–way ANOVA on the eleven citation–efficiency coefficients (βb1m on focal_search_diff)
  grouped by provider family. The within–family mean square is nearly eight times the between–family mean
  square:
                                                                          0.0015
               MSwithin = 0.0116,      MSbetween = 0.0015,          F(2, 8) =    ≈ 0.13, p = 0.88.
                                                                          0.0116
    Thus, variability inside each provider family dominates the small differences between family means: im-
  plementation choices explain ∼ 8× more of the spread in citation efficiency than the family label itself.

                                                      13
      difference. For GPT models: GPT-4o-search-high-loc (0.42) vs GPT-4o-mini (0.25) =
      0.17 difference.

    • Location signals matter too. Adding a country code to GPT-4o raises search-citation
      coefficient efficiency by roughly 10 % (0.39 → 0.43), confirming that retrieval relevance
      translates directly into better attribution (though it is unclear why this is the case).
      Practically, this effect size is moderate since for a model getting 10 extra search results,
      location signals would generate ≈ 0.37 additional citations. But we know that local
      search operates differently, both in traditional search and increasingly with LLMs [21].

    Lastly, the regression results show that more basic models (GPT-mini, GPT-search, and
basic Sonar models) compensate for lower search efficiency through verbosity – they need
longer answers to achieve similar citation performance. Advanced (‘high’ variant and Gemini)
models achieve higher citation rates through superior search utilization, making verbosity
unnecessary to achieve improved citation rates.

6     Policy Implications
Without standardized telemetry — comprehensive logs and traces of what an LLM retrieves
and cites — no transparent and competitive market for licensing, revenue-sharing, or other
content-monetization schemes can easily emerge. Publishers need hard numbers on how often
their pages power an answer in order to automate royalty or revenue-share flows; regulators
need the same auditable data to enforce forthcoming disclosure rules in jurisdictions such as
the European Union (EU) and California. In short, richer telemetry is the prerequisite for
both commercial remuneration and public oversight.
    The technical pieces already exist for full disclosure of an LLM’s search and citation
trace; what remains is coordination. The key challenge is to persuade providers to adopt
a common telemetry standard — and to ensure buyers and regulators can incentivize its
provision.
    Modern observability frameworks — LangSmith, Langfuse, Phoenix, and the GenAI
semantic-conventions in OpenTelemetry — allow for recording an end-to-end search trace,
which can detail the search activities that an LLM RAG system undertakes when trying to
find the most relevant context for the user. One way to think of traces is as a collection of
structured logs with context, correlation, and hierarchy baked in. Each web page retrieval,
reranking, and generation step by the LLM can be logged as an OpenTelemetry span, pro-
vided every document is tagged with a stable Source ID, typically a hash of the original URL

                                               14
or file.19
       Because hashes are one-way fingerprints, they enable later verification without revealing
copyrighted text. The same span can carry the numerical relevance score (‘how relevant
was this webpage to the LLM’s answer’) produced by the vector store, BM25 index, or
cross-encoder, as long as that score is preserved in the trace [15, 23]. If each retrieved
document carries two stable fields — say llm.retrieval.ids (a hash or URL that uniquely
identifies the page) and llm.retrieval.scores (its relevance score or rank) — and those
fields are propagated from the retrieval step all the way to the final API response, then
anyone inspecting the trace can, in theory:
   1. Enumerate every page the model actually saw;
   2. Check which of those pages were later cited in the answer; and
   3. Compare the relevance scores of cited pages with those that were ignored.
       In short, the full provenance of “pages viewed” versus “pages credited” becomes au-
ditable.20
       OpenTelemetry-like open protocols can be a lightweight standard that enables compar-
ison and validation of LLM behavior across models. And adopting telemetry protocols
(standards) requires only incremental changes to today’s open-source stacks.21
       The real challenge, perhaps, lies in constructing the market and regulatory incentives
to advance widespread adoption and disclosure. Transparent traces unlock clear, quantifi-
able monetary benefits for providers. API buyers in legal, medical, and financial sectors
increasingly require provenance guarantees. This means that model developers that expose
richer evidence trails could, therefore, command premium pricing and benefit from greater
demand in these compliance-sensitive sectors. However, the model developers may be ret-
icent to undertake such additional disclosures without liability safeguards or more reliable
RAG pipelines.
       Yet our findings also point toward possible paths forward. A business model for LLM
search could create a mutually beneficial exchange of content for web traffic or direct pur-
chases. Commercial queries present a fairly distinctive pattern in our analysis. Shopping
and commercial-intent queries show attribution gaps 76% larger than other categories, yet
these domains offer opportunities for such mutually beneficial arrangements. Early web ad-
  19
     With a span representing a unit of work or operation and are the building blocks of traces. See:
https://opentelemetry.io/docs/concepts/signals/traces/.
  20
     https://opentelemetry.io/docs/specs/semconv/gen-ai/
  21
     In LangChain, a single line of code drops the hash and score into Document.metadata. LangSmith then
records them automatically in each trace span [15]. Langfuse performs the same mapping when it converts
LangChain calls into OpenTelemetry. Phoenix ingests any span that follows the GenAI conventions, meaning
dashboards that plot “high-score pages not cited” or “low-score pages that slipped through” can be deployed
without further engineering.

                                                    15
vertising models, where attribution facilitated click-through and conversion, provide relevant
precedents for sustainable approaches.

7       Conclusion
This study provides one of the first systematic empirical audits of attribution practices in
commercial search-augmented LLMs. When LLMs exploit content from platforms without
proper attribution, they undermine the economic incentives that sustain high-quality infor-
mation production. Returning to our opening quote by the late economist Joan Robinson
– on the notion that exploitation under capitalism involves the absence of commercial rela-
tions as well as its presence – we find similar twin forces at work in our analysis. Gemini
systematically excludes the world wide web’s content ecosystem when answering questions
as its form of exploitation, while Perplexity exploits through the opposite behavior, overly
zealous consumption of web content without commensurate attributions.
    We find a substantial “attribution gap” between relevant content consumed from websites
and attribution practices that threatens the sustainability of the digital content ecosystem.
Our analysis of ≈14,000 real-world interactions demonstrates that leading AI systems sys-
tematically consume web content without adequate attribution, with Gemini providing no
citations in 92% of its responses and Perplexity visiting approximately a dozen relevant
websites while crediting only a few.
    A negative binomial hurdle model shows that the average query answered by Gemini or
Sonar leaves about 3 relevant websites uncited, whereas GPT-4o’s tiny uncited gap is best
explained by its selective log disclosures rather than by better attribution. GPT-4o models
remain difficult to audit due to what appears to be stricter pre-filtering of its model search
logs.
    The dramatic variation in citation efficiency between models when answering the same
question – from 0.19 to 0.45 citations per additional web page visited – illustrate that attri-
bution gaps result from design choices, not simply technical limitations. The best-performing
systems show that transparent, comprehensive attribution is technically feasible today (even
if accurate citations and output remain a real ongoing issue).
    Closing the attribution gap is, therefore, less a technical hurdle than one of proper co-
ordination and market incentives. Standardizing two telemetry fields — document hashes
and relevance scores — would allow anyone to verify which information an LLM consumed
and how faithfully it credited that information. Observability tools already provide the
necessary plumbing. What remains is a collective decision by model providers to enable it
and by developers and buyers to reward those who do. Transparent search traces would

                                              16
strengthen incentives for high-quality content and give users a robust evidentiary basis for
trusting machine-generated answers.
       Our results demonstrate that transparency in the web sources consumed and cited by
LLMs when answering user queries is fundamentally an engineering choice.22

  22
     This aligns with emerging research on LLM citation evaluation frameworks [9] and attribution methods
in scientific literature [17, 24], which show that technical solutions are available but underutilized. Source-
aware training and fine-tuning have also been shown to improve citation behavior [14]. See also Asai et al.
[1] and Borgeaud et al. [3].

                                                      17
References
 [1] Akari Asai, Zeqiu Wu, Yizhong Wang, Avirup Sil, and Hannaneh Hajishirzi. Self-
    rag: Learning to retrieve, generate, and critique through self-reflection. arXiv preprint
    arXiv:2310.11511, 2023.

 [2] AutoGPT. Perplexity ai faces attribution controversy, 06 2024. URL https://autogpt.
    net/perplexity-ai-faces-attribution-controversy/.

 [3] Sebastian Borgeaud, Arthur Mensch, Jordan Hoffmann, Trevor Cai, Eliza Rutherford,
    Katie Millican, George Van Den Driessche, Jean-Baptiste Lespiau, Bogdan Damoc,
    Aidan Clark, et al. Improving language models by retrieving from trillions of tokens.
    Proceedings of the 39th International Conference on Machine Learning, pages 2206–
    2240, 2022.

 [4] Sarah Cool-Fergus. What happens when the news starts answering back? in conver-
    sation with miso.ai ceo, lucky gunasekara, 2025. URL https://www.twipemobile.com/
    what-happens-when-the-news-starts-answering-back-in-conversation-with-miso-ai-ceo-l
    Interview with Lucky Gunasekara, CEO of Miso.ai, from AI Frontrunners in News
    webinar series.

 [5] Oli Elliott and Pete Archer.      Representation of bbc news content by ai assis-
    tants. Research report, BBC, 02 2025. URL https://www.bbc.co.uk/aboutthebbc/
    documents/bbc-research-into-ai-assistants.pdf.

 [6] Reza Fayyazi, Michael Zuzak, and Shanchieh Jay Yang. Llm embedding-based attri-
    bution (lea): Quantifying source contributions to generative model’s response for vul-
    nerability analysis. arXiv preprint arXiv:2506.12100, 2025. URL https://arxiv.org/
    abs/2506.12100. cs.CR.

 [7] Ben Fine. Marx’s capital, 1989.

 [8] Tianyu Gao, Howard Yen, Jiatong Yu, and Danqi Chen. Enabling large language models
    to generate text with citations. arXiv preprint arXiv:2305.14627, 2023.

 [9] Tianyu Gao, Howard Yen, Jiatong Yu, and Danqi Chen. Enabling large language models
    to generate text with citations. arXiv preprint arXiv:2305.14627, 2023.

[10] Hacker News. Citations on the anthropic api, 2025. URL https://news.ycombinator.
    com/item?id=42807173. Discussion thread on Claude citation behavior.

                                            18
[11] Samuel Hollander. Classical Economics. University of Toronto Press, 1992.

[12] Baixiang Huang, Canyu Chen, and Kai Shu. Authorship attribution in the era of llms:
    Problems, methodologies, and challenges. ACM SIGKDD Explorations Newsletter, 26
    (2):21–43, 2025.

[13] Jie Huang and Kevin Chen-Chuan Chang. Citation: A key to building responsible and
    accountable large language models. arXiv preprint arXiv:2307.02185, 2023.

[14] Muhammad Khalifa, David Wadden, Emma Strubell, Honglak Lee, Lu Wang, Iz Belt-
    agy, and Hao Peng. Source-aware training enables knowledge attribution in language
    models. arXiv preprint arXiv:2404.01019, 2024.

[15] LangChain. How to get a rag application to add citations. https://python.langchain.
    com/docs/how_to/qa_citations/, 2025. Accessed 24 June 2025.

[16] Dongfang Li, Zetian Sun, Xinshuo Hu, Zhenyu Liu, Ziyang Chen, Baotian Hu, Aiguo
    Wu, and Min Zhang. A survey of large language models attribution. arXiv preprint
    arXiv:2311.03731, 2023.

[17] Ayat Najjar, Huthaifa I. Ashqar, et al. Leveraging explainable ai for llm text attribu-
    tion: Differentiating human-written and multiple llms-generated text. arXiv preprint
    arXiv:2501.03212, 01 2025. URL https://arxiv.org/abs/2501.03212.

[18] Tim O’Reilly. How to fix “ai’s original sin”, 06 2024. URL https://www.oreilly.com/
    radar/how-to-fix-ais-original-sin/. O’Reilly Radar.

[19] Profound.    Ai platform citation patterns: How chatgpt, google ai overviews, and
    perplexity source information, 2025.         URL https://www.tryprofound.com/blog/
    ai-platform-citation-patterns. Research analysis from August 2024 to June 2025.

[20] Reuters.           Bbc    threatens   legal     action   against   ai   startup    per-
    plexity      over    content     scraping,      ft    reports.           Reuters,    06
    2025.                URL       https://www.reuters.com/business/media-telecom/
    bbc-threatens-legal-action-against-ai-start-up-perplexity-over-content-scraping-202
    Accessed 24 June 2025.

[21] Damian Rollison. How does chatgpt conduct local searches?, 05 2025. URL https:
    //searchengineland.com/how-does-chatgpt-conduct-local-searches-454894.
    Search Engine Land.

                                             19
[22] Sruly Rosenblat, Tim O’Reilly, and Ilan Strauss. Beyond public access in llm pre-
    training data: Non-public book content in openai’s models. Technical Report SSRC AI
    WP 2025-04, Social Science Research Council, 04 2025. URL https://ssrc-static.
    s3.us-east-1.amazonaws.com/OpenAI-Training-Violations-OReillyBooks_
    Sruly-OReilly-Strauss_SSRC_04012025.pdf.

[23] Michael      Ryaboy.                 Cross–encoders,      colbert,   and     llm–based
    re–rankers:           A   practical     guide.          https://medium.com/@aimichael/
    cross-encoders-colbert-and-llm-based-re-rankers-a-practical-guide-a23570d88548,
    2025. Accessed 24 June 2025.

[24] Yash Saxena, Deepa Tilwani, Ali Mohammadi, Edward Raff, Amit Sheth, Srinivasan
    Parthasarathy, and Manas Gaur. Attribution in scientific literature: New benchmark
    and methods. arXiv e-prints, pages arXiv–2405, 2024.

[25] Jordan-Marie Smith, Christopher Intagliata, and Mary Louise Kelly.                 The
    trump administration’s report on kids’ health cites made-up scientific stud-
    ies,    05    2025.        URL        https://www.npr.org/2025/05/30/nx-s1-5417962/
    the-trump-administrations-report-on-kids-health-cites-made-up-scientific-studies.

[26] Patrick Stox. Websites with more organic search traffic get mentioned more in ai search.
    https://ahrefs.com/blog/websites-with-more-traffic-have-more-mentions/,
    2025. Accessed 24 June 2025.

[27] Xiang Yue, Boshi Wang, Ziru Chen, Kai Zhang, Yu Su, and Huan Sun. Automatic
    evaluation of attribution by large language models. arXiv preprint arXiv:2305.06311,
    2023.

[28] Matt Zwolinski, Benjamin Ferguson, and Alan Wertheimer. Exploitation. In Edward N.
    Zalta and Uri Nodelman, editors, The Stanford Encyclopedia of Philosophy. Metaphysics
    Research Lab, Stanford University, Winter 2022 edition, 2022. Accessed: August 5, 2025.

                                                20
8       Appendix
8.1      Full Hurdle-Model Specification and Diagnostics
The regression is estimated with R’s pscl::hurdle() function, which maximizes a likelihood
that combines a binary gate for perfect attribution and a zero-truncated negative binomial
(NB) for positive gaps. Writing πi ≡ Pr(Yi = 0), the log-likelihood is

                  X                  X                                                   h                   i
ℓ(γ, β, α) =             log πi +              log(1 − πi ) + log fNB (yi | λi , α) − log 1 − fNB (0 | λi , α)     ,
                i: yi =0            i: yi >0
                                                                                                             (A1)
     with γ = (γ0 , γ1 , γ2 , γ3 )⊤ for the gate and β = (β0 , β1 , β2 , β3 , β4 )⊤ for the count compo-
nent. The NB kernel is parameterised by its mean λi and over-dispersion α > 0:

                                                                       
                           Γ y + α−1           y              − y+α−1
    fNB (y | λi , α) =                    αλi          1 + αλi                ,   Var(Yi | Yi ≥ 1) = λi + αλ2i .
                           Γ(α−1 ) y!
                                                                                                             (A2)
     Likelihood ratio tests can assess whether the count process is better modeled as Poisson
or negative binomial (null hypothesis H0 : α = 0), and whether inclusion of the interaction
term improves model fit. A negative binomial outperforms. Model fits (information criteria)
are superior with interaction terms and shows domains where the effect of a model family
changes the expected gap magnitude.
     With interaction terms the zero-inflated model performs better in a Vuong test than
a hurdle model. Our hurdle model though aligns better with theoretical understanding of
citation process. We believe interpretability advantages outweigh improvements though.
BFGS optimisation converged in 54 iterations, giving θb = 5.69.

                                                            21
        Figure 3. Attribution Gap Histogram vs Negative Binomial (Red)
                                                                                  size=1.94
                        0.100
                                                                                   mu=7.48

                        0.075

          Probability
                        0.050

                        0.025

                        0.000

                                0           50                      100
                                                 Attribution Gap
Note: Attribution gap (relevant sites visited in logs minus websites cited by in-text URLS) shows a negative
binomial distribution (red over-plot).

8.2     Detailed Model Results
Figure 4 shows topic specific gaps, as predicted by our model. ‘Shopping & Commercial
Intent’, perhaps surprisingly, shows the largest gap across models – being 0.2 lower for the
Sonar model family. This could reflect a greater selectivity in which results are shown by
the model given potential greater commercial incentives to ‘get it right’, or to abide by pre-
existing licensing agreements. But it also could simply highlight the absence of a worked out
business model in this area, despite large opportunities to monetize website traffic in this
area of LLM search.

                                                      22
Figure 4. Expected Citation Gaps by Regression Model (Query Classification
                                                     and Model Family)
                                                                               GPT
            Shopping & Commercial Intent                                                                                                0.3
                                     Sports                                                                    0.3
                                   Lifestyle                                                          0.2
  Mental & Physical Health & Relationships                                                            0.2
                     Finance & Economics                                                            0.2
                             Data Science                                                     0.2
                                     History                                            0.2
      Current Affairs & Factual Information                                           0.2
 Computer Science & Software Engineering                                           0.2
       Games, Fantasy & Creative Writing                                     0.2
                                 Education                             0.1
                                      Other                           0.1
                                               0.0              0.1                    0.2                            0.3

                                                                              Sonar
                                 Education                                                                                             3.9
                                     Sports                                                                                           3.8
                                     History                                                                                        3.8
       Games, Fantasy & Creative Writing                                                                                           3.7
 Computer Science & Software Engineering                                                                                           3.7
            Shopping & Commercial Intent                                                                                          3.7
                             Data Science                                                                                     3.5
                     Finance & Economics                                                                                      3.5
  Mental & Physical Health & Relationships                                                                                 3.4
                                   Lifestyle                                                                              3.4
                                      Other                                                                              3.3
      Current Affairs & Factual Information                                                                        3.1
                                               0            1                      2                           3                         4

                                                                             Gemini
            Shopping & Commercial Intent                                                                                                3.5
                                     Sports                                                                                       3.3
                     Finance & Economics                                                                                          3.3
                             Data Science                                                                                         3.3
                                     History                                                                                    3.3
  Mental & Physical Health & Relationships                                                                                     3.2
      Current Affairs & Factual Information                                                                              3.0
                                   Lifestyle                                                                            3.0
 Computer Science & Software Engineering                                                                             2.9
       Games, Fantasy & Creative Writing                                                                 2.5
                                 Education                                                            2.4
                                      Other                                                   2.1
                                               0                1                       2                                3

                                                                    Expected Attribution Gap

Note: Bars show the expected citation gap (relevant websites visited in the logs minus websites
cited in the LLM’s output) for each query classification. Classification labels are ordered by gap
magnitude within each panel. See Table 2 above for method.

                                                            23
                Table 3. Count Model Coefficients (No Interactions)

 Term                                                   Estimate Std. Error z value p-value
 (Intercept)                                                2.163     0.078   27.66   0.000
 modelfamilyGPT                                            -1.099     0.156   -7.05   0.000
 modelfamilySonar                                           0.207     0.054    3.81   0.000
 classificationCurrent Affairs & Factual Information       -0.021     0.053   -0.39   0.695
 classificationData Science                                 0.057     0.064    0.89   0.371
 classificationEducation                                   -0.115     0.091   -1.26   0.209
 classificationFinance & Economics                          0.034     0.068    0.50   0.615
 classificationGames, Fantasy & Creative Writing           -0.053     0.074   -0.72   0.473
 classificationHistory                                     -0.008     0.087   -0.09   0.929
 classificationLifestyle                                   -0.028     0.064   -0.43   0.665
 classificationMental & Physical Health & Relationships     0.050     0.077    0.66   0.512
 classificationOther                                       -0.093     0.065   -1.43   0.154
 classificationShopping & Commercial Intent                 0.021     0.061    0.35   0.727
 classificationSports                                      -0.033     0.091   -0.37   0.712
 search results count                                       0.125     0.003   39.74   0.000
 log(response length)                                      -0.171     0.008 -20.24    0.000
 log(θ)                                                     1.740     0.031   55.39   0.000
Note: Gemini as baseline model. Showing coefficients (main effects) from the count component of the
negative binomial hurdle model.

                Table 4. Hurdle Model Coefficients (No Interactions)

 Term                                                   Estimate Std. Error z value p-value
 (Intercept)                                               -0.729     0.207   -3.52   0.000
 modelfamilyGPT                                            -3.140     0.069 -45.66    0.000
 modelfamilySonar                                           1.601     0.061   26.28   0.000
 classificationCurrent Affairs & Factual Information        0.195     0.096    2.03   0.043
 classificationData Science                                 0.268     0.117    2.29   0.022
 classificationEducation                                   -0.245     0.144   -1.69   0.090
 classificationFinance & Economics                          0.341     0.121    2.83   0.005
 classificationGames, Fantasy & Creative Writing           -0.265     0.108   -2.45   0.014
 classificationHistory                                      0.398     0.169    2.36   0.018
 classificationLifestyle                                    0.177     0.111    1.59   0.113
 classificationMental & Physical Health & Relationships     0.189     0.144    1.31   0.190
 classificationOther                                       -0.529     0.098   -5.39   0.000
 classificationShopping & Commercial Intent                 0.567     0.115    4.93   0.000
 classificationSports                                       0.577     0.151    3.81   0.000
 log(response length)                                       0.165     0.024    6.92   0.000
Note: Gemini as baseline model. Showing coefficients (main effects) from the hurdle component of the
negative binomial hurdle model.

                                                24
 Table 5. Expected Citation Gaps by Model Family and Topic Classification

                                                       GPT-4o                  Gemini                Sonar
 Classification                                 Est.       95% CI      Est.       95% CI      Est.        95% CI
 Computer Science & Software Engineering        0.17   (0.14–0.22)     2.89    (2.63–3.14)    3.72   (3.55–3.89)
 Current Affairs & Factual Information          0.18   (0.15–0.23)     3.03    (2.78–3.29)    3.12   (3.00–3.26)
 Data Science                                   0.21   (0.16–0.27)     3.33    (2.97–3.73)    3.52   (3.34–3.74)
 Education                                      0.12   (0.08–0.19)     2.37    (1.97–2.78)    3.88   (3.57–4.19)
 Finance & Economics                            0.23   (0.18–0.29)     3.34    (2.95–3.73)    3.52   (3.34–3.72)
 Games, Fantasy & Creative Writing              0.15   (0.11–0.21)     2.48    (2.18–2.82)    3.73   (3.54–3.92)
 History                                        0.19   (0.13–0.30)     3.27    (2.77–3.80)    3.76   (3.45–4.10)
 Lifestyle                                      0.23   (0.17–0.31)     3.00    (2.69–3.34)    3.36   (3.19–3.54)
 Mental & Physical Health & Relationships       0.23   (0.17–0.32)     3.23    (2.76–3.73)    3.39   (3.17–3.63)
 Other                                          0.11   (0.09–0.15)     2.11    (1.88–2.39)    3.29   (3.13–3.47)
 Shopping & Commercial Intent                   0.35   (0.27–0.45)     3.51    (3.16–3.85)    3.66   (3.48–3.86)
 Sports                                         0.27   (0.19–0.38)     3.35    (2.85–3.95)    3.82   (3.59–4.07)

Note: Total expected attribution gap from negative binomial hurdle model. Predictions are at the median
query (5 search results and 2,089 characters). Confidence intervals from parametric bootstrap (n=1,000).
Est. = Expected citation gaps per query.

8.3     Head-to-Head Regressions: Table of results

    Table 6. Incremental citations per extra URL opened, by model variant

  Model variant                                        Family          n      β̂1m      SE            p
  ppl-sonar-reasoning-pro-high                         Sonar          848     0.447   0.015   1.4e-138
  ppl-sonar-reasoning                                  Sonar         1635     0.445   0.012   4.3e-215
  gemini-2.0-flash-grounding                           Gemini        1189     0.427   0.013   6.0e-172
  api-gpt-4o-search-high-loc                           GPT           1222     0.426   0.010   6.1e-240
  api-gpt-4o-search-high                               GPT           1695     0.389   0.010   1.3e-224
  ppl-sonar                                            Sonar         1200     0.339   0.012   1.8e-128
  gemini-2.5-pro-grounding                             Gemini        1200     0.312   0.011   4.8e-130
  api-gpt-4o-search                                    GPT           1188     0.264   0.012    2.5e-89
  api-gpt-4o-mini-search                               GPT           1158     0.251   0.012    1.1e-80
  ppl-sonar-pro                                        Sonar         1208     0.200   0.014    9.5e-46
  ppl-sonar-pro-high                                   Sonar         1359     0.191   0.012    9.9e-51
Note: n = pair-wise query comparisons involving the focal model.           β̂1m is the coefficient on
focal_search_diff, interpreted as the expected number of additional citations produced for each extra
URL the focal model opens.

                                                  25
