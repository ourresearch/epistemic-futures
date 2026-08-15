---
title: "‘Its the Economy Stupid’: Predictive Theory of Belief Shift Connecting Economic Stress to Societal Polarization"
person: james-evans
section: by
type: journal-article
year: 2023
date: 2023-03-08
venue: "Research Square"
authors: "David Yang, James EVans, Ishanu Chattopadhyay"
source_url: https://doi.org/10.21203/rs.3.rs-2653650/v1
openalex_id: https://openalex.org/W4323349152
retrieved: 2026-08-13
content: full-text
notes: "preprint version; full text via the OpenAlex Content API (content.openalex.org)"
---

# ‘Its the Economy Stupid’: Predictive Theory of Belief Shift Connecting Economic Stress to Societal Polarization

## Full text

‘Its the Economy Stupid’: Predictive Theory of Belief
Shift Connecting Economic Stress to Societal
Polarization
David Yang (  davidyangnyc@gmail.com )
University of Chicago
James EVans (  jevans@uchicago.edu )
University of Chicago
Ishanu Chattopadhyay (  ishanu@uchicago.edu )
University of Chicago https://orcid.org/0000-0001-8339-8162

Research Article
Keywords: polarization, machine learning, belief shift
DOI: https://doi.org/10.21203/rs.3.rs-2653650/v1
License:   This work is licensed under a Creative Commons Attribution 4.0 International License.
Read Full License

1

‘Its the Economy Stupid’: Predictive Theory of
Belief Shift Connecting Economic Stress to
Societal Polarization
David Yang✶❀✸ , James Evans✷❀✹❀✻ and Ishanu Chattopadhyay,✶❀✹❀✺⋆
✶ Department of Medicine, University of Chicago, Chicago, IL 60637, USA

✷ Department of Sociology, University of Chicago, Chicago, IL 60637, USA

✸ Department of Computer Science, University of Chicago, Chicago, IL 60637, USA

✹ Committee on Quantitative Methods in Social, Behavioral, and Health Sciences, University of Chicago,

Chicago, IL 60637, USA

✺ Committee on Genetics, Genomics & Systems Biology, University of Chicago, Chicago, IL 60637, USA
✻ Santa Fe Institute, Santa Fe NM 87501, USA

⋆

To whom correspondence should be addressed: e-mail: ishanu@uchicago.edu.

One Sentence Summary: Computational inference of emergent dependencies across opinions from
society-wide surveys to objectively measure polarization mechanics and its drivers.
Abstract: Despite growing concerns about increasing societal polarization, its mechanics remain unclear.
A lack of consensus in how to measure and analyze polarization, that takes more than a few hand-picked
variables into consideration, have hindered progress. Our new framework (CogNet) computationally
distills emergent dependencies between diverse opinions, which then allow us to infer ‘digital twins of
society-wide survey responses. In addition to enabling reliable opinion prediction at the individual level
to thousands of controversial questions, CogNet allows us to objectively assess societal polarization
from social survey data. Analyzing ❃ ✻✺❑ US respondents from the General Social Survey, and ❃ ✸✿✾▼
European Union participants from the Eurobarometer over half a century, here we provide new evidence
that faltering economies forecast greater polarization, and that affective polarizationis a precursor to
ideological polarization, yielding insight into how cultural clusters fragment with economic stress,
leading to widening gaps between dominant ideologies.

M AIN T EXT
Introduction

T

HE emergence of prominent mis- and disinformation campaigns to influence the political landscape have
highlighted the importance of capturing how opinions evolve across society. Isolating mechanisms that
modulate societal polarization is crucial for social theory, but also to design effective social policies and support
stable democracy. In this study, we begin by developing a computational framework to reliably predict opinions
from incomplete information, based on cross-cutting dependencies between opinions held across society. The
predictive ability of our approach fosters new tools that we validate for the measurement and analysis of evolving
opinion structures, societal polarization and the influences that drive them (Fig. 1a).
Highly polarized societies are generally deemed unhealthy 1 , becoming progressively hostile towards opposing
political or social groups (affective polarization), often adopting increasingly extreme and discriminating positions
on policy questions (ideological polarization). While specific attitudes have long been quantified through survey
elicitation, emergent ideological distinctions are inherently difficult to quantify as they cross multiple positions and
opinions. As a result, simple, effective measures to track polarization have been challenging to devise, despite
widespread interest 2–13 . General claims regarding polarization and its measurement 14,15 have as yet provided
unclear practical value for informing policy.
Attempts to “explain” polarization through mechanistic models have also had limited success, rarely using detailed
empirical patterns of opinion to inform assumed rules of belief shift. Various mechanics of imitation, influence
from, and communication with “social neighbors” have been assumed to modulate beliefs, but a lack of global
consensus in social systems suggests that more is at play 14,15 . These models often attempt to capture broad
characteristics of opinion dynamics reflecting simulated processes of network diffusion 16,17 . Such models predict
clustered diffusion better than opinions held by particular individuals on specific topics, and were not designed

2

to capture cross-cutting influences between the structure of society-wide opinions on the evolving distribution of
those held by individuals. Personalized information filtering 18 on social media has also been investigated as a
promoter of polarization with mixed results 19–23 , and experiments that demonstrate how increased exposure to
opposing views might make polarization worse 24 hint at mechanisms that violate patterns of simple diffusion.
The other popular approach, agent-based simulation 25–27 , has been used to explore progressive polarization by
creating artificial worlds mimicking desired characteristics. For example, self-reinforcing dynamics of influence
and homophily have been shown to drive “tipping points” that irreversibly polarize legislative bodies 28 . However,
in reality, agent models 26,29 and differential equations 30 are defined into existence as models that yield logically
sufficient but not necessary explanations. Such studies corroborate the plausibility of theoretically inspired agent
rules through coarse-grained similarity between model outcomes and specific political events 28 or stylized facts
about the world like segregation 31 .

The CogNet Framework
Here we take a new approach based on pattern discovery, aiming to computationally learn the emergent
dependencies across opinions and beliefs from society-wide social survey data, which allow us to assemble
a generative model – a digital twin – of survey datasets on opinions and beliefs. We call this model the CogNet.
A inferred CogNet can reliably predict opinions on thousands of controversial questions for specific individuals
from very limited a priori worldview information. This predictive capability allows us to formulate new objective
measures of polarization, and statistically probe the roles of different putative factors (See Fig. 1a for overall
scheme).
Leveraging inferred data-driven dependencies to identify dynamical processes 32 , our approach avoids some
concerns regarding agent-based simulation validation, such as the source of theoretical principles and the match
with outcomes alone. Our model does not assume rules and receives validation through individual-level prediction
on out-of-sample data. Thus our findings offer a complement to social “tipping point” hypotheses by accounting
for the thicket of dependencies between opinions across society. In effect, we encompass nonlinear “tipping
point” dynamics, along with many other functional forms and forces, from data on the interdependent system
of opinions, as they intersect within people across a society. Our finding that economic downturns anticipate
increased societal polarization contributes inspired our title, coined by political strategist James Carville in 1992
as the cornerstone for U.S. President Bill Clinton’s successful campaign against George H. W. Bush during a
recession economy.
Political polarization among US legislators and other decision-making organizations has received extensive
research attention 33 , but polarization in the general population remains relatively under-explored. This arises
partly from a lack of consensus around how to conceptualize and measure societal polarization. Some have
assessed it with fixed questions, but these may shift away from the axis of polarity 3 . Our study eliminates this
limitation, which has risen in importance as public opinion about seemingly innocuous topics, holding no semantic
or logical association with political affiliation, has become critical for differentiating political and social groups 30 .
Still others have assessed polarization through “influence” variables, like political party affiliation, which is often
assumed to drive cleavages in other dimensions, resulting in a self-reinforcing information echo-chambers 34,35 .
But influence may flow in multiple directions, from behaviors to ideas as from ideas to behaviors 36,37 . Instead,
we embed the entire societal space of opinions and derive a sociologically meaningful distance that varies
with the inferred CogNets – known as the CogNet-distance– between respondents’ raw opinion vectors, that
automatically accounts for emergent groups and network-effect blind-spots.
Thus, our approach is centered around the construction of first a generative model, and then a robust, intrinsically
meaningful metric induced by the model, for comparing and contrasting sets of opinions between pairs of
individuals. Importantly, opinions do not exist in a vacuum, but are embedded within a fluid background of
social and cultural constraints and emergent linkages, and the CogNet framework reflects these constraints via
its inferred dependencies. Importantly, some dependencies are trivial to intuit and anticipate, but others have
more subtle structure or violate historical expectations, and we both theorize and measure how opinions on
distinct topics are rarely independent.
Additionally as these dependencies between opinions can and do evolve over time, our optimal metric of
comparison, computed as a function of the inferred dependencies, evolves as well (Fig. 1b). And the ability
of the inferred CogNet to predict opinions on unobserved queries provides a path to objective validation: we set
aside a set of survey participants as out-of-sample participants during CogNet training, and then mask all but
20% of their recorded responses, and test the capability of the inferred CogNet to reconstruct these responses
correctly (Fig. 1c). Ultimately, this validated predictive capability suggests new objective measures of ideological
and affective polarization (polar separation, embedding diameter, cluster separation and cluster numerosity) that
may be computed from society-wide surveys (Fig. 1d).

3

CogNet Construction & Validation
Prior to the derivation of the optimal metric for opinion comparison, we must infer the CogNet. Structurally, a
CogNet comprises a set (“forest”) of interdependent decision trees. The individual trees are constructed with
statistically discriminant node splits (✐✿❡✿ they are conditional inference trees 38 , that carry out statistical tests
to ensure that each split qualifies above a preset level of significance). Given a survey dataset, we proceed
as follows: For each query item, we learn a distinct tree to predict the responses to this item (which may be
categorical, polytomic or numerical), as a function of responses to the remaining query items in the survey.
In this manner, we infer tree models for each of the query items in the survey. Thus, the predictive features
selected in one tree (modeling one query item) are themselves predicted ✐✿❡✿ are target labels for other trees and
vice versa, resulting in a recursive forest – in the sense that each non-leaf node in any tree can be “expanded”
to a tree itself (See Fig. 2). The overall CogNet represents a detailed and nearly assumption-free model of
conditional cross-dependencies between responses to different survey items (Supplementary Fig. 1).
To concretely elucidate the CogNet construction, note how the tree inferred for the variable “prayer” in the 2018
GSS survey (Fig. 2b) is inferred to use a variety of features, which are themselves other GSS variables, including
“bible”, “god” , “natsoc” and “fefam”. Each of these features (appearing in the non-leaf nodes) can be expanded
to its own inferred tree. We show this expansion of the “fefam” variable, which is seen to be dependent on other
variables including “hubbywork” and “fechld”. It is unavoidable that we would encounter cycles in this approach,
and in Fig. 2a we show some of these emergent cyclic relationships between variables, where variable A
variable B implies that the predictor for variable B uses variable A as a feature.

✦

In this study, we demonstrate the CogNet inference, our polarization analysis and conclusions, on the General
Social Survey and Eurobarometer datasets over the last half century. The GSS provides a rich window into
the opinions and beliefs held by the US populace between 1972-2021, documenting 31,670,949 responses to
6,209 unique query items from n=65,784 US residents. The year-specific CogNets inferred from the GSS data
informs us how to appropriately measure deviations in opinions, modulating the corresponding CogNet-distance
function mapping pairs of opinion vectors to a positive number (the CogNet-distance) between opinion vectors.
We replicate the key claims made here with the Eurobarometer: the official polling instrument used by the
European Parliament, the European Commission and other EU institutions and agencies to annually monitor
the state of public opinion across Europe. Eurobarometer is conducted every 6 months, and approximately 1,000
citizens from each EU country are polled. We have public access to 235 surveys (as of writing, July 2022), with
a total of ✸❀ ✾✽✵❀ ✷✹✹ participants, and an average number of ❃ ✺✵✵ questions per survey (Supplementary Table I).

