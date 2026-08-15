---
title: "Deep Learning Without Neural Networks: Fractal-nets for Rare Event Modeling"
person: james-evans
section: by
type: journal-article
year: 2020
date: 2020-10-26
venue: "Research Square"
authors: "Ishanu Chattopadhyay, Yi Huang, James Evans"
source_url: https://doi.org/10.21203/rs.3.rs-86045/v1
openalex_id: https://openalex.org/W3199966448
retrieved: 2026-08-13
content: full-text
notes: "preprint version; full text extracted from an open-access copy hosted at a repository or publisher OA location (OSTI, Zenodo, ACL Anthology, DSpace, OSF, IEEE, ResearchSquare or similar)"
---

# Deep Learning Without Neural Networks: Fractal-nets for Rare Event Modeling

## Full text

Deep Learning Without Neural Networks: Fractalnets for Rare Event Modeling
Ishanu Chattopadhyay (  ishanu@uchicago.edu )
University of Chicago https://orcid.org/0000-0001-8339-8162
Yi Huang
University of Chicago
James Evans
University of Chicago https://orcid.org/0000-0001-9838-0707

Social Sciences - Article
Keywords: neural networks, deep learning, fractal net architecture
Posted Date: October 26th, 2020
DOI: https://doi.org/10.21203/rs.3.rs-86045/v1
License:   This work is licensed under a Creative Commons Attribution 4.0 International License.
Read Full License

1

Deep Learning Without Neural Networks:
Fractal-nets for Rare Event Modeling
Yi Huang✶ , James Evans✶❀✷ and Ishanu Chattopadhyay✶❀⋆
✶
✷

University of Chicago, Chicago, IL 60637, USA
Santa Fe Institute, Santa Fe NM 87501, USA

⋆

To whom correspondence should be addressed: e-mail: ishanu@uchicago.edu

Complex phenomena of societal interest such as weather, seismic activity and urban crime, are often punctuated by rare
and extreme events 1 , which are difficult to model and predict. Evidence of long-range persistence 2,3 of such events has
underscored the need to learn deep stochastic structures in data for effective forecasts. Recently neural networks (NN)
have emerged as a defacto standard for deep learning 4–9 . However, key problems remain with NN inference, including a
high sample complexity, a general lack of transparency, and a limited ability to directly model stochastic phenomena. In this
study we suggest that deep learning and the NN paradigm are conceptually distinct – and that it is possible to learn “deep”
associations without invoking the ubiquitous NN strategy of global optimization via back-propagation 10 . We show that deep
learning of stochastic phenomena is related to uncovering the emergent self-similarities in data, which avoids the NN pitfalls
offering crucial insights into underlying mechanisms. Using the Fractal Net (FN) architecture introduced here, we actionably
forecast various categories of rare weather and seismic events, and property and violent crimes in major US cities. Compared
to carefully tuned NNs, we boost recall at
precision by
✿
for extreme weather events,
✿
for light-to-severe
seismic events with magnitudes above the local third quartile, and ✿
✿
for urban crime, demonstrating applicability
in diverse systems of societal interest. This study opens the door to precise prediction of rare events in spatio-temporal
phenomena, adding a new tool to the data science revolution.

✾✵✪

C

✶✻✶ ✾✪
✺✵ ✽✪ ✹✶✽ ✻✪

✶✾✶ ✸✪

OMPLEX systems exhibit rare and sudden transitions that impact dynamical fate 1 . Pre-empting these

events can help mitigate crises ranging from catastrophic environmental disasters, to social unrest, market
crashes, economic drawdowns on national scales, and global pandemics. However, modeling rare events is
challenging: analytical solution from first principle equations, even when known, are seldom tractable, and uncertainties from unresolved scales makes long-range models of the average dynamical behavior incompatible
with reliable prediction of low frequency events 11,12 . Here we develop a framework for tracking rare events in
the coupled evolution of discrete time stochastic processes. A rare event in our setting is defined to have an
13
occurrence frequency ❁
; extreme weather in US, seismic events around the globe, and violent urban
crime in major US cities – all fall in this category. Recent studies in geography 2,3 , hydrology 14,15 , climate 16,17 ,
and finance 18 suggest rare events might not be completely random, but show long-range persistence 19 . Thus,
uncovering deep predictive structures in data is crucial for reliable forecasts 1,20 .

✶✵✪

Neural Networks (NN) are now a defacto standard for deep learning 4–9,20 . The depth of the NN used to discover
prediction-relevant features suggested and sustained the deep metaphor. However, for complex systems in the
physical and social sciences, often the key missing piece is effective modeling of stochastic processes. And the
fantastic performance of NNs in learning input-output deterministic functions 21–23 carries over imperfectly and
with wasted expressive capacity to stochastic phenomena. In the context of low frequency seismic events and
extreme weather and crime, we care about precise event localization, underlining the importance of explicit
stochastic modeling.
To address this gap we prompt the reader to think of deep learning and the NN paradigm as conceptually
distinct — we show that it is possible to learn “deep” associations without invoking the ubiquitous NN strategy
of global optimization via backpropagation of the loss gradient 10 . Our key insight is tied to self-similar structures
arising in ergodic stochastic processes which take values over a finite alphabet. If such a process has a welldefined set of dynamical states, self-similarity arises naturally: once a trajectory visits a particular state, we

2

a. Philadelphia Crime, 22-03-2017

b. Atlanta Crime, 26-06-2017 and 27-06-2017

Property Crime [ ]
0.6
0.4
0.2
0.0 FN TP FP

1

violent crime risk
.8 .6 .4 .2

0

0

.2 .4 .6 .8
property crime risk

1

Property Crime [ ]
0.6
0.4
0.2
0.0 FN TP FP

Violent Crime [ ]

Violent Crime [ ]

0.8
0.6
0.4
0.2
0.0 FN TP FP

0.6
0.4
0.2
0.0 FN TP FP

1

violent crime risk
.8 .6 .4 .2

0

0

.2 .4 .6 .8
property crime risk

1

e. Chicago Crime, 27-03-2017

c. US Weather, 20-02-2019 12:00-24:00

Violent Crime [ ]
0.6
0.4
0.2
0.0 FN TP FP

Property Crime [ ]
Cold/Snow [

]

0.6
0.4
0.2
0.0 FN TP FP

Precipitation [ ]

0.8
0.6
0.4

1

precipitation risk
.8 .6 .4 .2

0.6
0.4

0

0.2

0.2
0.0

FN TP FP

0

.2 .4 .6 .8
cold/snow risk

0.0

1

FN TP FP

d. Seismic Events, 04-08-2020, 05-08-2020, 06-08-2020

Significant
Events
0.5
0.4
0.3
0.2

1

violent crime risk
.8 .6 .4 .2

0

0

.2 .4 .6 .8
property crime risk

1

0.1
0.0

FN TP FP

0

.2 .4 .6 .8
1
predicted event risk

Fig. 1. Snapshots of Spatio-temporal Rare Event Prediction. Panels a-e illustrate forecasts in diverse systems using Fractal Nets,
each with distinct spatio-temporal quantization and event definitions (See Extended Data Tab. 1 and 2). With the exception of seismic
prediction, these forecasts are actionable, ✐✿❡, are done early enough (✼ days for weather, ✸-✼ days for urban crime and ✶✷✵ days for
earthquakes), and the events are crucial enough, to trigger mitigation responses. We aim to predict seismic events above the local third
quartile magnitude, flagging events with magnitudes ❃ ✹✿✼ on average (✙ ✹✿✺ near Los Angeles, USA) without discriminating between
light (❁ ✺✿✵) or more severe events. Nevertheless we correctly predict 13 out of the largest 15 events in our out-of-sample period (August
2019 - Aug 2020) ✶✷✵ ✝ ✸ days in advance (See Extended Data Fig. 1).

3

b. Structure Recovery via Self-similar Compression

a. Fractal structures in simple processes
0
00 01

1
10 11

i.

❯✵
❯✶
❯✷

✵✭✿✹✮

✵✭✿✹✮

✶✭✿✻✮

✵✭✿✻✮

✵✭✿✻✮

✶✭✿✻✮

i. Hidden
process
✶✭✿✹✮

✶✭✿✹✮

sequence
length

❆✶✵

✵

✶✭✶❂✸✮

✵✭✷❂✸✮

✵

✶

✶

ii. Transition
Structure

✷

ii.
✵✭✶❂✸✮

✶✭✷❂✸✮

❆✶✵

✶✭✿✼✮

✵

✶✭✿✽✮

✶

✶✭✿✸✮

iii.

✶✭✿✷✮

✵✭✿✷✮

✶
✵

✵✭✿✸✮
✵✭✿✽✮

Self-similar
Compression

iii.
✵✭✿✺✮

✵

✶✭✿✺✮

✶✭✿✸✮

✶

✵

✶

✵✭✿✼✮

iv.

✵

✵

✶

✵

✵

✶

✶

✶

✵

✵
✶
✵

✶✭✿✽✮
✵✭✿✷✮

✵✭✿✼✮

✵

✶

✶
✵

Fig. 2. Fractal Structures in Stochastic processes and Self-Similar Compression. Panel a. We map the process states to the unit
interval, associating the history of observations from stationary distribution to the binary representation of the points in ❬✵❀ ✶❪. Stacking
these representations as the length of the observation increases reveals process-specific fractal structures shown in (i)-(iv) of panel a.
As an example in (i), because every sequence with the last symbol ✵ leads to the state q✵ , we can interpret ❯❦ as the subset of the unit
interval where the ❦t❤ digit in the binary representation is ✵. The block highlighted in red then maps from the sub-tree under the node
reached by ✶✵ (and referred to as ❆✶✵ ) in the binary tree shown in panel b(ii). Also note that the highlighted block in panel a(i) is a scaled
copy of the full representation. Panel b. The input data stream induces a ♠-ary tree, where ♠ is the alphabet size, with probabilities
attached to each branch in each split. SSC recursively identifies subtrees that are sufficiently similar to obtain a finite generative model.
For example for the the process in panel a(i), we note that the probability of a ✵ from the stationary distribution is different from that after
we observe a ✵, which is also different from after we observe a ✶ - leading to producing ✷ new states in the first step. But then we realize
that the probability of any string after we observe ✵✵ is the same after observing a single ✵, implying we have a loop labeled ✵ at the
state reachable by the first ✵. Continuing like this, we distill the complete transition stricture in six steps as shown in panel b(iii).

can “forget” what happened before, implying that future trajectories from each distinct visit of the same state
are statistically indistinguishable. Since an ergodic system must revisit its states, the observed dynamical
behavior must have self-similar structures, with the set of future paths from any state essentially a scaled
copy of the subset of futures from any subsequent visit of the same state. Fig. 2a demonstrates this idea for
simple processes with a binary alphabet; we map current states to the unit interval, associating the transpired
history with the binary representation of points on ❬✵❀ ✶❪, revealing the process-specific self-similar organization.
Uncovering hidden dynamical states is thus equivalent to recovering fractal structures in observed data, using
what we refer to as self-similar compression (SSC) as illustrated in Fig. 2b.
In our approach to learning this emergent self-similar structure, we employ no “neurons”, no fixed activation

4

a. Elemental unit model for Fractal Net architecture
event sequence (Rare Events:1)
source
000110001000000

q✵

ce
ur
so

s

H ✁
s

q✸

-ta
e
rg
nk
t li

current time

target

r

Output probability
distribution at target

✁ steps

r❀

q✶

Inferred from data:
• states q✵ ❀ q✶ ❀ q✷ ❀ q✸
• transitions
• output event distributions

q✷

00010001000001000000010000001

Reads from s,
predicts at r,
with a delay of

XPFSA Model

✁

♥✶

♥✷

♥✷

♥✸

♥✸

Van der Pol

✇✐❥ ❜✐

Van der Pol

c. Fractal Net Architecture
multi-scale transducers

✁

♥✵

✁✷

✁✵

✁✵✵

♥✵

✁✵✷

linear

♥✶

Duffing

hidden layers

d. Coeff. of Causality (✌ ) in FN vs gradient decay in NN)
①❴
autocor of ①❴
✌ ✭✁✮ of ①
loss gradient
✶
✶
✶
✺ ✂✶✵ ✻
✵✿✺
✵✿✺
✵
✵
✵✿✺
(i)
✵✿✺
✺
✵
✵
✶
✷ ✶ ✵ ✶ ✷ ✵ ✷✙ ✹✙ ✻✙ ✵ ✷✙ ✹✙ ✻✙ ✸✙ ✹✙ ✺✙ ✻✙
✶
✹
✵✿✹
✷ ✂✶✵ ✸
✷
✵
✿
✺
✵
✵✿✷
(ii)
✵
✷
✵
✹
✵
✷ ✶ ✵ ✶ ✷ ✵ ✷✙ ✹✙ ✻✙ ✵ ✷✙ ✹✙ ✻✙ ✸✙ ✹✙ ✺✙ ✻✙
✵✿✽
✷
✶
✷
✺
✵✿✻
✶
✵ ✂✶✵
✵✿✹
✵✿✺
✵
(iii)
✵✿✷
✷
✶
✵
✵
✵ ✷✙ ✹✙ ✻✙ ✵ ✷✙ ✹✙ ✻✙ ✸✙ ✹✙ ✺✙ ✻✙
✶ ✵ ✶
✶
✶
✷
✷ ✂✶✵ ✹
✵
✿✺
✵
✵
✵
✿✺
(iv)
✷
✷
✵
✵
✷ ✵ ✷ ✵ ✷✙ ✹✙ ✻✙ ✵ ✷✙ ✹✙ ✻✙ ✸✙ ✹✙ ✺✙ ✻✙
✶
✶
✺ ✂✶✵ ✻
✺
✵
✿✺
✵
✵
✵
✿
✺
(v)
✺
✺
✵
✵
✷ ✵ ✷
✵ ✷✙ ✹✙ ✻✙ ✵ ✷✙ ✹✙ ✻✙ ✸✙ ✹✙ ✺✙ ✻✙
steps (sec)
time (sec)
✁ (sec)
①
Duffing

