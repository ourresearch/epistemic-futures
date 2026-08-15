---
title: "Conflicts of interest improve collective computation of adaptive social structures"
person: david-krakauer
section: by
type: journal-article
year: 2018
date: 2018-01-05
venue: "Science Advances"
authors: "David C. Krakauer et al."
source_url: https://doi.org/10.1126/sciadv.1603311
retrieved: 2026-08-13
content: full-text
notes: "OpenAlex W2788405230; cited_by 28; OA status gold. Retrieved via EuropePMC fullTextXML (PMC5777398)."
---

# Conflicts of interest improve collective computation of adaptive social structures

## Full text

## Abstract

Conflicts of interest between members of a group can improve the accuracy of the collective computation they perform.

## INTRODUCTION

In biology, function emerges from the interactions of components making decisions with imperfect information. For example, behavior at the whole-organism level emerges from the firing activity of billions of neurons, each of which is responding to noisy input (, ). Quorum-sensing bacteria are able to detect the local density of conspecifics and change their behavior when density is sufficiently high, for example, producing a toxin or phosphorescing. This output depends on the individual cells’ “decisions” to produce a signaling molecule when they detect other bacteria close by (, ). At a much larger spatial scale, in macaque and chimpanzee social groups, a distribution of power is the outcome of noisy decisions between pairs of individuals about which is subordinate (–). In several species of fish, the collective motion of a school emerges from the movements of individual fish, with movement decisions based on how fish perceive the environment and register the positions of neighbors (–). The ability of ant nests to keep out ants that do not belong can emerge collectively from decisions individual ants make when they can distinguish those they have met before from those they have not (). These examples have inspired engineered networks: A group of robots can be designed to accomplish a task by interacting with each other and the environment according to specific rules ().

In each of these systems, individuals gather information in noisy environments and change their behavior as they become better informed. Under some conditions, the joint behavior of individuals produces a stable aggregate-level pattern, which feeds back to affect the components’ fitness. This two-part process constitutes a collective computation (in table S1, we list the inputs and outputs of the individual-level and collective computations in each of these systems) (–). In many instances, these groups are able to produce collective computations that are beneficial for the individuals and the group, even though the individual group members are subject to noisy inputs from the environment, have conflicts of interest, and have finite time in which to make decisions. For example, fish schools are able to successfully navigate their environments (–), even though individual fish do not have perfect information, either about the environment or about the positions of the other members of their school, and different fish prefer different directions (, ).

## Principles of collective computation

We introduce a model of collective computation and ground our analyses in the collective computation of power structure in a primate society. To understand how groups collectively compute solutions, we partition collective computation into individual and collective phases (). At the individual level, we ask how individuals make decisions based on accumulated information (). At the collective level, we consider information aggregation, that is, how these decisions combine to produce a computation. Our goal is to understand how the quality of the computation varies as a function of both the strategies individuals use to make decisions and the mechanism required to aggregate the information encoded in individual decision-making.

At the individual level, three factors are important in decision-making: (i) making an accurate assessment of the environment, (ii) the time it takes to reach a decision, and (iii) one’s self-interest, as opposed to the collective interest. In general, it is not possible to optimize all three of these factors. There is almost always a trade-off between speed and accuracy because taking more time to accumulate information results in a more accurate decision. This trade-off affects the strategies that animals use to reach decisions (). There are also trade-offs between decision speed and realizing a preferred outcome. For example, in a fight, being stubborn and waiting for one’s opponent to give up first makes winning more likely, but it also makes the fight last longer. In animal conflicts, human warfare, and economics, this trade-off has large effects on the strategies that individuals use to resolve differences (–). Finally, there is a trade-off between collective and immediate self-interest. For example, for groups to stay together, individuals must make compromises between the direction the group should be moving, to migrate successfully or to maximize the group’s food intake, and individual movement preferences. The relative importance of group accuracy versus individual preferences affects both how individuals make decisions about how to move and the accuracy with which the whole group can navigate (, , ). Although there are many studies considering trade-offs between two of these three factors—accuracy, time, and individual preference—few consider the interaction between all three.

The question of how individual-level decisions are combined to compute an output is essentially a problem of consensus formation. There are two senses of consensus: The group can come to consensus with all individuals or components settling on a single decision, which can be called redundant consensus. In the brain, neurons can reach redundant consensus where they all “agree” about what is present in a visual stimulus, which can help the brain discriminate among alternatives (). Fish schools navigate more quickly and accurately when there is a higher degree of redundant consensus about where to move (–). On the other hand, as each group member forms an opinion about, say, the value of another member of the group, the degree of agreement among group members about that value can be encoded collectively, with individuals retaining their own opinions, which can be called collective consensus. In the primate model system studied here, an individual’s power depends on collectively encoded consensus among members of its group about its ability to use force successfully (, , ).

We have reviewed algorithms for computing collectively encoded consensus elsewhere (, ). Here, we focus on the functional utility of the collective computation, with emphasis on two properties in particular: the accuracy of the collective computation and the skewness of the consensus values that are the output of the computation. In the neural case, the accuracy of an individual’s decision, given the environmental input, affects how successfully an individual will interact with its environment. If an individual is trying to decide among many alternatives, each alternative may be assigned a value that reflects the neurons’ collective certainty about that alternative. It should be easier to discriminate among alternatives if the distribution of consensus values is right-skewed ().

In the primate model system, “accurate” power scores—those that reflect the animals’ fighting abilities—are useful because if a monkey can estimate another’s power, then it can predict whether it will win in a fight against the other monkey and what the cost of interacting with it will be (). A power structure that accurately reflects the monkeys’ fighting abilities is also more stable because marked role reversals are less likely to occur (). Right skewness is also valuable in this system. As in the neural example, right skewness in the power distribution can be interpreted to mean that there is high confidence within the group that a few individuals are disproportionately powerful. These individuals pay little cost during conflicts and can afford to engage in costly conflict management behavior that is beneficial to the group (see the detailed description of the model system below) ().

## Models of individual and collective computation

