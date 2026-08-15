---
title: "Push and Pull: A Framework for Measuring Attentional Agency on Digital Platforms"
person: "nick-vincent"
section: "by"
type: "journal-article"
year: 2025
date: "2025-06-23"
venue: "ACM FAccT, 2025"
authors: "Zachary Wojtowicz, Shrey Jain, Nicholas Vincent"
source_url: "https://dl.acm.org/doi/10.1145/3715275.3732043"
retrieved: "2026-08-13"
content: "full-text"
notes: "OpenAlex W4411541752; CV ref [P17]; Full text via the OpenAlex Content API (GROBID TEI of the OA PDF) (https://content.openalex.org/works/W4411541752.grobid-xml)."
---

# Push and Pull: A Framework for Measuring Attentional Agency on Digital Platforms

## Full text

We propose a framework for measuring attentional agency, which we define as a user's ability to allocate attention according to their own desires, goals, and intentions on digital platforms that use statistical learning to prioritize informational content.Such platforms extend people's limited powers of attention by extrapolating their preferences to large collections of previously unconsidered informational objects.However, platforms typically also allow users to influence the attention of other users in various ways.We introduce a formal framework for measuring how much a given platform empowers each user to both pull information into their own attention and push information into the attention of others.We also use these definitions to clarify the implications of generative foundation models and other recent advances in AI for the structure and efficiency of digital platforms.We conclude with a set of possible strategies for better understanding and reshaping attentional agency online.


## Introduction

"The summation of human experience is being expanded at a prodigious rate, and the means we use for threading through the consequent maze to the momentarily important item is the same as was used in the days of square-rigged ships... Consider a future device... in which an individual stores all his books, records, and communications, and which is mechanized so that it may be consulted with exceeding speed and flexibility.It is an enlarged intimate supplement to his memory." -Vannevar Bush, As We May Think, 1945 The original promise of the web was to create an interconnected network of information that could, in the words of Tim Berners-Lee, "grow and evolve with the organization and the projects it describes" [6].Early advocates of expanding the web "world wide" via the internet argued that limited access to information was a substantial bottleneck constraining both technological innovation and economic development.It seemed to follow logically that making the world's informational resources accessible online would greatly expand what humanity could accomplish.

In the decades since, the internet has grown precipitously, yet its originally envisioned benefits remain only partially realized.As it turns out, simply increasing the volume of freely available information online has not automatically produced a commensurately more well-informed global populace, in part because attentional constraints sharply limit what people can actually absorb and process [42].As Herbert Simon [1971] so presciently pointed out in the early days of the information age, decades before the world wide web was introduced:

"In an information-rich world, the wealth of information means a dearth of something else: a scarcity of whatever it is that information consumes.What information consumes is rather obvious: it consumes the attention of its recipients.Hence a wealth of information creates a poverty of attention and the need to allocate that attention efficiently." Thus, attentional limitations mean that the practical utility of the internet depends critically on our methods for organizing and navigating the vast quantities of information it contains.Indeed, the limitations imposed by human attention mean that adding information to the internet without concomitant advances in search technology can actually reduce its overall functionality.Past a certain scale, attentional limitations necessitate curation, which, in turn, inevitably grants influence to whoever controls the curatorial process.We call this the internet's fundamental attention problem.

In theory, the internet is a neutral suite of protocols that enable people to freely transmit information between computers on demand.In practice, however, a collection of platforms built on top of these core protocols mediate which information flows actually take place.A key insight motivating the present work is that many prominent platform categories (e.g., search engines, content libraries, social media sites, matching platforms, online marketplaces, and, increasingly, consumer AI systems) all create value by helping people overcome the internet's fundamental attention problem outlined above.

In fact, many platforms accomplish this goal in essentially the same way-namely, by inferring people's attentional preferences, then algorithmically extrapolating them to intractably large sets of unconsidered informational objects (e.g., websites, products, people, content, messages, stories, and posts; see Table 1) [51,53].To echo Vannevar Bush, platforms have become the "means we use for threading through the consequent maze to the momentarily important item" [12].

The algorithms that platforms employ to infer and extrapolate users' attentional preferences play a pivotal role in shaping who has agency on the internet and, increasingly, the world at large.In this paper, we introduce a formal framework for measuring the attentional agency that a platform accords to each of its users.We define attentional agency as the capacity to allocate attention according to personal desires, goals, and intentions.Our framework offers a mathematical formulation of this concept that: (1) clarifies how various institutions currently solve the internet's fundamental attention problem, (2) furnishes operational measures of attentional agency that can be used to identify differences across users for any given platform, and (3) lends insight into how generative foundation models (GFMs) and other advances in artificial intelligence will impact the current paradigm for matching information and attention on the internet.


