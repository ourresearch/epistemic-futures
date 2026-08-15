---
title: "Learning Causal Effects on Hypergraphs"
person: brent-hecht
attendance: unconfirmed
section: by
type: conference-paper
year: 2022
date: 2022-08-12
venue: "Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining"
authors: "Jing Ma, Mengting Wan, Longqi Yang, Jundong Li, Brent Hecht, Jaime Teevan"
source_url: https://doi.org/10.1145/3534678.3539299
fulltext_url: https://arxiv.org/pdf/2207.04049
openalex_id: W4290943920
doi: https://doi.org/10.1145/3534678.3539299
oa_status: hybrid
cited_by_count: 65
retrieved: 2026-08-13
content: full-text
notes: "OpenAlex duplicate/preprint records: https://openalex.org/W4385763773 (conference-paper, 2023); https://openalex.org/W4285070145 (preprint, 2022); Full text retrieved from the open-access PDF at https://arxiv.org/pdf/2207.04049 (pdftotext; PDF not stored); full text is the arXiv preprint version of this work"
---

# Learning Causal Effects on Hypergraphs

## Full text

arXiv:2207.04049v1 [cs.LG] 7 Jul 2022

Learning Causal Effects on Hypergraphs
Jing Ma

Mengting Wan

Longqi Yang

University of Virginia
Charlottesville, VA, USA
jm3mr@virginia.edu

Microsoft
Redmond, WA, USA
mengting.wan@microsoft.com

Microsoft
Redmond, WA, USA
longqi.yang@microsoft.com

Jundong Li

Brent Hecht

Jaime Teevan

University of Virginia
Charlottesville, VA, USA
jundong@virginia.edu

Microsoft
Redmond, WA, USA
brent.hecht@microsoft.com

Microsoft
Redmond, WA, USA
teevan@microsoft.com
𝑢2

ABSTRACT
Hypergraphs provide an effective abstraction for modeling multiway group interactions among nodes, where each hyperedge can
connect any number of nodes. Different from most existing studies which leverage statistical dependencies, we study hypergraphs
from the perspective of causality. Specifically, in this paper, we
focus on the problem of individual treatment effect (ITE) estimation on hypergraphs, aiming to estimate how much an intervention
(e.g., wearing face covering) would causally affect an outcome (e.g.,
COVID-19 infection) of each individual node. Existing works on ITE
estimation either assume that the outcome on one individual should
not be influenced by the treatment assignments on other individuals
(i.e., no interference), or assume the interference only exists between
pairs of connected individuals in an ordinary graph. We argue that
these assumptions can be unrealistic on real-world hypergraphs,
where higher-order interference can affect the ultimate ITE estimations due to the presence of group interactions. In this work,
we investigate high-order interference modeling, and propose a
new causality learning framework powered by hypergraph neural
networks. Extensive experiments on real-world hypergraphs verify
the superiority of our framework over existing baselines.

CCS CONCEPTS
• Mathematics of computing → Causal networks; Hypergraphs;
• Information systems → Social networks.

KEYWORDS
Causal Inference; Graph Mining; Hypergraph; Interference
ACM Reference Format:
Jing Ma, Mengting Wan, Longqi Yang, Jundong Li, Brent Hecht, and Jaime
Teevan. 2022. Learning Causal Effects on Hypergraphs. In Proceedings of
the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining
(KDD ’22), August 14–18, 2022, Washington, DC, USA. ACM, New York, NY,
USA, 11 pages. https://doi.org/10.1145/3534678.3539299

1

INTRODUCTION

Group interactions among individuals exist in a wide range of scenarios, e.g., massive gathering events, day-to-day group chats on
This work is licensed under a Creative Commons Attribution
International 4.0 License.
KDD ’22, August 14–18, 2022, Washington, DC, USA
© 2022 Copyright held by the owner/author(s).
ACM ISBN 978-1-4503-9385-0/22/08.
https://doi.org/10.1145/3534678.3539299

𝑢5

𝑢1

𝑢5

𝑢2
𝑢1

𝑢3

𝑢4

𝑢3
(a) Hypergraph
2
3

5

(b) Ordinary graph
4,5

2,4

1
4

2,3

1

1
3,4

1st-order

𝑢4

2nd-order

2,3,4

3rd-order

(c) First, second, and third-order interferences with 𝑢 1 .

Figure 1: (a) An illustrative example of group interactions
on a hypergraph, where each circle represents a hyperedge
(group); (b) An ordinary graph projected from this hypergraph; (c) Illustration of interferences with 𝑢 1 from its neighbors on the hypergraph. Note interference on (b) is pairwise
(first-order only) while higher-order interference exists on
the original hypergraph (a).
WhatsApp or WeChat, and workplace interactions on Microsoft
Teams or Slack channels. Although the conventional pairwise graph
definition covers a vast number of applications (e.g., person-toperson physical contact networks or social networks [10]), it fails
to capture the complete information of these group interactions
(where each interaction may involve more than two individuals)
[5, 13, 44]. The notion of the hypergraph can thus be introduced to
address this limitation. Consider a hypergraph example that individuals are connected via in-person social events, each gathering
event can be represented as a hyperedge (Fig. 1a). Each hyperedge
can connect an arbitrary number of individuals, in contrast to an
ordinary edge which connects exactly two nodes (Fig. 1b).
While many studies have been devoted to utilizing such a generalized hypergraph structure to facilitate machine learning tasks
[5, 13, 44, 52], the majority were still executed at the statistical
correlation level, e.g., predicting the COVID-19 infection risk on
each individual (node) by capturing the correlations between one’s
demographic information (node features), in-person group gathering history (hypergraph structure) and the infection outcomes
(node labels). A critical limitation here is the lack of causality, which

KDD ’22, August 14–18, 2022, Washington, DC, USA

is particularly important for understanding the impact of a policy
intervention (e.g., wearing face covering) on an outcome of interest
(e.g., COVID-19 infection). For individuals connected as in Fig. 1a,
one may ask “how would each individual’s face covering practice
(treatment) causally influence their infection risk (outcome)?” Such
a causal inference task requires constructing the counterfactual
state of the same individual by holding all other possible factors
constant except the treatment variable of interest. This is a particularly hard problem on hypergraph data, since the outcome of each
individual is not only affected by their own confounding factors
(e.g., one’s health conditions and vaccine status) but also interfered
by other individuals on the hypergraph (e.g., face covering practice of other individuals who may physically contact the target
individual through a gathering event).
In this paper, we focus on learning causal effects on hypergraphs.
We are specifically interested in estimating the individual treatment
effect (ITE) under hypergraph interference from observational data.
Our study is motivated by the following gaps: (i) Empirical constraints of randomized experiments. One of the most reliable approaches for treatment effect estimation is randomized controlled
trials (RCTs). Nevertheless, running RCTs is often expensive, impractical, even unethical [15], and they are especially difficult on
graphs due to the dependencies among connected nodes [39]. (ii)
High-order interference on hypergraphs. Our work focuses on the
problem of ITE estimation, which aims to estimate the causal effect
of a certain treatment (e.g., face covering practice) on an outcome
(e.g., COVID-19 infection) for each individual. The classic ITE estimation is based on the Stable Unit Treatment Value (SUTVA) assumption [14, 36] that there is no interference [20, 37] (i.e., spillover
effect) among instances (also referred to as units in causal inference
literature). That means the outcomes for any instance are not influenced by the treatment assignment of other instances. This assumption can be impractical in the real-world, thus resulting in flawed
causal effect estimations, especially on graphs where the interference among instances are ubiquitous [1, 47, 50]. There have been
many efforts addressing this problem [3, 6, 21, 25, 28, 37, 39, 49],
but most assume the interference only exists in a pairwise way on
ordinary graphs (as shown in Fig. 1b). This pairwise interference
notion is insufficient to characterize the high-order interference
that exists on hypergraphs. As shown in Fig. 1c, within a gathering event (hyperedge) between 𝑢 1 , 𝑢 2 and 𝑢 3 , an individual’s (𝑢 1 )
infection outcome can be affected by the first-order interference
from other individuals (𝑢 2 → 𝑢 1 and 𝑢 3 → 𝑢 1 ) as well as the highorder interference from the interactions among other individuals
(the interaction between 𝑢 2 and 𝑢 3 may also act on influencing the
exposure of the virus to 𝑢 1 ; consequently, 𝑢 1 ’s infection risk can be
affected by this second-order interaction effect, i.e., 𝑢 2 × 𝑢 3 → 𝑢 1 ).
Notice that the number of such high-order interference items grows
combinatorially as the size of a hyperedge increases, leading to a
significant information gap between the original hypergraph and
the projected pairwise ordinary graph (which accounts for the
first-order interference only). This demands techniques capable of
modeling high-order interference, but to the best of our knowledge,
very little work has been done in this area.
In this paper, we propose a novel framework— Causal Inference
under Spillover Effects in Hypergraphs (HyperSCI )—to model
high-order interference. At a high-level, this framework controls

Jing Ma et al.

