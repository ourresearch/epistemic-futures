---
title: "The Rise and Fall of $G$ in AGI"
person: david-krakauer
section: by
type: journal-article
year: 2026
date: 2026-04-10
venue: "arXiv (Cornell University)"
authors: "David C. Krakauer et al."
source_url: https://arxiv.org/abs/2604.09911
retrieved: 2026-08-13
content: full-text
notes: "OA status: green; OpenAlex W7154540606; cited_by 0. Abstract reconstructed from OpenAlex abstract_inverted_index. Full text fetched 2026-08-13 via OpenAlex Content API (grobid_xml -> prose extraction)."
---

# The Rise and Fall of $G$ in AGI

## Full text

**Abstract.** In the psychological literature the term 'general intelligence' describes correlations between abilities and not simply the number of abilities.This paper connects Spearman's g-factor from psychometrics, measuring a positive manifold, to the implicit "G-factor" in claims about artificial general intelligence (AGI) performance on temporally structured benchmarks.By treating LLM benchmark batteries as cognitive test batteries and model releases as subjects, principal component analysis is applied to a models × benchmarks × time matrix spanning 39 models (2019-2025) and 14 benchmarks.Preliminary results confirm a strong positive manifold in which all 28 pairwise correlations positive across 8 benchmarks.By analyzing the spectrum of the benchmark correlation through time, PC1 explains 90% of variance on a 5-benchmark core battery (n = 19)) reducing to 77% by 2024.On a four benchmark battery, PC1 is found to peak at 92% of the variance between 2023-2024 and reduce to 64% with the arrival of reasoningspecialized models in 2024.This is coincident with a rotation in the G-factor as models outsource 'reasoning' to tools.The analysis of partial correlation matrices through time provides evidence for the evolution of specialization beneath the positive manifold of general intelligence (AIhedgehog) encompassing diverse high dimensional problem solving systems (AI-foxes).In strictly psychometric terms, AI models exhibit general intelligence suppressing specialized intelligences.LLMs invert the ideal of substituting complicated models with parsimonious mechanisms, a 'Ptolemaic Succession' of theories, with architectures of increasing hierarchical complication and capability.

1 Analytics of Generality

### The Positive Manifold

In 1904, Spearman observed that scores on diverse cognitive tests were positively correlated and proposed a single latent variable g, "general intelligence"-to account for this positive manifold (Spearman, 1904).The observation was robust: across batteries of tests, populations, and cultures, the intercorrelation matrix of cognitive tasks is overwhelmingly positive, and a single first principal component typically accounts for 40-60% of variance (Jensen, 1998;Carroll, 1993).

The case for g rests on convergent evidence.The statistical regularity is well established: the positive manifold has been replicated across diverse test batteries and populations (Johnson et al., 2008).Carroll's survey of factor-analytic studies, building on Cattel's typology (Cattell, 1963) established a hierarchy-g at the top, broad abilities (fluid reasoning G f , crystallized knowledge G c , and others) in the middle and narrow abilities at the base (Carroll, 1993).And g is a strong predictor of job performance, educational attainment, and health outcomes across occupations and contexts (Gottfredson, 1997).Evidence also exists for g in mice (Matzel et al., 2003).Different test batteries, constructed independently and measuring ostensibly different abilities, yield g-factors that correlate at r > 0.95 (Johnson et al., 2004).Jensen's characterization of g as a "distillate" of cognitive performance extracted by factor analysis from a limited set of tasks captures both its narrowness and its consistency (Jensen, 2002).

Challenges to the theoretical significance of g are numerous and include the fact that it tends to collapse informative factors or abilities (Thurstone, 1938) (Gardner, 1983).It places excessive emphasis on analytical forms of reasoning over creative and practical reasoning (Sternberg, 1985;Gottfredson, 2003), and arises easily from overlaps in sampling processes (Thomson, 1916;Bartholomew et al., 2009).Moreoever g is expected to grow as a natural consequence of overlapping processes (Kovacs and Conway, 2016) and developmental mutualisms (van der Maas et al., 2006).A recent extension to these synergistic frameworks is that of Savi et al. in which intelligence is conceptualized as an evolving graph of densely connected facts and procedures (Savi et al., 2019).

### Psychometric g vs Psychological g

The debate centers around a distinction that is relevant to the analysis of LLM benchmarks.Psychometric g (the first principal component of a battery of cognitive tests) is a statistical regularity.Psychological g, understood as a causal entity or a single cognitive capacity that explains why tests correlate, is a theoretical possibility.Spearman's notion of "mental energy," Jensen's characterization of g as processing speed or neural efficiency, and the parieto-frontal integration theory's identification of g with a specific brain network all represent claims about psychological g (Jung and Haier, 2007).Thomson's sampling theory, mutualism, and process overlap theory accept a limited form of psychometric g while denying psychological g.As Savi et al. put it, psychometric g is an index that summarizes a system without causing it (Savi et al., 2019).And the correlation versus causation debate has been extended to general intelligence across many species (Burkart et al., 2017).

### From g to G: The AGI Debate

