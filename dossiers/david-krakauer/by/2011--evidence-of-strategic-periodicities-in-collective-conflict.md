---
title: "Evidence of strategic periodicities in collective conflict dynamics"
person: david-krakauer
section: by
type: journal-article
year: 2011
date: 2011-02-16
venue: "Journal of The Royal Society Interface"
authors: "David C. Krakauer et al."
source_url: https://doi.org/10.1098/rsif.2010.0687
retrieved: 2026-08-13
content: full-text
notes: "OA status: green; OpenAlex W2098169005; cited_by 22. Abstract reconstructed from OpenAlex abstract_inverted_index. Full text recovered 2026-08-14 by the upgrade pass from best_oa_location.pdf_url (59,276 chars); OpenAlex has no stored content for this work."
---

# Evidence of strategic periodicities in collective conflict dynamics

## Full text

Evidence of strategic periodicities in collective conflict dynamics

arXiv:1101.1556v1 [q-bio.PE] 7 Jan 2011

Simon DeDeo1,∗ , David Krakauer1, Jessica Flack1,2
1 Santa Fe Institute, 1399 Hyde Park Road, Santa Fe, NM 87501
2 Yerkes National Primate Research Center, Emory University, Atlanta, GA 30322
∗ E-mail: simon@santafe.edu

1

Abstract

We analyze the timescales of conflict decision-making in a primate society. We present evidence for multiple, periodic timescales associated with social decision-making and behavioral patterns. We demonstrate
the existence of periodicities that are not directly coupled to environmental cycles or known ultraridian mechanisms. Among specific biological and socially-defined demographic classes, periodicities span
timescales between hours and days, and many are not driven by exogenous or internal regularities. Our
results indicate that they are instead driven by strategic responses to social interaction patterns. Analyses also reveal that a class of individuals, playing a critical functional role, policing, have a signature
timescale on the order of one hour. We propose a classification of behavioral timescales analogous to those
of the nervous system, with high-frequency, or α-scale, behavior occurring on hour-long scales, through
to multi-hour, or β-scale, behavior, and, finally γ periodicities observed on a timescale of days.

2

Introduction

Variability on multiple timescales is a fundamental feature of complex systems [4, 33]. Minimally, multiple timescales are critical for feedback, and without them there would be no memory, regulation, or
adaptation. Adaptation, for example, requires timescales fast relative to the environment. Memory,
on the other hand, arises from slow variables that average over the underlying fast dynamics. These
slow variables can serve as a reference for decision-making when the lower-level dynamics are rapidly
fluctuating [1, 10, 14, 19].
In the brain, multiple timescales, or characteristic frequencies of oscillation [2], enable populations of
neurons to efficiently represent different kinds of statistical information about the environment. Timescales
have been hypothesized to play a role in the emergence of a unitary consciousness by binding the activity
of large populations of cells [29] and to provide, by increasing the combinatorial space, new means of
storing complex temporal patterns [19] and optimizing synaptic weights.
Timescale variability has also been observed in behavioral dynamics and social systems. The dynamics
of learning (e.g., [27]) and decision-making (e.g., [31]) occur at timescales from seconds through to months
and years. Social systems are comprised of emergent, hierarchically organized social networks that change
over a broad range different timescales from hours to years [1, 14]. These observations raise interesting
questions including, how new timescales emerge, and what the optimal coupling is between time constants
given functional requirements at the individual and collective levels. To answer these questions we must
first quantitatively characterize the range of time constants in our study systems. Whereas much is known
about the range of time constants in neural systems, there is has been less quantitative characterization
of time constants and their implications in social phenomena.
Here we show that conflict decision-making behavior – specifically, the decision to join fights – in
a primate society is characterized by multiple, periodic timescales. We report the range of timescales
detected, and propose a broad classification of behavioral time scales into α waves on hour scales, β waves
on multi-hour scales, and γ waves from six hours up to days. We find that the timescales we detect are
properties of demographic classes defined by biological properties, like age and sex, or social properties,
like power and social roles.
Our analyses take as input a well-studied conflict timeseries [8] collected from a large, socially-housed,

1

primate group (pigtailed macaques, Macaca nemestrina) at the Yerkes National Primate Center in
Lawrenceville, Georgia (see Sec. 4). To characterize the range of timescales in our study system, we
adapt a technique developed to study irregularly-sampled astronomical phenomena, the Lomb-Scargle
periodogram. As described in Sec. 3, the Lomb-Scargle periodogram can be used to detect a very important class of timescales generated by regular periodicities in the dynamics. Examples of phenomena
with these kinds of periodicities include the ultraridian waves of physiology, circadian rhythms correlated
with the photoperiod, and seasonal and reproductive infraridian periodicities [15].
Using the Lomb-Scargle periodogram, we extract signatures of broad-band variation from the conflict
time-series. We consider three alternative hypotheses to account for the time constants we observe. These
include two null models intended to determine whether the timescales are the consequence of exogenous
or endogenous drivers of behavior, and a third hypothesis: the timescales are generated by strategically
timed decisions to join or avoid fights. By “strategic” we mean the decision to join or avoid fights is
timed in response to the pattern of social interactions rather to external cues or physiological clocks (see
Sec. 5.2 for an operational definition on what is meant by “strategy”).

3

Description of Lomb-Scargle Method

The quantitative study of timescale variation falls under the heading of spectral analysis. A tool ideally
suited to the spectral analysis of sparsely and irregularly sampled data is the Lomb-Scargle periodogram
[23, 28, 30]. One of the advantages of irregularly sampled data is the great reduction in windowing and
aliasing effects [28].
The Lomb Periodogram for a time-series, {hj }, j = 1 . . . N , sampled at times {tj }, is defined by
h
hP
i2 
i2
P
j (hj − h̄) sin ω(tj − τ ) 
j (hj − h̄) cos ω(tj − τ )
1 
P
+
(1)
P (ω) ≡
P
,

2
2
2Z
j cos ω(tj − τ )
j sin ω(tj − τ )
where Z is a normalization and τ is defined by
P

j sin 2ωtj

.

(2)

h(t) = A sin ωt + B cos ωt,

(3)

tan 2ωτ = P

j cos 2ωtj

As discussed in Ref. [28], if we write

