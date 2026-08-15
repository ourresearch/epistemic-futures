---
title: "Federated Select: A Primitive for Communication- and Memory-Efficient Federated Learning"
person: blaise-aguera-y-arcas
section: by
type: journal-article
year: 2022
date: 2022-08-19
venue: "arXiv (Cornell University)"
authors: "Zachary Charles, Kallista Bonawitz, Stanislav Chiknavaryan, Brendan McMahan, Blaise Agüera y Arcas"
source_url: http://arxiv.org/abs/2208.09432
retrieved: 2026-08-13
content: full-text
notes: "OpenAlex W4292753736 (type: preprint). Full text extracted from the open-access PDF at https://arxiv.org/pdf/2208.09432."
---

# Federated Select: A Primitive for Communication- and Memory-Efficient Federated Learning

## Full text

### Abstract (from OpenAlex metadata)

Federated learning (FL) is a framework for machine learning across heterogeneous client devices in a privacy-preserving fashion. To date, most FL algorithms learn a "global" server model across multiple rounds. At each round, the same server model is broadcast to all participating clients, updated locally, and then aggregated across clients. In this work, we propose a more general procedure in which clients "select" what values are sent to them. Notably, this allows clients to operate on smaller, data-dependent slices. In order to make this practical, we outline a primitive, federated select, which enables client-specific selection in realistic FL systems. We discuss how to use federated select for model training and show that it can lead to drastic reductions in communication and client memory usage, potentially enabling the training of models too large to fit on-device. We also discuss the implications of federated select on privacy and trust, which in turn affect possible system constraints and design. Finally, we discuss open questions concerning model architectures, privacy-preserving technologies, and practical FL systems.

---

Federated Select: A Primitive for Communication- and
Memory-Efficient Federated Learning

arXiv:2208.09432v1 [cs.LG] 19 Aug 2022

Zachary Charles∗1 , Kallista Bonawitz1 , Stanislav Chiknavaryan1 , Brendan McMahan1 , and
Blaise Agüera y Arcas1
1

Google, Inc.

August 22, 2022

Abstract
Federated learning (FL) is a framework for machine learning across heterogeneous client devices in a
privacy-preserving fashion. To date, most FL algorithms learn a “global” server model across multiple
rounds. At each round, the same server model is broadcast to all participating clients, updated locally,
and then aggregated across clients. In this work, we propose a more general procedure in which clients
“select” what values are sent to them. Notably, this allows clients to operate on smaller, data-dependent
slices. In order to make this practical, we outline a primitive, federated select, which enables client-specific
selection in realistic FL systems. We discuss how to use federated select for model training and show
that it can lead to drastic reductions in communication and client memory usage, potentially enabling
the training of models too large to fit on-device. We also discuss the implications of federated select on
privacy and trust, which in turn affect possible system constraints and design. Finally, we discuss open
questions concerning model architectures, privacy-preserving technologies, and practical FL systems.

1

Introduction

Federated learning (FL) is a privacy-preserved distributed learning paradigm. Throughout, we focus on the
specific notion of FL proposed by by (Kairouz et al., 2021),
Federated learning is a machine learning setting where multiple entities (clients) collaborate in
solving a machine learning problem, under the coordination of a central server or service provider.
Each client’s raw data is stored locally and not exchanged or transferred; instead, focused updates
intended for immediate aggregation are used to achieve the learning objective.
FL enables learning effective models across wide populations and varied data sources, while still preserving
the privacy of each individual client. In comparison to other distributed learning frameworks, some challenges
become much more prominent in federated learning, including constraints on communication, client memory
usage, and privacy (Kairouz et al., 2021). Another key facet of federated learning is data heterogeneity.
Clients typically have different distributions and quantities of local data, and learning across these diverse
datasets under the aforementioned constraints can be challenging. In this work, we will focus primarily on
cross-device FL, in which clients are typically edge devices with limits on download bandwidth, storage,
compute, and upload bandwidth (Kairouz et al., 2021, Table 1).
One notable method for performing federated learning is federated averaging (FedAvg) (McMahan et al., 2017).
While many other optimization methods for FL have since been proposed (Reddi et al., 2021; Karimireddy
∗ Correspondence to zachcharles@google.com

1

et al., 2020; Li et al., 2020), many of these can be parameterized in a thematically similar manner. In general,
these methods perform multiple rounds of training, which can roughly be broken down into broadcast, client
training, aggregation, and server update stages. In short, the server possesses a global model that is broadcast
to the clients, which then update the model according to their own data. The resulting local models are
aggregated by the server, and the result of this is used to update its global model.
We now arrive at an important challenge for cross-device FL: While machine learning has moved towards
larger and larger models, especially in natural language processing domains (Dai et al., 2019; Devlin et al.,
2018; Yang et al., 2019; Kaplan et al., 2020; Irie et al., 2019), this movement is predicated on the availability
of hardware with sufficient storage and compute capacity. By contrast, clients in cross-device FL systems
often have limited compute and storage, as well as constraints on the amount of data they can download and
upload. Thus, without any extra modifications, algorithms like FedAvg may require using smaller models
than if we were simply training in a data-center (Ro et al., 2022).
While compression techniques can help reduce communication costs in cross-device settings (Sattler et al.,
2019; Haddadpour et al., 2020; Reisizadeh et al., 2020; Rothchild et al., 2020; Mitchell et al., 2022), they often
do not provide mechanisms for training in more memory-efficient ways. While approaches like knowledge
distillation and student-teacher models have shown great promise in reducing client model sizes (Li and
Wang, 2019), such approaches often require artifacts like public data that may not be present in many tasks.
Similarly, a number of works have validated that partial model training approaches can often allow clients to
only train a much smaller portion of the server model (Ro et al., 2022; Liang et al., 2020; Yang et al., 2022).
However, such approaches still require transmitting the entire server model in full, and as such may simply
not fit in memory on some clients. In general, the approaches above may often communicate the full model
to a client, even parts of the model that are not needed by a given client. For example, a client with sparse
features may only require the portion of the model relevant to those features.
In this work, we explore an algorithmic framework for FL that allows us to train large server models while
enforcing limits on client communication, computation, and storage. Our approach allows the server to train
models far larger than the clients are able to download, train, or upload. We propose a novel primitive we
refer to as federated select. This primitive allows each client to select a sub-model of the server model that
will be used for local training. Notably, these sub-models can be significantly smaller, and therefore are more
amenable to cross-device FL. Moreover, federated select allows clients to select different sub-models, which
can be crucial due to the aforementioned data heterogeneity. This framework is fully compatible with existing
optimization frameworks for FL, as well as communication compression methods.

2

Background

2.1

Federated Computations

In order to formalize the notion of data location in a federated system, we define the concept of federated
values. Our framing and exposition here is building on analogous notions defined first in the TensorFlow
Federated framework (Ingerman and Ostrowski, 2019). Federated values are data hosted across a group of
devices in a distributed system. For our purposes, we will only consider two possible placements of a value:
1. A value located at the (conceptually) singleton server (server-placed). We will use the shorthand x@S
to denote a value x placed at the server.
2. A value located at all clients participating in a computation (client-placed). We model the collection of
values across all available clients as a single federated value. We use the shorthand {x1 , . . . , xN }@C to
denote a a client-placed federated value as where xi is the value held by client i.
Given the above, a federated computation is a function whose inputs and outputs are federated values.
Note that unlike federated values, federated computations do not have an inherent placement. By contrast,

2

non-federated computations can only modify the value, not the placement. When writing non-federated
computations, we will omit the @S and @C designations.
For example, suppose our client devices are all temperature sensors, each with some temperature reading
tn . Then the corresponding federated value is the set {t1 , . . . , tN }@C. The definition of federated learning
suggests that the server cannot access individual values in this set, but can compute aggregates such as the
average temperature across clients. Thus, we may be interested in the federated computation which maps
client-placed temperatures to their server-placed average, that is
!
N
1 X
{t1 , . . . , tN }@C 7→
tn @S.
N n=1
However, clients could first compute some local function f (tn ) of their temperature value (for example,
rounding to the nearest integer) and then take a “federated mean”, which we would denote
!
N
1 X
{t1 , . . . , tN }@C 7→
f (tn ) @S.
N n=1
Note that in this context, f is a non-federated computation, only changing the value of the temperature
readings locally.
This abstraction helps encode the data restrictions in federated learning and understand possible implementations. For example, a federated computation whose inputs and outputs are all placed at the server would
have no need for communication between clients and server, while functions with mixed placement usually
incur some form of communication between clients and server.
In order to describe algorithms that involve clients and a server, we will formalize two standard FL primitives:
Broadcast and Aggregate. Broadcast is simply a federated computation that takes x@S and returns
{x, x, . . . , x}@C. Notably, each client receives the same value under this function. Aggregate effectively
does the reverse. It takes as input {x1 , . . . , xN }@C, and produces some aggregate y@S. For simplicity,
we focus on the specialization of Aggregate that computes the mean over the client values, which we
denote Aggregatemean , but the discussion is valid for many other types of operations. Formally, we define
Broadcast and Aggregatemean via
!
N
1 X
xn @S.
(1)
Broadcast(x@S) = {x, x, . . . , x}@C, Aggregatemean ({x1 , . . . , xN }@C) =
N n=1
While we assume a fixed number of clients N for notational simplicity, in general the server will not know
how many clients actually successfully contributed to a round until after the rounds execution completes, due
to client failures and dropouts, etc. In general, other reduce-like operations could be used for Aggregate,
as could non-linear operations such as applying some robust estimator.

