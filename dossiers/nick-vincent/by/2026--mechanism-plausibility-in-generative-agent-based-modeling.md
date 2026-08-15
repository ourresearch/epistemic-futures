---
title: "Mechanism Plausibility in Generative Agent-Based Modeling"
person: "nick-vincent"
section: "by"
type: "journal-article"
year: 2026
date: "2026-06-23"
venue: "ACM FAccT, 2026 · Published"
authors: "Patrick Zhao, David Huu Pham, Nicholas Vincent"
source_url: "https://dl.acm.org/doi/10.1145/3805689.3812388"
retrieved: "2026-08-13"
content: "full-text"
notes: "OpenAlex W7161256790; CV ref [P25]; Full text from the arXiv HTML rendering of the preprint (https://arxiv.org/html/2605.12824v2); This is the preprint version; the version of record is at https://doi.org/10.1145/3805689.3812388."
---

# Mechanism Plausibility in Generative Agent-Based Modeling

## Full text

###### Report GitHub Issue

×

Title:

Content selection saved. Describe the issue below:

Description:

Submit without GitHub
Submit in GitHub

arXiv is now an independent nonprofit!
Learn more
×

Back to arXiv

Why HTML?

Report Issue

Back to Abstract

Download PDF

- Abstract.

- 1 Introduction

- 2 Motivation and Related Work

- 2.1 Operationalization

- 2.2 Phenomenal Models and Generative Sufficiency

- 2.3 Mechanisms

- 2.4 Mechanisms vs Prediction

- 2.5 Plausibility

- 3 A Mechanism Plausibility Scale

- 3.1 Level 0

- 3.1.1 Example

- 3.2 Level 1

- 3.2.1 Example

- 3.3 Level 2

- 3.3.1 Example

- 3.4 Level 3

- 3.4.1 Example

- 3.5 Interpreting the Plausibility Scale

- 3.5.1 The unreachable Ω\Omega simulation

- 4 The Mechanism Plausibility Scale Heuristic

- 5 Discussion

- 5.1 Reflections on the State of LLM Social Simulation

- 5.2 Proprietary LLM APIs and Reproducibility

- 5.3 Broader Ethical and Epistemic Concerns

- 5.4 Historical Issues and Harms of Poor ABM specification

- 6 Conclusion and Limitations

- References

- A Examples

- B Calibrating the Mechanism Plausibility Scale

- B.1 Calibration

- B.2 Round 1 Calibration

- B.2.1 Paper Selection and Review Process

- B.2.2 Inter-Rater Reliability

- B.2.3 Round 1 results of the applied review

- B.3 Round 2 Calibration

- B.4 Queries for LLM ABM-related papers

- C Additional Philosophy of Science Background

- C.1 Clarification of Model Targets TT

License: CC BY 4.0

arXiv:2605.12824v2 [cs.MA] 17 May 2026

## Mechanism Plausibility in Generative Agent-Based Modeling\conffull (\confshort), \confdate, \conflocDOI: 10.1145/3805689.3812388Conference: The 2026 ACM Conference on Fairness, Accountability, and Transparency; June 25–28, 2026; Montreal, QC, CanadaThe 2026 ACM Conference on Fairness, Accountability, and Transparency (FAccT ’26), June 25–28, 2026, Montreal, QC, CanadaISBN: 979-8-4007-2596-8/2026/06CCS: Computing methodologies Simulation evaluationCCS: Computing methodologies Model development and analysisCCS: Computing methodologies Modeling and simulationCCS: Computing methodologies Natural language processingCCS: Human-centered computing Collaborative and social computing design and evaluation methods

Patrick Zhao

email: patrick_zhao@sfu.ca

OrcID: 0009-0000-5494-868X

Affiliation: Simon Fraser University
, Burnaby
, BC
, Canada

,
David Huu Pham

email: dhpham@sfu.ca

OrcID: 0009-0007-6426-7467

Affiliation: Simon Fraser University
, Burnaby
, BC
, Canada

and
Nicholas Vincent

email: nvincent@sfu.ca

OrcID: 0000-0002-8493-7161

Affiliation: Simon Fraser University
, Burnaby
, BC
, Canada

2026© , 2026;

####### Abstract.

Large language models (LLMs) can generate high-level diverse phenomena without explicitly programmed rules. This capability has led to their adoption within different agent-based models (ABMs) and social simulations. Recent research aim to test whether they are capable of generating different phenomena of interest, for example, human behavior on social media platforms or performance in game-theoretic scenarios.

However, capability, prediction, and explanation are different – drawing from the philosophy of science and mechanisms literature, explanation requires showing, to some degree, how a phenomenon is produced by related organized entities and activities. For modelers, describing the characteristics of an experiment or whether a simulation provides progress in capability (or explanation), can be difficult without being grounded in potentially distant research areas.

We integrate recent work on LLM-ABMs with contemporary philosophy of science literature and make two main contributions. First, we gather insights from modeling and mechanisms literature and use them to operationalize a definition of ‘plausibility’ in a four-level scale. Our scale separates the evaluation of a model’s generative sufficiency (ability to reproduce a phenomenon) from its mechanistic plausibility (how the phenomenon could be produced), and clarifies the distinct roles of different models, such as predictive and explanatory ones. We introduce this as the Mechanism Plausibility Scale. Second, we discuss the early wave of LLM-ABM research and find that papers often conflate evidence of Agent-level functionality with claims about emergent ABM-level phenomenon, relying on ‘believability’ metrics that focus on generative sufficiency. Our discussion section speaks on how these findings echo long-standing problems in classical ABM, historical harms caused by these issues, and broader ethical and epistemic concerns about using LLMs in modeling. Using the findings from our review, we offer the scale as a practical heuristic in the form of a checklist which can clarify how simulations at different levels of plausibility may be useful. We hope the activity of filling out the scale will help new modelers ground the epistemic contribution of their simulations.

####### Keywords:

Agent-Based Modeling, Mechanisms, Generative Agents, Large Language Models, Philosophy of Science

††cc-license: by

### 1. Introduction

Developments in natural language processing have spurred interest in using large language models (LLMs) in social simulations (36; 61; 4), for example, extending the action space of agents in agent-based models (ABMs). It seems increasingly possible that product decisions, policymaking, and even research itself may be influenced by the outcome of such simulations (4; 49). Today, a modeler (83) creating simulations with LLMs is capable of reproducing higher-level phenomena without explicitly programming the mechanisms that produce them. In a canonical agent-based model (ABM), the mechanisms underlying a phenomenon are operationalized and programmed by the modeler (e.g., for an economic agent, “if the price of resource AA is XX and my internal requirement BB is at a threshold YY, then buy some amount of resource AA”). These rules are typically based on some combination of assumptions, scientific theory, and empirical data. For instance, a programmer might read several social science papers to determine a particular distribution from which their agents will draw values that represent their preferences and attributes. Using LLMs in simulations offers the tantalizing promise that weights and biases obtained by training on social data may contain relevant distributional information about human behavior, allowing for richer representations of human subjects (77; 4; 61). On the other hand, critiques have also formed around models failing to capture the complete experiences of the human subjects they substitute (1), which leaves us with questions about if this is tied to the nature of LLMs, and if so, the question of if LLMs should be used at all.

When using LLMs in modeling social phenomena, we are left with a few puzzles: For a given simulation, did the results emerge from some correctly retrieved social knowledge encoded in the LLM’s weights? Do our agents model the human behavior we are interested in? This could be the case, given that LLMs are trained on data describing real, human decision-making. Without improvements in the field of machine learning (ML) interpretability and data attribution, it could be the case that simulations incorporating LLMs are drawing on information that is irrelevant to the modeler’s intent (sometimes referred to in the machine learning space as ‘faithfulness’ (87; 64)). In other words, we might produce a simulation that looks like it is explaining a social science phenomenon, but is just generating it through some other means, regardless of the ‘how’. One can imagine that there are many ways in which a phenomenon can occur, and we are only interested in a particular one.

A recent review by Larooij et al. from April 2025 (45) surveyed and found that a number of studies involving ABMs with LLMs (LLM-ABM) fail to acknowledge established work in the traditional simulation literature, or even have proper operational validity. One particular summary is that recent evaluations rest on some variant of believability, where human annotators are tasked with labeling whether or not they think the outputs of agent dialogues are produced by a human. On top of this, much work focuses on whether or not a simulation or its LLM agents are capable of producing a specific phenomenon.

These problems leave us with further questions: Is it necessary to completely understand the inner workings of LLMs to produce useful simulations? What does ‘useful’ mean anyways, in the context of simulations? To facilitate the discussion we connect work from the philosophy of science about what can be learned from idealized computer models, such as ABMs.

Let us consider a target phenomenon TT a modeler is attempting to produce using a simulation SS. In traditional agent-based modeling it is mostly accepted that by generating TT using SS, they realize a possible candidate for how TT is created, sometimes called generative sufficiency (24). By ‘growing’ TT through their simulation, the modeler has created an input-output mapping and demonstrated a sufficient, but not necessary condition for how TT might arise (24).

Now suppose the modeler wants to explain, to some level, how TT arises in actuality–they need to describe the relationship between the simulation’s mechanisms and the “real” mechanisms that produce the target. Mechanisms are the theoretical organization of entities and activities behind a phenomenon (53; 19). In the mechanisms and neuroscience literature a simulation that produces TT without a connection to the “how-actually” is called a phenomenal model (42; 56). Connecting this to ABMs, a modeler might use a simulation to deduce or intuit parts of the mechanisms behind TT; however, since a simulation of TT is only a single possible candidate, one could say that generative success is not sufficient to show the mechanisms in SS correspond to the mechanisms responsible for TT. A modeler could generate TT in many possible ways, perhaps completely unrelated to any hypothesis about its real causes. If a modeler is interested in creating a simulation that helps in explaining the target phenomenon, it needs to convey some level of information about the underlying mechanism and propose how it is mapped to the simulation; that is, they need to show the mechanisms in SS are plausible mechanisms for TT.

In this paper we explain how simulations can vary in their level of plausibility and introduce a set of criteria for categorizing simulations along our axis of interest. This is not to say that the value of a simulation is dictated purely by plausibility or the mechanistic understanding of a model; it is of general agreement that idealizations and abstractions are common, if not, necessary in building accepted models, or science may never move forward (23; 8; 63). Simulations can vary in their level and type of claim, whether they claim to be predictive, illustrative, exploratory, explanatory, etc. However, if a modeler wants to use their simulation to make any level of claim about how TT might arise in actuality (explanatory), they must move beyond a purely phenomenal account.
We present a checklist version of the scale in Section 4, motivated by dataset and model information checklists in past work (29; 58; 86). We believe the scale will guide researchers in developing their own models, especially those integrating LLMs.

