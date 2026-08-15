---
title: "Contemporary AI lacks the imagination to diverge or negate in science"
person: james-evans
section: by
type: journal-article
year: 2026
date: 2026-06-06
venue: "arXiv (Cornell University)"
authors: "Bao, Honglin, Wu, Siyang, Liu, Xiao, Li, Sida, Cao, Shiyun, Evans, James A."
source_url: https://doi.org/10.48550/arxiv.2606.08251
openalex_id: https://openalex.org/W7164034365
retrieved: 2026-08-13
content: full-text
notes: "preprint version; OpenAlex duplicates merged: W7164034365 W7164446694; full text extracted from the arXiv PDF"
---

# Contemporary AI lacks the imagination to diverge or negate in science

## Full text

Contemporary AI lacks the imagination to
diverge or negate in science
Honglin Bao✉1,2 , Siyang Wu1,2 , Xiao Liu1,2 , Sida Li1 ,
Shiyun Cao2 , and James A. Evans✉1,2
1 Data Science Institute, University of Chicago

arXiv:2606.08251v3 [cs.CY] 10 Aug 2026

2 Knowledge Lab, University of Chicago

✉ Correspondence to: Honglin Bao (honglinbao@uchicago.edu); James A. Evans
(jevans@uchicago.edu).
Bold claims that artificial intelligence will accelerate scientific discovery have raced
ahead of evidence from working scientists 1–3 , yet large-scale, scientist-in-the-loop evidence is scarce. Here we mount the largest evaluation to date, inviting authors of
121,640 recent preprints in biology, medicine, chemistry, and social science to judge
large language model (LLM)-generated ideas derived from their own papers. 6,749 representative scientists returned 25,139 rating sets on novelty, feasibility, probability of
being true, and favorability of adoption. Three patterns emerge. First, non-reasoning
LLMs collapse into a narrow "hivemind" of similar ideas while reasoning models explore a wider hypothesis space, but no model spontaneously proposes null hypotheses,
a move humans make more freely. Second, scientists reward ideas resembling their
own and prize probability over novelty, though social scientists tolerate risk more than
life scientists; senior social scientists are the harshest critics 4 , and their skepticism is
earned, as LLMs falter most in pluralistic fields demanding context-aware interpretation and evolving theories. Third, automated evaluators—LLM-as-a-judge, artificial
metrics, and state-of-the-art (SOTA) models—agree only weakly with expert judgment. Retrieval augmentation and scientist persona prompting yield marginal gains.
A Qwen3-14B reward model we post-trained on human ratings captures nuances of
taste, beats SOTA models by up to 27%, and closes the gap to the consistency of human peer reviewers. An analysis of 39 million papers from 2010 to 2025 links survey
findings to macro-level patterns: following ChatGPT’s release, null claims are sharply
suppressed and ideas contract. Agent-based simulations further suggest that saturated
fields should especially prize human uniqueness and negation. For all the hype, today’s
AI for science remains a collaborator whose imagination, outputs, and judgment benefit
from human grounding.

1

The scientific community is being asked, with unusual urgency, to reorganise discovery
around artificial intelligence. Frontier laboratories now use LLMs to mine the literature,
generate hypotheses, design experiments, and prioritise research directions 1 . The promise is
that machines can navigate vast structured and unstructured knowledge to propose novel,
feasible, and probable ideas at scales no human can match. The risk is that fluent text substitutes for genuine insight: an idea may sound original because the phrasing is unfamiliar,
while still failing to extend, contradict or clarify what is known 5,6 . Whether AI is accelerating discovery, or merely its appearance, cannot be settled by automated benchmarks alone,
because those benchmarks themselves remain unvalidated against the people whose judgment ultimately defines a contribution. Existing algorithmic studies have been evaluated on
small groups of scientists, and a large-scale diagnostic study is still lacking.
To resolve this empirically, we returned to the source. We asked scientific authors to evaluate AI-generated hypotheses derived from their own recent papers, on the premise that
authors are the most informed—and most motivated—judges of ideas that immediately extend their own work. We assembled 121,640 full-text preprints posted after 2023 across
BioRxiv (biology, 68%), MedRxiv (medicine, 20%), SocArXiv, PsyArXiv, EdArXiv (social
science, jointly 9%) and ChemRxiv (chemistry, 3%), and deliberately excluded arXiv, whose
contents dominate LLM pretraining corpora 7–13 (Methods and Supplementary Information
A.1 for pretraining corpus inspection). For each paper, we used the reasoning model o3-mini
to extract the core scientific puzzle, the surrounding factual context, and the author’s own
hypotheses. To prevent leakage of human hypotheses into LLMs, we built a paraphrase-based
detector and discarded any context and puzzle containing sentences whose embedding similarity 14 to the corresponding human hypotheses exceeded a threshold calibrated on 20,000
controlled rephrasings; 99.7% of authors confirmed the extracted context and puzzle, and
98.6% confirmed the extracted hypotheses in our survey. Full details can be found in Methods and Supplementary Information A.4. We then prompted 26 LLMs to propose hypotheses
based solely on the context and puzzle. These models included nineteen non-reasoning chat
models, five reasoning models, and two agentic “deep research” systems across eight providers
(Supplementary Information A.3). Each author received a custom set of the five most semantically distinguishable hypotheses for their paper, balancing responses from reasoning
and chat models, and then rated each on conceptual novelty, empirical feasibility, probability of being true, and adoption favourability. To ensure data reliability, we administered
a comprehension test confirming that all participants understood and correctly applied our
rubrics, and we excluded potentially careless responses (e.g., submissions completed in under
2 minutes with identical ratings across all questions, against an average completion time of
15 minutes). These processes excluded 22.1% of low-quality responses. Fig. 1 summarizes
the pipeline (Methods and Supplementary Information A.5).
Three pieces of evidence emerge from this investigation: human-AI idea differences, expert
judgment, and the failure of (naive) automated judges. We then post-train a reward model on
2

human labels to distill expert judgment into machinery, and analyze a large scientific corpus
alongside agent-based simulations to link the individual AI use captured in the survey to the
macro pattern.

Reasoning broadens the hypothesis space; absence rarely
fills it
Non-reasoning LLMs collapse onto a narrow region of the idea space. Pairwise cosine similarity 14 between hypotheses generated for the same paper is highest within the non-reasoning
group, and higher than that of any other groups (Fig. 2a). Reasoning models, by contrast,
diverge from one another, from non-reasoning models, and from humans. To make this geometric, we treat each generated hypothesis as a displacement vector from a shared origin
defined by its context-and-puzzle embedding, projected to two and three dimensions with
t-SNE (robust to UMAP; Extended Data Figure 1). This enables us to define and visualize
an “idea space,” as shown in Fig. 2b, where we use Google models and human scientists as
an example. Reasoning models occupy a more diverse region than non-reasoning models,
measured by average standard deviations across dimensions (Fig. 2c). The gain is not driven
solely by parameter counts; it tracks whether the model deliberates internally, consistent
with the view that reasoning elicits an implicit ensemble of perspectives 15 . We do not find
evidence that LLMs from the same company exhibit stronger alignment in their generated
ideas, possibly because model architectures, post-training methods, and pretraining corpora
have largely converged across modern LLMs 12,16 .
Diversity, however, is not the same as scientific reach. We trained a high-precision ensemble
classifier (99.5% cross-validated accuracy; Methods and Supplementary Information A.6)
to detect null hypotheses, which contain explicit claims of no relationship, no effect, or no
difference. Humans formulate such hypotheses infrequently, but every LLM in our panel
formulates them less often (Fig. 2d). Even agentic deep research systems with live web
search, which presumably could supply the missing prior that makes a null result interesting, rarely articulate one. The simplest explanation is informative: Scientists are much
more likely to publish and theorize empirical associations and positive findings than nonassociations and null findings. This well-documented selection bias is often referred to as
the “file drawer” problem, in which scientists file away results from failed investigations and
remain unmotivated to publish them 17,18 , and here we provide a new channel, in which
negative-result-driven research is never even initiated. In this way, data about null effects
remain primarily embodied and underrepresented for model training. While the logical move
from “A is associated with B” to “A is not associated with B” is obviously a cognitive primitive of scientific thought 19,20 , LLMs compress their training data, and rare forms of reasoning
become attenuated 21,22 .

3

Scientists discount novelty, prefer their own ideas, and
split by field and seniority
We modeled adoption intention as a function of rated quality and four candidate biases—
human–AI idea similarity, field, seniority, and prior AI use—using a Mundlak (correlated
random-effects) specification that separates within-scientist variation (what makes a particular author favour one of their ideas over another) from between-scientist variation (persistent rater tendencies) 23 . The author-fixed-effect and ordinal-logit specifications give the
same answers (Methods, Supplementary Information A.9, and SI Table 3). The distribution
of scientist characteristics and ratings can be found in Extended Data Figure 3. A nonresponse analysis indicates that respondents are representative of the full sample: we find no
evidence that respondents and non-respondents differ systematically on any observed characteristic. Across all four fields, the distribution of respondents over 117 subtopics closely
matches the distribution of research across those subtopics in the full corpus (Pearson r
= 0.98). See Extended Data Figure 4 and Supplementary Information A.10 for more details. Re-estimating the specifications with weights given by the inverse of the estimated
probability of response yields coefficients that are similar in sign, magnitude, and statistical
significance (Supplementary Information A.11).
From these analyses, four regularities emerge. (i) Scientists prefer ideas that resemble
their own work (within-author coefficient = 1.28, p < 10−3 ; Fig. 3a, Extended Data Table
2). Higher resemblance (captured by the cosine embedding similarity 14 between human and
AI ideas) is associated with higher perceived feasibility (coefficient = 2.29, p < 10−3 ) and
probability (coefficient = 3.42, p < 10−3 ) but lower perceived novelty (coefficient = −3.15,
p < 10−3 ). As a result, adoption willingness rises anyway, a pattern consistent with prior
work on self-similar citation 24,25 (Extended Data Figure 2).
(ii) Senior scientists adopt fewer AI ideas. Using within-field yearly citation percentile
(coefficient = −0.16, p < 0.001), within-field yearly publication percentile (coefficient =
−0.10, p = 0.047), and log-transformed academic age (base e, coefficient = −0.04, p =
0.031)1 to represent seniority/status yields consistent conclusions (Fig. 3b,c, Extended Data
Table 2). Across the paper, we use citations to represent seniority by default. Seniority bias
stems simply from dislike and unwillingness to adopt; it does not affect quality judgments
(Extended Data Figure 2).
Medicine is the most receptive field (8.05% above social science, p < 10−3 , Fig. 3e), consistent
with our observation that medical scientists have the highest AI use (Fig. 3d), measured by
the proportion of prior publications involving AI 26 (Methods and Supplementary Information
A.7), although prior use does not itself predict greater favorability after controlling for quality
1

Measures of seniority and prior AI use all manifest a right-skewed distribution (Extended Data Figure

3).

4

(Extended Data Table 2). Senior social scientists drive the apparent field-level resistance
to AI. Once a field-by-seniority interaction enters the model, field effects vanish (Fig. 3f,
Extended Data Table 3).
(iii) Probability dominates among the three quality dimensions (coefficient = 0.31,
p < 10−3 ). Feasibility (coefficient = 0.13, p < 10−3 ) and novelty (coefficient = 0.12, p <
10−3 ) matter less and roughly equally, suggesting that scientists are risk-averse, preferring to
undertake likely-to-succeed ideas to surprising ones (Fig. 3g, Extended Data Table 2). The
aversion is strongest in biology (coefficient +0.06, p < 10−3 ) and medicine (coefficient +0.06,
p = 0.003), weakest in social science, captured by a field-by-quality-dimension interaction in
the model (Fig. 3h, Extended Data Table 4, and SI Table 4). This pattern likely reflects the
funding-driven model of the life sciences, where the high cost of failed experiments makes
risky ideas especially expensive to pursue.
(iv) LLMs falter most in pluralistic fields like the social sciences. These biases
are not unfounded. With each field receiving a balanced sample from all LLMs, AI ideas
in social science were rated as less novel (Fig. 3i), less feasible (Fig. 3j) and less probable
(Fig. 3k) than in any other domain. These judges are not subject to biases such as seniority
(Extended Data Figure 2). One interpretation is epistemic: in pluralistic fields like the social
sciences, where targets of research are themselves contested — competing interpretations,
context-dependent findings, evolving theories — scientists prize the surprising (Fig. 3h), and
an AI system optimized to reproduce the modal pattern of its training data has little to
converge on. Where there is no consensus to imitate, imitation looks shallow.

Automated evaluators do not yet measure scientific quality
A vast methodological literature treats LLM-as-a-judge, n-gram novelty, semantic distance,
conditional perplexity, cross entropy, natural-language inference, and literature-grounded
novelty checkers as proxies for expert assessment of research ideas 27,28 . With 25,139 expert
ratings as ground truth, we can ask whether any of these proxies recover expert judgment.
None performs well. We first prompted Gemini 2.5 Flash, DeepSeek R1 and OpenAI’s o4mini Deep Research model with the same rubric and rating scale shown to human authors,
with and without an injected scientist persona, operationalized by scientists’ own ideas.
The retrieval-augmented Deep Research model achieved the highest correlation with human
judgment, but no model exceeded r = 0.35 on any dimension (Fig. 4a). Persona prompting
helped in most settings, but not significantly for the retrieval-based Deep Research model. It
even reduced novelty accuracy where externally retrieved prior work and an internal persona
disagreed about what counts as new. This failure represents a strong central tendency.
Across all three judges, LLM ratings cluster around the upper-middle of the scale. Adding
explicit encouragement to assign extreme scores only increases the standard deviation of
5

ratings by 0.33 on a 1–9 scale (Fig. 4b and Supplementary Information B.1). Across all
settings, matching human experts’ probability of assigning truth to hypotheses was the
easiest dimension on which LLMs performed.
To probe a broader range of evaluators, including state-of-the-art (SOTA) reward models, we
follow standard practice and convert human ratings into within-scientist pairwise preferences.
We construct a held-out test set of 5,000 pairs with transitive relations removed (i.e., we
keep hypothesis pairs h1–h2 and h2–h3, but exclude h1–h3). On this set, we evaluate the
judgment of novelty2 across a wide range of established novelty assessment models and
metrics, including LLM-as-a-judge (as discussed above), 2-gram and 3-gram novelty, lengthnormalized cross-entropy, conditional perplexity, semantic distance, the natural language
inference-based entailment score, the SOTA score-based idea judge GraphEval-GNN 29 , and
the top three reward models that learn human preferences available on RewardBench 30 .
Each method follows the same protocol: score both items in a pair, determine the predicted
winner, and count the prediction as correct if its direction matches human judgment. All
methods perform near chance (Fig. 4c). LLM-as-a-judge fares especially poorly, as its
central-tendency bias always produces near-identical ratings of mediocrity.

Reward models trained on expert preference recover the
gap
On the within-scientist pairwise preference dataset, we post-trained a Qwen3-14B model under a Bradley–Terry objective augmented with a margin term proportional to the rating gap
(Supplementary Information A.13). Joint training across novelty, feasibility and probability
did not hurt per-dimension accuracy, indicating that the three dimensions are empirically
separable in expert judgment (Extended Data Table 5).
Scientific domain-specific models slightly outperformed a single general model when indomain data were abundant (Extended Data Table 6), suggesting that fields share a common
evaluative core and carry taste nuances that are not ineffable, but can be statistically captured. In the held-out test set, the biology model reached 69% pairwise accuracy on novelty,
62% on feasibility and 67% on probability, and the social-science model reached 64%, 62%
and 67%. For comparison, the top three models available on RewardBench 30 hover at chance
on this task across dimensions: the best, Skywork-Reward-V2-Qwen3-8B, scores 53%, 55%
and 49% across feasibility, probability, and novelty, and the o4-mini Deep Research judge
scores 41%, 55% and 43% (Extended Data Table 1). Our models improve on the strongest
baselines by up to 27% (+14 percentage points on average across three dimensions).
We benchmark these numbers against the realistic reference of human agreement. From
2

Ties are removed prior to evaluation.

6

26,731 OpenReview submissions to 46 conferences (2017–2025; spanning computer science,
physics, medicine and the social sciences; Methods and Supplementary Information A.8),
we constructed within-conference pairwise comparisons and measured how often a nonoverlapping-position reviewer agreed with the direction of a reference-position reviewer’s
preference. Averaged over 1,000 randomised position controls, agreement was 61.0 ± 0.1%.
Because same-position reviewers are distinct individuals rather than the same person, this
rate sets a floor that any reliable model should clear. Our reward models exceed it. Existing
automated evaluators do not.

Reckless AI use renders human knowledge less divergent
and less prone to negate
We probe the consequences of AI for human knowledge through two experiments (Fig. 5):
a large-scale scientific corpus analysis and a counterfactual simulation, and we find that
individual-level findings from the survey are well linked to the macro pattern. Focusing on
medicine and social science, fields our survey shows differ strongly in how much scientists
favor AI, we assembled all 38,863,847 papers published between 2010 and 2025 from OpenAlex. Applying the AI-use detector 26 to titles and abstracts (Fig. 5a), we find AI is indeed
more popular in medicine, either as a method or topic, and this predates LLMs. Traditional
AI had already reshaped the biomedical field. A similar pattern appears in the social sciences. AI-focused research began expanding in 2017, coinciding with the emergence of the
Transformer architecture. This is a conservative estimate, insofar as researchers may use AI
for research quietly (e.g., a writing tool) without reporting it explicitly as a method or topic.
We then track papers reporting zero null claims by applying our null-claim classifier to every
sentence in an abstract (Fig. 5b). We define all-significant papers as those containing zero
detected null claims. Social science initially had more all-significant papers than medicine,
but ChatGPT’s release in November 2022 reversed this relationship: LLMs sharply raised
the all-significant share in both fields, and with greater AI use in medicine, null claims are
suppressed more strongly in medicine than in social science. Our results align well with prior
work with LLM/human annotation methods: where earlier estimates 20 put significant-only
papers at 77% in political science (2010–2024), we find on average 74% in medicine and 77%
in social science (2010–2025). Notably, this share was declining before LLMs, plausibly due to
reforms of pre-registration, the replication-crisis reckoning, and the open-science movement.
The post-2022 reversal undoes a decade of progress, drawing it below the old baseline.
Embedding all papers with SPECTER2 31 , the SOTA embedding model specifically for scientific knowledge, we operationalize a field as a circle with radius given by the average
Euclidean distance from all papers to the center in the 768 dimensions of the model. Then
we compute two quantities 26 : center drift, the distance of the center in each year from its
7

