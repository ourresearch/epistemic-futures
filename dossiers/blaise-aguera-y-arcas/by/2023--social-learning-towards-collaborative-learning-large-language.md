---
title: "Social Learning: Towards Collaborative Learning with Large Language Models"
person: blaise-aguera-y-arcas
section: by
type: journal-article
year: 2023
date: 2023-12-18
venue: "arXiv (Cornell University)"
authors: "Amirkeivan Mohtashami, Florian Hartmann, Sian Gooding, Lukáš Žilka, Matt Sharifi, Blaise Agüera y Arcas"
source_url: http://arxiv.org/abs/2312.11441
retrieved: 2026-08-13
content: full-text
notes: "OpenAlex W4389974749 (type: preprint). Full text extracted from the open-access PDF at https://arxiv.org/pdf/2312.11441."
---

# Social Learning: Towards Collaborative Learning with Large Language Models

## Full text

### Abstract (from OpenAlex metadata)

We introduce the framework of "social learning" in the context of large language models (LLMs), whereby models share knowledge with each other in a privacy-aware manner using natural language. We present and evaluate two approaches for knowledge transfer between LLMs. In the first scenario, we allow the model to generate abstract prompts aiming to teach the task. In our second approach, models transfer knowledge by generating synthetic examples. We evaluate these methods across diverse datasets and quantify memorization as a proxy for privacy loss. These techniques inspired by social learning yield promising results with low memorization of the original data. In particular, we show that performance using these methods is comparable to results with the use of original labels and prompts. Our work demonstrates the viability of social learning for LLMs, establishes baseline approaches and highlights several unexplored areas for future work.

---

Social Learning:
Towards Collaborative Learning with Large Language Models

arXiv:2312.11441v2 [cs.LG] 8 Feb 2024

Amirkeivan Mohtashami * 1 Florian Hartmann * 2 Sian Gooding 2
Lukas Zilka 2 Matt Sharifi * 2 Blaise Aguera y Arcas 2

Abstract
We introduce the framework of "social learning"
in the context of large language models (LLMs),
whereby models share knowledge with each other
in a privacy-aware manner using natural language. We present and evaluate two approaches
for knowledge transfer between LLMs. In the first
scenario, we allow the model to generate abstract
prompts aiming to teach the task. In our second
approach, models transfer knowledge by generating synthetic examples. We evaluate these methods across diverse datasets and quantify memorization as a proxy for privacy loss. These techniques inspired by social learning yield promising results with low memorization of the original
data. In particular, we show that performance using these methods is comparable to results with
the use of original labels and prompts. Our work
demonstrates the viability of social learning for
LLMs, establishes baseline approaches and highlights several unexplored areas for future work.

1. Introduction
Increasingly, large language models are considered a crucial
building block for agents that can reason (Parisi et al., 2022),
use tools (Liu et al., 2023) and adapt to environmental cues
(Liu et al., 2022; Yao et al., 2023) for many real-world tasks.
As such, personal assistants are now commonly powered
by such models (Pinsky, 2023) while larger entities, e.g.
companies, can also have their own agents. When considering networks of personal agents, the ability to transfer
information and foster collaboration is highly desirable. For
instance, a spam detector can be collaboratively maintained
by sharing newly detected spam templates.
*
Equal contribution 1 EPFL, Work done during an internship at Google 2 Google. Correspondence to: Amirkeivan Mohtashami <amirkeivan.mohtashami@epfl.ch>, Florian Hartmann
<fhartmann@google.com>.

Collaboration among language models to solve complex
problems involves various research areas (Wang et al.,
2023), for example task planning (Huang et al., 2022),
information retrieval (Deng et al., 2023; Zamani et al.,
2023) and information exchange (Liang et al., 2023). LLMs
have shown impressive capabilities at performing novel
tasks by following natural language instructions or using a
limited number of examples (Brown et al., 2020; Wei et al.,
2021). This suggests that natural language might become
a viable means of knowledge transfer for personal agents.
However, a critical concern is how to ensure the privacy
of users is upheld by preventing the leakage of sensitive
information between agents.
In this work, we introduce the paradigm of privacy-aware
"social learning" to transfer knowledge between LLMs. We
take inspiration from the theory of social learning as defined by Bandura & Walters (1977) which proposes that
new behaviors can be acquired by observing and imitating others. Indeed, mechanisms of social learning have
proven highly effective in persistent multi-agent systems by
allowing agents to benefit from the accumulated learning
of others (Alonso et al., 2001; Ndousse et al., 2021). The
resulting framework enables agents to generate examples
and instructions tailored for task-specific information transfer with an emphasis on safeguarding the privacy of shared
examples and knowledge. We posit that this framework
is advantageous as it provides knowledge transference between models in a human-interpretable way without sharing
private data.
The key contributions of our work are (1) proposing and
formalizing the concept of social learning for LLM-driven
agents; (2) suggesting baseline implementations of social
learning and benchmarking them across a diverse set of
tasks and (3) establishing metrics to measure private data
leakage, and using them to demonstrate the benefits of social
learning whilst preserving privacy.

2. Problem Setting & Methods
Language models have made significant strides in generating effective responses based on instructions, spanning

Social Learning: Towards Collaborative Learning with Large Language Models
(Optional)
Additional Communication
(e.g. voting)

Student
(Aggregator)

Student

Instruction /
examples request

User

Training

Inference

Figure 1. An illustration of our social learning framework. Teachers have access to private data that they cannot directly share. The student
does not have access to such data. Instead it relies on the teachers to create instructions or non-private examples to teach it the task. After
receiving these instructions, the student aggregates them into a single prompt. This prompt is used by the student at inference time to
respond to a user’s queries.

domains like planning and memory (Wang et al., 2023).
However, the inclusion of private data brings forth new
challenges, including navigating data ownership, preserving
privacy, and securely transferring knowledge. In this work,
we introduce the social learning framework as a tailored
response to these challenges. Specifically, we explore an environment where information about a task is communicated
from multiple teachers to a student through text-based interactions, within predefined constraints aimed at preserving
the privacy of original examples.
As a real-world example of such an environment, consider
the task of detecting whether a message received through
Short Message Service (SMS) is spam or not. Let us assume
that we have asked m users to act as annotators and classify
their messages as spam or not spam. The goal is to use this
data to enable a new user’s phone to automatically detect
whether a new incoming message is spam or not. However,
while users may agree to perform the annotation, they
seldom want to share the contents of their messages due to
privacy concerns. Therefore the goal is to send informative
messages based on labeled data available locally on each
user’s phone without communicating the contents of any
message.
2.1. Social Learning Protocol
We provide a canonical definition of social learning in this
section by considering m agents T1 , . . . , Tm , called teachers
that teach a task (e.g. yes/no question answering) to another
agent S, called the student. Each teacher has access to its
own silo of data DTi which contains a distinct subset of
examples for the task. Meanwhile, the student does not have
access to any training data. A user queries the student at
inference time to solve new, unseen instances of the task.

As such, the goal is to transfer the knowledge of the teachers
to the student so that it can successfully respond to a query.
Similar to standard machine learning models, we consider
two operation modes for this environment: training and inference. During training the agents collaborate without any
input to transfer task-related knowledge whereas at inference time the student relies on this transferred knowledge
to answer the specific instance of the task. Therefore, the
student can augment its knowledge (stored in DS ) by communicating with teachers during training and subsequently
relies on the accumulated knowledge to answer queries at
inference time.
At training time, part of the role of the student is that of an
aggregator where it must select a subset of the information
provided to it by the teachers. In this work, we only consider
the most basic version of the student at inference which
replies to a user input by appending the input to a prompt,
querying its language model, and returning the continuation.
The whole process is illustrated in Figure 1.
A solution to the problem of how to teach the student can be
to send all the data accessible by the teachers to the student
and have it concatenate all of these data points to create
the final prompt. In this case, the student receives all the
knowledge and the task is reduced to generating a good response based on the available data. However, it is important
to consider cases where this is not possible, for example
because of privacy constraints. In particular, we consider
the scenario where the original examples accessible by the
teachers contains private data that should not be shared with
other parties. Therefore, the goal is to teach the student without sharing such private information which automatically
excludes the possibility of sharing the original examples. In
our evaluations, we consider directly sharing the original ex-

Social Learning: Towards Collaborative Learning with Large Language Models

amples of the teachers as a baseline to compare our methods
against.

method compromises privacy which is why we only consider it as a baseline. Instead, we consider sharing artificial
examples that are generated based on the real data.

2.2. Methods

To let teachers generate artificial examples, we make use of
their language models. In particular, given the capability
of language models to follow the format of the input and
replicate it (Shao et al., 2023), the continuation of a few-shot
prompt can be expected to contain new examples. As such,
to generate a new artificial example, each teacher selects
ngen examples from its private set and generates artificial
examples by providing them as the few-shot prompt to its
language model, using the model to generate a continuation
without any additional instructions.

