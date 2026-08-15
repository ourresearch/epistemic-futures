---
title: "Adaptive Sampling for Coarse Ranking"
person: james-evans
section: by
type: journal-article
year: 2018
date: 2018-02-20
venue: "arXiv (Cornell University)"
authors: "Katariya, Sumeet, Jain, Lalit, Sengupta, Nandana, Evans, James, Nowak, Robert"
source_url: https://doi.org/10.48550/arxiv.1802.07176
openalex_id: https://openalex.org/W2788294944
retrieved: 2026-08-13
content: full-text
notes: "preprint version; full text extracted from the arXiv PDF"
---

# Adaptive Sampling for Coarse Ranking

## Full text

Adaptive Sampling for Coarse Ranking

Sumeet Katariya
katariya@wisc.edu

Lalit Jain
lalitj@umich.edu

arXiv:1802.07176v1 [cs.LG] 20 Feb 2018

James Evans
jevans@uchicago.edu

Abstract
We consider the problem of active coarse
ranking, where the goal is to sort items according to their means into clusters of prespecified sizes, by adaptively sampling from
their reward distributions. This setting is
useful in many social science applications involving human raters and the approximate
rank of every item is desired. Approximate
or coarse ranking can significantly reduce the
number of ratings required in comparison to
the number needed to find an exact ranking.
We propose a computationally efficient PAC
algorithm LUCBRank for coarse ranking, and
derive an upper bound on its sample complexity. We also derive a nearly matching
distribution-dependent lower bound. Experiments on synthetic as well as real-world data
show that LUCBRank performs better than
state-of-the-art baseline methods, even when
these methods have the advantage of knowing
the underlying parametric model.

1

Introduction

We consider the problem of efficiently sorting items
according to their means into clusters of pre-specified
sizes, which we refer to as coarse ranking. In many
big-data applications, finding the total ranking can be
infeasible and/or unnecessary, and we may only be
interested in the top items, bottom items, or quantiles. Consider for instance the problem of assessing
the safety of neighborhoods from pairwise comparisons
of Google street view images, as is done in the Place
Pulse project (Naik et al., 2014), which can be applied
to develop social policy (Dubey et al., 2016). Finding a
Proceedings of the 21st International Conference on Artificial Intelligence and Statistics (AISTATS) 2018, Lanzarote, Spain. PMLR: Volume 84. Copyright 2018 by the
author(s).

Nandana Sengupta
nandana@uchicago.edu
Robert Nowak
rdnowak@wisc.edu

complete ordering of the images in this case is impractical because many images are difficult to compare i.e.,
their safety scores are very close (see Section 7.2). Furthermore, a total ordering may be unnecessary from a
public policy point of view, since the approximate rank
of every image on the safe-unsafe spectrum may suffice.
Motivated by these applications, we model the coarse
ranking problem as follows. Given K random variables, c ≥ 2 clusters, and cluster boundaries 1 ≤
κ1 < κ2 < · · · < κc−1 < κc = K, the goal is to reliably identify the κ1 random variables with the highest
means, the κ2 − κ1 random variables with the highest means among the remaining K − κ1 random variables, and so on, by observing samples from their reward distributions (for a precise formulation see Section 4). The focus of this paper is on algorithms that
achieve this clustering by requesting samples adaptively. The coarse ranking setting applies to the scenarios above, and also subsumes many well-studied
problems. The problem of finding the best item corresponds to κ1 = 1, κ2 = K. The problem of finding
the top-m items corresponds to κ1 = m, κ2 = K. The
problem of sorting the items into c equal-sized clusters corresponds to κi = round(iK/c), 1 ≤ i ≤ c. Finally, the complete ranking can be obtained by setting
κi = i, 1 ≤ i ≤ i ≤ K.
The problem of completely sorting items is in general hard in real-world applications, and does not exhibit gains from adaptivity. Maystre and Grossglauser
(2017) who analyze the performance of Quicksort, observe in their real-world experiments:
“The improvement is noticeable but modest.
We notice that item parameters are close to
each other on average; . . . This is because
there is a considerable fraction of items that
(1)
have their parameters (means) very close to
one another . . . Figuring out the exact order of these images is therefore difficult and
probably of marginal value.”
The fact that adaptivity doesn’t help for complete
ranking is true not just for Quicksort, but other adap-

Adaptive Sampling for Coarse Ranking

tive algorithms as well - as we observe in our experiments. Adaptivity does however help for coarse ranking, and this can be explained. Consider the case
when the K items have bounded reward distributions,
and their means are equally separated, with a gap ∆
between consecutive means. Correctly ordering any
two consecutive items requires Ω(1/∆2 ) samples, and
thus any algorithm would require Ω(K/∆2 ) to find
a total ordering. A non-adaptive algorithm sampling
the items uniformly would gather approximately equal
samples from every item, and hence will find the correct ranking after roughly these many samples (up to
perhaps log factors). Thus adaptivity doesn’t help in
this case. However, if the goal is to find only the quartiles say, an adaptive algorithm can quickly stop sampling items that are far from the quartile boundaries
and gain over non-adaptive algorithms.

two items and receives 1-bit feedback about who won
the duel. We next explain how to translate our algorithm to this setting.

In this work, we make six contributions. First, we
motivate the coarse ranking setting. We do this by
arguing that most real-life problems have high noise,
and by explaining why adaptive methods are ineffective in producing a complete ranking in these highnoise regimes (Section 3). Second, we precisely formulate the online probably approximately correct (PAC)coarse ranking problem with error tolerance  and failure probability δ that can model real-valued as well
as pairwise comparison feedback (Section 4). Third,
we propose a nonparametric PAC Upper Confidence
Bound (UCB)-type algorithm LUCBRank to solve this
problem. To the best of our knowledge, this is the first
UCB-type algorithm for ranking (Section 5). Fourth,
we analyze the sample complexity of LUCBRank and
prove an upper bound which is inversely proportional
to the distance of the item to its closest cluster boundary, where the distance is measured in terms of Chernoff information (Section 6). Fifth, we also prove a
nearly matching distribution-dependent lower bound.
The contribution of an item to the lower bound is inversely proportional to the distance of the item to the
closest item in an adjacent cluster, with distance in
this case measured using KL-divergences (Section 6.3).
Finally, we compare the performance of our algorithm
to several baselines on synthetic as well as real-world
data gathered using MTurk, and observe that it performs 2 - 3x better than existing algorithms even when
they have the advantage of knowing the underlying
parametric model (Section 7).

2

1.1

Ranking using Pairwise Comparisons

We use the term direct-feedback or real-rewards to indicate a setting where the learner can sample directly
from the item’s reward distribution. Our algorithm is
stated for this setting. In contrast, in the pairwisecomparison or dueling setting, the learner compares

Any algorithm designed to solve the direct-feedback
coarse ranking problem can also be used with pairwise
comparison feedback using Borda reduction (Jamieson
et al., 2015b). According to this technique, whenever
the algorithm asks to draw a sample from item i, we
compare item i to a randomly chosen item j, and ascribe a reward of 1 to item i if i wins the duel, and 0
otherwise. This is equivalent to the rewards being sampled from a Bernoulli distribution with means given by
the Borda scores of the items. The Borda score of an
item i is defined as
1 X
P(i > j).
(2)
pi :=
K −1
j6=i

Related Work

There is extensive work on ranking from noisy pairwise comparisons, we refer the reader to excellent surveys by Busa-Fekete and Hüllermeier (2014); Agarwal
(2016). We discuss the most relevant work next.
2.1