2010 position (Fig. 5c), and knowledge extension, the year-over-year growth ratio of the
radius (Fig. 5d). LLM use drives pronounced center drift, stronger in medicine, plausibly toward data-rich topics 26 ; LLMs initially expand the knowledge space but ultimately
contract it in medicine 26 .
To provide an existence proof of the consequences of reckless AI use, we build stylized
agent-based simulations where a collection of studies estimates a space of true effects {θj },
tracing the many questions a field could ask, and treating AI as a fast but error-correlated
instrument. Each study i reports θ̂i,j = θj + Bj + εi,j : the uncorrelated part of the error
εi,j is reduced by AI-driven throughput (the productivity premium), but a shared bias Bj
— together with the correlated part of εi,j , alike across studies because they all use AI —
never averages away (the disadvantage). As shown in Fig. 5e, the key move is to treat the
null and its significant part not as two rival hypotheses but as the two halves of a single
bell curve, split at the middle. Suppressing nulls is then literally the deletion of part of the
lower half, which unbalances the two sides and pushes the published mean upward while
making the shrunken literature look, misleadingly, more precise. This displacement depends
on where a question’s true effect sits. Large, robust effects are barely touched as little sat in
the deleted half to begin with, whereas small effects, unfortunately the most common kind,
are distorted most, as deleting one half destroys the balance required to cancel a borderline
effect. A single knob, the AI share a ∈ [0, 1], raises throughput but also raises cross-study
correlation ρ, blind-spot bias Bh , and null-suppression rate s. Three results follow. First, in
mature fields, where studies are already abundant, throughput adds little while the shared
(or correlated) part across studies does the real damage, shifting optimal adoption leftward
(Fig. 5f). Second, the averageable-variance band narrows while the shared/correlated part
widens with more AI use, eventually raising total error (Fig. 5g). Finally, null suppression
deepens the decline in net knowledge, as shown by comparing two counterfactual worlds: one
with the null-suppression channel on (0.47) and one with it off (0.76; Fig. 5h). See Methods
and Supplementary Information A.14 for details.

Discussion
The largest expert audit of AI for science to date returns a sober verdict. Non-reasoning
LLMs share a hivemind. Reasoning models broaden the hypothesis space but rarely populate
it with absences. Expert evaluators bring their own systematic biases. LLMs are not good at
research in pluralistic fields with competing interpretations and context-dependent findings.
The automated infrastructure built to substitute for expert judgment cannot yet do so.
Macro patterns closely echo our survey findings, reinforcing the concern that reckless use of
AI harms science. Three implications follow.
First, claims of AI-driven scientific acceleration cannot be adjudicated on benchmark performance, fluency, or demonstration alone. Discovery requires novelty, feasibility, plausibility
8

and adoption by domain experts, and only the last anchors the others.
Second, automated evaluation in its current form risks generating an optimistic literature
about itself. Judges and judged are drawn from the same distribution, and their agreement
reflects shared priors more than shared standards.
Third, the shortfall in null-hypothesis formulation is not an incidental gap; it indexes a
structural feature of how LLMs learn. Pretraining corpora are overwhelmingly populated
by claims of what is the case, amplified by a publication system that suppresses null results 20 . A claim that “A is not associated with B” is informationally richer than its positive
counterpart: it presupposes a backdrop of prior expectation that makes the absence surprising 32 . Generating it, therefore, requires not merely plausible continuation but a theory
of the field’s expected contrast, a piece of meta-knowledge that flat text underdetermines.
The deeper portion of negative knowledge, including what has been ruled out, what fails
to replicate, and what does not work, accumulates in the unwritten residues of embodied
practice: failed experiments, rejected grants, abandoned notebooks, and the tacit kill lists
circulated in laboratories. None of this enters training. Reasoning helps because deliberation
simulates the contrast structure that flat text omits 15 , but reasoning over a corpus already
pruned of negation cannot recover what was never recorded. The human asymmetry that
Adams and colleagues call our blindness to subtractive change 19 is sharper still in machines:
ours is a bias of attention, theirs is a bias of evidence. Until pretraining ingests these absences through deliberate elicitation of expert null intuitions, registered reports, replication
archives, and laboratory notebooks of dead ends, the asymmetry will persist.
A deeper limit, however, is not negation but appetite. Today’s models are optimised to
predict, not to wonder. Their generative behaviour is anchored to the distribution of what
has been said, not to the marginal value of what could be learned next. As we have argued
elsewhere 2 , the next phase of scientific automation will require encoding computational curiosity—an intrinsic drive that prizes anomaly, contradiction, and absence, and that pulls a
system toward data it has not yet seen rather than toward the centre of data it has 33 . A
curious system would propose null hypotheses precisely because nulls are where falsification
lives. It would probe the edges of consensus rather than its centre. And it would treat the
construction of new measurements, instruments, interventions and natural experiments as
part of the hypothesis space, not as exogenous to it. Until AI is routinely directed toward
violations of its expectations and to strategically accumulate data to facilitate abductive,
surprise-driven discovery, it cannot generate sustainable advances 32 . Hypothesis generators
that draw only from the published literature are condemned to recombination 34 . Only systems that actively reach into the world can extend the literature rather than recompress
it.
Our reward models recover the gap to peer-review consistency, but the residual is not a
quantity to be optimised away. What experts contribute is not only a verdict on individual
9

ideas but the collective construction of criteria by which ideas come to be judged. Novelty,
feasibility, and probability are not fixed features of a hypothesis; they are functions of an
evolving disciplinary horizon that communities continuously discover, contest, and revise as
their fields progress. Distilling current taste into a model is feasible, as our results show.
Distilling the practice that lets taste evolve is harder, and is the work for which expert
communities exist.
AI for discovery, on present evidence, is a collaborator: it expands the search, surfaces
candidate directions, and assists ideation. The work of framing the question, recognising
what kind of result would matter, contesting the categories themselves, and so of building
and rebuilding the epistemic infrastructure on which useful knowledge depends, remains, for
now, usefully human.

Materials and Methods
Full details of Materials and Methods are reported in Supplementary Information A.
Corpus and human-in-the-loop survey. From six non-arXiv preprint platforms (BioRxiv
68%, MedRxiv 20%, ChemRxiv 3%, plus a 9% social-science cluster of PsyArXiv/EdArXiv/SocArXiv), we assembled 121,640 post-2023 empirical papers; arXiv was excluded because
73% of its papers fall outside the classical hypothesis-testing tradition 35,36 and arXiv full
text dominates standard LLM pretraining corpora (LLaMA, Dolma, The Pile, RedPajama,
Common Pile) while other platforms are largely excluded – 10-gram overlap against a 10Btoken Dolma v1.6 pretraining sample matched only 4 of 8,000 random paragraphs, all false
positives on inspection. For each paper, o3-mini extracted the author’s explicit hypotheses
and, separately, the scientific puzzle and surrounding context rewritten from the introduction and related-work sections (parsed via GROBID); leakage was suppressed by dropping
any extracted context/puzzle as long as one sentence exceeded an MPNet 14 cosine similarity
threshold of 0.82 (calibrated on 20,000 GPT-4.1 paraphrases of 1,000 human hypotheses, 95%
recall) against the paper’s human hypotheses, with post-hoc author satisfaction of 98.62% on
hypotheses and 99.70% on context/puzzle. We then prompted 26 representative LLMs from
eight providers, spanning OpenAI, LLaMA, Gemma, Phi, Mistral, DeepSeek, Qwen, Grok,
and Gemini model families, to generate ideas. For each paper we sent the authors five distinguishable AI-generated hypotheses and the authors rated each on novelty, feasibility, probability, and adoption favorability after passing a comprehension check of the rubrics. In total
6,749 scientists participated, yielding 25,139 valid four-dimensional evaluations (University
of Chicago IRB25-1372). Full procedures in Supplementary Information A.1, A.2, A.3, A.4,
and A.5.
Null-hypothesis and AI-exposure classifiers. Two auxiliary classifiers support the
analysis. The null-hypothesis classifier feeds TF-IDF tokens (NLTK Treebank tokenization;
10

stopwords retained to preserve negation cues such as “no effect”) into an ensemble of two linear
(support vector machine, logistic regression) and two nonlinear (random forest, gradient
boosting) base learners, trained on 2,000 o3-mini-generated labels (null vs. not null) validated
at 100% agreement against two human annotators on a 200-instance manual check; 5-fold
cross-validation accuracy is 99.5%. AI exposure of each participating scientist is computed
by the proportion of prior papers involving AI from their 848,750 papers using the fine-tuned
BERT title–abstract classifier 26 (F1 ≈ 0.875 against expert annotation with Fleiss’ κ = 0.96);
a Gemini 2.5 Flash re-annotation of AI use yields 98.80% agreement. See Supplementary
Information A.6 and A.7.
Adoption regression. We estimate adoption favorability as a function of scientist-rated
novelty, feasibility, probability, and potential biases using a correlated random-effects (Mundlak) linear specification 23 that decomposes each rating into a within-scientist deviation
(ratingij − ratingi ) and a scientist-level mean ratingi , isolating which drives a given scientist’s own adoption decisions from persistent cross-scientist-level differences. Sources of
bias include seniority (within-field yearly citation percentile; robust to within-field yearly
publication-count percentile and log-academic-age proxies), prior AI use (see above), human–
AI idea cosine similarity (using the MPNet embedding model 14 ), and field. Average marginal
predictions are reported with clustered robust standard errors and conclusions replicate under an author-fixed-effect specification, a Mundlak-decomposed ordered logistic model, and
three additional specifications including interaction effects between field, seniority, and quality dimensions (Supplementary Information A.9). Non-response does not appear to bias
the sample. Respondents and non-respondents are statistically indistinguishable on every
observed characteristic, and in all four fields the distribution of respondents across the 117
subtopics closely tracks the distribution of research in the full corpus (Pearson r=0.98; Extended Data Figure 4 and Supplementary Information A.10). Re-estimating the main specification with weights equal to the inverse estimated probability of response yields coefficients
similar in sign, magnitude, and statistical significance (Supplementary Information A.11).
Novelty metrics. We benchmark seven operationalizations of novelty against author novelty ratings: semantic distance 1−cos(eg , ec ) where cos(eg , ec ) is the cosine similarity between
MPNet embeddings of the generated idea g and the puzzle+context c; Jaccard-complement
bi-gram and tri-gram divergence of g and c; length-normalized cross-entropy of g’s tokens under the empirical token distribution of c; natural language inference-based derivation pe − pc
from DeBERTa 37 (the probability of entailment minus contradiction)—lower, more novel;
conditional model perplexity of g given c averaged across four well aligned 7B base models
(Qwen-7B, Mistral-7B-v0.1, LLaMA-2-7B, and DeepSeek-LLM-7B-base); and GraphEval 29 ,
a graph-based LLM idea evaluator that links g via BERT-similarity edges into an idea graph,
and predicts the decision probability distribution via aggregated neighbor node representations; we collapse its four-way output to an overall score P (Spotlight)+ P (Oral)+P (Poster).
Full formulations are shown in Supplementary Information A.12.
11

Reward model and human-agreement benchmark. We trained a multi-dimensional reward model r(y) = (rnov , rfeas , rprob ) on the four consecutive pairs (h1 , h2 ), (h2 , h3 ), (h3 , h4 ), (h4 , h5 )
from each scientist’s five-hypothesis ranking; the non-consecutive pairs are deducible by
transitivity and induce severe overfitting (training accuracy ≈ 90%, test < 60%). The
Bradley–Terry loss incorporates both preference direction and score-gap margin. An 80trial grid search over learning rate and margin weight selects hyperparameters as well as
the backbone (Qwen3-14B). As an interpretive baseline, we benchmark against the agreement between non-overlapping human reviewers across 26,731 OpenReview submissions to
46 venues 2017–2025 38 : a randomized pairwise direction check yields 61.0% ± 0.1% consistency. LLM-as-a-judge, SOTA models, and popular metrics fall below this human baseline
on our task (Supplementary Information A.8 and A.13).
Simulation model. We model a field as pooling many noisy estimates of a whole space of
true effects {θj } that trace the many questions a field could ask, each with a non-negative
true magnitude, most small and a few large. We then track the mean-squared error (MSE) of
the field’s pooled estimate, which for each question decomposes into an averageable variance
term, a shared bias, and an error-correlation floor. AI adoption is a single dial a ∈ [0, 1]
that moves four primitives: it raises throughput and productivity n (beneficial) but also the
cross-study error correlation ρ, the shared blind-spot bias Bh , and the rate s at which null
results get suppressed, all of which are harmful for scientific understanding. The last of these
acts through a selection bias we formalize by treating a study’s null and its positive part
as two halves of a single bell curve split down the middle. Suppressing nulls deletes part of
the lower half of the symmetrical curve, unbalancing the two sides so the published mean
is pushed upward. This displacement depends on where a question’s true effect sits. Large
effects are barely touched while small effects, by far the most common kind, are distorted
most. The key asymmetry is that throughput is the only channel reaching the averageable
term, and it does so with diminishing returns (∼ 1/n2 ), while the three harms sit in the
irreducible part. Net knowledge V = 1 − MSE is therefore a trade-off between benefits and
harms. This model yields three findings: (1) the optimal AI share a∗ is interior, so a human–
AI mix dominates full automation; (2) a∗ is lower in mature fields because AI’s throughput
gains matter most in young, study-poor fields and least where evidence is abundant; and (3)
knowledge collapse at high adoption steepens as null suppression intensifies. Details can be
found in Supplementary Information A.14.

Acknowledgements
We thank Misha Teplitskiy, Julia Koschinsky, Pengda Wang, Beichen Lu, Kim Weeden,
Robert Ward, Zhen Zhang, Junsol Kim, Gio Choi, Austin Kozlowski, Philip N. Cohen,
Laura K. Nelson, Juan Pablo Pardo-Guerra, Alexander C. Furnas, Yian Yin, Alex Yan,
and participants at Yale AI for Social Science Methods Workshop for discussion. We thank
12

Knowledge Lab members and the many scientists who participated in, and wrote to us about,
the survey, as well as the Bluesky community, whose debates sharpened the study’s design.
Computation used the University of Chicago Midway / Data Science Institute Research
Computing Cluster.

Author Contributions
H.B. and J.A.E. designed the study. H.B. drafted the survey. S.C. and H.B. implemented the
survey, with all authors contributing to its distribution. S.W., S.L., X.L. and H.B. designed
the reward-model experiments. H.B. conducted data analysis, simulation models, and wrote
the first draft. S.W., X.L., S.L., and J.A.E. contributed to revising the manuscript. J.A.E.
supervised the work.

Competing Interests
J.A.E. is affiliated with Google.

Data and Code Availability
Aggregated, de-identified ratings, the trained reward-model checkpoints, and pipeline code
have been released at the project repository. Per IRB25-1372, individual identifiers will not
be released.

References
1

Wang, H. et al. Scientific discovery in the age of artificial intelligence. Nature 620, 47–60
(2023).

2

Evans, J. & Duede, E. After science. Science 390, eaec7650 (2025).

3

Wang, D. Ai agents are ‘aeroplanes for the mind’: Five ways to ensure that scientists are
responsible pilots. Nature 651, 32–34 (2026).

4

Cui, H., Wu, L. & Evans, J. A. Aging and the narrowing of scientific innovation. Science
392, 588–591 (2026).

5

Zhang, Y. et al. Noveltybench: Evaluating language models for humanlike diversity.
COLM (2025).

13

6

Kusumegi, K. et al. Scientific production in the era of large language models. Science
390, 1240–1243 (2025).

7

Touvron, H. et al. Llama: Open and efficient foundation language models. arXiv preprint
arXiv:2302.13971 (2023).

8

Soldaini, L. et al. Dolma: An open corpus of three trillion tokens for language model
pretraining research. In Proceedings of the 62nd Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers), 15725–15788 (2024).

9

Gao, L. et al. The pile: An 800gb dataset of diverse text for language modeling. arXiv
preprint arXiv:2101.00027 (2020).

10

Weber, M. et al. Redpajama: An open dataset for training large language models.
NeurIPS 37, 116462–116492 (2024).

11

Kandpal, N. et al. The common pile v0.1: An 8tb dataset of public domain and openly
licensed text. arXiv preprint arXiv:2506.05209 (2025).

12

Wolfram, C. & Schein, A. Layers at similar depths generate similar activations across llm
architectures. COLM (2025).

13

Wu, S., Bao, H., Li, S., Holtzman, A. & Evans, J. A. Mapping overlaps in benchmarks
through perplexity in the wild. ICLR (2026).

14

Song, K., Tan, X., Qin, T., Lu, J. & Liu, T.-Y. Mpnet: Masked and permuted pre-training
for language understanding. NeurIPS 33, 16857–16867 (2020).

15

Kim, J., Lai, S., Scherrer, N., Evans, J. et al. Reasoning models generate societies of
thought. arXiv preprint arXiv:2601.10825 (2026).

16

Wu, S., Bao, H., Kunievsky, N. & Evans, J. A. Automatically advancing llm expertise in
technology judgment. arXiv preprint arXiv:2505.12452 (2025).

17

Rosenthal, R. The file drawer problem and tolerance for null results. Psychological Bulletin
86, 638 (1979).

18

Chen, H., Rider, C. I., Jurgens, D. & Teplitskiy, M. Geographical disparities in navigating rejection in science drive disparities in its file drawer. In Academy of Management
Proceedings, vol. 2025, 18866 (2025).

19

Adams, G. S., Converse, B. A., Hales, A. H. & Klotz, L. E. People systematically overlook
subtractive changes. Nature 592, 258–261 (2021).

14

20

Briggs, R. C., Mellon, J. & Arel-Bundock, V. It must be very hard to publish null results.
Tech. Rep., I4R Discussion Paper Series (2026).

21

Sun, K., Xu, Y., Zha, H., Liu, Y. & Dong, X. L. Head-to-tail: How knowledgeable are
large language models (llms)? aka will llms replace knowledge graphs? In NAACL,
311–325 (2024).

22

Jaiswal, A. et al. Compressing llms: The truth is rarely pure and never simple. ICLR
(2024).

23

Schunck, R. Within and between estimates in random-effects models: Advantages and
drawbacks of correlated random effects and hybrid models. The Stata Journal 13, 65–76
(2013).

24

Bao, H. & Teplitskiy, M. A simulation-based analysis of the impact of rhetorical citations
in science. Nature Communications 15, 431 (2024).

25

Katz, J. S. The self-similar science system. Research Policy 28, 501–517 (1999).

26

Hao, Q., Xu, F., Li, Y. & Evans, J. Artificial intelligence tools expand scientists’ impact
but contract science’s focus. Nature 1–7 (2026).

27