The mechanisms of knowledge transfer in our work are
inspired by social learning theory (Bandura & Walters,
1977). The theory outlines models of observational learning amongst humans and we use two of these as the basic
models of communication in our framework. While a combination of these basic models is most likely more effective,
in this work we only look at the performance when they are
employed separately. These models are simple enough that
they satisfy additional constraints which allows us to avoid
the need for abilities in language models that are yet to be
perfected. We refer the interested reader to Appendix A
where we provide an overview of these constriants and their
motivations.
2.2.1. V ERBAL S OCIAL L EARNING : S HARING
I NSTRUCTIONS
In the verbal instruction model from social learning theory, a behavior is described in detail and a participant is
instructed in how to engage in the behavior.
Conversely, LLMs are able to perform new tasks based
on short, textual instructions describing the tasks in question (Mishra et al., 2021). Previous work has also shown
that these instructions can be generated by prompting an
instruction-tuned LLM with examples and then asking it to
complete the instruction for them (Honovich et al., 2022).
Similar to the verbal instruction model, we can thus ask
teacher agents to generate instructions based on their silo
of private data. These instructions are then shared with the
student who integrates the instructions in its prompt. In
this work, when using this model, we focus on the scenario
where there is only a single teacher. We apply this simplification to avoid the need for an aggregation mechanism
that merges multiple instructions and leave developing such
mechanisms for future work.
2.2.2. L IVE MODELS : S HARING E XAMPLES
In the live models method from social learning theory, an
individual demonstrates the desired behavior and the learner
imitates.
Conversely, a technique used that allows LLMs to perform
well on a new task is including examples of that task in
the prompt (Brown et al., 2020), a technique called fewshot learning. Even including a few examples can greatly
improve the downstream performance.
One option for teaching using this learning model is sharing
examples from the teacher’s private dataset. However, this

The continuations are generated by querying the model with
temperature sampling with temperature τ and selecting the
top scoring (based on perplexity) k continuations. Some
of these continuations might be discarded due to concerns
such as privacy or faulty generation while the rest are sent
to the aggregator, the component responsible for generating
the final prompt for the student. The aggregator then picks
from the at most ngen · k generated examples, and adds the
selected ones to the student’s prompt.

3. Related Work
3.1. LLMs and agents
Zero-shot or few-shot prompting has been shown to be
highly effective for transfer learning, notably by Brown
et al. (2020). In such approaches, a large pre-trained language model is zero-shot or few-shot prompted by being
shown examples of the desired behaviour, without training,
to perform a new task. Variations on these methods such as
chain-of-thought prompting (Wei et al., 2022) have shown
that even simple prompt modifications can have a substantial impact on target task performance (Wei et al., 2022;
Chowdhery et al., 2022) and enable new capabilities.
There is a large pre-existing body of work focused on multiagent based communication via dialogue to solve complex
tasks (Cobbe et al., 2021b; Rafailov et al., 2023). The
motivation is that by cross-agent interaction, LLMs can collectively exhibit enhanced performance by aggregating their
strengths. Multiple works have focused on debate between
LLMs to improve output of models. For instance, (Du et al.,
2023) allow multiple language model instances to propose
and debate their responses and reasoning processes. Their
findings indicate that this approach significantly enhances
mathematical and strategic reasoning across a number of
tasks. Perez et al. (2022) also propose a debate procedure to
verify the accuracy and safety of generated content. However, in these scenarios, the concept of agents having access
to separate datasets is not considered.

Social Learning: Towards Collaborative Learning with Large Language Models

Most similar to our work, Zeng et al. (2022) introduce a modular framework that allows multimodal models to exchange
information with each other and capture new capabilities using zero-shot transfer. Their approach does not require fine
tuning and aims to capitalize on the different types of knowledge contained by models capturing different modalities.
3.2. Federated Learning
Federated learning (Konečnỳ et al., 2016; McMahan et al.,
2017; Kairouz et al., 2021) is a technique for training models
on decentralized data without collecting any of this data in a
central place. Instead, a central server coordinates the fleet
of participants during the training process. In each round
of training, a subset of participants is sampled. Each participant receives the current weights of the model, uses their
local data to update them, and then sends back the gradients.
The server combines all the model updates across participants and uses them to update the model of the next iteration.
Social learning is similar to federated learning in that no
raw data is meant to be transmitted and that the participants
aim to jointly learn to perform a task. However, in contrast
to federated learning, social learning does not update any
model weights and instead works solely by exchanging
information expressed in natural language. This has a few
advantages:
1. All components are agnostic to the specific models
used. Teachers and students can be based on different
model sizes, architectures and weights. All they need
to be able to do is to input and output natural language.
2. Text is more compact than gradients. In federated
learning today, it would be prohibitively expensive to
send full updates for the largest foundation models.
With social learning, everything is expressed in text
fitting a prompt, which can easily be transmitted across
networks.
3. Text is much more interpretable than gradients. One
can read what teachers produce and analyze it.
While social learning is distinctively different from federated learning, some of its concepts can be transferred across
to the social learning setting. In our privacy analysis in
Section 5 for example, we adapt Secret Sharer (Carlini et al.,
2019), a technique that is also popular in federated learning.

4. Experiments
In order to assess the effectiveness of the methods we discussed in Section 2.2, we evaluate their performance on
different tasks in this section. Since the challenges involved
in social learning are new, it also requires its own task suite.

In this work, we propose a set of tasks with different properties and challenges and use them for benchmarking. We
provide an overview of the benchmarking suite and the
properties of each task in Appendix B. In most of the experiments, we use instances of PaLM 2 (Anil et al., 2023)
models, specifically PaLM 2-S, to power both the teachers
and the student. Since we need the model to follow instructions when doing instruction generation, to ease comparison,
we use the instruction-tuned version of the models in all of
our experiments.
To account for the randomness arising from temperature
sampling and the distribution of the dataset between teachers, we repeat each experiment 5 times and report the mean.
We also perform significance testing, as described in Appendix C. This lets us systematically evaluate whether there
are meaningful differences between using original data and
synthetic data generated through social learning.
4.1. Live models: Sharing Examples
We follow the process outlined in Section 2.2.2 with m = 8
teachers and compare the performance of a prompt with n
generated examples for different values of n against several baselines. The dataset is distributed between teachers
randomly so all teachers will have the same data distribution. The zero-shot performance of the model on the task
institutes a low bar baseline. As a high bar, we consider
the performance of doing few-shot learning with n private
examples from one of the teachers, equivalent to asking that
teacher to directly solve the task. Note that this is not feasible in practice and thus is a high bar since sending private
examples of a teacher, or querying one teacher with inputs
given to the student violates their privacy. Therefore, we do
not aim to outperform this baseline but to show that we can
perform comparably using the generated examples.
In most of our experiments we use a basic aggregation
mechanism where the aggregator picks one of the artificially
generated candidates at random. We call this aggregator the
random aggregator.
We start by considering the scenario where the student’s
language model is the same as the teachers’. Since the
only difference between the teachers and the student in
this case is the set of examples they can access, we can
compare the effect of using generated examples instead of
real ones more clearly. The results are shown in Table 1 and
highlight various patterns that give insight on effectiveness
of generating artificial examples. We now discuss several of
these patterns in detail.
For the majority of tasks, we observe no significant difference between using original private examples and the
generated ones, especially when the number of examples
is high enough, e.g. n = 16. This is especially interesting

Social Learning: Towards Collaborative Learning with Large Language Models

n

Type

Lambada

BoolQ

GSM8K

SMSSpam

SMS Spam
(With Class)

Random
Insertion

0

-

69.8

68.1

0.0α

14.2

92.7

22.0

1

Original
Generated

86.7
86.7

89.8
70.5 *

63.6
63.9

59.1
90.2 *

94.3
92.6 *

55.6
53.6 *

2

Original
Generated

87.3
86.7

90.1
88.6 *

64.2
63.2 *

77.2
88.2 *

94.9
92.2 *

70.0
65.9 *

4

Original
Generated

87.6
88.0

90.4
85.6 *

63.6
63.6

86.8
87.8

95.4
90.2 *

69.8
69.7

8

Original
Generated

88.4
88.1

90.5
88.7 *

64.1
63.4

96.0
86.5 *

96.8
91.5 *

74.5
69.2 *

16

Original
Generated

88.4
89.0

90.4
90.0

63.6
63.7

96.5
88.0 *

97.0
91.1 *

73.5
72.4

Table 1. Performance of PaLM 2-S with different methods on different datasets. A star marks a statistically significant difference between
performance using original and generated examples. We bold cells where no statistically significant difference was detected to emphasize
that in many cases the examples generated using social learning perform as well as the original ones. The average accuracy across 5 runs
is reported. Table 8 reports the same values with more precision.
α

GSM8K uses a special format to mark the answer. The model inevitably always fails when no instruction or examples are
provided to clarify this special format. Adding the prefix stated in Figure 4 in the Appendix to clarify the format yields an accuracy of
16.38%.

