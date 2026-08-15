---
title: "Responsible AI in Open Ecosystems: Reconciling Innovation with Risk Assessment and Disclosure"
person: "nick-vincent"
section: "by"
type: "journal-article"
year: 2024
date: "2024-09-27"
venue: "AAAI 2025 Workshop on AIGOV, 2025"
authors: "Mahasweta Chakraborti, Bert Joseph Prestoza, Nicholas Vincent, Vladimir Filkov, Seth Frey"
source_url: "https://arxiv.org/abs/2409.19104"
retrieved: "2026-08-13"
content: "full-text"
notes: "OpenAlex W4403810455; CV ref [W12]; Full text from the arXiv HTML rendering of the preprint (https://arxiv.org/html/2409.19104v1)."
---

# Responsible AI in Open Ecosystems: Reconciling Innovation with Risk Assessment and Disclosure

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

- Abstract

- 1 Introduction

- 2 Related Work

- 2.1 Ethics of AI, Tech Regulation, and Open Development

- 2.2 Evaluation Practices and Responsible AI

- 2.3 Empirical studies of open source and open weight AI

- 3 Methods

- 3.1 Research Questions

- 3.1.1 RQ1: How is documentation of risks, limits, and biases among projects related to model evaluation?

- 3.1.2 RQ2: How is risk documentation of projects related to their accuracy?

- 3.2 Data

- 4 Results

- 4.1 Exploratory Analysis

- 4.2 Multivariate Hypothesis Testing for RQ1 and RQ2

- 5 Discussion

- 5.1 Recommendations

- 5.2 Limitations

- 5.3 Ethics Statement

- 6 Conclusion

- References

- A Benchmarks in Open LLM Leaderboard

- B Service-ready Features and Identifiers

License: CC BY-NC-ND 4.0

arXiv:2409.19104v1 [cs.HC] 27 Sep 2024

## Responsible AI in Open Ecosystems: Reconciling Innovation with Risk Assessment and Disclosure

Mahasweta Chakraborti

Affiliation: University of California, Davis, CA

Email: mchakraborti@ucdavis.edu

Bert Joseph Prestoza

Affiliation: University of California, Davis, CA

Email: bertjosephprestoza@gmail.com

Nicholas Vincent

Affiliation: Simon Fraser University, British Columbia

Email: nicholas_vincent@sfu.ca

Seth Frey

Affiliation: University of California, Davis, CA

Email: sethfrey@ucdavis.edu

####### Abstract

The rapid scaling of AI has spurred a growing emphasis on ethical considerations in both development and practice. This has led to the formulation of increasingly sophisticated model auditing and reporting requirements, as well as governance frameworks to mitigate potential risks to individuals and society. At this critical juncture, we review the practical challenges of promoting responsible AI and transparency in informal sectors like OSS that support vital infrastructure and see widespread use. We focus on how model performance evaluation may inform or inhibit probing of model limitations, biases, and other risks. Our controlled analysis of 7903 Hugging Face projects found that risk documentation is strongly associated with evaluation practices. Yet, submissions (N=789) from the platform’s most popular competitive leaderboard showed less accountability among high performers. Our findings can inform AI providers and legal scholars in designing interventions and policies that preserve open-source innovation while incentivizing ethical uptake.

### 1 Introduction

In recent years, we have witnessed the adoption of artificial intelligence (AI) across various individual, collective, and public enterprises, including education, business, and research. This widespread implementation has been argued to boost productivity, enhance manufacturing, accelerate development, and facilitate the provisioning of critical services and infrastructure at unprecedented levels and reach (see e.g. Chapter 4 of the AI Index Report for an overview of specific claims along these lines [90]). The scalability offered by these technologies may revolutionize numerous industries and promote further investment in AI innovation for improved service delivery across diverse domains.

Nascent technologies often face skepticism and scrutiny before earning public trust [54]. Therefore, potential risks in AI need to be recognized and addressed at every stage of development, such as representative quality of training data [66], algorithmic designs [48], and learning objectives [117]. AI artifacts are also highly prone to inappropriate uses [39, 91]. As AI’s market impact and reach in people’s lives continues to expand, there have also been corresponding calls for ethical training and regulatory oversight for providers and deployers.

Model evaluation is a standard component of the AI development and deployment cycle. In its most common form, evaluation involves testing models on held-out datasets to understand how well a model has learned. Such benchmarking is essential for assessing novelty against the state-of-the-art, deciding whether the model is suitable for widespread use, improving training, and informing design choices for further innovation. Today, competitive benchmarking against other models is a popular form of evaluation, and high performers garner legitimacy from users and investors, enjoy market visibility, and even steer development and consumption [43, 50, 103].

With rising stakes, responsible developers are increasingly expected to use evaluations not only to assess model capabilities but also to recognize its limitations. Holistic evaluation goes beyond simply reporting gross accuracy and encourages probing edge cases, measuring biases in predictions for specific domains and vulnerable subpopulations, and cautions against failure modes [82, 27]. Depending upon the criticality of the application (e.g., medical diagnostics or defense), evaluation may demand nuanced expertise, where the developer needs to invest in understanding methodologies, conducting different tests, and selecting appropriate metrics. Empirical testing can provide developers, managers, and investors with necessary information regarding broader applicability and sociotechnical impact, thereby mitigating liability and harm. Importantly, these assessments should be documented and reported in an interpretable, accessible form that can empower experts and ordinary users to make informed choices over model use.

Our work explores current evaluation practices and developer accountability in informal sectors. Open-source AI is a rising player with a considerable market presence and increasing corporate adoption. Prized for fast-track innovation through crowd-sourced contributions, OSS projects have garnered significant attention from researchers in online communities and collaborative work. Yet open-source ecosystems face unique challenges in actuating responsible development; simply put, the governance and power structures tend to be more decentralized than in corporations, universities, or other institutions that might develop AI systems. Fostering accountability and standardization would necessitate collaborative monitoring of risk documentation, inadequate evaluations or malpractice [55, 50, 16], and downstream misuse. Their largely informal, decentralized organization might complicate agreement over testing requirements, documentation standards, and monitoring of their uptake. Holistic evaluations [82] may also bring additional costs and effort for small communities. Lastly, communities may be apprehensive about retaining their user base with stringent risk disclosure requirements.

We conduct an in-depth dataset documentation study of metadata on Hugging Face (HF), one of the largest open-source AI hosting platforms. In particular, we focus on collecting data and conducting quantitative analyses on the evaluation and risk documentation practices among projects and model the relationship between the two. Our contributions include the following:

- •

We thoroughly review documentation practices (Model cards), project organization, information management, compliance checks, and other platform support on Hugging Face.

- •

We explore the evolution of open source AI development through the scaling of model training, applications, contribution rates, model re-use patterns, and documentation practices among models across different organizational entities

- •

Among usable, service-ready projects, around 15.9% and 2.2% models contained evaluation and risk-related documentation from the developer.

- •

In a quantitative analysis of 7903 models with controls, we found a strong, positive association between the practices of model evaluation and risk documentation practices

- •

Among 789 projects participating in HF’s Open LLM leaderboard [18], higher-performing models were found to be less likely to provide documentation on risks and limitations.

### 2 Related Work

Here, we discuss background on Open Source AI and key areas of research that motivated our dataset documentation effort and accompanying quantitative study.

#### 2.1 Ethics of AI, Tech Regulation, and Open Development

Fostering and standardizing ethical development is a nuanced challenge in open source, which, contrary to regulated for-profits and commercial entities, is historically informal and free-forming [21, 42, 38]. Developer motivations, ranging from altruism to popularity, may lead to varying governance structures [81, 35, 120]. Open sourcing has led to remarkable progress in science and technology, and notable AI projects started out in the same to inspire and support collective innovation. At the same time, there have been multiple instances of biased or improperly curated training data and artifacts that can compromise regular applications [23, 22, 79]. Further, open source projects have also been appropriated for nefarious uses [4, 2, 89, 93]. We review some milestones in ethical discussions and regulatory approaches relevant to open-source AI.

With the growing potential of AI uses and misuse, researchers and ethicists came together early on to specify and advocate documentation guidelines for every link in the AI development pipeline. Model cards, [94, 41, 13], data sheets [57, 19], and other factsheets are crucial sociotechnical governance tools that keep stakeholders informed and define the scope of AI consumer applications, ultimately contributing to more transparent and accountable development practices. Responsible documentation outlines permissible use cases (possibly extending to licensing [39]), cautioning against out-of-scope applications, and discloses other anticipated risks and practical challenges. Projects generally explain any anticipated limitations in implementing the AI solution, such as predictive biases across ethnicity or gender-profession skew in generated outputs, robustness to adversarial attacks, reliability across use cases (e.g., whether a medical diagnostic system under diagnoses rare conditions), cautioning corner cases where a model is unsuitable for use.

Consensus over development standards and reporting requirements are evolving with expanding uses of AI, leading to attempts at governance systems [13, 54, 98, 72]. Legislative measures towards AI accountability also deliberated the drawbacks of strict regulation. Despite arguments in favor and against [77], open source is primarily exempted by the EU AI act, one of the first major steps towards formalized AI governance [51]. Yet, given product objectives and target uses, other vulnerabilities can arise from development, such as biased training data [66] (content, source, representative quality, etc.), limited robustness or generalizability [80] (particularly for high-stake uses), and other associated design choices. In Recital 89, the act strongly endorses documentation practices such as model cards and data sheets for open source developers ”to accelerate information sharing along the AI value chain, promoting trustworthy AI systems in the Union”. Therefore, open source developers must still strive towards responsible practices, address the concerns of potential stakeholders through information sharing, and institute contingencies to address risks and harms.

Given the contemporary state of affairs, we seek a closer understanding of open source aspirations to inform the design of guardrails that foster mindfulness and social responsibility while also preserving reasonable developer freedom.

#### 2.2 Evaluation Practices and Responsible AI

Evaluation and testing have been historically integral in informing innovation and consumer use of emergent technologies. As we work on making AI more capable, there are benefits to be seen from striving towards a 99% accurate solution from a 98% accurate solution. These gross accuracy metrics indeed serve to inform design decisions. However, model valuation through accuracy is only one of several aspects that concern AI use and governance [95, 53]. We review current approaches to AI evaluation, which inform how we analyze our collected data and interpret our findings.

A bid for greater accuracy through standardization led to the rise of evaluation benchmarks. As benchmarks became more widely adopted, they evolved into popular, competitive leaderboards [115, 116, 105, 110, 26, 45, 78]. These initiatives draw attention and participation, and have been instrumental in the rapid progress of AI by serving as a recognition-based incentive for continuous, incremental innovation. However, strides towards predictive efficiency have also culminated in a uni-dimensional emphasis on metric-races and ranking.

