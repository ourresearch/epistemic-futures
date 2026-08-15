---
title: "Precise Event-level Prediction of Urban Crime Reveals Signature of Enforcement Bias"
person: james-evans
section: by
type: journal-article
year: 2021
date: 2021-02-11
venue: "Research Square"
authors: "Victor Rotaru, Yi Huang, Timmy Li, James Evans, Ishanu Chattopadhyay"
source_url: https://doi.org/10.21203/rs.3.rs-192156/v1
openalex_id: https://openalex.org/W3129875167
retrieved: 2026-08-13
content: full-text
notes: "preprint version; full text extracted from an open-access copy hosted at a repository or publisher OA location (OSTI, Zenodo, ACL Anthology, DSpace, OSF, IEEE, ResearchSquare or similar)"
---

# Precise Event-level Prediction of Urban Crime Reveals Signature of Enforcement Bias

## Full text

Precise Event-level Prediction of Urban Crime
Reveals Signature of Enforcement Bias
Victor Rotaru
University Of Chicago
Yi Huang
University Of Chicago
Timmy Li
University Of Chicago
James Evans
University of Chicago and Santa Fe Institute https://orcid.org/0000-0001-9838-0707
Ishanu Chattopadhyay (  ishanu@uchicago.edu )
University of Chicago

Article
Keywords: enforcement bias, urban crime, crime rate
Posted Date: February 11th, 2021
DOI: https://doi.org/10.21203/rs.3.rs-192156/v1
License:   This work is licensed under a Creative Commons Attribution 4.0 International License.
Read Full License
Version of Record: A version of this preprint was published at Nature Human Behaviour on June 30th,
2022. See the published version at https://doi.org/10.1038/s41562-022-01372-0.

1

1

2

Precise Event-level Prediction of Urban Crime
Reveals Signature of Enforcement Bias
Victor Rotaru✶❀✸ , Yi Huang✶ , Timmy Li✶❀✸ , James Evans✷❀✺❀✻ and Ishanu Chattopadhyay,✶❀✹❀✺⋆

3

✶ Department of Medicine, University of Chicago, Chicago, IL 60637, USA

4

✷ Department of Sociology, University of Chicago, Chicago, IL 60637, USA

5

✸ Department of Computer Science, University of Chicago, Chicago, IL 60637, USA

6
7

✹ Committee on Quantitative Methods in Social, Behavioral, and Health Sciences, University of Chicago,

Chicago, IL 60637, USA

8
9

✺ Committee on Genetics, Genomics & Systems Biology, University of Chicago, Chicago, IL 60637, USA
✻ Santa Fe Institute, Santa Fe NM 87501, USA

10

⋆

11

12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31

32
33
34
35
36
37
38
39
40
41
42

43
44
45
46
47
48

To whom correspondence should be addressed: e-mail: ishanu@uchicago.edu.

Policing efforts to thwart urban crime often rely on detailed reports of criminal infractions. However,
crime rates do not document the distribution of crime in isolation, but rather its complex relationship
with policing and society. Several results attempting to predict future crime now exist, with varying
degrees of predictive efficacy. However, the very idea of predictive policing has stirred controversy,
with the algorithms being largely black boxes producing little to no insight into the social system
of crime, and its rules of organization. The issue of how enforcement interacts with, modulates, and
reinforces crime has been rarely addressed in the context of precise event predictions. In this study,
we demonstrate that while predictive tools have often been designed to enhance state power through
surveillance, they also enable the tracing of systemic biases in urban enforcement—surveillance of
the state. We introduce a novel stochastic inference algorithm as a new forecasting approach that
learns spatio-temporal dependencies from individual event reports with demonstrated performance far
surpassing past results (e.g., average AUC of ✙
in the City of Chicago for property and violent
crimes predicted a week in advance within spatial tiles ✙
ft across). These precise predictions enable
equally precise evaluation of inequities in law enforcement, discovering that response to increased crime
rates is biased by the socio-economic status of neighborhoods, draining policy resources to wealthy
areas with disproportionately negative impacts for the inner city, as demonstrated in Chicago and six
other major U.S. metropolitan areas. While the emergence of powerful predictive tools raise concerns
regarding the unprecedented power they place in the hands of over-zealous states in the name of civilian
protection, our approach demonstrates how sophisticated algorithms enable us to audit enforcement
biases, and hold states accountable in ways previously inconceivable.

✾✵✪

✶✵✵✵

T

HE emergence of large-scale data and ubiquitous data-driven modeling has sparked widespread government
interest in the possibility of predictive policing 1–5 : predicting crime before it happens to enable anticipatory
enforcement. Such efforts, however, do not document the distribution of crime in isolation, but rather its complex
relationship with policing and society. In this study, we reconceptualize the process of crime prediction, build
novel methods to improve it, and use it to diagnose both the distribution of reported crime and biases in its
enforcement. The history of statistics has co-evolved with the history of criminal prediction, but also with the
history of enforcement critique. Siméon Poisson published the Poisson distribution and his theory of probability
in an analysis of the number of wrongful convictions in a given country 6 . Andrey Markov introduced Markov
processes to show that dependencies between outcomes could still obey the central limit theorem to counter
Pavel Nekrasov’s argument that because Russian crime reports obeyed the law of large numbers, “decisions
made by criminals to commit crimes must all be independent acts of free will” 7 .
In this study, we conceptualize the prediction of criminal reports as that of modeling and predicting a system of
spatio-temporal point processes unfolding in social context. We report a fundamentally new approach to predict
urban crime at the level of individual events, with predictive accuracy far greater than has been achieved in
past. Rather than simply increasing the power of states by predicting the when and where of anticipated crime,
our new tools allow us to audit them for enforcement biases, and garner deep insight into the nature of the
dynamical processes through which policing and crime co-evolve in urban spaces.

58

Classical investigations into the mechanics of crime 8–10 have recently given way to event-level crime predictions
that have enticed police forces to deploy them preemptively and stage interventions targeted at lowering crime
rates. These efforts have generated multi-variate models of time-invariant hotspots 11–13 , and estimate both long
and short term dynamic risks 1–3 . One of the earliest approaches to predictive policing is based on the use
of epidemic-type aftershock sequences (ETAS) 4,5 , originally developed to model seismic phenomena. While
these approaches have suggested the possibility of predictive policing, many achieve only limited out-of-sample
performance 4,5 . More recently, deep learning architectures have yielded better results 14 . Machine learning
systems, however, are often black boxes producing little insight regarding the social system of crime and its
rules of organization. Moreover, the issue of how enforcement interacts with, modulates and reinforces crime
has been rarely addressed in the context of precise event predictions.

59

R ESULTS AND D ISCUSSION

49
50
51
52
53
54
55
56
57

60
61
62
63
64
65
66
67
68

69
70
71
72
73
74
75

76
77
78
79
80
81
82
83
84
85

86
87
88
89
90
91
92
93
94
95
96
97
98
99

100
101
102

Here we show that urban crime may be predicted reliably one or more weeks in advance, enabling modelbased simulations that reveal both the pattern of reported infractions and the pattern of corresponding police
enforcement. We learn from recorded historical event logs, and validate on events in the following year beyond
those in the training sample. Using incidence data from the City of Chicago, our novel spatio-temporal network
inference algorithm infers patterns of past event occurrences, and constructs a communicating network (the
Granger Network) of local estimators to predict future infractions. In this study, we consider two broad categories
of reported criminal infractions: violent crimes consisting of homicides, assault, and battery, and property crimes
consisting of burglary, theft and motor-vehicle thefts. The number of individuals arrested during each recorded
event is separately modeled and allows us to investigate the possibility and pattern of enforcement bias.
We begin by processing event logs to obtain time-series of relevant events, stratified by location and discretized
by time, yielding sequential event streams for 1) violent crime (✈ ), 2) property crime (✉) and 3) number of
arrests (✇), as shown in Fig. 1, panels a, b and c. To infer the structure of the Granger Net, we learn a finite
state probabilistic transducer 15,16 for each possible source-target pair s❀ r and time lag
(Fig. 1d), yielding
✙ ✿ billion modeled associations. Following the notion of Granger causality 17 , links in the network are retained
as they predict events at the target better than the target can predict itself. More details on the on problem
characteristics and performance are provided in Tab. I and II respectively.

✁

✷✻

For Chicago, we make predictions separately for violent and property crimes, individually within spatial tiles
roughly
❢ t across and time windows of
day approximately a week in advance with AUCs ranging from
across the city. We summarize our prediction results in Fig. 2, where panels a and b illustrate the
geospatial scatter of AUC obtained for different spatial tiles and types of crime, and c shows the distribution of
AUCs achieved. Out-of-sample predictive performance remains stable over time; our predictions on successive
years (each time using three preceding years for training, and one year for out-of-sample test, see Fig. 8 shows
little variation in average AUC. Inspecting excerpts of the average daily crime rate for successive years also
shows close match between actual and predicted behavior (See Fig. 9, panels a, c and e.) The remaining
panels (b, d and f) in the same figure illustrate how the Fourier coefficients match up, showing that we are able
to capture periodicities at the weekly and bi-weekly scales, and beyond.

✶✵✵✵
✽✵ ✾✾✪

✶

Unlike previous efforts 1–5 , we do not impose pre-defined spatial constraints. In contrast to contiguous diffusion
phenomena encountered in physical systems, crime may spread across the complex landscape of a modern
city unevenly, with regions hyperlinked by transportation networks, socio-demographic similarity, or historical
collocation. Rather than assuming that events far off across the city will have a weaker influence compared with
those physically near in space or time, we probe the topological structure emergent in the inferred dependencies
to estimate the shape, size and organization of neighborhoods that best predict events at each location. The
results illustrated in Fig. 2d and e show that the situation is complex with the locally predictive neighborhoods
varying widely in geometry and size, implying that restricting analysis to relatively small local communities
within the city is sub-optimal for crime prediction and enforcement analysis. In order to analyze if the effect of
reported criminal infractions diffuse outward in space and time, we simply calculate temporal-spatial distances
of influences, then average across all neighborhoods in the city, revealing the rapid decay with time delay in
diffusion rates shown in Fig. 2f. Interestingly we find the property and violent crimes differ in their rates of
influence diffusion (Fig. 2f); while the effect of property crimes decays rapidly in days, violent reported events
shape the dynamics for weeks to come.
Forecasting crime via analyzing historical patterns has been attempted before 18,19 . These approaches use state
of the art machine deep learning tools based on recurrent and convolutional neural networks (NN). In the first
article 18 , the authors train a NN model to predict next-day events for ❀
sample points in Chicago. The

✻✵ ✸✹✽

a. Violent Crimes including

c. Spatio-temporal Modeling Approach Using

b. Property Crimes including

Assaults, Battery & Homicides
(April 1-15, 2017)

✙ 1000 ft across

Daily Event Counts & Spatial Tiles

Thefts & Burglaries
(April 1-15, 2017)

00
0

ft

r

✙1
r

s

0
0.85, 0.15

q✷

✁❂✷

q✶

✁ ❂ ✸✵
Influence from
violent crimes

s’

s✵

✵

r

Infer
Linear
Combination

s

0.84, 0.16

0.89, 0.11

✶
✁❂✶
✁ ❂ ✷✻

s”

0

✁❂✸

✁❂✷

✹

1

0

1

q✸

1

q✵

Negative influence
shown dotted

Step 2.

0.58, 0.42
0,1

Step 1.

H❀ ✦
H✵ ❀ ✦ ✵

r

H✵✵ ❀ ✦ ✵✵

s✵✵

Infer
Local
Activation

Probabilistic transducer
from source s to target r
with delay
❥

✁✰

r ✰✁ ❂

❳

t

s

✷❙

❥

s

01.05 2017
01.05 2017

(i) Probabilistic Transducer Hsr❀✁❂✸✵

Property Crimes

21.04 2017
21.04 2017

(Note: Influence Exists over Multiple Time-scales from the Same Source)

Violent Crimes

11.04 2017
11.04 2017

d. Example of Remote Sources Influencing Property Crimes at a Target Location

✷
✶
✷
✶

01.04 2017
01.04 2017

No. of Events

s

target prediction
steps
from current time

✁

✵

✏

✦ ✁✰ H ✁✰ s ✶
s

r❀

s

❥

r❀

❥

t

✑

❥

≦

source data
upto ❥ steps
before current time

Fig. 1. Crime Data & Modeling Approach. a and b show the recorded infractions within the 2 week period between April

1 and 15 in 2017. Plate c illustrates our modeling approach: We break city into small spatial tiles approximately 1.5 times
the size of an average city block, and compute models that capture multi-scale dependencies between the sequential event
streams recorded at distinct tiles. In this paper, we treat violent and property crimes separately, and show that these categories
have intriguing cross-dependencies. Plate d illustrates our modeling approach. For example, to predict property crimes at
some spatial tile r, we proceed as follows: Step 1) we infer the probabilistic transducers that estimate event sequence at r
by using as input the sequences of recorded infractions (of different categories) at potentially all remote locations (s❀ s✵ ❀ s✵✵
shown), where this predictive influence might transpire over different time delays (a few shown on the edges between s and
r ). Step 2) Combine these weak estimators linearly to minimize zero-one loss. The inferred transducers can be thought of as
inferred local activation rules, which are then linearly composed, reversing the approach of linearly combining input and then
passing through fixed activation functions in standard neural net architectures. The connected network of nodes (variables)
with probabilistic transducers on the edges comprises the Granger Network.

