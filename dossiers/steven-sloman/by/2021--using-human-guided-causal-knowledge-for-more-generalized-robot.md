---
title: "Using Human-Guided Causal Knowledge for More Generalized Robot Task Planning"
person: steven-sloman
section: by
type: journal-article
year: 2021
venue: "arXiv (Cornell University)"
authors: "Tatlidil, Semir, Liu, Yanqi, Sheetz, Emily, Bahar, R. Iris, Sloman, Steven"
source_url: http://arxiv.org/abs/2110.04664
openalex_id: W3207617488
doi: https://doi.org/10.48550/arxiv.2110.04664
cited_by_count: 0
retrieved: 2026-08-13
content: full-text
notes: "preprint version; OA: https://arxiv.org/pdf/2110.04664; Full text from the arXiv PDF, extracted with pdftotext."
---

# Using Human-Guided Causal Knowledge for More Generalized Robot Task Planning

## Abstract (from OpenAlex metadata)

A major challenge in research involving artificial intelligence (AI) is the development of algorithms that can find solutions to problems that can generalize to different environments and tasks. Unlike AI, humans are adept at finding solutions that can transfer. We hypothesize this is because their solutions are informed by causal models. We propose to use human-guided causal knowledge to help robots find solutions that can generalize to a new environment. We develop and test the feasibility of a language interface that naïve participants can use to communicate these causal models to a planner. We find preliminary evidence that participants are able to use our interface and generate causal models that achieve near-generalization. We outline an experiment aimed at testing far-generalization using our interface and describe our longer terms goals for these causal models.

## Full text

Using Human-Guided Causal Knowledge for More Generalized Robot Task
Planning
Semir Tatlidil,1 Yanqi Liu,2 Emily Sheetz,3 R. Iris Bahar,2 Steven Sloman,1
1

arXiv:2110.04664v1 [cs.AI] 9 Oct 2021

Dept.of Cognitive, Linguistics, and Psychological Sciences, Brown University, Providence, RI 02912
2
Dept.of Computer Science, Brown University, Providence, RI 02912
3
Dept.of Electrical Engineering and Computer Science, Robotics Institute, Univ. of Michigan, Ann Arbor, MI 48109
kemal semir tatlidil@brown.edu, yanqi liu@brown.edu, esheetz@umich.edu, iris bahar@brown.edu,
steven sloman@brown.edu
Abstract
A major challenge in research involving artificial intelligence
(AI) is the development of algorithms that can find solutions
to problems that can generalize to different environments and
tasks. Unlike AI, humans are adept at finding solutions that
can transfer. We hypothesize this is because their solutions
are informed by causal models. We propose to use humanguided causal knowledge to help robots find solutions that
can generalize to a new environment. We develop and test
the feasibility of a language interface that naı̈ve participants
can use to communicate these causal models to a planner.
We find preliminary evidence that participants are able to use
our interface and generate causal models that achieve neargeneralization. We outline an experiment aimed at testing
far-generalization using our interface and describe our longer
terms goals for these causal models.

Introduction
One of the most impressive feats of human intelligence is
our ability to transfer learned knowledge to solve a problem
in a novel environment (Shepard 1987). Despite their overall
success, state-of-the-art machine learning methods struggle
with this (Edmonds et al. 2020; Nair et al. 2019).
What makes this problem challenging is determining an
appropriate level of granularity for state representations. If
an agent represents the states of its environment at a very detailed level, then it will likely fail to apply the solution that
it learned in a new environment because even small changes
in the environment will appear as new states. For example,
consider the task of putting together an object that can emit
light. In the training environment, we learn that connecting
wax and a wick and then lighting the wick will emit light. If
we try to apply this knowledge in a new environment where
wax is replaced with a container filled with oil, we can only
do this if we know that wax and oil share some critical feature that makes them interact with the wick in a similar way
to emit light. In other words, we need to construct an abstract
model of the states in our environment.
The importance of constructing abstract state representations for human-like intelligence has been emphasized by
AI researchers (Konidaris 2019). Previous works has shown
Copyright © 2021, Association for the Advancement of Artificial
Intelligence (www.aaai.org). All rights reserved.