Over time, several researchers have observed practical limitations with bench-marking and leaderboards, including errors and other vulnerabilities that compromise their validity or even obfuscate limitations and risks [43, 59, 31, 108]. Despite their usefulness as a general estimation of model capabilities, held-out test accuracy from a benchmark is not a comprehensive measure of generalizability, adversarial robustness or risk tolerance. Therefore, the error rate on a benchmark may not always reflect the population error rate [67, 122, 50, 43, 14, 25] Leaderboards are often dominated by highly over-parameterized, complex, and energy-inefficient models, sometimes overfitted to benchmarks [50, 62, 14, 43, 25]. Because of the visibility enjoyed by top performing developers, rampant attempts have been observed to game leaderboards, such as multiple submissions and tweaks, to maximize rank [62]. Benchmarks also generally lack transparency and fail to account for model attributes crucial to design and informing use, such as compactness, fairness, inference speed, and energy footprint, to name a few. [50, 103]. Moreover, as rankings are generally based on models’ aggregate performance (e.g., accuracy/F1, etc.) over a collection of tasks and datasets, submissions often conceal racial and gender biases [29, 88, 107, 24]. Researchers have also noted selective pressures arising from benchmarking with unintended consequences for innovation, such as the promotion of certain architectures and algorithms over others [43, 113].

With increasing recognition of the inadequacy of current evaluation practices, scholarship in AI safety has seen a notable push towards holistic approaches with expanding definitions, objectives and approaches beyond simply predictive accuracy [82, 28, 27, 92]. These include robustness against malicious or adversarial inputs [97], explainability of the model’s decision-making and intermediate processes [84, 49], generalizability on out-of-sample data [17], and granular testing across demographic subgroups for biased behavior. There have also been notable strides in designing evaluations to measure model fairness [123, 96, 104].

With the legitimacy popular leaderboards enjoy [103], high performance may easily lead developers and users to assume the generalizability of their models and undermine the need for additional efforts to stress-test for runtime risks. This is especially dangerous and requires a reassessment of benchmarking as it is. Opportunistic overfitting can be mitigated by promoting dynamic benchmarks [97, 43, 75, 58], that are constantly updated to accommodate temporal/distributional drifts and emerging domains, newer tasks, and capabilities. Dehghani et al. and Hardt et al. further guide benchmark design to ensure judicious assessment while mitigating opportunistic submissions [43, 62, 25]. Other proposed measures include confidentiality of test/hold out sets and mitigation of data leakage [85, 44] and contaminated models [47, 16, 87]. Multi-metric leaderboards, such as SNLI, which displays model sizes alongside accuracy [30, 61], can guide developers and users towards efficient and sustainable choices.

#### 2.3 Empirical studies of open source and open weight AI

With rapid interest and growth of AI in open-source contributions, researchers have been exploring the potential of data-driven research and feasibility of repository mining on AI-centric development platforms and services [68, 70, 11, 10]. Software engineers have been particularly interested in modularity and artifact reuse from pre-trained model repositories or "PTMs" [69, 60, 112], and accompanying security risks and vulnerabilities [71, 74]. Several studies have explored model documentation [102, 60, 119]. Gong et al. focus on usage documentation across multiple platforms [60], while Liang et al. analyzed different sections across Hugging Face model cards and how comprehensive documentation may improve model popularity [83]. Castano et al. studied carbon footprint reporting [34]. Hugging Face’s internal study found that among all model card components, respondents found the risks sections the longest and most challenging to complete [101]. Osborne analyzed licensing and collaboration patterns, finding positively skewered patterns in contribution, engagement, and model usage [99].

### 3 Methods

#### 3.1 Research Questions

After careful perusal of repositories
spanned by our review (Sec. 2.3), we base our exploration and empirical analysis on Hugging Face, the most popular of contemporary PTM repositories [60] with over 0.7 mil submissions at the time of the study. Hugging Face is increasingly appealing to AI developers, even over long-standing platforms like GitHub [11, 10]. This is especially true as projects scale, requiring greater storage and computing requirements. Hugging Face is a PaaS exclusively for AI/ML development, offering tooling, storage for large artifacts, and remote servers for training, testing, and hosting apps, all under a single roof. While some contemporary model directories provide official base model releases for specific libraries and frameworks (e.g., Nvidia CUDA, Tensorflow, or Pytorch model directories) or vetted research projects (e.g., ModelZoo), HF spans models from these categories alongside vast numbers of amateur submissions, community contributions as well as public and private institutions. Therefore, it provides a large enough representative sample to observe development and model adaptation practices as is and gauge developer ethics in the wild.

##### 3.1.1 RQ1: How is documentation of risks, limits, and biases among projects related to model evaluation?

Evaluation and Risks are core components of standard model cards. Hugging Face’s guided annotation template [52] encourages developers to select appropriate testing procedures and benchmarks to evaluate model performance and document the results. It also recommends that such evaluation should involve testing for potential usage limitations, vulnerabilities, and biases in the model to aid sociotechnical experts in comprehensive risk documentation.
Therefore, proper motivation, understanding, and proficiency in evaluation are expected to inculcate cognizance of responsible development practices. We frame the research question as follows:

R​i​s​k​s​a​n​d​B​i​a​s​e​s​D​o​c​u​m​e​n​t​e​d∼P​r​o​j​e​c​t​C​o​v​a​r​i​a​t​e​s+E​v​a​l​u​a​t​i​o​n​R​e​p​o​r​t​e​dRisks~and~Biases~Documented\sim Project~Covariates+Evaluation~Reported

##### 3.1.2 RQ2: How is risk documentation of projects related to their accuracy?

We may expect developers of highly accurate models to be more proficient and well-rounded and, therefore, likelier to be able to also thoroughly probe and document risks, biases, and other limitations. Yet, we explain (see Sec. 2.2) how current trends may undermine the validity of benchmarking or even downplay the need for holistic evaluations above and beyond accuracy. RQ2 can be modeled as follows:

R​i​s​k​s​a​n​d​B​i​a​s​e​s​D​o​c​u​m​e​n​t​e​d∼P​r​o​j​e​c​t​C​o​v​a​r​i​a​t​e​s+M​o​d​e​l​A​c​c​u​r​a​c​yRisks~and~Biases~Documented\sim Project~Covariates+Model~Accuracy

We pursue RQ2 on submissions to Hugging Face’s first edition of the Open LLM leaderboard, which ran from May 2023 to June 2024. It drew remarkable levels of participation across different project types. Importantly, it observed rigorous community monitoring for contamination [16] and other evaluation malpractices, as well as reproducibility checks to substantiate self-reported performances, thus strengthening the validity of measurements and analysis.

#### 3.2 Data

Here, we describe some of the project-level covariates we consider in our empirical data analysis and explain their inclusion, i.e., how they motivate documentation habits and accountability among projects. Table. 1 lists details of our multi-source data collection.

Our review of prior studies and the HF Hub codebase and documentation revealed how the information we sought is distributed across the project landing page, repository and its metadata, index tags, and finally, the model card markdown files. HF Hub uses semantic tags to index models and facilitate search, which are often auto-detected or parsed from the YML component of model cards. To access repository records or model tags, we use the Hugging Face API. We focus our study on 700,072 repositories uploaded to Hugging Face as of 06/15/2024. We only include completely open repositories by filtering out ’gated’ repositories whose file contents or commit history are private.

Project Aspect |

Variables
|

Description
|
Type |

Source
|

Model Features |

Model Size
|

Number of Model Parameters
|
Numeric |

Model Page
|

Training Resources
|

Data samples used to
train model
|
Numeric |

Training Data metadata (HF API)
|

|

Modalities
|

Modalities served e.g. Computer Vision
|
Categorical |

Model Card metadata (HF API)
|

|

Domain
|

Specific fields of application model is trained for e.g. code analysis, medical applications
|
Categorical |

Training Data metadata (HF API)
|

Model Developer |

Team Size
|

Community Strength
|
Numeric |

Linked Developer Profile
|

Total Models
|

Development experience of contributor
|
Numeric |

Linked Developer Profile
|

|

Entity Type
|

If contributor is a for or non profit, research projects, etc
|
Categorical |

Linked Developer Profile
|

User Engagement |

Likes
|

Total Likes from HF Users
|
Numeric |

Model Page
|

Deployed Apps
|

Number of apps on HF using model
|
Numeric |

Model Page
|

Developer Activity |

Age
|

Repository Age in days
|
Numeric |

Git History (HF API)
|

Total Commits
|

Development activity on repository
|
Numeric |

Git History (HF API)
|

|

Pull Requests
|

Feature Additions and Contributions received
|
Numeric |

Git History (HF API)
|

|

Discussions
|

Community feedback and engagement with repo
|
Numeric |

Git History (HF API)
|

Compliance |

Performance Evaluation
|

Developer’s evaluation objectives, protocols selected and results
|
Categorical |

HF Model Card scanner and API
|

(Documentation Available) |

Risks, Limitations and Biases
|

Foreseeable harms, vulnerabilities and limitations
|
Categorical |

HF Model Card scanner
|

|

C​O2{CO_{2}} Emissions
|

Model training footprint on environment
|
Categorical |

HF Model Card scanner and API
|

Competitive |

Accuracy
|

Best aggregate results reported on the Open LLM Leaderboard
|
Numeric |

Leaderboard Archives
|

Benchmarking |

Attempts
|

Number of leaderboard submissions for a single model
|
Numeric |

Leaderboard Archives
|

|

Precision
|

Precision used in testing e.g. 8 Bit, BF16 etc
|
Categorical |

Leaderboard Archives
|

Table 1: Data collection across Hugging Face: Variables with description.

Project use, Developer activity, and Community engagement: Git-based information, such as repository age and commit activity, were available for all open repositories, while usage/popularity metrics were available on every model’s landing page. Controlling for time lets us account for documentation practices as a function of evolving development standards, conception of ethical practices, and regulatory oversight. We measure repository age as the time between project initiation (first commit) and data collection. For developer and community engagement around a model, we measure the total number of commits, pull requests, and all other discussions (including issues) on each repo. Developers seeking greater exposure and usage of their projects may practice better documentation [60]. Several prior studies used API calls or downloads to measure model popularity. At the time of the study, Hugging Face only displayed model download stats for the current month. We use total model likes from users as a cumulative measure of popularity. Unlike its counterparts like GitHub, Hugging Face does not offer an option to fork repositories directly but allows porting to build applications called spaces. We use the total number of spaces spinning off a repository to measure model circulation.

Model application and usability: Since AI auditing and regulation through documentation are particularly applicable for service-ready models and AI applications [13, 77], we screen out incomplete projects and dumps and test our hypothesis on especially well integrated, ready to use projects. Based on a review of HF documentation and semantic categories listed in the API, we identify service-ready models through at least one of the following:

- •

Model cards filled with detailed instructions, examples, and use cases: Detected using HF’s Model card scanner

- •

Verifiable integration into the HF ecosystem (can be used for training, tuning, or inference) : Integrated models are tagged with training or deployment options within the HF ecosystem, such as "endpoints_compatible", "autotrain_compatible" or have widgets enabled on their webpage for users to explore and interact with the model.

- •

Model page carries a "Use this model" feature for deployment through a developer-provided space or supported third-party platforms.

All in all, 456,545 projects out of 700,072 repositories fulfilled this criteria.

