---
title: "Classroom AI: large language models as grade-specific teachers"
person: james-evans
section: by
type: journal-article
year: 2026
date: 2026-03-03
venue: "npj Artificial Intelligence"
authors: "Jio Oh, Steven Euijong Whang, James Evans, Jindong Wang"
source_url: https://doi.org/10.1038/s44387-026-00081-7
openalex_id: https://openalex.org/W7133298563
retrieved: 2026-08-13
content: full-text
notes: "full text via the OpenAlex Content API (content.openalex.org)"
---

# Classroom AI: large language models as grade-specific teachers

## Full text

## Abstract

Large Language Models (LLMs) offer a promising solution to complement traditional teaching and address global teacher shortages that affect hundreds of millions of children, but they fail to provide grade-appropriate responses for students at different educational levels.We introduce a framework for finetuning LLMs to generate age-appropriate educational content across six grade levels, from lower elementary to adult education.Our framework successfully adapts explanations to match students' comprehension capacities without sacrificing factual correctness.This approach integrates seven established readability metrics through a clustering method and builds a comprehensive dataset for grade-specific content generation.Evaluations across multiple datasets with 208 human participants demonstrate substantial improvements in grade-level alignment, achieving a 35.64 percentage point increase compared to prompt-based methods while maintaining response accuracy.AI-assisted learning tailored to different grade levels has the potential to advance educational engagement and equity.

Large Language Models (LLMs) have expanded beyond traditional natural language processing into diverse domains ranging from finance 1,2 and healthcare 3,4 to education [5][6][7] .With models like GPT 8 , Gemini 9 , and LLaMA 10 now accessible worldwide, LLMs transform education by assisting teachers and students with question-solving, confusion clarification, material creation, and content personalization 6,7 .

Teacher shortages present a large and growing global challenge.UNESCO estimates 44 million additional teachers are needed to achieve universal primary and secondary education by 2030 11 , while 35% of U.S. public schools report at least one teaching vacancy 12 .Worldwide, 244 million children lack access to school 11 , with shortages most acute in rural and high-poverty areas 13 .In Pakistan, 44% of students drop out between ages 5-16 14,15 , with 18.6% leaving before completing primary education.Limited access to qualified teachers exacerbates educational disparities 13,15 , with over 70% of teachers in sub-Saharan Africa classified as inadequately trained 16 .

With 67.9% of the global population connected to the internet, LLMbased educational tools could benefit over 100 million children currently without school access and provide enhanced assistance to countless others.LLMs can deliver consistent explanations and personalized assistance regardless of geographic location, potentially increasing learning engagement and reducing educational inequity worldwide.

Effective teachers require both subject knowledge and pedagogical skills tailored to different grade levels.Despite their capabilities, LLMs struggle to provide grade-appropriate answers 17 .Even with explicit prompts like "Answer for 3rd graders", LLMs generate responses that systematically exceed the target grade's comprehension level.Existing works mostly focus on prompt-based evaluations that fail to achieve a satisfactory level due to the lack of comprehensive evaluation criteria and appropriately curated training corpora [18][19][20][21] .To serve as effective educational tools, LLMs must produce content students can understand and directly engage with.

Previous work on finetuning LLMs for specific reading levels focused primarily on summarization or paraphrasing [22][23][24] .However, real classroom settings involve open-ended questions without source texts to summarize or paraphrase.For example, when a student asks "What is gravity?" and a teacher needs LLM assistance, summarization approaches fail.This becomes critical in AI tutoring scenarios where students interact directly with LLMs.Even high-quality LLM responses provide no benefit if students cannot comprehend them.

We propose a framework for grade-level targeted finetuning of LLMs that handles open-ended educational queries across various subjects.Our approach enables grade-appropriate content generation for natural questions across six educational levels: lower elementary (grades 1-2), middle elementary (grades 3-4), upper elementary (grades 5-6), middle school (grades 7-9), high school (grades 10-12), and college/adult (grade 13+).This granular classification reflects research in educational psychology showing that reading and comprehension skills develop rapidly during early education 25,26 .This classification can provide a more accurate measure of grade-level suitability, enabling our evaluation framework to detect subtle yet significant shifts in linguistic complexity that might be overlooked.Moreover, our approach advocates for models that behave appropriately given teaching context 27 .

