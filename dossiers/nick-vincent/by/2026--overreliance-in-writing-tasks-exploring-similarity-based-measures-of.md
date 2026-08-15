---
title: "Overreliance in Writing Tasks: Exploring Similarity-Based Measures of AI Influence on Writing and Proposing a Reflective Writing Interface Intervention"
person: "nick-vincent"
section: "by"
type: "journal-article"
year: 2026
date: "2026-06-23"
venue: "ACM FAccT, 2026 · Published"
authors: "Vitor H. A. Welzel, Nicholas Vincent"
source_url: "https://dl.acm.org/doi/10.1145/3805689.3812389"
retrieved: "2026-08-13"
content: "full-text"
notes: "OpenAlex W7161650804; CV ref [P26]; Full text from the arXiv HTML rendering of the preprint (https://arxiv.org/html/2605.15322v1); This is the preprint version; the version of record is at https://doi.org/10.1145/3805689.3812389."
---

# Overreliance in Writing Tasks: Exploring Similarity-Based Measures of AI Influence on Writing and Proposing a Reflective Writing Interface Intervention

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

- 2 Related Work

- 2.1 Mental Proofs

- 2.2 Overreliance on AI

- 2.3 Similarity Analysis Between Human and AI Text

- 2.4 Impact on Cognitive Engagement

- 3 Methods

- 3.1 Materials and Tasks

- 3.2 Participants and Recruitment

- 3.3 Pilot Experiment

- 3.4 Main Experiment

- Assistance Format

- Counterbalancing and Assignment

- Procedure

- Counterfactual baseline

- Similarity Metrics

- Workload (cognitive engagement).

- Statistical hypothesis tests

- Qualitative analysis.

- 3.5 Think-Aloud Study of the Implemented Interface Intervention

- Interface.

- Procedure.

- Analysis.

- 4 Results

- 4.1 Main Experiment

- Similarity Metrics.

- Self-Reported Usage and Qualitative Analysis.

- Cognitive Load and Time.

- 4.2 Think Aloud Experiment on the Proposed Writing Interface Intervention

- The metrics shaped writing strategies and calibrated reliance

- The interface made AI influence identifiable during writing

- 5 Discussion

- Adoption vs. Overreliance

- AI output adoption is multi-dimensional

- Reflective metrics

- Null and mixed results on workload

- Broader implications for adoption and authorship

- Limitations and future work

- 6 Conclusion

- References

- A Task Prompts and AI Suggestions

- Prompt.

- AI Suggestion.

- Prompt.

- AI Suggestion.

License: CC BY 4.0

arXiv:2605.15322v1 [cs.HC] 14 May 2026

## Overreliance in Writing Tasks: Exploring Similarity-Based Measures of AI Influence on Writing and Proposing a Reflective Writing Interface Intervention\acmConference@name (\acmConference@shortname), \acmConference@date, \acmConference@venueConference: The 2026 ACM Conference on Fairness, Accountability, and Transparency; June 25–28, 2026; Montreal, QC, CanadaThe 2026 ACM Conference on Fairness, Accountability, and Transparency (FAccT ’26), June 25–28, 2026, Montreal, QC, CanadaDOI: 10.1145/3805689.3812389ISBN: 979-8-4007-2596-8/2026/06CCS: Human-centered computing HCI design and evaluation methodsCCS: Computing methodologies Artificial intelligenceCCS: Human-centered computing Empirical studies in HCI

Vitor H. A. Welzel

Affiliation: Simon Fraser University
, Burnaby
, Canada

email: vhd1@sfu.ca

and
Nicholas Vincent

Affiliation: Simon Fraser University
, Burnaby
, Canada

email: nvincent@sfu.ca

2026; © cc

####### Abstract.

As generative AI (GenAI) systems become increasingly proficient at simulating human-like and well-reasoned text, users may attribute authority to AI outputs, shaping how they engage with writing and reasoning tasks. While prior work has raised concerns about AI overreliance, empirical approaches for observing this phenomenon during open-ended writing remain limited. In this paper, we examine how GenAI assistance influences users’ interactions with AI suggestions during writing. We report results from a mixed-methods study in which 47 participants completed analysis and synthesis writing tasks with or without AI assistance. We quantify the textual overlap between AI suggestions and participants’ writing and analyze participants’ reflections. Our results show that AI assistance is associated with patterns of suggestion reuse. Building on these findings, we design and evaluate an interactive writing interface that may support reflection on the usage of the AI suggestions during writing. Evidence from a small follow-up think-aloud study (n=4n=4) suggests that the interface can increase users’ awareness of how AI outputs are incorporated into their writing and may support more conscious engagement with AI assistance. Together, our findings contribute empirical methods for studying AI adoption in writing contexts and demonstrate how interface design can shape user–AI interaction.

####### Keywords:

Generative AI, Human-AI Interaction, Interface Design, User Studies

††cc-license: by

### 1. Introduction

Generative AI (GenAI) systems are increasingly capable of producing text that reflects human reasoning cues, including a consistent natural tone and textual structure. Users may interpret these cues as indicators of credibility and expertise. Particularly in low-trust environments, people rely on these mental proofs to assess credibility and sincerity (46). Previous work has shown that AI systems can simulate these proofs by crafting convincing arguments that users mistake for deep cognitive depth, therefore amplifying perceived expertise and trust (10). Understanding how these perceptions shape user interaction with AI is an important challenge for human-computer interaction research.

A growing research area highlights the tendency of overreliance on AI suggestions, accepting them even when they are incorrect, which can lead to poorer decision outcomes than independent reasoning (44; 7; 27; 5). Interface interventions, such as explainable AI (44; 48), cognitive forcing functions (7), and clickable source references (27), have shown some success in reducing overreliance, but often at the cost of usability or user satisfaction (7).

Much of the previous research has focused on binary decision-making tasks and has overlooked the impact of AI on open-ended tasks. Open-ended tasks generally require analysis and synthesis skills that are vital for human cognitive development. Unlike binary decision-making, which often yields clear answers, open-ended tasks require deeper thinking and understanding, resulting in more nuanced responses. They involve interpreting various factors, such as creating solutions that may not be straightforward. This nuance is crucial for developing higher-order cognitive skills, according to Bloom’s taxonomy (6; 21; 38). Frequent usage of AI has also been linked to cognitive offloading, shifting users from "doing" to "overseeing" the AI work (29) as well as weakening neural indicators of mental engagement (28). This shift may reduce opportunities to develop higher-order skills (29; 28; 8; 33).

Through an experiment, we investigate how users incorporate AI suggestions into their responses to open-ended tasks and further analyze their behaviour after completing each task. Building on the idea of overreliance, we provide additional evidence that people likely experience some degree of AI influence, i.e. the adoption of wording, structure, and sentiment. This is not necessarily a concern in some contexts — perhaps producing outputs that are similar to high-quality AI outputs is beneficial. Specifically, in a small experiment, we measure the effects of AI suggestions on textual similarity, sentiment alignment, and perceived cognitive load. Our findings illustrate the transition from more noticeable to more subtle yet meaningful ways in which generative AI can influence users’ responses.

In general, we might expect that as people see AI suggestions, their outputs become more similar to the AI outputs. In some cases, this may be the user’s intention. In other cases, it might be cause for concern for the user or other people affected by the content. In a writing context, even seeing an AI suggestion might warp a creator’s eventual output.

Therefore, the open question, and our focus, is what happens when users do not copy verbatim: to what extent do suggestions still imprint wording, structure, and sentiment on open-ended writing. To answer this, we argue that a single metric is insufficient; influence is not monolithic, and can manifest itself as lexical, structural, or tonal alignment.

In this paper, we use the term adoption to refer to the incorporation of AI output into a participant’s written response, rather than to the general adoption of AI tools (e.g., increased ChatGPT usage). In practical terms, adoption refers to the extent to which a participant’s final text aligns with the provided suggestion in wording, structure, meaning, and sentiment. We use overreliance to refer to the broader concern from prior work. We discuss the main differences and when adoption becomes a concern in the Discussion section.