The AI community has conducted a parallel debate about "general intelligence" in tests on artificial systems, largely without reference to the test of human intelligence literature.This is not a criticism but a surprising observation based on the fact, as described above, that the psychometric literature does have a definition of 'general intelligence'.The central claim that large language models exhibit a form of general intelligence was made explicitly by Bubeck et al. in "Sparks of Artificial General Intelligence," which showed that GPT-4 could solve novel tasks spanning mathematics, coding, medicine, and law.Hendrycks et al. (Hendrycks et al., 2025) proposed a quantitative definition of AGI grounded in the Cattell-Horn-Carroll (CHC) theory defining AGI as an AI that matches or exceeds the cognitive versatility and proficiency of a well-educated adult.LLMs are typically evaluated on batteries of benchmarks-MMLU (Hendrycks et al., 2021a), GSM8K (Cobbe et al., 2021), HumanEval (Chen et al., 2021), GPQA (Rein et al., 2024), MATH (Hendrycks et al., 2021b)-and performance across these batteries is taken as evidence for or against "general" intelligence.Responses to the "Sparks" claim have divided along lines that parallel the psychometric debate about g.Chollet argued that benchmark performance measures skill, not intelligence, and that skill can be purchased with sufficient training data without implying any general reasoning capacity (Chollet, 2019).Morris et al. have proposed a "Levels of AGI" framework that attempted to operationalize the concept by distinguishing depth (performance on specific tasks) from breadth (generality across tasks), and argued that current systems occupy a position of "Competent" narrow AI rather than any level of genuine AGI (Morris et al., 2023).

### Temporal Psychometrics of Transformers

This paper pursues an opportunity provided by LLMs: the positive manifold can be observed as models evolve in response to benchmarks.The LLM setting recapitulates the psychometric structure as models are evaluated on benchmark batteries and performance is positively correlated across tasks.The "subjects" (models) are released in a known temporal order with documented architectural differences, so the eigen-structure can be tracked across algorithmic epochs.Benchmarks saturate and are replaced on a timescale of months rather than decades, making the moving-battery problem tractable.And the distinction between statistical and mechanistic G can be mapped onto the Spearman-vs-Thomson debate: if the positive manifold in LLM benchmarks reflects a shared inferential mechanism (the transformer architecture, the language-modeling objective), it is closer to a mechanistic G; if it reflects the shared training corpus or the trivial temporal trend of latermodels-being-better, it is closer to a statistical G.

The claim that a model is approaching AGI should be a straightforward claim about the timedependent structure of its benchmark correlation matrix.In time a single dominant eigenvalue, the Principal Component, should come to account for cross-task performance.This paper makes the analogy explicit, and by dividing benchmarks into distinct model epochs, asks whether it is substantive.It is argued that a more pragmatic approach might be better off adopting the language of the 'Dimension of Intelligence', which is quantitatively justifiable, and allows for different forms of intelligence, animal or artificial, to occupy different subspaces of competence.

In prior work Ilic and Gignac (Ilić and Gignac, 2024) found strong evidence for a positive manifold in LLM performance, with a dominant leading g-factor accounting for around 66 percent of test variance.Ilic and Gignac analyze 12 benchmarks organized into four broad-ability categories using confirmatory factor analysis and conclude that performance on benchmarks justifies describing models in terms of achievement rather than intelligence.They propose that Artificial General Achievement (AGA) is a good fit to Cattell's crystallized intelligence and find little evidence for fluid intelligence.This paper builds on the idea that there is value in exploring how psychological metrics might describe AI performance; in this case using principal components to explore correlations across benchmarks with an emphasis on the changing nature of the positive manifold through time.

### Formal Framework

### The Data Structure

Let M = {m 1 , . . ., m N } be a set of N language models, each associated with a release date t(m i ) ∈ R and an organization org(m i ).Let B = {b 1 , . . ., b K } be a set of K benchmarks.Define the score matrix :

X ∈ R N ×K , X ij = score of model m i on benchmark b j (1)

where scores are normalized to [0, 100] (percentage correct).Missing entries are denoted X ij = NaN.

The structure of the score matrix is shown schematically in Figure 1: models are ordered by release date (rows), benchmarks are grouped by cognitive domain (columns), and the pattern of missing data indicates sparsity in the upper-left (early models, early benchmarks) and lower-right (late models, new benchmarks).Definition 2 (G-factor).The G-factor is the first principal component of the standardized score matrix Z = StandardScaler(X).The G-loading of benchmark b j is the j-th element of the first eigenvector v 1 of the correlation matrix R = Z ⊤ Z/(N -1).The G-score of model m i is its projection onto v 1 :

G(m i ) = z i • v 1 = K j=1 z ij v 1j (2)

### Eigenvalue Diagnostics

The eigenvalues λ 1 ≥ λ 2 ≥ • • • ≥ λ K of R encode the factor structure.Three diagnostic quantities characterize the factor structure:

(i) Variance ratio: ρ 1 = λ 1 / k λ k .A high ρ 1 indicates a dominant general factor.

(ii) Dominance ratio: δ = λ 1 /λ 2 .A high δ indicates that the first factor is clearly separated from the second.

(iii) Effective dimensionality:

d eff = ( k λ k ) 2 / k λ 2 k (participation ratio). d eff ≈ 1 indicates a single dominant factor; d eff ≈ K indicates uniform spread.

For factor retention, the Kaiser criterion is applied (λ k > 1) and Horn's parallel analysis (Horn, 1965), which compares observed eigenvalues to those expected under random permutation of the data matrix.

### Connection to Psychometric g

In psychometrics, the subjects are sampled from a natural population (humans), and the positive manifold reflects shared cognitive architecture.In the LLM setting, the "population" of models is an engineered trajectory where each model is designed to improve upon its predecessors.This introduces some important structural differences.Models are not independent draws from a distribution but temporally ordered optimizations.This inflates between-era correlations (early models are bad at everything; late models are good at everything).All transformer-based LLMs are trained on overlapping internet-scale corpora, potentially inducing positive correlations through shared data rather than shared mechanism.Benchmarks are designed with knowledge of model capabilities, and labs optimize against known benchmarks, creating a feedback loop absent from psychometric testing.

