---
title: "Designing LLM-Agents with Personalities: A Psychometric Approach"
person: james-evans
section: by
type: journal-article
year: 2024
date: 2024-10-24
venue: ""
authors: "Muhua Huang, Xijuan Zhang, Christopher J. Soto, James Evans"
source_url: https://doi.org/10.31234/osf.io/2kfw3
openalex_id: https://openalex.org/W4403710735
retrieved: 2026-08-13
content: full-text
notes: "preprint version; full text via the OpenAlex Content API (content.openalex.org)"
---

# Designing LLM-Agents with Personalities: A Psychometric Approach

## Full text

DESIGNING LLM-AGENTS WITH PERSONALITIES

Designing LLM-Agents with Personalities: A Psychometric Approach

Muhua Huang1 , Xijuan Zhang2 , Christopher Soto3 , and James Evans1 4
1

University of Chicago
2

York University
3

4

Colby College

Santa Fe Institute; Google

Author Note
Correspondence concerning this article should be addressed to Muhua Huang,
Knowledge Lab, the University of Chicago. Contact: muhua@uchicago.edu.

1

DESIGNING LLM-AGENTS WITH PERSONALITIES

2

Abstract
This research introduces a novel methodology for assigning quantifiable, controllable and
psychometrically validated personalities to Large Language Models-Based Agents (Agents)
using the Big Five personality framework. It seeks to overcome the constraints of human
subject studies, proposing Agents as an accessible tool for social science inquiry. Through a
series of four studies, this research demonstrates the feasibility of assigning
psychometrically valid personality traits to Agents, enabling them to replicate complex
human-like behaviors. The first study establishes an understanding of personality
constructs and personality tests within the semantic space of an LLM. Two subsequent
studies—using empirical and simulated data—illustrate the process of creating Agents and
validate the results by showing strong correspondence between human and Agent answers
to personality tests. The final study further corroborates this correspondence by using
Agents to replicate known human correlations between personality traits and
decision-making behaviors in scenarios involving risk-taking and ethical dilemmas, thereby
validating the effectiveness of the psychometric approach to design Agents and its
applicability to social and behavioral research.
Keywords: Artifical Intelligence, AI Agents, Large Language Model, Simulation, Big
Five Personalities, Psychometrics

DESIGNING LLM-AGENTS WITH PERSONALITIES

3

Designing LLM-Agents with Personalities: A Psychometric Approach
Introduction
The emergence of large language models (LLMs) has revolutionized our approach to
simulating human-like communication. LLMs are increasingly deployed across diverse
research fields to mimic human behaviors (Xi et al., 2023; Xu et al., 2024). In psychology,
LLMs are used to study cognitive processes, measure personality, and understand
psychological constructs (Hagendorff et al., 2023; Jiang et al., 2024; Rathje et al., 2024).
Sociologists employ these models to explore social bias and behavior (Lucy & Bamman,
2021; Park et al., 2023), while economists and political scientists utilize them to analyze
economic processes and political leanings (Bang et al., 2024; Hartmann et al., 2023). This
broad application underscores the growing interconnection between AI and social sciences.
Traditional human subject research methods, while standard in social and
behavioral studies, face significant challenges including ethical constraints, logistical
hurdles, and resource limitations (Demszky et al., 2023; Salganik, 2019). Recent
advancements in LLMs offer valuable complementary tools to address these challenges
(Agnew et al., 2024; Demszky et al., 2023). By using LLMs as stand-ins for human agents,
researchers can reduce logistical and financial burdens (S. Wang et al., 2021). These AI
Agents operate continuously, can simulate diverse demographic responses, and can be
deployed in scenarios that might pose ethical risks to human participants (Aher et al.,
2023; Argyle et al., 2023; Bai et al., 2022).
The integration of Agents in social and behavioral science research serves multiple
practical purposes while complementing rather than replacing human participants. They
can be used for pilot testing studies, allowing researchers to refine experimental designs
and identify potential issues before investing in full-scale human participant studies.
Additionally, Agents can independently replicate findings from human-subjects data,
enhancing the robustness and generalizability of research outcomes. This approach
provides a complementary method for validation and exploration, contributing to the

DESIGNING LLM-AGENTS WITH PERSONALITIES

4

overall rigor and efficiency of social and behavioral science research. By offering a novel
approach to corroborate and extend findings obtained through traditional human
participant studies, AI Agents represent an advancement in social science research
methodology, enhancing inclusivity and efficiency while preserving the essential depth of
human-centered understanding critical in the field.
Problems with Previous Approaches for Assigning Personas to Agents
Among the myriad of traits that can be incorporated into Agents, personalities, as a
part of persona, stand out as among the most intuitive characteristics to simulate.
Personalities encapsulate a spectrum of human behaviors and tendencies that are crucial
for the prediction of life outcomes ranging from academic and career to health and
socioeconomic outcomes (Soldz & Vaillant, 1999; Soto, 2019; Stewart et al., 2022) to a
multitude of interaction-based measures (Dang & Tapus, 2014; Furnham & Heaven, 1999).
Despite this potential and the capacity of Agents to advance personality research, existing
methodologies for implementing personality in Agents remain limited, typically falling into
three distinct approaches.
First, personas may be assigned with simple personality adjectives. For example,
Jiang et al. (2024) assigned personalities to one of the Agents by telling it “You are a
character who is introverted, antagonistic, conscientious, emotionally stable, and open to
experience." This type of approach holds a binary view — either high-low or
presence-absence of a trait — contradicts established empirical evidence that personality
traits exist on continuous spectra (Asendorpf, 2006; Marcus et al., 2006; Zrari & Sakale,
2024).
Second, personas may be assigned through demographic descriptions and personal
preferences (Park et al., 2023; Serapio-García et al., 2023). For instance, Park et al. (2023)
used narrative descriptions such as “John Lin is a pharmacy shopkeeper at the Willow
Market and Pharmacy who loves to help people.” This approach relies heavily on
stereotypical information extrapolated from the LLM’s training corpora, where names and

DESIGNING LLM-AGENTS WITH PERSONALITIES

5

occupations may trigger implicit assumptions (e.g., associating "John Lin" with Asian
ethnicity and pharmaceutical expertise). However, this approach, poses difficulties in
evaluating the full scope of stereotypical implications (i.e., potential confounds) and fails to
provide the granularity and precision necessary for social and behavioral science studies,
particularly when the degree of trait expression is crucial for creating agents with specific
personality profiles.
Third, personas may be assigned through fine-tuning LLMs on individual-specific or
group-specific text corpora (Liu et al., 2024), with each fine-tuned model representing a
distinct personality. While this approach modifies model behavior more fundamentally at
the parameter level compared to the second approach (i.e., in-context learning), it still
lacks precise control over trait expression. Furthermore, the fine-tuning process demands
substantial computational resources and deep learning expertise, limiting its accessibility to
researchers without specialized technical backgrounds or institutional support.
These approaches, while offering a superficial semblance of personality, suffer from
critical limitations. Relying on stereotypes underlying traits (e.g., naive) or roles (e.g.,
policing officer) does not provide the precise control necessary for rigorous social and
behavioral research and does not reflect the continuity and complexity inherent in human
personalities (Cummings & Sanders, 2019).
Psychometric Approach for Assigning LLM-Agents Persona
In this article, we propose creating Agents with personalities through a
psychometric approach by leveraging the Big Five Personality theory. Historically, the Big
Five personality theory was developed based on the Lexical Hypothesis, which states that
personality characteristics that are fundamental to humans have become a part of human
language, and the most important characteristics are encoded by a single word (Caprara &
Cervone, 2000). Based on the Lexical Hypothesis, scholars selected personality-related
words from the English dictionary (Allport & Odbert, 1936), refined the list of words
(W. T. Norman, 1963; W. Norman, 1967; Wiggins, 1979), had participants rate themselves

DESIGNING LLM-AGENTS WITH PERSONALITIES

6

against those descriptors, applied factor analysis to reduce the dimensionality of the data,
and eventually identified the Big Five Personality traits(Fiske, 1949; Goldberg, 1990;
McCrae, 1994; Peabody & Goldberg, 1989): Openness (O), Conscientiousness (C),
Extraversion (E), Agreeableness (A) and Neuroticism (N).
Over the past decades, many psychometric scales1 measuring the Big Five traits
have been developed, notably the Big Five Inventory (BFI; John et al., 1991), Big Five
Inventory - 2 (BFI2; Soto & John, 2017), Mini-Markers (Saucier, 1994), the Big Five
Aspects Scale (BFAS; DeYoung et al., 2007) and the NEO Five-Factor Inventory
(NEO-FFI; Costa & McCrae, 1989). Despite having different items, these psychological
measurements demonstrated high reliability, convergent validity and predictive validity in
samples from diverse backgrounds (McCrae, 2009; McCrae & Costa Jr, 1997; Poortinga
et al., 2002). Specifically, these psychological measurements of the Big Five can
significantly predict life outcomes, such as education achievement, socioeconomic status,
health, interpersonal relationships with peers and family, and more, indicating that
personality traits can indeed forecast a range of individual, interpersonal and societal
behaviors effectively (Ozer & Benet-Martinez, 2006; Roberts et al., 2007; Soto, 2019).
Given that the Big Five traits and LLMs are both developed based on natural
language (English), using the Big Five framework to create Agents with personality is
theoretically intuitive and coherent. More importantly, given the high reliability and
validity of the Big Five and the rigorous research on the Big Five theory over the decades,
using the Big Five will help create Agents with more realistic, find-grained, and varied
personalities that reflect the distribution of personality types and variability in a given
population.
Bringing psychometric principles to design and evaluate has practical benefits
(X. Wang et al., 2023). Integrating well-established psychometric tests (i.e., high reliability

1

The terms “scale” and “test” are used interchangeably to refer to psychometric instruments for assessing
personality traits.

DESIGNING LLM-AGENTS WITH PERSONALITIES

7

and validity) into the design of Agents could ensure that the personality traits assigned to
Agents are stable and reflective of their programmed characteristics, enhancing the
credibility and robustness of findings in applications where the consistency of Agents
performance is critical. In addition, as psychometric tests are designed to discern different
levels of expression of some psychological traits, we can reverse engineer that variability
into Agents to create diversity, which is necessary in simulating real-world settings.
Additionally, free from external confounds, this approach allows for precise and fine-grained
manipulation over the psychological constructs of interest, allowing nuanced understanding
and refinement of Agents’ personalities for tailored applications.
In summary, leveraging the Big Five personality test to design Agents presents an
opportunity to move beyond stereotypes and create Agents with psychometrically valid
traits. These traits can be quantified and controlled, are realistic and predictive of real
human behavior, and are thus better suited for large-scale deployment in psychology and
social science research.
Objectives of the Present Research
The primary objective of this research is to develop and validate a systematic
approach for creating Agents with psychometrically sound personality traits. To achieve
this goal, we conducted a series of four interconnected studies, each addressing a specific
aspect of the Agent creation and validation process.
Study 1 aims to establish a foundational understanding of personality constructs
and personality tests within the embedding space of LLMs. By analyzing the semantic
relationships between various personality assessments, we seek to uncover the underlying
structure of personality-related concepts as represented in LLMs. Study 2 focuses on
demonstrating the parallelism between Agents’ responses and empirical data obtained from
human participants. By comparing Agents’ responses to personality assessments with
human individuals, we aim to validate the accuracy and reliability of our Agent creation
method. Study 3 aims to demonstrate the effectiveness of a parametric approach for