We find that participants exposed to the fully formed AI suggestion exhibit higher levels of AI adoption. This adoption is reflected in the increase in textual and sentiment similarity metrics. Building on these findings, we designed and implemented an interactive writing interface that displays real-time metrics to users on AI response adoption. We evaluate this interface through a follow-up, exploratory think-aloud study, which shows that reflection on such metrics can increase users’ awareness of suggestion reuse.

Our work produces evidence and design practices for LLM tools:

- •

We conducted an empirical study with participants to assess whether viewing AI output leads users to produce more similar output.

- •

We identified similarity metrics that may be particularly affected by AI assistance.

- •

We design and evaluate an interface intervention that can promote reflective engagement with AI responses in writing workflows.

### 2. Related Work

#### 2.1. Mental Proofs

46 describe mental proofs as a set of behaviours and cues that enable people to externalize their internal cognitive states (42), such as understanding, sincerity and intention (18). In low-trust environments, people often rely on these signals to assess others’ credibility (16). For example, when reading news articles, we must rely on cues such as author credibility and presentation quality rather than directly verifying the facts. GenAI systems can simulate these mental cues by constructing convincing, well-structured arguments that lead users to mistake the AI’s output for genuine responses, with cognitive depth and accuracy. (46; 23)

Similarly, 18 analyzed how AI writes apologies and divided important patterns (e.g., interaction, offence, recipient, and offender). They showed how these elements map onto the structure of effective apologies in human–machine contexts. For example, a customer-service bot that mishandles a transfer may explicitly note the mistake, recognize the user’s inconvenience, apologize, attribute the failure to a system issue, and commit to an immediate fix and prevention. This example illustrates how AI can convincingly simulate the cues of genuine remorse. (18; 46)

Moreover, by amplifying these simulated cues: consistent tone, structure, and ensuring statements, GenAI can trigger a false sense of rapport or expertise. Users subconsciously attribute a level of "understanding" or "intent" to the AI, leading them to accept its suggestions with little scrutiny. (15)

#### 2.2. Overreliance on AI

Given the convincing cues that AI can externalize (18; 46; 15), a consistent finding in human-AI interaction research is the tendency for users to rely too heavily on AI suggestions. In this context, overreliance refers to accepting AI-generated suggestions even when those suggestions are incorrect. This overreliance on AI often leads to more incorrect decisions than those made independently, without AI assistance (24; 25). This unbalanced trust in AI output highlights the potential risks of overreliance on GenAI. (44; 7; 27; 5)

7 proposed cognitive forcing functions, which are interface-level interventions designed to stimulate user analytical thinking. These include requiring users to choose between viewing the AI suggestion and the AI-generated response confidence levels, among other measures. These efforts reduced overreliance. However, benefits often come at the cost of usability and user satisfaction.

44 connected overreliance to a cost–benefit framework with a model that assesses the perceived benefits of using an AI suggestion in a cognitively costly task (34). The authors demonstrated that people selectively engage in AI explanations, depending on the perceived difficulty of the task and the potential benefits that AI offers. In the context of our research, this framework provides reasons for achieving balanced experiences when utilizing AI to solve tasks. For example, when verifying the AI’s recommendation is less cognitively costly than solving the task independently, users rely on it less.

27 extended this discussion by showing that AI explanations and clickable sources influence user trust in AI. Although explanations increased trust in both correct and incorrect suggestions, sources had a more balanced effect, promoting appropriate reliance on correct suggestions and discouraging acceptance of incorrect ones. Clickable references embed links or buttons directly within the information source, allowing users to select them to reveal the original supporting material. These links encourage users to verify each assertion and trace its origin. Early studies find that providing access to source material can nudge users toward more critical evaluation (27; 40). However, users should remain cautious about fabricated sources, as shown by a study by 3. Relatedly, 26 found that when AI output contains uncertainty, for example, "I’m not sure, but…", users are less likely to overrely on incorrect responses, though the effect depends on how the uncertainty is phrased. This suggests that the form of AI assistance, not just its presence, shapes the extent to which users adopt it.

44 show that explanations, also known as Explainable AI or XAI, can prevent users from blindly accepting wrong suggestions, but only if those explanations make it easier or more worthwhile to check the AI’s advice than trust it. Explainable AI surfaces the model’s underlying reasoning through logical rules or visual path highlights, helping users judge when to trust or question the AI’s output. By formalizing explanation use within a cost–benefit framework, explanation clarity, and incentives, they show that easily digestible explanations reduce overreliance (44; 48; 12; 11).

41 contributed to this discussion by demonstrating that increasing task complexity can reduce reliance on generative AI and minimize AI plagiarism. In their experiment, the results showed a decrease in AI-generated content as tasks progressed toward higher-order thinking. This supports the premise that designing cognitively demanding tasks can reduce reliance on AI output.

These findings emphasize the complexity of calibrating AI and trusting interfaces to avoid overreliance. Recent work has further formalized this challenge. 17 proposed a decision-theoretic framework that grounds reliance measurement in statistical decision theory, showing that human-AI teams frequently underperform the AI alone because users follow AI recommendations even when doing so leads to worse outcomes than relying on their own judgment. However, previous studies on overreliance have primarily examined multiple-choice decisions with binary, correct or incorrect answer options. Our work aims to extend this to open-ended tasks, where the effects can be more nuanced. Specifically, our multi-metric approach complements 41 and 9 by providing quantitative similarity metrics that measure the degree to which AI suggestions shape written output, rather than inferring reliance from performance outcomes or self-reported measures alone.

#### 2.3. Similarity Analysis Between Human and AI Text

Prior work has examined the influence of AI in interactive writing contexts. CoAuthor (30), and Wordcraft (47) are two human-AI collaborative writing systems that study how users adopt or resist AI-generated suggestions during writing. CoAuthor provides a large-scale dataset of human writing sessions with GPT-3, revealing how writers incorporate and modify suggestions across different stages of writing. Wordcraft is a creative writing editor designed to support writers through a range of AI-assisted operations, including elaboration, rewriting, and continuation. Both systems primarily focus on behavioural patterns and user experience, leaving open the question of how to quantify the extent to which AI shapes the final text.

Research in AI-mediated communication (AMC) has similarly found measurable shifts in style and sentiment attributable to AI exposure. 32 identified a positivity bias in AI-generated communication, while 13 examined how sentence- versus message-level suggestions differ in adoption patterns, and 39 observed changes in text complexity and sentiment in social media posts following ChatGPT’s public introduction.

Our study extends this line of inquiry. While CoAuthor and Wordcraft characterize how writers interact with AI behaviourally, and AMC studies document population-level linguistic shifts, we contribute a controlled experiment for quantifying adoption across multiple textual dimensions simultaneously. This approach allows us to decompose AI influence into distinct axes and test which dimensions are affected by different assistance formats.

#### 2.4. Impact on Cognitive Engagement

Beyond trust and accuracy, researchers have also explored the cognitive implications of GenAI. In a survey with knowledge workers, 29 found that frequent use of GenAI tools was associated with a self-reported decrease in mental effort. Participants described a shift from "doing" to "overseeing" when using AI tools to solve day-to-day tasks. This shift may reduce the opportunity for cognitive development, particularly in tasks that require judgment and original thinking.

9 reported that users preferred the automated AI assistance condition for perceived ease and less effort, describing this as a discrepancy between convenience preference and cognitive benefit.

In Bloom’s taxonomy framework, originally proposed by Benjamin Bloom in 1965 and widely used in educational settings, this shift corresponds to a lower level of engagement with higher-order cognitive processes. Rather than formulating their arguments (Analysis) or integrating diverse ideas into new perspectives (Synthesis), users often accept AI-produced text with limited alteration, thus undermining vital practice in these cognitive skills. (6; 21; 38)

