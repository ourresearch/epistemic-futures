---
title: "Curvature of Hypergraphs via Multi-Marginal Optimal Transport"
person: james-evans
section: by
type: journal-article
year: 2018
date: 2018-12-01
venue: ""
authors: "Shahab Asoodeh, Tingran Gao, James Evans"
source_url: https://doi.org/10.1109/cdc.2018.8619706
openalex_id: https://openalex.org/W2794577929
retrieved: 2026-08-13
content: full-text
notes: "full text via the OpenAlex Content API (content.openalex.org)"
---

# Curvature of Hypergraphs via Multi-Marginal Optimal Transport

## Full text

## Abstract

We introduce a novel definition of curvature for hypergraphs, a natural generalization of graphs, by introducing a multimarginal optimal transport problem for a naturally defined random walk on the hypergraph.This curvature, termed coarse scalar curvature, generalizes a recent definition of Ricci curvature for Markov chains on metric spaces by Ollivier [Journal of Functional Analysis 256 (2009) 810-864], and is related to the scalar curvature when the hypergraph arises naturally from a Riemannian manifold.We investigate basic properties of the coarse scalar curvature and obtain several bounds.Empirical experiments indicate that coarse scalar curvatures are capable of detecting "bridges" across connected components in hypergraphs, suggesting it is an appropriate generalization of curvature on simple graphs.

## I. INTRODUCTION

Complex systems or datasets are often modeled as weighted simple graphs in network science problems.While edges in these simple graphs qualitatively characterize similarity or adjacency relations among entities represented by the graph vertices, the edge weights are frequently used to quantify the nature of the interactions between pairs of nodes.Simple yet powerful as these simple graph models are, many recent work reported the importance of understanding higher-order interactions among more than a pair of nodes, rendering simple graphs insufficient as a natural model for capturing the network structure information in these practices.Applications of this type include spatial network [1], image tagging [2], image retrieval [3], cellular networks [4], and co-authorship network [5], to name just a few.Hypergraphs have been proposed as a replacement to tackle this difficulty.

Roughly speaking, a hypergraph H = (V, E) consists of a finite set V of vertices and a set of hyperedges E ⊆ 2 Vjust as edges in a simple graph that can be identified with vertex pairs, hyperedge E ∈ E are subsets of V .The ubiquitous influence in modeling complex networks fostered numerous recent developments in the theory and algorithms of hypergraphs, including extensive studies of the spectral and algebraic properties such as hypergraph Laplacian [6], hypergraph partitioning [7], Cheeger's inequality for hypergraph [8], and spectrum of hypergraphs [9].Among many tools developed for better understanding the geometry of graphs, the graph Ricci curvature [10]- [14] has attracted an increasing amount of interest in the past years.In his original work [10], Ollivier defined coarse Ricci curvature for metric measure spaces, including simple graphs and Markov chains as special cases.In a nutshell, the coarse Ricci curvature summarizes the behavior of shortest paths with close-by starting points and parallel initial directions: two such paths tend to get closer to each other in a metric space of positive Ricci curvature, and further if the space is negatively curved.On simple graphs, this notion of Ricci curvature has found applications ranging from bounding the chromatic number [15] and analyzing the Internet topology [16] to measuring the stability in financial networks [17], brain structural connectivity [18], and similarity of networks [19].

This paper proposes a novel definition of curvature for hypergraphs by generalizing Ollivier's coarse Ricci curvature through a multi-marginal optimal transport framework (see e.g.[20]- [22]).Analogous to coarse Ricci curvatures, our definition of hypergraph curvature is grounded upon differential geometric intuitions, and reduces to the graph Ricci curvature when the hypergraph is a simple graph.While the coarse Ricci curvature is defined for pairs of points, which are naturally identified with edges in simple graphs, we need to adjust the construction to account for ≥ 3 vertices joined by a hyperedge simultaneously; consequently, the geometric information captured in our definition is a summary of a small neighborhood enclosing all the end nodes of a hyperedge, as opposed to the directional information revealed by the Ricci curvature.In fact, our construction corresponds to the scalar curvature of Riemannian manifolds under appropriate manifold assumptions analogous to the manifold Ricci curvature example in [10].