that abstract state representations can be learned automatically from simulations using reinforcement learning (RL)
(Abel, Hershkowitz, and Littman 2016) or generative adversarial nets (Kurutach et al. 2018). Studies focusing on transfer learning show that abstract representations lead to more
efficient solutions in novel tasks (Asadi, Abel, and Littman
2020; Kokel et al. 2021). However, a major drawback of
these methods is that they may require many trials in order
to learn a good abstract state representation, and the learned
representations may not be interpretable by humans.
In contrast to AI research, studies with people suggest
that they are able to construct abstract representations with
limited experience and are able to generalize this knowledge across tasks (Holyoak 2012). What makes people so
efficient in constructing abstract representations? One line
of evidence suggests that it is people’s tendency to think
about events in causal terms. Studies looking at how people create categories, which can be seen as a method of state
abstraction by aggregating instances, show that people are
heavily influenced by causal information in category formation (Marsh and Ahn 2009; Waldmann and Hagmayer
2006). Moreover, they tend to employ these causal categories to solve problems of a similar nature in new environments (Lien and Cheng 2000). In complex domains where
a multitude of features can be used for categorization (such
as categorizing different types of fish), evidence indicates
that novices are more likely to categorize by considering surface level features such as perceptual similarity. On the other
hand, experts are more likely to categorize based on causal
information (Rottman, Gentner, and Goldwater 2012; Shafto
and Coley 2003). Overall, these studies provide strong evidence that humans tend to create abstract categories using
causal information and use such information in a variety of
(simple or complex) tasks.
The central role of causality in achieving human-like intelligence has been recognized by AI researchers particularly with respect to learning abstract, generalizable knowledge (Schölkopf et al. 2021; Zhu et al. 2020). For instance,
Edmonds et al. (2020) investigated whether learning causal
information in an escape room task would lead to better performance in a new environment. They showed that
while a number of RL agents showed little to no transfer of
knowledge across environments, an agent that learned abstract causal rules was able to transfer this knowledge to the

new environment and learn the new solution much quicker.
Moreover, the behavior of the causal agent was similar to the
behavior of human subjects. This supports both the importance of causality in human thinking and how causal knowledge aids in generalizing knowledge across environments.
In a different task that involved learning the relationship between many electrical switches and light bulbs, Nair et al.
(2019) have found that an agent that learns causal rules is
better able to use this knowledge to solve tasks in new environments compared to model-free RL agents that do not
learn the causal rules. Overall, the evidence strongly suggests that understanding the causal mechanisms of a task is
critical for generalizing performance to new environments
both in human agents and in AI.
Our goal is to develop a human-robot interaction system
where causal knowledge communicated by a human is used
by the robot to complete specific tasks and apply this knowledge to novel tasks. We propose to use causal information
communicated to the robot by a human in the form of causal
graphical models (Sloman 2005). These causal models will
communicate which features of the environment are relevant
to the task, giving us an appropriate state abstraction. To the
extent that a new task fits into the same causal model, this
knowledge can be reused.
In this paper, we present the first step of this work where
we develop a user interface that allows people to communicate causal models of how various objects work to produce
light. We conducted a preliminary online experiment to test
if naı̈ve users could use our interface to express their causal
models and to see if their causal models would achieve neargeneralization.

Assembling objects using causal models
Our approach can be described in three steps. First, participants use an interface to express the causal model of how
an object works to produce light. The users are required to
express a causal graph in terms of what function each object part performs that causes light to be emitted, instead
of describing the object parts themselves. Second, we interpret the user-generated causal graph as a reward function for
a high-level symbolic planner. The planner generates a sequence of actions to assemble the object. Finally, the highlevel symbolic planner will be connected to a simulator that
converts the plan into a sequence of motor commands and
visually demonstrates the execution of the task. In our experiment, we have four light-producing objects: a candle, a
kerosene lamp, a desk lamp, and a flashlight. A candle and
a kerosene lamp are considered to be from the same category of ”light production method” as they both burn fuel to
produce light. A desk lamp and a flashlight are considered
to be from the same category as they both use electricity to
produce light.
Our definition of a successful causal model is a causal
model that can be used by the planner to generate an accurate
plan to assemble the new object, regardless of the specific labels chosen by the participants to represent the functions of
the object parts. If the causal model of an object can be used
to generate a plan for another object from the same category,
we consider this a successful near-generalization. If it can

be used to generate a plan for an object from a different category, then it is a successful far-generalization as shown in
Fig.1. In this experiment, we only tested near-generalization.
Training object

Neargeneralization

Fargeneralization

Desk lamp

