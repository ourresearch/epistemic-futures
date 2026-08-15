---
title: "Long-range Event-level Prediction and Response Simulation for Urban Crime and Global Terrorism with Granger Networks"
person: james-evans
section: by
type: journal-article
year: 2019
date: 2019-11-04
venue: "arXiv (Cornell University)"
authors: "Li, Timmy, Huang, Yi, Evans, James, Chattopadhyay, Ishanu"
source_url: https://doi.org/10.48550/arxiv.1911.05647
openalex_id: https://openalex.org/W2983247460
retrieved: 2026-08-13
content: full-text
notes: "preprint version; full text extracted from the arXiv PDF"
---

# Long-range Event-level Prediction and Response Simulation for Urban Crime and Global Terrorism with Granger Networks

## Full text

1

Long-range Event-level Prediction and Response
Simulation for Urban Crime and Global Terrorism with
Granger Networks
Timmy Li1,2,4 , Yi Huang1,2 , James Evans3,5 and Ishanu Chattopadhyay,1,2F
1

arXiv:1911.05647v1 [stat.AP] 4 Nov 2019

Institute of Genomics and Systems Biology,
2
Department of Medicine,
3
Department of Sociology,
and 4 Department of Computer Science
University of Chicago, Chicago, IL, 60637, USA
5
Santa Fe Institute, Santa Fe NM 87501, USA
F

To whom correspondence should be addressed: e-mail: ishanu@uchicago.edu.
Abstract

Large-scale trends in urban crime and global terrorism are well-predicted by socio-economic
drivers 1–3 , but focused, event-level predictions have had limited success 4–8 . Standard machine
learning approaches are promising 9 , but lack interpretability, are generally interpolative, and ineffective for precise future interventions with costly and wasteful false positives. Such attempts
have neither adequately connected with social theory, nor analyzed disparities between urban
crime and differentially motivated acts of societal violence such as terrorism. Thus, robust eventlevel predictability is still suspect, and policy optimization via simulated interventions remains
unexplored. Here, we are introducing Granger Network inference as a new forecasting approach
for individual infractions with demonstrated performance far surpassing past results, yet transparent enough to validate and extend social theory. Considering the problem of predicting crime
in the City of Chicago, we achieve an average AUC of ≈ 90% for events predicted a week in
advance within spatial tiles approximately 1000 ft across. Instead of pre-supposing that crimes
unfold across contiguous spaces akin to diffusive systems 7,8 , we learn the local transport
rules from data. As our key insights, we uncover indications of suburban bias 10–16 — how
law-enforcement response is modulated by socio-economic contexts with disproportionately
negative impacts in the inner city — and how the dynamics of violent and property crimes
co-evolve and constrain each other — lending quantitative support to controversial pro-active
policing policies 17–20 . To demonstrate broad applicability to spatio-temporal phenomena, we
analyze terror attacks in the middle-east in the recent past, and achieve an AUC of ≈ 80%
for predictions made a week in advance, and within spatial tiles measuring approximately 120
miles across. We conclude that while crime operates near an equilibrium quickly dissipating
perturbations, terrorism does not. Indeed terrorism aims to destabilize social order, as shown by
its dynamics being susceptible to run-away increases in event rates under small perturbations.

I NTRODUCTION
Crime and criminality have been undeniable aspects of the human condition since inception, as evidenced by
recorded history going back millennia 21 . Over time, the rise of cities and the development of the urban social
space created unique opportunities for crime 22–25 , resulting in new challenges for prevention and policing. The
recent emergence of ubiquitous data driven modeling has sparked interest in predictive policing: the possibility of
predicting crime, before it happens. In this study, we conceptualize this problem as that of modeling and prediction
of a system of spatio-temporal point processes unfolding in the social context. We report a fundamentally new
approach to predict urban crime in space and time at the level of individual events, with predictive accuracy far
greater than what has ever being achieved in the past. Beyond predicting the when and the where of the next
infraction, our new tools allow us to probe for enforcement biases, and garner deep insight into the nature of the
dynamical processes that drive criminality in urban spaces. With an analysis framework applicable to general
spatio-temporal phenomena, we compare and contrast urban crime with terrorism, and find important similarities
and distinctions. Our results indicate that while the dynamics of crime appears to operate in or around a stable

2

equilibrium, terrorism is essentially an unstable system of interdependent events where small perturbations might
be catastrophic.
Successful efforts to identify and explain trends in urban crime go back at least half a century 1–3 . Classical
investigations into the mechanics of criminality gave way to the possibility of event-level prediction of criminal
infractions, in a manner that would make it possible to preemptively intervene, and ultimately engineer urban
spaces with lower crime rates. These efforts have reported multi-variate modeling of time-invariant spatial
distribution of hotspots 26–28 , and have also included time-varying attributes 4–6 to estimate both long and short
term dynamic risks. A particularly visible approach to predictive policing is based on the use of epidemictype aftershock sequences (ETAS) 7,8 originally developed to model seismic phenomena. More recently, the
application of standard deep learning architectures 9 have been reported. While these approaches underscored
the potential of predictive policing, many have limited out-of-sample performance 7,8 . Machine learning strategies 9
have arguably performed better, but performance results generated with the common off-the-shelf tools ranging
from random forests to neural nets have at least one important caveat: the common approach of deleting a
random sample of events — training a machine learning system on the remaining data — and finally validating
on the deleted sample — is interpolative. Claims that good prediction on such interpolative validation schemes
automatically translate to good event predictions in the actual out-of-sample future time periods is, at best,
strongly suspect. Additionally, most machine learning systems are black boxes with little or no insight into the
sociology of the underlying phenomena — we learn nothing about the system, its rules of organization or have
insight into how and where we can possibly intervene to modulate the course of its evolution.
Here, we show that urban crime may be predicted precisely, reliably, and early enough that direct local intervention — as well as high level policy optimization from accurately predicted field impact — becomes a
practical strategy. We learn for a certain number of years (3) from recorded event logs, and then validate on
events in the following year beyond those in the training sample. Using incidence data from the City of Chicago,
our new spatio-temporal network inference algorithm, seeks out past patterns of event occurrences, and uses
these inferred patterns or rules to construct a communicating network (the Granger Net) of local estimators, to
ultimately predict future infractions.
We make predictions 1) separately for violent and property crimes, 2) individually within spatial tiles roughly
1000ft across, 3) approximately a week in advance, and 4) with AUCs ranging approximately between 80 − 99%
across the city. Our approach outperforms past efforts significantly, on account of realizing a predictive framework
with little pre-defined structure on one hand, and vastly improving the sample complexity required for inference
on the other (See Discussion for comparison with competing approaches).
While not assuming predefined constraints, we also do not employ off-the-shelf neural networks (NN) or other
standard learning architectures. Indeed, unlike NNs which use fixed non-linear activation functions to model
influence propagation, we learn the local transport rules from data. These local rules are learned as finite state
probabilistic transducer models, which significantly outperform NNs in numerical experiments in learning compact
models of stochastic processes (See Supplementary text for explicit examples).
The dependencies we infer are not constrained to be local. In contrast to what we expect in diffusive systems,
social rules of interactions are not required to mimic laws of physics; there is no guarantee that influence
diffuses in any orderly fashion, or that events far off across the city will have a weaker influence compared
to those physically near in space or time. Thus, a computational approach that discovers the emergent social
topology on which the dynamics of interest unfolds — as opposed to assuming either some rigid model structure
or a diffusive framework — is key to our achieved performance.
With our precise predictive apparatus in place, we run a series of computational experiments that perturb the
rates of violent and property crimes, and log the resulting alterations in future event rates across the city. By
inspecting the effect of SES variables on the perturbation response, we can then investigate if enforcement and
policy biases modulate outcomes. Our analysis suggests that the enforcement response to worsening crime
rates is strongly modulated by the status of socio-economic variables, and disadvantaged neighborhoods might
suffer from resources being pulled away to wealthier counterparts.
Additionally, our analysis reveals direct evidence as to how violent and property crimes co-evolve and influence
one another, indicating that increase in one typically down-regulates the other. These dependencies potentially
indicate that somewhat controversial pro-active enforcements, e.g. the broken window policy 17 , might be justified
in an operational sense. While this does not negate objections from the viewpoint of social theory 29 , or minimize
the issues of incorrect, overzealous, and improperly incentivized police practices 30 , our analysis suggests that
— if properly implemented — addressing property and non-violent infractions might indeed have a significant
suppressive effect on violent crime.
Further, we shed light on the continuing debate on the correct choice of neighborhood boundaries in urban crime