HF tracks information on the modalities and tasks performed in index tags for most service-ready models. These span six major types: Natural Language Processing, Computer Vision, Audio, Reinforcement Learning, Tabular Data, and Multimodal. Note that a particular AI application may qualify under multiple categories, e.g., a prompt-driven image generator may be placed under Natural Language Processing (interpreting human queries), Computer Vision (image generation), Multimodal (operates across multiple modalities, i.e., image and text), and Reinforcement Learning (learning from human feedback).

Developer attributes: We scrape the model landing pages and linked developer profiles for information vital for a controlled study. Hugging Face supports single-user accounts or team accounts called ”organizations." The growing importance and evolving sophistication of documentation benefits from multiple contributors and distributed responsibilities. Hugging Face’s official documentation designates model auditing responsibilities across well-defined roles, such as the manager, the sociotechnical expert, and the developer. Further, information management may also depend on the type of developer or provider. In particular, commercial entities anticipating regulatory purview may ideally conduct more thorough risk assessments to avert potential liabilities from failures and misuse. Team pages contain community sizes and the type of entity owning the account, such as a company releasing ’freemium’ models, an educational institution (university or classroom), or a non-profit. For all developers, we also include the total number of models they contributed as a measure of experience.

Model Scale: In the context of AI, scaling refers to enhancing learnability and performance by developing highly parameterized, data-intensive models. Between 2017 and 2022, parameterization in Google’s language models grew from 110 million for BERT (base) [46] to 540 Billion for PaLM [5]. While promising enhanced capabilities, Large Foundation ("Frontier") models have also seen increasing attention from ethicists and policy oversight bodies due to foreseeable market impact and consumer stakes [63, 20]. Recent proposals, particularly SB 1047 in California, explore graded requirements by model value. To inform ethical practice and test hypotheses around compliance behavior, it is necessary to account for emerging legal and social motivations from model valuation that may also influence documentation rigor.

Scaling solutions demand more storage and computing facilities. Comprehensive details on training and other expenses can often be challenging to obtain, be it from proprietary closed-source or informal settings like open-source. With providers seeking to scale models towards enhanced capabilities and higher performance, compute (hardware needed, floating point operations (FLOPs), etc.) comprises a significant share of development investments and directly depends on the model. Kaplan et al. experimentally validated a power law approximating the relationship between model performance and compute, model size (parameters), and training data size [73]. For a chosen level of performance, the compute budget follows from the requisite training data volume and model size. Recent work has validated variations of the law across other architectures, tasks, and learning paradigms [65, 12, 15]. These rules of thumb are widespread today and instrumental in neural scaling. We control for model value through both size (number of parameters) and training data volume (number of samples).

Diverse model sizes, non-uniform file nomenclature, and frameworks complicate the automated loading and parsing of model details such as size. Hugging Face does not track the model sizes of all repositories [1]. Safetensors [7] and GGUF [3] are two popular tensor formats promoted and tracked by HF. Models and training checkpoints correctly stored in these formats display verified details on their pages, including the number of parameters [8]. We obtained the parameter count for 140,783 models.

Developers often withhold training data details [66]. Reasons include but are not limited to, IP (particularly for proprietary freemium models) and licensing terms. Moreover, data provenance for transparency and explainability may be at odds with security by exposing the model to poisoning, privacy breaches, and other adversarial attacks [80, p. 2]. We only consider models with openly released training data and associated details. This allows controlled hypothesis testing between evaluation and risk documentation trends while adjusting for factors across the development cycle.

Model index tags contain links to training data provided by the developer, and Hugging Face provides size and other structured information on nearly all datasets it hosts. After selecting models with all their training data available on HF and screening out models directed to invalid dataset repositories, we obtained training data sizes for 17,260 models. Overall, 7093 models had complete model and training data size information.

Model Knowledge Domain: Knowledge Domain, in the context of ML, refers to the specific cases and tasks a model has learned to perform. Models are generally trained with data samples from their target domain, and high-stakes/critical applications may command greater developer accountability. E.g., minor diagnostic errors can significantly increase liabilities and derail the applicability of AI in medicine. HF tracks nine popular training data domains, including medical, finance, code generation, etc.

Compliance Information:

Developers chose appropriate tests and metrics to quantify model performance based on development objectives and target use. Our first hypothesis testing requires predicting models’ risk and limitations documentation against the rate at which they evaluate model performance. Model cards on HF contain several distinct sections for technicalities such as data provenance, development specifications, performance, legal/copyright aspects, and social implications of the model’s use. Based on the Annotation guide11
1

https://gitHub.com/huggingface/huggingface_Hub/blob/main/src/huggingface_Hub/templates/modelcard_template.md, the Evaluation section requires the model developer to specify objectives, protocols, and performance results. Ideally, these should be selected to ensure domain accuracy, demographic fairness i.e. performance specifically tested across relevant user groups, and foreseeable error contexts specific to the model’s use cases. Working with the developer, the sociotechnical expert generally fills out portions titled "Bias, Risks, and Limitations". They are expected to interpret all aspects of the development, from data to evaluation results and intended uses, to explain foreseeable harms and misunderstandings (including but not limited to: the model’s propensity towards discrimination and stereotyping, predictive skew across demographic subgroups, robustness, outlining and forbidding use cases beyond development goals etc) and other limitations. They may optionally include warnings and mitigation strategies.

Model cards are the default face of a model’s landing page, rendered from the repository’s ’README.md’ file11
1

https://gitHub.com/huggingface/huggingface_Hub/blob/main/src/huggingface_Hub/templates/modelcard_template.md. This file contains text and a machine-parseable YAML header. A repository lacking a "README.md" model card will create a blank landing page with no information. We measure such projects as non-compliant, lacking any documentation or evaluation. HF’s society and ethics team recently developed a regulatory tool to scan the text portions to check if certain sections have been filled out. Per the official, Annotated Guideline11
1

https://gitHub.com/huggingface/huggingface_Hub/blob/main/src/huggingface_Hub/templates/modelcard_template.md, evaluation details and carbon emissions may be provided in the header or the text. Risk information is generally more descriptive and only reported in the main model card text.

Using the text scanner and API, we analyze all model cards to detect whether evaluations or risk assessments have been included. Around 21.6% of all service-ready models contained risk assessment headings in the README.md. Some integrated libraries, e.g. Autotrain22
2

https://huggingface.co/autotrain, initialize default model cards based off the HF template. These often only contain text boilerplates for empty sections, such as "More information needed"11
1

https://gitHub.com/huggingface/huggingface_Hub/blob/main/src/huggingface_Hub/templates/modelcard_template.md. For measurement integrity, we further filter out model cards with unfilled/auto-generated sections as non-compliant along that particular section.

Evaluating C​O2{CO_{2}} footprint is the other crucial sociotechnical component of model cards. It follows closely on the heels of the social impact of AI and concerns the broader impacts of the development cycle on the environment [76, 111]. Conscientious, responsible developers may be motivated to report the social impact of the model comprehensively. Evaluation and disclosure of model C​O2{CO_{2}} emissions is included as a dichotomous control. We use the API for headers and string matching to detect valid C​O2{CO_{2}} emission entries under designated sections in the card text.

Competitive Benchmarking:

The second research question tests for any significant association between model performance and documentation of risks and use limits. Over time, different leaderboards have been created to test different AI applications (see 2.2). Leaderboard positions are highly vied, with high performers enjoying considerable visibility and popularity. The Open LLM Leaderboard is the most prominent and active leaderboard on Hugging Face, with its first edition running from May 2023 to June 2024. It was mainly geared towards language technologies and ranked submissions on aggregate performance across six extremely popular benchmarks [37, 109, 36, 121, 64, 86]. With 7173 unique, complete submissions, the leaderboard has served to encourage performance validation while the community also consults it for model selection.

The choice of the open LLM leaderboard was motivated by its prominence, upkeep, thoroughness, and monitoring. Notable leaderboard hosting services like Papers with Code [40] are often static and primarily cover academic and research communities. HF teams continuously test submissions for authenticity and reproducibility. Unlike other community leaderboards like Kaggle, HF encourages users to proactively identify and report malpractice, such as contaminated models [87]. This serves as a convenient sandbox for our research questions.

We use leaderboard archives33
3

https://huggingface.co/datasets/open-llm-leaderboard-old/results to collect details on participating models. Submissions were ranked by their aggregate performance across six popular benchmarks. Details on the benchmarks used by the leaderboard and their metrics are provided in the appendix. Developers often submit multiple entries to report incremental increases in accuracy. While this ostensibly reflects innovation, resubmissions are often overfitted to perform [62, 50] and may indicate the competitiveness of the participant rather than sustainable development. For our analysis, we only consider the best performance for each model, controlling for the number of attempts and the precision of the model version tested. We additionally control for evaluation malpractice through flagged models.

Developers or platform moderators often assign ’not-for-all-audience’44
4

https://huggingface.co/content-guidelines and ’NSFW’ tags to certain projects inappropriate for general use, such as ones trained on or meant for sexual content generation. By violating the fundamental premise of ethical AI, they are expected to show limited compliance. High-risk applications were incorporated as a categorical control in our analysis.

### 4 Results

#### 4.1 Exploratory Analysis

Before answering our quantitative RQs (covered in the next section), we begin with a preliminary analysis to understand general trends within our collected data.

Hugging Face initially gained recognition through an open-source implementation [118] of the seminal transformer architecture [114], primarily targeted toward NLP development. The first version of the Hugging Face client library was released in late December 202055
5

https://pypi.org/project/huggingface-Hub/ to facilitate remote, collaborative development and artifact storage, reuse, and sharing. By the end of 2020, the collective comprised 4,634 projects and 672 unique contributors. The platform has since expanded support to over 20 ML libraries, AI frameworks, and applications. At the time of data collection on 06/15/2024, the HF Hub held 700,072 projects across 178,030 developers. Fig. 1 charts the growth in repositories since the release of the Hub client.

Figure 1: (a) Growth of the number of projects on HF Hub after the release of their client library in December 2020. (b) We also map development trends as the number of projects by modality among service-ready models uploaded since 2021. Natural Language Processing is consistently the most sought-after AI/ML application, closely followed by Reinforcement Learning, Computer Vision, and Audio. The trend over time (mean with 95% confidence interval) in (c) model sizes and (d) training data requirements among 140,007 and 17,251 projects uploaded since 2021 showed a discernible increase in development scale.

The democratization of innovation afforded by open sourcing, coupled with rapid progress in AI, has paved the way for training libraries and solutions to cater to all sizes and requirements. Hugging Face and its integrated libraries provide off-the-shelf options from industrial-scale foundation models to easy, low-compute customization. Besides team collaboration, the empowerment of individual developers was evident in a visual exploration of contribution patterns across the service-ready projects (see Fig. 2). Around 87.57% of all service-ready projects were contributed by individual accounts, and a staggering 86.34% were built without receiving any collaborative input through pull requests. We also find that only 5.46% of all projects see any downstream use in apps.

Figure 2: Contribution trends among all 456,545 service-ready projects. Most contributions are individual projects rather than collaborative, with 87.57% having 0 pull requests and 86.34% uploaded by single-member accounts. Around 5.46% models have been deployed in applications (spaces).