b. Standard NN Architecture

e. Linear Combination of Local Activations with Memory

✁✵✵✸

♥✶

Learned activation model
from source s to target r
with delay
❥

✁✰

♥✶

r ✰✁ ❂

✁✵✸

❍♥♥✷✵❀✁✸
♥✷

✁✸

❳

t

s

✷❙

❥

♥✷

≦

✵

✏

✦ ✁✰ H ✁✰ s ✶
s

s

r❀

❥

target prediction
steps
from current time

r❀

❥

t

✑

❥

source data
upto ❥ steps
before current time

✁

Fig. 3. Fractal Net Organization. Panel a. SSC computes elemental units, which are crossed probabilistic automata inferred from
data, making predictions
steps in future of the target stream based on current state estimated from the source stream. Panels b
and c contrast the schematic differences between the NN and the FN architectures. Panel d illustrates the ability to avoid vanishing
gradients, where the last column shows the rapidly degrading gradients with Long Short-term Memory (LSTM) recurrent NN models,
while column 3 shows the stable behavior of the coefficient of causality ✌ with time shift . Panel d shows the linear combination of
local models, highlighting our linear combination of non-linearities instead
of non-linear filtering of linear combinations of inputs in NNs
.

✁

✁

5
TABLE 1
Performance comparison of the Fractal Net prediction and recurrent neural network with LSTM units

✵✺
✿

✵ ✼✺
✿

AUC (Fractal Net)

AUC distribution
RNN
Fractal Net

✶
✶ ✵✵✵
❀

Average ROC

Average precision/recall

RNN
Fractal Net

RNN
Fractal Net

✶
✵✾

✿

✺✵✵

❂ ✶✵✿✵✪

✵✻

✿

✿

✶

✻✵
✹✵

⋆
✍❆

✵✻

✿

✵✹

✿

✵

✿

✶
tpr

✹✵
✷✵

✶

✵✽
✿

⋆
✍❆

✶✼✿✼✪

=

✵✻
✿

✵

precision

✻✵

❀

✶ ✵✵✵

✿

✵✻
✿

✶
✵✽

②

✶✵✿✵✪

✿

=

✿

❂ ✹✶✽ ✻✪

✵✻

⋆
✍❆

✻ ✾✪

✵✹
✿

✶✺✵

✶

✶

✵✽

✵ ✽ ❂ ✺✵ ✽✪
✵✻
②

✶✵✵

✿

⋆
✍❆

✺✵

✿

✶✷✿✸✪

=

✵ ✵✻
✿

✵✻
✵✷ ✵✹ ✵✻ ✵✽
✿

✵✽
✿

AUC

✶

✍❇
✿

✿

✿

✿

✿

✿

fpr

✵✹
✿

✵

✵✺
✿

✶✵✵✻ ✂
✺✶✵
✷
✾✶✸
✶✵✵
✻
✹ ✵✪

Chicago Crime:
✵
✵,
spatial tile:
sequences:
,
temporal res.: day,
in-sample length:
,
out-sample length:
,
pred. horizon: days,
frequency: property
✿
, violent ✿

✍❇
✿

✿

✵✻

✵

✹ ✼✪

✿

✿

✺✵✵

✶✵✵✻

②

✵✹

✵✽

❀

Atlanta Crime:
✵
spatial tile:
✵,
sequences:
,
temporal res.: days,
in-sample length:
,
out-sample length:
,
pred. horizon: days,
frequency: property
✿
, violent ✿ .

✍❇ ❂
✶✺✵✪

✵✽

✶

✶ ✺✵✵

✶✷✾✻
✶✷✶
✶✷✵
✷ ✹✻✪

✵✻

✶✸✿✺✪

=

✼
✼ ✺✪
✶✵✪

✸ ✂✸
✹✼✵
✸

②

✍❇
✿

✿

✿

✷✶✾✷
✷✹✵

Earthquake:
✍,
spatial tile: ✍
sequences:
,
temporal res.: days,
in-sample length:
,
out-sample length:
,
pred. horizon:
days,
frequency: ✿
.

❂
✶✾✶ ✸✪

✵✽

✵✽

✷✵

frequency

✷✽ ✸✪

✵✼

✿

✵

②

✍❇
✿

✵✽

⋆
✍❆

✺✸✶✼
✶✷

❂
✶✻✶ ✾✪

✿

✵✽

US Weather:
sequences:
,
temporal res.:
hours,
in-sample length:
,
out-sample length:
,
pred. horizon: days,
frequency: precipitation
✿
, winter ✿ ,
severe events
.

✶

✾✺✽ ✂✶✵✵✼
✻✶✻✺
✶
✶✵✾✺
✶✵✵
✼
✼ ✻✪

Philadelphia Crime:
✵
✵,
spatial tile:
sequences:
,
temporal res.: days,
in-sample length:
,
out-sample length:
,
pred. horizon: days,
frequency: property
✿
, violent ✿ .

✾ ✶✪

✾✵✼ ✂ ✾✽✻
✶✵✸✼
✶
✶✵✾✼
✶✵✵
✸
✽ ✶✪

recall

⋆

✍❆ : AUC outperformance is measured as the percentage increase in the AUC averaged over the spatial tiles.

②

✍❇ : Sensitivity outperformance is measured at

✾✵✪ positive predictive value (PPV).

functions, no user-specified loss functions, and no global optimization via back-propagation. Instead, SSC
distills local models (See Fig. 3a), which are assembled into a predictive network (See Fig. 3c) which we call
the Fractal Net (FN). FN is archetypically distinct from the familiar NN architecture (See Fig. 3b vs Fig. 3c for

6
contrasting visuals). Each of our elemental units (SSC models) is a probabilistic finite state automaton (PFSA)
or a generalized probabilistic automaton for cross-dependencies (crossed PFSA or XPFSA). Thus, given a
source s and a target stream r, we infer models Hsr❀✁ (See Fig. 3a), which make predictions steps in future
from the current observation step, in the stream r after making observations in the stream s. These models
have a finite set of states, with the number of states, the state transition map and the output event probabilities
all inferred from data without prior constraints.

✁

Our models are discrete, and they learn from (and predict) categorical input streams. This is appropriately
suited for modeling rare event dynamics, where we treat an event as a and its absence . In applications with
continuous event magnitudes, such as seismic modeling, we use quantization to identify events of interest,
❡✿❣✿, treating all events with magnitude above the local third quartile as a .

✶

✵

✶

Instead of the number of layers of neurons, depth in FNs is reflected by average number of states in the
inferred SSC models. Instead of assuming fixed memoryless non-linear activation functions (such as tanh,
rectified linear unit 10 etc.), here we infer local activation structure from data. The individual SSC models dictate
link activation as a function of their current state, which is in turn determined by event history. Number of model
states reflects the temporal depth that might be important to determine link state. This results in deeper models
with a significantly smaller parameter set (See Extended Data Tab. 2).
Notably, as illustrated in Fig. 3c, each source-target link can have multiple SSC models operating at disparate
time scales. Thus, in contrast to layer stacking in Long Short-term Memory (LSTM) NNs, we model multiple
timescales explicitly (See Methods: Step Two and Extended Data Algorithm 1 line 11-22). As an added bonus,
this approach also addresses the problem of vanishing and exploding gradients. Back-propagation in NNs
proceeds by updating network parameters as a function of the iterated loss gradient. Often this decay is
too fast for effective learning 24 , and despite recent architectural modifications, the problem persists 24,25 . In
contrast, SSC inference does not propagate any gradients; identifying a distinct model Hsr❀✁ for each value of
. We compare the decay behavior in the two frameworks in Fig. 3d, where 1D systems ranging from being
linear (subpanel i) to those operating in non-linear chaotic regimes (subpanel ii-v) are analyzed. We find that
the loss gradient vanishes exponentially fast in the case of NNs (column 4) irrespective of the system, whereas
for FNs the corresponding measure – the coefficient of causality ✌ (Column 3) is analogous to the respective
autocorrelation functions for ① (Column 2).

✁

❴

As a final point of architectural contrast, we switch the order of the linear and non-linear operators: the nonlinear link activations are combined linearly to be passed on as inputs to downstream nodes (See Fig. 3d), ✐✿❡✿,
in FNs we have linear combination of inferred non-linear link activations instead of NNs where we have fixed
non-linear activation of linear combination of nodal inputs. Local weights are easily computed with standard
regressors, allowing local changes to be integrated on-the-fly (See Methods: Step One).
To briefly describe how SSC actually infers PFSAs or their crossed versions, we note that the input data
stream induces a ♠-ary tree, where ♠ is the alphabet size, with probabilities attached to each branch in each
split. SSC recursively identifies subtrees that are sufficiently similar to obtain a finite generative model of the
ergodic stationary process (See Fig. 2, panel b, i-iii). Thus SSC uncovers the emergent self-similar structure
that arises if different histories lead to identical future stochastic evolution, aiming to find a sufficiently good
finite generative model (See Supplementary Text: Defn. 5 and Defn. 7). As in Hidden Markov Models (HMM),
we assume to only see outputs from states and not the states themselves. PFSAs are indeed a special class of
HMMs (See Supplementary Text: Sec. II-D), but with distinct inference algorithms having the ability to discover
structure.
Not all processes have finite generators. The necessary and sufficient condition for our finite models to
exist (See Supplementary Text: Sec. II-F and Sec. III) is related to the topological properties of the set of
causal states: by definition, we reach the same causal state via distinct paths if the futures are statistically
indistinguishable (See Supplementary Text: Sec. I). For SSC to yield a finite model, it is sufficient to have a
finite set of causal states, but not necessary (Thm. SI-2). We show that a process has a finite PFSA model
only if the set of causal states that are reachable infinitely often (✐✿❡✿ are persistent) has a finite number of
limit points (Thm. SI-5 and Thm. SI-7). As a consequence of these results, we show that NNs are adequate to

7
model stochastic processes only if every sample path uniquely identifies a single causal state, even if we do not
know the initial state precisely, ✐✿❡✿, if all sample paths are synchronizing inputs. We show that this condition is
equivalent to a finite set of causal states, which is the precise criterion for NNs to model stochastic phenomena
(Thm. SI-2). Thus, it is now easy to construct counterexamples where NN inference fails irrespective of the
number of samples or the number and complexity of layers (See Extended Data Fig. 2).
Finally, precise results on sample complexity for NNs are unknown. In contrast, we establish explicit results on
sample complexity, and show that we obtain good models with high probability (See Methods: Performance
Analysis and Supplementary Text: Sec. VIII). More precisely, let ✧❀ ✧✵ be arbitrarily small positive numbers, with
input length that is polynomial in ❂✧ and logarithmic in ❂✧✵ , for a reasonably separated family of generating
models, the probability that the difference between the inferred and true generating models is bigger than ✧ as
measured by the KL divergence ❉KL is upper-bounded by ✧✵ . ✐✿❡✿, with input length ♥ ❖ ♣♦❧② ❂✧❀
❂✧✵ ,
we have

✶

✭

✭

✶

✮

❂ ✭

✭

✮

✮ ✶

P r ❉KL generating PFSA ❦ inferred PFSA ❃ ✧ ❁

✭✶ ❧♦❣ ✶ ✮✮

✧✵

(1)

A schematic map of how mathematical development leads to the performance bounds is shown in Extended
Data Fig. 3.
To demonstrate FN applicability in diverse spatio-temporal phenomena, we consider 1) rare weather events
in contiguous US, 2) global seismic events, and 3-5) urban crime in Atlanta GA, Chicago IL, and Philadelphia
PA. These applications, enumerated in Tab. 1 highlight our strictly superior performance over carefully tuned
LSTMs. In each of these cases, we begin with a spatio-temporal log enumerating events of interest, along with
their space-time coordinates. For example, for US weather, we use events logged by the the Automated Surface
Observing Systems (ASOS) network recording extreme precipitation and cold/snow events. The seismic event
log is curated by the United States Geological Survey (USGS) hazards program, where we forecast events
within ✍ ✂ ✍ tiles with a magnitude greater than the local third quartile of all events within the past decade.
For forecasting urban crime, we log daily occurrences of property crimes (consisting of burglary, theft etc.)
and violent crimes (homicide, assault, battery etc.) within a couple of city blocks. We tune discrete time-steps
automatically to maximize the average entropy rate of the data streams, resulting in steps measuring
hours
for the weather models, days for the seismic prediction, and
days for urban crime. With the exception
of the precipitation event in weather modeling, all event frequencies are lower than %. We also choose how
far into future we make predictions (prediction horizon), which is chosen to be week for weather, months for
seismic prediction, and
days for urban crime (See Tab. 1 for details) – performance modestly improves
for shorter and degrades rapidly for longer horizons. All these predictions, except perhaps in the case of the
seismic events, are actionable, ✐✿❡✿, are done precisely and early enough to intervene or mitigate. For the
seismic case, we target events with magnitude greater than the third quartile of the magnitudes of all local
recorded events in the past decade. (See Extended Data Fig. 1a, mean: ✿ ). Thus, we do not discriminate
between light ( - ✿ ) or more severe events to maintain statistical power. Nevertheless we correctly predict
out of the largest
events in our out-of-sample period (August 2019 - Aug 2020)
✝ days in advance
(See Extended Data Fig. 1c-d). In all these problems, we significantly outperform carefully tuned LSTMs. As
shown in Table 1, we boost sensitivity at
positive predictive value by
✿
for extreme weather events,
✿
for seismic activity over the local third quartile,
✿ ,
✿ , and ✿
for criminal infractions in
Chicago, Philadelphia and Atlanta respectively. Outperformance measured by the increased area under the
receiver operating characteristic curve for the corresponding problems is given by ✿ , ✿ , ✿ , ✿ ,
and ✿
respectively.