The rest of the paper is structured as follows.We list a few useful notation in Section II-A.After a brief review of coarse Ricci curvature in Section II-B, we define coarse scalar curvature in Section II-C.Based on this definition, we then propose our notion of hypergraph curvature and investigate its properties in Section II-D.We derive a closed form for the curvature of complete uniform hypergraphs in Section III and a general lower bound for hyperpaths in Section IV.In Section V, we provide a detailed consistency result for the definition of coarse scalar curvature in a Riemannian manifold setting.Finally, we conclude the paper in Section VI.

## II. HYPERGRAPH CURVATURE VIA MULTI-MARGINAL OPTIMAL TRANSPORT A. Notations

For each vertex i of a hypergraph H = (V, E), we use d i := E∈E 1 {i∈E} to denote the degree of vertex i and d(E) := r∈V 1 {r∈E} to denote the cardinality of hyperedge E ∈ E. Similar to graph, we use N (i) for the neighbors of vertex i, i.e., N (i) = {j ∈ V : ∃E ∈ E, (i, j) ∈ E}.For a pair of vertices i and j of a hypergraph, d(i, j) denotes the shortest distance, i.e., d(i, j) = r if there exist r interesting hyperedges E 1 , . . ., E r , such that i ∈ E 1 , j ∈ E r , and

We will always denote M for a d-dimensional Riemannian manifold.We use exp x (•) : T x M → M to denote the exponential map.For any x ∈ M and v ∈ T x M with v = 1, we denote Ric x (v, v) for the Ricci curvature at x ∈ M in the direction of v ∈ T x M , defined as

where v, e 2 , • • • , e d constitutes an orthonormal basis for T x M , and R is the Riemannian curvature tensor.We will often write Ric (v, v) for Ric x (v, v) when the point x is fixed throughout the discussion.Averaging out Ric x (v, v) for v ranging in an orthonormal basis of T x M gives rise to the scalar curvature at x ∈ M :

where z 1 , • • • , z d constitutes an orthonormal basis for T x M .Equivalently, the scalar curvature can be obtained from averaging out the Ricci curvature over the unit sphere in the tangent plane, i.e. (c.f.[23, Exercise 4.9])

where S d-1 (0) is the unit sphere in T x M and ω d-1 is the volume of the standard (d -1)-dimensional sphere in R d .For any set A ∈ R n , we let P (A) denote the set of all probability measures defined on A.

## B. Graph Ricci Curvature

Given a graph G = (V, E) and a pair of vertices x, y ∈ V , Ollivier [10] defined the curvature of edge (x, y) ∈ E as

where d(x, y) is the shortest distance from x to y, m i is the uniform random walk starting at i ∈ V , and W (m x , m y ) is the Wasserstein distance between m x and m y given by

where Π(m x , m y ) is the set of all joint distributions having m x and m y as marginals (i.e., the set of all couplings of m x and m y ).He then showed that positive curvature is equivalent to the contraction of the random walk under Wasserstein's distance which in turn leads to the existence of a unique stationary distribution.

To justify that ( 4) is a valid discrete version of Ricci curvature, Ollivier argued as follows.In a d-dimensional Riemannian manifold (M, d M ), consider the random walk (c.f.Definition 1) dm ε

x for each x ∈ M and ε > 0 given by

where

where v ∈ T x M is a unit tangent vector at x such that exp x (δv) = y and where

In Riemannian geometry, Ricci curvature Ric x (v, v) is, up to a scaling factor, the average of the sectional curvatures of all two-dimensional subspaces of T x M passing through v [23, §4] and hence, it measures the coupling of the random walks.In this context, if the curvature of a point in a manifold is zero, it is locally on a Euclidean space, positive if it is locally on an sphere and negative if it locally on a hyperbolic space.