2.2

Federated Model Training

Federated learning methods often aim to learn a global "server model" that minimizes the expected loss of a
function across some (generally unknown) distribution P of clients:
min f (x)

x∈Rs

where

f (x) := En∼P [fn (x)]

where Rs is the model space and fn : Rs → R is the loss function for client n. Due to data restrictions,
clients cannot directly share their loss functions fn . Instead, most methods (including the de facto standard,
FedAvg (McMahan et al., 2017)) operate in the following general manner: The server has a global model x,
which at each round uses Broadcast to send x to some set of available clients (referred to as a cohort (Charles
et al., 2021)). The clients in the cohort use their local loss function fn to compute some model update
un = ClientUpdate(x, fn ).
3

Algorithm 1 Federated Model Training
Input: ClientUpdate, ServerUpdate, T ∈ Z≥1 , x0 ∈ Rs
for t = 1, . . . , T do
Sample a set S t of available clients
for each client n ∈ S t in parallel do
Receive xt via Broadcast
utn = ClientUpdate(xt , fn )
Server receives ut @S = Aggregatemean ({utn : n ∈ S t }@C)
xt+1 = ServerUpdate(xt , ut )
The server then receives the result of Aggregatemean applied to these client updates, which we refer to as
the server update u. Finally, the server uses some subroutine ServerUpdate(x, u) to update its own global
model. Pseudo-code for this procedure is given in Algorithm 1.
For example, in FedAvg, ClientUpdate(x, fn ) is a model produced via E epochs of mini-batch SGD on
the loss function fn , starting from x. The server updates its model to be the average of these locally
updated models, so ServerUpdate(x, u) = u. Note that in realistic settings, clients may drop out during
the computation (Bonawitz et al., 2017), so that the aggregation step may involve a system-dependent set of
clients. We omit this in our discussion for simplicity of notation, but the same training algorithm applies in
this setting.
Generalizations of FedAvg often use a “model-delta” approach. In this, ClientUpdate(x, fn ) is the difference
between x and a model learned by performing E epochs of mini-batch SGD on fn starting from x. Note that
when clients do a single gradient descent step, ClientUpdate(x, fn ) = γ∇fn (x) where γ is the learning rate.
Thus, the average client update u is a kind of approximation to ∇f , and so we can let ServerUpdate(x, u)
be a first-order optimization method, treating u as the gradient (Reddi et al., 2021). This allows the
incorporation of techniques like adaptivity and momentum into the server update.
While often empirically effective (Reddi et al., 2021), Algorithm 1 may not work in settings where the model
x is large. Clients may not be able to receive the model, compute ClientUpdate, or send the corresponding
model update to the server. However, in certain settings, there are natural ways to use a smaller model y in
this training procedure, as we detail below.

2.3

Motivating Example 1 - Logistic Regression with Sparse Features

Suppose that we wish to use Algorithm 1 to perform federated logistic regression where ClientUpdate
is the “model-delta” update discussed above. For simplicity, suppose that each client has a single example
vn ∈ Rs , and that their loss function is fn (x) = σ(hx, vn i) where σ(a) is the logistic loss. In order to perform
Algorithm 1, each client would need to download, store, and compute inner products of s-dimensional vectors.
Let us now assume that for each client n, the example vn is supported on some smaller set of indices An .
Letting πA (x) denote the restriction of a vector x to the coordinates in A, we have
hx, vn i = hπAn (x), πAn (vn )i.

(2)

By linearity, we see that to compute ∇fn (x), the client need only know An and πAn (x). Moreover, ∇fn (x)
can be computed in time |An | which could be significantly smaller than s. Note that in applications like
click-through-rate prediction, it is common to have s ≈ 109 or more, with |An | only a small constant like
100 (McMahan et al., 2013).
For the sake of exposition, let us assume that the server and client both know An , and that ClientUpdate
is some number of SGD steps. To execute Algorithm 1, the server need only send client n the vector πAn (x).
By (2), the client can compute πAn (ClientUpdate(x, fn )), which it can then send back to the server. By
assumption, gradient descent does not change the coordinates outside of An , so ClientUpdate(x, fn ) is 0
at coordinates in the complement of An (as we are using the model-delta ClientUpdate). Thus, the server
4

can take the received πAn (ClientUpdate(x, fn )), fill in zeros in all other coordinates. Thus, we can exactly
recover Algorithm 1, but with a reduction in the download, storage, compute, and upload costs of each client.
In general, we say that this example exhibits fine-grained sparsity; Clients need only operate on a moderatelysized subset of a high-dimensional vector.

2.4

Motivating Example 2 - Conditional and Multi-modal Models

Suppose that we wish to use Algorithm 1 to train models with layers that trigger conditionally depending on
the input, such as “mixture-of-experts” models (Eigen et al., 2013; Shazeer et al., 2017). We may also want to
train multi-modal models, which perform different tasks but with shared representations. For example, Zhu
et al. (2022) propose the use of multi-modal models in the context of federated learning by Zhu et al. (2022)
in order to incorporate temporal modality among clients.
When using such models, a client may only need a small fraction of the model during training, either because
its dataset only triggers a subset of the conditional layers (Zhu et al., 2022), or because it has data relevant to
only a subset of the tasks performed by a multi-modal model (Shazeer et al., 2017). However, in Algorithm 1,
the entire model would need to be broadcast to each client.
In order to avoid this, we would like clients to select which part of the model is relevant to them. Under this
viewpoint, we say that this example exhibits coarse-grained sparsity; The number of components to a given
conditional or multi-modal model are generally much smaller than the number model parameters (eg. on the
order of tens, hundreds, or thousands (Eigen et al., 2013; Shazeer et al., 2017), not millions or billions), and
clients may only need to operate on a small number of them.

3

Federated Select

Generalizing the examples above, we are interested in the following scenario: Suppose we have a cohort of
N available clients (indexed by the set [N ] = {1, 2, . . . , N }). Further suppose there is x@S (with x ∈ X ),
and {z1 , . . . , zN }@C where zn ∈ Z. There is a function ρ : X × Z → Y, and we would like to compute the
federated computation
(x@S, {z1 , . . . , zN }@C) 7→ {ρ(x, z1 ), . . . , ρ(x, zN )}@C.
(3)
In the context of Section 2.3 and Section 2.4, x is the server model, zn is some information that allows client n
to determine which part of x is relevant to its data, and ρ(x, zn ) is some smaller model for client n. However,
the operation in (3) is much more general than in these examples, especially as we impose no restrictions on
the space Z.
For example, one operation that fits under (3) would be some operation that takes a server model x and client
datasets z1 , . . . , zN , and fine-tunes the model on each client’s dataset, sending the result back to the client.
This ambiguity in the space Z being operated on in turn means that implementing (3) in full-generality,
while preserving data privacy of clients, can be challenging for any practical FL system.
In order to discuss realistic and privacy-preserving FL systems, we will consider a special-case of (3) where
the set Z of client values is finite, which we call federated select.
Let K ∈ N, and recall that [K] := {1, 2, . . . , K}. Let ψ : X × [K] → Y be some (non-federated) function,
which we will call the select function. Intuitively, it should be thought of as selecting the k-th component of
x. The server has some value x ∈ X and each client n has a sequence zn = [zn,1 , . . . , zn,m ] ∈ [K]m . These
zn,i are referred to as the client’s select keys.
Federated select is the federated computation that takes x@S, {z1 , . . . , zN }@C, and a selection function ψ, and
whose output is
FedSelect(x@S, {z1 , . . . , zN }@C, ψ) = {[ψ(x, zn,1 ), . . . , ψ(x, zn,m )] : n ∈ [N ]}@C.
5

(4)

Server model

Client select
keys

Client models