✸

✸

✸

✶

✸ ✼

✶✵

✹

✹✼

✹✹✾
✶✺

✶✷✵ ✸

✾✵✪

✶✾✶ ✸✪

✶✷

✶ ✷

✶✺✵ ✵✪ ✹✶✽ ✻✪

✶✷ ✸✪

✶✸

✶✻✶ ✾✪
✺✵ ✽✪
✶✵ ✵✪ ✾ ✷✪ ✶✼ ✼✪ ✶✵ ✵✪

Beyond predictive performance, FNs provide insight into dynamical properties, which is generally difficult with
NNs. Each SSC model Hsr❀✁ has a coefficient of causality ✌rs
intuitively defined as:

✁

✭✁✮

uncertainty of the output steps in future in r with observation of the past in s
(2)
average uncertainty of the output steps in future in r
specifying how much information about the -step future of the target stream is obtained, per unit bit acquired
about the source stream s. As shown in Fig. 3d, for 1D systems ✌ss is analogous to autocorrelation: this is
expected since higher autocorrelation implies higher predictability. In general, the average -dependence of
✌ss provides us with simple sanity checks. For example, the physical nature of weather and seismic systems

✌r❀s ✁

❂✶

✁

✁

✁

8

a. Weather

c. Chicago Crime

b. Earthquakes

(i) ✌
❡ Variation with Aftermath Event Probability ♣
♣

✘

✶
✭✿✶✶✼✻t✮✷✿✺

✌

✶✿✵
✵✿✺

♣

✘

event frequency ♣

✶
✭✿✵✶✶✺t✮✿✾

♣

✶✿✵

✵✿✻

✵✿✽

✵✿✹

✵✿✻

✺

✶✵

✘

✶
✭✿✵✷✸t✮✶✵

✰ ✵ ✵✵✶
✿

t

✵✿✷

✵✿✹
✵✿✵

d. Atlanta Crime e. Philadelphia Crime

✵✿✷

✸✵

✻✵

✾✵

✵✿✵

✶✵

✷✵

✸✵

♣

❤✭♣✮

✶
✭✿✵✵✺t✮✶✿✺

♣

✶✿✵

✶✿✵

✵✿✺

✵✿✺

✵✿✵

✹✵

✘

❡❂✶
✌

✘ ✭ ✵✸✷✶ ✮✶ ✺
✿

t

✿

✵✿✵
✷✵

✹✵

✻✵

✽✵

✶✵

✷✵

✸✵

✹✵

✶✵

✷✵

✸✵

✹✵

time [day]
(ii) Observed ✌ Decay with Time
✵✿✽✵

✵✿✽✵

✌

rescaling and translation of ✌
❡

✌

✵✿✻✹
✵✿✽✵

✵✿✻✵

✵✿✻✵

✵✿✹✵
✺

✸✵

✻✵

✾✵

✵✿✻✵

✵✿✻✵

✵✿✼✺

✶✵

✵✿✻✺

✵✿✻✷

✵✿✺✺

✵✿✺✽
✶✵

✷✵

✸✵

✹✵

✷✵

✹✵

✻✵

✽✵

✵✿✺✵

time [day]
(iii) Observed ✌ Decay with Distance
✵✿✷✺
✵✿✶✺

✵✿✶✺

✌

✵✿✷✵

✵✿✶✵

✵✿✶✺

✵✿✶✹

✵✿✶✵
✷✵

✹✵

✻✵

✵✿✵✹

✵✿✵✷

✵✿✵✷

✵✿✵✵

✵✿✵✺
✾✵

✵✿✵✹

✶✽✵ ✷✼✵ ✸✻✵

✷

✵✿✵✵
✷

✹

✹

✷

✹

distance [mile]
Fig. 4. Dynamical Properties Revealed by the Coefficient of Causality ✌ . Row (i) illustrates that specific decay behaviors for the
aftermath event frequency yields different behaviors of ✌ with time, which is then shown to be consistent with observed ✌
behavior
(upto scaling and translation) in row (ii). For seismic activity, the aftermath event frequency is known to follow the Omori-Utsu law
with a decay exponent (0.7-1.5) consistent with our analysis (1.5). The very different behavior in the case of crime in Chicago is also
explainable via rapid decay and subsequent recovery of event frequency as shown in column c (See Methods for discussion). Row (iii)
illustrates the variation of ✌ with distance. As required in physical systems (columns 1 and 2) we find a rapid decay. This is absent in the
social systems (columns 3-5), suggesting long range persistence in organization akin to critical phenomena.

❡

✁

necessitates an influence decay as we move away in space and time from the event epicenters – no “teleportation” of influence should be possible. Thus, in the neighborhood of events we expect that on average,
✌ss must decay with increasing , and ✌rs should decay as physical distance between the source and the
target increases. Fig. 4 rows 2 and 3 illustrate that these patterns are correctly recovered for the weather and
the seismic systems. Interestingly while the temporal decay also holds true for urban crime, we find no such
decay in the spatial dimension for these social systems. This discrepancy possibly suggests that urban spaces
operate as one single unit with long-ranged coherence not unlike self-organized criticality suspected to emerge
in flocks of birds 26 and other physical systems near criticality.

✁

✭✁✮

In addition, ✌ss
also sheds light on event frequency after a rare event. Our models have specific states
which have large event likelihoods. As we move away from these states, the event likelihood decays. In the
context of earthquakes, the increased event frequency (aftershocks) following an event is known to rapidly
decay with time according to the empirical Omori-Utsu law 27–32 . This aftermath decay may be related to the
✌ss
response. To see this, note that the expression for ✌ (Supplementary Text Defn. 38) implies:

✭✁✮

❳
✌rs ❂
⑥✐
✐✷◗

✥

✦

(3)
✶ ✭✭ ✮✮
where ❤✭✁✮ is the binary entropy function (❤✭①✮ , ① ❧♦❣✭①✮✰✭✶ ①✮ ❧♦❣✭✶ ①✮), and ⑥✐ is the stationary probability

❤ ♣✐
❤ ♣✵

9
of the inferred state in stream s, ♣✐ is the event probability in stream r, and ♣♦ is the average event probability.
Considering “self-models”, ✐✿❡✿, where s and r are the same, we have the bound:

✌ss

✭✁✮ ≦ ❛✭✁✮ ✰ ✭✶

✭ ✮✮

❤ ♣❊
✁

(4)

❬✵ ✶❪

where the subscript ❊ refers to state(s) with the maximum event probability, and we use the fact that ✽✐⑥✐ ✷ ❀
and ❤ ♣✵ ≦ . Under the idealized assumption that events are unlikely from states other than ❊ ,
with ✐ ⑥✐
❛
is a weak function of , implying that the inferred ✌ vs plots suggest how the event frequency varies in
the aftermath. Fig. 4 illustrates that observed ✌ behaviors may be approximately reconstructed from variations
in the aftermath-event frequency. None of the above insights are possible within the NN framework, in which
the gradient decay is purely an artifact of the optimization algorithm, and does not reflect system properties.

P ❂✶

✭✁✮

✭ ✮ ✶
✁

✁

A key limitation of FNs is the need for categorical data in self-similar compression. In systems with continuousvalued observations, we can set a magnitude threshold effectively defining the events of interest (as demonstrated in seismic modeling). However more complex event definitions might be warranted elsewhere. Future
research will investigate these issues, and attempt to address event frequencies significantly lower to what
have been demonstrated here.
Thus, in this study we have laid the groundwork to broaden the applicability of data driven analytics to rare
event modeling in complex systems. We hope that this technology, integrated with existing tools, will push the
boundaries on our current limits of predictive mitigation of natural disasters and catastrophic societal events.

R EFERENCES
[1]

Sornette, D. Why stock markets crash: critical events in complex financial systems, vol. 49 (Princeton
University Press, 2017).
[2] Telesca, L., Cuomo, V., Lapenna, V. & Macchiato, M. Detrended fluctuation analysis of the spatial variability
of the temporal distribution of southern california seismicity. Chaos, Solitons & Fractals 21, 335–342
(2004).
[3] Yakovlev, G., Turcotte, D. L., Rundle, J. B. & Rundle, P. B. Simulation-based distributions of earthquake
recurrence times on the san andreas fault system. Bulletin of the Seismological Society of America 96,
1995–2007 (2006).
[4] Grefenstette, E., Hermann, K. M., Suleyman, M. & Blunsom, P. Learning to transduce with unbounded
memory. In Advances in neural information processing systems, 1828–1836 (2015).
[5] Kaiser, Ł. & Sutskever, I. Neural gpus learn algorithms. arXiv preprint arXiv:1511.08228 (2015).
[6] Dehghani, M., Gouws, S., Vinyals, O., Uszkoreit, J. & Kaiser, Ł. Universal transformers. arXiv preprint
arXiv:1807.03819 (2018).
[7] Voulodimos, A., Doulamis, N., Doulamis, A. & Protopapadakis, E. Deep learning for computer vision: A
brief review. Computational intelligence and neuroscience 2018 (2018).
[8] Liang, H., Sun, X., Sun, Y. & Gao, Y. Text feature extraction based on deep learning: a review. EURASIP
journal on wireless communications and networking 2017, 1–12 (2017).
[9] Hutson, M. Ai shortcuts speed up simulations by billions of times (2020).
[10] Bishop, C. M. Pattern recognition and machine learning (springer, 2006).
[11] Hamill, T. M. & Whitaker, J. S. Probabilistic quantitative precipitation forecasts based on reforecast
analogs: Theory and application. Monthly Weather Review 134, 3209–3229 (2006).
[12] Hu, G., Bódai, T. & Lucarini, V. Effects of stochastic parametrization on extreme value statistics. Chaos:
An Interdisciplinary Journal of Nonlinear Science 29, 083102 (2019).
[13] Murphy, A. H. Probabilities, odds, and forecasts of rare events. Weather and forecasting 6, 302–307
(1991).
[14] Ouarda, T. B., Girard, C., Cavadias, G. S. & Bobée, B. Regional flood frequency estimation with canonical
correlation analysis. Journal of Hydrology 254, 157–173 (2001).
[15] Kantelhardt, J. W. et al. Long-term persistence and multifractality of precipitation and river runoff records.
Journal of Geophysical Research: Atmospheres 111 (2006).
[16] Lennartz, S., Livina, V., Bunde, A. & Havlin, S. Long-term memory in earthquakes and the distribution of
interoccurrence times. EPL (Europhysics Letters) 81, 69001 (2008).

10
[17] Bódai, T. & Tél, T. Annual variability in a conceptual climate model: Snapshot attractors, hysteresis in
extreme events, and climate sensitivity. Chaos: An Interdisciplinary Journal of Nonlinear Science 22,
023110 (2012).
[18] Siokis, F. M. Multifractal analysis of stock exchange crashes. Physica A: Statistical Mechanics and its
Applications 392, 1164–1171 (2013).
[19] Zhao, X., Shang, P. & Lin, A. Universal and non-universal properties of recurrence intervals of rare events.
Physica A: Statistical Mechanics and its Applications 448, 132–143 (2016).
[20] Qi, D. & Majda, A. J. Using machine learning to predict extreme events in complex systems. Proceedings
of the National Academy of Sciences 117, 52–59 (2020).
[21] Cybenko, G. Approximation by superposition of sigmoidal functions. Mathematics of Control, Signals and
Systems 2, 303–314 (1989).
[22] Park, J. & Sandberg, I. W. Universal approximation using radial-basis-function networks. Neural
computation 3, 246–257 (1991).
[23] Ismailov, V. E. Approximation by neural networks with weights varying on a finite set of directions. Journal
of Mathematical Analysis and Applications 389, 72–83 (2012).
[24] Hochreiter, S., Bengio, Y., Frasconi, P., Schmidhuber, J. et al. Gradient flow in recurrent nets: the difficulty
of learning long-term dependencies (2001).
[25] Schmidhuber, J. Learning complex, extended sequences using the principle of history compression.
Neural Computation 4, 234–242 (1992).
[26] Mora, T. & Bialek, W. Are biological systems poised at criticality? Journal of Statistical Physics 144,
268–302 (2011).
[27] Omori, F. On the after-shocks of earthquakes, vol. 7 (The University, 1894).
[28] Utsu, T. A statistical study on the occurrence of aftershocks. Geophys. Mag. 30, 521–605 (1961).
[29] Enescu, B., Mori, J., Miyazawa, M. & Kano, Y. Omori-utsu law c-values associated with recent moderate
earthquakes in japan. Bulletin of the Seismological Society of America 99, 884–891 (2009).
[30] Davidsen, J., Gu, C. & Baiesi, M. Generalized omori–utsu law for aftershock sequences in southern
california. Geophysical Journal International 201, 965–978 (2015).
[31] Hainzl, S. & Marsan, D. Dependence of the omori-utsu law parameters on main shock magnitude:
Observations and modeling. Journal of Geophysical Research: Solid Earth 113 (2008).
[32] GRILLI, L., La MANNA, F. & PACELLI, V. Financial markets, shocks and omori-utsu law. Journal of Applied
Economic Sciences 13 (2018).
[33] Chattopadhyay, I. & Ray, A. Structural transformations of probabilistic finite state machines. International
Journal of Control 81, 820–835 (2008).
[34] Valiant, L. G. A theory of the learnable. Commun. ACM 27, 1134–1142 (1984).
[35] Moosavi, S., Samavatian, M. H., Nandi, A., Parthasarathy, S. & Ramnath, R. Short and long-term
pattern discovery over large-scale geo-spatiotemporal data. In Proceedings of the 25th ACM SIGKDD
International Conference on Knowledge Discovery & Data Mining, 2905–2913 (2019).
[36] Rnn (2020 (accessed Sep 3, 2020)). URL https://www.tensorflow.org/guide/keras/rnn.
[37] Lstm layers (2020 (accessed Sep 3, 2020)). URL https://www.tensorflow.org/api docs/python/tf/keras/la
yers/LSTM.
[38] Lstm time-distributed layers (2020 (accessed Sep 3, 2020)). URL https://www.tensorflow.org/api docs/py
thon/tf/keras/layers/TimeDistributed.
[39] Abadi, M. et al. TensorFlow: Large-scale machine learning on heterogeneous systems (2015). URL
https://www.tensorflow.org/. Software available from tensorflow.org.
[40] Turchetti, C., Conti, M., Crippa, P. & Orcioni, S. On the approximation of stochastic processes by
approximate identity neural networks. IEEE Transactions on Neural Networks 9, 1069–1085 (1998).
[41] Goodfellow, I., Bengio, Y. & Courville, A. Deep learning (MIT press, 2016).
[42] Sak, H., Senior, A. & Beaufays, F. Long short-term memory recurrent neural network architectures for
large scale acoustic modeling. In Fifteenth annual conference of the international speech communication
association (2014).