## Summary of our framework

In using the term "agency" throughout this paper, we intentionally maintain a narrow focus on people's capacity to influence what they and others see on a given digital platform, acknowledging that this leaves out other potentially rich notions of agency (e.g., the specific actions a platform makes available to users). 1 The motivation for this approach is that it yields measures that are immediately calculable using information that platforms already gather in the process of delivering services to users, and can therefore be readily implemented by technologists and policymakers. 2he fact that many prominent platforms are oriented around solving the same underlying preference inference and extrapolation problem enables us to formalize attentional agency using a common mathematical framework-a generalization of the "discounted cumulative gain" measure used in ranking systems [35].The general nature of this approach enables us to abstract away from many idiosyncrasies that distinguish platforms (e.g., whether they sort websites, videos, or restaurants) and address a fundamental question: who has attentional agency?Specifically, our analysis begins with the observation that many information flows on the internet take the form of a stylized interaction between three parties:

(1) An agent seeking to allocate their limited attention to informational objects that they themselves value highly.On some platforms, agents and advocates are non-overlapping groups of users (e.g., job-seekers versus employers on a job board); on others, however, they are the same users acting in different capacities, either simultaneously or at different points in time (e.g., users of a dating app who both view profiles and want their own profile to be widely viewed).

As we show in greater detail below, when an agent and advocate have sharply conflicting priorities, a platform often cannot deliver maximal value to both simultaneously.An influencer trying to "make a name for themselves, " for example, might want their work to be seen by as many people as possible, while other users only want to see content that is related to their personal interests.We define two separate measures that capture how much attentional value a platform delivers to both agents and advocates.

Pull: The amount of attentional value a platform delivers to an agent as a fraction of what it is technologically prepared to deliver them given its current knowledge of agent preferences.Push: The amount of attentional value a platform delivers to an advocate as a fraction of what it is technologically prepared to deliver them given its current knowledge of agent preferences.

Push and pull are not necessarily zero sum.Indeed, many forms of social interactions allow people to unilaterally enter into the attention of others (e.g., the practice of sending a cold-email, which can have net positive value for the recipient).In practice, however, increasing push often does reduce pull on digital platforms: limited attention means that pushing information into an agent's attention tends to exclude other objects they would have preferred to see more.As we elaborate in Section 3.2, the relative alignment of agent and advocate preferences and other primitives of a platform environment determine the rate at which these two measures trade off against one another.

Our framework defines pull and push at the level of an individual user for a given platform.These estimates can then easily be aggregated across users or systems.For instance, our push and pull measurements could be used to measure the attentional agency of specific sub-populations as defined by community membership, age, race, or other characteristics.Importantly, we define our measures such that the representations that platforms already compute in the process of mediating informational pushes and pulls can be used to quickly estimate different levels of agency-they are therefore not only operationalizable, but in a meaningful sense already operationalized.

Our framework highlights two separate channels by which GFMs and other advances in AI are impacting the nature of attentional agency online.First, platforms will ascertain progressively more granular representations of people's preferences and intentions.From the perspective of attentional agency, this is a double-edged sword-more accurate representations of a user's type not only enable platforms to deliver more targeted informational pulls, but also more targeted pushes.

Second, GFMs excel at inferring the significance of complex digital objects at the level of their atomic informational components ("tokens") and reconstituting them in novel ways [7,11,69].These models therefore enable platforms to extract and recombine information more flexibly.Whereas traditional search engines rank relevant web pages in their entirety, AI-powered search tools now recombine information from a variety of different pages into new informational objects on demand.This poses a fundamental challenge to the existing social, economic, and legal institutions that have emerged to generate and capture value on the internet.Most notably, the ability of GFMs to surgically extract information from its original delivery format-thus leaving embedded advertising, branding, and other promotional material behind-undermines many existing methods that platforms and content providers rely on to monetize their services.This is especially disruptive of the digital advertising model, which relies on the fact that people apprehend traditional informational bundles (e.g., web pages) as an integral whole.Stripping away context can also undermine established norms and expectations about how information should be interpreted, modified, and shared [33].

