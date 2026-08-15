---
title: "Outsourcing Memory Through Niche Construction"
person: david-krakauer
section: by
type: journal-article
year: 2022
date: 2022-09-01
venue: "bioRxiv (Cold Spring Harbor Laboratory)"
authors: "David C. Krakauer et al."
source_url: https://doi.org/10.1101/2022.09.01.506204
retrieved: 2026-08-13
content: full-text
notes: "OA status: green; OpenAlex W4294193436; cited_by 6. Abstract reconstructed from OpenAlex abstract_inverted_index. Full text fetched 2026-08-13 via OpenAlex Content API (grobid_xml -> prose extraction)."
---

# Outsourcing Memory Through Niche Construction

## Full text

**Abstract.** Note that in this binary example, the new environmental configuration when switching is unique, enforcing a deterministic switch, but in general there may be a large number of K ≫ 1 options such that the agent cannot easily guess at the results of environmental fluctuations.

Adaptation to changing environments is a universal feature of life and can involve the organism modifying itself in response to the environment as well as actively modifying the environment to control selection pressures.The latter case couples the organism to environment.Then, how quickly should the organism change in response to the environment?We formulate this question in terms of how memory duration scales with environmental rate of change when there are trade-offs in remembering vs. forgetting.We derive a universal scaling law for optimal memory duration, taking into account memory precision as well as two components of environmental volatility, bias and stability.We find sublinear scaling with any amount of environmental volatility.We use a memory complexity measure to explore the strategic conditions (game dynamics) favoring actively reducing environmental volatility-outsourcing memory through niche construction-over investing in neural tissue.We predict stabilizing niche construction will evolve when neural tissue is costly, the environment is variable, and it is beneficial to be able to encode a rich repertoire of environmental states.

adaptation | learning | stigmergy | niche construction | scaling W hat is the optimal timescale of adaptation-how long should memory of the environment persist when the environment is changing?And when should the organism invest in changing the rate of environmental change?Research in a wide range of fields suggests that bidirectional organism-environment feedback through niche construction and symbiosis is common and plays a significant role in shaping evolutionary dynamics.Slowly evolving genes co-evolve with quickly evolving culture (1), as illustrated by the evolution of dairy-farming facilitating selection of alleles for adult lactase persistence (2).Quickly evolving organisms modify their otherwise slowly changing niches and alter selection pressures (3-5), illustrated by yeast modifying fruit environments to attract Drosophilid flies that enhance yeast propagation (6).Institutions feed back to influence individual decisions by changing cost landscapes and enhancing cultural transmission (7,8) (e.g.legislation in support of same-sex marriage that increases the willingness to voice support in the face of risk ( 9)).

