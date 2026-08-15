---
title: "Open WebUI: An Open, Extensible, and Usable Interface for AI Interaction"
person: "nick-vincent"
section: "by"
type: "journal-article"
year: 2025
date: "2025-10-02"
venue: "arXiv preprint, 2025"
authors: "Jaeryang Baek, Ayana Hussain, Danny Liu, Nicholas Vincent, Lawrence H. Kim"
source_url: "https://arxiv.org/abs/2510.02546"
retrieved: "2026-08-13"
content: "full-text"
notes: "OpenAlex W4416368802; CV ref [O9]; Full text from the arXiv HTML rendering of the preprint (https://arxiv.org/html/2510.02546v1)."
---

# Open WebUI: An Open, Extensible, and Usable Interface for AI Interaction

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

- 2.1 Background on Local and Open-source LLMs

- 2.2 LLMs and HCI

- 3 System Design

- 3.1 Current Challenges in LLM Interfaces

- 3.1.1 Privately Hosted UI Limitations

- 3.1.2 Self-hosted UI Challenges

- 3.2 Design Goals for Open WebUI

- 3.2.1 Open

- Open-source

- Privacy and Data Management

- Transparency in AI Model Selection

- 3.2.2 Extensible

- Plugin Support

- Interface Customization

- Many Model Interactions

- 3.2.3 Usability

- Ease of Installation and Use

- 3.3 The Open WebUI Community Platform

- 3.3.1 Community Platform for Sharing and Innovation

- Tools and Functions

- Custom Model Presets

- Prompt Presets

- 3.3.2 Ethical Data Collection and Usage

- 4 Evaluation

- 4.1 User-generated Content

- 4.1.1 Data

- 4.1.2 Topic Modeling

- 4.1.3 UGC Results

- 4.2 User-Generated Plugins

- 4.2.1 Tools

- 4.2.2 Functions

- Filters

- Pipes

- Actions

- 4.3 User Survey

- 4.3.1 Methods

- 4.3.2 Results

- 5 Discussion

- 5.1 Design Implications for LLM Toolkits

- 5.2 Additional benefits of openness and extensibility for “local” models

- 5.3 Future Work and Limitations

- 6 Conclusion

- 7 Acknowledgments

- Trademarks.

- References

License: CC BY-NC-SA 4.0

arXiv:2510.02546v1 [cs.HC] 02 Oct 2025

## Open WebUI: An Open, Extensible, and Usable Interface for AI Interaction

Jaeryang Baek

email: jaeryang_baek@sfu.ca

Affiliation: Simon Fraser University
, Burnaby
, BC
, Canada

,
Ayana Hussain

email: ayana_hussain@sfu.ca

Affiliation: Simon Fraser University
, Burnaby
, BC
, Canada

,
Danny Liu

email: danny_liu_5@sfu.ca

Affiliation: Simon Fraser University
, Burnaby
, BC
, Canada

,
Nicholas Vincent

email: nvincent@sfu.ca

Affiliation: Simon Fraser University
, Burnaby
, BC
, Canada

and
Lawrence H. Kim

email: lawkim@sfu.ca

Affiliation: Simon Fraser University
, Burnaby
, BC
, Canada

Figure 1. Screenshot of Open WebUI. A) The Model Selector, central to the system’s design, supports simultaneous interactions with multiple models, including private models (e.g., GPT-4) via APIs. It also allows for directly downloading local models by searching within the selector. B) The Open WebUI accommodates both standalone and multi-account configurations. C) Users can access the settings menu to manage models. Additional options to adjust model parameters such as seed and temperature are provided through a controls button. D) The sidebar acts as a portal for integrating user-specific models, preset prompts, and documents via Workspace. E) The chat input section is equipped with document, image attachment, web search, and custom tool capabilities via the plus icon; additionally, options for voice and video calls are integrated.

####### Abstract.

While LLMs enable a range of AI applications, interacting with multiple models and customizing workflows can be challenging, and existing LLM interfaces offer limited support for collaborative extension or real-world evaluation. In this work, we present an interface toolkit for LLMs designed to be open (open-source and local), extensible (plugin support and users can interact with multiple models), and usable. The extensibility is enabled through a two-pronged plugin architecture and a community platform for sharing, importing, and adapting extensions. To evaluate the system, we analyzed organic engagement through social platforms, conducted a user survey, and provided notable examples of the toolkit in the wild. Through studying how users engage with and extend the toolkit, we show how extensible, open LLM interfaces provide both functional and social value, and highlight opportunities for future HCI work on designing LLM toolkit platforms and shaping local LLM-user interaction.

### 1. Introduction

Sparked by the release of ChatGPT (Ray 2023; Hu 2023) in 2022, many subfields of computing – including social computing (Kulkarni et al. 2023; Park et al. 2023) – have seen a surge of interest in working on and with large language models (LLMs) (Zhao et al. 2023). Some scholars have argued that the new generation of “foundation models” marks a major shift in computing, while raising a number of new sociotechnical concerns (Bommasani et al. 2021).

The initial set of LLM offerings from technology companies was privately designed, operated, and provisioned products. Early users of ChatGPT and competing products like Anthropic AI’s Claude (Bai et al. 2022) and Google’s Bard (Liedtke 2023) interacted with these new chatbots through gated online platforms or via APIs (Heikkilä [n. d.]).

While companies have made progress on advancing privately provisioned “closed” LLMs, various online communities have advanced efforts to build and distribute “open” models – large language models that are trained on web-scale data (such as “The Pile” (Gao et al. 2020)) and distributed as “raw weights” on platforms like HuggingFace, alongside open-source code that allows users to perform LLM inferences on their own computing devices. As early as April 2022, EleutherAI’s “GPT-NeoX-20B” was available (Black et al. 2022). More recently, models from Meta, Mistral AI, and others (Touvron et al. 2023; Jiang et al. 2023; Jiang et al. 2024) have received attention from researchers, the media, and users (Goldman 2023). The Ollama project (Morgan 2024) further contributes by facilitating the download of various model adaptations. However, it operates primarily through a command-line interface (CLI) and is designed for individual use, limiting accessibility for non-technical users.

Although communities have been formed around these openly released LLMs on online platforms like Discord and Reddit (see e.g., GPT4All (Anand et al. 2023), h2oGPT (Candel et al. 2023), and the r/LocalLLaMA subreddit), using these models remains a daunting task for many. The primary interface available to early adopters of local LLMs was CLIs, and using a model locally requires installation (Nuñez 2023; Ste 2023). This combination of growing interest and high entry barriers highlights a tension between the promise of open models and their current usability.

In theory, the proliferation of open models opens the door for alternative paradigms of LLM use. However, to fully realize this potential, platforms enabling users to run and configure interactions with open models need to be thoughtfully designed. To this end, we highlight three important design considerations for LLM hosting interfaces and toolkits. First, allowing users to run and configure open models through these platforms is already an important step in supporting openness. Openness allows people to select models based on both technical capabilities and preferences for alignment with particular values e.g., following fair training data practices (Fan et al. 2025)). Second, extensibility – which allows users to build and share their own extensions and plugins – also requires careful design for customizing the flow of information between different models and external systems (search engines, translations, bespoke preprocessing, etc.). Third, to fully leverage both openness and extensibility, platforms must prioritize usability. For example, by lowering barriers to adoption of these platforms, simplifying installation, and making model management more intuitive, platforms can support accessibility for individual users and organizations.

However, the reality for many users is a steep learning curve, especially without a programming or machine learning background. For instance, the release of models like LLaMa 2 generated excitement among tech-savvy communities on platforms such as Discord, Reddit, and Hacker News (Franzen 2023), but for many users, the process of setting up, downloading, and effectively interacting with these local LLMs remains daunting. Simplifying these processes is essential, not only to enhance user experience but also to ensure the accessibility of AI technologies.

Building on the challenges faced by everyday users, implementing open-source AI tools that can be self-hosted emerges as a critical solution. Such tools are especially valuable for people without stable internet connectivity, such as those in remote or rural areas. They also provide alternatives for users in countries where services like ChatGPT are unavailable or restricted. Moreover, open interfaces can help address privacy and data sovereignty concerns for users and organizations wary of sending queries to external data centers, a growing issue highlighted in discussions about data privacy and security (see e.g., discussion in (Chen et al. 2023)). Ensuring that these interfaces are open not only broadens access but also ensures that users can maintain control over their interactions and data, aligning with local needs and regulatory requirements.

The need for extensibility in AI interfaces is also becoming increasingly apparent as the field of AI grows at an exponential rate. Each user or community has distinct needs and requirements, which means interfaces must be adaptable and flexible. Implementing a robust plugin system allows for this necessary adaptability, enabling users to tailor functionalities to specific tasks or preferences. This extensibility benefits users by allowing continual adaptation to the latest AI developments, ensuring that the interface remains useful and relevant in a rapidly evolving technological landscape.

Finally, the cornerstone of broad adoption and effective use of AI interfaces lies in their user-friendliness. Simplifying complex processes is essential to make advanced AI tools accessible to a wider audience, including those with minimal technical background. Interfaces need to be intuitive, with clear guidance and streamlined processes for setting up, configuring, and using AI models. Making sophisticated AI technology easy to interact with not only enhances the overall user experience but also fosters greater engagement and democratization of cutting-edge AI capabilities, making them available and usable across diverse societal segments.

In this paper, we introduce Open WebUI, an open, extensible, and usable interface that allows users to interact simultaneously with many models via chat, audio, and video. Users can easily switch between local models and private model endpoints. Extensibility is a central strength of Open WebUI. Unlike existing systems, Open WebUI is designed with two distinct classes of extensibility: users can extend either the LLM capabilities or the user interface itself. These extensions can be easily shared and adopted through a community platform that is already being actively used by a large portion of the user base. Usability also distinguishes the system. Installation and configuration of basic functionalities are simplified, while heavier processing tasks are isolated in a dedicated container to ensure the main setup is lightweight. The interface also draws on the familiar design of ChatGPT to support new users while allowing for advanced functionalities and flexibility for advanced uses.

To evaluate the system, we take a multi-pronged approach. Because the system has already been deployed in the wild, our evaluation draws on real-world usage and community engagement. First, we analyze feedback from existing users across a wide variety of platforms, including feedback about the project (e.g., GitHub issues), public-facing discussion about the project (e.g., blog posts and YouTube videos organically created by users seeking to share information about the system), and publicly shared user-generated plugins. We highlight design choices that were particularly resonant with early users as well as evidence that Open WebUIachieved certain goals around openness, extensibility, and usability. Second, we report the results of a survey of active users to help understand how Open WebUI is meeting the design goals.

We conclude by discussing the implications of studying a widely adopted open LLM interface. Because Open WebUI has been leveraged and extended by a large user community, it provides an opportunity to examine real-world interaction patterns, preferred modes of engagement with LLMs, and emerging design challenges. Our analysis also highlights how community practices such as sharing configurations and prompts shape interface use, and how local, decentralized, and open alternatives can expand opportunities for experimentation. We contribute to HCI by grounding our analysis in in the wild use and identifying lessons for designing future LLM interfaces that respond to user practices and evolving needs.

In summary, our paper makes the following contributions:

- (1)

introduction of Open WebUI, an open-source LLM toolkit for interacting with multiple local and hosted LLMs through an open, extensible, and user-friendly interface, including a community platform for sharing and importing development resources.

- (2)

