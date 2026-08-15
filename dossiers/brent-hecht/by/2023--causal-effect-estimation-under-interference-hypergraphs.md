---
title: "Causal Effect Estimation under Interference on Hypergraphs"
person: brent-hecht
attendance: unconfirmed
section: by
type: journal-article
year: 2023
date: 2023-06-01
venue: "AI Matters"
authors: "Jing Ma, Mengting Wan, Longqi Yang, Jundong Li, Brent Hecht, Jaime Teevan"
source_url: https://doi.org/10.1145/3609468.3609472
fulltext_url: https://content.openalex.org/works/W4387506157.grobid-xml
openalex_id: W4387506157
doi: https://doi.org/10.1145/3609468.3609472
oa_status: bronze
cited_by_count: 0
retrieved: 2026-08-13
content: full-text
notes: "Full text retrieved via the OpenAlex Content API (https://content.openalex.org/works/W4387506157.grobid-xml); no binary stored; text extracted from the GROBID TEI rendering hosted at content.openalex.org"
---

# Causal Effect Estimation under Interference on Hypergraphs

## Full text

Causal Effect Estimation under Interference on Hypergraphs

University of Virginia ;

Causal Effect Estimation under Interference on Hypergraphs

Introduction

Hypergraphs offer a powerful abstraction for representing multi-way group interactions, allowing hyperedges to connect any number of nodes.In contrast to prevailing approaches that focus on capturing statistical dependencies, our research explores hypergraphs from a causal perspective.Specifically, we tackle the problem of estimating individual treatment effects (ITE) on hypergraphs, aiming to determine the causal impact of interventions (e.g., wearing face covering) on outcomes (e.g., COVID-19 infection) for each individual node.Existing ITE estimation methods either assume no interference between individuals or consider interference only among connected individuals in regular graphs.However, such assumptions may not hold in real-world hypergraphs.Recognizing this, we propose a novel causality learning framework HyperSCI by modeling high-order interference on hypergraphs.Through extensive experiments on real-world hypergraphs, we validate the effectiveness of HyperSCI and highlight the potential of causal inference in hypergraphs with complex group interactions. 1

High-order Interference

Group interactions among individuals exist in many scenarios such as massive gathering events.Although the regular pairwise graph definition covers various applications (e.g., physical contact networks) (Fig. 1b), it fails to capture the complete information of group interactions (where each interaction may involve more than two individuals) (Bai et al.,

2021).

Hypergraphs can be introduced to address this limitation by using each hyperedge to connect any number of nodes (Fig. 1a).

The majority of existing studies for hypergraph based machine learning tasks (Bai et al., 2021;Feng et al., 2019) still focus on the statistical correlation level.A key limitation here is the lack of causality, which is particularly important for understanding the impact of a policy intervention (e.g., wearing face covering) on an outcome of interest (e.g., COVID-19 infection).The causal problem is particularly hard on hypergraphs, since the outcome of each individual is not only affected by their own treatment, but also influenced by the treatment of other individuals (e.g., face covering practice of other individuals may affect the target individual through gathering events).

We focus on learning causal effects on hypergraphs.Specifically, we aim to estimate the individual treatment effect (ITE) under hyper-graph interference from observational data.Classic ITE estimation relies on the Stable Unit Treatment Value (SUTVA) assumption (Fisher, 1936;Splawa-Neyman et al., 1990) that there is no interference (i.e., spillover effect) among individuals/instances (also referred to as units in causal inference literature).That means the outcomes for any instance are not affected by the treatment of other instances.This assumption is often impractical in the real world, especially on graphs where the interference is ubiquitous (Ahluwalia et al., 2001;Yilmaz et al., 2002).