To assess text complexity, we integrate seven established readability metrics: Flesch Reading Ease 28 , Flesch-Kincaid Grade Level 29 , the Coleman-Liau Index 30 , Linsear Write 31 , the Gunning Fog Index 32 , Dale-Chall 33 , and the Spache Readability Formula 34 .Each metric captures different aspects of readability, and we group them based on their underlying characteristics to create a more reliable integrated measure (see Readability Metrics Integration for further details).

To address the challenge of limited training data for grade-specific content, we generate data using LLMs, a technique increasingly used for data collection and generation 35,36 .LLMs are known to generate high-quality text data that aligns with user instructions, thereby improving model performance when finetuned on such data [37][38][39] .Notably, Orca-math 40 presents a math dataset with GPT by guiding the model to adopt a teacher-student paradigm, which highlights the potential of instruction-aligned synthetic data to enhance educational resources.We categorize 54 subjects across 8 fields to create diverse questions, then use state-of-the-art LLMs (GPT 8 , Gemini 9 , LLaMA 10 , and Mixtral 41 ) to generate questions answerable across all grade levels (see Supplementary Fig. 1, for details on subjects).We craft tailored prompts for LLaMA3.1:70B to produce outputs for each grade level, then classify generated text using our integrated metrics algorithm (see Answer Generation for prompt details).

Our experiments demonstrate that this approach significantly improves grade-level alignment compared to prompt-based methods while maintaining response accuracy.Human studies with 208 participants confirm that our framework aligns with human perceptions of gradeappropriate content.

Our contributions include:

• A framework for developing grade-specific LLMs to enhance educational equity and deliver social benefits globally.• Extensive evaluation with 208 participants validating our framework's alignment with human perceptions of difficulty, showing that finetuned models can explain complex concepts at targeted grade levels.

## Results

We evaluate our method on two main dimensions: compatibility and accuracy.Compatibility measures whether finetuned models' outputs align with target grade students' comprehension capability.We assess compatibility using: (1) an integrated measure using seven readability metrics (see Supplementary Section B, for definitions of the metrics), (2) individual evaluations for each metric, and an (3) Automated Readability Index (ARI) 42 as a held-out metric to test generalizability.Accuracy measures whether the model maintains its ability to generate correct and relevant responses.We also measure perplexity and diversity gain 43 , which reflect linguistic variety relative to the training corpora and the base model.Finally, we conduct surveys with 208 human participants and GPT4o to validate our framework's alignment with human perceptions.

## Compatibility

We test the finetuned models' compatibility on all four datasets.For D GPT , D ELI , and D NQ , we use all sampled questions.For D SQ2 , we split questions based on their designated grade levels and analyze results accordingly.For example, when targeting lower elementary level, we focus exclusively on grades 1-2 questions.

As shown in Fig. 1A, our approach significantly increases target success rates for each grade level compared to prompt-based approaches, with an average improvement of 35.64 percentage points over the prompt-based baseline.The blue bars represent the success rate of each model in producing outputs at the intended grade level (higher is better), while red dots show corresponding ARI values discretized into six difficulty levels.Dots closer to the red dotted line indicate stronger alignment with ARI.Similar improvements appear for the held-out ARI metric, with our approach best aligning with intended grade levels.Detailed output grade-level distribution is shown in Supplementary Sections C.3, C.6.

Figure 1B shows that our approach successfully shifts all seven educational metrics toward their optimal values (1 for lower elementary through 6 for adult) compared to the base model or prompt-based approaches.(Note that DC, LW, FKGL, Fog, Sp, CLI, and FRES are measures for Dale-Chall, Linsear Write, Flesch-Kincaid Grade Level, Gunning Fox Index, Spache Readability Formula, Coleman-Liau Index, and Flesch Reading Ease respectively).This improvement stands out for elementary school grade levels, which previous research identified as most challenging to target 17 .

## Accuracy

We test the finetuned models' accuracy on D SQ , a multiple-choice dataset aligned with educational contexts.Figure 1C shows that finetuned models achieve performance comparable to the base model.While finetuning typically causes some accuracy reduction [44][45][46] , our results show minimal performance degradation.

