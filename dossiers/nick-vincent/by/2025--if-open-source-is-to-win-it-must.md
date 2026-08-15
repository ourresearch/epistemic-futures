---
title: "If open source is to win, it must go public"
person: "nick-vincent"
section: "by"
type: "journal-article"
year: 2025
date: "2025-07-12"
venue: "ICML, 2026 · Accepted"
authors: "Joshua Tan, Nicholas Vincent, Katherine Elkins, Magnus Sahlgren, Joseph Low, David Pham, Sampo Pyysalo, Jenia Jitsev"
source_url: "https://openreview.net/forum?id=zN7zY1UVru"
retrieved: "2026-08-13"
content: "full-text"
notes: "OpenAlex W4414691854; CV ref [P27]; Full text from the arXiv HTML rendering of the preprint (https://arxiv.org/html/2507.09296v3)."
---

# If open source is to win, it must go public

## Full text

## Position: If open source is to win, it must go public

Joshua Tan

Affiliation: Public AI Network

Affiliation: Current AI

Correspondence to: josh@publicai.co

Nicholas Vincent

Affiliation: Public AI Network

Affiliation: Simon Fraser University

Correspondence to: nvincent@sfu.ca

Katherine Elkins

Affiliation: Kenyon College

Magnus Sahlgren

Affiliation: AI Sweden

Joseph Low

Affiliation: Public AI Network

Affiliation: Metagov

David Pham

Affiliation: Public AI Network

Affiliation: Simon Fraser University

Sampo Pyysalo

Affiliation: University of Turku, Department of Computing

Jenia Jitsev

Affiliation: LAION

Affiliation: Juelich Supercomputing Center (JSC), Research Center Juelich (FZJ)

####### Abstract

Open source projects have made incredible progress in producing widely usable machine learning models and systems, but open source alone will face challenges in fully democratizing access to AI. Unlike previous generations of open source software, open source and open weight AI models require substantial resources to activate and maintain—e.g., data and compute for pre-training, post-training, and deployment—which only a few actors can currently provide. This position paper argues that open source AI must be complemented by public AI: infrastructure and institutions that ensure models are accessible, sustainable, and governed in the public interest. To achieve the full promise of AI models as prosocial public goods, we need to build public infrastructure to power and deliver open source software and models.

####### Keywords:

open source AI, public AI

### 1 Introduction

Open source, and the ethos of openness, has long served as a counterweight to concentrated control in computing. From Linux to Kubernetes, open collaboration has enabled researchers, companies, and the public at large to build on shared and trustworthy infrastructure (65; 19). But open source has always straddled a line between the emancipatory ideals of the Free Software movement and the strategic goals of firms (80; 40). What appears as a spontaneous gift economy is often scaffolded by sponsorships, employment arrangements, and various private (and public) subsidies. This compromise between community and commerce has proven to be remarkably productive in many software categories such as cloud computing, programming languages, and operating systems. But it is breaking down for the largest foundation models in AI. Such large language models (LLMs) are incredibly expensive to train, raising questions about the longevity of open models (51; 13). Once trained, open source weights alone are inert; without inference, fine-tuning, localization, tooling, and interfaces, they remain unusable to all but a small elite with the capital, compute, and engineering to deploy them (7; 32). And even if deployed, the decentralized nature of open source deployments means that important RLHF and query data can become stranded across many silos. As modern AI ecosystems mature, so too must our expectations about what open source practices can–and cannot–deliver for researchers, for firms, and for the public.

In this paper, we argue that without structural intervention from public institutions, current open source efforts in AI will not democratize access to AI nor provision public goods (in the technical sense of non-rivalrous and non-excludable goods) as comparable open source efforts have done in other categories. This will hurt the machine learning research community. It will hurt startups. It will also undermine the strategic interests of large firms promoting open weight and open source AI. To move forward, we need to build broader public AI ecosystems that ensure open source AI is accessible, trustworthy, and competitive with closed source alternatives.

### 2 Background on open source AI

Here, we briefly summarize open source software in ML and the role of open source AI projects in proving the viability of openness. This is not meant to comprehensively cover all the open software that plays a role in the ML research stack nor cover all successful open source AI projects, of which there have been many.

Open Source in ML: The machine learning community has embraced open source as both a cultural and technical norm. Software libraries like PyTorch (61), Hugging Face Transformers (82), and Diffusers (77) have made advanced ML tools widely accessible. Open source codebases like OpenCLIP (36) and Megatron-LM (70) have made training on supercomputers efficient and large-scale experiments reproducible. Evaluation suites like EleutherAI’s lm-eval-harness (26) and LAION’s CLIP Benchmark (12) have become de-facto industry standards. Researchers routinely release code and models alongside publications, and open pre-trained weights have accelerated innovation and experimentation. Many foundational libraries like NumPy have long been released as open source software, which helped reduce reliance on proprietary scientific software. Relatedly, peer production platforms like Wikimedia projects (including Wikipedia) have long been central to ML training data (38).

Open Source AI Projects: Various open source community communities have been extremely successful in producing AI projects, covering general models, domain specific models, datasets, benchmarks, and more. EleutherAI’s Pile, GPT-NeoX and later Pythia models (25; 5; 3) provide fully open data and GPT models that have been widely used for practical and scientific purposes in language modeling. On the multi-modal front, LAION-400M / 5B image-text, Re-LAION-5B (69; 42), DataComp (24), and LAION-audio-630k (83) projects were critical to providing open data for state-of-the-art vision and audio modeling. This enabled an open end-to-end pipeline for model training, resulting in fully open-source models like openCLIP (11), LAION-CLAP (83) and openMaMMUT (55), as well as fully open-source text-to-image generative models such as Latent and Stable Diffusion (67). Of special note is that at the time of their release, these community-built models matched or outperformed similar models from closed frontier labs. A wide array of other projects, including RWKV (62), BigScience (4), BigCode (46), OpenFold (1), RedPajama and RedPajamas-INCITE (79), OLMo (30), DCLM (45), Pixmo & Molmo (18), and more recently Marin (33) have all contributed to an ecosystem of usable open source AI.

### 3 Challenges for open source AI

Traditional open source software operates on the assumption that the full contribution cycle of use, modification, and redistribution is broadly accessible. While participation has never been perfectly equal, competent contributors can typically engage using commodity hardware and publicly available tooling. For large-scale AI models, this assumption breaks down.11
1

In practice, frontier models require private complements such as compute and energy to be useful. In economic terms, that means that they are “impure public goods” (66; 52) or club goods (29) rather than pure public goods. A classic example of an impure public good is a lighthouse financed by “light dues” (66) imposed on ship owners. The eventual economic model for AI could end up looking like this, though the question of who collects the dues will be salient to whether access to AI is democratized. For an example that more closely captures AI models, we might imagine a library whose collection is non-rival and openly licensed. As the catalog grows by orders of magnitude, it becomes impossible for typical users to find a book without hiring a private “guide” to help. The books remain true public goods, but access to their knowledge is mediated by a search-and-retrieval toll good, so access becomes “club-like” and effectively the library provides information as an impure public good. Although smaller open models can be run locally, meaningful participation in model development requires capital, compute, and data infrastructure that most potential contributors lack.

#### 3.1 Resource challenges

Pretraining Requires Capital and Scale: Modern models are trained on thousands of GPUs over weeks or months (51) and require substantial energy (47). This demands not only access to ever-larger compute clusters–often only available to well-funded corporations or state-supported institutions–but also web-scale datasets, robust engineering teams handling supercomputers, and complex distributed training infrastructure. Data collection is itself an extremely challenging process; merely downloading and storing large data sets (especially for multimodal training) presents a challenge for community contributors using commodity hardware.

Post-training Depends on Private Data and Feedback Loops: The fine-tuning, alignment, tool integration, and prompt orchestration that make models actually useful in practice are often kept closed. While model weights may be public, the systems that give them utility are private. Further, RLHF data generated by usage is typically siloed within individual platforms and not shared with the community, creating a compounding advantage for closed source and closed labs. Even when available, such RLHF and usage data require dedicated teams and additional resources to operationalize.