The rest of the paper is organized as follows.In the rest of Section 1, we provide a high-level summary of our framework, with additional motivation and an early coverage our limitations.In Section 2, we review related literature.Section 3 then presents our framework more formally and develops a mathematical analysis of our definitions.Section 4 highlights the broad applicability of our framework to five major categories of current internet platformssearch, content, social media, matching, and marketplaces.Section 5 presents some of the immediate policy implications of the concepts and formal definitions we propose and highlights open research questions.


## Related Work

Our work builds on ideas from a variety of literatures in computer science, economics, and behavioral science.Below, we summarize key prior work, focusing first on proposals to better align digital platforms.Next, we discuss how our framework builds on prior literature evaluating the efficacy and fairness of ranking systems.Finally, we summarize work from psychology and economics on the analysis of individual preferences, which form a key element of our approach.


## Aligning Digital Platforms

The challenge of aligning digital platforms has emerged as a key concern in modern computer science, prompting a variety of authors to propose methods for operationalizing potential social objectives, such as beneficence, equity, and fairness [37,54].The growing capabilities of GFMs have, moreover, introduced new forms of misalignment and new risks associated with failing to achieve alignment.A variety of potential solutions have been proposed in the literature, such as subjecting AI systems to a fiduciary requirement that would require them to both accurately learn people's preferences and uphold general principles, such as loyalty and care [5].Other related proposals include granting users new avenues of contestability [50] and implementing fair ranking in domains like education [4,30].

Conceptually, our article responds to a call originally made by Stray et al. [59], who argue that recommender systems represent a specific instance of this broader value alignment problem.They specifically advocate for the creation of operational measures of alignment-developing such a measure is the central aim of this paper.


## Evaluation of Ranking Systems

Our approach centers on a key feature of existing ranking and recommendation systems [32], namely the user-specific "relevance" scores that platforms use to match user attention and informational content.Existing approaches to evaluating recommender systems include measuring the precision and recall of a list of a fixed size (e.g., the "ten blue links" returned by a search engine), considering the mean reciprocal rank (applicable to social media feeds of arbitrary extent), or calculating variants of the discounted cumulative gain, which calculate a weighted average of relevance over ranks.

Our work intersects with prior research aimed at understanding how the design of recommender systems influences outcomes of interest, such as item diversity, bias, and user satisfaction [45,46].Given that the business value of ranking is typically proprietary and somewhat difficult to measure, estimates vary widely [34].Published work from Netflix suggests that the benefits of rankingbased personalization can be quite large in practice, at least in some domains [3,27].

Our measure of attentional agency advances the literature on ranking evaluation by directly mapping this construct to relevance scores using a calculation that can be easily performed using existing infrastructure and institutional practices.


## Fair Ranking

A large body of literature in machine learning has highlighted techniques to make ranking systems more "fair, " as interpreted in a variety of ways [18,21,31,40,67].

Patro et al. [47] critically review a large body of work focused on fairness for ranking, recommendation, and retrieval systems.They highlight the inherent challenge of defining fairness in the face of a "gap between high ranking placements and true provider utility, spillovers and compounding effects over time, induced strategic incentives, and the effect of statistical uncertainty" (pg.1929).Relatedly, Chen et al. [15] provide a synthesis of how "bias" has been studied in the context of recommendation systems, arguing that group unfairness is but one of seven types of bias.

Recent literature on fair ranking has underscored the difficulty of promoting fairness through a single definition, especially given that perception of fairness can vary widely from person to person [1].Techniques for incorporating fairness into ranking also tend to face a trade-off between fairness and utility (albeit techniques to ameliorate such trade-offs have also been developed [19]).One goal of our proposal is to draw the fairness community's attention to attention-that is, to highlight attentional agency as a potentially important factor in people's appraisals and experiences of fairness on digital platforms.


## Economic, Psychological, and Social Value of Attention

People's preferences over what they pay attention to arise from a wide variety of emotional [42], cognitive [63], social [8], decisional [58], and other considerations.Our framework distills these diverse motivations into a single utility function and asks: to what degree do platforms empower people to satisfy their own attentional priorities?By operationalizing attentional agency in terms of inferred utility values, our framework inherits both the advantages and limitations of revealed preference analysis.We adopt this approach because it enables us to capture a wide variety of motivations in a single measure that can be inferred from people's behavior using standard techniques (indeed, the very techniques that platforms already use to deliver value to users).

