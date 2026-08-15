---
title: "Can In-Context Learning Support Intrinsic Curiosity?"
person: blaise-aguera-y-arcas
section: by
type: journal-article
year: 2026
date: 2026-06-17
venue: "arXiv (Cornell University)"
authors: "Eric Elmoznino, Sangnie Bhardwaj, Johannes von Oswald, Rajai Nasser, Blaise Agüera y Arcas, João Sacramento, Rif A. Saurous, Guillaume Lajoie"
source_url: https://doi.org/10.48550/arxiv.2606.19476
retrieved: 2026-08-13
content: full-text
notes: "OpenAlex W7165403742, W7165424545 (type: preprint). Full text extracted from the open-access PDF at https://arxiv.org/pdf/2606.19476."
---

# Can In-Context Learning Support Intrinsic Curiosity?

## Full text

### Abstract (from OpenAlex metadata)

Effective machine learning depends not only on how we model data, but also on what data we choose to collect. While large sequence models have revolutionized data modeling, the problem of automated data selection, or "intrinsic curiosity", remains a significant challenge. Classic approaches incentivize exploration by rewarding an agent based on its "learning progress", which measures how much a newly acquired observation improves a world model's predictive ability. However, evaluating these rewards traditionally requires expensive inner loops of gradient descent updates within each trajectory, rendering them computationally impractical at scale. In this work, we investigate whether the emergent in-context learning (ICL) capabilities of sequence models can eliminate this bottleneck by serving as immediate, update-free world models. Specifically, we evaluate whether an exploration policy can be trained to maximize learning progress, using solely the prediction errors and counterfactual context manipulations of an in-context learner. We first prove that in general Markov decision processes, this is in fact impossible in an unbiased way: the resulting intrinsic rewards either suffer from nuisance terms that bias their estimation of true learning progress, or they cannot be implemented using an in-context learner's prediction errors. Conversely, we prove a positive result for a broad subclass of non-temporal settings, encompassing active learning and Bayesian Experimental Design: here, ICL-derived rewards successfully bound and asymptotically converge to the true learning progress. We corroborate our theory with controlled experiments across continuous and symbolic environments, demonstrating that our ICL-driven framework successfully trains curious data-collection policies that explore optimally.

---

Can In-Context Learning Support Intrinsic Curiosity?

Eric Elmoznino∗,1, Sangnie Bhardwaj∗,2, Johannes von Oswald1, Rajai Nasser1,
Blaise Agüera y Arcas1, João Sacramento1, Rif A. Saurous1, Guillaume Lajoie1

arXiv:2606.19476v1 [cs.LG] 17 Jun 2026

1

Google – Paradigms of Intelligence Team, 2Google DeepMind

Abstract
Effective machine learning depends not only on how we model data, but also on what
data we choose to collect. While large sequence models have revolutionized data
modeling, the problem of automated data selection, or “intrinsic curiosity”, remains a
significant challenge. Classic approaches incentivize exploration by rewarding an agent
based on its “learning progress”, which measures how much a newly acquired observation improves a world model’s predictive ability. However, evaluating these rewards
traditionally requires expensive inner loops of gradient descent updates within each trajectory, rendering them computationally impractical at scale. In this work, we investigate
whether the emergent in-context learning (ICL) capabilities of sequence models can eliminate this bottleneck by serving as immediate, update-free world models. Specifically,
we evaluate whether an exploration policy can be trained to maximize learning progress,
using solely the prediction errors and counterfactual context manipulations of an incontext learner. We first prove that in general Markov decision processes, this is in fact
impossible in an unbiased way: the resulting intrinsic rewards either suffer from nuisance
terms that bias their estimation of true learning progress, or they cannot be implemented
using an in-context learner’s prediction errors. Conversely, we prove a positive result for
a broad subclass of non-temporal settings, encompassing active learning and Bayesian
Experimental Design: here, ICL-derived rewards successfully bound and asymptotically
converge to the true learning progress. We corroborate our theory with controlled experiments across continuous and symbolic environments, demonstrating that our ICL-driven
framework successfully trains curious data-collection policies that explore optimally.

1 Introduction
How should an agent collect data in an unknown environment to ensure optimal exploration? One
foundational approach dictates that the data should maximally improve the agent’s model of its environment
(Schmidhuber, 1991a; Lindley, 1956). Such a model can subsequently support arbitrary downstream tasks,
either through explicit planning or by having acquired robust representations. To this end, prior work has
proposed utilizing “intrinsic rewards” to drive the collection of data, which are defined strictly as a function
of the trajectory of actions and observations collected by a policy, and assume no extrinsic “task”.
Given a Bayesian prior on the world, an optimal intrinsic reward is Bayesian information gain (BIG),
which measures the expected bits gained about the true environment’s dynamics with every action (Itti and
Baldi, 2009; Lindley, 1956). However, BIG is difficult to compute in practice because it requires explicitly
parameterizing the environment’s dynamics and performing intractable Bayesian inference. While tractable
prediction-based objectives have been proposed as alternatives (e.g., Schmidhuber, 1991a), they face two
major hurdles: (1) their theoretical relationship to BIG remains poorly understood and (2) computing
them requires expensive gradient descent updates to a world model that have slow credit assignment.
Overcoming this second bottleneck requires fast and data-efficient learning mechanisms. In-context learning
(ICL) has emerged as a highly effective paradigm for addressing this problem: sequence models can act as
amortized predictors that implicitly approximate the Bayesian posterior predictive in a single forward pass,
∗ Equal contribution. Correspondence to: {eric.elmoznino,guillaume.lajoie}@gmail.com, sangnie@google.com

Preprint.

bypassing the need for explicit inference. This capability is hypothesized to partly drive the success of large
language models (Radford et al., 2019; Brown et al., 2020), and has seen great success with Prior-Fitted
Networks (PFNs) (Nagler, 2023; Müller et al., 2022) such as TabPFN (Hollmann et al., 2022) which are
pretrained on a large prior over datasets to perform amortized learning on a new dataset at inference time.
In this work, we use ICL for evaluating prediction-based intrinsic curiosity rewards. We examine the
degree to which data collected by a policy improves a world model learned purely in-context, and reward
the policy based on this improvement. This raises several fundamental questions: First, is this possible
with ICL, and for which intrinsic rewards? Second, does the resulting reward approximate BIG, and if
so, under what circumstances? To answer these questions, we make the following contributions:
1. By formalizing in-context learners as implicit Bayesian predictors, we prove novel mathematical
relationships between prediction-based intrinsic rewards and BIG, which were previously unknown.
2. We provide a negative result for general Markov Decision Processes (MDPs), proving that predictionbased intrinsic rewards are biased estimators of BIG. Further, while some of these rewards can be implemented using ICL, we show that others, such as classic learning progress (Schmidhuber, 1991a), cannot.
3. In contrast, we establish a positive result for Bayesian Experimental Design (BED) settings,
demonstrating that several intrinsic rewards can be approximated using ICL, and that it is possible
to asymptotically approximate BIG for long trajectories with a particular reward structure.
4. We conduct experiments that corroborate our theoretical findings, demonstrating the practical viability
of this ICL approach to curiosity.

2 Problem Setting and Notation
Environment. We consider a Bayes-Adaptive MDP (BAMDP) with states st, actions at, horizon
T , and a latent environment parameter θ ∼ p(θ) fixed throughout an episode. Conditional on θ, the
environment’s dynamics are Markov and stationary: st+1 ∼ p(· | st, at, θ). Throughout, we write
ht :=(s1,a1,...,st−1,at−1) for the trajectory history just before st.
Intrinsic curiosity objective. Our goal is to train a policy πϕ(at | ht,st) under a “meta-RL” setting
(Duan et al., 2016) in which episodes are rolled out from environments sampled from p(θ). Crucially,
there is no notion of “task” or “extrinsic” reward. We instead consider “intrinsic” rewards that are
functions of only the trajectory (s1,a1,...,sT ), and which are ideally maximized when the trajectory is
highly informative about the latent parameters θ governing the environment’s dynamics. By training πϕ
across a broad distribution of environments sampled from p(θ), we aim for it to optimally explore a new
environment sampled from this distribution at inference time. In information theoretic terms, we consider
an “optimal” intrinsic reward as one that maximizes the per-step mutual information between an observed
state and the latent environment parameters, conditioned on the history. In the literature, this is called
Bayesian information gain (BIG) or Bayesian surprise (Itti and Baldi, 2009; Lindley, 1956):
BIG:=I(st;θ |ht).

(1)

In-context learning prediction errors. We consider whether a sequence model ρ can be used to
approximate BIG, using only its prediction errors and manipulations of its context. We assume that ρ has
been pretrained offline to perform next-state predictions on trajectories of BAMDPs sampled from prior p(θ)
with uniform action selection — ρ is then frozen when training the policy. We further suppose that ρ has been
trained with sufficient capacity and data, such that it has learned to emit the Bayesian posterior-predictive:
Z
ρ(st |ht)= p(st |st−1,at−1,θ)p(θ |ht)dθ.
(2)
This perspective of in-context learners as amortized Bayes-optimal predictors has been formalized in substantial prior work (Grau-Moya et al., 2024; Mikulik et al., 2020; Xie et al., 2022; Binz et al., 2024; Nagler,
2023; Müller et al., 2022), and it serves as a starting point for our investigations. In our setting, ρ can be seen
as a meta-learner that implicitly fits environment parameters θ in-context and exposes their predictions for
novel transitions, all within a single forward pass. The speed of in-context learners makes them particularly
promising for the purposes of optimizing certain intrinsic curiosity objectives, which, as we will see next,
require us to repeatedly assess the learning progress of a world model over the course of a trajectory.
2

3 Prior Work on Intrinsic Curiosity
We briefly describe approaches to intrinsic curiosity relevant to our work — Aubret et al. (2023) provides
a recent review. We discuss intrinsic rewards that are less directly related to our work in Appendix A.
We assume p(·|·,θ̂t) is a predictive world model that has been trained on subtrajectory (a1:t−1,s1:t).
Surprisal. A common heuristic for encouraging exploration is to maximize a world model’s
surprisal, seeking observations for which it has high prediction error. The surprisal reward is
rt := −log p(st | st−1,at−1, θ̂t−1). This approach has been used at least as far back as Schmidhuber
(1991b) and is simple but surprisingly effective (Burda et al., 2019; Levy et al., 2025; Hester and Stone,
2012; Chentanez et al., 2004). However, surprisal fails to distinguish between two sources of information:
epistemic (i.e., learnable) and aleatoric (i.e., noise). The latter can be detrimental: a policy seeking surprisal
will learn to sit in front of a “noisy TV”, even if these observations contain no new useful information
about the environment (Schmidhuber, 1991a). Thus, while surprisal excels in deterministic environments,
it fails in stochastic settings (Burda et al., 2019).
Learning progress. Another principled approach to intrinsic curiosity is to maximize “learning progress”,
introduced in Schmidhuber (1991a) and further explored in (Schmidhuber, 2009, 2010; Storck et al., 1995;
Oudeyer et al., 2007; Oudeyer and Kaplan, 2008, 2007; Lopes et al., 2012; Azar et al., 2019). It aims to reward a policy based on the degree to which the data that it acquires improves the predictive ability of a world
model. The learning progress intrinsic reward is rt :=log p(st |st−1,at−1,θ̂t)−log p(st |st−1,at−1,θ̂t−1),
i.e. the improvement in the model’s ability to predict st after the transition to it has been observed. pθ̂t
is often parameterized using a recurrent neural network updated online with gradient descent. Unlike
surprisal, it assigns zero reward to observations that only contain aleatoric noise, since they do not improve
the model’s predictive ability.
In Section 4, we will show that while learning progress has desirable exploration properties, the need to
evaluate a model’s prediction error on transitions that it has already seen makes it non-implementable using
an in-context learner’s prediction errors, for general environments. Azar et al. (2019) introduced an alternative that instead evaluates improvements in prediction error on future transitions (st+K−1,at+K−1,st+K ),
rather than on the current one. Section 4 will show that this alternative — along with a variant that considers
improvements on all future transitions — can be computed using an in-context learner’s prediction errors.
Bayesian information gain. Alternatively, we can seek data that maximally changes a model’s belief
over possible environments — an approach termed Bayesian information gain (BIG) or Bayesian surprise
(Sun et al., 2011; Little and Sommer, 2013; Itti and Baldi, 2009; Houthooft et al., 2016; Stadie et al., 2015;
MacKay, 1992; Fedorov, 1972; Houlsby et al., 2011; Lindley, 1956). The predictive model now considers
a distribution over possible environment dynamics, with initial prior p(θ̂). Sun et al. (2011) show that the
optimal exploration strategy is to maximize the Kullback-Leibler divergence between the prior and posterior
over environment parameters after having observed a novel transition: rt := KL(p(θ̂ | ht,st) || p(θ̂ | ht)),
where p(θ̂ | ht,st) ∝ p(θ̂|ht)p(st|ht, θ̂). Intuitively, this objective encourages the agent to reduce its
uncertainty about the environment dynamics as quickly as possible. Furthermore, if the initial prior p(θ̂) is
equal to the environment’s true prior distribution over latents p(θ), this reward is mathematically equivalent
in expectation to I(st;θ |ht) from Equation (1).
While optimal in terms of yielding the fastest convergence of p(θ̂ | ht,st) towards the true environment
dynamics θ, BIG poses significant implementation challenges. It requires a model to do Bayesian
inference over a space of possible environments — an operation that is generally intractable and difficult
to approximate. Moreover, this approach assumes the model can explicitly parameterize the hypothesis
space over θ, which is challenging in rich environments with unknown latent structure. In Section 4, we
will take BIG as the theoretically-optimal objective for intrinsic curiosity, and we will evaluate the degree
to which more tractable prediction-based rewards computed with in-context learners can approximate it.

4 Computing Intrinsic Rewards Using In-Context Learners
We now ask whether an in-context learner ρ can support intrinsic curiosity rewards that approximate
BIG. Section 4.1 writes candidate rewards in ρ’s interface; Section 4.2 shows none can identify BIG
in general BAMDPs at any finite horizon, and that the asymptotic limits required to escape this barrier
3