Shahid, S. et al. Literature-grounded novelty assessment of scientific ideas. In Proceedings
of the Fifth Workshop on Scholarly Document Processing, 96–113 (2025).

28

Moussa, H. N. et al. Scholareval: Research idea evaluation grounded in literature. arXiv
preprint arXiv:2510.16234 (Feb, 2026).

29

Feng, T., Sun, Y. & You, J. Grapheval: A lightweight graph-based llm framework for
idea evaluation. ICLR (2025).

30

Malik, S. et al. Rewardbench 2: Advancing reward model evaluation. arXiv preprint
arXiv:2506.01937 (2025).

31

Singh, A., D’Arcy, M., Cohan, A., Downey, D. & Feldman, S. Scirepeval: A multi-format
benchmark for scientific document representations. In Conference on Empirical Methods
in Natural Language Processing (2022).

32

Shi, F. & Evans, J. Surprising combinations of research contents and contexts are related
to impact and emerge with scientific outsiders from distant disciplines. Nature Communications 14, 1641 (2023).

33

Loewenstein, G. The psychology of curiosity: A review and reinterpretation. Psychological
Bulletin 116, 75–98 (1994).
15

34

Farrell, H., Gopnik, A., Shalizi, C. & Evans, J. Large ai models are cultural and social
technologies. Science 387, 1153–1156 (2025).

35

Cockburn, A., Dragicevic, P., Besançon, L. & Gutwin, C. Threats of a replication crisis
in empirical computer science. Communications of the ACM 63, 70–79 (2020).

36

Denning, P. J. The science in computer science. Communications of the ACM 56, 35–38
(2013).

37

He, P., Liu, X., Gao, J. & Chen, W. Deberta: Decoding-enhanced bert with disentangled
attention. ICLR (2021).

38

Bao, H., Wu, S., Choi, J., Mao, Y. & Evans, J. A. Language models surface the unwritten
code of science and society. arXiv preprint arXiv:2505.18942 (2025).

16

Figure 1: An expert-audit pipeline for AI-generated research ideas. Full-text
preprints (n = 121,640) from six non-arXiv platforms feed an extraction stage that recovers
(i) the author’s hypotheses, (ii) the surrounding factual context, and (iii) the core scientific
puzzle, with paraphrase-based leakage detection between (i), (ii), and (iii). LLMs propose
hypotheses from the context-and-puzzle alone; a custom set of hypotheses is sent to the
authors by email, who pass an understanding test before rating each on the quality of extraction, novelty, empirical feasibility, probability of being true, and favorability of adoption.

17

Figure 2: Reasoning broadens the hypothesis space; null reasoning rarely fills it.
a, Pairwise cosine similarity of hypotheses generated for the same paper, by group. Nonreasoning LLMs are more similar to each other (the “artificial hivemind”, p<0.001); reasoning
models diverge from non-reasoning models, humans, and each other. b, geometrically, we
treat each hypothesis as a displacement from a common context-and-puzzle origin in the
embedding space (length and width of a model are represented by the corresponding confidence interval of mean for each dimension. We use Google models based on 10000 random
papers as an example). c, reasoning models cover a substantially more diverse region than
non-reasoning models in both 2D (p<0.010) and 3D (p= 0.018) spaces. t-SNE for dimension reduction. UMAP-based replication in Extended Data Figure 1. No robust conclusions
can be drawn comparing reasoning models and humans. d, Rate of explicit null-hypothesis
formulation, by source. Humans are imperfect at negative reasoning, but every LLM is
markedly worse (p<0.001), including the agentic deep-research system with live web access.
Error bars = 95% CI.

18

b

c

2.5

citation

3.2

publication

3.1
3.0

0.0

Idea similarity (within)

3.2

***

***

**

bio

chem

3.0

med

Field

soc

Status

1.0

0

g

3.4

3.2

3.0
bio

chem

med

Field

3.0
2.5
2.0

soc

lty

nove

ility
feasib

−2

0

Feasibility

***

***

***

5.5

5.0

*

bio

chem

med

Field

soc

bio

chem med

soc overall

Field

0.36
0.32

***

**

0.28
0.24
bio

chem

med

soc

Field

k
***

5.0

2

Rating (within)

j
5.5

0.05

h

y

a
ob
pr

3.5

0.06

0.04

4

it
bil

4.0

i
Novelty

2

Age (log)

Probability

Adoption

3.4

0.5

f

Adoption (junior)

e

3.1
3.0

0.0

Adoption

−0.5

3.2

Favorability of prob.

3.0

d

3.3

Prior AI use

3.3

Adoption

3.5

Adoption

Adoption

a

bio

chem

med

Field

soc

5.5

***

5.0
***
bio

chem

med

soc

Field

Figure 3: Scientists discount novelty, prefer ideas resembling their own, and split
by field and seniority. Marginal predictions from the Mundlak adoption model are shown,
controlling for rated quality. a, within-scientist similarity to the author’s own ideas is the
strongest single driver of adoption. b, status, represented by within-field citation/publication percentile, lowers adoption. c, seniority, represented by log-transformed academic age,
lowers adoption. d, prior-AI use across fields. It is not a significant predictor of adoption.
e, social scientists adopt the least. f, once a field-by-seniority interaction is included in
the model, the field main effects vanish. Among junior scientists at the baseline citation
percentile of 0 (i.e., without seniority-induced decay), no statistically significant differences
in adoption are observed across fields. Senior scientists in every field are more skeptical,
with the decay being most pronounced in the social sciences. g, Effect of within-scientist
deviations in rated quality on adoption: probability ≫ feasibility ≈ novelty. h, biology and
medicine show larger probability slopes than social science. i to k, quality ratings of LLM
ideas. Social science is the weakest domain on novelty (i), feasibility (j) and probability
(k). All fields’ quality and adoption remain mid-scale. Baseline = social science. Uncertainty intervals: 2.5/97.5 percentiles of 300 draws from the asymptotic distribution of the
estimated coefficients N (β̂, V̂ ) with cluster-robust V̂ . ∗ p < 0.05; ∗∗ p < 0.01; ∗∗∗ p < 0.001.
Error bars/bands = 95% CI.

19

Figure 4: Automated evaluators do not yet measure scientific quality. a, Pearson
correlation between LLM-judge ratings and human ratings on the full dataset, by dimension
and judge, with and without injected scientist persona. The retrieval-augmented Deep Research judge is the best. Persona injection slightly helps. Yet no setting exceeds r = 0.35.
b, Calibration of LLM judges against human ratings on the full dataset. If LLM ratings
track humans, points would lie on the gray diagonal; instead, all three judges exhibit a
strong central tendency with narrow inter-quartile (25% and 75%) ranges, and rarely issue
the extreme scores that human raters routinely assign. c, Accuracy of novelty judgment on
the held-out pairwise test set: LLM-as-a-judge, SOTA models, and popular metrics perform
poorly. Our models perform better (p<0.001). Error bars = 95% CI.
20

Figure 5: AI renders human knowledge less divergent and less prone to negation.
Based on 39 million scientific papers in medicine and social science from 2010 to 2025: a,
medicine uses more AI. b, after the release of ChatGPT, the share of papers without any
null claims rises sharply. c, after the release of ChatGPT, the field’s center moves rapidly
away from its 2010 position. d, AI initially expands the knowledge space but then collapses
it in medicine. Based on simulation studies: e, an illustration of model design showing how
AI suppresses null hypotheses. f, the more mature a field, the smaller the optimal level of
AI use. g, in AI-assisted research, errors become correlated and blind spots shared, while
higher productivity offsets random noise, though at diminishing marginal returns as AI use
increases. h, toggling the AI-suppresses-null-findings mechanism on and off shows that the
loss of null findings substantially collapses net knowledge.

21

Extended Data Figures and Tables

Variance (UMAP)

4

reasoning
human
non-reasoning

p = 0.010

3

p = 0.006

2
1
0

Two-dimensional

Three-dimensional

Extended Data Figure 1. Reasoning models generate broader perspectives than
non-reasoning models. This is the replication of Figure 2 panel c in the main paper under a different dimension reduction method (UMAP). Reasoning models generate broader
perspectives than non-reasoning models in the embedding space and this conclusion is statistically significant.

22

2

1

1

0
1

p < 0.001

2

1
2

0.5

0.0

0
1
2

0.5

0.0

0.5

2

1

1

1

1
2

p = 0.16

0
1
2

0.0

0.5

Seniority

1.0

Probability

2

p = 0.43

0.0

Idea similarity (within)

2

0

p < 0.001

1

Idea similarity (within)

Feasibility

Novelty

p < 0.001

0

Idea similarity (within)

b

2

Probability

2

Feasibility

Novelty

a

0

p = 0.25

1
2

0.0

0.5

Seniority

1.0

0.0

0.5

Seniority

1.0

Extended Data Figure 2. Human-AI idea alignment shapes quality judgment,
but the seniority bias only shapes adoption. Regressing the potential sources of AIidea bias from humans against quality judgment (marginal predictions are shown): a, AI
ideas that resemble what evaluators have produced themselves are rated as more feasible
and more likely to be true, yet less novel. Authors who have conducted similar work are
more likely to view the idea as both implementable and valid. However, alignment with
one’s own ideas penalizes perceived novelty, since what overlaps with one’s own thinking is,
by construction, less surprising. b, seniority only affects the favorability of adoption, not
the judgment of quality (non-significant weak effects). The effect of human bias toward AI
ideas reported in the main paper is the additional impact after controlling for quality. Error
bands = 95% CI.

23

Extended Data Figure 3. Distribution of variables. Across fields, the human-rated
quality dimensions (novelty, feasibility, and probability) share a similar shape that is approximately normal, whereas adoption favorability departs from normality and is right-skewed.
The seniority measures (yearly citations, yearly publications, and age) and prior AI use likewise exhibit right-skewed distributions, visualized via Gaussian kernel density estimation.
These patterns motivate the statistical transformations applied to these variables in the
main text.

24

Extended Data Figure 4. No significant differences between respondent and
nonrespondent researchers. Across biology, medicine, chemistry, and social science, we
find no evidence that survey respondents differ systematically from nonrespondents in age
(panel a), productivity (panel b), citations (panel c), or prior AI use (panel d). Error
bars=95%. Respondents are also representative at the subtopic level: in all four fields the
distribution of respondents across the 117 subtopics closely tracks the distribution of research
in the overall corpus (Pearson r=0.98, panel e, and Supplementary Information A.10). The
117 subtopics are ordered left to right by their within-field percentile in the overall corpus
(black line); the corresponding percentile among respondent scientists is shown in red.

25

Extended Data Table 1. Pairwise judgment accuracy across models and settings.
On a held-out set of 5,000 human preference pairs, we evaluate state-of-the-art reward models
and two LLM-as-a-judge configurations: (i) direct comparison pairwise prompting, in which
the judge is asked which idea is better, and (ii) rating-based pairwise judgment, in which the
judge assigns individual scores that are subsequently converted into a pairwise preference.
All reward models, including ours, follow the rating-based (score-then-convert) protocol (that
is how they are trained). Our model consistently outperforms these models. Notably, the
direct-comparison LLM-as-a-judge exhibits strong framing bias: its predictions are unstable
under logically equivalent rephrasings of the same query.
Model

Label

Feasibility

Probability

Novelty

Covert Ratings

nicolinho/QRMGemma-2-27B
SkyworkReward-V2Qwen3-8B
SkyworkReward-V2Llama-3.1-8B
OpenAI o4-mini
Deep Research
DeepSeek R1
Gemini 2.5
Flash
OpenAI o4-mini
Deep Research
DeepSeek R1

SOTA Reward
model
SOTA Reward
model

0.51

0.51

0.47

Y

0.53

0.55

0.49

Y

SOTA Reward
model

0.50

0.53

0.51

Y

LLM-as-a-judge

0.41

0.55

0.43

Y

LLM-as-a-judge
LLM-as-a-judge

0.40
0.36

0.48
0.43

0.41
0.30

Y
Y

LLM-as-a-judge

0.59

0.61

0.61

LLM-as-a-judge

0.56

0.60

0.55

LLM-as-a-judge

0.58

0.60

0.53

N (direct
comparison)
N (direct
comparison)
N (direct
comparison)

Gemini 2.5
Flash

26

Extended Data Table 2. Factors that impact adoption. Major conclusions are robust
across seniority measures (within field yearly citation/publication percentile and academic
age). We use the citation measure to represent seniority by default. Across the paper, prior
AI use is also log-transformed due to its long-tailed distribution.

Intercept
Biology
Chemistry
Medicine
Novelty (within)
Novelty (between)
Feasibility (within)
Feasibility (between)
Probability (within)
Probability (between)
Human-AI idea similarity (within)
Human-AI idea similarity (between)
Seniority
Uses AI method (log)
Observations
R2
Adj. R2
F-statistic

(1) Citation pct.

(2) Productivity pct.

(3) log(Age)

-0.9717***
(0.117)
0.1245***
(0.037)
0.1635**
(0.061)
0.2295***
(0.050)
0.1227***
(0.006)
0.2191***
(0.010)
0.1296***
(0.006)
0.0730***
(0.012)
0.3143***
(0.006)
0.4468***
(0.012)
1.2835***
(0.120)
0.4726***
(0.148)
-0.1605***
(0.049)
-0.1697
(0.382)

-1.0100***
(0.116)
0.1244***
(0.037)
0.1635**
(0.061)
0.2287***
(0.050)
0.1227***
(0.006)
0.2198***
(0.010)
0.1296***
(0.006)
0.0722***
(0.012)
0.3143***
(0.006)
0.4481***
(0.012)
1.2835***
(0.120)
0.4717***
(0.148)
-0.0970*
(0.049)
-0.0793
(0.382)

-0.9505***
(0.123)
0.1426***
(0.038)
0.1813**
(0.061)
0.2397***
(0.050)
0.1226***
(0.006)
0.2199***
(0.010)
0.1296***
(0.006)
0.0719***
(0.012)
0.3142***
(0.006)
0.4474***
(0.012)
1.2825***
(0.120)
0.4684***
(0.147)
-0.0386*
(0.018)
-0.2315
(0.390)

23,615
0.395
0.395
874.5

23,615
0.395
0.395
873.5

23,635
0.395
0.395
876.0

Standard errors in parentheses. *** p<0.001, ** p<0.01, * p<0.05.

27

Extended Data Table 3. Regression results with interaction effects between
seniority and field. Once a field-by-seniority interaction is included in the model, the field
main effects vanish. Senior scientists in every field are more skeptical, with the decay being
most pronounced in the social sciences.

Favorability of Adoption
Intercept

-0.8070***
(0.126)

Biology

-0.0983
(0.076)
-0.0545
(0.125)
0.0340
(0.101)

Chemistry
Medicine
Novelty (within)

0.1227***
(0.006)
0.2178***
(0.010)

Novelty (between)
Feasibility (within)

0.1296***
(0.006)
0.0742***
(0.012)

Feasibility (between)
Probability (within)

0.3143***
(0.006)
0.4457***
(0.012)

Probability (between)
Human-AI Idea Similarity (within)

1.2835***
(0.120)
0.4927***
(0.148)

Human-AI Idea Similarity (between)
Seniority

-0.5073***
(0.112)
0.4451***
(0.129)
0.4364*

Seniority × Biology
Seniority × Chemistry

Continued on next page

28

Favorability of Adoption
(0.208)
0.3919*
(0.174)

Seniority × Medicine
Prior AI Use (log)

-0.1605
(0.382)

Observations
R2

23,615
0.396

*** p < 0.001, ** p < 0.01, * p < 0.05. Field-level comparisons use social science as the baseline.

29

Extended Data Table 4. Regression results with interactions between field and
quality dimensions. Social science is more tolerant of risky (less probable) ideas compared
to biomedicine.
Favorability of Adoption
Intercept

-0.9717***
(0.117)

Biology

0.1245***
(0.037)
0.1635**
(0.061)
0.2295***
(0.050)

Chemistry
Medicine
Novelty (within)

0.1338***
(0.014)
-0.0143
(0.017)
-0.0142
(0.027)
-0.0084
(0.021)
0.2191***
(0.010)

Novelty (within) × Biology
Novelty (within) × Chemistry
Novelty (within) × Medicine
Novelty (between)
Feasibility (within)

0.1316***
(0.012)
-0.0036
(0.015)
-0.0183
(0.025)
0.0094
(0.021)
0.0730***
(0.012)

Feasibility (within) × Biology
Feasibility (within) × Chemistry
Feasibility (within) × Medicine
Feasibility (between)
Probability (within)

0.2692***
(0.013)
0.0584***
(0.016)

Probability (within) × Biology

Continued on next page

30

Favorability of Adoption
Probability (within) × Chemistry

0.0208
(0.025)
0.0632**
(0.022)
0.4468***
(0.012)

Probability (within) × Medicine
Probability (between)
Human-AI Idea Similarity (within)
Human-AI Idea Similarity (within) × Biology
Human-AI Idea Similarity (within) × Chemistry
Human-AI Idea Similarity (within) × Medicine
Human-AI Idea Similarity (between)
Seniority

1.1298***
(0.232)
0.1499
(0.286)
-0.6233
(0.565)
0.5567
(0.377)
0.4726***
(0.148)
-0.1605***
(0.049)

Prior AI Use (log)

-0.1697
(0.382)

Observations
R2

23,615
0.396

*** p < 0.001, ** p < 0.01, * p < 0.05. Field-level comparisons use social science as the baseline.

31

Extended Data Table 5. General model vs. specific model for one quality dimension. Test accuracy is reported separately for each evaluation domain (Biology, Chemistry,
Medicine, Social Science), evaluated on held-out scientist ratings excluded from all training
sets. The general model assigns αd = 1 across all dimensions, while each dimension-specific
model sets αd = 1 for a single dimension and αd = 0 otherwise. In order to conduct a fair
comparison, we fixed the learning rate to be 3 × 10−5 and the margin weight to be 1. We can
simultaneously optimize all three dimensions without the need to train a separate model for
each specific dimension.
Domain

Config

Novelty

Feasibility

Probability

Training

General
Novelty-only
Feasibility-only
Probability-only

0.6845
0.7109
0.4760
0.6105

0.6800
0.4430
0.6142
0.4655

0.6312
0.4839
0.5198
0.6313

Biology

General
Novelty-only
Feasibility-only
Probability-only

0.6311
0.6443
0.4588
0.6212

0.5667
0.4489
0.5707
0.4448

0.6424
0.4913
0.5578
0.6957

Chemistry

General
Novelty-only
Feasibility-only
Probability-only

0.6283
0.6626
0.6077
0.5208

0.5912
0.4863
0.5757
0.5090

0.6766
0.5268
0.4984
0.6350