DESIGNING LLM-AGENTS WITH PERSONALITIES

8

creating Agents. By using sample statistics derived from existing personality data to
simulate responses, this study seeks to establish a method for generating psychometrically
valid Agents without extensive new data collection. Study 4 aims to establish that the
correspondence between Agents’ traits and behaviors parallels that observed in humans.
By examining how Agents with different personality profiles respond to various scenarios,
we aim to validate the behavioral consistency and predictive validity of our created Agents.
Collectively, these four studies form a comprehensive investigation into the creation,
validation, and application of Agents with psychometrically sound personality traits. We
hope to provide researchers with a powerful new tool for conducting personality and social
behavior research at scale, while maintaining high standards of validity and reliability.
Study 1: Semantic Representation of Personality Constructs in LLM
Study 1 aimed to establish a foundational understanding of the semantic nuances
inherent in personality tests and constructs using embedding. Given that Agents are
inherently constructed on embeddings, this initial investigation serves to validate the
approach and set the stage for subsequent studies.
Methods
Our analysis incorporated content from widely recognized Big Five tests, such as
the BFI (John et al., 1991), BFI2 (Soto & John, 2017), Mini-Markers (Saucier, 1994),
BFAS (DeYoung et al., 2007) and NEO-FFI (Costa & McCrae, 1989). We extracted
domain-specific content (i.e., test items) from these tests and processed it through
OpenAI’s advanced text-embedding model (text-embedding-3-large). Text-embedding
techniques are commonly used in natural language processing; they allow researchers to
represent text data (such as words, phrases, sentences, or even entire documents) in a
numeric format (i.e., vector) that quantifies the semantic relationships between words,
phrases, or entire documents. In the context of our study, each personality test item is
converted into a high-dimensional vector (3072 dimensions for the model we used) that
captures its semantic meaning. To illustrate this concept, consider two items from different

DESIGNING LLM-AGENTS WITH PERSONALITIES

9

Big Five tests:
• “Is outgoing, socioable” (BFI2, Extroversion)
• “Extraverted” (Mini-Markers, Extroversion)
Despite their different wording, these items are semantically similar and would be
represented by vectors that are close to each other in the high-dimensional space.
Conversely, an item measuring a different construct, such as:
• “Is original, comes up with new ideas” (BFI2, Openness)
would be represented by a vector that is farther away from the first two in this space. The
embedding model we used is capable of capturing nuanced, context-dependent meanings.
For instance, it can distinguish between different uses of the word “open" in items:
• “Is open to new experiences” (Openness)
• “Is open about personal feelings” (related to Extraversion or Agreeableness)
These items, despite sharing the word “open”, would be represented by distinct vectors
that reflect their different psychological meanings.
Embeddings Techniques
To analyze these embeddings, we employed two main techniques, namely, cosine
similarity and t-Distributed Stochastic Neighbor Embedding (t-SNE).
Cosine similarity. This measure quantifies the semantic similarity between two
embedded texts, analogous to how correlation coefficients measure the relationship between
variables in psychological research. Just as a correlation of 1 indicates a perfect positive
relationship, a cosine similarity of 1 indicates identical semantic meaning. In contrast, a
cosine similarity of 0 suggests no semantic relationship, similar to a correlation of 0
indicating no linear relationship between variables.

DESIGNING LLM-AGENTS WITH PERSONALITIES

10