In Section 2 we operationalize and elaborate on terms used across the paper such as mechanism, phenomenal, plausibility, and explanation. We aim to show how these concepts can be directly related to existing simulation work in various fields of computing, especially the use of LLM simulation across human computer interaction and computational social science. In Section 3 we introduce a “mechanism plausibility scale” that aims to capture core ideas from the diverse literatures discussed in the preceding section and provide a practical approach for classifying simulations and their contributions. In Section 4 we present the more pragmatic, checklist version of the scale and discuss the reviews involved in its development. Finally, in Section 5 we further discuss contemporary problems of LLM-enabled simulation and how it relates to their placement on these scales.

### 2. Motivation and Related Work

#### 2.1. Operationalization

In the philosophy of science, phenomena are defined to be stable patterns, regularities, or events that can be reliably inferred from data, and are the targets of explanation for scientific communities (10).
The patterns that qualify as ‘phenomena’ are scoped to the particular domain of inquiry (55), and may vary depending on the modeler’s methodological choices or research question (57).

Consider a subject who displays the phenomena of eye contact avoidance and shaking limbs. The phenomena of ‘eye contact avoidance’ is something that is inferred by patterns in the data pertaining to the subject’s average length of eye contact and their direction of gaze. Although behavioral, psychological, or social phenomena may be inferred from aggregated, third-person observational data, the mental experience of, and the cause of these phenomena may only be accessible to the subject experiencing them (76; 39), where outside observers can only agree upon a subject’s apparent reactions to their own internal experience (74). Third-person observers may posit that the phenomena displayed by the subject are indicative of the hypothetical construct of anxiety (52; 20).

Originating from psychometric evaluation, hypothetical constructs are a theoretical attribute postulated to explain observed behavioral patterns, but are not directly observable themselves (52; 20).
We often work with hypothetical constructs in order to characterize and reason about mental and social phenomena (78; 67).
To allow empirical measurements of these constructs, we create operational definitions: these are an explicit, unambiguous set of operations, protocols, or rules that are treated as equivalent to these abstract constructs within the bounds of the experiment, for the sake of falsifiable detection and experimental reproducibility (13).
The process of creating an operational definition for a particular concept is called the “operationalization” of the concept, and determining whether this operational definition measures what it is intended to measure, is called construct validity (20; 26).

Operationalization involves not only translating abstract constructs into measurable patterns, but also assigning interpretations to the formal components of a model. From the modeling and cognitive representation literature (84; 22), we recognize the distinction between a model’s formal functions and the interpretation assigned by the modeler to connect the functions to the domain of interest.
Egan distinguishes between what she calls the “theory proper” of a computational model and an “intentional gloss” that accompanies it (22). The theory proper specifies the mathematical function(s) computed, the algorithms, the structures maintained, and their physical realization. For LLM Agents within a simulation, this would be the next-token probability distribution over a vocabulary, given an input sequence. The intentional gloss is what connects the computation to the modeler’s interpretation, which could be some target persona the modeler says the agent is representing. But as Egan argues, the validity of an intentional gloss is not guaranteed by its computations and requires independent justification, typically grounded in the theorist’s explanatory goals. In our scale interpretation takes the form of an Intent II, which we will return to in Section 3.3.

Since our focus is on simulation models created by researchers, most researchers have particular phenomena that they would like the simulation to produce (32).
We refer to these phenomena of interest as TT, the target phenomena, and we expand on this definition in Section 2.2.
In our review we find gaps in the operationalization of target phenomena used in the evaluation of recent LLM-based social simulations, further discussed in 5.1.

#### 2.2. Phenomenal Models and Generative Sufficiency

The term phenomenal comes from established usage in the scientific modeling field (56; 42), where it is used to describe models that aim to produce the patterns describing a target phenomenon TT, but do not contain information about the mechanism behind it. They may produce an accurate output without describing the relevant internal structure, therefore limiting their explanatory power.

One can imagine that it is not always simple or practical to produce the target phenomenon; In the modeling field, the term generative sufficiency describes the level to which a model is able to accurately produce TT (32). Due to the black-box nature of deep neural networks and other practicality reasons, much of the emphasis in the traditional machine learning field is put on the generative sufficiency of different ML models–how accurately they are able to produce a target behavior. At the time of writing, the primary ways to evaluate LLMs are to measure scores they achieve on some benchmark centered around human evaluation or fact-checking. This mentality may have spread to the LLM social simulation area, as initial projects in the space used similar evaluations to benchmark the realism of their simulation. For example, projects using ‘believability’ as a metric for their sufficiency in producing a target behavior (61; 40; 79; 62; 47; 69).

While generative sufficiency could be appropriate for exploratory or illustrative settings, the goals of a model may not be limited to just reproducing the target behavior; One may want to test unknown counterfactual scenarios or interventions. Problematically, these simulations are evaluated based off of their generative sufficiency and then used to test interventions as if there are plausible mechanisms (37; 27). Phenomenal models cannot be used to test counterfactual scenarios because they lack the relevant internal causal structure. In order to move past being purely phenomenal, the model needs to suggest how TT is produced: the mechanisms behind it.

#### 2.3. Mechanisms

Mechanisms literature has seen a rise in discussion in the past two decades, primarily in the philosophy-of-science and neuroscience fields (19; 31; 53). Glennan gives a minimal definition for mechanisms in his text, The New Mechanical Philosophy:

“A mechanism for a phenomenon consists of entities (or parts) whose activities and interactions are organized so as to be responsible for the phenomenon.” (31)

Pragmatically, in our discussion of agent-based models and computer simulation, this might include how the agents, environment, and update rules function to produce TT.
A mechanism is involved in the causal process of TT, not just correlated, and hypothesizing about them is the first step towards explaining a phenomenon. This hypothesis can take the form of a mapping which details what parts of the simulation correspond to mechanisms behind TT. In our scale the addition of this mapping is what distinguishes a purely phenomenal model from one that presents the plausible candidate mechanisms behind TT.

To explain the mechanisms behind a phenomenon is to explain how the phenomenon is produced (falsifiably). Once some level of description of the mechanisms behind TT are produced, the model is beyond a purely phenomenal account. Kaplan and Craver have summarized these demands into an account called the 3M requirement:

“In successful explanatory models in cognitive and systems neuroscience (a) the variables in the model correspond to components, activities, properties, and organizational features of the target mechanism that produces, maintains or underlies the phenomenon, and (b) the (perhaps mathematical) dependencies posited among these variables in the model correspond to the (perhaps quantifiable) causal relations among the components of the target mechanism.” (41)

To be clear, an explanation does not need to constitute every detail down to the atomic level; it can use an adequate level of abstraction or idealization to fit the use case of the modeler (75; 17). For example, in Figure 1, lower-level mechanisms beyond the ‘Agent-level’ could be further explored and abstracted, but may be stubbed at the modeler’s adequate level of abstraction.

We note that mechanisms cannot be identified in isolation, and therefore the target phenomena need to be operationalized before identifying any mechanisms. Craver suggests, “mechanistic explanations can fail because one has tried to explain a fictitious phenomenon, because one has mischaracterized the phenomenon, and because one has characterized the phenomenon to be explained only partially.” (18) Mechanisms are not just ‘static’ concepts, they are functions that are defined relative to a phenomenon. Its identity, boundaries, and relevance are all defined by the specific outcome it is supposed to explain (19; 30). Therefore, as we will see later, in our Mechanism Plausibility Scale the operationalization precedes the hypothesis.

#### 2.4. Mechanisms vs Prediction

The focus on the productive process of a phenomenon distinguishes mechanisms from predictivism or correlation. One can use a barometer reading to predict weather, but the changing air pressure it measures is not the mechanism that produces it. In causal inference, this is the difference between observational and interventional questions (66; 65). A predictive model is appropriate for questions such as “given these initial conditions, what outcomes are likely?”
Without plausible mechanisms, however, a model’s predictive outputs are usually only appropriate to the extent that they can be validated against observed outcomes. For scenarios that have been or can be empirically tested, this validation may suffice (72). But for novel interventions, mechanisms provide the basis for reasoning about whether the model’s outputs are acceptable.

This distinction between explanation and prediction is well established and known to be easily conflated (72). The two goals require different criteria for model evaluation, different relationships to the underlying data-generating process, etc. An explanatory model aims to test causal hypotheses about the process producing TT; a predictive model aims to produce accurate forecasts of new observations, and may do so using variables that have no/weak causal relationship to the outcome. Conflating the two is a category error that appears in both classical statistics and, as we argue, in early LLM-ABM work.

#### 2.5. Plausibility

The definition of plausibility can be vague, subjective and is often treated as a qualitative property. A general definition from the Stanford Encyclopedia of Philosophy: “To say that a hypothesis is plausible is to convey that it has epistemic support: we have some reason to believe it, even prior to testing.” (9)

In this paper, we operationalize plausibility in ABMs based off of its standing on our scale (presented in Section 3), which encapsulates factors such as how a simulation’s components are operationalized, the type of evidence used to justify its parameters, the model’s relationship to hypotheses the modeler is presenting, etc. In particular, we are interested in if a model is a faithful representation of the modeler’s intent. As mentioned previously, scholars recently publishing in the LLM-ABM space have used believability/plausibility metrics like human annotation to support their simulations. We find that the task of identifying what these evaluations actually provide support for is elusive for even seasoned and capable researchers when it is applied to LLM simulation, giving us the primary motivation for developing our scale.

Figure 1.
An adapted Craver diagram (18) showing a simulation producing TT with higher and lower-level mechanisms. In the ABM, the agents/entities {x1,…,xm}\{x_{1},\ldots,x_{m}\} (circles) and activities {ϕ1,…,ϕn}\{\phi_{1},\ldots,\phi_{n}\} (arrows) work to produce TT. The agents in the ABM are further and reciprocally constituted by lower-level mechanisms, which are generally abstracted away for the purposes of tractability, but are also why simulations can never be fully validated (see Level Ω\Omega in Section 3.5).

### 3. A Mechanism Plausibility Scale

Now that we have distinguished explanatory models from predictive and illustrative ones, we introduce an axis for models as plausible explanations.

Craver: “For those interested in building plausible simulations, it will not suffice for simulation SS simply to reproduce the input–output mapping of target phenomenon TT. The model is further constrained by what is known about the internal machinery by which the inputs are transformed into outputs. It is possible, for example, to simulate human skills at multiplication with two sticks marked with logarithmic scales; but that is not how most humans multiply.” (17)

If we want a simulation to be a plausible representation for how TT is created, it is not sufficient to just reproduce TT – the simulation mechanisms must be adequately close to being a proxy for how TT may actually be generated (41; 84).

We formalize a model as a four-tuple M=(S,T,I,E)M=(S,T,I,E): Simulation (SS), Target phenomenon (TT), modeler Intent (II), and Evidence (EE) (these terms will be further defined below). We use this four-tuple to create a corresponding four-level Mechanism Plausibility Scale. Models climb our scale as more components of MM become falsifiable and relevant in explaining its mechanisms, as well as being overall more faithful in representing the modeler’s intentions. To make the scale concrete, we will revisit at each level a high-level running example: a (hypothetical) LLM-based simulation of opinion dynamics on a social media platform.