the definition of τ amounts to setting P (ω) proportional to A2 + B 2 , where the coefficients are set by a
linear least-squares fit. Choosing the normalization, Z, to be the variance of {hj } makes the estimator the
Lomb-Scargle normalized periodogram. A nice feature of the periodogram is that, under a null hypothesis
of i.i.d. Gaussian variables, the distribution of P (ω) is an exponential distribution with mean unity [30].
The output of the Lomb-Scargle is a (normalized) strength-of-signal as a function of frequency, P (ω).
The frequency, ω, measured in Hz, is simply the inverse period (times 2π). In our case, the different {hj }
for which we measure P (ω) are associated with conflicts involving different individuals and demographic
classes, as described in the following section.

4

Structure of the Data

Our study group contained 48 socially-mature individuals and 84 individuals in total. Conflicts, or ‘fights,’
in this system involve two or more individuals and are separated by peaceful periods – defined as the
2

absence of fights among any of the group members. Operational definitions, and additional details on
the data set and data collection protocol appear in the Materials and Methods.
Briefly, a “fight” was operationally defined to include any interaction in which one individual threatens
or aggresses a second individual. A conflict was considered terminated if no aggression or withdrawal
responses (fleeing, crouching, screaming, running away, submission signals) was exhibited by any of
the conflict participants for two minutes from the last such event. Fights involve multiple individuals,
ranging in size from two to twenty-eight individuals. Fights can be conceived of as small networks that
grow and shrink as pair-wise and triadic interactions become active or terminate, until there are no more
individuals fighting under the above-described two minute criterion. As described in the Methods (Sec.
7.1.1, only data on time of fight onset and the individuals involved in the fight are used in these analyses.
No time data are available within fights; although the order of an individuals entry was noted during
data collection, this information was not used in our analyses. Fight onset and termination time (using
above-described criterion) were noted in hours, minutes, and seconds (see Sec. 7.1.1 for further detail).
Our interest is in whether timing influences the decision of an individual to join fights. However,
because the average number of fights per individual is low, it is hard to detect a signal using the LombScargle periodogram at the individual level. Hence for most of our analyses, we aggregate individuals into
demographic classes, according to biological and social characteristics, and ask whether, taken collectively,
individuals of a given class exhibit a timescale on which they join fights.
The biological classes we consider include age-class (socially-mature individuals, and two subclasses
of the socially-mature set: subadults and adults), sex, and matriline (female and all daughters one year of
age or older). The criteria we use to define social classes – social power [12] and performance of policing
role – have been shown in previous work to be important factors in structuring social interactions in the
study group [9, 11]). Demographic class sample sizes are provided with each analysis. For further details
on these demographic classes and for definitions of power and policing, see Materials and Methods.
We calculate P (ω) for each of the demographic classes described above. For each demographic class,
the Lomb-Scargle Periodogram takes as input a discrete series of measurements from the conflict time
series. The timing of an event, ti , is set to be the onset of a fight in the observations; the hi is a
discrete variable: the presence (1) or absence (0) of an individual, or, in the case of classes, the number
of individuals involved in a fight at ti from that demographic class. In effect, a conflict is considered to
“sample” the dispositions of demographic class in question. Detection of a signal using the Lomb-Scargle
periodogram indicates a timescale on which members of that class join or avoid fights.
Conflicts are short, with a median duration of only 15 seconds. The scales we recover span nearly
six orders of magnitude in timescales – between tens and and tens of millions of seconds. Of that range,
the range of scales between 103 seconds (tens of minutes) and 105 seconds (days) is most accessible. On
much longer scales, measurements of nearby periodicities are strongly correlated, meaning there are few
independent measurements to be made. Meanwhile, on the very shortest scales, the finite duration of
conflicts tends to wash out signals.
In previous work [8], we found evidence that the decision to join fights made by individuals in this
study group depended on the properties of the preceding conflict event. The median time between conflicts
is 255 seconds and so decisions to join conflicts correspond to the shortest timescales accessible to our
analysis. Ref. [8] tested a set of alternative causal strategies, or behavioral production rules – formally
denoted as C(n, m)+AND/OR – that could be giving rise to these time scales, and found C(2, 1)+AND to be
a dominant strategy. This indicates that an individual decides to join the the current conflict because
a specific pair of individuals appeared in the previous conflict. This rule applies to all individuals the
group. As many, though not all, adjacent fights are separated by only a few minutes, this finding suggests
that second-to-minute reasoning scales can be of great importance to conflict dynamics.
Can timescales longer than this be found directly in this ruleset? Because any particular rule is
invoked so infrequently, detecting shifts becomes difficult, if not impossible. The analysis we present in
this paper does not need to measure whether individual decision-making rules change, and so does not

3

suffer from the same signal-to-noise issues.

5

Results

As described in Sec. 3, the output of the Lomb-Scargle method is a plot – a periodogram – of the
fluctuation power as a function of frequency (or inverse period). Power at a particular frequency or range
of frequencies indicates the presence of fluctuations with those characteristic timescales. For example, if
an individual or demographic class is characterized by a tendency to shift behaviors (from, for example,
less conflict prone to more conflict prone and back) on timescales of roughly one hour, one would see an
above the null model bump in the periodogram in that range (see Fig. 1, for an example of a periodogram
with significant detections in a number of logarithmically-spaced bins.)
As in previous work, the highly correlated nature of the system means the choice of adequate null
models is crucial. In presenting our results, we consider two null models: the mixed-strategy null, and a
stronger, daily-forcing null. The former, discussed in Sec. 5.1, looks for signatures of changing behavioral
dispositions; the latter, discussed in Sec. 5.2, tries to explain these changes by a model of contextinsensitive daily shifts in conflict behavior. Features unexplained by either null – and associated with
decision-making that is sensitive to fluctuations about mean behavior – are of particular interest. We
focus on them in Sec. 5.3.
In analyses such as these, where many bins are searched for signal, a distinction arises between the
statistical significance of a single-bin detection, and the statistical significance of the detection overall. As
an extreme example, if one searches one hundred bins, each considered equally likely to harbor a signal,
a p value of 10−2 in a single bin does not imply an overall significant detection. In some cases, such as
the subadult male demographic class (see Fig. 2) a single bin shows a strong above-null detection, but
combining that p value with many non-detections in other bins reduces the significance.

5.1

The Mixed-Strategy Null