Most existing studies of interference (Aronow and Samii, 2017;Basse and Feller, 2018) assume the interference only exists in a pairwise way on ordinary graphs, and are thus insufficient to characterize the high-order interference on hypergraphs.As shown in Fig. 1c, within a gathering event (hyperedge) between u 1 , u 2 and u 3 , an individual's (u 1 ) infection outcome can be affected by the first-order interference from other individuals (u 2 → u 1 and u 3 → u 1 ) as well as the high-order interference from the interactions among other individuals (the interaction between u 2 and u 3 may also act on influencing the exposure of the virus to u 1 ; consequently, u 1 's infection risk can be affected by this second-order interference, i.e., u 2 × u 3 → u 1 ).This demands techniques handling high-order interference, but very little work has studied this area.

Problem Definition Definition

The observational data is {X, H, T, Y}.X = {x i } n i=1 , T = {t i } n i=1 and Y = {y i } n i=1 represent node features, treatment assignments, and observed outcomes, respectively.H = {h i,e } ∈ R n×m is an incidence matrix for hypergraph H. Here, h i,e = 1 if node i is in hyperedge e, otherwise h i,e = 0.The treatment t i is binary.We use H, X, T to denote the random variables for the hypergraph structure, features, and treatment for any node.

Definition 2. The potential outcome (Rubin, 1980) of the unit i (denoted by y 1 i or y 0 i ) is defined as the outcome which would be realized for unit i under treatment t i = 1 or t i = 0.

Our aim is to estimate the ITE for each node i in the hypergraph, which is defined as the difference between the potential outcomes of node i under treatment t i = 1 and t i = 0 with the existence of hypergraph interference.

Proposed Method: HyperSCI

Fig. 2 shows an overview of our framework HyperSCI, which contains three main components: confounder representation learning, interference modeling, and outcome prediction.

Confounder Representation Learning

HyperSCI learns representations of confounders by mapping the node features x i into a latent space with a multilayer perceptron (MLP) module, i.e., z i = MLP(x i ).The confounder representations for all the nodes are denoted by Z = {z i } n i=1 .Similar as (Shalit et al., 2017), a representation balancing method is used to improve the treatment effect estimation performance.

Interference Modeling

An interference modeling module is developed to model the high-order interference among nodes in the hypergraph.A function Ψ(•) is learned via a hypergraph neural network module to obtain the interference representations (p i ) for each node i, i.e., p i = Ψ(Z, H, T -i , t i ).This module is implemented based on a hypergraph convolutional network and a hypergraph attention mechanism (Bai et al., 2021).

To learn the interference representations for each node, the treatment and confounder representations are propagated through the hypergraph structure.The hypergraph convolution operation is defined as:

where L is the vanilla Laplacian matrix for the given hypergraph H, P (l) denotes the representations in the l-th layer of the hypergraph module.W (l+1) denotes the parameter matrix in the (l+1)-th layer of the hypergraph module.

While the hypergraph convolution layer allows for interference modeling through hyperedges, it lacks flexibility to consider the varying significance of interference on different nodes

Outcome Prediction

Representation balancing

Node (treated)

Hyperedge

Node features Confounder representation

Interference representation via different hyperedges.To address this, a hypergraph attention mechanism (Bai et al., 2021) is utilized to capture the intrinsic relationship between nodes and hyperedges.

Outcome Prediction

Based on the confounder representations and the interference representations, the potential outcomes are predicted by:

(2) where f 1 (•) and f 0 (•) are learnable functions.The ITE for each node i is then estimated by: τi = ŷ1

i -ŷ0 i .The prediction for the observed outcome is ŷi = ŷt i i .The final loss function is:

where the first term is the outcome prediction loss, which can be implemented by standard mean squared error.L b is the representation balancing loss.Θ denotes all the model parameters.α and λ are hyperparameters that control the weights for different terms.

Experiments

It is often very hard to obtain the ground-truth counterfactuals as only one of the two potential outcomes can be obtained in the observational data.Hence, we follow a standard practice to evaluate our framework and the alternative approaches on semi-synthetic datasets.We leverage as much real-world information as possible in the simulated environment.Our datasets are all based on real-world hypergraphs, and we retain the treatment allocations as well as node features (covariates) if they are available.We simulate the outcome generation process to assess the true ITEs, which allow us to evaluate the performance of ITE estimation.Full details of the datasets, baselines, and experimental settings can be found in (Ma et al., 2022).