#### 3.1. Level 0

A Level 0 model is a ‘toy’ simulation or sandbox with no specified modeling goal. It consists of a Simulation SS, which is set of procedures, code, and update rules that generate outputs but lacks a clearly defined phenomenon to explain. Since mechanisms are defined relative to a phenomenon (sometimes referred to as Glennan’s Law) (30; 19), a model without a target cannot have mechanisms. We place models that lack explicit operationalization of a target TT unintentionally in level 0 as well.

##### 3.1.1. Example

A research team builds a sandbox where LLM agents are placed on a simulated social network and allowed to post, reply, and share content freely. The purpose is to demo and explore a new simulation technique. The researcher documents the system and observes what happens, but has no specified phenomenon to reproduce or explain.

#### 3.2. Level 1

To reach Level 1, a model must add an operationalized target TT.

Models that do not convey anything about the underlying mechanism are said to be phenomenal, their purpose being pattern reproduction rather than creating hypotheses with their simulation (17; 19). Models at level 1 are phenomenal; They have an operationally defined TT and are considered generatively sufficient if its simulation SS can produce the operationalized patterns of TT. However, it makes no claims about explanation. SS exists to produce TT in any way. To put it another way, they are ‘hard-coded’ simulations that produce a set of data points which match a pattern operationalized as TT.

Recently, Level 1 models using LLM agents have been used to explore the capabilities of different language models in cooperation, games, and other environments. The goal is not to accurately model the scenario, but to benchmark how different LLMs perform in those abstract environments. For example, there exists a multitude of work on placing LLMs in game-theoretic scenarios to see how they act or perform (2; 16; 35; 43; 50).

The research questions of these simulations often follow the lines of “can some LLM agents produce behaviors {x0,x1,…,xm}\{x_{0},x_{1},\dots,x_{m}\}” and are questions of generative sufficiency, rather than related to why a behavior was produced. More generally, a lot of work uses multi-agent LLM simulations to probe the capabilities of LLMs themselves, such as their capacity for cooperation or their inherent biases. The goal of these simulations is to characterize the LLM agents’ capabilities, not to necessarily explain a specific real-world social dynamic. In the survey of recent generative ABM literature by Larooij et al. (45), we see that many projects use believability as their primary evaluation metric in this way, which we argue is an assessment of generative sufficiency rather than explanatory power.

The existence of a level 1 bucket also helps to flag if an LLM-based simulation is ‘cheating’. It is entirely feasible to produce LLM agents that return the outputs which produce TT through the manipulation of prompts. The behaviors of agents can be heavily influenced by prompt engineering; an engineered prompt that produces a desired behavior is perfectly acceptable for a level 1 phenomenal model. However, if an explanatory claim is being made, it can become important to clarify in the model’s intent II whether the prompt is an ‘artifact’ that forces the correct output, or an intentional abstraction of a real-world mechanism. Without this clarification, a model may be phenomenally ambiguous.

##### 3.2.1. Example

Following our social media model example, at Level 1, the researchers tweak the simulation to produce recognizable polarization patterns, operationalized as some clustering of sentiment scores over time (TT). They audit the simulation and report that the LLM agents produce polarized discourse that human annotators rate as believable.

At this stage, the simulation can serve two purposes. First, it demonstrates that polarization can emerge from LLM agents interacting on a simulated platform. Secondly, it could be used to forecast polarization on platforms with similar features. Given these agents on this network structure, polarization reliably emerges, and we might expect it to do so again under similar conditions.

However, the polarization could be driven by the agents’ prompts, the network topology, the recommendation algorithm, or some interaction among them. Therefore the model does not serve to identify causal responsibilities behind the phenomenon.

#### 3.3. Level 2

Simulations with a plausibility of level 2 move beyond reproducing TT to proposing a hypothesis for how it could possibly be generated. This is achieved when modeler specifies their Intent II, which includes a hypothesis and mapping (sometimes called a ‘model key’ (32)) that connects the components and activities in SS to the proposed mechanisms responsible for generating TT. By doing this, one states a hypothesis about how the possible mechanisms of TT are related to the simulation code. Earlier, we discussed and summarized this into Kaplan and Craver’s 3M requirement (41) in Section 2.3.

Modeling literature often refers to these post-phenomenal simulations as ‘how-possibly’ simulations (71; 32; 11) or ‘logical possibilities’ (5). One distinguishment of level 2 from level 1 simulations is that they provide a basis for reasoning about counterfactual scenarios, given a hypothesis about TT’s mechanisms encoded through II. For example, one could reason about how TT might change if those mechanisms were different.

Later on in Level 3, when one tries to validate a model, II is what determines if the simulation behavior is right or wrong. It is worth being precise about what the mapping in II involves epistemically; As discussed in Section 2.1, we distinguish between a model’s computations and the interpretation the modeler assigns to it (22; 84). The mapping is an interpretation that proposes how certain computational components of SS can be understood as standing in for certain real-world entities and activities. This means that two modelers could look at the same simulation SS and target TT and propose different mappings in II.

To tie this to LLM-ABM, suppose an agent is initialized through persona prompts or steering vectors (14) describing a specific profile; we can imagine the mapping in II interpreting the LLM’s outputs as reflecting the behavioral patterns of a ‘person’ matching that profile. Considering the LLM’s “theory proper” is autoregressive text prediction conditioned on a token sequence, which bears questionable structural resemblance to the cognitive processes of the described persona, we need the mapping to state: the modeler is assuming that the LLM’s training data encodes the relevant distributions about human behavior. Whether this assumption holds for a given TT is an empirical question that is scoped to each particular domain. As this is a developing field, discerning when this assumption is reasonable is an open problem that would benefit from community discussion.

##### 3.3.1. Example

At Level 2, our example researchers propose a hypothesis and mapping II: that polarization emerges in their simulation because agents engage with content that aligns with their initialized viewpoints, and the simulated feed algorithm amplifies this by surfacing high-engagement content. As part of the mapping, the researchers propose that the LLM agents stand in for real users on the social media platform, as the affordances made on the simulated platform (posting, replying, sharing, and receiving algorithmically ranked content) mirror the same that are available to real users. With this, future interventional questions become answerable relative to the hypothesis. For instance, “what happens if we ablate on the recommendation algorithm?” is now a meaningful experiment to add to evidence EE, because the modeler has specified components they believe to be causally responsible, and exposes the hypothesis and its details to falsification.

Level |
SS |
TT |
II |
EE |

0 |
✓ |
∅\varnothing |
∅\varnothing |
∅\varnothing |

1 |
✓ |
✓ |
∅\varnothing |
∅\varnothing |

2 |
✓ |
✓ |
✓ |
∅\varnothing |

3 |
✓ |
✓ |
✓ |
✓ |

Table 1. Plausibility levels and their relationship to the existence/falsifiability of a model’s components.

#### 3.4. Level 3

A simulation with plausibility level 3 attempts to ground its components in evidence EE, which is used to support or constrain the model’s construction, parameterization, or validation. Since the addition of each previous term in S,T,IS,T,I is what makes them falsifiable, this evidence could inform the design of the simulation SS, the operationalization of the target TT, or the justification for the mapping in II. EE could also come in the form of further constrained experiments, for example, ablations or sensitivity analyses that reinforce the prescribed hypotheses contained in the mapping. A modeler might select initial parameters based off of some observed values from census data, survey results, or prior empirical studies. For example, initializing an agent’s political beliefs based on real-world polling data from a specific region might constitute a piece of evidence EE.

Prior work suggests that how-possibly and how-actually explanations may exist on a continuum rather than as a strict dichotomy (12). Metaphorically, as more evidence is gathered for the conditions postulated in an explanation, the explanation moves along the continuum until it is counted as how-actually. Adopting this viewpoint to our scale, Level 3 can be thought of not as a binary threshold like levels 0 through 2, but a gradient progressing further as the quality, quantity, and directness of that evidence increases towards an unreachable Ω\Omega. We return to the question of why evidence can only asymptotically approach a definitive confirmation in Section 3.5.

In our discussion in Section 5, we elaborate on the confusion creators of LLM-based social simulations face in gathering relevant evidence EE, particularly when much of the research effort is focused on validating the agent’s internal architecture rather than the emergent social phenomenon.

##### 3.4.1. Example

Continuing the social media polarization example, at Level 3 the researchers ground the simulation by presenting varying evidence EE. They show how agent viewpoint distributions are initialized from real survey data on political attitudes in a specific region and the recommendation algorithm mirrors a documented platform’s ranking function. They run ablation studies showing that reducing the algorithmic amplification component significantly reduces polarization, consistent with prior empirical findings. Whether this evidence is appropriate is a judgment for the standards of their research domain. The model becomes more plausible as more of its components are supported, but the question of “plausible enough” is not one the scale answers, just makes explicit.

Figure 2. The Plausibility scale classifies models based on their epistemic contribution. Level Ω\Omega is considered the unreachable simulation that we can approach along level 3 continuously.

#### 3.5. Interpreting the Plausibility Scale

Given these levels in their increasing order, it is not to say that simulations of a lower plausibility level are worse. It is of general agreement among scientists and philosophers that idealizations are useful, if not, necessary in building models (63; 8; 23). Our scale clarifies the kind of epistemic contribution each simulation can provide.
Some simulations demonstrate that a pattern can be generated, others propose and test explanations for how it can arise. Morgan and Morrison aptly describe that models can function as partially autonomous instruments that mediate between theory and data without being fully derived from either (59); they can serve as tools for exploration even when they are known to be incomplete or idealized.
For example, level 0 simulations like cellular automata can demonstrate that emergent behavior can arise from simple rules, which sets the ground for new simulation paradigms. Level 2 simulations can be used to generate “how-possibly” hypotheses which are falsifiable at the mechanisms level.

What increases as we move up the scale is the number of commitments the model has made that can, in principle, be shown to be wrong, and scope of the claims it can support. At Level 1, only the reproduction of TT is at stake. At Level 2, the mapping II becomes an additional falsifiable commitment. At Level 3, the empirical grounding EE opens further points of potential failure. In addition, the confidence that the operationalized components of SS faithfully capture the abstract constructs and hypotheses the modeler intends them to represent, becomes increasingly examinable as more of the model’s structure is made explicit and subject to evidence. We file all of this under the umbrella term of ‘plausibility’.

It is also of note that each term in M=(S,T,I,E)M=(S,T,I,E) is sequentially dependent on the previous terms for moving up plausibility levels. Consider a counterexample where a simulation SS only has component EE. If there is no TT and II, the pair of SS and EE stands as a pairing of simulation outputs and arbitrary ‘facts’, with no clear mapping between them. Thus, TT and II are necessary relational structures that, when composed in sequence as (S,T,I,E)(S,T,I,E), turn sets of unrelated facts into points of evidence which support a hypothesis. This is also why Table 1 can be helpful, as it shows each level depends on the inclusion of all previous terms.