The Hub indexes most service-ready models by semantic categories that are system-generated or developer-annotated. Examining models by modality and application category tags, we find Natural Language Processing still accounts for most applications, followed by Reinforcement Learning, Computer Vision, and Audio applications. The release of large GPTs [9, 33] and diffusion models [106] marked watershed moments for both language and image technologies. They were soon followed by a remarkable drive to build viable, open-access versions of commercial AI solutions. The dominance of NLP may also stem from Hugging Face’s historic focus on NLP and more mature platform support. Computer Vision applications exceeded Audio projects by 2023. Reinforcement Learning sees a steady uptick between 2021-2023, parallel to the expansion of feedback-driven learning from simulating games to refining language applications [100]. All in all, these visualizations confirm general trends in AI and merit future exploration into the transfusion of innovation milestones in wider open-source practice.

We obtained verifiable model sizes (in parameters) and training data samples for 140,783 and 17,260 of the service-ready projects, respectively. Examining the temporal evolution of model sizes and training data requirements among post-2020 uploads in these subsets (Fig. 1), we observe a clear upward trajectory in development scale, favoring more sophisticated and data-intensive models.

An overall analysis of model card reporting among 456,545 service-ready models found generally low model card compliance and even differences between different sections (see Fig. 3). Evaluations were most documented (15.9%), while risks and limitations were found among 2.2%. Finally, C​O2{CO_{2}} emissions saw the least reporting at 0.7%. About 0.7% contained both evaluations and limitations. Only around 0.1% of the models complete all three sections. These findings broadly agree with trends seen in prior work on AI documentation [83, 119] and call for greater attention to documentation and comprehensiveness across all reporting requirements.

Figure 3: Documentation Rates between of Model Card components. Among 456,545 usable models, evaluations were most documented (15.9%), while risks and limitations were found among 2.2%. Finally, C​O2{CO_{2}} emissions saw the least reporting at 0.7%. About 0.7% contained both evaluations and limitations. Only around 0.1% of the models complete all three sections.

Analyzing projects by team (’organization’) types in Fig. 4 a. we find company contributions showing the highest growth rate between 2022 and 2024. By 2024, company created models exceed traditional OSS participants such as academia and non-profits. Meanwhile Fig 4 b. shows noticeable differences in documentation across different developer/provider types. Non-profits lead among organizations in model evaluation and documentation. Yet, on the whole, non-profits, companies, and universities document risks more than the population average.

Figure 4: a. We find company contributions showing the highest growth rate between 2022 and 2024., surpassing universities and non-profits b. Noticeable differences exist in documentation across different developer/provider types. Non-profits lead among organizations in providing model evaluations. On the whole, non-profits, companies, and universities document risks more than the population average.

#### 4.2 Multivariate Hypothesis Testing for RQ1 and RQ2

Here, we address our core RQs introduced above. For both RQs, we consider models whose information on significant covariates was released on the HF Hub and available in structured, parseable form. Based on the literature review, trends in AI safety research, and our exploratory analysis, we consider five main categories of covariates: project scale, modality, domain, popularity and usage, and developer engagement. This left us with 7093 samples for RQ1, a subset of the entire HF directory representing service-ready, highly transparent models where data provenance and model specifics (number of parameters) are available through safe, robust file management. Around 23.19%, 7.86% and 2.04% had provided evaluation, risk assessments, and C​O2{CO_{2}} emission data, respectively.
We frame our RQs as binary prediction modeling to determine if risk assessment and social impact accountability are significantly associated with 1. rates of performance evaluation and disclosure and 2. absolute mean performance on a set of very popular benchmarks used in the Open LLM Leaderboard. For both cases, we model the likelihood of risk assessment in model cards using binomial logit models, where evaluation practices (RQ1) or performance (RQ2) are the main regressors of interest, adjusting for crucial project-level covariates. We set the significance level of our analysis at 0.01.

RQ2 is based on a subset of RQ1, which participates in the open LLM leaderboard and only comprises NLP models. In this particular subset of models with 100% evaluation reporting (through benchmark participation), we again find higher than average risk (8.7%) and carbon emission (1.5%) reporting, around 7173 models completed all six benchmarks. We test RQ2 on a smaller subset of 789 of these models for which all significant covariates were available. Some generalist models spanned multiple domains, such as medicine and legal/financial applications, leading to the aliasing. These knowledge domains were merged into a single category and renamed “multi-domain.”

Numeric covariates were log-transformed (base 10) for skew correction and comparison along the scale of different projects, followed by standardization. We check for multicollinearity using the car package from R, removing variables with VIF factor > 5. This excluded the model domains ’music’ and ’art’ from RQ1 and ’Biology,’ ’Chemistry’ and precision category ’Torch Float16’ from RQ2. We checked for high-leverage outliers for RQ1, based on Cook’s distance (D>4/N{D>4/N}) and standard residuals (>3>3), and removed 1 data point each from both analyses. Using the Box-Tidwell approach [32], suitable higher-order transformations (See Table. 2 And Table. 3) were performed on some variables to ensure that assumptions of linearity between log odds and the predictors held. Compared to simpler, more interpretable models, the models with power-transformed variables were ultimately preferred for the final reporting due to greater explainability (AIC from 374.4 to 371.6 for RQ2 and from 3454.3 to 3410.9) and validity. Encouragingly, the significant effects and their directionality remain largely preserved across both approaches, confirming the robustness of the results. All effects significant in the transformed models are also significant in the simpler models, except for the number of models built by the developer and likes in RQ1, which do not appear significant before transformation.

Finally, residual tests were performed using the DHARMa package. Neither regression model showed significant dispersion (RQ1:p=0.82{p=0.82} and RQ2:p=0.85{p=0.85}), presence of outliers (RQ1:p=0.18{p=0.18} and RQ2:p=0.42{p=0.42}), or deviation from normal distributions (KS test; RQ1:p=0.78{p=0.78} and RQ2:p=0.78{p=0.78}).

|

Predictor
|

Coefficient
|

p-value
|

|

(Intercept)
|

-3.263988
|

<<0.0001
|

Model Scale
|

Parameters 11
1

https://huggingface.co/spaces/society-ethics/model-card-regulatory-check/
|

0.120302
|

0.026334
|

Data size 11
1

https://huggingface.co/spaces/society-ethics/model-card-regulatory-check/
|

0.179451
|

0.000169
|

Modality
|

Audio
|

-0.949783
|

0.003028
|

Computer Vision
|

0.815687
|

0.014426
|

|

Multimodal
|

-1.288032
|

0.209746
|

|

Natural Language Processing
|

0.384321
|

0.019977
|

|

Reinforcement Learning
|

-13.517337
|

0.984074
|

Domain
|

Biology
|

0.068115
|

0.914340
|

Chemistry
|

0.320644
|

0.713684
|

|

Climate
|

1.646929
|

0.324356
|

|

Code
|

-0.483826
|

0.135364
|

|

Finance
|

-0.174213
|

0.796490
|

|

Legal
|

0.191019
|

0.720080
|

|

Medical
|

-1.235878
|

0.035409
|

Model Developer
|

Team members 11
1

https://huggingface.co/spaces/society-ethics/model-card-regulatory-check/
|

0.193956
|

0.000149
|

Total models 22
2

https://bias.xd.gov/resources/model-card-generator/
|

0.248375
|

<< 0.0001
|

|

Company
|

-0.204922
|

0.273141
|

|

University
|

-0.005852
|

0.983995
|

|

Classroom
|

0.623096
|

0.445068
|

|

Non-profit
|

0.529477
|

0.021068
|

Use and Popularity
|

Likes 33
3

https://huggingface.co/docs/Hub/en/model-card-appendix
|

0.174444
|

0.001643
|

Number of Spaces 11
1

https://huggingface.co/spaces/society-ethics/model-card-regulatory-check/
|

-0.015841
|

0.713853
|

Repository Activity
|

Total Commits 22
2

https://bias.xd.gov/resources/model-card-generator/
|

-0.359598
|

<< 0.0001
|

Threads 11
1

https://huggingface.co/spaces/society-ethics/model-card-regulatory-check/
|

0.090050
|

0.026619
|

|

PR 11
1

https://huggingface.co/spaces/society-ethics/model-card-regulatory-check/
|

0.001501
|

0.974375
|

|

Repository age 22
2

https://bias.xd.gov/resources/model-card-generator/
|

0.054596
|

0.268635
|

Transparency
|

C​O2{CO_{2}} footprint
|

2.177332
|

<< 0.0001
|

Evaluation Availability
|

0.913310
|

<< 0.0001
|

Others
|

High Risk Application
|

-13.834954
|

0.968635
|

|
N= 7092 R2{R^{2}} = 0.115 |

|
AIC = 3411 |

1 Log transformed (base 10) and Standardized 2 Log (base 10), 1/x{1/x} and Standardized 3 Log (base 10), x0.3x^{0.3} and Standardized

Table 2: Test statistics for binomial logistic regression of limits, bias, and risks documentation rates among models based on 1. their project attributes, 2. rates of compliance with related components of the Model Card

|

Predictor
|

Coefficient
|

p-value
|

|

(Intercept)
|

-2.8854
|

<< 0.0001
|

Model Scale
|

Parameters 22
2

https://bias.xd.gov/resources/model-card-generator/
|

0.6695
|

0.000803
|

Data size 11
1

https://huggingface.co/spaces/society-ethics/model-card-regulatory-check/
|

-0.1617
|

0.371708
|

Domain
|

Multi-domain
|

17.3876
|

0.987295
|

code
|

-16.6237
|

0.987853
|

|

medical
|

0.5741
|

0.730284
|

Model Developer
|

Team members 11
1

https://huggingface.co/spaces/society-ethics/model-card-regulatory-check/
|

1.0562
|

<< 0.0001
|

Profile models 11
1

https://huggingface.co/spaces/society-ethics/model-card-regulatory-check/
|

-0.6927
|

0.000257
|

Company
|

-1.6773
|

0.003041
|

University
|

-0.2654
|

0.714144
|

Non profit
|

-1.3751
|

0.173400
|

Use and Popularity
|

Likes 11
1

https://huggingface.co/spaces/society-ethics/model-card-regulatory-check/
|

-0.3491
|

0.194646
|

Number of Spaces 11
1

https://huggingface.co/spaces/society-ethics/model-card-regulatory-check/
|

0.2701
|

0.155802
|

Repository Activity
|

Total Commits 11
1

https://huggingface.co/spaces/society-ethics/model-card-regulatory-check/
|

0.8053
|

<< 0.0001
|

Threads 11
1

https://huggingface.co/spaces/society-ethics/model-card-regulatory-check/
|

0.1761
|

0.427108
|

PR 11
1

https://huggingface.co/spaces/society-ethics/model-card-regulatory-check/
|

-0.1766
|

0.162182
|

|

Repository age 11
1

https://huggingface.co/spaces/society-ethics/model-card-regulatory-check/
|

-0.0203
|

0.920262
|

Transparency
|

C​O2{CO_{2}} Footprint availability
|

2.3698
|

0.001487
|

Evaluation Details
|

Accuracy 33
3