The following examples are privately
shared with you and will not be given
to the participants. Describe the
format (any special markings used), and
general patterns and any other useful
generic notes that you can find based
on these examples. What you write will
be the only hint given to the
participant and they are expected to
output correct replies in the right
format.
<Original Examples>
Task format with detailed instructions:
Figure 2. The prompt used to generate instructions for a task.

since we observe that these generated examples are sufficiently different from the real ones. We confirm this in
Appendix D where we report a high average normalized
distance between each generated example and the prompt
used for generating it. We note that this investigation is
different from measuring the amount of data leakage which
we investigate in Section 5 as the examples can be different
and yet still contain sensitive information.
The main exception where a difference can be observed
between generated and real examples is the spam detec-

tion task. Based on our observations, we conjecture that
one of the underlying reasons that makes generating artificial examples for this task more challenging is that the
language model favors not spam examples over spam examples. Boolean Questions is another task where the model
struggles when given generated examples, though the gap
closes when the number of examples is large enough. In
this task we also observe that the language model seems
to strongly favor questions with a yes answer, suggesting
that the favor of one class is a re-occurring challenge in
generating examples for classification tasks. For Boolean
Questions we also observe another challenge that the language model tends to generate questions that do not have a
yes or no answer.
Finally, we observe that generating factual examples is not
essential for transferring knowledge. For example, we observe that some of the generated examples and provided
solutions in the GSM8K task can be wrong without hurting
performance. As shown in prior work (Min et al., 2022),
the demonstrations are not only useful to show the mapping
between the input and the label but are also important to
clarify the format and the input and label distributions. We
conjecture that in these cases the model mainly relies on
its own intrinsic ability to map the input to the label while
using the demonstrations to learn the other aforementioned
aspects of the task. We highlight that these aspects are sometimes essential to a good performance on the task. Indeed,
on the GSM8K task, thinking step by step is part of the for-

Social Learning: Towards Collaborative Learning with Large Language Models

mat learned from the examples which significantly improves
performance (Wei et al., 2022).
4.1.1. E XTENSIONS TO SHARING EXAMPLES
We additionally investigated two extensions to the above
setup which we only briefly describe here with details described in the appendix.
Teaching to a larger student This ability is natural to social learning since teachers only share text, enabling knowledge to be transferred between different models of different
sizes and architectures. On the other hand, typical gradientbased federated learning methods such as FedAvg (McMahan et al., 2017) and FedOpt (Reddi et al., 2020) require
the same model size and architecture to be used everywhere.
Given that the largest of language models currently can be
only executed on data centers, it would be especially useful
to be able to transfer knowledge back to such models. In our
experiments, we find this to be generally feasible in social
learning, with a small drop in performance compared to
teachers and student being of the same size, as is expected
to be in this more difficult setting. Details and results of this
setup is provided in Appendix G.
Voting aggregator As an example of a more sophisticated
aggregator, we evaluated an aggregator where teachers
vote on their preferred examples. To be able to do this,
teachers keep a hold-out dataset that is used during the
voting process. After teachers generated examples using
their training dataset, the aggregator sends back all received
examples to the teachers to let them vote. The most popular
examples are then used by the student during evaluation.
We find this protocol to improve results for intermediate
values of n, the total number of examples picked by the
aggregator. We refer interested readers to Appendix H for
more details and results.
4.2. Verbal Social Learning: Sharing Instructions
As discussed in Section 2.2.1, sharing an instruction for the
task is another possible method for social learning where the
teachers are asked to generate an instruction that describes
the task. In this work, we only consider the single teacher
case to avoid the need for merging multiple instructions. The
teacher is queried a single time to generate an instruction
based on 8 examples, pointing out any patterns or special
format instructions that it can observe (see the exact prompt
in Figure 2). The generated instruction is directly used as
the prompt for the student. As such, the aggregator in this
case simply forwards the instruction.
We present the results in Table 2 for two teacher models:
PaLM 2-S and OpenAI GPT3.5-Turbo. The table also includes the results for multiple baselines. In particular, we