3

modeling 31–34 . We demonstrate that influence often is communicated over large distances, and decay slowly,
and perhaps more importantly, the “correct” choice of spatial scale is less of an issue in sophisticated learning
algorithms, where the optimal scales can be inferred automatically.
Finally we ask how the dynamics of urban crime compares to event patterns in other acts of societal violence,
specifically terrorism. Using data from the Global Terrorism Database (GTD), and focusing on the relatively
recent 5 year time-frame in the Middle-east, we carry out predictive analysis similar to the urban crime case.
We find that predictability is lower (average AUC ≈ 80%), but not by much, for the case of terrorism; the drop
in performance is most likely is due to the lower frequency of recorded events. We find that event influences
propagate rapidly and widely — similar to the crime scenario. However, the nature of the dynamics, as revealed
by our perturbation analyses, is markedly different between these two categories of aberrant social behavior —
crime operates near or around a dynamic equilibrium, where perturbations generally tend to dissipate quickly,
whereas terrorism appears to operate far from equilibrium, and small perturbations can be destabilizing and
rapidly increase event rates.
To the best of our knowledge, analysis of the perturbation response of data-driven models to probe underlying
social constructs has not been reported before. Even with the current limitations, this new addition to the
toolbox of computational sociology allows for direct validation of complex theory from observed event incidence,
supplementing the use of subjective measurable proxies, and potential biases in questionnaire-based data
collection strategies. While such classical approaches have unquestionably broadened our understanding of
the societal forces shaping the urban landscape, and inspired social theory to investigate the nature, correlates,
and causal drivers of criminality 35–38 , they do not attempt to forecast individual events. In this study, we show
that the ability to predict such events opens new doors to not only precise intervention possibilities, but to a
whole new set of computational tools.

M ETHOD & M ATERIALS
Data Source
Event incidence data for this study is obtained from the City of Chicago Data Portal 39 . The log includes spatiotemporal event localization along with the nature, category, and a brief description of the recorded incident.
Additional information on the number of arrests made during each event is also included. The log is updated
daily, keeping current with a lag of 7 days. We only use data between 2014-2017 (3 years for model inference,
and last 1 year for out-of-sample validation) for the prediction results shown in Figure 1. The evolving nature
of the urban scenescape 40 necessitates that we restrict the modeling window to a few years at a time. The
length of this window is decided by trading off the loss of performance from shorter data streams to that from
the evolution of the underlying generative processes for wider windows (See Supplementary text). In this study,
we consider two broad categories of criminal infractions: violent crimes consisting of homicides, assault, and
battery, and property crimes consisting of burglary, theft and motor vehicle thefts. The number of individuals
arrested during each recorded event is considered as a separate variable to be modeled and predicted, which
allows us to investigate the possibility of enforcement biases in subsequent perturbation analyses.
Additionally, we use data on socio-economic variables available at the portal corresponding to the Chicago
community areas and census tracts, including the % of population living in crowded housing, those residing
below poverty line, those unemployed at various age groups, per capita income, and the urban hardship index 41 .
To contrast urban crime against a motivationally different phenomenon of societal violence, we analyzed data
from 2012 to 2016 from the open-source Global Terrorism Database (GTD), with the last year used as the
out-of-sample validation set. To ensure similarity to the urban crime scenario, we chose to consider events in
two categories: 1) anti-infrastructure events including bombing, explosions, and facility and infrastructure attacks,
and 2) anti-personnel events including armed assault, hostage-taking, barricade incident, hijacking, assassination
and kidnapping. We also consider the number of casualties as a third variable to be modeled, analogous to the
number of arrests in the crime scenario.

Event Log Processing: Spatial and Temporal Discretization & Event Quantization
The event log is processed to obtain time-series of events of interest, stratified by occurrence locations. This
is accomplished by choosing a spatial discretization, and focusing on an individual spatial tile at a time, which
allows us to represent the event log as a collection of sequential event streams (See Fig. 1, plate C). Additionally,
we discretize time, and consider the sum total of events recorded within each time window.
Coarseness of these discretizations reflects a trade-off between computational complexity, and event localization
in space and time. The spatial and the temporal discretizations are not independently chosen; a finer spatial

4

A. Violent Crimes including

B. Property Crimes including

Assaults, Battery & Homicides
(April 1-15, 2017)

C. Spatio-temporal Modeling Approach Using

Thefts & Burglaries
(April 1-15, 2017)

Daily Event Counts & Spatial Tiles ≈ 1000 ft across

00

ft

r

≈

10

s

0
0.85, 0.15

∆=

q2

24

0.89, 0.11

0

q3

Infer
Linear
Combination

1

0

1

q1

s

0.84, 0.16

H, ω

2
∆=
30

s’

H0 , ω0

s0

11

0

∆=3
Influence from
violent crimes

∆=

r

∆ = 26

s”

q0

1

Negative influence
shown dotted
∆=

Step 2.

0.58, 0.42
0,1

01.05 2017
01.05 2017

s
(i) Probabilistic Transducer Hr,∆=30

s

21.04 2017
21.04 2017

(Note: Influence Exists over Multiple Time-scales from the Same Source)

11.04 2017
11.04 2017

D. Example of Remote Sources Influencing Property Crimes at a Target Location

2
1

Property Crimes

r
01.04 2017
01.04 2017

No. of Events

Violent Crimes
2
1

Step 1.
Infer
Local
Activation

r

H00 , ω00
s00

rt+∆ =

X
s∈S
j50

s
target prediction
∆ steps
from current time

Probabilistic transducer
from source s to target r
with delay ∆ + j



s
s
−∞
ωr,∆+
H
s
j r,∆+ j t− j
source data
upto j steps
before current time