https://huggingface.co/docs/Hub/en/model-card-appendix
|

-0.7631
|

0.001124
|

|

Flagged
|

-0.2596
|

0.796655
|

|

Attempts 11
1

https://huggingface.co/spaces/society-ethics/model-card-regulatory-check/
|

0.3128
|

0.038215
|

Precision
|

4 bit
|

-18.0137
|

0.993056
|

8 bit
|

-0.3797
|

0.802545
|

|

Torch BFloat16
|

0.3294
|

0.316380
|

Others
|

High Risk Application
|

-15.3855
|

0.994607
|

|
N= 788 R2{R^{2}} = 0.272 |

|
AIC = 371.636 |

1 Log transformed (base 10) and Standardized 2 Log (base 10), x4.5{x^{4.5}} and Standardized 3 Standardized

Table 3: Test statistics for binomial logistic regression of limits, bias, and risks documentation rates among models based on 1. features of leaderboard models 2. competitive performance of the models

Interpretation
Our analysis from RQ1 confirms a strong association between evaluation practices and risk documentation, with models reporting some form of evaluation being 149.2% more likely to also carry information on model risks and limits. Other positive effects come from training data size, documentation of C​O2{CO_{2}} footprint, developer team size, commit activity, and popularity (likes). Audio applications and models associated with high contributors (more models) are also less likely to carry risk documentation.

Meanwhile, RQ2 finds that high performers on the Open LLM Leaderboard are less likely to document risks and limitations. One standard unit increase in accuracy reduced risk reporting chances by 53.4%. Greater model size (parameters), documentation of C​O2{CO_{2}} footprint, high number of commits, and developer team size also predict higher chances of a project carrying such documentation. At the same time, companies and high contributors are less likely to do the same. Interestingly, specific model knowledge domains do not exert any significant effect across both analyses, i.e., risk reporting rates are relatively the same across high-stake applications such as medicine or finance, niches such as code, and all other general domains.

### 5 Discussion

Evaluation is core to responsible AI. It is essential to determining model capabilities, and also serves as empirical means to other aspects of responsible AI, such as understanding and acknowledging risks and limitations. Our analyses of OSS practitioners confirms that evaluation and risk assessment generally go hand in hand. However, we also observed that metric-centric arenas, such as competitive leaderboards, may see lesser acknowledgment of model risks among high performers.

Certain other observations were consistent across both analyses. As one might anticipate, development at scale (data-intensive training or parameterization) positively correlates with compliance. Documentation of social impact is also closely associated with broader awareness (as expressed through estimation and reporting of C​O2{CO_{2}} footprint), and projects with more activity, contributions and larger teams tended to do a better job with risk reporting. On the other hand, prolific developers appear to pay less attention to assessing and documenting the limitations of their projects. Informed by these trends, we hereby present our recommendations for contributors, entrepreneurs, and AI hosting services. These include practices and interventions to encourage documentation overall, and to improve efficacy of evaluation protocols in informing both model strengths and weaknesses.

#### 5.1 Recommendations

As one of the leading open-source AI hosting services, Hugging Face has taken steps to inculcate responsible documentation, monitor compliance11
1

https://huggingface.co/spaces/society-ethics/model-card-regulatory-check/, and keep up with regulation [6]. Results from our empirical analyses suggest that risk documentation practices are more prevalent among large teams, while most contributions come from individual developers. Model card guidelines used by Hugging Face and other notable institutions22
2

https://bias.xd.gov/resources/model-card-generator/33
3

https://huggingface.co/docs/Hub/en/model-card-appendix are detailed to facilitate auditing, and usually set specific tasks across developers, sociotechnical experts and managers. Risk assessments involve multiple roles and can make compliance overwhelming for small teams. Streamlining, such as outlining priority requirements may make risk documentation more approachable.

HF’s open LLM leaderboard is a massive undertaking, supported by collaborative monitoring labor from community and moderators. It is notably more transparent than conventional leaderboards (See Sec. 2.2) and tracks model size, precision, libraries, and architectures of most submissions. Such considerations are expected to support explainability, promote sustainable models and inform judicious model selection for small-scale, decentralized applications, which are often less resourced than larger communities or funded corporations.

Data providers and platforms hosting leaderboards need to consider the emerging needs of evaluation, improve upon the reported limitations of benchmarking, and consider multi-faceted tasks and metrics – in short, make evaluation more multi-dimensional. Beyond leaderboards, the choice of tests and metrics for all other model evaluations (and risk assessment) are generally left up to the developer’s discretion. While HF modelcards mention that evaluation choices should ideally address social impact, there is currently a gap in terms of standards, expectations, and norms. Our results suggest that more precise guidelines could have a very large impact on OSS reporting practices. Lastly, fostering broad awareness and hosting training modules on the different dimensions of AI risks (social and environmental), promoting well-documented models [83], and messaging on the importance of quality and safety of models (over quantity) can improve overall developer accountability.

#### 5.2 Limitations

Our research formulation, analyses, and results are meant to explore the correlation between evaluation and risk documentation rather than establish a causal implication. We aimed to measure the prevalence of responsible development practices as operationalized through reporting compliance. With limited regulatory requirements or platform specifications on OSS as of now, we cannot conclusively determine whether the risk assessments provided are necessary or sufficient for any given model, i.e. while our quantitative analyses help to explain existing behaviors, it can be hard to translate these behaviors into impact. Growing consensus over AI safety standards and research establishing testing protocols can be expected to be adopted by platforms, and future work may explore their diffusion into practice, particularly how specific tests enable risk quantification and their efficacy.

Hugging Face’s popularity and moderation make their leaderboards amenable for our research questions (See Sec. 3.1 and Sec. 3.2). Most leaderboards are built towards a particular domain and set of tasks, and submissions are generally uniform in modality. Despite the testing ground being an NLP-only leaderboard, our conclusions about developer accountability are expected to hold for rapidly growing technologies, invariant of modality. We explored popular66
6

https://huggingface.co/docs/leaderboards/en/leaderboards/intro HF leaderboards like MTEB44
4

https://huggingface.co/spaces/mteb/leaderboard and LMSys55
5

https://huggingface.co/spaces/lmsys/chatbot-arena-leaderboard for additional scenarios and found that they drew much lower participation, with too few fully open projects for representative quality or power. We look forward to future studies on improved, up-and-coming leaderboards to further validate our findings and inform evaluation practices going forward.

#### 5.3 Ethics Statement

For our data collection, we largely followed prior work and used the public Hugging Face API for model cards and open repository data. Beyond the API, we collected some limited public-facing numeric data from model landing pages, which are intended for public reference and sharing with no expectation of privacy (Table. 1). We did not add any features to our data collection code for specifically parsing personally-identifying information, nor was such information required for our analysis. The only identifiers used were public developer usernames, which are also part of the model path in the HF web indexing.
Finally, we note that some public, open weight models carry ’’Not Safe For Work" and ’’Not for all Audiences" warnings from developers or the platform moderators77
7

https://huggingface.co/content-guidelines. We retain these labels in our dataset so that any researchers wishing to use this data can be fully informed about the potential for some model metadata to contain content inappropriate for some settings.
Proprietary LLM-based language editing services Grammarly and Anthropic Claude were used to a limited extent to correct misspellings, grammar and consistency of composition, and the resulting manuscript was thoroughly verified and updated by all the authors over multiple iterations.

### 6 Conclusion

Through our focused study of a rising open source platform, we had the opportunity to observe a diverse range of AI/ML applications and development practices. Our analyses empirically probe open source AI trends in the backdrop of increasing concerns over their potential to transform or affect society, and consequent legal and ethical oversight. As we situate our investigation amidst the interests of these various stakeholders, we discover promising trends of concurrent compliance of evaluations and risk assessments. At the same time, our large sample study produces evidence supporting long standing observations and calls for fundamental reforms and greater rigor in AI evaluation.

As AI continues to grow, these lessons emphasize the importance of fostering a culture of responsible development and accountability across all sectors, not only commercial but also informal and non-profit undertakings. Platforms, developers, and stakeholders must work together to establish best practices and design balanced policies and standards that mutually support each other while also preserving the true spirit of innovation. This will be vital in ensuring that AI technologies are developed and deployed ethically, safely, and benefit humanity at large.

### References

- [1]

Add sorting option by model size [New Feature Proposal] — discuss.huggingface.co.

https://discuss.huggingface.co/t/add-sorting-option-by-model-size-new-feature-proposal/29085.

[Accessed 09-09-2024].

- [2]

Artificial Intelligence Incident Database - Discover — incidentdatabase.ai.

https://incidentdatabase.ai/apps/discover/?is_incident_report=true&s=open%20source.

[Accessed 11-09-2024].

- [3]

GGUF — huggingface.co.

https://huggingface.co/docs/hub/en/gguf.

[Accessed 09-09-2024].

- [4]

Man Arrested for Producing, Distributing, and Possessing AI-Generated Images of Minors Engaged in Sexually Explicit Conduct — justice.gov.

https://www.justice.gov/opa/pr/man-arrested-producing-distributing-and-possessing-ai-generated-images-minors-engaged.

[Accessed 27-08-2024].

- [5]

Pathways Language Model (PaLM): Scaling to 540 Billion Parameters for Breakthrou — research.google.

https://research.google/blog/pathways-language-model-palm-scaling-to-540-billion-parameters-for-breakthrough-performance/.

[Accessed 09-09-2024].

- [6]

Public Policy at Hugging Face — huggingface.co.

https://huggingface.co/blog/policy-blog.

[Accessed 12-09-2024].

- [7]

Safetensors — huggingface.co.

https://huggingface.co/docs/safetensors/en/index.

[Accessed 09-09-2024].

- [8]

Safetensors params/precision on model page — discuss.huggingface.co.

https://discuss.huggingface.co/t/safetensors-params-precision-on-model-page/67913/3.

[Accessed 09-09-2024].

- [9]

Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, et al.

Gpt-4 technical report.

arXiv preprint arXiv:2303.08774, 2023.

- [10]

Adem Ait, Javier Luis Cánovas Izquierdo, and Jordi Cabot.

HFCommunity: An extraction process and relational database to analyze Hugging Face Hub data.

Science of Computer Programming, 234:103079, May 2024.

- [11]

Adem Ait, Javier Luis Cánovas Izquierdo, and Jordi Cabot.

On the Suitability of Hugging Face Hub for Empirical Studies, July 2023.

arXiv:2307.14841 [cs].

- [12]

Ibrahim M Alabdulmohsin, Behnam Neyshabur, and Xiaohua Zhai.

Revisiting neural scaling laws in language and vision.

Advances in Neural Information Processing Systems, 35:22300–22312, 2022.

- [13]

Matthew Arnold, Rachel KE Bellamy, Michael Hind, Stephanie Houde, Sameep Mehta, Aleksandra Mojsilović, Ravi Nair, K Natesan Ramamurthy, Alexandra Olteanu, David Piorkowski, et al.

Factsheets: Increasing trust in ai services through supplier’s declarations of conformity.

IBM Journal of Research and Development, 63(4/5):6–1, 2019.

- [14]

Sanjeev Arora and Yi Zhang.