11

M ATERIALS AND M ETHODS
Fractal Net is assembled from local SSC models which are, in general, crossed probabilistic automata
(XPFSA). The theoretical development supporting the claims in the main text is presented in the Supplementary
Text. A map of how the mathematical proofs relate to each other is presented in Extended Data Fig. 3,
which shows that the key concepts (causal states, persistent causal states, synchronization, and accumulation
measures) all come together to establish the correctness of the inference algorithm(s). The rest of this section
describes the Fractal Net construction.
The construction of a Fractal Net consists of two steps: 1) local SSC model generation and network pruning
and 2) local model aggregation for comprehensive prediction. As discussed in the main text, these local models
determine link activation based on their current state, and event prediction is accomplished by aggregating
these local activations via a local regressor. No global optimization of these aggregation function is necessary.
The model generation step of Fractal Net is accomplished by the algorithms GenESeSS (See Extended Data
Algorithm 2) and xGenESeSS (See Extended Data Algorithm 3). GenESeSS and xGenESeSS are implementations
of the self-similar compression (SSC) discussed in the main text. GenESeSS yields PFSA models that capture
how the history of an input process influences its own future, and xGenESeSS produces XPFSA models that
captures how the history of a source process influences the future of a target process. The Fractal Net
construction is described in Extended Data Algorithm 1, and takes as input a set ❢①s s ✷ ❙ ❣ of length-♥
time series, hyperparameters ✧ and ♥✵ ❁ ♥ for local model inference, max for maximum time delay, and ✌✵
for thresholding admissible models. For each target sequence ①r , Fractal Net outputs a set of admissible
models ▼r with a scalar weight for each model in ▼r via model inference and pruning (line 1-10) and training
of the aggregation weights (line 11-22).

✁

✿

Step 1: Model inference and pruning
The Fractal Net framework models the influence from a source time series ①s on a target time series ①r at a
particular time delay by an XPFSA ❍r❀s ✁ (line 7). Thus, we infer ❥❙ ❥ max XPFSA models for each ①r which
yields ❥❙ ❥✷ max models in total. Since the number of XPFSA models increases quadratically with the number of
time series and strength of the links may vary, pruning low-performing models early is important for parsimony.
Fractal Net rejects models by thresholding on the coefficient of causal dependence ✌r❀s ✁ of model ❍r❀s ✁ (line
8), which measures the strength of dependence of the output sequence on the input one. More specifically, we
have
uncertainty of the next output in ①r with observation of ①s
(5)
✌r❀s ✁
uncertainty of the next output in ①r
✌ can be evaluated from the synchronous composition (See Supplementary Text Defn. 39) of the PFSA that
models the input process (line 6) and the XPFSA that models the causal influence. In Extended Data Fig. 4j
we show the synchronous composition of the PFSA in Panel a to the XPFSA in Panel i. For more details on
synchronous composition and coefficient of causal dependence, see Supplementary Text Sec. VII. Fractal
Net retains the model ❍r❀s ✁ if and only if ✌r❀s ✁ is greater than a pre-specified threshold ✌✵ . At the conclusion of
Step 1, Fractal Net returns an admissible set of models

✁

✁

✁

❂✶

♥

for each r ✷ ❙ .

▼ ❂ ❍ ✁ ✿ ✌ ✁ ❃ ✌✵
r

s

s

r❀

r❀

♦

(6)

Step 2: Train linear weights
In this step, we integrate the local models in ①r ’s admissible set for forecasting events in ①r . To do this, Fractal
s
Net trains a linear coefficient ✦r❀
✁ for each ❍r❀s ✁ ✷ ▼r (line 22) so that the final prediction for ①r at time step ❤

12
is equal to

❳
❍r❀s ✁ ✷▼r

s ❍s
✦t❀
✁ r❀✁

✏

✑

✭①s✮❤ ✁ ❀

(7)

where ①s ❤ ✁ is the truncation of ①s at ❤
. To compute the coefficients, we solve a regression problem
Reg ❳❀ y (line 22) for each r ✷ ❙ with the predictor variables being predictions xt s❀
obtained by running
each sequence ①s ♥✵ ✰t ✁ through ❍r❀s ✁ (line 17), and the outcome variable being ①r ♥✵ t , value of ①r at
time ♥✵ t (line 18). Hence, the ❳ matrix is the ♥ ♥✵ ✂ ❥▼r ❥ matrix with the entry indexed by t❀ s❀
given
by xt s❀
and y, the ♥ ♥✵ -dimensional vector with the entry indexed by t given by ①r ♥✵ t . We can solve
for the linear weights with any standard regressor.

✭

✭ ✮
✮
✰
❬ ✁❪

✁

✭ ✮

✭

✭

✮

❬ ✁❪
❬ ✰❪
✭ ✁✮
❬ ✰❪

✮

Performance Analysis of GenESeSS
On line 6 and 7 of Extended Data Algorithm 1, Fractal Net calls subroutines GenESeSS and xGenESeSS. The
two algorithms are conceptually similar: while the first infers PFSA as generators of stochastic processes,
the second infers XPFSA as models of cross-dependencies between processes. Here, we establish the
correctness of GenESeSS.
The inference algorithm for PFSA is called GenESeSS for Generator Extraction Using Self-similar Semantics.
Both the derivation of the PFSA model and its SSC inference are based on the concept of causal state. A dynamical system reaches the same causal state via distinct paths if the futures are statistically indistinguishable.
More precisely, each process over an alphabet of size ♠ gives rise naturally to an ♠-ary tree with the nodes
at level ❞ being sequences of length ❞, and the edge from the node ① to ①✛ , ✛ ✷ , labeled by P r ✛ ❥① – the
probability of observing ✛ as the next output after ①. By the definition of causal state, if two subtrees are identical
with respect to edge labels, then their roots are sequences that lead the system to the same causal state. We
show in Supplementary Text Sec. II and III that, for a process of Markov order ❦, identifying all the roots of
identical subtrees indeed offers a finite automaton structure whose unique strongly connected component is
the generating PFSA of the process. The automaton structure obtained from this subtree “stitching” procedure
is conceptualized formally in Defn. 1.

✝

✝

✭ ✮

✭ ✝

✮

❡ , where ◗ is
Definition 1 (Probabilistic Finite-State Automaton (PFSA)). A PFSA ● is a quadruple ◗❀ ❀ ✍❀ ✙
❡ ◗ ✦ P✝ , where P✝ is the
a finite set, is a finite alphabet, ✍ ◗ ✂ ✦ is called the transition map, and ✙
space of probability distributions over , is called the transition probability. (Supplementary Text Sec. II)

✝

✿

✝

✝ ✝

✿

Step 2 of the Extended Data Algorithm 2 (line 5-19) is an implementation this subtree “stitching” approach
under finiteness of input data. Note that the criterion for “stitching” two subtrees with roots ① and ①✵ is that their
edge labels are identical for all depths, which translates to ♣ ② ❥①
♣ ② ❥①✵ for sequence ② of all lengths. The
criterion is not verifiable with finite data, and hence GenESeSS identifies two subtrees if they agree on depth one.
Defining symbolic derivative ✣① to be the vector with the entry indexed by ✛ given by ♣ ✛ ❥① , GenESeSS identifies
① and ①✵ if ✣①
✣① . This approach works well under the assumption that the target PFSA is in general position,
meaning that different causal states have distinct symbolic derivatives. In practice, GenESeSS uses empirical
symbolic derivative defined below to approximate ✣① . Let ① be an input sequence of finite length, the empirical
symbolic derivative ✣①② of a sub-sequence ② of ① is a probability vector with the entry indexed by ✛ given by

✭ ✮❂ ✭ ✮

❂

✭ ✮

✵

❫

❫ ✭ ✮ ❂ number of ②✛ in ①

✣①② ✛

(8)
number of ② in ①
GenESeSS identifies two sequences (line 12) if their empirical symbolic derivatives are within an ✧-neighborhood
of each other for certain ✧ ❃ .

✵

For simplicity, we first illustrate how GenESeSS solves the transition structure of the target PFSA from a sample
path ① generated from a process of Markov order ❦. Assuming the ①✵ produced by Step 1 (line 4) is ✕, the
empty sequence, GenESeSS starts by calculating ✣①✕ , ✐✿❡✿, the empirical distribution on , and records ✕ as the
identifier of the first state. Then, GenESeSS appends ✕ with each ✛ ✷ , and calculates ✣①✛ . By the general
position assumption and assuming ① is long enough, with high probability, no ✣①✛ is within an ✧-neighborhood

❫

✝

✝

❫

❫

13
of ✣❫①✛ for ✛ , ✛ ✵ , and hence each ✛ is recorded as the identifier for a new state. In fact, GenESeSS will keep on
appending symbols to identifiers of stored states and adding new states until it reaches a sequence of length
❦ ✰ ✶. Assuming ② ❂ ✛✶ ✁ ✁ ✁ ✛❦ ✛❦✰✶ , since the process is of order ❦, we have ✣② ❂ ✣③ for ③ ❂ ✛✷ ✁ ✁ ✁ ✛❦✰✶ , and
hence, with high probability, ✣❫①② and ✣❫①③ can be within an ✧-neighborhood of each other given long enough input
①. In this case, GenESeSS identifies the state represented by ② with that of ③ . In fact, GenESeSS will identify all
states represented by sequences of length ❦ ✰ ✶ to some previously-stored states. And since no new states
can be found, GenESeSS exits the loop on line 8 after iteration ❦ ✰ ✶. Taking the strongly connected component
on line 19, GenESeSS gets the correct transition structure. See Supplementary Text Sec. III for the proof that
the PFSA thus inferred indeed generates the process. In Extended Data Fig. 4e and f, we show the labeled
directed graph obtained by subtrees stitching for two processes with Markov order ✶ and ✷, respectively. The
two examples are discussed in Supplementary Text Example 1 and 3, and their tables of causal states can be
found in Extended Data Tab. 3 and 4. The generating models of the two processes are the PFSA in Extended
Data Fig. 4a and b, respectively. We point out that the unique strongly connected component of graph in Panel
e is the PFSA in Panel a and and f, b.
✵

