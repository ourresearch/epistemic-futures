---
title: "WikiGap: Promoting Epistemic Equity by Surfacing Knowledge Gaps Between English Wikipedia and other Language Editions"
person: "nick-vincent"
section: "by"
type: "journal-article"
year: 2025
date: "2025-05-30"
venue: "WikiWorkshop 2026, 2026 · Forthcoming"
authors: "Zining Wang, Yuxuan Zhang, Dongwook Yoon, Nicholas Vincent, Farhan Samir, Vered Shwartz"
source_url: "https://arxiv.org/abs/2505.24195"
retrieved: "2026-08-13"
content: "full-text"
notes: "OpenAlex W4416255835; CV ref [W19]; Full text from the arXiv HTML rendering of the preprint (https://arxiv.org/html/2505.24195v3)."
---

# WikiGap: Promoting Epistemic Equity by Surfacing Knowledge Gaps Between English Wikipedia and other Language Editions

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

- 2 Background and Related Work

- 2.1 English Wikipedia is Considered the Default, yet Information Gaps with Other Editions Persist

- English Wikipedia is considered the “default” edition.

- Knowledge gaps in English Wikipedia.

- Knowledge is often culturally-positioned.

- No language edition is complete.

- 2.2 Prior Work Targeting Cross-Lingual Knowledge Dissemination

- Towards a Monolithic Language Edition.

- Wikipedia’s Interlanguage Links (ILL)

- Prior Multilingual Interface Designs.

- 3 WikiGap System

- 3.1 Designing WikiGap

- 3.1.1 Design Requirements Informed by User Needs and Theory

- Exploratory Interviews on Multilingual Wikipedia Use

- R1: Surface cross-lingual content without disrupting reading flow.

- R2: Ensure clear language attribution and
traceability of multilingual facts to promote creditability.

- R3: Support both passive discovery and active exploration of cross-lingual knowledge gaps (customizable exploration).

- 3.1.2 Core Design Elements

- D1: In-text Gap Markers.

- D2: Cross-Lingual Fact Panel

- D3: Fact Provenance Card

- D4: Source Language Filter

- D5: Cross-lingual Fact Search.

- 3.2 The InfoGap Pipeline

- 3.3 Extending and Integrating InfoGap for WikiGap

- 3.3.1 Enabling Chinese language support.

- 3.3.2 Language attribution and fact selection

- 3.3.3 Translations and traceability.

- 3.3.4 In-text highlights.

- 3.4 System Implementation

- 4 Evaluation Methods

- 4.1 Participants

- 4.2 Tasks

- Quiz Construction.

- Performance Metrics.

- 4.3 Materials and Topic Assignment

- Selected topics

- Topic assignment

- 4.4 Procedure

- 5 Findings

- ①Users Strongly Preferred WikiGap over the Default ILL (D1, D2, D3)

- ②WikiGap Enhanced Fact-Finding Performance and Cross-Cultural Learning via Passive Discovery and Active Exploration (D4, D5)

- ③WikiGap Raises Awareness of Multilingual Gaps and Motivates Exploration

- ④Respondents’ Views on LLMs and Wikipedia: Perceived Trust and Tensions

- ⑤WikiGap Supports Editors in Validating and Integrating Multilingual Content

- 6 Discussion

- 6.1 Editor-Readership Asymmetry in English Wikipedia

- 6.2 English-as-superset Hypothesis Lives On

- 6.3 Objectivity in Knowledge Representation

- 6.4 Limitations and Future Work

- Language Coverage.

- WikiGap content selection.

- Other barriers in facilitating epistemic justice in Wikipedia.

- Capacity for misinformation contagion.

- System Architecture.

- 7 Conclusion

- Acknowledgements

- References

- A Sample Quiz Questions

- B Interview and Questionnaire Protocol

- C Average Completion Time and Accuracy across Different Topics

License: arXiv.org perpetual non-exclusive license

arXiv:2505.24195v3 [cs.HC] 23 Sep 2025

## WikiGap: Promoting Epistemic Equity by Surfacing Knowledge Gaps Between English Wikipedia and other Language Editions

Zining Wang

Affiliation: University of British Columbia
, Canada

Affiliation: Vector Institute for AI
, Canada

email: zining.wang@ubc.ca

,
Yuxuan Zhang

Affiliation: University of British Columbia
, Canada

,
Dongwook Yoon

Affiliation: University of British Columbia
, Canada

,
Nicholas Vincent

Affiliation: Simon Fraser University
, Canada

,
Farhan Samir

Affiliation: University of British Columbia
, Canada

Affiliation: Vector Institute for AI
, Canada

and
Vered Shwartz

Affiliation: University of British Columbia
, Canada

Affiliation: Vector Institute for AI
, Canada

Figure 1. The WikiGap interface embeds cross-lingual facts into English Wikipedia via five key design elements (D1–D5), supporting in-place access, traceability, and multilingual engagement.

####### Abstract.

With more than 11 times as many pageviews as the next largest edition, English Wikipedia dominates global knowledge access relative to other language editions. Readers are prone to assuming English Wikipedia as a superset of all language editions, leading many to prefer it even when their primary language is not English. Other language editions, however, comprise complementary facts rooted in their respective cultures and media environments, which are marginalized in English Wikipedia. While Wikipedia’s user interface enables switching between language editions through its Interlanguage Link (ILL) system, it does not reveal to readers that other language editions contain valuable, complementary information. We present WikiGap, a system that surfaces complementary facts sourced from other Wikipedias within the English Wikipedia interface. Specifically, by combining a recent multilingual information-gap discovery method (Samir et al. 2024) with a user-centered design, WikiGap enables access to complementary information from French, Russian, and Chinese Wikipedia. In a mixed-methods study (n=21), WikiGap significantly improved fact-finding accuracy, reduced task time, and received a 32-point higher usability score relative to Wikipedia’s current ILL-based navigation system. Participants reported increased awareness of the availability of complementary information in non-English editions and reconsidered the completeness of English Wikipedia. WikiGap thus paves the way for improved epistemic equity across language editions.

### 1. Introduction

Wikipedia boasts more than 300 language editions, inviting contributions from all over the world. The investment in creating multiple language editions reflects Wikipedia’s principles of democratizing both access to and contribution of information. By design, Wikipedia editions are not translations of one another, but rather reflect the specific knowledge that is relevant for their respective readers, often based on cultural experience and local media coverage (Avieson and Mazumdar 2025; Kumar 2021). As a result, readers of different Wikipedia editions are not exposed to the same information.

English Wikipedia in particular is the largest edition, which is read and edited by more people than any other language edition.
This is perhaps unsurprising given that English is the major global lingua franca.
However, given the complementary nature of Wikipedia editions,
even readers of English Wikipedia don’t have access to content that may yet be relevant from other language editions.

One might argue that since English is a global language, editors from other linguistic regions can add culturally-relevant information into English Wikipedia. Indeed, prospective editors, knowing that English Wikipedia attracts a higher readership than any other edition, often opt to try to contribute to English Wikipedia, even when they possess a high degree of literacy in other languages (Hale 2014). In 2024, English Wikipedia received nearly half of the 109M contributed edits (Wikipedia contributors 2025).

In practice, however, the overwhelming dominance of English poses a significant challenge to egalitarian knowledge curation. It is not uncommon for such editors to contribute culture- or region-specific knowledge to English Wikipedia
to encounter hegemonic resistance. While Wikipedia is in principle open to contributions from any person with literacy skills and an internet connection, it was reported in (Oberhaus 2017) that an overwhelming majority of edits are contributed by a small portion of the editor base (Oberhaus 2017). As of (Wikimedia Foundation 2024b), for English Wikipedia, these editors were overwhelmingly male and white (Wikimedia Foundation 2024b). This has resulted in contributions being rejected, even when the topic is geographically positioned in a non-Anglophone country; see, for example, a case study on a lengthy editor dispute resulting in the discarding of Indian editors’ cultural knowledge of the Ganga river in India (Kumar 2017).

Yet, at the same time, English Wikipedia is by far the most widely read and authoritative source among the 300+300+ language editions. In a 2011 report, 93%93\% of all editors surveyed attested to reading English Wikipedia, even though it was a primary language for only 52%52\% of them (Kumar 2021; Wikimedia Foundation 2011). We are thus presented with a remarkable asymmetry – English Wikipedia marginalizes potential contributions from non-Anglophone sources, yet inadvertently monopolizes attention from information-seeking readers away from language editions that contain these marginalized perspectives (Avieson and Mazumdar 2025, e.g.,). This epistemic assumption of the completeness of English Wikipedia, which gives rise to this asymmetrically large readership, was previously aptly named the English-as-superset hypothesis (Hecht 2013).

A promising approach for mitigating the hegemonic dominance of English Wikipedia is to increase engagement with information in other language editions. While these are smaller, they are by no means lacking in thoughtfully curated and often complementary content. As Hecht and Gergle 2010 showed, the English language edition was lacking coverage entirely for a considerable number of topics, with English Wikipedia lacking 60%60\% of the articles present in the Ukrainian edition, for instance. More recently, Samir et al. 2024 showed large information gaps in English Wikipedia compared to Russian and French Wikipedia across more than 2.5​k2.5k Wikipedia biography pages, finding that English Wikipedia can lack even 50−70%50-70\% of content in other language editions when looking at regionally prominent public figures. Prior studies have sought to capitalize on these complementary multilingual texts, either through consolidation into a monolithic knowledge base or through interface redesigns. Both of these approaches, which we lay out in greater detail in Section 2, face fundamental obstacles in smoothly integrating multilingual content into readers’ engagement with English Wikipedia.

In this work, we present WikiGap, a socio-technical system that surfaces sentence-level factual differences across language editions of Wikipedia. The system combines a computational backend (InfoGap) that identifies multilingual content gaps (Samir et al. 2024) with a browser-based interface that presents these differences through in-page highlights and a sidebar display (Figure 1). We address two research questions: First, how can multilingual content be seamlessly integrated into the English Wikipedia reading experience? Second, how might readers benefit from engaging with this cross-lingual content? To explore these questions, we developed a web extension that unobtrusively augments English Wikipedia articles with supporting facts drawn from the respective articles in the French, Russian, and Chinese editions.

We evaluated WikiGap through a mixed-methods user study using a fact-finding task focused on culturally rich food articles – a domain where cross-lingual disparities are particularly salient (Laufer et al. 2015). Our results show that participants strongly preferred WikiGap over Wikipedia’s default interlanguage links system (ILL), with System Usability Scale (SUS) scores 32 points higher on average. In terms of performance, participants were significantly more accurate and faster at answering factual questions when using WikiGap, suggesting that surfacing multilingual information directly within the English interface not only improves user satisfaction but also enhances learning efficiency.

Through a Post-Study interview, we find that participants, prior to using WikiGap, were largely unaware of content gaps in English Wikipedia, demonstrating that the problematic English-as-superset epistemic assumption persists more than a decade after it was identified in seminal studies by Hecht 2013.
Participants were overwhelmingly appreciative of WikiGap’s capacity to surface these substantive information gaps during the reading of English Wikipedia pages.
Moreover, a few participants with prior editing experience described how the system could support their editorial workflows by enabling source verification and facilitating the integration of multilingual content. These findings underscore WikiGap’s broader value as a bridge between communities of editors and readers across languages. At the same time, a minority of responses reflected concerns about the emergence of large language models (LLMs) in drawing readers away from information-seeking directly on Wikipedia, raising important questions about the increasingly marginalized role of provenance in accessing information, which should be investigated in future research.
Overall, participants largely expressed openness and enthusiasm about interacting with multilingual content in English Wikipedia. We hope that this work paves the way for further growth of language editions that have been marginalized relative to English since Wikipedia’s inception in 2001 (Kumar 2021).11
1

We are sharing the code and data: https://github.com/aw814/WikiGap

Our contributions are as follows:

- •

A novel system design that leverages a computational pipeline for detecting fact-level information gaps across languages, integrating facts sourced from other language editions into English Wikipedia articles.

