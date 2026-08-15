---
title: "Pika: Empowering Non-Programmers to Author Executable Governance Policies in Online Communities"
person: "nick-vincent"
section: "by"
type: "journal-article"
year: 2024
date: "2024-05-11"
venue: "ACM CHI, 2024"
authors: "Leijie Wang, Nicholas Vincent, Julija Rukanskaitė, Amy X. Zhang"
source_url: "https://dl.acm.org/doi/10.1145/3613904.3642012"
retrieved: "2026-08-13"
content: "full-text"
notes: "OpenAlex W4396833378; CV ref [P15]; Full text from arXiv (https://arxiv.org/html/2310.04329v2); This is the preprint version; the version of record is at https://doi.org/10.1145/3613904.3642012."
---

# Pika: Empowering Non-Programmers to Author Executable Governance Policies in Online Communities

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

- 2.1 Governance in of Online Communities

- 2.2 Tools to Support Governance Policy Authoring and Execution

- 2.3 End-User Programming

- 2.4 Abstractions for Describing Governance in PolicyKit

- 3 Overview of Pika

- 4 Design of Pika’s declarative language

- 4.1 Actions and Procedures

- 4.1.1 Custom Action

- 4.1.2 Custom Procedure

- 4.2 Compiling Declarative Language into Executable Code

- 4.3 Articulating
Policy Components

- 4.3.1 Settings of Policy Components

- 4.3.2 Variables of Policy Components

- 4.4 A Library of Policy Components

- 5 Web Interface

- 5.1 Web Interface

- 5.2 System Implementation

- 6 Evaluation

- 6.1 For Non-Programmers: Authoring Policies with Pika

- 6.1.1 Recruitment and Participants

- 6.1.2 Study procedure

- 6.1.3 Results

- 6.1.4 Common Mistakes and Observations

- 6.2 For Programmers: Authoring Policies with Pika

- 6.2.1 Recruitment and Participants

- 6.2.2 Study Procedures

- 6.2.3 Results

- 6.3 Expressivity of Pika

- 6.3.1 Expressivity of Declarative Language

- 6.3.2 Learnability and Usability of Declarative Language beyond Predefined Tasks

- 6.4 Feedback from Participants

- 7 Discussion

- 7.1 Generalization to Additional Online Platforms

- 7.2 Supporting Deliberative and Participatory Community Governance

- 7.3 Towards Empowering Programmers to Author Policy Components

- 7.4 End-User Programming in Community Governance

- 8 Limitation and Future Work

- 9 Conclusion

- Acknowledgements

- References

License: CC BY-NC-SA 4.0

arXiv:2310.04329v2 [cs.HC] 27 Feb 2024

## Pika: Empowering Non-Programmers to Author Executable Governance Policies in Online CommunitiesDOI: XXXXXXX.XXXXXXXConference: The ACM CHI conference on Human Factors in Computing Systems; May 11–16,
2024; Honolulu, Hawai’iPrice: 15.00ISBN: 978-1-4503-XXXX-X/18/06CCS: Human-centered computing Collaborative and social computing systems and tools

Leijie Wang

email: leijiew@cs.washington.edu

Affiliation: University of Washington
, Seattle
, United States

,
Nicholas Vincent

email: nicholas_vincent@sfu.ca

Affiliation: Simon Fraser University
, British Columbia
, Canada

,
Julija Rukanskaitė

email: julija.rukanskaite@gmail.com

Affiliation: Metagov Project

, Sweden

and
Amy X. Zhang

email: axz@cs.uw.edu

Affiliation: University of Washington
, Seattle
, United States

2023© , 2023;

####### Abstract.

Internet users have formed a wide array of online communities with diverse community goals and nuanced norms. However, most online platforms only offer a limited set of governance models in their software infrastructure and leave little room for customization. Consequently, technical proficiency becomes a prerequisite for online communities to build governance policies in code, excluding non-programmers from participation in designing community governance. In this paper, we present Pika, a system that empowers non-programmers to author a wide range of executable governance policies. At its core, Pika incorporates a declarative language that decomposes governance policies into modular components, thereby facilitating expressive policy authoring through a user-friendly, form-based web interface. Our user studies with 10 non-programmers and 7 programmers show that Pika can empower non-programmers to author policies approximately 2.5 times faster than programmers who author in code. We also provide insights about Pika’s expressivity in supporting diverse policies online communities want.

####### Keywords:

End-user Programming, Online Communities, Community Governance, Declarative Language

### 1. Introduction

Millions of communities gather in online platforms such as Reddit, Slack, and Discord (Kraut and Resnick 2012). These dynamic spaces operate based on the concept of governance, defined as the structures, processes, and cultural norms that oversee community organization, power delegation, and the regulation of user interactions (Fiesler et al. 2018; Preece et al. 2003). Governance policies further articulate the ways in which governance is operationalized in an online community.
A carefully negotiated set of governance policies not only is crucial to the stability of online communities (Ostrom 2000), but also impacts individual well-being and potentially broader social institutions (Noveck 2009; Matias 2016). Reflecting their rich and nuanced community norms, online communities have thus evolved to adopt a diverse spectrum of governance policies (Fiesler et al. 2018; Coleman 2013; Dimitri 2022; Müller-Birn et al. 2013).

However, many online platforms offer only a limited set of governance models in their software infrastructure. Predominantly, they adhere to a role-permission governance model (Zhang et al. 2020; Schneider 2022) where administrators and moderators are granted more privileges than regular users, such as full authority over membership and content moderation (Seering et al. 2019; Niederer and Van Dijck 2010). This governance model, inherited from the earliest online platforms, is no longer a technical necessity but remains the default choice on nearly all major platforms (Schneider 2022). While several platforms support other governance models like reputation systems (Posnett et al. 2012; Lampe and Resnick 2004) or jury systems (Kou and Nardi 2014), these often represent the sole governance option available.

Figure 1. Pika Overview. To enable users to articulate policies in a declarative language, the Pika authoring interface fetches community information from home platforms and loads policy components from the JSON library. After the authoring process, the system generates a policy in the form of declarative language and compiles it into executable code in PolicyKit.

Consequently, a growing number of online communities have started implementing governance policies that mirror their distinct norms, moving away from the default governance model. This shift is evidenced by the prevalence of bots or plugins supporting various governance policies across many online platforms, including Wikipedia (Zheng et al. 2019), Reddit (Chandrasekharan et al. 2019), Github (Wessel et al. 2018), and Twitch (Seering et al. 2018). For instance, in the popular online game Minecraft, there is an array of governance plugins, ranging from temporary bans and surveillance, to distribution of authority (Frey and Sumner 2019). However, the variety of existing bots is still restrictive compared to the rich and ever-evolving norms and needs of online communities. This issue is further exacerbated by the limited customization options these bots offer (Chandrasekharan et al. 2019; Kiene and Hill 2020). Communities would benefit more if they can directly author executable policies tailored to their unique community norms (De Laat 2007).

Unfortunately, authoring governance policies in code requires familiarity with platform software infrastructure and programming expertise, prerequisites that are out of reach for non-programmers (Long et al. 2017). More recently, PolicyKit has emerged as a software infrastructure that enables online communities to implement executable governance policies without worrying about integrating them with platform software (Zhang et al. 2020). Nevertheless, proficiency in Python programming and familiarity with the PolicyKit documentation remain fundamental requirements for authoring policies in PolicyKit.

If authoring code is the primary avenue for building governance policies, then technical proficiency becomes an insurmountable barrier to designing community governance, a value-laden process where there should be no barrier for anyone invested in community governance (Ostrom 2000; Viégas et al. 2007). This has several implications. First, the majority of communities without technical developers have to live with the default governance model and available bots even if they desire other forms of governance. Second, it can also lead to the reinforcement of technocratic autocracies within an online community. Because they cannot comprehend and implement governance policies in code, non-technical members are excluded from auditing and authoring governance policies (Hirschman 1970).

In this work, we present Pika, a novel system that empowers non-programmers to create a broad range of governance policies that are directly executable on their home platforms (Figure 1). Our system consists of three parts.

- •

A declarative language: At its core is a declarative language that decomposes governance policies into modular policy components (Figure 2), thereby enabling expressive policy authoring for non-programmers. For example, while online communities use various governance procedures to make decisions, a core set of procedures are commonly used (e.g., jury, consensus voting). Hence, we can separate the customization of these procedures (e.g., notifying individuals who haven’t voted) from the procedures themselves.

- •

A library of policy components: The modular design makes it possible to have a library of policy components and flexibly add new ones. We implemented a library of policy components (Figure 6) to support the authoring of common policies used by online communities.

- •

An authoring interface: Finally, we built a user-friendly, form-based web interface (Figure 7) for non-programmers to author policies, which are then compiled into executable policies.

We conducted a user study with 10 non-programmers who had experience in community governance to assess Pika’s usability and expressivity. They were asked to author policies using Pika in two distinct governance scenarios.
Additionally, we recruited 7 programmers who were interested in community governance to compare the efficiency of Pika with a baseline of programming policies using PolicyKit. These programmers were required to undertake the same tasks as the non-programmers, with an added task of programming one randomly chosen policy.
Our findings revealed that non-programmers were capable of authoring governance policies via Pika approximately 2.5 times faster than programmers coding the same set of policies.
We also found that Pika was rated by programmers as significantly more usable than the baseline, and that non-programmers also found Pika usable. Finally, we also gained insights about Pika’s expressivity, finding that non-programmer participants can use our declarative language to articulate the majority of policies they proposed.

### 2. Related Work

In this section, we begin by examining the tension between the diverse governance needs of online communities and the limited governance models offered by online platforms. In response to this, online communities have started to build technical governance tooling. This trend inadvertently excludes non-programmers from participating in designing and auditing community governance. To address this, we draw inspirations from the end-user programming literature to empower non-programmers to articulate policies using a declarative language.

#### 2.1. Governance in of Online Communities