Ranking from Pairwise Comparisons

The pairwise comparison matrix P (where Pij = P(i >
j)) and assumptions on it play a major role in the
design of ranking algorithms (Agarwal, 2016). A sequence of progressively relaxed assumptions on P can
be shown where ranking methods that work under
restrictive assumptions fail when these assumptions
are relaxed (Rajkumar and Agarwal, 2014; Rajkumar
et al., 2015). Spectral ranking algorithms have been
proposed when comparisons are available for a fixed set
of pairs (Negahban et al., 2012a,b); this corresponds to
a partially observed P matrix. Braverman and Mossel (2009); Wauthier et al. (2013) propose and analyze
algorithms for the noisy-permutation model; this corresponds to a P matrix which has two types of entries:
1 − p in the upper triangle and p in the lower triangle
(assuming the true ordering of the items is 1 . . . K).
They also focus on settings where queries cannot be
repeated. Our work makes no assumptions on the P
matrix and ranks items using their Borda scores. This
is important given the futility of parametric models to
model real-life scenarios (Shah et al., 2016).
Quicksort is another highly recommended algorithm
for ranking using noisy pairwise comparisons. Maystre
and Grossglauser (2017) study Quicksort under the
BTL noise model, and Alonso et al. (2003) analyze
Quicksort under the noisy permutation model. We
comment on these in Section 3.
Jamieson and Nowak (2011) propose an algorithm

Katariya, Jain, Sengupta, Evans, Nowak

for active ranking from pairwise comparisons when
points can be embedded in Euclidean space. Ailon
(2012) consider ranking when query responses are
fixed. More recently, Agarwal et al. (2017) consider
top-m item identification and ranking under limited
rounds of adaptivity, Falahatgar et al. (2017) consider the problem of finding the maximum and ranking assuming strong-stochastic transitivity and the
stochastic-triangle inequality. We do not need these
assumptions.
Our setting is closest to the setting proposed by Heckel
et al. (2016), in the context of ranking using pairwise comparisons. Our setting however applies to realvalued rewards as well as pairwise comparison feedback. Furthermore, our setting incorporates the notion of -optimality which allows the user to specify
an error tolerance (Even-Dar et al., 2006). This is important in practice if the item means are very close to
each other. Finally, as they note, their Active Ranking (AR) algorithm is an elimination-style algorithm,
our LUCBRank is UCB-style; it is known that the latter
perform better in practice (Jiang et al., 2017). We also
verify this empirically in Section 7.2, and observe that
LUCBRank requires 2-3x fewer samples than AR in our
synthetic as well as real-world experiments (see Fig. 2
and Fig. 5).
2.2

Relation to Bandits

The idea of sampling items based on lower and upper
confidence bounds is well-known in the bandits literature (Auer, 2002). However, these algorithms either
focus on finding the best or top-m items (Audibert
and Bubeck, 2010; Kalyanakrishnan et al., 2012; Kaufmann et al., 2015; Chen et al., 2017), or on minimizing
regret (Bubeck et al., 2012). This is the first work to
our knowledge that employs this tool for ranking.

3

Motivation

We argue that existing adaptive methods offer no
significant gains over their non-adaptive counterparts
when the goal is to find a complete ranking, and coarse
ranking is more appropriate for many real-world applications. We provide brief theoretical justification
for this claim in the discussion after quote (1), and
empirically verify this behavior in Fig. 4. In this
section, we focus on Quicksort, because it has been
well-studied under multiple noise models. Quicksort
has optimal sample complexity when comparisons are
noiseless (Sedgewick and Wayne, 2011) and is naturally appealing when comparisons are noisy (Maystre
and Grossglauser, 2017). Intuitively it feels like the
right thing to do - by comparing an item with the
pivot and putting it left or right appropriately, Quicksort performs a binary search for the true position of

an item. However it is far from optimal under two
noise models as we argue next.
First, consider the noisy-permutation (NP) noise
model (Feige et al., 1994) where the outcomes of pairwise comparisons are independently flipped with an
error probability p. In the first stage of Quicksort, every item that is compared with the pivot and put in the
wrong bucket contributes on average K
2 to the Kendall
tau error (total number of inverted pairs). Now, Kp
items are put in the wrong bucket on average in the
first stage of Quicksort, and hence the total number of
inverted pairs is at least Ω(K 2 p). Alonso et al. (2003)
show that Θ(K 2 p) is indeed the expected number of
inversions. This is far from optimal because Braverman and Mossel (2009) propose an algorithm which
has a Kendall tau error of O(K) with high probability, using K log K comparisons (same as quicksort).
Alonso et al. (2003) conjecture that for quicksort to
have O(K) expected inversions, p needs to go down
1
faster than 1/K, like K log
K . As the above calculation
shows, they conjecture that this is because Quicksort is
extremely brittle: “the main contribution (to the total
inversions) comes from the ‘first’ error, in some sense.”
One may be able to get rid of this lack of robustness by
repeating queries, but this requires knowledge of the
error probability p or adapting to its unknown value.
This is possible, but as we argue shortly, a good model
for real-world problems where comparisons are made
by humans is one where p increases to 1/2 as K grows,
since it becomes more difficult to compare adjacent
items in the true ranking as K increases. Quicksort
certainly fails in this regime.
The other class of well-studied noise models are the
Bradley-Terry-Luce (BTL) (Bradley and Terry, 1952)
or Thurstone (Thurstone, 1927) models, which assume
a K-dimensional weight vector that measures the quality of each item, and the pairwise comparison probabilities are determined via some fixed function of the
qualities of pair of objects. These models are more
realistic than the NP model since under these models,
comparisons between items that are far apart in the
true ranking are less noisy than those between nearby
items. Maystre and Grossglauser (2017) analyze the
expected number of inversions of Quicksort under the
BTL model, and show that when the average gap between adjacent items is ∆, the expected number of inversions is O(∆−3 ). They note however that real-world
datasets have extremely small ∆ ( ˆ
∆−1 = 376 in their
experiments) and Quicksort performs no better than
random (see quote (1)). We make similar observations
about the inefficacy of Quicksort (and other adaptive
algorithms) in our real-world experiments (see Fig. 4).
The problem in finding an exact/total ranking is that
if the means of the items lie in a bounded range,

Adaptive Sampling for Coarse Ranking

e.g., [0, 1], then the minimum gap must decrease at
least linearly with K and many items become essentially indistiguishable. To see this, suppose there is
a constant gap ∆ between consecutive means and let
3
e. Then, assuming the logistic model, the mm = d∆
th item beats the 1st item with probability ≥ 0.95,
the 2m-th item beats the m-th item with probability ≥ 0.95, and so on. Thus, items that are m-apart
can be considered distinguishable. Assuming the range
of possible means is bounded implies that ∆ ∝ 1/K.
Thus, the number of items that are essentially indistiguishable increases linearly with K, suggesting that
seeking a total ranking is a futile effort. This situation arises in applications such as Place Pulse where
humans rate street view images according to their perceived safety (Naik et al., 2014), or the task in Wood
et al. (2017) where humans rate face images according
to the strength of their emotions.
Coarse ranking allows the experimenter to set the
number of clusters in accordance with the number
of distinguishable levels, and thus frees the algorithm
from the task of distinguishing incomparable items.
In this sense, it converts a high-noise problem to a
low-noise one. Even though the gap between adjacent
items is small, most items are far from their nearest
cluster boundary, and an adaptive algorithm can stop
sampling these items early.

4

Setting