are practically out of reach; Section 4.3 restores tractability under a structural restriction, namely that of
Bayesian Experimental Design (BED).
4.1 Predictive Rewards
We retain the BAMDP setup of Section 2 and additionally write ht′ \t for the history ht′ with st replaced
by a “mask” token — a counterfactual manipulation of ρ’s context used by learning-progress-style rewards.
We assume: (i) Markovian, stationary dynamics given θ, (ii) ρ is exactly Bayesian over θ, (iii) the masked
trajectory ht′ \t removes only st’s contribution and ρ remains exactly Bayesian on it, (iv) posterior consistency: p(θ |ht)→δθ∗ as t→∞, (v) actions are policy-generated; future actions do not update the posterior
over θ, (vi) mixing given θ: I(st;st+k |θ,ht,at:t+k−1)→0 as k →∞. Detailed treatments, including the
consequences of approximation, masked-input training, and non-mixing dynamics, are in Appendix B.
We want πϕ to collect observations that are maximally informative about the world, and we investigate
how to maximize the stepwise Bayesian information gain (BIG) contributed by a new observation st:
I(st;θ | ht). Importantly, we do not allow explicit access or manipulation of θ, and consider intrinsic
rewards reviewed in Section 3 that are built off of state prediction errors, expressed in terms of ρ when
possible. Our theoretical results apply to a general class of rewards, including the following common ones:
rtsur :=−log ρ(st |ht),
Z
rtdl :=log p(st |st−1,at−1,θ)p(θ |ht,st)dθ−log ρ(st |ht).

(3)
(4)

Here, rsur is classical predictive surprisal. rdl is a learning progress reward based on description length
(dl) reduction (Schmidhuber, 1991a, 2009, 2010), which asks how much a just-observed transition would
improve a model’s predictions if included in its posterior. Adding to this list, we propose a novel reward:
rtsum :=

T
X



log ρ(st′ |ht′ )−log ρ(st′ |ht′ \t) ,

(5)

t′ =t+1

where T is the trajectory length. rsum is one of our core contributions, and experiments show it performs
well (Section 5). It telescopes over the remaining trajectory and is an extension of the NDIGO reward
of Azar et al. (2019), which measured the difference in predictive log-likelihoods for a single future
observation K steps in the future. We refer the reader to Appendix C.6 for a treatment of the NDIGO
reward. We illustrate our setting in Figure 1, using rsum as an example.

Intrinsic reward
samples

Environment
at

a0

a1

s0

s1

st+1

Policy πϕ

⋯

a t−1

at

st−1

st

⋯

aT
sT

Pretrained
in-context learner ρ
updates
s ̂1

s ̂2

⋯

s ̂t

s ̂t+1

⋯

Implicitly posterior predictive
ρ (st ∣ h t ) ≈ p (st | a t , θ )p (θ ∣ h t )
∫

implicit update

Rewards can
(i) use predictions and
(ii) manipulate context
r tsum = [−log ρ (st+1:T ∣ a 0:T , s 0:t−1 )]
− [−log ρ (st+1:T ∣ a 0:T , s 0:t )]

s ̂T+1

Next-s NLL

Agent interaction

without observing st
with st

st+1

⋯

sT

Figure 1: Our method involves using a pretrained in-context learner ρ to construct intrinsic curiosity rewards for a policy
πϕ . Trajectories unrolled by the policy are passed to the in-context learner, and the reward can be any function of the resulting observation prediction errors on manipulated sequence contexts. We give an example for the reward rsum , which
measures the improvement in future prediction errors when a particular state is observed compared to when it is masked.

4.2 Limits on Intrinsic Rewards From In-Context Learners
We first characterize the class of rewards easily implementable with in-context learners ρ:
4

Definition 1 (Class F). F is the class of arbitrary functions of finitely many predictive likelihoods of
ρ at conditioning subsets of the actual trajectory:
n
o

F = rt =f (ρ(Xi |Yi))i∈I :Xi observation, Yi ⊆trajectory, ∀i∈I, and f :[0,1]|I| →R .
At any finite horizon T , rsur and rsum belong to F. rdl does not: the integral in Equation (4) requires
an explicit Bayesian update of ρ’s posterior — outside ρ’s predictive interface in general (see Appendix D).
We return to rdl in Section 4.3, where it does admit a ρ-tractable form for a subclass of environments.
Returning to our goal of maximizing BIG, no finite-horizon reward in F can be an unbiased estimator:
Theorem 1 (Impossibility of BIG identification in F). Let M be the class of BAMDPs satisfying (i)–(v)
above, whose transition kernels are neither deterministic nor independent across time given θ. Then for
every rt ∈F, there exists M ∈M with EM [rt |ht]̸= I(st;θ |ht).
The proof (Appendix C.2) constructs two BAMDPs whose priors share enough leading moments to match
E[rt] for any finite rt ∈ F while their expected BIG differs. We now decompose rsur and rsum against
I(st;θ |ht) to locate the bias.
Theorem 2 (Decomposition of rsur). Under (i)–(iii),
E[rtsur |ht] = I(st;θ |ht) + H(st |ht,θ) .
| {z }
aleatoric entropy

H(st |ht,θ)=H(st |st−1,at−1,θ) is non-negative and does not vanish as θ becomes identified.
The proof is in Appendix C.3. Theorem 2 highlights the classic “noisy TV problem”, where an agent
seeks sources of unpredictable noise.
Theorem 3 (Decomposition of rsum). Under (i)–(iii) and (v),
E[rtsum |ht,at:T −1] = I(st;θ |ht) + I(st;st+1 |θ,ht,at) −I(st;θ |ht,at:T −1,st+1:T ).
{z
} |
{z
}
|
one-step “abductive”

“residual”

Both terms are non-negative. Under (iv), the residual vanishes as T →∞; the abductive does not.
The proof is in Appendix C.4. The abductive term captures kernel-mediated coupling between st and the
next observation st+1 that is not explained by their common dependence on θ. Similarly, a general treatment
of rewards involving log-ratios lead to signal/abductive/residual decomposition (Appendix C.5). Notably,
applied to NDIGO, it produces an analogous decomposition whose abductive and residual both fail to vanish.
Beyond F: infinite-horizon rewards. Taking T →∞ to drive rsum’s residual to zero already pushes
rsum outside the finite-horizon class F of Theorem 1. Are there infinite-horizon rewards built from ρ’s
predictives that recover BIG in general BAMDPs? Consider the generalization of rsum with a gap parameter
K separating st from the predicted block, rtgap(K) := log ρ(st+K:T | ht,st,at:T −1) − log ρ(st+K:T |
ht,at:T −1). Under the mixing assumption (vi), rgap recovers BIG in the iterated limit limK→∞limT →∞
(Corollary 6.1), and this double limit is structurally necessary — any log-ratio reward universally identifying
BIG must place all weight at infinite gap with blocks of unbounded size (Theorem 7). We use rgap as an
analytical tool only: it is not feasibly tractable using in-context learners (see below; details in Appendix C.7).
Summary. The section identified compounding obstructions to building ρ-based estimators of BIG:
• Interventional rewards — those requiring modifications of ρ’s posterior — lie outside ρ’s standard
interface. The canonical example, rdl (Equation (4)), folds the just-observed st into the posterior over θ
before re-evaluating the kernel at (st−1,at−1), and is not implementable through ρ in general BAMDPs.
• Among ρ-implementable rewards in F, no finite-horizon estimator identifies BIG (Theorem 1); rsur
and rsum exemplify the bias structure, the former acquiring an aleatoric “noisy TV” offset (Theorem 2)
and the latter a persistent one-step abductive (Theorem 3).
• Recovery of BIG via a reward related to F requires both sequence length T → ∞ and marginalizing
gap K →∞, as exemplified by the theoretical reward rgap (Corollary 6.1 and Theorem 7). The latter
is a substantial obstacle: significant unobserved intermediate states st+1:t+K−1 that ρ must marginalize
over are poorly supported in sequence models (Appendix B.3).
In sum, we argue there is no practical reward easily implementable with an in-context learner ρ that
converges to BIG in general BAMDPs. Moreover, rsum stands as the best ρ-implementable approximation
of BIG — scaling naturally with trajectory length but nevertheless retaining an irreducible abductive bias.
We now consider BED, in which several of these obstructions vanish.
5

4.3 Bayesian Experimental Design Setting
We now consider Bayesian Experimental Design (BED) environments, where the transition kernel satisfies
p(st |st−1,at−1,θ)=p(st |at−1,θ) — the effect of action at depends on θ but not on the current state. This
covers any sequential experiment with trials conditionally independent given θ and the action sequence,
such as active learning. Aleatoric biases remain, and rsur’s decomposition is unchanged (Theorem 2).
But, any abductive bias of the form seen in Theorem 3 vanishes structurally, simplifying rsum:
Corollary 3.1 (Decomposition of rsum in BED). Under (i)–(v),
E[rtsum |ht,at:T −1] = I(st;θ |ht) − I(st;θ |ht,at:T −1,st+1:T ),
i.e., the abductive of Theorem 3 vanishes structurally. As T →∞, E[rtsum]→I(st;θ |ht).
The proof is in Appendix C.9. Thus rsum is an asymptotically unbiased BIG estimator in BED. For rdl
in the BED setting, things also improve. The posterior predictive term admits a ρ-predictive form via a
counterfactual action commitment that “copies” the current transition (st−1,at−1,st) into ρ’s context:
Z

p(st |st−1,at−1,θ)p(θ |ht,st)dθ = ρ st+1 =st ht,st,at =at−1 .
(6)
The counterfactual is the action choice at =at−1 (re-using the same action), valid because actions are policygenerated and the BED environment’s transition kernel has no st−1 dependence. The identity in Equation (6)
makes rdl implementable using in-context learners at the cost of a hypothetical extra rollout step.
Theorem 4 (Decomposition of rdl in BED). Under (i)–(v), with L(θ):=p(st |at−1,θ)/ρ(st |ht),
h
i
E[rtdl |ht] = I(st;θ |ht) + Est |at−1 log Ep(θ|ht ,st )[L(θ)]−Ep(θ|ht ,st )[log L(θ)] ,
i.e., BIG plus a non-negative Jensen gap. Both terms in the expectation vanish as t→∞ under (iv).
The proof is in Appendix C.10. Like rsum, rdl converges to BIG in BED, but with opposite-sign bias:
rsum is biased downward by a residual on future data, rdl upward by a Jensen gap on past data. We thus
get E[rtsum] ≤ I(st;θ | ht) ≤ E[rtdl], with the gap closing asymptotically. Importantly, however, it should
be noted that rdl’s bias (the Jensen gap) vanishes together with BIG I(st;θ | ht) itself, as t → ∞ (see
Appendix C.9).
Summary. BED removes the obstructions of general BAMDPs: rsum and rdl both asymptotically
recover BIG. However, rsum recovers BIG as T →∞ while rdl does so as t→∞. This means that given
long sequences, rsum can, in principle, recover BIG at finite t while rdl only trivially recovers BIG in
the limit where the signal itself vanishes. Nevertheless, both rewards can still be useful at finite T and
finite t, as we now investigate in experiments.

5 Experiments
We evaluate our framework on three structured BED environments: Gaussian Process function estimation,
Mastermind code-breaking, and Alchemy transition-rule discovery, each requiring the policy to actively
gather observations that are informative about unknown latent variables.
We train policies with PPO or REINFORCE using curiosity-driven rewards from Section 4.1: rsur, rdl,
and rsum. We also compare to rtask, which uses a validation metric of the environment (indicative of
having learned its dynamics) as the reward. For each environment, we pretrain an in-context learner ρ
by sampling environment latents from the prior θ ∼p(θ) and unrolling trajectories with uniformly-random
actions; as such, we call these Prior-Fitted Networks (PFNs) in line with prior work (Müller et al., 2022).
Some environments additionally admit an exact predictive Bayesian oracle predictive ρ∗. Details and
results for each environment are given below.
5.1 Gaussian Process
The Gaussian Process (GP) environment models active function estimation in a continuous domain.
An unknown function f is sampled from a GP prior with a rational quadratic kernel. The function f is
represented by a finite set of inducing points sampled on a regular grid of resolution R over the domain
[−xmax,xmax]2; the posterior mean at any query location is obtained by exact GP conditioning on these
inducing points. More details can be found in Appendix E.1.1.
6

logp(Yval Xval)

Oracle
0.0
0.2
0.4
0.6
0.8
1.0
1.2

Oracle
Reward
rsum
rsur
rdl

0

2500 5000 7500 10000

step

0.0
0.2
0.4
0.6
0.8
1.0
1.2

PFN
0.0
0.2
0.4
0.6
0.8
1.0
1.2

rbayes rtask rsum rdl rsur random

Reward

rtask rsum

rdl

Reward

rsur random

Figure 2: Comparison of validation log-likelihood for Gaussian Processes for the Oracle and PFN predictive models.
(Left) For rsur validation score decreases over training steps. (Center and right) Final validation scores: rsum and
rdl achieve equivalent performance to training on rtask , but rsur performs significantly worse than a random policy.

A fresh function f is drawn at the start of each episode. At each step the policy selects a query location

2
xt ∈ [−xmax,xmax]2 and observes a noisy evaluation yt = f(xt) + εt, where εt ∼ N 0, σnoise
(xt) is
spatially varying noise. The noise is in the form of a tiled checkerboard pattern (details in Appendix E.1.1),
and is the same in every episode. An optimal information-gathering policy should therefore learn to
preferentially query the low-noise tiles. Consecutive observations are conditionally independent given f
and the noise map. Therefore, the environment follows the BED setting with θ =f, at =xt, and st+1 =yt.
Predictive model. The Bayesian oracle ρ∗ performs exact GP posterior
 inference. After observing ht,
the predictive distribution for yt is ρ∗(yt |ht,xt)=N yt;µt(xt),σt2(xt) where µt and σt2 are the standard
GP posterior mean and predictive variance (including observation noise) conditioned on ht. Note ρ∗ has
access to the true kernel and the noise map. The learned PFN ρ is a causal Transformer. Details about the
training and architecture are in Appendix E.1.3. We also show in Figure E.1 that ρ approximates ρ∗ well.

Figure 3: Left: The colourbar depicts noise strength of the GP. Top 10% of random paths ranked by the rewards
show that rsum is high for the noiseless tiles, conversely rsur favours the noisy regions. Center: BIG across trajectories
generated by trained policies. rsur has the lowest information gain due to the Noisy TV problem. Right: Zoomed
comparison. Higher BIG for rsum , rdl , and rtask indicates that these policies select queries that are more informative
about the underlying function.