Online community governance refers to the systems, structures, processes, and cultural norms that guide, manage, and oversee decision-making within communities (Preece et al. 2003; Williamson 1999).
Within this broad scope, governance policies describe how governance becomes operationalized in online communities. Policies in this context are neither traditional public polices or laws, nor Terms of Service externally imposed by platforms. Instead they articulate both informal norms and formal rules by which communities organize members, delegate power, and regulate user interactions (Fiesler et al. 2018; Butler et al. 2008).
Policies play a critical role in combating online harassment (Chandrasekharan et al. 2019), resolving disputes (Im et al. 2018; Kittur et al. 2007), and even fostering offline political coordination (Aragón et al. 2017; Kling et al. 2015). A carefully negotiated set of policies is vital to the long-term stability and survival of online communities (Ostrom 2000).

Online communities have embraced a diverse spectrum of governance policies. The most studied example is Wikipedia (Müller-Birn et al. 2013; Forte and Bruckman 2008; Lovink et al. 2012) where more than 800 pages are dedicated to articulating various policies and guidelines (Zheng et al. 2019). Policies vary greatly to accommodate diverse norms and needs of individual communities, even when located on the same platform (Fiesler et al. 2018).
Moreover, many online communities learn from offline governance practices. For instance, Wikipedia has an elected board that functions as a judiciary body, tasked with policy interpretation and formal arbitration (Forte and Bruckman 2008). Similarly, the Debian Project is governed by a liberal-democratic constitution that meticulously prescribes the procedures for administrator election and community membership (Coleman 2013). More recently, tech-savvy communities have begun to explore innovative governance practices, such as quadratic voting (Dimitri 2022) and liquid democracy (Hardt and Lopes 2015).

Despite the evident need for a variety of governance policies in online communities, online platforms offer a limited set of governance models in their software infrastructure. Predominantly, these platforms follow a role-permission governance model (Zhang et al. 2020; Schneider 2022). In this model, administrators and moderators are granted more privileges than regular users, such as full authority over membership and content moderation (Seering et al. 2019; Niederer and Van Dijck 2010). It originated from the earliest online communities, such as BBSes (Malloy 2016), Usenet (Spencer and Lawrence 1998), and email-list platforms, where one technical administrator is required to operate the community server. As online communities transitioned from self-hosted servers to a small number of commercial platforms, this governance model is no longer a technical necessity but remains the default choice (Schneider 2022). While several platforms support other governance models like reputation systems (Posnett et al. 2012; Lampe and Resnick 2004) or jury systems (Kou and Nardi 2014), these often represent the sole governance option available.

#### 2.2. Tools to Support Governance Policy Authoring and Execution

Nevertheless, online communities have started to move away from the default governance model via several approaches, a journey that can entail significant efforts and resources. Many online communities manually maintain and execute governance policies that are either implicitly recognized or expressly documented (Fiesler et al. 2018; Forte et al. 2009). However, the manual execution of policies demands substantial human efforts and becomes increasingly infeasible as the community grows (Im et al. 2018; Mnookin 2017). This has led to a noticeable shift towards technical governance tooling (Müller-Birn et al. 2013), characterized by the increasing prevalence of bots or plugins that encapsulate policies into code and automatically execute them (Halfaker and Riedl 2012).
Deployed across various online platforms, including Reddit (Chandrasekharan et al. 2019), GitHub (Wessel et al. 2018), and Twitch (Seering et al. 2018), these bots are used to perform repetitive and laborious tasks regarding content moderation and newcomer onboarding.
In Wikipedia, a significant fraction of the 1,601 registered bots undertake the duty of upholding community standards and regulating user behaviors (Zheng et al. 2019; Geiger and Ribes 2010). In Minecraft, a popular online game, communities have access to an array of governance plugins, ranging from temporary bans and surveillance to the distribution of authority (Frey and Sumner 2019).

However, compared with the rich and ever-evolving norms of online communities, the variety of existing bots is still restrictive. It is evidenced by the complaints that many basic features of offline governance legacies are not available on online platforms (Schneider et al. 2021).
The issue is exacerbated by the limited customization options these bots offer. For instance, Automod on Reddit allows moderators to author only simple rules using regular expressions for removing unwanted messages, offering limited flexibility for alternative moderation actions beyond message removal (Chandrasekharan et al. 2019). As communities’ perception of their desired governance model continually evolves over time (De Laat 2007), there is a growing demand for governance policies specifically tailored to their community norms.

Authoring governance policies in code requires familiarity with platform software infrastructure and programming expertise, prerequisites that are out of reach for non-programmers. Long et al. documented the challenges non-programmers have when requesting or creating Reddit bots (Long et al. 2017). They grapple not only with the complexities of the Reddit API and programming but also with assessing the feasibility of their bot requests. Recently, PolicyKit has enabled online communities to articulate executable governance policies in code without worrying about integrating them with platform APIs (Zhang et al. 2020). Nevertheless, proficiency in programming remains a fundamental requirement for authoring policies in PolicyKit.

If authoring code becomes the primary avenue for building governance policies, then technical proficiency is an insurmountable barrier to participation in designing community governance. This trend has two implications. First, communities without technical developers must adapt to the default governance model a platform offers even when they prefer other forms of governance. They are also obliged to find ways to work with bots that may have been designed for communities with slightly different needs. Second, non-programmer members are inadvertently excluded from discussion, deliberation, and articulation of governance policies in code, a value-laden process where there should be no barrier to participate (Ostrom 2000; Viégas et al. 2007; Geiger 2014).
Consequently, non-technical community leaders are forced to depend on skilled developers for policy implementation, creating a potential disconnect (O’mahony and Ferraro 2007). Meanwhile, non-programmer members struggle to comprehend governance policies in code, which, in turn, hampers their ability to audit these policies and effectively voice their concerns (Hirschman 1970).

#### 2.3. End-User Programming

End-user programming enables non-programmers to tailor computer technologies to meet their personal or professional needs (Scaffidi et al. 2005), such as analyzing data with spreadsheets (Nardi et al. 1990; Hermans et al. 2011), authoring web pages (Verou et al. 2016; Alrashed et al. 2022), or connecting Internet of Things (IoT) devices (Dey et al. 2006; Akiki et al. 2017).
On online platforms, end-user programming systems such as IFTTT (short for “if-this-then-that”) (Ur et al. 2016; Mi et al. 2017) and Zapier enable everyday users to automate tasks, including facilitating email conversations (Kokkalis et al. 2017), and collecting community responses.
Some online platforms also build tools that enable community moderators to define rules and filters to remove unwanted content (Jhaver et al. 2019a; Kiene and Hill 2020). For instance, moderators can configure simple rules using regular expressions to filter unwanted messages (Jhaver et al. 2019a; Jhaver et al. 2022), or create simple conditional statements to trigger different moderation actions (Chandrasekharan et al. 2019).
However, these end-user programming systems offer limited expressivity and are restricted to a narrow scope of community governance policies. In comparison, our system empowers non-programmers to author an extensive array of governance policies.

End-user programming has been enabled through a variety of methods, including programming by demonstration (Dey et al. 2004; Li et al. 2017),
wizard-based interaction (Castelli et al. 2017; Schobel et al. 2016), and natural language programming (Van Kleek et al. 2010; Gulwani and Marron 2014). An overview of these approaches is provided by Myers et al. (Myers et al. 2006) and Barricelli et al. (Barricelli et al. 2019) Central to many approaches is the use of declarative languages. In contrast to imperative languages that specify “how” to achieve a particular outcome, declarative languages focus on the “what”—the desired outcome—without detailing the exact steps to reach it (Satyanarayan et al. 2016). Given their nature, declarative languages can often be paired with visual interfaces, allowing users to interact with higher-level constructs than code.

One notable example of declarative languages is trigger-action programming, in which a user associates a trigger with an action, such that the action is automatically executed when the trigger event occurs. This programming model empowers non-programmers to express automated tasks on smart devices and online platforms (Dey et al. 2006; Brush et al. 2011). But researchers have also criticized its over-simplification and limited expressivity (Huang and Cakmak 2015). For instance, IFTTT does not allow users to create rules with conjunctions of multiple triggers (Ur et al. 2014). We draw design inspiration from trigger-action programming, as a subset of governance policies can be considered specialized automated tasks. Nevertheless, rather than simply conditioning actions on triggers, governance policies often require input from community members and need a more expressive declarative language.

#### 2.4. Abstractions for Describing Governance in PolicyKit

We aim to enable end-users to author a wide range of governance policies that are executable on their home platform of choice.
Since PolicyKit obviates the need to work directly with platform APIs (Zhang et al. 2020), our system builds on top of the open-source PolicyKit infrastructure.
As a result, the abstractions underlying our policy authoring process further extend PolicyKit’s abstractions of actions and procedures.

These two abstractions stem from the observation that, across myriad governance policies, we can describe the specific behavior that is being proposed separately from the rules being used to determine whether that behavior is allowed. Specifically, an action describes an event that can occur within a community and is typically first proposed by a community member. In contrast, a procedure is a structured process that determines whether a proposed action should pass or fail.
For example, a policy might state that “renaming of any channel must first be approved by a random jury of members”. An example of an action governed by this policy might be, “Bob tries to rename the channel #general”, while the procedure would detail the process of selecting, convening, and determining the outcome of a jury.
We break down PolicyKit’s abstractions of actions and procedures into modular components, which form the basis of our declarative language and end-user authoring tool.

In addition to leveraging PolicyKit’s abstractions, we use its policy engine infrastructure, which perpetually monitors actions, checks them against written policies, orchestrates any asynchronous voting that takes place as required by policies, and and executes approved actions on the platform.
Policies written in our declarative language are compiled into Python code readable by PolicyKit.
This enables our system to focus on lowering barriers to policy authoring, as PolicyKit handles execution.

### 3. Overview of Pika

We introduce Pika, a novel system that empowers non-programmers to efficiently author a broad range of executable governance policies using a form-based web interface. Our system is motivated by the following two design goals.

Design Goal I: Empower users to author policies without programming. Since technical proficiency is a prerequisite for building governance policies, non-technical communities are excluded from articulating their policies that adapt to their unique culture and norms.
Even if a community has the technical expertise to implement policies, it is also important to ensure that non-programmer community members can contribute to and evaluate governance policies.