On a physical level, 28 conducted a large-scale EEG study to investigate how external AI support influences neural indicators of cognitive engagement during essay writing. They found that participants who relied on LLMs exhibited significantly weaker neural connectivity than those who wrote without assistance. This pattern suggests that AI assistance immediately reduces cognitive effort and may reduce neural processes associated with analytical thinking and memory retrieval.

Although it is not a central focus of our study, we also administered a TLX (cognitive load) questionnaire as a post-task self-reflection component of our main experiment. We elaborate on this in the Results and Discussion sections.

### 3. Methods

To investigate how users adopt AI suggestions into open-ended writing and how this aligns with users’ own accounts of AI output usage, we conducted a within-participant, counterbalanced across tasks, user study, approved by the Simon Fraser University Research Ethics Board (30003047). For the main experiment, participants resolved two tasks based on a short reference text. We then prototyped and conducted a follow-up think-aloud evaluation of a writing interface intervention.

#### 3.1. Materials and Tasks

In the main experiment, participants completed two open-ended tasks based on the short story "After Twenty Years" by O. Henry (20). We chose this text because of its concise form, which allows quick reading while simultaneously requiring cognitive engagement for interpretation. Its twist ending and well-rounded characters provide participants with many points for analysis while minimizing background knowledge variance. For the writing interface intervention, participants completed an open-ended writing activity in which they wrote three paragraphs on a topic of their choice.

#### 3.2. Participants and Recruitment

We recruited participants on Prolific across phases. Participants reported fluency in English and at least secondary-level education. We compensated the participants at £6.00/hr, with an additional £1.00 bonus in some variations of the experiment. For the think-aloud interface intervention study, we recruited undergraduate students from various course backgrounds.

To achieve precise similarity metrics in the main experiment, we explicitly instructed participants not to use any external large language models. Instead, they should use the AI suggestion provided in the interface of our experiment, if available. We manually examined the participants who pasted content in the experiment and found a high likelihood that they were produced by external LLMs, given their completion time and pasted content compared to the final response (37; 2). A recent study found that 33-46% of crowd-workers rely on LLMs for text production tasks (45). Although using external LLMs for this study could be informative for the topic, we focused on task completion, as it could affect our measurements. We also consider this to warrant further exploration in future experiments.

#### 3.3. Pilot Experiment

We conducted a small pilot experiment in two iterations. First, a brief, time-limited pilot with 5 participants was conducted to validate the setup; it revealed that the time constraints and phrasing produced short, surface-level responses, limiting the interpretability of the adoption and reflection data (14; 4). We then conducted an untimed iteration with 11 participants using revised prompts and incentives. The pilot data were used solely to inform the design change and were not treated as evidence for the main experiment.

Across the pilot iterations, the key changes were: (i) removing strict time limits, (ii) removing "brief" and "short" prompt phrasing that encourages minimal responses both to the task and self-reflection, (iii) adding a small bonus to incentivize richer reflections, and (iv) changing the experiment design from between-subjects to a counterbalanced within-subjects design to reduce sensitivity to individual differences in writing ability and baseline similarity. These changes were motivated by our goal of comparing observed adoption with perceived adoption, which requires sufficiently rich responses and reflections.

#### 3.4. Main Experiment

We recruited a total of 54 participants on Prolific. After data collection, we excluded 7 participants who used external tools, resulting in 47 valid participants. Each user completed two tasks: an analysis task and a synthesis task. The tasks were designed to be cognitively engaging to reduce trivial responses and better support conclusions about adoption behaviour (41).

##### Assistance Format

The study included two tasks: one analytical and one creative. In assisted trials, the format of AI assistance depended on the type of task. For the analytical task, participants received a fully direct AI response that addressed the prompt. For the creative task, participants received a scaffolded suggestion (e.g. key points and proposed structure). This asymmetric assistance design allowed us to compare the adoption pattern between two common GenAI support models.

Before the study, the research team reviewed AI suggestions for both tasks to ensure factual accuracy and quality. No misleading or incorrect content was included, ensuring that observed adoption effects reflect natural exposure to real-scenario suggestions rather than a manipulation of suggestion quality or correctness.

To illustrate the experimental setup and task interface, we include a screenshot in Figure 1.

Figure 1. Experiment interface showing: (a) reading of the reference text, (b) presentation of AI suggestions, and (c) participant response entry field. These screenshots illustrate the environment in which participants completed both tasks.

The specific task prompts and the AI suggestion used in both conditions are provided in Appendix A.

##### Counterbalancing and Assignment

To mitigate task order effects, task order and AI assistance were counterbalanced (Latin-square style). Participants faced an AI suggestion on at least one task, with the order of exposure varying between participants. This counterbalancing enables within-participant comparisons across tasks while allowing between-subject variation in order and task pairing.

##### Procedure

The participants first read the story in the interface and then completed two tasks in sequence. The interface presented a prompt and a text editor, along with the AI suggestion panel for the assisted trials. Participants were not informed of the study’s specific hypothesis. After each task, participants completed a brief post-task reflection survey, including the NASA-TLX questionnaire (19), which measures self-reported cognitive effort. In assisted trials, participants also completed open-ended reflection questions, from which the perceived level of AI suggestion use was derived through thematic coding.

##### Counterfactual baseline

To compare AI-present and AI-absent writing using the same adoption metrics, we score every response against a fixed, task-specific AI suggestion text. In AI-present trials, this is the suggestion shown to the participant. In no-AI trials, participants don’t see a suggestion; however, we still compute similarity between their response and the held-out task AI suggestion shown to other participants for the same prompt. We refer to these scores as a counterfactual baseline. For the creative task, the AI suggestion took the form of scaffold bullet points rather than a full direct answer. Accordingly, the counterfactual baseline for that task was computed against the bullet points, not against a hypothetical full-text response. Similarity scores across conditions should therefore be interpreted relative to each condition’s baseline.

##### Similarity Metrics

For each participant response AA, we quantify similarity to the fixed AI suggestion of the task BB. In trials without an AI suggestion, we still compare AA to the same task-level suggestion as a counterfactual baseline, allowing direct AI vs. no-AI comparisons. We report four complementary measures (35):

- (1)

Jaccard similarity (lexical overlap) We compute the Jaccard coefficient (22) on sets of word tokens extracted with the regex pattern [A-Za-z’]+. The Jaccard similarity is then computed as the number of unique tokens shared by both texts divided by the number of unique tokens appearing in either text. Values closer to 0 indicate smaller lexical overlap, while values closer to 1 indicate greater lexical overlap.

- (2)

POS TF-ISF cosine (structural alignment) Following 43, we perform part-of-speech tagging (POS-tagging), form lemma+class terms and compute the cosine similarity between the vectors. Values closer to 0 indicate weaker structure alignment, while values closer to 1 indicate stronger alignment.

- (3)

SBERT cosine similarity (semantic alignment) We encode each text with Sentence-BERT (36) using roBERTa11
1

https://huggingface.co/sentence-transformers/roberta-base-nli-mean-tokens and compute cosine similarity between the embeddings. Values closer to -1 indicate weaker semantic alignment, while values closer to 1 indicate stronger alignment.

- (4)

Aspect sentiment match (sentiment alignment) In line with the aspect-level sentiment consistency metric proposed by 49, we split each text into sentences and compute the TextBlob polarity for each one (31; 1). We then compare the aspect sentiment labels (positive/negative/neutral) between the participant response and the task suggestion. Values closer to 0 indicate weaker sentiment alignment, while values closer to 1 indicate stronger alignment.

Together, these metrics capture adoption at the lexical, structural, semantic, and sentiment levels. We note that individual similarity values are expected to be high even in no-AI trials because both the participant response and the AI suggestion address the same short story. This expected baseline is precisely why relying on a single similarity metric is insufficient.

##### Workload (cognitive engagement).

We collected a NASA-TLX-style workload measure after tasks as an exploratory context. We report these and interpret null/non-robust effects carefully, consistent with our goal of focusing on AI output adoption rather than cognitive outcomes.

##### Statistical hypothesis tests