for the confounders and models high-order interference based on
representation learning, then estimates the outcomes based on
the learned representations. More specifically: (i) Controlling for
Confounders. Our framework is based on the widely accepted unconfoundedness assumption [33], i.e., the confounders are contained in
the observed features. With this assumption, we leverage representation learning techniques to capture and control for confounders
from the features of each individual. Note as shown in previous
works [34], the discrepancy between confounder distributions in
the treatment group and the control group can lead to biases in
causal effect estimations. Therefore, we also propose to use a representation balancing technique to mitigate the discrepancy between these two distributions. (ii) Modeling High-order Interference.
Modeling high-order relationships can be challenging due to the
complexity of enumerating multi-way interactions among nodes
within each hyperedge. Historically, one may need to simplify the
original hypergraph and approximate it through a series of projected ordinary graphs [48]. This obstacle is fortunately unblocked
by the recent advances of hypergraph neural networks [5, 44]. We
extend this line of techniques to model interference by learning
interference representations for each node. To learn the interference representations, the learned confounder representations and
the treatment assignment are propagated via hypergraph convolution and attention operations. (iii) Outcome Prediction. Based on
the learned representations of confounders and interference, we
predict the potential outcomes corresponding to different treatment
assignments for each individual. Overall, the main contributions of
this work can be summarized as follows:
• We formalize the problem of ITE estimation under high-order
interference on hypergraphs. To the best of our knowledge, it is
the first work for this problem.
• We propose a novel framework HyperSCI for the studied problem. HyperSCI models confounders and high-order interference
via representation learning and hypergraph neural networks.
• We validate the effectiveness of the proposed framework through
extensive experiments and provide in-depth analysis on how it
acts on different nodes and hyperedges.

2

PROBLEM DEFINITION AND ANALYSIS

We provide the formal problem definition and a brief theoretical
analysis of our studied problem in this section. A notation table is
provided in Appendix A.
Definition 2.1. Suppose a set of individuals V = {𝑣𝑖 }𝑛𝑖=1 are
connected via hyperedges E = {e𝑘 }𝑚
, together these form a hy𝑘=1
pergraph H = {V, E} with 𝑛 nodes and 𝑚 hyperedges, where each
hyperedge can connect an arbitrary number of nodes.
The observational data on this hypergraph can be denoted as
{X, H, T, Y}, where X = {x𝑖 }𝑛𝑖=1 , T = {𝑡𝑖 }𝑛𝑖=1 and Y = {𝑦𝑖 }𝑛𝑖=1 represent node features, treatment assignments, and observed outcomes,
respectively. H = {ℎ𝑖,𝑒 } ∈ R𝑛×𝑚 is an incidence matrix which
describes the hypergraph structure of H . ℎ𝑖,𝑒 = 1 if node 𝑖 is in
hyperedge 𝑒, otherwise ℎ𝑖,𝑒 = 0. For ease of discussion, we consider
the treatment assignment for each node as a binary variable in this
study (i.e., 𝑡𝑖 ∈ {0, 1}), but our work can be extended to non-binary
categorical variables and continuous variables.

Learning Causal Effects on Hypergraphs

KDD ’22, August 14–18, 2022, Washington, DC, USA

Definition 2.2. The potential outcome [33] of the instance 𝑖
(denoted by 𝑦𝑖1 or 𝑦𝑖0 ) is defined as the realized value of outcome
for instance 𝑖 under the treatment value 𝑡𝑖 = 1 or 𝑡𝑖 = 0. These
potential outcomes can be instantiated via a transformation 𝑌𝑖𝑇𝑖 =
Φ𝑌 (𝑇𝑖 , 𝑋𝑖 ,𝑇−𝑖 , 𝑋 −𝑖 , 𝐻 ). Φ𝑌 can be regarded as a (non-deterministic)
function to output potential outcomes, which takes each node’s treatment assignment, node features, the information (treatment assignments and node features) of other nodes on the hypergraph, and
the hypergraph structure as input1 , i.e., 𝑦𝑖𝑡𝑖 = Φ𝑌 (𝑡𝑖 , x𝑖 , T−𝑖 , X−𝑖 , H),
where the subscript −𝑖 denotes all other nodes on H except 𝑖.

We use 𝐻, 𝑋,𝑇 to denote the random variables for the hypergraph
structure, features, and treatment assignment for any node. Then
our first assumption can be formalized as below.
Assumption 1. (Expressiveness of summary function) For any node
𝑖, any values of 𝐻, 𝑋 −𝑖 , and 𝑇−𝑖 , if the output of summary function
o𝑖 is determined, then the value of the potential outcomes 𝑦𝑖1 and 𝑦𝑖0
with feature x𝑖 are also determined.

Given the above preliminaries, we are ready to provide the formal
definition of individual treatment effect on hypergraphs.

Our second assumption extends the unconfoundedness assumption [33] to the hypergraph interference setting. That is we assume
conditioned on the above summary function, the observed features
can capture all possible confounders.

Definition 2.3. For each node 𝑖 on the hypergraph H , the individual treatment effect (ITE) is defined by the difference between
potential outcomes corresponding to 𝑡𝑖 = 1 and 𝑡𝑖 = 0:

Assumption 2. (Unconfoundedness) For any node 𝑖, given the node
features, the potential outcomes are independent with the treatment
assignment and summary of neighbors, i.e., 𝑌𝑖1, 𝑌𝑖0 ⊥
⊥ 𝑇𝑖 , 𝑂𝑖 |𝑋𝑖 .

𝜏 (x𝑖 , T−𝑖 , X−𝑖 , H) = E[𝑌𝑖1 − 𝑌𝑖0 |𝑋𝑖 = x𝑖 ,𝑇−𝑖 = T−𝑖 , 𝑋 −𝑖 = X−𝑖 , 𝐻 = H]
= E[Φ𝑌 (1, x𝑖 , T−𝑖 , X−𝑖 , H) − Φ𝑌 (0, x𝑖 , T−𝑖 , X−𝑖 , H)].
(1)

Based on the above assumptions, the identification of the expectation of potential outcomes 𝑌𝑖1 and 𝑌𝑖0 can be proved (here we take
𝑌𝑖1 as an example):

We clarify that the ITE in this paper is actually defined in the
form of conditional average treatment effect (CATE), similar as
[17, 28]. The expectation is taken over the potential outcome (output of Φ𝑌 ) of the instances with same node features x𝑖 and “environmental information” (hypergraph structure H, other nodes’
features X−𝑖 and treatments T−𝑖 ). The distribution of the output
of Φ𝑌 is equivalent to the conditional distribution of the potential
outcome conditioned on the parameters in Φ𝑌 with fixed values.
For notation simplicity, we also denote 𝜏𝑖 = 𝜏 (x𝑖 , T−𝑖 , X−𝑖 , H) in
this paper. Meanwhile, we introduce the notion of spillover effect
in this work to assess the level of interference on hypergraphs.
Definition 2.4. The spillover effect of node 𝑖 under its treatment
𝑡𝑖 and other nodes’ treatment assignment T−𝑖 on the hypergraph H
is defined as:
𝛿𝑖 = E[Φ𝑌 (𝑡𝑖 , x𝑖 , T−𝑖 , X−𝑖 , H) − Φ𝑌 (𝑡𝑖 , x𝑖 , 0, X−𝑖 , H)].

(2)

In this paper, given the observed data {X, H, T, Y}, we aim to
estimate the ITE defined in Eq. 1 for each node in H with the
existence of high-order interference defined in Eq. 2.

2.1

Theoretical Analysis

With the above definitions, we show that the ITE can be identifiable
from the observational data under the following two assumptions.
Similar as the assumptions in other works of causal inference
under network interference [28], for each individual, we assume
there exists a summary function capable of characterizing all the
“environmental” information related to this node on the hypergraph.
Suppose there is a summary function SMR(·): for each node 𝑖, SMR(·)
takes the hypergraph structure H, the treatment assignment of other
nodes T−𝑖 and the features of these nodes X−𝑖 as input, then maps
them into a vector o𝑖 :
o𝑖 = SMR(H, T−𝑖 , X−𝑖 ).

(3)

1 In this paper, we use non-bold, italicized, and capitalized letters (e.g., 𝑋 ) to denote
𝑖
random variables; non-bold lowercase letters (e.g., 𝑡𝑖 ) to denote observed values of
a scalar; bold lowercase letters (e.g., x𝑖 ) to denote observed values of a vector; bold

capitalized letters (e.g., X) to denote observed values of a matrix or a set.

E[𝑌𝑖1 |𝑇𝑖 = 1, 𝑋𝑖 = x𝑖 ,𝑇−𝑖 = T−𝑖 , 𝑋 −𝑖 = X−𝑖 , 𝐻 = H]

(4)

=E[Φ𝑌 (𝑇𝑖 = 1, 𝑋𝑖 = x𝑖 ,𝑇−𝑖 = T−𝑖 , 𝑋 −𝑖 = X−𝑖 , 𝐻 = H)]

(5)

(𝑎)
(𝑏)