However, not all processes generated by PFSA have finite Markov order. For examples, the processes
generated by PFSA in Extended Data Fig. 4c and d (See Supplementary Text Examples 4 and 5 for detail) do
not have finite Markov order. For such cases, Step 2 of GenESeSS will never exit in theory, since there exists no
♥ ✷ N such that every causal state is visited for sequences with length ✔ ♥. And if we implement an artificial exit
criterion, the model inferred might be unnecessarily large, and have hard-to-model approximations. We address
this issue via the notion of synchronization – the ability to identify that we are localized or synchronized to a
particular state despite being uncertain of the initial state.
The solution for inferring succinct models in non-finite Markov order cases lies in the concept of synchronization.
In Step 1 of Extended Data Algorithm 2 (line 1-4), GenESeSS finds an almost synchronizing sequence, which
allows GenESeSS to distill a structure that is similar to that of the finite Markov order cases, and thus carry out
the subtree “stitching” procedure described before.
A sequence ① is synchronizing if all sequences that end with the suffix ① terminates on the same causal state.
A process is synchronizable if it has a synchronizing sequence, and a PFSA is synchronizable if the process
it generates is synchronizable. All processes of finite Markov order, and hence their generating PFSA, are
synchronizable.
Example: An example of synchronizable process without finite Markov order is given by the process generated
by the PFSA in Extended Data Fig. 4c. The shortest synchronizing sequence of the PFSA is ✶✶. The binary
tree of the process generated by the PFSA is given in Panel g, with darker nodes representing synchronizing
sequences. See Supplementary Text Example 4 for detail. We show in Supplementary Text Sec. IV that,
although a synchronizable process generated by a PFSA may have an infinite set of causal states, only finitely
many among them are persistent, ✐✿❡✿ repeated with non-vanishing probabilities with increasing sequence
length. We also show in Supplementary Text Sec. III that any process having a finite set of persistent causal
states whose sum of probabilities approaches ✶ as the sequence length increases has a PFSA generator
whose state set ◗ is in one-to-one correspondence with the set of persistent causal states. In Extended Data
Fig. 5a, we show the probability of sequences synchronizing to the three states of the PFSA in Extended Data
Fig. 4c. We can see that the sum approaches ✶ as the sequence length increases. Hence, although the process
has no finite Markov order, it has a PFSA generator.
Since any sequence prefixed by a synchronizing sequence is synchronizing, as long as Step 1 of GenESeSS
produces a synchronizing sequence, Step 2 of GenESeSS will work solely with causal states represented by
a synchronizing sequence. The analysis above implies that, assuming a process has a PFSA generator, the
PFSA obtained by subtree stitching on a subtree rooted at a synchronizing sequence is indeed the generating
PFSA of the process. We show in Extended Data Fig. 6g the running tree of GenESeSS for the PFSA in Panel
e. A running tree of GenESeSS rooted at state q visualizes the run of GenESeSS, given that the ①✵ found in Step
1 is a synchronizing to state q , and GenESeSS correctly identifies all new and repeating states. Nodes colored
orange in the tree are the new states GenESeSS finds in its run, while the gray states are the repeating ones.
Note that, in the running tree, if we let the gray nodes (repeating states) to travel along the gray lines until they

14
overlaps with the orange nodes (stored states) with a matching label, we get the PFSA in Panel e back.
Finally, we describe the scenario of recovering PFSA from non-synchronizable processes. An example of a
non-synchronizable process is given in Extended Data Fig. 4d (See Supplementary Text Example 5 for detailed
description). The directed graph obtained by the subtree stitching for sequences up length ✺ is shown in Panel
h. Recall that GenESeSS can recover synchronizable PFSA with the help of synchronizing sequence because
of the one-to-one correspondence between the set persistent causal states and the state set of the PFSA.
However, as we show in Supplementary Text Sec. III Example 7, the set of persistent causal state of this PFSA
is empty. In this specific example, the set of causal states has the form ❢q♥ ✿ ♥ ✷ Z❣, where Z is the set of
integers. The probability of the causal state q♥ for sequence length ❞, denoted as ♣❞ ✭q♥ ✮, can be calculated
from the recursive formula (61) and we plot ♣❞ ✭q♥ ✮ vs ♥ in Extended Data Fig. 5b for ❞ ❂ ✶✵✵❀ ✷✵✵❀ ✸✵✵❀ ✹✵✵.
It follows from Eq. (61) and also by direct observation of Fig. 5b that, as the sequence length increases, the
curves flatten out, suggesting ❧✐♠❞✦✶ ♣❞ ✭q♥ ✮ ❂ ✵ for all ♥ and hence the PFSA has no persistent states.
In order to obtain a finite generator, we consider the topological properties of the set of causal states, specifically
the closure of the set (See Supplementary Text Sec. III). We show that if the closure of the causal states has
finitely many atomic accumulation points, then the process is generated by a PFSA whose set of states is in
one-to-one correspondence with the set of atomic accumulation points of the set of causal states. In Extended
Data Fig. 5C, we show the cumulative density function of ✣① ✭✵✮ (which is the probability of producing ✵ after
observing ①) for ❥①❥ ❂ ✷✵ and ✹✵. We can see that the curve approaches a step function with two steps. In fact,
we can show that the two steps correspond to q ✶ and q✶ , the two limit points of the set of causal states. See
Supplementary Text Example 8 for detail.
From the analysis above, we see that the problem of recovering a finite structure of the target PFSA from nonsynchronizable process boils down to approximating atomic accumulation points of the set of causal states,
which induces the concept of ✧-synchronization 33 .
A sequence ① is ✧-synchronizing to the state q if the distribution ⑥① on the state set ◗ induced by ① satisfies
❦⑥① eq ❦✶ ❁ ✧, where eq is the base vector with ✶ on the entry indexed by q and ✵ elsewhere. We show
in Supplementary Text Sec. IV that there exists ✧-synchronizing sequence for arbitrarily small ✧ ❃ ✵. The
importance of ✧-synchronizing sequence is twofold: 1) since ✣❚① ❂ ⑥❚① ❡
✆, where ❡✆ is the ❥◗❥ ✂ ❥✝❥ matrix with
❡ ✭q ✮, a ⑥① close to eq give rise to a ✣① close to ✙
❡ ✭q ✮. And 2) although sequences
the row indexed by q given by ✙
prefixed by an ✧-synchronizing sequence to a state q may not remain ✧-synchronizing to state q , they are
close to q on average. As an example, let us consider the non-synchronizable PFSA in Extended Data Fig. 6f
over an alphabet of size ✸. In Extended Data Fig. 6a and c, we show scatter plots of points ✭✣① ✭✵✮❀ ✣① ✭✶✮✮ and
✭✣✵✺ ① ✭✵✮❀ ✣✵✺ ① ✭✶✮✮ for ❥①❥ ❂ ✸ and ✾. In Panel b, we show the density plot with
a Gaussian kernel of points in panel
✁
a weighted by ♣✭①✮ and, in Panel d, points in panel c weighted by ♣ ①❥✵✺ . Although Panel b shows that, when
❡ ✭q❀ ✵✮❀ ✙
❡ ✭q❀ ✶✮✮ for
sequence length gets bigger, the points become more clustered to the red dots, which are ✭✙
the three states of the PFSA, Panel a shows that ✣① s can be too scattered for GenESeSS to derive a succinct
model. However, by appending all sequences with ✵✵✵✵✵, a sequence with induced distribution on states, ⑥✵✺ ,
close to es , not only the density plots in Panel d show a much tighter clustering around the red dots, the scatter
plots in Panel c also shows points are better clustered to the red dots.
To find an almost synchronizing sequence algorithmically, GenESeSS first calculates the convex hull of symbolic
derivatives of subsequences of ① up to length ▲ (line 1-3), and then selects
a sequence
①✵ whose symbolic
♦
♥
▲
is a linear projection
derivative is a vertex of the convex hull (line 4). Since the convex hull of ✣① ✿ ① ✷ ✝
♥

♦

✆, we can expect sequence ① with ✣① being a vertex of the convex hull
of the convex hull ⑥● ✭①✮ ✿ ① ✷ ✝▲ via ❡
♥

♦

of ✣① ✿ ① ✷ ✝▲ to be a good candidate for an almost synchronizing sequence.

Due to the finiteness of data, we cannot expect to distinguish causal states whose marginals on ✝ are too
❡ of the target
close. Thus, to make explicit our identifiability conditions, we require the transition probability ✙
❡ ✭q ✮ ✙
❡ ✭q ✵ ✮❦✶ ❃ ✖ ✽q , q ✵ ✷ ◗. Under these conditions, we show in
PFSA to be ✖-distinguishable, ✐✿❡✿ ❦✙
Supplementary Text VIII a probabably approximately correct (PAC) 34 learnability for the class of synchronizable
❡ ✭q❀ ✛ ✮ ✿ ✙
❡ ✭q❀ ✛ ✮ ❃ ✵❣ ✕ ✑ . In particular, assuming ✧ ✔ ♠✐♥ ❢✖❂✷❀ ✑ ❣
✖-separable PFSA with ❥◗❥ ✔ ▼ and ♠✐♥ ❢✙

15
and the length ▲ for finding a synchronizing sequence is in the order of ❧♦❣❥✝❥ ✶❂✧, then we have
✌

P r ❉KL ● ✌ ●

✵

✁

✁

❃✧ ❁✶

✧

✵

(9)

where ●✵ is a PFSA inferred from a sequence generated by ● and of minimum length ♥ satisfying:

♥❂❖

✥

✶ ❧♦❣ ✶ ✒ ✶ ✓▼ ✰▲✭✧✮

✧✷

✓

✦

✑

(10)

We can also show that, assuming ● is a synchronizable PFSA and the sequence ①✵ found in Step 1 is a
synchronizing sequence, then an inferred PFSA ●✵ from a length ♥ sequence generated by ● satisfies
E ❉KL ●✵ ❦ ●

✁✁

✔ ♥✑ ◗✶ ✰▲
❥

❥

(11)

See Extended Data Fig. 3 for a summary of the theoretical development discussed above for guaranteeing
algorithmic performance as a directed graph.
Performance Analysis of xGenESeSS
The inference algorithm for XPFSA is called xGenESeSS, which takes as input two sequences ①in , ①out , and a
hyperparameter ✧, and outputs an XPFSA in a manner very similar to the inference algorithm of PFSA. See
Extended Data Algorithm 3 for detail.
While a PFSA models how the past of a time series influences its own future, a XPFSA models how the past
of an input time series influences the future of an output time series. Hence, while in the SSC algorithm of
PFSA, we identify sequences if they lead to futures that are statistically indistinguishable, in the SSC algorithm
of XPFSA, we identify sequences if they lead to the same future distribution of the output.
Definition 2 (Crossed Probabilistic Finite-State Automaton (XPFSA)). A crossed probabilistic finite-state
automaton is specified by a quintuple ✭✝in ❀ ❘❀ ✑ ❀ ✝out ❀ ✤✮, where ✝in is a finite input alphabet, ❘ is a finite
state set, ✑ is a partial function from ❘ ✂ ✝in to ❘ called transition map, ✝out is a finite output alphabet, and ✤
is a function from ❘ to P✝out called output probability map, where P✝out is the space of probability distributions
over ✝out . In particular, ✤✭r❀ ✜ ✮ is the probability of generating ✜ ✷ ✝out from a state r ✷ ❘ (See Supplementary
Text Sec. VII).
Extended Data Fig. 4i gives an example of an XPFSA with ✹ states. Note that a XPFSA has no transition
probabilities defined between states as a PFSA does. The XPFSA in the example has a binary input alphabet
and an output alphabet of size ✸. The bar charts next to the ✹ states of the XPFSA indicate the output probability
distributions. To generate a sample path, an XPFSA requires an input sequence over its input alphabet.
Similar to the PFSA construction approach, here we compute the cross symbolic derivative, which is the
ordered tuple P r✭✜ ❥①✮, with ✜ ✷ ✝out and a sequence ① over ✝in . We compute the empirical approximation of
the cross symbolic derivative from sequences ①in and ①out as:
number of ✜ in ①out after ② transpires in ①in
(12)
✣❫②①in ❀①out ✭✜ ✮ ❂
number of sub-sequence ② in ①in
Thus, xGenESeSS is almost identical to GenESeSS except that, in Step 1, xGenESeSS finds an almost synchronizing sequence based on cross symbolic derivatives, and in Step 2, identifies the transition structure based on the
similarity between cross symbolic derivatives. Arguments for establishing the effectiveness of GenESeSS carry
over to xGenESeSS with empirical symbolic derivative replaced by empirical cross symbolic derivative (See
Supplementary Text Defn. 44).
Loss Function As Generalized KL Divergence Between Stochastic Processes
Deviation of deterministic functions may be measured in diverse metrics, leading to the necessity of a userdefined choice of loss functions in NNs. In contrast, the deviation between stochastic processes needs to be

16
measured in terms of some quantification of the deviation of the associated finite dimensional distributions
(FDD). Thus, any notion of a loss that we use must have the property that a zero loss indicates convergent
FDDs. We quantify this loss via defining the notion of KL divergence between two PFSA, extending the wellknown information-theoretic measure of deviation of probability distributions to stochastic processes.
We show that the log-likelihood of a sequence being generated by a second PFSA converges to the sum
entropy rate of the generating PFSA and the KL divergence of the second process from the actual generator
(See Extended Data Fig. 5d-g). Performance of the GenESeSS is then measured in the term of KL divergence
between the actual and inferred processes (See Sec. and Supplementary Text Sec. VIII). It is still possible
to have different choices of the loss metric by defining functions of the KL divergence between processes.
However, they all produce qualitatively similar results.