A variety of models, including the leaky integrator model (, –) and the sequential probability ratio test (SPRT) (, ), have been developed to study how components (for example, individual animals or neurons) choose among alternatives in a noisy environment [reviewed in the study of Ratcliff et al. ()]. For example, the leaky integrator model has been used to describe the firing of neurons during a motion coherence task in which a subject must decide whether it is seeing dots moving left or right (–, ). Both the leaky integrator model and the SPRT keep track of the amount of accumulated evidence supporting alternative choices. The leaky integrator model has the advantage over the SPRT of allowing for memory loss, but application of the leaky integrator model to explain, for example, neural firing, has been largely phenomenological (more details on these decision-making models are provided in section S1).

Here, we develop a leaky integrator model by deriving stochastic differential equations (SDEs) that mechanistically specify how information is accumulated by components and is used in decision-making. We use empirical and computational results from work on collective computation in a primate society model system to justify the form of our equations. Our model extends the standard leaky integrator model in two ways: In addition to considering the accuracy of the decision and the time it takes to make a decision, we introduce a game theoretic element describing an individual’s preference to be dominant, and we use the stochastic model to generate a network of pairwise decisions between many individuals, rather than just two. These extensions allow us to study how the importance of the three decision properties—error rate, decision time, and individual preference about the decision—influence (i) the “correctness” of the collective computation of social structure, (ii) the accessibility of different social structures, and (iii) the best way to perform the collective computation.

## RESULTS

## Impact of conflict on signaling decision

The weight w3, given to the probability of an individual’s preferred outcome being reached, indicates the strength of the conflicts of interests between pairs of individuals. We start with a pair of individuals, that is, a group size of two, to build intuition for how the optimization weights affect the Nash equilibrium thresholds. If the error rate of the decision is important (w1 = 1), the Nash strategies are for the weaker individual to set its threshold as low as possible and the stronger individual to set its threshold as high as possible (). This will, with high probability, lead to the weaker individual signaling, which is the correct outcome. When only decision preference matters and there is a strong conflict of interest between individuals (w3 = 1), the Nash strategies are for both to set their thresholds high because each prefers to wait for the other to signal and there is no incentive for the individuals to stop accumulating evidence (). As the importance of decision time increases, the Nash thresholds of both individuals decrease, which enables them to reach the decision more quickly (, A to D). The error rate with which a pair using Nash thresholds can reach a decision is lowest when only error rate matters (w1 = 1) and increases as either decision time or decision preference becomes more important ().

[figure omitted]In a group with more than two individuals, the Nash thresholds respond to the optimization weights in a similar way (). There is a significant change brought about by introducing additional individuals: As long as there are nonzero waiting costs, the average error rate of all decisions in a group using Nash thresholds decreases as error rate becomes less important and decision preference becomes more important (this can be seen by moving from left to right in  and directly in ). This can be explained as follows. Consider a case where only error rate and decision time matter (as in the blue curve in , where w1 = 0.9, w2 = 0.1, and w3 = 0). When any individual raises its threshold, it becomes less likely to emit the subordination signal to all of its opponents. This is the correct behavior when it interacts with animals with lower ability, but an error when it interacts with animals with higher ability. Thus, when an animal increases its threshold, there are three effects: a lower error rate in its decisions with lower animals, a greater error rate in its decisions with higher animals, and an increase in its average decision time. Even if the animal’s total error rate would be smaller with a higher threshold, the improvement will be small because of the increase in its error rate with higher animals, and it has to pay the cost of a greater average decision time. Being at Nash equilibrium means that it cannot improve its utility by increasing its threshold. However, if the animal starts to value receiving the subordination signal and decision preference starts to matter (w3 > 0), then the errors made by waiting for higher animals to signal are no longer perceived as costly and are instead perceived as beneficial. This provides an incentive for it to raise its threshold and pay the costs for waiting longer to make decisions. Therefore, increasing the weight given to decision preference encourages all individuals, except the very strongest and the very weakest, to raise their thresholds (, compare iii and iv). (The strongest individual always uses the maximal threshold allowed. The weakest would have to wait so long to receive the signal that if there are any costs to waiting, it will not raise its threshold above the minimum allowed.) Because nearly all members of the group raise their thresholds, all decisions take longer, resulting in a decrease in the average error rate of all decisions. (We analyzed a group of n = 20 individuals. In fig. S6, we show that our results are robust to increasing group size. In fig. S7, we show how the amount of time it takes for a pair to make a decision depends on the optimization weights and on the difference in their abilities.)

[figure omitted]

## Impacts of conflict and waiting costs on collective computation

For each consensus algorithm, the mutual information between the distribution of social power (DSP) and the underlying distribution of abilities increases as the pairwise error rate decreases (fig. S8). Hence, the information content of the consensus scores produced by every algorithm is improved when decision preference is prioritized over error rate (), as long as the group has more than two components and there are nonzero waiting costs.

For each measure of consensus, skewness of the DSP is maximized at intermediate waiting costs and does not depend strongly on the trade-off between error rate and preference () (see section S3 for more details). Example distributions are shown in fig. S9. Results for all algorithms are shown in figs. S10 and S11.

[figure omitted]

## Impacts of waiting costs on which consensus algorithm is most informative

For a fully developed network, when there are no waiting costs and decision preference matters (w2 = 0 and w3 ≥ 0.3), weighted in-degree is the most informative algorithm (). When there are no waiting costs and the error rate is very important (w2 = 0 and w3 < 0.3) or when there are small waiting costs (0 < w2 ≤ 0.3), eigenvector centrality is the most informative algorithm (). These more “global” consensus algorithms do well when waiting costs are low because, in these circumstances, the edges of the decision network tend to be accurate and these measures make use of more information in the network. When waiting costs are higher, unweighted in-degree and entropy are more informative than eigenvector centrality, but only by a very small margin (for further discussion, see section S10). When we consider the status-signaling network as it develops, we find that eigenvector centrality has the advantages of never losing information content and consistently performing well on networks that are not fully formed (, B to D).

[figure omitted]

## DISCUSSION

