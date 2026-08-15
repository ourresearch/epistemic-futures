---
title: "Inductive Game Theory and the Dynamics of Animal Conflict"
person: david-krakauer
section: by
type: journal-article
year: 2010
date: 2010-05-13
venue: "PLoS Computational Biology"
authors: "David C. Krakauer et al."
source_url: https://doi.org/10.1371/journal.pcbi.1000782
retrieved: 2026-08-13
content: full-text
notes: "OA (gold); OpenAlex W1971475365; cited_by 53. Extracted via pypdf from https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1000782&type=printable."
---

# Inductive Game Theory and the Dynamics of Animal Conflict

## Full text

Inductive Game Theory and the Dynamics of Animal
Conflict
Simon DeDeo 1,2, David C. Krakauer 1, Jessica C. Flack 1,3*
1 Santa Fe Institute, Santa Fe, New Mexico, United States of America, 2 Institute for the Physics and Mathematics of the Universe, University of Tokyo, Kashiwa-shi, Chiba,
Japan, 3 Yerkes National Primate Research Center, Emory University, Atlanta, Georgia, United States of America
Abstract
Conflict destabilizes social interactions and impedes cooperation at multiple scales of biological organization. Of
fundamental interest are the causes of turbulent periods of conflict. We analyze conflict dynamics in an monkey society
model system. We develop a technique, Inductive Game Theory, to extract directly from time-series data the decision-
making strategies used by individuals and groups. This technique uses Monte Carlo simulation to test alternative causal
models of conflict dynamics. We find individuals base their decision to fight on memory of social factors, not on short
timescale ecological resource competition. Furthermore, the social assessments on which these decisions are based are
triadic (self in relation to another pair of individuals), not pairwise. We show that this triadic decision making causes long
conflict cascades and that there is a high population cost of the large fights associated with these cascades. These results
suggest that individual agency has been over-emphasized in the social evolution of complex aggregates, and that pair-wise
formalisms are inadequate. An appreciation of the empirical foundations of the collective dynamics of conflict is a crucial
step towards its effective management.
Citation: DeDeo S, Krakauer DC, Flack JC (2010) Inductive Game Theory and the Dynamics of Animal Conflict. PLoS Comput Biol 6(5): e1000782. doi:10.1371/
journal.pcbi.1000782
Editor: Christophe Fraser, Imperial College London, United Kingdom
Received August 24, 2009; Accepted April 9, 2010; Published May 13, 2010
Copyright: /C2232010 DeDeo et al. This is an open-access article distributed under the terms of the Creative Commons Attribution License, which permits
unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.
Funding: This work received funding from NIH 1 R24-RR024396-01, NSF NSCC 0904863, SFI James S. McDonnell Robustness Program (www.jsmf.org). The
funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.
Competing Interests: The authors have declared that no competing interests exist.
* E-mail: jflack@santafe.edu
Introduction
Conflict is dissipative. Organisms, aggregates, and societies must
overcome the destabilizing consequences of conflict in order to
persist [1–5]. Conflict consequently plays a central role in the
evolution of social organization. Particularly problematic for social
stability is ontogenetic conflict – conflict that finds expression in
fights between individuals over the course of their lifetimes. Much
is understood about control mechanisms [4–11], factors driving
escalation of pair-wise contests [12–15], the influence of third
parties on conflict outcome through coalition formation [16,17],
audience [18,19] and reputation effects [20], and redirected
aggression [21]. Somewhat paradoxically, less is understood about
the causes of conflict, and almost nothing is known about the
dynamics of multiparty conflict –conflicts that spread to involve
more than two individuals to encompass a sizable fraction of a
group. Multiparty conflicts are common in many gregarious
individual societies [22]. In these systems, it is often difficult to
establish why individuals become involved in an ongoing fight or
why the fight started.
A standard assumption is that individual strategies are highly
tuned to resource competition. Under this assumption the cause of
any single conflict is immediate competition for resources over
short time intervals. The probability of fighting depends directly
on the payoff obtained from acquiring the resource in the present.
These resources can include food, mates and dominance status.
The latter is thought to improve access to food and mates.
However, individual memory for previous interactions can alter
the occurrence and course of future conflicts, promoting longer-
timescale, competitive dynamics. This is because memory for
regular patterns of past conflict facilitates prediction of future
conflict, allowing individuals to respond strategically. It is well
understood, for example, that competition for dominance between
a pair of individuals can be played out over many months and
involve alliances and coalitions [23]. Memory can also introduce
costs, as it can lead to the amplification of conflict or to the
eruption of a sequence of related fights: a ‘‘cascade’’ [24,25]. Such
turbulent periods can increase the probability of injury and stress,
both of which are associated with increased mortality [26]. Large
conflicts can increase the probability that individuals not involved
in an initial dispute will be drawn in, and so can increase the
‘‘population cost’’ of conflict. Thus critical questions include: how
do individuals decide to fight, are multiparty conflicts are reducible
to pair-wise interactions or do they involve irreducible higher-
order interactions. How do alternative decision-making rules, or
strategies, effect inter-conflict dynamics and organizational
stability, and what role does memory play in amplifying and
dampening conflict?
Addressing these questions in multiplayer systems requires
models that make few or no assumptions about payoffs, as these
are rarely known, and which are tractable when allowing for
higher-order interactions (more than pairwise interactions). In
standard game theory models – a canonical approach to the study
of conflict – payoffs are posited, higher order strategic interactions
are typically neglected, and data rarely derive from temporally
resolved, natural observations of strategic interactions. The goal is
PLoS Computational Biology | www.ploscompbiol.org 1 May 2010 | Volume 6 | Issue 5 | e1000782