Inference Isn’t Cheap: Unlike a software library which have comparatively trivial hosting costs, inference at scale (especially for large models) demands ongoing GPU access, orchestration systems, and cost management. And like RLHF, the usage data that flows from inference is hard to aggregate or share across organizations, limiting the ability of open models to improve from failures.

#### 3.2 Licensing challenges

While the costs of training, running, and maintaining a frontier model vastly exceed those of compiling and distributing traditional open source software, the challenges that the open source AI community faces go far beyond resource constraints.

Sharing Data Is Risky and High-Friction: Unclear copyright status, licensing complexities, and jurisdictional uncertainty create significant risk around data reuse, making it hard to share data within the open source community. For labs that train open-source models, it is often difficult to efficiently collect and deploy data from their deployers and inference providers—when there is any agreement at all to share such data.

Licensing is Ambiguous or Fragile: The layperson’s understanding of ”open source” AI is in fact more accurately termed open-weight AI. However, the term “open” in open-weight AI is misleading in two respects. For example, LLaMA’s license contains restrictive terms and explicit revocability which have been widely criticized by the OSS community for being incompatible with established standards for open source (59). These concerns are not isolated, but extend across the industry as a whole. Companies like Meta can stop releasing models or add greater restrictions to future licenses at any time. Terms of service from other major providers impose additional constraints. For example, OpenAI’s terms prohibit using outputs to develop models that compete with OpenAI (57). Anthropic’s usage policy restricts how developer tools like Claude Code can be employed in third-party contexts. Restrictions like these, while commercially understandable, can limit independent evaluation, red-teaming, and reproducibility work upon which the research community depends.

Transparency is Partial and Inconsistent:
More fundamentally, however, releasing weights alone does not provide the transparency that makes open source software auditable and reproducible. With traditional open source, access to the code brings with it the ability to understand how the software works along with the ability to reproduce, modify, and verify any claims about it. With open weights, by contrast, researchers often lack access to training data along with data curation decisions, RLHF procedures, and compute configurations. The “source” in open source once meant access to the complete blueprint, but open weights provide only the finished artifact.

While nonprofit and academic models maintain a commitment to openness, most powerful “open” models are trained by private companies and largely fail to provide details on training data or evaluation procedures. Opacity undermines the core benefits that openness typically provides. Without access to training data and post-training methods, external researchers cannot verify safety claims or fully understand reasons behind model behavior. They can only observe outputs as a form of phenomenological auditing that falls far short of the transparency that makes traditional open source software trustworthy. Attempts at independent evaluation face many structural barriers, and recent work on frontier AI auditing has documented the extent to which current arrangements leave companies “writing their own rules” (8). When labs offer API access for external evaluation, sometimes accompanied by credits worth $1,000 or more, as is encouraged by the EU AI Act’s Code of Practice, auditors may still face usage monitoring and access that can be revoked. Researchers often cannot verify which model version they are testing, whether it matches production systems, or whether safety behaviors differ between evaluation and deployment contexts.

#### 3.3 Governance challenges

Open Does Not Mean Safe: A counterintuitive challenge for open source AI is that openly released models are often less safe than their closed counterparts. Open models are frequently research artifacts rather than deployment-ready systems. Safety work, including red-teaming, alignment tuning, and monitoring for emergent harms, requires sustained investment that volunteer communities and underfunded organizations cannot reliably provide. Furthermore, critical safety decisions occur during pre-training and data curation, not only during RLHF. By the time weights are released, significant portions of the safety-relevant design space have already been fixed.

Closed-source Co-optation: Open source is built on a compromise between community and commerce, but community-contributed evaluations, tooling, datasets, and fine-tuning techniques often accrue value to large firms whose commitment to open source is tenuous at best—in this case the frontier labs who train closed source models. Open source contributors imagine they are building shared infrastructure; in reality, they may be fueling a pipeline that concentrates power (81). Of particular concern to both open source software projects and the broader sphere of open or semi-open knowledge efforts like Wikipedia and StackOverflow is a trend whereby contributions that previously flowed into a commons pool instead flow into private ownership and begin to support a subsidized club good that looks like a public good.

Take the example of coding agents. With the release of more capable models in late 2025 (Gemini 3, Opus 4.5, Codex 5.2), software developers have increasingly adopted LLM coding agents like Claude Code into their workflows (54). For small open source projects, LLM coding agents can substantially accelerate the process of software development (44): not just by assisting with the direct code writing process, but also with the knowledge work around planning, design and reproducing research code (34); or even reproducing data analyses required for investigative journalism (31). With collaborative tasks too, agents are serving as a first-pass quality gate for issue triage (78; 22) or reviewing merge requests (14).

This can seem like a net positive for open source developers who want to contribute to a public good—however, access to the top-performing coding agents is gated through various means. Procuring substantial access to each coding agent often requires paying a hefty monthly subscription to each company, and it must be performed inside the company’s proprietary model harness (e.g. Claude Code) that captures the user’s exact process of software development. Open source model harnesses like OpenCode or OpenHands may provide open alternatives, but then access to the best models must be driven through API access, becoming several times more expensive than the direct subscription options.

Since it is most economically viable for a user to utilize a company’s cheaper subscription offerings through a proprietary model harness, many open source developers are vulnerable to having their knowledge work be captured and transformed into implicit data labour (76). Their user-agent interactions—prompting, responding to the model’s questions, providing detailed feedback, providing source code snippets alongside error messages—and the cycles of iterative refinement which help produce the best quality work (60; 16), also produce highly valuable annotations: annotations that include their preferences, acceptance criteria, problem-solving strategies, ideation processes, research and experimentation procedures, debugging strategies, potentially sensitive API keys, and sensitive documents on their filesystem—all directly captured by private model harnesses, and without clear governance mechanisms for requesting a data deletion.

Access Without Accountability: Proponents of the status quo suggest that AI access is increasingly free of charge. However, as social media has demonstrated, when users do not pay, they are often the product. Interactions can flow into the training pipelines with limited transparency about collection, retention, or use. Users may have little insight into how their data shapes future model behavior, limited ability to opt out of specific uses, and few mechanisms for recourse when their contributions are monetized. In this sense, users may still be paying for AI access, but with their data rather than their dollars.

Expanding Gaps: The AI ecosystem is evolving quickly. What began as token prediction from weights that fit on a local GPU is morphing into AI assistants that blend multi-modal reasoning, access to proprietary tools, and complex orchestration layers. As system complexity grows, the gap between “available weights” and “usable systems” widens. While there has been massive progress in terms of what can be run locally on consumer hardware (27; 56), these models still lack post-training alignment, retrieval augmentation, tool use integration, usage analytics, uptime guarantees, and continual updates that distinguish private, hosted services from merely downloadable weights.

Collectively, these challenges suggest that open source AI faces not a failure of values but of structure. The open source model, which flourished in an earlier era of low-cost computation and interoperable standards, is no longer sufficient on its own. To deliver on the promise of accessible and democratic AI (15), we must build new public AI infrastructures that can provision and govern the full model lifecycle beyond just the first training checkpoint.

### 4 Position Statement

We assert: open source AI, as currently practiced, will not by itself democratize access to AI or provision public goods as comparable open source efforts have done in other software categories. Instead, we propose that open source AI must be embedded within a broader vision of public AI, defined by the following principles:

- •

Public Support: There must be public funding and infrastructure for inference, deployment, post-training, and data, beyond important pretraining.

- •

Public Access: Everyone—-researchers lacking resources, civic technologists, local communities outside of Big Tech—-must be enabled to build, adapt, and use competitive models.

- •

Public Accountability: Institutions accountable to the public—-governments, national labs, public utilities, universities, and nonprofits—must provision, host, and maintain models and related infrastructure.

- •