Validation. To measure the quality of the collected trajectory hT , we evaluate on a set of validation
points on the grid. Let (Xval ,Yval )={(x̃j ,ỹj )}M
j=1 be a random subset of the episode’s ground-truth GP
inducing points. Regardless of whether ρ is a Bayesian oracle or a trained PFN, we validate by conditioning
PM
1
∗
the oracle ρ∗ on the trajectory hT and report the mean log-likelihood V = M
j=1 logρ (ỹj |hT ,x̃j ).
Results. Since the environment contains aleatoric noise, we observe a stark divergence in performance
between the rewards. As shown in Figure 2, both the random baseline and the policy trained with rsur
perform significantly worse than those trained with rdl and rsum. We note that the validation log-likelihood
steadily decreases over training, despite rsur increasing (Figure E.2). This provides strong empirical
confirmation of Theorem 2, which states that rsur is susceptible to the “noisy TV” problem, whereas rsum
and rdl successfully distinguish between reducible epistemic uncertainty and irreducible aleatoric noise.
7

To further confirm this, in Figure 3, we collect 1000 trajectories with a random policy. We then calculate
rsur and rsum for these trajectories, and in green highlight the ones in the 90% percentile for each reward.
We can observe that the trajectories with the highest rsum stray away from the noisy checkerboards,
whereas those for rsur concentrate in these regions instead. We also plot the BIG across trajectories
collected by the policies trained with the different rewards. As predicted, the BIG of rsur is much lower
than that of other rewards. Finally, in Appendix E.2, we show empirically that rsum and rdl decompose
into BIG and a shrinking finite-time nuisance term, as predicted by Corollary 3.1 and Theorem 4.
5.2 Mastermind
Mastermind (Noisy)

0.96
0.94
0.92
rtask rsum rdl

rsur random

0.750
0.725
0.700
0.675
0.650

rtask rsum rdl

rsur random

Alchemy

0.75

logp(Yval Xval)

0.775

0.98

0.90

0.800

0.70
0.65
0.60
0.55
0.50

0.30

logp(Yval Xval)

Mastermind
p(true code)

p(true code)

1.00

rsum

rdl

rsur random

Alchemy (Noisy)
PFN
Oracle

0.28
0.26
0.24
0.22
0.20

rsum

rdl

rsur random

Figure 4: Validation scores for Mastermind and Alchemy. In the standard variant, all rewards are competitive. In
both the noisy variants, rsur ’s performance falls below the random baseline, whereas rsum and rdl remain robust.

Mastermind is a code-breaking game parameterized by a secret code c∈{0,...,C−1}L made of coloured
pegs, where L is the code length and C the number of colours. At each step, the policy submits a guess gt
and receives feedback (bt,wt), where bt counts the number of pegs correct in both colour and position, and
wt counts the total number of pegs correct in colour irrespective of position. The feedback depends only on
the current guess and the fixed code. This follows the BED setting with θ =c, at =gt, and st+1 =(bt,wt).
We additionally consider a noisy variant of the environment in which one randomly chosen colour per
episode is designated as “evil.” Any guess position whose colour matches the evil colour has that position’s
value replaced with a uniformly random colour before feedback is computed, so the resulting (bt,wt) may
not reflect the true code. Additionally, the evil colour is guaranteed not to appear in the secret code itself.
The evil colour identity is unknown to the policy and the learned world model ρ.
Predictive model. The oracle ρ∗ maintains an exact posterior over secret codes by enumerating all
C L possibilities and filtering to those consistent with the observed history. It computes the predictive
probability of each new response as the fraction of consistent codes that would produce that response:
ρ∗(st |ht)=

|{c′ :c′ consistent with ht and (at−1,st)}|
.
|{c′ :c′ consistent with ht}|

ρ∗ is only tractable when the environment is deterministic. The learned PFN ρ is a causal Transformer
pretrained on randomly generated trajectories. More details about consistency, the PFN architecture, and
training process are in Appendices E.3.1 and E.3.2.
Validation. After the policy collects a trajectory of T guesses and responses hT , we measure how
much probability mass the world model places on the true secret code. We construct a synthetic
action/observation pair ãv =c, s̃v =(L,L) — the true code paired with a perfect-score response — append
it to the trajectory, and report V =ρ∗(s̃v |hT ,ãv ). For the noisy variant, we use ρ instead of ρ∗.
Results. As seen in Figure 4, rsur achieves near-optimal performance in the standard setup given that
the environment has no source of aleatoric noise, matching the performance of training directly for the
task. rsum and rdl also achieve comparable performance. In this setting, all reward functions perform
consistently across both the Bayesian oracle and the trained PFN, further validating that sequence models
can serve as effective predictive models for intrinsic reward computation.
However, the introduction of noisy pegs significantly alters these dynamics. In the noisy variant, the
performance of the policy trained with rsur falls even below the random baseline. Conversely, policies
trained with rsum and rdl remain robust, retaining high performance despite the corruption mechanism.
This confirms that rsur becomes a liability in environments with stochastic transitions, while rsum and
rdl consistently identify informative actions.
8

5.3 Alchemy
Alchemy (Wang et al., 2021) is a symbolic meta-learning environment. Each environment defines a fixed
set of transition rules mapping (stone, potion) input pairs to transformed output stones, and the agent must
discover these rules through sequential experimentation.
The environment is parameterized by a discrete ID θ, which determines the transition dynamics. Stones are
four-dimensional discrete vectors whose dimensions have (3,3,3,4) possible values respectively, and potions
take one of 6 values. At each step the policy selects both the initial stone and the potion (it,pt) and observes
final stone ft from the environment. Consecutive observations are conditionally independent given θ (i.e.
it+1 is chosen freely and need not equal ft). Therefore, Alchemy is BED with at =(it,pt), and st+1 =ft.
Similar to Mastermind, we consider a noisy variant of the environment in which one randomly chosen
stone type per episode is designated as “evil.” Any transition whose input stone matches the evil stone
has its output replaced with a uniformly random stone.
Predictive model. Like Mastermind, the oracle ρ∗ performs exact Bayesian inference by enumerating
all N candidates, and eliminating those that are not consistent (all observed transitions match θ’s rules).
ρ∗ is only tractable when the environment is deterministic. The learned PFN ρ is a causal Transformer
with an autoregressive GRU decoder that factorizes output prediction across the components of ft (see
Appendix E.4.2 for full architectural and training details).
Validation. After the policy collects a trajectory of T transitions hT , we evaluate how well the world
model can predict held-out transitions from the same environment. From the ground-truth transition table
of the current environment ID, we randomly sample M=10 transitions, excluding any whose initial stone
matches the evil stone (so that only clean transitions are used). These are appended sequentially to the
PM
1
trajectory, and we report the mean predictive log-probability V = M
j=1 logρ(s̃j | h1:T ,ã1:j−1 ,s̃1:j−1 ).
For the non-noisy environment we evaluate under both the Bayesian oracle ρ∗ and the trained PFN ρ;
for the noisy (evil stone) variant we evaluate under ρ only.
Results. We observe a similar pattern as Mastermind in the Alchemy environment in Figure 4. In the
noiseless task, rsur and rsum both exhibit strong performance, followed by rdl. Under the noisy variant,
rsur again demonstrates a failure to generalize, with performance below that of a random policy. In contrast,
rsum maintains its superiority with both oracle and PFN, achieving the highest validation log-probability.
The results across all three domains underscore the limitation of surprisal-based curiosity in realistic noisy
settings, and demonstrate the robustness of rsum and rdl. They also demonstrate the effectiveness of
trained in-context learners as predictive models in these settings, as replacements for the intractable BIG.

6 Discussion and Future Work
We demonstrated that in-context learners can efficiently evaluate prediction-based intrinsic curiosity rewards,
under certain conditions. In Bayesian Experimental Design (BED) settings, our proposed reward rsum and
description length reward from prior work rdl asymptotically approximate Bayesian information gain (BIG)
and drive exploration effectively, though rdl suffers from asymptotic pathologies that rsum avoids. Both
avoid the pitfalls of standard surprisal. This framework opens several promising directions for future work.
General BAMDPs. Extending this approach to general Bayes-Adaptive Markov Decision Processes
(BAMDPs) requires handling environments with temporal structure. Implementing rdl or BIG requires access to a model’s parameters, which is challenging using in-context learners that only expose the model’s predictions. A promising approach is to project the in-context learner’s hidden states into “task vectors” (Hendel
et al., 2023) that represent the environment’s latent dynamics. Modulating or manipulating these task vectors
counterfactually could allow the direct estimation of rdl or BIG in latent space. Attempting to approximate
rgap — which asymptotically converges to BIG — using long context lengths and gaps is also a possibility.
Training the in-context learner. Matching the true Bayesian posterior predictive over the distribution of
policy-sampled trajectories during training poses significant challenges. Large foundation models trained
on broad data mixtures offer powerful in-context learning, but they are often poorly calibrated to the true
Bayesian posterior predictive (Badola et al., 2025). Furthermore, standard causal Transformers suffer
from length generalization issues and positional encoding leakage, breaking the martingale properties
necessary for Bayesian coherence (Falck et al., 2024). While this is partially mitigated in BED by using
permutation-invariant sequence models trained on synthetic priors, covariate shift remains a primary
9

failure mode. Specifically, a model trained on trajectories from a random or fixed policy will degrade
when evaluated on informative trajectories collected by an active, reward-maximizing deployment policy
(Yadlowsky et al., 2023). Addressing this distribution shift may require techniques that jointly fine-tune
the predictive model and the policy (Ross et al., 2011; Ivanova et al., 2024; Azar et al., 2019), though
optimizing against non-stationary intrinsic rewards from a changing ρ might introduce instability.
Online RL setting. This work focuses on an episodic meta-RL setting, but translating these methods
to single-lifetime online reinforcement learning introduces several difficulties. First, the fixed context
window of sequence models limits the duration over which an agent can accumulate learning progress.
Second, in-context learning empirically exhibits saturation; predictive improvements decrease as the
context length grows (Elmoznino et al., 2025), perhaps requiring periodic weight updates to consolidate
long-term knowledge (Bornschein et al., 2024). Third, the rewards themselves become computationally
intractable in continuous online settings. Currently, the intrinsic reward computation is naturally episodic
and calculated only at the conclusion of a trajectory (where rsum evaluates over the remainder of the
fully unrolled sequence, and rdl requires trajectory reruns with the new parameters). Approximating
these episodic metrics for online scaling will require stochastic sampling or truncated evaluation windows.
Finally, exploration in domains with low-level action spaces is inherently difficult. Leveraging emergent
temporal and action abstractions within autoregressive models could allow intrinsic rewards to operate
over higher-level behaviors, improving the efficiency of information gathering (Kobayashi et al., 2025).
Comparing rsum and rdl. Empirically, we found that rsum and rdl both performed well, but that the
optimal one between the two depended on the environment in which they were deployed, suggesting that
they can be complementary. Theoretical analysis in BED settings established that rsum bounds BIG from
below, whereas rdl bounds it from above. The bounds for each are fundamentally different, rdl converging
as t→∞, and rsum as T →∞. rdl technically recovers BIG but its bias vanishes together with the signal
itself, and rsum should be more robust and approach BIG at finite t. However, our experiments show that
this distinction may not manifest in simple environments, and at finite T and t. Future work might be
able to characterize the properties of environments that influence these factors. In addition, because the
two bounds converge asymptotically from opposite sides, future work could explore hybridizing them
to yield a tighter, more stable estimator of true learning progress.

Acknowledgments and Disclosure of Funding
The authors acknowledge Seijin Kobayashi for helpful feedback and discussions. EE and SB are PhD
students at the Université de Montréal & Mila – Quebec AI Institute. GL is an Associate Professor at the
Université de Montréal and a Core Academic Member at Mila – Quebec AI Institute. EE acknowledges
support from Vanier Canada Graduate Scholarship #492702. GL acknowledges support from NSERC
Discovery Grant RGPIN-2018-04821, the Canada Research Chair in Neural Computations and Interfacing,
and a Canada-CIFAR AI Chair.

References
Aubret, A., Matignon, L., and Hassas, S. (2023). An information-theoretic perspective on intrinsic
motivation in reinforcement learning: A survey. Entropy, 25(2):327.
Azar, M. G., Piot, B., Pires, B. A., Grill, J.-B., Altché, F., and Munos, R. (2019). World discovery models.
arXiv preprint arXiv:1902.07685.
Badola, K., Simon, J., Hosseini, A., Carthy, S. M. M., Munkhdalai, T., Goyal, A., Kočiskỳ, T., Upadhyay,
S., Fatemi, B., and Kazemi, M. (2025). Multi-turn puzzles: Evaluating interactive reasoning and
strategic dialogue in llms. arXiv preprint arXiv:2508.10142.
Barto, A., Mirolli, M., and Baldassarre, G. (2013). Novelty or surprise? Frontiers in Psychology, 4.
Bellemare, M., Srinivasan, S., Ostrovski, G., Schaul, T., Saxton, D., and Munos, R. (2016). Unifying
count-based exploration and intrinsic motivation. Advances in neural information processing systems, 29.
Binz, M., Dasgupta, I., Jagadish, A. K., Botvinick, M., Wang, J. X., and Schulz, E. (2024). Meta-learned
models of cognition. Behavioral and Brain Sciences, 47:e147.
10