a. Spatial Distribution of AUC

c. Distribution of out-of-sample

b. Spatial Distribution of AUC

for Property crimes

AUC Across Spatial Tiles

for Violent Crimes
10

Average

5
1.0

1.0

0.9

0.9

0.8

0.8

0.7

0.7

0.6

0.6

0.5

0.5

0.897

0
0.8

0.85

0.9

0.87

0.8

0.9

8
6
4
2
0

0.87

0

0

0.4

0.2

0

Violent
Property
1.5

2

4

6

2

1

0.5

0
0

Property
Crime

0

1

Diffusion Rates

0.5 week
1 week
2 weeks
3 weeks

0.6

0.9

(ii) Property Crimes

Violent
Crime

0.2

AUC

f. Inferred Influence

(≦ 3 day influence period)

[mile/day]

probability

0.4

e. Inferred Neighborhood Samples
(i) Violent Crimes

0.5 week
1 week
2 weeks
3 weeks

1

Violent
Crime

0.8

0.6

1

Property
Crime

8
6
4
2
0

d. Distribution of Influence Radius

0.95

4
mile

5

10 15
time [days]

20

6

Fig. 2. Predictive Performance of Granger Nets. a an b illustrate the out-of-sample area under the receiver operating
characteristics curve (AUC) for predicting violent and property crimes respectively. The prediction is made a week in advance,
and the event is registered as a successful prediction if we get a hit within ✝ day of the predicted date. c illustrates the
distribution of AUC on average, individually for violent and property crimes. Our mean AUC is close to
. Panels d-f
shows influence Diffusion & Perturbation Space. If we are able to infer a model that is predicts event dynamics at a
specific spatial tile (the target) using observations from a source tile
days in future, then we say the source tile is within
the influencing neighborhood for the target location with a delay of . d illustrates the spatial radius of influence for 0.5,
1, 2 and 3 weeks, for violent (upper panel) and property crimes (lower panel). Note that the influencing neighborhoods,
as defined by our model, are large and approach a radius of miles. Given the geometry of the City of Chicago, this
maps to a substantial percentage of the total area of urban space under consideration, demonstrating that crime manifests
demonstrable long-range and almost city-wide influence. e illustrates the extent of a few inferred neighborhoods at time delay
of at most days. f illustrates the average rate of influence diffusion measured by number of predictive models inferred that
transduce influence as we consider longer and longer time delays. Note that the rate of influence diffusion falls rapidly for
property crimes, dropping to zero in about a week, whereas for violent crimes, the influence continues to diffuse even after
three weeks.

✶

✁
✁

✻

✸

✾✵✪

A. Spatial Distribution of

C. Distribution of Increased Arrests

Hardship Index

from Increase In Violent Crimes

0.15
0.10

0

0.05

0.00

0.00

∆+ =
17.9%

from Increase In Violent Crimes
(I) Perturbation In Violent Crime Rate

regression coeffcient (95% confidence)

0.20

0.03

E. Distribution of Decreased Arrests

Against Socio-Economic Indicators

0

12

0.

0.06

∆+ =
15.3%

B. Spatial Change of Arrest Rate

from Increase In property Crimes

06
0.

80

0.09

0
04
0.

0.0

80
60
40
20

0.12

D. Distribution of Increased Arrests

F. Distribution of Decreased Arrests
from Increase In Property Crimes

0.2
1.00

1.00

00

0.6

0

00

0.75

0.75

0.6

−0.2
0.25

(II) Perturbation: property crime Rate

0.00

0.1

0.50
0.25
0.00

0

E

D

M

IN

O
C

IP

IN

SH

TA

D
A
R
H

PI

EX

64

M
R
O

A
C
R
PE

N

R
O
VE

LO
18
ER

W
+

U
%

25

A

D
O
YE

IP

PL

D
T

EM

N

O
U
IT
H

U
16

+

EL
B
%

ED

%

0

AG

0

%

∆− =
-36.4%

.3

D

ED

RT
Y

D

PO
VE

RO
W
C

O
W

S.
U
O

∆− =
-36.3%

0

H

0

0.60

0.600

−0.1

%

0.300

0.50

socio-economic indicators

Fig. 3. Estimating Bias. a illustrates the distribution of hardship index (see SI). c, d, e, and f suggest biased response

to perturbations in crime rates. With a 10% increase in violent or property crime rates, we see an approximately a
decrease in arrests when averaged over the city. The spatial distribution of locations that experience a positive vs.
negative change in arrest rate reveals a strong preference favoring wealthy locations. If neighborhoods are doing better
socio-economically, increased crime predicts increased arrests. A strong converse trend is observed in predictions for
poor and disadvantaged neighborhoods, suggesting that under stress, wealthier neighborhoods drain resources from their
disadvantaged counterparts. b illustrates this more directly via a multi-variable regression, where hardship index is seen to
make a strong negative contribution.

✸✵✪

103
104
105
106
107
108
109
110
111

model is trained on crime statistics, demographic makeup, meteorological data, and Google street view images
to track graffiti, achieving an out-of-sample AUC of ✿ . Our AUC is demonstrably higher (see Table II), and
we predict with significantly less data (only past events), and days into future (instead of next-day). Additionally,
the use of demographic and graffiti is problematic with the possibility of introducing racial and socio-economic
bias, with dubious causal value. In the second article 19 , the authors combine convolutional and recurrent neural
networks with weather, socio-economic, transportation, and crime data, to predict the next-day count of crime in
Chicago. As spatial tiles, the authors use standard police beats, which break up Chicago into
regions. Police
beats reflect the classical notion of social neighborhoods, and measure approximately 1 sq. mile on average 20 .
In comparison, our spatial times are approximately ✿ sq. miles, representing a 2500% higher resolution. This

✽✸ ✸✪

✼

✷✼✹

✵ ✵✹

g. Regression against poverty

AUC

✵✿✺

a. Atlanta (mean AUC: ✙ ✵ ✽✾)

d.

✿

(std. error shown)

✵✿✾✺
Detroit (mean AUC: ✙ ✵✿✾✵)

crime rate
violent crime perturbation
property crime perturbation

Los Angeles

e. Los Angeles (mean AUC: ✙ ✵ ✽✼)
✿

San Francisco

b. Philadelphia (mean AUC: ✙ ✵ ✽✹)
✿

Philadelphia

Detroit

c. San Francisco (mean AUC: ✙ ✵ ✽✻) f. Austin (mean AUC: ✙ ✵ ✽✼)
✿

✿

Atlanta

Austin

✶✵

✵

✶✵

regression slope

Fig. 4. Prediction of property and violent crimes across major US cities and dependence of perturbation response
on socio-economic status of local neighborhoods. Panels a-f illustrate the AUCs achieved in six major US cities. These
cities were chosen on the basis of the availability of detailed event logs in the public domain. All of these cities show
comparably high predictive performance. Panel g illustrates the results obtained by regressing crime rate and perturbation
response against SES variables (shown here for poverty, as estimated by the 2018 US census). We note that while crime
rate typically goes up with increasing poverty, the number of events observed one week after a positive perturbation of
5-10% increase in crime rate is predicted to fall with increasing poverty. We suggest that this decrease is explainable by
reallocation of enforcement resources disproportionately, away from disadvantaged neighborhoods in response to increased
event rates, which leads to smaller number of reported crimes.

112
113
114
115
116

✼✺ ✻✪

✾✵✪

model achieves a classification accuracy of ✿
for Chicago, which compares against our accuracy of ❃
(See Table II). While this competing model tracks more crime categories, it is limited to next-day predictions with
significantly coarser spatial resolution. We also compare the predictive ability of naive autoregressive baseline
models (See Material and Methods and Table III), which perform poorly, but provide a yardstick to meaningfully
compare our claimed performance estimates.

117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132

133
134
135
136
137
138
139
140

With our precise predictive apparatus in place, we run a series of computational experiments that perturb the
rates of violent and property crimes, and log the resulting alterations in future event rates across the city. By
inspecting the effect of socio-economic status (SES) on the perturbation response, we investigate whether
enforcement and policy biases modulate outcomes. The inferred stress response of the city suggests the
presence of socio-economic bias (See Fig. 3). Wealthier neighborhoods away from the inner city respond to
elevated crime rates with increased arrests, while arrest rates in disadvantaged neighborhoods drop, but the
converse does not occur (See Fig. 3, panels e and f). Resource constraints on law enforcement, combined
with biased prioritization to wealthier neighborhoods, result in reduced enforcement across the remainder of the
city. This provides evidence for enforcement bias within U.S. cities that parallels widely discussed notions of
suburban bias in wealthy suburbs 21,22 . While self-evident at the scale of countries and regions, the existence
of unequal resource allocation in cities, where political power and influence concentrates in selective, wealthy
neighborhoods, has been widely suspected 23–27 . Our analysis provides direct support for this contention, which
shows up robustly for all years analyzed, going back over one and half decades in Chicago. Figs 6 and 7
show that these patterns are stable over time, at least in recent years. Additionally, Fig. 5 show the effect of
perturbations across all variables, suggesting that crime reduction from perturbations seems to be most effective
in regions with high crime rates, with SES confounders.
Beyond Chicago, we analyze criminal event logs available in the public domain for six additional major US cities:
Detroit, Philadelphia, Atlanta, Austin, San Francisco and Los Angeles. In all these cities we obtain comparably
high performance in predicting violent and property crimes, with average AUC ranging between (See
Fig 4a-f). In addition, our observed pattern of perturbation responses in Chicago, which suggests de-allocation
of policing resources from disadvantaged neighborhoods to advantaged ones, is replicated in all these cities.
While crime rate increases with degrading SES status of local neighborhoods, the number of predicted events
a week after a positive 5-10% increase in crime rate is predicted to go down. Thus increasing the crime rate
leads to a smaller number of reported crimes, a pattern holding more often in poorer neighborhoods.

✽✻ ✾✵✪

147

Our analysis also sheds light on the continuing debate over the choice for neighborhood boundaries in urban
crime modeling 28–31 . In Fig. 2d-f, we demonstrate that despite apparent natural boundaries, influence is often
communicated over large distances and decays slowly, especially for violent crimes. More importantly, this study
reveals how the “correct” choice of spatial scale should not be a major issue in sophisticated learning algorithms
where optimal scales can be inferred automatically. We find that there exists a skeleton set of spatial tiles, which
have strong influence on the overall event patterns (See Fig. 10). These induce a cellular decomposition of the
city that identifies functional neighborhoods, where the cell-size adapts automatically to the local event dynamics.