##### 3.5.1. The unreachable Ω\Omega simulation

Finally, we describe the theoretical unreachable model where every mechanism for a target phenomenon is described and leaves no doubt as to whether SS is a faithful representation of TT. In the mechanist’s view, to fully describe the mechanisms of a phenomenon is to explain it. We refer to this as a Level Ω\Omega simulation and note that it is a fiction we may never reach. As Brandon (12) argues, how-possibly explanations can be thought of as a continuum toward how-actually, as more evidence is accumulated for their postulated conditions. In our scale, Level Ω\Omega (see Figure 2) represents the (fictional) endpoint of this continuum where all postulated conditions are fully confirmed and we are sure that the mechanisms in SS are the mechanisms responsible for producing TT in actuality. However, Bokulich (11) suggests that as evidence confirms a mechanism at one level of abstraction, attempts to specify that mechanism open new branches of how-possibly explanation, each requiring their own evidence. Following this, the approach toward Ω\Omega may be better thought of as a “branching” process in which settling one question reveals further open ones that are implicitly abstracted away when unanswered.

Moreover, a related limitation arises from the more general relationship between evidence and theory. The Duhem-Quine thesis, loosely, holds that hypotheses are never tested in isolation, therefore the unambiguous falsification of a scientific hypothesis is impossible (21; 68). Another reason why we can never reach the Ω\Omega Level is that when a model is tested against empirical observations, a failure (or success) cannot unambiguously be attributed to particular components.

It is important to characterize the Ω\Omega level both because of the inevitable idealizations introduced into models, and because it makes explicit that one cannot confirm that a simulation has fully described the mechanisms behind a phenomenon.

### 4. The Mechanism Plausibility Scale Heuristic

We draw on existing frameworks for reporting on machine learning datasets and model deployments (29; 58; 86) and present a checklist for using the Mechanism Plausibility Scale. While hypothesis testing and operationalization are long-standing, established problems in science, the novelty of LLM-ABMs may lead researchers to struggle with putting out artifacts that are epistemically cohesive, where the target phenomenon, claims, and supporting evidence are aligned and appropriately scoped to one another. In Figure 3 we present the heuristic and in Appendix A we follow examples using historical ABMs, one for each level in the scale.

Figure 3. The Mechanism Plausibility Scale in checklist form.

### 5. Discussion

In the following section we review some popular ways LLMs are currently being used in simulation. Later in 5.3, we engage with broader ethical and epistemic considerations for using LLM in simulation. In Section 5.4, we go over historical examples and issues where the underspecification of models may have caused real-world harms.

#### 5.1. Reflections on the State of LLM Social Simulation

“How can we use LLM social simulation practically?” Given that no simulation can fully exhaust the mechanisms behind a phenomenon (as discussed in Section 3.5) this question is best interpreted as, “Under what conditions are LLM-ABMs adequate for a given purpose?”

The current state of affairs for LLM social simulation have a focus on demonstrating a simulation is capable of producing a target phenomenon. On the surface, the addition of LLMs in social simulation seemed to move us further up the “generative sufficiency scale”, allowing agents to access a larger action space, which prompted new work in the area. This focus on generative sufficiency is reflected in the systematic review by Larooij et al., where 22 out of 35 surveyed LLM social simulation papers used ‘believability’ as their primary validation metric (45). Here, the believability of an agent action or simulation outcome is judged by humans or LLMs (experimentally as part of a study, or simply by inspection). A simulation validated only through believability (Level 1) may be adequate for demonstrating that a phenomenon can be generated, or for exploratory purposes such as brainstorming and prototyping. However, if a modeler wishes to test what would happen under conditions that have not been observed – for example, how a policy intervention might alter the dynamics of TT – they are implicitly making a claim about which components of SS are causally responsible for TT. This is a mechanistic claim, whether or not the modeler frames it as such.

The field of machine learning revolves around learning unknown functions or distributions from real-world observed examples. The primary goal for many papers may be predictive accuracy, and the model’s internal workings are often considered a separate topic from empirical evaluations. This is no problem if prediction is the goal. However, there are a couple of caveats with LLM social simulation: many LLM-ABM projects use the evaluation of a functioning/believable LLM agent’s generative sufficiency to justify the usefulness of their simulation in exploring unknown scenarios, where plausible mechanisms instead would be the relevant factor for producing relevant counterfactuals.

We observe that LLM-based simulation is prone to conflation of agent-level validation for ABM/simulation-level validation. What do we mean by this? From the agent-based modeling perspective, a functioning agent is a presupposed mechanism – they are generally not the target phenomena of interest. An agent’s behaviors would have been manually programmed in classic agent-based models, and a non-functioning agent would have meant that the programmer made a bug. In our own attempts to review ABM papers that employ LLM-driven agents, we found that works tended to focus heavily on justifying their design of LLM-driven agents; this makes sense given that LLM-driven agents are a relatively new simulation technique. However, just as the validity of an intentional gloss is not guaranteed by the theory proper (Section 2.1), evidence supporting the functionality of the agent architecture (e.g., showing the agent can remember facts) is not sufficient as evidence EE for the mapping II concerning a higher-level social phenomenon TT. A functioning agent is a necessary part of the simulation SS, but its functionality alone does not validate the model’s explanation of TT. To distinguish agent-level and simulation-level mechanisms, we refer to the visual metaphor in Figure 1, which is a modified Craver diagram (18) showing how the overall phenomena TT is produced by agents {x1,…,xm}\{x_{1},\ldots,x_{m}\} and activities {ϕ1,…,ϕn}\{\phi_{1},\ldots,\phi_{n}\}.

An open question is how current LLM simulations can be made useful for policy or sociological settings given the discussed limitations so far. While we do not attempt to answer this fully, recent work suggests that practitioners already reason about simulations in ways that align with the distinctions in our scale.
Li et al. ran a year-long human co-design of simulations with their university’s emergency preparedness team from 2024-2025 (49). The policymakers seemed to show skepticism towards any models’ predictive abilities, even if the agents exhibited believable behavior. Instead, the simulations seemed to help them more as a brainstorming tool. For example, when a simulation’s dynamics were identified to be wrong, it resurfaced the policymakers’ tacit knowledge and allowed them to list out important concerns, for example, wheelchair ramps in evacuation settings. This has echoes in work done by Park et al. (62), where ‘false’ simulated social media platforms helped designers identify and prototype solutions to potential problems before they came up in a real deployed setting. The preparedness team began to trust the simulations more once the simulations started to align with real-world scenarios, when the authors tested it against their institution’s real-world graduation commencement setting. Once the policymakers saw that the simulations generated behavior that matched outcomes based on their experience and intuition, they were willing to entertain the ‘how-possibly’ outcomes generated by the simulation’s higher-level, abstracted mechanisms.

#### 5.2. Proprietary LLM APIs and Reproducibility

LLM API services have been known to introduce prompt injections, guardrails, or system prompts invisible to the end user. These features are added for safety, regulation, or other proprietary purposes but can be actively detrimental to experimental validity. For example, hidden prompts could unknowingly change the trajectory of an agent’s behavior or prevent agents from exhibiting relevant behavior the modeler is interested in. Furthermore, proprietary LLMs are often subject to unannounced version or system prompt11
1

See https://github.com/asgeirtj/system_prompts_leaks and similar for in-the-wild examples. updates, which could alter agent behavior between runs. This problem is solvable with open-sourced locally hosted models, but raises the barrier to entry for many researchers because of things like GPU and technical constraints.

Concerning ethical considerations of proprietary models, LLM training data is frequently assembled through practices that fall below disciplinary ethical standards, for example, mass scraping without consent, labor practices involving underpaid workers, the inclusion of private data, and environmental harms (34; 81). On the methodological and epistemic side, closed-process (training sources and methods, weights) models compromise the community’s ability to inspect training data, attribute model behavior to appropriate sources, and have rigorous control over their scientific methodology.

There are growing movements toward addressing these concerns. Initiatives such as AI2’s OLMo project (33) have demonstrated that competitive language models can be developed with fully open training data, code, and intermediate checkpoints, with the goal of enabling the scientific study of language models. The Public AI Network advocates for treating AI as public infrastructure – publicly accessible, accountable, and designed to produce permanent public goods (38). However, at the time of writing, proprietary models continue to dominate both commercial deployment and research usage.

#### 5.3. Broader Ethical and Epistemic Concerns

The problems related to reproducibility, proprietary APIs, and the conflation of generative sufficiency with mechanistic plausibility are largely methodological. However, there are broader ethical and epistemic concerns about the use of LLMs in social simulation that warrant consideration.

Regarding whether LLMs should serve as proxies for human subjects in the first place, Agnew et al. (1) examine proposals to substitute human research participants with LLM surrogates and find that such proposals conflict with values relating to representation, inclusion, and understanding of human subjects. Replacing participants with LLMs may disregard the relationship between researcher and subject existing in prior human subject research. When an LLM generates text that resembles survey responses or social behavior, it is not directly from the experience of a live, present individual. Furthermore, they identify the problem of “value lock-in”, also referenced by Weidinger et al. (82). LLMs encode the norms and attitudes present in their training data at a particular point in time. Related empirical work supports this; language models exhibit degraded performance in time periods not represented in their training corpus (46).

#### 5.4. Historical Issues and Harms of Poor ABM specification

While the Mechanism Plausibility Scale was motivated by recent challenges posed by LLM-ABM, the ideas are not specific to ABMs with LLMs; The literature surrounding well-motivated, sound ABM design in general is a long-standing discussion (75; 73; 6; 60; 45; 77). Importantly, we demonstrate how understanding a model’s limits is not only important to the modeler herself, but also to its end users.

Squazzoni et al. (73) note that during the COVID-19 pandemic, a team at the Imperial College of London reported that results from their model projected “a huge number of people would die in Britain unless severe policy measures were taken”. The results of their model and interventions were quickly adopted and implemented by the UK government, and advised governments of countries like the US and France in their attempts to minimize the damages caused by the virus. However, because of underspecification on what the model was adequate for, the model erroneously affected the policies of many countries, namely, being used in counterfactual scenarios when further peer analysis of the model showed it may only have been adequate for illustrative purposes. Moreover, the simulation code was not made public, even later at the time of Squazzoni et al.’s publication.

Axelrod’s iterated Prisoner’s Dilemma (PD) simulations are another well-known problematic case. In an adapted script on “The Evolution of Cooperation” (7), Axelrod asserts that many real-world scenarios such as arms races, nuclear proliferation, and crisis bargaining are instances of the iterated Prisoner’s Dilemma, and that advice to players of the game theoretic scenario might serve as advice to national leaders. In response, Northcott and Alexandrova (60) observe that despite the enormous attention devoted to the PD (over 16,000 articles since 1960), it has largely failed to explain phenomena of social scientific interest.