Bornschein, J., Li, Y., and Rannen-Triki, A. (2024). Transformers for supervised online continual learning.
arXiv preprint arXiv:2403.01554.
Bradley, H., Dai, A., Teufel, H. B., Zhang, J., Oostermeijer, K., Bellagente, M., Clune, J., Stanley, K.,
Schott, G., and Lehman, J. (2024). Quality-diversity through AI feedback. In The Twelfth International
Conference on Learning Representations.
Brown, T., Mann, B., Ryder, N., Subbiah, M., Kaplan, J. D., Dhariwal, P., Neelakantan, A., Shyam,
P., Sastry, G., Askell, A., et al. (2020). Language models are few-shot learners. Advances in neural
information processing systems, 33:1877–1901.
Burda, Y., Edwards, H., Pathak, D., Storkey, A., Darrell, T., and Efros, A. A. (2019). Large-scale study
of curiosity-driven learning. In International Conference on Learning Representations.
Chentanez, N., Barto, A., and Singh, S. (2004). Intrinsically motivated reinforcement learning. Advances
in neural information processing systems, 17.
De, S., Smith, S. L., Fernando, A., Botev, A., Cristian-Muraru, G., Gu, A., Haroun, R., Berrada, L., Chen,
Y., Srinivasan, S., Desjardins, G., Doucet, A., Budden, D., Teh, Y. W., Pascanu, R., Freitas, N. D., and
Gulcehre, C. (2024). Griffin: Mixing gated linear recurrences with local attention for efficient language
models.
Ding, L., Zhang, J., Clune, J., Spector, L., and Lehman, J. (2023). Quality diversity through human
feedback. In Second Agent Learning in Open-Endedness Workshop.
Du, Y., Kosoy, E., Dayan, A. L., Rufova, M., Gopnik, A., and Abbeel, P. (2023). What can AI learn from
human exploration? intrinsically-motivated humans and agents in open-world exploration. In Second
Agent Learning in Open-Endedness Workshop.
Duan, Y., Schulman, J., Chen, X., Bartlett, P. L., Sutskever, I., and Abbeel, P. (2016). Rl2: Fast
reinforcement learning via slow reinforcement learning. arXiv preprint arXiv:1611.02779.
Elmoznino, E., Marty, T., Kasetty, T., Gagnon, L., Mittal, S., Fathi, M., Sridhar, D., and Lajoie, G. (2025).
In-context learning and occam’s razor. In Forty-second International Conference on Machine Learning.
Falck, F., Wang, Z., and Holmes, C. (2024). Is in-context learning in large language models bayesian?
a martingale perspective. In Proceedings of the 41st International Conference on Machine Learning,
ICML’24. JMLR.org.
Fedorov, V. (1972). Theory of Optimal Experiments. Academic Press, NY.
Grau-Moya, J., Genewein, T., Hutter, M., Orseau, L., Deletang, G., Catt, E., Ruoss, A., Wenliang, L. K.,
Mattern, C., Aitchison, M., and Veness, J. (2024). Learning universal predictors. In Salakhutdinov,
R., Kolter, Z., Heller, K., Weller, A., Oliver, N., Scarlett, J., and Berkenkamp, F., editors, Proceedings
of the 41st International Conference on Machine Learning, volume 235 of Proceedings of Machine
Learning Research, pages 16178–16205. PMLR.
Hazan, E., Kakade, S., Singh, K., and Van Soest, A. (2019). Provably efficient maximum entropy
exploration. In International Conference on Machine Learning, pages 2681–2691. PMLR.
Hendel, R., Geva, M., and Globerson, A. (2023). In-context learning creates task vectors. In Findings
of the Association for Computational Linguistics: EMNLP 2023, pages 9318–9333.
Hester, T. and Stone, P. (2012). Intrinsically motivated model learning for a developing curious agent.
In 2012 IEEE International Conference on Development and Learning and Epigenetic Robotics (ICDL),
pages 1–6.
Hollmann, N., Müller, S., Eggensperger, K., and Hutter, F. (2022). Tabpfn: A transformer that solves
small tabular classification problems in a second. arXiv preprint arXiv:2207.01848.
Houlsby, N., Huszár, F., Ghahramani, Z., and Lengyel, M. (2011). Bayesian active learning for
classification and preference learning. arXiv preprint arXiv:1112.5745.
Houthooft, R., Chen, X., Duan, Y., Schulman, J., De Turck, F., and Abbeel, P. (2016). Vime: Variational
information maximizing exploration. Advances in neural information processing systems, 29.
11

Hughes, E., Dennis, M. D., Parker-Holder, J., Behbahani, F., Mavalankar, A., Shi, Y., Schaul, T., and
Rocktäschel, T. (2024). Position: Open-endedness is essential for artificial superhuman intelligence. In
Salakhutdinov, R., Kolter, Z., Heller, K., Weller, A., Oliver, N., Scarlett, J., and Berkenkamp, F., editors,
Proceedings of the 41st International Conference on Machine Learning, volume 235 of Proceedings
of Machine Learning Research, pages 20597–20616. PMLR.
Itti, L. and Baldi, P. (2009). Bayesian surprise attracts human attention. Vision research, 49(10):1295–1306.
Ivanova, D. R., Hedman, M., Guan, C., and Rainforth, T. (2024). Step-dad: Semi-amortized policy-based
bayesian experimental design. In ICLR 2024 Workshop on Data-centric Machine Learning Research
(DMLR), volume 2, page 21.
Kim, H., Kim, J., Jeong, Y., Levine, S., and Song, H. O. (2019). EMI: Exploration with mutual information.
In Chaudhuri, K. and Salakhutdinov, R., editors, Proceedings of the 36th International Conference on
Machine Learning, volume 97 of Proceedings of Machine Learning Research, pages 3360–3369. PMLR.
Klyubin, A. S., Polani, D., and Nehaniv, C. L. (2005a). All else being equal be empowered. In European
Conference on Artificial Life, pages 744–753. Springer.
Klyubin, A. S., Polani, D., and Nehaniv, C. L. (2005b). Empowerment: A universal agent-centric measure
of control. In 2005 ieee congress on evolutionary computation, volume 1, pages 128–135. IEEE.
Kobayashi, S., Schimpf, Y., Schlegel, M., Steger, A., Wolczyk, M., von Oswald, J., Scherrer, N., Maile,
K., Lajoie, G., Richards, B. A., et al. (2025). Emergent temporal abstractions in autoregressive models
enable hierarchical reinforcement learning. arXiv preprint arXiv:2512.20605.
Levy, G., Colas, C., Oudeyer, P.-Y., Carta, T., and Romac, C. (2025). Worldllm: Improving llms’ world
modeling using curiosity-driven theory-making. arXiv preprint arXiv:2506.06725.
Lindley, D. V. (1956). On a measure of the information provided by an experiment. The Annals of
Mathematical Statistics, 27(4):986–1005.
Little, D. Y. and Sommer, F. T. (2013). Learning and exploration in action-perception loops. Frontiers
in neural circuits, 7:37.
Lopes, M., Lang, T., Toussaint, M., and Oudeyer, P.-Y. (2012). Exploration in model-based reinforcement
learning by empirically estimating learning progress. Advances in neural information processing
systems, 25.
MacKay, D. J. (1992). Information-based objective functions for active data selection. Neural Computation,
4(4):590–604.
Mikulik, V., Delétang, G., McGrath, T., Genewein, T., Martic, M., Legg, S., and Ortega, P. (2020).
Meta-trained agents implement bayes-optimal agents. Advances in neural information processing
systems, 33:18691–18703.
Mohamed, S. and Jimenez Rezende, D. (2015). Variational information maximisation for intrinsically
motivated reinforcement learning. Advances in neural information processing systems, 28.
Müller, S., Hollmann, N., Arango, S. P., Grabocka, J., and Hutter, F. (2022). Transformers can do bayesian
inference. In International Conference on Learning Representations.
Nagler, T. (2023). Statistical foundations of prior-data fitted networks. In International Conference on
Machine Learning, pages 25660–25676. PMLR.
Ostrovski, G., Bellemare, M. G., Oord, A., and Munos, R. (2017). Count-based exploration with neural
density models. In International conference on machine learning, pages 2721–2730. PMLR.
Oudeyer, P.-Y. and Kaplan, F. (2007). What is intrinsic motivation? a typology of computational
approaches. Frontiers in neurorobotics, 1:108.
Oudeyer, P.-Y. and Kaplan, F. (2008). How can we define intrinsic motivation? In the 8th international
conference on epigenetic robotics: Modeling cognitive development in robotic systems. Lund University
Cognitive Studies, Lund: LUCS, Brighton.
12

Oudeyer, P.-Y., Kaplan, F., and Hafner, V. V. (2007). Intrinsic motivation systems for autonomous mental
development. IEEE Transactions on Evolutionary Computation, 11(2):265–286.
Pathak, D., Agrawal, P., Efros, A. A., and Darrell, T. (2017). Curiosity-driven exploration by self-supervised
prediction. In International conference on machine learning, pages 2778–2787. PMLR.
Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., Sutskever, I., et al. (2019). Language models are
unsupervised multitask learners. OpenAI blog, 1(8):9.
Ross, S., Gordon, G., and Bagnell, D. (2011). A reduction of imitation learning and structured prediction
to no-regret online learning. In Proceedings of the fourteenth international conference on artificial
intelligence and statistics, pages 627–635. JMLR Workshop and Conference Proceedings.
Salge, C., Glackin, C., and Polani, D. (2014). Empowerment–An Introduction, pages 67–114. Springer
Berlin Heidelberg, Berlin, Heidelberg.
Schiff, J. L. (1993). Normal Families. Universitext. Springer-Verlag, New York.
Schmidhuber, J. (1991a). Curious model-building control systems. In Proc. international joint conference
on neural networks, pages 1458–1463.
Schmidhuber, J. (1991b). A possibility for implementing curiosity and boredom in model-building
neural controllers. In From Animals to Animats: Proceedings of the First International Conference
on Simulation of Adaptive Behavior. The MIT Press.
Schmidhuber, J. (2009). Driven by compression progress: A simple principle explains essential aspects
of subjective beauty, novelty, surprise, interestingness, attention, curiosity, creativity, art, science, music,
jokes. In Pezzulo, G., Butz, M. V., Sigaud, O., and Baldassarre, G., editors, Anticipatory Behavior in
Adaptive Learning Systems, pages 48–76, Berlin, Heidelberg. Springer Berlin Heidelberg.
Schmidhuber, J. (2010). Formal theory of creativity, fun, and intrinsic motivation (1990–2010). IEEE
Transactions on Autonomous Mental Development, 2(3):230–247.
Schmüdgen, K. (2017). The Moment Problem, volume 277 of Graduate Texts in Mathematics. Springer.
Seitzer, M., Tavakoli, A., Antic, D., and Martius, G. (2022). On the pitfalls of heteroscedastic uncertainty
estimation with probabilistic neural networks. In International Conference on Learning Representations.
Stadie, B. C., Levine, S., and Abbeel, P. (2015). Incentivizing exploration in reinforcement learning with
deep predictive models. arXiv preprint arXiv:1507.00814.
Stanley, K. O. and Lehman, J. (2015). Why greatness cannot be planned: The myth of the objective. (No
Title).
Storck, J., Hochreiter, S., Schmidhuber, J., et al. (1995). Reinforcement driven information acquisition
in non-deterministic environments. In Proceedings of the international conference on artificial neural
networks, Paris, volume 2, pages 159–164.
Strehl, A. L. and Littman, M. L. (2008). An analysis of model-based interval estimation for markov
decision processes. Journal of Computer and System Sciences, 74(8):1309–1331.
Sun, Y., Gomez, F., and Schmidhuber, J. (2011). Planning to be surprised: Optimal bayesian exploration
in dynamic environments. In International conference on artificial general intelligence, pages 41–51.
Springer.
Wang, G., Xie, Y., Jiang, Y., Mandlekar, A., Xiao, C., Zhu, Y., Fan, L., and Anandkumar, A. (2024).
Voyager: An open-ended embodied agent with large language models. Transactions on Machine
Learning Research.
Wang, J., King, M., Porcel, N., Kurth-Nelson, Z., Zhu, T., Deck, C., Choy, P., Cassin, M., Reynolds, M.,
Song, F., Buttimore, G., Reichert, D., Rabinowitz, N., Matthey, L., Hassabis, D., Lerchner, A., and
Botvinick, M. (2021). Alchemy: A structured task distribution for meta-reinforcement learning. arXiv
preprint arXiv:2102.02926.
13

Wang, R., Lehman, J., Clune, J., and Stanley, K. O. (2019). Paired open-ended trailblazer (poet): Endlessly
generating increasingly complex and diverse learning environments and their solutions. arXiv preprint
arXiv:1901.01753.
Xie, S. M., Raghunathan, A., Liang, P., and Ma, T. (2022). An explanation of in-context learning as
implicit bayesian inference. In International Conference on Learning Representations.
Yadlowsky, S., Doshi, L., and Tripuraneni, N. (2023). Pretraining data mixtures enable narrow model
selection capabilities in transformer models. arXiv preprint arXiv:2311.00871.
Zhang, J., Lehman, J., Stanley, K., and Clune, J. (2024). OMNI: Open-endedness via models of human
notions of interestingness. In The Twelfth International Conference on Learning Representations.

14

Appendix A Additional Prior Work on Intrinsic Curiosity
Surprisal in a Learned Latent Space. One effective approach for mitigating the problem of aleatoric
noise is to measure surprisal in a learned latent space that only encodes predictable information about
the observation (Pathak et al., 2017; Kim et al., 2019; Burda et al., 2019). However, these methods
struggle in partially observed environments where the state representation depends on a long history,
and also remain sensitive to sources of aleatoric noise that are produced by the policy’s actions (Burda
et al., 2019). Ultimately, the problem of how to train a latent space for surprisal-based exploration that
is robust to aleatoric noise remains open. Since our investigation into the use of in-context learners for
intrinsic curiosity leverages only ρ’s input/output interface for computing observation-level prediction
errors, we do not consider methods that operate in latent space (although if in-context learners are trained
in an appropriate latent space, the approach might be viable).
Novelty. An approach with a long history in reinforcement learning is to seek novel states of the
environment, as measured by visitation counts or density models (Hazan et al., 2019; Strehl and Littman,
2008; Bellemare et al., 2016; Ostrovski et al., 2017). Novelty is deeply related to surprisal; while the two
are not quite equivalent (Barto et al., 2013), they both suffer from the same fundamental problem: noisy
regions of the environment with high observation entropy are a reliable source of both surprisal and novelty.
Empowerment. Empowerment is an alternative framework for intrinsic motivation that, instead
of gathering observations that improve a model of the environment, aims to explore regions of the
environment that are controllable by the policy (Klyubin et al., 2005a,b; Salge et al., 2014). Specifically,
empowerment is defined as the channel capacity of the policy’s actuation channel: I(S ′;A | S) where
I is mutual information, S is a random variable for the history of all past states, A is a random variable
for the agent’s current action, and S ′ is a random variable for the state(s) the policy observes after some
future horizon following the action (S ′ can represent a single future state at a fixed horizon, or potentially
a trajectory of such states). The distributions over A, S, and S ′ depend on both the environment and the
policy, and using empowerment as an intrinsic reward involves maximizing I(S ′;A|S) with respect to the
latter. Intuitively, this yields policies that learn to exert control over their environment by exploring regions
of the state space where actions provide substantial information about future environment dynamics.
It is unclear how empowerment theoretically relates to the above methods that seek to improve a model of
the environment. While exploring controllable regions of an environment might improve a model as a side
effect (e.g., knowing what is and is not controllable involves understanding the environment’s dynamics at
some level), the two are not equivalent in general. While empowerment appears to be a viable exploration
strategy empirically (Mohamed and Jimenez Rezende, 2015) and can be highly effective in modeling
human exploration behaviour (Du et al., 2023), we instead focus here on intrinsic rewards that explicitly
aim to improve a model of the environment.
Open-endedness. The aims of intrinsic curiosity closely align with those of research on “open-endedness”
(Stanley and Lehman, 2015), typically characterized as an ongoing process that continually generates
new data, tasks, or behaviours that are interesting, learnable, novel, without being too difficult relative
to an agent’s current capabilities. Most existing approaches operationalize open-endedness either through
diversity/complexity heuristics (Wang et al., 2019, 2024) or through proxies intended to capture subjective
human notions of interestingness (Ding et al., 2023; Bradley et al., 2024; Zhang et al., 2024).
A recent position paper attempts to mathematically formalize the concept of open-endedness (Hughes
et al., 2024), defining it as a process that continually generates data that is (a) surprising and (b) learnable,
where both are defined in terms of the prediction errors of a world model that has observed the data up to
a particular timepoint. Notably, their learnability component closely resembles learning progress rewards.
We further hypothesize that their explicit novelty term is redundant: if learning progress is sustained and
does not stagnate, then novelty and surprisal are already implied, because continued progress requires
exposure to information not yet captured by the model.