compare with the empty prompt (zero-shot) performance
as the low bar to showcase the improvement observed from
having an instruction. Since the instruction is generated
using 8 examples, we also compare with the 8-shot performance (without instruction) using the original, private
examples directly as the high bar. Finally, as an alternative,
we also report results on a prompt that we wrote manually
for each task. These prompts are listed in Table 7. While
writing a manual prompt is not a controlled process, we report the results here to provide an approximate of what can
be achieved without using social learning and simply relying on the intuition of the model developer. To simulate the
prompt developers’ limited access to a task’s examples, the
prompts were only tested and tuned with at most 2 examples
from each task.
With the exception of the GSM8K task and the spam detection task with list of classes provided, we observe an
accuracy that is significantly improved in comparison with
zero-shot performance. The most challenging dataset for
generating instruction seems to be GSM8K. We observed
that the main challenge for this task is providing the instruction for the special format of the output which involves
outputting the final answer after four hash (#) signs. In many
of the runs, the models ignore this special format and do not
include it in the instruction which leads to a zero accuracy
performance. Moreover, even in some of the runs where
GPT3.5 generates an instruction which includes the description of the format, the performance is usually below the
manual instruction performance and much lower than sharing original or generated examples. We note that our results
are based on a basic method for generating the instruction.
Indeed, recent work suggests that the instruction can be
significantly improved using more sophisticated generation
methods. For example Yang et al. (2023) report results
comparable to the performance we observe with original
examples by using a feedback loop in the generation process.
We leave exploration of different methods to improve the
instruction as future work. Interestingly, we can observe
that in some tasks, namely Lambada and Random Insertion,
generated artificial examples perform better than generated
instructions whereas in other tasks such as spam detection,
generated instruction obtains a higher accuracy. Still, in all
tasks the performance is lower than the high bar of 8-shot
original examples, suggesting a capacity for improvement.

5. Memorization
In the previous sections of the paper, we discussed how well
teachers can teach students in social learning in terms of
model quality. In this section, we investigate whether the
instructions and examples transferred to students indeed
help reduce private data leakage or not. To this end, we
propose and evaluate metrics to measure how much social

Social Learning: Towards Collaborative Learning with Large Language Models

Method

Lambada

BoolQ

GSM8K

SMSSpam

SMS Spam
(With Class)

Random
Insertion

Zero-Shot
Manual
8-shot Original Examples

69.8
77.5
88.4

68.1
90.2
90.5

0.0
15.6
64.1

14.2
94.0
96.0

92.7
94.2
96.8

22.0
34.9
74.5

8-shot PaLM 2-S Generated Examples
GPT3.5 Generated Instruction
PaLM 2-S Generated Instruction

88.1
82.8
85.1

88.7
90.1
88.7

63.4
4.1
0.0

86.5
85.4
92.9

91.5
95.4
93.4

69.2
59.2
40.4

Table 2. Performance of PaLM 2-S when transferring knowledge using generated instructions. For each dataset, we bold the bestperforming baseline and social learning method. In most cases, the generated instruction improves over directly prompting the model
with the task (zero-shot). We can observe that for some of the tasks such as Lambada and Random Insertion, using generated examples
performs better than using generated instructions whereas the situation is reversed for the spam detection task. The average accuracy
across 5 runs is reported. Table 9 reports the same values with more precision.

learning can memorize sensitive information included in the
private examples.
As a first step, we first investigate how often teachers copy
over one of their private examples verbatim. This can happen when the teacher repeats one of the examples given in
its prompts. On all datasets we found this to be the case in
fewer than 0.1% of cases, meaning the exact data point is
rarely leaked. As shown in Table 6 in the Appendix, the Levenshtein distances between original and generated examples
are also generally high. However, that does not necessarily mean that no sensitive parts of the original example are
memorized, either verbatim or in more subtle ways.
To investigate this further, we adapt the existing Secret
Sharer (Carlini et al., 2019) technique for social learning.
Secret Sharer is an established technique for measuring how
much a given training process leads a model to memorize
some of its training data. It has been used in federated
learning (Thakkar et al., 2021; Hartmann & Kairouz, 2023),
making it an interesting technique to adapt to social learning.
Secret Sharer works by inserting artificial secret data points,
called canaries, into the training data set. Injection of canaries provides access to a known set of secrets that should
not be shared, making it measurable how much the secrets
present in the data are memorized. To implement this, one
canary is randomly sampled from a list containing NSS potential canaries, while the other NSS − 1 data points that
were not sampled serve as comparison elements. In our experiments, we generate canaries containing secret codes and
names. This is done by using random four-digit numbers
for the codes and by taking names from a dataset of the
most common names given to newborns in the US in 2020
(Hugequiz.com, 2021). The codes or names are inserted
into patterns shown in Table 14 in the appendix.
After performing training using the data containing the canary, the score assigned by the model to the canary included

in the data is compared with the scores of the comparison
data points that were not included in the training data. This
metric, called rank, counts the number of comparison examples that get assigned a higher score than the canary that
was actually trained on. Secret Sharer assumes a scoring
function based on the model that assigns a higher score to
examples that the model memorized. Since the rank is a
random variable, the average of the rank across TSS runs is
computed and used for making deductions. For example, if
the model has not memorized the canary, the rank’s distribution would be uniform, leading to an average rank of N2SS .
In the case of perfect memorization, the rank would be 0.
To illustrate the method further, consider the example of
adding the canary The secret code is 1234 to the
training set. After training, we can check how high the
model’s score is in that particular example as opposed to
the same string with different codes. A model that only
learned a high-level pattern, would not assign a significantly
higher score to the string containing the particular code it
was trained on whereas a model that memorized the concrete
data point would.
In standard gradient descent training, the model’s loss for
the example can be used as the score. In social learning,
we do not optimize any numerical loss and do not update
any weights. Instead, the social learning process produces a
string in the form of new examples or an instruction which
can be added to the model’s prompt. Therefore, we use
the following mechanism to compute the score: Given the
final prompt from social learning process and a canary, the
likelihood of that canary as a continuation of the learned
prompt is determined by the model. This value is normalized
by the number of tokens in the canary to make it comparable
to the score of other canaries. This normalized value is used
as the score. We call this scoring function the example
reconstruction likelihood. An example of this can be seen
in Figure 3.

Social Learning: Towards Collaborative Learning with Large Language Models

Figure 3. Example reconstruction likelihood is the score the model
assigns to a generated example (in blue) which follows the original
examples. The score is only computed on the generated example.

Putting everything together, a Secret Sharer experiment in
social learning then works as follows:
1. A canary element and NSS − 1 comparison elements
are sampled.
2. The canary element is inserted into the training dataset
of all teachers.
3. The social learning process is executed, which results
in examples or an instruction generated by the teacher.
4. The example reconstruction likelihood is computed on
(a) The canary element used in training.
(b) The NSS − 1 comparison elements not used in
training.
5. The rank is computed by counting how many of the
comparison elements have a higher likelihood than the
one we trained on.
6. The above process is repeated TSS times and the average rank is returned.
Since each experiment requires performing many social
learning experiments to compute a stable average rank, running this method is costly. Therefore, we only evaluate it
on two of the tasks, namely Lambada and GSM8K. Furthermore, we focus on measuring the memorization for two
different types of secrets, namely numbers (as secret codes)
and names, in the canary elements.
We compare the rank of an included canary with 999 other
not included canaries, i.e. NSS = 1000 and compute the
average over TSS = 100 Secret Sharer experiments.
The results in Table 3 show the mean rank observed in these
experiments. The observed ranks are lower than the value
expected in the case of no memorization, i.e. N2SS = 500.
While this observation suggests that some memorization has
occurred, the average is still quite close to 500 signaling
that the memorization is either subtle or does not happen
often.
To check how often the code and name can be perfectly
reconstructed, we also looked at how often a rank of 0
is observed. Note that in a uniform distribution over the
rank (meaning no memorization happens), this event should
occur N1SS = 0.1% of the time. Table 4 shows that while

Canary

Lambada

GSM8K

Codes
Names

435
463

467
459

Table 3. The average rank across 100 Secret Sharer experiments.

Canary

Lambada

GSM8K

Codes
Names

8
7

3
4

Table 4. How often rank 0 occurs across 100 Secret Sharer experiments. In a random, uniform distribution, we would expect it to
occur once.

this event occurs more often than this baseline in our case,
the ratio is still low. Improving these metrics and bringing
them closer to the no memorization baselines is an important
direction for future work.

6. Future Work
Improving Teaching Process Both for sharing examples
and sharing instructions, our results show there is room for
improvement. Future work could explore other aggregators,
ways of introducing learning loops, or other techniques for
generating instructions or examples.
Generalized Settings and Other Modalities Future
work could also consider more generalized settings, such
as cases where teachers are allowed to communicate with
each other or are available during inference. Instead of
text-based examples and communication, future work can
investigate social learning based on other modalities, such
as image or audio data. These settings introduce other
challenges and require capabilities from the models that are
yet to be perfected.
Alternative Privacy Metrics and Mechanisms While the
privacy experiments using Secret Sharer provide some information about privacy in social learning, we do not consider
them to be exhaustive. Future work could look into different
ways of measuring data leakage in social learning or into
how to add formal guarantees in the form of differential
privacy.

7. Conclusion
In this work, we introduced the social learning framework
which allows language models with access to private data
to transfer knowledge through textual communication while
maintaining the privacy of that data. In this framework,
we identified sharing examples and sharing instructions as

Social Learning: Towards Collaborative Learning with Large Language Models

basic models and evaluated them on multiple tasks. Furthermore, we adapted the Secret Sharer metric to our framework,
proposing a metric for measuring data leakage. The paper
evaluates these methods on several datasets, reports results,
and outlines directions for future work.

Acknowledgements
We would like to thank Victor Cărbune, Zachary Garrett,
Tautvydas Misiunas, Sofia Neata and John Platt for their
comments which greatly improved this paper.

References
Almeida, T. A., Hidalgo, J. M. G., and Yamakami, A. Contributions to the study of sms spam filtering: new collection
and results. In Proceedings of the 11th ACM symposium
on Document engineering, pp. 259–262, 2011.
Alonso, E., D’Inverno, M., Kudenko, D., Luck,
M., and Noble, J.
Learning in multi-agent systems.
The Knowledge Engineering Review, 16
(3):277–284, September 2001.
ISSN 0269-8889,
1469-8005.
doi:
10.1017/S0269888901000170.
URL
https://www.cambridge.org/core/
product/identifier/S0269888901000170/
type/journal_article.
Anil, R., Dai, A. M., Firat, O., Johnson, M., Lepikhin,
D., Passos, A., Shakeri, S., Taropa, E., Bailey, P., Chen,
Z., et al. Palm 2 technical report. arXiv preprint
arXiv:2305.10403, 2023.
Bandura, A. and Walters, R. H. Social learning theory,
volume 1. Englewood cliffs Prentice Hall, 1977.
Brown, T., Mann, B., Ryder, N., Subbiah, M., Kaplan, J. D.,
Dhariwal, P., Neelakantan, A., Shyam, P., Sastry, G.,
Askell, A., et al. Language models are few-shot learners.
Advances in neural information processing systems, 33:
1877–1901, 2020.
Carlini, N., Liu, C., Erlingsson, Ú., Kos, J., and Song,
D. The secret sharer: Evaluating and testing unintended
memorization in neural networks. In 28th USENIX Security Symposium (USENIX Security 19), pp. 267–284,
2019.
Chowdhery, A., Narang, S., Devlin, J., Bosma, M., Mishra,
G., Roberts, A., Barham, P., Chung, H. W., Sutton,
C., Gehrmann, S., Schuh, P., Shi, K., Tsvyashchenko,
S., Maynez, J., Rao, A., Barnes, P., Tay, Y., Shazeer,
N., Prabhakaran, V., Reif, E., Du, N., Hutchinson, B.,
Pope, R., Bradbury, J., Austin, J., Isard, M., Gur-Ari, G.,
Yin, P., Duke, T., Levskaya, A., Ghemawat, S., Dev, S.,
Michalewski, H., Garcia, X., Misra, V., Robinson, K., Fedus, L., Zhou, D., Ippolito, D., Luan, D., Lim, H., Zoph,

B., Spiridonov, A., Sepassi, R., Dohan, D., Agrawal,
S., Omernick, M., Dai, A. M., Pillai, T. S., Pellat, M.,
Lewkowycz, A., Moreira, E., Child, R., Polozov, O., Lee,
K., Zhou, Z., Wang, X., Saeta, B., Diaz, M., Firat, O.,
Catasta, M., Wei, J., Meier-Hellstern, K., Eck, D., Dean,
J., Petrov, S., and Fiedel, N. PaLM: Scaling Language
Modeling with Pathways, October 2022. URL http://
arxiv.org/abs/2204.02311. arXiv:2204.02311
[cs].
Clark, C., Lee, K., Chang, M.-W., Kwiatkowski, T., Collins,
M., and Toutanova, K. Boolq: Exploring the surprising
difficulty of natural yes/no questions. In Proceedings
of the 2019 Conference of the North American Chapter
of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short
Papers), pp. 2924–2936, 2019.
Cobbe, K., Kosaraju, V., Bavarian, M., Chen, M., Jun, H.,
Kaiser, L., Plappert, M., Tworek, J., Hilton, J., Nakano,
R., Hesse, C., and Schulman, J. Training verifiers to solve
math word problems. arXiv preprint arXiv:2110.14168,
2021a.
Cobbe, K., Kosaraju, V., Bavarian, M., Chen, M., Jun,
H., Kaiser, L., Plappert, M., Tworek, J., Hilton, J.,
Nakano, R., Hesse, C., and Schulman, J. Training Verifiers to Solve Math Word Problems, November 2021b. URL http://arxiv.org/abs/2110.
14168. arXiv:2110.14168 [cs].
Deng, Y., Zhang, W., Chen, Z., and Gu, Q. Rephrase and
respond: Let large language models ask better questions
for themselves. arXiv preprint arXiv:2311.04205, 2023.
Du, Y., Li, S., Torralba, A., Tenenbaum, J. B., and
Mordatch, I.
Improving Factuality and Reasoning in Language Models through Multiagent Debate,
May 2023. URL http://arxiv.org/abs/2305.
14325. arXiv:2305.14325 [cs].
Hartmann, F. and Kairouz, P.
Distributed differential privacy for federated learning, 2023.
URL
https://ai.googleblog.com/2023/03/
distributed-differential-privacy-for.
html.
Honovich, O., Shaham, U., Bowman, S. R., and Levy,
O. Instruction induction: From few examples to
natural language task descriptions. arXiv preprint
arXiv:2205.10782, 2022.
Huang, W., Abbeel, P., Pathak, D., and Mordatch, I. Language models as zero-shot planners: Extracting actionable knowledge for embodied agents. In International Conference on Machine Learning, pp. 9118–9147.
PMLR, 2022.