Arnold (sharply) observes a broader pattern in the modeling tradition (6): over thirty years of Repeated PD simulations produced practically no successful empirical applications, yet this failure has been largely ignored. He identifies, firstly, the “justificatory narratives” modelers use after scrutiny, which is retreating to claims that the model is merely heuristic or exploratory without specifying the limits of that exploration. Secondly, modelers arguing that all models rely on simplification, a defense that, as Arnold notes, only holds when the causal factors a model isolates are empirically discernible from the other factors at work in the target system. When they are not, the simplification cannot be tested.

We felt it appropriate to reiterate these issues under our scale and point to related work, especially with the growing interest in simulation using LLMs.

### 6. Conclusion and Limitations

In this paper we connect contemporary mechanisms, cognitive representation, and other philosophy of science literature with agent-based modeling and LLM social simulation. We present the Mechanism Plausibility Scale, a heuristic that classifies simulations into levels based on the falsifiability and existence of components S,T,I,ES,T,I,E and offer a practical checklist. Through a review of recent LLM-ABM papers we confirm the existence of common category errors between Agent-level and ABM-level components and underspecified models. We also connect these problems with existing issues in ABM and highlight the historical harms that occurred when these mistakes happened in high-stakes scenarios.
While our scale provides a useful heuristic, the criteria for Level 3 could be refined to differentiate the quality and extent of evidence EE for a more practical setting. Additionally, more could be said about a separate axis for predictive models, as opposed to our plausible explanation axis. The main focus of the paper, ultimately, remains grounding multiple disciplines in common language and bringing these issues to attention.

### Generative AI Usage Statement

This document was produced with the assistance of Generative AI, which assisted in the formatting of tables, checklists, figures, proofreading, and typographical layout of the paper. It was also used to generate critique; the authors also used AI-augmented paper search engines, such as Asta22
2

https://asta.allen.ai/chat, for paper discovery.

### References

- Agnew et al. (2024)
W. Agnew, A. S. Bergman, J. Chien, M. Díaz, S. El-Sayed, J. Pittman, S. Mohamed, and K. R. McKee

The illusion of artificial inclusion.

In Proceedings of the CHI Conference on Human Factors in Computing Systems,

pp. 1–12.

Note: arXiv:2401.08572 [cs]Comment: Proceedings of the CHI Conference on Human Factors in Computing Systems (CHI 2024)

External Links: Link,
Document

Cited by: §1,
§5.3.

- Akata et al. (2025)
E. Akata, L. Schulz, J. Coda-Forno, S. J. Oh, M. Bethge, and E. Schulz

Playing repeated games with Large Language Models.

Nature Human Behaviour.

Note: arXiv:2305.16867 [cs]

External Links: ISSN 2397-3374,
Link,
Document

Cited by: §3.2.

- AL et al. (2024)
A. AL, A. Ahn, N. Becker, S. Carroll, N. Christie, M. Cortes, A. Demirci, M. Du, F. Li, S. Luo, P. Y. Wang, M. Willows, F. Yang, and G. R. Yang

Project Sid: Many-agent simulations toward AI civilization.

arXiv.

Note: arXiv:2411.00114 [cs]Comment: 35 pages, 14 figures

External Links: Link,
Document

Cited by: Table 2,
Table 3.

- Anthis et al. (2025)
J. R. Anthis, R. Liu, S. M. Richardson, A. C. Kozlowski, B. Koch, J. Evans, E. Brynjolfsson, and M. Bernstein

LLM Social Simulations Are a Promising Research Method.

arXiv.

Note: arXiv:2504.02234 [cs]

External Links: Link,
Document

Cited by: §1.

- Arnold (2013)
E. Arnold

Simulation Models of the Evolution of Cooperation as Proofs of Logical Possibilities. How Useful Are They?.

Etica E Politica 15 (2), pp. 101–138.

Note: Publisher: University of Trieste, Department of PhilosophyI believe that there are (at least) three different cases where the proof of logical possibilities can indeed provide an important piece in the puzzle of scientific research:
1. Novel Discovery. When it reveals a phenomenon that was formerly unknown and unexpected or believed to be impossible.
2. Best Explanation. When the explanation of some phenomenon merely hinges on the proof that a particular mechanism can produce a given result. This can become important in the context of an inference to the best explanation.
3. Real Possibility. If the proven logical possibility is also a real possibility and if the modeled mechanism can be identified empirically. Any one of these conditions suffices to render a theoretical model epistemically useful. I am now going to describe the three cases in more detail and one by one.… under what circumstances the proof of logical possibilities via computer simulations may provide valuable insights. I describe three sets of circumstances under which this may be the case:
1. If the logical possibility demonstrates something that in virtue of our prior beliefs and background knowledge is highly surprising or totally unexpected to us, or which we would not even have considered possible at all. I call this the novel discovery condition.
2. If the logical possibility is a key element in a best explanation of some phenomenon. This is the case, if the explanation of some phenomenon merely hinges on the question whether the phenomenon can be produced by a particular mechanism and if this can be demonstrated by a simulation. This can be called the best explanation condition.
3. If the logical possibility is also a real possibility (the difference between logically possible and really possible will be explained later) that can at least in principle be identified in some particular empirical setting then, again, it is useful to know this possibility. I call this the real possibility condition.

External Links: Link

Cited by: §3.3.

- Arnold (2015)
E. Arnold

How Models Fail: A Critical Look at the History of Computer Simulations of the Evolution of Cooperation.

In Collective Agency and Cooperation in Natural and Artificial Systems, C. Misselhorn (Ed.),

pp. 261–279 (en).

External Links: ISBN 978-3-319-15514-2 978-3-319-15515-9,
Link,
Document

Cited by: §5.4,
§5.4.

- [7]
R. Axelrod

The Evolution of Cooperation*.

(en).

External Links: Link

Cited by: §5.4.

- Aydinonat (2024)
N. E. Aydinonat

The puzzle of model-based explanation.

In The Routledge Handbook of Philosophy of Scientific Modeling,

pp. 177–192 (en).

External Links: ISBN 978-1-003-20564-7,
Link,
Document

Cited by: §1,
§3.5.

- Bartha (2024)
P. Bartha

Analogy and Analogical Reasoning.

In The Stanford Encyclopedia of Philosophy, E. N. Zalta and U. Nodelman (Eds.),

External Links: Link

Cited by: §2.5.

- Bogen and Woodward (1988)
J. Bogen and J. Woodward

Saving the Phenomena.

The Philosophical Review 97 (3), pp. 303–352.

External Links: 2185445,
ISSN 0031-8108,
Document

Cited by: §2.1.

- Bokulich (2014)
A. Bokulich

How the Tiger Bush Got its Stripes: ‘How Possibly’ vs. ‘How Actually’ Model Explanations.

The Monist 97 (3), pp. 321–338.

External Links: ISSN 0026-9662,
Link,
Document

Cited by: §3.3,
§3.5.1.

- Brandon and Brandon (2014)
R. N. Brandon and R. N. Brandon

Adaptation and environment.

Princeton University Press, Princeton.

External Links: ISBN 978-1-4008-6066-1,
Link,
Document

Cited by: §3.4,
§3.5.1.