Appendix B Assumptions for Theoretical Results
The main text states six assumptions in compact form. We unpack each here, flagging the nuances that
matter for the derivations.
15

(i) Markovian, stationary dynamics given θ. For each fixed θ, the transition kernel p(st+1 | st,at,θ)
is Markov in the state-action chain and time-independent. Stationarity rules out time-indexed families
{Pt}t in which the conditional law itself depends on chain time. Markov dynamics given θ are what let us
factorize ρ’s joint over future observations (Lemma 4.1); stationarity ensures that masking-based rewards
(rsum and the NDIGO reward of Azar et al. (2019)) can be evaluated by anchoring their kernels at the
actual chain times.
(ii) ρ is exactly
Bayesian over θ. The sequence model emits the exact posterior-predictive
R
ρ(st′ | ht′ ) = p(st′ | st′ −1,at′ −1,θ)p(θ | ht′ )dθ, with prior p(θ) matching the distribution of training
tasks. In practice ρ is a finite-capacity neural network and exact Bayesian computation is an idealization;
Appendix B.2 discusses how approximation error propagates into reward biases.
(iii) Observation-only masking. The masked history ht′ \t replaces st with a mask token while leaving
every other state and every action intact. We assume ρ’s response to ht′ \t is the posterior-predictive
obtained by Bayesian marginalization over the masked st, treating actions as still observed. This is a subtle
assumption when ρ is a learned sequence model: masked queries are out-of-distribution unless ρ has been
trained to handle them. See Appendix B.3.
(iv) Posterior consistency. The selection rule generates trajectories under which p(θ | ht) → δθ∗ in
probability as t → ∞. This requires (a) θ identifiability from the achievable observation distributions
under the policy and (b) sufficient coverage of the action space (each action taken often enough to
inform θ). Under standard regularity conditions (smooth parametric model, positive-definite per-arm
Fisher
I(θ) ≻ 0 uniformly on the parameter support), Bernstein–von-Mises gives the rate
 information

Var p(θ |ht) ∼I(θ∗)−1/t, controlling both the residual in Theorem 3 and the Jensen gap in Theorem 4
at the 1/t scale. Strictly, the consistency assumption alone is what the framework requires; the Fisherinformation regularity becomes relevant only when one wants asymptotic rates rather than asymptotic limits.
(v) Policy-generated actions. Actions are sampled from πϕ conditional on past observations. Because
actions are not generated by the environment, conditioning on a future action does not update the posterior
over θ: p(θ | ht,at,at+1,...,at′ −1) = p(θ | ht). This permits treating future actions as fixed inputs in the
derivations, and is equivalent to the standard interventional treatment of actions in causal Markov chains.
(vi) Mixing given θ. For each θ in the support of p(θ), I(st;st+k |θ,ht,at:t+k−1)→0 as k →∞. This
rules out absorbing states and other non-ergodic dynamics under which the Markov chain never forgets
st. Mixing is what makes the abductive bias of Theorem 3 (and its rgap-generalized analogues) decay
with the gap parameter K; without it, infinite-gap rewards still retain a bias from kernel-mediated coupling
between st and the deep future.
B.1 The Prior p(θ) and Meta-Learning
The prior p(θ) throughout this paper is the training distribution ptrain(θ) over MDPs — ρ is pretrained
on trajectories from MDPs sampled from ptrain, and its posterior-predictive is assumed to be Bayesian
under ptrain. This is a meta-learning setup, and the framework’s predictions extend to deployment insofar
as the deployed environment lies in supp(ptrain). We treat deployment mismatch on θ as a separate source
of bias and adopt the train-prior framing throughout.
A more pointed meta-learning concern is that ρ’s training data — pairs of trajectories and their
corresponding posterior-predictives — depends not only on ptrain(θ) but on the behavior of the policy
that generates the training trajectories. Pretraining ρ offline, separately from the deployment policy πϕ,
therefore requires the pretraining policy to cover the trajectory distribution adequately. This is mostly
tractable in BED settings, where trajectories factorize across actions given θ. Ensuring enough coverage of
action selection during training should suffice. It becomes increasingly difficult as the domain expands, and
especially in temporally rich BAMDPs where the trajectory distribution depends nonlinearly on the policy:
a deployed reward-maximizing policy can easily probe regions that the pretraining policy under-sampled,
leaving ρ uncalibrated where it matters most. In principle, this can be alleviated with large enough training
samples under enough random policies. Nevertheless, this is a practical matter to be considered.
This is a potential weakness of any offline-pretraining plus online-policy-training scheme: the predictive
model is fixed during policy optimization, but policy iteration may drift outside ρ’s effective training
16

support. On the other hand, the scheme opens the door to the use of massive pretrained but frozen
foundation models (maybe even LLMs) to support active ICL in a variety of environments. Practical
investigations of policy training in this regime, including the robustness of the method to departure from
Bayesian exactness of ρ (see next section), and the question of action selection bias, is exciting future work.
Another avenue for the approach to have practical legs at scale would be that of joint training of π and
ρ. This could take the form of a meta-learning regime in which the predictor and the data-collection policy
improve together so that ρ’s posterior-predictive remains accurate over the trajectories the policy actually
generates. We visit this question in Section 6.
B.2 Inexactitude of ρ’s Bayesian Posterior Predictive
Assumption (ii) demands that ρ be exactly Bayesian. In practice ρ is a finite-capacity neural network
trained by maximum likelihood on a finite dataset, so it differs from the exact Bayesian posterior-predictive
ρ∗ in a controllable but non-zero way. This subsection discusses the consequences of inexactitude as a
property of ρ as a learner — independent of any choice about how queries are conditioned on the trajectory.
Issues specifically arising from masked queries during training or inference are deferred to Appendix B.3.
Writing ∆(Y ):=DKL(ρ∗(·|Y )∥ρ(·|Y )) for the per-context KL between exact and approximate predictives at a conditioning Y , each reward inherits a bias that is a signed combination of such KLs. For example,
Eρ∗ [rtsur |ht] = I(st;θ |ht) + H(st |ht,θ) + ∆(ht),
showing that surprisal acquires an additional non-negative ∆(ht) on top of the noisy-TV bias. More
generally, rewards in F formed from log-ratios of predictives at two conditionings Y+,Y− pick up a
differential ¯
∆(Y+)− ¯
∆(Y−) rather than an absolute KL, since the two predictive errors partially cancel
under log-subtraction.
Two structural features:
• rsur’s bias is absolute. A single non-negative KL ∆(ht). Contexts where ρ predicts poorly
are systematically over-rewarded, on top of the aleatoric noisy-TV — a model-error-seeking
pathology specific to surprisal.
• Log-ratio rewards have differential bias. Rewards of the form logρ(· | Y+) − logρ(· | Y−)
inherit only the difference of ρ’s errors at Y+ and Y−. Uniform approximation error cancels;
only the asymmetry between the two conditionings survives.
The differential structure of log-ratio rewards is a robustness property: an across-the-board imperfection
in ρ cancels in the log-ratio, leaving only the part of the error that distinguishes the two conditionings.
Whether and how this differential is small in practice is a separate question — it depends on how ρ is
trained and queried. Figure E.1 in Appendix E.1.3 shows the difference of log-predictive terms between
an oracle observer and a trained PFN ρ for the Gaussian process experiment. Figure 2 in the main text
shows very little difference in reward training outcomes for the same experiment.
B.3 Training ρ With vs. Without Masked Inputs
Computing rsum (and analogously the NDIGO reward of Azar et al. (2019)) requires evaluating ρ on
histories with one or more past states masked out. A sequence model trained with standard autoregressive
next-token prediction will never have seen a mask token in its training data, so its behavior on masked
queries is out-of-distribution. Two training strategies are natural:
Standard autoregressive training. ρ is trained on natural (unmasked) trajectories. At inference,
predictives at masked conditioning sets reflect whatever extrapolation the model performs, with no
guarantee of agreement with the Bayesian marginalization over the masked observation. This is the source
of the differential bias described in Appendix B.2.
Masked training. ρ is trained with random masking of past observations during training, in the spirit
of masked language modeling. ρ then learns predictives that are well-calibrated with respect to the
marginalized joint, making mask-baseline rewards potentially more reliable.
We remark that these considerations impact reward evaluation in the full BAMDP setting where parts
of transition tuples (st−1,at−1,st) need to be masked. However in the BED setting, masking simplifies
17

to simply removing observations from pairs (at−1,st) and is not subject to the subtleties described above.
Our experiments take place in the BED setting, but a more general implementation of ICL intrinsic rewards
should consider the points above.

Appendix C Proofs for Theoretical Results
C.1 Interventional Factorization
Several of our derivations rely on factorizing ρ’s joint over future observations into a product of one-step
posterior-predictives. The factorization hinges on two structural features: (a) Markov dynamics given
θ (assumption (i)), and (b) policy-generated actions that do not update the θ-posterior (assumption (v)).
The second is what makes actions interventional in the causal sense: they enter the joint as fixed inputs,
not as random variables to be modeled.
Lemma 4.1 (Interventional factorization). For t1 <t2 and any action sequence at1 :t2 −1,
ρ(st1 :t2 |ht1 ,at1 :t2 −1) =

t2
Y

ρ(sτ |ht1 ,st1 :τ−1,at1 :τ−1),

τ=t1

and the same identity holds with masked histories provided masked states lie outside [t1,t2].
Q
Proof. Under (i), the joint factors as τ p(sτ | sτ−1, aτ−1, θ). By assumption (v), conditioning on
future actions does not update the posterior over θ. Marginalizing θ on both sides gives the product of
posterior-predictives. Assumption (iii) extends to masked histories.
This factorization is what allows rsum’s telescoping representation rtsum =pmi(st;st+1:T |ht,at:T −1) to
be used in the proof of Theorem 3.
C.2 Proof of Theorem 1
Theorem 1 (Impossibility of BIG identification in F). Let M be the class of BAMDPs satisfying (i)–(v)
above, whose transition kernels are neither deterministic nor independent across time given θ. Then for
every rt ∈F, there exists M ∈M with EM [rt |ht]̸= I(st;θ |ht).
Remark. The argument is a marginal-indistinguishability counterexample: we construct two BAMDPs
in M on which any rt ∈ F has the same unconditional expectation but for which the expected BIG
differs. Since an unbiased per-history estimator of BIG forces matched unconditional expectations, the
contradiction settles the theorem.
Proof.
Step 1: Unconditional reduction. Suppose rt ∈ F satisfies the per-history identity
EM [rt |ht]=I M (st;θ |ht) for every history ht and every M ∈M. Taking unconditional expectation,


EM [rt] = EM I M (st;θ |ht) .




We will exhibit M1,M2 ∈ M with EM1 [rt] = EM2 [rt] but EM1 I(st;θ | ht) ̸= EM2 I(st;θ | ht) ,
contradicting the per-history identity for at least one of them. We refer to such a pair (M1,M2) — or, since
the kernel is fixed in our construction, the corresponding prior pair (p1,p2) — as a witness to the theorem.

Step 2: E[rt] depends only on the marginal trajectory distribution. Each rt =f (ρ(Xi |Yi))i∈I ∈F
has finite touch horizon

Q := max τ :τ is a chain index appearing in some Xi or Yi ,
M
i.e., the largest chain index referenced by the reward. Under Assumption (ii), ρ(X | Y ) = Pmarg
(X | Y )
M
where Pmarg is the marginal trajectory law of M (with θ integrated out). Taking unconditional expectation,
h
i
M
M
EM [rt] = EPmarg
f (Pmarg
(Xi |Yi))i∈I ,
M
which depends on M only through Pmarg
(s1:Q,a1:Q−1). In particular, two BAMDPs with identical
marginal trajectory distributions on the first Q steps yield identical E[rt].

18

Step 3: A non-degenerate kernel family with prior-dependent BAMDPs. Take the BAMDP family
with state space S ={0,1}, a single (dummy) action, initial state s1 ∼Bernoulli(0.5), and transition kernel
p(sτ+1 ̸= sτ |sτ ,θ) = θ,

θ ∈(0,0.5).

The kernel is non-deterministic (θ > 0) and not independent across time given θ (θ ̸= 0.5), so each fixed
θ ∈ (0,0.5) yields a kernel meeting the non-degeneracy condition of Theorem 1. Different priors p(θ)
supported on (0,0.5) specify different BAMDPs in M.
The marginal trajectory distribution of a sequence s1:Q depends only on the number of state flips
k =#{τ :sτ+1 ̸= sτ }:
Z 0.5
p
θk (1−θ)Q−1−k p(θ)dθ.
Pmarg
(s1:Q) = 21
0

The integrand is a polynomial in θ of degree at most Q−1. Expanding,
p
Pmarg
(s1:Q) = 12

Q−1
X

βj (k)mj (p),

j=0

R
where mj (p) = θj p(θ)dθ is the j-th moment of p and the βj (k) are combinatorial constants. Hence
p
Pmarg
(s1:Q) depends on p only through its first Q−1 moments.
By the truncated Hausdorff moment problem (Schmüdgen, 2017), the set of probability measures on (0,0.5)
matching any prescribed first Q−1 moments is convex with multiple distinct extreme points. Choose
two distinct priors p1,p2 on (0,0.5) that match in their first Q−1 moments. Setting M1 =(kernel,p1) and
M2 =(kernel,p2), both lie in M, and by Step 2,
EM1 [rt] = EM2 [rt].
Step 4: Expected BIG differs. Decompose




EM I(st;θ |ht) = HM
marg (st |ht ) − Ep H(st |st−1 ,θ) .
The marginal entropy HM
marg (st |ht ) is identical for M1 and M2 (Step 3, marginals match). The aleatoric
term is




Ep H(st |st−1,θ) = Ep Hbin(θ) ,
where Hbin(θ)=−θlogθ−(1−θ)log(1−θ) is the binary entropy function. Since Hbin is not a polynomial,
its expectation under p is not determined by any finite number of moments of p. By the truncated moment
problem, we may
in the first
 choose p1,p2 matching

 Q−1 moments but with Ep1 [Hbin(θ)]̸= Ep2 [Hbin(θ)].
