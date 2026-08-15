---
title: "Complementary artificial intelligence designed to augment human discovery"
person: james-evans
section: by
type: journal-article
year: 2022
date: 2022-07-02
venue: "arXiv (Cornell University)"
authors: "Sourati, Jamshid, Evans, James"
source_url: https://doi.org/10.48550/arxiv.2207.00902
openalex_id: https://openalex.org/W4283834222
retrieved: 2026-08-13
content: full-text
notes: "preprint version; full text extracted from the arXiv PDF"
---

# Complementary artificial intelligence designed to augment human discovery

## Full text

Complementary artificial intelligence designed to augment human discovery

Jamshid Souratia
James Evansa,b*
a

University of Chicago
1155 S. 60th Street
Chicago, IL 60637
b

Santa Fe Institute
1399 Hyde Park Road
Santa Fe, NM 87501

Neither artificial intelligence designed to play Turing’s imitation game, nor augmented intelligence built to
maximize the human manipulation of information are tuned to accelerate innovation and improve humanity’s
collective advance against its greatest challenges. We reconceptualize and pilot beneficial AI to radically augment
human understanding by complementing rather than competing with human cognitive capacity. Our approach to
complementary intelligence builds on insights underlying the wisdom of crowds, which hinges on the
independence and diversity of crowd members’ information and approach. By programmatically incorporating
information on the evolving distribution of scientific expertise from research papers, our approach follows the
distribution of content in the literature while avoiding the scientific crowd and the hypotheses cognitively
available to it. We use this approach to generate valuable predictions for what materials possess valuable
energy-related properties (e.g., thermoelectricity), and what compounds possess valuable medical properties (e.g.,
asthma) that complement the human scientific crowd. We demonstrate that our complementary predictions, if
identified by human scientists and inventors at all, are only discovered years further into the future. When we
evaluate the promise of our predictions with first-principles or data-driven simulations of those properties, we
demonstrate an “expectation gap” such that increased complementarity of our predictions do not decrease and in
some cases increase the probability of these properties above those discovered and published by human scientists.
In summary, by tuning AI to avoid the crowd, we can generate hypotheses unlikely to be imagined or pursued
without intervention until the distant future that promise to punctuate scientific advance. By identifying and
correcting for collective human bias, these models also suggest opportunities to improve human prediction by
reformulating science education for discovery.

*

Correspondence to jevans@uchicago.edu
1

Two competing visions for computational intelligence have dominated designs over the past half-century, but
neither are tuned to accelerate humanity’s advance against its greatest challenges, such as advancing science and
technology for human benefit. Artificial Intelligence, coined by McCarthy in 1955, fixes humans as the standard
of intelligence, following Turing’s “imitation game”1. This influential approach became more tightly tethered to
human intelligence with Samuel’s work to build “machine learning” algorithms in the late 1950s2 that not only
produce human-like outcomes, but train on human moves. The Turing test vision of AI contrasted with a
contemporary program to directly “Augment” Intelligence by reducing frictions in the conveyance and
manipulation of information by Ashby 3, Englebart4, Licklider5 and others. If humanoid robots embody artificial
intelligence; human-computer interfaces (e.g., screens, mice, EEG helmets, brain implants) realize augmented
intelligence, but both visions feel inert to assist with science and technology design challenges, as in biomedicine
and material science, on which millions of human scientists and engineers have collaborated and competed for
centuries. Moreover, with millions of active scientists and engineers around the world and stagnating growth in
labor productivity, halving to 1.3% for all but one OECD country since the 1990s6, is the production of
computational intelligence that mimics human capacity our most strategic or ethical investment? Here we
reconceptualize and pilot beneficial AI that radically complements human understanding by thinking differently,
complementing human cognitive capacity rather than competing with or directly extending it.
Our approach to complementary intelligence builds on insights underlying the wisdom of crowds7, which hinges
on the independence and diversity of crowd members’ information 8 and approach9. In machine learning contexts
like the Netflix Prize and Kaggle, ensemble models have always won10. In scientific crowds, findings established
by more distinct methods and researchers are much more likely to replicate11,12. If we model discovery as
establishing novel links among otherwise disconnected concepts13, discovery cannot occur until discoverers arise
with viewpoints that bridge the fields required to imagine those conceptual connections (Fig. 1a). This diversity of
scientific viewpoints was implicitly drawn upon by pioneering information scientist Swanson in a heuristic
approach to knowledge generation. For example, he hypothesized that if Raynaud’s disorder was linked to blood
viscosity in one literature, and fish oil was known to decrease that viscosity in another, then fish oil might lessen
the symptoms of Raynaud’s disorder, but would unlikely be arrived at within the field because no scientist was
available to infer it14–16, one of several hypotheses later experimentally demonstrated17–19. Expansive opportunities
for discovery persist as researchers crowd around past discoveries20, refusing to explore regions of knowledge
cognitively distant from recent findings21 (Extended Data Fig. 1). Our approach in this article scales and makes
Swanson’s heuristic continuous, combining it with explicit measurement of the scientific expertise distribution
that draw upon advances in unsupervised manifold learning22. Recent efforts to generate scientific hypotheses rely
heavily on scientific literature, but ignore equally available publication meta-data. By programmatically
incorporating information on the evolving distribution of scientific expertise, our approach targets the exploration
of areas far from past discoveries, avoiding the scientific crowd. As such, the suggestions that result complement
collective intelligence and enable us to punctuate advance by identifying promising experiments unlikely to be
pursued by scientists in the near future without intervention.
In order to avoid the scientific crowd, our approach must first identify those topics at the focus of collective
attention in the scientific system. Metadata about the distribution of research experts across topics and time
represents a critical social fact that can stably improve our inference about whether scientific relationships will
receive scientific attention or remain unimagined and unexplored13,23. We build expert awareness into our
approach to identify and validate the scientific and technological benefit of pursuing complementary research
avenues unlikely to be considered by unassisted human experts. The proposed framework provides opportunities
for intellectual arbitrage between isolated communities through complementary intelligences unconstrained by the
human incentive to flock together within fields.
2