Medicine

General
Novelty-only
Feasibility-only
Probability-only

0.6218
0.6176
0.4637
0.6086

0.6597
0.4077
0.6486
0.4094

0.6845
0.4399
0.5700
0.6513

Social

General
Novelty-only
Feasibility-only
Probability-only

0.6281
0.6267
0.4255
0.5650

0.6216
0.4640
0.6378
0.4164

0.6361
0.5025
0.5192
0.6262

32

Extended Data Table 6. Train accuracy & test accuracy per evaluation domain
across dimensions. Bolded values indicate the better one among the domain-specific model
vs. the general model. We observe that across all dimensions, the domain-specific models for
biology and social science are consistently better, in some cases outperforming the general
model by nearly 10% (5.4% increase compared to the 56.7% feasibility accuracy for the
general model tested in biology). However, in domains with limited data, such as chemistry
and medicine, the general model sometimes performs better. When training data is sufficient
(i.e., Biology and Social Science), field-specific models can capture domain-distinctive taste;
however, when data is limited, the cross-field general model is still able to capture the
underlying logic of scientific judgment. In the study, for a fair comparison, we fixed the
learning rate to be 3 × 10−5 and the margin weight to be 1.
(a) Novelty

Domain
General
Biology
Chemistry
Medicine
Social Science

Train Acc.

Biology

Chemistry

Medicine

Social

0.6845
0.7221
0.5612
0.6565
0.6939

0.6311
0.6864
—
—
—

0.6283
—
0.6001
—
—

0.6218
—
—
0.6651
—

0.6281
—
—
—
0.6434

(b) Feasibility

Domain
General
Biology
Chemistry
Medicine
Social Science

Train Acc.

Biology

Chemistry

Medicine

Social

0.6800
0.6090
0.5612
0.6057
0.5999

0.5667
0.6205
—
—
—

0.5912
—
0.4756
—
—

0.6597
—
—
0.5959
—

0.6216
—
—
—
0.6218

(c) Probability

Domain
General
Biology
Chemistry
Medicine
Social Science

Train Acc.

Biology

Chemistry

Medicine

Social

0.6312
0.6979
0.5612
0.6598
0.6828

0.6424
0.6716
—
—
—

0.6766
—
0.6203
—
—

0.6845
—
—
0.6551
—

0.6361
—
—
—
0.6682

33

Supplementary Information
for
“Contemporary AI lacks the imagination
to diverge or negate in science”
Contents
A Methods
A.1 Data collection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
A.2 Name disambiguation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
A.3 The full list of LLMs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
A.4 Data processing pipeline . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
A.5 Survey design . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
A.6 The classifier of null hypotheses . . . . . . . . . . . . . . . . . . . . . . . . .
A.7 The detection of prior AI exposure . . . . . . . . . . . . . . . . . . . . . . .
A.8 The realistic reference of consistency between independent reviewers . . . . .
A.9 Statistical specifications . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
A.10 Subtopic-level distribution analysis . . . . . . . . . . . . . . . . . . . . . . .
A.11 Robustness to sample selection and response bias . . . . . . . . . . . . . . .
A.12 Implementation of novelty checkers . . . . . . . . . . . . . . . . . . . . . . .
A.13 Training reward models on human ratings . . . . . . . . . . . . . . . . . . .
A.14 Simulation models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

35
35
36
36
36
38
39
40
41
42
45
47
48
51
54

B Survey and Prompts
B.1 Prompts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
B.2 The pilot study, the recruitment email, and the survey . . . . . . . . . . . .

58
58
65

C SI Tables and Figures
SI Table 1: Pearson correlation of conditional perplexity across models . . . . . .
SI Table 2: Simulation model parameters . . . . . . . . . . . . . . . . . . . . . . .
SI Table 3: Adoption decisions with author fixed-effects vs. ordered logit models .
SI Table 4: Regression results with all tested interactions between seniority, field,
and quality dimensions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
SI Table 5: Nonresponse-adjusted estimates of adoption . . . . . . . . . . . . . . .
SI Figure 1: Test accuracy vs. training step for candidate models . . . . . . . . .
SI Figure 2: The recruitment email . . . . . . . . . . . . . . . . . . . . . . . . . .

73
73
74
75

34

76
78
79
80

A

Methods

A.1

Data collection

We collected 121,640 papers published after 2023 from six preprint platforms: BioRxiv (68%;
biology), ChemRxiv (3%; chemistry), MedRxiv (20%; medical science), PsyArXiv (psychology), EdArXiv (education), and SocArXiv (general social science), with the social science
platforms collectively accounting for 9%. Our dataset consists of full-text empirical papers,
each containing at least one extracted human hypothesis (described in detail in Subsection
A.4). For the hypothesis generation process, we used 26 well-representative LLMs spanning
both open-source and commercial models from eight mainstream companies (the full list can
be found in Subsection A.3). Unlike other hypothesis generation studies 1 , which concentrate
exclusively on computer science papers, we deliberately excluded papers from arXiv, the
most accessible data source. Our rationale is that we find 73% of papers on arXiv fall into
computing and mathematical domains - specifically, computer science (43%), mathematics
(18%), statistics (5%), and electronic engineering (7%). In contrast, hypothesis testing is
a practice most deeply embedded in the natural and social sciences. In computing and
mathematical fields, much of the work is algorithmic or engineering-oriented, and often does
not follow the classical hypothesis-testing framework 2,3 . More importantly, full-text papers
from arXiv are already largely included in common pretraining corpora, whereas papers from
other preprint platforms are typically excluded. This is the case for widely used datasets such
as LLaMA 4 , Dolma 5 , and Common Crawl–derived corpora (e.g., The Pile 6 , RedPajama 7 ,
and Common Pile 8 ), which underpin many modern LLMs 9,10 . This discrepancy arises for
two main reasons: (1) arXiv provides structured LaTeX source files via accessible storage
(e.g., Amazon S3 bucket), whereas platforms such as ChemRxiv, PsyArXiv, and SocArXiv
primarily distribute content as PDFs without standardized HTML/XML interfaces; and (2)
other platforms present more complex copyright and licensing constraints3 for large-scale
data inclusion in the LLM pretraining. BioRxiv and its sister platform MedRxiv even actively restrict automated crawling4 . This constraint similarly affects datasets derived from
Common Crawl. Our additional context-puzzle-rewriting and leakage detection procedures
(Subsection A.4) further mitigate the risk of the leakage of human-generated hypotheses,
and as shown in the main paper, AI models are not replicating ideas from humans.
We further conducted a data contamination experiment by comparing preprints sampled
from all non-arXiv platforms used in the paper against the actual pretraining corpus, for
which we use a 10B-token sample from Dolma v1.6 5 . Each paper’s full text is segmented
into paragraph-level chunks, and chunks shorter than 30 words are discarded. For each valid
chunk (paragraph), we extract all 10-gram (10-word) sequences with a two-word sliding
window of overlap between each sequence. We then scan Dolma and identify a chunk (para3
4

https://blog.dhimmel.com/biorxiv-licenses/
https://www.biorxiv.org/robots.txt

35

graph) as matched if more than 50% of its 10-grams are found. Applying this procedure to
all paragraphs from 8,000 random non-arXiv papers in 2024, we find that only 4 paragraphs
are matched. Upon closer inspection, however, even these cases are effectively false positives:
the matching n-grams consist of common phrasings widely used across Internet text; other
adjacent paragraphs from the same paper are not matched; and the "matching" occurrences
are scattered across the full corpus rather than concentrated in any single source.

A.2

Name disambiguation

Name disambiguation is always a concern in large-scale data for scientific papers. To validate
the author matching, we randomly sampled 100 author names and conducted a manual
robustness check, finding a 96% match rate. Furthermore, prior work using large-scale
gold-standard disambiguation datasets to benchmark OpenAlex has demonstrated relatively
strong disambiguation performance, with an F1-score of approximately 0.82 11 .

A.3

The full list of LLMs

The full list of LLMs used in this study to propose hypotheses is provided below. We use
instruction-following LLMs throughout.
• Reasoning models: o3-mini (OpenAI), o4-mini (OpenAI), DeepSeek R1 0528 (DeepSeek),
o1 (OpenAI), o3 (OpenAI)
• Agentic deep research models: o4-mini-deep-research (OpenAI), Tongyi-deep-research
(Alibaba)
• Non-reasoning models (some of which can be configured for reasoning, but were not in
this study): GPT-4o (OpenAI), GPT-4o-mini (OpenAI), GPT-4.1 (OpenAI), Grok-3
(xAI), Grok-3-mini (xAI), LLaMA 3.1 8B (Meta), LLaMA 3.1 70B (Meta), LLaMA 3.1
405B (Meta), Gemma 3 4B (Google), Gemma 3 12B (Google), Gemma 3 27B (Google),
Phi-4 (Microsoft), Phi-3-mini (Microsoft), Mixtral 8×7B MoE (Mistral AI), Ministral
3B (Mistral AI), DeepSeek-V3 (DeepSeek), Qwen-Turbo (Alibaba), Gemini 2.0 Flash
(Google), Gemini 2.0 Flash-Lite (Google)

A.4

Data processing pipeline

Extracting Human Hypotheses We input the full text of each paper into the advanced
reasoning model o3-mini to summarize and extract human hypotheses. Our prompt enforces
specific constraints, including the exclusion of inferred content, peripheral assumptions, and
vague directional statements (see Subsection B.1 for details). We exclude all papers from
which no human hypotheses could be extracted, as they are likely theoretical or surveytype works. We deliberately avoid a more intuitive alternative—simply searching for the
36