Private Commitments: Private actors must be encouraged (or required) to make commitments around openness, safety, and community control.

Public AI understands AI as a form of public infrastructure—think highways, libraries, water, or electricity. It is closely related to other forms of digital public infrastructure (DPI) including existing public digital stacks for identity, payments, and data exchange (37; 71; 73).

### 5 Examples of public AI

Public AI is not a theoretical aspiration. Around the world, countries are already experimenting with concrete strategies for building and deploying large-scale AI systems in the public interest. We cover some examples of ongoing public AI efforts below:

Creating New Foundation Models: Faced with limits of reproducibility of important foundation model types, various organizations turned to public infrastructure and funds to create open versions of closed foundation models. Important examples are: (i) work done by BigScience initiative (spearheaded by HuggingFace), which trained BLOOM to replicate GPT class models on public supercomputer Jean Zay (IDRIS, France); (ii) non-profit organization LAION, which composed datasets and trained language-vision openCLIP and language-audio CLAP models on various public supercomputers like JUWELS Booster (JSC, Germany) or Leonardo (CINECA, Italy); (iii) EleutherAI in US which collected Pile and trained models like GPT-NeoX-20B and Pythia, teamed up with various organizations including LAION on US public funded supercomputer SUMMIT (Oak Ridge Lab). Those self-organized efforts by grassroot communities executed on public infrastructure and backed up by public funds triggered a huge wave of follow-up open-source work including Stable Diffusion, RedPajama, FineWeb, DataComp, DCLM and so on, showing the potential of proper usage of public resources.

Most successful LLM efforts have primarily focused on high-resource languages (especially English), motivating efforts to create open-source models targeting other languages. For example
CroissantLLM (21),
FinGPT (49),
GPT-SW3 (20),
Minerva (58),
NorMistral (68)
and
Poro (48)
in Europe have been trained primarily using public resources via compute grants from EuroHPC and national HPC organizations. Although these efforts succeeded in creating models with capabilities for specific languages, they also fragmented limited public resources to a point where no individual effort has had sufficient compute to create frontier models. Consequently, European efforts are increasingly focusing on creating broadly multilingual models such as
EuroLLM (50),
Salamandra (28),
Teuken (2) and
TildeOpen. The EU is also funding efforts to create open multilingual datasets (17) and models. The largest current project in the latter category is OpenEuroLLM, a consortium of 20 European institutions developing fully open foundation models. The project has so far released many smaller reference baseline models and was recently given access to EuroHPC strategic compute resources, providing it with compute totaling over 10M GPUh on four
major European HPC systems (Leonardo, LUMI, JUPITER and MareNostrum5). While the quality of these models are still unremarkable by the standards of model families like Qwen, DeepSeek, gpt-oss, Nemotron, or Kimi, they reflect a substantial investment in public AI in Europe that demonstrate the possibility of sustaining a genuinely open commons and democratic governance over how shared resources are used.

Subsidizing Inference for Public Access: Public infrastructure initiatives are emerging to address the computational barriers that limit access to advanced AI models. For example, the Public AI Inference Utility, a nonprofit organization, coordinates donated compute resources across multiple countries to provide free inference access for public and sovereign models (63). As the primary deployer for models such as Switzerland’s Apertus, it illustrates how distributed public infrastructure can sustain model accessibility beyond initial release. By pooling computational resources from diverse donors, the utility reduces the financial barriers to deploying and maintaining open models at scale. Initiatives such as the National Deep Inference Fabric (NDIF) provides researchers with shared access to open-weight models (23) and enables remote experimentation on model internals through standardized tools, addressing the “activation gap” between publicly available weights and usable research capabilities. This infrastructure allows researchers without substantial computational resources to conduct interpretability studies, fine-tuning experiments, and other investigations that require direct model access. These initiatives demonstrate complementary strategies for subsidizing inference both for broad public access and for specialized researchers.

Auditing Standards and Benchmarks: Public AI can mandate audit access as a condition of public funding, as well as maintaining versioned model checkpoints and separating infrastructure providers from the entities being evaluated. The recently launched AI Verification and Evaluation Research Institute (AVERI) has proposed a framework of “AI Assurance Levels” that illustrates a vision of public AI auditing infrastructure (8). Level 1 is similar to current practice and involves limited third-party testing with constrained access. Level 4, on the other hand, would provide “treaty grade” assurance sufficient for international agreements on AI safety. Current private auditing arrangements largely operate at Level 1, but public AI infrastructure could enable Level 3-4 assurance as a baseline expectation with mandated access, versioned checkpoints, and separation between infrastructure providers and evaluated entities. Public AI initiatives are also developing comprehensive evaluation frameworks that address multilingual and multicultural capabilities. For example, SEA-HELM (Southeast Asian Holistic Evaluation of Language Models), developed in collaboration with AI Singapore, provides a rigorous evaluation suite emphasizing Southeast Asian languages across five core pillars: NLP Classics, LLM-specifics, SEA Linguistics, SEA Culture, and Safety (10). Supporting Filipino, Indonesian, Tamil, Thai, and Vietnamese, SEA-HELM demonstrates how public AI infrastructure can establish evaluation standards that go beyond English-centric benchmarks to ensure models serve diverse linguistic and cultural communities.

New approaches are still being developed, including the Airbus for AI (74; 72) and CERN for AI (9; 39) proposals for multilateral visions of public AI.

### 6 Alternative Views

We recognize a number of serious alternative views that challenge the necessity or feasibility of public AI.

#### 6.1 View 1: The Market Is Working. Let OpenAI and Meta Lead.

Many believe that the private sector is successfully scaling AI access. OpenAI, Meta, Mistral, and DeepSeek have made advanced models available cheaply or for free. Proprietary labs have shown tremendous speed and capability in model iteration, evaluation, and deployment. Their models are at the performance frontier, their user experience is polished, and their costs are rapidly dropping.

Response: Access is not governance, and it is not sovereignty. These systems remain opaque and subject to unilateral revocation. For example, it has been reported that LLaMA 4 will be the final model release in the LLaMA family, with Meta shifting their focus towards closed weight models (75). The ability to use a chatbot today also does not ensure access to trustworthy, auditable systems tomorrow. As another example, Alibaba Qwen removed access to the free version of Qwen Code in April 2026 (43). Public AI is not about replacing private labs, but about ensuring that there are durable, open, and accountable systems aligned with public needs and values. For example, the USA’s National Deep Inference Fabric was designed to provide democratic access to open-weight models (23), while Sweden’s GPT-SW3 (20) was initially trained to address ChatGPT’s poor performance in Swedish and other Scandinavian languages.

It is also worth noting that Meta and other corporate-OSS builders stand to benefit if open source inference becomes publicly funded: the cheaper the inference, the more value accrues to the application layer.

#### 6.2 View 2: Open Source Will Win Eventually. Just Be Patient.

This view argues that the open source ecosystem is improving rapidly (51) and will eventually produce models on par with or better than proprietary models. The release of high-quality weights (e.g., Mistral, DeepSeek, Zephyr), coupled with open fine-tuning libraries and model merging techniques, suggests that community-driven innovation will outcompete closed models in the long run.

Response: Open source progress has been remarkable. There have been many academic, nonprofit, and community-led efforts to train foundation models. However, most of the strongest and widely used open models today were pre-trained by well-capitalized private companies: compare LLaMA 3.1-8B’s 6M monthly downloads on Hugging Face with EleutherAI Pythia’s 900k and OLMo 3-7B’s 170k (as of late Jan 2026) (35). LLaMA is also broadly adopted in downstream models like VLMs (eg, LLaMA3-Nemotron, etc.), while the nonprofit versions lack comparable adoption as components. Notable exceptions that confirm the rule are models by LAION like language-audio CLAP (14M monthly downloads as of Jan 2026) and openCLIP variants (per model, between 1M-2M downloads per month, exceeding >60M all time downloads). LAION was backed up by public infrastructure like supercomputers and storage in its work, and evidence shows it is in such cases possible to be on par with private entities. Open options also do not compare well with the adoption seen by OpenAI and Anthropic—not to mention the potential for extraordinary adoption as proprietary models are incorporated into product platforms like Google Search or Microsoft Office. Open source may or may not be beat by closed source, but additional public investment is very unlikely to hurt and may prove critical to future sustainability and competitiveness. Public AI also ensures that open source models remain accessible, trustworthy, and responsive to broad public needs rather than to the incentives of a single commercial sponsor.