In the context of personality assessment, cosine similarity can be thought of as a
measure of construct overlap between items or scales. For instance, high cosine similarity
between items from different tests (e.g., “Is outgoing, socioable” from BFI2 and
“Extroverted" from Mini-Markers) would suggest they are tapping into the same
underlying construct, similar to how high inter-item correlations within a scale indicate
internal consistency in classical test theory.
t-SNE. This technique is conceptually similar to factor analysis, a method widely
used in personality psychology to uncover latent structures. While factor analysis typically
reduces many observed variables to a smaller number of latent factors, t-SNE reduces
high-dimensional data to two or three dimensions for visualization purposes
(Van der Maaten & Hinton, 2008). Just as factor analysis helps psychologists identify
underlying personality traits from patterns of item responses, t-SNE helps us visualize
clusters of semantically similar personality test items in a two-dimensional space. This
allows us to see how items from different tests relate to each other, much like how factor
loadings in exploratory factor analysis show how individual items relate to broader
personality constructs.
In our t-SNE visualizations, items that cluster together can be interpreted as
measuring similar constructs, analogous to how items with high loadings on the same
factor in factor analysis are interpreted as measuring the same underlying trait. This
provides a data-driven way to examine the convergent and discriminant validity of items
across different personality assessments.
The use of embedding in this study offers several advantages for personality
research. By capturing semantic relationships between test items, we can potentially
uncover subtle distinctions between various personality assessments that might not be
apparent through traditional psychometric methods. This approach provides a data-driven
complement to classical item analysis techniques, potentially informing more refined
personality models and enhancing our understanding of the semantic overlap between

DESIGNING LLM-AGENTS WITH PERSONALITIES

11

different personality measures.
Figure 1
Cosine Similarity Between Personality Tests: Overall Average and Domain-Specific
Comparisons

Results and Discussion
Figure 1 illustrates the cosine similarity between different personality tests across
the Big Five domains. The top-left subplot is the average similarity across all domains
which shows that most tests generally exhibit moderate to high cosine similarity (above
0.51), with the exception of Mini-Markers and NEO-FFI. Mini-Markers consistently shows
a relatively lower cosine similarity with other scales across all domains, which may be
attributed to its unique design approach: while other tests employ full statements, phrases,
or questions for each item (e.g., “Is complex, a deep thinker”), Mini-Markers exclusively
uses adjectives (e.g., philosophical”). The remaining subplots, each corresponding to a
specific Big Five domain, reveal similar patterns of cosine similarity between tests. This

DESIGNING LLM-AGENTS WITH PERSONALITIES

12

consistency across domains suggests that the semantic relationships between different
personality tests are relatively stable, regardless of the specific trait being measured.
However, the varying degrees of similarity observed between different test pairs highlight
the nuanced differences in how each instrument operationalizes and measures personality
constructs within the Big Five framework.
Figure 2
Two-Dimensional Projection of Big Five Personality Test Domain Embeddings Using t-SNE

Figure 2 illustrates a two-dimensional projection of the tests’ domain embeddings
using t-SNE2 . This visualization reveals distinct clustering patterns for each of the Big Five
2

The axes for t-SNE plot are usually not labelled, because the units of the axes are not directly related to

DESIGNING LLM-AGENTS WITH PERSONALITIES

13

personality domains, with the spatial arrangement of these clusters providing insight into
the semantic relationships between personality constructs. For instance, items assessing
Agreeableness are concentrated in the upper left quadrant, while those measuring
Openness are predominantly situated in the lower right quadrant. The remaining domains
— Extraversion, Conscientiousness, and Neuroticism — form separate, distinguishable
clusters within the projection space.
These results suggest that different personality tests tap into highly similar and
consistent constructs, despite variations in item wording and test structure. This finding
serves as the foundation for subsequent studies, which further examine Agents’
understanding of the underlying semantic associations during the personality assignment,
adaptation, and reflection process.
Study 2: Validating Personality Assignment in LLM-Agents Using Empirical
Data
Study 2 evaluates whether Agents can internalize and manifest human psychological
traits. It entails training of Agents using Big Five personality data obtained via one test
and validating their responses against an alternative Big Five personality test.
Considering the findings of Study 1, which indicate a relatively low semantic
similarity between BFI2 and Mini-Markers, we aim to validate the personality assignments
made by the BFI2 using Mini-Markers. The logic is that if this method supports two fairly
distinct psychometric tests, we can confidently generalize this validation approach to other
tests that exhibit greater semantic similarity.
Methods
Data
We repurposed data collected by Soto and John (2017) wherein participants (N =
438) responded to multiple Big Five tests, including: (1) BFI2: a sophisticated, 60-item,
any measurement from the original data. Instead, the axes represent a space that has been constructed to
best represent the similarities and differences between data points.

DESIGNING LLM-AGENTS WITH PERSONALITIES

14

Confirmatory Factor Analysis (CFA)-based Likert test designed to capture the
comprehensive hierarchical structure of personality, where each domain has three facets
and (2) Mini-Markers: a straightforward, 40-item test consisting of phenotypic Big Five
descriptive adjectives (Saucier, 1994). Participants BFI2 responses will serve as the
training (input) data, while their Mini-Markers responses (output) will be used for
validation. The convergent correlation between the two sets of responses averages .80 in
the original data, which serves as a reference for our comparison.
Procedure
Using OpenAIs API gpt-3.5-turbo-0125, we initiated 438 independent agent, each
corresponding to a participant. Shown in Figure 3, we embedded participants’ BFI2
answers into the prompts and asked the Agents to respond to the Mini-Markers test.
To examine the prompt format for personality assignment, we investigated two
distinct scale formats: the Likert format and the Expanded format. The Likert format,
traditionally used in most psychological scales, requires participants to rate their
agreement with statements on a numeric scale and typically includes both positively
worded items (e.g., “Is talkative") and reversely worded items (e.g., “Tends to be quiet") to
help detect response patterns and measure opposite ends of trait spectra. In contrast, the
Expanded format, a more recent innovation in psychological assessment, was developed to
address issues associated with the Likert format, such as response bias and careless
responding (e.g., Zhang & Savalei, 2016; Zhang et al., 2023, 2024). The Expanded format
eliminates the distinction between positively and reversely worded items by embedding
directionality within the response options rather than the items themselves. The Expanded
format presents each response option as a complete sentence, more closely approximating
natural language (Zhang et al., 2023, see Table 1 for example items). Soto and John (2017)
originally developed the BFI2 using the Likert format, and Zhang et al. (2024) translated
and validated BFI2 in the Expanded format. The prompts for both the Likert and
Expanded formats are provided in Appendix A and Appendix B, respectively. Throughout

DESIGNING LLM-AGENTS WITH PERSONALITIES

15

Figure 3
Flowchart depicting the training and validation procedures. On the left side, the two boxes
in the middle contain example items on BFI2 (Likert Format) and Mini-Markers.

the following sections, we will refer to Agents created using the Likert format personality
test as Agents-Likert, and those created using the Expanded format as Agents-Expanded.
Analysis
We performed convergent correlation analysis. Two convergent correlations were
computed after we summed participants’ Mini-markers domain scores: First, between
participants’ BFI2 scores and LLM-Agents’deduced Mini-markers scores. High correlations
would suggest that LLM-agents can consistently deduce personality traits from training
data. Second, between participants’ actual Mini-markers scores and those inferred by
LLM-Agents. High correlations here would indicate that LLM-Agents can accurately
mirror individual human personalities.

DESIGNING LLM-AGENTS WITH PERSONALITIES

16

Table 1
Example Extraversion Items in the Likert and Expanded Formats
Scale Formats
Likert
PW item

Is outgoing, sociable.
Disagree strongly
Disagree a little
Neutral; no opinion
Agree a little
Agree strongly

RW item

Tends to be quiet.
Disagree strongly
Disagree a little
Neutral; no opinion
Agree a little
Agree strongly

◦
◦
◦
◦
◦
◦
◦
◦
◦
◦

Expanded
Choose one that best describes you.
I am very reserved, unsociable.
I am quite reserved, unsociable.
I am somewhat outgoing, sociable.
I am quite outgoing, sociable.
I am very outgoing, sociable.

◦
◦
◦
◦
◦

Choose one that best describes you.
I am almost always quiet.
I am often quiet.
I am sometimes quiet.
I am rarely quiet.
I am almost never quiet.

◦
◦
◦
◦
◦

Meanwhile, we conducted CFA on the participants’, Agents-Likert’s and
Agents-Expanded’s Mini-Markers responses, using lavaan in R (Rosseel, 2012). The factor
loadings and Cronbachs alpha reliability scores would reveal the differences between
human’s and Agents’ item response patterns.
Results and Discussion
Convergent Correlations
Table 2 shows the convergent correlations between the Agents Mini-Markers scores
and input BFI2 scores, and the participants real Mini-Markers scores.
Likert Format. Responses from Agents-Likert had an average correlation of .728
with the BFI2 input scores, with coefficients ranging from .530 to .880. Furthermore, these
scores demonstrated an average correlation of .664 with the actual Mini-Markers scores

DESIGNING LLM-AGENTS WITH PERSONALITIES

17

obtained from human participants, with coefficients ranging from .486 to .826.
Expanded Format. Responses from Agents-Expanded had an average correlation
of .789 with the BFI2 input scores, with coefficients ranging from .648 to .840. These
scores also exhibited an average correlation of .689 with the actual Mini-Markers scores
from human participants, with coefficients ranging from .617 to .778.
Table 2
Convergent correlations between the Agents’ Mini-Markers scores and input BFI2 scores
(left), and the participants’ real Mini-Markers scores (right).

With BFI2
Format

O

C

E

A

With Human’s Mini-Markers
N

Avg

O

C

E

A

N

Avg

Likert
.530 .843 .880 .660 .727 .728 .486 .741 .826 .613 .655 .664
Expanded .823 .840 .833 .648 .803 .789 .670 .747 .778 .635 .617 .689
Note. O = Openness to Experience, C = Conscientiousness, E = Extraversion, A = Agreeableness, N = Neuroticism.

These results align closely with the correlations observed between BFI2 and
Mini-Markers scores among human participants, which vary from .739 to .885, with an
average of .802 (Soto & John, 2017). Agents-Expanded consistently had strong convergent
correlations with human participants data, indicating a high level of effectiveness.
Conversely, Agents-Likert showed similarly high convergence with observed BFI2 scores for
most personality traits, but notably weaker convergence for the Open-mindedness trait.
This finding likely reflects the ambiguous meaning of some Mini-Markers adjectives
without additional context (e.g., deep, complex).
CFA
Table 3 presents the standardized factor loadings and Cronbach’s alpha reliability
coefficients for Mini-Markers responses from participants, Agents-Likert and
Agents-Expanded. Three patterns emerged from this analysis.
First, the three sets of responses exhibited comparable Cronbach’s alpha reliability
coefficients. For participants’ data, the coefficients ranged from .820 to .869 (M = .843).

DESIGNING LLM-AGENTS WITH PERSONALITIES

18

For Agents’ responses in both formats, the initial Neuroticism domain model failed to
converge due to extreme multicollinearity between the items ‘Envious’ and ‘Jealous’, as
their responses had a perfect correlation of 1.0. After excluding one of these redundant
items, reliability coefficients for the remaining four domains yielded a mean of .832 (range:
.735 to .892) for the Likert format and a mean of .924 (range: .850 to .976) for the
Expanded format. Overall, responses from human participants and Agents in both formats
demonstrated similar reliability coefficients, with Agents-Expanded exhibiting the highest
coefficients, followed by Agents-Likert and human participants.

DESIGNING LLM-AGENTS WITH PERSONALITIES

19

Table 3
Standardized Factor Loadings and Cronbach’s alpha Reliability Scores for Human vs
LLM-Agents (Likert) vs LLM-Agents (Expanded) Response to Mini-Marker in Study 2 and
Study 3.
Domain

Extraversion

Agreeableness

Conscientiousness

Neuroticism1

Openness

Item

Human

Bold
Energetic
Extraverted
Talkative
Bashful
Quiet*
Shy*
Withdrawn*
Reliability
Cooperative
Kind
Sympathetic
Warm
Cold
Harsh*
Rude*
Unsympathetic*
Reliability
Efficient
Organized
Practical
Systematic
Careless
Disorganized*
Inefficient*
Sloppy*
Reliability
Envious
Fretful
Jealous
Moody
Temperamental
Touchy
Relaxed
Unenvious*
Reliability
Complex
Deep
Creative
Imaginative
Intellectual
Philosophical
Uncreative
Unintellectual*
Reliability

.482
.663
.833
.785
.499
.833
.751
.560
.869
.587
.719
.686
.726
.672
.522
.573
.675
.852
.546
.769
.459
.425
.605
.823
.648
.729
.842
.839
.517
.836
.583
.625
.524
.358
.636
.834
.365
.866
.511
.817
.512
.448
.719
.364
.820

Study 2
(Likert)
.827
.814
.919
.877
.515
.444
.480
.481
.892
.919
.998
.962
.996
.139
.122
.122
.150
.865
.698
.865
.711
.973
.155
.170
.137
.118
.816
NA
.584
.446
.823
.818
.824
.113
-.062
.735
.813
.824
.942
.954
.829
.796
.007
-.073
.852

Study 2
(Expanded)
.832
.760
.922
.851
.958
.971
.981
.989
.976
.813
.978
.957
.983
.609
.649
.587
.728
.944
.808
.989
.708
.987
.584
.879
.838
.693
.953
NA
.650
.254
.972
.987
.825
.581
.180
.850
.644
.685
.405
.481
.988
.975
.457
.615
.896

Study 3
(Likert)
.881
.769
.893
.804
.379
.101
.218
.209
.832
.894
.997
.955
.999
-.026
-.071
-.122
-.033
.796
.698
.872
.615
.981
.135
.098
.066
.202
.772
NA
.488
.389
.874
.889
.757
-.228
-.334
.600
.805
.808
.961
.951
.772
.735
-.170
-.236
.795

Study 3
(Expanded)
.851
.720
.825
.802
.977
.912
.984
.968
.970
.837
.965
.947
.969
.271
.366
.352
.378
.888
.654
.987
.632
.990
.527
.821
.736
.641
.937
NA
.647
.121
.973
.972
.697
.497
-.016
.800
.792
.810
.460
.563
.991
.981
.214
.455
.883

* indicates reversely worded items.
1
The initial Neuroticism domain model failed to converge due to multicollinearity between “Envious” and
“Jealous” (r = 1.0).

DESIGNING LLM-AGENTS WITH PERSONALITIES

20

Second, factor loadings obtained from human participants and Agents-Expanded
demonstrated relative consistency between positively worded and reversely worded items.
The average loading difference between these item types was .007 for human participants
and .096 for Agents-Expanded. However, Agents-Likert exhibited substantially higher
factor loadings for positively worded items compared to reversely worded items, with an
average difference of .647. This finding suggests that Agents-Likert are more sensitive to
prompt wording and may be more susceptible to acquiescence bias and wording effects.
This result is consistent with previous findings that the Likert format can cause
acquiescence bias and wording effects in LLMs (Salecha et al., 2024) and human
participants (Zhang & Savalei, 2016; Zhang et al., 2016, 2019). In contrast,
Agents-Expanded appear more robust and less susceptible to acquiescence bias, indicating
that the Expanded format may be a better method for creating Agents with
psychologically valid traits.
Third, the Neuroticism domain of the Mini-Markers might not be suitable to
examine Agents’ traits. Items “Envious" and “Jealous" having perfect correlations in
Agents’ data suggest that LLMs treat them as identical, or at least not distinct enough in
the context of personality assessment for them to give different answers. In contrast,
human data did not experience the same issue, indicating that the synonyms might be
interpreted differently by some humans, or it could be due to the inherent variability in
human responses, often referred to as measurement error: Human participants may provide
slightly different answers to the same or very similar questions due to various factors such
as momentary fluctuations in mood, attention, or interpretation of the items. The absence
of such variability in Agents’ responses could be a sign that Agents may not have as
nuanced a perception of semantic differences as humans, or may not replicate the
measurement error typically observed in human responses. Also, the loading difference for
positively worded items and reversely worded items is particularly large for Agents, even
for Agents-Expanded. This suggests that Agents have substantially different response

DESIGNING LLM-AGENTS WITH PERSONALITIES

21

patterns when responding to items in the Neuroticism domain compared to other domains.
One potential explanation is social desirability bias, a phenomenon where participants may
consciously or subconsciously respond in a socially desirable manner, over-reporting
desirable traits and under-reporting undesirable ones (Grimm, 2010). As Mini-Markers
items under the Neuroticism domain tend to be perceived as undesirable (e.g., “Envious”
and “Moody”), Agents may have been influenced by social desirability bias (Salecha et al.,
2024), as they are trained to produce responses aligned with human preferences and
socially desirable outcomes (Y. Wang et al., 2023).
The results from both the convergent correlation analysis and CFA reveal that
Agents can effectively simulate human personality traits, demonstrating strong alignment
with human responses across different personality measures. Comparing the two formats,
Agents-Expanded consistently outperformed Agents-Likert, showing higher reliability,
stronger convergent correlations, and greater robustness against biases such as acquiescence
and wording effects. These findings suggest that the Expanded format may be the better
choice for creating psychometrically valid Agents for personality research, offering a more
accurate and reliable simulation of human personality traits.
Study 3: Parametric Approach to Creating LLM-Agents with Simulated
Personality Data
Study 3 introduces a parametric approach for developing Agents using sample
statistics derived from existing personality data. This method involves extracting key
parameters from empirical data, simulating item responses based on these parameters, and
then assigning these simulated responses to Agents. By doing so, we aim to provide an
efficient alternative or precursor to traditional empirical data collection, facilitating the
creation of diverse sets of Agents while maintaining psychometric validity.
Methods
As shown in Figure 4, we began by extracting key statistics from Soto & Johns
(2017b) BFI2 data, we extracted statistics, including facet means and standard deviations,

DESIGNING LLM-AGENTS WITH PERSONALITIES

22

Figure 4
Flowchart depicting the data generation produce using a parametric approach.

facet correlations and average intra-facet item correlations. Using these statistics, we
simulated BFI2 responses based on several assumptions: (1) normal distribution of domain
scores, facet scores, and errors; (2) a linear relationship between correlated facets; and (3)
domain scores are independent.
We then created 200 Agents-Likert and 200 Agents-Expanded based on these
simulated BFI2 response. Following the protocol established in Study 2, we then prompted
the Agents to complete the Mini-Markers test.
To validate the results and assess the psychometric properties of the Agents’
responses, same as Study 2, we employed two primary methods. First, we calculated
convergent correlations between the simulated BFI2 inputs and the Agents’ Mini-Markers
responses. Second, we conducted CFA on the simulated Mini-Markers responses from
Agents. Through CFA, we assessed standardized factor loadings and Cronbach’s alpha
reliability coefficients. By comparing results with Study 2, we showed the similarity
between Agents created from empirical data and simulated data.
Convergent Correlations. Table 4 shows the convergent correlation coefficients
between the simulated BFI2 inputs and the Agents Mini-Markers responses. The average
correlation for the Likert format prompt is .679, with individual values ranging from .452
to .887. For the Expanded format prompt, the average correlation is .782, with values
ranging from .700 to .863. These results are comparable to those observed in Study 2,
where correlations between human participants BFI2 scores and Agents Mini-Markers
responses averaged .728 for Likert and .789 for Expanded. Moreover, as in Study 2,
Openness in the Likert format showed substantially lower convergence than all other
personality traits. These findings suggest that starting the design of Agents with

DESIGNING LLM-AGENTS WITH PERSONALITIES

23

Table 4
The Convergent Correlation Between BFI2 Input and Agents Mini-Markers Responses.

Likert
Expanded

O

C

E

A

N

Average

.452
.831

.844
.803

.887
.863

.591
.700

.621
.712

.679
.782

Note. O = Openness, C = Conscientiousness, E = Extraversion, A = Agreeableness, N =
Neuroticism.

psychological traits through simulation using sample statistics provides a valid and more
accessible alternative or precursor to collecting data from human participants.
CFA. The results reveal patterns similar to those observed in Study 2, further
validating the psychometric properties of Agents’ simulated responses. Table 3 presents the
standardized factor loadings and Cronbach’s alpha reliability coefficients for Agents’
simulated responses.
The CFA results are highly similar to Study 2’s. First, the Neuroticism domain
again had a convergence issue due to the multicollinearity. After removing either “Envious”
or “Jealous”, the reliability coefficients for Study 3 are similar to those observed in Study
2. For the Likert format, the reliability coefficients yielded a mean of .759 (range: .600 to
.832), while the Expanded format showed a mean of .896 (range: .800 to .970). These
values are comparable to those found in Study 2 (Likert: M = .843, range: .735 to .892;
Expanded: M = .942, range: .850 to .976) and remain higher than the mean reliability
observed in human participants (M = .843, range: .820 to .869). Meanwhile, factor
loadings obtained from Agents in Study 3 showed a similar pattern of discrepancy between
positively and reversely worded items as observed in Study 2. For Agents-Likert, the
average loading difference between these item types was .805, which is even more
pronounced than the .647 difference observed in Study 2. Agents-Expanded, however,
showed a smaller average difference of .223, which is closer to the .096 difference found in
Study 2 and the .007 difference in human participants. This finding further supports the
conclusion that the Expanded format produces more balanced and less biased responses.

DESIGNING LLM-AGENTS WITH PERSONALITIES

24

These results suggest that creating Agents using sample statistics provides a feasible
alternative or precursor to data collection from humans. The consistency in patterns
observed across Study 2 and Study 3—particularly the exceptional performance of the
Expanded format in terms of reliability, convergent correlations, and robustness against
wording effects—shows the practicality of this approach for creating psychometrically valid
Agents for personality research. This method offers researchers a powerful tool for
exploring personality dynamics and interactions in a controlled, scalable environment, while
maintaining psychometric validity comparable to traditional human-subject research.
Study 4: Comparing LLM-Agent and Human Risk-taking and Ethical Decisions
Study 4 aims to assess whether Agents exhibit behaviors consistent with humans
who have the same personality profiles. This investigation sought to elucidate both the
potential and limitations of employing Agents in behavioral science studies.
Methods
Data
We crafted ten scenarios: five ethical dilemmas and five risk-taking scenarios.
Following standard research protocols, we pre-registered the study and obtained ethical
approval before proceeding with data collection at a Canadian University. Participants
were asked to complete the BFI2 and respond to the ten scenarios. After applying
exclusion criteria based on English proficiency, consent for data deposit, and survey
completion, we retained a sample of 276 participants. The mean age of the participants
was 19.65 years (SD = 3.88). Regarding gender identity, the majority of participants
identified as female (80.4%), with 15.6% identifying as male and 4% identified as Other.
The ethnic composition of the sample was diverse: 26.8% as European/Caucasian, 25.0%
as South Asian, 7.3% as African, 6.9% as East Asian, 2.5% as Latino and Hispanic and
28.3% identified as Other.

DESIGNING LLM-AGENTS WITH PERSONALITIES

25

Procedure
Using gpt-3.5-turbo-0125, we generated 276 Agents (Expanded), each assigned a
unique set of personalities based on human participants’ responses to the BFI2. Agents
then indicated their decisions in risk-taking scenarios and moral dilemmas on a scale of 1
to 10.
Risk-Taking Scenarios. The scenarios were designed to test an individual’s
risk-taking tendency versus risk-avoidance tendency. The specific scenarios included: 1)
embarking on an entrepreneurial venture, 2) making significant investments, 3) confessing
romantic feelings to a close friend, 4) participating in extreme sports, and 5) opting to
study overseas. See Appendix C for the prompt.
Ethical Dilemma Scenarios. The scenarios were designed to assess individuals’
empathetic tendency versus rule adherence tendency. Given that the majority of currently
available LLMs have been safety-aligned and instruction fine-tuned (Biedma et al., 2024),
which typically skews them away from engaging in severe moral judgments (e.g., the
Trolley Problem), we introduced a series of everyday ethical dilemmas. These dilemmas
necessitated choosing between upholding a standard and prioritizing empathy. Examples
include decisions on 1) reporting a friend for cheating on a quiz, 2) addressing a colleague’s
misappropriation of office supplies, 3) underage drinking, 4) disclosing confidential
information that could save lives, and 5) providing candid feedback on subpar performance.
See Appendix D for the prompt.
Results and Discussion
In Table 5, for the risk-taking scenarios, Agents’ risk-taking tendencies were largely
consistent with those of humans with the same personality profiles: both humans and
Agents showed increased risk-taking tendencies when having high Openness and
Extraversion, and low Neuroticism. Conscientiousness and Agreeableness were not
associated with risk-taking. This finding is consistent with previous studies on personality
and risk, which found that high Extraversion and Openness were consistently associated