evaluation of the Open WebUI toolkit through analysis of organic engagement, voluntary survey responses, and examples of how Open WebUI has been used in practice.

- (3)

discussion around implications for HCI, particularly in supporting user communities, social computing, extensible human-AI interaction, and designing future LLM toolkit systems.

### 2. Related Work

Here, we describe related work in the space of local and open-source LLMs and their use in social computing and HCI.

#### 2.1. Background on Local and Open-source LLMs

Efforts to support open LLMs have been supported by grassroots contributions made via platforms like GitHub, Discord, Reddit, and HuggingFace, as well as support from private firms like Meta (Franzen 2023; Barr 2023). GitHub, primarily a tool for version control and collaboration on code, facilitates user contributions through “Pull requests" and allows community feedback via “Issues" and “Discussions". Discord, widely utilized for its robust communication features, including messaging and voice chat, supports vibrant communities centered on AI development. Finally, HuggingFace is a platform that supports the sharing of model weights and datasets and has achieved widespread adoption from local and open-source AI contributors.

By leveraging these online community platforms, contributors rapidly developed and shared code, datasets, and other resources that advanced local and open-source LLMs. Thus far, efforts to build open and local LLMs seem to have mirrored past successes in peer production (Benkler et al. 2015).

A major milestone in the movement for widespread use of local and open models was the development of the open source project “llama.cpp” (Gerganov 2024), which made running LLMs practical for more users. Following this release, the “Ollama” project (Morgan 2024) further expanded the reach of local models, including LLaMa and a huge array of other models, by streamlining the process of downloading and interacting with models via a CLI.

However, prior to the advent of Open WebUI in 2023 (ope [n. d.]), most of these popular self-hosted interfaces were designed with cloud-hosted LLMs in mind. These platforms—while powerful and user-friendly—seldom prioritized local inferences, often requiring internet connectivity and reliance on proprietary infrastructure. Efforts to create interfaces for local LLM deployment were limited, and when they did surface, they frequently lacked the polish or extensibility seen in cloud-first systems. For instance, many early local-first solutions were constrained by usability challenges, limited support for extensions, and difficulties adapting interfaces to varied use cases. Open WebUI addresses these gaps by offering an interface that integrates local inference with cloud interoperability, providing a foundation that has since been adapted and extended in other open-source projects.

In this paper, we are mainly concerned with the interface for local and open models, so we use the term “open models” to refer broadly to any models that could be downloaded and used locally with an interface like Open WebUI.
While much of the code released by contributors is open-source, some of the licenses under which certain models have been released are not fully “open source” (as defined by the Open Source Initiative) (Ope 2006). Furthermore, there is an ongoing debate about how model weights can actually be licensed (AIW 2023; Contractor et al. 2022).

#### 2.2. LLMs and HCI

Research in HCI has already begun to explore the potential of new LLM-based technologies.

At CHI 2023, just a few months after the release of ChatGPT, there were 21 works that mentioned LLMs. By CHI 2024, this number had surged to 145, highlighting an explosive growth in the field’s interest in LLMs. One notable direction of exploration has been the use of LLMs for social simulation (Park et al. 2023), generating synthetic data for HCI (Hämäläinen et al. 2023), and survey (Xiao et al. 2020). HCI researchers have also explored LLM interfaces, in contexts like mobile computing (Wang et al. 2023) and prompt design (Zamfirescu-Pereira et al. 2023a; Arawjo et al. 2023). All of these avenues of research stand to benefit from access to extensible LLM interfaces.

Interface design for LLMs can vary widely based on the application domain and target user group. Notably, chat-based interfaces represent one of the most intuitive and widely adopted methods for interacting with LLMs (OpenAI 2024; Google 2024; Anthropic 2024). These interfaces mimic human conversation, making them accessible and easy to use for a broad range of users. The versatility of chat-based UIs allows them to be adapted for various purposes, ranging from general-purpose virtual assistants to more niche applications. For instance, some users have adapted chat-based UIs to use LLMs as a virtual companion or “AI girlfriend” (Depounti et al. 2023; Lorenz 2023). This application leverages the conversational capabilities of LLMs to provide users with a simulated social interaction experience. While this raises ethical and psychological considerations, it also showcases the adaptability of LLMs to cater to diverse user needs and preferences. Beyond virtual companions, chat-based UIs find their utility in numerous other applications. For instance, customer service chatbots (Følstad and Skjuve 2019), effective educational chatbots (Ruan et al. 2019), and task management assistants (Toxtli et al. 2018) all utilize the chat-based model to facilitate user interaction with the underlying AI. For these reasons, the design of Open WebUI is motivated and mirrors these chat-based UIs.

Prior research has also explored interfaces for LLM chaining and prototyping ML functionality through iterative prompt design. These interfaces enable users to chain multiple LLM prompts, breaking tasks into manageable steps and facilitating prompt iteration (Wu et al. 2022b; Wu et al. 2022a). Systems like PromptChainer provide visual interfaces for constructing these chains (Wu et al. 2022a), while Prompt Sapper extends this by offering a block-style visual programming environment for AI chains (Cheng et al. 2024). Similarly, PromptMaker focuses on prompt-based prototyping, enabling few-shot prompting and iterative refinement (Jiang et al. 2022). ChainForge, an open-source visual toolkit, supports simultaneous cross-LLM comparison, prompt template design, and hypothesis testing (Arawjo et al. 2024). These works highlight the importance of an interactive, extensible, and user-friendly interface for working with LLMs. While they focus primarily on interfaces for prompting support—an area we also address through the Prompt Preset feature—our work broadens the interface capabilities and provide an opportunity to study how users interact with a system offering many configurable features, how they customize it to their own needs, and what this reveals about usability, interaction patterns, and emerging design challenges in HCI.

### 3. System Design

In this section, we present the design of Open WebUI, an open-source interface and toolkit for local and private LLMs. While interfaces of this kind are increasingly common (i.e., see (Any [n. d.]), (Studio 2024), (Lob [n. d.])), our contribution lies in the system’s layered and extensible design, which enables a wide range of use cases and has supported significant community-driven involvement.

#### 3.1. Current Challenges in LLM Interfaces

We first detail the limitations of existing UIs for private models such as ChatGPT, focusing on user privacy, limited extensibility, and restricted model selection. Then, we turn to the obstacles faced by UIs for local models, including complex setup processes, limited accessibility, and basic user interface features. These issues pose significant barriers to both research and broader user adoption.

##### 3.1.1. Privately Hosted UI Limitations

Proprietary AI interfaces like ChatGPT have several limitations. These include concerns about user privacy, lack of open-source availability leading to limited extensibility, restricted model selection, and constrained social features. First, user privacy concerns may restrict how the systems are actually used. This creates a ceiling on the contexts in which LLMs can be evaluated and audited, and could fundamentally cause certain topics and domains – especially anything deemed sensitive – to become understudied. Second, the ability to select from a diverse range of models would enable new HCI studies to be conducted. Such flexibility is also vital for accommodating the varied needs of different users.

##### 3.1.2. Self-hosted UI Challenges

Self-hosted local AI Interfaces, while addressing the above concerns, suffer from their own set of issues. These include the complexity of configuration and setup processes, rendering the installation process particularly daunting for individuals with limited technical expertise, and the restriction to individual use without support for multiple accounts. Additionally, these interfaces often lack the polished user experience and advanced features common in privately developed AI interfaces. These factors collectively impede the adoption of local LLMs for wider applications and for use by everyday users.

#### 3.2. Design Goals for Open WebUI

Open WebUI is designed to improve on both sets of challenges, and to effectively balance usability with an extensible and open approach. This involved providing a GUI that is intuitive and familiar (important for adoption (Yablonski 2024)), minimizing effort to interact with the local AIs.

Below, we provide additional details about the specific design goals for Open WebUI.

##### 3.2.1. Open

We identified the following specific goals for Open WebUI that relate to taking an “open” approach. This entails creating a system that not only provides users with transparency into how it works but also empowers them to contribute to its development and evolution.

###### Open-source

We have made the entire source code of Open WebUI publicly available
This allows users to freely examine and audit the system, its connections, and dependencies. This promotes transparency in the system and encourages collaboration among developers who can contribute to its growth and improvement. The open-source nature aligns with our goal of promoting transparency and accountability in AI development. With the entire code repository available, any user can identify potential vulnerabilities, suggest improvements, or even develop their own extensions to the system.

###### Privacy and Data Management

HCI has highlighted privacy concerns that stem from new LLM systems (Zhang et al. 2024). Open WebUI is designed to prioritize user data privacy protection by implementing robust privacy controls and by being able to function entirely offline, with the option to use an API key to also query private models, unlike many interfaces for private LLMs that necessitate continuous online connectivity and logging. This design choice not only enhances user privacy but also ensures the system’s utility in environments with limited or unreliable internet access. Users have full control over their data and can choose how it is shared with third-party services or models. This includes explicit opt-in for external connections and model interactions, ensuring that users are always aware of what data is being collected, used, or shared. Open WebUI also stores all interaction data locally, giving users complete ownership of their data.

###### Transparency in AI Model Selection

Unlike proprietary interfaces that often obscure the underlying AI models used, our open approach allows users to view and select from a list of available models. This enables users to make informed decisions about which model suits their needs best, promoting accountability and choice.

##### 3.2.2. Extensible

We identified three key sub-goals here: plugin support, interface customization, and integration with many models.

###### Plugin Support

The cornerstone of our approach to achieving a highly extensible AI interface is a novel two-pronged plugin architecture that integrates front-end and back-end extensibility, while remaining script-based for full control and easy sharing through the community platform. Open WebUI achieves this through the prongs described below.

Tools: Tools within Open WebUI operate at the model level and allow users to make use of virtually any Python script to extend the LLM’s capabilities, which supports the system’s goal of being highly extensible. This not only enables real-time capabilities that require external data fetching or active interfacing with other systems, but also significantly broadens the horizons for what can be achieved with LLMs. The term “Tools” is also commonly used within LLM research and primarily by OpenAI (OpenAI 2023) to refer to the same functionality.

The Tools feature is designed to support a diverse range of extensibility options by allowing the integration of executable scripts that interact with external data sources and systems. In the reference implementation provided, several exemplar tools demonstrate the system’s capacity to perform real-time data retrieval, execute numerical computations, and interface with dynamic state-based environments. These examples serve as foundational templates, showcasing how scripting components can be employed within the architecture to enable time-sensitive queries, perform precise mathematical operations, or fetch contextual environmental data. Such tools illustrate the extensibility of the framework, offering a flexible basis for users to develop and deploy specialized functionalities tailored to their specific research or application needs.

Functions: Functions operate at the application/interface level and focus on altering the functionalities of the interface itself, making them crucial for users who wish to tailor the interface according to their specific use cases.

While the term “Functions” is not a standard term across LLM platforms, similar concepts are often referred to broadly as “plugins” (Git [n. d.]; Lob [n. d.]) or “slash commands” (Any [n. d.]) in other systems. However, we adopt this terminology following general programming, where a function is a self-contained piece of logic that performs a specific operation. This emphasizes that they are active, modular units of behavior within the system, distinct from just commands or plugins, which may not convey the same sense of operational logic. Functions in Open WebUI are organized into three distinct classes, each serving unique purposes:

Filters: Filters serve as middleware solutions that both pre-process and post-process conversational data surrounding interactions with LLMs. Their utility spans a broad range of functions, from scrubbing sensitive information and clipping contexts to fit the operational limits of models (especially crucial for local models with restricted context windows) to monitoring dialogues to ensure adherence to usage policies. Filters can be particularly useful for supporting translation-based use cases, greatly increasing the potential pool of users who can benefit from AI systems.

Pipes: Central to the flexibility of Open WebUI is the concept of Pipes, which abstracts Python functions and presents them as “models" within the interface. This unique feature allows for an approach where Python code, irrespective of its purpose or complexity, can be seamlessly integrated and utilized just like an AI model. A Pipe encapsulates arbitrary Python functions, enabling them to interact with the system either in conjunction with LLMs or as standalone functions that bypass the need for LLMs entirely. Pipes shift the extensibility from requiring system-level updates to simply adding or modifying Python scripts, thus democratizing model integration and encouraging experimentation within the developer community.

One of the advantages of Pipes is their ability to execute independently of the traditional LLM chat interaction paradigm. This direct execution capability not only enhances the speed and efficiency of data processing tasks within Open WebUI but also reduces dependency on model capabilities for non-language-related tasks. Moreover, Pipes can serve as a bridge for incorporating niche models that are not natively supported under the OpenAI API spec, which is the standard API specification for most models integrated in Open WebUI. By wrapping these non-standard models within a Pipe, developers can bring in specialized AI capabilities (like those from newly developed or less common AI frameworks) and make them accessible to users through the same interface. This function is crucial because it allows for customization and expansion of Open WebUI’s capabilities without altering the core codebase. It shifts the extensibility from requiring system-level updates to simply adding or modifying Python scripts, thus democratizing model integration and encouraging experimentation within the developer community.

Actions: Equally important are Actions, which augment the interactive elements available within the system’s UI. Actions enhance user interactivity by allowing the inclusion of customizable buttons in the response toolbar. These buttons can trigger specific tasks when clicked, offering users a direct and intuitive way to interact with the AI system beyond the standard text input. This mechanism ensures that operations requiring user consent or initiation are controlled and deliberate, maintaining user autonomy.

This plugin architecture grants users the capability to modify and enhance their interaction with LLMs in a highly personalized manner while ensuring that Open WebUI remains adaptable.

###### Interface Customization

One of the key sub-goals for Open WebUI is to allow users to personalize their experience with features like advanced UI settings (e.g., model profile image, prompt suggestions) and custom CSS for unique themes. This adaptability ensures that Open WebUI remains relevant and useful as user preferences evolve.

Figure 2. Many Model Interaction: Users simultaneously interact with multiple language models, such as Llama 3.1, GPT 4, and Mistral. The user submits a query (“Why is the sky blue?”), which is processed by selected models, generating concurrent responses (R1, R2, R3). Users review and compare these responses, selecting the most appropriate one to continue the conversation. This method enables users to harness the strengths of each model, as they can select the best response for their needs and, in the process, generate preference data over models.

###### Many Model Interactions

Open WebUI works with both open-source and private models. This integration enables users to leverage the full spectrum of capabilities offered by these models (and new models that come out). Open WebUI also allows for simultaneous interactions with multiple models. This broadens the potential use cases, as users can leverage the strengths of various models concurrently. For instance, a user can query a model specialized in technical knowledge, while simultaneously interacting with another model that excels in creative tasks, all within the same interface.

##### 3.2.3. Usability

###### Ease of Installation and Use

One of the primary design goals for Open WebUI is to simplify the installation process and lower the barrier to setting up and using the system. This is achieved by automating most of the configuration process, enabling a ’plug-and-play’ installation experience. The system can be installed and operational with a single command line, eliminating the need for manual configuration of environmental variables or complex setup procedures.

Figure 3. Open WebUI’s admin settings facilitate easy AI model management through its graphical interface, enhancing accessibility by reducing dependency on command-line tools. The "Pull a model" feature enables users to download models simply by typing their names and clicking a button, with a progress bar displaying the download status. Additionally, the menu includes straightforward options for deleting models and uploading raw GGUF files, streamlining model management.

Moreover, an essential aspect of Open WebUI’s user-centric design involves the capability to manage AI models directly from the UI itself. This functionality streamlines the process of downloading and deploying new models, making it effortless for users to stay updated with the latest advancements in LLMs. The direct download feature negates the need for separate download and installation steps.

Finally, Open WebUI can also be set up within an organizational infrastructure. Installation requires only a standard server setup and an administrative account to manage user access and permissions. Employees or department members can then create their individual accounts, enabling a personalized experience while maintaining control at an organizational level.

#### 3.3. The Open WebUI Community Platform

The development and deployment of Open WebUI presents an exciting new frontier in the domain of HCI, particularly in the context of social computing. Our project also incorporates a community platform, which aims to foster a collaborative environment for sharing and learning. The organization of this platform is structured around distinct resource categories: Tools, Functions, models, and prompts. Users can browse and filter these categories and seamlessly import selected resources into the Open WebUI, making contribution, discovery, and adoption of community content intuitive and efficient.

##### 3.3.1. Community Platform for Sharing and Innovation

Figure 4. Open WebUI’s Prompt Preset feature, divided into four parts. (A) illustrates creating or importing Prompt Presets, where variables within square brackets are auto-selected for easy replacement using the tab key. Users also have the option to import community-shared presets. (B) demonstrates loading these presets into the chat input area using a forward slash command, enhancing user workflow. (C) highlights the efficient replacement of auto-selected variables, with the first variable selected by default and subsequent variables easily selectable with the tab key. (D) depicts submitting the customized prompt in Open WebUI, showcasing the feature’s utility in streamlining repetitive tasks.

The Open WebUI’s community platform enables the sharing of Tools, Functions, customized prompts, and model presets with custom parameters. This design allows users to extend their models’ capabilities or modify the interface without implementing these features themselves, simply by using contributions from others. It also helps non-expert users who struggle with constructing efficient prompts (Zamfirescu-Pereira et al. 2023b), which can otherwise lead to the underutilization of LLM capabilities. The community platform mitigates this by leveraging collective intelligence, allowing users to learn from shared experiences. Consequently, this fosters an environment of continuous improvement, empowering users to refine their interactions for more meaningful LLM engagements.

###### Tools and Functions

The community platform encourages active collaboration around Tools and Functions, which were previously introduced. Users can explore extensions developed by others, experiment with them in their own workflows, and contribute improvements or variations back to the platform. This collaborative cycle accelerates the spread of innovative features and provides insights into common usage patterns and emerging needs, which reinforces the platform’s role as a hub for collective creativity and knowledge sharing.

###### Custom Model Presets

The community platform is designed to facilitate the sharing of model “presets” – these include custom system prompts, specific parameters like temperature, and unique UI components such as model profile images and conversation starters.

###### Prompt Presets

Alongside model presets, users can also share custom prompt presets. These presets are particularly useful in guiding less experienced users in effectively utilizing LLMs for various tasks. By analyzing popular presets, researchers can gain insights into user preferences and typical use cases, informing future improvements in LLM design and interaction methods. This feature may significantly improve the user experience over existing privately hosted LLM UIs, like ChatGPT, which lack such sharing capabilities.

##### 3.3.2. Ethical Data Collection and Usage

A notable feature of the community platform is the ability to share chat logs. This functionality is not just for showcasing model characteristics but also plays a crucial role in ethical data collection (because the system is local, data is only available from users who opt in to a particular study or data sharing pool). This aspect is particularly relevant in the current landscape, where data privacy and intellectual property rights are of paramount importance (Michael M. Grynbaum 2023).

Shared chat logs open multiple avenues for research. They can be used to study user behavior, model-user interaction dynamics, and the effectiveness of different prompts and modelfiles. This data can be instrumental in understanding how users from diverse backgrounds and with varying levels of expertise use LLMs. Such insights are invaluable in making LLMs more accessible and effective for a broader user base. In short, getting more people to use systems like Open WebUIwill greatly increase the potential pool of data for academic and non-commercial research.

### 4. Evaluation

To understand how our system is meeting our design goals based on in-the-wild usage, we deployed an open-sourced Open WebUI to the public, similar to prior work (Kovacs et al. 2018). We use three approaches to understand users’ experience with Open WebUI: 1) analysis of organic public user-generated content provided by users (e.g., GitHub issues reported by users, YouTube videos, social media posts, and blogs about Open WebUI) through topic modeling, 2) analysis of user-contributed extensions on the community platform, and 3) a survey completed by a subset of current users.

#### 4.1. User-generated Content

This component of the evaluation aims to (1) look for evidence that our three core design goals were met and (2) identify areas for improvement. Given that our objective was to create a system that is extensible and locally-focused, we look to organic engagement as a fully opt-in data source describing user experiences with the system. Similarly, as Open WebUI is a toolkit supported by numerous community initiatives, we first employ topic modeling on in-the-wild content to gain a broad sense of real-world use cases and behaviors. These findings are then complemented by a more in-depth analysis of specific examples presented later in the section.

##### 4.1.1. Data

We obtained two datasets for our analysis: public engagement with the project’s GitHub page and public content posted to other UGC platforms.

GitHub Data: The data available from GitHub includes stars (GitHub’s ‘like” feature), forks (indicating a user wants to modify and extend Open WebUI), user-reported issues, and discussions (forum posts on the GitHub platform). We obtained data on this engagement using GitHub’s official API in August 2024.

Other UGC: While public UGC has long been frequently used in HCI research (Blythe and Cairns 2009), and can be a valuable potential source of data for evaluating live OSS systems, recent changes in data access and discussions about data collection (Freelon 2021) – some of them stemming from LLM training data practices (Reddit 2024) – complicate this process. For instance, acquiring data from Twitter and Reddit for research has become substantially more challenging.

As such, we take an approach that involves collecting snippets of UGC that have already been indexed by search engines, inspired by recent work in software engineering research (Wyrich and Bogner 2024) and by discussions about the “post-API” era (Poudel and Weninger 2024).