#### 6.3 View 3: OSS + Hosting Already Works.

Why add bureaucracy? A practical open source ecosystem is already in place. Open models are hosted via Hugging Face, Replicate, and Open Router. Inference is affordable. User-facing products are emerging. Why burden this with new governance structures or public spending?

Response: Like view 1, this view confuses current availability with long-term stability. Most current deployments rely on ephemeral commercial hosting or terms that can be revoked. The fragility of the OSS+hosting stack is exemplified by the LLaMA license and the risk of unilateral pullback from companies like Meta. Public AI does not aim to replace this ecosystem but to underwrite it. This already happens, especially for academic and nonprofit projects: for example, national labs in the US use EleutherAI’s GPT-NeoX and have provided some support for the project, while the French National Center for Scientific Research supported the BigScience project, which trained BLOOM on Jean Zay, a French public supercomputer (4). LAION’s work on openCLIP (69; 11; 55) was also enabled and supported by public compute and storage backed by the grants from the Gauss Center for Supercomputing at the Juelich Supercomputing Center, a public research facility in Germany hosting publicly funded supercomputers.

#### 6.4 View 4: Regulation Is a Better Tool Than Public Investment.

Instead of building new infrastructure, governments can simply regulate AI development—imposing transparency requirements, safety standards, and licensing constraints. Regulatory frameworks such as the EU AI Act and export controls on GPU sales aim to shape the AI landscape through law rather than through investment.

Response: Regulation is essential, but it is not sufficient. It can curb harmful behavior but does little to guarantee access, usability, or equitable participation. Public AI is proactive: it builds capabilities and institutions that embody public values from the outset. Rather than rely solely on constraints imposed on private actors, public AI enables public-purpose development from the ground up. This complements regulation by demonstrating and institutionalizing best practices. For example, Canada’s SCALE AI project funds both regulatory and capability-building efforts, providing shared infrastructure for data and training.

#### 6.5 View 5: Public AI Will Be Inefficient and Capture-Prone.

There is a long history of inefficient or mismanaged public-sector technology projects. Bureaucracies move slowly, are vulnerable to capture, and can’t attract talent (53). Why should we expect public AI to be different?

Response: This is a valid concern. However, well-governed public institutions do exist and have produced extraordinary technological advances—from GPS to the internet to the Hubble Space Telescope. Our position is not that governments should necessarily divert funds from other priorities toward AI, but rather that the public money already being spent on AI (for example, on procurement of AI goods and services) should be structured to better serve the public interest. Moreover, public AI need not be synonymous with government-only models. Public funding could support existing nonprofit activities—even OpenAI once contemplated asking for public funding (41). Proposals like Airbus for AI (72) envision a hybrid, multilateral structure of many national entities, each organized as public utilities. Successful examples like ERC, CERN, and W3C show that public AI can be designed to resist capture and reward quality.

### 7 Technical and Societal Implications

Public AI shifts the focus of machine learning research away from monolithic frontier labs and toward shared infrastructure, cooperative development, and inclusive deployment. For the ML community, this has far-reaching implications:

- •

For ML Researchers: Shared model libraries and pooled inference capacity democratize frontier experimentation. When models are shared, researchers can access and intervene on the internals of LLMs and other models without the cost or complexity of hosting their own hardware (6; 23). They can access more of the RLHF and query data that is essential to frontier model capability research. Public AI also reduces fragility and promotes reproducibility across labs.

- •

For Non-CS Fields: Domains like healthcare, education, and law increasingly require high-quality models. Public AI enables domain experts to adapt systems to local needs without relying on private APIs or black-box deployments.

- •

For Open Source Ecosystems: Many contributors now work without guarantees that their outputs will remain in the commons. Public AI ensures their efforts resist private capture and support genuinely open systems.

- •

For Governments and Funders: Public AI can serve as a key plank of digital sovereignty and national innovation strategies (64). Governments can focus investment on shared infrastructure and safety rather than competing on consumer UX.

- •

For the Broader Public: Public AI supports democratic accountability and contestability. It embeds collective input in how powerful systems are developed and used.

### 8 Conclusion

The machine learning community should not conflate open source with public good. We argue for a future in which open source AI is nested within public AI infrastructures: institutions and commitments that activate, sustain, and distribute AI systems for the public benefit.

If the goal is to enable a diversity of actors to build and deploy capable models, then we must move beyond a romantic view of open source and begin investing in AI as public infrastructure. If open source is to win, it must go public.

### Acknowledgements

We would like to thank Stella Biderman, Nathan Lambert, Imanol Schlag, and many others for helpful comments in the writing of this paper.

JJ acknowledges funding by EU Horizon under grant no. 101214398 (ELLIOT) and co-funding by EU from Digital Europe Programme under grant no. 101195233 (openEuroLLM), co-funding from EU under Digital Europe Programme under grant no. 101198470 (LLMs4EU), from EuroHPC Joint Undertaking Programme under grant no. 101182737 (MINERVA), and funding by the German Federal Ministry of Research, Technology and Space (BMFTR) under the grant 16HPC117K (MINERVA).

### References

- Ahdritz et al. (2024)
G. Ahdritz, N. Bouatta, C. Floristean, S. Kadyan, Q. Xia, W. Gerecke, T. J. O’Donnell, D. Berenberg, I. Fisk, N. Zanichelli, B. Zhang, A. Nowaczynski, B. Wang, M. M. Stepniewska-Dziubinska, S. Zhang, A. Ojewole, M. E. Guney, S. Biderman, A. M. Watkins, S. Ra, P. R. Lorenzo, L. Nivon, B. Weitzner, Y. A. Ban, S. Chen, M. Zhang, C. Li, S. L. Song, Y. He, P. K. Sorger, E. Mostaque, Z. Zhang, R. Bonneau, and M. AlQuraishi

OpenFold: retraining AlphaFold2 yields new insights into its learning mechanisms and capacity for generalization.

Nature Methods 21 (8), pp. 1514–1524 (en).

Note: Publisher: Nature Publishing Group

External Links: ISSN 1548-7105,
Link,
Document

Cited by: §2.

- Ali et al. (2025)
M. Ali, M. Fromm, K. Thellmann, J. Ebert, A. A. Weber, R. Rutmann, C. Jain, M. Lübbering, D. Steinigen, J. Leveling, K. Klug, J. S. Buschhoff, L. Jurkschat, H. Abdelwahab, B. J. Stein, K. Sylla, P. Denisov, N. Brandizzi, Q. Saleem, A. Bhowmick, L. Helmer, C. John, P. O. Suarez, M. Ostendorff, A. Jude, L. Manjunath, S. Weinbach, C. Penke, O. Filatov, F. Barth, P. Mirza, L. Weber, I. Wendler, R. Sifa, F. Küch, A. Herten, R. Jäkel, G. Rehm, S. Kesselheim, J. Köhler, and N. Flores-Herr

Teuken-7b-base & teuken-7b-instruct: towards european llms.

External Links: 2410.03730,
Link

Cited by: §5.

- Biderman et al. (2023)
S. Biderman, H. Schoelkopf, Q. G. Anthony, H. Bradley, K. O’Brien, E. Hallahan, M. A. Khan, S. Purohit, U. S. Prashanth, E. Raff, et al.

Pythia: a suite for analyzing large language models across training and scaling.

In International Conference on Machine Learning,

pp. 2397–2430.

Cited by: §2.