=E[Φ𝑌 (𝑇𝑖 = 1, 𝑋𝑖 = x𝑖 , 𝑂𝑖 = o𝑖 )]

(6)

(𝑐)

=E[Φ𝑌 (𝑇𝑖 = 1, 𝑋𝑖 = x𝑖 , 𝑂𝑖 = o𝑖 )|𝑋𝑖 = x𝑖 ]

(7)

(𝑑)

=E[Φ𝑌 (𝑇𝑖 = 1, 𝑋𝑖 = x𝑖 , 𝑂𝑖 = o𝑖 )|𝑋𝑖 = x𝑖 ,𝑇𝑖 = 1, 𝑂𝑖 = o𝑖 ]

(8)

(𝑒)

=E[𝑌𝑖 |𝑋𝑖 = x𝑖 ,𝑇𝑖 = 1, 𝑂𝑖 = o𝑖 ].

(9)

Here, the equation (𝑎) is based on the definition of potential
outcome in this setting; (𝑏) is inferred from Assumption (1); (𝑐) is
a straightforward derivation; (𝑑) is based on Assumption (2); and
(𝑒) is based on the widely used consistency assumption [33]. Based
on the above proof for the identification of potential outcomes, the
identification of ITE can be straightforwardly derived.

3

THE PROPOSED FRAMEWORK

Inspired by the previous theoretical analysis, we propose a novel
framework HyperSCI to address the studied problem. This framework contains three components: confounder representation learning, interference modeling, and outcome prediction. Holistically, we
aim to learn an expressive transformation to summarize high-order
interferences (Assumption 1), then take the interference representation, the confounder representation as well as the treatment assignment to estimate the expected potential outcome (Assumption 2).
The illustration of HyperSCI is shown in Fig. 2.

3.1

Confounder Representation Learning

We first encode the node features x𝑖 into a latent space via a multilayer perceptron (MLP) module, i.e., z𝑖 = MLP(x𝑖 ). This results in a
set of representations Z = {z𝑖 }𝑛𝑖=1 , which is expected to capture all
potential confounders, so the model can mitigate the confounding
biases by controlling for the learned representation z𝑖 .

KDD ’22, August 14–18, 2022, Washington, DC, USA

%"
P

%#
% "%# ×
×

P

×

Jing Ma et al.

Confounder Representation Learning
Confounder Representation Learning
!#
%#
%%
!#
%# % MLPMLP
%%
!%
%

×

%%
%
%$ $
%"
%"

P

P%
%$ $

!%
!
!$ $
!
!" "

Interference Modeling
Interference Modeling
!#
Hypergraph
!!"# × Hypergraph
module
!
%
!"
! module

×

P

P

!$

Representation balancing

Representation balancing

%

×'

×

P!$

#
# '(
(

P

Outcome Prediction

$#

$#
$%
$%
$$
$$
$
$" "

Representation balancing

Outcome Prediction

'&

P Node (treated)
(treated)
# P Node
(control)
× Node
'
&
#
(control)
× NodeHyperedge

Hyperedge
Node features

&
Concat (!) , $) ) '

+

'& +

Concat (!) , $) )

Representation balancing

Node features
Confounder
Confounder
representation
representation

Interference

Interference
representation
representation

Figure 2: An illustration of the proposed framework HyperSCI, which includes three key components: confounder representation learning, interference modeling, and outcome prediction.
Hypergraph
module
Hypergraph
module

!$ !$
!" "
!# !#
× ×
!
!
P
P!" !"
&
&
"
"
!" !"
P P !$ !$
Hypergraph
Hypergraph
(),,"(),,"
× ×
!% !%
$# $#
P P
P P
!# Convolution
!# Convolution
!# !# Attention
Attention
×
P P
×
× × !
Interference
Interference
# !#
#(),,#
!% !% representation
!&# (!),,
× ×
representation
× ×!% !
&#
P
%
!$ ! P
× ×
Hyperedge
$
P !P$ !
Hyperedge
P!
!!# !#

$P !

$ representation
representation

$

(𝑙 )

Figure 3: A detailed illustration of the hypergraph module
in the interference modeling component of HyperSCI. Here
we use the node 𝑣 1 (highlighted in yellow) as an example.
Representation Balancing. Note a discrepancy may exist between
the distributions of confounder representation Z in the treatment
group and the control group, incurring biases in causal effect estimation, as shown in [34, 46]. To minimize this discrepancy, we leverage
the representation balancing technique by adding a discrepancy
penalty to the loss function, where this discrepancy penalty can
be calculated with any distribution distance metrics. In our implementation, we use the Wasserstein-1 distance [34] between the
representation distributions of treatment group and control group.

3.2

Interference Modeling

In this interference modeling component, we take the confounder
representation (Z), the treatment assignment (T), and the relational
information on the hypergraph (H = {ℎ𝑖,𝑒 }) as input, to capture
the high-order interference for each individual. More specifically,
we learn a transformation function Ψ(·) through a hypergraph
module to generate the interference representations (p𝑖 ) for each
node 𝑖, i.e., p𝑖 = Ψ(Z, H, T−𝑖 , 𝑡𝑖 ). As shown in Fig. 3, this module is
implemented with a hypergraph convolutional network [5, 44] and
a hypergraph attention mechanism [5, 11, 52], where the convolutional operator forms the skeleton of interference from hyperedges,
and the attention operator enhances this mechanism by allowing
flexible node contributions to each hyperedge.
Learning interference representations. To learn the representations which encode the interference in the hypergraph for each
node, we propagate the treatment assignment and confounder representations with a hypergraph convoluntional layer. We first introduce a vanilla Laplacian matrix for the hypergraph H :
L = D−1/2 HB−1 H⊤ D−1/2 .

Then we can define the hypergraph convolution operator as:
$# $#

(𝑙+1)
P (𝑙+1) = LeakyReLU$%LP$(𝑙)
,
(11)
% W
$$ $$
where P (𝑙) represents the representations
$" $" from the 𝑙-th layer in
the × ×
hypergraph module. We feed the first layer with the previous
confounder representation masked by the treatment assignment,
(0)
i.e., p𝑖 = 𝑡𝑖 ∗ z𝑖 , where ∗ denotes element-wise multiplication.

(10)

Here D ∈ R𝑛×𝑛 is a diagonal matrix where each element represents
Í
𝑚×𝑚 is another diagonal
the node degree (i.e., 𝑚
𝑒=1 ℎ𝑖,𝑒 ). B ∈ R
Í
matrix, where each element is the size of each hyperedge ( 𝑛𝑖=1 ℎ𝑖,𝑒 ).

(𝑙 +1)

W (𝑙+1) ∈ R𝑑 ×𝑑
is the parameter matrix in the (𝑙+1)-th layer,
where 𝑑 (𝑙) and 𝑑 (𝑙+1) refer to the dimensionality of the interference
representations in the 𝑙-th and (𝑙+1)-th layers, respectively.
Modeling interference with different significance. Although the
above convolution layer can pass interferences through hyperedges,
it does not provide much flexibility to account for the significance of
interference for different nodes through different hyperedges. In the
aforementioned COVID-19 example, intuitively, those individuals
who are active in certain group gathering events are more likely
to influence or be influenced by others in these groups. To better
capture this intrinsic relationship between nodes and hyperedges on
a hypergraph, we leverage a hypergraph attention mechanism [5, 11,
52] to learn attention weights for each node and the corresponding
hyperedges that contain this node.
More specifically, we compute a representation for each hyperedge (𝑒) by aggregating across its associated nodes (N𝑒 ): z𝑒 =
Agg({z𝑖 | 𝑖 ∈ N𝑒 }). Here, Agg(·) can be any aggregation functions
(e.g., the mean aggregation). For each node 𝑖 and its associated
hyperedge 𝑒, the attention score between a node 𝑖 and a hyperedge
𝑒 can be calculated as:
exp(𝜎 (sim(z𝑖 W𝑎 , z𝑒 W𝑎 )))
,
(12)
𝛼𝑖,𝑒 = Í
𝑘 ∈E𝑖 exp(𝜎 (sim(z𝑖 W𝑎 , z𝑘 W𝑎 )))
where 𝜎 (·) is a non-linear activation function, E𝑖 denotes the set of
hyperedges associated with the node 𝑖. Here we use W𝑎 to denote a
parameter matrix to compute the node-hyperedge attention. sim(·)
is a similarity function, which can be implemented as:
sim(x𝑖 , x 𝑗 ) = a⊤ [x𝑖 ∥x 𝑗 ],

(13)

where a is a weight vector, [·∥·] is a concatenation operation.
Then we use the attention scores to model the interference with
different significance. Specifically, we replace the original incidence
e = {ℎe𝑖,𝑒 }, where ℎe𝑖,𝑒 =
matrix H in Eq. 10 with an enhanced matrix H
𝛼𝑖,𝑒 ℎ𝑖,𝑒 . In this way, the interference from different nodes on the
same hyperedge can be assigned with different importance weights,
indicating different levels of contribution for interference modeling.
We denote the final representations from the last convolution layer