148

L IMITATIONS & C ONCLUSION

141
142
143
144
145
146

149
150
151
152
153
154
155

156
157
158
159
160
161
162
163
164
165
166
167

To our knowledge, this is the first analysis exploring perturbations of predictive data-driven models to probe the
social dynamics of crime and its enforcement. Our ability to probe for the extent of enforcement bias is limited by
our dataset; since inference of crime patterns are easily skewed by arrest rates. Disproportionate police response
in Black communities can contribute to biases in event logs, which might propagate into inferred models. This
has resulted in significant pushback from diverse communities against predictive policing 32 . Our approach is
free from manual encoding of features (and thus resistant to implicit biases of the modelers themselves), but
biases arising from disproportionate surveillance might still remain.
Even with its current limitations, however, this new addition to the toolbox of computational social science enables
validation of complex theory from observed event incidence, supplementing the use of measurable proxies
and potential biases in questionnaire-based data collection strategies. While classical approaches 33–36 broaden
our understanding of the societal forces shaping both urban and regional landscapes, these approaches have
neither successfully attempted to forecast individual infraction reports, nor reveal how these predictive patterns
manifest systematic enforcement bias. In this study, we show how the ability of Granger Networks to predict such
events not only opens new doors for precise intervention, but also advances the diagnosis and explanation of
complex social patterns. We acknowledge the danger that powerful predictive tools place in the hands of overzealous states in the name of civilian protection, but here we demonstrate their unprecedented ability to audit
enforcement biases and hold states accountable in ways inconceivable in the past. We encourage widespread
debate regarding how these technologies are used to augment state action in public life, and call for transparency
that allows for continuous evaluation, reconsideration and critique.

168

M ATERIALS AND M ETHODS

173

In this study we use historical geolocated incidence data of criminal infractions to model and predict future events
in Chicago, Philadelphia, San Francisco, Austin, Los Angeles, Detroit and Atlanta. Each of the cities considered
have a specific temporal and spatial resolution, which are optimized to maximize predictive performance (See
Table I). The predictive performance obtained in these cities are enumerated in Table II. The distribution of AUCs
obtained in Chicago for earlier years (2014-2017, predicted individually) are shown in Fig 8.

174

Data Source

169
170
171
172

175
176
177
178
179
180
181
182
183
184
185
186
187
188
189

The sources of the crime incidence data used in this study for the different US cities are enumerated in Table I.
Theses logs include spatio-temporal event localization along with the nature, category, and a brief description
of the recorded incident. For the City of Chicago, we also have access to the number of arrests made during or
as a result of each event. For Chicago, the log is updated daily, keeping current with a lag of days, and we
make predictions for each of the years 2014-2017 (using years before the target year for model inference, and
year for out-of-sample validation) for the prediction results shown in Figure 1. The evolving nature of the urban
scenescape 37 necessitates that we restrict the modeling window to a few years at a time. The length of this
window is decided by trading off loss of performance from shorter data streams to that the evolution of underlying
generative processes for longer streams. The training and testing periods of the other cities is tabulated in Table I.
In this study, we consider two broad categories of criminal infractions: violent crimes consisting of homicides,
assault, battery etc., and property crimes consisting of burglary, theft, motor vehicle theft etc. Drug crimes are
excluded from our consideration due to the possibility of ambiguity in the use of violence in such events. For
the City of Chicago, the number of individuals arrested during each recorded event is considered a separate
variable to be modeled and predicted, which allows us to investigate the possibility of enforcement biases in
subsequent perturbation analyses.

✼

✸

✶

194

We also use data on socio-economic variables available at the portal corresponding to Chicago community
areas and census tracts, including
of population living in crowded housing, those residing below the poverty
line, those unemployed at various age groups, per capita income, and the urban hardship index 38 . Such data is
also obtained from the City of Chicago data portal. Additionally, we use data on poverty estimates for the other
cities, which are obtained https://www.census.gov.

195

Spatial and Temporal Discretization & Event Quantization

190
191
192
193

196
197
198
199

✪

Event logs are processed to obtain time-series of relevant events, stratified by occurrence locations. This is
accomplished by choosing a spatial discretization, and focusing on one individual spatial tile at a time, which
allows us to represent the event log as a collection of sequential event streams (See Fig. 1c). Additionally, we
discretize time, and consider the sum total of events recorded within each time window.

209

Coarseness of these discretizations reflects a trade-off between computational complexity and event localization
in space and time. Spatial and temporal discretizations are not independently chosen; a finer spatial discretization
dictates a coarser temporal quantization, and vice versa to prevent long no-event stretches and long periods of
contiguous event records, both of which reduce our ability to obtain reliable predictors. For the City of Chicago,
we fix the temporal quantization to day, and choose a spatial quantization such that we have high empirical
entropy rates for the time series obtained. This results in spatial tiles measuring ✿
°✂ ✿
° in latitude
✵
and longitude respectively, which is approximately
across, roughly corresponding to an area of under ✂
city blocks. Thus, any two points within our spatial tile are at worst in neighboring city blocks. We dropped from
our analysis the tiles that have too low a crime rate (❁
of days within the modeling window had any event
recorded) to reduce computational complexity, resulting in an ◆
of spatial tiles in the city of Chicago.

210

The temporal and spatial resolution is adjusted in a similar manner for the other cities (See Table I).

200
201
202
203
204
205
206
207
208

211
212
213
214
215
216

✶

✵ ✵✵✷✼✻

✶✵✵✵

✺✪

✵ ✵✵✸✺

✷ ✷

❂ ✷✷✵✺

Thus, we end up with three different integer-valued time series at each spatial tile: 1) violent crime (✈ ), 2)
property crime (✉) and 3) number of arrests (✇) in the City of Chicago. For other cities, we have only the first
two categories, since information on arrests was not available. We ignore the magnitude of the observations, and
treat them as Boolean variables. Thus, our models simply predict the presence or absence of a particular event
type in a discrete spatial tile within a neighboring city block and observation window, ✐✿❡✿, within the temporal
resolution chosen, which is day except for Atlanta, where is it is chosen to be days (See Table I).

✶

✷

217

218
219
220
221
222
223

224
225
226
227
228
229
230
231
232
233
234
235
236
237

238
239
240
241
242

243
244
245
246
247
248
249
250
251
252
253
254
255

Inferring Generators of Spatio-temporal Cross-dependence

❂

❂

Let ▲ ❢❵✶ ❀ ✁ ✁ ✁ ❀ ❵◆ ❣ be the set of spatial tiles, and ❊
❢✉❀ ✈❀ ✇❣ be the set of event categories as described
in the last section. At location ❵ ✷ ▲ for variable ❡ ✷ ❊ , at time t, we have ❵❀ ❡ t ✷ ❢ ❀ ❣, with indicating the
presence of at least one event. The set of all such combined variables (space + event type) is denoted as ❙ ,
i.e., ❙ ▲ ✂ ❊ . Let ❚ ❢ ❀ ✁ ✁ ✁ ❀ ▼
❣ denote the training period consisting of ▼ time steps. Because for any
time t, ❵❀ ❡ t is a random variable, our goal here is to learn its dependency relationships with its own past, and
with other variables in ❙ to accurately estimate its future distribution for t ❃ ❚ .

❂
✭ ✮

❂ ✵

✭ ✮

✵✶

✶

✶

To infer the structure of our predictive model, we learn a finite state probabilistic transducer 16 (referred to as
a Crossed Probabilistic Finite State Automata or a XPFSA 15 ) for each possible source-target pair s❀ r ✷ ❙ .
Given a sequence of events at the source, these inferred transducers estimate the distribution of events at
target r for some future point in time. Ability to estimate such a non-trivial distribution indicates the presence of
causal influence. Here we assume that causal influence from the source to the target manifests as the source
being able to predict events occurring at the target, better than the target can do by itself. This interpretation
follows from Granger’s eponymous approach to statistical causality 39 . Importantly, we do not assume that the
underlying processes are iid, or that the model has any particular linear structure. Additionally, such influence is
not restricted to be instantaneous. The source events might impact the target with a time delay, ✐✿❡✿, a specific
model between the source and target might predict events delayed by an a priori determined number of steps
≧ specific to the model. Here we model the influence structure for each integer-valued delay
♠❛① ≧
separately. Thus, for source s and target t, we can have ♠❛①
transducers each modeling the influence for
a specific delay in ❢ ❀ ♠❛① ❣. The maximum number of steps in time delay ♠❛① is chosen a priori, based on
the problem at hand.

✁

✁ ✵

✁

✵✁

✰✶

✁

While these influences or dependencies may differ for different delays, they need not be symmetric between
source and target pairs. The complete set, comprising at most ❥❙❥✷ ♠❛①
models, represents a predictive
framework for asymmetric multi-scale spatio-temporal phenomena. Note that the number of possible models
increase quickly. For example, for the City of Chicago, for ♠❛①
with
spatial tiles and three event
categories, the number of inferred models is bounded above by ✙ ✿ billion.

✭✁

✁

❂ ✻✵
✷✻

✰ ✶✮

✷✷✵✺

ur approach consists of inferring XPFSAs in two key steps (See Fig. 1d, and discussion later in SI-Section 2):
First, we infer XPFSA models for all source-target pairs and all delays up to ♠❛① . In the second step, we learn
a linear combination of these transducers to maximize predictive performance. Denoting the observed event
sequence in time interval ✶❀ t at source s as st ✶ , the XPFSA Hsr❀❦ estimates the distribution of events for
target r at time step t ❦. This is accomplished by learning an equivalence relation on the historical event
sequences observed at source s, such that equivalent histories induce an approximately identical future event
distribution at target r, ❦ steps in the future. Thus, for example, the XPFSA shown in Fig. 1d has four states,
indicating that there are such equivalence classes of observations that induce the distinct output probabilities
shown from each state. Often this estimate is not very precise due to the possibility for multi-scale and multisource influence, e.g., when target r is influenced by multiple sources with different time delays. In the second
step, we employ a standard gradient boosting regressor for each target, to optimize the linear combination of
s
inferred transducers and learn the scalar weights ✦r❀❦
for source s, target r and delay ❦. Detailed pseudocode
of the inference algorithms are provided in the SI-section 1.

✁

✰

✭

❪

✹

263

To compare with a standard neural net architecture, these probabilistic transducers may be viewed as local
non-linear activation functions. With neural networks we repeatedly compute affine combination of inputs and
apply fixed non-linear activation to the combined input and finally optimize affine combination weights via
backpropagation, but here we first learn the local non-linear activations, and then optimize the linear or affine
combination of weak estimators. Optimizing the weights is a significantly simpler, local operation and may be
done with any standard regressor. In contrast to recurrent neural nets (RNN), the role of hidden layer neurons
is partially accounted for by states of the XPFSA, which are a priori undetermined both with respect to their
multiplicity and their transition connectivity structure.

264

Computational & Model Complexity

256
257
258
259
260
261
262

265
266
267
268
269
270

✻✵
✻✶ ✻✺✵ ✵✵✵
✷✽

We assume the maximum time delay in the influence propagation to be
days for all cities, which for the City
of Chicago results in at most ❀
❀
❀
inferred models, of which ❀
❀
are useful with ✌ ≧ ✿ . Model
inference in this case consumed approximately
❑ core-hours on
core Intel Broadwell processors, when
carried out with incidence data over the period Jan 1, 2014 to December 31, 2016. Computational cost for other
time-periods and other cities are comparable and roughly scale with the square of the number of spatial tiles,
and linearly with the length of time-quantized data-streams considered as input to the inference algorithm.

✷ ✻✻✾ ✷✺✶ ✼✷✺

✷✵✵

✵ ✵✶

271

272
273
274
275
276
277
278
279
280
281
282
283
284

