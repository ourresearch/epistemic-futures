---
title: "Wasserstein Soft Label Propagation on Hypergraphs: Algorithm and Generalization Error Bounds"
person: james-evans
section: by
type: journal-article
year: 2019
date: 2019-07-17
venue: "Proceedings of the AAAI Conference on Artificial Intelligence"
authors: "Tingran Gao, Shahab Asoodeh, Yi Huang, James Evans"
source_url: https://doi.org/10.1609/aaai.v33i01.33013630
openalex_id: https://openalex.org/W2962723373
retrieved: 2026-08-13
content: full-text
notes: "OpenAlex duplicates merged: W2962723373 W2889992667; full text extracted from the arXiv PDF; text taken from duplicate OpenAlex record W2889992667"
---

# Wasserstein Soft Label Propagation on Hypergraphs: Algorithm and Generalization Error Bounds

## Full text

1

Wasserstein Soft Label Propagation on Hypergraphs: Algorithm and
Generalization Error Bounds
Tingran Gao1 , Shahab Asoodeh2 , Yi Huang3 , and James Evans4

arXiv:1809.01833v2 [stat.ML] 16 Nov 2018

Abstract
Inspired by recent interests in developing machine learning and data mining algorithms for hypergraphs, here we investigate
the semi-supervised learning algorithm of propagating "soft labels" (e.g. probability distributions, class membership scores) over
hypergraphs, by means of optimal transportation. Borrowing insights from Wasserstein propagation on graphs [Solomon et al.
2014], we re-formulate the label propagation procedure as a message-passing algorithm, which renders itself naturally to a
generalization applicable to hypergraphs through Wasserstein barycenters. Furthermore, in a PAC learning framework, we provide
generalization error bounds for propagating one-dimensional distributions on graphs and hypergraphs using 2-Wasserstein distance,
by establishing the algorithmic stability of the proposed semi-supervised learning algorithm. These theoretical results also offer
novel insight and deeper understanding about Wasserstein propagation on graphs.

I. I NTRODUCTION
Recent decades have witnessed a growing interest in developing machine learning and data mining algorithms on hypergraphs
[ZHS07], [JM18], [BP09], [LR15], [LM17], [HSJR13], [HZY15]. As a natural generalization of graphs, a hypergraph is a
combinatorial structure consisting of vertices and hyperedges, where each hyperedge is allowed to connect any number of
vertices. This additional flexibility facilitates the capture of higher order interactions among objects; applications have been
found in many fields such as computer vision [Gov05], network clustering [DAC08], folksonomies [GZCN09], cellular networks
[KHT09], and community detection [KBG18].
This paper develops a probably approximately correct (PAC) learning framework for soft label propagation or Wasserstein
propagation [SRGB14], a recently proposed semi-supervised learning algorithm based on optimal transport [Vil03], [Vil08], on
graphs and hypergraphs. Distinct from the prototypical semi-supervised learning algorithm of label propagation [BMN04], in
which labels of interest are numerical or categorical variables, Wasserstein propagation aims at inferring unknown soft labels,
such as histograms or probability distributions, from known ones, based on pairwise similarities qualitatively characterized
by edge connectivity and quantitatively measured using Wasserstein distances. Compared with traditional “hard labels,” soft
labels are built with extra flexibility and informativeness, rendering themselves naturally to applications where uncertainty and
distributional information is crucial. For example, the traffic density at routers on the Internet network or topic distributions
across the co-authorship network are more naturally modeled as probability distributions.
Semi-supervised learning is a paradigm that leverages unlabelled data to improve the generalization performance for
supervised learning, under generic, unsupervised structural assumptions about the dataset (e.g. the manifold assumption);
see [See01], [Zhu08], [CSZ06] for an overview. Given a graph G = (V, E) and a subset of vertices V0 ⊂ V , label propagation
is a procedure for extending an assignment of labels on V0 , denoted as a map f0 : V0 → D valued in an arbitrary set D, to a
map f : V → D on the entire vertex set V . Borrowing an analogy from the classical heat equation, this extension procedure
is reminiscent of heat propagation from “boundary” V0 to the “entire domain” V . For soft label propagation, the label set D
is the probability distribution P (N ) modeled on a complete, separable metric space (N, dN ).
Among the first works to address semi-supervised learning with soft labels are [CJ05], [Tsu05], [SB11]. In all of these
works, the similarity between two soft labels is quantitatively measured using the Kullback-Leibler (KL) divergence, but the
soft labels inferred from this process are often unstable and discontinuous. In [SRGB14] the authors proposed to replace
KL divergence with 1- or 2-Wasserstein distance. The resulting soft label propagation algorithm is thus termed “Wasserstein
propagation.” Specifically, given a measure-valued map f0 : V0 → P (N ) defined on V0 ⊂ V , Wasserstein propagation extends
f0 to f : V → P (N ) by solving the variational problem
X
min
Wpp (f (v) , f (w))
(1)
f :V →P(N )

(v,w)∈E

subject to the constraint f  V0 = f0 . Here Wp (µ, ν) denotes the p-Wasserstein distance between probability distributions
µ, ν ∈ P (N ) defined as
Z Z
 p1
p
Wp (µ, ν) := inf
dN (x, y) dπ (x, y)
(2)
π∈Π(µ,ν)

N ×N

1 Department of Statistics, The University of Chicago, Chicago, IL 60637 tingrangao@galton.uchicago.edu
2 Computation Institute and Institute of Genomics and System Biology, The University of Chicago, Chicago, IL 60637 A@uchicago.edu
3 Department of Medicine, University of Chicago, Chicago IL, yhuang10@uchicago.edu
4 Computation Institute and Department of Sociology, The University of Chicago, Chicago, IL 60637 jevans@uchicago.edu

2

