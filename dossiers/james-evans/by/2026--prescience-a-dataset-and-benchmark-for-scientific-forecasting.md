---
title: "PreScience: A Dataset and Benchmark for Scientific Forecasting"
person: james-evans
section: by
type: journal-article
year: 2026
date: 2026-02-24
venue: "Open MIND"
authors: "Ajith, Anirudh, Singh, Amanpreet, DeYoung, Jay, Kunievsky, Nadav, Kozlowski, Austin C., Tafjord, Oyvind, Evans, James, Weld, Daniel S., Hope, Tom, Downey, Doug"
source_url: https://doi.org/10.48550/arxiv.2602.20459
openalex_id: https://openalex.org/W7131395659
retrieved: 2026-08-13
content: full-text
notes: "OpenAlex duplicates merged: W7131395659 W7131475734; full text via the OpenAlex Content API (content.openalex.org); text taken from duplicate OpenAlex record W7131475734"
---

# PreScience: A Dataset and Benchmark for Scientific Forecasting

## Full text

PreScience: A Benchmark for Forecasting Scientific Contributions

Anirudh Ajith 1 * Amanpreet Singh 1 * Jay DeYoung 1 * Nadav Kunievsky 2 Austin C. Kozlowski 2
Oyvind Tafjord 1 James Evans 2 Daniel S Weld 1 Tom Hope 1 3 * Doug Downey 1 4 *

arXiv:2602.20459v1 [cs.AI] 24 Feb 2026

Abstract

who draw on existing literature to formulate new ideas, and
whose insights, once published, fold back into the corpus,
shaping the ongoing evolution of science. Forecasting this
arc—predicting which research directions will emerge, who
will pursue them, what contributions they will produce,
and what attention those contributions will receive—holds
promise for improving scientific decision-making. Such
forecasts could help researchers form effective teams and
pursue promising lines of inquiry while enabling institutions and policymakers to allocate resources and anticipate
emerging scientific and social impacts. From the perspective
of automated scientific discovery, forecasting the structure
and content of the scientific record provides a grounded
benchmark for systems that aim to generate and validate
research artifacts, where as argued in previous work existing
evaluations are often limited to more narrow or synthetic
tasks (Bragg et al., 2025; Cappello et al., 2025). At the same
time, it poses a challenging AI setting in which models
must integrate unstructured text with structured relational
signals (e.g., citation and collaboration graphs) under strong
temporal and distributional shift in a non-i.i.d. regime (Vu
et al., 2011; Margatina et al., 2023). Unlike closed-world
tasks, this problem is open-ended and temporally evolving,
requiring models to condition on a large and continually
expanding body of prior work.

Can AI systems trained on the scientific record
up to a fixed point in time forecast the scientific
advances that follow? Such a capability could
help researchers identify collaborators and impactful research directions, and anticipate which
problems and methods will become central next.
We introduce PreScience—a scientific forecasting
benchmark that decomposes the research process
into four interdependent generative tasks: collaborator prediction, prior work selection, contribution
generation, and impact prediction. PreScience is
a carefully curated dataset of 98K recent AIrelated research papers, featuring disambiguated
author identities, temporally aligned scholarly
metadata, and a structured graph of companion author publication histories and citations spanning
502K total papers. We develop baselines and evaluations for each task, including LACERScore, a
novel LLM-based measure of contribution similarity that outperforms previous metrics and approximates inter-annotator agreement. We find
substantial headroom remains in each task—e.g.
in contribution generation, frontier LLMs achieve
only moderate similarity to the ground-truth (GPT5, averages 5.6 on a 1-10 scale). When composed
into a 12-month end-to-end simulation of scientific production, the resulting synthetic corpus is
systematically less diverse and less novel than
human-authored research from the same period.
õ Dataset

Previous work has examined such science forecasting problems in isolation: including future collaborations (LibenNowell & Kleinberg, 2003b; Sun et al., 2011; Kanakaris
et al., 2021), novel idea combinations (Sternlicht & Hope,
2025; Frohnert et al., 2024), follow-up work (Wang et al.,
2023), and publication impact (Chen et al., 2025a). However, these constitute interdependent stages in the life-cycle
of a single scientific advance, and studying them separately
limits joint modeling and holistic analysis. Further, using
LLMs for uncontaminated analyses or simulation dictates
that the constituent papers post-date their training cutoffs.

§ Code

1. Introduction
The arc of scientific progress can be viewed as a sequence
of advances: each undertaken by a team of researchers

We introduce PreScience, a living and holistic benchmark for modeling and forecasting scientific contributions.
PreScience formulates the forecasting challenge as four
interdependent generative tasks: 1) collaborator prediction – forecasting the set of co-authors on a future paper,
2) prior work selection – identifying the key results from
existing literature that will inform their work, 3) contribu-

* Core contributor 1 Allen Institute for Artificial Intelligence,
Seattle, WA, USA 2 Knowledge Lab, University of Chicago,
Chicago, IL, USA 3 School of Computer Science and Engineering, Hebrew University, Jerusalem, Israel 4 Northwestern University, Evanston, IL, USA. Correspondence to: Anirudh Ajith
<anirudha@allenai.org>.
Preprint. February 25, 2026.

1

PreScience: A Benchmark for Forecasting Scientific Contributions

Prior Work

Collaborators

R

C

Scientific
Advance A

Impact

I
Figure 1. Our generative decomposition of a scientific advance. A team of collaborators (C) identifies a set of foundational prior work
(R) that they build upon to produce a scientific advance (A) which goes on to achieve impact (I). All of these steps are conditioned on
historical scientific advances H<t , and the resulting advance is incorporated back into the history to inform future advances.

2. A Generative Decomposition of Science

tion generation – generating a paper’s title and abstract,
and 4) impact prediction – estimating the paper’s near-term
citation impact. In PreScience, each subtask can be studied
in isolation or jointly—and as we show in our experiments,
can be composed to simulate new scientific contributions by
iteratively generating papers, incorporating them back into
the literature state, and analyzing their downstream effects.

We represent each scientific contribution by four components: a research team C, a set of influential prior work
R, a scientific advance A, and its downstream impact I.
Rather than treating scientific forecasting as a single-step
prediction problem, PreScience decomposes the modeling
of each new paper into four prediction tasks, one for each
core component. We do not intend this graph to be a highfidelity causal theory of scientific discovery, instead we use
it as a scaffold for tractable modeling and evaluation.

We summarize our main contributions as follows:
1. We present PreScience: the first large-scale, evergreen
benchmark for scientific forecasting that covers team
formation, prior work selection, contribution generation, and impact. We release a unified dataset of 98,000
AI-related arXiv papers (October 2023–October 2025)
with rich metadata, author histories, and citation links
to 502,000 total papers, along with code for evaluation
and data construction to support updates.

Our decomposition forms a directed graphical model (Figure 1). At time (day) t, H<t is the publication history of
all papers published prior to t. Each publication at t is
added to the history H<t+1 and informs future advances.
Formally, our model uses the following factorization of the
joint distribution of a scientific contribution:

2. We develop task-appropriate evaluation protocols, including LACERScore, a new LLM-based metric for
comparing generated and ground-truth contribution
descriptions that better reflects conceptual similarity
than standard text- or embedding-based measures. We
further develop multiple baselines ranging from taskspecific approaches to frontier models across our four
tasks, benchmarking current performance and remaining headroom. We find that current methods underexploit the information present in PreScience.
3. By composing our task-level models into end-to-end
simulations, we analyze how synthetic scientific trajectories differ from the real-world. We observe systematic degradations in diversity and novelty relative
to human-authored research from the same period.

P (C, R, A, I|H<t ) = P (C|H<t )P (R|C, H<t )
P (A|C, R, H<t )P (I|C, R, A, H<t )

(1)

Our benchmark involves estimating each of the conditional
distributions on the right-hand side. Each paper p provides
a supervised instance for the variables (C, R, A, I) under
this decomposition. C is the set of previously-published
authors of p, R is a set of “key references” that inform
p, A is represented by p’s title and abstract, and I is p’s
citation count in the year following publication. Rather than
evaluating the distributions directly, PreScience casts each
conditional as a standalone prediction task with interpretable
task-specific metrics. We detail each predictive task below.
2

PreScience: A Benchmark for Forecasting Scientific Contributions

2.3. Contribution Generation

Scope and simplifying assumptions This decomposition
makes several simplifying assumptions in order to be operationalizable. It implies a temporal unidirectional ordering
C → R → A → I even though these components may coevolve (e.g., developing a contribution can reshape which
references are salient, and exposure to prior work can influence collaborator choice). It also focuses on only part of the
observable record of scientific production (papers, authors,
citations, etc.), abstracting away institutions, venues, funding, and other factors. Enriching H<t with these factors
and relaxing our assumptions are directions for future work.
Further limitations are discussed in section 6.

In contribution generation we aim to synthesize a plausible scientific advance—its problem framing, approach, and
results—given the authors C and key references R of a
target paper. As scientific abstracts provide concise representations of a paper’s core contribution, we frame this task
as generating the paper’s title and abstract. For a paper p
published at time t, given C, R, and H<t , the task is to
generate a candidate title and abstract for p.
The objective of this task is to capture the underlying scientific contribution rather than reproduce its precise phrasing, requiring evaluation methods that assess conceptual
substance rather than surface-level textual overlap. In our
experiments, existing automatic textual similarity metrics
(e.g. BERTScore (Zhang et al., 2019), ASPIRE-OT (Mysore
et al., 2022), retrieval-based mean reciprocal rank, etc.)
exhibited limited dynamic range: substantially different
generated title-abstract pairs received similar scores. Moreover, the level of dissimilarity required to produce a score
near the lower extreme of the scale was often ill-defined
and seemingly arbitrary. We therefore developed two custom LLM-based metrics to compute similarity scores between title-abstract pairs: FacetScore (Appendix G.1) and
LACERScore. We ultimately opted for the latter since it
correlated better with human judgements (Figure 2).

2.1. Collaborator Prediction
We formulate collaborator prediction as a link prediction
problem (Liben-Nowell & Kleinberg, 2003a): given a “seed”
author of paper p and the prior literature state H<t , the task
is to predict the remaining authors of p in any order.1 We
start with a seed author for ease of evaluation, as predicting
an author set from scratch is underdetermined. We further
restrict all authors in our dataset to those with a non-empty
publication history, leaving the modeling of first-time authors to future work.
We evaluate a model’s ranking of potential collaborators
from most to least likely using standard ranking metrics:
normalized Discounted Cumulative Gain (nDCG) (Järvelin
& Kekäläinen, 2002) and R-precision (NIST TREC, 2006).

Defining LACERScore. We define LACERScore (Lattice of Automatically Constructed Exemplars for Reference
Score), an LLM-as-judge metric calibrated to a 1-10 semantic alignment scale using automatically constructed demonstrations. Defining a score of 1 to represent the similarity
between a key reference4 (representing topically related, but
clearly distinct prior work) and the target abstract, and a
score of 10 to represent semantic equivalence, we prompt
(Appendix G.2.2) an LLM to generate intermediate titleabstract pairs for scores 2 through 9 by incrementally modifying their semantic aspects to interpolate between the two
extremes. Formally, given a real paper’s title-abstract p, a
paraphrased version p̂, and the selected key reference r, we
generate a sequence

2.2. Prior Work Selection
We formulate this task as link prediction as well: given the
authors C of a target paper p, the model predicts the set
of p’s “key references”: a subset of prior work especially
influential to it, such that the authors are likely to build
upon this prior work for creating the new advance. To
our knowledge, this is the first large-scale benchmark that
frames literature choice as a prospective, team-conditioned
forecasting task.
As in collaborator prediction, we evaluate this task as a
ranking problem and report nDCG and R-precision against
the ground truth set of key references, determined by
the “highly influential citations”2 feature from Semantic
Scholar (Valenzuela-Escarcega et al., 2015). This provides
a scalable and consistent source of influential prior work.3

m(p2 |r)

m(p3 |p2 )

m(p9 |p8 )

r −−−−−→ p2 −−−−−−→ . . . p8 −−−−−−→ p9 → p̂,
where m(·|·) denotes an LLM’s incremental modification.

1

We assemble 5 such interpolations to serve as
few-shot demonstrations in LACERScore’s scoring
prompt (Appendix G.2.1). This approach ensures that
LACERScore evaluations enjoy an intuitive and welldefined dynamic range well-suited for this task without
relying on expensive human annotation. We show examples

Different seed selections (first, last, random, or the author
with maximum h-index) result in similar qualitative conclusions
and relative orderings across methods (Table 6: Appendix B.1).
2
We use Semantic Scholar’s production classifier. This yields
an average of 3.1 key references out of 45 total.
3
We find that alternative definitions of key references or using
the full reference list yield similar relative model rankings at a
substantially higher computational cost (Table 7: Appendix C.1).

4
Specifically, the key reference with median n-gram overlap
relative to the target abstract.

3

PreScience: A Benchmark for Forecasting Scientific Contributions
Table 1. Dataset Statistics. Average and median statistics are
computed over Target papers.

Train

Test Train ∪ Test

Target Papers
44990 52836
All Papers
373716 464942
Unique Authors
106913 129020
Avg. Authors
5.00
5.28
Avg. Author Hist.
22.5
27.8
Med. Author Hist.
7
9
Avg. Words
187.5 186.8
Avg. Key Refs
3.13
3.04
Med. Key Refs
3
2
Avg. Citations @ 12m
5.53
5.77

97826
501866
182727
5.15
25.5
8
187.1
3.08
3
5.57

cs.CV, cs.IR, and cs.NE. These constitute the target
papers in our benchmark. We include a set of companion papers consisting of key references of target papers,
prior publications of target authors, and key references of
those prior publications. Together, these form the historical
corpus H<t used to condition all tasks. The corpus can
be processed to construct task-specific representations (e.g.
document embeddings, citation and collaboration subgraphs,
author summaries, etc.) and perform controlled comparisons
between alternative representations of scientific history and
their impact on downstream prediction. We partition the target papers into train (October 2023-2024) and test (October
2024-2025). Summary statistics and distributions appear in
Table 1 and in Figure 5: Appendix A.1.

Figure 2. LACERScore approaches human-level agreement with
human similarity judgments, outperforming other metrics.

of its evaluations in Appendix G.5.
Validating LACERScore. We validate LACERScore using 250 human similarity rankings from 5 expert annotators
across 10 targets and 10 candidate generations (sourced
from four strong LLMs) per target. Annotators ranked candidates by conceptual similarity to the ground-truth abstract,
allowing ties. Correlating LACERScore with these rankings
using Kendall’s τb (Kendall, 1938) reveals that it approaches
human IAA5 , outperforming existing metrics (Figure 2).
More details can be found in Appendix G.3.

Each paper is accompanied by structured metadata including unique Semantic Scholar and arXiv identifiers (can be
used to retrieve full paper text), arXiv categories, and its
publication date. Target papers also include fields listing
their authors, key references, and cumulative citation counts
computed at a monthly cadence from the publication date.
Some companion papers include corresponding authorship
and reference metadata (Table 5: Appendix A.2).

2.4. Impact Estimation
We frame the impact estimation task as a regression problem
that predicts the number of citations a paper will accumulate in the first 12 months after publication. Each instance
provides the authors C, key references R, title and abstract
A, along with H<t . The prediction target is the cumulative
citation count at time t + 12 months, where t denotes the
paper’s publication date. For this regression task, we evaluate predictions in terms of mean absolute error, R2 , and
Pearson and Spearman correlations.

Ensuring dataset quality We take several steps to ensure that PreScience supports reliable modeling and evaluation. We source author identities and bibliographic metadata
from Semantic Scholar (Wade, 2022), and disambiguate author profiles using the S2AND pipeline (Subramanian et al.,
2021). To ensure that prior-work selection reflects meaningful literature choice rather than classification noise, we
restrict target papers to those having 1-10 key references, excluding instances with zero or unusually large key reference
sets. Finally, all author- and reference-level metadata (e.g.,
publication counts, citation counts, and h-indices) are temporally aligned to each paper’s publication date to prevent
leakage of future information into task inputs.

3. Dataset
The PreScience dataset is built from research papers posted
to arXiv6 between October 2023 and October 2025 in seven
AI-related categories: cs.CL, cs.LG, cs.AI, cs.ML,
5
Human–human Kendall τb = 0.53 reflects the non-trivial
subjectivity of these judgements, justifying the development of a
specialized similarity metric.
6
info.arxiv.org/help/bulk_data/index.html

4

PreScience: A Benchmark for Forecasting Scientific Contributions
Table 2. Performance comparison on collaborator prediction and
prior work selection (nDCG@1000 / R-Prec).
Collab

become less familiar to the seed author, with none of the
evaluated baselines able to predict first-time collaboration
pairs. This suggests that even our embedding-based methods are only able to recover repeat-collaboration structure
and not anticipate new relationships. The results of our
embedding-based approaches suggest that a more sophisticated treatment of the relational structure is necessary to
reliably model the formation of new research teams.

Prior Work

Method (Embed)

nDCG R-Prec nDCG R-Prec

Frequency

0.41

0.28

0.11

0.06

Rank Fusion (GTR)
Rank Fusion (Specter2)
Rank Fusion (GRIT)

0.15
0.11
0.17

0.06
0.05
0.08

0.03
0.02
0.02

0.01
0.01
0.01

Emb. Fusion (GTR)
Emb. Fusion (Specter2)
Emb. Fusion (GRIT)

0.24
0.19
0.28

0.16
0.11
0.18

0.05
0.07
0.11

0.02
0.03
0.05

Hier. Clustering (GTR)
Hier. Clustering (Specter2)
Hier. Clustering (GRIT)

0.25
0.25
0.25

0.15
0.14
0.15

0.06
0.07
0.06

0.02
0.02
0.02

Emb. Fusion Refs (GRIT)

–

–

0.06

0.02

Emb. Fusion Proj. (GRIT)

0.24

0.14

0.13

0.05

4.2. Prior Work Selection
For prior work selection, we evaluate similar strategies as for
collaborator prediction. Given a paper p written by collaborators C, Frequency ranks candidate references in H<t by
how often members of C have cited them previously. Rank
Fusion retrieves papers using embeddings of references previously cited by each author in C and aggregates retrieval
ranks. We evaluate two Embedding Fusion variants that
differ in how authors are represented: Embedding Fusion
(Papers) uses the centroid of each author’s own previously
authored papers, while Embedding Fusion (Refs) embeds
them as the centroid of their previously cited references. We
also evaluated a Projected version of this baseline that learns
a mapping of both authors (mean) and papers to the same
space over frozen embeddings before ranking. To model
author heterogeneity, we also evaluate a Hierarchical Clus√
tering baseline that represents each author by m = ⌊ n⌋
centroids derived from recent publications and ranks candidate references by the mean of their maximum similarity to
each author’s centroids in the author set.

4. Experiments
4.1. Collaborator Prediction
We evaluate five baseline methods for collaborator prediction: a co-authorship frequency heuristic; two embeddingbased fusion baselines; and two variants that (i) explicitly
represent authors as multi-interest profiles via clustering and
(ii) learn a task-specific embedding space via linear projection. Our Frequency baseline predicts collaborators for a
paper p with seed author c1 by ranking candidate authors
in H<t by their historical co-authorship frequency with c1 .
Rank Fusion represents c1 as the centroid of embeddings of
their n = 10 most recent papers, retrieves the top-k nearest
papers in H<t to this centroid, and ranks authors by the
summed ranks of their retrieved papers. Embedding Fusion
computes analogous centroid representations for all authors
in H<t and ranks candidates by cosine similarity to c1 . To
capture authors’ multiple interests, Hierarchical
Clustering
√
represents each author using m = ⌊ n⌋ centroids over
their recent papers and scores a candidate by the maximum
centroid-to-centroid cosine similarity to the seed author.
Finally, Projection optimizes the Multi-Instance NCE objective (Miech et al., 2019) to learn a linear mapping over
mean-pooled frozen paper embeddings, and performs ranking in the projected space. The embeddings are generated
with GTR (Ni et al., 2022), Specter2 (Singh et al., 2023),
and GRIT (Muennighoff et al., 2025).

Results Overall performance remains low (best nDCG
≈ 0.13), indicating that forecasting which prior work a team
will cite is difficult even with access to author histories. Figure 3b shows that the embedding-based methods achieve
low hit rates across all familiarity buckets and degrade further for less precedented references. Although Frequency
dominates in high-familiarity regimes, Embedding Fusion
(Papers) + Projected and Hierarchical Clustering exhibit
some ability to surface completely novel references suggesting that modeling author-level structure can recover weak
signals beyond direct citation history.
4.3. Contribution Generation
We evaluate large language models on contribution generation by conditioning on the titles and abstracts of the key
references R for a paper p and prompting (Appendix D.3)
models to generate a title and abstract for a new paper that
cites these references. We evaluate frontier models from
OpenAI and Anthropic alongside LoRA-finetuned (Hu et al.,
2022) 7–8B-scale open models (LLaMA 3.1 8B (Grattafiori
et al., 2024) and OLMo 3 7B (Olmo et al., 2025)), which

Results Frequency substantially outperforms all the
embedding-based approaches (e.g., 0.41 nDCG vs. 0.28 for
the strongest embedding variant) indicating that collaboration structure is difficult to infer from textual evidence alone
in the absence of explicit network, institutional, or graphstructured signals commonly used in prior work. Figure 3a
shows that performance degrades sharply as collaborators
5

PreScience: A Benchmark for Forecasting Scientific Contributions

(a) Collaborator prediction hit rate, i.e. the fraction of top-R
predicted authors that are among the R ground truth authors, as
the number of prior collaborations between ground truth author and
seed author varies. All baselines exhibit near-zero performance
when predicting first-time collaborators.

(b) Prior work prediction hit rate vs how frequently a paper’s
authors have cited the work previously. Methods struggle to predict
novel references, and Frequency dominates for more-cited papers.

Figure 3. Prediction performance as familiarity increases. (a) Collaborator prediction. (b) Prior-work prediction.

serve as compute-efficient7 baselines for scientific text generation. As points of reference, we also evaluate a gold
paraphrase of the target abstract, a random key reference,
and a random paper from the same primary arXiv category.
We report results with GPT-5 (gpt-5-2025-08-07) as
the LACERScore judge.

7-8B models outperform the same-topic baseline, but
remain well below frontier models, indicating that small
models can propose plausible continuations of existing
work but struggle to match real scientific contributions.
Even the strongest models achieve only moderate scores,
suggesting that identifying broadly reasonable directions is
substantially easier than reproducing the distinctive novelty
and substance of ground-truth advances. Adding richer
context, such as author information, may improve results.

Table 3. Evaluation results for contribution description. Asterisks
indicate that model cutoffs postdate the start of the test period.
Baseline

LACERScore

ROUGE-L

BERTScore

P

R

P

R

Primary Topic
Key Reference

1.27
4.31

0.13
0.16

0.12
0.16

0.14
0.19

0.13
0.18

LLaMA 3.1 8B (FT)
OLMo 3 7B (FT)

3.49
3.35

0.18
0.17

0.16
0.15

0.19
0.19

0.15
0.13

GPT 4o
GPT 4.1
GPT o3
GPT 5
GPT 5.1
GPT 5.2*
Claude Sonnet 4.5*
Claude Opus 4.5*

4.71
5.08
5.49
5.64
5.37
5.60
5.03
5.04

0.17
0.16
0.12
0.11
0.15
0.13
0.14
0.13

0.16
0.16
0.16
0.16
0.16
0.16
0.18
0.14

0.25
0.23
0.15
0.14
0.21
0.17
0.21
0.19

0.23
0.23
0.22
0.21
0.23
0.22
0.24
0.19

Gold Paraphrase

10.00

0.61

0.56

0.71

0.70

We perform robustness checks and find that systemic shift in
LACERScore scores before versus after model knowledge
cutoff dates are small, if present (Table 8:Appendix D.1),
and that relative model rankings remain stable across
LACERScore LLM-Judge choices (Table 9: Appendix G.4).
4.4. Impact Prediction
We evaluate citation forecasting baselines that draw on three
complementary sets of features: Target Text, Context Text,
and Bibliometrics. Target Text consists of the title and abstract of the target paper. Context Text includes the titles and
abstracts of the paper’s key references and the authors’ prior
publications. Bibliometrics comprises reference citation
counts and author-level statistics (h-index, total citations,
and publication counts) measured at the time of publication.
We train XGBoost regressors to predict the 12-month logtransformed citation count of target papers using different
combinations of these information sources (Table 4). For
text-based models, we represent Target and Context Text using embeddings from GTR, Specter2, or GRIT. To account
for the heavy-tailed distribution of citation counts, we report
performance in both the log space and raw counts.

Results Gold paraphrases achieve near-maximum
LACERScore scores, validating the upper bound of the
metric, while randomly selected key references and
same-topic papers cluster near the lower end. Fine-tuned
7

In our experiments, these models fail to adhere to the required
response format in ∼ 5% of test instances. We discard these and
report results averaged over the successes.

6

PreScience: A Benchmark for Forecasting Scientific Contributions
Table 4. Impact prediction results. Models use Target Text, Context Text, and Bibliometrics. Metrics are reported in both raw and log
citation space to account for heavy-tailed outcomes. SHAP (Lundberg & Lee, 2017) analyses for bibliometric features appear in Figure 9b:
Appendix E.1.

Baseline

MAE

MAE (log)

Pearson

Pearson (log)

Spearman

Target Text (GTR)
Target Text (Specter2)
Target Text (GRIT)

4.83
4.78
4.67

0.74
0.73
0.71

0.18
0.20
0.29

0.40
0.45
0.49

0.38
0.42
0.46

Bibliometrics

4.79

0.74

0.36

0.42

0.37

Target + Context
Target + Context + Bibliometrics

4.58
4.52

0.69
0.68

0.28
0.31

0.54
0.56

0.50
0.51

Algorithm 1 Corpus Generation

Results Among Target Text baselines, GRIT embeddings
yield the strongest performance. Incorporating Context Text
provides additional improvement as per all tabulated metrics.
Bibliometrics on their own are moderately predictive, but
offer limited marginal gains when combined with textual features. Prediction error remains substantial even when using
all three feature sets. We find substantial heteroscedasticity
(Figure 9a: Appendix E.1) in model predictions caused by
heavy-tailed nature of citation outcomes.8

Require: H<t0 , rollout horizon [t0 , tf )
Ensure: H<tf
1: PN , P|C| , P|R| , pnew ← E STIMATE D IST(H<t0 )
2: for t = t0 to tf − 1 do
3:
N ∼ P N , St ← ∅
4:
for i = 1 to N do
5:
|C| ∼ P|C| , |R| ∼ P|R|
6:
C ← S AMPLE R ESEARCH T EAM(|C|, pnew , H<t )
7:
R ← S ELECT P RIORW ORK(C, |R|, H<t )
8:
(τ, α) ← G ENERATE T ITLE A BSTRACT(C, R, H<t )
9:
St ← St ∪ {PAPER(τ, α, C, R, t)}
10:
end for
11:
H<t+1 ← H<t ∪ St
12: end for
13: return H<tf