Fig. 1. Crime Data & Modeling Approach. Plates A and B show the recorded infractions within the 2 week period between
April 1 and 15 in 2017. Place C illustrates our modeling approach: We break up the city into small spatial tiles that are
about 1.5 times the size of an average city block, and compute models that capture multi-scale dependencies between
the sequential event streams recorded at distinct tiles. In this paper, we treat violent and property crimes separately, and
show that these categories have intriguing cross-dependencies. Plate D illustrates our modeling approach. For example,
to predict the property crimes at some spatial tile r, we proceed as follows: step 1) we infer the probabilistic transducers
that estimate the event sequence at r by using as input the sequences of recorded infractions (of different categories) at
potentially all remote locations (s, s 0 , s 00 shown), where this predictive influence might transpire over different time delays (a
few shown on the edges between s and r). Step 2) Combine these weak estimators linearly to minimize zero-one loss. The
inferred transducers can be thought of as inferred local activation rules, which are then linearly composed, which reverses the
approach of linearly combining input and then passing through fixed activation functions in standard neural net architectures.
The connected network of nodes (variables), with probabilistic transducers on the edges comprises the Granger Net.

5

A. Spatial Distribution of AUC

C. Distribution of out-of-sample

B. Spatial Distribution of AUC

for Property crimes

AUC Across Spatial Tiles

for Violent Crimes

10

1.0
0.9
0.8
0.7
0.6
0.5

1.0
0.9
0.8
0.7
0.6
0.5

Average

5
0.897

0
0.8

0.85

0.9

1

Property
Crime

8
6
4
2
0

0.87

0.8

8
6
4
2
0

D. Snapshots of Out of Sample Predicted Risk Computed ≈ 1 week In Advance

0.95

0.9

1

Violent
Crime
0.87

0.8

AUC

0.9

1

Plates A an B illustrates the out-of-sample area under the receiver
operating characteristics curve (AUC) for predicting violent and property crimes respectively. The prediction is made a week
in advance, and the event is registered as a successful prediction if we get a hit within ±1 day of the predicted date. Plate
C illustrates the distribution of AUC on average, and individually for violent and property crimes. Our mean AUC is close
to 90%. Plate D illustrates the risk computed 7 days in advance for 3 consecutive days in 2017 February (out-of-sample).
The red dots are actual events (violent or property crimes), and the computed risk is shown as an overlay. Event predictions
at individual spatial tiles is used to construct the continuous risk intensity map by summing Gaussian densities centered at
each predicted event location. The variance of the Gaussian densities is tuned (in the course of training) to maximize recall.
The risk shown is normalized within each day.
Fig. 2. Predictive Performance of Granger Nets.

discretization dictates a coarser temporal quantization, and vice versa to prevent either long no-event stretches,
or long periods of contiguous event records, both of which are detrimental to obtaining reliable predictors. In

6

A.

C. Distribution of Increased Arrests D. Distribution of Increased Arrests

Spatial Distribution of
Hardship Index

from Increase In Violent Crimes

B.

0.20
0.15
0.10
0.05
0.00

∆+ =
17.9%

E. Distribution of Decreased Arrests F. Distribution of Decreased Arrests
from Increase In Violent Crimes

from Increase In Property Crimes

(I) Perturbation: violent crime rate
0.2

1.00
0.75
0.50
0.25
0.00

0.600

0
−0.2
(II) Perturbation: property crime rate
0.1

0.600
0.300

regression coeffcient (95% confidence)

0

∆+ =
15.3%
Spatial Change of Arrest Rate
Against Socio-Economic Indicators

0

0.12

0.12
0.09
0.06
0.03
0.00

0.06

0
0.04
0.080

80
60
40
20

from Increase In property Crimes

0.600

0.600

0

1.00
0.75
0.50
0.25
0.00

−0.1
∆− =
-36.3%

0

0
0.3

Y
D
A
D
64
ME DEX
DE ERT OYE LOM ER
CO
IN
OW OV
PL DIP
OV A IN HIP
R
P
M
C
R
E
T
UT 8 O
DS
S.
PI
OW UN
O
R
U
A
L
1
H
+
C
HA
IT
R
HO
BE
16
R
W
%
%
DE
PE
ED
5+
UN
AG % 2
%
%

∆− =
-36.4%

Fig. 3. Estimating
Bias. Plate
A illustrates the distribution of hardship index. Plates C, D, E, and F show the biased response
socio-economic
indicators

to perturbations in the crime rates. With a 10% increase in each of violent and property crime rates, we have approximately
a 30% decrease in arrests when averaged over the city. However, the spatial distribution of locations which experience a
positive vs a negative change in the rate of arrests reveals a strong preference for favorable socio-economic indicators for
the former. Thus, if neighborhoods are doing better socio-economically, increasing crime seems to predict increased arrests
as expected. A strong converse trend is observed in our predictions for neighborhoods doing worse, suggesting that under
stress, the wealthier neighborhoods drain resources from their disadvantaged counterparts. Plate B illustrates this more
directly via a multi-variable regression, where the hardship index is seen to have a strong negative contribution.

this study, we fixed the temporal quantization to 1 day, and chose a spatial quantization such that we have high
empirical entropy rates on average for the set of time series obtained (See Supplementary text for details). This
resulted in spatial tiles measuring 0.00276°×0.0035° in latitude and longitude respectively, which is approximately
1000 0 across, roughly corresponding to the area of under 4 city blocks. Note any two points within our spatial
tile are at most in neighboring blocks. We dropped from our analysis the tiles that have too low a crime rate
(< 5% of days within the modeling window had any event recorded) to reduce computational complexity, ending
up with a total of N = 2205 spatial tiles.
Thus, we end up with three different integer-valued time series at each spatial tile: 1) violent crime (v), 2) property
crime (u) and 3) number of arrests (w). We ignore the magnitude of the observations, and treat them as Boolean
variables; thus our models simply predict the presence or absence of a particular event type within a particular
spatial tile (within couple of blocks), and within a particular observation window (1 day).

7

Fig. 4. Influence Diffusion & Perturbation Space. If we are able to infer a model that is usefully predicts the event dynamics

at a specific spatial tile (the target) using observations at a source tile ∆ days in future, then we say that the source tile
is within the influencing neighborhood for the target location with a delay of ∆. Plate A illustrates the distribution of spatial
radius of influence for 0.5, 1, 2 and 3 weeks of time, for violent (upper panel) and property crimes (lower panel). We note
that the influence neighborhoods, as defined by us, are large, and tend to approach a radius of 6 miles eventually. Given
the geometry of the City of Chicago, this maps to a substantial percentage of the total area of the urban space under
consideration, showing that crime here has demonstrable long-range and almost city-wide influence on average. Plate B
illustrates the extent of a few of the inferred neighborhoods at a time delay of at most 3 days, which as noted, are not limited
to local city blocks. Plate C illustrates the average rate of influence diffusion measured, as before, by the number of predictive
models inferred that transduce influence as we consider longer and longer time delays. We note that the rate of influence
diffusion falls rapidly; for property crimes, the rate goes to zero in about a week, whereas for violent crimes, the influence
keeps diffusing even after three weeks. Plate D illustrates the multi-dimensional perturbation space constructed from probing
the inferred Granger Net with 1 − 10% perturbations in violent and property crime rates. We see that violent and property
crimes are anti-thetical: increase in one leads to suppression in the other. Most importantly, the effect of suppressing violent
crimes by increasing property crimes (moving right on the x-axis in plate D(i)), suggests important policy implications. Plate
E summarizes the key dependency patterns: notably violent crimes are more strongly self-limiting. The fact that we have all
suppressive relationships suggests a hidden variable that keeps the dynamics alive. Compare the dependency pattern in
terror events, where we could infer no such suppressive relation.