Conflicts of interest are a general feature of biological and social systems when resources are scarce or fates are not fully shared [for example, (, )]. The dominant view in biology is that conflicts of interest are negative because conflict can lead to instability, gridlock, and increased mortality [for example, (, –)]. Yet, some data suggest that when conflicts of interest are expressed as controlled antagonisms (for example, fights) in which components can challenge one another at relatively low cost, this can foster invention and innovation (, –), facilitate information flow (), allow components to test strategies (), and even improve social cohesion (). Hence, under some conditions, it appears that conflicts of interest can be beneficial.

We find support for this view. Specifically, we study a theoretical model of collective computation, based on data from a primate society model system. In the first stage of the model, pairs of components learn about each other through a stochastic process. Then, we quantify the collective computation of consensus by measuring the consensus encoded in the network of pairwise decisions about each individual’s ability. The components in the model have a strategy that dictates how they make pairwise decisions. We study how the Nash equilibrium strategies depend on the importance of the accuracy of the pairwise decision, the amount of time it takes, and the desired outcome. We find that (i) conflicts of interest can improve the accuracy of the collective computation to the benefit of all individual competitors and (ii) the output of the collective computation, in particular the skewness of the distribution of consensus scores, can be tuned by manipulating properties of conflict dynamics. When there are conflicts of interest, each member of a pair desires a different outcome. Strengthening these conflicts essentially makes the components more stubborn, which leads to increased decision times, and, on average, improves the quality of information aggregation at the group level.

These findings improve our understanding of the emergence of power structure in primate social groups. In particular, they show how our primate model system may be able to construct a power structure that both accurately reflects the animals’ fighting abilities and is right-skewed (, , ). The former can be achieved through the conflicts of interest inherent in the system. The latter can be achieved by changing the costs of waiting for a decision, for example, by fighting more aggressively and making it more likely for combatants to incur injuries (more details on how these costs can be tuned are provided in section S11).

More broadly, our findings provide a novel way of interpreting the widespread observation of competitive dynamics as a means of obtaining the most reliable information about components of a system, rather than solely as a mechanism by which components can gain access to resources (for more details on how our work extends previous findings on animal conflict, see section S12). Together, previous results about the benefits of conflict in biological systems (, –), along with those presented here, have implications for understanding the evolution and social engineering of information aggregation mechanisms and collective computation. If this view of the utility of conflicts of interest is correct, then we predict, following the study of Stearns () and Krakauer and Mira (), that when information processing is noisy and uncertainty is high, either strong regulatory mechanisms or conflict arenas will be a general feature of collective computation in biological and social systems, from biofilms to financial markets.

Our finding also suggests that in the design of any collective computation, it could be advantageous to introduce conflicts of interest between agents. For example, imagine a group of robots tasked with evaluating the relative likelihood of various events, where each robot is responsible for gathering evidence that a given event will occur and pairs of robots compare how certain they are about their assigned events. Our results suggest that the network as a whole would come up with more accurate predictions if the robots were “rewarded” for being more confident in their assessments than if they were rewarded only on the basis of the accuracy of their individual assessments.

The stochastic learning model that we derived based on our primate model system is nearly equivalent to one that has been used to describe stochastic learning in neural populations [for example, (–, )]. Our model extends this leaky integrator model by incorporating game theoretic strategic decisions and a social context, thus addressing some challenges associated with collective computation of social structure. This raises the possibility of a reapplication of the extended framework to collective computation in populations of neurons, where conflicts are not assumed to be common (, ). Conflicts of interest, even among the cells within somatically clonal tissues, could make the brain a better decision-maker. This provides indirect support for neural Darwinism (). When accuracy is not important for decision-making, competitive self-interest reduces to the “war of attrition” game in the game theory literature (for more details, see section S13) (–). The similarities between three frameworks—social decision-making, neural decision-making, and game theory—suggest that there are principles of collective computation that could be applicable to a large class of decision problems in which information is distributed and noisy.

## MATERIALS AND METHODS

## Model system

Our model system was a well-studied captive group of pigtailed macaques (Macaca nemestrina; n = 48). This system is characterized by social learning at the individual level, frequent non-kin interactions, multi-individual conflict interactions, and social structures that arise from nonlinear processes and feed back to influence individual behavior (see section S2 for more details) (–, , , , ).

Each individual learns about the fighting ability of other members of the group through direct fighting and observation (for operational definitions, see section S2.1). If an individual loses many fights against an opponent, it will come to perceive a large asymmetry in fighting ability in its opponent’s favor and will perceive the cost of continued aggression with the opponent as greater than the cost of accepting the subordinate role (). When this happens, the focal individual can decide to emit a silent-bared teeth display. The silent-bared teeth display communicates agreement to the subordinate role in a relationship when emitted during peaceful contexts (). The signal is highly unidirectional, that is, if one individual emits a silent-bared teeth display to another in a peaceful context, then the second individual is highly unlikely to emit the signal to the first (, ). Fighting after signals are exchanged is reduced, continuing at a low level, so that the relationship can reverse if the fighting ability of the weaker individual improves. The decision to emit the signal constitutes an individual-level computation that involves integrating over a history of fight outcomes to estimate the magnitude of asymmetry between a pair of individuals. The output is a dominance relationship.

An individual’s power in the group depends on the degree to which it is collectively perceived as capable of using force successfully in fights (). Individuals can estimate power by observing (some subset of) the network of subordination signals emitted between all pairs of individuals. The distribution of social power (DSP) in the group results from the collective computation by all individuals of their power scores (see also section S2) (, ). The functional significance of power is evident in how it changes social interactions. Individuals treat each other differently according to the power they perceive each other to have: Individuals solicit support in conflicts from powerful individuals more often, and powerful individuals use less aggression and receive less aggression when they do intervene in conflicts (, ). Consensus in the group about the capacity of an individual to successfully use force can be measured directly from the network of subordination signals. In previous work, we identified seven network metrics that assigned individuals scores that were significantly correlated with their power scores, as quantified by these social variables (, ).