In this section, we precisely formulate the coarse ranking setting. For ease of reference, we use terminology
from the bandits literature and refer to an item as
arm. Also, pulling or drawing an arm is equivalent to
sampling from the item’s reward distribution.
Consider a multi-armed bandit with K arms. Each
arm a corresponds to a Bernoulli distribution with an
unknown mean pa , denoted B(pa ). A draw / pull of
arm a yields a reward from distribution B(pa ). Without loss of generality, assume the arms are numbered
so that p1 ≥ p2 · · · ≥ pK .
Given an integer c ≥ 2 representing the number of clusters, let 1 ≤ κ1 < κ2 < · · · < κc = K be a collection
of positive integers. Any such collection of positive integers defines a partition of [K] into c disjoint sets of
the form
M1∗ := {1, . . . , κ1 }, M2∗ := {κ1 + 1, . . . , κ2 }, . . . ,
. . . , Mc∗ := {κc−1 + 1, . . . , K}.

(3)

To solve the coarse ranking problem given a set of
cluster boundaries (κi )ci=1 , an algorithm may sample
arms of the K-armed bandit and record the results;
the algorithm is required to terminate and cluster the
arms into an ordered set of disjoint sets of the form
(3). We refer to this output as a coarse ranking.

We next define the notion of -tolerance. For some
∗
fixed tolerance  ∈ [0, 1] and 1 ≤ i ≤ c, let Mi,
be
the set of all arms that should be in cluster i upto a
tolerance , i.e.
∗
Mi,
:= {a : pκi−1 +1 +  ≥ pa ≥ pκi − },

(with the convention that pκ0 = 1). Note that the true
set of arms in cluster i: Mi∗ := {κi−1 + 1, . . . , κi }, is a
∗
subset of Mi,
; the latter set contains in addition arms
that are  close to the boundary.
For a given mistake probability δ ∈ [0, 1] and a given
error tolerance  ∈ [0, 1], we call an algorithm (, δ)PAC if, with a probability greater that 1−δ, after using
a finite number of samples, it returns a rank for each
arm such that the ith ranked cluster according to the
∗
returned ranking is a subset of Mi,
for all 1 ≤ i ≤ c.
Formally, if σ(a) is the rank of arm a returned by the
algorithm after using a finite number of samples, we
can define the empirical cluster i as
M̂i := {a : κi−1 + 1 ≤ σ(a) ≤ κi },
and we say the algorithm is (, δ)-PAC if


∗
P ∃ i such that M̂i 6⊆ Mi,
≤ δ.

5

(4)

Algorithm

Let (κ1 , . . . , κc = K) be the cluster boundaries. We
describe here the LUCBRank algorithm using generic
confidence intervals Ia = [La (t), Ua (t)], where t indexes rounds of the algorithm. Let Na (t) be the number of times arm a has been sampled up to round t,
and Sa (t) be the sum of rewards of arm a up to round
Sa (t)
be the corresponding empirical
t. Let p̂a (t) = N
a (t)
mean reward. Sort the arms in the decreasing order of
their empirical mean rewards, and for 1 ≤ i ≤ c − 1,
let Ji (t) denote the κi arms with the highest empirical
mean rewards. Define
lti := arg min La (t),
a∈Ji (t)

uit := arg max Ua (t)

(5)

a/
∈Ji (t)

to be the two critical arms from Ji (t) and Jic (t) that
are likely to be misclassified (see Fig. 1).
Algorithm 1 contains the pseudocode of LUCBRank,
which is also depicted in Fig. 1. The algorithm maintains active cluster boundaries in the set C, where
a cluster boundary i is active if the overlap of confidence intervals in Ji and Jic is not less than . In
every round, it samples both the critical arms at every active cluster boundary (lines 11-15). At the end
of every round, it checks if the critical arms at any
boundary are separated according to the tolerance criterion, and removes such boundaries from the active

Katariya, Jain, Sengupta, Evans, Nowak

Algorithm 1 LUCBRank
1: Input:  > 0, cluster boundaries 1 ≤ κ1 , . . . , κc =

K
<ε?

Figure 1: A visualization of LUCBRank on a bandit instance with K = 20 arms, c = 3 clusters, with boundaries at κ1 = 5, κ2 = 15. Also shown are the critical
arms lti , uit pulled at each boundary. The algorithm
stops sampling a boundary when the confidence interval overlap is less than .
set (lines 21-25). For our experiments, we use KL-UCB
(Garivier and Cappé, 2011) confidence intervals. For
an exploration rate β(t, δ), the KL-UCB upper and lower
confidence bounds for arm a are calculated as
Ua (t) := max{q ∈ [p̂a (t), 1] : Na (t)d(p̂a (t), q) ≤ β(t, δ)},
La (t) := min{q ∈ [0, p̂a (t)] : Na (t)d(p̂a (t), q) ≤ β(t, δ)}.
(6)

where d(x, y) is the Kullback-Leibler divergence between two Bernoulli distributions, given by d(x, y) =
x log xy + (1 − x) log 1−x
1−y .
LUCBRank can also be easily modified for pairwisecomparison queries: whenever the algorithm calls for
drawing an arm i, duel arm i with another arm chosen
uniformly at random.

6

Analysis

We prove the accuracy of LUCBRank in Theorem 1,
and give an upper bound on the sample complexity in
Theorem 2. Our distribution-dependent lower bound
for the sample complexity of any δ-PAC algorithm is
stated in Theorem 3. All proofs can be found in the
Appendix. Recall that 1 ≤ κ1 < κ2 < · · · < κc−1 <
κc = K are the cluster boundaries.
6.1

PAC Guarantee

Theorem 1 gives choices of β(t, δ) such that LUCBRank
is correct with probability at least δ, in the sense defined by (4).
α
Theorem 1. LUCBRank using β(t, δ) = log( k1 Kt
)+
δ

k1 Ktα
c−1 α
2e
log log( δ ) with α > 1 and k1 > 2
+ α−1 +
4e
,
is
correct
with
probability
1
−
δ.
2
(α−1)
6.2

Sample Complexity

Our sample complexity results are stated in terms of
Chernoff information (Cover and Thomas, 2012).
Chernoff Information: Consider two Bernoulli distributions B(x) and B(y), and let d(x, y) denote the

2: t ← 1
3: C ← {1, . . . , c − 1}
//active cluster boundaries
4:
5: for a = 1, . . . , K do
6:
Sample item a, compute Ua (1) and La (1)
7: end for
8:
9: while C 6= ∅ do
10:
// Sample active cluster boundaries
11:
for i ∈ C do
12:
Sample item lti
13:
Sample item uit
14:
(If pairwise comparing, compare item lti to a

15:
16:
17:

random other item, and compare item uit to a
random other item. See Section 1.1)
end for
t=t+1
∀ a ∈ [K] : Update reward-estimate p̂a (t), number of samples Na (t), and confidence bounds
Ua (t), La (t) (see (6))
∀ i ∈ C: Compute lti , uit (see (5))

18:
19:
20:
// Eliminate unambiguous cluster boundaries
21:
for i ∈ C do
22:
if Uuit (t) − Llti (t) <  then
23:
C =C \i
24:
end if
25:
end for
26: end while
27:
28: Return items sorted by their empirical mean re-

wards.
KL-divergence between these distributions. The Chernoff information d∗ (x, y) between these two Bernoulli
distributions is defined by
d∗ (x, y) := d(z ∗ , x) = d(z ∗ , y)
where z is the unique z such that d(z, x) = d(z, y).
∗