Avoiding Cognitive Availability
We model the cognitive availability of a hypothesis to human scientists by measuring the distribution of experts
exposed to its underlying concepts, linked by previous discoveries that intermediate them and which could guide
human intuition from one to the other (Fig. 1a). The distribution of relevant experts in science can be estimated
from a sufficient corpus of research articles, where papers inscribe the mixed network of publishing scientists and
concepts they investigate. We represent these complex connectivities with a hypergraph, where published articles
are hyperedges connecting authors and mentioned concepts. Hypergraphs are effective at representing complex
social interaction24–26 and proximity between concepts across them quantifies their cognitive availability to
scientist teams, which effectively forecasts human discovery and publication27. Scientific entities further apart in
the hypergraph will be less likely conceived together, or seen as relevant by scientists, dramatically reducing their
chance for consideration and discovery. We can measure node proximities with any graph distance metric that
varies with expert density, such as unsupervised neural embeddings, Markov transition probabilities, or
self-avoiding walks from Schramm-Loewner evolutions. Here we use shortest-path distances (SPD) between
conceptual nodes, as interlinked by authors in our mixed hypergraph. In the remainder of our paper, we divide
concepts into materials such as chemical compounds and the valuable scientific properties that may be attributed
them, like conductivity, treatment potential, regulation of a disease-related gene, etc. The hypotheses we explore
involve material and biomedical relationships between materials and their properties.
In order to avoid selecting hypotheses without scientific promise, cognitive availability must couple with a signal
of hypothesis plausibility. Such a signal could be provided by the published research literature and quantified with
unsupervised knowledge embedding models28. Alternatively, a signal of plausibility could be derived from
theory-driven models of material properties. Here we use unsupervised knowledge embeddings for our algorithm,
reserving theory-driven model simulations to evaluate the value and human complementarity of our predictions.
Specifically, we measure the scientific merit of any given hypothesis using the cosine similarity between
embedding vectors of material and property nodes that comprise each hypothesis. Figure 1b provides a general
overview of our algorithm for inferring materials with a target property. Initialized once a pool of candidate
materials has been extracted from literature, we perform parallel operations to generate hypotheses that are both
scientifically plausible and human-complementary. We train an unsupervised word embedding model over prior
publications and measure scientific relevance as cosine distance in the embedding. In parallel, we indicate
cognitive availability by structuring the hypergraph such that each author and material or property node from a
paper is encased within a hyperedge and shortest path distances between the property and all materials are
computed across the graph. We transform signals of plausibility and cognitive availability into a unified scale and
linearly combine them with a mixing coefficient 𝛽 (see details in Methods and Supplementary Information). With
its expert awareness, our algorithm can symmetrically generate either the most or least-human hypotheses—those
likely to compete versus complement collective human capacity—based on the sign of the mixing coefficient.
Negative 𝛽 values lead to predictions that mimic human experts in discovery, while positive values produce
hypotheses least similar to those human experts could infer, straddling socially but not scientifically disconnected
fields. At extremes, 𝛽=-1 and 1 yield algorithms that generate predictions very familiar or very alien to human
experts, regardless of scientific merit. Setting 𝛽=0 implies exclusive emphasis on scientific plausibility, blind to
the distribution of experts. This mode is equivalent to traditional discovery prediction methods exclusively based
on previously published content. Intermediate positive 𝛽s balance exploitation of relevant materials with
exploration of areas unlikely considered or connected by human experts. Materials with the highest resulting
scores are reported as the algorithm’s predictions.
In the following sections, we evaluate the complementarity of our inferences for human science by verifying (1)
their distinctness from contemporary investigations and (2) their scientific promise. We anticipate that both
features will simultaneously increase in ranges of 𝛽 higher than those that characterize published science.
Scientific merit will naturally reduce at the extremes of our interval [-1,1], however, where the algorithm ignores
an inferred hypothesis’ literature-based plausibility.
Evaluating Discovered Predictions
3