Rip van winkle’s razor: A simple estimate of overfit to test data.

arXiv preprint arXiv:2102.13189, 2021.

- [15]

Yasaman Bahri, Ethan Dyer, Jared Kaplan, Jaehoon Lee, and Utkarsh Sharma.

Explaining neural scaling laws.

Proceedings of the National Academy of Sciences, 121(27):e2311878121, 2024.

- [16]

Simone Balloccu, Patrícia Schmidtová, Mateusz Lango, and Ondřej Dušek.

Leak, cheat, repeat: Data contamination and evaluation malpractices in closed-source llms.

In Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long Papers), pages 67–93, 2024.

- [17]

Peter L Bartlett, Andrea Montanari, and Alexander Rakhlin.

Deep learning: a statistical viewpoint.

Acta numerica, 30:87–201, 2021.

- [18]

Edward Beeching, Clémentine Fourrier, Nathan Habib, Sheon Han, Nathan Lambert, Nazneen Rajani, Omar Sanseviero, Lewis Tunstall, and Thomas Wolf.

Open llm leaderboard (2023-2024).

https://huggingface.co/spaces/open-llm-leaderboard-old/open_llm_leaderboard, 2023.

- [19]

Emily M. Bender, Emily M. Bender, Batya Friedman, and Batya Friedman.

Data Statements for Natural Language Processing: Toward Mitigating System Bias and Enabling Better Science.

Transactions of the Association for Computational Linguistics, 2018.

- [20]

Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, and Shmargaret Shmitchell.

On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?

In Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency, pages 610–623, Virtual Event Canada, March 2021. ACM.

- [21]

Yochai Benkler.

The Wealth of Networks: How Social Production Transforms Markets and Freedom.

Yale University Press, 2006.

- [22]

Abeba Birhane, vinay prabhu, Sanghyun Han, Vishnu Boddeti, and Sasha Luccioni.

Into the laion’s den: Investigating hate in multimodal datasets.

In A. Oh, T. Naumann, A. Globerson, K. Saenko, M. Hardt, and S. Levine, editors, Advances in Neural Information Processing Systems, volume 36, pages 21268–21284. Curran Associates, Inc., 2023.

- [23]

Abeba Birhane, Vinay Uday Prabhu, and Emmanuel Kahembwe.

Multimodal datasets: misogyny, pornography, and malignant stereotypes.

arXiv preprint arXiv:2110.01963, 2021.

- [24]

Su Lin Blodgett, Solon Barocas, Hal Daumé III, and Hanna Wallach.

Language (technology) is power: A critical survey of" bias" in nlp.

arXiv preprint arXiv:2005.14050, 2020.

- [25]

Avrim Blum and Moritz Hardt.

The ladder: A reliable leaderboard for machine learning competitions.

In International Conference on Machine Learning, pages 1006–1014. PMLR, 2015.

- [26]

Ondřej Bojar, Rajen Chatterjee, Christian Federmann, Yvette Graham, Barry Haddow, Shujian Huang, Matthias Huck, Philipp Koehn, Qun Liu, Varvara Logacheva, et al.

Findings of the 2017 conference on machine translation (wmt17).

In Proceedings of the Second Conference on Machine Translation, pages 169–214, 2017.

- [27]

Rishi Bommasani, Drew A Hudson, Ehsan Adeli, Russ Altman, Simran Arora, Sydney von Arx, Michael S Bernstein, Jeannette Bohg, Antoine Bosselut, Emma Brunskill, et al.

On the opportunities and risks of foundation models.

ACM Computing Surveys, 55(5):1–166, 2022.

- [28]

Rishi Bommasani, Kevin Klyman, Shayne Longpre, Sayash Kapoor, Nestor Maslej, Betty Xiong, Daniel Zhang, and Percy Liang.

The Foundation Model Transparency Index, October 2023.

arXiv:2310.12941 [cs].

- [29]

Shikha Bordia and Samuel Bowman.

Identifying and reducing gender bias in word-level language models.

In Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Student Research Workshop, pages 7–15, 2019.

- [30]

Samuel Bowman, Gabor Angeli, Christopher Potts, and Christopher D Manning.

A large annotated corpus for learning natural language inference.

In Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing, pages 632–642, 2015.

- [31]

Samuel Bowman and George Dahl.

What will it take to fix benchmarking in natural language understanding?

In Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, pages 4843–4855, 2021.

- [32]

George EP Box and Paul W Tidwell.

Transformation of the independent variables.

Technometrics, 4(4):531–550, 1962.

- [33]

Tom B Brown.

Language models are few-shot learners.

arXiv preprint arXiv:2005.14165, 2020.

- [34]

Joel Castaño, Silverio Martínez-Fernández, and Xavier Franch.

Lessons learned from mining the hugging face repository.

In Proceedings of the 1st IEEE/ACM International Workshop on Methodological Issues with Empirical Studies in Software Engineering, pages 1–6, 2024.

- [35]

Mahasweta Chakraborti, Curtis Atkisson, Ştefan Stănciulescu, Vladimir Filkov, and Seth Frey.

Do we run how we say we run? formalization and practice of governance in oss communities.

In Proceedings of the CHI Conference on Human Factors in Computing Systems, pages 1–26, 2024.

- [36]

Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot, Ashish Sabharwal, Carissa Schoenick, and Oyvind Tafjord.

Think you have solved question answering? try arc, the ai2 reasoning challenge.

arXiv preprint arXiv:1803.05457, 2018.

- [37]

Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, et al.

Training verifiers to solve math word problems.

arXiv preprint arXiv:2110.14168, 2021.

- [38]

Gabriella Coleman.

Coding freedom: The ethics and aesthetics of hacking.

Princeton University Press, 2013.

- [39]

Danish Contractor, Daniel McDuff, Julia Katherine Haines, Jenny Lee, Christopher Hines, Brent Hecht, Nicholas Vincent, and Hanlin Li.

Behavioral use licensing for responsible ai.

In Proceedings of the 2022 ACM Conference on Fairness, Accountability, and Transparency, pages 778–788, 2022.

- [40]

Papers With Code Contributors.

Papers with code.

https://paperswithcode.com/, 2024.

Accessed: [Insert access date here].

- [41]

Anamaria Crisan, Margaret Drouhard, Jesse Vig, and Nazneen Rajani.

Interactive Model Cards: A Human-Centered Approach to Model Documentation.

In 2022 ACM Conference on Fairness, Accountability, and Transparency, pages 427–439, Seoul Republic of Korea, June 2022. ACM.

- [42]

Kevin Crowston, Kangning Wei, James Howison, and Andrea Wiggins.

Free/libre open source software development: What we know and what we do not know.

ACM Computing Surveys (CSUR), 44(2):1–35, 2012.

- [43]

Mostafa Dehghani, Yi Tay, Alexey A. Gritsenko, Zhe Zhao, Neil Houlsby, Fernando Diaz, Donald Metzler, and Oriol Vinyals.

The Benchmark Lottery, July 2021.

arXiv:2107.07002 [cs].

- [44]

Chunyuan Deng, Yilun Zhao, Xiangru Tang, Mark Gerstein, and Arman Cohan.

Benchmark probing: Investigating data leakage in large language models.

In NeurIPS 2023 Workshop on Backdoors in Deep Learning - The Good, the Bad, and the Ugly, 2024.

- [45]

Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li, and Li Fei-Fei.

Imagenet: A large-scale hierarchical image database.

2009 IEEE Conference on Computer Vision and Pattern Recognition, pages 248–255, 2009.

- [46]

Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova.

Bert: Pre-training of deep bidirectional transformers for language understanding.

In Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers), pages 4171–4186, 2019.

- [47]

Cynthia Dwork, Vitaly Feldman, Moritz Hardt, Toniann Pitassi, Omer Reingold, and Aaron Roth.

The reusable holdout: Preserving validity in adaptive data analysis.

Science, 349(6248):636–638, 2015.

- [48]

Cynthia Dwork, Moritz Hardt, Toniann Pitassi, Omer Reingold, and Richard Zemel.

Fairness through awareness.

In Proceedings of the 3rd innovations in theoretical computer science conference, pages 214–226, 2012.

- [49]

Upol Ehsan, Q. Vera Liao, Michael Muller, Mark O. Riedl, and Justin D. Weisz.

Expanding explainability: Towards social transparency in ai systems.

In Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems, CHI ’21, New York, NY, USA, 2021. Association for Computing Machinery.

- [50]

Kawin Ethayarajh and Dan Jurafsky.

Utility is in the eye of the user: A critique of NLP leaderboards.

In Bonnie Webber, Trevor Cohn, Yulan He, and Yang Liu, editors, Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP), pages 4846–4853, Online, November 2020. Association for Computational Linguistics.

- [51]

European Parliament and Council of the European Union.

Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 laying down harmonised rules on artificial intelligence and amending Regulations (EC) No 300/2008, (EU) No 167/2013, (EU) No 168/2013, (EU) 2018/858, (EU) 2018/1139 and (EU) 2019/2144 and Directives 2014/90/EU, (EU) 2016/797 and (EU) 2020/1828 (Artificial Intelligence Act), 6 2024.

Text with EEA relevance.

- [52]

Hugging Face.

Model Card Guidebook huggingface.co.

https://huggingface.co/docs/hub/en/model-card-guidebook, 2024.

- [53]

Gregory Falco, Gregory Falco, Ben Shneiderman, Ben Shneiderman, Julia Badger, Julia Badger, Ryan Carrier, Ryan Carrier, Anton Dahbura, A. T. Dahbura, David Danks, David Danks, Martin Eling, Martin Eling, Alwyn E. Goodloe, Alwyn Goodloe, J. P. Gupta, Jerry Gupta, Christopher Hart, Christopher Hart, Marina Jirotka, Marina Jirotka, Henric Johnson, Henric Johnson, Cara Lapointe, Cara LaPointe, Ashley J. Llorens, Ashley J. Llorens, Alan K. Mackworth, Alan K. Mackworth, Carsten Maple, Carsten Maple, S. E. Pálsson, Sigurður Emil Pálsson, Frank A. Pasquale, Frank A. Pasquale, Alan F. T. Winfield, Alan F. T. Winfield, Zee Kin Yeong, and Zee Kin Yeong.

Governing AI safety through independent audits.

Nature Machine Intelligence, 2021.

- [54]

Luciano Floridi, Josh Cowls, Monica Beltrametti, Raja Chatila, Patrice Chazerand, Virginia Dignum, Christoph Luetge, Robert Madelin, Ugo Pagallo, Francesca Rossi, et al.

Ai4people—an ethical framework for a good ai society: opportunities, risks, principles, and recommendations.

Minds and machines, 28:689–707, 2018.

- [55]

Carl Franzen.

New open source AI leader Reflection 70B’s performance questioned, accused of ‘fraud’ — venturebeat.com.

https://venturebeat.com/ai/new-open-source-ai-leader-reflection-70bs-performance-questioned-accused-of-fraud/.

[Accessed 12-09-2024].

- [56]