### Results

### Data

The score matrix comprises N = 39 models and K = 14 benchmarks spanning February 2019 to December 2025.Models represent major releases from OpenAI, Anthropic, Google, Meta, DeepSeek, and Mistral.Benchmark scores are drawn from published technical reports, model cards, and third-party evaluations (Epoch AI, 2024).All scores are converted to a 0-100 percentage scale.The matrix has 42% overall coverage, with higher coverage for earlier benchmarks (MMLU: 77%) and lower for newer ones (SWE-bench Verified: 21%).The problem with the current state of data is its small sample size.This makes rigorous statistical conclusions provisional.When statistical confidence is significant this will be stated clearly in the manuscript.Otherwise the results should be seen as descriptive and awaiting further data.See Appendix B for permutation analysis.

### Benchmark Saturation

The raw data exhibit a clear pattern: frontier model performance on every major benchmark has increased monotonically over the 2020-2025 period, with different benchmarks reaching saturation (> 90%) at different times (Figure 2).This represents correlated growth across diverse tasks including general knowledge (MMLU), mathematical reasoning (MATH, GSM8K), code generation (HumanEval), and scientific knowledge (GPQA Diamond).

To characterize the growth dynamics, three functional forms are fit to the frontier envelope-the running maximum score across all models at each time point-for each benchmark: 4-parameter logistic, 4-parameter Gompertz, and linear, selecting by AIC (Table 1).

Table 1: Growth model fits to the frontier envelope.AIC values for logistic (L), Gompertz (G), and linear (Lin) models fitted to the running-maximum score trajectory.Bold indicates the selected model.L denotes the estimated asymptote for sigmoidal fits; n is the number of frontierenvelope points.Figure 2: The phenomenon to be dissected: benchmark performance rising across all tasks simultaneously.Bold markers show the running-maximum score (frontier envelope) for each benchmark; faded markers show all individual model scores.Curves are the best-fit growth model selected by AIC (Table 1).MMLU is best fit by a logistic with asymptote L = 94%; GPQA Diamond by a logistic with L = 92%; HumanEval by a Gompertz with L = 104% (no saturation yet).The shaded region marks > 90% scores where discriminability is lost.The correlated rise across all five benchmarks, despite their testing different cognitive demands, is the positive manifold in its raw form.

### Benchmark

A benchmark saturates when frontier models approach its ceiling, eliminating variance and rendering the benchmark useless for factor analysis.Define the discriminability of benchmark b j at time t as the standard deviation of scores among contemporaneous models: D j (t) = SD({X ij : |t(m i ) -t| < ∆}).When D j (t) → 0, benchmark b j is saturated.This creates a moving battery: the set of informative benchmarks changes over time, complicating longitudinal comparison.

### The Positive Manifold

Across the six benchmarks with sufficient pairwise coverage (MMLU, GSM8K, MATH, HumanEval, GPQA Diamond, MMLU-Pro), all 28 pairwise correlations are positive, confirming the positive manifold (Figure 3).With the updated data matrix, robust pairwise correlations (n ≥ 5) can be computed across 8 benchmarks (MMLU, HellaSwag, ARC, WinoGrande, GSM8K, MATH, Hu-manEval, BBH).Correlations range from r = 0.42 (WinoGrande × MATH) to r = 0.96 (BBH × MMLU; BBH × GSM8K), with a mean of r = 0.82.

### Factor Structure

PCA on the five-benchmark core battery (MMLU, GSM8K, MATH, HumanEval, GPQA Diamond) for the 19 models with complete data yields the eigenvalue structure shown in Table 2.Only PC1 exceeds the Kaiser criterion (λ > 1), supporting a single-factor solution.PC1 explains 90.0% of total variance-substantially stronger than the 40-60% typically attributed to g in human psychometrics, and consistent with the 66% reported by Ilić and Gignac (Ilić and Gignac, 2024) on a much larger sample of 591 models.All benchmarks load positively and near-uniformly on PC1 (range: +0.44 to +0.46), with the highest loadings on MMLU (+0.46) and HumanEval (+0.45) (Figure 4).PC2 (7% variance) separates an execution cluster (GSM8K at +0.62, HumanEval at +0.34: positive PC2 loadings) from a reasoning cluster (GPQA at -0.56, MATH at -0.43: negative PC2 loadings), with MMLU near zero (+0.04).

Figure 4: Factor loading plot for the 5-benchmark core battery.Arrows show each benchmark's loading on PC1 (G-factor, 90% variance) and PC2 (7% variance).All benchmarks load positively on PC1, confirming a general factor.PC2 separates an execution/fluency pole (GSM8K, HumanEval-positive PC2) from a reasoning pole (MATH, GPQA-negative PC2).MMLU is near the origin on PC2, contributing primarily to G rather than to the residual structure.

### G-Scores Across Models and Time

Projecting each model onto PC1 and normalizing to a 0-100 scale yields a G-score (Figure 5).G increases monotonically with release date, rising from Llama 2 70B Chat (G = 0, July 2023, the lowest-scoring model in the complete-data set) through GPT-4 (G = 58) and to the post-September 2024 models (o1-preview, G = 100; DeepSeek R1, G = 100).The expanded sample now includes models from GPT-3.5-Turbo (G = 14) through the Gemini and Claude families, providing a denser trajectory.The rate of G-growth accelerates around mid-2024, coinciding with inference-time reasoning.