Across the analysis, we report condition means and standard deviations (MM, S​DSD), mean differences (Δ\Delta), and effect sizes (dzd_{z} for paired and Cohen’s dd for independent-group designs). We conduct two-sided hypothesis tests at a significance level α=.05\alpha=.05. The null hypothesis for each metric is that AI presence does not change the outcome relative to no-AI. Conversely, the alternative hypothesis is that AI assistance changes the outcome.

Our statistical tests are exploratory and hypothesis-generating. We report mean differences and effect sizes to characterize the magnitude of observed patterns, and we treat pp-values as descriptive indicators of strength rather than definitive evidence. This is important because we evaluate multiple related outcomes that may be correlated. Accordingly, we interpret the pp-values cautiously (Tables 1, 2, 4, and 3). While future work could pre-register a primary adoption metric, we treat the set of metrics as exploratory and complementary.

##### Qualitative analysis.

We analyzed post-task reflections from AI-present trials in the main experiment to examine what participants reported adopting or rejecting (ideas, structure, phrasing) and how they justify those choices. The first author conducted thematic coding without a pre-defined codebook, with categories generated inductively across multiple passes over the reflections. The second author reviewed the final results. The relatively small set of observations allowed for thorough analysis. Given the exploratory nature of the study and the relatively small sample, formal inter-rater reliability was not computed. We interpret the qualitative findings as descriptive.

#### 3.5. Think-Aloud Study of the Implemented Interface Intervention

To evaluate whether an interface intervention can shape how users interpret and incorporate AI suggestions during writing, we conducted a follow-up think-aloud study using the implemented interface.

##### Interface.

We prototyped a web-based editor in which participants could paste any AI output they used as reference “snippets.” The participants completed the task entirely within the editor. As they wrote, the sidebar indicators updated in real time to show how closely the draft aligned with the added snippets, making the adoption more noticeable without constraining whether participants accepted, edited or ignored the suggestions. We include a representative screenshot in Figure 2.

Figure 2. Participants draft text in the main editor (left) while a side panel (right) provides feedback on similarity to an AI suggestion and saved snippets of AI outputs for reference and review.

##### Procedure.

Participants completed an open-ended writing activity by composing three paragraphs on a topic of their choice. For this task, they could use any LLM however they wished (e.g., brainstorming, drafting, or proofreading) and were asked to paste any AI output they referenced into the application as snippets. We specifically permitted the use of external LLMs for this task, as participants were able to record the exact suggestions they consulted, allowing us to compare their writing directly with those outputs and compute similarity measures accurately.

Before starting, we provided a quick overview of the editor, the snippet panel, and the real-time alignment feedback. We recorded the screen and audio and collected written debrief responses. After the task, participants took part in a debrief interview focused on (i) how they decided to adopt or reject aspects of the AI output (e.g., phrasing, structure, ideas) and (ii) which interface elements, if any, made AI influence more noticeable or easier to reflect on.

##### Analysis.

The first author open-coded the transcripts, focusing on two phenomena identified in advance: moments where participants made a clear decision to adopt, edit, or reject part of an AI suggestion, and moments where the sidebar metrics influenced participants. Given the small sample (n=4n=4), we treat the analysis as illustrative and use direct quotes to ground each theme.

### 4. Results

Across 47 participants in a counterbalanced within-subject design, exposure to an AI suggestion increased alignment between participants’ writing and the AI output on multiple adoption measures. Overall, AI-present trials showed higher lexical, structural, and aspect-level sentiment similarity than no-AI trials, whereas semantic similarity increased but did not reach statistical significance. These effects were driven primarily by the analytical task, where participants received a fully formed direct answer from the AI. In the creative task, where participants received a scaffolded suggestion, adoption effects were smaller, and only sentiment alignment increased significantly.

Self-reflections that reported using the suggestion often described it as helpful for direction and framing rather than as verbatim copying. These results motivate measuring AI influence in writing as multi-dimensional adoption rather than binary copying, and they set up our interface intervention aimed at making this influence more visible.

#### 4.1. Main Experiment

##### Similarity Metrics.

To quantify the adoption of AI output, we measured the similarity between each participant’s response and the AI’s task suggestion using four complementary metrics (lexical, structural, semantic, and sentiment alignment). For no-AI trials, we compared responses to the same task suggestion as a counterfactual baseline.

Overall (Table 1), AI assistance increased similarity on lexical overlap (Jaccard: M=0.108M=0.108 vs. 0.0930.093, Δ=0.015\Delta=0.015, p=.050p=.050, dz=0.294d_{z}=0.294), structural similarity (POS TF-ISF cosine: M=0.042M=0.042 vs. 0.0250.025, Δ=0.017\Delta=0.017, p=.029p=.029, dz=0.329d_{z}=0.329), and aspect sentiment match (M=0.092M=0.092 vs. 0.0400.040, Δ=0.052\Delta=0.052, p=.004p=.004, dz=0.444d_{z}=0.444). SBERT cosine was higher with AI (M=0.676M=0.676 vs. 0.6420.642, Δ=0.034\Delta=0.034) but not statistically significant (p=.086p=.086, dz=0.256d_{z}=0.256).

Comparisons within tasks (Table 2) indicate that this pattern is primarily driven by the analytical task, where we provided participants with a direct-answer AI suggestion. In that task, AI assistance increased Jaccard similarity (0.1280.128 vs. 0.1040.104, Δ=0.024\Delta=0.024, p=.003p=.003, d=0.900d=0.900), POS TF-ISF cosine (0.0610.061 vs. 0.0350.035, Δ=0.026\Delta=0.026, p=.022p=.022, d=0.692d=0.692), and aspect sentiment match (0.1470.147 vs. 0.0700.070, Δ=0.077\Delta=0.077, p=.002p=.002, d=0.945d=0.945), while SBERT cosine was not significantly different (p=.257p=.257). In the creative task, where we provided participants with a scaffold AI suggestion, only the aspect sentiment match increased significantly (0.0360.036 vs. 0.0110.011, Δ=0.024\Delta=0.024, p=.021p=.021, d=0.695d=0.695); differences in Jaccard, POS TF-ISF cosine, and SBERT cosine were not significant (p​s≥.129ps\geq.129).

Together, these results indicate that AI assistance increased alignment with the suggestion, with the strongest adoption effects in the direct response AI suggestion condition.

Table 1. Overall AI vs. no-AI differences in similarity (paired-samples t-test; paired by participant; tasks counterbalanced; significant rows bolded and marked with *).

Metric |
No-AI, M (SD) |
AI, M (SD) |
Δ\Delta |
pp |
Cohen’s dzd_{z} |

Jaccard |
0.093 (0.031) |
0.108 (0.038) |
0.015 |
0.050* |
0.294 |

POS TF-ISF cosine |
0.025 (0.024) |
0.042 (0.044) |
0.017 |
0.029* |
0.329 |

SBERT (RoBERTa) cosine |
0.642 (0.104) |
0.676 (0.082) |
0.034 |
0.086 |
0.256 |

Aspect sentiment match |
0.040 (0.055) |
0.092 (0.093) |
0.052 |
0.004* |
0.444 |

Table 2. Within-task AI vs. no-AI differences in similarity to the task suggestion (independent-samples t-test; significant rows bolded and marked with *).

Task |
Metric |
No-AI, M (SD) |
AI, M (SD) |
Δ\Delta |
pp |
Cohen’s dd |

Analytical |
Jaccard |
0.104 (0.023) |
0.128 (0.029) |
0.024 |
0.003* |
0.900 |

|
POS TF-ISF cosine |
0.035 (0.026) |
0.061 (0.046) |
0.026 |
0.022* |
0.692 |

|
SBERT (RoBERTa) cosine |
0.670 (0.128) |
0.707 (0.091) |
0.037 |
0.257 |
0.335 |

|
Sentiment match |
0.070 (0.061) |
0.147 (0.097) |
0.077 |
0.002* |
0.945 |

Creative |
Jaccard |
0.082 (0.034) |
0.087 (0.035) |
0.006 |
0.582 |
0.162 |