Revealed preference measures do, however, leave open the question of how tightly coupled people's attentional preferences are to their personal well-being or broader notions of social welfare [39].Indeed, there are many situations where the two seem to diverge quite sharply, such as video game addiction or "doom scrolling" highly engaging but emotionally deleterious content.Although our framework furnishes an operational measure of attentional agency, the question of how to evaluate its desirability in various circumstances is nuanced and requires careful consideration.Some of these concerns are only becoming more acute as AI search and other innovations enable platforms to deliver narrowly targeted persuasive messaging [20,52] and other novel forms of harmful content to users.


## Formal Framework 3.1 General Setup and Key Definitions

We study a canonical interaction between three parties: an agent, who wants to pay attention to informational objects they themselves value highly; an advocate, who also has preferences about what the agent attends to; and a platform that determines whether and how informational objects enter the agent's attention.

The agent has type drawn from a distribution ∈ Δ(Θ) where Θ is a finite type space.There is a universe of informational objects represented by an ordered set = ( 1 , 2 , . . .).An allocation is a bijective function : N → .

The agent has a type-dependent value for each informational object that is represented by a utility function : × Θ → R ≥0 .Owing to their limited attention, the agent discounts informational objects based on how they are allocated according to a weakly decreasing function : N → [0, 1], where 0 = 1 without loss of generality.The agent's value of allocation is

Logarithmic functions such as = log 2 ( + 1) -1 have been studied extensively in the literature on "discounted cumulative gain" and are particularly influential in the design of ranking algorithms [35].More generally, different specifications of enable the model to capture the reduced-form effects of limited attention in a variety of problem domains and platform interfaces.For example, discounted cumulative gain is natural in situations where the agent sequentially attends to informational objects (e.g., a web search or social media feed); however, a "cutoff" function where = 1 for ≤ and = 0 otherwise might be more natural for an interface that simultaneously presented a handful of recommendations (e.g., a homepage featuring personalized suggestions, or an AI-augmented search result that synthesizes information into a block of text, all of which is presumed to be read).

The platform supplies the agent with an allocation.Let Γ denote a partition of , which induces what we will call an allocation technology. 3Specifically, we assume that the platform can produce allocations that rearrange the order of the partition blocks of Γ, but not move objects within blocks.The interpretation is that digital information is naturally bundled together into objects (e.g., web pages, academic articles, social media posts), and greater degrees of technological sophistication are required to break apart, comprehend, extrapolate preferences to, and recombine more granular units of information within these objects.Let Φ(Γ) = { : N → | ∀ ∈ Γ, if , ∈ then -1 ( ) - -1 ( ) = - } denote the set of all possible allocations that can be constructed by permuting the blocks of Γ.

The platform has an imperfect understanding of and, therefore, the agent's preferences over allocations.Let denote the platform's model of the agent, which is a reduced-form representation of: (1) all information the platform possesses that pertains to the agent's type (e.g., as collected from past interactions, present context, and their query); and (2) whatever algorithms and other technology the platform uses to transform this information into a prediction about their type.Some systems enable users to explicitly reveal aspects of their stable or transient preferences (e.g., by selecting interests when first creating one's profile or entering a search query), whereas other systems implicitly learn a user's type from patterns of engagement (e.g., dwell time or likes in a feed-based interface).

The advocate also has preferences about what the agent sees, which we represent with a second utility function : × Θ → R ≥0 .Paralleling our notation for the agent, the advocate receives value

Note that we are assuming the advocate discounts utility using the same positional function as the agent.This is natural, for example, if the discount function is taken to represent the amount of attention the agent pays to each position and both parties value informational objects based on how likely they are to be attended to.We assume the platform chooses an allocation that maximizes a linear combination of agent and advocate utility subject to technological feasibility.

for a given weight ∈ [0, 1]. 45For simplicity, we will assume throughout that the primitives of the model are such that the solution to this problem exists and is unique (or can be arbitrarily chosen from a set of candidate solutions; this assumption does not materially affect the points we raise in our discussion).Next, define

which measure the amount of value that a particular choice of weight accords to the agent and advocate, respectively.Note that, from the platform's perspective, the total expected value generated at a particular value of is given by = + .We are now ready to define our central measures of attentional agency.

Definition 1. Pull is the amount of informational value a platform delivers the agent as a fraction of the total value it is technologically capable of delivering them.Formally, for a given , , , Γ, and , a platform's pull is

Definition 2. Push is the amount of informational value a platform delivers the advocate as a fraction of the total value it is technologically capable of delivering to them.Formally, for a given , , , Γ, and , a platform's push is