285
286

287

Crime Prediction Metrics
For each spatial location, the inferred Granger Net maps event histories to a raw risk score as a function of
time. The higher this value, the higher the probability of an event of target type occurring at that location, within
the specified time window. To make crisp predictions, however, we must choose a decision threshold for this
raw score. Conceptually identical to the notion of Type 1 and Type 2 errors in classical statistical analyses, the
choice of a threshold trades off false positives (Type 1 error) for false negatives (Type 2 error). Choosing a small
threshold results in predicting a larger fraction of future events correctly, i.e., have a high true positive rate (TPR),
while simultaneously suffering from a higher false positive rate (FPR), and vice versa. The receiver operating
characteristic curve (ROC) is the plot of the FPR vs the TPR, as we vary this decision threshold. If our predictor
is good, we will consistently achieve high TPR with small FPR resulting in a large area under the ROC curve
denoted as the AUC. Importantly, AUC measures intrinsic performance, independent of the threshold choice.
Thus, the AUC is immune to class imbalance (the fact that crimes are by and large rare events). An AUC of
indicates that the predictor does no better than random, and an AUC of
implies that we can achieve
perfect prediction of future events, with zero false positives.

✺✵✪

✶✵✵✪

We use a flexible approach in evaluating AUC; a positive prediction is treated as correct if there is at least one
event recorded in ✝ time steps in the target spatial tile.

✶

Predictability Analysis

✶

292

In the City of Chicago, we can predict events approximately a week in advance at the spatial resolution of ✝
city blocks with a temporal resolution of ✝ day, with a false positive rate of less than
and a median true
positive rate of
. The predictive performance in the other cities is enumerated in Table II. While not directly
modeled in the frequency domain, we found that the event forecasts produce very similar signatures in the
frequency domain (See Fig. 9), when compared over the first
days of each out-of-sample period (1 yr).

293

Spatial Neighborhoods

288
289
290
291

✶

✼✽✪

✷✵✪

✶✺✵

300

The degree of causal influence exerted by one variable (the source stream) on another (the target stream) is
quantified by the coefficient of causal dependence (✌ , see SI-Section 2). Identifying the source-target pairs for
which the coefficient of causality is high (See Fig 10), we note that there exists a sparse set of spatial tiles
which exert nearly all of the influence in the entire set of observed variables. Thus, observing these variables
alone would enable us to make good event forecasts. These tiles span the expanse of the city, and a Voronoi
decomposition based on the centers of these tiles in shown in Fig 10b. Such a decomposition demonstrates an
algorithmic approach to choosing optimal neighborhoods for urban analysis.

301

Perturbation Analysis

294
295
296
297
298
299

302
303
304
305

306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322

✶

We experimented with positive and negative perturbations to both violent and property crime rates ranging from
to
of observed rates. Response to perturbed crime rates was measured as the relative change from nominal
baseline in estimated time-average for the predicted event frequencies week in the future, corresponding to
violent and property crimes and number of arrests.

✶✵✪

✶

Results from our perturbation experiments shed light both on the stability characteristics of crime in Chicago,
and further allowed us to look for evidence of biased police enforcement responses under stress. Under stress,
well-off neighborhoods tend to drain resources disproportionately from disadvantaged locales (See Fig. 3). For
economically well-off neighborhoods in the bottom
of the hardship index are much more likely to see a near
-proportional increase (✙
) in law enforcement response, measured by the number or predicted arrests on
a
increase in crime rates (See Fig. 3, panels c and d, which show how regions with increased enforcement
response are concentrated in well-off neighborhoods), while the rest of the city see a drop in predicted response
of about twice the magnitude (❃
). Increased crimes causes enforcement resources to be drained from
disadvantaged neighborhoods to support their better socioeconomic counterparts. We performed multi-variable
linear regression analysis to evaluate the question in another way. Here we regressed violent and property crime
rates, independently, on the variables listed in (Fig. 3b), including a slope intercept variable in each model. In both
models, the hardship index exhibits a strong, negative influence on changes in arrest rate from perturbations that
increase violent and the property crime rates, which contradicts what might be expected in the absence of bias.
Poorer neighborhoods have more crime and so these socio-economic indicators should contribute positively
to the arrest rate with increasing crime. These patterns were replicated in our perturbation experiments for all
preceding years we analyzed (2014 through 2017, See Fig 6 and 7). Response measured in the property an
violent crimes, and in the associated arrests from perturbations is detailed in Fig 5.

✶✵✪

✷✺✪

✶✺✪

✸✵✪

TABLE I

C RIME E VENT L OG I NFORMATION FOR C ITIES C ONSIDERED
Atlanta

Austin

Detroit

Los Angeles

Philadelphia

San
Francisco

Chicago

no. of
variables✶

✺✶✵

✶✵✽✷

✶✶✻✶

✸✷✽✼

✶✵✸✼

✾✼✺

✸✽✷✻

temporal
resolution

✷ days
✸✸ ✻✺✍✍ N,
✸✸ ✽✻✍ N,
✽✹ ✺✹✍ W,
✽✹ ✸✶ W
✾✽✸✵ ✂ ✾✽✸✵

✶ day
✸✵ ✶✹✍✍ N,
✸✵ ✹✽✍ N,
✾✼ ✽✾✍ W,
✾✼ ✻✸ W
✾✽✸✵ ✂ ✾✽✸✵

✶ day
✹✷ ✸✵✍✍ N,
✹✷ ✹✺✍ N,
✽✸ ✷✽✍ W,
✽✷ ✾✶ W
✾✽✸✵ ✂ ✾✽✸✵

✶ day
✸✸ ✼✶✍ N,
✸✹ ✸✸✍ N,
✶✶✽ ✻✺✍ W,
✶✶✽ ✶✻✍ W
✾✽✸✵ ✂ ✾✽✸✵

✶ day
✸✾ ✽✽✍✍ N,
✹✵ ✶✷✍ N,
✼✺ ✷✼✍ W,
✼✹ ✾✻ W
✾✽✸✵ ✂ ✾✽✸✵

✶ day
✸✼ ✼✶✍ N,
✸✼ ✽✶✍ N,
✶✷✷ ✺✶✍ W,
✶✷✷ ✸✻✍ W
✾✽✸✵ ✂ ✾✽✸✵

✶ day
✹✶ ✻✹✍✍ N,
✹✷ ✵✻✍ N,
✽✼ ✽✽✍ W,
✽✼ ✺✷ W
✾✺✶✵ ✂ ✶✵✵✻✵

Spatial
exclusion
threshold✷

✷ ✺✪

✷ ✺✪

✷ ✺✪

✷ ✺✪

✺ ✵✪

✷ ✺✪

✺ ✵✪

training
period

14/01/0118/12/31

16/01/0118/12/31

12/01/0114/12/31

16/01/0118/12/31

16/01/0118/12/31

14/01/0116/12/31

14/01/0116/12/31

test period

19/01/0119/07/20

19/01/0119/04/11

15/01/0115/04/11

19/01/0119/04/11

19/01/0119/04/11

17/01/0117/04/11

17/01/0117/04/11

prediction
horizon

✻ days

✸ days

✸ days

✸ days

✸ days

✸ days

✼ days

violent
crime stat.

event count
, rate

✷✻✹✾
✸ ✾✽✪

event count
, rate

✷✵✶✸✷
✺ ✹✺✪

event count
, rate

✷✵✾✷✷
✸ ✼✷✪

event count
, rate

✼✷✸✺✺
✹ ✽✸✪

event count
, rate

✸✸✽✵✸
✽ ✶✶✪

event count
, rate

✷✸✸✶✼
✼ ✶✻✪

event count
, rate

✶✼✾✷✼✹
✼ ✼✪

property
crime stat.

event count
, rate

event count
, rate

event count
, rate

event count
, rate

event count
, rate

event count
, rate

✶✾✼✽✸✺
✶✷ ✽✸✪

event count
, rate

data.sfgov.
org

data.
cityofchicago.
org

bounding
box of
modeled
region
spatial
resolution

data source

✿

✿

✿

✿

✿

✿

✿

✿

✿

✿

✿

✿

✽✽✾✷✾
✻ ✷✷✪

✿

✿

✿

✿

✿

✿

✿

✿

✿

✿

✸✾✽✹✵
✸ ✸✵✪

✿

data.
detroitmi.gov

✿

✿

✿

✽✺✻✽✸
✾ ✵✷✪
✿

data.lacity.org

✿

✿

✿

✿

✷✵✺✹✸✺
✺ ✹✾✪

✿

data.
austintexas.
gov

✿

✿

✿

✿

opendata.
atlantapd.org

✿

✿

✿

✿

✷✸✺✷✷
✹ ✺✶✪

✿

✿

www.
opendata
philly.org

♥

✿

✿

✿

✿

✿

✿

✷✻✸✻✻✶
✼ ✵✪
✿

✶ No. of variables indicates the total number of time series considered for violent and property crimes.
✷ Tiles with less than threshold event-rate were excluded.

TABLE II

P REDICTION PERFORMANCE WITH G RANGER N ET FOR SEVEN US CITIES

city
Atlanta
Austin
Detroit
Philadelphia
Los Angeles
San Francisco
Chicago
②

property crimes

violent crimes

median AUC

accuracy②

median AUC

accuracy

✵✿✾✵

✵✿✽✹

✵✿✽✽

✵✿✽✹

✵✿✾✵

✵✿✽✻

✵✿✽✾

✵✿✽✹

✵✿✽✼
✵✿✽✼
✵✿✽✹
✵✿✽✻
✵✿✽✼

✵✿✽✷
✵✿✽✶
✵✿✽✸
✵✿✽✵
✵✿✾✸

✵✿✽✽
✵✿✽✼
✵✿✽✹
✵✿✽✻
✵✿✽✼

Accuracy calculated with sensitivity✂frequency✰specificity✂✭✶

✵✿✽✸
✵✿✽✶
✵✿✽✸
✵✿✽✶
✵✿✾✹

frequency✮.

325

We also carried out similar perturbation analyses for the other cities, and observed that with increasing poverty
we have expected increase of observed crime rates, but an unexpected decrease in violent and property crimes
after a 5-10% simulated uptick in either category of crimes (See Fig. 4).

326

Naive Baselines: Autoregressive Integrated Moving Average (ARIMA) Models

323
324

327
328
329
330

To explore the predictive ability of naive baseline models on our datasets, we consider four ARIMA ? configurations with lag orders ♣ ❂ ✺ and ✶✵, numbers of differencing ❞ ❂ ✶ and ✷, and the window of moving average
q ❂ ✵. Let ②t be the series we want to model and ②t✵ be ②t differenced by ❞ times, the ARIMA✭♣❀ ❞❀ q ✮ models
series ②t✵ by
②t✵ ❂ ❝ ✰ ✣✶ ②t✵ ✶ ✰ ✁ ✁ ✁ ✰ ✣♣ ②t✵ ♣ ✰ ✒✶ ✧t ✶ ✰ ✁ ✁ ✁ ✰ ✒q ✧t q ✰ ✧t
(1)

TABLE III

N AIVE BASELINE RESULTS : MEAN AUC ACHIEVED WITH ARIMA MODELS

city
Atlanta
Austin
Detroit
Philadelphia
Los Angeles
San Francisco
Chicago

ARIMA✭✺❀ ✶❀ ✵✮

ARIMA✭✶✵❀ ✶❀ ✵✮

ARIMA✭✺❀ ✷❀ ✵✮

ARIMA✭✶✵❀ ✷❀ ✵✮

✵✿✻✺

✵✿✻✻

✵✿✻✷

✵✿✻✻

✵✿✺✾

✵✿✻✷

✵✿✺✼

✵✿✻✶

✵✿✻✹

✵✿✻✼

✵✿✻✶

✵✿✻✻

✵✿✼✵

✵✿✼✶

✵✿✻✺

✵✿✻✽

✵✿✻✹