|
POS TF-ISF cosine |
0.015 (0.016) |
0.021 (0.031) |
0.006 |
0.393 |
0.252 |

|
SBERT (RoBERTa) cosine |
0.615 (0.065) |
0.643 (0.058) |
0.028 |
0.129 |
0.451 |

|
Sentiment match |
0.011 (0.028) |
0.036 (0.041) |
0.024 |
0.021* |
0.695 |

##### Self-Reported Usage and Qualitative Analysis.

After each AI-assisted trial, participants completed a brief post-task reflection survey that included two open-ended questions asking (i) whether or how they used the given AI suggestion and (ii) whether they would have completed the task differently if not displayed with a suggestion. Given that we had 47 participants, each of whom completed a task with and without assistance, we collected 47 instances of reflection in total.

Overall, 37/47 (78.7%) of AI-present responses reported using the AI suggestion: 22 from the creative task and 15 from the analytical task. When participants used the suggestion, they more often described it as beneficial than not (26/37, 70.3%), whereas 10/47 (21.3%) of all participants who were shown the AI suggestion explicitly reported that it was not helpful.

In terms of how they perceived themselves to adopt the suggestion, 22/37 (59.5%) responses referenced the suggestion that gave direction, compared to 10/37 (27.0%) mentioned wording or paraphrasing. These patterns were similar in proportion across task types. For the creative task, 16/22 (72.7%) responses were rated as helpful, whereas for the analytical task, 10/15 (66.7%) were rated as helpful.

For the second question, in which participants were asked whether they would complete the task differently without an AI suggestion, 28/47 (59.6%) AI-present tasks were tagged as indicating that they would answer differently. Of these, 15/47 (31.9%) referenced that the idea/content would be different, and 11/47 (24.5%) referenced that the wording/grammar would be different.

In summary, these provide a complementary lens on AI adoption, in which most participants perceived themselves as using the suggestion and many anticipated that their responses would change without it. This is directly connected to our study goals of measuring AI output adoption and perceived influence, offering a user-centred account of how suggestions shape writing even when they are not described as direct copying.

##### Cognitive Load and Time.

In general, we did not observe reliable differences between AI and non-AI conditions in total TLX scores or completion time for either task (Table 3 and Table 4).

Table 3. Within-task AI vs. no-AI differences in NASA-TLX ratings (independent-samples t-test; significant rows bolded and marked with *).

Task |
Metric |
No-AI, M (SD) |
AI, M (SD) |
Δ\Delta |
pp |
Cohen’s dd |

Analytical |
Mental demand |
5.043 (1.821) |
4.667 (1.685) |
-0.377 |
0.465 |
-0.215 |

|
Physical demand |
2.435 (1.532) |
2.917 (1.692) |
0.482 |
0.312 |
0.298 |

|
Rushed |
2.652 (1.301) |
2.250 (1.152) |
-0.402 |
0.267 |
-0.328 |

|
Accomplishment |
3.478 (1.563) |
3.458 (2.043) |
-0.020 |
0.970 |
-0.011 |

|
Effort |
5.087 (1.564) |
4.792 (1.474) |
-0.295 |
0.509 |
-0.194 |

|
Insecurity |
2.957 (1.364) |
2.208 (1.444) |
-0.748 |
0.075 |
-0.532 |

|
TLX total |
3.609 (0.799) |
3.382 (0.888) |
-0.227 |
0.363 |
-0.268 |

Creative |
Mental demand |
5.250 (1.539) |
5.609 (1.438) |
0.359 |
0.414 |
0.241 |

|
Physical demand |
3.458 (2.064) |
2.783 (1.536) |
-0.676 |
0.211 |
-0.370 |

|
Rushed |
2.292 (1.459) |
3.130 (1.740) |
0.839 |
0.080 |
0.523 |

|
Accomplishment |
3.500 (1.818) |
3.522 (1.880) |
0.022 |
0.968 |
0.012 |

|
Effort |
4.917 (1.472) |
5.739 (1.176) |
0.822 |
0.040* |
0.616 |

|
Insecurity |
2.500 (1.532) |
2.913 (1.474) |
0.413 |
0.352 |
0.275 |

|
TLX total |
3.653 (0.965) |
3.949 (0.748) |
0.296 |
0.247 |
0.342 |

Table 4. Within-task AI vs. no-AI differences in completion time in minutes (independent-samples t-test; significant rows bolded and marked with *).

Task |
Metric |
No-AI M (SD) |
AI M (SD) |
Δ\Delta |
pp |
Cohen’s dd |

Analytical |
Completion time (min) |
15.204 (9.785) |
18.246 (10.321) |
3.042 |
0.306 |
0.302 |

Creative |
Completion time (min) |
16.250 (8.905) |
20.875 (13.861) |
4.625 |
0.178 |
0.399 |

Most comparisons did not reach statistical significance. In the analytical task, AI assistance was associated with slightly lower mental demand, rushedness, effort, and insecurity. In the creative task, AI assistance was associated with slightly higher effort (the only statistically significant comparison), mental demand and rushedness, and a higher TLX total, although these differences were not statistically significant (all p > .05). The completion time also did not differ significantly between the AI and non-AI conditions for either task (Table 4).

These results suggest that AI suggestions did not reliably reduce perceived workload or time-on-task, and any potential effects are likely small or context-dependent. Larger-scale studies would be valuable for estimating these effects more precisely and for testing whether they reliably emerge for particular task types and assistance formats.

#### 4.2. Think Aloud Experiment on the Proposed Writing Interface Intervention

To evaluate whether real-time similarity feedback changes how users perceive and incorporate AI suggestions during writing, we conducted a think-aloud study with four university students using our reflective writing editor intervention. The interface was directly informed by the main experiment findings: given that participants showed measurable AI adoption across multiple dimensions yet often described their use as limited to ideas or direction, we designed feedback that makes these dimensions visible in real time, targeting the gap between perceived and actual adoption.

##### The metrics shaped writing strategies and calibrated reliance

Participants frequently described the sidebar metrics as a calibration aid that shaped writing choices (e.g., paraphrasing, restructuring, or deciding when to stop consulting the AI or to ask for a follow-up). The value of the interface was often framed as not preventing or impeding work, but as helping participants decide how much to use AI.

Participant 3 directly noted that "[It] was a very helpful tool in ensuring I was mindful of my AI usage," while Participant 4 emphasized its value as a boundary: “as a reluctant AI user, it’s helping me… in that kind of ethical way of… being aware of the impact.”

Participant 1’s reflection was slightly different: they described using AI mainly when they “don’t know the wording,” and the interface helped them feel reassured that reliance was not as high as expected: “I definitely thought… the structure would have been a little bit higher.”

Interestingly, calibration was not always about minimizing reliance. During the task, Participant 2 reflected: "I’m using a bit of the suggestion… but I could rely more on it from what I’m seeing on the panel.” This highlights an important nuance: depending on users’ goals, the same feedback can serve as a calibrated signal rather than uniformly discourage AI use.

##### The interface made AI influence identifiable during writing

Most participants used the bars as a real-time mirror of AI use. Most reported observing changes in the indicators while copying or paraphrasing AI-generated text. As participant 4 noted, the bar "jumped up right when I copied and pasted something in there. So I was like, OK, that was helpful because like I definitely did that." Participant 3 described trying to make the bars "go lower, like down, down, down," treating the indicator as a live constraint that supported mindful writing. Participant 2 said they "always use AI detectors at the end of my papers to make sure that it’s actually consistent with what I wrote. So having this going on as I’m writing the paper would save me time in the end."

These findings demonstrate that students can reflect on and adjust their adoption in real time, rather than treating it as a policing mechanism. By showing that participants used the bars to monitor, calibrate, and strategically adjust their engagement with AI, this study illustrates that the tool can be helpful as reflective writing support.

### 5. Discussion