## Perplexity and diversity

We measure output unexpectedness through perplexity and diversity gain (see Supplementary Sections B.2, B.3, for formulas).Figure 1D shows that lower-grade models exhibit higher values for both metrics, suggesting that text comprehensible for lower grades appears less frequently in training corpora, explaining why traditional approaches struggle with these levels.Lower-grade models convey difficult concepts using simpler language, resulting in higher diversity compared to the more direct language of existing models.

## Survey

We conduct two surveys using different datasets.Survey 1 uses questions from D NQ with 108 participants, while Survey 2 uses questions from D SQ2 with 120 participants.All participants are English-speaking and have completed high school, with most being undergraduate or graduate students who understand the relative difficulty across grade levels.We use two question types:

• Type 1: Each question includes six answers from different finetuned models ranging from lower elementary to adult.Participants assign each answer to a unique grade level, effectively ranking them.• Type 2: Each question includes one answer from a finetuned model.

Participants answer three five-point scale questions about question difficulty (Q1), answer comprehensibility (Q2), and answer accuracy (Q3).

For Type 1 questions, we measure the association between humanperceived difficulty rankings and model outputs using Kendall's τ coefficient.The high coefficient of 0.76 across 108 participants demonstrates strong agreement between intended and perceived difficulty levels.We also compute L1 distances between participant rankings and ground truth ordering.For example, given six outputs sorted by ascending grade levels, the ground-truth ranking would be [1,2,3,4,5,6].If a participant ranks them as [6,5,4,3,2,1], the L1 distances would be [5,3,1,1,3,5].The L1 distances between rankings, [0.293, 0.398, 0.659, 0.693, 0.676, 0.578], all fall below 1.Combined with the high Kendall's τ coefficient of 0.76, these results confirm our approach successfully generates grade-appropriate text aligned with human perception.Figure 1E shows dark cells along the diagonal, indicating strong alignment between model outputs and human perceptions.

For Type 2 questions, Fig. 2 shows user scores on a five-point scale for Q1, Q2, and Q3 across two surveys.For D NQ , despite relatively difficult questions (low Q1 scores), models generate outputs comprehensible for each grade level.In post-survey feedback, participants noted that lowergrade models effectively explain concepts beyond their grade level using shorter, simpler sentences.

Regarding relatively lower Q2 scores (answer comprehensibility) for lower grades, participants attributed this to topic complexity rather than explanation difficulty.One noted, "Despite how clearly the model explains the concept of LLC sublayer in an operating system, lower elementary students will struggle with the concept itself, hence I give a 1 for Q2".This observation is supported by higher Q2 scores in the second survey (D SQ2 ), where questions were designed for specific grade levels.High Q3 scores across all grade levels confirm our approach maintains factual correctness while adapting explanations.

We also evaluate surveys using GPT4o, following recent trends in using LLMs for human value alignment 47,48 .Results from GPT4o align with human evaluations, further validating our approach (see Supplementary Section C.7, for more details).

## Discussion

As students' perspectives evolve with age, we investigate whether finetuned models develop distinct worldviews by examining model layers and outputs.We finetune LLaMA3.1:8B and compare results between lower elementary and adult models.Using logit lens 49 to analyze internal model layers, we observe that lower-grade models formulate ideas more directly and succinctly, while higher-grade models favor in-depth explanations as shown in Fig. 3.This pattern mirrors human cognitive development, emphasizing clarity for younger students while preserving detail for advanced audiences.Plus, for lower-grade models, certain complex words (e.g., "atmosphere") are replaced by simpler synonyms (e.g., "air") and higher grade models internally show relatively complicated words such as "wavelength" or "dispersed".

Moreover, analysis of vocabulary and sentence structure reveals that lower-grade models use simpler words and shorter sentences, while highergrade models employ specialized terminology with longer explanations.These findings indicate our finetuning approach influences not only readability, but also the way models think and communicate, aligning each model with its target audience's comprehension needs.Detailed visualizations appear in Supplementary Section D.