### Epoch-Resolved Factor Structure

The scree plots across epochs (Figure 6) reveal the predicted structure.The key quantities are summarized in Table 3.The G-factor peaks during Epoch II (2023-2024.03),when pure scaling dominates and all labs improve uniformly across tasks.It then splinters in Epoch IV (2024.09+),where λ 2 rises above 1.0-suggestive of a two-factor structure, though with n = 4 this cannot be confirmed statistically (see Appendix B).This second factor appears to distinguish "depth of search" (MATH, GPQA: reasoning-chain models excel) from "breadth of recall" (MMLU, GSM8K, HumanEval: scaling models excel).The dominance ratio δ = λ 1 /λ 2 drops from 15:1 (Epoch II) to 1.8:1 (Epoch IV), a pronounced structural break.

### Expanding-Window Dynamics

An expanding-window analysis, produced by adding models chronologically and recomputing the eigenvalue structure at each step, reveals elements of the dynamics of G (Figure 7).The top panel tracks ρ 1 , the normalized fraction of total variance captured by PC1, which remains consistently above 90% from the earliest window through the entire timeline, peaking at 95.5% around the Claude 3 Opus release (early 2024) and settling to 93.3% by the final window.The bottom panel shows all four normalized variance fractions ρ k on a common scale, ρ 1 occupies the upper reaches of the plot while ρ 2 , ρ 3 , and ρ 4 are compressed near the floor.The ratio ρ 1 /ρ 2 peaks at 31:1 around the Llama 3.1 release and then declines to 24:1 as post-2024.09models enter the window.This decline in the ratio occurs not because ρ 1 collapses but because ρ 2 grows from 3.1% to 3.9%-a subtle redistribution of variance from the general factor to the residual structure.The reference line at 25% (uniform distribution across K = 4 components) makes clear how far the empirical spectrum is from "no structure": even at its weakest, G captures nearly four times the variance of the next component.

### Does the Positive Manifold Reduce in Dimension?

A strict positive manifold implies that the effective dimensionality of the benchmark space should decrease as G increases.Two measures track this through the expanding window: (i) the number of principal components required to capture 99% of total variance, and (ii) the participation ratio

d eff = ( k λ k ) 2 / k λ 2

k , which equals 1 when a single factor dominates and K when variance is uniformly spread (Figure 8).

On the 4-benchmark battery (MMLU, GSM8K, MATH, HumanEval), the participation ratio remains close to its minimum at d eff ≈ 1.1-1.2throughout the entire timeline.G has already absorbed essentially all the variance; the manifold is as compressed as it can be.Three of four components are needed for 99% variance, but this residual dimensionality reflects only minor taskspecific variance.

On the 5-benchmark battery (adding GPQA Diamond), a different picture emerges.The participation ratio begins at d eff = 1.3 when GPQA first enters the window (mid-2024) and rises to d eff = 1.9 as reasoning models arrive-a 40% increase in effective dimensionality.The number of components for 99% variance rises from 3 to 5 (i.e., all components).Figure 8: Effective dimensionality of the LLM benchmark space through time.Expanding-window analysis on two benchmark batteries.Top: Number of principal components required for 99% cumulative variance.On the 4-benchmark battery (blue circles), dimensionality stabilizes at 3 of 4-near-maximal compression.On the 5-benchmark battery (purple squares, adding GPQA Diamond), dimensionality rises from 3 to 5 as post-2024.09models enter the window.Bottom: Participation ratio d eff , a continuous measure ranging from 1 (perfect single-factor structure) to K (no structure).The 4-benchmark battery remains near d eff ≈ 1.1 throughout-a near-perfect G.The 5-benchmark battery rises from 1.3 to 1.9, suggestive of a second factor associated with inference-time reasoning.Vertical dotted lines mark algorithmic-epoch boundaries.

Within a fixed set of models the manifold remains maximally compressed: G captures nearly everything, and adding models does not alter the dimensionality.But when a new capability axis appears that the existing battery was not designed to measure the effective dimensionality increases.The manifold shows evidence of growing along a new dimension that harder benchmarks reveal.Each algorithmic epoch compresses the space within its own test battery and epoch transitions open new dimensions that require new benchmarks to detect.The positive manifold holds within each epoch, but the dimensionality of the full manifold grows as the set of distinguishable capabilities expands.

The full eigenvalue spectrum through time makes this conjecture more visible (Figure 9).Each component's marginal contribution to cumulative variance is shown as a stacked band, so the vertical extent of the blue band (G) relative to the total directly encodes the strength of the general factor.

On the 4-benchmark battery (panel a), PC1 accounts for 92-95% of variance throughout, and PC1+PC2 together exceed 97% at every time point.The higher components (PC3, PC4) contribute only thin slivers and the eigenvalue spectrum is essentially one-dimensional from the very first window.This is a near-maximal G in which one dimension suffices to reconstruct the entire benchmark space to within a few percent.

On the 5-benchmark battery (panel b), the spectrum undergoes a degree of structural transition.Initially, PC1 explains 85% and PC1+PC2 reach 97%-comparable to the 4-benchmark picture.With the expanded GPQA coverage, the 5-benchmark expanding window now begins earlier (from Llama 2 70B Chat onward) and includes 19 models.PC1 remains above 90% throughout most of the trajectory, settling at 90% by the final window.PC2 accounts for only 7% and PC3 for 2%.

