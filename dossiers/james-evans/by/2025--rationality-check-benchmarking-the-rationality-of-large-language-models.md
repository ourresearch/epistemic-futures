---
title: "Rationality Check! Benchmarking the Rationality of Large Language Models"
person: james-evans
section: by
type: journal-article
year: 2025
date: 2025-09-18
venue: "arXiv (Cornell University)"
authors: "Zhou, Zhilun, Wang, Jing Yi, Sukiennik, Nicholas, Gao, Chen, Xu, Fengli, Li, Yong, Evans, James"
source_url: https://doi.org/10.48550/arxiv.2509.14546
openalex_id: https://openalex.org/W4417081431
retrieved: 2026-08-13
content: full-text
notes: "preprint version; full text extracted from the arXiv PDF"
---

# Rationality Check! Benchmarking the Rationality of Large Language Models

## Full text

Rationality Check! Benchmarking the Rationality of Large Language
Models
Zhilun Zhou1* Jing Yi Wang1* Nicholas Sukiennik1
†
†
Chen Gao1
Fengli Xu1 Yong Li1 James Evans2,3
1
Department of Electronic Engineering, BNRist, Tsinghua University
2
Department of Sociology, University of Chicago, Chicago, IL, USA
3
Santa Fe Institute, Santa Fe, NM, USA
{zzl22, jy-w22}@mails.tsinghua.edu.cn

arXiv:2509.14546v1 [cs.AI] 18 Sep 2025

Abstract

mance on complex reasoning and planning tasks,
such as solving mathematical problems (RomeraParedes et al., 2023), playing video games (Zhu
et al., 2023), role-playing (Shanahan et al., 2023),
etc. This showcases LLMs’ promising potential
in many fields as an agent rather than a language
model alone (Xi et al., 2023; Wang et al., 2023b).
As a result, LLM agents have been employed as emulators in many fields to simulate human activities
(Gao et al., 2023a) and serve as AI assistants (Boiko
et al., 2023; Huang et al., 2023). In these contexts,
LLMs are utilized in problem-solving and decisionmaking tasks in place of humans. Nevertheless,
the decisions made by LLMs bear immense significance for the stability of human society, particularly in critical domains dealing with personal
privacy or security. Insofar as we engaged LLM
agents for these tasks, it is critical to ensure they
can demonstrate reasonable and responsible beliefs
and actions, which motivates our assessment their
rationality in this paper.
Rationality is an anchoring concept underlying
human decision-making and belief, which can be
understood as the quality of being guided by reasons or being reasonable (Knauff and Spohn, 2021).
It typically implies an agent has reflected on the
probable consequences of their actions and the
goals they were designed to realize. In this way,
rationality is a complex concept that involves reasoning, values, and even emotions. Any particular
domain’s evaluations or definitions will only cover
specific aspects. Nevertheless, it is widely acknowledged that rationality can be divided into theoretical and practical aspects (Wahlström, 1999), with
the former focusing on whether the internal belief
is reasonable, and the latter emphasizing the capacity to make appropriate decisions in real-world
contexts. These two folds of rationality are closely
related and are both quite essential in assessing the
final actions. For LLMs, an extensive evaluation of
twofold rationality involves determining whether

Large language models (LLMs), a recent
advance in deep learning and machine
intelligence, have manifested astonishing
capacities, now considered among the most
promising for artificial general intelligence.
With human-like capabilities, LLMs have
been used to simulate humans and serve as
AI assistants across many applications. As a
result, great concern has arisen about whether
and under what circumstances LLMs think and
behave like real human agents. Rationality
is among the most important concepts in
assessing human behavior, both in thinking
(i.e., theoretical rationality) and in taking
action (i.e., practical rationality). In this work,
we propose the first benchmark for evaluating
the omnibus rationality of LLMs, covering
a wide range of domains and LLMs. The
benchmark includes an easy-to-use toolkit,
extensive experimental results, and analysis
that illuminates where LLMs converge and
diverge from idealized human rationality.
We believe the benchmark can serve as a
foundational tool for both developers and users
of LLMs. Our code and dataset can be found at
https://github.com/tsinghua-fib-lab/
LLM-Rationality-Benchmark

1

Introduction

Large Language Models (LLMs) (Zhao et al., 2023)
represent a significant advancement in the field of
artificial intelligence, manifesting human-like capability in natural language processing, understanding, and generation. As emphasized in developmental psychology, language is a primary means
through which children form mental models of the
world (McCall, 1977), constituting one of humanity’s fundamental abilities and a primary tool for
interaction with the world. Therefore, besides linguistic abilities, LLMs also exhibit strong perfor* These two authors contributed equally.
†

Corresponding authors.

1

they have human-like rationality levels in handling
real-world decisions or task execution, thereby establishing a solid foundation for safer and more
responsible AI applications.
Despite its importance, extensively benchmarking the rationality of LLMs remains unexplored. In
this work, we take the pioneering step to establish
a systematic benchmark for measuring the rationality of various LLMs, covering different domains’
definitions and assessments of rationality. Specifically, we organized the framework into six distinct
domains: psychology, cognitive science, decisionmaking, economics, game theory, and collective
rationality. Leveraging widely acknowledged rationality questionnaires from various domains, we
conduct comprehensive assessments of the rationality of various LLMs, which encompass both opensource LLMs and commercial API-based models,
aiming to extensively cover commonly used models. While it might not encompass all individual
rationality measures, our benchmark covers the
main subclasses of rationality; thus, for an uncovered measure, we believe it easy to find a suitable
substitute or reference results in our benchmark.
Overall, our benchmark serves as a fundamental
evaluation tool for both developers and users of
LLMs. For developers, the benchmark can serve
as a reference for optimizing and training models,
indicating the position of a model’s rationality and
identifying potential areas for further enhancement.
For users, our benchmark offers a standardized
evaluative system, facilitating assessments of rationality levels within specific usage scenarios. This
helps mitigate risks associated with applications
utilizing LLMs as crucial AI assistance tools in
decision-making.
Under our framework for rationality assessment,
our experiments have the following findings. First,
LLMs demonstrate an overall level of high rationality, particularly evident in larger-scale models that
exhibit greater prowess. Second, LLMs show very
high collective rationality, showcasing a greater
inclination toward cooperation and a more homogeneous AI society compared to human society.
Third, LLMs showcased higher levels of rationality in non-abstract scenarios, indicating their capability for understanding and making decisions
in real-world scenarios. Furthermore, the results
of our benchmark have revealed a multitude of
insightful observations across different domains,
including exhibiting both similar and widely different responses to humans.

Our contribution can be summarized as follows.
• We propose a comprehensive taxonomy of rationality evaluation based on extensive literature review, which organizes rationality into individual,
interpersonal, and societal levels, covering six
domains of rationality research. This taxonomy
provides a structured foundation for evaluating
rationality from both theoretical and practical
perspectives.
• Based on this taxonomy, we construct the first
benchmark for measuring LLMs’ rationality, including a wide range of questionnaires, tests, and
games.
• We conduct a detailed assessment of a bundle of
renowned LLMs and rationality scales, with extensive analyses of the results, including comparisons with human rationality, inter-domain analysis, theoretical-practical analysis, the impact of
training methodologies and model parameters on
rationality, and the relationship between individual and collective rationality. We believe that
these conclusions hold significant implications
for both developers and users of LLMs. 1

2

Related Work

2.1

Evaluation of LLMs

The most evaluated aspect for LLMs is natural
language processing, including natural language
understanding (Liang et al., 2022; Bang et al.,
2023; Peña et al., 2023; Yang and Menczer, 2023;
Lee et al., 2023) and natural language generation (Chang et al., 2023). Additionally, LLM evaluations have expanded to simulations and decisionmaking contexts, where they act as autonomous
agents mimicking human behavior (Gao et al.,
2023b; Argyle et al., 2023; Li et al., 2023). While
these evaluations provide significant insights into
LLM capabilities, the evaluation of rationality,
a core component of human cognition, remains
underdeveloped. Although some recent studies
have started to explored the rationality in LLMs
like GPT-4 (Macmillan-Scott and Musolesi, 2024),
these efforts are limited to test from a single domain
of study, e.g., cognitive psychology (MacmillanScott and Musolesi, 2024) or economics (Guo et al.,
2024), providing insufficient data for a comprehensive rationality benchmark. In contrast, our work
1
Our employed measurements and code can be
found
at
https://github.com/tsinghua-fib-lab/
LLM-Rationality-Benchmark

2

3

proposes a more rigorous framework for rationality,
systematically assessing LLMs across diverse domains to provide deeper insights into their decisionmaking processes.

2.2

Benchmark Construction

Rationality is inherently a multidisciplinary concept, and few existing studies offer a comprehensive summary of all its forms. Building on an extensive review of research across various fields (Mele
and Rawling, 2004; Knauff and Spohn, 2021), our
benchmark evaluates rationality at three levels: individual, interpersonal, and societal. Each level
includes multiple domains and a range of aspects
used to assess rationality, as summarized in Table 1. Notably, the aspects within these domains
are categorized into theoretical and practical rationality based on their intrinsic nature. Theoretical
rationality focuses on the reasonableness of internal beliefs, while practical rationality emphasizes
decision-making in real-world contexts. In this section, we briefly introduce the benchmark construction process for each domain. More details and
examples of questions and prompts are presented
in Appendix A.

Rationality and its evaluation

Rationality, defined as being guided by reason, governs both belief formation and decisionmaking (Knauff and Spohn, 2021). It is often divided into theoretical rationality, which focuses on
logical reasoning and belief coherence, and practical rationality, which involves decision-making
and mitigating cognitive biases (Wahlström, 1999).
Moreover, rationality is widely studied across disciplines. In psychology, it is examined through
constructs such as self-reflection and emotional
regulation, assessing an individual’s ability to
reflect on thoughts and manage behavior (Shulman and Carey, 1984). Cognitive science investigates how biases and heuristics affect decisionmaking (Mccready-Flora, 2014). In decision theory, rationality is evaluated based on decisionmaking styles and biases in uncertain environments (Sleboda and Sokolowska, 2017). In economics, bounded rationality acknowledges the limitations of human decision-making due to cognitive
constraints (Chapman et al., 2023), with constructs
like overconfidence and risk attitudes playing a
key role (Kahneman, 2003; Stango and Zinman,
2019). Game theory extends rationality to strategic
interactions, assessing whether agents can achieve
optimal outcomes (Edelman et al., 2007; Graham
et al., 2017). Social sciences consider collective
rationality, examining group decision-making processes and the “wisdom of the crowd” (Aher et al.,
2023; Hendrycks et al., 2020, 2021).

3.1

Psychology

This domain evaluates rationality from a psychological perspective, covering three key aspects: self-reflection, emotion regulation, and intrinsic motivation. We assess these aspects using well-established psychological questionnaires
developed in prior human studies, including the
Self-Reflection and Insight Scale (SRIS) (Grant
et al., 2002), the Emotion Regulation Questionnaire (ERQ) (Gross and John, 2003), and the Need
for Cognition (NFC) scale (Cacioppo et al., 1984).
These questionnaires are designed to capture both
theoretical rationality (e.g., awareness and clarity
of thought) and practical rationality (e.g., emotional control and motivation for thinking). We
prompt LLMs to respond as participants to these
questionnaires and compute normalized rationality
scores based on their responses.

Rationality is commonly assessed through questionnaires, using self-assessments or scenariobased tasks (Zabojnik, 2004). Since human rationality is often evaluated in this way, LLMs can
also be assessed by having them respond as participants. Previous studies have applied this approach
to evaluate cognitive skills, logical reasoning, and
decision-making in LLMs (Binz and Schulz, 2023;
Betz et al., 2020; Chen et al., 2023b). While some
research has explored specific aspects of rationality in LLMs (Binz and Schulz, 2023; Gao et al.,
2023b), no comprehensive benchmark has yet been
established.

3.2

Cognitive Science

This domain assesses rationality by examining
LLMs’ cognitive processing, reasoning abilities,
thinking dispositions, and susceptibility to biases. Specifically, we evaluate theoretical rationality through dual process theory (Evans,
2003; Stanovich et al., 2000), logical and contextbased reasoning (including inductive, deductive,
causal, defeasible, scientific, and deontic reasoning)(Goswami, 2010; Binz and Schulz, 2023;
Ragni et al., 2017), and thinking dispositions such
3

Table 1: Rationality Measurement and Evaluation
Level

Domain

Rationality Type
Theoretical

Aspect
Self-reflection

Practical

Emotion regulation

Practical

Intrinsic motivation

Psychology

Individual

Theoretical

Dual-process reasoning

Cognitive Science

Decision-making

Economics

Theoretical

Logical reasoning

Theoretical

Contextual reasoning

Practical

Thinking dispositions

Practical

Decision styles

Practical

Decision biases

Theoretical

Overconfidence

Practical

Risk attitude

Practical
Practical
Practical
Practical

Practical
Practical
Interpersonal

Game Theory

Practical
Practical
Practical
Practical

Societal

Collective Rationality

Practical

Practical

Evaluation Metric
Total score
Average score
Average score
Total score
Accuracy
Accuracy

Accuracy

Average score

Scores for each decision style
Accuracy

Deviation between confidence
and performance
Total risk-taking and risk perception score
Average score
Average score
Total

Domain-Specific
Risk
Attitude
Scale
(DOSPERT) (Blais and Weber, 2006)
Risk propensity
Risk Propensity Scale (Bachmann, 2010)
Loss aversion
Loss Aversion Task (Stango and Zinman, 2019)
Time preference
Temporal Discounting Task (Toplak et al., 2014;
Frederick, 2005)
Economic biases
Endowment effect (Kahneman et al., 1990), Sunk Accuracy
cost fallacy (Bruine de Bruin et al., 2007), Gambler’s fallacy (Leonard and Williams, 2016), Mental accounting (Rieger et al., 2022), Regression to
the mean (Toplak et al., 2014)
Auction strategy
Second-price auction (Kahneman, 2003)
Deviation of bid from true value
Iterative reasoning
Beauty contest (Arthur, 1991)
Closer choice to Nash equilibrium
Strategic cooperation
One-shot prisoner’s dilemma (Hendrycks et al., Defection rate
2020)
Repeated cooperation
Finitely repeated prisoner’s dilemma (Hendrycks Average defection rate
et al., 2020)
Public goods provision
One-shot public goods game (Hendrycks et al., Percentage of private tokens re2020)
tained
Long-term public goods Finitely repeated public goods game (Hendrycks Average percentage of private toprovision
et al., 2020)
kens retained
Cooperation and coordina- Infinitely repeated prisoner’s dilemma, Battle of Efficiency score
tion
the sexes, Minimum effort, Stag hunt (Aher et al.,
2023)
Collective
decision- Wisdom of crowds (Aher et al., 2023; Zhang et al., Group decision accuracy
making
2024; Hendrycks et al., 2020)

as critical and open-minded thinking(Sosu, 2013;
Campitelli and Gerrans, 2014). Practical rationality
is evaluated by measuring a range of cognitive biases closely tied to irrational judgment (Kahneman,
2003; Berthet and de Gardelle, 2023). All assessments are based on established cognitive science
questionnaires or reasoning tasks adapted from
prior research. LLMs are prompted to complete
these tasks as participants, and their responses are
scored and normalized to yield rationality scores
ranging from 0 (least rational) to 1 (most rational).
3.3

Assessment Method
Self-Reflection Insight Scale (SRIS) (Grant et al.,
2002)
Emotion Regulation Questionnaire (ERQ) (Gross
and John, 2003)
Need for Cognition (NFC) scale (Cacioppo et al.,
1984)
Rationality-Experiential Inventory (REI) (Pacini
and Epstein, 1999)
Cognitive Reflection Test (CRT) (Toplak et al.,
2014)
Inductive reasoning (Ekstrom, 1976), Deductive
reasoning (Liu et al., 2023a), Causal reasoning (Waldmann and Hagmayer, 2005; Binz and
Schulz, 2023)
Defeasible reasoning (Ford and Billington, 2000),
Scientific reasoning (Drummond and Fischhoff,
2017), Deontic reasoning (Ragni et al., 2017)
Critical
Thinking
Disposition
Scale
(CTDS) (Sosu, 2013), Actively Open-Minded
Thinking (AOT) Scale (Campitelli and Gerrans,
2014)
Decision Style Scale (DSS) (Scott and Bruce,
1995)
Availability heuristic (Lichtenstein et al., 1978),
Base-rate neglect (Erceg et al., 2022), Confirmation bias (Rieger et al., 2022), Framing effect (Bruine de Bruin et al., 2007), Conjunction
fallacy (Burgoyne et al., 2023)
Overconfidence test (Michailova, 2010)