Flashlight

Candle

Figure 1: Near- and far-generalization

Near-generalization experiment
Nine undergraduates attending Brown University participated for course credit. They first read a short tutorial explaining that their task was to describe how an object produced a certain effect by constructing the causal model using our interface. The tutorial explained how the interface
worked with an example object that was different than the
light-producing objects. They were then directed to an experiment page that involved three steps. In the first step, they
were presented with one of the four light-producing objects
(order was counterbalanced across participants) with a short
explanation of how the object worked, as well as a picture
of the object with labeled parts. They identified the functions of object parts relevant to achieving the final effect light. They did this by writing down function labels for object parts themselves as shown in Fig.2. They were allowed
to associate multiple functions with a single part, and multiple parts with a single function.
The second step involves describing the causal model of
the object in terms of the functions of the object parts. The
causal model is a collection of causal rules that are expressed using predefined keywords. Each rule establishes
which function or multiple functions of object parts cause
an effect. The final effect is always the goal (i.e., light), but
participants were allowed to enter intermediate effects (that
were different from functions of object parts identified in the
first step) that can be used as causes in another causal rule.
After they entered their causal model, they saw their model
in graphical format and the interface generated a plan using their causal model and presented it to them in a text format describing which object parts are connected as shown in
Fig.3. If the generated plan was not satisfactory, participants
could go back and update their causal models.
The presentation of the plan is intended to establish a
dynamic communication channel between the human and
the robot: the robot uses the causal model to generate a
plan and the human sees how this causal model affects the
robot’s planning behavior, which can help the human understand what needs to be changed in the causal model if the
plan is not satisfactory. In the final step, we tested for neargeneralization by presenting a new object from the same cat-

Figure 2: Step 1 user input example

Figure 4: Step 3 user input example

Figure 3: Causal model created by a user in Step 2 for the
desk lamp. Functions of the object parts identified by the
same user are shown in Fig.2
egory as the training object and asked the participants to associate the functions of the new object parts with the functions they described for the previous object. Then, the planner tried to create a plan for the test object using the causal
model that was created for the training object. Note that participants were not allowed to create a new causal model for
the test object or to update their causal model of the training object. As a result, the planner could only succeed if the
causal model of the training object was abstract enough to
describe how the test object worked. Each participant went
through this 3-step process once for each category.

commands that can be performed by a simulator or a real
robot. We choose to use Markov Decision Process (MDP)
as the framework for planning. MDP captures the probability of state transition when an action is performed, which accounts for robot action uncertainty and object parts compatibility. The MDP problem is defined by {S, A, T, R}, where
S represents the current assembly state (i.e., the current object parts assembled, their positions in the assembled structure), A is the set of predefined actions, T is the transition
probability, and R is the reward function at a given state. The
transition probability T = P (S, A, S 0 ) can be estimated by
the compatibility of the connection points between two object parts O1 , O2 . The connection compatibility can be predefined with binary values or can be estimated based on the
geometric alignment of the connectors.
For the reward function R, we use the causal model G created by the user to guide the reward for each state. The causal
model generates a score representing whether a given state
is able to achieve the final effect. Each node V in the causal
graph is a binary value. For a current assembled structure
with object O1 .. On , function nodes associated with each
object parts will have value a of 1. The value of the final effect node, Vgoal , is determined by a functional relationship
f of the values of its parent nodes and calculated recursively
until the function nodes (i.e., root nodes) are reached:
Vgoal = f (parent(Vgoal ))

(1)

The reward function is dependent on the value of Vgoal . We
assign positive reward if the goal is reached and negative reward if goal is not reached and there is no further applicable
actions.

Planner
The planner is in charge of generating a sequence of actions. The actions that a planner generates are high-level
action primitives such as, screw, insert, connect. The highlevel action primitives will be processed to generate motor

Results
The results of our preliminary experiment suggest that most
people were able to use our interface to express reasonable
causal models with minimal instructions that they received