Our research addresses the critical global teacher shortage that impacts millions of children, aiming to improve educational equity.Our approach introduces a novel framework for training grade-specific LLMs to deliver age-appropriate educational content.These tools can supplement traditional teaching, providing personalized support to students of different grades and potentially increasing learning engagement worldwide.We believe that our work can contribute to a future where LLM-assisted learning can help mitigate educational disparities and create broader social benefits.The authors are responsible for all analyses and the final manuscript content.

While our approach successfully tailors textual complexity, it does not fully address conceptual difficulty.For example, even when written at a lower reading level, concepts like organizational culture may remain difficult for young students to comprehend based on their limited experience with the organizational world.Future work could incorporate domain-specific knowledge graphs or concept taxonomies to provide step-by-step explanations of challenging ideas.Combining readability metrics with conceptual difficulty frameworks would create truly adaptive LLMs that match both linguistic capacity and conceptual background.

## Methods

We construct a grade-aligned question-answering dataset by generating diverse questions across eight educational fields (Question Generation) and prompting LLMs to produce answers with different readability levels (Answer Generation).We then assign grade-levels to the generated data using a novel integrated metric based on seven established readability formulas (Readability Metrics Integration) and finally fine-tune six grade-specific models to produce grade-appropriate responses (Model Training) and test the performance of the models across different datasets (Datasets).An overview of the full framework is illustrated in Fig. 4.

## Question generation

We define eight educational fields based on K-12 curriculum frameworks: art, artificial intelligence, health education, literature, music, physical education, science, and social science.Each field contains five to eight subjects (see Supplementary Fig. 1).To create a comprehensive question set, we prompt ChatGPT to generate sample questions answerable across all grades for each subject.Using these generated questions as few-shot demonstrations 8 , we employ LLMs including Gemini 9 , GPT 50 , and LLaMA 10 to generate ~550 questions per subject.

## Answer generation

We design prompts to align with readability metrics and prior works 17,20 by varying word difficulty, sentence length, and target audience.The prompt template follows: "Please provide the explanation in plain text with no bullet points using <very easy, fairly easy, fairly difficult> words that <elementary school 1st grade, elementary school 3rd grade, elementary school 5th grade, middle school 7th grade, high school 10th grade, or college> students will know.Answer in detail with at a maximum of <4, 5, 6, 7, 8, 10, 12, 15, or 20> words per sentence.".The output distribution for the corresponding prompts is shown in Supplementary Fig. 3.

We vary grade level and maximum sentence length in the input prompts, creating 54 (6 × 9) distinct question-answer pairs for each question.Word difficulty matches grade level based on the Flesch Reading Ease Metric 28 .Using our integrated metric, we classify Q&A pairs into six grade levels.The distribution appears in Supplementary Table 1.

## Readability metrics integration

We integrate seven readability metrics: Flesch Reading Ease (FRES) 28 , Flesch-Kincaid Grade Level(FKGL) 29 , the Coleman-Liau Index(CLI) 30 , Linsear Write(LW) 31 , the Gunning Fog Index(Fog) 32 , Dale-Chall(DC) 33 , and the Spache Readability Formula(Sp) 34 .Each metric captures distinct aspects of linguistic complexity through word difficulty, sentence length, and syntactic structure.Because their calculations differ substantially, we categorize them into three groups based on shared characteristics to create an integrated evaluation process: G 1 ¼ Metrics utilizing predefined easy word lists ðe:g:; DC; SpÞ ; G 2 ¼ Metrics focusing on average sentence and word length ðe:g:; FRES; FKGL; CLIÞ ; G 3 ¼ Metrics accounting for syllables per word ðe:g:; LW; FogÞ : Each formula f ∈ G i provides a grade-level L f .The final grade-level calculation follows Algorithm 1, which computes group-wise votes and determines the final grade through majority agreement or median value.

## Algorithm 1. Grade-level Integration

How does exercise help reduces stress?

## Lower Elementary Model

Exercise is good for our body.It makes us feel happy inside.When we move our body, it helps.Our brain gets a break too.We can think more clearly then.Stress goes away when we exercise.

## High Elementary Model

Exercise helps reduce stress by releasing endorphins naturally.Endorphins are chemicals that make us feel happy.When we exercise, our body produces more endorphins…