### Eigenvalue Change-Point Analysis

The CUSUM (cumulative sum) statistic, applied to the sequences {ρ 1 (t)} and {δ(t)} generated by the expanding-window PCA on the 4-benchmark battery.Under the null hypothesis of a stationary factor structure, the CUSUM statistic fluctuates randomly around zero; a systematic excursion indicates a change in the mean level of the diagnostic.Significance follows from a permutation test (10,000 random reorderings of the sequence).

Both diagnostics yield significant change points (Figure 10).The CUSUM on ρ 1 reaches its maximum deviation in early 2024 (p = 0.004, permutation test), coinciding precisely with the transition from Epoch II to Epoch III (early 2024).The CUSUM on δ = λ 1 /λ 2 is even more decisive (p < 0.001), with the maximum deviation occurring at the same boundary.A caveat is in order: the expanding-window eigenvalue sequence is not a standard time series, since successive values share n -1 of n data points, and the permutation test (which shuffles model order) conflates temporal trend with structural change.The pattern suggests that G peaks in early 2024 and then declines, not because G disappears, but because the second factor increases.

### Eigenvector Rotation

For consecutive expanding windows W t and W t+1 , the cosine similarity is computed cos θ between first eigenvectors and report the angular displacement θ in degrees (Figure 11).

On the 4-benchmark battery the maximum angular displacement across all 18 steps is 0.57.The calculation of G, or which benchmarks it weights, does not change as models are added.This nearperfect alignment indicates that, within the 4-benchmark space, the general factor is structurally invariant across the entire 2023-2025 timeline.

On the 5-benchmark battery, a different pattern emerges.Most steps show small rotations (1-3), but the entry of DeepSeek V3 produces a 6.4 rotation-an order of magnitude larger than anything observed in the 4-benchmark analysis.This is a rotation of the G-factor following the addition of a model with a distinctive reasoning/knowledge profile thereby changing the loadings across benchmarks.The lower panel of Figure 11 confirms that individual benchmark loadings on G are essentially invariant in the 4-benchmark battery (all between |v 1j | = 0.48 and 0.52 throughout), consistent with a fixed general factor.

### Leave-one-out Validation

To calibrate the magnitude of the 6.4 rotation, a leave-one-out (LOO) analysis drops each model in turn from the complete-case set, recomputes PCA on the remaining n -1 models, and measures the angular displacement of PC1 from the full-sample eigenvector.This establishes a baseline distribution of single-model influence on the direction of G.

On the 4-benchmark battery (n = 22), the LOO perturbations are negligible: mean θ LOO = 0.08, max = 0.19 (dropping PaLM 540B), 95th percentile = 0.18.No single model perturbs the eigenvector by more than 0.2.The general factor in this battery is structurally invariant to any individual model.

On the 5-benchmark battery (n = 19), the picture is different and more revealing.The LOO displacements are substantially larger: mean θ LOO = 1.9, with a range from 0.28 (Claude 3 Opus) to 5.58 (DeepSeek V3).Three models produce rotations exceeding 3: DeepSeek V3 (5.58), , and DeepSeek R1 (3.16).The 6.4 rotation observed when DeepSeek V3 enters the expanding window exceeds the LOO maximum of 5.58 from dropping it, but only by a factor of 1.15.DeepSeek V3 is the single most influential model in the 5-benchmark battery; adding or removing it produces comparable perturbations.

### Test (iii): Partial Correlation Structure After Removing G

Projecting out the first principal component from the standardized 5-benchmark matrix exposes the correlation structure of the residuals (Figure 12).If a single G-factor fully explains the positive manifold, the residual correlations should be near-zero and randomly signed.If group factors exist beneath G, the residuals will show systematic positive correlations within groups and negative correlations between groups-the signature of a hierarchical factor structure.

It is found that 7 of 10 pairwise residual correlations are negative, with a mean residual r = -0.24.The positive manifold in the raw correlations (all 15 positive) is largely attributable to G. Once G is removed, the residual structure is predominantly anti-correlated.This is the pattern for a strong single-factor model with group factors.After removing the shared variance, benchmarks within the same group remain positively correlated, while benchmarks in different groups become negatively correlated revealing suppression in the analysis whereby G masks the group-level structure.Two group factors emerge clearly from the residual matrix:

Group I: Reasoning: MATH and GPQA Diamond are strongly positively correlated in the residuals (r resid = +0.59).These benchmarks test multi-step reasoning at the difficulty frontier.MMLU is no longer part of this cluster: its residual correlations with MATH (-0.35) and GPQA (-0.15) are negative, indicating that MMLU functions as an isolated benchmark once G is removed.

Group II: Execution/Fluency: GSM8K and HumanEval retain a strong positive residual correlation (r resid = +0.53).These benchmarks are related to procedural execution, step-by-step arithmetic, or code synthesis.

Cross-group correlations are negative: GSM8K×GPQA (r resid = -0.80),HumanEval×GPQA (r resid = -0.68),MMLU×HumanEval (r resid = -0.40).This strong suppressor structure confirms that G is important since it is the primary reason benchmarks appear positively correlated in the raw data.

### Adjudicating Statistical vs Mechanistic G

The most direct test of whether G is statistical (Outcome 1) or mechanistic (Outcome 2) is to ask whether the group factor structure beneath G is stable across epochs.If the same benchmarks cluster together regardless of which epoch is examined, the structure reflects a genuine computational dissociation.If the clusters rearrange, the structure is an artifact of the particular model population.