to provide solution concepts for games that find uninvadible
strategies, rather than to extract from the data directly those
strategies individuals are playing [27].
To complement these standard deductive game theoretic
approaches, we introduce Inductive Game Theory , in which the
strategies used by individuals, and their consequences for social
dynamics, are derived computationally from highly resolved time-
series data on competitive processes. Methodologically, this
approach borrows from statistical inference methods now standard
in genetics. The goal in genetics is typically to reconstruct gene
interactions from expression-profile, time-series. The problem is
that the number of transcripts is usually far greater than the
number of independent observations. Hence priors need to be
imposed on permissible solutions. The goal of Inductive Game
Theory is to extract decision-making strategies and behavioral
time series from known interaction networks. Hence these
problems are in some sense inverse of each other. In the
Discussion, we return to this issue, expanding the scope of IGT
to consider non-conflict time series.
In the body of the paper we develop the inductive game theory
approach and apply it to a conflict data set from a pigtailed
macaque ( Macaca nemestrina ) group. The macaque ( Macaca) genus
and its subset species are natural model systems for studying the
role of complex conflict dynamics in social evolution. This is
because in macaque societies individual decision making is plastic
and guided by learning, conflict is frequent and typically involves
multiple, unrelated players, and social dynamics occur over
multiple timescales [28,29]. The particular pigtailed macaque
group we study contains 48 socially-mature individuals (84
individuals in total) housed socially in a large compound at the
Yerkes National Primate Research Center Field Station in
Lawrenceville, Georgia (see Empirical Methods.) Data were
collected over a series of four months in which the group was
stable (no reversals in dominance status). Conflict events – ‘‘fights’’
– in this group vary in duration, number of participants, and other
measures of severity [4,9]. Because the entire sequence of conflict
events was collected, including data on fight duration, participant
identity, and participant behavior, we are able to construct a
highly-resolved time-series for each observation period. A total of
1,096 fights in 158 hours were observed over the study period; the
names of individuals in each fight were recorded.
Time Series Correlations
We begin by asking whether fight sizes are correlated in time.
An example time-series, from a single eight-hour observation
period and showing fight size and duration, is in Fig. 1; one may
construct from this various autocorrelation functions. Surprisingly,
the sizes of fights are nearly uncorrelated over the course of the
day. Larger-than-average fights do not, for example, predict the
appearance of larger-than-average fights later. This is discussed in
greater detail in the Supporting Information.
We then ask whether there are correlations across fights in
membership – does the the appearance of individual A in a fight at
time step one predict the appearance of B in the next fight? For
simplicity, the only within-fight information we use is individual
identity data; we do not take into account individual behavior ( e.g.,
aggressor, recipient, intervener, and so forth – see Empirical
Methods), nor do we consider which individuals interacted within
fights. Given this, the simplest correlations we can observe are
correlations in membership across fights separated by one peace
bout. We write these PA ?BðÞ , estimated as NB DAðÞ =NAðÞ : the
number of fights involving B that followed a fight involving A,
divided by the number of fights involving A. Informally, PA ?BðÞ
gives the probability of observing B in a conflict given that one has
just observed a conflict involving A.
The probabilities will vary for different pairs of individuals. In
order to remove time-independent effects on individual participa-
tion in fights, we compute DPA ?BðÞ ; the difference between the
null-expected P and that measured from the data:
DPA ?BðÞ ~
NB DAðÞ {Nnull BDAðÞ
NAðÞ , ð1Þ
where Nnull BDAðÞ is the average from a large Monte Carlo set of
null models generated by time-shuffling the series but not shuffling
identities within fights. Fig. 2 shows some of the strongest
correlations of this form found between the 48 individuals, in
the form of a directed graph.
Correlations across fights can also be generated by subgroups
deciding to fight in response to other subgroups fighting
previously. There are several possible variations in subgroup-
generated correlations. We consider only the two computationally
simplest correlational structures. Correlations of the form
DPA B ?CðÞ reveal the extent to which the presence or absence
of a pair of individuals at one time predicts the appearance of a
particular individual at the next step. They can be defined:
DPA B ?CðÞ ~
NC DABðÞ {Nnull CDABðÞ
NA BðÞ , ð2Þ
as can DPA ?BCðÞ , the extent to which the presence of an
individual at the previous step predicts the presence of a pair at the
next step:
DPA ?BCðÞ ~ NB C DAðÞ {Nnull BCDAðÞ
NAðÞ , ð3Þ
Using this combinatorial Monte Carlo technique, we find
significant correlations for both these structures. Plots of the
distribution of these three correlations can be found in the
Supporting Information. As one measures higher-level correla-
Author Summary
Persistent conflict is one of the most important contem-
porary challenges to the integrity of society and to
individual quality of life. Yet surprisingly little is under-
stood about conflict. Is resource scarcity and competition
the major cause of conflict, or are other factors, such as
memory for past conflicts, the drivers of turbulent periods?
How do individual behaviors and decision-making rules
promote conflict? To date, most studies of conflict use
simple, elegant models based on game theory to
investigate when it pays to fight. Although these models
are powerful, they have limitations: they require that both
the strategies used by individuals and the costs and
benefits, or payoffs, of these strategies are known, and
they are tied only weakly to real-world data. Here we
develop a new method, Inductive Game Theory, and apply
it to a time series gathered from detailed observation of a
primate society. We are able to determine which types of
behavior are most likely to generate periods of intense
conflict, and we find that fights are not explained by
single, aggressive individuals, but by complex interactions
among groups of three or higher. Understanding how
memory and strategy affect conflict dynamics is a crucial
step towards designing better methods for prediction,
management and control.
Inductive Game Theory
PLoS Computational Biology | www.ploscompbiol.org 2 May 2010 | Volume 6 | Issue 5 | e1000782

tions, between, for example, triplets and individuals, the effective
sample size – number of relevant observations (the conditional
Nx DyðÞ and Nnull xDyðÞ ) – drops, while the number of parameters
to estimate rises combinatorically. This leads to a rapid decrease in
signal-to-noise on any one observable.
Extracting overall significance levels for DP measurements
requires caution. For example, since individuals are correlated
within fights, and these correlations are maintained by the null
model, the various DP measurements are not independent of each
other. A Monte Carlo simulation of the expected numbers of
correlations confirms that the excess of positive DP values in the
observed data is significant at pv0:001; these issues are discussed
in greater detail in the Supporting Information.
A similar analysis can be done for two-step correlations between
named individuals and groups; while individual detections can be
made, Monte Carlo simulations of the expected noise properties of
the DP measurement suggest that such correlations, should they
exist, are too weak to detect even in the full sample of 1096 fights.
The Space of Strategies
Given the observed correlations, we now consider the causal
mechanisms underlying the detectable individual and subgroup
correlations. To do so, we introduce a class of minimal models for
social reasoning, or ‘‘strategy space.’’ Full specification of these
models is in the Supporting Information section, ‘‘Simulation
Specification.’’
We suppose that each individual or subgroup decides whether
to join a fight based on composition of the previous fight. The
space of possible strategies can then be written as C n,mðÞ ,w h e r e
n is the size of the relevant group in the previous fight, and m is
the number of individuals ma king the decision. We allow
decisions to be probabilistic ( ‘‘mixed,’’ in the game theory
terminology), so that a particula r fight composition can lead,
with some probability distrib ution, to different kinds of
subsequent fights.
Each element of a C n,mðÞ strategy is a number between z1 and
{1, specifying the probability that the appearance of a particular
n-tuple leads to a recommendation that a particular m-tuple join,
or avoid, the next fight. These probabilities derive directly from
the data, using the equations given in the previous section to
determine whether there is a significant identify correlation across
fights between two individuals or pairs. A negative value can be
interpreted as repulsion or inhibition, and a positive value can be
interpreted as attraction or stimulation.
Figure 1. Conflict event time-series data from one observation period. Begins at 12:00 hours, and ends just after 20:00 hours. Plotted on the
y-axis as ‘‘Total Fight Size’’ is the number of conflict participants per conflict, regardless of whether the participant was an aggressor, recipien t, or
intervener. The graph gives a sense of the distribution of conflict sizes, and conflict lengths, and the distribution of intervening peaceful period s.
Hatched bars indicate periods without data collection.
doi:10.1371/journal.pcbi.1000782.g001
Inductive Game Theory
PLoS Computational Biology | www.ploscompbiol.org 3 May 2010 | Volume 6 | Issue 5 | e1000782

In the case that a particular m-tuple receive multiple, possibly
incompatible, recommendations to join or avoid, which is always
possible because each fight has a minimum of two individuals
involved, the decision to join or avoid can be resolved by
introducing a temperament parameter, which we call a ‘‘combina-
tor.’’ We choose AND and OR to capture the two ends of the
spectrum of individual temperaments. Under the conflict averse,
or conservative AND combinator, an m-tuple must receive
recommendations to join from all relevant n-tuples. Under the
maximally conflict-prone OR combinator, a single recommenda-
tion to join is sufficient.
We begin with a randomly generated, spontaneous ‘‘seed’’ pair.
These seeds can trigger a subsequent series of fights (a ‘‘cascade’’)
that in our simulation build up a time series. At some point, a
particular fight may lead to no recommendations to join, or a
recommendation that only a single individual join; at this point,
the cascade ends, and a new seed pair is chosen.
This is a (one-step) Markov model; the restriction to single, as
opposed to multi-step models can be justified in part by the
absence of detectable correlations at two steps, discussed above,
and by the reproduction of this absence in the outputs of the one-
step model. Different C n,mðÞ and combinator choices amount to
Figure 2. The network of the strongest correlations detected in the data set, shown as directed edges between individuals. DP (as
defined in Eq. 1) positive is denoted as a solid line, and DP negative as a dashed line; arrows denote the forward direction of time. Edges with DDPD
above 6% (at 95% confidence) are shown; note that detections of different edges are not independent. Node color indicates frequency, with blue
meaning rare in fights, and red, frequent.
doi:10.1371/journal.pcbi.1000782.g002
Inductive Game Theory
PLoS Computational Biology | www.ploscompbiol.org 4 May 2010 | Volume 6 | Issue 5 | e1000782

constraining the 248|248 transition matrix. The estimation of
maximum-likelihood transition probabilities in (hidden) Markov
models is often accomplished with a variant of the EM algorithm
[30]; however, even in the simplest model, C 1,1ðÞ , the number of
parameters (48
2~2304) to be estimated is larger than the number
of events (1096 fights), and so such iterative methods are unlikely
to reliably converge.
On the other hand, determining the parameters directly by
searching the full parameter space is impossible. In this
exploratory work, we instead make a convenient Ansatz. Specif-
ically, we take the elements of C n,mðÞ to be equal to the
corresponding measurement of the DP between the relevant n-
and m-tuple. In the discussion of results (‘‘How Specific are the
Strategies’’), we consider a number of alterations from this first
guess as a way to assess the flatness of the likelihood and thus to
suggest, for future investigations, how to reduce the dimensionality
of the parameter space.
Our choice should be reasonably close to the maximum of the
likelihood when fights are small and do not grow or shrink too
quickly. We find that some choices of strategy class both
‘‘validate’’ (approximately reproduce the DP measurements
used to specify them) and ‘‘predict ’’ (reproduce other features of
t h ed a t at h a td on o td i r e c t l yi n f l u e n c et h ev a l u e so ft h e i r
parameters.)
As shown in Fig. 3 we can define a systematic, discrete space of
C n,mðÞ models that stand in hierarchical relation to one another.
Increases in n correspond to an increase in the memory capacity of
decision makers. Increases in m correspond to an increase in
Figure 3. Lattice classification of strategy space. All strategies live in the space of 1-step Markov transition functions. Starting with the simplest
model class C 1,1ðÞ , we can add individuals to either the first or second fight, systematically building up strategies of increasing complexity based on
cognitive, coordination, and computational requirements.
doi:10.1371/journal.pcbi.1000782.g003
Inductive Game Theory
PLoS Computational Biology | www.ploscompbiol.org 5 May 2010 | Volume 6 | Issue 5 | e1000782

coordination among individuals. Hence the space defines an
hierarchy of memory and information processing requirements.
We confine the space of models we consider to those in which
nƒ2 and mƒ2, as the strategies of higher-order models are
unlikely to be within the cognitive capabilities of the individuals. In
principle, C n,mðÞ can be extended systematically to (i) larger values
of n and m, (ii) include a combinator with more complicated
functional dependence, and (iii) accommodate longer timescales,
for example, by expanding the dimension of the strategy space
from C n,mðÞ to C n,m,pðÞ , and even C n,m,p,zðÞ , where p and z
respectively refer to the second and third time steps from the initial
fight. Later in the Results section, we consider how factors like
power [4] affect strategy use by individuals. Such factors can be
incorporated into the IGT framework but caution is warranted as
it is nontrivial to do so systematically; we defer this question to
future work.
Three Hypotheses
We consider C 1,1ðÞ , C 2,1ðÞ and C 1,2ðÞ , with either combinator.
Thus each hypothesis has two variants.
C 1,1ðÞ includes only pair-wise decision making strategies that do
not require any coordination between conflict participants fighting
in the second time-step. We call this the Rogue Actor Hypothesis –a n
individual’s involvement in a conflict provokes others to become
involved in subsequent conflicts. Rejection of this model would
suggest that individuals – by either appearing in many fights
themselves or by repeatedly provoking others – are not the
primary cause of fights or cascades.
C 2,1ðÞ means that an individual decides to participate in a
subsequent conflict based on the presence or absence of a
particular pair of individuals in the previous bout. This model
includes triadic-decision making strategies. Rejection of this model
would rule out what we call the Triadic Discrimination Hypothesis –
individuals make strategic decisions about whether to engage in
the present conflict based on who fought with whom previously,
and their strategic relation to that pair.
C 1,2ðÞ means that the decision of a pair of individuals to
participate in a subsequent conflict is based on the presence or
absence of a particular individual in the previous bout. This model
includes triadic decision-making strategies that additionally require
coordination of participants in the second time-step. Rejection of
this model would rule out what we call the Triadic Coordination
Hypothesis – individuals jointly decide to fight in a subsequent bout
based on the presence of a particular individual in the previous
bout, and their strategic relation to that individual.
Higher-order strategies are in general irreducible – not
decomposable into the products of lower-order strategies. In the
language of statistical inference, C 1,1ðÞ is nested within the other
two strategies; imposing equality constraints allows them to
approximate C 1,1ðÞ . With these three hypotheses in hand, we
can produce simulations of the empirical time series, whose
predictions we analyze below.
Results
Conflict Size
We test these hypotheses against each other by simulating
conflict dynamics using the C n,mðÞ models. We run one simulation
for each C n,mðÞ +combinator model. We ask how well each of the
resulting simulated distributions of fight sizes fits the empirical
distribution; the total number of simulated fights is at least 100
times larger than that observed, allowing Monte Carlo estimates of
the statistical properties of observable parameters.
The simulations tell us three things. One is the implication of
each C n,mðÞ model and its associated strategies for conflict
dynamics, including cascade severity. Another is which of the
models better reproduces the data, and thus which of the C n,mðÞ
strategies individuals and subgroups are more likely to be playing
in the group. A third insight given by the simulations is how much
information the individuals are using, when playing a particular
strategy, about other individuals and their interactions.
We operationalize conflict size using a measure we call the
‘‘long fraction’’ (Fig. 4). The long fraction is the number of fights of
size i, divided by the total number of fights larger than two;
formally,
LF iðÞ ~
NiðÞ
P48
j~3
NjðÞ
, ð4Þ
where NiðÞ is the number of fights of size i; the maximum fight
size of 48 comes from the total number of socially-mature
individuals in the group. The long fraction is a measure of cascade
severity, showing how large fights can grow due to the combined
strategies of individuals and subgroups. We consider only fights
larger than two in size in order to reduce the influence of seed pair
composition on the analysis.
As shown in Fig. 4, the most striking feature of the simulations is
the vastly different conflict sizes generated by the different
strategies. In the cases considered, these differences allow us to
quickly rule out certain simple models. Two of the variants we
consider, C 1,1ðÞ + AND and C 1,1ðÞ + OR, lead to ‘‘anomalous
quiescence’’ – few fights are sufficiently motivating to the group to
be consequential. Even if a small conflict manages to double in
size, it is rarely able to double again.
We find that in three cases the models lead to ‘‘forest fires’’ –
conflict expands in a cascade that engulfs the group, with nearly all
individuals participating, and refuses to die down. These are
C 2,1ðÞ + OR, C 1,2ðÞ + OR, and C 1,2ðÞ + AND. These strategies do
not reproduce the data. Since neither combinator for C 1,2ðÞ
works, we rule out the Triadic Coordination Hypothesis.
Only C 2,1ðÞ + AND reproduces the distribution of fight sizes.
This supports the Triadic Discrimination Hypothesis – individuals
decide to fight based on their relation to pairs in previous fights. A
small surplus of fights in the data at the very largest fight sizes
(§10) suggests that strategies of other models might come into
play at these extremes.
This might happen, for example, if during turbulent periods
individuals form coalitions in response to the perceived coalitions
of others – C 2,2ðÞ . However, the frequency with which this model
is used is likely to be low given it requires a level of coordination
made difficult by constraints imposed by spatial considerations and
limited capacity for communication [31] among the individuals in
individual societies. Model C 2,1ðÞ on the other hand does not
require coordination.
The Triadic models, and C 2,1ðÞ + AND in particular, have
(formally) many more parameters than the Rogue Actor
Hypotheses. A study of the comparative Akaike Information
Criterion (AIC) values, an information theoretic criterion that
includes a penalty for model complexity, shows that the
improvement in goodness-of-fit is sufficient to compensate; this is
discussed in detail in Supporting Information.
As we noted earlier, the autocorrelation function finds no
significant fight size correlations; our model also reproduces this
feature. Below we consider a wider range of observables to see how
well the Triadic model performs.
Inductive Game Theory
PLoS Computational Biology | www.ploscompbiol.org 6 May 2010 | Volume 6 | Issue 5 | e1000782

Conflict Cost
We find in our simulations that the different C n,mðÞ strategies
have different implications for cascade size – the pairwise strategies
produce small cascades, whereas the triadic strategies produce
longer cascades, with the conflict prone variants producing the
longest. Here we show, using data taken simultaneously with the
time series, that in addition to the assumed costs and benefits to
individuals from playing a particular strategy ( e.g., that triadic
strategies allow individuals to strategically respond to the
interactions of others, whereas pair-wise strategies allow no such
social ‘‘tuning’’), there is a group cost to playing strategies that
produce large fights. (We refer the reader to the Empirical
Methods for important operational definitions and statistical
methods used in this section.)
We consider two measures of group cost. These measures
capture how likely an individual is to receive aggression given the
eruption of a conflict in size class i. The first is the (population)
mean frequency of contact aggression ( e.g., tumbling, wrestling,
biting) received by group members during fights in size class, X
i .
The second is the (population) mean frequency of redirected
aggression ( e.g., aggression directed by a conflict participant to a
third party) received by group members during fight in size
class, Y
i . The total number of fights in size class i is given
by Fi . The total number of fights in size class i in which
individual j receives contact aggression is xij and redirected
aggression, yij . The aforementioned population-level means are
then, Xi ~ 1
48Fi
X
j xij and Yi ~ 1
48Fi
X
j yij . For all large fights
(fights size w4) L~ P36
i~5 Fi , and the means are given by
XL~ 1
48L
X
j
X36
i~5 xij , and YL~ 1
48L
X
j
X36
i~5 yij . For con-
tact aggression received, the fight sizes are 2, 3, 4, and w4. For
redirected aggression received, the fight sizes are 3, 4, w4. By
definition, there can be no redirected aggression in fights of size
two.
Measuring cost with respect to all individuals in the population
rather than conditioning the calculation only on the individuals
who fight allows us to capture the consequences to the group of
Figure 4. Individuals play triadic, not pairwise, strategies, and it is this triadic decision-making that produces turbulent periods.
This plot shows the distribution of fight sizes in the real data (red line) and the simulated distributions under each C 2,1ðÞ hypothesis. We plot the
‘‘long fraction,’’ the number of fights of a certain size, divided by the number of fights larger than two participants. In green is shown the 95%
confidence contours for C 1,1ðÞ + OR; the model is unable to generate conflicts of sizes much larger than three. The stricter variant, C 1,1ðÞ + AND,
performs even more poorly. In orange is shown C 2,1ðÞ + OR. Its distribution has a significant fraction of conflicts larger than eight individuals. In
yellow is C 1,2ðÞ + AND. Even though this is the ‘‘conflict-averse’’ variant ofC 1,2ðÞ , it produces many large fights over time such that the distribution
is ‘‘inverted’’ and there are more large fights than small fights.C 1,2ðÞ with the more ‘‘conflict prone’’OR combinator produces even larger cascades
that grow so quickly good statistics become computationally impossible. Dark blue is the 95% contour and light blue is the 68% contour for the
distribution generated by C 2,1ðÞ + AND, the only model that can capture important features of the data. This triadic strategy cannot be decomposed
into pairwise strategies.
doi:10.1371/journal.pcbi.1000782.g004
Inductive Game Theory
PLoS Computational Biology | www.ploscompbiol.org 7 May 2010 | Volume 6 | Issue 5 | e1000782

variation in the individual proclivity to fight as well as in strategy
variation. All else being equal, the population cost of 10
individuals fighting in a group of 10 is higher than the cost of
10 individuals fighting in a group of 100. Second, by considering
redirected aggression, we capture how conflict size affects the
likelihood that an individual uninvolved in the dispute will be
drawn in.
As shown in Figs. 5 and 6, we find, using a paired Wilcoxon
signed ranks test, significantly more contact aggression is received
by group members when fights are of size 3 than when fights are of
size 2 (one-tailed, n~48, pv0:001), when fights are of size 4 than
when fights are of size 3 (one-tailed, n~48, pv0:001), and when
fights are of size w4 than when they are of size 4 (one-tailed,
n~48, pv0:001). Note that the relation between contact
aggression received and fight size is nontrivial: aggressors need
not use contact aggression and some individuals participate
without using or receiving aggression (Methods). Consequently,
contact aggression received does not necessarily increase with
increasing fight size. Using a paired Wilcoxon Signed Ranks Test
we also find significantly more redirected aggression is received by
group members when fights are of size 4 than when they are of size
3 (one-tailed, n~48, pv0:05), and when fights are of size w4
than when they are of size 4 (one-tailed, n~48, pv0:001).
These results, in conjunction with the results reported in Fig. 4,
suggest that conflict decision-making strategies based on triadic
memory are associated with a higher population cost than
Figure 5. Large fights cost more – increased redirected aggression. Shown are box plots for the mean frequency of redirected aggression
received per individual for conflicts of a given size. Conflict sizes were binned so that each category contained an approximately equivalent number
of events and to reflect natural categories ( e.g. pairs and triplets). The heavy black horizontal line in each plot shows the median ‘‘mean value’’. The
bottom and top of the box give the 25th and 75th percentiles, respectively. The vertical dashed lines show 1.5 times the interquartile range (roughly
two standard deviations). The points are outliers, defined as 1.5 times the interquartile range above the third quartile. Note that redirection, by
definition, is not possible in conflicts smaller than triplets. Adjacent pairs of fight sizes were compared using the Wilcoxon signed ranks test to
determine whether the probability of aggression received increases with fight size. The stars indicate the level of significance for differences be tween
adjacent fight sizes.
doi:10.1371/journal.pcbi.1000782.g005
Inductive Game Theory
PLoS Computational Biology | www.ploscompbiol.org 8 May 2010 | Volume 6 | Issue 5 | e1000782

decision-making strategies based on pair-wise memory. Whether
this cost is outweighed by the direct benefits of playing these
strategies is a question for future work.
How Specific are Strategies?
The model C 2,1ðÞ is triadic; an individual makes a decision to join
the present fight depending on the participation of a particular pair of
individuals in the previous fight. For each individual, our simulations
associate a particular probability with every single pair.
The actual strategies are likely to be far less specific. Cognitive and
perceptual constraints mean that a pair might have been perceived as
‘‘Fred and Mary’’ or – at a much lower degree of specificity – as ‘‘Any
Male and Mary.’’ A decision-maker’s response might also not be so
fined graded; instead of a continuum of probabilities, only a finite
number of distinct probabilities might be allowed.
In addition to showing the effect of cognitive and biological
constraints, studying strategy specificity is important for future
work, since by reducing the dimensionality of the space, it could
allow direct maximum likelihood searches (see, e.g., [32].)
We consider two variants of C 2,1ðÞ + AND that are less specific.
These are Shuffled and Coarse-Grained. For clarity, we will sometimes
refer to the original model as Base.
Figure 6. Large fights cost more – increased contact aggression. Shown are box plots for the mean frequency of contact aggression received
per individual for conflicts of a given size. Conflict sizes were binned so that each category contained an approximately equivalent number of events
and to reflect natural categories ( e.g. pairs and triplets). The heavy black horizontal line in each plot shows the median ‘‘mean value’’. The bottom and
top of the box give the 25th and 75th percentiles, respectively. The vertical dashed lines show 1.5 times the interquartile range (roughly two standar d
deviations). The points are outliers, defined as 1.5 times the interquartile range above the third quartile. Note that redirection, by definition, i s not
possible in conflicts smaller than triplets. Adjacent pairs of fight sizes were compared using the Wilcoxon signed ranks test to determine whether th e
probability of aggression received increases with fight size. The stars indicate the level of significance for differences between adjacent fight s izes.
doi:10.1371/journal.pcbi.1000782.g006
Inductive Game Theory
PLoS Computational Biology | www.ploscompbiol.org 9 May 2010 | Volume 6 | Issue 5 | e1000782

The Shuffled models are alterations of Base that re-assign strategies
to the group. As with the base model, each individual maintains a
static set of strategies from fight to fight. However, the sets used are
shuffled compared to the base; we consider three kinds of shuffles.
A Total Shuffle takes all the combinations AB?C, and randomly
reassigns DP values to them from the original set. An Outgoing
Shuffle is shown schematically in Fig. 7. For each of the 48|47=2
incoming pairs AB, it randomly swaps the DP associated with two
outgoing elements. The distribution of the 48 DP values for any
particular pair AB remains constant. When possible, the swaps are
done between pairs with strategies of opposite sign. An Incoming
Shuffle is similar, but for incoming pairs; a particular outgoing
individual C has the same distribution of DP, but they are now
randomly associated with different pairs than in the original set.
The Coarse-Grained models are, like the base and Shuffled, also
C 2,1ðÞ + AND. The particular associations between pairs and
individuals are maintained, but the values of DP are now coarse-
grained to the nearest of a limited set of 2nz1 values. For n of
one, only three values are allowed: DP equal to the average of all
the negative DP, equal to zero, or equal to the average of all the
(strictly) positive DP values. The example of n of two, with two
negative and two positive values of DP allowed, is shown as dotted
lines in panel two of Fig. 4 in the Supporting Information. Given
the data indicating that Macaque perceptual systems have a
logarithmic bias [33], we space the bins logarithmically between
the min and max of the positive and negative ranges.
Testing the coarse-grained models gives a sense of how calibrated
an individual’s response needs to be to reproduce the data. Asn gets
larger, the coarse-grained models are closer and closer to the base
model in terms of the underlyingDP values that dictate the responses
of individuals to different pairs. One can considern
a measure of how
‘‘graded’’ an individual’s responses to a particular pair might be. Ifn
is two, for example, it suggests that individuals class pairs into five
categories – ‘‘don’t care’’ (zero),‘‘avoid’’ and ‘‘strongly avoid’’, and
‘‘join’’ and ‘‘strongly join’’ – with no finer distinction.
Earlier in this section, the long fraction alone was sufficient to
rule out alternative strategies. The long fractions for the different
shuffled strategies, shown in Fig. 8, also have worse x
2 values.
There are, of course, many more observables than simply the fight
size distribution, and we now consider a large set of them. They
are (see the Supporting Information) PAðÞ and P
c ABðÞ , individual
and (connected) pair appearance probability; /C22nnAðÞ and /C22nnA BðÞ ,
average fight size conditional on individual or pair appearance;
and DPA ?BðÞ . In Table 1, we show the Pearson cross-correlation
between the observed data, and the simulations, for the different
shuffles and coarse-grainings.
We may also make preliminary estimates of the change in
likelihood DL from the data; we find that the overall likelihood for
the parameters drops with either shuffling or coarse-graining. The
use of shuffled models also allows us to make a (very preliminary)
assessment of the ‘‘true’’ number of free parameters in the model,
and to penalize the more complicated models; this is discussed in
the Model Complexity section of the Supporting Information.
Evidence for Different Strategy Classes
The base model for which we find support assumes every
individual relies solely on C 2,1ðÞ + AND. Although it is likely that
some of the inconsistency with the data can be removed iteratively
through corrections to the DP’s as part of a high-dimensional
search using an approach similar to Ref. [34], it is worthwhile
asking whether some subset of individuals and pairs, chosen in a
biologically-principled fashion, are better reproduced than others.
In other words, are there subsets of individuals that are
particularly triadic, and other subsets that either care less about
triadic relations or make poorer discriminations?
We illustrate here how our methods allow one to investigate this
question. Individual properties (e.g. sex, age, power scores, etc.) can be
used to group individuals into categories. We can then ask how well
individuals in a particular category are fit by theBase model. This can
be done by considering for all individuals in the category of interest
the two PAðÞ and /C22nnAðÞ measurements, the 94 P
c ABðÞ and /C22nnA BðÞ
measurements, and the 95DPA ?BðÞ measurements, and estimating
the goodness of fit by computing the associated L=n.
By sorting the individuals into groups based on various extrinsic
characteristics, we can determine whether there is evidence for the
employment of strategies other than the triadic model of C 2,1ðÞ +
AND. Here, as an illustration of the method, we sort individuals by
power score. The power score, discussed in detail in Ref. [4], is an
estimate of how much ‘consensus’ there is among individuals in the
group about whether the receiver is capable of using force successfully
during fights. Power structure changes the cost of social interactions,
facilitating the evolution of intrinsically costly interactions, like
policing [9], by supporting a proto-division of labor in which powerful
individuals police and low-power individuals do not. Power structure
can thus change the strategies individuals play. We expect this
variation to influence the extent to which individuals play C 2,1ðÞ .
We find that the highest power individuals, and the lowest power
individuals, are the least-well fit by the data, suggesting that they are
using different strategies from those inC 2,1ðÞ + AND that reproduce
much of the behavior of the intermediate-power individuals. This is
shown graphically in Fig. 9, where the individuals are sorted into
groups of eight in order of decreasing power score.
Discussion
In this paper we have investigated the causes and properties of
conflict in a complex social system. To conduct this investigation
we developed a new conceptual and statistical framework applied
to conflict time series, which we call Inductive Game Theory (IGT.)
IGT allows the researcher to computationally extract from data
candidate strategies individuals employ to make decisions, and to
study using perturbations the effects of alternative strategies on
collective dynamics. IGT takes temporally-varying interaction
networks as input, and uses these as the basis for a statistical
reconstruction of putative, causal networks. These causal network
can be used to simulate conditions of conflict, validated against
observational data out of sample. Standard, deductive models for
the analysis of conflict are not designed to deal with large data sets,
and traditionally assume that strategies, payoffs and equilibria can
be defined in advance of observation.
We have applied IGT to a time series in which there are
multiple conflicts involving multiple players, and higher-order
interactions – a neglected feature of many gregarious societies,
including nonhuman primates, cetaceans, and humans [22], in
which multiple individuals interact at once. We are able to
reproduce a number of features of collective behavior, including
fight sizes. We discover that the triplet of interacting individuals is
an irreducible causal unit for conflict. This is surprising as the
pairwise interaction is commonly assumed to be sufficient to
explain strategic behavior.
IGT can be thought of as a complement to a range of statistical,
network reconstruction techniques. For example, in genetics,
temporal, expression profiles are treated as inputs, and interaction,
or transcriptional, networks the desired output (see, e.g., Ref. [35].)
In IGT we have knowledge of the interactions and seek to derive
the collective dynamics, whereas in gene expression, the dynamics
are observed, and the interactions are estimated. IGT is also
Inductive Game Theory
PLoS Computational Biology | www.ploscompbiol.org 10 May 2010 | Volume 6 | Issue 5 | e1000782

related also to studies of neural networks that invoke a Ising-model
structure to model correlations in the timing of neuronal firings
[34,36]; we differ in that our model invokes a causal process in an
out-of-equilibrium system instead of a maximum entropy
distribution at fixed temperature. All of these techniques attempt
to devise algorithmic approaches to pattern discovery in rich data
sets. It is largely the absence of such data in social dynamics that
has favored the development of simple models that explain
Figure 7. A schematic illustration of one of the Triadic tests – the Outgoing Shuffle. For the incoming pair AB, two outgoing names (here, C
and D) are chosen. The values of the two associated DP, DPA B ?CðÞ and DPA B ?DðÞ , are swapped. New names are chosen and the process
repeated until all the DPs associated with the AB incoming pair have been reassigned. This then is done for all 48|47=2 possible incoming pairs,
and the resultant DP set used to generate conflict cascades.
doi:10.1371/journal.pcbi.1000782.g007
Inductive Game Theory
PLoS Computational Biology | www.ploscompbiol.org 11 May 2010 | Volume 6 | Issue 5 | e1000782

qualitative features of behavior. Whereas IGT has been applied to
conflict in this project, there is nothing preventing these ideas
being applied to a wider range of collective behavioral sequences,
to include prosocial or cooperative behavior, communication, and
even coordinated, motor sequences.
Implications for Social Evolution
Behavior and cognition. We find that the primary cause of
conflicts in a multiplayer, primate population is individuals
responding to the social interactions among others. Neither pair-
wise decision-making, nor immediate competition for resources,
can account for the conflict patterns we observe in the empirical
data. Conflicts are not independent events but are related in time
through individual memory for previous conflicts and participants.
This effect holds despite peaceful periods, defined by the absence
of all overt conflict, separating fights lasting from a few seconds to
more than an hour. We expect memory will play a role in wild
populations, although the signal might be noisier as a result of
ecological stressors not present in captivity.
Identifying strategies individuals use in deciding to fight requires
introducing what we have called a class of minimal models for
social reasoning. These models vary in several important respects.
One is whether the memory underlying the decision to fight is
dyadic or triadic. That individuals primarily use triadic strategies,
coupled to the fact that these strategies are not reducible to pair-
wise interactions, provides further support for the role of triadic
awareness in primate social behavior [37–42].
A second way in which the models vary, is whether joint action
is required. The models we considered were of the form C n,mðÞ ,
where n refers to the number and identity of individuals in the
previous conflict and m refers to the number and identity of
individuals in the conflict. When mw1, m individuals jointly
decide to fight in response to n. Joint action implies coordination.
It is likely that the C n,mðÞ models in which mw1 make greater
cognitive and spatial demands on the decision-makers than those
models for which m~1. That we found little support for the
C 1,2ðÞ strategy is perhaps explained by these increased cognitive
and spatial demands [31].
A third way the models vary is whether the decision-maker is
conflict-averse or conflict prone. Our models assume that a decision-
maker decides to fight based on its response to individuals or pairs
fighting at the previous time step. However, because conflicts can
involve multiple pairs, it is possible that the previous fight included
both pairs who trigger a join response as well as pairs who trigger an
avoid response. To deal with these potential decision-making
conflicts, we introduced a binary combinator term that specified
whether a decision-maker needed a unanimous recommendation
(AND) to join or could be pushed over the edge to join by a single
Figure 8. The sensitivity of the Long Fraction to C 2,1ðÞðÞ + AND model variants. 68% confidence are shown. In blue is the base model. In
orange, a simulation based on strategies that have been shuffled relative to the base model ( Total Shuffle .) In green is a simulation based on
strategies where only the incoming pairs have been shuffled relative to the base model ( Incoming Shuffle.) In red are the data. Both variants of the
base, reliant on triadic decision-making, lie nearer to the data than those strategies of Fig. 4, but still neither are a better fit to the data.
doi:10.1371/journal.pcbi.1000782.g008
Inductive Game Theory
PLoS Computational Biology | www.ploscompbiol.org 12 May 2010 | Volume 6 | Issue 5 | e1000782

recommendation ( OR). Models with an AND combinator we
interpreted as conflict-averse strategies whereas models with OR
combinators we interpreted as conflict-prone strategies.
Although this binary combinator is crude it roughly captures
how a spectrum of temperaments [43] and neuro-endocrine
profiles might influence decision-making strategies by individuals
and their implications for collective conflict dynamics. In the
relatively conciliatory [44] pigtailed macaque society we study, it is
not surprising that the model supported by the data was C 2,1ðÞ +
AND as individuals in this species appear less conflict prone than,
for example, individuals in rhesus ( Macaca mulatta) groups [44]. We
hypothesize that macroscopic variation in aggression across
primate societies [28] reflects variation in the composition of the
fundamental microscopic strategies we have identified inductively.
If so, a conflict prone tuning term can explain why in some
societies we observe frequent aggression-generated mortality,
group fission, and, in captivity, cage wars [45].
A further cognitive issue raised by these results concerns how
much information individuals use to make decisions. Individuals
might tune their strategies to individual identity, responding
differently to each group member, or more approximately, resolve
individuals into classes such as males and females. Analogously,
behavior can be either discrete or continuous – with highly tuned
responses, or graded responses along the lines of ‘strongly avoid’,
‘avoid’, ‘join’ and ‘strongly join.’
The procedure of coarse-graining used in the Results section,
‘‘How Specific are the Strategies,’’ suggests that whereas decision-
makers have graded rather than continuously varying responses to
individuals, they also retain quite fine distinctions between the
pairs they react to. These results are consistent with studies of
primate cognition showing that individuals can identify other
individuals, have the capacity to form numerical representations
and discriminate between highly similar vocalizations [46], can
discriminate among emotional states and facial expressions
[47,48], and have some knowledge of the rank or relative power
of other group members [37,38,49].
Modeling the role of conflict in evolutionary
processes. There are two primary challenges faced by all
complex evolving systems. One is an uncertain, noisy environment.
The other – the topic of this paper – is conflict. Conflict arises when
the interests of system components – whether genes, cells, individuals,
or states – are not fully aligned. Conflict is one of the most important
social factor shaping the evolution of living systems (for many
examples, see Ref. [3]) and is thought to have played a prominent role
in the evolution of cooperation [50,51]. Some suggest that lack of
alignment, or ‘‘frustration’’, in many-body systems is the defining
feature of all complex systems [52].
Theoretical studies of conflict in particular have proceeded
deductively, employing simple models to generate important
intuitions about how payoffs select in evolutionary time stable
strategies individuals play. In these models there typically is no
distinction between evolutionary time and ontogenetic time as the
ontogenetic dynamics are either considered transient (timescale
too fast to be relevant) or fitness is a simple multiple of payoff.
Here we have shown that immediate resource competition does
not, at least directly, drive conflict in ontogenetic time in systems
with multi-party conflict interactions. Memory for social interac-
tions shapes the strategies individuals employ when deciding to
fight, and can generate costly collective conflict dynamics , thereby
influencing the evolution of conflict management. The particular
strategy used by the individuals in our study group, C 2,1ðÞ + AND,
requires that individuals respond to pairs. Compared to other
strategies the individuals could be playing, this triadic strategy
induces potentially manageable but not insignificant conflict
cascades. We found also found that different strategies have
different implications for cascade size and severity, and that larger
fights are on average more costly at the population level. These
results suggest that the costs and benefits of playing a particular
strategy filter back to group members through collective behavior
over relatively long timescales of multiple conflicts, as well as
directly. It is not clear whether a single integrated payoff can
capture these effects.
In addition to the relation bet ween conflict dynamics and
resource competition, our wor k has considered the role of
dynamical interaction structur e. In evolutionary game theory,
interactions are typically pair-wise or, in n-person treatments,
effectively pair-wise as higher-o rder strategic interactions tend
to be neglected in the mean field [16]. Our finding that the
causal unit of conflict dynamics is the triad, not the individual
nor the pair, suggests that individual agency has been
overemphasized in social evolution. It also suggests that
cooperative form and hybrid ga mes [53,54] could come to play
a central role when studying competitive and cooperative
interactions. A cooperativ e form game (in contrast to a
noncooperative form game – t he standard form in most of
evolutionary game theory) is one in which individuals form
higher-order units, typically thro ugh binding contracts, and play
against others through these ‘‘co alitions’’. The m athematical
definition of coalition is effecti vely highly correlated constitu-
ents; cooperative mechanisms are not required. The interaction
structure of these games, as well as that of hybrid games,
appears well-suited to studying the stability properties of the
strategies our results sugges t individuals are playing.
Finally, using IGT it is possible to computationally extract from
data a space of plausible strategies and to study their implications
for collective conflict dynamics without positing payoffs. This
makes IGT a good complement to standard game theory, which
despite its generative power, is well recognized to be weakly tied to
natural-system data [27] and limited by somewhat unrealistic
assumptions concerning stationary pay-offs.
Along with climate change and poverty, conflict is perhaps the
most important contemporary challenge to the integrity of human
society and to improving individual quality of life. Yet in many
Table 1. Pearson correlation coefficients for the model
variants.
Model PðAÞ Pc ABðÞ /C22nn AðÞ /C22nn ABðÞ DP
r A?B
Base 0.62 0.51 0.80 0.37 0.50
Shuffled
Total 0.013 20.007 0.17 0.20 20.026
Outgoing 0.17 0.034 0.12 0.19 0.035
Incoming 0.75 20.053 0.036 0.13 20.15
Coarse Grained
n~1 0.11 0.43 0.34 0.27 0.42
n~2 0.59 0.47 0.60 0.34 0.47
n~4 0.49 0.49 0.75 0.36 0.48
In nearly all cases, the model outperforms the various ‘‘shuffled’’ alternatives,
indicating that the triadic nature of the strategies is central to conflict dynamics.
The effect of coarse graining the strategies is to reduce correlations; as the
number of levels increases and thus finer distinctions are made, the effects
disappear. The data suggest that n~2 (two positive, and two negative, levels)
are sufficient to reproduce much of the group structure.
doi:10.1371/journal.pcbi.1000782.t001
Inductive Game Theory
PLoS Computational Biology | www.ploscompbiol.org 13 May 2010 | Volume 6 | Issue 5 | e1000782

respects little is understood about conflict, particularly its causes
and dynamics over the life time of an individual. This is because
biologists to date have emphasized costs and benefits of conflict in
evolutionary time (measured over many generations). The detailed
analysis of ontogenetic conflict should provide insights into the
behavioral raw material and variability upon which evolutionary
dynamics – both neutral and selective – operates.
Methods
Further details on Monte Carlo simulation methods can be
found in Text S1, available online. Empirical methods are
described below.
Model System
Macaque societies are characterized by social learning at the
individual level, social structures that arise from nonlinear
processes and feedback to influence individual behavior, frequent
non-kin interactions and multiplayer conflict interactions, the cost
and benefits of which can be quantified at the individual and social
network levels [4,5,9,28,29,44,49,55]. These properties coupled to
highly resolved data make this system an excellent one for drawing
inferences about critical processes in social evolution as well as for
developing new modeling approaches that are intended to apply
more broadly.
In this study we focus on one species in the genus, the pigtailed
macaque (Macaca nemestrina). The data set, collected by J.C.
Flack, is from a large, captive, breeding group of pigtailed
macaques that was housed at the Yerkes National Primate
Research Center in Lawrenceville, Georgia. Pigtailed macaques
have frequent conflict and employ targeted intervention and repair
strategies for managing conflict [9]. The study group had a
demographic structure approximating wild populations. Subadult
males were regularly removed to mimic emigration occurring in
wild populations. The group contained 84 individuals, including 4
adult males, 25 adult females, and 19 subadults (totaling 48
socially-mature individuals used in the analyses). All individuals,
except 8 (4 males, 4 females), were either natal to the group or had
been in the group since formation. The group was housed in an
indoor-outdoor facility, the outdoor compound of which was
125665 ft.
Pigtailed macaques are indigenous to south East Asia and live in
multi-male, multi-female societies characterized by female ma-
trilines and male group transfer upon onset of puberty [56].
Pigtailed macaques breed all year. Females develop swellings when
in Œ strus.
Data Collection Protocol
During observations all individuals were confined to the
outdoor portion of the compound and were visible to the observer.
The &158 hours of observations occurred for up to eight hours
daily between 1,100 and 2,000 hours over a twenty-week period
from June until October 1998 and were evenly distributed over the
day. Provisioning occurred before observations, and once during
Figure 9. Going beyond triadic discrimination. Overall L=n as a function of power score, showing how the highest and lowest-power groups
are fit least well by the C 2,1ðÞ + AND strategy assumptions. The 48 individuals are here grouped into units of eight by similarity in power score.
doi:10.1371/journal.pcbi.1000782.g009
Inductive Game Theory
PLoS Computational Biology | www.ploscompbiol.org 14 May 2010 | Volume 6 | Issue 5 | e1000782

observations. The data were collected over a four-month period
during which the group was stable (defined as no reversals in status
signaling interactions resulting in a change to an individual’s
power score, see [49]).
Conflict and power (subordinatio n signal) data were collected
using an all-occurrence sampling procedure [57] in which the
compound was repeatedly scanned from left to right for onset of
conflict or the occurrence of silent-bared teeth displays (used to
measure power, see below). The entire conflict event was then
followed, including start time, end time, and the identity of
individuals involved as aggressors , recipients, or interveners (see
below for operational definitio ns). Although conflicts in this
study group can involve many in dividuals, participation is
typically serial, making it possible to follow the sequence of
interactions. A nearly complete time-series of conflict events is
available for each observation p eriod. Breaks in data collection
during the day occurred sufficiently rarely (seldom more than
once a day), and were sufficie ntly short (seldom more than
fifteen minutes), that results changed little from when correla-
tions were computed assuming no activity during breaks, to not
including any fight pairs sepa rated by a break in correlation
estimators. We avoided altogeth er using fight pairs with fights
on different days.
Instantaneous scan sampling [57] occurred every 15 min for
state behaviours (here, grooming).
Operational Definitions
Grooming: passing hands or teeth through hair of another
individual or plucking the hair with hands or teeth for a minimum
of five seconds.
Conflict: includes any interaction in which one individual
threatens or aggresses a second individual. A conflict was
considered terminated if no aggression or withdrawal responses
(fleeing, crouching, screaming, running away, submission signals)
occurred for two minutes from the last such event. A conflict can
involve multiple pairs if pair-wise conflicts result in aggressive
interventions by third parties or redirections by at least one conflict
participant. In addition to aggressors, a conflict can include
individuals who show no aggression ( e.g. recipients or third-parties
who either only approach the conflict or show affiliative/
submissive behavior upon approaching, see [58].) Because
conflicts involve multiple players two or more individuals can
participate in the same conflict but not interact directly.
Contact aggression: aggression received by one group member
from another that involves grappling, tumbling, hitting, slapping,
or biting.
Power-disparity: difference between two individuals in their
power scores. Power scores for each individual in this study were
calculated using a procedure described in [49]. In brief, the total
frequency of peacefully-emitted subordination signals received by
an individual over a given duration (in this case, the study
duration, which was approximately four months) is corrected for
the uniformity (measured using Shannon entropy) of its distribu-
tion of signals received from its population of potential senders (all
socially-mature individuals). This equation quantifies how much
consensus there is among individuals in the group about whether
the receiver is capable of using force successfully during fights.
Redirected aggression: aggression or threat directed from a
conflict participant towards a third-party during or within
5 seconds of the conflict.
Subordination signal: the subordination signal in the pigtailed
macaque communication repertoire is the silent bared-teeth
display [58]. Bared-teeth (BT) displays are marked by a retraction
of the lips and mouth corners such that the teeth are partially
bared. In pigtailed macaques, the SBT occurs in two contexts:
peaceful and agonistic SBT see [58]) Signals in both contexts are
highly unidirectional. The agonistic SBT encodes submission. The
peaceful variant signals agreement to primitive social contract in
which the signaler has the subordinate role [58]. The network of
SBT interactions encodes information about power structure [49].
Statistical Analyses of Empirical Data
In the results of the main paper, we presented results obtained
using Wilcoxon Signed Ranks Tests on two measures of cost,
contact aggression received and redirected aggression received.
We preformed multiple (three for contact aggression received and
two for redirected aggression) independent Wilcoxon tests per cost
measure instead of one overall Friedman test (nonparametric
version of repeated measures) per measure because the post hoc
planned comparison tests associated with the Friedman test
typically do not have enough power to detect differences across
treatments. We performed nonparametric tests rather than
parametric tests because our data violated the homogeneity of
variance assumption.
Ethics Statement
The data collection protocol was approved by the Emory
University Institutional Animal Care and Use Committee and all
data were collected in accordance with its guidelines for the ethical
treatment of nonhuman study subjects.
Supporting Information
Text S1 Supporting information for the main MS.
Found at: doi:10.1371/journal.pcbi.1000782.s001 (0.16 MB PDF)
Acknowledgments
We thank our three referees for detailed comments on our manuscript. We
thank D. Eric Smith (Santa Fe) and Paul Sheridan (Tokyo Institute of
Technology) for discussion, and Frans de Waal for support during data
collection and the staff of YNPRC for help with data collection.
Author Contributions
Conceived and designed the experiments: JCF. Performed the experi-
ments: JCF. Analyzed the data: SD JCF. Wrote the paper: SD DCK JCF.
Contributed to design of simulations: SD DCK JCF. Coded the
simulations: SD. Contributed to data analysis: DCK.
References
1. Buss L (1987) The evolution of individuality. Princeton, NJ: Princeton University
Press.
2. Michod R (2000) Darwinian Dynamics: Evolutionary Transitions in Fitness and
Individuality. Princeton, NJ: Princeton University Press.
3. Burt A, Trivers R (2006) Genes In Conflict: The Biology of Selfish Genetic
Elements Belknap Press.
4. Flack JC, Krakauer DC, de Waal FBM (2005) Robustness mechanisms in
primate societies: A perturbation study. P Roy Soc B – Biol Sci 272: 1091–1099.
5. Flack JC, Girvan M, de Waal FBM, Krakauer DC (2006) Policing stabilizes
construction of social niches in primates. Nature 439: 426–429.
6. Dreber A, Rand DG, Fudenberg D, Nowak MA (2008) Winners don’t punish.
Nature 452: 348–351.
7. Clutton-Brock T, Parker G (1995) Punishment in animal societies. Nature 373:
209–216.
8. Frank S (2003) Repression of competition and the evolution of cooperation.
Evolution 57: 693–705.
9. Flack JC, de Waal FBM, Krakauer DC (2005) Social structure, robustness, and
policing cost in a cognitively sophisticated species. Am Nat 165: E126–E139.
10. de Waal FBM (2000) Primates - a natural heritage of conflict resolution. Science
289: 586–590.
Inductive Game Theory
PLoS Computational Biology | www.ploscompbiol.org 15 May 2010 | Volume 6 | Issue 5 | e1000782

11. Aureli F, de Waal F, eds. (2000) Natural Conflict Resolution. Berkeley:
University of California Press.
12. Clutton-Brock T, Albon SD, Gibson RM, Guinness FE (1979) The logical stag:
Adaptive aspects of fighting in red deer (cervus elaphus l.). Anim Behav 27:
211–225.
13. Maynard Smith J (1974) The theory of games and the evolution of animal
conflicts. J Theor Biol 47: 209.
14. Parker G, Rubenstein DI (1981) Role of assessment, reserve strategy, and
acquisition of information in asymmetric animal conflicts. Anim Behav 29:
221–240.
15. Taylor PW, Elwood RW (2003) The mismeasure of animal contests. Anim
Behav 65: 1195–1202.
16. Mesterton-Gibbons M, Sherratt TN (2006) Coalition formation: a game-
theoretic analysis. Behav Ecol 18: 277–286.
17. Noe R, Hammerstein P (1995) Biological markets. Trends Ecol Evol 10:
336–339.
18. Johnstone RA (2001) Eavesdropping and animal conflict. P Natl Acad Sci USA
98: 9177–9180.
19. Covas R, McGregor PK, Doutrelant C (2007) Cooperation and communication
networks. Behav Process 76: 149–151.
20. Nowak M, Sigmund K (1998) Evolution of indirect reciprocity by image scoring.
Nature 393: 573–577.
21. Kazem AJN, Aureli F (2005) Redirection of aggression: Multiparty signaling
within a network. In: McGregor P, ed. Animal Communication Networks,
Cambridge: Cambridge University Press.
22. Harcourt S, de Waal FBM, eds. Coalitions and Alliances in Humans and Other
Animals. Oxford: Oxford University Press.
23. de Waal F (1982) Chimpanzee Politics: Power and Sex Among the Apes.
London: Jonathan Cape.
24. Boehm C (1987) Blood Revenge: The Enactment and Management of Conflict
in Montenegro and Other Societies. The University of Pennsylvania Press.
25. Cairns ED, Roe MD, eds. (2003) The Role of Memory in Ethnic Conflict
MacMillan.
26. Sapolsky R (2005) The influence of social hierarchy on primate health. Science
308: 648–652.
27. Leimar O, Hammerstein P (2006) Facing the facts. J Evol Biol 19: 1403–1405.
28. Flack J, de Waal F (2004) Dominance style, social power, and conflict
management: A conceptual framework. In: Thierry B, Singh M, Kaumanns W,
eds. Macaque Societies: A Model for the Study of Social Organization,
Cambridge: Cambridge University Press. pp 157–181.
29. Thiery B, Singh M, Kaumanns W, eds. Macaque Societies: A Model for the
Study of Social Organization. Cambridge: Cambridge University Press.
30. Dempster A, Laird N, Rubin D (1977) Maximum likelihood from incomplete
data via the EM algorithm. J Roy Stat Soc B Met 39: 1–38.
31. Miller JH, Butts C, Rode D (2002) Communication and cooperation. J Econ
Behav Organ 47: 179–195.
32. Turner R (2008) Direct maximization of the likelihood of a hidden Markov
model. Comput Stat Data An 52: 4147–4160.
33. Nieder A, Miller EK (2003) Coding of cognitive magnitude: Compressed scaling
of numerical information in the primate prefrontal cortex. Neuron 37: 149–57.
34. Schneidman E, Berry M, II R, Bialek W (2006) Weak pairwise correlations
imply strongly correlated network states in a neural population. Nature 440:
1007.
35. Bansal M, Belcastro V, Ambesi-Impiombato A, di Bernardo D (2007) How to
infer gene networks from expression profiles. Mol Syst Biol 3: 78.
36. Tkacik G, Schneidman E, Berry MJ, Bialek W (2006) Ising models for networks
of real neurons. arXiv q-bio/0611072.
37. Silk J (1999) Male bonnet macaques use information about third-party rank
relations to recruit allies. Anim Behav 58: 45–51.
38. Cheney D, Seyfarth R (1999) Recognition of other individuals’ social
relationships by female baboons. Anim Behav 58: 67–75.
39. Seyfarth RM, Cheney DL (2000) Social awareness in monkeys. Am Zool 40:
902–909.
40. de Waal FBM (2003) Social syntax: The if-then structure of social problem
solving. In: de Waal FBM, Tyack PL, eds. Animal Social Complexity,
Cambridge, MA: Harvard University Press. pp 230–248.
41. Perry S, Barrett HC, Manson JW (2004) White-faced capuchins exhibit triadic
awareness in their choice of allies. Anim Behav 67: 165–170.
42. Barrett L, Henzi P (2005) The social nature of primate cognition. P Roy Soc B –
Biol Sci 272: 1865–1875.
43. Clarke A, Boinsky S (2005) Temperament in nonhuman primates. Am J Primatol
37: 103–125.
44. Thierry B (2000) Conflict management patterns across macaque species. In:
Aureli F, de Waal F, eds. Natural Conflict Resolution, Berkeley: University of
California Press. pp 106–128.
45. McCowan B, Anderson K, Heagarty A, Cameron A (2007) Utility of social
network analysis for primate behavioral management and well-being. Appl
Anim Behav Sci 109: 396–405.
46. Jordan KE, Brannon EM, Logothetis NK, Ghazanfar AA (2005) Monkeys
match the number of voices they hear to the number of faces they see. Curr Biol
15: 1034–1038.
47. Parr L (2009 In press) Facial expression in primate communication. In: The New
Encyclopedia of Neuroscience, Oxford.
48. Adachi I, Chou D, RR H (2009) Thatcher effect in monkeys demonstrates
conservation of face perception across primates. Curr Biol 19: 1270–1273.
49. Flack JC, Krakauer DC (2006) Encoding power in communication networks.
Am Nat 168: 97–102.
50. Bowles S (2008) Being human: Conflict: Altruism’s midwife. Nature 456:
326–327.
51. Frank S (2009 In press) Evolutionary foundations of cooperation and group
cohesion. In: Games, Groups and the Global Good, Springer Verlag.
52. Sherrington D (2009, In Press) Physics and complexity. Philos T Roy Soc A.
53. von Neumann J, Morgenstern O (1944) Theory of Games and Economic
Behavior. Princeton, NJ: Princeton University Press.
54. Bilbao JM (2000) Cooperative Games on Combinatorial Structures Kluwer
Academic Publishers.
55. de Waal F, Johanowicz D (1993) Modification of reconciliation through social
experience: An experiment with two macaque species. Child Dev 64: 897–908.
56. Caldecott J (1986) An Ecological and Behavioral Study of the Pigtailed
Macaque, volume 21 of Contributions to Primatology . Basel: S. Karger.
57. Altmann S (1974) Observational study of behavior: Sampling methods.
Behaviour 49: 227–267.
58. Flack JC, de Waal F (2007) Context modulates signal meaning in primate
communication. P Natl Acad Sci USA 104: 1581–1586.
Inductive Game Theory
PLoS Computational Biology | www.ploscompbiol.org 16 May 2010 | Volume 6 | Issue 5 | e1000782