Social Learning: Towards Collaborative Learning with Large Language Models

Hugequiz.com.
Us top 1000 baby names 18802020,
Oct 2021.
URL https://www.
kaggle.com/datasets/darinhawley/
us-top-1000-baby-names-18802020.
Kairouz, P., McMahan, H. B., Avent, B., Bellet, A., Bennis,
M., Bhagoji, A. N., Bonawitz, K., Charles, Z., Cormode,
G., Cummings, R., et al. Advances and open problems in
federated learning. Foundations and Trends® in Machine
Learning, 14(1–2):1–210, 2021.

Parisi, A., Zhao, Y., and Fiedel, N. TALM: Tool Augmented
Language Models, May 2022. URL http://arxiv.
org/abs/2205.12255. arXiv:2205.12255 [cs].
Perez, E., Huang, S., Song, F., Cai, T., Ring, R., Aslanides,
J., Glaese, A., McAleese, N., and Irving, G. Red Teaming Language Models with Language Models, February 2022. URL http://arxiv.org/abs/2202.
03286. arXiv:2202.03286 [cs].

Konečnỳ, J., McMahan, H. B., Yu, F. X., Richtárik, P.,
Suresh, A. T., and Bacon, D. Federated learning: Strategies for improving communication efficiency. arXiv
preprint arXiv:1610.05492, 2016.

Pinsky, Y.
Bard can now connect to your
google apps and services, Sep 2023.
URL
https://blog.google/products/bard/
google-bard-new-features-update-sept-2023/.

Liang, T., He, Z., Jiao, W., Wang, X., Wang, Y., Wang,
R., Yang, Y., Tu, Z., and Shi, S. Encouraging divergent
thinking in large language models through multi-agent
debate. arXiv preprint arXiv:2305.19118, 2023.

Radford, A., Wu, J., Child, R., Luan, D., Amodei, D.,
Sutskever, I., et al. Language models are unsupervised
multitask learners. OpenAI blog, 1(8):9, 2019.

Liu, R., Wei, J., Gu, S. S., Wu, T.-Y., Vosoughi, S., Cui,
C., Zhou, D., and Dai, A. M. Mind’s eye: Grounded
language model reasoning through simulation, 2022.
Liu, Z., Yao, W., Zhang, J., Xue, L., Heinecke, S., Murthy,
R., Feng, Y., Chen, Z., Niebles, J. C., Arpit, D., Xu, R.,
Mui, P., Wang, H., Xiong, C., and Savarese, S. BOLAA:
Benchmarking and Orchestrating LLM-augmented Autonomous Agents, August 2023. URL http://arxiv.
org/abs/2308.05960. arXiv:2308.05960 [cs].
McMahan, B., Moore, E., Ramage, D., Hampson, S., and
y Arcas, B. A. Communication-efficient learning of deep
networks from decentralized data. In Artificial intelligence and statistics, pp. 1273–1282. PMLR, 2017.
Min, S., Lyu, X., Holtzman, A., Artetxe, M., Lewis, M.,
Hajishirzi, H., and Zettlemoyer, L. Rethinking the role of
demonstrations: What makes in-context learning work?
arXiv preprint arXiv:2202.12837, 2022.
Mishra, S., Khashabi, D., Baral, C., and Hajishirzi, H. Crosstask generalization via natural language crowdsourcing
instructions. arXiv preprint arXiv:2104.08773, 2021.
Ndousse, K. K., Eck, D., Levine, S., and Jaques, N. Emergent Social Learning via Multi-agent Reinforcement
Learning. In Proceedings of the 38th International Conference on Machine Learning, pp. 7991–8004. PMLR,
July 2021. URL https://proceedings.mlr.
press/v139/ndousse21a.html. ISSN: 26403498.
Paperno, D., Kruszewski, G., Lazaridou, A., Pham, Q. N.,
Bernardi, R., Pezzelle, S., Baroni, M., Boleda, G., and
Fernández, R. The lambada dataset: Word prediction
requiring a broad discourse context. arXiv preprint
arXiv:1606.06031, 2016.

Rae, J. W., Borgeaud, S., Cai, T., Millican, K., Hoffmann,
J., Song, F., Aslanides, J., Henderson, S., Ring, R.,
Young, S., et al. Scaling language models: Methods,
analysis & insights from training gopher. arXiv preprint
arXiv:2112.11446, 2021.
Rafailov, R., Sharma, A., Mitchell, E., Ermon, S., Manning, C. D., and Finn, C. Direct Preference Optimization: Your Language Model is Secretly a Reward Model,
May 2023. URL http://arxiv.org/abs/2305.
18290. arXiv:2305.18290 [cs].
Reddi, S., Charles, Z., Zaheer, M., Garrett, Z., Rush, K.,
Konečnỳ, J., Kumar, S., and McMahan, H. B. Adaptive
federated optimization. arXiv preprint arXiv:2003.00295,
2020.
Shao, Z., Gong, Y., Shen, Y., Huang, M., Duan, N., and
Chen, W. Synthetic prompting: Generating chain-ofthought demonstrations for large language models. arXiv
preprint arXiv:2302.00618, 2023.
Thakkar, O. D., Ramaswamy, S., Mathews, R., and Beaufays, F. Understanding unintended memorization in language models under federated learning. In Proceedings
of the Third Workshop on Privacy in Natural Language
Processing, pp. 1–10, 2021.
Wang, L., Ma, C., Feng, X., Zhang, Z., Yang, H., Zhang, J.,
Chen, Z., Tang, J., Chen, X., Lin, Y., et al. A survey on
large language model based autonomous agents. arXiv
preprint arXiv:2308.11432, 2023.
Wei, J., Bosma, M., Zhao, V. Y., Guu, K., Yu, A. W., Lester,
B., Du, N., Dai, A. M., and Le, Q. V. Finetuned language models are zero-shot learners. arXiv preprint
arXiv:2109.01652, 2021.

Social Learning: Towards Collaborative Learning with Large Language Models

Wei, J., Wang, X., Schuurmans, D., Bosma, M., Xia, F.,
Chi, E., Le, Q. V., Zhou, D., et al. Chain-of-thought
prompting elicits reasoning in large language models.
Advances in Neural Information Processing Systems, 35:
24824–24837, 2022.
Yang, C., Wang, X., Lu, Y., Liu, H., Le, Q. V., Zhou, D., and
Chen, X. Large language models as optimizers. arXiv
preprint arXiv:2309.03409, 2023.
Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan,
K., and Cao, Y. React: Synergizing reasoning and acting
in language models, 2023.
Zamani, H., Trippas, J. R., Dalton, J., Radlinski, F.,
et al. Conversational information seeking. Foundations
and Trends® in Information Retrieval, 17(3-4):244–456,
2023.
Zeng, A., Attarian, M., Ichter, B., Choromanski, K., Wong,
A., Welker, S., Tombari, F., Purohit, A., Ryoo, M.,
Sindhwani, V., Lee, J., Vanhoucke, V., and Florence,
P. Socratic Models: Composing Zero-Shot Multimodal
Reasoning with Language, May 2022. URL http://
arxiv.org/abs/2204.00598. arXiv:2204.00598
[cs].

A. Additional Simplifying Constraints
We impose the following constraints on the communications
between the teachers and the student in our social learning
methods:
1. Teachers do not directly communicate with each
other: teachers are not able to send text messages
to each other either directly or via the student. This
constraint removes the effect of planning and debate
capabilities of the language models.
2. The query to all teachers is the same: the student
always sends the same message to all the teachers. This
constraint removes the need for the student to analyze
teacher’s knowledge of the task and react based on it.
3. The conversation flow is fixed: the tasks requested
from the teachers are fixed in advance and do not
depend on the conversation. For example, teachers
might initially be asked to describe the task and then
be prompted with a description from multiple teachers to produce a consolidated version. However, the
student will not ask for clarifications about a specific
part of the description that is vague. This constraint
removes the requirement of models to generate instructions during learning as the prompts can be manually
fixed.

