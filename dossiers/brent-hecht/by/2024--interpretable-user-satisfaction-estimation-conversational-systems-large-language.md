---
title: "Interpretable User Satisfaction Estimation for Conversational Systems with Large Language Models"
person: brent-hecht
attendance: unconfirmed
section: by
type: conference-paper
year: 2024
date: 2024-01-01
venue: "Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (ACL 2024)"
authors: "Ying-Chun Lin, Jennifer Neville, Jack Stokes, Longqi Yang, Tara Safavi, Mengting Wan, Scott Counts, Siddharth Suri, Reid Andersen, Xiaofeng Xu, Deepak Gupta, Sujay Kumar Jauhar, Xia Song, Georg Buscher, Saurabh Tiwary, Brent Hecht, Jaime Teevan"
source_url: https://doi.org/10.18653/v1/2024.acl-long.598
fulltext_url: https://arxiv.org/pdf/2403.12388
openalex_id: W4402672009
doi: https://doi.org/10.18653/v1/2024.acl-long.598
oa_status: gold
cited_by_count: 15
retrieved: 2026-08-13
content: full-text
notes: "OpenAlex duplicate/preprint records: https://openalex.org/W4393027244 (preprint, 2024); Full text retrieved from the open-access PDF at https://arxiv.org/pdf/2403.12388 (pdftotext; PDF not stored); full text is the arXiv preprint version of this work"
---

# Interpretable User Satisfaction Estimation for Conversational Systems with Large Language Models

## Full text

Interpretable User Satisfaction Estimation for
Conversational Systems with Large Language Models
Ying-Chun Lin∗‡ , Jennifer Neville∗† , Jack W. Stokes∗† , Longqi Yang∗† ,
Tara Safavi† , Mengting Wan† , Scott Counts† , Siddharth Suri† ,
Reid Andersen† , Xiaofeng Xu† , Deepak Gupta† , Sujay Kumar Jauhar† ,
Xia Song† , Georg Buscher† , Saurabh Tiwary† , Brent Hecht† , Jaime Teevan†
†
Microsoft Corporation, ‡ Purdue University

arXiv:2403.12388v2 [cs.IR] 9 Jun 2024

Abstract
Accurate and interpretable user satisfaction estimation (USE) is critical for understanding,
evaluating, and continuously improving conversational systems. Users express their satisfaction or dissatisfaction with diverse conversational patterns in both general-purpose (ChatGPT and Bing Copilot) and task-oriented (customer service chatbot) conversational systems.
Existing approaches based on featurized ML
models or text embeddings fall short in extracting generalizable patterns and are hard to interpret. In this work, we show that LLMs can
extract interpretable signals of user satisfaction
from their natural language utterances more
effectively than embedding-based approaches.
Moreover, an LLM can be tailored for USE via
an iterative prompting framework using supervision from labeled examples. Our proposed
method, Supervised Prompting for User satisfaction Rubrics (SPUR), not only has higher
accuracy but is more interpretable as it scores
user satisfaction via learned rubrics with a detailed breakdown.

1

Introduction

General-purpose conversational systems such as
ChatGPT and Copilot are revolutionizing how people live and work. Understanding when and why
users are satisfied or dissatisfied is critical for the
continuous improvement of these systems. It helps
system developers identify areas of improvements,
conduct effective A/B experiments, and optimize
underlying models. Unsurprisingly, developing
machine learning models for User Satisfaction Estimation (USE) (Hu et al., 2023; Kachuee et al.,
2021a; Song et al., 2019; Bodigutla et al., 2019,
2020) has captured significant attention from the
research community.
∗

These corresponding authors contributed equally to this work.
Email: lin915@purdue.edu, jenneville@microsoft.com, jstokes@microsoft.com, longqi.yang@microsoft.com

Figure 1: Illustration of user utterances with satisfaction
patterns (green) and dissatisfaction patterns (red).

When estimating user satisfaction, simply classifying that a user is satisfied or dissatisfied is insufficient. Understanding the reason why a user is satisfied or dissatisfied is just as valuable. For example,
frequent query reformulation presents opportunities for prompt recommendation and conversations
where users explicitly correct a bot’s mistakes can
suggest examples for model alignment. See Figure 1 for an illustration. However, most existing
work has focused on improving classification accuracy and has overlooked interpretability. Representation learning-based approaches (Song et al.,
2023; Deng et al., 2022; Ye Fanghua, 2023) are
relatively opaque due to their use of neural models (e.g., embeddings) and thus offer little insight
into conversational patterns that indicate satisfaction/dissatisfaction. Similar limitations apply to reward models for training LLMs, e.g., RLHF (Christiano et al., 2017) and RLAIF (Bai et al., 2022).
In this case, the learned model produces a continuous “reward” score that aims to distinguish outputs
that a human prefers without explaining why a conversation has a higher score than others. To our
knowledge, these reward models have not been directly used for USE, but we treat it as a baseline

due to their ability to rank outputs with respect to
human preferences.
Some prior work addressed the interpretation
needs of USE via featurized ML models. Examples include Walker et al. (1997), which evaluated
user satisfaction based on human-annotated features assessing task success and dialogue costs, and
Bodigutla et al. (2019), which proposed domainindependent features that evaluate response quality.
However, the growth of LLM-based conversational
systems (e.g., ChatGPT, Bing Copilot) means user
queries in conversational systems may now be
across multiple domains and intents (e.g., taskoriented, QA, chitchat). As such, approaches based
on domain-specific features have limited generalizability to these diverse conversational patterns (Deriu et al., 2021).
In this work, we make the key observation that
LLMs can achieve both high classification accuracy and fine-grained interpretability at the same
time – through their ability to reason about user
conversational patterns and identify salient pattern
classes that generalize and produce accurate predictions. We propose Supervised Prompting for User
satisfaction Rubrics (SPUR). We consider a fewshot scenario, where a small number of training
examples are available, and develop a supervised,
iterative prompting framework that uses an LLM
to (1) extract signals of satisfaction from user utterances in a labeled training set, (2) summarize
the reasons into rubrics for identifying satisfaction/dissatisfaction conversational patterns, and (3)
apply the rubrics to predict satisfaction labels on
unseen conversations.
In addition to being more accurate, our approach
provides an interpretable rubric for understanding
the conversational patterns that indicate user satisfaction/dissatisfaction. Notably, our approach can
be used to learn SAT/DSAT patterns automatically
for different conversational systems. In our experimental results, we show the distributions of
patterns in different types of systems and demonstrate how these patterns (1) correlate to overall
user satisfaction, and (2) differ across domains.
Moreover, we show that we can scale the application of the learned rubrics in two ways. First, we
show that we can distill individual rubric items into
an embedding-based model that can be applied at
scale without the need for LLM prompting. Next,
we show that we can add rubric items as features
to an embedding-based model to increase the accuracy of embedding-only models on datasets with

more available training data.
The main contributions of our work include:
• We propose Supervised Prompting for User
satisfaction Rubrics (SPUR), a novel framework for estimating user satisfaction in conversational systems with LLMs.
• We show the SPUR prompting process extracts patterns into clear and interpretable
rubrics that guide the LLM to classify user
satisfaction and show that diverse rubrics are
learned automatically for different domains.
• We show SPUR outperforms existing methods across different types of conversational
systems when training data is limited and provide insights into the factors that influence
user satisfaction.
• We use knowledge distillation to scale the
application of learned rubrics and show the
rubrics can continuously improve performance as more training data is available.

2

Problem Definition and Related Work