where Π (µ, ν) is the set of all probabilistic couplings on N × N with µ and ν as marginals. When p = 2, the minimizer of (1)
can be interpreted as a harmonic map, with boundary condition f  V0 = f0 that takes value in a weak, metric-measure space
sense [Ott01], [AGS05], [LV09], [Lav17]. Note that this is a nontrivial fact because harmonic maps (or minimizers of the
Dirichlet energy) generally only exist when the target metric space D has negative Alexandrov curvature [Jos94], but P (N )
equipped with the 2-Wasserstein distance has positive Alexandrov curvature [AGS05, §7.3]. When D is a one-dimensional
distribution on the real line defined by 2-Wasserstein distance, [SRGB14] related (1) to a Dirichlet problem.
In this work, we first extend the framework of [SRGB14] to hypergraphs using the Wasserstein barycenter [AC11], [AGE18].
For 2-Wasserstein distances this is equivalent to solving a multi-marginal optimal transport [CE10] problem with a naturally
constructed cost function. The hypergraph extension of Wasserstein propagation is based on a novel interpretation of the original
algorithm on graphs [SRGB14] as a message-passing algorithm. Next, we take a deeper look at the statistical learning aspects of
our proposed algorithm, and establish generalization error bounds for propagating one-dimensional distributions on graphs and
hypergraphs using the 2-Wasserstein distance. One dimensional distributions such as histograms are among the most frequent
applications for soft label propagation. The main technical ingredient is algorithmic stability [BE02]. To our knowledge, our
generalization bound is the first of its type in the literature on Wasserstein distance-based soft label propagation; on graphs
these results generalize the error bounds from [BMN04]. As no general semi-supervised learning algorithm is available for
large datasets [PWZSK17], this new connection between the Wasserstein barycenter and semi-supervised learning might be of
theoretical as well as computational interest.
In the last section, we provide promising numerical results for both synthetic and real data. In particular, we apply our
hypergraph soft label propagation algorithm to random uniform hypergraphs as well as UCI datasets including one on
Congressional voting records and another on mushroom characteristics, which are naturally represented using a hypergraph
representations.
A. Notation
We denote an undirected simple graph as G = (V, E) where V = [n] := {1, . . . , n} is the vertex set and E ∈ V × V denote
edges. We use L to denote the (weighted) graph Laplacian associated with (weighted) graph G, which is a real square matrix
of size n-by-n defined by L := D − W , where W ∈ Rn×n is the (weighted) adjacency matrix of G, and D ∈ Rn×n is a
diagonal matrix with the (weighted) degree of vertex j at its (j, j)-th entry. We use H = (V, E) to denote a hypergraph where
E ∈ 2V is the set of hyperedges of H. Given k ≥ 2 probability measures ρ1 , . . . , ρk in P(N ), their Wasserstein barycenter is
k


bar {ρi }ki=1 :=

1X 2
W2 (ρi , ν).
ν∈P(N ) k
i=1
inf

(3)

Fundamental properties of the minimizer in (3) are studied in [AC11]; similar results hold when thesquared 2-Wasserstein
|E|
distance are weighted differently. Given a hyperedge E of H, we use bar(E) to denote bar {µi }i=1 where the probability
measures µ1 , . . . , µ|E| associated with each vertex i in E are clear from the context.
II. M ESSAGE PASSING AND L ABEL P ROPAGATION ON G RAPHS AND H YPERGRAPHS
In this section, we formulate our hypergraph label propagation as a special case of belief propagation. To this end, we
begin with a brief description of a generalized version of Wasserstein label propagation [SRGB14] from a message passing
perspective.
A learning problem is specified by a probability distribution D on X×Y according to which labeled sample pairs zi = (xi , yi )
are drawn and presented to a learning algorithm. The algorithm then outputs a map from X to Y . In soft label propagation
problems, the maps of interest take values in a space of probability distributions Y . From now on, we assume Y is the space of
probability distributions on a complete metric space (N, dN ), i.e., Y = P (N ). Because N is complete, the space Y equipped
with Wasserstein distance is also a complete metric space [Vil03, Theorem 6.18].
A. Wasserstein Label Propagation on Graphs
Let X be a graph G = (V, E), possibly with weights ωij ≥ 0 on each edge (i, j). Wasserstein label propagation is an
extension of Tikhonov regularization framework on graphs [BMN04] from real-valued functions to measure-valued maps.
Denote a measure-valued map from G to P (N ) as µ : V → P (N ). For simplicity, write µi := µ (i) for i ∈ V . A prototypical
semi-supervised learning setting assumes µ1 , · · · , µm are known, where 1 ≤ m  n, and the goal is to determine µm+1 , · · · , µn
on the remaining vertices. We do so by minimizing the following objective function with Tikhonov regularization
m
X
1 X 2
W2 (µi , fi ) + γ
ωij W22 (fi , fj ) ,
f :V →P(N ) m
i=1

min

(i,j)∈E

(4)

3

where γ > 0 is a regularization parameter. This minimization problem can be conceived of as an extension of the Dirichlet
boundary problem studied in [SRGB14] as here we do not impose fi = µi for i ∈ [m]. The minimizer of (4) is the measurevalued map “learned” from the training data {(i, µi ) | 1 ≤ i ≤ n} and the given graph structure G = (V, E). We point out that
the formulation in [SRGB14] is a special case (parameter-free “interpolated regularization”) of (4) in the limit γ → 0, for the
same reason given in [BMN04, §2.2].
We now provide an algorithm for solving (4) based on belief propagation. Because this is only a motivating perspective, we
assume for simplicity that the graph is unweighted, but all arguments below can be extended to weighted graphs with heavier
notation. In this context, each vertex i updates its belief about the local minimizer of (4) fi by exchanging messages to edges
to which it is incident. The classical min-sum algorithm [MR09] describes this process as follows. At time t, vertex i ∈ [m]
(t)
(t)
has belief bi about the minimizer fi of (4); then, at time t + 1, i sends message Ji→e to edge e = (i, j) and receives message
(t)
Je→i from e, then updates the message for the next iteration according to
 




X
(t)
(t)
(t)
(t−1)
(t−1)
Ji→e bi
= W22 µi , bi
+
J(i,k)→i bi
(5)
k∈N (i)\{j}

and

 
(t)
(t)
Je→i bi
=

min

fj ∈P(N )

h



i
(t)
(t−1)
W22 bi , fj + Jj→e (fj ) .

(6)

The first term in (5) is set to zero if i ∈
/ [m]. The belief is then updated at time t + 1 according to evolution


X
(t+1)
(t)
:= arg min W2 (µi , fi ) +
bi
J(i,k)→i (fi ) .
fi

(t)

Convergence of bi
[MR09]).

k∈V :(i,k)∈E