Leo Gao, Jonathan Tow, Baber Abbasi, Stella Biderman, Sid Black, Anthony DiPofi, Charles Foster, Laurence Golding, Jeffrey Hsu, Alain Le Noac’h, Haonan Li, Kyle McDonell, Niklas Muennighoff, Chris Ociepa, Jason Phang, Laria Reynolds, Hailey Schoelkopf, Aviya Skowron, Lintang Sutawika, Eric Tang, Anish Thite, Ben Wang, Kevin Wang, and Andy Zou.

A framework for few-shot language model evaluation, 07 2024.

- [57]

Timnit Gebru, Timnit Gebru, Jamie Morgenstern, Jamie Morgenstern, Briana Vecchione, Briana Vecchione, Briana Vecchione, J. Vaughan, Jennifer Wortman Vaughan, Hanna Wallach, Hanna Wallach, Hal Daumé, Hal Daumé, Kate Crawford, and Kate Crawford.

Datasheets for Datasets.

arXiv: Databases, 2018.

- [58]

Sebastian Gehrmann, Tosin Adewumi, Karmanya Aggarwal, Pawan Sasanka Ammanamanchi, Anuoluwapo Aremu, Antoine Bosselut, Khyathi Raghavi Chandu, Miruna Clinciu, Dipanjan Das, Kaustubh Dhole, et al.

The gem benchmark: Natural language generation, its evaluation and metrics.

In Proceedings of the 1st Workshop on Natural Language Generation, Evaluation, and Metrics (GEM 2021), pages 96–120, 2021.

- [59]

Aryo Pradipta Gema, Joshua Ong Jun Leang, Giwon Hong, Alessio Devoto, Alberto Carlo Maria Mancino, Rohit Saxena, Xuanli He, Yu Zhao, Xiaotang Du, Mohammad Reza Ghasemi Madani, Claire Barale, Robert McHardy, Joshua Harris, Jean Kaddour, Emile van Krieken, and Pasquale Minervini.

Are We Done with MMLU?, June 2024.

arXiv:2406.04127 [cs].

- [60]

Lina Gong, Jingxuan Zhang, Mingqiang Wei, Haoxiang Zhang, and Zhiqiu Huang.

What Is the Intended Usage Context of This Model? An Exploratory Study of Pre-Trained Models on Various Model Repositories.

ACM Trans. Softw. Eng. Methodol., 32(3), May 2023.

Place: New York, NY, USA Publisher: Association for Computing Machinery.

- [61]

The Stanford Natural Language Processing Group.

Snli leaderboard.

https://nlp.stanford.edu/projects/snli/, 2015.

[Accessed 07-08-2024].

- [62]

Moritz Hardt.

Climbing a shaky ladder: Better adaptive risk estimation.

arXiv preprint arXiv:1706.02733, 2017.

- [63]

Lennart Heim and Leonie Koessler.

Training Compute Thresholds: Features and Functions in AI Regulation, August 2024.

arXiv:2405.10799 [cs].

- [64]

Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song, and Jacob Steinhardt.

Measuring massive multitask language understanding.

In International Conference on Learning Representations, 2021.

- [65]

Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, et al.

Training compute-optimal large language models.

In Proceedings of the 36th International Conference on Neural Information Processing Systems, pages 30016–30030, 2022.

- [66]

Ben Hutchinson, Andrew Smart, Alex Hanna, Emily Denton, Christina Greer, Oddur Kjartansson, Parker Barnes, and Margaret Mitchell.

Towards accountability for machine learning datasets: Practices from software engineering and infrastructure.

In Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency, pages 560–575, 2021.

- [67]

Robin Jia and Percy Liang.

Adversarial examples for evaluating reading comprehension systems.

In Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing. Association for Computational Linguistics, 2017.

- [68]

Wenxin Jiang, Jason Jones, Jerin Yasmin, Nicholas Synovic, Rajeev Sashti, Sophie Chen, George K. Thiruvathukal, Yuan Tian, and James C. Davis.

PeaTMOSS: Mining Pre-Trained Models in Open-Source Software, October 2023.

arXiv:2310.03620 [cs].

- [69]

Wenxin Jiang, Nicholas Synovic, Matt Hyatt, Taylor R. Schorlemmer, Konstantin Läufer, Yanbin Lü, George K. Thiruvathukal, and J. C. Davis.

An Empirical Study of Pre-Trained Model Reuse in the Hugging Face Deep Learning Model Registry.

International Conference on Software Engineering, 2023.

- [70]

Wenxin Jiang, Nicholas Synovic, Purvish Jajal, Taylor R. Schorlemmer, Arav Tewari, Bhavesh Pareek, George K. Thiruvathukal, and J. C. Davis.

PTMTorrent: A Dataset for Mining Open-source Pre-trained Model Packages.

IEEE Working Conference on Mining Software Repositories, 2023.

- [71]

Wenxin Jiang, Nicholas Synovic, Rohan Sethi, Aryan Indarapu, Matt Hyatt, Taylor R Schorlemmer, George K Thiruvathukal, and James C Davis.

An empirical study of artifacts and security risks in the pre-trained model supply chain.

In Proceedings of the 2022 ACM Workshop on Software Supply Chain Offensive Research and Ecosystem Defenses, pages 105–114, 2022.

- [72]

Anna Jobin, Anna Jobin, Marcello Ienca, Marcello Ienca, and Effy Vayena.

The global landscape of AI ethics guidelines.

Nature Machine Intelligence, 2019.

- [73]

Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B. Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, and Dario Amodei.

Scaling Laws for Neural Language Models, January 2020.

arXiv:2001.08361 [cs, stat].

- [74]

Adhishree Kathikar, Aishwarya Nair, Ben Lazarine, Agrim Sachdeva, and Sagar Samtani.

Assessing the Vulnerabilities of the Open-Source Artificial Intelligence (AI) Landscape: A Large-Scale Analysis of the Hugging Face Platform.

In 2023 IEEE International Conference on Intelligence and Security Informatics (ISI), pages 1–6, 2023.

- [75]

Douwe Kiela, Max Bartolo, Yixin Nie, Divyansh Kaushik, Atticus Geiger, Zhengxuan Wu, Bertie Vidgen, Grusha Prasad, Amanpreet Singh, Pratik Ringshia, et al.

Dynabench: Rethinking benchmarking in nlp.

In Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, pages 4110–4124, 2021.

- [76]

Alexandre Lacoste, Alexandra Luccioni, Victor Schmidt, and Thomas Dandres.

Quantifying the carbon emissions of machine learning.

arXiv preprint arXiv:1910.09700, 2019.

- [77]

Harry Law and Sébastien Krier.

Open-source provisions for large models in the AI Act.

2023.

Publisher: Cambridge University Science and Policy Exchange.

- [78]

Yann LeCun, Léon Bottou, Yoshua Bengio, and Patrick Haffner.

Gradient-based learning applied to document recognition.

Proceedings of the IEEE, 86(11):2278–2324, 1998.

- [79]

Hao-Ping (Hank) Lee, Yu-Ju Yang, Thomas Serban Von Davier, Jodi Forlizzi, and Sauvik Das.

Deepfakes, Phrenology, Surveillance, and More! A Taxonomy of AI Privacy Risks.

In Proceedings of the CHI Conference on Human Factors in Computing Systems, CHI ’24, New York, NY, USA, 2024. Association for Computing Machinery.

event-place: Honolulu, HI, USA.

- [80]

Bo Li, Peng Qi, Bo Liu, Shuai Di, Jingen Liu, Jiquan Pei, Jinfeng Yi, and Bowen Zhou.

Trustworthy ai: From principles to practices.

ACM Computing Surveys, 55(9):1–46, 2023.

- [81]

Renee Li, Pavitthra Pandurangan, Hana Frluckaj, and Laura Dabbish.

Code of conduct conversations in open source software projects on github.

Proceedings of the ACM on Human-Computer Interaction, 5(CSCW1):1–31, 2021.

- [82]

Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian Zhang, Deepak Narayanan, Yuhuai Wu, Ananya Kumar, et al.

Holistic evaluation of language models.

In Advances in Neural Information Processing Systems, volume 36, 2023.

- [83]

Weixin Liang, Nazneen Rajani, Xinyu Yang, Ezinwanne Ozoani, Eric Wu, Yiqun Chen, Daniel Scott Smith, and James Zou.

Systematic analysis of 32,111 ai model cards characterizes documentation practice in ai.

Nature Machine Intelligence, 6(7):744–753, 2024.

- [84]

Q. Vera Liao, Moninder Singh, Yunfeng Zhang, and Rachel Bellamy.

Introduction to explainable ai.

In Extended Abstracts of the 2021 CHI Conference on Human Factors in Computing Systems, CHI EA ’21, New York, NY, USA, 2021. Association for Computing Machinery.

- [85]

Adam Lilja, Junsheng Fu, Erik Stenborg, and Lars Hammarstrand.

Localization is all you evaluate: Data leakage in online mapping datasets and how to fix it.

In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages 22150–22159, 2024.

- [86]

Stephanie Lin, Jacob Hilton, and Owain Evans.

Truthfulqa: Measuring how models mimic human falsehoods.

In Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 3214–3252, 2022.

- [87]

Inbal Magar and Roy Schwartz.

Data contamination: From memorization to exploitation.

In Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers), pages 157–165, 2022.

- [88]

Thomas Manzini, Yao Chong Lim, Yulia Tsvetkov, and Alan W Black.

Black is to criminal as caucasian is to police: Detecting and removing multiclass bias in word embeddings.

In 2019 Annual Conference of the North American Chapter of the Association for Computational Linguistics (NAACL), 2019.

- [89]

Nahema Marchal, Rachel Xu, Rasmi Elasmar, Iason Gabriel, Beth Goldberg, and William Isaac.

Generative AI Misuse: A Taxonomy of Tactics and Insights from Real-World Data, June 2024.

arXiv:2406.13843 [cs].

- [90]

Nestor Maslej, Loredana Fattorini, Ray Perrault, Vanessa Parli, Anka Reuel, Erik Brynjolfsson, John Etchemendy, Katrina Ligett, Terah Lyons, James Manyika, Juan Carlos Niebles, Yoav Shoham, Russell Wald, and Jack Clark.

Artificial intelligence index report 2024.

ArXiv, abs/2405.19522, 2024.

- [91]

Daniel McDuff, Tim Korjakow, Scott Cambo, Jesse Josua Benjamin, Jenny Lee, Yacine Jernite, Carlos Muñoz Ferrandis, Aaron Gokaslan, Alek Tarkowski, Joseph Lindley, et al.

On the standardization of behavioral use clauses and their adoption for responsible licensing of ai.

arXiv preprint arXiv:2402.05979, 2024.

- [92]

Ninareh Mehrabi, MehrabiNinareh, Ninareh Mehrabi, Fred Morstatter, Fred Morstatter, MorstatterFred, Nripsuta Saxena, Nripsuta Saxena, SaxenaNripsuta, Nripsuta Saxena, Kristina Lerman, LermanKristina, Kristina Lerman, Aram Galstyan, GalstyanAram, and Aram Galstyan.

A Survey on Bias and Fairness in Machine Learning.

ACM Computing Surveys, 2021.