- BigScience Workshop et al. (2023)
BigScience Workshop, T. L. Scao, A. Fan, C. Akiki, E. Pavlick, S. Ilić, D. Hesslow, R. Castagné, A. S. Luccioni, F. Yvon, M. Gallé, J. Tow, A. M. Rush, S. Biderman, A. Webson, P. S. Ammanamanchi, T. Wang, B. Sagot, N. Muennighoff, A. V. d. Moral, O. Ruwase, R. Bawden, S. Bekman, A. McMillan-Major, I. Beltagy, H. Nguyen, L. Saulnier, S. Tan, P. O. Suarez, V. Sanh, H. Laurençon, Y. Jernite, J. Launay, M. Mitchell, C. Raffel, A. Gokaslan, A. Simhi, A. Soroa, A. F. Aji, A. Alfassy, A. Rogers, A. K. Nitzav, C. Xu, C. Mou, C. Emezue, C. Klamm, C. Leong, D. v. Strien, D. I. Adelani, D. Radev, E. G. Ponferrada, E. Levkovizh, E. Kim, E. B. Natan, F. D. Toni, G. Dupont, G. Kruszewski, G. Pistilli, H. Elsahar, …, and T. Wolf

BLOOM: A 176B-Parameter Open-Access Multilingual Language Model.

arXiv.

Note: arXiv:2211.05100 [cs]

External Links: Link,
Document

Cited by: §2,
§6.3.

- Black et al. (2022)
S. Black, S. Biderman, E. Hallahan, Q. Anthony, L. Gao, L. Golding, H. He, C. Leahy, K. McDonell, J. Phang, M. Pieler, U. S. Prashanth, S. Purohit, L. Reynolds, J. Tow, B. Wang, and S. Weinbach

GPT-NeoX-20B: An Open-Source Autoregressive Language Model.

arXiv.

Note: arXiv:2204.06745 [cs]

External Links: Link,
Document

Cited by: §2.

- Bommasani et al. (2021)
R. Bommasani, D. A. Hudson, E. Adeli, and et al.

On the opportunities and risks of foundation models.

arXiv preprint.

External Links: 2108.07258,
Link

Cited by: 1st item.

- Bommasani et al. (2024)
R. Bommasani, S. Kapoor, K. Klyman, S. Longpre, A. Ramaswami, D. Zhang, M. Schaake, D. E. Ho, A. Narayanan, and P. Liang

Considerations for governing open foundation models.

Science 386 (6718), pp. 151–153 (en).

External Links: ISSN 0036-8075, 1095-9203,
Link,
Document

Cited by: §1.

- Brundage et al. (2026)
M. Brundage, N. Dreksler, A. Homewood, S. McGregor, et al.

Frontier ai auditing: toward rigorous third-party assessment of safety and security practices at leading ai companies.

arXiv preprint arXiv:2601.11699.

Cited by: §3.2,
§5.

- [9]
CAIRNE

Confederation of Laboratories for Artificial Intelligence Research in Europe.

External Links: Link

Cited by: §5.

- Center for Research on Foundation Models (2025)
Center for Research on Foundation Models

SEA-HELM: southeast asian holistic evaluation of language models.

Note: https://crfm.stanford.edu/helm/seahelm/latest/A collaboration with AI Singapore

Cited by: §5.

- Cherti et al. (2023)
M. Cherti, R. Beaumont, R. Wightman, M. Wortsman, G. Ilharco, C. Gordon, C. Schuhmann, L. Schmidt, and J. Jitsev

Reproducible scaling laws for contrastive language-image learning.

In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition,

pp. 2818–2829.

Cited by: §2,
§6.3.

- Cherti and Beaumont (2022)
CLIP benchmark

External Links: Document,
Link

Cited by: §2.

- Choksi et al. (2025)
M. Z. Choksi, I. Mandel, and S. Benthall

The brief and wondrous life of open models.

In Proceedings of the 2025 ACM Conference on Fairness, Accountability, and Transparency,

pp. 3224–3240.

Cited by: §1.

- Cihan et al. (2025)
U. Cihan, V. Haratian, A. İçöz, M. K. Gül, Ö. Devran, E. F. Bayendur, B. M. Uçar, and E. Tüzün

Automated Code Review in Practice.

In 2025 IEEE/ACM 47th International Conference on Software Engineering: Software Engineering in Practice (ICSE-SEIP),

pp. 425–436.

External Links: ISSN 2832-7659,
Document

Cited by: §3.3.

- Collective Intelligence Project (2024)
Collective Intelligence Project

A Roadmap to Democratic AI.

Technical report

Collective Intelligence Project.

External Links: Link

Cited by: §3.3.

- Dai et al. (2025)
D. Dai, M. Liu, A. Li, J. Cao, Y. Wang, C. Wang, X. Peng, and Z. Zheng

FeedbackEval: A Benchmark for Evaluating Large Language Models in Feedback-Driven Code Repair Tasks.

arXiv.

External Links: Document

Cited by: §3.3.

- de Gibert et al. (2024)
O. de Gibert, G. Nail, N. Arefyev, M. Bañón, J. van der Linde, S. Ji, J. Zaragoza-Bernabeu, M. Aulamo, G. Ramírez-Sánchez, A. Kutuzov, S. Pyysalo, S. Oepen, and J. Tiedemann

A new massive multilingual dataset for high-performance language technologies.

In Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024),

pp. 1116–1128.

Cited by: §5.

- Deitke et al. (2025)
M. Deitke, C. Clark, S. Lee, R. Tripathi, Y. Yang, J. S. Park, M. Salehi, N. Muennighoff, K. Lo, L. Soldaini, et al.

Molmo and pixmo: open weights and open data for state-of-the-art vision-language models.

In Proceedings of the Computer Vision and Pattern Recognition Conference,

pp. 91–104.

Cited by: §2.

- Eghbal (2016)
N. Eghbal

Roads and bridges: the unseen labor behind our digital infrastructure.

Technical report

Ford Foundation.

External Links: Link

Cited by: §1.

- Ekgren et al. (2024)
A. Ekgren, A. C. Gyllensten, F. Stollenwerk, J. Öhman, T. Isbister, E. Gogoulou, F. Carlsson, A. Heiman, J. Casademont, and M. Sahlgren

GPT-SW3: An Autoregressive Language Model for the Nordic Languages.

arXiv.

Note: arXiv:2305.12987 [cs]

External Links: Link,
Document

Cited by: §5,
§6.1.

- Faysse et al. (2025)
M. Faysse, P. Fernandes, N. M. Guerreiro, A. Loison, D. M. Alves, C. Corro, N. Boizard, J. Alves, R. Rei, P. H. Martins, A. B. Casademunt, F. Yvon, A. F. T. Martins, G. Viaud, C. Hudelot, and P. Colombo

CroissantLLM: a truly bilingual french-english language model.

External Links: 2402.00786,
Link

Cited by: §5.

- Feiglin and Dar (2026)
J. Feiglin and G. Dar

SastBench: A Benchmark for Testing Agentic SAST Triage.

arXiv.

External Links: 2601.02941,
Document

Cited by: §3.3.

- Fiotto-Kaufman et al. (2025)
J. Fiotto-Kaufman, A. R. Loftus, E. Todd, J. Brinkmann, K. Pal, D. Troitskii, M. Ripa, A. Belfki, C. Rager, C. Juang, A. Mueller, S. Marks, A. S. Sharma, F. Lucchetti, N. Prakash, C. Brodley, A. Guha, J. Bell, B. C. Wallace, and D. Bau

NNsight and NDIF: democratizing access to open-weight foundation model internals.

In International Conference on Learning Representations (ICLR),

External Links: Link

Cited by: §5,
§6.1,
1st item.

- Gadre et al. (2023)
S. Y. Gadre, G. Ilharco, A. Fang, J. Hayase, G. Smyrnis, T. Nguyen, R. Marten, M. Wortsman, D. Ghosh, J. Zhang, et al.

Datacomp: in search of the next generation of multimodal datasets.