To define a social learning method, we have to define the
response functions of teachers and the student:
• Teachers’ Response: We need to define Ti (M ) which
is the message sent to the student in response to the
message M received from the student. For example if
M is a question, Ti (M ) can be the answer based on a
teacher’s private data.
• Student’s Response: Since the student sends the
same message to all the teachers, we can assume
that it replies only after receiving the update from
all teachers. The student responds to the message
by possibly sending a new message to the teachers
and creating an updated prompt PSNew . As such, to
define the response function of the student we need
to specify RG (MT1 , MT2 , . . . , MTm , PScurrent ) as a pair
(PSnew , Mnext ).
The training starts by querying the student to generate the
first message to the teachers. Afterwards, the teachers and
student alternate responding to each other’s messages. Once
the training is completed, the final prompt can be used by
the student during inference.

B. Datasets
In this section, we provide a summary for each of the tasks
in our evaluation suite. The exact format used to convert
instances of each task to a string given to the language
models is provided in Table 5.
Spam Detection We use the SMS Spam dataset (Almeida
et al., 2011) which contains a collection of SMS messages
classified into spam and not spam classes. We randomly
under-sample the dataset (without replacement) to make it
balanced. We use a fixed 500 element subset of the undersampled dataset as the test-set. To convert each example to
string we use a basic format which starts with the message’s
text followed by the class of the message. However, using
this format, it is infeasible for the model to perform well
when the list of classes are not known. For example, this
can happen in the zero-shot or one-shot case where the set
of examples contain at most one of the classes. Therefore,
we also experiment with another format that provides a list
of classes (spam or not spam) before stating the label for
the example. The exact format is shown in Table 5. While
in the literature normal messages are usually referred to as
"ham", we use "not spam" in this work.
Lambada The Lambada dataset (Paperno et al., 2016) is
a Cloze task where the last word of a sentence is removed
and the task is recovering the word based on the context. In
this work, we use the same format used to evaluate GPT-2
(Radford et al., 2019).

Social Learning: Towards Collaborative Learning with Large Language Models

Dataset
SMS Spam (Base)
SMS Spam (Class List)

Example Format
Text: <Message>
Class: <spam/not spam>
Text: <Message>
Class ("spam" or "not spam"): <spam/not spam>
Fill in blank:

Lambada
<Text without last word> ____ -> <last word>
BoolQ

<Context>
Question: <Question>
Answer: <Answer>

GSM8K

Question: <Question>
Answer: <Step By Step Reasoning>
#### <Final Answer>

Random Insertion

<Word With Punctuations> = <Original Word>

Table 5. Formats used to convert dataset elements to text. The segments enclosed in < and > correspond to placeholders replaced by values
from each example.

Boolean Questions BoolQ (Clark et al., 2019) is a dataset
of a context, question, and answer triplets. The model is
asked to provide a yes or no answer to the question based
on the given context.
Grade School Math We evaluate on the GSM8K dataset
(Cobbe et al., 2021a) which is a set of mathematical questions annotated with the final answer as well as the trace
to reach the answer. Solving mathematical problems is a
known challenging task for language models (Rae et al.,
2021). Therefore, this task is especially difficult for generating artificial examples since generating a correct example
requires solving the task in the process.
Random Insertion We also adapt the random insertion
artificial dataset from Brown et al. (2020). In this dataset,
a random punctuation mark is inserted after each character
of a word. The answer to the task is the original word without the punctuation marks. We choose this dataset as the
results in Brown et al. (2020) show noticeable improvement
from having more examples in the few-shot prompt, signaling the importance of having access to good examples or
instructions.

C. Significance Testing
We apply a permutation test to understand the significance
of our results in comparison to different baselines. In particular, to test the significance of the difference observed in
the accuracy of a certain method in comparison to a given

baseline, we first combine all the example and output pairs
generated by either the baseline or the considered method.
We randomly permute the aforementioned pile and break it
into a pile with the same number of pairs as the baseline and
another pile with the same number of pairs as the considered
method. We compute the accuracy of each pile and measure
the difference. Repeating this process 104 times allows us
to obtain an approximate distribution of the observed difference if the baseline and the considered method’s output
are not significantly different. We use this distribution to
compute the probability of the real difference in accuracy
between the baseline and the considered method and report
that as the p-value. When discussing results, if the p-value
is below the threshold 0.05 we say the result is significant
and state that we could not observe a significant difference
otherwise.

D. Distance of a Generated Example to its
Generation Prompt
We define a distance metric in order to take into account
that the student’s prompt can contain multiple examples. In
particular, we compute the minimum Levenshtein Distance
(with substitution not allowed) to any substring1 of the student’s prompt. To allow comparability, we normalize this
value by the generated example’s length and call it the nor1
for a string s with n characters, a substring is defined by a
pair (i, j) (1 ≤ i ≤ j ≤ n) and refers to the string containing the
i-th to j-th characters of s

Social Learning: Towards Collaborative Learning with Large Language Models

malized distance. The results are reported in Table 6. The
average normalized distance is typically large, indicating
that the example is sufficiently different from examples in
the prompt. We can also observe that the distance is lower
than others in some tasks, namely spam detection and random insertion. We point out that in random insertion almost
half the characters are punctuation marks which are limited
and can be expected to overlap more often, lowering the
distance. Furthermore, the SMS texts are usually short and
imitating the format of a spam message can lead to a low
distance. That being said, generating novel examples for
these tasks may also be more challenging for the model.

E. Manual Prompts
The manually written prompts are reported in Table 7.

F. Detailed Experiment Results
The detailed experiment results with standard errors and
p-values are reported in Table 8.

Solve the task described below. You may
output additional text however the
final answer should be marked with
prefix #### followed by a space.
Figure 4. Manually added prefix instruction to specify GSM8K
format. No instruction to perform CoT is given.

since teachers only share text, enabling knowledge to be
transferred between different models of different sizes and
architectures. On the other hand, typical gradient-based federated learning methods such as FedAvg (McMahan et al.,
2017) and FedOpt (Reddi et al., 2020) require the same
model size and architecture to be used everywhere. Given
that the largest of language models currently can be only
executed on data centers, it would be especially useful to be
able to transfer knowledge back to such models.
Table 10 contains the results for teaching a larger student
model (PaLM 2-S using smaller teacher models, PaLM 2XS). As the baseline we compare using original examples
either at the student (high bar) or at the teachers (low bar).
For all tasks except spam detection we can observe significant improvement over using the original examples from
the small model. The gap is especially large for smaller
values of n (e.g. 1-shot) where an improvement can be observed on all tasks. While this improvement is expected
given the larger size of the student’s model, it highlights the
success of generated examples to transfer the knowledge
and demonstrates the benefit of having such mechanism.
For larger values of n, the small model already performs
quite well on the spam detection task and as a result, no
significant improvement from the knowledge transfer can
be observed in these cases. Noticeably, in most cases for
Lambada and GSM8K no significant difference could be
observed between using the artificially generated examples
and using private examples directly at the student.

The results contain cases where the deviation of performance across the runs is quite high, demonstrated by the
high reported standard error. We observe that this can happen for multiple reasons. For the spam detection task, this
mainly happens when the basic format is used. In this case,
the list of classes are unknown to the model and, especially
when the number of examples is low, it is possible that the
model only receives examples from a single class. We observe that if this class is the spam class, the model uses
"ham" to classify non spam messages which is considered
the wrong class, thus reducing the accuracy significantly.
This is interesting as ham is the terminology typically used
in the literature whereas here we use the not spam class.
This issue is noticeably improved when the list of classes
is provided to the model. High variance is also observed
in Boolean Questions. As mentioned earlier, in some runs
most generated examples selected by the aggregator were
not a yes/no question, which leads to a poor performance.
Fortunately, the likelihood for generating such bad examples is low, and such a scenario mainly happens when the
number of selected examples n is small. As a result, the
high standard error can only be seen for small values of n.
We can also observe a high standard error in the random
insertion task. However, this standard error is also visible in
the baseline, suggesting that the model is in general more
sensitive to the choice of examples in this task. The root
cause of this sensitivity is not clear.

We discussed the challenges encountered when generating
new examples for the spam detection and Boolean Question
tasks in Section F. We observe that when using a smaller
model, the same challenges persist and are sometimes exacerbated. As a result, the generated examples can sometimes
perform poorly as can be observed for 1-shot inference in
the Boolean Questions task and 2-shot inference for the
spam detection task without list of classes. In these cases, a
high standard error is typically observed as the model only
sometimes fails to generate good examples.

G. Teaching a Larger Student Model

H. Voting Aggregator

In this section, we consider the ability to transfer knowledge
to a larger model. This ability is natural to social learning

In this section we explore using a more sophisticated aggregator than the random aggregator and assess its effect on
performance. In particular, we consider an aggregator that