As we increase 𝛽, the algorithm avoids inferences that lie within regions of high expert density and focuses on
candidate materials and properties that span disciplinary divides and evade human attention. As a result, we
expect that generated hypotheses with large 𝛽 will diverge from those pursued by the scientific community, will
less likely become published, and if published, will be discovered further into the future, after science has
reorganized itself to consider them. In order to verify these hypotheses, we first assess the discoverability of
hypotheses inferred from different 𝛽 values by computing the precision between our inferences and published
discoveries. Results strongly confirm our expectation that materials inferred at higher 𝛽 values are less
discoverable by human scientists (Extended Data Fig. 2). Materials distant from a given property in the
hypergraph remain cognitively unavailable to scientists in the property’s proximity (Fig. 1c). It takes longer for
researchers in the field to broach knowledge gaps separating unfamiliar materials from valued properties. Among
the inferences eventually discovered, we measure the discovery waiting time and expect to observe an increasing
trend in wait times as we move from negative (human-competitive) to positive (human-complementary) 𝛽 values
in our predictions. Generating 50 hypotheses per 𝛽 value and evaluating the resulting predictions indicates that for
the majority of targeted properties the average discovery wait times climb markedly when increasing 𝛽 (Fig. 2) for
energy-related chemical properties (Fig. 2a-2c), COVID-19 (Fig. 2d) and 70% of the other human diseases (Fig.
2e). Averaging wait times across all human diseases manifests a clear increasing trend. For some cases such as
COVID-19 (Fig. 2d), none of the complementary predictions made with positive 𝛽 values come to be discovered
by humans within the time frame we examine.
Evaluating Undiscovered Predictions
To evaluate the scientific merit of our algorithm’s undiscovered hypotheses requires data beyond the extant
literature. Such hypotheses necessarily grow to comprise the vast majority of cases for large values of 𝛽. If science
was an efficient market and experts optimally pursued scientific quality, then in human-avoiding high 𝛽
hypotheses, we would observe a proportional decline in their scientific promise and efficacy. On the other hand, if
scientists crowd together along the frontier of scientific possibility and their continued efforts yield diminishing
marginal returns, we might observe an increase in promise as we move beyond them.
To evaluate the merit of scientific inferences, we utilize first-principles or data-driven models derived uniquely for
each property based on well-established theoretical principles within the field. Such models assign real-valued
scores to candidate materials as a measure of their potential for possessing the targeted properties. These
computations may be carried out without regard for whether materials have yet been discovered, making them a
suitable, if conservative, scoring function for evaluating undiscovered hypotheses. We produced such scores for
approximately 45% of the properties we considered above using first-principle equations or based on databases
curated through high-throughput protein screens. To evaluate thermoelectric promise, we used power factor (PF)
as an important component of the overall thermoelectric figure of merit, zT, calculated using density functional
theory for candidate materials as a strong indication of thermoelectricity29,30. To evaluate ferroelectricity, estimates
of spontaneous polarization obtained through symmetry analysis and relevant theoretical equations serve as a
reliable metric for this property31. For human diseases including COVID-19, proximity between disease agents
(e.g., SARS-CoV-2) and candidate compounds in protein-protein interaction networks suggests the likelihood a
material will recognize and engage with the disease agent32 (for more details on how these theoretical scores are
derived see the Supplementary Information). We note that scores based on first-principles equations or
simulations represent conservative estimates of scientific merit as they are based on widely-accepted,
scientist-crafted and theory-inspired models. Because these scores are potentially available to scientists in the
area, they may be considered when guiding investigation, such that experiments on these unevaluated hypotheses
are very often promising. Nevertheless, in what follows we show that intermediate positive 𝛽s manifest
continuation or improvement on even this conservative measure of quality.
We expect the average theoretical scores of hypotheses to decay significantly at the extremes of the 𝛽 range [-1,1],
as at those points the algorithm ignores the merit signal putting it at higher risk of generating scientifically
irrelevant (or absurd) proposals. We expect, however, that this decay will occur more slowly than the decrease in
hypothesis discovery and publication, which implies a 𝛽 interval where proposals are not discoverable but highly
4