Learning Causal Effects on Hypergraphs

KDD ’22, August 14–18, 2022, Washington, DC, USA

as P = {p𝑖 }𝑛𝑖=1 and expect it to capture the high-order interference
for each node.

which eventually allows us to evaluate the performance of the ITE
estimation from different causal inference approaches.

Representation Balancing. Similar to the coufounder representation learning module, we calculate a discrepancy penalty to reflect
the difference between the distributions of interference representations in treatment and control groups. We sum up these two
discrepancy penalties together to compute a representation balancing loss, denoted by L𝑏 .

4.1

3.3

Outcome Prediction

With the confounder representation z𝑖 and the interference representation p𝑖 , we model the potential outcomes as:
𝑦b𝑖1 = 𝑓1 ([z𝑖 ∥p𝑖 ]), 𝑦b𝑖0 = 𝑓0 ([z𝑖 ∥p𝑖 ]),

(14)

where 𝑓1 (·) and 𝑓0 (·) are learnable functions to predict the potential
outcome w.r.t. 𝑡 = 1 and 𝑡 = 0. We implement 𝑓1 (·) and 𝑓0 (·) with
two MLP modules. Then the prediction for the observed outcome
is obtained by 𝑦b𝑖 = 𝑦b𝑖𝑡𝑖 . We optimize the model to minimize the
following loss function:
𝑛
∑︁
L=
(𝑦𝑖 − 𝑦b𝑖 ) 2 + 𝛼 L𝑏 + 𝜆∥Θ∥ 2,
(15)
𝑖=1

where the first term is the standard mean squared error, L𝑏 is the
representation balancing loss, Θ represents the parameters in this
neural network model. 𝛼 and 𝜆 are two hyperparameters which
control the weights for the representation balancing loss and the
parameter regularization term. The ITE for each instance 𝑖 can be
estimated as: 𝜏b𝑖 = 𝑦b𝑖1 − 𝑦b𝑖0 .

3.4

Discussion

Here we revisit some implicit assumptions in the proposed framework. First, we assume that the interference for each node 𝑖 comes
from its neighbors through the hypergraph structure. Here, the
interference from neighbors that are multiple hops away can also
be captured by stacking more hypergraph convoluntional layers.
Second, for simplicity, we assume that the interference for each
node only comes from other nodes with non-zero treatment assignment. Third, we assume that the representations of nodes in the
same hyperedge are similar in the latent space. Besides, following
[5], we assume that the representations of hyperedges are homogeneous with node representations. Nevertheless, we should still
mention that this proposed framework is general and extendable,
where the above assumptions can be further relaxed by enriching
the hypergraph processing module.

4

EXPERIMENTS

It is typically very hard to obtain the ground-truth counterfactual
data as only one of the two potential outcomes can be obtained in
the observational data. Hence, in this section, we follow a standard
practice to evaluate the proposed framework and the alternative
approaches on three semi-synthetic datasets. We aim to leverage
as much real-world information as possible in the simulated environment. Our datasets are all based on real-world hypergraph data
and we retain the treatment allocations as well as node features
(covariates) if they are available. We simulate the outcome generation process to assess the true individual treatment effect (ITE),

Dataset and Simulation

We obtain the semi-synthetic data based on two publicly available
hypergraph datasets (Contact [7, 29], Goodreads [40, 41]) and
one large-scale proprietary web application dataset (Microsoft
Teams). We do not account for the temporal information of each
hyperedge in our experiments and leave this as a future research
direction instead. In all three datasets, we discard extremely large
hyperedges and keep those with no more than 50 nodes only.2
4.1.1 Outcome Simulation. Given the treatment allocations T, node
features X, and the hypergraph structure H, the potential outcome
of an individual 𝑖 can be simulated via
individual treatment effect (ITE)