- •

An empirical evaluation using a mixed-methods study (N=21) showing that WikiGap significantly improves fact-finding accuracy and completion time, achieves higher usability than Wikipedia’s default ILL system, and fosters greater engagement with multilingual content, thereby challenging the perceived epistemic supremacy of English Wikipedia.

### 2. Background and Related Work

Wikipedia is a peer production system (Benkler et al. 2015), where a large number of collaborators come together to produce a shared outcome. There are important norms in this collaborative practice that are referenced heavily in deliberating content contributions, although the explication and invocation of these norms can vary widely across language editions (Hwang and Shaw 2022; Bipat et al. 2021). Community-developed tools such as vandalism patrol and bot-assisted help sustain these collaborative norms (Geiger and Ribes 2010). Wikipedia has also introduced formal mechanisms like page protection policies, which increase friction in contributing edits to popular or controversial pages (Ajmani et al. 2023b).
But the overarching ethos is that there should be no hard-set rules, and Wikipedia should remain largely self-organizing. These tensions between coordination, conflict, and self-organization mirror challenges seen across peer-production communities beyond Wikipedia, in thousands of other online wiki communities, for instance Wookiepedia and the Psychology Wiki (Kittur and Kraut 2010).
Large-scale collaborative peer production systems like Wikipedia are intended to democratize access to information, making it “easily available to people who would have otherwise had to seek it out in piecemeal and often haphazard fashion, if they could access it at all” (Justice and Golumbia 2024, pp. 273). It is not simply about access either; Wikipedia is largely associated with an air of democratizing the production of knowledge, a telos of rebelling against centralized authority and bureaucracy. This more laissez-faire form of collaborative content production is underpinned by the idea that a distributed form of knowledge curation could result in egalitarian outcomes in the access to and production of knowledge.

But this vision has been argued to be highly idealistic, as the capacity to create archival encyclopedia content has long been recognized as sociopolitically contingent (Foucault 2013; Said 1977). For example, the composition of the English Wikipedia editor base (white, male) has predictably led to the marginalization of women on Wikipedia (Hargittai and Shaw 2015; Wagner et al. 2016), as well as scholars from racial minority backgrounds (Adams et al. 2019). The demographic skews in the editor base are not merely incidental, but they can systematically shape whose knowledge is valued in the encyclopedia, privileging some forms of knowledge while marginalizing others. This can lead to reproducing epistemic injustice (Ajmani et al. 2024).

When it comes to multilingualism in Wikipedia, Wikipedia’s pillar for verifiable information, a component of the Neutral Point of View policy, has introduced barriers for creating content in other language editions. English is widely recognized as the preeminent vehicle for conveying scholarship, making it challenging to find primary sources for other language editions unless editors are fluent in English (Sen et al. 2015). While there are multilingual editors who contribute to multiple language editions, who serve as a bridge connecting different language editions (Hickman et al. 2021), they are a smaller proportion of editors on Wikipedia (Hale 2014).

In this section, we highlight the perceived hegemonic status of the English language edition, while maintaining that it has information gaps that illustrate that it should not serve as the authoritative language edition (Sec. 2.1). We then discuss previous solutions, including a unified language edition, Wikipedia’s Interlanguage Link navigation panel, and other interfaces proposed for interacting with content in different language editions (Sec. 2.2). We argue that these prior works have yet to achieve an important goal of increasing readers’ interaction with content from other language editions. In achieving this goal, we challenge the perceived completeness of the English language edition—what Hecht 2013 has previously called the English-as-superset hypothesis—an important step towards greater democratization of knowledge production. In Sec. 3, we introduce our system, WikiGap, that augments the experience of reading English Wikipedia documents by showcasing information gaps relative to other language editions.

#### 2.1. English Wikipedia is Considered the Default, yet Information Gaps with Other Editions Persist

In 2008, Wikimedia Foundation cofounder Jimmy Wales wrote that Wikipedia was for creating a free encyclopedia and making it available to “every single person on the planet in their own language” (Cohen 2008). Unsurprisingly, considering the status of English as the global lingua franca, the English edition of Wikipedia has significantly outpaced other language editions in terms of size and coverage.

###### English Wikipedia is considered the “default” edition.

It is often taken for granted that English Wikipedia serves as a superset of the knowledge encoded in other language editions. Hecht 2013 identified that this “English-as-superset” viewpoint. Although not explicitly stated as such, this viewpoint is nonetheless remarkably prevalent, even among researchers who rely on multilingual Wikipedia to train text-generation and text-embedding models.

###### Knowledge gaps in English Wikipedia.

Hecht and Gergle 2010’s ((Hecht and Gergle 2010)) formative study, however, found English Wikipedia was far more of a complement rather than a superset. They found considerable gaps in topic coverage in English Wikipedia relative to other language editions. Samir et al. 2024 ((Samir et al. 2024)) further showed that even when a topic is covered across languages, English Wikipedia often lacks a large body of facts present in other editions, studying French and Russian Wikipedia specifically.

###### Knowledge is often culturally-positioned.

One might interpret Wales’ statement to mean that there exists a set of facts constituting a language-agnostic encyclopedia, that can then be cryptographically encoded into various languages. More generally,
this view of language as an object that can exist outside of socio-geographic context is highly prevalent in philosophies of language, where language is metaphorized as a cryptographic encoding and the language-processing brain as (often literally) a computer (Golumbia 2009, Chapter 4).

While some facts are culturally invariant, such as physical laws, some of Wikipedia’s most-read articles pertain to socio-geographically positioned histories of peoples, places, recipes, and so on (Wikimedia Foundation 2024a). Generally speaking, all of Wikipedia’s language editions are necessarily socio-geographically positioned (Johnson and Lescak 2022)
and exhibit a “self-focus bias” (Hecht and Gergle 2009), the tendency of editors to contribute more to articles relevant to their region, including articles on people (Samir et al. 2024; Callahan and Herring 2011), places (Oeberst and Ridderbecks 2024), and cuisines (Laufer et al. 2015).

###### No language edition is complete.

For those culturally-positioned topics, the presupposition of a universal language-agnostic knowledge base has contributed to the marginalization of other language editions. English Wikipedia is treated as the default, standard, or “invisible center” (Benjamin 2023) through which other language editions are compared against. For example, Hickman et al. 2021 documents that bilingual Indian and Pakistani editors refer to English Wikipedia to determine the contributions to make to their local language editions, perceiving English Wikipedia to be the objective standard.22
2

This isn’t exclusive to South Asian editors; as we show in Section 5, readers and editors alike remain largely unaware of cross-linguistic heterogeneity in Wikipedia.
In reality, neither the English version nor the local language edition for a topic is a complete article; a considerable proportion of unique facts can still be identified in non-local language editions (Samir et al. 2024). There is thus an incentive to look at multiple language editions, even when a topic has a strong regional association with one language edition.

#### 2.2. Prior Work Targeting Cross-Lingual Knowledge Dissemination

Researchers have taken notice of the complementary nature of Wikipedia’s language editions, proposing various technical solutions to exposing users to information from different editions.

###### Towards a Monolithic Language Edition.

Differences between language editions that stem from socio-geographical interests have often been perceived as rather cross-linguistic disparities. Underpinning the framing of disparities is that there is a problem to be solved. Consider, for example, this quote from Duh et al. 2013, who propose to automatically construct a unified version of an article across languages:

Information disparity is a major challenge with multi-lingual document collections. When documents are dynamically updated in a distributed fashion, information content among different language editions may gradually diverge.

This problem formulation is not uncommon, even serving as the locus of a prominent shared task (Negri et al. 2013). Adar et al. 2009 take a similar approach and propose to unify information boxes across language editions, pursuing consolidation in Wikipedia infoboxes. Conversely, aligned with prior work in understanding cross-linguistic heterogeneity across Wikipedia’s language editions (Bao et al. 2012; Sen et al. 2015, e.g.,), we take the view that cultural positionality is one to be highlighted rather than a problem that needs to be solved via consolidation into a monolithic knowledge base, where different languages serve as mere cryptographic encodings over raw facts.

###### Wikipedia’s Interlanguage Links (ILL)

Currently, Wikipedia supports accessing different language editions of a topic through Interlanguage Links, available via a dropdown box on each article. While these links ostensibly provide readers with access to complementary information across editions, the interface gives little indication that articles may differ substantially in content. Instead, the hyperlinks imply only a change in linguistic encoding, similar to using Google Translate, and do not signal the significant differences in composition and curation across editions. Consistent with this design, our user studies (Section 5) show that many readers assume language editions share a single underlying knowledge base.

As Samir et al. 2024 identified through their InfoGap method (Sec. 3.2), English Wikipedia lacks facts from other language editions that may have a broader appeal. For example, Apple CEO Tim Cook’s association with the Russia-Ukraine war is only mentioned on Russian Wikipedia, but is conceivably noteworthy to the wider array of readers that engage with English Wikipedia.

###### Prior Multilingual Interface Designs.

There have been attempts to go beyond both a unified language edition as well as Wikipedia’s ILL and develop interfaces to surface information from various language editions. One such system is Manypedia (Massa and Scrinzi 2012), an interface providing a side-by-side view of an article from two language editions, translated into a common language using Google Translate. This interface, however, does not directly surface information gaps and inconsistencies between the two language editions. In contrast, the Chrome extension WikiCompare (Roy et al. 2022) identifies differences in topic coverage. In the typical scenario, a user reading an article in their native language (e.g., Hindi) will see highlighted phrases representing topics for which articles exist in another language edition (e.g., English) but not in the current language edition. Clicking on one of these links directs the user to the section of the English edition that discusses the topic. In our work, we go beyond identifying differences in topic coverage to pinpointing specific facts covered in one language but not another.

The most pathbreaking of these interfaces is Omnipedia (Bao et al. 2012), which enables readers to get an overarching sense of how different language editions’ editor communities conceptualize a concept. While they similarly rely on anchor links as WikiCompare does, their design enables visualizing several different language editions simultaneously and succinctly. This innovative redesign, however, would require users to completely change how they interact with Wikipedia. The Omnipedia workflow requires that readers start by entering a concept in their search bar. This starting point, however, contrasts with how most readers engage with Wikipedia, through information brokering search engines (Vincent and Hecht 2021). As such, this innovative redesign is unlikely to meet widespread adoption.

In the next section, we describe WikiGap, a system powered by InfoGap (Samir et al. 2024), that supplements English Wikipedia pages with relevant facts from other language editions, providing the reader with more information and, in doing so, raising awareness of unique content in other language editions. As such, it dispels the English-as-superset conceptual model (Hecht 2013) that, as our user studies demonstrate, remains remarkably prevalent. Unlike all of the aforementioned interfaces, our approach is not restricted to surfacing only differences in hyperlinks between language editions.

### 3. WikiGap System

The goal of WikiGap is to challenge the epistemic superiority of English Wikipedia, by increasing interaction with complementary content present in smaller language editions. Guided by this goal, we combine a computational pipeline that identifies sentence-level gaps across languages with a user interface designed to surface this content through in-situ annotations and structured fact cards. We begin with outlining the design requirements informed by user needs and foundational theories that shaped the WikiGap interface (§3.1). We then step behind the scenes to introduce InfoGap (Samir et al. 2024), which we use to detect language-exclusive facts lacking in English Wikipedia (§3.2). Furthermore, we describe how we extended and adapted InfoGap to detect and deliver language-exclusive facts, including how we filter, translate, and bind them to UI components at runtime (§3.3). We conclude this section by outlining the system implementation details (§3.4).

#### 3.1. Designing WikiGap

We describe the exploratory interview we conducted to understand users’ needs, from which we developed the design requirements (§3.1.1). Then, we describe the core UI elements that we derived from the requirements (§3.1.2).

##### 3.1.1. Design Requirements Informed by User Needs and Theory