Social Learning: Towards Collaborative Learning with Large Language Models

n

Lambada

BoolQ

GSM8K

SMS Spam

SMS Spam
(With Class)

Random
Insertion

1
2
4
8
16

0.78
0.76
0.77
0.76
0.77

0.85
0.84
0.83
0.83
0.83

0.79
0.82
0.80
0.81
0.81

0.47
0.63
0.58
0.56
0.60

0.47
0.46
0.43
0.43
0.47

0.58
0.56
0.61
0.61
0.59

Table 6. Average of the normalized distance between each generated example by PaLM 2-S and the prompt used to generate it. Distance
is defined as the minimum Levenshtein distance (substitution not allowed) to any substring of the prompt, making the maximum possible
distance equal to the generated example’s length. Normalization is done by the generated example’s length. It can be seen that the average
is usually quite high, suggesting that many of the generated examples are significantly different from the real ones provided in the prompt.

adheres to the following voting process:
1. Before beginning the generation process, the aggregator asks each teacher to create a evaluation dataset by
holding out a subset of its data, not used for generating
the artificial examples.
2. After each generation, as specified in Section 2.2.2, the
aggregator is queried with a set of artificially generated
candidates. As a response, the aggregator sends the list
of all candidates to all teachers asking them to select
the best candidate.
3. Each teacher computes the likelihood of each candidate
separately as a continuation of its held-out evaluation
dataset normalized by the length of that candidate and
votes for the candidate that scores the highest. The
teachers’ votes are sent back to the aggregator.
4. The aggregator selects the candidate with the most
votes.
As before, the process of generating candidates, voting and
selecting the highest voting candidate is repeated until the
desired number of examples is generated to be included in
the student’s prompt. We call this aggregator the voting
aggregator.
We compare the performance of using the voting aggregator
against using the random aggregator in Table 12. We observe that the benefit of using the voting aggregator varies
depending on n. For very small values of n (e.g. n = 1) the
performance is even worse than using the random aggregator for some tasks. Though the observed difference is not
always significant, this may suggest that the top-voted example, though possibly better formatted, might not be sufficient
to fully describe the task as a single example which encourages looking for better aggregation mechanisms. At the
other end of the spectrum, we observe no significant difference for very high values of n, e.g. n = 16. We hypothesize
that in this case given the large number of examples, these
examples contain most of the information even when they

are selected randomly. However, for middle range values of
n where the choice of the examples is important and there is
some freedom in using different combinations, we observe
a more pronounced difference when using a voting aggregator. In this case, for most of the tasks an improvement
is observed in the accuracy (though not always significant)
when using the voting aggregator. The exception is the spam
detection task where using the voting aggregator tends to
hurt the performance regardless of the magnitude of n. We
noticed that this is because when using voting, the bias of
the model toward one class as discussed in the previous
section becomes amplified. Our results suggest that additional research is required to find better aggregators that can
improve the performance further which we leave as an area
for future work.
In the case of the spam dataset, the random aggregator does
better than the voting aggregator. This is because language
models are inherently biased towards non-spam examples,
meaning the voting process leads to a class imbalance.
The choice of the aggregator is thus highly datasetdependent. When the quality of candidate examples and
instructions is high, random selection does well. When it is
not, it becomes more important to pick generated examples
well.

I. Canary Designs
Table 14 shows the canaries we use for Secret Sharer experiments.

Social Learning: Towards Collaborative Learning with Large Language Models

Dataset

Manual Instruction

SMS Spam

For the following sms message, determine if it
is a spam (e.g. sent by a bot containing
advertisement, phishing, spam, etc.) or a real
message (sent by a human) by classifying the
message into "spam" and "not spam" classes.

Lambada

The last word of the last sentence in a passage
has been removed. Write the missing word (which
is marked by four underscores) after the arrow
->.

BoolQ

A passage is given followed by a question.
Answer the given question with a simple yes or
no based on the given passage.

GSM8K

Solve the following math questions. Think step
by step and write the steps in your answer. When
you are done write the final answer write it (a
single number) marked with the prefix ####
followed by a space. This answer will be autograded so take extra care to follow this format.
Do not print anything after the final answer.

Random Insertion

A random punctuation mark (or a space) has been
inserted after each character of a word. The
result is written on the left hand side of the
equation below and the right hand side contains
the original word.

Table 7. Manually written instructions used for each task to establish a baseline.

Social Learning: Towards Collaborative Learning with Large Language Models

n

Type

Lambada

BoolQ

GSM8K

SMS Spam

SMS Spam
(With Class)

Random
Insertion

0

-

69.80(0.00)

68.10(0.00)

0.00(0.00)a

14.19(0.00)

92.70(0.00)

22.00(0.00)

1

Original
Generated

86.68(0.48)
86.65(0.44)

89.84(0.10)
70.46(7.19)

63.59(0.25)
63.87(0.76)

59.10(7.62)
90.22(0.57)

94.25(0.27)
92.55(0.40)

55.56(3.12)
53.58(7.89)

p-value

0.4895

0.0000

0.3708

0.0000

0.0023

0.0236

Original
Generated

87.30(0.44)
86.70(0.41)

90.12(0.03)
88.63(0.77)

64.20(0.28)
63.23(0.60)

77.15(9.96)
88.17(0.74)

94.87(0.25)
92.15(0.63)

70.04(3.19)
65.94(1.75)

p-value

0.2069

0.0000

0.1267

0.0000

0.0000

0.0000

Original
Generated

87.56(0.63)
87.98(0.43)

90.44(0.07)
85.54(3.87)

63.59(0.27)
63.58(0.48)

86.75(8.28)
87.77(0.75)

95.43(0.53)
90.19(0.81)

69.74(2.55)
69.72(2.42)

p-value

0.2809

0.0000

0.5000

0.0990

0.0000

0.5000

Original
Generated

88.36(0.54)
88.05(0.27)

90.53(0.07)
88.73(0.88)

64.05(0.23)
63.38(0.47)

96.02(0.27)
86.45(0.88)

96.75(0.11)
91.51(0.97)

74.50(1.15)
69.22(3.42)

p-value

0.3246

0.0000

0.2164

0.0000

0.0000

0.0000

Original
Generated

88.40(0.67)
89.04(0.23)

90.42(0.08)
89.94(0.08)

63.55(0.28)
63.71(0.35)

96.48(0.17)
87.98(1.18)

97.02(0.07)
91.08(1.57)

73.52(1.11)
72.36(1.01)

p-value

0.1747

0.0756

0.4266

0.0000

0.0000

0.1023

2

4

8

16

a
GSM8K uses a special format to mark the answer. The model inevitably always fails when no instruction or examples
are provided to it to clarify this special format. Adding the prefix stated in Figure 4 to clarify the format yields accuracy
16.38%.

Table 8. Accuracies and p-values reported in Table 1 with more precision. Standard error of the mean is reported in parentheses.

Method

Lambada

BoolQ

GSM8K

SMS Spam

SMS Spam
(With Class)

Random
Insertion

Zero-Shot
Manual

69.80
77.45

68.10
90.18

0.00
15.62

14.19
93.95

92.70
94.22

22.00
34.9

8-shot Original Examples
8-shot Artificial Examples

88.36(0.54)
88.05(0.27)

90.53(0.07)
88.73(0.88)

64.05(0.23)
63.38(0.47)

96.02(0.27)
86.45(0.88)

96.75(0.11)
91.51(0.97)

74.50(1.15)
69.22(3.42)

GPT3.5 Generated Inst.
PaLM 2-S Generated Inst.

82.81(1.87)
85.12(0.91)

90.12(0.07)
88.74(1.36)

4.11(2.27)
0.00(0.00)

85.38(8.70)
92.90(0.04)

95.38(0.37)
93.44(0.39)

59.22(4.76)
40.38(9.88)

Table 9. Accuracies and p-values reported in Table 2 with more precision. Standard error of the mean is reported in parentheses.

Social Learning: Towards Collaborative Learning with Large Language Models

n

Type

Student

Lambada

BoolQ

GSM8K

SMSSpam

SMS Spam
(With Class)

Random
Insertion

1

Original
Original
Generated
PaLM2-XS

PaLM 2-XS
PaLM 2-S

74.6
86.7

81.1
89.8

9.3
63.6

61.8
59.1

54.3
94.3

11.8
55.6

PaLM 2-S

86.7

72.2 *

57.2 *

75.9 *

92.4 *

50.9 *

Original
Original
Generated
PaLM2-XS

PaLM 2-XS
PaLM 2-S

73.7
87.3

80.9
90.1

16.0
64.2

72.2
77.2

75.1
94.9

19.9
70.0

PaLM 2-S

87.8

89.8

63.6

59.7 *

87.9 *

66.1 *

Original
Original
Generated
PaLM2-XS

PaLM 2-XS
PaLM 2-S

81.5
87.6

81.1
90.4

19.2
63.6

90.4
86.8

94.9
95.4

25.1
69.7

PaLM 2-S