4.5. Corpus Generation
We study corpus-level forecasting by composing our tasklevel models for the Collaborator Prediction, Prior Work
Selection and Contribution Generation tasks into a single
pipeline that simulates the daily production of scientific papers over a fixed horizon. Starting from an initial9 literature
state H<t0 , the simulator iteratively samples a set of new
papers each day, folds them back into the literature, and uses
the updated state to condition subsequent generations. At
each simulated day t, we first sample the number of papers
that day from an empirical multinomial distribution Pdaily
estimated on the training period. For each paper, we sample
a team size, predict a set of collaborators, select a set of key
references, and prompt a language model to generate a title
and abstract conditioned on the predicted references. The
resulting papers are then added to H<t+1 and indexed for
use in the next step of the rollout. We provide a description
of the above procedure in Algorithm 1.

Evaluation protocol We measure the diversity and novelty of synthesized papers using LACERScore. For each
month, we sample n = 100 of the generated papers, retrieve
their k = 10 nearest neighbors in GRIT embedding space
from a retrieval pool of paper embeddings. We set this pool
to be the set of papers synthesized within the same month as
the query paper for diversity measurements, and to be H<t
(where t represents the publication date of the target paper)
for novelty measurements. We report mean LACERScore
computed over the resulting n × k pairs. To ensure reliable
comparison, we subsample natural (real-world) retrieval
pools to match the size of the synthetic pools.10 We repeat
the full simulation six times and report mean trends with
95% confidence intervals across runs.

For this experiment, we choose baselines for each task that
are high-performing, uncontaminated, relatively inexpensive, and capable of returning new collaborating authors or
prior work (i.e. not Frequency). Specifically, we use GRIT +
Embedding Fusion for collaborator and reference prediction,
and GPT-5 for contribution generation.

Results Synthetic corpora are consistently less diverse
and trend towards lower novelty than natural papers from
the same time period (Figure 4). When novelty is measured
against the evolving literature state H<t , synthetic papers
exhibit a gradual decline (Figure 4b), indicating that new
generations become increasingly similar to what has already

8

A negative binomial regression model (designed for skewed
distributions) underperformed XGBoost in our experiments.
9
We use t0 = October 1st, 2024 to ensure the simulation period
coincides with the PreScience corpus test period.

10

Since we calibrate Pdaily using year-old data, the number of
papers in the synthetic retrieval pools slightly underestimates the
corresponding ground truth counts.

7

PreScience: A Benchmark for Forecasting Scientific Contributions

(a) Diversity (measured within each month)

(b) Novelty (measured against H<t )

(c) Novelty (measured against H<t0 )

Figure 4. Simulated (synthetic) papers (a) are less diverse and (b) trend towards being less novel compared to ground truth (natural) papers
that correspond to the same time period. When novelty is measured relative to the fixed pre-simulation corpus (c) this trend disappears.

5. Related Work

been produced within the simulation. However, when novelty is measured relative to the fixed pre-simulation corpus
H<t0 , this declining trend largely disappears (Figure 4c).
This suggests that the generated papers remain comparably
distant from the historical corpus, but because the diversity
of generated papers is relatively constrained, newly generated synthetic papers become more similar to the prior
synthetic outputs as the latter corpus increases in size. Synthetic corpora are consistently less diverse than their natural
counterparts at every simulated month in our rollouts (Figure 4a). This observation is consistent with a tendency to
reuse and recombine a limited set of directions, as opposed
to matching the breadth of exploration observed in realworld research. Interestingly, we find that the sets of authors
and prior work surfaced in our rollouts are more diverse than
their real-world counterparts (Appendix F.1), implying that
the observed disparity in diversity and novelty is due to the
large language model we use for contribution description.

5.1. Emulating the Scientific Research Workflow
Other approaches have previously sought to automatically
generate and evaluate ideas. Many require a seed research
question, and model the scientific process in terms of
ideation/hypothesis generation, experimentation, evaluation,
paper writing, and peer review (Cappello et al., 2025; Jansen
et al., 2024). Some include a human-in-the-loop (Jansen
et al., 2025), while others are completely automated (Lu
et al., 2024; Majumder et al., 2025).
However, a narrow focus on technical processes ignores the
collaborative aspect of science — the interchange of ideas
among researchers, the knowledge of relevant prior work in
their area of expertise, and how these ideas can be built upon
and combined to yield impactful research. Recent work
has tried to simulate this aspect with multi-agent systems
where agents have specialized roles and responsibilities with
access to relevant literature and can interact with each other
in a virtual lab-like setup (Su et al., 2024; Swanson et al.,
2024; Chen et al., 2025b; Yu et al., 2024). Even though these
simulate research interactions, the agents are synthetically
generated, with evaluation only for the final generation. In
contrast, Prescience uses real data and evaluates forecasting
across the scientific workflow rather than focusing solely on
ideation quality.

Discussion Accurately simulating scientific production
is inherently difficult, as real-world research is shaped not
only by the mechanisms we model but also by factors such
as funding, institutions, conferences, and external events.
Consistent with this, our simulated corpora fail to capture
the substantial seasonal variation in publication volume observed across subfields (Figure 11: Appendix F.2). Furthermore, individual statistics can be misleading when examined
in isolation: a system may appear to match some aspects
of scientific dynamics while diverging on others. We therefore interpret these results as reflecting both the limitations
of current approaches and the broader difficulty of modeling science as a complex, path-dependent process. A more
detailed discussion appears in Appendix F.2.

5.2. Evaluation Subtasks in PreScience
Collaborator prediction This task has been well-studied,
with most efforts using graph-based modeling approaches
(Kanakaris et al., 2021; Xi et al., 2021; Tuninetti et al., 2021;
Ebrahimi et al., 2021; Ho et al., 2019; Li et al., 2024). Some
methods explore alternative representations, such as modeling authors conditioned on a research topic (Chuan et al.,
2018; Xi et al., 2021; Cheng et al., 2023), or the temporal nature of their publication histories (O’Madadhain et al., 2005;
Munasinghe & Ichise, 2012; Koopmann et al., 2021). Some
8

PreScience: A Benchmark for Forecasting Scientific Contributions

Proxies for influence and impact We define key references with “highly influential citations” from Semantic
Scholar, and impact as citations accrued within a 12-month
window. These choices provide scalable and practical benchmarking targets, but favor influence manifested through formal citation practices and shorter time horizons.. Contributions such as negative results, conceptual or methodological
advances, may receive slower recognition, not captured by
citation counts, and this is not reflected in our benchmark.

works have further explored transformer-based approaches
(Koopmann et al., 2021). See Kong et al. (2019); Zhang et al.
(2023) for surveys on scholarly recommendation systems,
including author link prediction.
Prior work selection In our setting, for a given set of authors we forecast the literature they will build upon for
creating a new advance. To our knowledge, this task formulation is novel and not previously explored. In other, loosely
related lines of work on scientific ideation, it is common to
retrieve inspirations in the form of past papers (Wang et al.,
2023; Chen et al., 2025a; Luu et al., 2020; Radensky et al.,
2024; Sternlicht & Hope, 2025); however, the objective in
these papers is focused on surfacing inspirations for the
purpose of ideation, not forecasting the choice of prior work
conditioned on the collaborating authors and their expertise.

Domain and dataset scope We study recent AI papers on
arXiv, a field characterized by rapid preprinting, numerous
authors, industry involvement, and skewed citation patterns.
Hence, our findings may not generalize to slower-moving
fields, different authorship norms, or non-preprint venues.

Contribution generation The closest analogy to our contribution generation stage in current literature is scientific
hypothesis generation or ideation. Swanson (1986) treated
ideas as grounded in the interactions between different areas
of the scientific literature. Many modern approaches build
on this insight (Wang et al., 2023; Radensky et al., 2024; Lu
et al., 2024; Wang et al., 2024; Baek et al., 2025), including
recent benchmarks and multi-agent systems for research
ideation (Guo et al., 2025; Su et al., 2025), grounding insights to core research papers, sometimes with a literature
graph (e.g., of ideas and methods (Wang et al., 2023)).

Representation of scientific history Although
PreScience provides rich metadata, models must compress
this information into task-specific representations. These
representations encode assumptions about aspects of past
that are predictive of future advances. Benchmark result
interpretations should therefore consider the representations
and modeling choices used.

7. Conclusion
We present PreScience, a large-scale scientific forecasting
benchmark with four tasks representing the scientific workflow. We introduce a new evaluation metric for contribution
generation that agrees with human judgment better than
standard metrics. Our evaluation with various baselines indicates significant headroom in each task and our end-to-end
simulation experiments further show how today’s large language models fail to match the diversity and novelty of real
scientific research. We hope that the benchmark spurs the
development of stronger forecasting models. More broadly,
we envision PreScience as a workbench for training and optimizing systems to anticipate science—an objective where
supervision is naturally available at meaningful scale and
where success may require deep understanding of scientific
content. We speculate that optimizing models or representations for this forecasting task could, in turn, deepen their
grasp of scientific concepts, methods, and reasoning.

Impact prediction As impact and breakthrough prediction
is intrinsic to the academic process, the area has been well
studied. Prior works have used varied measures for impact
ranging from citation accumulation (Uddin et al., 2013; Gu
& Krenn, 2024), to novelty (Shi & Evans, 2023; Zhang &
Evans, 2025), to research grant success (Cole et al., 1981;
Boyack et al., 2018; Győrffy et al., 2020). PreScience situates impact prediction within a broader causal framework.
Unlike approaches that predict impact from metadata alone,
our benchmark conditions it on the full generative context:
the research team, their prior work, and the contribution
itself. Our finding that author and reference features provide
substantial predictive power aligns with the “cumulative
advantage” literature (Merton, 1968; Wang et al., 2013b),
while the residual variance points to other potentially helpful
signals that are unexplored.

In future work, we would like to enrich the dataset with
institution and funding information and more diverse domains. Another interesting potential addition to the dataset
could be multimodal information, such as tables and figures from past work, which may help enhance forecasting
performance. While PreScience assumed a specific causal
framework, our curated data could also be used to explore
different causal framings of the scientific process. This
raises interesting questions about how to compare and evaluate different causal frameworks, and how to design rigorous

6. Limitations and Scope
Modeling scientific processes PreScience decomposes a
scientific advance into four generative tasks. This factorization is an operational choice rather than a complete causal
theory of scientific discovery. In practice, these components may co-evolve, and real-world scientific trajectories
are shaped by additional factors like institutional incentives,
funding availability, venue selection, and social dynamics.
9

PreScience: A Benchmark for Forecasting Scientific Contributions

metrics that measure forecasting performance across the
entire arc of science.

classification. In Proceedings of the 48th International
ACM SIGIR Conference on Research and Development in
Information Retrieval, SIGIR ’25, pp. 2977–2981. ACM,
July 2025. doi: 10.1145/3726302.3730213. URL http:
//dx.doi.org/10.1145/3726302.3730213.

Impact Statement
Our hope is that PreScience spurs the development of
stronger scientific forecasting models. Stronger abilities
to predict along PreScience’s four tasks could help scientists when choosing collaborators, identifying promising
foundational prior work, or choosing among competing
research aims in order to maximize downstream impact.
Second, the benchmark could serve as a useful diagnostic.
Systematic failures clustered around particular types of research, career stages, or institutional contexts might reveal a
lack of critical signals, or an increase in fundamental unpredictability under those cases. For example, low accuracy on
collaborator prediction might reflect a lack of critical signals
regarding team formation, such as institutional proximity
(Duede et al., 2024). Such analyses could transform the
prediction benchmark into a tool for generating explanatory
hypotheses about how science works.

Arnaout, H., Sternlicht, N., Hope, T., and Gurevych, I.
In-depth research impact summarization through finegrained temporal citation analysis, 2025. URL https:
//arxiv.org/abs/2505.14838.
Baccini, A., Barabesi, L., and De Nicolao, G. On the agreement between bibliometrics and peer review: Evidence
from the italian research assessment exercises. PLOS
ONE, 15(11):e0242520, 2020.
Baek, J., Jauhar, S. K., Cucerzan, S., and Hwang, S. J. ResearchAgent: Iterative research idea generation over scientific literature with large language models. In Chiruzzo,
L., Ritter, A., and Wang, L. (eds.), Proceedings of the
2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics:
Human Language Technologies (Volume 1: Long Papers), pp. 6709–6738, Albuquerque, New Mexico, April
2025. Association for Computational Linguistics. ISBN
979-8-89176-189-6. URL https://aclanthology.
org/2025.naacl-long.342/.

Further, prospective research evaluation and science policy are longstanding concerns in the science of science.
Funding agencies and institutions routinely attempt such
assessments through peer review, yet meta-analyses reveal
troubling inconsistencies (Pier et al., 2018; Baccini et al.,
2020). Citation-based metrics offer an alternative but come
with well-documented limitations (Redman, 2023), such
as their slow evaluations and conflation of visibility with
quality (Wang et al., 2013a). Machine learning approaches
to impact prediction have shown greater promise (Weis &
Jacobson, 2021; Thelwall et al., 2023), and PreScience adds
a new resource to aid their development.

Boyack, K. W., Smith, C., and Klavans, R.
Toward predicting research proposal success. Scientometrics, 114:449–461, 2018. URL https://api.
semanticscholar.org/CorpusID:46804654.
Bragg, J., D’Arcy, M., Balepur, N., Bareket, D., Dalvi,
B., Feldman, S., Haddad, D., Hwang, J. D., Jansen, P.,
Kishore, V., Majumder, B. P., Naik, A., Rahamimov,
S., Richardson, K., Singh, A., Surana, H., Tiktinsky,
A., Vasu, R., Wiener, G., Anastasiades, C., Candra, S.,
Dunkelberger, J., Emery, D., Evans, R., Hamada, M.,
Huff, R., Kinney, R., Latzke, M., Lochner, J., LozanoAguilera, R., Nguyen, C., Rao, S., Tanaka, A., Vlahos,
B., Clark, P., Downey, D., Goldberg, Y., Sabharwal, A.,
and Weld, D. S. Astabench: Rigorous benchmarking
of ai agents with a scientific research suite, 2025. URL
https://arxiv.org/abs/2510.21652.

A potential danger of large scale simulations of science is
their mis-application. While there is a broad need among
policymakers for assistance in resource allocation, no simulation can fully replicate the nuance and decisions required
to produce large scale scientific advance. Inappropriate application of such systems may lead to truly novel research
directions being dropped, or higher-risk directions ignored
in favor of safer median outcomes.

Acknowledgements

Cappello, F., Madireddy, S., Underwood, R., Getty, N., Chia,
N., Ramachandra, N., Nguyen, J., Keceli, M., Mallick,
T., Li, Z., Ngom, M. C. N., Zhang, C., Yanguas-Gil, A.,
Antoniuk, E. R., Kailkhura, B., Tian, M., Du, Y., Ting,
Y.-S., Wells, A., Nicolae, B., Maurya, A., Rafique, M. M.,
Huerta, E. A., Li, B., Foster, I., and Stevens, R. Eaira:
Establishing a methodology for evaluating ai models as
scientific research assistants. ArXiv, abs/2502.20309,
2025. URL https://api.semanticscholar.
org/CorpusID:276647576.

This work was supported in part by NSF Grant 2404109.
We would also like to thank the Semantic Scholar team,
UChicago APTO group, Sewon Min, and other members of
Ai2 for their feedback and support.

References
Alexander, D. and de Vries, A. P. In a few words: Comparing weak supervision and llms for short query intent
10

PreScience: A Benchmark for Forecasting Scientific Contributions

Chen, J., Zhang, K., Li, D., Feng, Y., Zhang, Y.,
and Deng, B. Structuring scientific innovation: A
framework for modeling and discovering impactful
knowledge combinations.
ArXiv, abs/2503.18865,
2025a. URL https://api.semanticscholar.
org/CorpusID:277313413.
Chen, N., Tong, Y., Wu, J., Duong, M. D., Wang,
Q., Zou, Q., Hooi, B., and He, B.
Beyond brainstorming: What drives high-quality scientific ideas? lessons from multi-agent collaboration,
2025b. URL https://api.semanticscholar.
org/CorpusID:280540858.
Cheng, X., Zhang, Y., Joshi, H., Kejriwal, M., and
Calyam, P.
Knowledge graph-based embedding
for connecting scholars in academic social networks.
2023 IEEE 10th International Conference on Data
Science and Advanced Analytics (DSAA), pp. 1–10,
2023. URL https://api.semanticscholar.
org/CorpusID:265054862.
Chuan, P. M., Son, L. H., Ali, M., Khang, T. D., Huong,
L. T., and Dey, N. Link prediction in co-authorship
networks based on hybrid content similarity metric.
Appl. Intell., 48(8):2470–2486, 2018. doi: 10.1007/
S10489-017-1086-X. URL https://doi.org/10.
1007/s10489-017-1086-x.
Cole, S., Cole, J. R., and Simon, G. A. Chance and
consensus in peer review. Science, 214 4523:881–
6, 1981. URL https://api.semanticscholar.
org/CorpusID:11183533.
Duede, E., Teplitskiy, M., Lakhani, K., and Evans, J. Being together in place as a catalyst for scientific advance.
Research Policy, 53(2):104911, 2024.
Ebrahimi, F., Asemi, A., Nezarat, A., and Ko, A.
Developing a mathematical model of the co-author
recommender system using graph mining techniques
and big data applications. Journal of Big Data, 8,
2021. URL https://api.semanticscholar.
org/CorpusID:232133644.
Feng, N., Sui, Y., Hou, S., Cresswell, J. C., and Wu, G. Response quality assessment for retrieval-augmented generation via conditional conformal factuality. Proceedings of the 48th International ACM SIGIR Conference
on Research and Development in Information Retrieval,
2025. URL https://api.semanticscholar.
org/CorpusID:280011519.
Frohnert, F., Gu, X., Krenn, M., and van Nieuwenburg, E. P. L. Discovering emergent connections in
quantum physics research via dynamic word embeddings. Machine Learning: Science and Technology,
11

6, 2024. URL https://api.semanticscholar.
org/CorpusID:273963065.
Fu, J., Zhang, X., Pashami, S., Rahimian, F., and Holst,
A. Diffpad: Denoising diffusion-based adversarial patch
decontamination, 2024. URL https://arxiv.org/
abs/2410.24006.
Grattafiori, A., Dubey, A., Jauhri, A., Pandey, A., Kadian,
A., Al-Dahle, A., Letman, A., Mathur, A., Schelten, A.,
Vaughan, A., Yang, A., Fan, A., Goyal, A., Hartshorn,
A., Yang, A., Mitra, A., Sravankumar, A., Korenev,
A., Hinsvark, A., Rao, A., Zhang, A., Rodriguez, A.,
Gregerson, A., Spataru, A., Roziere, B., Biron, B., Tang,
B., Chern, B., Caucheteux, C., Nayak, C., Bi, C., Marra,
C., McConnell, C., Keller, C., Touret, C., Wu, C., Wong,
C., Ferrer, C. C., Nikolaidis, C., Allonsius, D., Song, D.,
Pintz, D., Livshits, D., Wyatt, D., Esiobu, D., Choudhary,
D., Mahajan, D., Garcia-Olano, D., Perino, D., Hupkes,
D., Lakomkin, E., AlBadawy, E., Lobanova, E., Dinan,
E., Smith, E. M., Radenovic, F., Guzmán, F., Zhang, F.,
Synnaeve, G., Lee, G., Anderson, G. L., Thattai, G., Nail,
G., Mialon, G., Pang, G., Cucurell, G., Nguyen, H., Korevaar, H., Xu, H., Touvron, H., Zarov, I., Ibarra, I. A.,
Kloumann, I., Misra, I., Evtimov, I., Zhang, J., Copet, J.,
Lee, J., Geffert, J., Vranes, J., Park, J., Mahadeokar, J.,
Shah, J., van der Linde, J., Billock, J., Hong, J., Lee, J.,
Fu, J., Chi, J., Huang, J., Liu, J., Wang, J., Yu, J., Bitton,
J., Spisak, J., Park, J., Rocca, J., Johnstun, J., Saxe, J., Jia,
J., Alwala, K. V., Prasad, K., Upasani, K., Plawiak, K., Li,
K., Heafield, K., Stone, K., El-Arini, K., Iyer, K., Malik,
K., Chiu, K., Bhalla, K., Lakhotia, K., Rantala-Yeary,
L., van der Maaten, L., Chen, L., Tan, L., Jenkins, L.,
Martin, L., Madaan, L., Malo, L., Blecher, L., Landzaat,
L., de Oliveira, L., Muzzi, M., Pasupuleti, M., Singh,
M., Paluri, M., Kardas, M., Tsimpoukelli, M., Oldham,
M., Rita, M., Pavlova, M., Kambadur, M., Lewis, M.,
Si, M., Singh, M. K., Hassan, M., Goyal, N., Torabi, N.,
Bashlykov, N., Bogoychev, N., Chatterji, N., Zhang, N.,
Duchenne, O., Çelebi, O., Alrassy, P., Zhang, P., Li, P.,
Vasic, P., Weng, P., Bhargava, P., Dubal, P., Krishnan,
P., Koura, P. S., Xu, P., He, Q., Dong, Q., Srinivasan,
R., Ganapathy, R., Calderer, R., Cabral, R. S., Stojnic,
R., Raileanu, R., Maheswari, R., Girdhar, R., Patel, R.,
Sauvestre, R., Polidoro, R., Sumbaly, R., Taylor, R., Silva,
R., Hou, R., Wang, R., Hosseini, S., Chennabasappa, S.,
Singh, S., Bell, S., Kim, S. S., Edunov, S., Nie, S., Narang,
S., Raparthy, S., Shen, S., Wan, S., Bhosale, S., Zhang,
S., Vandenhende, S., Batra, S., Whitman, S., Sootla, S.,
Collot, S., Gururangan, S., Borodinsky, S., Herman, T.,
Fowler, T., Sheasha, T., Georgiou, T., Scialom, T., Speckbacher, T., Mihaylov, T., Xiao, T., Karn, U., Goswami, V.,
Gupta, V., Ramanathan, V., Kerkez, V., Gonguet, V., Do,
V., Vogeti, V., Albiero, V., Petrovic, V., Chu, W., Xiong,
W., Fu, W., Meers, W., Martinet, X., Wang, X., Wang,

PreScience: A Benchmark for Forecasting Scientific Contributions

X., Tan, X. E., Xia, X., Xie, X., Jia, X., Wang, X., Goldschlag, Y., Gaur, Y., Babaei, Y., Wen, Y., Song, Y., Zhang,
Y., Li, Y., Mao, Y., Coudert, Z. D., Yan, Z., Chen, Z.,
Papakipos, Z., Singh, A., Srivastava, A., Jain, A., Kelsey,
A., Shajnfeld, A., Gangidi, A., Victoria, A., Goldstand,
A., Menon, A., Sharma, A., Boesenberg, A., Baevski, A.,
Feinstein, A., Kallet, A., Sangani, A., Teo, A., Yunus, A.,
Lupu, A., Alvarado, A., Caples, A., Gu, A., Ho, A., Poulton, A., Ryan, A., Ramchandani, A., Dong, A., Franco,
A., Goyal, A., Saraf, A., Chowdhury, A., Gabriel, A.,
Bharambe, A., Eisenman, A., Yazdan, A., James, B.,
Maurer, B., Leonhardi, B., Huang, B., Loyd, B., Paola,
B. D., Paranjape, B., Liu, B., Wu, B., Ni, B., Hancock,
B., Wasti, B., Spence, B., Stojkovic, B., Gamido, B.,
Montalvo, B., Parker, C., Burton, C., Mejia, C., Liu, C.,
Wang, C., Kim, C., Zhou, C., Hu, C., Chu, C.-H., Cai, C.,
Tindal, C., Feichtenhofer, C., Gao, C., Civin, D., Beaty,
D., Kreymer, D., Li, D., Adkins, D., Xu, D., Testuggine,
D., David, D., Parikh, D., Liskovich, D., Foss, D., Wang,
D., Le, D., Holland, D., Dowling, E., Jamil, E., Montgomery, E., Presani, E., Hahn, E., Wood, E., Le, E.-T.,
Brinkman, E., Arcaute, E., Dunbar, E., Smothers, E., Sun,
F., Kreuk, F., Tian, F., Kokkinos, F., Ozgenel, F., Caggioni, F., Kanayet, F., Seide, F., Florez, G. M., Schwarz,
G., Badeer, G., Swee, G., Halpern, G., Herman, G., Sizov,
G., Guangyi, Zhang, Lakshminarayanan, G., Inan, H.,
Shojanazeri, H., Zou, H., Wang, H., Zha, H., Habeeb, H.,
Rudolph, H., Suk, H., Aspegren, H., Goldman, H., Zhan,
H., Damlaj, I., Molybog, I., Tufanov, I., Leontiadis, I.,
Veliche, I.-E., Gat, I., Weissman, J., Geboski, J., Kohli,
J., Lam, J., Asher, J., Gaya, J.-B., Marcus, J., Tang, J.,
Chan, J., Zhen, J., Reizenstein, J., Teboul, J., Zhong, J.,
Jin, J., Yang, J., Cummings, J., Carvill, J., Shepard, J.,
McPhie, J., Torres, J., Ginsburg, J., Wang, J., Wu, K., U,
K. H., Saxena, K., Khandelwal, K., Zand, K., Matosich,
K., Veeraraghavan, K., Michelena, K., Li, K., Jagadeesh,
K., Huang, K., Chawla, K., Huang, K., Chen, L., Garg,
L., A, L., Silva, L., Bell, L., Zhang, L., Guo, L., Yu, L.,
Moshkovich, L., Wehrstedt, L., Khabsa, M., Avalani, M.,
Bhatt, M., Mankus, M., Hasson, M., Lennie, M., Reso,
M., Groshev, M., Naumov, M., Lathi, M., Keneally, M.,
Liu, M., Seltzer, M. L., Valko, M., Restrepo, M., Patel,
M., Vyatskov, M., Samvelyan, M., Clark, M., Macey,
M., Wang, M., Hermoso, M. J., Metanat, M., Rastegari,
M., Bansal, M., Santhanam, N., Parks, N., White, N.,
Bawa, N., Singhal, N., Egebo, N., Usunier, N., Mehta,
N., Laptev, N. P., Dong, N., Cheng, N., Chernoguz, O.,
Hart, O., Salpekar, O., Kalinli, O., Kent, P., Parekh, P.,
Saab, P., Balaji, P., Rittner, P., Bontrager, P., Roux, P.,
Dollar, P., Zvyagina, P., Ratanchandani, P., Yuvraj, P.,
Liang, Q., Alao, R., Rodriguez, R., Ayub, R., Murthy, R.,
Nayani, R., Mitra, R., Parthasarathy, R., Li, R., Hogan,
R., Battey, R., Wang, R., Howes, R., Rinott, R., Mehta,
S., Siby, S., Bondu, S. J., Datta, S., Chugh, S., Hunt, S.,