Push and Pull both range from 0 to 1 and index the amount of attentional value that is being delivered to agents and advocates, respectively.According to these definitions, it is always the case that increasing push (weakly) decreases pull.Note, however, that push and pull are not necessarily zero-sum.We analyze the conditions that determine the relative tradeoffs between push and pull fully in the next section.

Another important point is that our framework defines push and pull for a single agent, advocate, and platform interaction.Across many interactions, each platform produces a distribution of Pull and Push values which could be analyzed in terms of their 4 In general, the parameter is a choice variable under the control of the platforms.However, even if platforms can freely select in principle, the full range of choices may not be feasible in practice.Platforms operate within a broader "attention economy" and consequently must compete with other activities for user engagement (most notably, the services provided by competitors).Market forces therefore constrain the minimum and maximum amount of a platform can select without losing agent engagement or advocate buy-in entirely. 5An important exception occurs when platforms intentionally withhold attentional value to induce users to behave in a certain way-for example, when a dating app restricts how many profiles a user can view without paying for a premium version of the service.We note, however, that even in such cases, platforms typically incentivize behaviors by promising to move users onto or along the optimal push-pull frontier defined by the maximization (3).mean, variance, group-level differences, and other distributional properties.


## Analysis

In this section we highlight a few of the framework's most salient features.

3.2.1 Fixing technology, preference alignment determines the feasible push-pull frontier.First, note that is a weakly decreasing function of and is a weakly increasing function of . 6However, the rate at which these functions change depends upon the relative alignment of agent and advocate preferences.Taking the platform's allocation technology and agent model as given, we can consider the frontier of feasible push and pull values as a function of these underlying preferences.The platform effectively selects a point on this frontier by setting .

In a "zero-sum" situation where = -, the platform's objective simplifies to (2 -1) E[ (, )|], and they must choose either to deliver the agent's most-preferred allocation (if > 1

2 ) or their leastpreferred allocation (if < 1 2 ).In such an interaction, it is not only the case that pull and push are zero sum (Pull + Push = 1), but also that they change sharply around a critical value of .In other words, when agents and advocates push and pull in opposite directions, the platform will only accord agency to one of them.Conversely, if preferences are fully coincidental ( = ), then the platform can achieve maximal pull and push simultaneously (Pull = Push = 1) for any value of because the same allocation is optimal for both agents.

A less intuitive case of simultaneously maximal pull and push occurs when the agent is indifferent over certain aspects of their allocation that the advocate has strict preferences over and viceversa.When preferences are "orthogonal" in this way, the platform can also achieve maximal pull and push simultaneously (Pull = Push = 1) for any interior value of .From a policy perspective, situations of this variety are ideal targets for "nudges" [62], given that they can, in theory, achieve a planner's objectives without decreasing people's attentional agency.

In the more general case where preferences are partially aligned, the platform must choose how much weight they wish to place on agent versus advocate informational value, and, accordingly, how much agency each should be allocated.Note, however, that from the platform's perspective, the total informational value they create is a concave function of . 7This perhaps helps explain why interior values of Pull and Push are so commonly observed in practice-there is usually some value to the platform of choosing an interior and dividing attentional agency to some extent.


## 3.2.2

Model advances increase platform value, but also redistribute attentional agency.Advances in machine learning and artificial intelligence (e.g., new architectures, more parameters, or additional compute [36]) enter our framework in two ways.The first is through , which represents the depth and specificity with which the platform infers an agent's type before constructing an informational allocation. 8ritically, however, such changes enhance the platform's ability to provide value to both agent and advocate.In the former case, accurate inferences about an agent's type enable the platform to more successfully extrapolate their preferences to hypothetical allocations.Simultaneously, these inferences also enable the platform to facilitate more precise targeting by advocates.Indeed, recent work shows that frontier models are capable of greater persuasion precisely because they are better at "matching the language or content of a message to the psychological profile of its recipient" [44], increasing the stakes of strategic misalignment between agents and advocates.

The net effect of model improvements on attentional agency therefore depends on whether the innovations are more useful for predicting marginal differences in or across various allocations.Recall that the platform's objective when selecting an allocation is to maximize the linear combination

for some value of .If two types and ′ have conflicting preferences over allocations, then learning to distinguish them will make it more clear, in each case, what the marginal value of choosing one allocation over the other will be.This, in turn, will tend to shift emphasis in the overall optimization toward the agent's preferences.

A parallel argument, however, is also true for targeting.

Although the net effect on pull and push will depend, in each case, on which of these effects prevails, one implication always holds: the stakes of informational agency consistently grow as models become more sophisticated.