Design Goal II: Enable expressive authoring of policies. Nowadays, online communities enforce a variety of governance policies according to their diverse needs and norms.
This motivates us to ensure that our system provides non-programmers with nearly the same level of expressivity and flexibility as traditional coding.

However, a fundamental tension exists between two design goals. An end-user-friendly language often employs a higher level of abstraction, constraining non-programmers to author policies with nuanced expressiveness (Barricelli et al. 2019).
For example, one potential approach is to enable the sharing of policy templates in code (Castelli et al. 2017).
While non-programmers can easily configure a policy template, they may even struggle to replace the governed action with another one.

To resolve this tension, we draw inspiration from prior systems such as IFTTT (Ur et al. 2016) and Vega-lite (Satyanarayan et al. 2016) to build a declarative language with a modular and decomposable grammar for governance policies. Compared to policy templates, our declarative language provides non-programmers with greater expressivity to articulate their desired policies. Further, policies in a declarative language can be easily embedded in a form-based interface. It can also lower the threshold for non-programmers to understand policies and thus increase the transparency of community governance. Specifically, Pika consists of the following three components.

- •

A declarative language that decomposes a policy into modular policy components with fully specified attributes,

- •

A library of policy components to support the authoring of commonly used policies, and

- •

A form-based authoring interface that guides non-programmers to articulate a policy using declarative language, and compiles the authored policy into an executable policy in PolicyKit.

Figure 2. An Overview of Data Models. Extending PolicyKit’s abstractions of actions and procedures, we further decompose a custom action into a base action and filters, as well as a custom procedure into a base procedure, decorators, and executions. Such decomposition also grants non-programmers more expressivity in articulating a policy. Here we present approaches for users to articulate their governed action and governing procedure in our declarative language.

Figure 3. Definitions of Policy Components

### 4. Design of Pika’s declarative language

While PolicyKit offers valuable abstractions of actions and procedures for policy formulation (Zhang et al. 2020), our design goals compel us to refine these high-level abstractions into a modular grammar. In this section, we are driven to answer the question: what are the components that make up a policy, and how can they be pieced together?
We first introduce the central concepts of custom actions and custom procedures, and then delve deeper into the grammar of our declarative language. Following this, we describe how to compile this language into executable code for use with governance tooling like PolicyKit. Finally, we explain our efforts to build a shared library of policy components. As this section describes specific design choices using unique terms and platform-specific names, we use several fonts to make this section easier to follow: we emphasize different terms (e.g., custom actions) and direct references to PlatformSpecificNames (e.g., SlackRenameChannel).

#### 4.1. Actions and Procedures

As previously discussed in section 2.4, the two main abstractions within PolicyKit are actions and procedures. An action refers to an event initiated by a community member within a community, while a procedure is a structured process that evaluates the potential approval or rejection of a proposed action. Here, we extend these two concepts to custom actions and custom procedures, highlighting the customization options for end-users. In the following, we will explain how we break them down into a series of policy components. The concept policy component is our broad term for capturing all the different modular elements that constitute a policy, namely: base actions, filters, base procedures, decorators, and executions.

##### 4.1.1. Custom Action

Consider a scenario where a policy author wishes to govern the action when a Base User renames the #general channel in a Slack team. As illustrated in Figure 2, this can be articulated as a custom action in our declarative language, comprising the following two policy components.

- •

Base Action: First, the policy author should determine the base action they want to govern. Base actions are defined asthe core set of actions described and facilitated by online platforms. The unique technical affordances of each online platform delineate a limited set of base actions, such as renaming a channel on Slack or creating a post on Reddit. In practice, the set of base actions can be determined by a platform’s API and event listening offerings. Hence, regardless of the action a policy author wants to govern, they can always select one of these base actions as a starting point. In this scenario, the choice would be SlackRenameChannel.

- •

Filters: In the next step, the policy author should select and configure filters to provide more detailed descriptions of their governing action. Here, filters are defined as further specifications that apply to individual fields of a base action. For the base action SlackRenameChannel, authors can specify its action fields: initiator, channel, and new_name. As the governing action in this case restricts the initiator to have the role of Base User and the channel subject to renaming to #general, the author should select the corresponding filters for these two action fields respectively. As an intentional design choice, we restrict each filter to specify one action field and assume that multiple filters for the same base action are combined using the logical operator "and"11
1

If authors want to govern actions that satisfy this or that condition, they can set up two respective policies.. This approach enables us to focus on designing filters independently without worrying about how multiple filters might interact with each other.

Figure 4.(a) presents the resultant declarative language for this custom action.

##### 4.1.2. Custom Procedure

Figure 2 then illustrates how the policy author proceeds to articulate the custom procedure in our declarative language. They first select Jury as the base procedure, which is defined as the backbone of a governing procedure. This concept stems from the observation that, despite the myriad of governing procedures found on online platforms, a core set of governing procedures are commonly used. They could be traditional ones such as consensus voting, a jury, or dictatorship, or more sophisticated ones in tech-savvy communities, such as quadratic voting (Dimitri 2022) or liquid democracy (Hardt and Lopes 2015). While the specifics of these procedures may vary, they can be reduced to a limited set of base procedures that encapsulate their core mechanism. On the other hand, even a simple consensus voting procedure can have a variety of nuances in practice. To facilitate greater expressivity, our declarative language enables authors to customize a base procedure in three distinct ways.

- •

Settings of Base Procedures: First, after specifying a base procedure, policy authors can configure its settings that represent its important parameters. For instance, the number of jurors and the threshold of affirmative votes dictate how a jury procedure operates; authors from a small community might set the required number of jurors to three. Each base procedure define a list of settings as configuration interfaces, enabling initial customization.

- •

Decorators: Second, policy authors might want to add additional customization to their selected base procedure, such as enforcing time restrictions on voting or notifying people who haven’t voted. Such customization does not alter the core mechanism of a base procedure, but rather decorates it. Analogous to decorators in Python, decorators adjust the behavior of a base procedure without tampering with how it determines the final result.

- •

Executions: Finally, policy authors might want to have additional actions occur following the outcome of a procedure. For instance, in addition to executing the governed action when the procedure passes, they might notify community members about the voting outcomes. We term the actions triggered by outcomes of a governing procedure as Executions. Similar to base actions, the set of executions available is determined by platform affordances. However, they are conceptually different: executions describes actions that are to happen, while base actions refer to actions that have already happened.

Figure 4.(c) presents the resultant declarative language for this custom procedure.

Figure 4. (left) A Policy Written in the Declarative Language. This policy is corresponding to users’ configuration in Figure 2. For clarity, a boxed view is used instead of the actual JSON format. Note the references to variables (blue) and settings (red) in the channel and text fields of the execution SlackPostMessage. This execution is set to happen in the channel where the custom action happens and its message refers to the number of jurors and the number of final yes votes from the base procedure.
(right) The Corresponding but Simplified Executable Python Code in PolicyKit. We generate the code by linking and formatting the code snippet for each mentioned policy component according to PolicyKit’s requirements. The declarative language components and their corresponding code segments are color-coded for easy correlation. Similar to decorators in Python, the code of decorators is prepended to the code of the base procedure.

Figure 5. Details of policy components. Policy components are designed in a similar pattern: the name serves as its unique identifier, while the description offers a detailed explanation for end-users. The settings stipulate the necessary user input, complemented by variables that facilitate cross-component references. Each policy component is also paired with a respective code snippet used to compile policies in the declarative language into executable code in PolicyKit.

#### 4.2. Compiling Declarative Language into Executable Code

As illustrated in Figure 4, we built a compiler to translate a policy in the declarative language (left) to the executable Python code in PolicyKit (right). PolicyKit provides access to platform functions and requires a series of Python functions with expected inputs and outputs. Hence, we compile the code snippets associated with each policy component into the respective functions. Similar to decorators in Python, code of selected decorators is prepended to the code of the selected base procedure. This is to ensure decorators override the behavior of the base procedure.

#### 4.3. Articulating
Policy Components

In Pika, policy components act as a bridge connecting programmers and non-programmers: programmers are expected to implement a policy component in code and outline its customization interfaces, which, in turn, allows non-programmers to effortlessly engage in the policy authoring process.
As online communities often use a similar set of policy components, this approach can substantially reduce the workload involved in rebuilding them from scratch and promote the sharing of policy components with non-technical communities. Therefore, it is vital to maintain clearly defined structures for each category of policy components.

As illustrated in Figure 5, all policy components follow a consistent structure, represented using JSON fields and accompanied by a corresponding code snippet.
Specifically, every policy component is characterized by the following JSON fields: an identifier (typically name) and description that describe each policy component to end-users. Moreover, as elaborated below, it is imperative for each policy component to define a list of settings and variables.

##### 4.3.1. Settings of Policy Components

Settings outline potential ways that users can configure a policy component. Beyond settings of a base procedure that we have previously addressed, other policy components also have their respective settings. For example, as depicted in Figure 5, a user can specify the required role for the filter User.Role. They can also set the duration for a decorator that enforces procedure duration or personalize the text of the execution SlackPostMessage. Settings provide a useful abstraction of a policy component so that end-users no longer need to understand the intricate details of its implementation (Design Goal 1).