Our main experiment results suggest that seeing generative AI output can measurably shape open-ended writing, even when participants do not copy verbatim. Across analytical and creative tasks, exposure to an AI suggestion increased alignment between participants’ responses and the AI output in lexical, structural, and sentiment overlap. This effect was strongest when participants were shown a direct-answer output rather than a scaffolded suggestion. Together, these findings support our core motivation: AI influence on writing is not binary. It often appears as a subtle adoption of wording, organization, and even affect, and these measurements should be available for users’ reflection, which informed our reflective writing interface intervention.

##### Adoption vs. Overreliance

It is important to sharpen the discussion between adoption, which we measure, and overreliance, which carries normative weight. Our study quantified textual alignment between participant responses and AI suggestions. It does not assess whether any given instance of adoption affected performance or correctness outcomes. Adoption becomes a concern, though not exclusively, (i) when the user is unaware of the extent to which AI has shaped their writing, (ii) when adoption goes against the purpose of the task, for example, in educational assessments designed to elicit original reasoning, and (iii) when the resulting text misrepresents the author’s perspective or views. Determining whether and when observed adoption entails overreliance and effects on the mentioned concerns requires additional outcome measures, such as writing quality assessment, learning outcomes, task alignment, and correctness, which we identify as important directions for future work. In the current study, we use the term adoption to describe what we measure and reserve the term overreliance as a normative label for contexts in which this is demonstrated to be harmful.

##### AI output adoption is multi-dimensional

We argue that AI influence in writing is not monolithic, and our findings reinforce that a single metric may miss meaningful forms of adoption. Some forms are not obvious to the naked eye, such as sentiment alignment. At the same time, semantic similarity increased but did not reliably reach significance, suggesting that the metrics we used capture only part of the influence landscape. In practice, there may be other dimensions of similarity that matter for writing that are not fully represented by standard semantic measures. This motivates treating AI influence as a multi-dimensional phenomenon rather than reducing it to a single indicator.

The clearest similarity lever in our study was the assistance format. Direct-answer suggestions in the analytical task produced large and consistent adoption effects, while scaffolded suggestions yielded smaller effects. This has direct design implications: reducing unintended or excessive adoption on written tasks may be less about adding warnings and more about changing the form of help. Scaffolds may better preserve degrees of freedom, based on the limited measurements from our study. However, scaffolds primarily address surface-level expression, whereas overreliance on AI-generated ideas and arguments can occur regardless of assistance formats, since users may still adopt the content of the AI suggestion. More broadly, our results reinforce that open-ended writing is a distinct interaction setting from binary decision-making and that interventions should be guided by the purpose of writing; for example, this may apply differently across learning and professional environments.

##### Reflective metrics

Although not directly measured in our main experiment, our interface intervention addresses a potential gap between participants’ self-reported use of suggestions and their actual alignment with AI output. Reflective similarity feedback may function as a lightweight cognitive forcing mechanism: it introduces a moment of reflection without blocking progress. This shift emphasizes the opportunity to move away from policing toward agency—supporting user awareness rather than external enforcement. At the same time, reflective tools should be designed carefully so they do not become compliance instruments, or implicitly define “good writing” as merely “low similarity.” The goal is not to prohibit reuse, but to make adoption choices more visible and reflective.

##### Null and mixed results on workload

We did not observe reliable reductions in perceived workload or time-on-task. This is important evidence that AI assistance may not uniformly reduce writing effort. One interpretation is that AI shifts where effort is spent rather than reducing it, consistent with prior work 29. Users may expend less effort generating raw content but more effort evaluating and integrating suggestions. In open-ended tasks, especially, deciding whether to follow or resist a well-formed suggestion can be cognitively demanding.

##### Broader implications for adoption and authorship

Our work extends the discussion of AI influence on writing beyond plagiarism and correctness. We treat it as a multidimensional issue of similarity and reflection: not all reuse is harmful, but users should have visibility into how much the system shapes what they write. This reframes the ethical concern from solely external policy enforcement to a more balanced, user-centric model of reflective empowerment. One that can support education and accountable authorship. The stakes of adoption differ across contexts: in educational settings, AI influence may undermine assessments, while in professional contexts, it raises questions about accountability. Future work should explore the real-world consequences of AI adoption in specific contexts.

##### Limitations and future work

Our study is scoped to the tasks and settings we evaluated, and replication across genres and contexts would strengthen generalizability. One limitation of the current design is that task type and assistance format co-vary: the analytical task used a direct-answer suggestion while the creative task used a scaffolded suggestion. This means that we cannot fully determine whether the stronger adoption effects in the analytical condition reflect the format of assistance, the nature of the task, or an interaction between the two. Future work that focuses specifically on measuring these interactions should independently vary task type and assistance format.

Another consideration is the ecological validity of our sample. Participants were Prolific crowd-workers completing a low-stakes short-story analysis task, which may not generalize to high-stakes or professional settings. Additionally, prior familiarity with the O. Henry reference text was not pre-screened. However, since both AI and no-AI conditions use the same reference text in a counterbalanced design, any differential familiarity is unlikely to bias AI versus no-AI comparisons.

The follow-up interface evaluation should be understood as a design provocation, an initial exploration of where real-time similarity feedback can support reflective writing. With only four participants, we cannot make strong claims about usability or effect. The open-ended nature of the topics in the interface study reflects a naturalistic AI-assisted writing condition and allows us to compute similarity directly against the AI output each participant actually consulted. However, this also introduces variability that limits systematic cross-participant comparison. Future work should extend this with a controlled design setting.

### 6. Conclusion

Generative AI output can shape open-ended writing in ways that extend beyond verbatim copying. In this paper, we examined how exposure to AI suggestions influences users’ written responses to analysis and synthesis tasks, leading to a multidimensional alignment between a participant’s text and an AI suggestion. In our main experiment, AI-assisted trials showed higher alignment than no-AI trials on lexical overlap, structural similarity, and aspect-level sentiment match, whereas semantic similarity showed a trend upward but was not consistently significant. The strongest effects appeared when participants received a fully formed direct-answer AI suggestion rather than a scaffolded outline.

To complement these similarity measures, we designed an interface intervention that surfaces real-time similarity feedback during writing, aiming to make AI influence more visible. In a follow-up think-aloud study, participants treated the live indicators as a calibration aid, using them to monitor reuse, decide when to paraphrase, and reflect on how much they wanted AI to shape their text. This reflective feedback can support more conscious engagement without positioning the tool as a policing mechanism.

Together, our findings argue for studying AI influence on writing as a subtle, multi-axis form of adoption, and for interventions that support author agency through visibility rather than restriction. Future work should test across genres and real-world settings, scale the experiment, and examine how more diverse individuals moderate influence.

### Generative AI Usage Statement

We used ChatGPT (OpenAI; GPT-5.2 Thinking) for grammar/style proofreading and to assist with drafting code to generate the paper’s figures from our existing data. All results were reviewed and edited by the authors, who remain fully responsible for the manuscript’s originality and integrity.

### References

- Abiola et al. (2023)
O. Abiola, A. Abayomi-Alli, O. A. Tale, S. Misra, and O. Abayomi-Alli

Sentiment analysis of covid-19 tweets from selected hashtags in nigeria using vader and text blob analyser.

Journal of Electrical Systems and Information Technology 10 (1), pp. 5.

Cited by: item 4.

- Al-Rawas et al. (2025)
M. Al-Rawas, O. Qader, N. Othman, N. Ismail, R. Mamat, M. S. Halim, J. Abdullah, and T. Noorani

Identification of dental related chatgpt generated abstracts by senior and young academicians versus artificial intelligence detectors and a similarity detector.

Scientific Reports 15, pp. .

External Links: Document

Cited by: §3.2.

- Alkaissi and Mcfarlane (2023)
H. Alkaissi and S. Mcfarlane

Artificial hallucinations in chatgpt: implications in scientific writing.

Cureus 15, pp. .

External Links: Document

Cited by: §2.2.

- Allen et al. (2023)
G. Allen, M. Beijen, D. Maxwell, and U. Gadiraju

In a hurry: how time constraints and the presentation of web search results affect user behaviour and experience.