- Bridgman (1927)
P. W. (. W. Bridgman

The logic of modern physics.

The Macmillan Company.

External Links: LCCN EBook-No. 70620

Cited by: §2.1.

- Chen et al. (2025)
R. Chen, A. Arditi, H. Sleight, O. Evans, and J. Lindsey

Persona Vectors: Monitoring and Controlling Character Traits in Language Models.

arXiv.

Note: arXiv:2507.21509 [cs]

External Links: Link,
Document

Cited by: §3.3.

- Chen et al. (2023)
W. Chen, Y. Su, J. Zuo, C. Yang, C. Yuan, C. Chan, H. Yu, Y. Lu, Y. Hung, C. Qian, Y. Qin, X. Cong, R. Xie, Z. Liu, M. Sun, and J. Zhou

AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors.

arXiv.

Note: arXiv:2308.10848 [cs]Comment: Under review. Code at https://github.com/OpenBMB/AgentVerse/

External Links: Link,
Document

Cited by: Table 2,
Table 3.

- Costarelli et al. (2024)
A. Costarelli, M. Allen, R. Hauksson, G. Sodunke, S. Hariharan, C. Cheng, W. Li, and A. Yadav

GameBench: Evaluating Strategic Reasoning Abilities of LLM Agents.

arXiv.

Note: arXiv:2406.06613 [cs]
version: 1

External Links: Link,
Document

Cited by: §3.2.

- Craver (2006)
C. F. Craver

When mechanistic models explain.

Synthese 153 (3), pp. 355–376 (en).

External Links: ISSN 1573-0964,
Link,
Document

Cited by: §2.3,
§3.2,
§3.

- Craver (2009)
C. F. Craver

Explaining the Brain.

Oxford University Press.

Cited by: Figure 1,
§2.3,
§5.1.

- Craver et al. (2024)
C. Craver, J. Tabery, and P. Illari

Mechanisms in Science.

In The Stanford Encyclopedia of Philosophy, E. N. Zalta and U. Nodelman (Eds.),

External Links: Link

Cited by: Figure 4,
§1,
§2.3,
§2.3,
§3.1,
§3.2.

- Cronbach and Meehl (1955)
L. J. Cronbach and P. E. Meehl

Construct validity in psychological tests.

Psychological Bulletin 52 (4), pp. 281–302.

Note: Place: US
Publisher: American Psychological Association

External Links: ISSN 1939-1455,
Document

Cited by: §2.1,
§2.1.

- Duhem (1954)
P. M. M. Duhem

The aim and structure of physical theory.

Vol. 1, Princeton University Press.

Note: Pages: 85-87

Cited by: §3.5.1.

- Egan (2025)
F. Egan

Deflating Mental Representation (The Jean Nicod Lectures).

MIT Press (open access).

Cited by: §2.1,
§3.3.

- Elgin (2004)
C. Z. Elgin

True Enough.

Philosophical Issues 14, pp. 113–131.

Note: Publisher: [Wiley, Ridgeview Publishing Company]

External Links: ISSN 1533-6077,
Link

Cited by: §1,
§3.5.

- Epstein (2006)
J. M. Epstein

Generative Social Science: Studies in Agent-Based Computational Modeling.

STU - Student edition edition, Princeton University Press.

External Links: ISBN 978-0-691-12547-3,
Link

Cited by: Figure 7,
§1.

- Fisher (1999)
R. A. Fisher

The genetical theory of natural selection: by R.A. Fisher ; edited with a foreword and notes by J.H. Bennett.

A complete variorum ed edition, Oxford University Press, Oxford.

External Links: ISBN 978-0-19-850440-5

Cited by: §C.1.

- G.Carmines and A.Zeller (1979)
E. G.Carmines and R. A.Zeller

Reliability and Validity Assessment.

SAGE Publications, Inc..

External Links: Document,
ISBN 978-1-4129-8564-2

Cited by: §2.1.

- Gao et al. (2025)
C. Gao, X. Lan, Z. Lu, J. Mao, J. Piao, H. Wang, D. Jin, and Y. LiS$^3$: Social-network Simulation System with Large Language Model-Empowered Agents(Website)

External Links: 2307.14984,
Document,
Link

Cited by: 1st item,
Table 2,
Table 3,
§2.2.

- Gardner (1970)
M. Gardner

Mathematical Games.

Scientific American 223 (4), pp. 120–123.

Note: Publisher: Scientific American, a division of Nature America, Inc.

External Links: ISSN 0036-8733,
Link

Cited by: Figure 4,
Figure 4.

- Gebru et al. (2021)
T. Gebru, J. Morgenstern, B. Vecchione, J. W. Vaughan, H. Wallach, H. D. III, and K. Crawford

Datasheets for Datasets.

arXiv.

Note: arXiv:1803.09010 [cs]Comment: Published in CACM in December, 2021

External Links: Link,
Document

Cited by: §1,
§4.

- Glennan (1996)
S. S. Glennan

Mechanisms and the nature of causation.

Erkenntnis 44 (1), pp. 49–71 (en).

External Links: ISSN 1572-8420,
Link,
Document

Cited by: Figure 4,
§2.3,
§3.1.

- Glennan (2017)
S. Glennan

The New Mechanical Philosophy.

Oxford University Press, Oxford.

Cited by: §2.3,
§2.3.

- Graebner (2018)
C. Graebner

How to Relate Models to Reality? An Epistemological Framework for the Validation and Verification of Computational Models.

Journal of Artificial Societies and Social Simulation 21 (3), pp. 8.

External Links: ISSN 1460-7425

Cited by: §C.1,
§2.1,
§2.2,
§3.3,
§3.3.

- Groeneveld et al. (2024)
D. Groeneveld, I. Beltagy, P. Walsh, A. Bhagia, R. Kinney, O. Tafjord, A. H. Jha, H. Ivison, I. Magnusson, Y. Wang, S. Arora, D. Atkinson, R. Authur, K. R. Chandu, A. Cohan, J. Dumas, Y. Elazar, Y. Gu, J. Hessel, T. Khot, W. Merrill, J. Morrison, N. Muennighoff, A. Naik, C. Nam, M. E. Peters, V. Pyatkin, A. Ravichander, D. Schwenk, S. Shah, W. Smith, E. Strubell, N. Subramani, M. Wortsman, P. Dasigi, N. Lambert, K. Richardson, L. Zettlemoyer, J. Dodge, K. Lo, L. Soldaini, N. A. Smith, and H. Hajishirzi

OLMo: Accelerating the Science of Language Models.

arXiv.

Note: arXiv:2402.00838 [cs]

External Links: Link,
Document

Cited by: §5.2.

- Guest and van Rooij (2025)
O. Guest and I. van Rooij

Critical Artificial Intelligence Literacy for Psychologists.

PsyArXiv.

External Links: Link,
Document

Cited by: §5.2.

- Guo (2023)
F. Guo

GPT in Game Theory Experiments.

arXiv.

Note: arXiv:2305.05516 [econ]Comment: updated to use GPT-4 instead of GPT-3.5 and added reasoning analysis

External Links: Link,
Document

Cited by: §3.2.

- Horton (2023)
J. J. Horton

Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus?.

arXiv.

Note: arXiv:2301.07543 [econ]

External Links: Link,
Document

Cited by: §1.

- Hua et al. (2024)
W. Hua, L. Fan, L. Li, K. Mei, J. Ji, Y. Ge, L. Hemphill, and Y. Zhang

War and Peace (WarAgent): Large Language Model-based Multi-Agent Simulation of World Wars.

arXiv.

Note: arXiv:2311.17227 [cs]Comment: 47 pages, 9 figures, 5 tables

External Links: Link,
Document

Cited by: Table 2,
Table 3,
§2.2.

- Jackson et al. (2024)
B. Jackson, B. Cavello, F. Devine, N. Garcia, S. J. Klein, A. Krasodomski, J. Tan, and E. Tursman

Public AI: Infrastructure for the common good.

Public AI Network.

External Links: Link,
Document

Cited by: §5.2.

- Jackson (1982)
F. Jackson

Epiphenomenal Qualia.

The Philosophical Quarterly 32 (127), pp. 127–136.

External Links: ISSN 0031-8094,
Document

Cited by: §2.1.

- Kaiya et al. (2023)
Z. Kaiya, M. Naim, J. Kondic, M. Cortes, J. Ge, S. Luo, G. R. Yang, and A. Ahn

Lyfe Agents: Generative agents for low-cost real-time social interactions.

arXiv.

External Links: 2310.02172,
Document

Cited by: Table 2,
Table 3,
§2.2.

- Kaplan and Craver (2011)
D. M. Kaplan and C. F. Craver

The Explanatory Force of Dynamical and Mathematical Models in Neuroscience: A Mechanistic Perspective*.

Philosophy of Science 78 (4), pp. 601–627.

Note: Publisher: [The University of Chicago Press, Philosophy of Science Association]

External Links: ISSN 0031-8248,
Link,
Document

Cited by: §2.3,
§3.3,
§3.

- Kay (2018)
K. N. Kay

Principles for models of neural information processing.

NeuroImage 180, pp. 101–109.

External Links: ISSN 1053-8119,
Link,
Document

Cited by: §1,
§2.2.

- Kempinski et al. (2025)
B. Kempinski, I. Gemp, K. Larson, M. Lanctot, Y. Bachrach, and T. Kachman

Game of Thoughts: Iterative Reasoning in Game-Theoretic Domains with Large Language Models.

In Proceedings of the 24th International Conference on Autonomous Agents and Multiagent Systems,

AAMAS ’25, Richland, SC, pp. 1088–1097.

External Links: ISBN 979-8-4007-1426-9

Cited by: §3.2.

- Landis and Koch (1977)
J. R. Landis and G. G. Koch

The measurement of observer agreement for categorical data.

Biometrics 33 (1), pp. 159–174 (eng).

External Links: ISSN 0006-341X

Cited by: Table 4.

- Larooij and Törnberg (2025)
M. Larooij and P. Törnberg

Do Large Language Models Solve the Problems of Agent-Based Modeling? A Critical Review of Generative Social Simulations.

arXiv.

Note: arXiv:2504.03274 [cs]

External Links: Link,
Document

Cited by: §B.1,
§B.2.1,
§B.4,
§1,
§3.2,
§5.1,
§5.4.

- Lazaridou et al. (2021)
A. Lazaridou, A. Kuncoro, E. Gribovskaya, D. Agrawal, A. Liska, T. Terzi, M. Gimenez, C. d. M. d’Autume, T. Kocisky, S. Ruder, D. Yogatama, K. Cao, S. Young, and P. Blunsom

Mind the Gap: Assessing Temporal Generalization in Neural Language Models.

arXiv.

Note: arXiv:2102.01951 [cs]Comment: To appear as a Spotlight at NeurIPS 2021

External Links: Link,
Document

Cited by: §5.3.

- Li et al. (2023)
H. Li, Y. Q. Chong, S. Stepputtis, J. Campbell, D. Hughes, M. Lewis, and K. Sycara

Theory of Mind for Multi-Agent Collaboration via Large Language Models.

In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing,

pp. 180–192.

Note: arXiv:2310.10701 [cs]Comment: Accepted to EMNLP 2023 (Main Conference). Code available at https://github.com/romanlee6/multi_LLM_comm

External Links: Link,
Document

Cited by: Table 2,
Table 3,
§2.2.

- Li et al. (2024)
X. Li, Y. Xu, Y. Zhang, and E. C. Malthouse

Large Language Model-driven Multi-Agent Simulation for News Diffusion Under Different Network Structures.

arXiv.

Note: arXiv:2410.13909 [cs]

External Links: Link,
Document

Cited by: 2nd item,
Table 2,
Table 3.

- Li et al. (2025)
Y. Li, S. Das, and H. Shirado

What Makes LLM Agent Simulations Useful for Policy? Insights From an Iterative Design Engagement in Emergency Preparedness.

arXiv.

Note: arXiv:2509.21868 [cs]

External Links: Link,
Document

Cited by: §1,
§5.1.

- Li and Shirado (2025)
Y. Li and H. Shirado

Spontaneous Giving and Calculated Greed in Language Models.

arXiv.

Note: arXiv:2502.17720 [cs]

External Links: Link,
Document

Cited by: §3.2.

- Liu et al. (2024)
Y. Liu, X. Chen, X. Zhang, X. Gao, J. Zhang, and R. Yan

From Skepticism to Acceptance: Simulating the Attitude Dynamics Toward Fake News.

In Proceedings of the Thirty-ThirdInternational Joint Conference on Artificial Intelligence,

pp. 7849–7857.

Note: arXiv:2403.09498 [cs]Comment: IJCAI 2024 Oral

External Links: Link,
Document

Cited by: 4th item,
Table 2,
Table 3.

- MacCorquodale and Meehl (1948)
K. MacCorquodale and P. E. Meehl

On a distinction between hypothetical constructs and intervening variables..

Psychological Review 55 (2), pp. 95–107.

External Links: ISSN 1939-1471, 0033-295X,
Document

Cited by: §2.1,
§2.1.

- Machamer et al. (2000)
P. Machamer, L. Darden, and C. F. Craver

Thinking about Mechanisms.

Philosophy of Science 67 (1), pp. 1–25.

Note: Publisher: [The University of Chicago Press, Philosophy of Science Association]

External Links: ISSN 0031-8248,
Link

Cited by: §1,
§2.3.

- Marzo et al. (2023)
G. D. Marzo, L. Pietronero, and D. Garcia

Emergence of Scale-Free Networks in Social Interactions among Large Language Models.

arXiv.

Note: arXiv:2312.06619 [physics]

External Links: Link,
Document

Cited by: Table 2,
Table 3.

- Massimi (2022)
M. Massimi

Perspectival Ontology: Between Situated Knowledge and Multiculturalism.

The Monist 105 (2), pp. 214–228.

External Links: ISSN 0026-9662, 2153-3601,
Document

Cited by: §2.1.

- Mauk (2000)
M. D. Mauk

The potential effectiveness of simulations versus phenomenological models.

Nature Neuroscience 3 (7), pp. 649–651 (en).

Note: Publisher: Nature Publishing Group

External Links: ISSN 1546-1726,
Link,
Document

Cited by: §1,
§2.2.

- McAllister (1997)
J. W. McAllister

Phenomena and Patterns in Data Sets.

Erkenntnis (1975-) 47 (2), pp. 217–228.

External Links: 20012798,
ISSN 0165-0106,
Document

Cited by: §2.1.

- Mitchell et al. (2019)
M. Mitchell, S. Wu, A. Zaldivar, P. Barnes, L. Vasserman, B. Hutchinson, E. Spitzer, I. D. Raji, and T. Gebru

Model Cards for Model Reporting.

In Proceedings of the Conference on Fairness, Accountability, and Transparency,

pp. 220–229.

Note: arXiv:1810.03993 [cs]

External Links: Link,
Document

Cited by: §1,
§4.

- M. S. Morgan and M. Morrison (Eds.) (1999)
M. S. Morgan and M. Morrison (Eds.)

Models as Mediators: Perspectives on Natural and Social Science.

Ideas in Context, Cambridge University Press, Cambridge.

External Links: ISBN 978-0-521-65097-7,
Link,
Document

Cited by: §3.5.

- Northcott and Alexandrova (2015)
R. Northcott and A. Alexandrova

Prisoner’s Dilemma Doesn’t Explain Much.

In The Prisoner?s Dilemma. Classic philosophical arguments., M. Peterson (Ed.),

pp. 64–84.

External Links: Link

Cited by: §5.4,
§5.4.

- Park et al. (2023)
J. S. Park, J. C. O’Brien, C. J. Cai, M. R. Morris, P. Liang, and M. S. Bernstein

Generative Agents: Interactive Simulacra of Human Behavior.

arXiv.

Note: arXiv:2304.03442 [cs]

External Links: Link,
Document

Cited by: Table 2,
Table 3,
§1,
§2.2.

- Park et al. (2022)
J. S. Park, L. Popowski, C. Cai, M. R. Morris, P. Liang, and M. S. Bernstein

Social Simulacra: Creating Populated Prototypes for Social Computing Systems.

Proceedings of the 35th Annual ACM Symposium on User Interface Software and Technology, pp. 1–18 (en).

Note: Conference Name: UIST ’22: The 35th Annual ACM Symposium on User Interface Software and Technology
ISBN: 9781450393201
Place: Bend OR USA
Publisher: ACM[TLDR] It is demonstrated that social simulacra shift the behaviors that they generate appropriately in response to design changes, and that they enable exploration of “what if?” scenarios where community members or moderators intervene.

External Links: Link,
Document

Cited by: Table 2,
Table 3,
§2.2,
§5.1.

- Parker (2020)
W. S. Parker

Model Evaluation: An Adequacy-for-Purpose View.

Philosophy of Science 87 (3), pp. 457–477 (en).

External Links: ISSN 0031-8248, 1539-767X,
Link,
Document

Cited by: §1,
§3.5.

- Paul et al. (2024)
D. Paul, R. West, A. Bosselut, and B. Faltings

Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning.

Note: Version Number: 4Other
Accepted at EMNLP Findings

External Links: Link,
Document

Cited by: §1.

- Pearl and Mackenzie (2018)
J. Pearl and D. Mackenzie

The book of why: The new science of cause and effect.

1 edition, Basic Books, Inc., USA.

External Links: ISBN 0-465-09760-X

Cited by: §2.4.

- Pearl (2009)
J. Pearl

Causality.

2 edition, Cambridge University Press, Cambridge.

External Links: ISBN 978-0-521-89560-6,
Link,
Document

Cited by: §2.4.

- Pichler and Reiter (2022)
A. Pichler and N. Reiter

From Concepts to Texts and Back: Operationalization as a Core Activity of Digital Humanities.

Journal of Cultural Analytics 7 (4) (en).

Note: [TLDR] It is argued that operationalization plays such a crucial role for the digital humanities that any kind of theory needs to take off from operationalization practices, and a first scheme of the constraints and necessities of such a theory is developed.

External Links: ISSN 2371-4549,
Link,
Document

Cited by: §2.1.

- Quine (1953)
W. V. O. Quine

From a Logical Point of View.

Harvard University Press, Cambridge.

Cited by: §3.5.1.

- Ren et al. (2024)
S. Ren, Z. Cui, R. Song, Z. Wang, and S. Hu

Emergence of Social Norms in Generative Agent Societies: Principles and Architecture.

arXiv.

Note: arXiv:2403.08251 [cs]Comment: Published as a conference paper at IJCAI 2024

External Links: Link,
Document

Cited by: §2.2.

- Schelling (1969)
T. C. Schelling

Models of Segregation.

The American Economic Review 59 (2), pp. 488–493.

Note: Publisher: American Economic Association

External Links: ISSN 0002-8282,
Link

Cited by: Figure 6,
§C.1.

- Šešelja (2023)
D. Šešelja

Agent-Based Modeling in the Philosophy of Science.

In The Stanford Encyclopedia of Philosophy, E. N. Zalta and U. Nodelman (Eds.),

External Links: Link

Cited by: §3.3.

- Shmueli (2010)
G. Shmueli

To Explain or to Predict?.

Statistical Science 25 (3) (en).

External Links: ISSN 0883-4237,
Link,
Document

Cited by: §2.4,
§2.4.

- Squazzoni et al. (2020)
F. Squazzoni, J. G. Polhill, B. Edmonds, P. Ahrweiler, P. Antosz, G. Scholz, E. Chappin, M. Borit, H. Verhagen, F. Giardini, and N. Gilbert

Computational Models That Matter During a Global Pandemic Outbreak: A Call to Action.

JASSS - The Journal of Artificial Societies and Social Simulation 23 (2).

External Links: ISSN 1460-7425,
Document

Cited by: §5.4,
§5.4.

- Stevens (1935)
S. S. Stevens

The operational definition of psychological concepts.

Psychological Review 42 (6), pp. 517–527.

External Links: ISSN 1939-1471,
Document

Cited by: §2.1.

- Swarup (2019)
S. Swarup

Adequacy: What Makes a Simulation Good Enough?.

In 2019 Spring Simulation Conference (SpringSim),

pp. 1–12.

External Links: Link,
Document

Cited by: §2.3,
§5.4.

- Titchener (1910)
E. B. Titchener

A text-book of psychology.

A Text-Book of Psychology, MacMillan Co, New York, NY, US.

External Links: Document

Cited by: §2.1.

- Vanhée et al. (2025)
L. Vanhée, M. Borit, P. Siebers, R. Cremades, C. Frantz, Ö. Gürcan, F. Kalvas, D. R. Kera, V. Nallur, K. Narasimhan, and M. Neumann

Large Language Models for Agent-Based Modelling: Current and possible uses across the modelling cycle.

arXiv.

Note: arXiv:2507.05723 [cs]
version: 1Comment: 18 pages, including 2 pages of appendix, accepted for publication at the Social Simulation Conference 2025 (https://ssc2025.tbm.tudelft.nl/)

External Links: Link,
Document

Cited by: §1,
§5.4.

- Vessonen (2021)
E. Vessonen

Conceptual engineering and operationalism in psychology.

Synthese 199 (3), pp. 10615–10637 (en).

External Links: ISSN 1573-0964,
Link,
Document

Cited by: §2.1.

- Wang et al. (2025)
L. Wang, J. Zhang, H. Yang, Z. Chen, J. Tang, Z. Zhang, X. Chen, Y. Lin, H. Sun, R. Song, X. Zhao, J. Xu, Z. Dou, J. Wang, and J. Wen

User Behavior Simulation with Large Language Model-based Agents.

ACM Trans. Inf. Syst. 43 (2), pp. 55:1–55:37.

External Links: ISSN 1046-8188,
Link,
Document

Cited by: §2.2.

- Wang et al. (2023)
Z. Wang, Y. Y. Chiu, and Y. C. Chiu

Humanoid Agents: Platform for Simulating Human-like Generative Agents.

arXiv (en).

Note: arXiv:2310.05418 [cs]Comment: Accepted at EMNLP System Demonstrations 2023

External Links: Link,
Document

Cited by: Table 2,
Table 3.

- Weidinger et al. (2021)
L. Weidinger, J. Mellor, M. Rauh, C. Griffin, J. Uesato, P. Huang, M. Cheng, M. Glaese, B. Balle, A. Kasirzadeh, Z. Kenton, S. Brown, W. Hawkins, T. Stepleton, C. Biles, A. Birhane, J. Haas, L. Rimell, L. A. Hendricks, W. Isaac, S. Legassick, G. Irving, and I. Gabriel

Ethical and social risks of harm from Language Models.

arXiv.

Note: arXiv:2112.04359 [cs]

External Links: Link,
Document

Cited by: §5.2.

- Weidinger et al. (2022)
L. Weidinger, J. Uesato, M. Rauh, C. Griffin, P. Huang, J. Mellor, A. Glaese, M. Cheng, B. Balle, A. Kasirzadeh, C. Biles, S. Brown, Z. Kenton, W. Hawkins, T. Stepleton, A. Birhane, L. A. Hendricks, L. Rimell, W. Isaac, J. Haas, S. Legassick, G. Irving, and I. Gabriel

Taxonomy of Risks posed by Language Models.

In 2022 ACM Conference on Fairness Accountability and Transparency,

Seoul Republic of Korea, pp. 214–229 (en).

External Links: ISBN 978-1-4503-9352-2,
Link,
Document

Cited by: §5.3.

- Weisberg (2007)
M. Weisberg

Who Is a Modeler?.

The British Journal for the Philosophy of Science 58 (2), pp. 207–233.

Note: Publisher: [Oxford University Press, The British Society for the Philosophy of Science]

External Links: ISSN 0007-0882,
Link

Cited by: §C.1,
§1.

- Weisberg (2013)
M. Weisberg

Simulation and Similarity: Using Models to Understand the World.

Oxford University Press.

Cited by: §C.1,
§2.1,
§3.3,
§3.

- Williams et al. (2023)
R. Williams, N. Hosseinichimeh, A. Majumdar, and N. Ghaffarzadegan

Epidemic Modeling with Generative Agents.

arXiv.

Note: arXiv:2307.04986 [cs]

External Links: Link,
Document

Cited by: Table 2,
Table 3.

- Winikoff et al. (2025)
M. Winikoff, J. Thangarajah, and S. Rodriguez

A Scoresheet for Explainable AI.

arXiv.

Note: arXiv:2502.09861 [cs]Comment: To appear at AAMAS 2025 - arXiv version also includes appendices

External Links: Link,
Document

Cited by: §1,
§4.

- Yona et al. (2024)
G. Yona, R. Aharoni, and M. Geva

Can Large Language Models Faithfully Express Their Intrinsic Uncertainty in Words?.

Note: Publisher: arXiv
Version Number: 2Other
To appear in EMNLP 2024 (main conference)

External Links: Link,
Document

Cited by: §1.

- Zhang et al. (2024a)
D. Zhang, Z. Li, P. Wang, X. Zhang, Y. Zhou, and X. Qiu

SpeechAgents: Human-Communication Simulation with Multi-Modal Multi-Agent Systems.

arXiv.

Note: arXiv:2401.03945 [cs]Comment: work in progress

External Links: Link,
Document

Cited by: 3rd item,
Table 2,
Table 3.

- Zhang et al. (2024b)
J. Zhang, X. Xu, N. Zhang, R. Liu, B. Hooi, and S. Deng

Exploring Collaboration Mechanisms for LLM Agents: A Social Psychology View.

arXiv.

Note: arXiv:2310.02124 [cs]Comment: ACL 2024 Main Conference. 64 pages (8 main), 70 figures, 37 tables. Blog: https://www.zjukg.org/project/MachineSoM

External Links: Link,
Document

Cited by: Table 2,
Table 3.

### Appendix A Examples

In this section we step through Figures 4-7, which contain example checklists filled out for each level.

Figure 4. Example for Level 0: The Mechanism Plausibility Scale applied to an implementation of Conway’s Game of Life (28).

Figure 5. Example for Level 1: The Mechanism Plausibility Scale applied to a fabricated game theory paper.

Figure 6. Example for Level 2: The Mechanism Plausibility Scale applied to Schelling’s Model of Segregation (70)

Figure 7. Example for Level 3: The Mechanism Plausibility Scale applied to the Artificial Anasazi Model (24)

### Appendix B Calibrating the Mechanism Plausibility Scale

This section goes through the process of how we iterated on the scale.

#### B.1. Calibration

The Mechanism Plausibility Scale was refined through double-blinded review processes involving papers drawn from a systematic review of LLM-based social simulations by Larooij et al. (45). Each paper was independently evaluated by two reviewers who assigned scores before entering a reconciliation phase. After going through two rounds of calibration, multiple ambiguities still remained about how the scale should be applied. This led to further rework where we decided it would be more appropriate to reframe the scale as a practical checklist format.

#### B.2. Round 1 Calibration

##### B.2.1. Paper Selection and Review Process

We tested early versions of the scale on the first 15 out of 35 papers from Larooij et al.’s systematic review (45).
We chose to evaluate papers from Larooij et al.’s review because we found that their inclusion criteria was heavily aligned with our own research interests.
In particular, the requirements that the ABM uses an LLM as the basis for their agents, there are multiple interacting agents, and that the LLMs were seen to be simulating human behavior, were all aligned with our own conceptions of LLM-ABM social simulation. A copy of the exact queries they used can be found in our Appendix at B.4.

Each paper was reviewed and evaluated by two reviewers; their task comprised of two phases: (1) the evaluation period, and (2) the reconciliation period.
During the evaluation period, each reviewer would read a paper and assign it a score before moving onto the next paper.
The reviewers were blinded to the scores and sentiments of the other reviewer until the reconciliation period began.

##### B.2.2. Inter-Rater Reliability

To assess the reliability of the Mechanism Plausibility Scale, we calculated the inter-rater reliability using a weighted kappa (kwk_{w}) with quadratic weights, suitable for our ordinal scale. As mentioned before, the first structured round of applying the scale to a focused body of literature revealed that it was challenging for even two researchers to apply the scale consistently; we found ambiguities in the rating guidelines and confusion with the nested nature of the simulations through the reconciliation process.

##### B.2.3. Round 1 results of the applied review

Round 1 |

|
Reviewer Scores |

Shortened Title |
A |
B |

Generative Agents (61) |
3 |
1 |

WarAgent (37) |
3 |
1 |

Social Simulacra (62) |
3 |
1 |

S3 (27) |
0 |
1 |

Scale-Free Networks (54) |
3 |
2 |

Humanoid Agents (80) |
3 |
2 |

LyfeAgents (40) |
3 |
0 |

Collaboration (89) |
3 |
2 |

AgentVerse (15) |
3 |
0 |

Epidemic Modeling (85) |
3 |
2 |

Project Sid (3) |
3 |
1 |

Theory of Mind (47) |
3 |
1 |

News Diffusion (48) |
0 |
1 |

SpeechAgents (88) |
1 |
1 |

Fake News Propagation (51) |
1 |
1 |

Table 2. Levels of the Mechanism Plausibility Scale assigned to each paper by Reviewers A and B during the blinded first round of evaluation, along with its assigned level after unblinding and reconciliation.

The results of the first round are shown in Table 2.
Through the reconciliation process, we found that our scale’s rating guidelines and definitions were too ambiguous to handle the operationalization gaps discussed in Section 5.1.

Notably, we also found that many papers conflated Agent-level functionality with ABM-level plausibility.
A paper might have provided high-quality experimental evidence for its Agent-level social simulation (the lowest level in Figure 1), but then they implicitly treated that as sufficient evidence for the claims made about the emergent social phenomenon (TT) observed at the ABM-level, which is a category error.
Work that shows the mechanism plausibility of Agent-level phenomena does not necessarily translate to the mechanism plausibility of ABM-level phenomena. This remains to be shown and must be argued for in the modeler’s Intent, with further Evidence provided at the ABM-level.

Papers had this problem to varying degrees, but the ones that we flagged particularly were:

- •

S3 (27), which conflated (the LLM agent’s capacity to simulate the social media posts of an individual, with matching estimated emotions and attitudes) with (their ABM’s ability to simulate realistic social media phenomena, like opinion dynamics or information cascades).

- •

News Diffusion (48), which conflated their (LLM agent’s ability to share news based on personality traits and friend connections), with their (ABM’s capacity to produce realistic fake news diffusion patterns).

- •

SpeechAgents (88), which conflated (their LLM agent’s ability to generate text-to-speech outputs, which was successfully transcribed back into similar text) with (their ABM’s ability to simulate realistic, emergent human communication dynamics and social interaction patterns at the group level).

- •

Fake News Propagation (51), which conflated (an LLM agent’s capability to reason about, reflect on, and share fake news) with (their ABM’s ability to mechanistically explain realistic fake news propagation dynamics and the emergence of collective opinion patterns).

The presence of these nested simulations was particularly difficult to evaluate with our scale, as it was difficult to identify the target phenomenon TT, and also difficult to identify its operationalization. The ambiguous evaluations between Agent and ABM phenomena led to a split between the reviewer’s perceptions and resulted in an initial quadratic weighted kappa score of 0.207.

#### B.3. Round 2 Calibration

After uncovering the gaps in operationalization (also discussed in Section 5.1), in the second round the reviewers were to assign two scores: one for the ABM-level target phenomena, and one for the Agent-level target phenomena. In addition to the clarified scoring guidelines, the same reviewers were also used in both rounds. and so the increase in reliability may be partially attributable to the training received as part of the first round.

As shown in Table 4, the quadratic weighted kappa for the ABM ratings rose to 0.255, and the score for the Agent ratings reached 0.503. We posit that the score difference between Agent and ABM also comes from papers from the literature review operationalizing the Agent-level phenomena (implicitly) more in-depth compared to the ABM-level. These results are shown in Table 3.

Round 2 |

|
Reviewer Scores |

|
ABM |
Agent |

Shortened Title |
A |
B |
R |
A |
B |
R |

Generative Agents (61) |
3 |
1 |
3 |
3 |
3 |
3 |

WarAgent (37) |
3 |
1 |
3 |
3 |
1 |
3 |

Social Simulacra (62) |
1 |
1 |
1 |
3 |
3 |
3 |

S3 (27) |
0 |
0 |
0 |
1 |
2 |
1 |

Scale-Free Networks (54) |
3 |
3 |
3 |
1 |
1 |
1 |

Humanoid Agents (80) |
1 |
0 |
1 |
3 |
3 |
3 |

LyfeAgents (40) |
1 |
1 |
1 |
3 |
1 |
3 |

Collaboration (89) |
3 |
2 |
3 |
3 |
3 |
3 |

AgentVerse (15) |
3 |
2 |
3 |
3 |
1 |
3 |

Epidemic Modeling (85) |
3 |
2 |
3 |
3 |
2 |
3 |

Project Sid (3) |
3 |
2 |
3 |
3 |
1 |
3 |

Theory of Mind (47) |
1 |
2 |
2 |
3 |
2 |
3 |

News Diffusion (48) |
3 |
2 |
3 |
2 |
1 |
2 |

SpeechAgents (88) |
1 |
0 |
1 |
3 |
3 |
3 |

Fake News Propagation (51) |
3 |
2 |
3 |
3 |
2 |
3 |

Table 3. Levels of the Mechanism Plausibility Scale assigned to each paper by Reviewers A and B in the blinded second round of the literature review, along with its assigned level after unblinding and reconciliation.

Dataset |
Weighted Kappa (kwk_{w}) |
Interpretation |

Round 1 |
0.207 |
Fair Agreement |

Round 2 (Agent) |
0.503 |
Moderate Agreement |

Round 2 (ABM) |
0.255 |
Fair Agreement |

Table 4. Summary of weighted kappa (kwk_{w}) scores using quadratic weights. The ordinal measure was used because the plausibility scale has ordered categories. The interpretation comes from Landis and Koch (44).

In the second round of evaluations, we found that our definition of the Evidence (as stated in Section 3.4) was too broad, allowing for many papers to reach a Level 3 on our scale, regardless of the quality of their Evidence.
Difficulties in ignoring a paper’s perceived evidence quality led to large differences between reviewer scores at the ABM-level.

#### B.4. Queries for LLM ABM-related papers

The 15 papers from our applied study are from Larooij et al. (45):

TITLE-ABS-KEY ( ( "generative social simulation" ) OR ( "generative
agent-based model*" ) OR ( "agent-based simulation" AND "generative
AI" ) OR ( "LLM*" AND "agent-based model*" ) OR ( "large language
model*" AND "ABM" ) OR ( "foundation model*" AND "ABM" ) OR ( "multiagent system*" AND "generative AI" ) OR ( "generative agent*" )
OR ( "social simulation" AND "LLM*" ) OR ( "large language model-based
agents" ) )

We also used Asta33
3

https://asta.allen.ai/chat, an AI research paper search engine built on Semantic Scholar, for paper discovery. Other LLM-ABM papers were from previous knowledge of the authors or related work.

### Appendix C Additional Philosophy of Science Background

#### C.1. Clarification of Model Targets TT

According to a description by Weisberg, TT does not have to be a particular or ‘real’ phenomenon, and some models might not even have a TT; the target could be particular, generic, or even hypothetical (84). As an example, Graebner gives an account of how the target of Schelling’s segregation model (70) is a generalized target, where it represents an abstract city and its arguments can be applied generically rather than to a particular city (32; 84). TT can also be hypothetical; for example, Fisher’s three-sex population simulation (25) shows how a population with three sexes comes with large costs compared to those with only two and is a possible explanation for why three-sex populations do not exist in reality (32; 83).

Experimental support, please
view the build logs
for errors. Generated by

L
A
T
E

xml

.

### Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile
support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the
methods listed below:

- Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues. We appreciate your time reviewing and reporting rendering errors we
may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability
should not be a barrier to accessing research. Thank you for your continued support in championing open access for
all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion, and welcome developer contributions.

We gratefully acknowledge support from
our major funders,
member institutions, ,
and all contributors.

About
·
Help
·
Contact
·
Subscribe
·
Copyright
·
Privacy
·
Accessibility
·
Operational Status (opens in new tab)

Major funding support from