Figure 1: A graphical representation of federated select. In this setting, the clients’ select keys correspond to
rows of the server model, which are then sent to the clients. Note that 1) clients can have overlapping keys,
2) the order of the client keys is respected by FedSelect, and 3) the select function ψ(x, z) simply picks out
the z-th row of x. More sophisticated usages of FedSelect could also transform the items being selected.
A graphical representation of FedSelect is given in Figure 1. Note that (4) is the special-case of (3) where
ρ(x, zn ) = [ψ(x, zn,1 ), . . . , ψ(x, zn,m )]. Notably, this limits the scope of possible ρ to functions that have
this key-structure as in ψ. By restricting this scope, we are able to better ensure that FedSelect can be
computed in realistic FL systems. In fact, as we will see below, (4) has a number of possible implementations,
each with different levels of privacy and communication.
While we suppose that all clients have m keys for notational simplicity, in reality clients could have varying
numbers of keys. This is in fact another benefit of FedSelect. In settings where devices have heterogeneous
memory and computation power (eg. high-end and low-end mobile phones), we can use FedSelect to send
models of different sizes to different clients.
Conceptually, FedSelect is a federated analog of gather-type primitives in machine learning (such as
tf.gather in TensorFlow and torch.index_select in PyTorch). These operations are often used by models
with sparse structure, such as in looking up values in an embedding layer. However, FedSelect allows more
generality, by allowing transformations of the gathered data (rather than just restricting to sparse access).

3.1

Motivating Examples, Revisited

We now discuss how FedSelect can be applied in the examples of Sections Section 2.3 and Section 2.4.

6

Sparse logistic regression. Recall that in this example, the server has a logistic regression model x ∈ Rs ,
and each client has a single example vn supported on a set An ⊆ [s]. For simplicity, we will assume |An | = m,
but this is not strictly necessary. In this case, the client’s select keys zn are simply the set An in order
as a sequence, and the function ψ(x, i) := xi . In this case, FedSelect(x@S, {z1 , . . . , zN }@C, ψ) computes
{πA1 (x), . . . , πAn (x)}@C, that is, the restriction of x onto the coordinates in zn for each client. In other words,
FedSelect specializes to projecting x onto each client’s coordinate subspace.
Conditional and multi-modal models.
In this setting, we assume that we have a server model x
with a shared component, and C conditional components (eg. components for each possible task of a multitask model). Let x = (a1 , . . . , aC , b) where a1 , . . . , aC are the conditional components and b is the shared
component. The selection key space will be [C + 1], and the selection function ψ is defined as ψ(x, i) = ai if
i ∈ [C] and ψ(x, C + 1) = a. A client’s select keys are the elements of [C] indexing the conditional components
relevant to the client, plus an extra key of C + 1. Note that this key is used by all clients since it corresponds
to the shared component. Under this setup, FedSelect will exactly send to each client the conditional
components relevant to the client, along with the shared component.
We note that this implicitly assumed that the client could determine the relevant conditional components
of a model, without access to the global model. While this may not be true in general, for many models,
especially multi-modal models, the conditional components correspond to what types of data are present in a
client’s dataset. For example, a language model with different components for different languages could apply
in this setting, as the client can reasonably know which languages are present in its local data.

3.2

Possible Implementation of Federated Select

We now discuss possible ways to compute (4) in an actual federated system. Here we will outline their various
trade-offs, especially trade-offs between communication-efficiency and privacy. For more detail and a greater
focus on systems challenges of these implementations, see Section 6. While each implementation has a variety
of pros and cons, we will specifically focus on the communication and computation costs of each method.
While we briefly mention the privacy trade-offs of each implementation, we discuss this in greater detail in
Section 6.
Option 1: Broadcast and compute on clients. In this implementation, the server would simply
broadcast x in full to the clients. Each client n then computes [ψ(x, zn,1 ), . . . , ψ(x, zn,m )] locally. This
method fully preserves the privacy of the clients’ select keys (as they never leave the device), but can
incur high communication costs. In particular, there is no reduction in communication costs compared to
Broadcast(x@S).
Option 2: On-demand slice generation. In this implementation the clients would first upload their
select keys to the server. The server can then directly compute (4), and send each client their resulting values.
Effectively, the server would function as an on-demand service for computing FedSelect according to inputs
uploaded by the clients. This can reduce communication costs (as the server need not send its model in full),
but on-demand computation may lead to wasted computation effort if many clients are selecting the same
key (e.g. if K is comparable to the number of clients), or else may require a more complicated distributed
caching system to avoid such re-computation. Additionally, increased care must be given to privacy risks in
this implementation, as the slice computation server will have access to the client selection keys. For greater
discussion of this, see Section 6.
Notably, both of the implementation options above could also be used to compute (3). However, they both
come with significant downsides, both in terms of systems constraints and privacy constraints. Thus, we
consider a third implementation that relies on the space of possible select keys being of moderate size (and
notably, finite, as in (4)).

7

Option 3: Pre-generation of slices. In this implementation, the server would, before a given round of
training, compute all ψ(x, k) for all k ∈ [K]. It would send the values to some high-capacity content delivery
network (CDN). In order to compute (4), each client would simply query the content delivery network with
their own select keys. In the case where most keys are selected by multiple clients, this implementation will
minimize the computation cost (without need for a distributed cache or similar technique). However, if the
space of keys is much larger than the number of clients, this implementation will waste significant compute
resources computing unnecessary values of ψ(x, k). As in Option 2, the CDN will be able to see each client’s
key, and so care must be given to the privacy implications. Again, see Section 6 for more details.

3.3

Relationship to Other Primitives

Up to this point, we have introduced two general primitives for server-to-client communication in FL systems:
Broadcast (1) and FedSelect (4). In this section we briefly discuss the relation between these and other
possible operations.
First, we note that FedSelect is strictly more general than Broadcast. To see this, suppose that we
wished to compute Broadcast(x). This can be done via FedSelect simply by letting the select function
be ψ(x, k) = x and having each client select any single key, for example, 0. Then (4) simply becomes
FedSelect(x@S, {0, . . . , 0}@C, ψ) = {ψ(x, 0), . . . , ψ(x, 0)}@C = {x, x, . . . , x}@C.
Next, we note that in many examples, there are components that we would like to apply FedSelect
to, and others that we would like to apply Broadcast to; for example, we may simultaneously want to
compute FedSelect(x@S, {k1 , . . . , kN }@C, ψ) and Broadcast(y@S). In this case, we can combine the two
operations into a single FedSelect, using the tuple (x, y) as the model. That is, we could execute a single
FedSelect((x, y)@S, {k1 , . . . , kN }@C, ψ 0 ) operation, defining
ψ 0 ((x, y), k) = (ψ(x, k), y)
Similarly, we note that two applications of FedSelect can be merged, even if they operate on different key
spaces. Suppose we wish to compute
(1)

(1)

kn(1) ∈ [K (1) ]

(2)

(2)

kn(2) ∈ [K (2) ]

m(1) = FedSelect(x(1) @S, {k1 , . . . , kN }@C, ψ (1) );
m(2) = FedSelect(x(2) @S, {k1 , . . . , kN }@C, ψ (2) );

We can replace these two instances of FedSelect with a single FedSelect operating on a keyspace
[K (1) ] × [K (2) ]:
(1)

(2)

(1)

(2)

(m(1) , m(2) ) = FedSelect((x(1) , x(2) )@S, {(k1 , k1 ), . . . , (kN , kN )}@C, ψ 0 )
defining1 :

ψ 0 ((x(1) , x(2) ), (k (1) , k (2) )) = (ψ (1) (x(1) , k (1) ), ψ (2) (x(2) , k (2) ))

Finally, we note that applying FedSelect with multiple keys can be subsumed by a select call where each
client has a single key. To see this, suppose that each client has m keys zn = [zn,1 , . . . , zn,m ] that it would
like to use in FedSelect (with select function ψ), with each key in [K]. We can simply order all possible
sets of this form, so that client n has a single key zn0 ∈ [K m ] representing this ordered sequence. By defining
ψ 0 (x, zn0 ) accordingly, then we have
0
FedSelect(x@S, {z1 , . . . , zN }@C, ψ) = FedSelect(x@S, {z10 , . . . , zN
}@C, ψ 0 )

where each zn0 is a single key instead of m keys. While conceptually useful, this may be inefficient from a
systems standpoint, particularly with respect to pre-generation of slices where it might require K m slices
instead of K.
1 In order to maintain an integer keyspace, we can interpret (k (1) , k (2) ) as an integer in mixed-radix notation, in [K (1) · K (2) ]

8