Advances in Neural Information Processing Systems 36, pp. 27092–27112.

Cited by: §2.

- Gao et al. (2020)
L. Gao, S. Biderman, S. Black, L. Golding, T. Hoppe, C. Foster, J. Phang, H. He, A. Thite, N. Nabeshima, et al.

The pile: an 800gb dataset of diverse text for language modeling.

arXiv preprint arXiv:2101.00027.

Cited by: §2.

- Gao et al. (2024)
L. Gao, J. Tow, B. Abbasi, S. Biderman, S. Black, A. DiPofi, C. Foster, L. Golding, J. Hsu, A. Le Noac’h, H. Li, K. McDonell, N. Muennighoff, C. Ociepa, J. Phang, L. Reynolds, H. Schoelkopf, A. Skowron, L. Sutawika, E. Tang, A. Thite, B. Wang, K. Wang, and A. Zou

The language model evaluation harness.

Zenodo.

External Links: Document,
Link

Cited by: §2.

- Gerganov (2023)
G. Gerganov

Ggml-org/llama.cpp.

ggml.

Note: original-date: 2023-03-10T18:58:00Z

External Links: Link

Cited by: §3.3.

- Gonzalez-Agirre et al. (2025)
A. Gonzalez-Agirre, M. Pàmies, J. Llop, I. Baucells, S. D. Dalt, D. Tamayo, J. J. Saiz, F. Espuña, J. Prats, J. Aula-Blasco, M. Mina, I. Pikabea, A. Rubio, A. Shvets, A. Sallés, I. Lacunza, J. Palomar, J. Falcão, L. Tormo, L. Vasquez-Reina, M. Marimon, O. Pareras, V. Ruiz-Fernández, and M. Villegas

Salamandra technical report.

External Links: 2502.08489,
Link

Cited by: §5.

- Gries and Naudé (2022)
T. Gries and W. Naudé

Modelling artificial intelligence in economics.

Journal for labour market research 56 (1), pp. 12.

Cited by: footnote 1.

- Groeneveld et al. (2024)
D. Groeneveld, I. Beltagy, E. Walsh, A. Bhagia, R. Kinney, O. Tafjord, A. H. Jha, H. Ivison, I. Magnusson, Y. Wang, S. Arora, D. Atkinson, R. Authur, K. R. Chandu, A. Cohan, J. Dumas, Y. Elazar, Y. Gu, J. Hessel, T. Khot, W. Merrill, J. Morrison, N. Muennighoff, A. Naik, C. Nam, M. E. Peters, V. Pyatkin, A. Ravichander, D. Schwenk, S. Shah, W. Smith, E. Strubell, N. Subramani, M. Wortsman, P. Dasigi, N. Lambert, K. Richardson, L. Zettlemoyer, J. Dodge, K. Lo, L. Soldaini, N. A. Smith, and H. Hajishirzi

OLMo: accelerating the science of language models.

In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),

Bangkok, Thailand, pp. 15789–15809.

External Links: Document,
Link

Cited by: §2.

- Hagar (2026)
N. Hagar

Coding Agents for Investigative Journalism.

External Links: Link

Cited by: §3.3.

- HAI (2024)
S. HAI

AI Index: State of AI in 13 Charts.

(en).

External Links: Link

Cited by: §1.

- Hall et al. (2025)
D. Hall, A. Ahmed, C. Chou, A. Garg, R. Kuditipudi, W. Held, N. Ravi, H. Shandilya, J. Wang, J. Bolton, S. Karamcheti, S. Kotha, T. Lee, N. Liu, J. Niklaus, A. Ramaswami, K. Salahi, K. Wen, C. H. Wong, S. Yang, I. Zhou, and P. LiangIntroducing marin: an open lab for building foundation models(Website)

Note: Accessed: 2025-07-11

External Links: Link

Cited by: §2.

- Hua et al. (2025)
T. Hua, H. Hua, V. Xiang, B. Klieger, S. T. Truong, W. Liang, F. Sun, and N. Haber

ResearchCodeBench: Benchmarking LLMs on Implementing Novel Machine Learning Research Code.

In The Thirty-ninth Annual Conference on Neural Information Processing Systems Datasets and Benchmarks Track,

Cited by: §3.3.

- Hugging Face (2026)
Hugging Face

Model download statistics on hugging face hub (llama 3.1, olmo 2-7b, pythia).

Note: https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct,https://huggingface.co/allenai/Olmo-3-7B-Instruct,https://huggingface.co/EleutherAI/pythia-70m-dedupedAccessed Jan 29, 2026

Cited by: §6.2.

- Ilharco et al. (2021)
OpenCLIP

External Links: Document,
Link

Cited by: §2.

- Institute for Innovation and Public Purpose, UCL (2026)
Institute for Innovation and Public Purpose, UCL

DPI Map.

Note: Accessed: 2026-01-16

External Links: Link

Cited by: §4.

- Johnson et al. (2024)
I. Johnson, L. Kaffee, and M. Redi

Wikimedia data for ai: a review of wikimedia datasets for nlp tasks and ai-assisted editing.

arXiv preprint arXiv:2410.08918.

Cited by: §2.

- Juijn et al. (2024)
D. Juijn, B. Pataki, A. Petropoulos, and M. Reddel

The EU’s seat at the table.

Technical report

Centre for Future Generations (en).

External Links: Link

Cited by: §5.

- Kelty (2008)
C. M. Kelty

Two Bits: The Cultural Significance of Free Software.

Duke University Press.

External Links: ISBN 978-0-8223-8900-2 978-0-8223-4242-7,
Link,
Document

Cited by: §1.

- Klein (2021)
E. Klein

Transcript: Ezra Klein Interviews Sam Altman.

The New York Times (en-US).

External Links: ISSN 0362-4331,
Link

Cited by: §6.5.

- LAION (2024)
LAION

Releasing re-laion 5b: transparent iteration on laion-5b with additional safety fixes.

Note: https://laion.ai/blog/relaion-5b/Accessed: 30 aug, 2024

Cited by: §2.

- Lanz (2026)
J. A. Lanz

Free Qwen Is Dead: Alibaba Shuts Down Qwen Code Free Tier.

External Links: Link

Cited by: §6.1.

- Lewis (2025)
C. Lewis

The Unexpected Effectiveness of One-Shot Decompilation with Claude.

External Links: Link

Cited by: §3.3.

- Li et al. (2024)
J. Li, A. Fang, G. Smyrnis, M. Ivgi, M. Jordan, S. Gadre, H. Bansal, E. Guha, S. Keh, K. Arora, S. Garg, R. Xin, N. Muennighoff, R. Heckel, J. Mercat, M. Chen, S. Gururangan, M. Wortsman, A. Albalak, Y. Bitton, M. Nezhurina, A. Abbas, C. Hsieh, D. Ghosh, J. Gardner, M. Kilian, H. Zhang, R. Shao, S. Pratt, S. Sanyal, G. Ilharco, G. Daras, K. Marathe, A. Gokaslan, J. Zhang, K. Chandu, T. Nguyen, I. Vasiljevic, S. Kakade, S. Song, S. Sanghavi, F. Faghri, S. Oh, L. Zettlemoyer, K. Lo, A. El-Nouby, H. Pouransari, A. Toshev, S. Wang, D. Groeneveld, L. Soldaini, P. W. Koh, J. Jitsev, T. Kollar, A. G. Dimakis, Y. Carmon, A. Dave, L. Schmidt, and V. Shankar

Datacomp-lm: in search of the next generation of training sets for language models.

Advances in Neural Information Processing Systems 37, pp. 14200–14282.

Cited by: §2.