## 3.2.

3 AI enables attentional allocation to operate over more granular and varied information objects.Advances in artificial intelligence also enter our framework through the partition Γ, which defines the units over which a platform can deliver information.

Multiple features of modern generative foundational models [7] now enable AI systems to achieve unprecedented levels of informational granularity: (1) attentional transformers parse a wide variety of data sources into their constitutive tokens, meaning that systems can apprehend complex informational objects at the scale of individual symbols [66]; (2) expanded context windows enable sequence-based models to capture long-range data dependencies [49,60]; (3) multi-modality is in the process of extending the informational purview of AI systems to text, image, video, audio, and other formats [69]; and (4) generative capabilities enable systems to flexibly recombine these informational atoms into arbitrary new structures that do not necessarily resemble the sources they were initially drawn from.Although it has always been possible for platforms to disassemble informational objects in a literal sense, foundation models enable a categorically greater degree of sophistication when extrapolating an agent's preferences and intentions to these smaller units of information. 9ithin our framework, the cumulative effect of these innovations is to refine the platform's informational domain into a finer partition Γ ′ ⊂ Γ. 10 The additional degrees of freedom this opens up expand the space of possible allocations and, consequently, enable the platform to deliver more value overall.Formally, Φ(Γ) ⊂ Φ(Γ ′ ) so that ′ ≥ for any given .As in the case of model development, the ultimate impact of such a change on welfare and informational agency will depend on the relative alignment of preferences and other primitives of the model.

One clear take-away, however, is that highly capable multi-modal AI models which are fully aligned to agents (i.e., for which = 1 so that Pull = 1) increase their ability to extract informational value from a variety of sources without satisfying the implicit "attentional bargain" that supports much of the internet's current economic model-branding, sponsored content, advertising, and other features that businesses employ to monetize their content.As [68] points out in his history of the attention economy, the basic strategy to "draw attention with apparently free stuff and then resell it" has long been a part of the advertising business.Technological innovations intermittently disrupt the status quo implementation of this strategy, as exemplified by the famous "Betamax case" over whether Videocassette recordings of television shows (which enabled people to re-watch them without embedded advertisements) constituted copyright infringement. 11n contrast to other drivers of creative destruction, however, the very generality of general artificial intelligence means that a single technology stands to disrupt nearly every existing informational format simultaneously.The advent of human or super-human level artificial intelligence may represent a final frontier in these debates, effectively solving the attention problem.We return to the question of how these insights inform policy approaches to refactoring the landscape of attentional agency in Section 5.4, below.


## Attentional Agency on Platforms

Table 1 provides a high-level overview of how platform categories map on to our framework.Comparing various platforms side-byside highlights not only their common approach to attentional allocation, but also that the boundaries separating these categories are becoming increasingly blurred over time.Search engines that may have once depended purely on a user's entered query and a few contextual variables (e.g.location) now incorporate user history [43].Social media platforms often emphasize a feed (with minimal interaction options beyond "show me more content") but may also support search.Online marketplaces sell a mixture of physical and digital goods, but now often offer recommendation features.

In what follows, we briefly review how our framework maps onto existing platform categories, then briefly discuss how generative foundation models are further eroding the distinctions that have traditionally separated them [17].

Web Search Engine: Search engines primarily rank web pages based on user queries and intrinsic, site-specific features [51,65].Agents engaged in web search generally want to specify their query as briefly as possible, meaning that search engines are most efficient when they can anticipate people's needs and desires [43,51].This tends to incentivize platforms to build up a deep understanding of preferences and intention through repeated interaction with each individual user.One user's interactions with a platform are also used to tailor results delivered to similar users through techniques such as collaborative filtering.

Queries enable users to locate relevant content efficiently, but they also equip platforms with highly specific data about user characteristics and momentary intentions.Consequently, many leading search engines harness this information by allowing web pages to augment their ranking preferentially among users with specific characteristics.

Content Library: Content libraries provide access to large collections of media and generally enable users to both search for items they already know and browse recommendations to discover new items.Media preferences tend to correlate significantly across and within individuals, meaning that both general popularity and personalization can significantly enhance the value of recommendations [26].

In the context of content libraries, pull could be decreased because of platform promotion (e.g., a video streaming service promoting a show they funded), but also through limitations of collaborative filtering.