Both the accuracy with which the DSP reflects “true” fighting abilities and the skewness of the DSP are functionally important. If the DSP has high mutual information with the underlying distribution of fighting abilities, it will be a reliable predictor of interaction cost (). The fact that the distribution of power changes relatively slowly, marked changes in individuals’ power being relatively rare, and the fact that the individuals do seem to use information about the distribution of power to decide how to interact with each other both suggest that, in this system, the DSP is in fact highly informative about the individuals’ fighting abilities. The skewness of the DSP influences conflict management. Heavy-tailed distributions make otherwise costly conflict-management strategies, such as policing, accessible to individuals who occupy the tail of the distribution of power (see section S2 for details on policing and section S3 for further explanation of the importance of skewness in primate social structure) (). It therefore appears from the data that the study group was able to compute a DSP that was both accurate and structured in a beneficial way. Our goal was to understand the factors influencing the quality of the collective computation and how the group overcomes a noisy learning environment and the inherent conflicts of interest in this system.

## Stochastic approach

Here, we developed a model describing the collective computation of social structure. First, we developed a stochastic model of individual decision-making—in this case, whether to signal subordination. The SDEs used to model noisy decision processes are typically presented without derivation. Here, we followed the mathematical derivation of SDEs in chemical systems, as given by Gillespie (), to derive equations for how an individual learns about the fighting ability of each of its group mates. Each individual in the group accumulates evidence about its fighting ability relative to another individual by keeping track of the fights it has won and lost. For a given pair of individuals, A and B, A has a decision variable, X1, indicating the evidence that it has accumulated about its ability relative to B, and similarly, B has a decision variable, X2. In the absence of new information, the decision variables leak back toward 0 with rate l ( lists and defines all the variables used in the text). If there is no input, then over a period of length τ each decision variable decreases as Xi(t + τ) = (1 − lτ)Xi(t).

[table omitted]If they do fight and learn about each other, each individual incorporates this new evidence into its assessment. Specifically, X1 increases by an amount b when individual A wins a fight against individual B and decreases by b when it loses, and conversely for X2. To calculate the variables at time t + τ, we count how many times each type of input occurred in the time since t and add the changes resulting from these events to the background leaky estimate

Xi(t+τ)=(1−lτ)Xi(t)+b×# times i wins in [t,t+τ)−b×# times i loses in [t,t+τ)We ignored the possibility of individuals learning about each other by observing their fights with other individuals. This should mainly increase the rate at which they learn about each other and therefore should not greatly affect our results.

We assumed that individuals fight with each other at a constant rate. We also assumed that, even if one individual is stronger than another, there are random factors that affect which of the two will win a fight. Specifically, we described the number of each type of event—wins and losses—with a Poisson random variable, NA and NB, giving

X1(t+τ)=(1−lτ)X1(t)+bNA−bNBX2(t+τ)=(1−lτ)X2(t)−bNA+bNBIf fights occur at a rate r and A wins with probability c and loses with probability 1 − c, then the expectation of NA and NB in a period of length τ are, respectively, τrc and τr(1 − c). The parameter c ranges between 0 and 1 and is related to the strength of the asymmetry in the individuals’ abilities: If A is stronger, then it is more likely to win and c > 0.5.

When enough events accumulate in an interval of time from t to t + τ, we can approximate the Poisson random variables with normal random variables with mean and variance equal to the mean of the Poisson random variables. Let ZA and ZB be independent standard normal random variables, that is, with a mean of 0 and an SD of 1, giving

X1(t+τ)=(1−lτ)X1(t)+b(τrc+τrcZA)−b(τr(1−c)+τr(1−c)ZB)X2(t+τ)=(1−lτ)X2(t)−b(τrc+τrcZA)+b(τr(1−c)+τr(1−c)ZB)Finally, as we make the period of time shorter, where τ becomes infinitesimally small, these equations become SDEs

dX1=(−lX1(t)+br(2c−1))dt+brdWtdX2=(−lX2(t)−br(2c−1))dt−brdWtwhere dWt is Brownian motion representing the wins and losses for individual A. We assumed that X1(0) = X2(0) = 0. The sensitivity of this model to initial conditions is discussed in section S4.

Nearly identical SDEs have been used to model decision-making in the brain (see section S5 for more details) (, , ). In that case, X1 denotes the firing activity of a neural population responding to one property in the environment, for example, left motion, and X2 denotes the firing activity of a neural population responding to its opposite, for example, right motion. In , we listed the inputs, outputs, and variables of the decision model and how they should be interpreted in both social and neural systems.

## Modeling pairwise decisions—individual level computation

An individual decides to signal to another once it is sufficiently certain that it is the weaker of the two and that the costs of continued fighting are greater than the potential benefits of waiting for the other to signal. Here, B signals to A if X2 becomes very negative, and A signals if X1 becomes very negative. Specifically, there are two thresholds, T1 and T2, such that if X2 < − T2, then B signals and the pair reaches the “decision” that A has higher ability and if X1 < − T1, then A signals and the decision is that B has higher ability. It can be shown that, regardless of how high T1 and T2 are, eventually one individual’s decision variable will reach its threshold and it will signal.

In the empirical system, individuals do not emit subordination signals instantaneously (), so in the model, their thresholds should be greater than zero. Conversely, in the empirical system, every individual except the strongest emitted a subordination signal to at least one other individual (), so in the model, they should have finite thresholds. We restricted the thresholds that individuals in our model could use to be between 0.5 and 2. Our results depended on relative changes in threshold values, not the absolute values of thresholds, so our results should hold regardless of the actual range of thresholds allowed.

In the neural literature, it is usually assumed that the brain can evaluate the difference between two variables, which indicates the relative strength of evidence for each option. In most models of neural decision-making, it is assumed that, if Y = X1 − X2, then the brain decides on X1 when Y is large and positive and on X2 when Y is large and negative (, , ). Again, there are two thresholds, T1 and T2, such that if Y > T1, then the decision is that A has higher ability and if Y < − T2, then the decision is that B has higher ability. This reduces the number of relevant variables from two to one.