A PPLICATION D ETAILS : DATA S OURCE , P REPROCESSING & P ERFORMANCE C OMPARISON
We demonstrate five applications of FN modeling in complex spatio-temporal phenomena: predicting rare
weather events in contiguous US, global seismic events with magnitude registering above the local third
quartile, and forecasting urban crime in Atlanta GA, Chicago IL, and Philadelphia PA. These applications,
enumerated in Tab. 1, 1) highlight the strictly superior performance of FN over LSTMs, 2) underlines the
parsimony of the FN models, and 3) provide important insights into the underlying “physics” of the system at
hand.
In each of these systems, we begin from a spatio-temporal event log, which enumerates events of interest,
along with their space-time coordinates. For example, for US weather, the log is a culmination of events
recorded in one of the
airport-based weather stations as a part of the ASOS network logging extreme
precipitation and cold/snow events. The seismic event log comes from the USGS hazards program, where we
attempt to forecast events with a magnitude which is greater than the local third quartile of all events recorded
within the past decade. For urban crime, we take a similar approach logging property crimes (consisting of
burglary, theft etc.) and violent crimes (homicide, assault, battery etc.) within a couple of city blocks. In each
application, we need to choose a spatial discretization to define our tiles which, for each event type, defines
a distinct variable that we model and make predictions on. For example, in the weather prediction problem,
we have
spatial tiles, and three event categories (precipitation, cold/snow, and severity magnitude✕ 35 ),
resulting in
variables. We eliminate some tiles which have event frequencies under
, leaving us with
variables, or time series sequences. In case of seismic events, we discretize the globe into ✍ ✂ ✍ tiles
and consider events (event magnitude ❃ average event magnitude), where the average is taken over all events
recorded in the past decade above magnitude ✿ . As before, we eliminate tiles which are not seismically active
leaving us with
variables or sequences. In case of urban crime, we follow a similar approach by covering
the city with a grid spanning a couple of city blocks, and eliminating tiles which lack sufficient number of events.
This leads to
variables in Chicago,
sequences in Atlanta and
sequences in Philadelphia. We
also need to specify a temporal quantization, which specifies how one discrete step maps to continuous time
intervals. The temporal quantization is tuned programmatically to maximize the average entropy rate of the
event streams, which results in
hour steps in case of the weather data, days for the seismic prediction,
and or days for urban crime. With the exception of the precipitation event in case of the weather modeling
problem, the event frequencies are all lower than %. We also choose how far into future we make predictions
(prediction horizon), which is chosen to be week for weather, months for seismic prediction, and
days
for urban crime (See Extended Data Tab. 1 for details).

✷✵✵✵

✺✸✶✼

✷✵✵✵
✻✵✵✵

✶✪

✸

✸

✸✾

✹✼✵
✻✶✻✺

✶ ✷

✸

✺✶✵

✶✵✸✼

✶✷

✸

✶

✶✵

✹

✸ ✼

Predictive ability of the FN framework is bench-marked against carefully tuned LSTM models 36 . The LSTM
models use input dimension equal to the number of sequences, two fully connected hidden layers with LSTM
units 37 ((No. units in the first layer, No. units in the second layer)=
❀
and
❀
), and a timedistributed dense output layer 38 , trained over
epochs. We use tensorflow.keras package 39 for LSTM
implementation with mean squared error as loss and adam as optimizer. Using cross-entropy (ce) as the loss
function instead of mean square error did not produce significant difference in performance. We train LSTMs
with the same data used for FNs, using binarized input sequences with indicating absence of events and

✶✵✵✵

✭✶✵✵✵ ✶✵✵✮
✵

✭✷✵✵✵ ✺✵✵✮

✶

17
the events of interest (See Methods: LSTM Comparison for details). We compare the achieved performance
(See Tab. 1) of FN and LSTM architectures using 1) distribution of the area under the the receiver operating
curve (AUC) for the spatial tiles in each application, 3) the precision-recall curves (PRC)

Performance Metrics
We use a flexible approach in evaluating AUC for both Fractal Net and LSTM; a positive prediction is treated
as correct if there is at least one event recorded in ✝ time steps in the target spatial tile. We also account for
the spatial variability of the exact event location in the evaluation of PRC by replacing predicted events by 2D
Gaussian densities followed by the choice of a decision threshold.

✶

More specifically, for a fixed time step t, we construct a risk map by summing 2D Gaussian densities centered
at tiles with a positive prediction. Finally, a threshold ③ is chosen so that tiles with a risk level above ③ is reported
as having a positive prediction. The standard deviation and the ③ -levels are chosen in a manner a threshold is
selected on a ROC curve.
FN significantly outperforms LSTM models in all metrics. Specifically, FN increases area under the receiver
operating characteristic curve (AUC) by ✿
for extreme weather, ✿
for seismic activity over the local third
quartile, and ✿ , ✿ , and ✿
for criminal infractions in Atlanta, Chicago, and Philadelphia, respectively.
FN boosts sensitivity at
positive predictive value by
✿
,
✿
,
✿
,
✿
, and ✿
for the
corresponding datasets (See Tab. 1). In addition to superior performance, our framework results in models with
far fewer parameters (See Extended Data Tab. 2), likely due to the learning of stochastic generators rather than
trying to encode every possible input variation 40 , leading to a superior sample complexity.

✶✼ ✼✪ ✶✵ ✵✪ ✶✷ ✸✪
✾✵✪

✶✵ ✵✪

✶✸ ✺✪
✶✻✶ ✾✪ ✶✾✶ ✸✪ ✶✺✵ ✵✪ ✹✶✽ ✻✪

✺✵ ✽✪

18
Extended Data Tab. 1
Dataset Statistics, Data Sources, and Variable Explanation
US Weather

Earthquakes

Atlanta Crime

Chicago Crime

Philadelphia Crime

temporal
res.

✶✷ hrs

✸ days

✷ days

✶ day

✶ day

spatial
res.

neighborhood of
weather-station

✸✍ ✂ ✸✍

✶✵✵✻✵ ✂ ✶✵✵✻✵

✾✺✽✵ ✂ ✶✵✵✼✵

✾✵✼✵ ✂ ✾✽✻✵

prediction
horizon

✼ days

✶✷✵ days

✻ days

✼ days

✸ days

train
period

16/01/01 to 18/12/31

09/01/01 to
19/08/21

14/01/01 to 18/12/31

14/01/01 to
16/12/31

14/01/01 to
16/12/31

test
period

19/01/01 to 19/04/30

19/08/21 to
20/08/21

19/01/01 to 19/04/10

17/01/01 to
17/04/10

17/01/01 to
17/04/10

source

https://smoosavi.org/d
atasets/lstw Original
source: https://www.we
ather.gov/asos/

https://earthquake.u
sgs.gov/

https://data.world/bry
antahb/crime-in-atlant
a-2009-2017 Original
source: http://opendata
.atlantapd.org/

https://data.cityofchi
cago.org/browse?q
=crime

https://www.openda
taphilly.org/dataset
/crime-incidents.

event description
and frequency

precipitation: Fog,
Storm, Rain ( ✿ );
winter : Snow, Cold
( ✿ ); severe
events:
.

Earthquakes of
maginitude ✿ and
higher ( ✿
).

violent crime:
homicide, assault,
battery ( ✿ );
property crime:
burglary, theft, motor
vehicle theft ( ✿ );

violent crime:
homicide,
aggravated assault
( ✿ ); property
crime: burglary,
auto theft ( ✿ ).

violent crime:
homicide, assault
( ✿ ); property
crime: burglary,
theft, motor vehicle
theft ( ✿ );

✷✽ ✸✪

✼ ✺✪

✶✵✪

✹ ✵✪

✹✵
✷ ✹✻✪

✼ ✻✪

✹ ✼✪

✻ ✾✪

✽ ✶✪

✾ ✶✪

Extended Data Tab. 2
Prediction accuracy and model parameters comparison

Fractal Net AUC
LSTM 1 AUC
LSTM 2 AUC
outperformance

mean
median
mean
median
mean
median
mean
median

Fractal Net No. parameters
Fractal Net avg. depth
LSTM 1 No. parameters
LSTM 2 No. parameters

US Weather

Earthquakes

Atlanta Crime

Chicago Crime

Philadelphia Crime

✽✷✶✶✷
✽✶✽✸✹
✼✸✺✸✻
✼✸✾✺✶
✼✹✻✻✼
✼✺✹✵✹
✶✵ ✵✪
✽ ✺✪
✹ ✽✵✵ ✻✶✽
✸✵ ✶
✷✻ ✷✻✶ ✼✷✵
✻✻ ✷✸✺ ✸✷✵

✽✷✷✹✶
✽✷✼✹✺
✼✷✹✼✾
✼✹✾✽✸
✼✷✵✵✸
✼✺✶✹✻
✶✸ ✺✪
✶✵ ✹✪
✹✸✻ ✺✺✶
✹ ✼✽
✼ ✺✾✸ ✾✻✽
✷✼ ✺✸✽ ✼✻✽

✽✼✽✹✺
✽✽✻✼✼
✼✹✻✺✽
✼✻✸✷✹
✼✷✻✷✽
✼✹✸✹✵
✶✼ ✼✪
✶✻ ✷✪
✶✵✻ ✷✺✸
✹ ✶✼
✽ ✶✽✹ ✺✶✷
✷✽ ✼✻✷ ✾✶✷

✽✻✷✸✼
✽✺✾✾✶
✼✽✵✺✶
✼✽✷✾✹
✼✽✸✼✸
✼✽✺✾✹
✶✵ ✵✪
✾ ✹✪
✸ ✷✶✶ ✹✼✽
✶✺ ✸
✷✾ ✼✷✼ ✵✻✺
✼✸ ✹✶✽ ✻✺✺

✽✹✵✾✶
✽✹✷✷✷
✼✹✽✼✵
✼✻✶✶✽
✼✸✼✽✵
✼✺✹✹✻
✶✷ ✸✪
✶✵ ✻✪
✹✹✵ ✵✵✺
✽ ✹✾
✽ ✻✾✼ ✶✸✼
✷✾ ✽✷✺ ✺✸✼

✿

✿

✿

✿

✿
✿

✿

✿

❀

❀

✿

❀

❀

❀

❀

✿

✿

✿
✿

✿
✿

✿

✿

❀

✿

❀

❀

❀

❀

✿

✿

✿
✿

✿
✿

✿

✿

❀

✿

❀

❀

❀

❀

✿

✿

✿
✿

✿
✿

✿

✿

❀

❀

✿

❀

❀

❀

❀

1. We denote an LSTM by ✭no. units in the first layer, no. units in the second layer, epochs✮.
2. We consider two LSTMs: LSTM ✶ ❂ ✭✶✵✵✵❀ ✶✵✵❀ ✶✵✵✵✮ and LSTM ✷ ❂ ✭✷✵✵✵❀ ✺✵✵❀ ✶✵✵✵✮.
3. The LSTM model having the better performance for each dataset is highlighted.
4. The outperformance is calculated as ✭Fractal Net AUC Better LSTM AUC✮❂✭Better LSTM AUC✮.

✿

✿

✿
✿

✿
✿

✿

✿

❀

✿

❀

❀

❀

❀

19

a. Minimum magnitudes used in defining

c. Correct and missed predictions for ✶✺ most significant events

target seismic events for prediction
4.2

4.6

4.4

4.8

in period 22-08-2019 to 21-08-2020

5.0

5.2
1

Richter scale

3
8

2

4

10
6
9 and 13

14

12

7

11
5

15

correctly predicted

b. Distribution of minimum magnitudes

d. Top ✶✺ events recorded between 22-08-2019 and 21-08-2020

of events targeted for prediction

time

✷✵✵

mean minimum
magnitude
Los Angeles
minimum
magnitude

count

✶✺✵
✶✵✵
✺✵
✵

✹✿✺

✺

missed

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15

2020-07-22 06:12:44
2020-01-28 19:10:24
2020-03-25 02:49:21
2020-06-23 15:29:04
2020-06-18 12:49:53
2019-11-14 16:17:40
2020-07-17 02:50:22
2020-02-13 10:33:44
2020-08-18 22:29:24
2019-12-15 06:11:51
2020-06-03 07:35:36
2020-05-06 13:53:55
2020-08-18 22:23:59
2020-07-06 22:54:47
2019-09-29 15:57:53

mag.

✼✿✽
✼✿✼
✼✿✺
✼✿✹
✼✿✹
✼✿✶
✼✿✵
✼✿✵
✻✿✾
✻✿✽
✻✿✽
✻✿✽
✻✿✽
✻✿✼
✻✿✼

location
105 km SSE of Perryville, Alaska
123km NNW of Lucea, Jamaica
221km SSE of Severo-Kuril’sk, Russia
9 km SE of Santa Marı́a Xadani, Mexico
south of the Kermadec Islands
138km E of Bitung, Indonesia
114 km NNW of Popondetta, Papua New Guinea
94km ENE of Kuril’sk, Russia
126 km WSW of Bengkulu, Indonesia
7km S of Magsaysay, Philippines
48 km SW of San Pedro de Atacama, Chile
Banda Sea
139 km WSW of Bengkulu, Indonesia
98 km N of Batang, Indonesia
69km WSW of Constitucion, Chile

✺✿✺

magnitude

Extended Data Fig. 1. Minimum magnitudes used in defining target seismic events for prediction and performance on recent
events of significance. Panel a Minimum magnitude of events considered as prediction targets for locations around the globe. Note
that the distribution of the minimum magnitudes in panel b illustrates a minimum magnitude of ✹✿✷ and a maximum of ✺✿✻✺ on the Richter
scale with an average of ✹✿✼. As a comparison, the minimum magnitude of target events near Los Angeles, USA is ✙ ✹✿✺. Panel c and
d shows recent high-magnitude events of maximum magnitude predicted correctly and missed in the out-of-sample prediction period
between August 2019 and August 2020. As shown, we correctly predict 12 out of top 15 events (10 out of top 10), and do so ✶✷✵ ✝ ✸
days in advance.

20

a.

c.

b.
✶✭✿✼✮
✵✭✿✼✮

✶✭✿✽✮

✶✭✿✸✮

✶✭✶❂✸✮

✶✭✿✸✮
✶✭✿✷✮

✵✭✿✸✮

✶✭✿✺✮

✵✭✿✷✮

✵✭✶❂✸✮
✵✭✿✽✮

✵✭✿✼✮

prediction

✶✭✿✷✮

0 1

✵✿✽

✵✿✺