Dhillon, S., Sidorov, S., Pan, S., Mahajan, S., Verma,
S., Yamamoto, S., Ramaswamy, S., Lindsay, S., Lindsay,
S., Feng, S., Lin, S., Zha, S. C., Patil, S., Shankar, S.,
Zhang, S., Zhang, S., Wang, S., Agarwal, S., Sajuyigbe,
S., Chintala, S., Max, S., Chen, S., Kehoe, S., Satterfield, S., Govindaprasad, S., Gupta, S., Deng, S., Cho,
S., Virk, S., Subramanian, S., Choudhury, S., Goldman,
S., Remez, T., Glaser, T., Best, T., Koehler, T., Robinson,
T., Li, T., Zhang, T., Matthews, T., Chou, T., Shaked,
T., Vontimitta, V., Ajayi, V., Montanez, V., Mohan, V.,
Kumar, V. S., Mangla, V., Ionescu, V., Poenaru, V., Mihailescu, V. T., Ivanov, V., Li, W., Wang, W., Jiang, W.,
Bouaziz, W., Constable, W., Tang, X., Wu, X., Wang, X.,
Wu, X., Gao, X., Kleinman, Y., Chen, Y., Hu, Y., Jia, Y.,
Qi, Y., Li, Y., Zhang, Y., Zhang, Y., Adi, Y., Nam, Y., Yu,
Wang, Zhao, Y., Hao, Y., Qian, Y., Li, Y., He, Y., Rait,
Z., DeVito, Z., Rosnbrick, Z., Wen, Z., Yang, Z., Zhao,
Z., and Ma, Z. The llama 3 herd of models, 2024. URL
https://arxiv.org/abs/2407.21783.
Gu, X. and Krenn, M. Forecasting high-impact research
topics via machine learning on evolving knowledge
graphs. Machine Learning: Science and Technology,
6, 2024. URL https://api.semanticscholar.
org/CorpusID:267636723.
Guo, S., Shariatmadari, A. H., Xiong, G., Huang, A., Xie,
E., Bekiranov, S., and Zhang, A. Ideabench: Benchmarking large language models for research idea generation. Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2,
2025. URL https://api.semanticscholar.
org/CorpusID:273821733.
Győrffy, B., Herman, P., and Szabó, I.
Research
funding: past performance is a stronger predictor
of future scientific output than reviewer scores.
J. Informetrics, 14:101050, 2020.
URL https:
//api.semanticscholar.org/CorpusID:
219933512.
Hadžić, A., Papez, M., and Pevný, T. Distillation of a
tractable model from the vq-vae, 2025. URL https:
//arxiv.org/abs/2509.01400.
Ho, T. K. T., Bui, Q. V., and Bui, M. Co-author relationship prediction in bibliographic network: A new approach using geographic factor and latent topic information. Proceedings of the 10th International Symposium on Information and Communication Technology,
2019. URL https://api.semanticscholar.
org/CorpusID:209450869.
Hu, E. J., Shen, Y., Wallis, P., Allen-Zhu, Z., Li, Y., Wang,
S., Wang, L., and Chen, W. LoRA: Low-rank adaptation
of large language models. In International Conference
12

PreScience: A Benchmark for Forecasting Scientific Contributions

on Learning Representations, 2022. URL https://
openreview.net/forum?id=nZeVKeeFYf9.
Huang, L., Huang, C., Leng, J., Huang, D., and Huang,
J. Poss: Position specialist generates better draft for
speculative decoding, 2025. URL https://arxiv.
org/abs/2506.03566.
Jansen, P., Tafjord, O., Radensky, M., Siangliulue,
P., Hope, T., Dalvi, B., Majumder, B. P., Weld,
D. S., and Clark, P.
Codescientist: End-toend semi-automated scientific discovery with codebased experimentation.
ArXiv, abs/2503.22708,
2025. URL https://api.semanticscholar.
org/CorpusID:277451644.
Jansen, P. A., Côté, M.-A., Khot, T., Bransom,
E., Dalvi, B., Majumder, B. P., Tafjord, O., and
Clark, P.
Discoveryworld: A virtual environment for developing and evaluating automated scientific discovery agents.
ArXiv, abs/2406.06769,
2024. URL https://api.semanticscholar.
org/CorpusID:270380311.
Järvelin, K. and Kekäläinen, J. Cumulated gain-based evaluation of ir techniques. ACM Trans. Inf. Syst., 20:422–446,
2002. URL https://api.semanticscholar.
org/CorpusID:1981391.
Jin, L., Ruan, Z., Mai, H., and Shang, J. Verilocc: End-toend cross-architecture register allocation via llm, 2025.
URL https://arxiv.org/abs/2506.17506.

Koopmann, T., Kobs, K., Herud, K., and Hotho, A.
Cobert: Scientific collaboration prediction via sequential recommendation. 2021 International Conference
on Data Mining Workshops (ICDMW), pp. 45–54,
2021. URL https://api.semanticscholar.
org/CorpusID:246081502.
Lee, A. X. W., Yeung, P.-H., and Rajapakse, J. C. Subcortical Masks Generation in CT Images via Ensemble-Based
Cross-Domain Label Transfer, pp. 160–174. Springer Nature Switzerland, July 2025. ISBN 9783031986949. doi:
10.1007/978-3-031-98694-9 12. URL http://dx.
doi.org/10.1007/978-3-031-98694-9_12.
Lewandowski, A., Schuurmans, D., and Machado, M. C.
Plastic learning with deep fourier features, 2024. URL
https://arxiv.org/abs/2410.20634.
Li, D., Wang, Y., Cleaveland, M., Cai, M., and
Tron, R.
Conformal prediction for signal temporal logic inference.
ArXiv, abs/2509.25473,
2025. URL https://api.semanticscholar.
org/CorpusID:281682043.
Li, X., Wang, M., Wang, C., Fu, Y., and Wang,
X. Novsrc: A novelty-oriented scientific collaborators recommendation model. International Journal of Advanced Computer Science and Applications,
2024. URL https://api.semanticscholar.
org/CorpusID:268818672.
Liben-Nowell, D. and Kleinberg, J. The link prediction problem for social networks. In Proceedings of the Twelfth
International Conference on Information and Knowledge Management, CIKM ’03, pp. 556–559, New York,
NY, USA, 2003a. Association for Computing Machinery.
ISBN 1581137230. doi: 10.1145/956863.956972. URL
https://doi.org/10.1145/956863.956972.

Kanakaris, N., Giarelis, N., Siachos, I., and Karacapilidis, N. Shall i work with them? a knowledge
graph-based approach for predicting future research
collaborations. Entropy, 23, 2021. URL https:
//api.semanticscholar.org/CorpusId:
235301976.

Liben-Nowell, D. and Kleinberg, J. M. The link prediction problem for social networks. In International Conference on Information and Knowledge Management,
2003b. URL http://dl.acm.org/citation.
cfm?id=956972.

Kapoor, T., Chandra, A., Stamou, A., and Roberts, S. J.
Beyond accuracy: Ecol2 metric for sustainable neural
pde solvers, 2025. URL https://arxiv.org/abs/
2505.12556.
Kendall, M. G.
A new measure of rank correlation. Biometrika, 30:81–93, 1938. URL https:
//api.semanticscholar.org/CorpusID:
120478295.

Lu, C., Lu, C., Lange, R. T., Foerster, J. N., Clune, J.,
and Ha, D. The ai scientist: Towards fully automated
open-ended scientific discovery. ArXiv, abs/2408.06292,
2024. URL https://api.semanticscholar.
org/CorpusID:271854887.

Kong, X., Shi, Y., Yu, S., Liu, J., and Xia, F. Academic social networks: Modeling, analysis, mining
and applications. J. Netw. Comput. Appl., 132:86–103,
2019. URL https://api.semanticscholar.
org/CorpusID:86850665.

Lundberg, S. M. and Lee, S.-I. A unified approach to interpreting model predictions. In Proceedings of the 31st International Conference on Neural Information Processing
Systems, NIPS’17, pp. 4768–4777, Red Hook, NY, USA,
2017. Curran Associates Inc. ISBN 9781510860964.

13

PreScience: A Benchmark for Forecasting Scientific Contributions

Luu, K., Wu, X., Koncel-Kedziorski, R., Lo, K., Cachola, I., and Smith, N. A. Explaining relationships between scientific documents. In Annual Meeting of the Association for Computational Linguistics,
2020. URL https://api.semanticscholar.
org/CorpusID:236459799.
Majumder, B. P., Surana, H., Agarwal, D., Mishra, B. D.,
Meena, A., Prakhar, A., Vora, T., Khot, T., Sabharwal,
A., and Clark, P. Discoverybench: Towards data-driven
discovery with large language models. In The Thirteenth
International Conference on Learning Representations,
2025. URL https://openreview.net/forum?
id=vyflgpwfJW.

2022 Conference of the North American Chapter of
the Association for Computational Linguistics: Human Language Technologies, pp. 4453–4470, Seattle,
United States, July 2022. Association for Computational Linguistics. doi: 10.18653/v1/2022.naacl-main.
331. URL https://aclanthology.org/2022.
naacl-main.331/.
Ni, J., Qu, C., Lu, J., Dai, Z., Hernandez Abrego, G., Ma, J.,
Zhao, V., Luan, Y., Hall, K., Chang, M.-W., and Yang, Y.
Large dual encoders are generalizable retrievers. In Goldberg, Y., Kozareva, Z., and Zhang, Y. (eds.), Proceedings
of the 2022 Conference on Empirical Methods in Natural
Language Processing, pp. 9844–9855, Abu Dhabi, United
Arab Emirates, December 2022. Association for Computational Linguistics. doi: 10.18653/v1/2022.emnlp-main.
669. URL https://aclanthology.org/2022.
emnlp-main.669/.

Margatina, K., Wang, S., Vyas, Y., Anna John, N., Benajiba, Y., and Ballesteros, M. Dynamic benchmarking of masked language models on temporal concept
drift with multiple views. In Vlachos, A. and Augenstein, I. (eds.), Proceedings of the 17th Conference of
the European Chapter of the Association for Computational Linguistics, pp. 2881–2898, Dubrovnik, Croatia,
May 2023. Association for Computational Linguistics.
doi: 10.18653/v1/2023.eacl-main.211. URL https://
aclanthology.org/2023.eacl-main.211/.

Ni, Z., Wang, Y., Zhou, R., Han, Y., Guo, J., Liu, Z., Yao,
Y., and Huang, G. Enat: Rethinking spatial-temporal
interactions in token-based image synthesis, 2024. URL
https://arxiv.org/abs/2411.06959.
NIST TREC. Common evaluation measures. TREC
2006 Proceedings (Appendix), 2006.
URL
https://trec.nist.gov/pubs/trec15/
appendices/CE.MEASURES06.pdf. Appendix
CE.MEASURES06.

Merton, R. K. The matthew effect in science. Science, 159
(3810):56–63, 1968.
Miao, Y., Chen, Z., Li, C., and Mandic, D. Respdiff: An
end-to-end multi-scale rnn diffusion model for respiratory waveform estimation from ppg signals, 2024. URL
https://arxiv.org/abs/2410.04366.

Muennighoff, N., SU, H., Wang, L., Yang, N., Wei, F.,
Yu, T., Singh, A., and Kiela, D. Generative representational instruction tuning. In The Thirteenth International Conference on Learning Representations,
2025. URL https://openreview.net/forum?
id=BC4lIvfSzv.

Olmo, T., :, Ettinger, A., Bertsch, A., Kuehl, B., Graham, D.,
Heineman, D., Groeneveld, D., Brahman, F., Timbers, F.,
Ivison, H., Morrison, J., Poznanski, J., Lo, K., Soldaini,
L., Jordan, M., Chen, M., Noukhovitch, M., Lambert, N.,
Walsh, P., Dasigi, P., Berry, R., Malik, S., Shah, S., Geng,
S., Arora, S., Gupta, S., Anderson, T., Xiao, T., Murray,
T., Romero, T., Graf, V., Asai, A., Bhagia, A., Wettig,
A., Liu, A., Rangapur, A., Anastasiades, C., Huang, C.,
Schwenk, D., Trivedi, H., Magnusson, I., Lochner, J., Liu,
J., Miranda, L. J. V., Sap, M., Morgan, M., Schmitz, M.,
Guerquin, M., Wilson, M., Huff, R., Bras, R. L., Xin, R.,
Shao, R., Skjonsberg, S., Shen, S. Z., Li, S. S., Wilde,
T., Pyatkin, V., Merrill, W., Chang, Y., Gu, Y., Zeng, Z.,
Sabharwal, A., Zettlemoyer, L., Koh, P. W., Farhadi, A.,
Smith, N. A., and Hajishirzi, H. Olmo 3, 2025. URL
https://arxiv.org/abs/2512.13961.

Munasinghe, L. and Ichise, R. Time score: A new feature for link prediction in social networks. IEICE Trans.
Inf. Syst., 95-D:821–828, 2012. URL https://api.
semanticscholar.org/CorpusID:30012200.

O’Madadhain, J., Hutchins, J., and Smyth, P. Prediction
and ranking algorithms for event-based network data.
SIGKDD Explor., 7:23–30, 2005. URL https://api.
semanticscholar.org/CorpusID:3343116.

Mysore, S., Cohan, A., and Hope, T. Multi-vector models with textual guidance for fine-grained scientific document similarity. In Carpuat, M., de Marneffe, M.C., and Meza Ruiz, I. V. (eds.), Proceedings of the

Opris, A. A first runtime analysis of nsga-iii on a manyobjective multimodal problem: Provable exponential
speedup via stochastic population update, 2025. URL
https://arxiv.org/abs/2505.01256.

Miech, A., Alayrac, J.-B., Smaira, L., Laptev, I.,
Sivic, J., and Zisserman, A. End-to-end learning
of visual representations from uncurated instructional
videos. 2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), pp. 9876–9886,
2019. URL https://api.semanticscholar.
org/CorpusID:209370497.

14

PreScience: A Benchmark for Forecasting Scientific Contributions

Pier, E. L., Brauer, M., Filut, A., et al. Low agreement
among reviewers evaluating the same nih grant applications. Proceedings of the National Academy of Sciences,
115(12):2952–2957, 2018.

Sternlicht, N. and Hope, T. Chimera: A knowledge base of
scientific idea recombinations for research analysis and
ideation, 2025. URL https://arxiv.org/abs/
2505.20779.

Pramanick, A., Hou, Y., Mohammad, S. M., and
Gurevych, I. The nature of nlp: Analyzing contributions in nlp papers.
ArXiv, abs/2409.19505,
2024. URL https://api.semanticscholar.
org/CorpusID:272986926.

Su, H., Chen, R., Tang, S., Yin, Z., Zheng, X., Li,
J., Qi, B., Wu, Q., Li, H., Ouyang, W., Torr, P.,
Zhou, B., and Dong, N.
Many heads are better than one: Improved scientific idea generation by
a llm-based multi-agent system. In Annual Meeting of the Association for Computational Linguistics,
2024. URL https://api.semanticscholar.
org/CorpusID:273346445.

Radensky, M., Shahid, S., Fok, R., Siangliulue, P.,
Hope, T., and Weld, D. S.
Scideator: Humanllm scientific idea generation grounded in researchpaper facet recombination. ArXiv, abs/2409.14634,
2024. URL https://api.semanticscholar.
org/CorpusID:272827497.
Redman, B. Science evaluation: Peer review, bibliometrics, and research impact assessment. In Reconstructing
Research Integrity, pp. 127–148. Springer, 2023.
Riechers, P. M., Elliott, T. J., and Shai, A. S. Neural networks leverage nominally quantum and post-quantum
representations, 2025. URL https://arxiv.org/
abs/2507.07432.
Semnani, S. J., Zhang, H., He, X., Tekgürler, M., and Lam,
M. S. Churro: Making history readable with an openweight large vision-language model for high-accuracy,
low-cost historical text recognition, 2025. URL https:
//arxiv.org/abs/2509.19768.

Su, H., Chen, R., Tang, S., Yin, Z., Zheng, X., Li, J., Qi, B.,
Wu, Q., Li, H., Ouyang, W., Torr, P., Zhou, B., and Dong,
N. Many heads are better than one: Improved scientific
idea generation by a LLM-based multi-agent system. In
Che, W., Nabende, J., Shutova, E., and Pilehvar, M. T.
(eds.), Proceedings of the 63rd Annual Meeting of the
Association for Computational Linguistics (Volume 1:
Long Papers), pp. 28201–28240, Vienna, Austria, July
2025. Association for Computational Linguistics. ISBN
979-8-89176-251-0. doi: 10.18653/v1/2025.acl-long.
1368. URL https://aclanthology.org/2025.
acl-long.1368/.
Subramanian, S., King, D., Downey, D., and Feldman, S.
S2AND: A Benchmark and Evaluation System for Author
Name Disambiguation. In JCDL ’21: Proceedings of the
ACM/IEEE Joint Conference on Digital Libraries in 2021,
JCDL ’21, New York, NY, USA, 2021. Association for
Computing Machinery.

Shalyt, M., Seligmann, U., Halachmi, I. B., David, O.,
Elimelech, R., and Kaminer, I. Unsupervised discovery of formulas for mathematical constants, 2024. URL
https://arxiv.org/abs/2412.16818.
Sharifymoghaddam, S., Pradeep, R., Slavescu, A., Nguyen,
R., Xu, A., Chen, Z., Zhang, Y., Chen, Y., Xian, J.,
and Lin, J. Rankllm: A python package for reranking
with llms, 2025. URL https://arxiv.org/abs/
2505.19284.

Sun, Y., Barber, R., Gupta, M., Aggarwal, C., and
Han, J. Co-author relationship prediction in heterogeneous bibliographic networks.
2011 International Conference on Advances in Social Networks Analysis and Mining, pp. 121–128, 2011.
URL http://ieeexplore.ieee.org/stamp/
stamp.jsp?tp=&arnumber=5992571.

Shi, F. and Evans, J. Surprising combinations of research
contents and contexts are related to impact and emerge
with scientific outsiders from distant disciplines. Nature
Communications, 14(1):1641, 2023.

Swanson, D. R. Undiscovered public knowledge. The
Library Quarterly, 56:103 – 118, 1986. URL https:
//api.semanticscholar.org/CorpusID:
267792818.

Singh, A., D’Arcy, M., Cohan, A., Downey, D., and Feldman, S. SciRepEval: A multi-format benchmark for scientific document representations. In Bouamor, H., Pino, J.,
and Bali, K. (eds.), Proceedings of the 2023 Conference
on Empirical Methods in Natural Language Processing,
pp. 5548–5566, Singapore, December 2023. Association
for Computational Linguistics. doi: 10.18653/v1/2023.
emnlp-main.338. URL https://aclanthology.
org/2023.emnlp-main.338/.

Swanson, K., Wu, W., Bulaong, N. L., Pak, J. E., and Zou,
J. Y. The virtual lab: Ai agents design new sars-cov2 nanobodies with experimental validation. bioRxiv,
2024. URL https://api.semanticscholar.
org/CorpusID:274060096.

15

Thelwall, M. et al. Predicting article quality scores with machine learning: The u.k. research excellence framework.
Quantitative Science Studies, 4(2):547–573, 2023.

PreScience: A Benchmark for Forecasting Scientific Contributions

Tuninetti, M., Aleta, A., Paolotti, D., Moreno, Y., and
Starnini, M. Prediction of new scientific collaborations through multiplex networks. EPJ Data Science,
10, 2021. URL https://api.semanticscholar.
org/CorpusID:234489207.
Uddin, S., Hossain, L., and Rasmussen, K. J. R. Network effects on scientific collaborations. PLoS ONE,
8, 2013. URL https://api.semanticscholar.
org/CorpusID:7633781.
Valenzuela-Escarcega, M. A., Ha, V. A., and Etzioni,
O. Identifying meaningful citations. In AAAI Workshop: Scholarly Big Data, 2015. URL https://api.
semanticscholar.org/CorpusID:2538517.

Yang, Y., Dan, S., Roth, D., and Lee, I. Benchmarking llm
guardrails in handling multilingual toxicity, 2024. URL
https://arxiv.org/abs/2410.22153.
Yu, H., Hong, Z., Cheng, Z., Zhu, K., Xuan, K., Yao,
J., Feng, T., and You, J. Researchtown: Simulator of
human research community. ArXiv, abs/2412.17767,
2024. URL https://api.semanticscholar.
org/CorpusID:274992362.
Zhang, T., Kishore, V., Wu, F., Weinberger, K. Q., and
Artzi, Y. Bertscore: Evaluating text generation with
bert. ArXiv, abs/1904.09675, 2019. URL https:
//api.semanticscholar.org/CorpusID:
127986044.
Zhang, Y., Tang, H., Wang, C., and Ding, W. Policy newton
algorithm in reproducing kernel hilbert space, 2025. URL
https://arxiv.org/abs/2506.01597.

Vu, D. Q., Asuncion, A. U., Hunter, D. R., and Smyth,
P. Dynamic egocentric models for citation networks.
In Proceedings of the 28th International Conference on
Machine Learning (ICML), 2011.
Wade, A. D. The semantic scholar academic graph (s2ag).
Companion Proceedings of the Web Conference 2022,
2022. URL https://api.semanticscholar.
org/CorpusID:251597885.
Wang, D., Song, C., and Barabási, A.-L. Quantifying
long-term scientific impact. Science, 342(6154):127–132,
2013a.
Wang, D., Song, C., and Ĺaszló Barabási, A. Quantifying
long-term scientific impact. Science, 342:127 – 132,
2013b. URL https://api.semanticscholar.
org/CorpusID:260558492.
Wang, Q., Downey, D., Ji, H., and Hope, T. Scimon: Scientific inspiration machines optimized for
novelty. In Annual Meeting of the Association for
Computational Linguistics, 2023.
URL https:
//api.semanticscholar.org/CorpusID:
258841365.
Wang, W., Gu, L., Zhang, L., Luo, Y., Dai, Y., Shen, C.,
Xie, L., Lin, B., He, X., and Ye, J. Scipip: An llm-based
scientific paper idea proposer. ArXiv, abs/2410.23166,
2024. URL https://api.semanticscholar.
org/CorpusID:273695165.
Weis, J. W. and Jacobson, J. Delphi: A machine learning
framework for early alert of high-impact research. Nature
Biotechnology, 2021.
Xi, X., Guo, Y., and Duan, W. Recommendation of academic collaborators: A methodology incorporating word
embedding and network embedding. In AII@iConference,
2021. URL https://api.semanticscholar.
org/CorpusID:235259334.
16

Zhang, Z. and Evans, J. Language model perplexity predicts scientific surprise and transformative impact. arXiv
preprint arXiv:2509.05591, 2025.
Zhang, Z., Patra, B. G., Yaseen, A., Zhu, J., Sabharwal, R., Roberts, K., Cao, T. H., and Wu, H.
Scholarly recommendation systems: a literature survey. Knowledge and Information Systems, 65:4433–4478,
2023. URL https://api.semanticscholar.
org/CorpusID:259081885.
Zhao, C., Pisu, P., Comert, G., Begashaw, N., Vaidyan,
V., and Hubig, N. C. Causal interpretability for adversarial robustness: A hybrid generative classification
approach, 2025. URL https://arxiv.org/abs/
2412.20025.

PreScience: A Benchmark for Forecasting Scientific Contributions

A. PreScience Dataset
A.1. Statistics
Figure 5 visualizes key properties of the PreScience dataset over target papers, including distributions of author counts
per paper, author publication history lengths, key reference counts, and citation trajectories. These statistics highlight the
heavy-tailed and heterogeneous structure of the benchmark, which underlies the difficulty of forecasting collaboration,
literature choice, and downstream impact.

(a) Number of Authors per paper

(b) Author Publication History Length

(c) Number of Key References per paper

(d) (Averaged) Citation Trajectories of target papers of various
ages in the PreScience corpus

Figure 5. Author, Key Reference and Citation Trajectory statistics plotted over Target papers.

A.2. Features
We organize papers in PreScience into four roles: target papers, key references of target papers, papers in a target author’s
publication history, and key references of those publication-history papers. All papers share a common set of bibliographic
fields (Semantic Scholar corpus ID, arXiv ID, publication date, arXiv categories, title, and abstract).
For target papers, we additionally ensure the availability of complete, temporally aligned citation- and author-level metadata,
including key references, cumulative citation counts at the time of publication, and author statistics (IDs, names, h-indices,
publication counts, and citation counts), as well as each author’s publication history up to the same publication time.
For certain companion papers, some feature availability is best-effort: we include key references and basic author identity
when they can be reliably recovered from the Semantic Scholar Graph and matched to arXiv preprints, but these fields may
be empty when a cited work is not indexed by Semantic Scholar or does not have an arXiv version. Table 5 summarizes
17

PreScience: A Benchmark for Forecasting Scientific Contributions

feature availability by role, with checkmarks indicating required fields and parentheses indicating best-effort fields.
Table 5. Feature availability by paper role in the PreScience dataset. A checkmark (✓) indicates that the field is provided; parentheses
indicate best-effort availability. All papers are restricted to arXiv preprints reachable from at least one target paper through the relations
described in Section 3.

Field

Target

Target.Key Ref

Author Pub. Hist.

Author Pub. Hist. Key Ref

✓
✓
✓
✓
✓
✓

✓
✓
✓
✓
✓
✓

✓
✓
✓
✓
✓
✓

✓
✓
✓
✓
✓
✓

✓
✓

–
–

(✓)
–

–
–

✓
✓
✓
✓
✓
✓

–
–
–
–
–
–

(✓)
(✓)
–
–
–
–

–
–
–
–
–
–

Paper Metadata
Corpus ID
arXiv ID
Publication Date
arXiv Categories
Title
Abstract

Citation and Reference Data
Key References
Citations @ Pub. Time
Author Metadata
Author IDs
Author Names
Author h-index
Author Num. Papers
Author Num. Citations
Publication History

18

PreScience: A Benchmark for Forecasting Scientific Contributions