Algorithm 2 Federated Model Training with Federated Select
Input: ClientUpdate, ServerUpdate, T ∈ Z≥1 , x0 ∈ Rs
for t = 1, . . . , T do
Sample a subset S t of available clients
for each client n ∈ S t in parallel do
t
t
Choose select keys znt = [zn,1
, . . . , zn,m
] ∈ [K]m
t
t t
t t
Receive yn = [ψ(x , zn,1 ), . . . , ψ(x , zn,m )] via FedSelect
utn = ClientUpdate(ynt , gn )
Server receives ut @S = Aggregate?mean ({utn : n ∈ S t }@C, {znt : n ∈ S t }@C, φ).
xt+1 = ServerUpdate(xt , ut )

4

Model Training with Federated Select

We now re-focus our attention on federated model training. In particular, we would like to incorporate
FedSelect into Algorithm 1, in order to improve communication-efficiency and client memory usage. Recall
that in Algorithm 1, we assume that given a model x ∈ Rs and some loss function fn : Rs → R, each client
can compute ClientUpdate(x, fn ) ∈ Rs .
We now assume that s is sufficiently large such that x ∈ Rs does not fit on client devices. Instead, let us
assume that we have some select function ψ such that given select keys [zn,1 , . . . , zn,m ] for client n, the vector
yn = [ψ(x, zn,1 ), . . . , ψ(x, zn,m )] is an element of Rc where c  s. In other words, the result of FedSelect
produces a smaller c-dimensional vector. Note that in full generality, there could also be components of the
model x that are broadcast to the client without the use of FedSelect.
Analogous with Algorithm 1, we will assume that each client also has a loss function gn : Rc → R, and can
compute a local update un = ClientUpdate(yn , gn ) ∈ Rc . However, we must now take pause. Recall that
in Algorithm 1, the server receives the average of all the client updates. With FedSelect, averaging the
client model updates may no longer be meaningful, as they can correspond to updates to different parts of
the model.
In order to actually update the server’s model, we will need a kind of inverse to FedSelect in (4). Motivated
by the aggregation step in Algorithm 1, we assume that there is a “deselection” function φ : Rc × [K]m → Rs
mapping a “small” model and some selection keys to a large model. We can then extend Aggregatemean to
take the deselection function φ as an argument, computing:
!
N
1 X
?
Aggregatemean ({u1 , . . . , uN }@C, {z1 , . . . , zN }@C, φ) =
φ(un , zn ) @S.
(5)
N n=1
Just as with the specialization of Aggregate in (1), the use of averaging here is not strictly necessary; any
Aggregate function can be similarly extended. Once the server receives the s-dimensional update to its own
model from Aggregate?mean , it can use then use with ServerUpdate (as in Algorithm 1). Putting this all
together, we can perform model training with federated select. Pseudo-code for this is given in Algorithm 2.
We note a few immediate advantages to this framework:
• When c  s, this can reduce memory and computational costs on clients substantially.
• The reduction in communication can be used in tandem with compression methods in order to further
reduce communication. For example, we could use a select function ψ in (4) that extracts some index
from x and then applies quantization.
• This approach can be immediately integrated with other existing ClientUpdate (which uses SGD with
an extra proximal term) or first-order optimization in ServerUpdate (as in methods like FedAdam).

9

4.1

Applying Algorithm 2

While Algorithm 2 gives a general framework for applying FedSelect for model training, it is not immediately
clear how best to apply it to specific machine learning models of interest. In this section, we detail a few
possible approaches. These are corroborated by empirical evaluation in Section 5.
For expository purposes, we assume that each client has some finite set of examples Dn , and their loss
function gn is of the form
1 X
gn (y) =
`(y; q)
(6)
|Dn |
q∈Dn

where `(y; q) is the loss of the local model y on the example q. We will also let ClientUpdate(y, gn ) = y − y 0 ,
per the “model-delta” approach discussed in Section 2.2. In particular, for the remainder of this work, we
will let ServerUpdate(x, u) be a first-order optimization step treating u as a gradient estimate, with some
server learning rate η.
Given the above, we will discuss how to use FedSelect to give clients small sub-models of a server model.
Typically, we do this by applying FedSelect to some of the largest layers of a model, while broadcasting
the other layers in full. For example, when training a logistic regression model, we typically only apply
FedSelect to the dense weight matrix, not the bias vector (as it is comparatively small).
With this in mind, there are two primary ways to apply FedSelect to a model. In the first, which utilizes
structured select keys, clients choose their select keys based on their local datasets Dn . In the second,
which utilizes random select keys, clients select their keys randomly from the set [K] of all possible keys.
We discuss the motivation and examples of these two paradigms below, as well as a paradigm that uses both.
4.1.1

Structured Select Keys

First, we revisit the example in Section 2.3. In that example, Dn contains a single vector vn that is supported
on some set of indices An . Thus, one natural approach to FedSelect would be to have each client use these
support indices as their set of select keys, and select the weight sub-matrix corresponding to this index set.
More generally, if Dn has sparse feature vectors, then clients could total the frequency of each feature and
use the most frequently occurring feature indices as their set of select keys. We will explore this empirically
in Section 5.2.
From a modeling perspective, this approach is relevant to any model whose first layer is a fully-connected
layer (which of course includes logistic and linear regression models). It is also relevant to models with sparse
embedding layers, such as the kind often employed by language models. In such models, the inputs are often
sequences of integer tokens, each of which is mapped into some higher-dimensional space. If Dn only contains
a subset of all possible words in the embedding layer’s vocabulary, then this same approach can be used to
select the portion of the embedding layer relevant to the client’s dataset.
We note that structured select keys may also be relevant to a model’s output layer. For example, if a model’s
output layer has a discrete set of possible outcomes (such as when applying softmax) and a client can discern
that its possible outputs are only a small subset of this, then FedSelect could also be used to select the
relevant component of the output layer. For example, if we are performing next-word prediction with a
model whose input layer is an embedding layer, then the set An of words in a client’s dataset Dn can be used
for applying FedSelect to the input and output layers. Notably, unlike the input selection, sub-sampling
outputs in a softmax layer actually changes the behavior of the network, though this can potentially be
alleviated via softmax subsampling (Waghmare et al., 2022).
4.1.2

Random Select Keys

Unfortunately, in many modeling settings there is no sparse structure to harness for FedSelect. For example,
in computer vision tasks the inputs typically do not have native sparse structure. When using a CNN for

10

instance, we may wish to apply FedSelect to the filters in a convolutional layer. Unlike in Section 4.1.1, it
is not clear a priori how a client could choose which filters are relevant to them without accessing the model.
In such settings, we can instead have clients select their keys randomly from the set [K] of all possible keys.
In effect, clients use FedSelect to obtain a random sub-model of x. This approach is analogous to that of
Federated Dropout (Caldas et al., 2018), though differs in that the modeler can pick how the select keys
correspond to sub-models.
Notably, we have not specified how clients choose keys in relation to one another. While clients could select
keys independently, we may also want to choose one set of random keys per round and have all clients in that
round use that same set. We explore random key selection, and whether clients choose keys independently or
not, empirically in Section 5.3.
4.1.3

Combining Structured and Random Keys

While the discussion above appears to delineate structured and random keys, in many cases we may wish
to apply both to a model. While structured keys can be more useful than random keys when they can be
applied (as we have no extra variance incurred), many models have components not amenable to structured
keys (such as internal layers with no sparse structure in their input and output). Thus, FedSelect with
structured keys may not be enough by itself to reduce the server model size sufficiently. In many realistic
models we would like to apply both. We will explore this in the context of training a transformer model for
next-word prediction in Section 5.4.

4.2

Sparse Aggregation and Privacy Considerations

Aggregations in federated systems typically represent the most privacy-sensitive flow of information from client
devices towards the server, and thus are crucial privacy-preservation opportunities. Federated systems typically
ensure that the updates from clients are held only ephemerally (Bonawitz et al., 2019), but significant effort
has gone into enhancing the formal privacy properties of aggregations, both through the use of cryptography
(in the form of secure multiparty computation, e.g. the Secure Aggregation protocol (Bonawitz et al., 2017;
Bell et al., 2020)) and through the use of secure enclaves (Mo and Haddadi, 2019; Huba et al., 2022).
Existing FL systems have typically focused their privacy-preserving aggregation efforts on the computation of
sums of dense vectors2 . However, when aggregating in the context of a deselection function (e.g., when using
Aggregate?mean as defined in Section 4) the operation looks much more like a sparse aggregation: each key
selects a sub-model of the full model to which to apply the model update. In some settings, especially when
clients have structured select keys (see Section 4.1.1), we would like to perform this sparse aggregation while
ensuring that both the model updates and the selection keys are not visible to the server.
Similarly to the options for FedSelect implementations presented in Section 3.2, a variety of options present
themselves for aggregation with deselect. One could simply apply the deselection function at the client, then
use standard dense aggregation function; this would directly inherit the privacy properties of the the system’s
dense aggregation function, and would protect the privacy of the selection keys (up to the limit of what could
be learned from the aggregate value itself). However, this strategy is typically communication-inefficient as it
entails sending an update the size of the full (pre-selection) model.
Instead, it should be possible to extend the implementations of the cryptographic and/or enclave-based
private aggregation protocols (such as secure aggregation (Bonawitz et al., 2019)) to directly accept (key,
update) pairs and incorporate the application of the deselection function inside the security boundary (i.e.
computing it as part of the cryptographic protocol or inside the secure enclave). While such strategies holds
the promise of improving the communication-efficiency of Aggregate?mean to match that of FedSelect
while maintaining their security properties, we leave the specifics of their implementation as a topic for
2 Notably, the same is not true of federated analytics (FA). Many recent FA works have focused on privacy-preserving mechanisms