✵✿✻✸

✵✿✻✺

✵✿✻✽

✵✿✻✸

✵✿✼✵

✵✿✻✻
✵✿✻✼

✵✿✻✼

✵✿✻✺
✵✿✻✾
✵✿✻✾

where ✣✶ ❀ ✿ ✿ ✿ ❀ ✣♣ and ✒✶ ❀ ✿ ✿ ✿ ❀ ✒q are the coefficients to be fitted. In Eq. (1), ②t✵ ❦ s are the historical values of
②t✵ whose inclusion models the influence of past values on the current value (autoregression), and ✧t ❦ s are
the white noise terms whose inclusion models the dependence of current value against current and previous
(observed) white noise error terms or random shocks (moving average). Specifically, we use the following four
models for the earthquake and the crime datasets

✵
✁ ✁ ✁ ✰ ✣✺ ②t✵ ✺
✭✶✮
②t ❂ ❝ ✰ ✣✶ ②t✵ ✶ ✰ ✁ ✁ ✁ ✰ ✣✺ ②t✵ ✶✵
✭✷✮
②t ❂ ❝ ✰ ✣✶ ②t✵ ✶ ✰ ✁ ✁ ✁ ✰ ✣✺ ②t✵ ✺
✭✷✮
② ❂ ❝ ✰ ✣✶ ② ✵ ✰ ✁ ✁ ✁ ✰ ✣✺ ② ✵
✭✶✮

②t

✭❞✮

t

✭✶✮

❂ ❝ ✰ ✣✶ ②t ✶ ✰

t

t

✶

✶✵

(2)
(3)
(4)
(5)

✭✷✮

336

where ②t is ②t different by ❞ times (②t ❂ ②t ②t ✶ and ②t ❂ ②t ✷②t ✶ ✰ ②t ✷ ). For simple benckmarking,
we apply the ARIMA model to each individual time series, which means the predictive model is trained without
exogenous variables. For the implementation, we use the Python statsmodels package ? , and the result is
shown in Tab. III. The inadequate performance of ARIMA may be due to 1) the use of a single data stream
limits the ability of ARIMA to capture the interplay between co-evoluting processes, and 2) a pre-determined lag
order fails to capture the possibly varying temporal memory of individual processes.

337

ACKNOWLEDGMENTS

331
332
333
334
335

338
339
340

341
342
343
344
345
346
347