Social Media: Social media platforms present users with a curated stream of multimedia objects centered around the activities of other users.Many social media feeds orient the user's attention around a single activity: requesting more content.Social media platforms tend to primarily infer an agent's interests and intentions implicitly (e.g., from dwell time), rather than explicitly (e.g, entering a query).Social media is also distinguished by the fact that many users want to both "see and be seen," acting as both agents and advocates.

Matching: Matching platforms help interested parties find one another.Some such platforms, such as dating apps, are "two-sided, " with users acting as both agents and advocates.Many matching platforms allow advocates (premium users) to gain visibility by influencing the attention of other users.

Marketplace : Online marketplaces help people search for goods and services.User preferences on marketplaces are driven by a combination of immediate shopping needs, long-term consumption habits, and sensitivity to factors like price, quality, and seller reputation.Attention can have a sizable impact on consumer behavior [25], which makes featured listing, personalized recommendations, promotional offers, and targeted advertising especially valuable to advocates.

AI Search: Table 2 summarizes how AI search tools (powered by generative foundation models) compare to the five existing platform categories just reviewed.As discussed in Section 3, AI search tools operate at the level of individual tokens [7], which enables them to flexibly tailor content to the user's specific preferences ( ), as inferred from their interaction history and context.The capacity of modern AI systems to draw meaningful connections between distal information sources and modalities (see Section 3.2.3)strengthens complementarities between various data sources: scientific papers, law articles, encyclopedia entries, code, and other sources of knowledge that were previously mostly referenced independently can now be interrelated in new and more valuable ways.


## Discussion


## Advertising in the Technology Industry

A common refrain in early commentary on the targeted digital advertising model was "if you are not paying for the product, you are the product." Subsequent proposals, such as data as labor [48] and data dignity [41], pursue a related critique: that under the current paradigm, users of free internet platforms are also effectively workers producing data.Advocates of the advertising model, on the other hand, argue that it promotes equity and access because free products extend the benefits of technological innovation to those at the bottom of the socio-economic ladder.Our framework shows how key claims frequently made in these debates can be made more concrete by quantifying the amount of attentional agency these platforms accord to various groups of individuals.If someone is not paying for a costly service, their activity is being subsidized in some way, often by advocates.The degree to which this reduces their attentional agency, however, depends on the relative alignment of preferences, technological context, and other factors.Measures of push and pull show how the combined influence of these factors can be operationalized using relatively lightweight calculations.

This creates an open challenge for balancing the welfare implications of attentional agency and the consumer surplus afforded by ad-funded internet platforms [10].Below, we outline ideas aimed at making tangible progress on this challenge, especially in light of recent AI progress.


## Attentional Agency and Alignment

Our measures of attentional agency also complement ongoing research into AI alignment, especially work that applies concepts such as pluralism in human values [57] and social choice [16].Platforms create value by extending a user's attention to unseen informational objects, which necessarily entails the user entrusting the platform with a certain degree of discretion.Thus, pull can measure alignment to an individual's intentions.Push, on the other hand, measures alignment to the objectives of others.

Push and pull further clarify interventions that aim to block specific concepts or pieces of information (e.g., instructions to build a weapon), such as preference ranking optimization [56] and chained "safety classifiers" [38].In our framework, such measures can be understood as seeking to fulfill the goals of an advocate-which might be a public body acting in the public interest.This insight is useful because modeling such situations as conflicts between advocates allows us to bring economic reasoning and mechanism design to bear on the problem.


## Attentional Agency and Generative Foundation Models

Our framework reveals that, from the perspective of attentional agency, the key innovation of generative foundation models lies in their ability to parse information from a wide range of sources at an exceptionally granular level-that of the individual token.As we argued in Section 3.2.3,this enables AI-powered search tools to extract information from websites while leaving behind embedded advertising and other elements that support monetization.This raises a critical question: will some form of the advertising model endure, or will it give way to a new paradigm in which agents pay directly (e.g., via subscriptions or API credits) for access to information?

The potential for generative foundation models to circumvent existing monetization pathways has raised concerns about their implications for journalism and related industries [29].Our framework highlights, however, that this problem arises precisely because these technologies enable agents to maximize pull.However, there exists a hopeful future in which direct access to highly personalized and carefully ranked chunks of information is worth paying for and ultimately leads to more funding for information creation and curation.

In short, if we view advances in AI as reducing the granularity of informational objects that can be processed on digital platforms, the lens of attentional agency gives us a clear vocabulary (and with regulatory support, concrete data-see below for how lightweight regulatory interventions could allow for the sharing and use of push and pull measurements) to reason about when the reduction in granularity will work to advance human values, and when it will create new challenges (e.g., violate previous arrangements around incentives).