to the true minimizer fi∗ can be guaranteed under mild conditions on initial beliefs if G is a tree (see e.g.,

B. Wasserstein Label Propagation on Hypergraphs
Now let X be represented by a hypergraph H = (V, E). Because each hyperedge may contain an arbitrary number of
vertices, the minimization (4) fails to formulate our learning objective. Nevertheless, belief propagation updates (5) and (6)
can naturally be extended passing the message between vertex i and hyperedge E containing i as
 




X
(t)
(t)
(t)
(t−1)
(t−1)
Ji→E bi
= W22 µi , bi
+
JE 0 →i bi
(7)
E 0 ∈E\{E}:i∈E 0

and

 
h
(t)
(t)
JE→i bi
= min bar(E) +
fE\{i}

X

i
(t−1)
Jk→E (fk ) .

(8)

k∈E\{i}

where fE\{i} = {fk ∈ P(N ) : k ∈ E\{i}}. The belief of vertex i ∈ [m] is then obtained according to the following rule:
"
#
X
(t+1)
(t)
bi
= arg min W22 (µi , fi ) +
JE→i (fi ) .
fi ∈P(N )

E∈E:i∈E

These belief propagation update rules justify the following formulation of label propagation for hypergraphs:
m

X
1 X 2
W2 (µi , fi ) + γ
bar(E)
f :V →P(N ) m
i=1
min

(9)

E∈E

which is a natural generalization of (4) when the graph is unweighted. For weighted graphs, (9) still holds with properly
adjusted bar(E) with weights.
III. BARYCENTER AND C LIQUE R EPRESENTATION
In this section, we assume that labels are one-dimensional probability distributions, i.e., N ⊂ R, and work solely with the
2-Wasserstein distance. We will see that in this case, hypergraph label propagation can be cast into a Wasserstein propagation on
a weighted graph arising from the clique representation of the hypergraph. The remainder of this paper focuses on establishing
generalization error bounds for graphs. The main advantage of one-dimensional soft labels is illustrated by the following
classical result in optimal transportation theory.
Theorem 1 ([Vil03]). Let µ, ν ∈ P(N ) with N ⊂ R with cumulative density functions (c.d.f.) Fµ and Fν , respectively. Then
Z 1
2
W22 (µ, ν) =
Fµ−1 (s) − Fν−1 (s) ds,
0

4

where Fµ−1 and Fν−1 are the generalized inverses of Fµ and Fν , respectively, i.e., Fµ−1 (s) := inf{x ∈ N : Fµ (x) > s}.
The explicit expression for Wasserstein distance enables us to derive the barycenter of any number of one-dimensional
distributions in a closed form.
Theorem 2 ([BGKL17]). Let ρ1 , . . . , ρk ∈ P(N ) be m probability distributions on N ⊂ R with cumulative density functions
Fρi , i ∈ [k]. Let ρb be the (unique) Wasserstein barycenter of {ρi }ki=1 . Then the generalized inverse c.d.f. Fb−1 of ρb is given
by
k
1 X −1
Fb−1 (s) =
F (s).
k i=1 ρi
Because the inverse cdfs and distributions are in one-to-one correspondence, this theorem characterizes the 2-Wasserstein
barycenter of {ρi }m
i=1 . In light of Theorem 2, one can simplify the barycenter of hyperedge E that contains vertices, such as
{1, 2, . . . , k} as
k

bar(E)

=

1X 2
W (µi , µb )
k i=1 2
Z 1

=

1X
k i=1
k

n

k
X

k
X

k

=

=

1
Fµ−1
(s) −
i

k
X

k i=1

0

1 X X
k 2 i=1 j=i+1

Z 1
0

!2
Fµ−1
(s)
i

ds

2
Fµ−1
(s) − Fµ−1
(s) ds
i
j

1
W 2 (µi , µj )
k 2 i=1 j=i+1 2

(10)

where the first and second equalities follow from Theorems 1 and 2, respectively. Comparing (10) with (9), we now have
Proposition 1. Soft label propagation with 2-Wasserstein distance for one-dimensional distributions on hypergraphs H using
(9) is equivalent to Wasserstein propagation on a weighted graph arising from the clique representation GH of H. The weight
of each edge e in GH depends only on the degrees of the hyperedges containing e.
Proof. Recall that the clique representation of a hypergraph H = (V, E) is a graph GH = (V, EH ), where EH = {(i, j) :
∃E ∈ E, {i, j} ⊂ E}. The rest of the proof follows from checking definitions.
IV. G ENERALIZATION B OUNDS FOR WASSERSTEIN P ROPAGATION
In this section we derive generalization bounds for label propagation (4) on graphs. The same results apply to hypergraphs,
by Proposition 1. We begin by briefly reviewing empirical risk, generalization error, and algorithmic stability in message
passing.
A. Algorithmic Stability
The framework of algorithmic stability [DW79], [BE02], [MNPR06] was proposed in statistical learning as an alternative to
the VC-dimension framework. The latter is often overly pessimistic because it attempts to bound the generalization performance
uniformly over all possible algorithms. We briefly recapture the essence of algorithmic stability here. Let X and Y be two
measurable spaces, and a set of training samples S = {zi = (xi , yi ) , i = 1, · · · , m} of size m sampled i.i.d. with respect to an
unknown joint distribution D on the product space Z = X × Y . A learning algorithm is a mechanism that maps S to a global
map fS : X → Y defined on the entire X. It is often assumed for simplicity that the algorithm is symmetric with respect to
training sets—that the learning algorithm should return identical maps for two training sets with samples differing from each
other only by permutation. We shall assume all maps considered here are measurable, and all measure spaces are separable.
We are interested in the case where X is a simple finite graph and Y is the probability space P (N ). The empirical risk or
empirical error of a mapping fS : X → Y learned from a training set S of size m > 0 is defined as
m

Rm (fS ) :=

1 X
c (fS , zi )
m i=1

where c (·, ·) : Y X × (X × Y ) → R≥0 is a cost function evaluating the predictive error of fS : X → Y at a point sampled
from the joint distribution D on X × Y . The generalization error of the learned map is
RD (fS ) = Ez∼D [c (fS , z)]

5

which measures the average prediction error for a map learned from training data. The central problem in the PAC learning
framework is bounding the discrepancy between Rm and RD . In [BE02], the authors proved that such a bound exists if the
algorithm satisfies a uniform stability property, essentially meaning that the learned mapping changes very little in terms of
predictive power if the training sample undergoes a small change.
Definition 1 (Uniform Stability, [BE02]). Fix a positive integer m ∈ Z+ . Let S = {z1 , · · · , zm } ⊂ X × Y be a training set,
and S 0 be another training set that contains the same elements as S with the only exception that the sample zi is replaced
m
with a different sample zi0 6= zi . A learning algorithm A : (X × Y ) → Y X that sends any training set S to a mapping
fS : X × Y is said to be (uniform) β-stable for some positive constant β > 0 if for any pair of training sets S, S 0 that differ
by exactly one element the following inequality holds:
|c (fS , z) − c (fS 0 , z)| ≤ β

∀z ∈ X × Y.

Theorem 3 ([BE02]). Let S 7→ fS be a β-stable learning algorithm, such that 0 ≤ c (fS , z) ≤ M for all z ∈ X × Y and all
learning set S. For any arbitrary  > 0 we have for all m ≥ 8M 2 /2
PS∼Dm {|Rm (fS ) − RD (fS )| > } ≤

64M mβ + 8M 2
,
m2

(11)

and for any m ≥ 1
PS∼Dm {|Rm (fS ) − RD (fS )| >  + β}
≤ 2 exp −

!

m2
2 (mβ + M )

2

.

(12)

Of course, the order of β in terms of training samples m will be crucial here, otherwise any learning algorithm is uniformly
stable for any bounded cost function. In [BE02] it was pointed out that a sufficient condition for these bounds to be tight is
β = O (1/m) as m → ∞. It was verified in [BE02] that the Tikhonov regularization framework for scalar-valued functions
with quadratic cost function satisfies this requirement; but Theorem 3 is indeed much more general and applicable to any
measurable spaces X and Y . The rest of this paper is devoted to establishing algorithmic stability for(hyper)graph soft label
propagation.
B. Generalization bounds for Soft Label Propagation
The goal of this subsection is to verify that the conditions of Theorem 3 are satisfied for the Tikhonov regularization
framework (4). The first task is to find an appropriate model class for the distributions in P (N ) that ensures uniform
boundedness of the cost function
c (f, (j, µj )) = W22 (fj , µj ) .
(13)
This can be fulfilled trivially, for instance, if the metric space (N, dN ) is of bounded diameter. This includes many generic
applications we come across in practice, in particular for propagating histograms but are not already satisfied with popular
distribution classes such as the Gaussian distribution. It is therefore preferable to work with a model class for distributions with
uniformly bounded pairwise Wasserstein distances under mild assumptions. By definition (2), bounding the Wassertein distance
from above can be achieved by plugging an arbitrary coupling into the variational energy functional defining (2). However,
explicitly constructing meaningful couplings is typically difficult. Many existing bounds explore the multiscale structure of
supports from the two distributions [Dav88], [Lei18], [SP18], but it is not clear how those technical conditions can be used as
model class specifications. Here we bypass this difficulty by leveraging the simple characterization of Wasserstein distances
between one-dimensional distributions using quantile functions.
According to Theorem 1, one can simplify (4) as
Z 1h X
m 
2
1
−1
Fµ−1
(s)
−
F
(s)
min
fi
i
m i=1
f :V →P(N ) 0
2 i
X 
+γ
Ff−1
(s) − Ff−1
(s)
ds.
i
j
(i,j)∈E

Because the inverse c.d.f.s and the distributions are in one-to-one correspondences, and all Fµ−1
are given, it suffices to solve
i
−1
for the Ff−1
’s
in
their
entirety
and
then
recover
each
probability
distribution
at
vertex
i
from
F
fi : [0, 1] → R. To simplify
i
−1
notation, we define Φ : V × [0, 1] → R as Φ (i, s) := Ffi (s) and denote Φs (i) := Φ (i, s) for all s ∈ [0, 1] and i ∈ V . For
each fixed s ∈ [0, 1], Φs can be viewed as a function defined on vertices from graph G. For simplicity, we identify each Φs

6

with a real column vector of length n = |V |. Then the regularization term in (4) can be written in terms of L, the weighted
graph Laplacian of G. Thus (4) transforms into
m Z
1 X 1 −1
2
min
Fµi (s) − Φs (i) ds
Φ:V ×[0,1]→R m
i=1 0
(14)
Z
1

Φ>
s LΦs ds.

+γ
0

The optimization problem (14) can be viewed as a linear combination of infinitely many Tikhonov regularization problems,
one for each s ∈ [0, 1] where each sub-problem is decoupled from others. Indeed, standard variational analysis shows that it
suffices to solve each subproblem individually, i.e., solve for each fixed s ∈ [0, 1]
m

minn

Φs ∈R

2
1 X −1
Fµi (s) − Φs (i) + γΦ>
s LΦs .
m i=1

(15)

Once all subproblems are solved, it is necessary to check compatibility across solutions {Φs : s ∈ [0, 1]}, i.e., for any fixed i ∈
V , the map s 7→ Φs (i) is indeed the inverse c.d.f. of a probability distribution. This compatibility will become straightforward
after we derive the closed-form solution for each subproblem (15); see Proposition 2 below.
>
The solutions for Tikhonov regularization problems (15) were known back in [BMN04]. Let 1 = (1, · · · , 1) ∈ Rn be a
column vector of all ones, and
>
T` = diag (t1 , · · · , t` , 0, · · · , 0) ∈ Rn
where ti is the multiplicity of vertex i ∈ V in the training set S (we assumed without loss of generality that the training
samples are the first ` vertices, for notational convenience), and
!>
X
X
−1
−1
ys =
Fµi (s) , · · · ,
Fµi (s) , 0, · · · , 0
∈ Rn
(16)
vi =1

vi =`

i.e., for 1 ≤ i ≤ `, the i-th entry of ys is the sum of the ti values of the inverse c.d.f.’s of i ∈ V . With this notation, it becomes
easy to write down the Euler-Lagrange equation of the optimization problem (15) as
(T` + mγL) Φ∗s = ys .