Next we introduce some notation. For an arm a, let
g(a) (read group of arm a) denote the index of the
cluster that arm a belongs to. Formally,
g(a) := min{1 ≤ i ≤ c : pa ≤ pκi }.
(7)
Let bi ∈ [pκi , pκi +1 ], 1 ≤ i ≤ c − 1 be any points in
the cluster boundary gaps, and b := (b1 , b2 , . . . , bc−1 ).
Define

d∗ (pa , b1 )
a ∈ {1, . . . , κ1 }



min(d∗ (p , b
),
d∗ (pa , bg(a) )
a
g(a)−1
∆∗b (a) :=

a ∈ {κ1 + 1, . . . , κc−1 }


 ∗
d (pa , bc−1 )
a ∈ {κc−1 + 1, . . . , K}

(8)

Adaptive Sampling for Coarse Ranking

to be the “distance” of each arm from the closest cluster boundary. Our upper bound on the sample complexity of LUCBRank is stated in Theorem 2, and con∗
tains the quantity H,b
where
X
1
∗
H,b
:=
.
(9)
max(∆∗b (a), 2 /2)

where g(a) defined in (7) is the cluster that arm a belongs to. We highlight the differences from (8). First,
the Chernoff information in (8) is replaced with KLdivergence in (11), and second, the distance is measured with the closest arm in either adjacent cluster
here, as opposed to a point in the gap between the
clusters in (8).

Theorem 2. Let b = (b1 , b2 , . . . , bc−1 ), where αbi ∈
)+
[pκi , pκi +1 ]. Let  > 0. Let β(t, δ) = log( k1 Kt
δ

α
c−1 α
4e
2e
)
with
k
>
+
.
+
log log( k1 Kt
1
δ
2
α−1
(α−1)2 Let
τ be the random number of samples taken by LUCBRank
before termination. If α > 1,


∗ α 
k1 K(2H,b
)
∗
P τ ≤ 2C0 (α)H,b
log
≥1−δ
δ

Our lower bound involves the quantity

a∈{1,...,K}

where  C0 (α)
is
such  that
1 + 1e α log(C0 (α)) + 1 + αe .
6.3

C0 (α)

≥

Distribution-Dependent Lower Bound

In this section, we state our non-asymptotic lower
bound on the expected number of samples needed by
any δ-PAC algorithm to cluster and rank the arms into
groups of sizes (κ1 , κ2 − κ1 , . . . , K − κc−1 ). For simplicity, we focus on the case  = 0. The proof of the
lower bound uses standard change of measure arguments (Kaufmann et al., 2015), which requires some
continuity and well-separation assumptions. We state
these next.

and is as follows:
Theorem 3. Let p ∈ Mκ , and assume that P satisfies
Assumption 1; any coarse ranking algorithm that is δPAC on Mκ satisfies, for δ ≤ 0.15,




X
1
1
 log
Ep [τ ] ≥ 
∆KL
2.4δ
κ (a)
a∈1,...,K

6.4 Remarks
• The tightest high-probability upper bound is ob∗
in
tained by setting b equal to
arg min H,b
b:bi ∈[pκi ,pκi +1 ]

Theorem 2.
• Although stated for Bernoulli distributions, the
results in this paper can easily be extended to
rewards in the exponential family (Garivier and
Cappé, 2011) by using the appropriate d function.

7

Mκ = {p = (p1 , . . . , pK ) : pi ∈ P, pκi > pκi +1 , 1 ≤ i < c},
(10)
7.1
where P is a set that satisfies

We also assume the following:
Assumption 1. For all p, q ∈ P 2 such that p 6= q, for
all α > 0,
there exists q1 ∈ P: KL(p, q) < KL(p, q1 ) < KL(p, q)+
α and EX∼q1 [X] > EX∼q [X],
there exists q2 ∈ P: KL(p, q) < KL(p, q2 ) < KL(p, q)+
α and EX∼q2 [X] < EX∼q [X].
To state our lower bound, we need to define for each
arm a, another “distance” from the boundary, similar
to (8). Define
∆KL
κ (a) :=


KL(pa , pκ1 +1 )
a ∈ {1, . . . , κ1 }



min(KL(pa , pκ
), KL(pa , pκg(a) +1 )
g(a)−1




KL(pa , pκc−1 )

a ∈ {κ1 + 1, . . . , κc−1 }
a ∈ {κc−1 + 1, . . . , K},
(11)

(12)

∆KL
κ (a)
a∈1,...,K

We consider the following class of bandit models where
the clusters are unambiguously separated, i.e.

∀ p, q ∈ P 2 , p 6= q ⇒ 0 < KL(p, q) < +∞.

1

X

Experiments
Ranking from Direct Feedback
1.0

Empirical mistake probability
Uniform
AR
LUCBRank

0.8
0.6
0.4
0.2
0.0

4K

8K

#Samples

12K

16K

Figure 2: Exp 1 (description in text)
We first compare LUCBRank with uniform sampling and
the Active Ranking (AR) algorithm (Heckel et al.,
2016). AR is an adaptation of the successive elimination approach to solve the coarse ranking problem.
It maintains a set of unranked items and samples every item in this set, removing an item from the set
when it is confident of the cluster the item belongs

Katariya, Jain, Sengupta, Evans, Nowak

to. Although developed for pairwise comparison feedback, AR can easily be adapted to the direct-feedback
setting.
We look at the bandit instance B with K = 15 arms
whose rewards are Bernoulli distributed with means
a
for a = 2, 3, . . . , K). This prob(p1 = 12 ; pa = 12 − 40
lem has been studied in the literature in the context
of finding the best-arm (Bubeck et al., 2013). We consider the problem of finding the top-3 and the bottom3 arms, which corresponds to κ1 = 3, κ2 = 12.
In Fig. 2, we record the probability (averaged over
1000 simulations) that the empirical clusters returned
by the algorithm do not match the true clusters. We
set δ = 0.1 for both LUCBRank and AR, and  = 0 in
LUCBRank to have a fair comparison with AR. We see
that the mistake probability drops faster for LUCBRank
than for AR.

Terry-Luce (BTL) model (Bradley and Terry, 1952)
using maximum likelihood estimation, and used this
as the ground truth to generate noisy comparisons.
Given two items i and j with scores θi and θj , the BTL
model estimates the probability that item i is preferred
θi
to item j as P(i > j) = eθie+eθj . Fig. 3(b) shows 4 images overlayed with their estimated BTL scores (where
the lowest score was set to 0), and Fig. 3(c) shows a
scatter plot of the scores of all 100 images.
0.10

Fraction of inverted pairs
Uniform
AR
UniformParam
QSParam

0.08
0.06
0.04
0.02

7.2

Ranking from Pairwise Comparisons

1.09

2.98

3.77

(b)

0.0

20K

40K

60K

#Samples

80K

100K

Figure 4: The futility of adaptive methods if the goal
is to obtain a complete ranking. We compare uniform sampling with Active Ranking (both use nonparametric rank aggregation), and uniform sampling
with quicksort (where both use parametric rank aggregation). We see that the Kendall tau distance of
adaptive methods is no lower than those of their nonadaptive counterparts.

(a)

0.05

0.00

4.0
(c)

Figure 3: (a) A sample query on NEXT. (b) Four sample images and their estimated BTL scores beneath.
(c) Scatter plot of all the BTL scores, with the sample
image markers highlighted.
To measure the performance of our algorithm on realworld data, we selected K = 100 Google street view
images in Chicago, and collected 6000 pairwise responses on MTurk using NEXT (Jamieson et al.,
2015a), where we asked users to choose the saferlooking image out of two images. This experiment
is similar to the Place Pulse project (Naik et al.,
2014), where the objective is to assess how the appearance of a neighborhood affects its perception of safety.
Fig. 3(a) shows a sample query from our experiment.
We estimated the safety scores of these street view
images from the user-responses by fitting a Bradley-

We first study the performance of adaptive methods
with the goal of finding a complete ranking, and observe that adaptive methods offer no advantages when
items means are close to each other as they are in
this dataset. Oblivious of the generative model, a
lower bound (ignoring constants and log factors) on
the number of samples required
P to sort the items by
their Borda scores is given by 1/∆2i (Jamieson et al.,
2015b), where the ∆i s are gaps between consecutive
sorted Borda scores.
the dataset considered in
P For
this experiment,
1/∆2i = 322 million! We verify
the futility of adaptive methods in Fig. 4, where we
compare the performance of parametric as well as nonparametric adaptive methods in the literature (we describe these methods shortly) to their non-adaptive
counterparts, with a goal of finding a complete ranking of the images. In the parametric algorithms (UniformParam and QSParam), we find MLE estimates of
the BTL scores that best fit the pairwise responses.
In the non-parametric algorithms (Uniform and AR),
we estimate the scores using empirical probabilities in
Eq. (2). In Fig. 4, we plot the fraction of pairs that are
inverted in the empirical ranking compared to the true
ranking, and see no benefits for adaptive methods. We

Adaptive Sampling for Coarse Ranking

do see gains from adaptivity in the coarse formulation
(Fig. 5), as we explain next.
LUCBRank can be used in the pairwise comparison setting using Borda reduction, as described in Section 1.1.
The adaptive methods in literature we compare to
are AR (as in the previous section), and Quicksort
(QS) (Ailon et al., 2008; Maystre and Grossglauser,
2017). The Quicksort algorithm works exactly like its
non-noisy counterpart: it compares a randomly chosen
pivot to all elements, and divides the elements into two
subsets - elements preferred to the pivot, and elements
the pivot was preferred over. The algorithm then recurses into these two subsets. In this experiment, we
stop the quicksort algorithm early as soon as all the
subsets are inside the user-specified clusters. Continuing the algorithm further won’t change the items in
any cluster. This reduces the sample complexity of
Quicksort.
1.0

Empirical mistake probability

0.8
0.6
0.4
0.2
0.0

UnifParam
Uniform
AR
QSParam
QS
LUCBRank
500K
1M

#Samples

1.5M

2M

Figure 5: Probability of error in identifying the clusters: LUCBRank does better than parametric versions
of other active algorithms.
We consider the problem of clustering the images into
pentiles (κi = 20 i, 1 ≤ i ≤ 5). We set δ = 0.1 for
both LUCBRank and AR, and  = 0 in LUCBRank to ensure a fair comparison with AR. In Fig. 5, we record
the probability (averaged over 600 simulations) that
the empirical pentiles returned by the algorithm do
not match the true pentiles. We find that LUCBRank
has a lower mistake probability than even the parametric version of Quicksort, which assumes knowledge
of the BTL model. As an aside, note that when the
items are close as in this experiment, the parametric
versions of Uniform and Quicksort perform similarly,
and the active nature of Quicksort offers no significant
advantage.
In Fig. 6(a) and (b) we plot the ratio of inter-cluster
and intra-cluster inversions respectively of LUCBRank
and Uniform. An inter-cluster pair is a pair of items
that are in different clusters in the true ranking, while
an intra-cluster pair is a pair of items from the same
cluster. We see the that ratio of inter-cluster inversions goes down in Fig. 6(a), because that is the met-

0.98
0.96
0.94
0.92
0.90
0.88
0.86
0.84
0.82
1.07

Ratio of inter-cluster inversions
#interLUCB/#interUnif

20K

40K
60K
80K
#Samples
Ratio of intra-cluster inversions

100K

#intraLUCB/#intraUnif

1.06
1.05
1.04
1.03
1.02
1.01

20K

40K
60K
#Samples

80K

100K

Figure 6: (a) The ratio of inter-cluster inversions of
LUCBRank and Uniform. (b) The ratio of intra-cluster
inversions of LUCBRank and Uniform. LUCBRank focuses on minimizing inter-cluster inversions at the cost
of intra-cluster inversions.
ric LUCBRank focuses on. LUCBRank does not expend
effort on refining its estimate of an item’s rank once
its cluster has been found, and hence pays a price in
the form of intra-cluster inversions (Fig. 6(b)).

8

Conclusion

The coarse ranking setting is motivated from realworld problems where humans rate items. These problems have high noise and are hard, and a complete
ranking is not feasible; fortunately, it is often also
not necessary. We propose a practical online algorithm for solving it, LUCBRank, and prove distributiondependent upper and lower bounds on its sample complexity. We evaluate its performance on crowdsourced
data gathered using MTurk, and observe that it performs better than existing algorithms in the literature.
We leave open several questions. First, our upper
bound is stated in terms of Chernoff information between distributions, while our lower bound is in terms
of KL-divergences, and there is a gap between the
two. Second, the cluster boundaries need to be userspecified in our current setting. If the gap between the
nearest items in adjacent clusters is small, this can adversely affect the sample complexity. Although this is
partially addressed through the error-tolerance , an
attractive algorithm would be one which auto-tunes
the positions of the cluster boundaries at the widest
gaps, subject to user-specified constraints.
To the best of our knowledge, this paper presents the
first bandit UCB algorithm for ranking.

Katariya, Jain, Sengupta, Evans, Nowak

Acknowledgements
The authors would like to thank Scott Sievert and Xiaomin Zhang for help with experiments, and Ervin
Tanczos for discussions.

L. Chen, J. Li, and M. Qiao. Nearly instance optimal
sample complexity bounds for top-k arm selection.
In Artificial Intelligence and Statistics, pages 101–
110, 2017.

References

T. M. Cover and J. A. Thomas. Elements of information theory. John Wiley & Sons, 2012.

A. Agarwal, S. Agarwal, S. Assadi, and S. Khanna.
Learning with limited rounds of adaptivity: Coin
tossing, multi-armed bandits, and ranking from
pairwise comparisons. In Conference on Learning
Theory, pages 39–75, 2017.

A. Dubey, N. Naik, D. Parikh, R. Raskar, and C. A.
Hidalgo. Deep learning the city: Quantifying urban
perception at a global scale. In European Conference
on Computer Vision, pages 196–212. Springer, 2016.

S. Agarwal. On ranking and choice models. In IJCAI,
pages 4050–4053, 2016.
N. Ailon. An active learning algorithm for ranking
from pairwise preferences with an almost optimal
query complexity. Journal of Machine Learning Research, 13(Jan):137–164, 2012.
N. Ailon, M. Charikar, and A. Newman. Aggregating inconsistent information: ranking and clustering. Journal of the ACM (JACM), 55(5):23, 2008.
L. Alonso, P. Chassaing, F. Gillet, S. Janson, E. M.
Reingold, and R. Schott. Sorting with unreliable
comparisons: A probabilistic analysis. 2003.
J.-Y. Audibert and S. Bubeck. Best arm identification
in multi-armed bandits. In COLT-23th Conference
on Learning Theory-2010, pages 13–p, 2010.
P. Auer. Using confidence bounds for exploitationexploration trade-offs. Journal of Machine Learning
Research, 3(Nov):397–422, 2002.
R. A. Bradley and M. E. Terry. Rank analysis of
incomplete block designs: I. the method of paired
comparisons. Biometrika, 39(3/4):324–345, 1952.
M. Braverman and E. Mossel. Sorting from noisy information. arXiv preprint arXiv:0910.1191, 2009.
S. Bubeck, N. Cesa-Bianchi, et al. Regret analysis
of stochastic and nonstochastic multi-armed bandit
problems. Foundations and Trends R in Machine
Learning, 5(1):1–122, 2012.
S. Bubeck, T. Wang, and N. Viswanathan. Multiple
identifications in multi-armed bandits. In International Conference on Machine Learning, pages 258–
265, 2013.
R. Busa-Fekete and E. Hüllermeier. A survey of
preference-based online learning with bandit algorithms. In International Conference on Algorithmic
Learning Theory, pages 18–39. Springer, 2014.

E. Even-Dar, S. Mannor, and Y. Mansour. Action
elimination and stopping conditions for the multiarmed bandit and reinforcement learning problems.
Journal of machine learning research, 7(Jun):1079–
1105, 2006.
M. Falahatgar, A. Orlitsky, V. Pichapati, and A. T.
Suresh. Maximum selection and ranking under noisy
comparisons.
arXiv preprint arXiv:1705.05366,
2017.
U. Feige, P. Raghavan, D. Peleg, and E. Upfal. Computing with noisy information. SIAM Journal on
Computing, 23(5):1001–1018, 1994.
A. Garivier and O. Cappé. The kl-ucb algorithm for
bounded stochastic bandits and beyond. In COLT,
pages 359–376, 2011.
R. Heckel, N. B. Shah, K. Ramchandran, and M. J.
Wainwright. Active ranking from pairwise comparisons and the futility of parametric assumptions.
arXiv preprint arXiv:1606.08842, 2016.
K. G. Jamieson and R. Nowak. Active ranking using
pairwise comparisons. In Advances in Neural Information Processing Systems, pages 2240–2248, 2011.
K. G. Jamieson, L. Jain, C. Fernandez, N. J. Glattard, and R. Nowak. Next: A system for real-world
development, evaluation, and application of active
learning. In Advances in Neural Information Processing Systems, pages 2656–2664, 2015a.
K. G. Jamieson, S. Katariya, A. Deshpande, and R. D.
Nowak. Sparse dueling bandits. In AISTATS, 2015b.
H. Jiang, J. Li, and M. Qiao. Practical algorithms for
best-k identification in multi-armed bandits. arXiv
preprint arXiv:1705.06894, 2017.
S. Kalyanakrishnan, A. Tewari, P. Auer, and P. Stone.
Pac subset selection in stochastic multi-armed bandits. In Proceedings of the 29th International Conference on Machine Learning (ICML-12), pages
655–662, 2012.

Adaptive Sampling for Coarse Ranking

E. Kaufmann and S. Kalyanakrishnan. Information
complexity in bandit subset selection. In COLT,
pages 228–251, 2013.
E. Kaufmann, O. Cappé, and A. Garivier. On the
complexity of best arm identification in multi-armed
bandit models. The Journal of Machine Learning
Research, 2015.
L. Maystre and M. Grossglauser. Just sort it! a simple
and effective approach to active preference learning.
In Proceedings of Machine Learning Research, volume 70, 2017.
N. Naik, J. Philipoom, R. Raskar, and C. Hidalgo.
Streetscore-predicting the perceived safety of one
million streetscapes. In Proceedings of the IEEE
Conference on Computer Vision and Pattern Recognition Workshops, pages 779–785, 2014.
S. Negahban, S. Oh, and D. Shah. Iterative ranking
from pair-wise comparisons. In Advances in Neural
Information Processing Systems, pages 2474–2482,
2012a.
S. Negahban, S. Oh, and D. Shah. Rank centrality:
Ranking from pair-wise comparisons. arXiv preprint
arXiv:1209.1688, 2012b.
A. Rajkumar and S. Agarwal. A statistical convergence perspective of algorithms for rank aggregation
from pairwise data. In Proceedings of the 31st International Conference on Machine Learning, pages
118–126, 2014.
A. Rajkumar, S. Ghoshal, L.-H. Lim, and S. Agarwal. Ranking from stochastic pairwise preferences:
Recovering condorcet winners and tournament solution sets at the top. In International Conference on
Machine Learning, pages 665–673, 2015.
R. Sedgewick and K. Wayne. Algorithms. AddisonWesley Professional, 2011.
N. Shah, S. Balakrishnan, A. Guntuboyina, and
M. Wainwright. Stochastically transitive models
for pairwise comparisons: Statistical and computational issues. In International Conference on Machine Learning, pages 11–20, 2016.
L. L. Thurstone. A law of comparative judgment. Psychological review, 34(4):273, 1927.
F. Wauthier, M. Jordan, and N. Jojic. Efficient ranking from pairwise comparisons. In International
Conference on Machine Learning, pages 109–117,
2013.

A. Wood, J. Martin, and P. Niedenthal. Towards
a social functional account of laughter: Acoustic
features convey reward, affiliation, and dominance.
PloS one, 12(8):e0183811, 2017.

Katariya, Jain, Sengupta, Evans, Nowak

9

Appendix

9.1

PAC Guarantee

We’ll use the following lemma (Kaufmann and Kalyanakrishnan, 2013) which bounds the probability of ‘bad’
events in round t.
Lemma 1. Let Ua (t) and La (t) be the confidence bounds defined in Eq. (6). For any algorithm and arm a,
P(Ua (t) < pa ) = P(La (t) > pa ) ≤ e(β(t, δ) log t + 1) exp(−β(t, δ))

We shall also need the following technical lemma, which we’ll use to upper bound the probability of any bad
event.
α

α

) + log log( k1 Kt
),
Lemma 2. If β(t, δ) = log( k1 Kt
δ
δ
∞
X

δ
k1 K







(β(t, δ) log t + 1) exp(−β(t, δ)) ≤

t=1

1
2
+
(α − 1)2
(α − 1)



Proof. Let us consider
β(t, δ)(log t)e

−β(t,δ)



= log



k1 Ktα
δ


≤ 2 log



k1 Ktα
δ

= 2 log t ·

+ log log

· log t ·

k1 Ktα
δ

(log t)

1
δ
·
α
k
α
k1 Kt
log 1 Kt
δ
!

!

δ
1
·
α
k1 Ktα log k1 Kt
δ

δ
k1 Ktα

Hence
∞
X
t=1

9.1.1

∞ 
X

δ
δ
+
α
k1 Kt
k1 Ktα
t=1


δ
2
1
≤
+
k1 K (α − 1)2
(α − 1)

(β(t, δ) log t + 1) exp(−β(t, δ)) ≤



2 log t ·

Proof of Theorem 1
α

α

2e
4e
Theoremm. LUCBRank using β(t, δ) = log( k1 Kt
) + log log( k1 Kt
) with α > 1 and k1 > 1 + α−1
+ (α−1)
2 , is
δ
δ
correct with probability 1 − δ.

Proof. Consider the event
W =

\

\

((Ua (t) > pa ) ∩ (La (t) < pa ))

t∈N a∈{1,...,K}

where all arms are well-behaved i.e. their true means are inside their confidence intervals. We show that LUCBRank
is correct on the event W .
Assume LUCBRank fails, which means that when it terminates, there exists a cluster i, such that arm a belongs
∗,c
to cluster i in the returned ranking, and a ∈ M,i
; that is, either 1) pa > pκi−1 +1 +  or 2) pa < pκi − .