In social systems, the one-dimensional simplification implies a third party evaluating the difference in the evidence each individual has accumulated, which is not realistic. Hence, we used the two-dimensional system. In section S4 and in fig. S1, we show that, with our assumption that X1(0) = X2(0) = 0, the two-dimensional and one-dimensional processes are equivalent (we also show that, if X1(0) − X2(0) is not zero, then the two processes are nearly equivalent). Our results therefore also apply when the one-dimensional simplification is used.

## Assessing pairwise decisions

Once the decision thresholds T1 and T2 have been specified, the SDEs determine the probability that each individual’s decision variable will reach its threshold before the other, that is, the probability that either of the two individuals would be the one to emit the subordination signal. They also determine the expected time it would take for one of the individuals to signal. We show in section S6 that each of these quantities—the probability of each individual signaling and the expected time until a signal is emitted—satisfies a partial differential equation that depends on the decision thresholds and the parameters of the model.

A “correct” decision is one that results in the weaker individual emitting the subordination signal. If individual i is the weaker individual and individual j is the stronger individual, then the probability that j incorrectly signals is the error rate (ER) of their decision. Each animal would prefer to receive the subordination signal. Thus, the error rate is equal to the probability of i’s decision preference being reached (DPi), whereas the probability of j receiving the signal and j’s decision preference being reached is 1 minus this quantity (DPj = 1 − DPi). The decision time (DT) for the pair is the expected time until either of the two individuals signals. These quantities determine each individual’s utility from the decision-making process. Winning any particular fight can give an individual access to resources, which may improve its fitness. Once an individual emits the subordination signal, it agrees to be subordinate to its opponent and cedes access to resources when it comes into conflict with that individual in the future. We were interested in the formation of these stable relationships, so we focused on the benefits of receiving the subordination signal, rather than transient benefits from winning any particular fight.

In models of individual conflict and dominance relationships, it is often assumed that both individuals prefer to be dominant, regardless of whether they are in fact stronger [for example, (, , )]. However, a correct subordination signal from a weaker to a stronger individual has been shown to lead to a more stable and affiliative relationship than would be the case had the signal been withheld (, ). Hence, error rate needs to be considered. Conversely, in models of neural decision-making, error rate, rather than decision preference, is assumed to be the currency driving decision-making strategies (). Our model connects these two bodies of work by allowing for both error rate and decision preference to affect individual strategies.

To describe trade-offs between error rate, decision time, and preference, we quantified the utility of the decision process by introducing three weights, w1, w2, and w3 such that w1 + w2 + w3 = 1. These weights describe how the three quantities are prioritized. For individual i interacting with individual j, we defined i’s utility to be

Uij=w1(1− ER)+w2(1−DT)+w3DPiEach individual wants to maximize its utility. Note that it is impossible to minimize both ER and DT because waiting longer and accumulating more evidence will help the pair reach a decision more accurately. The weight w2 can be interpreted as the cost of fighting because, when w2 is higher, the time spent fighting until a decision is reached is more costly. The weight w3 captures the benefit from being the dominant individual in a pair and the extent to which each individual perceives agreeing to be subordinate to be more costly than continued fighting. The higher w3 is, the more stubborn the individuals will be about waiting for their desired outcome. It is impossible for both individuals to maximize DPi, so w3 indicates the strength of the conflict of interests between individuals.

We show outputs of the model that depend on the three weights, w1, w2, and w3, on a triangular simplex, as in . In each such figure, points in the lower left corner indicate that w1 is high; points in the upper corner indicate that w2 is high; and points in the lower right corner indicate that w3 is high. Points on the edge of the triangle indicate that one of the three weights is equal to 0. For example, points on the bottom edge of the triangle indicate that w2 = 0. Moving left means that w1 is increasing and w3 is decreasing; moving right means the opposite; and moving up means that w2 increases.

## Nash equilibrium thresholds

We assumed that if two individuals have equal fighting ability, then any fight between them is a toss-up, that is, c = 0.5, and that as the difference in their abilities increases, the probability of the stronger individual winning approaches 1. We assigned each individual in the model a fighting ability ai. Then, we assumed cij=exp(ai−aj)exp(ai−aj)+1. We further assumed that each individual has the same decision threshold for all the decision processes with each of its peers. Given those thresholds and the importance of error rate, decision time, and decision preference (w1, w2, and w3, respectively), each individual i has a utility Uij from its decision process with individual j and a total utility given by the average of these, 〈Uij〉j. For each set of abilities {a1, …, aN}, we found the Nash equilibrium thresholds {T1, …, TN} such that no individual has an incentive to choose another threshold to improve its total utility. Because the Nash thresholds depend on the abilities {a1, …, aN}, we drew a set of abilities from a uniform distribution 1000 times and found the Nash thresholds for each set.

To show how the weights encoding error rate, decision time, and decision preference (w1, w2, and w3, respectively) affect decision-making strategies, below we reported the average Nash threshold for an individual with the ith highest ability, for each rank i = 1, …, N, where 1 is the strongest and N is the weakest. However, we used the actual Nash thresholds, not their average, in our analyses. Specifically, to show how the weights affect how accurately individuals can make decisions, we considered 1000 groups of individuals using Nash thresholds and take the average error rate across all N × (N − 1)/2 pairs and all 1000 iterations. Similarly, we found the average decision time across all N × (N − 1)/2 pairs in all 1000 iterations of the model, where the individuals in each group used Nash thresholds.

We were interested in understanding the factors influencing whether the collective computation would produce a right-skewed distribution of power. To avoid building in a distribution with a long tail, we used a uniform distribution of fighting abilities because it has short tails. Our results did not change when we used a normal distribution of fighting abilities instead of a uniform distribution of fighting abilities (compare figs. S2 to S4 to  to ). Our procedure for finding the Nash equilibrium thresholds is provided in section S7.

## Modeling collective computation at group level

We used the pairwise decision model to create a directed signaling network among all pairs of individuals. We drew the direction of the signal between each pair according to these probabilities. Once an individual decided to emit the subordination signal, it continued to do so regularly over a long period of time. Eventually, the relationship can reverse if an individual comes to perceive that it could win against an individual to which it has previously signaled (). However, this would take longer than the period of time that we considered, and we do not allow for this possibility. To describe the accumulation of signals over time, at each point in time t, we defined the weight of the edge from i to j to be