## Middle Model

Exercise helps reduce stress by releasing endorphins naturally.Endorphins are chemicals that improve mood instantly.They interact with brain receptors to calm nerves…

## Middle Elementary Model

Exercise helps our body feel better.When we move our body, it makes happy chemicals.These happy chemicals are called endorphins.Endorphins make us feel calm and relaxed…

## High Model

Exercise helps reduce stress by releasing special chemicals called endorphins into the body… Lower cortisol levels make you feel less anxious and more in control of your emotions…

## Adult Model

Exercise helps reduce stress by releasing endorphins, which are chemicals that act as natural painkillers and mood elevators.A Overview of our pipeline: we generate open-ended educational questions, prompt an LLM with readability-aligned prompt variants to generate multiple candidate explanations, classify each explanation into one of six grade-levels using our integrated readability metric, and aggregate the labeled question-answer pairs into grade-specific datasets used to finetune corresponding grade-specific models.B Example outputs for the question, "How does exercise help reduces stress?" from the six grade-specific models (lower elementary to adult), illustrating progressively more complex wording and sentence structure at higher grade-levels.

The final result L final belongs to the predefined set of grade levels: f½1; 2; ½3; 4; ½5; 6; ½7; 8; 9; ½10; 11; 12; ½13þg:

## Model training

We perform supervised finetuning on GPT4o-mini via the OpenAI API to train six grade-specific models, spanning from lower elementary to adult (college+).We train each model on the corresponding subset of our gradelabeled question and answer corpus, classified based on our integrated readability metrics.

## Datasets

We test our approach on real and synthetic datasets representing diverse grade levels.We use four datasets: ScienceQA (D SQ ) 51 , ELI5_Category (D ELI ) 52 , Natural Questions (D NQ ) 53 , and synthetic questions generated by GPT4o (D GPT ).

• D SQ : ScienceQA comprises multiple-choice questions across 21 educational domains for grades 1-12.We use this dataset to measure accuracy and convert the questions to an open-ended format using GPT4o for compatibility testing (D SQ2 ).We sample 10,876 and 10,427 questions for D SQ and D SQ2 respectively.• D ELI : ELI5_Category contains questions from Reddit requiring explanatory multi-sentence answers.We sample 12,000 questions to evaluate compatibility for open-ended questions detailed explanations.• D NQ : Natural Questions contains real user questions submitted to Google search.We sample 24,000 questions to evaluate compatibility for naturally occurring questions.• D GPT : We prompt GPT4o to create 740 questions across 54 subjects that require explanations and can be answered across all grade levels.

## Fig. 1 |

Fig. 1 | Results across evaluation criteria.A Compatibility through integrated measure and ARI; B compatibility for each metric; C accuracy; D diversity gain and perplexity; and E survey results for type 1 questions.

## Fig. 2 |

Fig. 2 | Survey results on Type 2 questions.A D NQ and B D SQ2 .Box plots show Q1 (question difficulty), Q2 (answer comprehensibility), and Q3 (model accuracy) across grade levels, with mean values as red dots on a five-point scale.Higher Q1 and Q2 results indicate lower question and answer difficulty; higher Q3 results indicate stronger accuracy.While D NQ questions appear difficult for lower grades (low Q1 in A), answers remain comprehensible (high Q2 in A).Answer comprehensibility increases (higher Q2 in B vs. A) for grade-specific questions in D SQ2 .

## Fig. 3 |

Fig. 3 | Logit-lens visualization for the lower-elementary (top) and adult (bottom) models of LLaMA3.1:8B on the prompt, "Why is the sky blue?The sky is blue because".The bottom row for each figure shows the final output tokens, and each row above represents the top prediction at each transformer layer.Warmer colors (e.g., red) indicate higher confidence.

## Fig. 4 |

Fig.4| Grade-specific LLM finetuning framework and exemplar outputs.A Overview of our pipeline: we generate open-ended educational questions, prompt an LLM with readability-aligned prompt variants to generate multiple candidate explanations, classify each explanation into one of six grade-levels using our integrated readability metric, and aggregate the labeled question-answer pairs into

npj Artificial Intelligence | (2026) 2:28