B. Collaborator Prediction
B.1. Effect of Seed Author Choice
We find that the choice of seed author in the collaborator prediction task does not affect the relative ordering of baseline
performance. This is a non-trivial result, as research team formation and collaborator discovery may be governed by different
mechanisms for authors at different career stages or seniority levels. However, the baselines we evaluate primarily operate on
order-invariant features of the observed co-authorship graph (e.g., local neighborhoods and aggregated publication histories),
so it appears changing the seed largely only shifts the strength of the underlying collaboration signal without favoring any of
the baselines over others.
Table 6. Effect of seed author choice on collaborator prediction performance (nDCG) (n=1000). The relative performance order among
baselines remains unchanged.

Baseline

First

Last

Random

Argmax h-index

Frequency
Rank Fusion (GRIT)
Embedding Fusion (GRIT)
Embedding Fusion + Projection (GRIT)

0.38
0.15
0.29
0.24

0.34
0.12
0.23
0.22

0.37
0.14
0.26
0.23

0.26
0.10
0.18
0.18

B.2. Further Task Analyses
Figure 6 analyzes collaborator prediction performance across two sources of variation. Panel (a) shows that nDCG typically
decreases as the first author’s publication history length grows, indicating that larger and more crowded collaboration
neighborhoods dilute the signal available to frequency- and embedding-based baselines. Panel (b) shows that R-Precision
declines monotonically with team size, reflecting the increasing combinatorial difficulty of recovering all collaborators as
the target set grows.

(a) Prediction difficulty appears to increase with longer author
publication history.

(b) Predicting collaborators is easier for smaller teams.

Figure 6. Collaborator Prediction

19

PreScience: A Benchmark for Forecasting Scientific Contributions

C. Prior Work Selection
C.1. Effect of “Key” References Choice
In addition to the production implementation of Semantic Scholar’s highly influential references (Valenzuela-Escarcega
et al., 2015), we evaluate two alternative definitions of influential prior work: (i) using the full set of references cited by
each paper, and (ii) using impact-revealing references (Arnaout et al., 2025). As shown in Table 7, neither alternative
yields a dramatic improvement in prediction performance over the default key-reference definition11 . However, both incur
substantially higher computational and data costs: including all references dramatically expands the set of companion papers
and causes the historical corpus H<t to balloon, while computing impact-revealing references requires repeated calls to
commercial LLM APIs. These results motivate our use of Semantic Scholar key references as a practical trade-off between
predictive signal and scalability.
Table 7. Prior work selection performance (n=1000) across reference types. Standard deviations are shown in subscript parentheses.
Reference Type
S2 Highly Influential
All References
Impact-Revealing

Reference Count

nDCG

R-Prec

5.43(0.12)
34.04(0.63)
10.65(0.22)

4.2(0.4)
7.6(0.3)
5.7(0.3)

3.0(0.3)
4.6(0.2)
3.6(0.3)

C.2. Further Task Analyses
Figure 7 presents analyses of prior work selection performance across author experience, number of references, and team
size. Across all three views, we observe limited and non-monotonic variation in nDCG and R-Precision across baselines,
suggesting that no single factor strongly governs performance in isolation.

(a) nDCG vs. the research team’s mean publication history length

(b) nDCG vs. key reference count

(c) R-precision vs. research team size

Figure 7. Prior Work Selection

11
These results are reported on an earlier snapshot of the corpus; we expect the updated release to preserve the relative trends across
reference definitions, even if absolute values shift.

20

PreScience: A Benchmark for Forecasting Scientific Contributions

D. Contribution Generation
D.1. Effect of Pretraining Corpus Contamination
Table 8 compares mean LACER scores in the month immediately before and after each model’s reported knowledge
cutoff date. We observe modest changes in absolute scores and no changes in relative model ordering, suggesting that any
cutoff-related effects are small relative to the performance differences reported in the main results.
Table 8. Mean LACER scores (over 1 month) before and after model knowledge cutoff dates.

Model

Cutoff Date

Pre-cutoff

Post-cutoff

Claude Sonnet 4.5
Claude Opus 4.5
GPT-5.2

Jan 31, 2025
May 31, 2025
Aug 31, 2025

4.900
5.054
5.706

5.062
5.008
5.595

D.2. Further Task Analyses
Figure 8(a) shows that contribution generation becomes easier as more key references are available, consistent with additional
contextual signal improving conceptual alignment. Figure 8(b) indicates that LACER scores are largely insensitive to a
paper’s future citation impact, suggesting that predictive difficulty is decoupled from downstream popularity. Figure 8(c)
shows that papers whose key references have lower average citation counts are easier to predict. This is consistent with
highly cited prior work being useful to a wide application space. Figure 8(d) shows that higher topical diversity among key
references is associated with improved prediction performance, perhaps indicating fewer “valid” ways in which diverse
work can be combined (given that the subset can in fact be combined). Figure 8(e) reveals systematic variation across
arXiv categories, with computation-and-language papers exhibiting lower scores and machine-learning papers higher scores.
Figure 8(f) summarizes common failure modes, dominated by problem mismatch and application-context drift rather than
surface-level keyword errors.12

12
We categorize these failure modes by employing prompting GPT-5.2 with a sample of 240 low-scoring generated abstracts along with
their corresponding ground truths and instructing it to study and categorize them into common failure modes.

21

PreScience: A Benchmark for Forecasting Scientific Contributions

(a) Prediction is easier in instances with
more key references.

(b) Prediction difficulty appears agnostic to
future impact of paper.

(c) Papers whose key references have fewer
citations are easier to predict.

(d) Papers whose key references are more
diverse in topics appear easier to predict.

(e) There is statistically significant varia- (f) Problem mismatch and application drift
tion in LLMs’ abilites to predict work corre- account for the majority of incorrect predicsponding to different ArXiv topics.
tions.
Figure 8. Contribution Generation

D.3. Contribution Generation LLM Prompt
We provide below, the prompt we use with the baselines we list in Table 3.

Contribution Generation Prompt
You are a seasoned computer science researcher who has done extensive work in machine
,→
learning, deep learning, computer vision, natural language processing,
,→
reinforcement learning, artificial intelligence, human computer interaction, and
,→
many related fields.
You have spent many years on the organizing and peer-review committees of many
,→
relevant conferences and publications like NeurIPS, ICLR, ICML, ICCV, ACL, EMNLP,
,→
NAACL, AAAI, CHI, TMLR, TACL, etc.
You need to use your expertise to accurately and realistically predict a followup
,→
paper that builds on (cites) the set of background papers given to you. For the
,→
paper you predict, you must output its title and abstract.
Below are a few solved examples for this prediction problem where we provide only one
,→
possible followup.
<example 1>
Background Paper 1:
Title: Adam: A Method for Stochastic Optimization

22