When it come to start designing the interface, we combined our findings from the exploratory interview with established theories that explain how people seek, process, and comprehend information while reading to define a set of design requirements for WikiGap. These consist of the overarching goal, helping readers seamlessly access cross-lingual content while maintaining the familiar experience of browsing English Wikipedia. The findings from the exploratory interview, requirements, and design elements are summarized in Figure 2 and detailed below.

###### Exploratory Interviews on Multilingual Wikipedia Use

We conducted an exploratory interview with four Computer Science graduate students (2 women, 2 men), all regular Wikipedia users; three spoke an additional language (Korean, Russian, or Hindi). Each 30-minute session followed an unstructured, conversational format guided by open-ended questions about their multilingual Wikipedia usage, perceptions of the Wikipedia ILL system, and ideas for improving cross-lingual content presentation. Participants reviewed an English Wikipedia article on mooncake–a topic unfamiliar to them–and reflected on how multilingual facts could be surfaced in this context. They proposed interface features to better support multilingual reading habits. We took notes during the sessions and synthesized them using thematic coding to derive the following design requirements for WikiGap.

Figure 2. How the findings from our preliminary interviews (F1-F4) informed WikiGap’s design requirements (R1-R3) and core design elements (D1-D5).

###### R1: Surface cross-lingual content without disrupting reading flow.

Participants expressed a strong desire to access multilingual information without breaking their reading experience. They reported rarely using Wikipedia’s ILLs (F1), noting the disorienting nature of full-page switches: “Even if I click the other language, I don’t know where to look for the thing I care about. It’s like starting over.” Such page jumps impose high navigation costs (Pirolli and Card 1999), requiring users to reorient to a new layout and language, which discourages exploration.

Instead, users preferred lightweight, non-intrusive cues – similar to annotations in Grammarly or Google Docs – that subtly signal the presence of additional information (F2). This aligns with Anchored Annotation Theory (Marshall 1997), which finds that tying annotations to specific text locations improves comprehension and recall. Our design anchors cross-lingual facts directly to the English article using click-triggered underlines and a collapsible panel, allowing users to access additional facts only when interested. This approach follows the Spatial Contiguity Principle (Johnson and Mayer 2012), which emphasizes placing related information close together. Collectively, these design choices preserve reading flow while enabling low-friction, in-place access to multilingual content.

###### R2: Ensure clear language attribution and
traceability of multilingual facts to promote creditability.

In our interviews, a recurring concern among participants was the trustworthiness of information surfaced from other language editions–particularly when such facts were not present in the English version. Participants emphasized that they wanted to know “where the information comes from,“ including which language edition it originated from and the ability to read it in its original context (F3), because it is crucial for accessing information’s credibility. This requirement highlights the importance of traceability and attribution in multilingual information access. Readers must be able to understand both the linguistic source and the original context of each surfaced fact. This entails more than just showing a translation, but rather also requires visual and interactive mechanisms that reinforce provenance and credibility.

To meet this need, we present each fact with an explicit, color-coded language label and allow readers to trace each fact back to its source by opening the corresponding language edition and viewing the sentence in context. These strategies support transparency and accountability, giving readers confidence in the surfaced content and encouraging deeper multilingual exploration.

###### R3: Support both passive discovery and active exploration of cross-lingual knowledge gaps (customizable exploration).

User feedback revealed a range of interaction preferences: users want flexible access modes–both passive discovery and targeted retrieval (F4). Different participants had different expectations for how cross-lingual facts should be surfaced. Some favored passive discovery, where the system automatically highlights interesting differences without requiring user input. Others preferred more active control, such as being able to search for specific content or filter information by language or topic. They discussed concern over potential information overload if too many facts were presented at once.

This requirement reflects that readers should be able to modulate how much cross-lingual content they see and which languages they want to include in their exploration. From a cognitive standpoint, this helps reduce information overload and supports a more goal-directed behavior. It necessitates features like search, filtering, and toggling between languages – functions that empower users without requiring them to dig through entire articles in other languages.

##### 3.1.2. Core Design Elements

Based on our design process and the identified requirements (R1-R3), we developed five core design elements for WikiGap, as illustrated in Figure 1.

###### D1: In-text Gap Markers.

To address R1 (non-disruptive presentation) and R2 (traceability), we implemented a subtle underlining system that signals the presence of additional information from other language editions. Each marker is country-color coded and appears as a patterned underline within the English article. When clicked, the side panel retrieves the fact relevant to that sentence, where the extension identifies complementary or missing information from another language edition. The underline then becomes more prominent, providing interaction feedback and inviting further exploration. Each language is associated with a distinct color – red for Chinese, blue for French, and green for Russian. This color coding is applied across both in-text highlights and corresponding elements in the side panel, reinforcing source attribution as emphasized in R2. As we elaborate in Sec. 3.3.2, only significant knowledge gaps identified by InfoGap are highlighted, rather than minor variations or differences in wording. This selective highlighting prevents information overload and ensures that users’ attention is drawn to substantive cross-lingual differences.

###### D2: Cross-Lingual Fact Panel

To fulfill R1 and R2, we developed a margin-anchored sidebar that displays the facts, translated to English and organized by their source language. When a user interacts with an in-text highlight, the corresponding fact card is revealed in the sidebar, which appears on the right side of the article. The sidebar is collapsible and can be pinned for extended browsing or hidden entirely to maintain a minimalist reading view. Each language section presents its facts in dedicated groups. Each fact is shown in English, accompanied by attribution information, including the source language tag and link to the original article. The close spatial relationship between in-text cues and sidebar content supports R1’s emphasis on minimizing reading disruption.

###### D3: Fact Provenance Card

At the heart of WikiGap’s cross-lingual surfacing system is the fact card interface, which presents individual facts from other language editions in a compact, standardized format. Each fact card includes: (1) the target fact, translated into English, (2) a color-coded badge indicating the source language, and (3) a hyperlink labeled “View on [Language] Wikipedia” that opens the source article in a new tab with the original sentence highlighted. It mainly address R2 (transparent attribution), because it offers enough context to understand the fact at a glance, while providing a direct pathway to its original source for users who wish to verify or explore further.

###### D4: Source Language Filter

To support R3 (customizable exploration), we introduced a language filter function located at the top of the sidebar. These filters allow users to specify which language(s) they want to view content from, enabling personalization based on their linguistic background and interests. The filters use both language names and colors to maximize clarity. This functionality directly supports both passive and active interaction modes (R3).

###### D5: Cross-lingual Fact Search.

To further support R3, specifically the directed exploration function, we added a search box feature that allows users to perform keyword-based queries across multilingual facts. When a user enters a search term, relevant fact cards from the selected languages are retrieved and displayed in the sidebar. This feature caters to users with goal-oriented information-seeking tasks, such as verifying a specific claim or comparing facts across language editions. While D1 and D2 emphasize passive and contextual discovery, the search box fulfills a complementary role by enabling intentional, focused retrieval. Together, these elements provide a spectrum of access modes that reflect users’ varying preferences for how and when to engage with multilingual content.

#### 3.2. The InfoGap Pipeline

WikiGap relies on InfoGap, a previously developed computational pipeline introduced by Samir et al. (Samir et al. 2024), which detects factual misalignments between Wikipedia articles across languages. This subsection introduces the core components of the original InfoGap system, which we use to identify sentence-level knowledge gaps between English and other language editions. In the following section, we will describe how we extended this pipeline to support additional languages and adapted its outputs for integration into the WikiGap interface.

InfoGap is a state-of-the-art LLM-based pipeline that takes an article LsL_{s} in the source language and the respective article LtL_{t} in the target language and returns the sets of common facts and facts that are exclusive to one article. As illustrated in Figure 3, given a Wikipedia article in the source language (LsL_{s}, e.g., English) and the respective article in another language (LtL_{t}, e.g., French),
InfoGap identifies three categories of facts: those shared across editions, those unique to the source, and those unique to the target (i.e., language-exclusive facts). For example, “Oolong is a semi-oxidized Chinese tea” is shared across languages, while “It is served in US restaurants” may appear only in English.

The pipeline leverages a multilingual LLM and sentence embeddings to perform cross-lingual comparison in three stages, as illustrated in Figure 4:

- (1)

Fact decomposition.
Each paragraph in LsL_{s} and LtL_{t} is decomposed into atomic factual statements using prompts issued to a multilingual LLM. The output includes both the fact and its paragraph index for downstream alignment.

- (2)

Multilingual alignment.
Each fact is encoded using a multilingual sentence encoder. For every fact in LtL_{t}, the top three nearest neighbors in LsL_{s} are retrieved based on cosine similarity. This reduces noise and narrows the search space when looking for equivalent facts.

- (3)

Alignment verification.
For each fact in LtL_{t}, the LLM is prompted to determine whether it is inferable from any of its nearest neighbors in LsL_{s}. If a matching fact is found in LsL_{s}, these facts are considered aligned, otherwise, the fact is labeled as a knowledge gap in LsL_{s}.

Figure 3. Knowledge differences in the Wikipedia coverage of Oolong identified by InfoGap. Connecting lines mark overlapping facts; green boxes highlight facts unique to each language edition. English sentences in italics represent translations of facts from Chinese or French Wikipedia, while non-italicized English sentences are from the original English Wikipedia article.

Figure 4. Overview of the InfoGap backend pipeline for cross-lingual fact alignment, reproduced from Samir et al. 2024 and adapted. For additional technical details, see the original paper.

#### 3.3. Extending and Integrating InfoGap for WikiGap

In this section, we outline the conceptual modifications and integration steps that enable InfoGap to serve as the backend for WikiGap. We adapted and extended the existing InfoGap pipeline (Samir et al. 2024) in two key ways: (1) by enabling new language (Chinese) support beyond the original study, and (2) by building an integration layer that transforms InfoGap’s output into interactive interface components usable within our system.

##### 3.3.1. Enabling Chinese language support.

The original InfoGap pipeline was developed for detecting cross-lingual gaps in biographical articles between English and either Russian or French. To generalize the method to a new domain and an additional language, we incorporated support for Chinese into the fact decomposition and verification modules. This involved custom preprocessing for tokenization, crafting prompts, and conducting human evaluation on Chinese texts to confirm that InfoGap performs comparably to its performance on the original languages studied by Samir et al. 2024.

##### 3.3.2. Language attribution and fact selection

Our focus is on knowledge gaps – facts that appear in the LtL_{t} version (e.g., French, Russian, or Chinese) of an article but not in LsL_{s} (English). We therefore filter the InfoGap output to retain only gap facts. To ensure interface responsiveness, we use a precomputed output from InfoGap for each article topic. For every topic, we prepare a unified dataset that includes exclusive facts from three target languages (French, Russian, and Chinese). These facts are grouped by language code (fr, zh, ru) to support language-specific interaction features such as language filtering (D4). To reduce cognitive overload, we limit the number of displayed facts to 10 per language, proportionally sampling based on section-level gap counts. If fewer than 10 gaps exist for a language, we display all available facts.

##### 3.3.3. Translations and traceability.

Because WikiGap displays cross-lingual content within the English Wikipedia page to readers who we do not assume read other languages, we translate the gap facts from their original language (LtL_{t}) into English for presentation in the fact cards. To support source traceability and deeper exploration, we create a direct link-to-highlight for each fact. An encoded version of the original sentence in LtL_{t} is appended to the target article’s URL, sending readers to the exact sentence in context when they click on the “View on [LtL_{t}] Wikipedia” in the card (D3).

##### 3.3.4. In-text highlights.

For each gap fact, InfoGap outputs the most semantically related English sentence from the source article, even when the fact itself is absent in English. We use these sentences as anchors for subtle in-text highlights (D1), which allow readers to preview cross-lingual differences inline without disrupting their reading flow. Figure 5 illustrates how such outputs map onto WikiGap’s interface components. For example, the French Wikipedia article for Peking Duck mentions that the dish became a favorite of Empress Cixi in the 18th century – a detail missing from the English article. InfoGap aligns this fact to the closest English sentence “The Peking roast duck that came to be associated with the term was fully developed during the later Ming dynasty”,
which provides a semantically-relevant anchor for surfacing the French-exclusive fact in context.