Therefore EM1 I(st;θ |ht) ̸= EM2 I(st;θ |ht) .




Conclusion. We have EM1 [rt] = EM2 [rt] but EM1 I(st;θ | ht) ̸= EM2 I(st;θ | ht) . The per-history
identity EM [rt |ht]=I M (st;θ |ht) implies matched unconditional expectations, so it must fail on at least
one of M1,M2. Since the construction works for any rt ∈F, the theorem follows.
C.3 Proof of Theorem 2
Theorem 2 (Decomposition of rsur). Under (i)–(iii),
E[rtsur |ht] = I(st;θ |ht) + H(st |ht,θ) .
| {z }
aleatoric entropy

H(st |ht,θ)=H(st |st−1,at−1,θ) is non-negative and does not vanish as θ becomes identified.
Proof. E[− log ρ(st | ht) | ht] = H(st | ht). By the conditioning-information identity,
H(st | ht) = H(st | ht, θ) + I(st; θ | ht). Under (ii), ρ’s θ-conditional predictive equals the true
kernel, so H(st |ht,θ)=H(st |st−1,at−1,θ).
19

C.4 Proof of Theorem 3
Theorem 3 (Decomposition of rsum). Under (i)–(iii) and (v),
E[rtsum |ht,at:T −1] = I(st;θ |ht) + I(st;st+1 |θ,ht,at) −I(st;θ |ht,at:T −1,st+1:T ).
{z
} |
{z
}
|
one-step “abductive”

“residual”