Our work greatly benefited from discussion of everyone who participated in our workshop series on crime
prediction at the Neubauer Collegium for culture and society 40 , and with those with whom we had extended
conversations to ground and refine our modeling approach.
Data was provided by the City of Chicago Data Portal at https://data.cityofchicago.org. The City of Chicago
(“City”) voluntarily provides the data on this website as a service to the public. The City makes no warranty,
representation, or guaranty as to the content, accuracy, timeliness, or completeness of any of the data provided
at this website (https://www.chicago.gov/city/en/narr/foia/data disclaimer.html), and the authors of this study are
solely responsible for the opinions and conclusions expressed in this study. Sources of the crime incidence data
for the other cities are tabulated in the Supplementary text. Socio-ecomonic data for metropolitan areas was
obtained from https://www.census.gov.

351

This work is funded in part by the Defense Sciences Office of the Defense Advanced Research Projects Agency
projects HR00111890043/P00004 and W911NF2010302, and the Neubauer Collegium for Culture and Society
through the Faculty Initiated Research Program 2017. The claims made in this study do not necessarily reflect
the position or the policy of the sponsors, and no official endorsement should be inferred.

352

R EFERENCES

348
349
350

353
354
355
356
357
358
359

[1] Bowers, K. J., Johnson, S. D. & Pease, K. Prospective hot-spotting: The future of crime mapping? The
British Journal of Criminology 44, 641–658 (2004).
[2] Chainey, S., Tompson, L. & Uhlig, S. The utility of hotspot mapping for predicting spatial patterns of crime.
Security Journal 21, 4–28 (2008).
[3] Fielding, M. & Jones, V. ‘disrupting the optimal forager’: Predictive risk mapping and domestic burglary
reduction in trafford, greater manchester. International Journal of Police Science & Management 14, 30–41
(2012).

A. Distribution of Decreased B. Distribution of Increased

C. Distribution of Decreased D. Distribution of Increased

Non-violent Crimes from
Increase in Violent Crimes

Violent Crimes from
Increase in Violent Crimes

Non-violent Crimes from
Increase in Violent Crimes

0.20

0

Violent Crimes from
Increase in Violent Crimes

0

0.10

0
0
.2
0

0.32
0.6

0.3

.1

.6

0

0

0.08

0

0

0.0

0.00

0.2
0

0

0.2

0.4

0

0.2

0.1

5

0

0.60

0.16

.1

0.4

0.200

0.4
0.6

0

0

.4

0

00

0.3

0.0

0

0

0.40

0.24

0.200

0.0

00

2
0.

0.200

0.300

0.6

00
0

.4

0

00

0

0.1

0
0

.2

0

0.400

0.200

0.10

0.200

0

E. Distribution of Decreased F. Distribution of Increased

G.

H.

Distribution of Decreased
Distribution of Increased
Non-violent Crimes from
Non-violent Crimes from
Violent Crimes from
Violent Crimes from
Increase in Non-violent Crimes Increase in Non-violent Crimes Increase in Non-violent Crimes Increase in Non-violent Crimes
0

00

0

0

.2

.2

0.1

0

0

0

0.60
0.45

0.6

00

00

0.3

0

00

0.00

0.32

0.2
00
0.30
0

0.24

0

0.400

0.15

0.15

0.4

0.45

.2

0.30

0.30

0.600

0.60

0.45

0.450

0

200

0.

0.600

0.00

0.30

0.16

0.15

0.08

0.00

0.00

0

0

10

0.

50

0.4

0

.2

0

0

40

0.

0.30

0

0
0

0.400

00

0.300

5

.1

0

0.2

0.40

00

0.1

I. Distribution of Decreased

J. Distribution of Increased

K. Distribution of Decreased L. Distribution of Increased

Non-violent Crimes from
Increased Arrests

Non-violent Crimes from
Increased Arrests

Violent Crimes from
Increased Arrests

Violent Crimes from
Increased Arrests
0

15

0.

0.60

0

.2

0

50

0

0.45

0
0
.3

0.00

0.4

0.30

0

0.400

0.15

0.15

0.00

0.00

0.40

0.

15

0

0.200

0.1

0.3

00

0
0.20

0
0

.4
0

0

0

0

0.30

0.2

0.0

.1

0.600

0.300

0.3

0.30

5
0

0

00

0

50

0.4

0.20

0.1

0.30
0.15

0.45

0.45

0.30

0.4

0.60

0.150

Fig. 5. Perturbation Effects Across Variables. We see that the decrease of violent crimes from increase of property

crimes are localized in disadvantaged neighborhoods (panel g). Similarly, the decrease of property crimes from increase
of violent crimes is also localized to disadvantaged neighborhoods (panel a), as well as the decreased violent crimes
from increased arrests (panel k). We see a weaker localization for the corresponding increases in crime rates under similar
perturbations. Looking at other pairs of variables under perturbation (rest of the panels), we generally do not see a very
prominent correspondence with the distribution of socio-economic indicators. It seems crimes (and particulalrly violent crimes)
are easier to dampen in lcales with high existing crime rates, which is desirable result. But such conclusions are currently
confounded by SES variables, and futher work is needed to investigate these effects more thoroughly.

360
361
362
363
364

[4] Mohler, G. O., Short, M. B., Brantingham, P. J., Schoenberg, F. P. & Tita, G. E. Self-exciting point process
modeling of crime. Journal of the American Statistical Association 106, 100–108 (2011).
[5] Mohler, G. O. et al. Randomized controlled field trials of predictive policing. Journal of the American
Statistical Association 110, 1399–1411 (2015).
[6] Poisson, S. D. Probabilité des jugements en matière criminelle et en matière civile, précédées des règles

a. 2014 Distribution of Increased

c. 2015 Distribution of Increased

e. 2016 Distribution of Increased

Arrests from Increase In Violent Crimes

Arrests from Increase In Violent Crimes

Arrests from Increase In Violent Crimes

0.000

0

0.06

0.06

0.03

0.03

0

0.09

4

40

0.025

0.12

08

0.09

.0

0

0.0

0
3
.0
0
60
0.0

0.050

0.

0.12

08

0.075

0.00

0.00

0

0.

0.100

b.
2014 Distribution of Decreased
d.
2015 Distribution of Decreased
f.
2016 Distribution of Decreased
Arrests from Increase In Violent Crimes
Arrests from Increase In Violent Crimes
Arrests from Increase In Violent Crimes
1.00

0.600
0

90

0.

00

1.00

0.6

00

0.75

0.50

0.50

0.50

0.25

0.25

0.25

0.00

0.00

0.00

0

0.30

0.75

0.300

0.300

0

0.60

1.00

0.6

0.75

0.600

0.600

Fig. 6. Stability of Suburban Bias over Years (Violent Crimes). We show that the nature of the perturbation response

shown in Fig. 3 in the main text holds true for earlier years as well: panels a and b correspond to year 2014, c and d
correspond to 2015 and e and f correspond to year 2016, all of which follow the same pattern shown in Fig. 3 in the main
text.

365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380

générales du calcul des probabilitiés (Bachelier, 1837).
[7] Du Sautoy, M. The Creativity Code: Art and Innovation in the Age of AI (Harvard University Press, 2020).
[8] Ferdinand, T. N. Demographic shifts and criminality: An inquiry. The British Journal of Criminology 10,
169–175 (1970).
[9] Cohen, L. & Felson, M. Social change and crime rate trends: A routine activity approach. American
Sociological Review 44, 588–608 (1979). Cited By 4102.
[10] Cohen, L. E. Modeling crime trends: a criminal opportunity perspective. Journal of Research in Crime and
Delinquency 18, 138–164 (1981).
[11] Wang, X. & Brown, D. E. The spatio-temporal modeling for criminal incidents. Security Informatics 1, 2
(2012).
[12] Liu, H. & Brown, D. E. Criminal incident prediction using a point-pattern-based density model. International
Journal of Forecasting 19, 603 – 622 (2003).
[13] Caplan, J. M., Kennedy, L. W., Barnum, J. D. & Piza, E. L. Crime in context: Utilizing risk terrain modeling
and conjunctive analysis of case configurations to explore the dynamics of criminogenic behavior settings.
Journal of Contemporary Criminal Justice 33, 133–151 (2017).
[14] Kang, H. W. & Kang, H. B. Prediction of crime occurrence from multi-modal data using deep learning.

Arrests from Increase In Property Crimes

c. 2015 Distribution of Increased

Arrests from Increase In Property Crimes

e. 2016 Distribution of Increased

Arrests from Increase In Property Crimes

0.16

0.16
5
.0
0
00
0.1

05
0.

0.050

a. 2014 Distribution of Increased

0.12

0.12

0.16
0.12
0.08

0.04

0.04

0.04

0.00

0.00

0

0

0.08

0.08

0.00
0

5
0.0

b.
2014 Distribution of Decreased
d. 2015 Distribution of Decreased
f. 2016 Distribution of Decreased
Arrests from Increase In Property Crimes Arrests from Increase In Property Crimes Arrests from Increase In Property Crimes
0.6

1.00

00

1.00

0.600

0.50

0.50

0.25

0.25

0.00

0.00

0.500

0.8

0

0.6

5

.7

0

0.4
0.250

0.75

0.2
0.0

0

0.30

0.300

0.75

0.600

0.600
0

.7

5

0

0.500

Fig. 7. Stability of Suburban Bias over Years (Property Crimes). We show that the nature of the perturbation response
shown in Fig. 3 in the main text holds true for earlier years as well: panels a and b correspond to year 2014, c and d
correspond to 2015 and e and f correspond to year 2016, all of which follow the same pattern shown in Fig. 3 in the main
text.

381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396

PLoS ONE 12, e0176244 (2017).
[15] Chattopadhyay, I. Causality networks. arxiv CoRR (2014). URL http://arxiv.org/abs/1406.6651.
[16] Mohri, M. Weighted Finite-State Transducer Algorithms. An Overview, 551–563 (Springer Berlin Heidelberg,
Berlin, Heidelberg, 2004).
[17] Granger, C. W. J. Testing for causality: A personal viewpoint. Journal of Economic Dynamics and Control
2, 329 – 352 (1980).
[18] Kang, H.-W. & Kang, H.-B. Prediction of crime occurrence from multi-modal data using deep learning. PloS
one 12, e0176244 (2017).
[19] Stec, A. & Klabjan, D. Forecasting crime with deep learning. arXiv preprint arXiv:1806.01486 (2018).
[20] Hannon, L. Neighborhood residence and assessments of racial profiling using census data. Socius 5,
2378023118818746 (2019).
[21] Meyer, W. B. & Graybill, J. K. The suburban bias of american society? Urban Geography 37, 863–882
(2016).
[22] Lipton, M. et al. Why poor people stay poor: a study of urban bias in world development (London: Canberra,
ACT: Temple Smith; Australian National University Press, 1977).
[23] Jackson, K. T. Crabgrass frontier: The suburbanization of the United States (Oxford University Press, 1987).

a. 2014

b. 2015

c. 2016

AUC
1.00
0.95
0.90
0.85
0.80
0.75

d. 2017

AUC
1.00
0.95
0.90
0.85
0.80
0.75

AUC
1.00
0.95
0.90
0.85
0.80
0.75

AUC
1.00
0.95
0.90
0.85
0.80
0.75

400

400

400

300

300

300

300

200

200

200

200

100

100

100

0.894

0.898

0

0

0
0.8

0.9
AUC

1

100

0.895

0.8

0.9
AUC

1

0.897

0
0.8

0.9
AUC

1

0.8

0.9

1

AUC

Fig. 8. Out of Sample Predictive Performance over the Years. We show that the predictive performance is very stable, and

variation in mean AUC is limited to the third place of decimal, at least when analyzing the last few years (✹ years shown).

397
398
399
400
401
402
403
404
405
406
407
408
409
410
411
412
413
414
415
416
417
418
419
420
421
422
423
424
425
426
427
428
429

[24] Duany, A., Plater-Zyberk, E. & Speck, J. Suburban nation: The rise of sprawl and the decline of the American
dream (Macmillan, 2001).
[25] Logan, J. R. The suburban advantage: New census data show unyielding city-suburb economic gap, and
surprising shifts in some places. Lewis Mumford Center for Comparative Urban and Regional Research,
University at Albany (2002).
[26] Lazare, D. America’s Undeclared War: What’s Killing Our Cities and how to Stop it (Harcourt, 2001).
[27] Young, I. M. Inclusion and democracy (Oxford University press on demand, 2002).
[28] SHERMAN, L. W., GARTIN, P. R. & BUERGER, M. E. Hot spots of predatory crime: Routine activities and
the criminology of place*. Criminology 27, 27–56 (1989). https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.
1745-9125.1989.tb00862.x.
[29] WOOLDREDGE, J. Examining the (ir)relevance of aggregation bias for multilevel studies of neighborhoods
and crime with an example comparing census tracts to official neighborhoods in cincinnati*. Criminology
40, 681–710 (2002).
[30] MEARS, D. P. & BHATI, A. S. No community is an island: The effects of resource deprivation on
urban violence in spatially and socially proximate communities*. Criminology 44, 509–548 (2006).
https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1745-9125.2006.00056.x.
[31] Weisburd, D., Groff, E. R., Yang, S.-M. & Telep, C. W. Criminology of Place, 848–857 (Springer New York,
New York, NY, 2014).
[32] Predictive
policing
algorithms
are
racist.
they
need
to
be
dismantled.
—
https://www.technologyreview.com/2020/07/17/1005396/
mit
technology
review.
predictive-policing-algorithms-racist-dismantled-machine-learning-bias-criminal-justice/.
(Accessed on
01/29/2021).
[33] Sutherland, E. H. Juvenile delinquency and urban areas: A study of rates of delinquents in relation to
differential characteristics of local communities in american cities. clifford r. shaw , henry d. mckay , norman
s. hayner , paul g. cressey , clarence w. schroeder , t. earl sullenger , earl r. moses , calvin f. schmid.
American Journal of Sociology 49, 100–101 (1943). https://doi.org/10.1086/219339.
[34] Sampson, R. J., Raudenbush, S. W. & Earls, F. Neighborhoods and violent crime: A multilevel study of
collective efficacy. Science 277, 918–924 (1997).
[35] Miethe, T. D., Hughes, M. & McDowall, D. Social Change and Crime Rates: An Evaluation of Alternative
Theoretical Approaches*. Social Forces 70, 165–185 (1991). http://oup.prod.sis.lan/sf/article-pdf/70/1/165/
6887328/70-1-165.pdf.
[36] Braga, A. A. & Clarke, R. V. Explaining high-risk concentrations of crime in the city: Social disorganization,
crime opportunities, and important next steps. Journal of Research in Crime and Delinquency 51, 480–498

predicted (normalized)
actual (normalized)

a. 2015 (time domain)

predicted
actual

b. 2015 (frequency domain)

2

50

0

0

−50
−2
0

20

40

60

80

100

120

140

0

5

10

time [day]
predicted (normalized)
actual (normalized)

c. 2016 (time domain)

15

20

25

30

35

40

time period [day]
predicted
actual

d. 2016 (frequency domain)
50

2
0
0

−50
−2
0

20

40

60

80

100

120

0

140

5

10

predicted (normalized)
actual (normalized)

e. 2017 (time domain)

15

20

25

30

35

40

time period [day]

time [day]

2

predicted
actual

f. 2017 (frequency domain)
50

0
0
−2
−50
0

20

40

60

80

time [day]

100

120

140

0

5

10

15

20

25

30

35

40

time period [day]

Fig. 9. Comparison of Predicted vs Actual Sample Paths in Time and Frequency Domains. Panels a, c and e show that

the predicted and actual sample paths are pretty close for different years, when compared over the first ✶✺✵ days of each
year. Panels b, d and f show that the Fourier coefficients match up pretty well as well. More importantly, while our models do
not explicitly incorporate any periodic elements that are being tuned, we still manage to capture the weekly, (approximately)
biweekly and longer periodic regularities.

430
431
432
433
434
435
436
437

(2014).
[37] Silver, D. & Clark, T. Scenescapes: How Qualities of Place Shape Social Life (University of Chicago Press,
2016).
[38] Nathan, R. P. & Adams, C. F. Four perspectives on urban hardship. Political Science Quarterly 104,
483–508 (1989).
[39] Granger, C. W. J. Testing For Causality. Journal of Economic Dynamics and Control 2, 329–352 (1980).
[40] University of Chicago. Crimes of prediction workshop, the neubauer collegium for culture and society.
https://neubauercollegium.uchicago.edu/events/uc/crimes of prediction workshop/ (2019).

a. Logarithmic Coefficient of Causality

b. Voronoi Decomposition with high predicting points

100
targets

sources

10−6

Fig. 10. Automatic Neighborhood Decomposition Using Event Predictability Computing a biclustering on the source-vs-

target influence matrix (panel A) isolates a set of spatial tiles that are, on average, good predictors for all other tiles. Using
this set, we use a Voronoi decomposition of the city (Panel B), which realizes an automatic spatial decomposition of the
urban space, driven by event predictability.

1

Supplementary Text: Precise Event-level
Prediction of Urban Crime Reveals Signature
of Enforcement Bias
Victor Rotaru✶❀✸ , Yi Huang✶ , Timmy Li✶❀✸ , James Evans✷❀✺❀✻ and Ishanu Chattopadhyay,✶❀✹❀✺⋆
✶ Department of Medicine, University of Chicago, Chicago, IL 60637, USA

✷ Department of Sociology, University of Chicago, Chicago, IL 60637, USA

✸ Department of Computer Science, University of Chicago, Chicago, IL 60637, USA

✹ Committee on Quantitative Methods in Social, Behavioral, and Health Sciences, University of Chicago,

Chicago, IL 60637, USA

✺ Committee on Genetics, Genomics & Systems Biology, University of Chicago, Chicago, IL 60637, USA
✻ Santa Fe Institute, Santa Fe NM 87501, USA

⋆

To whom correspondence should be addressed: e-mail: ishanu@uchicago.edu.

✦

C ONTENTS
1

Algorithm Pseudocode

1

2

Theory of Probabilistic Automata

4

3

Software Availability & Repository

6

1

A LGORITHM P SEUDOCODE

2

Algorithm 1: Granger Net
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
4
Let ①in
①s ✶♥✵ ✁ ;
✵ ;
5
Let ①out
①r ♥✁✰✶
6
Calculate PFSA ● GenESeSS ①in ❀ ✧ ;
s
7
Calculate XPFSA ❍r❀
✁ xGenESeSS ①out ❀ s✧ ;
s
8
Let ✌r❀✁ coefCausalDependence ●❀ ❍r❀
✁;
s ✕ ✌ then
9
if ✌r❀
✁ ✵
✟ s ✠
10
Let ▼r ▼r ❬ ❍r❀✁ ;
/* Learn scalar weights
11 for each target r
❀ ✿ ✿ ✿ ❀ ◆ do
✟
s ✷ ▼ ✠;
12
Let ■r
s❀
there is a model ❍r❀
r
✁
13
for each timestamp t
❀ ✿ ✿ ✿ ❀ ♥ ♥✵ do
14
Let xt be a vector with index set ■r ;
15
for each pair s❀
✷ ■r do
16
Let ①in the length ❧ sub-sequence of ①s that ends
in the ♥✵ t
-th entry;
s ❀ ① ✁;
17
Let the entry of xt s❀
predict ❍r❀
✁ in
18
Let ②t ①r ♥✵ t ;
19
Let ❳ the matrix with the t-th row being xt ;
20
Let y be the vector with the t-th entry being ②t ;
21
Initialize a suitable regressor Reg;
s ✁
22
Get scalar weights wr
✇r❀
✁ ✭s❀✁✮✷■r Reg ❳❀ y ;
23 return ❢ ▼r ❀ wr
r
❀ ✿ ✿ ✿ ❀ ◆ ❣;

✿ ❂✶
✶

✵
✁

✶

❂

✁❂✶ ✁
❂✶
❂✭ ✮
❂✭ ✮
❂
✭
❂
❂
❂
❂✶
❂ ✭ ✁✮ ✿
❂✶
✭ ✁✮
❬ ✁❪ ❂
❂ ❬ ✰❪

✭

✮✿ ❂✶

❂

*/

✶

❂✶

✮
✭
✭

✮

✮

✭ ✰

❂

✭

*/

✁✮

✮

Algorithm 2: GenESeSS
Data: A sequence ① over alphabet , ❁ ✧ ❁
Result: State set ◗, transition map ✍ , and transition probability ✙
❡
/* Step✝ One: Approximate
✧-synchronizing sequence
✞
1 Let ▲
❥✝❥ ❂✧ ;
✟ ①
✠
①
2 Calculate the derivative heap ❉✧ equaling ✣②
② is a sub-sequence of ① with ❥② ❥ ✔ ▲ ;
①
3 Let ❈ be the convex hull of ❉✧ ;
①
4 Select ①✵ with ✣①✵ being a vertex of ❈ and has the highest frequency in ①;

✝✵

❂ ❧♦❣ ✶

✶

*/

❫ ✿

❫

/* Step Two: Identify transition structure
*/
5 Initialize ◗
❢ q✵ ❣ ;
id
6 Associate to q✵ the sequence identifier ①q✵
①✵ and the probability vector ❞q✵ ✣①①✵ ;
❡ be the set of states that are just added and initialize it to be ◗;
7 Let ◗
❡ , ❀ do
8 while ◗
9
Let ◗new ❀ be the set of new states;
❡ ✂ do
10
for q❀ ✛ ✷ ◗
①
11
Let ① ①id
q and ❞ ✣①✛ ;
12
if ❦❞ ❞q✵ ❦✶ ❁ ✧ for some q ✵ ✷ ◗ then
13
Let ✍ q❀ ✛
q✵ ;
14
else
15
Let ◗new ◗new ❬ ❢qnew ❣ and ◗ ◗ ❬ ❢qnew ❣;
16
Associate to qnew the sequence identifier ①id
①✛ and the probability vector ❞qnew ❞;
qnew
17
Let ✍ q❀ ✛
qnew ;
❡ ◗new ;
18
Let ◗
19 Take a strongly connected subgraph of the labeled directed graph defined by ◗ and ✍ , and denote the vertex set of
the subgraph again by ◗;
/* Step Three: Identify transition probability
*/
20 Initialize counter ◆ q❀ ✛ for each pair q❀ ✛ ✷ ◗ ✂ ;
21 Choose a random starting state q ✷ ◗;
22 for ✛ ✷ ① do
23
Let ◆ q❀ ✛
◆ q❀ ✛
;
24
Let q q
✍ q❀ ✛ ;
y
25 Let ✙
❡ q
◆ q❀ ✛ ✛✷✝ ;
26 return ◗, ✍ , ✙
❡;

❂

✭ ✮

❂

❂❫

❂

❂

❂

✝

❂❫

✭ ✮❂
❂
✭ ✮❂

❬ ❪

❬ ❪❂ ❬ ❪✰✶
❂ ✭ ✮
✭ ✮ ❂ ✭ ❬ ❪✮

❂

✭ ✮

❂

✝

❂

3

Algorithm 3: xGenESeSS
Data: A sequence ①in over alphabet ✝in , a sequence ①out over alphabet ✝out , and ✵ ❁ ✧ ❁ ✶
Result: State set ❘, transition map ✑ , and output probability ✤
/* Step✝ One: Approximate
✧-synchronizing sequence
✞
1 Let ▲ ❂ ❧♦❣❥✝ ❥ ✶❂✧ ;
in
✟
✠
①in ❀①out
2 Calculate cross derivative heap ❉✧
equaling ✣❫②①in ❀①out ✿ ② is a sub-sequence of ①in with ❥② ❥ ✔ ▲ ;

*/

Let ❈ be the convex hull ❉✧①in ❀①out ;
❫①①✵in ❀①out being a vertex of ❈ and has the highest frequency in ①;
4 Select ①✵ with ✣
/* Step Two: Identify transition structure
*/
5 Initialize ❘ ❂ ❢r✵ ❣;
id
❫①①✵in ❀①out ;
6 Associate to r✵ the sequence identifier ①r✵ ❂ ①✵ and the probability vector ✤ ✭r✵ ✮ ❂ ✣
❡ be the set of states that are just added and initialize it to be ❘;
7 Let ❘
❡ , ❀ do
8 while ❘
9
Let ❘new ❂ ❀ be the set of new states;
❡ ✂ ✝in do
10
for ✭r❀ ✛ ✮ ✷ ❘
①in ❀①out
❫①✛
11
Let ① ❂ ①id
;
r and ❞ ❂ ✣
✵
12
if ❦❞ ✤ ✭r ✮❦✶ ❁ ✧ for some r✵ ✷ ❘ then
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
19 Take a strongly connected subgraph of the labeled directed graph defined by ❘ and ✑ , and denote the vertex set of
the subgraph again by ❘;
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
Let r ❂ ✑
r ✭r❀ ✛✐ ✮;
z
26 Let ✤ ✭r ✮ ❂ ✭◆ ❬r❀ ✜ ❪✮✜ ✷✝
;
out
27 return ❘, ✑ , ✤;
3

4

2

T HEORY OF P ROBABILISTIC AUTOMATA

Granger Net is assembled from local models which are, in general, crossed probabilistic automata (XPFSA).
The construction of a Granger Net consists of two steps: 1) local model generation and network pruning and 2)
local model aggregation for comprehensive prediction. Event prediction is accomplished by aggregating these local
activations via a local regressor. No global optimization of these aggregation function is acrried out.
The model generation step of Granger Net is accomplished by the algorithms GenESeSS (See Algorithm 2) and
xGenESeSS (See Algorithm 3). xGenESeSS produces XPFSA models that captures how the history of a source
process influences the future of a target process. The Granger Net construction is described in Algorithm 1, and takes
as input a set ①s s ❙ of length-♥ time series, hyperparameters ✧ and ♥✵ ❁ ♥ for local model inference, max for
maximum time delay, and ✌✵ for thresholding admissible models. For each target sequence ①r , Granger Net outputs a
set of admissible models
r with a scalar weight for each model in
r via model inference and pruning (line 1-10)
and training of the aggregation weights (line 11-22).