z }| {
𝑦𝑖 = 𝑓𝑦,0 (x𝑖 ) + 𝛾 𝑓𝑡 (𝑡𝑖 , x𝑖 ) + 𝛽 𝑓𝑠 (T, X, H) + 𝜖 𝑦𝑖 ,
| {z }

(16)

hypergraph spillover effect

where 𝑓𝑦,0 (x𝑖 ) describes the outcome of instance 𝑖 when 𝑡𝑖 = 0
and without network interference, 𝑓𝑡 (·) calculates the ITE of each
instance, 𝑓𝑠 (·) calculates the spillover effect, and 𝜖 𝑦𝑖 denotes the
random noise from a Gaussian distribution N (0, 1). We specify
𝑓𝑦,0 (x𝑖 ) as a linear transformation of x𝑖 :
𝑓𝑦,0 = w0 x𝑖 ,

(17)

where w0 ∼ N (0, I), w0 ∈ R𝑑 . Then we control the individual
treatment effect (𝑓𝑡 (𝑡𝑖 , x𝑖 )) and the hypergraph spillover effect
(𝑓𝑠 (T, X, H)) under two different settings:
(1) Linear.

𝑓𝑡 (𝑡𝑖 , x𝑖 ) =

w1 x𝑖 + 𝜖

if 𝑡𝑖 = 1

0

if 𝑡𝑖 = 0

(18)

Here w1 ∈ R𝑑 , and each element in w1 follows a Gaussian
distribution. We generate 𝑓𝑠 as:
1 ∑︁ ′ 1 ∑︁
𝑓𝑠 (T, X, H) =
𝜎 (
𝑡 𝑗 × 𝑓𝑡 (𝑡 𝑗 , x 𝑗 )).
(19)
|E𝑖 |
|N𝑒 |
𝑒 ∈E𝑖

𝑗 ∈N𝑒

Here, 𝜎 ′ (·) is a function on the aggregation over each hyperedge. We implement it with an identity function by default.
(2) Quadratic.
( ⊤
x W𝑡 x𝑖 + 𝜖 if 𝑡𝑖 = 1
𝑓𝑡 (𝑡𝑖 , x𝑖 ) = 𝑖
(20)
0
if 𝑡𝑖 = 0
Here W𝑡 ∈ R𝑑×𝑑 , and each element in W𝑡 follows a Gaussian
distribution. We generate 𝑓𝑠 as:
1 ∑︁ ′ 1
(T𝑒 ∗ X𝑒 )W𝑡 (T𝑒 ∗ X𝑒 ) ⊤ ). (21)
𝑓𝑠 (T, X, H) =
𝜎 (
|E𝑖 |
|N𝑒 | 2
𝑒 ∈E
𝑖

Here X𝑒 and T𝑒 are the feature matrix and treatment assignment of nodes contained in hyperedge 𝑒, respectively. Here
∗ denotes element-wise multiplication.
2 Note hyperedges with large size of nodes are usually less meaningful [7].

KDD ’22, August 14–18, 2022, Washington, DC, USA

Jing Ma et al.

4.1.2 Dataset Details. We follow the above process to generate
potential outcomes on all three datasets. Additional details about
each dataset are provided as the follows.
Contact. This dataset collects interactions recorded by wearable
sensors among students at a high school [7, 29], and includes 327
nodes and 7,818 hyperedges. Each node represents a person, and
each hyperedge stands for a group of individuals are in close physical proximity to each other. This contact hypergraph data allows us
to simulate a hypothetical question: “how does one’s face covering
practice (treatment) causally affect their infection risk of an infectious disease (outcome)?”. In each group contact, one may bring the
virus to the surrounding environment, and thus affect other people’s infection risk. Due to the lack of detailed information about
each individual, apart from the potential outcome, we also generate
the treatment (𝑡𝑖 ) and the covariates (x𝑖 ) as the follows:
x𝑖 ∼ N (0, I), 𝑡𝑖 ∼ 𝐵𝑒𝑟 (sigmoid(x𝑖 v𝑡 )),

GoodReads. This dataset collects book information from the book
review website GoodReads3 , including the book title, authors, descriptions, reviews, and ratings [40, 41]. We take each book in the
Children category as an instance. The bag-of-words of the book
descriptions are used as the covariates of each book. Each hyperedge corresponds to each author and all books sharing the same
author are in the same hyperedge. The real-world book ratings are
considered as treatment assignments: for each node 𝑖, we define
𝑡𝑖 = 1 if the rating score is larger than 3 and 𝑡𝑖 = 0 otherwise. We
aim to study the causal effect of the rating score on the sales of
each book. The ratings of each author’s books can establish this
author’s overall reputation, and thus influence the sales of other
books from the same author. The final processed dataset includes
57,031 nodes (where 40% are treated) and 12,709 hyperedges. Note
each book may have more than one author, and each author may
have published multiple books.
Microsoft Teams. We sampled 91,391 anonymized employees of a
multinational technology company and collected their aggregated
telemetry data on Microsoft Teams4 . Microsoft Teams is a workplace communication platform where users are allowed to create a
group space (i.e., “team” or “channel”) to enable public communication within each group. We are interested in how a user’s usage of
these group spaces causally affects their productivity. We process
the treatment assignment into binary values by taking it as 1 if
the employee has sent out at least one message in any of these
group spaces during the first week of March, 2021; otherwise the
treatment is assigned as 0. Each group space can be regarded as a
hyperedge, where information can be shared via group discussions
thus one’s activeness on this platform may affect other individuals’
outcomes in the same group. Employee demographics (e.g., office
location, job description, work experience) were leveraged as the
covariates.
3 https://www.goodreads.com/

Linear
Quadratic
√
√
𝜖𝑃 𝐸𝐻 𝐸
𝜖𝐴𝑇 𝐸
𝜖𝑃 𝐸𝐻 𝐸
𝜖𝐴𝑇 𝐸
LR
25.41 ±0.04 9.11 ±0.09 38.22 ±0.77 20.28 ±0.38
CEVAE
22.88 ±1.07 8.29 ±0.69 35.28 ±0.75 18.22 ±0.76
CFR
24.04 ±0.75 7.17 ±0.43 32.24 ±1.01 17.28 ±0.75
Netdeconf 10.22 ±0.47 4.29 ±0.13 21.23 ±0.72 11.39 ±0.74
GNN-HSIC 7.42 ±0.39 2.06 ±0.03 16.28 ±0.24 7.28 ±0.39
GCN-HSIC 7.28 ±0.44 2.08 ±0.04 14.23 ±0.20 6.27 ±0.15
HyperSCI 3.45 ±0.27 1.39 ±0.03 9.20 ±0.09 2.24 ±0.07
LR
23.01 ±0.04 13.42 ±0.12 48.56 ±1.02 31.19 ±0.47
CEVAE
22.69 ±0.03 12.49 ±0.06 45.21 ±3.10 29.22 ±0.44
CFR
20.30 ±0.03 13.21 ±0.09 41.72 ±0.72 26.28 ±0.43
Netdeconf 18.39 ±0.19 12.20 ±0.03 35.18 ±0.78 21.20 ±0.76
GNN-HSIC 17.20 ±0.23 12.18 ±0.13 27.22 ±0.78 16.87 ±0.47
GCN-HSIC 16.01 ±0.20 12.06 ±0.15 25.42 ±0.76 16.28 ±0.76
HyperSCI 15.68 ±0.21 11.81 ±0.15 19.23 ±0.44 13.33 ±0.27
LR
22.80 ±0.64 21.41± 0.74 414.17 ±3.94 192.80 ±2.97
CEVAE
19.36 ±0.80 8.63 ±0.78 315.01 ±2.53 188.47 ±4.27
CFR
25.23 ±0.01 18.28 ±0.02 392.56 ±4.33 189.75 ±4.80
Netdeconf 11.11 ±0.01 9.22 ±0.03 241.02 ±2.32 147.29 ±1.04
GNN-HSIC 9.38 ±0.44 6.91 ±0.38 114.28 ±3.62 81.21 ±2.53
GCN-HSIC 8.27 ±0.41 6.60 ±0.48 109.57 ±3.85 77.75 ±3.93
HyperSCI 5.13 ±0.56 4.46 ±0.61 81.08 ±0.37 74.41 ±0.42

Data Method
CT

GR

(22)

where I is an 𝑑 × 𝑑 identity matrix, here we set 𝑑 = 50. v𝑡 is a 𝑑dimensional vector where each element inside follows a Gaussian
distribution. Eventually about 50% ∼ 60% of the nodes are treated
(𝑡𝑖 = 1) in our experiments.

4 https://www.microsoft.com/en-us/microsoft-teams

Table 1: ITE estimation performance (mean ± standard error). “CT", “GR" and “MS" stand for Contact, GoodReads and
Microsoft Teams datasets, respectively.

MS

4.2

Experiment Settings

4.2.1 Metrics. We evaluate the performance of causal effect estimation through two standard metrics, including Rooted Precision
√
in Estimation of Heterogeneous Effect ( 𝜖𝑃𝐸𝐻 𝐸 ) [18] and Mean
Absolute Error (𝜖𝐴𝑇 𝐸 ) [42]. These metrics can be defined as follows:
v
t ∑︁
√
1
1 ∑︁
1 ∑︁
𝜖𝑃𝐸𝐻 𝐸 =
(𝜏𝑖 − 𝜏b𝑖 ) 2, 𝜖𝐴𝑇 𝐸 = |
𝜏𝑖 −
𝜏b𝑖 |.
𝑛
𝑛
𝑛
𝑖 ∈ [𝑛]

𝑖 ∈ [𝑛]

𝑖 ∈ [𝑛]

(23)
√
Lower 𝜖𝑃𝐸𝐻 𝐸 or 𝜖𝐴𝑇 𝐸 indicates better causal effect estimations.
4.2.2 Baselines. To investigate the effectiveness of our framework,
we compare it with multiple state-of-the-art ITE estimation baselines. These baselines can be divided into the following categories:
• No graph. We compare the estimation results with traditional
methods which do not consider graph data and spillover effects.
These methods include outcome regression which is implemented
by linear regression (LR), counterfactual regression (CFR [34]),
causal effect variational autoencoder (CEVAE [27]). By comparing the proposed framework to these methods, we evaluate the
effectiveness of modeling interference for ITE estimation.
• No spillover effect in ordinary graphs. Although assuming
no spillover effect exists, the network deconfounder (Netdeconf)
[17] captures latent confounders for ITE estimation by utilizing
the network structure among instances.
• Spillover effect in ordinary graphs. We compare our framework with other ITE estimation baselines which can handle the
pairwise spillover effect on ordinary graphs: a node representation learning based method [28] estimates ITE under network
interference, including two variants: (a) GNN + HSIC, which is

Learning Causal Effects on Hypergraphs

εATE

εPEHE

12
11

14

√
(a) GoodReads, 𝜖𝑃 𝐸𝐻 𝐸

β = 5.0

(b) 𝜖𝐴𝑇 𝐸

5

√

εPEHE

4
3
2
1

4.4

Ablation Study

To investigate the effectiveness of different components in the proposed framework, we conduct ablation studies by considering the
following variants: 1) we apply the proposed model HyperSCI on
the projected graph (in a hypergraph structure) (denoted as HyperSCI-P); 2) we replace the hypergraph neural network module

εPEHE

HyperSCI-G, √ εPEHE
HyperSCI, εATE
HyperSCI-G, εATE

√

16
2 5 10

20

50

k

18
17
16
15
14
13
12

(a) GoodReads, Linear

28
26
24
22
20
18
16
14
50 12

30

εATE

HyperSCI, √ εPEHE

18

20

2 5 10

20

k

(b) GoodReads, Quadratic

Figure 6: ITE estimation performance of HyperSCI / HyperSCI-G on hypergraphs with hyperedge size no more than 𝑘.
20
14
13

16

12

14
0.0001 0.001

0.01

18

16

εATE

14
13
12
14

11
2
3
# of attention head

4

(c) # of attention head

32

d

64

11
128

(b) Representation dimension
18

15

16

13
12

0.1

(a) Balancing weight

1

14
16
14

11
α

15
εATE

εPEHE
√

18

18

15

εPEHE
εATE
√

εPEHE

We include the results for the ITE estimation task in Table 1. From
this table we observe that the proposed framework outperforms all
the baselines under both linear and quadratic outcome simulation
settings. We attribute these results to the fact that HyperSCI utilizes the relational information in hypergraph to model the highorder interference, and thus mitigates the influence of the spillover
effect on ITE estimation performance. Compared with other baselines, the methods which incorporate the pairwise network interference (GCN-HSIC and GNN-HSIC), as well as Netdeconf which
utilizes the network structure for ITE estimation, perform better
than those baselines which do not take advantage of the relational
information (LR, CEVAE, CFR).
We also vary the hyperparameter (𝛽) which controls the significance of hypergraph spillover effect in the outcome simulation
and report the ITE estimation results in Fig. 4. As 𝛽 increases, i.e.,
the outcome is more heavily influenced by interference, larger performance gains can be observed from the proposed framework
(HyperSCI) against baselines. This observation further validates
the effectiveness of our framework in modeling the interference
for enhancing the performance of ITE estimation.

(d) Contact, 𝜖𝐴𝑇 𝐸

Figure 5: Ablation studies of different variants of our framework HyperSCI. Results (mean and standard error) are reported under the linear setting but similar patterns can be
found under the quadratic setting and on all datasets.

√

ITE Estimation Performance

I
P
B
G
rSCI- yperSCI- perSCI-N HyperSC
Hype
H
Hy

√
(c) Contact, 𝜖𝑃 𝐸𝐻 𝐸

20

4.2.3 Setup. We randomly partition all datasets into 60%-20%-20%
training/validation/test splits. All the results are averaged over ten
repeated executions. Unless otherwise specified, we set the hyperparameters as 𝛼 = 0.001, 𝛽 = 1.0, 𝛾 = 1.0, 𝜆 = 0.01, the dimension
for confounder representation and interference representation both
as 64. We use ReLU as the activation function, and use an Adam optimizer. By default, the interference modeling component contains
one hypergraph convolutional layer.

0