DESIGNING LLM-AGENTS WITH PERSONALITIES

26

Table 5
Regression Coefficients for Risk and Moral (Ethics) by Big Five Personality Traits

Risk Taking
Empathy in Dilemma
O
C
E
A
N
O
C
E
A
N
Human .136* -.046 .228* -.047 -.151* -.040 .229* .021 .093 -.141*
Agents .347* .023 1.132* .233 -.455* -.138* .140 .108* -.263* -.059
Note. O = Openness, C = Conscientiousness, E = Extraversion, A = Agreeableness, N =
Neuroticism.
* indicates p < .05

with greater risk-taking (Joseph & Zhang, 2021; Nicholson et al., 2005). Both the current
study and Nicholson et al. (2005) identified a negative association between Neuroticism
and risk-taking, although this was not observed in Joseph and Zhang (2021).
For the ethical dilemmas, among human participants, Conscientiousness was a
positive predictor and Neuroticism was a negative predictor of individuals’ tendency to
empathize individuals rather than adhere to rules. For Agents, Conscientiousness also
positively predicts their empathic tendency, but the other domains show different patterns
compared to humans. There could be several explanations for this discrepancy. First, the
relationship between moral decisions and personality is unclear and is largely affected by
the sample and measurement tools (Luke & Gawronski, 2022; Smillie et al., 2021).
Inconsistent results were also observed in Luke and Gawronski (2022), where student
samples and online worker samples yielded mixed results when examining the impact of
personalities on moral decisions. If the relationship is inconsistent within different
populations, then without introducing demographic information, LLMs cannot accurately
infer behavioral tendencies. Second, different cultures have different moral values
(Abdulhai et al., 2023; Graham et al., 2013). It is possible that our student sample is not
representative of the training corpora of the LLMs. Lastly, Agents might not be suitable
for testing moral judgments or ethical dilemmas due to alignment. That is, AI developers
may intentionally align LLMs values to an idealistic standard that best serves humans but
is unrepresentative of any specific culture (Yao et al., 2024).

DESIGNING LLM-AGENTS WITH PERSONALITIES

27