❢ ✿ ✷ ❣
▼

✁

▼

Step 1: Model inference and pruning
The Granger Net framework models the influence from a source time series ①s on a target time series ①r at a particular
s
time delay
by an XPFSA ❍r❀
✁ (line 7). Thus, we infer ❙ max XPFSA models for each ①r which yields ❙ ✷ max
models in total. Since the number of XPFSA models increases quadratically with the number of time series and strength
of the links may vary, pruning low-performing models early is important for parsimony. Granger Net rejects models by
s
thresholding on the coefficient of causal dependence ✌r❀
✁ of model ❍r❀s ✁ (line 8), which measures the strength of
dependence of the output sequence on the input one. More specifically, we have
uncertainty of the next output in ①r with observation of ①s
s
✌r❀
(1)
✁
uncertainty of the next output in ①r
✌ can be evaluated from the synchronous composition of the PFSA that models the input process (line 6) and the
s
XPFSA that models the causal influence. Granger Net retains the model ❍r❀
✁ if and only if ✌r❀s ✁ is greater than a
pre-specified threshold ✌✵ . At the conclusion of Step 1, Granger Net returns an admissible set of models

✁

❥ ❥✁

❥ ❥✁

❂✶

✟

for each r

▼ ❂ ❍ ✁ ✿ ✌ ✁ ❃ ✌✵
r

✷ ❙.

s
r❀

s
r❀

✠

(2)

Step 2: Train linear weights
In this step, we integrate the local models in ①r ’s admissible set for forecasting events in ①r . To do this, Granger Net
s
trains a linear coefficient ✦r❀
r (line 22) so that the final prediction for ①r at time step ❤ is equal to
✁ for each ❍r❀s ✁

✷▼
❳

✭ ✮ ✁

s
r❀

❍

✁ ✷▼

✁

✦t❀s ✁ ❍r❀s ✁

✏

✑

✭① ✮ ✁ ❀
❤

(3)

s

r

✭

✮

where ①s
is the truncation of ①s at ❤
. To compute the coefficients, we solve a regression problem Reg ❳❀ y
(line 22) for each r
❙ with the predictor variables being predictions xt s❀
obtained by running each sequence
①s ♥✵ ✰t ✁ through ❍r❀s ✁ (line 17), and the outcome variable being ①r ♥✵ t , value of ①r at time ♥✵ t (line 18).
Hence, the ❳ matrix is the ♥ ♥✵
matrix with the entry indexed by t❀ s❀
given by xt s❀
and y, the
r
♥ ♥✵ -dimensional vector with the entry indexed by t given by ①r ♥✵ t . We can solve for the linear weights with
any standard regressor.
❤

✭ ✮
✭
✮

✷

✭

✮ ✂ ❥▼ ❥

❬ ✁❪
❬ ✰❪
✭ ✁✮
❬ ✰❪

✰
❬ ✁❪

Inference Algorithms
On line 6 and 7 of Algorithm 1, Granger Net calls subroutine xGenESeSS, which infers XPFSA as models of crossdependencies between processes. Here, we establish the correctness of GenESeSS.
The inference algorithm for PFSA is called GenESeSS for Generator Extraction Using Self-similar Semantics. The PFSA
model is based on the concept of the causal state. A dynamical system reaches the same causal state via distinct paths
if the futures are statistically indistinguishable. More precisely, each process over an alphabet of size ♠ gives rise
naturally to an ♠-ary tree with the nodes at level ❞ being sequences of length ❞, and the edge from the node ① to ①✛ ,
✛
, labeled by P r ✛ ① – the probability of observing ✛ as the next output after ①. By the definition of causal state, if
two subtrees are identical with respect to edge labels, then their roots are sequences that lead the system to the same
causal state. Identifying all the roots of identical subtrees induces a finite automaton structure whose unique strongly
connected component is the generating model of the process.

✝

✷✝

✭❥✮

✭ ✝

✮

Definition 1 (Probabilistic Finite-State Automaton (PFSA)). A PFSA ● is a quadruple ◗❀ ❀ ✍❀ ✙
❡ , where ◗ is a finite
set, is a finite alphabet, ✍ ◗
is called the transition map, and ✙
❡ ◗ P✝ , where P✝ is the space of
probability distributions over , is called the transition probability.

✝

✿ ✂✝ ✦ ✝
✝

✿ ✦

Step 2 of Algorithm 2 (line 5-19) is an implementation this subtree “stitching” approach under finiteness of input data.

5

Note that the criterion for “stitching” two subtrees with roots ① and ①✵ is that their edge labels are identical for all depths,
which translates to ♣✭② ①✮ ❂ ♣✭② ①✵ ✮ for sequence ② of all lengths. The criterion is not verifiable with finite data, and
hence GenESeSS identifies two subtrees if they agree on depth one. Defining symbolic derivative ✣① to be the vector
with the entry indexed by ✛ given by ♣✭✛ ①✮, GenESeSS identifies ① and ①✵ if ✣① ❂ ✣①✵ . This approach works well under
the assumption that the target PFSA is in general position, meaning that different causal states have distinct symbolic
derivatives. In practice, GenESeSS uses empirical symbolic derivative defined below to approximate ✣① . Let ① be an
input sequence of finite length, the empirical symbolic derivative ✣❫①② of a sub-sequence ② of ① is a probability vector
with the entry indexed by ✛ given by
number of ②✛ in ①
✣❫①② ✭✛ ✮ ❂
(4)
number of ② in ①
GenESeSS identifies two sequences (line 12) if their empirical symbolic derivatives are within an ✧-neighborhood of
each other for certain ✧ ❃ ✵.

❥

❥

❥

For simplicity, we first illustrate how GenESeSS solves the transition structure of the target PFSA from a sample path ①
generated from a process of Markov order ❦. Assuming the ①✵ produced by Step 1 (line 4) is ✕, the empty sequence,
GenESeSS starts by calculating ✣❫①✕ , ✐✿❡✿, the empirical distribution on ✝, and records ✕ as the identifier of the first state.
Then, GenESeSS appends ✕ with each ✛ ✝, and calculates ✣❫①✛ . By the general position assumption and assuming ①
is long enough, with high probability, no ✣❫①✛ is within an ✧-neighborhood of ✣❫①✛✵ for ✛ , ✛ ✵ , and hence each ✛ is recorded
as the identifier for a new state. In fact, GenESeSS will keep on appending symbols to identifiers of stored states and
adding new states until it reaches a sequence of length ❦ ✰✶. Assuming ② ❂ ✛✶
✛❦ ✛❦✰✶ , since the process is of order
❦, we have ✣② ❂ ✣③ for ③ ❂ ✛✷
✛❦✰✶ , and hence, with high probability, ✣❫①② and ✣❫①③ can be within an ✧-neighborhood
of each other given long enough input ①. In this case, GenESeSS identifies the state represented by ② with that of ③ . In
fact, GenESeSS will identify all states represented by sequences of length ❦ ✰ ✶ to some previously-stored states. And
since no new states can be found, GenESeSS exits the loop on line 8 after iteration ❦ ✰✶. Taking the strongly connected
component on line 19, GenESeSS gets the correct transition structure.