Inferring Stochastic Generators of Spatio-temporal Cross-dependence
Let L = {`1 , · · · , `N } be the set of spatial tiles, and E = {u, v, w} be the set of event categories as described
in the last section. At location ` ∈ L for variable e ∈ E, at time t, we have (`, e)t ∈ {0, 1}, with 1 indicating the
presence of at least one event. The set of all such combined variables (space + event type) is denoted as S,
i.e., S = L × E. Let T = {0, · · · , M − 1} denote the training period consisting of M time steps. Since for any time
t, (`, e)t is a random variable, our goal here is to learn its dependency relationships with its own past, and with

8

Fig. 5. Terror Event Prediction & Perturbation Space. Plate A shows out of sample predictions for terror events in the

middle east and surrounding regions for two specific days in 2015 and 2016 respectively. The overall distribution of AUC for
anti-infrastructure events and anti-personnel events is shown in plate B. In Plate C, we illustrate the influence diffusion rates
for the two classes of terror events (Fig. 4, Plate C). We see that the diffusion rates decay rapidly as before, and the rate for
anti-infrastructure events reduces to zero in about 7 − −10 days, whereas the rate for anti-personnel events keeps diffusing
even after three weeks. Plate D illustrates the multi-dimensional perturbation space constructed, as before, by probing the
inferred Granger Net with 1 − 10% perturbations in the two classes of events. Unlike the dynamics of crime, terrorism does
nit seem to have any self-limiting behavior: injecting positive perturbations in either kind of event stream strongly increases
the future probability of both categories of events. Plate E summarizes the key dependency patterns: notably we find no
suppressive dependencies, implying a very distinct dynamical pattern compared to urban crime.

other variables in S, to accurately estimate its future distribution for t > T .
To infer the structure of the Granger Net, we learn a finite state probabilistic transducer 42,43 for each possible
source-target pair s, r ∈ S. Given a sequence of events at the source, these inferred transducers estimate the
distribution of events at the target r at some future point in time. Ability to estimate such a non-trivial distribution
indicates the presence of causal influence. Here we assume that causal influence from the source to the target

9

manifests as the source being able to predict events occurring at the target, better than the target can do by
itself; this interpretation follows from Granger’s 44 eponymous approach to statistical causality. Such influence is
not restricted to be instantaneous; the source events might impact the target with a time delay, i.e., a specific
model between the source and the target might predict events delayed by an a priori determined number of
steps ∆max = ∆ = 0 specific to the model. Here, we model the influence structure for each integer-valued delay
separately; thus for source s and target t, we can have ∆max + 1 transducers each modeling the influence for
a specific delay in [0, ∆max ). The maximum number of steps in time delay ∆max is chosen a priori, based on
the problem at hand.
While these influences or dependencies may be different for different delays, they also do not need to be
symmetric between the source-target pairs. The complete set, comprising at most |S|2 (∆max + 1) models,
represents a predictive framework for asymmetric multi scale spatio-temporal phenomena. Note that the number
of possible models increase quickly, e.g., for ∆max = 60, with 2205 spatial tiles, and three event categories, the
number of inferred models is bounded above by ≈ 2.6 billion.
In this study we learn transducers as crossed finite state probabilistic automata (XPFSA) models (See Supplementary text). Our approach consists of two key steps (See Fig. 1, plate D): First, we infer XPFSA models for
all source-target pairs and all delays upto ∆max , and then in the second step, we learn a linear combination of
these transducers to maximize predictive performance.
s
Step 1: Denoting the observed event sequence in the time interval (∞, t] at source s as s−∞
t , the XPFSA Hr,k
estimates the distribution of events for target r at time step t+k. This is accomplished by learning an equivalence
relation on the historical event sequences observed at the source s, such that equivalent histories induce an
identical (or a nearly identical) future event distribution at the target r, k steps in the future. Thus, for example,
the XPFSA shown in Fig. 1 plate D, has four states, indicating that there are 4 such equivalence classes of
observations that induce the distinct output probabilities shown from each state. Often this estimate is not very
precise due to the possibility of multi-scale and multi-source influence, e.g., when the target r is influenced by
multiple sources, and with different time delays.

Step 2: We employ a standard gradient boosting regressor for each target, to optimize the linear combination of
inferred transducers, and learn the scalar weights ωsr,k for source s, target r and delay k, such that the estimate:


X
rt+∆ =
ωsr,∆+j Hsr,∆+j s−∞
(1)
t−j
j50
s∈S

minimizes the expected loss. Note that the left hand side of Eq. 1 is a random variable, i.e, we are estimating a
stochastic process indexed by t + ∆, as a function of the observed sample path s−∞
t . Here, ∆ is a pre-specified
constant, which specifies how far into future we are making the prediction.
To compare with a standard neural net architecture, these probabilistic transducers may be viewed as local nonlinear activation functions. Thus, while with neural networks we repeatedly compute affine combination of inputs
and apply fixed non-linear activation to the combined input and finally optimize the affine combination weights
via backpropagation, here we first learn the local non-linear activations, and then optimize the linear or affine
combination of the weak estimators. Optimizing the weights is significantly simpler — and a local operation —
for us, and may be done with any standard regressor, even with a local NN. In contrast to recurrent neural nets
(rnn), the role of the hidden layer neurons is partially taken over in our case by the states of the XPFSA, which
are a priori undetermined both with regards to their multiplicity and their transition connectivity structure. Even
with the significantly simplified computation, our approach is provably PAC-efficient 45 , i.e., we can learn good
models with high probability with relatively small sampling complexity.
The non-trivial structure of the Granger Net emerges from not all models being useful; we do not ultimately
use all 2.6 billion models for crime prediction. We estimate the usefulness of a particular model by computing
it coefficient of causality 42 (γ, see Supplementary text), which estimates the relative reduction in entropy in the
predicted outcomes over the entropy of the time-averaged target distribution, i.e. the prediction we will get with
no model inference. Throwing away these poor models reveals the complex predictive wiring of the system at
hand, which in itself holds important clues to its dynamical characteristics.

Computational & Model Complexity
We assume the maximum time delay in the influence propagation to be 60 days, resulting in at most 2, 669, 251, 725
inferred models, of which 61, 650, 000 are useful with γ 5 0.01. Model inference consumed approximately 200K
core-hours on 28 core Intel Broadwell processors, carried out with incidence data over the period Jan 1, 2014
to December 31, 2016. Data from January 1 2017 to December 31, 2017 is used for out-of-sample validation.

10

Perturbation Analysis
Determination of stability characteristics is a central question in any system modeling. For the dynamics of
criminal infractions, the question of stability has important sociological implications: how close is the system to a
run-away behavior, where we experience increasingly large upticks in the event rates? Or is there some tangible
evidence in the data at hand that such instabilities are not likely in the foreseeable future?
To answer these questions, we investigated the response of the system to bounded perturbations. The perturbations are injected by modifying the observed event sequences as follows: to introduce a positive perturbation
to the crime rates, we randomly replaced 0s in the binary event streams with a sample from a Bernoulli(θ)
distribution, where θ is chosen to reflect the desired increase in the event rate (See Supplementary text). To
introduce a negative perturbation, i.e., a reduction in the crime rates, we replaced 1s in the discretized binary
data streams with a sample from a Bernoulli(1 − θ) distribution.
We experimented with positive and negative perturbations to both violent and property crime rates ranging
between 1 to 10% of the observed rates. Response to the perturbed crime rates was measured as the relative
change from the nominal baseline in the estimated time-average in the predicted event frequencies 1 week into
the future, corresponding to violent and property crimes, and the number of arrests.
Results from the perturbation experiments shed light both on the stability characteristics of crime in Chicago,
and further allowed us to look for the evidence of biased enforcement response under stress.

R ESULTS
Our key result is the development of an efficient framework for event-level prediction of urban crime. For each
spatial location, the inferred Granger Net maps event histories to a raw risk score as a function of time —
higher this value, higher the probability of an event of the target type occurring at that location, within the
specified time window. However, to make crisp predictions, we must choose a decision threshold for this raw
score. Conceptually identical to the notion of Type 1 and Type 2 errors in classical statistical analyses, the
choice of a threshold trades off false positives (Type 1 error) for false negatives (Type 2 error): choosing a
small threshold results in predicting a larger fraction of future events correctly, i.e. have a high true positive
rate (TPR), while simultaneously suffering from a higher false positive rate (FPR), and vice versa. The receiver
operating characteristic curve (ROC) is the plot of the FPR vs the TPR, as we vary this decision threshold. If
our predictor is good, we will consistently achieve high TPR with small FPR resulting in a high area under the
ROC curve denoted as the AUC; AUC measures intrinsic performance, independent of the threshold choice.
More importantly, the AUC is immune to class imbalance (the fact that crimes are by and large rare events). An
AUC of 50% indicates that the predictor does no better than random, and an AUC of 100% implies that we can
achieve perfect prediction of future events, with zero false positives.

Predictability Achieved In the City of Chicago
We can predict events approximately a week in advance at the spatial resolution of ≈ 2 city blocks with a
temporal resolution of ±1 day, with a false positive rate of less than 20%, with a median true positive rate of
78%. Our prediction results are summarized in Fig. 2, where plates A and B illustrate the geospatial scatter of
AUC obtained for different spatial tiles, property and violent crimes respectively. Plate C shows the distribution of
the AUC achieved where we predict a crime ignoring its category (top plate, mean AUC ≈ 90%), and where we
predict property and violent crimes separately (middle and bottom plates, with mean AUC 87% in both cases).
These predictions are made 1 week in advance, but we register a true hit if the predicted event transpires within
6 − 8 days of the day the prediction is made.
Plate D illustrates the predicted risk map for 3 consecutive days in 2017 February, overlaid with the locations
of actual criminal infractions, with both violent and property crimes considered. Event predictions at individual
spatial tiles is used to construct the continuous risk intensity map by summing Gaussian densities centered at
each predicted event location. The variance of the Gaussian densities is tuned (in the course of training) to
maximize recall (ratio of true positives to the sum of true positives and false negatives). The risk map shown
in Fig. 2 Plate D is normalized within each day. Such normalized maps can be directly used to optimize law
enforcement deployments under constrained resources, where the recommendation will be to prioritize the peaks
of the daily risk map.

Enforcement & Policy Bias: Resource Distribution Response Under Stress
The results from the perturbation experiments suggest that under stress, well-off neighborhoods tend to drain
resources disproportionately from disadvantaged locales. Our findings are summarized in Fig. 3. We find that

11

on small perturbations of the crime rate, the corresponding variation in law enforcement response, measured
by variation in the number or predicted arrests, is very different in economically well-off neighborhoods. These
neighborhoods see a roughly proportionate increase in arrest rate with increasing crime (as expected), whereas
the arrest rate in the rest of the city crashes by a factor of nearly 3. This suggests that increased “stress” in
the form of increased number of crimes causes the enforcement resources to be drained out of disadvantaged
neighborhoods to support their better socioeconomic counterparts.
A multi-variable regression analysis (Fig. 3 plate B) also supports this conclusion. It shows that the change in
arrest rate from perturbations that increase the violent and the property crime rates have a strongly negative
contribution from hardship index, which is contradictory to what is expected in the absence of bias. Poorer
neighborhoods have more crime, and thus, these socio-economic indicators should contribute positively, if at all,
to increase the arrest rate as response to increasing crime. The reverse association seen here is problematic,
and potentially indicative of biases at the level of policy driving resource allocation in the city.

Temporal Memory & Neighborhood Effects
There is significant work in the literature aiming to understand the role of neighborhood organization in shaping
urban interactions. We probed the topological structure emergent in the inferred dependencies to estimate the
shape, size and organization of the neighborhoods that predict events at each location. The results, illustrated
in Fig. 4 plates A and B, show that the situation is complex with the locally predictive neighborhoods varying
widely in geometry and size. Clearly, restricting our analysis to relatively small local communities within the city
is less than optimal, and even attempting to determine a priori the correct scale of such organization that best
predicts crime might not be even feasible.
We then asked if the effect of criminal infractions diffuse outward in space and time, and if the diffusion rate of
influence can be meaningfully estimated. While the diffusion rates appear to vary significantly from one location
to the next, when averaged across the city, we see a rapid decay with time delay in the diffusion rates as shown
in Fig. 4, plate C. Note however that the diffusion rate for property crimes decays much faster compared to that
from violent crimes. In particular, on average, the diffusion rate from property crimes decays to zero in about
10 days, while violent crimes stay relevant event after a couple of months.

Emergent Relationships Between Violent & property crimes
The system responses from our perturbation experiments is used to estimate the multi-dimensional perturbation
manifold, as illustrated in Fig. 4, plate D. Plate D (i) shows the contours of the estimated time-averaged change
in property crimes a week in future after the perturbations were introduced. Plate D(ii) illustrates the response for
violent crimes. We can gain important insights into the underlying dynamical rules and constraints by imagining
likely system trajectories in this manifold, e.g., by moving along the Y-axis in Plate D(i), i.e. by increasing violent
crimes, we suppress property crimes. And by moving along the X-axis in plate D(ii), i.e., by increasing property
crimes, we suppress violent crimes.
We observe that the two categories of criminal infractions interact asymmetrically. As summarized in Fig. 4,
plate E, we see that these two categories tend to counteract each other: increase in one leads to suppression
in the other. Violent crimes seem to have significantly stronger self-limiting effect compared to property crimes.
Most importantly, the effect of suppressing violent crimes by “increasing” property crimes (moving right on the
x-axis in plate D(i)), suggests important policy implications (See Discussion).

Modeling Terror Event Dynamics From GTD
For the analysis of terror events, we use a spatial tiles that measure 1◦ × 2◦ is latitudinal and
√ longitudinal extent,
and limited to the middle east (See Fig. 5), this implies that our spatial tiles are roughly 692 + 1022 ≈ 123.1
miles along the diagonal. As with crime, we use a temporal quantization of 1 day, and measure performance with
prediction made a week in advance. We achieve AUCs close to 80% (78.8% for anti-infra-structure events, and
77.9% for anti-personnel events). The slightly reduced performance maybe attributed to the significantly lower
rates of terror attacks compared to crime in Chicago, which in the later case allows us to model low probability
patterns better.
We also compute the diffusion rates for influence of terror events, and it appears that anti-personnel events in this
case is the one that decays slowly (See Fig. 5, plate C, and compare with violent crimes in Fig. 4, plate C). The
influence of anti-infrastructure events dies down after about 10 days, which is also the time that property crime
influence take to approximately vanish, suggesting intriguing similarities between the two dynamical systems. In
contrast, the perturbation analysis for terrorism brings forward important distinctions from urban crime.

12

D ISCUSSION
Despite both violent and property crime in US falling sharply over the past quarter century 46 , major cities continue
to have unacceptably high rates of violent and property crimes (See Fig. 1, plates A and B). The distinctive
patterns of urban crime have led sociologists to advance theories ranging from the connection between urbanity
and immoral behavior, to the mechanics of opportunity arising from denser population, more contact with the
wealthy leading to higher expected pecuniary returns, and the demonstrably better chances of getting away
with crime in cities 22–25 . To theorize on the underlying causal factors shaping the urban scene, scholars have
suggested mechanisms which breakdown informal social control 47–50 , and collective efficacy 36 to encourage
and shape criminal behavior. In this study, we take a computational approach: we design a learning architecture
to reliably predict individual crimes sufficiently before they happen, such that direct intervention becomes a
possibility.
The contribution of this study is two fold: 1) our approach significantly outperforms past attempts to actionably
predict crime, 2) we can use our inferred predictive structure to probe for fundamental insights into the underlying
processes that drive urban crime. The centerpiece of our approach is the Granger Net, which models complex
spatio-temporal dependencies inferred without presupposing any particular model structure. Consequently, we
have a median TPR of 78% with FPR not more than 20%; in contrast to one of the prominent past efforts tuning
pre-supposed ETAS-based models 8 achieve a 5 10% true positive rate with no corresponding figure on false
positives. While the lack of prior assumptions allow us to discover novel structure, we also outperform standard
deep learning approaches 9 , both in head-to-head performance comparison (mean AUC ≈ 90% vs 85%), and
the fact that we can produce AUCs for individual locations, have much lower sample complexity, and require
only past incidence data. The ability to predict future events based purely on past event streams allows us to
probe the underlying social constructs via injecting perturbations in the rates of the different event categories.
This is either not feasible, or at least not transparently so, if a more diverse set of features are used as inputs;
it is hard to see for example how one perturbs street imagery in a principled manner, which has been used in
the literature 9 to identify problematic neighborhoods from the presence of wall graffiti. Ability to distill accurate
predictions using inputs that are easily and interpretably perturbed in silico provides us with a new investigative
tool in computational sociology.
Our perturbation analyses reveal that the stress response of the city potentially has indications of socio-economic
bias; wealthier neighborhoods respond appropriately when crime rates are elevated, whereas in disadvantaged
neighborhoods predicted arrest rates decrease rapidly. Importantly, we are not simply comparing magnitudes
here: the neighborhoods in which direction of movement for the change in arrest rate is incorrect tends to be
the wealthier ones, away from the inner city. A possible explanation is resource constraints on law enforcement,
which combined with biased prioritization to wealthier neighborhoods, leads to reduced enforcement efforts in
the rest of the city. This is not entirely surprising, and reinforces aspects of the notion of suburban bias in US
cities 11 .
The suburban bias hypothesis grew out of the idea of urban bias 10 put forward in the late 1970s, which posited
that urban interests wield political power to bias resource allocation. While imagined to be applicable at the much
larger scale of countries and nations, the existence of a similar effect in US urban society, where the political
power and influence concentrates in the suburbia instead, has long been suspected and written about 12–16 . Our
analysis now provides direct validation to that effect, which shows up robustly for all years of analysis going
back over one and half decades in Chicago (for which we have data).
Additionally, the structure of the inferred perturbation space suggest how violent and property crime rates interact
and co-evolve. The fact that we seem to be able to suppress violent crime by increasing the property crime rate
has deep policy implications: it suggests that proactive policing that penalizes property crimes more aggressively
— and thus “increases” the rate of property crime by causing to augment the number of such records in the
event log — might indeed have a suppressive effect on more serious crime. This directly echoes some aspects of
Wilson and Kelling’s broken windows policy 51 model that highlighted the importance of perceived social disorder
in setting up conditions conducive for more serious crime.
However, the efficacy of the broken windows model, with regards to both its theoretical validity and its implementation, has been strongly questioned, including by the original authors 17 . One of the most prominent
adoptions of the broken windows approach to crime and disorder occurred in New York City. While crime rates
were significantly reduced post-adoption, there is little consensus on the impact of the specific policies that
were introduced, with the qualitative estimates ranging from large 18 to small but significant 19 , to inconclusive 52 ,
to nil 20 . Recently, quantitative assessment with 30 randomized experimental and quasi-experimental tests of
disorder policing concluded that such strategies are associated with an overall statistically significant, modest
crime reduction effect 53 . We view our results to be further quantitative evidence for this basic notion underlying
the broken-windows model. While we do not claim to resolve or justify the issues stemming from over-zealous or

13

mis-interpreted and possibly mis-applied zero tolerance policing in lieu of Kelling’s original ideas, it does indicate
that the different categories of crime have limiting cross-dependencies.
This study also sheds light on the question of choosing the right spatial unit or scale of analysis in urban social
modeling and in studies relating to the ecology of crime 54,55 . Our results indicate that different spatial locations
have different range of local influence; indeed what is meant by the “local neighborhood” is context-dependent.
The importance of multiple spatial scales in urban crime has been long suspected 32,56 , and has been explored
to be as narrow as face blocks 57 to city communities to census tracts to tract groups 58 . Our results indicate that
instead of deciding these spatial scales a priori, a better alternative is that the appropriate neighborhoods of
predictive influence be inferred from data, as shown in Fig. 4, plates A and B. These results suggest that spatial
influence on crime might have a scale-free organization, where no particular unit of organization emerges as
particularly important. This interplay of scales, emerging from diverse mechanisms of social interaction is well
known 31,33,34,59 ; this study underscores the importance of these multi-scale processes to determine the optimal
influence neighborhoods that vary across the city. Also, the influence of crime seems to behave as a diffusive
process only on average, hence is not very useful for prediction of individual events at specific locations (See
Fig. 4, plate C), and simply assuming diffusive transport mechanisms are therefore incorrect.
Finally, the Granger net approach is shown to be successfully predicting future terror attacks via modeling the
GTD. With regards to the AUC we achieve in this case (approximately 80%), it is important to remember that
our validation is extrapolative. As pointed out earlier, predicting event/no-event on a randomly selected sample
of points within two fixed points of time is generally easier. This interpolative exercise need not model the
data as an evolving time series, and generally achieves inflated performance values. Evaluating the predictive
performance on events occurring at future time-periods requires the models to actually learn the evolution, and
the structure of the historical dependencies. To the best of our knowledge, attempts at such extrapolative eventlevel prediction of terrorism has not been reported, with the only recent reports solving interpolative exercises
with standard machine learning tools 60 , often without a temporal component 61 , or evaluating performance with
one-sided metrics such as precision 62 .

C ONCLUSION
This study demonstrates that given enough observations, complex social interactions are surprisingly predictable.
This opens the door to new approaches to policing, interventions, and policy design methodologies that has the
potential to radically improve societal well-being. At the same time, there is the distinct danger of misuse via overzealous enforcement, and careful consideration and transparency needs to be in place for such technologies to
be used to make decisions in public life.

ACKNOWLEDGMENTS
Our work greatly benefited from discussion of everyone who participated in our workshop series on crime
prediction at the Neubauer Collegium for culture and society 63 , and with those with whom we had extended
conversations to ground and refine our modeling approach.
Data was provided by the City of Chicago Data Portal at https://data.cityofchicago.org. The City of Chicago
(City) voluntarily provides the data on this website as a service to the public. The City makes no warranty,
representation, or guaranty as to the content, accuracy, timeliness, or completeness of any of the data provided
at this website (https://www.chicago.gov/city/en/narr/foia/data disclaimer.html), and the authors of this study are
solely responsible for the opinions and conclusions expressed in this study.
Data on terror attacks was downloaded from the GTD (https://www.start.umd.edu/data-tools/global-terrorismdatabase-gtd), which is a database of incidents of terrorism from 1970 -2016. The database is maintained by
the National Consortium for the Study of Terrorism and Responses to Terrorism (START) at the University of
Maryland, College Park in the United States, and receives funding from a variety of organizations including the
US Department of Defense, and the National Science Foundation.
This work is funded in part by the Defense Advanced Research Projects Agency (DARPA) project #FP07094301-PR and the Neubauer Collegium for Culture and Society through the Faculty Initiated Research Program
2017. The claims made in this study do not necessarily reflect the position or the policy of the sponsors, and
no official endorsement should be inferred.

14

R EFERENCES
[1] Ferdinand, T. N. Demographic shifts and criminality: An inquiry. The British Journal of Criminology 10,
169–175 (1970).
[2] Cohen, L. & Felson, M. Social change and crime rate trends: A routine activity approach. American
Sociological Review 44, 588–608 (1979). Cited By 4102.
[3] Cohen, L. E. Modeling crime trends: a criminal opportunity perspective. Journal of Research in Crime and
Delinquency 18, 138–164 (1981).
[4] Bowers, K. J., Johnson, S. D. & Pease, K. Prospective hot-spotting: The future of crime mapping? The
British Journal of Criminology 44, 641–658 (2004).
[5] Chainey, S., Tompson, L. & Uhlig, S. The utility of hotspot mapping for predicting spatial patterns of crime.
Security Journal 21, 4–28 (2008). URL https://doi.org/10.1057/palgrave.sj.8350066.
[6] Fielding, M. & Jones, V. disrupting the optimal forager: Predictive risk mapping and domestic burglary
reduction in trafford, greater manchester. International Journal of Police Science & Management 14, 30–41
(2012).
[7] Mohler, G. O., Short, M. B., Brantingham, P. J., Schoenberg, F. P. & Tita, G. E. Self-exciting point process
modeling of crime. Journal of the American Statistical Association 106, 100–108 (2011).
[8] Mohler, G. O. et al. Randomized controlled field trials of predictive policing. Journal of the American
Statistical Association 110, 1399–1411 (2015).
[9] Kang, H. W. & Kang, H. B. Prediction of crime occurrence from multi-modal data using deep learning.
PLoS ONE 12, e0176244 (2017).
[10] Lipton, M. et al. Why poor people stay poor: a study of urban bias in world development (London: Canberra,
ACT: Temple Smith; Australian National University Press, 1977).
[11] Meyer, W. B. & Graybill, J. K. The suburban bias of american society? Urban Geography 37, 863–882
(2016).
[12] Jackson, K. T. Crabgrass frontier: The suburbanization of the United States (Oxford University Press, 1987).
[13] Duany, A., Plater-Zyberk, E. & Speck, J. Suburban nation: The rise of sprawl and the decline of the American
dream (Macmillan, 2001).
[14] Logan, J. R. The suburban advantage: New census data show unyielding city-suburb economic gap, and
surprising shifts in some places. Lewis Mumford Center for Comparative Urban and Regional Research,
University at Albany (2002).
[15] Lazare, D. America’s Undeclared War: What’s Killing Our Cities and how to Stop it (Harcourt, 2001). URL
https://books.google.com/books?id=miSzAAAAIAAJ.
[16] Young, I. M. Inclusion and democracy (Oxford University press on demand, 2002).
[17] Kelling, G. L. & Coles, C. M. Fixing broken windows : restoring order and reducing crime in our communities
(New York : Martin Kessler Books, 1996). Includes bibliographical references (p. 291-301) and index.
[18] Bratton, W. & Knobler, P. The Turnaround: How America’s Top Cop Reversed the Crime Epidemic (Random
House Publishing Group, 2009). URL https://books.google.com/books?id=Ns7GAZcA9AYC.
[19] MESSNER, S. F. et al. Policing, drugs, and the homicide decline in new york city in the 1990s*. Criminology
45, 385–414 (2007). URL https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1745-9125.2007.00082.x. https:
//onlinelibrary.wiley.com/doi/pdf/10.1111/j.1745-9125.2007.00082.x.
[20] Harcourt, B. E. & Ludwig, J. Broken windows: New evidence from new york city and a five-city social
experiment. The University of Chicago Law Review 73, 271–320 (2006). URL http://www.jstor.org/stable/
4495553.
[21] Hammurabi & Harper, R. F. The code of Hammurabi King of Babylon, about 2250 B.C. (University of
Chicago Press, 1904).
[22] FLANGO, V. E. & SHERBENOU, E. L. Poverty, urbanization, and crime. Criminology 14, 331–346 (1976).
URL https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1745-9125.1976.tb00027.x. https://onlinelibrary.wiley.
com/doi/pdf/10.1111/j.1745-9125.1976.tb00027.x.
[23] Glaeser, E. L. & Sacerdote, B. Why is there more crime in cities? Working Paper 5430, National Bureau
of Economic Research (1996). URL http://www.nber.org/papers/w5430.
[24] SHICHOR, D., DECKER, D. L. & O’BRIEN, R. M. Population density and criminal victimizationsome
unexpected findings in central cities. Criminology 17, 184–193 (1979). URL https://onlinelibrary.wiley.com/
doi/abs/10.1111/j.1745-9125.1979.tb01285.x. https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1745-9125.
1979.tb01285.x.
[25] Wirth, L. Urbanism as a way of life. American Journal of Sociology 44, 1–24 (1938). URL https://doi.org/
10.1086/217913. https://doi.org/10.1086/217913.
[26] Wang, X. & Brown, D. E. The spatio-temporal modeling for criminal incidents. Security Informatics 1, 2
(2012). URL https://doi.org/10.1186/2190-8532-1-2.
[27] Liu, H. & Brown, D. E. Criminal incident prediction using a point-pattern-based density model. International Journal of Forecasting 19, 603 – 622 (2003). URL http://www.sciencedirect.com/science/article/pii/

15

S0169207003000943.
[28] Caplan, J. M., Kennedy, L. W., Barnum, J. D. & Piza, E. L. Crime in context: Utilizing risk terrain modeling
and conjunctive analysis of case configurations to explore the dynamics of criminogenic behavior settings.
Journal of Contemporary Criminal Justice 33, 133–151 (2017).
[29] Sridhar, C. R. Broken windows and zero tolerance: Policing urban crimes. Economic and Political Weekly
41, 1841–1843 (2006). URL http://www.jstor.org/stable/4418196.
[30] CHILDRESS, S. The problem with ’broken windows’ policing (2016). URL https://www.pbs.org/wgbh/
frontline/article/the-problem-with-broken-windows-policing/.
[31] SHERMAN, L. W., GARTIN, P. R. & BUERGER, M. E. Hot spots of predatory crime: Routine activities
and the criminology of place*. Criminology 27, 27–56 (1989). URL https://onlinelibrary.wiley.com/doi/
abs/10.1111/j.1745-9125.1989.tb00862.x. https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1745-9125.1989.
tb00862.x.
[32] WOOLDREDGE, J. Examining the (ir)relevance of aggregation bias for multilevel studies of neighborhoods
and crime with an example comparing census tracts to official neighborhoods in cincinnati*. Criminology
40, 681–710 (2002).
[33] MEARS, D. P. & BHATI, A. S. No community is an island: The effects of resource deprivation on urban
violence in spatially and socially proximate communities*. Criminology 44, 509–548 (2006). URL https:
//onlinelibrary.wiley.com/doi/abs/10.1111/j.1745-9125.2006.00056.x. https://onlinelibrary.wiley.com/doi/pdf/
10.1111/j.1745-9125.2006.00056.x.
[34] Weisburd, D., Groff, E. R., Yang, S.-M. & Telep, C. W. Criminology of Place, 848–857 (Springer New York,
New York, NY, 2014). URL https://doi.org/10.1007/978-1-4614-5690-2 663.
[35] Sutherland, E. H. Juvenile delinquency and urban areas: A study of rates of delinquents in relation to
differential characteristics of local communities in american cities. clifford r. shaw , henry d. mckay , norman
s. hayner , paul g. cressey , clarence w. schroeder , t. earl sullenger , earl r. moses , calvin f. schmid.
American Journal of Sociology 49, 100–101 (1943). URL https://doi.org/10.1086/219339. https://doi.org/
10.1086/219339.
[36] Sampson, R. J., Raudenbush, S. W. & Earls, F. Neighborhoods and violent crime: A multilevel study of
collective efficacy. Science 277, 918–924 (1997).
[37] Miethe, T. D., Hughes, M. & McDowall, D. Social Change and Crime Rates: An Evaluation of Alternative
Theoretical Approaches*. Social Forces 70, 165–185 (1991). URL https://doi.org/10.1093/sf/70.1.165.
http://oup.prod.sis.lan/sf/article-pdf/70/1/165/6887328/70-1-165.pdf.
[38] Braga, A. A. & Clarke, R. V. Explaining high-risk concentrations of crime in the city: Social disorganization,
crime opportunities, and important next steps 51, 480–498 (2014).
[39] City of chicago: Data portal: City of chicago: Data portal (2019). URL https://data.cityofchicago.org/.
[40] Silver, D. & Clark, T. Scenescapes: How Qualities of Place Shape Social Life (University of Chicago Press,
2016). URL https://books.google.com/books?id=gjQljgEACAAJ.
[41] Nathan, R. P. & Adams, C. F. Four perspectives on urban hardship. Political Science Quarterly 104,
483–508 (1989). URL http://www.jstor.org/stable/2151275.
[42] Chattopadhyay, I. Causality networks. arxiv CoRR (2014). URL http://arxiv.org/abs/1406.6651.
[43] Mohri, M. Weighted Finite-State Transducer Algorithms. An Overview, 551–563 (Springer Berlin Heidelberg,
Berlin, Heidelberg, 2004). URL https://doi.org/10.1007/978-3-540-39886-8 29.
[44] Granger, C. W. J. Testing For Causality. Journal of Economic Dynamics and Control 2, 329–352 (1980).
[45] Valiant, L. G. A theory of the learnable. Commun. ACM 27, 1134–1142 (1984).
[46] GRAMLICH, J. 5 facts about crime in the u.s. (2019). URL https://www.pewresearch.org/fact-tank/2019/
01/03/5-facts-about-crime-in-the-u-s/.
[47] Shaw, C. & McKay, H. Juvenile Delinquency and Urban Areas (1942). Cited By 3715.
[48] Veysey, B. & Messner, S. Further testing of social disorganization theory: An elaboration of sampson and
groves’s ’community structure and crime’. Journal of Research in Crime and Delinquency 36, 156–174
(1999). Cited By 133.
[49] Sampson, R. & Groves, W. Community structure and crime: Testing social-disorganization theory. American
Journal of Sociology 94, 774–802 (1989). Cited By 2273.
[50] Kubrin, C. & Weitzer, R. New directions in social disorganization theory. Journal of Research in Crime and
Delinquency 40, 374–402 (2003). Cited By 352.
[51] KELLING,
G.
L.
&
WILSON,
J.
Q.
Broken
windows,
the
atlantic.
https://www.theatlantic.com/magazine/archive/1982/03/broken-windows/304465/ (1982).
[52] Rosenfeld, R. & Fornango, R. The impact of police stops on precinct robbery and burglary rates in new
york city, 2003-2010. Justice Quarterly 31, 96–122 (2014).
[53] Braga, A. A., Welsh, B. C. & Schnell, C. Can policing disorder reduce crime? a systematic review and
meta-analysis. Journal of Research in Crime and Delinquency 52, 567–588 (2015).
[54] Boessen, A. & Hipp, J. Close-ups and the scale of ecology: Land uses and the geography of social context
and crime. Criminology 53, 399–426 (2015). Cited By 51.

16

[55] Hipp, J. Block, tract, and levels of aggregation: Neighborhood structure and crime and disorder as a case
in point. American Sociological Review 72, 659–680 (2007). Cited By 213.
[56] Rosenfeld, R. & Bursik, R. J. American Journal of Sociology 99, 1387–1389 (1994). URL http://www.jstor.
org/stable/2781176.
[57] Hunter, A. & Suttles, G. The Expanding Community of Limited-Liability (University of Chicago Press, 1972).
[58] Miethe, T. & Meier, R. Crime and its Social Context: Toward an Integrated Theory of Offenders, Victims,
and Situations. SUNY series in deviance and social control (State University of New York Press, 1994).
URL https://books.google.com/books?id= 4wTiaBRclIC.
[59] Quick, M. Multiscale spatiotemporal patterns of crime: a bayesian cross-classified multilevel modelling
approach. Journal of Geographical Systems 21, 339–365 (2019). Cited By 0.
[60] Hao, M., Jiang, D., Ding, F., Fu, J. & Chen, S. Simulating spatio-temporal patterns of terrorism incidents
on the indochina peninsula with gis and the random forest method. ISPRS International Journal of GeoInformation 8, 133 (2019).
[61] Ding, F., Ge, Q., Jiang, D., Fu, J. & Hao, M. Understanding the dynamics of terrorism events with multiplediscipline datasets and machine learning approach. PLoS ONE 12, e0179057 (2017).
[62] Mo, H., Meng, X., Li, J. & Zhao, S. Terrorist event prediction based on revealing data. In 2017 IEEE 2nd
International Conference on Big Data Analysis (ICBDA)(, 239–244 (2017).
[63] University of Chicago. Crimes of prediction workshop, the neubauer collegium for culture and society.
https://neubauercollegium.uchicago.edu/events/uc/crimes of prediction workshop/ (2019).