promising—an ideal operating region for the generation of hypotheses that complement those from the human
scientific crowd. In order to verify this, we contrasted changes in average theoretical scores with the
discoverability of generated hypotheses for various 𝛽 values, which we quantify with precision—the overlap
between predictions and published discoveries. As illustrated in Fig. 3 (first row), discoverability decreases near
the transition of 𝛽 from negative to positive values, but its decay is much sharper than average theoretical scores,
which do not collapse until nearly 𝛽=0.4. This holds for electrochemical properties and the majority of diseases.
Results for certain individual diseases can be seen in the second row of Fig. 3 (for the full set of results see
Extended Data Fig. 3 and Supplementary Information). Moreover, note that for the cases investigated, average
theoretical scores for inferred hypotheses grow higher than average scores for actual, published discoveries before
eventual decay at high 𝛽 values. For certain properties like thermoelectricity or therapeutic efficacy against the
disease Alopecia, theoretical merit of our inferences exhibit striking and dramatic growth from negative
(scientist-mimicking) to positive (scientist-avoiding) hypotheses, suggesting strong diminishing returns to
following these scientific crowds, whose overharvested fields have become barren for new discoveries.
In order to compare the decay rate of discoverability and theoretical scores, we define and compute the
expectation gap to measure the distance between expected values for two conditional distributions over 𝛽. A
randomly selected prediction is (1) identified as promising based on its corresponding first-principle score, and (2)
discoverable, i.e., studied and published by a scientist following prediction year (for details see Methods and
Supplementary Information). A positive expectation gap indicates that increasing 𝛽 will preserve the quality of
predictions while making them more complementary to human hypotheses. As shown in Fig. 4a, the vast majority
of properties considered in this section yield substantial and significantly positive expectation gaps. Building on
this, we use a probabilistic model to assess the complementarity of our algorithm’s prediction with those of the
scientific community for any value of 𝛽. This is done by computing the joint probability that a randomly selected
prediction is plausible in terms of the desired property and beyond current scientists’ scope of research (see
Supplementary Information). These probabilities specify the optimal 𝛽 to balance exploitation and exploration in
augmenting collective human prediction. Results in Fig. 4b indicates the optimal point varies for different
properties, but one can distinguish the range 0.2-0.3 as the most consistently promising interval.
Discussion
Here we explore the potential for building AI algorithms to radically augment the scientific community. Building
on insights about independence underlying the wisdom of crowds, we seek to complement the clustering driven
by interactions and institutions of the scientific community. By tuning our algorithm to avoid the crowd, we
generate promising hypotheses unlikely to be imagined, pursued or published without machine recommendation
for years into the future. By identifying and correcting for collective patterns of human attention, formed by field
boundaries and institutionalized education, these models complement the contemporary scientific community. A
further class of complementary predictions could be tuned to compensate not only for emergent collective bias,
but universal cognitive constraints, such as limits on the human capacity to conceive or search through complex
combinations (e.g., high-order therapeutic cocktails33). Disorienting hypotheses from such a system will not be
beautiful, but being inconceivable, they break fresh ground and sidestep the path-dependent “burden of
knowledge” where scientific institutions require new advances built upon the old for ratification and support34,35.
Our approach can also be used to identify individual and collective biases that limit productive exploration and
suggest opportunities to improve human prediction by reformulating science education for discovery. Insofar as
research experiences and relationships condition the questions scientists investigate, education tuned to discovery
would conceive of each student as a new experiment, recombining knowledge and opportunity in novel ways. Our
investigation underscores the power of incorporating human and social factors to produce artificial intelligence
that complements rather than substitutes for human expertise. By making AI hypothesis generation aware of
human expertise, it can race with rather than against the scientific community to expand the scope of human
imagination and discovery.

5