✵✿✻

✵✿✹

00 01 10 11

✵✿✹

✵✿✹

✵✭✷❂✸✮

✶✭✿✸✮

✵✭✿✸✮

✶✭✿✼✮

✵✿✻

d.

✵✭✿✺✮

✵✭✿✽✮

✶✭✷❂✸✮

✵✭✿✼✮

q r s

✵✿✻

✵✿✺

✵✿✸

✵✿✷
✵

✺✵✵

✶❀✵✵✵

✵

✺✵✵

✶❀✵✵✵

✵

✺✵✵

✶❀✵✵✵

✵

✺✵✵

✶❀✵✵✵

sequence length

Extended Data Fig. 2. Neural nets need finite Markov order to succeed We generate ✶✵✵ sequences of length ✺✵✵✵ from each
of the four stochastic processes generated by the models in the top row (See Examples of PFSA in Supplementary Text Sec. II). We
train LSTM models 41,42 using the tensorFlow.keras package 39 with ✺✵ hidden units, sigmoid function for activation, mean squared error
(MSE) as loss function, ✶✵✵ training epochs with batch size ✸✷. Given our loss function, the LSTM model should learn to output the
probability of producing ✶ as the next output symbol. In the bottom row, we show the scatter plots of probability of ✶-predictions of LSTM
models vs input length. We color-code the dots in the scatter plots for the two processes of finite Markov order (Panel a and b), and the
one generated by the three-state model (Panel c). If we know the current input leads to a certain state, we color the next output with
the color of the state. The process in panel d has no finite Markov order and its generating model is not synchronizable. The predictions
show that the LSTM fails to uncover the ✶-probability distribution.

21

No Finite Markov Order

Finite Markov Order
B. Prepresentation Limits of Model

Th. 2:
Finite set of
causal states
PFSA
generator

✮

A. Process
Generation

Def. 15:
Persistent
causal states

Def. 19:
Accumulation
measures

Th. 5:
Finite set of
persistent
states
PFSA
generator

Th. 7:
Finite set of
atomic
accumulation
measures
PFSA
generator

✮

C. Learnability

Th. 1:
PFSA
generates
stationary
ergodic
processes

Th. 10:
All PFSA are
epsilon
synchronizable

Def. 5:
causal
states

Def. 27:
Epsilon
Synchronization

✮

C. Algorithm
Performance
TH 11:
Uniform
epsilon
synchronization

Alg 2:
Self-similar
compression
(GenESeSS)

Th. 17:
KL divergence
of stochastic
processes

Th. 21:
Sample
complexity
bound

Th. 22 & 23:
Performance
bounds

Extended Data Fig. 3. Schematic Map of Theoretical Development. The mathematical development detailed in the Supplementary
text comes together as shown above to establish correctness of the inference algorithms, and performance and complexity bounds.

22

Algorithm 1: Fractal Net
Data:
✎ a set of sequence ❢①✐ ✐
❀ ✿ ✿ ✿ ❀ ◆ ❣ of length ♥;
✎ a hyperparameter ❁ ✧ ❁ ;
✎ a model inference length ♥✵ ❁ ♥;
✎ a maximal delay max ;
✎ a threshold coefficient of causal dependence ✌✵ for admissible models;
Result: A set of XPFSA models and a set of scalar weights for each target r ✷ ❢ ❀ ✿ ✿ ✿ ❀ ◆ ❣.
/* Infer models
1 Let ▼r
❀ be the set of admissible models for each target r ✷ ❢ ❀ ✿ ✿ ✿ ❀ ◆ ❣;
2 for each delay
❀ ✿ ✿ ✿ ❀ max do
3
for each source s
❀ ✿ ✿ ✿ ❀ ◆ and target r
❀ ✿ ✿ ✿ ❀ ◆ do
♥✵
✁
4
Let ①in
①s ✶
;
✵
5
Let ①out
①r ♥✁✰✶
;
6
Calculate PFSA ● GenESeSS ①in ❀ ✧ ;
7
Calculate XPFSA ❍r❀s ✁ xGenESeSS ①out ❀ ✧ ;
8
Let ✌r❀s ✁ coefCausalDependence ●❀ ❍r❀s ✁ ;
9
if ✌r❀s ✁ ✕ ✌✵ then
♦
♥
10
Let ▼r ▼r ❬ ❍r❀s ✁ ;
/* Learn scalar weights
11 for each target r
❀ ✿ ✿ ✿ ❀ ◆ do
♦
♥
12
Let ■r
s❀
there is a model ❍r❀s ✁ ✷ ▼r ;
13
for each timestamp t
❀ ✿ ✿ ✿ ❀ ♥ ♥✵ do
14
Let xt be a vector with index set ■r ;
15
for each pair s❀
✷ ■r do
16
Let ①in the length ❧ sub-sequence of✏ ①s that ends
-th entry;
✑ in the ♥✵ t
s
17
Let the entry of xt s❀
predict ❍r❀✁ ❀ ①in ;
18
Let ②t ①r ♥✵ t ;
19
Let ❳ the matrix with the t-th row being xt ;
20
Let y be the vector with the t-th entry being ②t ;
21
Initialize a suitable regressor
✏ Reg;
✑
s
22
Get scalar weights wr
✇r❀
Reg ❳❀ y ;
✁

✵
✁

✿ ❂✶
✶

✶

❂

✁❂✶

❂✭ ✮
❂✭ ✮

❂✶

✶

✁

❂

❂

*/

❂✶

✭

❂

✭

✮
✭

✮
✮

❂

❂✶
❂ ✭ ✁✮ ✿

❂✶
✭ ✁✮

✭ ✰

❬ ✁❪ ❂
❂ ❬ ✰❪
❂

23 return

❢✭▼ ❀ w ✮ ✿ r ❂ ✶❀ ✿ ✿ ✿ ❀ ◆ ❣;
r

r

✭ ✁✮✷ r ❂
s❀

■

✭

✮

✁✮

*/

23

Algorithm 2: GenESeSS
Data: A sequence ① over alphabet ✝, ✵ ❁ ✧ ❁ ✶
❡
Result: State set ◗, transition map ✍ , and transition probability ✙
✧
-synchronizing
sequence
*/
/* Step❧ One: Approximate
♠
1 Let ▲ ❂ ❧♦❣❥✝❥ ✶❂✧ ;
♥
♦
❫①② ✿ ② is a sub-sequence of ① with ❥②❥ ✔ ▲ ;
2 Calculate the derivative heap ❉✧① equaling ✣
3 Let ❈ be the convex hull of ❉✧① ;
❫①①✵ being a vertex of ❈ and has the highest frequency in ①;
4 Select ①✵ with ✣
/* Step Two: Identify transition structure
*/
5 Initialize ◗ ❂ ❢q✵ ❣;
❫①
6 Associate to q✵ the sequence identifier ①id
q✵ ❂ ①✵ and the probability vector ❞q✵ ❂ ✣①✵ ;
❡ be the set of states that are just added and initialize it to be ◗;
7 Let ◗
❡ , ❀ do
8 while ◗
9
Let ◗new ❂ ❀ be the set of new states;
❡ ✂ ✝ do
10
for ✭q❀ ✛ ✮ ✷ ◗
❫①
11
Let ① ❂ ①id
q and ❞ ❂ ✣①✛ ;
12
if ❦❞ ❞q ❦✶ ❁ ✧ for some q ✵ ✷ ◗ then
13
Let ✍ ✭q❀ ✛ ✮ ❂ q ✵ ;
14
else
15
Let ◗new ❂ ◗new ❬ ❢qnew ❣ and ◗ ❂ ◗ ❬ ❢qnew ❣;
16
Associate to qnew the sequence identifier ①id
qnew ❂ ①✛ and the probability vector ❞qnew ❂ ❞;
17
Let ✍ ✭q❀ ✛ ✮ ❂ qnew ;
❡ ❂ ◗new ;
18
Let ◗
19 Take a strongly connected subgraph of the labeled directed graph defined by ◗ and ✍ , and denote the
vertex set of the subgraph again by ◗;
*/
/* Step Three: Identify transition probability
20 Initialize counter ◆ ❬q❀ ✛ ❪ for each pair ✭q❀ ✛ ✮ ✷ ◗ ✂ ✝;
21 Choose a random starting state q ✷ ◗;
22 for ✛ ✷ ① do
23
Let ◆ ❬q❀ ✛ ❪ ❂ ◆ ❬q❀ ✛ ❪ ✰ ✶;
24
Let q ❂ ✍ ✭q❀ ✛ ✮;

❡ ✭q ✮ ❂ ✭◆ ❬q❀ ✛ ❪✮✛✷✝ ;
25 Let ✙
❡;
26 return ◗, ✍ , ✙
✵

24

Algorithm 3: xGenESeSS
Data: A sequence ①in over alphabet ✝in , a sequence ①out over alphabet ✝out , and ✵ ❁ ✧ ❁ ✶
Result: State set ❘, transition map ✑ , and output probability ✤
/* Step❧ One: Approximate
✧-synchronizing sequence
*/
♠
1 Let ▲ ❂ ❧♦❣❥✝in ❥ ✶❂✧ ;
♥
♦
① ❀①
①in ❀①out
2 Calculate cross derivative heap ❉✧
equaling ✣❫② in out ✿ ② is a sub-sequence of ①in with ❥② ❥ ✔ ▲ ;
①in ❀①out
3 Let ❈ be the convex hull ❉✧
;
❫①①in✵ ❀①out being a vertex of ❈ and has the highest frequency in ①;
4 Select ①✵ with ✣
/* Step Two: Identify transition structure
*/
5 Initialize ❘ ❂ ❢r✵ ❣;
❫①in ❀①out ;
6 Associate to r✵ the sequence identifier ①id
r✵ ❂ ①✵ and the probability vector ✤ ✭r✵ ✮ ❂ ✣①✵
❡ be the set of states that are just added and initialize it to be ❘;
7 Let ❘
❡ , ❀ do
8 while ❘
9
Let ❘new ❂ ❀ be the set of new states;
❡ ✂ ✝in do
10
for ✭r❀ ✛ ✮ ✷ ❘
❫①in ❀①out ;
11
Let ① ❂ ①id
r and ❞ ❂ ✣①✛
12
if ❦❞ ✤ ✭r✵ ✮❦✶ ❁ ✧ for some r✵ ✷ ❘ then
13
Let ✑ ✭r❀ ✛ ✮ ❂ r✵ ;
14
else
15
Let ❘new ❂ ❘new ❬ ❢rnew ❣ and ❘ ❂ ❘ ❬ ❢rnew ❣;
16
Associate to rnew the sequence identifier ①id
rnew ❂ ①✛ and the probability vector ✤ ✭rnew ✮ ❂ ❞;
17
Let ✑ ✭r❀ ✛ ✮ ❂ rnew ;
❡ ❂ ❘new ;
18
Let ❘
19 Take a strongly connected subgraph of the labeled directed graph defined by ❘ and ✑ , and denote the
vertex set of the subgraph again by ❘;
/* Step Three: Identify output probability
*/
20 Initialize counter ◆ ❬r❀ ✜ ❪ for each pair ✭r❀ ✜ ✮ ✷ ❘ ✂ ✝out ;
21 Choose a random starting state r ✷ ❘;
22 for ✐ ✷ ✶❀ ✿ ✿ ✿ ❀ ❥①in ❥ do
23
Let ✛✐ be the ✐-th symbol in ①in and ✜✐ be the ✐-th symbol in ①out ;
24
Let ◆ ❬r❀ ✜✐ ❪ ❂ ◆ ❬r❀ ✜✐ ❪ ✰ ✶;
25
Let r ❂ ✑ ✭r❀ ✛✐ ✮;

;
26 Let ✤ ✭r ✮ ❂ ✭◆ ❬r❀ ✜ ❪✮✜ ✷✝
out
27 return ❘, ✑ , ✤;

25

Extended Data Tab. 3
Causality table of the process in Example 1

① ✷ ✝❄
✕

✵
✶
✵✵
✵✶
✶✵
✶✶
✵✵✵
✵✵✶
✵✶✵
✵✶✶
✶✵✵
✶✵✶
✶✶✵
✶✶✶
✿✿
✿

✖ ✭①✝✦ ✮

✶
✿✺
✿✺
✿✸
✿✷
✿✷
✿✸
✿✶✽
✿✶✷
✿✵✽
✿✶✷
✿✶✷
✿✵✽
✿✶✷
✿✶✽
✿✿
✿

✣①
✭✿✺❀ ✿✺✮
✭✿✻❀ ✿✹✮
✭✿✹❀ ✿✻✮
✭✿✻❀ ✿✹✮
✭✿✹❀ ✿✻✮
✭✿✻❀ ✿✹✮
✭✿✹❀ ✿✻✮
✭✿✻❀ ✿✹✮
✭✿✹❀ ✿✻✮
✭✿✻❀ ✿✹✮
✭✿✹❀ ✿✻✮
✭✿✻❀ ✿✹✮
✭✿✹❀ ✿✻✮
✭✿✻❀ ✿✹✮
✭✿✹❀ ✿✻✮
✿✿
✿

causal state

q✕
q✵
q✶
q✵
q✶
q✵
q✶
q✵
q✶
q✵
q✶
q✵
q✶
q✵
q✶
✿✿
✿

Extended Data Tab. 4
Causality table of the process in Example 3

① ✷ ✝❄
✕