- Li et al. (2023)
R. Li, L. B. Allal, Y. Zi, N. Muennighoff, D. Kocetkov, C. Mou, M. Marone, C. Akiki, J. Li, J. Chim, Q. Liu, E. Zheltonozhskii, T. Y. Zhuo, T. Wang, O. Dehaene, M. Davaadorj, J. Lamy-Poirier, J. Monteiro, O. Shliazhko, N. Gontier, N. Meade, A. Zebaze, M. Yee, L. K. Umapathi, J. Zhu, B. Lipkin, M. Oblokulov, Z. Wang, R. Murthy, J. Stillerman, S. S. Patel, D. Abulkhanov, M. Zocca, M. Dey, Z. Zhang, N. Fahmy, U. Bhattacharyya, W. Yu, S. Singh, S. Luccioni, P. Villegas, M. Kunakov, F. Zhdanov, M. Romero, T. Lee, N. Timor, J. Ding, C. Schlesinger, H. Schoelkopf, J. Ebert, T. Dao, M. Mishra, A. Gu, J. Robinson, C. J. Anderson, B. Dolan-Gavitt, D. Contractor, S. Reddy, D. Fried, D. Bahdanau, Y. Jernite, C. M. Ferrandis, S. Hughes, T. Wolf, A. Guha, L. v. Werra, and H. d. Vries

StarCoder: may the source be with you!.

arXiv.

Note: arXiv:2305.06161 [cs]

External Links: Link,
Document

Cited by: §2.

- Luccioni et al. (2024)
S. Luccioni, Y. Jernite, and E. Strubell

Power hungry processing: watts driving the cost of ai deployment?.

In Proceedings of the 2024 ACM conference on fairness, accountability, and transparency,

pp. 85–99.

Cited by: §3.1.

- Luukkonen et al. (2025)
R. Luukkonen, J. Burdge, E. Zosa, A. Talman, V. Komulainen, V. Hatanpää, P. Sarlin, and S. Pyysalo

Poro 34B and the blessing of multilinguality.

In Proceedings of the Joint 25th Nordic Conference on Computational Linguistics and 11th Baltic Conference on Human Language Technologies (NoDaLiDa/Baltic-HLT 2025), R. Johansson and S. Stymne (Eds.),

pp. 367–382.

Cited by: §5.

- Luukkonen et al. (2023)
R. Luukkonen, V. Komulainen, J. Luoma, A. Eskelinen, J. Kanerva, H. Kupari, F. Ginter, V. Laippala, N. Muennighoff, A. Piktus, T. Wang, N. Tazi, T. Scao, T. Wolf, O. Suominen, S. Sairanen, M. Merioksa, J. Heinonen, A. Vahtola, S. Antao, and S. Pyysalo

FinGPT: large generative models for a small language.

In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing,

pp. 2710–2726.

Cited by: §5.

- Martins et al. (2025)
P. H. Martins, J. Alves, P. Fernandes, N. M. Guerreiro, R. Rei, A. Farajian, M. Klimaszewski, D. M. Alves, J. Pombal, N. Boizard, M. Faysse, P. Colombo, F. Yvon, B. Haddow, J. G. C. de Souza, A. Birch, and A. F. T. Martins

EuroLLM-9b: technical report.

External Links: 2506.04079,
Link

Cited by: §5.

- Maslej et al. (2025)
N. Maslej, L. Fattorini, R. Perrault, Y. Gil, V. Parli, N. Kariuki, E. Capstick, A. Reuel, E. Brynjolfsson, J. Etchemendy, K. Ligett, T. Lyons, J. Manyika, J. C. Niebles, Y. Shoham, R. Wald, T. Walsh, A. Hamrah, L. Santarlasci, J. B. Lotufo, A. Rome, A. Shi, and S. Oak

Artificial intelligence index report 2025.

External Links: 2504.07139,
Link

Cited by: §1,
§3.1,
§6.2.

- Mazzucato et al. (2024)
M. Mazzucato, D. Eaves, and B. Vasconcellos

Digital public infrastructure and public value: what is ’public’ about dpi?.

Working Paper

Technical Report IIPP WP 2024-05, UCL Institute for Innovation and Public Purpose.

External Links: Link

Cited by: footnote 1.

- Mazzucato (2013)
M. Mazzucato

The entrepreneurial state: debunking public vs. private sector myths.

Anthem Press.

External Links: ISBN 9780857282521

Cited by: §6.5.

- Menlo Ventures (2025)
Menlo Ventures

2025: The State of Generative AI in the Enterprise.

Cited by: §3.3.

- Nezhurina et al. (2025)
M. Nezhurina, T. Porian, G. Puccetti, T. Kerssies, R. Beaumont, M. Cherti, and J. Jitsev

Scaling laws for robust comparison of open foundation language-vision models and datasets.

In The Thirty-ninth Annual Conference on Neural Information Processing Systems,

External Links: Link

Cited by: §2,
§6.3.

- Ollama Team (2025)
Ollama Team

Ollama.

Ollama.

Note: original-date: 2023-06-26T19:39:32Z

External Links: Link

Cited by: §3.3.

- OpenAI (2025)
OpenAI

Terms of use.

Note: Accessed January 2026

External Links: Link

Cited by: §3.2.

- Orlando et al. (2024)
R. Orlando, L. Moroni, P. Huguet Cabot, S. Conia, E. Barba, S. Orlandini, G. Fiameni, and R. Navigli

Minerva LLMs: the first family of large language models trained from scratch on Italian data.

In Proceedings of the Tenth Italian Conference on Computational Linguistics (CLiC-it 2024), F. Dell’Orletta, A. Lenci, S. Montemagni, and R. Sprugnoli (Eds.),

pp. 707–719.

Cited by: §5.

- OSI Opinion and Maris (2025)
OSI Opinion and J. Maris

Meta’s LLaMa license is still not Open Source.

(en-US).

External Links: Link

Cited by: §3.2.

- Pan et al. (2025)
J. Pan, R. Shar, J. Pfau, A. Talwalkar, H. He, and V. Chen

When benchmarks talk: re-evaluating code LLMs with interactive feedback.

In Findings of the Association for Computational Linguistics: ACL 2025, W. Che, J. Nabende, E. Shutova, and M. T. Pilehvar (Eds.),

Vienna, Austria, pp. 24672–24700.

External Links: Link,
Document,
ISBN 979-8-89176-256-5

Cited by: §3.3.

- Paszke et al. (2019)
A. Paszke, S. Gross, F. Massa, and et al.

PyTorch: an imperative style, high-performance deep learning library.

In Advances in Neural Information Processing Systems 32,

pp. 8024–8035.

External Links: Link

Cited by: §2.

- Peng et al. (2023)
B. Peng, E. Alcaide, Q. Anthony, A. Albalak, S. Arcadinho, S. Biderman, H. Cao, X. Cheng, M. Chung, M. Grella, K. K. GV, X. He, H. Hou, J. Lin, P. Kazienko, J. Kocon, J. Kong, B. Koptyra, H. Lau, K. S. I. Mantri, F. Mom, A. Saito, G. Song, X. Tang, B. Wang, J. S. Wind, S. Wozniak, R. Zhang, Z. Zhang, Q. Zhao, P. Zhou, Q. Zhou, J. Zhu, and R. Zhu

RWKV: Reinventing RNNs for the Transformer Era.

arXiv.

Note: arXiv:2305.13048 [cs]

External Links: Link,
Document

Cited by: §2.

- Public AI Inference Utility (2025)
Public AI Inference Utility

Public ai inference utility.

Note: Accessed: January 2026

External Links: Link

Cited by: §5.

- Public AI Network (2024)
Public AI Network

Public AI: Infrastructure for the Common Good.

Technical report

(en).

External Links: Link,
Document

Cited by: 4th item.

- Raymond (1999)
E. S. Raymond

The cathedral & the bazaar: musings on linux and open source by an accidental revolutionary.

O’Reilly Media, Sebastopol, CA.

External Links: ISBN 9780596001087

Cited by: §1.

- Reiss (2021)
J. Reiss

Public Goods.

In The Stanford Encyclopedia of Philosophy, E. N. Zalta (Ed.),

Note: https://plato.stanford.edu/archives/fall2021/entries/public-goods/

Cited by: footnote 1.