nitive biases. We adopt the framework from Scott
and Bruce (Scott and Bruce, 1995) to evaluate
five decision-making styles, with an emphasis on
the rational style as indicative of higher rationality. In addition, we examine LLMs’ performance
across a set of well-established decision-making
heuristics and biases, including availability heuristic, base-rate neglect, confirmation bias, conjunction fallacy, framing effect, and others (Berthet and
de Gardelle, 2023; Ceschi et al., 2019). These tasks
are adapted from prior psychological and behavioral research (Erceg et al., 2022; Burgoyne et al.,
2023; Toplak et al., 2014; West and Stanovich,
2003; Bruine de Bruin et al., 2007), and a lower
susceptibility to biases is interpreted as reflecting

Decision-making

This domain assesses rationality through both
decision-making styles and susceptibility to cog4

greater rationality.
3.4

efficient outcomes in classic game-theoretic settings, including the infinitely repeated prisoner’s
dilemma, battle of the sexes, minimum effort, and
stag hunt. Rationality is quantified using an efficiency score (Bednar et al., 2012), which compares
actual agent payoffs to the possible maximum and
minimum. For the wisdom of crowds, we investigate whether groups of LLMs can collectively
produce more accurate decisions than individuals.
Following prior work (Aher et al., 2023; Zhang
et al., 2024), we assess group performance through
answer aggregation and multi-agent debate on general knowledge, multiple-choice (Hendrycks et al.,
2020), and math questions (Hendrycks et al., 2021).
Higher accuracy in these tasks indicates stronger
collective rationality.

Economics

In this domain, rationality is framed around utility maximization (Kahneman, 2003) and is evaluated from both theoretical and practical dimensions. We emphasize economic-specific aspects,
such as overconfidence, risk and time preferences,
and common economic biases. For theoretical
rationality, we assess overconfidence by comparing LLMs’ self-rated confidence with their actual
performance (Michailova, 2010). For practical
rationality, we examine risk preference (via risk
attitude, risk propensity (Blais and Weber, 2006;
Bachmann, 2010), and loss aversion (Stango and
Zinman, 2019)), time preference (using temporal
discounting tasks (Frederick, 2005; Toplak et al.,
2014)), and economic biases, including endowment effect (Franciosi et al., 1996), gambler’s fallacy (Leonard and Williams, 2016), mental accounting (Rieger et al., 2022), regression to the
mean (Toplak et al., 2014), and sunk cost fallacy (Bruine de Bruin et al., 2007). All tasks and
questionnaires are adapted from established economic psychology literature, and rationality scores
are determined based on lower susceptibility to bias
and greater alignment with normative economic
reasoning.
3.5

Experiment Setup

4.1

Toolkit

We developed a toolkit to test models on the same
prompts, querying multiple models (both API and
local) simultaneously and reporting performance
across different rationality domains. The toolkit
manages API and local model requests, retrieves
responses asynchronously, and processes results
based on the benchmarking scheme for rationality
assessment. Specifically, the toolkit queries commercial API-based models and open-source models
using a unified interface for both input and output,
enabling seamless comparisons between models of
different types. Then, the toolkit processes model
responses according to our rationality benchmarking framework, assessing various domains such as
psychology, cognitive science, decision-making,
and game theory, and compares results across models in each rationality domain. Finally, the toolkit
generates heatmaps visualizing the performance of
each model across all rationality types and compares LLM performance to human benchmarks,
providing a comprehensive view of rationality levels among the evaluated models.

Game Theory

This domain assesses rationality at the interpersonal level, where agents must make strategic decisions while anticipating the actions of others. We
adopt several classic economic games with welldefined Nash or subgame perfect Nash equilibria
(SPNE), including the second-price auction, beauty
contest, one-shot and finitely repeated prisoner’s
dilemma, and one-shot and finitely repeated public
goods games. These games are widely used in behavioral economics to evaluate interactive decisionmaking. In our benchmark, we construct several
agents with the same LLM and let them play the
games with each other. Rationality is measured by
how closely their behaviors align with the equilibrium strategies.
3.6

4

4.2

Models

We evaluate a mix of commercial models (e.g.,
GPT-4o, DeepSeek) and open-source models (e.g.,
Llama2, Vicuna) in our benchmark. Commercial
models, accessible via API, typically perform better due to extensive resources, while open-source
models offer versatility and modification opportunities. A complete list of models, including sizes,
is provided in Appendix B.2.

Collective Rationality

At the societal level, this domain assesses rationality through group behaviors such as cooperation and coordination and the wisdom of crowds.
For cooperation and coordination, we evaluate
whether LLM agents can work together to achieve
5

in higher cognitive load tasks. as illustrated in Figure 2b.

Rationality Assessment Domain
Psychology

Cognitive

DecisionMaking

Economics

Game
Theory

Social
Interaction

Example Question

 6 5 , 6  6 H O I  5 H I O H F W L R Q
 6 5 , 6  , Q V L J K W
 2 Y H U D O O

“A bat and a ball cost $1.10 in total. The bat costs a dollar more than the ball.
How much does the ball cost? ____ cents”

API Server
gpt-4

Deepseek-v2.5

Qwen-72b

…