✷

✁✁✁

✁✁✁

However, not all processes generated by PFSA have finite Markov order. For such cases, Step 2 of GenESeSS will
never exit in theory, since there exists no ♥ N such that every causal state is visited for sequences with length ♥.
And if we implement an artificial exit criterion, the model inferred might be unnecessarily large, and have hard-to-model
approximations. We address this issue via the notion of synchronization – the ability to identify that we are localized or
synchronized to a particular state despite being uncertain of the initial state.

✷

✔

In Step 1 of Algorithm 2 (line 1-4), GenESeSS finds an almost synchronizing sequence, which allows GenESeSS to distill
a structure that is similar to that of the finite Markov order cases, and thus carry out the subtree “stitching” procedure
described before. A sequence ① is synchronizing if all sequences that end with the suffix ① terminates on the same
causal state. A process is synchronizable if it has a synchronizing sequence, and a PFSA is synchronizable if the
process it generates is synchronizable. The structure of the “graph” of a perfectly synchronizable PFSA is that of a
co-final automata 1 .
A sequence ① is ✧-synchronizing 2 to the state q if the distribution ⑥① on the state set ◗ induced by ① satisfies
⑥① eq ✶ ❁ ✧, where eq is the base vector with ✶ on the entry indexed by q and ✵ elsewhere. The importance of ✧❡ , where ✆
❡ is the ◗ ✝ matrix with the row indexed by q given
synchronizing sequence is twofold: 1) since ✣❚① ❂ ⑥❚① ✆
by ✙
❡ ✭q ✮, a ⑥① close to eq give rise to a ✣① close to ✙❡ ✭q ✮. And 2) although sequences prefixed by an ✧-synchronizing
sequence to a state q may not remain ✧-synchronizing to state q , they are close to q on average.

❦

❦

❥ ❥✂❥ ❥

To find an almost synchronizing sequence algorithmically 2 , GenESeSS first calculates the convex hull of symbolic
derivatives of subsequences of ① up to length ▲ (line 1-3), and✟then selects ✠
a sequence ①✵ whose symbolic derivative
is a vertex of the convex hull (line 4). Since the convex hull of ✣① ✿ ① ✝▲
is a linear projection of the convex hull
✠
✠
✟
✟
✆, we can expect sequence ① with ✣① being a vertex of the convex hull of ✣① ✿ ① ✝▲ to be
⑥● ✭①✮ ✿ ① ✝▲ via ❡
a good candidate for an almost synchronizing sequence.

✷

✷

✷

The corresponding inference algorithm for XPFSA is called xGenESeSS, which takes as input two sequences ①in , ①out ,
and a hyperparameter ✧, and outputs an XPFSA in a manner very similar to the inference algorithm of PFSA.
While a PFSA models how the past of a time series influences its own future, a XPFSA models how the past of an
input time series influences the future of an output time series. Hence, while in the SSC algorithm of PFSA, we identify
sequences if they lead to futures that are statistically indistinguishable, in the SSC algorithm of XPFSA, we identify
sequences if they lead to the same future distribution of the output.
Definition 2 (Crossed Probabilistic Finite-State Automaton (XPFSA)). A crossed probabilistic finite-state automaton
is specified by a quintuple ✭✝in ❀ ❘❀ ✑ ❀ ✝out ❀ ✤✮, where ✝in is a finite input alphabet, ❘ is a finite state set, ✑ is a partial
function from ❘ ✝in to ❘ called transition map, ✝out is a finite output alphabet, and ✤ is a function from ❘ to P✝out
called output probability map, where P✝out is the space of probability distributions over ✝out . In particular, ✤✭r❀ ✜ ✮ is the
probability of generating ✜ ✝out from a state r ❘.

✂

✷

✷

Note that a XPFSA has no transition probabilities defined between states as a PFSA does. The XPFSA in the example

6

has a binary input alphabet and an output alphabet of size ✸. The bar charts next to the ✹ states of the XPFSA indicate
the output probability distributions. To generate a sample path, an XPFSA requires an input sequence over its input
alphabet.
Similar to the PFSA construction approach, here we compute the cross symbolic derivative, which is the ordered tuple
P r ✭✜ ❥①✮, with ✜ ✷ ✝out and a sequence ① over ✝in . We compute the empirical approximation of the cross symbolic
derivative from sequences ①in and ①out as:
❫②①in ❀①out ✭✜ ✮ ❂ number of ✜ in ①out after ② transpires in ①in
✣
(5)
number of sub-sequence ② in ①in
Thus, xGenESeSS is almost identical to GenESeSS except that, in Step 1, xGenESeSS finds an almost synchronizing
sequence based on cross symbolic derivatives, and in Step 2, identifies the transition structure based on the similarity between cross symbolic derivatives. Arguments for establishing the effectiveness of GenESeSS carry over to
xGenESeSS with empirical symbolic derivative replaced by empirical cross symbolic derivative.

3

S OFTWARE AVAILABILITY & R EPOSITORY

Software for the cynet implementation, with instructions for installation and quick-start examples, is available at
https://pypi.org/project/cynet/

R EFERENCES
[1] Ito, M. & Duske, J. On cofinal and definite automata. Acta Cybernetica 6, 181–189 (1983).
[2] Chattopadhyay, I. & Lipson, H. Abductive learning of quantized stochastic processes with probabilistic finite
automata. Philos Trans A 371, 20110543 (2013).

Figures

Figure 1
Crime Data & Modeling Approach. a and b show the recorded infractions within the 2 week period
between April 1 and 15 in 2017. Plate c illustrates our modeling approach: We break city into small
spatial tiles approximately 1.5 times the size of an average city block, and compute models that capture

multi-scale dependencies between the sequential event streams recorded at distinct tiles. In this paper, we
treat violent and property crimes separately, and show that these categories have intriguing crossdependencies. Plate d illustrates our modeling approach. For example, to predict property crimes at some
spatial tile r, we proceed as follows: Step 1) we infer the probabilistic transducers that estimate event
sequence at r by using as input the sequences of recorded infractions (of different categories) at
potentially all remote locations (s; s 0 ; s 00 shown), where this predictive in uence might transpire over
different time delays (a few shown on the edges between s and r). Step 2) Combine these weak
estimators linearly to minimize zero-one loss. The inferred transducers can be thought of as inferred local
activation rules, which are then linearly composed, reversing the approach of linearly combining input
and then passing through xed activation functions in standard neural net architectures. The connected
network of nodes (variables) with probabilistic transducers on the edges comprises the Granger Network.

Figure 2
Predictive Performance of Granger Nets. a an b illustrate the out-of-sample area under the receiver
operating characteristics curve (AUC) for predicting violent and property crimes respectively. The
prediction is made a week in advance, and the event is registered as a successful prediction if we get a hit
within +1 day of the predicted date. c illustrates the distribution of AUC on average, individually for violent
and property crimes. Our mean AUC is close to 90%. Panels d-f shows in uence Diffusion & Perturbation

Space. If we are able to infer a model that is predicts event dynamics at a speci c spatial tile (the target)
using observations from a source tile + days in future, then we say the source tile is within the in uencing
neighborhood for the target location with a delay of D. d illustrates the spatial radius of in uence for
0.5, 1, 2 and 3 weeks, for violent (upper panel) and property crimes (lower panel). Note that the
in uencing neighborhoods, as de ned by our model, are large and approach a radius of 6 miles. Given
the geometry of the City of Chicago, this maps to a substantial percentage of the total area of urban
space under consideration, demonstrating that crime manifests demonstrable long-range and almost
city-wide in uence. e illustrates the extent of a few inferred neighborhoods at time delay of at most 3
days. f illustrates the average rate of in uence diffusion measured by number of predictive models
inferred that transduce in uence as we consider longer and longer time delays. Note that the rate of
in uence diffusion falls rapidly for property crimes, dropping to zero in about a week, whereas for violent
crimes, the in uence continues to diffuse even after three weeks.

Figure 3
Estimating Bias. a illustrates the distribution of hardship index (see SI). c, d, e, and f suggest biased
response to perturbations in crime rates. With a 10% increase in violent or property crime rates, we see an
approximately a 30% decrease in arrests when averaged over the city. The spatial distribution of locations
that experience a positive vs. negative change in arrest rate reveals a strong preference favoring wealthy
locations. If neighborhoods are doing better socio-economically, increased crime predicts increased
arrests. A strong converse trend is observed in predictions for poor and disadvantaged neighborhoods,

suggesting that under stress, wealthier neighborhoods drain resources from their disadvantaged
counterparts. b illustrates this more directly via a multi-variable regression, where hardship index is seen
to make a strong negative contribution.

Figure 4
Prediction of property and violent crimes across major US cities and dependence of perturbation
response on socio-economic status of local neighborhoods. Panels a-f illustrate the AUCs achieved in six

major US cities. These cities were chosen on the basis of the availability of detailed event logs in the
public domain. All of these cities show comparably high predictive performance. Panel g illustrates the
results obtained by regressing crime rate and perturbation response against SES variables (shown here
for poverty, as estimated by the 2018 US census). We note that while crime rate typically goes up with
increasing poverty, the number of events observed one week after a positive perturbation of 5-10%
increase in crime rate is predicted to fall with increasing poverty. We suggest that this decrease is
explainable by reallocation of enforcement resources disproportionately, away from disadvantaged
neighborhoods in response to increased event rates, which leads to smaller number of reported crimes.

Figure 5
Perturbation Effects Across Variables. We see that the decrease of violent crimes from increase of
property crimes are localized in disadvantaged neighborhoods (panel g). Similarly, the decrease of
property crimes from increase of violent crimes is also localized to disadvantaged neighborhoods (panel
a), as well as the decreased violent crimes from increased arrests (panel k). We see a weaker localization
for the corresponding increases in crime rates under similar perturbations. Looking at other pairs of

variables under perturbation (rest of the panels), we generally do not see a very prominent
correspondence with the distribution of socio-economic indicators. It seems crimes (and particulalrly
violent crimes) are easier to dampen in lcales with high existing crime rates, which is desirable result. But
such conclusions are currently confounded by SES variables, and futher work is needed to investigate
these effects more thoroughly.

Figure 6
Stability of Suburban Bias over Years (Violent Crimes). We show that the nature of the perturbation
response shown in Fig. 3 in the main text holds true for earlier years as well: panels a and b correspond to
year 2014, c and d correspond to 2015 and e and f correspond to year 2016, all of which follow the same
pattern shown in Fig. 3 in the main text.

Figure 7
Stability of Suburban Bias over Years (Property Crimes). We show that the nature of the perturbation
response shown in Fig. 3 in the main text holds true for earlier years as well: panels a and b correspond to
year 2014, c and d correspond to 2015 and e and f correspond to year 2016, all of which follow the same
pattern shown in Fig. 3 in the main text.

Figure 8
Out of Sample Predictive Performance over the Years. We show that the predictive performance is very
stable, and variation in mean AUC is limited to the third place of decimal, at least when analyzing the last
few years (4 years shown).

Figure 9
Comparison of Predicted vs Actual Sample Paths in Time and Frequency Domains. Panels a, c and e
show that the predicted and actual sample paths are pretty close for different years, when compared over
the rst 150 days of each year. Panels b, d and f show that the Fourier coe cients match up pretty well
as well. More importantly, while our models do not explicitly incorporate any periodic elements that are
being tuned, we still manage to capture the weekly, (approximately) biweekly and longer periodic
regularities.

Figure 10
Automatic Neighborhood Decomposition Using Event Predictability Computing a biclustering on the
source-vs-target in uence matrix (panel A) isolates a set of spatial tiles that are, on average, good
predictors for all other tiles. Using this set, we use a Voronoi decomposition of the city (Panel B), which
realizes an automatic spatial decomposition of the urban space, driven by event predictability.