ITE Estimation Performance

The performance of ITE estimation in hypergraph is shown in Fig. 3. HyperSCI outperforms all the baselines under different simulation settings.As for the reasons, Hyper-SCI can leverage the hypergraph structure to model the high-order interference.In this way, it mitigates the influence of the interference on ITE estimation performance.Furthermore, in the simulation, the hyperparameter β controls the level of hypergraph interference in the outcome generation.From Fig. 3, when β increases, the outcome is more strongly affected by interference, and larger performance gains can be observed from HyperSCI compared with the baselines.

Figure 1 :

Figure 1: (a) An example of a hypergraph; (b) An ordinary graph projected from this hypergraph; (c) Interferences with u 1 on the hypergraph.

Figure 2 :

Figure 2: An illustration of HyperSCI.

Figure 3 :

Figure 3: ITE estimation performance under different levels of interference (e.g., varying β).

& ' #&

The moderating role of commitment on the spillover effect of marketing communications

Journal of Marketing research

Ahluwalia, R., Unnava, H. R., and Burnkrant, R. E. (2001). The moderating role of commit- ment on the spillover effect of marketing com- munications. Journal of Marketing research, 38(4):458-470.

Estimating average causal effects under general interference, with application to a social network experiment

The Annals of Applied Statistics

Aronow, P. M. and Samii, C. (2017). Estimat- ing average causal effects under general in- terference, with application to a social network experiment. The Annals of Applied Statistics, 11(4):1912-1947.

Hy-pergraph convolution and hypergraph attention

Pattern Recognition

Bai, S., Zhang, F., and Torr, P. H. (2021). Hy- pergraph convolution and hypergraph atten- tion. Pattern Recognition, 110:107637.

Analyzing two-stage experiments in the presence of interference

Journal of the American Statistical Association

Basse, G. and Feller, A. (2018). Analyzing two-stage experiments in the presence of in- terference. Journal of the American Statistical Association, 113(521):41-55.

Hypergraph neural networks

Proceedings of the AAAI Conference on Artificial Intelligence

Feng, Y., You, H., Zhang, Z., Ji, R., and Gao, Y. (2019). Hypergraph neural networks. In Pro- ceedings of the AAAI Conference on Artificial Intelligence, volume 33, pages 3558-3565.

Design of experiments

Br Med J

Fisher, R. A. (1936). Design of experiments. Br Med J, 1(3923):554-554.

Learning causal effects on hypergraphs

ACM SIGKDD International Conference on Knowledge Discovery and Data Mining

Ma, J., Wan, M., Yang, L., Li, J., Hecht, B., and Teevan, J. (2022). Learning causal ef- fects on hypergraphs. In ACM SIGKDD Inter- national Conference on Knowledge Discovery and Data Mining.

Randomization analysis of experimental data: The fisher randomization test comment

Journal of the American Statistical Association

Rubin, D. B. (1980). Randomization analysis of experimental data: The fisher randomiza- tion test comment. Journal of the American Statistical Association, 75(371):591-593.

Estimating individual treatment effect: generalization bounds and algorithms

ternational Conference on Machine Learning

Shalit, U., Johansson, F. D., and Sontag, D. (2017). Estimating individual treatment effect: generalization bounds and algorithms. In In- ternational Conference on Machine Learning.

On the application of probability theory to agricultural experiments

Statistical Science

essay on principles. section 9

Splawa-Neyman, J., Dabrowska, D. M., and Speed, T. (1990). On the application of proba- bility theory to agricultural experiments. essay on principles. section 9. Statistical Science, pages 465-472.

Geographic and network neighbors: Spillover effects of telecommunications infrastructure

Journal of Regional Science

Yilmaz, S., Haynes, K. E., and Dinc, M. (2002). Geographic and network neighbors: Spillover effects of telecommunications in- frastructure. Journal of Regional Science, 42(2):339-360.