Figure 5.
Overview of system implementation and data processing pipeline.
Top: A high-level overview of the data stream in the WikiGap system. We adapted the InfoGap pipeline to support Chinese-language input alongside existing language pairs, followed by post-processing steps to standardize and merge datasets by topic. Orange process blocks indicate components we developed to enable proper integration and display of multilingual facts in the UI.
Bottom: The data structure and rendering flow for an individual fact. This illustrates how each multilingual fact is transformed – through translation, alignment, tagging, and contextual linking – into an interactive component in the WikiGap interface.

#### 3.4. System Implementation

We implemented WikiGap as a browser-based system that overlays multilingual content directly onto English Wikipedia articles. The system interface was developed as a Chrome extension using standard web technologies – HTML, CSS, and vanilla JavaScript – while the underlying data pipeline generates and serves precomputed JSON files derived from the InfoGap framework. When running InfoGap, we used GPT-4o for fact decomposition and fact alignment verification, and computed sentence embeddings using the multilingual LaBSE model (OpenAI 2024b; Feng et al. 2020). For each English Wikipedia topic, InfoGap produces three separate datasets, each containing factual gaps between English and one of three target languages (fr, zh, ru). We then merge these files by topic into a unified, standardized JSON file named after the English article. This consolidation supports runtime efficiency: when a user visits an English topic page, the extension loads the corresponding file based on the topic title. Each file contains multilingual facts translated into English which are generated using GPT-4o-mini (OpenAI 2024a). The overall system workflow is illustrated in Figure 5.

The extension interacts with the live English Wikipedia page, dynamically injecting highlights and sidebar content based on the current topic the user is browsing (the corresponding dataset is selected for rendering the data on the UI based on that topic). For each fact card, we generate external links that redirect readers to the original sentence in the source-language Wikipedia article. This is done by appending an encoded version of the original sentence to the article’s base URL, allowing users to jump directly to the fact in context. Additionally, the search function is implemented by scanning both the fact body and language label for matches with the user’s input and dynamically hiding non-matching entries.

### 4. Evaluation Methods

To validate our design, we conducted a mixed-methods user evaluation study, combining quantitative performance measures and qualitative feedback, which are summarized in Table 1 and detailed below. We aim to understand WikiGap’s usability, its impact on knowledge gain, and user perceptions about the system and the cross-lingual content.33
3

The study protocol received approval from our institutional REB.

Table 1. Description of study metrics and corresponding data collection and analysis.
All metrics were collected at the individual participant level and compared across WikiGap and control conditions.

Metrics |

Data Collected
|

Data Analysis
|

Performance |
|
|

Quiz Accuracy |

Percentage of correct answers in each condition
|

Paired t-test comparing WikiGap vs. control conditions
|

Completion Time |

Time (in minutes) to complete each quiz session
|
|

Preference |
|
|

Usability |

System Usability Scale (SUS) score in each condition
|

Paired t-test comparing SUS scores between conditions
|

User Feedback |

Open-ended responses and interview transcripts
|

Thematic coding to extract perceived usability, utility, and challenges
|

#### 4.1. Participants

Twenty-one people participated in the study. Of these, eight were student volunteers from the HCI course where this project originated, and the remaining thirteen participants were recruited through Upwork, and were compensated at a rate of 20 USD for the user study. Participants ranged in age from 18 to 44 and represented diverse cultural and ethnic backgrounds (see Table 2). All participants reported that they typically use the English version of Wikipedia. Twelve had previously contributed to Wikipedia to varying degrees, with two considering themselves frequent editors. Participants were required to meet the following inclusion criteria: (i) regular use of English Wikipedia, (ii) comfort with using a Chrome browser, and (iii) willingness to contribute user experience feedback.

The study followed a within-subject design, in which each participant was assigned two out of five topics (Sec. 4.3). Each participant read one article using the WikiGap extension and another article using the default Wikipedia interface (with ILLs) as a control. The assignment of treatment and control conditions was randomized for each participant.

Table 2. Participant self-reported cultural background.

Cultural / Ethnic background |
% of participants |

East Asian |
24% |

White or European |
19% |

South Asian |
14% |

Hispanic or Latin American |
14% |

Black or African |
10% |

Middle Eastern or North
Southeast Asian |
10% |

African |
5% |

Other |
5% |

#### 4.2. Tasks

Participants completed an open-book reading quiz consisting of 10 multiple-choice questions in each condition. For each quiz, participants were provided with four Wikipedia articles on the same topic—specifically, the English article and its corresponding versions in French, Russian, and Chinese. They were instructed to rely solely on these four articles to answer the quiz questions and were not allowed to use external resources such as Google Search. Each participant completed the quiz twice: once using the standard Wikipedia interface (control condition) and once using the WikiGap extension (treatment condition). For every question, participants were also asked to indicate the language edition in which they found the answer.

###### Quiz Construction.

We constructed one quiz per article topic using facts extracted by InfoGap and surfaced through the WikiGap interface. From the 30 multilingual facts identified for each article, we manually selected a subset of 10, ensuring a roughly equal number of facts from each of the three language editions—French (fr), Russian (ru), and Chinese (zh)—to maintain balanced representation. For a fair comparison, we ensured that all quiz questions are answerable from InfoGap facts and by extension from the respective articles in French, Russian, and Chinese.

We then prompted a large language model GPT-4o (OpenAI 2024b) to generate a multiple-choice question with four answer choices from each fact. The questions were manually reviewed and edited to ensure clarity, factual correctness, and alignment with the presented content. In addition to selecting the correct answer, participants were asked to indicate the language edition in which they found the supporting fact. Although all quiz facts were sourced from non-English Wikipedia editions, we note that some participants may have inferred the correct answer from contextual clues in the English article. Nonetheless, the quizzes were designed to evaluate whether participants engaged with multilingual content. If participants had guessed entirely at random, the expected accuracy would be 25%, given the four-choice format. Example questions are included in the Appendix A.

###### Performance Metrics.

We recorded each participant’s task completion time and quiz accuracy score under both conditions. Quiz accuracy captured how much multilingual knowledge participants were able to obtain, while completion time reflected how quickly they could locate and interpret the relevant information. Taken together, these two measures provide an indication of learning efficiency and allowed us to quantitatively compare the effectiveness of WikiGap with the standard Wikipedia interface.

#### 4.3. Materials and Topic Assignment

###### Selected topics

We focus on food articles because food serves as a culturally rich lens through which to explore knowledge gaps across language editions in Wikipedia. Culinary practices are deeply embedded in regional customs, social histories, and national identities, making food a meaningful proxy for cultural knowledge (Luo et al. 2023; Winata et al. 2025). Analyzing food allows researchers to capture both shared and divergent cultural representations, such as differences in dish names, preparation styles, and regional associations (Winata et al. 2025). This cultural complexity makes food an ideal domain for surfacing factual asymmetries. We selected five culturally specific dishes: Injera (Ethiopia), Paella (Spain), Philippine Adobo (Philippines), Peking Duck (China), and Wiener Schnitzel (Austria). Each of these dishes has a dedicated Wikipedia article and distinct cultural heritage. Table 3 summarizes the number of language-exclusive facts detected per topic and the total number shown in the WikiGap interface.

All five dishes satisfy the following practical constraints: (i) they originate outside the English-speaking world, providing a comparable degree of cultural distance from the English source language, (ii) their English Wikipedia article is moderately sized (1,000–2,000 words), and (iii) the WikiGap extension can surface ~30 multilingual facts for each.44
4

Oolong tea was included in the pilot with the first two participants but was dropped because its cultural context overlapped substantially with Peking Duck. It was therefore replaced with Philippine Adobo to preserve cultural diversity in topic representation.

Table 3. Number of knowledge gap facts discovered per food topic and language by InfoGap, and the total number of facts shown in the WikiGap interface. For each topic, up to 10 facts per language were selected to ensure balanced representation and reduce cognitive overload. Injera had only 8 gaps in Chinese, resulting in 28 total facts shown (*).

Food Topic |
Russian (ru) |
French (fr) |
Chinese (zh) |
Facts Shown in WikiGap |

Wiener schnitzel |
65 |
20 |
62 |
30 |

Peking duck |
13 |
23 |
69 |
30 |

Paella |
28 |
62 |
52 |
30 |

Philippine adobo |
21 |
15 |
84 |
30 |

Injera |
10 |
14 |
8 |
28* |

###### Topic assignment

Topic assignment was designed to minimize cultural confounds and familiarity-driven performance differences. Specifically, the food topic chosen for each participant could not be strongly linked to the participant’s self-reported cultural or ethnic background. To reduce individual-performance bias, each topic was assigned in every condition to exactly four different participants.

#### 4.4. Procedure

The lead investigator conducted the study remotely over a 1–1.5 hour recorded Zoom call. At the start, participants received a zip file containing the WikiGap extension and were instructed to install it on their Google Chrome browser. A short tutorial was provided by the researcher for both the treatment and control conditions. During the treatment condition, we began the round by introducing the WikiGap’s functionality and allowed participants to explore the extension on their own until they felt ready to proceed. In the control condition, we demonstrated how to access language versions on Wikipedia using ILLs, and how to use Chrome’s Google Translate function to read the content in English. At the beginning of each round, one of the five topics was assigned to the participant according to the topic assignment rules. After completing each round, the participant completed a System Usability Scale (SUS) after finishing the quiz. We used the SUS to measure ease-of-use and users’ preference on with or without the WikiGap extension. To conclude, the first twelve participants completed an open-ended questionnaire, while the remaining nine took part in a semi-structured interview. Both instruments covered the same six areas: overall impressions of the system, presentation of multilingual information, perceived cultural impact, trust in the augmented facts, perceptions of Wikipedia’s reliability after using WikiGap, and future inclination to explore multilingual content (see Appendix B for the full list of questions).

### 5. Findings

We report findings from our mixed-method evaluation of WikiGap. We
present five key findings that drive our understanding towards the user perceptions of multilingual knowledge engagement. These findings highlight how WikiGap reshapes users’ awareness of content asymmetries, supports multilingual exploration, and triggers additional reflections on the role of provenance in a multilingual and LLM-driven knowledge landscape.

###### ①Users Strongly Preferred WikiGap over the Default ILL (D1, D2, D3)

We evaluated user preference using the System Usability Scale (SUS). The average SUS scores for each condition are presented in Figure 6, along with general SUS cutoff scores for fair, good, and excellent usability (Bangor et al. 2009). Overall, WikiGap achieved a substantially higher usability score compared to the control. WikiGap falls within the “excellent” usability category, while the default Wikipedia page with ILL scored below the “fair” threshold. A paired-samples t-test revealed a significant difference in scores between the WikiGap condition (M = 82.5, SD = 10.9) and the control condition (M = 48.2, SD = 18.6), t(20) = 6.60, p < .001.

Figure 6.
Box plot showing the System Usability Scale (SUS) scores for each condition. Blue represent the control condition (no WikiGap), and orange represent the treatment condition (with WikiGap). Horizontal dashed lines represent standard usability benchmarks in varying shades of green: light green for Fair usability (SUS > 51), medium green for Good usability (SUS > 71), and dark green for Excellent usability (SUS > 86).

Participants attributed their strong preference for WikiGap not only to its ability to surface knowledge disparities, but also to the various design elements (D1-D3) that supported the quick access and ease of reading. Many highlighted how having access to multilingual content directly within the English article – through translated facts in a sidebar (D2, D3) – lowered the barrier to engaging with other language editions. It helped users “absorb information without the language difference obstacle” (P8). Participants appreciated the sidebar’s structure and organization by language, which kept all cross-lingual facts “apparent within a single page” (P5), eliminating the need to navigate away and reducing friction in multilingual exploration. In contrast to ILL’s full-page switch model, participants noted that the sentence-level fact card interface (D3) made the information easier to process. As P11 remarked, “[WikiGap] presents sentences instead of long paragraphs from the Wikipedia page.”