Both terms are non-negative. Under (iv), the residual vanishes as T →∞; the abductive does not.
PT
′
Proof. By Lemma 4.1,
| ht′ ) = log ρ(st+1:T | ht, st, at:T −1) and
t′ =t+1 log ρ(st
PT
sum
′
′
= pmi(st;st+1:T | ht,at:T −1).
t′ =t+1 logρ(st | ht \t ) = logρ(st+1:T | ht ,at:T −1 ). Subtracting, rt
sum
Take expectation: E[rt ]=I(st;st+1:T |ht,at:T −1).
Applying the chain rule against θ:
I(st;st+1:T |ht,at:T −1)=I(st;θ |ht,at:T −1)
−I(st;θ |ht,at:T −1,st+1:T )
+I(st;st+1:T |θ,ht,at:T −1).
Future actions do not update the θ-posterior, so I(st;θ | ht,at:T −1) = I(st;θ | ht). By Markov given θ,
st ⊥ st+2:T | st+1,θ, and so I(st;st+1:T | θ,ht,at:T −1) = I(st;st+1 | θ,ht,at) after dropping d-separated
future actions.
Vanishing residual term. Under assumption (iv), p(θ |ht,at:T −1,st+1:T )→δθ∗ in probability as T →∞;
further conditioning on st cannot move a delta, so the residual term vanishes.
C.5 The Log-Ratio Subclass and Its Chain-Rule Decomposition
The proof of Theorem 1 settles the impossibility for the entire class F via the unconditional reduction.
A complementary structural perspective is available for a specific sub-class of F — log-ratio rewards
— whose expected value reduces to an observation-space mutual information rather than to an entropy.
This subsection isolates that sub-class and gives the chain-rule decomposition that underlies the named
confound terms in rsum’s decomposition (Theorem 3) and in the rone(K) decomposition (Appendix C.6).
P
The log-ratio subclass FLR. For any linear combination of log likelihoods rt = icilogρ(Xi |Yi)∈F,
taking expectation under ρ∗ gives
X
X
X
E[rt] = − ciH(Xi |Yi) = − ciH(Xi) +
ciI(Xi;Yi).
i

i

i

P
The marginal-entropy contribution iciH(Xi) vanishes identically iff, for each distinct random variable
X appearing among the Xi’s, the coefficients on terms with that X sum to zero. Rewards meeting this
constraint can be written as a sum of matched log-ratios
X 

rt =
αk logρ(Xk |Yk+)−logρ(Xk |Yk−) .
k

We denote this sub-class FLR. Membership:
• rtsum ∈FLR: each summand is a paired log-ratio with Xk =st′ for the same future state.
• rtone(K)∈FLR: a single paired log-ratio with X =st+K .
• rtsur ∈
/ FLR: its single unpaired term −logρ(st | ht) has expectation equal to the conditional
entropy H(st |ht), with the marginal entropy of st surviving.
Chain-rule decomposition. For rt ∈ FLR, the expected reward reduces to a signed sum of
observation-space conditional MIs:
X
E[rt] =
αj I(Aj ;Bj |Cj ),
j

with Aj ,Bj ,Cj subsets of the trajectory and θ absent from all arguments (since ρ marginalizes over it).
Each term decomposes via the chain rule against θ:
I(Aj ;Bj |Cj ) = I(Aj ;θ |Cj ) −I(Aj ;θ |Cj ,Bj ) +I(Aj ;Bj |θ,Cj ).
| {z } |
{z
} |
{z
}
signal-like

residual

20

abductive

Reading the three terms.
• Signal-like terms quantify how the observation subsets Aj inform θ given the conditioning Cj .
• Residual terms measure the θ-information that Aj retains after Bj is also observed.
• Abductive terms capture dependencies between observation subsets that operate through the
kernel’s dynamics rather than through their shared dependence on θ.
This decomposition is exactly what produces the named offsets in Theorem 3 (one-step abductive
and residual for rsum) and in Theorem 5 (K-step abductive and residual for rone(K)). It does not
extend to rewards outside FLR: rsur in particular requires its own analysis via the entropy chain rule
H(st |ht)=H(st |ht,θ)+I(st;θ |ht), yielding the BIG-plus-aleatoric form of Theorem 2.
Relation to Theorem 1. For log-ratio rewards, the chain-rule decomposition gives a useful diagnostic
of where the bias relative to BIG comes from: typically a non-vanishing abductive or a non-vanishing
residual. It is not, however, the engine of Theorem 1. The proof above (Appendix C.2) operates at the
level of unconditional expectations and works for the entire class F uniformly, including non-log-ratio
rewards, without invoking the chain-rule decomposition.
C.6 NDIGO reward Decomposition
The NDIGO reward of Azar et al. (2019) is the single-summand analogue of rsum at horizon K. We thus
refer to it as rone(K), and define in the ρ setting as:
rtone(K) := logρ(st+K |ht,st,at:t+K−1)−logρ(st+K |ht,at:t+K−1).
Theorem 5 (Decomposition of rone(K)). Under assumptions (i)–(iii) and (v),
E[rtone(K)|ht,at:t+K−1] = I(st;θ |ht)
+I(st;st+K |θ,ht,at:t+K−1)
−I(st;θ |ht,at:t+K−1,st+K ).
Proof. By assumption (v), ρ(st |ht,at:t+K−1)=ρ(st |ht), hence rtone(K)=pmi(st;st+K |ht,at:t+K−1)
(where pmi is point-wise mutual information). Take expectation and apply the chain rule against θ as
in the proof of Theorem 3.
At finite K the residual I(st;θ | ht,at:t+K−1,st+K ) does not vanish: a single K-step-ahead observation
does not identify θ. rone(K) is therefore doubly biased relative to I(st;θ | ht) at finite K (abductive
plus persistent residual), and under BED structure reduces to I(st;θ | ht) minus a residual. In the limit
K →T −t, rone(K) approaches a single-summand analogue of rsum.
C.7 Beyond Finite Touch Horizon: The Gap Reward
The decomposition theorems above place rsum and rone(K) at opposite structural extremes within the
log-ratio subclass:
• rtsum queries the entire future block st+1:T with no gap. Its epistemic residual vanishes as T →∞
(the block contains infinite data, identifying θ), but its one-step abductive I(st;st+1 | θ,ht,at)
persists — the block starts immediately at t+1, fully coupled to st through the Markov kernel.
• rtone(K) queries a single state st+K at gap K. For K → ∞ in a mixing chain, the abductive
I(st;st+K | θ,ht,at:t+K−1) vanishes; but the epistemic residual I(st;θ | ht,at:t+K−1,st+K )
persists — a single state cannot identify θ.
rsum controls the residual; rone controls the abductive. Each pushes one of two independent structural
dials. This invites a unification: query a block that simultaneously starts at a gap K and extends to the
trajectory horizon T .
Definition 2 (Gap reward). For 1≤K ≤T −t,


rtgap(K) := logρ st+K:T |ht,st,at:T −1 −logρ st+K:T |ht,at:T −1 .
21

The two limits of Definition 2 recover the rewards above. At K = 1, the conditioning block extends
from t+1 to T and Lemma 4.1 together with assumption (iii) yields rtgap(1)=rtsum exactly. Restricting
the block of rtgap(K) to its first state st+K recovers rtone(K). rgap is the two-parameter family that
interpolates between them by independently choosing a gap K and a block size T −t−K +1.
Beyond assumptions (i)–(v), the gap-reward analysis crucially uses assumption (vi): mixing of the chain
given θ, ruling out absorbing states and other non-ergodic dynamics under which the chain never forgets st.
Theorem 6 (Decomposition of rgap). Under (i)–(iii) and (v),
E[rtgap(K)|ht,at:T −1] = I(st;θ |ht)
+I(st;st+K:T |θ,ht,at:T −1)
|
{z
}
abductive at gap K

−I(st;θ |ht,at:T −1,st+K:T ).
|
{z
}
residual at block end T

Both correction terms are non-negative.
Proof. By Lemma 4.1, rtgap(K)=pmi(st;st+K:T |ht,at:T −1); by (v), ρ(st |ht,at:T −1)=ρ(st |ht). Take
expectation and apply the chain rule against θ as in the proof of Theorem 3:
I(st;st+K:T |ht,at:T −1) = I(st;θ |ht,at:T −1)
− I(st;θ |ht,at:T −1,st+K:T )
+ I(st;st+K:T |θ,ht,at:T −1).
By (v), I(st;θ |ht,at:T −1)=I(st;θ |ht).
Theorem 6 subsumes Theorem 3 (K =1) and reveals that the abductive of rgap is a K-shifted analogue
of the one-step abductive of rsum. The decomposition immediately yields a positive counterpart to the
impossibility theorem in the iterated infinite limit.
Corollary 6.1 (rgap recovers BIG in the double limit). Under (i)–(vi),
lim lim E[rtgap(K)|ht,at:T −1] = I(st;θ |ht).

K→∞ T →∞

Proof. Inner limit (T → ∞, K fixed). As T → ∞ the conditioning block st+K:T grows without bound.
Under (iv), p(θ |ht,at:T −1,st+K:T )→δθ∗ in probability, so the residual I(st;θ |ht,at:T −1,st+K:T )→0.
Outer limit (K → ∞). With the residual at zero, only the abductive remains. By (i), the dependence of
st+K:T on st given θ funnels through st+K : I(st;st+K:T | θ,ht,at:T −1) = I(st;st+K | θ,ht,at:t+K−1)
(data-processing along the post-st+K chain). By (vi), this vanishes as K →∞.
Remarks.
• Outside F. The limit reward in Corollary 6.1 cannot be expressed as a function of finitely many
likelihoods, hence not a member of F. This is consistent with Theorem 1: at every finite T,K,
rtgap(K)∈FLR ⊂F and inherits the bias of Theorem 6; only the asymptotic limit escapes F.
• Marginalization burden. Computing rtgap(K) requires ρ to evaluate predictives on histories
where st is masked and the intermediate states st+1:t+K−1 are absent — effectively asking ρ
to marginalize over a gap of K −1 unobserved states. Assumption (iii) — that ρ’s response to
such queries is the correctly marginalized posterior-predictive — becomes increasingly strained
as the gap grows; see Appendix B.3.
• Mixing failure. Assumption (vi) fails for environments with absorbing states or other non-ergodic
structure given θ. In such cases the abductive does not decay with K and the double limit need
not yield BIG.
22

C.8 Necessity boundlessly growing gaps for Log-Ratio Rewards
Corollary 6.1 shows that an infinite gap together with an infinite block is sufficient to recover BIG
within a log-ratio reward. We now prove the converse: the same double-limit geometry is also necessary.
Concretely, any countable linear combination of matched log-ratios that universally identifies BIG must
place all of its weight at infinite gap, with each non-trivial block of infinite size.
Let FLR,T (cf. Appendix C.5) be the set of estimators which are linear combinations of log ratios involving
subsets of observations up to a horizon T , i.e.,




h
i
X
FLR,T =
cZ logρ(sZ |ht,st,at:T )−logρ(sZ |ht,at:T ) :cZ ∈R,∀Z ⊆{t+1,...,T } .


Z⊆{t+1,...,T }

The following theorem shows that for any sequence of estimators chosen from FLR,T which is asymptotically equal to the Bayesian Information Gain I(st;θ|ht) as T →∞ in a universal fashion over all BAMDPs,
this sequence must involve an unboundedly growing gap akin to the one discussed in Corollary 6.1.
Theorem 7 (Necessity of a growing gap). Let M be the class of BAMDPs satisfying (i)–(vi) whose
transition kernels are non-deterministic and not independent across time given θ. Suppose that (Rt,T )T
is a sequence of estimators such that
• Rt,T ∈FLR,T for all T , i.e.,
X
Rt,T =

h
i
cZ,T logρ(sZ |ht,st,at:T )−logρ(sZ |ht,at:T ) ,

Z⊆{t+1,...,T }

• limT →∞EM [Rt,T |ht,at:T ]=I(st;θ |ht) for every M ∈M and every ht,at:∞, and
P
• there exist constants C >0 and B ≥1 such that |Wk,T |≤ kZ =k |cZ,T |≤CBk for all k and T .2
If we define for each block of observations Z ⊂{t+1,...} the gap kZ :=min{k ≥1:t+k ∈Z} and write
X
Wk,T :=
cZ,T ,
Z⊆{t+1...,T }:
kZ =k

then
lim Wk,T =0.
P
In other words, as T →∞, almost all the weight Z cZ,T “will become concentrated on blocks of infinite
gap”.
T →∞

Proof. Step 1: Chain-Rule Decomposition.
By definition, each matched log-ratio term in FLR,T evaluates to a pointwise mutual information. Taking
the expectation of Rt,T and applying the chain rule against the environment parameter θ, we obtain:
X
EM [Rt,T |ht,at:T ]=
cZ,T I(st;sZ |ht,at:T )
Z

X

X
X
=
cZ,T I(st;θ |ht)+ cZ,T AZ − cZ,T EZ ,
Z

Z

Z

where AZ := I(st;sZ | θ,ht,at:T ) is the abductive term and EZ := I(st;θ | ht,at:T ,sZ ) is the epistemic
residual.
Step 2: Isolating the Abductive Bias.
The abductive term AZ captures dependencies generated purely by the known transition kernel, relying on
the prior p(θ) only through the posterior p(θ |ht). We may evaluate the limit on an environment M ∈M
whose prior is a degenerate point mass at some θ∗. For such a prior, there is no uncertainty about the
2 It is worth noting that this is a mild assumption. In practice, numerically stable estimators must satisfy this.

23

environment, so the true Bayesian Information Gain I(st;θ | ht) = 0 and all epistemic residuals EZ = 0
identically. The universal convergence hypothesis then reduces to:
X
lim
cZ,T AZ (θ∗)=0 for every θ∗.
(7)
T →∞

Z

Step 3: The Markov Funnel.
Under assumption (i), conditional on the exact parameter θ∗, the environment is Markovian. By the
data-processing inequality, the dependence of any block sZ on the state st must funnel strictly through
the chronologically earliest state in that block, st+kZ . Dropping the separated future actions, we have:
AZ (θ∗)=I(st;st+kZ |θ∗,ht,at:t+kZ −1):=IkZ (θ∗).
Grouping the terms in equation 7 by their gap kZ =k, we rewrite the limit in terms of the gap weights Wk,T :
lim

T
X

Wk,T Ik (θ∗)=0 for every θ∗.

T →∞
k=1

(8)

Step 4: AR(1) Instantiation and Power Series Extraction.
To evaluate equation 8, we instantiate M with the Gaussian AR(1) family parameterized by α ∈ (0,1),
for which the mutual information across a gap k is Ik (α)=− 21 log(1−α2k ). Letting x=α2 ∈(0,1), we
define the sequence of functions:
FT (x):=

T
X


Wk,T −log(1−xk ) .

k=1

By hypothesis, limT →∞ FT (x) = 0 for all x ∈ (0,1). We extend FT (x) to the complex plane as FT (z),
which is analytic on the open unit disk |z| < 1. Expanding the principal branch of the logarithm in its
P∞ km
Maclaurin series −log(1−zk )= m=1 zm , we express FT (z) as:
∞
X

∞
zkm X Vn,T n
=
z ,
m n=1 n
m=1
k=1
P
where we have grouped terms by n=km and defined Vn,T := d|n, d<T dWd,T .

FT (z)=

T
X

Wk,T

Now recall
Pthat the theorem statement assumes that there exist constants C > 0 and B ≥ 1 such that
|Wk,T | ≤ kZ =k |cZ,T | ≤ CBk for all k and T . For z strictly inside the unit disk, we may bound the
P∞
logarithmic term using its Maclaurin series: |−log(1−zk )|≤ m=1|z|km/m≤|z|k /(1−|z|). Applying
our exponential bound to the weights yields:
|FT (z)|≤

T
∞
X
C X
|Wk,T ||−log(1−zk )|≤
(B|z|)k .
1−|z|
k=1

k=1

This geometric series converges absolutely for B|z| < 1. Thus, defining a bounding radius
R := min(1/2,1/B), the sequence of functions {FT (z)} is uniformly bounded by a finite constant on
any closed ball B(0,r) with r <R.
Because FT (x)→0 pointwise on the real interval (0,R), and this interval contains an accumulation point
strictly within B(0,R), the Vitali-Porter Convergence Theorem (Schiff, 1993, Section 2.4) guarantees
that FT (z) converges uniformly to 0 on any strictly smaller closed contour γ enclosing the origin. By
Cauchy’s Integral Formula, the n-th Maclaurin coefficient is given by:
I
1
FT (z)
Vn,T
=
dz.
n
2πi γ zn+1
Since FT (z) converges uniformly to 0 on γ, we may pass the limit inside the integral, yielding:
lim

T →∞

Vn,T
=0 =⇒ lim Vn,T =0 for all n≥1.
T →∞
n

Step 5: Strong Induction.
We prove limT →∞ Wk,T = 0 by strong induction on k. For the base case k = 1, we have V1,T = W1,T
24

(since d < T trivially for T > 1), and thus limT →∞ W1,T = 0. For the inductive step, assume that
limT →∞Wd,T =0 for all proper divisors d<n. By definition, for T >n:
X
Vn,T =nWn,T +
dWd,T .
d|n
d<n

Taking the limit as T →∞:
0=n lim Wn,T +
T →∞


X 
d lim Wd,T =⇒ lim Wn,T =0.
T →∞
T →∞
{z
}
d|n |

d<n

=0

This holds for all integers n≥1, proving that all finite gap weights strictly vanish as T →∞. Consequently,
any estimator universally approaching BIG must concentrate its weight strictly at an unbounded, infinite gap.

Remark (relation to Theorem 1). The earlier impossibility theorem covers F at every finite touch
horizon Q: at finite T , no member of F identifies BIG, even without log-ratio structure. Theorem 7
extends the negative result into the limit: even allowing countable log-ratio combinations and asymptotic
T , the only escape is a structural double limit in which both the gap and the block grow without bound.
As mentioned in the main text, this imposes severe implementation limitations since predictive models
ρ are well suited for long sequence modeling (large T ) but less so for marginalization over unobserved
sequence blocks (large gaps).
C.9 Proof of Corollary 3.1
Corollary 3.1 (Decomposition of rsum in BED). Under (i)–(v),
E[rtsum |ht,at:T −1] = I(st;θ |ht) − I(st;θ |ht,at:T −1,st+1:T ),
i.e., the abductive of Theorem 3 vanishes structurally. As T →∞, E[rtsum]→I(st;θ |ht).
Proof. Under BED structure, given θ and the action sequence, st ∼p(·|at−1,θ) and st+1 ∼p(·|at,θ) are
independent. Hence I(st;st+1 |θ,ht,at)=0, and the abductive term in Theorem 3 drops out.
C.10 Proof of Theorem 4
Theorem 4 (Decomposition of rdl in BED). Under (i)–(v), with L(θ):=p(st |at−1,θ)/ρ(st |ht),
h
i
E[rtdl |ht] = I(st;θ |ht) + Est |at−1 log Ep(θ|ht ,st )[L(θ)]−Ep(θ|ht ,st )[log L(θ)] ,
i.e., BIG plus a non-negative Jensen gap. Both terms in the expectation vanish as t→∞ under (iv).
Proof. Under BED, p(st |st−1,at−1,θ)=p(st |at−1,θ), so the integral in Equation (4) simplifies:
Z
p(st |at−1,θ)p(θ |ht,st)dθ = Ep(θ|ht ,st )[p(st |at−1,θ)] = ρ(st |ht)Ep(θ|ht ,st )[L(θ)],
where the last equality uses the definition L(θ)=p(st |at−1,θ)/ρ(st |ht). Hence
rtdl = logEp(θ|ht ,st )[L(θ)].
By Jensen’s inequality,
rtdl = Ep(θ|ht ,st )[logL(θ)]+Jt,
with Jt ≥ 0 the Jensen gap. Bayes’ rule gives
 L(θ) = p(θ | ht, st)/p(θ | ht), so
Ep(θ|ht ,st )[log L(θ)] = DKL p(θ | ht, st) ∥ p(θ | ht) . Taking expectation over st, the KL term
integrates to I(st;θ |ht) (Bayesian-surprise identity).
25

Remark. Theorem 4 shows an important limitation of rdl. While technically, rdl does recover BIG
asymptotically, it does so as t→∞ which also implies that BIG I(st;θ |ht) itself vanishes. This means that
rdl biases vanish at the same time as the BIG signal itself does. In contrast, rsum also recovers BIG asymptotically, but it does so as T →∞, meaning that for long trajectories, one can hope to recover minimally biased
BIG signal for finite t. However, the practical effect of finite-time biases may or may not be consequential
for a useful policy, depending on the environment. Experiments in the main text illustrate this point.

Appendix D Implementing rdl in General BAMDPs vs. BED
The reward rdl defined in Equation (4) contains an integral term
Z
p(st |st−1,at−1,θ)p(θ |ht,st)dθ
that pairs the kernel at the trajectory input (st−1,at−1) with a posterior conditioned on the subsequent
observation st. We explain here why this combination is generically not implementable through ρ’s
standard predictive interface, and how the BED restriction restores implementability via a counterfactual
action commitment.
Why no ρ-implementation in general BAMDPs. A standard ρ query ρ(s′ | h) evaluates the kernel
at the most recent (s,a) in the conditioning history h, averaged under the posterior p(θ |h) that this same
history induces. The integrand above departs from this template in a structural way: the kernel input is
(st−1,at−1) from time t−1, while the posterior is p(θ |ht,st) from after st has been observed. In a general
MDP, where the kernel genuinely depends on the chain-position state, no rearrangement of conditioning
subsets in ρ’s query interface produces this combination — evaluating ρ at (st−1,at−1) gives the posterior
only up to time t−1, and evaluating ρ after st shifts the kernel input as well. Implementing rdl in general
BAMDPs therefore requires explicit Bayesian-update machinery beyond ρ’s forward-pass interface.
BED counterfactual identity. In BED the transition kernel has no st−1 dependence,
p(st |st−1,at−1,θ)=p(st |at−1,θ), so the integrand becomes
Z

p(st |at−1,θ)p(θ |ht,st)dθ = ρ st+1 =st ht,st,at =at−1 ,
recovering Equation (6). The right-hand side is a standard ρ query: condition on the history (ht,st), commit
to the action at =at−1 (a counterfactual on the action choice, valid because actions are policy-generated
and thus interventional), and read off the predictive probability of the next outcome equaling the observed
st. This makes rdl implementable in BED at the cost of one hypothetical rollout step in ρ’s context.
The key takeaway: BED collapses the chain-time mismatch by removing the st−1 dependence in the
kernel — an obstruction that no rearrangement of ρ’s queries can resolve in a general MDP. It could be
possible to address this issue with a modified sequence model architecture that allows multiple channels
for the same sequence location, together with a gating mechanism to implement a form of counterfactual
“superposition”. This remains a non-trivial design.

Appendix E Experimental Details
E.1 Gaussian Processes
E.1.1 Environment
The Gaussian Process (GP) environment presents the agent with an unknown function f : R2 → R that
must be explored through sequential point queries. At the start of each episode, a function f is sampled
from a Gaussian process prior f ∼GP(0,k), where k is the rational quadratic kernel:

−α
∥x−x′∥2
′
2
k(x,x )=σ 1+
,
(9)
2αℓ2
with α=1, lengthscale ℓ=4.0, and σ2 =1.
26

Since a GP sample is an infinite-dimensional function, we represent it in practice via finite-grid sampling:
we place R=10 equally spaced points along each of the d input dimensions in [−xmax,,xmax] and take
their Cartesian product, yielding a grid Xgrid of N = Rd locations. To draw a sample ygrid from this
multivariate Gaussian we use the standard Cholesky method. Function values at arbitrary query points
are then obtained via GP posterior interpolation. We use xmax =10.
When the agent queries location xt, it observes:
yt =f(xt)+ϵt,


2
ϵt ∼N 0,σnoise
(xt) ,

(10)

2
where the noise variance σnoise
(x) is spatially varying according to a fixed checkerboard noise map. Xgrid
2
is partitioned into an 8 × 8 grid of cells; Tiles alternate between high-noise (σnoise
= 5) and low-noise
2
(σnoise ≈ 0) regions. This creates a heteroscedastic noise landscape that an effective exploration policy
must learn to navigate.

E.1.2 Bayesian Oracle World Model
The Bayesian oracle leverages the closed-form GP posterior. Given a history of observations {(xi,yi)}t−1
i=0 ,
the posterior predictive distribution for a new query xt is Gaussian:

p(yt |xt,ht)=N yt;µt,σt2 ,
(11)
where the posterior mean and variance are given by the standard GP regression formulae:
−1
µt =k⊤
∗ (K +Σnoise ) y<t ,

(12)

−1
σt2 =k(xt,xt)−k⊤
∗ (K +Σnoise ) k∗ ,

(13)

2
2
with k∗ =[k(xi,xt)]t−1
i=0 , Kij =k(xi ,xj ), and Σnoise =diag(σnoise (x0 ),...,σnoise (xt−1 )).

For the predictive distribution used by the surprisal-based rewards, the predictive variance additionally
includes the noise at the query point:
2
σ̃t2 =σt2 +σnoise
(xt).
(14)
Per-step Surprisal The observation surprisal is the negative log-likelihood under the predictive Gaussian:
1
1
(yt −µt)2
−logp(yt |xt,ht)= log(2π)+ logσ̃t2 +
.
2
2
2σ̃t2

(15)

Per-step Information Gain (Bayesian Surprise) The information gain reward uses the KL divergence
between the GP posterior and the predictive observation distribution. In exact form:


σt2 ·(yt −µt)2
1
σt2
σt2
Gt = log 1+ 2
−
+
(16)
2 (x ))
2 (x ))2 ,
2
σnoise(xt)
2(σt2 +σnoise
2(σt2 +σnoise
t
t
where σt2 is the latent GP posterior variance (without observation noise).
E.1.3 In-Context PFN World Model
Data-Generating Process The PFN is trained to predict the next observation yt in-context from the
history of observed pairs. For each training example, a function f is sampled from the same GP prior
as the environment (rational quadratic kernel with α=1, ℓ=4.0, spatially-varying noise), and Ttrain =100
random query locations are drawn uniformly from [−10,10]2.
Model Architecture The PFN uses a causal Transformer decoder. Each past observation (xj ,yj ) is
embedded by summing a linear projection of xj and a linear projection of yj into a single “pair” token.
This pair token is interleaved with an isolated embedding of the next query xj+1, yielding a sequence
of length 2(t−1). The causal Transformer decoder has model dimension d=512, MLP hidden dimension
F = 1024, N = 12 layers, and H = 8 attention heads with head dimension d/H = 64. The model uses
LayerNorm and GELU activations. The Transformer output at each query-token position (odd positions)
is projected via a learned linear layer to produce a 2-dimensional output (µ̂t,σ̂t), representing a predicted
mean and log-standard-deviation.
27

Training The training objective is the mean negative log-likelihood of the observed y values under the
predicted Gaussian, with a variance-weighted loss to encourage better calibration (Seitzer et al., 2022):


B T
−1
X
X

β 1
1
(yt −µ̂t)2
L=
sg(σ̂t2) · log(2πσ̂t2)+
,
(17)
(T −1)B
2
2σ̂t2
t=1

b=1
where sg(·) denotes stop-gradient, σ̂t2 = exp(2σ̂t) is the predicted variance, and β = 1. The model is
−4
6

optimized using Adam with a learning rate of 10

, batch size B =128, for 10 training steps.

We collect random trajectories from Gaussian processes, and plot the correlation between the predictions
of the Bayesian oracle world model and the trained PFN world model in Figure E.1. The trained PFN
is effective at approximating the exact likelihood and, as evidenced by other results, is effective even in
settings where the oracle cannot be computed.

Figure E.1: The correlation between the values computed by an exact bayesian oracle vs our learned PFN for
likelihood and reward of randomly generated trajectories from Gaussian processes.

E.1.4 Policy
2.3
Reward
Validation

2.2

0.6

Validation = logp(Yval Xval)

0.7

Reward = rsur

2.1

0.8

2.0

0.9

1.9

1.0
1.1

1.8

1.2
1.7
0

2000

4000

step

6000

8000

10000

Figure E.2: Training reward vs Validation log-probability over the course of training a policy for Gaussian Process.
This highlights that in noisy environments, rsur can behave oppositely to the intended effect of learning the
environment’s dynamics.

The policy is trained using REINFORCE with a learned value baseline. At each training step, B = 32
trajectories of length T =26 are collected by rolling out the current policy in the environment. A single
trajectory-level reward R is computed from the world model, and the policy is updated with a single gradient
step per batch. The REINFORCE objective combines a policy gradient loss and a value baseline loss:
L=Lπ +λV LV ,
(18)
where λV =0.5.
28

Model Architecture The policy is a sequence model that processes the history of observations
recurrently. The backbone is a Griffin model (De et al., 2024), a recurrent architecture based on linear
recurrences (LRU). The Griffin configuration uses model dimension d=128, MLP dimension 256, LRU
dimension 128, 4 attention heads, and 2 recurrent layers.
At each step t, the observation ot = (xt,yt) is encoded by concatenating xt ∈ R2 and yt ∈ R, yielding a
3-dimensional vector, which is projected to the model dimension d=128 via a learned linear layer.
The sequence model output at each step is mapped to logits over the 64 discrete grid locations via a single
linear layer. A separate linear layer maps the sequence model output to a scalar value estimate V (st)∈R.
E.2 Decomposition of rewards
In Section 4.3, we analyzed the theoretical behaviour of curiosity rewards in BED environments. Corollary 3.1 showed that rsum decomposes into BIG−Residual terms, while Theorem 4 showed that rdl decomposes into BIG+JensenGap terms. In our Gaussian process environment using an Bayesian oracle observer,
all terms can be computed analytically. After having trained a policy with either rsum or rdl, we can
therefore check whether the reward empirically decomposes into the expected terms that our theory predicts.
Theoretical Decompositions in BED (Gaussian Process Oracle)
rdl ( [rdl] = BIG + JensenGap)
rsum ( [rsum] = BIG Residual)
3.5

3.5

3.0

3.0

Nats

2.5

2.5
Term
Reward
BIG
Nuisance (Residual)

2.0
1.5
1.0

Term
Reward
BIG
Nuisance (Jensen Gap)

2.0
1.5
1.0

0.5

0.5

0.0
0

5

10

t

15

20

25

0.0

0

5

10

t

15

20

25

Figure E.3: Empirical decompositions of (i) rsum into BIG and a subtracted residual term and (ii) rdl into an additive
Jensen gap, in a Gaussian process environment with oracle in-context learner.

Figure E.3 plots the resulting reward, BIG, and nuisance term as a function of time, averaged across
10 training seeds and 1000 unrolled trajectories. We find that both rewards decompose exactly into their
theoretical constituents, thus validating our theoretical analyses. Indeed, plotting BIG−Residual overlaps
exactly with rsum, and plotting BIG+JensenGap overlaps exactly with rdl.
E.3 Mastermind
At the start of each episode, the environment samples a secret code c∗ ∈ {0,1,...,C −1}L uniformly at
random, where C is the number of colours and L is the code length. In our experiments we set C = 6
and L=7, yielding 67 =279,936 possible codes. We hold out 10% of the possible codes for evaluation.
At each timestep t, the agent submits a guess gt ∈{0,1,...,C −1}L and receives a response (bt,wt) where:
• Black peg bt ∈{0,...,L} is the number of exact matches (correct colour in the correct position), and
• White peg wt ∈{0,...,L} is the number of colour matches (correct colour regardless of position),

PC−1
computed as wt = c=0 min count(c,c∗), count(c,gt) , where count(c,v) is the number of
occurrences of colour c in vector v.
Note that wt ≥ bt always holds, and colours are not double-counted: if the code contains N repeats of
a colour but the guess has M >N entries of that colour, only N contribute to wt.
29

The episode proceeds for a fixed trajectory length of T =8 guesses. A random initial guess is generated
at the start of each episode and forms the first observation.
E.3.1 Bayesian Oracle World Model
The Bayesian oracle world model maintains the exact posterior over secret codes by enumerating over all
C L possible codes. Given a history of guesses and responses {(g1,b1,w1),...,(gt−1,bt−1,wt−1)}, the oracle
computes the set of consistent codes—those that would have produced the observed responses for all past
guesses. Formally, a code c is consistent at step t if for all i<t: exact(c,gi)=bi and colour(c,gi)=wi.
The uniform prior over codes, combined with consistency filtering, yields the posterior probability of a
newly observed response (bt,wt) given a new guess gt as:
|{c∈Ct :exact(c,gt)=bt ∧colour(c,gt)=wt}|
p(bt,wt |ht =[ht−1,st−1,gt])=
,
(19)
|Ct|
where Ct denotes the set of codes consistent with all observations prior to step t.
E.3.2 In-Context PFN World Model
Data-Generating Process The PFN is trained on synthetically generated game trajectories. For each
training example, a secret code is sampled uniformly at random, and then a sequence of Ttrain =50 random
guesses is generated. Each guess is drawn uniformly from {0,...,C −1}L, and the corresponding responses
(bt,wt) are computed by the environment.
Model Architecture The in-context world model is a causal Transformer decoder that processes
interleaved guess and response tokens. Specifically, each guess gt is one-hot encoded over the C colours
for each of the L positions, yielding a vector of dimension C ×L, which is then projected to the model
dimension d via a linear layer. Each response (bt,wt) is one-hot encoded as a concatenation of two vectors
of dimension (L+1) each, giving a total dimension of 2(L+1), which is projected to d via a separate
linear layer. For a trajectory of T steps, the input sequence is constructed by interleaving pairs and isolated
guesses. A pair token is formed by summing the guess and response embeddings for the same timestep:
pt = embedg (gt)+embedr (bt,wt). The isolated guess token for the next step is embedg (gt+1). These
are interleaved as [p1,embedg (g2),p2,embedg (g3),...], resulting in a sequence of length 2(T −1).
The sequence is processed by a causal (left-to-right) Transformer decoder with the model dimension
d = 512, MLP hidden dimension = 1024, 12 layers, and 8 attention heads with head dimension = 64.
The Transformer output at every odd position (i.e., the isolated guess positions) is used to predict the
corresponding response. A linear readout maps the Transformer output to (L+1)2 logits, representing
the joint distribution over all possible (bt,wt) pairs via a softmax. The target is the index bt ·(L+1)+wt.
The in-context world model is trained to minimize the cross-entropy loss of predicting the response at
each step. In each training step, a fresh batch of B =128 random trajectories is generated on-the-fly (no
fixed dataset).
E.3.3 Policy
The policy is trained using REINFORCE with a learned value baseline. At each training step, a batch
of B = 32 trajectories of length T = 8 is collected by rolling out the current policy in the environment.
The total loss for REINFORCE is:
L=Lπ +λV LV ,
(20)
where λV =0.5. When using the in-context world model (PFN observer), an entropy bonus −λH H[πϕ]
with λH =0.01 is added to the loss to encourage exploration.
Model Architecture The policy model’s backbone is a Griffin model with the same configuration as
the one for GP. The guess gt is one-hot encoded over the C colours for each position, yielding a vector
of dimension C ×L. The exact matches bt and colour matches wt are each one-hot encoded into vectors of
dimension L+1. These are concatenated into a single vector of dimension C ·L+2(L+1) and projected
to the model dimension d via a linear layer.
The policy produces a value estimate and an action distribution. A linear layer maps the sequence model
output at each step to a scalar value estimate V (st). The action (a guess of L colour values) is generated
autoregressively, one position at a time, using a GRU cell. At each position k ∈{1,...,L}:
30

1. The GRU cell updates its hidden state using the current input (the sequence model output for
k =1, or the embedding of the previously selected colour for k >1).
2. A linear readout produces logits over the C colours for position k.
3. A colour is sampled from Categorical(softmax(logitsk /τ)), where τ is the temperature (set to
1.0 during training).
4. The selected colour is embedded and fed as input to the GRU for the next position.
The log-probability of the full action is the sum of the per-position log-probabilities:
PL
(k)
(1:k−1)
logπ(at |st)= k=1logπk (at |st,at
).
E.4 Alchemy
The Alchemy environment is inspired by the latent-chemistry paradigm of Wang et al. (2021). At the start
of each episode, an environment is sampled with a hidden chemistry: a set of deterministic transition rules
governing how potions transform stones. Stones are described by D =4 discrete dimensions with value
counts (3,3,3,4), yielding 3×3×3×4=108 distinct stone types. Potions are described by a single discrete
dimension with P =6 values. Each chemistry defines a fixed mapping from (initial_stone, potion) pairs
to resulting stones; if a given (stone, potion) pair has no matching rule, the stone is returned unchanged
and the transition is marked as invalid. The full set of chemistries and their transition rules are stored as
a precomputed transition table of shape [Nenvs,Nrules,2D+P ].
At each timestep t, the agent chooses an action at = (it,pt)—an initial stone and a potion—and the
environment returns an observation (vt,ft) where vt ∈ {0,1} indicates whether the transition was valid
(i.e., a matching rule exists in the current chemistry), and ft is the resulting stone (equal to it when vt =0).
The episode proceeds for a fixed trajectory length of T =5 steps. A random initial transition is sampled
from the environment’s transition table at the start of each episode and forms the first observation.
E.4.1 Bayesian Oracle World Model
Similar to Mastermind, the Bayesian oracle world model maintains the exact posterior over hidden
chemistries by enumerating all Nenvs candidate environments. Given a history of observations, the oracle
computes a consistency mask: a candidate chemistry θ is consistent at step t if, for all prior observations
(it′ ,pt′ ,vt′ ,ft′ ) with t′ <t:
1. If vt′ =1: chemistry θ contains a rule (it′ ,pt′ )7→ ft′ that produces the observed output stone, and
2. If vt′ =0: chemistry θ has no rule matching the input pair (it′ ,pt′ ).
The posterior probability of a new observation st =(vt,ft) is computed as:
ρ(st |ht =[ht−1,st−1,(it,pT )])=

{e∈Et :e is consistent with (it,pt,vt,ft)}
,
|Et|

(21)

where Et denotes the set of chemistries consistent with all observations prior to step t.
This world model provides exact Bayesian inference but scales linearly in the number of candidate
environments, which must be enumerated exhaustively.
E.4.2 In-Context PFN World Model
The world model is a 12-layer causal Transformer with model dimension d=512, 8 attention heads, and
feed-forward dimension 1024. Each observation ot =(it,pt,ft) is split into an input token (encoding it and
pt via concatenated one-hot vectors, projected to Rd) and an output token (encoding ft similarly). These
are interleaved into a sequence [in1,out1,in2,out2,...] of length 2T and processed with causal attention,
so that the hidden state at each input position int attends to all tokens up to and including outt−1.
The output prediction head is an autoregressive GRU decoder that, starting from the Transformer’s
hidden state at int, sequentially predicts each component of the observation output: first a validity flag
(2 categories), then each of the four stone dimensions (3, 3, 3, and 4 categories respectively). At each step
the GRU receives the embedding of the previous ground-truth component (teacher forcing during training),
31

updates its hidden state, and produces logits over the current component’s categories. Invalid logit positions
(where the category index exceeds the component’s vocabulary) are masked to −∞ before the softmax.
The model is trained on sequences of Ttrain=50 transitions sampled with uniformly random actions from
uniformly sampled environment IDs, with batch size B=64 and the Adam optimizer at learning rate 10−4.
Data-Generating Process The PFN is trained on synthetically generated transition trajectories. For each
training example, a chemistry (environment) is sampled uniformly at random, and then a sequence of Ttrain =
20 random transitions is generated. Each transition draws a random initial stone and potion uniformly from
their respective value ranges, and the corresponding observation (vt,stout) is computed by the environment.
Model Architecture The in-context world model is a causal Transformer decoder that processes
interleaved input (action) and output (observation) tokens. Each input token encodes the initial stone and
potion via per-dimension one-hot vectors. The stone dimensions (3,3,3,4) and potion dimension (6) are
each one-hot encoded and concatenated, yielding a vector of dimension of 19, which is projected to the
model dimension d via a linear layer. Each output token encodes the validity indicator vt and the final
stone. The validity is one-hot encoded into a vector of dimension 2, and is concatenated with the final
stone’s one-hot into a 15-dimensional vector, which is projected to d via a separate linear layer.
For a trajectory of T steps, the input sequence is constructed by interleaving input and output embeddings.
For each timestep t, the input embedding and output embedding are placed at positions 2t and 2t + 1,
resulting in a sequence of length 2T . The sequence is processed by a causal Transformer decoder with
model dimension d=512, MLP hidden dimension F =1024, N =12 layers, H =8 attention heads with
head dimension d/H =64.
Similar to Mastermind’s policy, the output prediction uses a GRU-based autoregressive decoder that conditions each output component’s prediction on the previously observed ground-truth components (teacher
forcing during training). The per-step loss is the sum of the per-component negative log-probabilities:
P5
(k) (1:k−1)
− k=1logp(ot |ot
,ht). The in-context world model is trained to minimize the cross-entropy loss
of predicting the output at each step. In each training step, a fresh batch of B =64 random trajectories is
generated on-the-fly (no fixed dataset), and the model is optimized using Adam with a learning rate of 10−4.
E.4.3 Policy
The policy is trained using PPO (Proximal Policy Optimization). At each training step, a batch of B =32
trajectories of length T = 5 is collected by rolling out the current policy in the environment. The PPO
objective uses K =4 update epochs per batch of collected data.
Model Architecture The policy is the same sequence model as used in Mastermind, with a Griffin
backbone model (De et al., 2024), and a GRU to predict the final output components autoregressively
conditioned on the Griffin’s output. The log-probability of the full action is the sum of the per-component
P5
(k)
(1:k−1)
log-probabilities: logπ(at |st)= k=1logπk (at |st,at
).

32