A methodological subtlety is important here.Test (ii) demonstrated that the G-factor rotates across epochs: the first eigenvector changes direction as new models enter the window.This means that subtracting a global PC1 (computed across all models) from epoch-specific data conflates different G-factors-it removes too much variance along directions that are not the epoch's own G, and too little along directions that are.The correct procedure is to extract PC1 within each epoch's data and subtract only that epoch's G before examining the residual structure.

4-benchmark analysis.Partitioning the 4-benchmark battery into the four epochs defined in Section 4.1, Epochs I (n = 3) and IV (n = 4) have insufficient data (n < K + 1 = 5), but Epochs II (n = 8, ρ 1 = 92%) and III (n = 7, ρ 1 = 80%) provide well-powered comparisons (Figure 13).Of 6 benchmark pairs, 4 maintain the same sign across Epochs II and III; only the two weakest pairs (GSM8K×HumanEval and MATH×HumanEval, both |r resid | < 0.3) flip sign.The stable negatives are MMLU×GSM8K, MMLU×HumanEval, MMLU×MATH, GSM8K×MATH which persist across both epochs, indicating that the trade-off structure beneath G is a genuine feature of the model population, not an artifact of any particular temporal window.

5-benchmark analysis.The expanded GPQA Diamond coverage permits epoch-specific partial correlation analysis on the 5-benchmark battery (K = 5).In Epoch II, the residual correlations are overwhelmingly negative (2 positive, 8 negative).The dominant positive correlation is MATH×GPQA (r resid = +0.92)-competitionmathematics and PhD-level science are tightly coupled once G is removed.The second positive correlation is GSM8K×HumanEval (r resid = +0.41),confirming the execution cluster.The cross-group negatives are strong: GSM8K×GPQA (r resid = -0.74),MMLU×HumanEval (r resid = -0.64).The group structure is crisp: a reasoning cluster (MATH, GPQA) and an execution cluster (GSM8K, HumanEval), with MMLU negatively correlated with nearly everything.

In Epoch III, the pattern shifts.The MATH×GPQA correlation collapses from +0.92 to +0.13-the tight reasoning cluster has splintered.Meanwhile, the number of positive residual correlations rises from 2 to 4: MATH×HumanEval flips from -0.24 to +0.14, and MMLU×GPQA flips from -0.18 to near zero (+0.02).The execution cluster weakens: GSM8K×HumanEval drops from +0.41 to +0.32.But the cross-group negatives remain stable: GSM8K×GPQA is -0.77(was -0.74), and HumanEval×GPQA is -0.54 (was -0.48).

The interpretation is that the group structure beneath G is partly stable and partly epochdependent.The stable features-the strong negative correlation between execution benchmarks (GSM8K) and reasoning benchmarks (GPQA), the negative correlation between MMLU and HumanEvalpersist across both epochs and likely reflect genuine computational dissociations in the transformer architecture.The unstable features, captured by the splintering of the MATH×GPQA reasoning cluster reflects the changing model population as labs begin to specialize.In Epoch II, all models used the same scaling recipe, so MATH and GPQA moved in lockstep; in Epoch III, mixture-ofexperts and early tool augmentation began to decouple these tasks.The verdict is mixed: the broad group structure (reasoning vs. execution) is mechanistic, but the fine-grained within-group couplings are population-dependent. 2024) on a cross-sectional sample of 591 models.

### Discussion

Figure 14 summarizes the principal findings in a three-dimensional space defined by mean benchmark performance, the variance explained by G (ρ 1 ), and the effective dimensionality of the benchmark space (d eff ).Four points are plotted: the within-epoch factor structures for Epoch II and Epoch III, and the all-models factor structure before and after removing the linear time trend.If the positive manifold behaved as Spearman's g predicts, a fixed latent factor that accounts for correlated improvement, the trajectory would follow the dashed green line where performance increases while ρ 1 and d eff remain constant.Instead, the observed trajectory (solid arrow, point 1 to point 2) moves in the opposite direction, as performance rises from 59% to 80%, ρ 1 falls from 92% to 77%, and d eff rises from 1.19 to 1.62.The dashed purple arrow shows that detrending the allmodels data (point 3 to point 4) reproduces this shift whereby removing the temporal trend moves the all-models point from the Epoch II structural region (ρ 1 = 90%, d eff = 1.23) to the Epoch III region (ρ 1 = 77%, d eff = 1.61).Sphere colour encodes the number of negative partial correlations (out of 10 benchmark pairs) after removing each analysis's own G, indicating the strength of the suppressor structure beneath the positive manifold.The projection lines onto the floor and back wall display coordinate pairs for each point.The dimensions of capability are expanding and diversifying they are not collapsing onto a single factor.The psychometric dynamics of AI are not toward AGI but something more interesting involving the outsourcing of tools in order to explore a higher dimensional space of capability.LLMs by virtue of the collective archive on which they are trained, and the technological-tool niche in which they live, show evidence of becoming a society of minds.

### The Primacy of the Positive Manifold