✵
✶
✵✵
✵✶
✶✵
✶✶
✵✵✵
✵✵✶
✵✶✵
✵✶✶
✶✵✵
✶✵✶
✶✶✵
✶✶✶
✿✿
✿

✖ ✭①✝✦ ✮

✶
✶ ❂✷
✶ ❂✷
✹❂✶✺
✼❂✸✵
✼❂✸✵
✹❂✶✺
✷❂✷✺
✶✹❂✼✺
✼❂✶✺✵
✶✹❂✼✺
✶✹❂✼✺
✼❂✶✺✵
✶✹❂✼✺
✷❂✷✺
✿✿
✿

✣①

✭✶❂✷❀ ✶❂✷✮
✭✽❂✶✺❀ ✼❂✶✺✮
✭✼❂✶✺❀ ✽❂✶✺✮
✭✸❂✶✵❀ ✼❂✶✵✮
✭✶❂✺❀ ✹❂✺✮
✭✹❂✺❀ ✶❂✺✮
✭✼❂✶✵❀ ✸❂✶✵✮
✭✸❂✶✵❀ ✼❂✶✵✮
✭✶❂✺❀ ✹❂✺✮
✭✹❂✺❀ ✶❂✺✮
✭✼❂✶✵❀ ✸❂✶✵✮
✸❂✶✵❀ ✼❂✶✵
✭✶❂✺❀ ✹❂✺✮
✭✹❂✺❀ ✶❂✺✮
✭✼❂✶✵❀ ✸❂✶✵✮
✿✿
✿

causal state

q✕
q✵
q✶
q✵✵
q✵✶
q✶✵
q✶✶
q✵✵
q✵✶
q✶✵
q✶✶
q✵✵
q✵✶
q✶✵
q✶✶
✿✿
✿

26

a.

g.

b.
✵✭✿✹✮

✶✭✿✼✮

✶✭✿✻✮

✶✭✿✽✮
✶✭✿✸✮

✶✭✿✷✮

✵✭✿✻✮

✶✭✿✹✮

✵✭✿✷✮

✵✭✿✸✮
✵✭✿✽✮

✵✭✿✺✮

c.

d.

✶✭✿✺✮

✵✭✿✼✮
✶✭✶❂✸✮

✵✭✷❂✸✮

✶✭✿✸✮
✵✭✶❂✸✮
✵✭✿✽✮

✶✭✿✷✮

✵✭✿✼✮

e.

f.
✵✭✿✹✮

✵✭✿✻✮

✶✭✷❂✸✮

✶✭✿✻✮

q✵

✽
✵ ✶✺

q✶

✁

✼
✶ ✶✺

q✵

✶✭✿✼✮

✵✭✿✺✮

✁

q

✶✭✿✺✮

✶✭✿✽✮

q✵✶

h.

✕

✶✭✿✸✮
✹
q✵✵

✶✭✿✹✮

✵✭✿✺✮

q

✶✭✿✺✮

✶✭✿✷✮

✵✭✿✷✮

q✶✶

✽
✶ ✶✺

✵✭✿✸✮

✕

✵✭✿✽✮

q✶✵

✸

✷

✶

✵

✶

✷

✸

✹

✺

✻

✁

✵✭✿✼✮

✼
✵ ✶✺

✁

q✶

i.

j.
✿✸

✿✸

✿✹

❛

❜

❝

r✶

✶
r✵

✵

✶
✶

✿✸

✿✺

❛

❜

❝

r✸

✵

✵
✿✷

✵✭✿✻✮

✵✭✿✻✮

✵

✿✺

✿✷

✿✸

❛

❜

❝

✶

✿✸

✿✺

✿✷

❛

❜

❝

✵✭✿✻✮
✭ q✵ ❀ r ✵ ✮

✿✷

✿✸

✿✺

❛

❜

❝

✭ q✵ ❀ r ✶ ✮

✭ q✵ ❀ r ✷ ✮

✵✭✿✹✮
✵✭✿✹✮

✵✭✿✹✮

✭ q✶ ❀ r ✶ ✮
✶✭✿✻✮

r✷

✭ q✶ ❀ r ✷ ✮

✿✺

✿✷

✿✸

✿✸

✿✹

❛

❜

❝

❛

❜

❝

✶✭✿✹✮

✿✺

✿✷

✿✸

❛

❜

❝

✭ q✶ ❀ r ✸ ✮

✶✭✿✻✮
✶✭✿✻✮

✿✸

✭ q✵ ❀ r ✸ ✮

✵✭✿✹✮
✶✭✿✹✮
✶✭✿✹✮

✶✭✿✹✮

✭ q✶ ❀ r ✵ ✮

✵✭✿✻✮

✶✭✿✻✮

Extended Data Fig. 4. Examples of PFSA in Supplementary Text Sec. II and in Supplementary Text Sec. VII. Panel a: an ▼ ✷
PFSA. The PFSA generates a Markov process, which gives rise to the labeled directed graph in Panel e by subtree stitching. We note
that the graph is not strongly connected since the causal state q✕ has no in-coming edge. The unique strongly connected component
of the graph, ✐✿❡✿, the induced subgraph on q✵ and q✶ , is exactly the generating ▼ ✷ PFSA. See Supplementary Text Example 1 for
detail. Panel b: an ▼ ✹ PFSA. The PFSA generates a process of Markov order ✷, which gives rise to the labeled directed graph in
Panel f by subtree stitching. We note that the graph is not strong connected, since the causal states q✕ , q✵ , and q✶ have no in-coming
edge. The unique strongly connected component, ✐✿❡✿, the induced subgraph on q✐❥ , ✐❀ ❥ ✷ ❢✵❀ ✶❣. is exactly the generating ▼ ✹ PFSA.
See Supplementary Text Example 3 for detail. Panel c: a synchronizable ✸-state PFSA discussed in Supplementary Text Example 4.
The shortest synchronizing sequence of the PFSA is ✶✶. Part of the binary tree given rise by the process generated by the PFSA
is demonstrated in Panel g. The nodes in the tree are sequences, with the root being the empty sequence. The darker nodes in the
tree represent sequences containing ✶✶ and hence are synchronizing. There are higher fraction of synchronizing nodes with longer
sequences. Panel d: a non-synchronizable ❙ PFSA discussed in Supplementary Text Example 5. The labeled directed graph obtained
by subtree stitching is an infinite graph,✁ and we demonstrate part of the graph in Panel f. Thgge node labeled by ♥ represents the causal
♥✰✶ ✰ ✶❀ ✿✺♥ ✰ ✿✺ in Supplementary Text Eq. (41). Panel i: Example of an XPFSA with four states. The bar charts
state ❬①❪ with ✣① ✘
❴ ✿✺
show the output probability vectors ✤✭r✐ ✮, ✐ ❂ ✵❀ ✶❀ ✷❀ ✸. For example, at state r✵ , the probability of getting symbol ❛, ❜, and ❝ as output is
✿✷, ✿✸, and ✿✺, respectively. We note that an XPFSA doesn’t have a transition probability map as a PFSA does. Panel j: the synchronous
composition of the ▼ ✷ PFSA in Fig. 4a to the XPFSA in Panel a. We show the composition over ❢q✵ ❀ q✶ ❣ ✂ ❢r✵ ❀ r✶ ❀ r✷ ❀ r✸ ❣ but highlight
only the strongly connected component that is kept for the synchronous composition.

27

a.
✵✿✻
✵✿✹

♣❞ ✭q♥ ✮

♣❞ ✭❬✶✶✵✶❪✮
♣❞ ✭❬✶✶✵❪✮
♣❞ ✭❬✶✶❪✮

✵✿✽

frequency

b.
✵✿✵✻

✵✿✷
✵

❞ ❂ ✶✵✵
❞ ❂ ✸✵✵

✵✿✵✹

❞ ❂ ✷✵✵
❞ ❂ ✹✵✵

✵✿✵✷
✵

✵

✶✵

✷✵

✹✵✵

✷✵✵

sequence length

d.
log-likelihood

c.
✶

cumulative density
of ✣① ✭✵✮

✶

✵✿✾✽

▲✭● ✦ ①❀ ●✮
❍✭●✮
✵

✺✵✵

♥

✶❀✵✵✵

✵✿✾

✺✵✵

✶❂✸
✵

✹✵✵

✶❂✸

✷❂✸ ✶❂✸

✷❂✸

✣① ✭✵✮

g.

✶✿✹
✶
✶✿✷

▲✭● ✦ ①❀ ❍ ✮ ✵✿✾✽
❍✭●✮ ✰
❉❑▲ ✭● ❦ ❍ ✮ ✵✿✾✻
✺✵✵
✶❀✵✵✵

✵✿✽
✵

❞ ❂ ✹✵

f.

▲✭❍ ✦ ①❀ ❍ ✮
❍ ✭❍ ✮

✶

✵✿✾✹

✷✵✵

e.

✶

✵✿✾✻

✵

❞ ❂ ✷✵

✶❀✵✵✵

✶
✵

▲✭❍ ✦ ①❀ ●✮
❍ ✭❍ ✮ ✰
❉❑▲ ✭❍ ❦ ● ✮
✺✵✵
✶❀✵✵✵

✵

sequence length

Extended Data Fig. 5. Examples in Supplementary Text Sec. III and example 11 in Supplementary Text Sec. VI Panel a: Sum
of probabilities of causal states ❬✶✶❪, ❬✶✶✵❪, and ❬✶✶✵✶❪ for sequence length ❞ ❂ ✵❀ ✶❀ ✿ ✿ ✿ ❀ ✷✺ as discussed in Example 6. The sum of
probabilities of sequences synchronzing to the three causal states approaches ✶ as ❞ increases. Hence, although the process has
infinitely many causal states, it is generated by a PFSA. Panel b: ♣❞ ✭q♥ ✮ vs ♥ for sequence length ❞ ❂ ✶✵✵❀ ✷✵✵❀ ✸✵✵❀ ✹✵✵ as discussed
in Example 7. The curves keep on flattening with increasing ❞, which implies that no causal state q♥ is persistent. The cumulative
probability density functions
✟ of ✣① ✭✵✮ with✠sequence lengths ❞ ❂ ✷✵✟❀ ✹✵ is demonstrated ✠in Panel c for this process. For each fixed ❞, the
abscissa is a value ❤ ✷ ✣① ✭✵✮ ✿ ① ✷ ✝❞ , and the ordinate is ♣❞ ① ✷ ✝❞ ✿ ✣① ✭✵✮ ✔ ❤ . The curves approaches a step function as ❞
increases, which implies the set of causal states has two cumulation points ✖✶ and ✖✷ with ✖✶✶ ❂ ✭✶❂✸❀ ✷❂✸✮ and ✖✶✷ ❂ ✭✷❂✸❀ ✶❂✸✮. The two
accumulation points correspond to q✶ and q ✶ as in Eq. (60). Panel d-g: examples of log-likelihood convergence to the sum of entropy
rate and KL divergence. The horizontal line in each plot shows the limit the log-likelihood should approach to as length of sequence
increases.

a.

b.

c.

d.

e.

✵

❢✣✵✺ ① ✿ ❥①❥ ❂ ✸❣

❢✣① ✿ ❥①❥ ❂ ✸❣

q✵

✣① ✭✶✮

✶

✶

q✸

❢✣✵✺ ① ✿ ❥①❥ ❂ ✾❣

❢✣① ✿ ❥①❥ ❂ ✾❣

✵

q✵

✵

✶

✵

f.✿

r

✶✭✿✷✮

✶

q✸

✷✭✿✹✮
✷✭✿✸✮

q✶

✵

q
✷✭✿✺✮

✶

q✷

q✷

✶✭✿✹✮

✣① ✭✵✮

q✶
✵

✵✭ ✷✮

✵

✵✭✿✸✮

✶

✵

q✶

q✹

g.

q✵

✶

✶

q✹

✵

✶

q✸

q✵

✵

✶

q✶

q✸

✶✭✿✷✮

s

✵✭✿✺✮

Extended Data Fig. 6. Examples in Supplementary Text Sec. VIII For the non-synchronizable ✸-state ✸-symbol PFSA ● in Panel f,
and for sequence length ❞ ❂ ✸ and ✾, we show in Panel a the scatter plots of ❢✣① ✭✵❀ ✶✮ ✿ ❥①❥ ❂ ❞❣, in Panel b the density plots of the
previous set with the weight of the point ✣① ✭✵❀ ✶✮ being ♣● ✭①✮, in Panel c the scatter plots of ❢✣✵✺ ① ✭✵❀ ✶✮ ✿ ❥①❥ ❂ ❞❣, and in Panel d the
density plots of the previous set with the weight of the point ✣✵✺ ① ✭✵❀ ✶✮ being ♣● ✭①❥✵✺ ✮. Panel e is a PFSA with ✺ states and over binary
alphabet, and Panel g is a running tree of GenESeSS in case ①✵ find in Extended Data Algorithm 2 line 4 is a synchronizing sequence to
state q✵ . A new state is colored orange, and a repeated state is colored gray.

Figures

Figure 1
Snapshots of Spatio-temporal Rare Event Prediction. Panels a-e illustrate forecasts in diverse systems
using Fractal Nets, each with distinct spatio-temporal quantization and event de nitions (See Extended
Data Tab. 1 and 2).

Figure 2
Fractal Structures in Stochastic processes and Self-Similar Compression.

Figure 3
Fractal Net Organization.

Figure 4
Dynamical Properties Revealed by the Coe cient of Causality γ.

Supplementary Files
This is a list of supplementary les associated with this preprint. Click to download.
SI.pdf