Problem Definition. Let a conversation C
from session i and consisting of t interaction turns of user-agent utterances be Ci =
[U1 , A1 , . . . , Ut , At ]. Here Ut refers to a user utterance and At refers to an AI agent utterance. The
user-agent utterances Ci typically consist of multiple turns, e.g., t > 1. The conversation also has
an overall user satisfaction label yi ∈ [−1, +1]
provided by thumb feedback (e.g., like or dislike).
Our goal is to learn a function f : C → y to
accurately predict the satisfaction label of unseen
conversations and explain the predicted label. In
multi-turn conversational sessions, a user can convey their satisfaction (or dissatisfaction) explicitly
in their utterances or implicitly through their behavioral interactions with the agent. We refer to these
satisfaction/dissatisfaction conversational patterns
as SAT/DSAT patterns. Let S = {s1 , s2 , · · · , s∞ }
and D = {d1 , d2 , · · · , d∞ } be the set of all interpretable SAT and DSAT patterns respectively.
We assume these are latent and unknown. The
goal is to identify a subset of SAT/DSAT pattern
classes (Ss ⊂ S, Ds ⊂ D) that summarize the
conversation enough
to accurately

 predict its label:
P (y|C) ≈ P y Ss (C), Ds (C) .
SAT and DSAT patterns may be direct compliments or complaints about the AI agent’s responses,

or behavioral patterns that implicitly express user
satisfaction. For example, users may continue to
ask follow-up questions, indicating that the AI has
provided accurate information that inspires their
curiosity and leaves them satisfied. Conversely, if a
user repeatedly rephrases the same question, it can
signal dissatisfaction.
Related Work. Numerous prior research studies
have examined User Satisfaction Evaluation (USE)
through the lenses of sentiment analysis (Song
et al., 2023, 2019), content analysis (Walker et al.,
1997; Sun et al., 2021), and response quality assessment (Schmitt and Ultes, 2015; Bodigutla et al.,
2019). While analyzing user sentiment distribution in a dialogue session can enhance the model’s
USE capabilities, it is important to note that sentiment analysis is not equivalent to USE (Song et al.,
2023). Another common approach involves content
analysis, which typically necessitates the employment of human annotators to evaluate interaction
quality in a dialogue session (Schmitt and Ultes,
2015; Bodigutla et al., 2019). Afterwards, a classifier is trained to predict user satisfaction based on
the features extracted from the annotation process.
With the advancement of language models, there
is a growing trend in the use of text embeddings
to estimate user satisfaction for conversational systems (Liang et al., 2021; Kachuee et al., 2021b;
Pan et al., 2022; Sun et al., 2021). This approach is
also being employed to simulate user satisfaction.
Some work has focused on identifying dialogue
acts or user intents in measuring the fulfillment of
the user’s goals (Cai and Chen, 2020; Sun et al.,
2021). Other work has focused on incorporating
the sequential dynamics of dialogue acts (Deng
et al., 2022), jointly predicting sentiment and satisfaction (Song et al., 2023), or modeling dynamics
of satisfaction across turns (Ye Fanghua, 2023).
Recently, Large Language Models (LLMs) revolutionized the traditional learning framework (Kojima et al., 2022; Wei et al., 2022), especially for
natural language processing (NLP) tasks. LLMs
have achieved performance comparable to supervised baselines or state-of-the-art results across various NLP tasks with In-Context Learning (ICL).
By providing a few examples or hints (Lampinen
et al., 2022; Sun et al., 2023) and simple reasoning process (Kojima et al., 2022; Wei et al., 2022),
LLMs can provide significant performance boosts
for NLP tasks. Hu et al. (2023) further uses LLMs
as a user simulator for USE and adopts the user sim-

ulator into RLAIF (Bai et al., 2022) for fine-tuning
the existing LLM models. For USE with zero-shot
prompting (Kojima et al., 2022; Hu et al., 2023),
instructions provided by a human may not fit the
actual conversation patterns in the data and hence
introduce bias. For few-shot prompting Lampinen
et al. (2022); Sun et al. (2023), the provided examples are not enough to describe the full distribution
of the conversational patterns, and this results in
inaccuracies for USE.

3

SPUR

We propose SPUR for interpretable User Satisfaction Estimation (USE) given a small set of labeled
conversation C from a conversational system. Due
to the multi-turn and general-purpose nature in such
conversational systems, users demonstrate a variety of response patterns when expressing satisfaction or dissatisfaction. Our approach follows the
three-phase prompting strategy depicted in Figure
2: Supervised Extraction, Rubric Summarization,
and User Satisfaction Estimation. Our three-phase
approach is essential for ensuring accuracy, generalization, and interpretability. Through Supervised
Extraction, SPUR improves accuracy by capturing
the diverse conversational patterns in the training
set Ctrain = {C1 , C2 , · · · , CN }, which are annotated with thumb feedback. In the Rubric Summarization stage, the LLM improves generalization
and interpretability by identifying prominent SAT
and DSAT pattern classes among the full set of
extracted pattern. Finally, SPUR uses the learned
rubrics generated from the previous stage to score
user satisfaction on unlabeled conversations. For
the ease of understanding, we use mathematical
definitions to approximate the process of SPUR in
the following three sections.
3.1

Supervised Extraction

The first step of our framework is Supervised
Extraction—where we use a prompt to obtain meaningful and interpretable SAT/DSAT pattern classes
from GPT-4, which has an exceptional ability for
natural language understanding and reasoning (Ye
and Durrett, 2023; Huang et al., 2023; Kojima
et al., 2022). Given a conversation Ci with its
user satisfaction label yi = +1, how the user
expresses satisfaction in Ci can be formulated
as: b
si ≈ arg maxk P (S|Ci , yi = +1) where
s∈S

S = {s1 , s2 , · · · , s∞ } is the set of all possible SAT
patterns. The goal is to identify the top-k potential
bi = {s1 , s2 , · · · , sk } ⊂ S that are
pattern classes s

Figure 2: Illustration of SPUR approach. Step 1 corresponds to Sec. 3.1, Step 2: Sec. 3.2, and Step 3: Sec. 3.3.

exhibited in Ci relevant to satisfaction expression.
b i ≈ arg maxk P (D|Ci , yi = −1),
Similarly, d
d∈D

where D = {d1 , d2 , · · · , d∞ } is the set of all possible DSAT patterns.
b
b or d
The prompt for generating the possible s
patterns from Ctrain is provided in Appendix A.1.
In our prompt, we specifically require GPT-4 to
restrict k ≤ 3 for each Ci . The prompt for DSAT
patterns is similar; we only replace “satisfaction”
with “dissatisfaction” in the instructions.
For the ease of discussion in the next section,
let Sb = {b
s1 , · · · , sbN } denote all the SAT patb=
terns derived from Supervised Extraction and D
b
b
{d1 , · · · , dN } are all the DSAT patterns.
3.2

Rubric Summarization