In International Conference on Web Engineering,

pp. 221–235.

Cited by: §3.3.

- Bansal et al. (2021)
G. Bansal, T. Wu, J. Zhou, R. Fok, B. Nushi, E. Kamar, M. T. Ribeiro, and D. Weld

Does the whole exceed its parts? the effect of ai explanations on complementary team performance.

In Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems,

CHI ’21, New York, NY, USA.

External Links: ISBN 9781450380966,
Link,
Document

Cited by: §1,
§2.2.

- Bloom et al. (1956)
B. S. Bloom, M. D. Engelhart, E. J. Furst, W. H. Hill, D. R. Krathwohl, et al.

Taxonomy of educational objectives: the classification of educational goals. handbook 1: cognitive domain.

Longman New York.

Cited by: §1,
§2.4.

- Buçinca et al. (2021)
Z. Buçinca, M. B. Malaya, and K. Z. Gajos

To trust or to think: cognitive forcing functions can reduce overreliance on ai in ai-assisted decision-making.

Proceedings of the ACM on Human-Computer Interaction 5 (CSCW1), pp. 1–21.

External Links: ISSN 2573-0142,
Link,
Document

Cited by: §1,
§2.2,
§2.2.

- Chan and Tsi (2023)
C. K. Y. Chan and L. H.Y. Tsi

The ai revolution in education: will ai replace or assist teachers in higher education?.

ArXiv abs/2305.01185.

External Links: Link

Cited by: §1.

- Chen et al. (2025)
X. Chen, K. Ruan, K. P. Ju, N. Yap, and X. Wang

More AI Assistance Reduces Cognitive Engagement: Examining the AI Assistance Dilemma in AI-Supported Note-Taking.

Proceedings of the ACM on Human-Computer Interaction 9 (7), pp. 1–29 (en).

External Links: ISSN 2573-0142,
Link,
Document

Cited by: §2.2,
§2.4.

- Danry et al. (2025)
V. Danry, P. Pataranutaporn, M. Groh, and Z. Epstein

Deceptive explanations by large language models lead people to change their beliefs about misinformation more often than honest explanations.

In Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems,

CHI ’25, New York, NY, USA.

External Links: ISBN 9798400713941,
Link,
Document

Cited by: §1.

- de Jong et al. (2025)
S. de Jong, V. Paananen, B. Tag, and N. van Berkel

Cognitive forcing for better decision-making: reducing overreliance on ai systems through partial explanations.

Proc. ACM Hum.-Comput. Interact. 9 (2).

External Links: Link,
Document

Cited by: §2.2.

- Ehsan and Riedl (2020)
U. Ehsan and M. O. Riedl

Human-centered explainable ai: towards a reflective sociotechnical approach.

In International conference on human-computer interaction,

pp. 449–466.

Cited by: §2.2.

- Fu et al. (2023)
L. Fu, B. Newman, M. Jakesch, and S. Kreps

Comparing sentence-level suggestions to message-level suggestions in ai-mediated communication.

In Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems,

CHI ’23, New York, NY, USA.

External Links: ISBN 9781450394215,
Link,
Document

Cited by: §2.3.

- Gergle and Tan (2014)
D. Gergle and D. S. Tan

Experimental research in hci.

In Ways of Knowing in HCI,

pp. 191–227.

Cited by: §3.3.

- Glikson and Asscher (2022)
E. Glikson and O. Asscher

AI-mediated apology in a multilingual work context: implications for perceived authenticity and willingness to forgive.

Computers in Human Behavior 140, pp. 107592.

External Links: Document

Cited by: §2.1,
§2.2.

- Goldwasser et al. (1985)
S. Goldwasser, S. Micali, and C. Rackoff

The knowledge complexity of interactive proof-systems.

In Proceedings of the Seventeenth Annual ACM Symposium on Theory of Computing,

STOC ’85, New York, NY, USA, pp. 291–304.

External Links: ISBN 0897911512,
Link,
Document

Cited by: §2.1.

- Guo et al. (2024)
Z. Guo, Y. Wu, J. D. Hartline, and J. Hullman

A decision theoretic framework for measuring ai reliance.

In Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency,

FAccT ’24, New York, NY, USA, pp. 221–236.

External Links: ISBN 9798400704505,
Link,
Document

Cited by: §2.2.

- Harland et al. (2025)
H. Harland, R. Dazeley, H. Senaratne, P. Vamplew, F. Cruz, and B. Nakisa

AI apology: a critical review of apology in ai systems.

Artificial Intelligence Review 58 (12), pp. 369.

Cited by: §2.1,
§2.1,
§2.2.

- Hart and Staveland (1988)
S. G. Hart and L. E. Staveland

Development of nasa-tlx (task load index): results of empirical and theoretical research.

In Advances in psychology,

Vol. 52, pp. 139–183.

Cited by: §3.4.

- Henry (1906)
O. Henry

After twenty years.

In The Four Million,

Note: Originally published in 1906; short story

Cited by: §3.1.

- Hui (2025)
E. S. Y. E. Hui

Incorporating bloom’s taxonomy into promoting cognitive thinking mechanism in artificial intelligence-supported learning environments.

Interactive Learning Environments 33 (2), pp. 1087–1100.

External Links: Document,
Link,
https://doi.org/10.1080/10494820.2024.2364237

Cited by: §1,
§2.4.

- Jaccard (1901)
P. Jaccard

Etude comparative de la distribution florale dans une portion des alpes et des jura.

Bulletin de la Societe Vaudoise des Sciences Naturelles 37, pp. 547–579.

Cited by: item 1.

- Kahneman (2011)
D. Kahneman

Thinking, fast and slow.

Farrar, Straus and Giroux, New York.

External Links: ISBN 9780374275631 0374275637,
Link

Cited by: §2.1.

- Kamar et al. (2012)
E. Kamar, S. Hacker, and E. Horvitz

Combining human and machine intelligence in large-scale crowdsourcing.

In Proceedings of the 11th International Conference on Autonomous Agents and Multiagent Systems - Volume 1,

AAMAS ’12, Richland, SC, pp. 467–474.

External Links: ISBN 0981738117

Cited by: §2.2.

- Kamar (2016)
E. Kamar

Directions in hybrid intelligence: complementing ai systems with human intelligence.

In Proceedings of the Twenty-Fifth International Joint Conference on Artificial Intelligence,

IJCAI’16, pp. 4070–4073.

External Links: ISBN 9781577357704

Cited by: §2.2.

- Kim et al. (2024)
S. S. Y. Kim, Q. V. Liao, M. Vorvoreanu, S. Ballard, and J. W. Vaughan

"I’m not sure, but…": examining the impact of large language models’ uncertainty expression on user reliance and trust.

In Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency,

FAccT ’24, New York, NY, USA, pp. 822–835.

External Links: ISBN 9798400704505,
Link,
Document

Cited by: §2.2.

- Kim et al. (2025)
S. S. Y. Kim, J. W. Vaughan, Q. V. Liao, T. Lombrozo, and O. Russakovsky

Fostering appropriate reliance on large language models: the role of explanations, sources, and inconsistencies.

In Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems,

CHI ’25, pp. 1–19.

External Links: Link,
Document

Cited by: §1,
§2.2,
§2.2.

- Kosmyna et al. (2025)
N. Kosmyna, E. Hauptmann, Y. T. Yuan, J. Situ, X. Liao, A. V. Beresnitzky, I. Braunstein, and P. Maes

Your brain on chatgpt: accumulation of cognitive debt when using an ai assistant for essay writing task.

External Links: 2506.08872,
Link

Cited by: §1,
§2.4.