## C. Coarse Scalar Curvature for Metric Spaces

We begin our construction of coarse scalar curvature by defining random walks on a metric space, which was used in [10] to define coarse Ricci curvatures.Definition 1 ( [10] Definition 1).Let (M, d M ) be a Polish metric space equipped with its Borel σ-algebra.A random walk m on M is a family of probability measures {m

where W 1 (X n ) is the minimum of the multi-marginal optimal transport problem

with (A) # π being the push-forward of measure π under mapping A and

It must be mentioned that the multi-marginal optimal transport problem is first studied in Gangbo and Świe ¸ch [22] where they showed the necessary conditions for the existence and uniqueness of the optimizer when c(ξ

The coarse scalar curvature is closely tied to the multi-marginal optimal transport problem among n ≥ 2 probability measures m x1 , • • • , m xn , which is a direct generalization of the pairwise Wasserstein distance between measures.We will make frequent use of the following well-known facts in the theory of multi-marginal optimal transport problems (see e.g.[20]- [22], [24], [25] and the references therein):

Proposition 1 (Multi-marginal and barycenter [20]).The minimum of the multi-marginal optimal transport problem is equal to the minimum of the Wasserstein barycenter problem, i.e.

where the L 1 -Wasserstein distance W 1 (m, ν) for any m, ν ∈ P (M ) is defined in (8).

The minimization problem in (11) is called Wasserstein barycenter of X n .

Proposition 2 (Duality [25]).

where the supremum is taken over

We postpone the justification of our nomenclature of "scalar curvature" in Section V, under an appropriate manifold setting.Briefly speaking, at least when the hypergraph arises from a Riemannian manifold in a natural geometric construction, the coarse scalar curvature ( 9) is asymptotically lower bounded by the scalar curvature of the Riemannian manifold.

## D. Hypergraph Curvature

Let a hypergraph H = (V, E) with V = {1, 2, . . ., N } and a hyperedge E = {1, 2, . . ., n} be given.Inspired by coarse scalar curvature, we wish to define the curvature for each hyperedge E of H.To this goal, we first need to define random walk over hypergraphs.It is natural to define the (uniform) random walk started at vertex i ∈ V on H as the following: for each j ∈ V m i (j) = E∈E:(i,j)∈E

and hence we associate E with n probability measures m i ∈ P(V ), 1 ≤ i ≤ n.Replacing X n with {1, 2, . . ., n} in Definition 2 and defining c(x 1 , . . ., x n ) = min z∈V n i=1 d(x i , z), we can define a multi-marginal optimal transport problem associated with E ∈ E as W (E) := min π∈Π(m1,m2,...,mn)

where

Definition 3 (Hypergraph Curvature).The curvature of a hyperedge E = {1, 2, . . ., n} ∈ E is defined as

Hence, we have either c(x 1 , . . ., x n ) ≤ 3(n -1) or π(x 1 , . . ., x n ) = 0 for all π ∈ Π(m 1 , . . ., m n ).This then demonstrates that, similar to graph curvature, -2 ≤ κ(E) ≤ 1.

Specializing Propositions 1 and 2 to the hypergraph setting, we now provide two equivalent formulations for hypergraph curvature.Barycenter: Although the minimization problem in ( 14) is a linear program, its complexity is exponential in N .However, it turns out [26] that Wasserstein barycenter problem (11) can be solved quite efficiently.The equivalence between barycenter problem and multi-marginal optimal transport problem justifies to define the Wasserstein barycenter of hyperedge E as bar(E) := inf

Following mutatis mutandis Proposition 1, we have

The term barycenter makes sense by recalling that for the Euclidean space the barycenter of points {x i } n i=1 is given by arg min x n i=1 x ix 2 .Consequently, bar(E) is the barycenter of points {m i } n i=1 in the Wasserstein space (i.e., a metric space with Wasserstein distance).Duality Following mutatis mutandis Proposition 2, we can write the following dual formula for W (E)

where E ν [•] is the expectation operator with respect to measure ν and K is the set of all integrable real-valued functions on V such that for any vector

After defining hypergraph curvature, a natural question is whether or not this definition reduces to graph Ricci curvature (4) if the hypergraph is indeed a simple graph, i.e., the cardinality of each hyperedge is two.We answer this question in affirmative by invoking the barycenter interpretation.If H is in fact a graph and E is a hyperedge (i.e., n = 2 and thus E = {1, 2}), then bar(E) equals either m 1 or m 2 , because for any ν ∈ P(V ) the triangle inequality implies W (m 1 , ν) + W (m 2 , ν) ≥ W (m 1 , m 2 ).Thus, hypergraph curvature coincides with (4).

It is a well-known fact that Ollivier-Ricci curvature of edge (x, y) depends heavily on the number of common neighbors of x and y.Specifically, if N (x) ∩ N (y) = ∅, then κ(x, y) ≤ 0 (see e.g., [14]).We now prove a similar result for hypergraphs.

Theorem 1.For any hyperedge E with cardinality m, we have

Proof.Let again E be denoted by {1, 2, . . ., n}.The proof relies on the dual formula of W (E). In order to make use of ( 17), we need to find a set of functions {f j } n j=1 that satisfy the constraint (18).Fix two vertices υ and ϑ in E. Set f i ≡ 0 for i ∈ E\{ϑ, υ} and suppose

for all pairs of vertices (r, s).Then we have for any vector (x 1 , . . .,

Hence, the constraints f i ≡ 0 for i ∈ E\{ϑ, υ} and ( 19) are sufficient to satisfy (18).Letting C υ,ϑ denote the set of real-valued functions satisfying (19), we can write

where the last equality is due to [27, Theorem 1.14] and A is the set of all real-valued 1-Lipschitz functions f on V , that is

## Now consider the following function

Clearly, f ∈ A and therefore,

In light of this theorem, we have

If H happens to be a simple graph, then for every edge E = (υ, ϑ), we have m υ (N (υ) ∩ N (ϑ)) = ∆ dυ , where ∆ is the number of triangles supported on edge E. Hence, the bound (20) implies

which appears in [14,Theorem 4].Remark 1 (Curvature as a projection of Boltzmann).Cuturi [26] introduced an entropic regularized version of Wasserstein distance between two measures as

where ε > 0 is the regularization parameter, H(•) denotes the Shannon entropy function, K ε is the Boltzmann distribution defined as K ε (x, y) := e -d(x,y)/ε Z(ε)

and Z(ε) := (x,y)∈V ×V e -d(x,y)/ε .It follows that W (µ, ν) = lim ε↓0 W ε (µ, ν) [?].As mentioned in [26], despite the theoretically-guaranteed convergence, the procedure cannot work beyond a graph-dependent value ε 0 beyond which some entries of K ε are represented as zeroes in memory.Since H(•) is a strictly concave function, the optimization problem in (22) has a unique solution π * which corresponds to the projection of K ε onto Π(µ, ν).Following this spirit, we can define the entropic regularized Wasserstein barycenter problem as

where

is the unique projection of K ⊗n ε onto C. Assuming ε is sufficiently small, it follows that W (m 1 , . . ., m n ) is an approximation of this projection.

## III. COMPLETE UNIFORM HYPERGRAPHS

Graph Ricci curvature turns out to have a simple formula for complete graphs K N .In particular, it is shown [14] that κ(x, y) = N -2 N -1 for any edges (x, y) in K N .In this section, we show that complete uniform hypergraphs with N vertices have the same curvature as K N .

n-2 many hyperedges.Therefore, according to ( 13), the random walk started at

Lemma 1.For every hyperedge E of H n N , we have

In particular,

In light of this lemma, the curvature of complete n-uniform hypergraphs is independent of n.This is, in fact, a result of the normalization in Definition 3.

## Proof.

Again let E = {1, 2, . . ., n}.Notice that for H n M , we have d(r, s) = 1 for any distinct pair of vertices r, s ∈ V .Thus, we can write for a measure ν ∈ P(V )

where the last equality follows from [27, Exercise 1.17] and for two vectors a and b, a

## IV. EXAMPLES

In this section, we focus on the computation of hypergraph curvature in two examples to illustrate the differences and similarities with the graph curvature.The first example is a natural generalization of infinite path P n ; a simple graph that has n vertices with n -2 vertices of degree 2 and the other two of degree one.

Example 1.It is shown [28] that P n is one of the few graphs (among graphs with girth at least 5) with constant zero curvature.We now demonstrate in the following theorem that a similar statement does not hold for the hyperpath; a hypergraph whose vertices have degree at most 2. For the ease of presentation, we assume that any two intersecting hyperedges have exactly one common vertex; see Fig. 2.

Theorem 2. For any hyperedge E of a hyperpath described above, we have

,

In particular, the curvature of hyperedge E is bounded from below by

Proof Sketch.The proof relies on the simple observation that for the hyperedge E = {1, 2, . . ., n}, we have W (E) ≤ n i=1 W (m i , ν) for any probability measure ν ∈ P(V ).In particular,

Assuming that {1, 2, . . ., n -β} are vertices in E that are shared with other hyperedges and {nβ + 1, . . ., n} are isolated vertices inside E, we can employ a tedious (yet standard) linear-programming argument to show that

and

Plugging ( 25) and ( 26) into (24), we obtain the result.

In light of this result, we have κ(E) > 0 if only one vertex of E is shared, i.e., β > n -2.In other words, the leaves of a hyperpath have positive curvature which is different from graph curvature in that in simple graphs (with girth at least 5) each edge connecting to a leaf has zero curvature, see [28,Theorem 3.3].

Example 2. As a toy example, consider the hypergraph H = (V, E) with V = {1, 2, . . ., 13} and E = {E 1 , E 2 , E 3 , E 4 }, where E 1 = {1, 2, 3}, E 2 = {2, 4, . . ., 7}, E 3 = {6, . . ., 11}, and E 4 = {7, 11, 12, 13}, as illustrated in Fig. 2. Using (13), we can compute the probability measures associated to each hyperedge.For instance, the random walk started at vertex 2 is µ 2 = [0.25,0, 0.25, 0.125, 0.125, 0.125, 0.125, 0, . .., 0].Since there are only 13 vertices, we can solve the optimization problem (14) (as a linear program) for each hyperedge.Solving this optimization problem, we obtain W (E 1 ) = 1, W (E 2 ) = 2.38, W (E 3 ) = 2.08, and W (E 4 ) = 1.45.Consequently, it follows that κ(E 1 ) = 0.5, κ(E 2 ) = 0.4, κ(E 3 ) = 0.58, and κ(E 4 ) = 0.52.

Informally speaking, the hyperedge with the lowest curvature is the bridge connecting two components of hypergraphs.This is similar to the intuition of graph Ricci curvature, as experimentally observed in [29], that edges with negative curvature are locally shortcuts of two component of graph.Lemma 3. Assume M , ε > 0 satisfy the same assumptions as in Lemma 2. Let {X n } ∞ n=1 be a sequence of i.i.d.random points uniformly distributed in a geodesic ball B (x, ε) of radius ε > 0 centering at x ∈ M , and denote µ n for the Riemannian median of X 1 , • • • , X n for all n ∈ N. Then µ n → x a.s. as n → ∞, where x is the unique Riemannian median of the uniform distribution on B (x, ε).

Proof.The existence and uniqueness of µ n and x follows from Lemma 2; note here that x need not coincide with x in general, by the characterization of Riemannian medians established in [32, Proposition 2.1 and Theorem 2.2].The almost sure convergence has been established in [34,Corollary 4.1].

We now turn to investigating the coarse scalar curvature of hypergraphs generated from a geometric probabilistic model: saturated ε-neighborhood hypergraphs supported on a Riemannian manifold M , with vertices uniformly distributed on M .We consider the same random walk on the Riemannian manifold M as in [10], namely, the one given in (6): for any x ∈ M and ε > 0,

which is essentially the standard volume measure on M restricted and renormalized on B (x, ε).For simplicity of statement, let us denote xE for the Riemannian median -when it exists and is unique -of the vertices connected by a hyperedge E in a saturated hypergraph G = (V, E).

Theorem 3. Let M , ε > 0 be as assumed in Lemma 2. Let {v i } ∞ i=1 be a sequence of i.i.d.random points sampled uniformly on M with respect to the standard Riemannian volume measure.For any N ∈ N, let V N := {v i } N i=1 and H N = (V N , E N ) be an ε-neighborhood hypergraph supported on M .If there exists a hyperedge E N ∈ E N for each H n such that

) for all sufficiently large N ∈ N then the coarse scalar curvature of hyperedge E N satisfies, for all sufficiently small ε > 0, lim sup

Proof.Since curvature is a local quantity, we may assume without loss of generality that M is connected and even compact.Let ε > 0 be sufficiently small such that the geodesic ball B (x, ε) is geodesically convex neighborhood of x (c.f.[23, Proposition 4.2]).To ease notations, write ℓ N := |E N | and denote x 1 , • • • , x ℓN ∈ V N for the vertices of H N connected by the hyperedge E N ∈ E. By Proposition 1 and the definition of Riemannian median, we have

where the limit follows from the law of large number and the Lipschitz continuity of the function (see e.g.[32, §2])

We know from [10, Example 7] that, for any y ∈ B (x, ε),

where v x,y is a unit tangent vector in T xM such that

which, when plugged back into (30), gives lim sup

A straightforward calculation using geodesic normal coordinates reveals

Theorem 3 indicates that coarse scalar curvature asymptotically upper bounds the scalar curvature of the Riemannian manifold, when the hypergraph is constructed from uniformly sampling the manifold in a natural way.This justifies the nomenclature of "scalar curvature" in our definition.We conjecture that coarse scalar curvature also asymptotically lower bounds the scalar curvature in the same setting, but will have to leave that for future work.

## VI. CONCLUSION AND FUTURE WORK

In this paper, we propose a novel definition of curvature for hypergraphs by generalizing coarse Ricci curvature to coarse scalar curvature through multi-marginal optimal transport.Our definition is shown to be consistent with graph curvature in that (i) it reduces to graph curvature if the hypergraph of interest is indeed a simple graph, and (ii) it shares several properties with graph curvature.In particular, it is experimentally observed that, analogous to graph curvature, hypergraph curvature can be used to determine the bridge between components in the network.We are currently computing hypergraph curvature in real-world hypergraph networks (in particular co-authorship or cellular networks) to observe this centrality property of hypergraph curvature.We are also applying hypergraph curvature to characterize dynamic effects in large dynamic network (in particular, financial network).Intuitively, hypergraph curvature provides a computational method for detecting changes in dynamic networks, characterizing fast evolving network components, as well as identifying stable network region.On the theoretical side, we are interested in gaining better understandings of our hypergraph curvature with deeper insights from differential geometry.

## Fig. 1 .

Fig.1.A hyperpath with 42 vertices and 7 hyperedges.For the green hyperdge, we have m = 10 and β = 7.Note that, unlike path graph, hyperpath might have cycles.

## 1 E 2 E 3 E 4 Fig. 2 .

Fig. 2. The hypergraph studied in Example 2.

x,y , v x,y ) d M (x, y) dvol M (y) vol (B (x, ε)) (e i , e i )|2 for an arbitrary orthonormal basis e 1 , • • • , e d of T xM .Plugging (32) and (33) back into(31) to conclude that lim sup

[10,s the metric ball with radius ε centered at x and 1 {x∈A} is the indicator function of set A. It is then shown[10, Example 7]that for sufficiently small δ