I
P
B
G
rSCI- yperSCI- perSCI-N HyperSC
Hype
H
Hy

15
14

εATE

based on graph neural network [30] and Hilbert Schmidt independence criterion (HSIC) [16], and (b) GCN + HSIC, which is
based on GCN [24].
To utilize the baselines which handle ordinary graphs, we
project the original hypergraph H to an ordinary graph G =
{V, E 𝑝 } by setting (𝑣𝑖 , 𝑣 𝑗 ) ∈ E 𝑝 if 𝑣𝑖 and 𝑣 𝑗 are contained in
at least one common hyperedge in H . By comparing HyperSCI to the above baselines, we are able to evaluate the benefits of
modeling high-order interferences on the original hypergraph.

(b) GoodReads, 𝜖𝐴𝑇 𝐸

14
13
12
11
10
9

εATE

β = 3.0

I
P
B
G
rSCI- yperSCI- perSCI-N HyperSC
H
Hy

Hype

εPEHE

β = 1.0

Figure 4: Comparison of the performance of ITE estimation
under different values of 𝛽 in linear setting on GoodReads.

4.3

10

I
P
B
G
rSCI- yperSCI- perSCI-N HyperSC
Hype
H
Hy

√

β = 5.0

13

15

εPEHE

β = 3.0

√
(a) 𝜖𝑃 𝐸𝐻 𝐸

14

16

√

β = 1.0

15

17

εPEHE

20

18

16

13

√

40
0

45
40
35
30
25
20
15
10
5
0

εATE

60

GNN-HSIC
GCN-HSIC
HyperSCI

√

80

LR
CEVAE
CFR
Netdeconf

εATE

√

εPEHE

100

εATE

120

KDD ’22, August 14–18, 2022, Washington, DC, USA

12
14
0.0001 0.001

11
λ

0.01

0.1

(d) Regularization weight

Figure 7: ITE estimation performance (mean and standard
error) of the proposed framework HyperSCI under different
parameters or model structures on GoodReads dataset.
with a graph neural network module with the same number of
layers, and then apply it on the projected graph (in an original
graph structure) (HyperSCI-G). Notice that although both evaluated on the projected graph, HyperSCI-G handles ordinary graphs
with its graph neural network module, while HyperSCI-P handles
hypergraphs with its hypergraph neural network module; 3) we remove the balancing techniques in the framework (HyperSCI-NB).

KDD ’22, August 14–18, 2022, Washington, DC, USA

The ITE estimation results are reported in Fig. 5, where we notice
significant performance gaps between HyperSCI-P/HyperSCIG and HyperSCI, which imply the effectiveness of modeling the
high-order relationships on hypergraphs. We also observe the ITE
estimation performance degrades after removing the representation balancing modules, which indicates the effectiveness of the
representation balancing techniques on mitigating the biases of ITE
estimations.

4.5

A Closer Look at High-Order Interference

In addition to the overall ITE estimation performance, we take
a closer look at high-order interference. We investigate how the
proposed framework responds to hyperedges with difference sizes.
More specifically, we remove the hyperedges with size larger than
𝑘, denote the modified hypergraph as H (𝑘) , and vary the value
of 𝑘. In Fig 6, we compare the ITE estimation performance of the
proposed framework HyperSCI with its variant on the projected
ordinary graph HyperSCI-G. We observe that: 1) When 𝑘 = 2
(hyperedge size ≤ 2), the performance of HyperSCI-G is close to
HyperSCI. Because when 𝑘 = 2, graph convolution can be regarded
as a special case of hypergraph convolution with small differences
in the graph Laplacian matrix (as illustrated in [5]). Empirically
this leads to a minor performance difference between HyperSCIG and HyperSCI; 2) When 𝑘 increases, the performance of ITE
estimation from both methods are gradually improved, but such an
improvement becomes less significant when 𝑘 is larger. Besides, we
notice HyperSCI consistently outperforms HyperSCI-G and such
a difference becomes larger as 𝑘 increases, indicating its efficacy on
modeling high-order interference especially on large hyperedges.

4.6

Sensitivity Analysis

To evaluate the robustness of the proposed framework, we present
the ITE estimation performance of HyperSCI under different settings of model hyper-parameters in Fig. 7. More specifically, we vary
the value of the balancing weight from {0.0001, 0.001, 0.01, 0.1}, and
vary the representation dimension from {16, 32, 64, 128}. We also
vary the number of attention head from {1, 2, 3, 4}, then change the
parameter of regularization weight from {0.0001, 0.001, 0.01, 0.1}.
As can be observed, our framework is generally robust to different
hyper-parameter settings, but proper fine-tuning of these hyperparameters is still beneficial for the ITE estimation performance.

5

RELATED WORK

Causal studies under network interference. There have been
many causal studies [3, 6, 9, 21, 25, 28, 37, 39, 49] which address the
existence of network interference. These works mainly include the
following categories: (i) Random assignment strategy under interference [3, 6, 12, 21, 39]. These works focus on experimental studies
under interference (without SUTVA assumption). In some studies
[23], strong interference is assumed to exist within each group while
there is no interference across different groups; (ii) Causal effect
estimation on observational data with interference [2, 28, 32, 38]. Different from the experimental studies which can design assignment
strategy, another line of works (and also our work) assume interferences exist across individuals in the observational data. They
relax the SUTVA assumption and define the potential outcome
with a function that takes the instance covariates and treatment

Jing Ma et al.

assignment of each individual and other interacted individuals as
input. Among them, Rakesh et al. [32] propose a Linked Causal
Variational Autoencoder (LCVA) framework to estimate the causal
effect of a treatment on an outcome with the existence of interference between pairs of instances. Different from these works
that focus on pairwise spillover effects, Ma et al. [28] consider the
spillover effect in network structure, and propose a graph neural
network (GNN) [24] based framework for causal effect estimation
under network interference. However, these works are still limited
in pairs of individuals or ordinary graphs and lack consideration of
high-order interference. Another line of studies is bipartite causal
inference [31, 53]. Traditionally, bipartite causal inference involves
two types of units: interventional/outcome units. Interventional
units are assigned with treatments, and outcomes are observed
from outcome units. Although this setup is different from ours,
considering that there is a node-hyperedge bipartite corresponding
to each hypergraph (and ordinary graph), thus the two modeling
approaches (bipartite and hypergraph) are conceptually similar.
Nevertheless, we argue hypergraph is a more appropriate framing
in many scenarios since: i) hypergraph does not require instantiating edges as additional nodes, or treating these two kinds of nodes
differently, thus more computationally efficient; ii) hypergraph has
the potential to be more convenient and efficient when generalizing to new hyperedges, while bipartite needs to generate both new
nodes for the new hyperedges and their associated new edges.
Hypergraph algorithms and neural networks. To process hypergraph structures for downstream tasks, a line of works simplify
the hypergraph structure by taking abstract representations of
complicated multi-way interactions [7, 26, 43, 45, 51]. Other works
directly tackle the original hypergraph structure [4, 8, 13, 19, 35, 44].
Recently, numerous works have studied on hypergraph neural networks [5, 44]. Feng el al. [13] propose hypergraph neural networks
(HGNN) framework to encode high-order data correlation in a hypergraph structure. A hyperedge convolution operation is designed
for representation learning. Bai et al. [5] introduce two end-to-end
trainable operators hypergraph convolution and hypergraph attention to learn node representations in hypergraphs. Yadati et
al. [44] develop a self-attention based hypergraph neural network
Hyper-SAGNN, which is applicable to homogeneous or heterogeneous hypergraphs with variable hyperedge sizes. Jiang et al. [22]
propose a dynamic hypergraph neural network (DHGNN) which
can dynamically update hypergraph structure on each layer.

6

CONCLUSION

In this paper, we study an important research problem of individual
treatment effect estimation with the existence of high-order interference on hypergraphs. We identify and analyze the influence of
high-order interference in causal effect estimation. To address this
problem, we propose a novel framework HyperSCI, which estimates the ITEs based on representation learning. More specifically,
HyperSCI learns the representation of confounders, models the
high-order interference with a hypergraph neural network module, then predicts the potential outcomes for each instance with
the learned representations. We conduct extensive experiments to
evaluate the proposed framework, where the results consistently
validate the effectiveness of HyperSCI in ITE estimation under
different interference scenarios.

Learning Causal Effects on Hypergraphs