To gain information about noisy, hidden variables and reduce social uncertainty, error-prone individual pigtailed macaques collectively compute a social power structure that reduces uncertainty about the cost of social interaction, making accessible new forms of conflict management (reviewed in references 10,11).Bacteria quorum sense, controlling group behavior in dynamically complex, changing environments (reviewed in reference 12).Individuals, institutions, and firms all adapt to audit targets (Goodhart's Law), creating new feedbacks as they attempt to game the system (13)(14)(15)(16).In order to undermine competitors, agents can destabilize a system like in the recent Reddit-Gamestop event in which powerful hedge funds are thought to have introduced volatility to markets by manipulating Reddit users to short squeeze yet other hedge funds (17).Motivated by these examples, we develop a synthetic framework that combines information theory, game dynamics, and scaling theory, in order to determine how adaptation scales in a range of plausible strategic settings including niche construction.

We start by reformulating adaptation as rate of discounting of the past, building a conceptual and mathematical bridge to work on memory (18)(19)(20)(21).We take into account four factors: bias as preference in the environment for a particular state, stability as the rate at which environment fluctuates (22,23), precision as the capacity agents have to resolve environmental signal, and feedback as the rate of agent modification of the environment.In Table 1, we provide examples of studies addressing the interaction of bias, stability, and precision.We also drop the separation of timescales assumption commonly made in modeling papers and explicitly consider feedback.We allow modification of the environment to be either passive or active, such that active modification can be destabilizing (increasing entropy) as well as stabilizing (reducing entropy).The Reddit-Gamestop event is one example of this "destabilizing" niche construction.Another is guerrilla warfare in which a weaker party randomly determines which battles to neglect by allocating zero resources (24).In contrast, active agents can stabilize the environment by buffering against variation (5) or slowing its rate of change to reduce uncertainty about the future (10,25).A relatively simple example is stigmergy in which trails or routes are consolidated through repeated use (26).More complicated examples include the collective computation of slowly changing power structures in macaque groups (27) and foraging subgroup size distributions by spider monkeys (28) in which social structures are computed through communication and decision networks.Finally, we take into account how the precision (29) of an agent's or organism's

### Significance Statement

All organisms must adapt to changing environments, but adaptation can modify the environment itself.We solve a version of this problem in terms of how long organisms remember.Shorter memory should be better for variable environments and longer for slow changing ones, but environmental variability depends on feedback.Surprisingly, we find the same mathematical law in both cases, revealing how much shorter memory should be relative to the environmental timescale.We consider how this depends on memory complexity and metabolic costs in populations, allowing us to predict a general set of conditions for when organism will outsource memory to the environment: when maintaining a brain is costly, the environment fluctuates quickly, and organisms inhabit a complex environment.

All authors helped develop the initial idea.E.D.L. did the analysis, modeling, and wrote the code.The authors drafted the manuscript jointly.

The authors declare no competing interests.

### I Bias-Stability II Stability-Precision

III Bias-Precision IV Integrated Taxis of larval invertebrates (30) Seed dormancy/germ banking (31) Bandit problems (32) Volatile bandits (33) Stochastic voting models (34) Particle swarms (35) Microbial chemotaxis (36) Learning changing data sources (37) Learning changing distributions (38) Cognitive aging (39) Speed-accuracy trade-offs (40-42) Consensus with link failure (43) Loss/Change aversion (44) Optimal foraging (45) Retinal sensitivity rescaling (19) Page Rank consensus ( 46 estimates of environmental state influences its ability to fit the environment at a given degree of volatility.

In "Result 1," we explore the conditions under which long memory is beneficial.In "Result 2," we derive the scaling relationship for optimal memory duration and environmental change.In "Result 3," we derive by way of a back-of-theenvelope calculation the costs of memory using the literature on metabolic scaling.In "Result 4," we introduce game dynamics introducing a complexity cost of memory to explore the evolution of active modification and outsourcing of memory to the environment.

### Model structure & assumptions

We summarize the structure of our model in Figure 1, which combines the essential components of adaptive agents.As a result, it connects passive agents that learn the statistics of a fluctuating environment with those that modify the environment itself.We summarize notation in Appendix Table S2.

The environment E at time t is described by a probability distribution pE(s, t) over configurations s, a vector of descriptive properties.The environment has a bias for preferred states that changes on a relatively slow timescale.Here, we represent the state of the environment with a single bit s ∈ {-1, 1}, analogous to the location of a resource as a choice between left and right (41,(47)(48)(49).In one configuration, the distribution of resources pE is biased to the left at a given time t, or pE(s = -1, t) > pE(s = 1, t), such that an agent with matching preference would do better on average than an agent with misaligned preference.In the mirrored configuration, the environment shows a bias of equal magnitude to the right pE(s = -1, t) < pE(s = 1, t).Such probabilistic bias can be represented as an evolving "field" hE(t), pE(s, t) = 1 2 + s 2 tanh hE(t), [1] such that reversal in bias corresponds to flip of sign hE(t) → -hE(t) that naturally embodies a symmetry between left and right.At every time point, the environment has clearly defined bias in one direction or another, determined by setting the external field to either hE(t) = -h0 or hE(t) = h0.With probability 1/τE per unit time, the bias in the environment reverses such that over time τE the environment remains correlated with its past.When τE is large, we have long correlation times and a slow environment or a "slow variable."This formulation yields a stochastic environment whose uncertainty depends on both fluctuation rate, such that low rate implies high stability, and the strength of bias for a particular state, such that a strong bias yields a clear environmental signal.Passive agents sample from the environment and choose a binary action.In principle, the precision of the choice is dependent on the number of sensory cells contributing to the estimate of environmental state, the sensitivity of those cells, and the number of samples each cell collects while the contribution of each factor to the estimate can differ.In our model, all the alternatives are captured by τc.When τc is high (either because the sensory cells sampled from the environment for a long time, many sensory cells contributed estimates, or each sensory cell is very sensitive) agents obtain exact measurements of the environment.A small τc corresponds to noisy estimates.The resulting estimate of environmental state p thus incurs an error ϵτ c , p(s, t) = pE(s, t) + ϵτ c (t).

[2]

From this noisy signal, sensory cells obtain an estimate of bias ĥ(t), which is related to environmental bias hE(t) plus measurement noise ητ c (t), ĥ(t) = hE(t) + ητ c (t). [3] In the limit of large precision τc and given that the noise in the estimated probabilities ϵτ c (t) from Eq 2 is binomial distributed, the corresponding error in field ητ c (t) converges to a Gaussian distribution (see Materials and Methods).Then, at each time step the agent's measurement of the environment includes finite-sample noise which is inversely related to precision.An aggregation algorithm determines how much to prioritize the current measurement over historical ones.This gives the duration of memory by recording the agent's estimate of the state of the environment at the current moment in time h(t) and feeding it to sensory cells at time t + 1 with some linear weighting 0 ≤ β ≤ 1 (50), h(t + 1) = (1 -β) ĥ(t + 1) + βh(t).

[4]

This estimate is stored in an "aggregator" At, and we define h(0) = 0.The weight β determines how quickly the previous state of the system is forgotten such that when β = 0 the agent is constantly learning the new input and has no memory and when β = 1 the agent ceases to learn preserving its initial

A t-1 environment sensory cells memory E 1 agent τ m τ e E 2 τ f A B τ c C E E′ A t Fig. 1. (A) Overview of framework.Environment E switches configuration on timescale τ E .The agent measures the current environment through sensory cells with precision τc, here worth 4 bits.To obtain an estimate of environment statistics at time t, the agent At combines present sensory estimates with memory of previous estimates recorded in an aggregator At-1 (Eq 4) such that memory decays over time τm (Eq 5).Coupling with the environment speeds up or slows down environmental change on timescale τ f (Eq 6).(B) Example trajectories of agents adapting to environmental state h E (t) with short, medium, and long memory.(C) Rate of environment switching per time step as a function of agent bias h relative to environmental bias h E = 0.2.For passive agents, switching rate does not depend on agent bias.For destabilizers α = 0.95, for stabilizers α = -0.95.For both, v = 0.1 from Eq 6 and environmental timescale τ E = 5.

state.In between, agent memory decays exponentially with lifetime τm ≡ -1/ log β. [5] We think of the weight β that the aggregation algorithm places on the current estimate relative to the stored value as the timescale of adaptation τm, or agent memory duration.The output of this computation is the agent's behavior, p(s, t).We measure the effectiveness of adaptation, or fit to the environment, with the divergence between a probability vector describing an agent and that of the environment.Measures of divergence, like Kullback-Leibler (KL) divergence, and, more generally, mutual information, have been shown to be natural measures of goodness of fit in evolutionary and learning dynamics from reinforcement learning through to Bayesian inference (51,52).

Here we extend the model to include feedback by allowing agents to alter environmental stability, which is operationalized as the probability of switching.We add to the switching rate 1/τE, the active construction rate, [6] such that the probability q that the environment changes at the next point in time is q[hE(t + 1) ̸ = hE(t)] = 1/τE + α/τ f (t).[7] Eq 6 is written so that it remains normalized for arbitrary v and that the rate gets smaller as the squared distance between agent bias and environmental bias [h(t) -hE(t)] 2 goes to zero.The probability q of the environment switching to the opposite configuration includes weight α ∈ (0, 1] to tune the strength of destabilizers, or α ∈ [-1, 0) for stabilizers.This means that for positive α, the rate of switching increases as the agent matches the environment more closely and the opposite for negative α, whereas the parameter v controls how closely the agent must match the environment to have an effect (i.e. the width of the peak as plotted in Figure 1C).The two types of active agents capture two ways adaptive behavior can feedforward to influence the timescale environmental change.* We note that when 1/τ f = 0, we obtain passive agents that do not modify their environment, thus connecting passive and active agents to one another along a continuum scale.Putting these elements of adaptation together, as shown in Figure 1A, we obtain a toy learning agent that infers the statistics of a time-varying and stochastic environment.

1 τ f (t) ≡ v 2 /τE [h(t) -hE(t)] 2 + v 2 ,

### Result 1: Long memory and adaptation favored when sensory cells are imprecise & environments are slow

The timescale of adaptation represents a balance between the trade-offs of preserving an internal state for too long or losing it too fast.We explore this trade-off by calculating an agent's fit to a changing environment.The fit can be quantified with the KL divergence between environment pE(s, t) with bias hE(t) and agent p(s, t), D KL [pE||p](t) = s∈{-1,1} pE(s, t) log 2 pE(s, t) p(s, t) .[8] When the KL divergence is D KL = 0, the agents use optimal bet-hedging, known as "proportional betting," which is important for population growth dynamics (53,54).Eq 8 is also minimized for Bayesian learners under optimal encoding (55).Assuming agents are playing a set of games in which they must guess the state of the environment at each time step, Eq 8 is the information penalty paid by imperfect compared to perfect agents.After averaging over many environmental bias switches, we obtain the agent's typical divergence,

D ≡ lim T →∞ 1 T T -1 t=0 D KL [pE||p](t), [9]

The bar notation signals an average over time.Thus, fit improves as D decreases.

10 1 10 1 10 3 agent memory m 10 6 10foot_3 10 2 divergence D A P 10 1 10 1 10 3 agent memory m 10 6 10 4 10 2 divergence D B env. timescale E = 1 E = 7 E = 46 E = 316 E = 2154 E = 14678 E = 100000 S' S 10 0 10 2 10 4 env.timescale E 10 1 10 0 10 1 memory * m 10 0 10 2 10 4 env.timescale E 10 5 10 4 divergence D * passive (P) destabilizer (S') stabilizer (S) * m 1/2 E D * 1/2 E C D In Figures 2A and B, we show divergence D(τm, τE) as a function of the agent's memory τm given environmental timescale τE.In the limiting cases in which an agent has either no memory and is constantly adapting or has infinite memory and adaptation is absent, the timescale on which environmental bias changes ultimately has no effect-we observe convergence across all degrees of bias and stability.When an agent has no memory, or τm = 0, an agent's ability to match the environment is solely determined by its sensory cells.Low precision τc leads to large errors on measured environmental bias hE(t) and large divergence D(τm = 0).On the other hand, high precision τc increases performance and depresses the intercept (Eq 23).At the right hand side of Figure 2A, for large τm ≫ 1, behavior does not budge from its initial state.Assuming that we start with an unbiased agent such that the transition probability is centered as q(h) = δ(h), the Dirac delta function, the agent's field is forever fixed at h = 0.Then, divergence D(τm = ∞) reduces to a fixed value that only depends on environmental bias (Eq 24).In between the two limits of zero and infinite agent memory, the model produces a minimum divergence D(τm = τ * m ).This indicates the optimal duration of memory τ * m for a given degree of environmental bias and stability.

The benefits of memory are more substantial for agents with imprecise sensory cells.This benefit is the difference D(τm = 0) -D(τm = τ * m ) as shown in Figure 3A.As one might expect, integrating over longer periods of time provides more of a benefit when the present estimate p is noisy, τc -1 is large, and sensory cells are not particularly precise, a deficiency in precision that memory counters by allowing organisms to accumulate information over time.This intuition, however, only applies in the limit of large environmental bias h0 where the contours of optimal memory flatten and become orthogonal to precision τc -1 .When the bias in the environment is weak, the curved contours show that the benefits of memory come to depend strongly on nontrivial interaction of precision and environmental bias.The complementary plot is the benefit from forgetting, D(τm = ∞) -D(τm = τ * m ) in Figure 3 B, which is largely determined by bias h0.When bias is strong, the costs of estimating the environment inaccurately are large, and it becomes important to forget if sensory cells are imprecise.Thus, our model encapsulates the trade-off between remembering and forgetting both in terms of their absolute benefits as well as the emergence of simple dependence of the respective benefits in the limits of high environmental bias and high sensory precision.An agent has optimally tuned its timescale of adaptation τm = τ * m when it has balanced the implicit costs of tuning to fluctuations against the benefits of fitting bias correctly.

### Result 2: Adaptation and environmental change scale sublinearly

For sufficiently slow environments, or sufficiently large τE, we find that optimal memory duration τ * m scales with the environmental timescale τE sublinearly as in Figure 2C.To derive the scaling between optimal memory and environmental timescale, we consider the limit when agent memory persistence is small relative to the environmental persistence τm ≪ τE.Under this condition, optimal memory represents a trade-off between a poor fit lasting time τm and a good fit for time τE -τm.During the poor fit, the agent pays a typical cost at every single time step such that the cost grows linearly with its duration, Cτm, for constant C. When the environment is stable, agent precision is enhanced by a factor of τm because it effectively averages over many random samples, or a gain of G log τm for constant G.When we weight each term by the fraction of time spent in either transient or stable phases, τm/τE and (τE -τm)/τE respectively, we obtain the trade-off

C τ 2 m τE -G τE -τm τE log τm. [10]

At optimal memory τ * m , Eq 10 will have zero derivative.Keeping only the dominant terms and balancing the resulting equa- tion, we find

τ * m ∼ τ 1/2 E .

[11]

This scaling argument aligns with numerical calculation as shown in Figure 2C.Similarly, we calculate how optimal divergence D * scales with environmental timescale.Assuming that the agent has a good estimate of the environment such that the error in average configuration ϵτ c (t) is small, agent behavior is pE(s, t)+ ϵτ c (t) and ϵτ c (t) is normally distributed.Then, we expand the divergence about pE(s, t) in Taylor series of error ϵτ c (t) (Materials & Methods).Over a timescale of τ * m , the precision of this estimate is further narrowed by a factor of τ * m such that

D * ∼ 1/τ * m ∼ τ -1/2 E . [12]

Although we do not account for the transient phase, we expect the relation in Eq 12 to dominate in the limit of large τE, and our numerical calculations indeed approach the predicted scaling in Figure 2C.In contrast, when environment does not fluctuate, or bias h0 = 0, agents pay no cost for failing to adapt to new environments and infinite memory is optimal.Overall, the sublinear scaling between memory duration and rate of environmental change indicates an economy of scale.Agents require proportionally less expenditure on adaptation in slow environments than would be true under a linear relationship.Hence a slow environment is in this sense highly favorable to an adaptive agent when considering the costs of poor adaptation.

### Result 3: Metabolic cost of memory can become prohibitive in slow environments

Here we ask how memory might become limited by the metabolic costs of neural tissue.

We start with the well-documented observation that physical constraints on circulatory networks responsible for energy distribution influence organismal traits including lifespan and size across the animal kingdom from microorganisms to blue whales (56,57).Metabolic costs matter for brain mass M br , which scales with body mass M bo sublinearly, M br = AM a bo , where a = 3/4 across taxa (within individual taxa it spans the range 0.24 to 0.81 (58)).To account for memory cost, we make the simple assumption that the quantity of brain mass required for memory is proportional to the number and duration of environmental states (the "environmental burden") the organism encounters, M br ∝ N τE.[13] After all, we say, "an elephant never forgets" and not the same of a mouse.Now, we use predictions of allometric scaling theory to relate metabolic rate B to mass, B ∝ M 1/4 (59), and lifespan to body mass, T ∝ M b bo for metabolic exponent b = 1/3 (60).From Eq 13, we obtain a relationship between metabolic rate and memory burden, B ∝ N ϕ τ ϕ E , where ϕ ≡ a/4b.† Note that this scaling is sublinear for biological organisms, ϕ < 1.Although the adaptive cost decays with τE in Figure 4A, metabolism grows as τ ϕ E as shown in Figure 4B.The competing scalings suggest that for small organisms the cost of adaptation will make a disproportionate contribution to the lifetime energy budget of an organism.This is consistent with observations on developmental neural growth in butterflies (61).‡ † When we use a = 3/4, we obtain the range ϕ = [5/8, 15/16], the endpoints depending on whether b = 0.3 or b = 0.2, respectively, while accounting for taxa-specific variation in a leads to much wider range of ϕ ∈ [0.2, 1.01].Thus, we hypothesize that longer environmental timescales lead to increased brain mass and metabolic expenditure with sublinear scaling.‡ As noted in the cited study and its citations, experience leads to larger brain size, indicating that learning from such experience is sufficiently valuable to warrant concomitant constitutive and induced costs.

10 3 10 1 stab.weight 10 3 10 2 10 1 10 0 complexity weight 0.02 0.00 0.02 stab.advantage To generalize the previous argument, we assume larger organisms experience longer environmental timescales.Then, τE ∝ T y , where y ∈ [0, 1] to ensure that τE and N increase together since τ 1/y-1 E ∝ N .We now find the relationship between metabolic rate and environmental timescale

B ∝ τ ϕ/y E ∝ N ϕ/(1-y) , [14]

which reduces to the previous case when y = 1 (and N is a constant).Such dependence implies that the metabolic cost of memory will explode with environmental timescale (and organism lifetime) as y approaches zero and grow slowly and sublinearly when y = 1.Both possibilities are shown in Figure 4B.More generally, lifespan is expected to influence the relative contributions of adaptive versus metabolic costs (62,63).

### Result 4: Niche construction, memory complexity, & the outsourcing principle

In Result 3, we explored the metabolic cost of memory versus adaptation, emphasizing the metabolic constraints on long memories.In this section we focus on the information costs of adaptation when allowing for active modification of the environment.We explore how outsourcing memory to the environment by slowing it down is beneficial when costs of poor adaptation are dominant (10).

A slow environmental timescale increases the advantages of persistent memory, but it also reduces the amount of new information an organism requires by reducing uncertainty about the state of the environment.In this sense, slow environmental variables reflect a form of niche construction.Whether ant pheromone trails, food caching, collectively computing power structures, writing, or map-making, niche construction that promotes the stability or predictability of the local environment (5, 64) reduces the number of environmental configurations that an organism needs to encode.Stabilizing niche construction, however, also creates a public good that by reducing environmental uncertainty, provides a benefit to all agents, and can be exploited by free riders.This can lead to a tragedy of the commons (65).

We explore the conditions under which active modification of the environment can evolve given the free-rider problem, and how this overcomes the costs of adaptation.We introduce stabilizing mutants into a population of passive agents.Assuming other organisms are poorly adapted to regularities in the environment, we expect stabilizing mutants to gain a competitive advantage but only over the short term.In the longer term, an established stabilizer population is susceptible to invasion by free-riders exploiting outsourced memory; said another way, stabilizers slow environmental timescales and reduce divergence for all individuals sharing the environment, but they uniquely pay for stabilization.Thus, as in the classical example of niche construction, the usual "tragedy of the commons" argument makes it an evolutionary dead end (65).

It follows that stabilization is only a competitive strategy if individuals can monopolize extraction of resources from the stabilized environment.In the natural world, this could occur through physical encryption (e.g.undetectable pheromones (66)), the erasure of signal (e.g.food caching (67)), or the restriction of social information (e.g.concealment ( 68)).To model competition between monopolistic stabilizers and other strategies, we account for the costs of memory, stabilization, and precision.We introduce a new memory cost of encoding complex environments as H(τm) = log 2 (1 + 1/τm).

[15]

Eq 15 can be thought of as a cost of exploring more configurations over a short period time versus agents that are temporally confined.This is different from costs associated with the environmental burden in Result 3, which emphasizes the costs of persistence, not variability.We define the cost stabilizers pay for niche construction as the extent of change to the environmental switching rate, or the KL divergence between the natural environmental rate 1/τE and the time-averaged, modified rate ⟨1/τE⟩,

G(1/τE, ⟨1/τE⟩) = 1 τE log 2 1/τE ⟨1/τE⟩ + 1 - 1 τE log 2 1 -1/τE 1 -⟨1/τE⟩ .

[16]

The quantity G depends implicitly on stabilization strength α because smaller α slows the environment further.For passive agents and destabilizers, G = 0 by definition because nonstabilizers fit to τE and only stabilizers benefit from the slower timescale with monopolization.We finally consider the cost of precision, which we assume to be given by the information obtained by the agent from sampling the environment, C(τc) = log 2 τc.

[17]

Sensory complexity means that higher precision implies higher expenditure to obtain such precision, given by the KL divergence between environment configuration and agent behavior, C ∼ -log 2 (σ 2 ) leaving out constants.This depends on the variance of agent measurement noise σ 2 = pE(s, t)[1 -pE(s, t)]/τc.Infinitely precise sensory cells lead to diverging cost, whereas imprecise cells are cheap.Putting these costs together with divergence D, we obtain the total divergence D = D + µH + χG + βC.

[18]

Weights µ ≥ 0, χ ≥ 0, β ≥ 0 represent the relative contribution of these costs.As a result, we can distinguish dominant strategies by comparing total divergence such as between the pair of destabilizer and stabilizer strategies shown in Figure 5. Large µ, or high complexity cost, means that a pure population of stabilizers would be stable to invasion from destabilizers.Whereas for large χ, or heavy stabilization cost, the opposite is true.The generalized measure of adaptive cost in Eq 18, given the weights, carves out regions of agent morphospace along axes of computational cost.This is a morphospace that captures the relative advantage of internal versus external memory that can be thought of as a space of evolutionary outsourcing.

As has often been remarked in relation to evolution, survival is not the same as arrival.We now determine when stabilizer strategies can emerge in this landscape.We start with a pure population of passive agents with stabilization strength α = 0 and poised about optimal memory duration τm = τ * m determined by minimizing both divergence D and complexity µH.Whether or not stabilizers emerge under mutation and selection can be determined through adaptive dynamics (69)(70)(71), that is by inspecting the gradient of the total divergence along the parameters (∂τ m D, ∂αD, ∂τ c D), or memory complexity, stabilizer strength, and precision.As we show in SI Appendix C and Eq S16, the gradient terms can be calculated under a set of perturbative approximations.Using local convexity about optimal memory τ * m , we show that the term ∂αD drives passive agents to smaller α and slower timescales; it originates from combining the scaling law from Eq 12 and complexity of memory.The term ∂τ c D shows that precision tends to decrease when the cost gradient ∂τ c (βC) dominates over ∂τ c D. In this case, the general conditions ∂αD < 0 and ∂τ c D < 0 funnel a passive population towards stabilization and reduced precision.

### Discussion

Life is adaptive, but optimal adaptation would seem to depend on a multitude of properties of both organism and environment, which have been studied in a wide literature (Table 1).To the contrary, we predict that it does not.This becomes clear once we organize crucial aspects of adaptation into a unified framework in terms of timescales including niche construction that speeds up or slows down the environment (Figure 1).We find that memory duration, under a wide range of assumptions and conditions, scales sublinearly with environmental rates of change (Figure 2).This essentially derives from the competition between using current but noisy information and the reliance on outdated but precise information, leading to a universal, optimal timescale for adaptation.Importantly, sublinear scaling implies that persistent features of the environment can be more efficiently encoded the longer-lasting they become; there is an economy of scale.

Yet, memory remains costly as it requires investing in neural tissue.To estimate this cost and how it might affect adaptation, we use metabolic scaling theory to estimate how much neural tissue an organism must allocate to memory for a given rate of environmental change.We find that the metabolic costs of memory can increase super-linearly with the persistence time of environmental statistics.Thus, while memory need not grow in proportion to environmental stability, costs of memory could increase disproportionately (Figure 4).Because adaptive costs peak at short timescales, this suggests that adaptive costs are most important for organisms with short lifespans such as insects.

When the costs of adaptation are greater than the metabolic costs of memory, active modification of the environment such as stabilizing niche construction can be favored.In this case the organism intervenes on the environmental timescale to decrease volatility.Although outsourcing of memory to the environment reduces the organism's need to adapt, it introduces two new problems.First, active modification is itself not free.Second, slow environmental variables created by active modification are public goods that can be exploited by free riders.

To address the costs of active modification and free riding, we introduce game dynamics considering the information costs of adaptation including the complexity of memory.Unlike memory duration, memory complexity quantifies the effective number of states that agents occupy.Starting with passive agents, we find that the spontaneous emergence of adaptive dynamics stabilizes the environment, lengthening the optimal memory duration τ * m and thereby making weak stabilizers less competitive.This moves a population as a whole towards slower timescales.In other words, stabilizing niche construction, because of the economy of scale with respect to memory, requires proportionally less neural tissue for memory relative to the size of the whole brain as given by metabolic scaling theory.This is effectively outsourcing memory from neural tissue to the environment.As a possible consequence, organisms could reduce absolute brain size or invest in a larger behavioral repertoire, increasing competitiveness by monopolizing a larger number of environmental states.Do learning agents in volatile environments "given a choice" to invest in additional memory or to directly change the environment favor the latter?

This hypothesis is consistent with related work on institutions and social structure as a form of collectively encoded memory (72)(73)(74)(75) or as devised constraints (e.g.reference 76) that slow down the need to acquire functional information.In pigtailed macaque society (reviewed in reference 10), individuals collectively compute a social-power distribution from status signaling interactions.The distribution of power as a coarsegrained representation of underlying fight dynamics changes relatively slowly and consequently provides a predictable social background against which individuals can adapt.By reducing uncertainty and costs, the power distribution facilitates the emergence of novel forms of impartial conflict management.Conflict management, in turn, further reduces volatility, allowing individuals to build more diverse and cohesive local social niches and engage in a greater variety of socially positive interactions (77).In other words, outsourcing memory, in this case, of fight outcomes, to a stable social structure in the power distribution allows for a significant increase in social complexity.More generally, we anticipate that one of the features of slowing environmental timescales, including social environments fostered by institutions, might the emergence of new functions (78).

Without feedforward and feedback loops between environment and agent such as in the case of the passive agent, our framework is akin to the classical problem of learning.This has been a major problem of interest in foraging (79), neural circuits that adapt to changing input distributions (19,80,81) and modes of prediction in order to best adapt to multiple clustered sets of statistics (20,80).We introduce here a min-imal modeling framework for connecting learners to active agents that modify the environment through the act of adaptation.Our framework provides a first-order approximation to this extended space, which could itself be extended in several directions to include how agents physically modify their environments, connecting to the physics of behavior with the physics of information (82).

### Materials and Methods

The code used to generate these results will be made available on GitHub at https://github.com/eltrompetero/adaptation.

### Numerical solution to model.

Given Eqs 1-4 defining the binary agent, we calculate agent behavior in two ways.The first method is with agent-based simulation (ABS).We generate a long time series either letting the environment fluctuate independently and training the agent at each moment in time or coupling environmental fluctuations at each time step with the state of the agent.By sampling over many such iterations, we compute the distribution over agent bias given environmental bias, q(h|h E ), which converges to a stationary form.

This principle of stationarity motivates our second solution of the model using an eigenfunction method.If the distribution is stationary, then we expect that under time evolution that the conditional agent distribution map onto itself

q(h|h E ) = T [q(h|h E )].

[19]

If the time-evolution operator T evolves the distribution over a single time step, the external field can either stay the same with probability 1 -1/τ E or reverse with probability 1/τ E .For either for these two possible alternatives over a single time step, we must convolve the distribution with the distribution of noise for the field ητ c .The distribution of noise derives from agent perceptual errors ϵτ c on the estimated probabilistic bias of the environment (Eq 2).Hence, the corresponding error distribution for the bias ητ c originates from the binomial distribution through a transformation of variables.We can simplify this because in the limit of large sensory cell sample size τc the binomial distribution converges to a Gaussian and a concise representation of the distribution of ητ c becomes accurate.Using Eq 1, we find that the distribution of perceptual errors in the bias yields [20] Here, the agent's perceptual estimate of the environment includes finite-sample noise determined by the sensory cell precision 1/τc.At finite τc, there is the possibility that the agent measure a sample from the environment of all identical states.In our formulation, the fields then diverge as do the fields averaged over many separate measurements.We do not permit such a "zero-temperature" agent that freezes in a single configuration in our simulation just as thermodynamic noise imposes a fundamental limit on invariability in nature.Our agents inhabit an in silico world, where the corresponding limit is fixed by the numerical precision of the computer substrate, so we limit the average of the bits sampled from the environment to be within the interval [-1 + 10 -15 , 1 -10 -15 ].This is one amongst variations of this idea that inference is constrained by regularization, Bayesian priors, Laplace counting (in the frequentist setting), etc. Regardless of the particular approach with which finite bounds might be established, they are only important in the small τc limit.See SI Appendix A.

ρ(ητ c , t) = (8πσ 2 ) -1/2 exp -[tanh h E (t)- tanh(h E (t) + ητ c )] 2 /8σ 2 sech 2 (h E (t) + ητ c ) .

Given the Gaussian approximation to precision error, we propagate the conditional distribution over a single time step, defining a self-consistent equation that can be solved by iterated application.To make this calculation more efficient, we only solve for abscissa of the Chebyshev basis in the domain β ∈ [0, 1], fixing both the endpoints of the interval including the exact value for β = 1 from Eq 24 ( 83) (more details in SI Appendices A and B).In Figure S7, we show that our two methods align for a wide range of agent memory τm.Importantly, the eigenfunction approach is much faster than ABS for large τc because the latter can require a large number of time steps to converge.On the other hand, ABS is relatively fast for small τc.Thus, these two approaches present complementary methods for checking our calculation of agent adaptation.

### Divergence curves.

To measure how well agent behavior is aligned with the environment, we compare environment p E (s, t) and agent p(s, t) with the KL divergence at each time step to obtain the agent's typical loss in Eq 9. Equivalently, we can average over the stationary distribution of fields conditional on environment

D = 1 N E E ∞ -∞ dh q(h|h E )D KL [p E (h E )||p(h)],[21]

where we sum over all possible environments E and weight them inversely with the number of total environments N E .For the binary case, N E = 2.We furthermore simplify this for the binary case as

D = ∞ -∞ dh q(h|h E = h 0 )D KL [p E (h E = h 0 )||p(h)]

. [22] In Eq 22, we have combined the two equal terms that arise from both positive h E = h 0 and negative h E = -h 0 biases of the environment.

In Figure 2A and B, we show divergence as a function of agent memory over a variety of environments of varying correlation time D(τm, τ E ).When the agent has no memory, its behavior is given solely by the properties of the sensory cells as is determined by the integration time τc.Then, we only need account for the probability that the environment is in either of the two symmetric configurations and how well the memoryless agent does in both situations.Since the configurations are symmetric, the divergence at zero memory is

D(τm = 0) = ∞ -∞ dητ c ρ(ητ c |h E = h 0 )× s∈{-1,1} p E (s|h E = h 0 ) log 2 p E (s|h E = h 0 ) p(s) , [23

]

where the biased distribution of environmental state p E and the error distribution ρ from Eq 20 are calculated with environmental bias set to h E = h 0 .Note that this is simply Eq 22 explicitly written out for this case.At the limit of infinite agent memory, as in the right hand side of Figure 2A, passive agents have perfect memory and behavior does not budge from its initial state.Assuming that we start with an unbiased agent such that q(h) = δ(h), the Dirac delta function, the agent's field is forever fixed at h = 0.Then, divergence reduces to D(τm = ∞) = 1 -S[p E ], [24] where the conditional entropy

S[p E ] = -p E (s|h = h 0 ) log 2 p E (s|h = h 0 ) -[1 -p E (s|h = h 0 )] log 2 [1 -p E (s|h = h 0 )].

Scaling argument for optimal memory.As is summarized by Eq 10, the value of optimal memory can be thought of as a trade-off between the costs of mismatch with environment during the transient adaptation phase and gain from remembering the past during stable episodes.In order to apply this argument to the scaling of divergence, we consider the limit where the environment decay time τ E is very long and agent memory τm is long though not as long as the environment's.In other words, we are interested in the double limit τm → ∞ and τm/τ E → 0.Then, it is appropriate to expand divergence in terms of the error in estimating the bias

D = s∈{-1,1} p E (s, t) log p E (s, t)p E (s, t) log[p E (s, t) + ϵτ c (t)] , [25] where the average is taken over time.Considering only the second term and simplifying notation by replacing ϵτ c (t) with ϵ, ⟨p E (s, t) log p E (s, t) + log[1 + ϵ/p E (s, t)]⟩ ≈ p E (s, t) log p E (s, t) + ϵ p E (s, t) -1 2 ϵ 2 p E (s, t) 2 [26] where the average error ⟨ϵ⟩ = 0 and assuming that the next nontrivial correlation of fourth order O ϵ 4 is negligible.Plugging this back into Eq 25,

D ≈ s∈{-1,1} τ E -τm τ E ϵ 2 p E (s) 2 + τm τ E ϵ 2 p E (s, t) 2 .

[27]

The first term in Eq 27 relies on the fact that when environmental timescales are much longer than agent memory, the errors become independent of the state of the environment.Thus, we can average over the errors separately, and the environment configuration average can be treated independently of time p E (s, t) → p E (s).The second term, however, encases the transient dynamics that follow immediately after a switch in environmental bias while the agent remembers the previous bias.It is in the limit τm/τ E → 0 that we can completely ignore this term and the scaling for optimal memory τ * m ∼ τ

1/2 E

from Eq 11 is the relevant limit that we consider here.Since the errors with which the agent's matching of environmental bias is given by a Gaussian distribution of errors, the precision increases with the number of samples taken of the environment: it should increase with both sensory cell measurement time τc as well as the typical number of time steps in the past considered, τm = -1/ log β.Thus, we expect the scaling of divergence at optimal memory to be D * ∼ 1 τ * m τc , [28] which with Eq 11 leads to the scaling of optimal memory with environment decay time Eq 12. Though the scaling with precision timescale τc in Eq 28 is at τm = τ * m , it is clear that a similar scaling with τc holds at τm = 0, where only precision determines divergence.However, such a scaling does not generally hold for any fixed τm, the trivial case being at τm = ∞, where divergence must go to a constant determined by environmental bias.

### A. Agent-based simulation

To complement the eigenfunction solution described in Appendix B, we present the agent-based simulation.

After having specified the environmental bias h E (t), we generate a sample of τc binary digits from the distribution p E (s, t).From this sample, we calculate the mean of the environment ⟨s⟩ which is bounded in the interval [-1 + 10 -15 , 1 -10 -15 ].These bounds are necessary to prevent the measured field ĥ(t) from diverging and reflects the fact that in silico agents have a finite bound in the values they can represent, mirroring finite cognitive resources for biological or social agents as discussed in Materials and Methods.We combine this estimated field ĥ(t) with the one from the aggregator having set the initial value condition H(0) = 0. Given the estimate of the field h(t), we compute the Kullback-Leibler (KL) divergence between the agent distribution p(s) and the environment p E (s).

When we calculate the divergence landscape across a range of different agent memories, we randomly generate the environment using the same seed for the random number generator.Though this introduces bias in the pseudorandom variation between divergence for agents of different types, it makes clearer the form of the divergence landscape by eliminating different offsets between the points.Our comparison of this approach with the eigenfunction solution in Appendix B provides evidence that such bias is small with sufficiently long simulations.For the examples shown in the main text, we find that total time T = 10 7 or T = 10 8 are sufficient for convergence to the stationary distribution after ignoring the first t = 10 4 time steps.

### B. Eigenfunction solution

We present more details on top of those in Materials and Methods on the iterative, eigenfunction solution to the divergence of an agent relying on the fact that the distribution of agent bias q(h) becomes stationary at long times.

Let us first consider the case of the passive agent.After sufficiently long time, the distribution of agent behavior q(h) and the distribution conditioned on the two states of the environment q(h|h E = h 0 ) and q(h|h E = -h 0 ) converge to stationary forms.Assuming that the distributions have converged, we evolve the distribution a single time step.If the external field h E (t) = h 0 , then it either stays fixed with probability 1 -1/τ E or it switches to the mirrored configuration with probability 1/τ E .

Considering now the evolution of the conditional probability q(h|h E = h 0 ), we note that the state of the agent will be either be convolved by the distribution of sampling error at the next time step or lose probability density from a switching field.Since we are considering a symmetric configuration, however, the mirrored conditional density will reflect the same probability density back such as in Eq S1.Thus, Eq S1 is satisfied by the conditional density of agent bias that is solved by the eigenfunction for q(h|h E ) with eigenvalue 1.By the Perron-Frobenius theorem when considering normalized eigenvectors, this is the unique and largest eigenvalue that returns the stationary solution.

To extend this formulation to active agents, we must also account for the dependence of the rate of switching on the distance between agent and environmental bias.This additional complication only requires a modification of Eq S1 to include such dependence in the rate coefficients.Thus, all types of agents can be captured by this eigenfunction solution and solved by iteration til convergence.

Eq S1 is only independent of time when agent memory τm = 0.When there is finite memory, or β > 0, the distribution q(h, t) "remembers" the previous state of the environment such that we must iterate Eq S1 again.Over many iterations, we will converge to the solution, but the convergence slows with agent memory which introduces ever slower decaying eigenfunctions.An additional difficult arises because the narrowing in the peak of the agent's estimate of the environment, like the peaks shown in Figure S7, require increased numerical precision.As a result, increasing memory and computational costs make it infeasible to calculate the eigenfunction with high precision for β close to 1.

Instead of calculating the full functional form directly below but not at the limit β → 1, we use the output of the iterative eigenfunction procedure as input for an interpolation procedure using Chebyshev polynomials.We iterate Eq S1 for β equal to

10 4 10 3 10 2 10 1 sensory cell precision 1/ c A 10 1 10 1 10 3 agent memory m 10 4 10 3 10 2 10 1 sensory cell precision 1/ c B 0.0 1.2 2.4 3.6 4.8 6.0 7.2 8.4 9.6 complexity cost H + C 2.7 2.4 2.1 1.8 1.5 1.2 0.9 0.6 arises from numerical precision errors where we matched up ABS and eigenfunction methods.

the Gauss-Lobatto abscissa of the Chebyshev polynomial of degree d, mapping the interval β ∈ [0, 1] to the domain x ∈ [-1, 1] for the set of Chebyshev polynomials (83).The Gauss-Lobatto points include the endpoints β = 0 and β = 1, the first of which is trivial numerically and the latter for which we have an exact solution given in Eq 24.Then, we exclude calculated values for large β that show large iteration error ϵ > 10 -4 .This threshold, however, leaves the coefficients of the Chebyshev polynomial undetermined.We instead interpolate these remaining N -k points by by fitting a Chebyshev polynomial of degree N -k -1 with least-squares on the logarithm of the divergence.A similar procedure can be run for the stabilization cost from Eq 16 to obtain Figure S6B.We find that typically N = 30 or N = 40 starting abscissa with a maximum of 10 3 iterations are sufficient to obtain close agreement with the agent-based simulation (ABS) from Appendix A (Figure S8).This interpolation procedure does not work well with ABS because small stochastic errors can lead to high-frequency modes in interpolation (and thus large oscillations), errors that can be essentially driven to zero exponentially fast for the eigenfunction method.

### C. Evolution of reduced complexity

We consider a population of passive agents, or an agent with stabilization parameter α = 0, precision timescale τc, and optimal memory τ * m , the variables that determine agent fitness.Assuming that the canonical equation for evolution applies (i.e.mutations only change phenotype and fitness slightly, the population dynamics move much faster than the evolutionary landscape such that we can assume a single phenotype dominates), the rate at which the population evolves across the phenotypic landscape is proportional to the fitness gradient.In addition to this assumption, we will assume that the population is always poised at optimal memory, an assumption that will be made clear below.

We recall that the total divergence consists of the time-averaged divergence D, statistical complexity cost H, stabilization cost G, and precision cost C

D = D + µH(τm) + χG(τ E , τE ) + βC(τc) [S2] q(h, t|hE = h0) = 1 - 1 τE ∞ -∞ ∞ -∞ ρ(ητ c |hE = h0)q(h, t -1|hE = h0)δ(h -h0 -ητ c ) dητ c dh+ 1 τE ∞ -∞ ∞ -∞ ρ(ητ c |hE = -h0)q(h, t -1|hE = -h0)δ(h + h0 -ητ c ) dητ c dh.

[S1] with semi-positive weights µ, χ, and β.In Figure S9, we show each the divergence of a stabilizer without such costs in blue, each of these costs separately in black, and their sum in orange to generate the total divergence in Eq 18.For the evolutionary dynamics, we must calculate the gradient (∂τ m D, ∂αD, ∂τ c D) determining the evolution in the properties of the agent.We calculate these term by term and then put them together at the end.

We assume that agent memory τm is at the minimum of the combination of time-averaged divergence D and statistical complexity cost µH (stabilization is zero for passive agents).Since divergence has a unique minimum and complexity monotonically approaches H(τm = ∞) = 0, the addition of complexity only shifts optimal memory to a larger value.Without the complexity cost, we have that small deviations about optimal memory can be represented by a quadratic function for some positive constant a,

D = D * + a(τm -τ * m ) 2 , [S3]

where we write

D * = D 0 (τ * m ) 1/2 [S4]

for some positive constant D 0 .Once we have accounted for a perturbative addition from memory complexity, however, we have a shifted optimal memory

τ * * m = τ * m + µ 2(log 2)aτ * m (τ * m + 1) + O(µ 2 ) [S5]

obtained from ∂τ m [ D + µH] = 0 and using the approximation that µ is small.Eq S18 shows us that memory complexity, the term proportional to µ, drives optimal memory τ * * m up.

Taking the approximation in Eq S18 the shifted optimal divergence, denoted by an apostrophe, becomes D′ (τ * * m ) = D * + a µ 2 4(log 2) 2 (τ * m ) 2 (τ * m + 1) 2 + O(µ 3 ).

[S6]

Again, perturbations about the local optimum lead to

D′ (τm) ≈ D * + a µ 2 4(log 2) 2 (τ * m ) 2 (τ * m + 1) 2 + b(τm -τ * * m ) 2 [S7]

for some positive constant b, which implicitly depends on the complexity cost.Eq S20 expresses local convexity about shifted optimal memory τ * * m according to the corresponding shifted divergence D′ .This indicates how the population is poised along the ridge of optimal memory given a perturbative cost of memory complexity.

Then, time-averaged divergence will grow because optimal memory changes.Assuming that the population is at optimal memory, we obtain for the partial derivative with respect to α

∂α D′ = D 0 2 (τ * m ) -3 2 + a µ 2 (2τ * m + 1) 2(log 2)(τ * m ) 3 (τ * m + 1) 3 ∂τ * m ∂α , [S8]

where we have used the fact that optimal memory must increase with stronger stabilizer, or that ∂ατ * m < 0, to explicitly pull out a negative sign.Given that we are in the scalin regime, this confirms that in Eq S8 divergence at optimal memory decreases as α approaches -1 from above as expected.

Niche-constructing stabilization changes the environmental timescale through feedback.We start by considering over a long (bottom) Stabilization cost is similarly interpolated, but it is slower to converge with visible oscillations disappearing by N = 30.For N = 20 and N = 30, not all the points fell within the convergence criterion and only 19 and 28 points were fit, respectively.For both plots, the Chebyshev polynomial approximation is slowest to converge near the sharp bends at large τm.ABS is run for 10 7 time steps.

### period of time the average over many environmental switches

⟨1/τ E ⟩ = 1/τ E + α v 2 v 2 + (h -h E ) 2 , = 1/τ E + αf (τm).

[S9] Since we do not know the exact form of the second term on the right hand side, we represent it as some function f that represents an average over time.For notational simplicity, we only make explicit f 's dependence on τm, but it depends on agent properties and environmental timescale.Now, a change in α also indirectly affects τ * m because the environmental timescale will change, reducing or increasing the agents ability to track the new environment.For example, with the passive agent, an increase in α introduces environmental stabilization, driving the effective environmental timescale slower and moving the optimal memory timescale up.Accounting for these derivatives means that

dα ⟨1/τ E ⟩ = f (τm) + α∂τ m f (τm)∂ατm.

[S10]

Now, we will again make use of the assumption that τm is close τ * m such that we can make the linear approximation f (τm

) ≈ f (τ * m ) + (τm -τ * m )f ′ (τ * m ). Putting this in, we find dα ⟨1/τ E ⟩ (τm) = f (τ * m ) + (τm -τ * m )f ′ (τ * m )+ α∂τ m [f (τ * m ) + (τm -τ * m )f ′ (τ * m )]∂ατ * m [S11]

For a passive agent, this simplifies because α = 0. Furthermore, we know that f ′ (τ * m ) = 0 because we have assumed that the agent is at optimal memory so any deviation from optimal memory must generally increase the typical distance between environmental and agent bias (h -h E ) 2 .Then, not situated exactly at optimal memory and when α ̸ = 0 are more complicated).In other words, decreasing α for the weak stabilizer will reduce the probability that the environment switches by the term in Eq S12 because f > 0 and f ′ -the change in probability is not just dependent on the rate effect f but also its derivative.Under such a change, the new environmental timescale will deviate from τ E and so the stabilization cost can be expanded as

dα ⟨1/τ E ⟩ (τm) = f (τ * m ). [S12]

G(τ E , τE ) = 1 τ E log 1/τ E ⟨1/τ E ⟩ + 1 τ E log 1 -1/τ E 1 -⟨1/τ E ⟩ ≈ 1 2τ E [⟨1/τ E ⟩ -1/τ E ] 2 + 1 2 1 - 1 τ E [⟨1/τ E ⟩ -1/τ E ] 2 = 1 2 [⟨1/τ E ⟩ -1/τ E ] 2 , [S13]

a cost that increases quadratically with the change in the averaged switch probability ⟨1/τ E ⟩ away from 1/τ E .For a passive agent, this direction is 0 unless we allow for α to vary, which leads to the relation

G(τ E , τE ) = α 2 2 f (τ * m ) 2 . [S14]

Eq S14 tells us that if we vary α, we must pay a stabilization cost that, at least locally, grows quadratically with the strength of stabilization with zero gradient.The simplest contribution is with respect to the change in the precision timescale τc.Divergence, as derived in Materials & Methods, is proportional to 1/τc.On the other hand, precision cost is C = log τc.Since optimal memory timescale does not depend on τc, the change of the total divergence is

∂τ c [D 1 /τc + β log 2 τc] = -D 1 /τc 2 + β/τc, [S15]

where we take D * = D 1 /τc to encapsulate the terms in the divergence apart from the scaling with precision timescale.If this has a minimum at positive τc, the value of τc at which the minimum is reached is τc * = D 1 /β.Putting all of these together, we have the terms in the gradient

∂τ m D = 2a(τm -τ * m ) ∂αD = D 0 2 (τ * m ) -3 2 + a µ 2 (2τ * m + 1) 2 log(2)(τ * m ) 3 (τ * m + 1) 3 ∂τ * m ∂α ∂τ c D = β/τc -D 1 /τc 2 [S16]

When the cost gradient ∂αD < 0, a population of passive agents is driven towards niche construction and when ∂τ c D < 0 towards precision reduction.Thus, the conditions that lead to reduction in agent complexity by increasing memory, enhancing stabilization, and lowering precision are captured by these gradients.

A similar derivation can be made for the evolution of a starting population of destabilizers, or agents with α > 0, instead a pure population of passive agents.However, this requires us to deal with all the terms in Eq S11 and to account for a term from the gradient of stabilization cost in Eq S16 instead of assuming α = 0.The change in the environmental timescale is more complicated to calculate because we must then consider the way that destabilization determines the modified environmental timescale in Eq S9, but it is clear that the qualitative results will be the same because of the adaptive gain from slower environmental timescales, i.e. decreasing α, but the exact rate at which α changes will depend on the curvature of the stabilization cost.

### D. Metabolic costs of neural tissue for memory

In the total divergence in Eq 18 and as discussed in Appendix C, we consider information costs separately from energetic, metabolic costs of neural tissue.An important consideration for comparing the costs directly with one another is that that the right units for comparison are not clear, an issue that we avoid by only considering the scaling exponents presented in Result 3. Furthermore, while the scaling argument makes clear that the metabolic costs will dominate at sufficiently long lifetimes, the differences in how information and energetic costs affect reproductive fitness make a direct comparison in a combined "total divergence" equation problematic.

Nonetheless, if we do entertain the inclusion of metabolic costs into the total divergence, we will find that rising metabolic costs with environmental timescale will lead to a upper cutoff, i.e. truncating memory at some point beyond which the benefits of increasing stabilization are counteracted by the monotonically increasing costs of supporting neural tissue for memory.

To show this more formally, we redo the calculations in the previous section with an additional metabolic cost of memory, obtained from ∂τ m [ D + µH + γF ] = 0 and using the approximation that both µ and γ are small.The perturbative assumption is not necessary to take, but then there is no closed analytical solution for the shifted optimal memory τ * * m that we can write down.Eq S18 shows us that memory complexity, the term proportional to µ, tends to drive optimal memory τ * * m up but the metabolic cost, the term proportional to γ, tends to drive it down, the balance of which determine the exact change in optimal memory.

D = D + µH(τm) + χG(τ E , τE ) + βC(τc) + γF (τm), [S17]

Taking the approximation in Eq S18 the shifted optimal divergence, denoted by an apostrophe, becomes

D′ (τ * * m ) = D * + a µ 2 4(log 2) 2 (τ * m ) 2 (τ * m + 1) 2 + γ 2 ϕ 2 (τ * m ) 4ϕ a 2 (τ * m + 1) 2 - aϕµγ(τ * m ) 2ϕ 2(log 2)aτ *

m (τ * m + 1) 2 + O(µ 3 ) + O(γ 3 ) + O(µγ 2 ) + O(µ 2 γ).

[S19]

Again, perturbations about the local optimum lead to

D′ (τm) ≈ D * + a µ 2 4(log 2) 2 (τ * m ) 2 (τ * m + 1) 2 + ϕ 2 (τ * m ) 4ϕ a 2 (τ * m + 1) 2 -aϕµ(τ * m ) 2ϕ 2(log 2)aτ * m (τ * m + 1) 2 + b(τm -τ * * m ) 2 [S20] for some positive constant b, which implicitly depends on the complexity cost.Assuming that the population is at optimal memory, we obtain for the partial derivative with respect to α ∂α D′ = -D 0 2 (τ * m ) -3/2 + a µ 2 (2τ * m + 1) 2(log 2)(τ * m ) 3 (τ * m + 1) 3 + 2(log 2)ϕ 2 a -2 (τ * m ) 4ϕ + µϕ(τ * m ) 2ϕ-1 (log 2)(τ * m + 1) 3 -4(log 2)ϕ 3 (τ * m ) 4ϕ-1 + 2 -1 µϕ(2ϕ -1)(τ * m ) 2ϕ-2 (log 2)(τ * m + 1) 2 ∂τ * m ∂α .

[

Unlike the previous outcome in Eq S8, it is not necessarily the case that a stronger stabilizer will decrease divergence because sufficiently large metabolic costs will counteract the adaptive benefits of a slower environment.

Table S2.Variables used in main text organized by section in which they are first introduced or used.

### Model structure & assumptions

Description At discrete agent state at time t, e.g.{-1, 1} Et discrete environmental state at time t, e.g.{-1, 1} h0 parameter for strength of environmental bias h agent bias ĥ agent's estimate of environmental bias h E environmental bias p agent's probability distribution over possible states of At after time integration p agent's estimate of environment probability distribution at time t based on present samples p E environmental probability distribution over possible states of Et q probability of change in environmental bias at a single time step s state of environment taking values of -1 or 1 t time v construction rate curvature α construction rate weight, α < 0 for stabilizers and α > 0 for destabilizers β learning weight in Eq 4; coefficient of precision cost in Eq 18 ϵτ c perceptual error ητ c estimated bias error τc sampling duration, inverse precision τE environment duration τ f niche construction duration τm agent memory duration Result 1 Parameter Description D time-averaged Kullback-Leibler (KL) divergence D * time-averaged KL divergence at optimal memory duration D KL KL divergence τ * m optimal memory duration