The patterns extracted through Supervised Extraction prompting may exhibit significant variation
based on the text descriptions across different conversations, and their relative importance may not
be uniform. Our observations indicate that, despite
differences in the text descriptions, most sbi ∈ Sb
b are semantically similar. As such, the
and dbi ∈ D
goal of the Rubric Summarization stage is to further condense Sb and b
D, and identify frequently
occurring SAT/DSAT patterns across Ctrain . The
outcome of this process is the establishment of a
b
clear rubric for USE based on Sb and D.
However, it is infeasible to summarize Sb and
b into a clear rubric using a single prompt beD
b is too large
cause the number of tokens in Sb and D
to fit into the context size limit of GPT-4. (Note,
we used GPT-4-32K with a 32K context window

in this work.) To address this, we propose an iterative process to incrementally update the satisfaction and dissatisfaction rubrics by processing a
fixed-size minibatch of patterns. The satisfaction
batches are denoted as {Sb1 , Sb2 , · · · , SbB } where
b
Sb = ∪B
b=1 Sb and the number of batches is B. Simb1 , D
b2 , · · · , D
bB } are the batches to learn
ilarly, {D
b = ∪B D
b
the dissatisfaction rubric and D
b=1 b . In
each iteration, GPT-4 is asked to generate an n-item
rubric for the SAT patterns in Sbb . This n-item SAT
rubric is then appended at the end of Sbb+1 to incorporate in the generation of the next n-item SAT
rubric. The iterative process continues until the
final batch, and then the last output n-item rubric
is used as the final SAT rubric Se = {s̃1 · · · s̃n }.
The process is illustrated at Step 2 in Figure 2. A
similar process is applied to generate the DSAT
e = {d˜1 · · · d˜n }. We set n = 10 in our
rubric D
experiments. The final SAT and DSAT rubrics for
Bing Copilot are in Table 4, and the Rubric Summarization prompt is provided in Appendix A.2.
There are two benefits to utilizing the LLMgenerated satisfaction and dissatisfaction rubrics
from this iterative process. First, the rubrics are
developed in a supervised manner from the set of
training conversations, Ctrain , thereby ensuring that
prominent (and thus predictive) SAT and DSAT pattern classes in the distribution are identified. As a
result, the generated rubrics provide a clear guideline for GPT-4 to estimate user satisfaction accurately. Second, the rubrics are generated from more
examples than can fit in a single context window.
As such, Rubric Summarization improves the gen-

user satisfaction and the sequential dynamics
of dialogue acts.

eralization for GPT-4 in terms of in-context learning.
3.3

User Satisfaction Estimation

After learning the satisfaction rubric Se and dissatisfaction rubric e
D, we incorporate the generated
rubrics as instructions in a third prompt that we provide GPT-4 to score user satisfaction. The rubric
items provide a consistent decision making criteria
and enhance the performance of GPT-4 on USE.
For each rubric item s̃r ∈ Se or d˜r ∈ e
D, the prompt
asks GPT-4 to make a binary decision as to whether
a given conversation demonstrates the described
behavior. If the answer is "Yes", the prompts further instruct GPT-4 to evaluate how likely the expressed pattern will impact the user’s overall satisfaction/dissatisfaction with their interaction on
a scale of 1 − 10 (low to high). Otherwise, if the
answer is “No,” the score is 0. After the score for
each rubric item is output, we further aggregate the
scores into a single SAT score R to represent the
overall user satisfaction in the
Pngiven conversation.
Pn
R is computed as: R =
i=1 r̃si −
j=1 r̃dj
where r̃si is the score for the ith SAT rubric item
and r̃dj for the jth DSAT item. The prompt is in
Appendix A.3.

4

Evaluation

We evaluate SPUR by comparing its performance
quantitatively against previous embedding-based
approaches and several ablated versions of our
LLM-based approach.
4.1

Baselines

We compare SPUR with two LLM-based methods, including ZeroShot and FewShot, and three
embedding-based methods: Linear Regression,
USDA (Deng et al., 2022) and ASAP (Ye Fanghua,
2023). Note that we choose GPT-4 for all LLMbased methods instead of other smaller language
models because smaller language models struggle
to accurately generate scores for each rubric item,
which results in incorrect SAT scores. The detailed
descriptions of the models are as follows:
1. Lin-ada: Linear regression model with ada002 embedding (Ada)
2. USDA (Deng et al., 2022)1 is an embeddingbased method for USE by jointly optimizing
1

https://github.com/dengyang17/USDA

3. ASAP (Ye Fanghua, 2023)2 is another
embedding-based method which models user
satisfaction across turns via a Hawkes Process.
4. Zero shot: prompt GPT-4 directly to score
conversations for user satisfaction with basic
reasoning steps by providing explanations.
5. Few shot: prompt GPT-4 directly to score
conversations, include 2 examples of labeled
conversations to guide GPT-4 to determine
user satisfaction and include basic reasoning
steps by providing explanations.
6. RQ: prompt GPT-4 with a manually selected
features to assess the response quality (Bodigutla et al., 2020) and ask GPT-4 to determine
user satisfaction based on the set of features.
7. Reward: pretrained reward model for RLHF3 .
4.2

Dataset

We use four datasets to evaluate the performance of
the compared methods. Bing Copilot is a generalpurpose and multilingual conversational system,
and this dataset includes 50K fully anonymized
conversations.4 . MWOZ (Eric et al., 2020),
SGD (Rastogi et al., 2020) and ReDial (Siro et al.,
2022) are three task-oriented, English conversational systems, and they have 1155, 1638, and 1387
conversations, respectively. These three datasets
are further processed and labeled user satisfaction
by Sun et al. (2021). Because Sun et al. (2021) labeled user satisfaction by turn, we further process
these labels into a label to represent the overall
satisfaction of the whole conversation. The preprocessing details are described in Appendix B.
Ethics. As part of the production process, the Bing
Copilot data is anonymized, and each conversation
is formed by aggregating turns based on a unique
conversation ID. Thus, none of the researchers who
analyzed the data are able to recover and identify
https://github.com/smartyfh/ASAP
https://huggingface.co/OpenAssistant/reward-modeldeberta-v3-large-v2
4
All personal, private, or sensitive information was
scrubbed and masked before the conversations were used for
this research. The access to the dataset is strictly limited
to the authors who conducted hands-on analysis and model
development.
2
3

the conversations from any individual user. In addition, this research study was reviewed and approved by representatives from our institutional
review board (IRB), as well as our ethics and security teams. No formal IRB certificate was required
since we did not conduct any human studies for
this paper.

lower weighted F1 scores because they cannot accurately classify the conversations from the less
likely classes. However, the strong performance of
ZeroShot and SPUR demonstrate that LLM-based
methods can effectively identify accurate satisfaction/dissatisfaction conversational patterns from
limited data.

4.3

4.4

USE under Few-Shot Setting.

Table 1 shows the performance of each model
trained with a small number of training examples.
The performance scores are the average of five runs
in different train/test splits. The performance metrics are weighted based on the label distributions
due to the data imbalance in the different datasets.
The training set sizes are shown beside the name
of each dataset, and the remaining 80% of the data
is used for testing. The number of items in the
satisfaction and dissatisfaction rubrics is ten, respectively. Three task-oriented datasets have larger
training sizes because we want to ensure that there
are at least ten conversations with satisfaction labels and ten conversations with dissatisfaction labels to derive SPUR’s rubrics.
The performance difference between ZeroShot
and SPUR lies in that the learned rubrics can provide better guidance for LLMs to determine user
satisfaction. Comparing the performance between
RQ and SPUR in Table 1, the effectiveness of the
rubrics can be observed. Prompting with learned
rubrics can provide guidance specific to a dataset
for LLMs than prompting with a set of manually
selected features (Bodigutla et al., 2020) used by
all datasets. On the other hand, FewShot has worse
performance compared to other methods because
the examples provided in the prompt cannot cover
many types of satisfaction/dissatisfaction conversational patterns, and the decision is usually biased
by the examples provided in the prompt.
The performance of the Reward model (reward
deberta) validates our hypothesis that Reward models used for RLHF is not a good proxy for scoring
user satisfaction. Because Reward models are usually trained with auxiliary human feedback, this
reward is not learned from the perspective of the
user who was involved in the conversation with the
AI agent (Kirk et al., 2023).
Embedding methods perform worse than SPUR
in Table 1. Due to the smaller training size, embedding methods cannot generalize well, particularly
when the class is imbalanced. They usually have

Importance of Rubric Summarization.

Table 2 demonstrates that learning the rubric on
each dataset is important for improving the performance on USE. In this experiment, we first use the
rubric learned from Bing Copilot (Appendix A.3)
in the prompt for MWOZ, SGD and Redial, and
evaluate USE performance. Then, we apply the specialized rubrics learned from the target datasets and
reevaluate USE performance to gauge how much
the Bing Copilot rubrics fail to generalize across
tasks. The weighted F1 scores in the first column
show that rubrics learned on domain-specific data
produce an average gain of 13%. The last two
columns show the set difference between the rubric
items in the target and source sets, i.e., Se(·) \ SeCopilot
e(·) \ D
eCopilot . Values ≥ 0 indicate that the
and D
Rubric Summarization process learns a different
set of SAT/DSAT rubrics compared to that of Bing
Copilot. This demonstrates that the handcrafted
features used by several previous studies (Walker
et al., 1997; Bodigutla et al., 2019, 2020) are unlikely to generalize across different types of conversational systems. At the same time, manually
designing rubrics (features) for each different conversational systems is time consuming and likely to
be ineffective. With our LLM Rubric Summarization process, a targeted set of rubric items can be
learned for each task/domain, thereby improving
USE accuracy.
4.5

Rubric vs. Thumb Feedback.

Figure 3 shows the correlation between each rubric
item and thumb feedback from users. As discussed
in Section 3.3, we ask GPT-4 to generate a label
(Yes or No) and a score (0 to 10) for each rubric
item in the prompt. The “Yes” label for a rubric
item means that the conversational pattern exists in
the given conversation, and the score indicates how
likely this conversation pattern impacts the overall user satisfaction. The title of each sub-figure
in Figure 3 provides a short keyword to summarize the rubric item, and the full descriptions of
these keywords are listed in Table 4. The x-axis

Table 1: Precision (P), Recall (R), and F1 Score (F1) on USE with small training set sizes. The training sizes are
shown besides the name of each dataset. The testing size is 80% of the data. The best scores are in bold face.
Bing Copilot (0.8%)

Models

P
74.0
49.7
66.0
43.6
75.5
63.8
57.7
76.3

Lin-ada
USDA
ASAP
Reward
ZeroShot
FewShot
RQ
SPUR

Score

6

F1
73.3
47.3
58.4
52.7
68.3
61.9
57.7
75.4

P
48.0
38.1
51.2
63.0
66.2
68.4
33.3
65.7

R
24.0
50.7
56.1
47.4
52.2
47.4
52.5
61.6

F1
29.1
35.3
52.5
40.7
53.6
44.8
38.1
59.0

SGD (5%)
P
53.9
66.1
64.8
65.3
75.3
67.3
49.6
73.7

R
34.9
66.3
69.8
66.9
70.8
69.9
67.3
74.1

ReDial (5%)

F1
39.4
61.3
66.3
58.6
71.9
66.2
54.4
72.6

Suggestion Personal
Positive
No
Gratitude* Feedback* Engagement* Follow-up* Frustration* Acceptance* Details*

P
56.0
56.1
60.0
44.1
71.2
41.0
40.6
68.4

Task
Request*

R
27.7
56.8
63.6
57.7
58.2
62.2
63.6
68.7

F1
33.6
48.3
58.3
48.2
57.0
49.4
49.5
66.3

Correction* Learning*

4
2
0
6

Score

R
72.5
53.3
70.1
52.0
73.7
68.8
69.6
77.2

MWOZ (5%)

Repetition*

Errors*

Negative
Feedback*

Dislike Like

Dislike Like

Dislike Like

Topic
Lack
No
Irrelevant Complex
Switch* Visualization*Engagement* Information* Answer*

Sudden
End*

Lack
Diversity*

Dislike Like

Dislike Like

4
2
0

Dislike Like

Dislike Like

Dislike Like

Dislike Like

Dislike Like

Figure 3: The average scores for each rubric item w.r.t. thumb feedback (Like or Dislike). The ‘*’ beside each
keyword indicates that the rubric item is significantly correlated with thumb feedback.
Table 2: The F1 Gain shows the improvement after
learning the dataset-specific rubrics compared to the
Bing Copilot rubrics, and the last two columns report
the set difference between the SAT/DSAT rubrics of
each open dataset and the Bing Copilot dataset.
Dataset
MWOZ
SGD
ReDial

F1
Gain
20.8%
9.5%
9.2%

Num. New
SAT Patterns
6
3
5

Num. New
DSAT patterns
8
4
4

shows thumb feedback from users (Like or Dislike). The y-axis shows the average score for each
rubric item with respect to the conversations with
particular user satisfaction labels. The satisfaction
rubric items, which are in the top row, have a higher
average score when thumb feedback is Like. Conversely, the conversations where thumb feedback
is Dislike have higher scores for the dissatisfaction
rubric items (bottom row).
From Figure 3, we can see that all twenty rubric
items exhibit a significant difference in scores with
respect to thumb feedback. This indicates that the
score for each rubric item can be used to improve
USE predictions. We conducted a Chi-Square
test between the labels of each rubric item and
thumb feedback from users to observe whether

these rubric items are useful for USE. The “*” beside each keyword indicates that the rubric item
is significantly correlated (p < 0.05?) with the
signals provided by thumb feedback.
4.6

Pattern Variance for Different
Conversational Systems.

Figure 4 reports the satisfaction and dissatisfaction rubric items summarized from the Bing Copilot dataset in the top row, and the bottom row
shows the rubric items learned from the MWOZ
dataset. Different types of conversational patterns
can be observed for the two different conversational systems. Each bar indicates the distribution
of the number of times that each rubric item appears in a conversation. Because Bing Copilot is
a general-purpose conversational system, the summarized rubric items are general conversational
patterns. The detailed description of each Bing
Copilot rubric item is shown in Table 4 in Appendix E. In contrast, since MWOZ is a booking
chatbot, some satisfaction patterns, e.g. booking
confirmation or dissatisfaction patterns and plan
adaption, are specific to the booking chatbot. The
descriptions for each rubric item learned from the
MWOZ dataset are listed in Table 5 in Appendix E.

0

20

40

Percentage (%)

Negative Feedback
Repetition
Errors
Topic Switch
Lack Visualization
No Engagement
Irrelevant Information
Complex Answer
Sudden End
Lack Diversity

60

(a) Bing Copilot.
Gratitude
Booking Acceptance
No Frustration
Follow-up
Booking Confirmation
Farewell
Cooperation
Clarification
Request Fulfillment
Request Flexibility

25

50

75

Percentage (%)

100

10

0

20

40

Percentage (%)

(d) MWOZ.

Figure 4: Satisfaction/Dissatisfaction Conversational
Pattern Distributions.

Similarly, different conversational systems have
different service targets, and therefore, the reasons
causing user satisfaction or dissatisfaction are related to the target of the system. Because Bing
Copilot is a general-purpose question-answering
system, inaccurate information contributes to a
larger portion of dissatisfaction. While MWOZ
is a booking-reservation system, more of the dissatisfaction is due to a lack of proactivity or a compromise in preference, which means that users have
to actively search or choose an option that is less
preferred.
4.7

Knowledge Distillation.

Although SPUR can be effectively applied to predict user satisfaction as shown above, since SPUR
requires GPT-4 prompting, it is still inefficient to
apply USE at web scale (e.g., there have been
more than 5 billion conversations in Bing Copilot to date (Mehdi). To address this, we propose
a knowledge distillation process for each of the
rubric items to reduce the cost of the evaluation
process. Given the rubric item, we prompt GPT4 to label a set of conversations for training (the
label represents whether or not the conversational
pattern described by the rubric item appears in the
conversation). Then we calculate an embedding
for the conversation (e.g., using OpenAI ada-002)
and train a classifier (Logistic Regression) to distill GPT-4 knowledge (i.e., learn a mapping from
embedding to rubric label).
We use the above process to distill knowledge
from GPT-4 for one of the satisfaction rubric items

ada-002 AUC= 0.975
E5 AUC= 0.957
XLM-roBERTa AUC= 0.85

0.2

20

DSAT Rubric

0.8

0.4

Percentage (%)

Negative Feedback ROC

1.0

0.6

0.0
0.0

0

Irrelevant Information
Repetition
Lack Feedback
Ignored or Misunderstood
Compromise Preference
Lack of Proactivity
Plan Adaption
Topic Switch
Failed Bookings
False Confirmation

(c) MWOZ.

Gratitude ROC

1.0
0.8

(b) Bing Copilot.

SAT Rubric

0

DSAT Rubric

True Positive Rate

SAT Rubric

True Positive Rate

Gratitude
Positive Feedback
Engagement
Follow-up
No Frustration
Suggestion Acceptance
Personal Details
Task Request
Correction
Learning

0.2

0.4

0.6

False Positive Rate

0.8

1.0

(a) Gratitude.

0.6
0.4

ada-002 AUC= 0.916
E5 AUC= 0.888
XLM-roBERTa AUC= 0.74

0.2
0.0
0.0

0.2

0.4

0.6

False Positive Rate

0.8

1.0

(b) Negative Feedback.

Figure 5: ROC on Knowledge Distillation from GPT-4.

(Gratitude) and one of the dissatisfaction rubric
items (Negative Feedback). Specifically, we train a
Gratitude classifier and a Negative-Feedback classifier. The effectiveness of knowledge distillation
is shown in Figure 5a and Figure 5b. A higher
AUC metric indicates that the classifier can successfully distill the knowledge from GPT-4 for the
given rubric item. We compare the performance of
the distilled model with two different embeddings:
OpenAI’s text-embedding-ada-002 (Ada) and multilingual E5 (E5). As a baseline we compare to
an embedding-based sentiment classifier: XLMroBERTa (XLM-roBERTa). The results show that
ada-002 is the most effective text embedding model
for knowledge distillation, so we use that in the experiments below.
Feedback Distributions. After learning the two
textual feedback classifiers, we deploy them to a
production environment and seek to understand
whether they provide different coverage compared
to explicit thumb feedback (i.e.,“Like” or “Dislike”). Figure 6 reports the distribution of the two
types of feedback from one week in production.
“Textual” feedback records the proportion of conversations that have true labels predicted by the Gratitude classifier (Textual Like) or by the NegativeFeedback classifier (Textual Dislike). Instead of reporting absolute numbers, we report results relative
to the proportion of thumb feedback we observe in
the data. Figure 6 shows the relative frequency of
thumb vs. textual feedback. We can observe that
users give more positive feedback through thumb
feedback and more negative feedback through their
utterances. This also demonstrates the importance
of mining conversational SAT/DSAT patterns via
SPUR.
4.8

Rubrics as Features

Finally, we seek to understand if combining the
rubrics with conversation text embeddings can produce better results using the model proposed in Appendix D. We use Bing Copilot dataset with 100K

Thumb Feedback

Like
Dislike

Textual Feedback

0.0

0.5

1.0

Figure 6: Distributions of Click and Textual Feedback.

95
90

F1 Score

85
80
75
70

ASAP
SPUR
Lin-ada
SPUR-Lin-ada

65
60
55

103

104

Training Set Size

Figure 7: Comparison of F1 scores for the proposed
SPUR and SPUR-Lin-ada models and baseline models
for different training set sizes.

conversations for this experiment. This experiment
varies the training size from 400 to 90K of the data
and 10K of the data is for testing. The results in
Figure 7 indicate that SPUR provides the best F1
results for smaller training set sizes. As the training set size increases, the weighted F1 scores of
the SPUR-Lin-ada (SPUR rubrics and linear regression with OpenAI ada-002 embeddings) improves
compared to our SPUR model and the SOTA embedding ASAP baseline. The results demonstrate
that adding the SPUR metrics to the feature vector
consistently provides additional USE signals that
are not captured by the conversation embeddings.
Note, due to the prohibitive cost, we did not retrain
SPUR for larger training set sized above 10,000
samples. Thus, the orange dashed line from 10K to
90K training samples indicates the SPUR F1 score
for the test set if we only trained with 10K samples.

5

Conclusion and Limitations

In this paper, we proposed Supervised Prompting for User satisfaction Rubrics (SPUR), a novel
framework for estimating user satisfaction with
LLMs in conversational systems. We demonstrated
that SPUR outperforms existing methods on user

satisfaction estimation across different types of conversational systems and also provided insights into
the factors that influence user satisfaction. Moreover, SPUR is more interpretable because it automatically grounds/scores the dimensions of satisfaction in observed user behavior from Rubric
Summarization prompting. We also demonstrated
the utility of our rubrics for knowledge distillation
and coverage analysis. Finally, we showed the utility of our model for different training set sizes by
combining the rubric item scores with the conversational embeddings as features and observed that
these rubrics provide extra signals for performance
improvement on USE.
Limitations. Although SPUR outperforms baseline models with limited training sets, an important
factor, the framework is costly if the goal is to estimate user satisfaction at the scale of millions of
conversations. We have proposed a method to distill knowledge from GPT-4, but a thorough study is
needed to show the robustness of this approach. In
future work, we will focus on the scalability issues
of SPUR to reduce its cost at a larger scale.

References
OpenAI Ada. Embeddings. Accessed on: Feb 15, 2024.
Yuntao Bai, Saurav Kadavath, Sandipan Kundu,
Amanda Askell, Jackson Kernion, Andy Jones, Anna
Chen, Anna Goldie, Azalia Mirhoseini, Cameron
McKinnon, Carol Chen, Catherine Olsson, Christopher Olah, Danny Hernandez, Dawn Drain, Deep
Ganguli, Dustin Li, Eli Tran-Johnson, Ethan Perez,
Jamie Kerr, Jared Mueller, Jeffrey Ladish, Joshua
Landau, Kamal Ndousse, Kamile Lukosiute, Liane
Lovitt, Michael Sellitto, Nelson Elhage, Nicholas
Schiefer, Noemí Mercado, Nova DasSarma, Robert
Lasenby, Robin Larson, Sam Ringer, Scott Johnston, Shauna Kravec, Sheer El Showk, Stanislav Fort,
Tamera Lanham, Timothy Telleen-Lawton, Tom Conerly, Tom Henighan, Tristan Hume, Samuel R. Bowman, Zac Hatfield-Dodds, Ben Mann, Dario Amodei,
Nicholas Joseph, Sam McCandlish, Tom Brown, and
Jared Kaplan. 2022. Constitutional AI: harmlessness
from AI feedback. CoRR, abs/2212.08073.
Praveen Kumar Bodigutla, Lazaros Polymenakos, and
Spyros Matsoukas. 2019. Multi-domain conversation
quality evaluation via user satisfaction estimation.
CoRR, abs/1911.08567.
Praveen Kumar Bodigutla, Aditya Tiwari, Josep VallsVargas, Lazaros Polymenakos, and Spyros Matsoukas. 2020. Joint turn and dialogue level user satisfaction estimation on multi-domain conversations.
CoRR, abs/2010.02495.
Wanling Cai and Li Chen. 2020. Predicting user intents
and satisfaction with dialogue-based conversational
recommendations. In Proceedings of the 28th ACM
Conference on User Modeling, Adaptation and Personalization, UMAP 2020, Genoa, Italy, July 12-18,
2020, pages 33–42. ACM.
Paul F. Christiano, Jan Leike, Tom B. Brown, Miljan
Martic, Shane Legg, and Dario Amodei. 2017. Deep
reinforcement learning from human preferences. In
Advances in Neural Information Processing Systems
30: Annual Conference on Neural Information Processing Systems, pages 4299–4307.
Yang Deng, Wenxuan Zhang, Wai Lam, Hong Cheng,
and Helen Meng. 2022. User satisfaction estimation with sequential dialogue act modeling in goaloriented conversational systems. In WWW ’22: The
ACM Web Conference 2022, Virtual Event, Lyon,
France, April 25 - 29, 2022, pages 2998–3008. ACM.

2020. Multiwoz 2.1: A consolidated multi-domain
dialogue dataset with state corrections and state tracking baselines. In Proceedings of The 12th Language
Resources and Evaluation Conference, LREC 2020,
Marseille, France, May 11-16, 2020, pages 422–428.
European Language Resources Association.
Zhiyuan Hu, Yue Feng, Anh Tuan Luu, Bryan Hooi,
and Aldo Lipani. 2023. Unlocking the potential of
user feedback: Leveraging large language model as
user simulators to enhance dialogue system. In Proceedings of the 32nd ACM International Conference
on Information and Knowledge Management, CIKM
2023, Birmingham, United Kingdom, October 21-25,
2023, pages 3953–3957. ACM.
Shiyuan Huang, Siddarth Mamidanna, Shreedhar
Jangam, Yilun Zhou, and Leilani H. Gilpin. 2023.
Can large language models explain themselves? A
study of llm-generated self-explanations. CoRR,
abs/2310.11207.
Mohammad Kachuee, Hao Yuan, Young-Bum Kim,
and Sungjin Lee. 2021a. Self-supervised contrastive
learning for efficient user satisfaction prediction in
conversational agents. In Proceedings of the 2021
Conference of the North American Chapter of the
Association for Computational Linguistics: Human
Language Technologies, NAACL-HLT 2021, Online,
June 6-11, 2021, pages 4053–4064. Association for
Computational Linguistics.
Mohammad Kachuee, Hao Yuan, Young-Bum Kim, and
Sungjin Lee. 2021b. Self-supervised contrastive
learning for efficient user satisfaction prediction
in conversational agents. In Proceedings of the
2021 Conference of the North American Chapter of
the Association for Computational Linguistics: Human Language Technologies, Online. Association for
Computational Linguistics.
Hannah Rose Kirk, Bertie Vidgen, Paul Röttger, and
Scott A. Hale. 2023. Personalisation within bounds:
A risk taxonomy and policy framework for the alignment of large language models with personalised
feedback. CoRR, abs/2303.05453.
Takeshi Kojima, Shixiang Shane Gu, Machel Reid, Yutaka Matsuo, and Yusuke Iwasawa. 2022. Large language models are zero-shot reasoners. In NeurIPS.

Hugginface E5. intfloat/multilingual-e5-large. Accessed on: Accessed on: Feb 15, 2024.

Andrew K. Lampinen, Ishita Dasgupta, Stephanie C. Y.
Chan, Kory W. Mathewson, Michael Henry Tessler,
Antonia Creswell, James L. McClelland, Jane Wang,
and Felix Hill. 2022. Can language models learn
from explanations in context? In Findings of the
Association for Computational Linguistics: EMNLP
2022, Abu Dhabi, United Arab Emirates, December
7-11, 2022, pages 537–563. Association for Computational Linguistics.

Mihail Eric, Rahul Goel, Shachi Paul, Abhishek Sethi,
Sanchit Agarwal, Shuyang Gao, Adarsh Kumar,
Anuj Kumar Goyal, Peter Ku, and Dilek Hakkani-Tür.

Runze Liang, Ryuichi Takanobu, Feng-Lin Li, Ji Zhang,
Haiqing Chen, and Minlie Huang. 2021. Turn-level
user satisfaction estimation in E-commerce customer

Jan Deriu, Álvaro Rodrigo, Arantxa Otegi, Guillermo
Echegoyen, Sophie Rosset, Eneko Agirre, and Mark
Cieliebak. 2021. Survey on evaluation methods for
dialogue systems. Artif. Intell. Rev., 54(1):755–810.

service. In Proceedings of the 4th Workshop on eCommerce and NLP, pages 26–32, Online. Association for Computational Linguistics.
Yusuf Mehdi. Bringing the full power of copilot to more
people and businesses. Accessed on: Feb 15, 2024.
Yan Pan, Mingyang Ma, Bernhard Pflugfelder, and
Georg Groh. 2022. User satisfaction modeling with
domain adaptation in task-oriented dialogue systems.
In Proceedings of the 23rd Annual Meeting of the
Special Interest Group on Discourse and Dialogue,
Edinburgh, UK. Association for Computational Linguistics.
Abhinav Rastogi, Xiaoxue Zang, Srinivas Sunkara,
Raghav Gupta, and Pranav Khaitan. 2020. Towards
scalable multi-domain conversational agents: The
schema-guided dialogue dataset. In The ThirtyFourth AAAI Conference on Artificial Intelligence,
AAAI 2020, The Thirty-Second Innovative Applications of Artificial Intelligence Conference, IAAI 2020,
The Tenth AAAI Symposium on Educational Advances
in Artificial Intelligence, EAAI 2020, New York, NY,
USA, February 7-12, 2020, pages 8689–8696. AAAI
Press.
Hugginface reward deberta. Openassistant/rewardmodel-deberta-v3-large-v2. Accessed on: Accessed
on: Feb 15, 2024.
Alexander Schmitt and Stefan Ultes. 2015. Interaction
quality: Assessing the quality of ongoing spoken
dialog interaction by experts - and how it relates to
user satisfaction. Speech Commun., 74:12–36.
Clemencia Siro, Mohammad Aliannejadi, and Maarten
de Rijke. 2022. Understanding user satisfaction with
task-oriented dialogue systems. In SIGIR ’22: The
45th International ACM SIGIR Conference on Research and Development in Information Retrieval,
Madrid, Spain, July 11 - 15, 2022, pages 2018–2023.
ACM.
Kaisong Song, Lidong Bing, Wei Gao, Jun Lin, Lujun
Zhao, Jiancheng Wang, Changlong Sun, Xiaozhong
Liu, and Qi Zhang. 2019. Using customer service dialogues for satisfaction analysis with context-assisted
multiple instance learning. In Proceedings of the
2019 Conference on Empirical Methods in Natural Language Processing and the 9th International
Joint Conference on Natural Language Processing,
EMNLP-IJCNLP, pages 198–207. Association for
Computational Linguistics.
Kaisong Song, Yangyang Kang, Jiawei Liu, Xurui Li,
Changlong Sun, and Xiaozhong Liu. 2023. A speaker
turn-aware multi-task adversarial network for joint
user satisfaction estimation and sentiment analysis.
In Thirty-Seventh AAAI Conference on Artificial Intelligence, AAAI 2023, Thirty-Fifth Conference on Innovative Applications of Artificial Intelligence, IAAI
2023, Thirteenth Symposium on Educational Advances in Artificial Intelligence, EAAI 2023, Washington, DC, USA, February 7-14, 2023, pages 13582–
13590. AAAI Press.

Weiwei Sun, Shuo Zhang, Krisztian Balog, Zhaochun
Ren, Pengjie Ren, Zhumin Chen, and Maarten de Rijke. 2021. Simulating user satisfaction for the evaluation of task-oriented dialogue systems. In SIGIR ’21:
The 44th International ACM SIGIR Conference on
Research and Development in Information Retrieval,
Virtual Event, Canada, July 11-15, 2021, pages 2499–
2506. ACM.
Xiaofei Sun, Xiaoya Li, Jiwei Li, Fei Wu, Shangwei
Guo, Tianwei Zhang, and Guoyin Wang. 2023. Text
classification via large language models. In Findings of the Association for Computational Linguistics: EMNLP 2023, Singapore, December 6-10, 2023,
pages 8990–9005. Association for Computational
Linguistics.
Marilyn A. Walker, Diane J. Litman, Candace A. Kamm,
and Alicia Abella. 1997. PARADISE: A framework for evaluating spoken dialogue agents. In
35th Annual Meeting of the Association for Computational Linguistics and 8th Conference of the European Chapter of the Association for Computational
Linguistics, Proceedings of the Conference, 7-12 July
1997, Universidad Nacional de Educación a Distancia (UNED), Madrid, Spain, pages 271–280. Morgan
Kaufmann Publishers / ACL.
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten
Bosma, Brian Ichter, Fei Xia, Ed H. Chi, Quoc V. Le,
and Denny Zhou. 2022. Chain-of-thought prompting
elicits reasoning in large language models. In Advances in Neural Information Processing Systems 35:
Annual Conference on Neural Information Processing Systems 2022, NeurIPS.
Hugginface XLM-roBERTa. cardiffnlp/twitter-xlmroberta-base-sentiment. Accessed on: Accessed on:
Feb 15, 2024.
Xi Ye and Greg Durrett. 2023. Explanation selection
using unlabeled data for chain-of-thought prompting.
In Proceedings of the 2023 Conference on Empirical
Methods in Natural Language Processing, EMNLP
2023, Singapore, December 6-10, 2023, pages 619–
637. Association for Computational Linguistics.
Yilmaz Emine Ye Fanghua, Hu Zhiyuan. 2023. Modeling user satisfaction dynamics in dialogue via hawkes
process. In The 61st Annual Meeting of the Association for Computational Linguistics (ACL’23).

A

Prompts

A.1

Supervised Extraction Prompt

You job is to understand and elaborate how a
user expresses that they are **satisfied**
with their interaction with an AI agent. You
will be given a conversation that a user had
with an AI agent where the user provided a
signal of satisfaction through a like button.
Your task is to summarize how the user expressed

satisfaction with the conversation.
Instructions:
- Provide your answer in xml format between
<REASONS></REASONS> tags.
- Return NONE if you can't think of any part
of the user's utterances that expresses
satisfaction.
- The reasons you summarized should be
grounded on the conversation history only.
You should **NOT** extrapolate, imagine, or
hallucinate beyond the text of the
conversation that is given.
- The reasons should be mutually exclusive.
- You should **NOT** refer to the fact that
there was a like in your summary.
- Your summary should be concise, use bullet
points, and provide no more than 3 reasons.
<CONVERSATION>
[user-agent utterances]
</CONVERSATION>
The main reasons why the user is satisfied
with the interaction are:
A.2

Rubric Summarization Prompt

# Task
You job is to summarize why a user feels
**satisfied** with their interaction with
an AI agent and provide a rubric for
evaluation of a single conversation. You
will be given a list of example explanations
from conversations that users had with an
AI agent where these users provided a
signal of satisfaction.

rubric to identify user satisfaction with
respect to a conversation. Requirements:
* Provide your answer as a numbered list
of up to {num_rubric} bullet items.
* The number of items in the rubric should
be less than {num_rubric}.
* The rubric should be user-centric,
concise, and mutually exclusive.
* Provide your answer as a numbered list of
bullet items in <Rubric></Rubric>. The
output format is as follows:
```
# Output
<Rubric>
1. [item 1]
2. [item 2]
3. [item 3]
...
</Rubric>
```
# Output
A.3

User Satisfaction Estimation Prompt

# Your task is to evaluate both user
satisfaction and dissatisfaction with a
conversational AI agent by applying the
given rubrics to the given conversation
history between the user and the agent.

# Rubric instructions
- Each rubric contains 10 criteria.
- Each criterion has a Yes or No statement.
- Your job is to go through the
conversation history carefully and answer
Y to each statement that applies to the
user utterances in the conversation, then
# Instruction
give the statement a score of 1-10 to
Your task is to provide a rubric to
reflect how likely the expressed sentiment
identify user satisfaction with respect
will impact the user's overall
to a conversation. Requirements:
satisfaction/dissatisfaction with the
* Provide your answer as a numbered list
interaction. If the statement is not
of up to {num_rubric} bullet items.
applicable answer N and give an overall
* The rubric should be user-centric,
score of 0.
concise, and mutually exclusive.
- Each rubric is formatted in a table format
with 10 rows and two columns: Index|Y/N
# Example Explanations of User Satisfaction Question.
"[S_b + n-item rubrics from S_{b-1}.
# SATISFACTION RUBRIC
If b=0, put S_0]"
{n_item_sat_rubric}
# Now summarize these examples into a

# DISSATISFACTION RUBRIC

{n_item_dsat_rubric}

The modified label counts for the three open
datasets after following this label conversion process are provided in Table 3.

# Task:
- Go through the conversation history
Table 3: Label Distribution
thoroughly and evaluate the user's
Dataset SAT DSAT Neutral Sum
utterances. Do not consider the AI's
redial
822
463
102
1387
responses except to put the user's
sgd
1008 496
179
1683
response in context.
mwoz
560
524
71
1155
- For each rubric question think about your
answer to each question carefully.
- Answer Y or N only to each rubric question.
- For Y answer, score your answer on a scale C Experiment Setup
of 1-10 (low to high) to reflect how likely
We use GPT-4 for the entire process of training
the expressed sentiment will impact the
and evaluating SPUR, and SPUR-Lin-ada is trained
user's overall satisfaction or
and tested on an NVIDIA A100 instance. Every
dissatisfaction with the interaction.
experiment runs one time but with a large testing
For N answer, score 0.
- Only provide ONE most confident answer to size (80% is used for testing). The hyperparameters
are listed as follows:
each question.
- You *MUST* output your answers to all 10
• The number of top-k SAT or DSAT patterns
questions provided in each rubric.
for a conversation is 3.
# Conversation:
[user-agent utternaces]

• The batch size for each minibatch is 100
SAT/DSAT patterns.

# Answers

• The number of items for the satisfaction rubric
and dissatisfaction rubric is 10.

B

Labeling Adjustment for the Open
Data

The open datasets include turn-by-turn labels
whereas SPUR requires a label for the entire conversation. The process of translating turn-by-turn
labels into conversation labels follows these steps:
• If the full conversation has only neutral and
SAT, then the label for full conversation is
SAT.
• If the full conversation has only neutral and
DSAT, then the label for full conversation is
DSAT.
• If the full conversation has only neutral, then
the label for the full conversation is neutral.
• If the full conversation has both SAT and
DSAT.
– start from the beginning of the conversation, discard the rest of the conversation
when contradiction happens and assign
the label as the first non-neutral label.

D

User Satisfaction Model

The User Satisfaction Rubrics can be used by themselves to compute a USE score. However, we have
found that the utility can be further improved by
including a text embedding of the chat conversation
in addition to the values of the rubrics. In particular,
results show that using the OpenAI ada-002 text
embeddings are particularly effective.
The proposed model is depicted in Figure 8. On
the left, the conversations are projected into an
embedding space using the GPT-3 Ada-002 embeddings. In parallel, the 20 LLM rubric itmes are
computed using the GPT-4-32K LLM on the right.
The 1536-dimension conversation embedding vector is concatenated with the 20 SPUR rubric scores
to form the final feature vector which is then input
to a model such as Linear Regression, Logistic Regression, or a DNN. The output of the model is the
final predicted USE score.
Figure 9 compares the results using a final linear
regression layer and a logistic regression layer, with
and without the SPUR rubrics. The figure shows
that adding the SPUR rubrics improves both baseline models which only consider the conversation

embeddings as features. Furthermore, while the
two logistic regression models offer the best performance for smaller training set sized, the linear
regression models are the best performing models
for the larger training set sizes. We also evaluated
replacing the regression layer (e.g., linear, logistic)
with a DNN, but the performance was much worse
due to overfitting.
Predicted SAT Score
Linear Regression /
Logistic Regression
Concatenate

S1

OAI Ada-002
Embeddings

...

S10

D1

...

D10

GPT-4-32K Prompt

Chat Conversations

Figure 8: The proposed model combines the SPUR
LLM rubrics and conversation embeddings.

95
90

F1 Score

85
80
75
70

Lin-ada
SPUR-Lin-ada
Log-ada
SPUR-Log-ada

65
60
55

103

104

Training Set Size

Figure 9: Comparison of F1 scores for the proposed
SPUR and the combined SPUR and conversation embedding models for different training set sizes. Using
logistic regression offers better performance for smaller
training set sizes, but linear regression yields the best
results for the higher range.

E

Usage of AI Assistants

SPUR is an implementation based on GPT-4. We
only use Bing Copilot to assist our writing to identify grammar errors, typos and rephrase terms for
readability.

Table 4: Satisfaction and Dissatisfaction Features for Copilot

Satisfaction
Name
Gratitude

Description
The user thanks or compliments
the AI agent for its help, quality,
performance, or abilities.
Positive Feed- The user expresses positive
back
emotions or evaluations using
words, phrases, punctuation
marks, or emoticons.

Dissatisfaction
Name
Repetition

Errors

Description
The user repeats their query or
request multiple times.

The user points out an error,
inconsistency, or inaccuracy in
the AI’s output or information
and does not receive any acknowledgment or apology from
the agent.
Engagement
The user engages in a diverse Negative Feed- The user uses a negative tone
and lengthy conversation with back
or words to express frustration,
the AI agent, covering multiple
disappointment, anger, or disretopics or domains.
spect towards the AI agent.
Follow-up
The user asks follow-up ques- Topic Switch
The user changes their topic or
tions or requests more informaquery abruptly.
tion from the AI agent that show
curiosity and interest in learning
more.
No Frustration The user does not express any Lack Visualiza- The user does not receive any
negative emotion toward the tion
visual output from the AI agent
AI agent’s responses throughout
when they expect images, links,
the conversation.
charts, etc.
Suggestion Ac- The user accepts or follows the No
Engage- The user does not engage with
ceptance
AI agent’s suggestions, recom- ment
the AI agent’s questions, commendations, and feedback withments, suggestions, feedback reout hesitation, resistance, or
quests, etc.
challenging it.
Personal De- The user initiates or continues Irrelevant Infor- The user receives a generic,
tails
a personal conversation with mation
vague, irrelevant answer from
the AI agent by sharing details
the AI agent that does not adabout themselves or asking how
dress their specific needs, goals,
it is doing.
or preferences.
Task Request
The user requests specific tasks Complex An- The user receives a long and
from the AI agent that match swer
complex answer from the AI
its domain and scope of knowlagent that may be overwhelmedge, abilities, skills, and expering, confusing, or too technical
tise.
for them.
Correction
The user corrects some of the Sudden End
The conversation ends abruptly
AI agent’s mistakes, guesses, erwithout fulfilling, completing,
rors, or misunderstandings in a
or addressing the initial request,
cooperative, trusting, respectful,
problem, task, or goal.
and polite manner.
Learning
The user enjoys, appreciates, Lack Diversity The user expects a more inand learns from different forteractive, engaging, personalmats, styles, modes, and meized, humorous, and creative redia of outputs and services, as
sponse from the AI, rather than
well as information provided,
a generic, pre-written, factual,
explained, and generated by the
technical, verbose one.
AI agent.

Table 5: Satisfaction and Dissatisfaction Features for MWOZ

Satisfaction
Name
Gratitude

Description
Name
The user thanks the AI agent for Repetition
its service, indicating gratitude
and appreciation.
Booking Accep- The user accepts the AI agent’s Lack Feedback
tance
suggestions or bookings without asking for changes or alternatives, implying trust and satisfaction.

Dissatisfaction
Description
The user repeats their query or
request multiple times.

The user does not receive any
confirmation or feedback from
the AI after making requests,
asking questions, or providing
information, leading to uncertainty and confusion.
No Frustration The user does not express any Irrelevant Infor- The user receives irrelevant or
frustration, confusion, or dissat- mation
incomplete information from
isfaction with the AI agent’s rethe AI that does not align with
sponses or queries throughout
their queries or expectations,
the conversation.
which shows a lack of understanding or flexibility.
Follow-up
The user asks questions about Ignored or Mis- The user feels ignored or misthe information or options pro- understood
understood by the AI as it does
vided by the AI agent, showing
not answer some of their quesinterest and engagement.
tions, acknowledge their inputs,
or provide any clarification.
Booking Confir- The user confirms their book- Compromise
The user has to compromise on
mation
ing details or information with Preference
their desired options or critea positive expression, showing
ria because of limited availabilagreement and happiness.
ity or mismatched recommendations from the AI.
Farewell
The user ends the conversation Lack of Proac- The user has to ask basic queswith a polite farewell and no tivity
tions about features or details
complaints or requests for furthat the AI should have prother assistance.
vided upfront.
Cooperation
The user follows the AI agent’s Plan Adaption
The user changes their mind
guidance and prompts without
about something they previhesitation or objection, indicatously requested or agreed upon
ing acceptance and cooperation.
(e.g., location preference) without giving a clear reason.
Clarification
The user specifies their pref- Topic Switch
The user switches to a different
erences or constraints clearly
topic without closing the previand specifically, showing conous one.
fidence and comfort in communicating with the AI agent.
Request Fulfill- The user receives relevant and Failed bookings The user experienced several
ment
helpful information from the
failed bookings and received inAI agent that matches their reconsistent information from the
quests, such as phone number,
AI about availability.
price, etc.
Request Flexi- The user is able to change their False Confirma- The user was misled by the AI’s
bility
query or ask for different types tion
confirmation messages, which
of information without encounturned out to be false.
tering any errors or misunderstandings from the AI agent.