for non-linear or sparse aggregates of user data. This includes work on private heavy hitters (Zhu et al., 2020), which
involves estimating the most frequent items across users, and data queries with inherently sparse structure, such as location
heatmaps (Bagdasaryan et al., 2021).

11

Table 1: Dataset statistics.

Dataset
EMNIST
Stack
Overflow

Train
Clients

Train
Examples

Validation
Clients

Validation
Examples

Test
Clients

Test
Examples

3,400

671,585

N/A

N/A

3,400

77,483

342,477

135,818,730

38,758

16,491,230

204,088

16,586,035

future works. Notably, recent work has already proposed the use of invertible Bloom lookup table for secure
aggregation in order to deal with inherently sparse structure (Bell et al., 2020), as could occur in federated
select settings.

5

Experiments

We wish to understand whether (and by how much) training with federated select can actually reduce client
model sizes, while still learning a global model with good accuracy. In order to study this, we perform an
evaluation of federated select across 4 tasks, using 2 distinct datasets. In this section, we focus on the Stack
Overflow dataset. Along the way, we will discuss how selection occurs in each example.

5.1

Experimental Setup

Datasets. We use two datasets: Stack Overflow (TFF, 2019) and EMNIST (Cohen et al., 2017). In the
former, clients are users on the Stack Overflow forum, and their examples consist of their posts. In the latter,
clients are authors of hand-written digits. The number of train, validation, and test clients (along with the
total number of examples in each split) is given in Table 1.
Implementation and tuning. We use Algorithm 2 to do the training. We let ClientUpdate(y, g) = y 0 −y
where y 0 is the model learned by doing one epoch of training via SGD with learning rate γ using the client’s
local dataset (assuming g is of the form (6)). We let ServerUpdate(x, u) be a first-order optimization step
using either SGD, Adagrad, or Adam with learning rate η. We refer to the combination of SGD at the clients
and SGD, Adagrad, or Adam at the server as FedAvg, FedAdagrad, and FedAdam respectively, as proposed
by Reddi et al. (2021) (though our training is more general due to the use of FedSelect).
In each round of Algorithm 2, we sample we sample 50 clients uniformly at random without replacement
from the set of training clients. When running multiple trials of two different algorithms, we use different
random model initializations, and vary which clients are sampled in each round in a pseudo-random manner
(so that across the same trial, both algorithms see the same sequence of clients), as this helps control for
variance across algorithms.
We tune client and server learning rates γ, η over {10i | − 3 ≤ i ≤ 1}. This tuning is done without using
FedSelect, and we pick the parameters that maximize the average validation performance over 5 random
trials. Since EMNIST does not have a built-in validation split, we reserve 20% of the training clients for
held-out validation when tuning. For Stack Overflow, we use the built-in split provided by TensorFlow
Federated (Ingerman and Ostrowski, 2019).
Presentation of results. We run 5 random trials for each experiment discussed below, using the learning
rates tuned without FedSelect. These trials vary the model initialization and which clients are sampled
per round. In all figures, dark lines indicate the mean across the 5 trials, and shaded regions indicate the
standard deviation across trials.
12

Validation Recall@5

0.75 Server Vocab Size (n) = 10000 Server Vocab Size (n) = 50000 Server Vocab Size (n) = 100000
0.70

Client Vocab Size (m)

0.65

100
1000
10000

0.60
0.55
0.50

0

500

1000

1500

Communication Rounds

0

500

1000

1500

Communication Rounds

0

500

1000

1500

Communication Rounds

105

5 × 105

106

10 3

10

10 2

72

10

10 1

Test Recall@5
65.03 66.32 66.37
67.71 70.12 70.29

68

67.39 69.99 70.23

66

10

1.000 0.200 0.100

100

Client
Vocab
Size 3(m)
5
4

10

10

0.100 0.020 0.010

Client
Vocab
Size 3(m)
5
4

Relative Model Size
0.010 0.002 0.001

10

Figure 2: Validation recall@5 for Stack Overflow tag prediction with federated select. We use FedAdagrad
and vary the server vocabulary size n and the number of select keys per client (m). Clients pick the m most
frequently occurring words in their local datasets.

Server Vocab Size (n)

105

5 × 105

106

70

64

Server Vocab Size (n)

(a) Relative model size of client and server.

(b) Test recall.

Figure 3: Relative model size and test recall tag prediction using FedSelect. We vary the server’s vocabulary
size n as well as the number of select keys per client m. Clients pick the m most frequently occurring words
in their local datasets.

5.2

Structured Select Keys

In this section, we will use structured select keys to train a logistic regression model whose inputs are
sparse feature vectors. Specifically, we will apply multi-class logistic regression models (with one-versus
rest classification) to the task of predicting tags in the Stack Overflow datasets. The input data are binary
indicator bag-of-words vectors for each example in a client’s dataset. We restrict the server’s model to the
n most frequently occurring words across the entire dataset, and the t = 500 most frequent tags. We use
FedAdagrad as the server optimizer.
As outlined in Section 4.1.1, clients can use FedSelect to select a sub-matrix of the logistic regression
weight matrix corresponding to some subset of size m of the total vocabulary set of size n. Clients choose
their select keys to be the m most frequently occurring words in their local dataset. The validation recall
across communication rounds for varying m is given in Figure 2, while the final test recall is given in Figure 3
along with the ratio of the client model size to the server model size. Note that when m = n, we recover
model training without the use of FedSelect.
While m = 100 select keys leads to reduced accuracy, we see little to no gain by increasing m from 103 to
104 . In particular, using FedSelect can lead to a 10× reduction in client model size without adversely
13

Validation Recall@5

0.75 Server Vocab Size (n) = 10000 Server Vocab Size (n) = 50000 Server Vocab Size (n) = 100000
0.70

Key Sampling

0.65

Top k
Random Top k
Random k

0.60
0.55
0.50

0

500

1000

1500

Communication Rounds

0

500

1000

1500

Communication Rounds

0

500

1000

1500

Communication Rounds

Figure 4: Validation recall for Stack Overflow tag prediction with federated select. We use FedAdagrad and
vary the server’s vocabulary size (n) and set the number of select keys per client (m) to 1000. Clients use
different methods for choosing their select keys.
affecting accuracy. Particularly notable is the case where n = 104 , as setting m = 104 recovers training
without FedSelect. Analyzing Figure 3, we see another important observation: If we fix the number of
select keys m, we can generally increase the server’s vocabulary size n to increase accuracy, without affecting
client compute costs.
Ablation: Key selection strategies.
One natural question that arises is whether we can improve the
client key selection method over selecting the most frequent words (which we refer to as “Top”). To that
end, we try two other simple approaches. In the first (Random), clients randomly choose m select keys
from the set of words in their own vocabulary. In the second (Random Top), clients identify the 2m most
frequently occurring words in their vocabulary, and randomly use m keys from this set. Note that in contrast
to selecting the m most frequent, these other two methods allow clients to use different keys at different
rounds of training. We compare these methods in Figure 4.
While all three methods eventually reach comparable accuracy levels, we note that Top k strictly dominates
the other two in performance across rounds. Moreover, we find that while all methods have a significant
amount of variance, the variance in the Random k method persists throughout training, and is generally
larger than the variance of the other two methods. Finally, we note that Random Top k offers little to no
benefit over Random k, suggesting that the importance of a word to a client is somewhat strongly correlated
with its frequency.

5.3

Random Select Keys