(17)

To solve this equation, note that the operator T` + mγL may not be invertible—in fact, neither T` nor L is invertible.
Nevertheless, assuming the graph is connected, the nullspace of L is one-dimensional and spanned precisely by the all-one
vector 1. This means that L will be invertible on the orthogonal complement of the one-dimensional subspace spanned by 1.
Furthermore, noting that


1
T` + L ,
(18)
T` + mγL = mγ
mγ
−1

by standard functional analysis (or [BMN04, Proof of Theorem 5]) we know that the perturbed operator L + (mγ) T` is
invertible on the orthogonal complement as well provided that mγ is sufficiently large. More precisely, invertibility holds for
γ≥

max {t1 , · · · , t` }
mλ1

where λ1 is the smallest non-zero eigenvalue of L, or the spectral gap of the (possibly weighted) connected graph G. This
observation, together with the invariance of the quadratic cost in (15) under global translations, allow us to preprocess the
input data by subtracting scalar
m
1
1 X −1
ȳs := 1> ys =
F (s)
(19)
m
m i=1 µi
from each Fµ−1
(s), applying the inverse of T` + mγL, and finally adding ȳs back to the obtained solution. More specifically,
i
we would like to solve the equivalent optimization problem
Φ∗s = arg min
Φs ∈Rn

m

2
1 X  −1
Fµi (s) − ȳs − (Φs (i) − ȳs )
m i=1

(20)

>

+ γ (Φs − ȳs 1) L (Φs − ȳs 1) ,
−1

which gives Φ∗s − ȳs 1 = (T` + mγL)

(ys − ȳs T` 1) . Therefore, the solution to (15) takes the form
Φ∗s = (T` + mγL)

−1