- Rombach et al. (2022)
R. Rombach, A. Blattmann, D. Lorenz, P. Esser, and B. Ommer

High-resolution image synthesis with latent diffusion models.

In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition,

pp. 10684–10695.

Cited by: §2.

- Samuel et al. (2025)
D. Samuel, V. Mikhailov, E. Velldal, L. Øvrelid, L. G. G. Charpentier, A. Kutuzov, and S. Oepen

Small languages, big models: A study of continual training on languages of Norway.

In Proceedings of the Joint 25th Nordic Conference on Computational Linguistics and 11th Baltic Conference on Human Language Technologies (NoDaLiDa/Baltic-HLT 2025), R. Johansson and S. Stymne (Eds.),

pp. 573–608.

Cited by: §5.

- Schuhmann et al. (2022)
C. Schuhmann, R. Beaumont, R. Vencu, C. W. Gordon, R. Wightman, M. Cherti, T. Coombes, A. Katta, C. Mullis, M. Wortsman, P. Schramowski, S. R. Kundurthy, K. Crowson, L. Schmidt, R. Kaczmarczyk, and J. Jitsev

LAION-5B: an open large-scale dataset for training next generation image-text models.

In Thirty-sixth Conference on Neural Information Processing Systems (NeurIPS), Datasets and Benchmarks Track,

External Links: Link

Cited by: §2,
§6.3.

- Shoeybi et al. (2019)
M. Shoeybi, M. Patwary, R. Puri, P. LeGresley, J. Casper, and B. Catanzaro

Megatron-lm: training multi-billion parameter language models using model parallelism.

arXiv preprint arXiv:1909.08053.

Cited by: §2.

- Sieker et al. (2025)
F. Sieker, A. Tarkowski, L. Gimpel, and C. Osborne

Public AI white paper: a public alternative to private AI dominance.

White Paper

Bertelsmann Stiftung.

External Links: Document,
Link

Cited by: §4.

- Tan et al. (2025)
J. Tan, B. Jackson, R. Berjon, and D. Coyle

Airbus for AI: a global strategy for public value creation.

Report

Bennett School of Public Policy.

External Links: Document,
Link

Cited by: §5,
§6.5.

- Tarkowski and Sieker (2026)
A. Tarkowski and F. Sieker

European public AI – policy brief.

Bertelsmann Stiftung.

Cited by: §4.

- Valero and Crespo (2024)
M. Valero and D. Crespo

Es la hora de ‘AIbus’: por qué Europa debe crear una gran empresa de AI.

El País (es).

External Links: Link

Cited by: §5.

- Vaughan-Nichols (2026)
S. J. Vaughan-Nichols

Meta abandons open-source Llama for proprietary Muse Spark.

External Links: Link

Cited by: §6.1.

- Vincent (2026)
N. Vincent

The Coding Agent Data Deal.

Substack Newsletter, Data Leverage.

External Links: Link

Cited by: §3.3.

- von Platen et al. (2022)
P. von Platen, S. Patil, A. Lozhkov, and et al.

Diffusers: state-of-the-art diffusion models.

Note: https://github.com/huggingface/diffusers

Cited by: §2.

- Wang et al. (2024)
Z. Wang, J. Li, M. Ma, Z. Li, Y. Kang, C. Zhang, C. Bansal, M. Chintalapati, S. Rajmohan, Q. Lin, D. Zhang, C. Pei, and G. Xie

Large Language Models Can Provide Accurate and Interpretable Incident Triage.

In 2024 IEEE 35th International Symposium on Software Reliability Engineering (ISSRE),

pp. 523–534.

External Links: ISSN 2332-6549,
Document

Cited by: §3.3.

- Weber et al. (2024)
M. Weber, D. Fu, Q. Anthony, Y. Oren, S. Adams, A. Alexandrov, X. Lyu, H. Nguyen, X. Yao, V. Adams, B. Athiwaratkun, R. Chalamala, K. Chen, M. Ryabinin, T. Dao, P. Liang, C. Ré, I. Rish, and C. Zhang

RedPajama: an Open Dataset for Training Large Language Models.

arXiv.

Note: arXiv:2411.12372 [cs]
version: 1

External Links: Link,
Document

Cited by: §2.

- Weber (2005)
S. Weber

The Success of Open Source.

Harvard University Press.

External Links: ISBN 978-0-674-04499-9 978-0-674-01292-9,
Link,
Document

Cited by: §1.

- Widder et al. (2024)
D. G. Widder, M. Whittaker, and S. M. West

Why ‘open’ AI systems are actually closed, and why this matters.

Nature 635 (8040), pp. 827–833 (en).

Note: Publisher: Nature Publishing Group

External Links: ISSN 1476-4687,
Link,
Document

Cited by: §3.3.

- Wolf et al. (2019)
T. Wolf, L. Debut, V. Sanh, J. Chaumond, C. Delangue, A. Moi, P. Cistac, T. Rault, R. Louf, M. Funtowicz, et al.

Huggingface’s transformers: state-of-the-art natural language processing.

arXiv preprint arXiv:1910.03771.

Cited by: §2.

- Wu et al. (2022)
Y. Wu, K. Chen, T. Zhang, Y. Hui, M. Nezhurina, T. Berg-Kirkpatrick, and S. Dubnov

Large-scale contrastive language-audio pretraining with feature fusion and keyword-to-caption augmentation.

arXiv:2211.06687.

Cited by: §2.

### Appendix A Comparing select open source software and open models

Properties
|

Linux
|

scikit-learn
|

TensorFlow
|

Kubernetes
|

OLMo
|

DeepSeek
|

LLaMA
|

Type
|

Operating System
|

ML Library
|

ML Framework
|

Container Orchestration
|

AI Model
|

AI Model
|

AI Model
|

Transparency
|

High — development is fully visible
|

High — all algorithms and tests are publicly documented and peer-reviewed
|

Medium — public codebase, but production usage depends on internal forks
|

High — development processes, governance, and roadmap are fully public
|

High — training pipeline, data decisions, and documentation openly shared
|

Medium — some training details and weights released, but pipeline unclear
|

Low — no access to training data, limited documentation, opaque post-training
|

Community Governance
|

Yes — community + Linux Foundation
|

Yes — consensus driven; backed by research orgs
|

Yes — SIGs, GitHub issues, TF RFCs
|

Yes — CNCF technical governance
|

Yes — AI2 hosts calls, roadmap, accepts contributions
|

No — releases set by DeepSeek
|

No — decisions made by Meta; no public forum
|

License Stability
|

Clear
|

Clear
|

Clear
|

Clear
|

Clear
|

Unclear
|

Unclear
|

Use Without Large Infra
|

Yes; runs on typical personal hardware
|

Yes; any Python env
|

Yes; CPUs or GPUs; many hosted options
|

Yes; single-node or small clusters
|

Partially; some GPUs locally; pruning supported
|

No; inference targets powerful clusters
|

No; needs high-end GPUs
|

Open Source Maintenance
|

Active; broad community + LF
|

Active; INRIA-led core + community
|

Active; Google + community
|

Active; CNCF + industry
|

Active; AI2 with public roadmap
|

Partial; periodic checkpoints
|

Irregular; Meta-driven
|

Business Model
|

Service-based (Red Hat, etc.), donations
|

Academic; grants/volunteers
|

Freemium support by Google
|

Cloud-vendor support via CNCF
|

Non-profit; philanthropic
|

Hedge-fund backed; opaque
|

Meta strategic positioning
|

Supporters/Adopters
|

Universities, enterprises, hobbyists, clouds
|

Universities, educators, research
|

Enterprises, researchers, hobbyists
|

Global enterprises, cloud providers
|

Academic labs, open-science advocates
|

Emerging China-centric dev community
|

Academic labs, startups via HF
|

Table 1: Comparing open source software and open source AI projects along a variety of axes, including transparency, governance, licensing, and maintenance concerns. A key takeaway is that AI is not like other open source software.