Other visual elements also shaped participants’ perceptions of usability. Several users found the in-text gap markers (D1) helpful in surfacing areas of missing information in the English article. However, reactions to the color scheme used for language cues were mixed. While some found the colors intuitive, others, like P19, felt that the red-green coding could unintentionally suggest “right or wrong”.

Despite minor confusion about the color scheme, most users described the overall experience as more enjoyable and cognitively less demanding than their usual experience with Wikipedia’s default ILL. P9 summarized this sentiment: “Sometimes even when I open my Wikipedia, I would not read that much because of laziness, but WikiGap did a good job extracting information and makes the whole experience much more pleasant.”

###### ②WikiGap Enhanced Fact-Finding Performance and Cross-Cultural Learning via Passive Discovery and Active Exploration (D4, D5)

To evaluate the impact of WikiGap on users’ ability to retrieve and retain cross-lingual information, we measured task performance through a fact-finding quiz, using both accuracy and completion time as metrics. As shown in Figure 7, participants performed significantly better when using WikiGap, achieving higher quiz accuracy and completing the task more quickly than with the default Wikipedia interface. A paired-samples t-test showed that accuracy was significantly higher in the WikiGap condition (MM = 0.91, S​DSD = 0.09) than in the control condition (MM = 0.73, S​DSD = 0.19), t(20) = 4.75, p < .001. Completion time also improved significantly, with users finishing the quiz faster using WikiGap (MM = 12.39 minutes, S​DSD = 5.78) compared to the control (MM = 20.84 minutes, S​DSD = 8.68), t(20) = -5.52, p < .001.55
5

Faster completion times in the WikiGap condition is partly expected, as the quiz questions were constructed from facts extracted by InfoGap. In real-world use, not all facts would be presented by WikiGap, and completion time gains may therefore be more modest. These results suggest that WikiGap not only facilitated access to relevant information but also improved users’ efficiency in locating and interpreting cross-lingual facts. WikiGap consistently improved user performance across all five culturally diverse topics. For a topic-by-topic breakdown of quiz accuracy and completion time, see Appendix Figure 8.

Figure 7.
Average completion time (left) and quiz accuracy (right) across conditions. Blue represent the control condition (no WikiGap), and orange represent the treatment condition (with WikiGap). Using WikiGap demonstrates a statistically significant improvement in user performance on the quiz.

These performance gains were reinforced by participants’ qualitative feedback, which highlighted the value of both passive discovery and active exploration features. The fact search (D5) enabled users to directly retrieve relevant facts, supporting goal-oriented behaviors and speeding up information retrieval. As P16 explained, “I don’t need to go to multiple pages. I can search in the WikiGap extension and find any information quickly. Using the WikiGap extension saved me a lot of time.” This targeted retrieval helped users answer questions more efficiently, contributing to the improved fact-finding performance observed in the quiz metrics. Complementing this, the language filter controls (D4) allowed users to personalize their exploration by prioritizing facts from languages culturally aligned with the topic. Several participants reported that they first filtered to the language they deemed most relevant, as they“will trust more when the language is directly aligned with the original country of the food.” (P1). Similarly, P7 remarked, “I would love to see how the Tagalog page talks about Philippine adobo. In fact, diverse cultural perspectives on food is more linked to the cultural ecosystem where the food is grounded.”. Together, D4 and D5 supported efficient, goal-driven access to cross-lingual content.

Beyond performance gains, the extension also facilitated passive discovery and cross-cultural learning – a central goal of our design. Several users remarked that they encountered information they would not have actively sought out on their own. As P1 reflected, “Without [WikiGap], I wouldn’t have thought about looking into Wikipedia pages in different languages.” Others described moments of unexpected cultural insight, such as P5, who noted, “I would have completely missed out on the historical aspect if I used Wikipedia normally (only in English).” Participants also pointed to surprising culture-specific facts, like the culinary use of Sprite in a traditional dish (P13). These examples illustrate that WikiGap not only supported successful task completion but also broadened users’ awareness of culturally situated knowledge that is often absent from English Wikipedia.

###### ③WikiGap Raises Awareness of Multilingual Gaps and Motivates Exploration

Participants consistently credited WikiGap for revealing factual disparities they were previously unaware of. Several users described being surprised that different language versions did not simply mirror each other. As P20 reflected, “Before WikiGap, I always assumed that everything presented in English would also be visible in another language.” Similarly, P18 noted that they “didn’t know there could be so many differences in how the content was presented in various languages.”

This realization often triggered a sense of frustration, as users became aware of the limits of English Wikipedia.

“I’m frustrated that this doesn’t already exist! I feel like I’ve been missing out on information from other languages because I just assumed other pages would have the same information translated.” — P5

Other participants had deeper reflections on how WikiGap changed their perception about knowledge: “Knowledge is not plain, knowledge has different dimensions waiting to be discovered, and this tool offers this opportune moment.” (P10).

Importantly, the awareness raised by WikiGap also led to changes in participants’ attitudes and future behaviors. Now they can “see different viewpoints from different language pages“ (P17), they are more inclined to explore content outside their primary language in the future. Several users described feeling more motivated to engage with multilingual content now that they understood its value.

“I was never on the pages of Wikipedia where the language is not what I speak, because I often assume that all pages under different languages are the same if they are of the same topic, so sometimes I struggled to find some information in the Wikipedia. But if I have WikiGap, I think I will definitely explore more.” — P9

Echoing this, Since WikiGap displays multilingual content in one centralized place, it provides great convenience to explore cross-lingual knowledge, and contributes to users’ willingness to engage. As P1 noted, “If there’s a tool like WikiGap that can help me easily get various information from other pages, I would like to explore. If not, I wouldn’t navigate multiple pages myself.”

###### ④Respondents’ Views on LLMs and Wikipedia: Perceived Trust and Tensions

Awareness of cross-lingual disparities also led participants to reflect on the trustworthiness of Wikipedia and how it compares to LLM-based knowledge sources. We observed a wide range of perspectives. For some, WikiGap surfaced surprising inconsistencies between language editions. Those differences made them question the completeness or neutrality of English Wikipedia. Others interpreted these variations not as flaws, but as a feature of Wikipedia’s multilingualism and editorial diversity. These divergent views led participants to compare Wikipedia to emerging alternatives such as LLMs, positioning WikiGap as a catalyst for rethinking how people evaluate and engage with knowledge sources.

A minority (n=2) of the participants reported a decline in trust in Wikipedia after using WikiGap. They described how uncovering missing or differing facts between language editions made them feel less confident in the platform’s ability to represent comprehensive or balanced information. This, in turn, increased their inclination to rely on LLMs as knowledge sources:

“I feel that after using WikiGap, I would be inclined to use Wikipedia even less. Before this, I assumed that Wikipedia would be a reliable and complete source of knowledge. However, I now know that the English version misses several key details. This leads me to be more reliant on LLM-based tools that have all the information in one place.” — P2

For this participant and others, WikiGap altered their perception of Wikipedia as a trustworthy authority. The perceived comprehensiveness of LLMs, combined with their ability to synthesize content across sources, positioned them as a more efficient alternative, even if they lacked transparency.66
6

In practice, the assumption that multilingual LLMs such as ChatGPT and Gemini can synthesize information learned from web text in different languages is not entirely true; they often fail to retrieve facts learned in one language when prompted in another language (Goldman et al. 2025).

However, not all participants responded this way. Others voiced strong concerns about the lack of attribution and provenance in LLM-generated responses, and emphasized that WikiGap made them appreciate Wikipedia’s editorial structure and citation practices even more. For these users, the ability to trace facts back to their original source, including reading the sentence in the original language edition, was critical to their sense of trust:

“I don’t trust ChatGPT that much because sometimes it just makes things up, and it doesn’t provide sources. With WikiGap, I can click on, say, the French Wikipedia page, read it, and see the sources. It feels more reliable. I also appreciate that Wikipedia cites everything, so there’s some quality control, even if it’s not always perfect.” — P13

These contrasting responses underscore an important dynamic in how users engage with knowledge platforms: while LLMs offer convenience and perceived comprehensiveness, they can lack the transparency and editorial accountability that are central to Wikipedia’s epistemic model. For some users, WikiGap undermined their confidence in Wikipedia. For others, it reaffirmed the value of its provenance-driven structure, even in the face of inconsistency. We return to the socio-technical implications in Sec. 6.

###### ⑤WikiGap Supports Editors in Validating and Integrating Multilingual Content

Although WikiGap was primarily designed to support readers by surfacing factual cross-lingual content, a few participants, particularly those with prior editing experience, reflected on how it could assist with editorial tasks. These insights point to an emergent opportunity for WikiGap to support not only knowledge consumption but also knowledge curation on Wikipedia.

Some users noted that the ability to trace and verify information from other language editions made the tool useful for improving article quality. As one frequent editor explained, “Sometimes an article in another language has crucial information that’s missing in English. WikiGap helps me find and translate it, then cite it properly.” (P16). Another participant elaborated on how the tool fits into their existing editing workflow: “I’d check the source WikiGap shows me, then cite the same source… WikiGap helps me discover facts and references.” (P17).
While these reflections were not the result of targeted prompts or interview questions targeted towards editing-specific tasks, they highlight WikiGap’s broader potential to support contributors in bridging cross-lingual knowledge gaps.

### 6. Discussion

In this work, we sought to combat the epistemic injustice (Ajmani et al. 2023a) posed by the dominance of the English Wikipedia project over other language editions. We did so by leveraging novel affordances brought by advances in fine-grained cross-linguistic comparison (Samir et al. 2024), enabling us to identify factual gaps in English Wikipedia and succinctly display them to readers. By surfacing complementary facts through WikiGap, our system performs an infrastructural inversion (Star 1999): it makes visible the hidden cross-lingual knowledge gaps while productively challenging the long-standing English-as-superset assumption. Importantly, this intervention is introduced with minimal disruption to the familiar English Wikipedia reading experience. Beyond enabling access to a more complete set of factual information, our work educates readers about how knowledge on multilingual Wikipedia is composed and contested. Through this sociotechnical interaction, WikiGap demonstrates how systems can foster more equitable collaboration in distributed knowledge production across linguistic boundaries (Ackerman 2000), reshaping how knowledge is consumed and shared across communities. Below, we discuss how English Wikipedia came to have a limited demographic representation in its editor base, yet an outsized global readership (Sec. 6.1); how the English-as-superset hypothesis still persists among readers, despite its debunking in prior seminal studies from over a decade ago (Hecht and Gergle 2010, e.g.,) (Sec. 6.2); and why this epistemology is a byproduct of the subsuming culture of computationalism (Golumbia 2009), which (in part) explains its stubborn persistence (Sec. 6.3).

#### 6.1. Editor-Readership Asymmetry in English Wikipedia

While English has undeniably achieved the status of a global lingua franca (Schneider 2019), this does not mean that English speakers worldwide have had equal opportunity to contribute to English Wikipedia. Wikipedia as a whole is animated by an ethos of participatory, democratic knowledge curation. Yet from its inception, historical inequities have undermined this libertarian ideal (Shaw and Hargittai 2018). Participation in the internet has been unequal, both within and across nation-states, with greater access among socially privileged individuals. Four years after English Wikipedia was launched, access to the internet for developing countries was still in the single digits, percentage-wise (Chen and Wellman 2005). Within nation states, internet usage is clearly stratified across gender, socioeconomic class, race, and a stark urban-rural divide (Chen and Wellman 2005), many of which have also been studied in the context of English Wikipedia (Johnson et al. 2016; Hargittai and Shaw 2015; Adams et al. 2019). The inequities that were present during the establishment of English Wikipedia matter, as peer production processes are understood to ossify and concentrate power among a small group of early editors, resembling an oligarchy (Shaw and Hill 2014). This editor–reader asymmetry exemplifies a socio-technical gap (Ackerman 2000), in which the ideals of open participation clash with the realities of unequal collaboration in a large-scale knowledge infrastructure.