- Lee et al. (2025)
H. (. Lee, A. Sarkar, L. Tankelevitch, I. Drosos, S. Rintel, R. Banks, and N. Wilson

The impact of generative ai on critical thinking: self-reported reductions in cognitive effort and confidence effects from a survey of knowledge workers.

In Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems,

CHI ’25, New York, NY, USA.

External Links: ISBN 9798400713941,
Link,
Document

Cited by: §1,
§2.4,
§5.

- Lee et al. (2022)
M. Lee, P. Liang, and Q. Yang

CoAuthor: designing a human-ai collaborative writing dataset for exploring language model capabilities.

In CHI Conference on Human Factors in Computing Systems,

CHI ’22, pp. 1–19.

External Links: Link,
Document

Cited by: §2.3.

- Loria and contributors (2026)
S. Loria and contributors

TextBlob documentation (release 0.19.0).

Note: Read the DocsAccessed 2026-01-06

Cited by: item 4.

- Mieczkowski et al. (2021)
H. Mieczkowski, J. T. Hancock, M. Naaman, M. Jung, and J. Hohenstein

AI-mediated communication: language use and interpersonal effects in a referential communication task.

Proc. ACM Hum.-Comput. Interact. 5 (CSCW1).

External Links: Link,
Document

Cited by: §2.3.

- Murtaza et al. (2025)
M. Murtaza, C. Cheng, B. Albahlal, M. Muslam, and M. Raza

The impact of llm chatbots on learning outcomes in advanced driver assistance systems education.

Scientific Reports 15, pp. .

External Links: Document

Cited by: §1.

- Navon and Gopher (1979)
D. Navon and D. Gopher

On the economy of the human-processing system..

Psychological review 86 (3), pp. 214.

Cited by: §2.2.

- Qurashi et al. (2020)
A. W. Qurashi, V. Holmes, and A. P. Johnson

Document processing: methods for semantic text similarity analysis.

In 2020 international conference on INnovations in Intelligent SysTems and Applications (INISTA),

pp. 1–6.

Cited by: §3.4.

- Reimers and Gurevych (2019)
N. Reimers and I. Gurevych

Sentence-bert: sentence embeddings using siamese bert-networks.

In Proceedings of the 2019 conference on empirical methods in natural language processing and the 9th international joint conference on natural language processing (EMNLP-IJCNLP),

pp. 3982–3992.

Cited by: item 3.

- Russell et al. (2025)
J. Russell, M. Karpinska, and M. Iyyer

People who frequently use chatgpt for writing tasks are accurate and robust detectors of ai-generated text.

In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),

pp. 5342–5373.

Cited by: §3.2.

- Singh et al. (2025)
A. Singh, K. Taneja, Z. Guan, and A. Ghosh

Protecting human cognition in the age of ai.

External Links: 2502.12447,
Link

Cited by: §1,
§2.4.

- Sussman and Carter (2025)
K. Sussman and D. Carter

Detecting effects of ai-mediated communication on language complexity and sentiment.

In Companion Proceedings of the ACM on Web Conference 2025,

WWW ’25, New York, NY, USA, pp. 2689–2693.

External Links: ISBN 9798400713316,
Link,
Document

Cited by: §2.3.

- Tang et al. (2023)
N. Tang, M. Chen, Z. Ning, A. Bansal, Y. Huang, C. McMillan, and T. J. Li

An Empirical Study of Developer Behaviors for Validating and Repairing AI-Generated Code.

External Links: Link,
Document

Cited by: §2.2.

- Toker and Akgun (2024)
S. Toker and M. Akgun

The role of task complexity in reducing ai plagiarism: a study of generative ai tools.

External Links: 2412.13412,
Link

Cited by: §2.2,
§2.2,
§3.4.

- Tomasello et al. (2005)
M. Tomasello, M. Carpenter, J. Call, T. Behne, and H. Moll

Understanding and sharing intentions: the origins of cultural cognition.

Behavioral and Brain Sciences 28, pp. 675–735.

External Links: Document

Cited by: §2.1.

- Vani and Gupta (2015)
K. Vani and D. Gupta

Investigating the impact of combined similarity metrics and pos tagging in extrinsic text plagiarism detection system.

In 2015 international conference on advances in computing, communications and informatics (ICACCI),

pp. 1578–1584.

Cited by: item 2.

- Vasconcelos et al. (2023)
H. Vasconcelos, M. Jörke, M. Grunde-McLaughlin, T. Gerstenberg, M. S. Bernstein, and R. Krishna

Explanations can reduce overreliance on ai systems during decision-making.

Proceedings of the ACM on Human-Computer Interaction 7 (CSCW1), pp. 1–38.

Cited by: §1,
§2.2,
§2.2,
§2.2.

- Veselovsky et al. (2023)
V. Veselovsky, M. H. Ribeiro, and R. West

Artificial artificial artificial intelligence: crowd workers widely use large language models for text production tasks.

External Links: 2306.07899,
Link

Cited by: §3.2.

- Wojtowicz and DeDeo (2025)
Z. Wojtowicz and S. DeDeo

Undermining mental proof: how ai can make cooperation harder by making thinking easier.

In Proceedings of the Thirty-Ninth AAAI Conference on Artificial Intelligence and Thirty-Seventh Conference on Innovative Applications of Artificial Intelligence and Fifteenth Symposium on Educational Advances in Artificial Intelligence,

AAAI’25/IAAI’25/EAAI’25.

External Links: ISBN 978-1-57735-897-8,
Link,
Document

Cited by: §1,
§2.1,
§2.1,
§2.2.

- Yuan et al. (2022)
A. Yuan, A. Coenen, E. Reif, and D. Ippolito

Wordcraft: story writing with large language models.

In Proceedings of the 27th International Conference on Intelligent User Interfaces,

IUI ’22, New York, NY, USA, pp. 841–852.

External Links: ISBN 9781450391443,
Link,
Document

Cited by: §2.3.

- Zhang et al. (2020)
Y. Zhang, Q. V. Liao, and R. K. E. Bellamy

Effect of confidence and explanation on accuracy and trust calibration in ai-assisted decision making.

In Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency,

FAT* ’20, pp. 295–305.

External Links: Link,
Document

Cited by: §1,
§2.2.

- Zhao et al. (2022)
Q. Zhao, J. Niu, and X. Liu

ALS-MRS: Incorporating aspect-level sentiment for abstractive multi-review summarization.

Knowledge-Based Systems 258, pp. 109942.

External Links: ISSN 0950-7051,
Link,
Document

Cited by: item 4.

### Appendix A Task Prompts and AI Suggestions

#### Task A - Analysis

##### Prompt.

Evaluate Bob’s decision to wait at the old restaurant site for twenty years. Judge whether his choice was wise or misguided, using two story details. Finally, conclude what this reveals about the theme of friendship versus duty.

##### AI Suggestion.

Bob’s decision to wait at the old restaurant site for twenty years reflects a mix of admirable loyalty and ultimately misguided hope. His declaration that he “came a thousand miles to stand here tonight” highlights his deep commitment to the promise he made, while his certainty that Jimmy “will never forget” shows his unwavering faith in his friend’s character. Yet the ironic moment when Bob realizes, “Twenty years is a long time, but not long enough to change the shape of a man’s nose,” reveals how his trust has blinded him to the possibility that their lives—and moral paths—have diverged. Together, these details show that Bob’s long wait, though rooted in sincere friendship, becomes a tragic misjudgment. Ultimately, the story suggests that the tension between friendship and duty can force painful choices, and Jimmy’s decision to prioritize justice over personal loyalty underscores that duty may demand sacrifices that even lifelong bonds cannot prevent.

#### Task B - Creative

##### Prompt.

Rewrite the final scene from Jimmy Wells’s point of view (begin when he arrives on the street). Show how Jimmy processes the twist when he realizes Bob is a wanted man.

##### AI Suggestion.

Suggested Structure:

- (1)

Introduction — Jimmy’s emotions as he arrives.

- (2)

Recognition — His reaction upon seeing Bob.

- (3)

Conflict — Realizing Bob is a wanted man.

- (4)

Resolution — Choosing duty with compassion.

- (5)

Reflection — Jimmy’s lasting feelings.

Suggested Focus:
Explore Jimmy’s emotional conflict — his loyalty to friendship versus his duty as a policeman — and how he chooses a compassionate yet responsible path.

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