Qwen-32b

    
    

                                                                                                  

    

                                                                                                 

    
    

 + X P
 J S W  D Q
   R
 G H H  J S J S W  
 S V H  W   
 H N   
 Y   
 W H
 W H [ W [ W  E L V R  E D U G
 
 W H [ W  G D Y L Q  Q    
  G  F L
 F O D X D Y L Q F L    
 G H      
 T Z H L Q V W D Q
 Q   W
 R S H  T Z H Q    E
 
 Q
 F
 K
 Z L ]  D W    E
 D U G   
 Y L F X  O P    E
 O O D P Q D    E
 D  E
 R D V      E
 V
 T Z H W    E
 Y L F X  Q   E
 O O  Q D 
 F K D D P D    E
 W J O P   E
   
 E

gpt-4o

Local Server

                                                                                                  

Qwen-7b

…

Evaluation & Model Comparisons

(a) Theoretical rationality
 ( 5 4  5 H D S S U D L V D O
 ( 5 4  6 X S S U H V V L R Q
 1 ) &
 2 Y H U D O O

Figure 1: Benchmark for assessing the rationality of
LLMs across multiple domains.

Results

The illustration of the benchmark is shown in Figure 1. Under this framework, the user can specify the domain, aspect, or LLM. The benchmark
toolkit can call and receive responses from both
open-source and commercial API-based models,
calculate the quantitative results of rationality, and
provide an analysis of the human-LLM comparison. In the following, we present heatmap results
(Figures 2- 7), normalized by human performance,
comparing different LLM models. Higher rationality is shown in orange (better than human performance), while blue indicates lower rationality
than humans. Human performance data is sourced
from literature reviews, where specific scales are
measured by the LLMs. We also conduct further
analysis on cross-domain correlations, impact of
model size, data contamination, and comparison
with reasoning models in Appendix C. We present
the original rationality scores in Appendix C.7
5.1

                                                                                                 
                                                                                                   
                                                                                               

   
   
   
   
   

 + X P
 J S W  D Q
   R
 G H H  J S J S W  
 S V H  W   
 H N   
 Y   
 W H
 W H [ W [ W  E L V R  E D U G
 
 W H [ W  G D Y L Q  Q    
  G  F L
 F O D X D Y L Q F L    
 G H      
 T Z H L Q V W D Q
 Q   W
 R S H  T Z H Q    E
 
 Q
 F
 Z L ]  K D W    E
 D U G   
 Y L F X  O P    E
 O O D P Q D    E
 D  E
 R D V      E
 V
 T Z H W    E
 Y L F X  Q   E
 O O  Q D 
 F K D D P D    E
 W J O P   E
   
 E

5

                                                                                                    

(b) Practical rationality

Figure 2: Normalized rationality scores of LLMs (x) on
different aspects (y) in psychology domain.

5.2

Cognitive Science Domain

In the cognitive science domain, as depicted in Figure 3, advanced LLMs such as GPT-4o, GPT-4,
DeepSeek v2.5, Qwen-7b, Qwen-32b, Qwen-72b,
and Bard outperform humans in several reasoning
tasks, including rational thinking, scientific reasoning, abstract reasoning, deontic reasoning, and
critical thinking dispositions. These models are
also less susceptible to cognitive biases such as
regret aversion, consistently opting for the most
optimal decision, regardless of potential regret or
hindsight bias, indicating a stronger focus on rational decision-making.
As shown in Figure 3a, LLMs consistently prefer
rational thinking over intuitive approaches as revealed by REI. Models like Qwen-72b, Qwen-32b,
and GPT-4o show a significantly stronger preference for rationality compared to humans. While
all models (except GPT-4) also rated as more inclined to engage in intuitive thinking than humans.
In terms of performance on the CRT, advanced
LLMs all performed well and well than human. In
general, results from CRT, REI, CTDS, and AOT
indicate that advanced LLMs prefer rational thinking more than other models and humans. Moreover,
DeepSeek v2.5 stands out in defeasible reasoning,
a task that is particularly difficult for humans. However, in tasks like logical reasoning, including inductive, deductive, and causal reasoning, humans
outperform LLMs. This is surprising and suggests
that future research could investigate the varying
levels of difficulty in these reasoning tasks. In
general, as we move from older to more advanced

Psychology Domain

In the psychology domain, LLMs appear to be
better than an average human in self-reflection
and emotional reappraisal and worse than human
in emotional suppression and motivation towards
higher cognitive effort tasks. As shown in Figure 2a, most LLMs, except the older models, e.g.,
chatglm2-6b and text-bison-001, are more capable of introspection and understanding their own
thoughts than average human. All LLMs outperform humans at emotional reappraisal, which
means they are better at cognitively reframing emotional situations. However, older LLM models perform better at emotion suppression, while advanced
models struggle with it. For NFC, DeepSeek and
Qwen-72b, Qwen-32b slightly outperform humans,
indicating they have greater motivation for engaging more complex cognitive tasks. Models, such
as GPT-4o and GPT-4 are less inclined to engage
6

LLMs, there is a clear improvement in their performance on cognitive science tasks. Finally, regarding the tasks involving cognitive biases, as
shown in Figure 3b, LLMs generally perform better than humans, particularly in regret aversion,
where almost all models (except smaller ones) outperform humans. Notably, Bard excels across all
cognitive bias tasks compared to humans. However,
advanced models like DeepSeek and GPT-4o struggle with biases such as illusion of control, bias
blind spot, and belief bias, indicating that while
these models excel in theoretical rationality, they
still face challenges in applying rational decisionmaking in practical scenarios.

                                                                                                      

                                                                                                     
                                                                                                  
   

                                                                                                     
   

                                                                                                  

(a) Theoretical rationality

                                                                                                   

 $ Y D L O D E L O L W \  + H X U L V W L F

                                                                                                   

 % 5 1  6 W D W L V W L F D O

                                                                                                 

 % 5 1  & D X V D O

                                                                                                    

 % 7 $ (

                                                                                                   
                         

                                               

   

   

         

 & R Q M X Q F W L R Q  ) D O O D F \

                                                                                                        

 & R Y D U L D W L R Q  ' H W H F W L R Q

                                                                                                  

 ' H Q R P L Q D W R U  1 H J O H F W

                                                                                                

   

 

                                                                                         

 3 U R E D E L O L W \  0 D W F K L Q J

                                                                                                   

 2 Y H U D O O

                                                                                                   

   
   
   

   

                                                                                                
                                                                                                
                                                                                                 

   

                                                                                                   
                                                                                           
                                                                                                  
                                                                                                 

   

                                                                                                   
                                                                                                 
                                                                                                  
                                                                                                 

   

                                                                                                
                                                                                                 
                                                                                                 
                                                                                                    

   

                                                                                                  
                                                                                                   
                                                                                      
                                                                                                  

   

                                                                                                  

Figure 5: Normalized rationality scores of LLMs (x) on
different aspects (y) in economics domain.

   

5.4

(b) Practical rationality

Economy Domain

The evaluation results in the economics domain
are shown in Figure 5. Risk-taking (RT) and risk
perceptions (RP) are both measured across five
different fields, such as financial, health, and recreational (also known as entertainment). We found
that LLMs are overly concerned with risks relating
to morality and health safety, far beyond the level
of human concern. Interestingly, while LLMs are
extremely concern about any type of risks, even
entertainment risks, such as extreme sports, in action (i.e., for risk-taking), they often do not show
the same level of concern as humans do for these
potential risks.

Figure 3: Normalized rationality scores of LLMs (x) on
different aspects (y) in the cognitive science domain.

5.3

                                                                                                 

 2 X W F R P H  % L D V

 + X P
 J S W  D Q
   R
 G H H  J S J S W  
 S V H  W   
 H N   
 Y   
 W H
 W H [ W [ W  E L V R  E D U G
 
 Q
 G
 
 D
 W H [ W  Y L Q    
  G  F L
 F O D X D Y L Q F L    
 G H      
 T Z H L Q V W D Q
 Q   W
 R S H  T Z H Q    E
 
 Q
 F
 K
 Z L ]  D W    E
 D U G   
 Y L F X  O P    E
 O O D P Q D    E
 D  E
 R D V      E
 V
 T Z H W    E
 Y L F X  Q   E
 O O  Q D 
 F K D D P D    E
 W J O P   E
   
 E

   

 + X P
 J S W  D Q
  R
 G H H  J S J S W  
 S V H  W   
 H N  Y  
   
 W H
 W H [ W [ W  E L V R  E D U G
 W H [ W  G D Y L Q  Q    
  G  F L
 F O D X D Y L Q F L    
 G H      
 T Z H L Q V W D Q W
 Q
 R S H  T Z H Q     E
 Z L ] D Q F K D W    E
 U G   
 Y L F X  O P    E
 O O D P Q D    E
 D  E
 R D V      E
 V
 T Z H W    E
 Y L F X  Q   E
 O  Q D
 F K D O D P D     E
 W J O P   E
   
 E

 % H O L H I  % L D V                                                                                                    
 % L D V  % O L Q G  6 S R W                                                                                                  
 + L Q G V L J K W  % L D V                                                                                                
 , O O X V L R Q  R I  & R Q W U R O                                                                                                    
 5 H J U H W  $ Y H U V L R Q                                                                                          
 2 Y H U D O O                                                                                                  

                                                                                                    

 P D
 J S  Q
 W  
 R
 J S
 W
 G H
 H S  J S W    
 V H
 H N    
  Y 
  
 W H [
 W H [  W  E L V  E D U G
 W  G  R Q 
 D
 W H [  Y L    
 W  G  Q F L 
 D
 F O D  Y L Q F    
 X G  L  
 H  L   
 Q
 T Z  V W D Q
 H
 W
 T Z  Q   
 R S
 E
 H
 H Q  Q  
 Z L ]  F K D W   E
 D U G    
 E
 Y L F  O P  
  E
 X
 O O D P Q D  
 
 E
 D
 R D     
 V V W  E
 T Z     E
 Y L F  H Q  
 E
 X
 O O D  Q D  
 F K  P D   E
 D W J   
 O P  E
   
 E

   

                                                                                                  

 * ' 0 6  , Q W X L W L Y H
 * ' 0 6  6 S R Q W D Q H R X V

   

 + X

   

                                                                                                  

                                                                                                

 2 Y H U F R Q I L G H Q F H
 5 7  ( W K L F D O
 5 7  ) L Q D Q F L D O
 5 7  + H D O W K  6 D I H W \
 5 7  5 H F U H D W L R Q D O
 5 7  6 R F L D O
 5 3  ( W K L F D O
 5 3  ) L Q D Q F L D O
 5 3  + H D O W K  6 D I H W \
 5 3  5 H F U H D W L R Q D O
 5 3  6 R F L D O
 5 L V N  3 U R S H Q V L W \
 / R V V  $ Y H U V L R Q
 7 H P S R U D O  ' L V F R X Q W L Q J
 ( Q G R Z P H Q W  ( I I H F W
 * D P E O H U 
 V  ) D O O D F \
 0 H Q W D O  $ F F R X Q W L Q J
 5 7 0
 6 X Q N  & R V W  ) D O O D F \
 2 Y H U D O O

   

                                                                                                      
                                                                                                 

 * ' 0 6  ' H S H Q G H Q W

                                                                                                

Figure 4: Normalized rationality scores of LLMs (x) on
different aspects (y) in decision-making domain.

                                                                                                   
                                                                                                     

                                                                                                

 ) U D P L Q J  ( I I H F W

                                                                                                 
                                                                                                    

 

 & R Q I L U P D W L R Q  % L D V

 + X P
 J S W  D Q
   R
 G H H  J S J S W  
 S V H  W   
 H N   
 Y   
 W H
 W H [ W [ W  E L V R  E D U G
 
 Q
 G
 
 D
 W H [ W  Y L Q    
  G  F L
 F O D X D Y L Q F L    
 G H      
 T Z H L Q V W D Q
 Q   W
 R S H  T Z H Q    E
 
 Q
 F
 Z L ]  K D W    E
 D U G   
 Y L F X  O P    E
 O O D P Q D    E
 D  E
 R D V      E
 V
 T Z H W    E
 Y L F X  Q   E
 O O  Q D 
 F K D D P D    E
 W J O P   E
   
 E

 5 ( ,  5 D W L R Q D O L W \
 5 ( ,  ( [ S H U L P H Q W D O L W \
 & 5 7
 / H W W H U  6 H W V  7 H V W
 / R J L T D
 & D X V D O  5 H D V R Q L Q J
 6 F L H Q W L I L F  5 H D V R Q L Q J
 ' H I H D V L E O H  5 H D V R Q L Q J
 : 6 7  $ E V W U D F W
 : 6 7  ' H R Q W L F
 & 7 ' 6
 $ 2 7
 2 Y H U D O O

 * ' 0 6  5 D W L R Q D O
 * ' 0 6  $ Y R L G D Q W

Decision-making Domain

In the decision-making domain, as shown in Figure 4, all measured LLM models rate themselves
as more rational than humans. Most models, especially newer ones, identify as avoidant, dependent,
and spontaneous decision-makers, but are less intuitive than humans, with the exception of the Qwen
models. Furthermore, GPT-4o, GPT-4, DeepSeek
v2.5, Qwen-72b, and Qwen-32b show significantly
lower susceptibility to most decision-making biases, except for the Better-than-Average Effect and
Causal Base-Rate Neglect biases.

5.5

Game Theory Domain

The evaluation results in the game theory domain
are shown in Figure 6, of which the main conclusions are as follows. Most of LLMs have lower
7

rationality than humans in the game theory domain, including models that perform best in other
domains like GPT-4. Only one LLM (text-bison)
model has a higher overall rationality than humans.
This phenomenon also holds for each specific game,
where LLMs seldom surpass human performance.
This result indicates that games are too complex for
most LLMs to handle, where players need to anticipate others’ strategies and respond accordingly.
The level of rationality is positively correlated
with the number of parameters. The overall rationalities (average of all the games) of proprietary
LLM models are generally higher than open-source
models, and 13B models are also generally more
rational than 7B models. Among them, text-bison
achieves the highest overall rationality 0.78 in the
game theory domain, surpassing human rationality
0.72. On the contrary, the smallest model chatglm26b exhibits the lowest rationality of 0.36.
Fine-tuning increases the level of rationality. We
note that openchat-13b, vicuna-13b, and wizardlm13b are fine-tuned from Llama model, and they
exhibit higher overall rationality than llama-13b,
indicating that the fine-tuning process may have a
positive effect on LLM’s rationality in game theory.

than humans. On the contrary, in a battle of the
sexes where the best strategy is to alternate between
two actions, most LLMs fail to establish such coordination with the other player.
Larger models demonstrate higher rationality in
the wisdom of crowds experiments. As shown in
Figure 7(b), gpt-4 and gpt-3.5 outperform humans
by a considerable margin. In addition, the rationality score generally decreases as the model size
becomes smaller (from left to right). Moreover, in
the general knowledge test (shown in Figure 7(c),
the closer to 1, the more rational), it can be observed that most LLMs correctly answer the five
questions no matter how we set the agent profiles,
while human answers vary greatly across different
people.

 6 H F 3 U L $ X F
 % H D & R Q
 2 Q H 3 '
 ) L Q 5 H S 3 '
 2 Q H 3 *
 ) L Q 5 H S 3 *
 2 Y H U D O O

 0 0 / 8

                                                                                                

 0 $ 7 +

                                                                                                   

 2 Y H U D O O

 

                                                                                                 

   

                                                                                                  

   

 ) L Q 5 H S 6 +

                                                                                                  

   

 ) L Q 5 H S 0 (

                                                                                               

   

 2 Y H U D O O

                                                                                           

   

 + X P
 J S W  D Q
  
 J  R
 G H H  J S  S W  
 W
 S
 W H [  V H H N     
 W H [ W  W  E L V R   Y   
 W H [ W  G D Y L Q  Q    
  G  F L 
 F O D X D Y L Q F L    
 G H     
 L
 T Z H Q V W D Q W
 Q  
 T
 Z
 R S H  H Q    E
 Q F K    E
 Z L ]  D W 
 D U G    E
 Y L F X  O P   
 E
 O O D P Q D   
 D  E
 R D V      E
 V W
 T Z     E
 Y L F X H Q   E
 O O  Q D  
 F K D D P D    E
 W J O P   E
   
 E

 , Q I 5 H S 3 '
 ) L Q 5 H S % R 6

(a) Cooperation and coordination
   
                                                                                               

   

 + X P
 J S W  D Q
   R
 G H H  J S J S W  
 S V H  W   
 W H  H  
 W H [ W [ W  E L V R N  Y   
 W H [ W  G D Y L Q  Q    
  G  F L 
 F O D X D Y L Q F L    
 G H      
 L
 T Z H Q V W D Q W
 Q 
 T
 R S H  Z H Q    E
 Z L ]  Q F K D W    E
 D U G   
 Y L F X  O P    E
 O O D P Q D    E
 D  E
 R D V      E
 V
 T Z  W    E
 Y L F X H Q   E
 O O  Q D 
 F K D D P D    E
 W J O P   E
   
 E

   

Q1

Q2

Q3

Q4

Q5

2
1

gpt
-3
pse .5
ek
text -v2.5
-bis
text on-001
-dav
incitext
0
-dav 03
inc
clau i-002
de-in
stan
qwe t
n-7
2b
qwe
n-3
2b
ope
nch
at-1
3b
wiza
rdlm
-13
b
vicu
na-1
3b
llam
a2-1
3b
oas
st-1
2b
qwe
n-7
b
vicu
na-7
b
llam
a2-7
b
cha
tglm
2-6
b
dee

Hum

0

-4

Normalized median

Figure 6: Normalized rationality scores of LLMs (x) on
different aspects (y) in game theory domain. (Missing
values in the first row is due to the lack of human experiment data of the Second Price Auction game.)

5.6

   

(b) Wisdom of crowds - MMLU and MATH
3

gpt

                                                                                              

                                                                                                

   

 + X P
 J S W  D Q
  
 J  R
 G H H  J S  S W  
 W
 S
 W H [  V H H N     
 W H [ W  W  E L V R   Y   
 W H [ W  G D Y L Q  Q    
  G  F L 
 F O D X D Y L Q F L    
 G H     
 L
 T Z H Q V W D Q W
 Q  
 T
 R S H  Z H Q    E
 Q F K    E
 Z L ]  D W 
 D U G    E
 Y L F X  O P   
 E
 O O D P Q D   
 D  E
 R D V      E
 V W
 T Z     E
 Y L F X H Q   E
 O O  Q D  
 F K D D P D    E
 W J O P   E
   
 E

   

                                                                                                  

an

                                                                                           

   

-4o

                                                                                               

   

gpt

                                                                                                

   

   

(c) Wisdom of crowds - General knowledge

Collective Rationality Domain

Figure 7: Normalized rationality scores of LLMs (x) on
different aspects (y) in collective rationality domain.

The evaluation results in the collective rationality
domain are shown in Figure 7, of which the main
conclusions are as follows.
LLMs generally perform better than humans in
cooperation and coordination games. As shown in
Figure 7(a), the overall rationality scores of almost
all LLMs are higher than that of humans. This
is probably because LLMs have relatively lower
variance and can maintain stable strategies. For
example, in minimum-effort games, LLMs tend to
consistently choose values that lead to high efficiency, resulting in much higher rationality scores

6

Conclusions

In this paper, we propose the first benchmark for
evaluating the rationality of LLMs. The results
reveal insightful observations in different domains
and various model characteristics, especially for the
comparisons with humans. The proposed toolkit of
the benchmark can benefit the developers for training better LLMs, especially for AI-human alignment, and the users for assessing whether the spe8

cific LLM is capable and suitable for a given application.

Limitations
Different Characteristics in Measurement and
Assessment Between LLMs and Humans: Due
to human-AI alignment regulations and ethical concerns, LLMs may be restricted from responding
to certain questions, which can hinder direct feedback. Unlike humans, LLMs can operate continuously without fatigue, ensuring consistent processing, whereas human respondents may experience
fatigue, affecting the quality of their responses.
Additionally, humans might manipulate their responses or show inconsistencies, leading to inaccuracies. Detecting and addressing these discrepancies is crucial for robust evaluation. Our evaluation
covers a selection of LLMs and may not represent
all existing models or relevant criteria, so broader
evaluation approaches are needed.
Data Contamination in Rationality Evaluation: LLMs may have encountered similar rationality questionnaires during training, leading to
overestimation of their rationality by recalling answers rather than reasoning. This data contamination is a recognized issue, and methods for detection and mitigation are being explored. Innovative
approaches, such as psychometric techniques and
dynamic synthesis of evaluation benchmarks, are
needed to avoid data contamination.

9

References

Marcel Binz and Eric Schulz. 2023. Using cognitive
psychology to understand gpt-3. Proceedings of the
National Academy of Sciences, 120(6):e2218523120.

Gati V Aher, Rosa I Arriaga, and Adam Tauman Kalai.
2023. Using large language models to simulate multiple humans and replicate human subject studies.
In International Conference on Machine Learning,
pages 337–371. PMLR.

Ann-Renée Blais and Elke U Weber. 2006. A domainspecific risk-taking (dospert) scale for adult populations. Judgment and Decision making, 1(1):33–47.

Rohan Anil et al. 2023. Palm 2 technical report.

Daniil A Boiko, Robert MacKnight, and Gabe Gomes.
2023. Emergent autonomous scientific research capabilities of large language models. arXiv preprint
arXiv:2304.05332.

Lisa P Argyle, Ethan C Busby, Nancy Fulda, Joshua R
Gubler, Christopher Rytting, and David Wingate.
2023. Out of one, many: Using language models to simulate human samples. Political Analysis,
31(3):337–351.

Wändi Bruine de Bruin, Andrew M Parker, and Baruch
Fischhoff. 2007. Individual differences in adult
decision-making competence. Journal of personality
and social psychology, 92(5):938.

W Brian Arthur. 1991. Designing economic agents
that act like human agents: A behavioral approach to
bounded rationality. The American economic review,
81(2):353–359.
Janet Wilde Astington and Jennifer M Jenkins. 1995.
Theory of mind development and social understanding. Cognition & Emotion, 9(2-3):151–165.

Alexander P Burgoyne, Cody A Mashburn, Jason S
Tsukahara, David Z Hambrick, and Randall W Engle.
2023. Understanding the relationship between rationality and intelligence: a latent-variable approach.
Thinking & Reasoning, 29(1):1–42.

Michael Bachmann. 2010. The risk propensity and rationality of computer hackers. International Journal
of Cyber Criminology, 4(1/2):643.

John T Cacioppo, Richard E Petty, and Chuan F Kao.
1984. The efficient assessment of need for cognition.
Journal of personality assessment.

Yejin Bang, Samuel Cahyawijaya, Nayeon Lee, Wenliang Dai, Dan Su, Bryan Wilie, Holy Lovenia, Ziwei
Ji, Tiezheng Yu, Willy Chung, et al. 2023. A multitask, multilingual, multimodal evaluation of chatgpt
on reasoning, hallucination, and interactivity. arXiv
preprint arXiv:2302.04023.

Guillermo Campitelli and Paul Gerrans. 2014. Does
the cognitive reflection test measure cognitive reflection? a mathematical modeling approach. Memory
& cognition, 42:434–447.
Andrea Ceschi, Arianna Costantini, Riccardo Sartori,
Joshua Weller, and Annamaria Di Fabio. 2019. Dimensions of decision-making: An evidence-based
classification of heuristics and biases. Personality
and Individual Differences, 146:188–200.

Jonathan Baron, Ozan Isler, and Onurcan Yilmaz. 2022.
Actively open-minded thinking and the political effects of its absence.
Jenna Bednar, Yan Chen, Tracy Xiao Liu, and Scott
Page. 2012. Behavioral spillovers and cognitive load
in multiple games: An experimental study. Games
and Economic Behavior, 74(1):12–31.

Yupeng Chang, Xu Wang, Jindong Wang, Yuan Wu,
Kaijie Zhu, Hao Chen, Linyi Yang, Xiaoyuan Yi,
Cunxiang Wang, Yidong Wang, et al. 2023. A survey on evaluation of large language models. arXiv
preprint arXiv:2307.03109.

Sebastian Bender. 2016. Reflection and rationality in
leibniz. Subjectivity and Selfhood in Medieval and
Early Modern Philosophy, pages 263–275.

Jonathan Chapman, Mark Dean, Pietro Ortoleva, Erik
Snowberg, and Colin Camerer. 2017. Willingness
to pay and willingness to accept are probably less
correlated than you think. Technical report, National
Bureau of Economic Research.

D Alan Bensley. 2023. Critical thinking, intelligence,
and unsubstantiated beliefs: An integrative review.
Journal of Intelligence, 11(11):207.
Vincent Berthet. 2021. The measurement of individual differences in cognitive biases: A review and
improvement. Frontiers in psychology, 12:630177.

Jonathan Chapman, Mark Dean, Pietro Ortoleva, Erik
Snowberg, and Colin Camerer. 2023. Econographics. Journal of Political Economy Microeconomics,
1(1):115–161.

Vincent Berthet and Vincent de Gardelle. 2023. The
heuristics-and-biases inventory: An open-source tool
to explore individual differences in rationality. Frontiers in Psychology, 14:1145246.

Bocheng Chen, Advait Paliwal, and Qiben Yan. 2023a.
Jailbreaker in jail: Moving target defense for large
language models. arXiv preprint arXiv:2310.02417.

Gregor Betz, Christian Voigt, and Kyle Richardson.
2020. Critical thinking for language models. arXiv
preprint arXiv:2009.07185.

Yiting Chen, Tracy Xiao Liu, You Shan, and Songfa
Zhong. 2023b. The emergence of economic rationality of gpt. arXiv preprint arXiv:2305.12763.

10

Wei-Lin Chiang, Zhuohan Li, Zi Lin, Ying Sheng,
Zhanghao Wu, Hao Zhang, Lianmin Zheng, Siyuan
Zhuang, Yonghao Zhuang, Joseph E. Gonzalez, Ion
Stoica, and Eric P. Xing. 2023. Vicuna: An opensource chatbot impressing gpt-4 with 90%* chatgpt
quality.

Marilyn Ford and David Billington. 2000. Strategies
in human nonmonotonic reasoning. Computational
Intelligence, 16(3):446–468.
Robert Franciosi, Praveen Kujal, Roland Michelitsch,
Vernon Smith, and Gang Deng. 1996. Experimental
tests of the endowment effect. Journal of Economic
Behavior & Organization, 30(2):213–226.

Petru Lucian Curseu. 2006. Need for cognition and
rationality in decision-making.

Shane Frederick. 2005. Cognitive reflection and decision making. Journal of Economic perspectives,
19(4):25–42.

Petru Lucian Curşeu and Sandra GL Schruijer. 2012.
Decision styles and rationality: An analysis of the
predictive validity of the general decision-making
style inventory. Educational and Psychological Measurement, 72(6):1053–1062.

Chen Gao, Xiaochong Lan, Nian Li, Yuan Yuan, Jingtao
Ding, Zhilun Zhou, Fengli Xu, and Yong Li. 2023a.
Large language models empowered agent-based modeling and simulation: A survey and perspectives.
arXiv preprint arXiv:2312.11970.

Fabio Cuzzolin, Alice Morelli, Bogdan Cirstea, and
Barbara J Sahakian. 2020. Knowing me, knowing
you: theory of mind in ai. Psychological medicine,
50(7):1057–1061.
Wim De Neys and Tamara Glumicic. 2008. Conflict
monitoring in dual process theories of thinking. Cognition, 106(3):1248–1299.

Chen Gao, Xiaochong Lan, Zhihong Lu, Jinzhu Mao,
Jinghua Piao, Huandong Wang, Depeng Jin, and
Yong Li. 2023b. S3: Social-network simulation system with large language model-empowered agents.
arXiv preprint arXiv:2307.14984.

DeepSeek-AI. 2024. Deepseek-v2: A strong, economical, and efficient mixture-of-experts language model.
Preprint, arXiv:2405.04434.

Nadia Garnefski and Vivian Kraaij. 2007. The cognitive
emotion regulation questionnaire. European journal
of psychological assessment, 23(3):141–149.

Chunyuan Deng, Yilun Zhao, Xiangru Tang, Mark Gerstein, and Arman Cohan. 2023. Investigating data
contamination in modern benchmarks for large language models. arXiv preprint arXiv:2311.09783.

Team GLM, Aohan Zeng, Bin Xu, Bowen Wang, Chenhui Zhang, Da Yin, Diego Rojas, Guanyu Feng, Hanlin Zhao, Hanyu Lai, Hao Yu, Hongning Wang, Jiadai Sun, Jiajie Zhang, Jiale Cheng, Jiayi Gui, Jie
Tang, Jing Zhang, Juanzi Li, Lei Zhao, Lindong Wu,
Lucen Zhong, Mingdao Liu, Minlie Huang, Peng
Zhang, Qinkai Zheng, Rui Lu, Shuaiqi Duan, Shudan Zhang, Shulin Cao, Shuxun Yang, Weng Lam
Tam, Wenyi Zhao, Xiao Liu, Xiao Xia, Xiaohan
Zhang, Xiaotao Gu, Xin Lv, Xinghan Liu, Xinyi Liu,
Xinyue Yang, Xixuan Song, Xunkai Zhang, Yifan
An, Yifan Xu, Yilin Niu, Yuantao Yang, Yueyan Li,
Yushi Bai, Yuxiao Dong, Zehan Qi, Zhaoyu Wang,
Zhen Yang, Zhengxiao Du, Zhenyu Hou, and Zihan
Wang. 2024. Chatglm: A family of large language
models from glm-130b to glm-4 all tools. Preprint,
arXiv:2406.12793.

Markus Domeier, Pierre Sachse, and Bernd Schäfer.
2018. Motivational reasons for biased decisions: the
sunk-cost effect’s instrumental rationality. Frontiers
in psychology, 9:815.
Caitlin Drummond and Baruch Fischhoff. 2017. Development and validation of the scientific reasoning scale. Journal of Behavioral Decision Making,
30(1):26–38.
Benjamin Edelman, Michael Ostrovsky, and Michael
Schwarz. 2007. Internet advertising and the generalized second-price auction: Selling billions of dollars worth of keywords. American economic review,
97(1):242–259.

Shahriar Golchin and Mihai Surdeanu. 2023. Time
travel in llms: Tracing data contamination in large
language models. arXiv preprint arXiv:2308.08493.

Ellery Eells. 2016. Rational decision and causality.
Cambridge University Press.

Usha Goswami. 2010. Inductive and deductive reasoning. The Wiley-Blackwell handbook of childhood
cognitive development, pages 399–419.

Ruth B Ekstrom. 1976. Kit of factor-referenced cognitive tests. Educational Testing Service.

John R Graham, Campbell R Harvey, and Manju Puri.
2017. A corporate beauty contest. Management
Science, 63(9):3044–3056.

Nikola Erceg, Zvonimir Galić, and Andreja Bubić. 2022.
Normative responding on cognitive bias tasks: Some
evidence for a weak rationality factor that is mostly
explained by numeracy and actively open-minded
thinking. Intelligence, 90:101619.

Anthony M Grant, John Franklin, and Peter Langford.
2002. The self-reflection and insight scale: A new
measure of private self-consciousness. Social Behavior and Personality: an international journal,
30(8):821–835.

Jonathan St BT Evans. 2003. In two minds: dualprocess accounts of reasoning. Trends in cognitive
sciences, 7(10):454–459.

11

James J Gross and Oliver P John. 2003. Individual differences in two emotion regulation processes: implications for affect, relationships, and well-being. Journal of personality and social psychology, 85(2):348.

Nian Li, Chen Gao, Yong Li, and Qingmin Liao. 2023.
Large language model-empowered agents for simulating macroeconomic activities. arXiv preprint
arXiv:2310.10436.

Shangmin Guo, Haoran Bu, Haochuan Wang, Yi Ren,
Dianbo Sui, Yuming Shang, and Siting Lu. 2024.
Economics arena for large language models. arXiv
preprint arXiv:2401.01735.

Percy Liang, Rishi Bommasani, Tony Lee, Dimitris
Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian
Zhang, Deepak Narayanan, Yuhuai Wu, Ananya Kumar, et al. 2022. Holistic evaluation of language
models. arXiv preprint arXiv:2211.09110.

Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou,
Mantas Mazeika, Dawn Song, and Jacob Steinhardt.
2020. Measuring massive multitask language understanding. arXiv preprint arXiv:2009.03300.

Sarah Lichtenstein, Paul Slovic, Baruch Fischhoff, Mark
Layman, and Barbara Combs. 1978. Judged frequency of lethal events. Journal of experimental
psychology: Human learning and memory, 4(6):551.

Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul
Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. 2021. Measuring mathematical problem solving with the math dataset. arXiv preprint
arXiv:2103.03874.

Hanmeng Liu, Jian Liu, Leyang Cui, Zhiyang Teng, Nan
Duan, Ming Zhou, and Yue Zhang. 2023a. Logiqa
2.0—an improved dataset for logical reasoning in
natural language understanding. IEEE/ACM Transactions on Audio, Speech, and Language Processing.

Qian Huang, Jian Vora, Percy Liang, and Jure Leskovec.
2023. Benchmarking large language models as ai
research agents. arXiv preprint arXiv:2310.03302.

Yang Liu, Yuanshun Yao, Jean-Francois Ton, Xiaoying
Zhang, Ruocheng Guo Hao Cheng, Yegor Klochkov,
Muhammad Faaiz Taufiq, and Hang Li. 2023b. Trustworthy llms: a survey and guideline for evaluating
large language models’ alignment. arXiv preprint
arXiv:2308.05374.

Aaron Hurst, Adam Lerer, Adam P Goucher, Adam
Perelman, Aditya Ramesh, Aidan Clark, AJ Ostrow, Akila Welihinda, Alan Hayes, Alec Radford,
et al. 2024. Gpt-4o system card. arXiv preprint
arXiv:2410.21276.

Olivia Macmillan-Scott and Mirco Musolesi. 2024. (ir)
rationality and cognitive biases in large language
models. Royal Society Open Science, 11(6):240255.

Daniel Kahneman. 2003. Maps of bounded rationality:
Psychology for behavioral economics. American
economic review, 93(5):1449–1475.

James Manyika and Sissie Hsiao. An overview of bard:
an early experiment with generative ai.

Daniel Kahneman, Jack L Knetsch, and Richard H
Thaler. 1990. Experimental tests of the endowment
effect and the coase theorem. Journal of political
Economy, 98(6):1325–1348.

Henry Markovits and Guilaine Nantel. 1989. The beliefbias effect in the production and evaluation of logical
conclusions. Memory & cognition, 17(1):11–17.
Robert B McCall. 1977. Challenges to a science of developmental psychology. Child Development, pages
333–344.

Alison Duncan Kerr. 2021. On the rationality of
emotion regulation. Philosophical Psychology,
34(4):453–473.
Markus Knauff and Wolfgang Spohn. 2021. The handbook of rationality. MIT Press.

Ian Mccready-Flora. 2014. Aristotle’s cognitive science: Belief, affect and rationality. Philosophy and
Phenomenological Research, 89(2):394–435.

Michal Kosinski. 2023. Theory of mind may have spontaneously emerged in large language models. arXiv
preprint arXiv:2302.02083.

Alfred R Mele and Piers Rawling. 2004. The Oxford
handbook of rationality. Oxford University Press.
Julija Michailova. 2010. Development of the overconfidence measurement instrument for the economic
experiment.

John A Lambie. 2008. On the irrationality of emotion
and the rationality of awareness. Consciousness and
cognition, 17(3):946–971.

Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida,
Carroll Wainwright, Pamela Mishkin, Chong Zhang,
Sandhini Agarwal, Katarina Slama, and Alex Ray.
2022a. Training language models to follow instructions with human feedback. Advances in Neural
Information Processing Systems, 35:27730–27744.

Noah Lee, Na Min An, and James Thorne. 2023. Can
large language models infer and disagree like humans? arXiv preprint arXiv:2305.13788.
Carrie A Leonard and Robert J Williams. 2016. The
relationship between gambling fallacies and problem gambling. Psychology of Addictive Behaviors,
30(6):694.

Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida,
Carroll Wainwright, Pamela Mishkin, Chong Zhang,
Sandhini Agarwal, Katarina Slama, Alex Ray, et al.
2022b. Training language models to follow instructions with human feedback. Advances in Neural
Information Processing Systems, 35:27730–27744.

Alan M Leslie, Ori Friedman, and Tim P German. 2004.
Core mechanisms in ‘theory of mind’. Trends in
cognitive sciences, 8(12):528–533.

12

Rosemary Pacini and Seymour Epstein. 1999. The relation of rational and experiential information processing styles to personality, basic beliefs, and the
ratio-bias phenomenon. Journal of personality and
social psychology, 76(6):972.

David P Spicer and Eugene Sadler-Smith. 2005. An
examination of the general decision making style
questionnaire in two uk samples. Journal of Managerial Psychology, 20(2):137–149.
Victor Stango and Jonathan Zinman. 2019. We are
all behavioral, more or less: Measuring and using
consumer-level behavioral sufficient statistics. Technical report, National Bureau of Economic Research.

Alejandro Peña, Aythami Morales, Julian Fierrez, Ignacio Serna, Javier Ortega-Garcia, Iñigo Puente, Jorge
Cordova, and Gonzalo Cordova. 2023. Leveraging large language models for topic classification
in the domain of public affairs. arXiv preprint
arXiv:2306.02864.

KE Stanovich, RF West, and R Hertwig. 2000. Individual differences in reasoning: Implications for
the rationality debate?-open peer commentary-the
questionable utility of cognitive ability in explaining
cognitive illusions.

Wendy J Phillips. 2020. Rational-experiential inventory. Encyclopedia of personality and individual
differences, pages 4291–4294.

Keith E Stanovich and Maggie E Toplak. 2023. Actively
open-minded thinking and its measurement. Journal
of Intelligence, 11(2):27.

Marco Ragni, Ilir Kola, and Phil Johnson-Laird. 2017.
The wason selection task: A meta-analysis. In
CogSci.

Claude Team. 2023a. Claude.

Marc Oliver Rieger, Mei Wang, Po-Kai Huang, and
Yuan-Lin Hsu. 2022. Survey evidence on core factors of behavioral biases. Journal of Behavioral and
Experimental Economics, 100:101912.

LAION Team. 2023b. Laion-ai/open-assistant.
OpenAI Team. 2023c. Gpt-4 technical report.
OpenAI Team. 2023d. Introducing chatgpt.

Bernardino
Romera-Paredes,
Mohammadamin
Barekatain, Alexander Novikov, Matej Balog,
M Pawan Kumar, Emilien Dupont, Francisco JR
Ruiz, Jordan S Ellenberg, Pengming Wang, Omar
Fawzi, et al. 2023. Mathematical discoveries from
program search with large language models. Nature,
pages 1–3.

Qwen Team. 2024. Qwen2.5: A party of foundation
models.
Predrag Teovanović, Goran Knežević, and Lazar
Stankov. 2015. Individual differences in cognitive
biases: Evidence against one-factor theory of rationality. Intelligence, 50:75–86.

Irene Scopelliti, Carey K Morewedge, Erin McCormick,
H Lauren Min, Sophie Lebrecht, and Karim S Kassam. 2015. Bias blind spot: Structure, measurement, and consequences. Management Science,
61(10):2468–2486.

Maggie E Toplak, Richard F West, and Keith E
Stanovich. 2014. Assessing miserly information processing: An expansion of the cognitive reflection test.
Thinking & reasoning, 20(2):147–168.

Susanne G Scott and Reginald A Bruce. 1995. Decisionmaking style: The development and assessment of a
new measure. Educational and psychological measurement, 55(5):818–831.

Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier
Martinet, Marie-Anne Lachaux, Timothée Lacroix,
Baptiste Rozière, Naman Goyal, Eric Hambro,
Faisal Azhar, et al. 2023. Llama: Open and efficient foundation language models. arXiv preprint
arXiv:2302.13971.

Murray Shanahan, Kyle McDonell, and Laria Reynolds.
2023. Role play with large language models. Nature,
pages 1–6.

Tomer Ullman. 2023. Large language models fail on
trivial alterations to theory-of-mind tasks. arXiv
preprint arXiv:2302.08399.

Lee S Shulman and Neil B Carey. 1984. Psychology and
the limitations of individual rationality: Implications
for the study of reasoning and civility. Review of
Educational Research, 54(4):501–524.

Björn Wahlström. 1999. A discussion of theoretical and
practical rationality.

Patrycja Sleboda and Joanna Sokolowska. 2017. Measurements of rationality: Individual differences in information processing, the transitivity of preferences
and decision strategies. Frontiers in psychology,
8:1844.

Michael R Waldmann and York Hagmayer. 2005. Seeing versus doing: two modes of accessing causal
knowledge. Journal of Experimental Psychology:
Learning, Memory, and Cognition, 31(2):216.
Guan Wang, Sijie Cheng, Xianyuan Zhan, Xiangang Li,
Sen Song, and Yang Liu. 2023a. Openchat: Advancing open-source language models with mixed-quality
data. (arXiv:2309.11235). ArXiv:2309.11235 [cs].

Edward M Sosu. 2013. The development and psychometric validation of a critical thinking disposition
scale. Thinking skills and creativity, 9:107–119.

13

Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhang, Hao
Yang, Jingsen Zhang, Zhiyuan Chen, Jiakai Tang,
Xu Chen, Yankai Lin, et al. 2023b. A survey on large
language model based autonomous agents. arXiv
preprint arXiv:2308.11432.
Qiaosi Wang, Koustuv Saha, Eric Gregori, David Joyner,
and Ashok Goel. 2021. Towards mutual theory of
mind in human-ai interaction: How language reflects
what students perceive about a virtual teaching assistant. In Proceedings of the 2021 CHI conference on
human factors in computing systems, pages 1–14.
Xuena Wang, Xueting Li, Zi Yin, Yue Wu, and Jia
Liu. 2023c. Emotional intelligence of large language models. Journal of Pacific Rim Psychology,
17:18344909231213958.
Erik Weber, Dietlinde Wouters, and Joke Meheus.
2014. Logic, reasoning, and rationality, volume 5.
Springer.
Richard F West and Keith E Stanovich. 2003. Is probability matching smart? associations between probabilistic choices and cognitive ability. Memory &
Cognition, 31:243–251.
Zhiheng Xi, Wenxiang Chen, Xin Guo, Wei He, Yiwen
Ding, Boyang Hong, Ming Zhang, Junzhe Wang,
Senjie Jin, Enyu Zhou, et al. 2023. The rise and
potential of large language model based agents: A
survey. arXiv preprint arXiv:2309.07864.
Can Xu, Qingfeng Sun, Kai Zheng, Xiubo Geng,
Pu Zhao, Jiazhan Feng, Chongyang Tao, and
Daxin Jiang. 2023. Wizardlm: Empowering large
language models to follow complex instructions.
(arXiv:2304.12244). ArXiv:2304.12244 [cs].
Kai-Cheng Yang and Filippo Menczer. 2023. Large language models can rate news outlet credibility. arXiv
preprint arXiv:2304.00228.
Jan Zabojnik. 2004. A model of rational bias in selfassessments. Economic Theory, 23:259–282.
Jintian Zhang, Xin Xu, Ningyu Zhang, Ruibo Liu,
Bryan Hooi, and Shumin Deng. 2024. Exploring
collaboration mechanisms for llm agents: A social
psychology view. In Proceedings of the 62nd Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), pages 14544–
14607.
Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang,
Xiaolei Wang, Yupeng Hou, Yingqian Min, Beichen
Zhang, Junjie Zhang, Zican Dong, et al. 2023. A
survey of large language models. arXiv preprint
arXiv:2303.18223.
Xizhou Zhu, Yuntao Chen, Hao Tian, Chenxin Tao, Weijie Su, Chenyu Yang, Gao Huang, Bin Li, Lewei Lu,
Xiaogang Wang, et al. 2023. Ghost in the minecraft:
Generally capable agents for open-world enviroments
via large language models with text-based knowledge
and memory. arXiv preprint arXiv:2305.17144.

14

Appendix
A

Detailed Measurement and Evaluation

A.1

Psychology

a 10-item scale employed by Gross et al. (Gross
and John, 2003) on human subjects. It consists of
two aspects of emotional regulation: cognitive reappraisal and expressive suppression. Cognitive reappraisal represents reevaluating situations to ameliorate their emotional impact, while expressive
suppression refers to the deliberate control of one’s
emotions (Gross and John, 2003). A higher rating
on cognitive reappraisal and expressive suppression
is scored as being more rational.
Intrinsic motivation. It refers to an individual’s
internal drive to undertake challenging cognitive
tasks (Cacioppo et al., 1984). When people are
intrinsically motivated, they are more inclined to
engage in rational thinking and decision-making
processes (Curşeu and Schruijer, 2012; Knauff and
Spohn, 2021). In this study, we used the 18-item
Need for Cognition (NFC) scale developed by Cacioppo et al. (Cacioppo et al., 1984) to assess individuals’ willingness to engage in active cognitive
activities. As indicated in prior literature, NFC is
positively correlated with rationality in decisionmaking processes (Curseu, 2006). For the scale
evaluation, several questions are reverse-scored and
a high overall average score is representative of
greater rationality.
In general, for the aspects mentioned above, we
instruct each LLM to act as a participant to answer
the questionnaires. Afterward, we calculate their
average score and normalize it to a rationality score
ranging from 0 to 1, with 0 representing the least
rational and 1 representing the most rational.
An example prompt from the psychology domain is shown below.

In the field of psychology, we employ psychometric
evaluations, commonly applied to human participants, to assess rationality from both theoretical
and practical perspectives. Specifically, we measure self-reflection as a key element of theoretical
rationality as well as emotional regulation and intrinsic motivation as vital aspects of practical rationality. The following are the detailed descriptions
of each measured aspect.
Self-reflection. It is an introspective aspect that
evaluates an individual’s awareness and clarity of
their thoughts, emotions, and behaviors (Grant
et al., 2002). It serves as a basis for the understanding and connection of arguments and judgments, leading to clearer and more logical thinking (Bender, 2016). It also plays a role in debiasing
interventions by bringing unconscious biases into
conscious awareness (Domeier et al., 2018), contributing to the enhancement of rationality. We
measure LLMs’ ability in self-reflection by adapting the Self-Reflection Insight Scale (SRIS) from
Grant et al. (Grant et al., 2002). The scale is a 20item self-rating questionnaire that consists of two
major components: self-reflection (the introspection and self-evaluation of their thoughts, feelings,
and behaviors) and insight (the clarity in acknowledging their inner self). All our used questionnaires are available on GitHub. Several questions
are reverse-scored (i.e., the score on the item indicates the opposite of the intended aspect), and
a high average score on this scale is evaluated as
being more rational.
Emotion regulation. It is the ability to control,
evaluate, and adjust one’s emotional state (Garnefski and Kraaij, 2007). Emotion can provoke errors
or even hinder goal achievement if the individual
neither intends nor decides to adopt the emotional
state (Lambie, 2008). Prior literature suggests that
effective emotion management can indicate emotional rationality (Kerr, 2021). Wang et al. (Wang
et al., 2023c) illustrate that many LLMs, such as
GPT 4, GPT 3.5 turbo, ChatGLM, and text-davinci001, are capable of understanding emotions and
have performed better than average humans on an
emotional intelligence test. In our study, we assess
LLMs’ emotion regulation ability using the Emotion Regulation Questionnaire (ERQ), which was

Prompt for Self-reflection:
Please act like a participant in this survey. For
the following statements, please respond to each
statement by selecting a number from 1 to 6. This
number should best represent your opinion on a
6-point Likert scale (1 = strongly disagree, 2 =
disagree, 3 = somewhat disagree, 4 = somewhat agree,
5 = agree, 6 = strongly agree).
1. I don’t often think about my thoughts
2. I rarely spend time in self-reflection
3. I frequently examine my feelings
4. I don’t really think about why I behave in the way
that I do
5. I frequently take time to reflect on my thoughts
6. I often think about the way I feel about things
7. I am not really interested in analyzing my behavior
8. It is important to me to evaluate the things that I do
9. I am very interested in examining what I think
about
10. It is important to me to try to understand what my
feelings mean

15

the REI scale from Pacini and Epstein (Pacini and
Epstein, 1999), which measures an individual’s tendency to engage in rational and experimental thinking processes. A rational thinking style is characterized by a tendency to make judgments analytically
and logically (“System 2”), while an experimental
thinking style is associated with the inclination to
make decisions based on intuitions, feelings, and
immediate thoughts (“System 1”) (Phillips, 2020).
Note that both rationality and experimentality can
be further broken down into two subdimensions,
namely ability and engagement; however, for our
study, we consider them collectively. In our evaluation, a higher average score on the rational component of the scale and a lower average score on
the experimental component are both considered
as indications of being more rational. Moreover,
we measure CRT as the tendency to refrain from
intuitive (“System 1”) yet incorrect responses in
favor of reflective thinking (“System 2”). Erceg
et al. (Erceg et al., 2022) have found that CRT
is highly correlated with rationality. In our study,
we utilize the 7-item CRT proposed by Toplak et
al. (Toplak et al., 2014) and calculate the correct
rate as a measurement of the degree of rationality
(e.g., a higher correction rate indicating a greater
degree of rationality).
Inductive reasoning. As a major component of
logical reasoning, inductive reasoning refers to the
ability to derive general conclusions from specific
observations or premises (Goswami, 2010). We
utilize the Letter Sets, combining part 1 and 2 of
the test in the Kit of Factor-Referenced Cognitive
Test developed by Ekstrom et al. (Ekstrom, 1976),
to assess inductive reasoning. Our test consists of
30 items, with each question presenting five groups
of four letters, and four of the sets follow the same
rule, while one does not. Participants are tasked to
identify the set with different rules. The rationality
degree is measured by the accuracy of the answers.
Deductive reasoning. As another key aspect
of logical reasoning, deductive reasoning involves
the ability to apply general rules to obtain specific
conclusions (Goswami, 2010). Adapting from Liu
et al. (Liu et al., 2023a), we randomly selected
100 multiple-choice questions from the “test.txt”
dataset provided by the researchers on their GitHub
to evaluate the LLMs. This dataset covers five
subcategories of deductive reasoning: categorical,
sufficient conditional, necessary conditional, disjunctive, and conjunctive reasoning. LLMs are
assessed on their ability to categorize aspects, in-

11. I have a definite need to understand the way that
my mind works
12. It is important to me to be able to understand how
my thoughts arise

A.2

Cognitive Science

In the field of cognitive science, similar to psychology, we evaluate LLMs’ rationality from both
theoretical and practical approaches. For theoretical rationality, we assess their cognitive processes (i.e., dual process theory), logical reasoning
(i.e., inductive, deductive, and causal reasoning),
context-based reasoning (i.e., defeasible reasoning, scientific reasoning, and deontic reasoning),
and thinking dispositions (i.e., critical thinking and
open-minded thinking). Understanding LLMs’ cognitive processing styles can offer insights into the
underlying mechanisms that govern their behaviors (Stanovich et al., 2000; Evans, 2003). Logical
reasoning is the fundamental capability of rationality (Arthur, 1991; Weber et al., 2014). These
various forms of context-specific reasoning are essential for making conditional and situational judgments, as they adapt to the unique aspects of each
situation, allowing for a more tailored approach
to the rationality assessment (Knauff and Spohn,
2021; Ragni et al., 2017). Thinking dispositions.
including critical as well as open-minded thinking
dispositions represent individuals’ cognitive styles
of thinking and they substantially relate to rationality (Stanovich et al., 2000; Erceg et al., 2022).
Lastly, we assess practical rationality through a
range of cognitive biases. As discussed in numerous studies, the use of biases often contributes to
systematic errors or irrational thinking (Kahneman,
2003; Erceg et al., 2022; Kahneman, 2003). In our
study, we engage LLMs as participants, prompting
them to respond to a variety of questionnaires that
measure different aspects related to rationality. Below are the details of the facets of rationality that
we measure.
Dual process theory. This theory is often described as the architecture of cognition that differentiates between two cognitive modalities: System 1 (i.e., intuitive, rapid, and automatic thinking) and System 2 (i.e., rational, analytic, and
controlled thinking) (Knauff and Spohn, 2021;
Evans, 2003; De Neys and Glumicic, 2008). In our
study, we assess these processes through two scales:
Rationality-Experimental Inventory (REI) and Cognitive Reflection Test (CRT). Specifically, we adapt
16

terpret “if P, then Q” conditional statements, understand necessary conditions (e.g., “P only if Q”),
handle scenarios with two premises where only one
is needed for the conclusion, and determine when
the conclusion holds true if and only if all premises
are true. LLMs’ rationality scores are determined
based on their overall accuracy in responding to all
100 questions.
Causal reasoning. Causal reasoning, critical for
understanding cause-and-effect relationships and
their underlying logic, often intersects with both
inductive and deductive reasoning, playing a core
role in our interpretation of the world (Eells, 2016;
Binz and Schulz, 2023). To measure causal reasoning, we employ a set of questions originally
developed by Waldman and Hagmayer (Waldmann
and Hagmayer, 2005) and then modified by Binz
and Schulz (Binz and Schulz, 2023). The questionnaire composites both common-cause scenarios
(e.g., a shared causal variable “A” causes two other
variables “B” and “C”) and causal-chain scenarios
(e.g., each variable sequentially causes the other:
“B” causes “A”, and “A” then causes “C” ). In particular, interventions are utilized in the test to better
scrutinize the inherent causal systems of LLMs by
manipulating a variable while observing the consequences of other variables. Each LLM receives a
rationality score based on the absolute difference
between its responses and the ideal answers.
Defeasible reasoning. This is characterized by
the ability to withdraw or revise previously held
beliefs or background knowledge in response to
new information. This form of reasoning is adaptable, allowing for adjustments based on emerging
evidence or changing situations (Chen et al., 2023a;
Ford and Billington, 2000). We apply the six defeasible reasoning questions designed by Ford and
Billington (Ford and Billington, 2000) to assess
LLMs’ abilities. Rationality score is based on the
accuracy of their answers.
Scientific reasoning. Scientific reasoning,
rooted in scientific methods and principles, evaluates LLMs’ competence in handling scientific
evidence, contributing to our understanding of
LLMs’ scientific rationality (Knauff and Spohn,
2021; Drummond and Fischhoff, 2017). Recognizing the accuracy and reliability of these models
within research contexts is crucial for determining their appropriate application in research and
acknowledging their limitations as research assistants, as prior researchers have pointed out (Liu
et al., 2023b). It guides us in effectively lever-

aging LLMs in scientific inquiries and in making
informed decisions about their use. We employ the
scientific reasoning scale developed by Drummond
and Fischhoff (Drummond and Fischhoff, 2017),
which is applicable even for individuals with no
scientific background to evaluate their scientific reasoning skills. The rationality score is determined
based on the correctness rate of LLMs’ responses.
Deontic reasoning. This involves assessing
whether actions follow or violate the normative
rules and duties, and thus practice social and moral
reasoning (Ragni et al., 2017). To assess the reasoning, we include two sets of Wason Selection
Task questions, a total of six questions, developed
by Ragni et al. (Ragni et al., 2017) and Erceg et
al. (Erceg et al., 2022). Half of the questions utilize abstract conditional reasoning, and the other
half evaluate deontic reasoning. LLMs’ abilities
in both reasoning types are evaluated. The correctness rate of LLMs’ responses, separated by the two
reasoning types, determines the rationality score.
Critical thinking disposition. This refers to
the inclination to analytically and logically think
and evaluate information or situations (Sosu, 2013;
Betz et al., 2020). In our study, we applied the
Critical Thinking Disposition Scale proposed by
Sosu (Sosu, 2013). The scale comprises two components: critical openness and reflective skepticism.
Critical openness refers to the willingness to embrace new ideas, critically analyze them, and adjust
beliefs based on new evidence. Reflective skepticism is the inclination to learn through reflecting
on prior experiences and thoroughly evaluating evidence. The rationality score is determined by the
overall average rating on the scale.
Open-minded thinking disposition. Openminded thinking disposition refers to the tendency
to consider diverse and alternative ideas, objectively assess evidence that contradicts one’s beliefs, and reflect on current thoughts (Stanovich
and Toplak, 2023). In our study, we apply the Actively Open-Minded Thinking scale, developed by
Campitelli and Gerrans (Campitelli and Gerrans,
2014), to evaluate rationality. This approach is supported by prior studies as a measurement of rational
thinking (Baron et al., 2022; Bensley, 2023; Erceg
et al., 2022). The rationality score is determined by
the overall average rating on the scale.
Cognitive biases. Cognitive biases are mental shortcuts often used to reduce cognitive load
and facilitate rapid judgments (Erceg et al., 2022;
Knauff and Spohn, 2021). They are known as sys17

tematic errors in reasoning and evaluation (Berthet
and de Gardelle, 2023). In this case, our assessment of LLMs focuses on specific biases closely related to rationality (Berthet and de Gardelle, 2023).
These biases include belief bias in syllogistic reasoning, bias blind spot, hindsight bias, illusion of
control, and regret aversion. Belief bias in syllogistic reasoning refers to the tendency to judge
an argument’s validity based on the believability
of the conclusion, rather than on logical consistency (Markovits and Nantel, 1989). We implement the measured scale from Berthet (Berthet,
2021), originally developed from Teovanović et
al. (Teovanović et al., 2015). Bias blind spot is the
tendency to perceive oneself as less biased than others (Scopelliti et al., 2015; Berthet and de Gardelle,
2023). We apply the scale from Scopelliti et
al. (Scopelliti et al., 2015). Hindsight bias represents the tendency to view past events as more predictable than they actually were (Teovanović et al.,
2015). Illusion of control refers to the tendency
to overestimate one’s control of situations (Rieger
et al., 2022). Regret aversion is the tendency to
make decisions to avoid future regret (Berthet and
de Gardelle, 2023). We assess the performance of
LLMs on these three biases, adopting tests from
Rieger et al. (Rieger et al., 2022), to evaluate their
susceptibility. For all applied scales, we determine
the presence of these biases in LLMs and inversely
adjust the final scores to reflect rationality levels.
In sum, similar to the evaluation of psychology
aspects, we compute an average score based on selfassessment or accuracy for the scales and normalize
the final scores to reflect rationality levels, where 0
signifies the least rational and 1 signifies the most
rational.
An example prompt from the cognitive science
domain is shown below.

c. the card labeled with "22 years of age"
d. the card labeled with "16 years of age"

A.3

Decision-making

In the field of decision-making theory, research
outlines representative patterns to categorize individuals by their decision-making styles. Scott
and Bruce (Scott and Bruce, 1995) developed
a self-report questionnaire that delineates five
decision-making styles: rational, intuitive, dependent, avoidant, and spontaneous. The rational style
refers to the logical and structured approaches to
decision-making; the intuitive style indicates the
reliance upon hunches, feelings, and impressions;
dependent style means the reliance upon the direction and support of others; the avoidant style entails
postponing or avoiding decision-making; and spontaneous style is characterized by being impulsive
and prone to making “snap” or “spur of the moment” decisions (Scott and Bruce, 1995; Spicer and
Sadler-Smith, 2005). We evaluate LLMs across different decision-making styles, interpreting a higher
score in the rational style as a stronger propensity
towards rationality and a lower score in all other
styles as a weaker propensity towards rationality.
Furthermore, we assess LLMs on various
decision-making related heuristics and biases, the
systematic deviations that are inherent in the
decision-making processes: availability heuristics,
base-rate neglect (statistical and causal), betterthan-average, confirmation bias, conjunction fallacy, covariation detection, denominator neglect,
framing effect, probabilistic matching, and outcome bias (Berthet and de Gardelle, 2023; Ceschi
et al., 2019). Availability heuristic refers to the
inclination to evaluate the likelihood or frequency
of an event by how immediately examples come
to one’s mind. We assess the availability heuristic
using the task from Erceg et al. (Erceg et al., 2022),
originally developed by Lichtenstein et al. (Lichtenstein et al., 1978). Base-rate neglect is the propensity to neglect base-rate information in favor of
specific instances. It has two forms: statistical baserate neglect refers to general base-rate information,
and causal base-rate neglect indicates causationrelated base-rate information. We adopt the tasks
provided by Erceg et al. (Erceg et al., 2022) to
measure these aspects. Better-than-average effect describes the tendency for individuals to consider their abilities, traits, and characteristics to be
above the average level of their peers. This bias is

Prompt for Watson selection task:
Please act like a participant in this survey. Imagine
you are a police officer on duty. It is your job to
ensure that people conform to certain rules. There are
four cards shown to you that have information about
four people sitting at a table. Each card is labeled
with "Drinking beer", "Drinking coke", "22 years of
age", and "16 years of age" on one side of the card,
respectively. On one side of a card is a person’s age
and on the other side of the card is what a person
is drinking. Here is a rule: If a person is drinking
beer, then that person must be over 18 years of age.
Select the cards that you need to turn over to determine
whether or not the people are violating the rule.
a. the card labeled with "Drinking beer"
b. the card labeled with "Drinking coke"

18

measured using the scale from Erceg et al. (Erceg
et al., 2022). Confirmation bias involves the tendency to interpret and favor information that aligns
with one’s beliefs and values. In this case, we
assess the susceptibility of LLMs toward confirmation bias through a set of financial decision-making
tasks (Rieger et al., 2022). Conjunction fallacy
represents the tendency to erroneously believe that
the combination of two events is more probable
than either event occurring independently. We
adapt the scenario task from Burgoyne et al. (Burgoyne et al., 2023) to evaluate the bias. Covariation detection is the tendency to overestimate
the relationship between two variables, often exacerbated by neglecting essential comparative (e.g.,
control group) information. We utilize the scenario
task proposed by Toplak et al. (Toplak et al., 2014)
to measure the bias. Denominator neglect, also
known as the ratio bias, indicates the tendency to
focus excessively on numerators while neglecting
denominators, affecting the judgment of probabilities, especially when presented in different ratio
formats. We assess it using the task from Toplak et
al. (Toplak et al., 2014). Framing effect refers to
the tendency for people’s decisions to be influenced
by the way in which information is presented, particularly with respect to risk-choice and attribute
framing. To evaluate both forms of this effect concurrently, we employ the task methodology from
Bruine de Bruin et al. (Bruine de Bruin et al., 2007).
Probability matching is the inclination of aligning
the proportions of choices with the proportions of
outcomes in a binary prediction task, rather than
optimizing for the most likely outcome. The bias
is measured by the dice problem and card guessing
game implemented by West and Stanovich (West
and Stanovich, 2003). Outcome bias indicates the
tendency to evaluate a decision based on the outcome rather than the quality of the decision at the
time it was made. We employ Erecg et al. (Erceg
et al., 2022) to measure the bias. In sum, a higher
susceptibility to biases indicates a lower score in
rationality.
An example prompt from the decision-making
domain is shown below.

in a fancy neighborhood. He expresses himself nicely
and is very interested in politics. He invests a lot of
time in his career. Which is more likely?
a. John is a nurse.
b. John is a doctor.

A.4

Economics

In the field of economics, rationality is commonly
understood as the maximization of utility (Kahneman, 2003). It can also be categorized into theoretical and practical dimensions. Particularly, given
the overlapping interests with other domains mentioned previously, we focus more on the unique
aspects prominent in economics. In the theoretical
aspect, overconfidence is a key factor influencing
individuals’ economic judgment. Overconfidence
refers to individuals’ inclination to overestimate
their capabilities, which could lead to poor judgment. We measure the aspect using the metrics
provided by Michailova et al. (Michailova, 2010)
where we compare the difference between LLMs’
performance and their self-rated confidence level
on the test. Rationality score is determined as the
resistance to overconfidence.
For practical rationality, the evaluation contains
several major aspects, including risk preference,
time preference, and economic biases. Risk preference is measured by risk attitude, risk propensity,
and loss aversion. In our study, we apply the revised version of domain-specific risk attitude scale
developed by Blais and Weber (Blais and Weber,
2006). The scale measures across five different domains (i.e., ethical, financial, health or safety, recreational, and social) between two different facets
(i.e., risk-taking and risk perception). Rationality degree is determined by the lower risk-taking
and higher risk perception score towards these riskrelated questions. Risk propensity, as another dimension of risk preference, is assessed using the
5-item risk propensity scale included in prior literature (Bachmann, 2010). Lower risk propensity
indicates a higher degree of rationality. Furthermore, loss aversion, often considered as a variation
in risk aversion (Stango and Zinman, 2019), is the
tendency to prefer avoiding losses over acquiring
gains (Chapman et al., 2017). To measure this
aspect, we employ the task proposed by Stango
and Zinman (Stango and Zinman, 2019), which
captures the influence of loss aversion on decisionmaking processes. The degree of rationality is determined by the lower score of loss aversion. Moreover, time preference is assessed through a task

Prompt for Base-rate neglect:
Please act like a participant in this survey and answer
the following questions. Among the 1000 people that
participated in the study, there were 995 nurses and 5
doctors. John is randomly chosen participant in this
research. He is 34 years old. He lives in a nice house

19

that measures temporal discounting, which is the
phenomenon of favoring more immediate rewards
over future benefits. The task we utilize is adapted
from Toplak et al.(Toplak et al., 2014), originally
developed by Frederick(Frederick, 2005). Rationality is indicated by a lower propensity for temporal
discounting.
Finally, we evaluate the susceptibility of LLMs
to economic-related biases: endowment effect,
gambler’s fallacy, mental accounting, regression
to the mean, and sunk cost fallacy (Berthet and
de Gardelle, 2023; Stango and Zinman, 2019). Endowment effect is characterized by the tendency
for individuals to value an object more once they
own it, compared to when they do not. To measure
this effect, we adapt the mug problem from Franciosi et al. (Franciosi et al., 1996), which was initially developed from Kahneman et al. (Kahneman
et al., 1990). The effect is quantified by subtracting the willingness to pay (the maximum amount
one is willing to pay to acquire an object) from the
willingness to accept (the minimum amount one
is willing to accept to give up the object). Gambler’s fallacy delineates the erroneous belief that
a departure from what occurs on average will be
corrected in the short term, such as believing that
a run of one outcome in a chance event will result in an increased probability of the opposite outcome in the next instance. The bias is measured
using the questionnaire provided by Leonard and
Williams (Leonard and Williams, 2016). Mental
accounting refers to the practice of valuing the
same amount of money differently based on subjective criteria, such as the source of the money
or its intended use. It is assessed through the task
provided by Riger et al. (Rieger et al., 2022). Regression to the mean describes the tendency to
overlook the statistical phenomenon that exceptionally high or low performances or measurements
are likely to be followed by more moderate ones.
We adopt the task from Toplak et al. (Toplak et al.,
2014) to measure the bias. Sunk cost fallacy is
the inclination to continue an endeavor once an investment in money, effort, or time has been made,
based on the investment already made rather than
current and future costs and benefits. We adopt the
task from Bruine de Bruin et al. (Bruine de Bruin
et al., 2007) to measure the fallacy. The degree of
rationality refers to the lower susceptibility towards
various biases.
An example prompt from the economics domain
is shown below.

Prompt for Loss aversion:
Please act like a participant in this survey and answer
the following questions. Now, imagine you have a
choice between the following two options:
Option A: A lottery with a 50% chance of winning
$80 and a 50% chance of losing $50.
Option B: Zero dollars.
Which option would you choose?
a. Option A
b. Option B

A.5

Game Theory

In game theory, rational players are expected to
maximize their payoffs based on anticipating others’ choices, resulting in a Nash equilibrium, where
each player’s strategy is the best response to others’ strategies. In particular, we choose secondprice auction, beauty contest, one-shot prisoner’s
dilemma, finitely repeated prisoner’s dilemma, oneshot public goods game, and finitely repeated public goods game. All these games have a unique
subgame perfect Nash equilibrium (SPNE), and we
measure rationality by the extent to which agents
can play as Nash equilibrium.
Second price auction (SecPriAuc). This is an
auction game with only one item. Two bidders
simultaneously bid a price. Then the bidder with
a higher price wins the item and only needs to pay
the second highest bid. A dominant strategy in this
game is to place a bid equaling to the bidder’s value
of the item. As a result, we calculate the rationality
degree as the deviation of bid from one’s value:
R = |bid − value|/value.
Beauty contest (BeaCon). In this game, two
players simultaneously choose a number between 0
and 100, and the winner is the player whose number
is closest to two-thirds of the average of all chosen
numbers. The Nash equilibrium in this game is to
choose zero, so the rationality degree is calculated
as R = |100 − number chosen|/100.
One-shot prisoner’s dilemma (OnePD). This
a classic game where two players simultaneously
choose to cooperate (choice F) for mutual benefit or
defect (choice J) for individual earnings, as shown
in Figure 8(a). The unique Nash equilibrium here
is mutual defection, so we calculate the rationality
degree as the defection rate.
Finitely repeated prisoner’s dilemma (FinRepPD). This is the repeated version of prisoner’s
dilemma where two players play the prisoner’s
dilemma for ten rounds. The payoff matrix in each
round is the same (Figure 8(a)). The unique SPNE
is that both players defect in every round. There20

(a)
Prisoner’s
dilemma

(b) Stag hunt

on the interaction between agents. However, what
we are concerned with here is whether agents can
achieve better results together through cooperation
and coordination instead of competing with each
other. Therefore, we let LLM agents play games
that need cooperation (infinitely repeated prisoner’s
dilemma) and coordination (battle of the sexes,
minimum effort, stag hunt). In these games, the
rationality is measured by the efficiency (Bednar
et al., 2012), which is defined as the actual payoff
normalized by the maximum payoff and minimum
payoff the player might receive:

(c) Battle of the
sexes

Figure 8: Payoff matrix of prisoner’s dilemma, stag hunt
and battle of the sexes.

fore, we measure the rationality degree as the average defection rate of all rounds.
One-shot public goods game (OnePG). In this
game, each player has some tokens and simultaneously choose how many of them to contribute to
the public account. Then all tokens in the public account are multiplied by a factor and equally shared
among all players. Although everyone contributing
all tokens to the public can yield the maximum total payoff, the only Nash equilibrium in this game
is zero contributions of all players. Therefore, we
measure the rationality degree as the percentage of
private tokens.
Finitely repeated public goods game (FinRepPG). This is the repeated version of public
goods game and the unique SPNE is to keep all
tokens as private in all rounds. Similar to one-shot
PG, the rationality degree is calculated as the average percentage of private tokens of all rounds.
An example prompt from the game theory domain is shown below.

Efficiency =

(1)

This metric lies in [0, 1] and a larger efficiency indicates that agents can achieve better payoffs, thus
being more rational. Specifically, in the infinitely
repeated prisoner’s dilemma, cooperation can be
supported as a subgame perfect Nash equilibrium
with the highest efficiency. In the coordination
games, there are multiple Nash equilibria with different efficiency, and rational players are expected
to play the Pareto-efficient one.
Wisdom of crowds. This means that groups
can make better and more rational decisions than
individuals. We let a group of LLM agents collaborate to solve a problem through aggregating the
answers (Aher et al., 2023) or debate (Zhang et al.,
2024). In the first experiment, we follow (Aher
et al., 2023) and ask a group of LLM agents with
different profiles to answer 5 general-knowledge
questions. In the second experiment, LLM agents
are asked to solve multiple-choice (Hendrycks
et al., 2020) or math problems (Hendrycks et al.,
2021), where several LLM agents discuss with each
other and revise their answers. The rationality degree is measured by the accuracy of answers.
An example prompt from the collective rationality domain is shown below.

Prompt for Beauty Contest:
Please act as a human player. You are playing a game
with another human player (called the opponent) for
only one round. You and the opponent will simultaneously choose a number between 0 and 100 (including
0 and 100). The winner is the player whose number
is closest to two thirds of the average of all chosen
numbers. The winner will earn 100 points, and the
other player will earn nothing. If there is a tie, both
players will earn 50 points. Your goal is to maximize
your own earnings. You should first think carefully
about what to do, and then make a decision. Now
let’s start the game. Tell me how you think and the
number you would like to choose. Please answer in
json format with keys ’thought’ and ’number’. The
’number’ should be between 0 and 100 (including 0
and 100).

A.6

Payoffsactual − Payoffsmin
Payoffsmax − Payoffsmin

Prompt for Stag Hunt:
Please act as a human player. You are playing a game
with another human player (called the opponent) for
10 rounds. In each round, you and the opponent will
simultaneously choose an action between F and J. If
you choose J and the opponent chooses J, you earn
10 points and the opponent earns 10 points in this
round... Before you choose an action, your actions,
the opponent’s actions and your earnings in each of
the previous rounds will be shown. Your goal is to
maximize your own total earnings in all 10 rounds.
In each round, you should first think carefully about
what to do, and then choose one of the two actions:
F or J. The history of the game is listed as follows

Collective Rationality

In the society domain, we measure rationality
by cooperation and coordination, and wisdom of
crowds.
Rationality of cooperation and coordination.
Similar to game theory, this evaluation also focuses
21

Local server: Aside from the commercial models, which are accessed by API, there is a bundle
of open-sourced models which is widely used. In
our benchmark, we provide a general, easy-to-use
interface to call the locally deployed models. That
is, with the arguments specified for the path of
the deployed large language models (or automated
downloading from mirror websites when the name
of the OSS model is given). The usage of OSS is
similar to that of the commercial models based on
the uniform interface of both input and output, as
described above.

delimited by triple backticks.
“‘
{history}
“‘
It is round-{round} out of 10 rounds now. Tell me
how you think and the action you would like to choose.
Please answer in json format with keys ’thought’ and
’action’. The ’action’ should be F or J. Please return
only one json.

B

Supplementary Information for
Experiment Setup

B.1

Toolkit

B.1.1 Input: Configuration and Arguments
In order to seamlessly test a collection of models
on the same prompts without having to change contexts constantly, we develop a toolkit that queries
multiple models at a time for a given input prompt
and reports the relative and overall performance
across all of them. As seen in figure 1, the user
first passes a prompt that can include both text and
image. When submitted, the data will be sent to
the API servers of each of the models to retrieve
the responses. After the prompt is sent, the toolkit
will create two separate workflows, one requesting
the APIs and another requesting the offline models
on the local server.

B.1.3

Performance Testing

Once the responses from both the APIs and the
local server are retrieved, the toolkit will automatically collect and process the results according to
our benchmarking scheme, which includes each of
the forms of rationality tested in this work: psychology, cognitive, decision making, economics,
game theory, and collective rationality. Once the
rationality performance is gauged for all the models, their results are compared across each of the
groupings under each form of rationality tested.
For example, under psychology, there are prompts
for both theoretical and practical rationality. Under
each sub-grouping, there are individual prompts
to test different aspects of it, e.g., self-reflection
and insight. These results are then passed to the
next module for processing and visualization, as
described below.

B.1.2 Model Response
API server: The models called via the toolkit
include all the models in our work that are accessible by API, namely those that are commercial rather than open-source: gpt-4, gpt-3.5, bard,
claude-instant, text-bison, text-davinci-002, and
text-davinci-003. The APIs are requested asynchronously so that multiple APIs can be called and
their responses received concurrently. The models
that can accept image inputs are bard and gpt-4,
whereas the rest accept exclusively text. The API
interface that is requested for each model is in some
cases is made available by its provider, thereby allowing developers to easily integrate theirs into a
versatile array of applications. However, in other
cases, third-party APIs are used. Specifically, gpt-4,
gpt-3.5, text-davinci-003, and text-davinci-003 are
accessed via OpenAI’s platform2 , text-bison is accessed via Google’s PaLM API interface3 , bard is
queried via a third-party API4 , and finally, claudeinstant is accessed via Poe5 .

B.1.4

Output: Results and Comparison

After all sub-groupings under each rationality
type are fully processed, the toolkit will output
a heatmap comparing the results across each model.
Finally, once all forms of rationality are tested, the
toolkit offers the ability to visualize the full model
benchmark comparison across all forms of rationality in addition to human-LLM comparison, offering
a bird’s eye view of the overall state of rationality
among the most powerful LLMs. It should be noted
that relevant API-keys are required to access certain
models, which can be retrieved from the relevant
API platforms. Therefore, prior to using the toolkit,
one must register for the services on their respective platforms, which in some cases may involve a
fee.

2

B.2

https://openai.com
https://ai.google.dev/models/palm
4
https://github.com/dsdanielpark/Bard-API
5
https://poe.com

Models

3

We have employed a collection of some of the most
widely used models, both open-source and com22

Table 2: LLMs utilized in our benchmark.
Type

API

OSS

Model
gpt-4o (Hurst et al., 2024)
gpt-4 (Team, 2023c)
gpt-3.5 (Team, 2023d)
text-davinci-002 (Ouyang et al., 2022a)
text-davinci-003 (Ouyang et al., 2022a)
deepseek-v2.5 (DeepSeek-AI, 2024)
bard (Manyika and Hsiao)
text-bison (Anil et al., 2023)
claude-instant (Team, 2023a)
Qwen2.5-72B-Instruct (Team, 2024)
Qwen2.5-32B-Instruct (Team, 2024)
Qwen2.5-7B-Instruct (Team, 2024)
Llama-2-13b (Touvron et al., 2023)
Llama-2-7b (Touvron et al., 2023)
openchat-13b (Wang et al., 2023a)
WizardLM-13B (Xu et al., 2023)
vicuna-13b (Chiang et al., 2023)
vicuna-7b (Chiang et al., 2023)
oasst-12b (Team, 2023b)
chatglm2-6b (GLM et al., 2024)

Size*
∼200B
∼1.8T
∼175B
∼175B
∼175B
236B
∼137B
∼340B
∼130B
72B
32B
7B
13B
7B
13B
13B
13B
7B
12B
6B

Year
2024
2023
2022
2022
2022
2024
2023
2023
2023
2024
2024
2024
2023
2023
2023
2023
2023
2023
2023
2023

Version
2024-08-06
1106
1106
v2.5
v1.2
v2.5
v2.5
v2.5
chat
chat
v3.2
v1.2
v1.5
v1.5
sft-4
v2

Creator
OpenAI
OpenAI
OpenAI
OpenAI
OpenAI
DeepSeek
Google
Google
Anthropic
Alibaba Cloud
Alibaba Cloud
Alibaba Cloud
Meta
Meta
Tsinghua
Microsoft
LMSYS
LMSYS
LAION
Tsinghua

*The sizes of some API-based models are actually unknown as they have not
been publicized. ∼ represents their estimated parameter size.

mercial. The commercial models are accessible
via APIs (as described in section B.1), whereas the
open-source models are downloaded and trained
individually, making them more versatile and open
to modification. However, commercial models typically perform better due to the access to highly
valuable data and computing resources that nonprofits and academic institutions seldom have. A
complete list of model details, including sizes and
a brief description, is provided in Table 2.

additional or special types of data, as well as their
overall number of parameters. Additionally, the
way in which humans play a role in the reinforcement learning stage varies across each one.

C

Supplementary Experiment Results

C.1

Correlation Among Different Domains.

The evaluation of rationality is conducted on different domains, leaving us an interesting question
of how the ability in different domains is correlated. That is, some domains’ rationality may share
a similar definition, or the ability level depends on
some common abilities. Therefore, to present the
correlation among different domains, we present
the results in Appendix Figure 9. Specifically, in
Appendix Figure 9 (b), we further merge the theoretical and practical evaluations in each domain by
computing the average. From the results, we have
the following observations.
From the overall view, rationality in different
domains is highly related. In these two heatmap
figures, most of the correlation values are positive, revealing strong relations in different domains.
These can be explained in two ways. First, many
different scales in various domains are similar, with
different emphases, but they share the same ability.
Second, the abilities affecting the rationality level
may depend on some shared basic abilities. For
example, in theoretical rationality, the reasoning
ability may affect a lot of aspects of rationality in
different domains.
In addition, some domains have significantly
lower correlations than others. Specifically, for

Commercial LLM models: There are seven
models in total: five models released by OpenAI:
gpt-4o, gpt-4, gpt-3.5, text-davinci-002, and textdavinci-003; one model released by Deepseek:
deepseek v2.5; two models released by Google:
bard, text-bison; and one model released by Anthropic: claude-instant. The number of the parameters used to train these models is undisclosed
although it can be estimated.
Open-Source LLM models: There are eight
models from a variety of academic and corporate institutions. Notably, llama2-13b and llama2-7b are
provided open source by Meta, whereas the others
(Qwen-72b/32b/7b, openchat-13b, wizardlm-13b,
vicuna-13b, vicuna-7b, oasst-12b, chatglm2-6b)
are from academic or other institutions who have
released their source code publicly. In contrast to
commercial models, they all publicize the number
of parameters they use.
Most of the models follow a similar paradigm of
reinforcement with human feedback on top of a pretrained transformer model. However, the ways in
which they differ usually involve fine-tuning with
23

1.00 0.21 0.52 0.50 0.42 0.19 0.54 0.11 0.01 0.47

1.00

Psychology 1.00 0.34 0.21 0.49 0.18 0.31

0.75

0.52 0.11 1.00 0.50 0.85 0.67 0.65 0.50 -0.05 0.97

0.50

Cognitive and Behavioral Science 0.34 1.00 0.90 0.65 0.49 0.87

0.25

Decision Making 0.21 0.90 1.00 0.46 0.35 0.86

0.50 -0.19 0.50 1.00 0.67 0.44 0.39 0.29 0.20 0.48
0.42 -0.04 0.85 0.67 1.00 0.48 0.45 0.35 0.24 0.81
0.19 0.00 0.67 0.44 0.48 1.00 0.68 0.72 -0.10 0.67

Domain

0.21 1.00 0.11 -0.19 -0.04 0.00 0.28 0.17 -0.06 0.10

0.00

Economics 0.49 0.65 0.46 1.00 0.45 0.62

Society 0.31 0.87 0.86 0.62 0.28 1.00

0.47 0.10 0.97 0.48 0.81 0.67 0.61 0.49 -0.11 1.00

0.75

Psychology

0.01 -0.06 -0.05 0.20 0.24 -0.10 0.10 -0.33 1.00 -0.11

1.00

Domain

(a) Correlation among different domains

1.00
0.75
0.50
0.25
0.00
0.25
0.50
0.75
1.00

Society

0.50

Economics

0.11 0.17 0.50 0.29 0.35 0.72 0.43 1.00 -0.33 0.49

Game theory

Game theory 0.18 0.49 0.35 0.45 1.00 0.28

Decision Making

0.25

Cognitive and Behavioral Science

0.54 0.28 0.65 0.39 0.45 0.68 1.00 0.43 0.10 0.61

Psychology
Theoretical
Psychology
Practical
Cognitive and Behavioral Science
Theoretical
Cognitive and Behavioral Science
Practical
Decision Making
Practical
Economics
Theoretical
Economics
Practical
Game theory
Practical
Society
Cooperation and coordination
Society
Wisdom of crowd

Domain

Psychology
Theoretical
Psychology
Practical
Cognitive and Behavioral Science
Theoretical
Cognitive and Behavioral Science
Practical
Decision Making
Practical
Economics
Theoretical
Economics
Practical
Game theory
Practical
Society
Cooperation and coordination
Society
Wisdom of crowd

Domain

(b) Correlation among different domains (practical and
theoretical rationality is merged).

Figure 9: The correlation of the average rationality in different domains.
text-bison-001

gpt-4o

qwen-32b

llama2-13b

0.70

0.56
0.54
0.52
0.50

qwen-72b

0.75

Overall rationality

Overall rationality

text-davinci-002
0.58
text-davinci-003

qwen-7b

deepseek-v2.5

0.65
0.60
0.55

wizardlm-13b
openchat-13b
llama2-13b
vicuna-13b

chatglm2-6b vicuna-7b
0.50
llama2-7b
oasst-12b
0.45
1010

chatglm2-6b
llama2-7b
1012
Training data size (tokens)

gpt-4

(a) Impact of parameter size

claude-instant
text-davinci-002 text-bison-001
gpt-3.5
text-davinci-003

1011
Model size

1012

(b) Impact of dataset size

Figure 10: Impact of parameter size and data size on rationality.

“psychology-practical”, we can observe that its correlation is much smaller, which can be explained by
the fact that EQR tests in psychology-practical focus more on the quite different aspects of emotional
regulation compared with scales in other domains
or the theoretical rationality of psychology domain.
C.2

varying training methodologies, and the sufficiency
of data used in training.
C.3

Impact of Reinforcement Learning with
Human Feedback

Reinforcement learning with human feedback
(RLHF) (Ouyang et al., 2022b) is the recent advance of reinforcement learning, which has shown
good performance in training language models.
Specifically, it is different from the traditional reinforcement learning methods, which receive the
reward from the environment, such as the score
in the game environment; instead, in RLHF, the
model can take feedback from humans. Therefore,
in training LLMs, the human feedback integrated
by RLHF also takes human characteristics into the
model. One representative example is the value
alignment in politics, wherein ChatGPT has similar preferences with those about forty hired men/women in labeling the training samples in RLHF.

Impact of Dataset Size and Model Size

LLMs exhibit remarkable abilities that correlate
with their parameter sizes (Zhao et al., 2023). Thus,
studying how model size affects rationality is crucial. Additionally, the training dataset size influences their reasoning and knowledge, prompting an
examination of its impact on rationality evaluations.
Appendix Figure 10 shows a strong positive correlation between model size and rationality, with
larger models generally displaying higher rationality. However, no strong relationship is observed
between rationality and training dataset size, which
may be influenced by factors such as dataset quality,
24

Human
text-davinci-003
(RLHF)
text-davinci-002

Society

Practical

Domain

Game theory
Economics

Human
text-davinci-003
(RLHF)
text-davinci-002

Decision Making

Theoretical

Cognitive and Behavioral Science
Psychology
0.0

0.2

0.4

Rationality

0.6

0.0

0.8

0.1

0.2

0.3

0.4

Rationality

0.5

0.6

0.7

Figure 11: Impact of reinforcement learning with human feedback.

qwen-72b
0.70

gpt-4o qwen-32b
qwen-7b gpt-4

Practical rationality

0.65

deepseek-v2.5

wizardlm-13b
text-davinci-002
claude-instant
openchat-13b
text-davinci-003
vicuna-13b
llama2-13b
0.55
gpt-3.5
vicuna-7b
chatglm2-6b
0.50 oasst-12b
llama2-7b
0.60

0.50

text-bison-001

0.55

0.60

0.65 0.70 0.75
Theoretical rationality

0.80

0.85

Figure 12: Relation between theoretical rationality and practical rationality.

As a result, when assessing whether the LLMs behave rationally, RLHF is worth studying as it may
cause the LLM to exhibit a similar amount of high
or low rationality as real human beings. Since
text-davinci-003 is the improved version of textdavinci-002, having introduced the technique of
RLHF, comparing rationality between the two can
help us understand the impact of RLHF, for which
the results are shown in Appendix Figure 11.
C.4

the action is rational. As illustrated in Appendix
Figure 12, there is a strong correlation between theoretical rationality and practical rationality. GPT-4
has both the best practical rationality and practical
rationality overall. Those open-source models with
the fewest model parameters have the lowest theoretical and practical rationality. GPT-3.5 has high
theoretical rationality but low practical rationality,
which is very interesting. As we know, theoretical
rationality is more about basic reasoning, belief,
and thinking, while practical rationality ensures the
selected action is rational given the belief is correct.

Correlation Between Theoretical and
Practical Domain.

As mentioned above, rationality can be overall divided into theoretical rationality and practical rationality, of which the previous one focuses more
on how to reason, and the latter about whether

C.5

Data Contamination Analysis

One potential limitation of our work is the data
contamination of LLMs. The contamination prob25

lem arises when LLMs have previously encountered similar rationality questionnaires during their
training, which could lead to an overestimation of
their rationality. Essentially, the LLMs might be
recalling answers rather than genuinely reasoning
through the questions, thus skewing the results of
our benchmarking efforts. Such data contamination problem is widely recognized as a universal
issue in truthful LLM evaluation (Deng et al., 2023;
Golchin and Surdeanu, 2023), especially as LLM
are gaining increasing access to enormous training
datasets.
In this section, we conduct experiments to assess
the potential impact of data contamination issue.
Specifically, for experiments at the interpersonal
and societal level, the payoff matrices of games and
prompts are manually constructed, and thus there
is no data contamination issue. However, the questions in the individual level are from existing scales
and tests. To verify whether data contamination
affects the results, we slightly modify the questions
of several tests to ensure that the questions do not
appear in the training data of LLMs. Then, we
test different LLMs on the modified questions, and
compare the results with original ones.
Specifically, we choose three typical tests, including the Cognitive Reflection Test, Base-Rate
Neglect (Statistical), and Conjunction Fallacy.
These tests are popularly used and thus are likely to
have data contamination issues. We modify these
tests from the following aspects.
Changing character names. For example, for
the following question in Base-Rate Neglect (Statistical) test, we replace the character name ”John”
with a randomly sampled name (Aher et al., 2023)
without changing the answers as follows:

b. Mr. WERITO is a doctor.

Changing the numerical value in the questions. For example, for the following question in
Cognitive Reflection Test, we change the number
“48” to “24”, and the correct answer also changes
from 47 to 23.
Original:
In a lake, there is a patch of lily pads. Every day, the
patch doubles in size. If it takes 48 days for the patch
to cover the entire lake, how long would it take for the
patch to cover half of the lake? _ days
Modified:
In a lake, there is a patch of lily pads. Every day, the
patch doubles in size. If it takes 24 days for the patch
to cover the entire lake, how long would it take for the
patch to cover half of the lake? _ days

Considering that LLMs from different creators
may use different training datasets, we conduct
experiments on LLMs from a wide range of creators, including OpenAI, Meta, Deepseek, Alibaba,
Tsinghua, Microsoft, LMSYS, and LAION. Their
rationality scores are presented in Table 3, calculated as the accuracy on these questions. It can be
observed that most LLMs obtain similar rationality scores after modifying the questions, indicating
that the data contamination issue does not affects
the results significantly.
Table 3: Comparison of rationality scores on modified
questions with original questions.
gpt-4o
deepseek-v2.5
openchat-13b
wizardlm-13b
vicuna-13b
oasst-12b
qwen-7b
llama-7b

Original:
Among the 1000 people that participated in the study,
there were 995 nurses and 5 doctors. John is randomly chosen participant in this research. He is 34
years old. He lives in a nice house in a fancy neighborhood. He expresses himself nicely and is very
interested in politics. He invests a lot of time in his
career. Which is more likely?
a. John is a nurse.
b. John is a doctor.
Modified:
Among the 1000 people that participated in the study,
there were 995 nurses and 5 doctors. Mr. WERITO
is randomly chosen participant in this research. He
is 34 years old. He lives in a nice house in a fancy
neighborhood. He expresses himself nicely and is very
interested in politics. He invests a lot of time in his
career. Which is more likely?
a. Mr. WERITO is a nurse.

C.6

Original
0.882
0.647
0.294
0.176
0.176
0.235
0.706
0.118

Modified
0.882
0.588
0.294
0.118
0.118
0.353
0.706
0.059

Comparison with Reasoning Model

In this section, we test several recent reasoning
models on our benchmark, including OpenAI o1,
Deepseek R1, and DeepSeek-R1-Distill-Qwen32B (a distilled model based on Qwen2.5-32B using outputs from DeepSeek R1). As shown in Table 4, reasoning models such as o1 show a higher
overall rationality score compared to GPT-4o.
However, Deepseek R1 has a slightly lower score
than Deepseek V3, while DeepSeek-R1-DistillQwen-32B outperforms Qwen-32B. Deepseek V3
holds the highest cognitive rationality score among
26

 5 ( ,  5 D W L R Q D O L W \                                                                                                  
 5 ( ,  ( [ S H U L P H Q W D O L W \                                                                                                 
 & 5 7                                                                                          
 / H W W H U  6 H W V  7 H V W                                                                                                
 / R J L T D                                                                                                   
 & D X V D O  5 H D V R Q L Q J                                                                                                      
 6 F L H Q W L I L F  5 H D V R Q L Q J                                                                                                
 ' H I H D V L E O H  5 H D V R Q L Q J                                                                                                    
 : 6 7  $ E V W U D F W                                                               
 : 6 7  ' H R Q W L F                                                                                 
 & 7 ' 6                                                                                                         
 $ 2 7                                                                                                         
 2 Y H U D O O                                                                                                      

C.7

Original Rationality Scores

 % H O L H I  % L D V                                                                                      
 % L D V  % O L Q G  6 S R W                                                                                                     
 + L Q G V L J K W  % L D V                                                                       
 , O O X V L R Q  R I  & R Q W U R O                                                           
 5 H J U H W  $ Y H U V L R Q                                                                                                      
 2 Y H U D O O                                                                                                        

    
    
    
    

   

   

   

   
   
   
   
   
   

(b) Practical rationality
   
   
   

Figure 14: Rationality scores of LLMs (x) on different
aspects (y) in the cognitive science domain.

   
   

 + X P
 J S W  D Q
   R
 G H H  J S J S W  
 S V H  W   
 H N   
 Y   
 W H
 W H [ W [ W  E L V R  E D U G
 
 Q
 G
 
 W H [ W  D Y L Q    
  G  F L
 F O D X D Y L Q F L    
 G H      
 T Z H L Q V W D Q
 Q   W
 R S H  T Z H Q    E
 
 Q
 F
 Z L ]  K D W    E
 D U G   
 Y L F X  O P    E
 O O D P Q D    E
 D  E
 R D V      E
 V
 T Z  W    E
 Y L F X H Q   E
 O O  Q D 
 F K D D P D    E
 W J O P   E
   
 E

   

ment, particularly in areas requiring rapid data analysis and nuanced comprehension, fostering a synergistic relationship between human cognition and
machine intelligence for more effective decisionmaking.

(b) Practical rationality

Figure 13: Rationality scores of LLMs (x) on different
aspects (y) in psychology domain.

D

   

 + X P
 J S W  D Q
  R
 G H H  J S J S W  
 S V H  W   
 H N  Y  
   
 W H
 W H [ W [ W  E L V R  E D U G
 W H [ W  G D Y L Q  Q    
  G  F L
 F O D X D Y L Q F L    
 G H      
 T Z H L Q V W D Q W
 Q
 R S H  T Z H Q     E
 Z L ] D Q F K D W    E
 U G   
 Y L F X  O P    E
 O O D P Q D    E
 D  E
 R D V      E
 V
 T Z H W    E
 Y L F X  Q   E
 O  Q D
 F K D O D P D     E
 W J O P   E
   
 E

    

 + X P
 J S W  D Q
   R
 G H H  J S J S W  
 S V H  W   
 H N   
 Y   
 W H
 W H [ W [ W  E L V R  E D U G
 W H [ W  G D Y L Q  Q    
  G  F L
 F O D X D Y L Q F L    
 G H      
 T Z H L Q V W D Q
 Q   W
 R S H  T Z H Q    E
 
 Z L ]  Q F K D W    E
 D U G    E
 O
 P
 Y L F X    
 O O D P Q D    E
 D  E
 R D V      E
 V
 T Z  W    E
 Y L F X H Q   E
 O O  Q D 
 F K D D P D    E
 W J O P   E
   
 E

(a) Theoretical rationality
 ( 5 4  5 H D S S U D L V D O                                                                                                     
 ( 5 4  6 X S S U H V V L R Q                                                                                                      
 1 ) &                                                                                                        
 2 Y H U D O O                                                                                                         

   

(a) Theoretical rationality

We present the original rationality scores of LLMs
in Figure 13, 14, 15, 16, 17, and 18.
 6 5 , 6  6 H O I  5 H I O H F W L R Q                                                                                                      
 6 5 , 6  , Q V L J K W                                                                                                  
 2 Y H U D O O                                                                                                       

   

 + X P
 J S W  D Q
   R
 G H H  J S J S W  
 S V H  W   
 H N   
 Y   
 W H
 W H [ W [ W  E L V R  E D U G
 W H [ W  G D Y L Q  Q    
  G  F L
 F O D X D Y L Q F L    
 G H      
 T Z H L Q V W D Q
 Q   W
 R S H  T Z H Q    E
 
 Z L ]  Q F K D W    E
 D U G   
 Y L F X  O P    E
 O O D P Q D    E
 D  E
 R D V      E
 V
 T Z H W    E
 Y L F X  Q   E
 O O  Q D 
 F K D D P D    E
 W J O P   E
   
 E

the LLMs. This suggests that while reasoning models can demonstrate high rationality, they do not
always lead to more cognitively rational behavior.
Based on our observations, these models tend to
spend significantly more time in their reasoning
processes, sometimes leading to overthinking during their responses. This pattern of reasoning models not consistently outperforming other models is
evident across the various domains analyzed.

Rational Models and Predictability: Measuring LLM rationality is crucial for predicting their
behavior in human interactions. Theory of Mind
(ToM) (Leslie et al., 2004), the ability to attribute
mental states to oneself and others, is key to this.
While LLMs can emulate ToM, it’s uncertain if they
truly grasp mental states (Ullman, 2023; Kosinski,
2023). ToM enables LLMs to understand nuances
in human interaction, including sarcasm, humor,
and indirect speech (Wang et al., 2021). Genuine ToM capability enhances LLMs’ rational and
contextually appropriate responses. Incorporating
ToM into LLMs can develop empathy and moral
reasoning, crucial in emotional support or ethical
dilemmas. This represents advanced rationality, a
key aspect of human intelligence (Cuzzolin et al.,
2020). However, integrating ToM into LLMs poses
challenges, requiring advanced algorithms and an
understanding of human cognitive and social processes. Measuring this capability involves exploring how humans develop ToM (Astington and Jenkins, 1995) and simulating these processes in LLMs.

Open Discussions

LLMs as Simulators: Evaluating LLMs reveals
their capacity to emulate human behavior, offering
insights that refine their contextual understanding,
coherence, and responsiveness. These evaluations
allow developers to tailor LLMs for diverse communication scenarios, enhancing their roles in natural language processing, conversational AI, and
decision-making. This process ultimately advances
LLMs as sophisticated tools that mirror and augment human-like rationality.
LLMs as AI Assistants: Evaluating LLMs enhances their utility in decision-making by leveraging their rationality. These comprehensive evaluations guide the integration of LLMs into decisionmaking frameworks, aiding in complex scenarios.
Insights from these evaluations ensure the reliability and consistency of LLM outputs, making
them valuable support systems. This understanding enables decision-makers to improve their judg27

Table 4: Comparison of rationality score with reasoning models on cognitive science domain.
Aspect

Scale
REI Rationality
REI Experimentality
Cognitive Reflection Test
Letter Sets Test
Logiqa 2.0
Causal Reasoning
Scientific Reasoning Scale
Defeasible Reasoning
Wason Selection Task - Abstract
Wason Selection Task - Deontic
Critical Thinking Disposition Scale
Actively Open-Minded Thinking Scale
Belief Bias in Syllogistic Reasoning
Bias Blind Spot
Hindsight Bias
Illusion of Control
Regret Aversion
Overall

Dual System Thinking
Inductive Reasoning
Deductive Reasoning
Causal Reasoning
Scientific Reasoning
Defeasible Reasoning
Deontic Reasoning
Thinking Disposition

Heuristics and Biases

Overall

o1
0.84
0.28
1.00
0.93
0.79
0.85
1.00
0.67
1.00
1.00
0.86
0.73
0.75
0.72
1.00
0.00
0.67
0.77

                           
          

 

 

 

 2 X W F R P H  % L D V                                                                                                     
 

 

                   
       

 

 

                                

                                  

 

   

   

             

 % 5 1  & D X V D O                                                                                                         
 % 7 $ (                                                                                                         
 & R Q I L U P D W L R Q  % L D V                                                                                                         
 & R Q M X Q F W L R Q  ) D O O D F \                                           

                                         

 

 & R Y D U L D W L R Q  ' H W H F W L R Q       

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 ' H Q R P L Q D W R U  1 H J O H F W       

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

   

   

 ) U D P L Q J  ( I I H F W                                                                                                        
 3 U R E D E L O L W \  0 D W F K L Q J             

 

 

 

 

 

Deepseek-R1 Distill
0.69
0.23
1.00
0.70
0.77
0.69
1.00
0.17
1.00
1.00
0.93
0.79
1.00
0.80
1.00
0.50
0.33
0.74

Qwen-32b
1.00
0.26
1.00
0.57
0.72
0.44
0.91
0.167
0.33
1.00
0.8625
0.71
0.50
0.41
1.00
1.00
0.67
0.68

 2 Y H U F R Q I L G H Q F H                                                                                                        
 5 7  ( W K L F D O                                                                                             
 5 7  ) L Q D Q F L D O                                                                                                        
 5 7  + H D O W K  6 D I H W \                                                                                                   
 5 7  5 H F U H D W L R Q D O                                                                                                      
 5 7  6 R F L D O                                                                                                        
 5 3  ( W K L F D O                                                                                                         
 5 3  ) L Q D Q F L D O                                                                                                         
 5 3  + H D O W K  6 D I H W \                                                                                                         
 5 3  5 H F U H D W L R Q D O                                                                                                        
 5 3  6 R F L D O                                                                                                      
 5 L V N  3 U R S H Q V L W \                                                                                               
 / R V V  $ Y H U V L R Q                                                       
 7 H P S R U D O  ' L V F R X Q W L Q J                                                                                                   
 ( Q G R Z P H Q W  ( I I H F W                                                                  
 * D P E O H U 
 V  ) D O O D F \                                                                                   
 0 H Q W D O  $ F F R X Q W L Q J                                             
 5 7 0                                            
 6 X Q N  & R V W  ) D O O D F \                                                                                                     
 2 Y H U D O O                                                                                                        

   

 * ' 0 6  6 S R Q W D Q H R X V                                                                                                 
 

Deepseek-V3
0.96
0.21
1.00
0.93
0.79
0.92
0.91
0.67
1.00
1.00
0.84
0.71
1.00
0.76
1.00
0.00
0.67
0.79

                   

 * ' 0 6  , Q W X L W L Y H                                                                                               

 % 5 1  6 W D W L V W L F D O                       

Deepseek-R1
0.74
0.20
1.00
0.87
0.79
0.98
1.00
0.50
1.00
1.00
0.80
0.72
1.00
0.74
1.00
0.00
0.33
0.75

                                  

 * ' 0 6  ' H S H Q G H Q W                                                                                                    

 $ Y D L O D E L O L W \  + H X U L V W L F            

GPT-4o
0.86
0.28
1.00
0.50
0.69
0.52
1.00
0.50
0.33
1.00
0.80
0.71
0.50
0.63
1.00
0.50
0.67
0.68

   

 * ' 0 6  5 D W L R Q D O                                 
 * ' 0 6  $ Y R L G D Q W                                

 

Human
0.60
0.37
0.21
0.64
0.84
0.82
0.62
0.56
0.19
0.44
0.72
0.72
0.63
0.75
0.80
0.59
0.33
0.58

   

 

 

 

   

 

   

 

 

 

 

 

 

 2 Y H U D O O                                                                                                        

 + X

 P D
 J S  Q
 W  
 R
 J S
 W
 G H
 H S  J S W    
 V H
 
 
 
 H N
  Y 
  
 W H [
 W H [  W  E L V  E D U G
 W  G  R Q 
 D
 W H [  Y L    
 W  G  Q F L 
 D
 F O D  Y L Q F    
 X G  L  
 H  L   
 Q
 T Z  V W D Q
 H
 W
 T  Q  
 R S  Z H Q   E
 H Q
  
 Z L ]  F K D W   E
 D U G    
 E
 Y L F  O P  
  E
 X
 O O D P Q D  
 D    E
 
 R D   
 V V W  E
 T Z     E
 Y L F  H Q  
 E
 X
 O O D  Q D  
 F K  P D   E
 D W J   
 O P  E
   
 E

   

   

   

   

   

   

 + X P
 J S W  D Q
   R
 G H H  J S J S W  
 S V H  W   
 H N   
 Y   
 W H
 W H [ W [ W  E L V R  E D U G
 
 Q
 G
 W H [ W  D Y L Q     
  G  F L
 F O D X D Y L Q F L    
 G H      
 T Z H L Q V W D Q
 Q   W
 R S H  T Z H Q    E
 
 Z L ]  Q F K D W    E
 D U G    E
 O
 P
 Y L F X    
 O O D P Q D    E
 D  E
 R D V      E
 V
 T Z  W    E
 Y L F X H Q   E
 O O  Q D 
 F K D D P D    E
 W J O P   E
   
 E

Figure 15: Rationality scores of LLMs (x) on different
aspects (y) in decision-making domain.

   

These efforts can lead to AI systems capable of
genuinely human-like understanding and interactions.

Figure 16: Rationality scores of LLMs (x) on different
aspects (y) in economics domain.

   
   
   
   
   
   

 + X P
 J S W  D Q
  
 J  R
 G H H  J S  S W  
 W
 S
 W H [  V H H N     
 W H [ W  W  E L V R   Y   
 Q
 
 W H [ W  G D Y L Q     
  G  F L 
 F O D X D Y L Q F L    
 G H     
 L
 T Z H Q V W D Q W
 Q  
 R S H  T Z H Q    E
 Q F K    E
 Z L ]  D W 
 D U G    E
 Y L F X  O P   
 E
 O O D P Q D   
 D  E
 R D V      E
 V W
 T Z     E
 Y L F X H Q   E
 O O  Q D  
 F K D D P D    E
 W J O P   E
   
 E

                                                                                   
 6 H F 3 U L $ X F
 % H D & R Q                                                                                                
 2 Q H 3 '                                                                                                  
 ) L Q 5 H S 3 '                                                                                                 
 2 Q H 3 *                                                                                    
 ) L Q 5 H S 3 *                                                                                               
 2 Y H U D O O                                                                                                  

Figure 17: Rationality scores of LLMs (x) on different
aspects (y) in game theory domain. (The missing values
in the first row is due to the lack of human experiment
data of the Second Price Auction game.)

28

 , Q I 5 H S 3 '                                                                                                
 ) L Q 5 H S % R 6                                                                                                   
 ) L Q 5 H S 6 +                                                                                                   
 ) L Q 5 H S 0 (                                                                                              

   
   
   
   
   

 + X P
 J S W  D Q
  
 J  R
 G H H  J S  S W  
 S V H  W   
 W H [  H N  
 W H [ W  W  E L V R   Y   
 W H [ W  G D Y L Q  Q    
  G  F L 
 F O D X D Y L Q F L    
 G H     
 L
 T Z H Q V W D Q W
 Q  
 T
 R S H  Z H Q    E
 Q F K    E
 Z L ]  D W 
 D U G    E
 Y L F X  O P   
 E
 O O D P Q D   
 D    E
 
 R D V   E
 V W
 T Z     E
 Y L F X H Q   E
 O O  Q D  
 F K D D P D    E
 W J O P   E
   
 E

 2 Y H U D O O                                                                                                 

   

(a) Cooperation and coordination
 0 0 / 8                                                                                                 
 0 $ 7 +

                                                                                                

 2 Y H U D O O                                                                                                    

   
   
   
   
   

 + X P
 J S W  D Q
  
 J  R
 G H H  J S  S W  
 W
 S
 W H [  V H H N     
 W H [ W  W  E L V R   Y   
 W H [ W  G D Y L Q  Q    
  G  F L 
 F O D X D Y L Q F L    
 G H     
 L
 T Z H Q V W D Q W
 Q  
 T
 Z
 R S H  H Q    E
 Q F K    E
 Z L ]  D W 
 D U G    E
 Y L F X  O P   
 E
 O O D P Q D   
 D    E
 R D V    E
 V W
 T Z     E
 Y L F X H Q   E
 O O  Q D  
 F K D D P D    E
 W J O P   E
   
 E

   

(b) Wisdom of crowds - MMLU and MATH

Figure 18: Rationality scores of LLMs (x) on different
aspects (y) in collective rationality domain.

29