The positive manifold is confirmed by all 28 pairwise correlations across 8 benchmarks returning positive values with a mean of r = 0.82.A single dominant eigenvalue, G, captures 90% of variance in the 5-benchmark core battery (n = 19) and 93% in the 4-benchmark battery.This much is consistent with the psychometric precedent.But what does G actually measure?G loads most heavily on benchmarks that test knowledge-intensive reasoning at the difficulty frontier (MMLU, GPQA, MMLU-Pro, MATH, all at +0.44 to +0.47), and loads more weakly on procedural execution (HumanEval at +0.20).G is not "being good at everything."It is the capacity to generalize across knowledge-informed problems.The residual structure beneath G reveals two group factors and an isolate: a reasoning cluster (MATH, GPQA: r resid = +0.59),an execution cluster (GSM8K, HumanEval: r resid = +0.53),and MMLU, which is largely isolated once G is removed-near-zero residual correlation with GSM8K (+0.01) and negative with MATH (-0.35) and HumanEval (-0.40).Cross-group correlations are strongly negative (GSM8K×GPQA: -0.80; HumanEval×GPQA: -0.68).The detrending analysis (Section 4.9) confirms that this structure is not a temporal artifact: the positive manifold survives completely after removing the linear time trend, with PC1 still significant at p < .0001and all pairwise correlations remaining positive.The picture has affinities with the Cattell-Horn-Carroll hierarchy in human psychometrics (Cattell, 1963;Ilić and Gignac, 2024).

### The Rise and Fall of G

G-scores increase monotonically with release date.This is unsurprising and largely uninformative: later models are better at everything because they are engineered to be.The expanding-window analysis confirms that G dominates throughout, with ρ 1 > 90% across the entire timeline on the 4-benchmark battery.However, the expanding window pools all models cumulatively, so the early models tend to dominate and buffer the late decline revealed by the segmented epoch-specific analysis, which isolates each period and reveals evidence of a decline.

The detrending analysis (Section 4.9) resolves this apparent tension and clarifies the trajectory.The raw all-models G (ρ 1 = 90% on the 5-benchmark battery) is a composite of two contributions: genuine shared structure and temporal inflation from all models improving together.Detrending removes the second and leaves ρ 1 = 77%.This figure matches the within-epoch Epoch III value (also 77%), and the agreement is not coincidental.Within an epoch, models span only a few months, so the temporal trend is negligible and within-epoch PCA is approximately equivalent to detrended PCA.The correspondence confirms that both methods are measuring the strength of G after the shared trajectory of improvement has been removed.

The trajectory that emerges is:

Analysis ρ 1 n Interpretation

Epoch II, within-epoch (5-bench) 92% 7 Genuine G at its peak Epoch III, within-epoch (5-bench) 77% 7 Genuine G after specialization begins All models, detrended (5-bench) 77% 19 Current state of the field, trend removed All models, raw (5-bench) 90% 19 Genuine G + temporal inflation

The within-epoch decline from 92% to 77% cannot be attributed to temporal confounding, because there is almost no temporal trend within a six-month epoch.That 15 percentage-point decline is real architectural divergence-models in Epoch III genuinely share less of their variance than models in Epoch II.And the fact that the detrended all-models figure matches the Epoch III within-epoch figure tells us that the current state of the field, after the temporal tide is drained, is already at the Epoch III level of coherence, not the Epoch II level.The raw 90% was flattering because it was inflated by the shared trajectory of improvement.

The rise (to 92%) occurred during the scaling era, when all labs pursued the same recipe of larger dense transformers trained on more data.The fall (to 77%) reflects architectural divergence as labs began to specialize: mixture-of-experts architectures, inference-time reasoning chains, tool augmentation, and code-specialized fine-tuning.The "rise and fall of G" is therefore better supported than the expanding window alone might have suggested and it is the detrended and within-epoch analyses, not the raw expanding window, that reveal it.

### The Dawn of a New Dimension

In Epoch IV (2024.09+), the second eigenvalue increases (λ 2 = 1.88), and the dominance ratio δ = λ 1 /λ 2 drops from 15:1 to 1.8:1.The benchmark space is suggestive of departure from 1dimension.The second component separates "depth of search" (MATH, GPQA) from "breadth of recall" (MMLU, GSM8K), capturing the distinction between models that invest inference-time compute in reasoning chains (o1, DeepSeek R1) and those that rely on training-time knowledge.There is at least descriptive evidence that the effective dimensionality rises from d eff = 1.3 to d eff = 1.9 on the 5-benchmark battery.In B where a full permutation analysis of statistical significance is performed PC1 remains dominant, albeit declining, but the importance of PC2 cannot be confirmed.At this point a second dimension remains suggestive and awaits more benchmark data.

### Tectonic shifts

The more interesting observation is what happens to the internal structure of G over time.During Epoch II (2023.03-2024.03),the component loadings are nearly uniform: all four benchmarks in the core battery load between +0.48 and +0.51 on PC1, and a single component captures 92% of variance.The models of this period, including GPT-4, Claude 3, Gemini Ultra, Llama 3, all improve in lockstep across all tasks.G is essentially a scalar and the only thing that varies between models is how far along the common trajectory they have traveled.

By Epoch III (2024.04-2024.09),the loadings begin to shift.HumanEval's loading on PC1 rises to +0.54 above the knowledge benchmarks.The advent of code-specialized fine-tuning and function-calling capabilities begins to decouple procedural execution from broad knowledge.By the time the 6-benchmark battery is examined, HumanEval's loading on G has dropped to +0.20, while the knowledge-heavy benchmarks cluster at +0.44 to +0.47.

### The Great Rotation

The most consequential result is not a splintering of the eigenvalue spectrum (which is statistically underpowered) but the rotation of the first eigenvector.When DeepSeek V3 enters the expanding window, the angular displacement of G's eigenvector reaches 6.4, which is an order of magnitude larger than any previous step.What it might mean to be generally intelligent, as operationalized by the benchmark battery, is different after the arrival of tool-augmented and reasoning-chain models than it was before.