0 if j signals to i or t<DTijt if i signals to j and t>DTijwhere, as above, DTij is the time it takes the pair to reach a decision.

Individuals can estimate the degree of consensus within the group by observing (some subset of) the network of subordination signals emitted between all pairs of individuals. For these estimates to be good indicators of the individuals’ true abilities, two things need to happen: First, the edges in the network need to be accurate indicators of the differences in abilities between pairs of individuals, and second, the algorithm that individuals use to quantify consensus needs to aggregate the relevant information appropriately. In previous work, we identified a set of algorithms that can be used to compute consensus about node state in any network (, ). In our system, consensus in the subordination signaling network reflected how much power a node was perceived to have (, ), as described above. For the sake of brevity, we considered four of the best-performing algorithms here.

Of these, the simplest algorithm was the unweighted in-degree of a node, that is, the number of individuals that have signaled to each individual. We also considered weighted in-degree, the sum of all signals an individual receives. The third algorithm that we considered was the entropy of the distribution of the numbers of signals that each individual receives, which gave a coarse measurement of the uniformity of all of the opinions in the group about a focal individual. The fourth was the eigenvector centrality of the network, which measured how central each node was in the global structure of the network (, ). We generated 1000 directed signaling networks as described above. To each of these networks, we applied the four network metrics, each of which generated a DSP.

## Assessing collective computation

We assessed the quality of the output of the collective computation—the DSP—by assessing the accuracy and skewness of the resulting distribution. We operationally defined an accurate distribution as one having high mutual information with the underlying distribution of fighting abilities. This allowed us to study how conflict influences DSP accuracy, as well as the relative ability of each algorithm to recover an accurate DSP [the question of how the system “knows” the desired output has been achieved, called the “halting problem” in computer science, is discussed by Flack (, ) and in section S8]. We measured the mutual information between the consensus scores produced by a given algorithm and the underlying distribution of fighting abilities, over all 1000 iterations of the model (see section S9 for details). We measured the skewness of the set of consensus scores given by each algorithm and took the average over the 1000 iterations of the model. A schematic of the whole model of collective computation, from pairwise decision-making to consensus computation, is provided in fig. S5.

## Supplementary Material

## http://advances.sciencemag.org/cgi/content/full/4/1/e1603311/DC1

## Acknowledgments

We thank B. Daniels, C. Ellison, P. Poon, and E. Lee for helpful discussion. E.R.B. thanks S. Levin for helpful discussion and comments on the model during development. We also thank two anonymous reviewers for their comments, which have greatly improved the paper. Funding: This research was supported by two grants to the Santa Fe Institute from the John Templeton Foundation for the study of complexity, a grant to the Santa Fe Institute from the John Templeton Foundation to study the mind-brain problem, and a grant from the Templeton foundation to study niche construction (JTF number 60501, St. Andrews subaward number 13337), and by ARO (Army Research Office) contract W911NF-13-1-0340. J.C.F. acknowledges the Proteus Foundation. E.R.B. acknowledges support from NIH training grant 5T32HG003284. Author contributions: E.R.B. developed and analyzed the model and wrote the paper. D.C.K. helped develop the model and write the paper. J.C.F. designed the study and collected the data motivating the model, helped develop the model, and wrote the paper. Competing interests: The authors declare that they have no competing interests. Data and materials availability: All data about the model needed to evaluate the conclusions in the paper are present in the paper and/or the Supplementary Materials. Additional data related to this paper and the code for the model may be requested from the authors.

## SUPPLEMENTARY MATERIALS

Supplementary material for this article is available at http://advances.sciencemag.org/cgi/content/full/4/1/e1603311/DC1

section S1. Background on models of decision-making

section S2. Study system

section S3. Skewness of DSP

section S4. Dimensionality and initial conditions

section S5. Analogous model of neural decision-making

section S6. Derivation of partial differential equations for decision time, error rate, and probability of reaching decision preference

section S7. Nash equilibria

section S8. A notion of correctness for biological computation

section S9. Calculation of mutual information

section S10. Most informative measures of consensus

section S11. Tuning waiting costs

section S12. Comparison of our model to previous studies of animal conflict

section S13. War of attrition

section S14. Supplementary table

section S15. Supplementary figures

table S1. Examples of collective computation.

fig. S1. Error rate decreases as decision time increases, as long as the initial conditions are not biased toward the correct decision.

fig. S2. The mutual information of the power scores computed by a group using Nash thresholds increases as the weight given to decision preference increases, as long as there are nonzero waiting costs.

fig. S3. The average skewness of the distribution of eigenvector centrality is maximized at intermediate waiting costs.

fig. S4. The best measure of consensus in the decision network depends on the average error rate and the types of errors being made.

fig. S5. Schematic of the model.

fig. S6. The error rate of a group using Nash thresholds decreases as the weight given to decision preference increases, regardless of the size of the group.

fig. S7. Pairs with similar and high abilities always take as long or longer to make a decision than any other pairs do.

fig. S8. The mutual information of each consensus algorithm is a decreasing function of the average pairwise error rate.

fig. S9. The average skewness of the distribution of unweighted in-degree is maximized at intermediate waiting costs.

fig. S10. The average skewness of the distribution of consensus scores from each measure is maximized at intermediate waiting costs.

fig. S11. The average skewness of the distribution of consensus scores from each measure is maximized at intermediate waiting costs.

fig. S12. When a pair of animals have equal fighting abilities, c = 0.5, there are asymmetric Nash equilibrium thresholds.

References (–)

## REFERENCES AND NOTES