(ys − ȳs T` 1) + ȳs 1.

(21)

7

−1

We emphasize here that the notation (T` + mγL) alone does not make sense because the matrix T` + mγL may well be
−1
non-invertible; only the notation (T` + mγL) u for u ∈ Rn satisfying 1> u = 0 bears meaning.
Remark 1. Alternatively, one can derive a solution to (15) by directly applying the pseudo-inverse of T` + mγL to ys , i.e.,
†
setting Φ∗s := (T` + mγL) ys . This avoids the requirement that γ need not be too small, but leaves the algorithmic stability
∗
of the resulting solution Φs in question.
Now that we have obtained closed-form solutions (21) to subproblems (15) for each s ∈ [0, 1], it is imperative to guarantee
that the closed-form solutions {Φ∗s | 0 ≤ s ≤ 1} piece together and give rise to inverse c.d.f.’s at each vertex i ∈ V . This
requires that, for each i ∈ V , the map [0, 1] 3 s 7→ Φ∗s (i) ∈ R should be non-decreasing and right continuous. The right
continuity is obvious, because for each i ∈ V the map [0, 1] 3 s 7→ ys (i) is right continuous, and the linear combination of right
continuous functions is still right continuous, thus this assertion follows from the closed-form expression (21). Monotonicity
−1
would be guaranteed if there is a “maximum principle” for the operator T` + mγL, or equivalently L + (mγ) T , on the
n
graph G, i.e., if R 3 y ≥ 0 (entrywise) and (T` + mγL) Φ = y then Φ ≥ 0 (entrywise). This is because we already have
ys − yt ≥ 0 for any 0 ≤ t ≤ s ≤ 1 by the monotonicity of the inverse c.d.f.’s, hence such a “maximum principle” would
guarantee Φs − Φt ≥ 0 (entrywise). Such maximum principles abound for graph Laplacians, see e.g., [HS97], [CCK07]. It is
−1
natural to expect such a maximum principle to hold for L + (mγ) T as well, since T is a non-negative.
Lemma 1 (Maximum Principle). If Φ ∈ Rn is such that [(T` + mγL) Φ] (i) ≥ 0 for all 1 ≤ i ≤ ` and [(T` + mγL) Φ] (i) = 0
for all ` + 1 ≤ i ≤ n, then Φ attains both its maximum and minimum over i = 1, · · · , n within {1, · · · , `}. In particular,
Φ (i) ≥ 0 for all 1 ≤ i ≤ n.
Proof. The conditions on Φ can be written as


X
ti
+ deg (i) Φ (i) −
Φ (j) ≥ 0
mγ
j:j∼i
X
deg (i) Φ (i) −
Φ (j) = 0

1≤i≤`

(22)

`+1≤i≤n

(23)

j:j∼i

where deg (i) ≥ 1 is the degree of vertex i in graph G. First, we assert that the minimum of Φ must be attained among the
vertices 1, · · · , `, for otherwise, if ` + 1 ≤ i∗ = arg mini∈V Φ (i) ≤ n, then by (23) we have
X
deg (i∗ ) Φ (i∗ ) =
Φ (j)
j:j∼i∗

≥

X

Φ (i∗ ) = deg (i∗ ) Φ (i∗ )

j:j∼i∗

which implies Φ (j) = Φ (i∗ ) for all vertices j ∼ i∗ . This argument can be repeated until the constant value propagates into
the vertices within 1, · · · , `, and the assertion follows from the connectivity of the graph. The assertion for the maximum can
be established analogously. Next we argue that the minimum of Φ on the vertices of G must be non-negative. Assume the
contracy, i.e. the minimum attained at i∗ ∈ [1, `] is strictly negative, then by (22) we have


X
ti∗
0≤
+ deg (i∗ ) Φ (i∗ ) −
Φ (j)
mγ
j:j∼i∗
X
ti
[Φ (i∗ ) − Φ (j)] < 0
= ∗ Φ (i∗ ) +
mγ
j:j∼i
∗

where the strict inequalty follows from the counter-assumption Φ (i∗ ) < 0. This contradiction completes our proof that Φ ≥ 0
on the entire graph G.
This lemma then implies the promised monotonicity.
Proposition 2. For any vertex i ∈ V , the closed-form solutions (21) is non-decreasing with respect to s ∈ [0, 1].
Proof. By the equivalence of (20) and (15), solutions Φs satisfy the Euler-Lagrange equations for (15):
(T` + mγL) Φ∗s = ys .
For any 0 ≤ t ≤ s ≤ 1, subtracting two Euler-Lagrange equations yields
(T` + mγL) (Φ∗s − Φ∗t ) = ys − yt ≥ 0
where the inequality follows from the definition of ys in (16). Furthermore, it is straightforward to see that ys − yt satisfies
the assumption in Lemma 1, which then implies Φ∗s ≥ Φ∗t .

8

We can now rest assured that the solutions (21) constitute an inverse c.d.f. at each vertex i ∈ V . But there is more: it can be
easily verified that (20) is equivalent to the Tikhonov regularization problem formulated in [BMN04] if we view (Φs − ȳs 1) as
variables. We can thus follow the idea of [BMN04, Theorem 5] to get algorithmic stability for each individual Φs , s ∈ [0, 1].
Theorem 4. Assume m ≥ 4 and 0 < T := max {t1 , · · · , t` } < ∞ satisfies mγλ1 − T > 0, where λ is the regularization
parameter in (15) and λ1 is the spectral gap of the connected graph G. Let S = {(vi , µi ) | 1 ≤ i ≤ m, vi ∈ V, µi ∈ P (R)}
and S 0 = {(vi0 , µ0i ) | 1 ≤ i ≤ m, vi ∈ V, µi ∈ P (R)} be two training sets that differ from each other by exactly one data
sample. Assume further that, for a fixed s ∈ [0, 1] there holds
o
n
−1
,
i
=
1,
·
·
·
,
m
≤ Ms < ∞.
(24)
F
(s)
max Fµ−1
(s)
,
0
µ
i
i

0
Let Φ∗s , Φ0∗
s be solutions of (15) for S and S , respectively,
−1

Φ∗s = (T` + mγL)

(ys − ȳs T` 1) + ȳs 1
−1
0∗
0
Φs = (T` + mγL) (ys0 − ȳs0 T`0 1) + ȳs0 1
where T`0 , ys0 , ȳs0 are defined analogously to T` , ys , ȳs but with respect to S 0 instead of S. Then
√
3Ms T m
4Ms
2Ms
∗
0∗
kΦs − Φs k∞ ≤
2 + mγλ − T + m .
1
(mγλ1 − T )

(25)

Proof. Following the same argument as in the proof of [BMN04, Theorem 5], we can assume without loss of generality that
0
S, S 0 differ by a new point (vm , µm ) ↔ (vm
, µ0m ); the other case where only the multiplicities differ can be treated similarly.
By our assumption (24), the two averages differ by at most an amount of
|ȳs − ȳs0 | ≤

2Ms
.
m

For simplicity, introduce temporary notations
A := T` + mγL,

B := T`0 + mγL.

Using the simple fact that the 2-norm dominate the ∞-norm, we have
∗
0∗
kΦ∗s − Φ0∗
s k∞ ≤ kΦs − Φs k2
2Ms
≤
+ A−1 (ys − ȳs T` 1) − B −1 (y0 s − ȳs0 T`0 1) 2
m
2Ms
+ A−1 (ys − ȳs T` 1) − A−1 (y0 s − ȳs0 T`0 1) 2
≤
m
+ A−1 (y0 s − ȳs0 T`0 1) − B −1 (y0 s − ȳs0 T`0 1) 2 .
−1

Standard functional analysis argument (the same perturbation reasoning we gave in (18)) tells us that A−1 2 ≤ (mγλ1 − T )
Together with the observation that

.

k(ys − ȳs T` 1) − (y0 s − ȳs0 T`0 1)k2
≤ kys − ys0 k2 + kȳs T` 1 − ȳs0 T`0 1k2
2Ms
< 4Ms
≤ 2Ms +
m
we have
A−1 (ys − ȳs T` 1) − A−1 (y0 s − ȳs0 T`0 1) 2 ≤
−1

4Ms
.
mγλ1 − T

In the meanwhile, noting that we also have B −1 2 ≤ (mγλ1 − T ) , and kA − Bk2 = kT`0 − T` k2 ≤
conclude that
A−1 (y0 s − ȳs0 T`0 1) − B −1 (y0 s − ȳs0 T`0 1) 2
√
3Ms T m
= B −1 (B − A) A−1 (y0 s − ȳs0 T`0 1) 2 ≤
2.
(mγλ1 − T )

√

2 < 3/2, we

Putting everything together completes the proof.
The boundedness assumption on Φs seems artificial, but is actually natural: an almost identical argument as the first part
of the proof of Lemma 1, with minimum replaced with maximum and mutatis mutandis, establishes that the global maximum
of Φs must be attained at the boundary 1 ≤ i ≤ `. Hence, because there are only finitely many data in the training set, this
boundedness is a mild requirement (e.g., satisfied if each Fµ−1
(s) is finite). We define a model class to reflect the requirement
i

9

that the inverse c.d.f.’s of one-dimensional probability distributions in the training set should be controlled. We define the model
class in Definition 2 and summarize the maximum principle argument as a lemma on a priori estimates for future convenience.
Definition 2 (Dominated Quantile Class). Let φ ∈ L2 [0, 1] and φ ≥ 0 on [0, 1]. A probability distribution µ ∈ P (R) is said
to belong to dominated quantile class M2φ if Fµ−1 (s) ≤ φ (s) for e.g., s ∈ [0, 1].
Lemma 2 (A Priori Estimates). If in the training set S = {(vi , µi ) | 1 ≤ i ≤ m, vi ∈ V, µi ∈ P (R)} all µi lie in a dominated
quantile model class M2φ for some φ ∈ L2 [0, 1] with φ ≥ 0 on [0, 1], then any map f : V → P (R) minimizing (4) takes
values in M2φ as well.

(s) , i = 1, · · ·
Proof. By the equivalence between (4) and (14), it suffices to show the following fact: for each fixed s ∈ [0, 1], if max Fµ−1
i
φ (s) then kΦ∗s k∞ ≤ φ (s), where Φ∗s is defined in (20). But this follows straightforwardly from the maximum principle.
We now present the main theoretical result of this paper. In our setting these results apply to graphs as well as hypergraphs
by Proposition 1.
Proposition 3 (Algorithmic Stability for Soft Label Propagation of One-Dimensional Distributions). Assume m ≥ 4 and
0 < T := max {t1 , · · · , t` } < ∞ satisfying mγλ1 − T > 0, where γ is the regularization parameter in (15) and λ1 is the
spectral gap of the weighted, connected graph G. If the joint distribution D ∈ P (V × P (R)) is supported on V × M2φ for a
quantile model class M2φ ⊂ P (R) for some φ ∈ L2 [0, 1] with φ ≥ 0 on [0, 1], then the solutions of (4) or (9) are β-stable
in the sense of Definition 1 with respect to cost function (13), where
#
"
√
4
2
3 Tm
2
(26)
β = 4 kφk2
2 + mγλ − T + m .
1
(mγλ1 − T )
Proof. Let (j, θj ) be a new sample drawn from the joint distribution D. Then θj ∈ M2φ with probability 1. Let S, S 0 be two
training samples with values in M2φ and differ by exactly one data point. By Theorem 4 we have
|Φ∗s (j) − Φ0∗
s (j)|
#
"
√
2
3 Tm
4
≤
2 + mγλ − T + m φ (s) .
1
(mγλ1 − T )

(27)

By (10), the difference between the squared Wasserstein losses satisfy
|c (fS , (j, θj )) − c (fS 0 , (j, θj ))|
= W22 (fS (j) , θj ) − W22 (fS 0 (j) , θj )
Z 1
Z 1
2
2
−1
−1
∗
Φ0∗
Φs (j) − Fθj (s) ds −
=
s (j) − Fθj (s) ds
0
0
Z 1 

−1
∗
0∗
≤
Φ∗s (j) + Φ0∗
s (j) − 2Fθj (s) (Φs (j) − Φs (j)) ds
0
"
# Z
√
1
(∗)
3 Tm
4
2
≤
+
+
·
4φ (s) · φ (s) ds
2
mγλ1 − T
m
(mγλ1 − T )
0
"
#
√
3 Tm
4
2
2
= 4 kφk2
2 + mγλ − T + m = β,
1
(mγλ1 − T )
where at (∗) we used (27) to bound the difference |Φ∗s (j) − Φ0∗
s (j)|, and invoked Lemma 2 to conclude that
Φ∗s (j) , Φ0∗
s (j) ≤ φ (s)
and hence
−1
Φ∗s (j) + Φ0∗
s (j) − 2Fθj (s) ≤ 4φ (s) .
2

Note that the cost function is uniformly bounded by M = 4 kφk2 in our setting. Our main result follows from combining
Proposition 3 and Theorem 3.
Theorem 5 (Generalization Error for Soft Label Propagation for One-Dimensional Distributions). Under the same assumptions
as Proposition 3, for any  > 0 we have for all m ≥ 8M 2 /2
PS∼Dm {|Rm (fS ) − RD (fS )| > } ≤

64M mβ + 8M 2
,
m2

(28)

10

and for any m ≥ 1
PS∼Dm {|Rm (fS ) − RD (fS )| >  + β}
!
m2
≤ 2 exp −
,
2
2 (mβ + M )

(29)

2

where M = 4 kφk2 and β given by (26).
V. N UMERICAL E XPERIMENTS
A. Label Propagation Algorithm
Alg. 1 details the label propagation algorithm we use to obtain the results in the next two sections.
Algorithm 1: Alternating label propagation algorithm
Data: hypergraph H = (V, E); a subset of vertices V0 with known labels ¯l(v), ∀v ∈ V0 ; parameters α, γ > 0, a condition
EC for exiting the main loop on line 19.
Result: labels l(v), ∀v ∈ V .
1 Randomly initialize labels l(v), ∀v ∈ V
2 for every E ∈ E do
3
for every v ∈ E do
4
if v ∈ V0 then
5
WE (v) = α
6
else
7
WE (v) = 1
8
end
9
end
10 end
11 for every v ∈ V do
12
for every E ∈ E incident to v do
13
wv (E) = 1/|E|
14
end
15
if every v ∈ V0 then
16
append vector Wv with γ
17
end
18 end
19 while EC is not met do
20
Initialize loss = 0
21
for every E ∈ E do
22
LE = (l(v))v∈E
23
l(E) = Barycenter (WE , LE )
24
end
25
for every v ∈ V do
26
Lv = (l(E))E incident to v
27
if v ∈ V0 then
28
append Lv with ¯l(v)
29
end
30
l(v) = Barycenter (Wv , Lv )
31
for every E ∈ E incident to v do
32
loss = loss + Wv (E) · WassDist(l(v), l(E))
33
end
34
if v ∈ V0 then

35
loss = loss + γ · WassDist l(v), ¯l(v)
36
end
37
end
38 end
The functions Barycenter and WassDist can be any algorithms that calculate the weighted Wasserstein barycenter of a
vector of labels L with weights W , and the Wasserstein distance between two input labels, respectively. Note that we introduce

11

another parameter α > 1 to adjust the weights of vertices with known labels (in line 5) in order to increase their influences to
hyperedge barycenters. Similar techniques are explored in [SOZ17], [SOZ18].
The algorithm relies on the alternating technique in minimizing (9) in each iteration. This technique consists of two steps:
(i) first calculates the barycenters bar(E) of all hyperedges E using the current labels of vertices they contain and treats the
derived barycenters as the labels of the hyperedges (lines 21 to 24), and (ii) then calculates the barycenters, i.e. the new labels,
of all vertices using labels of the hyperedges incident to them, together with their targeted labels if the latter are known (line
25 to 37). Due to the alternating nature of the algorithm, we call it alternating label propagation.
B. Stochastic Block Model
In the first two experiments, we run label propagation on 3-uniform hypergraphs generated using the stochastic block
model (SBM) over 100 vertices that are grouped into either 2 or 3 blocks. More specifically, the probability that a hyperedge
{vi , vj , vr } exists is p = 0.01 if all vi , vj , and vr belong to the same block and is q = 0.002 otherwise.
We set the soft labels to be b-dimensional Gaussian distributions, where b is the number of blocks. For any vertex from block
i, i = 1, . . . , b, whose label is known, we set the mean of its label to be ei , where ei is the base vector with the i-th coordinate
being 1 and the rest being 0. The covariance matrix of each known label is set to be 0.05Ib , where Ib is the b-dimensional
identity matrix. The predicted block assignment of a vertex is the arg max of its predicted mean. In both of the experiments,
we use α = 20 and γ = 10. We run the experiments with 5 to 15 vertices of known block assignment from each block, and
the error bars are obtained by averaging over 20 random selections of vertices with known labels.
We compare the performance of our label propagation approach with with AdaBoost, random forest, and SVM in Fig. 1.
We use incidence matrix as the feature matrix in AdaBoost, Random forest, and SVM to solve the classification problem.

(a) SBM with 2 blocks

(b) SBM with 3 block

Fig. 1. Comparison of traditional classification algorithms with hypergraph label propagation on SBM.

SBM with two blocks: The hypergraph generated for this experiment has two blocks of sizes 50 and 50, and 629 hyperedges
with 388 of them containing vertices from one block.
SBM with three blocks: The hypergraph generated for this experiment has three blocks of sizes 33, 33, and 34, and 384
hyperedges with 182 of them has vertices from one block.
C. UCI datasets
In the next two experiments, we apply our label propagation as a classification algorithm to the following two datasets with
categorical features from the UCI machine learning repository:
Congressional Voting Records: This dataset contains voting records on 16 issues of the 2nd session of the 98th Congress.
We form a pair of hyperedges for each issue each of which contains voters who voted "Yay" and "Nay", respectively. For
voters whose votes were missing, we don’t include them in any of the hyperedges constructed for the corresponding issue. This
resilience to the missing data samples illustrates another advantage of applying hypergraph label propagation to classification
problems. We test label propagation algorithm with 5, 10, 15, 20, 25, and 30 congressmen and women from each party whose
affiliation are given.
Mushrooms: This dataset contains 22 features (e.g., shapes, colors, and habitats, etc) of 8124 mushrooms. We form 97 hyperedges each of which contains mushrooms sharing identical features. We choose 1000 edible and 1000 poisonous mushrooms
to run the experiment. We run the algorithm in 6 cases where 10, 20, 30, 40, 50, and 60 mushrooms are given labels from
each category.
In both datasets, the soft labels are either 1-dimensional Gaussian distributions N (+1, 0.01) and N (−1, 0.01) or 2-dimensional
Gaussian distributions N ((1, 0), 0.01I2 ) and N ((0, 1), 0.01I2 ) depending on which class the labelled sample belongs to. The

12

predicted class of a vertex is obtained as follows: For the 1-dimensional case, it is the sign of the mean of its label and for the
2-dimensional case, it is +1 if the first coordinate of the mean vector of its label is larger than the second coordinate and −1
otherwise. For both experiments, we set α = 10 and γ = 1. The error bars are obtained by averaging 20 random selections of
vertices with known labels. We compare the performance of hypergraph label propagation (as a classification algorithm) with
SVM in Fig. 2.

(a) Congressional voting records

(b) Mushrooms

Fig. 2. Comparison of SVM with hypergraph label propagation as a classification algorithm.

D. Discussion of numerical experiments
The above experiments demonstrate that the hypergraph label propagation can serve as a powerful alternative classification
algorithm especially when the dataset is structured as a network (for example as in SBM). The reason as to why the traditional
classification algorithms may fail on network-like datasets (as illustrated in Fig. 1) is because for these datasets almost all
coordinates of a feature vector tend to be identical except for few of them. We can understand these features as describing
only local properties of the dataset. Therefore, they can give rise to global characterizations of the datasets, in a substantial
way, only when properly “patched” together. Label propagation algorithm provides a novel way of combining features which
is shown in Fig. 1 to outperform the classical algorithms.
VI. C ONCLUSION
In this paper, we proposed a novel framework for a semi-supervised learning problem where (i) the labels are given by
probability measures on a metric space (“soft labels”) and (ii) the underlying similarity structure is given by a hypergraph,
which subsumes graphs and simplicial complexes. Our framework was inspired by a re-formulation of graph-based label
propagation in terms of message passing and borrowed ideas from the theory of multi-marginal optimal transport. We then
established generalization error bounds for propagating one-dimensional distributions using 2-Wasserstein distances. To the best
of our knowledge, this constitutes the first generalization error bounds for Wasserstein distance based soft label propagation,
even on graphs. We expect similar generalization bounds to hold for propagating higher-dimensional probability distributions
as well as using other Wasserstein distances, but a deeper understanding of the geometry underlying Wasserstein spaces will
be indispensable for those purposes. Future work includes (i) generalization of our results to higher-dimensional probability
measures, (ii) investigating the scalability and efficiency of our message-passing algorithm, and (iii) experimental study of our
framework on real-work networks that can be naturally represented by hypergraphs.
R EFERENCES
[AC11]
[AGE18]
[AGS05]
[BE02]
[BGKL17]
[BMN04]
[BP09]
[CCK07]

M. Agueh and G. Carlier. Barycenters in the wasserstein space. SIAM Journal on Mathematical Analysis, 43(2):904–924, 2011.
S. Asoodeh, T. Gao, and J. Evans. Curvature of hypergraphs via multi-marginal optimal transport. In The 57th IEEE Conference on Decision
and Control (CDC 2018), 2018.
L. Ambrosio, N. Gigli, and G. Savare. Gradient Flows: In Metric Spaces and in the Space of Probability Measures. Lectures in Mathematics.
ETH Zürich. Birkhäuser Basel, 2005.
O. Bousquet and A. Elisseeff. Stability and generalization. J. Mach. Learn. Res., 2:499–526, March 2002.
J. Bigot, R. Gouet, T. Klein, and A. López. Geodesic PCA in the wasserstein space by convex PCA. Ann. Inst. H. Poincaré Probab. Statist.,
53(1):1–26, 02 2017.
Mikhail Belkin, Irina Matveeva, and Partha Niyogi. Regularization and Semi-Supervised Learning on Large Graphs. In International Conference
on Computational Learning Theory, pages 624–638. Springer, 2004.
S. R. Bulò and M. Pelillo. A game-theoretic approach to hypergraph clustering. In Advances in Neural Information Processing Systems 22,
pages 1571–1579, 2009.
Soon-Yeong Chung, Yun-Sung Chung, and Jong-Ho Kim. Diffusion and Elastic Equations on Networks. Publications of the Research Institute
for Mathematical Sciences, 43(3):699–725, sep 2007.

13

[CE10]
[CJ05]

G. Carlier and I. Ekeland. Matching for Teams. Economic Theory, 42(2):397–418, 2010.
A. Corduneanu and T. S. Jaakkola. Distributed information regularization on graphs. In Advances in Neural Information Processing Systems,
pages 297–304. MIT Press, 2005.
[CSZ06]
O. Chapelle, B. Schölkopf, and A. Zien. Semi-supervised Learning. Adaptive computation and machine learning. MIT Press, 2006.
[DAC08]
E. Demir, C. Aykanat, and B. B. Cambazoglu. Clustering spatial networks for aggregate query processing: A hypergraph approach. Information
Systems, 33(1):1–17, 2008.
[Dav88]
Guy David. Morceaux de Graphes Lipschitziens et Intégrales Singulières sur une Surface. Revista Matemática Iberoamericana, 4(1):73–114,
apr 1988.
[DW79]
L. Devroye and T. Wagner. Distribution-free performance bounds for potential function rules. IEEE Transactions on Information Theory,
25(5):601–604, sep 1979.
[Gov05]
V. M. Govindu. A tensor decomposition for geometric grouping and segmentation. In 2005 IEEE Computer Society Conference on Computer
Vision and Pattern Recognition (CVPR’05), volume 1, pages 1150–1157 vol. 1, June 2005.
[GZCN09] Gourab Ghoshal, Vinko Zlatić, Guido Caldarelli, and MEJ Newman. Random hypergraphs and their applications. Physical Review E,
79(6):066118, 2009.
[HS97]
Ilkka Holopainen and Paolo M. Soardi. $p$-Harmonic Functions on Graphs and Manifolds. Manuscripta Mathematica, 94(1):95–110, dec 1997.
[HSJR13]
M. Hein, S. Setzer, L. Jost, and S. S. Rangapuram. The total variation on hypergraphs - learning on hypergraphs revisited. In Advances in
Neural Information Processing Systems, pages 2427–2435, 2013.
[HZY15]
Jin Huang, Rui Zhang, and Jeffrey Xu Yu. Scalable hypergraph learning and processing. In Proc. of IEEE Int. Conf. on Data Mining (ICDM),
pages 775–780, 2015.
[JM18]
J. Jost and R. Mulas. Hypergraph laplace operators for chemical reaction networks, 2018.
[Jos94]
J. Jost. Equilibrium maps between metric spaces. Calculus of Variations and Partial Differential Equations, 2(2):173–204, May 1994.
[KBG18]
Chiheon Kim, Afonso S Bandeira, and Michel X Goemans. Stochastic block model for hypergraphs: Statistical limits and a semidefinite
programming approach. arXiv preprint arXiv:1807.02884, 2018.
[KHT09]
Steffen Klamt, Utz-Uwe Haus, and Fabian Theis. Hypergraphs and cellular networks. PLoS computational biology, 5(5):e1000385, 2009.
[Lav17]
H. Lavenant. Harmonic mappings valued in the wasserstein space, 2017.
[Lei18]
Jing Lei. Convergence and Concentration of Empirical Measures under Wasserstein Distance in Unbounded Functional Spaces. arxiv preprint,
apr 2018.
[LM17]
P. Li and O. Milenkovic. Inhomogeneous hypergraph clustering with applications. In Advances in Neural Information Processing Systems 30,
pages 2308–2318, 2017.
[LR15]
X. Li and K. Ramchandran. An active learning framework using sparse-graph codes for sparse polynomials and graph sketching. In Advances
in Neural Information Processing Systems 28, pages 2170–2178, 2015.
[LV09]
John Lott and Cédric Villani. Ricci Curvature for Metric-Measure Spaces via Optimal Transport. Annals of Mathematics, pages 903–991, 2009.
[MNPR06] Sayan Mukherjee, Partha Niyogi, Tomaso Poggio, and Ryan Rifkin. Learning theory: stability is sufficient for generalization and necessary and
sufficient for consistency of empirical risk minimization. Advances in Computational Mathematics, 25(1):161–193, Jul 2006.
[MR09]
C. C. Moallemi and B. Van Roy. Convergence of min-sum message passing for quadratic optimization. IEEE Trans. Inf. Theory, 55(5):2413–2423,
May 2009.
[Ott01]
Felix Otto. The Geometry of Dissipative Evolution Equations: the Porous Medium Equation. Communications in Partial Differential Equations,
26(1-2):101–174, 2001.
[PWZSK17] L. Petegrosso, Z. Li W. Zhang, Y. Saad, and R. Kuang. Low rank label propagation for semi-supervised learning with 1000 millions samples.
arxiv preprint, Feb. 2017.
[SB11]
A. Subramanya and J. Bilmes. Semi-supervised learning with measure propagation. Journal of Machine Learning Research, 12:3311–3370,
Nov. 2011.
[See01]
Matthias Seeger. Learning with labeled and unlabeled data. Technical report, University of Edinburgh, 2001.
[SOZ17]
Zuoqiang Shi, Stanley Osher, and Wei Zhu. Weighted nonlocal laplacian on interpolation from sparse data. Journal of Scientific Computing,
73(2-3):1164–1177, 2017.
[SOZ18]
Zuoqiang Shi, Stanley Osher, and Wei Zhu. Generalization of the weighted nonlocal laplacian in low dimensional manifold model. Journal of
Scientific Computing, 75(2):638–656, 2018.
[SP18]
Shashank Singh and Barnabás Póczos. Minimax Distribution Estimation in Wasserstein Distance. arxiv preprint, feb 2018.
[SRGB14] J. Solomon, R. M. Rustamov, L. Guibas, and A. Butscher. Wasserstein propagation for semi-supervised learning. In Proceedings of the 31st
International Conference on International Conference on Machine Learning - Volume 32, ICML’14, pages 306–314, 2014.
[Tsu05]
Koji Tsuda. Propagating distributions on a hypergraph by dual information regularization. In Proceedings of the 22Nd International Conference
on Machine Learning, pages 920–927, 2005.
[Vil03]
C. Villani. Topics in Optimal Transportation. Graduate studies in mathematics. American Mathematical Society, 2003.
[Vil08]
Cédric Villani. Optimal transport: old and new, volume 338. Springer Science & Business Media, 2008.
[ZHS07]
D. Zhou, Jiayuan H., and B. Schölkopf. Learning with hypergraphs: Clustering, classification, and embedding. In Advances in Neural Information
Processing Systems 19, pages 1601–1608. MIT Press, 2007.
[Zhu08]
Xiaojin Zhu. Semi-Supervised Learning Literature Survey. Technical report, University of Wisconsin-Madison, 2008.