on the tutorial page. An example of a successful model created by a participant for the desk lamp (training) that transferred to the flashlight (test) is shown in Fig.3 and Fig.4.
This provides preliminary evidence supporting the claim
that causal models created by people can achieve neargeneralization. Moreover, it also shows that our interface
can be used to communicate these causal models. In some
cases, participants created valid causal models for the training object but their model failed to transfer to the test object.
An example model that failed to transfer from desk lamp
to flashlight is shown in Fig.5. This model fails because of
two reasons. First, the participant did not specify any of the
flashlight parts with the function “turn electricity into light”
that was in their causal model, and as such, the flashlight
parts were not enough to achieve the goal. Second, in step
3 the user added a new function “hold things together” for
the “case” part of the flashlight that was not present in their
earlier causal model.
Some of the failures of transfer are likely due to participants misunderstanding the task. For instance, it is likely that
the participant decided to include “hold things together” as
a function for the flashlight because they misunderstood the
task to be describing the functions of all object parts instead
of describing only the functions relevant to producing light.
The same participant included “diffuse light” function of the
“shade” of the desk lamp to be necessary for achieving the
goal of producing light, which clearly cannot be true since
one has to produce light before it can be diffused. In the
next experiment, we will clarify subtle differences like these
to elicit more appropriate causal models for our task.

causal models. For instance, some users specified intermediate effect nodes in their causal models but did not specify
their causes despite being instructed to do so in the tutorial.
We will prevent the users from submitting such causal models and present them with an error message explaining what
they need to change.

Far-generalization experiment
For our next experiment, we will update our interface to
address the ambiguities that led some participants to generate causal models that were invalid or failed to transfer,
as discussed in the previous section. We will use the updated interface to test for both near-generalization and fargeneralization. We will present two training objects to participants and ask them to generate a single causal model
that describes how they produce light. Half of the participants will be assigned to a near-generalization condition
where the two training objects they see will be from the
same category (i.e., producing light by burning fuel or by using electricity). The other half will be in a far-generalization
condition and they will see one object from each category.
The test phase will be identical for both groups of participants: they will see a novel object from one category and
will be asked to complete step 3 of the current experiment
as described in the ”Near-generalization experiment” section. Then, they will see a second test object from a different
category than the first test object and will be asked to repeat
step 3 with this object as well. We predict that presenting
two objects from the same category will lead participants to
generate causal models that will only generalize to the test
object from the same category, so participants in the neargeneralization condition are predicted to create models that
will achieve near-generalization but not far-generalization.
In contrast, presenting two objects from different categories
to the participants in the far-generalization category should
lead them to think in even more abstract terms, so we predict
that their causal models will generalize to both test objects.
The order of objects presented as training and test objects
will be counterbalanced across participants.

Future Work

desk lamp parts
shade
light bulb
base with cables
flashlight parts
case
head
batteries

functions
diffuse light
turn electricity into light
provide electricity
functions
hold things together
diffuse light, provide electricity
provide electricity

Figure 5: Example of a failed causal model generated by a
user. Table on the top shows the step 1 input for the training
object (desk lamp) and the table below shows the step 3 input
for the test object (flashlight)
Finally, in a few trials participants generated invalid

In addition to our next experiment, in the future, we are
planning to use an online platform, such as Amazon Mechanical Turk, to recruit a high number of participants and
test the generalizability of the causal models they generate.
Inspired by recent developments in relation networks (Sung
et al. 2017) and graph neural networks (Zhou et al. 2018), we
aim to use a neural network to extract a single causal model
from a large sample of user-generated causal models. We
predict that a causal model learned from a large sample of
users is more likely to be accurate compared to a model generated by an average user, given the evidence suggesting that
collective decision making tends to outperform decisions of
individuals (Surowiecki 2005) even if the individuals are experts (Wolf et al. 2015).

References
Abel, D.; Hershkowitz, D.; and Littman, M. 2016. Near
Optimal Behavior via Approximate State Abstraction. In