1.Gold J. I., Shadlen M. N., 
Neural computations that underlie decisions about sensory stimuli. Trends Cogn. Sci.
5, 
10–16 (2001).2.Feng S., Holmes P., Rorie A., Newsome W. T., 
Can monkeys choose optimally when faced with noisy stimuli and unequal rewards?. PLOS Comput. Biol.
5, 
e1000284 (2009).3.Bassler B. L., 
How bacteria talk to each other: Regulation of gene expression by quorum sensing. Curr. Opin. Microbiol.
2, 
582–587 (1999).4.Miller M. B., Bassler B. L., 
Quorum sensing in bacteria. Annu. Rev. Microbiol.
55, 
165–199 (2001).5.Flack J. C., de Waal F. B. M., Krakauer D. C., 
Social structure, robustness, and policing cost in a cognitively sophisticated species. Am. Nat.
165, 
E126–E139 (2005).6.Flack J. C., Krakauer D. C., 
Encoding power in communication networks. Am. Nat.
168, 
E87–E102 (2006).7.Flack J. C., 
Multiple time-scales and the developmental dynamics of social systems. Philos. Trans. R. Soc. B.
367, 
1802–1810 (2012).8.Couzin I. D., Krause J., James R., Ruxton G. D., Franks N. R., 
Collective memory and spatial sorting in animal groups. J. Theor. Biol.
218, 
1–11 (2002).9.Herbert-Read J. E., Perna A., Mann R. P., Schaerf T. M., Sumpter D. J. T., Ward A. J. W., 
Inferring the rules of interaction of shoaling fish. Proc. Natl. Acad. Sci. U.S.A.
108, 
18726–18731 (2011).10.Katz Y., Tunstrøm K., Ioannou C. C., Huepe C., Couzin I. D., 
Inferring the structure and dynamics of interactions in schooling fish. Proc. Natl. Acad. Sci. U.S.A.
108, 
18720–18725 (2011).11.Rosenthal S. B., Twomey C. R., Hartnett A. T., Wu H. S., Couzin I. D., 
Revealing the hidden networks of interaction in mobile animal groups allows prediction of complex behavioral contagion. Proc. Natl. Acad. Sci. U.S.A.
112, 
4690–4695 (2015).12.Esponda F., Gordon D. M., 
Distributed nestmate recognition in ants. Proc. R. Soc. B Biol. Sci.
282, 
20142838 (2015).13.Punzo G., Young G. F., Macdonald M., Leonard N. E., 
Using network dynamical influence to drive consensus. Sci. Rep.
6, 
26318 (2016).14.Flack J. C., Krakauer D. C., 
Challenges for complexity measures: A perspective from social dynamics and collective social computation. Chaos
21, 
037108 (2011).15.Kearns M., 
Experiments in social computation. Commun. ACM
55, 
56–67 (2012).16.Hein A. M., Rosenthal S. B., Hagstrom G. I., Berdahl A., Torney C. J., Couzin I. D., 
The evolution of distributed sensing and collective computation in animal populations. Elife
4, 
e10955 (2015).17.J. C. Flack, Life’s information hierarchy, in From Matter to Life, S. I. Walker, P. C. W. Davies, G. F. R. Ellis, Eds. (Cambridge Univ. Press, 2017).18.Shaw A. K., Couzin I. D., 
Migration or residency? The evolution of movement behavior and information usage in seasonal environments. Am. Nat.
181, 
114–124 (2013).19.Couzin I. D., Krause J., Franks N. R., Levin S. A., 
Effective leadership and decision-making in animal groups on the move. Nature
433, 
513–516 (2005).20.Berdahl A., Westley P. A. H., Levin S. A., Couzin I. D., Quinn T. P., 
A collective navigation hypothesis for homeward migration in anadromous salmonids. Fish Fish.
17, 
525–542 (2014).21.Torney C. J., Lorenzi T., Couzin I. D., Levin S. A., 
Social information use and the evolution of unresponsiveness in collective systems. J. R. Soc. Interface
12, 
20140893 (2015).22.Chittka L., Skorupski P., Raine N. E., 
Speed-accuracy tradeoffs in animal decision-making. Trends Ecol. Evol.
24, 
400–407 (2009).23.Daniels B. C., Flack J. C., Krakauer D. C., 
Dual coding theory explains biphasic collective computation in neural decision-making. Front. Neurosci.
11, 
313 (2017).24.Smith J. M., Price G. R., 
The logic of animal conflict. Nature
246, 
15–18 (1973).25.J. M. Smith, Evolution and the Theory of Games (Cambridge Univ. Press, 1982).26.Nalebuff B., Riley J., 
Asymmetric equilibria in the war of attrition. J. Theor. Biol.
113, 
517–527 (1985).27.Brush E. R., Krakauer D. C., Flack J. C., 
A family of algorithms for computing consensus about node state from network data. PLOS Comput. Biol.
9, 
e1003109 (2013).28.Cisek P., 
Making decisions through a distributed consensus. Curr. Opin. Neurobiol.
22, 
927–936 (2012).29.R. Bogacz, E. Brown, J. Moehlis, P. Holmes, J. D. Cohen, “Optimizing reward rate in two alternative choice tasks: Mathematical formalism” (Technical Report 04-01, Center for the Study of Brain, Mind, and Behavior, 2004).30.Brown E., Gao J., Holmes P., Bogacz R., Gilzenrat M., Cohen J. D., 
Simple neural networks that optimize decisions. Int. J. Bifurcat. Chaos
15, 
803–826 (2005).31.Bogacz R., Brown E., Moehlis J., Holmes P., Cohen J. D., 
The physics of optimal decision making: A formal analysis of models of performance in two-alternative forced-choice tasks. Psychol. Rev.
113, 
700–765 (2006).32.Pais D., Hogan P. M., Schlegel T., Franks N. R., Leonard N. E., Marshall J. A. R., 
A mechanism for value-sensitive decision-making. PLOS ONE
8, 
e73216 (2013).33.A. J. De Froment, “Fighting for information: Decision-making, animal contests and the emergence of social hierarchy,” thesis, Princeton University (2010).34.Ratcliff R., Smith P. L., Brown S. D., McKoon G., 
Diffusion decision model: Current issues and history. Trends Cogn. Sci.
20, 
260–281 (2016).35.Shadlen M. N., Newsome W. T., 
Neural basis of a perceptual decision in the parietal cortex (area LIP) of the Rhesus Monkey. J. Neurophysiol.
86, 
1916–1936 (2001).36.Frank S. A., 
Perspective: Repression of competition and the evolution of cooperation. Evolution
57, 
693–705 (2003).37.A. Burt, R. Trivers, Genes in Conflict: The Biology of Selfish Genetic Elements (Harvard Univ. Press, 2008).38.Flack J. C., Krakauer D. C., de Waal F. B. M., 
Robustness mechanisms in primate societies: A perturbation study. Proc. R. Soc. B Biol. Sci.
272, 
1091–1099 (2005).39.Bishop D. T., Cannings C., Smith J. M., 
The war of attrition with random rewards. J. Theor. Biol.
74, 
377–388 (1978).40.Krakauer D. C., Page K., Flack J., 
The immuno-dynamics of conflict intervention in social systems. PLOS ONE
6, 
e22709 (2011).41.Flack J. C., de Waal F., 
Context modulates signal meaning in primate communication. Proc. Natl. Acad. Sci. U.S.A.
104, 
1581–1586 (2007).42.S. C. Stearns, The selection-arena hypothesis, in The Evolution of Sex and its Consequences, S.C. Stearns, Ed. (Birkhäuser, 1987), pp. 337–349.43.Krakauer D. C., Mira A., 
Mitochondria and germ-cell death. Nature
400, 
125–126 (1999).44.Daniels B. C., Krakauer D. C., Flackm J. C., 
Control of finite critical behaviour in a small-scale social system. Nat. Commun.
8, 
14301 (2017).45.Wang X. J.
Probabilistic decision making by slow reverberation in cortical circuits. Neuron
36, 
955–968 (2002).46.Wong K.-F., Wang X.-J., 
A recurrent network mechanism of time integration in perceptual decisions. J. Neurosci.
26, 
1314–1328 (2006).47.Edelman G. M., 
Neural Darwinism: Selection and reentrant signaling in higher brain function. Neuron
10, 
115–125 (1993).48.B. Thierry, M. Singh, W.Kaumanns, Macaque Societies: A Model for the Study of Social Organization (Cambridge Univ. Press, 2004).49.Flack J. C., Girvan M., de Waal F. B. M., Krakauer D. C., 
Policing stabilizes construction of social niches in primates. Nature
439, 
426–429 (2006).50.Gillespie D. T., 
The chemical Langevin equation. J. Chem. Phys.
113, 
297–306 (2000).51.Hemelrijk C. K., 
An individual–orientated model of the emergence of despotic and egalitarian societies. Proc. R. Soc. B
266, 
361–369 (1999).52.Enquist M., Leimar O., 
Evolution of fighting behaviour: Decision rules and assessment of relative strength. J. Theor. Biol.
102, 
387–410 (1983).53.S. Preuschoft, Power and communication, in Macaque Societies: A Model for the Study of Social Organization, B. Thierry, M. Singh, W. Kaumanns, Eds. (Cambridge Univ. Press, 2004).54.Allesina S., Pascual M., 
Googling food webs: Can an eigenvector measure species’ importance for coextinctions?
PLOS Comput. Biol.
5, 
e1000494 (2009).55.J. O. Caldecott, An Ecological and Behavioural Study of the Pig-Tailed Macaque. (S. Karger, 1986).56.de Waal F. B. M., Luttrell L. M., 
The formal hierarchy of rhesus macaques: An investigation of the bared-teeth display. Am. J. Primatol.
9, 
73–85 (1985).57.J. C. Flack, F. B. M. de Waal, Dominance style, social power, and conflict management: A conceptual framework, in Macaque Societies: A Model for the Study of Social Organization, B. Thierry, M. Singh, W. Kaumanns, Eds. (Cambridge Univ. Press, 2004), chap. 8, 157–181.58.S. Preuschoft, Power and communication, in Macaque Societies: A Model for the Study of Social Organization, B. Thierry, M. Singh, W. Kaumanns, Eds. (Cambridge Univ. Press, 2004), pp. 56–60.59.C. Gardiner, Stochastic Methods: A Handbook for the Natural and Social Sciences (Springer-Verlag, 2009).