While the name of a setting may imply expected values from a policy author, it is critical to provide more detailed descriptions for each setting to facilitate user choices and validate their inputs. While categorizing a setting based on its data type (e.g., number, string) might seem natural from a technical standpoint, this approach falls short in achieving both aforementioned objectives. For instance, the setting voting_channel is represented in the backend as a string of random alphanumeric (i.e., channel IDs) rather than its more intuitive, readable names (e.g., #general). Identifying and then inputting the correct value for this setting could be a daunting task for non-programmers. Moreover, we cannot verify the validity of users input simply through data type information.

Therefore, we further enriched the description of a setting by incorporating details about its linked entity, if applicable. Some settings reflect entities within a community, such as CommunityUser and SlackChannel. While data types dictate the representation and storage of a setting in code, entities are more recognizable and intuitive to end-users, facilitating a smoother configuration process (Design Goal 1). For instance, as the setting voting channel permits values of the entity SlackChannel, we could present users with a predefined list of Slack channels fetched from the community.

##### 4.3.2. Variables of Policy Components

Variables of a policy component provide useful information for references across components. While a modular grammar of policies is more accessible and expressive for end-users’ articulation, it also presents a challenge to connect independently implemented policy components. This could inadvertently limit end-users’ ability to fully express certain policies (Design Goal 2). For instance, users may want to cast a vote in the channel subject to renaming or send thank-you messages to the selected jurors after the procedure ends. Such policies are not possible if users cannot reference information about the channel subject to renaming or selected jurors across policy components. To overcome this challenge, we stipulate that each policy component should define a list of variables for references across components. Unlike settings, variables are not open to user configuration but instead, are results of user configuration. Examples of variables include the channel of the base action SlackRenameChannel, or the selected juries of the base procedure Jury.

As users continuously add new policy components in the authoring process, we expect a considerable number of variables in the authoring environment. This can potentially overwhelm users when they attempt to reference a variable for a specific setting, struggling to determine which variable constitutes a valid input for this setting. To reducing the cognitive burden on end-users in such scenarios, entities of variables helps narrow down potential variables by filtering variables of the same entity as the setting (Design Goal 1).

#### 4.4. A Library of Policy Components

While our declarative language offers expressive grammar to describe a policy, it will only become useful to non-programmers when coupled with a diverse library of policy components as building blocks. As a starting point, we implemented a library of policy components to support a decent number of common policies used by online communities. The modular design of our declarative language also leaves room for programmers to add new policy components–it simply involves adding them to the JSON library. We now introduce the library of policy components in more detail.

- •

Base action and Executions. We support a set of common base actions and executions on Slack (e.g., renaming a Slack channel, inviting a user to a Slack channel) and those more closely related to community governance (e.g., granting a role to a user, editing community documents).

- •

Filters. We implemented nearly 20 filters to support further specification of a variety of entities (e.g., CommunityUser, Text, Timestamp, SlackChannel).

- •

Base procedure. As listed in Figure 6, we implemented a series of base procedures that represent the commonly used decision-making procedures by online communities, ranging from Consensus Voting, Benevolent Dictator to more complex procedures such as Ranked Voting, Quadratic Voting, and Liquid Democracy.

- •

Decorators. We focused on the customization of voting procedures and implemented decorators that notify people who have not voted, require all eligible voters to vote, and delay voting checks.

It’s important to highlight that our objective isn’t to narrow down each kind of policy component to the most succinct set possible. Rather, our focus is on fostering a straightforward comprehension for non-programmers.
Hence, we allowed some implemented policy components to share a similar core mechanism. For example, configuring the threshold of a majority vote to be nearly 100% effectively transforms it into a consensus voting procedure. In this way, non-programmers can select procedures they are familiar with, without the necessity of delving into the complex conceptual variances in each category of policy components.

Figure 6. A list of implemented base procedures.

### 5. Web Interface

#### 5.1. Web Interface

Figure 7. The Web Interface of Pika. This interface guides users through the policy articulation process in the following steps, as indicated by the numbered steps in the figure: (1) configure the custom action by selecting base actions and filters, (2) choose and configure the base procedure, (3) choose the decorators, and (4) choose the executions. While technical terms are used to explain these steps here, the web interface employs user-friendly language for non-programmers.
Additionally, the figure highlights several noteworthy interactions, marked by letters. (A) The side panel allows users to select and scrutinize various options for each policy component (e.g., base actions, base procedures, decorators). (B) This section aids users in configuring the settings of each policy component, presenting input boxes with validations that correspond to each setting’s data type and entity. (C) For settings corresponding to a specific entity, such as voting channel, a drop-down menu that includes both matching variables and entities in the community facilitates easier input than a standard input box (D) The "Insert Variables" button enables users to reference variables and settings directly in the text. (E) Users with a basic programming background can access and view the source code for each policy component.

Incorporating both a declarative language and access to the library of policy components, our web interface serves as an important tool for empowering non-programmers to successfully author executable policies. Following the steps outlined in Figure 2, the web interface guides users to author policies as illustrated in Figure 7: Steps 1 and 2 showcase the configuration interface of the custom action and base procedure. At steps 3 and 4, users will then be guided to specify the decorators and executions respectively.

At each step of the authoring process, the left side panel (Figure 7.A) displays a selection of available options along with detailed explanations. Additionally, to enhance system transparency, users with a basic understanding of programming can also view the source code of the selected option (Figure 7.E). In the right panel, users are asked to configure the settings of the selected option (7.B). According to each setting’s data type, we display various input boxes with validations in place. For settings corresponding to a specific entity, a drop-down list replaces the standard input box. For example, for the Vote Channel setting, rather than requiring users to input the channel ID, we pre-populate a drop-down list with Slack channels fetched from the user’s community, allowing for direct selection (7.C).

As we use variables to connect policy components in our declarative language, it is important to make sure that end-users can understand and use them easily. We maintain a global list of variables to tracks them throughout an authoring process. When users start to configure a new setting, we automatically identify and present relevant variables from the global list–matching them based on their respective entity and data types–within a drop-down list for selection. For instance, within the Vote Channel setting drop-down list (7.C), users can find an entry named the channel where the message was renamed, a variable derived from the base action. For settings of the entity Text, we noticed that users may want to reference both settings and variables of diverse data types and entities–for instance, introducing the configuration of a voting procedure in a message sent to eligible voters. Therefore, we’ve integrated an “Insert Variables” button, granting users access to the comprehensive list of variables and settings (7.D).

Figure 8. Outlines of Authoring Tasks for Non-Programmers. During the user study, we presented a community governance scenario that motivates the creation of each policy. Participants were required to parse out the custom action, custom procedure, and executions of each policy from the scenario and articulate them in our system Pika.

#### 5.2. System Implementation

We developed our system within PolicyKit’s Django framework. Our system, hosted on a web server, consists of a frontend web interface (JavaScript, HTML, CSS), a Python backend, and a JSON library for policy components. The backend loads all policy components from the JSON library and fetches community information (e.g., slack channels, community users) via platform API. The web interface then guides users to author a policy in the declarative language. Upon the completion of policy authoring, the web interface gathers the newly authored policy in JSON format, which will then be compiled into executable code compatible with PolicyKit.

### 6. Evaluation

In our evaluation, we examined whether Pika could be learned and used by community members to author a variety of policies in a short amount of time.
Specifically, we aim to address the following three research questions through two user studies. The first study with non-programmer community members primarily assesses Pika’s usability and expressivity. The second study with programmers, on the other hand, evaluates its efficiency compared to a code-based baseline for authoring governance policies, PolicyKit (Zhang et al. 2020). We developed our final study protocol iteratively through three pilot interviews with lab members to ensure its effectiveness.

- •

Learnability and Usability. Can non-programmers use our system to author governance policies?

- •

Efficiency. Can programmers use our system to author policies faster than writing code?

- •

Expressivity. Can non-programmers use our system to author most policies they want to enact?

#### 6.1. For Non-Programmers: Authoring Policies with Pika

##### 6.1.1. Recruitment and Participants

We recruited 10 participants, experienced in community governance on online platforms and not programmers by publishing a call for participation on mailing lists related to community governance. The studies were conducted via video calls, averaging a duration of 79 minutes each, with participants receiving a compensation of $20.

##### 6.1.2. Study procedure

We started our user study with an onboarding session. We first introduced to participants the fundamental concepts of Pika (e.g., policy, action, procedure, execution) through policy examples. We then gave them a tutorial on how to use Pika to author a simple policy, a consensus vote for channel renames, step by step. This process took 18 minutes on average.
Participants were then tasked with authoring policies of incremental difficulty based on two distinct community governance scenarios, as illustrated in Figure 10. The first task, titled Enforcing Channel Membership Governance, pertains to a community’s need for a consensus vote whenever someone invites a new user to join their private channel. It has a similar structure to the example policy in our tutorial to help participants become familiar with Pika. The second task A Structured Election of Community Admins is more challenging: a community wants to trigger a ranked vote election by posting a message like %voteadmin candidate1, candidate2, candidate3. As such command-triggered policies are often used in community governance tools (Slack 2023), it is important to ensure non-programmers can author this kind of policies in our system.

Participants were asked to speak aloud their thoughts and confusion as they worked. Researchers were silent except to clarify the details of task scenarios and the web interface. If they spent over 5 minutes on a subtask but were not close to succeeding, the researchers would offer hints or explain the answer and mark the respective task as failed. We measured the time participants spent on each task and asked them to fill in a post-survey that assesses the task workload and system usability through Task Load Index (Hart and Staveland 1988) and System Usability Scale (Brooke 1996) respectively.

To gain preliminary insights into our system’s expressivity, we asked each participant what governance policies their communities have enforced (either manually or algorithmically) and what kinds of policies they envision authoring using Pika at the end of the study. We will have more detailed discussion about the study process and results of expressivity evaluation in Section 6.3.

##### 6.1.3. Results

9 out of 10 participants successfully completed the first task, and 7 out of 9 successfully completed the second task. One participant had to leave early so did not take part in the second task. On average, participants who succeeded took 7.5 minutes and 8.6 minutes for two tasks respectively. Most participants could quickly learn how to articulate a policy in our system. While the participant who failed in the first task had trouble navigating the Pika, the two participants who failed in the second task struggled with understanding command-triggered policies. Even participants who succeeded also spent a significant amount of time learning how to connect the list of community users extracted from the triggering message to the candidates of the governing procedure.

We asked participants to rate the system’s usability via a post-survey. On a 5-point Likert scale (1–strongly disagree, 5–strongly agree), participants rated 3.90 on average on the statement “I think I would like to use this system frequently” and 2.30 on the statement “I would need a technical person to be able to use this system”. However, participants also acknowledged they should spend some effort learning how to use this system, as evidenced by the rating of 2.90 for “I would still need to learn a lot before using this system,” and 2.80 for “I thought the system was easy to use”.

Figure 9. Results of Two User Studies. We calculated the average times after excluding data from participants who failed to complete the tasks. We observed that most non-programmer participants can use Pika to articulate policies around 2.5 times faster than programmers across two different governance scenarios. We also reported the usability score measured by the System Usability Scale (Brooke 1996). We found that Pika vastly outperformed PolicyKit from the perspective of programmers, and was also rated as usable by non-programmers.

##### 6.1.4. Common Mistakes and Observations

Participants primarily struggled with articulating the custom action in the second task. It proved challenging as the election candidates were derived from the triggering message—this concept of command parameters confounded several participants. Participants were expected to choose a specific filter only texts that begin with a command and are followed by a list of community users for the message field of the base action. This choice allows the list of candidates to be captured as variables and available for references in the base procedure. However, participants often selected the filter only texts that start with the specified word but only changed it upon realizing they could not set the election candidates later. While this challenge partly arose from non-programmers’ unfamiliarity with command parameters, a real-time feedback system that displays what kind of actions are now governed could be beneficial.

Many participants liked the global data list that enables them to reference variables across components easily and create a more generic policy (e.g., a policy that governs any renaming channel actions through a voting procedure in the channel subject to renaming). However, we also noticed participants often tended not to use variables whenever possible. For instance, in the second task, as the channel where the triggering message is posted is always the channel #governance, almost all participants selected the channel #governance directly.

These variables and settings also enable participants to deliver more nuanced messages when a procedure happens, passes, or fails. For instance, they wanted to provide a detailed summary of voting outcomes or to warmly welcome a new channel member. Interestingly, 4 out of 10 participants dedicated half of their authoring time solely to fine-tuning these messages. This behavior underscores a shift of focus from the technical aspects of policy authoring to clear communication with community members. As existing research has highlighted the significance of notification messages in community governance (Geiger et al. 2012), our study further indicates that non-programmers, when equipped with the appropriate system, can introduce fresh perspectives into the policy authoring process.

#### 6.2. For Programmers: Authoring Policies with Pika

##### 6.2.1. Recruitment and Participants

We recruited 7 programmers who are interested in community governance. As we aimed to evaluate the efficiency of our Pika, prior experience in community governance was not a prerequisite for participation. Similarly, familiarity with PolicyKit was not a prerequisite given there are only a few communities actively using PolicyKit. We recruited participants by publishing a call for participation on mailing lists related to community governance and Slack channels of the university CS department. All 7 participants are familiar with Python programming and 4 of them have a basic knowledge of PolicyKit. The user studies were conducted via video calls, with each session averaging a duration of 95 minutes. Participants were compensated with $40.

##### 6.2.2. Study Procedures

The second user study is designed to evaluate the efficiency of Pika. We chose PolicyKit (Zhang et al. 2020) as our baseline for the following reasons. Our literature review revealed that, aside from PolicyKit, there are limited options for programmers to author comprehensive sets of policies. While most online platforms offer tutorials for bot creation, these often demand extensive knowledge of the platform’s software infrastructure and server deployment skills. End-user systems like AutoMod on Reddit support only a limited range of policies, typically for content moderation. While authoring policies in PolicyKit requires familiarity with its documentation, it is still a better baseline than directly implementing bots via platform APIs. In the following, we describe each condition in more details.

System Condition. The system condition for Pika mirrors the non-programmers’ study: programmers started with a Pika tutorial and then authored policies based on two distinct community governance scenarios.

Baseline Condition. We first introduced to participants the basic syntax of PolicyKit and walked them through the implementation of the policy a consensus vote for channel renames. We provided comprehensive API documentation detailing relevant functions and classes. Then participants were asked to author a policy given one randomly selected governance scenario from Figure 10. We limited this task to only one policy to prevent the study from becoming overly time-consuming. We evaluated participants’ performance via a close examination of their code.

Recognizing the difficulty of authoring policies in PolicyKit, we added several facilitating conditions to the baseline condition to make two conditions comparable. Instead of randomizing the order of the two test conditions, we consistently began with the system condition before the baseline condition. This sequence allowed participants to familiarize themselves with crucial concepts before tackling more demanding programming tasks. We also made several simplification in the programming task: for instance, we assumed that all ranked votes are valid, thereby eliminating the need to check the validity of votes. Moreover, participants were allowed to copy the code of the example policy and were exempted from debugging. These arrangements together make our baseline condition a more robust comparison to authoring policies in Pika.

##### 6.2.3. Results

For the system condition, all 6 participants successfully authored two policies using Pika with an average time of 3.6 minutes and 4.4 minutes. In comparison, for the baseline condition, while all participants were able to author the given policy using PolicyKit, they spent considerably longer time, 19.9 minutes on average for the first task and 21.6 minutes for the second (paired t-test, p<0.01p<0.01). During the study, participants spent much time understanding the workflow of PolicyKit engines and looking for relevant functions in the API documentations. The efficiency of Pika becomes even more apparent when considering that participants were not required to debug their implemented policies, a task that might have substantially increased their time usage.

We asked participants to rate the usability of both Pika and PolicyKit via a post-survey. For the Task Load Index survey using a 7-point Likert scale (1–very low, 7–high), participants reported experiencing a significant higher mental workload while using PolicyKit, with average scores being 2.66 points higher for mental demand (paired t-test, p<0.05p<0.05) and 2.17 points higher for effort level (paired t-test, p<0.01p<0.01) than Pika. Regarding the System Usability Score (SUS), Pika vastly outperformed PolicyKit. The average SUS scores were 75.85 for Pika, indicating good usability, and 35.45 for PolicyKit that represents less acceptable user experience. A paired t-test revealed a statistically significant difference between the SUS scores of these two conditions (p<0.01p<0.01). These findings demonstrate that, compared to PolicyKit, Pika significantly improves the ease of authoring governance policies for programmers.

Figure 10. New Policy Components Participants Want. During the study, we asked non-programmer participants about policies they enforced or desired in their communities. Here we list representative examples of new policy components they proposed. As a significant number of policy components participants mentioned have already been supported in our library, we do not include them in the table. Instead, refer to Section 4.4 for more details.

#### 6.3. Expressivity of Pika

To gain an understanding of Pika’s expressivity, we inquired non-programmer community members about policies they enforced or desired in their communities. If our library of policy components supported their needs, participants were asked to author these new policies. In cases where their proposed policies required new policy components or needed integration with other online platforms, participants were instead asked to describe these policies using our declarative language. This process helps us understand (1) how our declarative language can support real-world policy authoring, and (2) how non-programmers can use our declarative language to author policies they desire beyond predefined scenarios. Participants proposed more than 25 policies in total.

##### 6.3.1. Expressivity of Declarative Language

We want to first differentiate between the expressivity of our declarative language and of our library of policy components. As we have only implemented an initial library of policy components, some policies that would fit well into our declarative language still require authoring new components or supporting online platforms other than Slack. As we will discuss in 7.3, a crowdsourcing approach is crucial to enriching this library. We will prioritize the expressivity of our declarative language in this work.

We found that a significant number of proposed policies are supported by our library of components. Many policies govern a variety of community actions through a voting process. These actions span from platform-specific ones, such as regulating community or channel memberships and message posting, to more high-level actions, such as adding new rules to community documents, appointing admins or moderators, or determining action item priorities. For instance, one policy states that if a message posted in the #announcement channel gathers more than five thumb-down emoji votes, it should be deleted with a warning sent to the message sender. In addition, participants also wanted to automate some governance tasks without a voting process. Examples include mandating the invitation of a moderator when a new channel is created or having the command !mods automatically mention all moderators.

Other policies can be described by our declarative language but require the authoring of new policy components.
Most prominently, participants desired governing actions on diverse platforms, such as expense submissions on OpenCollective, appointments of maintainers or contributors on GitHub, or access control on Google Docs. As Pika relies on PolicyKit for action listening and execution, governing actions on other platforms requires the development of the corresponding platform integrations, which is a straightforward process in PolicyKit.
For governing procedures, some participants also envisioned other voting procedures, such as allowing the dictator to override the consensus decision or requiring representatives from different user groups to vote.
In addition, participants also mentioned more decorators, including voting notification through DMs, displaying the time left for a vote, periodic reminders about deliberation topics, and keeping individual votes private.

However, there exists a small set of policies that Pika cannot support for now. This limitation arises from Pika’s focus on event-driven rather than state-driven governance.
Huang (Huang and Cakmak 2015) differentiates between triggers based on events (as instantaneous signals) and states (as Boolean conditions that can be evaluated to be true or false at any time) in trigger-action programming. Participants mentioned some policies that govern states: if the channel admin has been inactive for one month, hold an election for new admins, or if a user has more than 10 warnings, kick the user out of the community. As PolicyKit listens to platform actions through webhooks, we only support policies triggered by event-driven actions. In the future, we plan to set up periodic backend polls to check state triggers.

##### 6.3.2. Learnability and Usability of Declarative Language beyond Predefined Tasks

We found that most non-programmer participants were able to effectively use Pika’s language to map out the policy components for policies they proposed. However, we identified two main challenges. First, while some state triggers can be reframed as actions about state changes (e.g., when a user has received the 10th warning), participants found state expressions more familiar and natural. Second, there was confusion around whether certain functionalities should be categorized as decorators or base procedures. For instance, in a policy that allows a dictator to override a consensus decision, it was unclear whether this required a new procedure (a mixture of dictatorship and consensus voting) or a new decorator (e.g., giving certain individuals higher voting weights).

#### 6.4. Feedback from Participants

The overall reactions to Pika ranged from positive to enthusiastic.
One non-programmer said: “I’m very impressed by the solid basis you have developed, and by how helpful, inviting, and urgently needed, I think it will prove helpful for many online communities and their administrators.”
Along similar lines, another programmer commented, “I would say you’re ready to release it to users to see how that goes.”

Many non-programmer participants felt that Pika would grant them greater agency in community governance.
One user appreciated the exposure to an extensive array of governance possibilities: “Programmers and technical people know what their set of options are so they can start imagining it. This system is really interesting because it starts exposing what options are available that can be played with, what are the things that are captured or not captured in the platform.”
Another participant believed this system can motivate community administrators to document policies: “[This new policy] is a nice idea, but I’m not going to document it because I don’t have a way to enforce it…Why bother creating that out here? [But] this [system] forces our hand as administrators to start saying like, okay well, what are the rules that I would like to have and then see if I can implement them? Because now there’s a way to potentially automate that.”

Even if their community has already had technical developers, participants were enthusiastic about involving non-programmers in the governance process.
One participant believed Pika can be used as a proof of concept to facilitate their communication with developers: “The developers are not usually the ones doing governance. [To ask programmers to develop a policy], you need to have the UI available and easily accessible to people to see what it does. Otherwise, you’re only going to get developers hearing about this.”
More broadly, participants appreciated the value of incorporating non-programmers’ perspective in community governance: “I think it’s helpful to have a governance panel: there are a coder, the governance person, a layman member of the community who are someone who’s like a subject to the rules.”

### 7. Discussion

Pika offers a declarative language to articulate governance in online communities. From our evaluations, we found that Pika can both express a wide range of desired governance policies and is usable to non-programmers and programmers alike. Below, we will describe how Pika unlocks a range of higher-level extensions that could be built on top of it and enables new research directions.

#### 7.1. Generalization to Additional Online Platforms

While we built our system prototype around Slack, our design of the declarative language is not tied to any specific platform and can be easily generalized to other platforms. For example, our conceptualization of base procedures requires only a space for group discussion (e.g., posts, channels, or threads) and a method for response (e.g., emoji reactions, threaded replies, or up-vote/down-vote mechanisms). Extending Pika’s functionality across different platforms is a straightforward process. First, as Pika relies on PolicyKit platform integrations for action listening and execution, it requires the development of the corresponding platform integrations. Once any developer has written a PolicyKit integration, every community on that platform has the ability to install Pika. Due to frequent changes in API standards across platforms, we acknowledge that this still requires dedicated engineering efforts; however, Pika’s design would not need to chance to accommodate the same policies on additional platforms.

Second, our initial library developed for Slack offers a valuable starting point, as many governance procedures are platform-agnostic and can be easily adapted. For instance, as long as the underlying platform integrations use consistently named functions for sending notifications, initiating votes, and enumerating vote outcomes, our implemented voting procedures can be adapted to other platforms via minor changes. Indeed, PolicyKit exposes a unified API to policy authors via the Metagov Gateway library 22
2

https://github.com/metagov/gateway, which implements the same named functions across different platform integrations. Drawing parallels between platform features—like Slack’s workspaces and Discord’s servers, or Slack’s messages and Reddit’s posts—can further facilitate this adaptation process.

#### 7.2. Supporting Deliberative and Participatory Community Governance

Pika supports a transition from a programming-centric to a governance design-centric perspective, which paves the way towards more deliberative and participatory community governance. First, non-programmer community administrators can channel their energy into deliberating their governance policies rather than struggling with coding them. For instance, instead of searching for bots that enable more sophisticated voting processes, communities can focus on discussing which voting process can best reflect community consensus. Similarly, they can spend more time designing detailed and transparent procedural messages to better communicate a policy, a critical aspect of community governance often overlooked from a programming perspective (Jhaver et al. 2019b). Developers can also use Pika to rapidly prototype governance policies.

Second, for non-programmers not involved in designing governance policies, Pika also empowers them to engage in governance discourse. Given that non-programmers constitute the majority of online users today (Nielsen 2016), it is critical to invite them to audit governance policies embedded in code. For instance, Geiger et al. documented that Wikipedians expressed discontent with a bot developed based on inaccurate assumptions regarding social norms and demanded the implementation of an opt-out mechanism (Lovink et al. 2012). By translating governance policies in code to a more accessible declarative language, Pika facilitates a clearer understanding of policies among non-programmers, thereby encouraging them to voice their concerns more effectively.

In the long term, our ambition extends to creating an “app store” for governance (Schneider 2022) which offers communities a variety of governance models beyond the default ones. As the center of this app store, Pika enables communities to consistently evolve their governance. Hence, it becomes feasible to analyze which policies—and their specific configurations—are frequently used. This then opens avenues for comparing governance policies across different communities, leading to the development of more community-tailored policy components.
In addition, such an app store could also motivate community users who have programming expertise to author policy components, as it serves as a dynamic space where programmers of policy components can exchange ideas, receive feedback, and see the real-world impact of their work.

#### 7.3. Towards Empowering Programmers to Author Policy Components

In this work, we prioritized designing an expressive declarative language over building a comprehensive list of policy components. As a result, we only implemented a library of components as a starting point. Our user study has indicated that this library can accommodate a significant number of policies participants wanted. However, to truly unlock Pika’s full potential, crowdsourcing efforts are needed to enrich this shared library.
While programming skills remain required for authoring policy components, developers no longer need to implement a policy from scratch but instead can concentrate on building individual components.
More importantly, Pika facilitates the reuse of policy components across communities. When a new component is added to the library, it becomes readily accessible to other communities. This significantly reduces collective efforts in implementing repetitive governance policies.

However, the current version of Pika only supports adding new components through direct edits to the JSON-formatted library.
This process presents several challenges for programmers. First, programmers might have difficulties in following the specific schema of policy components we enforce to ensure end-user accessibility. Second, coding policy components within PolicyKit is a complex task. It requires not only familiarity with PolicyKit’s documentation but also navigating its limited debugging capabilities. In our study, our programmer participants typically spent about 30 minutes learning PolicyKit grammar and implementing a simplified ranked voting procedure. Enhancing the user-friendliness of these policy components can be more time-consuming, which may involve adding default values and validation for settings and sending procedural messages (e.g., when they cast invalid votes).

To overcome these challenges, we envision introducing a form-based web interface that guides programmers through authoring new components. This interface would ask programmers to specify a component’s descriptive attributes, determine component settings that require user input, expose variables to connect with other components, and finally provide the corresponding code snippet.
This interface could also help programmers author code snippets that adhere to the required format.
Additional tools for debugging, simulation, and testing are also essential to facilitate the component authoring process. Given a component needs to be integrated into a policy to fully operate, this interface should simulate the enforcement of the whole policy, allowing programmers to observe the effectiveness of their authored components.

#### 7.4. End-User Programming in Community Governance

During the design process, we made deliberate design choices to tailor Pika to the needs of non-programmers. At times, this meant sacrificing the expressivity of some aspects of the system.
For instance, while we envisioned a generic filter that captures a command followed by parameters of any type or entity, we realized that this filter would make non-programmers grapple with determining whether a generic parameter can be used for a specific component setting. Therefore, we opted for a more restricted filter for each use case—for instance, one that starts with a command and is followed by a list of community users.
Similarly, to simplify the authoring process for non-programmers, we categorize executions that happen when the procedure starts (e.g., notifying moderators about the start of a voting procedure) as decorators but not as executions in our declarative language.

While we primarily drew design inspiration from trigger-action programming (Dey et al. 2006; Ur et al. 2014), non-programmers can also benefit from other techniques widely used in end-user programming research (Myers et al. 2006; Barricelli et al. 2019).
For instance, a visual programming interface with drag-and-drop components might offer them a more intuitive grasp of policy flows than Pika’s form-based authoring interface (Akiki et al. 2017; Dörner et al. 2011).
Real-time feedback about the expected policy behaviors based on users’ selection can also aid non-programmers in debugging their policies.
Moreover, similar to how people build upon existing recipes in trigger-action programming tools (Ur et al. 2014), Pika could offer a series of representative policies, enabling users to modify these examples as an initial step towards mastering their policy authoring.

Although our declarative language is designed to accommodate a broad spectrum of policies, certain communities might need a specific kind of policies and therefore find an expressive declarative language unnecessarily complex. For instance, financial management platforms (e.g., OpenCollective) might only need policies regarding the categorization and approval process of different expenses. In such scenarios, we envision our declarative language serves as a foundational framework, upon which communities may build custom apps that restrict the expressivity of our declarative language or selectively use components from the library. These custom apps can communicate seamlessly with PolicyKit backend via our declarative language. These apps may also have a simplified authoring interface that integrates with platform clients, enhancing their usability for non-programmer community members.

### 8. Limitation and Future Work

As we focus on empowering non-programmers to author governance policies that are commonly desired, we do not explore explore how Pika can engage community members in making “good” policies.
This limitation arises from the inherent challenge of defining “good” governance, which may vary greatly across communities (Fiesler et al. 2018; Wang and Zhu 2022).
To mitigate this limitation, we have curated a library of policy components, based on what we identified as “best practices” in community governance from prior literature and our observations from deploying PolicyKit with a few communities for several years. We also focus on empowering knowledgeable community members to easily and expressly author policies they want. Furthermore, achieving good governance is often an experiential and learning process (De Laat 2007). Pika can support communities to iteratively develop and refine governance policies. Looking forward, future work could uncover guidelines on designing “good” policies for a given community or provide tools to comprehensively evaluate policies. Other future longitudinal field studies with real-world online communities are also necessary to fully understand Pika’s impact on community policymaking processes.

We also envision having a fine-grained classification inside each category of policy components. For instance, voting procedures share a similar set of settings like eligible voters and voting channels, and can be considered as a special group of base procedures. Correspondingly, there are a group of decorators that are only compatible with these voting procedures, such as notifying voters. In our current implementation, we standardize the naming of shared settings across voting procedures, and ensure that the corresponding decorators reference these standardized names. As we expand our library with additional base procedures and decorators, we aim to clearly define the interfaces for each category of base procedures. This will not only ensure that newly added procedures are compatible with existing decorators, but also help non-programmers determine whether a decorator is applicable to a base procedure.

In addition, as our user studies only illustrate the usability and expressivity of Pika in a controlled lab setting, future longitudinal field studies with real-world online communities should also help further uncover new usability and expressivity issues. Finally, we also plan to support a range of online platforms beyond Slack by developing PolicyKit’s platform integrations and creating a library of policy components.

### 9. Conclusion

In this work, we present Pika, a novel system that empowers non-programmers to create a broad range of governance policies that are directly executable on their home platforms. Our system consists of three parts. At its core, Pika uses a declarative language that decomposes governance into modular policy components, thereby scaffolding an expressive policy authoring process for non-programmers. The modular design also makes it possible to have a library of policy components and flexibly add new ones. We implemented a library of policy components to support the authoring of a number of common policies used by online communities. Finally, we built a user-friendly, form-based web interface to guide non-programmers to author policies based on this declarative language and policy component library. Our user studies with 10 non-programmers and 7 programmers show that Pika can empower non-programmers to author governance policies around 2.5 times faster than programmers who author in code. We also provide insights about Pika’s expressivity in supporting an extensive array of policies that online communities want.

####### Acknowledgements.

### References

- (1)

- Akiki et al. (2017)

Pierre A Akiki, Arosha K
Bandara, and Yijun Yu. 2017.

Visual simple transformations: empowering end-users
to wire internet of things objects.

ACM Transactions on Computer-Human
Interaction (TOCHI) 24, 2
(2017), 1–43.

- Alrashed et al. (2022)

Tarfah Alrashed, Lea
Verou, and David Karger.
2022.

Wikxhibit: Using HTML and Wikidata to Author
Applications that Link Data Across the Web. In
Proceedings of the 35th Annual ACM Symposium on
User Interface Software and Technology. 1–15.

- Aragón et al. (2017)

Pablo Aragón, Andreas
Kaltenbrunner, Antonio Calleja-López,
Andrés Pereira, Arnau Monterde,
Xabier E Barandiaran, and Vicenç
Gómez. 2017.

Deliberative platform design: The case study of the
online discussions in Decidim Barcelona. In Social
Informatics: 9th International Conference, SocInfo 2017, Oxford, UK,
September 13-15, 2017, Proceedings, Part II 9. Springer,
277–287.

- Barricelli et al. (2019)

Barbara Rita Barricelli,
Fabio Cassano, Daniela Fogli, and
Antonio Piccinno. 2019.

End-user development, end-user programming and
end-user software engineering: A systematic mapping study.

Journal of Systems and Software
149 (2019), 101–137.

- Brooke (1996)

John Brooke.
1996.

Sus: a “quick and dirty’usability.

Usability evaluation in industry
189, 3 (1996),
189–194.

- Brush et al. (2011)

AJ Bernheim Brush,
Bongshin Lee, Ratul Mahajan,
Sharad Agarwal, Stefan Saroiu, and
Colin Dixon. 2011.

Home automation in the wild: challenges and
opportunities. In proceedings of the SIGCHI
Conference on Human Factors in Computing Systems.
2115–2124.

- Butler et al. (2008)

Brian Butler, Elisabeth
Joyce, and Jacqueline Pike.
2008.

Don’t look now, but we’ve created a bureaucracy:
the nature and roles of policies and rules in wikipedia. In
Proceedings of the SIGCHI conference on human
factors in computing systems. 1101–1110.

- Castelli et al. (2017)

Nico Castelli, Corinna
Ogonowski, Timo Jakobi, Martin Stein,
Gunnar Stevens, and Volker Wulf.
2017.

What happened in my home? an end-user development
approach for smart home data visualization. In
Proceedings of the 2017 CHI Conference on Human
Factors in Computing Systems. 853–866.

- Chandrasekharan et al. (2019)

Eshwar Chandrasekharan,
Chaitrali Gandhi, Matthew Wortley
Mustelier, and Eric Gilbert.
2019.

Crossmod: A cross-community learning-based system
to assist reddit moderators.

Proceedings of the ACM on human-computer
interaction 3, CSCW
(2019), 1–30.

- Coleman (2013)

E Gabriella Coleman.
2013.

Coding freedom: The ethics and aesthetics
of hacking.

Princeton University Press.

- De Laat (2007)

Paul B De Laat.
2007.

Governance of open source software: state of the
art.

Journal of Management & Governance
11 (2007), 165–177.

- Dey et al. (2004)

Anind K Dey, Raffay
Hamid, Chris Beckmann, Ian Li, and
Daniel Hsu. 2004.

a CAPpella: programming by demonstration of
context-aware applications. In Proceedings of the
SIGCHI conference on Human factors in computing systems.
33–40.

- Dey et al. (2006)

Anind K Dey, Timothy
Sohn, Sara Streng, and Justin Kodama.
2006.

iCAP: Interactive prototyping of context-aware
applications. In Pervasive Computing: 4th
International Conference, PERVASIVE 2006, Dublin, Ireland, May 7-10, 2006.
Proceedings 4. Springer, 254–271.

- Dimitri (2022)

Nicola Dimitri.
2022.

Quadratic voting in blockchain governance.

Information 13,
6 (2022), 305.

- Dörner et al. (2011)

Christian Dörner,
Fahri Yetim, Volkmar Pipek, and
Volker Wulf. 2011.

Supporting business process experts in tailoring
business processes.

Interacting with Computers
23, 3 (2011),
226–238.

- Fiesler et al. (2018)

Casey Fiesler, Jialun
Jiang, Joshua McCann, Kyle Frye, and
Jed Brubaker. 2018.

Reddit rules! characterizing an ecosystem of
governance. In Proceedings of the International
AAAI Conference on Web and Social Media, Vol. 12.

- Forte and Bruckman (2008)

Andrea Forte and Amy
Bruckman. 2008.

Scaling consensus: Increasing decentralization in
Wikipedia governance. In Proceedings of the 41st
Annual Hawaii International Conference on System Sciences (HICSS 2008).
IEEE, 157–157.

- Forte et al. (2009)

Andrea Forte, Vanesa
Larco, and Amy Bruckman.
2009.

Decentralization in Wikipedia governance.

Journal of Management Information Systems
26, 1 (2009),
49–72.

- Frey and Sumner (2019)

Seth Frey and Robert W
Sumner. 2019.

Emergence of integrated institutions in a large
population of self-governing communities.

PloS one 14,
7 (2019), e0216335.

- Geiger et al. (2012)

R Geiger, Aaron Halfaker,
Maryana Pinchuk, and Steven Walling.
2012.

Defense mechanism or socialization tactic?
Improving Wikipedia’s notifications to rejected contributors. In
Proceedings of the International AAAI Conference on
Web and Social Media, Vol. 6. 122–129.

- Geiger (2014)

R Stuart Geiger.
2014.

Bots, bespoke, code and the materiality of software
platforms.

Information, Communication & Society
17, 3 (2014),
342–356.

- Geiger and Ribes (2010)

R Stuart Geiger and
David Ribes. 2010.

The work of sustaining order in Wikipedia: The
banning of a vandal. In Proceedings of the 2010
ACM conference on Computer supported cooperative work.
117–126.

- Gulwani and Marron (2014)

Sumit Gulwani and Mark
Marron. 2014.

Nlyze: Interactive programming by natural language
for spreadsheet data analysis and manipulation. In
Proceedings of the 2014 ACM SIGMOD international
conference on Management of data. 803–814.

- Halfaker and Riedl (2012)

Aaron Halfaker and John
Riedl. 2012.

Bots and cyborgs: Wikipedia’s immune system.

Computer 45,
03 (2012), 79–82.

- Hardt and Lopes (2015)

Steve Hardt and Lia CR
Lopes. 2015.

Google votes: A liquid democracy experiment on a
corporate social network.

(2015).

- Hart and Staveland (1988)

Sandra G Hart and
Lowell E Staveland. 1988.

Development of NASA-TLX (Task Load Index): Results
of empirical and theoretical research.

In Advances in psychology.
Vol. 52. Elsevier,
139–183.

- Hermans et al. (2011)

Felienne Hermans, Martin
Pinzger, and Arie Van Deursen.
2011.

Supporting professional spreadsheet users by
generating leveled dataflow diagrams. In
Proceedings of the 33rd International Conference on
Software Engineering. 451–460.

- Hirschman (1970)

Albert O Hirschman.
1970.

Exit, voice, and loyalty: Responses to
decline in firms, organizations, and states. Vol. 25.

Harvard university press.

- Huang and Cakmak (2015)

Justin Huang and Maya
Cakmak. 2015.

Supporting mental model accuracy in trigger-action
programming. In Proceedings of the 2015 acm
international joint conference on pervasive and ubiquitous computing.
215–225.

- Im et al. (2018)

Jane Im, Amy X Zhang,
Christopher J Schilling, and David
Karger. 2018.

Deliberation and resolution on wikipedia: A case
study of requests for comments.

Proceedings of the ACM on Human-Computer
Interaction 2, CSCW
(2018), 1–24.

- Jhaver et al. (2019a)

Shagun Jhaver, Iris
Birman, Eric Gilbert, and Amy
Bruckman. 2019a.

Human-machine collaboration for content regulation:
The case of reddit automoderator.

ACM Transactions on Computer-Human
Interaction (TOCHI) 26, 5
(2019), 1–35.

- Jhaver et al. (2019b)

Shagun Jhaver, Amy
Bruckman, and Eric Gilbert.
2019b.

Does transparency in moderation really matter? User
behavior after content removal explanations on reddit.

Proceedings of the ACM on Human-Computer
Interaction 3, CSCW
(2019), 1–27.

- Jhaver et al. (2022)

Shagun Jhaver, Quan Ze
Chen, Detlef Knauss, and Amy X Zhang.
2022.

Designing word filter tools for creator-led comment
moderation. In Proceedings of the 2022 CHI
Conference on Human Factors in Computing Systems. 1–21.

- Kiene and Hill (2020)

Charles Kiene and
Benjamin Mako Hill. 2020.

Who uses bots? A statistical analysis of bot usage
in moderation teams. In Extended abstracts of the
2020 CHI conference on human factors in computing systems.
1–8.

- Kittur et al. (2007)

Aniket Kittur, Bongwon
Suh, Bryan A Pendleton, and Ed H Chi.
2007.

He says, she says: conflict and coordination in
Wikipedia. In Proceedings of the SIGCHI conference
on Human factors in computing systems. 453–462.

- Kling et al. (2015)

Christoph Kling,
Jérôme Kunegis, Heinrich
Hartmann, Markus Strohmaier, and
Steffen Staab. 2015.

Voting behaviour and power in online democracy: A
study of LiquidFeedback in Germany’s Pirate Party. In
Proceedings of the International AAAI Conference on
Web and Social Media, Vol. 9. 208–217.

- Kokkalis et al. (2017)

Nicolas Kokkalis,
Chengdiao Fan, Johannes Roith,
Michael S Bernstein, and Scott
Klemmer. 2017.

Myriadhub: Efficiently scaling personalized email
conversations with valet crowdsourcing. In
Proceedings of the 2017 CHI Conference on Human
Factors in Computing Systems. 73–84.

- Kou and Nardi (2014)

Yubo Kou and Bonnie A
Nardi. 2014.

Governance in League of Legends: A hybrid system.

FDG 7
(2014), 1.

- Kraut and Resnick (2012)

Robert E Kraut and Paul
Resnick. 2012.

Building successful online communities:
Evidence-based social design.

Mit Press.

- Lampe and Resnick (2004)

Cliff Lampe and Paul
Resnick. 2004.

Slash (dot) and burn: distributed moderation in a
large online conversation space. In Proceedings of
the SIGCHI conference on Human factors in computing systems.
543–550.

- Li et al. (2017)

Toby Jia-Jun Li, Amos
Azaria, and Brad A Myers.
2017.

SUGILITE: creating multimodal smartphone automation
by demonstration. In Proceedings of the 2017 CHI
conference on human factors in computing systems.
6038–6049.

- Long et al. (2017)

Kiel Long, John Vines,
Selina Sutton, Phillip Brooker,
Tom Feltwell, Ben Kirman,
Julie Barnett, and Shaun Lawson.
2017.

" Could You Define That in Bot Terms"? Requesting,
Creating and Using Bots on Reddit. In Proceedings
of the 2017 CHI Conference on Human Factors in Computing Systems.
3488–3500.

- Lovink et al. (2012)

Geert Lovink, Nathaniel
Tkacz, Joseph M Reagle, Dan
O’Sullivan, Lawrence Liang, Amila
Salah, Cheng Gao, Krzystztof Suchecki,
Andrea Scharnhorst, R Geiger,
et al. 2012.

Critical point of view: A Wikipedia reader.

(2012).

- Malloy (2016)

Judy Malloy.
2016.

The origins of social media.

(2016).

- Matias (2016)

J Nathan Matias.
2016.

Going dark: Social factors in collective action
against platform operators in the Reddit blackout. In
Proceedings of the 2016 CHI conference on human
factors in computing systems. 1138–1151.

- Mi et al. (2017)

Xianghang Mi, Feng Qian,
Ying Zhang, and XiaoFeng Wang.
2017.

An empirical characterization of IFTTT: ecosystem,
usage, and performance. In Proceedings of the 2017
Internet Measurement Conference. 398–404.

- Mnookin (2017)

Jennifer L Mnookin.
2017.

Virtual (ly) law: The emergence of law in
LambdaMOO.

In Law and Society Approaches to
Cyberspace. Routledge, 645–701.

- Müller-Birn et al. (2013)

Claudia Müller-Birn,
Leonhard Dobusch, and James D
Herbsleb. 2013.

Work-to-rule: the emergence of algorithmic
governance in Wikipedia. In Proceedings of the 6th
International Conference on Communities and Technologies.
80–89.

- Myers et al. (2006)

Brad A Myers, Amy J Ko,
and Margaret M Burnett. 2006.

Invited research overview: end-user programming.
In CHI’06 extended abstracts on Human factors in
computing systems. 75–80.

- Nardi et al. (1990)

Bonnie A Nardi, James R
Miller, et al. 1990.

The spreadsheet interface: A basis for end
user programming. Vol. 10.

Hewlett-Packard Laboratories.

- Niederer and Van Dijck (2010)

Sabine Niederer and
José Van Dijck. 2010.

Wisdom of the crowd or technicity of content?
Wikipedia as a sociotechnical system.

New media & society 12,
8 (2010), 1368–1387.

- Nielsen (2016)

Jakob Nielsen.
2016.

The Distribution of Users’ Computer Skills: Worse
Than You Think.

https://www.nngroup.com/articles/computer-skill-levels/

Accessed: 13-08-2023.

- Noveck (2009)

Beth Simone Noveck.
2009.

Wiki government: How technology can make
government better, democracy stronger, and citizens more powerful.

Brookings Institution Press.

- O’mahony and Ferraro (2007)

Siobhán O’mahony and
Fabrizio Ferraro. 2007.

The emergence of governance in an open source
community.

Academy of Management Journal
50, 5 (2007),
1079–1106.

- Ostrom (2000)

Elinor Ostrom.
2000.

Collective action and the evolution of social
norms.

Journal of economic perspectives
14, 3 (2000),
137–158.

- Posnett et al. (2012)

Daryl Posnett, Eric
Warburg, Premkumar Devanbu, and
Vladimir Filkov. 2012.

Mining stack exchange: Expertise is evident from
initial contributions. In 2012 international
conference on social informatics. IEEE, 199–204.

- Preece et al. (2003)

Jenny Preece, Diane
Maloney-Krichmar, and Chadia Abras.
2003.

History of emergence of online communities.

Encyclopedia of Community
(01 2003).

- Satyanarayan et al. (2016)

Arvind Satyanarayan,
Dominik Moritz, Kanit Wongsuphasawat,
and Jeffrey Heer. 2016.

Vega-lite: A grammar of interactive graphics.

IEEE transactions on visualization and
computer graphics 23, 1
(2016), 341–350.

- Scaffidi et al. (2005)

Christopher Scaffidi, Mary
Shaw, and Brad Myers. 2005.

Estimating the numbers of end users and end user
programmers. In 2005 IEEE Symposium on Visual
Languages and Human-Centric Computing (VL/HCC’05). IEEE,
207–214.

- Schneider (2022)

Nathan Schneider.
2022.

Admins, mods, and benevolent dictators for life:
The implicit feudalism of online communities.

New Media & Society 24,
9 (2022), 1965–1985.

- Schneider et al. (2021)

Nathan Schneider,
Primavera De Filippi, Seth Frey,
Joshua Z Tan, and Amy X Zhang.
2021.

Modular politics: Toward a governance layer for
online communities.

Proceedings of the ACM on Human-Computer
Interaction 5, CSCW1
(2021), 1–26.

- Schobel et al. (2016)

Johannes Schobel,
Rüdiger Pryss, Marc Schickler,
Martina Ruf-Leuschner, Thomas Elbert,
and Manfred Reichert. 2016.

End-user programming of mobile services: empowering
domain experts to implement mobile data collection applications. In
2016 IEEE International Conference on Mobile
Services (MS). IEEE, 1–8.

- Seering et al. (2018)

Joseph Seering, Juan Pablo
Flores, Saiph Savage, and Jessica
Hammer. 2018.

The social roles of bots: evaluating impact of bots
on discussions in online communities.

Proceedings of the ACM on Human-Computer
Interaction 2, CSCW
(2018), 1–29.

- Seering et al. (2019)

Joseph Seering, Tony
Wang, Jina Yoon, and Geoff Kaufman.
2019.

Moderator engagement and community development in
the age of algorithms.

New Media & Society 21,
7 (2019), 1417–1443.

- Slack (2023)

Slack. 2023.

Enabling interactivity with Slash Commands.

https://api.slack.com/interactivity/slash-commands

Accessed: 04-09-2023.

- Spencer and Lawrence (1998)

Henry Spencer and David
Lawrence. 1998.

Managing Usenet.

O’Reilly & Associates, Inc.

- Ur et al. (2014)

Blase Ur, Elyse McManus,
Melwyn Pak Yong Ho, and Michael L
Littman. 2014.

Practical trigger-action programming in the smart
home. In Proceedings of the SIGCHI conference on
human factors in computing systems. 803–812.

- Ur et al. (2016)

Blase Ur, Melwyn Pak
Yong Ho, Stephen Brawner, Jiyun Lee,
Sarah Mennicken, Noah Picard,
Diane Schulze, and Michael L Littman.
2016.

Trigger-action programming in the wild: An analysis
of 200,000 ifttt recipes. In Proceedings of the
2016 CHI Conference on Human Factors in Computing Systems.
3227–3231.

- Van Kleek et al. (2010)

Max Van Kleek, Brennan
Moore, David R Karger, Paul André,
and MC Schraefel. 2010.

Atomate it! end-user context-sensitive automation
using heterogeneous information sources on the web. In
Proceedings of the 19th international conference on
World wide web. 951–960.

- Verou et al. (2016)

Lea Verou, Amy X Zhang,
and David R Karger. 2016.

Mavo: creating interactive data-driven web
applications by authoring HTML. In Proceedings of
the 29th Annual Symposium on User Interface Software and Technology.
483–496.

- Viégas et al. (2007)

Fernanda B Viégas,
Martin Wattenberg, and Matthew M
McKeon. 2007.

The hidden order of Wikipedia. In
Online Communities and Social Computing: Second
International Conference, OCSC 2007, Held as Part of HCI International 2007,
Beijing, China, July 22-27, 2007. Proceedings 2. Springer,
445–454.

- Wang and Zhu (2022)

Leijie Wang and Haiyi
Zhu. 2022.

How are ML-Based Online Content Moderation Systems
Actually Used? Studying Community Size, Local Activity, and Disparate
Treatment. In Proceedings of the 2022 ACM
Conference on Fairness, Accountability, and Transparency.
824–838.

- Wessel et al. (2018)

Mairieli Wessel,
Bruno Mendes De Souza, Igor Steinmacher,
Igor S Wiese, Ivanilton Polato,
Ana Paula Chaves, and Marco A Gerosa.
2018.

The power of bots: Characterizing and understanding
bots in oss projects.

Proceedings of the ACM on Human-Computer
Interaction 2, CSCW
(2018), 1–19.

- Williamson (1999)

Oliver E Williamson.
1999.

Strategy research: governance and competence
perspectives.

Strategic management journal
20, 12 (1999),
1087–1108.

- Zhang et al. (2020)

Amy X Zhang, Grant Hugh,
and Michael S Bernstein.
2020.

PolicyKit: building governance in online
communities. In Proceedings of the 33rd Annual ACM
Symposium on User Interface Software and Technology.
365–378.

- Zheng et al. (2019)

Lei Zheng, Christopher M
Albano, Neev M Vora, Feng Mai, and
Jeffrey V Nickerson. 2019.

The roles bots play in Wikipedia.

Proceedings of the ACM on Human-Computer
Interaction 3, CSCW
(2019), 1–20.

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