REFERENCES
[1] Rohini Ahluwalia, H Rao Unnava, and Robert E Burnkrant. 2001. The moderating
role of commitment on the spillover effect of marketing communications. Journal
of Marketing research 38, 4 (2001), 458–470.
[2] David Arbour, Dan Garant, and David Jensen. 2016. Inferring network effects
from observational data. In Proceedings of the 22nd ACM SIGKDD International
Conference on Knowledge Discovery and Data Mining. 715–724.
[3] Peter M Aronow and Cyrus Samii. 2017. Estimating average causal effects under
general interference, with application to a social network experiment. The Annals
of Applied Statistics 11, 4 (2017), 1912–1947.
[4] Devanshu Arya and Marcel Worring. 2018. Exploiting relational information in
social networks using geometric deep learning on hypergraphs. In Proceedings of
the 2018 ACM on International Conference on Multimedia Retrieval. 117–125.
[5] Song Bai, Feihu Zhang, and Philip HS Torr. 2021. Hypergraph convolution and
hypergraph attention. Pattern Recognition 110 (2021), 107637.
[6] Guillaume Basse and Avi Feller. 2018. Analyzing two-stage experiments in the
presence of interference. J. Amer. Statist. Assoc. 113, 521 (2018), 41–55.
[7] Austin R Benson, Rediet Abebe, Michael T Schaub, Ali Jadbabaie, and Jon Kleinberg. 2018. Simplicial closure and higher-order link prediction. Proceedings of
the National Academy of Sciences 115, 48 (2018), E11221–E11230.
[8] Austin R Benson, Ravi Kumar, and Andrew Tomkins. 2018. Sequences of sets.
In Proceedings of the 24th ACM SIGKDD International Conference on Knowledge
Discovery & Data Mining. 1148–1157.
[9] Rohit Bhattacharya, Daniel Malinsky, and Ilya Shpitser. 2020. Causal inference
under interference and network uncertainty. In Uncertainty in Artificial Intelligence.
[10] Ulrik Brandes, Linton C Freeman, and Dorothea Wagner. 2013. Social networks.
[11] Kaize Ding, Jianling Wang, Jundong Li, Dingcheng Li, and Huan Liu. 2020. Be
more with less: Hypergraph attention networks for inductive text classification.
arXiv preprint (2020).
[12] Zahra Fatemi and Elena Zheleva. 2020. Minimizing interference and selection
bias in network experiment design. In International AAAI Conference on Web and
Social Media.
[13] Yifan Feng, Haoxuan You, Zizhao Zhang, Rongrong Ji, and Yue Gao. 2019. Hypergraph neural networks. In Proceedings of the AAAI Conference on Artificial
Intelligence, Vol. 33. 3558–3565.
[14] Ronald Aylmer Fisher. 1936. Design of experiments. Br Med J 1, 3923 (1936),
554–554.
[15] Cory E Goldstein, Charles Weijer, Jamie C Brehaut, Dean A Fergusson, Jeremy M
Grimshaw, Austin R Horn, and Monica Taljaard. 2018. Ethical issues in pragmatic
randomized controlled trials: a review of the recent literature identifies gaps in
ethical argumentation. BMC Medical Ethics (2018).
[16] Arthur Gretton, Olivier Bousquet, Alex Smola, and Bernhard Schölkopf. 2005.
Measuring statistical dependence with Hilbert-Schmidt norms. In International
conference on algorithmic learning theory. Springer, 63–77.
[17] Ruocheng Guo, Jundong Li, and Huan Liu. 2020. Learning individual causal
effects from networked observational data. In Proceedings of the 13th International
Conference on Web Search and Data Mining. 232–240.
[18] Jennifer L Hill. 2011. Bayesian nonparametric modeling for causal inference.
Journal of Computational and Graphical Statistics 20, 1 (2011).
[19] Jin Huang, Rui Zhang, and Jeffrey Xu Yu. 2015. Scalable hypergraph learning and
processing. In 2015 IEEE International Conference on Data Mining. IEEE, 775–780.
[20] Michael G Hudgens and M Elizabeth Halloran. 2008. Toward causal inference
with interference. J. Amer. Statist. Assoc. 103, 482 (2008), 832–842.
[21] Kosuke Imai, Zhichao Jiang, and Anup Malani. 2020. Causal inference with
interference and noncompliance in two-stage randomized experiments. J. Amer.
Statist. Assoc. (2020), 1–13.
[22] Jianwen Jiang, Yuxuan Wei, Yifan Feng, Jingxuan Cao, and Yue Gao. 2019. Dynamic Hypergraph Neural Networks.. In IJCAI. 2635–2641.
[23] Brian Karrer, Liang Shi, Monica Bhole, Matt Goldman, Tyrone Palmer, Charlie
Gelman, Mikael Konutgan, and Feng Sun. 2021. Network experimentation at
scale. In Proceedings of the 27th ACM SIGKDD Conference on Knowledge Discovery
& Data Mining. 3106–3116.
[24] Thomas N Kipf and Max Welling. 2016. Semi-supervised classification with graph
convolutional networks. arXiv preprint (2016).
[25] Ron Kohavi, Alex Deng, Brian Frasca, Toby Walker, Ya Xu, and Nils Pohlmann.
2013. Online controlled experiments at large scale. In Proceedings of the 19th
ACM SIGKDD international conference on Knowledge discovery and data mining.
1168–1176.
[26] Dong Li, Zhiming Xu, Sheng Li, and Xin Sun. 2013. Link prediction in social
networks based on hypergraph. In Proceedings of the 22nd International Conference
on World Wide Web. 41–42.
[27] Christos Louizos, Uri Shalit, Joris M Mooij, David Sontag, Richard Zemel, and
Max Welling. 2017. Causal effect inference with deep latent-variable models. In
Advances in Neural Information Processing Systems.
[28] Yunpu Ma and Volker Tresp. 2021. Causal Inference under Networked Interference and Intervention Policy Enhancement. In International Conference on

KDD ’22, August 14–18, 2022, Washington, DC, USA

Artificial Intelligence and Statistics. PMLR, 3700–3708.
[29] Rossana Mastrandrea, Julie Fournet, and Alain Barrat. 2015. Contact patterns
in a high school: a comparison between data collected using wearable sensors,
contact diaries and friendship surveys. PloS one 10, 9 (2015), e0136497.
[30] Christopher Morris, Martin Ritzert, Matthias Fey, William L Hamilton, Jan Eric
Lenssen, Gaurav Rattan, and Martin Grohe. 2019. Weisfeiler and leman go neural:
Higher-order graph neural networks. In Proceedings of the AAAI Conference on
Artificial Intelligence, Vol. 33. 4602–4609.
[31] Jean Pouget-Abadie, Kevin Aydin, Warren Schudy, Kay Brodersen, and Vahab
Mirrokni. 2019. Variance reduction in bipartite experiments through correlation
clustering. (2019).
[32] Vineeth Rakesh, Ruocheng Guo, Raha Moraffah, Nitin Agarwal, and Huan Liu.
2018. Linked causal variational autoencoder for inferring paired spillover effects.
In Proceedings of the 27th ACM International Conference on Information and
Knowledge Management. 1679–1682.
[33] Donald B Rubin. 1980. Randomization analysis of experimental data: The Fisher
randomization test comment. J. Amer. Statist. Assoc. 75, 371 (1980), 591–593.
[34] Uri Shalit, Fredrik D Johansson, and David Sontag. 2017. Estimating individual
treatment effect: generalization bounds and algorithms. In International Conference on Machine Learning.
[35] Ankit Sharma, Jaideep Srivastava, and Abhishek Chandra. 2014. Predicting
multi-actor collaborations using hypergraphs. arXiv preprint (2014).
[36] Jerzy Splawa-Neyman, Dorota M Dabrowska, and TP Speed. 1990. On the application of probability theory to agricultural experiments. Essay on principles.
Section 9. Statist. Sci. (1990), 465–472.
[37] Eric J Tchetgen Tchetgen and Tyler J VanderWeele. 2012. On causal inference in
the presence of interference. Statistical methods in medical research 21, 1 (2012),
55–75.
[38] Eric J Tchetgen Tchetgen, Isabel R Fulcher, and Ilya Shpitser. 2021. Auto-gcomputation of causal effects on a network. J. Amer. Statist. Assoc. 116, 534 (2021),
833–844.
[39] Johan Ugander, Brian Karrer, Lars Backstrom, and Jon Kleinberg. 2013. Graph
cluster randomization: Network exposure to multiple universes. In Proceedings of
the 19th ACM SIGKDD international conference on Knowledge discovery and data
mining. 329–337.
[40] Mengting Wan and Julian McAuley. 2018. Item recommendation on monotonic
behavior chains. In Proceedings of the 12th ACM conference on recommender
systems. 86–94.
[41] Mengting Wan, Rishabh Misra, Ndapandula Nakashole, and Julian McAuley. 2019.
Fine-Grained Spoiler Detection from Large-Scale Review Corpora. In Proceedings
of the 57th Annual Meeting of the Association for Computational Linguistics. 2605–
2610.
[42] Cort J Willmott and Kenji Matsuura. 2005. Advantages of the mean absolute
error (MAE) over the root mean square error (RMSE) in assessing average model
performance. Climate research 30, 1 (2005), 79–82.
[43] Ye Xu, Dan Rockmore, and Adam M Kleinbaum. 2013. Hyperlink prediction
in hypernetworks using latent social features. In International Conference on
Discovery Science. Springer, 324–339.
[44] Naganand Yadati, Madhav Nimishakavi, Prateek Yadav, Anand Louis, and Partha
Talukdar. 2018. Hypergcn: Hypergraph convolutional networks for semisupervised classification. arXiv preprint 22 (2018).
[45] Naganand Yadati, Vikram Nitin, Madhav Nimishakavi, Prateek Yadav, Anand
Louis, and Partha Talukdar. 2018. Link prediction in hypergraphs using graph
convolutional networks. (2018).
[46] Liuyi Yao, Sheng Li, Yaliang Li, Mengdi Huai, Jing Gao, and Aidong Zhang. 2018.
Representation learning for treatment effect estimation from observational data.
Advances in Neural Information Processing Systems 31 (2018).
[47] Serdar Yilmaz, Kingley E Haynes, and Mustafa Dinc. 2002. Geographic and network neighbors: Spillover effects of telecommunications infrastructure. Journal
of Regional Science 42, 2 (2002), 339–360.
[48] Se-eun Yoon, Hyungseok Song, Kijung Shin, and Yung Yi. 2020. How Much and
When Do We Need Higher-order Information in Hypergraphs? A Case Study on
Hyperedge Prediction. In Proceedings of The Web Conference 2020. 2627–2633.
[49] Yuan Yuan, Kristen Altenburger, and Farshad Kooti. 2021. Causal Network Motifs:
Identifying Heterogeneous Spillover Effects in A/B Tests. In Proceedings of the
Web Conference 2021. 3359–3370.
[50] Chen Zeng, Yan Song, Dawei Cai, Peiying Hu, Huatai Cui, Jing Yang, and Hongxia
Zhang. 2019. Exploration on the spatial spillover effect of infrastructure network
on urbanization: A case study in Wuhan urban agglomeration. Sustainable Cities
and Society 47 (2019), 101476.
[51] Muhan Zhang, Zhicheng Cui, Shali Jiang, and Yixin Chen. 2018. Beyond link
prediction: Predicting hyperlinks in adjacency space. In Thirty-Second AAAI
Conference on Artificial Intelligence.
[52] Ruochi Zhang, Yuesong Zou, and Jian Ma. 2019. Hyper-SAGNN: a self-attention
based graph neural network for hypergraphs. arXiv preprint (2019).
[53] Corwin M Zigler and Georgia Papadogeorgou. 2021. Bipartite causal inference
with interference. Statistical science: a review journal of the Institute of Mathematical Statistics 36, 1 (2021), 109.