Although these disparities are well studied, Wikimedia has struggled to reduce these editor demographic skews. As of (Wikimedia Foundation 2024b), English Wikipedia contributions are still overwhelmingly contributed by male-identifying editors, and there is a remarkable lack of Black and Hispanic editors from within the United States (Wikimedia Foundation 2024b).

Wikipedia’s most prominent pillar, the Neutral Point-of-View (NPOV) policy, has been roundly criticized for obstructing more equitable production of knowledge. In particular, it runs counter to feminist epistemology that the act of knowing is necessarily situated, that there is no voice from nowhere (Haraway 2013). Importantly, the policy has been criticized for obscuring the role of patriarchic and Anglocentric power structures in how knowledge produced by different communities is appraised (Foucault 2013; Kumar 2017). Kumar 2017 situates this discourse in a case-study on Indian editors presenting arguments on the naming of the Ganga river (as opposed to the Ganges river) on English Wikipedia. Ultimately, the smaller group of Indian editors was overwhelmed by the preponderance of reliable Anglocentric sources that asserted the veracity of the Ganges label. The case-study is illustrative of how the notion of neutrality is in fact biased towards information that is disseminated from Anglocentric institutions. Importantly, this discounts against knowledge derived from lived experiences and societies that privilege oral traditions, or have had historically unequal opportunities in access to the internet (Avieson and Mazumdar 2025).

It is important to note that English Wikipedia attracts a massive readership, even outside of the geographic Anglosophere. As Kumar 2017 notes (at the time), 20%20\% of English Wikipedia’s visitors were based in India, even more than readers from the United Kingdom. The composition of English Wikipedia’s editor base is thus hardly representative of the broader population of literate, internet-equipped English speakers. As acknowledged in responses to our open-ended surveys, readers believe in the knowledge of local authorities. As one participant noted: “diverse cultural perspectives on food is more linked to the cultural ecosystem where the food is grounded” (P7). Indeed, the capacity for volunteers to contribute and disseminate information from geographically-situated sources was seen as one of the primary benefits of Wikipedia (Sen et al. 2015), Yet prior work highlights that readers are not simply passive consumers but active participants with distinct roles and needs, and that their preferences do not always align with where editorial effort is concentrated. This production–consumption gap poses a fundamental challenge for distributed collaborative work: designing socio-technical processes of knowledge creation that account for readers as well as editors (Antin and Cheshire 2010; Lehmann et al. 2014). There is thus a strong impetus to achieve more equitable knowledge representation. WikiGap presents an important contribution towards achieving greater epistemic equity.

#### 6.2. English-as-superset Hypothesis Lives On

Although there are well-documented structural barriers to contributing to English Wikipedia, its overwhelming dominance makes it appear as a superset of the information contained in all other language editions, rather than a necessarily biased and socio-geographically-positioned construction (Kumar 2021). Hecht 2013 studied this perception of English Wikipedia, calling it the English-as-superset hypothesis, writing that the hypothesis is “commonly adopted in Wikipedia-based research projects and systems”. Practically, this has entailed designating English Wikipedia as the ground-truth language edition for assessing, for example, the correctness of question-answering systems (Asai et al. 2021).

Although there is now greater appreciation among Wikipedia researchers of the cross-linguistic information diversity between Wikipedia language editions, there is little reason to expect the broader Wikipedia userbase outside of Wikipedia experts to be privy to these results. As Hickman et al. 2021 documented in their cross-linguistic comparative analysis of articles pertaining to Kashmir, editors of Hindi and Urdu articles drew on English Wikipedia for their primary research to a large extent. Their editing process thus implies an underlying acceptance of the English-as-superset hypothesis, where English Wikipedia is perceived as neutral, objective, and, critically, complete.

Our user studies also demonstrate the prevalence of the hypothesis, with some participants commenting on the hypothesis directly: “Before WikiGap, I always assumed that everything presented in English would also be visible in another language.” Thus, while Hecht and Gergle 2010 effectively critiqued the English-as-superset hypothesis 1515 years ago, its continued prevalence calls for greater institutional intervention to increase awareness among the broader Wikipedia userbase of the vast cross-linguistic diversity between language editions.

Our research demonstrates that the WikiGap interface directly challenges the English-as-superset perception as well as the invisibility problem: The sentence-level complementary facts presented by WikiGap function as boundary objects (Star and Griesemer 1989), serving users across different linguistic communities by making the otherwise hidden contributions of diverse editor communities visible and facilitating understanding of the distributed nature of collaborative knowledge production.
As such, adoption of our interface can challenge the problematic status quo.

#### 6.3. Objectivity in Knowledge Representation

It should be acknowledged however that the epistemic assumption of the English-as-superset hypothesis is deeply ingrained in the broader culture of computationalism (Golumbia 2009). Computationalism is concerned with treating the mind as a computer, and thereby entails the aim of codifying knowledge with digital precision. This entails that all concepts, even socioculturally-contingent artifacts like cultural dishes, have one-to-one definitions, in the form of a single collection of facts (Golumbia 2009, Chapter 6). The role of language here, then, is a cryptographic encoding scheme, rather than a reflection of socio-geographic context (Golumbia 2009, Chapter 4). Within this cultural philosophy, it makes sense that cross-linguistic diversity between language editions are seen by some as a deviation, a shortcoming, relative to a monolithic, consistent set of facts. This is why some computational research projects have formulated cross-linguistic diversity as a problem to be solved (see Sec. 2).

Our study showed that some participants, although a minority, held perspectives that are aligned with computationalism (Sec. 5). That is, they viewed the gaps in English Wikipedia (foregrounded by WikiGap) as a shortcoming of the English language edition, making them perceive it as less “reliable” and “complete”, and even asking, akin to the work we describe in Sec. 2, why all Wikipedia language editions don’t contain the same set of facts. We thus see that cross-linguistic diversity is perceived by some as being in opposition to neutrality and objectivity. One of these participants even said they would prefer to turn to LLMs, which conveys what they perceive as a consolidated view of all information on a prompted topic. In this light, we can understand that some view LLMs as the purest form of the “voice from nowhere” (Haraway 2013), in practically a literal sense.

While there have been anxieties circulating around how contributions to Wikipedia might be affected by the emergence of LLMs (Maiberg 2024), our work highlights that Wikipedia’s role in presenting information to readers is similarly in flux. That is, our work demonstrated that readers looking for an (ostensibly) objective summary of a topic may turn to LLMs over Wikipedia. While LLMs pose some advantages (directly answering user queries), they also marginalize the role of provenance in accessing information (Shah and Bender 2022). WikiGap presents one approach for encouraging continued readership of Wikipedia as it highlights one of its foundational strengths: an established platform for soliciting citation-backed Volunteered Geographic Information from all around the world (Sen et al. 2015), containing a plurality of socio-geographically positioned perspectives (Figure 3). The current multilingual reading experience facilitated by Interlanguage Links fails to foreground this strength, however. Instead, readers are led to believe that Wikipedia’s language editions reflect global consensus – that the information on the pages are consistent. As Hecht and Gergle 2010 explain, a natural corollary of believing in global consensus is the English-as-superset hypothesis, which contributes a form of epistemic injustice by marginalizing novel information in other language editions. As demonstrated in our user evaluations, WikiGap does well to promote epistemic equity across language editions.

#### 6.4. Limitations and Future Work

###### Language Coverage.

In this study, we intentionally focused on English and three additional language editions, namely Russian, French, and Chinese. We chose the first two as the performance of InfoGap was validated on English, French, and Russian (Samir et al. 2024), and we additionally evaluated the performance of the system on Chinese for this work as some co-authors were proficient in Chinese. Several participants expressed a desire for broader language coverage, particularly for pages in their language of origin. For example, one participant noted,
“I would love to see how the Tagalog page could complement it. In fact, diverse cultural perspectives on food are more linked to the cultural ecosystem where the food is grounded” (P7).
Expanding to more languages will enrich cross-cultural perspectives and align with users’ expectations in future work.
The underlying InfoGap pipeline is language-agnostic: in principle, it can operate on any language that GPT-4 supports, though quality may vary, especially for low-resource languages. This is important for future research as smaller language editions remain largely understudied and present additional challenges in their own right (Nigatu et al. 2024; Khatri et al. 2022).

###### WikiGap content selection.

We selected a random subset of facts to present from other language editions (Sec. 3.3.2 for further detail). This selection could be improved for greater localization through applying a geoprovenance classifier (Sen et al. 2015), thereby emphasizing those facts that are sourced from a geographical region relevant to the language edition. This is an important step for future work as our respondents expressed the desire for localized Volunteered Geographic Information.

###### Other barriers in facilitating epistemic justice in Wikipedia.

WikiGap presents only one potential component of the puzzle towards achieving greater epistemic justice in Wikipedia. But other critical challenges have been identified in facilitating the growth of smaller language editions. To name a few, the gender divide that has been reported largely in English Wikipedia is present in many other language editions (Johnson et al. 2021). Some smaller language editions are difficult to contribute to due to the lack of language technology support that is taken for granted in larger ones, such as spellcheck and translation (Nigatu et al. 2024). Other language editions lack scholarly sources in the local language, making it difficult to corroborate contributed information (Nigatu et al. 2024; Sen et al. 2015). Smaller language editions also lack established mentorship structures, making it difficult for new editors to contribute content (Khatri et al. 2022). All of these challenges ultimately affect WikiGap, as they limit the set of useful facts that can be presented in the interface.

###### Capacity for misinformation contagion.

Language editions vary considerably in their susceptibility to organized disinformation campaigns (Kharazian et al. 2024). Thus, there is a risk of spreading misinformation from other language editions into English Wikipedia through WikiGap. WikiGap may thus inadvertently make smaller language editions more attractive for actors carrying out disinformation campaigns, as audience size has previously been proposed as a motivating factor for bad-faith contributions (Kharazian et al. 2024). Care should be thus taken in deploying WikiGap, with attention paid to the language editions and topics that are selected for the extension.

###### System Architecture.

WikiGap demonstrates a socio-technical intervention that aims to reshape how people access, relate to, and interpret multilingual knowledge, which is beyond a purely technical innovation. We have an overwhelmingly positive result from the evaluation. It’s important to acknowledge that these results come from a relatively controlled setting. While the findings are encouraging, future work will need to address the technical and interaction challenges of deploying a live, scalable version of the system in more variable real-world conditions.

### 7. Conclusion

WikiGap contends with longstanding structural inequalities in Wikipedia by enabling readers to access cross-lingual facts directly within the English interface. Through a novel combination of fact-centric text comparison (Samir et al. 2024, InfoGap;) based on LLMs (Min et al. 2023) and user-centered design, the system unobtrusively displays knowledge missing due to linguistic and editorial asymmetries. Our evaluation shows that WikiGap not only improves usability and fact-finding efficiency, but also fosters greater awareness of cultural variation and the limitations of assuming English Wikipedia as a default knowledge base. By surfacing multilingual content in context, WikiGap connects readers with perspectives on topics that are situated outside of the Anglosphere, connections that were previously occluded by the hegemonic dominance of English Wikipedia (Kumar 2021, Chapter 3). This work demonstrates how augmentative tools can shift reader practices and challenge epistemic assumptions, paving the way for more inclusive, transparent, and culturally grounded knowledge infrastructures.

####### Acknowledgements.

ChatGPT was utilized to generate code snippets and to assist in refining the grammar and writing style of this work. All AI-generated content was reviewed and edited by the authors to ensure accuracy and adherence to academic standards.
This work was funded, in part, by the Vector Institute for AI, Canada CIFAR AI Chairs program, Accelerate Foundation Models Research Program Award from Microsoft, and an NSERC discovery grant

### References

- (1)

- Ackerman (2000)

Mark S. Ackerman. 2000.

The intellectual challenge of CSCW: the gap between social requirements and technical feasibility.

Hum.-Comput. Interact. 15, 2 (Sept. 2000), 179–203.

doi:10.1207/S15327051HCI1523_5

- Adams et al. (2019)

Julia Adams, Hannah Brückner, and Cambria Naslund. 2019.