Without strong priors on timescales of variability – or an intuition for the expected signal strength in
the periodogram – we first compare the observed variability against a null model that retains only the
time-independent properties of the data.
We produce a set of null periodograms by shuffling the time series. We keep the timing of fights the
same, but shuffle their internal compositions, so a fight at time t in the data will correspond to a fight
at time t in all null sets, but will have the composition of a different fight, drawn (without replacement)
from a different time t′ . The normalization of the Lomb-Scargle periodogram is such that the mean value
of the null is unity; further statistical issues associated with null model estimation are discussed in the
Materials and Methods.
In a game theoretic context, this null model corresponds to assigning individuals a constant mixed
strategy (in the game-theoretic sense of mixed): time-independent probabilistic play of one of two strategies, “join conflict” or “avoid.” Note that Lomb-Scargle analyses the data in terms of periodic functions;
failure to reject the null suggests that the animals are playing probabilistic strategies without strong
periodicities.
In the case of a demographic class of size n, the equivalent mixed strategy is for the group as a
whole, and amounts to a probabilistic choice of n + 1 options – “none of us join,” “one of us joins,”
and so forth to “all n of us join.” This is a distinct process from averaging, over a demographic class,
the periodograms obtained for individuals. It is sensitive to the timescales for collective behaviors of a
demographic class, which may be different from the timescales of its individuals. For example, in the
case that two individuals in a demographic class alternate their participation – perhaps because either
is sufficient to play a particular functional role – the observed timescale for the group will be faster, and
more coherent, than that of either of the two individuals taken independently.

4

Figure 1. Timescales of the decision to join fights for the socially-mature individuals considered as a
demographic class (n = 47). Top panel: Lomb-Scargle Periodogram for the socially-mature demographic
class. The data are shown as the solid red line. The (darker) blue band shows the p = 0.05 confidence
for the mixed-strategy null of Sec. 5.1; the (lighter) green band shows the p = 0.05 confidence for the
daily forcing null of Sec. 5.2. Bottom panel: one-sided p-value significance levels for the mixed (solid
line) and daily (dashed line) null models, showing evidence for α and γ oscillations, between 103
seconds and 2.5 days. (See Materials and Methods for further details). The overall significance of
deviation from the mixed-strategy null is p ∼ 10−3 ; the fluctuations are consistent with daily forcing.
Evidence for non-null behavior indicates failure of the assumption of stationary and memoryless
play; it is, among other things, prima facie evidence against the convergence to a stationary solution
concept [16] – unless, of course, the “game” is assumed to take place on timescales longer than those
detected in the data.
In behavioral terms, this choice of null allows us assess whether there are non-stationary features of
behavior over and above static properties that tell us about an individual’s or demographic class’ overall
willingness to engage in conflict.
Additionally, as discussed in the Materials and Methods, the null allows us to bound the influence of
systematic effects, due to the sampling strategy or the correlations induced by noise, that might affect
naive estimates of statistical significance.
Of the 47 socially mature adults we consider in these analyses (see Methods), 6 show significant (p <
0.01) deviations from the mixed-strategy null when their individual patterns of behavior are examined. By
analyzing at the demographic class level, we increase our signal-to-noise and are able to detect significant
patterns in the timescale spectra.
Fig. 1 shows the periodogram for the aggregated data of the 47 socially-mature individuals; the top
panel shows the (smoothed) power at each timescale, whereas the bottom panel shows the significance of
any above-null power. The p-values are computed for the two conceptually distinct null models. Strong
signals at two well-separated scales are the first evidence for timescales of behavior. The faster, α, scale,
is at one hour; whereas there are broad γ-scale oscillations between eleven and twenty-four hours.
As an example of the mixed-strategy null, Fig. 2 shows the periodograms for two biologically-defined
demographic classes – the subadult females (36 to less than 48 months old), and the subadult males (48 to
less than 60 months old). The blue bands show the p = 0.05 confidence levels for the mixed-strategy null.
Although these two demographic classes appear in a similar numbers of conflicts, in similar frequencies,
the periodogram uncovers striking differences in their timescales.
Whereas the subadult males show some evidence for an α-scale oscillation (p ∼ 10−3 in a single bin),
5

Figure 2. Demographic classes defined by sex and age show different timescales. Top left pair:
periodogram, and p-values, for the subadult females (n = 11.) Bottom left pair: adult females (n = 22.)
Top right pair: the subadult males (n = 6.) Bottom right pair: the adult males (n = 8.) As before, the
periodogram data are shown in red, and the blue band shows the p = 0.05 confidence for the
mixed-strategy null of Sec. 5.1; the green band shows the p = 0.05 confidence for the daily forcing null
of Sec. 5.2. The p-values are one-sided, and for the mixed (solid line) and daily forcing (dashed line)
nulls discussed in the text.

6