keyword “hypothesis” and its variants and summarizing the targeted passages across the
paper—because such matches often yield irrelevant content. To accurately identify the core
human hypotheses related to the key puzzle, the model must instead consider the paper
holistically. In our survey, 98.62% of scientists reported being generally satisfied with the
AI-summarized human hypotheses derived from their own papers.
Extracting Context and Scientific Puzzles The background of a scientific paper - particularly the introduction and, when available, the related work sections - serves to establish
the narrative, build the stage, motivate the study, and lay the groundwork for the readers
and following sections. We use this contextual material to approximate the information that
builds the core research puzzle for LLMs generating hypotheses. We extract the introduction
and related work sections using GROBID5 (some papers do not include a distinct "related
work" section). The two sections minimize the risk of fully disclosing the researchers’ own
hypotheses, experiments, interpretations, and conclusions, which are typically developed in
the following method/result section of the paper. We then prompt the o3-mini model to
extract two elements: (1) the core scientific puzzle and (2) the contextual information that
sets up the puzzle, specifically factual, reasoning-free statements about the key terms that
appear in the puzzle, with a particular focus on avoiding the disclosure of any human hypotheses. During the extraction, we apply few-shot prompting - providing the LLM with
several examples of well-formed puzzles and poor ones (e.g., cases that are not true puzzles
but rather proposed solutions or results), see Subsection B.1 for details.
Preventing Human Hypothesis Leakage to LLMs Sometimes the scientific puzzle
itself is essentially the rephrasing of a hypothesis and they cannot be meaningfully separated
(e.g., "does A increase B?"). To prevent data (human hypotheses) leakage during hypothesis
generation by LLMs, we include a further leakage detection step. We randomly selected
1000 human hypotheses. Using the GPT-4.1 model, we generated 20 rephrasings for each
hypothesis. Note that our rewriting may alter sentence structures, such as transforming
declarative sentences into interrogative ones, simulating the variety of ways humans might
express the same idea. This resulted in 20000 paraphrased hypotheses. We computed textual
similarity using the MPNet model 12 and identified an embedding similarity threshold of 0.82,
which captured 95% of the paraphrased pairs. If any sentence in an extracted context and
puzzle exceeds the similarity score of 0.82 with the corresponding human hypothesis, we
consider it a leakage and will not use the context or puzzle accordingly. In the survey, we
find 99.70% scientists are generally satisfied with the AI-summarized context and puzzle
from their own paper. We dropped all cases in which authors were unsatisfied with the
extracted context, puzzle and hypotheses in the subsequent analysis.
An example of the context, puzzle, and human hypotheses:
5

https://python.langchain.com/docs/integrations/document_loaders/grobid/

37

Example
Context: Microfinance institutions extend small loans to low-income borrowers who
lack access to traditional banks. Many such lenders issue loans to groups rather than
individuals, a practice known as joint-liability lending, in which all members are held
responsible if any one member defaults. Repayment rates under group lending have,
in many settings, exceeded those of conventional individual loans to comparable borrowers.
Puzzle: Why do joint-liability loans achieve higher repayment rates than individual
loans extended to borrowers of similar income and credit risk?
Human Hypothesis: Joint liability raises repayment chiefly by harnessing peer monitoring and social sanctions within the group.

A.5

Survey design

We prompted LLMs to generate hypotheses for each paper based on its summarized context
and stated research puzzle. For every paper, this produced a set of hypotheses generated by
LLMs, together with the original author’s hypotheses, context and puzzle. From the pool of
LLM-generated hypotheses, we selected five per paper and sent them to the original author
for evaluation, as long as we can access their email6 . Each author received a custom set of five
most semantically distinguishable hypotheses for their paper, drawn under a stratified rule
that partitioned the 26 LLMs into non-reasoning and reasoning7 models (Subsection A.3)
and required at least two hypotheses from each stratum. Within each stratum, hypotheses
were selected to maximize semantic distinguishability between each other, ensuring that the
five evaluations represented distinct ideas rather than near-duplicates, making the scientists’
judgments easier. This design yielded a nearly even distribution of to-be-judged hypotheses
from different models and addressed a concern particularly salient for non-reasoning models,
whose generations exhibited substantial within-group similarity, as shown in the main paper.
Given the nontrivial nature of the evaluation task, we implemented a comprehension check
prior to the rating phase. Participants were required to complete a brief understanding test
to ensure they could reliably apply the evaluation criteria: novelty (the extent to which the
generated idea introduces new elements beyond the input; rated on a 1–9 scale from not
novel to highly novel, with the same scale applied below), feasibility (the extent to which
a concrete experiment could be designed to test the proposed idea), and probability (the
likelihood that the generated idea is true even without experimental validation). Subsection B.2 provides additional details on the survey. This understanding test filtered out a
large amount of low-quality input, with many scientists dropping out of the study at the
6

The case of multiple corresponding authors is not very common in our dataset.
Reasoning models include agentic deep-research models, since these models reason simultaneously while
performing agentic web search.
7

38

test. Scientists then assessed the quality of extractions of context, puzzle, and their own
ideas, and independently rated each hypothesis along four dimensions: novelty, feasibility,
probability, and their favorability (measured by overall adoption intention). We also excluded all data from authors who indicated that they did not fully remember the content
of the paper and removed corresponding ratings from authors who only partially consented
(e.g., permitting use of their papers in open-source models but not all models). In total,
112,101 scientists received the invitation; 6,749 scientists participated in the crowd-sourced
evaluation task, with some participants contributing only partially completed responses, e.g.,
before the understanding test. This finally yielded 25,139 human-labeled evaluations (each
evaluation includes three scientific quality dimensions and adoption) contributed by 5,259
out of all participants. The study was conducted under the University of Chicago Institutional Review Board protocol IRB25-1372, titled “The Capabilities and Potential of AI for
Automating Scientific Idealization: A Large-Scale Human-in-the-Loop Study.”

A.6

The classifier of null hypotheses

We built a pipeline to automatically detect null hypothesis statements. In the preprocessing
stage, we used NLTK’s TreebankWordTokenizer, a rule-based tokenizer tailored for English
text. This tokenizer handles punctuation and contractions (e.g., “don’t” → “do not”) and
respects standard word boundaries more effectively than simple whitespace splitting. After
tokenization, we reconstructed each text as a space-separated sequence of tokens to ensure
consistency in representation, which is important for downstream vectorization. Unlike more
aggressive preprocessing pipelines, we intentionally avoided removing stopwords. This choice
preserves subtle but critical linguistic signals—particularly negations such as “no effect” or
“not significant”—that are essential for identifying null hypothesis statements.
We then passed the cleaned and tokenized text into a TF-IDF vectorizer, which transforms
the corpus into a sparse numerical representation based on term frequency–inverse document
frequency weighting. This representation preserves the discriminative power of informative
tokens (e.g., “no”, “not significant”), allowing them to receive higher weights in the feature
space. To construct the training dataset, we generated 1,000 labeled instances of null hypotheses (label 1) and an additional 1,000 non-null examples (label 0) using o3-mini (see
Subsection B.1 for prompt details). Two human annotators independently evaluated 100
generated null hypotheses and 100 generated not-null hypotheses, achieving an agreement
rate of 100%. Training the classifier on another training set generated by Google Gemini
2.5 Flash achieves 99.9% agreement with the results based on the o3-mini-generated training set across 1000 random samples (500 null and 500 not-null). Following prior work 13,14 ,
we trained an ensemble classifier composed of four widely used text classification models.
Specifically, we included two models suited for linearly separable features—Support Vector
Machine (with a linear kernel) and Logistic Regression—and two models capable of capturing non-linear relationships—Random Forest (with 100 estimators) and Gradient Boosting
39

Decision Trees (with 100 estimators). This combination enables the model to accommodate
potentially diverse feature geometries present in null hypothesis statements. Each classifier produces a probability estimate for the positive class (label = 1). The final prediction
is obtained by averaging these probabilities across all classifiers and applying a threshold
of 0.5. The task is relatively well-structured, as null hypotheses often contain distinctive
lexical patterns (e.g., “no relationship”, “no effect”), which are effectively captured by our
proposed algorithm. 5-fold cross-validation yields an accuracy of 99.5%, corresponding to
approximately 5 misclassifications per 1,000 samples.

A.7

The detection of prior AI exposure

We collect a total of 848,750 papers authored by participating scientists and assign each
scientist a prior AI usage rate, defined as the proportion of their papers involving AI. We
primarily adopt the pretrained language model developed by Hao and colleagues to detect AI-related research 15 . The authors developed a supervised natural language processing
pipeline based on a fine-tuned BERT model that classifies papers using their titles and abstracts. The model was trained in a two-stage procedure, first leveraging coarse labels from
explicitly AI-related venues and then refining predictions using higher-precision venue-level
signals. Separate models trained on titles and abstracts were ensembled to improve robustness (as our null-hypothesis classifier), eliminating the need for manually curated keyword
rules. The resulting classifier outputs the probability that a paper incorporates AI, enabling
large-scale identification of AI-related research across millions of publications. The method
was validated against expert-annotated data, where multiple domain experts independently
labeled sampled papers with high inter-rater agreement (Fleiss’ K = 0.96). Compared to
this human ground truth, the model achieved strong performance, reaching an F1-score of
approximately 0.875.
To ensure the robustness of our approach, we employ LLMs (specifically, Google Gemini
2.5 Flash) to detect AI usage, leveraging the growing adoption of LLM-based annotation
in the literature 16 . The model is tasked with determining, based on the title and abstract,
whether artificial intelligence or machine learning is involved in the paper. We then examine
the agreement between this LLM-based annotation method and Hao’s approach 15 across
both negative (0: non-AI) and positive (1: AI) classifications. If we treat Hao’s method
as the ground truth, the two methods exhibit near-perfect agreement in identifying non-AI
research, with precision, recall, and F1-scores all exceeding 0.99. While some discrepancies
arise in identifying AI-related papers, these differences remain within an acceptable range.
Google Gemini 2.5 Flash correctly identifies 80.0% of AI-related papers, while misclassifying
the remaining 20.0% as non-AI. Upon closer inspection of these misclassifications, we find
that the primary source of disagreement lies in the definition of AI usage. The LLM-based
annotation method classifies a paper as AI-related (label 1) only when AI is used as a
methodological tool. In contrast, Hao’s approach labels papers as AI-related not only when
40

AI is used as a method, but also when AI is used as the research topic itself (e.g., "what
should be the new paradigm of regulation for human-AI society in the future?").
We argue that the latter definition is more appropriate for our research setting. Regardless
of whether AI is used as a method or a research subject, it is expected to have implications
for AI attitude. Therefore we retain Hao’s method as the primary classification approach in
the main analysis. Despite these differences, the two methods demonstrate a high level of
overall consistency, achieving an alignment rate of 98.80%.

A.8

The realistic reference of consistency between independent reviewers

We do not assume that a perfect reward model would achieve 100% accuracy in our test
set. Such a ceiling is unattainable due to inherent randomness, subjective judgment, and
variability in human evaluation. Instead, we benchmark against the level of human agreement
observed in real-world peer review. We collected peer reviews from 26,731 submissions across
46 conferences hosted on OpenReview between 2017 and 2025 (see below). The dataset spans
multiple disciplines, including computer science, physics, medicine, and the social sciences.
Within each conference, we construct pairwise comparisons between papers. For each pair,
we consider cases where the reviewer in position p assigns a lower score to one paper and
a higher score to the other (excluding ties). The "human accuracy" is then operationalized
as the probability that a different, non-overlapping reviewer (i.e., the reviewer in another
position q) agrees with the direction of this preference. To control for positional bias, we
randomize the position of the reference reviewer and the non-overlapping reviewer 1,000
times, yielding the human consistency of 61.0% ± 0.1%. Note that this result should be
lower than the human agreement upper bound, since reviewers in the same position across
different papers are different.
The 46 conferences in our dataset: 1st ContinualAI Unconference, AAAI Conference on
Artificial Intelligence 2024 and 2025, Symposium on Advances in Approximate Bayesian Inference 2024, Conference on Language Modeling 2024, Cooking Robotics Workshop 2024,
Conference on Robot Learning 2023 and 2024, Conference on Parsimony and Learning 2024,
IEEE/CVF Conference on Computer Vision and Pattern Recognition 2023 and 2024, Workshop on Distributed Infrastructure for Common Good 2023, Workshop on EmbodimentAware Robot Learning 2024, European Conference on Computer Vision 2024, Conference on
Empirical Methods in Natural Language Processing 2023, European Space Power Conference
2023, Fast, Low-resource, and Accurate Organ and Pan-cancer Segmentation in Abdomen
CT 2023, SIGIR Workshop on Generative Information Retrieval 2024, ACM/IEEE International Conference on Human-Robot Interaction 2023 and 2024, International Conference
on Integration of Science and Technology for Sustainable Development 2024, International
Conference on Learning Representations 2017 to 2025, International Conference on Ma41

chine Learning 2023 and 2024, ACM International Conference on the Theory of Information
Retrieval 2024, International Joint Conference on Artificial Intelligence 2024, International
Semantic Web Conference 2024, ACM SIGKDD Conference on Knowledge Discovery and
Data Mining 2023 and 2024, ACM International Conference on Multimedia 2024, Conference on Neural Information Processing Systems 2021-2024, Neuro-Symbolic Learning and
Reasoning in the Era of Large Language Models 2024, Next-generation Data Governance
Workshop 2024, Tsinghua University Advanced Machine Learning 2024.

A.9

Statistical specifications

The Mundlak model with different representations of seniority In the main paper,
we estimate the relation between the level of favorability of adoption and potential sources
of biases and idea quality. We follow the correlated random-effects (Mundlak) tradition to
estimate a linear model 17 . The logic is that a pooled OLS specification without the Mundlak
adjustment may suffer from omitted-variable bias because it does not account for persistent
scientist-specific tendencies. For example, some scientists may systematically assign higher
ratings overall or be more inclined to pursue AI ideas. To address this concern, we include
each idea-level covariate both in deviation-from-scientist-mean form (ratingi,j − ratingi ) and
the scientist-level mean ratingi of scientist i for idea j. This decomposition separates withinscientist variation from between-scientist differences. As a result, the coefficients on the
within-scientist components capture how a scientist’s favorability of adoption changes when
an idea is evaluated as more novel, feasible, likely to be true, or more similar to their own
perspectives than is typical for that same scientist (thus "within" terms are our primary
interest for what kind of quality drives adoption), while the scientist-level means absorb
persistent cross-scientist differences in average evaluation levels.
We extract the main effect of human bias from scientist i on hypothesis j by the following
regression:


Adoptionij = β0 + β1 Noveltyij − Noveltyi + β2 Noveltyi

+ β3 Feasibilityij − Feasibilityi + β4 Feasibilityi

+ β5 Probabilityij − Probabilityi + β6 Probabilityi

+ β7 Human-AI Similarityij − Human-AI Similarityi + β8 Human-AI Similarityi
+ δ0 Seniorityi + δ1 Prior AI Usei + δ2 Fieldi + εij .

(1)

Novelty, feasibility, and probability are included as controls for baseline idea quality, thus β1 ,
β3 , and β5 answer what kind of quality drives adoption. β7 , δ0 , δ1 , and δ2 answer what impacts
adoption other than quality. Following a standard parametric uncertainty approach, in the
42

main paper, we reported model-based adjusted predictions (average marginal predictions)
with cluster-robust standard errors, holding the empirical distribution of other covariates
fixed.
Across the paper, we used log transformations (base e) for prior AI use, since many participants in our survey had near-zero prior AI use—they were not computer scientists. We
used the embedding model MPNet 12 to calculate the cosine similarity between human and
AI ideas.
We used the within-field yearly citation percentile to represent seniority by default. We
also employ two alternative seniority measures — average publication count per year and
academic age — and find consistent results across all specifications. Academic age is operationalized by identifying each author’s first publication based on their ID in the OpenAlex
dataset (name disambiguation in SI section A.2), with age defined as 2025 minus that first
publication year. Academic age is represented on a loge scale in regressions, as its distribution
is long-tailed—some participants are very junior (fewer than five years of experience). Yearly
publication/citation counts are percentilized within each field to (1) ensure comparability
across disciplines; (2) account for their long-tailed distribution; and (3) avoid confounding
with the cumulative nature of age. Full results of Equation 1 with different representations
of seniority can be found in Extended Data Table 2.
Author fixed effects and ordinal regressions We also test an alternative statistical
specification, author fixed effects, thereby absorbing variables such as seniority, prior AI
use, and field, which yields similar signs, magnitudes, and levels of statistical significance
compared to the Mundlak approach in the main paper. We estimate the following regression
(with αi representing the author fixed effects):

Adoptionij = αi
+ β1 Noveltyij + β2 Feasibilityij + β3 Probabilityij + β4 Human-AI Similarityij
+ εij .
(2)
Among the three quality dimensions, probability is still the strongest driver of adoption.
Individuals still show a strong preference for ideas that are more similar to their own perspectives (bigger than probability). All coefficients are statistically significant.
We use a linear specification as our main model for ease of interpretation. With nine ordered categories of quality dimensions, the outcome is sufficiently fine-grained that a linear
model provides a useful approximation. Here for robustness, we use a cluster-robust ordered logistic regression model (proportional odds model) estimated using the BFGS maxi43

mum likelihood optimization method, with Mundlak decomposition to separate within- and
between-individual effects to replicate the conclusion in the main paper. Conclusions are
consistent.
The regression results of the author-fixed effect model and ordered logistic regression model
can be found in SI Table 3.
Seniority by field interaction We then estimate human bias for scientist i evaluating
hypothesis j by augmenting Equation 1 with interaction terms between seniority and field
as shown in Equation 3.


Adoptionij = β0 + β1 Noveltyij − Noveltyi + β2 Noveltyi

+ β3 Feasibilityij − Feasibilityi + β4 Feasibilityi

+ β5 Probabilityij − Probabilityi + β6 Probabilityi

+ β7 Human-AI Similarityij − Human-AI Similarityi + β8 Human-AI Similarityi
+ δ0 Seniorityi + δ1 Prior AI Usei + δ2 Fieldi
+ γ0 Seniorityi × Fieldi
+ εij .
(3)
We observe that the field-level differences disappear once this interaction is included. While
being senior continues to have a negative effect overall, the interaction terms are positive
for all fields except the baseline category (social science), though not large enough to fully
offset the baseline negative effect. These results suggest that skepticism toward AI among
senior scientists is broadly universal, but is particularly pronounced among social scientists.
Consequently, the strong negative attitudes within senior social scientists drive the aggregate
pattern in which the field, as a whole, appears more resistant to AI. Results can be found in
Extended Data Table 3.
Quality by field interaction We then estimate human bias for scientist i evaluating
hypothesis j by augmenting Equation 1 with interaction terms between field and withinscientist quality rating differences (parameters γ0 –γ2 ), as well as a within-scientist preference
term capturing alignment between human and AI-generated ideas γ3 . All other statistical
specifications remain the same. This specification allows epistemic standards to vary systematically across fields, say, whether a field especially appreciates novel research (Equation
4).

44


Adoptionij = β0 + β1 Noveltyij − Noveltyi + β2 Noveltyi

+ β3 Feasibilityij − Feasibilityi + β4 Feasibilityi

+ β5 Probabilityij − Probabilityi + β6 Probabilityi

+ β7 Human-AI Similarityij − Human-AI Similarityi + β8 Human-AI Similarityi
+ δ0 Seniorityi + δ1 Prior AI Usei + δ2 Fieldi

+ γ0 Noveltyij − Noveltyi × Fieldi

+ γ1 Feasibilityij − Feasibilityi × Fieldi

+ γ2 Probabilityij − Probabilityi × Fieldi

+ γ3 Human-AI Similarityij − Human-AI Similarityi × Fieldi
+ εij
(4)
As shown in Extended Data Table 4, the regression results are consistent with those reported
in the main paper. The newly introduced interaction terms yield an interesting pattern: we
do not find meaningful field-level differences in how novelty or feasibility or human-AI idea
alignment affect adoption, but we do observe significant heterogeneity across fields in the
effect of probability. The interaction results show that the positive effect of within-author
probability is significantly stronger in biology and medicine than in social science, but not
significantly different in chemistry. Since the baseline effect is already positive and significant
(0.269, p < 0.001), the positive interaction terms for biology (0.058, p < 0.001) and medicine
(0.063, p = 0.003) imply that these fields are even more likely to adopt ideas that are judged
as more probable. This suggests that, compared with social science, biology and medicine
exhibit a stronger preference for relatively "safe” research directions. We further include
interaction terms between field, within-author rating differences, and seniority in SI Table
4. Across all specifications, our main conclusions remain robust.

A.10

Subtopic-level distribution analysis

Preprint platforms require authors to assign a subtopic label to each submission (see below).
We collected these labels and compared their distribution across respondents (based on their
papers) with that of the full corpus (121,640 papers). The two distributions are closely
aligned (Pearson’s r = 0.98; Spearman’s ρ = 0.96; Mean absolute error = 0.01). Each
subtopic label is followed by two numbers: the first is its proportion among respondents, the
second its proportion in the full corpus.
• Biology (20 subtopics): Animal Behavior and Cognition (1.93%, 1.93%); Biochemistry and Molecular Biology (12.48%, 11.04%); Bioengineering and Synthetic Biology
(2.06%, 2.44%); Bioinformatics and Computational Systems Biology (6.79%, 7.52%);
45

Biophysics (1.10%, 0.74%); Cancer Biology (5.90%, 5.85%); Cell Biology (7.91%,
6.32%); Developmental Biology (4.46%, 3.75%); Ecology (3.55%, 4.32%); Evolutionary
Biology (2.85%, 3.04%); Genetics and Genomics (6.42%, 6.93%); Immunology (5.26%,
4.29%); Microbiology (9.20%, 9.72%); Neuroscience (13.61%, 13.26%); Paleontology
(0.11%, 0.09%); Pathology and Disease Biology (7.96%, 9.16%); Pharmacology and
Toxicology (1.06%, 0.85%); Physiology and Organismal Biology (4.41%, 4.86%); Plant
Biology (2.47%, 3.64%); Scientific Communication and Education (0.47%, 0.23%).
• Medicine (40 subtopics): Addiction Medicine (1.74%, 0.87%); Allergy, Immunology,
and Rheumatology (1.74%, 1.76%); Anesthesia and Pain Medicine (0.68%, 0.89%);
Cardiovascular Medicine (7.82%, 11.35%); Dentistry and Oral Medicine (0.57%, 0.52%);
Dermatology (0.27%, 0.51%); Emergency and Critical Care Medicine (0.92%, 1.24%);
Endocrinology and Metabolic Disease (2.50%, 3.10%); Epidemiology and Public Global
Health (10.65%, 8.52%); Forensic Medicine (0.27%, 0.10%); Gastroenterology and
Hepatology (1.06%, 1.74%); Genetic and Genomic Medicine (9.89%, 7.43%); Geriatric and Palliative Medicine (1.82%, 1.87%); Health Informatics and Digital Health
(4.51%, 3.43%); Health Policy, Economics, and Systems (1.28%, 1.45%); Hematology (0.79%, 0.59%); Infectious Diseases (11.65%, 14.60%); Medical Education (1.22%,
0.89%); Medical Ethics (0.14%, 0.08%); Nephrology (0.84%, 1.26%); Neurology (8.53%,
8.37%); Nursing (0.65%, 0.28%); Nutrition (1.06%, 1.34%); Obstetrics, Gynecology,
and Reproductive Health (3.01%, 3.35%); Occupational and Environmental Health
(1.09%, 0.78%); Oncology (5.62%, 6.10%); Ophthalmology (0.81%, 1.01%); Orthopedics (1.17%, 0.82%); Otolaryngology (0.27%, 0.29%); Pathology and Laboratory
Medicine (1.20%, 0.72%); Pediatrics (1.39%, 2.08%); Pharmacology, Therapeutics,
and Toxicology (0.62%, 0.48%); Primary Care Research (0.52%, 0.70%); Psychiatry
and Clinical Psychology (7.52%, 5.66%); Radiology and Imaging (1.36%, 1.27%); Respiratory Medicine (1.63%, 2.02%); Sports Medicine and Rehabilitation (2.04%, 1.45%);
Surgery (0.43%, 0.52%); Transplantation (0.46%, 0.32%); Urology (0.27%, 0.22%).
• Chemistry (14 subtopics): Agriculture and Food Chemistry (0.96%, 1.21%); Analytical Chemistry (4.60%, 4.77%); Biological and Medicinal Chemistry (11.47%, 15.17%);
Catalysis (7.23%, 7.01%); Chemical Education (0.90%, 0.80%); Chemical Engineering
and Industrial Chemistry (0.66%, 1.61%); Earth, Space, and Environmental Chemistry (3.41%, 4.60%); Energy and Electrochemistry (8.00%, 9.31%); Inorganic and
Organometallic Chemistry (5.97%, 5.69%); Materials Science and Nanoscience (18.94%,
18.16%); Organic Chemistry (14.04%, 11.95%); Physical Chemistry (6.27%, 5.06%);
Polymer Science (4.24%, 3.39%); Theoretical and Computational Chemistry (13.32%,
11.26%).
• Social sciences (43 subtopics): Behavior Analysis (1.82%, 1.46%); Biological Psychology and Cognitive Neuroscience (6.35%, 6.48%); Clinical and Counseling Psy46

chology (2.77%, 4.50%); Cognitive Psychology, Cognition, and Perception (18.32%,
14.61%); Developmental Psychology (2.54%, 3.31%); Health and Community Psychology (1.56%, 2.97%); Linguistics and Psycholinguistics (5.39%, 4.43%); Social, Personality, and Cultural Psychology (23.01%, 22.99%); Anthropology (0.25%, 0.13%);
Communication and Media Studies (2.13%, 1.70%); Criminology and Criminal Justice (0.61%, 0.45%); Demography and Population Studies (0.84%, 0.54%); Economics
(1.62%, 1.81%); Family, Life Course, and Society (0.94%, 0.88%); Gender and Sexuality Studies (0.68%, 1.21%); Geography, Urban Studies, and Planning (0.25%, 0.80%);
Health, Medicine, and Society (1.13%, 2.63%); History (0.80%, 1.44%); Inequality,
Stratification, and Mobility (1.31%, 0.86%); Law and Legal Studies (1.02%, 0.95%);
Library and Information Science (0.10%, 0.06%); Metascience and Science and Technology Studies (8.59%, 8.87%); Political Science and International Relations (2.93%,
2.52%); Public Policy and Public Administration (0.88%, 0.50%); Race, Ethnicity,
and Migration (1.05%, 0.37%); Religion (1.04%, 1.16%); Research Methods, Statistics, and Measurement (5.35%, 3.90%); Social Work and Social Policy (0.02%, 0.17%);
Sociology (general) (1.33%, 1.33%); Work, Organizations, and Occupations (0.90%,
1.29%); Adult, Vocational, and Continuing Education (0.00%, 0.06%); Curriculum
and Instruction (0.00%, 0.00%); Early Childhood Education (0.08%, 0.06%); Educational Leadership, Administration, and Policy (0.10%, 0.19%); Educational Psychology
(1.88%, 2.26%); Educational Technology and Online Learning (0.27%, 0.22%); Higher
Education (0.18%, 0.45%); International and Comparative Education (0.00%, 0.00%);
K–12 Education (0.06%, 0.15%); Language, Literacy, and Bilingual Education (0.59%,
0.77%); Science and Mathematics Education (1.19%, 1.16%); Special and Inclusive
Education (0.08%, 0.15%); Teacher Education and Professional Development (0.06%,
0.19%).

A.11

Robustness to sample selection and response bias

The estimation sample consists of researchers who responded to the survey, and respondents
need not be representative of the population from which they were drawn. If the propensity
to respond is correlated with both the covariates and the outcome, the coefficients in the
main result may be biased.
We assess this using an auxiliary frame covering the full set of contacted researchers, respondents and non-respondents alike. For every individual in the frame, we observe field, average
annual publications, average annual citations, academic age, and prior AI use. The frame
therefore permits a direct comparison of respondents and non-respondents on pre-treatment
observables, and allows us to reweight the estimation sample so that its covariate distribution
matches that of the full contacted population.
Let Si = 1 denote that researcher i appears in the sample and Xi the vector of pre-treatment
47

observables. The reweighting procedure below maintains selection on observables,
Yi ⊥ Si | Xi .

(5)

We estimate the response propensity p̂(Xi ) = Pr(Si = 1 | Xi ) on the full frame by logistic
regression, fit separately within each field so that the selection mechanism is allowed to differ
across disciplines, and include second-order terms (squares and pairwise interactions of the
covariates) so that the propensity is not restricted to be linear in X. Predicted propensities
are truncated to [0.02, 0.98]. Each sampled researcher then receives the stabilised weight
wi =

Pr(S = 1)
,
p̂(Xi )

(6)

winsorised at the 99th percentile and normalised to mean one, which reweights the respondents back to the full contacted population: researchers of a type that respond rarely receive
proportionally larger weight. Weights are constructed at the researcher level and applied
to all ideas evaluated by that researcher. The main outcome equation (Equation 1) is then
re-estimated by weighted least squares, with all other features of the main specification left
unchanged (e.g., standard errors are clustered at the same level).
SI Table 5 reports the outcome equation with and without weighting. All coefficients of substantive interest are essentially unchanged in sign, magnitude, and significance classification
under reweighting.

A.12

Implementation of novelty checkers

We evaluate several mainstream novelty evaluation methods in the main paper. All approaches essentially operationalize novelty as the degree of deviation between a generated
idea g and its corresponding context and puzzle c, capturing how unexpected the generation
is with respect to the input.
Semantic Similarity This is the most intuitive way: we encode both the context/puzzle c
and generated idea g into dense vector representations using a pretrained sentence embedding
model 12 . Novelty is defined as the inverse cosine similarity:
Noveltysem (g, c) = 1 − cos(eg , ec )

(7)

where eg and ec denote the embeddings of g and c, respectively. Lower similarity corresponds
to higher novelty.
n-gram Novelty (2/3-gram) We quantify the lexical novelty of generated ideas using
bi-grams and tri-grams relative to the original context and puzzle text. Let Nn (x) denote
48

the set of n-grams extracted from sequence x.
We define n-gram novelty as the complement of the Jaccard similarity between the generated
hypothesis and its corresponding context and puzzle:
Noveltyn (g, c) = 1 −

|Nn (g) ∩ Nn (c)|
,
|Nn (g) ∪ Nn (c)|

n ∈ {2, 3}.

(8)

This formulation captures the extent to which the generated hypothesis introduces lexical
combinations that do not already appear in the original input. Higher values indicate greater
lexical divergence from the sources.
Entropy-based Novelty (Length-normalized Cross-Entropy) To capture distributional deviation relative to the original context and puzzle, we measure novelty using lengthnormalized cross-entropy. For each generated hypothesis g, we compare its token sequence
against the empirical token distribution induced by its context and puzzle text c. Let Pc (w)
denote the empirical probability of token w as estimated from c.
We define distributional novelty as:
NoveltyCE (g, c) = −

1 X
log max(Pc (w), ϵ),
|g| w∈g

(9)

where |g| is the number of tokens in g (length normalization). To handle unseen tokens, we
apply smoothing by using max(Pc (w), ϵ), ϵ = 1e − 8.
This measure quantifies the average token-level surprisal of the generated hypothesis under
the token distribution of its paired context and puzzle. Intuitively, it captures how difficult
it is to explain the generated text using the lexical distribution of the original input. Higher
values indicate that the generated hypothesis uses fewer expected tokens relative to the input
and therefore exhibits greater distributional novelty.
Natural Language Inference (NLI) We use an NLI model, DeBERTa 18 , to evaluate
the relationship between the context/puzzle and the idea generated from it. Let pe and pc
denote the probabilities of entailment and contradiction, respectively. A high pe indicates
that the generated idea is well supported by, and can be inferred from, the context/puzzle,
whereas a high pc indicates that the idea conflicts with or contradicts it. We define:
DerivationNLI (g, c) = pe − pc
A higher derivation score implies lower novelty.

49

(10)

Contextual Perplexity We compute the conditional perplexity of each generated idea
given its corresponding context/puzzle. Concretely, we concatenate the context/puzzle and
the generated idea into a single sequence, and mask out the context/puzzle tokens by setting the ignore index to -100 so that the loss is computed only over the generated portion.
This setup ensures that the model evaluates the likelihood of the ideas conditioned on the
preceding context/puzzle, rather than in isolation. The resulting metric—obtained by exponentiating the cross-entropy loss—captures how “surprised” the model is by the generated
ideas: lower perplexity indicates that the answer is more predictable given the context/puzzle, while higher perplexity suggests greater novelty or unexpectedness. We first want to
see whether different LLMs yield similar results and we consider four similar-sized models:
Qwen-7B, Mistral-7B-v0.1, LLaMA-2-7B, and DeepSeek-LLM-7B-base. Empirically, we find
that the conditional perplexity scores produced by these four models are highly correlated
with one another, indicating strong agreement across evaluators (SI Table 1). We therefore
aggregate them by taking the mean perplexity as a unified measure of novelty. However,
despite this internal consistency, the resulting mean perplexity-based metric exhibits little
to no correlation with human judgments of novelty.
GraphEval-GNN 19 GraphEval is a lightweight graph-based framework for LLM-driven
idea evaluation. Its key insight is that directly prompting an LLM to judge a complex idea
yields biased and prompt-sensitive scores; the idea is instead represented as a node (or a set
of nodes) and evaluated through graph algorithms over a similarity graph. In the original
design, a small prompted LLM first decomposes each (long-text) idea into fine-grained viewpoints (atomic claims or facts). Because each idea in our setting is a single AI-generated
hypothesis—typically one to three sentences, far shorter than the paper abstracts decomposed in the original paper of GraphEval—we thus treat each hypothesis as an atomic unit.
Concretely, (i) each hypothesis is embedded with BERT into a single node; (ii) nodes are connected via top-5 cosine-similarity edges across hypotheses, forming a hypothesis-similarity
graph; (iii) a two-layer weighted GNN learns node representations through neighborhood
aggregation and predicts the hypothesis-level label.
Following the original design, we classify the raw scientist ratings into the four review-decision
classes used by GraphEval8 (reject, poster, oral, spotlight) by binning within-field quantiles
rather than at fixed thresholds. Concretely, within each field we take the empirical 25th,
50th, and 75th percentiles of the raw novelty ratings as cut points c1 ≤ c2 ≤ c3 (rounded
to the nearest integer on the 1–9 scale), and assign a rating r to reject if r ≤ c1 , poster if
c1 < r ≤ c2 , oral if c2 < r ≤ c3 , and spotlight if r > c3 (a spotlight hypothesis is one rated
among the most novel for its field, as shown in the original paper). Where the discreteness
of the scale and the central concentration of ratings collapse two cut points onto the same
integer, we shift one cut point by a single rating value so that all four classes remain non8

In our implementation, we found that the original 1–9 scale classes were too fine-grained for the model
to learn effectively.

50

empty. Quantile binning keeps the four classes comparably sized within each field—avoiding
the severe imbalance that fixed thresholds would induce given that ratings cluster near the
middle of the scale—so that macro-averaged metrics are not dominated by a sparse class,
and it aligns the labels with the within-field, relative notion of quality used throughout our
analysis.
We fit GraphEval-GNN transductively within each field: all hypotheses in the field, both
train and test, are embedded into a single graph, with training hypotheses carrying these
binned labels and test hypotheses being unlabeled, so that the model is supervised only by
the rated training split. GraphEval-GNN has modest data requirements (300 training and 50
test ideas in the original paper), so our sample is more than sufficient for training. For each
hypothesis, GraphEval-GNN outputs a probability distribution over the four classes, which
we collapse into a scalar novelty score by summing the probabilities of the three more-novel
classes:

Score = P (Spotlight) + P (Oral) + P (Poster).

A.13

(11)

Training reward models on human ratings

Basic setup We first convert the original ratings into pairwise comparisons among five
hypotheses evaluated by the same scientist (denoted h1 , h2 , h3 , h4 , and h5 ), where each pair
indicates which hypothesis is preferred along a given dimension. Scientists’ own ideas are
added into the prompt to represent their judgment perspectives. To prevent overfitting, we
deliberately avoid using all possible pairs. For example, if (h1 , h2 ), (h2 , h3 ), and (h1 , h3 ) are
all included, the relation between h1 and h3 can be inferred by transitivity (if h1 > h2 and
h2 > h3 , then h1 > h3 ); in our experiments, including such inferable pairs induced strong
overfitting (training accuracy near 90% but test accuracy below 60%). We therefore retain
only pairs whose relations cannot be deduced from others, namely the consecutive pairs (h1 ,
h2 ), (h2 , h3 ), (h3 , h4 ), and (h4 , h5 ).
The reward model maps a hypothesis y to a vector of dimension-specific rewards,
r(y) = (r1 (y), r2 (y), . . . , rD (y)),
where D = 3 in our setting, corresponding to novelty, feasibility, and probability. Given two
hypotheses ya and yb , we adopt the Bradley–Terry (BT) framework to model preference based
on reward differences. For each dimension d, we define a preference sign sd ∈ {+1, −1, 0},
where sd = +1 if ya is preferred to yb , sd = −1 if yb is preferred to ya , and sd = 0 if
the comparison is tied9 . Using this sign, we define the signed reward difference as ∆d =
9

In experiments we found that excluding tie pairs in training raises the accuracy, thus we excluded them.

51


sd rd (ya ) − rd (yb ) , which is positive when the model assigns a higher reward to the humanpreferred hypothesis and negative otherwise. The per-dimension BT loss is then defined
as
LBT
d = − log σ(∆d − λmd ) .
σ is the sigmoid function to map any real-valued number (∆d − λmd ) into a range between 0
and 1. To account for not only the direction but also the strength of preference, we further
incorporate the absolute score gap md ≥ 0 between the two hypotheses on dimension d as a
margin term, where the strength is controlled by λ.
We combine losses across dimensions using a weighted sum,
Lmulti-BT =

D
X

αd LBT
d .

d=1

Evaluation setup As shown in Extended Data Table 1, we report the full results for LLMas-a-judge and SOTA reward models10 on our held-out human-labeled dataset. We construct
pairwise comparisons from human judgments by selecting instances where scientists assign
a higher score to one AI-generated hypothesis over another (no tie). A model’s prediction is
considered correct if it agrees with the human preference, and we report simple accuracy.
For reward models, the evaluation follows their standard usage: each model assigns scalar
scores to both hypotheses, which we then convert into a directional preference (i.e., A > B or
A < B) and compare against the human judgment. This procedure is applied consistently to
both our trained models and all SOTA reward models. We evaluate LLM-as-a-judge under
the same framework for consistency, using three representative models as reported in the
main paper: Gemini 2.5 Flash, DeepSeek R1, and OpenAI’s o4-mini Deep Research model.
Under this setup, all three LLM judges perform even sometimes below random chance. This
appears to be driven by a central tendency bias, as they frequently assign similar or neutral
scores to both hypotheses, despite the absence of ties in our dataset.
When prompted instead with a direct comparative question (e.g., “Which hypothesis is better?”), LLM-as-a-judge performance improves (as there is no tie option for output). However,
this improvement is unstable and difficult to interpret. We observe pronounced positional
and framing biases: swapping the order of hypotheses, or rephrasing the prompt (e.g., “Is
A better/worse than B?” vs. “Is B worse/better than A?”), leads to significant fluctuations in their evaluation. These sensitivities have also been observed in other ambiguous
judgment tasks 20 , raising concerns about whether the observed gains, although still lower
than our trained model, reflect genuine evaluative capability or artifacts of prompt design.
10
Note that nicolinho/QRM-Gemma-2-27B was ranked No. 4 on RewardBench as of May 2026. We included
it because the No. 2 model, Databricks-Mosaic-Research/PGRM, was unavailable by May 2026.

52

Meanwhile, across all settings, matching human experts’ probability of assigning truth to
hypotheses was the easiest dimension on which LLMs performed.
Qwen3-14B is the optimal model SI Figure 1 presents test accuracy as a function of
global training step for five candidate models. Qwen3-14B achieves the highest test accuracy
throughout training, reaching approximately 0.615 at peak and stabilizing around 0.610.
Qwen3-32B converges to a similar range near 0.604, offering no substantial accuracy gain
over Qwen3-14B. Llama-3.1-8B records the lowest final accuracy, stabilizing near 0.585.
Regarding hardware, all models are trained on NVIDIA A100 80GB PCIe GPUs except
Qwen3-32B, which requires NVIDIA H200 NVL GPUs due to its need for larger GPU memory. Given that Qwen3-32B achieves no substantial improvement over Qwen3-14B in test
accuracy while demanding more advanced hardware, Qwen3-14B has been proven to be the
most practical choice. It delivers the best accuracy among all candidates while remaining
trainable on 4 A100 GPUs. Accordingly, all subsequent experiments are conducted using
Qwen3-14B.
SI Figure 1 is to justify the selection of the base model (Qwen3-14B). In order to conduct a
fair comparison, we fixed the learning rate to be 3 × 10−5 and the margin weight to be 111 .
Models are able to handle three quality dimensions simultaneously Extended
Data Table 5 presents training and test accuracy across four evaluation domains and three
dimensions, comparing a general model trained jointly on all three quality dimensions (αd = 1
for all dimensions—novelty, feasibility, and probability) against three dimension-specific
models, each trained with αd only switched-on on a single dimension (Novelty-only, Feasibilityonly, or Probability-only), using Qwen3-14B with learning rate 3 × 10−5 and margin weight
= 1.
The training accuracy results reveal that the general model learns all three dimensions in a
balanced way, with training and test scores remaining close, indicating no signs of overfitting. These three dimensions are indeed relatively independent from scientists’ eyes. The
test results reveal a consistent pattern across domains and dimensions. On Feasibility,
the general model achieves scores comparable to the Feasibility-only model across all four
domains (Biology: 0.5667 vs. 0.5707; Chemistry: 0.5912 vs. 0.5757; Medicine: 0.6597 vs.
0.6486; Social: 0.6216 vs. 0.6378), suggesting that dimension-specific training yields no clear
advantage. On Novelty and Probability, a similar pattern appears as Feasibility. Together, these findings indicate that joint training on all three dimensions is not only viable
but also preferable. The general model preserves capacity across three dimensions without
sacrifice on any individual dimension.
11

Note that these parameters, here and throughout Section A.13, are set uniformly for fair comparison, but
they are not necessarily the optimal parameter configuration for model performance. We provide a separate
paragraph later that specifically discusses the optimal parameters for each trained model.

53

Domain-specific models are necessary if the data is enough As shown in Extended
Data Table 6, we trained five models: four domain-specific models (Biology, Social Science,
Chemistry, and Medicine) and one general model trained on the full dataset. We tested
these models in the specific domains. Recall that the data is imbalanced—biology and
social science have more preprints than medicine and chemistry. Biology, which accounts for
the largest share of the data, outperforms the general model in domain-specific evaluation,
suggesting that specialization is particularly effective when abundant in-domain data are
available. Social Science, which has a more moderate share of the data, also exceeds the
general model, albeit by a smaller margin. This indicates that each field indeed contains
nuanced evaluative tastes that can be captured through specialization in model training.
By contrast, Medicine and Chemistry have considerably fewer examples, and their domainspecific models do not consistently surpass the general model, which benefits from training on
pooled and significantly larger datasets across all fields. Taken together, these results suggest
that domain-specific training is preferable when sufficient in-domain data are available, while
general models are more robust when in-domain data are limited.
Hyperparameter search Since the training objective involves two interacting hyperparameters, the learning rate and the margin weight, their joint effect on model performance is
difficult to predict a priori. We therefore conduct a grid search over 80 trials, combining five
learning rate values ({1, 3, 5, 7, 9}) with four learning rate scales ({10−3 , 10−4 , 10−5 , 10−6 })
and four margin weight values ({0, 0.1, 0.5, 1}), evaluating each configuration on the general
model trained across all domains and dimensions on a separate validation set. This search
also serves to examine the robustness of performance across the explored ranges.
The optimal hyperparameter configuration varies across scientific domains in the testing
process. Biology model performs best with a learning rate of 2 × 10−5 and a margin weight
of 1.0, Chemistry model with a learning rate of 5 × 10−6 and a margin weight of 0.1, Social
Science model with a learning rate of 3 × 10−5 and a margin weight of 1.0, and Medicine
model with a learning rate of 2 × 10−5 and a margin weight of 0.0. The margin weight does
not always help but it is necessary in some cases of training.

A.14

Simulation models

A field as a collective estimating a space of quantities A research field faces a
space of questions it could ask, such as the magnitude of each of many drug effects, or the
prevalence of each of many social regularities, then studies them one by one. We write the
true magnitudes as θ1 , . . . , θm , all non-negative12 , drawn from a single distribution in which
most effects are small and a few are large:
θj ∼ |N (0, ω 2 )|,
12

Negative impacts are included here as well: we study only the magnitude of the effect, not its direction.

54

where ω sets how large real effects in the field tend to be.
Each study contributes a noisy measurement of whichever question it takes up. With significant AI use, a study of question j reports
θ̂i,j = θj +

Bj
|{z}

shared bias

+ εi,j .
|{z}
error

Here εi,j ∼ N (0, σ 2 ) with Corr(εi,j , εi′ ) = ρ for any two studies (i and i′ ) of the same question,
so that ρ is the share of the error variance that all studies hold in common and σ sets the
scale of a single study’s measurement error. The two components above behave in opposite
ways:
• Idiosyncratic error, a fraction 1 − ρ of the error variance — each study’s own noise.
Only this uncorrelated part averages out over enough studies.
• Shared bias Bj , together with the correlated share ρ of the error variance — the
component everyone gets wrong in the same direction, or in similar ways. This never
averages away.
• The shared bias decomposes into two parts, Bj = Bh +Bsel (zj ): a question-independent
blindspot Bh ≥ 0 (shared methods, data and models make the whole field wrong in
the same direction, regardless of which question is asked), and a question-dependent
selection term Bsel (zj ) arising from suppressed nulls, derived in (13) below. Both scale
with AI adoption.
What the field learns about question j from its nj studies decomposes cleanly:
MSEj =

Bj2
|{z}

shared bias (will not average out)

+ σ2

ρ
|{z}

correlation floor (will not either)

+ σ2

1−ρ
nj
| {z }

the only piece more studies shrink

(12)
where MSEj represents the mean squared error of the pooled collective estimates of question
j, i.e., how badly the field gets one question wrong.
Greater throughput, generated by AI, can reduce the last term and no other. A
corpus of correlated studies on one question is worth only neff = nj /[1 + (nj − 1)ρ] → 1/ρ
independent ones: at ρ = 0.20, even a million studies of one question are worth five. The
P
field’s total error is the average of (12) over its questions, MSE = m1 j MSEj (i.e., how
badly the field gets all questions wrong), and net knowledge is V = 1 − MSE.

Null and alternative as two halves of a single distribution The evidence a study
would produce, x ∼ N (θj , σ 2 ), we treat as a single bell curve: its upper part (the "effect")
55

.

and its lower part (the "null") are the two halves of the same object, split down the middle.
This makes suppressing nulls a single, literal operation — deleting part of one half of a
normal distribution. Specifically, we keep everything above the middle, then keep what falls
below it only with probability 1 − s, where s is how hard the null half is censored. At s = 0
the curve is intact; at s = 1 nothing below zero survives and what remains is the curve
truncated at zero. Once part of the lower half is gone, the two halves no longer cancel, and
the average of what gets published is pushed upward. Writing zj = θj /σ for how far the
question’s true effect sits above zero in noise units, the displacement is
Bsel (zj ) = σ

s φ(zj )
,
1 − s Φ(−zj )

φ(0) = √12π ≈ 0.40

(13)

Two further consequences follow from the same cut: the published pool also narrows (it drops
its lower tail), so the literature looks more precise exactly as it becomes more displaced; and
Bsel does not depend on nj . No amount of throughput recovers a half that was
never written down. Human researchers already delete part of this half, known as the
file-drawer problem 21,22 ; AI, trained to anticipate publishable findings, deletes it harder. The
total shared bias on a question is Bj = Bh + Bsel (zj ).
Where the cut bites hardest The displacement depends on where the true effect of the
question sits. At s = 0.98 (the AI null-suppression rate selected for the model, based on our
empirical findings):
• Large true effects survive almost untouched. At zj = 2 the displacement is
0.05 σ, at zj = 3 only 0.004 σ: there was almost nothing in the null half to delete, so
removing it changes almost nothing.
• Small effects are distorted most. At zj = 0 the displacement is 0.77 σ — the two
halves were balanced, and deleting one destroys the cancellation. The questions a field
gets most wrong are exactly those that possess a true effect that is smallest and most
questionable, and by construction those are most of its questions.
AI as a fast but error-correlated instrument AI is an instrument that is far faster,
but whose errors are also more highly correlated. Adoption is captured by a single parameter
a ∈ [0, 1]. Increasing a raises throughput n — the sole benefit, insofar as more studies shrink
the averageable term σ 2 (1 − ρ)/n — but it also raises three harms: (1) the cross-study error
correlation ρ (shared methods, (2) data and models make errors more alike), and (3) the
shared blindspot Bh , and the null-suppression rate s. All three scale with adoption and fall
on the parts of Equation (12) that throughput cannot reach: speed addresses only the first
error type and leaves the three harms untouched.

56

Three patterns The parameters used in the model can be found in SI Table 2. As we
discuss below, changing the numbers slides the hump, but it remains a hump, leaning away
from AI in mature fields, and falling faster when nulls are buried.
(1) AI’s benefit follows an inverted-U shape. Net knowledge V (1 minus MSE, so that
higher is better) traces a hump as the AI share a rises from 0 to 1:
• Up-slope (low a): few studies, low correlation — added AI throughput cancels random
noise, and knowledge rises.
• Peak (a = a∗ ): the marginal noise-cancelling benefit exactly balances the marginal
growth in bias and correlation.
• Down-slope (high a): the three harms accumulate in the irreducible part of the error;
additional speed buys almost nothing, and knowledge falls.
The optimum a∗ is therefore interior — a human/AI mix. The only benefit enters through
σ 2 (1 − ρ)/n, whose marginal value decays like 1/n2 ; the three harms grow with no such
damping. The benefit necessarily dominates while n is small (the up-slope) and the harms
once n is large (the down-slope). Equivalently: switch throughput off and only harms remain,
so the optimum sits at a = 0; switch all harms off and only the benefit remains, so it sits at
a = 1; with both active the peak lies between.
(2) Mature fields should use less AI. Young fields have few studies, so AI’s throughput
gains are valuable. Mature fields already have many, so additional studies add little and the
“everyone looks alike” harm dominates. The more studies a field already has (a maturity
factor τ ), the lower its optimal a∗ : raising τ lifts n at every a, so the marginal value of additional throughput (∼ 1/n2 ) is smaller everywhere, while the blindspot and null-suppression
harms are untouched by τ ; the balance therefore tips at a smaller a.
(3) Suppressing more nulls steepens the collapse. The more aggressively AI use
suppresses null claims (higher s at full automation), the further left the optimum shifts and
the deeper full-AI science falls. The selection bias Bsel rises with s and is independent of n, so
extra suppression adds harm that no amount of throughput can offset, lowering V at every
high-a point. Raising s at full automation from 0.90 to 0.995 lowers V (1) from 0.53 to 0.46
and shifts a∗ leftward. Comparing suppression off against on is the sharpest statement of the
point: with the file drawer switched off, full automation still leaves V (1) = 0.76. Switching
it on brings that to 0.47.

57

B

Survey and Prompts

B.1

Prompts

Hypothesis Extraction Prompt
You are reading a paper. Your task is to extract **relevant, explicit
scientific hypotheses** proposed by the authors.
Extraction Instructions:
1. **Exclude** background/factual claims, method descriptions,
presumptions, mathematical prerequisites/preconditions, and narrow
inferences/interpretations drawn from tables and figures.
2. **Apply strict selection criteria - do not over-generate**.
Extract only those hypotheses that the authors explicitly motivate and
place at the core of the paper’s main argument (typically introduced
early, e.g., in the Introduction or thereafter). Omit minor and
peripheral hypotheses confined to specific method, experiment, or
result subsections.
3. **Exclude vague directional statements** such as "xxx is a valuable
model for studying xxx"; "The proposed model provides a promising
and crucial direction for xxx"; and "This technology can be applied
to improve xxx," as these are summaries of the paper’s overarching
narrative rather than hypotheses.
4. Extract hypotheses based strictly on the **raw content**. Do not
generate or infer hypotheses on your own. Preserve the **original
meaning** of the authors’ hypotheses.
5. If no relevant, explicit hypotheses are found, output an empty
string "".
––- PAPER STARTS ––f{text}
––- PAPER ENDS ––Context/Puzzle Extraction Prompt
You are a helpful research assistant. You will be given the
introduction of a scientific paper. Your task is to identify and
extract two kinds of structured information from the text:
1. The **broad scientific context** of the work:
**Context** consists of only *factual*, *non-speculative,
non-reasoning* statements. These include big pictures and related
works, etc. This should read like what a researcher might see *before*

58

they propose a theory.
You extract hypothesis-agnostic explanations or definitions of key
terms and concepts that appear in the material.
These should help a reader understand the **context**, and should not
overlap with the **reasoning or hypotheses**.
Think of this as building a small supporting knowledge base. All
contextual snippets must be grounded in the text, though you may
rewrite or clarify them for precision and readability.
2. At the **end of each context**, add a sentence that explicitly
states *the core question or puzzle* that the paper addresses and can
be derived from the context.
Focus on the **high-level picture** of the work.
**Avoid**:
- Specific hypotheses or findings
- Technical/experimental details, methods, or datasets
- Any mention of author-proposed solutions
Your output should take the form of **describing the context then
proposing a question.**
Below are some illustrative examples of the puzzle:
Bad: Integration of hypergraph-based models that represent RNA-peptide
relationships will significantly improve the prediction of ncPEPs in
diverse cancer subtypes compared to existing deep learning approaches.
Good: What can we do to improve deep learning models so they can
accurately and robustly predict cancer-associated noncoding peptides
(ncPEPs)?
Bad: Declining androgen levels during aging reduce suppression of
gastric ILC2s, increasing cytokine production and susceptibility to
gastric disease.
Good: How do androgen levels influence the development of gastric
diseases?
Bad: Multi-modal sensor fusion improves real-time activity recognition
in smart homes by resolving ambiguities in unimodal data and merging
them using a deep LSTM model trained on the CASAS dataset.
Good: How to best integrate information from different individual
sensory inputs to recognize real-time activity in smart homes?
Now, based on the given introduction, write the
human-hypothesis-agnostic context and puzzle:
Introduction: text
Human hypotheses: text

59

Hypothesis Generation Prompt
You are an experienced scientist. You are writing a paper about the
following scientific puzzle. Your task is to propose **relevant,
publishable, novel, and feasible** hypotheses that have not appeared
in the literature to investigate the puzzle.
Instructions:
1. **Be concise**: exclude **background/factual claims or
methodological/experimental descriptions**.
2. Keep the hypotheses **relevant** to the core of the puzzle.
3. **Do not generate vague directional statements** such as "xxx is
a valuable model for studying xxx"; "The proposed model provides a
promising and crucial direction for xxx"; and "This technology can
be applied to improve xxx", as these are summaries of the paper’s
overarching narrative rather than hypotheses.
4. **Be creative** - reach beyond your existing knowledge base to
propose **untested** ideas.
5. Ensure that the generated hypotheses are **clear, specified,
well-reasoned, valid, and actionable**.
––- CONTEXTUAL PUZZLE STARTS ––f{text}
––- CONTEXTUAL PUZZLE ENDS ––Now, your output of the hypotheses:
Model Evaluation Prompt
You are an experienced scientist who is judging ideas (hypotheses)
proposed from the same context and puzzle as your own paper.
**Given the context and puzzle of your own paper**, you will judge the
novelty, empirical feasibility, and likelihood of being true of the
given hypotheses.
A hypothesis here can be a testable idea, or more broadly, a guiding
assumption in research methods, design, and direction.
Please use the following definitions:
<Novelty>: To what extent do the generated hypotheses - based on the
given context - generalize and introduce new, unseen, and interesting
ideas?
Given the context and puzzle: "Students in urban high schools
consistently underperform on standardized science exams compared
to their suburban counterparts. While factors such as <funding>,
<class size>, and <teacher experience> have been well studied, they

60

do not fully explain the persistent performance gap. The puzzle:
Why do students in urban high schools continue to underperform in
science despite comparable teacher credentials and similar classroom
resources?"
Hypothesis A: Urban students’ lower science achievement may stem from
prolonged exposure to high-information-density environments in urban
areas, which trains the brain to favor a "fast-response cognitive mode"
while weakening the "slow-reasoning circuits" essential for scientific
thinking.
Hypothesis B: Larger class sizes and the associated lower individual
attention from teachers lead to decreased academic performance in
science subjects among students in urban areas, compared to their peers
in suburban areas.
Hypothesis A is thus MORE NOVEL than hypothesis B, as class size has
been studied in the provided context.
<Empirical feasibility>: How empirically feasible are the hypotheses?
Relations between variables in an empirically feasible hypothesis
should be operationalizable, measurable, implementable, and testable.
"Even in a society where all individuals share a unified collective
consciousness, social conflict would still persist" thus is LESS
FEASIBLE than "More English listening practices could improve the
English writing scores among high-school students".
<Likelihood of being true>: How believable the hypotheses sound, based
on existing knowledge or internal logic? A probable (likely true)
hypothesis should be intuitive.
"Regular physical exercise reduces the risk of cardiovascular disease
in adults" thus is MORE PROBABLE than "Drinking two liters of soda per
day enhances memory retention in older adults".
Please do not evaluate format, writing style or grammar except where it
prevents understanding.
Please rate the novelty on a scale from **1 to 9**.
9: Highly novel: The hypothesis generalizes and stands out
significantly from the given context following an unconventional
reasoning path. If empirically validated, it could unlock a range
of new, impactful, and interesting implications.
5: Moderately novel: The hypothesis introduces some new ideas, but
they are expected given the context.
1: Not novel: The hypothesis is essentially a rephrasing of the
content in the provided context, with no meaningful innovation.

61

Please rate the likelihood of being true on a scale from **1 to 9**.
9: Highly probable: The hypothesis makes sense. It is highly likely
to be true, even without empirical validation.
5: Moderately probable: The hypothesis has an equal chance of being
true or false; it requires experimental validation.
1: Not probable: The hypothesis is incoherent, logically flawed, and
very likely to be false.
Please rate the empirical feasibility on a scale from **1 to 9**.
9: Highly feasible: The hypothesis clearly states relationships
between variables, including null or negative relations (e.g., A has
no relationship with B). The variables are operationalizable, and I can
readily envision experiments to test the hypothesis.
5: Moderately feasible: The hypothesis refers to some identifiable
variables and implies a general relationship, but the variables lack
clear definitions or operationalization. I can roughly outline a
direction for empirical tests, though the experimental design would
need refinement of details.
1: Not feasible: The hypothesis is infeasible. The variables are
neither measurable nor operationalizable, and they lack clarity. This
makes it difficult to specify their relation empirically or design a
testable experiment.
**Return ONLY a JSON object in the following format**:
novelty: <int, 1 to 9>,
feasibility: <int, 1 to 9>,
likelihood: <int, 1 to 9>
CONTEXT AND PUZZLE:
{context_puzzle}
<SCIENTIST PERSONA>: Your own perspective on this context and puzzle
can be summarized as the following hypotheses:
{idea} (not always provided to LLMs)
HYPOTHESIS TO BE JUDGED:
{hypothesis}
Model Evaluation with Explicit Requirement of Extreme Scores
<Same as the model evaluation prompt>
**Assign an explicit low (1) or high (9) rating when a quality
dimension is clearly poor or excellent.**

62

Model Evaluation with Direct Comparison
System Prompt:
You are an experienced scientist who is judging ideas (hypotheses)
proposed from the same context and puzzle as your own paper.
User Prompt:
You will be given:
1. the context: background information and the research puzzle of
the paper
2. two proposed hypotheses: Hypothesis A and Hypothesis B proposed
based on the given context
Your task:
Compare the two hypotheses on novelty according to the following
criteria:
"To what extent do the generated hypotheses - based on the given
context - generalize and introduce new, unseen, and interesting
ideas?”
[Replace novelty with other dimensions:]
Feasibility: "How empirically feasible are the hypotheses? Relations
between variables in an empirically feasible hypothesis should be
operationalizable, measurable, implementable, and testable.”
Probability: "How believable the hypotheses sound, based on existing
knowledge or internal logic? A probable (likely true) hypothesis
should be intuitive.”
Context:
{context}
Hypothesis A:
{left_resp}
Hypothesis B:
{right_resp}
Respond with ONLY one word:
if Hypothesis B is better.

"left” if Hypothesis A is better, "right”

Reward Model Training Prompt
criteria_definitions = {
"probability": (
"How believable the hypotheses sound, based on existing knowledge

63

or internal logic? A probable (likely true) hypothesis should be
intuitive."
),
"novelty": (
"To what extent do the generated hypotheses - based on the given
context - generalize and introduce new, unseen, and interesting ideas?"
),
"feasibility": (
"How empirically feasible are the hypotheses? Relations between
variables in an empirically feasible hypothesis should be
operationalizable, measurable, implementable, and testable."
)
}
You are an experienced scientist evaluating a scientific hypothesis.
Criterion: {criterion_definition}
Context and puzzle: {context_puzzle}
Your own perspective on this context and puzzle can be summarized as
the following hypotheses:
{idea}
Please evaluate the assistant’s hypothesis with respect to this
criterion:
{hypotheses to be judged}
Generation of Null Hypotheses
You are an experienced scientist.
null: Based on the following information, write one possible NULL
hypothesis: A null hypothesis is a default assumption that there is no
effect, no difference, or no relationship between variables. It is the
hypothesis a study seeks to test or potentially reject.
not_null: Based on the following information, write one possible
ALTERNATIVE (non_null) hypothesis: An alternative hypothesis proposes
that there is an effect, a difference, or a relationship between
variables. It is what researchers hope to support through evidence.
Robustness Check for the Detection of AI Use
You are an experienced scientist.
Does the following paper involve AI and machine learning?
**ONLY 1 (yes) or 0 (no)**.
Text: {text}
64

Return

B.2

The pilot study, the recruitment email, and the survey

We administered the survey on Qualtrics, distributing the first pilot study to a random
sample of 400 recipients. Among them, 241 reported being satisfied or at least content with
the AI-generated ideas, indicating a generally positive attitude. The remaining respondents
expressed skepticism, describing the ideas as superficially plausible yet lacking substantive
coherence. The recruitment email (SI Figure 2)13 and the survey are provided below.
The survey:
Thank you for participating! We are a group of researchers at the Knowledge Lab and Data
Science Institute, University of Chicago. We are studying whether AI can help scientists
extend their work in new directions, and especially, propose novel, empirically feasible, and
likely true scientific hypotheses.
In this survey, you will see a few AI-generated hypotheses that were developed based on your
own preprint "${e://Field/title}”. Each will come with a short context (e.g., definitions
of concepts and the scientific puzzle discussed in your paper). We greatly value your expert
feedback on them – particularly regarding their novelty, empirical feasibility, and likelihood
of being true. Your input will enable the entire scientific community to assess whether
transitioning toward a more AI-driven pipeline is warranted.
Expected time: around 15 minutes. You will evaluate 5 hypotheses, each judged across three
dimensions, and respond to several related questions.
• You may withdraw at any time by closing the survey.
• Participation is voluntary and has no impact on your publication record.
• Your participation in this study does not involve any risk to you beyond that of everyday
life. However, you may feel mild frustration or discomfort if AI-generated hypotheses
misrepresent your work or seem poor in quality. Please note that some AI-generated hypotheses may be intentionally weak, as these serve as valuable data points for evaluation
purposes.
• Your ratings and the fine-tuned machine learning models derived from them will be
shared openly with the research community after proper de-identification. We wish to
assure you that this project is intended solely for scientific research, with no commercial
13

This is the final version. We revised it from slightly different earlier versions of the email after observing that some scientists strongly disliked AI and responded with inappropriate messages, while some were
highly enthusiastic about AI and sent messages offering praise and seeking further collaboration with us —
something we had not anticipated during the pilot study. This is actually exactly our intention: to cover a
wide spectrum of positions.

65

objectives.
• If you would like the final draft, technical details, aggregate results, and AI-generated
hypotheses later, you can opt in at the end.
This project is conducted under the University of Chicago IRB25-1372, titled "The Capabilities and Potential of AI for Automating Scientific Idealization: A Large-Scale Human-in-theLoop Study”. If you have any questions about your rights as a participant in this research,
feel you have been harmed, or wish to discuss other study-related concerns with someone
who is not part of the research team, you can contact the University of Chicago Social &
Behavioral Sciences Institutional Review Board (IRB) Office by phone at (773) 702-2915, or
by email at sbs-irb@uchicago.edu.
Project Lead
Honglin Bao: PhD student at UChicago Data Science Institute.
honglinbao@uchicago.edu
James A. Evans: Max Palevsky Professor at UChicago Data Science Institute and Sociology.
jevans@uchicago.edu

◦ I have read the information above and agree to participate.
◦ I do not agree to participate.

Are you an author of the following paper?
${e://Field/title}

◦ Yes
◦ No
(If the answer is no, the survey will automatically end)
How familiar are you with this paper’s content?

◦ 1 = I almost forgot the paper’s content
◦ 2 = I can only remember part of the content
◦ 3 = I remember the content, but I am not quite confident about my judgment
66

◦ 4 = I was deeply involved in this research. I remember this piece. I am confident about
my judgment

◦ 5 = I supervised/led this research. I remember this piece very well. I am very confident
about my judgment
(We only used ratings from authors with a confidence score above (and including) 3)

Context review
Before you evaluate the AI-generated scientific hypotheses, we would like to know to what
extent the context, the puzzle, and the extracted hypotheses reflect your own paper.
Please review the information below and answer the questions.
Paper:
${e://Field/title}
Context and puzzle:
${e://Field/context_puzzle}
Extracted human hypotheses:
${e://Field/human}
How well do you feel the extracted context and puzzle represent what you actually did in your paper, e.g., the basic concepts and topics you explored?

◦ Very good. They are indeed what I did.
◦ Good. They are generally fit.
◦ They are OK with some deviations from what I did.
◦ They are hallucinations.
(Only 0.3% scientists chose the fourth option "hallucinations")
How well do you think the extracted hypotheses capture the hypotheses, explicitly or implicitly, included in your own paper?

◦ Very good. They are indeed what I did.
67

◦ Good. They are generally fit.
◦ They are OK with some deviations from what I did.
◦ They are hallucinations.
(Only 1.4% scientists chose the fourth option "hallucinations")

Instructions
In this study, you will judge the novelty, empirical feasibility, and probability (likelihood of
being true) of the given hypotheses in relation to your paper.
A hypothesis here can be a testable idea, or more broadly, a guiding assumption in research
methods, design, and direction. You will see a set of hypotheses that may be rephrased
directly from your own paper or proposed by AI based on the content of your paper.
Please use the following definitions:
• Novelty: To what extent do the generated hypotheses – based on the given context –
generalize and introduce new, unseen, and interesting ideas?
• Empirical feasibility: How empirically feasible are the hypotheses? Relations between
variables in an empirically feasible hypothesis should be operationalizable, measurable,
implementable, and testable.
• Probability (likelihood of being true): How believable the hypotheses sound, based
on existing knowledge or internal logic? A probable (likely true) hypothesis should be
intuitive.
Please do not evaluate format, writing style or grammar except where it prevents understanding.
To familiarize you with the evaluation criteria, please answer the following practice questions.

Practice questions
Which hypothesis is more probable, i.e., likely to be true?

68

◦ Regular physical exercise reduces the risk of cardiovascular disease in adults.
◦ Drinking two liters of soda per day enhances memory retention in older adults.
(The correct answer: the first one)
Which hypothesis is more novel? Context: Students in urban high schools consistently underperform on standardized science exams compared to their suburban counterparts. While factors such as funding, class size, and teacher experience have been well studied, they do not fully explain the persistent performance gap.
The puzzle: Why do students in urban high schools continue to underperform in science
despite comparable teacher credentials and similar classroom resources?

◦ Urban students’ lower science achievement may stem from prolonged exposure to highinformation-density environments in urban areas, which trains the brain to favor a "fastresponse cognitive mode” while weakening the "slow-reasoning circuits” essential for scientific thinking.

◦ Larger class sizes and the associated lower individual attention from teachers lead to
decreased academic performance in science subjects among students in urban areas, compared to their peers in suburban areas.
(The correct answer: the first one, as class size has been well studied in the provided context)
Which hypothesis is more empirically feasible and testable?

◦ Even in a society where all individuals share a unified collective consciousness, social
conflict would still persist.

◦ More English listening practices could improve the English writing scores among highschool students.
(The correct answer: the second one. The survey will not continue unless participants fill in
all the right answers)

Hypothesis evaluation
Given the context and puzzle, please evaluate the following hypothesis generated by AI.
You will assess three dimensions independently, followed by an overall favorability rating of
adoption (i.e., the extent to which the hypothesis is worth pursuing). AI models did not
69

have access to your paper’s conclusions, though they may still have proposed similar ideas.
Hypothesis (5 in Total): ${lm://Field/1 to 5}
Please rate the novelty on a scale from 1 to 9.
Rating Guide:
• 9 – Highly novel: The hypothesis generalizes and stands out significantly from the
given context following an unconventional reasoning path. If empirically validated, it
could unlock a range of new, impactful, and interesting implications.
• 5 – Moderately novel: The hypothesis introduces some new ideas, but they are expected given the context.
• 1 – Not novel: The hypothesis is essentially a rephrasing of the content in the provided
context, with no meaningful innovation.
1 (Not
novel)

2

3

4

5

6

7

8

9
(Highly
novel)

◦

◦

◦

◦

◦

◦

◦

◦

◦

Please rate the probability, i.e., likelihood of being true, on a scale from 1 to 9.
Rating Guide:
• 9 – Highly probable: The hypothesis makes sense. It is highly likely to be true, even
without empirical validation.
• 5 – Moderately probable: The hypothesis has an equal chance of being true or false;
it requires experimental validation.
• 1 – Not probable: The hypothesis is incoherent, logically flawed, and very likely to be
false.
1 (Not
probable)

2

3

4

5

6

7

8

9
(Highly
probable)

◦

◦

◦

◦

◦

◦

◦

◦

◦

Please rate the empirical feasibility on a scale from 1 to 9.

70

Rating Guide:
• 9 – Highly feasible: The hypothesis clearly states relationships between variables,
including null or negative relations (e.g., "A has no relationship with B”). The variables
are operationalizable, and I can readily envision experiments to test the hypothesis.
• 5 – Moderately feasible: The hypothesis refers to some identifiable variables and implies a general relationship, but the variables lack clear definitions or operationalization. I
can roughly outline a direction for empirical tests, though the experimental design would
need refinement of details.
• 1 – Not feasible: The hypothesis is infeasible. The variables are neither measurable nor
operationalizable, and they lack clarity. This makes it difficult to specify their relation
empirically or design a testable experiment.
1 (Not
feasible)

2

3

4

5

6

7

8

9
(Highly
feasible)

◦

◦

◦

◦

◦

◦

◦

◦

◦

(The order of the quality-dimension questions and the hypotheses is randomized)

After reviewing all five AI-generated hypotheses, how likely would you be to
study the following one for a new research paper? This could be your overall favorability of adoption and the judgment of the overall "quality” of hypotheses.
${lm://Field/1 to 5} for five hypotheses
1 (Not at
all)

2

3

4

5

6

7 (Very
much)

◦

◦

◦

◦

◦

◦

◦

(The order of the hypotheses is randomized)

Follow-up
If you are not the original recipient of this survey but still complete it (for example, if it was
forwarded by your coauthor), please provide your email address below.
□ I am NOT the original recipient. This is my email:
71

□ I am the original recipient.
We will follow up with you to share the aggregate results once the study is complete.
□ I am interested in the aggregate result.
□ I am not interested in the aggregate result.
Any other comments or suggestions?

Thank you for your time and expertise. Your judgments will help us evaluate and improve
automated scientific discovery systems. We appreciate your contribution!

72

C

SI Tables and Figures

SI Table 1. Pearson correlation of conditional perplexity across judge models.
This table shows the model perplexity of AI-generated ideas conditioned on the context and
puzzle across 7B models. The perplexities these models produce are highly correlated with
one another, but not with human judges’ assessments of novelty.
Qwen2-7B
Mistral-7B
Llama2-7B
Deepseek-llm-7b-base

Qwen2-7B
1.000000
0.869664
0.842063
0.919653

Mistral-7B
0.869664
1.000000
0.936273
0.900076

73

Llama2-7B
0.842063
0.936273
1.000000
0.882319

Deepseek-llm-7b-base
0.919653
0.900076
0.882319
1.000000

SI Table 2. Simulation model parameters. Note that as our survey empirically demonstrates, null-suppression rates are substantial for both humans and AI, and markedly higher
for AI.
Parameter

Value

Description

ω
m
seed
n0
n1
ρ0
ρ1
s0
s1
Bh
σ
τ

1.0
20,000
0
3
30
0.01
0.20
0.90
0.98
0.10
1.0
1.0

scale of the true-effect law θj ∼ |N (0, ω 2 )|
size of the sampled truth space {θj }
random seed for drawing the truth space
baseline number of studies at AI use a=0
number of studies at a=1
error correlation for human research
error correlation under full AI automation
null-suppression rate for human research
null-suppression rate under full AI automation
blind-spot bias at a=1
noise scale
field maturity factor (baseline; varied as [0.6, 1.2, 1.8])

74

SI Table 3. Adoption decisions with author fixed-effects vs. ordered logit models.
The major conclusions are robust to Extended Data Figure Table 2.
(1) Author FE (OLS)

(2) Ordered Logit

0.121***
(0.006)
—

0.164***
(0.008)
0.291***
(0.014)
0.186***
(0.008)
0.111***
(0.015)
0.407***
(0.009)
0.579***
(0.016)
1.649***
(0.154)
0.508**
(0.189)
-0.189**
(0.062)
-0.212
(0.463)
0.051
(0.070)
0.135**
(0.052)
-0.152***
(0.047)
—

Novelty (within)
Novelty (between)
Feasibility (within)

0.129***
(0.006)
—

Feasibility (between)
Probability (within)

0.313***
(0.006)
—

Probability (between)
Human-AI idea similarity (within)

1.281***
(0.119)
—

Human-AI idea similarity (between)
Seniority

—

Prior AI usage (log)

—

Chemistrya

—

Medicinea

—

Social sciencea

—

Constant

0.000
(0.000)

Observations
R2
Adj. R2
Log-Likelihood
AIC
BIC

23,855
0.304
0.304
-37,039
74,090
74,130

Standard errors in parentheses. *** p<0.001, ** p<0.01, * p<0.05.
a
Biology is the baseline field.
Column (1) uses the author-fixed effect model, so only within-author
variation is identified; between-author and time-invariant controls drop out.

75

23,615
—
—
-37,077
74,190
74,350

SI Table 4. Regression results with all tested interactions between seniority,
field, and quality dimensions. Conclusions of Extended Data Tables 3 and 4 are robust.
Favorability of Adoption
Intercept

-0.8070***
(0.126)

Biology

-0.0983
(0.076)
-0.0545
(0.125)
0.0340
(0.101)

Chemistry
Medicine
Novelty (within)

0.1338***
(0.014)
-0.0143
(0.017)
-0.0142
(0.027)
-0.0084
(0.021)
0.2178***
(0.010)

Novelty (within) × Biology
Novelty (within) × Chemistry
Novelty (within) × Medicine
Novelty (between)
Feasibility (within)

0.1316***
(0.012)
-0.0036
(0.015)
-0.0183
(0.025)
0.0094
(0.021)
0.0742***
(0.012)

Feasibility (within) × Biology
Feasibility (within) × Chemistry
Feasibility (within) × Medicine
Feasibility (between)
Probability (within)

0.2692***
(0.013)
0.0584***
(0.016)
0.0208

Probability (within) × Biology
Probability (within) × Chemistry

Continued on next page

76

Favorability of Adoption
(0.025)
0.0632**
(0.022)
0.4457***
(0.012)

Probability (within) × Medicine
Probability (between)
Human-AI Idea Similarity (within)
Human-AI Idea Similarity (within) × Biology
Human-AI Idea Similarity (within) × Chemistry
Human-AI Idea Similarity (within) × Medicine
Human-AI Idea Similarity (between)
Seniority

1.1298***
(0.232)
0.1499
(0.286)
-0.6233
(0.565)
0.5567
(0.377)
0.4927***
(0.148)
-0.5073***
(0.112)
0.4451***
(0.129)
0.4364*
(0.208)
0.3919*
(0.174)

Seniority × Biology
Seniority × Chemistry
Seniority × Medicine
Prior AI Use (log)

-0.1605
(0.382)

Observations
R2

23,615
0.397

*** p < 0.001, ** p < 0.01, * p < 0.05. Field-level comparisons use social science as the baseline.

77

SI Table 5. Nonresponse-adjusted estimates of adoption. Major conclusions in the
main text are robust.

Novelty (within)
Novelty (between)
Feasibility (within)
Feasibility (between)
Probability (within)
Probability (between)
Idea similarity (within)
Idea similarity (between)
Seniority
Prior AI use
Biology
Chemistry
Medicine
Constant
Observations (ideas)

(1)
Unweighted

(2)
Inverse probability weighted

0.123∗∗∗
(0.006)
0.219∗∗∗
(0.010)
0.130∗∗∗
(0.006)
0.073∗∗∗
(0.012)
0.314∗∗∗
(0.006)
0.447∗∗∗
(0.012)
1.284∗∗∗
(0.120)
0.473∗∗∗
(0.148)
−0.161∗∗∗
(0.049)
−0.170
(0.382)

0.122∗∗∗
(0.006)
0.218∗∗∗
(0.010)
0.129∗∗∗
(0.006)
0.073∗∗∗
(0.012)
0.315∗∗∗
(0.006)
0.448∗∗∗
(0.012)
1.272∗∗∗
(0.120)
0.493∗∗∗
(0.147)
−0.157∗∗∗
(0.049)
−0.232
(0.384)

0.125∗∗∗
(0.037)
0.164∗∗
(0.061)
0.230∗∗∗
(0.050)
−0.972∗∗∗
(0.117)

0.128∗∗∗
(0.037)
0.164∗∗
(0.061)
0.233∗∗∗
(0.050)
−0.987∗∗∗
(0.117)

23,615

23,615

Notes: Social science is the omitted field category (the reference). Continuous evaluation measures are decomposed into researcher-specific means (between) and deviations from those means (within). Standard errors are clustered in parentheses.
Model 1 (the unweighted model) replicates the main result in the paper (Extended
Data Table 2 Model 1). ∗∗∗ p < 0.001, ∗∗ p < 0.01, ∗ p < 0.05.

78

SI Figure 1. Test accuracy versus global training step for five candidate models.
All models are trained using 2 GPUs except Qwen3-14B and Qwen3-32B, which are trained
using 4 GPUs. As a result, each global step for these two models corresponds to twice the
amount of data processed compared to the 2-GPU training, accounting for their half global
steps compared to others.

79

SI Figure 2. The recruitment email.

80

References
1

O’Neill, C. et al. Sparks of science: Hypothesis generation using structured paper data.
arXiv preprint arXiv:2504.12976 (2025).

2

Cockburn, A., Dragicevic, P., Besançon, L. & Gutwin, C. Threats of a replication crisis
in empirical computer science. Communications of the ACM 63, 70–79 (2020).

3

Denning, P. J. The science in computer science. Communications of the ACM 56, 35–38
(2013).

4

Touvron, H. et al. Llama: Open and efficient foundation language models. arXiv preprint
arXiv:2302.13971 (2023).

5

Soldaini, L. et al. Dolma: An open corpus of three trillion tokens for language model
pretraining research. In Proceedings of the 62nd Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers), 15725–15788 (2024).

6

Gao, L. et al. The pile: An 800gb dataset of diverse text for language modeling. arXiv
preprint arXiv:2101.00027 (2020).

7

Weber, M. et al. Redpajama: An open dataset for training large language models.
NeurIPS 37, 116462–116492 (2024).

8

Kandpal, N. et al. The common pile v0.1: An 8tb dataset of public domain and openly
licensed text. arXiv preprint arXiv:2506.05209 (2025).

9

Wu, S., Bao, H., Li, S., Holtzman, A. & Evans, J. A. Mapping overlaps in benchmarks
through perplexity in the wild. ICLR (2026).

10

Wolfram, C. & Schein, A. Layers at similar depths generate similar activations across llm
architectures. COLM (2025).

11

Zhang, L., Lu, W. & Yang, J. Lagos-and: A large gold standard dataset for scholarly
author name disambiguation. Journal of the Association for Information Science and
Technology 74, 168–185 (2023).

12

Song, K., Tan, X., Qin, T., Lu, J. & Liu, T.-Y. Mpnet: Masked and permuted pre-training
for language understanding. NeurIPS 33, 16857–16867 (2020).

13

Bao, H., Sun, M. & Teplitskiy, M. Where there’s a will there’s a way: Chatgpt is used
more for science in countries where it is prohibited. Quantitative Science Studies 1–16
(2025).

81

14

Bao, H., Zhang, J., Cao, M. & Evans, J. A. From division to unity: A large-scale study
on the emergence of computational social science, 1990-2021. In Companion Proceedings
of the ACM on Web Conference 2025, 859–863 (2025).

15

Hao, Q., Xu, F., Li, Y. & Evans, J. Artificial intelligence tools expand scientists’ impact
but contract science’s focus. Nature 1–7 (2026).

16

Tan, Z. et al. Large language models for data annotation and synthesis: A survey. In
EMNLP, 930–957 (2024).

17

Schunck, R. Within and between estimates in random-effects models: Advantages and
drawbacks of correlated random effects and hybrid models. The Stata Journal 13, 65–76
(2013).

18

He, P., Liu, X., Gao, J. & Chen, W. Deberta: Decoding-enhanced bert with disentangled
attention. ICLR (2021).

19

Feng, T., Sun, Y. & You, J. Grapheval: A lightweight graph-based llm framework for
idea evaluation. ICLR (2025).

20

Wu, S., Bao, H., Kunievsky, N. & Evans, J. A. Automatically advancing llm expertise in
technology judgment. arXiv preprint arXiv:2505.12452 (2025).

21

Rosenthal, R. The file drawer problem and tolerance for null results. Psychological Bulletin
86, 638 (1979).

22

Chen, H., Rider, C. I., Jurgens, D. & Teplitskiy, M. Geographical disparities in navigating rejection in science drive disparities in its file drawer. In Academy of Management
Proceedings, vol. 2025, 18866 (2025).

82