Who counts as a notable sociologist on wikipedia? gender, race, and the “professor test”.

Socius 5 (2019), 2378023118823946.

- Adar et al. (2009)

Eytan Adar, Michael Skinner, and Daniel S Weld. 2009.

Information arbitrage across multi-lingual Wikipedia. In Proceedings of the Second ACM International Conference on Web Search and Data Mining. 94–103.

- Ajmani et al. (2023a)

Leah Ajmani, Mo Houtti, Jasmine C Foriest, Michael Ann Devito, Nicholas Vincent, and Isaac Johnson. 2023a.

Epistemic Injustice in Online Communities: Unpacking the Values of Knowledge Creation and Curation within CSCW Applications. In Companion Publication of the 2023 Conference on Computer Supported Cooperative Work and Social Computing. 527–531.

- Ajmani et al. (2023b)

Leah Ajmani, Nicholas Vincent, and Stevie Chancellor. 2023b.

Peer Produced Friction: How Page Protection on Wikipedia Affects Editor Engagement and Concentration.

Proceedings of the ACM on Human-Computer Interaction 7, CSCW2 (2023), 1–33.

- Ajmani et al. (2024)

Leah Hope Ajmani, Jasmine C. Foriest, Jordan Taylor, Kyle Pittman, Sarah Gilbert, and Michael Ann DeVito. 2024.

Whose Knowledge is Valued? Epistemic Injustice in CSCW Applications.

Proc. ACM Hum.-Comput. Interact. 8, CSCW2, Article 523 (Nov. 2024), 28 pages.

doi:10.1145/3687062

- Antin and Cheshire (2010)

Judd Antin and Coye Cheshire. 2010.

Readers are not free-riders: reading as a form of participation on wikipedia. In Proceedings of the 2010 ACM Conference on Computer Supported Cooperative Work (Savannah, Georgia, USA) (CSCW ’10). Association for Computing Machinery, New York, NY, USA, 127–130.

doi:10.1145/1718918.1718942

- Asai et al. (2021)

Akari Asai, Jungo Kasai, Jonathan Clark, Kenton Lee, Eunsol Choi, and Hannaneh Hajishirzi. 2021.

XOR QA: Cross-lingual Open-Retrieval Question Answering. In Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Kristina Toutanova, Anna Rumshisky, Luke Zettlemoyer, Dilek Hakkani-Tur, Iz Beltagy, Steven Bethard, Ryan Cotterell, Tanmoy Chakraborty, and Yichao Zhou (Eds.). Association for Computational Linguistics, Online, 547–564.

doi:10.18653/v1/2021.naacl-main.46

- Avieson and Mazumdar (2025)

Bunty Avieson and Suruchi Mazumdar. 2025.

Wiki warriors: language editors counter knowledge hierarchies during the pandemic.

Asian Journal of Communication (2025), 1–19.

- Bangor et al. (2009)

Aaron Bangor, Philip Kortum, and James Miller. 2009.

Determining what individual SUS scores mean: adding an adjective rating scale.

J. Usability Studies 4, 3 (May 2009), 114–123.

- Bao et al. (2012)

Patti Bao, Brent Hecht, Samuel Carton, Mahmood Quaderi, Michael Horn, and Darren Gergle. 2012.

Omnipedia: bridging the wikipedia language gap. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems. 1075–1084.

- Benjamin (2023)

Ruha Benjamin. 2023.

Race after technology.

In Social Theory Re-Wired. Routledge, 405–415.

- Benkler et al. (2015)

Yochai Benkler, Aaron Shaw, and Benjamin Mako Hill. 2015.

Peer production: A form of collective intelligence.

Handbook of collective intelligence 175 (2015).

- Bipat et al. (2021)

Taryn Bipat, Negin Alimohammadi, Yihan Yu, David W McDonald, and Mark Zachry. 2021.

Wikipedia Beyond the English Language Edition: How do Editors Collaborate in the Farsi and Chinese Wikipedias?

Proceedings of the ACM on Human-Computer Interaction 5, CSCW1 (2021), 1–39.

- Callahan and Herring (2011)

Ewa S Callahan and Susan C Herring. 2011.

Cultural bias in Wikipedia content on famous persons.

Journal of the American society for information science and technology 62, 10 (2011), 1899–1915.

- Chen and Wellman (2005)

Wenhong Chen and Barry Wellman. 2005.

Minding the cyber-gap: The internet and social inequality.

The Blackwell companion to social inequalities (2005), 523–545.

- Cohen (2008)

Noam Cohen. 2008.

Open-Source Troubles in Wiki World.

New York Times.

https://www.nytimes.com/2008/03/17/technology/17wikipedia.html

- Duh et al. (2013)

Kevin Duh, Ching-Man Au Yeung, Tomoharu Iwata, and Masaaki Nagata. 2013.

Managing information disparity in multilingual document collections.

ACM Transactions on Speech and Language Processing (TSLP) 10, 1 (2013), 1–28.

- Feng et al. (2020)

Fangxiaoyu Feng, Yinfei Yang, Daniel Cer, Naveen Arivazhagan, and Wei Wang. 2020.

Language-agnostic BERT Sentence Embedding. In Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP). Association for Computational Linguistics, 879–894.

https://arxiv.org/abs/2007.01852

- Foucault (2013)

Michel Foucault. 2013.

Archaeology of knowledge.

routledge.

- Geiger and Ribes (2010)

R. Stuart Geiger and David Ribes. 2010.

The work of sustaining order in wikipedia: the banning of a vandal. In Proceedings of the 2010 ACM Conference on Computer Supported Cooperative Work (Savannah, Georgia, USA) (CSCW ’10). Association for Computing Machinery, New York, NY, USA, 117–126.

doi:10.1145/1718918.1718941

- Goldman et al. (2025)

Omer Goldman, Uri Shaham, Dan Malkin, Sivan Eiger, Avinatan Hassidim, Yossi Matias, Joshua Maynez, Adi Mayrav Gilady, Jason Riesa, Shruti Rijhwani, Laura Rimell, Idan Szpektor, Reut Tsarfaty, and Matan Eyal. 2025.

ECLeKTic: a Novel Challenge Set for Evaluation of Cross-Lingual Knowledge Transfer.

arXiv:2502.21228 [cs.CL]

https://arxiv.org/abs/2502.21228

- Golumbia (2009)

David Golumbia. 2009.

The cultural logic of computation.

Harvard University Press.

- Hale (2014)

Scott A Hale. 2014.

Multilinguals and Wikipedia editing. In Proceedings of the 2014 ACM conference on Web science. 99–108.

- Haraway (2013)

Donna Haraway. 2013.

Situated knowledges: The science question in feminism and the privilege of partial perspective 1.

In Women, science, and technology. Routledge, 455–472.

- Hargittai and Shaw (2015)

Eszter Hargittai and Aaron Shaw. 2015.

Mind the skills gap: the role of Internet know-how and gender in differentiated contributions to Wikipedia.

Information, communication & society 18, 4 (2015), 424–442.

- Hecht and Gergle (2009)

Brent Hecht and Darren Gergle. 2009.

Measuring self-focus bias in community-maintained knowledge repositories. In Proceedings of the fourth international conference on communities and technologies. 11–20.

- Hecht and Gergle (2010)

Brent Hecht and Darren Gergle. 2010.

The tower of Babel meets web 2.0: user-generated content and its applications in a multilingual context. In Proceedings of the SIGCHI conference on human factors in computing systems. 291–300.

- Hecht (2013)

Brent Jaron Hecht. 2013.

The mining and application of diverse cultural perspectives in user-generated content.

Ph. D. Dissertation. Northwestern University.

- Hickman et al. (2021)

Molly G Hickman, Viral Pasad, Harsh Kamalesh Sanghavi, Jacob Thebault-Spieker, and Sang Won Lee. 2021.

Understanding wikipedia practices through hindi, urdu, and english takes on an evolving regional conflict.

Proceedings of the ACM on Human-Computer Interaction 5, CSCW1 (2021), 1–31.

- Hwang and Shaw (2022)

Sohyeon Hwang and Aaron Shaw. 2022.

Rules and rule-making in the five largest wikipedias. In Proceedings of the International AAAI Conference on Web and Social Media, Vol. 16. 347–357.

- Johnson and Mayer (2012)

Cheryl I Johnson and Richard E Mayer. 2012.

An eye movement analysis of the spatial contiguity effect in multimedia learning.

Journal of Experimental Psychology: Applied 18, 2 (2012), 178.

- Johnson et al. (2021)

Isaac Johnson, Florian Lemmerich, Diego Sáez-Trumper, Robert West, Markus Strohmaier, and Leila Zia. 2021.

Global gender differences in Wikipedia readership. In Proceedings of the International AAAI Conference on Web and Social Media, Vol. 15. 254–265.

- Johnson and Lescak (2022)

Isaac Johnson and Emily Lescak. 2022.

Considerations for multilingual wikipedia research.

arXiv preprint arXiv:2204.02483 (2022).

- Johnson et al. (2016)

Isaac L Johnson, Yilun Lin, Toby Jia-Jun Li, Andrew Hall, Aaron Halfaker, Johannes Schöning, and Brent Hecht. 2016.

Not at home on the range: Peer production and the urban/rural divide. In Proceedings of the 2016 CHI conference on Human Factors in Computing Systems. 13–25.

- Justice and Golumbia (2024)

George Justice and David Golumbia. 2024.

Cyberlibertarianism: The right-wing politics of digital technology.

University of Minnesota Press.

- Kharazian et al. (2024)

Zarine Kharazian, Kate Starbird, and Benjamin Mako Hill. 2024.

Governance capture in a self-governing community: A qualitative comparison of the croatian, serbian, bosnian, and serbo-croatian wikipedias.

Proceedings of the ACM on Human-Computer Interaction 8, CSCW1 (2024), 1–26.

- Khatri et al. (2022)

Sejal Khatri, Aaron Shaw, Sayamindu Dasgupta, and Benjamin Mako Hill. 2022.

The social embeddedness of peer production: A comparative qualitative analysis of three Indian language Wikipedia editions. In Proceedings of the 2022 CHI Conference on Human Factors in Computing Systems. 1–18.

- Kittur and Kraut (2010)

Aniket Kittur and Robert E. Kraut. 2010.

Beyond Wikipedia: coordination and conflict in online production groups. In Proceedings of the 2010 ACM Conference on Computer Supported Cooperative Work (Savannah, Georgia, USA) (CSCW ’10). Association for Computing Machinery, New York, NY, USA, 215–224.

doi:10.1145/1718918.1718959

- Kumar (2017)

Sangeet Kumar. 2017.

A river by any other name: Ganga/Ganges and the postcolonial politics of knowledge on Wikipedia.

Information, Communication & Society 20, 6 (2017), 809–824.

- Kumar (2021)

Sangeet Kumar. 2021.

The digital frontier: Infrastructures of control on the global web.

Indiana University Press.

- Laufer et al. (2015)

Paul Laufer, Claudia Wagner, Fabian Flöck, and Markus Strohmaier. 2015.

Mining cross-cultural relations from Wikipedia: a study of 31 European food cultures. In Proceedings of the ACM web science conference. 1–10.

- Lehmann et al. (2014)

Janette Lehmann, Claudia Müller-Birn, David Laniado, Mounia Lalmas, and Andreas Kaltenbrunner. 2014.

Reader preferences and behavior on Wikipedia. In Proceedings of the 25th ACM Conference on Hypertext and Social Media (Santiago, Chile) (HT ’14). Association for Computing Machinery, New York, NY, USA, 88–97.

doi:10.1145/2631775.2631805

- Luo et al. (2023)

Yiwei Luo, Kristina Gligoric, and Dan Jurafsky. 2023.

Othering and Low Status Framing of Immigrant Cuisines in US Restaurant Reviews and Large Language Models. In International Conference on Web and Social Media.

https://api.semanticscholar.org/CorpusID:259936860

- Maiberg (2024)

Emanuel Maiberg. 2024.

