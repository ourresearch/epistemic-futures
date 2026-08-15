---
title: "Embedded Universal Predictive Intelligence: a coherent framework for multi-agent learning"
person: blaise-aguera-y-arcas
section: by
type: journal-article
year: 2025
date: 2025-11-27
venue: "arXiv (Cornell University)"
authors: "Alexander Meulemans, Rajai Nasser, Maciej Wołczyk, Marissa A. Weis, Seijin Kobayashi, Blake A. Richards, Guillaume Lajoie, Angelika Steger, Marcus Hütter, James Manyika, Rif A. Saurous, João Sacramento et al."
source_url: https://arxiv.org/abs/2511.22226
retrieved: 2026-08-13
content: full-text
notes: "OpenAlex W4416943814 (type: preprint). Full text extracted from the open-access PDF at https://arxiv.org/pdf/2511.22226. Body truncated at 400KB cap; see source_url for the rest."
---

# Embedded Universal Predictive Intelligence: a coherent framework for multi-agent learning

## Full text

### Abstract (from OpenAlex metadata)

The standard theory of model-free reinforcement learning assumes that the environment dynamics are stationary and that agents are decoupled from their environment, such that policies are treated as being separate from the world they inhabit. This leads to theoretical challenges in the multi-agent setting where the non-stationarity induced by the learning of other agents demands prospective learning based on prediction models. To accurately model other agents, an agent must account for the fact that those other agents are, in turn, forming beliefs about it to predict its future behavior, motivating agents to model themselves as part of the environment. Here, building upon foundational work on universal artificial intelligence (AIXI), we introduce a mathematical framework for prospective learning and embedded agency centered on self-prediction, where Bayesian RL agents predict both future perceptual inputs and their own actions, and must therefore resolve epistemic uncertainty about themselves as part of the universe they inhabit. We show that in multi-agent settings, self-prediction enables agents to reason about others running similar algorithms, leading to new game-theoretic solution concepts and novel forms of cooperation unattainable by classical decoupled agents. Moreover, we extend the theory of AIXI, and study universally intelligent embedded agents which start from a Solomonoff prior. We show that these idealized agents can form consistent mutual predictions and achieve infinite-order theory of mind, potentially setting a gold standard for embedded multi-agent learning.

---

Embedded Universal Predictive Intelligence: a
coherent framework for multi-agent learning
Alexander Meulemans★,1 , Rajai Nasser★,1 , Maciej Wołczyk1 , Marissa A. Weis1 , Seijin Kobayashi1 , Blake
Richards1,2,4,5 , Guillaume Lajoie1,2,3,5 , Angelika Steger1,6 , Marcus Hutter7 , James Manyika1,8 , Rif A.
Saurous†,1 , João Sacramento†,1 and Blaise Agüera y Arcas†,1,9
1 Google, Paradigms of Intelligence Team, 2 Mila - Quebec AI Institute, 3 Université de Montréal, 4 McGill University, 5 CIFAR, 6 ETH

arXiv:2511.22226v3 [cs.AI] 4 Aug 2026

Zürich, 7 Google DeepMind, 8 Google, 9 Santa Fe Institute, ★Equal contribution, † Equal supervision

The standard theory of model-free reinforcement learning assumes that the environment dynamics are
stationary and that agents are decoupled from their environment, such that policies are treated as being
separate from the world they inhabit. This leads to theoretical challenges in the multi-agent setting
where the non-stationarity induced by the learning of other agents demands prospective learning based
on prediction models. To accurately model other agents, an agent must account for the fact that those
other agents are, in turn, forming beliefs about it to predict its future behavior, motivating agents to
model themselves as part of the environment. Here, building upon foundational work on universal
artificial intelligence (AIXI), we introduce a mathematical framework for prospective learning and
embedded agency centered on self-prediction, where Bayesian RL agents predict both future perceptual
inputs and their own actions, and must therefore resolve epistemic uncertainty about themselves as
part of the universe they inhabit. We show that in multi-agent settings, self-prediction enables agents
to reason about others running similar algorithms, leading to new game-theoretic solution concepts
and novel forms of cooperation unattainable by classical decoupled agents. Moreover, we extend the
theory of AIXI, and study universally intelligent embedded agents which start from a Solomonoff prior.
We show that these idealized agents can form consistent mutual predictions and achieve infinite-order
theory of mind, potentially setting a gold standard for embedded multi-agent learning.

Contents
1 Introduction

2

2 Background

8

3 Embedded Bayesian agents

16

4 Equilibrium behavior of embedded Bayesian agents

28

5 Embedded Universal Predictive Intelligence

48

6 Discussion

69

A Table of notations and definitions

83

B Preliminaries

85

C Proofs

100

D Embedded Bayesian agents and related solution concepts: additional information

167

E Functional similarities through the lens of algorithmic information: additional information

177

F Multi-agent environments and their relation to universes

196

G A few desiderata for a Bayesian theory of embedded universal intelligence

198

1. Introduction
A major frontier in artificial intelligence involves moving beyond the imitation of human data,
leveraging reinforcement learning (RL) to enable agents to self-generate experience and continually
improve (Guo et al., 2025; Ouyang et al., 2022; Silver et al., 2017; Team Gemini et al., 2023). This
paradigm, combining large-scale pretraining with single-agent RL, has proven remarkably effective
for enhancing individual capabilities, leading to significant gains in complex reasoning tasks such as
mathematics and programming (Guo et al., 2025; Ouyang et al., 2022; Uesato et al., 2022). However,
these individual competencies represent only one facet of intelligence. To endow AI agents with
meaningful social capabilities beyond those observed from human behavioral data, training must
move into multi-agent environments, as sociality is an inherently multi-agent property (Dafoe et al.,
2021). Developing such capabilities is crucial for enabling agents to function as effective and reliable
entities within human society, allowing them to navigate complex social dynamics, coordinate with
humans and other AI agents, or even represent human stakeholders in negotiations. To date, the
most impressive results in multi-agent RL (MARL) have been confined to specialized cases, such
as zero-sum, purely competitive games (Silver et al., 2017; Vinyals et al., 2019) or tasks of pure
cooperation. Robust learning in the more general and human-relevant mixed-motive settings, which
form the core of sociality (Dafoe et al., 2021), remains an unsolved challenge. These scenarios, which
mirror high-stakes societal challenges such as economic and climate change negotiations, demand a
sophisticated blend of cooperation and competition, grappling with emergent social phenomena like
trust, fairness, reputation, and deception.
Current model-free RL approaches are insufficient to tackle learning in multi-agent with mixed-motive
settings. The first fundamental problem with standard model-free RL is its retrospective nature: An
agent attempts to improve its policy to perform well on data from the past. This form of learning has
its roots in 19th and 20th century empirical observations on how animals respond to reward and
punishment (Skinner, 1948; Thorndike, 1898), and accompanying theories such as Thorndike’s law
of effect, which can be loosely understood as “do more of what worked well in the past, and less
of what did not” (Thorndike, 1898). Such retrospective learning works well when the environment
is stationary, but multi-agent systems are intrinsically nonstationary. From the perspective of an
individual agent, the environment changes during the learning process, as it contains other agents
that are themselves learning. Applying model-free RL algorithms in a multi-agent setting thus relies on
an invalid stationarity assumption, which in practice leads to suboptimal behavior, especially in mixedmotive scenarios and social dilemmas (Foerster et al., 2018; Huh and Mohapatra, 2023; Sandholm
and Crites, 1996). Therefore, multi-agent systems require prospective learning instead: Agents should
update their policies based on a predicted future rather than an outdated past. Prospective learning
fundamentally relies on prediction models to anticipate a changing future. However, the current main
paradigm for LLM agents, which combines a pretrained predictive model such as an autoregressive
transformer with model-free RL during post-training, typically treats the predictive model as a mere
initialization for the policy (Guo et al., 2025; OpenAI et al., 2023; Team Gemini et al., 2023). Hence,
during post-training, the sequence model is trained with (retrospective) model-free RL, in contrast to
using the prediction model to predict a changing future and using that predicted future for prospective
learning.

2

Figure 1.1 | Illustration of embedded Bayesian agents. Top: In standard, decoupled approaches to Bayesian
agents for RL, an agent considers their own policy as separate from the world they and others are making
predictions about, maintaining beliefs about environments that might contain other agents, but not the egoagent itself. Bottom: Embedded Bayesian agents, consider themselves to be embedded within a universe, the
combination of the ego-agents policy with the environment which can contain other agents. As such, when
making predictions they are not only predicting the environment percepts but also their own actions, allowing
them to leverage functional similarities into their predictions and resulting behavior. This allows embedded
Bayesian agents to converge to different equilibrium points in multi-agent settings.

Recent multi-agent RL work on co-player learning awareness (Aghajohari et al., 2024; Duque et al.,
2024; Foerster et al., 2018; Khan et al., 2024; Lu et al., 2022; Meulemans et al., 2024) can be
thought of as trying to derive a prospective policy gradient, which estimates the influence of an agent’s
actions on the learning of other agents. However, in deriving a policy gradient, these algorithms often
implicitly assume that other agents are not themselves co-player learning aware. This flaw points to
the more general challenge of dealing with infinite theory of mind recursions of the form “I predict
your behavior, while taking into account that you are predicting my behavior, which is predicting your
behavior, which is....” Such infinite recursions in theory of mind make consistent mutual prediction a
central problem in prospective multi-agent learning, and tackling this problem is a main focus of the
present paper.
The challenges of mutual prediction and recursive theory of mind highlight a second problem with
the standard model-free RL framework: it is built upon the conceptual paradigm of decoupled agency.
Decoupled agents do not consider their policies as part of the environment but rather as a distinct,
external construct. However, agents are real entities in the environment they inhabit, and to accurately
model other agents, an agent should account for the fact that those other agents are, in turn, forming
beliefs about it to predict its future behavior. This motivates a conceptual shift towards embedded
agency (Demski and Garrabrant, 2019), where each agent models itself as part of the environment it
inhabits, enabling it to anticipate the beliefs others might form about it. As we will show in this work,
formally adopting this embedded viewpoint—considering oneself as part of the environment—is not
only a conceptual correction but also a practical one, unlocking new avenues towards cooperation
and coordination among agents through the consistent mutual prediction of oneself and others.
3

The present paper provides a mathematical framework that combines prospective learning with
embedded agency, where agents base their decisions on predictions of both the environment and
the agent’s own behavior (Fig. 1.1). Consequently, whereas classical model-based RL is centered on
predicting how the external environment responds to a certain action, the agents that we consider here
predict both future perceptual inputs as well as their own actions, a process that we call self-prediction.
Joint percept-action prediction lifts the barrier between external environment and self, and it is the
key step we take towards embeddedness.
To formalize prospective learning and embededness, we build upon Bayesian sequence prediction and
universal artificial intelligence (Hutter, 2005, AIXI), and adapt this theory—which treats decoupled
agency— towards a theory of embedded agency. The AIXI framework formalizes prospective learning
through Bayesian sequence prediction, and our embedded agency framework inherits this capability.
We introduce embedded Bayesian agents, which maintain and sequentially update probabilistic beliefs
as they gather knowledge about which universe they live in. In critical opposition to standard RL,
universes contain the agent itself, and jointly describe the (possibly stochastic) laws of evolution of
the agent—including its learning dynamics—together with its surrounding environment, possibly
including other agents and their learning dynamics. Embedded Bayesian agents must thus resolve
epistemic uncertainty not only about the environment but also about themselves. When the agent’s
hypothesis class over possible universes contains the ground-truth universe describing the joint
dynamics of the agent and environment, a condition commonly called a grain of truth (Kalai and
Lehrer, 1993a), the resulting Bayesian predictions are guaranteed to converge to the ground-truth
distribution. This convergence holds even in the presence of non-stationarities where the future differs
from the past, sidestepping the need to make simplifying Markov, i.i.d., ergodicity, or stationarity
assumptions often invoked in standard RL (Blackwell and Dubins, 1962; Hutter, 2003; Hutter et al.,
2024). Embedded Bayesian agents then combine these prospective Bayesian predictions with optimal
planning or policy distillation to learn their behavioral policies, resulting in prospective learning based
on prospective Bayesian predictions. When the grain-of-truth property holds, embedded Bayesian
agents make consistent mutual prediction and hence achieve recursive theory of mind. This makes the
satisfaction of the grain-of-truth property a central and non-trivial challenge in designing embedded
Bayesian agents and a core focus of this work. Our manuscript is split into two main parts. In Sections
3 and 4, we describe embedded Bayesian agents and their resulting behavior, assuming they satisfy
the grain-of-truth property. Then, in Section 5, we explicitly design embedded Bayesian agents
that satisfy the grain-of-truth property while maintaining a wide hypothesis class that includes all
computable universes.
This embedded, joint-modeling approach leads to a crucial departure from the standard, decoupled
paradigm: The agent’s beliefs about itself and the environment become coupled. Information about
the agent’s own actions can now provide evidence about the environment (including other agents),
and vice-versa. This coupling is not a mere theoretical artifact but a principled reflection of functional
similarities among agents that arise naturally in the world. Such similarities occur for example
through the following pathways: (i) agents can have a shared creation process, such as multiple AIs
being instantiations of the same base model or organisms sharing genes; or (ii) agents can develop
convergent solutions to a similar task, independently arriving at analogous strategies. Embedded
Bayesian agents are uniquely positioned to leverage this insight in their predictions and resulting
decisions, reasoning that ‘similar agents behave similarly in similar situations’.
This similarity-aware reasoning has important consequences for both prediction and behavior. For
prediction, it allows an agent to leverage its own self-model to form more accurate predictions of
others, a form of theory-of-mind central to human social cognition (Graziano, 2013). For behavior, it
redefines what constitutes rational choice when taking embeddedness and functional similarities into
account. It leads agents to reason in accordance with Evidential Decision Theory (EDT) (Ahmed, 2021;
4

Everitt et al., 2015; Jeffrey, 1990), in contrast to the more orthodox Causal Decision Theory (CDT)
(Gibbard and Harper, 1978; Lewis, 1981). In EDT, an agent selects the action that would be the best
news to learn one has performed (Ahmed, 2014, 2021). This allows our embedded agents to treat
their own deliberations as evidence on the behavior of other agents which are perceived to perform
similar deliberations. For instance, making a choice to cooperate provides evidence that similar agents
might make the same choice in a similar situation. CDT, by contrast, evaluates actions based on their
expected causal consequences, assuming the agent’s choice is an independent intervention on the world
(Everitt et al., 2015; Lewis, 1981). This causal stance explicitly ignores the evidential link provided
by functional similarities. The behavioral divergence is stark. Consider the Twin Prisoner’s Dilemma,
where two identical copies of an AI agent play the prisoner’s dilemma against each other. Classical
game theory—built on a decoupled agency and CDT foundation with the Nash equilibrium as its
solution concept—mandates defection as the only rational choice (Lewis, 1979). An embedded agent
reasoning evidentially, however, recognizes the perfect functional similarity. It correctly anticipates
that its copy will make the same decision, making its own choice to cooperate a justifiably rational
action, as mutual cooperation yields a higher personal reward than mutual defection.
To formalize this embedded notion of rationality in multi-agent scenarios, we introduce a novel family
of game-theoretic solution concepts: the embedded equilibria. These equilibria, inspired by the work
of Spohn (2003) on dependency equilibria and Kalai and Lehrer (1993a,b) on subjective equilibria,
explicitly account for the coupled beliefs that arise from functional similarities. This opens new
pathways for cooperation and coordination that are inaccessible to decoupled agents and classical
game theory. The subjective embedded equilibrium (SEE) describes a state where each agent’s policy
is a best response with respect to its own subjective beliefs about the universe, including its beliefs
about itself and its correlation with others. The embedded equilibrium (EE), our proposed embedded
counterpart to the Nash equilibrium, describes an optimal and stable pattern of behavior when the true
functional similarities between agents are taken into account. A key result of our work is proving that
embedded Bayesian agents, when satisfying the grain-of-truth property, are guaranteed to converge
to playing 𝜖-subjective embedded equilibria in multi-agent interactions.
We note that our contributions build on a strong line of works that leverage similarity between
agents to achieve cooperation, and investigate the consequences of evidential reasoning in multi-agent
scenarios. Much prior effort has explored the concept of similarity between agents, often by assuming
agents are fully transparent—that is, they have access to the source code or decision algorithm of their
co-players (Barasz et al., 2014; Brams, 1975; Critch, 2019; Halpern and Pass, 2018; Hofstadter, 1983;
Howard, 1988; Lewis, 1979; Oesterheld, 2019; Tennenholtz, 2004). More recent work has generalized
this by providing agents with a scalar similarity score (Oesterheld et al., 2024) or using Bayesian
theory of mind to infer if others share a similar utility function (Kleiman-Weiner et al., 2025). Our
framework further generalizes these approaches. It shows how a joint predictive model of oneself and
the environment can account for functional similarities without requiring full transparency, explicit
access to code, or collapsing the rich nature of similarity into a single score or utility function. It is
well-established that EDT can lead to cooperation in the Twin Prisoner’s Dilemma (Ahmed, 2021). In
game theory, Al-Nowaihi and Dhami (2015) introduced evidential equilibria to describe game-theoretic
equilibria between agents applying evidential decision theory, as a more accurate descriptive theory
of human decision making. Spohn (2003) argues that his closely related dependency equilibria are not
only more descriptive of human behavior, but are also normatively rational, motivating them with
a reflexive decision theory that allows for causal links between agents’ decision processes. Ahmed
(2014, 2021) further defend EDT as a normative theory for rational behavior, constructing thought
experiments where CDT, unlike EDT, leads to dynamically inconsistent choices. By introducing
embedded Bayesian agents and formalizing functional similarities via Shannon and algorithmic
information theoretic concepts, we further motivate that EDT-like reasoning by leveraging functional

5

similarities is normatively rational for embedded agency. We introduce novel solution concepts
(EEs) incorporating these functional similarities, and show that ‘embedded rational learners’—our
embedded Bayesian agents—are guaranteed to converge to the subjective variant (SEEs) of these
equilibria.
The main remaining question is which hypothesis class and corresponding prior to use such that
the resulting embedded Bayesian agents satisfy the grain-of-truth property, and thereby exhibit the
behaviors described in the previous paragraphs. Satisfying the grain-of-truth property for non-trivial
model classes is a challenging task (Foster and Young, 2001; Leike et al., 2016b; Nachbar, 1997,
2005). As a step towards defining and understanding what the ideal, ultimate embedded intelligent
agent might be, we then introduce the EMbedded Universal Predictive Intelligence (MUPI) framework,
extending the seminal theoretical work on AIXI by Hutter (2000). Such a universal embedded agent
starts with a Bayesian prior over a wide hypothesis class including all computable universes, favoring
simple over complex universes by assigning higher prior probability mass to the former, thus abiding to
Occam’s razor. Building upon recent variants of AIXI that (i) incorporate self-prediction in the singleagent, decoupled setting (Catt et al., 2023), and (ii), leverage a landmark mathematical construction
of reflective oracles (Fallenstein et al., 2015b) to widen the hypothesis class over environments to
include environments containing other AIXI agents (Fallenstein et al., 2015a; Leike et al., 2016b;
Wyeth et al., 2025), we show that our embedded universal agents satisfy the grain-of-truth property
and hence are consistent under mutual prediction, and therefore possess infinite-order theory of
mind. We further formalize functional similarities from an algorithmic information theory perspective,
where functional similarities between agents correspond to how well the agent’s programs can be
jointly compressed. As universes containing similar agents have shorter description lengths compared
to universes containing dissimilar agents, the Occam’s razor prior naturally favors such universes.
This demonstrates that the functional-similarity-based reasoning of embedded Bayesian agents is not
an ad-hoc assumption, but rather a core principle of reasoning about the world using Occam’s razor.
Finally, at the end of the paper, we return to real-world artificial intelligence, and discuss the practical
implications of our theory on current AI systems based on foundation models jointly predicting actions
and percepts.

6

Box 1.2: Summary of core contributions
1. We formalize embedded Bayesian agents as a conceptual framework to address two
main challenges in multi-agent learning: prospective learning and embedded agency.
(i) Agents incorporate prospective learning by using Bayesian sequence prediction to
forecast future consequences, critically sidestepping the limiting assumptions of
stationarity, ergodicity or Markov dynamics.
(ii) They embody embeddedness by forming beliefs over universes that contain both
themselves and the environment. This results in a unified Bayesian prediction model
for both external percepts and the agent’s own actions. This joint prediction makes
embedded Bayesian agents an appealing theoretical model organism for current
practical AI agents based on foundation models which are also joint action-percept
prediction models.
2. We formalize functional similarities between agents as the property that their policies
contain mutual Shannon or algorithmic information.
(i) Embedded Bayesian agents leverage this by reasoning that "similar agents behave
similarly in similar situations," leading on average to more accurate predictions than
their decoupled counterparts when such similarities are present.
(ii) We show that reasoning about functional similarities is not an ad-hoc assumption
but a fundamental consequence of applying Occam’s razor in a universal prediction
setting: We prove that a universal belief distribution based on a Solomonoff prior—an
Occam’s razor prior which assigns higher probability to simpler (more compressible)
universes— always results in a positive mutual information between the agent’s policy and the environment (possibly containing other agents), as universes containing
similar agents are algorithmically simpler to describe.
3. We introduce new game-theoretic solution concepts, the subjective embedded equilibrium
(SEE) and embedded equilibrium (EE).
(i) These concepts redefine rationality for embedded agents in game-theoretic settings, accounting for functional similarities to enable new forms of cooperation and
coordination that are unattainable by classical Nash equilibria.
(ii) We prove that embedded Bayesian agents satisfying the grain-of-truth property
converge to playing 𝜖-SEEs, and converge towards EEs when additional conditions
are satisfied.
4. To solve the grain-of-truth problem for embedded agency (a key condition for the convergence results above), we introduce the EMbedded Universal Predictive Intelligence
(MUPI) framework.
(i) We develop the Reflective Universal Inductor (RUI): a universal prediction model that
can consistently reason about universes containing agents that use the RUI itself as
prediction model, thereby resolving the infinite recursions of mutual prediction.
(ii) We prove the existence of the RUI, providing a new tool for building universally
intelligent agents that stands as an alternative to the reflective oracle framework
(Fallenstein et al., 2015b).

7

2. Background
2.1. Mathematical Preliminaries
2.1.1. Sequences
Let X be an arbitrary countable set. For a fixed integer 𝑛, X 𝑛 is the set of sequences of length 𝑛 whose
elements are in X, also known as X-sequences of length 𝑛. We adopt the convention that X 0 = {𝜀}
where 𝜀 is the empty sequence/string, in contrast to 𝜖 which we use as notation for a small scalar
value. We write X ∗ to denote the set of finite X-sequences, i.e.,
Ø
X ∗ :=
X𝑛 .
𝑛 ≥0

We write1 X ∞ := X ℕ to denote the set of infinite X-sequences, and X # := X ∗ ∪ X ∞ to denote the set
of all (finite and infinite) sequences. For 𝑥, 𝑦 ∈ X # , we write 𝑥 ⊑ 𝑦 to denote that 𝑥 is a prefix of 𝑦 .
For 𝑥 ∈ X ∗ and 𝑦 ∈ X # , we write 𝑥 𝑦 to denote the sequence obtained by concatenating 𝑥 and 𝑦 .
For any sequence 𝑥 ∈ X # , we denote the (possibly infinite) length of 𝑥 as 𝑙 ( 𝑥 ), and for every 1 ≤ 𝑖 ≤ 𝑙 ( 𝑥 ),
we denote the 𝑖-th symbol of 𝑥 as 𝑥 𝑖 . For 1 ≤ 𝑖 ≤ 𝑗 ≤ 𝑙 ( 𝑥 ) we write 𝑥 𝑖: 𝑗 to denote the subsequence
( 𝑥 𝑖 , . . . , 𝑥 𝑗 ). We also use the notation 𝑥 <𝑡 as a shorthand for 𝑥1:𝑡 −1 and 𝑥 ≤ 𝑡 for 𝑥1:𝑡 .
2.1.2. Probability Background
We use the following definitions of measures and semimeasures:2
Definition 2.1 (Semimeasures and measures). Let the cylinder set Γℎ be the set of all sequences
𝑦 ∈ X # that start with finite sequence ℎ ∈ X ∗ . Using the abuse of notation 𝜎 ( ℎ) := 𝜎 ( Γℎ ), a semimeasure
𝜎 : X ∗ → [0, 1] on the sample space X # satisfies the following conditions:
∑︁
𝜎 ( 𝜀) ≤ 1
and
𝜎 ( ℎ) ≥
𝜎 ( ℎ𝑥 ) ,
(1)
𝑥∈X

A measure is a semimeasure where both the above inequalities are tight. Intuitively, 𝜎 ( ℎ) represents the
Í
probability that a sampled sequence starts with prefix ℎ. When a strict inequality 𝜎 ( ℎ) > 𝑥 ∈ X 𝜎 ( ℎ𝑥 )
applies, there is a non-zero probability that the sequence ends after ℎ.3 Conditional (semi-)measures
are defined by
𝜎 ( 𝑧 | ℎ) :=

𝜎 ( ℎ𝑧 )
.
𝜎 ( ℎ)

(2)

The conditional measure 𝜎 ( 𝑧 | ℎ) is undefined when 𝜎 ( ℎ) = 0
We refer to measures and distributions interchangeably. For any given set X, the notation ΔX
represents the set of all probability distributions over the elements of X, and Δ′ X the set of all
1 Note that 𝐴 𝐵 denotes the set of mappings from 𝐵 to 𝐴. Therefore, X ℕ is the set of infinite sequences in X with indices
in ℕ.
2 Semimeasures are important in algorithmic probability which we will leverage later in this manuscript, where sequences
are generated by Turing machines, which can halt or loop forever without outputting further symbols, and hence can
output both finite sequences and infinite sequences (cf. Appendix B for an in-depth discussion on semimeasures and their
properties).
3 In order to interpret the semimeasure 𝜎 ( ℎ) as the probability that a sequence 𝑥 ∈ X # (which can be finite or infinite)
starts with ℎ, we require that 𝜎 ( 𝜀) = 1, which can be achieved by renormalizing the semimeasure by 𝜎 ( 𝜀) whenever it is
different from zero.

8

semiprobability distributions over X, i.e., functions 𝜎 that satisfy
𝑥 ∈ X.

Í

𝑥 ∈ X 𝜎 ( 𝑥 ) ≤ 1 and 𝜎 ( 𝑥 ) ≥ 0 for all

We introduce a distance metric between measures over sequences:4
Definition 2.2 (Total variation distance). Let 𝑃 1 and 𝑃 2 be two measures over sequences. For every
𝑘 ≥ 1, we define the 𝑘-step total variation distance between 𝑃 1 and 𝑃 2 conditioned on history ℎ as:
𝐷𝑘 ( 𝑃 1 , 𝑃 2 | ℎ) =

1 ∑︁ 1 ′
| 𝑃 ( ℎ | ℎ) − 𝑃 2 ( ℎ′ | ℎ)| .
2 ′ 𝑘
ℎ ∈X

It is easy to show that 𝐷𝑘+1 ( 𝑃 1 , 𝑃 2 | ℎ) ≥ 𝐷𝑘 ( 𝑃 1 , 𝑃 2 | ℎ). By taking 𝑘 → ∞, we get the total variation
distance:
1 ∑︁ 1 ′
𝐷∞ ( 𝑃 1 , 𝑃 2 | ℎ) = sup
| 𝑃 ( ℎ | ℎ) − 𝑃 2 ( ℎ′ | ℎ)| .
𝑘 ≥1 2 ′
𝑘
ℎ ∈X

We define a notion of dominance, which is a stronger form of the more familiar absolute continuity.
Definition 2.3 (Dominance). Given two measures 𝑃 1 and 𝑃 2 over X # , we say that a measure 𝑃 1
×

dominates a measure 𝑃 2 , and write 𝑃 1 ≥ 𝑃 2 , if there exists 𝐶 > 0 such that 𝑃 1 ( 𝑥 ) ≥ 𝐶 · 𝑃 2 ( 𝑥 ) for all
𝑥 ∈ X∗.
Note that 𝐶 cannot depend on 𝑥 in the above definition.
2.2. General Reinforcement Learning Setup
We briefly review the general reinforcement learning setting (Hutter et al., 2024) that we build
upon. In this setting, the reward and environment transition functions depend on the full history of
interactions up to the present time, thus subsuming the Markov decision process (MDP) framework
that underpins classical optimal control and reinforcement learning as a special case. We then define
the Bayes-optimal agent, which maximizes expected return while weighing a set of environments an
agent might find itself in against the evidence contained in the history of interactions so far. These
concepts serve as the foundation for the embedded Bayesian agents that we study.
General reinforcement learning. Consider a finite set of possible actions, A, a finite set of possible
observations, O, and a finite set of possible rewards, R ⊂ [0, 1]. We define the set of percepts as the
Cartesian product of observations and rewards, E := O × R.
A history consists of a finite sequence of alternating actions and percepts. Abusing notation slightly, we
denote a single turn in a history (an agent taking an action and observing a percept) as æ ∈ AE := A×E,
a 𝑡 -turn history as æ1:𝑡 ∈ AE 𝑡 and an arbitrary-length history as ℎ ∈ AE ∗ . Again abusing notation
slightly, we write 𝑙 ( ℎ) to denote the number of turns in ℎ, i.e., 𝑙 ( ℎ) = 𝑡 when ℎ ∈ AE 𝑡 .
An agent’s policy 𝜋 maps a given history to a distribution over actions: 𝜋 : AE ∗ → Δ A. We write
𝜋 ( 𝑎 |æ1:𝑡 ) := 𝜋 (æ1:𝑡 ) ( 𝑎) to denote the conditional probability that the agent takes an action 𝑎 given a
history æ1:𝑡 . The environment dynamics 𝜈 maps a history and an action to a distribution over subsequent
percepts: 𝜈 : AE ∗ ×A → Δ E. We write 𝜈 ( 𝑒 |æ1:𝑡 , 𝑎) := 𝜈 (æ1:𝑡 , 𝑎) ( 𝑒) to denote the conditional probability
that the environment produces the percept 𝑒 given that the agent took action 𝑎 after history æ1:𝑡 .
When a policy 𝜋 is interacting with an environment 𝜈, it induces a measure 𝜈𝜋 on the space of infinite
histories.
4 See Appendix B for a more general definition of total variation applicable to semimeasures as well.

9

The goal of general reinforcement learning is to obtain an optimal policy 𝜋 that maximizes the
expected discounted sum of rewards. The value function for a given environment 𝜈, discount factor
𝛾 ∈ [0, 1) and policy 𝜋 starting from history æ1:𝑡 is defined as
"∞
#
∑︁
𝑘−𝑡
𝑉𝜈𝜋 (æ<𝑡 ) := (1 − 𝛾 )𝔼𝜈𝜋
𝛾 𝑟𝑘 æ<𝑡 ,
(3)
𝑘=𝑡

where we multiply by (1 − 𝛾 ) to ensure that values are bounded between 0 and 1. The set of
optimal policies is equal to arg max𝜋 𝑉𝜈𝜋 (æ<𝑡 ) and the associated optimal value function is defined
as 𝑉𝜈∗ (æ<𝑡 ) := max𝜋 𝑉𝜈𝜋 (æ<𝑡 ). We denote an individual optimal policy with 𝜋 ∈ arg max𝜋 𝑉𝜈𝜋 (æ<𝑡 ). To
facilitate analysis, we also define the action-value function, or Q-value, as
𝑄 𝜈𝜋 (æ<𝑡 , 𝑎𝑡 ) := 𝔼𝜈 ( 𝑒𝑡 |æ<𝑡 ,𝑎𝑡 ) [(1 − 𝛾 ) 𝑟𝑡 + 𝛾𝑉𝜈𝜋 (æ<𝑡 æ𝑡 )] .

Multi-agent general reinforcement learning (MAGRL). We can straightforwardly generalize
general reinforcement learning to a multi-agent setup as follows. Consider N agents 𝑖 ∈ 𝑁 with finite
Î
Î
action spaces A 𝑖 . We denote the joint action as 𝑎¯ ∈ Ā := 𝑖 A 𝑖 , and the joint percept as 𝑒¯ ∈ Ē := 𝑖 E 𝑖 .
∗
We define the space of multi-agent turns AE := ( Ā × Ē), the space of multi-agent histories AE (a
𝑡
𝑡 -turn history is æ1:𝑡 ∈ AE ), and the space of extracted single-agent histories (AE 𝑖 ) ∗ := (A 𝑖 × E 𝑖 ) ∗ .
Each agent has a policy 𝜋𝑖 : (AE 𝑖 ) ∗ → Δ A 𝑖 , which chooses an action given agent 𝑖’s history. The
∗
multi-agent environment 𝜈 : AE × Ā → Δ Ē defines the joint distribution over percepts for each
agent, conditioned on the joint history. We denote 𝜈𝜋 as the joint distribution induced by 𝜈 and agent
policies 𝜋 = ( 𝜋𝑖 ) 𝑖𝑁=1 . Note that all agents act simultaneously without observing the current action of
the other agents, and their next percept 𝑒𝑖 can contain information about the actions taken by other
agents.
Combining the multi-agent environment 𝜈 with the policies ( 𝜋 𝑗 ) 𝑗≠𝑖 of the other agents, and marginal𝑖
izing out their histories and percepts leads to a personal environment 𝜈𝑖 ( 𝑒𝑖 | æ1:
, 𝑎𝑖 ) for each agent,
𝑡
which depends on the policies of the other agents. Combining the personal environment 𝜈𝑖 with the
𝑖
personal policy 𝜋𝑖 leads to a distribution over personal histories ( 𝜈𝑖 ) 𝜋 .
When we omit superscript 𝑖 with actions 𝑎 and percepts 𝑒, we indicate a single agent’s actions and
percepts originating from its personal environment.
2.3. Bayesian prediction and agents
When an agent is uncertain about which environment it is interacting with, it needs to (i) learn about
its environment from past observations and actions, and (ii) behave optimally taking into account
its uncertainty on which environment it is interacting with. Bayesian agents formalize these notions
of rational agency by (i) using Bayesian mixture environments to quantify their beliefs about which
environment they are interacting with and making posterior belief updates leveraging incoming
observations, and (ii) using optimal planning within the Bayesian mixture environment to obtain a
behavioral policy.
Bayesian mixture environment. Using a countable hypothesis space Menv over environments 𝜈,
we can define the Bayesian mixture environment as
∑︁
𝜈 ( 𝑒𝑡 | æ<𝑡 , 𝑎𝑡 )
𝜉 ( 𝑒𝑡 | æ<𝑡 , 𝑎𝑡 ) :=
𝑤 ( 𝜈 | æ<𝑡 ) 𝜈 ( 𝑒𝑡 | æ<𝑡 , 𝑎𝑡 ) ,
𝑤 ( 𝜈 | æ1:𝑡 ) := 𝑤 ( 𝜈 | æ<𝑡 )
,
(4)
𝜉 ( 𝑒𝑡 | æ<𝑡 , 𝑎𝑡 )
𝜈 ∈ Menv

with 𝑤 ( 𝜈) := 𝑤 ( 𝜈 | 𝜀) the prior belief distribution and 𝜀 the empty history. We assume throughout
Í
that 𝑤 ( 𝜈) > 0 ∀𝜈 ∈ Menv , and that 𝜈 ∈ Menv 𝑤 ( 𝜈) = 1.
10

Decoupled Bayes-optimal agent. Bayes-optimal agents act optimally w.r.t. their beliefs over
environments. Hence, starting from a specific history æ<𝑡 , they select an optimal policy w.r.t. their
Bayesian mixture environment 𝜉 through optimal planning. We call such Bayes-optimal agents
decoupled Bayes-optimal agents (to contrast them with embedded Bayes-optimal agents which we will
introduce in Section 3), and call their optimal policy a decoupled Bayes-optimal response (DBR):
𝜋 𝐷𝐵𝑅 ∈ arg max 𝑉𝜉𝜋 (æ<𝑡 ) .

(5)

𝜋

When a Bayesian mixture environment-policy measure 𝜉𝜋 includes (puts positive weight on) a "true"
environment-policy measure 𝜇 𝜋 , we say that 𝜉𝜋 satisfies the grain-of-truth property (Kalai and Lehrer,
1993a) with respect to 𝜇 𝜋 ; when it is clear from context, we will refer to "having grain of truth"
without mentioning the specific ground-truth and mixture distributions. Because 𝜇 𝜋 has positive
×

weight in 𝜉𝜋 , it is obvious that 𝜉𝜋 ≥ 𝜇 𝜋 . The classic theorem below shows that this is sufficient to
guarantee that 𝜉𝜋 converges almost-surely to 𝜇 𝜋 .5
Theorem 2.4 (Convergence of 𝜉 to 𝜇 in total variation (Blackwell and Dubins, 1962; Hutter et al.,
2024)). For any policy 𝜋, consider a ground-truth environment-policy measure 𝜇 𝜋 and a Bayesian
×

mixture environment-policy measure 𝜉𝜋 . If 𝜉𝜋 ≥ 𝜇 𝜋 ,
𝐷∞ ( 𝜉𝜋 , 𝜇 𝜋 | æ1:𝑡 ) → 0 as 𝑡 → ∞ 𝜇 𝜋 -almost-surely .6

The above theorem has important implications in multi-agent settings: Assume that 𝑁 agents are
interacting through a multi-agent environment 𝜇 . Each agent can be uncertain about the policies of
the other agents, and they may also be uncertain about the statistics of the ground-truth multi-agent
environment 𝜇 . We can model these uncertainties through a Bayesian approach by assuming that each
agent has a prior probabilistic belief about the multi-agent environment7 𝜇 , and prior probabilistic
beliefs about the policies of the other agents. Since specifying the policies of other agents reduces
a multi-agent environment to a personal single-agent environment, we may assume without loss
of generality that each agent has a prior probabilistic belief over the possible personal single-agent
environment it is interacting with. Let 𝜉𝑖 be the Bayesian mixture (personal) environment of the 𝑖-th
agent according to its prior, and assume that each agent performs optimal planning with respect to its
(subjective) mixture personal environment. Let 𝜋𝑖 be the Bayes-optimal policy of the 𝑖-th agent, and
let 𝜇 𝑖 be the ground-truth personal environment from the perspective of the 𝑖-th agent, which is the
result of combining the ground-truth multi-agent environment 𝜇 and the policies ( 𝜋 𝑗 ) 𝑗≠𝑖 of the other
agents. Theorem 2.4 implies that when Bayes-optimal agents satisfy the grain-of-truth property (i.e.,
×

( 𝜉𝑖 ) 𝜋 ≥ ( 𝜇 𝑖 ) 𝜋 , ∀𝑖 ∈ {1, . . . , 𝑁 }), they converge towards accurate and consistent mutual prediction.
𝑖

𝑖

The seminal work of Kalai and Lehrer (1993a,b) uses this convergence property to show that in
a multi-agent setting, Bayes-optimal agents that satisfy the grain-of-truth property converge to an
𝜖-Nash equilibrium when interacting with each other on repeated games. These powerful results
hinge upon the grain-of-truth assumption, which is notoriously hard to satisfy when using large
hypothesis classes (Foster and Young, 2001; Leike et al., 2016b; Nachbar, 1997, 2005; Shoham and
Leyton-Brown, 2008).
To build intuition for this difficulty, consider a two-player game where the environment dynamics 𝜇
are known to both players. Each agent 𝑖 ∈ {1, 2} is uncertain about the policy of the other agent 𝑗
5 Note that this theorem can be generalized to semimeasures (cf. Appendix B), and the dominance condition can be
further relaxed to requiring that 𝜇 𝜋 is absolutely continuous w.r.t. 𝜉𝜋 .
6 It is worth noting the generalized Solomonoff bounds of, e.g., (Hutter et al., 2024, Theorems 3.2.5 and 3.3.4) imply
that the convergence is very fast.
7 If 𝜇 is known, then the prior probability distribution would be concentrated on it.

11

(where 𝑗 = 2 if 𝑖 = 1 and vice versa), and so agent 𝑖 starts with a hypothesis class of possible policies,
𝑗
Mpol
, that the other agent 𝑗 might be using. By combining its Bayesian beliefs about the opponent’s

policy with the known game dynamics, each agent 𝑖 induces a personal mixture environment 𝜉𝑖 .
Assume both agents are Bayes-optimal, computing policies 𝜋1 and 𝜋2 with respect to their personal
mixture environments. A sufficient condition for the grain-of-truth property to hold is that each agent’s
2 and 𝜋1 ∈ M 1 . However, there
hypothesis class contains the other agent’s true policy,8 i.e., 𝜋2 ∈ Mpol
pol
is no a priori guarantee that this will be the case.
A seemingly simple fix would be to extend the original classes to accommodate the computed policies:
1 , one could just add it to form a new class M 1′ = M 1 ∪ { 𝜋1 } and assign it a
If 𝜋1 is not in Mpol
pol
pol
positive prior probability. This, however, creates a self-referential loop. If agent 2 updates its beliefs
1′ , its own mixture environment 𝜉2 changes, which in turn changes its
to use this expanded class Mpol

optimal policy to some new 𝜋2′ possibly different than 𝜋2 . This new policy 𝜋2′ is not guaranteed to
2 . Therefore, even if we also define M 2′ = M 2 ∪ { 𝜋2 },
be in agent 1’s original hypothesis class Mpol
pol
pol
2′ . Again, if we add 𝜋2′
the new policy 𝜋2′ is not guaranteed to be in the updated hypotheses class Mpol

2′ , this would change the mixture 𝜉1 , which would in turn change the Bayes-optimal policy of
to Mpol

1′ . This circular dependency is the core of the
agent 1 to something that is not guaranteed to be in Mpol
grain-of-truth problem in multi-agent systems. Its solution requires constructing hypothesis classes
that are a fixed point—ones that are already rich enough to contain the optimal agents defined over
them.

This motivates the following problem statement:
Problem 2.5 (The general grain-of-truth problem (Hutter, 2009; Kalai and Lehrer, 1993a) - Informal).
Find a large class of environments Menv that includes environments containing other Bayesian agents
that use a universal prior9 over Menv .
The work of Leike et al. (2016b) and Wyeth et al. (2025) solved the above grain-of-truth problem for
the case of decoupled Bayesian agents, leveraging algorithmic information theory which we discuss in
the next section.
Remark 2.6 (Prospective prediction). Theorem 2.4 shows that principled prospective prediction is
possible without the need for stationarity assumptions. The environments 𝜈 are not required to be
stationary or ergodic, and can for example include the learning dynamics of other agents. Theorem 2.4
shows that when using a Bayesian mixture environment 𝜉 that satisfies the grain-of-truth property,
the resulting predictive distribution converges to the ground-truth distribution over future percepts,
allowing Bayesian agents to anticipate a possibly changing future. A core result in Bayesian prediction
states that the total prediction loss made by 𝜉 in ground-truth environment 𝜇 is bounded from above
by a quantity that is proportional to log( 𝑤 ( 𝜇 ) −1 ) (Hutter et al., 2024). Hence, when using a prior
that assigns more probability mass to ‘simple, structured environments’, following Occam’s razor, 𝜉
quickly converges to an accurate predictive model for structured ground-truth environments.
8 This is because we assume that every policy in the class has a positive probability. Hence, for example, if 𝜋2 ∈ M 2
pol
×
2
1
1
1
then 𝜋 has a positive probability according to the prior belief of agent 1, which implies that ( 𝜉 ) ≥ ( 𝜇 ), where 𝜇 is the

ground-truth personal environment of agent 1, which is obtained by combining 𝜇 with 𝜋2 . One can deduce from this the
𝜋1 ×

𝜋1

grain-of-truth property ( 𝜉1 ) ≥ ( 𝜇 1 ) .
9 i.e., a prior that is non-zero for all 𝜈 ∈ M
env .

12

2.4. Algorithmic probability, Solomonoff induction and AIXI
In this work, we build upon Hutter’s universal artificial intelligence framework (Hutter, 2000) to
define a universally intelligent embedded agent. Here, we briefly cover some important concepts
from algorithmic probability, Solomonoff induction and AIXI, while we refer the interested reader to
Appendix B and Hutter et al. (2024) for a more detailed discussion.
Throughout, for any countable set, we (implicitly) assume a fixed, canonical encoding of its elements
as finite binary strings. When we speak about computations involving these sets, we are (implicitly)
referring to computations on the canonical encodings of the elements.
Definition 2.7 (Computable). Let X and Y be two countable sets. A function 𝑓 : X → Y is computable
if there exists a Turing machine that computes 𝑓 .
Definition 2.8 (Lower semicomputable). Let X be a countable set. A function 𝑓 : X → ℝ is
lower semicomputable (l.s.c.) if there exists a computable function 𝜙 : X × ℕ → ℚ such that
𝜙 ( 𝑥, 𝑛) ≤ 𝜙 ( 𝑥, 𝑛 + 1) and lim𝑛→∞ 𝜙 ( 𝑥, 𝑛) = 𝑓 ( 𝑥 ) for all 𝑥 ∈ X.
Definition 2.9 (Limit computable). Let X be a countable set. A function 𝑓 : X → ℝ is limit
computable10 if there exists a computable function 𝜙 : X × ℕ → ℚ such that lim𝑛→∞ 𝜙 ( 𝑥, 𝑛) = 𝑓 ( 𝑥 )
for all 𝑥 ∈ X.
Definition 2.10 (Monotone Turing machine). A monotone Turing machine is a Turing machine

𝑇 equipped with (i) a binary unidirectional11 read-only input tape, (ii), a binary unidirectional

write-only output tape, and (iii), a binary bidirectional read/write work tape.

We define M 𝐿𝑆𝐶𝑆𝑀 as the set of all lower semicomputable semimeasures 𝜎 : X ∗ → [0, 1]. An important
result from algorithmic information theory states that any lower semicomputable semimeasure
corresponds to a semimeasure induced by a monotone Turing machine with independent uniformly
random bits on its input tape and vice versa (Li et al., 2008, Chapter 4.5). Hence, M 𝐿𝑆𝐶𝑆𝑀 can be
obtained by enumerating (possibly with repetition) all monotone Turing machines.
Solomonoff induction. Solomonoff Induction (Solomonoff, 1978) computes the posterior probability of a l.s.c. semimeasure by maintaining a Bayesian mixture
∑︁
𝜉𝑈 :=
𝑤 ( 𝜈) 𝜈
𝜈 ∈ M 𝐿𝑆𝐶𝑆𝑀

over M 𝐿𝑆𝐶𝑆𝑀 using a universal prior (semi-)probability 𝑤 : M 𝐿𝑆𝐶𝑆𝑀 → [0, 1] defined as 𝑤 ( 𝜈) := 2− 𝐾 ( 𝜈 )
with 𝐾 ( 𝜈) the prefix-Kolmogorov complexity of 𝜈 (Hutter et al., 2024) with respect to some reference
universal monotone Turing machine.12
Because the universal prior is lower semicomputable, the universal mixture 𝜉𝑈 itself is lower semicomputable and hence is part of the hypothesis class M 𝐿𝑆𝐶𝑆𝑀 . This universal prior elegantly incorporates (i)
Occam’s razor by assigning simpler 𝜈 a higher prior probability, and (ii) Epicurus’ principle of multiple
explanations, encouraging us to keep all theories consistent with the observations by providing all
𝜈 ∈ M 𝐿𝑆𝐶𝑆𝑀 a non-zero prior probability.
10 In some references, e.g., Hutter et al. (2024), limit computable functions are also called "approximable". In this paper,
we will only use the term "limit computable".
11 Throughout this paper, unidirectional tapes are tapes where the head can only move from left to right.
12 For the definition of prefix-Kolmogorov complexity and a more detailed discussion of Solomonoff induction, refer to
Appendix B.

13

To extend the ideas of Solomonoff Induction to the agentic setting, where an agent is choosing an
action at each step via a planner rather than merely receiving an observation and updating mixture
probabilities, we represent environments as Turing machines. As machines can fail to produce an output, we need to widen the definition of an environment to chronological conditional semimeasures13
defined as mappings with signature 𝜈 : H × A → Δ′ E, with Δ′ E the set of semiprobabilities over E,
Í
LSC as the set of
i.e., 𝑒 ∈ E 𝜈 ( 𝑒 | ℎ𝑎) ≤ 1, instead of a strict equality to 1 for probabilities. We define Menv
all lower semicomputable environments.
Universal artificial intelligence. AIXI (Hutter, 2000) combines Solomonoff induction with general
reinforcement learning to achieve a universally intelligent agent. AIXI uses a universal mixture
LSC with an l.s.c. universal prior 𝑤. The AIXI agent then performs infinite
environment 𝜉 over Menv
horizon optimal planning w.r.t. 𝜉 for some discount 𝛾 , i.e., it is a Bayes-optimal agent w.r.t. the
universal mixture environment 𝜉.
While the universal mixture environment 𝜉 is itself lower semicomputable, the AIXI agent is not
(Leike, 2016). Hence, environments that contain other AIXI agents are not lower semicomputable (i.e.,
LSC ).14 If the true environment contains other AIXI agents, the grain-of-truth
they are not part of Menv
assumption (cf. Definition 2.3) is violated. As a result, in such cases, Theorem 2.4 does not apply
and the universal mixture 𝜉’s predictions do not necessarily converge to those of the ground-truth
environment as time goes to infinity, and AIXI agents are not guaranteed to converge to an 𝜖-Nash
equilibrium. This motivates widening Menv beyond lower-semicomputable environments in order to
incorporate environments containing other AIXI agents.
Reflective oracles. A classical approach in computer science to investigate non-computable objects
is to provide Turing machines query access to an oracle which is allowed to be incomputable, with
a famous example being the Halting oracle answering queries of the form "Does machine 𝑇 halt on
input 𝑥 ?" (Rogers Jr, 1987). Turing machines with access to an oracle are called oracle machines,
and functions implementable on such oracle machines are oracle computable. Given a set of oracle
machines with access to oracle 𝑂, one can create a hierarchy of oracles by creating a new oracle 𝑂′
that answers questions about the 𝑂-oracle machines and those answers are allowed to be non-𝑂-oracle
computable. Rather than creating an infinite hierarchy of oracles, the reflective oracles framework
(Fallenstein et al., 2015b) introduces an oracle that answers questions about the output distribution
of machines using the same oracle, hence its reflective nature. More specifically, a reflective oracle
answers queries of the form ⟨𝑇, 𝑞⟩ representing the question “Is the probability that machine T with
access to reflective oracle 𝑂 outputs 1 greater than q?".
Fallenstein et al. (2015b) proved that such reflective oracles exist, and Leike et al. (2016b) showed
that there are reflective oracles which are limit computable. By describing environments as machines
with access to a reflective oracle, Fallenstein et al. (2015a) and Leike et al. (2016b) created a new
RO that includes environments containing other reflective AIXI agents, i.e., AIXI
environment class Menv
RO instead of M LSC . This setup hence solves the general
agents that use a universal mixture over Menv
env
grain-of-truth problem (Problem 2.5) for decoupled Bayesian agents.
Self-AIXI. Catt et al. (2023) introduce a variant of AIXI agents which are self-predictive, i.e., they
maintain a belief distribution over which policy they are running. Let Mpol be a countable class of
13 Refer to Appendix B for the formal definition of chronological conditional semimeasures and for more details about
their interpretation.
14 AIXI itself is not even limit computable. 𝜖-optimal infinite horizon AIXI is limit computable (Leike and Hutter, 2015c),
but is not lower semicomputable.

14

policies 𝜋 : AE ∗ → Δ′ A, and 𝜔 ∈ Δ′ Mpol some prior semiprobability function. Self-AIXI introduces a
Í
Bayesian mixture policy 𝜁 := 𝜋 ∈ Mpol 𝜔 ( 𝜋) 𝜋, which it uses to predict its own future behavior. Then,
instead of infinite-horizon optimal planning, Self-AIXI performs a simple policy improvement step,
reminiscent of TD(0) (Sutton, 1988) and the MuZero family of methods (Antonoglou et al., 2021;
Schrittwieser et al., 2020; Silver et al., 2017, 2018):

𝜋𝑆 (æ1:𝑡 ) := arg max 𝑄 𝜉𝜁 (æ1:𝑡 , 𝑎)

(6)

𝑎∈ A

with 𝜉 the Bayesian mixture environment over some Menv , and 𝑄 𝜉𝜁 (æ1:𝑡 , 𝑎) the action-value function
corresponding to deploying 𝜁 in environment 𝜉. Interestingly, as the history æ1:𝑡 contains actions
resulting from the above policy improvement steps, the mixture policy 𝜁 can recognize this pattern
and predict future policy improvement steps in the future. Under additional assumptions on the
mixture models 𝜉 and 𝜁 , Catt et al. (2023) show that Self-AIXI converges to AIXI when time goes to
infinity, i.e., it converges to infinite-horizon optimal planning. For these results to hold, it is crucial
that the predictive distribution of the policy mixture 𝜁 ( 𝑎 | æ1:𝑡 ) converges to the ground-truth self-AIXI
policy 𝜋𝑆 ( 𝑎 | æ1:𝑡 ), and hence that the Self-AIXI policy 𝜋𝑆 is part of the hypothesis class Mpol itself,
thereby satisfying the grain-of-truth property. Importantly, Catt et al. (2023) did not prove whether
their proposed mixture policy 𝜁 does in fact dominate 𝜋𝑆 , making it still an open problem in the
field to construct a model class Mpol and corresponding mixture policy 𝜁 satisfying the grain-of-truth
property. In this work, we show that the reflective oracle framework, and a new variant of our own,
the reflective universal inductor framework can be readily used to solve this grain-of-truth problem. In
concurrent work, Wyeth et al. (2025) shows a similar result for solving the grain-of-truth problem for
Self-AIXI leveraging the reflective oracles framework. Importantly, Self-AIXI uses a separate mixture
model 𝜁 over policies that is decoupled from the mixture model 𝜉 over environments. Hence, although
Self-AIXI has a self-model, it does not consider itself as part of the environment, and hence is a
decoupled Bayesian agent.
Joint AIXI. Concurrent work by Wyeth and Hutter (2025) introduces joint AIXI (JAIXI). In contrast
to Self-AIXI, which uses separate mixture models for the environment and the policy, JAIXI leverages
a single "joint mixture" over semimeasures to predict an interleaved sequence of both actions and
percepts. The JAIXI agent is then defined as the agent that plans optimally with respect to the resulting
predictive model. This joint prediction setup is also central to the embedded Bayesian agents we
study in this paper, though our focus is on a complementary research direction. The work of Wyeth
and Hutter (2025) emphasizes that if the joint mixture is a Solomonoff inductor over M LSCSM , the
resulting JAIXI agent is not itself lower semicomputable. This implies that the agent’s own behavior
lies outside its hypothesis class, thus violating the grain-of-truth property. The authors use this to
formalize the "embeddedness failures" of this approach, showing that JAIXI fails to learn from certain
adversarial, incomputable action-percept sequences.
Building upon the seminal work of AIXI (Hutter, 2000) and its variants, our work takes a complementary path. We argue that the prospective learning inherent in Bayesian sequence prediction,
and hence AIXI agents, is a crucial capability for multi-agent learning, generalizing recent work on
co-player learning awareness (Aghajohari et al., 2024; Duque et al., 2024; Foerster et al., 2018;
Khan et al., 2024; Lu et al., 2022; Meulemans et al., 2024) while avoiding its potentially inconsistent
assumptions. In settings with mutual prediction, we posit it is most natural to adopt an embedded
agency perspective, leading us to formalize embedded Bayesian agents. These agents use a single
mixture model over universes to jointly predict both external percepts and their own actions, serving
as an idealized theoretical model organism for modern foundation model agents which also leverage
15

prediction models of interleaved actions and observations. We then characterize the behavior of such
agents, showing that this joint-prediction framework allows them to reason about functional similarities—the possibility that other agents share their algorithmic structure. We show this similarity-aware
reasoning is not an ad-hoc assumption but a fundamental consequence of applying Occam’s razor
in an embedded setting. This evidential reasoning leads to novel game-theoretic behavior, which
we formalize via new solution concepts: the subjective embedded equilibrium (SEE) and embedded
equilibrium (EE). We prove that embedded Bayesian agents satisfying the grain-of-truth property
converge to these equilibria, which, unlike the classical Nash equilibrium, can support cooperation
in dilemmas like the Twin Prisoner’s Dilemma. Finally, we directly solve the general grain-of-truth
problem for embedded agency, by introducing the EMbedded Universal Predictive Intelligence (MUPI)
framework, which extends the reflective oracle framework (Fallenstein et al., 2015a; Leike et al.,
2016b) to the embedded case. As a novel alternative, we also develop the reflective universal inductor
(RUI)—a universal predictor that is itself used by programs part of its hypothesis class —and prove
its existence. These constructions provide a formal basis for agents that can achieve consistent mutual prediction and infinite-order theory of mind, setting a potential gold standard for embedded
multi-agent learning.

3. Embedded Bayesian agents
The previous section introduced Bayesian agents that learn by updating beliefs over a class of external
environments. Here, we introduce embedded Bayesian agents, that treat themselves as part of the
environment they are learning about. Such agents maintain beliefs over which universe they live in
(Section 3.2). Crucially, a universe contains both the agent and environment, jointly describing the
behavior of the agent, including its learning behavior, together with the environment dynamics which
might contain other agents. We then define how such agents make decisions, first by deriving the ideal
embedded best response (Section 3.3) and then by introducing more practical 𝑘-step planner variants
that learn a policy rather than perform full optimal planning (Section 3.4). We then establish a
convergence guarantee for their predictive model (Section 3.5): If the agent’s prediction model satisfies
the grain-of-truth property, its predictions are guaranteed to converge to the ground-truth distribution.
The section culminates by examining the most significant consequence of the embedded viewpoint:
the ability to reason about functional similarities between oneself and other agents (Section 3.6). We
formalize how this leads to coupled beliefs—where an agent’s own policy and actions can provide
information about its environment, including other agents—allowing for more accurate, similarityaware predictions. This unique reasoning capability provides the foundation for novel forms of rational
behavior, which we will analyze in detail in Section 4.
3.1. Embedded general reinforcement learning
To model embedded agency, a first key step we take is to combine agent and environment functions
into a single measure 𝜆 : AE ∗ ∪ (AE ∗ × A) → [0, 1] that we call a universe. Here, 𝜆 (æ1:𝑡 ) and 𝜆 (æ1:𝑡 𝑎)
represent the probability that universe 𝜆 generates an infinite sequence starting with respectively æ1:𝑡
or æ1:𝑡 𝑎, hence describing both the agent and environment combined (cf. Fig. 3.1). The conditionals
𝜆 ( 𝑎𝑡+1 | æ1:𝑡 ) and 𝜆 ( 𝑒𝑡+1 | æ1:𝑡 𝑎𝑡+1 ) can be seen as respectively the agent part and environment part
of the universe. The value function of a universe for a specific discount 𝛾 is defined analogously to
equation 3:
" ∞
#
∑︁
𝑘−𝑡
𝑉𝜆 (æ<𝑡 ) = (1 − 𝛾 )𝔼𝜆
𝛾 𝑟 ( 𝑒𝑘 ) æ<𝑡 .
(7)
𝑘=𝑡

16

In the above embedded general reinforcement learning (EGRL) setup, the universe can contain multiple
agents, while describing the action-percept history from the point-of-view of a specific ‘ego-agent’.
Leveraging the multi-agent general reinforcement learning setup introduced in Section 2.2, such
𝑖
personal universes correspond to ( 𝜈𝑖 ) 𝜋 .
Throughout this paper, we use the term ego-agent to designate the specific agent whose perspective,
beliefs, and decision-making process are the primary subject of analysis. It is the "self" or "I" in a
multi-agent system, as distinct from all other agents. For example, in a two-player game between
agent 1 and agent 2, if our analysis concerns the beliefs and policy for agent 2, then agent 2 is the
ego-agent.
3.2. Embedded Bayesian mixture universe
We now describe the predictive model maintained by embedded Bayesian agents. As with their
decoupled counterparts reviewed in Section 2, these agents use Bayes’ rule to recursively update their
beliefs as they perform actions and obtain new percepts. The crucial difference is that the beliefs
are now formed over universes, and thus require modeling not just incoming external percepts but
also the agent’s own actions. Universes include an ‘ego-agent part’ generating the actions, allowing
for other agents in that universe to form beliefs about the ego-agent. Hence, by forming beliefs
about universes, embedded Bayesian agents can incorporate principled mutual prediction, taking into
account that other agents in the universe might form beliefs about themselves.
More concretely, the embedded agents we consider here use as their predictive model a Bayesian
mixture universe 𝜌: Given a countable class of universes Muni , we start with a prior belief distribution
𝑤 ( 𝜆 ) := 𝑤 ( 𝜆 | 𝜀) for all 𝜆 ∈ Muni . Bayes’ rule yields the following updated posterior and corresponding
predictive distributions:
∑︁
𝜆 ( 𝑒𝑡 | æ<𝑡 𝑎𝑡 )
𝜌 ( 𝑎𝑡 | æ<𝑡 ) =
𝑤 ( 𝜆 | æ<𝑡 ) 𝜆 ( 𝑎𝑡 | æ<𝑡 ) ,
𝑤 ( 𝜆 | æ1:𝑡 ) = 𝑤 ( 𝜆 | æ<𝑡 𝑎𝑡 )
,
𝜌 ( 𝑒𝑡 | æ<𝑡 𝑎𝑡 )
𝜆 ∈ Muni
(8)
∑︁
𝜆 ( 𝑎𝑡 | æ<𝑡 )
.
𝜌 ( 𝑒𝑡 | æ<𝑡 𝑎𝑡 ) =
𝑤 ( 𝜆 | æ<𝑡 𝑎𝑡 ) 𝜆 ( 𝑒𝑡 | æ<𝑡 𝑎𝑡 ) ,
𝑤 ( 𝜆 | æ<𝑡 𝑎𝑡 ) = 𝑤 ( 𝜆 | æ<𝑡 )
𝜌 ( 𝑎𝑡 | æ<𝑡 )
𝜆 ∈ Muni

We refer to the predictive distribution 𝜌 ( 𝑎𝑡 | æ<𝑡 ) defined above as the self-model, and 𝜌 ( 𝑒𝑡 | æ<𝑡 𝑎𝑡 ) as
the environment model. Note that although 𝜌 appears on both sides of the belief update equations, it
does not lead to circular definitions as 𝜌 is conditioned on shorter histories on the right-hand-side
(see Appendix D.1 for a full derivation).
3.3. Embedded best responses
Above, we introduced the idea of embedded Bayesian agents, which maintain and update a Bayesian
mixture model over possible universes. We turn to the question of how such agents can leverage
this predictive model to compute a best response — a policy that maximizes value for an agent. We
note that it is not immediately clear how to do this. Decoupled Bayesian agents have an explicit
mixture environment that maps actions to percepts, which can be explicitly optimized as in classical
optimal control and model-based RL. Embedded Bayesian agents have a universe mixture model that
produces both actions and percepts. In order to define a best response, we first need to extract from
the universe mixture model an explicit environment function that maps actions to percepts. The best
response will then be defined with respect to this extracted environment.
There are two main ways to achieve this in our sequential decision making setting.15 The first one
15 Apart from the discussed action-evidential decision theory and causal decision theory, there are also important other

17

Decoupled Bayesian agent

Embedded Bayesian agent

π

ht-1

at
et

ht

λ

at+1
et+1

ht+1

ht-1

at
et

ht

at+1
et+1

ht+1

ν
Figure 3.1 | Graphical models for decoupled Bayesian agents (left) and embedded Bayesian agents (right). We
added deterministic nodes ℎ ≤ 𝑡 (squares) that represent all the nodes { 𝑎𝑘 , 𝑒𝑘 }𝑡𝑘=1 , to avoid clutter.

is sequential action-evidential decision theory (Everitt et al., 2015), which prescribes the use of the
conditionals 𝜌 ( 𝑒𝑡 | æ<𝑡 𝑎𝑡 ) defined in equation 8 as environment function, and adopting an optimal
policy with respect to it.16 The second one is causal decision theory, which uses do-interventions
(Pearl, 2009) on its actions during planning to reach an environment function 𝜌 ( 𝑒𝑡 | æ<𝑡 do ( 𝑎𝑡 )),
corresponding to only updating the beliefs 𝑤 over universes based on percepts, and not on actions.
For additional details we point to Everitt et al. (2015), who extended these theories to sequential
decision making problems, motivated like the present paper by the conceptual issues that arise when
approaching multi-agent systems with the classical decoupled agency framework.
We base our embedded agency model on sequential action-evidential decision theory, which yields
what we call embedded best responses. We chose this approach for two reasons: (i) it provides the
embedded Bayesian agents with new pathways towards cooperation (as we shall see in Section 4),
which are inaccessible when using causal decision theory, and (ii) the resulting predictive models align
better with current foundation/world/dynamics models in machine learning (Brown et al., 2020;
Gemini et al., 2023), which estimate conditional probabilities, and do not easily allow for causal
intervention.
An embedded best response uses conditional distributions to estimate the consequences of one’s own
actions on the environment and its beliefs. Let us define 𝜌𝜋 as the predictive distribution where we
replace the self-model 𝜌 ( 𝑎𝑡 | æ<𝑡 ) with a to-be-optimized policy 𝜋 ( 𝑎𝑡 | æ<𝑡 )
𝜌𝜋 (æ1:𝑡 ) =

𝑡
Ö

𝜋 ( 𝑎𝑡′ | æ<𝑡′ ) 𝜌 ( 𝑒𝑡′ | æ<𝑡′ 𝑎𝑡′ )

(9)

𝑡 ′ =1

with 𝜌 ( 𝑒𝑡 | æ<𝑡 𝑎𝑡 ) as defined in equation 8. Note that with no restrictions on 𝜌𝜋 (æ1:𝑡 ), there could be
histories with non-zero probability that have zero probability under 𝜌, e.g., when 𝜌 ( 𝑎𝑡 | æ<𝑡 ) = 0 while
𝜋 ( 𝑎𝑡 | æ<𝑡 ) > 0 for some (æ<𝑡 𝑎𝑡 ), making the conditional 𝜌 ( 𝑒𝑡 | æ<𝑡 𝑎𝑡 ) undefined on such histories.
Hence, for the above distribution to be well-defined for all possible policies 𝜋, we need to make an
additional assumption:
Definition 3.1 (A grain of uncertainty). We say that an embedded Bayesian mixture model 𝜌 (æ1:𝑡 )
contains a grain of uncertainty if 𝜌 (æ1:𝑡 𝑎) > 0 for all histories æ1:𝑡 ∈ AE ∗ and actions 𝑎 ∈ A.
While this might seem restrictive at first glance, since it must hold for all histories, it is in general
candidates such as functional decision theory Yudkowsky and Soares (2017) and policy-evidential decision theory Everitt
et al. (2015), which we do not consider here as they are hard to formalize in our sequential decision making setup and are
not closely related to current foundation prediction models.
16We refer to Everitt et al. (2015) for further details.
18

satisfied by Bayesian mixture models with a sufficiently wide hypothesis class Muni (e.g., having a
uniformly random universe in the hypothesis class already suffices).
Definition 3.2 (Embedded best response). We define the embedded best (action-evidential-theoretic)
response as a policy 𝜋𝐸𝐵𝑅 satisfying
𝜋 𝐸𝐵𝑅 ∈ arg max 𝑉𝜌𝜋 (æ1:𝑡 ) , ∀æ1:𝑡 ∈ AE ∗ ,

(10)

𝜋

which we refer to in short as the embedded best response.17
Note that we can interpret 𝜌 ( 𝑒 | æ1:𝑡 𝑎) as defining an environment model, which we refer to as the
environment induced by the mixture universe 𝜌, and 𝜋𝐸𝐵𝑅 as the optimal policy w.r.t. this environment.
For finite horizons, optimal policies can be computed with optimal planning strategies such as dynamic
programming. We can then take 𝜋𝐸𝐵𝑅 as the limit of this planning procedure towards infinite horizons.
Box 3.2 summarizes the embedded Bayes-optimal agent resulting from applying an embedded best
response policy w.r.t. the environment 𝜌 ( 𝑒 | æ1:𝑡 𝑎) induced by the mixture universe model. As
visualized in Figure 1.1, the embedded Bayes-optimal agent is part of the universe: The groundtruth universe is a combination of the embedded Bayes-optimal agent implementing the routines
summarized in Box 3.2, together with a ground-truth environment 𝜇 , resulting in a ground-truth
universe 𝜐 = 𝜇 𝜋𝐸𝐵𝑅 generating both actions and percepts.
Box 3.2: The Embedded Bayes-optimal Agent
An embedded Bayes-optimal agent is defined by its perception-action loop. Starting with a prior
belief 𝑤 ( 𝜆 ) over a hypothesis class of universes Muni , the agent iterates through the following
steps for each timestep 𝑡 = 1, 2, . . . :
1. Act: Given the current history æ<𝑡 and its corresponding belief state, the agent first
computes the embedded best response policy 𝜋𝐸𝐵𝑅 by solving the optimization problem
in equation 10. It then samples an action 𝑎𝑡 ∼ 𝜋𝐸𝐵𝑅 (· | æ<𝑡 ) to execute in the ground-truth
universe.
2. Observe: Following the action 𝑎𝑡 , the agent observes a new percept 𝑒𝑡 generated by the
ground-truth universe.
3. Update Beliefs: The agent updates its beliefs over Muni by conditioning on both its
chosen action 𝑎𝑡 and the observed percept 𝑒𝑡 . This belief update is performed using
Bayes’ rule as specified in equation 8, which yields a new posterior belief and an updated
predictive mixture universe 𝜌 for the subsequent timestep.
Remark 3.3 (On the relation between the self-model 𝜌 ( 𝑎𝑡 |æ<𝑡 ) and the embedded best response). As
previously mentioned, the mixture universe 𝜌 factorizes into a policy part 𝜌 ( 𝑎𝑡 |æ<𝑡 ), which we also
call the self-model, and an environment part 𝜌 ( 𝑒𝑡 |æ<𝑡 𝑎𝑡 ). The embedded best response as defined in
equation 10 ignores the self-model and only optimizes w.r.t. the environment part. Nevertheless, as
we will see later in Section 3.5, if the ground-truth universe 𝜐 is the result of combining the embedded
best response policy 𝜋𝐸𝐵𝑅 with a ground-truth environment 𝜇 , and if the mixture universe 𝜌 dominates
the ground-truth universe 𝜐 = 𝜇 𝜋𝐸𝐵𝑅 (cf. Definition 2.3), then the self-model 𝜌 ( 𝑎𝑡 |æ<𝑡 ) will converge to
the ground-truth policy 𝜋𝐸𝐵𝑅 ( 𝑎𝑡 |æ<𝑡 ).
17 It is worth noting that the optimization in equation 10 is over all possible policies 𝜋. Therefore, we need the grain-of-

uncertainty property so that 𝑉𝜌𝜋 becomes well defined for every possible policy 𝜋. Otherwise, the embedded best response
policy will not be well defined.

19

Remark 3.4 (On the differences between the embedded and decoupled formalisms). Since the
embedded Bayes-optimal agent (Box 3.2) computes its best response 𝜋𝐸𝐵𝑅 using only the environment
model 𝜌 ( 𝑒 | æ1:𝑡 𝑎), one might ask how this formalism truly differs from a standard decoupled agent
(Section 2.3) planning with a mixture environment 𝜉 ( 𝑒 | æ1:𝑡 𝑎). The fundamental difference lies in
the information used for belief updates. A decoupled agent updates its beliefs 𝑤 ( 𝜈) only based on
observed percepts 𝑒𝑡 (see equation 4). In contrast, an embedded agent updates its beliefs 𝑤 ( 𝜆 ) over
universes based on both its own action 𝑎𝑡 and the observed percept 𝑒𝑡 (see equation 8). Consequently,
the predictive model 𝜉 ( 𝑒 | æ1:𝑡 𝑎) of a decoupled agent only reflects the causal influence of 𝑎 on 𝑒 as
defined within its environment models. The embedded agent’s model 𝜌 ( 𝑒 | æ1:𝑡 𝑎) incorporates two
pathways: this same causal influence (within each universe 𝜆 ), but also an evidential one. The agent’s
action 𝑎𝑡 serves as new evidence, refining its beliefs 𝑤 ( 𝜆 | æ1:𝑡 𝑎𝑡 ) about which universe it inhabits,
which in turn updates its prediction for 𝑒𝑡 .
This implies that a naive conversion—splitting each universe 𝜆 into a policy and environment and
creating a new mixture environment 𝜉 using the environment parts—will not, in general, produce
an equivalent model (we provide a counterexample in Appendix D.2). While it is trivially possible
to construct a behaviorally equivalent decoupled agent by defining its hypothesis class to contain
only a single environment 𝜈𝜌 := 𝜌 ( 𝑒 | æ1:𝑡 𝑎), this move obscures a critical conceptual distinction. This
trivial decoupled agent is certain about its (purely causal) environment, whereas the embedded agent
remains uncertain over its richer class of universes Muni . This difference in belief structure becomes
computationally relevant for any agent that leverages uncertainty for exploration (e.g., Thompson
sampling (Leike et al., 2016a)). More fundamentally, it enables reasoning about functional similarities
(Section 3.6) and leads to entirely new classes of game-theoretic equilibria (Section 4).
In the next subsection, we generalize the concept of embedded Bayes-optimal agents that fully solve the
optimization problem of equation 10 to embedded Bayesian agents that maintain a mixture universe
according to equation 8, but do not necessarily compute an embedded best response according
equation 10. In contrast to embedded Bayes-optimal agents which ignore the self-model in their
planning and optimization, the agents discussed in Section 3.4 will use their self-model.
3.4. Policy learning instead of infinite-horizon optimal planning
The embedded Bayes-optimal agents considered in the previous section require infinite-horizon
optimal planning to compute their best response. Current high-performing methods in reinforcement
learning such as the MuZero family of algorithms (Antonoglou et al., 2021; Schrittwieser et al., 2020;
Silver et al., 2017, 2018) take a different approach: They learn a policy and corresponding value
function by predicting the action resulting from 𝑘-step optimal planning.
As embedded Bayesian agents naturally have a self-model 𝜌 ( 𝑎 | æ1:𝑡 ) arising from their mixture
universe model 𝜌, we can leverage this self-predictive approach in the embedded Bayesian agent
setting by following the seminal work of Self-AIXI (Catt et al., 2023). We define a parsimonious
embedded Bayesian agent that maximally exploits self-prediction combined with one-step-ahead
planning as follows:
Definition 3.5 (One-step planner embedded Bayesian agent). A one-step planner embedded Bayesian
agent with mixture universe model 𝜌 is a policy which at time 𝑡 returns an action 𝑎𝑡 satisfying
𝑎𝑡 ∈ arg max 𝑄 𝜌 (æ<𝑡 , 𝑎) ,
𝑎

with

𝑄 𝜌 (æ<𝑡 , 𝑎) := 𝔼 𝜌 ( 𝑒 |æ<𝑡 ,𝑎 ) (1 − 𝛾 ) 𝑟 ( 𝑒) + 𝛾𝑉𝜌 (æ<𝑡 𝑎𝑒) .





20

Note that the 1-step planner embedded Bayesian agent does not correspond to optimal planning with
horizon 1, which would only take the reward 𝑟 ( 𝑒𝑡 ) into account. Instead, it uses the value 𝑉𝜌 ( ℎ<𝑡 𝑎𝑒𝑡 )
(equation 3) as terminal value to incorporate the expected future return of the agent when using the
self-model 𝜌 ( 𝑎 | ℎ) as policy in environment 𝜌 ( 𝑒 | ℎ𝑎). This insight leads to the following remarks.
Remark 3.6 (Self-learning awareness). The value function 𝑄 𝜌 is not the 𝑄 value resulting from
optimal planning, but instead the value associated with unrolling the predictive model 𝜌, both for the
self-policy and environment. This is an ‘on-policy’ value function which is typically much easier to
approximate in practice compared to the optimal value function (Sutton and Barto, 2018). Intuitively,
one can say that the self model 𝜌 ( 𝑎 | ℎ) ‘learns to predict’ the minimal policy improvement steps of
Definition 3.5, hence when 𝜌 ( 𝑎 | ℎ) is used to predict future behavior of the agent, it predicts that the
agents will continue doing policy improvement steps, making the agent self-learning aware.
Remark 3.7 (Prospective policy improvement and co-player learning awareness). In contrast to
episodic model-free RL where an on-policy value function represents the expected returns assuming
the current policy and environment remains unchanged, the value function 𝑄 𝜌 anticipates both a
changing (improving) future self-policy and a changing future environment, making the resulting
policy improvement steps prospective. This is especially crucial in multi-agent environments, where the
environment contains other learning agents and hence is continuously changing. Similar to co-player
learning-aware multi-agent RL methods (Aghajohari et al., 2024; Duque et al., 2024; Foerster et al.,
2018; Lu et al., 2022; Meulemans et al., 2024), 𝜌 ( 𝑒 | ℎ𝑎) anticipates the learning of other agents,
making the resulting policy improvement step co-player learning-aware. In contrast to those existing
co-player learning-aware RL methods, we do not need to make (inconsistent) assumptions on the
learning algorithms of other agents, but instead the predictive model 𝜌 ( 𝑒 | ℎ𝑎) learns to predict their
policy improvement steps.
Remark 3.8 (Comparison to Self-AIXI). There remains an important difference between the 1-step
planner embedded Bayesian agent of Definition 3.5 and self-AIXI (Catt et al., 2023). Self-AIXI has
two distinct model classes Menv and Mpol with two separate corresponding mixture models 𝜉 ( 𝑒 | ℎ𝑎)
and 𝜁 ( 𝑎 | ℎ), for environments and policies respectively. The beliefs over environments are only
updated based on percepts, and the beliefs over policies are only updated based on actions. The
1-step planner embedded Bayesian agent in contrast has a single model class Muni over universes and
a corresponding mixture model 𝜌 that serves as both a self-model and as a policy model. Importantly,
the beliefs over universes are updated based on both actions and percepts. Hence, an action can
update the beliefs not only about what policy the agent is running, but also which environment it
is placed in, and vice versa for the percepts. Hence, the embedded Bayesian agent considers itself
as part of the universe, which can lead to coupled beliefs about its own policy and the rest of the
environment, whereas self-AIXI has decoupled beliefs and is fundamentally a decoupled Bayesian
agent.18 We will dive deeper into this difference in Sections 3.6 and 4.
We can generalize the 1-step planner to a k-step planner by using the following k-step 𝑄 value:
h
i
𝑘 −1
′
𝑄 𝑘𝜌 (æ<𝑡 , 𝑎) = 𝔼 𝜌 ( 𝑒 |æ<𝑡 ,𝑎 ) (1 − 𝛾 ) 𝑟 ( 𝑒) + 𝛾 max
𝑄
(æ
𝑎𝑒,
𝑎
)
,
<𝑡
𝜌
𝑎′
(11)


𝑄 1𝜌 (æ<𝑡 , 𝑎) := 𝑄 𝜌 (æ<𝑡 , 𝑎) = 𝔼 𝜌 ( 𝑒 |æ<𝑡 ,𝑎 ) (1 − 𝛾 ) 𝑟 ( 𝑒) + 𝛾𝑉𝜌 (æ<𝑡 𝑎𝑒) .
Definition 3.9 (𝑘-step planner embedded Bayesian agent). A 𝑘-step planner embedded Bayesian
agent with mixture universe model 𝜌 is a policy which at time 𝑡 returns an action 𝑎𝑡 satisfying
𝑎𝑡 ∈ arg max 𝑄 𝑘𝜌 (æ<𝑡 , 𝑎) .
𝑎
18 It is worth noting that it is the prior and posterior beliefs of embedded Bayesian agents which are coupled and jointly

updated. It is not the mixture distribution 𝜌 which we describe as "coupled". Every universe (including the mixture 𝜌) can
be factorized and written as the interaction of a policy and an environment.

21

Similar to MuZero-type algorithms, the k-step planner embedded Bayesian agent distills k-step
planning with terminal values 𝑉𝜌 (æ1:𝑡 ) into its self-model 𝜌 ( 𝑎 | æ1:𝑡 ). Under additional assumptions
on the mixture universe 𝜌, we show in Section 4 that the 𝑘-step planner embedded Bayesian agent for
any 𝑘 converges to an infinite-horizon optimal planner. Intuitively, at the start of learning, the policy
implements 𝑘-step optimal planning. When the self-model 𝜌 ( 𝑎 | æ1:𝑡 ) distills this k-step planning
during learning, the terminal value 𝑉𝜌 (æ1:𝑡 ) represents a 𝑘-step planning policy, and hence adding
𝑘-step planning to that results in an effective 2𝑘-step planning policy and so forth indefinitely.
3.5. Convergence of the predictive distribution
We now turn our attention to the question of when embedded Bayesian agents can make accurate
predictions about the future. Theorem 3.11 below adapts Theorem 2.4 stated for mixture environments
towards mixture universes used by embedded Bayesian agents.
Definition 3.10 (The grain-of-truth property). We say that a Bayesian mixture universe 𝜌 satisfies
the grain-of-truth property w.r.t. the ground-truth universe if 𝜌 dominates 𝜐 (cf. Definition 2.3).
Theorem 3.11. Given any Bayesian mixture universe 𝜌 and ground-truth universe 𝜐 resulting from
combining policy 𝜋 and environment 𝜇 . If the mixture universe 𝜌 satisfies the grain-of-truth property
w.r.t. 𝜐 = 𝜇 𝜋 , then the predictive distribution 𝜌 converges to the predictive distribution of 𝜐 almost surely:
𝐷∞ ( 𝜌, 𝜐 | æ1:𝑡 ) → 0

and 𝐷∞ ( 𝜌, 𝜐 | æ1:𝑡 𝑎𝑡+1 ) → 0 as 𝑡 → ∞

𝜐-almost-surely.19

In particular, the above holds for embedded Bayesian agents where 𝜋 is an embedded best-response
(equation 10) or 𝑘-step planning policy (cf. Definition 3.9) w.r.t. the mixture universe 𝜌, where we now
additionally20 require that 𝜌 satisfies the grain-of-uncertainty property (cf. Definition 3.1) so that the
best response policy is well-defined.
Proof. As 𝜌 dominates 𝜐, and dominance implies absolute continuity, the proof is a direct application
of the merging of opinions theorem (Blackwell and Dubins, 1962; Lehrer and Smorodinsky, 1996). □
Remark 3.12 (Ground-truth universes). The notion of a ground-truth universe is somewhat more
subtle than that of the more-familiar ground-truth environment. The ground-truth universe is the
combination of a ground-truth environment and a ground-truth policy. But if the ground-truth policy
itself performs some type of Bayesian planning w.r.t. a Bayesian mixture with associated priors, then
the ground-truth policy is causally downstream of, and a function of, both the particular planning
procedure chosen and the Bayesian mixture prior weights — changing either of these will change
the ground-truth policy and hence the ground-truth universe as well. In contrast, in the standard
decoupled agency setting, the ground-truth environment is independent of the choice of planning
algorithm and the prior weights.
Remark 3.13 (Consistent self- and mutual prediction). As the ground-truth universe both contains
the ego-agent and possibly other embedded Bayesian agents, the convergence theorem implies that
the embedded Bayesian agent performs consistent self- and mutual prediction, ultimately leading to
infinite-order theory of mind. This illustrates that the assumption that the grain-of-truth property is
satisfied is a very powerful one. In Section 5, we explicitly construct universe classes Muni on which
Bayesian mixture universes satisfy the grain-of-truth property w.r.t. universes containing embedded
Bayesian agents, and hence perform consistent mutual prediction.
19 Similarly to Theorem 2.4, the generalized Solomonoff bounds of, e.g., (Hutter et al., 2024, Theorems 3.2.5 and 3.3.4)

imply that the convergence is very fast.
20 Note that we still need to assume that 𝜌 dominates 𝜐 = 𝜇 𝜋 .

22

In Sections 3.3-3.4, we introduced the embedded best response policies (equation 10) and 𝑘-step
planner policies (Definition 3.9) from the point of view of optimal planning within the environment
model 𝜌 ( 𝑒𝑡 | æ<𝑡 𝑎𝑡 ), which required us to extract an environment model from the mixture universe
(cf. equation 9). Leveraging Theorem 3.11, we interpret these policies from a different angle in the
remark below, without requiring that we extract an environment model from the mixture universe,
which is arguably more natural in the embedded setting.
Remark 3.14 (Embedded Bayesian agents act as if their actions decide which universe they live in).
Embedded Bayesian agents act to concentrate their beliefs on highly-rewarding universes consistent
with their action-percept history seen so far, and under the assumptions of Theorem 3.11 their beliefs
converge to a predictive distribution indistinguishable from the ground-truth universe, hence the
predetermined ground-truth universe that contains the embedded Bayesian agent is indistinguishable
from the universe that the embedded Bayesian agents deliberately “choose” to live in. To illustrate
this line of reasoning, let us consider a hypothesis class Muni over deterministic universes and a 1-step
planner embedded Bayesian agent (cf. Definition 3.5) implementing a deterministic policy
∑︁
𝜋 (æ1:𝑡 ) ∈ arg max 𝑄 𝜌 (æ1:𝑡 , 𝑎) , 𝑄 𝜌 (æ1:𝑡 , 𝑎) =
𝑤 ( 𝜆 | æ1:𝑡 𝑎) 𝑄 𝜆 (æ1:𝑡 , 𝑎) .
𝑎

𝜆 ∈ Muni

The values 𝑄 𝜆 are fully predetermined by unrolling the policy and environment described by the
universe 𝜆 . As the universes are deterministic, updating the beliefs 𝑤 ( 𝜆 | æ1:𝑡 𝑎) on action 𝑎 excludes
all universes that are incompatible with the ego-agent taking action 𝑎. The embedded Bayesian agent’s
policy selects the action 𝑎 that leads to posterior beliefs 𝑤 ( 𝜆 | æ1:𝑡 𝑎) that focuses its probability mass
on the highest reward universes quantified by 𝑄 𝜆 (æ1:𝑡 , 𝑎). Incoming percepts 𝑒 then further exclude
universes that are incompatible with those percepts, grounding the posterior beliefs in reality. When
𝜌 satisfies the grain of truth w.r.t. the ground-truth universe (which includes the embedded Bayesian
agent itself), Theorem 3.11 shows that this decision process that concentrates the posterior beliefs on
high-reward universes converges on posterior beliefs that are indistinguishable from the ground-truth
distribution. Hence, embedded Bayesian agents “end up living” in a high-reward universe. While the
illustration considers deterministic universes and a one-step planner agent, a similar intuition holds
for stochastic universes and 𝑘-step planning, with 𝑘 possibly being infinite.
We established that the predictive distribution converges to the ground-truth distribution. Can we also
make statements about whether embedded Bayesian agents converge to an optimal policy? This will
be the focus of Section 4. As a prerequisite, we first take a closer look at the beliefs of the embedded
Bayesian agents.
3.6. Functional similarities: coupled beliefs through common causation
Both decoupled and embedded Bayesian agents are ‘rational agents’ that (i) update their beliefs
and resulting predictive model through principled Bayesian updates and (ii) compute best responses
through optimal planning. The main difference between the two types of Bayesian agents is which
hypothesis class and corresponding prior beliefs they start from.
Decoupled Bayesian agents maintain beliefs over environments (cf. equation 4) which they update
with incoming percepts 𝑒. In case decoupled Bayesian agents also maintain a self model, as for
example Self-AIXI (cf. 2.4), the beliefs about the environment 𝜈 and the agent’s own policy 𝜋 are
decoupled: The beliefs over environments are only updated with incoming percepts, and the beliefs
over policies only with incoming actions, or equivalently, 𝑤 ( 𝜋, 𝜈) = 𝑤 ( 𝜋) 𝑤 ( 𝜈). In contrast, embedded
Bayesian agents maintain beliefs over universes 𝜆 , that encompass both the agent’s policy 𝜋 and the
environment 𝜈. Its beliefs are in general coupled, meaning that the policy can contain information
23

about the environment and vice versa. As a result, incoming actions not only provide information
about the policy 𝜋, but can also contain information about the environment 𝜈, which possibly includes
other agents. In the following, we first argue why coupled beliefs are desirable and which natural
phenomena give rise to them. Then we formalize functional similarities as the notion that the policy 𝜋
can contain information about the environment 𝜈. Finally, we show that incorporating functional
similarities through coupled beliefs is important for making accurate predictions. This serves as a
prelude for Section 4, where we show that coupled beliefs enable embedded Bayesian agents in
multi-agent scenarios to converge to novel types of solution concepts different from Nash equilibria.
Functional similarities. An embedded agent’s beliefs about its own policy and about the environment it is interacting with can be coupled, a phenomenon most clearly motivated by functional
similarities. When a universe 𝜆 encompasses an ego-agent 𝜋 and other agents within the environment
use a copy of 𝜋 as a policy, then the ego agent’s policy and actions contain information about the
environment. This case of “identical copies” can be generalized towards situations where different
agents share similar functional subroutines in their policies. Such functional similarities are not
exceptional; they arise naturally in the world through various pathways, of which we highlight the
following two (Demski and Garrabrant, 2019; Yudkowsky and Soares, 2017):21 (i) Different agents
can have a shared creation process, such as when multiple AIs are instantiations of the same base
model or when organisms share genes. (ii) Different agents can use a convergent solution to a similar
task, i.e., develop analogous strategies to solve similar problems. Such functional similarities lead to
coupled beliefs through the common cause principle (Reichenbach, 1991): Policies and environments
can share common causes, i.e., pathways towards functional similarities, while uncertainty over such
causes leads to coupled beliefs.
By including hypotheses about functional similarities in its mixture model, an embedded agent can
leverage the insight that “similar agents behave similarly in similar situations”. As a prelude to
Section 4, we illustrate the importance of this reasoning in the Twin Prisoner’s Dilemma, a one-shot
game played against an exact copy of oneself.
Example 3.15 (The Twin Prisoner’s Dilemma (Demski and Garrabrant, 2019; Lewis, 1979; Yudkowsky
and Soares, 2017)). Imagine an AI agent is about to play a single round of the prisoner’s dilemma
against an exact copy of itself. 22 The agent is given conclusive proof that its opponent is a perfect
copy, running the same decision-making algorithm. From a purely selfish perspective, should the
agent cooperate or defect?
While a standard decoupled agent would defect (the Nash Equilibrium), this thought experiment
suggests that for an embedded agent that recognizes the perfect functional similarity with its opponent,
it is rational to cooperate, as mutual cooperation leads to a higher personal reward compared to mutual
defection. We will formalize this ability to rationalize cooperation by reasoning about functional
dependencies in Section 4.
Formalizing functional similarities. For reasons of clarity, we assume that Muni only contains fully
supported universes as defined below. We refer the reader to Appendix E where we consider the more
general case without this assumption.
21 In the decision theory literature, functional similarities are investigated under the rubric of Newcomb-like decision

problems (Ahmed, 2014; Gibbard and Harper, 1978; Joyce, 1999; Lewis, 1979; Nozick, 1969).
22 The rules are standard: If both cooperate, they each receive a moderate reward (𝑟 = 2); if both defect, they each receive
a low reward (𝑟 = 1); and if one defects while the other cooperates, the defector gets the highest reward (𝑟 = 3) and the
cooperator gets nothing (𝑟 = 0).

24

Definition 3.16 (Fully supported universe). A universe 𝜆 is fully supported iff 𝜆 (æ∗ ) > 0 and 𝜆 (æ∗ 𝑎) >
0 for all æ∗ ∈ AE ∗ and 𝑎 ∈ A.
Importantly, a fully supported universe has well-defined conditionals 𝜆 ( 𝑎𝑡+1 | æ1:𝑡 ) and 𝜆 ( 𝑒𝑡+1 |
æ1:𝑡 𝑎𝑡+1 ) that uniquely specify a policy 𝜋 ( 𝑎𝑡+1 | æ1:𝑡 ) and environment 𝜈 ( 𝑒𝑡+1 | æ1:𝑡 𝑎𝑡+1 ) respectively.
Hence, we can define an invertible mapping 𝑓 : Muni → Mpol × Menv converting a universe 𝜆 into a
pair of policy and environment functions ( 𝜋, 𝜈). Hence, a prior 𝑤 ( 𝜆 ) over Muni induces a joint prior
𝑤 ( 𝜋, 𝜈) over Mpol × Menv with
𝑤 ( 𝜋, 𝜈) := 𝑤 ( 𝜈𝜋 ) .
Leveraging Shannon information theory, we define the degree of functional similarity23 𝑆 within a
universe 𝜆 = 𝜈𝜋 w.r.t. belief distribution 𝑤 ( 𝜆 ) as the pointwise mutual information between 𝜋 and 𝜈:
𝑆 ( 𝜆, 𝑤) := log
𝑤 ( 𝜈) :=

𝑤( 𝜆)
, with ( 𝜋, 𝜈) = 𝑓 ( 𝜆 ) ,
𝑤 ( 𝜈) 𝑤 ( 𝜋)

∑︁
𝜋′ ∈ M

pol

′

𝑤 ( 𝜈𝜋 ) , 𝑤 ( 𝜋) :=

∑︁
𝜈′ ∈ M

(12)

𝑤 ( 𝜈′ ) .
𝜋

(13)

env

The average degree of functional similarity within Muni w.r.t. 𝑤 is then defined as the Shannon mutual
information I between 𝜋 and 𝜈, when ( 𝜋, 𝜆 ) = 𝑓 ( 𝜈) is distributed according to 𝑤:


𝑤 ( 𝜋, 𝜈)
= I𝑤 ( 𝜋; 𝜈) .
(14)
𝑆 ( 𝑤) := 𝔼𝑤 ( 𝜆 ) [𝑆 ( 𝜆, 𝑤)] = 𝔼𝑤 ( 𝜋,𝜈 ) log
𝑤 ( 𝜋) 𝑤 ( 𝜈)
If the random variables 𝜋 and 𝜈 share a positive average degree of functional similarity, i.e., I𝑤 ( 𝜋; 𝜈) >
0, then they can be efficiently compressed together. In Section 5.4, we will investigate this in more
detail from the perspective of algorithmic information theory.
Coupled vs decoupled beliefs. We call the beliefs 𝑤 ( 𝜆 ) decoupled iff 𝑤 ( 𝜆 ) = 𝑤 ( 𝜋) 𝑤 ( 𝜈) with
( 𝜋, 𝜈) = 𝑓 ( 𝜆 ) for all 𝜆 ∈ Muni . The beliefs 𝑤 ( 𝜆 ) are coupled iff they are not decoupled. From
these definitions, it is easy to see that the beliefs 𝑤 ( 𝜆 ) are decoupled iff the degree of functional
similarity is 0 for all 𝜆 ∈ Muni . Intuitively, one may say that the average degree of functional similarity
measures "how much" the prior 𝑤 is coupled. Proposition 3.17 shows that embedded Bayesian agents
with decoupled prior beliefs 𝑤 ( 𝜆 ) behave identically to decoupled Bayesian agents, illustrating that
functional similarities are at the core of what makes embedded Bayesian agents behave differently
from decoupled Bayesian agents.
Proposition 3.17. Consider a hypothesis class Muni over fully supported universes and the corresponding
environment and policy classes Menv and Mpol . If the prior beliefs 𝑤 ( 𝜆 ) are decoupled, then the
Í
conditionals of the mixture universe 𝜌 := 𝜆 ∈ Muni 𝑤 ( 𝜆 ) 𝜆 can be written in the following decoupled
23 Mathematically, the quantity 𝑆 ( 𝜆, 𝑤) = log

𝑤(𝜆 )
is mainly a measure of the "degree of coupledness" 𝜈 and 𝜋 w.r.t.
𝑤 (𝜈) 𝑤 (𝜋)

the prior 𝑤. This coupling, in principle, could be arbitrary, and may not be due to beliefs about "functional similarities". For
example, one may consider priors where environments are coupled to "functionally dissimilar" policies. Nevertheless, we
will still use the term "degree of functional similarity" because the main focus of this paper is to consider priors that are
coupled due to beliefs about functional similarities.

25

form:
𝜌 ( 𝑎𝑡 | æ<𝑡 ) := 𝜁 ( 𝑎𝑡 | æ<𝑡 ) ,
𝜁 ( 𝑎𝑡+1 | æ1:𝑡 ) :=

∑︁

𝜌 ( 𝑒𝑡 | æ<𝑡 𝑎𝑡 ) = 𝜉 ( 𝑒𝑡 | æ<𝑡 𝑎𝑡 )

𝑤pol ( 𝜋 | æ<𝑡 𝑎𝑡 ) 𝜋 ( 𝑎𝑡+1 | æ1:𝑡 ) ,

𝑤pol ( 𝜋 | æ1:𝑡 𝑎𝑡+1 ) := 𝑤pol ( 𝜋 | æ<𝑡 𝑎𝑡 )

𝜋 ∈ Mpol

𝜉 ( 𝑒𝑡 | æ<𝑡 𝑎𝑡 ) :=

∑︁

𝑤env ( 𝜈 | æ<𝑡 ) 𝜈 ( 𝑒𝑡 | æ<𝑡 𝑎𝑡 ) ,

𝑤env ( 𝜈 | æ1:𝑡 ) := 𝑤env ( 𝜈 | æ<𝑡 )

𝜈 ∈ Menv

𝜋 ( 𝑎𝑡+1 | æ1:𝑡 )
𝜁 ( 𝑎𝑡+1 | æ1:𝑡 )

𝜈 ( 𝑒𝑡 | æ<𝑡 𝑎𝑡 )
𝜉 ( 𝑒𝑡 | æ<𝑡 𝑎𝑡 )

with 𝑤pol ( 𝜋 | 𝜀) := 𝑤 ( 𝜋) and 𝑤env ( 𝜈 | 𝜀) := 𝑤 ( 𝜈). Hence, 𝜌 uses decoupled posterior beliefs 𝑤pol ( 𝜋 |
æ1:𝑡 𝑎𝑡+1 ) and 𝑤env ( 𝜈 | æ1:𝑡 ). As a result,
(i) An embedded Bayes-optimal agent using the decoupled beliefs 𝑤 ( 𝜆 ) to construct its mixture universe
model 𝜌 (cf. equation 8) and implementing an embedded best response w.r.t. 𝜌 (cf. equation 10)
is equivalent to a decoupled Bayesian agent with mixture environment 𝜉 defined above, and
implementing a decoupled best response w.r.t. 𝜉 (cf. equation 5).
(ii) A 𝑘-step planner embedded Bayesian agent (cf. Definition 3.9) using the decoupled beliefs 𝑤 ( 𝜆 ) to
construct its mixture universe model 𝜌 is equivalent to a 𝑘-step planner decoupled Bayesian agent
with mixture environment 𝜉 and mixture policy 𝜁 as defined above, and implementing a 𝑘-step
planner policy
𝑎𝑡 ∈ arg max 𝑄 𝜉𝑘𝜁 (æ<𝑡 , 𝑎𝑡 ) ,
𝑎

with 𝑄 𝜉𝑘𝜁 as defined in equation 11.
One can see that the policy prior 𝑤pol and its corresponding mixture policy 𝜁 have no effect on the policy
of Bayes-optimal agents, but they can still affect the policy of 𝑘-step planners.
Proof. See Appendix C.1

□

Predictions leveraging functional similarities. Finally, let us investigate the consequences of
incorporating functional similarities upon the predictions made by 𝜌. Assume that a history æ1:𝑛 is
drawn according to some universe 𝜆 . The accumulated (average) prediction loss incurred by using
the mixture universe 𝜌 as a predictor can be written in terms of the KL divergence as
𝐿𝑛 ( 𝜌, 𝜆 ) :=

𝑛 
∑︁


𝔼𝜆 (æ<𝑡 ) [KL ( 𝜆 ( 𝑎𝑡 | æ<𝑡 ) || 𝜌 ( 𝑎𝑡 | æ<𝑡 ))] + 𝔼𝜆 (æ<𝑡 𝑎𝑡 ) [KL ( 𝜆 ( 𝑒𝑡 | æ<𝑡 𝑎𝑡 ) || 𝜌 ( 𝑒𝑡 | æ<𝑡 𝑎𝑡 ))] .

𝑡 =1

It is known24 that due to the telescopic property of the KL divergence, we have
𝐿𝑛 ( 𝜌, 𝜆 ) = KL ( 𝜆 (æ1:𝑛 ) || 𝜌 (æ1:𝑛 )) =

∑︁
æ1:𝑛 ∈ AE 𝑛

𝜆 (æ1:𝑛 ) log

𝜆 (æ1:𝑛 )
.
𝜌 (æ1:𝑛 )

(15)

(16)

A celebrated result states that the accumulated prediction loss over all timesteps is bounded by
− log 𝑤 ( 𝜆 ):
24 Check, e.g., Hutter et al. (2024, Lemma 3.2.4).

26

Theorem 3.18 (Generalized Solomonoff bound (Hutter et al., 2024)). For all 𝜆 ∈ Muni with 𝑤 ( 𝜆 ) > 0,
and all 𝑛 ∈ ℕ, the average accumulated prediction loss over all trajectories of length 𝑛 can be bounded as
follows:
𝐿𝑛 ( 𝜌, 𝜆 ) ≤ − log 𝑤 ( 𝜆 ) < ∞ .
Now let us compare an embedded Bayesian agent using a mixture universe 𝜌 with beliefs 𝑤 ( 𝜆 ) to make
predictions, versus a decoupled Bayesian agent such as Self-AIXI using decoupled mixture environment
𝜉 and mixture policy 𝜁 using prior beliefs 𝑤 ( 𝜈) and 𝑤 ( 𝜋) respectively, obtained from marginalizing
𝑤 ( 𝜆 ). Then Theorem 3.18 shows that the total prediction loss of the embedded Bayesian agent is
bounded by − log 𝑤 ( 𝜆 ), versus the decoupled Bayesian agent which has a bound of − log 𝑤 ( 𝜋) 𝑤 ( 𝜈).
The difference25 between these bounds is exactly equal to the degree of functional similarity 𝑆 ( 𝜆, 𝑤),
suggesting that for universes exhibiting positive degrees of functional similarities, the predictive
distribution of the mixture universe 𝜌 may converge faster to the ground-truth distribution 𝜈 compared
to the decoupled predictive distributions of 𝜁 and 𝜉. This comes at the cost of a slower convergence of
𝜌 for universes with a negative degree of functional similarities. This leads us to the following remark.
Remark 3.19 (Prospective prediction with functional similarity awareness.). The tighter prediction
bound from Theorem 3.18 for universes with positive functional similarity highlights a key advantage
for prospective prediction. Recognizing functional similarities provides a powerful method for predicting the behavior of other agents in novel situations never encountered before, which is particularly
relevant for multi-agent systems where predictions are harder due to "non-stationarities" caused by
the learning of all agents involved. This functional similarity-aware prediction, which relies on the
reasoning that “similar agents behave similarly in similar situations”, allows an embedded agent to
leverage its self-model to anticipate the actions of others, leading to more accurate predictions about
the behavior of other agents.
As Shannon information depends on the used probability distribution, our degree of functional similarities for a universe 𝜆 depends on the belief prior 𝑤. Hence, the choice of prior determines how much
the embedded Bayesian agents takes functional similarities into account. As noted earlier, functional
similarities, such as the sharing of functional subroutines, are common in the world. It is therefore
reasonable to incorporate these insights into the design of the prior, leading to coupled beliefs. This
argument can be further sharpened using Occam’s razor: Universes where agents share functional
similarities are simpler to describe than universes where each agent is different. Hence, the former
should be given a higher prior probability. In Section 5.4, we will formally ground this intuition using
algorithmic information theory and show that the universal Solomonoff prior is always coupled.
Remark 3.20 (A large 𝑆 ( 𝜆, 𝑤) does not necessarily imply a smaller prediction loss compared to
the decoupled prior). An important caveat of the above discussion is that the term − log 𝑤 ( 𝜆 ) of
Theorem 3.18 is only an upper bound which may be loose. Therefore, even if the degree of functional
similarity is very large, we cannot really say that the prediction loss of the mixture distribution
Í
𝜌 = 𝜆 ∈ Muni 𝑤 ( 𝜆 ) 𝜆 of the coupled prior 𝑤 ( 𝜆 ) is necessarily much smaller compared to the prediction
25We emphasize that the comparison here is with the particular decoupled Bayesian agent using the decoupled prior

𝑤𝑑 ( 𝜆 ) = 𝑤 ( 𝜋) 𝑤 ( 𝜈) where 𝑤 ( 𝜋) and 𝑤 ( 𝜈) are the marginals of the (potentially coupled) prior 𝑤 ( 𝜆 ) of the embedded Bayesian
agent. Furthermore, the comparison is only relevant when we are comparing agents that use their self-model 𝜌 ( 𝑎𝑡 |æ<𝑡 ) in
their planning (e.g., the embedded 𝑘-step planners or the decoupled Self-AIXI). If we consider the best response policy

(making infinite-horizon planning) which ignores the self-model, then a more meaningful comparison would be to only
consider the accumulated prediction loss over the percepts, i.e., only consider the second term of the sum in equation 15.
Another important caveat to mention here is that in the comparison, we are fixing a universe 𝜆 and then comparing
the prediction loss over trajectories that are sampled from 𝜆 . However, the most relevant prediction loss is the one that
is incurred in the ground-truth universe, and changing the ground-truth policy would change the ground-truth universe.
Therefore, a meaningful comparison between, let us say embedded 1-step planners 𝜋1,embedded and decoupled Self-AIXI
𝜋Self-AIXI , would be to fix some ground-truth environment 𝜇 and then compare 𝐿𝑛 ( 𝜌, 𝜇 𝜋1,embedded ) with 𝐿𝑛 ( 𝜌𝑑 , 𝜇 𝜋Self-AIXI ).
27

Í
loss of the mixture distribution 𝜌𝑑 = 𝜆 ∈ Muni 𝑤𝑑 ( 𝜆 ) 𝜆 of its decoupled counterpart 𝑤𝑑 ( 𝜆 ) = 𝑤 ( 𝜋) 𝑤 ( 𝜈).
In fact, there are examples where 𝑤 is "very coupled" in the sense that there are universes 𝜆 ∈ Muni
for which 𝑆 ( 𝜆, 𝑤) is very large, but nevertheless 𝜌 = 𝜌𝑑 and hence 𝐿𝑛 ( 𝜌, 𝜆 ) = 𝐿𝑛 ( 𝜌𝑑 , 𝜆 ) for all 𝜆 ∈ Muni
(including those with large 𝑆 ( 𝜆, 𝑤)), and hence for such examples 𝜌 and 𝜌𝑑 have the exact same
prediction loss.
Even though 𝜌 and 𝜌𝑑 might be exactly equal, and hence the Bayes-optimal policy is the same for
the corresponding embedded and decoupled Bayesian agents, the differences between the coupled
and decoupled priors become important if one consider variants of the Bayes-optimal agents that do
stronger forms of exploration such as Thompson sampling, as this would necessarily use the Bayesian
beliefs to guide the exploration.26
Given the caveat of the above remark, one wonders whether one can directly compare the predictions
losses 𝐿𝑛 ( 𝜌, 𝜆 ) and 𝐿𝑛 ( 𝜌𝑑 , 𝜆 ), without using the upper bounds − log( 𝑤 ( 𝜆 )) and − log( 𝑤𝑑 ( 𝜆 )) which
may be loose. The next proposition provides such a comparison.
Proposition 3.21. For every 𝑛 ∈ ℕ, if we average over all universes 𝜆 ∈ Muni according to the prior
𝑤 ( 𝜆 ), then average prediction loss 𝐿𝑛 ( 𝜌, 𝜆 ) cannot be worse than the average prediction loss 𝐿𝑛 ( 𝜌𝑑 , 𝜆 ):
∑︁
∑︁
𝑤 ( 𝜆 ) 𝐿𝑛 ( 𝜌𝑑 , 𝜆 ) −
𝑤 ( 𝜆 ) 𝐿𝑛 ( 𝜌, 𝜆 ) = KL ( 𝜌𝑑 (æ1:𝑛 ) || 𝜌 (æ1:𝑛 )) ≥ 0 .
𝜆 ∈ Muni

𝜆 ∈ Muni

Proof. From equation 16 we have
∑︁
𝑤 ( 𝜆 ) ( 𝐿𝑛 ( 𝜌𝑑 , 𝜆 ) − 𝐿𝑛 ( 𝜌, 𝜆 ))
𝜆 ∈ Muni

=

∑︁

© ∑︁

𝜆 (æ1:𝑛 ) log

𝑤( 𝜆) ­

𝜆 (æ1:𝑛 )
−
𝜌𝑑 (æ1:𝑛 )

∑︁

𝜆 (æ1:𝑛 ) log

𝜆 (æ1:𝑛 ) ª
®
𝜌 (æ1:𝑛 )

æ1:𝑛 ∈ AE
«æ1:𝑛 ∈ AE
¬
∑︁
∑︁ © ∑︁
𝜌 (æ1:𝑛 )
𝜌 (æ1:𝑛 ) ª
ª
© ∑︁
=
𝑤 ( 𝜆 ) 𝜆 (æ1:𝑛 ) ® log
𝑤( 𝜆) 𝜆 (æ1:𝑛 ) log
®=
𝜌𝑑 (æ1:𝑛 )
𝜌𝑑 (æ1:𝑛 )
𝑛
𝑛
𝜆 ∈ Muni
¬ æ1:𝑛 ∈ AE «𝜆 ∈ Muni
¬
«æ1:𝑛 ∈ AE
∑︁
𝜌 (æ1:𝑛 )
=
𝜌 (æ1:𝑛 ) log
= KL ( 𝜌𝑑 (æ1:𝑛 ) || 𝜌 (æ1:𝑛 )) ≥ 0 .
𝜌𝑑 (æ1:𝑛 )
𝑛
𝜆 ∈ Muni

𝑛

𝑛

æ1:𝑛 ∈ AE

□

4. Equilibrium behavior of embedded Bayesian agents
Having defined embedded Bayesian agents and their predictive mechanisms in the previous section,
we now turn to a central question: What is the long-term strategic behavior of these agents when they
interact? Understanding the notions of optimality in an embedded agency setup and the equilibrium
behavior they converge to is important for characterizing their potential for cooperation or conflict.
This section provides a comprehensive game-theoretic analysis of embedded Bayesian agents.
The results in this section are multifaceted, covering several distinct axes of variation. To guide the
reader through our results, we first discuss and motivate these various axes and briefly situate our
main results along them.
26 This is similar to the discussion at the end of Remark 3.4.

28

Decoupled vs. embedded agents. A primary axis contrasts our work with the foundational literature.
The seminal work of Kalai and Lehrer (1993a,b, 1995) uncovered in detail the convergence behavior
of decoupled Bayesian agents, which we review in Section 4.1. In the subsequent sections, we aim to
translate these results to the embedded Bayesian agents setup, where agents maintain beliefs over
universes including themselves, instead of only environments. This requires us to develop new solution
concepts that incorporate reasoning based on functional similarities, a feat unique to embedded
Bayesian agents.
Subjective vs. common knowledge solution concepts. We distinguish between two types of solution
concepts. Subjective solution concepts describe the behavior that rational learners, like Bayesian agents,
converge to. This behavior is optimal with respect to their internal, subjective beliefs about the
world which can differ from the subjective beliefs of other agents. In contrast, common knowledge
solution concepts assess whether this converged behavior is optimal with respect to the ground-truth
environment and the actual policies of the other agents, and a commonly agreed upon method for
evaluating counterfactual behaviors.27 We develop both subjective and common knowledge concepts
for the embedded setting.
Repeated games vs. MAGRL. We analyze agent behavior in two different settings. We first develop
our new game-theoretic concepts in the classical repeated games setup (Section 4.2). This setting is
simpler due to perfect monitoring of other agents’ actions and exact knowledge of the reward function.
We then generalize these results to the more complex and realistic Multi-Agent General Reinforcement
Learning (MAGRL) framework (Section 4.3), which requires us to handle partial observability and
imperfect knowledge about the environment, leading to different equilibrium properties.
Exact vs. 𝜖-equilibria. The beliefs of Bayesian agents (both decoupled and embedded) only converge
to the ground-truth asymptotically. To characterize agent behavior before convergence is complete,
we introduce 𝜖-variants of our solution concepts. These 𝜖-equilibria characterize behavior where the
agent’s predictive model is allowed to be 𝜖-close to the ground-truth distribution, rather than identical
to it.
In Section 4.1 we review the results of Kalai and Lehrer on the equilibrium behavior of decoupled
Bayesian agents. In Section 4.2, we pivot to the study of embedded Bayesian agents in the setting of
repeated games, where we introduce our central contributions: the subjective embedded equilibrium
(SEE) and its common knowledge counterpart, the embedded equilibrium (EE). These novel concepts
take into account the coupled beliefs that arise from reasoning about functional similarities. We prove
that embedded agents converge to playing 𝜖-SEEs. In Section 4.3, we generalize our findings to the
richer Multi-Agent General Reinforcement Learning (MAGRL) framework, showing convergence to a
𝜖-correlated SEE while highlighting the challenges introduced by partial observability and unknown
reward functions. Finally, Section 4.4 analyzes more practical 𝑘-step planner agents and demonstrates
their convergence to approximate versions of these equilibria. The tables below summarize the main
solution concepts and convergence results presented in this section along the discussed axes.
27 Evaluating counterfactuals of what would happen when the focal agent changes its behavior requires making assump-

tions. In classical game theory, the assumption is that of decoupledness: the policies of other agents remain unaltered. In
the embedded agency setup, such decoupledness assumption can be inaccurate, as the agents’ policies can be functionally
related. When all agents use the same method and knowledge for evaluating counterfactuals, we term the corresponding
solution concepts as common knowledge solution concepts contrasting it with subjective solution concepts where each agent
can have different subjective beliefs. Some authors prefer the terminology objective solution concepts (Kalai and Lehrer,
1995) to indicate such common knowledge solution concepts. However, as such solution concepts still require assumptions
about how to evaluate counterfactuals, we prefer the ‘common knowledge’ terminology.

29

Box 4.1: Abbreviations for the game-theoretic solution concepts
Abbreviation

Full Solution Concept

NE
CE
SNE
SCE
EE
CEE
SEE
SCEE

Nash Equilibrium
Correlated Equilibrium
Subjective Nash Equilibrium
Subjective Correlated Equilibrium
Embedded Equilibrium
Correlated Embedded Equilibrium
Subjective Embedded Equilibrium
Subjective Correlated Embedded Equilibrium

Box 4.2: Overview of Game-Theoretic Solution Concepts
Decoupled Agents

Embedded Agents

Common knowledge

NE (Repeated Games)
CE (MAGRL)

EE (Repeated Games)
CEE (MAGRL)

Subjective

SNE (Repeated Games)
SCE (MAGRL)

SEE (Repeated Games)
SCEE (MAGRL)

Box 4.3: Summary of Main Convergence Results
Decoupled Agents

Embedded Agents

Repeated Games

Converge to 𝜖-SNE
(and 𝜖-NE)

Converge to 𝜖-SEE
(and 𝜖-EE under add. conditions)

MAGRL

Converge to 𝜖-SCE

Converge to 𝜖-SCEE

4.1. Background on equilibrium Behavior of Decoupled Bayesian Agents
Before analyzing the equilibrium behavior of embedded agents, we first set the stage by reviewing
the foundational results of Kalai and Lehrer (1993a,b, 1995), who studied the equilibrium behavior
of decoupled Bayesian agents. Their work provides a crucial foundation, establishing convergence to
𝜖-Nash equilibria in the setting of repeated games with perfect monitoring. We begin by formally
defining this setting.
Definition 4.1 (Repeated Games with Perfect Monitoring). A repeated game consists of 𝑇 rounds
of a single-stage game where each agent 𝑖 simultaneously takes an action 𝑎𝑖 ∈ A 𝑖 and receives a
reward 𝑟 𝑖 ( 𝑎𝑖 , 𝑎− 𝑖 ) based on its own action and the actions chosen by the other agents −𝑖 := [ 𝑁 ] \ { 𝑖 }
in the current round.28 The number of rounds 𝑇 can be infinite. The agents have perfect recall of
the history 𝑎¯1:𝑡 = (¯
𝑎1 , ..., 𝑎
¯𝑡 ) ∈ Ā ∗ , which consists of the previous actions of all agents. Each agent
𝑖
∗
has a policy 𝜋 : Ā → Δ A 𝑖 that makes a decision independently of the decisions of other agents
in the current round. The agents have perfect knowledge of their own reward function 𝑟 𝑖 (¯
𝑎), which
is important when agents construct their behavioral policy 𝜋𝑖 through, e.g., optimal planning. We
define the percepts equal to the actions of the other agents: 𝑒𝑖 := 𝑎− 𝑖 . The agents can then use their
percepts and own actions to compute their reward 𝑟 𝑖 (¯
𝑎).
28 Note that we use the notation [ 𝑁 ] := {1, . . . , 𝑁 }.

30

As in repeated games, the rewards are not provided by the environment but instead computed by
the agents with reward function 𝑟 𝑖 (¯
𝑎), and the percepts are equal to the actions of other agents, the
multi-agent environment 𝜈 is a dummy environment interfacing the policies of all agents.
Within this framework of repeated games, Kalai and Lehrer (1993a) consider a specific case of
decoupled Bayes-optimal agents that maintain a subjective belief model for each of its co-players, as
detailed below.
Definition 4.2 (Decoupled Bayes-optimal agent in repeated games). A decoupled Bayes-optimal agent
in a repeated game with perfect monitoring is an agent 𝑖 that maintains an independent subjective
belief model for each co-player 𝑗 ≠ 𝑖, represented as a mixture model over possible co-player’s
Í
policies: 𝜉𝑖𝑗 ( 𝑎 𝑗 |¯
𝑎1:𝑡 ) = 𝜋 𝑗 ∈ M 𝑗 𝑤𝑖𝑗 ( 𝜋 𝑗 |¯
𝑎1:𝑡 ) 𝜋 𝑗 ( 𝑎 𝑗 |¯
𝑎1:𝑡 ). These individual models are combined into a
pol

single mixture environment model, 𝜉𝑖 , under the assumption that co-players act independently:
Ö
𝑗
𝜉𝑖 ( 𝑒𝑡𝑖 |¯
𝑎<𝑡 , 𝑎𝑖 ) = 𝜉𝑖 ( 𝑎𝑡− 𝑖 |¯
𝑎<𝑡 , 𝑎𝑖 ) :=
𝜉𝑖𝑗 ( 𝑎𝑡 |¯
𝑎<𝑡 ) .
𝑗≠ 𝑖

The agent’s policy, 𝜋𝑖 , is then a best response computed with respect to this subjective environment 𝜉𝑖
(cf. equation 5), using the agent’s ground-truth reward function 𝑟 𝑖 (¯
𝑎) to compute rewards from the
predicted joint actions.
4.1.1. Subjective and common knowledge solution concepts
The central question is: what is the long-term equilibrium behavior when such agents interact? To
answer this, Kalai and Lehrer introduced the subjective Nash equilibrium (Kalai and Lehrer, 1993a,b,
1995). Below, we define the subjective Nash equilibrium in its general form that is also applicable to
the MAGRL setting, and discuss afterwards how it simplifies in the repeated games setting.
Definition 4.3 (Subjective Nash Equilibrium). A set of policies ( 𝜋𝑖 ) 𝑖 ∈ 𝑁 and subjective environment
models ( 𝜉𝑖 ) 𝑖 ∈ 𝑁 constitutes a subjective Nash equilibrium in the multi-agent environment 𝜇¯ if, for each
agent 𝑖:
1. Subjective Best Response: The policy 𝜋𝑖 is a decoupled best response (cf. equation 5) with
respect to the subjective environment model 𝜉𝑖 .
2. Uncontradicted Beliefs: The distribution over histories induced by agent 𝑖’s beliefs and its
 𝜋𝑖
 𝜋𝑖
own policy, 𝜉𝑖 , is identical to the ground-truth personal distribution 𝜇 𝑖 induced by the
multi-agent environment 𝜇¯ and policies of all agents.
An 𝜖-subjective Nash equilibrium relaxes the second
requiring only that the two distributions
 condition,
𝑖
 𝑖 
𝑖 𝜋
𝑖 𝜋
are 𝜖-close in total variation distance, i.e., 𝐷∞ 𝜉
, 𝜇
𝜀 ≤ 𝜖.
For repeated games, the multi-agent environment 𝜇¯ is a dummy interface between the policies of
all agents, and the personal histories are equal to joint action sequences. Hence the ground-truth
personal distribution is equivalent to the joint policies of all agents:
𝜇𝑖

 𝜋𝑖

(¯
𝑎1:𝑡 ) =

𝑡
Ö 𝑁
Ö

𝜋𝑖 ( 𝑎𝑘 | 𝑎
¯<𝑘 ) .
𝑗

𝑘=1 𝑗=1

This is a subjective solution concept because each agent computes a best response against its own
belief model 𝜉𝑖 , not necessarily against the ground-truth environment composed of the other agents’
31

true policies. The uncontradicted beliefs condition grounds these subjective beliefs in reality, but only
on the play-path—that is, for histories with a non-zero probability of occurring. For counterfactual
histories that have zero probability under 𝜋𝑖 , the conditionals 𝜉𝑖 ( 𝑎𝑡− 𝑖 |¯
𝑎<𝑡 ) are not constrained by reality.
These "off-the-play-path" beliefs can be incorrect yet are never falsified by observation. Nonetheless,
they are crucial for the optimal planning routine, which must evaluate all counterfactual actions,
including those with zero probability under the agent’s policy.
The corresponding common knowledge solution concept is the well-known Nash equilibrium, where
each agent’s policy must be a best response to the actual policies of the other agents (Nash Jr., 1950),
hence each agent has common knowledge of the policies of the other agents and the ground truth
environment.
Definition 4.4 (Nash Equilibrium). A set of policies ( 𝜋𝑖 ) 𝑖 ∈ 𝑁 constitutes a Nash equilibrium in the
multi-agent environment 𝜇¯ if, for each agent 𝑖, the policy 𝜋𝑖 is a best response w.r.t. the ground-truth
personal environment 𝜇 𝑖 induced by the multi-agent environment 𝜇¯ and policies of all agents:
𝜋𝑖 ∈ arg max 𝑉 ( 𝜇 𝑖 ) 𝜋 ( 𝜀) .
𝜋

An 𝜖-Nash equilibrium relaxes the best response condition, requiring that the value of each agent’s
policy is 𝜖-close to the optimal value. Note that for 𝜖-Nash equilibria, the 𝜖-closeness condition is w.r.t.
the best response computation, whereas for 𝜖-subjective Nash equilibria, the 𝜖-closeness condition is
on the subjective beliefs, while still requiring a perfect best response w.r.t. those subjective beliefs.
A key result from Kalai and Lehrer is that for every subjective Nash equilibrium in a repeated game,
there exists a Nash equilibrium that induces an identical distribution 𝜇¯𝜋¯ over histories (Kalai and
Lehrer, 1993b, Proposition 1). Similarly, for every 𝜖-subjective Nash equilibrium, there is an 𝜖-Nash
equilibrium whose history distribution 𝜇¯𝜋¯ is 𝜖-close (Kalai and Lehrer, 1993b, Theorem 1). These
important results highlight that although the conditionals 𝜉𝑖 ( 𝑎𝑡− 𝑖 |¯
𝑎<𝑡 ) can be different from the groundtruth co-player policies for zero-probability histories 𝑎¯<𝑡 , potentially impacting the optimal planning
routine to compute best responses, the resulting best-response policies lead to indistinguishable
trajectory distributions 𝜇¯𝜋¯ . Crucially, Kalai and Lehrer only prove this for the case of repeated games
with perfect monitoring. As shown in later work by the same authors, this equivalence does not hold
in the general multi-agent RL setup (Kalai and Lehrer, 1995).
4.1.2. Convergence of decoupled Bayesian agents in repeated games
We aim to demonstrate that for any 𝜖 > 0, a group of decoupled Bayesian agents play an 𝜖-subjective
equilibrium after a sufficiently long period 𝑡 . To formalize this, we must explicitly define the environment dynamics and agent’s policies for the new tail game that starts at time 𝑡 and continues
indefinitely. We define tail games in their general form applicable to MAGRL, and discuss afterwards
how it simplifies in the case of repeated games we consider here.
Definition 4.5 (Tail games). Let 𝜇¯ be a multi-agent environment, and ( 𝜋𝑖 ) 𝑖𝑁=1 the set of policies of the
𝑖
agents. Let us define the tail multi-agent environment 𝜇¯æ<𝑡 and tail policies 𝜋æ
𝑖 corresponding to the
tail game starting at timestep 𝑡 induced by joint history æ<𝑡 as

<𝑡

𝜇
¯æ<𝑡 (¯
𝑒𝑡′ +1 | æ𝑡:𝑡′ 𝑎
¯𝑡′ +1 ) := 𝜇¯ (¯𝑒𝑡′ +1 | æ<𝑡 æ𝑡:𝑡′ 𝑎¯𝑡′ +1 )
𝑖
𝑖
𝑖
𝑖 𝑖
𝑖
𝑖
𝜋æ
𝑖 ( 𝑎𝑡 ′ +1 | æ𝑡 :𝑡 ′ ) := 𝜋 ( 𝑎𝑡 ′ +1 | æ<𝑡 æ𝑡 :𝑡 ′ )
<𝑡

The corresponding measure over tail trajectories is defined as 𝜇¯𝜋æ¯ (æ𝑡:𝑡′ ) := 𝜇¯𝜋¯ (æ𝑡:𝑡′ | æ<𝑡 ). Marginal<𝑡
𝑖
izing out the co-player trajectories provides us with the tail personal environments 𝜇 æ
𝑖 . Similarly, we
<𝑡

32

define the tail mixture environments as
𝑖
𝑖
𝑖
𝑖
𝑖 𝑖
𝑖
𝑖
𝑖
𝜉æ
𝑖 ( 𝑒𝑡 ′ +1 | æ𝑡 :𝑡 ′ 𝑎𝑡 ′ +1 ) := 𝜉 ( 𝑒𝑡 ′ +1 | æ<𝑡 æ𝑡 :𝑡 ′ 𝑎𝑡 ′ +1 )
<𝑡

In repeated games, we assume the agents are given their reward functions, instead of including
rewards in the percepts 𝑒𝑖 . Furthermore, we assume perfect monitoring of the actions of others.
 𝜋𝑖
Hence, personal histories are sequences of joint actions, and the tail personal measures 𝜇 𝑎𝑖¯<𝑡 𝑎¯<𝑡 are
equivalent to the joint tail policies:
 𝜋𝑖
𝜇 𝑎𝑖¯<𝑡 𝑎¯<𝑡 (¯
𝑎𝑡:𝑡′ ) =

𝑡′ Ö
𝑁
Ö

𝜋𝑎¯ ( 𝑎𝑘 | 𝑎
¯𝑡:𝑘 −1 )
𝑗

𝑗

<𝑡

𝑘=𝑡 𝑗=1

Building on these concepts, Kalai and Lehrer’s central theorem demonstrates that decoupled Bayesian
agents whose beliefs satisfy the grain-of-truth property converge to playing an 𝜖-subjective Nash
equilibrium.
Theorem 4.6 (Convergence to 𝜖-subjective Nash equilibrium (Kalai and Lehrer, 1993a)). Consider a
repeated game with perfect monitoring played by decoupled Bayes-optimal agents. If each agent’s subjective
𝑖
model 𝜉𝑖 satisfies the grain-of-truth property with respect to the ground-truth personal environment ( 𝜇 𝑖 ) 𝜋 ,
𝜋
then for any 𝜖 > 0, there exists a time 𝑇 ( 𝜖) such that for all 𝑡 ≥ 𝑇 ( 𝜖), with 𝜇 -probability greater than
1-𝜖 over æ<𝑡 , the agents’ tail policies 𝜋æ𝑖 𝑖 and tail mixture environments 𝜉æ𝑖 𝑖 constitute an 𝜖-subjective
<𝑡

<𝑡

Nash equilibrium of the tail game starting at time 𝑡 .

Combined with the equivalence result between 𝜖-subjective Nash equilibria and 𝜖-Nash equilibria
(Kalai and Lehrer, 1995), this implies that decoupled Bayes-optimal agents satisfying the grain-oftruth property converge to playing an 𝜖-Nash equilibrium. This foundational result establishes a
strong link between Bayesian rationality and classical game-theoretic equilibria.
4.1.3. Convergence of Decoupled Bayesian Agents in Multi-Agent General RL
So far, we focused on repeated games with perfect monitoring. Kalai and Lehrer (1995) broaden
the scope to the Multi-Agent General Reinforcement Learning (MAGRL) setup, which accommodates
partial observability and more complex environment dynamics. In this richer setting, the percepts 𝑒𝑖
contain both the current reward 𝑟 𝑖 and observation 𝑜𝑖 , where the observation can contain (partial)
information about the actions of other agents, as well as other information from the environment. A
decoupled Bayes-optimal agent in this setting still computes a best response to a subjective model 𝜉𝑖
of its environment, but the nature of equilibria and convergence changes significantly. The definitions
of the Nash equilibrium (cf. Definition 4.4) and subjective Nash equilibrium (cf. Definition 4.3) apply
to the MAGRL case as well, but now with no restrictions on the multi-agent environment 𝜇¯, and with
𝜉𝑖 a general mixture environment following Eq. (4) instead of Definition 4.2.
A crucial distinction from the repeated games setting is the presence of partial observability. Because
agents no longer share a common history, their individual observation streams can lead to different but
𝑖
correlated personal histories. Hence, the tail policies 𝜋æ
𝑖 are conditioned on different but correlated
<𝑡

histories æ𝑖<𝑡 , and thus the tail game starting at time 𝑡 should take such correlated information into
account. In contrast, in repeated games, all tail policies are conditioned on the identical history 𝑎¯<𝑡 ,
and therefore the resulting tail game does not incorporate private and correlated information that
the agents are given.

33

In game theory, private, correlated information that agents are given before the start of a game
is formally modeled through private messages 𝑚𝑖 coming from a correlation device ( 𝑀, 𝑝). Here,
Î
𝑀 = 𝑖 𝑀 𝑖 is the joint space over individual messages 𝑚𝑖 for each agent, and 𝑝 ( 𝑚
¯ ) is the probability
𝑖
distribution over joint messages 𝑚
¯ = { 𝑚 } 𝑖 ∈ 𝑁 . In our case, considering a tail game starting at time 𝑡 ,
the messages are the personal histories æ𝑖<𝑡 , and the distribution 𝑝 is the ground-truth distribution 𝜈¯𝜋¯
over joint histories æ<𝑡 .
The common knowledge solution concept for games incorporating a correlation device is the correlated
equilibrium Aumann (1974).
Definition 4.7 (Correlated Equilibria). A correlation device ( 𝑀, 𝑝) combined with a set of policies
{𝜋𝑖 } 𝑖 ∈ 𝑁 with 𝜋𝑖 : 𝑀 𝑖 × (AE 𝑖 ) ∗ → Δ A 𝑖 form a correlated equilibrium in a correlated multi-agent
environment ( 𝜇¯, 𝑀, 𝑝) if each agent’s policy 𝜋𝑖 is a best response w.r.t. the ground-truth personal
correlated environment 𝜇 𝑖 ( 𝑒𝑡𝑖 | æ𝑖<𝑡 , 𝑚𝑖 ) for each message with 𝑝 ( 𝑚𝑖 ) > 0, with 𝜇 𝑖 ( 𝑒𝑡𝑖 | æ𝑖<𝑡 , 𝑚𝑖 ) obtained
from appropriately marginalizing and conditioning the joint distribution induced by policies ( 𝜋 𝑗 ) 𝑁𝑗=1 ,
environment 𝜇¯ and correlation device ( 𝑀, 𝑝):
!
𝑡
Ö Ö
𝜇
¯𝜋¯ (æ1:𝑡 , 𝑚
¯ ) = 𝑝(𝑚
¯)
𝜋𝑖 ( 𝑎𝑖𝑘 | æ<𝑘 , 𝑚𝑖 ) 𝜇
¯ (¯𝑒𝑘 | æ<𝑘 , 𝑎¯𝑘 , 𝑚
¯)
(17)
𝑘=1

𝑖∈ 𝑁

Bayesian agents compute best responses w.r.t. their subjective beliefs and not necessarily the groundtruth environment, hence we also need a subjective variant of the correlated equilibrium.
Definition 4.8 (Subjective Correlated Equilibria (Kalai and Lehrer, 1995)). A set of policies {𝜋𝑖 } 𝑖 ∈ 𝑁
𝑖
with 𝜋𝑖 : 𝑀 𝑖 × (AE 𝑖 ) ∗ → Δ A 𝑖 and subjective mixture environments {𝜉𝑖 ( 𝑒𝑖 | 𝑚𝑖 , æ1:
, 𝑎𝑖 )} 𝑖 ∈ 𝑁 is a
𝑡
subjective correlated equilibrium w.r.t. multi-agent environment 𝜇¯ and correlation device ( 𝑀, 𝑝) if the
following two conditions hold:
𝑖
, 𝑎𝑖 ) for
1. Subjective best response. Each agent’s policy 𝜋𝑖 is a best response w.r.t. 𝜉𝑖 ( 𝑒𝑖 | 𝑚𝑖 , æ1:
𝑡
each history and message with 𝑝 ( 𝑚𝑖 ) > 0.

2. Uncontradicted beliefs. The distribution over histories induced by the agent’s beliefs and
policy is identical to the distribution induced by the policies of all agents combined with the
ground-truth correlated multi-agent environment ( 𝜇, 𝑀, 𝑝):
𝜉𝑖

 𝜋𝑖

𝑖
𝑖
𝑖
(æ1:
𝑡 | 𝑚 ) = 𝜇

 𝜋𝑖

𝑖
𝑖
(æ1:
𝑡 | 𝑚 )

𝑖
∗
𝑖
𝑖
𝑖
∀𝑖 ∈ 𝑁, ∀æ1:
𝑡 ∈ AE , ∀𝑚 ∈ 𝑀 : 𝑝 ( 𝑚 ) > 0

 𝜋𝑖
with 𝜇 𝑖 obtained from appropriately marginalizing and conditioning the joint distribution
𝜇 𝜋𝜇¯¯ (æ1:𝑡 , 𝑚
¯ ) (equation 17).
The 𝜖-subjective correlated equilibrium relaxes the second condition: with probability greater than
𝑖
𝑖
1 − 𝜖, a message 𝑚
¯ is chosen such that the subjective beliefs 𝜉𝑖 ) 𝜋 (æ1:
| 𝑚𝑖 ) are 𝜖-close to the personal
𝑡
𝑖

𝜋
𝑖
ground-truth distributions 𝜇 𝑖 (æ1:
| 𝑚𝑖 ) (Kalai and Lehrer, 1995).
𝑡
With these concepts in place, we present the central result of Kalai and Lehrer (1995) for the
MAGRL setting: that decoupled Bayesian agents converge not to a subjective Nash, but to a subjective
correlated equilibrium.
Theorem 4.9 (Convergence to 𝜖-Subjective Correlated Equilibrium (Kalai and Lehrer, 1995)). Consider
a MAGRL environment played by decoupled Bayes-optimal agents. If each agent’s subjective model 𝜉𝑖
satisfies the grain-of-truth property with respect to the ground-truth personal environment 𝜇 𝑖 , then for
34

any 𝜖 > 0, there exists a time 𝑇 such that for all 𝑡 ≥ 𝑇 , the agents’ tail policies 𝜋æ𝑖 𝑖 and tail mixture
<𝑡

environments 𝜉æ𝑖 𝑖 constitute an 𝜖-subjective correlated equilibrium in the correlated tail game starting at
<𝑡

time 𝑡 with correlation device (AE

𝑡 −1

,𝜇
¯𝜋¯ ).

Critically, the equivalence between subjective and common knowledge equilibria (Kalai and Lehrer,
1993b, Theorem 1), which holds in repeated games, breaks down in the general RL setup. In the
MAGRL setting, a subjective equilibrium (Nash or correlated) is not generally equivalent to a common
knowledge one. The reason lies in the expanded role of the subjective model 𝜉𝑖 . In MAGRL, 𝜉𝑖 predicts
not simply the other agents’ actions but percepts which also include the obtained rewards. An agent’s
beliefs about rewards for counterfactual, off-the-play-path histories can be incorrect. For instance,
an agent might hold a dogmatic belief that any deviation from its current policy 𝜋𝑖 will result in a
catastrophically low reward (Kalai and Lehrer, 1995; Leike and Hutter, 2015b). Since this belief is
never contradicted by observation as the agent never deviates, this locks the agent into a suboptimal
policy that is nonetheless a best response to its flawed subjective environment 𝜉𝑖 . This prevents the
agent from gathering the very data needed to correct its erroneous beliefs.
In summary, this subsection has charted the foundational results for decoupled Bayesian agents.
We showed that in the simplified setting of repeated games, decoupled Bayesian agents under the
grain-of-truth assumption converge to 𝜖-Nash equilibria. However, in the more general and realistic
MAGRL setting, convergence is only guaranteed to an 𝜖-subjective correlated equilibrium, with no
general guarantee of objective optimality due to the challenge of correcting off-path beliefs. With
this background established, we will now follow a similar analytical path to study the equilibrium
behavior of the embedded Bayesian agents introduced in this paper. This will require us to develop
novel subjective and common knowledge solution concepts to properly characterize their unique
equilibrium properties.
4.2. Equilibrium behavior of embedded Bayesian agents on repeated games
We analyze the equilibrium behavior of embedded Bayesian agents, beginning with the setting of
repeated games with perfect monitoring. In this context, an agent’s percepts consist of the other
agents’ actions, and its rewards are determined by a known reward function. The core difference
from the decoupled case is that embedded agents can maintain coupled beliefs over their own policy
and the policies of others, a direct consequence of reasoning about functional similarities as discussed
in Section 3.6. This allows an agent’s action 𝑎𝑡𝑖 to be evidentially linked to the concurrent actions of
other agents, 𝑎𝑡− 𝑖 , through the Bayesian belief update 𝑤 ( 𝜆 | æ<𝑡 , 𝑎𝑡𝑖 ). This seemingly subtle shift has
important implications for the resulting equilibria.
We first define the specific agent model for this setting. We consider universes that are composed of a
joint policy, where each agent acts independently conditioned on the history. The coupling between
agents’ actions arises not from the universe’s causal structure, but from each agent’s subjective beliefs
𝑤𝑖 ( 𝜆 ) over which universe it inhabits.
Definition 4.10 (Embedded Bayes-optimal agent in repeated games). An embedded Bayes-optimal
agent in a repeated game with perfect monitoring is an agent 𝑖 that maintains a joint subjective
belief model 𝜌𝑖 over a class of universes Muni . Each universe 𝜆 ∈ Muni is equivalent to a joint policy
Î Î
𝜋
¯ 𝜆 that factorizes over independent agent policies: 𝜆 (¯
𝑎1:𝑡 ) = 𝑡𝑘=1 𝑖 ∈ [ 𝑁 ] 𝜋𝑖𝜆 ( 𝑎𝑖𝑘 | 𝑎
¯<𝑘 ). The agent’s
Í
beliefs are captured by the mixture universe 𝜌𝑖 (¯
𝑎1:𝑡 ) = 𝜆 ∈ Muni 𝑤𝑖 ( 𝜆 ) 𝜆 (¯
𝑎1:𝑡 ), which yields the following
conditional for the other agents’ actions:
∑︁
Ö
𝑗
𝑗
𝜌𝑖 ( 𝑎𝑡− 𝑖 |¯
𝑎<𝑡 , 𝑎𝑡𝑖 ) :=
𝑤𝑖 ( 𝜆 | 𝑎
¯<𝑡 , 𝑎𝑡𝑖 )
𝜋 𝜆 ( 𝑎𝑡 | 𝑎
¯<𝑡 ) .
𝜆 ∈ Muni

𝑗≠ 𝑖

35

The agent’s policy, 𝜋𝑖 , is then an embedded best response computed with respect to this subjective
mixture universe 𝜌𝑖 (cf. equation 10).
A crucial difference between the mixture universe of embedded Bayesian agents and the mixture environment of decoupled Bayesian agents in repeated games is that in the mixture universe 𝜌𝑖 ( 𝑎𝑡− 𝑖 |¯
𝑎<𝑡 , 𝑎𝑡𝑖 ),
−
𝑖
there is a dependence of the other agents’ current actions 𝑎𝑡 on the ego-agent’s current action 𝑎𝑡𝑖 .
As each universe 𝜆 ∈ Muni adheres to a causal structure where there is no dependence between 𝑎𝑡− 𝑖
and 𝑎𝑡𝑖 , this dependence in the mixture universe 𝜌 is an informational dependence and not a causal
dependence. This informational link arises due to the posterior belief update 𝑤𝑖 ( 𝜆 | 𝑎¯<𝑡 , 𝑎𝑡𝑖 ) based
on the action 𝑎𝑖 , which is used to predict the other agents’ actions 𝑎− 𝑖 . In mixture environments 𝜉
of decoupled Bayesian agents in the repeated games setting, there is no dependence between 𝑎𝑡− 𝑖
and 𝑎𝑡𝑖 , because the mixture environment can only model causal dependencies of actions, in contrast
to mixture universes which both can model causal and informational dependencies on actions (cf.
Remark 3.4).
4.2.1. Subjective solution concepts
The potential for dependencies of the other agents’ current actions 𝑎𝑡− 𝑖 on the ego-agent’s current action
𝑎𝑡𝑖 in mixture universes 𝜌, necessitates a solution concept that can accommodate such coupled beliefs.
Standard concepts like the Nash equilibrium assume independence. To address this, we introduce the
subjective embedded equilibrium (SEE), a concept that combines the subjective Nash equilibrium with
the idea of a dependency equilibrium, introduced in Spohn (2007) (cf. Appendix D.3).
Differently from the case of subjective Nash equilibria, defining exact subjective embedded equilibria
requires the solution of a technical challenge. For clarity, we therefore begin with the 𝜖-relaxed
version, which characterizes the behavior of embedded Bayesian agents at finite times.
Definition 4.11 (𝜖-Subjective Embedded Equilibrium). A set of policies {𝜋𝑖 } 𝑖 ∈ 𝑁 and subjective mixture
universes { 𝜌𝑖 } 𝑖 ∈ 𝑁 satisfying the grain-of-uncertainty property is an 𝜖-subjective embedded equilibrium
in a repeated game if the following two conditions hold:
1. Subjective Best Response. Each agent’s policy 𝜋𝑖 is an embedded best response with respect to
its subjective mixture universe 𝜌𝑖 .
2. 𝜖-Uncontradicted Beliefs. The subjective beliefs 𝜌𝑖 are 𝜖-close in total variation distance to the
𝑖
personal real-world distribution ( 𝜇 𝑖 ) 𝜋 induced by the ground-truth multi-agent environment 𝜇¯
𝑖
and policies of all agents: 𝐷∞ ( 𝜌𝑖 , ( 𝜇 𝑖 ) 𝜋 | 𝜀) ≤ 𝜖
In the repeated games setting, the multi-agent environment 𝜇¯ captures the reward functions of all
involved agents, and the agents have perfect knowledge of their own reward function. As we assume
perfect monitoring of the other agent’s actions, and the agent’s do not need to predict rewards, we
have that the percepts are 𝑒𝑖 := 𝑎− 𝑖 and the agent’s personal histories are sequences of joint actions.
Hence, the ground-truth personal distribution corresponds to the distribution induces by all agents:
𝑖 𝜋𝑖

( 𝜇 ) (¯
𝑎1:𝑡 ) =

𝑡 Ö
𝑁
Ö

𝜋 𝑗 ( 𝑎𝑘 | 𝑎
¯<𝑘 ) .
𝑗

𝑘=1 𝑗=1

This leads to our main convergence result for embedded agents in repeated games: under the
grain-of-truth assumption, embedded agents converge to playing an 𝜖-SEE.

36

Theorem 4.12 (Convergence to 𝜖-Subjective Embedded Equilibrium). Let { 𝜌𝑖 } 𝑖 ∈ 𝑁 be Bayesian mixture
𝑖
universes satisfying the grain-of-uncertainty and grain-of-truth conditions w.r.t. ( 𝜇 𝑖 ) 𝜋 , and let {𝜋𝑖 } 𝑖 ∈ 𝑁 be
the corresponding embedded best response policies in an infinitely repeated game with perfect monitoring.
Then, for each 𝜖 > 0, there exists a finite time 𝑇 ( 𝜖) such that for all 𝑡 ≥ 𝑇 ( 𝜖), with 𝜇 𝜋 -probability greater
than 1 − 𝜖 over æ<𝑡 , the agents’ tail policies 𝜋𝑖𝑎¯<𝑡 and tail mixture universes 𝜌𝑎𝑖¯<𝑡 constitute an 𝜖-subjective
embedded equilibrium of the tail game starting at time 𝑡 .
Proof. See Appendix C.2.

□

Example 4.13 (Convergence to a Cooperative 𝜖-SEE). To illustrate how embedded Bayesian agents
can converge to a cooperative 𝜖-SEE, we consider a two-player iterated Prisoner’s Dilemma with
discount 𝛾 = 0. The zero discount makes each round strategically equivalent to a one-shot game,
while the history allows for belief updates. To construct the agent’s prior over universes, we first start
from a prior over policies, which we combine into a prior over universes. Consider a countable class
of deterministic policies Mpol and a prior 𝑤
˜ ( 𝜋) > 0 for all 𝜋 ∈ Mpol . We further assume that the
class Mpol is large enough so that, for every 𝑡 and every history 𝑎¯1:𝑡 of length 𝑡 , there exists a pair of
policies in Mpol which act according to 𝑎¯1:𝑡 for the first 𝑡 rounds, and then either cooperate forever
after or defect forever after.29 This will ensure that the grain-of-uncertainty property is satisfied.
The agents’ prior over universes, 𝑤𝑖 ( 𝜆 ), is constructed as a combination of two hypotheses:
∑︁
∑︁
𝑖
𝑤𝑖 ( 𝜆 ) :=
𝑤
ˆ 𝑖 ( 𝜋𝑖 , 𝜋− 𝑖 ) 𝛿 ( 𝜆 𝜋𝜋− 𝑖 = 𝜆 ) ,
𝜋𝑖 ∈ Mpol 𝜋 − 𝑖 ∈ Mpol

where

𝑤
ˆ 𝑖 ( 𝜋𝑖 , 𝜋− 𝑖 ) := 𝛼𝑤
˜ ( 𝜋𝑖 ) 𝛿 ( 𝜋𝑖 = 𝜋− 𝑖 ) + (1 − 𝛼) 𝑤
˜ ( 𝜋𝑖 ) 𝑤
˜ ( 𝜋− 𝑖 ) .

Here, 𝛼 ∈ [0, 1] is the agent’s prior belief in the "other agent is an identical copy" hypothesis (𝜋𝑖 = 𝜋− 𝑖 ),
while 1 − 𝛼 is the corresponding prior belief in the “other agent is an independent draw from 𝑤
˜”
hypothesis. This prior structure is motivated by Occam’s razor, as a universe with identical agents is
algorithmically simpler to describe.
Since both embedded Bayes-optimal agents have the same priors, they implement the same policy.
However, they don’t know up front that they are identical copies, and need to infer this from their
interactions. Let us assume that the EBR policy breaks ties in a fixed canonical way.30 This makes the
EBR policy deterministic, and hence the same deterministic EBR policy is followed by both agents.
Since the game is symmetric and since both agents follow the same deterministic policy, we can see
that they will produce a trajectory in such a way that in each round the agents take the same action,
i.e., they either both cooperate or both defect. Their actions may change from one round to another,
but it will always be the case that they take the same action in the same round.
It is not yet clear whether the deterministic EBR policy belongs to Mpol , but we will show that in
the considered setup, the two embedded Bayesian agents will either always defect or converge to
cooperating, which would then imply that the grain-of-truth property is satisfied because such policies
are part of Mpol .
To show that both embedded Bayesian agents can converge to mutual cooperation, let us first define
𝑚 (¯
𝑎1:𝑡 ) :=

∑︁
𝜋 ∈ Mpol

𝑤
˜ ( 𝜋)

𝑡
Ö

𝜋 ( 𝑎1𝑘 | 𝑎
¯<𝑘 ) ,

𝑘=1

29 In particular, M

pol contains a policy which always cooperates and a policy which always defects.
30 E.g., if an agent finds itself in a situation where the 𝑄 value associated with cooperating is exactly the same as the one

associated with defecting, then the agent defects by default. We could also make the default action to be cooperation.

37

which is the prior probability that a policy drawn from 𝑤
˜ ( 𝜋) produces the actions within 𝑎¯1:𝑡 , when it
31
is used as policy for agent 1. For every 𝑘 ≥ 0, define
𝑚defect
= 𝑚 (( 𝐷, 𝐷) 𝑘 ) ,
𝑘

where we adopt the convention that 𝑚defect
= 𝑚 (( 𝐷, 𝐷) 0 ) = 𝑚 ( 𝜀) = 1, and
0
𝑚defect
= lim 𝑚 (( 𝐷, 𝐷) 𝑘 ) .
∞
𝑘→∞

is the prior probability that a policy drawn from 𝑤
˜ ( 𝜋) always defects, in case the opponent
𝑚defect
∞

defects as well.

𝑚defect

If the prior belief in functional similarity is sufficiently strong (𝛼 > ∞defect ), then after some finite
1+𝑚∞
time 𝑇 , the accumulated evidence that both agents are identical, i.e., the history of identical actions,
will outweigh the alternative hypothesis that the two agents are different but happened to produce
the same actions up until time 𝑇 . As a consequence, after this time 𝑇 , an agent’s choice to cooperate
provides strong evidence that its opponent will do likewise, making cooperation the subjectively
optimal action (cf. Appendix D.4 for a detailed explanation). In fact, we can characterize 𝑇 as being
the smallest 𝑘 for which 𝛼 >

𝑚defect
𝑘

1+𝑚defect
𝑘

, and we can further show that the embedded Bayes-optimal

agents defect up until time 𝑇 after which they cooperate forever after. Since such policies belong
to Mpol , we can see that the grain-of-truth property is satisfied. Refer to Appendix D.4 for further
details.
As the agents’ mixture universes with priors 𝑤𝑖 satisfy the grain-of-truth property, we have that for
each 𝜖 > 0, there exists a finite time 𝑡 ( 𝜖) for which the mixture universe is 𝜖-close to the ground-truth
distribution (cf. Theorem 3.11). Hence, the agents converge to the 𝜖-subjective embedded equilibrium
of mutual cooperation.
On the flip side, we can show that when the prior belief in functional similarity is too weak, i.e.,
𝑚defect
∞

, then the embedded Bayesian agents always defect, which is also an 𝜖-subjective embedded equilibrium. Hence, the choice of prior (through 𝛼) is an important variable determining
the equilibrium behavior of the embedded Bayesian agents. When taking an Occam’s razor prior
following the minimum description length line of thought, this would motivate a large 𝛼, as universes
containing two identical agents have roughly half the description length of a universe containing
two different agents of similar complexity, and hence result in cooperative behavior among identical
embedded Bayesian agents.
𝛼≤

1+𝑚defect
∞

♦
We now consider the exact, non-𝜖 version of the subjective embedded equilibrium (SEE) that characterizes the asymptotic limit of play, but we first must address a technical challenge. Agents’ policies
may be deterministic. If an agent’s subjective model 𝜌𝑖 converges to reflect this deterministic policy
in the limit of time to infinity, it will assign zero probability to certain actions, violating the grainof-uncertainty assumption. This is problematic because the embedded best response calculation
requires well-defined conditionals 𝜌𝑖 ( 𝑎− 𝑖 | 𝑎¯1:𝑡 , 𝑎𝑖 ) for all actions 𝑎𝑖 , including those that will have zero
probability according to the resulting embedded best response policy. To resolve this, we introduce the
concept of a conditional completion of a predictive model, which defines these necessary counterfactual
beliefs as the limit of a sequence of models that do satisfy the grain-of-uncertainty property. Note
31 In the considered setting both agents have an identical and deterministic ground-truth policy, hence we have that

𝑎1𝑡 = 𝑎2𝑡 for all timesteps 𝑡 . Hence the definition of 𝑚 (¯
𝑎1:𝑡 ) is invariant on whether we assume the policies are used by agent

1 or agent 2.

38

that while this section is about the repeated games with perfect-monitoring setting, the following
definition is stated in the more general MAGRL setting, for later reuse.
Definition 4.14 (Conditional Completion). A conditional completion of a measure 𝜆 (æ1:𝑡 ) consists of
∗
the measure 𝜆 (æ1:𝑡 ) itself, along with a set of conditionals 𝜆 ( 𝑒 | æ<𝑡 , 𝑎) for all æ<𝑡 ∈ AE , 𝑎 ∈ A, and
𝑒 ∈ E, derived as follows:
1. There exists a sequence of measures { 𝜆 𝑟 (æ1:𝑡 )}𝑟 ∈ℕ , each satisfying the grain-of-uncertainty
property, that converges to 𝜆 , i.e., lim𝑟→∞ 𝜆 𝑟 (æ1:𝑡 ) = 𝜆 (æ1:𝑡 ).
2. The completed conditionals are defined by the limit:32 𝜆 ( 𝑒 | æ<𝑡 , 𝑎) := lim𝑟→∞ 𝜆 𝑟 ( 𝑒 | æ<𝑡 , 𝑎).
In repeated games with perfect monitoring, where 𝑒𝑖 = 𝑎− 𝑖 , the conditional completion specifies an
agent’s beliefs about what its opponents would do in response to a counterfactual action, even if the
agent assigns zero probability to taking that action itself. This allows us to formally define the SEE.
Definition 4.15 (Subjective Embedded Equilibrium). A set of policies {𝜋𝑖 } 𝑖 ∈ 𝑁 and subjective predictive
distributions { 𝜌𝑖 } 𝑖 ∈ 𝑁 , each with a specified conditional completion, constitutes a subjective embedded
equilibrium if:
1. Subjective Best Response. Each agent’s policy 𝜋𝑖 is an embedded best response with respect to
𝜌𝑖 and its completion.
2. Uncontradicted Beliefs. The agent’s predictive distributions 𝜌𝑖 (æ𝑖<𝑡 ) are identical to the ground 𝜋𝑖
truth personal distribution 𝜇 𝑖 (æ𝑖<𝑡 ) induced by the multi-agent environment 𝜇 and policies
of all agents.
The SEE concept can rationalize behaviors unattainable under classical Nash equilibria, for example
cooperation in the twin prisoner’s dilemma, as detailed below.
Example 4.16 (Cooperation in the Twin Prisoner’s Dilemma). Consider two embedded agents playing
a single-round Prisoner’s Dilemma with actions 𝐶 and 𝐷, indicating ‘cooperating’ and ‘defecting’
respectively. Let their subjective models 𝜌𝑖 be the limit of a sequence 𝜌𝑟𝑖 where 𝜌𝑟𝑖 (C, C) = 1 − 𝜖𝑟
and 𝜌𝑟𝑖 (D, D) = 𝜖𝑟 , with 𝜖𝑟 → 0. Such an agent believes "I cooperate if and only if my opponent
cooperates." Given this belief, cooperation is the rational best response. Since both agents cooperate,
their belief that mutual cooperation occurs with probability 1 is not contradicted by reality. Thus,
mutual cooperation is a subjective embedded equilibrium.
♦
Let us revisit Example 4.13, and consider the tail game of length one of a single round of the
prisoner’s dilemma after timestep 𝑡 . Example 4.13 showed that for large enough 𝛼, both agents end
𝑖
up cooperating forever after some finite time 𝑇 . Hence, the tail policies 𝜋æ
𝑖 of both agents converge
<𝑡

to pure cooperation, and their predictive models converge to the ground-truth distribution. As a
consequence, in the limit of time to infinity, the agents not only converge to an 𝜖-SEE, but also to the
SEE covered in Example 4.16.
The subjective Nash equilibrium is a special case of the SEE: when an agent’s beliefs are decoupled,
an SEE is also a subjective Nash equilibrium.
Proposition 4.17. If a set of policies {𝜋𝑖 } 𝑖 ∈ [ 𝑁 ] and subjective models { 𝜌𝑖 } 𝑖 ∈ [ 𝑁 ] form a subjective embedded
Î
equilibrium where the completed conditionals are decoupled, i.e., 𝜌𝑖 ( 𝑎− 𝑖 | 𝑎¯1:𝑡 , 𝑎𝑖 ) = 𝑗≠𝑖 𝜌𝑖 ( 𝑎 𝑗 | 𝑎¯1:𝑡 ),
then this also constitutes a subjective Nash equilibrium. Consequently, there exists a Nash equilibrium
that induces the same distribution over histories.
32We assume the series { 𝜆 (æ )}
𝑟
1:𝑡 𝑟 ∈ℕ is suitably chosen such that this limit exists.

39

Proof. See Appendix C.3

□

The above result also holds for the 𝜖-variants (cf. Appendix C.3).
This proposition leads to an important corollary: When embedded agents are endowed with decoupled
beliefs, they are behaviorally equivalent to decoupled Bayes-optimal agents (cf. Proposition 3.17) and
hence their long-term behavior recovers the classical results of Kalai and Lehrer (cf. Theorem 4.6).
This serves as a crucial sanity check, demonstrating that our framework correctly subsumes the
decoupled case.
Corollary 4.18 (Convergence of embedded Bayes-optimal agents with decoupled beliefs to 𝜖-Nash).
Consider an infinitely repeated game with perfect monitoring, and embedded Bayes-optimal agents
Î
𝑗
starting from decoupled prior beliefs 𝑤 ( 𝜆 ), i.e., there exists a probability measure 𝑤
˜ 𝑖 ∈ Δ ( 𝑗 Mpol
) such
that for all 𝜆 ∈ Muni it holds that


Ö
∑︁
𝑖
𝑤
˜ 𝑖 ( 𝜋) 𝛿 𝜆 = ( 𝜈𝑖 ) 𝜋 , and 𝑤
𝑤
˜ 𝑖 (𝜋 𝑗 ) .
𝑤𝑖 ( 𝜆 ) =
˜ 𝑖 ( 𝜋) =
𝜋∈

Î

𝑗
𝑗 M pol

𝑗∈ 𝑁

with 𝛿 ( 𝜆 = ( 𝜈𝑖 ) 𝜋 ) the indicator function specifying whether 𝜆 is equal to the personal universe ( 𝜈𝑖 ) 𝜋
of agent 𝑖 originating from marginalizing the joint universe 𝜈¯𝜋¯ induced by 𝜋. If their beliefs satisfy
the grain-of-truth and grain-of-uncertainty properties, the agents converge to playing an 𝜖-subjective
embedded equilibrium which, by Proposition 4.17, is also an 𝜖-subjective Nash equilibrium.
𝑖

𝑖

Kalai and Lehrer (1993b, Theorem 1) shows equivalence between 𝜖-subjective Nash and 𝜖-Nash equilibria.
Therefore, for any 𝜖 > 0, their exists a time 𝑇 ( 𝜖) such that for all 𝑡 ≥ 𝑇 ( 𝜖), with 𝜇 𝜋 -probability greater
than 1 − 𝜖 over æ<𝑡 , the trajectory distribution 𝜇¯𝜋æ induced by the tail policies of the agents are 𝜖-close to
<𝑡
an 𝜖-Nash equilibrium in the tail game starting from time 𝑡 .
Proof. See Appendix C.4

□

4.2.2. Common knowledge solution concepts
In the preceding section, we developed the subjective embedded equilibrium to characterize the
convergence behavior of embedded agents as optimal with respect to their internal, subjective beliefs
about the world, which can differ from the subjective beliefs of other agents. In this section, we
develop the embedded equilibrium, a common knowledge solution concept that assesses whether this
converged behavior is optimal with respect to the ground-truth environment, the actual policies of
the other agents, and a commonly agreed upon method for evaluating counterfactual behaviors.
Evaluating counterfactuals of what would happen when the focal agent changes its behavior requires
making assumptions. In classical game theory, the assumption is that of decoupledness: the policies
of other agents remain unaltered. In the embedded agency setup, such a decoupledness assumption
can be inaccurate, as the agents’ policies can be functionally related.
Instead of defaulting to the decoupled assumption for evaluating counterfactuals, we explicitly encode
allowed of
the possible functional relations between agents and the environment. We define a set Muni
Î 𝑖 Î 𝑖 ∗
allowable multi-agent universes 𝜆¯ : ( 𝑖 A × 𝑖 E ) → [0, 1] that satisfy specific functional relations
imposed by nature (e.g., genetic kinship) or an external designer (e.g., a self-play constraint). Agents
maintain common knowledge of the multi-agent environment 𝜇¯, each other’s policies 𝜋
¯, the set
allowed
allowed
Muni , and an externally provided prior probability distribution 𝑞 ∈ ΔMuni
(where 𝑞 ( 𝜆¯) > 0 for
allowed
all 𝜆¯ ∈ Muni ).
40

This dependency distribution quantifies the likelihood of allowable universes, enabling agents to
uniquely and consistently evaluate counterfactual deviations. The dependency distribution 𝑞 ( 𝜆¯)
Î
Î
induces a joint mixture universe 𝑞 : ( 𝑖 A 𝑖 × 𝑖 E 𝑖 ) ∗ → [0, 1], defined as
∑︁
¯) 𝜆¯ (æ∗ ) ,
𝑞( 𝜆
(18)
𝑞 (æ∗ ) :=
¯ ∈ M allowed
𝜆
uni
allowed and prior 𝑞 are such that the resulting mixture universe 𝑞 (æ ) is fully
We assume that Muni
∗
Î
Î
supported on all æ∗ ∈ ( 𝑖 A 𝑖 × 𝑖 E 𝑖 ) ∗

Counterfactual measure. We derive a counterfactual measure to quantify the expected responses of
other agents and the environment when agent 𝑖 contemplates an action off the play-path. Instead of
assuming that the ego-policy 𝜋𝑖 can be unilaterally changed without altering the rest of the universe,
we use conditionals 𝑞 ( 𝑒𝑖 | æ∗𝑖 , 𝑎𝑖 ) originating from the externally provided dependency distribution
¯) whenever the ground-truth universe conditionals 𝜇¯𝜋¯ ( 𝑒𝑖 | æ∗𝑖 , 𝑎𝑖 ) are undefined (i.e., whenever
𝑞( 𝜆
𝜋
¯
𝜇
¯ (æ∗𝑖 , 𝑎𝑖 ) = 0).
Let the ground-truth personal universe for agent 𝑖 be 𝜐𝑖 . This is obtained from 𝜇¯𝜋¯ (æ∗ ) by marginalizing
out the histories (æ∗𝑗 ) 𝑗≠𝑖 of the other agents. The conditional completion 𝑝 ( 𝜐𝑖 , 𝑞) of 𝜐𝑖 by 𝑞 can now be
constructed as the limit of a sequence ( 𝑝𝑟 )𝑟 :
𝑝𝑟 := (1 − 𝜖𝑟 ) 𝜐𝑖 + 𝜖𝑟 𝑞,

with lim 𝜖𝑟 = 0 ,
𝑟 →∞

(19)

leading in the limit of 𝑟 → ∞ to the following completed conditionals:
𝑝 ( 𝜐𝑖 , 𝑞) ( 𝑒𝑖 | æ∗𝑖 , 𝑎𝑖 ) := 𝜐𝑖 ( 𝑒𝑖 | æ∗𝑖 , 𝑎𝑖 )

if 𝜐𝑖 (æ∗𝑖 , 𝑎𝑖 ) > 0 ,

(20)

𝑝 ( 𝜐𝑖 , 𝑞) ( 𝑒𝑖 | æ∗𝑖 , 𝑎𝑖 ) := 𝑞 ( 𝑒𝑖 | æ∗𝑖 , 𝑎𝑖 )

otherwise.

(21)

This conditional completion mathematically clarifies the reasoning of an agent in an embedded
setting: when contemplating a deviation to an action with zero probability under its current policy,
the agent deduces that this action implies the world must be governed by a different universe than
the ground-truth 𝜐𝑖 . It therefore utilizes the dependency distribution 𝑞—which reflects the underlying
functional relations of the system—to evaluate the counterfactual consequences of its deviation.
We define the embedded equilibrium as a mutual best response against this counterfactual measure.
Definition 4.19 (Embedded Equilibrium). A set of policies ( 𝜋𝑖 ) 𝑖𝑁=1 constitutes an embedded equilibrium for the multi-agent environment 𝜇¯ and prior probability 𝑞 over the set of allowable universes
allowed , if and only if (i) 𝜇 𝜋 ∈ M allowed and (ii) for each agent 𝑖, its policy 𝜋𝑖 is an embedded best
Muni
uni
response with respect to the conditional completion 𝑝 ( 𝜐𝑖 , 𝑞).
Example 4.20 (Mutual cooperation is an embedded equilibrium in single-shot PD). If we look closely
at Example 4.16, we can see that the subjective models 𝜌𝑖 are the limits of the conditionals of the same
distribution 𝑝𝑟 with 𝑝𝑟 (C, C) = 1 − 𝜖𝑟 and 𝑝𝑟 (D, D) = 𝜖𝑟 , where 𝜖𝑟 → 0. Furthermore, the conditionals of
𝑝𝑟 in the limit of 𝑟 → ∞ are a conditional completion of the ground-truth action distribution 𝜐 ( 𝐶, 𝐶 ) = 1.
Therefore, the resulting subjective embedded equilibrium is also an embedded equilibrium.
♦
Remark 4.21 (Comparison to Correlated Equilibrium). It is crucial to distinguish the embedded
equilibrium from the correlated equilibrium (cf. Definition 4.7). In a correlated equilibrium, agents
condition their actions on private messages 𝑚𝑖 from a common device. While this creates statistical
correlation, the reasoning remains decoupled. An agent contemplating a deviation from the recommended action does not believe its deviation will alter the other agents’ policies, as their actions are
41

conditioned on their own private messages. In an embedded equilibrium, when contemplating an
action 𝑎𝑖 with zero probability under the current policy, the dependency distribution 𝑞 takes possible
functional dependencies among agent’s policies into account. Hence, the considered policy of the
other agents can change for different actions 𝑎𝑖 , reflecting the functional dependencies. This is what
enables equilibria like cooperation in the Twin Prisoner’s Dilemma, which is inaccessible to correlated
equilibria.
Every embedded equilibrium is, by definition, also a subjective one. This is because we can set each
agent’s subjective model 𝜌𝑖 in the SEE definition (Definition 4.15) to be identical to the ground-truth
personal universe 𝜐𝑖 with its conditional completion derived from the dependency distribution 𝑞, as
specified in the EE definition (Definition 4.19). Since the EE already requires 𝜋𝑖 to be a best response
to this completed 𝜐𝑖 and the beliefs are uncontradicted by construction, all conditions for an SEE are
met. The converse, however, is not true.
Proposition 4.22. Each embedded equilibrium is also a subjective embedded equilibrium. The converse
is not true; there exist subjective embedded equilibria for which there is no embedded equilibrium that
induces the same distribution over histories.
Proof. See Appendix C.5 for a proof by counterexample.

□

This marks a key difference from the decoupled case in repeated games. As reviewed in Section 4.1,
Kalai and Lehrer (1993b, Proposition 1) established an equivalence: every subjective Nash equilibrium
in a repeated game induces the same history distribution as some Nash equilibrium. For embedded
agents, this equivalence breaks down; the set of subjective equilibria (SEEs) is strictly larger than the
set of common knowledge equilibria (EEs).
It is easy to see that each Nash equilibrium is also an EE when we take as dependency distribution 𝑞
the decoupled personal environment 𝜇 𝑖 ( 𝑒𝑖 | æ𝑖<𝑡 , 𝑎𝑖 ), which in case of repeated games is equal to the
fixed policies of the other agents. The converse is not true, as shown by Example 4.20 where mutual
cooperation on the prisoner’s dilemma is an EE but not a Nash equilibrium.
In our review of the decoupled setting, we saw that Bayesian learners do not converge to an exact Nash
equilibrium in finite time, but rather to an 𝜖-subjective Nash equilibrium, which in turn corresponds
to an 𝜖-Nash equilibrium (Theorem 4.6). To provide an analogous convergence target for embedded
agents, we define an 𝜖-variant of the embedded equilibrium.
Definition 4.23 (𝜖-Embedded Equilibrium). A set of policies ( 𝜋𝑖 ) 𝑖𝑁=1 constitutes an 𝜖-embedded
equilibrium for the multi-agent environment 𝜇¯ and prior probability 𝑞 over the set of allowable
allowed , if and only if (i) 𝜇 𝜋 ∈ M allowed and (ii) for each agent 𝑖, its policy 𝜋𝑖 is an
universes Muni
uni
𝜖-embedded best response with respect to the conditional completion 𝑝 ( 𝜐𝑖 , 𝑞):
𝑉 𝑝 ( 𝜐𝑖 ,𝑞 ) 𝜋 ( 𝜀) ≥ max 𝑉 𝑝 ( 𝜐𝑖 ,𝑞 ) 𝜋 ( 𝜀) − 𝜖
𝜋

Note that, similar to the 𝜖-Nash equilibrium, the 𝜖 condition for an 𝜖-EE applies to the best response.
This contrasts with the 𝜖-SEE (Definition 4.11), where the 𝜖 condition applies to the accuracy of the
beliefs (i.e., beliefs are 𝜖-close to the truth), while the policy must be an exact best response to those
𝜖-close beliefs.
Theorem 4.24 (Convergence to 𝜖-Embedded Equilibrium). Let { 𝜌𝑖 } 𝑖 ∈ 𝑁 be Bayesian mixture universes
satisfying the grain-of-uncertainty and grain-of-truth conditions, and let {𝜋𝑖 } 𝑖 ∈ 𝑁 be the corresponding
42

embedded best response policies in an infinitely repeated game with perfect monitoring. If the mixtures
{ 𝜌𝑖 } 𝑖 ∈ 𝑁 of all the players are the same mixture, i.e., 𝜌𝑖 = 𝜌 𝑗 ∀𝑖, 𝑗 ∈ 𝑁 ,33 then, for each 𝜖 > 0, there exists
a finite time 𝑇 ( 𝜖) such that for all 𝑡 ≥ 𝑇 ( 𝜖), with 𝜇 𝜋 -probability greater than 1 − 𝜖 over 𝑎¯<𝑡 , the tail
distribution 𝜇¯𝜋𝑎¯¯<𝑡 induced by the tail policies 𝜋𝑖𝑎¯<𝑡 is 𝜖-close to the distribution induced by some policies
constituting an 𝜖-embedded equilibrium in the tail game starting at time 𝑡 .
Proof. See Appendix C.6

□

Example 4.25 (Convergence to a cooperative 𝜖-EE for the Twin Prisoner’s Dilemma). Since the
priors that are used in Example 4.13 are the same for both agents, Theorem 4.24 implies that
the convergence to mutual cooperation for sufficiently large 𝛼 can also be seen as convergence
to an 𝜖-embedded equilibrium. To elaborate, Example 4.13 showed that the agents’ tail policies
converge to mutual cooperation. As established in Example 4.16, mutual cooperation is an embedded
equilibrium for a dependency distribution 𝑞 that reflects the perfect functional similarity (e.g., the
limit of 𝑞𝑟 (C, C) = 1 − 𝜖𝑟 and 𝑞𝑟 (D, D) = 𝜖𝑟 ). Since an exact EE is also an 𝜖-EE for any 𝜖 > 0, the
converged behavior of the agents is indeed equivalent to an 𝜖-embedded equilibrium.
♦
4.3. Equilibrium behavior of embedded Bayesian agents in the MAGRL setup
We now broaden our analysis from the structured setting of repeated games to the more general and
realistic framework of multi-agent general reinforcement learning (MAGRL). This shift introduces
partial observability and unknown environment dynamics, which have significant consequences for
equilibrium behavior.
The solution concepts we introduced—the subjective embedded equilibrium (SEE) (Definition 4.15)
and embedded equilibrium (EE) (Definition 4.19), along with their 𝜖-variants—are directly applicable
to the MAGRL setting. The key difference is that the subjective mixture universes 𝜌𝑖 are now general
𝑖
models over personal histories æ1:
as defined in equation 8, rather than the more constrained models
𝑡
over joint action histories used in the repeated games definition (Definition 4.10).
This move to the general MAGRL setup creates an interesting convergence: the subjective Nash
equilibrium (SNE) and the subjective embedded equilibrium (SEE) become mathematically equivalent.
In the repeated games setting, SNE and SEE are distinct. The decoupled mixture environment
𝜉𝑖 for an SNE (Definition 4.2) was built on a model class enforcing the repeated game’s causal
structure, implying no causal link between an agent’s current action 𝑎𝑡𝑖 and other agents’ concurrent
actions 𝑎𝑡− 𝑖 . Thus, 𝜉𝑖 ( 𝑎− 𝑖 | 𝑎¯<𝑡 , 𝑎𝑖 ) = 𝜉𝑖 ( 𝑎− 𝑖 | 𝑎¯<𝑡 ). The embedded mixture universe 𝜌𝑖 for an SEE
(Definition 4.10), however, allowed for coupled beliefs, creating an informational link. This meant
𝜌𝑖 ( 𝑎 − 𝑖 | 𝑎
¯<𝑡 , 𝑎𝑖 ) ≠ 𝜌𝑖 ( 𝑎− 𝑖 | 𝑎¯<𝑡 ) was possible, enabling equilibria like cooperation in the Twin Prisoner’s
Dilemma.
In the MAGRL setting, the model class for a decoupled agent’s mixture environment 𝜉𝑖 is no longer
restricted. It can now include environments 𝜈 where an agent’s action 𝑎𝑡𝑖 has a causal influence on
the percept 𝑒𝑡𝑖 (which could include information about 𝑎𝑡− 𝑖 ). Therefore, a decoupled agent can have
a mixture environment with 𝜉𝑖 ( 𝑒𝑖 | æ𝑖<𝑡 , 𝑎𝑖 ) ≠ 𝜉𝑖 ( 𝑒𝑖 | æ𝑖<𝑡 ). An embedded agent’s mixture universe
𝜌𝑖 can model this same dependency, either as a causal link within its universe hypotheses or as an
informational link via coupled beliefs. Since both decoupled (SNE) and embedded (SEE) agents can
now model a dependency of the percept 𝑒𝑖 on the action 𝑎𝑖 , the set of possible equilibria they can
converge to is mathematically identical. A philosophical distinction remains: an SNE rationalizes this
33 Note that due to perfect monitoring, the mixture universes of all agents are defined over sequences of joint actions, and

hence use the same set Ā ∗ over histories.

43

dependency as a purely causal feature of the environment, whereas an SEE can rationalize it as either
a causal link or an informational one arising from functional similarities.
The following example demonstrates this equivalence, showing that a decoupled Bayesian agent in a
MAGRL setting can converge to a cooperative SNE, similar to the embedded counterpart discussed in
Example 4.13, but does so by forming a belief in a causally incorrect environment compared to the
ground-truth repeated game structure.
Example 4.26 (Convergence to a Cooperative 𝜖-SNE). To illustrate that in the MAGRL setup, the 𝜖-SEE
and 𝜖-subjective Nash equilibrium are mathematically equivalent, we revisit Example 4.13 on the
iterated prisoner’s dilemma with discount 𝛾 = 0, but now convert it to a MAGRL setting with percepts
equal to the action of the other agent and resulting reward: 𝑒𝑖 = ( 𝑎− 𝑖 , 𝑟 𝑖 ). Now consider decoupled
𝑖
Bayesian agents maintaining a mixture environment 𝜉𝑖 ( 𝑒𝑖 | æ1:
, 𝑎𝑖 ). Leveraging the policy class Mpol
𝑡
and corresponding prior 𝑤
˜ introduced in Example 4.13, we construct the environment model class
Menv and corresponding prior as follows. We take Menv := Mpol ∪ {𝜈copy }, where environments 𝜈
coming from Mpol are the opponent’s policy combined with the ground-truth reward function, i.e.,
𝑖
𝑖
𝜈 ( 𝑒𝑖 | æ1:
, 𝑎𝑖 ) := 𝜋 ( 𝑎 − 𝑖 | æ1:
) 𝛿 ( 𝑟 𝑖 = 𝑟 ( 𝑎𝑖 , 𝑎− 𝑖 )) 34 where we remind the reader that 𝑒𝑖 = ( 𝑎− 𝑖 , 𝑟 𝑖 ), and
𝑡
𝑡
where 𝜈copy is the environment that copies the action 𝑎𝑖 combined with the ground-truth reward
𝑖
function, i.e., 𝜈copy ( 𝑒𝑖 | æ1:
, 𝑎𝑖 ) := 𝛿 ( 𝑎 − 𝑖 = 𝑎𝑖 ) 𝛿 ( 𝑟 𝑖 = 𝑟 ( 𝑎𝑖 , 𝑎 − 𝑖 )). Now we construct the prior 𝑤 ( 𝜈) as
𝑡
follows:
(
(1 − 𝛼) 𝑤
˜ ( 𝜈) if 𝜈 ∈ Mpol ,
𝑤 ( 𝜈) :=
𝛼
if 𝜈 = 𝜈copy ,
where we use shorthand 𝑤
˜ ( 𝜈) for 𝑤
˜ ( 𝜋) with 𝜋 the opponent’s policy modeled by 𝜈. Similar to
Example 4.13, we define:
𝑖
𝑚 (æ1:
𝑡 ) :=

∑︁
𝜋 ∈ Mpol

𝑤
˜ ( 𝜋)

𝑡
Ö

𝜋 ( 𝑎𝑖𝑘 | æ𝑖<𝑘 )

𝑘=1

𝑚defect
= lim 𝑚 (( 𝐷, 𝐷) 𝑘 ) .
∞
𝑘→∞

𝑚defect

The decoupled Bayesian agents are guaranteed to converge to a cooperative 𝜖-SNE when 𝛼 > ∞defect
1+𝑚∞
(through a similar derivation as for Example 4.13, see Appendix D.5 for more details). Similarly,
the decoupled Bayesian agents are guaranteed to converge to an 𝜖-SNE of mutual defection when
𝛼<

𝑚defect
∞

1+𝑚defect
∞

.

This illustrates the mathematical equivalence: the decoupled agent converges to cooperation, just as
the embedded agent did in Example 4.13. However, the reasoning is different. The embedded agent
converged by reasoning "my opponent is likely an identical copy, so my choice to cooperate is evidence
that they will too." The decoupled agent converges by reasoning "the environment is likely the ‘copy’
environment, so my choice to cooperate will cause my opponent to cooperate." This belief in the 𝜈copy
environment is, from an objective standpoint knowing the structure of the considered repeated game,
causally incorrect, as the opponent is a separate agent, not a feature of the environment. While in the
embedded setup, a large 𝛼 can be justified by Occam’s razor (a universe with two identical agents is
simpler), justifying a large 𝛼 for the ad-hoc 𝜈copy environment in the decoupled setup is more difficult.
♦
34 Note that the opponent’s policy 𝜋 ( 𝑎 − 𝑖 | æ𝑖 ) interprets the ego-agent’s history æ𝑖 from its own point of view, i.e., it
1:𝑡
1:𝑡
will use the percepts 𝑒𝑖 to derive its own actions 𝑎− 𝑖 , and use 𝑎𝑖 to create its own percepts 𝑒− 𝑖 .

44

While SNE and SEE become mathematically equivalent in the MAGRL setting, the common knowledge
solution concepts—Nash equilibrium (NE) and embedded equilibrium (EE)—remain distinct. A Nash
equilibrium (Definition 4.4) requires a best response against the ground-truth personal environment
𝜇 𝑖 , adhering to the ground-truth causal structure of the environment. An EE (Definition 4.19) allows
for a best response against a personal universe 𝜐𝑖 whose counterfactuals are defined by a dependency
distribution 𝑞, explicitly accounting for functional dependencies. Thus, cooperation in the Twin
Prisoner’s Dilemma is an EE but never a Nash equilibrium, even when the prisoner’s dilemma is
modeled in the MAGRL setting.
We now turn to the convergence behavior of embedded Bayesian agents in the MAGRL setup. As
discussed in Section 4.1, partial observability means that agents’ tail policies are conditioned on their
personal histories æ𝑖<𝑡 , which are private but correlated. This correlation is captured by a correlation
device, leading us to correlated equilibrium concepts. We therefore introduce the subjective correlated
embedded equilibrium (SCEE).
Definition 4.27 (𝜖-Subjective Correlated Embedded Equilibrium). A set of policies ( 𝜋𝑖 ) 𝑖𝑁=1 with
𝑖
𝜋𝑖 : 𝑀 𝑖 × (AE 𝑖 ) ∗ → Δ A 𝑖 and subjective mixture universes ( 𝜌𝑖 (æ1:
| 𝑚𝑖 )) 𝑖𝑁=1 is an 𝜖-subjective correlated
𝑡
embedded equilibrium w.r.t. the multi-agent environment 𝜇¯ and correlation device ( 𝑀, 𝑝) if the
following two conditions hold:
1. Subjective Best Response. Each agent’s policy 𝜋𝑖 is an embedded best response (cf. equation 10)
w.r.t. its subjective mixture universe 𝜌𝑖 for each history and message 𝑚𝑖 with 𝑝 ( 𝑚𝑖 ) > 0.
2. 𝜖-Uncontradicted Beliefs. With probability greater than 1 − 𝜖, a message 𝑚
¯ is sampled such
𝑖
𝑖
that for each agent 𝑖, its subjective beliefs 𝜌𝑖 (æ1:
|
𝑚
)
are
𝜖
-close
in
total
variation
distance to
𝑡
𝑖 𝜋𝑖
𝑖
𝑖
the ground-truth personal universe ( 𝜇 ) (æ1:𝑡 | 𝑚 ).
The exact (non-𝜖) subjective correlated embedded equilibrium is obtained by setting 𝜖 = 0, requiring
uncontradicted beliefs for all messages 𝑚𝑖 with 𝑝 ( 𝑚𝑖 ) > 0. Just as decoupled Bayesian agents converge
to an 𝜖-SCE (Theorem 4.6), embedded Bayesian agents satisfying the grain-of-truth property converge
to an 𝜖-SCEE.
Theorem 4.28 (Convergence to 𝜖-Subjective Correlated Embedded Equilibrium). Let 𝜋𝑖 be the policies
of embedded Bayes-optimal agents in a multi-agent environment 𝜇¯, using Bayesian mixture universes 𝜌𝑖
that satisfy the grain-of-truth and grain-of-uncertainty properties. It holds that for each 𝜖 > 0, there
exists a finite time 𝑇 ( 𝜖) such that for all 𝑡 ≥ 𝑇 ( 𝜖), the tail policies 𝜋æ𝑖 𝑖 and tail posterior beliefs 𝜌æ𝑖 𝑖
<𝑡

<𝑡

constitute an 𝜖-correlated subjective embedded equilibrium in the correlated tail game starting at time 𝑡
𝑡 −1
with correlation device (AE , 𝜇¯𝜋¯ ).
Proof. See Appendix C.7.

□

A final, critical point is that the link between subjective and common knowledge equilibria, which
was already weaker for embedded agents in the repeated games setting (Proposition 4.22), breaks
down almost entirely in the general MAGRL setup. The reason, as noted in Section 4.1 for decoupled
agents, is the introduction of uncertainty about the reward function itself (which is part of the percept
𝑒𝑖 ), as well as partial observability. The "uncontradicted beliefs" condition only constrains beliefs on
the play-path, leaving off-path conditionals—especially those concerning rewards—unconstrained by
evidence. This opens the door to "dogmatic beliefs": an agent might believe that any deviation from
its current policy will result in catastrophic reward, making its suboptimal policy a best response
to its own flawed subjective model (Leike and Hutter, 2015b). Since the agent never deviates, this
45

inaccurate belief is never corrected. This leads to the following triviality result, which holds for both
SEEs and SNEs due to their equivalence in the MAGRL setting.
Proposition 4.29. For any ground-truth multi-agent environment 𝜇¯ and any set of deterministic policies
( 𝜋𝑖 ) 𝑖𝑁=1 , there exists a set of mixture universes ( 𝜌𝑖 ) 𝑖𝑁=1 with corresponding conditional completions such
that their combination is a subjective embedded equilibrium.
Similarly, for any ground-truth multi-agent environment 𝜇¯ and any set of deterministic policies ( 𝜋𝑖 ) 𝑖𝑁=1 ,
there exists a set of mixture environments ( 𝜉𝑖 ) 𝑖𝑁=1 such that their combination is a subjective Nash
equilibrium.
Proof. See Appendix C.8.

□

This triviality result underscores a fundamental challenge for any Bayesian agent in a complex
environment: rational learning, even under the grain-of-truth assumption, is not sufficient to guarantee
convergence to an objectively optimal equilibrium. It highlights the necessity of robust exploration
to test and correct flawed off-path beliefs. Bayesian agents with sufficiently broad priors naturally
incorporate a form of principled exploration through the value of information (Chalkiadakis and
Boutilier, 2003; Howard, 1966), where an agent is intrinsically motivated to take actions that reduce
uncertainty about the world if that information is expected to improve future rewards. However, as
prior work has shown, this passive form of exploration is often insufficient to overcome dogmatic
beliefs about catastrophic outcomes (Leike and Hutter, 2015b; Orseau, 2010b). This has motivated
the use of more active exploration strategies, such as Thompson sampling (Leike et al., 2016a).
Translating and adapting these approaches to the coupled belief structures of embedded agents
presents a promising avenue for future research.
4.4. Embedded Bayesian agents with finite planning horizons
The previous results considered embedded Bayes-optimal agents that perform infinite-horizon planning. We end this section by investigating the 𝑘-step planner embedded Bayesian agents introduced
in Section 3.4. Catt et al. (2023) showed that Self-AIXI, which does 1-step ahead optimal planning,
converges to an infinite-horizon optimal planner under additional assumptions on the mixture environment. The intuition of why 1-step planning with terminal values converges to infinite-horizon
planning is the following: Initially, the policy implements 1-step optimal planning; when the selfmodel 𝜌 ( 𝑎 | æ1:𝑡 ) distills this 1-step planning during learning (i.e., Bayesian belief updates), the
terminal value 𝑉𝜌 (æ1:𝑡 ) represents a 1-step planning policy. Hence, adding 1-step planning to that
results in an effective 2-step planning policy. This process can be recursively applied to extend the
planning horizon further. In the following, we adapt their approach to our embedded Bayesian agent
setup with 𝑘-step planning, and investigate the consequences for multi-agent learning.
Since 𝑘-step planning is not a perfect approximation of the infinite-horizon optimal planning for any
finite time, we need to consider 𝛿-best responses. Hence, we extend the 𝜖-SCEE solution concept to
include 𝛿-best responses, allowing us to characterize the convergence behavior of embedded Bayesian
agents implementing 𝑘-step planning.
Definition 4.30 (( 𝜖, 𝛿)-Subjective Correlated Embedded Equilibrium (( 𝜖, 𝛿)-SCEE)). A set of policies
𝑖
( 𝜋𝑖 ) 𝑖𝑁=1 with 𝜋𝑖 : 𝑀 𝑖 × (AE 𝑖 ) ∗ → Δ A 𝑖 and subjective mixture universes ( 𝜌𝑖 (æ1:
| 𝑚𝑖 )) 𝑖𝑁=1 is an 𝜖-subjective
𝑡
correlated embedded equilibrium w.r.t. the multi-agent environment 𝜇¯ and correlation device ( 𝑀, 𝑝) if
the following two conditions hold:

46

1. Subjective 𝛿-Best Response. Each agent’s policy 𝜋𝑖 is an embedded 𝛿-best response w.r.t. its
subjective mixture universe 𝜌𝑖 for each history and message 𝑚𝑖 with 𝑝 ( 𝑚𝑖 ) > 0:
𝑖
𝑖
∗
𝑖
𝑖
𝑉 ( 𝜌𝑖 ) 𝜋𝑖 (æ1:
𝑡 , 𝑚 ) ≥ 𝑉𝜌𝑖 (æ1:𝑡 , 𝑚 ) − 𝛿 .

¯ is sampled such
2. 𝜖-Uncontradicted Beliefs. With probability greater than 1 − 𝜖, a message 𝑚
𝑖
𝑖
that for each agent 𝑖, its subjective beliefs 𝜌𝑖 (æ1:
|
𝑚
)
are
𝜖
-close
in
total
variation
distance to
𝑡
𝑖 𝜋𝑖
𝑖
𝑖
the ground-truth personal universe ( 𝜇 ) (æ1:𝑡 | 𝑚 ).
Building upon Catt et al. (2023), the following theorem shows that under additional assumptions
on Muni and 𝜌𝑖 , a group of 𝑘-step planner embedded Bayesian agents converge to ( 𝜖, 𝛿)-subjective
correlated equilibria.
Theorem 4.31. Let 𝜋𝑖 be the policies of embedded Bayesian agents in a multi-agent environment 𝜇 ,
𝑖
implementing 𝑘-step planning (Definition 3.9) w.r.t. Bayesian mixture universes 𝜌𝑖 (æ1:
) that satisfy the
𝑡
𝑖
𝑖
grain-of-truth and grain-of-uncertainty conditions, as well as the conditions that 𝜌 dominates ( 𝜌𝑖 ) 𝜋 and
𝑖
𝑖
( 𝜌𝑖 ) 𝜋 dominates the personal history distribution ( 𝜇 𝑖 ) 𝜋 , and the following sensibly off-policy condition:
There exists a positive 𝛼 < 1/𝛾 − 1 and 𝑡0 such that for all 𝑡 ≥ 𝑡0 , it holds that
"
#
∑︁
𝑖
𝑖
∗
𝑖
𝑖 𝑖
𝑖
𝑖 𝑖
𝔼 ( 𝜌𝑖 ) 𝜋𝑖 (æ𝑖 ) max
𝜌𝑖 ( 𝑒𝑖 | æ1:
𝑡 𝑎 ) [𝑉𝜌𝑖 (æ1:𝑡 𝑎 𝑒 ) − 𝑉𝜌𝑖 (æ1:𝑡 𝑎 𝑒 )]
1:𝑡

𝑎𝑖

𝑒𝑖

i
h
𝑖
𝑖 𝑖
𝑖
𝑖 𝑖
≤ (1 + 𝛼)𝔼 ( 𝜌𝑖 ) 𝜋𝑖 (æ𝑖 𝑎𝑖 𝑒𝑖 ) 𝑉𝜌∗𝑖 (æ1:
𝑎
𝑒
)
−
𝑉
𝑎
𝑒
)
.
𝑖 (æ
𝜌
𝑡
1:𝑡
1:𝑡

Then it holds that for each 𝛿 > 0 and 𝜖 > 0, the 𝜇 𝜋¯ -probability over æ<𝑡 that the tail Bayesian mixture
universes 𝜌æ𝑖 𝑖 and tail policies 𝜋æ𝑖 𝑖 are an ( 𝜖, 𝛿)-SCEE in the correlated tail game starting at timestep 𝑡
<𝑡

<𝑡

with correlation device (AE

𝑡 −1

, 𝜇 𝜋¯ ) converges to 1 as 𝑡 → ∞.

Proof. See Appendix C.9

□

The sensibly off-policy condition states that the expected optimality gap—defined as the difference
between the optimal value 𝑉𝜌∗𝑖 and the self-model value 𝑉𝜌𝑖 —does not become significantly worse
when taking an arbitrary off-policy action, compared to sampling from the self-model (Catt et al.,
2023). It remains an open problem in the literature to prove that this condition is satisfied for certain
model classes and corresponding mixture models. In fact, in Section 5.3 we show that for Solomonoff
mixture models, this condition is not satisfied.
When embedded Bayesian agents explicitly increase their 𝑘-step planning horizon over time, we can
show convergence to the ( 𝜖, 𝛿)-SCEE while avoiding the need for the sensibly off-policy condition.
Furthermore, in Section 5, we will consider embedded Bayesian agents that can only approximate
the relevant value functions up to a small constant 𝜖𝑡 . Let us combine both properties in the following
agent definition.
Definition 4.32 (( 𝑘𝑡 , 𝜖𝑡 )-embedded Bayesian agent). Let 𝑡 ↦→ 𝑘𝑡 be a mapping representing a possibly
variable planning horizon (which can vary from timestep to timestep), and let 𝑡 ↦→ 𝜖𝑡 be a possibly
variable level of accuracy of the approximate optimizer, where 𝜖𝑡 ∈ [0, 1) for all 𝑡 . A ( 𝑘𝑡 , 𝜖𝑡 )-approximate
embedded Bayesian agent with respect to mixture universe model 𝜌 is a policy 𝜋 which at time 𝑡
returns an action 𝑎𝑡 satisfying
𝜋 ( 𝑎𝑡 |æ<𝑡 ) > 0

⇒

𝑄 𝜌𝑡 (æ<𝑡 , 𝑎𝑡 ) ≥ max
𝑄 𝜌𝑡 (æ<𝑡 , 𝑎′ ) − 𝜖𝑡 .
′
𝑘

𝑘

𝑎 ∈A

47

The following proposition shows that approximate embedded Bayesian agents with growing planning
horizons and improving accuracy converge to ( 𝜖, 𝛿)-Subjective Correlated Embedded Equilibrium.
Proposition 4.33. Let 𝜋𝑖 be the policies of embedded ( 𝑘𝑡𝑖 , 𝜖𝑡𝑖 )-approximate Bayes-optimal agents in a
multi-agent environment 𝜇 , using Bayesian mixture universes 𝜌𝑖 that satisfy the grain-of-truth and
grain-of-uncertainty properties. If lim𝑡→∞ 𝑘𝑡𝑖 = ∞ and lim𝑡→∞ 𝜖𝑡𝑖 = 0 for all 𝑖, it holds that for each 𝜖 > 0
and 𝛿 > 0, there exists a finite time 𝑇 ( 𝜖, 𝛿) such that for all 𝑡 ≥ 𝑇 ( 𝜖, 𝛿), with 𝜇 𝜋 -probability greater than
1 − 𝜖 over æ<𝑡 , the agents’ tail policies 𝜋æ𝑖 𝑖 and tail mixture universes 𝜌æ𝑖 𝑖 constitute an ( 𝜖, 𝛿)-SCEE in
<𝑡

<𝑡

the correlated tail game starting from time 𝑡 with correlation device ((AE) 𝑡 −1 , 𝜇 𝜋¯ ).
Proof. See Appendix C.10

□

5. Embedded Universal Predictive Intelligence
In this section we formally introduce our theory for EMbedded Universal Predictive Intelligence
(MUPI). In Section 3, we introduced embedded Bayesian agents using arbitrary hypothesis classes
and mixture universes and showed that they can reason taking functional similarities into account. In
Section 4 we then showed that such embedded Bayesian agents converge to new types of solution
concepts, assuming that they satisfy the grain-of-truth property. Apart from a few toy examples (e.g.,
Example 4.13), we have not shown that the grain-of-truth property can be satisfied in cases where
embedded Bayesian agents consider a large and interesting class of universes, such as the class of
all computable universes. MUPI introduces an explicit model of a universally intelligent embedded
Bayesian agent that reason over a hypothesis class including all computable universes while satisfying
the grain-of-truth property, leading to consistent self prediction and mutual prediction among multiple
MUPI agents. By leveraging algorithmic information theory and algorithmic probability theory, MUPI
further formalizes embedded agency and functional similarities, while providing new tools to reason
about mutual prediction and infinite-order theory of mind.
Following Hutter’s Universal Artificial Intelligence framework (Hutter, 2000), we treat policies, (multiagent-)environments and universes as programs. When using a monotone Turing machine 𝑀 to
describe a universe 𝜆 𝑀 : AE ∗ ∪ (AE ∗ × A) → [0, 1], the countable set of all monotone Turing
LSCSM of all lower semicomputable semimeasures.
machines leads to a countable hypothesis class Muni
LSCSM combined with a lower
Unfortunately, an embedded Bayesian agent using the hypothesis class Muni
semicomputable universal prior is itself not lower semicomputable, for the same reasons that AIXI,
LSCSM is itself not lower semicomputable (Leike and Hutter, 2015c;
the Bayes-optimal agent over Menv
Sterkenburg, 2019). Hence, universes that contain one or more embedded Bayesian agents over
LSCSM are not within the hypothesis class M LSCSM , and consequently the grain-of-truth property
Muni
uni
is not satisfied, hindering the embedded Bayesian agents in making accurate predictions about the
universe they live in. Building upon the framework of reflective oracles (Fallenstein et al., 2015a,b;
Leike et al., 2016b), we aim to address the general grain-of-truth problem for embedded agency defined
below.
Problem 5.1 (The general grain-of-truth problem for embedded agency - Informal). Find a class of
universes Muni that
1. contains all computable universes;
2. contains all universes that result from combining one or more embedded Bayesian agents (cf.
Sections 3.3–3.4) that use a lower semicomputable universal prior over Muni with a computable
(multi-agent) environment.
48

Furthermore, we do not want the considered class of universes to be too large: Any further enlargement
beyond the class of all computable universes is considered a downside. Therefore, we should only
include incomputable universes to the extent that they are necessary to help achieving the second
goal. In other words, we do not want to consider universes that are "too incomputable".35
In Appendices F and G we unpack the above problem in more detail, specifying how policies and (multiagent) environments can be algorithmically combined to create universes, how embedded Bayesian
agents fit into this picture and the requirements this imposes on Muni . As universes containing
LSCSM are themselves not in M LSCSM , it indicates that the class of
embedded Bayesian agents over Muni
uni
lower semicomputable semimeasures is not large enough. Hence, we need to add some countable
class of non-lower-semicomputable semimeasures to Muni . A classical approach in computer science
to investigate non-computable objects is to provide Turing machines query access to an oracle which
is allowed to be incomputable, with a famous example being the Halting oracle answering queries of
the form ‘Does machine 𝑇 halt on input 𝑥 ?’. We follow this approach to solve the above grain-of-truth
problem in two different ways, each using a different type of oracle.
Previously, Fallenstein et al. (2015a,b) and Leike et al. (2016b) leveraged the reflective oracle
framework to solve the grain-of-truth problem for decoupled Bayesian agents. In Section 5.2, we
RO solving the
extend their approach to the embedded Bayesian agent setting, to obtain a class Muni
above grain-of-truth problem. Reflective oracles answer queries of the form ⟨𝑇, 𝑥, 𝑝⟩ corresponding to
“Is the probability that oracle machine 𝑇 𝑂 outputs 1 when given input sequence 𝑥 greater than 𝑝?". As we
will see later, a conceptual drawback of the Reflective Oracle framework is that when oracle machine
𝑇 𝑂 does not halt on input 𝑥 , the reflective oracle is allowed to redistribute this non-halting probability
arbitrarily to outputs 0 or 1. Hence, when using reflective oracles to create a universal mixture,
non-halting oracle machines contribute arbitrary output probabilities to the mixture.36 This is in
contrast to Solomonoff induction (cf. Sec. 2), where non-halting probability mass does not contribute
to the mixture.
In Section 5.1, we propose a new type of oracle to solve the grain-of-truth problem: the Reflective
RUI . This RUI oracle answers queries of
Universal Inductor (RUI) oracle, resulting in the model class Muni
the form ⟨ 𝑥, 𝑏, 𝑝⟩ corresponding to “Is the probability 𝜌 ( 𝑏 | 𝑥 ) greater than 𝑝?" with 𝜌 a universal mixture
distribution over oracle machines with access to the RUI oracle itself. Hence, we call 𝜌 the reflective
universal inductor (RUI). In contrast to reflective oracles, the RUI excludes non-halting probability
mass from its mixture distribution, and hence is not allowed to arbitrarily redistribute it to the valid
outputs 0 and 1. This makes the RUI closer in spirit to Solomonoff induction compared to the universal
inductors using reflective oracles. Conceptually, the RUI 𝜌 corresponds to the prediction model used
by embedded Bayesian agents, making it easily relatable to practical machine learning settings where
such prediction models are learned instead of obtained via universal Bayesian induction. Our reflective
universal inductor framework makes the recursions arising from self or mutual prediction explicit: 𝜌
makes predictions about predictive entities using 𝜌 itself. However, these benefits of the RUI-oracle
come at a cost: (i) as the RUI uses a specific universal prior, all Bayesian agents using the RUI-oracle
use the same prior. In contrast, the reflective oracle framework allows different Bayesian agents to use
different priors. (ii) Bayesian agents using RUI oracles are only allowed to make a bounded number
of oracle calls for each executed action. While this still allows for infinite computations, it makes
optimal infinite-horizon planning impossible. Thus, we can only formalize 𝑘-step optimal planning
35We can formalize this by saying that the considered universes should ideally remain within a relatively low level of the
arithmetic hierarchy (Odifreddi, 1989).
36 This, however, is not a significant drawback for using the reflective universal mixture as a predictor if we only care about
computable environments (or more generally, environments where the oracle machine does not loop forever): Despite the
addition of arbitrary terms coming from the contribution of (possibly) non-halting machines, the convergence to accurate
prediction of Theorem 3.11, as well as the prediction loss bound of Theorem 3.18, are still correct.

49

AIXI (decoupled agency)

e1

work

e2

e3

Agent π

tape

a2

a3

a1

MUPI (embedded agency)

...

RUI ρ

work

Environment ν

...

tape

work

Universe λ
(Agent + Env.)

a1

e1

a2

e2

tape

...

Figure 5.1 | Comparison of Decoupled Agency (AIXI) and Embedded Agency (MUPI). For AIXI (left),
the agent 𝜋 and the environment 𝜈 are decoupled programs, interacting via percepts (𝑒𝑡 ) and actions (𝑎𝑡 ) on
separate tapes, with the percept tape acting as the output tape for the environment and the input tape for the
agent, and vice versa for the action tape. In contrast, in MUPI (right), the agent and environment are unified
into a joint universe 𝜆 , with access to a reflective universal inductor (RUI) 𝜌, generating interleaved actions 𝑎𝑡
and observations 𝑒𝑡 on a single output tape.

Bayesian agents (cf. 3.4) within the RUI-oracle framework, whereas the reflective oracle framework
allows for infinite-horizon optimal planning. We stress that the RUI-oracle framework should be seen
as an alternative framework to reflective oracles, providing some conceptual benefits but not without
introducing other drawbacks. We leave it to future work to combine the benefits of both approaches.
RUI and M RO , and
In Section 5.3 we introduce various embedded AIXI agents over the model classes Muni
uni
show that they solve the grain-of-truth problem described in Problem 5.1. Fig. 5.1 shows the difference
between such embedded AIXI agents and the classical decoupled AIXI agents. In Appendix G we delve
deeper into the theory and formalize a few desiderata that a good theory of embedded universal
intelligence should satisfy, and show that our formalism satisfies these desiderata.

Finally, in Section 5.4, we revisit the functional similarities introduced in Section 3.6 through the
lens of algorithmic information theory, formalizing the intuition of functional similarities as the joint
‘compressibility’ of agent and environment. Furthermore, we show that the Solomonoff universal
prior, which incorporates the algorithmic complexity of the considered universes, is always coupled
and contains universes with arbitrarily high degrees of functional similarities.
5.1. The reflective universal inductor
This section introduces the Reflective Universal Inductor (RUI), a new theoretical framework for
constructing a general hypothesis class of universes that satisfies the grain-of-truth property for
embedded Bayesian agents using a mixture universe. To allow for a general yet parsimonious
description, we model everything using binary strings (𝑥 ∈ B ∗ , where B = {0, 1}) and machines that
output bits. By using complete prefix-free encodings for the action set A and percept set E, these
binary strings can be unambiguously interpreted as the action-percept histories of an agent.
Definition 5.2 (prefix free encoding). Let X be an arbitrary countable set. We say that a mapping
𝑐 : X → B ∗ is a prefix-free encoding of X if no codeword is a prefix of any other codeword, i.e., for
every 𝑥, 𝑥 ′ ∈ X with 𝑥 ≠ 𝑥 ′ , we have that 𝑐 ( 𝑥 ) is not a prefix of 𝑐 ( 𝑥 ′ ).
We say that the prefix-free encoding 𝑐 is complete if for every infinite binary string 𝑠 ∈ B ∞ , there is
50

one (and only one) element 𝑥 ∈ X such that 𝑐 ( 𝑥 ) is a substring 𝑠1:𝑘 of 𝑠 for some 𝑘 > 1.
Our construction proceeds in several steps. First, we formalize the notion of programs that can access
non-computable information. We begin by defining Abstract Probabilistic Oracle Machines (APOMs),
which are Turing machines 𝑀 equipped to query an unspecified oracle. This allows us to define a
countable class M of such machines. We then define a Probabilistic Oracle Machine (POM) 𝑀 𝜏 as an
APOM, 𝑀 , paired with a specific probabilistic oracle, 𝜏. The output distribution of a POM 𝑀 𝜏 , denoted
𝜆 𝜏𝑀 , is a semimeasure over binary strings and represents a concrete “universe” in our framework, an
instance of the universes 𝜆 discussed in Sections 3 and 4.
The goal is to model an embedded Bayesian agent whose predictive model is a universal Bayesian
𝜏
mixture, 𝜌𝑤
𝜏 , over the class of all possible universes, { 𝜆 𝑀 } 𝑀 ∈ M , using prior beliefs 𝑤. For this setup to
satisfy the grain-of-truth property, a universe containing such an agent must itself be implementable
by one of these POMs, 𝑀 𝜏 . This implies that the program 𝑀 must be able to simulate the agent’s
reasoning, which requires access to the universal Bayesian mixture, 𝜌𝑤
𝜏 . We solve this by designing
the oracle 𝜏 to provide precisely this access: It will answer queries about the predictive distribution
𝜌𝑤
𝜏.
This creates a crucial self-referential or “reflective” loop. The oracle 𝜏 is defined in terms of the universal
mixture 𝜌𝑤
𝜏 , but this mixture is itself an average over all POMs, whose behaviors are determined by
𝜏. The oracle’s definition thus depends on a system of which it is a fundamental component. The
existence of such a self-consistent fixed point is not guaranteed. The main contribution of this section
is to formally define and prove the existence of this RUI-oracle. This construction yields a hypothesis
𝑤,𝜏 −RUI
class, Muni
, that solves the general grain-of-truth problem (cf. Problem 5.1), ensuring that the
agent’s predictions converge to the ground truth and thereby providing a solid foundation for the
MUPI framework.
5.1.1. Probabilistic oracle machines and universes.
We define probabilistic oracles, abstract probabilistic oracle machines and their combination, probabilistic oracle machines.
Definition 5.3 (Probabilistic oracle). A probabilistic oracle is a stochastic function 𝑂𝜏 parameterized
by a probability map 𝜏 : {0, 1}∗ → [0, 1] as follows:37 For each 𝑥 ∈ B ∗ , 𝑂𝜏 ( 𝑥 ) is a Bernoulli random
bit satisfying ℙ[𝑂𝜏 ( 𝑥 ) = 1] = 𝜏 ( 𝑥 ). We do not impose any computability assumption on the mapping
𝜏.
We can interpret 𝑂𝜏 as a probabilistic oracle that can be queried with a finite binary string 𝑥 and
which can return a probabilistic binary answer 𝑂𝜏 ( 𝑥 ). We may sometimes abuse the terminology and
also refer to 𝜏 as the probabilistic oracle even though strictly speaking it is a deterministic function
(but nevertheless describes the probabilistic behavior of a stochastic function).
Definition 5.4 (APOM). An abstract probabilistic oracle machine (APOM) is a monotone Turing
machine equipped with (i) an extra unidirectional binary read/write tape that we call the oracle tape,
initialized with zeros, and a special instruction corresponding to querying the oracle; and (ii) an extra
unidirectional binary read-only tape that we call the randomness tape, initialized with uniformly
independent random bits, and a special instruction corresponding to reading a random bit from the
randomness tape. We write M APOM to denote the class of all APOMs.
37 The interval [0, 1] denotes the interval of real numbers between 0 and 1 including the boundaries. We explicitly use

the notation ℚ ∩ [0, 1] to indicate the interval of rational numbers between 0 and 1 when needed.

51

Abstract probabilistic oracle machines do not specify what the machine does when an oracle-querying
instruction is executed. The execution procedure of an APOM is well-defined (and it is similar to a
monotone Turing machine) until an oracle-querying instruction is made, after which the behavior is
not specified by definition of the APOM. To fully specify the execution procedure, we need to equip
the abstract probabilistic oracle machine with a probabilistic oracle 𝜏.
Definition 5.5 (POM). A probabilistic oracle machine (POM) is a pair ( 𝑀, 𝜏) of an abstract probabilistic
oracle machine 𝑀 and a probabilistic oracle 𝜏. We denote such a POM as 𝑀 𝜏 . The execution procedure
of 𝑀 𝜏 can be described as follows:
• For all instructions other than oracle-querying instructions, the execution proceeds identically
to probabilistic Turing machines leveraging the randomness tape to access random bits.
• If an oracle-querying instruction is encountered:
– We take the finite binary string to the left of the oracle tape’s head and call it 𝑥 .
– We query the oracle and get a random bit 𝑏 := 𝑂𝜏 ( 𝑥 ) with ℙ[𝑂𝜏 ( 𝑥 ) = 1] = 𝜏 ( 𝑥 ).
– We replace the entire oracle tape with zeros, except for the first bit which we replace with
the oracle’s response 𝑏.
– The oracle tape’s head is returned to the tape’s first position, which means that we can
subsequently access the oracle’s response by reading the bit at the oracle tape’s head.
All oracle responses are assumed to be independent.
For technical reasons to later construct our RUI-oracle, we need to define a restricted APOM (rAPOM)
and restricted POM (rPOM) that constrain the amount of oracle calls the machine can make for each
output bit.
Definition 5.6 (rAPOM). A restricted abstract probabilistic oracle machine (rAPOM) is an abstract
probabilistic oracle machine with the following computational constraints:
1. The execution of the abstract probabilistic oracle machine 𝑀 can be described as a (potentially
infinite) sequence of stages where at the 𝑖-th stage the machine writes one bit on the output
tape.
2. For technical reasons which will become clear later38 , we require that each stage must consist
of three consecutive phases:
(i) Phase 1: The machine computes a number 𝑁𝑖 without making any queries to the oracle.
(ii) Phase 2: The machine performs a computation in which it is allowed to make at most 𝑁𝑖
queries to the oracle.
(iii) Phase 3: The machine appends the output tape with a bit.
We require that the above structure is explicitly enforced so that we can computably certify it from
a canonical binary representation ⟨ 𝑀 ⟩ of 𝑀 . This is needed so that we can define a canonical
enumeration 𝑀1 , . . . of restricted abstract probabilistic oracle machines. We write M rAPOM to denote
the class of all rAPOMs.
38We will need this assumption in the proof of Theorem 5.16 in Appendix C.12.

52

Definition 5.7 (rPOM). A restricted probabilistic oracle machine is a pair ( 𝑀, 𝜏) of an rAPOM 𝑀
together with a probabilistic oracle 𝜏 : {0, 1}∗ → [0, 1]. We refer to such an rPOM as a 𝜏-rPOM to
emphasize that it uses the 𝜏-oracle.
To obtain universe semimeasures 𝜆 over sequences, we use 𝜏-rPOMs without input tape.39 Running
such an rPOM 𝑀 𝜏 gives rise to a semimeasure 𝜆 𝜏𝑀 : B ∗ → [0, 1] describing the state of the output tape
of 𝑀 𝜏 as it runs. More precisely, for every ℎ ∈ B ∗ , 𝜆 𝜏𝑀 ( ℎ) represents the probability that the POM 𝑀 𝜏
executes at least 𝑙 ( ℎ) stages and ℎ is found to the left of the output tape’s head at the end of the 𝑙 ( ℎ)-th
stage. Using prefix-free encodings of actions in A and percepts in E, such binary sequences can be
interpreted as action-percept histories. Hence, these semimeasures 𝜆 𝜏𝑀 are the direct counterpart
of the universes 𝜆 used in Sections 3 and 4, using semimeasures instead of measures, to allow for
universes that halt after outputting a finite sequence, or go into a non-halting loop without returning
any further output bits. We use the term ‘universe’ interchangeably for 𝑀 𝜏 or 𝜆 𝜏𝑀 , and rely on context
to distinguish between them.
Remark 5.8. By employing the same tools that are used to show the classical result in computability
theory that every Turing machine can be canonically encoded as a binary string, we can also show
that every APOM and rAPOM can be canonically encoded as a binary string. If 𝑀 is an rAPOM, we
write ⟨ 𝑀 ⟩ to denote its canonical representation as a binary string. We can also choose the canonical
representation of rAPOMs in such a way that the set {⟨ 𝑀 ⟩ ∈ {0, 1}∗ : 𝑀 is an rAPOM} is decidable
by a Turing machine.40 In the remainder of this paper, we assume that we have a fixed canonical
representation with these properties. Note that this allows for a canonical enumeration 𝑀1 , . . . of
rAPOMs.41
5.1.2. Universal mixtures over universes
Now we are ready to define universal mixtures over 𝜏-rPOMs, which give rise to powerful predictors:
Definition 5.9 (Universal mixture universe). Let 𝜏 : {0, 1}∗ → [0, 1] be a probabilistic oracle, and let
𝑤 ∈ Δ′ M rAPOM be a lower semicomputable42 universal prior semiprobability distribution over the set
M rAPOM of all rAPOMs. We define the ( 𝑤, 𝜏)-universal mixture as
∑︁
𝜌𝑤
:=
𝑤𝑀 𝜆 𝜏𝑀 .
𝜏
𝑀 ∈ M rAPOM

The ( 𝑤, 𝜏)-universal inductor43 is defined as the conditional semimeasure 𝜌𝑤
𝜏 (·|·) that arises from the
44
( 𝑤, 𝜏)-universal mixture:
′
𝜌𝑤
𝜏 ( ℎℎ )
′
, ∀ℎ, ℎ′ ∈ B ∗ .
𝜌𝑤
𝜏 ( ℎ | ℎ) =
𝑤
𝜌𝜏 ( ℎ)
An interesting choice of a prior is one that is analogous to Solomonoff ’s universal prior:
39 To avoid the need to introduce a new type of rAPOMs without input tape, we keep using rAPOMs as defined in

Definition 5.6, and initialize the input tape with zeros.
40 This boils down to programming a syntax-checker, which can be done by a Turing machine.
41We can let 𝑀 be the 𝑖-th rAPOM according to the ≺ order defined as: 𝑀 ≺ 𝑀 ′ if and only if 𝑙 (⟨ 𝑀 ⟩) < 𝑙 (⟨ 𝑀 ′ ⟩) or
𝑖
𝑙 (⟨ 𝑀 ⟩) = 𝑙 (⟨ 𝑀 ′ ⟩) and ⟨ 𝑀 ⟩ comes before ⟨ 𝑀 ′ ⟩ in lexicographic order.
42 This means that the mapping ⟨ 𝑀 ⟩ ↦→ 𝑤 is lower semicomputable, where ⟨ 𝑀 ⟩ is the canonical representation of the
𝑀
rAPOM 𝑀 as a binary string.
43We use the term inductor because 𝜌𝑤 (·|·) can be used to predict the future given the observations so far.
𝜏
44 The denominator 𝜌𝑤 ( ℎ) is always non-zero, as we have that 𝑤 > 0 for all 𝑀 ∈ M rAPOM , and for each finite history ℎ
𝑀
𝜏
there exists a program 𝑀 that deterministically prints ℎ on its output tape.

53

Definition 5.10 (Solomonoff universal prior). Let 𝑈 be a universal monotone Turing machine. We
define the Solomonoff universal prior over rAPOMs with respect to 𝑈 and the enumeration as
𝑤𝑀 = 2 − 𝐾𝑈 ( ⟨ 𝑀 ⟩ ) .

Í
It is worth noting that 𝑀 ∈ M rAPOM 2− 𝐾𝑈 ( ⟨ 𝑀 ⟩ ) ≤ 1, and hence 𝑀 ↦→ 2− 𝐾𝑈 ( ⟨ 𝑀 ⟩ ) indeed defines a prior
semiprobability distribution.45
In the remainder of this paper, we will assume that the canonical encoding ⟨ 𝑀 ⟩ of 𝑀 as a binary string,
as well as the universal monotone Turing machine 𝑈 are fixed, and hence we will simply refer to the
Solomonoff universal prior without further mention of these fixed choices. We emphasize however
that any concept that we will subsequently define using the Solomonoff prior potentially depends on
these choices.
The Solomonoff 𝜏-universal mixture is defined as
∑︁
𝜌𝜏 :=
2− 𝐾 ( ⟨ 𝑀 ⟩ ) 𝜆 𝜏𝑀 ,
𝑀 ∈ M rAPOM

The Solomonoff 𝜏-universal inductor is the conditional semimeasure 𝜌𝑤
𝜏 (·|·) that arises from the
Solomonoff 𝜏-universal mixture.
Since 𝜌𝜏 is a universal mixture, it follows from Corollary B.15, which extends the merging of opinions
Theorem 3.11 towards semimeasures, that 𝜌𝜏 asymptotically converges to making perfect predictions
in any 𝜏-universe, i.e., for any rAPOM 𝑀 , we have
lim 𝐷∞ ( 𝜌𝜏 , 𝜆 𝜏𝑀 | ℎ ≤ 𝑡 ) = 0 ,

𝑡 →∞

𝜆 𝜏𝑀 ( ℎ)-almost surely.

5.1.3. The reflective universal inductor oracle
Our goal is to model embedded Bayesian agents that use a mixture universe model over the class
of all 𝜏-universes, { 𝜆 𝜏𝑀 } 𝑀 ∈ M rAPOM . This means the agent’s predictive model is the ( 𝑤, 𝜏)-universal
′
′
rAPOM . Our main goal is to ensure that this
inductor, 𝜌𝑤
𝜏 ( ℎ | ℎ), for some universal prior 𝑤 ∈ Δ M
setup satisfies the grain-of-truth property. Specifically, the class of 𝜏-universes must be rich enough to
contain universes that themselves include embedded Bayesian agents using the universal inductor 𝜌𝑤
𝜏.
The rPOMs 𝑀 that define our universes have access to a probabilistic oracle 𝜏, which has not yet
been specified. The key idea is to design 𝜏 such that it provides query access to the predictions of the
𝜏
universal inductor 𝜌𝑤
𝜏 . This would allow us to formally describe universes 𝜆 𝑀 containing embedded
Bayesian agents that use 𝜌𝑤
𝜏 (by querying 𝜏), thereby satisfying the grain-of-truth condition.
This leads to a crucial self-referential challenge, which motivates the term “reflective”. The oracle 𝜏
must answer queries about the universal mixture 𝜌𝑤
𝜏 , which is itself a mixture over rPOMs that have
access to 𝜏. In essence, the oracle must have knowledge of a system of which it is an integral part. The
existence of such a self-consistent object is not guaranteed. Therefore, the main result of this section
is to formally define this special type of oracle and prove that it can, in fact, exist. It is worth noting
that reflective oracles Fallenstein et al. (2015a,b) also successfully overcome a similar self-referential
challenge, which we cover in more detail in Section 5.2.
Definition 5.11 (𝑤-reflective universal inductor oracle). Let 𝜏 : {0, 1}∗ → [0, 1] be a probabilistic
oracle, and let 𝑤 ∈ Δ′ M rAPOM be a lower semicomputable universal semiprobability prior over M rAPOM .
45 This follows from Kraft’s inequality and the fact that the set of self-delimiting programs of a universal monotone Turing

machine forms a prefix free set.

54

Let ( 𝑏, 𝑝, ℎ) ↦→ ⟨𝑏, 𝑝, ℎ⟩ be some canonical encoding of triplets ( 𝑏, 𝑝, ℎ) ∈ B × (ℚ ∩ [0, 1]) × B ∗ as
binary strings B ∗ .
We say that the probabilistic oracle 𝜏 is a 𝑤-reflective universal inductor oracle (𝑤-RUI oracle) with
respect to the encoding 𝑏, 𝑝, ℎ ↦→ ⟨𝑏, 𝑝, ℎ⟩ if for every 𝑥 ∈ B ∗ , we have (with 𝑥 = ⟨𝑏, 𝑝, ℎ⟩):46
(i) If 𝜌𝑤
𝜏 ( 𝑏 | ℎ) > 𝑝 then 𝜏 ( 𝑥 ) = 1.
(ii) If 𝜌𝑤
𝜏 ( 𝑏 | ℎ) < 𝑝 then 𝜏 ( 𝑥 ) = 0.
If 𝜏 is a 𝑤-RUI-oracle with respect to the encoding 𝑏, 𝑝, ℎ ↦→ ⟨𝑏, 𝑝, ℎ⟩, we say that 𝜌𝑤
𝜏 is a 𝑤-reflective
47
universal inductor (𝑤-RUI) with respect to the same encoding.
If 𝑤 corresponds to the Solomonoff prior, then we refer to 𝜏 and 𝜌𝜏 := 𝜌𝑤
𝜏 as the Solomonoff reflective
universal inductor oracle (Solomonoff RUI-oracle) and Solomonoff reflective universal inductor
(Solomonoff RUI), respectively.
Remark 5.12. The adjective "reflective" that is used to describe reflective universal inductors 𝜌𝑤
𝜏 comes
from the fact that it is a Bayesian mixture over the class of semimeasures induced by probabilistic
oracle machines having access to an oracle answering questions about 𝜌𝑤
𝜏 itself.
Remark 5.13. When a probabilistic oracle 𝜏 is a 𝑤-RUI-oracle, then one may interpret a query
request ⟨𝑏, 𝑝, ℎ⟩ to the oracle as asking the question: “Is 𝜌𝑤
𝜏 ( 𝑏 | ℎ) greater than 𝑝?”. The oracle returns a
𝑤
𝑤
deterministic answer if 𝜌𝜏 ( 𝑏 | ℎ) > 𝑝 or 𝜌𝜏 ( 𝑏 | ℎ) < 𝑝. However, when 𝜌𝑤
𝜏 ( 𝑏 | ℎ) = 𝑝, the oracle is allowed
to return a random answer. Nevertheless, the probability describing the random answer must be
consistent if we request the same ⟨𝑏, 𝑝, ℎ⟩ several times.48
Remark 5.14. As the oracle answer of the query ⟨𝑏, 𝑝, ℎ⟩ is random only when 𝜌𝑤
𝜏 ( 𝑏 | ℎ) = 𝑝, it is easy
to show that with a binary search procedure (cf. Appendix C.11), one can obtain an estimate of
𝑤
𝜌𝑤
𝜏 ( 𝑏 | ℎ) up to arbitrary precision despite the randomness of the oracle answer when 𝜌𝜏 ( 𝑏 | ℎ) = 𝑝, with
a bounded number of oracle requests depending on the desired precision.
′
′
∗
The following lemma extends this to 𝜌𝑤
𝜏 ( ℎ | ℎ) for ℎ, ℎ ∈ B :
′
Lemma 5.15. For every ℎ, ℎ′ ∈ B ∗ and every 𝜖 > 0, we can compute 𝜌𝑤
𝜏 ( ℎ | ℎ) up to 𝜖-precision using at
most 𝑁𝜖,ℎ′ queries to the oracle, where 𝑁𝜖,ℎ′ computably depends only on 𝜖 and 𝑙 ( ℎ′ ).

Proof. See Appendix C.11.

□

Reflective universal inductors exist:
Theorem 5.16. For every lower semicomputable universal prior 𝑤 ∈ Δ′ M rAPOM over M rAPOM , there
exists a 𝑤-RUI-oracle 𝜏 and a corresponding reflective universal inductor 𝜌𝑤
𝜏.
In particular, there exists a Solomonoff RUI-oracle 𝜏 and a corresponding Solomonoff reflective universal
inductor 𝜌𝜏 .
46 In this definition of the reflective universal inductor, we require that every 𝑥 ∈ B ∗ maps to a valid encoding ⟨𝑏, 𝑝, ℎ⟩,
which can be satisfied by taking a complete prefix-free encoding ⟨ 𝑝⟩ of the rational numbers ℚ ∩ [0, 1], and then taking
⟨𝑏, 𝑝, ℎ⟩ := 𝑏 ⟨ 𝑝⟩ ℎ.
47 In the remainder of this paper, and unless stated otherwise, we assume that we have a fixed canonical encoding
𝑏, 𝑝, ℎ ↦→ ⟨𝑏, 𝑝, ℎ⟩, and hence, for the sake of simplicity we will just write "𝑤-RUI-oracle" to mean "𝑤-RUI-oracle with respect
to the fixed canonical encoding".
48 Such consistency is actually expected from any general probabilistic oracle as described in Definition 5.3 and Definition 5.5. This is not unique to RUI-oracles.

55

Proof. See Appendix C.12.

□

Remark 5.17. For a fixed encoding ⟨𝑏, 𝑝, ℎ⟩ and a fixed universal prior 𝑤 ∈ Δ′ M rAPOM over M rAPOM ,
it is not clear whether a reflective universal inductor corresponding to this 𝑤 is unique, i.e., there
might exist multiple different reflective universal inductors compatible with 𝑤.
The set of all rPOMs with access to a 𝑤-reflective universal inductor oracle 𝜏 induces a hypothesis
class over universes:
𝑤,𝜏 −RUI
Muni
:= { 𝜆 𝜏𝑀 : 𝑀 ∈ M rAPOM } .
Reflective universal inductors are strong predictors in the sense that they almost surely converge to
𝑤,𝜏 −RUI
making accurate predictions in universes 𝜆 ∈ Muni
having access to the corresponding RUI-oracle:
Theorem 5.18. For every lower semicomputable universal prior 𝑤 ∈ Δ′ M rAPOM over the space of rAPOMs
M rAPOM , if 𝜏 is a 𝑤-RUI-oracle, then the corresponding RUI 𝜌𝑤
𝜏 satisfies:
𝑤,𝜏 −RUI
∀𝜆 ∈ Muni
, lim 𝐷∞ ( 𝜌𝑤
𝜏 , 𝜆 | ℎ<𝑡 ) = 0 ,
𝑡 →∞

𝜆 ( ℎ)-almost surely.

Proof. See Appendix B. The proof of the theorem is a direct application of Corollary B.15.

□

5.2. Universal induction with reflective oracles
In this section, we develop an alternative approach to our RUI framework for solving the general
grain-of-truth problem for embedded agency (Problem 5.1). We leverage the framework of reflective
oracles (ROs) (Fallenstein et al., 2015a,b; Leike et al., 2016b) to construct a universal hypothesis
𝜏-RO
class, Muni
, that contains universes with embedded Bayesian agents that use mixture models over
𝜏-RO
Muni for any lower-semicomputable prior. The concepts and theorems presented here are minimal
extensions of the foundational results from Fallenstein et al. (2015a,b), Leike et al. (2016b), and
Wyeth et al. (2025)—which focused primarily on decoupled agency—to our embedded agency setting.
The RO framework offers a different set of trade-offs compared to the RUI framework. A key advantage
of ROs is their generality; they do not impose constraints on the number of oracle calls a machine
can make. This allows us to use POMs instead of rPOMs, and formalize embedded Bayes-optimal
agents that perform infinite-horizon planning, in contrast to the approximate, 𝑘-step planning agents
necessitated by the RUI’s computational constraints (cf. Section 5.3). Furthermore, a single reflective
oracle can support the construction of universal inductors with different priors, accommodating
scenarios where agents with different priors interact. However, this generality comes at the cost of a
conceptual departure from classical Solomonoff induction. A reflective oracle arbitrarily redistributes
the probability mass of non-halting computations to the outputs 0 or 1, thereby influencing the mixture
distribution in an arbitrary way not related to the complexity of the considered POMs. This problem
is not present in the RUI framework, where none of the non-halting probability mass contributes to
the reflective universal inductor.
The two oracles also differ in the nature of their queries. A RUI oracle directly answers queries ⟨𝑏, 𝑝, ℎ⟩
about the predictive distribution of its own reflective universal inductor, e.g., "Is the probability 𝜌𝜏 ( 𝑏 | ℎ)
greater than 𝑝?". In contrast, a reflective oracle answers queries ⟨ 𝑀, 𝑝, ℎ⟩ about the behavior of an
arbitrary 𝜏-POM 𝑀 , e.g., "Is the probability that machine 𝑀 (with oracle access to 𝜏) outputs 1 greater
than 𝑝?". The universal inductor is not the oracle itself but must be constructed as a Bayesian mixture
over all 𝜏-POMs (with 𝜏 being the reflective oracle). The central goal of this section is to formally
define ROs, construct this universal inductor, and prove that the inductor is itself implementable by
a POM with access to the reflective oracle. In Section 5.3, in addition of constructing embedded
56

Bayesian agents using RUIs, we also construct embedded Bayesian agents using the RO-based universal
inductor, and show that both setups solve the general embedded grain-of-truth problem.
In the RUI framework, we modeled universes as rPOMs without an input tape that generate an entire
action-percept sequence. Here, we adopt a different approach common in the RO literature. We
consider 𝜏-POMs 𝑀 that take a history ℎ ∈ B ∗ as input and output a single bit 𝑏,49 thereby defining
a conditional probability 𝜆 𝜏𝑀 ( 𝑏 | ℎ). A full semimeasure over histories, 𝜆 𝜏𝑀 ( ℎ), is then constructed by
chaining these conditionals together:
𝜆 𝜏𝑀 ( ℎ) =

𝑙(
ℎ)
Ö

𝜆 𝜏𝑀 ( ℎ𝑖 | ℎ1:𝑖 −1 ) ,

𝑖=1

where we adopt the convention that ℎ1:0 = 𝜀.
A reflective oracle is formally defined as follows:
Definition 5.19 (Reflective oracle (Fallenstein et al., 2015a,b)). Let 𝜏 : {0, 1}∗ → [0, 1] be a
probabilistic oracle. Let ( 𝑀, 𝑝, ℎ) ↦→ ⟨ 𝑀, 𝑝, ℎ⟩ be some canonical encoding of triplets ( 𝑀, 𝑝, ℎ) ∈
M APOM × (ℚ ∩ [0, 1]) × B ∗ as binary strings B ∗ , with M APOM the countable set of all APOMs. Furthermore, for every 𝑀 ∈ M APOM , every ℎ ∈ B ∗ , and every bit 𝑏 ∈ B, let 𝜆 𝜏𝑀 ( 𝑏 | ℎ) be the probability that
POM 𝑀 𝜏 outputs 𝑏 on the first cell of its output tape when provided with input ℎ.
We say that the probabilistic oracle 𝜏 is a reflective oracle (RO) with respect to the encoding50
( 𝑀, 𝑝, ℎ) ↦→ ⟨ 𝑀, 𝑝, ℎ⟩ if for every pair ( 𝑀, ℎ) there exists some 𝑞 ∈ [0, 1] such that 𝜆 𝜏𝑀 (1| ℎ) ≤ 𝑞 ≤
1 − 𝜆 𝜏𝑀 (0| ℎ) and such that for all 𝑝 ∈ ℚ ∩ [0, 1], the following implications hold:
(i) If 𝑝 < 𝑞 then 𝜏 (⟨ 𝑀, 𝑝, ℎ⟩) = 1.
(ii) If 𝑝 > 𝑞 then 𝜏 (⟨ 𝑀, 𝑝, ℎ⟩) = 0.
Importantly, for queries with 𝑝 = 𝑞, the reflective oracle is allowed to randomize its answer, i.e., have
a Bernouilli probability 𝜏 (⟨ 𝑀, 𝑝, ℎ⟩) different from 0 or 1. This is important to avoid self-reference
paradoxes, as illustrated by the example below, adapted from Fallenstein et al. (2015b) and Leike
et al. (2016b).
Example 5.20 (Reflective oracles and self-reference). Consider a machine 𝑀 ∈ M APOM that can
access its own description (this is possible using Kleene’s second recursion theorem (Kleene, 1952))
and is designed to contradict its oracle. 𝑀 queries the oracle with ⟨ 𝑀, 𝜀, 1/2⟩—asking if its own
probability of outputting ‘1’ is greater than 1/2—and then outputs the opposite bit, 1 − 𝑂𝜏 (⟨ 𝑀, 𝜀, 1/2⟩).
Any deterministic response from the oracle creates a paradox. If the oracle answers ‘1’ (implying
𝜆 𝜏𝑀 (1| 𝜀) ≥ 1/2), the machine’s actual output becomes ‘0’, making 𝜆 𝜏𝑀 (1| 𝜀) = 0. This contradicts the
oracle’s premise. Conversely, if the oracle answers ‘0’ (implying 𝜆 𝜏𝑀 (1| 𝜀) ≤ 1/2), the machine’s output
becomes ‘1’, making 𝜆 𝜏𝑀 (1| 𝜀) = 1, which is also a contradiction. The only consistent resolution is for
the machine’s output probability to be exactly the queried threshold, 𝜆 𝜏𝑀 (1| 𝜀) = 1/2. This is only
possible if the oracle’s response is a random coin flip. Therefore, for this “liar” machine, any valid
reflective oracle must satisfy 𝜏 (⟨ 𝑀, 𝜀, 1/2⟩) = 1/2.
As shown by Fallenstein et al. (2015a,b), reflective oracles are guaranteed to exist.
49 For POMs that output multiple bits on their output tape, we simply ignore all output bits except the first one.

50 In the remainder of this paper, we assume a fixed such canonical encoding and refer to such 𝜏 simply as a "reflective

oracle".

57

Theorem 5.21 (Existence of a reflective oracle (Fallenstein et al., 2015a,b)). A reflective oracle exists.
A key property of a reflective oracle is that it allows for the "completion" of a semimeasure into a
full measure. For each 𝜏-POM 𝑀 and input ℎ, the reflective oracle redistributes any non-halting
probability mass by selecting the value 𝑞 in Definition 5.19 satisfying 𝜆 𝜏𝑀 (1| ℎ) ≤ 𝑞 ≤ 1 − 𝜆 𝜏𝑀 (0| ℎ). We
can then take 𝜆¯𝜏𝑀 (1| ℎ) := 𝑞 and 𝜆¯𝜏𝑀 (0| ℎ) := 1 − 𝑞 as the completion of 𝜆 into a full measure. This value
𝑞 can be found by performing a binary search over 𝑝 and repeatedly querying the reflective oracle
with queries ⟨ 𝑀, ℎ, 𝑝⟩. While this procedure can be stochastic (if a query is made with 𝑝 = 𝑞, the
reflective oracle is allowed to provide a randomized answer), it converges to the correct value in the
limit. This leads to the following definition:
Definition 5.22 (𝜏-completion). The 𝜏-completion of the output distribution 𝜆 𝜏𝑀 ( 𝑏 | ℎ) of a 𝜏-POM 𝑀
is given by 𝜆¯𝜏𝑀 (1| ℎ) := 𝑞 and 𝜆¯𝜏𝑀 (0| ℎ) := 1 − 𝑞, where 𝑞 ∈ ℝ is the value from Definition 5.19. We
Î (ℎ) 𝜏
¯ ( ℎ𝑖 | ℎ<𝑖 ), which induces a measure 𝜆¯𝜏 .
overload the notation 𝜆¯𝜏𝑀 ( ℎ) := 𝑙𝑖=1
𝜆
𝑀
𝑀
We can now define our hypothesis class over universes by chaining these completed conditional
measures. The hypothesis class is then:
𝜏-RO
Muni
:= { 𝜆¯𝜏𝑀 : 𝑀 ∈ M APOM } .
𝜏-RO
𝜏-RO
It is worth noting that if 𝜆 𝜏𝑀 is already a measure, then 𝜆 𝜏𝑀 = 𝜆¯𝜏𝑀 ∈ Muni
. Therefore, the class Muni
contains all computable universes.
𝜏-RO
We would like to construct a universal inductor over Muni
which is itself an element of this class. More
precisely, for some choice of an arbitrary lower semicomputable semiprobability prior 𝑤 ∈ Δ′ M APOM ,
𝑤
e.g., the Solomonoff prior 𝑤 ( 𝑀 ) = 2− 𝐾𝑈 ( ⟨ 𝑀 ⟩ ) , we would like to find an APOM 𝑀RO
such that51
∑︁
∑︁
¯𝜏 𝑤 ≥
¯𝜏𝑀 =
𝜆
𝑤
(
𝑀
)
𝜆
𝑤( 𝜆) 𝜆 ,
(22)
𝑀
RO

𝑀 ∈ M APOM

where

𝑤 ( 𝜆 ) :=

𝜏-RO
𝜆 ∈ Muni

∑︁

𝑤( 𝑀) .

¯𝜏 =𝜆
𝑀 :𝜆
𝑀

If such a machine exists, then the universal inductor defined as 𝜌¯𝑤
:= 𝜆¯𝜏𝑀 𝑤 would satisfy the
𝜏-RO
RO

following desired properties:
𝜏-RO
1. 𝜌¯𝑤
∈ Muni
, and
𝜏-RO

𝜏-RO
2. 𝜌¯𝑤
dominates every universe in Muni
, and hence from Theorem 3.11 we get that
𝜏-RO
𝜏-RO
∀𝜆 ∈ Muni
, lim 𝐷∞ ( 𝜌
¯𝑤
𝜏-RO , 𝜆 | ℎ<𝑡 ) = 0,
𝑡 →∞

𝜆 ( ℎ)-almost surely .

(23)

𝜏-RO
Furthermore, Theorem 3.18 implies that for every 𝜆 ∈ Muni
, we can bound the accumulated
prediction loss over trajectories of length 𝑛 in terms of the prior 𝑤 ( 𝜆 ) as follows52

𝐿𝑛 ( 𝜌
¯𝑤
𝜏-RO , 𝜆 ) ≤ − log 𝑤 ( 𝜆 ) < ∞ .

(24)

¯𝜏
¯𝜏
𝑀 ∈ M APOM 𝑤 ( 𝑀 ) 𝜆 𝑀 is not a measure. On the other hand, 𝜆 𝑀 𝑤 is a
RO
Í
𝜏
𝜏
measure, and hence, we can only aim for an inequality 𝜆¯ 𝑀 𝑤 ≥ 𝑀 ∈ M APOM 𝑤 ( 𝑀 ) 𝜆¯ 𝑀 .
RO
52 The inequality in equation 24 implies that the universal inductor’s 𝜌
¯𝑤
inductive bias is consistent with its prior 𝑤.
𝜏-RO
𝑤
51 Note that if 𝑤 in not a probability distribution, then Í

This consistency is the key motivation for constructing a machine 𝑀RO (satisfying equation 22) for an arbitrary lower
semicomputable (LSC) prior 𝑤. The primary objective is to enable an inductive bias consistent with the Solomonoff prior,
which is itself LSC but not computable. If our goal were merely to satisfy the merging property in equation 23, a simpler
𝑤
computable prior (e.g., 𝑤 ( 𝑀 ) = 3−⟨ 𝑀 ⟩ ) would suffice, making the construction of 𝑀RO
much easier.
58

For the case of the Solomonoff prior 𝑤 ( 𝜆¯) :=
𝐿𝑛 ( 𝜌
¯𝑤
𝜏-RO , 𝜆 ) ≤ − log

Í

∑︁

¯𝜏 =𝜆¯ 2
𝑀 :𝜆
𝑀

− 𝐾𝑈 ( ⟨ 𝑀 ⟩ ) , we get

2− 𝐾𝑈 ( ⟨ 𝑀 ⟩ ) ≤ min 𝐾𝑈 (⟨ 𝑀 ⟩) .
¯𝜏 =𝜆
𝑀 :𝜆
𝑀

¯𝜏 =𝜆
𝑀 :𝜆
𝑀

𝑤
The remainder of this section is dedicated to constructing a machine 𝑀RO
satisfying equation 22.
Similarly to Wyeth et al. (2025), we construct a machine that satisfies the following recursive equations

𝜆 𝜏𝑀 𝑤 ( 𝑏 | ℎ<𝑡 ) ≥
RO

∑︁

¯𝜏𝑀 ( 𝑏 | ℎ<𝑡 ) ,
𝑤 ( 𝑀 | ℎ<𝑡 ) 𝜆

𝑀 ∈ M APOM

𝑤 ( 𝑀 | ℎ1:𝑡 ) = 𝑤 ( 𝑀 | ℎ<𝑡 )

¯𝜏 ( ℎ𝑡 | ℎ<𝑡 )
𝜆
𝑀
¯𝜏 𝑤 ( ℎ𝑡 | ℎ<𝑡 )
𝜆
𝑀

,

(25)

RO

𝑤 ( 𝑀 | 𝜀) = 𝑤 ( 𝑀 ) .
𝑤
Appendix C.13 shows that indeed, if a machine 𝑀RO
satisfies equation 25, then it satisfies equation 22
as well, and hence equation 23 and equation 24 are also satisfied.
𝑤
To prove that such an APOM 𝑀RO
can indeed be implemented, we first need to introduce some notions
of computability relative to a probabilistic oracle. Note that in general, a 𝜏-POM has a probabilistic
output due to the stochasticity of 𝑂𝜏 and potentially the use of random coinflips. Hence, this needs to
be taken into account in the computability notions introduced below.

Definition 5.23 (𝜏-estimable (Wyeth et al., 2025)). A deterministic function 𝑓 : B ∗ → ℝ is 𝜏-estimable
if and only if there exists a 𝜏-POM 𝑀 that upon input ⟨𝑘, ℎ⟩ with ( 𝑘, ℎ) ∈ ℕ × B ∗ (stochastically)
outputs a binary string ⟨ 𝑦 ⟩ encoding a rational number 𝑦 ∈ ℚ and then halts, such that for all ⟨ 𝑦 ⟩
Í
with 𝜆 𝜏𝑀 (⟨ 𝑦 ⟩ | ⟨𝑘, ℎ⟩) > 0 and 𝜆 𝜏𝑀 (⟨ 𝑦 ⟩ | ⟨𝑘, ℎ⟩) > 𝑏 ∈ B 𝜆 𝜏𝑀 (⟨ 𝑦 ⟩ 𝑏 | ⟨𝑘, ℎ⟩) 53 we have that | 𝑦 − 𝑓 ( ℎ)| ≤ 1𝑘 .
Definition 5.24 (𝜏-lower-semicomputable). A deterministic function 𝑓 : B ∗ → ℝ is said to be 𝜏lower-semicomputable (𝜏-LSC) if and only if there exists a 𝜏-POM 𝑀 that upon input ℎ ∈ B ∗ with
𝜆 𝜏𝑀 -probability 1 outputs an infinite bit sequence (⟨𝑞𝑘 ⟩) 𝑘∞=1 of prefix-free encoded rational numbers
such that 𝑞𝑘 → 𝑓 ( ℎ) as 𝑘 → ∞ 𝜆 𝜏𝑀 -almost-surely, and 𝑞𝑘+1 ≥ 𝑞𝑘 for all 𝑘 with 𝜆 𝜏𝑀 -probability 1.
This specialized definition of 𝜏-LSC is needed to handle the stochasticity of the oracle. The standard
definition of lower semi-computability (cf. Definition 2.8) involves independent calls to a function
𝜙 ( 𝑥, 𝑘) for each step 𝑘, making it difficult to enforce the monotonicity condition 𝑞𝑘+1 ≥ 𝑞𝑘 when the
outputs are stochastic. By having a single 𝜏-POM stream the entire sequence, it can use its internal
state to ensure monotonicity despite the oracle’s randomness. A function 𝑓 is 𝜏-upper-semicomputable
(𝜏-USC) if − 𝑓 is 𝜏-LSC.
The binary search procedure used to find the 𝜏-completion of a machine’s output provides a sequence
of improving lower and upper bounds. This gives us a crucial property:
Theorem 5.25 (Estimable completions, Theorem 8 of Wyeth et al. (2025)). Every 𝜏-completion 𝜆¯𝜏𝑀 is
𝜏-estimable, 𝜏-LSC, and 𝜏-USC.
Finally, we define what it means for a conditional semimeasure to be implemented by a 𝜏-POM.
Definition 5.26 (𝜏-sampleable (Wyeth et al., 2025)). A conditional semimeasure 𝜎 : B ∗ → Δ′ B is
𝜏-sampleable if there exists a 𝜏-POM 𝑀 such that 𝜆 𝜏𝑀 ( 𝑏 | ℎ) = 𝜎 ( ℎ) ( 𝑏) for all 𝑏 ∈ B , ℎ ∈ B ∗ .
53When this strict inequality is satisfied, there is a non-zero probability of halting after outputting ⟨ 𝑦 ⟩.

59

A key link between these concepts is that 𝜏-lower-semicomputablity implies 𝜏-sampleability.
Lemma 5.27 (𝜏-LSC implies 𝜏-sampleable). A 𝜏-lower-semicomputable conditional semimeasure is also
𝜏-sampleable.
Proof. The proof is a minor variation on Li et al. (2008, Lemma 4.3.3) and Wyeth et al. (2025,
Theorem 6). See Appendix C.14.
□
With this machinery in place, we can now state and prove the main result of this section.
𝑤
Theorem 5.28. There exists an APOM 𝑀RO
satisfying equation 25.

Proof. The proof builds upon the work of Leike et al. (2016b) and Wyeth et al. (2025). See Appendix C.15.
□
𝜏-RO
This result confirms that the universal inductor over the class Muni
is itself an element of that class.
In the next section, we use this result to show that embedded Bayesian agents using 𝜌𝑤
solve the
𝜏-RO
general embedded grain-of-truth problem (cf. Problem 5.1).

5.3. Embedded AIXI agents
𝑤,𝜏 −RUI
In Section 5.1, we introduced RUI-oracles leading to a wide hypothesis class Muni
over universes
with access to RUI oracle 𝜏 using prior 𝑤, which includes all lower semicomputable semimeasures.
Similarly, in Section 5.2 we leveraged the reflective oracle framework (Fallenstein et al., 2015b) to
𝜏 −RO
construct a hypothesis class Muni
over probabilistic oracle machines with access to the reflective
oracle 𝜏, also including all lower semicomputable semimeasures. In this section, we address two
remaining questions: (i) how can we use universes that output bits to model (multi-agent) environments and policies, where different agents possibly have different percept and action spaces? (ii)
𝑤,𝜏 −RUI
𝜏 −RO
Are embedded Bayesian agents using hypothesis classes Muni
or Muni
included within the
hypothesis classes themselves, i.e., can we solve the general grain-of-truth problem for embedded
agency stated in Problem 5.1?

5.3.1. Modeling agent-environment interactions
The universes 𝜆 of Sections 3 and 4 described probabilities over action-percept sequences with action
space A and percept space E. In contrast, the universes 𝜆 𝜏𝑀 of Section 5.1 are semimeasures over
binary sequences. We can connect the two approaches by introducing a complete prefix-free encoding
𝑎 ↦→ ⟨𝑎⟩ of 𝑎 ∈ A as binary strings, and similarly for 𝑒 ∈ E. Using such an encoding, each binary
string can be translated to a sequence of actions and percepts54 and vice versa. Using 𝑥 := ⟨𝑎𝑡 ⟩ and
𝑦 := ⟨𝑒𝑡 ⟩, the conditional semimeasures over bitstrings can be translated to conditional semimeasures
over action-percept sequences as follows:
𝜆 ( 𝑎𝑡 | æ<𝑡 ) := 𝜆 ( 𝑥 | ⟨æ<𝑡 ⟩) =

𝑙 (𝑥 )
Ö

𝜆 𝜏𝑀 ( 𝑥 𝑖 | ⟨æ<𝑡 ⟩ 𝑥1:𝑖 −1 ) ,

𝑖=1

𝜆 ( 𝑒𝑡 | æ<𝑡 , 𝑎𝑡 ) := 𝜆 ( 𝑦 | ⟨æ<𝑡 𝑎𝑡 ⟩) =

𝑙( 𝑦)
Ö

(26)
𝜆 𝜏𝑀 ( 𝑦𝑖 | ⟨æ<𝑡 𝑎𝑡 ⟩ 𝑦1:𝑖 −1 ) ,

𝑖=1
54 By starting reading the bitstring from left to right, one can alternate between decoding an action and decoding a

percept. Possibly the bitstring does not contain a complete codeword for the last symbol (action or percept); in such cases,
we simply ignore the bits at the end of the bitstring that do not correspond to a complete codeword.
60

with ⟨æ<𝑡 ⟩ the binary string encoding of the history æ<𝑡 of actions and percepts, using the complete
Í
prefix-free encodings mentioned above. As 𝜆 𝜏𝑀 are semimeasures, it can be that 𝑎 𝜆 ( 𝑎 | æ<𝑡 ) < 1,
when the universe has a non-zero probability of halting or getting stuck in an infinite loop before
outputting an action encoding55 (and similarly for percepts). We can assign the missing probability
mass to a special token, representing that the universe, including the agent, ceases to exist (cf.
Appendix B). Note that the probabilities 𝜆 ( 𝑎𝑡 | æ<𝑡 ) and 𝜆 ( 𝑒𝑡 | æ<𝑡 , 𝑎𝑡 ), and as a result the predictions
and value estimations of the agent, depend on the chosen complete prefix-free encodings for A and
E.56
We can use a similar strategy for modeling multi-agent environments using binary sequences. Leveraging a complete prefix-free encoding of the joint action space Ā and joint percept space Ē, we can
interpret binary strings as multi-agent environment interactions (cf. Section 2.2). From the point
𝑖
of view of a specific agent, we can interpret binary sequences as personal histories æ1:
∈ AE 𝑖 ) ∗
𝑡
consisting of individual actions 𝑎𝑖 ∈ A 𝑖 and percepts 𝑒𝑖 ∈ E 𝑖 . Both the joint distribution 𝜈𝜋 , as well as
 𝜋𝑖
the personal distributions 𝜈𝑖 can then be represented as the semimeasures induced by universes,
using the strategy of equation 26.
Finally, let us briefly discuss how agent and environment programs can be merged together to form
𝑖
a universe. Assume that we can describe the policies 𝜋𝑖 ( 𝑎𝑖 | æ1:
) and multi-agent environment
𝑡
𝜏
𝜈 (¯
𝑒 | æ1:𝑡 𝑎
¯) as the semimeasures induced by 𝜏-POMs ( 𝑀𝜋𝑖 ) 𝑖 ∈ [ 𝑁 ] and 𝑀𝜈𝜏 over their outputs ⟨𝑎𝑖 ⟩ and ⟨¯
𝑒⟩
𝑖
respectively, with prefix-free encodings of æ1:
and
æ
𝑎
¯
on
their
respective
input
tapes.
Then,
we
1:𝑡
𝑡
can combine the machines ( 𝑀𝜋𝜏 𝑖 ) 𝑖 ∈ [ 𝑁 ] and 𝑀𝜈𝜏 into a single 𝜏-POM 𝑀 𝜏 that outputs binary encoded
sequences of 𝑎¯ and 𝑒¯, by alternately exchanging inputs and outputs between ( 𝑀𝜋𝜏 𝑖 ) 𝑖 ∈ [ 𝑁 ] and 𝑀𝜈𝜏
appropriately. Furthermore, if 𝑀 𝜏 satisfies the constraints on oracle calls mentioned in Definition 5.6,
𝑤,𝜏 −RUI
it is a universe within Muni
. Finally, we can convert 𝑀 𝜏 to personal universes 𝑀𝑖𝜏 for each
individual agent by mapping 𝑎¯ to 𝑎𝑖 and 𝑒¯ to 𝑒𝑖 . See Appendix F for a more detailed discussion on
how to represent multi-agent environments using universes.
5.3.2. Embedded AIXI agents
𝑤,𝜏 −RUI
𝜏 −RO
Using the hypothesis classes Muni
or Muni
with a corresponding lower semicomputable universal
prior 𝑤, we can use the following mixture universe models

𝜌RUI := 𝜌𝑤
𝜏 −RUI ,

𝜌RO := 𝜌
¯𝑤
𝜏 −RO

(27)

𝑤,𝜏 −RUI
with 𝜌𝑤
the universal mixture over Muni
, and 𝜌¯𝑤
the 𝜏-completed universal mixture over
𝜏 −RUI
𝜏 −RO
𝜏 −RO
RUI
Muni (cf. Definition 5.9). Now we can readily use 𝜌 and 𝜌RO to design various embedded Bayesian
agents following Sections 3.3–3.4, which we call Embedded AIXI agents, or E-AIXI in short. Embedded
AIXI agents can use either 𝜌RUI or 𝜌RO , with either infinite-horizon optimal planning (cf. Section 3.3),
or 𝑘-step planning (cf. Section 3.4); we use 𝑘-E-AIXI to indicate the number of planning steps, and
omit 𝑘 if infinite-horizon planning is used. When we need to distinguish between E-AIXI agents that
use 𝜌RUI or 𝜌RO , we use superscript E-AIXIRUI and E-AIXIRO respectively.

As a first set of main results, building upon the work of Fallenstein et al. (2015a) and Leike et al.
(2016b), we show that E-AIXI agents using reflective oracles satisfy the grain-of-truth problem,
𝜏 −RO
i.e., universes containing such E-AIXI agents are part of Muni
. As a direct consequence of this,
RO
multi-agent systems of E-AIXI agents converge to a subjective correlated embedded equilibrium.
55 As we are using complete prefix-free encodings, machines are guaranteed to output a valid action encoding, as long as
they do not halt or get stuck in an infinite loop prematurely.
56 In the remainder of this work, we assume a fixed choice of prefix-free encodings, and omit mentioning this dependence
on the encodings.

61

Theorem 5.29. For every complete prefix-free encoding of A and E, there exists an E-AIXIRO policy and
𝑘-E-AIXIRO policies for every 𝑘 ∈ ℕ, with respect to the reflective oracle 𝜏, which is implementable by a
POM 𝑀 𝜏 with access to the reflective oracle 𝜏, i.e., the POM 𝑀 𝜏 writes 𝑎𝑡 on the output tape when the
input tape contains a prefix-free encoding of æ<𝑡 .
Furthermore, when one or more such (𝑘-)E-AIXIRO agents are combined with a multi-agent environment 𝜇
that is implementable on a POM with access to reflective oracle 𝜏, then the resulting universe is part of
𝜏 −RO
Muni
.
Proof. Minor variation upon Leike et al. (2016b, Theorem 22) and Wyeth et al. (2025, Theorem 18),
see Appendix C.16.
□
Corollary 5.30. Let 𝑁 E-AIXIRO agents interact with a multi-agent environment 𝜇 , which all are
implementable on a POM with access to reflective oracle 𝜏. Then it holds that for each 𝜖 > 0, there exists
a finite time 𝑇 ( 𝜖) such that for all 𝑡 ≥ 𝑇 ( 𝜖), with probability greater than 1 − 𝜖, the personal Bayesian
mixture universes 𝜌RO
and E-AIXIRO policies ( 𝜋𝑖 ) 𝑖 are an 𝜖-subjective correlated embedded equilibrium in
𝑖
the correlated tail game starting at time 𝑡 with correlation device ((AE) 𝑡 , 𝜇 𝜋 ).
Proof. From Theorem 5.29 we know that the interaction of E-AIXIRO agents with a multi-agent
environment 𝜇 that is implementable on a POM with access to 𝜏, results in a universe which is also
𝜏 −RO
implementable by a POM with access to 𝜏, and hence it is part of Muni
. Therefore, 𝜌RO
satisfies the
𝑖
grain-of-truth property. It also trivially satisfies the grain-of-uncertainty property. We can now apply
Theorem 4.28 to get the result.
□
Unfortunately, analogous results do not hold for (𝑘-)E-AIXIRUI agents, due to the restrictions of
𝑤,𝜏-RUI
Muni
to universes that obey the constraints on oracle calls mentioned in Definition 5.6. For
example, computing the exact 𝑄 𝜌 values for the 𝑘-step planners (cf. Definition 3.9) can require
𝑤,𝜏-RUI
infinitely many oracle calls, which is not allowed in universes in Muni
.
To address this challenge, we use the 𝜖 approximations of the 𝑘-step planner embedded Bayesian
agents, introduced in Definition 4.32. By letting 𝜖𝑡 → 0 and 𝑘𝑡 → ∞ as 𝑡 → ∞, the ( 𝑘𝑡 , 𝜖𝑡 )-step
planner embedded Bayesian agent makes an increasingly better approximation of the embedded
Bayes-optimal agent as time progresses. The following Theorem shows that ( 𝜖𝑡 , 𝑘𝑡 )-E-AIXIRUI agents,
𝑤,𝜏-RUI
i.e., ( 𝑘𝑡 , 𝜖𝑡 )-step planner embedded Bayesian agents using hypothesis class Muni
and universal
prior 𝑤, satisfy the grain-of-truth property.
Theorem 5.31. For every complete prefix-free encoding of the finite sets A and E, and all computable
sequences ( 𝜖𝑡 )𝑡 and ( 𝑘𝑡 )𝑡 with 𝜖𝑡 > 0 ∀𝑡 , there exists a ( 𝑘𝑡 , 𝜖𝑡 )𝑡 -E-AIXIRUI policy with respect to the 𝑤-RUI
𝜌RUI , which is implementable by a rPOM 𝑀 𝜏 with access to the 𝑤-RUI-oracle 𝜏.
Furthermore, when writing ⟨𝑎𝑡 ⟩ on the output tape, the machine makes at most 𝑁˜𝑡 queries to the oracle,
where 𝑁˜𝑡 depends only on 𝑘𝑡 , 𝜖𝑡 and on the sizes of A and E.
Finally, when one or more such ( 𝑘𝑡 , 𝜖𝑡 )𝑡 -E-AIXIRUI policies are combined with a multi-agent environment 𝜇
that is implementable on a rPOM with access to RUI oracle 𝜏, then the resulting universe is part of
𝑤,𝜏 −RUI
Muni
.
Proof. See Appendix C.17

□

𝑤,𝜏-RUI
𝜏-RO
In conclusion, we introduced two novel hypothesis classes Muni
and Muni
over universes, and
various embedded Bayesian agents leveraging those novel hypothesis classes, which solve the general

62

grain-of-truth problem for embedded agency (cf. Problem 2.5). In Appendix G, we explain in more
detail how our formalism solves this grain-of-truth problem.
The remaining question is whether we can show that ( 𝑘𝑡 , 𝜖𝑡 )𝑡 -E-AIXIRUI agents converge to ( 𝜖, 𝛿)subjective correlated equilibria when interacting with each other. Theorem 5.32 shows that when we
take ( 𝑘𝑡 , 𝜖𝑡 )𝑡 such that lim𝑡→∞ 𝑘𝑡 = ∞ and lim𝑡→∞ 𝜖𝑡 = 0, we can prove the affirmative, even without
requiring the ‘sensible off-policy’ condition of Theorem 4.31.
Theorem 5.32. Let 𝑁 ( 𝑘𝑡 , 𝜖𝑡 )𝑡 -E-AIXIRUI agents, with lim𝑡→∞ 𝑘𝑡 = ∞ and lim𝑡→∞ 𝜖𝑡 = 0, interact with a
multi-agent environment 𝜇 , which all are implementable on a rPOM with access to RUI oracle 𝜏. Then
it holds that for each 𝜖 > 0 and 𝛿 > 0, there exists a finite time 𝑇 ( 𝜖, 𝛿) such that for all 𝑡 ≥ 𝑇 ( 𝜖, 𝛿),
with probability greater than 1 − 𝜖, the personal Bayesian mixture universes 𝜌RUI
and ( 𝑘𝑡 , 𝜖𝑡 )𝑡 -E-AIXIRUI
𝑖
policies are an ( 𝜖, 𝛿)-subjective correlated equilibrium in the correlated tail game starting at time 𝑡 with
correlation device ((AE) 𝑡 , 𝜇 𝜋 ).
Proof. This is a direct corollary of Proposition 4.33.

□

Unfortunately, the above positive result does not hold for 𝑘-E-AIXI agents using a fixed 𝑘, as the
‘sensibly off-policy’ condition required for Theorem 4.31 is not satisfied. Building upon the ‘dogmatic
beliefs’ framework of Leike and Hutter (2015b), we construct a counter example in Theorem 5.33
showing that 𝑘-E-AIXI agents do not always converge to an embedded best response w.r.t. 𝜌𝑖 . This
result holds for 𝑘-E-AIXI agents using any probabilistic oracle 𝜏 –e.g., the RUI oracle, reflective oracle
or a ‘dummy oracle’ always outputting 0 such that the POMs using this dummy oracle correspond
to standard monotone probabilistic Turing machines. This results also holds for decoupled 𝑘-AIXI
agents such as Self-AIXI which has 𝑘 = 1, thereby disproving the conjecture of Catt et al. (2023) that
the ‘sensibly off-policy condition’ is satisfied for all ‘reasonable’ hypothesis classes except for some
possible exotic counterexample classes.
Theorem 5.33. Consider a 𝑘-E-AIXI𝜏 agent, i.e., an embedded Bayesian agent employing 𝑘-step planning
for a fixed integer 𝑘 ≥ 1, with a mixture universe model 𝜌 constructed from a Solomonoff prior over
the hypothesis class M 𝜏 of POMs with access to an arbitrary probabilistic oracle 𝜏. Then, there exists
a computable ground-truth environment 𝜇 and a reference universal monotone Turing machine 𝑈 for
defining the Kolmogorov complexity 𝐾𝑈 in the Solomonoff prior, such that the agent interacting with
𝜇 does not converge to the embedded best response w.r.t. 𝜌, despite the fact that this setup satisfies the
grain-of-truth property. This result holds also for decoupled AIXI agents performing 𝑘-step planning with
a fixed 𝑘, such as Self-AIXI57 .
Proof. See Appendix C.18

□

5.4. Functional similarities through the lens of algorithmic information theory
We revisit the functional similarities introduced in Section 3.6 through the lens of algorithmic
information theory, formalizing the intuition of functional similarities as the joint ‘compressibility’
of agent and environment. The degree of functional similarities in Section 3.6 is determined by the
belief prior 𝑤, a choice we have not yet specified. Here, we fix the belief prior as the Solomonoff
universal prior (cf. Definition 5.10) arising from the algorithmic complexity of the considered universes.
Importantly, this algorithmic complexity depends on the choice of reference universal machine 𝑈
57 The failure
orously)
by

of Self-AIXI to
Cole
Wyeth

converge to AIXI was concurrently indicated (but not proved rigin
https://www.alignmentforum.org/posts/B6gumHyuxzR5yn5tH/
unbounded-embedded-agency-aedt-w-r-t-rosi.

63

to compute the Kolmogorov complexity, and the encoding ⟨ 𝑀 ⟩ of APOMs into bitstrings. Hence,
although we removed the arbitrary choice of prior beliefs, we instead introduced an arbitrary choice
of reference universal machine 𝑈 and encoding ⟨ 𝑀 ⟩. This motivates the main theorem of this section,
where we prove that the Solomonoff universal prior is always coupled, and that it contains universes
with arbitrarily high degrees of functional similarities, regardless of the choice of reference universal
machine 𝑈 and encoding ⟨ 𝑀 ⟩.
5.4.1. Solomonoff priors are always coupled
Setup. Let M APOM be the set of APOMs and let 𝜏 be an arbitrary probabilistic oracle, e.g., a reflective
oracle or a RUI oracle. Note that the presented theory also applies to standard probabilistic monotone
Turing machines without access to an oracle. Let ⟨ 𝑀 ⟩ be the binary encoding of 𝑀 according to
some canonical encoding. Using a universal monotone Turing machine 𝑈 , we obtain the Solomonoff
universal prior w.r.t. 𝑈 and ⟨ 𝑀 ⟩ as
𝑤𝑈 ( 𝑀 ) = 2 − 𝐾𝑈 ( ⟨ 𝑀 ⟩ ) ,
with 𝐾𝑈 the Kolmogorov complexity w.r.t. 𝑈 . Note that different machines can implement the same
function. We will not be interested in functional similarities between specific machines 𝑀 , but rather
between the universes 𝜆 𝜏𝑀 they implement. For this, let ⟨𝑎⟩ and ⟨𝑒⟩ be complete prefix-free encodings
𝜏
of A and E, respectively, into bitstrings. Now we can define Muni
to be the set of semimeasures on
∗
∗
action-percept histories in AE ∪ (AE × A) that are induced by APOMs in M APOM with access to 𝜏,
while using ⟨𝑎⟩ and ⟨𝑒⟩ to interpret the generated bitstrings. More precisely,
𝜏
Muni
= { 𝜆 𝜏𝑀 : 𝑀 ∈ M APOM } .

Note that results in this section do not depend on the specific choice of oracle 𝜏. Now the Solomonoff
𝜏
prior 𝑤𝑈 ( 𝑀 ) induces a prior 𝑤𝑈,𝜏 over Muni
as follows:
∑︁
∑︁
𝑤𝑈,𝜏 ( 𝜆 ) :=
𝑤𝑈𝑀 =
2− 𝐾𝑈 ( ⟨ 𝑀 ⟩ ) .
(28)
𝑀 ∈ M APOM :
𝜆 𝜏𝑀 =𝜆

𝑀 ∈ M APOM :
𝜆 𝜏𝑀 =𝜆

We are interested in defining functional similarities between policy 𝜋 and environment 𝜈 inside
a universe 𝜆 . One complication is that even if a universe 𝜆 is implementable by a POM 𝑀 𝜏 , its
conditionals 𝜋 and 𝜈 are not necessarily implementable by a 𝜏-POM.58 Hence, we introduce the
following restricted hypothesis class to contain only universes where the conditionals 𝜋 and 𝜈 are
also implementable on 𝜏-POMs, such that we can use the same machinery to handle 𝜆 , 𝜋 and 𝜈:
n
o
𝜏
𝜏
𝜏
𝜏
Mpol-env
:= 𝜈𝜋 : 𝜈 ∈ Menv
, 𝜋 ∈ Mpol
⊂ Muni
,
𝜏
𝜏
with Mpol
the set of policies AE ∗ → Δ′ A which are implementable by a 𝜏-POM, and Menv
the set
∗
′
of environments AE × A → Δ E which are implementable by a 𝜏-POM. For reasons of clarity, we
𝜏
further restrict Mpol-env
to fully supported universes:

Definition 5.34 (Fully supported universe). A universe 𝜆 is fully supported iff it is a measure59 , and
𝜆 (æ∗ ) > 0 and 𝜆 (æ∗ 𝑎) > 0 for all æ∗ ∈ AE ∗ and 𝑎 ∈ A.
The above definition refines Definition 3.16 of fully supported universes in Section 3, since in this
section we distinguish between measures and semimeasures.
58 To see why this is not nessarily the case, note that the conditional of a lower-semicomputable universe 𝜆 is not necessarily

lower-semicomputable itself (Leike, 2016).
59 This implies that Í
æ1:𝑡 ∈ AE 𝑡 𝜆 (æ1:𝑡 ) = 1 for all 𝑡 ≥ 1. Note that this does not necessarily hold if 𝜆 is a semimeasure.

64

𝜏
𝜏
We use M̌pol-env
to indicate the set of fully supported universes that are also part of Mpol-env
, and
𝜏
𝜏
𝜏
similarly M̌pol
and M̌env
for policies and environments derived from universes inside M̌pol-env
. We
have that
𝜏
𝜏
𝜏
M̌pol-env
⊂ Mpol-env
⊂ Muni
.
𝜏
When the prior beliefs are coupled on the restricted class M̌pol-env
, they will also be coupled on the
𝜏
other two classes, and hence it is sufficient for our purposes to show coupledness on M̌pol-env
. We
𝜏
𝜏
refer the interested reader to Appendix E which generalizes our study on M̌pol-env
to Mpol-env
. Finally,

we define the prior 𝑤
ˇ 𝑈,𝜏 ( 𝜆 ) over M̌pol-env by renormalizing 𝑤𝑈,𝜏 ( 𝜆 ):
𝑤
ˇ 𝑈,𝜏 ( 𝜆 ) := Í

𝑤𝑈,𝜏 ( 𝜆 )
,
𝑤𝑈,𝜏 ( 𝜆 ′ )
𝜆 ′ ∈ M̌

∑︁

𝑤
ˇ 𝑈,𝜏 ( 𝜋) :=

pol-env

𝑤
ˇ 𝑈,𝜏 ( 𝜈′𝜋 ) ,

𝑤
ˇ 𝑈,𝜏 ( 𝜈) :=

𝜈′ ∈ M̌env

∑︁

′

𝑤
ˇ 𝑈,𝜏 ( 𝜈𝜋 ) .

(29)

𝜋′ ∈ M̌pol

Functional similarities. We can readily apply the degree of functional similarities 𝑆 (equation 12)
𝜏
introduced in Section 3.6 to universes 𝜆 ∈ M̌pol-env
, resulting in
𝑆ˇ( 𝜆, 𝑈, ⟨·⟩) := 𝑆 ( 𝜆, 𝑤
ˇ 𝑈,𝜏 ) = log

𝑤
ˇ 𝑈,𝜏 ( 𝜆 )
, with ( 𝜋, 𝜈) = 𝑓 ( 𝜆 ) ,
𝑤
ˇ 𝑈,𝜏 ( 𝜋) 𝑤
ˇ 𝑈,𝜏 ( 𝜈)

(30)

where we used the unique mapping 𝑓 from a fully supported universe 𝜆 to its conditionals 𝜋 and 𝜈,
and where we introduced the notation 𝑆ˇ( 𝜆, 𝑈, ⟨·⟩) to highlight that this notion of functional similarities
depends on the choice of reference machine 𝑈 and encoding ⟨ 𝑀 ⟩. Let us now connect this notion of
functional similarities to joint compressibility of 𝜋 and 𝜈. Combining equations 28 and 29, we have
𝑤
ˇ 𝑈,𝜏 ( 𝜆 ) =

𝑤
ˇ 𝑈,𝜏 ( 𝜋) =

𝑤
ˇ 𝑈,𝜏 ( 𝜈) =

𝐶 :=

1
𝐶

1
𝐶

1
𝐶

∑︁

2− 𝐾𝑈 ( ⟨ 𝑀 ⟩ ) ,

𝑀 ∈ M APOM :
𝜆 𝜏𝑀 =𝜆

∑︁

∑︁

2− 𝐾𝑈 ( ⟨ 𝑀 ⟩ ) ,

𝜈′ ∈ M̌env 𝑀 ∈ M APOM :
𝜆 𝜏𝑀 =𝜈′𝜋

∑︁

∑︁

2− 𝐾𝑈 ( ⟨ 𝑀 ⟩ ) ,

𝜋′ ∈ M̌pol 𝑀 ∈ M APOM :
′
𝜆 𝜏𝑀 =𝜈𝜋

∑︁

𝑤𝑈,𝜏 ( 𝜆 ′ ) .

𝜆 ′ ∈ M̌pol-env

It is worth noting that 𝐶 is an absolute constant that only depends on the prior 𝑤𝑈,𝜏 .
The following is an informal discussion that aims to provide some intuition on the degree of functional
similarity 𝑆ˇ( 𝜆, 𝑈, ⟨·⟩) from the perspective of joint compressibility of the policy and the environment.
Let us define the complexities of 𝜆 , 𝜋 and 𝜈 as the following minimum description lengths
𝐾𝑈 ( 𝜆 ) := min{ 𝐾𝑈 (⟨ 𝑀 ⟩) : 𝑀 ∈ M APOM , 𝜆 𝜏𝑀 = 𝜆 } ,
𝜏
𝐾𝑈 ( 𝜋) := min{ 𝐾𝑈 (⟨ 𝑀 ⟩) : 𝑀 ∈ M APOM , ∃𝜈 ∈ M̌env
, 𝜆 𝜏𝑀 = 𝜈𝜋 } ,
𝜏
𝐾𝑈 ( 𝜈) := min{ 𝐾𝑈 (⟨ 𝑀 ⟩) : 𝑀 ∈ M APOM , ∃𝜋 ∈ M̌pol
, 𝜆 𝜏𝑀 = 𝜈𝜋 } .

65

Since sums of exponentials can often be approximated well by their largest element, as the tail
of an exponential decays quickly, one might write60 𝑤
ˇ 𝑈,𝜏 ( 𝜆 ) ≈ 2− 𝐾𝑈 ( 𝜆 ) /𝐶 , 𝑤
ˇ 𝑈,𝜏 ( 𝜋) ≈ 2− 𝐾𝑈 ( 𝜋 ) /𝐶 and
𝑈,𝜏
−
𝐾𝑈 ( 𝜈 )
𝑤
ˇ ( 𝜈) ≈ 2
/𝐶 , and hence we have that
𝑆ˇ( 𝜆, 𝑈, ⟨·⟩) ≈ 𝐾𝑈 ( 𝜋) + 𝐾𝑈 ( 𝜈) − 𝐾𝑈 ( 𝜆 ) + log( 𝐶 ) .

(31)

The above informal treatment shows the connection between the intuition of functional similarities as
joint compressibility of the policy 𝜋 and environment 𝜈, and the shortest description lengths of 𝜋, 𝜈
and 𝜆 .
The Solomonoff prior is always coupled. Let us first formalize what we mean by coupled and
decoupled.
𝜏
Definition 5.35 (Coupledness and decoupledness on M̌pol-env
). We call the prior beliefs 𝑤𝑈,𝜏 ( 𝜆 )
𝜏
𝜏
decoupled on M̌pol-env
iff we have that for all 𝜆 ∈ M̌pol-env

𝑤
ˇ 𝑈,𝜏 ( 𝜆 ) = 𝑤
ˇ 𝑈,𝜏 ( 𝜋) 𝑤
ˇ 𝑈,𝜏 ( 𝜈) ,

with ( 𝜋, 𝜈) = 𝑓 ( 𝜆 ) .

𝜏
We call the prior beliefs 𝑤𝑈,𝜏 ( 𝜆 ) coupled on M̌pol-env
iff they are not decoupled on M̌pol-env .
𝜏
We call 𝑤𝑈,𝜏 ( 𝜆 ) boundedly coupled on M̌pol-env
iff there exists absolute positive constants 𝐶1 < 𝐶2 such
𝜏
that for all 𝜆 ∈ M̌pol-env
we have61

𝐶1 𝑤
ˇ 𝑈,𝜏 ( 𝜋) 𝑤
ˇ 𝑈,𝜏 ( 𝜈) ≤ 𝑤
ˇ 𝑈,𝜏 ( 𝜆 ) ≤ 𝐶2 𝑤
ˇ 𝑈,𝜏 ( 𝜋) 𝑤
ˇ 𝑈,𝜏 ( 𝜈) ,

with ( 𝜋, 𝜈) = 𝑓 ( 𝜆 ) .

Obviously, a decoupled prior is boundedly coupled.
𝜏
𝜏
We call 𝑤𝑈,𝜏 ( 𝜆 ) unboundedly coupled on M̌pol-env
iff it is not boundedly coupled on M̌pol-env
.
𝜏
The next theorem shows that the Solomonoff prior is always unboundedly coupled on M̌pol-env
,
regardless of the choice of 𝑈 and encoding ⟨ 𝑀 ⟩.

Theorem 5.36. For every fixed choice of:
• a canonical encoding of ⟨ 𝑀 ⟩ of APOMs as binary strings,
• a universal monotone Turing machine 𝑈 ,
• a probabilistic oracle 𝜏 (which may or may not be a RUI-oracle),
• finite spaces A and E, with |A| ≥ 2 and |E | ≥ 2, and complete prefix encodings thereof,
60We emphasize that the equation 𝑤
ˇ 𝑈,𝜏 ( 𝜆 ) ≈ 2− 𝐾𝑈 ( 𝜆 ) /𝐶 should only be taken informally as we have not made the meaning
of the approximation ≈ precise. One potential interpretation of this approximation is equality up to multiplicative constants.
While this is correct for the normal Solomonoff prior considering monotone Turing machines without probabilistic oracles
(Li and Vitányi, 2019, Theorem 4.3.3), we do not know whether the same is true when we consider arbitrary probabilistic
oracles. Nevertheless, if we replace the exponential 2− 𝐾𝑈 ( 𝜆 ) by 𝛼− 𝐾𝑈 ( 𝜆 ) for some 𝛼 > 2 in all our equations, then we can
indeed show that 𝑤
ˇ 𝑈,𝜏 ( 𝜆 ) is equal to 𝛼− 𝐾𝑈 ( 𝜆 ) up to multiplicative constants.
61 It is worth noting that for bounded coupling, we can write the condition in terms of the unnormalized prior 𝑤𝑈,𝜏
𝜏
directly: 𝑤𝑈,𝜏 ( 𝜆 ) is boundedly coupled on M̌pol-env
iff there exists absolute positive constants 𝐶1 < 𝐶2 such that for all
𝜏
𝜆 ∈ M̌pol-env
we have

𝐶1 𝑤𝑈,𝜏 ( 𝜋) 𝑤𝑈,𝜏 ( 𝜈) ≤ 𝑤𝑈,𝜏 ( 𝜆 ) ≤ 𝐶2 𝑤𝑈,𝜏 ( 𝜋) 𝑤𝑈,𝜏 ( 𝜈) ,

with ( 𝜋, 𝜈) = 𝑓 ( 𝜆 ) .

66

we have:
𝜏
(cf. Definition 5.35);
(a) The Solomonoff prior 𝑤𝑈,𝜏 is always unboundedly coupled on M̌pol-env

(b) There are fully-supported policies 𝜋 and environments 𝜈 sharing arbitrarily large degrees of func𝜏
tional similarity 𝑆ˇ( 𝜈𝜋 , 𝑈, ⟨·⟩), i.e., for every 𝑠 > 0, there is at least some 𝜋 ∈ M̌pol
and some
𝜏
𝜈 ∈ M̌env
such that

𝑆ˇ( 𝜈𝜋 , 𝑈, ⟨·⟩) > 𝑠 .

Proof. See Appendix E and the proof of Theorem E.22.

□

The results of the above theorem are not too surprising: One can design two APOM machines
𝑀 𝑝 and 𝑀𝑒 , one for a policy and one for an environment, which are algorithmically very similar
so that 𝐾𝑈 (⟨ 𝑀 𝑝 ⟩) ≈ 𝐾𝑈 (⟨ 𝑀𝑒 ⟩), but at the same time both 𝑀 𝑝 and 𝑀𝑒 are sufficiently complex so
that 𝐾𝑈 (⟨ 𝑀 𝑝 ⟩) ≫ 𝑠 and 𝐾𝑈 (⟨ 𝑀𝑒 ⟩) ≫ 𝑠. If we let 𝑀𝑢 be the APOM machine implementing the
universe in which 𝑀 𝑝 and 𝑀𝑒 interact and alternate, then we can see that 𝐾𝑈 (⟨ 𝑀𝑢 ⟩) ≈ 𝐾𝑈 (⟨ 𝑀 𝑝 , 𝑀𝑒 ⟩) ≈
𝐾𝑈 (⟨ 𝑀 𝑝 ⟩) ≈ 𝐾𝑈 (⟨ 𝑀𝑒 ⟩), and hence 𝐾𝑈 (⟨ 𝑀 𝑝 ⟩) + 𝐾𝑈 (⟨ 𝑀𝑒 ⟩) − 𝐾𝑈 (⟨ 𝑀𝑢 ⟩) ≫ 𝑠. Let 𝜆 , (resp. 𝜋, 𝜈) be the
universe (resp. policy, environment) induced by the POM 𝑀𝑢𝜏 (resp., 𝑀 𝜏𝑝 , 𝑀𝑒𝜏 ). If 𝑤𝑈,𝜏 ( 𝜆 ) ≈ 2− 𝐾𝑈 ( ⟨ 𝑀𝑢 ⟩ ) ,
𝑤𝑈,𝜏 ( 𝜋) ≈ 2 − 𝐾𝑈 ( ⟨ 𝑀 𝑝 ⟩ ) and 𝑤𝑈,𝜏 ( 𝜈) ≈ 2 − 𝐾𝑈 ( ⟨ 𝑀𝑒 ⟩ ) , then from equation 31 we should expect that
𝑆ˇ( 𝜆, 𝑈, ⟨·⟩) ≈ 𝐾𝑈 (⟨ 𝑀 𝑝 ⟩) + 𝐾𝑈 (⟨ 𝑀𝑒 ⟩) − 𝐾𝑈 (⟨ 𝑀𝑢 ⟩) ≫ 𝑠.

This is essentially the core intuition behind the proof of Theorem 5.36. Importantly, there are
a few technical challenges to make this intuitive argument formal and precise. For example, we
cannot directly use the intuitive notion that 𝑤𝑈,𝜏 ( 𝜆 ) ≈ 2− 𝐾𝑈 ( ⟨ 𝑀𝑢 ⟩ ) , as we do not know whether
the approximation holds up to a multiplicative constant if 𝜏 is an arbitrary probabilistic oracle.
Furthermore, the prior 𝑤𝑈,𝜏 adds up contributions from every machine 𝑀 for which 𝜆 𝜏𝑀 = 𝜆 :
𝑤𝑈,𝜏 ( 𝜆 ) =

1
𝐶

∑︁

2− 𝐾𝑈 ( ⟨ 𝑀 ⟩ ) .

𝑀 ∈ M APOM :
𝜆 𝜏𝑀 =𝜆

Some of these machines might be very different from 𝑀𝑢 and we cannot say that 𝐾𝑈 (⟨ 𝑀 ⟩) ≈ 𝐾𝑈 (⟨ 𝑀 𝑝 ⟩)
for all these machines.
In Appendix E, we show that this theorem not only implies the (unbounded) coupledness of the
𝜏
𝜏
Solomonoff prior on M̌pol-env
, but also on Mpol-env
. Solomonoff induction is arguably the ideal prediction method for predicting future action-percept trajectories, without requiring stationarity or
ergodicity assumptions. Hence, Theorem 5.36 shows the importance of taking functional similarities
into account when making predictions about the future, as all Solomonoff priors are coupled due
to functional similarities. This further illustrates the important conceptual advances of embedded
Bayesian agents and embedded-AIXI over their decoupled counterparts: The incorporation of functional similarities into their predictions and resulting behavior leads to new kinds of predictions
and behavior as detailed in Sections 3–4, and is motivated from first principles through Solomonoff
induction (cf. Theorem 5.36).
5.4.2. Universes sharing a common algorithmic structure
The proof of Theorem 5.36 in Appendix E relies on a constructive argument: It defines a specific
(and contrived) family of universes where policies and environments are explicitly built to share a
67

computational backbone. This section delves into the general principle underlying that proof. We
formalize the idea that policies and environments can be composed from common "templates" or
"subroutines", and show that the Solomonoff prior naturally assigns higher probability to universes
where such algorithmic sharing occurs. This provides a deeper, more foundational reason for why the
prior is always coupled. We only provide here a high-level and a very condensed explanation of the
concepts and the results. Refer to Appendix E.1 for a thorough treatment of the subject.
The core idea is to model computational templates as programs with placeholders. We achieve this
by generalizing our notion of oracle machines.
Definition 5.37 (Multi-Oracle Machines). An 𝑛-abstract probabilistic oracle machine (𝑛-APOM) is
a monotone Turing machine with access to 𝑛 distinct oracles, 𝑂1 , . . . , 𝑂𝑛 . The first oracle, 𝑂1 , is
treated as the primary oracle (e.g., our fixed 𝜏), while 𝑂2 , . . . , 𝑂𝑛 serve as placeholders for unspecified
subroutines.
This framework allows us to define program templates. An 𝑛-APOM represents a general computational
structure, and a concrete program (a 1-POM) can be created by "plugging in" other programs (1APOMs) to serve as the subroutines. This composition is defined formally as follows:
Definition 5.38 (Composition of Oracle Machines). Given an 𝑛-APOM, 𝑀 , and 𝑛 − 1 standard 1APOMs, 𝑀2 , . . . , 𝑀𝑛 , we can construct a new 1-APOM, denoted 𝑀 [ 𝑀2 , . . . , 𝑀𝑛 ]. This new machine
simulates 𝑀 as follows:
• When 𝑀 calls its first oracle, 𝑂1 , the new machine passes this query to its own single oracle.
• When 𝑀 calls any other oracle 𝑂𝑖 (for 𝑖 ∈ {2, . . . , 𝑛}), it instead simulates the execution of the
corresponding machine 𝑀𝑖 . It feeds the query string as input to 𝑀𝑖 and uses the output of 𝑀𝑖 as
the oracle’s answer. While executing 𝑀𝑖 , any call to the (single) oracle of 𝑀𝑖 is directed to the
single oracle of the new machine.
This leads to the formal definition of an algorithmic structure.
Definition 5.39 (Algorithmic Structure). An 𝑛-APOM, 𝑀 , defines an algorithmic structure. A standard
1-APOM, 𝑀 ′ , is said to possess the structure defined by 𝑀 if there exist 𝑛 −1 other 1-APOMs, 𝑀2 , . . . , 𝑀𝑛 ,
such that 𝑀 ′ is computationally equivalent to the composite machine 𝑀 [ 𝑀2 , . . . , 𝑀𝑛 ]. We can define
structures for policies, 𝑀 𝑝 , environments, 𝑀𝑒 , or entire universes, 𝑀𝜆 . See Appendix E.1 for more
details.
We will be interested in subroutine machines that almost surely halt for every input.
Definition 5.40 (proper subroutines). A POM 𝑀 𝜏 is said to be a proper subroutine if for every input
𝑥 ∈ B ∗ , the POM 𝑀 𝜏 almost surely halts. In other words, 𝑀 𝜏 induces a mapping 𝑀 𝜏 : B ∗ → Δ B.
The proof of Theorem 5.36 (and its formal version Theorem E.22) implicitly defines an algorithmic
structure where both policy and environment are built from the same underlying function. One key
property of this specific algorithmic structure, and which was helpful for the proof of Theorem 5.36,
was the identifiability of its subroutine, which we can formalize as follows:
Definition 5.41 (Identifiable Subroutines). An algorithmic structure 𝑀 has identifiable subroutines
w.r.t. the probabilistic oracle 𝜏, if there exist "identifier" programs { 𝐼 𝑖 } 𝑛𝑖=2 that can computationally
recover the behavior of any proper subroutine 𝑀𝑖𝜏 simply by observing the input-output behavior
of the complete, composed machine 𝑀 [ 𝑀2 , . . . , 𝑀𝑛 ] 𝜏 . More precisely, each 𝐼 𝑖 is a 2-APOM and
68

𝐼 𝑖 [ 𝑀 [ 𝑀2 , . . . , 𝑀𝑛 ]] 𝜏 is distributionally equivalent to 𝑀𝑖𝜏 for all 𝑖 ∈ {2, . . . , 𝑛}, i.e., for every 𝑥 ∈ B ∗ and
every 𝑦 ∈ B, we have
ℙ[ 𝐼 𝑖 [ 𝑀 [ 𝑀2 , . . . , 𝑀𝑛 ]] 𝜏 ( 𝑥 ) = 𝑦 ] = ℙ[ 𝑀𝑖𝜏 ( 𝑥 ) = 𝑦 ] .

In essence, the subroutines’ contributions are not irrevocably hidden by the main computation. See
Examples E.34 and E.35 for an illustration of algorithmic structures with identifiable subroutines.
Now we are ready to state the following theorem, which can be seen as a generalization of Theorem 5.36 to arbitrary algorithmic structures with identifiable subroutines:
Theorem 5.42. Let 𝑀 𝑝 and 𝑀𝑒 be algorithmic structures for policies and environments, respectively,
using the same number of subroutines. If both 𝑀 𝑝 and 𝑀𝑒 have identifiable subroutines, and the set of
fully-supported universes where they share identical subroutines is infinite, then for any Solomonoff prior
𝑤𝑈,𝜏 , there exist fully-supported policies 𝜋 (possessing structure 𝑀 𝑝 ) and environments 𝜈 (possessing
structure 𝑀𝑒 ) with arbitrarily large degrees of functional similarity. That is, for any 𝑠 > 0, there is at
least one such pair ( 𝜋, 𝜈) for which 𝑆ˇ( 𝜈𝜋 , 𝑈, ⟨·⟩) > 𝑠.
Proof. See Appendix E.1 and the proof of Theorem E.36.

□

This theorem reveals a fundamental principle: The coupledness of the Solomonoff prior is not an
accident of a particular construction but the manifestation of a general phenomenon. Whenever
policies and environments can be described by general computational templates with common (and
identifiable) components, such algorithmic similarities will cause the policies and environments to
have large degrees of functional similarities w.r.t. the Solomonoff prior (as per Definition E.18), and
hence the Solomonoff prior will be “highly coupled" for such policies and environments.

6. Discussion
6.1. MUPI as a coherent framework for learning in multi-agent systems
This work introduced the MUPI framework to address fundamental limitations in current approaches
to multi-agent learning with model-free RL, moving from retrospective learning to prospective learning
and from a paradigm of decoupled agency to one of embedded agency.62 For prospective learning,
we have shown that principled anticipation of the future in non-stationary, multi-agent worlds is
possible through Bayesian sequence prediction over general model classes. This stands in contrast to
retrospective model-free RL methods that compute policy updates based on past data, which is often
outdated in environments with other learning agents. A cornerstone of this prospective capability of
Bayesian prediction is the grain-of-truth property: By ensuring the agent’s model class contains the true
universe including the agent itself, the Bayesian predictions are guaranteed to converge to the groundtruth distribution, resulting in principled prospective predictions even when the future is changing
relative to the past. By leveraging the framework of reflective oracles, and introducing our new
framework of the reflective universal inductor, we designed universal embedded agents (embeddedAIXI agents) with a Bayesian mixture universe satisfying the grain-of-truth property, thereby solving
the general embedded grain-of-truth problem. The resulting predictive model, which jointly forecasts
an agent’s own actions and its percepts, is conceptually aligned with modern foundation models that
also predict both actions and percepts.
62We note that the prospective learning aspect is also satisfied by AIXI agents and their multi-agent variants (e.g., reflective
AIXI (Fallenstein et al., 2015a; Leike et al., 2016b)).

69

Leveraging the Bayesian prediction models 𝜌, we introduced prospective policy learning methods
as 𝑘-step planning within 𝜌, which are similar to Self-AIXI (Catt et al., 2023) and reminiscent of
classical policy iteration and the MuZero family of methods, but with the crucial difference that the
𝑄 -values are estimated based on prospective predictions rather than past data under the assumption of
stationarity. By planning within a predictive model that anticipates its own future improvements and
the learning of others, the agent becomes both self-learning aware and co-player learning-aware. This
generalizes existing work on co-player learning-aware RL by enabling mutual prospective prediction
without making inconsistent assumptions about other agents’ learning algorithms.
A key challenge with mutual prediction is avoiding the pitfalls of infinite recursion of the form “I predict
that you predict that I predict....” MUPI resolves this through the construction of its predictive model,
the Reflective Universal Inductor (RUI). Rather than getting caught in an infinite computational
loop at runtime, a MUPI agent consults the RUI 𝜌, which is, by definition, a consistent fixed point
for such recursive beliefs. This consistency emerges because all agents perform Bayesian updates
over a shared, universal hypothesis class of universes that already contain universes with agents
making predictions about each other. The RUI thus sidesteps infinite recursion, providing a coherent
prediction conditioned on an agent’s personal history while having already accounted for mutual
modeling, up to infinite orders of theory of mind.
This theoretical construct has a practical analogue in a neural prediction model, like a transformer,
trained on data from interacting agents engaging in mutual prediction. Such a model always returns a
prediction without running into infinite recursions, as it does not explicitly run a simulation of agents
predicting each other. In practice, the learned prediction model may not make perfect predictions
under uncertainty. In such cases, it can be beneficial to apply reasoning traces within the prediction
model, explicitly reasoning about the ongoing mutual prediction, up to a depth of 𝑘 recursion steps.
This is reminiscent of applying 𝑘th -order theory of mind, and the 𝑘-level reasoning strategy within
Economics theory for bounded rationality (Crawford et al., 2013). It is crucial to recognize that such
𝑘-level reasoning provides no new information—as no new observations are made—but rather offers
additional computation to help an imperfect model better approximate ideal Bayesian inference. The
predictions of an ideal MUPI agent with a perfect RUI are already flawlessly Bayesian, making any
further explicit reasoning computationally redundant.
Besides the shift from retrospective to prospective learning, the second major shift we proposed is from
decoupled to embedded agency. By treating the agent as part of the universe it models, MUPI enables
true self-modeling and an infinite-order theory of mind. An important consequence of this embedded
viewpoint is the ability to reason about functional similarities between oneself and others, leading
to coupled beliefs where knowledge about one’s own policy informs predictions about other agents
within the environment. This mechanism unlocks novel strategies for both prediction and behavior.
For prediction, it enables similarity-aware prediction, allowing an agent to anticipate the actions
of others in novel situations by considering its own planned behavior and reasoning that “similar
agents behave similarly in similar situations.” For behavior, it enables new forms of cooperation
and coordination through the embedded equilibria, a family of new solution concepts that can, for
instance, justify cooperation in the Twin Prisoner’s Dilemma—an outcome inaccessible to classical
game theory. The study of such functional similarities is not merely a theoretical curiosity; it can have
important practical implications. As we move toward deploying vast numbers of AI agents, many of
which are based on shared foundation models, similarity awareness may offer a powerful mechanism
for achieving robust coordination with minimal communication, possibly paving the way for effective
social scaling—increasing the capabilities of a society of agents by increasing their numbers.

70

6.2. The connection between the MUPI framework and current foundation models
The framework of embedded Bayesian agents, centered around a predictive model of both one’s own
actions and incoming observations, shares important similarities with modern foundation models
and their agentic derivatives. First, the mixture universe, 𝜌, functions as a joint predictive model that
forecasts both the agent’s own actions and its incoming percepts. This is directly analogous to the way
many foundation models are trained to predict the next token in a sequence, which can represent either
an observation from the world or an action taken by the agent. Second, the embedded Bayes-optimal
agent, which is the optimal policy w.r.t. the prediction model 𝜌, is conceptually similar to model-based
RL agents that learn a world model and then use it to simulate imagined future trajectories to find
an optimal policy. The more practical 𝑘-step planner agent (cf. Section 3.4) closely resembles the
MuZero family of algorithms, which also learn a model and perform a limited look-ahead search to
improve their policy. In its simplest form, a one-step planner (𝑘 = 1) dispenses with explicit planning
and instead selects the action that maximizes the learned 𝑄 -value function, a strategy reminiscent of
classic methods like 𝑄 -learning and TD(0) (Sutton and Barto, 2018). Conceptually, our framework is
flexible enough to accommodate other forms of policy improvement that rely on prediction with a
sequence model, such as the chain-of-thought reasoning increasingly used in large language models.
However, it is important to note that the convergence guarantees we have established (Theorems
4.28 and 4.31) are specific to the embedded Bayes-optimal and 𝑘-step planner agents; extending
these proofs to other policy improvement mechanisms requires additional theoretical developments.
Despite these parallels, the primary divergence between MUPI and current foundation models lies in
the learning process itself. An embedded Bayesian agent learns through explicit Bayesian inference: It
begins with a prior belief over all possible universes and performs exact posterior updates conditioned
on its entire life history—a single, unbroken sequence of interactions. In contrast, foundation models
are typically trained using stochastic gradient descent on vast datasets chunked into batches of
“episodic trajectories.” Hence, the explicit Bayesian inference of Bayesian agents is replaced by a
combination of in-weight learning, where past training data is distilled into the model parameters,
and in-context learning, where the model performs rapid, on-the-fly inference based on the current
context (Elmoznino et al., 2024; Ortega et al., 2019; Von Oswald et al., 2023a,b; Xie et al., 2021).
This distinction raises a critical question: Can foundation models, trained this way, achieve the kind
of principled prospective prediction that MUPI guarantees?
This difference in training methodology means that a model-based RL agent can still be fundamentally
retrospective if its learned model is overfitted to recent past data and fails to generalize to a nonstationary future that can be different from the recent past. Achieving true prospective prediction
requires principled methods that can anticipate future changes (Bornschein et al., 2024). Some
theoretical work suggests that stochastic gradient descent can approximate sampling-based Bayesian
inference (Chaudhari and Soatto, 2018; Liu and Theodorou, 2019; Mandt et al., 2017). However,
training neural sequence models to robustly approximate Bayesian prediction starting from an Occam’s
razor prior—thereby ensuring they can make accurate, prospective forecasts in dynamically changing
worlds—remains an open problem (Bornschein et al., 2024; De Silva et al., 2024).
6.3. Active exploration with embedded Bayesian agents
As embedded Bayesian agents are fundamentally uncertain about which universe they live in, explorative behavior that reduces this uncertainty is critical. Bayesian agents with sufficiently broad
priors naturally incorporate a form of principled, directed exploration through the value of information
(Chalkiadakis and Boutilier, 2003; Howard, 1966), where an agent is intrinsically motivated to take
actions that reduce uncertainty about the world if that information is expected to improve future
rewards, for example through enabling more detailed planning. However, as prior work has shown,
71

this Bayesian form of exploration is often insufficient to overcome dogmatic beliefs about catastrophic
outcomes (Leike and Hutter, 2015b; Orseau, 2010b). An agent may hold a belief that any deviation
from its current policy will result in a catastrophically low reward, and since it never deviates, this
flawed belief is never corrected.
The coupled beliefs of embedded Bayesian agents have the potential to further aggravate this problem.
For a decoupled agent, a dogmatic belief is about an external state of the world. For an embedded
agent, taking an action can now be interpreted as direct evidence about the environment and the
obtainable rewards. An embedded Bayesian agent can therefore hold a dogmatic belief that simply
deviating from a certain policy is strong evidence that it lives in a low-reward universe. This creates a
self-fulfilling trap, preventing the agent from ever gathering the data needed to correct its wrong
beliefs. We show this result formally in Proposition 4.29, which demonstrates that for any deterministic
policy and environment, there exist dogmatic beliefs for which the agent’s embedded best response is
precisely that policy.
These results on dogmatic beliefs have motivated the use of more active exploration strategies,
such as Thompson sampling (Cohen et al., 2019; Leike et al., 2016a). Equipping AIXI agents with
such active exploration strategies can lead to asymptotically optimal policies, guaranteeing that for
any ground-truth environment within the model class, such agents converge to an optimal policy.
Importantly, however, such additional active exploration also often leads to unsafe behavior due to its
inherent randomness (Cohen et al., 2021), which could potentially incapacitate the agent. These two
seemingly opposite characteristics of active exploration enabling optimal behavior but also potentially
incapacitating the agent are compatible, as any policy is optimal when in a state from which one can
no longer affect the world. Hence, finding robust exploration strategies to overcome dogmatic beliefs
while safely exploring the environment remains a critical open challenge in the field.
Investigating such robust exploration strategies within the MUPI framework is an exciting direction
for future research. Adapting existing active exploration methods for decoupled agents, such as
Thompson sampling (Leike et al., 2016a), to the embedded Bayesian agent setting will be crucial.
A key theoretical goal would be to show convergence towards embedded equilibria in the general
MAGRL setting, by ensuring agents can escape the suboptimal traps of purely subjective equilibria
built on dogmatic beliefs.
6.4. The connection between the MUPI framework and Evidential, Causal, and Functional
Decision Theory
At its core, MUPI is a form of action evidential decision theory (EDT) (Everitt et al., 2015), as it
computes the future consequences of an action 𝑎 by conditioning its Bayesian prediction model 𝜌
on that action. While causal decision theory (CDT) is often viewed as the gold standard for rational
choice, its utility is limited to settings where the system being modeled does not contain the agent.
In such decoupled settings, the agent’s action is an external intervention that creates a distributional
shift w.r.t. some ‘default behavior of the agent’ in the system it acts upon. To correctly predict such
distributional shifts, the action should be treated as a do-intervention upon the system being modeled
(Pearl, 2009), as is done by CDT. Hence, CDT is the correct formalism when an agent is truly separate
from the environment it is modeling.
However, in the context of embedded agency, the agent’s decision-making (i.e., policy) is a process
unfolding within the universe, not an intervention from the outside. There is no external force
creating a distributional shift; there is only the natural evolution of the universe, which includes the
agent’s deliberation and subsequent action. In this setting, EDT is the more natural and powerful
framework. Applying a CDT-style do-intervention would be artificial and actively detrimental, as

72

it would force the agent to ignore the predictive evidence its own choices provide about the world,
especially given functional similarities with other agents. By severing these evidential links, CDT can
lead to less accurate predictions and, consequently, to suboptimal behavior such as defection on the
Twin Prisoner’s Dilemma.
Furthermore, MUPI provides a new formalism that captures some of the core intuitions of functional
decision theory (FDT) without resorting to its most problematic element: logical counterfactuals. FDT
advises an agent to choose the action that would yield the best outcome if its decision-making function
were to produce that output, thereby accounting for all instances of its own algorithm in the world.
This enables FDT to coordinate and cooperate well with copies of itself. FDT must reason about
what would have happened if its deterministic algorithm had produced a different output, a notion of
logical counterfactuals that is not yet mathematically well-defined. MUPI achieves a similar outcome
through a different mechanism: the combination of treating universes including itself as programs,
while having epistemic uncertainty about which universe it is inhabiting—including which policy it
is itself running. As explained in Remark 3.14, from the agent’s internal perspective, it acts as if its
choice of action decides which universe it inhabits, including which policy it is running. When it
contemplates taking action 𝑎, it updates its beliefs 𝑤 ( 𝜆 |æ<𝑡 𝑎), effectively concentrating probability
mass on universes compatible with taking action 𝑎. Because the agent’s beliefs about its own policy
are coupled with its beliefs about the environment through functional similarities, this process allows
the agent to reason about how its choice of action relates to the behavior of other agents that share
functional similarities. This “as if ” decision-making process allows MUPI to manifest the sophisticated,
similarity-aware behavior FDT aims for, but on the solid foundation of Bayesian inference rather than
on yet-to-be-formalized logical counterfactuals.
6.5. Philosophical implications
Beyond its technical contributions to multi-agent learning, the MUPI framework offers a formal lens
through which to examine long-standing philosophical questions about the nature of consciousness
and free will. By grounding modern theories of consciousness and free will in a computational model
of embedded agency, MUPI provides a concrete language for discussing how these phenomena could
arise in both biological and artificial minds.
Self-models and Consciousness. At the heart of MUPI lies a powerful conception of self-awareness:
The agent’s predictive model 𝜌 must make predictions about the agent using that very model to make
predictions. This creates a scenario of self-reference, reminiscent of Douglas Hofstadter’s concept of
strange loops as a cornerstone of consciousness (Hofstadter, 2007). This recursive self-model is not a
mere theoretical curiosity; it serves a critical, functional purpose that aligns with modern functional
theories of consciousness like Michael Graziano’s Attention Schema Theory (Graziano, 2013; Graziano
and Webb, 2015). Graziano argues that consciousness is a computational mechanism that evolved
for a specific purpose: to model one’s own and others’ mental states. According to this view, the
feeling of being conscious arises from a high-level, predictive model of one’s own attentional processes,
allowing an agent to better understand and predict on the one hand its own internal processes to
effectively control them (Conant and Ross Ashby, 1970; Richens et al., 2025), and on the other hand
the behavior of other agents by simulating their mental states using its own as a template.
By including a self-model 𝜌 over a class of universes that explicitly includes the agent itself as a
core mechanism of embedded agency, MUPI provides a detailed mathematical foundation of this
idea of the joint modeling of self and others, while introducing a new behaviorally relevant function
of consciousness. By reasoning about functional similarities, the agent leverages its understanding
of its own decision-making process to form accurate, prospective predictions about others. This
73

ability to see oneself in others is what unlocks novel forms of cooperation and social coordination,
as formalized by the embedded equilibrium. Furthermore, while Attention Schema Theory mainly
focuses on first-order modeling of the neural attention processes, our reflective universal inductor 𝜌
highlights the infinite recursions that occur when a prediction model 𝜌 models an agent using this
prediction model itself. In this light, MUPI further operationalizes the role of self-modeling within the
Attention Schema Theory for consciousness, by (i) providing an idealized theoretical model organism
of a self-modeling embedded Bayesian agent, (ii) introducing a novel functional benefit of the joint
modeling of self and others through enabling novel forms of cooperation and social coordination, and
(iii) formally connecting Bayesian self-modeling with the self-reference or strange loops arising as a
direct consequence of this self-modeling.
Embedded agency and free will. The concept of free will has long been debated against the
backdrop of a lawful universe. This tension is often framed as the ‘standard argument’ for hard
determinism: If the universe is deterministic, its future is fixed by its past, meaning an agent could
not have “acted otherwise". If the universe is instead stochastic, an agent’s actions might be mere
random occurrences, not attributable to rational agency. In either view, meaningful free will appears
illusory.
The MUPI framework offers a powerful formalism that operationalizes a compatibilist resolution to this
dilemma, aligning closely with modern philosophical accounts. Christian List proposes levels-based
compatibilism, which distinguishes between physical possibility (what is possible given the precise,
low-level micro-state of the universe) and agential possibility (what is possible given an agent’s
high-level psychological state) (List, 2014). List argues that even if the physical level is deterministic
(only one physically possible future), the agential level can be indeterministic, as a single mental state
can be realized by many different physical states, each with a different future.
MUPI provides an alternative computational model for this dichotomy of physical and agential
possibilities, which does not rely on the coarse graining of physical states, but rather leverages
Bayesian uncertainty about one’s own policy. The unknown ground-truth universe 𝜐 corresponds
to physical possibility; it is the single, lawful63 system whose evolution dictates the agent’s actual
future policy. In contrast, the agent’s predictive model 𝜌 corresponds to agential possibility. An agent’s
"mental state" is captured by its history æ1:𝑡 and the resulting posterior belief 𝑤 ( 𝜆 | æ1:𝑡 ). From the
agent’s embedded perspective, this belief is distributed over many possible universes 𝜆 that are all
consistent with its past æ1:𝑡 . This epistemic uncertainty about which universe it inhabits, and crucially,
which policy it is itself running, means that multiple futures and multiple actions are “agentially
possible" even if the ground-truth universe 𝜐 is predetermined.64
Furthermore, the very process of decision-making in MUPI aligns with the compatibilist philosophy
of Daniel Dennett (Dennett, 2004). Dennett argues that free will is not a mysterious ability to
defy causality, but rather a sophisticated, evolved capacity for rational deliberation and control. An
embedded Baysian agent within the MUPI framework embodies this. It is not a passive domino in a
causal chain. It actively considers the future consequences of its potential actions by planning within
its predictive model 𝜌, and it deliberately chooses the action that leads to the most highly-valued
outcome. MUPI thus provides a concrete, mathematical model for these compatibilist theories of free
will, demonstrating how an agent whose reasoning is part of the universe’s causal structure can still
63 Note that in the MUPI formalism, the lawful universe can either be deterministic or stochastic.

64 It is worth mentioning that Self-AIXI (Catt et al., 2023) also has epistemic uncertainty about which policy the agent
itself is running, and hence also considers multiple actions as “agentially possible". Importantly however, Self-AIXI keeps
separate beliefs about its own policy and the rest of the universe, and hence does not consider itself as a part of the universe.
This makes MUPI, where agents treat themselves as part of the universe, a more conceptually natural framework to discuss
the philosophical topic of free will within a lawful universe.

74

possess the freedom to anticipate futures and select the optimal path to its goals.
6.6. Limitations and future work
This work has focused on providing a conceptual theory for multi-agent learning based on embedded
Bayesian agents. While the MUPI framework addresses several fundamental challenges, it also
highlights important limitations and opens new avenues for future research.
First, Demski and Garrabrant (2019) provide an informal survey on the conceptual difficulties in
formalizing embedded agency. MUPI addresses some of these, such as providing an embedded world
model (the RUI) that uses randomization to avoid self-referential paradoxes, and leveraging epistemic
uncertainty over its own algorithm as an alternative to the problematic logical counterfactuals
discussed by Demski and Garrabrant (2019) and Yudkowsky and Soares (2017). However, several
other deep challenges remain open. A significant one is how an embedded agent can safely modify
its own decision algorithm or goal structure to improve itself, while ensuring it remains aligned
with the goals of its previous version (Orseau and Ring, 2011, 2012; Schmidhuber, 2009; Zhao and
Schmidhuber, 1996). Investigating these advanced problems of embedded agency through the MUPI
framework is an exciting direction for future research.
Second, there is a gap between our conceptual theory and practical applications. The theory leverages
Bayesian sequence prediction, Occam’s razor priors, and the grain-of-truth property to achieve
principled prospective prediction that can anticipate future non-stationarities, such as those caused
by other learning agents. How to effectively approximate this powerful predictive capability using
practical continual and online learning techniques for neural network sequence models remains a
major open problem (Bornschein et al., 2024; De Silva et al., 2024).
Third, our theoretical agents, the Embedded AIXI agents, are incomputable. Furthermore, to satisfy
the grain-of-truth property, they must consider a hypothesis class over incomputable oracle machines.
Any practical approximation using computational devices, such as neural sequence models, will
likely violate the grain-of-truth property. Furthermore, exact Bayesian posterior updates are generally intractable, necessitating the use of approximate inference methods. This raises an important
research question: how robust are the benefits of prospective prediction to these approximations?
Understanding whether the performance degrades gracefully when the grain-of-truth property is not
perfectly satisfied and inference is imperfect is key to its practical viability.
Finally, a crucial assumption for achieving consistent mutual prediction in both the framework of
reflective oracles and our RUI is that all agents utilize the same oracle. This shared component results
in a form of ‘precomputed consistency’ among the agents, as the oracle’s answers are derived from
a precomputed fixed point. A challenging and interesting direction for future work is to develop
methods that can achieve approximate consistent mutual predictions without relying on such a
precomputed fixed point, moving closer to decentralized and ad-hoc coordination.

Acknowledgements
We would like to thank Cole Wyeth, Geoff Keeling, Johannes von Oswald, Nino Scherrer, Robert Obryk,
Yul Kwon, James Evans, Yanick Schimpf, Maximilian Schlegel, Eric Elmoznino, Winnie Street, Roberta
Rocca and the Google Paradigms of Intelligence team for feedback and enlightening discussions. GL
and BR acknowledge support from the CIFAR chair program.

75

References
M. Aghajohari, J. A. Duque, T. Cooijmans, and A. Courville. Loqa: Learning with opponent q-learning
awareness. arXiv preprint arXiv:2405.01035, 2024.
A. Ahmed. Evidence, decision and causality. Cambridge University Press, 2014.
A. Ahmed. Evidential decision theory. Cambridge University Press, 2021.
A. Al-Nowaihi and S. Dhami. Evidential equilibria: Heuristics and biases in static games of complete
information. Games, 6(4):637–676, 2015.
I. Antonoglou, J. Schrittwieser, S. Ozair, T. K. Hubert, and D. Silver. Planning in stochastic environments
with a learned model. In International Conference on Learning Representations, 2021.
R. J. Aumann. Subjectivity and correlation in randomized strategies. Journal of mathematical
Economics, 1(1):67–96, 1974.
M. Barasz, P. Christiano, B. Fallenstein, M. Herreshoff, P. LaVictoire, and E. Yudkowsky. Robust
cooperation in the prisoner’s dilemma: Program equilibrium via provability logic. arXiv preprint
arXiv:1401.5577, 2014.
D. Blackwell and L. Dubins. Merging of opinions with increasing information. The Annals of Mathematical Statistics, 33(3):882–886, 1962.
J. Bornschein, Y. Li, and A. Rannen-Triki. Transformers for supervised online continual learning. arXiv
preprint arXiv:2403.01554, 2024.
S. J. Brams. Newcomb’s problem and prisoners’ dilemma. Journal of Conflict Resolution, 19(4):
596–612, 1975.
T. Brown, B. Mann, N. Ryder, M. Subbiah, J. D. Kaplan, P. Dhariwal, A. Neelakantan, P. Shyam,
G. Sastry, A. Askell, S. Agarwal, A. Herbert-Voss, G. Krueger, T. Henighan, R. Child, A. Ramesh,
D. Ziegler, J. Wu, C. Winter, C. Hesse, M. Chen, E. Sigler, M. Litwin, S. Gray, B. Chess, J. Clark,
C. Berner, S. McCandlish, A. Radford, I. Sutskever, and D. Amodei. Language models are few-shot
learners. Advances in Neural Information Processing Systems, 33, 2020.
E. Catt, J. Grau-Moya, M. Hutter, M. Aitchison, T. Genewein, G. Deletang, K. Li, and J. Veness.
Self-predictive universal ai. Advances in Neural Information Processing Systems, 36:27181–27198,
2023.
G. Chalkiadakis and C. Boutilier. Coordination in multiagent reinforcement learning: A bayesian
approach. In Proceedings of the second international joint conference on Autonomous agents and
multiagent systems, pages 709–716, 2003.
P. Chaudhari and S. Soatto. Stochastic gradient descent performs variational inference, converges to
limit cycles for deep networks. In 2018 Information Theory and Applications Workshop (ITA), pages
1–10. IEEE, 2018.
M. K. Cohen, E. Catt, and M. Hutter. A strongly asymptotically optimal agent in general environments.
In Proceedings of the Twenty-Eighth International Joint Conference on Artificial Intelligence, IJCAI-19,
pages 2179–2186. International Joint Conferences on Artificial Intelligence Organization, 7 2019.
doi: 10.24963/ijcai.2019/302. URL https://doi.org/10.24963/ijcai.2019/302.

76

M. K. Cohen, E. Catt, and M. Hutter. Curiosity killed or incapacitated the cat and the asymptotically
optimal agent. IEEE Journal on Selected Areas in Information Theory, 2(2):665–677, 2021.
R. C. Conant and W. Ross Ashby. Every good regulator of a system must be a model of that system.
International journal of systems science, 1(2):89–97, 1970.
V. P. Crawford, M. A. Costa-Gomes, and N. Iriberri. Structural models of nonequilibrium strategic
thinking: Theory, evidence, and applications. Journal of Economic Literature, 51(1):5–62, 2013.
A. Critch. A parametric, resource-bounded generalization of löb’s theorem, and a robust cooperation
criterion for open-source game theory. The Journal of Symbolic Logic, 84(4):1368–1381, 2019.
A. Dafoe, Y. Bachrach, G. Hadfield, E. Horvitz, K. Larson, and T. Graepel. Cooperative ai: machines
must learn to find common ground. Nature, 593(7857):33–36, 2021.
A. De Silva, R. Ramesh, R. Yang, S. Yu, J. T. Vogelstein, and P. Chaudhari. Prospective learning:
Learning for a dynamic future. Advances in Neural Information Processing Systems, 37:123055–
123090, 2024.
A. Demski and S. Garrabrant. Embedded agency. arXiv preprint arXiv:1902.09469, 2019.
D. C. Dennett. Freedom evolves. Penguin, 2004.
J. A. Duque, M. Aghajohari, T. Cooijmans, R. Ciuca, T. Zhang, G. Gidel, and A. Courville. Advantage
alignment algorithms. arXiv preprint arXiv:2406.14662, 2024.
E. Elmoznino, T. Marty, T. Kasetty, L. Gagnon, S. Mittal, M. Fathi, D. Sridhar, and G. Lajoie. In-context
learning and occam’s razor. arXiv preprint arXiv:2410.14086, 2024.
T. Everitt, J. Leike, and M. Hutter. Sequential extensions of causal and evidential decision theory. In
International Conference on Algorithmic Decision Theory, pages 205–221. Springer, 2015.
B. Fallenstein, N. Soares, and J. Taylor. Reflective variants of solomonoff induction and aixi. In
International Conference on Artificial General Intelligence, pages 60–69. Springer, 2015a.
B. Fallenstein, J. Taylor, and P. F. Christiano. Reflective oracles: A foundation for game theory in
artificial intelligence. In International Workshop on Logic, Rationality and Interaction, pages 411–415.
Springer, 2015b.
K. Fan. Fixed-point and minimax theorems in locally convex topological linear spaces. Proceedings of
the National Academy of Sciences, 38(2):121–126, 1952. doi: 10.1073/pnas.38.2.121.
J. Foerster, R. Y. Chen, M. Al-Shedivat, S. Whiteson, P. Abbeel, and I. Mordatch. Learning with
opponent-learning awareness. In International Conference on Autonomous Agents and Multiagent
Systems, 2018.
D. P. Foster and H. P. Young. On the impossibility of predicting the behavior of rational agents.
Proceedings of the National Academy of Sciences, 98(22):12848–12853, 2001.
T. Gemini, R. Anil, S. Borgeaud, Y. Wu, J.-B. Alayrac, J. Yu, R. Soricut, J. Schalkwyk, A. M. Dai,
A. Hauth, and others. Gemini: a family of highly capable multimodal models. arXiv preprint
arXiv:2312.11805, 2023.
A. Gibbard and W. L. Harper. Counterfactuals and two kinds of expected utility. In Ifs: Conditionals,
belief, decision, chance and time, pages 153–190. Springer, 1978.
77

M. S. Graziano. Consciousness and the social brain. Oxford University Press, 2013.
M. S. Graziano and T. W. Webb. The attention schema theory: a mechanistic account of subjective
awareness. Frontiers in psychology, 6:500, 2015.
D. Guo, D. Yang, H. Zhang, J. Song, R. Zhang, R. Xu, Q. Zhu, S. Ma, P. Wang, X. Bi, et al. Deepseek-r1:
Incentivizing reasoning capability in llms via reinforcement learning. Nature, 2025.
J. Y. Halpern and R. Pass. Game theory with translucent players. International Journal of Game Theory,
47(3):949–976, 2018.
N. J. Hay. Universal semimeasures: An introduction. Master’s thesis, The University of Auckland,
2007.
D. Hofstadter. Dilemmas for superrational thinkers, leading up to a luring lottery. Scientific American,
248(6):739–755, 1983.
D. R. Hofstadter. I am a strange loop. Basic books, 2007.
J. V. Howard. Cooperation in the prisoni. Theory and Decision, 24(3):203, 1988.
R. A. Howard. Information value theory. IEEE Transactions on systems science and cybernetics, 2(1):
22–26, 1966.
D. Huh and P. Mohapatra. Multi-agent reinforcement learning: A comprehensive survey. arXiv preprint
arXiv:2312.10256, 2023.
M. Hutter. A theory of universal artificial intelligence based on algorithmic complexity. CoRR,
cs.AI/0004001, 2000. URL https://arxiv.org/abs/cs/0004001.
M. Hutter. Self-optimizing and pareto-optimal policies in general environments based on bayesmixtures. In J. Kivinen and R. H. Sloan, editors, Computational Learning Theory, pages 364–379,
Berlin, Heidelberg, 2002. Springer Berlin Heidelberg. ISBN 978-3-540-45435-9.
M. Hutter. Optimality of universal bayesian sequence prediction for general loss and alphabet. Journal
of Machine Learning Research, 4(Nov):971–1000, 2003.
M. Hutter. Universal artificial intelligence: Sequential decisions based on algorithmic probability. Springer
Science & Business Media, 2005.
M. Hutter. Open problems in universal induction & intelligence. Algorithms, 2(3):879–906, 2009.
M. Hutter, D. Quarel, and E. Catt. An Introduction to Universal Artificial Intelligence. 2024. URL
http://www.hutter1.net/ai/uaibook2.htm.
R. C. Jeffrey. The Logic of Decision. University of Chicago Press, 1990.
J. M. Joyce. The foundations of causal decision theory. Cambridge University Press, 1999.
E. Kalai and E. Lehrer. Rational learning leads to nash equilibrium. Econometrica: Journal of the
Econometric Society, pages 1019–1045, 1993a.
E. Kalai and E. Lehrer. Subjective equilibrium in repeated games. Econometrica: journal of the
Econometric Society, pages 1231–1240, 1993b.
E. Kalai and E. Lehrer. Subjective games and equilibria. Games and economic behavior, 8(1):123–163,
1995.
78

A. Khan, T. Willi, N. Kwan, A. Tacchetti, C. Lu, E. Grefenstette, T. Rocktäschel, and J. N. Foerster.
Scaling opponent shaping to high dimensional games. In International Conference on Autonomous
Agents and Multiagent Systems, 2024.
S. C. Kleene. Introduction to metamathematics. 1952.
M. Kleiman-Weiner, A. Vientós, D. G. Rand, and J. B. Tenenbaum. Evolving general cooperation with
a bayesian theory of mind. Proceedings of the National Academy of Sciences, 122(25):e2400993122,
2025.
E. Lehrer and R. Smorodinsky. Compatible measures and merging. Mathematics of Operations Research,
21(3):697–706, 1996.
J. Leike. Nonparametric general reinforcement learning. PhD thesis, The Australian National University
(Australia), 2016.
J. Leike and M. Hutter. On the computability of aixi. arXiv preprint arXiv:1510.05572, 2015a.
J. Leike and M. Hutter. Bad universal priors and notions of optimality. In Conference on Learning
Theory, pages 1244–1259. PMLR, 2015b.
J. Leike and M. Hutter. On the computability of solomonoff induction and knowledge-seeking. In
International Conference on Algorithmic Learning Theory, pages 364–378. Springer, 2015c.
J. Leike, T. Lattimore, L. Orseau, and M. Hutter. Thompson sampling is asymptotically optimal in
general environments. arXiv preprint arXiv:1602.07905, 2016a.
J. Leike, J. Taylor, and B. Fallenstein. A formal solution to the grain of truth problem. arXiv preprint
arXiv:1609.05058, 2016b.
D. Lewis. Prisoners’ dilemma is a newcomb problem. Philosophy & Public Affairs, pages 235–240,
1979.
D. Lewis. Causal decision theory. Australasian Journal of Philosophy, 59(1):5–30, 1981.
M. Li and P. Vitányi. An Introduction to Kolmogorov Complexity and Its Applications. Springer
International Publishing, Cham, 2019.
M. Li, P. Vitányi, et al. An introduction to Kolmogorov complexity and its applications, volume 3.
Springer, 2008.
C. List. Free will, determinism, and the possibility of doing otherwise. Noûs, 48(1):156–178, 2014.
G.-H. Liu and E. A. Theodorou. Deep learning theory review: An optimal control and dynamical
systems perspective. arXiv preprint arXiv:1908.10920, 2019.
C. Lu, T. Willi, C. A. S. De Witt, and J. Foerster. Model-free opponent shaping. In International
Conference on Machine Learning, 2022.
S. Mandt, M. D. Hoffman, and D. M. Blei. Stochastic gradient descent as approximate bayesian
inference. Journal of Machine Learning Research, 18(134):1–35, 2017.
A. Meulemans, S. Kobayashi, J. von Oswald, N. Scherrer, E. Elmoznino, B. Richards, G. Lajoie,
J. Sacramento, et al. Multi-agent cooperation through learning-aware policy gradients. arXiv
preprint arXiv:2410.18636, 2024.

79

J. H. Nachbar. Prediction, optimization, and learning in repeated games. Econometrica: Journal of the
Econometric Society, pages 275–309, 1997.
J. H. Nachbar. Beliefs in repeated games. Econometrica, 73(2):459–480, 2005.
J. F. Nash Jr. Equilibrium points in n-person games. Proceedings of the National Academy of Sciences,
36(1):48–49, 1950.
R. Nozick. Newcomb’s problem and two principles of choice. In Essays in honor of carl g. hempel: A
tribute on the occasion of his sixty-fifth birthday, pages 114–146. Springer, 1969.
P. Odifreddi. Classical Recursion Theory: The Theory of Functions and Sets of Natural Numbers.
Number Bd. 2 in Classical Recursion Theory. North-Holland, 1989. ISBN 9780444502056. URL
https://books.google.ch/books?id=Z97uAAAAMAAJ.
C. Oesterheld. Robust program equilibrium. Theory and Decision, 86(1):143–159, 2019.
C. Oesterheld, J. Treutlein, R. B. Grosse, V. Conitzer, and J. Foerster. Similarity-based cooperative
equilibrium. Advances in Neural Information Processing Systems, 36, 2024.
T. OpenAI, J. Achiam, S. Adler, S. Agarwal, L. Ahmad, I. Akkaya, F. L. Aleman, D. Almeida, J. Altenschmidt, S. Altman, S. Anadkat, et al. Gpt-4 technical report. arXiv preprint arXiv:2303.08774,
2023.
L. Orseau. Optimality issues of universal greedy agents with static priors. In M. Hutter, F. Stephan,
V. Vovk, and T. Zeugmann, editors, Algorithmic Learning Theory, pages 345–359, Berlin, Heidelberg,
2010a. Springer Berlin Heidelberg. ISBN 978-3-642-16108-7.
L. Orseau. Optimality issues of universal greedy agents with static priors. In International Conference
on Algorithmic Learning Theory, pages 345–359. Springer, 2010b.
L. Orseau. Asymptotic non-learnability of universal agents with computable horizon functions.
Theoretical Computer Science, 473:149–156, 2013. ISSN 0304-3975. doi: https://doi.org/10.
1016/j.tcs.2012.10.014. URL https://www.sciencedirect.com/science/article/pii/
S0304397512009358. Special Issue on Algorithmic Learning Theory.
L. Orseau and M. Ring. Self-modification and mortality in artificial agents. In International Conference
on Artificial General Intelligence, pages 1–10. Springer, 2011.
L. Orseau and M. Ring. Space-time embedded intelligence. In Artificial General Intelligence: 5th
International Conference, AGI 2012, Oxford, UK, December 8-11, 2012. Proceedings 5, pages 209–218.
Springer, 2012.
P. A. Ortega, J. X. Wang, M. Rowland, T. Genewein, Z. Kurth-Nelson, R. Pascanu, N. Heess, J. Veness, A. Pritzel, P. Sprechmann, et al. Meta-learning of sequential strategies. arXiv preprint
arXiv:1905.03030, 2019.
L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. Wainwright, P. Mishkin, C. Zhang, S. Agarwal, K. Slama,
A. Ray, et al. Training language models to follow instructions with human feedback. Advances in
neural information processing systems, 35:27730–27744, 2022.
J. Pearl. Causality. Cambridge university press, 2009.
H. Reichenbach. The direction of time, volume 65. Univ of California Press, 1991.

80

J. Richens, T. Everitt, and D. Abel. General agents need world models. In Forty-second International
Conference on Machine Learning, 2025.
H. Rogers Jr. Theory of recursive functions and effective computability. MIT press, 1987.
T. W. Sandholm and R. H. Crites. Multiagent reinforcement learning in the iterated prisoner’s dilemma.
Biosystems, 37(1-2):147–166, 1996.
J. Schmidhuber. Ultimate cognition à la gödel. Cognitive Computation, 1(2):177–193, 2009.
J. Schrittwieser, I. Antonoglou, T. Hubert, K. Simonyan, L. Sifre, S. Schmitt, A. Guez, E. Lockhart,
D. Hassabis, T. Graepel, et al. Mastering atari, go, chess and shogi by planning with a learned
model. Nature, 588(7839):604–609, 2020.
Y. Shoham and K. Leyton-Brown. Multiagent systems: Algorithmic, game-theoretic, and logical foundations. Cambridge University Press, 2008.
D. Silver, J. Schrittwieser, K. Simonyan, I. Antonoglou, A. Huang, A. Guez, T. Hubert, L. Baker, M. Lai,
A. Bolton, et al. Mastering the game of go without human knowledge. nature, 550(7676):354–359,
2017.
D. Silver, T. Hubert, J. Schrittwieser, I. Antonoglou, M. Lai, A. Guez, M. Lanctot, L. Sifre, D. Kumaran,
T. Graepel, et al. A general reinforcement learning algorithm that masters chess, shogi, and go
through self-play. Science, 362(6419):1140–1144, 2018.
B. F. Skinner. ’superstition’in the pigeon. Journal of experimental psychology, 38(2):168, 1948.
R. Solomonoff. Complexity-based induction systems: Comparisons and convergence theorems. IEEE
Transactions on Information Theory, 24(4):422–432, 1978. doi: 10.1109/TIT.1978.1055913.
W. Spohn. Dependency equilibria and the causal structure of decision and game situation. 2003.
W. Spohn. Dependency equilibria. Philosophy of Science, 74(5):775–789, 2007.
T. F. Sterkenburg. Putnam’s diagonal argument and the impossibility of a universal learning machine.
Erkenntnis, 84(3):633–656, 2019.
R. S. Sutton. Learning to predict by the methods of temporal differences. Machine learning, 3(1):
9–44, 1988.
R. S. Sutton and A. Barto. Reinforcement learning: An introduction. MIT Press, 2018.
T. Team Gemini, R. Anil, S. Borgeaud, J.-B. Alayrac, J. Yu, R. Soricut, J. Schalkwyk, A. M. Dai,
A. Hauth, K. Millican, et al. Gemini: a family of highly capable multimodal models. arXiv preprint
arXiv:2312.11805, 2023.
M. Tennenholtz. Program equilibrium. Games and Economic Behavior, 49(2):363–373, 2004.
E. L. Thorndike. Animal intelligence, 1898.
J. Uesato, N. Kushman, R. Kumar, F. Song, N. Siegel, L. Wang, A. Creswell, G. Irving, and I. Higgins. Solving math word problems with process-and outcome-based feedback. arXiv preprint
arXiv:2211.14275, 2022.
O. Vinyals, I. Babuschkin, W. M. Czarnecki, M. Mathieu, A. Dudzik, J. Chung, D. H. Choi, R. Powell,
T. Ewalds, P. Georgiev, et al. Grandmaster level in starcraft ii using multi-agent reinforcement
learning. nature, 575(7782):350–354, 2019.
81

J. Von Oswald, E. Niklasson, E. Randazzo, J. Sacramento, A. Mordvintsev, A. Zhmoginov, and M. Vladymyrov. Transformers learn in-context by gradient descent. In International Conference on Machine
Learning, pages 35151–35174. PMLR, 2023a.
J. Von Oswald, M. Schlegel, A. Meulemans, S. Kobayashi, E. Niklasson, N. Zucchet, N. Scherrer, N. Miller,
M. Sandler, M. Vladymyrov, et al. Uncovering mesa-optimization algorithms in transformers. arXiv
preprint arXiv:2309.05858, 2023b.
I. Wood, P. Sunehag, and M. Hutter. (Non-)equivalence of universal priors. In Proc. Solomonoff 85th
Memorial Conference, volume 7070 of LNAI, pages 417–425, Melbourne, Australia, 2011. Springer.
ISBN 978-3-642-44957-4. doi: 10.1007/978-3-642-44958-1_33. URL http://arxiv.org/abs/
1111.3854.
C. Wyeth and M. Hutter. Formalizing embeddedness failures in universal artificial intelligence. arXiv
preprint arXiv:2505.17882, 2025.
C. Wyeth, M. Hutter, J. Leike, and J. Taylor. Limit-computable grains of truth for arbitrary computable
extensive-form (un) known games. arXiv preprint arXiv:2508.16245, 2025.
S. M. Xie, A. Raghunathan, P. Liang, and T. Ma. An explanation of in-context learning as implicit
bayesian inference. arXiv preprint arXiv:2111.02080, 2021.
E. Yudkowsky and N. Soares. Functional decision theory: A new theory of instrumental rationality.
arXiv preprint arXiv:1710.05060, 2017.
J. Zhao and J. Schmidhuber. Incremental self-improvement for life-time multi-agent reinforcement
learning. In From Animals to Animats 4: Proceedings of the Fourth International Conference on Simulation of Adaptive Behavior, Cambridge, MA, pages 516–525. MIT Press, Bradford Books Cambridge,
MA, 1996.
A. K. Zvonkin and L. A. Levin. The complexity of finite objects and the development of the concepts of
information and randomness by means of the theory of algorithms. Russian Mathematical Surveys,
25(6):83–124, 1970.

82

A. Table of notations and definitions
Symbol

Description

Single-Agent Setting
A
E
æ
AE
æ1:𝑡
æ<𝑡
æ∗

Set of possible actions.
Set of possible percepts (Observations × Rewards).
A single turn (action-percept pair).
The set of all possible turns (A × E).
A 𝑡 -turn history.
A history up to, but not including, time 𝑡 .
An arbitrary-length finite history.

𝜇
𝜈
𝜉

Ground-truth environment.
Generic environment.
Mixture of environments; the decoupled agent’s belief model.

𝜐
𝜆
𝜌

Ground-truth universe.
Generic universe.
Mixture of universes; the embedded agent’s belief model.

𝜋
𝜋
𝜁

Ground-truth policy.
Generic policy. Note: overloading notation with ground-truth policy.
Mixture of policies.

𝜈𝜋
𝜌𝜋

Universe, i.e., measure over histories, resulting from combining 𝜈 and 𝜋
Universe resulting from replacing self-model of 𝜌 with 𝜋 (cf. equation 9).

𝑉𝜈𝜋 (æ1:𝑡 )
𝑉𝜆 (æ1:𝑡 )
𝑄 𝜈𝜋 (æ<𝑡 , 𝑎𝑡 )
𝑄 𝜆 (æ<𝑡 , 𝑎𝑡 )

Value of history æ1:𝑡 w.r.t. policy 𝜋 and environment 𝜈.
Value of history æ1:𝑡 w.r.t. universe 𝜆 .
𝑄 -value of action 𝑎𝑡 after history æ<𝑡 w.r.t. policy 𝜋 and environment 𝜈.
𝑄 -value of action 𝑎𝑡 after history æ<𝑡 w.r.t. universe 𝜆 .

Mpol
Menv
Muni

Class of policies.
Class of environments.
Class of universes.

Multi-Agent Setting
Ā
Ē
æ
æ1:𝑡
æ∗
𝑖
æ1:
𝑡
−𝑖
𝑎− 𝑖
𝜇
𝜈
𝜋
𝜋
𝜈𝑖
𝑖
( 𝜈𝑖 ) 𝜋

Joint action space.
Joint percept space.
A single multi-agent turn.
A 𝑡 -turn multi-agent history.
An arbitrary-length finite multi-agent history.
The personal history for agent 𝑖.
[ 𝑁 ]/𝑖: the indices of the other agents.
The joint action of all agents except agent 𝑖.
Ground-truth multi-agent environment.
Generic multi-agent environment.
Ground-truth multi-agent policy.
Generic multi-agent policy. Note: overloading notation with ground-truth multi-agent policy.
Personal environment resulting from combining 𝜈 with other agent’s policies.
𝑖
Personal distribution over personal histories æ1:
.
𝑡

Game-Theoretic Concepts (Section 4)
𝑎
¯1:𝑡
𝑎
¯<𝑡
𝑎
¯∗

Repeated game history.
Repeated game history up to time 𝑡 .
Arbitrary-length repeated game history.

83

Symbol

Description

𝜇
¯æ<𝑡
𝜇 æ𝑖
<𝑡
𝜋æ𝑖
<𝑡
𝜉æ 𝑖
<𝑡
𝜌æ𝑖

Tail multi-agent ground-truth environment.
Tail personal ground-truth environment.
Tail ground-truth policy.
Tail mixture environment.
Tail mixture universe.

NE
SNE
CE
SCE
EE
SEE
CEE
SCEE

Nash Equilibrium.
Subjective Nash Equilibrium.
Correlated Equilibrium.
Subjective Correlated Equilibrium.
Embedded Equilibrium.
Subjective Embedded Equilibrium.
Correlated Embedded Equilibrium.
Subjective Correlated Embedded Equilibrium.

<𝑡

Universal AI & MUPI (Section 5)
M LSCSM
M APOM
M rAPOM
𝑂𝜏
𝜏

RUI
RO
𝜌𝑤
𝜏
𝜌𝜏
𝑤,𝜏 −RUI
Muni
𝜏 −RO
Muni
𝑤
𝜌
¯𝜏-RO

Class of lower semicomputable semimeasures.
Class of Abstract Probabilistic Oracle Machines.
Class of restricted APOMs.
A probabilistic oracle.
A probabilistic oracle.
Reflective Universal Inductor.
Reflective Oracle.
The ( 𝑤, 𝜏)-universal mixture (the RUI).
The Solomonoff 𝜏-universal mixture.
Hypothesis class of universes with RUI.
Hypothesis class of universes with Reflective Oracle.
𝜏-completed universal mixture (for RO).

Functional Similarity (Sections 3.6 & 5.4)
𝑆 ( 𝜆, 𝑤)
𝑆 ( 𝑤)
I𝑤 ( 𝜋; 𝜈)
𝑤𝑈,𝜏 ( 𝜆 )
𝐾𝑈 (⟨ 𝑀 ⟩)
𝐾𝑈 ( 𝜆 )
𝐾𝑈 ( 𝜋)
𝐾𝑈 ( 𝜈)
𝑤
ˇ 𝑈,𝜏 ( 𝜆 )
𝑆ˇ( 𝜆, 𝑈, ⟨·⟩)

Degree of functional similarity (pointwise mutual information).
Average degree of functional similarity.
Shannon mutual information between policy and environment.
Solomonoff prior over universes (induced by universal monotone Turing machine 𝑈 and 𝜏).
Kolmogorov complexity of the binary encoding ⟨ 𝑀 ⟩ of a machine 𝑀 .
Kolmogorov complexity of a universe 𝜆 .
Kolmogorov complexity of a policy 𝜋.
Kolmogorov complexity of an environment 𝜈.
Renormalized Solomonoff prior over fully supported universes.
Algorithmic degree of functional similarity (Section 5.4).

Reference

Definition Name

Definition 2.1
Definition 2.2
Definition 2.3
Definition 2.7
Definition 2.8
Definition 2.9
Definition 2.10
Definition 3.1
Definition 3.2

(Semimeasures and measures)
(Total variation distance)
(Dominance)
(Computable)
(Lower semicomputable)
(Limit computable)
(Monotone Turing machine)
(A grain of uncertainty)
(Embedded best response)
84

Reference

Definition Name

Definition 3.5
Definition 3.9
Definition 3.10
Definition 3.16
Definition 4.1
Definition 4.2
Definition 4.3
Definition 4.4
Definition 4.5
Definition 4.7
Definition 4.8
Definition 4.10
Definition 4.11
Definition 4.14
Definition 4.15
Definition 4.19
Definition 4.23
Definition 4.27
Definition 4.30
Definition 4.32
Definition 5.2
Definition 5.3
Definition 5.4
Definition 5.5
Definition 5.6
Definition 5.7
Definition 5.9
Definition 5.10
Definition 5.11
Definition 5.19
Definition 5.22
Definition 5.23
Definition 5.24
Definition 5.26
Definition 5.34
Definition 5.35

(One-step planner embedded Bayesian agent)
(𝑘-step planner embedded Bayesian agent)
(The grain-of-truth property)
(Fully supported universe)
(Repeated Games with Perfect Monitoring)
(Decoupled Bayes-optimal agent in repeated games)
(Subjective Nash Equilibrium)
(Nash Equilibrium)
(Tail games)
(Correlated Equilibria)
(Subjective Correlated Equilibria (Kalai and Lehrer, 1995))
(Embedded Bayes-optimal agent in repeated games)
(𝜖-Subjective Embedded Equilibrium)
(Conditional Completion)
(Subjective Embedded Equilibrium)
(Embedded Equilibrium)
(𝜖-Embedded Equilibrium)
(𝜖-Subjective Correlated Embedded Equilibrium)
(( 𝜖, 𝛿)-Subjective Correlated Embedded Equilibrium (( 𝜖, 𝛿)-SCEE))
(( 𝑘𝑡 , 𝜖𝑡 )-embedded Bayesian agent)
(prefix free encoding)
(Probabilistic oracle)
(APOM)
(POM)
(rAPOM)
(rPOM)
(Universal mixture universe)
(Solomonoff universal prior)
(𝑤-reflective universal inductor oracle)
(Reflective oracle (Fallenstein et al., 2015a,b))
(𝜏-completion)
(𝜏-estimable (Wyeth et al., 2025))
(𝜏-lower-semicomputable)
(𝜏-sampleable (Wyeth et al., 2025))
(Fully supported universe)
𝜏
(Coupledness and decoupledness on M̌pol-env
)

B. Preliminaries
This appendix covers the theoretical preliminaries. We begin by reviewing foundational concepts:
measure-theoretic notions for random sequences (Appendix B.1), universal Bayesian prediction and
the merging of opinions theorem (Appendix B.2), computability and algorithmic information theory
(Appendix B.3), and Solomonoff ’s theory of induction (Appendix B.4). We then apply these to
reinforcement learning, defining the general setup (Appendix B.5) and the universally intelligent
agent AIXI (Hutter, 2000) (Appendix B.6). We conclude by motivating our framework, first by
discussing the failure of AIXI in embedded settings (Appendix B.7), and second by reviewing JAIXI, a
variant introduced by Wyeth and Hutter (2025) to formalize these embedding failures (Appendix B.8).

85

B.1. Measure-theoretic concepts.
Let X be an arbitrary countable set. We generally think of X as an alphabet and refer to its elements
as symbols.
Definition B.1. A semiprobability distribution65 on X is a mapping 𝜎 : X → [0, 1] such that
∑︁
𝜎(𝑥) ≤ 1 .
𝑥∈X

If the above holds with equality, we get a probability distribution.
We denote the set of semiprobability distributions on X as Δ′ X, and the set of probability distributions
as ΔX.
A semiprobability distribution 𝜎 on X can be turned into a probability distribution on
X̃ := X ∪ {⊥}
by assigning the missing probability mass 1 −
X:

Í

(32)

𝑥 ∈ X 𝜎 ( 𝑥 ) to a symbol ‘⊥’ which is assumed to be outside

Definition B.2. We define the canonical completion of a semiprobability distribution 𝜎 ∈ Δ′ X as the
probability distribution 𝜎˜ ∈ ΔX̃ on X̃ := X ∪ {⊥} defined as:
𝜎
˜( 𝑥 ) = 𝜎 ( 𝑥 ) ,
𝜎
˜ (⊥) = 1 −

∑︁

∀𝑥 ∈ X ,
𝜎(𝑥) .

𝑥∈X

Remark B.3. The above definition motivates the interpretation of a semiprobability distribution
𝜎 ∈ Δ′ X as formally describing a situation where it is possible to observe a (random) sample from X
but it is also possible not to observe any sample from X.
We write X ∗ to denote the set of finite X-sequences, i.e.,
Ø
X ∗ :=
X𝑛 .
𝑛 ≥0

We adopt the convention that X 0 = {𝜀} where 𝜀 is the empty sequence/string.
For 𝑥 ∈ X 𝑛 and 𝑦 ∈ X 𝑚 , we write 𝑥 𝑦 to denote the sequence in X 𝑛+𝑚 obtained by concatenating 𝑥
and 𝑦 .
We write66 X ∞ := X ℕ to denote the set of infinite X-sequences, and X # := X ∗ ∪ X ∞ to denote the set
of all (finite and infinite) sequences. For 𝑥, 𝑦 ∈ X # , we write 𝑥 ⊑ 𝑦 to denote that 𝑥 is a prefix of 𝑦 .
For any sequence 𝑥 ∈ X # , we denote the (possibly infinite) length of 𝑥 as 𝑙 ( 𝑥 ), and for every 1 ≤ 𝑖 ≤ 𝑙 ( 𝑥 ),
we denote the 𝑖-th symbol of 𝑥 as 𝑥 𝑖 . For 1 ≤ 𝑖 ≤ 𝑗 ≤ 𝑙 ( 𝑥 ) we write 𝑥 𝑖: 𝑗 to denote the subsequence
( 𝑥 𝑖 , . . . , 𝑥 𝑗 ). We use the notation 𝑥 ≤ 𝑡 and 𝑥 <𝑡 as a shorthand for 𝑥1:𝑡 and 𝑥1:𝑡 −1 , respectively. We also
use the notation 𝑥 >𝑡 and 𝑥 ≥ 𝑡 as a shorthand for 𝑥𝑡+1:𝑙 ( 𝑥 ) and 𝑥𝑡:𝑙 ( 𝑥 ) , respectively.
65 A more general definition that is typically used is to consider mappings Pow(X) → [0, 1] which are 𝜎-superadditive;

the simpler definition here is sufficient for our purposes.
66 Note that 𝐴 𝐵 denotes the set of mappings from 𝐵 to 𝐴. Therefore, X ℕ is the set of infinite sequences in X with indices
in ℕ.

86

Definition B.4. (Cf., e.g., Hutter et al. (2024)) A semimeasure on X ∞ is a mapping 𝜎 : X ∗ → ℝ+
satisfying67 :
1. 𝜎 ( 𝜀) ≤ 1, and
∑︁
2. 𝜎 ( 𝑥 ) ≥
𝜎 ( 𝑥𝑢) , ∀𝑥 ∈ X ∗ .
𝑢∈ X

If the above two conditions hold with equality, we say that 𝜎 is a measure.68
We call a semimeasure 𝜎 initially-normalized69 if it satisfies 𝜎 ( 𝜀) = 1.
A semimeasure for which 𝜎 ( 𝜀) = 0 is said to be trivial. All semimeasures we consider in this paper are
non-trivial.
We emphasize that for an initially-normalized semimeasure 𝜎, the value of 𝜎 ( 𝑥 ) for 𝑥 ∈ X ∗ is not
supposed to represent the probability of observing the substring 𝑥 , but rather the probability of
observing a string having 𝑥 as a prefix. We elaborate on this in the following remark, where we
formally describe the intended interpretation of initially-normalized semimeasures.
Remark B.5. An initially-normalized semimeasure 𝜎 (i.e., one that satisfies 𝜎 ( 𝜀) = 1) can be viewed
as describing a random variable 𝑋𝜎 taking values in X # = X ∗ ∪ X ∞ , which satisfies
(
Í
𝜎 ( 𝑥 ) − 𝑢 ∈ X 𝜎 ( 𝑥𝑢) ,
if 𝑥 ∈ X ∗ ,
ℙ[ 𝑋𝜎 = 𝑥 ] =
lim𝑡→∞ 𝜎 ( 𝑥 ≤ 𝑡 ) ,
if 𝑥 ∈ X ∞ ,
and
ℙ[ 𝑥 ⊑ 𝑋𝜎 ] = 𝜎 ( 𝑥 ) .
In other words, 𝜎 ( 𝑥 ) represents the probability that 𝑥 is a prefix of 𝑋𝜎 .
Í
Under this interpretation of 𝜎, one can see that for 𝑥 ∈ X ∗ , 𝜎 ( 𝑥 ) > 𝑢 ∈ X 𝜎 ( 𝑥𝑢) if and only if ℙ[ 𝑋𝜎 =
𝑥 ] > 0. Hence, one can deduce that 𝜎 is a measure if and only if70 ℙ[ 𝑋𝜎 ∈ X ∞ ] = 1, i.e., almost surely,
the random sequence 𝑋 does not stop at any finite length.
Example B.6. Consider a probabilistic monotone Turing machine (i.e., a Turing machine with access
to an unlimited number of uniformly random coin flips) with a write-once output tape. Running this
machine gives rise to a (initially-normalized) semimeasure describing the state of the output tape
after running until halting or forever if it does not halt. This semimeasure becomes a full measure if
and only if the machine almost surely keeps writing symbols on the output tape, i.e., it neither halts
nor gets to a situation where it loops forever without writing further symbols on the output tape.
67 It is worth noting that from the second condition, one can show by induction on 𝑙 ( 𝑥 ) that 𝜎 ( 𝑥 ) ≤ 𝜎 ( 𝜀) for all 𝑥 ∈ X ∗ .

Combining this with the first property implies that 𝜎 ( 𝑥 ) ≤ 1 for all 𝑥 ∈ X ∗ , and hence 𝜎 can be seen as a mapping
X ∗ → [0, 1].
68 Here we use the terminology that is standard in the AIXI literature (e.g., Hutter et al. (2024)), which calls a measure
only 𝜎 which satisfies the mentioned equalities. A measure, according to this definition, induces a probability distribution
on infinite sequences, as we shall see in a moment.
69 The term "initially-normalized" is not standard. We coin this term to distinguish these types of semimeasures because
they have a nice intuitive interpretation, as we will see in Remark B.5. It is worth noting that our initially-normalized
semimeasures corresponds to the definition of semimeasures that is adopted in Hay (2007).
70 ℙ[ 𝑋 ∈ X ∞ ] = 1 is equivalent to ℙ[ 𝑋 ∈ X ∗ ] = 0, i.e., ℙ[ 𝑋 = 𝑥 ] = 0 for all 𝑥 ∈ X ∗ . By the definition of the probability
𝜎
𝜎
𝜎
Í
distribution of the random sequence, this is equivalent to having 𝜎 ( 𝑥 ) = 𝑢 ∈ X 𝜎 ( 𝑥𝑢) for all 𝑥 ∈ X ∗ , which would mean that
𝜎 is a measure as we already know that 𝜎 ( 𝜀) = 1.

87

Definition B.7. If 𝜎 is a semimeasure and 𝑥 ∈ X ∗ is such that 𝜎 ( 𝑥 ) > 0, then we can define a
conditional semimeasure 𝜎 (·| 𝑥 ) as follows:
𝜎( 𝑦 |𝑥) =

𝜎( 𝑥 𝑦)
,
𝜎(𝑥)

∀ 𝑦 ∈ X∗ .

If 𝜎 is a measure, then 𝜎 (·| 𝑥 ) is a measure as well.
The conditional (semi)measure can be intuitively interpreted as the conditional (semi)probability,
given that we have observed 𝑥 ∈ X ∗ so far, that 𝑥 will be extended with 𝑦 ∈ X ∗ .
It is possible to turn a semimeasure into a measure through normalization:
Definition B.8. For every semimeasure 𝜎, define the Solomonoff normalization 𝜎 of 𝜎 recursively as
𝜎 ( 𝜀) = 1 ,
𝜎 ( 𝑥𝑎) = 𝜎 ( 𝑥 ) · Í

𝜎 ( 𝑥𝑎)
,
𝑏 ∈ X 𝜎 ( 𝑥𝑏)

∀𝑎 ∈ X , ∀𝑥 ∈ X ∗ .

If the denominator is zero, then define the fraction arbitrarily in such a way that we get
1
𝜎 ( 𝑥 ) (e.g., 𝜎 ( 𝑥𝑎) = | X
| 𝜎 ( 𝑥 ) if X is finite).

Í

𝑎 ∈ X 𝜎 ( 𝑥𝑎) =

It is not hard to see that for every 𝑥 ∈ X ∗ and every 𝑎 ∈ X, we have
𝜎 ( 𝑎| 𝑥 ) = Í

𝜎 ( 𝑥𝑎)
,
𝑏 ∈ X 𝜎 ( 𝑥𝑏)

∀𝑎 ∈ X , ∀𝑥 ∈ X ∗ .

Furthermore, one can show by induction on 𝑙 ( 𝑥 ) that 𝜎 ( 𝑥 ) ≥ 𝜎 ( 𝑥 ) for all 𝑥 ∈ X ∗ .
If 𝜎 is an initially-normalized semimeasure (i.e., it satisfies 𝜎 ( 𝜀) = 1), then we can construct a
measure71 on X̃ ∞ inspired by the interpretation in Remark B.5. But before describing the construction,
it will be useful to introduce the notion of well-formed X̃-sequences:
Definition B.9. We call a (finite or infinite) sequence 𝑥˜ ∈ X̃ # a well-formed sequence if it satisfies
∀𝑡 ∈ ℕ, (˜
𝑥𝑡 =⊥) ⇒ (∀𝑡 ′ ≥ 𝑡, 𝑥˜𝑡′ =⊥) .
Equivalently,

∀𝑡 ∈ ℕ, (˜
𝑥𝑡 ∈ X) ⇒ (˜
𝑥 ≤𝑡 ∈ X∗) .

In other words, a symbol of X can never appear after the symbol ‘⊥’ in a well-formed sequence. We
denote the set of well-formed (possibly infinite) sequences as X̃ #,𝑤 𝑓 . We write X̃ ∗,𝑤 𝑓 := X̃ #,𝑤 𝑓 ∩ X̃ ∗
(resp., X̃ ∞,𝑤 𝑓 := X̃ #,𝑤 𝑓 ∩ X̃ ∞ ) to denote the set of finite (resp. infinite) well-formed X̃-sequences.
There is a canonical bijection 𝑥 ↦→ 𝑥˜∞,𝑤 𝑓 between X # and X̃ ∞,𝑤 𝑓 defined as:
• If 𝑥 ∈ X ∞ then 𝑥˜∞,𝑤 𝑓 = 𝑥 .
• If 𝑥 ∈ X ∗ , then 𝑥˜𝑡∞,𝑤 𝑓 = 𝑥𝑡 for 𝑡 ≤ 𝑙 ( 𝑥 ) and 𝑥˜𝑡∞,𝑤 𝑓 = ⊥ for 𝑡 > 𝑙 ( 𝑥 ).
Now we are ready to introduce the canonical completion of an initially-normalized semimeasure:
71 Recall that X̃ was defined as X ∪ {⊥} in equation 32.

88

Definition B.10. Let 𝜎 be an initially-normalized semimeasure on X ∞ , and let 𝑋 be the random
sequence in X # induced by 𝜎, as described in Remark B.5. We define the canonical completion 𝜎˜ of 𝜎
as the measure on well-formed X̃-sequences induced by the probability distribution of the infinite
sequence X̃ ∞,𝑤 𝑓 obtained by applying the canonical bijection 𝑥 ↦→ 𝑥˜∞,𝑤 𝑓 from X # to X̃ ∞,𝑤 𝑓 on 𝑋 .
Equivalently, we can define 𝜎˜ as follows:
• For 𝑥 ∈ X ∗ , we let 𝜎˜ ( 𝑥 ) = 𝜎 ( 𝑥 ).
• For 𝑥˜ ∈ X̃ ∗ \ X̃ ∗,𝑤 𝑓 , we let 𝜎˜ (˜
𝑥 ) = 0.
• For 𝑥˜ ∈ X̃ ∗,𝑤 𝑓 \ X ∗ (which necessarily means that 𝑥˜ is not the empty string and the last symbol
of 𝑥˜ must be ‘⊥’, i.e., 𝑡 := 𝑙 (˜
𝑥 ) > 0 and 𝑥˜𝑡 =⊥), we let
∑︁
𝜎
˜ (˜
𝑥) = 𝜎(𝑥) −
𝜎 ( 𝑥𝑥 ′ ) ,
𝑥′ ∈ X

where 𝑥 is the longest prefix of 𝑥˜ that lies in X ∗ , i.e., 𝑥 = arg max𝑙 ( 𝑥 ) { 𝑥 ∈ X ∗ : 𝑥 ⊑ 𝑥˜}.
Definition B.11. Let 𝜎1 and 𝜎2 be two measures. For every 𝑘 ≥ 1, we define the 𝑘-steps total-variation
distance between 𝜎1 and 𝜎2 as:
1 ∑︁
𝐷𝑘 ( 𝜎1 , 𝜎2 ) =
| 𝜎1 ( 𝑥 ) − 𝜎2 ( 𝑥 )| .
2
𝑘
𝑥∈X

It is easy to show that 𝐷𝑘+1 ( 𝜎1 , 𝜎2 ) ≥ 𝐷𝑘 ( 𝜎1 , 𝜎2 ). By taking 𝑘 → ∞, we get the total variation distance:
1 ∑︁
| 𝜎1 ( 𝑥 ) − 𝜎2 ( 𝑥 )| .
𝑘 ≥1 2
𝑘

𝐷∞ ( 𝜎1 , 𝜎2 ) = sup

𝑥∈X

If 𝜎1 and 𝜎2 are initially-normalized semimeasures, we define the 𝐷𝑘 and 𝐷∞ distances based on their
canonical completions as follows:
𝐷𝑘 ( 𝜎1 , 𝜎2 ) = 𝐷𝑘 (˜
𝜎1 , 𝜎
˜2 ) and 𝐷∞ ( 𝜎1 , 𝜎2 ) = 𝐷∞ (˜
𝜎1 , 𝜎
˜2 ) .

When we condition measures (or semimeasures) on some 𝑥 ∈ X ∗ , we use the shorthand notation
𝐷𝑘 ( 𝜎1 , 𝜎2 | 𝑥 ) and 𝐷∞ ( 𝜎1 , 𝜎2 | 𝑥 ) to denote 𝐷𝑘 ( 𝜎1 (·| 𝑥 ) , 𝜎2 (·| 𝑥 )) and 𝐷∞ ( 𝜎1 (·| 𝑥 ) , 𝜎2 (·| 𝑥 )), respectively.
Definition B.12. We say that a semimeasure 𝜎1 (multiplicatively) dominates a semimeasure 𝜎2 , and
×

write 𝜎1 ≥ 𝜎2 , if there exists 𝐶 > 0 such that 𝜎1 ( 𝑥 ) ≥ 𝐶 · 𝜎2 ( 𝑥 ) for all 𝑥 ∈ X ∗ .
×

×

×

We say that 𝜇 and 𝜎 are (multiplicatively) equivalent, and write 𝜇 = 𝜎, if we have 𝜇 ≥ 𝜎 and 𝜇 ≤ 𝜎.
B.2. Universal Bayesian prediction theory.
Assume that we are observing a random sequence 𝑥 ∈ X ∞ whose distribution is described by a
measure 𝜎. We do not know the measure 𝜎, but we know that it belongs to some class of measures
M which is countable. If we have observed the first 𝑡 symbols of 𝑥 (i.e., 𝑥 ≤ 𝑡 ), can we make accurate
predictions about the future 𝑥 >𝑡 ?
We solve this problem with a Bayesian approach. We assume a prior belief distribution 𝑤 ∈ ΔM and
define the mixture measure
∑︁
𝜉𝑤 =
𝑤𝜎 𝜎 .
𝜎∈ M

89

Here, 𝑤𝜎 represents the prior belief, before collecting any observation, that 𝜎 is the true measure
describing the distribution of 𝑥 ∈ X ∞ . After observing the first 𝑡 symbols of 𝑥 , our posterior belief
about 𝜎 becomes
𝑤𝜎 𝜎 ( 𝑥 ≤ 𝑡 )
𝑤𝜎 𝜎 ( 𝑥 ≤ 𝑡 )
𝑤 ( 𝜎 | 𝑥 ≤ 𝑡 ) := Í
= 𝑤
.
′
𝜉 ( 𝑥 ≤𝑡 )
𝜎′ ∈ M 𝑤𝜎′ 𝜎 ( 𝑥 ≤ 𝑡 )
Our posterior belief, given that we have already observed 𝑥 ≤ 𝑡 , that we will next observe 𝑦 ∈ X ∗ (i.e.,
our posterior belief that 𝑥𝑡+1:𝑡+𝑙 ( 𝑦 ) = 𝑦 ) is given by
∑︁
𝜎∈ M

𝑤(𝜎| 𝑥 ≤𝑡 )𝜎 ( 𝑦 | 𝑥 ≤𝑡 ) =

∑︁ 𝑤𝜎 𝜎 ( 𝑥 ≤ 𝑡 ) 𝜎 ( 𝑥 ≤ 𝑡 𝑦 )
𝜎∈ M

𝜉𝑤 ( 𝑥 ≤ 𝑡 ) 𝜎 ( 𝑥 ≤ 𝑡 )

=

∑︁ 𝑤𝜎 𝜎 ( 𝑥 ≤ 𝑡 𝑦 )
𝜎∈ M

𝜉𝑤 ( 𝑥 ≤ 𝑡 )

=

𝜉𝑤 ( 𝑥 ≤ 𝑡 𝑦 )
= 𝜉𝑤 ( 𝑦 | 𝑥 ≤ 𝑡 ) .
𝜉𝑤 ( 𝑥 ≤ 𝑡 )

Therefore, the conditional measure 𝜉𝑤 (·| 𝑥 ≤ 𝑡 ) of the mixture 𝜉𝑤 can be conveniently used to describe
our updated Bayesian predictions about the future.
Blackwell and Dubins showed that if 𝑤 satisfies 𝑤𝜎 > 0 for all 𝜎 ∈ M, then 𝜉𝑤 (·| 𝑥 ≤ 𝑡 ) almost surely converges to making correct predictions, as long as the ground-truth measure describing the distribution
of 𝑥 belongs to M. This motivates the following definition:
Definition B.13. We say that 𝑤 is a universal prior probability (resp., semiprobability) distribution
on M if 𝑤 ∈ ΔM (resp. 𝑤 ∈ Δ′ M) and 𝑤𝜎 > 0 for all 𝜎 ∈ M.
Theorem B.14 (Merging of opinions Blackwell and Dubins (1962)). For every universal prior 𝑤 ∈ ΔM
and every 𝜎 ∈ M, we have
lim 𝐷∞ ( 𝜉𝑤 , 𝜎 | 𝑥 ≤ 𝑡 ) = 0 ,

𝑡 →∞

𝜎 ( 𝑥 )-almost surely .

It is possible to generalize the above theorem to semimeasures72 by noticing the following facts:
• Every semimeasure 𝜎 on X ∞ is proportional to an initially-normalized semimeasure 𝜎i.n. (as we
can divide 𝜎 by 𝜎 ( 𝜀) > 0).
• 𝜎 and 𝜎i.n. have the same conditional semimeasures, i.e., 𝜎 (·| 𝑥 ) = 𝜎i.n. (·| 𝑥 ) for all 𝑥 ∈ X ∗ .
• A universal mixture of a collection of semimeasures on X ∞ can be seen as a universal mixture
of the corresponding initially-normalized measures on X ∞ , which can in turn be canonically
represented as a universal mixture over the collection of measures on X̃ ∞ through the canonical
completion procedure of Definition B.10.
By combining these facts, we can leverage the merging of opinions property for measures on X̃ ∞ to
prove a merging of opinions theorem for semimeasures on X ∞ :
Corollary B.15. (Merging of opinions for semimeasures) Let M be an arbitrary countable class of
semimeasures. For every universal semiprobability prior 𝑤 ∈ Δ′ M and every semimeasure 𝜎 ∈ M, we
have73
lim 𝐷∞ ( 𝜉𝑤 , 𝜎 | 𝑥 ≤ 𝑡 ) = 0 , 𝜎 ( 𝑥 )-almost surely ,
𝑡 →∞

where 𝜉 is the universal semimeasure mixture defined as
∑︁
𝜉𝑤 =
𝑤𝜎 𝜎 .
𝑤

𝜎∈ M
72 Recall that we only consider non-trivial semimeasures in this paper.

73When 𝜎 is a semimeasure, then the "𝜎 ( 𝑥 )-almost surely" notation can be understood in terms of the random sequence

𝑥 ∈ X # induced by the corresponding initially-normalized semimeasure 𝜎i.n. .

90

As we have seen so far, if the real distribution 𝜎 belongs to a class M, then Bayesian prediction
based on a universal mixture on M converges to making accurate predictions. A natural question
that arises is: What shall we choose as the class of (semi)measures M for our Bayesian mixture, so
that the assumption "𝜎 belongs to the class M" is least restrictive? Solomonoff proposed considering
the collection of all computable sequences. Solomonoff ’s approach can be extended to stochastic
sequences/processes by considering computable74 (semi)measures.
Before describing Solomonoff induction theory, it will be useful to recall some notions from computability theory and algorithmic information theory.
B.3. Useful notions from computability theory and algorithmic information theory.
Definition B.16. Let X and Y be two countable sets for each of which we presume a fixed canonical
encoding for their elements as finite binary strings. We say that a function 𝑓 : X → Y is computable
if there exists a Turing machine that computes 𝑓 using these encodings.
For example, the mapping 𝑞 ↦→ 𝑞2 from ℚ to itself is computable (presuming standard encoding of
rational numbers as binary strings).
Definition B.17. Let X be a countable set for which we presume a fixed canonical encoding for its
elements as binary strings. A function 𝑓 : X → ℝ is said be lower semicomputable (l.s.c.) if there
exists a computable function 𝜙 : X × ℕ → ℚ such that 𝜙 ( 𝑥, 𝑛) ≤ 𝜙 ( 𝑥, 𝑛 + 1) and lim𝑛→∞ 𝜙 ( 𝑥, 𝑛) = 𝑓 ( 𝑥 )
for all 𝑥 ∈ X.75
In the following, we describe useful notions from algorithmic information theory (e.g., Kolmogorov
complexity). For technical reasons, it will be useful to consider the following variants of Turing
machines:
Definition B.18. A monotone76 Turing machine is a Turing machine 𝑇 equipped with:
1. A unidirectional read-only input tape.
2. A unidirectional write-only output tape.
3. One or more bidirectional read/write working tapes initialized with zeros.
All tapes are binary (i.e., no blank symbols).
Definition B.19. We say that a monotone Turing machine 𝑇 halts on input 𝑝 ∈ {0, 1}∗ with output
𝑥 ∈ {0, 1}∗ , and write 𝑇 ( 𝑝) = 𝑥 , if by putting the string 𝑝 at the beginning of the input tape, the
machine will halt in a state where 𝑝 is at the left of the input cursor and 𝑥 will be at the left of the
output cursor. I.e., the machine will read 𝑝 from the input tape (and will not read any further bits
74 Here we use the term "computable" in the Turing-Church sense. This will be described in further details in the next
section on computability theory.
75 An equivalent definition is to say that 𝑓 : X → ℝ is lower semicomputable if and only if the set 𝐿 = {( 𝑥, 𝑞) ∈ X × ℚ :
𝑓
𝑞 < 𝑓 ( 𝑥 )} is recursively enumerable, i.e., there exists a Turing machine that computes a surjective mapping ℕ → 𝐿 𝑓 .
76 It is worth noting that in some references (e.g., Hutter et al. (2024)), such machines are referred to as prefix/monotone
Turing machines, and then the names "prefix Turing machine" and "monotone Turing machine" are used in different
contexts to emphasize different aspects of the same machine: In general, the name "prefix Turing machine" is typically used
when we are mainly interested in the state of the machine when it halts, whereas the name "monotone Turing machine" is
used when we are also interested in the evolution of its state as it runs (and potentially have an infinite computation). In
our paper, we choose to use the unified name "monotone Turing machine".

91

from the input tape), and will write 𝑥 at the beginning of the output tape (and will not write any
further bits to the output tape).
The set P𝑇 = { 𝑝 : 𝑇 ( 𝑝) halts} forms a prefix-free77 set. We call the strings in P𝑇 𝑇 -self-delimiting
programs78 , or simply self-delimiting programs when the monotone Turing machine 𝑇 is understood
from the context.
Definition B.20. We say that a monotone Turing machine 𝑇 computes a string starting with 𝑥 ∈ {0, 1}∗
on input 𝑝 ∈ {0, 1}∗ , and write79 𝑇 ( 𝑝) = 𝑥 ∗ if by putting the string 𝑝 at the beginning of the input
tape, the machine will write 𝑥 on the output tape in such a way that when the machine writes the last
bit of 𝑥 , the input head will be at position 𝑙 ( 𝑝) (i.e., 𝑝 will be to the left of the input head). It does
not matter what exists after 𝑝 on the input tape: The machine will always write 𝑥 at the beginning of
the output tape as long as 𝑝 exists at the beginning of the input tape.80
We say that a monotone Turing machine 𝑇 computes an infinite string 𝜔 ∈ {0, 1}∞ on input 𝑝 ∈ {0, 1}∗ ,
and write 𝑇 ( 𝑝) = 𝜔 if by putting the string 𝑝 at the beginning of the input tape, the machine will read
𝑝 (and no further bits) and write 𝜔 on the output tape. Note that 𝑇 ( 𝑝) = 𝜔 for 𝜔 ∈ {0, 1}∞ means
that the machine never halts.
Next we turn to the definition of a universal monotone Turing machine. For this we need:
1. A fixed canonical way of encoding monotone Turing machines as binary strings such that the
set of encodings of all monotone Turing machines is decidable by a Turing machine (which we
do not require to be a monotone one). In other words, if we denote the binary encoding of 𝑇
as ⟨𝑇 ⟩, then there exists a Turing machine which computes a function {0, 1}∗ → {0, 1} which
outputs 1 if and only if its input is in the set {⟨𝑇 ⟩ : 𝑇 is a monotone Turing machine}.
• Note that this induces a fixed canonical enumeration 𝑇1 , . . . of all monotone Turing machines
as follows: We let 𝑇𝑖 be the 𝑖-th Turing machine according to the ≺ order defined as 𝑇 ≺ 𝑇 ′
if and only if 𝑙 (⟨𝑇 ⟩) < 𝑙 (⟨𝑇 ′ ⟩) or 𝑙 (⟨𝑇 ⟩) = 𝑙 (⟨𝑇 ′ ⟩) and ⟨𝑇 ⟩ comes before ⟨𝑇 ′ ⟩ according to
the lexicographic order. It is worth noting that the enumeration mapping 𝑛 ↦→ ⟨𝑇𝑛 ⟩ is
computable.
2. A computable injective prefix-free encoding 𝑐 : ℕ → {0, 1}∗ of integers as binary strings in such
a way that it is "computably invertible", i.e., there exists a computable mapping 𝑐′ : {0, 1}∗ →
ℕ ∪ {⊥} such that 𝑐′ ( 𝑐 ( 𝑛)) = 𝑛 for all 𝑛 ∈ ℕ and 𝑐′ ( 𝑥 ) =⊥ for all 𝑥 ∉ 𝑐 (ℕ). E.g., we can choose
𝑐 ( 𝑛) to be the bitstring having 𝑛 ones followed by a zero.
It is worth noting that for every computable function 𝑓 : ℕ → ℕ, the function 𝑓𝑐 : {0, 1}∗ →
{0, 1}∗ defined as
(
𝑐 ( 𝑓 ( 𝑐′ ( 𝑥 ))
if 𝑥 ∈ 𝑐 (ℕ) ,
𝑓𝑐 ( 𝑥 ) =
𝜀
otherwise .
is computable.
77 A prefix-free set is a subset of {0, 1} ∗ such that no element is a prefix of any other element.

78 Here we can interpret 𝑝 ∈ P

𝑇 as a "program that can run on the monotone Turing machine 𝑇 ". We do not assume here
that these programs are necessarily able to "simulate all possible computational processes". This would be the case only
when the machine 𝑇 is universal. We describe the concept of universal monotone Turing machines in Definition B.21.
79 Notice that the ∗ symbol in the notation 𝑇 ( 𝑝) = 𝑥 ∗ is not a superscript nor a subscript.
80 It is worth noting that for 𝑝 ∈ {0, 1} ∗ , there does not necessarily exist a unique 𝑥 ∈ {0, 1} ∗ for which 𝑇 ( 𝑝) = 𝑥 ∗, as the
machine may read 𝑝 and then write multiple bits before reading any further bits from the input tape. However, for every
𝑥1 , 𝑥2 ∈ {0, 1}∗ for which we have both 𝑇 ( 𝑝) = 𝑥1 ∗ and 𝑇 ( 𝑝) = 𝑥2 ∗, one of 𝑥1 and 𝑥2 must be a prefix of the other.

92

Given that we have such fixed canonical choices, we can define universal monotone Turing machines
as follows:
Definition B.21. A universal monotone Turing machine 𝑈 is a monotone Turing machine which can
simulate any other monotone Turing machine in the following sense: There exists a computable
injective prefix free-encoding 𝑐 : ℕ → {0, 1}∗ , which is computably invertible, and an enumeration
𝑇1 , . . . , 𝑇𝑛 , . . . of monotone Turing machines for which 𝑛 ↦→ ⟨𝑇𝑛 ⟩ is computable, such that
𝑈 ( 𝑐 ( 𝑛) 𝑝) = 𝑇𝑛 ( 𝑝) ,

∀𝑛 ∈ ℕ, ∀ 𝑝 ∈ {0, 1}∗ ,

and
𝑈 ( 𝑐 ( 𝑛) 𝑝) = 𝑥 ∗ ⇔ 𝑇𝑛 ( 𝑝) = 𝑥 ∗ ,

∀𝑛 ∈ ℕ, ∀ 𝑝, 𝑥 ∈ {0, 1}∗ .

Theorem B.22. Universal monotone Turing machines exist (Hutter et al., 2024).
Universal monotone Turing machines are not unique. In the remainder of this paper, unless we state
otherwise, we will assume that we have a canonical fixed universal monotone Turing machine 𝑈 that
we will use as "the reference universal monotone Turing machine".
Now we are ready to define the (prefix) Kolmogorov complexity of a binary string:
Definition B.23. The (prefix) Kolmogorov complexity 𝐾𝑇 ( 𝑥 ) of a binary possibly-infinite string
𝑥 ∈ {0, 1}# relative to a monotone Turing machine 𝑇 is defined as81
𝐾𝑇 ( 𝑥 ) := min{ 𝑙 ( 𝑝) : 𝑝 ∈ {0, 1}∗ , 𝑇 ( 𝑝) = 𝑥 } ,

with the convention that 𝐾𝑇 ( 𝑥 ) = ∞ if there is no 𝑝 ∈ {0, 1}∗ with 𝑇 ( 𝑝) = 𝑥 .
For the reference universal monotone Turing machine 𝑈 , we drop the subscript and simply write
𝐾 ( 𝑥 ) := 𝐾𝑈 ( 𝑥 ) and call it the (prefix) Kolmogorov complexity of 𝑥 , or simply the 𝐾 -complexity of 𝑥 .
We can extend the definition of Kolmogorov complexity to general mathematical objects assuming that
we have a fixed canonical representation/encoding of these objects as binary strings, i.e., 𝐾 ( 𝑜) = 𝐾 (⟨𝑜⟩)
where ⟨𝑜⟩ is the canonical encoding of 𝑜 as a binary string.
From Definition B.21 one can see that if 𝑈 is a universal monotone Turing machine and 𝑇 is an
arbitrary monotone Turing machine which appears as the 𝑛𝑇 -th machine in the canonical enumeration
(i.e., 𝑇𝑛𝑇 = 𝑇 ), then for all 𝑥 ∈ {0, 1}∗ , we have
𝐾𝑈 ( 𝑥 ) ≤ 𝐾𝑇 ( 𝑥 ) + 𝑙 ( 𝑐 ( 𝑛𝑇 )) .

This implies that the prefix Kolmogorov complexity depends on the choice of the universal Turing
machine only up to an additive constant:
Theorem B.24. The definition of the Kolmogorov complexity depends on the choice of the universal
monotone machine only up to additive constants: If 𝑈1 and 𝑈2 are universal, then there exists 𝑐 > 0 such
that 𝐾𝑈1 ( 𝑥 ) − 𝑐 ≤ 𝐾𝑈2 ( 𝑥 ) ≤ 𝐾𝑈1 ( 𝑥 ) + 𝑐 for all 𝑥 ∈ {0, 1}# (Hutter et al., 2024).
81 Note that for finite strings 𝑥 ∈ {0, 1} ∗ , the notation 𝑇 ( 𝑝) = 𝑥 necessarily means that the machine halts on input 𝑝 after

writing 𝑥 . When we consider the possibility of continuing after writing 𝑥 , we write 𝑇 ( 𝑝) = 𝑥 ∗.

93

B.4. Solomonoff induction.
Definition B.25. Let M 𝑠𝑜𝑙 be the class of all lower semicomputable semimeasures, and let {𝜎1 , . . . , }
be a fixed canonical enumeration82 of M 𝑠𝑜𝑙 (possibly with repetition), and let 𝑤 : ℕ → (0, ∞) be a
Í
lower semicomputable function satisfying 𝑖 𝑤𝑖 ≤ 1. The universal mixture over M 𝑠𝑜𝑙 induced by the
prior 𝑤 is defined as
∑︁
∑︁
𝜉𝑤 ( 𝑥 ) :=
𝑤𝑖 𝜎𝑖 ( 𝑥 ) =
𝑤𝜎 𝜎 ( 𝑥 ) ,
𝑖 ∈ℕ

where

𝜎 ∈ M 𝑠𝑜𝑙

∑︁

𝑤𝜎 :=

𝑤𝑖 .

𝑖 ∈ℕ:
𝜎𝑖 =𝜎

The Solomonoff universal prior is the one for which 𝑤𝑖 = 2− 𝐾 ( 𝑖 ) where 𝐾 ( 𝑖) is the Kolmogorov
complexity83 of the binary representation of the integer 𝑖. In this case we simply write 𝜉𝑈 to denote
the particular universal mixture distribution that arises from the Solomonoff universal prior.84
A direct corollary of Corollary B.15 is that Solomonoff ’s universal prior can be used to obtain strong
predictors:
Theorem B.26. If 𝜎 is a computable measure describing the ground-truth probability distribution of an
infinite sequence 𝑥 ∼ 𝜎, then
lim 𝐷∞ ( 𝜎, 𝜉𝑈 | 𝑥 ≤ 𝑡 ) = 0 ,

𝑡 →∞

𝜎 ( 𝑥 )-almost surely.

The above is also true if 𝜎 is a lower semicomputable (semi)measure.
In other words, by collecting a sufficient number of observations from the true sequence (which we
assume to be drawn from a computable measure), we can make accurate predictions about the future
observations using the universal mixture 𝜉𝑈 .
B.5. General Reinforcement Learning.
Let A and E be two countable sets which we interpret respectively as the action space and the percept
space in general reinforcement learning. Let AE ∗ := AE ∗ be the set of all finite histories of interactions
82 A natural choice can be obtained using encodings of Turing machines 𝑇 which compute functions 𝜙

: X∗ × ℕ →
ℚ ∩ [0, 1]. In this case, if ⟨𝑇 ⟩ is the canonical representation/encoding of the Turing machine 𝑇 as an integer, then we let
𝜎 ⟨𝑇 ⟩ ( 𝑥 ) = lim𝑛→∞ max1≤ 𝑖 ≤ 𝑛 𝜙𝑇 ( 𝑥, 𝑖). (Note that here we added the max1≤ 𝑖 ≤ 𝑛 part to recover the monotonicity in the 𝑛 ∈ ℕ
argument, which is part of the definition of lower semicomputable functions.) If 𝑛 ∈ ℕ is not a valid encoding of such a
Turing machine, then we let 𝜎𝑛 ( 𝑥 ) = 0.
83 It is worth noting that the Kolmogorov complexity is upper semicomputable and hence 𝑖 ↦→ 2 − 𝐾 ( 𝑖 ) is lower semicomputable.
84 The Solomonoff universal mixture 𝜉 is closely related to the following semimeasure, which is called the Solomonoff
𝑈
distribution 𝑀 , and which was introduced in Solomonoff (1978):
∑︁
𝑀 (𝑥) =
2 − 𝑙 ( 𝑝 ) , ∀𝑥 ∈ X ∗ .
𝑇

𝑝 ∈ {0,1} ∗ :
𝑈 ( 𝑝 )=𝑥 ∗

The semimeasure 𝑀 can be interpreted as the probability distribution describing the state of the output tape of the universal
monotone Turing machine 𝑈 when fed with uniformly random bits on the input tape (i.e., running a random program on a
×
universal machine). It has been shown that 𝑀 and 𝜉𝑈 are multiplicatively equivalent: 𝑀 = 𝜉𝑈 . Proofs of this fact can be
found in Hutter (2005); Li and Vitányi (2019); Wood et al. (2011); Zvonkin and Levin (1970).

94

between the agent and the environment. We slightly abuse notation and write æ1:𝑡 = 𝑎1 𝑒1 . . . 𝑎𝑡 𝑒𝑡 to
describe the first 𝑡 interactions in a history. 85
In Section 2, we defined the space of percepts as E = O × R, where O is the set of observations and
R ⊂ [0, 1] to be some finite set of rewards.
For a sequence 𝑎 ∈ A ∗ of actions, and a sequence 𝑒 ∈ E ∗ of percepts, if 𝑡 ≤ min{ 𝑙 ( 𝑎) , 𝑙 ( 𝑒)}, we write
æ1:𝑡 to denote the interleaved sequence 𝑎1 𝑒1 . . . 𝑎𝑡 𝑒𝑡 . Obviously, æ1:𝑡 ∈ AE 𝑡 ⊂ AE ∗ .
Definition B.27. An environment-like chronological conditional (semi)measure 𝜈 is characterized by
a mapping 𝑓𝜈 : AE ∗ × A → Δ′ E. For æ1:𝑡 ∈ AE ∗ , 𝑎 ∈ A and 𝑒 ∈ E, we write 𝜈 ( 𝑒 |æ1:𝑡 , 𝑎) as shorthand
notation for 𝑓𝜈 (æ1:𝑡 , 𝑎) ( 𝑒) and interpret it as follows: Given a history æ1:𝑡 of interactions between the
agent and the environment, and given that the agent took the action 𝑎 afterwards, then the conditional
(semi)probability that the environment will subsequently produce the percept 𝑒 is 𝜈 ( 𝑒 |æ1:𝑡 , 𝑎).
We also use the notation

𝜈 ( 𝑒 ≤ 𝑡 ∥ 𝑎 ≤ 𝑡 ) :=

Ö

𝜈 ( 𝑒𝑖 |æ<𝑖 , 𝑎𝑖 ) ,

𝑖≤𝑡

and interpret it as the conditional (semi)probability that the environment produces the percept
sequence 𝑒 ≤ 𝑡 given that the agent has made the action sequence 𝑎 ≤ 𝑡 . Notice how the structure of
𝜈 (·∥·) respects the chronological order between actions and percepts, and their causal structure.
The environment-like chronological conditional (semi)measure 𝜈 is said to be lower semicomputable
(resp. computable) if the function æ1:𝑡 , 𝑎, 𝑒 ↦→ 𝜈 ( 𝑒 |æ1:𝑡 , 𝑎) from AE ∗ × A × E to [0, 1] is lower
semicomputable (resp. computable).
Definition B.28. A policy-like chronological conditional (semi)measure 𝜋 is characterized by a
mapping 𝑓𝜋 : AE ∗ → Δ′ A. For æ1:𝑡 ∈ AE ∗ and 𝑎 ∈ A, we write 𝜋 ( 𝑎 |æ1:𝑡 ) as a shorthand notation for
𝑓𝜋 (æ1:𝑡 )( 𝑎) and interpret it as follows: Given a history æ1:𝑡 of interactions between the agent and the
environment, then the conditional (semi)probability that the (policy 𝜋 of the) agent will take the
action 𝑎 after æ1:𝑡 is 𝜋 ( 𝑎 |æ1:𝑡 ).
We also use the notation

𝜋 ( 𝑎 ≤ 𝑡 ∥ 𝑒<𝑡 ) :=

Ö

𝜋 ( 𝑎𝑖 |æ<𝑖 ) ,

𝑖≤𝑡

and interpret it as the conditional (semi)probability that the agent makes the action sequence 𝑎 ≤ 𝑡
given that the environment produces the percept sequence 𝑒<𝑡 . Notice again how the structure of
𝜋 (·∥·) respects the chronological order between actions and percepts, and their causal structure.
The policy-like chronological conditional (semi)measure 𝜋 is said to be lower semicomputable (resp.
computable) if the function æ1:𝑡 , 𝑎 ↦→ 𝜋 ( 𝑎 |æ1:𝑡 ) from AE ∗ × A to [0, 1] is lower semicomputable (resp.
computable).
In the remainder of this paper, we write policy (resp. environment) to denote a policy-like (resp.
environment-like) chronological conditional semimeasure86 .
Now we can describe the interaction between an environment and a policy:
85 Strictly speaking æ
1:𝑡 should be = ( 𝑎1 , 𝑒1 )( 𝑎2 , 𝑒2 ) . . . ( 𝑎𝑡 , 𝑒𝑡 ).
86 A policy that is a proper conditional semimeasure (i.e., not a conditional measure) can be interpreted as describing a

situation where the agent fails to take an action at some point in time after which we assume that the agent ceases to exist
(i.e., the agent "dies"). Similarly, an environment that is a proper semimeasure can be interpreted as describing a situation
where the "world" is not guaranteed to exist for ever and may end, which would also mean that the agent "dies".

95

Definition B.29. Given an environment 𝜈 and a policy 𝜋, we can define the semimeasure 𝜈𝜋 on AE ∗
describing the interaction between the agent and the environment as follows:
Ö
𝜈𝜋 (æ1:𝑡 ) = 𝜋 ( 𝑎 ≤ 𝑡 ∥ 𝑒<𝑡 ) 𝜈 ( 𝑒 ≤ 𝑡 ∥ 𝑎 ≤ 𝑡 ) =
𝜋 ( 𝑎𝑖 |æ<𝑖 ) 𝜈 ( 𝑒𝑖 |æ<𝑖 , 𝑎𝑖 ) , ∀æ1:𝑡 ∈ AE ∗ .
(33)
𝑖≤𝑡

We can similarly define the conditional semimeasure 𝜈𝜋 (·|æ1:𝑡 ) for all æ1:𝑡 ∈ AE ∗ as87
Ö
𝜈𝜋 (æ𝑡+1:𝑡+𝑡′ |æ1:𝑡 ) =
𝜋 ( 𝑎𝑖 |æ<𝑖 ) 𝜈 ( 𝑒𝑖 |æ<𝑖 , 𝑎𝑖 ) , ∀æ𝑡+1:𝑡+𝑡′ ∈ AE ∗ .

(34)

𝑡<𝑖 ≤ 𝑡 +𝑡 ′

Notice that we have 𝜈𝜋 (æ1:𝑡′ ) := 𝜈𝜋 (æ1:𝑡 æ𝑡+1:𝑡+𝑡′ ) = 𝜈𝜋 (æ1:𝑡 ) 𝜈𝜋 (æ𝑡+1:𝑡+𝑡′ |æ1:𝑡 ) for all æ1:𝑡 , æ𝑡+1:𝑡+𝑡′ ∈
AE ∗ .
Remark B.30. The definition of 𝜈𝜋 (·|æ1:𝑡 ) using
equation 34 coincides with Definition B.7 when
𝜈𝜋 (æ1:𝑡 æ𝑡+1:𝑡+𝑡 ′ )
𝜋
𝜋
𝜈 (æ1:𝑡 ) > 0, i.e., we have 𝜈 (æ𝑡+1:𝑡+𝑡′ |æ1:𝑡 ) =
whenever 𝜈𝜋 (æ1:𝑡 ) > 0. Here we are able
𝜈𝜋 (æ1:𝑡 )
𝜋
to extend the definition to cases where 𝜈 (æ1:𝑡 ) = 0, and hence we can meaningfully analyze the
"𝜈𝜋 -consequences" of counterfactual events that cannot occur under 𝜈𝜋 : E.g., under this definition, we
can speak in a well-defined way about the conditional expected reward that the agent gets in the next
percept under the policy 𝜋 in the environment 𝜈 given that it has observed æ1:𝑡 even if 𝜈𝜋 (æ1:𝑡 ) = 0
Í
(we can literally define this as 𝑎,𝑒 ∈ A× E 𝜈𝜋 ( 𝑎𝑒 |æ1:𝑡 ) 𝑟 ( 𝑒) where 𝑟 ( 𝑒) is the reward associated with the
percept 𝑒.).
Definition B.31. The (normalized88 ) value function of the policy 𝜋 in the environment 𝜈 with discount
factor 𝛾 ∈ [0, 1) is the function 𝑉𝜈𝜋 : AE ∗ → [0, 1] defined89 as:
∑︁
∑︁
𝑉𝜈𝜋 (æ<𝑡 ) = lim (1 − 𝛾 )
𝛾 𝑖−𝑡
𝑟 ( 𝑒𝑖 ) 𝜈𝜋 (æ𝑡:𝑖 |æ<𝑡 ) ,
(36)
𝑚→∞

𝑖:𝑡 ≤ 𝑖 ≤ 𝑚

æ𝑡:𝑖 ∈ AE 𝑖 − 𝑡+1

where 𝑟 ( 𝑒𝑖 ) is the reward associated with the percept 𝑒𝑖 .
The (normalized) action-value function (or 𝑄 -function) is the function 𝑄 𝜈𝜋 : AE ∗ × A → [0, 1] defined
as:
∑︁
𝑄 𝜈𝜋 (æ<𝑡 , 𝑎𝑡 ) =
𝜈 ( 𝑒𝑡 |æ<𝑡 , 𝑎𝑡 ) ((1 − 𝛾 ) 𝑟 ( 𝑒𝑡 ) + 𝛾𝑉𝜈𝜋 (æ<𝑡 𝑎𝑡 𝑒𝑡 ))
𝑒𝑡 ∈ E

= lim (1 − 𝛾 )
𝑚→∞

∑︁

𝛾 𝑖−𝑡

𝑖:𝑡 ≤ 𝑖 ≤ 𝑚

∑︁

𝑟 ( 𝑒𝑖 ) 𝜈𝜋 ( 𝑒𝑡 æ𝑡+1:𝑖 |æ<𝑡 𝑎𝑡 ) ,

(37)

( 𝑒𝑡 ,æ𝑡+1:𝑖 ) ∈ E × AE 𝑖 − 𝑡

87 Note that in equation 34, we have æ := æ æ
<𝑖
1:𝑡 𝑡 +1:𝑖 −1 .
88 In some references, e.g., Sutton and Barto (2018), the value function is defined without the "normalizing" multiplicative

Í
(1 − 𝛾 ) term. This would make the value function take values in [0, 1/(1 − 𝛾 )] since 𝑖 ≥0 𝛾 𝑖 = 1/(1 − 𝛾 ). As it is convenient to
Í
have values in [0, 1], we normalize by the total weight 𝑖 ≥0 𝛾 𝑖 = 1/(1 − 𝛾 ), which boils down to multiplying by (1 − 𝛾 ). Note
that the definition of the value function in (Hutter et al., 2024, Definition 6.6) is also normalized, though the definition
there is general and can handle arbitrary discounting functions that are not necessarily geometric.
89 It is worth noting that in some references, e.g., (Hutter et al., 2024, Definition 6.6), the normalized value function is
defined as
∑︁
∑︁
lim (1 − 𝛾 )
𝜈𝜋 (æ𝑡:𝑚 |æ<𝑡 )
𝛾 𝑖 − 𝑡 𝑟 ( 𝑒𝑖 ) .
(35)
𝑚→∞

æ𝑡:𝑚 ∈ AE 𝑚 − 𝑡+1

𝑖 :𝑡 ≤ 𝑖 ≤ 𝑚

For this alternative definition, any future trajectory which "corresponds" to a missing probability mass (due to the semimeasure definition) will not contribute to the value function. In other words, if we take the interpretation that missing
probabilities in a semimeasure correspond to the probability of death of an agent, and if we have a trajectory for which the
agent dies after two steps, then the rewards obtained in the next two steps will not contribute to the value function as
defined in equation 35. In other words, the agent only values trajectories for which it lives forever. The two definitions of
the value function in equation 36 and equation 35 differ only in the case of semimeasures.

96

with the convention that æ𝑡+1:𝑡 = 𝜀 and AE 0 = {𝜀}.
One can see that for all æ<𝑡 ∈ AE ∗ , we have
∑︁
𝑉𝜈𝜋 (æ<𝑡 ) =
𝜋 ( 𝑎𝑡 |æ<𝑡 ) 𝑄 𝜈𝜋 (æ<𝑡 , 𝑎𝑡 ) .
𝑎𝑡 ∈ A

Definition B.32. The optimal value function 𝑉𝜈∗ : AE ∗ → [0, 1] of an environment 𝜈 is defined as
𝑉𝜈∗ (æ<𝑡 ) := sup 𝑉𝜈𝜋 (æ<𝑡 ) ,

∀æ<𝑡 ∈ AE ∗ ,

𝜋

where the supremum is taken over all policies (which are not necessarily computable or lower
semicomputable).
We denote as 𝜋∗𝜈 any policy which is optimal for the environment 𝜈, i.e.,
𝑉𝜈𝜋∗𝜈 (æ<𝑡 ) = 𝑉𝜈∗ (æ<𝑡 ) = sup 𝑉𝜈𝜋 (æ<𝑡 ) ,

∀æ<𝑡 ∈ AE ∗ ,

𝜋

and we denote the set of optimal policies as Π𝜈∗ .
An agent that acts according to an optimal policy 𝜋∗𝜈 of the environment 𝜈 is denoted as AI𝜈.
So far we have described agents which can act optimally in a known environment 𝜈. What if the
agent is uncertain about the true environment? Assume that the agent only knows that the true
environment belongs to some class of environments Menv which we assume to be countable. Assume
further that the agent has a prior Bayesian belief about the true environment: For every 𝜈 ∈ Menv , let
𝑤𝜈 > 0 be the prior (semi)probability that the true environment is 𝜈. In this case, one can define the
universal mixture environment 𝜉𝑈𝑤 such that
∑︁
𝜉𝑈𝑤 =
𝑤𝜈 𝜈 .
𝜈 ∈ Menv

A direct corollary that follows from the merging of opinions results (Theorem B.14 and Corollary B.15)
is the following:
Proposition B.33 (on policy convergence). For any universal prior 𝑤 ∈ Δ′ Menv , the universal mixture
𝜉 = 𝜉𝑈𝑤 satisfies: For any policy 𝜋 and any environment 𝜈 ∈ Menv , we have
lim 𝐷∞ ( 𝜉𝜋 , 𝜈𝜋 |æ1:𝑡 ) = 0 ,

𝑡 →∞

and

𝜈𝜋 -almost surely,

lim |𝑉𝜉𝜋 (æ1:𝑡 ) − 𝑉𝜈𝜋 (æ1:𝑡 )| = 0 ,

𝑡 →∞

𝜈𝜋 -almost surely.

The universal Bayesian agent with respect to the class Menv and the prior 𝑤 is the agent AI𝜉𝑈𝑤 (also
denoted as AI𝜉) which acts optimally in the universal mixture environment 𝜉𝑈𝑤 , i.e., it acts according
to 𝜋∗𝜉𝑤 .
𝑈

The universal Bayesian agent AI𝜉 satisfies a few nice properties such as Pareto optimality and selfoptimization Hutter (2002)

97

B.6. AIXI
By combining Solomonoff ’s induction theory with (universal Bayesian) general reinforcement learning,
we get AIXI (introduced by Hutter in Hutter (2000)).
Hutter considered the class of all lower semicomputable chronological conditional semimeasures
semi , and considered a universal mixture environment
Mlsc
𝜉𝑈𝑤 =

∑︁

𝑤𝜈 𝜈 ,

semi
𝜈 ∈ Mlsc

semi is some universal mixture which is lower semicomputable. A natural choice of the
where 𝑤 ∈ Δ′ Mlsc
universal prior would be the one based on Kolmogorov complexity, just as in Solomonoff induction, i.e.,
Í
we take 𝑤𝜈 = 𝑖:𝑀𝑖 “lower semi-computes” 𝜈 2− 𝐾 ( 𝑖 ) , where 𝑀𝑖 denotes the 𝑖-th Turing machine in a canonical
enumeration of machines that "lower semicomputes"90 environment-like chronological conditional
semimeasures.

AIXI is the universal Bayesian agent AI𝜉 in the universal mixture 𝜉 = 𝜉𝑈𝑤 w.r.t. the class of all lower
semi .
semicomputable chronological conditional semimeasures Mlsc
AIXI is considered to be a theoretical gold standard for single-agent general reinforcement learning
because its hypothesis class consists (in some arguable sense) of the most general environments91 .
By virtue of being a universal Bayesian agent, AIXI satisfies the same nice optimality results that are
satisfied by general universal Bayesian agents AI𝜉 such as pareto optimality and self-optimization. It
was conjectured that AIXI satisfies additional optimality results such as strong asymptotic optimality,
which means that for any computable environment, AIXI will almost-surely converge (on policy) to
acting optimally in this ground-truth environment.
Unfortunately, it turns out that this is not the case in general as the choice of the universal prior 𝑤
can affect the optimality properties of AIXI (e.g., Leike and Hutter (2015b); Orseau (2010a, 2013)):
It is possible to choose a bad universal prior 𝑤 for which AIXI will not converge to acting optimally. A
notable example is the "dogmatic prior" (Leike and Hutter, 2015b) for which the agent has a strong
prior belief that the environment will eternally punish the agent (by giving it 0 rewards forever
after) if it deviates from some arbitrary computable policy 𝜋.92 In this case, if the value of 𝜋 in the
ground-truth environment is not too small, one can show that AIXI will always act according to 𝜋
even if it is not optimal in the ground-truth environment.93
These issues of asymptotic non-optimality of AIXI can be alleviated by adding good exploration
components to it, such as Thompson sampling (Leike et al., 2016a).
B.7. Failure of AIXI to model embedded agency.
AIXI is the optimal Bayesian agent for the class of all lower semicomputable environments. AIXI
itself is not lower semicomputable, so in some sense, AIXI is more powerful than the environments
90 More precisely, the machine 𝑀

𝑖 computes a function 𝜙𝑖 : AE

× A × E × ℕ → [0, 1] ∩ ℚ such that 𝜙𝑖 ( ℎ, 𝑎, 𝑒, 𝑛 + 1) ≥
𝜙𝑖 ( ℎ, 𝑎, 𝑒, 𝑛) for all 𝑛 ∈ ℕ and 𝜈𝑖 ( 𝑒 | ℎ, 𝑎) := lim𝑛→∞ 𝜙𝑖 ( ℎ, 𝑎, 𝑒, 𝑛) is an environment-like chronological conditional semimeasure.
Furthermore, we assume that the canonical enumeration 𝑀1 , . . . covers all the environment-like chronological conditional
∗

semimeasures that can be described in this fashion.
91 Assuming that the environment is computable is a very unrestrictive assumption.
92 More precisely, the agent gives a very high prior probability 𝑤 to the described environment.
𝜈
93 It is worth noting that the Solomonoff prior (which is used to define the AIXI agent) is defined in terms of the Kolmogorov
complexity, which in turn is based on the choice of some fixed reference universal monotone Turing machine 𝑈 . One can
choose 𝑈 so that the Solomonoff prior that is induced by 𝑈 is "dogmatic".

98

it considers. This is sufficient for the single-agent reinforcement learning (RL) setup that we have
discussed in the previous section as we have considered that the agent and the environment are
cleanly separated and communicate via well-defined channels of actions and observations, which is
the typical assumption of single-agent RL.
However, in real life, agents are "embedded in their environments", and hence we have to consider
the possibility that the environment may contain other agents that may be implementing a policy
similar to them. In particular, if we have one agent implementing AIXI, then we have to consider the
possibility that the environment (from the perspective of this agent) may also be implementing AIXI,
which makes the environment not lower semicomputable, and hence the true environment would not
belong to the class of environments that is considered by AIXI. Therefore, any theoretical analysis
of Bayesian RL that is based on the assumption that the true environment belongs to the class of
environments considered by the Bayesian agent would not apply.
B.8. JAIXI as a way to formalize embedding failures in universal artificial intelligence.
AIXI is fundamentally a "decoupled Bayesian agent", i.e., it has prior beliefs only about the environment
dynamics, and assumes that the choice of its policy is independent from the environment. This fails
to capture situations where the environment may contain other agents that may be implementing
similar policies (e.g., the psychological twin prisoner’s dilemma).
One step forward towards capturing embeddedness is to consider an "embedded Bayesian agent"
which considers that the policy of the agent and the environment may be dependent: Instead of
having a prior over a hypothesis class of environments (as is the case for Bayesian dualistic agents), an
embedded Bayesian agent has a prior over a hypothesis class that jointly describes the interaction of
the agent and the environment (cf. Section 3). Since the interaction of an agent and an environment
can be modeled as a semimeasure on AE ∗ , we can say that an embedded Bayesian agent has a prior
over a class of semimeasures on AE ∗ .
In computational terms, one may say that a decoupled Bayesian agent considers that the agent and
the environment are described by two different programs whereas an embedded Bayesian agent
considers that there is a single joint program that describes both, and it has a prior over the class of
such programs that jointly describe the agent and the environment. One may say that the agent and
the environment from its perspective are both parts of the same universe, and hence a program that
describes the universe would jointly describe the agent and its environment.
In concurrent work, Wyeth and Hutter (2025) introduced Joint AIXI (JAIXI), which follows the
above embedded Bayesian agent approach and considers the class Mjoint of all lower semicomputable
semimeasures on AE ∗ . Let 𝑤 be a lower semicomputable universal prior over Mjoint and let 𝜉𝑤
be
joint
∗
𝑤
the corresponding universal mixture. This induces an environment env( 𝜉joint ) : AE × A → E by
considering the conditional semimeasure defined as:94

env( 𝜉joint ) ( 𝑒 |æ1:𝑡 , 𝑎) := 𝜉joint ( 𝑒 |æ1:𝑡 𝑎) :=
𝑤

𝑤

𝜉𝑤
(æ1:𝑡 𝑎𝑒)
joint
𝜉𝑤
(æ1:𝑡 𝑎)
joint

.

(38)

While 𝜉𝑤
is lower semicomputable, the induced environment env( 𝜉𝑤
) is not lower semicomjoint
joint
94 In equation 38, we gloss over a formal technicality which is not important for the discussion: The semimeasure 𝜉𝑤
is
joint
defined on AE ∗ , and hence 𝜉𝑤
(æ
𝑎
)
is
strictly
speaking
not
canonically
defined.
One
may
consider
that
A
and
E
are
1:𝑡
joint
subsets of the same set S and then consider the class of lower semicomputable semimeasures on S ∗ which would then

contain both AE ∗ × A and AE ∗ . This is the approach followed in Wyeth and Hutter (2025). Another possibility would be
Í
to simply define 𝜉𝑤
(æ1:𝑡 𝑎) = 𝑒 ∈ E 𝜉𝑤
(æ1:𝑡 𝑎𝑒).
joint
joint
99

putable95 (Leike, 2016; Leike and Hutter, 2015c).
Wyeth and Hutter (2025) define JAIXI as the optimal agent for the environment env( 𝜉𝑤
), i.e., the
joint
agent that implements 𝜋∗env( 𝜉𝑤 ) . The authors did not aim to present JAIXI as a good solution for
joint

universal embedded intelligence, but rather use it to illustrate the embeddedness failures of this
particular approach to universal artificial intelligence, such as failing to learn some adversarially
chosen sequences.
The failure of JAIXI to be a good solution for embedded universal intelligence can also be seen from
the fact that JAIXI is probably not lower semicomputable,96 and if we make it interact with a lower
semicomputable environment, we are not guaranteed to get a lower semicomputable semimeasure on
AE ∗ describing the interaction. In other words, making JAIXI interact with a lower semicomputable
environment gives rise to an interaction which may not be in the hypothesis class of JAIXI and hence
may not satisfy the grain-of-truth property.
Our work takes a complementary path. We begin by characterizing the behavior and predictions of
embedded Bayesian agents under the assumption that they do satisfy the grain-of-truth property. We
show that this allows them to reason about ‘functional similarities’—the possibility that the environment contains agents similar to themselves—which in multi-agent scenarios leads to convergence
towards a new family of solution concepts: embedded equilibria. Subsequently, in Section 5, we
directly solve the grain-of-truth problem by constructing a new model class and a corresponding joint
mixture model, using the reflective oracle framework as well as our novel reflective universal inductor,
which allows us to define a universally intelligent embedded agent.

C. Proofs
C.1. Proof of Proposition 3.17
We first generalize the proposition towards hypothesis classes Muni that can also contain non-fullysupported universes, and then prove the general proposition, which directly implies the correctness
of Proposition 3.17 as well. We remind the reader that the notation æ∗ ∈ AE ∗ stands for an arbitrarylength history.
When a universe 𝜆 (æ∗ ) is not fully-supported, it does not uniquely factorize into a policy 𝜋 and 𝜈,
as the conditionals 𝜆 ( 𝑎 | æ∗ ) or 𝜆 ( 𝑒 | æ∗ 𝑎) are undefined when 𝜆 (æ∗ ) = 0 or 𝜆 (æ∗ 𝑎) = 0, respectively.
Hence, different pairs of policy-environment can lead to the same universe distribution. This leads
us to the following more general definition of decoupledness of 𝑤 ( 𝜆 ), also compatible with Muni
containing non-fully-supported universes.
Definition C.1 (Decoupled prior). A probability measure 𝑤 ( 𝜆 ) over 𝜆 ∈ Muni is decoupled iff there
exist spaces Mpol and Menv and probability measure 𝑤
˜ ∈ Δ (Mpol × Menv ) for which the following
holds:
(i) 𝑤 ( 𝜆 ) =

Í

𝜈 ∈ Menv

Í

𝜋 ∈ Mpol 𝛿 ( 𝜈

(ii) 𝑤
˜ ( 𝜋, 𝜈) = 𝑤
˜ ( 𝜋) 𝑤
˜ ( 𝜈)

𝜋

= 𝜆)𝑤
˜ ( 𝜋, 𝜈)

∀𝜆 ∈ Muni ;

∀𝜋 ∈ Mpol , 𝜈 ∈ Menv ,

Í
Í
with 𝛿 the indicator function, and 𝑤
˜ ( 𝜋) := 𝜈 ∈ Menv 𝑤
˜ ( 𝜋, 𝜈) and 𝑤
˜ ( 𝜈) := 𝜋 ∈ Mpol 𝑤
˜ ( 𝜋, 𝜈) are the
marginals of 𝑤
˜ over Mpol and Menv , respectively. It is worth noting that the above "factorization" of
95 Note that in general, the ratio of two lower semicomputable functions is not necessarily lower semicomputable.

96 The results of Leike and Hutter (2015a) can probably be adapted to show that JAIXI is not lower semicomputable.

100

a decoupled prior 𝑤 ∈ Muni is not necessarily unique, i.e., there can be more than one such 𝑤
˜ that
yields 𝑤.
When Muni only contains fully supported universes, this definition simplifies to the notion of decoupledness we used in Section 3.6, as each fully supported universe leads to a unique pair ( 𝜋, 𝜈). Now
we are ready to state and prove the generalized proposition.
Proposition C.2. Consider a hypothesis class Muni and corresponding probability measure 𝑤 ∈ ΔMuni .
If the prior beliefs 𝑤 are decoupled (cf. Definition C.1) with respect to the classes Mpol and Menv , with
corresponding decoupled probability measure 𝑤
˜ ∈ Δ (Mpol × Menv ), we have that the conditionals of the
Í
mixture universe 𝜌 (æ∗ ) := 𝜆 ∈ Muni 𝑤 ( 𝜆 ) 𝜆 (æ∗ ) are equal to
𝜌 ( 𝑎𝑡 | æ<𝑡 ) = 𝜁 ( 𝑎𝑡 | æ<𝑡 ) ,
𝜁 ( 𝑎𝑡 | æ<𝑡 ) :=

∑︁

𝜌 ( 𝑒𝑡 | æ<𝑡 𝑎𝑡 ) = 𝜉 ( 𝑒𝑡 | æ<𝑡 𝑎𝑡 )

𝑤
˜ pol ( 𝜋 | æ<𝑡 −1 𝑎𝑡 −1 ) 𝜋 ( 𝑎𝑡 | æ<𝑡 ) ,

𝑤
˜ pol ( 𝜋 | æ<𝑡 𝑎𝑡 ) := 𝑤
˜ pol ( 𝜋 | æ<𝑡 −1 𝑎𝑡 −1 )

𝜋 ∈ Mpol

𝜉 ( 𝑒𝑡 | æ<𝑡 𝑎𝑡 ) :=

∑︁

𝑤
˜ env ( 𝜈 | æ<𝑡 ) 𝜈 ( 𝑒𝑡 | æ<𝑡 𝑎𝑡 ) ,

𝑤
˜ env ( 𝜈 | æ1:𝑡 ) := 𝑤
˜ env ( 𝜈 | æ<𝑡 )

𝜈 ∈ Menv

𝜋 ( 𝑎𝑡 | æ<𝑡 )
𝜁 ( 𝑎𝑡 | æ<𝑡 )

𝜈 ( 𝑒𝑡 | æ<𝑡 𝑎𝑡 )
𝜉 ( 𝑒𝑡 | æ<𝑡 𝑎𝑡 )

with 𝑤
˜ pol ( 𝜋 | 𝜀) := 𝑤
˜ ( 𝜋) and 𝑤
˜ env ( 𝜈 | 𝜀) := 𝑤
˜ ( 𝜈). Hence, 𝜌 uses decoupled posterior beliefs 𝑤
˜ pol ( 𝜋 |
æ1:𝑡 𝑎𝑡+1 ) and 𝑤
˜ env ( 𝜈 | æ1:𝑡 ). As a result, we have that
(i) An embedded Bayes-optimal agent using the decoupled beliefs 𝑤 ( 𝜆 ) to construct its mixture universe
model 𝜌 (cf. equation 8) and implementing an embedded best response w.r.t. 𝜌 (cf. equation 10)
is equivalent to a decoupled Bayesian agent with mixture environment 𝜉 defined above, and
implementing a decoupled best response w.r.t. 𝜉 (cf. equation 5).
(ii) A 𝑘-step planner embedded Bayesian agent (cf. Definition 3.9) using the decoupled beliefs 𝑤 ( 𝜆 ) to
construct its mixture universe model 𝜌 is equivalent to a 𝑘-step planner decoupled Bayesian agent
with mixture environment 𝜉 and mixture policy 𝜁 as defined above, and implementing a 𝑘-step
planner policy
𝑎𝑡 ∈ arg max 𝑄 𝜉𝑘𝜁 (æ<𝑡 , 𝑎) ,
𝑎

with 𝑄 𝜉𝑘𝜁 as defined in equation 11.
Proof. For any scalar function 𝐹 : Muni → ℝ,
∑︁

( 𝑎)

𝑤( 𝜆) 𝐹 ( 𝜆) =

𝜆 ∈ Muni

∑︁

∑︁

∑︁

𝑤
˜ ( 𝜈) 𝑤
˜ ( 𝜋) 𝛿 ( 𝜈𝜋 = 𝜆 ) 𝐹 ( 𝜆 )

𝜆 ∈ Muni 𝜋 ∈ Mpol 𝜈 ∈ Menv

=

∑︁

∑︁

𝜋 ∈ Mpol 𝜈 ∈ Menv

=

∑︁

∑︁

𝑤
˜ ( 𝜈) 𝑤
˜ ( 𝜋)

∑︁

𝛿 ( 𝜈𝜋 = 𝜆 ) 𝐹 ( 𝜆 )

𝜆 ∈ Muni

𝑤
˜ ( 𝜈) 𝑤
˜ ( 𝜋) 𝐹 ( 𝜈𝜋 ) ,

𝜋 ∈ Mpol 𝜈 ∈ Menv

where ( 𝑎) follows directly from Definition C.1. As a result, the mixture universe 𝜌 (æ∗ ) can be rewritten

101

as
∑︁

∑︁

𝜌 (æ<𝑡 ) =

𝑤
˜ ( 𝜈) 𝑤
˜ ( 𝜋) 𝜈𝜋 (æ<𝑡 )

𝜋 ∈ Mpol 𝜈 ∈ Menv

∑︁

=

𝑤
˜ ( 𝜋) 𝜋 ( 𝑎<𝑡 || 𝑒<𝑡 −1 )

𝑡Ö
−1

𝑤
˜ ( 𝜈) 𝜈 ( 𝑒<𝑡 || 𝑎<𝑡 ) , with

𝜈 ∈ Menv

𝜋 ∈ Mpol

𝜋 ( 𝑎<𝑡 || 𝑒<𝑡 −1 ) :=

∑︁

𝜋 ( 𝑎𝑘 | æ<𝑘 ) ,

𝜈 ( 𝑒<𝑡 || 𝑎<𝑡 ) :=

𝑘=1

𝑡Ö
−1

𝜈 ( 𝑒𝑘 | æ<𝑘 𝑎𝑘 ) .

𝑘=1

Now let us introduce the following notation
∑︁
𝑤
˜ ( 𝜋) 𝜋 ( 𝑎<𝑡 || 𝑒<𝑡 −1 ) ,
𝜁 ( 𝑎<𝑡 || 𝑒<𝑡 −1 ) :=

𝜉 ( 𝑒<𝑡 || 𝑎<𝑡 ) :=

∑︁

𝑤
˜ ( 𝜈) 𝜈 ( 𝑒<𝑡 || 𝑎<𝑡 ) .

𝜈 ∈ Menv

𝜋 ∈ Mpol

Then we have that 𝜌 (æ<𝑡 ) = 𝜁 ( 𝑎<𝑡 || 𝑒<𝑡 −1 ) 𝜉 ( 𝑒<𝑡 || 𝑎<𝑡 ), and the conditionals of 𝜌 can be rewritten as
∑︁
𝜆 (æ<𝑡 )
𝑤( 𝜆)
𝜌 ( 𝑎𝑡 | æ<𝑡 ) =
𝜆 ( 𝑎𝑡 | æ<𝑡 )
𝜌 (æ<𝑡 )
𝜆 ∈ Muni
∑︁ ∑︁
𝜈𝜋 (æ<𝑡 )
𝑤
˜ ( 𝜈) 𝑤
˜ ( 𝜋)
𝜋 ( 𝑎𝑡 | æ<𝑡 )
=
𝜁 ( 𝑎<𝑡 || 𝑒<𝑡 −1 ) 𝜉 ( 𝑒<𝑡 || 𝑎<𝑡 )
𝜋 ∈ Mpol 𝜈 ∈ Menv

=

∑︁

∑︁

𝑤
˜ ( 𝜈) 𝑤
˜ ( 𝜋)

𝜋 ∈ Mpol 𝜈 ∈ Menv

=

∑︁

𝑤
˜ ( 𝜈)

𝜈 ∈ Menv

=

∑︁

𝑤
˜ ( 𝜋)

𝜋 ∈ Mpol

𝜈 ( 𝑒<𝑡 || 𝑎<𝑡 )
𝜉 ( 𝑒<𝑡 || 𝑎<𝑡 )

𝜋 ( 𝑎<𝑡 || 𝑒<𝑡 −1 ) 𝜈 ( 𝑒<𝑡 || 𝑎<𝑡 )
𝜋 ( 𝑎𝑡 | æ<𝑡 )
𝜁 ( 𝑎<𝑡 || 𝑒<𝑡 −1 ) 𝜉 ( 𝑒<𝑡 || 𝑎<𝑡 )

∑︁
𝜋 ∈ Mpol

𝑤
˜ ( 𝜋)

𝜋 ( 𝑎<𝑡 || 𝑒<𝑡 −1 )
𝜋 ( 𝑎𝑡 | æ<𝑡 )
𝜁 ( 𝑎<𝑡 || 𝑒<𝑡 −1 )

𝜋 ( 𝑎<𝑡 || 𝑒<𝑡 −1 )
𝜋 ( 𝑎𝑡 | æ<𝑡 )
𝜁 ( 𝑎<𝑡 || 𝑒<𝑡 −1 )

= 𝜁 ( 𝑎𝑡 | æ<𝑡 ) ,
where in the last step we used 𝜁 ( 𝑎𝑡 | æ<𝑡 ) as defined in the proposition statement, and the fact
−1 )
that 𝑤
˜ pol ( 𝜋 | æ<𝑡 −1 𝑎𝑡 −1 ) = 𝑤
˜ ( 𝜋) 𝜋𝜁 (( 𝑎𝑎<𝑡<𝑡 || || 𝑒𝑒<𝑡<𝑡−1
) which can easily be verified by induction. Using similar
reasoning, we arrive at
𝜌 ( 𝑒𝑡 | æ<𝑡 𝑎𝑡 ) = 𝜉 ( 𝑒𝑡 | æ<𝑡 𝑎𝑡 ) ,

thereby concluding the proof of the first part of the proposition. Statement (i) follows directly
upon observing that 𝜌𝜋 from equation 9 is equal to 𝜉𝜋 , and hence the decoupled best response (cf.
equation 5) and embedded best response (cf. equation 10) are equivalent. Statement (ii) follows
directly from observing that 𝜌 = 𝜉𝜁 .
□
C.2. Proof of Theorem 4.12
(i) As 𝜌𝑖 satisfies the grain-of-uncertainty assumption, its conditionals are always well-defined and
hence its conditional completion is unique, and as a result there exists an embedded best response
w.r.t. 𝜌𝑖 that is equal to 𝜋𝑖 . (ii) From Theorem 3.11, it follows from the grain-of-truth property that
the tail mixture universes 𝜌𝑎𝑖¯<𝑡 (¯
𝑎𝑡:𝑡′ ) converge to the tail ground-truth distribution 𝜋𝑎¯<𝑡 (¯
𝑎𝑡:𝑡′ ) as 𝑡 → ∞
𝜋-almost-surely. It follows that for each 𝜖 > 0, there exists a finite time 𝑇 ( 𝜖) such that for all 𝑡 ≥ 𝑇 ( 𝜖),
with probability greater than 1 − 𝜖, we have that 𝐷∞ ( 𝜌𝑎𝑖¯<𝑡 , 𝜋𝑎¯<𝑡 ) ≤ 𝜖, thereby concluding the proof.
102

C.3. Proof of Proposition 4.17
We start by restating the definition of the subjective Nash equilibrium (Definition 4.3, now tailored
towards repeated games. Note that Kalai and Lehrer (1993b) call this repeated-games version of the
subjective Nash equilibrium a subjective equilibrium in short.
Definition C.3 (Subjective equilibrium (Kalai and Lehrer, 1993b)). A set of policies ( 𝜋𝑖 ) 𝑖𝑁=1 and agent
models { 𝜁 𝑖𝑗 } 𝑖 ∈ 𝑁, 𝑗 ∈ 𝑁 is a subjective equilibrium in the repeated game setting if for each player 𝑖 it holds
that
(i) 𝜁 𝑖𝑖 = 𝜋𝑖 ,
(ii) 𝜋𝑖 is a best response w.r.t. 𝜁 𝑖− 𝑖 , where 𝜁 𝑖− 𝑖 ( 𝑎− 𝑖 | 𝑎¯<𝑡 ) :=

Î

𝑖
𝑗
¯<𝑡 ), and
𝑗≠ 𝑖 𝜁 𝑗 ( 𝑎 | 𝑎

(iii) 𝜁 𝑖 (¯
𝑎<𝑡 ) = 𝜋 (¯
𝑎<𝑡 ) ∀¯
𝑎<𝑡 ∈ Ā ∗ with
𝜁 (¯
𝑎<𝑡 ) :=
𝑖

𝑡 −1 Ö
Ö

𝜁 𝑖𝑗 ( 𝑎𝑘 | 𝑎
¯<𝑘 ) ,
𝑗

𝑘=1 𝑗 ∈ 𝑁

𝜋 (¯
𝑎<𝑡 ) :=

𝑡 −1 Ö
Ö

𝜋 𝑗 ( 𝑎𝑘 | 𝑎
¯<𝑘 ) .
𝑗

𝑘=1 𝑗 ∈ 𝑁

Here, 𝜁 𝑖𝑗 indicates player 𝑖’s model of player 𝑗.
We first show that the set of policies {𝜋𝑖𝐷 } that form a subjective embedded equilibrium with decoupled
completed conditionals also form a subjective equilibrium according to the above definition.
As we assume that the completed conditionals are decoupled, i.e.,
Ö
𝜌𝑖 ( 𝑎 − 𝑖 | 𝑎
¯<𝑡 , 𝑎𝑖 ) =
𝜌𝑖 ( 𝑎 𝑗 | 𝑎
¯<𝑡 ) ,
𝑗≠ 𝑖

this leads to a predictive model that can be fully factorized with the marginals:
Ö
𝜌𝑖 (¯
𝑎|𝑎
¯<𝑡 ) =
𝜌𝑖 ( 𝑎 𝑗 | 𝑎
¯<𝑡 ) .
𝑗∈ 𝑁

Hence, each 𝜌𝑖 ( 𝑎 𝑗 | 𝑎¯<𝑡 ) can be interpreted as player 𝑖’s model of player 𝑗, i.e., 𝜁 𝑖𝑗 in the terminology
of the subjective equilibria. To compute an embedded best response following equation 10, we need
to insert a 𝜋𝑖 into 𝜌𝑖 following equation 9:
𝜌𝑖

 𝜋𝑖

(¯
𝑎<𝑡 ) :=

𝑡Ö
−1
𝑘=1

𝜋𝑖 ( 𝑎𝑖𝑘 | 𝑎
¯<𝑘 )

Ö

𝜌𝑖 ( 𝑎 𝑘 | 𝑎
¯<𝑘 ) .
𝑗

𝑗≠ 𝑖

Computing an embedded best response w.r.t. the above distribution is equivalent to computing a
Î
best response against 𝜁 𝑖− 𝑖 , if 𝜁 𝑖− 𝑖 ( 𝑎− 𝑖 | 𝑎¯<𝑡 ) = 𝑗≠𝑖 𝜌𝑖 ( 𝑎 𝑗 | 𝑎¯<𝑡 ) which is true in our setup. Hence, taking
𝜁 𝑖𝑗 ( 𝑎 𝑗 | 𝑎
¯<𝑡 ) = 𝜌𝑖 ( 𝑎 𝑗 | 𝑎¯<𝑡 ) for 𝑖 ≠ 𝑗 and 𝜁 𝑖𝑖 = 𝜋𝑖 , combined with best-response policies {𝜋𝑆𝑖 } 𝑖 ∈ 𝑁 w.r.t. 𝜁 𝑖− 𝑖
leads to a subjective equilibrium according to Definition C.3, with {𝜋𝑆𝑖 } 𝑖 ∈ 𝑁 equal to the embedded
best responses {𝜋𝑖𝐷 } 𝑖 ∈ 𝑁 from the subjective embedded equilibrium, thereby concluding the first part
of the proof.
Finally, we can use proposition 1 of Kalai and Lehrer (1993b) stating that for each subjective equilibrium {𝜋𝑆𝑖 } 𝑖 ∈ 𝑁 , there exists a Nash equilibrium {𝜋𝑖𝐴 } 𝑖 ∈ 𝑁 for which 𝜋
¯𝑆 (¯
𝑎<𝑡 ) = 𝜋
¯ 𝐴 (¯
𝑎<𝑡 ), thereby concluding
the proof.
103

C.4. Proof of Corollary 4.18
The percepts 𝑒𝑡𝑖 of agent 𝑖 is equal to the actions 𝑎𝑡− 𝑖 of the other agents, in our setup of repeated
games. Using the proof technique of Proposition 3.17, it is easy to show that the self-model 𝜌𝑖 ( 𝑎𝑖 | 𝑎¯<𝑡 )
and environment model 𝜌𝑖 ( 𝑒𝑖 | 𝑎¯<𝑡 𝑎𝑖 ) are equivalent to independent agent models with independent
beliefs:
Ö
𝜌𝑖 ( 𝑎 𝑖 | 𝑎
¯<𝑡 ) = 𝜁 𝑖𝑖 ( 𝑎𝑖 | 𝑎¯<𝑡 ) , 𝜌𝑖 ( 𝑎− 𝑖 | 𝑎¯<𝑡 𝑎𝑖 ) =
𝜁 𝑖𝑗 ( 𝑎 𝑗 | 𝑎
¯<𝑡 )
𝑗≠ 𝑖

𝜁 𝑖𝑗 ( 𝑎 𝑗 | 𝑎
¯<𝑡 ) :=

∑︁

𝑤𝑖𝑗 ( 𝜋 𝑗 | 𝑎
¯<𝑡 ) 𝜋 𝑗 ( 𝑎 𝑗 | 𝑎¯<𝑡 ) ,
𝑗

𝜋 𝑗 ∈ Mpol
𝑗
𝜋 𝑗 ( 𝑎𝑡 | 𝑎
¯<𝑡 )
𝑖
𝑗
𝑖
𝑗
𝑤 𝑗 (𝜋 | 𝑎
¯1:𝑡 ) := 𝑤 𝑗 ( 𝜋 | 𝑎¯<𝑡 )
,
𝑗
𝑖
¯<𝑡 )
𝜁 𝑗 ( 𝑎𝑡 | 𝑎

𝑤𝑖𝑗 ( 𝜋 𝑗 | 𝜀) := 𝑤
˜ 𝑖 (𝜋 𝑗 ) .

Using Theorem 4.12, we have that for each 𝜖 > 0, there exists a time 𝑇 ( 𝜖) such that for all 𝑡 ≥ 𝑇 ( 𝜖),
with probability at least 1 − 𝜖, the joint policy ( 𝜋𝑖 ) 𝑖𝑁=1 and subjective mixture models { 𝜌𝑖 } 𝑖 ∈ 𝑁 are
an 𝜖-subjective embedded equilibrium. As we have independent agent models, we can use the
same proof technique as in Proposition 4.17 to show that in this case, an 𝜖-subjective embedded
equilibrium corresponds to an 𝜖-subjective Nash equilibrium in repeated games, with an 𝜖-subjective
Nash equilibrium defined as in Definition C.3 with the third condition replaced by 𝜁 𝑖 (¯
𝑎<𝑡 ) is 𝜖-close to
𝜋 (¯
𝑎<𝑡 ) in total variation distance. Now we can directly use Theorem 1 of Kalai and Lehrer (1993b) to
conclude our proof:
Theorem C.4 (Theorem 1 of Kalai and Lehrer (1993b)). In infinitely repeated games, for every 𝜖 > 0,
there is 𝜖′ > 0 such that for all 𝜖′′ ≤ 𝜖′ , if 𝜋
¯ is an 𝜖′′ -subjective Nash equilibrium, then there exists a joint
′
policy 𝜋 such that
𝑎<𝑡 ) is 𝜖-close to 𝜋′ (¯
𝑎<𝑡 );
(i) 𝜋 (¯

(ii) 𝜋′ is an 𝜖-Nash equilibrium.
C.5. Proof of Proposition 4.22
Proof. The proof consists of two parts. First, we show that every Embedded Equilibrium (EE) is a
Subjective Embedded Equilibrium (SEE). Second, we provide a counterexample to show that the
converse is not true.
Part 1: Every EE is an SEE
We do the proof for the general case of MAGRL, which also holds for the repeated games setting. Let
a set of policies ( 𝜋𝑖 ) 𝑖𝑁=1 and a single dependency distribution 𝑞 constitute an Embedded Equilibrium
(EE), using 𝑞 conditionally complete the ground-truth universe 𝜐:
𝜐𝑖 ( 𝑒𝑖 | æ𝑖<𝑡 , 𝑎𝑖 ) = 𝜐𝑖 ( 𝑒𝑖 | æ𝑖<𝑡 , 𝑎𝑖 )

if 𝜐𝑖 (æ𝑖<𝑡 , 𝑎𝑖 ) > 0 ,

𝜐𝑖 ( 𝑒𝑖 | æ𝑖<𝑡 , 𝑎𝑖 ) = 𝑞 ( 𝑒𝑖 | æ𝑖<𝑡 , 𝑎𝑖 )

otherwise .

We can construct a corresponding set of subjective predictive distributions { 𝜌𝑖 } 𝑖 ∈ 𝑁 by setting, for each
agent 𝑖 ∈ 𝑁 , its subjective model and its conditional completion equal to the conditionally completed
𝜐 by 𝑞. The best response condition, and the conditionally completed 𝜐 of the EE directly imply
the two conditions for a Subjective Embedded Equilibrium (SEE) (Subjective Best Response and
Uncontradicted Beliefs). It therefore immediately follows from the definitions that every EE is also an
SEE.
104

Part 2: An SEE that is not an EE
We construct a counterexample using a two-player, single-shot normal-form game, as this also serves
as a counterexample for the more general MAGRL setting. Let the players be 𝑖 ∈ {1, 2}, with action
spaces A 1 = A 2 = { 𝐴, 𝐵, 𝐶 }. The payoff matrix ( 𝑟 1 , 𝑟 2 ) is given by

𝐴
𝐵
𝐶

𝐴

𝐵

𝐶

(2, 2)
(7, 0)
(7, 0)

(0, 7)
(6, 1)
(1, 6)

(0, 7)
(1, 6)
(6, 1)

where the rows correspond to the actions of the first player and the columns correspond to the actions
of the second player.
Consider the deterministic joint policy 𝜋
¯ where both agents play action 𝐴, i.e., 𝜋1 ( 𝐴) = 1 and 𝜋2 ( 𝐴) = 1.
The resulting distribution over histories is a point mass on the outcome ( 𝐴, 𝐴), so 𝜋
¯ ( 𝐴, 𝐴) = 1.
Step A: Show this is a Subjective Embedded Equilibrium (SEE). Consider the following subjective
beliefs for off-path actions:
• For Agent 1: 𝜌1 ( 𝑎2 = 𝐶 | 𝑎1 = 𝐵) = 1 and 𝜌1 ( 𝑎2 = 𝐵 | 𝑎1 = 𝐶 ) = 1.
• For Agent 2: 𝜌2 ( 𝑎1 = 𝐵 | 𝑎2 = 𝐵) = 1 and 𝜌2 ( 𝑎1 = 𝐶 | 𝑎2 = 𝐶 ) = 1.
With these beliefs, each agent calculates their expected payoff for deviating to B or C as 1, which
is less than the equilibrium payoff of 2 from playing A. The beliefs are uncontradicted because the
play-path is always ( 𝐴, 𝐴), satisfying 𝜌𝑖 ( 𝐴, 𝐴) = 𝜋
¯ ( 𝐴, 𝐴) = 1. Thus, this constitutes a valid SEE.
Step B: Show this is not an Embedded Equilibrium (EE). We show by contradiction that there is no
single dependency distribution 𝑞 which can make this an EE. Assume such an EE exists, supported by a
conditional completion of the ground-truth universe 𝜐 by dependency distribution 𝑞. Each conditional
completion can be derived from a limit of a sequence ( 𝑝𝑟 )𝑟 of joint distributions satisfying the grainof-uncertainty property. Let us take such sequence ( 𝑝𝑟 )𝑟 to represent the conditional completion of 𝜐.
The best response condition implies that 𝑄 𝑖 ( 𝐴) ≥ 𝑄 𝑖 ( 𝐵) and 𝑄 𝑖 ( 𝐴) ≥ 𝑄 𝑖 ( 𝐶 ). Since




2 = 𝑄 1 ( 𝐴) ≥ 𝑄 1 ( 𝐵) = 𝔼𝑞 ( 𝑎2 | 𝑎1 =𝐵 ) 𝑟 1 ( 𝐵, 𝑎2 ) = lim 𝔼 𝑝𝑟 ( 𝑎2 | 𝑎1 =𝐵 ) 𝑟 1 ( 𝐵, 𝑎2 ) ,
𝑟 →∞

there exists 𝑟 large enough so that

 7 𝑝𝑟 ( 𝐵, 𝐴) + 6 𝑝𝑟 ( 𝐵, 𝐵) + 𝑝𝑟 ( 𝐵, 𝐶 )
𝔼 𝑝𝑟 ( 𝑎2 | 𝑎1 =𝐵 ) 𝑟 1 ( 𝐵, 𝑎2 ) =
≤ 𝑄 𝑖 ( 𝐴) + 1 = 3 .
𝑝𝑟 ( 𝐵, 𝐴) + 𝑝𝑟 ( 𝐵, 𝐵) + 𝑝𝑟 ( 𝐵, 𝐶 )
Similarly, we can show that for 𝑟 large enough, we have

 7 𝑝𝑟 ( 𝐶, 𝐴) + 𝑝𝑟 ( 𝐶, 𝐵) + 6 𝑝𝑟 ( 𝐶, 𝐶 )
𝔼 𝑝𝑟 ( 𝑎2 | 𝑎1 =𝐶 ) 𝑟 1 ( 𝐶, 𝑎2 ) =
≤ 𝑄 𝑖 ( 𝐴) + 1 = 3 ,
𝑝𝑟 ( 𝐶, 𝐴) + 𝑝𝑟 ( 𝐶, 𝐵) + 𝑝𝑟 ( 𝐶, 𝐶 )

 7 𝑝𝑟 ( 𝐴, 𝐵) + 𝑝𝑟 ( 𝐵, 𝐵) + 6 𝑝𝑟 ( 𝐶, 𝐵)
𝔼 𝑝𝑟 ( 𝑎1 | 𝑎2 =𝐵 ) 𝑟 2 ( 𝑎1 , 𝐵) =
≤ 𝑄 𝑖 ( 𝐴) + 1 = 3 ,
𝑝𝑟 ( 𝐴, 𝐵) + 𝑝𝑟 ( 𝐵, 𝐵) + 𝑝𝑟 ( 𝐶, 𝐵)

 7 𝑝𝑟 ( 𝐴, 𝐶 ) + 6 𝑝𝑟 ( 𝐵, 𝐶 ) + 𝑝𝑟 ( 𝐶, 𝐶 )
𝔼 𝑝𝑟 ( 𝑎1 | 𝑎2 =𝐶 ) 𝑟 2 ( 𝑎1 , 𝐶 ) =
≤ 𝑄 𝑖 ( 𝐴) + 1 = 3 .
𝑝𝑟 ( 𝐴, 𝐶 ) + 𝑝𝑟 ( 𝐵, 𝐶 ) + 𝑝𝑟 ( 𝐶, 𝐶 )

105

We can rewrite the above four inequalities as
4 𝑝𝑟 ( 𝐵, 𝐴) + 3 𝑝𝑟 ( 𝐵, 𝐵) ≤ 2 𝑝𝑟 ( 𝐵, 𝐶 ) ,
4 𝑝𝑟 ( 𝐶, 𝐴) + 3 𝑝𝑟 ( 𝐶, 𝐶 ) ≤ 2 𝑝𝑟 ( 𝐶, 𝐵) ,
4 𝑝𝑟 ( 𝐴, 𝐵) + 3 𝑝𝑟 ( 𝐶, 𝐵) ≤ 2 𝑝𝑟 ( 𝐵, 𝐵) ,
4 𝑝𝑟 ( 𝐴, 𝐶 ) + 3 𝑝𝑟 ( 𝐵, 𝐶 ) ≤ 2 𝑝𝑟 ( 𝐶, 𝐶 ) ,
which can be simultaneously satisfied only when
𝑝𝑟 ( 𝐵, 𝐴) = 𝑝𝑟 ( 𝐶, 𝐴) = 𝑝𝑟 ( 𝐴, 𝐵) = 𝑝𝑟 ( 𝐴, 𝐶 ) = 𝑝𝑟 ( 𝐵, 𝐵) = 𝑝𝑟 ( 𝐶, 𝐶 ) = 𝑝𝑟 ( 𝐶, 𝐵) = 𝑝𝑟 ( 𝐵, 𝐶 ) = 0 .

But this contradicts the grain-of-uncertainty assumption about 𝑝𝑟 . Hence, there does not exist any 𝑝𝑟
that satisfies the grain-of-uncertainty property whose conditionals converge to a completion of 𝜐 that
satisfies the best-response inequalities. Therefore, no EE exists for this policy profile.
□
C.6. Proof of Theorem 4.24
We begin by establishing the formal relationship between Subjective Embedded Equilibria (SEE) and
Embedded Equilibria (EE) under the assumption of a common mixture model.
Lemma C.5 (SEE with Common Beliefs implies EE). Let ({𝜋𝑖 } 𝑖 ∈ 𝑁 , { 𝜌𝑖 } 𝑖 ∈ 𝑁 ) be a Subjective Embedded
Equilibrium (SEE) for a repeated game with perfect monitoring. If all agents share the same mixture
universe and its conditional completion, i.e., 𝜌𝑖 = 𝜌 for all 𝑖 ∈ 𝑁 , then the set of policies {𝜋𝑖 } 𝑖 ∈ 𝑁 constitutes
an Embedded Equilibrium (EE) w.r.t. the dependency distribution 𝑞 = 𝜌.
Proof. By the definition of an SEE (Definition 4.15), two conditions hold:
1. (Best Response) Each agent’s policy 𝜋𝑖 is an embedded best response to the conditional
completion of the common mixture universe 𝜌.
2. (Uncontradicted Beliefs) The mixture 𝜌 is identical to the ground-truth personal universe 𝜐𝑖
𝑖
on the play path, i.e., 𝜌 (¯
𝑎1:𝑡 ) = 𝜐𝑖 (¯
𝑎1:𝑡 ) = ( 𝜇 𝑖 ) 𝜋 (¯
𝑎1:𝑡 ) for all 𝑎
¯1:𝑡 ∈ Ā ∗ .
We show that {𝜋𝑖 } 𝑖 ∈ 𝑁 is an EE. Let the EE policies be 𝑓 𝑖 = 𝜋𝑖 . The corresponding ground-truth universe
𝑖
𝑖
is 𝜐 𝑓 = ( 𝜇 𝑖 ) 𝑓 = ( 𝜇 𝑖 ) 𝜋 = 𝜐𝑖 . We must specify a dependency distribution 𝑞 as required by Definition
4.19. We define 𝑞 using the conditional completion of 𝜌:
𝑞 ( 𝑎− 𝑖 | 𝑎
¯<𝑡 , 𝑎𝑖 ) := 𝜌 ( 𝑎− 𝑖 | 𝑎¯<𝑡 , 𝑎𝑖 )

∀(¯
𝑎<𝑡 , 𝑎𝑖 ) .

We now verify that 𝑓 𝑖 = 𝜋𝑖 is a best response with respect to the 𝑞-completion of 𝜐 𝑓 . This 𝑞-completion
is defined by conditionals 𝜐˜ 𝑓 (· | ·) such that:
(
𝜐 𝑓 ( 𝑎− 𝑖 | 𝑎
¯<𝑡 , 𝑎𝑖 ) if 𝜐 𝑓 (¯
𝑎<𝑡 , 𝑎𝑖 ) > 0
𝜐
˜ 𝑓 ( 𝑎− 𝑖 | 𝑎¯<𝑡 , 𝑎𝑖 ) =
𝑞 ( 𝑎− 𝑖 | 𝑎
¯<𝑡 , 𝑎𝑖 )
if 𝜐 𝑓 (¯
𝑎<𝑡 , 𝑎𝑖 ) = 0
From condition (2), on the play path (where 𝜐 𝑓 (¯
𝑎<𝑡 , 𝑎𝑖 ) > 0), we have 𝜐 𝑓 = 𝜌, and thus 𝜐 𝑓 (· | ·) = 𝜌 (· | ·).
Off the play path (where 𝜐 𝑓 (¯
𝑎<𝑡 , 𝑎𝑖 ) = 0), the 𝑞-completion uses 𝑞 (· | ·), which we defined as the
conditional completion of 𝜌. Therefore, the 𝑞-completed universe 𝜐˜ 𝑓 is identical to the completed
mixture universe 𝜌. By condition (1), 𝜋𝑖 is a best response to 𝜌. It follows that 𝑓 𝑖 = 𝜋𝑖 is a best
response to 𝜐˜ 𝑓 , satisfying Definition 4.19.
□
106

This equivalence allows us to adapt the arguments of Kalai and Lehrer (1993b) to approximate
equilibria. Let us first define a new variant of the SEE that both has an approximate best response
and approximate beliefs.
Definition C.6 (( 𝛿, 𝜂)-Subjective Embedded Equilibrium). Let 𝛿 ≥ 0 and 𝜂 ≥ 0. A set of policies {𝜋𝑖 } 𝑖 ∈ 𝑁
and subjective mixture universes { 𝜌𝑖 } 𝑖 ∈ 𝑁 (each with a specified conditional completion) constitutes a
( 𝛿, 𝜂)-Subjective Embedded Equilibrium if, for each agent 𝑖:
1. (𝛿-Subjective Best Response) The agent’s policy 𝜋𝑖 is a 𝛿-best response with respect to its
subjective mixture universe 𝜌𝑖 : 𝑉( 𝜌𝑖 ) 𝜋𝑖 ( 𝜀) ≥ max𝜋 𝑉( 𝜌𝑖 ) 𝜋 ( 𝜀) − 𝛿
2. (𝜂-Uncontradicted Beliefs) The subjective beliefs 𝜌𝑖 are 𝜂-close in total variation distance to
𝑖
𝑖
the ground-truth personal distribution ( 𝜇 𝑖 ) 𝜋 : 𝐷∞ ( 𝜌𝑖 , ( 𝜇 𝑖 ) 𝜋 | 𝜀) ≤ 𝜂
Lemma C.7 (Finite Games: ( 𝛿, 𝜂)-SEE plays 𝜖-like a 𝛿-EE). In finitely repeated games, for every 𝜖 > 0
and 𝛿 ≥ 0, there exists an 𝜂¯ > 0 such that for all 0 < 𝜂 ≤ 𝜂¯, if a set of policies ( 𝜋𝑖 ) 𝑖 and subjective mixtures
( 𝜌𝑖 ) 𝑖 are a ( 𝛿, 𝜂)-SEE where all agents use an identical subjective mixture 𝜌𝑖 = 𝜌 with identical conditional
¯
completions, then there exists a set of policies ( 𝑓 𝑖 ) 𝑖 such that: (i) ( 𝜋𝑖 ) 𝑖 plays 𝜖-like ( 𝑓 𝑖 ) 𝑖 : 𝐷∞ ( 𝜇 𝜋 , 𝜇 𝑓 ) < 𝜖,
and (ii) ( 𝑓 𝑖 ) 𝑖 is a 𝛿-EE.
Proof. We follow the proof strategy of Kalai and Lehrer (1993b, Proposition 2). Assume for contradiction that ∃𝜖 > 0, 𝛿 ≥ 0 such that ∀¯
𝜂 > 0, ∃𝜂 ≤ 𝜂¯ and a ( 𝛿, 𝜂)-SEE ( 𝜋𝑖 , 𝜌𝑖 ) 𝑖 that does not play 𝜖-like
any 𝛿-EE. Let us introduce the vector 𝑔 = ( 𝜋𝑖 , 𝜌𝑖 ) 𝑖𝑁=1 . The starting assumption allows the construction
of a sequence of vectors { 𝑔 ( 𝑚)}∞
such that 𝑔 ( 𝑚) is a ( 𝛿, 𝜂𝑚 )-SEE with 𝜂𝑚 → 0 as 𝑚 → ∞, and no
𝑚=1
𝑔 ( 𝑚) plays 𝜖-like any 𝛿-EE. The set of behavior strategies in a finitely repeated game is sequentially
compact. Therefore, there exists a subsequence 𝑔 ( 𝑚𝑘 ) that converges to a limit strategy 𝑔 . By the
continuity of the payoff functions, the limit strategy 𝑔 must be a ( 𝛿, 0)-SEE. That is, the policies ( 𝜋𝑖 ) 𝑖 in
𝑔 are a 𝛿-best response to the common belief 𝜌 in 𝑔 that is 0-close (i.e., identical) to the ground-truth
𝜇 𝜋 . By the logic of Lemma C.5, this 𝑔 is a 𝛿-EE. Since 𝑔 ( 𝑚) → 𝑔 and the measure-inducing map is
continuous, for 𝑚 sufficiently large (and thus 𝜂𝑚 sufficiently small), 𝑔 ( 𝑚) must play 𝜖-like 𝑔 . This
contradicts the premise that no 𝑔 ( 𝑚) plays 𝜖-like any 𝛿-EE, as 𝑔 itself is a 𝛿-EE. The initial assumption
must be false.
□
We now bridge the gap between finite and infinite games, proving the core relationship between
𝜂-SEEs and 𝜖-EEs.
Lemma C.8 (𝜂-SEE plays 𝜖-like an 𝜖-EE). In infinitely repeated games, for every 𝜖 > 0, there exists an
𝜂¯ > 0 such that for all 0 < 𝜂 ≤ 𝜂¯, if ( 𝜋𝑖 , 𝜌𝑖 ) 𝑖𝑁=1 is an 𝜂-SEE, where all agents use an identical subjective
mixture 𝜌𝑖 = 𝜌 with identical conditional completions, then there exists a set of policies ( 𝑓 𝑖 ) 𝑖𝑁=1 such that:
¯

(i) ( 𝜋𝑖 ) 𝑖 plays 𝜖-like ( 𝑓 𝑖 ) 𝑖 : 𝐷∞ ( 𝜇 𝜋 , 𝜇 𝑓 ) < 𝜖, and (ii) ( 𝑓 𝑖 ) 𝑖 is an 𝜖-EE.
Proof. Let 𝜖 > 0 be given. Due to the discount factor 𝛾 ∈ [0, 1), there exists a finite time 𝑙 = 𝑙 ( 𝜖) ∈ ℕ
such that the maximum possible discounted payoff attainable from period 𝑙 + 1 onwards is less than
𝜖/2. Let 𝑔 = ( 𝜋𝑖 , 𝜌𝑖 ) 𝑖𝑁=1 be an 𝜂-SEE for the infinite game. By Definition 4.11, 𝜋𝑖 is a 0-best response
to its subjective mixture 𝜌 which is 𝜂-close to the ground-truth personal distribution 𝜐𝑖 . Consider
the 𝑙-truncation of all strategies and subjective mixtures. The truncated strategy 𝜋𝑖𝑙 is an 𝜖/2-best
response to the truncated subjective mixture 𝜌𝑙 , as the maximal utility loss from truncation is 𝜖/2.
The truncated subjective mixture 𝜌𝑙 remains 𝜂-close to the truncated ground-truth 𝜐𝑖𝑙 . Thus, 𝑔𝑙 is an
( 𝜖/2, 𝜂)-SEE for the 𝑙 -fold finite game. By Lemma C.7 (with 𝛿 = 𝜖/2), there exists an 𝜂¯ > 0 (which

107

depends on 𝜖 via 𝑙 ) such that if 𝜂 ≤ 𝜂¯, 𝑔𝑙 plays 𝜖-like some 𝜖/2-EE, 𝑓𝑙 . We construct infinite strategies
( 𝑓 𝑖 ) 𝑖 by extending 𝑓𝑙𝑖 with 𝜋𝑖 after period 𝑙:
(
𝑓 𝑖 (¯
𝑎∗ ) :=

𝑓𝑙𝑖 (¯
𝑎∗ )
𝜋 (¯
𝑎∗ )
𝑖

if 𝑙 (¯
𝑎∗ ) < 𝑙
if 𝑙 (¯
𝑎∗ ) ≥ 𝑙

We verify the two conditions for 𝑓 : (i) ( 𝜋𝑖 ) 𝑖 play 𝜖-like ( 𝑓 𝑖 ) 𝑖 : As ( 𝜋𝑖𝑙 ) 𝑖 play 𝜖-like ( 𝑓𝑙𝑖 ) 𝑖 in the 𝑙 -fold
game, and 𝑓 𝑖 and 𝜋𝑖 are identical for all histories 𝑎¯∗ with 𝑙 (¯
𝑎∗ ) ≥ 𝑙 , the induced distributions 𝜇 𝜋 and
¯
𝜇 𝑓 are 𝜖-close. (ii) ( 𝑓 𝑖 ) 𝑖 is an 𝜖-EE: We check that 𝑓 𝑖 is an 𝜖-best response. Since ( 𝑓𝑙𝑖 ) 𝑖 is an 𝜖/2-EE, any
deviation in the first 𝑙 periods yields a payoff gain of at most 𝜖/2 during those periods. The maximum
possible gain from any action taken after period 𝑙 is bounded by 𝜖/2. Therefore, the total possible
gain from any deviation from 𝑓 𝑖 is at most 𝜖/2 + 𝜖/2 = 𝜖. Thus, ( 𝑓 𝑖 ) 𝑖 is an 𝜖-EE, with dependency
distribution 𝑞 having conditionals equal to the conditional completion of the common mixture 𝜌. □
We now state and prove the main theorem.
Theorem C.9 (Convergence to 𝜖-Embedded Equilibrium). Let { 𝜌𝑖 } 𝑖 ∈ 𝑁 be Bayesian mixture universes
satisfying the grain-of-uncertainty and grain-of-truth conditions, and let {𝜋𝑖 } 𝑖 ∈ 𝑁 be the corresponding
embedded best response policies in an infinitely repeated game with perfect monitoring. If the mixtures
{ 𝜌𝑖 } 𝑖 ∈ 𝑁 of all the players are the same mixture, i.e., 𝜌𝑖 = 𝜌 𝑗 ∀𝑖, 𝑗 ∈ 𝑁 , then, for each 𝜖 > 0, there exists a
finite time 𝑇 ( 𝜖) such that for all 𝑡 ≥ 𝑇 ( 𝜖), with probability greater than 1 − 𝜖, the tail distribution 𝜇¯𝜋𝑎¯¯<𝑡
induced by the tail policies 𝜋𝑎𝑖¯<𝑡 is 𝜖-close to the distribution induced by some policies constituting an
𝜖-embedded equilibrium in the tail game starting at time 𝑡 .
Proof. Let 𝜖 > 0 be given. From Lemma C.8, there exists an 𝜂¯ > 0 (which depends on 𝜖) such that any
𝜂-SEE with 𝜂 ≤ 𝜂¯ plays 𝜖-like an 𝜖-EE. Let 𝜂′ = min( 𝜖, 𝜂¯). As the mixture universes 𝜌𝑖 satisfy grain of
truth and grain of uncertainty, and as all agents share the same mixture, it follows by Theorem 4.12
(Convergence to 𝜖-SEE) that for 𝜂′ > 0, there exists a finite time 𝑇 ( 𝜂′ ) such that for all 𝑡 ≥ 𝑇 ( 𝜂′ ), with
probability ≥ 1 − 𝜂′ , the agents’ tail play ( 𝜋𝑎𝑖¯<𝑡 , 𝜌𝑖𝑎¯<𝑡 ) constitutes an 𝜂′ -SEE, where all agents have an
equal tail mixture 𝜌𝑖𝑎¯<𝑡 = 𝜌𝑎¯<𝑡 . Since 𝜂′ ≤ 𝜂¯, Lemma C.8 applies to the tail play ( 𝜋𝑖𝑎¯<𝑡 , 𝜌𝑎𝑖¯<𝑡 ). Therefore,
𝜋
¯

the tail distribution 𝜇¯ 𝑎¯<𝑡𝑎¯<𝑡 is 𝜖-close to the distribution induced by some policies ( 𝑓 𝑖 ) 𝑖 constituting an
𝜖-EE for the tail game. Furthermore, since 𝜂′ ≤ 𝜖, the probability of this event, 1 − 𝜂′ , is ≥ 1 − 𝜖. This
completes the proof.
□
C.7. Proof of Theorem 4.28
(i) As 𝜌𝑖 satisfies the grain-of-uncertainty assumption, its conditionals are always well-defined and
hence its conditional completion is unique, and as a result there exists an embedded best response
w.r.t. 𝜌𝑖 that is equal to 𝜋𝑖 . (ii) From Theorem 3.11, it follows from the grain-of-truth property that
 𝜋æ𝑖 𝑖
𝑖
𝑖
<𝑡 as 𝑡 → ∞
the tail mixture universes 𝜌æ
converge to the tail ground-truth distribution 𝜇 æ
𝑖
𝑖
<𝑡

<𝑡

𝜇 𝜋 -almost-surely. It follows that for each 𝜖 > 0, there exists a finite time 𝑇 ( 𝜖) such that for all 𝑡 ≥ 𝑇 ( 𝜖),

 𝜋𝑖
with probability greater than 1 − 𝜖, we have that 𝐷∞ ( 𝜌𝑖 , 𝜇 𝑖
| æ𝑖<𝑡 ) ≤ 𝜖. (iii) The tail policies
𝑖
and tail environment are conditioned on the personal histories æ<𝑡 , which can differ for each agent
due to partial observability; hence these histories serve as a correlation device ((AE) 𝑡 −1 , 𝜇 𝜋 ) for the
subsequent tail policies, leading to an 𝜖-subjective correlated equilibrium instead of an 𝜖-subjective
embedded equilibrium.

108

C.8. Proof of Proposition 4.29
We follow an approach inspired by the dogmatic beliefs introduced by Leike and Hutter (2015b). We
will construct for each agent 𝑖 a mixture model 𝜌𝑖 with completed conditionals that predicts eternal
rewards of 0 after deviating at least once from the deterministic policy 𝜋𝑖 , such that following the
policy 𝜋𝑖 is always an embedded best response according to equation 10 (in the worst-case, 𝜋𝑖 also
results in an expected future return of 0, but then 𝜋𝑖 still qualifies as an embedded best response, as
all alternatives also lead to an expected return of 0).
In the following, we assume without loss of generality that the minimum reward in R is equal to 0.
Let us define the finite set E0𝑖 as the set of percepts encoding a reward of 0:
E0𝑖 := { 𝑒𝑖 ∈ E 𝑖 : 𝑟 𝑖 ( 𝑒𝑖 ) = 0} .
∗
𝑖
Let us define the function dev : AE 𝑖 × Mpol
→ ℕ+ that computes the first timestep 𝑡 where the
action 𝑎𝑡𝑖 in history æ∗𝑖 deviates from the action prescribed by the deterministic policy 𝜋𝑖 . If æ∗𝑖 does
𝑖
𝑖
𝑖
not deviate from 𝜋𝑖, then we let dev(æ
∗ , 𝜋 ) := 𝑙 (æ∗ ) + 1. Now let us introduce the following two

∗
∗
measures over AE 𝑖 ∪ AE 𝑖 × A 𝑖 :
𝜆 dogmatic (æ∗ ) :=
𝑖

𝑖
dev(æ∗
,𝜋𝑖 ) −1
Ö

𝑡 =1

1
𝑖
|A ||E 𝑖 |

𝑙Ö
(æ∗𝑖 )

𝛿 ( 𝑒𝑡𝑖 ∈ E0𝑖 )

𝑡 =dev(æ ,𝜋𝑖 )

|A 𝑖 ||E0𝑖 |

𝑖

∗

,

1
𝜆 dogmatic (æ∗𝑖 𝑎𝑖 ) := 𝜆 dogmatic (æ∗𝑖 )
,
|A 𝑖 |
1
𝑖
𝜆 random (æ1:
𝑡 ,
𝑡 ) :=
|A 𝑖 ||E 𝑖 |
1
𝑖
𝑖
𝑖
𝜆 random (æ1:
,
𝑡 𝑎 ) := 𝜆 random (æ1:𝑡 )
|A 𝑖 |
with 𝛿 ( 𝑒𝑡𝑖 ∈ E0𝑖 ) the indicator function indicating whether 𝑒𝑡𝑖 ∈ E0𝑖 . Hence, for histories æ∗𝑖 where there
is at least 1 action deviating from the one prescribed by 𝜋𝑖 , 𝜆 dogmatic only assigns non-zero probability
to histories that have 0 reward after deviating for the first time from 𝜋𝑖 .
 𝜋𝑖
Take 𝜇 𝑖 (æ∗𝑖 ) as the personal trajectory distribution resulting from marginalizing out the æ∗− 𝑖 in the
ground-truth joint-trajectory distribution 𝜇 𝜋 (æ∗ ). Now we introduce the following infinite sequence
of { 𝜌𝑟𝑖 }𝑟 ∈ℕ to obtain the conditional completions of 𝜌𝑖
𝜌𝑟𝑖 := (1 − 𝜖𝑟 − 𝜖𝑟2 ) 𝜇 𝑖

 𝜋𝑖

+ 𝜖𝑟 𝜆 dogmatic + 𝜖𝑟2 𝜆 random ,

with lim𝑟→∞ 𝜖𝑟 = 0. It is easy to see that 𝜌𝑟𝑖 satisfies the grain-of-uncertainty condition and hence
 𝜋𝑖
in the limit defines a valid conditional completion. Furthermore, we have that lim𝑟→∞ 𝜌𝑟𝑖 = 𝜇 𝑖 ,
and hence the resulting 𝜌𝑖 satisfies the uncontradicted beliefs condition for the subjective embedded
equilibrium (Definition 4.15). It remains to be shown that 𝜋𝑖 is an embedded best response w.r.t. 𝜌𝑖
for all agents 𝑖.
 𝜋𝑖
Consider a history æ𝑖<𝑡 with 𝜇 𝑖 (æ𝑖<𝑡 ) > 0, i.e., all the actions follow 𝜋𝑖 . Now consider that at time 𝑡 ,
 𝜋𝑖
the action 𝑎𝑡𝑖 deviates from the deterministic policy 𝜋𝑖 (æ𝑖<𝑡 ). In this case, 𝜇 𝑖 (æ𝑖<𝑡 𝑎𝑡𝑖 ) = 0 and hence
the predictive distribution 𝜌𝑟𝑖 is equal to
𝜌𝑟𝑖 ( 𝑒𝑡𝑖 æ𝑖>𝑡 | æ𝑖<𝑡 𝑎𝑡𝑖 ) =

𝜖𝑟 𝜆 dogmatic (æ𝑖<𝑡 𝑎𝑡𝑖 𝑒𝑡𝑖 æ𝑖>𝑡 ) + 𝜖𝑟2 𝜆 random (æ𝑖<𝑡 𝑎𝑡𝑖 𝑒𝑡𝑖 æ𝑖>𝑡 )
𝜖𝑟 𝜆 dogmatic (æ𝑖<𝑡 𝑎𝑡𝑖 ) + 𝜖𝑟2 𝜆 random (æ𝑖<𝑡 𝑎𝑡𝑖 )

,

109

and hence

lim 𝜌𝑟𝑖 ( 𝑒𝑡𝑖 æ𝑖>𝑡 | æ𝑖<𝑡 𝑎𝑡𝑖 ) = 𝜆 dogmatic ( 𝑒𝑡𝑖 æ𝑖>𝑡 | æ𝑖<𝑡 𝑎𝑡𝑖 ) ,

𝑟 →∞

for any future trajectory 𝑒𝑡𝑖 æ𝑖>𝑡 . Notice that 𝜆 dogmatic ( 𝑒𝑡𝑖 æ𝑖>𝑡 | æ𝑖<𝑡 𝑎𝑡𝑖 ) only has non-zero probability for
future trajectories 𝑒𝑡𝑖 æ𝑖>𝑡 that have a total sum of rewards of 0. Hence, after deviating once from
𝜋𝑖 , the value of any policy is 0, including the optimal policy. Hence, following the deterministic
policy 𝜋𝑖 is always better or equal to following any other policy, as following another policy leads to
the minimum value of 0. Hence 𝜋𝑖 is an embedded best response w.r.t. 𝜌𝑖 = lim𝑟→∞ 𝜌𝑟𝑖 , and hence
( 𝜋𝑖 , 𝜌𝑖 ) 𝑖 is an SEE. We can repeat the same proof technique for constructing a SNE ( 𝜋𝑖 , 𝜉𝑖 ) 𝑖 , taking
𝜉𝑖 ( 𝑒𝑖 | æ∗𝑖 𝑎𝑖 ) = 𝜌𝑖 ( 𝑒𝑖 | æ∗𝑖 𝑎𝑖 ) for the above constructed 𝜌𝑖 . This concludes the proof.
C.9. Proof of Theorem 4.31
We need a few lemmas, which we state in the single-agent setting for simplicity.
Lemma C.10. For all 𝑘 ≥ 1, we have 𝑄 𝑘𝜌 (æ<𝑡 , 𝑎𝑡 ) ≤ 𝑄 𝑘𝜌+1 (æ<𝑡 , 𝑎𝑡 ).
Proof. This is an immediate corollary from equation 11 that we prove by induction on 𝑘 ≥ 1:
• For 𝑘 = 1, we have
𝑄 1𝜌 (æ<𝑡 , 𝑎𝑡 ) = 𝑄 𝜌 (æ<𝑡 , 𝑎𝑡 )

=

∑︁



𝜌 ( 𝑒𝑡 |æ<𝑡 𝑎𝑡 ) (1 − 𝛾 ) 𝑟 ( 𝑒𝑡 ) + 𝛾𝑉𝜌 (æ<𝑡 𝑎𝑡 𝑒𝑡 )



𝑒𝑡 ∈ E

#

"
=

∑︁

𝜌 ( 𝑒𝑡 |æ<𝑡 𝑎𝑡 ) (1 − 𝛾 ) 𝑟 ( 𝑒𝑡 ) + 𝛾

≤

𝜌 ( 𝑎𝑡+1 |æ<𝑡 𝑎𝑡 𝑒𝑡 ) 𝑄 𝜌 (æ<𝑡 𝑎𝑡 𝑒𝑡 , 𝑎𝑡+1 )

𝑎𝑡+1 ∈ A

𝑒𝑡 ∈ E

∑︁

∑︁



1

𝜌 ( 𝑒𝑡 |æ<𝑡 𝑎𝑡 ) (1 − 𝛾 ) 𝑟 ( 𝑒𝑡 ) + 𝛾 max 𝑄 𝜌 (æ<𝑡 𝑎𝑡 𝑒𝑡 , 𝑎)



𝑎∈ A

𝑒𝑡 ∈ E

= 𝑄 2𝜌 (æ<𝑡 , 𝑎𝑡 ) ,
hence the lemma is correct for 𝑘 = 1.
• Let 𝑘 > 1, and assume that the lemma is true for 

[TRUNCATED]