Fig. 1. (a) Distribution and overlap of experts investigating (and publishing on) topics represented by yellow geometric shapes. Dashed
lines represent paths of more or less cognitive availability between topics (“triangle”, “diamond” and “square”). (b) Overview of our
complementary discovery prediction algorithm. Beginning with a scientific corpus and a targeted property, candidate materials are
extracted from the corpus and used along with property mentions and authors to form the hypergraph. The algorithm follows two branches
to compute plausibility from word embedding semantic similarities and “alienness” or human inaccessibility from hypergraph shortest-path
distances. These two signals are combined after proper normalization and standardization through the mixing coefficient 𝛽 to generate a
prediction more or less complementary to the flow of human discovery. Candidate materials are sorted based on resulting scores and those
with highest rank are reported as proposed discoveries. (c) Discovery wait times for relations between “triangle”–“diamond” and
“triangle”–“square”. The time one needs to wait for a relationship to be discovered is proportional to the path length of cognitive
availability between the two relevant topics. The denser presence of experts around the pair “triangle”–“diamond” implies greater cognitive
availability leading to earlier discovery and publication versus “triangle”–“square” where the connection requires a longer path.

6

Fig. 2. Wait time for published discoveries associated with distinct properties and different 𝛽 values. (a-d) Average annual/monthly
discovery wait times are shown as thick gray arcs, where thickness represents the percentage of materials discovered in the corresponding
year/month. Each orbit is associated with a particular 𝛽 value with larger (more red) orbits representing larger 𝛽 values. The values we
consider here vary between -0.8 (the smallest, bluest orbit) and 0.8 (the largest, reddest orbit). The plot in the upper right quarter of the
orbits reveals the total average of discovery wait times including all years/months for the considered 𝛽 values. (f) Total average for wait
times across all the human diseases (except COVID-19) in our experiments.

7

Fig. 3. Overlapping percentage and average theoretical scores calculated for predictions. (a-b) Green bars show overlapping percentages
and curves indicate (a) average PF for thermoelectricity and (b) spontaneous polarization for ferroelectricity. (c) Overlapping and average
theoretical scores (i.e., protein-protein interaction similarity scores) of the therapeutic predictions. Dashed lines in all cases show average
theoretical scores computed for actual discoveries following prediction year. (d) Overlapping versus average protein-protein similarity
scores for nine human disease examples. The y-axis indicates overlapping percentage and color gradient represents average theoretical
scores for predictions.

8

Fig. 4. (a) Expectation gap calculated for properties with theoretical first-principle scores. We plot the conditional distributions
ℙ(𝛽|plausible) and ℙ(𝛽|discoverable) separately for Thermoelectricity, Ferroelectricity and COVID-19, whereas for the remainder of human
diseases included in our experiments we simply show the normalized histogram (first row) and individual (second row) gaps. (b) The joint
probability of simultaneous undiscoverability and plausibility for different 𝛽 values.

9