The initial stage involved manually searching for content related to Open WebUI (keywords omitted for anonymity). We found content on: LinkedIn, Twitter, Reddit, Hacker News, Medium, and YouTube. This list is not meant to be exhaustive, but rather aims to cover a variety of potential perspectives. To analyze this content systematically, we collected public snippets that appear in search engine results (similar to work mentioned above (Wyrich and Bogner 2024; Poudel and Weninger 2024) using the SerpAPI service. We collected 300 results for each platform (using queries formatted as “site:reddit.com”) and then manually filtered this data using keywords to ensure the indexed content was directly relevant.

Poudel et al. specifically examined the viability of this “post-API” approach (Poudel and Weninger 2024). Their results were potentially concerning regarding the use of SERP-based UGC data: results did not match random samples that were biased towards popular and positive content. However, for our purposes, we are not aiming to obtain a random sample of UGC, but rather to select for both critical and positive content and identify themes within each corpus, and so this limitation is at least partially mitigated.

After performing filtering for posts containing direct references to our system, we were left with 533 unique posts (including the title, as indexed by Google, and a snippet of content).

We treat our GitHub data and other UGC data as two distinct corpora, working from an initial observation that GitHub data seemed to primarily involve people reporting and discussing issues and pain points, whereas UGC (such as YouTube videos and blog posts) seemed to primarily involve people’s tutorials, promotional content, and descriptions about how they use Open WebUI.

##### 4.1.2. Topic Modeling

Given the varied nature of the content, topic modeling offers a scalable way to extract and compare thematic structures across different platforms consistently.
For GitHub data, a document is the title of one issue, pull request, or discussion post. For other UGC, a document is one SERP item (page title and page snippet). While this approach necessarily misses out on specific parts of content (e.g., the main body of a blog post or the audio of a YouTube video), it has the benefit of standardizing document size across different platforms so that we can summarize topics.

Following similar methods to (antoniak_blog; Antoniak et al. 2019), we used a Latent Dirichlet Allocation topic model. We used the Python “tomotopy” library with Gibbs sampling, and the data was preprocessed using regular expressions and the “nltk” library for removing stopwords and special characters (which we found was useful for the interpretation of our topics). We experimented with different topic numbers, using both manual evaluation of topic coherence and quantitative coherence scores. Each model was trained over 2000 iterations. After training, we used the top 10 words, along with an inspection of specific posts, to name the topics (our figures below show just the top 3 words for space).

##### 4.1.3. UGC Results

First, examining the overall volume of engagement with our system, we saw that at the time of the analysis (January 2025), the GitHub repository for Open WebUI had 57k+ stars and 4.5k+ forks with a total of 13M+ package downloads, and 1500+ pull requests were submitted, with 320 unique contributors. Looking at our non-GitHub UGC, after using keyword filtering to find highly relevant content, we found 165 posts from LinkedIn, 147 on Twitter, 129 on YouTube, 115 on Reddit, 99 on Medium, and 24 on Hacker News. Looking specifically at our GitHub forks, several stood out as notable. Several prominent governmental organizations forked the system, suggesting the potential for locally-focused AI interfaces to support AI run by public bodies.

Additionally, our manual analysis revealed clear evidence that Open WebUI has already gained traction within the research community. It has been cited in studies exploring its potential for deploying LLMs in education (Zesch et al. 2024; Eronen and Lee 2024), advancing applied agent design workflows (Ishihara et al. 2024), and improving multilingual accessibility in special education—for example, in gloss sign language translation (Othman et al. 2024). A key strength of the system lies in its self-hostable and extensible architecture, which has been particularly beneficial for applications requiring local deployment to address concerns such as data privacy, regulatory compliance, or operating in resource-constrained environments. This versatility is further demonstrated in research focusing on integrating intranet and internet environments for LLMs within organizational infrastructures (Joa et al. [n. d.]). Collectively, these examples highlight Open WebUI’s ability to meet diverse user demands by fostering innovation and empowering users to design and deploy custom AI workflows tailored to their unique contexts and constraints.

Moreover, user-generated content and community experimentation provide compelling evidence of the system’s flexibility for customization—both at high and low levels. At a high level, as discussed in Section 3.4, users have developed and shared plugins that extend the functionality of Open WebUI to interact seamlessly with external services. For example, one popular customization integrates a Google Home plugin, allowing users to control smart home devices directly via the Open WebUI’s web-based interface. Another user-created extension enables real-time Google Search queries from within the Open WebUI, effectively turning the chatbot into an interactive browsing assistant. On the lower level, some community members have gone further by adapting the system for mobile platforms, deploying it on Android devices using Termux. This not only enables local, on-device AI experiences but also demonstrates the lightweight flexibility and platform-agnostic nature of the framework. These use cases illustrate how users are actively extending Open WebUI beyond its original design, repurposing it for new environments and applications that span productivity, usability, and personal automation.

For the purposes of topic modeling, our GitHub data had 4926 documents (titles of issues, pull requests, and discussions), and our other UGC data had 533 documents after dropping duplicates.

Figure 5. A heatmap summarizing the topics in user-generated content from Github. The rows show the top three words in each topic and the columns show topics. Each cell shows how frequently a word (row) appeared in posts matching the corresponding topic (column).

Figure 6. A heatmap summarizing the topics in user-generated content from platforms other than GitHub (YouTube, Reddit, LinkedIn, Hackernews, Twitter, and Medium). The rows show the top three words in each topic and the columns show topics. Each cell shows how frequently a word (row) appeared in posts matching the corresponding topic (column).

Figure 5 summarizes topics we identified in our GitHub data, while Figure 6 covers the UGC data. Each figure shows the top three words from each topic and the labels we assigned each topic based on their top words and key examples.

Looking at these topics in our GitHub data, a key finding was the emphasis on user desire for features that work with local data (“File / Document Uploads”). This resonated with our manual examination of feedback data, in particular, a frequent request by users for “Retrieval Augmented Generation” (RAG), a specific technique in the generative AI space for working with specific documents. In this case, the presence of a topic provided very straightforward feedback: to satisfy user demands, open-source projects have to keep up with new capabilities and features.

Other topics appearing in GitHub engagement included discussion about chat interfaces, server hosting, and discussion of specific issues with Docker and external APIs (e.g., using Open WebUI with the OpenAI API). These suggested that users were using our system in a variety of contexts.

In our models summarizing other UGC data, we also see discussion by users of features such as RAG (leftmost topic), discussion on the local emphasis of our system (third from left), as well as mentions of specific models (stable diffusion, rightmost topic). It is also notable that in the content they posted, people directly discussed open-source funding, a key consideration for the sustainability of similar projects.

Looking manually through our UGC data, we observed broadly four different types of content: tutorial, demonstration (including direct examples of extensibility), testimonial, and integration. In terms of standout examples of UGC, we identified YouTube videos that demonstrated particularly in-depth engagement with Open WebUI (in terms of the effort to create the video, and the engagement with the video itself). Tutorials on YouTube covered installation, how to use multiple AI models, how to work with prompts, how to implement RAG, voice input, and more. This observation suggested that emphasizing the open-source aspect of Open WebUI was, as one might expect, helpful in allowing users to participate in making the system more usable.

To summarize, analyzing organically generated content from users suggests that Open WebUI was able to meet the demand for a local-focused, privacy-friendly interface for using AI models, but that technical issues (e.g., installation) are likely still a barrier to more widespread use. As expected, content posted to GitHub focused on issues whereas content posted to other platforms focused more on promotion, tutorials, and positive feedback. We identified direct areas for improving our system’s usability (address issues with installation, hosting, Docker, external API support) and feature set (continue adding features that support local-first interaction with documents). These findings offer valuable guidance for HCI researchers developing similar toolkit platforms and highlight the practical aspects that directly affect adoption and user experience.

#### 4.2. User-Generated Plugins

In addition to engaging with the project on GitHub and posting in-the-wild content on platforms like YouTube and Reddit, Open WebUIusers also utilized the extensibility of the system by building and openly sharing user-generated plugins: Filters, Pipes, and Actions. The community-driven ecosystem surrounding Open WebUI has generated a considerable volume of these plugins (this volume is a useful indicator that the goals of openness, extensibility, and usability resonated with users). Currently, the user community has contributed 541 unique functions and 276 unique tools to the community platform, with additional plugins available through platforms like GitHub. In this section, we offer a comprehensive overview of notable examples of these user-generated plugins, demonstrating the utility, innovation, and breadth of applications made possible by Open WebUI’s extensibility.

In order to understand how users utilized the extensibility of Open WebUI , we also applied topic modeling to the corpus of user-contributed plugins. Our preprocessing and modeling approach is consistent with that described in Section 4.1, but we extend the stopword list to include terms frequently appearing in plugin descriptions such as “tool”, “function”, “feature”, and “application”. For each identified topic, we select representative extensions based on their probability scores. Our focus in this section is not on reporting the exact distribution of topics, but instead on systematically answering, “What did users do with the extensibility offered by Open WebUI”. We include raw model outputs in an Appendix.

To better contextualize community contributions, we also report each user-generated extension’s number of downloads recorded from the community platform and rounded to the nearest hundred or thousand.

This analysis offers several advantages in this context. It provides a reproducible method to identify meaningful groups of functionality, highlights patterns in use cases, and reduces manual bias in categorization.

##### 4.2.1. Tools

Tools are designed as powerful extensibility mechanisms, allowing users to integrate commands that extend beyond traditional LLM capabilities. By executing external Python scripts or interfacing directly with APIs and external services, these tools significantly augment the interactive and computational possibilities of local and privately hosted LLMs.

We performed topic modeling on the top 100 tools on the community platform by download count to find themes and examples that are representative of the community’s most influential extensions.

Some notable plugin tools contributed by the user community include:

- •

Enhanced Web Scrape [16K Downloads] — A web scraping tool that extracts text content from web pages, supporting user customization and improved filtering.

- •

ComfyUI Image Prompt [552+ Downloads] — A tool that converts images into prompts for image generation workflows, enabling enhanced image-based prompting.

- •

WolframAlpha LLM API [2.6K Downloads] — This tool uses the WolframAlpha LLM API to access knowledge and retrieve information.

- •

Run Code [6.2K Downloads] — Executes Python or Bash code securely within a sandboxed environment.

- •

SQL Server Access [2.9K Downloads] — Provides access to SQL databases, allowing users to query, retrieve, and explore database content.

- •

Stock Reporter [7.6K Downloads] — Gathers stock market data and generates comprehensive reports.

- •

Deep Research (Browser UI) [1.5K Downloads] — Performs real-time research and data retrieval from online sources.

- •

Home Assistant Light Control [642 Downloads] — Enables control and management of smart lights through the platform.

These tools strongly support the stated goals of openness by interfacing with external APIs and sources, while through extensibility, they provide essential new functionalities that extend model capabilities beyond typical language-based tasks.

##### 4.2.2. Functions

Functions provide modular ways to enhance or customize the behavior of the Open WebUI system itself. Recall, these are composed of Filters, Pipes, and Actions, each of which serves unique and clearly delineated purposes.

For the topic modeling, our analysis was limited to the top 30 functions for each class due to the smaller overall set compared with the tools. Only three items were selected per class according to their highest probability scores for brevity.

###### Filters

Filters act as middleware, refining I/O interactions on their way into or out of the LLM interface. Exceptional community-contributed examples, reflecting diverse objectives, include:

- •

GPT Usage Tracker [1K Downloads] — Tracks usage and costs for GPT models, allowing users to monitor and log model interactions.

- •

Google Translate [4.1K Downloads] — Provides automatic translation between a user’s preferred language and the language used by the LLM.

- •

AutoTool Filter (User Setting) [145 Downloads] — Preprocesses user queries to identify and select relevant tools automatically.

Filters directly support our design objectives of openness and privacy by controlling and managing conversational data flows. Specifically, community-generated Filters addressing anonymization and personally identifiable information (PII) redaction align closely with our stated privacy and data protection goals.

###### Pipes

Pipes allow arbitrary Python functionalities to behave analogously to native models in Open WebUI. This greatly simplifies and generalizes how users interact with different models or integrated services. Some user-created Pipes notably include:

- •

Anthropic Claude Model Access [327 Downloads] — Provides API access to the Anthropic Claude models, supporting the latest API features such as prompt caching, document input, and multimodal capabilities.

- •

DeepSeek R1 Think Chain [695 Downloads] — Shows the reasoning chain of the DeepSeek R1 model, helping users follow and understand model decision processes.

- •

DeepSeek V3 R1 Gemini Vision [558 Downloads] — Integrates DeepSeek with Gemini Vision for enhanced image analysis and processing, combining advanced vision capabilities with precise reasoning.

The Pipes promotes extensibility, opening Open WebUI to myriad AI services, modalities (text, vision, images), and cross-model benchmarking.

###### Actions

Actions are UI-driven functionalities that allow direct, explicit invocation by users, complementing more traditional text-only inputs. Key user-generated Actions include:

- •

Mixture of Agents [9.2K Downloads] — Enables combining the strengths of multiple models in a layered, iterative workflow to improve response quality and decision-making.

- •

Visualize Data [13K Downloads] — Generates charts from conversation data, allowing users to quickly view and interpret information within the chat.

- •

Add to Memories [9.1K Downloads] — Saves assistant messages to the user’s memory, supporting persistent context for ongoing interactions.

Actions directly tie into usability, significantly reducing user friction in performing additional tasks within Open WebUI.

Ultimately, examining community-contributed plugins complements the prior UGC analysis by specifically exploring the range of use cases the toolkit can support and highlighting extensions most representative of key functional areas of the platform. We discuss further implications in Section 5.

#### 4.3. User Survey

In addition to analyzing the organic engagement with Open WebUI, we created and posted a voluntary non-paid survey for current users to complete to better understand how the Open WebUI is currently being used and areas of improvement. The survey was
approved by our institution’s ethics review board.

##### 4.3.1. Methods

To gather user feedback, we created an online survey and announced it on the dedicated Discord channel, Open WebUI subreddit, and GitHub Discussions section for the diverse user community within the Open WebUI. The survey was designed to solicit input from users spanning a range of use cases and expertise levels, including developers, end users, and researchers actively engaging with the system. The survey aimed to capture how user interact with Open WebUI , including their use of extensibility features, and overall system functionality.

The survey was structured to collect feedback across five areas: (1) user background and experience with LLMs, (2) how participants use Open WebUI and their motivations for choosing it, (3) experiences with extensibility features such as tools and functions, (4) perceptions of usability, and openness, and (5) overall experience. We included these questions to capture general user feedback and also explicitly assess whether the system meets its three primary design goals through a combination of quantitative and qualitative questions.

The survey included a combination of question types. Likert scale questions measured familiarity, ease of use, and perceptions of transparency/openness. Multiple choice questions captured users experiences with Open WebUI, their uses, and reasons for choosing it. Free-text responses allowed users to provide further details on ease of use, projects that used the extensibility features, impact of openness on their experiences, as well as likes and dislikes. All responses were manually reviewed to identify overall themes for each question. Representative examples from identified themes were reported. For multiple-choice questions, responses outside the predefined options were reported, and for free-text questions, unique or more detailed answers were presented.

Within two weeks starting in August of 2025, we received a total of 20 survey responses from active users from 10 countries: Argentina, Australia, Austria, Brazil, Canada, Germany, Norway, Singapore, the United Kingdom, United States of America. We did not ask any other demographic questions to help preserve privacy. On average, the survey took 5-10 minutes to complete.

##### 4.3.2. Results

Figure 7. Survey results showing reasons for choosing Open WebUI, usability of extensibility features, ease of installation, perceptions of transparency, and the role of open design.

Figure 8. Survey results showing the difficulty of using each extensibility feature.

Here, we provide a summary of participants’ responses to each question.

User Background and LLM Experience
These questions collected basic information about participants, including their familiarity with LLMs, and prior experience using or configuring them. The goal was to contextualize responses by understanding the diversity and expertise of the user base.

Respondents reported a high level of familiarity with LLMs, with an average rating of 4.4 on a 5-point Likert scale. Regarding prior experience, 18 respondents had interacted with LLMs via a user interface, 18 had configured or set up LLMs on their own systems, 9 had created extensions, and 15 had integrated LLMs into other systems or workflows. Most participants had hands-on experience across multiple aspects of LLM use, providing a solid foundation for evaluating Open WebUI .

Usage Patterns and Motivations
Participants were asked about how they use Open WebUI and why they chose it. This included questions about the types of tasks they performed and their key motivations in order to identify common usage patterns and features of the platform users find most valuable.

For usage of Open WebUI, respondents reported a variety of activities: 15 used it for code generation or debugging, 14 for writing or creative work, 17 for research, 12 for personal assistant or automation tasks, 13 for teaching or learning about LLMs, 12 for integrating with external tools or APIs, 12 for recreational uses, and 1 respondent indicated a custom use — “summary and preliminary analysis of different data sources.”

Regarding the key reasons for choosing Open WebUI, respondents highlighted multiple motivations (see Fig. 7A): 16 chose it because it is open-source, transparent, or designed to protect user privacy; 13 valued the active community and contributor-friendly design; 11 cited ease of installation and setup; 7 noted ease of configuration and customization; 12 appreciated the ability to extend with plugins; 17 valued support for multiple LLM models and providers; 2 selected it because it was recommended by others; and 2 provided custom reasons, including: “It’s a great piece of software. Before learning about Open WebUI, I tried coding my own UI. Then immediately stopped once I figured out how to deploy WebUI + Ollama in my homelab,” and “Integrated user role system and permissions, Knowledge base system.” These responses demonstrate that users are motivated by a combination of openness, extensibility, and multi-model support, which aligns with the system’s design goals.

Experiences with Extensibility Features
Tools were the most widely used extensibility feature, reported by 18 participants, followed by Filters with 13, Pipes with 11, and Actions with 10 (see Fig. 7B).

We also asked about projects directly using the extensibility feature and found that 15 of 20 responses described projects or experiments, while 5 participants stated they had not created anything. Four participants mentioned working with Model Context Protocol (MCP) tools or planning MCP integrations, while one built automation features such as deep research, email, and Teams messaging. One person described a central knowledge hub for a marketing team, another added extra context for models with small memory windows, and one created a news feed scraper and summarizer. Individual contributions also included a Document360/Google Drive sync for a knowledge base, LaTeX whitepaper generation for retrieval, code workflows, and basic prompt modifications, such as adding time stamps or adjusting instructions. Three participants reported smaller or unfinished work, including an AssemblyAI transcription attempt, custom filters, configuration of TTs, and use of ChatGPT’s API, while two simply shared GitHub links to their code.

Participants also rated their experience with different extensibility features. For a visualization of the distributions, see Fig. 8. For ease of use, writing tool scripts were rated with a weighted average of 2.7 and a standard deviation of 1.0. This shows that most participants found this task to be of moderate difficulty rather than straightforward. Creating functions for UI/UX changes was rated with a weighted average ease of use of 2.7 and a standard deviation of 1.3.
Here, similar to the Tools results, participants were split, with several finding it difficult and only a few reporting ease of use. Sharing or importing extensions from the community platform had a weighted average ease of use of 4.0 with a standard deviation of 1.3. This indicates that the majority found community extension sharing relatively accessible compared to other extensibility tasks. Our findings show that community-driven sharing mechanisms are comparatively more accessible and easy to use, in contrast to the difficulties users reported when developing or customizing their own extensions.

User Perception of Usability and Openness
This final set of questions elicited user feedback on usability, transparency, openness, and comparisons to other LLM interfaces, along with general impressions and suggestions for improvement. These questions were included to assess whether Open WebUImeets its design goals of openness and usability.

For ease of installation, the weighted average was 3.8, with a standard deviation of 1.2.
(see Fig. 7D). This shows that most participants (12) found installation straightforward, though a smaller group experienced challenges.

Open-ended responses about the setup process reported a mix of straightforward and difficult experiences. Ten participants generally found the initial installation simple, especially when using Docker Compose or the one-command setup, and three noted that adding models was easy. However, several highlighted difficulties: 2 users reported challenges with networking and proxy configuration, poor or outdated documentation (2 participants), and challenges with advanced features such as RAG, MCP tools, and API integrations (5 participants). Two participants also mentioned struggles with permissions management and consistency in handling uploaded files. These responses indicate that while Open WebUI lowers the barrier for getting started, more complex workflows remain difficult to configure.

When asked about transparency, no participants rated the system as “not transparent”, instead, the average transparency rating was 4.1 with a standard deviation of 0.6.
This suggests that most participants felt the platform provided strong transparency into model use, API controls, and data handling, as shown in Fig. 7E.

On the role of open design, participants overwhelmingly emphasized its importance. Many described it as a “primary driver,” “critical,” or “mandatory” for adoption (6 responses), while others highlighted specific benefits such as owning their stack, model agnosticism, or privacy guarantees. Two participants also noted that the open-source nature and “beautiful UI” differentiated Open WebUI from alternatives and made it their preferred choice. Only four participants saw it as secondary or “not a determining factor.” For full visualization, refer to Fig. 7F.

Overall Experience

Participants consistently praised the open-source and extensible nature of Open WebUI, with 8 respondents explicitly mentioning extensibility, openness, modularity, or customizability as a strength. For example, one participant stated: “Degree of customization, aggregate multiple LLM providers. Extremely easy to switch to another model/company when a new SoTA is released (which is very often in the current stage of LLMs).” Another emphasized flexibility, stating: “It can do whatever I want it to.” The user experience and interface was another common theme, highlighted by 7 participants, who described the UI as “good,” “decent,” or “nice.”. Four participants emphasized the ability to integrate or switch between providers, while community involvement was valued by 3 respondents. Furthermore, control and ownership of data were noted by 2 participants. Overall, the most consistent positives were its flexibility, customization, and strong UI, coupled with the value of being an open-source project supported by an engaged community.

Dislikes were more varied, but several themes emerged. Documentation and learning curve issues were mentioned by 5 participants, who found features hard to understand, poorly documented, or confusing in implementation (e.g., RAG, system prompts, tool use). UI customization limitations and performance issues were highlighted by 4 participants, ranging from a lack of theme options to frontend bugs. Another 3 participants pointed to installation or configuration difficulties, while 2 expressed concerns about licensing restrictions and enterprise integration. Two participants also mentioned limited features, such as TTS or markdown support. Lastly, 2 participants reported having no significant dislikes or mentioned some dislike for occasional bugs. In summary, the strongest areas of concern were documentation gaps, UI performance, customization limitations, and installation challenges.

Responses comparing Open WebUI to other platforms were strongly favorable. 13 participants explicitly stated that Open WebUI is better or the best among platforms they have used, often citing extensibility, customization, and feature richness. For example, one participant stated: “It has no direct competitor, all other options are behind in features and extensibility.” Another highlighted flexibility compared to proprietary platforms: “Much better than using ChatGPT’s interface, I like that I can choose the tools to use and the connections to make, and how I can export conversations and choose my database.”
Four participants contrasted Open WebUI positively against specific alternatives, such as LibreChat and AnythingLLM, noting that while these competitors sometimes offered a more polished interface, they lacked Open WebUI’s breadth of features. As one explained: “Tested only AnythingLLM… while their presentation and UI look more polished and complete, it lacks many features Open WebUI has. The user groups and permissions was really the feature that moved us to try Open WebUI”. Three participants reported limited use of other platforms, stating they had little basis for comparison, and 1 participant raised licensing as a drawback despite otherwise viewing Open WebUI as favorable. Overall, the majority of participants saw Open WebUI as preferable to mainstream interfaces and competing open-source projects, particularly because of its customization, integration options, and active development.

### 5. Discussion

Above, we discussed the design of Open WebUI, provided a list of social computing applications that Open WebUI enables, and reported on an early evaluation of our approach, with a focus on how well the system achieved three design goals: simultaneous openness, extensibility, and usability. Here, we discuss several potential consequences of future efforts aimed at making local LLM interfaces easier to use, including benefits for users across various geographic contexts, communities with diverse values, and the benefits of decentralization. We highlight fruitful directions for future work along each of these lines.

Our early evaluation results suggested that the initial design of Open WebUI made significant progress towards meeting its design goals. Early users also reported high levels of experience with LLMs (and self-selected to engage with GitHub, Discord, etc.). Therefore, we encourage future work to explore further how interfaces like Open WebUI may better support the needs of an increasingly broad user population.

#### 5.1. Design Implications for LLM Toolkits

Overall, this work contributes to HCI by revealing how users engage with and extend an open-source LLM toolkit platform. To our knowledge, there has been little HCI work documenting user experiences in an open-source LLM toolkit at scale, making this study an early step toward understanding and highlighting how these interfaces can be designed to support extensible human-AI interaction.

We find that participants consistently value the openness of the platform, the multi-model support, and the level of customization provided. These features were seen as key reasons for choosing Open WebUI over proprietary systems. However, participants also mentioned several challenges related to customization, such as creating new plugin scripts from scratch. In contrast, participants found using community contributions much easier. This points to the important role of the community platform in extensible AI systems for lowering entry barriers and enabling easier experimentation, where the value of the platform is multiplied by users’ ability to share and build upon each other’s work. Furthermore, HCI research should continue to explore ways to simplify the process of using advanced functionalities, such as creating plugins in these toolkits.

We also show the importance of careful interface design of these platforms. Participants valued the clean and intuitive UI, but noted challenges with documentation, configuration, and performance. This reinforces the need to balance extensibility with usability to ensure users can navigate, understand, and use these customization features with appropriate support.

We see several opportunities for future work. First, we encourage HCI researchers and LLM platform developers to engage in more systematic studies of user contributions, experiences, and practices in open-source settings to better understand how to advance these platforms. Second, future research can explore how extensible architectures may be designed to better support both expert and novice users, either through improved methods for onboarding, documentation, or new forms of collaborative extension development. Lastly, further work is needed to understand the social dynamics of Open WebUI, including how users collectively improve the platform, assist one another, and how the interface itself supports this active, collaborative community – features largely absent in proprietary platforms. We hope our work serves as a stepping stone to guide the design of future LLM toolkit systems.

#### 5.2. Additional benefits of openness and extensibility for “local” models

Geographic inclusion: We observed that survey participants hailed from a variety of countries across the world. This suggests that open interfaces can support users in locations that limit access to private LLM offerings. Two major reasons someone might be unable to use an LLM service like ChatGPT or Bard might be local regulations, cost, or lack of stable Internet access (e.g., people living in rural areas or developing countries). In the future, attempts to deploy LLMs in extreme environments (e.g., space) might also benefit. Similarly, organizations stand to benefit from running local LLMs with no outbound data, especially given the availability of a local model whose performance is on par with “GPT-3.5." (Zheng et al. 2023).

“Many models” approach: Furthermore, an open and extensible approach means that users can benefit from many models at once, each potentially containing domain-specific advantages or tuned to a particular set of human values. Individuals could download specialist LLMs to their local devices, enabling access to expert knowledge in various fields, including medicine, engineering, and law. The medical field, in particular, may benefit significantly from this development (Nori et al. 2023; Gu et al. 2021; Tu et al. 2024). Local LLMs may serve as an initial point of contact, offering preliminary diagnoses or health advice, thereby reducing the strain on healthcare systems and freeing up specialists’ time for more critical cases. Of course, mitigating risk will require attention to the challenges of using LLMs in high-stakes scenarios (Meskó and Topol 2023).

Pluralism through online community governance: The platforms where users are discussing and sharing Open WebUIand other local AI tools (e.g., GitHub, Reddit, Discord, HuggingFace, the Open WebUIsocial platform) are of great interest in social computing, especially scholarship on online governance. These platforms require moderation practices (Jiang et al. 2019) (sometimes using bots (Kiene and Hill 2020; Kiene et al. 2019)), and sometimes use governance tools (e.g., (Zhang et al. 2020)) to allow communities to employ voting, juries, and more. Reddit (Baumgartner et al. 2020) and GitHub (Maldeniya et al. 2020) are especially well studied in social computing, but further understanding Discord and any new social platforms will be critical for understanding the future of AI systems.

In a world of many models – collaboratively built and governed through interactions using online platforms – the design of these platforms could be shaped to support a pluralistic approach to values. There remain many open research questions about how models themselves might achieve values pluralism (Sorensen et al. 2023), but it seems likely that online communities can foster broader public engagement with AI governance.

#### 5.3. Future Work and Limitations

Our results suggest that building more open, extensible interfaces for LLMs can enable a number of new directions in HCI research. One particularly exciting direction of research might be applying systems like Open WebUI to the evaluation of AI. The rapid advancement of LLMs has created an “evaluation crisis”, underscoring the need for effective, ethical, and socially responsible evaluation and auditing methods (Xiao et al. 2023). Extensibility can help users to participate in the evaluation of AI, as a system that is flexible enough to accommodate diversity of use cases and user groups, especially in local settings, can actually collect data needed to evaluate AI that otherwise might be expensive or impossible to acquire via a “centralized” private approach. In the case of Open WebUI, this involves creating frameworks that allow users to assess the model’s performance based on parameters that are significant to their specific context.

Above, we noted that the choice to use local LLMs, for individual users or for organizations, will involve navigating trade-offs. Here, we reiterate some of the expected limitations of the local LLM approach and the current implementation of Open WebUI.

First, while some users may see cost savings, ultimately, all LLM users must either pay for API access or pay for compute resources (and associated costs such as energy, maintenance, etc.). Researchers have begun to highlight concerns with the energy use of AI (Schwartz et al. 2020); it is likely that a shift toward local models may decentralize decisions around energy use and compute costs.

Second, we note several system-specific limitations. Survey respondents identified challenges related to installation, server deployment, and hardware constraints. Although Open WebUI was commended for simplifying these processes, participants noted that familiarizing oneself with the system for the first time, and configuring or creating custom extensions, can be challenging. This is especially true as Open WebUI and many other LLM platforms implement extensions through scripts, which are straightforward to import but require some technical expertise to create from scratch.

These findings highlight several directions for future work. First, simplifying system installation and the creation of extensions to better support non-technical users or those without development experience would broaden the accessibility and usability of Open WebUI. Although many existing extensions cover the majority of typical use cases, providing novice users the ability to develop their own extensions easily for highly custom or unique workflows remains important. Second, conducting a larger-scale survey would provide a more comprehensive understanding of user experiences.

### 6. Conclusion

In this paper, we introduced Open WebUI, an open-source LLM toolkit that streamlines the use of local large language models (LLMs) by providing a user-friendly interface for downloading, installing, and managing various models. Open WebUI supports both open-source and proprietary models and provides a collaborative ecosystem in which users can share and import community-contributed extensions and presets. Our evaluations, based on organic user engagement, survey responses, and curated examples of toolkit use in the wild, indicate that Open WebUI is making significant progress toward its design goals of openness, extensibility, and usability. We highlight directions for future work, including simplifying installation and lowering the barrier to creating extensions. Overall, our findings highlight the potential of LLM toolkit platforms and encourage both research and platform developers to contribute to HCI studies that inform the design of future local LLM interfaces.

### 7. Acknowledgments

We thank the global open-source community whose creativity and collaboration have been central to Open WebUI’s development. The efforts of independent maintainers and contributors worldwide, working across borders and areas of expertise, exemplify the potential of open-source collaboration. We also recognize and appreciate the efforts of Open WebUI, Inc. for its role in supporting the broader ecosystem and making Open WebUI publicly available.11
1

Use of the software is governed by the license terms in the official project repository.

This paper is an independent academic study of Open WebUI in the context of AI and HCI research. The authors’ contributions here are limited to analysis and description. Development and maintenance of Open WebUI are carried out independently by the community and Open WebUI, Inc. Any personal contributions by the authors to Open WebUI were made outside their institutional roles. This paper does not claim ownership of the project and should not be read as suggesting institutional endorsement or involvement.

We close by expressing gratitude to all contributors who continue to shape and extend Open WebUI. We look forward to observing its ongoing evolution.

### Conflict of Interest

The lead author is the founder of Open WebUI, Inc., which maintains Open WebUI. This article is an independent academic analysis and was not funded, directed, or otherwise financially supported by Open WebUI, Inc. No confidential or non-public company information was used. The findings and opinions are those of the authors alone and do not represent the views of Open WebUI, Inc. or the authors’ institutions.

###### Trademarks.

Open WebUI is a mark of Open WebUI, Inc. All other names and marks are the property of their respective owners and are used here for identification purposes only.

### References

- (1)

- Any ([n. d.])

[n. d.].

https://anythingllm.com/

- Lob ([n. d.])

[n. d.].

https://lobechat.com/

- Git ([n. d.])

[n. d.].

https://www.librechat.ai/

- ope ([n. d.])

[n. d.].

Open WebUI.

https://github.com/open-webui/open-webui

- Ope (2006)

2006.

The Open Source Definition.

https://opensource.org/osd/.

https://opensource.org/osd/

- Ste (2023)

2023.

5 Steps to Getting Started with Llama 2.

https://ai.meta.com/blog/5-steps-to-getting-started-with-llama-2/

- AIW (2023)

2023.

AI weights are not open "source".

https://opencoreventures.com/blog/2023-06-27-ai-weights-are-not-open-source/

Section: blog.

- Anand et al. (2023)

Yuvanesh Anand, Zach Nussbaum, Adam Treat, Aaron Miller, Richard Guo, Ben Schmidt, GPT4All Community, Brandon Duderstadt, and Andriy Mulyar. 2023.

GPT4All: An Ecosystem of Open Source Compressed Language Models.

arXiv:2311.04931 [cs.CL]

- Anthropic (2024)

Anthropic. 2024.

Claude.

https://claude.ai/

- Antoniak et al. (2019)

Maria Antoniak, David Mimno, and Karen Levy. 2019.

Narrative Paths and Negotiation of Power in Birth Stories.

Proc. ACM Hum.-Comput. Interact. 3, CSCW, Article 88 (nov 2019), 27 pages.

https://doi.org/10.1145/3359190

- Arawjo et al. (2023)

Ian Arawjo, Chelse Swoopes, Priyan Vaithilingam, Martin Wattenberg, and Elena Glassman. 2023.

ChainForge: A Visual Toolkit for Prompt Engineering and LLM Hypothesis Testing.

https://doi.org/10.48550/arXiv.2309.09128

arXiv:2309.09128 [cs].

- Arawjo et al. (2024)

Ian Arawjo, Chelse Swoopes, Priyan Vaithilingam, Martin Wattenberg, and Elena L Glassman. 2024.

ChainForge: A Visual Toolkit for Prompt Engineering and LLM Hypothesis Testing. In Proceedings of the CHI Conference on Human Factors in Computing Systems. 1–18.

- Bai et al. (2022)

Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort, Deep Ganguli, Tom Henighan, Nicholas Joseph, Saurav Kadavath, Jackson Kernion, Tom Conerly, Sheer El-Showk, Nelson Elhage, Zac Hatfield-Dodds, Danny Hernandez, Tristan Hume, Scott Johnston, Shauna Kravec, Liane Lovitt, Neel Nanda, Catherine Olsson, Dario Amodei, Tom Brown, Jack Clark, Sam McCandlish, Chris Olah, Ben Mann, and Jared
Kaplan. 2022.

Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback.

https://doi.org/10.48550/arXiv.2204.05862

arXiv:2204.05862 [cs].

- Barr (2023)

Alistair Barr. 2023.

Meta made its Llama 2 AI model open-source because ’Zuck has balls,’ a former top Facebook engineer says.

https://www.businessinsider.com/meta-llama2-open-source-mark-zuckerberg-balls-replit-amjad-masad-2023-10

- Baumgartner et al. (2020)

Jason Baumgartner, Savvas Zannettou, Brian Keegan, Megan Squire, and Jeremy Blackburn. 2020.

The Pushshift Reddit Dataset.

Proceedings of the International AAAI Conference on Web and Social Media 14 (May 2020), 830–839.

https://ojs.aaai.org/index.php/ICWSM/article/view/7347

- Benkler et al. (2015)

Yochai Benkler, Aaron Shaw, and Benjamin Mako Hill. 2015.

Peer production: A form of collective intelligence.

Handbook of collective intelligence 175 (2015).

- Black et al. (2022)

Sid Black, Stella Biderman, Eric Hallahan, Quentin Anthony, Leo Gao, Laurence Golding, Horace He, Connor Leahy, Kyle McDonell, Jason Phang, et al. 2022.

Gpt-neox-20b: An open-source autoregressive language model.

arXiv preprint arXiv:2204.06745 (2022).

- Blythe and Cairns (2009)

Mark Blythe and Paul Cairns. 2009.

Critical methods and user generated content: the iPhone on YouTube. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (Boston, MA, USA) (CHI ’09). Association for Computing Machinery, New York, NY, USA, 1467–1476.

https://doi.org/10.1145/1518701.1518923

- Bommasani et al. (2021)

Rishi Bommasani, Drew A Hudson, Ehsan Adeli, Russ Altman, Simran Arora, Sydney von Arx, Michael S Bernstein, Jeannette Bohg, Antoine Bosselut, Emma Brunskill, et al. 2021.

On the opportunities and risks of foundation models.

arXiv preprint arXiv:2108.07258 (2021).

- Candel et al. (2023)

Arno Candel, Jon McKinney, Philipp Singer, Pascal Pfeiffer, Maximilian Jeblick, Prithvi Prabhu, Jeff Gambera, Mark Landry, Shivam Bansal, Ryan Chesler, Chun Ming Lee, Marcos V. Conde, Pasha Stetsenko, Olivier Grellier, and SriSatish Ambati. 2023.

h2oGPT: Democratizing Large Language Models.

arXiv:2306.08161 [cs.CL]

- Chen et al. (2023)

Zhihong Chen, Feng Jiang, Junying Chen, Tiannan Wang, Fei Yu, Guiming Chen, Hongbo Zhang, Juhao Liang, Chen Zhang, Zhiyi Zhang, Jianquan Li, Xiang Wan, Benyou Wang, and Haizhou Li. 2023.

Phoenix: Democratizing ChatGPT across Languages.

arXiv:2304.10453 [cs.CL]

- Cheng et al. (2024)

Yu Cheng, Jieshan Chen, Qing Huang, Zhenchang Xing, Xiwei Xu, and Qinghua Lu. 2024.

Prompt sapper: a LLM-empowered production tool for building AI chains.

ACM Transactions on Software Engineering and Methodology 33, 5 (2024), 1–24.

- Contractor et al. (2022)

Danish Contractor, Daniel McDuff, Julia Katherine Haines, Jenny Lee, Christopher Hines, Brent Hecht, Nicholas Vincent, and Hanlin Li. 2022.

Behavioral use licensing for responsible AI. In Proceedings of the 2022 ACM Conference on Fairness, Accountability, and Transparency. 778–788.

- Depounti et al. (2023)

Iliana Depounti, Paula Saukko, and Simone Natale. 2023.

Ideal technologies, ideal women: AI and gender imaginaries in Redditors’ discussions on the Replika bot girlfriend.

Media, Culture & Society 45, 4 (2023), 720–736.

- Eronen and Lee (2024)

Juuso Eronen and Saeun Lee. 2024.

Improving English Education in Japan: Leveraging Large Language Models for Personalized and Skill-Diverse Learning.

(2024).

- Fan et al. (2025)

Dongyang Fan, Vinko Sabolčec, Matin Ansaripour, Ayush Kumar Tarun, Martin Jaggi, Antoine Bosselut, and Imanol Schlag. 2025.

Can Performant LLMs Be Ethical? Quantifying the Impact of Web Crawling Opt-Outs.

arXiv preprint arXiv:2504.06219 (2025).

- Franzen (2023)

Carl Franzen. 2023.

Meta quietly unveils Llama 2 Long AI that beats GPT-3.5 Turbo and Claude 2 on some tasks.

https://venturebeat.com/ai/meta-quietly-releases-llama-2-long-ai-that-outperforms-gpt-3-5-and-claude-2-on-some-tasks/

- Freelon (2021)

Deen Freelon. 2021.

The Post-API Age Reconsidered: Web Science in the ’20s and Beyond. In Proceedings of the 13th ACM Web Science Conference 2021 (Virtual Event, United Kingdom) (WebSci ’21). Association for Computing Machinery, New York, NY, USA, 3.

https://doi.org/10.1145/3447535.3466177

- Følstad and Skjuve (2019)

Asbjørn Følstad and Marita Skjuve. 2019.

Chatbots for customer service: user experience and motivation. In Proceedings of the 1st International Conference on Conversational User Interfaces (CUI ’19). Association for Computing Machinery, New York, NY, USA, 1–9.

https://doi.org/10.1145/3342775.3342784

- Gao et al. (2020)

Leo Gao, Stella Biderman, Sid Black, Laurence Golding, Travis Hoppe, Charles Foster, Jason Phang, Horace He, Anish Thite, Noa Nabeshima, et al. 2020.

The pile: An 800gb dataset of diverse text for language modeling.

arXiv preprint arXiv:2101.00027 (2020).

- Gerganov (2024)

Georgi Gerganov. 2024.

ggerganov/llama.cpp.

https://github.com/ggerganov/llama.cpp

original-date: 2023-03-10T18:58:00Z.

- Goldman (2023)

Sharon Goldman. 2023.

Mistral AI bucks release trend by dropping torrent link to new open source LLM.

https://venturebeat.com/ai/mistral-ai-bucks-release-trend-by-dropping-torrent-link-to-new-open-source-llm/

- Google (2024)

Google. 2024.

Bard - Chat Based AI Tool from Google.

https://bard.google.com/

- Gu et al. (2021)

Yu Gu, Robert Tinn, Hao Cheng, Michael Lucas, Naoto Usuyama, Xiaodong Liu, Tristan Naumann, Jianfeng Gao, and Hoifung Poon. 2021.

Domain-Specific Language Model Pretraining for Biomedical Natural Language Processing.

ACM Trans. Comput. Healthcare 3, 1, Article 2 (oct 2021), 23 pages.

https://doi.org/10.1145/3458754

- Hämäläinen et al. (2023)

Perttu Hämäläinen, Mikke Tavast, and Anton Kunnari. 2023.

Evaluating large language models in generating synthetic hci research data: a case study. In Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems. 1–19.

- Heikkilä ([n. d.])

Heikkilä. [n. d.].

Four trends that changed AI in 2023.

https://www.technologyreview.com/2023/12/19/1085696/four-trends-that-changed-ai-in-2023/

- Hu (2023)

Krystal Hu. 2023.

ChatGPT sets record for fastest-growing user base - analyst note.

Reuters (Feb. 2023).

https://www.reuters.com/technology/chatgpt-sets-record-fastest-growing-user-base-analyst-note-2023-02-01/

- Ishihara et al. (2024)

Shigekazu Ishihara, Taku Ishihara, and Keiko Ishihara. 2024.

Facilitation of Kansei Engineering Design Process With LLM Multi-Agent.

(2024).

- Jiang et al. (2023)

Albert Q. Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Devendra Singh Chaplot, Diego de las Casas, Florian Bressand, Gianna Lengyel, Guillaume Lample, Lucile Saulnier, Lélio Renard Lavaud, Marie-Anne Lachaux, Pierre Stock, Teven Le Scao, Thibaut Lavril, Thomas Wang, Timothée Lacroix, and William El Sayed. 2023.

Mistral 7B.

https://doi.org/10.48550/arXiv.2310.06825

arXiv:2310.06825 [cs].

- Jiang et al. (2024)

Albert Q. Jiang, Alexandre Sablayrolles, Antoine Roux, Arthur Mensch, Blanche Savary, Chris Bamford, Devendra Singh Chaplot, Diego de las Casas, Emma Bou Hanna, Florian Bressand, Gianna Lengyel, Guillaume Bour, Guillaume Lample, Lélio Renard Lavaud, Lucile Saulnier, Marie-Anne Lachaux, Pierre Stock, Sandeep Subramanian, Sophia Yang, Szymon Antoniak, Teven Le Scao, Théophile Gervet, Thibaut Lavril, Thomas Wang, Timothée Lacroix, and William El Sayed. 2024.

Mixtral of Experts.

arXiv:2401.04088 [cs.LG]

- Jiang et al. (2022)

Ellen Jiang, Kristen Olson, Edwin Toh, Alejandra Molina, Aaron Donsbach, Michael Terry, and Carrie J Cai. 2022.

Promptmaker: Prompt-based prototyping with large language models. In CHI Conference on Human Factors in Computing Systems Extended Abstracts. 1–8.

- Jiang et al. (2019)

Jialun Aaron Jiang, Charles Kiene, Skyler Middler, Jed R Brubaker, and Casey Fiesler. 2019.

Moderation challenges in voice-based online communities on discord.

Proceedings of the ACM on Human-Computer Interaction 3, CSCW (2019), 1–23.

- Joa et al. ([n. d.])

Byeongha Joa, Hanseung Seoa, Hyuna Jeonb, Joowon Chac, Jaejun Leec, Seungdon Yeomc, and Yonggyun Yucd. [n. d.].

Development of a Versatile Large Language Model Platform by KAERI: Integrating Intranet and Internet Environments.

([n. d.]).

- Kiene and Hill (2020)

Charles Kiene and Benjamin Mako Hill. 2020.

Who Uses Bots? A Statistical Analysis of Bot Usage in Moderation Teams. In Extended Abstracts of the 2020 CHI Conference on Human Factors in Computing Systems (CHI EA ’20). Association for Computing Machinery, New York, NY, USA, 1–8.

https://doi.org/10.1145/3334480.3382960

- Kiene et al. (2019)

Charles Kiene, Jialun Aaron Jiang, and Benjamin Mako Hill. 2019.

Technological Frames and User Innovation: Exploring Technological Change in Community Moderation Teams.

Proceedings of the ACM on Human-Computer Interaction 3, CSCW (Nov. 2019), 44:1–44:23.

https://doi.org/10.1145/3359146

- Kovacs et al. (2018)

Geza Kovacs, Zhengxuan Wu, and Michael S Bernstein. 2018.

Rotating online behavior change interventions increases effectiveness but also increases attrition.

Proceedings of the ACM on Human-Computer Interaction 2, CSCW (2018), 1–25.

- Kulkarni et al. (2023)

Chinmay Kulkarni, Tongshuang Wu, Kenneth Holstein, Q. Vera Liao, Min Kyung Lee, Mina Lee, and Hariharan Subramonyam. 2023.

LLMs and the Infrastructure of CSCW. In Companion Publication of the 2023 Conference on Computer Supported Cooperative Work and Social Computing (Minneapolis, MN, USA) (CSCW ’23 Companion). Association for Computing Machinery, New York, NY, USA, 408–410.

https://doi.org/10.1145/3584931.3608438

- Liedtke (2023)

Michael Liedtke. 2023.

Google brings its AI chatbot Bard into its inner circle, opening door to Gmail, Maps, YouTube.

https://apnews.com/article/google-artificial-intelligence-bard-gmail-youtube-maps-1229638b82d19afb5226c913821fa1ad

Section: Business.

- Lorenz (2023)

Taylor Lorenz. 2023.

An influencer’s AI clone will be your girlfriend for $1 a minute.

Washington Post (May 2023).

https://www.washingtonpost.com/technology/2023/05/13/caryn-ai-technology-gpt-4/

- Maldeniya et al. (2020)

Danaja Maldeniya, Ceren Budak, Lionel P. Robert Jr., and Daniel M. Romero. 2020.

Herding a Deluge of Good Samaritans: How GitHub Projects Respond to Increased Attention. In Proceedings of The Web Conference 2020 (WWW ’20). Association for Computing Machinery, New York, NY, USA, 2055–2065.

https://doi.org/10.1145/3366423.3380272

- Meskó and Topol (2023)

Bertalan Meskó and Eric J Topol. 2023.

The imperative for regulatory oversight of large language models (or generative AI) in healthcare.

npj Digital Medicine 6, 1 (2023), 120.

- Michael M. Grynbaum (2023)

Ryan Mac Michael M. Grynbaum. 2023.

The Times Sues OpenAI and Microsoft Over A.I. Use of Copyrighted Work.

https://www.nytimes.com/2023/12/27/business/media/new-york-times-open-ai-microsoft-lawsuit.html

- Morgan (2024)

Jeffrey Morgan. 2024.

jmorganca/ollama.

https://github.com/jmorganca/ollama

original-date: 2023-06-26T19:39:32Z.

- Nori et al. (2023)

Harsha Nori, Nicholas King, Scott Mayer McKinney, Dean Carignan, and Eric Horvitz. 2023.

Capabilities of GPT-4 on Medical Challenge Problems.

arXiv: 2303.13375.

https://www.microsoft.com/en-us/research/publication/capabilities-of-gpt-4-on-medical-challenge-problems/

- Nuñez (2023)

Michael Nuñez. 2023.

LLaMA 2: How to access and use Meta’s versatile open-source chatbot right now.

https://venturebeat.com/ai/llama-2-how-to-access-and-use-metas-versatile-open-source-chatbot-right-now/

- OpenAI (2023)

OpenAI. 2023.

ChatGPT: AI Language Model.

https://openai.com/.

Accessed: 2025-08-27.

- OpenAI (2024)

OpenAI. 2024.

ChatGPT.

https://chat.openai.com/

- Othman et al. (2024)

Achraf Othman, Khansa Chemnad, Ahmed Tlili, Ting Da, Huanhuan Wang, and Ronghuai Huang. 2024.

Comparative analysis of GPT-4, Gemini, and Ernie as gloss sign language translators in special education.

Discover Global Society 2, 1 (2024), 1–14.

- Park et al. (2023)

Joon Sung Park, Joseph O’Brien, Carrie Jun Cai, Meredith Ringel Morris, Percy Liang, and Michael S Bernstein. 2023.

Generative agents: Interactive simulacra of human behavior. In Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology. 1–22.

- Poudel and Weninger (2024)

Amrit Poudel and Tim Weninger. 2024.

Navigating the Post-API Dilemma. In Proceedings of the ACM Web Conference 2024 (Singapore, Singapore) (WWW ’24). Association for Computing Machinery, New York, NY, USA, 2476–2484.

https://doi.org/10.1145/3589334.3645503

- Ray (2023)

Partha Pratim Ray. 2023.

ChatGPT: A comprehensive review on background, applications, key challenges, bias, ethics, limitations and future scope.

Internet of Things and Cyber-Physical Systems (2023).

- Reddit (2024)

Reddit. 2024.

Upholding Our Public Content Policy and Updating Our robots.txt file - Upvoted.

https://www.redditinc.com/blog/robot-txt-update

- Ruan et al. (2019)

Sherry Ruan, Liwei Jiang, Justin Xu, Bryce Joe-Kun Tham, Zhengneng Qiu, Yeshuang Zhu, Elizabeth L. Murnane, Emma Brunskill, and James A. Landay. 2019.

QuizBot: A Dialogue-Based Adaptive Learning System for Factual Knowledge. In Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems (Glasgow, Scotland Uk) (CHI ’19). Association for Computing Machinery, New York, NY, USA, 1–13.

https://doi.org/10.1145/3290605.3300587

- Schwartz et al. (2020)

Roy Schwartz, Jesse Dodge, Noah A Smith, and Oren Etzioni. 2020.

Green ai.

Commun. ACM 63, 12 (2020), 54–63.

- Sorensen et al. (2023)

Taylor Sorensen, Liwei Jiang, Jena Hwang, Sydney Levine, Valentina Pyatkin, Peter West, Nouha Dziri, Ximing Lu, Kavel Rao, Chandra Bhagavatula, et al. 2023.

Value Kaleidoscope: Engaging AI with pluralistic human values, rights, and duties.

arXiv preprint arXiv:2309.00779 (2023).

- Studio (2024)

LM Studio. 2024.

LM Studio.

https://lmstudio.ai/

- Touvron et al. (2023)

Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, et al. 2023.

Llama 2: Open foundation and fine-tuned chat models.

arXiv preprint arXiv:2307.09288 (2023).

- Toxtli et al. (2018)

Carlos Toxtli, Andrés Monroy-Hernández, and Justin Cranshaw. 2018.

Understanding Chatbot-Mediated Task Management. In Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems (<conf-loc>, <city>Montreal QC</city>, <country>Canada</country>, </conf-loc>) (CHI ’18). Association for Computing Machinery, New York, NY, USA, 1–6.

https://doi.org/10.1145/3173574.3173632

- Tu et al. (2024)

Tao Tu, Anil Palepu, Mike Schaekermann, Khaled Saab, Jan Freyberg, Ryutaro Tanno, Amy Wang, Brenna Li, Mohamed Amin, Nenad Tomasev, Shekoofeh Azizi, Karan Singhal, Yong Cheng, Le Hou, Albert Webson, Kavita Kulkarni, S Sara Mahdavi, Christopher Semturs, Juraj Gottweis, Joelle Barral, Katherine Chou, Greg S Corrado, Yossi Matias, Alan Karthikesalingam, and Vivek Natarajan. 2024.

Towards Conversational Diagnostic AI.

arXiv:2401.05654 [cs.AI]

- Wang et al. (2023)

Bryan Wang, Gang Li, and Yang Li. 2023.

Enabling conversational interaction with mobile ui using large language models. In Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems. 1–17.

- Wu et al. (2022a)

Tongshuang Wu, Ellen Jiang, Aaron Donsbach, Jeff Gray, Alejandra Molina, Michael Terry, and Carrie J Cai. 2022a.

Promptchainer: Chaining large language model prompts through visual programming. In CHI Conference on Human Factors in Computing Systems Extended Abstracts. 1–10.

- Wu et al. (2022b)

Tongshuang Wu, Michael Terry, and Carrie Jun Cai. 2022b.

Ai chains: Transparent and controllable human-ai interaction by chaining large language model prompts. In Proceedings of the 2022 CHI conference on human factors in computing systems. 1–22.

- Wyrich and Bogner (2024)

Marvin Wyrich and Justus Bogner. 2024.

Beyond Self-Promotion: How Software Engineering Research Is Discussed on LinkedIn. In Proceedings of the 46th International Conference on Software Engineering: Software Engineering in Society (Lisbon, Portugal) (ICSE-SEIS’24). Association for Computing Machinery, New York, NY, USA, 85–95.

https://doi.org/10.1145/3639475.3640113

- Xiao et al. (2023)

Ziang Xiao, Wesley Hanwen Deng, Michelle S. Lam, Motahhare Eslami, Juho Kim, Mina Lee, and Q. Vera Liao. 2023.

Workshop on Human Centered Evaluation and Auditing of Large Language Models (HEAL) CHI’24.

https://heal-workshop.github.io/

- Xiao et al. (2020)

Ziang Xiao, Michelle X. Zhou, Q. Vera Liao, Gloria Mark, Changyan Chi, Wenxi Chen, and Huahai Yang. 2020.

Tell Me About Yourself: Using an AI-Powered Chatbot to Conduct Conversational Surveys with Open-ended Questions.

ACM Transactions on Computer-Human Interaction 27, 3 (June 2020), 15:1–15:37.

https://doi.org/10.1145/3381804

- Yablonski (2024)

Jon Yablonski. 2024.

Laws of UX.

" O’Reilly Media, Inc.".

- Zamfirescu-Pereira et al. (2023a)

JD Zamfirescu-Pereira, Richmond Y Wong, Bjoern Hartmann, and Qian Yang. 2023a.

Why Johnny can’t prompt: how non-AI experts try (and fail) to design LLM prompts. In Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems. 1–21.

- Zamfirescu-Pereira et al. (2023b)

J.D. Zamfirescu-Pereira, Richmond Y. Wong, Bjoern Hartmann, and Qian Yang. 2023b.

Why Johnny Can’t Prompt: How Non-AI Experts Try (and Fail) to Design LLM Prompts. In Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems (<conf-loc>, <city>Hamburg</city>, <country>Germany</country>, </conf-loc>) (CHI ’23). Association for Computing Machinery, New York, NY, USA, Article 437, 21 pages.

https://doi.org/10.1145/3544548.3581388

- Zesch et al. (2024)

Torsten Zesch, Michael Hanses, Niels Seidel, Piush Aggarwal, Dirk Veiel, and Claudia de Witt. 2024.

FernUni LLM Experimental Infrastructure (FLEXI)–Enabling Experimentation and Innovation in Higher Education Through Access to Open Large Language Models.

arXiv preprint arXiv:2407.13013 (2024).

- Zhang et al. (2020)

Amy X. Zhang, Grant Hugh, and Michael S. Bernstein. 2020.

PolicyKit: Building Governance in Online Communities.

In Proceedings of the 33rd Annual ACM Symposium on User Interface Software and Technology. Association for Computing Machinery, New York, NY, USA, 365–378.

https://doi.org/10.1145/3379337.3415858

- Zhang et al. (2024)

Zhiping Zhang, Michelle Jia, Hao-Ping Lee, Bingsheng Yao, Sauvik Das, Ada Lerner, Dakuo Wang, and Tianshi Li. 2024.

“It’s a Fair Game”, or Is It? Examining How Users Navigate Disclosure Risks and Benefits When Using LLM-Based Conversational Agents. In Proceedings of the CHI Conference on Human Factors in Computing Systems. 1–26.

- Zhao et al. (2023)

Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang, Xiaolei Wang, Yupeng Hou, Yingqian Min, Beichen Zhang, Junjie Zhang, Zican Dong, et al. 2023.

A survey of large language models.

arXiv preprint arXiv:2303.18223 (2023).

- Zheng et al. (2023)

Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric P. Xing, Hao Zhang, Joseph E. Gonzalez, and Ion Stoica. 2023.

Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena.

arXiv:2306.05685 [cs.CL]

https://huggingface.co/spaces/lmsys/chatbot-arena-leaderboard

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