This rotation is the factor-analytic signature of a change in representational basis.In the scaling era, G pointed uniformly across all benchmarks and the general component was to be a bigger transformer trained on more data.In the tools era, G rotates toward knowledge-intensive benchmarks and away from procedural execution because the tools themselves (code interpreters, web search, reasoning scaffolds) handle procedural tasks.This frees the model's own capacity for the problem of generalization across knowledge domains.The reasoning profile of intelligence has changed, and it has recapitulated a very human tendency, to diminish the self through outsourcing.

### AI Foxes and Hedgehogs

The partial correlations, obtained by subtracting each epoch's own PC1, expose what lies beneath the general component.Four of the six benchmark pairs maintain the same sign across Epochs II and III, and the two that flip are near-zero in at least one epoch.The stable negative correlations (MMLU×HumanEval, GSM8K×MATH, MMLU×GSM8K, MMLU×MATH) reveal a pattern: once G is removed, increasing capability on one dimension comes at the expense of another.Knowledge trades off against code amd grade-school arithmetic trades off against competition mathematics.The general component masks the underlying specializations that the partial correlations reveal.

This finding has direct implications for the AGI debate.In the scaling era, the appearance of generality was maintained because all capabilities rose together on a single component.In the tools era, the partial correlations show increasing anti-correlation whereby models that excel at reasoning-chain benchmarks (MATH, GPQA) do so partly at the expense of rote procedural execution (GSM8K, HumanEval).Later models conceal what Isiah Bering in 1951 might have described as skulk of foxes that know many things within a hedgehog that knows one big thing (Berlin, 2013).Unlike Jensen's idea of an underlying 'distillate' of intelligence, the models reveal something more akin to Minsky's Society of Mind (Minsky, 1986).

### Inversion of the Ptolemaic Succession

There is a useful inverted analogy in the evolution of LLMs to the history of astronomy.Ptolemy's geocentric model could accommodate each new planetary observation by adding another epicycleanother circular motion layered on top of the existing ones.Each addition improved the fit, but the dimensionality of the model grew without bound, and the framework never arrived at a simple underlying law.The current benchmarking regime has a similar structure.Each time a model demonstrates a new capability (tool use, code execution, web browsing, chain-of-thought reasoning), a new benchmark is introduced to measure it.The battery grows, and the component structure becomes more complicated.The positive manifold holds across an expanding set of tasks, with each requiring its own epicycle of evaluation.

The Keplerian move would be to find the right basis-a small set of latent dimensions that account for the observed covariance without requiring a new benchmark for each new capability.The Newtonian move would be to move beyond a parsimonious basis by discovering a unifying law of transformers that govern how those components evolve across epochs.This is what one might describe as the 'Ptolemaic Succession' familiar from the history of natural scientific revolutions.The inversion of the Ptolemaic Succession in the evolution of LLMS shows how epicycles are not necessarily deleterious given enough computational power.LLMS are able to add epicycle-like specializations (revealed by the partial correlations) and coordinate them through a dominant compressor (the leading positive manifold).If bottlenecks of the human mind are overcome, as they seem to be in certain domains of LLM application, there is little stopping intelligences becoming more diverse and significantly more complicated, albeit less attractive.

### Intelligence is Tool-Using Intelligence

A final observation concerns the coherence of the benchmarking enterprise itself.The benchmarks in the current battery were designed to test models without tool access as a means of obtaining something close to raw cognitive performance on knowledge retrieval, mathematical reasoning, and code generation.But the models of Epoch IV do not operate this way.They use tools including code interpreters and search engines.Evaluating a tool-augmented model on a no-tools benchmark is like measuring the intelligence of a literate human by forbidding them to write anything down.

If the benchmarks that define G in AI are to be compared against human reasoning, then human reasoning should also be evaluated with its characteristic tools.Most of what makes Homo sapiens cognitively distinctive-language, mathematics, writing, scientific reasoning, institutional knowledge-emerged after the Paleolithic, and therefore after the human brain ceased to evolve in any substantial way (Tattersall, 2012;Neubauer et al., 2018).The cognitive explosion of the last 50,000 years is not a story of neural hardware improvement but of tool accumulation: symbolic systems, notational technologies, social institutions, and information storage devices that progressively externalized cognitive functions (Clark, 1998;Hutchins, 2000).

The same is now true of LLMs.A model equipped with a code interpreter, a calculator, and a web browser is not the same cognitive system as the same model running in isolation.Its effective intelligence has been extended by its tools, just as human intelligence has been extended by writing, libraries, and the internet.And now these tools include LLMs themselves.In this regime, the concept of a pure general intelligence factor, whether g or G, ceases to be well-defined.Intelligence is not a property of the individuated substrate it is a property of the expanded individual-tool system.

The practical consequence is that benchmarks designed for the pre-tool era of LLMs will progressively lose their meaning as tools become standard.The score matrix spectrum documented in this paper is a snapshot of a transitional period and perhaps the last moment at which it made sense to evaluate models on isolated cognitive tasks.This argues for less emphasis to be placed on general intelligence, or AGI, which is rooted in psychometric simplifications, and for a concerted effort to reveal the full dimensionality of intelligence.Toward respecting the many different reasoning dimensions of humans, non-human life, and machines (Vallor, 2024).

4. With n = 4 models and K = 4 benchmarks, the Epoch IV correlation matrix has zero degrees of freedom and parallel analysis cannot be applied.The two-factor structure reported for Epoch IV (Section 4.2) remains a descriptive observation.