Objective Measures of Polarization
Human-solicited survey data is imperfect, and within our framework, individuals are represented by opinion
vectors that can and often do contain missing responses. To compute the distance between two individuals from
their partially populated opinion vectors, it is insufficient to specify their opinions in isolation; we must note the
historical moment in which these opinions were recorded. As the social and cultural background evolves over
time, we can demonstrate that the distance between two extreme opinion vectors can vary solely because of
the time-dependence of socio-cultural structures, reflected in the inferred CogNets. Thus, the distance between
two opinion vectors can change if either opinion changes, if the norms, beliefs and environment evolve around
fixed opinions, or both. While numerous definitions of legitimate “distance”s are conceivable, the CogNet-distance
between two opinion vectors is canonical in representing the simplest metric distance function, and we show that
the CogNet-distance between two opinion vectors ①❀ ② scales as the log-likelihood of a spontaneous opinion shift
from ① to ② (Theorem 1 in Supplementary methods). This information-theoretic property, established explicitly,
induces a range of theoretically interpretable and efficiently computable measures of polarization, which in turn
allow us to uncover key insights into the mechanics of polarization in U.S. and global society.
Specifically, if we can measure variation in the distance between extreme, fixed opinion vectors – ideological
“poles” – then we can measure ideological polarization by computing the distance between them. In the context
of U.S. society, we consider two poles, namely the ultra-conservative and ultra-liberal response sets to a fixed set
of socially contentious query items (Table I). These responses are not given by any one individual, but represent
intuitively the extreme opinion sets in this context. Additionally, variations in the exact query items used to define
the poles do not change our conclusions. The time-dependent distance between these polar vectors, referred to
as polar separation, then measures the log-likelihood of spontaneous change from one to the other. The larger
this distance, the harder it is to “bridge” the divide, the greater degree of ideological polarization. Our model also
proposes a complementary measure of ideological polarization, referred to as the embedding diameter. Unlike
polar separation, which captures the distance between fixed poles, embedding diameter estimates the greatest
distance between opinion vectors observed at a given time within a sub-sample of respondents. Thus, while
polar separation measures the distance between a theoretical pair of extreme opinions, diameter measures the
distance between observed pairs of extreme opinions.

4

a. Conceptual framework

dependencies

r
ila s Q1. yes
Q2. no
sim view
Q3. agree
rld ch
wo wit le

cognet
model