## Policy Strategies

There have been many proposals to promote greater transparency and accountability online.Some of the most prominent examples include the transparency provisions in the EU's Digital Services Act (DSA), EU's General Data Protection Regulation (GDPR), and proposed EU Artificial Intelligence Act [23, 24] 12 .

Below, we highlight three policy strategies that naturally complement our framework.Notably, each of these simple proposals can be implemented with relatively little effort or tailoring by platforms.

(1) Transparency into attentional agency: Measure and provide information on the distribution of Pull and Push, both in aggregate and by subgroup.Greater transparency would help users identify instances where they are experiencing reduced levels of attentional agency and make informed choices between platforms, potentially increasing both accountability and competition.(2) Expanded consumer choice: A variety of platforms sell push in order to generate revenue.For those that do, users could be given the option to pay for a "push-free" experience (which would generalize the "ad-free" tier offered by some services).This would enable users who place a greater premium on pull to maximize it for a price, increasing overall economic efficiency.(3) Provably neutral algorithms: Platforms offer a version of their service independent of advocate-driven factors, but that may not maximize pull.An example would be the inclusion of an option to sort one's social media feed chronologically and without promotion.

These strategies all target the concrete attentional choices that platforms make on behalf of users and the structural incentives that shape those choices.These ideas are not a substitute for existing algorithmic audits, privacy protections, content moderation standards, or other key planks of the online safety agenda.Attentional agency attacks the problem of manipulative platform design from a neglected angle, one grounded in a numerical accounting of how platform incentives distort the information that users encounter.

While paid push-free options, neutral algorithm defaults, or push/pull disclosures may seem like relatively modest interventions, they reflect a fundamentally different theory of platforms than conventional transparency approaches.Rather than focusing on the black-box mechanics of ranking and recommendation systems, they target the concrete attentional choices that platforms make on behalf of users and the structural incentives that shape those choices.Importantly, measures to increase transparency at this level would support broader societal conversations about how attentional agency is distributed without requiring detailed technical knowledge of how algorithms produce specific rankings.

As we pointed out in our discussion of the "Economic, Psychological, and Social Value of Attention" (Section 2.4), people's revealed attentional preferences are not always tightly coupled to their underlying welfare.Policies that uncritically seek to maximize pull may therefore not only fail to improve, but in fact actively undermine, a user's overall health and happiness (e.g., if they are struggling with attentional self-control problems).One promising solution would be to develop and apply our framework to algorithms that infer people's reflective (rather than impulsive) preferences (see [39] for a general discussion).


## The Political Economy of Social Media and AI

Recent policy debates have highlighted a variety of issues that arise when large organizations have the capacity to determine what people pay attention to at scale.As one example, concerns about the political independence of TikTok's content and algorithmic recommendations spurred the United States to pass legislation banning any "website, desktop application, mobile application, or augmented or immersive technology application" that is "controlled by a foreign adversary" [64].

Our framework helps inform these debates by providing a quantitative tool that can be used to evaluate the impact that competing incentives of various stakeholders have on user agency.As just discussed in Section 5.3, generative foundation models and other innovations are quickly expanding the capacities of platforms, raising the stakes of developing a more participatory role for users in technological development [2].

These developments reflect a growing desire for better evidencebased approaches to platform accountability and governance.By demanding transparency into the attentional agency of users, policymakers and the public can work towards aligning platform incentives with democratic values and the genuine preferences of users.

Measures of attentional agency also complement recent work on the interplay of algorithmic platforms and phenomena such as ideological segregation [28], echo chambers and "rabbit holes" [9], and interaction with misinformation more generally [22].This body of work provides a complementary lens for understanding the health of an algorithmic platform or feed.Given that push and pull measurements can be assessed in a faceted manner, it could be useful to consider push and pull along axes such as political valence or through the lens of "trust."


## Conclusion

The framework we propose provides a lens for reasoning about how current platforms distribute attention.Our methods also provide new insight into ways that future platforms, especially ones powered by highly capable forms of artificial intelligence, might come closer to achieving the original visions of the thinkers who inspired the internet.The framework we propose is intended to be readily applicable to policy discussions-indeed, the operational definitions we propose are based on techniques and computations already in use by platform operators.

How prominent digital platform categories map onto our framework.

Applying the push/pull framework to AI search, chat, and assistant tools, as powered by modern generative foundation models.