Balcan, M. F.; and Weinberger, K. Q., eds., Proceedings of
The 33rd International Conference on Machine Learning,
volume 48 of Proceedings of Machine Learning Research,
2915–2923. New York, New York, USA: PMLR.
Asadi, K.; Abel, D.; and Littman, M. L. 2020. Learning
State Abstractions for Transfer in Continuous Control. arXiv
preprint arXiv:2002.05518 .
Edmonds, M.; Ma, X.; Qi, S.; Zhu, Y.; Lu, H.; and Zhu, S.C. 2020. Theory-based causal transfer: Integrating instancelevel induction and abstract-level structure learning. In Proceedings of the AAAI Conference on Artificial Intelligence,
volume 34, 1283–1291. doi:10.1609/aaai.v34i02.5483.
Holyoak, K. J. 2012. Analogy and relational reasoning. In
Holyoak, K. J.; and G., M. R., eds., The Oxford handbook
of thinking and reasoning, 234–259. New York, NY, USA:
Oxford University Press.
Kokel, H.; Manoharan, A.; Natarajan, S.; Ravindran, B.; and
Tadepalli, P. 2021. RePReL: Integrating Relational Planning and Reinforcement Learning for Effective Abstraction.
Proceedings of the International Conference on Automated
Planning and Scheduling 31(1): 533–541.
Konidaris, G. 2019. On the necessity of abstraction. Current
Opinion in Behavioral Sciences 29: 1–7. doi:https://doi.org/
10.1016/j.cobeha.2018.11.005.
Kurutach, T.; Clavera, I.; Duan, Y.; Tamar, A.; and Abbeel,
P. 2018. Model-ensemble trust-region policy optimization.
arXiv preprint arXiv:1802.10592 .
Lien, Y.; and Cheng, P. W. 2000. Distinguishing genuine
from spurious causes: A coherence hypothesis. Cognitive Psychology 40(2): 87–137. doi:https://doi.org/10.1006/
cogp.1999.0724.
Marsh, J. K.; and Ahn, W.-k. 2009. Spontaneous assimilation of continuous values and temporal information in
causal induction. Journal of Experimental Psychology:
Learning, Memory, and Cognition 35(2): 334–352. doi:
https://doi.org/10.1037/a0014929.
Nair, S.; Zhu, Y.; Savarese, S.; and Fei-Fei, L. 2019. Causal
induction from visual observations for goal directed tasks.
arXiv preprint arXiv:1910.01751 .
Rottman, B. M.; Gentner, D.; and Goldwater, M. B. 2012.
Causal Systems Categories: Differences in Novice and Expert Categorization of Causal Phenomena. Cognitive Science 36(5): 919–932. doi:https://doi.org/10.1111/j.15516709.2012.01253.x.
Schölkopf, B.; Locatello, F.; Bauer, S.; Ke, N. R.; Kalchbrenner, N.; Goyal, A.; and Bengio, Y. 2021. Toward causal
representation learning. Proceedings of the IEEE 109(5):
612–634.
Shafto, P.; and Coley, J. D. 2003. Development of categorization and reasoning in the natural world: Novices to
experts, naive similarity to ecological knowledge. Journal
of Experimental Psychology: Learning, Memory, and Cognition 29(4): 641–649. doi:https://doi.org/10.1037/02787393.29.4.641.

Shepard, R. N. 1987. Toward a universal law of generalization for psychological science. Science 237(4820): 1317–
1323.
Sloman, S. 2005. Causal models: How people think about
the world and its alternatives. Oxford University Press.
Sung, F.; Yang, Y.; Zhang, L.; Xiang, T.; Torr, P. H. S.; and
Hospedales, T. M. 2017. Learning to Compare: Relation
Network for Few-Shot Learning. CoRR abs/1711.06025.
URL http://arxiv.org/abs/1711.06025.
Surowiecki, J. 2005. The wisdom of crowds. Anchor.
Waldmann, M. R.; and Hagmayer, Y. 2006. Categories and
causality: The neglected direction. Cognitive Psychology
53(1): 27–58. doi:https://doi.org/10.1016/j.cogpsych.2006.
01.001.
Wolf, M.; Krause, J.; Carney, P. A.; Bogart, A.; and Kurvers,
R. H. 2015. Collective intelligence meets medical decisionmaking: the collective outperforms the best radiologist. PloS
one 10(8): e0134269. doi:https://doi.org/10.1371/journal.
pone.0134269.
Zhou, J.; Cui, G.; Zhang, Z.; Yang, C.; Liu, Z.; and Sun, M.
2018. Graph Neural Networks: A Review of Methods and
Applications. CoRR abs/1812.08434. URL http://arxiv.org/
abs/1812.08434.
Zhu, Y.; Gao, T.; Fan, L.; Huang, S.; Edmonds, M.; Liu, H.;
Gao, F.; Zhang, C.; Qi, S.; Wu, Y. N.; Tenenbaum, J. B.; and
Zhu, S.-C. 2020. Dark, Beyond Deep: A Paradigm Shift to
Cognitive AI with Humanlike Common Sense. Engineering 6(3): 310–345. doi:https://doi.org/10.1016/j.eng.2020.
01.011.