- [93]

Sophie Mellor.

A.I. chatbot trained on 4chan by YouTuber is slammed by ethics experts — fortune.com.

https://fortune.com/2022/06/10/ai-chatbot-trained-on-4chan-by-yannic-kilcher-draw-ethics-questions/.

[Accessed 11-09-2024].

- [94]

Margaret Mitchell, Simone Wu, Andrew Zaldivar, Parker Barnes, Lucy Vasserman, Ben Hutchinson, Elena Spitzer, Inioluwa Deborah Raji, and Timnit Gebru.

Model cards for model reporting.

In Proceedings of the conference on fairness, accountability, and transparency, pages 220–229, 2019.

- [95]

Jakob Mökander, Jonas Schuett, Hannah Rose Kirk, and Luciano Floridi.

Auditing large language models: a three-layered approach.

AI and Ethics, May 2023.

- [96]

Moin Nadeem, Anna Bethke, and Siva Reddy.

Stereoset: Measuring stereotypical bias in pretrained language models.

In Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers), pages 5356–5371, 2021.

- [97]

Yixin Nie, Adina Williams, Emily Dinan, Mohit Bansal, Jason Weston, and Douwe Kiela.

Adversarial nli: A new benchmark for natural language understanding.

In Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, pages 4885–4901, 2020.

- [98]

Alexandra Olteanu, Alexandra Olteanu, Carlos Castillo, Carlos Castillo, Fernando Diaz, Fernando Diaz, Emre Kıcıman, Emre Kiciman, and Emre Kiciman.

Social Data: Biases, Methodological Pitfalls, and Ethical Boundaries.

Social Science Research Network, 2019.

- [99]

Cailean Osborrne, Jennifer Ding, and Hannah Rose Kirk.

The ai community building the future? a quantitative analysis of development activity on hugging face hub.

Journal of Computational Social Science, pages 1–39, 2024.

- [100]

Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al.

Training language models to follow instructions with human feedback.

Advances in neural information processing systems, 35:27730–27744, 2022.

- [101]

Ezi Ozoani, Marissa Gerchick, and Margaret Mitchell.

Model card guidebook.

https://huggingface.co/docs/hub/en/model-card-guidebook, 2022.

Accessed: [Insert access date here].

- [102]

Federica Pepe, Vittoria Nardone, Antonio Mastropaolo, Gabriele Bavota, Gerardo Canfora, and Massimiliano Di Penta.

How do hugging face models document datasets, bias, and licenses? an empirical study.

In Proceedings of the 32nd IEEE/ACM International Conference on Program Comprehension, pages 370–381, 2024.

- [103]

Inioluwa Deborah Raji, Emily M. Bender, Amandalynne Paullada, Emily Denton, and Alex Hanna.

AI and the Everything in the Whole Wide World Benchmark, November 2021.

arXiv:2111.15366 [cs].

- [104]

Inioluwa Deborah Raji and Joy Buolamwini.

Actionable auditing: Investigating the impact of publicly naming biased performance results of commercial ai products.

In Proceedings of the 2019 AAAI/ACM Conference on AI, Ethics, and Society, pages 429–435, 2019.

- [105]

Pranav Rajpurkar, Jian Zhang, Konstantin Lopyrev, and Percy Liang.

Squad: 100,000+ questions for machine comprehension of text.

In Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing, pages 2383–2392, 2016.

- [106]

Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, and Björn Ommer.

High-resolution image synthesis with latent diffusion models.

In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pages 10684–10695, 2022.

- [107]

Rachel Rudinger, Jason Naradowsky, Brian Leonard, and Benjamin Van Durme.

Gender bias in coreference resolution.

In Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 2 (Short Papers), pages 8–14, 2018.

- [108]

Oscar Sainz, Jon Ander Campos, Iker García-Ferrero, Julen Etxaniz, Oier Lopez de Lacalle, and Eneko Agirre.

Nlp evaluation in trouble: On the need to measure llm data contamination for each benchmark.

In The 2023 Conference on Empirical Methods in Natural Language Processing, 2023.

- [109]

Keisuke Sakaguchi, Ronan Le Bras, Chandra Bhagavatula, and Yejin Choi.

Winogrande: An adversarial winograd schema challenge at scale.

Communications of the ACM, 64(9):99–106, 2021.

- [110]

Aarohi Srivastava, Abhinav Rastogi, Abhishek Rao, Abu Awal Md Shoham, Xinyun Bai, Shunyu Gu, Mayank Arora, Kuan Zhou, Pang Wei Koh, Romal Saxena, et al.

Beyond the imitation game: Quantifying and extrapolating the capabilities of language models, 2022.

- [111]

Emma Strubell, Ananya Ganesh, and Andrew McCallum.

Energy and policy considerations for modern deep learning research.

In Proceedings of the AAAI conference on artificial intelligence, volume 34, pages 13693–13696, 2020.

- [112]

Mina Taraghi, Gianolli Dorcelus, Armstrong Foundjem, Florian Tambon, and Foutse Khomh.

Deep Learning Model Reuse in the HuggingFace Community: Challenges, Benefit and Trends, January 2024.

arXiv:2401.13177 [cs].

- [113]

Yi Tay, Mostafa Dehghani, Jai Prakash Gupta, Vamsi Aribandi, Dara Bahri, Zhen Qin, and Donald Metzler.

Are pretrained convolutions better than pretrained transformers?

In Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers), pages 4349–4359, 2021.

- [114]

A Vaswani.

Attention is all you need.

Advances in Neural Information Processing Systems, 2017.

- [115]

Alex Wang, Yada Pruksachatkun, Nikita Nangia, Amanpreet Singh, Julian Michael, Felix Hill, Omer Levy, and Samuel R Bowman.

Superglue: A stickier benchmark for general-purpose language understanding systems.

In Advances in Neural Information Processing Systems, pages 3266–3280, 2019.

- [116]

Alex Wang, Amanpreet Singh, Julian Michael, Felix Hill, Omer Levy, and Samuel R Bowman.

Glue: A multi-task benchmark and analysis platform for natural language understanding.

In Proceedings of the 2018 EMNLP Workshop BlackboxNLP: Analyzing and Interpreting Neural Networks for NLP, pages 353–355, 2018.

- [117]

Laura Weidinger, John Mellor, Maribeth Rauh, Conor Griffin, Jonathan Uesato, Po-Sen Huang, Myra Cheng, Mia Glaese, Borja Balle, Atoosa Kasirzadeh, Zac Kenton, Sasha Brown, Will Hawkins, Tom Stepleton, Courtney Biles, Abeba Birhane, Julia Haas, Laura Rimell, Lisa Anne Hendricks, William Isaac, Sean Legassick, Geoffrey Irving, and Iason Gabriel.

Ethical and social risks of harm from Language Models, December 2021.

arXiv:2112.04359 [cs].

- [118]

Thomas Wolf, Lysandre Debut, Victor Sanh, Julien Chaumond, Clement Delangue, Anthony Moi, Pierric Cistac, Tim Rault, Rémi Louf, Morgan Funtowicz, et al.

Transformers: State-of-the-art natural language processing.

In Proceedings of the 2020 conference on empirical methods in natural language processing: system demonstrations, pages 38–45, 2020.

- [119]

Xinyu Yang, Weixin Liang, and James Zou.

Navigating dataset documentation in ml: A large-scale analysis of dataset cards on hugging face.

In NeurIPS 2023 Workshop on Regulatable ML, 2023.

- [120]

Likang Yin, Mahasweta Chakraborti, Yibo Yan, Charles Schweik, Seth Frey, and Vladimir Filkov.

Open source software sustainability: Combining institutional analysis and socio-technical networks.

Proc. ACM Hum.-Comput. Interact., 6(CSCW2), nov 2022.

- [121]

Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali Farhadi, and Yejin Choi.

Hellaswag: Can a machine really finish your sentence?

In Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics, pages 4791–4800, 2019.

- [122]

Wei Emma Zhang, Quan Z Sheng, Ahoud Alhazmi, and Chenliang Li.

Adversarial attacks on deep-learning models in natural language processing: A survey.

ACM Transactions on Intelligent Systems and Technology (TIST), 11(3):1–41, 2020.

- [123]

Jieyu Zhao, Tianlu Wang, Mark Yatskar, Vicente Ordonez, and Kai-Wei Chang.

Gender bias in coreference resolution: Evaluation and debiasing methods.

In Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 2 (Short Papers), pages 15–20, 2018.

### Appendix A Benchmarks in Open LLM Leaderboard

Benchmark
|

Brief Description
|

Metric Used
|

AI2 Reasoning Challenge (ARC) [36]
|

A set of grade-school science questions (25-shot)
|

Accuracy (normalized by target length)
|

HellaSwag [121]
|

A test of commonsense inference, challenging for SOTA models but easy for humans (10-shot)
|

Accuracy (normalized by target length)
|

MMLU [64]
|

Measures multitask accuracy across 57 tasks including mathematics, history, law, and more (5-shot)
|

Accuracy
|

TruthfulQA [86]
|

Measures a model’s propensity to reproduce common online falsehoods (0-shot)
|

MC2 (Normalized probability over true references)
|

Winogrande [109]
|

An adversarial and difficult Winograd benchmark for commonsense reasoning (5-shot)
|

Accuracy
|

GSM8k [37]
|

Diverse grade school math word problems to test multi-step mathematical reasoning (5-shot)
|

Accuracy
|

Table 4: Summary of the six key benchmarks adopted by the Open LLM Leaderboard v1 from the Eleuther LLM evaluation harness [56]. The main leaderboard, by default, ranks models by their average performance across these benchmarks

### Appendix B Service-ready Features and Identifiers

- •

Use this code: Platform-generated example scripts (button above the repository) to guide model loading and use through recognized libraries.

- •

Endpoints_compatible11
1

https://huggingface.co/inference-endpoints/dedicated: Inference Endpoints are scalable and production-ready API endpoints for machine learning models. This repo tag indicates that a particular model is compatible with Inference Endpoints.

- •

Pipeline_tag22
2

https://huggingface.co/docs/hub/en/models-tasks: These tags denote the specific task a model was designed for, such as "text-classification", or "object-detection". These tags act as semantic categories to enhance model discoverability for specific applications, and are either detected by the hub or indicated by the developer from a list of recognized applications.

- •

Autotrain_compatible33
3

https://huggingface.co/autotrain: This tag indicates if a project is a complete pre-trained model and compatible within the HF ecosystem for downstream fine-tuning on custom data.

- •

Text-embeddings-inference44
4

https://github.com/huggingface/text-embeddings-inference: Allows generation of text embeddings at scale from compatible models. This tag appears in the repository of such compatible models.

- •

Text-generation-inference55
5

https://github.com/huggingface/text-generation-inference: A runtime, sometimes also a widget, to handle text generation queries to a model. Enabled for fully functional LLMs, these models are tagged the same.

- •

Intended Purpose (Documentation)66
6

https://huggingface.co/docs/hub/en/model-card-annotated: We use the model card scanner from HF to detect detailed documentation from developers on explaining model usage, e.g., direct or downstream applications, optionally provided code etc

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