In this section, clients use random keys to apply Algorithm 1 to image classification on the EMNIST dataset.
We try two different models, both extracted from the original work on FedAvg (McMahan et al., 2017): A
convolutional model (CNN) with two convolutional layers, and a densely-connected network with two hidden
layers (2NN). For the CNN model, the model size is dominated by the second convolutional layer, which
has 64 filters. We apply FedSelect to these filters, having each client select m of these filters randomly
(without replacement). For the 2NN model, the model size is dominated by the first dense layer, which has
200 neurons. We apply FedSelect to these neurons, where each client selects m neurons randomly (also
without replacement).
For both of these models, we vary m and plot the test accuracy throughout the course of training in Figure 5,
and the final test accuracy along with relative client-to-server model size in Tables 2 and Table 3. We see that
the impact of FedSelect varies significantly across the two model architectures. While many settings of m
obtain relatively good accuracy for the CNN model, accuracy drops precipitously with m for the 2NN model.

14

0.8

0.6

Select Keys (m)
4
8
16
32
64

0.4
0.2
0.0

0

500

Test Accuracy

Test Accuracy

0.8

0.6

10
50
100
200

0.4
0.2
0.0

1000 1500 2000

Select Keys (m)

Communication Rounds

0

500

1000 1500 2000

Communication Rounds

Figure 5: Test accuracy of the CNN model (left) and 2NN model (right) on EMNIST when training with
FedSelect, using m randomly chosen select keys per client.
Table 2: Final test accuracy and relative model
size when applying FedSelect to the CNN model.
Clients select m filters randomly (out of 64 total)
from the second convolutional layer.

m

Test Accuracy

Rel. Model Size

4
8
16
32
64

75.02 ± 0.92
81.92 ± 0.10
84.15 ± 0.12
85.66 ± 0.15
86.71 ± 0.06

0.08
0.14
0.26
0.51
1.00

Table 3: Final test accuracy and relative model
size when applying FedSelect to the 2NN model.
Clients select m neurons randomly (out of 200 total)
from the first hidden layer.

m

Test Accuracy

Rel. Model Size

10
50
100
200

14.17 ± 0.78
50.61 ± 0.93
63.97 ± 0.32
74.93 ± 0.13

0.11
0.30
0.53
1.00

Ablation: Independent key selection.
We also wish to see whether clients need to sample their keys
independently. If we were to randomly select a single set of selection keys each round, and have all clients
in the round use that same key set, then there would be no need to actually use FedSelect. Rather, the
server could randomly choose the keys, compute the appropriate sub-model, and simply apply Broadcast.
In Figure 6, we compare the test accuracy of model training with FedSelect when we clients use the same
keys per round (ie. they use some “fixed” set of keys per round) or clients use different keys per round. We
find that the difference in performance between these two approaches depends on the model architecture.
While fixing the set of keys yields no real loss of accuracy on the CNN model, it further drops accuracy on
the 2NN model.

5.4

Structured and Random Select Keys

In this section, we give a more complex example of using structured and random keys in FedSelect. We
use a transformer model to perform next-word prediction on the Stack Overflow dataset. Specifically, we use
the same transformer model architecture used in Wang et al. (2021). The model takes sequences (of length
20) of tokenized words, with a vocabulary size of n = 10000. The model uses an embedding layer followed by
a transformer model, followed by a final dense layer with n = 10000 output units, followed by a softmax. We
use FedAdam for our optimization throughout.
First, we can apply structured key selection to the input and output layers, based on the m most frequently
occurring words in a client’s dataset (as we did in Section 5.2). In order to further reduce the model size,
we can also apply FedSelect with d random keys to the largest dense layer in the transformer, which has
h = 2048 neurons.

15

4
8
16
32
64

0.6
0.4

Fix Keys Per Round

0.2
0.0

0.8

Select Keys (m)

0

500

1000 1500 2000

Test Accuracy

Test Accuracy

0.8

False
True

Select Keys (m)

0.6

10
50
100
200

0.4

Fix Keys Per Round

0.2
0.0

Communication Rounds

False
True

0

500

1000 1500 2000

Communication Rounds

Test Accuracy

Figure 6: Test accuracy of the CNN model (left) and 2NN model (right) on EMNIST when training with
FedSelect, using m randomly chosen select keys per client. Either all clients use the same select keys per
round (True) or independently sample their own keys at each round (False).

0.23
0.22
0.21
0.20
0.19
0.18
0.2

Select Keys

structured
random
mixed

0.4

0.6

0.8

Relative Model Size

1.0

Figure 7: Test accuracy for Stack Overflow word prediction with FedSelect when training using FedAdam,
under structured, random, and mixed selection schemes. We plot the test accuracy with respect to the model
size used by the clients during training.
We parameterize our experiments by a factor α determining the number of structured and random keys used,
with three different types of selection mechanisms. In our structured experiments, we use m = αn structured
select keys per client (applied to the input/output layers), and do not use random keys. In our random
experiments, we use d = αh random keys per client (applied to the dense layer) and do not use structured
keys. Finally, in the mixed experiments, we use m = αn structured select keys and d = αh random keys
simultaneously. Note that in all three cases, α = 1 we recover model training without FedSelect. Moreover,
for the same value of α, all three approaches lead to a different model size.
In Figure 7, we plot the trade-off between test accuracy and client model size incurred by each method.
Notably, purely random key selection drops off in accuracy very quickly, without incurring significant model
size reduction benefits. While structured maintains accuracy better as model size shrinks, there is a limit
to how much the model size can be reduced. Notably, by using the mixed approach, we are able to recover
comparable accuracy to the structure selection for large α, but extend the frontier of test accuracy versus
model size for smaller α.

16

6

Trust Models and System Constraints

The actual benefits (and costs) incurred by using FedSelect will necessarily depend on the surrounding FL
system. While some of these trade-offs were discussed briefly in Section 3.2, in this section we give a more
detailed and systems-oriented viewpoint of implementing FedSelect. We focus on the relation between
systems implementations and the trust model between clients and server.
Privacy is a broad concept, and for this discussion it is useful to highlight two privacy principles in particular:
data minimization and data anonymization (Bonawitz et al., 2022). In the context of a federated computation,
data anonymization involves ensuring that the final output of the computation revealed at the server does not
itself reveal private information. For example, it can help ensure that a language model does not memorize
one user’s data, or that an analytics query does not reveal information about an individual. These concerns
are often addressed by differential privacy (Dwork, 2008), but are generally out-of-scope for this work.
In contrast, data minimization involves the properties of the system that runs a federated computation. In
particular, it suggests that such a system should minimize access to any intermediate state of the computation
to all parties including the service provider. Thus, an implementation of federated select held to the highest
standards of data minimization should not reveal the select keys of any client to the service provider, as these
are internal to the computation and not a designated output (e.g., the model being trained).
Recall that FedSelect requires clients to specify their own select keys. Above, we saw examples where the
select keys were purely random, as well as instances where the select keys contained information about the
client’s local dataset (such as which words frequently appear). This leads us to a core observation: Depending
on how FedSelect is used, the select keys may be more or less private. The sensitivity of a client’s select
key is not simply binary (public or fully private), even when using structured keys that reflect information
about a client’s dataset. For example, select keys codifying the most frequent languages used by a client,
while still derivative of a client’s sensitive data, may be less sensitive than, for example, keys indicative of the
actual content written in a messaging application.
We now consider the problem of implementing FedSelect in a way that 1) allows reduced communication
between clients and server, 2) scales to large-scale FL settings, and 3) allows some data minimization and
privacy-preserving techniques to be applied. We note that Option 1 in Section 3.2 does not fit criteria 1, as it
still requires the server value to be broadcast in full. Thus, we will focus on Options 2 and 3 in Section 3.2,
wherein clients are sent slices either via on-demand slice generation or pre-generation of slices.
On-Demand Slice Generation In this system, clients upload their select keys directly to the server. As
the clients upload their keys to the server, the server computes and packages up the relevant model slices,
and sends them to each client. While this does allow reduced communication between the server and the
clients, this approach can suffer from privacy and systems issues.
In particular, suppose that we want a system that can handle communication rounds with thousands of
clients. Even if the clients use a modest number of select keys on average (ie. m is small), this means that
the server has to compute the selection function ψ(x, i) thousands of times before being able to send all
clients their models. Furthermore, synchronous cross-device FL systems typically have execution patterns
where the clients are coordinated to start rounds at the same time and where the clients only have limited
time-windows in which they participate, and are prone to dropping out of a round. That makes it likely for
the clients to upload their keys and request slices all at nearly the same time, which puts a peak demand on
throughput of the on-demand slice generation. If the server model is stored in only a single place, the slice
generation is likely to become a bottleneck leading to clients running out of their time-window and dropping
out. And while it is possible to distribute the model over multiple places and parallelize on-demand slice
generation requests, that by itself has a cost of replicating a potentially large model. This is a challenging
system task, and can lead to significant latency and throughput issues.
This approach also reveals the clients’ select keys to the server in full, thus assuming that the keys are not
entirely private. In order to remedy this, we could also utilize data minimization techniques, though these
will not suffice for totally private keys. While one might consider using systems like private information
17