## Associated Data

## Supplementary Materials

## http://advances.sciencemag.org/cgi/content/full/4/1/e1603311/DC1

Supplementary material for this article is available at http://advances.sciencemag.org/cgi/content/full/4/1/e1603311/DC1

section S1. Background on models of decision-making

section S2. Study system

section S3. Skewness of DSP

section S4. Dimensionality and initial conditions

section S5. Analogous model of neural decision-making

section S6. Derivation of partial differential equations for decision time, error rate, and probability of reaching decision preference

section S7. Nash equilibria

section S8. A notion of correctness for biological computation

section S9. Calculation of mutual information

section S10. Most informative measures of consensus

section S11. Tuning waiting costs

section S12. Comparison of our model to previous studies of animal conflict

section S13. War of attrition

section S14. Supplementary table

section S15. Supplementary figures

table S1. Examples of collective computation.

fig. S1. Error rate decreases as decision time increases, as long as the initial conditions are not biased toward the correct decision.

fig. S2. The mutual information of the power scores computed by a group using Nash thresholds increases as the weight given to decision preference increases, as long as there are nonzero waiting costs.

fig. S3. The average skewness of the distribution of eigenvector centrality is maximized at intermediate waiting costs.

fig. S4. The best measure of consensus in the decision network depends on the average error rate and the types of errors being made.

fig. S5. Schematic of the model.

fig. S6. The error rate of a group using Nash thresholds decreases as the weight given to decision preference increases, regardless of the size of the group.

fig. S7. Pairs with similar and high abilities always take as long or longer to make a decision than any other pairs do.

fig. S8. The mutual information of each consensus algorithm is a decreasing function of the average pairwise error rate.

fig. S9. The average skewness of the distribution of unweighted in-degree is maximized at intermediate waiting costs.

fig. S10. The average skewness of the distribution of consensus scores from each measure is maximized at intermediate waiting costs.

fig. S11. The average skewness of the distribution of consensus scores from each measure is maximized at intermediate waiting costs.

fig. S12. When a pair of animals have equal fighting abilities, c = 0.5, there are asymmetric Nash equilibrium thresholds.

References (–)