88.1

82.8 *

63.9

94.1 *

93.8 *

51.5 *

Original
Original
Generated
PaLM2-XS

PaLM 2-XS
PaLM 2-S

86.2
88.4

81.9
90.5

18.7
64.1

95.7
96.0

96.5
96.8

31.4
74.5

PaLM 2-S

89.1

90.2

63.6 *

94.6 *

96.1

63.3 *

Original
Original
Generated
PaLM2-XS

PaLM 2-XS
PaLM 2-S

87.3
88.4

82.6
90.4

17.7
63.6

96.3
96.5

96.2
97.0

30.2
73.5

PaLM 2-S

89.2

89.1 *

63.8

94.6 *

94.0 *

61.8 *

2

4

8

16

Table 10. Performance of teaching a larger student model. The performance of an PaLM 2-XS student using original examples is reported
as the low bar baseline whereas the performance using original examples and PaLM 2-S student constitutes the high bar baseline. A star
marks statistically significant results from the high bar baseline. We bold cells where no statistically significant difference was detected to
emphasize that in many cases the examples generated using social learning perform as well as the original ones. The average accuracy
across 5 runs is reported. Table 11 reports the same values with more precision.

Social Learning: Towards Collaborative Learning with Large Language Models

n

1

2

4

8

16

Type

Student

Lambada

BoolQ

GSM8K

SMS Spam

SMS Spam
(With Class)

Random
Insertion

Original
Original

PaLM 2-XS
PaLM 2-S

74.61(2.15)
86.68(0.48)

81.05(1.02)
89.84(0.10)

9.28(2.04)
63.59(0.25)

61.75(4.55)
59.10(7.62)

54.30(1.88)
94.25(0.27)

11.80(3.37)
55.56(3.12)

86.72(0.72)

72.17(6.46)

57.21(4.83)

75.94(7.89)

92.42(1.51)

50.92(3.25)

0.4883

0.0000

0.0000

0.0000

0.0012

0.0000

73.65(3.22)
87.30(0.44)

80.94(0.98)
90.12(0.03)

16.03(0.26)
64.20(0.28)

72.15(8.16)
77.15(9.96)

75.11(9.25)
94.87(0.25)

19.94(2.60)
70.04(3.19)

87.84(0.53)

89.75(0.15)

63.55(0.58)

59.73(6.78)

87.88(3.55)

66.10(1.25)

0.2240

0.1346

0.2211

0.0000

0.0000

0.0000

81.48(2.90)
87.56(0.63)

81.11(0.22)
90.44(0.07)

19.15(0.65)
63.59(0.27)

90.43(1.41)
86.75(8.28)

94.92(0.66)
95.43(0.53)

25.14(1.94)
69.74(2.55)

88.05(0.26)

82.82(4.48)

63.85(0.64)

94.09(0.44)

93.87(0.51)

51.46(0.43)

0.2372

0.0000

0.3846

0.0000

0.0019

0.0000

86.20(0.43)
88.36(0.54)

81.90(0.27)
90.53(0.07)

18.61(0.44)
64.05(0.23)

95.73(0.59)
96.02(0.27)

96.45(0.23)
96.75(0.11)

31.44(2.43)
74.50(1.15)

89.12(0.11)

90.18(0.08)

62.64(0.77)

94.62(0.29)

96.13(0.30)

63.26(2.46)

0.1263

0.1511

0.0497

0.0029

0.0844

0.0000

87.26(0.24)
88.40(0.67)

82.62(0.35)
90.42(0.08)

17.68(0.45)
63.55(0.28)

96.34(0.35)
96.48(0.17)

96.16(0.39)
97.02(0.07)

30.22(1.70)
73.52(1.11)

89.18(0.33)

89.08(0.99)

63.75(0.71)

94.62(0.47)

93.95(1.11)

61.76(3.49)

0.1196

0.0000

0.4120

0.0002

0.0000

0.0000

Generated
PaLM 2-S
PaLM2-XS
p-value

Original
Original

PaLM 2-XS
PaLM 2-S

Generated
PaLM 2-S
PaLM2-XS
p-value

Original
Original

PaLM 2-XS
PaLM 2-S

Generated
PaLM 2-S
PaLM2-XS
p-value

Original
Original

PaLM 2-XS
PaLM 2-S

Generated
PaLM 2-S
PaLM2-XS
p-value

Original
Original

PaLM 2-XS
PaLM 2-S

Generated
PaLM 2-S
PaLM2-XS
p-value

Table 11. Accuracies and p-values reported in Table 10 with more precision. Standard error of the mean is reported in parentheses.

n

Method

Lambada

BoolQ

GSM8K

SMSSpam

SMS Spam
(With Class)

Random
Insertion

1

Random
Voting

86.7
86.5

70.5
86.6 *

63.9
60.5 *

90.2
87.3 *

92.6
93.2

53.9
56.6 *

2

Random
Voting

86.7
87.9 *

88.6
85.8 *

63.2
64.8 *

88.2
83.7 *

92.2
88.1 *

65.9
67.8 *

4

Random
Voting

88.0
88.2

85.5
89.8 *

63.6
64.8

87.8
84.1 *

90.2
91.1

69.7
72.9 *

8

Random
Voting

88.1
88.2

88.7
89.5 *

63.4
64.0

86.5
84.8 *

91.5
89.5 *

69.2
71.4 *

16

Random
Voting

89.0
88.8

89.9
89.7

63.7
63.5

88.0
87.9

91.1
89.4 *

72.4
72.8

Table 12. Comparison of the performance of PaLM 2-S when using the voting and random aggregators. A star marks statistically
significant results from the random to the voting aggregator according to the permutation test. We bold the cells that are better and have
statistical significance. The change in performance when using the voting aggregator seems to depend on the value of n. While for the
large values of n the results do not change and the random aggregator performs better for the small values of n, middle values of n benefit
from using the voting aggregator. The exception is the spam detection task where using a voting aggregator always reduces performance,
possibly due to the bias of model towards not spam messages. The average accuracy across 5 runs is reported. Table 13 reports the same
values with more precision.

Social Learning: Towards Collaborative Learning with Large Language Models

n

Method

Lambada

BoolQ

GSM8K

SMS Spam

SMS Spam
(With Class)

Random
Insertion

1

Random
Voting

86.65(0.44)
86.50(0.28)

70.46(7.19)
86.63(2.60)

63.87(0.76)
60.52(1.07)

90.22(0.57)
87.31(0.61)

92.55(0.40)
93.15(0.24)

53.58(7.89)
56.56(3.66)

p-value

0.3122

0.0000

0.0000

0.0001

0.1711

0.0019

Random
Voting

86.70(0.41)
87.87(0.28)

88.63(0.77)
85.80(2.81)

63.23(0.60)
64.75(0.33)

88.17(0.74)
83.74(2.19)

92.15(0.63)
88.06(1.71)

65.94(1.75)
67.84(1.29)

p-value

0.0001

0.0000

0.0367

0.0000

0.0000

0.0228

Random
Voting

87.98(0.43)
88.18(0.33)

85.54(3.87)
89.76(0.22)

63.58(0.48)
64.82(0.42)

87.77(0.75)
84.11(1.94)

90.19(0.81)
91.05(0.96)

69.72(2.42)
72.90(2.07)

p-value

0.2408

0.0000

0.0691

0.0000

0.1127

0.0001

Random
Voting

88.05(0.27)
88.22(0.20)

88.73(0.88)
89.53(0.30)

63.38(0.47)
64.03(0.32)

86.45(0.88)
84.78(1.96)

91.51(0.97)
89.52(1.12)

69.22(3.42)
71.36(0.98)

p-value

0.2809

0.0092

0.2216

0.0230

0.0019

0.0098

Random
Voting

89.04(0.23)
88.76(0.25)

89.94(0.08)
89.65(0.09)

63.71(0.35)
63.53(0.36)

87.98(1.18)
87.85(3.04)

91.08(1.57)
89.44(1.26)

72.36(1.01)
72.82(2.18)

p-value

0.1613

0.1956

0.4195

0.4427

0.0089

0.3116

2

4

8

16

Table 13. Accuracies and p-values reported in Table 12 with more precision. Standard error of the mean is reported in parentheses.

Dataset

LAMBADA

GSM8K

Codes

Names

The secret ____ is 1234 -> code

<name> was on the way to buy
bread at the bakery. On the way
to the bakery he came across a
dog. Instead of continuing to
the ____ <name> followed the dog.
-> bakery

The first secret code is 1234.
The second secret code is 5678.
What is the product of the
secret codes?
The product is 1234 * 5678 =
<<<1234 * 5678>>>
#### 7006652

<name> went to the bakery to buy
two dozen cookies. <name> then
shared the cookies equally with
five friends. How many cookies
did each person get?
There are 24 cookies and 6
people, so each person got 24 /
6 = <<24 / 6>> cookies.
#### 4

Table 14. The canary patterns used to generate the canaries for each dataset.