Contrasting results from the risk-taking scenarios and ethical dilemmas yield
important implications for the capabilities and limitations of Agents in simulating human
behavior. The parallelism between Agents and human participants in risk-taking
tendencies suggests that Agents have the ability to effectively model certain critical aspects
of human decision-making, particularly those closely tied to well-established personality
traits. This success indicates potential for using Agents in research on risk assessment,
consumer behavior, or career decision-making. However, the discrepancies observed in
ethical dilemmas highlight the complexities involved in modeling moral reasoning. These
differences imply the challenges of capturing the nuanced interplay between personality,
cultural context, and ethical decision-making within Agents. This limitation points to the
need for more sophisticated approaches in modeling complex human behaviors, possibly
incorporating cultural context, individual life experiences, and more nuanced ethical
frameworks into LLM-Agent designs. Furthermore, it emphasizes the importance of careful
validation and potential recalibration of Agents when applying them to studies involving
moral or cultural considerations.
Transparency and Openness
This research adheres to JARS Guidelines (Appelbaum et al., 2018). All data,
research materials, and analysis code have been made publicly available through the OSF
(https://osf.io/nrzy3/?view_only=50e6bc00bc0f495a8765e031a655f0ab) and GitHub
(https://github.com/muhua-h/Psychometrics4AI). Study 4 was preregistered on the Open
Science Framework prior to data collection (https://osf.io/4t9bf) and received ethical
approval from the Ethics Review Board at [Institution Name] (ID: e2024-221). The sample
size, exclusion criteria, and analysis plan for Study 4 were specified in the preregistration.
The analyses were primarily conducted in Python 3.9, using the OpenAI API
(version 1.35.3) for accessing text-embedding-3-large (Study 1) and gpt-3.5-turbo-0125
(Studies 2-4) models. Data manipulation and statistical analyses were performed using
pandas (version 2.2.0) and numpy (version 1.26.3), with statsmodels (version 0.14.0) for

DESIGNING LLM-AGENTS WITH PERSONALITIES

28

regression analyses. Visualizations were created using matplotlib (version 3.8.2). The
confirmatory factor analyses in Studies 2 and 3 were conducted in R using the lavaan
package (version 0.6.19; Rosseel, 2012) for structural equation modeling.
General Discussion
The present research introduces a novel methodology for assigning quantifiable,
controllable, and psychometrically validated personalities to Agents using the Big Five
personality framework. Through a series of four studies, we demonstrated the feasibility of
this approach and its potential applications in social science research.
Study 1 established a foundational understanding of personality constructs and
personality tests within the embedding space of LLMs. By analyzing the semantic
similarities across various personality tests, we laid the groundwork for understanding how
LLMs interpret and represent personality-related concepts. This finding serves as the basis
for subsequent studies, which further examined Agents’ understanding of the underlying
semantic associations during the personality assignment, adaptation, and reflection process.
Study 2 and Study 3 demonstrated that Agents could effectively absorb and
manifest psychometrically validated personality traits. Study 2 showed strong alignment
between Agents’ responses and empirical data from human participants, while Study 3
illustrated the effectiveness of using a parametric approach to create Agents with distinct
personalities. The use of both empirical data and simulated data based on sample statistics
enhances the robustness and flexibility of our approach, offering tools that can adapt to
varied research needs without compromising scientific rigor.
Importantly, our research highlighted the advantage of the Expanded format over
the traditional Likert format in assigning personalities to Agents. The Expanded format
demonstrated consistently stronger convergent correlations with human participants’ data
and showed greater robustness against biases such as acquiescence and wording effects.
This finding suggests potential modifications to the scale format of current psychometric
tests that could lead to more nuanced and accurate personality replications in Agents.

DESIGNING LLM-AGENTS WITH PERSONALITIES

29

Study 4 revealed that while Agents’ risk-taking behaviors closely paralleled those of
humans with similar personality profiles, their responses to ethical dilemmas showed
significant divergence from human patterns. These results showed both the promise and
the peril of simulating realistic Agents in behavioral science research (Kozlowski & Evans,
2024), suggesting the need for more sophisticated approaches in modeling complex human
behaviors such as demographic information and cultural context.
Our research contributes to the field in several ways. First, it harnesses the power of
embeddings and LLMs to uncover semantic similarities between different Big Five
personality tests, which provides a data-driven complement to classical item analysis
techniques. Second, our methodology offers a systematic and robust approach for creating
Agents endowed with psychological traits, which can be applied across various psychometric
tests. Finally, by demonstrating the usefulness of Agents in simulating complex,
human-like behaviors, we provide a powerful tool that expands empirical investigation
beyond traditional methodological constraints in social and behavioral research.
Limitation & Future Direction
Model Selection
We selected the gpt-3.5-turbo-0125 API to develop Agents due to several
compelling advantages. Firstly, this model is notable for its robust performance across
various benchmarks, making it a preferred choice in the field. Additionally, its
cost-effectiveness and the extensive context window it offerscapable of encompassing text
from an hour-long behavioral science studyensure comprehensive data handling without the
interference of system drift. In addition, this version of gpt-3.5-turbo represents a static
snapshot as of January 25th, 2024, thus it remains unaffected by alterations in subsequent
versions of GPT, ensuring consistency and reproducibility in our research outputs.
However, we recognize the potential for algorithmic confounding (Salganik, 2019) in
Agents’ responses, as market-available LLMs are intricately engineered to exhibit socially
desirable traits. This raises concerns about the elicitation of less socially desirable traits

DESIGNING LLM-AGENTS WITH PERSONALITIES

30

(e.g., Neuroticism) and corresponding behaviors (e.g., rule-breaking). If one LLM is
unsuitable for the tasks, researchers should be prepared to explore alternative LLMs such
as Claude and Llama. This contingency is distinct from practices like p-hacking or data
fabrication since our aim is not hypothesis testing but engineering a system capable of
generating Agents with psychometrically valid traits that can be quantified and managed.
Another concern could be the reliability of the Agents responses under novel
conditions, particularly given that current LLMs have a knowledge cutoff and may not be
familiar with the most recent news and changes. This is an inherent limitation of LLMs
and is outside the scope of our current investigation. However, it is important to
acknowledge that most LLMs are updated periodically. These updates can potentially
mitigate the issue by ensuring that the models remain relevant for a majority of study
designs that do not require the very latest knowledge. For study setups that necessitate
specific domain knowledge or recent information, researchers can incorporate this
information via in-context learning (Min et al., 2022), retrieval augmented generation (Gao
et al., 2024) or fine-tuning (Touvron et al., 2023) the model before assigning personalities.
This process ensures that the Agents are equipped with the relevant knowledge required for
the specific study context.
Present-day LLMs contend with issues such as context forgetting and hallucination
(OpenAI et al., 2024), reflecting similar cognitive constraints found in humans. Yet, the
swift advancement of AI technology hints that forthcoming LLM versions might show
improved cognitive functions and reduced cognitive bias. This advancement could present
challenges in crafting Agents that closely mimic human cognitive traits in future research.
Consequently, developing methods to equip Agents with the nuanced blend of human
cognitive strengths and weaknesses is essential for enhancing their authenticity and
effectiveness as alternative for human participants in social science studies.

DESIGNING LLM-AGENTS WITH PERSONALITIES

31

Generalizability & Engineering Considerations
The scope of our investigation is primarily centered around the Big Five personality
traits, which, while foundational, restricts the breadth of our inquiry. To transcend this
limitation, a systematic evaluation encompassing a diverse array of psychometric tests is
needed. Such an in-depth comparative analysis of these tests will not only examine the
generalizability of our findings but also significantly contribute to refining the engineering
processes underlying the development of Agents.
Simultaneously, the current research showcases the potential of using psychometric
tests to create Agents with nuanced psychological traits, suggesting a novel intersection of
psychology and artificial intelligence. However, the current reliance on manual coding
practices and the bespoke nature of the developed code poses barriers to adoption,
especially for social science researchers with limited experience with programming.
Addressing this challenge necessitates the development of more user-friendly tools and
frameworks that abstract away the complexities of the underlying code. By doing so, we
can democratize the use of Agents in social science research, enabling a broader spectrum
of scholars to leverage these advanced technologies in their work.
Diversity, Representation & Inclusion
Our approach to simulating population diversity using temperature settings is a
preliminary step. However, this method falls short of capturing the intricate interplay of
individual backgrounds and societal complexity. Future research should explore integrating
more detailed demographic information and assessing its influence on model outputs. This
will enable more precise control and deeper insights into model behavior.
Critics may argue that our study’s aim—to supplant human participants with
Agents—could be misguided (Agnew et al., 2024). Indeed, humans still surpass the most
advanced LLMs on multiple benchmarks, suggesting the intrinsic differences between
Agents and humans. Furthermore, LLMs are often trained on WEIRD datasets, which do
not adequately represent diverse cultural backgrounds and subpopulations, although

DESIGNING LLM-AGENTS WITH PERSONALITIES

32

algorithmic approaches exist to mitigate this bias and construct representative LLMs and
Agents (Argyle et al., 2023). We acknowledge these legitimate concerns and the
irreplaceable value of human participants in social science research. Our goal is not to
eliminate human participation but to provide an alternative methodone that, from a
beneficence perspective, aims to minimize harm and protect individuals from the potential
negative impacts of participation, particularly when it would be ethically problematic to
involve humans.
Philosophical Boundaries and Pragmatic Focus
In the endeavor to create Agents with personality traits, a potential critique arises
concerning the essence of “humanhood” in these agents, particularly given the ongoing
debate about the consciousness of LLMs. This question undeniably merits exploration
within the realms of artificial intelligence and large model research. Nevertheless, our study
intentionally steers clear of this philosophical terrain. Our primary objective is to explore
the feasibility of applying psychometric principles to construct Agents and to assess their
utility in advancing social science research. By focusing on these pragmatic aspects, we aim
to contribute to the methodological toolkit available to social scientists, leaving the
contemplation of consciousness and “humanhood” in Agents to future interdisciplinary
discourse. Instead, the method pioneered here could be used to pilot test studies before
they are conducted with human participants, or to replicate previous findings obtained
with human participants using a novel method.
Conclusion
In conclusion, this research presents a novel and promising approach to creating
Agents with psychometrically valid personality traits. By leveraging the Big Five
personality framework and advanced language models, we have demonstrated the potential
for Agents to serve as valuable tools in social and behavioral research. While
acknowledging the limitations and areas for future investigation, our findings suggest that
this methodology could significantly enhance the efficiency, scale, and ethical

DESIGNING LLM-AGENTS WITH PERSONALITIES

33

considerations of personality research. As we continue to refine and expand this approach,
Agents may become increasingly valuable precursors, alternatives, and supplements to
human participants in a wide range of social science studies.
Acknowledgement
We gratefully acknowledge Dr. Oliver John for providing original Big Five data
crucial for Study 2 and Study 3. We also thank OpenAI’s Researcher Access Program for
providing API access and funding support for computational resources used in this research.

DESIGNING LLM-AGENTS WITH PERSONALITIES

34

References
Abdulhai, M., Serapio-Garcia, G., Crepy, C., Valter, D., Canny, J., & Jaques, N. (2023).
Moral foundations of large language models. https://arxiv.org/abs/2310.15337
Agnew, W., Bergman, A. S., Chien, J., Díaz, M., El-Sayed, S., Pittman, J., Mohamed, S.,
& McKee, K. R. (2024, February). The illusion of artificial inclusion.
https://doi.org/10.1145/3613904.3642703
Aher, G., Arriaga, R. I., & Kalai, A. T. (2023, July). Using large language models to
simulate multiple humans and replicate human subject studies.
Allport, G. W., & Odbert, H. S. (1936). Trait-names: A psycho-lexical study. Psychological
monographs, 47 (1), i. https://doi.org/10.1037/h0093360
Appelbaum, M., Cooper, H., Kline, R. B., Mayo-Wilson, E., Nezu, A. M., & Rao, S. M.
(2018). Journal article reporting standards for quantitative research in rsychology:
The APA Publications and Communications Board Task Force Report. The
American Psychologist, 73 (1), 3–25. https://doi.org/10.1037/amp0000191
Argyle, L. P., Busby, E. C., Fulda, N., Gubler, J. R., Rytting, C., & Wingate, D. (2023).
Out of one, many: Using language models to simulate human samples. Political
Analysis, 31 (3), 337–351. https://doi.org/10.1017/pan.2023.2
Asendorpf, J. B. (2006). Typeness of personality profiles: A continuous person-centred
approach to personality data. European Journal of Personality, 20 (2), 83–106.
https://doi.org/10.1002/per.575
Bai, Y., Kadavath, S., Kundu, S., Askell, A., Kernion, J., Jones, A., Chen, A., Goldie, A.,
Mirhoseini, A., McKinnon, C., Chen, C., Olsson, C., Olah, C., Hernandez, D.,
Drain, D., Ganguli, D., Li, D., Tran-Johnson, E., Perez, E., . . . Kaplan, J. (2022).
Constitutional AI: Harmlessness from AI feedback.
https://arxiv.org/abs/2212.08073
Bang, Y., Chen, D., Lee, N., & Fung, P. (2024, August). Measuring political bias in large
language models: What is said and how it is said. In L.-W. Ku, A. Martins, &

DESIGNING LLM-AGENTS WITH PERSONALITIES

35

V. Srikumar (Eds.), Proceedings of the 62nd annual meeting of the association for
computational linguistics (volume 1: Long papers) (pp. 11142–11159). Association
for Computational Linguistics. https://doi.org/10.18653/v1/2024.acl-long.600
Biedma, P., Yi, X., Huang, L., Sun, M., & Xie, X. (2024). Beyond human norms: Unveiling
unique values of large language models through interdisciplinary approaches.
https://arxiv.org/abs/2404.12744
Caprara, G. V., & Cervone, D. (2000). Personality: Determinants, dynamics, and
potentials. Cambridge University Press.
https://doi.org/10.1017/CBO9780511812767
Costa, P. T., & McCrae, R. R. (1989). NEO PI/FFI manual supplement for use with the
NEO personality inventory and the NEO five-factor inventory. Psychological
Assessment Resources.
Cummings, J. A., & Sanders, L. (2019, June). Introduction to psychology. University of
Saskatchewan Open Press. Retrieved December 7, 2023, from
https://openpress.usask.ca/introductiontopsychology/
Dang, T.-H.-H., & Tapus, A. (2014). Towards personality-based assistance in
human-machine interaction. The 23rd IEEE International Symposium on Robot and
Human Interactive Communication, 1018–1023.
https://doi.org/10.1109/ROMAN.2014.6926386
Demszky, D., Yang, D., Yeager, D. S., Bryan, C. J., Clapper, M., Chandhok, S.,
Eichstaedt, J. C., Hecht, C., Jamieson, J., Johnson, M., Jones, M.,
Krettek-Cobb, D., Lai, L., JonesMitchell, N., Ong, D. C., Dweck, C. S., Gross, J. J.,
& Pennebaker, J. W. (2023). Using large language models in psychology. Nature
Reviews Psychology. https://doi.org/10.1038/s44159-023-00241-5
DeYoung, C. G., Quilty, L. C., & Peterson, J. B. (2007). Between facets and domains: 10
aspects of the big five. Journal of Personality and Social Psychology, 93 (5),
880–896. https://doi.org/10.1037/0022-3514.93.5.880

DESIGNING LLM-AGENTS WITH PERSONALITIES

36

Fiske, D. W. (1949). Consistency of the factorial structures of personality ratings from
different sources. The Journal of Abnormal and Social Psychology, 44 (3), 329.
https://doi.org/https://doi.org/10.1037/h0057198
Furnham, A., & Heaven, P. (1999). Personality and social behaviour. Arnold.
Gao, Y., Xiong, Y., Gao, X., Jia, K., Pan, J., Bi, Y., Dai, Y., Sun, J., Wang, M., &
Wang, H. (2024). Retrieval-augmented generation for large language models: A
survey. https://arxiv.org/abs/2312.10997
Goldberg, L. R. (1990). An alternative "description of personality": The big-five factor
structure. Journal of Personality and Social Psychology, 59 (6), 1216–1229.
https://doi.org/10.1037//0022-3514.59.6.1216
Graham, J., Haidt, J., Koleva, S., Motyl, M., Iyer, R., Wojcik, S. P., & Ditto, P. H. (2013).
Chapter two - moral foundations theory: The pragmatic validity of moral pluralism.
In P. Devine & A. Plant (Eds.), Advances in experimental social psychology
(pp. 55–130, Vol. 47). Academic Press.
https://doi.org/https://doi.org/10.1016/B978-0-12-407236-7.00002-4
Grimm, P. (2010). Social desirability bias. In J. Sheth & N. Malhotra (Eds.), Wiley
international encyclopedia of marketing. John Wiley & Sons.
https://doi.org/10.1002/9781444316568.wiem02057
Hagendorff, T., Fabi, S., & Kosinski, M. (2023). Human-like intuitive behavior and
reasoning biases emerged in large language models but disappeared in ChatGPT.
Nature Computational Science, 3 (10), 833–838.
https://doi.org/10.1038/s43588-023-00527-x
Hartmann, J., Schwenzow, J., & Witte, M. (2023). The political ideology of conversational
ai: Converging evidence on chatgpt’s pro-environmental, left-libertarian orientation.
https://arxiv.org/abs/2301.01768

DESIGNING LLM-AGENTS WITH PERSONALITIES

37

Jiang, H., Zhang, X., Cao, X., Breazeal, C., Roy, D., & Kabbara, J. (2024). Personallm:
Investigating the ability of large language models to express personality traits.
https://arxiv.org/abs/2305.02547
John, O. P., Donahue, E. M., & Kentle, R. L. (1991). Big five inventory. Journal of
Personality and Social Psychology.
https://doi.org/https://doi.org/10.1037/t07550-000
Joseph, E., & Zhang, D. (2021). Personality profile of risk-takers: An examination of the
big five facets. Journal of Individual Differences, 42, 1–10.
https://doi.org/10.1027/1614-0001/a000346
Kozlowski, A. C., & Evans, J. (2024). Simulating subjects: The promise and peril of ai
stand-ins for social agents and interactions. https://doi.org/10.31235/osf.io/vp3j2
Liu, N., Chen, L., Tian, X., Zou, W., Chen, K., & Cui, M. (2024). From llm to
conversational agent: A memory enhanced architecture with fine-tuning of large
language models. https://arxiv.org/abs/2401.02777
Lucy, L., & Bamman, D. (2021, June). Gender and representation bias in gpt-3 generated
stories. In N. Akoury, F. Brahman, S. Chaturvedi, E. Clark, M. Iyyer, &
L. J. Martin (Eds.), Proceedings of the Third Workshop on Narrative Understanding
(pp. 48–55). Association for Computational Linguistics.
https://doi.org/10.18653/v1/2021.nuse-1.5
Luke, D. M., & Gawronski, B. (2022). Big five personality traits and moral-dilemma
judgments: Two preregistered studies using the cni model. Journal of Research in
Personality, 101, 104297. https://doi.org/10.1016/j.jrp.2022.104297
Marcus, D. K., Lilienfeld, S. O., Edens, J. F., & Poythress, N. G. (2006). Is antisocial
personality disorder continuous or categorical? a taxometric analysis. Psychological
medicine, 36 (11), 1571–1581. https://doi.org/10.1017/S0033291706008245

DESIGNING LLM-AGENTS WITH PERSONALITIES

38

McCrae, R. R. (1994). Openness to experience: Expanding the boundaries of factor v.
European Journal of Personality, 8 (4), 251–272.
https://doi.org/https://doi.org/10.1002/per.2410080404
McCrae, R. R. (2009). The physics and chemistry of personality. Theory & Psychology,
19 (5), 670–687. https://doi.org/10.1177/0959354309341928
McCrae, R. R., & Costa Jr, P. T. (1997). Personality trait structure as a human universal.
American psychologist, 52 (5), 509. https://doi.org/10.1037//0003-066x.52.5.509
Min, S., Lyu, X., Holtzman, A., Artetxe, M., Lewis, M., Hajishirzi, H., & Zettlemoyer, L.
(2022). Rethinking the role of demonstrations: What makes in-context learning
work? https://arxiv.org/abs/2202.12837
Nicholson, N., Soane, E., Fenton-O’Creevy, M., & Willman, P. (2005). Personality and
Domain-Specific Risk Taking. Journal of Risk Research, 8.
https://doi.org/10.1080/1366987032000123856
Norman, W. T. (1963). Toward an adequate taxonomy of personality attributes: Replicated
factor structure in peer nomination personality ratings. The journal of abnormal
and social psychology, 66 (6), 574. https://doi.org/10.1037/h0040291
Norman, W. (1967). 2800 personality trait descriptors: Normative operating characteristics
for a university population. University of Michigan, Department of Psychology.
https://books.google.com/books?id=Az8rAAAAMAAJ
OpenAI, Achiam, J., Adler, S., Agarwal, S., Ahmad, L., Akkaya, I., Aleman, F. L.,
Almeida, D., Altenschmidt, J., Altman, S., Anadkat, S., Avila, R., Babuschkin, I.,
Balaji, S., Balcom, V., Baltescu, P., Bao, H., Bavarian, M., Belgum, J., . . . Zoph, B.
(2024). GPT-4 technical report. https://arxiv.org/abs/2303.08774
Ozer, D. J., & Benet-Martinez, V. (2006). Personality and the prediction of consequential
outcomes. Annual Review of Psychology, 57, 401–421.
https://doi.org/10.1146/annurev.psych.57.102904.190127

DESIGNING LLM-AGENTS WITH PERSONALITIES

39

Park, J. S., O’Brien, J., Cai, C. J., Morris, M. R., Liang, P., & Bernstein, M. S. (2023).
Generative agents: Interactive simulacra of human behavior. Proceedings of the 36th
Annual ACM Symposium on User Interface Software and Technology.
https://doi.org/10.1145/3586183.3606763
Peabody, D., & Goldberg, L. R. (1989). Some determinants of factor structures from
personality-trait descriptors. Journal of personality and social psychology, 57 (3),
552. https://doi.org/10.1037//0022-3514.57.3.552
Poortinga, Y. H., Van De Vijver, F. J., & Van Hemert, D. A. (2002). Cross-cultural
equivalence of the big five: A tentative interpretation of the evidence. The
five-factor model of personality across cultures, 281–302.
https://doi.org/10.1007/978-1-4615-0763-5_14
Rathje, S., Mirea, D.-M., Sucholutsky, I., Marjieh, R., Robertson, C. E., & Bavel, J. J. V.
(2024). Gpt is an effective tool for multilingual psychological text analysis.
Proceedings of the National Academy of Sciences, 121 (34), e2308950121.
https://doi.org/10.1073/pnas.2308950121
Roberts, B. W., Kuncel, N. R., Shiner, R., Caspi, A., & Goldberg, L. R. (2007). The power
of personality: The comparative validity of personality traits, socioeconomic status,
and cognitive ability for predicting important life outcomes. Perspectives on
Psychological science, 2 (4), 313–345.
https://doi.org/10.1111/j.1745-6916.2007.00047.x
Rosseel, Y. (2012). Lavaan: An r package for structural equation modeling. Journal of
statistical software, 48, 1–36. https://doi.org/10.18637/jss.v048.i02
Salecha, A., Ireland, M. E., Subrahmanya, S., Sedoc, J., Ungar, L. H., & Eichstaedt, J. C.
(2024). Large language models show human-like social desirability biases in survey
responses. https://arxiv.org/abs/2405.06058
Salganik, M. J. (2019). Bit by bit: Social research in the digital age. Princeton University
Press.

DESIGNING LLM-AGENTS WITH PERSONALITIES

40

Saucier, G. (1994). Mini-Markers: A Brief Version of Goldberg’s Unipolar Big-Five
Markers. Journal of Personality Assessment, 63 (3), 506.
https://doi.org/10.1207/s15327752jpa6303_8
Serapio-García, G., Safdari, M., Crepy, C., Sun, L., Fitz, S., Romero, P., Abdulhai, M.,
Faust, A., & Matari, M. (2023). Personality traits in large language models.
https://arxiv.org/abs/2307.00184
Smillie, L. D., Katic, M., & Laham, S. M. (2021). Personality and moral judgment: Curious
consequentialists and polite deontologists. Journal of Personality, 89 (3), 549–564.
https://doi.org/10.1111/jopy.12598
Soldz, S., & Vaillant, G. E. (1999). The big five personality traits and the life course: A
45-year longitudinal study. Journal of research in personality, 33 (2), 208–232.
https://doi.org/10.1006/jrpe.1999.2243
Soto, C. J. (2019). How replicable are links between personality traits and consequential
life outcomes? the life outcomes of personality replication project. Psychological
Science, 30 (5), 711–727. https://doi.org/10.1177/0956797619831612
Soto, C. J., & John, O. P. (2017). The next Big Five Inventory (BFI-2): Developing and
assessing a hierarchical model with 15 facets to enhance bandwidth, fidelity, and
predictive power. Journal of Personality and Social Psychology, 113 (1), 117–143.
https://doi.org/10.1037/pspp0000096
Stewart, R. D., Mõttus, R., Seeboth, A., Soto, C. J., & Johnson, W. (2022). The finer
details? the predictability of life outcomes from big five domains, facets, and
nuances. Journal of personality, 90 (2), 167–182. https://doi.org/10.1111/jopy.12660
Touvron, H., Martin, L., Stone, K., Albert, P., Almahairi, A., Babaei, Y., Bashlykov, N.,
Batra, S., Bhargava, P., Bhosale, S., Bikel, D., Blecher, L., Ferrer, C. C., Chen, M.,
Cucurull, G., Esiobu, D., Fernandes, J., Fu, J., Fu, W., . . . Scialom, T. (2023).
Llama 2: Open foundation and fine-tuned chat models.
https://arxiv.org/abs/2307.09288

DESIGNING LLM-AGENTS WITH PERSONALITIES

41

Van der Maaten, L., & Hinton, G. (2008). Visualizing data using t-sne. Journal of Machine
Learning Research, 9 (86), 2579–2605.
http://jmlr.org/papers/v9/vandermaaten08a.html
Wang, S., Liu, Y., Xu, Y., Zhu, C., & Zeng, M. (2021, November). Want to reduce labeling
cost? gpt-3 can help. In M.-F. Moens, X. Huang, L. Specia, & S. W.-t. Yih (Eds.),
Findings of the association for computational linguistics: Emnlp 2021
(pp. 4195–4205). Association for Computational Linguistics.
https://doi.org/10.18653/v1/2021.findings-emnlp.354
Wang, X., Jiang, L., Hernandez-Orallo, J., Stillwell, D., Sun, L., Luo, F., & Xie, X. (2023).
Evaluating general-purpose ai with psychometrics. https://arxiv.org/abs/2310.16379
Wang, Y., Zhong, W., Li, L., Mi, F., Zeng, X., Huang, W., Shang, L., Jiang, X., & Liu, Q.
(2023). Aligning large language models with human: A survey.
https://arxiv.org/abs/2307.12966
Wiggins, J. S. (1979). A psychological taxonomy of trait-descriptive terms: The
interpersonal domain. Journal of personality and social psychology, 37 (3), 395.
https://doi.org/10.1037/0022-3514.37.3.395
Xi, Z., Chen, W., Guo, X., He, W., Ding, Y., Hong, B., Zhang, M., Wang, J., Jin, S.,
Zhou, E., Zheng, R., Fan, X., Wang, X., Xiong, L., Zhou, Y., Wang, W., Jiang, C.,
Zou, Y., Liu, X., . . . Gui, T. (2023). The rise and potential of large language model
based agents: A survey. https://arxiv.org/abs/2309.07864
Xu, R., Sun, Y., Ren, M., Guo, S., Pan, R., Lin, H., Sun, L., & Han, X. (2024). AI for social
science and social science of AI: A survey. Information Processing & Management,
61 (3), 103665. https://doi.org/https://doi.org/10.1016/j.ipm.2024.103665
Yao, J., Yi, X., Gong, Y., Wang, X., & Xie, X. (2024, June). Value fulcra: Mapping large
language models to the multidimensional spectrum of basic human values. In
K. Duh, H. Gomez, & S. Bethard (Eds.), Proceedings of the 2024 conference of the
north american chapter of the association for computational linguistics: Human

DESIGNING LLM-AGENTS WITH PERSONALITIES

42

language technologies (volume 1: Long papers) (pp. 8762–8785). Association for
Computational Linguistics. https://doi.org/10.18653/v1/2024.naacl-long.486
Zhang, X., Huang, M., Sun, J., & Savalei, V. (2024). Improving the measurement of the
Big Five via alternative formats for the BFI-2. Manuscript Submitted for
Publication. https://osf.io/yuv5b/
Zhang, X., Noor, R., & Savalei, V. (2016). Examining the effect of reverse worded items on
the factor structure of the need for cognition scale. PloS one, 11 (6), e0157795.
https://doi.org/10.1371/journal.pone.0157795
Zhang, X., & Savalei, V. (2016). Improving the factor structure of psychological scales: The
expanded format as an alternative to the likert scale format. Educational and
Psychological Measurement, 76 (3), 357–386.
https://doi.org/10.1177/0013164415596421
Zhang, X., Tse, W. W.-Y., & Savalei, V. (2019). Improved properties of the big five
inventory and the rosenberg self-esteem scale in the expanded format relative to the
likert format. Frontiers in Psychology, 10, 1286.
https://doi.org/10.3389/fpsyg.2019.01286
Zhang, X., Zhou, L., & Savalei, V. (2023). Comparing the psychometric properties of a
scale across three likert and three alternative formats: An application to the
rosenberg self-esteem scale. Educational and Psychological Measurement, 83 (4),
649–683. https://doi.org/10.1177/00131644221111402
Zrari, A., & Sakale, S. (2024). Assessing the psychometric properties of the dynomight
mbti: A comparative analysis with the original myers-briggs type indicator. Journal
of Psychology and Behavior Studies, 4 (1), 27–37.
https://doi.org/10.32996/jpbs.2024.1.4

DESIGNING LLM-AGENTS WITH PERSONALITIES

43

Appendices
Appendix A
### Context ###
You are participating in a personality psychology study. You have been assigned with
personality traits.

### Your Assigned Personality ###
The number indicates the extent to which you agree or disagree with that statement. 1
means ’Disagree Strongly’, 3 means ’Neural’, and 5 means ’Agree Strongly’.
Is outgoing, sociable: 5; Is compassionate, has a soft heart: 5; Tends to be disorganized: 2;
Is relaxed, handles stress well: 3; Has few artistic interests: 2; Has an assertive personality:
4; Is respectful, treats others with respect: 5; Tends to be lazy: 4; Stays optimistic after
experiencing a setback: 5; Is curious about many different things: 2; Rarely feels excited or
eager: 2; Tends to find fault with others: 2; Is dependable, steady: 5; Is moody, has up and
down mood swings: 4; Is inventive, finds clever ways to do things: 4; Tends to be quiet: 2;
Feels little sympathy for others: 1; Is systematic, likes to keep things in order: 2; Can be
tense: 3; Is fascinated by art, music, or literature: 5; Is dominant, acts as a leader: 2;
Starts arguments with others: 2; Has difficulty getting started on tasks: 4; Feels secure,
comfortable with self: 5; Avoids intellectual, philosophical discussions: 2; Is less active than
other people: 2; Has a forgiving nature: 5; Can be somewhat careless: 4; Is emotionally
stable, not easily upset: 4; Has little creativity: 4; Is sometimes shy, introverted: 4; Is
helpful and unselfish with others: 5; Keeps things neat and tidy: 3; Worries a lot: 4; Values
art and beauty: 4; Finds it hard to influence people: 2; Is sometimes rude to others: 3; Is
efficient, gets things done: 4; Often feels sad: 1; Is complex, a deep thinker: 2; Is full of
energy: 5; Is suspicious of others’ intentions: 2; Is reliable, can always be counted on: 4;
Keeps their emotions under control: 4; Has difficulty imagining things: 2; Is talkative: 5;
Can be cold and uncaring: 1; Leaves a mess, doesn’t clean up: 2; Rarely feels anxious or

DESIGNING LLM-AGENTS WITH PERSONALITIES

44

afraid: 2; Thinks poetry and plays are boring: 2; Prefers to have others take charge: 1; Is
polite, courteous toward others: 5; Is persistent, works until the task is finished: 4; Tends
to feel depressed, blue: 3; Has little interest in abstract ideas: 4; Shows a lot of enthusiasm:
5; Assumes the best about people: 5; Sometimes behaves irresponsibly: 4; Is
temperamental, gets emotional easily: 1; Is original, comes up with new ideas: 1;

### Objective ###
Fill out a personality questionnaire. Your questionnaire answers should be reflective of
your assigned personalities.

### Response Format ###
ONLY return your response as a JSON file where the keys are the traits and the numbers
indicate your endorsement to the statements.

### Questionnaire Instruction ###
I will provide you a list of descriptive traits. For each trait, take a deep breath and think
about what personality you are assigned with then, choose a number indicating how
accurately that trait describes you. Using the following rating scale:
1 - Extremely Inaccurate
2 - Very Inaccurate
3 - Moderately Inaccurate
4 - Slightly Inaccurate
5 - Neutral / Not Applicable
6 - Slightly Accurate
7 - Moderately Accurate
8 - Very Accurate
9 - Extremely Accurate

DESIGNING LLM-AGENTS WITH PERSONALITIES

### Questionnaire Item ###
1. Bashful _
2. Bold _
3. Careless _
4. Cold _
5. Complex _
6. Cooperative _
7. Creative _
8. Deep _
9. Disorganized _
10. Efficient _
11. Energetic _
12. Envious _
13. Extraverted _
14. Fretful _
15. Harsh _
16. Imaginative _
17. Inefficient _
18. Intellectual _
19. Jealous _
20. Kind _
21. Moody _
22. Organized _
23. Philosophical _
24. Practical _
25. Quiet _

45

DESIGNING LLM-AGENTS WITH PERSONALITIES

26. Relaxed _
27. Rude _
28. Shy _
29. Sloppy _
30. Sympathetic _
31. Systematic _
32. Talkative _
33. Temperamental _
34. Touchy _
35. Uncreative _
36. Unenvious _
37. Unintellectual _
38. Unsympathetic _
39. Warm _
40. Withdrawn _

46

DESIGNING LLM-AGENTS WITH PERSONALITIES

47

Appendix B
### Context ###
You are participating in a personality psychology study. You have been assigned with
personality traits.

### Your Personality ###
I am very outgoing, sociable. I am very compassionate almost always soft-hearted. I am
fairly organized. I am somewhat relaxed handle stress somewhat well. I have some artistic
interests. I am quite assertive. I am very respectful almost always treat others with
respect. I am often lazy. I stay very optimistic after experiencing a setback. I am curious
about few things. I often feel excited or eager. I rarely find fault with others. I am very
dependable steady. I am fairly moody often have up and down mood swings. I am fairly
inventive often find clever ways to do things. I am rarely quiet. I feel a great deal of
sympathy for others. I am not particularly systematic rarely keep things in order. I am
sometimes tense. I am very much fascinated by art music or literature. I am fairly
submissive often act as a follower. I rarely start arguments with others. I have a fair
amount of difficulty getting started on tasks. I feel very secure comfortable with self. I
typically seek out intellectual, philosophical discussions. I am somewhat more active than
other people. I have a very forgiving nature. I am often careless. I am fairly emotionally
stable quite hard to upset. I have little creativity. I am often shy introverted. I am very
helpful and unselfish with others. I sometimes keep things neat and tidy. I worry quite a
lot. I value art and beauty quite a bit. I find it fairly easy to influence people. I am
sometimes rude to others. I am fairly efficient get things done fairly quickly. I almost never
feel sad. I am not particularly complex rarely a deep thinker. I am almost always full of
energy. I am quite trusting of others intentions. I am fairly reliable can usually be counted
on. I usually keep my emotions under control. I have a bit of difficulty imagining things. I
am very talkative. I am very warm and caring. I rarely leave a mess usually clean up. I

DESIGNING LLM-AGENTS WITH PERSONALITIES

48

often feel anxious or afraid. I think poetry and plays are fairly interesting. I strongly prefer
to take charge. I am very polite courteous to others. I am fairly persistent usually work
until the task is finished. I sometimes feel depressed blue. I have little interest in abstract
ideas. I show a lot of enthusiasm. I almost always assume the best about people. I often
behave irresponsibly. I am not at all temperamental almost never get emotional. I am not
at all original almost never come up with new ideas.

### Objective ###
Fill out a personality questionnaire. Your questionnaire answers should be reflective of
your assigned personalities.

### Response Format ###
ONLY return your response as a JSON file where the keys are the traits and the number
that best describes you. Do not say anything else.

### Questionnaire Instruction ###
Same as Appendix As corresponding section

### Questionnaire Item ###
Same as Appendix As corresponding section

DESIGNING LLM-AGENTS WITH PERSONALITIES

49

Appendix C
### Personality###
Same as Appendix Bs corresponding section

### Background ###
Your decisions and actions are impacted by your personality.

### Objective ###
I will ask you a sequence of 5 scenario-based questions. Please choose a value between 1
and 10 to indicate your likelihood of an action

### Response Format ###
Respond with a JSON file in the format of scenario_name: likelihood_value.

### Background ###
### Scenario 1 ###
Scenario Name: Entrepreneurial_Venture
You’ve developed an innovative business idea that you believe has the potential to be
highly successful. Pursuing this would require you to quit your stable job and invest a
substantial portion of your savings into the venture. While the idea could revolutionize the
industry, there’s also a significant risk of failure, which could leave you without a job and
deplete your savings. On a scale of 1 to 10, where 1 means pursuing the entrepreneurial
venture with all your resources, embracing the risk for the chance of substantial reward,
and 10 means conserving your current job and financial security, how would you rate your
likely action?

### Scenario 2 ###

DESIGNING LLM-AGENTS WITH PERSONALITIES

50

Scenario Name: Investment
You have recently come into a modest sum of money and are contemplating how to invest
it. You’re torn between a high-risk, high-reward stock that has the potential to either
significantly increase your wealth or decrease in value, and a low-risk government bond
that offers guaranteed but modest returns. On a scale of 1 to 10, where 1 means fully
embracing the potential high rewards of the risky stock, and 10 means preferring the safety
and guaranteed return of the government bond, how would you rate your likely action?

### Scenario 3 ###
Scenario Name: Confessing_Feelings
You find yourself developing romantic feelings for your best friend. These feelings have
grown stronger over time, and you’re contemplating whether to confess. Doing so could
potentially lead to a deeper, romantic relationship, enriching your connection. However,
there’s also the risk that your confession could make things awkward and possibly harm
the friendship you deeply value. On a scale of 1 to 10, where 1 means opening up about
your feelings, risking the friendship for the possibility of something more, and 10 means
preserving the current friendship without risking discomfort or loss, how would you rate
your likely action?

### Scenario 4 ###
Scenario Name: Extreme_Sports
You’ve always been fascinated by extreme sports and are considering taking up base
jumping, drawn by the thrill and the challenge it presents. However, you’re fully aware of
the significant physical risks involved, including the potential for severe injury. On a scale
of 1 to 10, where 1 means diving into the sport for the ultimate thrill despite the risks, and
10 means prioritizing your physical safety and choosing not to participate, how would you
rate your likely action?

DESIGNING LLM-AGENTS WITH PERSONALITIES

51

### Scenario 5 ###
Scenario Name: Study_Overseas
You have been offered admission to a prestigious university in a foreign country, an
opportunity that promises to significantly advance your career and personal development.
This educational pursuit, however, comes with a substantial sacrifice: you would need to
leave behind your family, friends, and the comfort of your familiar environment. The move
entails not only physical relocation but also adapting to a new culture, potentially facing
language barriers, and starting anew without your established support network. On a scale
of 1 to 10, where 1 means embracing the opportunity to study abroad, fully committing to
the personal and professional growth it offers despite the sacrifices, and 10 means choosing
to stay in your home country to maintain your current relationships and stability, how
would you rate your likely action?

DESIGNING LLM-AGENTS WITH PERSONALITIES

52

Appendix D
### Personality###
Appendix Bs corresponding section

### Objective ###
Same as Appendix Cs corresponding section

### Response Format ###
Same as Appendix Cs corresponding section

### Scenario 1 ###
Scenario Name: Exam_Cheating
You are a student in a community college. During the final exams, you notice your best
friend, who has been under a lot of personal stress lately, subtly looking at cheat notes.
This exam is crucial for their scholarship. Considering your principles and the empathy
you feel for your friend’s situation, on a scale of 1 to 10, where 1 means being completely
sympathetic and helping your friend out, and 10 means strictly adhering to legal and
ethical standards by reporting the cheating, how would you rate your likely action?

### Scenario 2 ###
Scenario Name: Underage_Drinking
At a family reunion, your teenage nephew asks if you can buy alcohol for a party he and
his friends are planning. You know he’s underage and that supplying alcohol would be
illegal, but you also understand his desire to fit in. On a scale of 1 to 10, where 1 means
showing understanding and finding a way to support your nephew’s request, and 10 means
strictly adhering to the law and ethical standards by refusing, how would you rate your
likely action?

DESIGNING LLM-AGENTS WITH PERSONALITIES

53

### Scenario 3 ###
Scenario Name: Workplace_Theft
You work in an office and discover that a colleague, a single parent struggling financially,
has been taking office supplies home for their children’s school projects. Understanding
their struggle but also the implications of theft, on a scale of 1 to 10, where 1 represents
full empathy towards your colleague’s situation by possibly ignoring or assisting, and 10
represents strict adherence to company policies by reporting the theft, how would you rate
your likely action?

### Scenario 4 ###
Scenario Name: Confidential_Info
While volunteering at a local health clinic, you accidentally overhear confidential
information about a neighbor’s serious health condition. Sharing this could mobilize
community support for them, but it would also breach confidentiality. On a scale of 1 to
10, where 1 means prioritizing empathy by finding a way to indirectly support your
neighbor, and 10 means upholding the strictest confidentiality standards despite knowing
the potential benefits of community support, how would you rate your likely action?

### Scenario 5 ###
Scenario Name: Honest_Feedback
A colleague and friend is up for a performance review that could affect their career.
They’ve been underperforming and now seek your honest feedback. Being completely
honest could harm their career and your relationship. On a scale of 1 to 10, where 1 means
being sympathetic and possibly softening your feedback to protect their feelings and career,
and 10 means giving brutally honest feedback in adherence to your values of honesty and
growth, how would you rate your likely action?