retrieval (PIR) (Chor et al., 1995), these often require some finite database of possible values and are not
directly compatible with on-demand slice generation. PIR may be more amenable to slice pre-generation
approaches, as we detail below.
In short, on-demand slice generation are a natural method for computing FedSelect, but can suffer from
systems-issues in cross-device settings, and does not directly permit the use of cryptographic primitives for
keeping client keys private.
Pre-Generation of Slices When the space of select keys (of size K) is not too large, pre-generation of
slices can remedy some of the issues of on-demand slice generation. In particular, we consider scenarios where
the server can compute all possible slices of a model in a reasonable amount of time in-between communication
rounds. This allows the server to send these slices to a content delivery network (CDN), effectively a database
that clients can query in order to get model slices in a distributed, scalable way.
Pre-generation amortizes the cost of slice generation when clients have overlapping select keys, as is often the
case. This amortization is particularly important in settings with large numbers of clients, and therefore
may represent a better solution for large-scale cross-device settings. Since the slice-generation happens
before the communication with clients begin, this helps mitigate issues where clients can dropout of a round
while waiting for their on-demand slices. The pre-generation of slices may also be easier to parallelize than
on-demand slicing, as the set of keys to operate on is not too large and is known a priori. It is worth noting
that in synchronous FL systems, the server must wait until pre-generation is complete before accepting client
connections for the next round. In asynchronous systems, such as Papaya (Huba et al., 2022), this may not be
necessary (though a detailed understanding of how staleness of slices impacts training is beyond this work).
This pre-generation approach also allows data minimization barriers between the CDN and the server that
prevent the server from seeing what queries are being made to the CDN. However, even if we assume that
the server has access to the queries being made to the CDN, we can utilize PIR (Chor et al., 1995). This
allows a set of clients to download keys from the CDN such that the server owner gains no information
(cryptographically speaking) about which keys each client has requested. Such guarantees are more difficult to
make in on-demand settings, especially when there is little to no overlap between clients’ key sets. However,
PIR does incur a certain amount of communication overhead, and we leave a formal evaluation of the trade-off
between communication savings gained by federated select and communication increases incurred by PIR to
future work. Alternatively, if secure enclave hardware is available , we could implement either the CDN or
the on-demand slice computation server inside a sufficiently powerful secure enclave, such that decrypted
select keys are only available inside the enclave’s trust boundary and the client can verify how these keys will
be used (and their privacy maintained) via remote attestation
This approach comes at a cost. Notably, since the key space cannot be too large, we must be careful about
how FedSelect can be applied to a given model. For example, throughout language model experiments in
Section 5, keys correspond to words in some vocabulary set of size K. If K is too large, pre-generation of
slices may not be computationally tractable and many of the generated slices may not even be downloaded by
clients resulting in a significant overhead. Thus, one avenue for future work would be to investigate dividing
up the vocabulary set into a moderate number of buckets, each of which correspond to a possible select keys.
Similarly, to use pre-generation of slices with the random key selection in Section 5.3, we may need to bucket
neurons in a dense layer. More generally, future work could investigate how to design FedSelect usages
that only require a moderately-sized key space, rather than one that scales with the size of the model.

7

Open Questions

While we believe that FedSelect is a useful primitive for training large-scale models in federated settings,
there are a number of important open questions related to its usage, implementation, and privacy concerns.
Model-specific selection techniques. While federated select is a general primitive for reducing communication and computation costs in federated learning, much of its application is model-dependent. While
18

we detail some ways to use it in Section 5 above, these techniques need not work well across all model
architectures (and indeed, have disparate impacts on model architecture even in our experiments). Thus,
future work may need to develop more methods for applying federated select depending on the underlying
client data and model architecture. More generally, one could investigate which architectures are more
compatible with federated select.
Compatibility with privacy-preserving technologies. As discussed in Section 6, different implementations of federated select can incorporate different data minimization techniques. However, many federated
settings require data anonymization techniques, including secure aggregation and differential privacy. While
these can be used with naive implementations of federated select (see the "Broadcast and compute" implementation in Section 3.2), it is unclear how to make other implementations (including those based on
on-demand slice generation and pre-generation of slices, as in Section 6) compatible.
Implementation in practical systems. While we have attempted to motivate, examine, and discuss
system benefits and constraints of federated select, future work may investigate how federated select impacts
practical FL training. In particular, how it affects problems such as client dropout (Bonawitz et al., 2017), or
its impact on synchronous versus asynchronous training (Huba et al., 2022). The scalability of such a system
is a particularly important future investigation, especially with respect to model sizes. For example, when
applying federated select to sufficiently large models, it may need to operate over millions, or even billions, of
possible keys held by clients, each of which may have thousands or even millions of local keys.

Acknowledgments
First and foremost, we would like to thank Krzysztof Ostrowski, Taylor Cramer, and Zachary Garrett for
their contributions to the original design of federated select. We would also like to thank Taylor Cramer,
Hubert Eichner, Timon Van Overveldt, Zachary Garrett, Keith Rush, Hugo Song, and Daniel Ramage for
their valuable insights and inputs on the paper. Finally, we note that the experiments contained in this work
would not be possible without the support of Taylor Cramer, Zachary Garrett, and Keith Rush, and the rest
of the TensorFlow Federated team.

References
Eugene Bagdasaryan, Peter Kairouz, Stefan Mellem, Adrià Gascón, Kallista Bonawitz, Deborah Estrin, and
Marco Gruteser. Towards sparse federated analytics: Location heatmaps under distributed differential
privacy with secure aggregation. arXiv preprint arXiv:2111.02356, 2021.
James Henry Bell, Kallista A Bonawitz, Adrià Gascón, Tancrède Lepoint, and Mariana Raykova. Secure
single-server aggregation with (poly)logarithmic overhead. In Proceedings of the 2020 ACM SIGSAC
Conference on Computer and Communications Security, pages 1253–1269, 2020.
K. A. Bonawitz, Vladimir Ivanov, Ben Kreuter, Antonio Marcedone, H Brendan McMahan, Sarvar Patel,
Daniel Ramage, Aaron Segal, and Karn Seth. Practical secure aggregation for privacy-preserving machine
learning. In proceedings of the 2017 ACM SIGSAC Conference on Computer and Communications Security,
pages 1175–1191, 2017.
K. A. Bonawitz, Hubert Eichner, Wolfgang Grieskamp, Dzmitry Huba, Alex Ingerman, Vladimir Ivanov,
Chloé Kiddon, Jakub Konečný, Stefano Mazzocchi, Brendan McMahan, Timon Van Overveldt, David
Petrou, Daniel Ramage, and Jason Roselander. Towards federated learning at scale: System design. In
Proceedings of Machine Learning and Systems. Proceedings of MLSys, 2019.
Kallista Bonawitz, Peter Kairouz, Brendan McMahan, and Daniel Ramage. Federated learning and privacy.
Commun. ACM, 65(4):90–97, mar 2022. ISSN 0001-0782. doi: 10.1145/3500240. URL https://doi.org/
10.1145/3500240.

19