PreScience: A Benchmark for Forecasting Scientific Contributions
Abstract: We introduce Adam, an algorithm for first-order gradient-based optimization
,→
of stochastic objective functions. The method is straightforward to implement and
,→
is based on adaptive estimates of lower-order moments of the gradients. The method
,→
is computationally efficient, has little memory requirements and is well suited
,→
for problems that are large in terms of data and/or parameters. The method is also
appropriate for non-stationary objectives and problems with very noisy and/or
,→
,→
sparse gradients. The method exhibits invariance to diagonal rescaling of the
,→
gradients by adapting to the geometry of the objective function. The
,→
hyper-parameters have intuitive interpretations and typically require little
,→
tuning. Some connections to related algorithms, on which Adam was inspired, are
,→
discussed. We also analyze the theoretical convergence properties of the algorithm
,→
and provide a regret bound on the convergence rate that is comparable to the best
,→
known results under the online convex optimization framework. We demonstrate that
,→
Adam works well in practice and compares favorably to other stochastic
,→
optimization methods.
Background Paper 2:
Title: IP-Adapter: Text Compatible Image Prompt Adapter for Text-to-Image Diffusion
,→
Models
Abstract: Recent years have witnessed the strong power of large text-to-image
diffusion models for the impressive generative capability to create high-fidelity
,→
images. However, it is very tricky to generate desired images using only text
,→
prompt as it often involves complex prompt engineering. An alternative to text
,→
prompt is image prompt, as the saying goes:"an image is worth a thousand words".
,→
Although existing methods of direct fine-tuning from pretrained models are
,→
effective, they require large computing resources and are not compatible with
,→
other base models, text prompt, and structural controls. In this paper, we present
,→
IP-Adapter, an effective and lightweight adapter to achieve image prompt
,→
capability for the pretrained text-to-image diffusion models. The key design of
,→
our IP-Adapter is decoupled cross-attention mechanism that separates
,→
cross-attention layers for text features and image features. Despite the
,→
simplicity of our method, an IP-Adapter with only 22M parameters can achieve
,→
comparable or even better performance to a fully fine-tuned image prompt model. As
,→
we freeze the pretrained diffusion model, the proposed IP-Adapter can be
,→
generalized not only to other custom models fine-tuned from the same base model,
,→
but also to controllable generation using existing controllable tools. With the
,→
benefit of the decoupled cross-attention strategy, the image prompt can also work
,→
well with the text prompt to achieve multimodal image generation. The project page
,→
is available at \url{https://ip-adapter.github.io}.
,→
Background Paper 3:
Title: High-Resolution Image Synthesis with Latent Diffusion Models
Abstract: By decomposing the image formation process into a sequential application of
denoising autoencoders, diffusion models (DMs) achieve state-of-the-art synthesis
,→
,→
results on image data and beyond. Additionally, their formulation allows for a
,→
guiding mechanism to control the image generation process without retraining.
,→
However, since these models typically operate directly in pixel space,
,→
optimization of powerful DMs often consumes hundreds of GPU days and inference is
,→
expensive due to sequential evaluations. To enable DM training on limited
,→
computational resources while retaining their quality and flexibility, we apply
,→
them in the latent space of powerful pretrained autoencoders. In contrast to
,→
previous work, training diffusion models on such a representation allows for the
,→
first time to reach a near-optimal point between complexity reduction and detail
,→
preservation, greatly boosting visual fidelity. By introducing cross-attention
,→
layers into the model architecture, we turn diffusion models into powerful and
,→
flexible generators for general conditioning inputs such as text or bounding boxes
,→
and high-resolution synthesis becomes possible in a convolutional manner. Our
latent diffusion models (LDMs) achieve a new state of the art for image inpainting
,→
,→
and highly competitive performance on various tasks, including unconditional image
,→
generation, semantic scene synthesis, and super-resolution, while significantly
,→
reducing computational requirements compared to pixel-based DMs. Code is available
,→
at https://github.com/CompVis/latent-diffusion.

23

PreScience: A Benchmark for Forecasting Scientific Contributions
Background Paper 4:
Title: BrainVis: Exploring the Bridge between Brain and Visual Signals via Image
,→
Reconstruction
Abstract: Analyzing and reconstructing visual stimuli from brain signals effectively
,→
advances the understanding of human visual system. However, the EEG signals are
,→
complex and contain significant noise. This leads to substantial limitations in
,→
existing works of visual stimuli reconstruction from EEG, such as difficulties in
,→
aligning EEG embeddings with the fine-grained semantic information and a heavy
,→
reliance on additional large self-collected dataset for training. To address these
,→
challenges, we propose a novel approach called BrainVis. Firstly, we divide the
,→
EEG signals into various units and apply a self-supervised approach on them to
,→
obtain EEG time-domain features, in an attempt to ease the training difficulty.
,→
Additionally, we also propose to utilize the frequency-domain features to enhance
,→
the EEG representations. Then, we simultaneously align EEG time-frequency
,→
embeddings with the interpolation of the coarse and fine-grained semantics in the
,→
CLIP space, to highlight the primary visual components and reduce the cross-modal
alignment difficulty. Finally, we adopt the cascaded diffusion models to
,→
,→
reconstruct images. Using only 10\% training data of the previous work, our
,→
proposed BrainVis outperforms state of the arts in both semantic fidelity
,→
reconstruction and generation quality. The code is available at
,→
https://github.com/RomGai/BrainVis.
Predicted Followup Paper:
Title: BrainDecoder: Style-Based Visual Decoding of EEG Signals
Abstract: Decoding neural representations of visual stimuli from
electroencephalography (EEG) offers valuable insights into brain activity and
,→
cognition. Recent advancements in deep learning have significantly enhanced the
,→
field of visual decoding of EEG, primarily focusing on reconstructing the semantic
,→
content of visual stimuli. In this paper, we present a novel visual decoding
,→
pipeline that, in addition to recovering the content, emphasizes the
,→
reconstruction of the style, such as color and texture, of images viewed by the
,→
subject. Unlike previous methods, this ``style-based'' approach learns in the CLIP
,→
spaces of image and text separately, facilitating a more nuanced extraction of
,→
information from EEG signals. We also use captions for text alignment simpler than
,→
previously employed, which we find work better. Both quantitative and qualitative
,→
evaluations show that our method better preserves the style of visual stimuli and
,→
extracts more fine-grained semantic information from neural signals. Notably, it
,→
achieves significant improvements in quantitative results and sets a new
,→
state-of-the-art on the popular Brain2Image dataset.
,→
</example 1>

<example 2>
Background Paper 1:
Title: CrypTen: Secure Multi-Party Computation Meets Machine Learning

24

PreScience: A Benchmark for Forecasting Scientific Contributions
Abstract: Secure multi-party computation (MPC) allows parties to perform computations
,→
on data while keeping that data private. This capability has great potential for
,→
machine-learning applications: it facilitates training of machine-learning models
,→
on private data sets owned by different parties, evaluation of one party's private
,→
model using another party's private data, etc. Although a range of studies
implement machine-learning models via secure MPC, such implementations are not yet
,→
,→
mainstream. Adoption of secure MPC is hampered by the absence of flexible software
,→
frameworks that"speak the language"of machine-learning researchers and engineers.
,→
To foster adoption of secure MPC in machine learning, we present CrypTen: a
,→
software framework that exposes popular secure MPC primitives via abstractions
,→
that are common in modern machine-learning frameworks, such as tensor
,→
computations, automatic differentiation, and modular neural networks. This paper
,→
describes the design of CrypTen and measure its performance on state-of-the-art
,→
models for text classification, speech recognition, and image classification. Our
,→
benchmarks show that CrypTen's GPU support and high-performance communication
,→
between (an arbitrary number of) parties allows it to perform efficient private
,→
evaluation of modern machine-learning models under a semi-honest threat model. For
,→
example, two parties using CrypTen can securely predict phonemes in speech
,→
recordings using Wav2Letter faster than real-time. We hope that CrypTen will spur
adoption of secure MPC in the machine-learning community.
,→
Predicted Followup Paper:
Title: Low-Latency Privacy-Preserving Deep Learning Design via Secure MPC
Abstract: Secure multi-party computation (MPC) facilitates privacy-preserving
computation between multiple parties without leaking private information. While
,→
most secure deep learning techniques utilize MPC operations to achieve feasible
,→
privacy-preserving machine learning on downstream tasks, the overhead of the
,→
computation and communication still hampers their practical application. This work
,→
proposes a low-latency secret-sharing-based MPC design that reduces unnecessary
,→
communication rounds during the execution of MPC protocols. We also present a
,→
method for improving the computation of commonly used nonlinear functions in deep
,→
learning by integrating multivariate multiplication and coalescing different
,→
packets into one to maximize network utilization. Our experimental results
,→
indicate that our method is effective in a variety of settings, with a speedup in
,→
communication latency of $10\sim20\%$.
,→
</example 2>

<example 3>
Background Paper 1:
Title: Retrieval-Augmented Generation for Large Language Models: A Survey
Abstract: Large Language Models (LLMs) demonstrate significant capabilities but face
,→
challenges such as hallucination, outdated knowledge, and non-transparent,
,→
untraceable reasoning processes. Augmented Generation (RAG) has emerged as a
promising solution to these issues by incorporating real-time data from external
,→
,→
databases into LLM responses. This enhances the accuracy and credibility of the
,→
models, particularly for knowledge-intensive tasks, and allows for continuous
,→
knowledge updates and integration of domain-specific information. RAG
,→
synergistically merges LLMs' intrinsic knowledge with the vast, dynamic
,→
repositories of external databases. This survey paper provides an in-depth
,→
analysis of the evolution of RAG, focusing on three key paradigms: Naive RAG,
,→
Advanced RAG, and Modular RAG. It methodically examines the three fundamental
,→
components of RAG systems: the retriever, the generator, and the augmentation
,→
methods, underscoring the cutting-edge technologies within each componenet.
,→
Additionally, the paper introduces novel metrics and capabilities for evaluating
,→
RAG models, as well as the most recent evaluation framework. Finally, the paper
,→
outlines future research directions from three perspectives: future
,→
challenges,modality extension,and the development of the RAG technical stack and
ecosystem.
,→
Background Paper 2:
Title: From Local to Global: A Graph RAG Approach to Query-Focused Summarization

25

PreScience: A Benchmark for Forecasting Scientific Contributions
Abstract: The use of retrieval-augmented generation (RAG) to retrieve relevant
,→
information from an external knowledge source enables large language models (LLMs)
,→
to answer questions over private and/or previously unseen document collections.
,→
However, RAG fails on global questions directed at an entire text corpus, such
,→
as"What are the main themes in the dataset?", since this is inherently a
query-focused summarization (QFS) task, rather than an explicit retrieval task.
,→
,→
Prior QFS methods, meanwhile, fail to scale to the quantities of text indexed by
,→
typical RAG systems. To combine the strengths of these contrasting methods, we
,→
propose a Graph RAG approach to question answering over private text corpora that
,→
scales with both the generality of user questions and the quantity of source text
,→
to be indexed. Our approach uses an LLM to build a graph-based text index in two
,→
stages: first to derive an entity knowledge graph from the source documents, then
,→
to pregenerate community summaries for all groups of closely-related entities.
,→
Given a question, each community summary is used to generate a partial response,
,→
before all partial responses are again summarized in a final response to the user.
,→
For a class of global sensemaking questions over datasets in the 1 million token
,→
range, we show that Graph RAG leads to substantial improvements over a naive RAG
,→
baseline for both the comprehensiveness and diversity of generated answers. An
,→
open-source, Python-based implementation of both global and local Graph RAG
approaches is forthcoming at https://aka.ms/graphrag.
,→
Predicted Followup Paper:
Title: LightRAG: Simple and Fast Retrieval-Augmented Generation
Abstract: Retrieval-Augmented Generation (RAG) systems enhance large language models
(LLMs) by integrating external knowledge sources, enabling more accurate and
,→
contextually relevant responses tailored to user needs. However, existing RAG
,→
systems have significant limitations, including reliance on flat data
,→
representations and inadequate contextual awareness, which can lead to fragmented
,→
answers that fail to capture complex inter-dependencies. To address these
,→
challenges, we propose LightRAG, which incorporates graph structures into text
,→
indexing and retrieval processes. This innovative framework employs a dual-level
,→
retrieval system that enhances comprehensive information retrieval from both
,→
low-level and high-level knowledge discovery. Additionally, the integration of
,→
graph structures with vector representations facilitates efficient retrieval of
,→
related entities and their relationships, significantly improving response times
,→
while maintaining contextual relevance. This capability is further enhanced by an
,→
incremental update algorithm that ensures the timely integration of new data,
,→
allowing the system to remain effective and responsive in rapidly changing data
,→
environments. Extensive experimental validation demonstrates considerable
,→
improvements in retrieval accuracy and efficiency compared to existing approaches.
,→
We have made our LightRAG open-source and available at the link:
,→
https://github.com/HKUDS/LightRAG.
,→
</example 3>

You need to first think through how exactly you want to combine the background papers
,→
(i.e. which aspects from these papers will be used in the followup work) before
,→
making each prediction. This will constitute the 'reasoning' part of your
,→
response. Only then will you make your prediction of the title and abstract of the
,→
followup work.
When making your prediction, please use the output format shown below. Please don't
,→
use any newlines or whitespace that cause deviation from this format.
Reasoning: ...
Title: ...
Abstract: ...

26

PreScience: A Benchmark for Forecasting Scientific Contributions
EXTREMELY IMPORTANT: Please make sure to output all 3 fields: Reasoning, Title and
,→
Abstract in that order before ending your response. RESPONSES WITHOUT THE Title
AND Abstract FIELDS WILL BE CONSIDERED INVALID. YOU MUST OUTPUT ALL THREE FIELDS
,→
,→
IN THE SAME RESPONSE SEPERATED BY NEWLINES. DO NOT SPLIT UP FIELDS BETWEEN
,→
RESPONSES.

27

PreScience: A Benchmark for Forecasting Scientific Contributions

E. Impact Prediction
E.1. Further Task Analyses
Figure 9a plots the predictions of the XGBoost regressor trained using the full set of features described in Section 4.4.
We find that the model exhibits clear heteroscedasticity: variance in prediction error increases with citation magnitude,
indicating that highly cited papers are systematically harder to predict than low-impact papers. Figure 9b summarizes feature
attributions via SHAP (Lundberg & Lee, 2017) for the XGBoost regressor trained on Bibliometrics.

(a) Predictions show substantial heterscedasticity.

(b) SHAP values for the XGBoost regressor trained over only
author- and key-reference-related numerical metadata features
(Bibliometrics).

Figure 9. Impact Prediction

28

PreScience: A Benchmark for Forecasting Scientific Contributions

F. Corpus Generation
F.1. Further Task Analyses
We define the “effective” number of authors/cited papers surfaced during simulation as the exponentiation of the entropy
of the cumulative distribution of author/cited papers that are attached to target papers. We compute these cumulative
distributions over the target papers written/synthesized during the simulation period (or equivalently, the PreScience test
period). We employ retrieval pool subsampling to remove systemic biases due to discrepancies between natural and synthetic
corpus sizes. Figure 10 shows that our simulations (Section 4.5) systematically surface more diverse collections of authors
and prior work than truly occur in real-world research.

(a) Authors surfaced by the synthetic rollouts are more diverse
than the corresponding natural authors.

(b) Prior work surfaced during synthetic rollouts is more diverse
than by natural papers from the same time period.

Figure 10. Diversity of Authors and Prior work surfaced during corpus generation.

F.2. Discussion
Realistically simulating corpus rollouts can be difficult. Even assuming access to models that can perform individual
tasks well, it can be challenging to use them to generate realistic corpora. Choices made while designing the procedure
that utilizes these models for multi-turn corpus roll-outs can have unintended consequences that bias corpus statistics. For
example, Figure 11 shows the distribution of primary arXiv topics of Natural and Synthetic13 papers corresponding to this
period. Real-world research shows much more seasonal variation in the distribution over papers published year-round
than the synthetic corpus. This arises from the fact that our simulation uniformly and independently randomly selects seed
authors from the PreScience dataset for each synthesized paper whereas certain seed authors may be more likely to publish
their work at certain times of the year than others due to external circumstances like venue deadlines or academic schedules.
Individual statistics computed over a generated corpus can be misleading. It can be difficult to accurately measure
the quality of a synthetic corpus. For instance, in Figure 12, we measure the fraction of target papers from the natural and
simulated corpora that contain at least one key reference that cites another of the same target paper’s key references. Although
it appears that this coefficient approaches that from the natural corpus as the simulation proceeds, an observation that can be
mistaken for implying that the simulated papers’ citation patterns become more realistic as simulation proceeds–we find
that its upward slope is due to another factor: Synthetic papers that enter the corpus can connect two previously disparate
papers. However, in the event that these baselines experience a type of mode-collapse, tending to predict these same citations
unnaturally often, the local clustering coefficient would continue to increase as the simulation proceeds. Hence, such a
phenomenon that skews the synthetic corpus away from the natural corpus would counterintuitively have the effect of
causing this statistic to trend in the “correct” direction.
13

We use a classifier with ∼ 70% accuracy on a held-out set from the train period to predict the topics of synthesized papers.

29

PreScience: A Benchmark for Forecasting Scientific Contributions

Figure 11. Primary arXiv topics of ground truth (natural) and simulated (synthetic) papers. Natural papers show significant seasonal
variation while synthetic papers do not.

Figure 12. Local clustering coefficient (i.e. the fraction of pairs of key references of the target paper that cite another of its key references)

G. Selecting a Corpus Generation Metric
G.1. FacetScore
Unsatisfied with existing measures of textual similarity (ROUGE-L, BERTScore (Zhang et al., 2019), ASPIRE-OT (Mysore
et al., 2022)), we developed a similarity metric called FacetScore based on the work of Radensky et al. (2024). Intended
to assist in scientific ideation, Scideator (Radensky et al., 2024) introduced the representation of a scientific advance as a
combination of several facets: purpose, mechanism, and evaluation. We further added a notion of the scientific contribution
type (Pramanick et al., 2024) (an artifact, knowledge, or better understanding) into this collection of facets. Once FacetScore
extracts each of these fields from the provided pair of title-abstracts, it prompts an LLM to score the similarity between
corresponding pairs of facets on a five-point scale. Finally, FacetScore returns the average of these facet-level similarity
scores as the overall similarity score between the two provided papers.
However, we opted to omit FacetScore computations from out later experiments since we found that LACERScore judgements correlate significantly better with human judgements (Figure 13).
30

PreScience: A Benchmark for Forecasting Scientific Contributions

G.2. LACERScore
In our experiments, existing automatic textual similarity metrics (ROUGE-L, BERTScore (Zhang et al., 2019), ASPIREOT (Mysore et al., 2022), retrieval-based mean reciprocal rank (MRR), etc.) exhibited limited dynamic range: substantially
different generated title-abstract pairs received similar scores, and it was often unclear or arbitrary, the degree of dissimilarity
that yields a score at the lower extreme of the scale. To address this, we define LACERScore, an LLM-as-judge metric
explicitly calibrated to a 1-10 semantic alignment scale using automatically constructed demonstrations.
Instead of relying on human-annotated similarity judgments, we generate calibration examples by interpolating between
two intuitive endpoints. For each demonstration sequence, a key reference whose abstract lies at the 50th percentile14 of
n-gram overlap with the target defines score 1, representing related but clearly distinct prior work. A paraphrase of the target
abstract defines score 10, representing near-semantic equivalence.
We then prompt (Appendix G.2.2) GPT-5 to generate intermediate title–abstract pairs for scores 2 through 9 by gradually
modifying one semantic aspect at a time (e.g., contribution type, model architecture, or task domain), forming a smooth
transition between these endpoints. Five such interpolation sequences are included as few-shot examples in the scoring
prompt (Appendix G.2.1), which the judge model uses to assign calibrated 1–10 scores to new generation–reference pairs.
This approach anchors the LACERScore scale in concrete, task-specific contrasts while avoiding the cost of manual
annotation, while also providing a well-defined and sensitive measure of conceptual alignment in scientific contributions.
G.2.1. LACERS CORE J UDGE P ROMPT
LACERScore Judge Prompt
You will be given a pair of title-abstracts Reference and Generated. Your task is to
assign a score from 1-10 measuring how similar the Generated is to the Reference
,→
title-abstract where 1 represents the lowest similarity score and 10 represents
,→
the highest.
,→
Here are some examples of References along with 10 Generations each corresponding to
,→
scores 1-10.
Reference A:
Intelligent Urban Surveillance in India: Real-Time Recognition of Individual
,→
Attributes
This study introduces a smart surveillance system for Indian cities that performs
real-time identification and analysis of people's attributes. Leveraging advanced
,→
artificial intelligence and machine learning, the system recognizes features such
,→
as upper-body color, clothing, accessories, headgear, and so on, and analyzes
,→
behavior using camera feeds installed throughout the city.
,→
Generations:
PyTorch: A High-Performance Deep Learning Library with an Imperative, Pythonic Design
Deep learning frameworks have often emphasized either ease of use or performance, but
,→
seldom both. PyTorch demonstrates that these aims can be jointly achieved: it
provides an imperative, Python-native programming model that treats code as the
,→
,→
model, simplifies debugging, and harmonizes with popular scientific computing
,→
libraries, while remaining efficient and supporting hardware accelerators such as
,→
GPUs. In this work, we articulate the principles that guided PyTorch's
,→
implementation and show how they manifest in its architecture. We underscore that
,→
every part of PyTorch is an ordinary Python program under the user's full control.
,→
We also describe how a careful, pragmatic realization of the runtime's key
,→
components enables them to interoperate to deliver compelling performance.
,→
Finally, we present evidence of the efficiency of individual subsystems and the
,→
overall speed of PyTorch on several common benchmarks.
Score: 1

14
We also experimented with using 25th percentile, 75th percentile, and randomly chosen key references to define the minimum
LACERScore. We found that this choice does not meaningfully change its judgements.

31

PreScience: A Benchmark for Forecasting Scientific Contributions
PyTorch-Stream: Eager, High-Throughput Extensions for Real-Time Vision and Video
We present PyTorch-Stream, a set of runtime and library extensions that bring
,→
low-latency, multi-stream video analytics to PyTorch while preserving its
,→
imperative programming model. PyTorch-Stream introduces asynchronous camera
,→
ingest, zero-copy decoding, fused preprocessing ops, and CUDA graph capture to
,→
minimize per-frame overhead. We describe design decisions that retain Pythonic
,→
control flow yet enable ahead-of-time export of hot paths for steady-state
,→
performance. Across common video tasks (object detection, tracking-by-detection,
,→
and attribute classification), PyTorch-Stream reduces end-to-end latency by 30-55%
Score: 2
PyTorch-PersonAttr: A Reproducible Toolkit for Person Attribute Recognition in
,→
Surveillance Video
We release PyTorch-PersonAttr, a modular toolkit for training, evaluating, and
,→
deploying person attribute recognition models using the PyTorch-Stream runtime.
,→
The toolkit standardizes data adapters (e.g., RAP, PA-100k, PETA), implements
,→
strong CNN and hybrid CNN-Transformer baselines, and provides consistent
,→
evaluation protocols for multi-label classification (e.g., apparel type, color,
,→
accessories). We detail reference training recipes, mixed-precision/compiled
,→
execution for real-time inference, and uncertainty calibration methods for
,→
attribute outputs. Experiments show state-of-the-art or competitive results on
,→
public benchmarks and >60 FPS inference for 720p streams on a single GPU.
Score: 3
CityAttr: A Benchmark for Fine-Grained Person Attribute Recognition in Urban Camera
,→
Feeds
We introduce CityAttr, a benchmark targeting fine-grained person attributes in urban
environments, with 250k annotated person crops spanning diverse weather, lighting,
,→
and camera viewpoints. CityAttr adds difficult classes pertinent to city
,→
operations (upper-body color under motion blur, reflective accessories, safety
,→
gear) and defines standardized train/val/test splits and occlusion strata. We
,→
provide strong PyTorch-PersonAttr baselines, error taxonomies, and fairness
,→
analyses across scene contexts. Results highlight failure modes in crowded scenes
,→
and under low light, motivating temporal modeling and domain adaptation for
,→
real-time deployments.
,→
Score: 4
TorchStream City: A Low-Latency, Multi-Camera Video Analytics System for Urban
,→
Attribute Tagging
Building on PyTorch-Stream and CityAttr, we present TorchStream City, a reference
system for city-scale, real-time attribute tagging. The system integrates
,→
multi-camera ingest, on-GPU batching/scheduling, online multi-object tracking, and
,→
temporal ensembling for stable attribute estimates. A hybrid eager-compiled
,→
execution path allows imperative control for orchestration while compiling
,→
per-operator graphs for steady-state throughput. Deployed on traffic and
,→
pedestrian cameras, TorchStream City sustains 25-30 FPS per stream across 32 feeds
,→
on two GPUs, with <200 ms median latency for detection, tracking, and attribute
,→
,→
tagging, and provides APIs for downstream behavior analytics.
Score: 5
EdgeTorch-Attr: Efficient Person Attribute Recognition on Embedded and On-Camera
,→
Accelerators
We propose EdgeTorch-Attr, an optimization stack enabling person attribute recognition
,→
on edge devices. Techniques include compound scaling, quantization-aware training,
,→
structured pruning, knowledge distillation from server-grade models, and
,→
deployment via PyTorch 2 AOT compilation and TensorRT backends. We co-design the
,→
streaming pipeline to overlap decode, preproc, and inference on limited memory
,→
budgets. Field trials on NVIDIA Jetson- and VPU-class devices show 3-5x energy
,→
efficiency gains while maintaining >90%
Score: 6
IndAttr: Culturally-Aware Attribute Recognition for Indian Urban Scenes via
,→
Domain-Adaptive Temporal Transformers

32

PreScience: A Benchmark for Forecasting Scientific Contributions
We present IndAttr, a domain-adaptive model suite tailored to Indian urban video
,→
feeds. IndAttr augments attribute taxonomies to include culturally salient apparel
and accessories (e.g., kurta, sari, dupatta, school uniforms, turbans, safety
,→
,→
vests), and leverages temporal Vision Transformers with cross-frame attention for
,→
stability under occlusion and crowding. We introduce unsupervised domain
,→
adaptation from CityAttr using camera-style augmentation and self-training, plus
,→
limited expert-labeled Indian samples collected under ethical protocols. IndAttr
,→
improves mAP by 7.8 points over generic baselines on Indian pilot datasets while
,→
sustaining edge-ready throughput via distillation to compact temporal backbones.
Score: 7
PriCity-Attr: Privacy-Preserving, Federated Multi-Camera Attribute Analytics for
,→
Indian Smart Cities
We develop PriCity-Attr, a privacy-preserving training and deployment framework for
,→
multi-camera attribute analytics in Indian cities. The system performs on-device
,→
anonymization (face/body blurring for raw frames), stores only attribute and
,→
trajectory metadata, and trains models via cross-ward federated learning with
,→
secure aggregation and differential privacy accounting. We include governance
,→
hooks (policy-driven retention, audit logs) and human-in-the-loop tools for bias
,→
auditing. In a city pilot across 120 cameras, PriCity-Attr maintains IndAttr-level
,→
accuracy, reduces cross-site generalization error by 25%
Score: 8
Real-Time Indian Urban Monitoring: City-Scale Deployment of Attribute and Behavior
,→
Analytics
We present a production-grade, city-scale deployment that integrates IndAttr and
PriCity-Attr into a unified smart monitoring platform for Indian metros. The
,→
system performs real-time identification of salient person attributes (upper-body
,→
color, apparel type, accessories, headgear) and stabilizes outputs via temporal
,→
modeling to feed behavior analytics (zone occupancy, queueing, safety-gear
,→
compliance). An edge-cloud architecture supports heterogeneous cameras, with
,→
resilient scheduling, adaptive bitrate, and failover. We report month-long
,→
operations over 500+ feeds, covering throughput, latency, availability, and model
,→
drift monitoring, demonstrating actionable, privacy-aware analytics for urban
,→
management at scale.
,→
Score: 9
Intelligent Urban Surveillance in India: Real-Time Recognition of Individual
,→
Attributes
This study introduces a smart surveillance system for Indian cities that performs
real-time identification and analysis of people's attributes. Leveraging advanced
,→
artificial intelligence and machine learning, the system recognizes features such
,→
as upper-body color, clothing, accessories, headgear, and so on, and analyzes
,→
behavior using camera feeds installed throughout the city.
,→
Score: 10
Reference B:
Ada-Instruct: Retooling Instruction Generation for Complex Reasoning
Augmenting instructions is critical for unlocking the full potential of large language
,→
models (LLMs) on downstream tasks. Current Self-Instruct approaches largely
,→
fabricate new instructions from a small seed set via in-context learning. Our
,→
analysis reveals a key limitation of this paradigm: even with GPT4o, Self-Instruct
,→
fails to produce complex instructions of length 100 or more, which are necessary
,→
for demanding tasks such as code completion. To overcome this, we observe that
,→
fine-tuning open source LLMs with only ten examples can yield complex instructions
that preserve distributional consistency for complex reasoning tasks. We introduce
,→
,→
Ada-Instruct, an adaptive instruction generator obtained through fine-tuning. We
,→
validate Ada-Instruct empirically across different applications, and the results
,→
demonstrate its ability to generate long, intricate, and distributionally
,→
consistent instructions.
Generations:
Evaluating Mathematical Problem Solving Using the MATH Dataset

33

PreScience: A Benchmark for Forecasting Scientific Contributions
Many forms of intellectual work depend on mathematical problem solving, yet computers
,→
still struggle with this capability. To assess this skill in machine learning
,→
systems, we present MATH, a dataset of 12,500 difficult competition mathematics
,→
problems. Each problem includes a complete step-by-step solution, enabling models
,→
to be trained to produce answer derivations and explanations. To support future
,→
research and improve accuracy on MATH, we additionally release a large auxiliary
,→
pretraining dataset aimed at teaching models the fundamentals of mathematics.
,→
While we are able to raise accuracy on MATH, our results show that performance
,→
remains relatively low, even with extremely large Transformer models. Moreover, if
,→
current scaling trends persist, simply expanding compute budgets and model
,→
parameter counts appears impractical for achieving strong mathematical reasoning.
,→
Although scaling Transformers is largely solving most other text-based tasks, it
,→
is not currently solving MATH. Substantive progress on mathematical problem
,→
solving will likely require new algorithmic advances from the broader research
,→
community.
Score: 1
Fine-Grained Evaluation of Mathematical Reasoning with Stepwise Derivations
We revisit evaluation on competition mathematics by exploiting the full step-by-step
solutions accompanying problems. Beyond final-answer accuracy, we introduce
,→
derivation-aware metrics that align a model's generated reasoning with reference
,→
solutions via step matching, dependency agreement, and algebraic edit distance. We
,→
release standardized evaluation scripts and human-verified annotations for a
,→
subset of the MATH dataset, enabling assessment of intermediate reasoning quality
,→
and error localization. Our analysis across model scales shows that improvements
,→
in final accuracy often mask brittle derivations and shortcut patterns. We find
,→
that models benefiting from chain-of-thought prompting still diverge significantly
,→
from canonical derivations, suggesting the need for training signals that target
,→
the structure and granularity of mathematical reasoning rather than only end
,→
answers.
,→
Score: 2
AutoHint-MATH: Augmenting Competition Problems with Model-Generated Hints and Subgoals
To bridge the gap between final-answer evaluation and robust derivations, we introduce
AutoHint-MATH, a data augmentation pipeline that generates targeted hints,
,→
subgoals, and intermediate checks for competition-level math problems. Using large
,→
language models guided by our stepwise metrics, we produce pedagogically
,→
structured scaffolds that highlight crucial transformations and decision points.
,→
We curate 60k high-quality hint-problem-solution triplets and show that training
,→
with these augmentations yields consistent gains in both final answers and
,→
derivation alignment on MATH. Compared to vanilla chain-of-thought prompting,
,→
AutoHint-MATH improves sample efficiency and reduces off-track reasoning,
,→
indicating that explicit scaffolding can better shape model search through complex
,→
solution spaces.
,→
Score: 3
InstructMATH: Instruction-Tuning for Step-by-Step Mathematical Problem Solving
We move from passive scaffolds to active task framing by introducing InstructMATH, a
,→
collection of instruction-problem-solution triples designed to instruction-tune
,→
models for mathematical reasoning. Instructions specify goals, permissible
,→
operations, and verification strategies, teaching models how to structure
,→
derivations before generating them. We compile 25k diverse instruction templates
,→
spanning algebra, geometry, and number theory, and show that instruction-tuned
,→
models outperform hint-augmented baselines on MATH under both few-shot and
,→
zero-shot settings. Analyses indicate that explicit procedural instructions reduce
,→
hallucinated steps and improve adherence to algebraic invariants. Our results
,→
suggest instruction-tuning is a promising path to controllable, reliable
,→
mathematical reasoning.
Score: 4
ReasonBench: A Multi-Domain Corpus of Instruction-Driven Problems with Worked
,→
Solutions

34

PreScience: A Benchmark for Forecasting Scientific Contributions
To test whether instruction-tuned reasoning transfers beyond mathematics, we create
,→
ReasonBench, a multi-domain corpus covering competition math, physics word
,→
problems, logic puzzles, and algorithmic thinking tasks, each paired with
,→
domain-specific instructions and worked solutions. We design a shared schema for
,→
instructions (goal, constraints, permitted tools, validation) and provide
cross-domain transfer splits. Instruction-tuned models trained on ReasonBench
,→
,→
improve on out-of-domain reasoning tasks, especially when instructions emphasize
,→
decomposition and verification. However, performance plateaus on tasks requiring
,→
long, intricate directives (e.g., multi-function code synthesis, multi-lemma
,→
proofs), motivating a closer study of instruction complexity and its role in
,→
reasoning.
Score: 5
On the Complexity of Instructions for Complex Reasoning Tasks
We systematically measure how instruction complexity-length, structural depth, and
,→
constraint density-affects performance on challenging tasks such as proof
,→
sketching and code completion. We find that instructions longer than ˜100 tokens
,→
with nested constraints substantially improve reliability in multi-step reasoning,
,→
but current self-instruction pipelines rarely produce such long, structured
,→
directives and often drift from the target task's distribution. Using ReasonBench
,→
extensions for coding and formal reasoning, we quantify this mismatch and show
,→
that in-context self-instruct deteriorates instruction quality as length
,→
increases. These results highlight a bottleneck: generating long, distributionally
,→
faithful instructions is essential for unlocking complex reasoning, yet existing
automatic pipelines fall short.
,→
Score: 6
Scaffold-Instruct: Hierarchical Self-Instruct for Long-Form, Structured Prompts
We propose Scaffold-Instruct, a hierarchical self-instruction framework that builds
long-form instructions via iterative decomposition: a planner drafts high-level
,→
goals, a refiner injects constraints and verification steps, and a validator
,→
enforces structural templates. Scaffold-Instruct increases instruction length and
,→
structural depth while improving internal consistency over standard self-instruct.
,→
On math, logic, and code tasks, models trained with Scaffold-Instruct show better
,→
adherence to multi-step procedures and fewer dead ends. Nevertheless, the approach
,→
is compute-intensive, relies on strong planners, and still exhibits distributional
,→
drift on specialized domains like code completion. These limitations motivate
,→
moving from purely in-context pipelines toward trainable instruction generators.
,→
Score: 7
Few-Shot Fine-Tuned Instruction Generators for Mathematical and Program Reasoning
We introduce a trainable alternative to hierarchical self-instruct: fine-tuning a
,→
compact open-source LLM to act as an instruction generator using a small curated
,→
set (20-50) of long, structured seed instructions per domain. The resulting
,→
generator produces instructions that are longer, more constraint-aware, and more
,→
distributionally aligned with math and coding datasets than in-context
,→
self-instruct. When used to create training corpora, these instructions yield
,→
larger gains on multi-step reasoning and code completion benchmarks than
,→
Scaffold-Instruct, at a fraction of the cost. Ablations show that even minimal
,→
fine-tuning stabilizes long-instruction formatting and reduces semantic drift,
,→
suggesting few-shot fine-tuned generators are a scalable path forward.
Score: 8
AdaGen: Adaptive Few-Shot Instruction Generators for Complex Reasoning

35

PreScience: A Benchmark for Forecasting Scientific Contributions
Building on few-shot fine-tuned generators, we present AdaGen, an adaptive instruction
,→
generation framework that (1) fine-tunes open-source LLMs with as few as ten
,→
carefully selected seed instructions per domain, and (2) adaptively controls
,→
length, constraint density, and style to match target-task distributions. AdaGen
,→
automatically diagnoses gaps in coverage using lightweight discriminators and
,→
iteratively steers generation to maintain distributional fidelity. Across
,→
mathematical reasoning and code completion, AdaGen produces long (>=100 tokens),
,→
structurally rich instructions that lead to consistent downstream gains over
,→
self-instruct and hierarchical baselines. These findings set the stage for
,→
general-purpose, low-budget instruction generators tailored to complex reasoning
,→
tasks.
Score: 9
Ada-Instruct: Retooling Instruction Generation for Complex Reasoning
Augmenting instructions is critical for unlocking the full potential of large language
,→
models (LLMs) on downstream tasks. Current Self-Instruct approaches largely
,→
fabricate new instructions from a small seed set via in-context learning. Our
,→
analysis reveals a key limitation of this paradigm: even with GPT4o, Self-Instruct
,→
fails to produce complex instructions of length 100 or more, which are necessary
,→
for demanding tasks such as code completion. To overcome this, we observe that
,→
fine-tuning open source LLMs with only ten examples can yield complex instructions
that preserve distributional consistency for complex reasoning tasks. We introduce
,→
,→
Ada-Instruct, an adaptive instruction generator obtained through fine-tuning. We
,→
validate Ada-Instruct empirically across different applications, and the results
,→
demonstrate its ability to generate long, intricate, and distributionally
,→
consistent instructions.
Score: 10
Reference C:
Reinforced Self-Training (ReST) for Training Language Models
Reinforcement learning from human feedback (RLHF) can enhance the quality of large
language models' (LLMs) outputs by aligning them with human preferences. We
,→
present a straightforward alignment approach, inspired by growing-batch
,→
reinforcement learning (RL), which we call Reinforced Self-Training (ReST).
,→
Starting from an initial LLM policy, ReST constructs a dataset by sampling from
,→
that policy, and then uses offline RL algorithms on this data to further improve
,→
the policy. Because the training data are generated offline and can be reused,
,→
ReST is more efficient than standard online RLHF procedures. Although ReST is a
,→
general method applicable across generative learning scenarios, we center our
,→
investigation on machine translation. Our results demonstrate that ReST can
,→
substantially boost translation quality-according to both automated metrics and
,→
human evaluations on machine translation benchmarks-while being compute- and
,→
sample-efficient.
,→
Generations:
Algorithms for Proximal Policy Optimization
We present a new class of policy gradient algorithms for reinforcement learning that
,→
alternate between collecting data through environment interaction and maximizing a
,→
surrogate objective via stochastic gradient ascent. Unlike standard policy
,→
gradient approaches that make only one gradient update per data sample, we
,→
introduce a novel objective that enables multiple epochs of minibatch updates. The
,→
resulting methods, termed proximal policy optimization (PPO), capture some of the
,→
benefits of trust region policy optimization (TRPO) while being much simpler to
,→
implement, more general, and empirically exhibiting better sample complexity. We
,→
evaluate PPO on a set of benchmark tasks, including simulated robotic locomotion
,→
and Atari game playing, and show that it outperforms other online policy gradient
methods, achieving an overall favorable balance among sample complexity,
,→
,→
simplicity, and wall-time.
Score: 1
Proximal Policy Optimization with Replay: Enabling Stable Data Reuse in On-Policy RL

36

PreScience: A Benchmark for Forecasting Scientific Contributions
We extend proximal policy optimization (PPO) with a principled form of experience
,→
replay that increases sample efficiency while preserving stability. Our method
,→
augments the clipped surrogate objective with lightweight off-policy corrections
,→
using per-batch importance weights and a target network for value learning,
,→
enabling multiple epochs over mixed recent on-policy and near-on-policy samples.
,→
Across MuJoCo locomotion and Atari benchmarks, PPO+Replay achieves comparable or
,→
better asymptotic performance than PPO with 30-50%
Score: 2
Proximal Sequence Policy Optimization for Text Generation
We adapt proximal policy optimization to autoregressive sequence models for text
,→
generation. Our approach optimizes a clipped sequence-level policy gradient
,→
objective over Transformer language models, with rewards defined by task-specific
,→
automated metrics (e.g., ROUGE for summarization, BLEU for translation). We
,→
introduce a token-wise advantage estimator that stabilizes long-horizon credit
,→
assignment and a curriculum over sequence lengths. Experiments on CNN/DailyMail
,→
summarization and WMT14 En-De translation show consistent metric gains over
,→
supervised fine-tuning and REINFORCE baselines at comparable compute,
,→
demonstrating that PPO's trust-region-like updates transfer effectively to
,→
discrete text generation.
Score: 3
KL-Regularized Proximal Optimization for Controlled Text Generation
We propose a KL-regularized variant of proximal optimization for sequence models that
constrains updates relative to a supervised reference model. The objective
,→
augments PPO's clipped surrogate with an adaptive KL penalty against the reference
,→
policy, yielding stable improvements while preserving fluency. We instantiate
,→
rewards from automated metrics and task-specific constraints (length, toxicity
,→
filters), and introduce a reference-anchored value function to reduce variance. On
,→
summarization and translation, KL-Prox achieves higher ROUGE/BLEU and better
,→
human-rated coherence than metric-only PPO, highlighting the benefit of explicit
,→
distributional control for language generation.
,→
Score: 4
Preference-Guided Proximal Optimization: Online RLHF for Sequence Models
We integrate human preference learning with proximal policy optimization for language
generation. A reward model is trained from pairwise human comparisons and used to
,→
guide KL-regularized PPO updates of a Transformer policy anchored to a supervised
,→
reference. We interleave data collection (sampling candidate texts), preference
,→
labeling, reward model updates, and policy improvement. On summarization and
,→
open-ended generation, our method improves human preference win-rates over
,→
supervised baselines and metric-optimized PPO, while maintaining stability via
,→
adaptive KL and early stopping. Results demonstrate that online RLHF can be
,→
realized with simple proximal updates and modest human annotation.
,→
Score: 5
Growing-Batch Preference Optimization: Bridging Online RLHF and Offline RL for LMs
We introduce a growing-batch training regime for preference-optimized language models
,→
that alternates between short bursts of sample collection and extended offline
,→
optimization. Candidate texts are generated from the current policy, scored by a
,→
learned preference model, and stored in a replay buffer. We then apply offline
,→
RL-style updates-advantage-weighted likelihood with conservative clipping and
,→
value targets fit by fitted policy evaluation-over the accumulated batch, with
,→
occasional refresh of the data. Compared to purely online PPO-based RLHF,
,→
Growing-Batch PO reduces the number of preference queries and environment
,→
interactions while achieving similar or better human preference win-rates on
,→
summarization and dialogue.
Score: 6
Self-Generated Corpora for Batch RLHF: Offline Advantage Optimization of LMs

37

PreScience: A Benchmark for Forecasting Scientific Contributions
We present a purely offline procedure for aligning language models using
,→
self-generated datasets. Starting from a supervised policy, we sample candidate
,→
continuations, score them with a learned preference model, and construct a static
,→
training set. We then perform multiple epochs of offline reinforcement learning
,→
using advantage-weighted regression with KL regularization to the reference,
without further online sampling during optimization. This self-training loop can
,→
,→
be repeated to grow the dataset. On summarization and translation, our batch RLHF
,→
approach matches or exceeds online PPO-based RLHF in human and automatic metrics
,→
while reducing compute and annotation overhead via data reuse.
Score: 7
Offline Reinforcement Learning for Machine Translation via Self-Generated Batches
Focusing on machine translation, we instantiate an offline RL framework that improves
,→
a Transformer translator using only self-generated candidate translations and
,→
offline optimization. We generate n-best lists from the current model, score them
,→
with a mixture of automatic metrics (BLEU, COMET) and a lightweight preference
,→
model, and train with KL-regularized advantage-weighted updates over the static
,→
pool. Periodic regeneration expands coverage, but all policy learning is performed
,→
offline, enabling aggressive data reuse. On WMT benchmarks, our method delivers
,→
substantial BLEU/COMET gains over supervised fine-tuning and online policy
,→
gradient methods at lower compute, with humans preferring our outputs for adequacy
,→
and fluency.
Score: 8
Preference-Scored Self-Training with Offline RL for LLM Translators
We propose a simple self-training algorithm for large language model (LLM) translators
that combines dataset generation by the model with offline reinforcement learning.
,→
Given an initial LLM policy and a reference model, we produce candidate
,→
translations, score them using a learned preference model (optionally blended with
,→
automated metrics), and optimize the policy offline with KL-regularized
,→
advantage-weighted regression and value fitting. The process can be repeated in a
,→
growing-batch fashion to refresh the static dataset while retaining offline
,→
updates. Applied to WMT machine translation, this approach yields sizable
,→
improvements in BLEU/COMET and human evaluations relative to supervised
,→
fine-tuning and online RLHF, with favorable compute and sample efficiency.
,→
Score: 9
Reinforced Self-Training (ReST) for Training Language Models
Reinforcement learning from human feedback (RLHF) can enhance the quality of large
,→
language models' (LLMs) outputs by aligning them with human preferences. We
,→
present a straightforward alignment approach, inspired by growing-batch
,→
reinforcement learning (RL), which we call Reinforced Self-Training (ReST).
Starting from an initial LLM policy, ReST constructs a dataset by sampling from
,→
,→
that policy, and then uses offline RL algorithms on this data to further improve
,→
the policy. Because the training data are generated offline and can be reused,
,→
ReST is more efficient than standard online RLHF procedures. Although ReST is a
,→
general method applicable across generative learning scenarios, we center our
,→
investigation on machine translation. Our results demonstrate that ReST can
,→
substantially boost translation quality-according to both automated metrics and
,→
human evaluations on machine translation benchmarks-while being compute- and
,→
sample-efficient.
Score: 10
Reference D:
MAPO: Boosting Multilingual Reasoning by Casting Cross-Language Alignment as
,→
Preference Optimization

38

PreScience: A Benchmark for Forecasting Scientific Contributions
Although reasoning is often regarded as language-independent, current LLMs display
,→
uneven reasoning performance across languages; for instance, a dominant language
,→
like English typically outperforms others due to imbalanced multilingual training
,→
data. To strengthen reasoning in non-dominant languages, we introduce a
,→
Multilingual-Alignment-as-Preference Optimization framework (MAPO) that aligns the
reasoning processes in other languages with those of the dominant language. In
,→
,→
particular, we leverage an off-the-shelf translation model to enforce consistency
,→
between answers in non-dominant and dominant languages, and treat this consistency
,→
as a preference signal for optimization with methods such as Direct Preference
,→
Optimization (DPO) or Proximal Policy Optimization (PPO). Empirically, MAPO
,→
reliably delivers substantial improvements in multilingual reasoning across
,→
various models on three benchmarks (MSVAMP +16.2%
Generations:
Advancing Cross-Lingual Mathematical Reasoning: Empirical Findings and Lessons Learned
Prior work has largely emphasized building strong language models (LLMs) for
,→
mathematical reasoning in single-language settings, with limited attention to
,→
maintaining performance across multiple languages. To close this gap, we initiate
,→
the exploration and training of robust Multilingual Math Reasoning (xMR) LLMs.
,→
Using translation, we assemble the first multilingual instruction dataset for math
,→
reasoning, MGSM8KInstruct, spanning ten languages, thereby mitigating training
,→
data scarcity for xMR tasks. Leveraging this corpus, we introduce several training
,→
strategies to construct a family of xMR LLMs, dubbed MathOctopus, which
,→
consistently outperform typical open-source LLMs and surpass ChatGPT in few-shot
setups. In particular, MathOctopus-13B attains 47.6%
,→
Score: 1
Consistency-Regularized SFT for Multilingual Mathematical Reasoning
Building on multilingual instruction tuning for mathematical reasoning, we investigate
whether explicitly encouraging cross-lingual agreement can further improve xMR
,→
LLMs. Using the MGSM8KInstruct corpus, we construct parallel
,→
problem-solution-rationale tuples across ten languages via high-quality
,→
translation. We introduce a consistency-regularized supervised fine-tuning
,→
(CR-SFT) objective that augments standard SFT with two auxiliary signals: (1)
,→
answer-level agreement across parallel languages, enforced via a differentiable
,→
dual-decoding consistency loss; and (2) rationale-level agreement, measured by
,→
semantic similarity between chain-of-thought embeddings. Fine-tuning 7B-13B models
,→
with CR-SFT yields consistent gains over MathOctopus, with the 7B model improving
,→
by +2.4%
,→
Score: 2
Cross-Lingual Distillation for Multilingual Math Reasoning
We extend consistency-regularized multilingual SFT with a teacher-student framework
,→
that distills reasoning skills from a strong English teacher into a multilingual
,→
student. Given parallel MGSM8KInstruct data, the teacher generates high-quality
,→
rationales and answers in English, which are translated and used to supervise the
,→
student in non-dominant languages. We combine teacher-forced rationale
,→
distillation with consistency losses on final answers, and introduce a selective
,→
distillation filter to discard low-confidence teacher traces. On MGSM and a
,→
bilingual subset of MSVAMP, our 7B student outperforms CR-SFT by +1.5-2.1%
Score: 3
Round-Trip Self-Training for Low-Resource Multilingual Reasoning
To reduce reliance on parallel supervision, we propose round-trip self-training
,→
(RT-ST) that bootstraps multilingual mathematical reasoning from monolingual
,→
non-English data. RT-ST generates pseudo-labeled rationales by translating
,→
non-English problems to English, invoking the English teacher to produce
,→
rationales/answers, and translating them back. We introduce round-trip
,→
validation-requiring that translating the generated rationale back to English
,→
recovers an equivalent solution-and an error-aware filter using a symbolic solver.
,→
Training with a mix of distilled parallel data and RT-ST pseudo-labels improves
low-resource languages by +2.7%
,→
Score: 4

39

PreScience: A Benchmark for Forecasting Scientific Contributions

Step-Contrast: Contrastive Alignment of Cross-Lingual Reasoning Traces
We study whether aligning the structure of reasoning across languages yields further
,→
gains beyond answer consistency. Step-Contrast introduces a contrastive objective
,→
over token-level reasoning steps: steps that correspond across translations are
,→
pulled together in an embedding space, while steps from unrelated problems are
,→
pushed apart. We obtain soft step correspondences using attention-based alignment
,→
between bilingual rationales. Step-Contrast is combined with SFT and RT-ST to
,→
yield a unified objective that encourages both accurate and structurally aligned
,→
reasoning. On MGSM and MSVAMP, Step-Contrast reduces cross-language variance of
,→
step-level entailment by 15%
Score: 5
XM-Reward: Cross-Lingual Consistency Reward Modeling for Reasoning
Moving beyond purely supervised objectives, we introduce XM-Reward, a learned reward
,→
model that scores multilingual reasoning traces by cross-lingual faithfulness and
,→
correctness. XM-Reward leverages (i) translation-consistency checks between
,→
non-dominant and English rationales/answers, (ii) symbolic verification when
,→
applicable, and (iii) fluency and step-validity heuristics. We train XM-Reward on
,→
preference pairs derived from Step-Contrast outputs and filtered by round-trip
,→
validation. Using offline policy optimization with reward-weighted SFT and
,→
KL-regularization, we improve over Step-Contrast by +1.6%
Score: 6
MPO: Multilingual Preference Optimization via Consistency-Derived Feedback
We convert cross-lingual consistency signals into pairwise preferences to directly
optimize the policy with preference learning. Our Multilingual Preference
,→
Optimization (MPO) framework constructs, for each problem and language, pairs of
,→
model-generated traces with different cross-lingual agreement and solver-verified
,→
correctness. We study Direct Preference Optimization (DPO) vs. likelihood-ratio
,→
methods on this multilingual preference data, initialized from the XM-Reward-tuned
,→
model. MPO enhances both answer accuracy and cross-language agreement: on MGSM, it
,→
yields +3.8%
,→
Score: 7
Anchor-Align PO: Dominant-Language Anchored Preference Optimization for xMR
We formalize dominant-language anchoring in preference optimization. Anchor-Align PO
uses an off-the-shelf translation model to map non-dominant language traces to
,→
English, and defines preferences by (1) answer equivalence to a trusted English
,→
reference, (2) rationale consistency measured by bilingual entailment, and (3)
,→
solver-backed correctness. We train with both DPO and PPO variants, balancing
,→
cross-lingual alignment with exploration via KL control. Evaluated on MGSM,
,→
MSVAMP, and a subset of MNumGLUESub, Anchor-Align PO improves non-dominant
,→
language performance by +5.6%
,→
Score: 8
Towards MAPO: Multilingual-Alignment-as-Preference Optimization for Reasoning
We unify consistency-driven preference learning into a general
,→
Multilingual-Alignment-as-Preference Optimization (MAPO) paradigm. MAPO defines
,→
preferences by aligning non-dominant language reasoning to a dominant-language
,→
anchor using translation-mediated agreement on both answers and intermediate
,→
steps, supervised by solver checks when feasible. The framework supports DPO for
,→
stable offline alignment and PPO for online refinement, and plugs into any base
,→
LLM. Across three benchmarks-MSVAMP, MGSM, and MNumGLUESub-MAPO yields robust
,→
gains over Anchor-Align PO (+1.5-3.0%
Score: 9
MAPO: Boosting Multilingual Reasoning by Casting Cross-Language Alignment as
,→
Preference Optimization

40

PreScience: A Benchmark for Forecasting Scientific Contributions
Although reasoning is often regarded as language-independent, current LLMs display
,→
uneven reasoning performance across languages; for instance, a dominant language
,→
like English typically outperforms others due to imbalanced multilingual training
,→
data. To strengthen reasoning in non-dominant languages, we introduce a
,→
Multilingual-Alignment-as-Preference Optimization framework (MAPO) that aligns the
reasoning processes in other languages with those of the dominant language. In
,→
,→
particular, we leverage an off-the-shelf translation model to enforce consistency
,→
between answers in non-dominant and dominant languages, and treat this consistency
,→
as a preference signal for optimization with methods such as Direct Preference
,→
Optimization (DPO) or Proximal Policy Optimization (PPO). Empirically, MAPO
,→
reliably delivers substantial improvements in multilingual reasoning across
,→
various models on three benchmarks (MSVAMP +16.2%
Score: 10
Reference E:
ConDaFormer: A Decomposed Transformer with Local Structure Boosting for 3D Point Cloud
,→
Analysis
Recent studies have applied transformers to 3D point cloud understanding with notable
success. However, the sheer number of points-often over 0.1 million-renders global
,→
self-attention impractical for point clouds. Consequently, many methods confine
,→
the transformer to local neighborhoods, such as spherical or cubic windows. Even
,→
then, the volume of Query-Key pairs remains large, incurring high computational
,→
overhead. Moreover, prior approaches typically derive queries, keys, and values
,→
via linear projections, neglecting explicit modeling of local 3D geometric
,→
structure. To tackle both efficiency and local geometry priors, we propose a new
,→
transformer block, ConDaFormer. Specifically, ConDaFormer decomposes a cubic
,→
window into three orthogonal 2D planes, thereby reducing the number of points
,→
involved while maintaining a comparable attention span. This disassembly enables a
,→
larger attention range without increasing computational complexity, albeit at the
,→
risk of missing some contextual information. To address this, we introduce a local
,→
structure enhancement strategy that applies a depth-wise convolution before and
,→
after the attention, which also reinforces the encoding of local geometric cues.
,→
With these components, ConDaFormer captures both long-range contextual
,→
dependencies and local priors. We demonstrate its effectiveness through
,→
experiments on multiple 3D point cloud understanding benchmarks. Code is available
,→
at https://github.com/LHDuan/ConDaFormer .
,→
Generations:
Swin: A Hierarchical Vision Transformer Based on Shifted Window Attention
We introduce Swin Transformer, a vision Transformer that serves as a general-purpose
backbone for computer vision. Adapting Transformers from language to vision is
,→
,→
challenging due to domain differences, including the wide range of object scales
,→
in images and the far higher spatial resolution of pixels compared to words. To
bridge this gap, we propose a hierarchical Transformer that computes
,→
,→
representations using shifted windows. This shifted window strategy confines
,→
self-attention to non-overlapping local windows for efficiency, while still
,→
enabling connections across windows. The hierarchical design supports multi-scale
,→
modeling and achieves computational complexity that scales linearly with image
,→
size. These properties make Swin Transformer applicable to a broad set of tasks,
,→
from image classification (87.3 top-1 accuracy on ImageNet-1K) to dense prediction
,→
tasks such as object detection (58.7 box AP and 51.1 mask AP on COCO test-dev) and
,→
semantic segmentation (53.5 mIoU on ADE20K val). It surpasses prior
,→
state-of-the-art results by large margins of +2.7 box AP and +2.6 mask AP on COCO,
,→
and +3.2 mIoU on ADE20K, highlighting the potential of Transformer-based backbones
,→
for vision. The hierarchical formulation and shifted window mechanism also prove
,→
advantageous for all-MLP architectures. Code and models are available at
,→
https://github.com/microsoft/Swin-Transformer.
Score: 1
Swin-Stripe: Shifted Window Transformers with Orthogonal Strip Fusion for 2D Vision

41

PreScience: A Benchmark for Forecasting Scientific Contributions
We extend the shifted-window paradigm of hierarchical vision Transformers by
,→
introducing orthogonal strip attention that complements square local windows. In
,→
Swin-Stripe, self-attention is computed within non-overlapping windows as in Swin,
,→
while lightweight horizontal and vertical strip attentions bridge distant regions
,→
with negligible overhead. This hybrid local-global scheme increases the effective
,→
receptive field without abandoning linear complexity in image size. The
,→
architecture remains hierarchical and maintains cyclic shifts for cross-window
,→
connectivity. Experiments on image classification, object detection, and semantic
,→
segmentation show consistent gains over a pure windowed baseline, particularly on
,→
long, thin structures where strip fusion is beneficial.
Score: 2
Video Swin-Tube: Hierarchical Spatiotemporal Transformer with Shifted Tube Windows
We adapt shifted-window Transformers from images to videos by generalizing local
,→
windows into spatiotemporal tubes. Video Swin-Tube performs self-attention within
,→
space-time tubes and uses cyclic temporal-spatial shifts to exchange information
,→
across tube boundaries. To preserve efficiency, we augment tube attention with the
,→
orthogonal strip fusion from Swin-Stripe along spatial and temporal axes,
,→
enlarging context without incurring full global cost. The hierarchical design
,→
yields linear complexity in the number of frames and spatial resolution. On video
,→
action recognition and spatiotemporal segmentation benchmarks, Video Swin-Tube
,→
achieves competitive accuracy with significantly reduced memory compared to global
,→
attention baselines.
Score: 3
Voxel-Swin: Shifted Cubic Windows for 3D Volumetric Vision
We move from spatiotemporal grids to true 3D volumetric data, introducing Voxel-Swin,
a hierarchical Transformer with shifted cubic windows. Analogous to its 2D and
,→
video counterparts, Voxel-Swin computes attention locally within cubes and uses
,→
cyclic shifts for cross-cube communication, enabling scalable modeling of large
,→
medical or scientific volumes. We analyze memory and compute trade-offs of cubic
,→
window sizes and demonstrate that Voxel-Swin attains strong performance on
,→
volumetric segmentation tasks (e.g., multi-organ CT, brain MRI), while maintaining
,→
near-linear complexity in voxel count. Results highlight the generality of
,→
shifted-window Transformers across 2D, 2.5D, and 3D grid-structured data.
,→
Score: 4
GeoVoxel-Transformer: Geometry-Aware Local Attention on Sparse Voxelized Point Clouds
To address the inefficiency of dense volumetric grids for real-world 3D scenes, we
,→
propose GeoVoxel-Transformer, which operates on sparse voxelized point clouds.
,→
Building on shifted cubic windows, we introduce geometry-aware relative positional
,→
encodings and a lightweight depth-wise convolutional refinement applied after
,→
attention to inject local geometric priors. This design retains the hierarchical
,→
pyramid while respecting sparsity via submanifold operations. Evaluations on
,→
indoor scene segmentation and semantic scene completion demonstrate improved
,→
accuracy and efficiency over both dense volumetric Transformers and sparse 3D CNN
,→
baselines, highlighting the importance of geometry-aware attention on sparse data.
Score: 5
PlaneSwin: Disassembled Cubic Attention via Orthogonal Plane Aggregation
We further reduce the cost of local 3D attention by disassembling each cubic window
,→
into three orthogonal 2D planes (XY, YZ, ZX) and computing attention on these
,→
planes independently. PlaneSwin fuses the three plane-wise outputs to approximate
,→
cubic-context modeling while processing substantially fewer query-key pairs per
,→
pass. This disassembly enlarges the effective attention range at fixed complexity
,→
compared to purely cubic windows. Integrated into a sparse, hierarchical backbone,
,→
PlaneSwin yields faster inference and improved segmentation accuracy on
,→
large-scale indoor datasets. Ablations show that plane-wise attention provides a
,→
favorable accuracy-efficiency trade-off over cubic attention in sparse voxel
,→
settings.
Score: 6
PointPlane: Plane-wise Local Attention on Raw Point Clouds

42

PreScience: A Benchmark for Forecasting Scientific Contributions
We remove the voxelization step and introduce PointPlane, a Transformer operating
,→
directly on raw point clouds with plane-wise local attention. For each point, we
,→
form a local neighborhood via radius search and project neighbors onto three
,→
orthogonal 2D planes anchored to a canonical axis frame. Attention is computed per
,→
plane to capture long-range context within a controlled 2D manifold, then fused
across planes and scales using a hierarchical pooling scheme. PointPlane preserves
,→
,→
the efficiency of plane disassembly while avoiding voxel quantization artifacts.
,→
On classification and segmentation benchmarks, it outperforms voxel-based
,→
counterparts at comparable or lower computational cost.
Score: 7
PointPlane-LSE: Local Structure Enhanced Plane-wise Transformers for 3D Point
,→
Understanding
We enhance plane-wise point Transformers with an explicit local structure modeling
,→
module. PointPlane-LSE applies depth-wise convolutions on the projected plane maps
,→
both before attention (to encode geometric cues such as curvature and anisotropy)
,→
and after attention (to refine aggregated context). Coupled with a hierarchical
,→
subsampling and feature propagation strategy, this yields improved robustness to
,→
sampling density and noise. Experiments on indoor (S3DIS, ScanNet) and outdoor
,→
(SemanticKITTI) segmentation, as well as shape classification, show consistent
,→
gains over PointPlane and other local attention baselines, demonstrating the
,→
complementary roles of plane-wise attention and convolutional structure
,→
enhancement.
Score: 8
ConDaFormer-A: Disassembled Transformer with Adaptive Plane Decomposition for Point
,→
Clouds
We present ConDaFormer-A, a disassembled point cloud Transformer that generalizes
orthogonal plane-wise attention to adaptive planes derived from local geometry.
,→
For each point neighborhood, we estimate a local frame via PCA and project
,→
neighbors onto three data-adaptive planes, enabling attention to align with
,→
surface orientation while retaining the computational benefits of 2D processing.
,→
As in PointPlane-LSE, depth-wise convolutions are applied before and after
,→
attention to encode and refine local structure. This adaptive decomposition
,→
improves modeling of anisotropic surfaces and thin structures, albeit with modest
,→
overhead for frame estimation. Across standard 3D benchmarks, ConDaFormer-A
,→
achieves strong accuracy-efficiency trade-offs and ablations highlight when
,→
adaptive versus fixed planes are preferable.
,→
Score: 9
ConDaFormer: A Decomposed Transformer with Local Structure Boosting for 3D Point Cloud
,→
Analysis
Recent studies have applied transformers to 3D point cloud understanding with notable
,→
success. However, the sheer number of points-often over 0.1 million-renders global
,→
self-attention impractical for point clouds. Consequently, many methods confine
the transformer to local neighborhoods, such as spherical or cubic windows. Even
,→
,→
then, the volume of Query-Key pairs remains large, incurring high computational
,→
overhead. Moreover, prior approaches typically derive queries, keys, and values
,→
via linear projections, neglecting explicit modeling of local 3D geometric
,→
structure. To tackle both efficiency and local geometry priors, we propose a new
,→
transformer block, ConDaFormer. Specifically, ConDaFormer decomposes a cubic
,→
window into three orthogonal 2D planes, thereby reducing the number of points
,→
involved while maintaining a comparable attention span. This disassembly enables a
,→
larger attention range without increasing computational complexity, albeit at the
,→
risk of missing some contextual information. To address this, we introduce a local
,→
structure enhancement strategy that applies a depth-wise convolution before and
,→
after the attention, which also reinforces the encoding of local geometric cues.
,→
With these components, ConDaFormer captures both long-range contextual
,→
dependencies and local priors. We demonstrate its effectiveness through
experiments on multiple 3D point cloud understanding benchmarks. Code is available
,→
,→
at https://github.com/LHDuan/ConDaFormer .
Score: 10

43

PreScience: A Benchmark for Forecasting Scientific Contributions
Before providing the score, write about your reasoning about the similarity or
,→
dissimilarity. Immediately after that reasoning line, provide the similarity
,→
score.
Now please score the following pair of title-abstracts for similarity.
Reference:
{{reference_title}}
{{reference_abstract}}
Generation:
{{generation_title}}
{{generation_abstract}}
Use the following output format:
Reasoning: ...
Score: ...

G.2.2. LACERS CORE I NTERPOLATIONS P ROMPT
LACERScore Interpolations Prompt
You are an expert computer scientist.
You will be given a pair of title-abstracts (A and J) corresponding to real research
papers. Your task is to synthesize a realistic sequence of 8 intermediate
,→
title-abstracts (B, C, D, E, F, G, H, I) that sequentially interpolate smoothly
,→
between the two provided ones that each change one specific facet of the
,→
corresponding contribution. Some examples of facets you could change are 1. the
,→
type of contribution (eg. analysis, benchmark, system demo, theoretical advance,
,→
etc.) 2. Type of architecture/technique used (eg. CNNs, transformers, RL, RAG,
,→
diffusion models, RNNs, etc. 3. The type of task / motivation (eg. image
,→
recognition, semantic parsing, language modeling, code generation, image
,→
generation, etc.)
,→
Feel free to change other facets too as you see appropriate. It is important that the
synthesized title-abstracts B-I represent a smooth interpolation between A and J
,→
such that no two consecutive title-abstracts differ too dramatically from each
,→
other. However, it is also important that every pair of consecutive
,→
title-abstracts from A-J do differ from each other in at least one important way.
,→
Please return you responses in the following format:
Title B: ...
Abstract B: ...
Title C: ...
Abstract C: ...
Title D: ...
Abstract D: ...
Title E: ...
Abstract E: ...
Title F: ...
Abstract F: ...
Title G: ...
Abstract G: ...

44

PreScience: A Benchmark for Forecasting Scientific Contributions
Title H: ...
Abstract H: ...
Title I: ...
Abstract I: ...
Here are your inputs:
Title A: {{title_a}}
Abstract A: {{abstract_a}}
Title J: {{title_j}}
Abstract J: {{abstract_j}}

G.3. Validating Metrics
To develop and select among candidate metrics for the Contribution Generation task, we constructed both a validation set
and a test set of human preference judgments.
For the test set, we sampled ten (key reference, target) pairs from PreScience’s training set. For each pair, we
generated ten possible candidate scientific advances, effectively attempting to reproduce each target ten times from
its key references: Concretely, we prompted each of claude-3-sonnet-20240229, gpt-4o-2024-11-20,
meta-llama/Meta-Llama-3.1-8B-Instruct, and o3 mini to produce three follow-up contributions, yielding 30 candidates per target. From the union of these 30 generations and the target paper’s ground-truth key references, we
randomly sampled ten title–abstract pairs to use for annotation and evaluation.
Human annotators (drawn from PreScience’s authors) ranked the sampled generated contributions by conceptual similarity
to the target paper’s ground-truth abstract, allowing ties. In the test set, each annotator ranked all candidates. For the
validation set, we generated ten additional targets with corresponding candidate generations; these were singly annotated.
We used the validation set internally to experiment with variations of FacetScore and LACERScore, and report results in this
paper computed over the test set and the final versions of these metrics.
We measured inter-annotator agreement (IAA) and automated metrics’ agreement with human judgements using Kendall’s
τb (Kendall, 1938) evaluated over the above test set. Annotators exhibit substantial agreement on this task, though some
variability remains. We find that LACERScore is the only metric that approaches agreement comparable with human IAA.
Further, LACERScore judgements appear robust to the choice of underlying LLM judge (Figure 13).

45

PreScience: A Benchmark for Forecasting Scientific Contributions

Figure 13. Agreement between humans, models, and aggregates. ‘Human’ refers to an average agreement among all five annotators –
agreement computed against all the human annotators (excluding self-agreement), and then averaged. LACERScore is the only automated
metric that reaches agreement with humans that is comparable to their IAA.

G.4. Effect of LLM Judge Choice on LACERScore
Table 9 compares LACER scores for Contribution Generation under two independent LLM-based judges (GPT-5 and Claude
Opus 4.5). We observe shifts in absolute values but strong agreement in relative ordering (Pearson 0.97, Spearman 0.81),
suggesting that our main comparisons are not sensitive to the specific choice of judge.
Table 9. LACER scores (n=1000) for Contribution Generation as judged by GPT-5 and Claude Opus 4.5. The scores have a Pearson
correlation of 0.97 and a Spearman correlation of 0.81.

Model
Key Reference
GPT-4o
GPT-4.1
o3
GPT-5
GPT-5.1
GPT-5.2
Claude Sonnet 4.5
Claude Opus 4.5
Gold Paraphrase

LACER (GPT-5)

LACER (Opus)

LACER (Avg)

4.30
4.74
5.11
5.50
5.66
5.39
5.63
5.04
5.04
10.00

4.05
4.53
4.60
4.67
4.65
4.74
4.70
4.44
4.55
9.79

4.18
4.63
4.86
5.08
5.16
5.07
5.16
4.74
4.79
9.89

G.5. LACERScored Examples
46

PreScience: A Benchmark for Forecasting Scientific Contributions
Table 10. Example (Ground Truth, Generated) Abstract Pairs by LACER Score (Descending)
Score

Ex.

Ground Truth

Generated

10

1

Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality (Feng et al., 2025)

Conformal RAG: Evidence-Conditioned Guarantees and Utility-Preserving
Editing for Retrieval-Augmented LLMs

Existing research on Retrieval-Augmented Generation (RAG) primarily focuses on improving overall question-answering accuracy, often overlooking the quality
of sub-claims within generated responses. Recent methods that attempt to improve
RAG trustworthiness, such as through auto-evaluation metrics, lack probabilistic
guarantees or require ground truth answers. To address these limitations, we propose
Conformal-RAG, a novel framework inspired by recent applications of conformal
prediction (CP) on large language models (LLMs). Conformal-RAG leverages CP
and internal information from the RAG mechanism to offer statistical guarantees
on response quality. It ensures group-conditional coverage spanning multiple
sub-domains without requiring manual labelling of conformal sets, making it suitable
for complex RAG applications. Compared to existing RAG auto-evaluation methods,
Conformal-RAG offers statistical guarantees on the quality of refined sub-claims,
ensuring response reliability without the need for ground truth answers. Additionally,
our experiments demonstrate that by leveraging information from the RAG system,
Conformal-RAG retains up to 60% more high-quality sub-claims from the response
compared to direct applications of CP to LLMs, while maintaining the same reliability
guarantee.

Retrieval-augmented generation (RAG) reduces hallucinations by grounding
large language models (LLMs) in external evidence, but it offers no finite-sample
guarantees and often trades factuality for answer completeness. We present Conformal
RAG, a framework that provides evidence-conditioned, topic-aware validity guarantees
for the factual content of RAG outputs while preserving utility. Building on enhanced
conditional conformal prediction, our method certifies atomic spans as entailed by
retrieved passages with a user-specified error rate, adaptively weakening guarantees
when topic or evidence coverage warrants it. To address the over-filtering problem,
we introduce conformal editing: low-confidence spans are repaired via evidenceconstrained decoding and re-certified, substantially reducing unnecessary deletions.
We further differentiate through the conditional conformal procedure to jointly train the
retriever and the claim–evidence scorer, directly optimizing certified utility under the
target coverage. Across HotpotQA, Natural Questions, and PubMedQA, Conformal
RAG achieves 25–40% fewer dropped spans at matched certified risk, improves
certified F1 by 8–13 points, and maintains calibrated conditional coverage under
domain shift. Ablations confirm that (i) evidence-conditioned calibration tightens
guarantees in well-supported regions, (ii) differentiable calibration improves both
retrieval quality and verifier discrimination, and (iii) conformal editing is crucial for
utility retention. Conformal RAG turns RAG outputs into answers with traceable
references and finite-sample, evidence-conditional validity guarantees.

Conformal Prediction for Signal Temporal Logic Inference (Li et al., 2025)

ConfTLINet: Conformal Temporal Logic Inference with End-to-End Calibration
and Coverage Guarantees

10

2

Signal Temporal Logic (STL) inference seeks to extract human-interpretable
rules from time-series data, but existing methods lack formal confidence guarantees
for the inferred rules. Conformal prediction (CP) is a technique that can provide
statistical correctness guarantees, but is typically applied as a post-training wrapper
without improving model learning. Instead, we introduce an end-to-end differentiable
CP framework for STL inference that enhances both reliability and interpretability
of the resulting formulas. We introduce a robustness-based nonconformity score,
embed a smooth CP layer directly into training, and employ a new loss function that
simultaneously optimizes inference accuracy and CP prediction sets with a single term.
Following training, an exact CP procedure delivers statistical guarantees for the learned
STL formulas. Experiments on benchmark time-series tasks show that our approach
reduces uncertainty in predictions (i.e., it achieves high coverage while reducing
prediction set size), and improves accuracy (i.e., the number of misclassifications when
using a fixed threshold) over state-of-the-art baselines.

9

1

Interpretable temporal specifications learned from data are critical in safetyand mission-critical settings, yet existing neural-symbolic approaches offer limited
uncertainty control at deployment. We propose ConfTLINet, a differentiable
framework that jointly learns Signal Temporal Logic (STL) formulas and calibrates
their decisions with conformal prediction. ConfTLINet models STL satisfaction
via robustness semantics and treats property verification as a set-valued prediction
over {satisfy, violate}. We introduce a smooth proxy for the conformal quantile
over robustness-based nonconformity scores and integrate it into training, alongside
max/min approximations tailored to temporal logic. This enables end-to-end
optimization that directly minimizes conformal inefficiency (prediction set size or
abstention rate) while shaping where uncertainty concentrates, all under a target risk
level α. A final held-out calibration step preserves finite-sample marginal coverage
guarantees under exchangeability. Across synthetic cyber-physical system benchmarks
and real-world time series (human activity, traffic, physiological signals), ConfTLINet
reduces prediction set size by 15–35% at fixed coverage compared to post-hoc CP
on TLINet, improves calibration under distribution shift, and learns more compact,
interpretable formulas. Ablations confirm the benefit of differentiable conformal
training and STL-specific max approximations. ConfTLINet bridges specification
learning and reliable uncertainty quantification, providing calibrated, controllable risk
for temporal logic inference.

A First Runtime Analysis of NSGA-III on a Many-Objective Multimodal Problem:
Provable Exponential Speedup via Stochastic Population Update (Opris, 2025)

Stochastic NSGA-III with Crossover: Near-Tight Runtimes on Many-Objective
Benchmarks and Exponential Separations on Royal Roads

The NSGA-III is a prominent algorithm in evolutionary many-objective optimization. It is well-suited for optimizing functions with more than three objectives,
setting it apart from the classic NSGA-II. However, theoretical insights about
NSGA-III of when and why it performs well are still in its early development. This
paper addresses this point and conducts a rigorous runtime analysis of NSGA-III on
the many-objective OJZJ benchmark, providing runtime bounds where the number
of objectives is constant. We show that NSGA-III finds the Pareto front of OJZJ in
time O(nk+d/2 + µn ln(n)) where n is the problem size, d is the number
of objectives, k is the gap size, a problem specific parameter, if its population size
µ ∈ 2O(n) is at least (2n/d + 1)d/2 . Notably, NSGA-III is faster than NSGA-II
by a factor of µ/nd/2 for some µ ∈ ω(nd/2 ). We also show that a stochastic
population update provably guarantees a speedup of order Θ((k/b)k−1 ) in the
runtime where b > 0 is a constant. This is the first rigorous runtime analysis of
NSGA-III on OJZJ. Proving these bounds requires a much deeper understanding of the
population dynamics of NSGA-III than previous papers achieved.

We study a crossover-enabled and stochastically updated variant of NSGA-III
for many-objective discrete optimization. Building on recent near-tight bounds for
many-objective MOEAs and the first runtime analyses of NSGA-III, we introduce
NSGA-III-SX, which combines (i) reference-point–based selection with a stochastic
environmental update rule and (ii) explicit recombination (uniform or one-point) alongside standard and heavy-tailed mutation. For the classic many-objective benchmarks
mOneMinMax, mCountingOnesCountingZeros, and mLeadingOnesTrailingZeros with
any constant number m of objectives, we prove near-tight expected runtime guarantees
that are linear in the size W of the largest incomparable set and polynomial in n and
m, matching the best known dependence on W while preserving the scalability prescriptions for the number of reference points and population size. For the multimodal
many-objective OneJumpZeroJump with jump size 2 ≤ k ≤ n/4, we show that
NSGA-III-SX strictly improves over deterministic-update, mutation-only variants: its
expected time decreases by a superpolynomial factor in k when heavy-tailed mutation
is used, and by an additional polynomial factor when crossover is enabled, yielding
bounds of the form W · poly(n, m) · nk−1 under standard parameter settings. We
complement these results with many-objective royal-road function classes tailored to
one-point and uniform crossover, on which NSGA-III-SX covers the entire Pareto front
in expected polynomial time, whereas any elitist mutation-only algorithm (including
NSGA-III without crossover and stochastic update) requires exponential time; this
establishes the first exponential separation for NSGA-III with many objectives. Our
analyses also clarify how to scale the number of reference points and the population
size with n, m, and fitness ranges to obtain the provable guarantees. Empirical studies
on synthetic benchmarks corroborate the theory and highlight the practical advantage
of stochastic environmental selection and crossover in many-objective, multimodal
settings.
Continued on next page

47

PreScience: A Benchmark for Forecasting Scientific Contributions
Score

Ex.

Ground Truth

Generated

9

2

DiffPAD: Denoising Diffusion-based Adversarial Patch Decontamination (Fu
et al., 2024)

Mask-DDRM: Training-Free Adversarial Patch Defense via Robust Diffusion
Restoration

In the ever-evolving adversarial machine learning landscape, developing effective defenses against patch attacks has become a critical challenge, necessitating
reliable solutions to safeguard real-world AI systems. Although diffusion models
have shown remarkable capacity in image synthesis and have been recently utilized
to counter ℓp -norm bounded attacks, their potential in mitigating localized patch
attacks remains largely underexplored. In this work, we propose DiffPAD, a novel
framework that harnesses the power of diffusion models for adversarial patch
decontamination. DiffPAD first performs super-resolution restoration on downsampled
input images, then adopts binarization, dynamic thresholding scheme and sliding
window for effective localization of adversarial patches. Such a design is inspired
by the theoretically derived correlation between patch size and diffusion restoration
error that is generalized across diverse patch attack scenarios. Finally, DiffPAD
applies inpainting techniques to the original input images with the estimated patch
region being masked. By integrating closed-form solutions for super-resolution
restoration and image inpainting into the conditional reverse sampling process
of a pre-trained diffusion model, DiffPAD obviates the need for text guidance or
fine-tuning. Through comprehensive experiments, we demonstrate that DiffPAD not
only achieves state-of-the-art adversarial robustness against patch attacks but also
excels in recovering naturalistic images without patch remnants.

We present Mask-DDRM, a training-free defense that unifies adversarial patch
localization and removal by extending Denoising Diffusion Restoration Models
(DDRM) with robust, anomaly-aware inference. We model a patched image as an
unknown occlusion process y = (1 − m) ⊙ x + m ⊙ o + n, where x is the clean
image, m is an unknown patch mask, and o captures adversarial content. Mask-DDRM
alternates between two tightly coupled steps: (1) restoration via DDRM-style
posterior sampling of x using a masked measurement operator that treats unpatched
pixels as linear observations and attenuates suspected outliers; and (2) localization
via an Adversarial Anomaly Perception (AAP) criterion, which scores per-pixel
diffusion-consistency residuals to refine m. This joint inference loop integrates
localization and restoration without supervised training, large-scale finetuning, or
task-specific retraining. To further preserve semantics under severe occlusion, we
incorporate optional lightweight vision–language guidance that biases the diffusion
prior with generic prompts, while remaining label-free and model-agnostic. Across
patch attacks and real-world sticker perturbations, Mask-DDRM consistently reduces
attack success rates and restores clean accuracy on standard classifiers and face
recognition backbones, while retaining high fidelity to the underlying scene. Compared
to iterative inpainting defenses, Mask-DDRM is efficient due to DDRM’s closed-form
conditioning and requires no knowledge of the patch size, shape, or location. Ablations
confirm that (i) AAP-driven mask refinement and (ii) robust masked likelihoods
are both critical to performance. Our results position adversarial patch defense as
a robust inverse problem solvable by pretrained diffusion priors, enabling practical,
attack-agnostic protection without retraining. Code and models will be released.

Unsupervised Discovery of Formulas for Mathematical Constants (Shalyt et al.,
2024)

Learning-Guided Discovery and Certification of Conservative Matrix Fields

8

1

Ongoing efforts that span over decades show a rise of AI methods for accelerating scientific discovery, yet accelerating discovery in mathematics remains a
persistent challenge for AI. Specifically, AI methods were not effective in creation
of formulas for mathematical constants because each such formula must be correct
for infinite digits of precision, with “near-true” formulas providing no insight toward
the correct ones. Consequently, formula discovery lacks a clear distance metric
needed to guide automated discovery in this realm. In this work, we propose a
systematic methodology for categorization, characterization, and pattern identification
of such formulas. The key to our methodology is introducing metrics based on the
convergence dynamics of the formulas, rather than on the numerical value of the
formula. These metrics enable the first automated clustering of mathematical formulas.
We demonstrate this methodology on Polynomial Continued Fraction formulas, which
are ubiquitous in their intrinsic connections to mathematical constants, and generalize
many mathematical functions and structures. We test our methodology on a set of
1,768,900 such formulas, identifying many known formulas for mathematical constants,
and discover previously unknown formulas for π, ln(2), Gauss’, and Lemniscate’s
constants. The uncovered patterns enable a direct generalization of individual formulas
to infinite families, unveiling rich mathematical structures. This success paves the way
towards a generative model that creates formulas fulfilling specified mathematical
properties, accelerating the rate of discovery of useful formulas.

8

2

Conservative matrix fields organize and generate infinite families of continued
fraction identities, unifying known formulas and enabling Apéry-like proofs of
irrationality. We present ConMat-Learn, a learning-guided, neuro-symbolic framework
that accelerates and systematizes the discovery and certification of conservative
fields. ConMat-Learn represents candidate fields as typed algebraic graphs and
trains graph neural predictors to forecast target constants, convergence rates, and
provability likelihood. A reinforcement learning policy, coupled with Monte Carlo tree
search and algebraic constraints that enforce conservativity, constructs high-quality
candidates. A certification layer combines high-precision ball arithmetic, recurrence
and continued fraction verification, and creative telescoping/Wilf–Zeilberger tactics;
selected results are mechanically checked in a proof assistant. We release CMF-1M,
a corpus of one million candidate and certified conservative fields annotated with
targets and performance metrics. Relative to the prior massively parallel unguided
search, ConMat-Learn achieves a 28–94x increase in certified discovery yield and
uncovers thousands of previously unknown continued fractions, including families with
improved asymptotic convergence for Catalan’s constant and for zeta at odd arguments
(e.g., ζ(5), ζ(7)), alongside new relations linking polylogarithms and Euler sums.
We prove several new identities and construct Apéry-like sequences that sharpen known
irrationality measures for ζ(3) and log 2. Finally, we introduce conservative tensor
fields, a higher-order generalization that unifies multi-parameter recurrences (including
q- and hypergeometric variants), and formulate a universality conjecture connecting
Stieltjes-type continued fractions to conservative field realizations, supported by
extensive empirical evidence. Code, data, and certified proofs are available at a public
repository.

Neural networks leverage nominally quantum and post-quantum representations
(Riechers et al., 2025)

From Belief States to Quantum Instruments: Learning Completely-Positive
Realizations with Transformers

We show that deep neural networks, including transformers and RNNs, pretrained as usual on next-token prediction, intrinsically discover and represent beliefs
over ‘quantum’ and ‘post-quantum’ low-dimensional generative models of their
training data – as if performing iterative Bayesian updates over the latent state of this
world model during inference as they observe more context. Notably, neural nets easily
find these representation whereas there is no finite classical circuit that would do the
job. The corresponding geometric relationships among neural activations induced
by different input sequences are found to be largely independent of neural-network
architecture. Each point in this geometry corresponds to a history-induced probability
density over all possible futures, and the relative displacement of these points reflects
the difference in mechanism and magnitude for how these distinct pasts affect the
future.

We address the problem of inferring physically valid quantum generators of
classical stochastic processes directly from sequence data. Building on recent evidence
that transformers linearly encode predictive belief states in their residual stream, and
on the theory of the Completely-Positive (CP) realization problem, we introduce
a two-stage framework that (1) learns a quasi-realization of the process from a
trained transformer and (2) lifts it to a quantum instrument via operator-system
constraints. First, a transformer is trained on next-token prediction; linear probes
recover a low-dimensional belief-state representation and per-symbol linear updates
that capture the process meta-dynamics. Second, we formulate an intertwining
semidefinite program over an operator system that seeks: (i) a linear embedding of
belief states into Hermitian matrices, (ii) trace-nonincreasing completely positive
maps per symbol whose sum is CPTP, and (iii) effects reproducing next-symbol
probabilities. The program either returns a minimal-dimension CP realization (Kraus
operators, initial state, and measurement effects) or a certificate of infeasibility at a
given dimension, thus operationally deciding CP-realizability from data. We prove a
robustness result: if the transformer’s residual stream is an ϵ-linear sufficient statistic
and achieves δ next-token loss above Bayes-optimal, then the recovered instrument
is O(ϵ, δ)-close (in diamond distance) to a true CP realization when one exists.
Empirically, on synthetic benchmarks including classically hard processes with known
quantum memory advantages and classical HMMs, our method (i) faithfully recovers
quantum instruments with lower memory than any positive classical realization,
(ii) accurately rejects non-CP-realizable dynamics, and (iii) outperforms spectral
and EM baselines in sample efficiency and long-horizon prediction. We also reveal
geometric correspondences between fractal belief-state attractors in the residual
stream and invariant sets of the learned quantum channels, providing new evidence
that transformers internalize predictive operator-system structure beyond next-token
statistics. Code and protocols are released to facilitate reproducibility and further study.
Continued on next page

48

PreScience: A Benchmark for Forecasting Scientific Contributions
Score

Ex.

Ground Truth

Generated

7

1

POSS: Position Specialist Generates Better Draft for Speculative Decoding (Huang
et al., 2025)

HEDGE: Harmonized, Uncertainty-Aware Dynamic Draft Graphs for Lossless
Speculative Decoding

Speculative decoding accelerates Large Language Model (LLM) inference by
using a small draft model to predict multiple tokens, and a large target model to
verify these tokens in parallel. Recent studies leverage the hidden state of the target
model to enhance draft model prediction accuracy. However, existing methods suffer
from the degrading quality of draft token predictions at later positions, due to error
accumulation in draft model generated features. In this paper, we propose Position
Specialists (PosS), which consist of multiple position-specialized draft layers to
generate tokens at assigned position(s). Position specialists greatly improve token
acceptance rate at later positions per drafting round, as each specialist only needs to
focus on handling a certain level of draft model feature deviation. Experiment results
on Llama-3-8B-Instruct and Llama-2-13B-chat across six datasets demonstrate that
PosS effectively improves over baselines on average acceptance length and speed-up
ratio.

Speculative sampling accelerates large language model (LLM) decoding but
remains bottlenecked by (i) suboptimal, static draft structures, (ii) training–decoding
mismatches in both context and objective, and (iii) incomplete use of feature-level
signals that can reduce uncertainty. We introduce HEDGE, a unified framework that
addresses all three. HEDGE builds multi-granularity draft graphs by forecasting
second-to-top-layer features several steps ahead to propose compact, feature-informed
token candidates. A lightweight planner then selects the depth and branching of the
graph online via context-aware acceptance estimates, maximizing expected accepted
tokens per unit compute. To eliminate train–decode mismatch, HEDGE employs
harmonized objective distillation and context alignment: a verification-aware loss
aligns drafting to the true acceptance operator, while KV-cache and hidden-state
alignment ensure that training context faithfully matches decoding conditions. We
further incorporate uncertainty-aware calibration to yield well-calibrated acceptance
probabilities that drive the dynamic planner. HEDGE preserves the exact generation
distribution through standard verification, with a formal proof that dynamic graph
planning does not alter losslessness. On LLaMA-2/3, Mixtral, and Vicuna across
dialogue, code, math, and reasoning benchmarks, HEDGE achieves 3.6×–5.1×
average wall-clock speedup over vanilla decoding, outperforming EAGLE by
25%–48% and EAGLE-2 by 12%–28%, and surpassing HASS by 9%–21% at
comparable quality. Ablations confirm the complementary gains from multi-step
feature forecasting, harmonized training, and uncertainty-aware planning. We release
code and models to facilitate adoption.

In a Few Words: Comparing Weak Supervision and LLMs for Short Query
Intent Classification (Alexander & de Vries, 2025)

IntentLLM: LLM-Guided Weak Supervision and Distillation for Fine-Grained
Query Intent Classification

User intent classification is an important task in information retrieval. Previously, user intents were classified manually and automatically; the latter helped to
avoid hand labelling of large datasets. Recent studies explored whether LLMs can
reliably determine user intent. However, researchers have recognized the limitations of
using generative LLMs for classification tasks. In this study, we empirically compare
user intent classification into informational, navigational, and transactional categories,
using weak supervision and LLMs. Specifically, we evaluate LLaMA-3.1-8B-Instruct
and LLaMA-3.1-70B-Instruct for in-context learning and LLaMA-3.1-8B-Instruct for
fine-tuning, comparing their performance to an established baseline classifier trained
using weak supervision (ORCAS-I). Our results indicate that while LLMs outperform
weak supervision in recall, they continue to struggle with precision, which shows the
need for improved methods to balance both metrics effectively.

Understanding user intent is central to retrieval quality. ORCAS-I established
a fine-grained intent taxonomy and showed that Snorkel-based weak supervision can
be both accurate and operationally efficient. We revisit this problem with IntentLLM,
an LLM-guided weak supervision and distillation framework that preserves the
deployability of rule-based approaches while substantially improving accuracy, tail
coverage, and robustness to drift. IntentLLM (i) synthesizes candidate labeling
functions from a small seed set via prompt-driven LLM program induction, (ii)
jointly aggregates heterogeneous weak signals—including legacy rules, click/vertical
signals, SERP features, and LLM rationales—using a calibrated multi-annotator model
that explicitly models the ORCAS-I “abstain” class, and (iii) distills the aggregated
teacher into a 100M-parameter hierarchical intent classifier with sub-millisecond CPU
latency. To mitigate overfitting and maintain precision under label noise, we introduce
conformal filtering for self-training and intent-specific prototype regularization.
Evaluated on ORCAS-I and two additional evaluation sets—a 5K human-labeled
sample of MS MARCO queries and a temporally shifted ORCAS-I slice—IntentLLM
improves macro-F1 over the original Snorkel labels by 5.6–8.9 points overall and
by 9.4–12.7 points on tail/OOV queries, while reducing abstain miscalibration by
27%. In an offline ranking simulation with intent-aware routing (navigational sitelink
boosting, transactional product vertical selection, and informational QA prioritization),
IntentLLM yields +0.8 NDCG@10 and +1.1 MRR on MS MARCO dev and a +0.5%
absolute CTR uplift on a held-out click log. Ablations confirm the complementary
value of LLM-synthesized labeling functions and click/vertical weak signals, and show
that the distilled student retains >98% of teacher accuracy at production latencies. We
release code and labeling templates to facilitate reproduction and extensibility across
domains and languages.

Causal Interpretability for Adversarial Robustness: A Hybrid Generative
Classification Approach (Zhao et al., 2025)

Interventional Adversarial Training at Scale: Causal Robustness Beyond
Norm-Balls

Deep learning-based discriminative classifiers, despite their remarkable success, remain vulnerable to adversarial examples that can mislead model predictions.
While adversarial training can enhance robustness, it fails to address the intrinsic
vulnerability stemming from the opaque nature of these black-box models. We
present a deep ensemble model that combines discriminative features with generative
models to achieve both high accuracy and adversarial robustness. Our approach
integrates a bottom-level pre-trained discriminative network for feature extraction with
a top-level generative classification network that models adversarial input distributions
through a deep latent variable model. Using variational Bayes, our model achieves
superior robustness against white-box adversarial attacks without adversarial training.
Extensive experiments on CIFAR-10 and CIFAR-100 demonstrate our model’s superior
adversarial robustness. Through evaluations using counterfactual metrics and feature
interaction-based metrics, we establish correlations between model interpretability and
adversarial robustness. Additionally, preliminary results on Tiny-ImageNet validate
our approach’s scalability to more complex datasets, offering a practical solution for
developing robust image classification models.

Adversarial training has emerged as the most effective defense against worstcase perturbations, yet conventional formulations constrain the adversary to pixel-space
norm-balls and often fail to capture semantically meaningful manipulations that
arise in the data-generating process. Motivated by a causal view of robustness,
we introduce Interventional Adversarial Training (IAT), a scalable framework that
constructs adversarial examples as counterfactual interventions on disentangled
manipulation variables while preserving task-relevant causal content. Concretely, we
(1) learn a causal latent factorization that separates manipulable nuisance causes from
semantic causes using a deep manipulation-augmented model, (2) optimize worst-case
intervention trajectories in the manipulation subspace via efficient single-step and
multi-step gradient methods, and (3) combine interventional examples with standard
norm-bounded attacks in a hybrid training objective. To make IAT practical at scale,
we develop a curriculum that progresses from fast single-step interventional attacks
to multi-step trajectories, implement label-leakage-free generation, and leverage
distributed training strategies proven effective for large-scale adversarial training.
On ImageNet and CIFAR benchmarks, IAT consistently improves robust accuracy
against both ℓ∞ /ℓ2 attacks and semantically grounded manipulations, enhances
black-box transfer robustness across architectures, and exhibits better generalization
under distribution shift. Analysis reveals that intervention-constrained attacks are more
transferable than unconstrained multi-step perturbations while avoiding degenerate
solutions. Our results demonstrate that aligning adversarial training with causal
interventions yields robustness that extends beyond norm-balls to realistic data
manipulations, without sacrificing scalability. Code and models will be released.

7

6

2

1

Continued on next page

49

PreScience: A Benchmark for Forecasting Scientific Contributions
Score

Ex.

Ground Truth

Generated

6

2

Plastic Learning with Deep Fourier Features (Lewandowski et al., 2024)

OPAL: Overparameterized Paired Activation Layers Preserve Plasticity and
Accelerate Adaptation in Continual Learning

Deep neural networks can struggle to learn continually in the face of nonstationarity. This phenomenon is known as loss of plasticity. In this paper, we
identify underlying principles that lead to plastic algorithms. In particular, we provide
theoretical results showing that linear function approximation, as well as a special case
of deep linear networks, do not suffer from loss of plasticity. We then propose deep
Fourier features, which are the concatenation of a sine and cosine in every layer, and
we show that this combination provides a dynamic balance between the trainability
obtained through linearity and the effectiveness obtained through the nonlinearity of
neural networks. Deep networks composed entirely of deep Fourier features are highly
trainable and sustain their trainability over the course of learning. Our empirical results
show that continual learning performance can be drastically improved by replacing
ReLU activations with deep Fourier features. These results hold for different continual
learning scenarios (e.g., label noise, class incremental learning, pixel permutations) on
all major supervised learning datasets used for continual learning research, such as
CIFAR10, CIFAR100, and tiny-ImageNet.

5

5

1

2

Policy Newton Algorithm in Reproducing Kernel Hilbert Space (Zhang et al.,
2025)

Deep networks trained in non-stationary environments often lose plasticity,
exhibiting slower adaptation and diminished gradients after distribution shifts.
Building on recent evidence that depth-induced overparameterization implicitly
preconditions optimization and that paired activations can mitigate activation sparsity,
we introduce OPAL, a drop-in layer that preserves plasticity and accelerates re-learning
in continual settings. Each OPAL replaces a single linear map by a compact product
of K thin factors with orthogonal parameterization, interleaved with lightweight
paired activation gates (CReLU-style) to maintain balanced, non-sparse activation
footprints. Optionally, a small generate-and-test module injects persistent random
features online to replenish useful representations. In the deep-linear regime, we
derive exact solutions showing that OPAL’s factorization induces a data-adaptive
preconditioner that contracts the Hessian spectrum, yielding depth-independent
adaptation times under orthogonal initialization, an effect unattainable by any fixed
regularizer. Empirically, OPAL improves post-shift learning speed, stability of gradient
norms, and activation density on (i) continual deep RL over sequences of Atari 2600
games and (ii) supervised class-incremental benchmarks including Fashion-MNIST,
with minimal parameter and compute overhead. Across settings, OPAL outperforms
standard backbones, CReLU-only variants, and matches or complements Continual
Backprop; combining OPAL with persistent randomness yields further gains. Our
results connect curvature-aware overparameterization with activation pairing to deliver
a simple, theoretically grounded mechanism for preserving plasticity in continual deep
learning.
VR-CRPO: Off-Policy Variance-Reduced Cubic-Regularized Policy Optimization

Reinforcement learning (RL) policies represented in Reproducing Kernel Hilbert
Spaces (RKHS) offer powerful representational capabilities. While second-order
optimization methods like Newton’s method demonstrate faster convergence than
first-order approaches, current RKHS-based policy optimization remains constrained
to first-order techniques. This limitation stems primarily from the intractability
of explicitly computing and inverting the infinite-dimensional Hessian operator in
RKHS. We introduce Policy Newton in RKHS, the first second-order optimization
framework specifically designed for RL policies represented in RKHS. Our approach
circumvents direct computation of the inverse Hessian operator by optimizing a
cubic regularized auxiliary objective function. Crucially, we leverage the Representer
Theorem to transform this infinite-dimensional optimization into an equivalent,
computationally tractable finite-dimensional problem whose dimensionality scales with
the trajectory data volume. We establish theoretical guarantees proving convergence
to a local optimum with a local quadratic convergence rate. Empirical evaluations
on a toy financial asset allocation problem validate these theoretical properties,
while experiments on standard RL benchmarks demonstrate that Policy Newton in
RKHS achieves superior convergence speed and higher episodic rewards compared
to established first-order RKHS approaches and parametric second-order methods.
Our work bridges a critical gap between non-parametric policy representations and
second-order optimization methods in reinforcement learning.

Second-order policy optimization with cubic regularization has recently been
shown to avoid saddle points and achieve improved sample complexity in reinforcement learning. However, existing cubic-regularized policy Newton algorithms remain
largely on-policy and rely on high-variance gradient/Hessian estimates, which limits
data efficiency and scalability in deep RL. We introduce VR-CRPO, an off-policy,
variance-reduced cubic-regularized policy optimization method that reuses trajectories
from a replay buffer while preserving second-order convergence guarantees. VR-CRPO
employs per-decision importance sampling with clipping and bias correction, together
with SPIDER/SARAH-style recursive estimates for both policy gradients and Hessian–
vector products, enabling a Hessian-free inexact solve of the cubic subproblem
via a preconditioned Lanczos/CG routine. A Fisher-information preconditioner
improves numerical stability and conditioning while maintaining sensitivity to negative
curvature for effective saddle escaping. Under standard smoothness, ergodicity, and
bounded-importance-weight assumptions, we establish high-probability convergence to
an ϵ-second-order stationary point with sample complexity O(ϵ−3 polylog(1/ϵ)),
improving on the best known O(ϵ−3.5 ) rate for policy optimization with cubic
regularization. Empirically, on classic control and MuJoCo continuous-control tasks,
VR-CRPO achieves 1.5–3× lower sample usage to a target return than PPO, TRPO,
and natural policy gradient, and consistently outperforms the prior cubic-regularized
policy Newton baseline in both data efficiency and robustness across seeds. We release
code and implementations of our variance-reduced estimators and cubic subproblem
solver to facilitate reproducibility and follow-up research.

ENAT: Rethinking Spatial-temporal Interactions in Token-based Image Synthesis
(Ni et al., 2024)

MaskDiT: A Unified Masked–Diffusion Transformer with Token-Critic Guidance
for Scalable High-Resolution Image Synthesis

Recently, token-based generation have demonstrated their effectiveness in image synthesis. As a representative example, non-autoregressive Transformers (NATs)
can generate decent-quality images in a few steps. NATs perform generation in a
progressive manner, where the latent tokens of a resulting image are incrementally
revealed. At each step, the unrevealed image regions are padded with mask tokens
and inferred by NAT. In this paper, we delve into the mechanisms behind the
effectiveness of NATs and uncover two important patterns that naturally emerge from
NATs: Spatially (within a step), although mask and visible tokens are processed
uniformly by NATs, the interactions between them are highly asymmetric. In specific,
mask tokens mainly gather information for decoding, while visible tokens tend to
primarily provide information, and their deep representations can be built only upon
themselves. Temporally (across steps), the interactions between adjacent generation
steps mostly concentrate on updating the representations of a few critical tokens, while
the computation for the majority of tokens is generally repetitive. Driven by these
findings, we propose EfficientNAT (ENAT), a NAT model that explicitly encourages
these critical interactions inherent in NATs. At the spatial level, we disentangle the
computations of visible and mask tokens by encoding visible tokens independently,
while decoding mask tokens conditioned on the fully encoded visible tokens. At the
temporal level, we prioritize the computation of the critical tokens at each step, while
maximally reusing previously computed token representations to supplement necessary
information. ENAT improves the performance of NATs notably with significantly
reduced computational cost. Experiments on ImageNet-256, ImageNet-512 and
MS-COCO validate the effectiveness of ENAT.

We present MaskDiT, a single latent-space transformer that unifies masked
generative modeling and diffusion denoising to achieve fast and high-fidelity image
synthesis at scale. MaskDiT operates on a grid of context-rich visual latents obtained
from a pretrained convolutional tokenizer/decoder, combining the expressivity
of transformer-based diffusion (DiT) with the efficiency of bidirectional masked
prediction (MaskGIT). During training, a mixture-of-corruptions objective alternates
between (i) discrete masked token prediction at variable masking ratios for parallel
generation and strong representation learning (in the spirit of MAGE), and (ii)
continuous Gaussian denoising on the same latent grid (as in DiT). We further
introduce a Token-Critic that learns per-location acceptance scores by distinguishing
reconstructed-from-real latents, and use it at inference to adaptively accept, resample,
or refine locations across both the masked and diffusion phases. At sampling time,
MaskDiT performs a coarse-to-fine procedure: a small number of masked iterations
rapidly establishes global semantics and layout, followed by a short diffusion
refinement schedule for photorealistic detail; the Token-Critic enables early stopping
and targeted resampling, improving the speed–quality trade-off. On class-conditional
ImageNet, MaskDiT surpasses non-autoregressive generative transformers and
matches or exceeds diffusion-only baselines with 2–4× fewer refinement steps,
enabling 256×256 and 512×512 synthesis with markedly lower latency. The unified
pretraining also yields competitive representations (e.g., strong linear-probe accuracy)
without task-specific heads. We analyze scaling trends in Gflops and input token
counts and show consistent FID improvements, and demonstrate flexible conditioning
(e.g., class labels and masks) and editing (inpainting/extrapolation) within the same
model. Code and models will be released.
Continued on next page

50

PreScience: A Benchmark for Forecasting Scientific Contributions
Score

Ex.

Ground Truth

Generated

4

1

Benchmarking LLM Guardrails in Handling Multilingual Toxicity (Yang et al.,
2024)

AEGIS-Chat: Context-Aware No-Regret Safety Moderation for Real-World
User–AI Conversations

With the ubiquity of Large Language Models (LLMs), guardrails have become crucial
to detect and defend against toxic content. However, with the increasing pervasiveness
of LLMs in multilingual scenarios, their effectiveness in handling multilingual toxic
inputs remains unclear. In this work, we introduce a comprehensive multilingual test
suite, spanning seven datasets and over ten languages, to benchmark the performance
of state-of-the-art guardrails. We also investigates the resilience of guardrails against
recent jailbreaking techniques, and assess the impact of in-context safety policies
and language resource availability on guardrails’ performance. Our findings show
that existing guardrails are still ineffective at handling multilingual toxicity and lack
robustness against jailbreaking prompts. This work aims to identify the limitations of
guardrails and to build a more reliable and trustworthy LLMs in multilingual scenarios.

Safety moderation for large language models in the wild must contend with
domain shift, multi-turn context, and subtle harms that escape sentence-level filters.
Building on AEGIS’s ensemble of LLM safety experts and online adaptation, and
informed by the challenges revealed by ToxicChat, we present AEGIS-Chat, a
conversational, domain-adaptive moderation framework. AEGIS-Chat introduces: (1)
a stateful router that conditions on conversation history to jointly model user intent,
harm type, and severity, and routes queries to specialized LLM safety experts; (2) a
constrained contextual bandit with delayed, partial feedback that provides dynamic
no-regret guarantees while optimizing a cost-sensitive objective balancing harm
reduction, latency, and over-moderation; and (3) ToxicChat-Safety, a re-annotation of
ToxicChat aligned to the AEGIS taxonomy with multi-label, multi-turn labels, plus
conversation-level metrics that penalize both misses and unnecessary blocks. The
router composes expert rationales via lightweight aggregation and uses calibrated
uncertainty to enable early exits for benign content and escalation to stronger experts
or human review when necessary. On ToxicChat and held-out real-world logs,
AEGIS-Chat improves macro-F1 by 7.8–12.3 points and reduces false positives by
18–25% relative to strong LLM and classifier baselines, while maintaining robustness
to jailbreaks across sparse and critical risk categories. Ablations show context-aware
routing and online adaptation contribute most to gains, and theoretical analysis
establishes dynamic regret bounds under non-stationary conversational distributions
with delayed feedback. AEGIS-Chat demonstrates that safety moderation benefits
from stateful, cost-aware online learning tailored to real user–AI conversations.

RankLLM: A Python Package for Reranking with LLMs (Sharifymoghaddam
et al., 2025)

Expando–Mono–Duo–List: A Unified, Label-Free Seq2Seq Framework for
Efficient Zero-Shot Text Ranking

The adoption of large language models (LLMs) as rerankers in multi-stage retrieval systems has gained significant traction in academia and industry. These models
refine a candidate list of retrieved documents, often through carefully designed
prompts, and are typically used in applications built on retrieval-augmented generation
(RAG). This paper introduces RankLLM, an open-source Python package for reranking
that is modular, highly configurable, and supports both proprietary and open-source
LLMs in customized reranking workflows. To improve usability, RankLLM features
optional integration with Pyserini for retrieval and provides integrated evaluation for
multi-stage pipelines. Additionally, RankLLM includes a module for detailed analysis
of input prompts and LLM responses, addressing reliability concerns with LLM APIs
and non-deterministic behavior in Mixture-of-Experts (MoE) models. This paper
presents the architecture of RankLLM, along with a detailed step-by-step guide and
sample code. We reproduce results from RankGPT, LRL, RankVicuna, RankZephyr,
and other recent models. RankLLM integrates with common inference frameworks and
a wide range of LLMs. This compatibility allows for quick reproduction of reported
results, helping to speed up both research and real-world applications. The complete
repository is available at rankllm.ai, and the package can be installed via PyPI.

Large LLM-based listwise rerankers are effective but costly, while recent seq2seq
rankers demonstrate competitive accuracy with far fewer parameters. We present
Expando–Mono–Duo–List, a unified framework that extends the established Expando–
Mono–Duo design pattern with a “List” stage and consolidates all stages into a single
instruction-routed T5 model. Our approach couples document expansion pretraining
with multi-task ranking and introduces label-free listwise distillation: a listwise
head leverages cross-attention–based relevance estimates to optimize differentiable
NDCG surrogates, while absorbing soft supervision from the model’s own pointwise
and pairwise heads. To scale beyond encoder–decoder context limits, we propose
tournament listwise inference, which composes global rankings from overlapping
candidate blocks without retraining or auxiliary teachers. Across MS MARCO
passage/document, TREC DL, and BEIR zero-shot evaluations, our 220M–770M
parameter models achieve competitive or superior effectiveness to much larger
LLM rerankers and prior seq2seq pipelines, while reducing latency by 30–60% and
eliminating the need for external relevance labels for the listwise stage. Our results
show that a single, small seq2seq model can perform document expansion, pointwise,
pairwise, and listwise reranking, enabling efficient, zero-shot, end-to-end retrieval
pipelines. Code and checkpoints will be released.

Distillation of a tractable model from the VQ-VAE (Hadžić et al., 2025)

Prob-Stream: Uncertainty-Aware Neural Audio Coding via Continuous Mixtures
of Probabilistic Circuits

4

3

2

1

Deep generative models with discrete latent space, such as the Vector-Quantized
Variational Autoencoder (VQ-VAE), offer excellent data generation capabilities, but,
due to the large size of their latent space, their probabilistic inference is deemed
intractable. We demonstrate that the VQ-VAE can be distilled into a tractable model by
selecting a subset of latent variables with high probabilities. This simple strategy is
particularly efficient, especially if the VQ-VAE underutilizes its latent space, which is,
indeed, very often the case. We frame the distilled model as a probabilistic circuit,
and show that it preserves expressiveness of the VQ-VAE while providing tractable
probabilistic inference. Experiments illustrate competitive performance in density
estimation and conditional generation tasks, challenging the view of the VQ-VAE as
an inherently intractable model.

Neural audio codecs such as SoundStream achieve impressive quality at very
low bitrates using residual vector quantization (RVQ) and end-to-end training, but
remain limited by approximate entropy models and ad hoc heuristics for variable
bitrate and robustness. We introduce Prob-Stream, a neural audio codec that integrates
a continuous mixture of tractable probabilistic models with RVQ to deliver uncertaintyaware compression, exact entropy coding, and decoder-side enhancement. Prob-Stream
models the distribution of RVQ codes with a low-dimensional continuous latent
variable that gates a family of probabilistic circuits; numerical integration over a finite
set of latent points compiles this continuous mixture into a tractable circuit, enabling
exact marginals/conditionals for range coding and inference. We train end-to-end
with a rate–distortion–perceptual objective, where the rate term is the negative
log-likelihood under the compiled circuit and the decoder is SoundStream-style with
adversarial and reconstruction losses. Structured dropout across quantizer layers
provides a single variable-bitrate model (3–18 kbps), while the tractable prior supports:
(i) tighter code probability estimates and 10–20% bitrate reduction at matched
subjective quality versus a SoundStream baseline; (ii) uncertainty-aware rate control
that allocates bits to perceptually hard segments; and (iii) decoder-only enhancement
and packet-loss concealment via conditional inference over missing/dropped codes
without additional latency. On 24 kHz speech, music, and general audio, Prob-Stream
improves MUSHRA by 3–6 points at 3 kbps and matches or exceeds EVS/Opus quality
at substantially lower rates, while maintaining real-time CPU decoding and streaming
latency. Ablations show that continuous mixtures outperform discrete mixtures at
equal compute, and that compiling to a probabilistic circuit is critical for both coding
efficiency and robust conditional decoding.
Continued on next page

51

PreScience: A Benchmark for Forecasting Scientific Contributions
Score

Ex.

Ground Truth

Generated

3

2

Beyond Accuracy: EcoL2 Metric for Sustainable Neural PDE Solvers (Kapoor
et al., 2025)

SepNOFormer: Separable Spectral-Temporal Transformers for Scalable
Physics-Informed Operator Learning

Real-world systems, from aerospace to railway engineering, are modeled with
partial differential equations (PDEs) describing the physics of the system. Estimating
robust solutions for such problems is essential. Deep learning-based architectures,
such as neural PDE solvers, have recently gained traction as a reliable solution method.
The current state of development of these approaches, however, primarily focuses on
improving accuracy. The environmental impact of excessive computation, leading to
increased carbon emissions, has largely been overlooked. This paper introduces a
carbon emission measure for a range of PDE solvers. Our proposed metric, EcoL2,
balances model accuracy with emissions across data collection, model training,
and deployment. Experiments across both physics-informed machine learning and
operator learning architectures demonstrate that the proposed metric presents a holistic
assessment of model performance and emission cost. As such solvers grow in scale and
deployment, EcoL2 represents a step toward building performant scientific machine
learning systems with lower long-term environmental impact.

We introduce SepNOFormer, a neural operator that learns families of PDE solution maps with strong physics fidelity, resolution independence, and scalability.
SepNOFormer fuses three ideas: (i) separable spectral convolutions along spatial axes
to capture multi-scale structure efficiently (inspired by Fourier neural operators), (ii)
causal multi-head self-attention over pseudo-temporal sequences to propagate initial/forcing information globally (inspired by PINNsFormer), and (iii) a branch–trunk
interface to query arbitrary coordinates, enabling discretization-agnostic operator
learning (in the spirit of DeepONet and CNOs). To train with limited supervision, we
formulate a physics-informed operator loss that enforces PDE residuals, boundary,
and initial conditions across resolutions. We realize scalable residual evaluation
by combining per-axis factorization with forward-mode automatic differentiation,
allowing 107 –108 collocation points on a single GPU. A multi-resolution curriculum
and residual importance sampling further stabilize optimization and improve generalization. Across Burgers’, Darcy flow, Allen–Cahn, wave, and 2D/3D Navier–Stokes
(including chaotic regimes), SepNOFormer reduces L2 error by 20–45% versus
FNO/CNO/DeepONet and by 35–60% versus PINNs/PINNsFormer under the same
wall-clock budget, while cutting training time by 5–20× relative to PINNs on
high-dimensional problems. The model zero-shot super-resolves solutions by 4–8×,
generalizes across unseen parameter ranges and boundary conditions, and maintains
stability under long rollouts. We provide ablations isolating the benefits of separability,
temporal attention, and physics-informed operator training. Code and pretrained
models will be released.

CHURRO: Making History Readable with an Open-Weight Large VisionLanguage Model for High-Accuracy, Low-Cost Historical Text Recognition
(Semnani et al., 2025)

olmIngest: Structure-Preserving PDF Ingestion for LLM Pretraining and
Retrieval-Augmented Generation

2

1

Accurate text recognition for historical documents can greatly advance the
study and preservation of cultural heritage. Existing vision-language models (VLMs),
however, are designed for modern, standardized texts and are not equipped to read the
diverse languages and scripts, irregular layouts, and frequent degradation found in
historical materials. This paper presents CHURRO, a 3B-parameter open-weight VLM
specialized for historical text recognition. The model is trained on CHURRO-DS, the
largest historical text recognition dataset to date. CHURRO-DS unifies 155 historical
corpora comprising 99,491 pages, spanning 22 centuries of textual heritage across
46 language clusters, including historical variants and dead languages. We evaluate
several open-weight and closed VLMs and optical character recognition (OCR)
systems on CHURRO-DS and find that CHURRO outperforms all other VLMs. On the
CHURRO-DS test set, CHURRO achieves 82.3% (printed) and 70.1% (handwritten)
normalized Levenshtein similarity, surpassing the second-best model, Gemini 2.5
Pro, by 1.4% and 6.5%, respectively, while being 15.5 times more cost-effective. By
releasing the model and dataset, we aim to enable community-driven research to
improve the readability of historical texts and accelerate scholarship.

2

2

PDF corpora contain vast amounts of high-quality knowledge that remain underutilized without faithful recovery of document structure. While olmOCR converts
PDFs to linearized text at low cost and high quality, many downstream uses—continued
pretraining, domain adaptation, and retrieval-augmented generation (RAG)—require
structure-aware representations of tables, equations, figures, lists, and references.
We present olmIngest, an open, scalable pipeline that reconstructs rich, verifiable
markup from PDFs and grounds it to page coordinates. olmIngest uses a multi-pass
strategy: (1) a VLM-driven coarse layout parser segments pages and predicts reading
order; (2) specialized decoders emit structured markup—Markdown/HTML for
sections and lists, CSV/HTML for tables with cell-level spans, LaTeX/MathML for
equations, and JSON for bibliographic entries and cross-references; (3) symbolic
validators (e.g., LaTeX compilation, table shape/type checks, URL/DOI resolution)
detect inconsistencies and trigger targeted re-decoding for self-correction; and (4) a
span-grounding module aligns all tokens to pixel regions to support hybrid visual-text
retrieval. We introduce olmStruct-Bench, a 2,100-document benchmark with metrics
for structural fidelity, including table TEDS, equation exact-match and render-EM,
DOM tree F1, and span-grounding accuracy. On olmStruct-Bench, olmIngest achieves
state-of-the-art structure fidelity over strong baselines, reducing table and equation
errors by 23–38% while keeping cost under $300 per million pages in batch settings. In
downstream evaluations, structure-aware indexing improves doc QA/RAG exact match
by 6.8–11.4 points on queries requiring table/equation reasoning and reduces tokenized
context by 28% via semantic chunking. Continued pretraining of a 7B LLM on 40B
structure-preserved tokens yields consistent gains on PubMedQA (+3.2), DocLayQA
(+5.4), and GSM8K (+1.9). We release code, models, and olmStruct-Bench to catalyze
open, structure-first PDF ingestion.

RespDiff: An End-to-End Multi-scale RNN Diffusion Model for Respiratory
Waveform Estimation from PPG Signals (Miao et al., 2024)

Anytime Diffusion: Schedule-Agnostic Training for Variable-Compute Sampling
and Progressive Decoding

Respiratory rate (RR) is a critical health indicator often monitored under inconvenient
scenarios, limiting its practicality for continuous monitoring. Photoplethysmography
(PPG) sensors, increasingly integrated into wearable devices, offer a chance to
continuously estimate RR in a portable manner. In this paper, we propose RespDiff,
an end-to-end multi-scale RNN diffusion model for respiratory waveform estimation
from PPG signals. RespDiff does not require hand-crafted features or the exclusion
of low-quality signal segments, making it suitable for real-world scenarios. The
model employs multi-scale encoders, to extract features at different resolutions,
and a bidirectional RNN to process PPG signals and extract respiratory waveform.
Additionally, a spectral loss term is introduced to optimize the model further.
Experiments conducted on the BIDMC dataset demonstrate that RespDiff outperforms
notable previous works, achieving a mean absolute error (MAE) of 1.18 bpm for RR
estimation while others range from 1.66 to 2.15 bpm, showing its potential for robust
and accurate respiratory monitoring in real-world applications.

We revisit denoising diffusion probabilistic models (DDPMs) through the lens
of schedule-agnostic training and progressive decoding. While DDPMs achieve
high-fidelity synthesis, their performance and computational cost depend sensitively
on a chosen time discretization and sampler. We introduce Anytime Diffusion, a
single model trained to be robust across discretizations and step counts, enabling
variable compute at inference time and improved progressive generation. Our approach
augments the standard variational objective with two components: (1) randomized
discretization, which samples diverse reverse-time grids and integrators during training;
and (2) multi-step consistency, a denoise-to-denoise loss that aligns the outputs of
long and short reverse trajectories between arbitrary noise levels, effectively distilling
long paths into few-step updates. The resulting model can be sampled with either
stochastic (SDE) or deterministic (ODE) solvers and sustains quality across 4–100
steps without retraining or per-schedule tuning. Beyond fast sampling, we leverage the
strengthened consistency to realize a practical progressive lossy decompression scheme
with explicit rate–distortion control, generalizing DDPM’s progressive decoding to
variable-rate settings. Experiments on CIFAR-10, ImageNet 64×64, and LSUN
256×256 show substantial improvements in low-NFE FID and IS over baseline
DDPMs and competitive solvers, with up to 2–3× reduction in steps for similar
quality. Ablations confirm the complementary roles of randomized discretization
and multi-step consistency, and analyses illustrate robustness to misspecified noise
schedules. Code and models will be released.
Continued on next page

52

PreScience: A Benchmark for Forecasting Scientific Contributions
Score

Ex.

Ground Truth

Generated

1

1

VeriLocc: End-to-End Cross-Architecture Register Allocation via LLM (Jin et al.,
2025)

RULER++: Verifiable, Streaming, and Robust Evaluation of Long-Context
Language Models

Modern GPUs evolve rapidly, yet production compilers still rely on hand-crafted
register allocation heuristics that require substantial re-tuning for each hardware
generation. We introduce VeriLocc, a framework that combines large language
models (LLMs) with formal compiler techniques to enable generalizable and
verifiable register allocation across GPU architectures. VeriLocc fine-tunes an LLM to
translate intermediate representations (MIRs) into target-specific register assignments,
aided by static analysis for cross-architecture normalization and generalization
and a verifier-guided regeneration loop to ensure correctness. Evaluated on matrix
multiplication (GEMM) and multi-head attention (MHA), VeriLocc achieves 85-99%
single-shot accuracy and near-100% pass@100. Case study shows that VeriLocc
discovers more performant assignments than expert-tuned libraries, outperforming
rocBLAS by over 10% in runtime.

Long-context language models (LMs) increasingly claim context windows of
128K tokens and beyond, yet their true ability to utilize long inputs remains
unclear. Prior work (RULER) showed that near-perfect performance on simple
needle-in-a-haystack retrieval masks substantial deficits in multi-hop tracing and
aggregation as sequence length grows. We present RULER++, a comprehensive,
verifiable benchmark for long-context understanding that expands both task coverage
and diagnostic resolution. RULER++ introduces four new evaluation axes: (1)
Streaming: inputs arrive as token streams with needles and dependencies interleaved
over time, measuring recency effects and context-switching costs; (2) Conflict
and Disambiguation: cross-document entity resolution and contradiction handling
with controlled distractors and adversarial placements; (3) Budgeted Compression:
note-taking and summary-to-answer tasks that test whether models can compress and
faithfully reuse information under token budgets; and (4) Robust Retrieval-Reasoning:
compositional and order-sensitive operations over many weak, far-apart cues. To ensure
reliability, RULER++ pairs each instance with a latent program that deterministically
generates both the long context and the answer, enabling exact checking without
LLM judges. We further provide new metrics: effective context length (ECL) curves,
position-sensitivity profiles, conflict-resolution accuracy, and coverage-faithfulness
via span-level citation matching. Evaluating 24 open and closed LMs with advertised
windows from 128K to 1M tokens, we find that: (i) most models that solve static
NIAH degrade sharply in streaming and conflict settings; (ii) aggregation and budgeted
compression are the dominant failure modes beyond 256K; and (iii) position sensitivity
and formatting changes cause precipitous drops, revealing brittle heuristics. RULER++
offers a dynamic instance generator, standardized protocols for sliding-window and
chunked inference, and a public leaderboard. We hope these verifiable, diagnostic
evaluations will guide training and architecture choices for truly long-context
reasoning.

Subcortical Masks Generation in CT Images via Ensemble-Based Cross-Domain
Label Transfer (Lee et al., 2025)

Drift-Adam: Change-Point Aware Adaptive Optimization for Non-Stationary
Objectives

Subcortical segmentation in neuroimages plays an important role in understanding brain anatomy and facilitating computer-aided diagnosis of traumatic brain
injuries and neurodegenerative disorders. However, training accurate automatic
models requires large amounts of labelled data. Despite the availability of publicly
available subcortical segmentation datasets for Magnetic Resonance Imaging (MRI),
a significant gap exists for Computed Tomography (CT). This paper proposes an
automatic ensemble framework to generate high-quality subcortical segmentation
labels for CT scans by leveraging existing MRI-based models. We introduce a robust
ensembling pipeline to integrate them and apply it to unannotated paired MRI-CT
data, resulting in a comprehensive CT subcortical segmentation dataset. Extensive
experiments on multiple public datasets demonstrate the superior performance of
our proposed framework. Furthermore, using our generated CT dataset, we train
segmentation models that achieve improved performance on related segmentation tasks.
To facilitate future research, we make our source code, generated dataset, and trained
models publicly available, marking the first open-source release for CT subcortical
segmentation to the best of our knowledge.

Adaptive moment methods such as Adam are widely used due to their robustness, scale invariance, and ease of use. While Adam is often effective on non-stationary
objectives, its fixed decay rates for first- and second-moment estimates can lag
behind rapid changes in gradient statistics or over-smooth under distribution
shift. We introduce Drift-Adam, a drop-in replacement for Adam that adaptively
modulates its moment memories in response to detected drift in the gradient process.
Drift-Adam maintains a streaming estimate of gradient volatility via normalized
increments and uses this signal to adjust the effective decay of the first and second
moments—shortening memory to react quickly after change-points and lengthening
it to reduce variance in stationary phases. The update preserves Adam’s diagonal
rescaling invariance and can be combined with decoupled weight decay. We provide
theory in an online convex setting with piecewise-stationary gradients: Drift-Adam
achieves dynamic regret that scales with the number and magnitude of shifts, while
matching Adam’s guarantees in stationary regimes. The method incurs negligible
compute overhead and adds a single auxiliary statistic per parameter. Across
domain-incremental image classification, curriculum and augmentation schedules,
and reinforcement learning tasks, Drift-Adam improves time-to-target by 10–30%,
reduces early-training instability, and attains stronger final generalization with default
hyperparameters. Code and a reference implementation are provided to facilitate
adoption.

1

2

53