`

q-distance

Raw survey
responses

b. Measuring distance between worldviews

Q1. yes
Q2. no
Q3. strongly
agree
...

Intrinsic
distance
between
opinions

s sib
s
po

p1.

Q1. no
Q2. yes
Q3. strongly
disagree
...

...

p2.

p3.

switch unlikely

c. Worldview reconstruction

Dependency structure evolves

missing
responses

individual opinion
change

learned model

Allows
quantitative
validation

d. Generalizable polarization metrics induced by the cognet framework
cluster
separation

embedding
diameter

Number of
clusters

ric
et
m
ing
al
iet edd
c
so mb
e

liberal pole

ideological measure
affective measure

conservative pole

polar separation
Fig. 1. Conceptual framework. Panel a illustrates that the CogNet architecture infers a model of dependencies between

opinions, beliefs and demographic variables from raw survey data, without any apriori assumptions on the structure of
such inferred reltionships. These dependencies are inferred as a recursive forest of conditional inference trees, known as a
CogNet. The inferred CogNet induces an distance between any two possibly partially populated opinion vectors, and can
be shown to scale approximately as the log-likelihood of spontaneous transition between two distinct belief vectors, thus
making the CogNet-distance a naturally meaningful metric on the space of opinions. Panel b illustrates that we can infer a
CogNet specific to different time-periods, ❡✿❣✿ year of a GSS survey, implying we can measure how the distance between
two fixed opinion vectors vary over time, as the social environment changes. Panel c illustrates the idea that we can use
the CogNet to estimate missing data on an individual’s position of specific issues, thus probabilistically completing partially
observed worldviews. We leverage this ability to validate the CogNet framework. Panel d illustrates four distinct measures
of polarization that arise in the CogNet framework: two of these (the embedding diameter and the polar separation) are
measures of ideological polarization, whereas the remaining two (number and spacing of clusters) are measures of affective
polarization. Note “polar separation” is simply the CogNet-distance between two extreme opinion vectors (the poles) to a
fixed set of socially contentious questions (See Table I). Variation of the metric over time implies that the polar separation
varies over time, although the poles themselves are held constant.

We also consider a pair of metrics related to the coherence of opinion groups most likely to contribute to
affective polarization, or the self-conscious awareness and reinforcement of separation between polar groups 3,39 .
These include a measure of opinion fragmentation in the optimal number of clusters, and a measure of opinion
dissociation in the average cluster separation, derived from the metric embedding computed from the CogNet-

5

GSS variable description key
grass
natsoc
natarms
natheal
premarsx
nihilism
prayer
relgeneq
fefam
hubbywrk
fechld
fepresch
RELEXT1
fund

Use of marijuana should be made legal
RACDIF4
Govt. spending on social security
miracles
Govt. spending in military
Govt. spending in healthcare
wrkwayup
Sex before marriage
teensex
Life does not serve any purpose
godmeans
Bible prayer in public schools
satfin
Religion treats men and women
equally
Better for man to work, woman tend
home
Husb shld work wife shld look after
home
Mother working doesn’t hurt children
Preschool kids suffer if mother works
Religious extremists can hold public
meetings
How fundamentalist are you

a. Selected closed circuits

Worse black wages are due to lack of
will
Belief in religious miracles
Blacks overcome prejudice without
favors
Sex before marriage: teens
Life meaningful because god exists
Satisfaction with financial situation

abinspay

pornlaw

abpoorw
grass
RACDIF3
natarms

bible
premarsx

b. GSS variable prayer

reborn

natheal

RACDIF4

prayer

bible

approve disapprove

usedup

inspired word
other
word of god

book of fables

socfrend
natsoc

2018

natarms

natsoc

fefam

socbar
natheal

fefam

nihilism

natroad

wrktime

godmeans
wrkwayup

agree
disagree strongly agree
strongly disagree

overwork

disagree
neither agree nor disagree
strongly agree
strongly disagree

agree

workfast
fatalism

prayer
nateduc
natsoc

approve
Prob: 0.711
Frac: 0.086

wrkwayup

RELEXT1

agree somewhat
disagree strongly
agree strongly
neither agree nor disagree
disagree somewhat
approve
Prob: 0.736
Frac: 0.064

approve
Prob: 0.964
Frac: 0.05

deﬁnitely
deﬁnitely not

approve
Prob: 0.538
Frac: 0.058

probably
probably not

disapprove
Prob: 0.766
Frac: 0.114

hubbywrk

strongly disagree

natsoc

approve
Prob: 0.754
Frac: 0.051

believe sometimes
dont believe
know god exists
no way to ﬁnd out
some higher power

believe but doubts

about right

hubbywrk
agree
disagree
neither agree nor disagree
strongly agree

too little
too much

disapprove
Prob: 0.543
Frac: 0.093

teensex

almst always wrg

approve
Prob: 0.512
Frac: 0.075

always wrong
not wrong at all
sometimes wrong

miracles

fechld
yes, deﬁnitely

disagree
neither agree nor disagree

agree
Prob: 0.513
Frac: 0.158

fepresch
agree
disagree
strongly agree

disagree

strongly disagree

disagree
Prob: 0.448
Frac: 0.057

hubbywrk

agree
strongly agree

agree
disagree

relgeneq

strongly agree
strongly disagree
satﬁn

strongly disagree
Prob: 0.619
Frac: 0.206
i don't belong to or follow any religion
treats men and women equally
treats women better than men

treats men better than women
disagree
Prob: 0.573
Frac: 0.069

more or less

disapprove
Prob: 0.588
Frac: 0.102

visnhist

neither agree nor disagree

natenrgy

god

fund

not at all sat
satisﬁed

disapprove
Prob: 0.843
Frac: 0.108

no, deﬁnitely not
no, probably not
yes, probably

liberal

fundamentalist
moderate

approve
Prob: 0.632
Frac: 0.061

age

d
e

c

c

disagree
Prob: 0.708
Frac: 0.206

strongly disagree
Prob: 0.591
Frac: 0.056

fepresch

disagree
disagree
Prob: 0.59
Frac: 0.089

agree
strongly agree

agree
Prob: 0.436
Frac: 0.047

b
d
e

RACDIF4

no

yes

disapprove
Prob: 0.747
Frac: 0.088

approve
Prob: 0.544
Frac: 0.051

c. GSS variable fefam
strongly
agree

strongly
agree disagree disagree

disagree
Prob: 0.658
Frac: 0.062

disagree
Prob: 0.533
Frac: 0.051

Fig. 2. CogNet dependency framework. Panel a illustrates some inferred dependencies in the CogNet inferred for the

2018 GSS survey. More specifically, we illustrate a selected set of closed shortest-path circuits in among the GSS variables,
showing the interplay of social, political, demographic and educational backgrounds. Panel b and c illustrate two specific
conditional inference trees inferred for the GSS variable prayer (support of bible prayer in public schools) and fefam (It is
better for men to work and women tend home) respectively. Note that that these variables may be predicted using these
trees using responses to other GSS variables as features, and the variables that act as features in these trees, are predicted
by their own inference trees. For example, the prayer tree (panel b) uses fefam (panel c) as a feature. The descriptions of
the GSS variables used in these two trees are shown in top left inset. Node colors correspond to the response distribution
characterized by that node: colors of the “pure” responses (❡✿❣✿ purely “approve” or purely “disapprove” in panel b) are shown
under the panel titles. Since the nodes have a non-degenerate distribution over possible responses, the actual node color is
a mixture of the colors of the pure responses. In the terminal nodes, “Prob.” refres to the probability of the chosen decision,
and “Frac.” denotes the probability of ending up in that leaf.

distance (Supplementary Fig. 2). Importantly for the metric embeddings computed for each of the GSS surveys
from 1972 to 2021, we use the corresponding inferred CogNet, and thus the actual metric (the CogNet-distance)
varies over time to reflect the variation in the emergent dependencies between the query responses.
While ideological polarization measures quantify how removed ideological positions are from one another,
affective polarization measures estimate the fragmentation and internal separation of emergent cultural groups.

6

TABLE I

P OLAR RESPONSE VECTORS ON A FIXED SET OF SOCIALLY CONTENTIOUS TOPICS❄
index
abany

confed
conlabor

description
abortion should be legal if mother wants it for any reason
abortion is wrong if there is a strong chance of serious
defect in the baby
abortion should be legal if there is a strong chance of
serious defect in baby
abortion should be legal if mother’s own health is seriously
endangered by the pregnancy
abortion legal if mother does not want any more children
abortion should be legal if family has a very low income and
cannot afford any more children
wrong for woman to get abortion if low income
abortion should be legal if mother pregnant by rape
abortion should be legal if mother is not married and does
not want to marry the man
the bible is the actual word of god and is to be taken literally
or is a book of fables
communist allowed to teach in a college
militarists be allowed to teach in a college or university
practicing a religion helps people to gain comfort in times of
trouble and sorrow
confidence in federal government
confidence in organized labor

godchnge

which best describes your beliefs about god

abdefctw
abdefect
abhlth
abnomore
abpoor
abpoorw
abrape
absingle
bible
colcom
colmil
comfort

grass
gunlaw
intmil
libcom
libhomo
libmil
libmslm
maboygrl
natarms
natenvir
natfare
natsoc
owngun
pillok
pilloky
polabuse
pray
prayer
prayfreq
religcon
religint
reliten
rowngun
shotgun
spkcom
spkmil
taxrich
viruses

conservative pole (⑥❄ )
no

liberal pole (⑥❄ )
yes

always wrong

not wrong at all

use of marijuana should be made legal
require a person to obtain a police permit before he or she
could buy a gun
interest in issues about military and defense policy
communist books allowed in your public library
book in favor of homosexuality allowed in public library
allow militarists book in library
allow anti-american muslim clergymen’s books in library
mother’s gene decides whether the baby is a boy or a girl
govt spending on military
govt spending on environment
govt spending on welfare
govt spending on social security
have in your home any guns or revolvers
birth control should be available to teenagers between the
agesof 14 and 16 if their parents do not approve
birth control to teenagers 14-16
policeman can strike a citizen who says vulgar and obscene
things to the policeman
about how often do you pray
Bible prayer in public schools
about how often do you pray
religions bring more conflict than peace
people with very strong religious beliefs are often too
intolerant of others
would you call yourself a strong religious person
own a gun
own a shotgun
communist allowed to make a speech in your community
militarists allowed to make a speech in your community
describe taxes in america today
antibiotics kill viruses as well as bacteria

no

yes

no

yes

no

yes

no

yes

always wrong
no
no
inspired word
fired
not fired
strongly agree
hardly any
hardly any
believe now, always
have
not legal
oppose
very interested
remove
remove
not remove
remove
true
about right
too much
too much
too much
yes

not wrong at all
yes
yes
book of fables
not fired
not allowed
strongly disagree
a great deal
a great deal
don’t believe now, never
have
legal
favor
not at all interested
not remove
not remove
remove
not remove
false
too much
too little
too little
too little
no

strongly disagree

strongly agree

strongly disagree

strongly agree

no

yes

several times a day
disapprove
several times a day
strongly disagree

never
approve
never
strongly agree

strongly disagree

strongly agree

strong
yes
yes
not allowed
allowed
about right
definitely true

no religion
no
no
allowed
not allowed
much too low
definitely not true

❄ No actual respondent is expected to align perfectly with these poles. However, a conservative is expected to lean towards the

conservative pole and vice versa, ✐✿❡, the ideology index (Def. 8) for a conservative is expected to be negative.

CogNet Validation By Predicting Unobserved Opinions
To validate the CogNet framework, and demonstrate that CogNet-distance captures meaningful sociological
distance, we leverage the generative property of the CogNet to impute missing responses in a partially observed
opinion vector. We randomly mask 80% of the responses from out-of-sample participants, then reconstruct their
hidden responses using CogNet from the participant’s time period. Our results show that this reconstruction can

7

a. General Reconstruction scheme (First validation)

b. Reconstruction performance with q-distance
✵✿✵✶✺

random
mask

probability density

reconstruction error
reconstruction

mean: 45.1

histogram
Beta distribution fit
all subjects
left fringe
right fringe

✵✿✵✶
✵✿✵✵✺
9.92%

✵

✷✵

✵

✹✵

✻✵

✽✵

✶✵✵

✶✷✵

✶✹✵

✶✻✵

✶✽✵

✷✵✵

post-reconstruction error as % of initial

gender-related
opinion

c. Presidential vote forecast: Two approches (using race/gender-related opinions and direct reconstruction)
PRES16 reconstruction

PRES16

PRES16

2016

race-related
opinion

e. Selected

shortest-path cycles
partyid
polviews

PRES16

d. ROC Curves and AUC
helpblk

✶

PRES16

RACDIF4
RACDIF4

sensitivity

spec. 0.8

✵✿✽

spec. 0.95

partyid
sensitivity: ✵✿✽✾

voting decision:
PRES16

polviews

✵✿✻

education

wordsum
AUC
cognet (using reconst.) 84.63%
cognet (using race/gender poles) 91.03%
random forest 69.98%
gradient boosting 73.68%

✵✿✷

✵

✵✿✷

✵✿✹

✵✿✻

✵✿✽

prayer

nihilism

social
political

helpblk

✵✿✹

fefam

wrkwayup

religion

workwhts
sensitivity at 95% spec.: ✵✿✺✹

✵

ballot

wordj

fatalism

ballot
workwhts

wordj
prayer

wordsum
nateduc
natenrgy

natsoc

✶

1-specificity

Fig. 3. Missing opinion reconstruction and CogNet validation. We mask off opinions for a randomly chosen 80% of the
available responses in the out-of-sample participants within the polar items shown in Table I (panel a), and reconstruct them
using CogNet-sampling as described in Supplementary methods. Panel b shows the distribution of the post-reconstruction
error (measured by the CogNet-distance between the estimated opinion vector and the ground-truth), as a fraction of the
pre-reconstruction error. Any result less than 100% is an improvement, with error ❃
indicates that our reconstruction
did not succesfully improve the assessment of the masked opinions. We note that we can reduce the error in ❃
of the
participants. It is somewhat easier to reconstruct extreme opinions on both ends of the belief spectrum (illustrated by the
peaks of the left/right fringe, defined by an abolute ideology index ❃ ✿ occurring on the left of the scenarion where we
consider all participants). Supplementary Tables II, III, IV, V, VI and VII show examples of actual reconstruction, comparing
the ground-truth responses with estimated ones in randomly chosen participants, with Table VII showing an example where
the reconstruction was not very successful. The probability of such poor reconstruction is small, as shown in panel b. We
also test if we can forecast individual voting in the 2016 presidential election (GSS variable PRES16), using either a selected
set of variables to localize subjects in a race/gender-related opinion plane (See Supplementary Table VIII), or reconstruction
of the masked response. Panel d shows that the ROC curves, demonstrating that we achieve out-of-sample AUC❃
beating out standard ML models using responses as features. Panel e illustrates two shortest path cycles involving the target
GSS variable PRES16, showing dependencies across social, political, educational and religious beliefs.

✶✵✵✪

✾✵✪

✵✼

✾✵✪

✾✵✪

be achieved reliably for ❃
of out-of-sample participants, demonstrating the ability of our framework to capture
central patterns in the interdependence of opinions, suggesting its utility as a digital double of societal opinions,

8

✶✾✽✵

✷✵✵✵

✽

✵✿✵✶

✵✿✵✵✺

✹
✶✾✽✵

✷✵✷✵

✻

✷✵✵✵

normalized value

✵✿✵✺

GOP senate
S&P 500 close
number of clusters

✵✿✶

✵✿✵✶✺

c. Selected economic variables

average cluster separation
number of clusters

✘ ✷✵✵✵

average cluster separation

✘ ✷✵✵✹

✵✿✶✺

floor

q-distance

✵✿✷

b. Affective polarization measures

polar separation
embedding diameter

floor

a. Ideological polarization measures

✷
✵
✷

✷✵✷✵

✶✾✽✵

Economic variables

significant

(iv) cluster separation

(v) number of clusters
100

GNP
0.005

100

(i) polar separation

average
cluster
separation

101
100
10 1
10 2

(ii) diameter

GDP
poverty
tradebalance
GNPUSD
sp500
congress
senate
congress:senate
sepclusters

GDP
poverty
tradebalance
GNPUSD
sp500
congress
senate
congress:senate
sepclusters

0

0.006

Affective
polarization measures

0.003
lag=3

optimal
number of
clusters

0.009

polar
separation

0.03
lag=3

embedding
diameter

Ideological
polarization measures

f. Correlation: eco-politics & polarization
✶

GDP
poverty
S&P 500
GOP congress
GNIUSD
GNP
trade balance
polar sep
diameter
cluster sep
numclusters

✵✿✺
✵
✵✿✺
✶
GDP
poverty
S&P 500
GOP congress
GNIUSD
GNP
trade balance
polar sep
diameter
cluster sep
numclusters

10 3

0.004
0.005

GDP
poverty
tradebalance
GNPUSD
sp500
congress
senate
congress:senate

0

GDP
poverty
tradebalance
GNPUSD
sp500
congress
senate
congress:senate

0

101
100
10 1
10 2
0
10 2

✷✵✷✵

year

e. Granger causality tests (p-values/lags shown)

d. Generalized Linear Model regession coefficients

10 3

✷✵✵✵

year

year

GNP
poverty

Fig. 4. Polarization measures and link to GNP. Panel a shows the variation in the measures of ideological polarization
over time, which achieves a minimum approximately around 2004. Panel b illustrates the variation in affective measures of
polarization, which achieve a minimum between approximately 1996-2000. Panel c plots a subset of key economic variables
considered in this study, namely GNP, fraction of GOP senate representation, end-of-year S&P 500 close prices, and US
Census Bureau’s standard index of national poverty. Panel d shows GLM modeling with polarization measures as response
variables (subpanels i-iv), in which GNP is the only significant variable for affective polarization, and GNP along with affective
polarization are significant covariates for ideological polarization. Panel e carries out a standard Granger causality analysis,
presenting only the statistically significant relationships, which suggest a causal chain GNP
affective polarization
ideological polarization. Panel f computes Pearson’s correlation between the relevant variables, which corroborates the
emerging statistically significant picture: GNP changes are associated with changes in societal polarization.

✦

✦

reliable for probing polarization and estimating individual worldviews from incomplete information (Fig. 3a-b, and
Supplementary Tables II-VII). Compared to the CogNet-distance between an occluded response vector and an
observed one, reconstruction achieved an error reduction of 54.9% on average.
We note that our results indicate it is easier to reconstruct opinions for the portion of the population with more
extreme beliefs. To quantify how extreme the opinions of an individual are, we use the notion of the ideological
index, which quantifies as a scalar value in the range ❬✵❀ ✶❪ if an individual are closer to the left or the right

9

b. economic indicators vs EU polarization
normalized embedding diameter
normalized
GNI
normalized
GDP

✵✶
✿

Corr.

✁ GNI : emb. dia
✙ ✵ ✷✼
✿

✵
emb. dia. 9

✿

✶✾✽✵

✁ GDP

pval : 0.675
✷ ✁ GDP
9 emb. dia.
pval : 0.008
✶✾✾✵
✷✵✵✵
✷✵✶✵

✵ ✵✺
✷✵✵✵
year

✵ ✵✻

mean:
39.1

✿

1970
97.6% of subjects

q-distance

q-distance

2013

✷

mean post reconstruction error
probability density

✿

✁
✁

2013

embedding diameter
LOESS smoothing

✵ ✶✺

c. out-of-sample opinion reconstruction (EU)

✵ ✵✹
✿

✵ ✵✷
✿

✵✵

✷✵✷✵

✺✵

Very
positive

✿

2018-11-12

2018-04-26

2017-10-08

2017-03-22

2016-09-03

2016-02-16

2015-07-31

2015-01-12

Very
negative

2014-06-26

Neutral

✿

2013-12-08

✿

2013-05-22

✶✺✵

possible
responses

random prediction

76.9%

✿

2012-11-03

accuracy

d. Out of sample 3-way prediction of opinion on “EU IMAGE - POSITIVE/NEGATIVE” in Eurobarometer surveys

✶
✵✽
✵✻
✵✹
✵✷

✶✵✵

% of pre-reconstriction masking error

year

CogNet-based prediction

2022

99.5% of subjects

a. polarization in Eurobarometer data

time

Fig. 5. a, Polarization in the EU estimated via the embedding diameter of survey data computed by CogNet, showing runaway

polarization in teh post 2010 period, with significant worsening after 2013. b, GDP and GNI are computed to have a causla
influence with the pvalue for the hypothesis that changes in GDP does not Granger-cause the observed polarization being
0.008. c, Out-of-sample opinion reconstruction reduces error in greater than 99.5% of the participants. d, Three-way accuracy
for estimating the opinion of out-f-sample participants on EU IMAGE, achieving an average of 76.9% compared to the ✙
for the random predictor.

✸✵✪

extreme (Definition 8 in Supplementary methods), within our defined extreme poles. Our definition implies that
an ideological index ❁ ✵ implies the individual leans conservative, and ❃ ✵ implies a liberal leaning. We find that
for the left and right fringe, defined as the set of participants with an absolute ideology index ❃ ✵✿✼, reconstruction
error distribution leans more towards smaller reconstruction error.
For further validation, we investigated whether the CogNet framework can predict individual voting in the 2016 US
Presidential election, an election that historically defied expectations and polling 40 . We tested two approaches:
1) direct reconstruction of masked response to the GSS variable PRES16 to enumerate what candidate each
respondent voted for, and alternatively 2) positioning each respondent in a demographic opinion plane, and
using their planar coordinates as features in a standard machine learning classifier.
We defined this opinion plane by first selecting two pole-pairs: the first pair of poles (✗ ❄ , ✗❄ ) relate to insensitivity
to gender equality issues, and the second pair (✖❄ ❀ ✖❄ ) relate to insensitivity to racial inequalities (Supplementary
Table VIII). The plane coordinates of each individual is then given by the polar indices computed with respect
to these pole-pairs, similar to the ideological index described above. Our results remain stable for variations in
the exact choice of these polar variables.
We achieve out-of-sample AUC exceeding 84% for approach 1 (CogNet based direct reconstruction of masked
response to GSS variable PRES16) and 90% for approach 2 using the above-described planar coordinates of
individuals as features. In both cases, we significantly outperform standard ML models using raw responses as
features (Fig. 3c, d).

Analyzing Putative Drivers of Polarization
With our validated framework in place, we focused on uncovering mechanisms driving polarization in U.S. and
European society, emergent over the past 50 years. Our results suggest that 1) economic variables are strongly
associated with polarization, and 2) that there is suggestive, statistical evidence of a causal chain initiated with
economic downturns, leading to affective polarization or opinion fragmentation and dissociation, and finally to
ideological polarization (Fig. 4). In Fig. 4a-b we plot variation in ideological and affective polarization respectively,
showing that affective polarization minima precedes that for ideological polarization. Using three different lines
of reasoning we elucidate the dynamical connection between putative economic and political drivers of these

10

cultural effects. In panel d we fit a generalized linear model to the polarization response variables, and find
Gross National Product (GNP) as the only significant factor for the affective polarization variables of opinion
fragmentation and dissociation. For ideological polarization, we find that in addition to GNP, affective polarization
is also a significant contributor along with GOP senate representation over time. We structured these regressions
to maximize goodness-of-fit according to Bayesian and Akaike Information criterion (AIC). These observations
are corroborated in a Granger causal analysis 41 (panel e), which reveals how all unidirectional significant causal
links amongst the set of all possible pairwise variables, suggest that economic variables (GNP) ✦ affective
polarization ✦ ideological polarization. Finally, the Pearson correlation matrix (panel f) indicates that measures
of polarization cluster together, as does the putative econo-political drivers, with the “bridge” between the clusters
dominated by GNP, S&P500 close prices, and GOP senate representation.
These key results replicate in analyses of Eurobarometer surveys (Fig. 5). We verify that CogNet models of the
Eurobarometer remain as or more predictive than those for the GSS. We reduce post-reconstruction error in the
deviation of occluded worldviews for out-of-sample participants to 39.1% relative to pre-reconstruction deviation
from the ground truth. Finally, we test accuracy of predicting individual responses to a fixed topic (EU IMAGE POSITIVE/NEGATIVE), and achieve a 3-way accuracy of 76.9%. Responses were generated by including this
topic among the 80% of responses masked for out-of-sample participants, and letting CogNet reconstruct those
response. A random predictor achieves an accuracy close to 30% as expected (panel c).
The timing and nature of polarization is naturally different in the EU. With the nature of “poles” less obvious
in the EU, we only consider embedding diameter (panel a), where we see indications of runaway polarization
in the post-2010 period, reaching unprecedented levels after 2013. These patterns coincide with socio-political
changes in Europe that occurred around the coalescence of public opinion around the “Brexit” issue – the
electoral referendum of the United Kingdom (UK) to withdraw from the EU. Several key political events, including
the promise of a public vote on the issue https://www.bbc.com/news/uk-politics-21148282 by then British prime
minister Theresa May. The eventual vote on the issue in 2016, and the continuing debate over nationalism
versus populism has had significant impact on the political and social fabric or the EU 42 . Our analysis captures
the concomitant increase of societal polarization, and as before, statistical evidence suggesting that economic
changes reflected in the European GDP/GNI are a likely cause (panel b) (♣ ❁ ✿✵✶).

Conclusion
Understanding societal polarization and its drivers is emerging as a fundamental challenge in policy making
and governance, without which nations risk irreversible erosion of democratic norms and institutions 43–45 . Our
model offers new insight into the mechanics of polarization that confirm patterns described and hypothesized
in contemporary literature, where polarization, particularly affective polarization, has been linked to rising inequality and economic decline 46 . Similar conclusions have been reached from comparative analysis of societal
polarization emerging globally 47 . While the threat of growing affective polarization has been acknowledged, its
connection to an ideological divide has remained more ambiguous 48 . Our finding that economic downturns anticipate increased societal polarization contributes suggestive new evidence for why the economically-devastating
COVID19 pandemic may have failed to achieve social unity. Our analysis adds multiple points of evidence for
the role that eco-political factors play in driving affective polarization, and not directly ideological separation 3 .
Our approach has aimed at complementing the current academic discourse and analysis. Instead of devising
simple models manually designed to reflect important perceived characteristics of polarization dynamics, or using
proxies to measure polarization and then elucidate its correlation to eco-political variables, we have modeled the
complex distribution of opinions across US and EU societies directly at the level of the individual, but through
learning highly complex structures that shape and constrain the shared belief space over a half century in the
US and Europe. This analysis provides quantitative and actionable suggestive evidence of a causal chain from
economic hardship through opinion fragmentation and dissociation to ideological polarization. It further lays the
foundation for machine inference to inform policy decisions and for data-driven digital doubles of social opinion
to not only generate insight, but simulate response 49 .

R EFERENCES
[1] Heltzel, G. & Laurin, K. Polarization in america: two possible futures. Current opinion in behavioral sciences
34, 179–184 (2020).
[2] Fiorina, M. P. & Abrams, S. J. Political polarization in the american public. Annu. Rev. Polit. Sci. 11, 563–588
(2008).
[3] Iyengar, S., Sood, G. & Lelkes, Y. Affect, not ideologya social identity perspective on polarization. Public
opinion quarterly 76, 405–431 (2012).
[4] Ura, J. D. & Ellis, C. R. Partisan moods: Polarization and the dynamics of mass party preferences. The
Journal of Politics 74, 277–291 (2012).

11

[5] Druckman, J. N., Peterson, E. & Slothuus, R. How elite partisan polarization affects public opinion formation.
American Political Science Review 107, 57–79 (2013).
[6] Grosser, J. & Palfrey, T. R. Candidate entry and political polarization: An antimedian voter theorem. American
Journal of Political Science 58, 127–143 (2014).
[7] Lauderdale, B. E. Does inattention to political debate explain the polarization gap between the us congress
and public? Public Opinion Quarterly 77, 2–23 (2013).
[8] Levendusky, M. S. Why do partisan media polarize viewers? American Journal of Political Science 57,
611–623 (2013).
[9] Prior, M. The challenge of measuring media exposure: Reply to dilliplane, goldman, and mutz. Political
Communication 30, 620–634 (2013).
[10] Leeper, T. J. The informational basis for mass polarization. Public Opinion Quarterly 78, 27–46 (2014).
[11] Thomsen, D. M. Ideological moderates won’t run: How party fit matters for partisan polarization in congress.
The Journal of Politics 76, 786–797 (2014).
[12] Weinschenk, A. C. Polarization, ideology, and vote choice in us congressional elections. Journal of Elections,
Public Opinion & Parties 24, 73–89 (2014).
[13] Mason, L. “i disrespectfully agree”: The differential effects of partisan sorting on social and issue polarization.
American Journal of Political Science 59, 128–145 (2015).
[14] Bramson, A. et al. Understanding polarization: Meanings, measures, and model evaluation. Philosophy of
science 84, 115–159 (2017).
[15] Bramson, A. et al. Disambiguation of social polarization concepts and measures. The Journal of
Mathematical Sociology 40, 80–111 (2016).
[16] DeGroot, M. H. Reaching a consensus. Journal of the American Statistical Association 69, 118–121 (1974).
[17] Friedkin, N. E. & Johnsen, E. C. Social influence and opinions. Journal of Mathematical Sociology 15,
193–206 (1990).
[18] Pariser, E. The filter bubble: What the Internet is hiding from you (Penguin UK, 2011).
[19] Bakshy, E., Messing, S. & Adamic, L. A. Exposure to ideologically diverse news and opinion on facebook.
Science 348, 1130–1132 (2015).
[20] Boxell, L., Gentzkow, M. & Shapiro, J. M. Greater internet use is not associated with faster growth in
political polarization among us demographic groups. Proceedings of the National Academy of Sciences
114, 10612–10617 (2017).
[21] Musco, C., Musco, C. & Tsourakakis, C. E. Minimizing polarization and disagreement in social networks.
In Proceedings of the 2018 World Wide Web Conference, 369–378 (2018).
[22] Mao, Y., Bolouki, S. & Akyol, E. Spread of information with confirmation bias in cyber-social networks. IEEE
Transactions on Network Science and Engineering 7, 688–700 (2018).
[23] Aslay, C., Matakos, A., Galbrun, E. & Gionis, A. Maximizing the diversity of exposure in a social network.
In 2018 IEEE International Conference on Data Mining (ICDM), 863–868 (IEEE, 2018).
[24] Bail, C. A. et al. Exposure to opposing views on social media can increase political polarization. Proceedings
of the National Academy of Sciences 115, 9216–9221 (2018).
[25] Fischbach, K., Marx, J. & Weitzel, T. Agent-based modeling in social sciences (2021).
[26] Manzo, G. Review of agent-based models (2008).
[27] Lorenz, J. Data-driven agent-based modeling in computational social science. In Handbook of Computational Social Science, Volume 1, 150–167 (Routledge, 2021).
[28] Macy, M. W., Ma, M., Tabin, D. R., Gao, J. & Szymanski, B. K. Polarization and tipping points. Proceedings
of the National Academy of Sciences 118, e2102144118 (2021).
[29] Macy, M. W. & Willer, R. From factors to actors: Computational sociology and agent-based modeling.
Annual review of sociology 143–166 (2002).
[30] DellaPosta, D., Shi, Y. & Macy, M. Why do liberals drink lattes? American Journal of Sociology 120,
1473–1511 (2015).
[31] Schelling, T. C. Micromotives and macrobehavior (WW Norton & Company, 2006).
[32] Hahn, H. A. The conundrum of verification and validation of social science-based models. Procedia
Computer Science 16, 878–887 (2013).
[33] Lu, X., Gao, J. & Szymanski, B. K. The evolution of polarization in the legislative branch of government.
Journal of the Royal Society Interface 16, 20190010 (2019).
[34] Bail, C. Breaking the social media prism: How to make our platforms less polarizing (Princeton University
Press, 2022).
[35] Cinelli, M., De Francisci Morales, G., Galeazzi, A., Quattrociocchi, W. & Starnini, M. The echo chamber
effect on social media. Proceedings of the National Academy of Sciences 118, e2023301118 (2021).
[36] Weber, M. & Kalberg, S. The Protestant ethic and the spirit of capitalism (Routledge, 2013).
[37] Bearman, P. S. Relations into rhetorics: elite transformation and the eclipse of localism in England, 15401640 (Harvard University, 1985).
[38] Sard-Espinosa, A., Subbiah, S. & Bartz-Beielstein, T. Conditional inference trees for knowledge extraction

12

from motor health condition data. Eng. Appl. Artif. Intell. 62, 26–37 (2017). URL https://doi.org/10.1016/j.
engappai.2017.03.008.
[39] Iyengar, S., Lelkes, Y., Levendusky, M., Malhotra, N. & Westwood, S. J. The origins and consequences of
affective polarization in the united states. Annual review of political science 22, 129–146 (2019).
[40] Jacobson, G. C. Polarization, gridlock, and presidential campaign politics in 2016. The ANNALS of the
American Academy of Political and Social Science 667, 226–246 (2016).
[41] Granger, C. Investigating causal relations by econometric models and cross-spectral methods. In Essays
in econometrics: collected papers of Clive WJ Granger, 31–47 (2001).
[42] Ford, R. & Goodwin, M. Britain after brexit: A nation divided. Journal of Democracy 28, 17–30 (2017).
[43] Bonikowski, B. Ethno-nationalist populism and the mobilization of collective resentment. The British journal
of sociology 68, S181–S213 (2017).
[44] Hawkins, K. & Littvay, L. Contemporary US populism in comparative perspective (Cambridge University
Press, 2019).
[45] Steven, L. & Daniel, Z. How democracies die. United States: Crown (2018).
[46] Stewart, A. J., McCarty, N. & Bryson, J. J. Polarization under rising inequality and economic decline.
Science advances 6, eabd4201 (2020).
[47] Gidron, N., Adams, J. & Horne, W. American affective polarization in comparative perspective (Cambridge
University Press, 2020).
[48] Wagner, M. Affective polarization in multiparty systems. Electoral Studies 69, 102199 (2021).
[49] Rotaru, V., Huang, Y., Li, T., Evans, J. & Chattopadhyay, I. Event-level prediction of urban crime reveals a
signature of enforcement bias in us cities. Nature human behaviour 6, 1056–1068 (2022).
[50] Manning, C. D., Manning, C. D. & Schütze, H. Foundations of statistical natural language processing (MIT
press, 1999).
[51] Cover, T. M. Elements of information theory (John Wiley & Sons, 1999).
[52] Fedotov, A. A., Harremoës, P. & Topsoe, F. Refinements of pinsker’s inequality. IEEE Transactions on
Information Theory 49, 1491–1498 (2003).
[53] Neath, A. A. & Cavanaugh, J. E. The bayesian information criterion: background, derivation, and
applications. Wiley Interdisciplinary Reviews: Computational Statistics 4, 199–203 (2012).
[54] Casella, G. & George, E. I. Explaining the gibbs sampler. The American Statistician 46, 167–174 (1992).

ACKNOWLEDGMENTS
Funding: This work is funded in part by the Defense Sciences Office of the Defense Advanced Research
Projects Agency (Project Nos. W911NF2010302 and HR00111820006). The claims made in this study do not
necessarily reflect the position or the policy of the sponsors, and no official endorsement should be inferred.
Author Contributions: DY and IC developed software, and carried out computational analysis. IC developed the
theory of CogNet and procured funding. IC and JE interpreted results and wrote the paper. Data and Materials
Availability: The GSS and Eurobarometer databases are publicly accessible. The complete implementation for
the CogNet architecture is available under a permissive license at https://pypi.org/project/cognet/, with complete
instructions for installation in any Python 3.x environment. The inferred CogNet models are available at https:
//zenodo.org/record/5781768/.

L IST OF S UPPLEMENTARY M ATERIALS
1) Supplementary Methods
2) Supplementary Figures 1-3
3) Supplementary Tables 1-8

13

S UPPLEMENTARY M ETHODS
Data Sources
Our data comprises the complete GSS database procured from the National Opinion Research Center (NORC)
at the University of Chicago. The survey sampled ❃ ✻✺❑ US residents over nearly half a century. We use 80%
of the data for training, and the rest for out-of-sample validation. Data for the putative economic and political
factors are obtained from the United States Census Bureau. We corroborate these patterns with Eurobarometer,
the polling instrument used by the European Parliament, European Commission and other EU institutions and
agencies to monitor the state of European public opinion. The survey sampled ✸❀ ✾✽✵❀ ✷✹✹ participants over 235
surveys.

Basic Definitions and Notation
Definition 1 (Item Set). Let I be a finite set of questions (items) asked to a population of respondents. We call
this the item set. Each item response can be either categorical, ordinal or real valued. The range of each item
✐ ✷ I is denoted as ✝✐ .
Note that each respondent can be imagined to produce a single data point in a very high dimensional space, ❡✿❣✿
if there are 6000 items, then each set of ≦ ✻✵✵✵ responses from an individual is a point in a ✻✵✵✵ dimensional
space. More importantly, these items are not independent, and have non-trivial, and often surprising and counterintuitive dependencies, which cannot be anticipated or modeled a priori. We can think of I as the index set of
a set of random variables, ✐✿❡✿, the item ✐ ✷ I indexes a random variable ❳✐ taking values in ✝✐ . Because these
random variables are not independent, our task here is to infer their dependencies.
Definition 2 (Response Set or Sample). Given an item set I, a response set or a sample is a set of responses
to a subset of items in I from a specific individual. We allow partial responses, ✐✿❡✿., a response set can only
contain responses to any subset of I.
Definition 3 (CogNet ✟P ). The construction of the recursive decision forest, as a collection of conditional
inference trees referred to as the CogNet, may be summarized as: If we have ♥ questions/topics ❳✶ ❀ ✁ ✁ ✁ ❀ ❳♥ , and
we have a subject responding with
◗ ① ✐ , ❢①✶ ❀ ✁ ✁ ✁ ❀ ①✐ ✶ ❀ ①✐✰✶ ❀ ✁ ✁ ✁ ❀ ①♥ ✶ ❀ ①♥ ❣, then the distribution of responses
to question ❳✐ is given by ✟✐ ✿ ❥ ,✐ ✝❥ ✦ ❉✭✝✐ ✮ where ❉✭✝✐ ✮ is the set of all possible distributions over the
set of all possible responses ✝✐ . The CogNet ✟P is the collection of all such decision trees computed on I for
participant population P .
In this study we use conditional inference trees 38 , to infer the component decision trees in a CogNet. In contrast
to decision tree construction algorithms that perform univariate splits and use information measures such as the
Gini coefficient to select covariates, conditional inference trees use multiple significance tests at each split to
substantially resist overfitting.
Definition 4 (CogNet-distance). For two opinion vectors ①❀ ② , our intrinsic metric (CogNet-distance) is defined
as:
✑✑
✏ ✏
✒P❀◗ ✭①❀ ② ✮ , E✐ J ✷
✶

✟ ✭① ✮❀ ✟ ✭② ✮
P
✐

◗

✐

✐

✐

where P❀ ◗ are possibly two distinct populations with distinct CogNets, such that
① ✷ P❀ ② ✷ ◗ and J✭✁❀ ✁✮ is the Jensen-Shannon (JS) divergence 50

If the populations are identical, we denote CogNet-distance between ①❀ ② as ✒P ✭①❀ ② ✮ or ✒✭①❀ ② ✮ if the populations
are clear from context.
Importantly, the square-root in the definition arises naturally from the bounds we are able to prove, and is
dictated by the form of Pinsker’s inequality 51 , making sure that distances along a sequence of successive opinion
vectors sum linearly. Insofar as the JS divergence is a legitimate metric, and sums and scaling preserves metric
properties, the CogNet-distance satisfies the required properties of being a distance metric, with the exception
of the requirement to be 0 if and only if opinion vectors are identical. Thus, the CogNet-distance is technically
a pseudo-metric because distinct opinion vectors can induce the same distributions over each index, and thus
evaluate to a zero distance. This is desirable in our case as we do not want our distance to be sensitive to
changes not socially relevant. The intuition is that not all opinion variations are equally important or likely, and
CogNet-distance is designed to be sensitive to those that matter for societal polarization – affective or ideological.
We can extend the definition of CogNet-distance to define a distance between an individual and a group (a
sub-population), or between two groups, as follows:
Definition 5 (Pseudo-metric Between Individuals and Groups, and Two Groups). Using Hausdorff metric be-

14

tween sets:

✽① ✷ P❀ ② ✷ ◗❀
✒✭①❀ ◗✮ ❂ ♠✐♥
✒✭①❀ ②✮
② ✷◗

(1)

✚

✛

✒✭P❀ ◗✮ ❂ ♠❛① ♠❛①
✒✭①❀ ◗✮❀ ♠❛①
✒✭②❀ P ✮
①✷P
② ✷◗

(2)

Estimating Goodness of Fit
For our modeling to be reliable, we need a quantitative test of how well the CogNet represents the survey data.
Here, we formulate an explicit model membership test to address this.
Definition 6 (Membership Probability of an opinion vector). Given a population P inducing the CogNet ✟P and
an opinion vector ①, we can compute the membership probability of ① in the set of samples modeled well by
the CogNet:

✦①P , P r✭① ✷ P ✮ ❂

◆
❨
❥ ❂✶

✟P❥ ✭① ❥ ✮❥①❥

✁

(3)

which represents the probability that the CogNet generates the sample ①.
Note that ①❥ is the ❥ t❤ entry in ①, and is thus an element in the set ✝❥ . Because we are predominantly concerned
with the case where ✝❥ is a finite set, ✟P❥ ✭① ❥ ✮❥①❥ is the entry in the probability mass function corresponding
to the element of ✝❥ which appears at the ❥ t❤ index in sequence ①. We can assess the goodness of fit of an
inferred CogNet by testing if the null hypothesis ❍✵ : “samples have a higher probability of being generated by
randomly selecting responses, compared to being generated by the inferred CogNet” is rejected. We find that
for all years ❍✵ is rejected at ❃ ✾✾✿✾✾✪ significance level (Supplementary Fig. 3).

Theoretical Probability Bounds
The CogNet framework allows us to rigorously compute bounds on the probability of a spontaneous change
from one opinion vector to another, brought about by chance variations. Not all perturbations in an opinion
vector are likely or sociologically meaningful, ✐✿❡✿, opinions of some topics are more likely to vary given the rest
of one’s opinions or beliefs. With the exponentially exploding number of possibilities in which an opinion vector
over a large set of query items can vary, it is computationally intractable to exhaustively model this dynamics.
Nevertheless, we can constrain the possibilities using patterns distilled by the CogNet construction. We show
in Theorem 1 that at a significance level ☛, with the number of query items ◆ , the probability of a spontaneous
jump of opinion vector ① from population P to an opinion vector ② in population ◗, P r✭① ✦ ② ✮ is bounded:
♣✽◆ ✷
♣✽◆ ✷
(4)
✦②◗ ❡ ✶ ☛ ✒✭①❀②✮ ≧ P r✭① ✦ ②✮ ≧ ✦②◗ ❡ ✶ ☛ ✒✭①❀②✮
where ✦② is the membership probability of opinion vector ② in ◗.
◗

Theorem 1 (Probability Bound). Given an opinion vector ① of length ◆ that transitions to ② ✷ ◗, we have the
following bounds at significance level ☛.
♣✽◆ ✷
♣✽◆ ✷
✦②◗ ❡ ✶ ☛ ✒✭①❀②✮ ≧ P r✭① ✦ ②✮ ≧ ✦②◗ ❡ ✶ ☛ ✒✭①❀②✮
(5)

where ✦② is the membership probability of ② in the population ◗ (See Def. 6), and ✒✭①❀ ② ✮ is the q-distance
between ①❀ ② (See Def. 4).
◗

Proof. Using Sanov’s theorem 51 on large deviations, we conclude that the probability of a spontaneous jump
from ① ✷ P to ② ✷ ◗, with the possibility P , ◗, is given by:

P r ✭① ✦ ② ✮ ❂
Writing the factors on the right hand side as:

◆
❨

✐❂✶

✟P✐ ✭① ✐ ✮❥②✐

✟ ✭① ✐ ✮❥②✐ ❂ ✟ ✭② ✐ ✮❥②✐
P
✐

◗
✐

✥

✁

✟P✐ ✭① ✐ ✮❥②✐
✟◗✐ ✭② ✐ ✮❥②✐

(6)
✦

(7)

we note that ✟P✐ ✭① ✐ ✮, ✟✐ ✭② ✐ ✮ are distributions on the same index ✐, and hence:
◗

❥✟P✐ ✭① ✐ ✮②✐ ✟◗✐ ✭② ✐ ✮②✐ ❥ ≦

❳

②✐

✷✝✐

❥✟P✐ ✭① ✐ ✮②✐ ✟◗✐ ✭② ✐ ✮②✐ ❥

(8)

Using a standard refinement of Pinsker’s inequality 52 , and the relationship of Jensen-Shannon divergence with

15

total variation, we get:

☞

☞

☞
✶
✟◗✐ ✭② ✐ ✮②✐ ☞☞ ≦ ✶ ♣✽✒
✒✐ ≧ ❥✟P✐ ✭① ✐ ✮②✐ ✟◗✐ ✭② ✐ ✮②✐ ❥✷ ✮ ☞☞☞✶
✐
✽
✟P✐ ✭① ✐ ✮②✐ ☞☞ ❛✵

(9)

where ❛✵ is the smallest non-zero probability value of generating the entry at any index. We will see that this
parameter is related to the statistical significance of our bounds. First, we can formulate a lower bound as
follows: ✥
✦
✦
✦
✥
✥

✟P✐ ✭① ✐ ✮❥②✐ ❂ ❳ ❧♦❣ ✟P✐ ✭① ✐ ✮❥②✐
❧♦❣
◗
✟◗✐ ✭② ✐ ✮❥②✐
✐
✐❂✶ ✟✐ ✭② ✐ ✮❥②✐
◆
❨

Similarly, the upper bound may be derived as:
✥

✦

✥

≧

❳

✐

✟P✐ ✭① ✐ ✮❥②✐ ❂ ❳ ❧♦❣ ✟P✐ ✭① ✐ ✮❥②✐
❧♦❣
◗
✟◗✐ ✭② ✐ ✮❥②✐
✐
✐❂✶ ✟✐ ✭② ✐ ✮❥②✐
◆
❨

Combining Eqs. 10 and 11, we conclude:

◗
✶ ✟P✐ ✭② ✐ ✮②✐
✟✐ ✭① ✐ ✮②✐
✦

≦

❳

✥

✐

♣✽◆

✦②◗ ❡ ❛✵ ✒ ≧ P r✭① ✦ ②✮ ≧ ✦②◗ ❡

≧

♣ ❳
✽

❛✵

✐

✟◗✐ ✭② ✐ ✮②✐ ✶
✟P✐ ✭① ✐ ✮②✐

♣✽◆
❛✵

✒✶❂✷ ❂

♣

✐

✽◆ ✒
❛✵

(10)

♣

✦

≦

✽◆ ✒
❛✵

(11)

(12)

Now, interpreting ❛✵ as the probability of generating an unlikely event below our desired threshold (✐✿❡✿ a “failure”),
we note that the probability of generating at least one such event is given by ✶ ✭✶ ❛✵ ✮◆ . Hence if ☛ is the
pre-specified significance level, we have for ◆ ❃❃ ✶:
❛✵ ✙ ✭✶ ☛✮❂◆
(13)
Hence, we conclude, that at significance level ≧ ☛, we have the bounds:
♣✽◆ ✷
♣✽◆ ✷
✦②◗ ❡ ✶ ☛ ✒ ≧ P r✭① ✦ ②✮ ≧ ✦②◗ ❡ ✶ ☛ ✒

(14)


Remark 1. This bound can be rewritten in terms of the log-likelihood of the spontaneous jump and with constants
independent of the initial sequence ① as:

❥❧♦❣ P r✭① ✦ ②✮ ❈✵ ❥ ≦ ❈✶ ✒

where the constants are given by:

❈✵ ❂ ❧♦❣ ✦②◗
♣ ✷
✽◆
❈✶ ❂
✶ ☛

(15)
(16)
(17)

Handling Missing Data & Curated Poles
The CogNet construction naturally handles missing entries during the construction of component decision trees.
Additionally, we can compute the CogNet-distance between partially complete opinion vectors without any
additional modification. This follows from the fact that if all responses ① ✐ ❂ ❢①✶ ❀ ✁ ✁ ✁ ❀ ①✐ ✶ ❀ ①✐✰✶ ❀ ✁ ✁ ✁ ❀ ①♥ ✶ ❀ ①♥ ❣
other than that at the index ✐ is available, ✟✐ is conditioned on ① ✐ , whereas if any other responses are missing,
the distribution ✟✐ is simply conditioned on a smaller set. This allows us to choose a smaller set of GSS or
Eurobarometer variables, and enumerate responses which would reflect certain ideological leanings. These are
referred to as “polar vectors”, ❡✿❣✿, the liberal pole, and the conservative pole.
The liberal and conservative poles (⑥❄ ❀ ⑥❄ respectively) used in this study are shown in Table I. Poles corresponding to opinions on race-related items (✗ ❄ ❀ ✗❄ respectively) and gender-related items (✖❄ ❀ ✖❄ respectively)
are shown in Supplementary Table VIII.
Neither the choice of query items to define these race/gender and ideological poles, nor the responses chosen
to reflect extreme ideological positions is unique. Nevertheless, we verified that different choices to compose
these vectors do not substantially change our results or conclusions.

Ideological Polarization Measures
Definition 7 (Polar Separation). As a function of the inferred CogNet ✟P for population P , and given poles
⑥❄ ❀ ⑥❄ (See Table I), polar separation is defined as:
(18)
❞❄ , ✒✟P ✭⑥❄ ❀ ⑥❄ ✮

Definition 8 (Ideology index). For a bipolar society, the ideology index of an opinion vector s for population P
with an inferred CogNet is defined as:

✒ P ✭s❀ ⑥❄ ✮ ✒✟P ✭s❀ ⑥❄ ✮
✑ P ✭s ✮ ❂ ✟
✒✭⑥❄ ❀ ⑥❄ ✮

(19)

where ⑥❄ ❀ ⑥❄ are the two polar vectors. In general, for a multi-pole society the ideology index measures the

16

closeness to one of the poles. Thus, in general, the ideology index is a real-valued vector, where the ✐t❤
component is given by:
⑥✐ ✮ ♠❛①❥ ,✐ ✒✟P ✭s❀ ⑥❥ ✮
✭ ✮ ❂ ✒✟P ✭s❀♠❛①
❥ ,✐ ✒✟P ✭⑥✐ ❀ ⑥❥ ✮

✑P s ✐

(20)

Definition 9 (Embedding diameter). The embedding diameter of a population P with an inferred CogNet is
defined as:

♠❛① ✒✟P ✭①❀ ②✮
①✷P ✵ ❀②✷P ✵
where P ✵ is a sufficiently large sample from the population P .
❞P , EP ✵ ✘P

(21)

Affective Polarization Measures
We formalize two measures of affective polarization measures, 1) opinion fragmentation through the optimal
number of clusters (❈ ) in a year-specific metric embedding, where we optimize the number of clusters using
the Bayesian Information criterion (BIC) 53 , and 2) opinion dissociation through the average cluster separation
(❞❈ ), which is the average distance in the metric embedding when we use the BIC-optimal number of clusters.
While this structure of opinions does not necessarily relate to individuals’ affect regarding those from other
opinion clusters, empirically, nonfragmented separation has been historically associated with negatively valenced
affective views and behaviors with respect to the out-group, and as such, has typically been conceived and
measured in similar ways 3 .

Race and Gender Related Indexes
Definition 10 (Race-related Index). The race-related index is defined for an opinion vector s from a population
P is defined as:
❄
✭ ✮ ❂ ✒✟P ✭✖✒ ❀ sP ✮✭✖❄ ❀✒✖✟P ✮✭✖❄ ❀ s✮

❘P s

✟

(22)

❄

Definition 11 (Sexism Index). The gender-related index is defined for an opinion vector s from a population P
is defined as:
❄
✭ ✮ ❂ ✒✟P ✭✗✒ ❀ sP✮✭✗ ❄ ❀✒✗✟P✮✭✗❄ ❀ s✮

❙P s

✟

(23)

❄

If the population is fixed, ❡✿❣✿ if we are considering a single year with its corresponding CogNet, the denominators
can be ignored in the definition of race and gender indices, as we do in our second validation exercise (prediction
of 2016 US Presidential election outcome).

Reconstruction Approach: CogNet-sampling
The inferred CogNet can be used to optimally impute missing entries in an opinion vector, factoring in the
constraints that the remaining known responses to the rest of the opinion vector confers. Given a population
P inducing a CogNet ✟P , we can sample the neighborhood of an opinion vector ①, factoring in the inferred
◆
dependencies captured by ✟♣ . This induces a random field N✭①❀ ✟P ❀ ✖✮ taking values in ✐❂✶ ✝✐ . A specific
realization for N✭①❀ ✟P ❀ ✖✮ ❂ ✏ ✭①❀ ✟P ❀ ✖✮ is computed as shown in Algo. 1. Note that ✏ ✭①❀ ✟P ❀ ✖✮ is a random
function of its inputs, and can potentially change each time it is evaluated, and as described above, and outputs
a realization of the random field N✭①❀ ✟P ❀ ✖✮. We call ✏ the CogNet-sampler.

◗

Definition 12 (CogNet-sampling). Given a population P inducing a CogNet ✟P , we can sample the neighborhood
of an opinion vector ① via the CogNet-sampling algorithm, denoted by ✏ ✭①❀ ✟P ❀ ✖✮ (See Algo. 1). Here ✖ denotes
a baseline or average probability of the ✐t❤ item getting perturbed by random chance, which is estimated as
scaling with the variance of responses observed for that item in the overall population.

Thus, the reconstruction approach used in this study may be described as follows: Let ① be a partial opinion
vector, with a missing response at index ✐❄ ✷ I. We carry out q-sampling as follows:
① ✥ ✏ ✭①❀ ✟P ❀ ✖✮
(24)
stopping when ✐❄ has been populated.
The q-sampling algorithm realizes a probabilistic dynamical system:
①

✦ ✏ ✭①❀ ✟P ❀ ✖✮ ✦ ✏ ✭✏ ✭①❀ ✟P ❀ ✖✮❀ ✟P ❀ ✖✮ ✦ ✁ ✁ ✁

(25)

which also induces a (deterministic) dynamical system if we opt for a maximum likelihood choice for the
perturbations, ✐✿❡✿, if
✏ ✭①❀ ✟P ❀ ✖✮ , ❛r❣♠❛① ✟P ✭① ✐ ✮❥✛
(26)
✛✷✝✐

17

Note, that such a dynamical system has fixed points ①❄ defined by:

❥ ❂ ❛r❣♠❛① ✟P ✭① ✐ ✮❥✛

①❄ ✐

✛✷✝✐

(27)

which can be interpreted as the stable thought centers in society.
In general, q-sampling is a means to sample the joint distribution of responses to the set of query items in the
survey. Note that the CogNet is a means of estimating conditional distributions, and a direct sampling of the
ultra high-dimensional joint distribution is intractable both computationally, and due to the impractical sample
complexity required for such an approach. Nevertheless, we can easily show that the q-sampling approach
samples from this joint distribution asymptotically.
Theorem 2 (Convergence of q-sampling). The q-sampling algorithm described in Algo. 1 samples the joint
distribution of the survey items.
Proof. The q-sampling algorithm is identical to Gibb’s sampling 54 , which has the required property.



Algorithm 1: Q-sampling (✏ ✭①❀ ✟P ❀ ✖✮)

Data: Baseline propabaility ✖, Qnet ✟P , opinion vector ①
Result: opinion vector ①✵
/* choose item index to perturb
1 Choose ✐ with probability ✖✐ ;
/* choose new response for item at index
P
2 Choose ✛ ✷ ✝✐ with probability ✟✐ ❥✛ ;
/* update opinion vector
3 ①✐ ✥ ✛ ;
4 return ①;

*/
*/
*/

Analysis of Causal Drivers of Societal Polarization
We consider GDP (❣❉ ), GNP (❣◆ ) , GNI (✭❣■ ), trade balance (❣❚ ), poverty index (❣P ), US population, S&P 500
yearly close prices (❣▼ ) and political representation in the US Congress (❣❈ ) and the Senate (❣❙ ) as putative
factors driving societal polarization (See Fig. 4f). We fit multi-variable regression models to the polarization
measures estimated over time choosing the regression equations via minimizing AIC over a large set of randomly
generated equations, which led to the optimal regression equations:

❈ ❂ ❣❉ ✰ ❣P ✰ ❣❚ ✰ ❣◆ ✰ ❣▼ ✰ ❣❙ ❣❈

❂ ❣❉ ✰ ❣P ✰ ❣❚ ✰ ❣◆ ✰ ❣▼ ✰ ❣❙ ❣❈
❂ ❣❉ ✰ ❣P ✰ ❣❚ ✰ ❣◆ ✰ ❣▼ ✰ ❣❙ ❣❈ ✰ ❞❈
❂ ❣❉ ✰ ❣P ✰ ❣❚ ✰ ❣◆ ✰ ❣▼ ✰ ❣❙ ❣❈ ✰ ❞❈

❞❈
❞P
❞❄

(28)
(29)
(30)
(31)

Importantly, not all putative factors show up in the optimized equations, and not all factors included emerge as
significant (See Fig. 4d).
We also carried out pairwise Granger tests on all combinations of economic/political (9) and polarization variables
(4), ✐✿❡✿ in total ✹ ✂ ✾ ✂ ✷ ❂ ✼✷ such possible relations were tested, out of which seven directed links turn out to be
statistically significant (Fig. 4e). We allowed for a range of time delays or lags in the Granger tests to ascertain
if the relationships turn out to be significant with some time lag measured in the unit of years. Two out of the
four significant relationships from affective to ideological polarization showed up with a lag of three years.
While correlation is not a measure of statistical causality, computing the Pearson’s correlation matrix (Fig. 4f)
revealed the strong association between the economic/political putative drivers and the measures of polarization
defined in this study.

18

Supplementary Table I

DATABASE CHARACTERISTICS

characteristics
mean no. of items
mean no. of subjects
total no. of subjects
total no. of surveys considered
begin date
end date

eurobarometer
500.33
20307.37
3980244
196
1962-01-31
2021-02-12

GSS
707.0
1993.45
65784
33
1972
2021

Supplementary Table II

R ECONSTRUCTION EXAMPLE (2018, SUBJECT NUMBER 706)
item
abany
abdefect
abpoor
abpoorw
abrape
absingle
colcom
colmil
godchnge
gunlaw
intmil
libhomo
owngun
pillok
prayer
prayfreq
religcon
religint
shotgun
spkmil

description
abortion should be legal if mother wants it for any reason
abortion should be legal if there is a strong chance of serious defect
in baby
abortion should be legal if family has a very low income and cannot
afford any more children
wrong for woman to get abortion if low income
abortion should be legal if mother pregnant by rape
abortion should be legal if mother is not married and does not want
to marry the man
communist allowed to teach in a college
militarists be allowed to teach in a college or university
which best describes your beliefs about god
require a person to obtain a police permit before he or she could buy
a gun
interest in issues about military and defense policy
book in favor of homosexuality allowed in public library
have in your home any guns or revolvers
birth control should be available to teenagers between the agesof 14
and 16 if their parents do not approve
Bible prayer in public schools
about how often do you pray
religions bring more conflict than peace
people with very strong religious beliefs are often too intolerant of
others
own a shotgun
militarists allowed to make a speech in your community

true
yes

reconstructed
yes

yes

yes

yes

yes

not wrong at all
yes
yes
not fired
allowed
believe now, always have
favor
moderately interested
not remove
no
strongly agree
disapprove
about once a month
not agree/dsagre
not agree/dsagre
no
allowed

not wrong at all
no
yes
fired
allowed
believe now, didn’t used to
favor
moderately interested
not remove
no
strongly agree
disapprove
every week
agree
not agree/dsagre
no
allowed

Supplementary Table III

R ECONSTRUCTION EXAMPLE (2018, SUBJECT NUMBER 1040)
item
abany
abdefect
abnomore
abpoor
abpoorw
abrape
absingle
colmil
comfort
godchnge
gunlaw
libhomo
libmil
libmslm
owngun
pillok
prayfreq
rowngun
shotgun
spkcom

description
abortion should be legal if mother wants it for any reason
abortion should be legal if there is a strong chance of serious defect
in baby
abortion legal if mother does not want any more children
abortion should be legal if family has a very low income and cannot
afford any more children
wrong for woman to get abortion if low income
abortion should be legal if mother pregnant by rape
abortion should be legal if mother is not married and does not want
to marry the man
militarists be allowed to teach in a college or university
practicing a religion helps people to gain comfort in times of trouble
and sorrow
which best describes your beliefs about god
require a person to obtain a police permit before he or she could buy
a gun
book in favor of homosexuality allowed in public library
allow militarists book in library
allow anti-american muslim clergymen’s books in library
have in your home any guns or revolvers
birth control should be available to teenagers between the agesof 14
and 16 if their parents do not approve
about how often do you pray
own a gun
own a shotgun
communist allowed to make a speech in your community

true
yes

reconstructed
yes

yes

yes

no

no

no

no

always wrong
yes
no

not wrong at all
yes
yes

allowed

allowed

agree

agree

believe now, always have
favor
not remove
not remove
not remove
yes
strongly agree
several times a week
no
yes
allowed

believe now, always have
favor
not remove
not remove
not remove
no
strongly disagree
several times a week
no
no
allowed

19

a. Dependency network across survey items
Year 2021

Year 2018

Year 2016

RES16
natenrgy

RELIG16

reliten

polviews

parsol

savesoul
relig

conjudge

degree

satfin

bible

hlthphys

nateduc

abinspay
ABSTATE2

partyid

sprtlrgr

natchld

reliten

educ
pray

socrel

RES12

bible

ballot

conmedic

wordsum

sprtprsn

relpersn

attend

savesoul

pray

heaven

aidold

equalize

hlthcare

afterlif
wrktime

relactiv

grnlaws
attend
happy

condemnd

polviews

hlthmntl
HOE5

hlthphys
healthissp

Year 2010

Year 2004

Year 1998

immameco

nobuygrn

immjobs

immcosts
immimp

gochurch

amtv

wordsum

degree

forcult
version

powrorgs

wordsum

theism
godwatch

reliten

savesoul

COE3

reborn

reliten

godlove

attend

relcmfrt
uniongod

hlpequip

grnprog
grnexagg
grwtharm

supcares
promtefr

toodifme

attrally
cntctgov

partyid

indusgen

wrkstat

grncon

natchld
natenviy

conlegis

Year 1990

Year 1984

Year 1974

conlegis

marcohrt
libath

satfam

libcom

ballot

DEATH16

sppoorkd
sphlthkd

sphomekd

degree
age

AISCO08

marcohrt

ROTEST3

spheadst

aidold

sex

wordj

wordsum

SEI10EDUC

reliten

wrkstat

colath
spkath

dotdata
fund

ISCO08

fund

AOCC16

reliten

spkhomo

age
spkcom

makejobs

wordsum

aidunemp

libcom

degree

sex

setwage

colath
spkath

violwhts

colhomo

INTLJewS

milokme

ISCO08

RACDIF4

SEI10EDUC
contv

libcom

OCC10

EQUAL3

blkjobs

helpnot

farehsps

helpblk

marblk
marhisp

liveblks
conjudge

liveasns

b. Variation of large-degree item categories
out degree

✷✵

demography

education

health

social topics

politics

religion

✶✺

✷✵✷✶

✷✵✶✽

✷✵✶✻

✷✵✶✵

✷✵✵✻

✷✵✵✹

✶✾✾✽

✶✾✾✸

✶✾✾✵
✶✾✾✶

✶✾✽✷
✶✾✽✸
✶✾✽✹
✶✾✽✺
✶✾✽✻
✶✾✽✼
✶✾✽✽

✶✾✽✵

✶✾✼✻
✶✾✼✼
✶✾✼✽

✶✾✼✹

✶✾✼✷

✶✵

year

Supplementary Fig. 1. Emergent dependency graphs for selected time-periods. The CogNet models inferred with the GSS

reponse data of each year results in a forest of conditional inference trees, which induces year-specific dependency graphs
shown here. A directed edge from GSS variable A to varaibel B implies that teh conditional inference tree predicting B uses
A as a feature. The nodes in the graphs shown here are therefore GSS variables, and the size and color scaling of the nodes
represent the out-degree of the nodes: the larger a node, higher is the number of variables that the variable corresponding
to this node affects significantly. Panel b illustrates that the composition of the set of high out-degree variables changes over
time, with demographic chracterization of the participants and opinions on social topics replaced with religious beliefs and
political opinions in more recent times. We also note that the maximum out-degree of the nodes seem to somewhat relfect
the state of societal polarization, which we infer to be low in late 90s to early 2000s.

20

ideology index

✶

a. societal embedding

✵✿✺

✵

✵✿✺

✶

1972

1973

1974

1975

1976

1977

1978

1980

1982

1983

1984

1985

1986

1987

1988

1989

1990

1991

1993

1994

1996

1998

2000

2002

2004

2006

2008

✶
✵
✶
✶
✵
✶
✶

PCA dimension 2

✵
✶
✶
✵

✵

✵

✶

✶
2010

2012

2014

✶

✶

✷✵✵✵
✶✺✵✵
✶✵✵✵

✶

2016
✵

✶

✶

2018
✵

✶

✶

2021
✵

✶

✵
✶
✶

✵

✶

✶

✵

✶

✶

PCA dimension 1

✵

✶

cluster separation

✶

✶

✶

✵

✵

✶

✶

✶

✶

✶✾✽✵
✵

✵
✶

✶

b. database characteristics

✶

✵✿✵✶✵
✵

✵

✶

✷✵✵✵

✶
✵

year

✻✵✵

✹✵✵
✶

✵
✷✵✵

✷✵✷✵

c. cluster
number and spacing
✶
✶
✶

✶

✵

✶

✶

✶

✵

✵✿✽
✵✿✼

✵✿✵✵✺

✵✿✻
✵✿✺

✵✿✵✵✵
✷

✹

conservative fraction

✶
responses per item

✶

responses per sample

✶

✶

✻

optimal number of clusters

Supplementary Fig. 2. Visualization of societal embedding via CogNet-distance. Panel a. The year-specific distance
matrices obtained by computing pairwise CogNet-distance between individual participants in the GSS surveys are mapped
into a 2D plane using first a Sippl embedding (converting a distance matrix to a minimal-erroe high dimensional embedding),
followed by a PCA construction (mapping a high dimensional emedding to an approximate 2D embedding). Each data point
coresponds to an individual participant, and represents their opinion vector in this embedding. The color scale corresponds
to the ideology index of their opinion vector, which ranges from red (conservative, closer to the conservative pole, which has
an ideology index of -1) to blue (liberal, closer to the liberal pole, which has an ideology index of 1). Panel b shows that the
embedding produces distinct clusters, and the average spacing between clusters seem to linearly increase with the optimal
number (optimized via minimizing the Bayesian Information Criterion (BIC)) of cluster in any year.

21

Supplementary Table IV

R ECONSTRUCTION EXAMPLE (2018, SUBJECT NUMBER 1297)
item
abany
abhlth
abnomore
abpoor
abpoorw
abrape
colcom
godchnge
gunlaw
libcom
libmil
pillok
pray
prayer
prayfreq
religcon
religint
reliten
shotgun
spkmil

description
abortion should be legal if mother wants it for any reason
abortion should be legal if mother’s own health is seriously
endangered by the pregnancy
abortion legal if mother does not want any more children
abortion should be legal if family has a very low income and cannot
afford any more children
wrong for woman to get abortion if low income
abortion should be legal if mother pregnant by rape
communist allowed to teach in a college
which best describes your beliefs about god
require a person to obtain a police permit before he or she could buy
a gun
communist books allowed in your public library
allow militarists book in library
birth control should be available to teenagers between the agesof 14
and 16 if their parents do not approve
about how often do you pray
Bible prayer in public schools
about how often do you pray
religions bring more conflict than peace
people with very strong religious beliefs are often too intolerant of
others
would you call yourself a strong religious person
own a shotgun
militarists allowed to make a speech in your community

true
no

reconstructed
yes

yes

no

no

no

no

no

always wrong
no
not fired
believe now, always have
favor
not remove
not remove
strongly disagree
once a day
disapprove
every week
disagree

always wrong
no
not fired
believe now, always have
favor
not remove
not remove
disagree
several times a day
approve
several times a week
disagree

disagree

agree

strong
no
allowed

strong
no
allowed

Supplementary Table V

R ECONSTRUCTION EXAMPLE (2016, SUBJECT NUMBER 354)
item
abdefect
abhlth
abnomore
abpoor
abrape
bible
grass
gunlaw
libcom
libhomo
libmil
libmslm
owngun
polabuse
rowngun
shotgun
spkcom
spkmil

description
abortion should be legal if there is a strong chance of serious defect
in baby
abortion should be legal if mother’s own health is seriously
endangered by the pregnancy
abortion legal if mother does not want any more children
abortion should be legal if family has a very low income and cannot
afford any more children
abortion should be legal if mother pregnant by rape
the bible is the actual word of god and is to be taken literally or is a
book of fables
use of marijuana should be made legal
require a person to obtain a police permit before he or she could buy
a gun
communist books allowed in your public library
book in favor of homosexuality allowed in public library
allow militarists book in library
allow anti-american muslim clergymen’s books in library
have in your home any guns or revolvers
policeman can strike a citizen who says vulgar and obscene things
to the policeman
own a gun
own a shotgun
communist allowed to make a speech in your community
militarists allowed to make a speech in your community

true

reconstructed

yes

yes

yes

yes

yes

yes

yes

yes

yes

yes

inspired word

word of god

legal

not legal

favor

favor

not remove
not remove
not remove
not remove
yes
no
yes
no
allowed
allowed

not remove
not remove
not remove
remove
no
no
yes
no
allowed
allowed

✶✵✵
✶✵ ✶✽

✷✵✷✶

✷✵✶✽

✷✵✶✻

✷✵✶✹

✷✵✶✷

✷✵✶✵

✷✵✵✽

✷✵✵✻

✷✵✵✹

✷✵✵✷

✷✵✵✵

✶✾✾✽

✶✾✾✻

✶✾✾✸
✶✾✾✹

✶✾✽✷
✶✾✽✸
✶✾✽✹
✶✾✽✺
✶✾✽✻
✶✾✽✼
✶✾✽✽
✶✾✽✾
✶✾✾✵
✶✾✾✶

✶✵ ✺✹

✶✾✽✵

✶✵ ✸✻

✶✾✼✷
✶✾✼✸
✶✾✼✹
✶✾✼✺
✶✾✼✻
✶✾✼✼
✶✾✼✽

p-value

0.004

year
Supplementary Fig. 3. The null hypothesis that a random selection of responses can generate the observed responses is

rejected in every year with p-values as shown above. Here we use the straightforward normal approximation to the multinomial
distribution of a varying number of possible responses to teh query items estimate the p-value.

22

Supplementary Table VI

R ECONSTRUCTION EXAMPLE (2008, SUBJECT NUMBER 1909)
item
abdefctw
abhlth
abnomore
abpoor
absingle
bible
colcom
colmil
conlabor
godchnge
grass
gunlaw
libcom
libhomo
libmil
libmslm
polabuse
pray
prayfreq
shotgun
spkcom
taxrich

description
abortion is wrong if there is a strong chance of serious defect in the
baby
abortion should be legal if mother’s own health is seriously
endangered by the pregnancy
abortion legal if mother does not want any more children
abortion should be legal if family has a very low income and cannot
afford any more children
abortion should be legal if mother is not married and does not want
to marry the man
the bible is the actual word of god and is to be taken literally or is a
book of fables
communist allowed to teach in a college
militarists be allowed to teach in a college or university
confidence in organized labor
which best describes your beliefs about god
use of marijuana should be made legal
require a person to obtain a police permit before he or she could buy
a gun
communist books allowed in your public library
book in favor of homosexuality allowed in public library
allow militarists book in library
allow anti-american muslim clergymen’s books in library
policeman can strike a citizen who says vulgar and obscene things
to the policeman
about how often do you pray
about how often do you pray
own a shotgun
communist allowed to make a speech in your community
describe taxes in america today

true

reconstructed

always wrong

always wrong

yes

yes

no

no

no

no

no

no

word of god
not fired
allowed
only some
believe now, always have
not legal
favor
remove
not remove
not remove
not remove
no
several times a day
several times a day
no
allowed
too high

word of god
not fired
allowed
only some
believe now, always have
legal
oppose
not remove
remove
not remove
remove
no
several times a day
several times a day
no
allowed
much too high

Supplementary Table VII

R ECONSTRUCTION EXAMPLE WITH POOR RECONSTRUCTION PERFORMANCE (2008, SUBJECT NUMBER 1076)❄
item
abany
abdefctw
abdefect
abnomore
abpoor
abpoorw
absingle
bible
colcom
colmil
comfort
conlabor
grass
libcom
libmil
owngun
polabuse
pray
religint
reliten
shotgun
spkcom
spkmil
taxrich

description
abortion should be legal if mother wants it for any reason
abortion is wrong if there is a strong chance of serious defect in the
baby
abortion should be legal if there is a strong chance of serious defect
in baby
abortion legal if mother does not want any more children
abortion should be legal if family has a very low income and cannot
afford any more children
wrong for woman to get abortion if low income
abortion should be legal if mother is not married and does not want
to marry the man
the bible is the actual word of god and is to be taken literally or is a
book of fables
communist allowed to teach in a college
militarists be allowed to teach in a college or university
practicing a religion helps people to gain comfort in times of trouble
and sorrow
confidence in organized labor
use of marijuana should be made legal
communist books allowed in your public library
allow militarists book in library
have in your home any guns or revolvers
policeman can strike a citizen who says vulgar and obscene things
to the policeman
about how often do you pray
people with very strong religious beliefs are often too intolerant of
others
would you call yourself a strong religious person
own a shotgun
communist allowed to make a speech in your community
militarists allowed to make a speech in your community
describe taxes in america today

❄ Probability of getting worse reconstruction is less than 12%

true
yes
not wrong at all

reconstructed
yes
wrong only sometimes

yes

yes

yes

yes

yes

yes

always wrong
yes

almost always wrong
yes

inspired word

inspired word

not fired
not allowed

fired
not allowed

strongly agree
hardly any
not legal
not remove
remove
no
no
lt once a week
agree
not very strong
no
allowed
allowed
too high

agree
hardly any
not legal
not remove
not remove
yes
yes
several times a day
strongly agree
strong
yes
not allowed
not allowed
about right

23

Supplementary Table VIII

P OLAR VECTORS USED TO IDENTIFY IDEOLOGIVAL LEANING TO RACE / GENDER INSENSITIVITY OR VIEWS THAT FAIL TO
PROMOTE SOCIAL EQUALITY

index

description

less
sexism/racism

more
sexism/racism

type

no

race

yes
yes
too much
allowed
oppose pref
disagree
strongly
not remove
allowed
oppose

race
race
race
race
race

disagree

agree

gender

agree

disagree

gender

disagree
for

agree
against

gender
gender

very unlikely

very likely

gender

agree
disagree

disagree
agree

gender
gender

agree

disagree

gender

yes
disagree

no
agree

gender
gender

✖❄

RACDIF2
RACDIF4
natrace
colrac
affrmact

Blacks have worse jobs income etc than white people due to
discrimination
Because most Blacks have less inborn ability to learn
Because most Blacks just donot have sufficient motivation
govt spending on improving the conditions of Blacks
Racists allowed to teach in a college or university
Oppose affirmative action

wrkwayup

Blacks should work their way up without special favors

RACDIF1

librac
spkrac
marblk
fepol
fechld
fepresch
fejobaff
discaffm
fehire
hubbywrk
meovrwrk
abany
fefam

Book written by racists be taken out of your public library
Racists allowed to speak in community speeches
Comfortable having a close relative marry a black person
Most men are better suited emotionally for politics than are most
women
A working mother can establish just as warm and secure a
relationship with her children
A preschool child is likely to suffer if his or her mother works
Preferential hiring of women
Now equally or less qualified woman gets job or promotion instead of
man
Should hire and promote women
A husband should earn money and a wife should look after family
Family life often suffers because men concentrate too much on their
work
Abortion ok for any reason
Man should be the achiever outside while woman takes care of family

yes
no
no
too little
not allowed
support pref
agree
strongly
remove
not allowed
favor

✗❄

✖❄

✗❄

race
race
race
race