KDD ’22, August 14–18, 2022, Washington, DC, USA

Table 2: Notation.
Notation

Definition

H
V, E
H
𝑛
𝑚
N𝑖
N𝑒
E𝑖
X, x𝑖
T, 𝑡𝑖
Y, 𝑦𝑖
𝑦𝑖1, 𝑦𝑖0
Φ𝑌 (·)
𝜏𝑖 , 𝜏b𝑖
𝑦𝑖 , 𝑦b𝑖
(·)−𝑖
𝛿𝑖
SMR(·)
O, o𝑖
Z, z𝑖
Ψ(·)
𝑓1 (·), 𝑓0 (·)
P, p𝑖
𝑟 (𝑖)

hypergraph
the set of nodes/hyperedges
hypergraph structure matrix
the number of nodes
the number of hyperedges
the set of neighboring nodes for the 𝑖-th node
the set of nodes on the hyperedge 𝑒
the set of hyperedges which contains the 𝑖-th node
features of all nodes/the 𝑖-th node
treatment assignment of all nodes/the 𝑖-th node
observed outcome of all nodes/the 𝑖-th node
potential outcomes of the 𝑖-th node
potential outcome function
true/predicted ITE for the 𝑖-th node
true/predicted outcome for the 𝑖-th node
variables for all the nodes except the 𝑖-th node
the spillover effect of the 𝑖-th node
summary function
the environment information of the 𝑖-th node
confounder representations of all nodes/the 𝑖-th node
interference representation learner
potential outcome prediction functions
interference representations of all nodes/the 𝑖-th node
the ratio of the treatment assignment of the 𝑖-node
in its neighborhood

B MORE EXPERIMENTAL RESULTS
B.1 ITE Estimation Performance under
Different Settings on All the Datasets
In this section, we show the ITE estimation performance under
different settings (including the linear and quadratic settings with
𝛽 among {1.0, 3.0, 5.0}) on all the datasets in Fig. 9. We can observe
that the proposed HyperSCI consistently outperforms the baselines under different settings on all the datasets. The superiority of
our framework against baselines becomes more obvious when 𝛽
is larger (i.e., the interference is stronger), because our framework
can better handle the interference in the hypergraph.

B.2

Case Studies

We further conduct case studies to investigate how the proposed
method acts on individuals in responding to their neighboring nodes
(i.e., the size of one’s neighborhood and the homophily of treatment
assignments within one’s neighborhood). The neighborhood of 𝑖
is defined as the set of nodes which are connected with 𝑖 via any
Ð
hyperedges, i.e., N𝑖 = 𝑒 ∈ E𝑖 { 𝑗 ∈ N𝑒 }. The homophily of treatment
assignment is defined as the ratio of neighboring nodesÍwhich share
𝑗 ∈N

1(𝑡 𝑗 =𝑡𝑖 )

𝑖
the same treatment assignment as oneself, i.e., 𝑟 (𝑖) =
.
|N𝑖 |
In Fig. 8a, we show the difference between the ITE estimation

results made with the original hypergraph and with the projected
graph, w.r.t. N𝑖 and 𝑟 (𝑖). Overall, we see larger divergences on
individuals with a larger neighborhood size but less agreement with
their neighbors in terms of treatment assignments. In Fig. 8b, we
further showcase the insights by presenting several representative
children books on the GoodReads dataset. For example, the author
of “Peter Pan” had not published many works but these books all
received good rating scores, leading to a “consistent" reputation of
the author. Therefore, the outcome of the book “Peter Pan” is less
impacted by the high-order interference among its neighbors. On
the other hand, the high rating score of the book “Oddhopper Opera”
differs from most of its neighbors, leading to a mixed reputation of
the author. In this case, the potential outcome is more likely to be
affected by the high-order interference on the hypergraph.

0.9
0.7
0.6
0.4
0.2
0.1

15
10
5
5 10 15 20 25 30 0
| (i)|
(a) Heatmap

Harry Potter and the Prisoner of Azkaban

r(i)

NOTATION TABLE

We use Table 2 to list the most important notations used in this
paper.

r(i)

A

Jing Ma et al.

1.2
Go, Dog. Go!
(8, 1.0)
(33, 0.911)
1.0
Love Monster
Peter Pan
0.8 (1, 1.0)
(16, 0.588)
Oddhopper Opera:
0.6
A Bug's Garden
of Verses
The Gingerbread Rabbit
0.4
(30, 0.129)
(8, 0.111)
0.2
0.0
0 5 10 15 20 25 30 35 40
|(i)|

14
12
10
8
6
4
2

(b) Case studies

Figure 8: (a) Heatmap: the difference between ITE estimations with hypergraph and with projected ordinary graph
on GoodReads. Nodes are divided into 6 × 6 grids w.r.t. their
number of neighbors |N𝑖 | and the homophily of treatment
assignment 𝑟 (𝑖). (b) Case studies of representative books.

C

DETAILS OF EXPERIMENTAL SETTINGS

All the experiments are conducted under the following environment:
• Operating system: Ubuntu 18.04
• GPU memory: 16GB
• Pytorch 1.9.0, Cuda ToolKit 11.1, cuDNN 8.0.5
Baseline parameter settings. For the baselines CEVAE, CFR, Netdeconf, GNN-HSIC, and GCN-HSIC, we set the representation dimension as 32, 32, 100, 64, respectively. The numbers of training
epochs for these baselines are set as 500. The number of samples in
CEVAE in training is set as 5 by default.

Learning Causal Effects on Hypergraphs

KDD ’22, August 14–18, 2022, Washington, DC, USA

√
(a) Linear, 𝜖𝑃 𝐸𝐻 𝐸 , CT

(b) Linear, 𝜖𝐴𝑇 𝐸 , CT

√
(c) Quadratic, 𝜖𝑃 𝐸𝐻 𝐸 , CT

(d) Quadratic, 𝜖𝐴𝑇 𝐸 , CT

√
(e) Linear, 𝜖𝑃 𝐸𝐻 𝐸 , GR

(f) Linear, 𝜖𝐴𝑇 𝐸 , GR

√
(g) Quadratic, 𝜖𝑃 𝐸𝐻 𝐸 ,GR

(h) Quadratic, 𝜖𝐴𝑇 𝐸 , GR

√
(i) Linear, 𝜖𝑃 𝐸𝐻 𝐸 , MS

(j) Linear, 𝜖𝐴𝑇 𝐸 , MS

√
(k) Quadratic, 𝜖𝑃 𝐸𝐻 𝐸 , MS

(l) Quadratic, 𝜖𝐴𝑇 𝐸 , MS

Figure 9: Comparison of the performance of ITE estimation under different settings. “CT", “GR" and “MS" stand for Contact,
GoodReads and Microsoft Teams datasets, respectively.