Methods
Experiments and Data Collection
We used two distinct datasets in our experiments. For energy-related properties, i.e., thermoelectricity,
ferroelectricity and photovoltaic materials, we used a pre-curated dataset of approximately 1.5M articles whose
topics are relevant to inorganic materials. These articles have been selected and pre-processed by Tshitoyan et. al
(2019)28, who also made their DOIs publicly available. We downloaded abstracts of these DOIs through the
Scopus API provided by Elsevier (https://dev.elsevier.com/) and extracted 106K candidate inorganic materials
from the downloaded abstracts using Python Materials Genomics36 and direct rule-based string processing. For
COVID-19 and other human diseases, we used the MEDLINE database which includes more than 28M articles
published on a wide range of topics. In this dataset, we identified around 7,800 approved candidate drugs, from
which we selected approximately 4,000 drugs with simple names (excluding names with multiple numerical
subparts). We use Comparative Toxicogenomics Database (CTD) 37 to extract ground-truth associations between
our drug pool and 400 human diseases (besides COVID-19), selected such that they represent the largest number
of associations. Note that in order to form our hypergraph, we need to know who authored the articles. The
Scopus API distinguishes distinct authors and assigns unique codes to them. However, this is not the case with
MEDLINE, where authors are not identified other than by name. We use the set of disambiguated authors shared
through PubMed Knowledge Graph (PKG) package38, which were obtained by combining results from the
Author-ity disambiguation of PubMed39 and the more recent semantic scholar database40.
Our discovery prediction experiment begins by setting a date of prediction (e.g., the beginning of January 2001).
We then form our hypergraph using literature prior to that date and let our algorithm make predictions from
materials unstudied in relation to a given property at that point. Many of our evaluation criteria are based on
human discovery. For energy-related properties, we model human discovery as first-time co-occurrence of
materials with the targeted property, following methodology of the team that curated the dataset28. For all diseases
except COVID-19, human discoveries were identified through drug-disease associations indicated in CTD. We set
the date for each drug-disease discovery to the earliest publication reported by the CTD for curated associations.
For COVID-19, discovered drugs are identified based on their involvement in COVID-related studies reported by
ClinicalTrials.org that began after breakout of the disease in the US in the beginning of 2020. Discovery date for
each association is set to the date the corresponding study was first posted, and if the drug was involved in
multiple trials we considered the earliest. There were 6,280 trials posted as of August 5th, 2021 (ignoring 37 trials
dated before 2020), which included 279 drugs from our pool (~7%) within their designs.

Prediction Algorithm
Our predictor consists of two scoring functions. The first measures the cognitive unavailability (“alienness”) of
candidate materials via Shortest-Path distance (SPD) between the nodes corresponding to the targeted property
and candidates. The second measures scientific plausibility through the semantic cosine similarities of their
corresponding keywords. For this purpose, we train skipgram word2vec embedding models over the literature
(literature collected on inorganic materials for energy-related properties and MEDLINE for the diseases) produced
prior to the prediction year. The prediction year is set to the beginning of 2001 for all the considered properties
except for COVID-19 for which the prediction year is set to the beginning of 2020. We combine the alienness and
plausability scores with a mixing coefficient, denoted by 𝛽, adjusting their contributions to obtain a final score for
the candidate. The plausibility component yields continuous scores distributed close to Gaussian, whereas the
alienness component offers unbounded ordinal SPD values. Simple normalization methods are insufficient to
combine scores with such distinct characteristics. As a result, we first standardize the two scores to a unified scale
by applying the Van der Waerden transformation 41, followed by a Z-score normalization. The final step includes
10

taking the weighted average of the resulting Z-scores with weights depending on 𝛽 (see Supplementary
Information for more details).
We want our predictor to infer undiscoverable yet promising hypotheses. Setting 𝛽 to a more positive value makes
predictions less familiar and more alien, i.e., less discoverable. Moreover, increasing 𝛽 to the positive extreme
(i.e., +1) excludes scientific merit from the algorithm’s objective in materials selection. Hence, growing 𝛽 causes
both discoverability and plausibility of predictions to decay. What matters to us is that plausibility decreases more
slowly than discoverability, suggesting that the predictor achieves a close-to-ideal state where predictions are
simultaneously alien and promising. In order to verify this with a single number, we define the expectation gap
criterion, computed as the difference between expected values of the following two distributions over 𝛽:
ℙ(𝛽|plausible) and ℙ(𝛽|discoverable). The terms “plausible” and “discoverable” on the conditional sides could be
substituted by the precise statements “a randomly selected inferred hypothesis is theoretically plausible” and “a
randomly selected inferred hypothesis is discoverable”—it will be published by scientists, respectively. While we
know both of these distributions reduce as 𝛽 approaches +1, the expectation gap measures any positive shift in the
mass of ℙ(𝛽|plausible) against ℙ(𝛽|discoverable). The likelihood of discovery ℙ(𝛽|discoverable) can be estimated
through an empirical distribution of predictions discovered and published. Scientific plausibility can be estimated
by leveraging properties’ theoretical scores obtained from prior knowledge and first-principles equations and data
from relevant fields. We estimate ℙ(𝛽=𝛽0 | plausible) in two steps: (1) converting theoretical scores to
probabilities, and (2) computing weighted maximum likelihood estimates of ℙ(𝛽=𝛽0|plausible) given a set of
predictions generated by our algorithm operated with 𝛽0 (see Supplementary Information for details). We restrict
experiments in this section to only those properties for which we could obtain a reliable source of theoretical
scores (see Supplementary Information for details of the scores): thermoelectricity, ferroelectricity, COVID-19
and 175 other human diseases (178 out of 404 total properties). Finally, note that expectation gaps and average
discovery dates (described above) say nothing about the 𝛽 interval most likely to lead to complementarity and
plausibility. We introduce an additional probabilistic criterion for this purpose, which jointly models these two
features and computes their likelihood for various 𝛽 values, ℙ(undiscoverable, plausible | 𝛽). One can use this
distribution to screen the best operating point for complementary artificial intelligence (see Supplementary
Information).

11

References
1.

Turing, A. M. I.—COMPUTING MACHINERY AND INTELLIGENCE. Mind vol. LIX 433–460 (1950).

2.

Samuel, A. L. Some Studies in Machine Learning Using the Game of Checkers. IBM Journal of Research and Development vol. 3
210–229 (1959).

3.

Ashby, W. R. An introduction to cybernetics. (1956) doi:10.5962/bhl.title.5851.

4.

Engelbart, D. C. Augmenting human intellect: A conceptual framework. Menlo Park, CA (1962).

5.

Licklider, J. C. R. Man-Computer Symbiosis. IRE Transactions on Human Factors in Electronics HFE-1, 4–11 (1960).

6.

Brynjolfsson, E., Rock, D. & Syverson, C. Artificial Intelligence and the Modern Productivity Paradox: A Clash of Expectations and
Statistics. https://www.nber.org/papers/w24001 (2017) doi:10.3386/w24001.

7.

Galton, F. Vox populi (the wisdom of crowds). Nature 75, 450–451 (1907).

8.

Surowiecki, J. The wisdom of crowds: Why the many are smarter than the few and how collective wisdom shapes business.
Economies, Societies and Nations 296, (2004).

9.

Page, S. E. The Diversity Bonus: How Great Teams Pay Off in the Knowledge Economy. (Princeton University Press, 2019).

10. Freund, Y., Schapire, R. E. & Others. Experiments with a new boosting algorithm. in icml vol. 96 148–156 (Citeseer, 1996).
11. Danchev, V., Rzhetsky, A. & Evans, J. A. Centralized scientific communities are less likely to generate replicable results. Elife 8,
(2019).
12. Belikov, A. V., Rzhetsky, A. & Evans, J. Prediction of robust scientific facts from literature. Nature Machine Intelligence 1–10 (2022).
13. Rzhetsky, A., Foster, J. G., Foster, I. T. & Evans, J. A. Choosing experiments to accelerate collective discovery. Proc. Natl. Acad. Sci.
U. S. A. 112, 14569–14574 (2015).
14. Swanson, D. R. Fish oil, Raynaud’s syndrome, and undiscovered public knowledge. Perspect. Biol. Med. 30, 7–18 (1986).
15. Swanson, D. R. Medical literature as a potential source of new knowledge. Bull. Med. Libr. Assoc. 78, 29–37 (1990).
16. Weeber, M., Klein, H., de Jong-van den Berg, L. T. W. & Vos, R. Using concepts in literature-based discovery: Simulating Swanson’s
Raynaud--fish oil and migraine--magnesium discoveries. J. Am. Soc. Inf. Sci. Technol. 52, 548–557 (2001).
17. Evans, J. & Rzhetsky, A. Machine Science. Science 329, 399–400 (2010).
18. Digiacomo, R. A., Kremer, J. M. & Shah, D. M. Fish-oil dietary supplementation in patients with Raynaud’s phenomenon: A
double-blind, controlled, prospective study. The American Journal of Medicine vol. 86 158–164 (1989).
19. Chiu, H.-Y., Yeh, T.-H., Huang, Y.-C. & Chen, P.-Y. Effects of Intravenous and Oral Magnesium on Reducing Migraine: A
Meta-analysis of Randomized Controlled Trials. Pain Physician 19, E97–112 (2016).
20. Singer, U., Radinsky, K. & Horvitz, E. On Biases Of Attention In Scientific Discovery. Bioinformatics (2020)

12

doi:10.1093/bioinformatics/btaa1036.
21. Chu, J. S. G. & Evans, J. A. Slowed canonical progress in large fields of science. Proc. Natl. Acad. Sci. U. S. A. 118, (2021).
22. Mikolov, T., Yih, W. & Zweig, G. Linguistic regularities in continuous space word representations. hlt-Naacl (2013).
23. Sourati, J., Belikov, A. & Evans, J. Data on how science is made can make science better. (2022).
24. Shi, F., Foster, J. G. & Evans, J. A. Weaving the fabric of science: Dynamic network models of science’s unfolding structure. Soc.
Networks 43, 73–85 (2015).
25. Lung, R. I., Gaskó, N. & Suciu, M. A. A hypergraph model for representing scientific output. Scientometrics 117, 1361–1379 (2018).
26. Antelmi, A., Cordasco, G., Spagnuolo, C. & Szufel, P. Social Influence Maximization in Hypergraphs. Entropy 23, (2021).
27. Sourati, J. & Evans, J. Accelerating science with human versus alien artificial intelligences. arXiv [cs.AI] (2021).
28. Tshitoyan, V. et al. Unsupervised word embeddings capture latent knowledge from materials science literature. Nature 571, 95–98
(2019).
29. Mehdizadeh Dehkordi, A., Zebarjadi, M., He, J. & Tritt, T. M. Thermoelectric power factor: Enhancement mechanisms and strategies
for higher performance thermoelectric materials. Mater. Sci. Eng. R Rep. 97, 1–22 (2015).
30. Ricci, F. et al. An ab initio electronic transport database for inorganic materials. Sci Data 4, 170085 (2017).
31. Smidt, T. E., Mack, S. A., Reyes-Lillo, S. E., Jain, A. & Neaton, J. B. An automatically curated first-principles database of
ferroelectrics. Sci Data 7, 72 (2020).
32. Gysi, D. M. et al. Network Medicine Framework for Identifying Drug Repurposing Opportunities for COVID-19. ArXiv (2020).
33. Gediya, L. K. & Njar, V. C. Promise and challenges in drug discovery and development of hybrid anticancer drugs. Expert Opin. Drug
Discov. 4, 1099–1111 (2009).
34. Jones, B. F. The Burden of Knowledge and the ‘Death of the Renaissance Man’: Is Innovation Getting Harder? Rev. Econ. Stud. 76,
283–317 (2009).
35. Szell, M., Ma, Y. & Sinatra, R. A Nobel opportunity for interdisciplinarity. Nat. Phys. 14, 1075–1078 (2018).
36. Ong, S. P. et al. Python Materials Genomics (pymatgen): A robust, open-source python library for materials analysis. Comput. Mater.
Sci. 68, 314–319 (2013).
37. Davis, A. P. et al. The Comparative Toxicogenomics Database: update 2019. Nucleic Acids Res. 47, D948–D954 (2019).
38. Xu, J. et al. Building a PubMed knowledge graph. Sci Data 7, 205 (2020).
39. Torvik, V. I. & Smalheiser, N. R. Author Name Disambiguation in MEDLINE. ACM Trans. Knowl. Discov. Data 3, (2009).
40. Ammar, W. et al. Construction of the Literature Graph in Semantic Scholar. arXiv [cs.CL] (2018).
41. Coakley, C. W. Practical Nonparametric Statistics (3rd ed.). J. Am. Stat. Assoc. 95, 332 (2000).

13

Acknowledgements
The authors wish to thank our funders for their generous support: National Science Foundation #1829366; Air
Force Office of Scientific Research #FA9550-19-1-0354, #FA9550-15-1-0162; DARPA #HR00111820006. We
thank Laszlo Barabasi and Deisy Morselli Gysi for helpful data related to their network-based forecast of
COVID-19 drugs and vaccines with protein-protein interactions 32, and Anubhav Jain, Vahe Tshitoyan and Alex
Dunn for sharing data and code to help replicate their work on unsupervised word embeddings and latent
knowledge about material science28. We also thank participants of the Santa Fe Institute workshop “Foundations
of Intelligence in Natural and Artificial Systems”, the University of Wisconsin at Madison’s HAMLET workshop,
and colleagues at the Knowledge Lab for helpful comments.

14

Extended Data Fig. 1. Illustration of localized discoveries made by scientists regarding thermoelectric materials (a) and repurposing
materials for treating gout (b), asthma (c) and malaria (d). Red bars indicate fractions of discoveries occurring at various levels of
proximity (measured through shortest path distances (SPD) in a literature-based hypergraph) to a particular targeted property. Note how
these distributions concentrate around low proximites. Blue bars indicate average scores representing plausibility that candidate materials
have the targeted property in theory. For thermoelectricity (a), we defined Power Factor (PF) as the plausibility score, and for the three
human diseases shown here (b-d), scores are obtained through similarities between protein profiles of the candidate materials and the
targeted diseases.

15

Extended Data Fig. 2. Illustration of decaying discoverability for predictions as 𝛽 increases. Discoverability of predictions is measured
through computing the precision metric, i.e., their overlapping percentage with respect to actual discoveries made after prediction year.
Decreasing precision curves and their highly negative Pearson correlation coefficients are shown for (a) thermoelectricity, (b)
ferroelectricity, (c) photovoltaics and (d) COVID-19. We visualize these statistics for the remaining human diseases with a scatterplot of
their Pearson correlation coefficients (e).

16

Extended Data Fig. 3. Discoverability and scientific merit for predictions made with varying 𝛽 values in the research case repurposing
drugs for treating human diseases. (a) Precision values for predictions generated with eight levels of 𝛽 and computed for all 400 human
diseases we considered (except COVID-19). Diseases are sorted in terms of the number of relevant drugs. (b) Average theoretical scores
measured through protein-protein similarity between diseases and candidate drugs for predictions generated with the same 𝛽 values. We
compute such protein-based theoretical scores for 176 diseases out of 400 total cases (44%). In both subfigures, horizontal lines show
average values across all diseases.

17