their overall behavior is consistent with the mixed-strategy null. The subadult females show strong γ
oscillations on scales between eight and twenty-four hours, with a number of bins with p ≪ 10−3 . The
subadult females, in particular, have an overall p-value, against the mixed-strategy null, of p . 10−3 .
The adult females (48 months and older) and adult males (60 months and older) show similarly distinct
timescales. The adult females show a strong α-scale oscillation that overlaps with the subadult males;
they also show evidence for γ oscillations. The adult males show γ oscillations, as well as (p ∼ 0.01)
evidence for the faster timescales seen in the subadult males and adult females. The adult females show
α and γ oscillations; their α waves are similar to the subadult males; their γ waves are slightly weaker
than the subadult females (but still detectable.)
In addition to the sex/age-defined demographic classes, the demographic classes defined in terms of
social power show important differences. Grouping individuals by power [11] reveals additional complexities in the timescale structure of conflict decision-making. We also find important structure in the
functionally-defined policing class (four high power individuals that perform the majority of effective
policing interventions [9].
In particular, whereas the policing class shows similar α and γ oscillations to all 47 socially-mature
individuals considered collectively, the α band signal is absent in the remaining eight individuals that
make up the top power quartile. The second quartile in power shows no evidence for either of these scales.
Instead, this second tier shows evidence for an intermediate β-scale oscillation around three hours.
Interestingly, there is far less evidence for timescales inherent to particular matrilines. Of the eleven
matrilines present in the study group, only two show evidence for strong intrinsic timescales; these are
shown in the Materials and Methods, Figs. 5 through 7. Since members of these matrilines are naturally
included in other demographic classes that do have strong timescales, lack of evidence for matriline-level
timescales suggests that the timescales on which individuals within any particular matriline decide to
join or avoid conflicts differ enough that, when taken collectively, the signals are washed out. We present
the full results in the Materials and Methods.

5.2

Daily Forcing

In the previous section, we found evidence for multiple behavioral timescales in our data. These timescales
show evidence for systematic modulation of the behavior of different individuals and demographic classes.
What is the nature of such modulation?
As the name suggests, the daily-forcing null is intended to capture shifts in behavior due to external
or systematic internal cues that act, over the course of the day, identically from day to day. Such forcing
might be generated by daily shifts in ambient temperature, by a regular feeding time, or by internal
processes such as fatigue that naturally accrue over the course of a day. Hence, the daily-forcing null is
much more demanding – i.e., conservative – on the time series than the mixed-strategy null, as it allows
for temporal inhomogeneity.
Observationally, the daily-forcing null is equivalent to a time-varying mixed strategy in which the
variation is constrained to be the same from day to day. The variation of the mixed-strategy is measured,
for the demographic class in question, from the data itself (see Materials and Methods). In our analysis,
we allow the shifts to occur on timescales as fast as (but no faster than) 15 minutes – sufficient to model,
if possible, even the fastest, α scales. The null does not, of course, specify what particular processes leads
to these daily shifts. It can be a combination of external, internal, and social factors (the behaviors of
others that shift due to their own external and internal factors).
Deviations from the daily forcing null can be accounted for in two ways. On the one hand, since
the null has no day-to-day variations, deviations might indicate forcing on longer timescales such as
œstrus, or that learning is causing accumulated shifts in behavior. These effects would be visible, in the
periodograms themselves, as strong signals beyond 105 seconds. There is some evidence, in the subadult
female demographic class (Fig. 2), for these longer scales; there, fluctuations at and above 24 hours reject
the daily forcing null at p . 10−3 , and the overall significance has p ∼ 0.01.
7

The other explanation for deviations from daily forcing is a breakdown in the assumption of independentlydistributed behavior. In this case, signatures of variability, over and above the daily forcing null, are associated with context-sensitive, or strategic, decision-making. Mathematically, rejection of this null would
mean that shifts in the average behavior are not driving the system on these scales. Instead it is the
system’s correlated responses to fluctuations about that average. Purely random fluctuations about the
average will generate spurious timescales, but these are accounted for by the sampling-with-replacement,
and so violations the daily-forcing null indicate correlations in those responses.
To demonstrate the importance of the daily forcing null, consider the top panel of Fig. 1, which shows
the periodogram of the 47 socially-mature individuals considered collectively. There are strong signals of
timescales in the α band (around 1 hour) and in the γ bands (at 11 hours and 24 hours) – sufficiently
< 0.001). However, the data for
strong that the mixed-strategy null is ruled out at high confidence (p ∼
these 47 animals are fully consistent with the daily forcing null, which allows for a changing “mood” that
systematically shifts the probabilities of becoming involved in fights over the course of the day. Only
one individual from the 47 socially mature adults shows significant (p < 0.01) deviations from the daily
forcing null when patterns of behavior are independently examined.
The strongest deviations from daily forcing are found in some of the most important demographic
classes in the study group. The top left pair of panels in Fig. 3 show the timescales associated with the
policing class. In addition to the longer γ scales, there is strong evidence for timescales, over and above
that of daily forcing, that between 1 hour and 2 hours. We return to these strategic time signatures in
Sec. 5.3.
These results suggest that context-free models are adequate explanations for the collective decisionmaking pattern exhibited by the 47 socially-mature individuals, but fail as descriptions for the more
specific decision-making patterns exhibited by other demographic classes.
Whereas violations of the daily-forcing null indicate strategic timing, it is also worth noting that
failure to reject the daily forcing null does not necessarily mean the absence of strategy. Individuals and
demographic classes structuring their conflict behavior in response to others whose behavior is driven
by daily forcing would show patterns consistent with this rather stringent null and would result in a
false negative (Type II error.) Even behavior consistent with the mixed null may have strategic aspects
invisible to this analysis, if the relevant contexts are uncorrelated with the size of involved demographic
class. Hence, whereas rejection of the daily forcing null indicates a strategic timescale, failure to reject
the daily-forcing null does not necessarily mean the absence of a strategic timescale.

5.3

Timescales for Strategic Behavior

The possibility of strategic decision-making over and above daily forcing is implied in the short timescales
of the policing class, which is shown in the top left panels of Fig. 3. These scales are much shorter than
can be accounted for by multi-day shifts in behavior. This policing timescale appears in the fastest, α
band. As shown in Table 1 and Fig. 2, the adult female demographic class also shows strong evidence
for violations of the daily-forcing null in the α band.
The timescales of conflict-related activity can thus be mapped onto demographic classes playing
functional – in our case, conflict management – roles as well as biological and other socially defined
demographic classes. The rest of Fig. 3 shows schematically how individuals with differing social power
(in a system in which the power distribution is heavy-tailed [12]) show context-sensitive timescales of
variation. Lower-power classes show both long and short timescales; the second power quartile shows a
β-scale oscillation at ∼ 3 hours, consistent with daily forcing. In the Materials and Methods, Fig. 4 we
show as well the timescales for the fourth and lowest power quartile, which shows marginal evidence for
fluctuations at the slower β-scales.

8

Figure 3. Uncovering strategic timescales for power and policers. Top left pair: periodogram, and
p-values, for the policing class – four top-quartile power individuals who effectively intervene
impartially, and break up, conflicts. Top right pair: similarly, for the top quartile in power minus
policers (n = 8.) Bottom left pair, similarly for the second power quartile (n = 12). Bottom right pair:
for the third power quartile (n = 12). In all cases, the demographic classes show significant deviations
from the mixed-strategy null. In the policing class, and in the top power quartile, there is also
significant deviation from daily forcing, suggesting that the timing of the decision to join or avoid a
fight is strategic. There is also evidence of strategic timing, in particular, at the α-scale oscillations seen
for the 47 socially-mature individuals, when treated collectively (Fig. 1).

9

Demographic Class

All Socially-mature Individuals
Age & Sex
Subadult Females
Subadult Males
Adult Females
Adult Males
Social Power & Role
Policers
Top Quartile (minus Police)
Second Quartile
Third Quartile
Bottom Quartile
Matrilines

Timescales
Mixed-Strategy
(p < 0.01)
α, γ

Timescales
Daily Forcing
(p < 0.01)
–

Overall Significance
(103 sec to 2.5 days)
pmix = 0.002; pforce > 0.01

γ
α
α, γ
α, γ

γ
α
γ

pmix = 0.001; pforce > 0.01
pmix > 0.01; pforce > 0.01
pmix = 0.01; pforce > 0.01
pmix = 0.001; pforce = 0.01

α, γ
γ
β
α, γ
–
α, β

α, γ
–
α
–
–

pmix = 0.001; pforce = 0.005
pmix = 0.008; pforce > 0.01
pmix = 0.01; pforce > 0.01
pmix = 0.004; pforce > 0.01
pmix > 0.01; pforce > 0.01
pmix (min) = 0.003; pforce > 0.01

Table 1. Summary of conflict decision-making timescales detected in the study group. Detections in
the various bands (α, β, and γ) are shown for the two null models. In addition, we show the overall
significance of the detections. The primary timescales found are α (between 30 minutes and 2 hours)
and γ (above 6 hours). One demographic class the second power quartile, shows a significant
intermediate, β, scale between 2 hours and 6 hours. Taken collectively, the 47 socially-mature
individuals, as well as a number of smaller demographic classes, show significant evidence overall for
non-stationary behavior (above the mixed-strategy null); overall violations of the daily-forcing null,
indicating fluctuation-sensitive behavior, are rarer and found in only in the adult males and in the
policing class. In the eleven matrilines, there are two detections of α and β scales; only one matriline
has an overall significance against the mixed-strategy null (p = 0.003.)

10

5.4

Summary Table

Table 1 summarizes our results for the different demographic classes.

6

Discussion

6.1

Evidence for Multiple Timescales

Periodic behavior at multiple time scales [15] is a fundamental feature of biological systems. Biological
periodicities range from cellular activity measured at the scale to milliseconds, through ultraridian cycles
measured at time scales of months or years. Many of these cycles derive from fundamental physiological
and biochemical processes, and are observed across distantly related taxa [3]. This study presents, to the
best of our knowledge, the first evidence for multiple, periodic timescales associated with social decisionmaking and behavioral patterns in an animal society, and the first empirical study of social systems to
demonstrate the existence of periodicities that are not directly coupled to environmental cycles or known
ultraridian mechanisms. Rather we find that for particular sets of individuals playing important conflict
management roles, the timescale on which they decide to join or avoid fights is strategic. By “strategic”
we mean that, collectively, these individuals time their decision to join fights in response to correlated
fluctuations around the mean pattern of conflict decision-making shown by the rest of the group.
We find three main results. First, whereas some demographic classes have no timescale structure
at all, a number of classes show well-separated fluctuations at either short, α, or long, γ, timescales;
intermediate β scales are seen only rarely in the demographic classes we consider. Secondly, different
demographic classes have different timescale signatures, with, for example, subadult females showing
strong γ-band fluctuations whereas the subadult males show fluctuations on in the α band. Finally, and
most strikingly, we find a strategic timescale associated with a functional role: a subset of individuals who
perform effective policing show a conflict decision-making timescale that is tuned to the mean pattern of
conflict in the group and is on the order of one to two hours.
The longest time scales, the γ band, are largely but not completely driven by external or internal
systematic periodicities, like day-night cycles, feeding cycles, œstrus, and context-independent fatigue
that accrues over the course of a day. These scales are not observed for all group members. The adult
females show the clearest day-scale, or γ, periods in their behavior.
The γ activity in the subadult females that is absent in the subadult males suggests some intriguing
sex-related differences in conflict decision-making. The males appear to behave more randomly (in so
far as they, as a group, are indistinguishable from the homogeneous mixed-strategy) than the females.
Females manifest systematic variation in their willingness to join fights over the course of days. Males
on average appear to be more opportunistic in their decisions to joint conflicts in that their decisions are
time invariant. These results are consistent with the data on opportunistic coalition formation in males
in several primate species [7, 32].
The β activity on multi-hour scales seen in some of the intermediate- and low-social power groups could
relate to simple daily variation in mood, variable sensitivity to hidden triggers in the environment, or
group-level variability in temperament that manifests in a variety of behaviors, including conflict-related
behavior.
Of particular interest are the α-scale behaviors that can not be explained by daily forcing. On these
shorter timescales, we find demographic class periodicities associated with the management of conflict by
powerful individuals. These policers appear regularly in the time series at timescale of an hour to two
hours.
This result is consistent with previous results showing policers preemptively forestall the escalation
of aggression by checking conflicts through impartial interventions [13, 22]. It appears that the policers
dampen conflict not only by intervening in the regular cycles of fighting, but also by dampening fluctuations about these cycles by making regular appearances in fights. That policing has a signature timescale
11

raises the interesting question of whether policing is predictable by individuals in the society. If so, individuals might be able to tune their conflict decision-making strategies to avoid or facilitate intervention
by policers.

6.2

Implications and Significance

A body of work in neuroscience [2,20], and preliminary results from the study of social niche construction
in animal societies [1, 14], suggest that multiple timescales within what is typically considered a “level”
(e.g. the “neural level” or the “behavioral level”) play an important role in the collective construction of
aggregate patterns as well as in inter-individual coordination during communication [17]. However, beyond the neural level and the study of biological rhythms, where multiple timescales are well documented,
little is quantitatively known about the number, distribution, or significance of timescales.
This is particularly true at the behavioral level, where there has been little explicit consideration
of the role of time in structuring social interactions or in constraining or facilitating the emergence of
coordinated aggregates. An important exception is the study of spatial patterning in groups, such as
schooling in fish or flocking in birds [5]. Our analysis differs from these studies in that it stresses periodic
variability in a strategic state space rather than non-periodic variability in an explicitly spatial domain.
There are many important timescale-related questions in the study of social evolution, and many
of these concern whether such scales are non-functional emergent properties of collective dynamics, or
functional features that serve to better coordinate complex societies. If timescales are functional, how
do individuals influence the timescales of behavior of a large group? This study provides provisional
evidence that policers, for example, function to modify aggression in the group by performing policing
interventions and appearing in fights at regular, predictable intervals. This explanation is consistent
with the results of an experiment showing that even though the proportion of fights that receive policing
interventions is relatively small, aggression increases when the policing function is disabled by “knockout”
of the policers [9].
The question of why social and other systems display a range of timescales, as opposed to simpler
cases where a single strongly coherent oscillation – such as the circadian rhythm – dominates a system,
is also of a great interest. It can indicate, among other things, the presence of spin-glass behavior [4].
Near-critical spin-glass properties have been found in the dynamics of neural networks [34], and behaviors
guided by social interactions may have similar properties. Given the hypothesized role of fluctuationcorrelated behavior that violates the daily forcing null, it is also of interest that such glassy systems show
non-trivial responses to their own internal fluctuations [6].
Timescale separations due to the emergence of slow variables at the aggregate level – e.g, the emergence
of a slowly changing power structure from a network of status signaling interactions – are thought to be a
means for reducing social uncertainty generated by fluctuations at a lower-level in fight outcomes [1,10,14].
In many cases, timescale variability appears to emerge from combinations of connectivity and constraints
among populations of components – in the case of power, for example, this corresponds to a network of
individuals signaling about their dominance status. We remain ignorant, however, of mechanisms that
might channel variation in timescales at the aggregate level back to influence the timescales on which
individuals make decisions. To answer these kinds of questions, we need a means of combining inductive,
game-theoretic models of the kind presented in Ref. [8] with the spectral properties of the highly-resolved
behavioral time series as we have presented them here.

7

Materials and Methods

Here we cover the methods of data collection protocol, as well as details on the statistical analysis
associated with the Lomb-Scargle periodogram and the two null models.

12

7.1

Data Collection

The data collection protocol was approved by the Emory University Institutional Animal Care and Use
Committee and all data were collected in accordance with its guidelines for the ethical treatment of
nonhuman study subjects.
7.1.1

Operational Definitions

Fight: includes any interaction in which one individual threatens or aggresses a second individual. A
conflict was considered terminated if no aggression or withdrawal responses (fleeing, crouching, screaming,
running away, submission signals) was exhibited by any of the conflict participants for two minutes from
the last such event. A fight can involve multiple individuals. Third parties can become involved in
pair-wise conflict through intervention or redirection, or when a family member of a conflict participant
attacks a fourth-party (See Methods). Fights in this data set ranged in size from two to 28 individuals
and can be represented as small networks that grow and shrink as pair-wise and triadic interactions
become active or terminate, until there are no more individuals fighting under the above described two
minute criterion. In addition to aggressors, a conflict can include individuals who show no aggression (e.g.
recipients or third-parties who either only approach the conflict or show affiliative / submissive behavior
upon approaching). Because conflicts involve multiple actors, two or more individuals can participate in
the same conflict but not interact directly.
In this study only information about fight composition (which individuals were involved) and time of
fight onset are used. Our analyses focus only on the decision to fight. We do not in this paper consider
whether this decision is made with respect to starting a fight or to joining an ongoing fight. We also do
not consider any internal aspects of the fight, such as who does what to whom. No time data are available
within fights; although the order of an individual’s entry was noted, the information was not used in this
analysis. The median duration of fights is 15 seconds. The minimum timescale we consider is on the
order of 1000 seconds. Given the median duration and this minimum time criterion, deviations between
the fight start time and the time of entry of any individual into the fight should not be problematic.
Fight onset and termination time were noted in hours, minutes, and seconds. Timing accuracy – is
at worst, on the order of seconds for fight onset time, and so accuracy to this level is more than sufficient
for the range of timescales we investigate here.
Demographic Classes: The demographic classes we consider include age-sex classes (see below), matrilines (see below), power quartiles (see below) and policers (see below).
Age-sex Classes: With the exception of the matriline analyses, all animals in our analyses are “sociallymature”. Socially-mature males were at least 48 months and socially-mature females were at least 36
months by study start. Subadult males were males between 48 and 60 months; adult males were at
least greater than or equal to 60 months. Subadult females were at least 36 months but less than 48
months; adult females were at least greater than or equal to 48 months. These thresholds correspond to
approximate onset of social maturity in pigtailed macaques.
Matriline: an adult female and her daughters. In the study group, all females in a matriline were
related through the maternal line. Only females one year or older were included in the matriline analyses.
Power: the degree of consensus among individuals in the group about whether an individual is capable
of using force successfully. Consensus is quantified by taking into account the total number of subordination signals an individual receives and multiplying this quantity by a measure of the diversity of
signals received from its population of signalers (quantified using Shannon Information) [12]. In the pigtailed macaque, the subordination signal is the silent bared teeth display [10]. The distribution of power

13

in our study group is heavy tailed. The first power quartile corresponds to the top 12 individuals of the 48.
Policers: four individuals (one female, three males) who preform the majority of effective policing interventions (sit towards the tail in a log normal distribution of the frequency of effective policing interventions). A policing intervention is an impartial intervention performed by a third party into an ongoing
conflict. [9]. These individuals occupy the top four spots in the power structure and sit toward the tail
of the distribution.
General note about demographic classes: Our results showing that demographic classes that have signature timescales suggests that there are empirical grounds for treating them as coherent units with sets
of actions. This is similar to the concept of coalitions in cooperative form games [26], and the finding is
consistent with results of a previous study in which we showed that the triad, not the individual or the
dyad, is a the fundamental unit of conflict dynamics in this group [8].
7.1.2

Data Collection Protocol

During observations all individuals were confined to the outdoor portion of the compound and were visible
to the observer, JF. The ≈ 150 hours of observations occurred for up to eight hours daily between 1,100
and 2,000 hours over a twenty-week period, comprising roughly 122 days, from June through October
1998 and were evenly distributed over the day. This span allows us to study a wide range of scales on
which behavior can change. The sampling is sparse relative to the total number of hours (150 of 2928)
in the data collection period; it is also irregular, in that observational periods are not separated by the
same number of days and have different lengths and gaps. Fight and status signaling data were collected
using all-occurrence sampling.
Provisioning occurred before observations, and once during observations at the same time each day.
The group was stable during the data collection period (defined as no reversals in status signaling interactions resulting in a change to an individual’s power score, see [12]). One animal, Ud, was removed from
the group for health reasons towards the end of the study; as this sudden removal (and thus zeroing out
of all behavior data) is likely to produce strong, but spurious signals of behavioral variation, we excluded
her from the analysis.

7.2

Q Values and Timescale Coherence

In common with many spectral analysis methods, Lomb-Scargle takes as basis functions the sine and
cosine, phase shifting them to find the optimal fit. A pure sine-wave signal, for example, would amount
to an extremely sharp spike at the relevant frequency in the periodogram.
Although precise oscillations are unlikely to be found in the noisy and non-ergodic environments
we consider here, more realistic behaviors are also mapped to the relevant portions of the plot; for
example, repetitive excitation and subsequent exponential decay would map to a peak centered around
the excitation period. If one also allowed there to be jitter in the exponential decay – random variation
both in the time-constant and in the precise timing of the excitations following decay – the peak would
broaden further.
One sometimes defines a Q-factor, a measure of the width of a peak in a periodogram, as f0 /∆f ;
here f0 is the peak center and ∆f the width of the peak at half-maximum. Very “pure” oscillations –
close to a sinusoidal variation – have high Q-factors; conversely, purely damped systems that dissipate
oscillations – such as a suspension system in a car or building – have Q less than unity.
Man-made systems such as optical cavities for lasers can have Q factors in the millions and billions;
mechanical vibrating systems such as a tuning fork have Q of of order 103 . Meanwhile, natural phenomena
tend to have much lower Q-factors, indicating the presence of noise and blended signals at different scales.
For example the Q-factors of brain oscillations measured from an EEG of a sleeping human of can be of
14

order 10 or 100; the quasi-periodic phenomena found in neutron star systems can have Q of order 10 or
lower [25, 35].
In the system we study here, we find Q factors of larger than, but of order, unity – i.e., slightly less
coherent than the quasi-periodic oscillations of the human brain. These are similar to the Q-factors one
can estimate for the bacterial motors of E. coli measured in Ref. [21], and higher than the Q-factors seen
for the signaling networks that control them.

7.3

Statistical Features of Broadband Lomb-Scargle

The Lomb-Scargle periodogram, introduced in Sec. 2, forms the center of the data analysis in this paper.
Traditionally it has been applied to the detection of high-Q signals such as the detection of orbital periods
of stellar systems. We discuss here some of the statistical tools employed to uncover much the broader
features of the spectrum observed in our study system.
It turns out that despite the discreteness of the measurement values – and the correlations between
conflict behaviors of different individuals at the same time – the distribution of P (ω) under the mixedstrategy null of Sec. 5.1 is also approximately both exponential and of mean unity. The daily forcing
null is far more structured, and induces strong correlations between bins that can be seen visually in the
plots.
If one is then seeking a signal at a precise frequency – i.e., a sinusoidal oscillation with an extremely
high Q-value – then it becomes simple to determine a threshold power above which a detection is considered significant with a certain p-value. The approximate value is
P (ω) ≈ − ln p/M ,

(4)

where M is the number of independent frequencies. The dependence on M comes from the fact that
rare events become more likely the more one samples – in the words of Ref. [28], “look long enough, find
anything!”
However, for signatures that are more broad-band – that are expected to cover a range of frequencies
– this simple method is too conservative. The presence of correlated noise makes the analytic estimation
even harder, since, in contrast to the Gaussian, there is no simple version of the multivariate exponential
distribution that allows for correlations between arbitrary numbers of different frequencies. Instead
of analytic approximations, then, a Monte Carlo estimate of bin-by-bin significance is made: many
instantiations of the null model are produced, and their distribution compared to measured value, binby-bin, to produce an estimate of the p-value.
Given a set of such p-values for all bins, we then wish to estimate, in Sec. 5.1, the overall p-value for a
detection of non-null timescales. The Bonferroni correction for combining p-values is generally considered
to be too conservative. In a search for periodicity in gene expression data, Ref. [18] used an order statistic
on p-values. Here, following Ref. [24], we use the χ2 (2) test of Fisher, which works well where one is
seeking evidence for strong signals in one or two bins. All these methods require that the p-values be
independent (in the null).
Failures of null independence – and, in general, failures of null p-values to fall in a U (0, 1) distribution
– can lead to both Type I and Type II errors for any method of combination. We check the validity
of the χ2 (2) test by running our same analyses on null data alone. We find that the Fisher method
works reasonably well, though not perfectly, and can underestimate p-values when p ≤ 10−3 . We silently
insert these corrections to reported p-values in the main paper, so that our stated p-values for overall
significance are our best estimates, and do not rely on the strong assumptions of combination methods
such as the χ2 (2) test.
Our bins are logarithmically spaced; we search the range between 103 seconds and 2.5 days, and, once
we correct for correlations, our results are, as they should be, insensitive to the number of bins. The
periodograms themselves are very noisy, with fluctuations from point to point; when we show them, we

15

smooth with a small window; the width of this window is shown visually as the short black line in the
top left corner of each plot. The smoothing is done by a Savitzky-Golay filter, which helps preserve the
sharpness (or lack thereof) of the spectral features and is less likely to bias the amplitude [28]. All of our
significance estimates are made, naturally, on the unsmoothed data.
In the case of the mixed-strategy null, we found our results insensitive to whether we sampled with
replacement or simply shuffled the timeseries (sampling without replacement.) This is a consequence
both of how much data we have, and that the Lomb-Scargle technique is not strongly sensitive to very
rare events.
In the case of the daily-forcing null, we bin fight sizes for each demographic class in 15 minute
increments over the day to produce a distribution that we then draw from to simulate a new series of
conflicts. (Results are largely insensitive to bin size; in many cases, the daily-forcing null can be replaced
with a parametrized fit – for example, the overall conflict behavior of the study group can be modeled as
a Poisson process with a mean that slowly increases over the course of the day.)

7.4

Periodograms

In Figs. 4 through 7, we show the periodograms for all the remaining demographic classes discussed in
the paper. These results are also summarized in Table 1.

16

Figure 4. Top pair: the top quartile in power, including police class (n = 12; in the main text this
quartile is split to show the influence of the policing functional class.) Bottom pair: the lowest quartile
in power (n = 11.)

17

Figure 5. Matrilines 1 through 4. n = {4, 3, 3, 2}

18

Figure 6. Matrilines 5 through 8. n = {3, 2, 3, 3}

19

Figure 7. Matrilines 9 through 11. n = {3, 2, 2}

20

8

Acknowledgements

We thank Frans de Waal for support during data collection, and the staff of the Yerkes National Primate
Research Center, for help with the data collection.

References
1. C. Boehm and J.C. Flack. The emergence of simple and complex power structures through social
niche construction. In A. Guinote, editor, The Social Psychology of Power. Freeman, 2010.
2. György Buzsáki and Andreas Draguhn.
304:1926, 2004.

Neuronal oscillations in cortical networks.

Science,

3. V.M. Cassone. Time and time again: The phylogeny of melatonin as a transduce of biological time.
Journal of Biological Rhythms, 12:489–497, 1997.
4. A. C. C Coolen and D Sherrington. Order-parameter flow in the SK spin glass. I. Replica symmetry.
J. Phys. A, 27:7687, 1994.
5. I. Couzin. Collective cognition in animal groups. Trends in Cognitive Sciences, 13:36–43, 2009.
6. C. De Dominicis and I.. Giardina. Random Fields and Spin Glasses: A Field Theory Approach.
Cambridge University Press, Cambridge, U.K., 2006.
7. F.B.M. de Waal. Sex differences in the formation of coalitions among chimpanzees. Ethology and
Sociobiology, 5:239–255, 1984.
8. Simon DeDeo, David C Krakauer, and Jessica C Flack. Inductive game theory and the dynamics
of animal conflict. PLoS Computational Biology, 6(5):e1000782, 2010.
9. J. C. Flack, F. B. M. de Waal, and D. C. Krakauer. Social structure, robustness, and policing cost
in a cognitively sophisticated species. American Naturalist, 165:E126–E139, 2005.
10. J. C. Flack and F.B.M. de Waal. Context modulates signal meaning in primate communication.
Proc. Natl. Acad. Sci, 104:1581–1586, 2007.
11. J. C. Flack, M. Girvan, F. B. M. de Waal, and D. C. Krakauer. Policing stabilizes construction of
social niches in primates. Nature, 439:426–429, 2006.
12. J. C. Flack and D. C. Krakauer. Encoding power in communication networks. American Naturalist,
168:97–102, 2006.
13. J. C. Flack, D. C. Krakauer, and F. B. M. de Waal. Robustness mechanisms in primate societies:
A perturbation study. Proceedings of the Royal Society of London, Series B, 272:1091–1099, 2005.
14. J.C. Flack, D. Erwin, T. Elliot, and D.C. Krakauer. Construction of slow variables required for
the emergence of aggregates: A new approach to the origins of levels in evolution. In K. Sterelney,
B. Calcott, and R. Joyce, editors, Cooperation and Complexity. MIT Press, Cambridge, MA, 2010.
in press.
15. R. Foster. Rhythms of Life: The Biological Clocks that Control the Daily Lives of Every Living
Thing. Profile Books, London, 2004.
16. Drew Fudenberg and David K. Levine. The Theory of Learning in Games. MIT Press, Cambridge,
MA, 1998.
21

17. A.A. Ghanzanfar, C. Chandrasekaran, and R.J. Morrill. Dynamic, rhythmic facial expressions and
the superior temporal sulcus of macaque monkeys: implications for the evolution of audiovisual
speech. European Journal of Neuroscience, 31:1807–1817, 2010.
18. Earl Glynn, Jie Chen, and Arcady Mushegian. Detecting periodic patterns in unevenly spaced
gene expression time series using lomb-scargle periodograms. Bioinformatics, 22(3):310, 2006.
19. S. J. Kiebel, J. Daunizeau, and K. J. Friston. Perception and hierarchical dynamics. Frontiers in
Neuroinformatics, 3:20, 2009.
20. C. Koch, M. Rapp, and I. Segev. A brief history of time (constants). Cerebral Cortex, 6:93–101,
1996.
21. Ekaterina Korobkova, Thierry Emonet, Jose M. G Vilar, Thomas S Shimizu, and Philippe Cluzel.
From molecular noise to behavioural variability in a single bacterium. Nature, 428:574, 2004.
22. D.C. Krakauer, K. Page, and J.C. Flack. An empirical and theoretical analysis of the immunodynamics of conflict intervention in social systems. PLoS Computational Biology, in review, 2010.
23. N. R Lomb. Least-squares frequency analysis of unequally spaced data. Astr. and Space Sci.,
39:447, 1976.
24. T. M. Loughin. A systematic comparison of methods for combining p-values from independent
tests. Comput. Stat. Data An., 47(3):467–485, 2004.
25. J. Middleditch and W. C. Priedhorsky. Discovery of rapid quasi-periodic oscillations in scorpius
x-1. Astrophys. J, 306:230, Jul 1986.
26. Roger B. Myserson. Game Theory: Analysis of Conflict. Harvard University Press, Cambridge,
MA, 1991.
27. K. M. Newell, Y.T. Liu, and G. Mayer-Kress. Time scales in motor learning and development.
Psychological Review, 108:57–82, 2001.
28. William H. Press, Saul A. Teukolsky, William T. Vetterling, and Brian P. Flannery. Numerical
Recipes in C: The Art of Scientific Computing. Cambridge University Press, Cambridge, U.K.,
1996.
29. M. Roser and M.S. Gazzaniga. Automatic brains –interpretive minds. Current Directions in
Psychological Science, 13:56–59, 2004.
30. J. D Scargle. Studies in astronomical time series analysis. ii - statistical aspects of spectral analysis
of unevenly spaced data. Astrophys. J., 263:835, 1982.
31. E. Selezneva, H. Scheich, and M. Brosch. Dual time scales for categorical decision making in
auditory cortex. Current Biology, 16:242833, 2006.
32. J. Silk. The patterning of interventions among male bonnet macaques: Reciprocity, revenge, and
loyalty. Current Anthropology, 33:318–325, 1992.
33. H Sompolinsky. Time-dependent order parameters in spin-glasses. Phys. Rev. Lett., 47:935, 1981.
34. Gasper Tkacik, Elad Schneidman, Michael J Berry, and William Bialek. Ising models for networks
of real neurons. arXiv, q-bio/0611072v1, 2006.
35. M van der Klis, F Jansen, J van Paradijs, W. H. G Lewin, E. P. J van den Heuvel, J. E Trumper,
and M Szatjno. Intensity-dependent quasi-periodic oscillations in the X-ray flux of GX5-1. Nature,
316:225, Jul 1985.

22