Adaptive Sampling for Coarse Ranking

Consider the first case: pa > pκi−1 +1 +. Consequently, there exists arm b such that pb ≤ pκi−1 +1 , and τ (b) ≤ κi−1
in the returned ranking. Since the algorithm stopped and boundary i − 1 was removed from the set of active
boundaries C, it must be the case that Ua (t) − Lb (t) <  upon stopping. Hence, the following holds:
[

(∃ a, b : pa > pκi−1 +1 + , pb ≤ pκi−1 +1 , Ua (t) − Lb (t) < )

t∈N

⊆

[

(∃ a, b : (Ua (t) < pb +  < pa ) ∪ (Lb (t) > pb ))

t∈N

⊆

[

[

[

(Ua (t) < pa )

t∈N a∈{1,...,K}

(Lb (t) > pb ) ⊆ W c

b∈{1,...,K}

Consider the second case: pa < pκi − . Consequently, there exists an arm b such that pb ≥ pκi , and τ (b) > κi in
the returned ranking. Since the algorithm stopped and boundary i was removed from the set of active boundaries
C, it must be the case that Ub (t) − La (t) <  upon stopping. Hence, the following holds:
[

(∃ a, b : pa < pκi − , pb ≥ pκi , Ub (t) − La (t) < )

t∈N

⊆

[

(∃ a, b : (Ub (t) < pb ) ∪ (La (t) > pb −  > pa ))

t∈N

⊆

[

[

[

(Ub (t) < pb )

t∈N b∈{1,...,K}

(La (t) > pa ) ⊆ W c

a∈{1,...,K}

Hence
P(LUCBRank fails) ≤ P(W c )
∞
X
(β(t, δ) log t + 1) exp(−β(t, δ))
≤ 2eK

(by Lemma 1)

t=1

δ
≤
k1



2e
4e
+
2
(α − 1)
(α − 1)


(by Lemma 2)

≤δ

9.2

(by the constraint on k1 )

Sample Complexity

We define the event Wt which says that all arms are well-behaved in round t i.e. their true means are contained
inside their confidence intervals.
\
Wt =
((Ua (t) > pa ) ∩ (La (t) < pa ))
a∈{1,2,...,K}

Note that the event W defined earlier is W = ∪t∈N Wt .
Proposition 1 gives a sufficient condition for stopping.
Proposition 1. Let bi ∈ [pκi , pκi +1 ]. If Uuit − Llti >  and Wt holds, then either k = lti or k = uit satisfies
bi ∈ Ik (t) and β̃k (t) >
where we define β̃a (t) =

q


,
2

β(t,δ)
2Na (t)

Proof. Our Wt condition is stronger than that required in the Proposition 1 in Kaufmann and Kalyanakrishnan
(2013), and hence their proof applies.

Katariya, Jain, Sengupta, Evans, Nowak

Lemma 3 is another concentration result that will be used in our sample complexity guarantee.
Lemma 3. Let T ≥ 1 be an integer, and 1 ≤ i ≤ (c − 1) be any cluster boundary. Let δ > 0, γ > 0 and x ∈]0, 1[
be such that pa 6= x. Then




T
X
exp(−γ)
γ
,
N
(t)d(p̂
(t),
x)
≤
γ
≤ ∗
P a = uti ∨ a = lit , Na (t) >
a
a
∗ (p , x)
d
d
(pa , x)
a
t=1

We prove the following lemma, which states that the Chernoff information increases as the second distribution
moves away from the first.
Lemma 4. If x < y < y 0 or x > y > y 0 , d∗ (x, y) ≤ d∗ (x, y 0 )
Proof. We shall prove the statement for the case x < y < y 0 . The proof for x > y > y 0 is analogous.
Let z ∗ be the unique z such that d(z ∗ , x) = d(z ∗ , y). Since z ∗ < y < y 0 , d(z ∗ , y 0 ) ≥ d(z ∗ , y) = d(z ∗ , x). Hence,
0
0
0
there exists z ∗ ≥ z ∗ such that d∗ (x, y) = d(z ∗ , x) ≤ d(z ∗ , x) = d(z ∗ , y 0 ) = d∗ (x, y 0 ).
Lemma 5. Let x∗ be the solution of the equation:
1
x=
γ



xα
xα
log
+ log log
η
η

Then if γ < 1 and η < 1/ee ,
1
log
γ
where C0 is such that C0 ≥ 1 + 1e





1
ηγ α



≤ x∗ ≤

C0
log
γ



1
ηγ α




α log C0 + 1 + αe .



α
α
Proof. x∗ is upper bounded by any x such that γ1 log xη + log log xη
≤ x. We look for x∗ of the form


C0
1
γ log ηγ α .
1
γ





 α
xα
xα
1
1
x
+ log log
log
≤
1+
log
η
η
γ
e
η



1
1
1
1
=
1+
α log C0 + log α + α log log α
γ
e
ηγ
ηγ





1
1
α
1
≤
1+
α log C0 + 1 +
log α
γ
e
e
ηγ


1
1 
α
1
≤
1+
α log C0 + 1 +
log α
γ
e
e
ηγ

where the first and second inequalities hold because log x ≤ xe , and the last inequality holds because ηγ1α > e.
Choosing C0 such that


1 
α
C0 ≥ 1 +
α log C0 + 1 +
e
e
gives us our upper bound.
To prove the lower bound, consider the series defined by
x0 = 1
1
xn+1 =
γ



xα
xα
log n + log log n
η
η



Adaptive Sampling for Coarse Ranking

First note that since γ < 1 and η < 1/ee , the sequence is increasing. Second, note that the sequence converges
to x∗ . Hence


 
α 

α 
1
1
1
1
1
1
1
log + log log
log + log log
log
+ log log
x ≥ x2 =
γ
ηγ α
η
η
ηγ α
η
η





1
1
1
1
1
1
1
=
log α + α log log + log log
+ log log α + α log log log + log log
γ
ηγ
η
η
ηγ
η
η
1
1
≥ log α
γ
ηγ
∗

since η < 1/ee .

Corollary 1. Let γ = 2H1∗ , η = k1δK . Then applying Lemma 5 gives
,b

∗
2H,b
log

9.3



∗ α
k1 K(2H,b
)
δ



∗
≤ S1∗ ≤ 2C0 (α)H,b
log



∗ α
k1 K(2H,b
)
δ



Proof of Theorem 2
α

Theoremm. Let b = (b1 , b2 , . . . , bc−1 ), where bi ∈ [pκi , pκi +1 ]. Let  > 0. Let β(t, δ) = log( k1 Kt
)+
δ
k1 Ktα
2e
4e
log log( δ ) with k1 > 1 + α−1 + (α−1)2 . Let τ be the random number of samples taken by LUCBRank before termination. If α > 1,

P

∗
τ ≤ 2C0 (α)H,b
log

where C0 (α) is such that C0 (α) ≥ 1 + 1e



∗ α
k1 K(2H,b
)
δ


≥1−δ


α log(C0 (α)) + 1 + αe .



Proof. The LUCBRank algorithm proceeds in rounds. In a round, it samples the two arms on opposite sides of an
active boundary whose confidence intervals overlap the most. A boundary is active as long as this overlap is less
than . Thus, the number of samples up to round T is

#samples(T ) ≤ 2

T X
c−1
X
t=1 i=1

=2

T
X c−1
X
t=1 i=1

≤2

T X
c−1
X
t=1 i=1

≤2

T X
c−1
X

1(Uui −Lli >)
t

t

1(Uui −Lli >) (1Wt + 1Wtc )
t

t

1(Uui −Lli >) 1Wt + 2
t

t

X

t=1 i=1 a∈{1,2,...,K}

T X
c−1
X

1Wtc

t=1 i=1

1(a=lti )∨(a=uit ) 1(bi ∈Ia (t)) 1(β̃a (t)> 2 ) + 2

T X
c−1
X

1Wtc

t=1 i=1

(by Proposition 1)
We now split the first sum into two depending on whether an arm a belongs to the set A = {a ∈ {1, 2, ..., K} :

Katariya, Jain, Sengupta, Evans, Nowak

∆∗b < 2 /2}.
#samples(T ) ≤ 2

T X
c−1
X X

1(a=lti )∨(a=uit ) 1Na (t)< β(t,δ)  +
2 /2

a∈A t=1 i=1
T X
c−1
X X

2

1(a=lti )∨(a=uit ) 1(bi ∈Ia (t)) + 2

a∈Ac t=1 i=1

≤2

X β(T, δ)
2 /2

a∈A

2

T X
c−1
X

+2

T X
c−1
X X

1(a=lti )∨(a=uit ) 1

a∈Ac t=1 i=1

X T
X c−1
X

1Wtc

t=1 i=1

1(a=lti )∨(a=uit ) 1

a∈Ac t=1 i=1

|


Na (t)>

β(T ,δ)
∆∗ (a)
b


Na (t)≤

 + 2

β(T ,δ)
∆∗ (a)
b

T
X c−1
X

 +

1Wtc

t=1 i=1

{z

}

RT

∗
= 2H,b
β(T, δ) + RT

where
RT = 2

X T
X c−1
X

1(a=lti )∨(a=uit ) 1

a∈Ac t=1 i=1


Na (t)>

β(T ,δ)
∆∗ (a)
b



1(bi ∈Ia (t)) + 2

T
X c−1
X

1Wtc

t=1 i=1

∗
If we define S1∗ = min{x : 2H,b
β(x, δ) < x}, then we get that for S > S1∗ , the algorithm must have stopped
before S samples on the event (RT = 0). Denoting the total number of samples used by the algorithm by τ , we
have that, for any S > S1∗ , P(τ > S) ≤ P(RT 6= 0).

P(τ > S) ≤ P(RT 6= 0)




β(T, δ)
c
i
i
, bi ∈ Ia (t) + P(W c )
≤ P ∃ a ∈ A , t ≤ T, 1 ≤ i ≤ (c − 1) : a = lt ∨ a = rt , Na (t) >
∆∗b (a)




β(T, δ)
c
i
i
≤ P ∃ a ∈ A , t ≤ T, 1 ≤ i ≤ (c − 1) : a = lt ∨ a = rt , Na (t) >
,
b
∈
I
(t)
+ P(W c )
i
a
d∗ (pa , bi )

(13)

where the final inequality follows because ∆∗b (a) ≤ d∗ (pa , bi ) ∀ 1 ≤ i ≤ c − 1 (by Lemma 4).
Let us look at the first term:




β(T, δ)
P ∃ a ∈ Ac , t ≤ T, 1 ≤ i ≤ (c − 1) : a = lti ∨ a = rti , Na (t) >
,
b
∈
I
(t)
i
a
d∗ (pa , bi )




c−1 X
T
X X
β(T, δ)
≤
P a = lti ∨ a = rti , Na (t) >
,
b
∈
I
(t)
i
a
d∗ (pa , bi )
c i=1 t=1
a∈A

≤

c−1
X X
exp(−β(T, δ))

(by Lemma 3)

d∗ (pa , bi )

a∈Ac i=1

≤ (c − 1) exp(−β(T, δ))

1
∗ (p , b )
d
a i
c

X

a∈A

∗
≤ (c − 1)H,b
exp(−β(T, δ))

 ∗ 
S1
∗
≤ (c − 1)H,b
exp −β c−1
,δ
∗
= (c − 1)H,b
·

S∗

1
(if τ > S1∗ , T > c−1
))

δ(c − 1)α
1
∗,α
k1 KS1∗,α log k1 KS1 α
δ(c−1)

≤ (c − 1)

α+1

∗
H,b
·

k1 K
≤

δ
·
k1



c−1
2



∗ log
2H,b

δ
 k K(2H ∗ )α α
1

,b

δ

1
k1 KS1∗,α
log δ(c−1)
α

α
(since (c − 1) ≤ K and α > 1)

(by the lower bound in Corollary 1)

Adaptive Sampling for Coarse Ranking

For the second term, note that
P(W c ) ≤ 2eK

∞
X
(β(t, δ) log t + 1) exp(−β(t, δ))

(by Lemma 1)

t=1

≤

δ
k1



2e
4e
+
(α − 1)2
(α − 1)


(by Lemma 2)

Substituting in Eq. (13), we get that for S > S1∗ ,

α

δ
2e
c−1
4e
P(τ > S) ≤
+
+
≤δ
k1
2
(α − 1)2
(α − 1)
by the choice of k1 .
9.4

Lower Bound

The proof uses standard change of measure arguments used to prove lower bounds. For bandit problems, this is
succinctly expressed through Lemma 1 in Kaufmann et al. (2015) that we restate here for completeness.
Lemma 6. Let p and p0 be two bandit models with K arms such that for all a, the distributions pa and p0a are
mutually absolutely continuous. Let σ be a stopping time with respect to (Ft ) and let A ∈ Fσ . Then
K
X

Ep [Na (σ)]KL(pa , p0a ) ≥ d(Pp (A), Pp0 (A))

a=1

where d(x, y) = x log(x/y) + (1 − x) log((1 − x)/(1 − y)).
9.4.1

Proof of Theorem 3

Consider any arm a. By Assumption 1, there exists alternative model p0 such that:
KL(pa , pκg(a) +1 ) < KL(pa , p0a ) < KL(pa , pκg(a) +1 ) + α and p0a < pκg(a) +1
Note that in the model p0 , arm a no longer belongs to the cluster g(a). Let M̂g(a) be the set of arms returned
by an algorithm in the g(a)th cluster. If we define the event A = {a ∈ M̂g(a) } ∈ Fτ , then by definition, for any
δ-PAC algorithm, Pp (A) ≥ 1 − δ and Pp0 (A) ≤ δ. Letting Na (τ ) denote the number of pulls of arm a by time τ ,
we have by Lemma 6 and the monotonicity of d(x, y) that
1
)
KL(pa , p0a )Ep [Na (τ )] ≥ d(1 − δ, δ) ≥ log( 2.4δ
1
where we use the property that for x ∈ [0, 1], d(x, 1 − x) ≥ log 2.4x
. This gives us that


1
1
Ep [Na (τ )] ≥
log
KL(pa , pκg(a) +1 ) + α
2.4δ

Letting α → 0, we get
Ep [Na (τ )] ≥

1
log
KL(pa , pκg(a) +1 )



1
2.4δ


(14)

Similarly, by considering an alternative model p00 such that
KL(pa , pκg(a)−1 ) < KL(pa , p00a ) < KL(pa , pκg(a)−1 ) + α and p00a > pκg(a)−1
we get
1
Ep [Na (τ )] ≥
log
KL(pa , pκg(a)−1 )



1
2.4δ



From Eq. (14), Eq. (15), and the definition of ∆KL
κ (a) in Eq. (11), we get that


1
1
Ep [Na (τ )] ≥ KL
log
∆κ (a)
2.4δ
PK
Summing over all the arms yields the required bound for Ep [τ ] = a=1 Ep [Na (τ )].

(15)