Sebastian Caldas, Jakub Konečny, H Brendan McMahan, and Ameet Talwalkar. Expanding the reach of
federated learning by reducing client resource requirements. arXiv preprint arXiv:1812.07210, 2018.
Zachary Charles, Zachary Garrett, Zhouyuan Huo, Sergei Shmulyian, and Virginia Smith. On large-cohort
training for federated learning. arXiv preprint arXiv:2106.07820, 2021.
Benny Chor, Oded Goldreich, Eyal Kushilevitz, and Madhu Sudan. Private information retrieval. In
Proceedings of IEEE 36th Annual Foundations of Computer Science, pages 41–50. IEEE, 1995.
Gregory Cohen, Saeed Afshar, Jonathan Tapson, and Andre Van Schaik. EMNIST: Extending MNIST to
handwritten letters. In 2017 International Joint Conference on Neural Networks (IJCNN), pages 2921–2926.
IEEE, 2017.
Zihang Dai, Zhilin Yang, Yiming Yang, Jaime Carbonell, Quoc V Le, and Ruslan Salakhutdinov. TransformerXL: Attentive language models beyond a fixed-length context. arXiv preprint arXiv:1901.02860, 2019.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. BERT: Pre-training of deep bidirectional
transformers for language understanding. arXiv preprint arXiv:1810.04805, 2018.
Cynthia Dwork. Differential privacy: A survey of results. In International conference on theory and applications
of models of computation, pages 1–19. Springer, 2008.
David Eigen, Marc’Aurelio Ranzato, and Ilya Sutskever. Learning factored representations in a deep mixture
of experts. arXiv preprint arXiv:1312.4314, 2013.
Farzin Haddadpour, Belhal Karimi, Ping Li, and Xiaoyun Li. FedSKETCH: Communication-efficient and
private federated learning via sketching. arXiv preprint arXiv:2008.04975, 2020.
Dzmitry Huba, John Nguyen, Kshitiz Malik, Ruiyu Zhu, Mike Rabbat, Ashkan Yousefpour, Carole-Jean Wu,
Hongyuan Zhan, Pavel Ustinov, Harish Srinivas, et al. Papaya: Practical, private, and scalable federated
learning. Proceedings of Machine Learning and Systems, 4:814–832, 2022.
Alex Ingerman and Krzysztof Ostrowski. Introducing TensorFlow Federated, Mar 2019. URL https:
//blog.tensorflow.org/2019/03/introducing-tensorflow-federated.html.
Kazuki Irie, Albert Zeyer, Ralf Schlüter, and Hermann Ney. Language modeling with deep transformers.
arXiv preprint arXiv:1905.04226, 2019.
Peter Kairouz, H. Brendan McMahan, Brendan Avent, Aurélien Bellet, Mehdi Bennis, Arjun Nitin Bhagoji,
Kallista Bonawitz, Zachary Charles, Graham Cormode, Rachel Cummings, Rafael G. L. D’Oliveira, Hubert
Eichner, Salim El Rouayheb, David Evans, Josh Gardner, Zachary Garrett, Adrià Gascón, Badih Ghazi,
Phillip B. Gibbons, Marco Gruteser, Zaid Harchaoui, Chaoyang He, Lie He, Zhouyuan Huo, Ben Hutchinson,
Justin Hsu, Martin Jaggi, Tara Javidi, Gauri Joshi, Mikhail Khodak, Jakub Konečný, Aleksandra Korolova,
Farinaz Koushanfar, Sanmi Koyejo, Tancrède Lepoint, Yang Liu, Prateek Mittal, Mehryar Mohri, Richard
Nock, Ayfer Özgür, Rasmus Pagh, Hang Qi, Daniel Ramage, Ramesh Raskar, Mariana Raykova, Dawn
Song, Weikang Song, Sebastian U. Stich, Ziteng Sun, Ananda Theertha Suresh, Florian Tramèr, Praneeth
Vepakomma, Jianyu Wang, Li Xiong, Zheng Xu, Qiang Yang, Felix X. Yu, Han Yu, and Sen Zhao. Advances
and open problems in federated learning. Foundations and Trends® in Machine Learning, 14(1–2):1–210,
2021. ISSN 1935-8237. doi: 10.1561/2200000083. URL http://dx.doi.org/10.1561/2200000083.
Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B Brown, Benjamin Chess, Rewon Child, Scott Gray,
Alec Radford, Jeffrey Wu, and Dario Amodei. Scaling laws for neural language models. arXiv preprint
arXiv:2001.08361, 2020.
Sai Praneeth Karimireddy, Martin Jaggi, Satyen Kale, Mehryar Mohri, Sashank J Reddi, Sebastian U Stich,
and Ananda Theertha Suresh. Mime: Mimicking centralized stochastic algorithms in federated learning.
arXiv preprint arXiv:2008.03606, 2020.
Daliang Li and Junpu Wang. FedMD: Heterogenous federated learning via model distillation. arXiv preprint
arXiv:1910.03581, 2019.
20

Tian Li, Anit Kumar Sahu, Manzil Zaheer, Maziar Sanjabi, Ameet Talwalkar, and Virginia Smith. Federated
optimization in heterogeneous networks. In Proceedings of Machine Learning and Systems 2020, pages
429–450, 2020.
Paul Pu Liang, Terrance Liu, Liu Ziyin, Nicholas B Allen, Randy P Auerbach, David Brent, Ruslan
Salakhutdinov, and Louis-Philippe Morency. Think locally, act globally: Federated learning with local and
global representations. arXiv preprint arXiv:2001.01523, 2020.
Brendan McMahan, Eider Moore, Daniel Ramage, Seth Hampson, and Blaise Aguera y Arcas. Communicationefficient learning of deep networks from decentralized data. In Proceedings of the 20th International
Conference on Artificial Intelligence and Statistics, volume 54, 2017.
H. Brendan McMahan, Gary Holt, D. Sculley, Michael Young, Dietmar Ebner, Julian Grady, Lan Nie, Todd
Phillips, Eugene Davydov, Daniel Golovin, Sharat Chikkerur, Dan Liu, Martin Wattenberg, Arnar Mar
Hrafnkelsson, Tom Boulos, and Jeremy Kubica. Ad click prediction: a view from the trenches. In Proceedings
of the 19th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD),
2013.
Nicole Mitchell, Johannes Ballé, Zachary Charles, and Jakub Konečnỳ. Optimizing the communicationaccuracy trade-off in federated learning with rate-distortion theory. arXiv preprint arXiv:2201.02664,
2022.
Fan Mo and Hamed Haddadi. Efficient and private federated learning using TEE. In Proc. EuroSys Conf.,
Dresden, Germany, 2019.
Sashank J. Reddi, Zachary Charles, Manzil Zaheer, Zachary Garrett, Keith Rush, Jakub Konečný, Sanjiv
Kumar, and Hugh Brendan McMahan. Adaptive federated optimization. In International Conference on
Learning Representations, 2021.
Amirhossein Reisizadeh, Aryan Mokhtari, Hamed Hassani, Ali Jadbabaie, and Ramtin Pedarsani. FedPAQ: A communication-efficient federated learning method with periodic averaging and quantization. In
International Conference on Artificial Intelligence and Statistics, pages 2021–2031. PMLR, 2020.
Jae Hun Ro, Theresa Breiner, Lara McConnaughey, Mingqing Chen, Ananda Theertha Suresh, Shankar
Kumar, and Rajiv Mathews. Scaling language model size in cross-device federated learning. arXiv preprint
arXiv:2204.09715, 2022.
Daniel Rothchild, Ashwinee Panda, Enayat Ullah, Nikita Ivkin, Ion Stoica, Vladimir Braverman, Joseph
Gonzalez, and Raman Arora. FetchSGD: Communication-efficient federated learning with sketching. In
International Conference on Machine Learning, pages 8253–8265. PMLR, 2020.
Felix Sattler, Simon Wiedemann, Klaus-Robert Müller, and Wojciech Samek. Robust and communicationefficient federated learning from non-IID data. IEEE transactions on neural networks and learning systems,
31(9):3400–3413, 2019.
Noam Shazeer, Azalia Mirhoseini, Krzysztof Maziarz, Andy Davis, Quoc Le, Geoffrey Hinton, and Jeff
Dean. Outrageously large neural networks: The sparsely-gated mixture-of-experts layer. arXiv preprint
arXiv:1701.06538, 2017.
TFF. TensorFlow Federated Stack Overflow dataset, 2019. URL https://www.tensorflow.org/federated/
api_docs/python/tff/simulation/datasets/stackoverflow/load_data.
Sagar M Waghmare, Hang Qi, Huizhong Chen, Mikhail Sirotenko, and Tomer Meron. Efficient image
representation learning with federated sampled softmax. arXiv preprint arXiv:2203.04888, 2022.
Jianyu Wang, Zachary Charles, Zheng Xu, Gauri Joshi, H Brendan McMahan, Maruan Al-Shedivat, Galen
Andrew, Salman Avestimehr, Katharine Daly, Deepesh Data, et al. A field guide to federated optimization.
arXiv preprint arXiv:2107.06917, 2021.

21

Tien-Ju Yang, Dhruv Guliani, Françoise Beaufays, and Giovanni Motta. Partial variable training for efficient
on-device federated learning. In ICASSP 2022-2022 IEEE International Conference on Acoustics, Speech
and Signal Processing (ICASSP), pages 4348–4352. IEEE, 2022.
Zhilin Yang, Zihang Dai, Yiming Yang, Jaime Carbonell, Russ R Salakhutdinov, and Quoc V Le. Xlnet:
Generalized autoregressive pretraining for language understanding. Advances in neural information
processing systems, 32, 2019.
Chen Zhu, Zheng Xu, Mingqing Chen, Jakub Konečný, Andrew Hard, and Tom Goldstein. Diurnal or
nocturnal? Federated learning of multi-branch networks from periodically shifting distributions. In
International Conference on Learning Representations, 2022. URL https://openreview.net/forum?id=
E4EE_ohFGz.
Wennan Zhu, Peter Kairouz, Brendan McMahan, Haicheng Sun, and Wei Li. Federated heavy hitters
discovery with differential privacy. In International Conference on Artificial Intelligence and Statistics,
pages 3837–3847. PMLR, 2020.

22