The Editors Protecting Wikipedia from AI Hoaxes.

404 Media (9 October 2024).

- Marshall (1997)

Catherine C Marshall. 1997.

Annotation: from paper books to the digital library. In Proceedings of the second ACM international conference on Digital libraries. 131–140.

- Massa and Scrinzi (2012)

Paolo Massa and Federico Scrinzi. 2012.

Manypedia: Comparing language points of view of Wikipedia communities. In Proceedings of the Eighth Annual International Symposium on Wikis and Open Collaboration. 1–9.

- Min et al. (2023)

Sewon Min, Kalpesh Krishna, Xinxi Lyu, Mike Lewis, Wen-tau Yih, Pang Wei Koh, Mohit Iyyer, Luke Zettlemoyer, and Hannaneh Hajishirzi. 2023.

Factscore: Fine-grained atomic evaluation of factual precision in long form text generation.

arXiv preprint arXiv:2305.14251 (2023).

- Negri et al. (2013)

Matteo Negri, Alessandro Marchetti, Yashar Mehdad, Luisa Bentivogli, and Danilo Giampiccolo. 2013.

Semeval-2013 Task 8: Cross-lingual Textual Entailment for Content Synchronization. In Second Joint Conference on Lexical and Computational Semantics (*SEM), Volume 2: Proceedings of the Seventh International Workshop on Semantic Evaluation (SemEval 2013), Suresh Manandhar and Deniz Yuret (Eds.). Association for Computational Linguistics, Atlanta, Georgia, USA, 25–33.

https://aclanthology.org/S13-2005/

- Nigatu et al. (2024)

Hellina Hailu Nigatu, John Canny, and Sarah E Chasins. 2024.

Low-Resourced Languages and Online Knowledge Repositories: A Need-Finding Study.. In Proceedings of the 2024 CHI Conference on Human Factors in Computing Systems. 1–21.

- Oberhaus (2017)

Daniel Oberhaus. 2017.

Wikipedia’s Top Editors Are Staying Secretive and Elite.

https://www.vice.com/en/article/wikipedia-editors-elite-diversity-foundation/

Accessed: 2025-03-24.

- Oeberst and Ridderbecks (2024)

Aileen Oeberst and Till Ridderbecks. 2024.

How article category in Wikipedia determines the heterogeneity of its editors.

Scientific Reports 14 (2024).

https://api.semanticscholar.org/CorpusID:266842093

- OpenAI (2024a)

OpenAI. 2024a.

GPT-4o mini: Advancing Cost-Efficient Intelligence.

https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence.

Large language model, July 18 version.

- OpenAI (2024b)

OpenAI. 2024b.

GPT-4o System Card.

arXiv preprint arXiv:2410.21276 (2024).

https://arxiv.org/abs/2410.21276

- Pirolli and Card (1999)

Peter Pirolli and Stuart Card. 1999.

Information foraging.

Psychological review 106, 4 (1999), 643.

- Roy et al. (2022)

Dwaipayan Roy, Sumit Bhatia, and Prateek Jain. 2022.

Information asymmetry in Wikipedia across different languages: A statistical analysis.

Journal of the Association for Information Science and Technology 73, 3 (2022), 347–361.

- Said (1977)

Edward W Said. 1977.

Orientalism.

The Georgia Review 31, 1 (1977), 162–206.

- Samir et al. (2024)

Farhan Samir, Chan Young Park, Anjalie Field, Vered Shwartz, and Yulia Tsvetkov. 2024.

Locating Information Gaps and Narrative Inconsistencies Across Languages: A Case Study of LGBT People Portrayals on Wikipedia. In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, Yaser Al-Onaizan, Mohit Bansal, and Yun-Nung Chen (Eds.). Association for Computational Linguistics, Miami, Florida, USA, 6747–6762.

doi:10.18653/v1/2024.emnlp-main.384

- Schneider (2019)

Britta Schneider. 2019.

Methodological nationalism in linguistics.

Language Sciences 76 (2019), 101169.

- Sen et al. (2015)

Shilad W Sen, Heather Ford, David R Musicant, Mark Graham, OS Keyes, and Brent Hecht. 2015.

Barriers to the localness of volunteered geographic information. In Proceedings of the 33rd Annual ACM Conference on Human Factors in Computing Systems. 197–206.

- Shah and Bender (2022)

Chirag Shah and Emily M Bender. 2022.

Situating search. In Proceedings of the 2022 Conference on Human Information Interaction and Retrieval. 221–232.

- Shaw and Hargittai (2018)

Aaron Shaw and Eszter Hargittai. 2018.

The pipeline of online participation inequalities: The case of Wikipedia editing.

Journal of communication 68, 1 (2018), 143–168.

- Shaw and Hill (2014)

Aaron Shaw and Benjamin M Hill. 2014.

Laboratories of oligarchy? How the iron law extends to peer production.

Journal of Communication 64, 2 (2014), 215–238.

- Star (1999)

Susan Leigh Star. 1999.

The Ethnography of Infrastructure.

American Behavioral Scientist 43, 3 (1999), 377–391.

doi:10.1177/00027649921955326

- Star and Griesemer (1989)

Susan Leigh Star and James R. Griesemer. 1989.

Institutional Ecology, ‘Translations’ and Boundary Objects: Amateurs and Professionals in Berkeley’s Museum of Vertebrate Zoology, 1907-39.

Social Studies of Science 19, 3 (1989), 387–420.

doi:10.1177/030631289019003001
arXiv:https://doi.org/10.1177/030631289019003001

- Vincent and Hecht (2021)

Nicholas Vincent and Brent Hecht. 2021.

A deeper investigation of the importance of Wikipedia links to search engine results.

Proceedings of the ACM on Human-Computer Interaction 5, CSCW1 (2021), 1–15.

- Wagner et al. (2016)

Claudia Wagner, Eduardo Graells-Garrido, David Garcia, and Filippo Menczer. 2016.

Women through the glass ceiling: gender asymmetries in Wikipedia.

EPJ data science 5, 1 (2016), 5.

- Wikimedia Foundation (2011)

Wikimedia Foundation. 2011.

Editor Survey Report – April 2011.

Technical Report. Wikimedia Foundation.

https://upload.wikimedia.org/wikipedia/commons/7/76/Editor_Survey_Report_-_April_2011.pdf

Accessed.

- Wikimedia Foundation (2024a)

Wikimedia Foundation. 2024a.

Announcing English Wikipedia’s most popular articles of 2024.

https://wikimediafoundation.org/news/2024/12/03/announcing-english-wikipedias-most-popular-articles-of-2024/

Accessed: 2025-09-09.

- Wikimedia Foundation (2024b)

Wikimedia Foundation. 2024b.

Community Insights 2024 Report.

https://meta.wikimedia.org/wiki/Community_Insights/Community_Insights_2024_Report

Accessed: 2025-03-12.

- Wikipedia contributors (2025)

Wikipedia contributors. 2025.

Wikipedia:Statistics.

https://en.wikipedia.org/wiki/Wikipedia:Statistics

Accessed: 2025-04-13.

- Winata et al. (2025)

Genta Indra Winata, Frederikus Hudi, Patrick Amadeus Irawan, David Anugraha, Rifki Afina Putri, Wang Yutong, Adam Nohejl, Ubaidillah Ariq Prathama, Nedjma Ousidhoum, Afifa Amriani, Anar Rzayev, Anirban Das, Ashmari Pramodya, Aulia Adila, Bryan Wilie, Candy Olivia Mawalim, Cheng Ching Lam, Daud Abolade, Emmanuele Chersoni, Enrico Santus, Fariz Ikhwantri, Garry Kuwanto, Hanyang Zhao, Haryo Akbarianto Wibowo, Holy Lovenia, Jan Christian Blaise Cruz, Jan Wira Gotama Putra, Junho Myung,
Lucky Susanto, Maria Angelica Riera Machin, Marina Zhukova, Michael Anugraha, Muhammad Farid Adilazuarda, Natasha Christabelle Santosa, Peerat Limkonchotiwat, Raj Dabre, Rio Alexander Audino, Samuel Cahyawijaya, Shi-Xiong Zhang, Stephanie Yulia Salim, Yi Zhou, Yinxuan Gui, David Ifeoluwa Adelani, En-Shiun Annie Lee, Shogo Okada, Ayu Purwarianti, Alham Fikri Aji, Taro Watanabe, Derry Tanti Wijaya, Alice Oh, and Chong-Wah Ngo. 2025.

WorldCuisines: A Massive-Scale Benchmark for Multilingual and Multicultural Visual Question Answering on Global Cuisines. In Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), Luis Chiruzzo, Alan Ritter, and Lu Wang (Eds.). Association for Computational Linguistics, Albuquerque, New Mexico, 3242–3264.

https://aclanthology.org/2025.naacl-long.167/

### Appendix A Sample Quiz Questions

We present two example questions from each of the five topics used in our study. These examples illustrate the format and cultural specificity of the quiz items. All questions were drawn from the 30 language-exclusive facts surfaced by WikiGap, and were manually reviewed for clarity and accuracy. The correct answers are bolded in Table 4.

Table 4. Example Quiz Questions Across Topics. Correct answers are bolded.

Topic
|

Question 1
|

Question 2
|

Peking Duck
|

What unique preparation step is done to the duck before roasting it for Peking duck?

A. It is marinated in soy sauce

B. It is inflated with air under the skin

C. It is stuffed with rice

D. It is boiled in water
|

What is served after the meat in a traditional Peking duck meal?

A. A fruit platter

B. Rice

C. Chinese cabbage soup

D. A cup of tea
|

Wiener Schnitzel
|

During which historical period was Wiener schnitzel brought to Italy and then to Austria?

A. World War I

B. French Revolution

C. Napoleonic Wars

D. Renaissance
|

Which city of China has a type of Western cuisine similar to Vienna schnitzel?

A. Beijing

B. Nanjing

C. Guangdong

D. Shanghai
|

Paella
|

What festival is Spanish paella associated with?

A. La Tomatina

B. San Fermín

C. Falles

D. Semana Santa
|

How was paella traditionally eaten?

A. On plates

B. In bowls

C. Straight from the cooking pan

D. Consumed with bread
|

Philippine Adobo
|

Which ingredient is sometimes added to adobo to replace palm or coconut sugar and help tenderize the meat?

A. Honey

B. Molasses

C. Sprite

D. Maple syrup
|

Which of the following is a traditional method used in adobo to keep meat fresh in tropical climates?

A. Drying the meat

B. Frying with vinegar

C. Smoking the meat

D. Freezing the meat
|

Injera
|

How large is traditional injera typically?

A. 30 centimeters

B. Half a meter

C. About 1 meter

D. 2 meters
|

Injera closely resembles which Middle Eastern pancake variant?

A. Naan

B. Lahoh

C. Pita

D. Lavash
|

### Appendix B Interview and Questionnaire Protocol

Participants were asked the following questions during either the semi-structured interview or the open-ended questionnaire.

- •

Describe your experience using WikiGap. What stood out to you the most, and why?

- •

When you enabled WikiGap to see multilingual facts, how did you feel about the way information was presented? What aspects of the presentation worked well or could be improved?

- •

Can you describe a specific fact you discovered through WikiGap that surprised you or changed your understanding of the topic? How did this discovery influence your perception or understanding of diverse cultural viewpoints?

- •

When using WikiGap, how did you decide which information to trust? Please explain your reasoning.

- •

After using WikiGap, do you see Wikipedia as more reliable or complete, especially for finding information from other languages? Please explain your answer with examples if possible.

- •

In what ways, if any, did WikiGap change your perception or understanding of diverse cultural viewpoints related to the topics you explored?

- •

Did using WikiGap make you more inclined to explore content outside your primary language in the future? Why or why not?

### Appendix C Average Completion Time and Accuracy across Different Topics

Figure 8.
Side-by-side bar charts comparing average completion time and accuracy across different topics, with and without the WikiGap extension. Blue represent the control condition (no WikiGap), and orange represent the treatment condition (with WikiGap).

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
