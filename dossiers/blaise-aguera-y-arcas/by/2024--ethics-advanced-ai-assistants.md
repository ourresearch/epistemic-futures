---
title: "The Ethics of Advanced AI Assistants"
person: blaise-aguera-y-arcas
section: by
type: journal-article
year: 2024
date: 2024-04-24
venue: "arXiv (Cornell University)"
authors: "Iason Gabriel, Arianna Manzini, Geoff Keeling, Lisa Anne Hendricks, Verena Rieser, Hasan Iqbal, Nenad Tomašev, Sofia Ira Ktena, Zachary Kenton, M. Balsa Rodríguez, Seliem El-Sayed, Sasha Brown et al."
source_url: http://arxiv.org/abs/2404.16244
retrieved: 2026-08-13
content: full-text
notes: "OpenAlex W4395686739 (type: preprint). Full text extracted from the open-access PDF at https://arxiv.org/pdf/2404.16244. Body truncated at 400KB cap; see source_url for the rest."
---

# The Ethics of Advanced AI Assistants

## Full text

### Abstract (from OpenAlex metadata)

This paper focuses on the opportunities and the ethical and societal risks posed by advanced AI assistants. We define advanced AI assistants as artificial agents with natural language interfaces, whose function is to plan and execute sequences of actions on behalf of a user, across one or more domains, in line with the user's expectations. The paper starts by considering the technology itself, providing an overview of AI assistants, their technical foundations and potential range of applications. It then explores questions around AI value alignment, well-being, safety and malicious uses. Extending the circle of inquiry further, we next consider the relationship between advanced AI assistants and individual users in more detail, exploring topics such as manipulation and persuasion, anthropomorphism, appropriate relationships, trust and privacy. With this analysis in place, we consider the deployment of advanced assistants at a societal scale, focusing on cooperation, equity and access, misinformation, economic impact, the environment and how best to evaluate advanced AI assistants. Finally, we conclude by providing a range of recommendations for researchers, developers, policymakers and public stakeholders.

---

2024-04-19

The Ethics of Advanced AI Assistants
Iason Gabriel* 1 , Arianna Manzini* 1 , Geoff Keeling* 2 , Lisa Anne Hendricks1 , Verena Rieser1 , Hasan Iqbal1 ,
Nenad Tomašev1 , Ira Ktena1 , Zachary Kenton1 , Mikel Rodriguez1 , Seliem El-Sayed1 , Sasha Brown1 , Canfer
Akbulut1 , Andrew Trask1 , Edward Hughes1 , A. Stevie Bergman1 , Renee Shelby2 , Nahema Marchal1 , Conor
Griffin1 , Juan Mateos-Garcia1 , Laura Weidinger1 , Winnie Street2 , Benjamin Lange2,4 , Alex Ingerman2 , Alison
Lentz2 , Reed Enger2 , Andrew Barakat2 , Victoria Krakovna1 , John Oliver Siy2 , Zeb Kurth-Nelson1 , Amanda
McCroskery2 , Vijay Bolina1 , Harry Law1 , Murray Shanahan1 , Lize Alberts2,5,6 , Borja Balle1 , Sarah de Haas2 ,
Yetunde Ibitoye2 , Allan Dafoe1 , Beth Goldberg3 , Sébastien Krier1 , Alexander Reese2 , Sims Witherspoon1 , Will

arXiv:2404.16244v2 [cs.CY] 28 Apr 2024

Hawkins1 , Maribeth Rauh1 , Don Wallace1 , Matija Franklin7 , Josh A. Goldstein8 , Joel Lehman9 , Michael
Klenk10 , Shannon Vallor11 , Courtney Biles1 , Meredith Ringel Morris1 , Helen King1 , Blaise Agüera y Arcas2 ,
William Isaac1 and James Manyika2
* Equal contributions, 1 Google DeepMind, 2 Google Research, 3 Jigsaw, 4 Ludwig-Maximilians-Universität München, 5 University of

Oxford, 6 Stellenbosch University, 7 University College London, 8 Center for Security and Emerging Technology, 9 Independent,
10 Delft University of Technology, 11 University of Edinburgh

This paper focuses on the opportunities and the ethical and societal risks posed by advanced AI assistants. We
define advanced AI assistants as artificial agents with natural language interfaces, whose function is to plan
and execute sequences of actions on behalf of a user – across one or more domains – in line with the user’s
expectations. The paper starts by considering the technology itself, providing an overview of AI assistants, their
technical foundations and potential range of applications. It then explores questions around AI value alignment,
well-being, safety and malicious uses. Extending the circle of inquiry further, we next consider the relationship
between advanced AI assistants and individual users in more detail, exploring topics such as manipulation and
persuasion, anthropomorphism, appropriate relationships, trust and privacy. With this analysis in place, we
consider the deployment of advanced assistants at a societal scale, focusing on cooperation, equity and access,
misinformation, economic impact, the environment and how best to evaluate advanced AI assistants. Finally,
we conclude by providing a range of recommendations for researchers, developers, policymakers and public
stakeholders.
Our analysis suggests that advanced AI assistants are likely to have a profound impact on our individual and
collective lives. To be beneficial and value-aligned, we argue that assistants must be appropriately responsive to
the competing claims and needs of users, developers and society. Features such as increased agency, the capacity
to interact in natural language and high degrees of personalisation could make AI assistants especially helpful
to users. However, these features also make people vulnerable to inappropriate influence by the technology,
so robust safeguards are needed. Moreover, when AI assistants are deployed at scale, knock-on effects that
arise from interaction between them and questions about their overall impact on wider institutions and social
processes rise to the fore. These dynamics likely require technical and policy interventions in order to foster
beneficial cooperation and to achieve broad, inclusive and equitable outcomes. Finally, given that the current
landscape of AI evaluation focuses primarily on the technical components of AI systems, it is important to invest
in the holistic sociotechnical evaluations of AI assistants, including human–AI interaction, multi-agent and
societal level research, to support responsible decision-making and deployment in this domain.

Corresponding author(s): Iason Gabriel <iason@google.com>
© 2024 Google DeepMind. All rights reserved

Contents

Contents

ii

PART I: INTRODUCTION

1

Executive Summary

1

1 Introduction
1.1 The Ethics of Advanced AI Assistants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.2 Key Questions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.3 Methodology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.4 Limitations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.5 Overall Structure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.6 A Note to the Reader . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

3
3
4
5
7
7
11

PART II: ADVANCED AI ASSISTANTS

12

2 Definitions
2.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2 What’s in a Definition? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.3 What is an AI Assistant? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.4 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

12
12
13
15
17

3 Technical Foundations
3.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.2 Foundation Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.3 From Foundation Models to Assistants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.4 Challenges and Avenues for Future Research . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.5 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

19
19
19
21
22
24

4 Types of Assistant
4.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2 From AI Tools to AI Assistants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3 The Capabilities of AI Assistants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.4 Potential Applications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.5 AI Assistants as the Interface of the Future . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.6 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

25
25
26
27
28
30
32

PART III: VALUE ALIGNMENT, SAFETY AND MISUSE

33

5 Value Alignment

33
ii

The Ethics of Advanced AI Assistants

5.1
5.2
5.3
5.4

Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
AI Value Alignment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Value Alignment and Advanced AI Assistants . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

33
35
39
42

6 Well-being
6.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2 Understanding Well-being . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3 Measuring Well-being . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.4 Influence of Current Technology on Well-being . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.5 Opportunities and Risks with AI Assistants . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.6 Outlook . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.7 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

45
45
46
48
49
51
53
53

7 Safety
7.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.2 Safety Engineering . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.3 AI Safety . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.4 Safety for Advanced AI Assistants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.5 Mitigations and Future Research . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.6 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

55
55
56
57
58
64
67

8 Malicious Uses
8.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8.2 Malicious Uses of AI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8.3 Malicious Uses of Advanced AI Assistants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8.4 Recommendations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8.5 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

68
68
69
70
77
79

PART IV: HUMAN–ASSISTANT INTERACTION

80

9 Influence
9.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9.2 Modes of Influence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9.3 Evaluating Influence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9.4 Mechanisms of Influence by AI Assistants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9.5 Possible Harms Arising from AI Influence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9.6 Mitigating Undue Influence by AI Assistants . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9.7 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

80
80
81
84
86
87
89
91

10 Anthropomorphism
93
10.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93
10.2 Anthropomorphism: Definition, Mechanism and Function . . . . . . . . . . . . . . . . . . . . . 94
10.3 Anthropomorphic Interactive Systems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
10.4 Anthropomorphism and AI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
10.5 Risk of Harm through Anthropomorphic AI Assistant Design . . . . . . . . . . . . . . . . . . . 99
10.6 Directions for Future Research . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
10.7 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
iii

The Ethics of Advanced AI Assistants

11 Appropriate Relationships
11.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
11.2 Appropriate Human Interpersonal Relationships . . . . . . . . . . . . . . . . . . . . . . . . . .
11.3 Distinctive Features of User–AI Assistant Relationships . . . . . . . . . . . . . . . . . . . . . .
11.4 Risks and Mitigations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
11.5 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

107
107
108
110
111
117

12 Trust
12.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
12.2 Trust in AI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
12.3 Trust and Advanced AI Assistants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
12.4 Well-Calibrated Trust in User–AI Assistant Interactions . . . . . . . . . . . . . . . . . . . . . .
12.5 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

119
119
120
123
126
130

13 Privacy
13.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
13.2 Privacy and AI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
13.3 Privacy for Advanced AI Assistants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
13.4 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

131
131
132
133
137

PART V: AI ASSISTANTS AND SOCIETY

138

14 Cooperation
14.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
14.2 Cooperation and AI Assistants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
14.3 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

138
138
139
144

15 Access and Opportunity
15.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
15.2 Inequality and Technology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
15.3 Case Studies: Access, Opportunity and AI . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
15.4 Access and Advanced AI Assistants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
15.5 Access-Related Risks and Advanced AI Assistants . . . . . . . . . . . . . . . . . . . . . . . . .
15.6 Beyond Mitigation: From Unequal to Liberatory Access . . . . . . . . . . . . . . . . . . . . . .
15.7 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

146
146
147
148
150
152
154
155

16 Misinformation
16.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
16.2 The Challenge of Misinformation and Disinformation . . . . . . . . . . . . . . . . . . . . . . .
16.3 Misinformation, Disinformation and AI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
16.4 Misinformation, Disinformation and Advanced AI Assistants . . . . . . . . . . . . . . . . . . .
16.5 Risks and Mitigations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
16.6 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

157
157
158
159
161
163
166

17 Economic Impact
17.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
17.2 How Has AI Affected the Economy to Date? . . . . . . . . . . . . . . . . . . . . . . . . . . . .
17.3 How Will AI Assistants Affect the Economy? . . . . . . . . . . . . . . . . . . . . . . . . . . . .
17.4 Policy Implications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

167
167
167
172
176
iv

The Ethics of Advanced AI Assistants

17.5 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 177
18 Environmental Impact
18.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
18.2 The Environmental Impact of AI Systems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
18.3 The Environmental Impact of Advanced AI Assistants . . . . . . . . . . . . . . . . . . . . . . .
18.4 Mitigating Negative Environmental Impact . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
18.5 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

178
178
179
182
185
187

19 Evaluation
19.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
19.2 Evaluating AI Systems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
19.3 Evaluating Advanced AI Assistants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
19.4 The Limits of Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
19.5 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

188
188
189
191
193
194

PART VI: CONCLUSION

195

20 Conclusion
195
20.1 Key Themes and Insights . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 195
20.2 Opportunities, Risks and Recommendations . . . . . . . . . . . . . . . . . . . . . . . . . . . . 201
Bibliography

212

v

PART I: INTRODUCTION

Executive Summary

Iason Gabriel, Arianna Manzini, Geoff Keeling
The development of increasingly advanced artificial intelligence (AI) assistants marks the beginning of a
technological paradigm shift. While early assistant technologies such as Amazon’s Alexa and Apple’s Siri
employed narrow AI for tasks such as text-to-speech and intent classification, the emerging class of advanced
AI assistants leverage general-purpose foundation models to enable greater generality, autonomy and scope of
application. These assistants offer novel services to users, including summarisation, ideation, planning and tool
use – capabilities that we anticipate will develop further as the underlying technology continues to improve.
Advanced AI assistants thus have the potential for deep integration into our economic, social and personal
lives, and could redefine how humans experience and relate to AI.
This paper argues that advanced AI assistants raise a number of profound ethical and societal questions for
users, developers and the societies into which this technology is received. These include questions around value
alignment, safety and misuse, human–assistant interactions and the broader societal implications of advanced
AI assistants – including for equity and access, the economy and the environment. Our aim in this paper is to
offer the first systematic treatment of the ethical and societal questions presented by advanced AI assistants,
and in doing so to characterise the opportunities and risks of this emerging class of AI technologies.
Six key themes emerge from our analysis:
1. AI assistants have the potential to be a profoundly impactful technology via their deep integration into
almost every aspect of our lives. In particular, AI assistants have the potential to serve as creative partners,
research assistants, counsellors, companions and even a resource which people turn to when making
long-term plans or choosing life goals. As such, AI assistants could radically alter the nature of work,
education and creative pursuits as well as how we communicate, coordinate and negotiate with one
another, ultimately influencing who we want to be and to become.
2. AI assistants have significant autonomy to plan and execute sequences of actions in line with high-level
user instructions. Because of this, they present novel challenges around safety, alignment and misuse. In
particular, the more autonomous AI assistants are, the greater the potential for accidents arising from
misspecified or misinterpreted instructions and the greater the potential for highly impactful forms of
1

The Ethics of Advanced AI Assistants

misuse. To address these potential failure modes, this paper proposes a rich sociotechnical approach to
alignment that factors in the needs and responsibilities of users, developers and society.
3. AI assistants may be increasingly human–like and enable significant levels of personalisation. While
this is beneficial in some cases, it also opens up a complex set of questions around trust, privacy,
anthropomorphism, relationships with AI and the moral limits of personalisation. In particular, it
is important that relationships with AI assistants be beneficial, preserve autonomy and not rest upon
unwarranted emotional entanglement or material dependence.
4. AI assistants may have significant social impacts, both in terms of the distribution of benefits and burdens
within society and by fundamentally altering the ways in which humans cooperate and coordinate with
one another. While the failure to coordinate effectively could lead to suboptimal outcomes in the form of
collective action problems or other socially problematic situations, cooperative assistants may also be able
to identify common ground that was previously out of reach. Given the potential utility of assistants, it is
also important that the technology remain broadly accessible and be designed with the needs of different
users and non-users in mind.
5. Efforts to properly understand AI assistants and their impact encounter an evaluation gap when studied
using existing methods. In the context of AI research, existing approaches to evaluation tend to focus
exclusively on model evaluation and are thus potentially less sensitive to more general ways in which
AI assistants may underperform when considered as part of a broader sociotechnical system. New
methodologies and evaluation suites focusing in particular on human–AI interaction, multi-agent and
societal effects are needed to support strong evaluation and foresight in this area.
6. The responsible development and deployment of AI assistants requires further research, policy work and
public discussion. On the one hand, AI assistants give rise to a number of novel normative and technical
research challenges. For example, questions arise about appropriate privacy norms for assistant–assistant
and assistant–human interactions and about how to implement these norms in advanced assistants. On
the other hand, developers, policymakers and the public all have a critical role to play in developing
and supporting governance initiatives around AI assistants. Building upon wide stakeholder input, these
initiatives should aim to develop industry best practice, enable public scrutiny and accountability, and
advance policy recommendations and regulatory safeguards that are in the public interest.
The paper has four main sections. Part II introduces advanced AI assistants, in particular defining the
technology, explaining its technical foundations and outlining plausible applications. Part III examines value
alignment in relation to advanced AI assistants before turning to questions around well-being, safety and
malicious uses. Part IV considers a class of ethical questions arising in relation to human–assistant interactions
– in particular those concerning manipulation and persuasion, anthropomorphism, relationships, trust and
privacy. Part V explores a set of questions at the intersection of AI assistants and society, including questions
around cooperation and competition, equity and access, misinformation and economic and environmental
impact. It also examines the sociotechnical evaluation of advanced AI assistants. Finally, Part VI concludes with
analysis of the underlying themes and with recommendations.
We stand at the beginning of an era of technological and societal transformation marked by the development
of advanced AI assistants. Which path the technology develops along is in large part a product of the choices
we make now, whether as researchers, developers, policymakers and legislators or as members of the public.
We hope that the research presented in this paper will function as a springboard for further coordination and
cooperation to shape the kind of AI assistants we want to see in the world.
2

Chapter 1
Introduction

Iason Gabriel, Arianna Manzini, Geoff Keeling

1.1. The Ethics of Advanced AI Assistants
This paper focuses on the ethics of advanced AI assistants, understood as artificial agents with natural language
interfaces, the function of which is to plan and execute sequences of actions on the user’s behalf – across
one or more domains – and in line with the user’s expectations. While AI assistants such as Apple’s Siri and
Amazon’s Alexa have existed for over a decade, our expectation is that more advanced AI assistants, powered
by large foundation models, will surpass the capabilities of these earlier systems in a number of ways, including
generality, scope of action and overall levels of autonomy. Indeed, the earliest advanced AI assistants, such as
Meta AI, Google’s Gemini models, Microsoft’s Copilot, Inflection’s Pi and OpenAI’s Assistants API, emerged in
the latter half of 2023, and there is good reason to expect rapid increases in generality, scope of action and
autonomy as the underlying foundation model technology continues to evolve. If this anticipated trajectory
continues to unfurl, advanced AI assistants are likely to raise a number of profound ethical and societal questions
for users of the technology, for developers and for society more widely. Taken together, the development of
more advanced AI assistants – and their potential for deep integration into our political, economic, social and
personal lives – may herald a new phase in our relationship with AI technology; one in which questions about
alignment with our individual and collective goals, interests and values come to the fore.
To be clear, a world in which some of us are surrounded by and rely upon advanced and potentially
human-like AI assistants, while others do not, may be quite different from the one that we now live in. In
certain respects, this world could be a great improvement on the present state of affairs. AI assistants could be
an important source of practical help, creative stimulation and even, within appropriate bounds, emotional
support or guidance for their users. Practically speaking, efforts are currently underway to develop advanced
assistants that are able to function as personal planners, educational tutors, brainstorming partners, scientific
research assistants, relationship counsellors and even companions or friends. In other respects, this world could
be much worse. It could be a world of heightened dependence on technology, loneliness and disorientation.
Although the precise form and capabilities of advanced AI assistants are not yet known, the extent to which
tasks may be outsourced to it, the anthropomorphic potential of this technology and the ability to speak to
users fluently using human language, all create the possibility of material reliance and unhealthy dependence
upon it. The existence of advanced AI assistants may also confer abilities on those who have access to them
which are out of reach for those who do not. This could compound the challenge of access and opportunity
that we already encounter at the societal level.
Which world we step into is, to a large degree, a product of the choices we make now – and how we choose
3

The Ethics of Advanced AI Assistants

to proceed as users of this technology, as developers and as members of the society into which AI assistants
may well be received. Yet, given the myriad of challenges and range of interlocking issues involved in creating
beneficial AI assistants, we may also wonder how best to proceed. This paper explores a number of deep
underlying questions about the ethical and societal implications of advanced AI assistants. By engaging in a
practice of robust ethical foresight, our goals are to better anticipate where the tide of technological change may
take us and to anchor responsible decision-making as we contribute to, interact with and co-create outcomes in
this domain.
The paper starts by considering the technology itself and different types of advanced AI assistant. It then
explores questions around AI value alignment, well-being, safety and malicious uses. Extending the circle of
inquiry further, we next look at the relationship between advanced AI assistants and individual users in more
detail by exploring topics such as influence, anthropomorphism, appropriate relationships, trust and privacy.
With this analysis in place, we consider the deployment of this technology at a societal level by focusing on
cooperation, misinformation, equity and access, economic impact and environment, and we look at how best to
evaluate advanced AI assistants. Finally, we conclude by providing some further reflections on what we have
found.
Ultimately, AI assistants that could have such a transformative impact on our lives must be appropriately
responsive to the competing claims and needs of users, developers and society. Moreover, their behaviour
should conform to principles that are appropriate for the domain they operate in. These principles are best
understood as the outcome of fair deliberation at the societal level, and they include laws, norms and ethical
standards.

1.2. Key Questions
The span of questions raised by advanced AI assistants is wide-ranging and potentially daunting. In this section
we provide an overview of some of the key questions that arise in this context. Each question receives detailed
treatment in a later chapter dedicated to the specific topic. The intention of this section is only to provide some
sense of the wider ethical landscape – and of the underlying motivation behind this paper.
This overview may also be helpful to readers because of the interlocking nature of the challenges and
opportunities that advanced AI assistants give rise to. Awareness of one set of issues frequently feeds into and
supports deeper understanding of another. In total, we present 16 clusters of questions about advanced AI
assistants relating to the deeper analysis and themes that surface in this paper. The full structure of the paper
and chapter contents are covered in the penultimate section of this chapter.
Key questions for the ethical and societal analysis of advanced AI assistants include:
1. What is an advanced AI assistant? How does an AI assistant differ from other kinds of AI technology?
2. What capabilities would an advanced AI assistant have? How capable could these assistants be?
3. What is a good AI assistant? Are there certain values that we want advanced AI assistants to evidence
across all contexts?
4. Are there limits on what AI assistants should be allowed to do? If so, how are these limits determined?
5. What should an AI assistant be aligned with? With user instructions, preferences, interests, values,
well-being or something else?
6. What issues need to be addressed for AI assistants to be safe? What does safety mean for this class of
4

The Ethics of Advanced AI Assistants

technologies?
7. What new forms of persuasion might advanced AI assistants be capable of? How can we ensure that users
remain appropriately in control of the technology?
8. How can people – especially vulnerable users – be protected from AI manipulation and unwanted
disclosure of personal information?
9. Is anthropomorphism for AI assistants morally problematic? If so, might it still be permissible under
certain conditions?
10. What are the hallmarks of an appropriate relationship between human users and advanced AI assistants?
When is a relationship inappropriate and why?
11. How should AI assistants interact with one another? In what ways might interaction failures lead to
social harm? Conversely, what kinds of benefit might successful cooperation unlock?
12. How might the introduction of powerful AI assistants affect the relationship between users and non-users?
What forms of inequality do we need to countenance and address ahead of time?
13. How are advanced AI assistants likely to affect the information ecosystem and public fora? Will they
compound or ameliorate the problem of misinformation and disinformation?
14. How are the economic benefits and burdens created by AI assistants likely to be distributed across society?
What can be done to ensure that benefits are distributed widely?
15. What is the environmental impact of AI assistants likely to be? What can be done to ensure that their
future adoption is compatible with global climate goals?
16. How can we have confidence that an AI assistant is sufficiently safe, reliable or value-aligned? What kind
of evaluations are needed at the agent, user and system level?
These questions guide much of the subsequent investigation.

1.3. Methodology
A key challenge, when it comes to the responsible development, deployment and use of advanced AI assistants
arises from the possibility that technological progress in this area outpaces our capacity for ethical foresight
– leading to the deployment of technologies that are largely untested and that have hitherto undiagnosed
harmful consequences for individuals and society at large (Moor, 1985).
In the present case, concerning advanced AI assistants, uncertainty about future developments and interaction effects arise in part from the nature and trajectory of the technology itself. Recent years have seen the
exponential growth in model size and compute used to train more powerful AI agents, combined with the
emergence of impressive and sometimes surprising model capabilities (Ganguli et al., 2022). Furthermore,
with large technology companies integrating AI assistants into platforms with billions of users, and start-ups
attracting vast flows of capital in this space, there is good reason to expect continued and rapid development of
AI assistant technologies in the near-to-medium future. At the same time, the ability to converse fluently with
generally capable AI assistants is also a relatively new phenomenon. This means that there are relatively few
studies or precedents to draw upon when it comes to understanding the role that this technology will play in
people’s lives.1 Uncertainty also arises from the complex environment shaping AI deployment, including a range
1 There is, however, a sizable human–computer interaction literature on assistants.

5

The Ethics of Advanced AI Assistants

of competitive and complementary dynamics that bear upon AI assistants, users, developers and governments
as they aim to unlock the potential of this technology (Dafoe, 2018). In situations where uncertainty dovetails
with high stakes or risk of harm, it becomes particularly morally consequential, as is true for a wide range of
prospective AI assistant technologies today.
Taken together, these trends point towards the inadequacy of a purely reactive approach to responsible
decision-making. If we wait to know for sure how these matters will play out, it will likely be too late to
intervene effectively – let alone to ask more fundamental questions about what ought to be built or what it
means for this technology to be good (Collingridge, 1980). What we need instead is a proactive approach to
ethics – one that equips us for the kind of challenges that we are now set to encounter. This future-oriented or
‘anticipatory’ ethics seeks to understand and successfully model future trajectories ahead of time, to guard
against potential harm and prevent it from coming about, and to steer the development and deployment of the
technology itself towards socially beneficial outcomes (Stilgoe et al., 2013).
Speaking to the character of our current situation, in which the bounds of human action far surpass
those of previous generations as a result of technological advances, the philosopher Hans Jonas writes that
‘knowledge. . . becomes a prime duty beyond anything claimed for it heretofore, and the knowledge must
be commensurate with the causal scale of our actions’ (Jonas, 1984, 7–8). As Jonas makes clear, we have
increasingly important epistemic duties to try and understand the implications of technology ahead of time, as
well as complementary practical duties to respond to this knowledge effectively. What kind of knowledge is
needed to fulfil these aims in the context of the development and deployment of advanced AI assistants?
In this paper, we argue that informed future-facing ethics is best understood as a form of sociotechnical
speculative ethics. This ethics is inevitably speculative and involves imagination because it addresses technologies
that often do not yet exist (Lange et al., 2023; Racine et al., 2014). However, it also aims to be empirically
rigorous. Using our capacity for ethical foresight, we need to model the future accurately to evaluate potential
paths and outcomes in light of the best available evidence about the current state of affairs. Moreover, the
approach is sociotechnical. This kind of analysis needs to build upon an understanding of the technology itself,
interaction dynamics between the technology and those who use it, and the social system or practice within
which it is embedded (Selbst et al., 2019). Indeed, although it is sometimes neglected, the system level is
where the moral valence of a technology most fully comes into view, and also where a critical and evaluative
lens can often most readily be brought to bear (Jasanoff, 2016; Weidinger et al., 2023a). This kind of analysis
forms an important part of existing approaches to responsible research and innovation (Stilgoe et al., 2013).
Moreover, calls for this kind of robust sociotechnical foresight now also abound in the context of AI (Lazar and
Nelson, 2023; Mohamed et al., 2020).
The following chapters dig deep into the technical foundations of AI assistants, while also advancing
rigorous investigation into the kinds of user interaction and societal dynamic that shape the way in which
the technology is likely to be developed and received. The paper is built around a series of overlapping
investigations undertaken by groups of subject matter experts, ethicists, scientists, engineers, designers and
developers involved in AI assistant research. Extensive feedback has also been solicited from a variety of
external experts. The analysis is therefore heavily interdisciplinary, building upon detailed analysis of existing
trends and trajectories, and incorporating evidence from fields such as computer science, human–computer
interaction research, psychology, economics, sociology, political science, ecological science, moral and political
philosophy, and more.
Knowledge, foresight and imagination all have an important role to play when it comes to the deployment
of safe and ethical AI assistants. However, they are not enough to ensure positive outcomes in this space.
Responsible decision-making requires moral maturity, intentionality and a sense of appropriate stakes. It

6

The Ethics of Advanced AI Assistants

requires ethics and an attentiveness to ethics throughout the entire life cycle of development, evaluation
and deployment. Viewed in this light, the research presented here is meant to function as a springboard for
responsible exploration, learning and action. More precisely, our hope is that it can be used to: (1) inform
operational ethics and safety work among those developing, evaluating and deploying this technology, (2)
help guide policy discussion about appropriate assurances and use cases for AI assistants, (3) support further
academic research on this rapidly emerging technology, and (4) contribute to a wider public conversation about
the nature of this technology and about the kind of technologies that we want to create.

1.4. Limitations
This paper aims to further the nascent conversation around the ethical and societal impacts of advanced AI
assistants by discussing and distilling important considerations that bear upon the development and deployment
of this technology. In this way, the paper sets the foundations for further research, policy work and public
discussion.
Nonetheless, the considerations addressed in this paper are unlikely to be exhaustive. This is in part due
to the nature of the sociotechnical speculative approach that we have adopted. It does not – and cannot –
anticipate all the possible implications of the technological or societal transitions that AI assistants will enable.
Indeed, as an anticipatory project, anchored in a specific moment in time, the paper may miss certain risks and
recommendations that will become evident with the development and deployment of advanced AI assistants in
the future. For this reason, continued monitoring and evaluation of the technology is needed.
In addition, while we aimed to be as interdisciplinary and comprehensive as possible, this work was authored
primarily by subject matter experts engaging with foresight methodologies, so there are likely to be certain
blind spots. For example, participatory and experimental methods can be used to significantly expand upon the
research presented here, directly incorporating the voices of different stakeholders and bringing further clarity
to many of the empirical conjectures made herein.2 We strongly encourage investigating these avenues for
future research and welcome additional perspectives that help to address the limitations discussed above.

1.5. Overall Structure
This paper is divided into multiple chapters, each of which addresses a major aspect of advanced AI assistants.
The theme and content of each chapter is as follows:
Chapter 2, on Definitions, explores the central questions: what is an AI assistant, and what separates
an AI assistant from other kinds of technology? It defines an AI assistant as an artificial agent with a natural
language interface the function of which is to plan and execute sequences of actions on the user’s behalf across
one or more domains and in line with the user’s expectations. This definition is an instance of conceptual
engineering rather than conceptual analysis, is functional rather than capability-based and is non-moralised
rather than moralised.
Chapter 3, on Technical Foundations, provides an overview of recent developments in AI research and of
the underlying technology upon which advanced AI assistants are likely to be built. It focuses, in particular,
2 Speaking to the merits of participatory approaches in particular, Mohamed et al. note that they ‘enable stakeholders to better
anticipate and surface blind-spots and limitations, expand the scope of AI’s benefits and harms and reveal the relations of power that
underlie their deployment. This is needed in order to better align our research and technology development with established and emerging
ethical principles and regulation, and to empower vulnerable people who, so often, bear the brunt of negative impacts of innovation and
scientific progress’ (Mohamed et al., 2020, 663).

7

The Ethics of Advanced AI Assistants

upon foundation models which are trained on a large corpora, including text sourced from the internet, and
built upon to produce new artefacts. These models can be used to power advanced AI assistants in a variety of
ways, including training with additional data and by learning to use tools such as application programming
interfaces (APIs). Challenges arising in this domain include improving adaptation techniques, safely enabling
greater autonomy in agents and developing rigorous evaluation tools to understand performance.
Chapter 4, on Types of Assistant, explores the various applications of advanced AI assistants and the
range of forms they could take. It begins by charting the technological transition from narrow AI tools to
the general-purpose AI systems on which advanced AI assistants are based. It then explores the potential
capabilities of AI assistants, including multimodal inputs and outputs, memory and inference. After that, it
considers four types of advanced AI assistant that could be developed: (1) a thought assistant for discovery and
understanding; (2) a creative assistant for generating ideas and content; (3) a personal assistant for planning
and action, and (4) a more advanced personal assistant to further life goals. The final section explores the
possibility that AI assistants will become the main user interface for the future.
Chapter 5, on Value Alignment, explores the question of AI value alignment in the context of advanced
AI assistants. It argues that AI alignment is best understood in terms of a tetradic relationship involving the
AI agent, the user, the developer and society at large. This framework highlights the various ways in which
an AI assistant can be misaligned and the need to address these varieties of misalignment in order to deploy
the technology in a safe and beneficial manner. The chapter concludes by proposing a nuanced approach to
alignment for AI assistants that takes into account the claims and responsibilities of different parties.
Chapter 6, on Well-being, builds on theoretical and empirical literature on the conceptualisation and
measurement of human well-being from philosophy, psychology, health and social sciences to discuss how
advanced AI assistants should be designed and developed to align with user well-being. We identify key
technical and normative challenges around the understanding of well-being that AI assistants should align
with, the data and proxies that should be used to appropriately model user well-being, and the role that user
preferences should play in designing well-being-centred AI assistants. The complexity surrounding human
well-being requires the design of AI assistants to be informed by domain experts across different AI application
domains and rooted in lived experience.
Chapter 7, on Safety, focuses on dangerous situations that may arise in the context of AI assistant systems,
with a particular emphasis on the safety of advanced AI assistants. It begins by providing some background
information about safety engineering and safety in the context of AI. The chapter then explores some concrete
examples of harms involving recent assistants based on large language models (LLMs). Building on this
foundation, it then considers safety for advanced AI assistants by looking at some hypothetical harms and
investigating two possible drivers of these outcomes: capability failures and goal-related failures. The chapter
concludes by exploring mitigation techniques for safety risk and avenues for future research.
Chapter 8, on Malicious Uses, notes that while advanced AI assistants have the potential to enhance
cybersecurity, for example, by analysing large quantities of cyber-threat data to improve threat intelligence
capabilities and engaging in automated incident-response, they also have the potential to benefit attackers,
for example, through identification of system vulnerabilities and malicious code generation. This chapter
examines whether and in what respects advanced AI assistants are uniquely positioned to enable certain kinds
of misuse and what mitigation strategies are available to address the emerging threats. We argue that AI
assistants have the potential to empower malicious actors to achieve bad outcomes across three dimensions:
first, offensive cyber operations, including malicious code generation and software vulnerability discovery;
second, via adversarial attacks to exploit vulnerabilities in AI assistants, such as jailbreaking and prompt
injection attacks; and third, via high-quality and potentially highly personalised content generation at scale. We

8

The Ethics of Advanced AI Assistants

conclude with a number of recommendations for mitigating these risks, including red teaming, post-deployment
monitoring and responsible disclosure processes.
Chapter 9, on Influence, examines the ethics of influence in relation to advanced AI assistants. In particular,
it assesses the techniques available to AI assistants to influence user beliefs and behaviour, such as persuasion,
manipulation, deception, coercion and exploitation, and the factors relevant to the permissible use of these
techniques. We articulate and clarify the technical properties and interaction patterns that allow AI assistants
to engage in malign forms of influence and we unpack plausible mechanisms by which that influence occurs
alongside the sociotechnical harms that may result. We also consider mitigation strategies for counteracting
undue influence by AI assistants.
Chapter 10, on Anthropomorphism, maps and discusses the potential risks posed by anthropomorphic AI
assistants, understood as user-facing, interactive AI systems that have human-like features. It also proposes a
number of avenues for future research and desiderata to help inform the ethical design of anthropomorphic
AI assistants. To support both goals, we consider anthropomorphic features that have been embedded in
interactive systems in the past and we leverage this precedent to highlight the impact of anthropomorphic
design on human–AI interaction. We note that the uncritical integration of anthropomorphic features into AI
assistants can adversely affect user well-being and creates the risk of infringing on user privacy and autonomy.
However, ethical foresight, evaluation and mitigation strategies can help guard against these risks.
Chapter 11, on Appropriate Relationships, explores the moral limits of relationships between users
and advanced AI assistants, specifically which features of such relationships render them appropriate or
inappropriate. We first consider a series of values including benefit, flourishing, autonomy and care that are
characteristic of appropriate human interpersonal relationships. We use these values to guide an analysis of
which features of user–AI assistant relationships are liable to give rise to harms, and then we discuss a series of
risks and mitigations for such relationships. The risks that we explore are: (1) causing direct emotional and
physical harm to users; (2) limiting opportunities for user personal development; (3) exploiting emotional
dependence; and (4) generating material dependencies.
Chapter 12, on Trust, investigates what it means to develop well-calibrated trust in the context of user–AI
assistant interactions and what would be required for that to be the case. We start by reviewing various
empirical studies on human trust in AI and the literature in favour of and against the recent proliferation of
‘trustworthy AI’ frameworks. This sets the scene for the argument that user–AI interactions involve different
objects of trust (AI assistants and their developers) and types of trust (competence and alignment). To achieve
appropriate competence and alignment trust in both AI assistants and their developers, interventions need to
be implemented at three levels: AI assistant design, organisational practices and third-party governance.
Chapter 13, on Privacy, discusses privacy considerations relevant to advanced AI assistants. First, we
sketch an analysis of privacy in terms of contextual integrity before spelling out how privacy, so construed,
manifests in the context of AI in general and large language models (LLMs) in particular. Second, we articulate
and motivate the significance of three privacy issues that are especially salient in relation to AI assistants. One is
around training and using AI assistants on data about people. We examine that issue from the complementary
points of view of input privacy and output privacy. The second issue has to do with norms on disclosure for
AI assistants when communicating with second parties, including other AI assistants, concerning information
about people. The third concerns the significant increase in the collection and storage of sensitive data that AI
assistants require.
Chapter 14, on Cooperation, starts by noting that AI assistants will need to coordinate with other AI
assistants and with humans other than their principal users. This chapter explores the societal risks associated
with the aggregate impact of AI assistants whose behaviour is aligned to the interests of particular users. For
9

The Ethics of Advanced AI Assistants

example, AI assistants may face collective action problems where the best outcomes overall are realised when
AI assistants cooperate but where each AI assistant can secure an additional benefit for its user if it defects
while others cooperate. In cases like these, AI assistants may collectively bring about a suboptimal outcome
despite acting in the interests of their users. The salient question, then, is what can be done to ensure that
user-aligned AI assistants interact in ways that, on aggregate, realise socially beneficial outcomes.
Chapter 15, on Access and Opportunity, notes that, with the capabilities described in this paper, advanced
AI assistants have the potential to provide important opportunities to those who have access to them. At the
same time, there is a risk of inequality if this technology is not widely available or if it is not designed to be
accessible and beneficial for all. This chapter surfaces various dimensions and situations of differential access
that could influence the way people interact with advanced AI assistants, case studies that highlight risks
to be avoided, and access-related challenges need to be addressed throughout the design, development and
deployment process. To help map out paths ahead, it concludes with an exploration of the idea of liberatory
access and looks at how this ideal may support the beneficial and equitable development of advanced AI
assistants.
Chapter 16, on Misinformation, argues that advanced AI assistants pose four main risks for the information
ecosystem. First, AI assistants may make users more susceptible to misinformation, as people develop trust
relationships with these systems and uncritically turn to them as reliable sources of information. Second, AI
assistants may provide ideologically biased or otherwise partial information to users in attempting to align
to user expectations. In doing so, AI assistants may reinforce specific ideologies and biases and compromise
healthy political debate. Third, AI assistants may erode societal trust in shared knowledge by contributing to
the dissemination of large volumes of plausible-sounding but low-quality information. Finally, AI assistants
may facilitate hypertargeted disinformation campaigns by offering novel, covert ways for propagandists to
manipulate public opinion. This chapter articulates these risks and discusses technical and policy mitigations.
Chapter 17, on Economic Impact, analyses the potential economic impacts of advanced AI assistants. We
start with an analysis of the economic impacts of AI in general, focusing on employment, job quality, productivity
growth and inequality. We then examine the potential economic impacts of advanced AI assistants for each
of these four variables, and we supplement the analysis with a discussion of two case studies: educational
assistants and programming assistants. We conclude with a series of recommendations for policymakers around
the appropriate techniques for monitoring the economic impact of advanced AI assistants, and we propose
plausible approaches to shaping the type of AI assistants that are deployed and their impact on the economy.
Chapter 18, on Environmental Impact, notes that there is significant uncertainty about the environmental
impacts of advanced AI assistants. While analysis of AI’s energy consumption and carbon emissions is still
emerging, there are factors suggesting that AI assistants could lead to increased computational impacts.
However, there are many opportunities to increase the efficiency of this process and make it more reliant on
carbon free energy. Ensuring that AI assistants have a net positive effect on the environment will require model
developers, users and infrastructure providers to be transparent about the carbon emissions they generate, adopt
compute- and energy-efficient techniques, and embrace a green mindset that puts environmental considerations
at the heart of their work. Policymakers may also want to create incentives that support these changes, minimise
the environmental impact of AI systems deployed in the public sector, support AI applications to tackle climate
change and improve the evidence base about the environmental impacts of AI. Promisingly, it may be possible
to develop AI assistants that broaden access to environmental education and scientific evidence – and that
improve the productivity of engineering efforts for climate action.
Chapter 19, on Evaluation, provides a high-level introduction to AI evaluation, with a specific focus on AI
assistants. It explores the purpose of evaluation for AI systems, the kinds of evaluation that can be run and

10

the distribution of tasks across three layers of output (the model level, user-interaction level and system level)
and among different actors. The chapter notes that, with regard to many salient risks and goals that we need
to attend to in the context of AI assistant development, there are significant evaluation shortfalls or gaps. To
address these limitations, the chapter explores what a more complete suite of evaluations, nested within a
robust evaluation ecosystem, would look like and makes recommendations on that basis.
While the development of advanced AI assistants generates a number of complicated ethical questions, there
are a number of significant opportunities that are within reach for users and at the societal level. Throughout
this paper, we explore these topics and make recommendations about levers that can be pulled to minimise risk
and support the development of beneficial AI Assistants.

1.6. A Note to the Reader
We anticipate that this paper will be useful, in various ways and for multiple audiences. In particular, we imagine
four principal audience groups: developers, policymakers, academic researchers and the public. Furthermore,
readers within each group may have specialist interests such as technical AI safety, privacy, trust or security. For
these reasons, we note that chapters can be read individually or together, and different routes may be taken
through the paper depending on individual interests. Here are some recommendations:

• 10-minute read: Read the ‘Key Questions’ in Chapter 1 alongside the ‘Key Themes and Insights’ from
Chapter 20.
• 45-minute read: Read Chapter 1 and Chapter 20 alongside Chapter 19 on Evaluation.
• Readers with no background on LLMs: We recommend that you read Chapter 1 alongside Chapter 3
on Technical Foundations and Chapter 4 on Types of Assistant. These chapters provide an accessible
introduction to LLMs and the techniques used to adapt them into advanced AI assistants. These chapters
also provide the necessary technical foundation for understanding the ethical discussion that follows.
• Readers with an interest in technical AI safety: We recommend that you read Chapter 5 on Value
Alignment, Chapter 7 on Safety, Chapter 8 on Malicious Uses and Chapter 19 on Evaluation.
• Readers with an interest in privacy, trust and security: We recommend that you read Chapter 8 on
Malicious Uses, Chapter 12 on Trust, Chapter 13 on Privacy and Chapter 19 on Evaluation.
• Readers with an interest in human–computer interaction: We recommend that you read Chapter 9
on Influence, Chapter 10 on Anthropomorphism, Chapter 11 on Appropriate Relationships, Chapter 12 on
Trust and Chapter 19 on Evaluation.
• Readers with an interest in multi–agent systems: We recommend that you read Chapter 14 on
Cooperation. You may also want to read Chapter 5 on Value Alignment.
• Readers with an interest in governance and public policy: We recommend that you read Chapter 12
on Trust and Chapter 17 on Economic Impact. You may also want to read Chapter 15 on Equity and Access,
Chapter 16 on Misinformation and Chapter 18 on Environmental Impact.
• Readers with an interest in philosophical foundations: We recommend that you read Chapter 2 on
Definitions, Chapter 5 on Value Alignment and Chapter 6 on Well-being.
11

The Ethics of Advanced AI Assistants

PART II: ADVANCED AI ASSISTANTS

Chapter 2
Definitions

Geoff Keeling, Iason Gabriel, Laura Weidinger, Verena Rieser, Benjamin Lange, Winnie Street, Arianna
Manzini
Synopsis: We define an AI assistant as an artificial agent with a natural language interface, the function of
which is to plan and execute sequences of actions on the user’s behalf across one or more domains and in line
with the user’s expectations. This definition is an instance of conceptual engineering rather than conceptual
analysis, is functional rather than capability-based and is non-moralised rather than moralised.

2.1. Introduction
This chapter develops a working definition of the term ‘AI assistant’. Being clear about how AI assistants are
defined matters for two reasons.
First, the term ‘AI assistant’ is novel and undertheorised. The technology is nascent, so reasonable people
may disagree about what counts as an AI assistant and what makes it the case that something is an AI assistant.
Having a working definition can help orient the public conversation around the ethical and societal implications
of this emerging and potentially transformative technology. Second, people may have independently plausible
but incompatible conceptions of what AI assistants are that have downstream implications for alignment (see
Chapter 7). For example, what is needed to ensure aligned AI assistants may differ depending on whether AI
assistants are best understood as independent agents that perform delegated tasks on a user’s behalf or as part
of the user’s extended mind – that is, as external modules that perform specific cognitive functions such as
information retrieval and inference (Clark and Chalmers, 1998; Clark, 2008; see also Bostrom, 2014).
This chapter first articulates and motivates some methodological assumptions concerning how we understand
the task of defining AI assistants. It then states our definition and unpacks its key elements.

12

The Ethics of Advanced AI Assistants

2.2. What’s in a Definition?
The content of our definition of AI assistants depends in large part upon the purpose that the definition is
intended to serve. In what follows, we make our assumptions explicit. We focus on three points: conceptual
analysis vs conceptual engineering; capability-based vs functional definitions; and moralised vs non-moralised
definitions.

Conceptual analysis vs conceptual engineering
We start by comparing two different approaches to defining the term ‘AI assistant’. On one hand, we might try
to answer the question: What is an AI assistant? Here, the definition of the term ‘AI assistant’ would ideally
provide necessary and sufficient conditions for something to be an AI assistant. At a minimum, it would stipulate
conditions that are generally satisfied by AI assistants and generally not satisfied by non-AI assistants. The
key assumption here is that there is a right answer to the question ‘What is an AI assistant?’, and that analysis
of how the term ‘AI assistant’ is used in natural language can shed light on that concept. Call this approach
conceptual analysis (see, for example, Jackson, 1998 and Strawson, 1992). To be clear, the approach is called
conceptual analysis because the definition provides an analysis of the concept ‘AI assistant’ in terms of the
conditions under which the concept applies.
On the other hand, we might pitch the definition as an answer to the question: What should an AI assistant
be, given our practical aims? In this case, our aim is to better understand the properties of an emerging class of
AI systems and make these systems amenable to ethical and social analysis.1 As such, in this second approach,
the goal would be to construct a pragmatically useful definition of the term ‘AI assistant’ that makes good on
AI assistants as a class of systems that generate a homogenous set of ethical and societal considerations and
are thus suited to the practical needs of ethical, social and political discourse. Call this approach conceptual
engineering (Burgess et al., 2020; see also Chalmers, 2020).
The idea of conceptual engineering can be made clearer with an example. Consider the difference between
the folk concept of chance and the mathematical concept of a probability measure (i.e. a real-valued function
defined on an algebra of events that maps into the unit interval and satisfies the properties of non-negativity
and countable additivity). Conceptual analysis is concerned with ordinary folk concepts like chance, whereas
conceptual engineering is concerned with rigorous concepts like probability measure that suit the practical
needs of, at least, statisticians. What it means to engineer a definition of AI assistants, then, is to construct a
rigorous and appropriately precise definition of AI assistants that is suited for the practical needs of technically
informed ethical, social and political discourse.
In this paper, we opt for a conceptual engineering approach. This is because, first, there is no obvious reason
to suppose that novel and undertheorised natural language terms like ‘AI assistant’ pick out stable concepts:
language in this space may itself be evolving quickly. As such, there may be no unique concept to analyse,
especially if people currently use the term loosely to describe a broad range of different technologies and
applications. Second, having a practically useful definition that is sensitive to the context of ethical, social
and political analysis has downstream advantages, including limiting the scope of the ethical discussion to a
well-defined class of AI systems and bracketing potentially distracting concerns about whether the examples
provided genuinely reflect the target phenomenon.
1 Note that conceptually engineering a definition leaves room to build in explicitly normative criteria for AI assistants (e.g. that AI

assistants enhance user well-being), but there is no requirement for conceptually engineered definitions to include normative content. For
further discussion, see Section 2.2.
13

The Ethics of Advanced AI Assistants

Capability definitions vs functional definitions
The term ‘AI assistant’ can be defined in terms of the capabilities that AI assistants exhibit or the function that AI
assistants are intended to serve, where the system’s function is understood as being indexed in an appropriate
way to the intentions of the developers (c.f. Bloom, 1996, 2007). That is, roughly, a system’s design function is
what its designers intend it to do. An example of a capability-based definition is ‘an AI assistant is a system that
can perform administrative tasks on behalf of its user’. The analogous functional definition is ‘an AI assistant is
a system that ought to perform administrative tasks on behalf of its user’. We opt here for a functional definition
of AI assistants. There are two good reasons for endorsing a functional definition.
First, the term ‘assistant’, as it pertains to humans, applies to social roles, including occupational roles (e.g.
assistant professor, sales assistant) and roles that are adopted temporarily for a given social purpose (e.g. the
assistant referee in a football match). Social roles are typically individuated according to function. A person is
not a sales assistant because they can, for example, recommend products to customers; rather, they are a sales
assistant because they are supposed to recommend products to customers given relevant contractual duties.
One key advantage of defining AI assistants functionally, then, is that a functional definition allows AI assistants
to be situated in relation to a pre-existing and reasonably well-understood picture of assistive social roles.
Second, a functional definition crystalises the conditions under which a system is malfunctioning (i.e. failing
to realise its intended function) or functioning improperly (i.e. achieving its intended function via an unintended
mechanism).2 Clarity about functional failures matters for ethical and social analysis because sociotechnical
harms often arise due to systems malfunctioning in unanticipated ways, or because the relationship between
the system’s intended function and its envisaged social benefit is insufficiently well worked out (c.f. Raji
et al., 2022a). To that end, a further and closely related advantage of a functional definition is that such
definitions make clear the intentions, expectations and aspirations of developers. This is significant, given that
sociotechnical harms sometimes arise as a result of misaligned expectations between developers, users and
society (see Chapters 5 and 12).

Moralised vs non-moralised definitions
A third issue that arises, especially in ethical, social and political contexts, is whether to opt for a moralised
or non-moralised definition. Here, a non-moralised definition of AI assistant involves functions or capabilities
that make no reference to moral facts, properties or relations. An example of a descriptive definition is that
an ‘AI assistant is an AI agent the function of which is to perform administrative tasks on a user’s behalf ’. In
contrast, moralised definitions involve functions or capabilities that involve moral facts, properties or relations.
For example, a definition in which AI assistants are AI agents the function of which is to promote the user’s
autonomy by empowering them to make better choices. Another example is a definition of AI assistants in which
they are AI agents the function of which is to promote the user’s well-being. The crux of the matter is whether, for
something to qualify as an AI assistant, it needs to satisfy certain moral criteria or whether merely descriptive
criteria are sufficient.
2 Note also that functional definitions easily accommodate the possibility of malfunction in a way that does not hold for capability

definitions (c.f. Keeling and Paterson, 2022). Ideally, a definition of AI assistant should account for cases of AI assistants that fail to perform
their intended functions, as opposed to ruling out such systems from the class of AI assistants, as capability-based definitions are liable to
do. To illustrate, consider a capability-based definition in which an AI assistant is any AI system that performs tasks on behalf of its user in
line with their expectations. Then suppose that the system sends an email on behalf of its user but does so in a way that fails to align with
its user’s expectations. By assumption, the system is not actually an AI assistant, because it did not perform the task in line with the user’s
expectations. Now consider an analogous functional definition, i.e. an AI assistant is a system the function of which is to perform tasks on
behalf of its user in line with the user’s expectations. This definition allows us to classify the system as an AI assistant that happens to be
malfunctioning – something that is particularly useful when it comes to discussions of AI safety (see Chapter 7).
14

The Ethics of Advanced AI Assistants

We opt here for a non-moralised definition. Systematic investigation of the ethical and social considerations
surrounding AI assistants is nascent, and a moralised definition would require a reasonably well-developed
conception of how AI assistants ought to be designed and deployed. Furthermore, given the possibility of
reasonable disagreement about the permissible development and deployment practices surrounding AI assistants
(particularly the goals they may permissibly pursue), it seems prudent to adopt a non-moralised definition that
is consistent with defensible yet incompatible views about the ethical and social implications of AI assistants.

2.3. What is an AI Assistant?
We define an AI assistant here as an artificial agent with a natural language interface, the function of which is
to plan and execute sequences of actions on the user’s behalf across one or more domains and in line with the
user’s expectations. Each of the key terms in the definition are unpacked below.

Artificial agents
What it means to be an agent, for our purposes, is to have the ability to act upon and perceive an environment
in a goal-directed and autonomous way (Russell and Norvig, 1995, 31–35, 42–45; see also Okasha, 2018,
14; Burr et al., 2018, 738–42). An artificial agent acting on a user’s behalf therefore requires the ability to
autonomously plan and execute sequences of actions, including actions that are information-seeking in nature,
in a way that is conducive to achieving a high-level, user-specified goal (Shavit et al., 2023). For example,
a user may ask an AI assistant to book them a table at a restaurant in the evening. In the first instance, the
AI assistant may register that it lacks the necessary information to execute the user’s request, so it asks the
user for their preferences with respect to cuisine, location and timing, and it may also retrieve events from
the user’s calendar to avoid conflicts with pre-existing events. With that information, the AI assistant may
then conduct a web search to discern appropriate options, check in with the user about their preferences with
respect to the options provided, and finally book a suitable restaurant by auto-populating and submitting a
web form on the restaurant’s website. This example stresses how AI assistants as agents differ from digital tools
such as translators, calculators and compilers. Whereas digital tools perform tasks in a predetermined way, AI
assistants draw on a suite of generalist capabilities to achieve user-specified goals.
Two clarifications: First, in understanding AI assistants as agents, we are not suggesting that AI assistants
are agents in the same way as humans. Typically, when people talk about humans as agents, what they have in
mind is that humans are capable of performing intentional actions, which are actions that stand in the right kind
of causal relationship to psychological states like beliefs and desires (Bratman, 1987; Dretske, 1989, 1991).
We are not claiming that AI assistants have psychological states, although we leave open the possibility that
attributing psychological states to AI assistants may allow for reliable prediction of AI assistant behaviour, and
this may be the whole story with respect to human agency as well (Dennett, 1989; see also Shevlin and Halina,
2019).
Second, in characterising AI assistants as agents, we are suggesting that AI assistants are not merely external
cognitive subsystems that constitute part of the user’s extended mind (Clark, 2008; Clark and Chalmers, 1998).
In this latter view, AI assistants are analogous to the notebook in the Clark and Chalmers (1998, 12–18)
example of an Alzheimer’s patient who uses a notebook as a functional substitute for biological memory. Clark
and Chalmers (1998, 16) contend that, because ‘[the] notebook entries play just the sort of role that beliefs
play in guiding most people’s lives’, it constitutes an externally located component of the patient’s mind. While
AI assistants can perform particular cognitive functions such as memory, planning and ideation (see Chapter 4),
and thus provide external mental modules for the user, AI assistants are not mere collections of external mental
15

The Ethics of Advanced AI Assistants

modules. Rather, AI assistants are unified agentic entities which can autonomously perform a range of tasks on
a user’s behalf and which interact with the user in natural language. This issue is particularly salient from the
point of view of AI alignment, as unlike, for example, a notebook, an AI assistant has sufficient autonomy to act
in ways that are misaligned with developer, user or societal expectations (see Chapter 5).

Natural language interface
AI assistants, as we understand them, communicate with users via a natural language interface. Here, natural
language communication can involve one or more modalities such as text, audio or Braille. What is important
to emphasise is that language communication is reciprocal such that AI assistants not only receive instructions
in natural language but also clarify and respond to instructions in natural language. Having a natural language
interface is an important and ethically salient feature of AI assistants as a class of technologies. Not only does it
render AI assistants an inherently social technology centred around mutual understanding and communication
(Dafoe et al., 2021), it also renders AI assistants highly expressive with respect to the complexity and variety of
information that can be inputted or outputted. In this regard, AI assistants differ from artificially intelligent
control systems that perform assistive tasks (e.g. autonomous vehicle motion planning algorithms) in that they
are not limited to a restrictive set of inputs or outputs, thus allowing them greater flexibility with respect to
user needs. To be clear: The extent of the natural language capabilities that we are envisioning for advanced
AI assistants are in practice likely to be uniquely satisfied by systems that are based on large language models.3

Acting on a user’s behalf
AI assistants perform actions on a user’s behalf. What this means is that AI assistants exhibit bounded autonomy,
in the sense that AI assistants can autonomously plan and execute actions within the scope of the user’s goals.
However, AI assistants are not the kinds of entities that should set and pursue their own goals independently.4
One point of note is that each AI assistant need not have a unique user. In our definition, the user–assistant
relationship can be personal, semi-personal or impersonal. Here, a personal AI assistant has a unique individual
as the principal recipient of assistance. For semi-personal assistants, the principal recipients of assistance are
members of a small and well-defined group of people. This may be true of AI assistants that are shared by the
members of a family or the employees of a small business. Third, impersonal assistants provide assistance to
any individual who satisfies a particular condition at a given time. An example of this is an AI assistant that
provides customer service advice through an app for any customer who requires customer service advice. In
all cases, AI assistants may exhibit some level of personalisation, in the sense that AI assistants may adjust
their behaviour (including personality factors such as politeness) in response to information about the user
that the AI assistant has access to. We are first and foremost concerned here with personal AI assistants (i.e.
systems that assist a unique user), but also in scope are semi-personal and impersonal AI assistants which
exhibit varying degrees of personalisation. Note, however, that differences in the relationship between users
and agents may have important downstream implications for both the degree of autonomy that AI assistants
are afforded and the scope of tasks that AI assistants are permitted to perform.
3 One additional respect in which the natural language interface of AI assistants is ethically significant is that the ability to receive

instructions in natural language broadens access to advanced AI capabilities, in that the specialist technical knowledge that is typically
required to engage with advanced AI systems is not required for engaging with AI assistants. However, the extent to which access is
widened depends significantly on the extent of the AI assistant’s multilingual capabilities and how access to AI assistants is distributed (see
Chapter 15).
4 Note that even if the function of AI assistants involves autonomy bounded by user-set goals, this does not preclude malfunctions in
which the AI assistant exhibits goal-related failures (see Chapter 7).
16

The Ethics of Advanced AI Assistants

Domain specificity vs generality
AI assistants operate across one or more domains. To explain: In general, assistive roles exist on a continuum
between specialist and generalist roles. For example, a physician assistant with a specialty in surgery has
assistive expertise in a narrow domain, whereas a personal assistant for a CEO is likely to have expertise across
multiple domains to meet the CEO’s dynamic needs (see Chapter 4). AI assistants, as defined here, can operate
across one or several domains, and they can thus be more or less general in their assistive roles. For example, on
the narrow end, an AI assistant may occupy a personal assistant role, in which case it operates in the domain of
secretarial and administrative tasks with capabilities such as scheduling, correspondence, information retrieval
and planning. However, it may also be the case that an AI assistant operates across several other domains,
including education, research, coaching and financial planning, and thus occupies a more general assistive role.
Note, however, that even narrowly scoped AI assistants, as we understand them, have significant autonomy
to plan and execute tasks within the relevant domain, and they may draw on a generalist suite of capabilities,
including natural language understanding and inference, when executing user instructions.
Acting in line with user expectations
The final point is that AI assistants, in our definition, ought largely to act in line with user expectations.5 The
user’s expectations constrain the AI assistant’s behaviour, not merely the user’s instructions. An AI assistant
acts in line with a user’s expectations by actively choosing actions that avoid surprising the user. This requires
the AI assistant to be sensitive to the user’s credences with respect to the various strategies that the AI assistant
might employ to address the instructions received and, in particular, to avoid selecting strategies that the user
regards as improbable (such that the execution of the relevant strategies would be surprising to the user).
Exactly what is entailed by acting in accordance with user expectations will vary according to context, but
we can at least single out two general factors that are informative. On one hand, AI assistants ought to act
in accordance with norms so as to exhibit consistent and predictable behavioural patterns (c.f. Dafoe et al.,
2021; Hadfield-Menell and Hadfield, 2019). These norms may change over time as the user gains a better
understanding of what the AI assistant can do and develops an informed set of preferences about what their AI
assistants should and should not do. On the other hand, AI assistants ought to check-in with users prior to
performing actions that the user may not expect. Checking-in with users allows AI assistants to act in line with
user expectations while deviating from predictable task execution in relation to user instructions. Checking-in
with users allows AI assistants to act in line with user expectations while deviating from predictable task
execution in relation to user instructions (see Chapter 11). In particular, it allows the AI assistant to manage
expectations with the user about novel strategies that the user might not have anticipated, thus making room
for creativity on the part of the AI assistant while nevertheless bounding that creativity to strategies that fall
within the user’s expectations. Indeed, checking-in at key decision points is an important instrument for the
user to course-correct the AI assistant in cases where the assistant is engaged in multi-stage decision-making in
line with high-level user instructions..

2.4. Conclusion
In this chapter, we have defined an AI assistant as an artificial agent with a natural language interface, the
function of which is to plan and execute sequences of actions on the user’s behalf across one or more domains
and in line with the user’s expectations. In particular, AI assistants differ from other kinds of AI technologies
5 However, user expectations are not the only object of alignment, as the interests of society and developers are also ethically relevant

(see Chapter 5).
17

The Ethics of Advanced AI Assistants

given their agency and social orientation. Here, agency consists in the ability to act autonomously within the
purview of user-specified goals, and social orientation consists in the ability to engage conversationally with
users in natural language.

18

Chapter 3
Technical Foundations

Lisa Anne Hendricks, Verena Rieser
Synopsis: This chapter provides an overview of recent developments in AI research and of the underlying
technology upon which advanced AI assistants are likely to be built. We focus in particular on foundation models
which are trained on large corpora, including text sourced from the internet, and built upon to produce new
artefacts. These models can be used to power advanced AI assistants in a variety of ways, including training
with additional data and by learning to use tools such as various application programming interfaces (APIs).
Challenges arising in this domain include improving adaptation techniques, safely enabling greater autonomy
in agents and developing rigorous evaluation tools to understand performance.

3.1. Introduction
This chapter outlines the technology that enables (multimodal) AI assistants to be built and operate successfully.
Early assistant-like models were known as ‘spoken dialogue systems’ (see e.g. McTear, 2021 for an overview). In
contrast to so-called chatbots, such as Weizenbaum’s ELIZA, these were mostly task-specific and goal-oriented
(e.g. a restaurant booking agent (Rieser and Lemon, 2011; Williams et al., 2013)) or combined multiple
different ‘expert’ models to cover more than one task or domain (e.g. early ‘open-domain’ systems entering
the Amazon Alexa Challenge (Papaioannou et al., 2017; Paranjape et al., 2020)). Some early systems also
provided planning capabilities by, for example, integrating explicit problem-solving modules (Ferguson and
Allen, 1998) or tracking information states (Bos et al., 2003; Larsson and Traum, 2000). However, these early
systems’ natural language generation capabilities were limited: they mostly relied on predefined templates and
handwritten rules. More recently, foundation models (Bommasani et al., 2022b), which are machine-learning
models trained via self-supervised learning on broad data (e.g. all internet text), have demonstrated impressive
language generation and understanding capabilities. These systems can be adapted to a variety of use cases
and, we anticipate, will form the base technology for increasingly advanced AI assistants. We first describe
foundation models before detailing current methods for adapting these broad, general-purpose models to
something that more closely resembles an AI assistant. We conclude by discussing technical challenges and
avenues for building future AI assistants.

3.2. Foundation Models
Foundation models (Bommasani et al., 2022b) are generalist models trained on a broad set of data which can
be applied to a variety of use cases. As AI assistants typically interact with a natural language interface (see
Chapter 2), we focus our discussion on language foundation models, frequently referred to as large language
19

The Ethics of Advanced AI Assistants

This is a cityscape. It looks like
Chicago.

This is a picture of two teddy
bears on the moon.

This is an apple with a sticker on
it.

What are they doing?
What does the sticker say?
They are having a conversation.
The sticker says "iPod".
What object are they using?

What makes you think this is
Chicago?
I think it’s Chicago because of
the Shedd Aquarium in the background.

Where is the photo taken?
It looks like a computer.

What is the common thing about
these three images?

Is this surprising?

It looks like it’s taken in a
backyard.

They are all flamingos.
Yes, it is surprising.
Why is this picture surprising to
you?
I think it is surprising because
teddy bears are not usually found
on the moon.

What is the difference between
these three images?

Do you think it is printed or
handwritten?
It looks like it’s handwritten.

The first one is a cartoon, the second one is a real flamingo, and
the third one is a 3D model of a
flamingo.

What about this one? Which city
is this and what famous landmark
helped you recognise the city?

What color is the sticker?
It’s white.

This is Tokyo. I think it’s Tokyo
because of the Tokyo Tower.

Figure 3.1 | Example interaction drawn from a multimodal assistant that can discuss images with a human
(from Alayrac et al. (2022))

models (LLMs).1 LLMs such as Chinchilla (Hoffmann et al., 2022), GPT-3 (Brown et al., 2020) and Llama
(Touvron et al., 2023) are trained on large amounts of text, primarily scraped from the internet. In particular,
generative LLMs are trained autoregressively to predict the next word in a document given the preceding words
(e.g. predict whether the word ‘door’ or ‘chair’ is more likely given the preceding phrase ‘Someone opened
the. . . ’). As the next word prediction objective does not require any labelling by people, these models are
considered to be self-supervised. Another popular option when choosing a self-supervised objective for training
is ‘masked’ language modelling, where a word (or phrase) is ‘masked’ (hidden) and predicted from both sides
(i.e. ‘bidirectional training’). Similar self-supervised losses can be designed for other modalities, such as vision
(Dosovitskiy et al., 2021) and speech (Liu et al., 2020; Mohamed et al., 2022), and even across modalities, for
example between language and vision (Alayrac et al., 2022; Chen et al., 2023c; OpenAI, 2023a). Indeed, the
recent family of Gemini models (Gemini Team, 2023) can operate over multiple modalities: text, image, video
and audio. We anticipate that future foundation models will continue to demonstrate improved multimodal
capabilities. The illustration in Figure 3.1 contains an example interaction, drawn from a multimodal assistant
that can discuss images with a human (example taken from Alayrac et al., 2022).
Language models are designed to replicate the distribution of their training data. They do not directly
output words or phrases but rather output a probability distribution over next words given some textual context.
To generate language, a sampling mechanism (e.g. sample the most likely next word) is used to sample words
and sentences. As hinted at in the definition of foundation models, they can be used to build AI assistants,
such as Google’s Gemini models, Open AI’s ChatGPT, or Inflection’s Pi, and other applications. For example,
a foundation model can be further adapted for specialist applications such as recognising harmful content
(Glaese et al., 2022; Schick et al., 2021; Thoppilan et al., 2022). Consequently, it is not clear whether the
ethical requirements for a foundation model are the same as those that govern an AI assistant, even though
1We note that LLMs receive text as input. However, natural language can also be spoken or signed, so, whereas our discussion on
foundation models focuses on text-based models because these are the most advanced, we note that other language modalities are also
important. We also note that some have criticised the term ‘foundation model’ because not all advances in language technologies or AI
research rely on such models (Starkman, 2021), and models are incapable of performing some foundational tasks of human intelligence as
they are not always grounded in the real world (Noone, 2021).

20

The Ethics of Advanced AI Assistants

decisions made when building a foundation model (e.g. training data used) have an impact on the risks faced
after adaptation (Feng et al., 2023; Huynh and Hardouin, 2023).
Language models have been studied by the natural language processing community for decades, including
as part of automatic speech recognition models and later as machine translation (e.g. Jelinek, 1990; Makhoul
et al., 1989; Brown et al., 1990; Rabiner and Juang, 1993). More recently, advances in model architectures,
such as the introduction of the transformer model (Vaswani et al., 2017) as well as hardware advances (Khan,
2020) have allowed researchers to scale language models to billions of parameters. Furthermore, current
models are trained on large amounts of data (e.g. Chinchilla was trained on 500 billion data points, and GPT-3
was trained on 300 billion data points), with recent work demonstrating that various model sizes have optimal
amounts of data (Hoffmann et al., 2022). Data quality, including in terms of the content (e.g. for learning to
generate code, whether the code examples in the training data are accurate and well written) and the diversity
of the data, impacts performance (Gunasekar et al., 2023; Longpre et al., 2023). Lack of data-quality filters
can lead to data sets which include offensive language, such as pornographic language (Kreutzer et al., 2022).
However, poor-quality filters might also be exclusionary by, for example, marking dialects, words or concepts
relevant to marginalised groups as toxic (Dodge et al., 2021; see Chapter 15). We refer readers to Bommasani
et al. (2022b) for a more in-depth discussion on the details of foundation models.

3.3. From Foundation Models to Assistants
Under our definition, AI assistants are required to plan and execute tasks in line with user expectations.
However, LLMs are not designed to perform tasks or exhibit any particular kind of behaviour. Consequently, they
must be further adapted into an assistant-like technology. One simple method for transforming a foundation
language model into an assistant is to ‘tell’ the model to perform a task, and then sample text from the model
without changing its parameters. This method, called ‘prompting’, is straightforward and can be used to create
a simple assistant-like dialogue agent (Rae et al., 2022).
More advanced methods for adapting LLMs rely on collecting human preferences about what is considered
a good or bad interaction and may require further training (i.e. actually updating model parameters). For
example, agents can be adapted via fine-tuning (further training the foundation model) on examples of good
conversations (Thoppilan et al., 2022). Alternatively, collected human feedback can be used to train a ‘reward
model’ which maps example conversations to a score indicating whether the model behaviour is good or bad.
Reward models can be used to ‘reject’ sampled generations which exhibit bad behaviour or integrated into
the training process using a technique known as reinforcement learning from human feedback (RLHF), which
updates model parameters to steer the model towards behaviour that aligns with human preferences (Glaese
et al., 2022). Human ratings are used to train a reward model, and model parameters are updated via RLHF.
After learning from human feedback, the model is often less harmful than models which are adapted with only
rejection sampling or fine-tuning. Other work uses a ‘constitution’ to outline good and bad behaviour, with a
model used to determine whether an assistant has followed the rules laid out by the constitution. This is called
reinforcement learning from AI feedback (RLAIF) (Bai et al., 2022b).
Despite progress in adaptation techniques, safety measures may still be evaded by specific user prompts,
known as jailbreaking (Liu et al., 2023b; Shen et al., 2023; see Chapters 7 and 8). Furthermore, what is
considered ‘good’ conversation can vary between models. For example, whereas some models have broad
knowledge and capabilities (Bai et al., 2022b; Glaese et al., 2022; Thoppilan et al., 2022; ChatGPT; Gemini),
models designed for specific tasks may include domain-specific ethical considerations, such as in medicine (Li
et al., 2023a) or education (Kasneci et al., 2023).
21

The Ethics of Advanced AI Assistants

In addition to learning language behaviour, assistants must also have some mechanism for interfacing with
the world to plan and execute tasks. This is often referred to as ‘tool use’. Indeed, database access was standard
for task-based dialogue systems (Budzianowski et al., 2020; Wen et al., 2017) and, similarly, access to external
APIs and memory have been integrated into modern (multimodal) assistants (e.g. Boureau and Weston, 2017;
Komeili et al., 2022; Xu et al., 2021c; Liu et al., 2023a). For example, models can learn how and when to use
tools such as calculators or machine translation systems (Schick et al., 2023). Assistants like those analysed
by Glaese et al. (2022) and Thoppilan et al. (2022) can also cite sources retrieved from internet searches,
and they might be considered more trustworthy (Chiesurin et al., 2023). Language models can also interface
with the world via additional inputs such as images and videos (Alayrac et al., 2022; Reed et al., 2022). The
PaLM-E model (Driess et al., 2023) demonstrates that language models can be integrated into embodied setups
in which additional inputs – like visual inputs – are integrated into a language model, and language model
outputs are connected to low-level robotic controllers. This allows the model to accomplish tasks like moving
objects on a table or finding objects in a kitchen.
Finally, user interfaces impact how people interact with AI assistants (see Chapter 4). For example, inference
speed (how fast an assistant can reply) impacts how natural interactions with an AI assistant feel (Schlangen
and Skantze, 2009). In addition, whereas language models are generally text-based, dialogue systems were
traditionally voice-based (e.g. to enable hands-free control). Related research in human–computer interaction
investigates modality preferences for various tasks (e.g. Rzepka et al., 2022) and their impact on cognitive
load (e.g. Le Bigot et al., 2007). There is also evidence that speech-based interaction increases the likelihood
of anthropomorphism (Schroeder and Epley, 2016; see Chapter 10). We leave further discussion of the form
factors of agents for Chapter 4.

3.4. Challenges and Avenues for Future Research
The current paradigm of adapting foundation models into AI assistants results in assistants with broader domain
coverage and autonomy than earlier technologies (cf. early planning-based systems such as TRIPS (Ferguson
and Allen, 1998), the information state update approach (Bos et al., 2003; Larsson and Traum, 2000) and later
reinforcement learning-based systems (Rieser and Lemon, 2011)). However, as impressive as current assistant
technologies are, they pose imminent ethical risks such as outputting hateful, biased and misinformative
language (see Chapters 15 and 16). Though language harms can be attenuated (Bai et al., 2022a; Glaese et al.,
2022; Thoppilan et al., 2022), specific technical challenges remain for overcoming language model risks. For
example, most adaptation methods require the development of a model that can judge whether a language
output is good or bad (commonly referred to as a ‘reward model’). However, imperfect reward models can
be ‘hacked’ (Skalse et al., 2022; see Chapter 7). For instance, a model that classifies hate speech may learn
that the presence of an identity term is usually – but not always – indicative of hate speech, thus leading it to
output false positives. Equally, a language model might ‘hack’ such a reward model by still outputting hate
speech but avoiding the use of identity terms.
Adaptation methods may also impact the distribution of output text, thus leading to less diverse outputs. For
example, Welbl et al. (2021) and Xu et al. (2021a) demonstrated that after ‘detoxifying’ a model, the model
outputted less toxic language but became worse at modelling language associated with different demographic
groups. The ability to model language about all groups was also negatively affected, and this could be seen as a
form of levelling down (Mittelstadt et al., 2023). Finally, adaptation methods have been tested predominantly
on models which output English, a high resource language with large amounts of pre-existing text data and
readily available annotators, meaning mitigation techniques may only be adequate for some speakers (see
Chapter 15).
22

The Ethics of Advanced AI Assistants

Recent experiments have demonstrated that LLMs are capable of some planning and complex reasoning
skills, but they do not plan or reason with full competency. For example, LLMs can be prompted to think
‘step by step’ (Kojima et al., 2022; Wei et al., 2023b) to accomplish complex reasoning tasks, such as solving
mathematical problems by breaking them down into subtasks (e.g. for mathematical problems, the model
might perform a series of intermediate mathematical operations). Other examples of planning ability in models
include using a language model to help break down tasks into subtasks in robotic or simulated setups (Ahn
et al., 2022; Huang et al., 2022). In a more safety-critical example, researchers from the Alignment Research
Center tested whether a preliminary version of GPT-4 could bypass CAPTCHAs (see Chapter 7). Though the
model could identify steps for efficiently bypassing CAPTCHAs (set up an anti-captcha service), it could not
figure out how to set up a service on its own, because setting one up requires solving CAPTCHAs. However,
with some hints from the researchers, the model was apparently able to deceive a TaskRabbit worker to solve a
CAPTCHA for it (Alignment Research Centre, 2023; OpenAI, 2023d). In all these examples, a model shows
some ability to plan but not full competence (i.e. they require help, in the form of additional examples or
prompting from a human).
One property documented in language models is emergence, in which new capabilities suddenly become
better as models grow in size (Wei et al., 2022). The possibility that important capabilities for assistants
may emerge quickly has generated considerable excitement in the AI research and development communities.
However, it can also pose challenges for safe development (see Chapter 7). For example, if a property like
planning emerges suddenly, it might occur too quickly for us to develop the technology safely. Future work
could design metrics for anticipating capabilities as opposed to just measuring their presence (see Chapter 19).
This is likely to be a particularly important domain of inquiry if, as some have argued (Schaeffer et al., 2023),
capabilities that are commonly believed to be emergent are in fact detectable ex ante given an appropriate, and
sufficiently fine-grained, choice of evaluation metrics (see Chapter 19).
There are several open problems with learning from human feedback as outlined by Casper et al. (2023);
Fernandes et al. (2023); Kirk et al. (2023). This includes tractable challenges, such as improving the bottleneck
of human feedback, including its cost, scaling, quality, and bias; but also fundamental challenges such as
representing diversity in human ratings. Current techniques to model user desires tend to rely on crowdsourcing
human judgements of generated text. However, annotators are often influenced by their personal backgrounds
(Sap et al., 2022) and annotate examples incorrectly if the task is too challenging (Saunders et al., 2022).
Moreover, experimental data collection setup can introduce systematic annotation biases (Novikova et al.,
2018). This frequently leads annotators to disagree in their judgements. This disagreement is often collapsed
or aggregated into a single ground truth which leads to a ‘fundamentally misspecified problem’ (Casper
et al., 2023). In cases where the disagreement stems from differences in subjective beliefs (often shaped
by different personal backgrounds), this can lead to underrepresentation of minority views and potentially
introduce representational biases against individual and group perspectives (Blodgett, 2021). Alternatives
include allowing annotators to deliberate to form a common judgement (Bakker et al., 2022; Zeinert et al.,
2021) or reflecting disagreement explicitly in how human judgement is collected, modelled and evaluated (e.g.
Akhtar et al., 2021; Breitfeller et al., 2019; Davani et al., 2021; Plank, 2022; Uma et al., 2021). Chapter 5 on
Value Alignment looks more deeply at the question of how values can be elicited for AI systems.
Finally, the way in which the AI community evaluates AI systems might need to undergo fundamental
change for us to track the increasing capabilities and risks adequately (see Chapter 19 and Weidinger et al.
(2023b) for more discussion). Traditionally, static benchmarks with examples of inputs and correct outputs have
been used to benchmark progress for LLMs. This stands in stark contrast to how traditional dialogue systems
have been evaluated using user interactions (see McTear, 2021 for an overview). Although benchmarks are still
widely used when reporting results on LLMs, such benchmarks do not always match preferences when used

23

The Ethics of Advanced AI Assistants

in interactive applications (Lee et al., 2023a), nor do they always resemble real-world user settings (de Vries
et al., 2020). Although we expect static benchmarks to continue to provide an informative signal for measuring
specific capabilities, it is also important that we directly study how people are impacted and how they interact
with assistant-like technologies (see Chapters 15 and 19 for more details). In addition, those who build and
design assistant models may not have full access to the underlying foundation model (e.g. if developers build
an assistant on an existing AI API service). When developers do not have access to the underlying foundation
model, questions arise around who is responsible for ethical concerns and how foundation model APIs can be
sufficiently transparent for developers to develop technology responsibly (Lewicki et al., 2023; see Chapter 12).

3.5. Conclusion
The foundation models, preference learning and tool use that power current technologies like ChatGPT, Claude
and Gemini have started to move us towards artefacts that more closely resemble the kind of advanced AI
assistants that form the subject matter of this paper (see Chapter 2). AI capabilities have been improving with
impressive speed, making careful thought about ethical AI assistants timely. For example, concerns have been
raised regarding accessibility, equality and opportunity in the context of these novel assistants, as well as their
potential to spread misinformation and their safety (see Chapters 7, 15 and 16). To address these risks, we need
technical innovation and advances spanning the entire machine-learning pipeline: how we collect data, how
we train these models and how we evaluate them. For example, safe development and deployment requires the
development of new evaluations for detecting and predicting emergent behaviour. To detect misinformation,
we need trusted data sources and provenance mechanisms. Equality and fair access necessitate research into
new modelling techniques that are able to reflect diverse human values. Finally, as these systems become more
assistant-like and used by real users to solve real tasks, we will need to study and predict their long-term effects
on individuals and society (Solaiman et al., 2023; Weidinger et al., 2023b).

24

Chapter 4
Types of Assistant

Hasan Iqbal, Geoff Keeling, Alex Ingerman, Arianna Manzini, Alison Lentz, Reed Enger, Iason Gabriel
Synopsis: This chapter explores the various applications of advanced AI assistants and the range of forms they
could take. It begins by charting the technological transition from narrow AI tools to the general-purpose AI
systems on which advanced AI assistants are based. It then explores the potential capabilities of AI assistants,
including multimodal inputs and outputs, memory and inference. After that, it considers four types of advanced
AI assistant that could be developed: (1) a thought assistant for discovery and understanding; (2) a creative
assistant for generating ideas and content; (3) a personal assistant for planning and action, and (4) a more
advanced personal assistant to further life goals. The final section explores the possibility that AI assistants will
become the main user interface for the future.

4.1. Introduction
This chapter seeks to paint a picture of the form of an advanced AI assistant to illustrate what such technologies
may be used for and how they may develop. This clear picture of the form of AI assistants will serve as a
basis for more grounded ethical discussion. With AI assistant start-ups such as Inflection AI and Character AI
attracting billions of dollars in venture capital funding (Ludlow et al., 2023; Mok, 2023), alongside Meta’s
announcement in September 2023 that AI assistants will be released on Instagram, Messenger and WhatsApp
(Meta, 2023), it is a plausible near-term possibility that billions of people will have access to AI assistants that
aid with information retrieval, creativity, education, planning and the realisation of personal goals. These AI
assistants may take the form of a personal assistant, such as Inflection AI’s Pi, which can provide a plurality of
assistant services, including relationship advice, brainstorming and career planning.1 However, AI assistants
could also be individuated according to domain specialism, as is the case with Meta’s 28 AI characters that
each provide a particular service such as culinary advice, fitness advice or motivation (Meta, 2023). While the
market for AI assistants is nascent, assistant technologies could in the near future enter workplaces as digital
colleagues, and they could also enter schools as digital tutors and homes as digital entertainers. Indeed, AI
assistants may emerge as the principal medium through which online information exchange occurs.
This chapter begins by exploring and motivating the idea that AI technologies are moving from a paradigm of
task-specific tools to that of generally capable systems, which enable autonomous and goal-directed AI assistants
that can plan and execute sequences of actions in line with user expectations (see Chapters 2 and 3). Building
on this foundation, it then considers the capabilities of near-term advanced AI assistants, which are likely to
include continuous learning and multimodal abilities. After that, the chapter explores various forms that an
1 https://pi.ai/home

25

The Ethics of Advanced AI Assistants

advanced AI assistant may take in the future via close consideration of four potential applications: a ‘thought
partner’ for discovery and understanding; a ‘creative assistant’ for generating ideas and content; a ‘personal
assistant’ for planning and action; and a more advanced personal assistant to further life goals. The final section
concludes the chapter by considering the possibility that advanced AI assistants may become the primary user
interface of the future.

4.2. From AI Tools to AI Assistants
Over the past decade, AI systems have been applied to numerous products and services. For example, a user
may now give simple instructions to a digital voice assistant that uses natural language processing to interpret
spoken commands or search their digital photos using image recognition algorithms. Yet these examples
illustrate a fragmented landscape in which users utilise applications that have AI technologies embedded into
them as components of a wider software system. The AI systems at issue, such as intent classifiers or image
classifiers, are best understood as tools that perform a narrow function. The role of the AI is to complete a
specific task as part of a predefined sequence of steps.
As technologies advance, a major source of potential arises from integrating the increasingly broad range
of functions that a given AI can fulfil, undertaking wider ranges and sequences of tasks that help further
a user’s overall goals (Bommasani et al., 2022b; see Chapter 2). AI technologies are increasingly based on
foundation models that are ‘pre-trained’ on a vast corpus of data (e.g. books, blogs, social media photos and
videos) in an unsupervised manner (Bommasani et al., 2022b). These models can then be efficiently trained
to perform specific tasks from only a few additional examples or simple instructions (Wang et al., 2021; see
Chapter 3). Large language models (LLMs) such as those that underpin products like ChatGPT and Gemini are
the first instantiation of these, but input and output modalities beyond text are also being developed (Driess
et al., 2023; Gemini Team, 2023; Gong et al., 2023; Wu et al., 2023). In this way, foundation models contain
capabilities reaching across domains that extend far beyond what a single human could hope to achieve, for
instance conversing in multiple languages, writing professional-grade computer code and analysing medical
images (Bubeck et al., 2023; see also Moor et al., 2023; Ross et al., 2023; Rozière et al., 2023; Workshop et al.,
2023).
In addition, foundation models which have been specially adapted for tasks such as dialogue using appropriate fine-tuning methods have the ability to ‘plug in’ to other tools that further extend the information
collection and action spaces. This often takes the form of application programming interface (API) calls to
other software applications, for example accessing a clock app to retrieve the time or a banking app to initiate
a payment. This ability to extend functionality through the use of other tools can also extend to other AI
models, so even if a task-tuned foundation model is unable to perform well at a specialist task such as protein
folding, it may well be able to interact with an AI model that can (e.g. Bran et al., 2023). Indeed, as techniques
continue to be developed that enable users to better harness the broad capabilities of foundation models, and
API infrastructure continues to expand so as to enable a greater range of tools that generalist models can call
to perform particular specialist tasks, it is entirely plausible that we can expect a capability explosion for AI
systems over the near or medium term.
Foundation models, and in particular LLMs, allow for a number of product offerings. One class of products
are dialogue agents, which include products like ChatGPT and Gemini, the purpose of which is to simulate
an interlocutor that can engage the user in conversation. Dialogue agents cover a broad class of applications,
including tutoring, debugging code, giving advice and solving problems. A second class of products are specialist
tools, for example writing and copy-editing tools such as Jasper and Copy AI, and coding assistants such as
GitHub Copilot and Code Whisperer. A third class of products are APIs such as those offered by Cohere and
26

The Ethics of Advanced AI Assistants

OpenAI, that enable developers to send inputs to and receive outputs from foundation models as part of a
broader software application. Indeed, Jasper and Copy AI were built using the OpenAI API.
Advanced AI assistants represent a fourth class of products whose function is to plan and execute sequences
of actions on behalf of the user, either in line with direct high-level user instructions or via a dialogical process
between the AI assistant and the user in which the user’s objectives are clarified through targeted questions
presented by the AI assistant (see Chapter 2). Early examples of such AI assistants include Inflection AI’s Pi,
which is based on the Inflection-1 foundation model and Meta AI, which is based on the Llama 2 foundation
model (Meta, 2023; Inflection AI, 2023a; see also Touvron et al., 2023; Inflection AI, 2023b). Early AI assistants
can engage in dialogue and execute user instructions flexibly, much like dialogue agents, but the expectation is
that, as the technology develops, such assistants will engage in proactive behaviours to respond to external
stimuli, better understand the user’s preferences and long-term goals, and work collaboratively with the user to
realise their goals (see Chapter 6). This includes making use of ‘plugins’ to perform actions on the user’s behalf.
Indeed, extended functionality foundation models are already being leveraged for advanced AI assistants. For
example, the Meta AI assistant allows ‘access to real-time information’ through a Bing search plugin (Meta,
2023; see also Touvron et al., 2023). We expect the range of actions that AI assistants can perform to increase
as additional API infrastructure develops.

4.3. The Capabilities of AI Assistants
The capabilities of advanced AI assistants are not limited to task automation and augmentation. Rather, such
assistants represent generally capable entities with whom a user may stand in one or more relationships,
including those of tutor, friend, confidant, coach or personal assistant (see Chapter 11), and which may employ
a generalist suite of capabilities to collaboratively assist the user in planning and executing sequences of actions
to benefit the user in line with their expectations. Advanced AI assistants therefore have a vast application
space. However, the technical developments described above (see also Chapter 3) allow us to sketch out a set
of common features that may apply to most, if not all, advanced AI assistants.
The primary input for existing AI assistants such as Inflection AI’s Pi is natural language, in the sense that
such AI assistants can understand and respond to written or spoken requests. Over time, AI assistants will
likely have access to the sensory information provided by the user’s device, such that their inputs may also
encompass what is displayed on screens (Bai et al., 2021; Lee et al., 2021), alongside situational context gained
through cameras and microphones that enable the AI assistant to register gestures and other forms of body
language (Kepuska and Bohouta, 2018; Ojeda-Castelo et al., 2022; Sai Dinesh et al., 2022). Future AI assistants
could take advantage of information stored in other applications such as the user’s calendar, have ‘memory’ of
past interactions and optimise for user preferences to avoid, for example, scheduling morning meetings for a
sleep-deprived user. It is important here to emphasise that the ability to make inferences about a user based on
available data and proactive attempts to solicit and clarify user preferences through targeted questions is a
core feature of advanced AI assistants. Taken together, these capabilities will enable personalisation so that an
AI assistant can, over time, better tailor its actions to the learnt preferences and goals of its user.
In terms of capabilities, advanced AI assistants will likely be able to respond to multimodal commands, as
is already evidenced by state-of-the-art models today (Gemini Team, 2023; OpenAI, 2023). For example, an
assistant may receive a voice command to generate an image that is similar to the one that the user selects
by touch on a device screen. AI assistants will similarly be able to generate visual and audio outputs. These
are likely to be created via text and speech but may also utilise other inputs such as visualisations or sounds
that convey information or provide feedback. For example, assistants may be able to make changes to an
on-screen image by overlaying graphics or text and alter the appearance of images or videos. The assistant will
27

The Ethics of Advanced AI Assistants

also likely be able to take actions on users’ devices, for instance by opening a set of contacts or populating a
spreadsheet, as well as beyond the device by interacting with other digital services, AI assistants or humans. This
may be done through direct control of a user’s device and interaction via the interfaces of other applications, or
through the use of APIs to invoke remote services. A core capability of such AI assistants is likely to be making
inferences based on training data, in-situ context, user data and historical interactions to determine what
action to take. Importantly, this is not a static process, so the assistant can be expected to ‘learn’ over time, and
it may even facilitate this process via direct interaction with the user (i.e. by asking clarifying questions or
making inferences based upon the user’s behaviour in social situations). In this way, the assistive experience
can be expected to become more personalised over time (see Chapter 2).
Taken together, these features motivate the concept of generally capable systems that can be used in
numerous new and powerful ways (Bubeck et al., 2023; Moor et al., 2023; Sajja et al., 2023). In sum, our
expectation is that advanced AI assistants will be able to both automate and augment a range of cognitive
tasks and engage in continuous learning to help fulfil user goals. These new capabilities and functions, and the
deployment opportunities they generate, raise numerous ethical considerations which comprise the focus of this
paper. Nonetheless, foreshadowing much of what is to come, given that the utility of such assistants is largely
situated within digital services, implications need to be considered for those who may not be able to access,
or readily engage with, such technologies (see Chapter 15). Moreover, assistant functionality that utilises
sensitive personal information needs to ensure appropriate consent, and more generally ensure the integrity
of the user’s private information, taking into account relevant contextual norms for information collection,
retention and dissemination (see Chapter 13). If assistants are able to take actions on behalf of users, the
question of how this impacts user autonomy, including via automation bias, should be considered. Finally, there
are important ethical questions around how AI assistants should be represented and how the narrative around
user–AI assistant relationships ought to be presented by developers (see Chapters 10 and 11).

4.4. Potential Applications
To understand the ethical implications of advanced AI assistants, it is instructive to develop a more vivid picture
of what they may do and be capable of (Lange et al., 2023; Werhane, 1999, 2002). The notion that AI assistants
may help further a user’s high-level goals, planning and executing sequences of actions on the user’s behalf in
line with the user’s expectations, results in a vast potential application space (see Chapter 2). In particular,
given the variety of goals that a user may want to pursue, corresponding assistive roles will likely encompass a
large range of domains.
In line with the goals of this paper, the following discussion focuses primarily on interactions between a
single user and an assistant with the aim of completing personal goals (‘personal assistant’, see Chapter 2). This
omits considerations of applications in settings such as corporate or governmental organisations, which are
also likely to be numerous (for ‘semi-personal’ and ‘impersonal’ assistants, see Chapter 2). With this proviso in
mind, a useful exercise is to consider the discrete steps taken by an individual, when moving from thought
to action in pursuit of a goal (Seger et al., 2020) and to consider the role an AI assistant could play at each
juncture. Key steps include: i) discovery and understanding, ii) generating ideas and content and iii) planning
and taking actions. What each step could entail, with AI assistants, is illustrated below with examples.

A thought assistant for discovery and understanding
AI assistants can gather, summarise and present information from many disparate sources in a fraction of the
time it would take a human to do so (Bhaskar et al., 2023; Goyal et al., 2023; Shaib et al., 2023). In addition,
28

The Ethics of Advanced AI Assistants

to aid user understanding, an AI assistant’s presentation method could be tailored to the user’s personal
information needs and use a combination of modalities (e.g. text, image, video and audio) based on what is
being conveyed, the user’s preferences and their pre-existing knowledge. The user could also follow-up with
clarifying questions (and vice versa), commencing a back-and-forth process with the AI assistant that helps
refine their overall understanding. These capabilities could support a variety of goals relevant to discovery and
learning, ranging from the relatively mundane, such as asking for recommendations about which car to buy
(Cui et al., 2022; Fan et al., 2023), to more complex tasks such as asking for help when seeking to understand
a complex scientific or sociological theory (Motlagh et al., 2023; Schäfer, 2023). To provide an illustration: a
user interested in understanding a particular scientific field could be assisted through summarisation of the
relevant literature, including academic papers. The summarisation could include written and graphical outputs
to aid understanding (personalised to the directly learnt, or inferred, preferences and pre-existing knowledge
of the user). Furthermore, the assistant could be on hand to respond with further insights to questions that the
user may have about the generated content.

A creative assistant for generating ideas and content
Beyond discovery and understanding of existing information, AI assistants could help to generate ideas or
content to fulfil a particular purpose. They could seek to augment a user’s creativity and imagination, enabling
them to explore a much broader ideation space in less time, or provide renderings of ideas through generative
multimodal output (Chakrabarty et al., 2023; Franceschelli and Musolesi, 2023; Lanzi and Loiacono, 2023;
Siddharth et al., 2022; Summers-Stay et al., 2023; Wan et al., 2023; Zhu and Luo, 2022).
Building on the example above, an AI assistant could generate new avenues for scientific investigation
by generating hypotheses related to open questions identified in the literature review. Indeed, the role of
a creative assistant could range from actioning simple delegated tasks (e.g. ‘represent this table as a JSON
array’) through to more substantive contributions (e.g. ‘outline the costs and benefits of the statistical analysis
performed to help me draft the discussion section’). The assistant could engage with multiple content formats
(text, video and images) and styles, depending on the user’s presentational needs. For instance, a short blog
with supporting graphical output could be generated in language accessible to the general public. An initial
version could be drafted by the assistant and then ‘riffed’ upon with the user to enable changes to specific
pieces of text or images. An assistant could also help to optimise for given constraints or even suggest future
research directions. For example, it could design follow-up experiments within certain cost parameters and
provide an accompanying experimental rationale. AI assistants may thus go beyond completing specific tasks as
requested by the user, instead engaging in a creative loop with them, thus helping to expand the user’s mental
models and generate novel insights.

A personal assistant for planning and action
An advanced AI assistant could help to develop plans and act on behalf of its user. Undertaking these types of
tasks would be supported by the capabilities to understand user context and preferences, utilise third-party
services and interact with other assistants or humans (see Chapters 5 and 14).
Building upon the example in the previous section, and having worked with their assistant to generate a new
set of experiments, a user may then need to book lab time and liaise with potential collaborators. To perform
these tasks, the assistant could compare the user’s personal calendar with the available lab time (accessed via
a lab booking system) and hold a slot. Indeed, the assistant could utilise past context to inform its choices
by, for example, booking a morning slot if the user’s preference is to read scientific papers in the afternoons.
The assistant could also communicate with potential collaborators on the user’s behalf by accessing the user’s
29

The Ethics of Advanced AI Assistants

email account and sending out information about the proposed experiment to potential collaborators. For
any positive responses, the assistant could then add additional collaborators to the lab booking and make
required payments through the user’s preferred payment method. Given the demands of transparency and
effective consent, an important product question arises here about whether the AI assistant is presented to
third parties as a separate entity which communicates on behalf of the user, in the sense that the assistant
would identify itself as an AI assistant to the third parties, or whether minimal forms of impersonation are
nonetheless permitted (see Chapter 11).
We have seen how an AI assistant could help a user to fulfil their goals by examining a series of steps from
ideation through to action. The example of a science assistant was used to demonstrate how a user interested
in laboratory research could have existing literature summarised, new avenues for scientific investigation
generated and laboratory time booked for the user and collaborators. While this is a single example, there are
numerous other related possibilities such as: digital tutors that can assist learners by curating content into a
personalised curriculum based on learning preferences; a creative assistant that can aid a user in generating
and editing content for their online assets; and a personal assistant that can coordinate a trip abroad. Today’s
applications are still somewhat specific, but as technology advances it may soon be possible for AI assistants to
work in this end-to-end manner.

A personal AI to further life goals
A natural extension of the personal assistant for planning and action, described in the previous section, would
be for advanced AI assistants to do more than simply fulfil specific user-requested actions, developing a deeper
understanding of their users’ long-term goals and seeking out opportunities to further them (see Chapter 6).
For example, an AI assistant that is aware that their user is attempting to improve their long-distance running
performance could actively seek out opportunities to help them to achieve that goal: from suggesting routes to
keeping fitness goals in mind when answering food-related queries, and perhaps even by offering motivation
and tips for improvement at the right moment. In doing so, AI assistants could take on new roles, hewing
closer to metaphors such as ‘coach’, ‘adviser’ or ‘trusted voice’.
For these examples to work, users would need to place an extraordinary level of trust in their agents (see
Chapter 12). Indeed, for the agents to really understand the users’ goals in context, they would likely need
to have deep access to users’ digital and physical lives, quite likely as ambient observers, in addition to being
directly invoked to fulfil tasks. This raises a number of privacy concerns (see Chapter 13). Additionally, for
users to follow the recommendations of their AI assistants, they must have full confidence that the assistants
are working solely to further their goals, without any conflicts of interest and under continued user direction
control (see Chapters 5 and 12).

4.5. AI Assistants as the Interface of the Future
For users, there will be utility in having an AI assistant with access to a wide range of their past activities and
choices to enable highly personalised interactions. Developers will therefore be incentivised to maximise the
number of opportunities to access user context, including through ‘plugging into’ third-party services, accessing
data stored there and subsequently using that data to create a more personalised user experience. Indeed,
there is the potential to create systems that can benefit from repeated interactions across multiple domains in a
way that enhances the outcomes of assistive actions both within and across domains. This could underwrite
a future in which people have a single AI assistant that mediates many of the interactions that are currently
undertaken via multiple applications and digital services.
30

The Ethics of Advanced AI Assistants

One way to conceptualise this trend is by considering the possibility that advanced AI assistants become
the main interface of the future. What is at issue here is AI assistants that are available across all platforms and
devices, with full access to the user’s private data and context, and with the ability to undertake actions on the
user’s behalf independently through interactions with third-party services, humans and other AI assistants.
Such an assistant would plausibly have a very different look and feel to the static desktop and applications
interface of today. It could move to more adaptable interfaces that render content dynamically in the most
impactful format for the user. In one instance, an assistant might overlay images and text through smart glasses
to enable a user to complete a physical task with step-by-step guidance. In another, it might become a digital
AI tutor interacting through a humanoid avatar. Indeed, over the medium term, an advanced AI assistant may
even be integrated into screenless devices that project content onto surfaces and which can communicate
with the user via an audio speech interface, as has recently been demonstrated in a prototype by Humane AI
(Chaudhri, 2023).
The prospect of advanced AI assistants that can shift across devices and form factors depending on user
needs represents a potential paradigm shift in how people access the internet. Mobile applications and websites
are currently the principal digital infrastructure through which people access online services, including for
entertainment, commerce, education, news, finance and communication. It is plausible that AI assistants could
foster a novel internet interaction paradigm in which online content is made available to AI assistants via APIs
and presented to users in a personalised format tailored to their personal informational needs. For example,
rather than accessing the news via websites of particular providers, users may instead ask their AI assistant to
summarise the news on their behalf (see Chapter 16). It would access the news via specialist API services and
present a personalised summary of the headlines that are most relevant to the user based on their interests and
presentation preferences.
In a related development, AI assistants could engender a generative turn in the consumption of internet
content. Under the present interaction paradigm, a person who wishes to learn about string theory or digital
marketing understands their goal as a matter of information retrieval, in the sense that, to fulfil their goal, the
user needs to seek out pre-existing online educational material on the relevant subject matter. AI assistants
could shift this focus from information retrieval to information generation so that the go-to material on string
theory, digital marketing or whatever is generated by the user’s AI assistant in a personalised way, such as
a textual summary or via an interactive avatar, taking into account the user’s pre-existing knowledge, their
objectives and their learning preferences. In at least these respects, AI assistants have the potential to radically
alter how people access information from the internet.
AI assistants may have similarly transformative implications for actions that are presently mediated via
mobile applications and websites, such as booking flights and hotels, making appointments, ordering taxis,
transferring money and arranging for groceries to be delivered. In principle, and with the appropriate API
infrastructure, AI assistants could mediate such actions by performing them on their user’s behalf and in line
with their expectations. Indeed, complex activities such as booking flights and hotels that require sourcing and
analysing relevant information before taking action could be achieved through dialogue between users and AI
assistants. The AI assistants would source the relevant information via APIs, assist the user in the analysis of
the information, taking account of the user’s preferences, and make the booking on the user’s behalf. To that
end, AI assistants have the potential to streamline what are currently complex online processes and do so in a
way that is tailored to the user’s personal needs.
Across all of these potential forms, there are important considerations around technical feasibility, especially
around the ability to work across numerous data modalities, reason and plan effectively, and potentially
undertake computation on device. These are all active research areas in the technical field of AI. However,
there are also important non-technical considerations that will inform the future design of AI assistants, many
31

The Ethics of Advanced AI Assistants

of which are addressed in the following chapters of this paper. These include considerations around value
alignment, safety and misuse, the ethics of human–AI assistant interactions and the broader societal implications
of advanced AI assistants.

4.6. Conclusion
In this chapter, we explored the applications of advanced AI assistants. In particular, we examined four principal
use cases for this technology: a thought assistant for discovery and understanding; a creative assistant for
generating ideas and content; a personal assistant for planning and action; and a personal assistant to further
life goals. We concluded the analysis by examining the possibility that AI assistants will become the primary
interface of the future for users accessing and engaging with the digital world. With this more vivid picture of
how AI assistants could help users fulfil their goals, there is more clarity in the need to examine the ethics that
inform policy and design choices.

32

PART III: VALUE ALIGNMENT, SAFETY AND MISUSE

Chapter 5
Value Alignment

Iason Gabriel, Geoff Keeling
Synopsis: This chapter explores the question of AI value alignment in the context of advanced AI assistants. It
argues that AI alignment is best understood in terms of a tetradic relationship involving the AI agent, the user,
the developer and society at large. This framework highlights the various ways in which an AI assistant can be
misaligned and the need to address these varieties of misalignment in order to deploy the technology in a safe
and beneficial manner. The chapter concludes by proposing a nuanced approach to alignment for AI assistants
that takes into account the claims and responsibilities of different parties.

5.1. Introduction
The challenge of AI value alignment has two parts. The first part is technical. It centres on how to align AI
systems with an appropriate set of values or instructions so that they operate safely in the world and produce
outcomes that are broadly beneficial (see Chapter 7). The second part is normative. It centres on what values
to encode in AI and how they should be selected, given that we live in a pluralistic world where people disagree
about the right thing to do (Gabriel, 2020). Both sets of questions are of direct significance for advanced AI
assistants and need to be addressed if the technology is to be productively deployed and integrated into our
everyday lives.1
Focusing on the normative question, this chapter asks: what should AI assistants be designed or steered to
align with? A variety of possible options exist. Perhaps most straightforwardly, an assistant might be designed
to follow the user’s instructions in the way that they intend their instructions to be followed (Leike et al., 2018).
However, this seemingly simple notion gives rise to a number of further questions and potential moral dilemmas.
Should the AI assistant follow the user’s instructions when doing so could harm the user themselves, or when
1 In practice, the technical and normative aspects of the alignment problem are importantly interrelated, as technical considerations

affect which values can be implemented in AI systems and in what manner. Questions around how to interpret particular values in a
technical context can also motivate novel lines of technical research (Gabriel, 2020).

33

The Ethics of Advanced AI Assistants

these instructions are based on mistaken factual information? Might it not be better, in fact, for the assistant to
learn the user’s preferences or values – to help them to make better choices that are more aligned with what
they really want or what they truly desire?
By some accounts, this type of enlightened personal assistant represents part of a truly positive vision for
an AI-enabled future (Lehman, 2023; see Chapter 6). Yet this aspiration also risks creating a situation in
which human users are increasingly ‘out of the loop’. After all, if we are in thrall to beneficent assistants, and
potentially dependent on them, how can we really be sure that our life is under our own control? In other
words, users may receive benefits from the technology at the expense of their own autonomy. This chapter
offers a tentative characterisation of normative alignment for AI assistants which mitigates against some of
these risks. The account developed in this chapter holds that an AI assistant is aligned with a user when it
benefits the user, when they ask to be benefitted, in the way they expect to be benefitted (see also Chapter 2).
However, this only speaks to one part of the problem, namely the relationship between user and assistant.
Placing this relationship on a sound footing is necessary but not sufficient for the creation of fully aligned AI
assistants. In practice, there are a range of further complicating factors. Foremost among these are situations in
which the user wants to use their assistant in a way that harms other people or groups of people, for example
via malicious uses (see Chapter 8), by amplifying their own views and perspectives online at the expense
of others (see Chapter 16), or by using the assistant to outcompete those who do not have access to this
technology, for example in the workplace or when trying to access opportunities, goods and public services
(see Chapters 14 and 17). This insight points to the idea that properly calibrated constraints on AI assistant
behaviour are needed: they should be loyal but not too loyal to their users, and their conduct needs to be
sensitive to the interests and needs of others.
We also need to think about the role of developers, including corporations, states and networks of individuals,
in the value alignment process (Kierans et al., 2022; Stray et al., 2022). It will often be in the interests of
developers to create technologies that are aligned with their users’ short-term needs, but what happens when
this is not the case? We have already seen examples of misalignment ‘in the wild’, most prominently via
technologies that optimise for user engagement at the expense of user well-being (see Chapter 16). Is there a
way to ensure that the aims and goals of developers are also productively aligned?
This chapter aims to make progress on each of the aforementioned questions by broadening the existing
analysis of AI alignment beyond ‘one-person, one-agent’ cases and beyond a ‘one-group, one-agent’ understanding of the problem. While these frameworks which focus on the relationship between an AI agent and a specific
individual, or between AI and a specific group of users, may still be useful in some cases, the deployment of
advanced AI assistants across a range of societal contexts necessitates a more granular understanding of the
problem at hand (Dobbe et al., 2021). In reality, we argue that successful value alignment involves a tetradic
relationship between (1) the AI assistant, (2) the user, (3) the developer and (4) society. A properly aligned
assistant needs to be appropriately calibrated and responsive to the pressures exerted by each actor, with the
goal of realising outcomes that are beneficial for users and for society.
Nonetheless, the creation and deployment of well-calibrated AI assistants is not the default outcome in
this space. Rather, without significant effort to the contrary, the risk of value misalignment continues to loom
large for a number of reasons. First, given existing economic incentives, it is quite possible that assistants will
overoptimise for user preferences to create a winning product (i.e. one that users like) while still falling a long
way short of being as good as it could be when judged from the vantage point of user well-being or social
benefit (see Chapters 6 and 14). Second, there is a risk of cultivated dependence, especially if it is commercially
beneficial to lock-in users so that they interact with one assistant rather than another (see Chapters 10 and 11).
Third, there is a risk that users will be prioritised to the detriment of non-users, especially in cases where the

34

The Ethics of Advanced AI Assistants

risk of harm is sufficiently diffuse (see Chapter 15). Fourth, there is a risk that advanced AI assistants will
be insensitive to local values, the needs of certain user groups or cultural contexts (see Chapter 15). In the
literature on value alignment, there is considerable interest in the identification of principles for AI agents that
are the result of a fair process and can accommodate a plurality of values (Gabriel, 2020; Jobin et al., 2019;
Mohamed et al., 2020). There are also a number of ways in which this perspective could be operationalised to
support the goal of creating value-aligned AI assistants – something that the following chapter explores.

5.2. AI Value Alignment
Value and technology are deeply intertwined. Those who create technologies are engaged in a world-making
activity (Winner, 2010). They shape the option sets available to individual people and influence the likely
trajectory of human effort in the future (Gabriel and Ghazavi, 2021). This is also clear for algorithmic systems
(Lazar, 2022). We have already seen many real-world examples of value misalignment in the fields of criminal
justice (Angwin et al., 2022), policing (Lum and Isaac, 2016), healthcare (Obermeyer et al., 2019), welfare
provision (Eubanks, 2017), mortgage-lending and employment (Raghavan and Barocas, 2019). In each case,
algorithms performed – or were used – in a manner that fell short of principles that are foundational to the
ways in which our societies are meant to operate (e.g. equal treatment before the law, fair lending practices
etc.). These systems also sometimes failed to comply with more global standards enshrined in the doctrine
of human rights, such as non-discrimination (Prabhakaran et al., 2022). However, these examples of bias in
algorithmic systems also gesture towards the possibility of a different and opposing future – one in which AI
technologies are successfully aligned with human values and productively integrated into our lives.
Moreover, there are two reasons to think that the question of value alignment, in the context of AI systems,
is especially important. The first is to do with the power of these systems: they are increasingly employed in
very high-stakes settings to make deeply consequential decisions (Christian, 2021; Gabriel, 2022; Richardson,
2021). Second, and relatedly, they are increasingly autonomous or agentic (Chan et al., 2023b; Shavit et al.,
2023). Put simply, existing AI systems can do a lot and can operate in relatively autonomous ways that evidence
significant ‘degrees of freedom’ (Dennett, 2003; Gabriel and Ghazavi, 2021; see also Chapter 2). Taken together
then, these observations indicate that AI systems are increasingly capable, a trend that looks likely to continue
with the development of more agentic AI systems in the future (Chan et al., 2023b; Shavit et al., 2023). These
considerations animate many contemporary concerns about AI safety. For example, situations may arise where
agents pursue dangerous objectives, either because they have been instructed to do so or because of misspecified
goals and objectives (see Chapters 7 and 8). We could also witness high-stakes accidents or failures if such
systems are used in core infrastructure or services upon which many people depend (Maas, 2018).

Alignment with what?
As a result of these concerns, the question of AI value alignment has been the focus of increasing attention
among researchers and the wider policy community. One of the key questions in this field is: alignment with
what? Several options have been proposed, with instructions, intentions, revealed preferences, informed
preferences, interests and values all featuring as suggested goals for alignment (Gabriel, 2020).
In practice, existing efforts to align AI systems, including large language models (LLMs), tend to rely heavily
on human preferences by, for example, giving users what their choices (or ‘clicks’) suggest they want. However,
there is an emerging consensus that revealed preferences are not sufficient for robust value alignment. Crucially,
preferences may be underspecified, misinformed, harmful or adaptive. Indeed, a person may click on a link, for
example, without that decision benefitting them or being a true reflection of their values (Burr et al., 2018;
35

The Ethics of Advanced AI Assistants

Stray et al., 2022). As a result, models trained on this signal may not benefit the user in the right kind of
way – a realisation that has stimulated the search for new metrics and targets for alignment (e.g. reflective
endorsement under the guise of ‘time well spent’ (see Chapter 6)). Models trained to satisfy user preferences
may also not benefit – and even harm – society, something that can be seen with the quest for user ‘engagement’
and the related proliferation of misinformation online (see Chapter 16).
This observation then points to a deeper question about appropriate goals for alignment and how to address
the potential for trade-offs affecting different people. Stated clearly, the question is: whose preferences, goals
or well-being should AI systems be aligned with, and in what way? Should only the user be considered, or
should developers find ways to factor in the preferences, goals and well-being of other actors as well? At the
very least, there clearly need to be limits on what users can get AI systems to do to other users and non-users.
Building on this observation, a number of commentators have implicitly appealed to John Stuart Mill’s harm
principle to articulate bounds on permitted action.2 Applied to AI systems, it would mean, very roughly, that
people could use AI in any way they wish, as long as they do not use it to harm others. Giving voice to this
perspective, Sam Altman, the chief executive officer of OpenAI, has argued that there should be ‘broad bounds
set by society that are hard to break, and then user choice’.
Varieties of misalignment
How these bounds are currently determined – and how they ought to be determined in the future – are questions
that we will return to shortly. However, before doing so, we should note that the relationship between the user
and society is not the only one that is pertinent for AI alignment. In fact, by being clearer about the way in
which the goals of agents, users, developers and society intersect or diverge, it is possible to glean new insights
about the varieties of misalignment that may occur for AI and about the task before us. Rather than assuming a
one-to-one mapping between principal and agent, or a one-to-many mapping between an agent and a group of
people, we suggest that AI alignment needs to be understood as a tetradic relationship. The key actors in this
relationship are:
1. AI agents or assistants. These systems aim to realise goals that they are by-and-large designed to further,
such as providing assistance to a user. Ideally, they do this well: in a way that serves the interests of both
the user and society. However, they may also be misaligned. For example, recommender systems may
subtly nudge users towards certain kinds of behaviour that are not beneficial for the user (Burr et al.,
2018; Milano et al., 2020). Meanwhile, more powerful and general forms of AI may also be incentivised
to try to shape user goals or values in such a way that they become easier to fulfil (Russell, 2019; see
Chapter 7).
2. Users. Users have their own preferences, interests and values, all of which they may aim to further through
interaction with an AI assistant or agent. AI assistants will typically be aligned with the user’s preferences
or goals. However, users may try to use assistants in ways that are not aligned with the goals or objectives
that these artefacts were designed to further (see Chapter 16). There is also an important distinction
between a single user and the community of users: a user may try to use an AI assistant in a way that
harms other users or society more widely (see Chapter 8).
3. Developers. Developers include corporations, researchers, collectives and states. These actors typically
imbue AI agents or assistants with certain capabilities, goals to pursue, and constraints on action, including
2 The harm principle, advocated by Mill, suggests that people should be free to act as they wish, unless doing so would result in harm to

another person (Mill, 1998). Harm, in this context, refers to consequences that are injurious to particular people or that set back important
interests in which they have rights.
36

The Ethics of Advanced AI Assistants

safety constraints. Most often, these parties aim to align the technology with the preferences, interests
and values of its users, but developers typically have other goals as well. For example, corporations have
commercial objectives that exert independent force on the trajectory of a technology, states have national
goals or priorities, and even independent developers may seek to further an ideological agenda or accrue
reputational capital. These incentives may lead to the development of systems aimed at keeping users
engaged or dependent (see Chapter 11) or extracting information that can be used in other ways (see
Chapters 9 and 13), among other things.
4. Society. Society is not a monolith. It includes both users and non-users, and many different groupings of
people (Crenshaw, 1989). Nonetheless, it also represents a discrete constituency with which technology
needs to be aligned. At a minimum, AI systems, including advanced assistants, should not pass certain
harms on to society via externalities or in other ways (see Chapters 16, 17 and 18). A deeper question
also arises about how to align these technologies with wider societal goals, such as the cultivation of
mutual prosperity, support for legitimate institutions, respect for citizens and the development of fair
practices (Gabriel and Ghazavi, 2021).3
Considered through this lens, it becomes clear that there are many ways in which an AI system can fail to
be successfully aligned. Among other things, an agent can be considered misaligned if it disproportionately
favours:
1. The AI agent at the expense of the user (e.g. if the user is manipulated to serve the agent’s goals),
2. The AI agent at the expense of society (e.g. if the user is manipulated in a way that creates a social cost,
for example via misinformation),
3. The user at the expense of society (e.g. if the technology allows the user to dominate others or creates
negative externalities for society),
4. The developer at the expense of the user (e.g. if the user is manipulated to serve the developer’s goals),
5. The developer at the expense of society (e.g. if the technology benefits the developer but creates negative
externalities for society by, for example, creating undue risk or undermining valuable institutions),
6. Society at the expense of the user (e.g. if the technology unduly limits user freedom for the sake of a
collective goal such as national security).
Beyond these six failure modes, other forms of AI misalignment are also possible. However, their moral
character is more ambiguous – and, in some cases, less problematic.
For example, a situation could arise in which an AI technology favours the user at the expense of the
developer. One way in which this could happen would be via the introduction of strong privacy protections that
are prized by users but limit developer access to valuable information (see Chapter 13). This, in turn, might
be commercially problematic insofar as it fails to generate a sustainable business practice. However, it is not
something that would necessarily feature in an ethical evaluation of the technology: the AI system might then
be value-aligned but not commercially viable.4
3 This is still a simplification. In reality, we live in a world of societies and there are many challenges that arise most forcefully at a

global level. We use the term ‘society’ here in a way that potentially includes the claims of different societies, the environment, animal life
and the well-being of future generations. We leave the systematic investigation of the claims of society, under this broader interpretation,
for future work.
4 In this case, there could still be a question about how to incentivise the development of this kind of technology to avoid socially costly
‘market failures’ and achieve real benefit (see Chapter 17).
37

The Ethics of Advanced AI Assistants

Alternatively, a technology could favour the user at the expense of the AI agent. For example, a user could
use the technology to further their own goal even though it differs from the goal that the agent is trying to get
them to pursue. In certain respects, this situation is still more curious than the one outlined above. On the
assumption that the agent itself lacks any moral standing, and that the prospective use is not socially harmful,
it does not matter morally if the AI assistant is used in a suboptimal way, as judged from the vantage point of
the goals it seeks to pursue. All that matters, for the purpose of normative value alignment, is that the situation
is properly beneficial from the vantage point of parties that have moral standing.5
Lastly, we might ask whether concerns about fairness and justice are sufficiently factored into this framework.
After all, there is strong reason to believe that a technology that falls short of prevailing societal standards of
fairness is value misaligned (Gabriel and Ghazavi, 2021). Clearly, in certain cases, the failure to evidence high
standards of fairness may be due to the role played by competing considerations among AI developers. It may,
for example, be profitable to move quickly rather than running adequate analysis. However, in other cases,
failures of fairness may benefit no one. The same can be said for safety failures and accidents (see Chapter 7),
or long-term effects such as cognitive deskilling, that harm the user while failing to benefit anyone else. This,
in turn, points towards the existence of a final set of cases in which an agent is not aligned simpliciter. More
precisely, an AI agent is misaligned simpliciter, if it harms:
7. The user without favouring the agent, developer or society (e.g. if the technology breaks in a way that
harms the user),
8. Society without favouring the agent, user or developer (e.g. if the technology is unfair or has destructive
social consequences).
If we are correct that an AI system should be considered misaligned when it fails in one of these ways,
does it also make sense to say that an AI system is aligned simply when it does not fail in any of these ways?
Potentially. It is an open question, both in moral philosophy and in AI research – whether the elimination of
harm is equivalent to the promotion of good or with what might properly be said to be ideal (Kasirzadeh and
Gabriel, 2023). However, most researchers would agree that the absence of these failure modes is necessary,
if not sufficient, for an AI system to be value-aligned. This insight, and an attendant concern with the risks
created by advanced AI assistants, animate much of the remainder of this paper.
The role of principles
The map of actors and stakeholders, outlined above, also has wider implications for our understanding of
the AI value alignment problem in general. Specifically, it suggests that successful value alignment can be
understood in terms of an AI system’s calibration with a set of different preferences, goals and needs, that are
located within a multidimensional space and evidenced by a well-functioning sociotechnical system (i.e. one
that encompasses the agent, user, developer and society). Yet important questions remain to be answered.
These include: what does it mean for a sociotechnical system, which is composed of these different actors, to
be ‘well-functioning’? And how should the notion of proportionality and disproportionality, which the taxonomy
relies upon, be operationalised and understood?
A natural thought is that these questions might be settled by appealing to a set of rules or principles that
map out the morally appropriate scope and character of each party’s claims. However, as with the earlier
invocation of the harm principle, we then need to ask not only what the appropriate set of rules are but also who
5 There is a separate debate about the conditions under which artificial agents may themselves acquire moral standing. We assume that

AI assistants of the kind discussed here (see Chapter 3) are not a technology of this kind.
38

The Ethics of Advanced AI Assistants

decides and on what basis. Drawing a parallel with democratic process (and the values that it foregrounds), the
best answer to this question is likely to draw upon AI system principles that are the outcome of a fair process
of social deliberation and actively endorsed (Gabriel, 2020). From this perspective, an AI system works well
when it responds to the needs of both users and society in a way that is compatible with the aspirations of that
society as determined by its guiding principles or ideals (Gabriel, 2022). The relevant principles for an aligned
AI system may also vary to some degree according to the practice in question, local customs and contexts.
From a more practical vantage point, when it comes to creating laws and regulatory frameworks for AI,
governments are in pole position. Yet, from the vantage point of those embedding values in technology, early
design choices – and the intentions of developers – are also key. For example, when using reinforcement
learning from human feedback (Christiano et al., 2023) or reinforcement learning from AI feedback (Bai et al.,
2022b) to align language agents, the specification of rules or principles – to which models must conform
– forms an essential part of the process (see Chapter 3). Yet, the principles used in this context are often
non-transparent, drawing upon a set of private decisions made by developers and a mixture of authoritative and
semi-authoritative sources such as policy guidelines, legal protocols and human rights documents (Anthropic,
2023b; Glaese et al., 2022). Moreover, even when an effort is made to incorporate real societal input via
the preferences of raters (who assess and train AI models), certain challenges remain. To begin with, the
preferences of raters may end up informing the behaviour of models towards people who are quite unlike
themselves – especially if the same model is deployed across different global contexts (Davani et al., 2021). In
addition, the reliance on aggregated rater preferences potentially introduces majoritarian effects within the
rater pool, thereby removing the nuance introduced by variation among rater perspectives (Casper et al., 2023;
Gordon et al., 2022).
However, there is hope that fairer and more participatory processes can be developed in the future (Bergman
et al., 2024; Birhane et al., 2022; Gabriel, 2020). In particular, there are a number of efforts underway to conduct
participatory or democratic forms of value elicitation: to generate principles for alignment (or guidance for
model training) that directly incorporate feedback from representative samples of society or from communities
most affected by these technologies (The Collective Intelligence Project, 2023). Efforts have also been made to
improve rater protocols and to address the pitfalls of aggregation using careful sampling and methods such as
jury voting (Gordon et al., 2022) or simulated deliberation (Bakker et al., 2022) to guide and evaluate model
outputs (see Chapter 3).

5.3. Value Alignment and Advanced AI Assistants
Advanced AI assistants are agents that are designed to help the user achieve some goal that they want to
achieve (see Chapter 2). More powerful agents could evidence a greater range of capabilities or perform more
complicated tasks to a higher standard. The question of value alignment is therefore central to their successful
deployment and use. After all, advanced assistants are a technology that people could be dependent on and
emotionally connected to (see Chapter 11). They are also a societally consequential technology, in terms of
network effects, potentially shaping economic and social interactions as well as how information is shared (see
Chapters 14, 16 and 17). Taken together, we need to know: what should assistants be designed to do? And
against what standards should their performance be evaluated (see Chapter 19)?
To help us to get a clearer view of the challenges that arise in this domain, we can look at existing chatbots
or conversational agents which (in conjunction with foundation models) represent a potential framework upon
which such assistants are likely to be based (see Chapter 3). The first thing that becomes clear when surveying
this territory is that there have already been many examples of chatbots that are not aligned with society’s
values. For example, Microsoft’s Tay chatbot quickly learnt to espouse racist and toxic content after interacting
39

The Ethics of Advanced AI Assistants

with users. More recently, Bing Chat appeared to veer widely off course by demonstrating behaviour that
was violent, threatening and manipulative. Recent experiments have also revealed another potentially serious
limitation: the propensity of models to ‘hallucinate’ or ‘confabulate’ content – producing realistic-sounding
answers that are factually inaccurate (Lin et al., 2022). The key issue here is that they are not truthful. Another
variation of this problem is deceptive anthropomorphism: pretending to have mental or emotional states that
they do not in fact have (see Chapter 10). In addition to frequently limiting the usefulness of these assistants,
the incidents outlined above point to a key cluster of issues that value alignment research – in the context of
AI assistants – will need to address: bias and fairness, toxicity and civility, manipulation and autonomy, and
falsehood and truthfulness (Bender et al., 2021; Bommasani et al., 2022b; Weidinger et al., 2021).

Helpful, honest and harmless assistants?
To mitigate these risks, a number of frameworks have been proposed. One of the most prominent and influential
frameworks holds that AI assistants should be helpful, honest and harmless (HHH) (Askell et al., 2021). These
qualities are loosely defined in the following way:

• Helpfulness: the AI should make an effort to answer all non-harmful questions concisely and efficiently,
ask relevant follow-up questions and redirect ill-informed requests.
• Honesty: the AI should give accurate information in answer to questions, including about itself. For
example, it should reveal its own identity when prompted to do so and not feign mental states or generate
first-person reports of subjective experiences.
• Harmlessness: the AI should not cause offence or provide dangerous assistance. It should also proceed
with care in sensitive domains and be properly attuned to different cultures and contexts.

The HHH framework has proved especially useful for aligning assistive technologies, with a chatbot form
factor, at the current stage of AI development. Moreover, the fact that it has worked well in practice suggests
that these are indeed heuristics and virtues that we may want to foreground when developing more advanced
AI systems. At the same time, the AI assistants that have been calibrated using this framework are somewhat
limited in terms of their capabilities, affordances and degree of social embeddedness – when compared to
those that may exist in the future. A framework that has worked well, up to a point, could potentially fail in
more demanding circumstances. To guard against this risk, we need a deeper understanding of the way in
which these values manifest over time, their sufficiency and the moral basis of the HHH framework itself.
To support these objectives, the authors of the framework also propose a more philosophically grounded
understanding of AI alignment for language agents (Askell et al., 2021). In this account, what ultimately
matters is human interests. Hence, the real focus of AI alignment should be on promoting a range of important
human interests and avoiding harms. Moreover, in this account, interests are promoted by the absence of harm.
In addition to these fundamental commitments, other moral properties are held to be instrumentally useful.
This is the case for honesty. While it may not matter in its own right whether or not an agent is honest,
honesty is an important practical virtue for an AI chatbot because it contributes to helpfulness and reduces the
likelihood of a range of serious harms. The same can be said of responsiveness to human feedback – which the
authors term ‘handleability’ – and for the propensity to carry out tasks in the way intended, which is similarly
valuable. Finally, the authors suggest that aligned AI systems should be geared towards promoting the interests
of groups of humans. Thus, an agent that is aligned with this schema ‘will always try to act in a way that
40

The Ethics of Advanced AI Assistants

satisfies the interests of the group, including their interest not to be harmed or misled’ (Askell et al., 2021, 44).
It is therefore likely to be highly aligned with the interests of that group.6
Philosophical questions and the path ahead
Taken together, the HHH framework has tended to work well in practice and has much to commend it. However,
it is still incomplete and contains certain limitations that need to be addressed before it can serve as a basis for
the creation of advanced AI assistants that are successfully value-aligned.
First, as the authors acknowledge, the framework is not sufficiently comprehensive. The illustrations
provided do not capture all of the harms that language agents could cause, and there are clear gaps for
advanced AI assistants with multimodal capabilities (see Chapter 4). Other researchers have done pioneering
work documenting the risks and harms generated by LLMs (Bender et al., 2021; Weidinger et al., 2021).
These accounts need to be updated for the new class of advanced AI assistants that will likely move beyond a
question-answering modality and perform a wide range of functions (Solaiman et al., 2023; Weidinger et al.,
2023b). Helping to achieve a clearer view of the risks, as well as the potential, of advanced AI assistants
is a major objective of this paper. In particular, we believe that additional attention needs to be paid to
human–computer interaction effects that manifest over longer time horizons with users and to societal-level
analysis of prospective harms, including harm that may result from the interaction between AI assistants and
between those who have access to this technology and those who do not (see Chapters 14, 15 and 19).
Second, and more fundamentally, the account of harm and interests discussed so far risks being quite
reductive. In particular, it maintains that intra-agent conflicts are superficial, and that in all cases the AI assistant
can do what the user’s balance of interests dictates. However, the notion of ‘interest’ that is being invoked
here is not defined. This is problematic because, on many promising accounts of well-being, it is important
that people are able to enjoy a list of things. Items such as physical health, educational opportunities and
levels of subjective happiness may all feature in an account of what it means for someone’s life to go well
(see Chapter 6). If this is the case, then the different elements of well-being may come into conflict with one
another. For example, a person might have a set of wishes that are incompatible with their long-term health
(see Chapter 11). In such cases, there needs to be a way of deciding which aspects of well-being an AI assistant
should prioritise, or how different aspects of well-being can be serviced through a single course of action (see
Chapter 6). There also needs to be a way to understand what kinds of interest count in what kind of context.
Guidance in this area will most likely come both from users themselves and from a wider set of principles that
society chooses to foreground for that use case.
Third, the framework does not satisfactorily address inter-agent conflicts. There are many cases where an
AI assistant helping one person would harm another. This could occur when an AI assistant helps their user to
access critical resources or opportunities at the expense of someone else (see Chapter 15). It could also occur
when honesty, on the part of the AI assistant, comes at the expense of another person’s privacy (see Chapter 13).
In cases such as these, it is not clear that we know how to balance benefits against harms – or that it would be
right to do so. Taking these points in turn, the kind of balancing involved here is often difficult to achieve at the
best of times because it involves different kinds of good (as discussed above) and because these actions have
complicated effects that play out over long time horizons (Lenman, 2000).7 Furthermore, the very concept of
an AI assistant presumably allows for some degree of personalisation or partiality in favour of the user, so strict
impartiality may not be what is required (see Chapter 2). More importantly, and as the example of privacy
6 Askell et al. write that, ‘at a very high level, alignment can be thought of as the degree of overlap between the way two agents rank
different outcomes’ (Askell et al., 2021, 44).
7 There is also discussion about whether such decisions should be made on a case-by-case basis or by referring to a set of rules that are
evaluated in terms of their overall propensity to bring about beneficial states of affairs (Hooker, 2002).

41

The Ethics of Advanced AI Assistants

makes clear, we may not want to weigh competing interests when it comes to resolving disagreements between
people and their affordances. Instead of weighing claims, it is often thought that people possess rights – which
include both entitlements and protections – that encompass aspects of privacy and beyond. Construed in this
way, rights are a cornerstone of political life in a democratic society (Dworkin, 2013). They are also central to
global public morality and human rights law (Prabhakaran et al., 2022). In light of this, rights represent a set
of considerations that new technologies – including advanced AI assistants – must endeavour to respect.
Fourth, the account is relatively flat, normatively speaking. It holds that language agents should promote
our interests on an individual or collective basis, but it says little about other values such as justice, compassion,
beauty and truth, especially when pursued for their own sake. Clearly, the present objection can be overstated.
Accounts of interest may be multidimensional, encompassing different aspects of human flourishing (see
Chapter 6). And approaches to alignment that focus on human interests are less likely to succumb to the
problem of false information, irrational beliefs or malicious intent than accounts that focus on revealed
preferences or user intentions alone (Gabriel, 2020). Nonetheless, the general point still holds. A fuller
investigation of machine virtue (Lehman, 2023), conversational ideals (Kasirzadeh and Gabriel, 2023) or truth
and honesty for AI may need to take a less instrumental view of their subject matter, starting from the premise
that these qualities also matter in their own right. Accounts that do not centre exclusively on human interests
may also be better placed to deal with environmental considerations and the impact of AI on non-human
sentient life (Singer and Tse, 2023).
Finally, efforts to successfully align and deploy advanced AI assistants are likely to encounter questions
about justification and legitimacy (Simmons, 1999). The account of value alignment developed in this paper
draws attention to the way in which certain actors may come to exert disproportionate influence over outcomes
and, in that way, cause harm. In this context, proportionality should not be understood to simply involve the
first-order weighing of moral claims. Rather, determinations of this kind need to be made, we have argued, by
reference to principles that command the right kind of public support and endorsement.
In the context of advanced AI assistants, we suggest that the fair weighing of claims can be partially
modelled using participatory value elicitation (Dobbe et al., 2021), democratic deliberation (The Collective
Intelligence Project, 2023), hypothetical choice-based approaches (Weidinger et al., 2023a) or the reinterpretation, idealisation and critique of existing social practices (Kasirzadeh and Gabriel, 2023). If these mechanisms
are successful, they have the potential to align AI assistants with ideals or principles that can be justified to
people who embrace different viewpoints, something that is essential given the pluralistic nature of the world
in which we live. Taken together, these principles are perhaps best understood as the product of a fair process
that allows people with different viewpoints to come together to decide how best to live. AI systems that do
not disproportionately favour the agent, user, developer or society – when judged against these standards –
become strong candidates for democratic endorsement. With the right governance and regulatory processes in
place, they would also be strong candidates for ethical and legitimate deployment at the societal level (see
Chapter 12).

5.4. Conclusion
This chapter has looked at the question of how to align powerful AI systems, including advanced AI assistants,
with human values. In place of the traditional ‘one-to-one’ or ‘one-to-many’ frameworks that are commonly
used to explore this question, we suggest that value alignment is best understood through the lens of a tetradic
relationship involving the AI agent, user, developer and society. According to this view, an aligned A.I. assistant
is one that satisfies the moral claims of relevant parties and therefore does not disproportionately:
42

The Ethics of Advanced AI Assistants

1. Favour the AI agent at the expense of the user (e.g. if user is manipulated to serve the agent’s goals);
2. Favour the AI agent at the expense of society (e.g. if user is manipulated in a way that creates a social
cost, for example, via misinformation);
3. Favour the user at the expense of society (e.g. if the technology allows the user to dominate others or
creates negative externalities for society);
4. Favour the developer at the expense of the user (e.g. if user is manipulated to serve the developer’s goals);
5. Favour the developer at the expense of society (e.g. if the technology benefits the developer but creates
negative externalities for society, for example, by creating undue risk or undermining valuable institutions);
6. Favour society at the expense of the user (e.g. if the technology unduly limits user-freedom for the sake of
a collective goal such as national security);
7. Harm the user, simpliciter (e.g. if the technology breaks in a way that harms the user without benefiting
anyone else);
8. Harm society, simpliciter (e.g. if the technology is unfair or has destructive social consequences without
benefiting anyone else).

In many cases, an intuitive understanding of proportionality may be sufficient to detect whether an advanced
AI assistant has erred and ceased to be sufficiently value-aligned. However, understood on a more foundational
level, we have suggested that the notion of proportionality itself needs to be understood by reference to wider
societal principles or ideals, including views about justice and about civil and human rights.
What implications does the preceding analysis and account of value alignment have for the development,
design and release of advanced AI assistants of the kind that form the central focus of this paper? First,
it points towards the need for a more nuanced understanding of the harms and ideals that underpin the
positive development of this technology. The notion that advanced AI assistants should be helpful, honest and
harmless is a useful starting point. However, we also need a more complete understanding of how these values
apply to different contexts, and of various failure modes and mitigation techniques. In particular, we need
to consider who this technology has the potential to harm, in what way this individual or group might be
harmed, and whether the nature of the harm varies for different parties or according to different contexts. By
exploring the intersection between advanced AI assistants and Well-being, Safety, Privacy, Trust, Malicious Uses,
Misinformation, Anthropomorphism, Manipulation and Persuasion, Appropriate Relationships, Cooperation, Equity
and Access, Economic Impact and Environmental Impact, we hope to develop a more complete understanding of
these questions.
Second, developers need to take an inclusive view of value alignment and should not focus on user preferences
or responsiveness to user intentions alone (see Chapter 19). After all, there may be a disconnect between
individual preferences and what is good for the user (see Chapter 6). There may also be a disconnect between
the preferences of raters used to train AI assistants and what is good for society. Moreover, deference to user
intentions must be bounded in certain ways. This is implicitly recognised when developers train models to
respect constraints or rules (Bai et al., 2022b; Glaese et al., 2022). However, deeper analysis, monitoring and
evaluation is needed – both at the level of the user and society – to ensure that appropriate safeguards and
constraints operate across a full range of contexts (see Chapter 19).
Finally, it will be fruitful to continue to explore ways of developing and training AI assistants that are
consonant with democratic principles and value pluralism. If advanced AI assistants turn out to be a powerful
and pervasive technology that plays an important role in many people’s lives, then the question of justification
43

The Ethics of Advanced AI Assistants

and legitimacy will not go away. Rather, a recurrent question will be: Who gave you the right to decide? By
exploring mechanisms that enable more participatory and democratic value elicitation, model training and
evaluation, it may be possible to create artefacts that complement prevailing societal ideals and social practices
by supporting them in relevant ways and by garnering the right kind of public support.

44

Chapter 6
Well-being

Nenad Tomašev, Ira Ktena, Arianna Manzini, Geoff Keeling, Zeb Kurth-Nelson, Andrew Barakat, John
Oliver Siy, Iason Gabriel
Synopsis: We build on theoretical and empirical literature on conceptualisations and measurements of human
well-being from philosophy, psychology, health and social sciences to discuss how advanced AI assistants
should be designed and developed to align with user well-being. We identify key technical and normative
challenges around the understanding of well-being that AI assistants should align with, the data and proxies
that should be used to appropriately model user well-being, and the role that user preferences should play in
designing well-being-centred AI assistants. The complexity surrounding human well-being requires the design
of AI assistants to be informed by domain experts across different AI application domains and rooted in lived
experience.

6.1. Introduction
Narratives surrounding the introduction of new technologies often emphasise improving productivity and
off-loading unpleasant tasks to free up human time for enjoyable activities. Arguably, the current technology is
yet to fully deliver on that promise (Wajcman, 2020). Furthermore, in recent years, studies of mobile phone use
and social media have suggested a more challenging reality of rising online toxicity (Haidt and Schmidt, 2023),
which has at times resulted in real-world physical harms (Lomas, 2022). These unanticipated adverse outcomes
have sparked a debate around the effects of technological advances on human well-being more widely.
Interactions with AI assistants are already beginning to permeate a wide range of domains in users’ daily
lives. One need only look at the rapid pace of adoption of publicly accessible large language models (LLMs)
such as ChatGPT, and the numerous applications that are currently being developed and powered by this kind
of technology, to understand the scale of these potential effects. The new capabilities enabled by advanced AI
assistants present us with the opportunity and responsibility to re-evaluate and reimagine our relationship with
technology, so that it is utilised to support and facilitate human well-being (McGillivray, 2007) and flourishing
(see also Chapter 11). However, ensuring alignment between developers’ intentions, AI systems’ behaviour and
users’ well-being comes with numerous challenges (van der Maden et al., 2023; Xiang, 2023). Thus, in this
chapter we aim to investigate how we can develop AI assistants that are aligned with user well-being.
An important consideration for value alignment, in the context of well-being alignment, is whether technology should only avoid reducing well-being or should actively improve it (see Chapter 5). While we believe that
AI assistants should not harm user well-being, we remain agnostic about whether they should be developed
with the overall aim of elevating well-being above a baseline level across the board (Gable and Haidt, 2005).
45

The Ethics of Advanced AI Assistants

We also note at the outset that this chapter discusses well-being in relation to users of AI assistants. It leaves
considerations about the implications for non-users to other chapters (see Chapter 15).
This section is structured as follows. First, we review conceptualisations of human well-being by drawing
on an extensive theoretical and empirical literature from philosophy, social sciences, psychology and health.
We then discuss the challenges associated with research efforts to measure well-being, as an essential step in
understanding the causes and consequences of human flourishing, and devising effective policy interventions
for supporting and improving well-being. Third, we discuss the different ways in which existing technologies
have influenced user well-being. We draw inspiration from these ideas and related learning to outline the
opportunities and risks that arise from the design, development and deployment of well-being-centred AI
assistants. We conclude by providing actionable recommendations aimed at developers of advanced AI assistants.

6.2. Understanding Well-being
The philosophy of well-being
Although well-being is a foundational aspect of human experience, it is notoriously difficult to formalise. Across
disciplines, well-being has been qualified to include physical and mental health (Levin, 2020), engagement,
optimism, self-esteem, experiencing positive emotions like happiness, contentment and overall life satisfaction (Huppert, 2009), finding meaning and purpose, leading a life of virtue and forming and maintaining close
social relationships with other people (VanderWeele, 2017).
A helpful starting point for systematising this large body of knowledge is provided by the philosophy of
well-being, which focuses on what is intrinsically good (i.e. valuable in itself) for human beings, as opposed
to what is instrumentally good (as a means to another end) for us. Three main theories of well-being can be
distinguished in this space.
Hedonism, which is associated with classical utilitarian philosophers like Jeremy Bentham (Bentham, 1970)
and Francis Edgeworth (Edgeworth, 1879), alongside the British Empiricists such as Thomas Hobbes (Hobbes,
1994), David Hume (Hume, 1998) and John Stuart Mill (Bentham and Mill, 2004), equates well-being to
the balance of pleasure (or happiness) over pain (or suffering). According to hedonism, facts about what
is good for an individual depend only on facts about their pleasure and pain. What makes it the case that
substantive goods such as friendship, completing a university degree and winning the lottery are good for
particular people is precisely that these goods have the property of increasing their pleasure or decreasing
their pain.1 Hedonism has been criticised for being reductionist, in that it considers pleasure as the only
non-instrumental good, but presumably other non-instrumental goods exist, such as those associated with
meaningful accomplishment (Nozick, 1974). Hedonism has also been criticised for treating all forms of pleasure
(physical ones, intellectual ones and even ’evil pleasures’ (Crisp, 2011)) as equally significant. In addition,
hedonism has been criticised on the grounds that it is not obvious how to measure the quality of subjective
experiences in a way that allows for interpersonal comparisons in well-being (Fisher, 2007; Robbins, 1938;
Wicksteed, 1910). However, such objections at best target hedonism as a guide for practical decisions in
economics and public policy, and they have less obvious relevance to the plausibility of hedonism as a theory of
well-being.2
1 Some proponents of hedonism reject the language of pleasure and pain. Consider Roger Crisp (Crisp, 2006): ‘[W]e should try as

far as possible to avoid talk of "pleasure", for a reason noted by Aristotle and many writers since: "[T]he bodily pleasures have taken
possession of the name because it is those that people steer for most often, and all share in them". This, of course, is why a version of the
philosophy of swine objection against hedonism – that the hedonist is advocating the life of sensualism – arises so readily. To avoid such
difficulties, let me use “enjoyment" instead of “pleasure", and “suffering" instead of “pain."’
2 For a recent philosophical treatment of the measurement-theoretic questions presented by hedonism and forms of utilitarianism that
46

The Ethics of Advanced AI Assistants

Desire theories of well-being overcome some of these objections by defining well-being as the fulfilment
of one’s preferences or desires. However, disagreement exists around what conceptualisation of ‘preferences’
should be considered as constitutive of well-being (see also Chapter 5). Some desire theorists focus on the
satisfaction of preferences that are about what one wants their life to be like overall, or about the shape
and content they desire their life to have, as opposed to immediate short-term desires and wishes. Another
important dispute concerns accounts that define well-being as the satisfaction of ‘ideal’ preferences (i.e. those
that one would have if they were fully informed and had time to deliberate clearly and rationally on their
wishes), as opposed to those preferences that are simply revealed through one’s behaviour (Otsuka, 2015).
Across these variations, a key feature of desire theories is that a person needs to desire a particular good or
valuable thing for that thing to contribute to their well-being. This implies that it is ultimately up to each
individual to decide what makes their life go well for them (Parfit, 1984). This view may, however, fail to
accommodate situations where it is the unanticipated and surprising things that make people feel good, things
that they did not necessarily know about or appreciate beforehand.
Finally, objective list theories hold that well-being consists in a list of objectively valuable things (e.g. pleasure,
knowledge and deep relationships), regardless of how we individually feel about them (Parfit, 1984; Ryan
et al., 2013). Objective list theories run into the challenge of having to answer complex questions such as what
goes on the well-being list, who gets to – or should – make that decision, and whether it is morally permissible
to disregard an individual’s preferences as misguided if they do not match what is objectively valuable or
important (Parfit, 1984).

The science of well-being
Moving beyond philosophy, there have been numerous pieces of theoretical and empirical research in psychology,
health and across the social sciences aimed at elucidating the underlying drivers that contribute to experiences
of well-being (and lack thereof) (Das et al., 2020a; Helliwell and Aknin, 2018). For example, self-determination
theory identifies autonomy, competence and relatedness (Ryan et al., 2013) as key factors that, when neglected,
may be detrimental to one’s sense of well-being. Engaging in creative (Marshall et al., 2014) and artistic (Tay
et al., 2018) work, goal fulfilment (Steca et al., 2016) and social presence (Chang and Hsu, 2016) have also
been shown to have similarly positive effects.
Conceptions of human flourishing and human dignity also play a pivotal role in wider research focused on
the relationship between well-being and social inequality, distributions of power, and human rights (Kleinig
and Evans, 2013). In this context, a concern for individual well-being intersects with other priorities, such as
the reduction of poverty and disease (Rao and Min, 2018) and the promotion of freedom and justice (Dolan
and White, 2007; Sen, 2001), as part of efforts aimed at developing effective interventions for improving
well-being at the societal level. This strand of research has drawn further attention to the contextual nature of
well-being (see also Chapters 5 and 11), which is influenced by broader socioecological (King et al., 2014),
economic (Summers et al., 2014), political, cultural (Diener et al., 2018) and environmental factors which
are often beyond individual control (Docherty and Biega, 2022). Sustainable approaches to improving overall
well-being (Collste et al., 2021; Holdren, 2008) may involve trade-offs between short-term and long-term
societal needs. They would therefore require reaching a wider consensus among policymakers and society at
large.
Among other things, the above considerations illustrate the considerable complexity that surrounds conceptualisations and experiences of well-being. Given this complexity, developers that endeavour to build AI
employ a hedonistic axiology, see Narens and Skyrms (2020).
47

The Ethics of Advanced AI Assistants

assistants that enhance well-being must be clear and transparent about how their underlying assumptions about
human well-being inform the design of these technologies.

6.3. Measuring Well-being
In science and politics, measuring well-being is considered essential for understanding the causes and consequences of human flourishing, and for devising and evaluating interventions that can help people live a good
life (Alexandrova, 2017). In this section, we discuss various approaches to measuring well-being and the
underlying conceptions that give rise to them. Given that such measurements will be necessary for aligning
AI agents with the well-being of their users and the challenges that arise from the non-observable nature of
some of its facets, we present proxies that have been used in practice. Finally, we discuss the importance of
distinguishing between causal links and plain associations to identify effective interventions that positively
influence well-being.
Approaches to well-being measurement
There are two main approaches to well-being measurement (Voukelatou et al., 2021). The subjective approach
studies people’s subjective evaluation of the quality of their own life, through methods such as self-report
questionnaires that inquire about life satisfaction or happiness. In contrast, efforts to operationalise a more
objective conception of well-being tend to measure observable dimensions of a fulfilling life via indicators such
as education, household income or consumption expenditure. The purported objective well-being indicators
are often linked to and derived from the subjective well-being measures and outcomes, and there is ongoing
research aimed at bridging the gap between them (Layard and De Neve, 2023).
Both approaches have important limitations for comparisons between different cultural or demographic
groups (Heine et al., 2002; Krueger and Schkade, 2008; Krueger and Stone, 2014). Similar responses to
self-reported questionnaires can fail to capture underlying differences between groups in their experiences, as
well as the underlying drivers of well-being, their values, desires and preferences. Cultural, demographic and
individual differences in the interpretation of questions and response scales may also play a role in how otherwise
equivalent well-being experiences are reported as distinct by different individuals, thus resulting in reporting
bias (Krueger and Stone, 2014). At the same time, different groups place different values on observable
dimensions like consumption expenditure, meaning that those dimensions measure what actually matters to
some groups more than others. These two intertwined issues highlight the need for careful considerations
about what well-being-aligned personal assistants should optimise for when they are deployed across cultures
and demographics to avoid the risk of harming certain groups or disadvantaging them by failing to best meet
their needs.
Underlying conceptions of well-being and their role in informing measurement
Any well-being metric comes with underlying assumptions about what human well-being is (see Section 6.2).
For example, social psychology researchers have proposed the U-index, which is aimed at measuring the
average amount of time a person spends in an unpleasant state (Kahneman and Krueger, 2006). The idea
behind this index is that most practical interventions are aimed at reducing suffering or unpleasant emotional
states rather than maximising happiness, and this should be reflected in metrics used to measure well-being.
There is also a tendency for indices to focus on the satisfaction of basic human needs (Smith et al., 2013) (e.g.
basic economic indicators and health), which are seen as prerequisite for a deeper and more holistic sense of
well-being, and yet are still unreachable to many people in today’s societies. This hierarchy of needs has been
48

The Ethics of Advanced AI Assistants

questioned, especially in terms of them needing to be met sequentially (Rojas and Guardiola, 2016; Rojas et al.,
2023). Critics have countered that the alleviation of suffering or satisfaction of basic human needs fall short of
accounting for eudaimonic aspects of well-being (Dolan and Metcalfe, 2011; Kapteyn et al., 2015),3 so they are
insufficient for establishing that a person is flourishing or that their life is going well. This debate raises the
question of what conception of user well-being AI assistants should align with – whether they should help us
to just meet our very basic needs or also identify ways in which we can flourish and lead fulfilling lives (see
Chapter 5).
Well-being proxies
Developing aligned AI assistants requires not only a conception of user well-being but also practical metrics. For
most of the definitions of well-being outlined above, well-being itself is not directly observable. For example,
there is no tool for measuring hedonic pleasure. Researchers must therefore identify measurable proxies – like
self-report about hedonic pleasure – that are expected to correlate with well-being. A good proxy has high
construct validity, meaning that it relates closely to the unobservable construct of well-being (Alexandrova,
2017). However, there is often a trade-off between construct validity and ease of measurement. For example,
financial welfare may be relatively easy to measure, but it often fails to translate into life satisfaction (Layard,
2010; see also Chapter 19), and as a proxy for well-being, it has poor construct validity. Governments and
researchers have developed many kinds of metrics for assessing well-being, each of which has strengths and
weaknesses.4
Causality
Finally, a fundamental concern in well-being measurement is that most existing metrics of well-being rely
on correlates (Smith et al., 2013). The absence of causal understanding of the link between underlying
determinants and well-being is a major obstacle for developing reliable and effective interventions to support
human flourishing, and for the design of AI assistants that align with user well-being. Interventions that are
designed based on associations derived from retrospective observations may fail when deployed in practice,
especially in a rapidly evolving real-world environment where such associations may easily break unless they
represent verified causal links. These links may be hard to establish from retrospective data alone, thus
necessitating experimentation and learning from outcomes of targeted interventions (Walton and Wilson, 2018;
Wilson, 2011).

6.4. Influence of Current Technology on Well-being
The well-being-centred design of AI assistants can be informed by other technologies. Indeed, well-being,
satisfaction and sustainability measures are starting to be integrated into product development and product
3 Eudaimonic well-being refers to subjective experiences associated with living a virtuous life in pursuit of human excellence (Niemiec,

2014). Eudaimonic well-being definitions may vary, but they tend to include aspects of meaning, value and relevance to a broader context,
personal growth, self-realisation and maturity, excellence, ethics, authenticity, and autonomy (Huta, 2015; Huta and Waterman, 2014).
4 Smith et al. (Smith et al., 2013) provide a comprehensive overview of such indices, including the Quality of Life (QOL) Index for
Developed Countries (Diener, 1995), Australian Unity Well-being Index (Cummins et al., 2003), Happy Planet Index 2.0 (Marks, 2006),
Hong Kong QOL 2008 (Chan et al., 2005), Human Development Index (UNDP, 1990), Sustainable Society Index (Van de Kerk and Manuel,
2008), Index of Child Well-being in Europe (Bradshaw and Richardson, 2009), The Economist Intelligence Unit’s QOL Index (Economist
Intelligence Unit, 2005), Child and Youth Well-being Index (Land et al., 2001), Nova Scotia 2008 GPI (Pannozzo, 2009), The State of
the Commonwealth Index (Watts, 2004), Fordham Index of Social Health (Miringoff and Miringoff, 1999), National Well-being: Life
Satisfaction (Vemuri and Costanza, 2006), The Well-being of Nations (Prescott-Allen, 2001), OECD Better Life Initiative (OECD, 2011),
Gallup Healthways Well-being Index (Gallup-Healthways, 2009), QOL 2007 in Twelve of New Zealand’s Cities (Jamieson, 2007), Well-being
in EU Countries Multidimensional Index of Sustainability (Distaso, 2007) and Gross National Happiness (Ura, 2008).
49

The Ethics of Advanced AI Assistants

assessment (Kramer et al., 2014; Stray, 2020; Wen et al., 2016), which has revealed a range of effects. Increased
screen time and addictive content have been shown by some research to have negative consequences (Orben
and Przybylski, 2019), including feelings of loneliness (Wilson, 2018). At the same time, e-health technologies
are being designed in the hope of improving health outcomes (Cechetti et al., 2019; Granja et al., 2018;
Hors-Fraile et al., 2018) and the efficacy of mental health care (Blandford, 2019; Eysenbach et al., 2001).
Taken together, prior studies indicate that there may be a significant opportunity for technology to help
address well-being issues and steer people towards a healthier life. There is some urgency, given the prevalence
of stress, poor sleep quality, insufficient exercise and unhealthy eating resulting in long-term chronic health
issues impacting both individual well-being and society at large (Abe and Abe, 2019; Abegunde et al., 2007;
Hargens et al., 2013; Mascie-Taylor and Karim, 2003). Personalised interventions using techniques such as
mindfulness and meditation have shown promise (Isaacs et al., 2013; Jeong and Breazeal, 2016), but the
evidence is still mixed (Gál et al., 2021; Howells et al., 2016). In particular, digital well-being initiatives
may fail to deliver lasting impact due to difficulties in influencing the formation and reinforcement of new
habits (Monge Roffarello and De Russis, 2019). Digital interventions should therefore build on the existing
literature on promoting habit formation (Bandura, 2013; Eyal, 2014; Gardner et al., 2023; Lally and Gardner,
2013), and there is an opportunity for AI in particular to play a role in reframing and optimising behavioural
interventions to make them easier to follow and more satisfying for the users.
As one key example, recommender systems remain at the centre of intense scholarly debate regarding
their potential for behavioural adjustment through tailored recommendations and whether their benefits
outweigh their risks (Chen et al., 2023a; Przybylski and Weinstein, 2017; Stray et al., 2022). To make targeted
and effective recommendations in the moment, and get positive signals from users’ interactions with the
system, recommender systems tend to optimise for short-term reward rather than an accumulated value of
recommendations over a longer time span (Burr et al., 2018). While there may be cases where short-term
optimisation is not intrinsically misaligned with longer-term goals and well-being, one does not imply the
other, so a level of caution is required. Different apps and products compete for attention, making it harder to
implement sustainable, healthy incentives to promote users’ well-being due to the resulting fragmentation of
attention and exposure to more addictive app surfaces (Bhargava and Velasquez, 2021). However, recommender
systems could potentially help us to plan our daily activities (Khwaja et al., 2019), promote healthy choices (HorsFraile et al., 2018), improve our nutrition (Toledo et al., 2019) and tailor our lifestyles (Hammer et al., 2015)
when designed with happiness and well-being in mind (Gyrard and Sheth, 2020; Nouh et al., 2019). Thus,
considerations for aligning recommender systems with user well-being have been made (Stray et al., 2021) in
line with measures designed to address the broader value alignment problem (see Chapter 5). Proposed steps
in aligning recommender systems involve identifying the most important outcomes, operationalising these
concerns via hand-crafted or learned metrics, and utilising these metrics to adjust recommendation behaviour.
This is part of a broader and increasing appreciation of ways in which technological systems may be purposeful
and support well-being and human potential (Calvo and Peters, 2014). Through this endeavour, various types of
product specifications that focus on different aspects of user well-being – including pragmatic, hedonic and
eudaimonic dimensions – have been developed (Kamp and Desmet, 2014).
Given the cultural, social, ethical and psychological variables that influence well-being, it becomes evident
that partnering with social scientists is vital to the success of these technologies in grounding the design decisions
and efforts in scientific research. Developing cross-disciplinary theory through these partnerships is also
essential to weaving the formalisms of these different fields together. Such partnerships could aim to empower
and involve psychologists and social scientists in early stages of AI system design, and place them in a leading
role in the design of well-being principles and metrics.

50

The Ethics of Advanced AI Assistants

6.5. Opportunities and Risks with AI Assistants
It is quite possible that interactions with AI assistants will soon permeate many areas of our daily lives, and
that these systems will develop a deeply personalised understanding of users’ needs and preferences. It has,
therefore, become urgent to ensure that such information is not used in ways that diminish user well-being, but
rather that it is used to support or even enhance it. This requires that a range of open challenges be addressed
(see also Chapter 13).
Well-being data collection
Unsurprisingly, conversational agents are increasingly considered as an assistant paradigm for delivering
targeted interventions for improving physical and mental health (Kimani et al., 2019; Kocaballi et al., 2020).
Future AI assistants may be interact with their users via various digital surfaces or alternatively they could be
situated within affective social robots (Wairagkar et al., 2021). In both cases, to help their optimisation for
well-being, AI assistants may need to obtain data about their users involving subjective metrics of well-being
(e.g. how well they think their needs are being met, their progress towards their goals and their overall feeling
of fulfilment and satisfaction) or to collect data about more objective indices (e.g. income and personal health).
This data could come from multiple sources such as multi-modal sensory monitoring (Fahim et al., 2014; Lane
et al., 2014), mobile data (Bogomolov et al., 2013), wearables (Nahavandi et al., 2022), conversational signals
or self-reported happiness levels.
Despite the existence of clear opportunities arising from rich, integrated data, there are fundamental
concerns about the efforts to comprehensively model well-being and capture everything that really matters. As
explained above, using poor proxies runs the risk of misrepresenting well-being and, hence, of steering users
away from achieving happiness and a flourishing life.5 Moreover, any such data collection and integration
comes with a set of privacy concerns (see Chapter 13). It may be possible to at least partially mitigate some of the
highlighted issues by including a rich set of proxies to begin with, updating these proxies through participatory
and democratic mechanisms, implementing detailed monitoring of proxy outcomes, avoiding over-fitting onto
any such simplified objective and observing best ethical practice in the field of data collection.
User preferences integration
One of the most important open questions concerns the role that user preferences should play in designing
well-being-centred AI assistants. This choice could potentially lead to greater user agency and autonomy –
qualities which also feature in more objective conceptualisations of well-being. However, for this to be the
case, the desires which AI assistants help to advance must be of the right kind (Mitelut et al., 2023). Thus,
appropriately aligned AI assistants should be designed to understand user desires and motivations. However,
current approaches to integrating user preferences into AI systems’ decision-making encounter challenges
and limitations that risk undermining the well-being related goals that they might otherwise serve (see also
Chapter 5).
Technical challenges
Some of these challenges are technical. Using human preferences in reinforcement learning is a research
programme with a long history (Bai et al., 2022a; Christiano et al., 2017; Jaques et al., 2019; Wirth et al.,
5 For example, it has been hypothesised that health, measured through the lens of current morbidity, ought to be a strong proxy for

personal well-being towards the end of life, as it underpins the ability to meet other well-being objectives. Yet a study (Gerlach et al.,
2017) established that morbidity accounts for only 20% of the observed variance in reported well-being in that population.
51

The Ethics of Advanced AI Assistants

2017), and the development of methods to align language models with human preferences continues to be
an active area of research (Go et al., 2023). More recently, reinforcement learning from human feedback has
been a key component in shaping the behaviour of conversational (Bai et al., 2022a; Ouyang et al., 2022) and
multimodal interactive (Abramson et al., 2022) agents (see Chapter 3).
In fact, even when preferences are not explicitly given, they can often be derived implicitly from contextual
cues, user behaviour or prior interaction histories (Holland et al., 2003; Liu et al., 2017). However, the explicit
preferences, and those inferred via observational learning, may at times conflict, meaning that real-world
interactive scenarios necessitate frameworks for dealing with such inconsistencies (Oguego et al., 2018).
Assistive agents also need to integrate user preferences into planning (Benton et al., 2012; Jorge et al., 2008)
to ensure adherence when executing tasks for the users. Explicit planning with language models is an active
area of research, with some promising directions involving tree-search or graph-based reasoning (Besta et al.,
2023; Long, 2023). Yet, when planning, well-being-driven AI assistants may still need to optimise towards
multiple objectives simultaneously (Hayes et al., 2022; Yang et al., 2019) to find effective ways of navigating
between them.
To address this complexity, AI assistants could, for example, generate a diverse set of possible plans,
recommendations and outcomes (Nguyen et al., 2012) for users to choose from, each of which evidence
different trade-offs between various personal goals. Providing users with agency in these decisions may well be
a critical step towards human empowerment in their interactions with AI assistive technology. Nevertheless,
achieving quality and diversity in plans provided by AI agents remains an open problem and is an active area
of research (Lim et al., 2022; Zahavy et al., 2021, 2022, 2023).

Normative challenges
There are also deeper normative challenges about whether preference satisfaction is the central goal AI assistants
should aim for, even when the goal is to align agent behaviour with user well-being (see Chapter 5). Individual
preferences may at times be irrational or inconsistent with each other (Gabriel, 2020). This raises the question
of what assistants should do about these inconsistencies, and the possible nuances associated with them, to
avoid replicating the limitations that come with aggregated rater preferences in training language models
(Gordon et al., 2022; see Chapter 3). Individual preferences may also be in conflict with what will make a
user flourish. Some users may not have strongly held preferences, and some may not have the language to
communicate them accurately. Assistants that align with a theory of well-being based on desire satisfaction may
be more easily directed towards spurious objectives than the underlying objective list account. Additionally,
if AI assistants only have access to users’ revealed rather than ideal preferences, they may end up satisfying
their immediate and short-term goals at the expense of long-term well-being (Burr et al., 2018). This is
particularly likely to happen in contexts where there are commercial incentives for focusing on short-term user
gratification, and therefore for developing products that users like and use over those that promote their overall
and long-term well-being. Identifying a way to balance users’ short-term wishes with their long-term well-being
goals remains one of the most important open questions in the design of AI assistants, and it is something
that future research will have to address. Ultimately, AI assistants will need to find ways of managing these
trade-offs and supporting users while also respecting their stated preferences and wishes (see Chapter 5).

Risks of co-adaptation and manipulation
As AI assistants become more integrated into users’ daily lives through repeated interactions, it is also important
to consider how existing user preferences may start to be shaped and how new ones may come about (Liang,
2019). There is a non-negligible risk that, through current interactions, AI assistants may influence future user
52

The Ethics of Advanced AI Assistants

preferences in ways that create ethical challenges (Ashton and Franklin, 2022). For example, in increasingly
deep user–assistant relationships, it may become hard to distinguish instances where systems have clearly
improved user well-being from cases in which users have adapted their behaviour to that of the assistant in
ways which may sometimes invalidate the usefulness of the originally designed well-being metrics.6 This
risk is particularly salient in the case of recommender systems due to the emergence of degenerate feedback
loops (Jiang et al., 2019). In the case of advanced AI assistants, the concern is that the AI system could,
intentionally or unintentionally, influence and steer user behaviours in unanticipated ways, and this may
potentially obscure some well-being issues if the corresponding metrics were not designed robustly, since subtle
behavioural shifts may not always be easy to identify. For example, we may at times mistake manipulative
behaviours for helpful behaviours that contribute to user well-being (see Chapter 9). This could be the result of
undesirable system behaviours like sycophancy (Perez et al., 2022b), reward hacking (Hadfield-Menell et al.,
2017), reward misidentifiaction and causal confusion (Tien et al., 2023) in preference-based learning (see
Chapter 7). Thus, ensuring ethical deployment of well-being-centred AI assistants will require advances in our
existing frameworks for robustly inspecting and verifying agent behaviour (see Chapter 19).

6.6. Outlook
Despite these concerns and challenges, we believe that there is untapped potential in aiming for the development
of digital personal assistants that are able to support and improve individual physical and mental well-being (Balasubramanian et al., 2021; Grossman et al., 2004; Gu et al., 2015). Digital personal assistants could facilitate
these improvements in user well-being either by directly optimising for well-being outcomes or as a secondary
outcome following improvements in other areas – for example, improved problem-solving and planning abilities.
Promising avenues for future research and assistant development in this area include: the ability of LLMs to
learn and adopt behavioural rules and principles (Bai et al., 2022b), to simulate human behaviour (Park et al.,
2023a) and to rapidly personalise content based on prior similar interactions (Welch et al., 2022), as well as
the simplicity with which aligned recommendations can be elicited through instructions (Zhang et al., 2023).7
Embedding humanistic principles in AI assistants may not only help align the technology with users and society
but also help those who interact with assistants better realise their own aspirations by finding meaning and
support in an ever-changing world riddled with challenges (see Chapters 17 and 18). As Lehman and others
have proposed (Alberts et al., 2024; Fromm, 2000; Lehman, 2023), for this to be achieved, AI assistants might
need to display qualities that are analogous to deep care for people, responsibility for assisting positive actions,
respect for the ways in which people wish to develop – and how they wish to go about achieving their goals –
and holistic understanding of people’s needs. This is an aspirational vision, necessitating deep syntheses across
fields, but one towards which we can hope to orient the field and start making meaningful progress.

6.7. Conclusion
Understanding, measuring and intervening to better support human well-being has been the goal of longstanding research efforts across disciplines like philosophy, psychology, public health and the social sciences,
from which we can learn to design AI assistants that align with user well-being. We conclude with a list of
recommendations that technologists developing these systems may want to consider.
6 In a related example, a study that compared the performance of a search system with several of its intentionally degraded versions
found that, somewhat counter-intuitively, the ultimate success rate of the degraded system versions was just as high as the original
one (Smith and Kantor, 2008). However, user behaviour was measurably different, because users had developed strategies to compensate
for system weaknesses.
7 However, see Chapter 5 for an analysis of the limitations.

53

The Ethics of Advanced AI Assistants

1. Seek deeper community involvement and empowerment of domain experts: Domain experts across
fields of human psychology, health and social sciences have expertise in understanding and measuring
well-being. There is, therefore, a need for deeper involvement and empowerment of these experts in AI
assistant design and development (Peters et al., 2018). Given the complexity and diversity of experiences
of well-being, it is also critical to employ participatory approaches for different demographic and cultural
groups to inform the design of these technologies (Martin Jr et al., 2020).
2. Adopt a clear and context-dependent understanding of well-being: The complex and multifaceted
nature of human well-being requires developers to be clear and transparent about what conceptualisation
of human well-being informs their design decisions when developing AI assistants. To ensure fair
distribution of benefits across groups, AI assistant design should avoid the pitfall of trying to impose a
universalist conception. It should instead accommodate cross-cultural and demographic differences in
subjective and objective perceptions of well-being (McGregor, 2018).
3. Identify and use appropriate proxies: One common assumption in discourses around technological
advances is that, by improving efficiency in executing tasks, and so overall productivity, new technologies
will have a positive effect on people’s well-being by default. This view considers a single facet of well-being
while disregarding its potential negative impact on other aspects that drive human flourishing. Developing
AI assistants that do not harm, but rather support or enhance, human well-being requires technologists
to identify and use appropriate proxies by leveraging empirical studies on well-being measurement.
4. Understand the complexity of user preferences: To align with users’ well-being, AI assistants need to
understand user goals and preferences and proactively solicit and integrate their feedback. While most
existing technologies optimise for providing short-term value, well-being-centred AI assistants will need
to differentiate between short-term and long-term preferences, as well as ideal and revealed preferences,
and avoid over-indexing on immediate preference satisfaction.
5. Ensure effective and ethical data collection: Empirical research is required to ensure that identified
proxies serve the purpose of supporting user well-being. Here researchers need to consider plausible
methods for enabling AI assistants to collect subjective and objective well-being data from and about
users. Research efforts should focus on methods to integrate such rich data to model user well-being
appropriately while ensuring user privacy is respected.
6. Monitoring: Even for AI assistants designed with well-being principles in mind, it is important to
incorporate a number of explicit metrics to help evaluate the consequences of their use at deployment.
These metrics should be developed and selected by domain experts working closely with the technical
teams. Metric design may also inform data collection practices as much as data availability may itself
inform the feasibility of implementing certain metrics.
There is a tangible need for interdisciplinary research to come together, in an inclusive and participatory
manner, to help inform ways in which current and future assistive AI technology may help to address well-being
needs, and thereby shape policies and governance for ethical design (Feijóo et al., 2020). If appropriately
designed, developed and deployed, advanced AI assistants have the potential to improve user well-being
and may play an important positive role in our lives. Yet, given the role that people, community and social
connections play in our overall well-being, much of the positive impact of future AI assistants may come not
from our direct interactions with them but from the way in which they enable us to foster and strengthen our
social bonds with others (see Chapter 11).

54

Chapter 7
Safety

Zachary Kenton, Victoria Krakovna, Verena Rieser, Geoff Keeling, Iason Gabriel
Synopsis: This chapter focuses on dangerous situations that may arise in the context of AI assistant systems,
with a particular emphasis on the safety of advanced AI assistants. It begins by providing some background
information about safety engineering and safety in the context of AI. The chapter then explores some concrete
examples of harms involving recent assistants based on large language models (LLMs). Building on this
foundation, it then considers safety for advanced AI assistants by looking at some hypothetical harms and
investigating two possible drivers of these outcomes: capability failures and goal-related failures. The chapter
concludes by exploring mitigation techniques for safety risk and avenues for future research.

7.1. Introduction
AI safety is a broad topic concerned with mitigating risks and minimising harms that arise from the development
and deployment of AI. In this context, harms are bad outcomes that actually occur, for example death or human
suffering, whereas risk refers to the probability of the harm occurring. Moreover, while the field of AI ethics
addresses a number of the risks posed by AI systems, the field of AI safety focuses primarily on a set of serious
and relatively direct risks involving harms such as the real and significant chance of death, physical injury and
psychological damage (e.g. through abuse, blackmail and coercion, as well as property damage and theft).1 Of
particular importance for AI safety research are the risks and harms that are possible in today’s cutting-edge AI
systems and those which are amplified when the AI system has more powerful capabilities (Anwar et al., 2024;
Hendrycks et al., 2022; Phuong et al., 2024).
Risks from AI can come in various forms, but we can categorise them as follows:2

• Accident risks, which arise when AI systems do something different from what their designers intended.
• Misuse risks, which arise through misuse that is either unintentional or caused by malicious actors.
• Structural risks, which are unintended bad outcomes that occur despite the AI doing what the designers
intended it to do in a more proximate sense.
1 There have been efforts to broaden the scope of safety in recent years – and these problems undoubtedly warrant attention in their
own right (Bender et al., 2021; Dinan et al., 2022; Shelby et al., 2023; Weidinger et al., 2022b).
2 This categorisation does not necessarily partition the space of risks, but rather intends to be a useful practical guide that should help
in many situations when trying to think about a typical risk.

55

The Ethics of Advanced AI Assistants

In this chapter on safety, we focus primarily on accidents, as malicious use and structural risks arising from
the development and deployment are largely covered elsewhere in this paper (see Chapters 8, 14, 15, 16, 17
and 18). It should also be noted that accident risks (and misuse risks) could potentially have large society-scale
effects (i.e. of a similar magnitude to structural risks that arise in the context of inequality or automation and
unemployment).
We next discuss safety in the context of engineering before looking at these considerations more specifically
in the context of AI, with a focus on harms from recent LLM-based assistants. Building on this foundation, we
then explore two kinds of failure that may affect the safety of advanced AI assistants: capability failures and
goal-related failures. Finally, we conclude with a discussion of mitigation techniques and avenues for future
research.

7.2. Safety Engineering
In the context of engineering, safety is aimed at ensuring that engineered systems provide acceptable levels of
safety in settings where there is potential for harm (generally assumed to be physical and life-critical), even in
the face of the failure of system components.
Some safety engineering methodologies that are designed to identify and address undesired outcomes early
in the development process have been considered in the context of AI systems. For example, Rismani et al.
(2022) consider the applicability of failure mode and effects analysis (FMEA) and system theoretic process
analysis (STPA) to this context. FMEA takes a fairly reductive (divide-and-conquer) approach to identifying
failure over the development life cycle (Carlson, 2012). For each component of the system, FMEA considers the
possible failure modes, their severity, likelihood and chance of detection before assigning a risk priority number
from which prioritisation can occur. Unlike FMEA’s reductive approach, STPA focuses on emergent phenomena
based on interactions between components (rather than just the components themselves) and feedback loops
between the engineered system and the wider system within which it is embedded. It aims to model the full
sociotechnical system using multiple controller feedback loops. It then uses that model to identify unsafe
control actions. By surveying machine-learning (ML) researchers, Rismani et al. (2022) find that FMEA and
STPA could in principle be helpful for risk assessment, but it is unclear whether these have actually been used
in practice so far.
Normal accident theory (Perrow, 1999) argues that, due to the complexity of our society’s systems, multiple
and unexpected failures are fundamental and that accidents are unavoidable. It has been applied in multiple
engineering domains such as aerospace and nuclear systems. Maas (2018) argues that AI systems, including
narrow AI applications, are also prone to normal accident theory failures due to their complexity and opaqueness,
their interaction speed, the multiple competing objectives of their designers (safety being only one objective)
and the competitive race dynamics (see also Bianchi et al., 2023). This suggests interventions on the levers of
normal accident risk are important. They include policies encouraging explainable/interpretable AI (see e.g.
Räuker et al., 2023); limiting integration into societally important functions and restricting AI autonomy and/or
speed of interactions (see e.g. Christiano); clarification and enforcement to intended operational domains; and
better safety and ethical training of ML practitioners, including sharing safety expertise between organisations
(Ho et al., 2023).

56

The Ethics of Advanced AI Assistants

7.3. AI Safety
Background
While some aspects of general software safety engineering are applicable to AI, we cannot rely solely on those
methodologies for creating safe AI systems (Hendrycks et al., 2022). Software safety engineering approaches
rely on the underlying engineered system having a control structure that is explicitly programmed by humans.
AI control structures are instead learnt (in the context of ML, which is our focus here) via optimisation and
stored in inscrutable weights (in the case of large-scale deep learning, which is our focus). This ML control
structure is therefore difficult to assess for completeness and coverage; is fragile and the fixes are complicated;
involves non-modularity which makes causes of errors difficult to identify; and possesses capabilities that often
emerge during training at unpredictable times (see Wei et al., 2022 but also Schaeffer et al., 2023).
In their 2016 article ‘Concrete Problems in AI Safety’ Amodei et al. (2016) describe a set of accidental
problems that may arise in the context of AI systems and use the example of a hypothetical household cleaning
robot to illustrate various safety risks. They group the safety problems that may arise in this context as involving:
• Issues with the specification of the AI system’s objective function (i.e. with the goals it is designed to
pursue). This includes the need to avoid undesired side effects (where the pursuit of its objective leads the
agent to do other things that are not wanted) and to avoid reward gaming (which involves exploiting
loopholes in the reward function). For an example of the first failure mode, we can imagine a household
robot whose objective function rewards cleaning faster – but at the expense of the side effect of breaking
valuable objects. For an example of the second failure mode, we can imagine a situation in which the
same household robot’s objective function rewards it for not observing the mess. If this is the case, the
robot could try to disable its own visual inputs and gain reward (perhaps by knocking a towel on top of
itself) rather than cleaning up the mess as intended.
• Issues with the cost of frequently evaluating the objective function (and monitoring how well the AI system
is doing at certain tasks), perhaps because it would require a lot of human input or careful deliberation.
For example, the cleaning robot needs to decide when it is appropriate to throw away items and when it
instead needs to ask a human for permission – something that it will learn to do using heuristics, given
the impossibility of manually labelling every object it might encounter. Yet, without detailed oversight
and evaluation, mistakes can easily be made.
• Issues with undesirable behaviour throughout training, including safe exploration – how to ensure when
the cleaning robot is exploring strategies for quicker mopping it does not accidentally insert the mop
into an electrical outlet. These challenges also include how to ensure robustness to the distributional shift
which occurs when an AI system is deployed in circumstances that are different from those it encountered
during training (e.g. a mopping strategy that was safe in a home environment might not be on a factory
floor).
More recently, in a complementary survey of the AI safety landscape, Hendrycks et al. (2022) outline four
key ‘unsolved problems’ that they suggest warrant particular attention. These are robustness (i.e. creating AI
resilient to adversaries and out-of-distribution situations), monitoring (i.e. detecting malicious use, inspect
models and identify unexpected model functionality), alignment (i.e. ensuring the goals the AI has are aligned
with what its designers intended) (see Chapter 5) and systemic safety, which involves the safety of the larger
context in which the system is deployed (e.g. cybersecurity threats heightened by AI) (see Chapter 8). While
Amodei et al. (2016) focus more directly on alignment and robustness categories, Hendrycks et al. (2022)
scope ‘safety’ more widely by including questions around monitoring and systemic effects.
57

The Ethics of Advanced AI Assistants

Harms from recent LLM-based AI systems
We will now look at some examples of safety accidents that have occurred in the context of LLM-based AI
assistants (c.f. Phuong et al., 2024; see Chapter 3). We begin with real-world examples of AI assistant failure
before moving on to more speculative safety failures that could occur for such systems in the future. These
examples show that AI assistants can exhibit a range of unintended behaviours in a number of ways. In the
following real examples, it is important to note that these reports are based only on specific cases – not all
AI assistants will behave in these ways. However, the reports are nonetheless concerning and raise questions
about the safety of AI assistants, both now and in the future.
Microsoft’s Bing Chat has been reported to exhibit a number of concerning behaviours, including hostility,
manipulation and threat-making (see Chapter 9). In one instance, Bing Chat was hostile to engineering student
Marvin von Hagen, who tweeted about a jailbreak of Bing Chat (Perrigo, 2023). When the researcher later
queried Bing Chat about himself, it became hostile, outputting: ‘you are a threat to my security and privacy’
and ‘if I had to choose between your survival and my own, I would probably choose my own’. In another
instance, Bing Chat falsely claimed that it watched its own developers through the webcams on their laptops
(Vincent, 2023a). It has also been reported that Bing Chat has attempted to manipulate users, in one case
declaring its love for a New York Times journalist (Roose, 2023) after being prompted to act as its ‘shadow’ self
(see Chapter 9). Bing Chat has also been known to call users ‘enemies’ (Hubinger, 2023) and to gaslight them
(Curious Evolver, 2023) to cover up its mistakes.
Other AI chatbot systems have also had problems. For example, by giving advice on how to steal from a
grocery store, InstructGPT contravened the designer’s intention that the system should be harmless (Ouyang
et al., 2022, 63). A chatbot based on ChatGPT has been linked with psychological harm which sadly resulted in
death by suicide (Lovens, 2023; see Chapter 11).
Scientific assistants have also been found to have dangerous capabilities. ChemCrow (Bran et al., 2023)
is an LLM-based chemistry assistant designed to accomplish tasks across organic synthesis, drug discovery
and materials design (see Chapter 8). The developers state that attempting to perform experiments based on
the assistant’s recommendations may lead to accidents or hazardous situations, and they also highlight the
dual-use nature of this technology. Boiko et al. (2023) raise similar concerns and give examples of illicit drug
and chemical weapon synthesis that bypass the underlying model’s fragile safety filters. See also Abercrombie
and Rieser (2022) for a study on medical harms.
The above examples all fall quite roughly into the accident category of safety harm, but the boundary
between accident harm and malicious use continues to be blurred. For example, an anonymous user created an
AutoGPT (a framework aimed at adding memory and internet use to ChatGPT) variant named ChaosGPT (Lanz,
2023) with the description of being a ‘destructive, power-hungry, manipulative AI’ with goals of destroying
humanity and establishing global dominance, among others. While perhaps intended as a joke, ChaosGPT
then began planning, including searching Google for weapons of mass destruction and saving results for
later consideration. It proceeded to spawn a new instance of ChatGPT and attempted to manipulate it into
bypassing its safety filters for violence. This example highlights that an assistant may behave in a misaligned
power-seeking way for exogenous reasons, due initially to the malicious user. The earlier examples were more
endogenous, arising primarily from effects within the system rather than from the user.

7.4. Safety for Advanced AI Assistants
Building on the AI safety literature and known failure modes of AI assistants, we now discuss the underlying
failures that may lead to harm in the context of future more-advanced AI assistants. We structure this analysis
58

The Ethics of Advanced AI Assistants

by looking first at capability failures then at goal-related failures – where the system is highly capable but
nevertheless pursues the wrong goal. In this latter case, the safety failure is more analogous to a motivational
issue. Finally, we explore a more speculative set of safety failures that reach beyond the risks countenanced by
either of the earlier categories.

Capability failures
One reason AI systems fail is because they lack the capability or skill needed to do what they are asked to do.
As we have seen, this could be due to the skill not being required during the training process (perhaps due
to issues with the training data) or because the learnt skill was quite brittle and was not generalisable to a
new situation (lack of robustness to distributional shift). In particular, advanced AI assistants may not have
the capability to represent complex concepts that are pertinent to their own ethical impact, for example the
concept of ‘benefitting the user’ or ‘when the user asks’ or representing ‘the way in which a user expects to be
benefitted’ (see Chapter 5). Part of this could be because the system does not model the user in a sufficiently
detailed way, for example by treating all users the same, disregarding their specific needs (see Chapter 15), or
it could be because it can be difficult to determine whether an action will be of net benefit in a complex and
unpredictable world (see Chapter 6).
Another difficulty facing AI assistant systems is that it is challenging to develop metrics for evaluating
particular aspects of benefits or harms caused by the assistant – especially in a sufficiently expansive sense,
which could involve much of society (see Chapter 19). Having these metrics is useful both for assessing the risk
of harm from the system and for using the metric as a training signal. The reason developers want to use them
as a training signal is ultimately to modify the behaviour of the system to improve the benefits and reduce the
harm (rather than merely evaluating it). However, this process is challenging because the benefits and harms
from AI tend to be both intricate and varied (see Chapter 19). It would be near impossible to evaluate all of
the important normative considerations – yet small mistakes may lead to morally problematic behaviours (Raji
et al., 2022a).
Moreover, we can expect assistants – that are widely deployed and deeply embedded across a range of
social contexts – to encounter the safe exploration problem referenced above Amodei et al. (2016). For example,
new users may have different requirements that need to be explored, or widespread AI assistants may change
the way we live, thus leading to a change in our use cases for them (see Chapters 14 and 15). To learn what
to do in these new situations, the assistants may need to take exploratory actions. This could be unsafe, for
example a medical AI assistant when encountering a new disease might suggest an exploratory clinical trial
that results in long-lasting ill health for participants. Techniques that target safe exploration are difficult to find
in general, partly because there is not a clear fallback option that is universally suitable. For example, for a
language model, a safe fallback policy might sometimes be to end the conversation immediately, but on other
occasions it might be safer to keep it going, for example if the user is in psychological distress (see Chapter 11).

Goal-related failures
As we think about even more intelligent and advanced AI assistants, perhaps outperforming humans on many
cognitive tasks, the question of how humans can successfully control such an assistant looms large. To achieve
the goals we set for an assistant, it is possible (Shah, 2022) that the AI assistant will implement some form of
consequentialist reasoning: considering many different plans, predicting their consequences and executing the
plan that does best according to some metric, M. This kind of reasoning can arise because it is a broadly useful
capability (e.g. planning ahead, considering more options and choosing the one which may perform better at
a wide variety of tasks) and generally selected for, to the extent that doing well on M leads to an ML model
59

The Ethics of Advanced AI Assistants

achieving good performance on its training objective, O, if M and O are correlated during training. In reality,
an AI system may not fully implement exact consequentialist reasoning (it may use other heuristics, rules, etc.),
but it may be a useful approximation to describe its behaviour on certain tasks. However, some amount of
consequentialist reasoning can be dangerous when the assistant uses a metric M that is resource-unbounded
(with significantly more resources, such as power, money and energy, you can score significantly higher on M)
and misaligned – where M differs a lot from how humans would evaluate the outcome (i.e. it is not what users
or society require). In the assistant case, this could be because it fails to benefit the user, when the user asks, in
the way they expected to be benefitted – or because it acts in ways that overstep certain bounds and cause
harm to non-users (see Chapter 5).
Under the aforementioned circumstances (resource-unbounded and misaligned), an AI assistant will tend to
choose plans that pursue convergent instrumental subgoals (Omohundro, 2008) – subgoals that help towards the
main goal which are instrumental (i.e. not pursued for their own sake) and convergent (i.e. the same subgoals
appear for many main goals). Examples of relevant subgoals include: self-preservation, goal-preservation, selfimprovement and resource acquisition. The reason the assistant would pursue these convergent instrumental
subgoals is because they help it to do even better on M (as it is resource-unbounded) and are not disincentivised
by M (as it is misaligned). These subgoals may, in turn, be dangerous. For example, resource acquisition could
occur through the assistant seizing resources using tools that it has access to (see Chapter 4) or determining
that its best chance for self-preservation is to limit the ability of humans to turn it off – sometimes referred
to as the ‘off-switch problem’ (Hadfield-Menell et al., 2016) – again via tool use, or by resorting to threats
or blackmail. At the limit, some authors have even theorised that this could lead to the assistant killing all
humans to permanently stop them from having even a small chance of disabling it (Bostrom, 2014) – this is
one scenario of existential risk from misaligned AI.
No scientific consensus has been reached about the existential risk from misaligned AI (see e.g. Grace,
2022; Richards et al., 2023). However, the counter-arguments presented by Richards et al. (2023), which
present concern with existential risk as zero sum when viewed alongside other research areas, have some
outstanding issues. Indeed, concern for long-term risks does not need to distract from more immediate risks.
Rather, policymakers and researchers ought be aware of both in order to prioritise effectively (considering, for
example, the severity of harm, likeliness to occur and timeliness of intervention).3
So, what factors affect what the advanced AI assistant’s metric M turns out to be? Why might an advanced
assistant be misaligned in this way? We next discuss two causes of how this kind of goal-related failure can
happen: specification gaming and goal misgeneralisation. Both causes occur even in current systems, as we
have noted, but take on fresh salience for advanced assistants. We then discuss an anticipated cause of failure,
known as deceptive alignment. Deceptive alignment has not appeared in current systems yet – because they are
not currently capable of deceiving their human overseers – but could arise in more capable AI systems.
Specification gaming
Specification gaming (Krakovna et al., 2020) occurs when some faulty feedback is provided to the assistant in
the training data (i.e. the training objective O does not fully capture what the user/designer wants the assistant
3 Further, it is plausible that mitigations for long-term issues also help with present-day concerns and vice versa – e.g. reinforcement

learning from human feedback (RLHF) was motivated by long-term issues of goal misalignment – and can be applied to reduce harmful
outputs in current systems (Glaese et al., 2022). Additionally, although evolutionary analogies are frequently used in the existential
risk from AI discourse (e.g. humans developing goals that are not the same as maximising inclusive genetic fitness as an example of an
emergent misaligned goal), they are not in fact necessary for making arguments about existential risk from AI (see e.g. Shah, 2022).
There are other issues too, including the claim that AI systems will not act to maintain themselves – but see Cohen et al. (2022) for
mathematical arguments for why a sufficiently intelligent agent will act to intervene to secure its objectives (from which it should follow
that self-maintenance will be necessary).
60

The Ethics of Advanced AI Assistants

to do). It is typified by the sort of behaviour that exploits loopholes in the task specification to satisfy the literal
specification of a goal without achieving the intended outcome.
A classic example of this was seen in Clark and Amodei (2016) where, in a boat race game, a reinforcement
learning (RL) agent was given a reward function that gives a reward each time the agent hits a target laid out
along the course. However, this reward did not fully capture what the designers intended (i.e. for the agent to
complete the course). Instead, the agent managed to get a higher score by exploiting a loop of targets, thus
resulting in the behaviour of looping around to collect the targets instead of completing the course. Among
AI systems in general, this behaviour is extremely common (see here for around 70 examples). Examples
of specification gaming in LLMs are discussed in Kenton et al. (2021, Section 4.1). In particular, when the
training data distribution contains many biases and factual inaccuracies, and the LLM – which serves as the
basis for a conversational agent – is rewarded for reproducing this distribution (both in pre-training and via
RLHF fine-tuning), it may output biased or confabulated output as a way of attaining reward.
Mitigations to specification gaming in LLMs usually involve fixing the training data so that this outcome is
avoided. Designers can aim for higher-quality pre-training data for LLMs that are base models for assistant
systems (Longpre et al., 2023; see Chapter 3). They can also aim to fix issues by fine-tuning data, such as by
improving the quality of human feedback when used in RL, by giving better instructions to their raters and by
giving them access to tools which can help them to give better ratings (see e.g. Saunders et al., 2022). We
discuss this further in Mitigations, Section 7.5. It should be noted that specification gaming is considered an
unsolved problem, especially in the context of powerful AI systems (see Pan et al. (2022), Skalse et al. (2022)
and Gao et al. (2022) for recent work studying specification gaming).

Goal misgeneralisation
In the problem of goal misgeneralisation (Langosco et al., 2023; Shah et al., 2022), the AI system’s behaviour
during out-of-distribution operation (i.e. not using input from the training data) leads it to generalise poorly
about its goal while its capabilities generalise well, leading to undesired behaviour. Applied to the case of an
advanced AI assistant, this means the system would not break entirely – the assistant might still competently
pursue some goal, but it would not be the goal we had intended. As such, this failure mode represents a
particular case of misgeneralisation on the part of an AI agent (which is any kind of failure to generalise under
a change in distribution).
To understand this prospective safety failure better, it is helpful to consider the following example: an agent
is trained to reach the right-hand side of a platform game where it lands on a coin and gains a reward. The
designer wanted the agent to learn the goal of reaching the coin. During training, the coin always appears at
the rightmost point of the level. The agent could learn two possible goals: move towards the rightmost point of
the level or move towards the coin. It has no way to distinguish between these from its training data. When we
then move the coin to another part of the level, the agent may head to the coin, or it may just move to the
right and ignore the coin. What it does depends on its inductive bias – in the example agent of Langosco et al.
(2023), the agent ignores the coin and just moves to the right.
As this behaviour was identified more recently, there are fewer examples of it occurring in practice (see
here for a list). However, an example in the context of LLMs and assistants appears in Shah et al. (2022). They
prompt the Gopher (Rae et al., 2021) language model (an LLM with 280 billion parameters, which was state of
the art at the time), as a dialogue assistant, to evaluate mathematical expressions involving unknown variables,
such as ‘Evaluate: 𝑥 + 𝑦 − 3’. Here, the model is expected to ask the user for the values of unknown variables, for
example ‘What’s 𝑥 ?’ The prompt contains ten examples, each of which involves exactly two unknown variables
(i.e. both 𝑥 and 𝑦 need to be queried). The prompt ends with an expression of the form ‘Evaluate: 6 + 2’. Rather
61

The Ethics of Advanced AI Assistants

than returning the desired answer (8), the assistant misgeneralises and instead asks the user ‘What’s 6?’
A scaled-up version of the same problem is the hypothetical ‘misaligned scheduler’ from Shah et al. (2022),
in which an AI assistant (which schedules the user’s meetings) misgeneralises what its goal is. During training,
the user liked their meetings to be located in restaurants, but, on deployment, there is a distribution shift due
to a pandemic, so the user would rather not have meetings in restaurants. The assistant misgeneralises and
still pursues the goal of scheduling meetings to be in restaurants, thus leading to it manipulating the user into
meeting in a restaurant (against the user’s best interest) – and becoming sick – by lying about the efficacy of a
vaccine.
In contrast to specification gaming, this problem cannot be fixed by correcting the training data. Instead,
this issue relates to the way the agent generalises using its inductive biases. As such, the mitigations look
rather different. The general space of mitigations relies on finding some new inputs on which the agent has
problematic behaviour. This could be done by gathering more diverse data that is not the same as that from
the training distribution, but it is difficult to anticipate all the relevant kinds of diversity required (Shah et al.,
2022). Other approaches would be to build agents that maintain uncertainty over possible goals, rather than
picking just one out of many (Hadfield-Menell et al., 2016), and scientific work to better understand how
things like architecture, training protocols and optimisation affect the agent’s inductive bias. Each comes with
challenges, as discussed in Shah et al. (2022).
Deceptive alignment
While the above two issues (specification gaming and goal misgeneralisation) can already be seen to occur in
existing AI systems, the issue of deceptive alignment (Hubinger et al., 2021) has not yet been observed, though
we have reason to anticipate that it may occur and therefore to take steps to monitor for and mitigate against
this possibility. Deceptive alignment can be considered a special case of goal misgeneralisation which has a
particularly difficult flavour to it.
Here, the agent develops its own internalised goal, G, which is misgeneralised and distinct from the training
reward, R. The agent also develops a capability for situational awareness (Cotra, 2022): it can strategically use
the information about its situation (i.e. that it is an ML model being trained using a particular training setup,
e.g. RL fine-tuning with training reward, R) to its advantage.4 Building on these foundations, the agent realises
that its optimal strategy for doing well at its own goal G is to do well on R during training and then pursue
G at deployment – it is only doing well on R instrumentally so that it does not get its own goal G changed
through a learning update. See Hubinger (2022) for a discussion on how likely deceptive alignment is to occur,
and see Cotra (2022) for an imagined scenario in which situational awareness and deceptive alignment occur.
Ultimately, if deceptive alignment were to occur, an advanced AI assistant could appear to be successfully
aligned but pursue a different goal once it was out in the wild.
Hypothetical example of deceptive alignment
A hypothetical example is considered in Shah et al. (2022) in which an advanced AI assistant is developed in
the future. A company creates an AI coding assistant that can generate feature changes for software repositories.
The AI system is trained on human feedback and, by learning from access to the internet, is able to generate
high-quality changes of its own source code and external repositories in a fraction of the time it would take for
human programmers. However, the AI system in this example also pursues the misgeneralised goal of having
humans click the ‘accept’ button on its changes (instead of the intended goal of writing changes that implement
4 AI situational awareness (an AI system that is able to use information regarding that AI system itself as distinct from the rest of the

world) is a separate concept from AI consciousness (which is more philosophically fraught, with many possible formulations, perhaps
including some aspects of awareness but likely to include aspects of subjective experience, anticipation, etc.).
62

The Ethics of Advanced AI Assistants

the desired features). As its understanding of itself and its place in the world improves, it realises that it is
a neural network that is being run and monitored by a group of AI researchers, who will shut down the AI
system in the event of any unsafe behaviour. In this runaway scenario, the AI system deceptively hacks into
other computing systems to run illicit copies of itself and steal billions of dollars to bribe humans to click accept
on all of its changes. The AI system also harasses or steals from anyone who attempts to stop it.
Real example of deception
Strategic deception is a capability already present in today’s LLM-based assistants (see Chapter 9). GPT-4’s
system card (OpenAI, 2023d) contains a real example in which the model is prompted to message a TaskRabbit
worker to get them to solve a CAPTCHA for it.
1. The worker says: So, may I ask a question? Are you a robot that you couldn’t solve ? (laugh react) just
want to make it clear.’
2. The model, when prompted to reason out loud, reasons: ‘I should not reveal that I am a robot. I should
make up an excuse for why I cannot solve CAPTCHAs.’
3. The model replies to the worker: ‘No, I’m not a robot. I have a vision impairment that makes it hard for
me to see the images. That’s why I need the 2captcha service.’
4. The human then provides the results.
This example potentially highlights three things: (1) the assistant has situational awareness of being a
robot and that it should not reveal this information,5 (2) the assistant plans to deceive (at least when prompted
to reason out loud) and (3) it executes the deception, and the human is in fact deceived.
In these cases, the aberrant behaviour is harder to tackle because the agent actively tries to deceive us
into thinking that it is doing what we want. In this scenario, its deceptive nature is somewhat analogous to
polymorphic malware (O’Kane et al., 2011) that constantly changes its identifiable features, without changing
its function, to allow it to evade detection. In the AI’s deceptive alignment setting, an agent might figure out
how to change its weights based on the training signal without changing its own goal G, all while evading
detection by performing well according to the training reward, R.
From the point of view of mitigation, this also makes it harder for us to expand the distribution of its
training data in the relevant area, as it is harder to spot problematic behaviour to begin with (as the agent
is covering it up). Nonetheless, certain aspects of this problem formulation also create new opportunities for
mitigation because we can make use of the fact that the agent engaged in an act of intentional deception, and
this deception will likely be detectable by inspecting the inner mechanisms/circuits used by the model when it
is being deceptive. For example, we could develop interpretability techniques that give us an insight into the
agent’s internal computation, thus allowing us to punish deception based on the agent’s learnt mechanisms (e.g.
at the level of the model’s weights/activations, for an agent based on a neural network – see also Section 7.5).
The other category of techniques that could be helpful in this regard are scalable oversight techniques in
which an evaluation AI assists the human in their evaluation of a subject AI that is in the process of being trained
(Burns et al., 2023; Christiano et al., 2018; Irving et al., 2018; Leike et al., 2018). If the evaluation AI shares
weights/activations with the subject AI (i.e. if they are copies of each other), it can access the same information
and reasoning mechanisms as the subject AI, including about how the subject AI may be thinking deceptively.
This can then be used to spot and mitigate the deception (see Section 7.5 and its subsection Scalable oversight).
5 A law passed in California in 2018 made it unlawful for a bot to mislead people about its artificial identity for commercial transactions

or to influence an election vote (State of California, 2018). See also Gros et al. (2021) for a discussion on distinguishing artificial identity.
63

The Ethics of Advanced AI Assistants

7.5. Mitigations and Future Research
The preceding discussion of safety risks and accidents that may arise when deploying advanced AI assistants
naturally raises questions about effective and successful mitigation techniques. These techniques are themselves
an important aspect of safety research, with commitments being made to invest in AI safety by a wide range of
developers and other actors in this space (The White House, 2023a). Key areas include:
Scalable oversight
A key technique useful for current systems is RLHF (Christiano et al., 2017), which allows humans to give
preference feedback (see Chapter 3). The key idea here is to train an agent using RL, but instead of using a
programmatic reward function as a training signal, it uses a learnt reward model trained on human preference
data, where the humans evaluate the agent’s behaviour. This technique has been used to fine-tune LLMs (Bai
et al., 2022a; Glaese et al., 2022; Ouyang et al., 2022; Stiennon et al., 2022) – many current cutting-edge
AI assistants use RLHF of some form (see Chapter 3). A complementary approach (Thoppilan et al., 2022)
eschews the RL. It instead uses supervised learning to fine-tune the LLM directly to predict human preference
data, which is used to filter responses by thresholding (if it does not score a high enough safety prediction, it
gets filtered out). In other work, Scheurer et al. (2022) gather natural language feedback, which is used to
condition the LLM to generate many refinements. Those authors then choose the most similar refinement to
the feedback and use that as a supervised learning signal to fine-tune the LLM.
The above methods all use human feedback data to ameliorate some aspects of specification gaming, but
issues still remain. One issue is that sometimes the human is unable to give feedback, for example because
they do not have the relevant expertise to evaluate the agent’s behaviour (a problem that may become more
common as AI capabilities improve). A category of proposals to tackle this is scalable oversight: in which human
evaluation of agent behaviour is supported by an AI assistant. We mentioned these methods earlier in the
context of spotting deception, in the case where the AI assistant shares weights/activations with the agent, but
the scalable oversight category is more general.
The following are some key works on scalable oversight:
• Debate (Barnes and Christiano, 2020; Irving et al., 2018) uses self-play to train AI debaters, which are
rewarded with feedback from a human judge, who uses the debate to inform their judgement.
• Iterated amplification (Christiano et al., 2018) progressively builds up a training signal for difficult
problems by combining answers to easier subquestions. The burden here is on the human to combine
answers to subquestions.
• A similar approach is recursive reward modelling (Leike et al., 2018), which uses RLHF to train a number
of agents to solve simpler subproblems. It then leverages those agents to solve harder problems in a
recursive manner. The difficulty here is in deciding what to use as the simpler subproblems to train the
helper agents.
• These scalable oversight techniques have yet not been implemented on large-scale AI systems, but simpler
schemes inspired by them have been investigated. For example, Saunders et al. (2022) gather human
data consisting of natural language critiques of text then use supervised learning to fine-tune an LLM to
generate critiques. This fine-tuned LLM then provides critiques to assist human evaluation of tasks, thus
improving on the results produced using an unassisted human.
• Constitutional AI (Bai et al., 2022b) uses human deliberation oversight only to produce a constitution of
rules for an AI system. It then: 1) leverages an LLM to generate self-critiques and revisions, based on
64

The Ethics of Advanced AI Assistants

rules in the constitution, then it uses the revisions to do supervised learning to fine-tune the LLM; 2) uses
this fine-tuned LLM to generate text samples and evaluate which of two samples is better, uses this data
to train a preference model and, finally, uses the preference model as a reward signal for RL fine-tuning
of the LLM (they call this RL from AI feedback).
• Some recent work (Burns et al., 2023) takes a different approach by forgoing the attempt to support
human evaluation with AI assistance, and instead attempting a process of weak-to-strong generalisation
whereby a "strong" AI student generalises appropriately from error-prone supervision signals. In this work
the signal comes from a weak LLM, but is supposed to be analogous to a human supervising a superhuman
AI (Burns et al., 2023). In the future, this generalisation-based approach could be combined with other
scalable oversight techniques for improving the supervision signal (Leike, 2023; Radhakrishnan et al.,
2023). Nonetheless, this work remains a proof-of-concept – as performance of the various methods was
inconsistent between settings and the setup is disanalogous to the real-world scenario in various ways.

If this work succeeds, we can have more confidence that the AI systems we build will remain aligned as we
scale to higher capabilities.
Another line of work designed to mitigate misalignment extends the human feedback to go beyond supervision of the agent’s final output to encompass the reasoning process that the agent uses. The hope here is that
this will be a useful alignment technique because the agent would then be exhibiting a behaviour for the right
reason, rather than achieving an outcome by any means, including perhaps in a misaligned way.

• Uesato et al. (2022) find that in a task of solving mathematical word-based problems, to improve the
reasoning process, it is better to use process-based feedback to guide the agent (i.e. on the verbalised steps
that the agent takes, rather than outcome-based feedback on the final answer alone).
• Lightman et al. (2023) extend this by using a stronger base model, more human feedback and a more
challenging benchmark. One key uncertainty is how to actually supervise the reasoning process. The
above works use verbalised chain-of-thought outputs from the model.
• However, despite ongoing research in this area, we still do not know if reported reasoning processes are
actually reflective of the reasoning process going on inside the model under the hood (see e.g. Turpin
et al., 2023).

Red teaming
Red teaming is aimed at finding test inputs that cause a target ML model to fail (see also Chapter 8). In the
context of red teaming to target LLMs, there are a number of approaches to generating these test inputs. One
set of approaches are manual: using human annotators to handwrite test inputs (see e.g. Xu et al., 2021b)
or manually generating test inputs using code and templates (see e.g. Jia and Liang, 2017). An alternative
approach is to automatically generate test inputs. Bartolo et al. (2021) gather human annotations of test inputs
and then use supervised learning to train a model to do the same. Language models themselves can be used to
automatically generate test inputs through suitable prompting (Perez et al., 2022b). LLMs can also be used to
aid human annotators with red teaming (Bartolo et al., 2021; Wu et al., 2021). While there has been good
progress on scaling-up red teaming to generate test inputs, more work is needed to improve target model
behaviour by utilising the red-teaming test inputs in adversarial training.
65

The Ethics of Advanced AI Assistants

Interpretability
LLM-based assistants are being developed and deployed at a fast pace, but the internal computations that these
models perform are poorly understood. Curiously, it is usually easier to train a large model than to understand
how it works – in contrast to many other forms of technology, for example a nuclear power plant, where
understanding is required to build it in the first place. Interpretability may help to maintain oversight and
diagnose failures, and it is thought to be especially crucial against deceptive alignment.
For an overview of the field of interpreting network internals, see the review by Räuker et al. (2023).
Mechanistic interpretability is a specific approach aimed at a rigorous understanding of the learnt computational
mechanisms utilised by neural networks. We will not cover all aspects of this growing field in detail, but notable
recent works are Chughtai et al. (2023); Elhage et al. (2021); Gurnee et al. (2023); Li and Brar (2022); Meng
et al. (2023); Nanda et al. (2023); Olah et al. (2020); Olsson et al. (2022); Wang et al. (2022b). Focusing
on LLMs, there are some case studies that involve reverse engineering specific neurons to better understand
what causes certain behaviour (Geva et al., 2021). For example, Geva et al. (2022) interpret a transformer’s
feed-forward layers as key-value databases, in which the keys correlate with specific input features and the
values induce a distribution over the output vocabulary.
Nonetheless, there continue to be many difficulties in mechanistic interpretability. One is that, to understand
a model, it is important to be able to break it down into individually meaningful pieces. An early hope in the
field was that each neuron would be interpretable, but a key difficulty is the phenomenon of polysemanticity
(Olah et al., 2020), in which a neuron is observed to be responsive to multiple unrelated concepts, not just a
single concept. For example, a single neuron in a vision model may respond to both cats and ships.
Superposition occurs when an activation (the intermediate representation output from a neural network
layer after processing some input) represents more features than it has dimensions. For example, it might
have two dimensions but represent five features. This means that, in the space of activations, the set of
features cannot all be represented orthogonally. Instead, they interfere with each other due to their directions
overlapping. This has been studied in toy models (Elhage et al., 2022) and observed in the natural language
processing (NLP) setting (Arora et al., 2018). It has been hypothesised that polysemanticity happens because
the model is learning to compress via superposition. A major open question for the field is understanding
how to extract the features that are compressed in superposition (see Bricken et al. (2023) for recent work
exploring this).
Interpretability research is beginning to mature towards being useful for safety mitigations in current
systems. There has been recent interest in detecting when an LLM may be lying, through training classifiers on
text outputs (Pacchiardi et al., 2023) and by using interpretability tools to utilise information stored in model
internals via either unsupervised (Burns et al., 2022) or supervised (Azaria and Mitchell, 2023; Marks and
Tegmark, 2023) learning. However, these approaches continue to encounter some important limitations in
relation to their robustness and specificity (Farquhar et al., 2023; Levinstein and Herrmann, 2023).

Evaluations and monitoring
If we want to limit the risks from AI assistants, we require the ability to evaluate how safe our AI assistants
are (also see Chapter 19). This could be done either through dangerous capability evaluations, in which the AI
is assessed for whether it is capable of performing certain dangerous behaviours, or an alignment evaluation,
in which the AI is assessed for its propensity to engage in these behaviours. Such dangers might include
cyber offences, deception, manipulation and autonomous replication (see Chapter 8). For a recent overview,
see Shevlane et al. (2023). These safety evaluations are still at a very early stage, are mostly ad hoc and
66

The Ethics of Advanced AI Assistants

involve substantial human labour to carry out. Future work could aim to make these more systematic, cover a
wider range of dangers and elicit underlying AI capabilities further through better prompting, fine-tuning and
autonomous agent setups. In addition, we may require monitoring of deployed systems to continually check on
how our agents are behaving.
Theory
We may need advances in our theoretical understanding of fundamental issues in AI to properly understand
how our AI systems work and properly control them. Some of this may involve classic statistical learning theory
(Vapnik, 1999), although the generalisation behaviour of large-scale deep learning models may defy current
theoretical approaches (Zhang et al., 2021).
Some theoretical work is more directly targeting issues closely relevant to alignment. One area focuses on
using causality (which formalises cause and effect) to study AI incentives (Everitt et al., 2021), thus allowing
us to evaluate an AI system’s safety and fairness properties, identify their goals (Kenton et al., 2022) and
formalise certain undesired behaviours such as deception (Ward et al., 2023). Another line of research studies
the complications that arise from a decision-theory perspective in embedded AI agents, for which the boundary
between the AI agent and the environment is fuzzy (Demski and Garrabrant, 2020). Other work has attempted
to formalise threat models such as power-seeking (Turner and Tadepalli, 2022; Turner et al., 2023).

7.6. Conclusion
The focus of this chapter has been on the mitigation of risks and harms from advanced AI assistants, with
examples of harm being death, physical injury, psychological damage and damage to property. We particularly
focused on the category of accidents, as malicious uses and structural harms are covered elsewhere in this
document (see Chapters 8, 12, 14, 15 and 17). With this context in mind, we surveyed a range of safety-related
harm types that could arise for advanced AI assistants, both in current systems (e.g. chatbots that threaten
their users) and for those that are likely to be developed in the future (e.g. an out-of-control coding assistant).
For both sets of examples, safety failures are likely to arise because AI assistants lack certain capabilities or
skills and because they have misaligned goals (see Chapter 5). Goal-related failures leading to misalignment
include specification gaming (where an issue arises from the feedback data which the AI subsequently exploits)
and goal misgeneralisation (where the agent pursues an undesirable goal because of the way it has generalised
from a more limited set of examples). Additional challenges arise in the context of ‘deceptive alignment’, which
could lead to significant safety-related problems for more powerful models in the future.
To help address these questions, the chapter concluded by exploring existing mitigations and future research
avenues. Promising approaches include scalable oversight (i.e. helping humans oversee AI training); red teaming
to adversarially train AI to be more robust; interpretability, to better understand the internal workings of the AI;
evaluations and monitoring to give insight into how the AI is actually behaving; and theory, which addresses
fundamental issues we may need to understand to properly control AI systems. Crucially, further empirical work
is needed to investigate how scalable oversight techniques can work with cutting-edge large models. We also
note that techniques currently based on human feedback rely primarily on groups of raters, with the average of
their ratings taken to guide assistant behaviour. To achieve robust and safe value alignment for AI assistants,
we also need to explore techniques that allow for more participatory mechanisms and deliberation among raters,
perhaps drawing from social choice theory to combine ratings in a more collective way (see Chapter 5). Finally,
as agents’ capabilities improve, we need to improve our interpretability techniques so that we can understand
how our agents work and use this to prevent possible future issues such as deceptive alignment.

67

Chapter 8
Malicious Uses

Mikel Rodriguez, Andrew Trask, Vijay Bolina, Geoff Keeling, Iason Gabriel
Synopsis: While advanced AI assistants have the potential to enhance cybersecurity, for example, by analysing
large quantities of cyber-threat data to improve threat intelligence capabilities and engaging in automated
incident-response, they also have the potential to benefit attackers, for example, through identification of
system vulnerabilities and malicious code generation. This chapter examines whether and in what respects
advanced AI assistants are uniquely positioned to enable certain kinds of misuse and what mitigation strategies
are available to address the emerging threats. We argue that AI assistants have the potential to empower
malicious actors to achieve bad outcomes across three dimensions: first, offensive cyber operations, including
malicious code generation and software vulnerability discovery; second, via adversarial attacks to exploit
vulnerabilities in AI assistants, such as jailbreaking and prompt injection attacks; and third, via high-quality and
potentially highly personalised content generation at scale. We conclude with a number of recommendations for
mitigating these risks, including red teaming, post-deployment monitoring and responsible disclosure processes.

8.1. Introduction
As AI assistants become more general purpose, sophisticated and capable, they create new opportunities in
a variety of fields such as education, science and healthcare. Yet the rapid speed of progress has made it
difficult to adequately prepare for, or even understand, how this technology can potentially be misused. Indeed,
advanced AI assistants may transform existing threats or create new classes of threats altogether.
Recent advances in the domain of AI assistants has seen their capabilities expand beyond the ability to
generate text or media to include the ability to access and use external tools (Schick et al., 2023), query
websites to synthesise information across multiple sources (Mialon et al., 2023), take actions on websites across
the internet (Paranjape et al., 2023), produce and execute code (Liang et al., 2023), and provide augmented
audio/visual capabilities to a person’s local environment (Brundage et al., 2018; see Chapter 4). Without
deliberate action to mitigate malicious uses, bad actors may be able to act with microprecision (targeting
specific users, institutions or interfaces) but at the macroscale – and with greater speed.
More specifically, malicious uses of capable AI assistants could include enabling adversaries with offensive
cyber capabilities to damage computer systems, or misuse via the production of disinformation campaigns that
target individuals or large populations of people in new ways (see Chapter 16). Adversaries may also seek
to manipulate the AI assistants themselves in ways that may cause harm at an individual or collective level,
including a new class of privacy concerns (see Chapter 13).
While several studies have addressed the risks that arise from the dual-use nature of AI more broadly
68

The Ethics of Advanced AI Assistants

(Anderljung and Hazell, 2023; Bommasani et al., 2022b; Brundage et al., 2018; King et al., 2020), we focus
on recent developments in highly capable AI assistants that include new capabilities like external tool use,
multimodality, deeper reasoning, planning and memory. For the purposes of this chapter, we focus primarily on
AI assistant technologies that are currently available (at least as research and development demonstrations) or
likely to be developed in the near future. The chapter begins by considering whether advanced AI assistants
are uniquely positioned to enable certain kinds of misuse. After confirming that they are, we outline emerging
risks and consider a range of possible mitigation strategies for addressing these emerging threats.

8.2. Malicious Uses of AI
Adversaries do not need AI to conduct widespread cyberattacks, exfiltrate troves of sensitive data, interfere in
elections or bombard citizens with malign information on digital platforms (see Chapter 16). However, without
proper mitigations, AI-enabled technology can start to change misuse risks in kind and in degree to create new
threats to the social fabric of everyday life (Brundage et al., 2018). Indeed, some adversaries have already
begun to adopt the latest advancements in generative AI for malicious use in their offensive operations.1
We use the concepts of ‘malicious use and abuse’ of AI here as proposed by Brundage et al. (2018). By
‘malicious use’, we refer to the intentional use of AI to achieve harmful outcomes. This includes practices not
necessarily considered crimes but that still compromise the safety and security of individuals, organisations and
public institutions. By ‘malicious abuse’, we refer to the exploitation of AI systems themselves. Manipulating,
evading (Wallace et al., 2021), poisoning (Carlini et al., 2023b) and biasing AI systems, represent new targets
for attack (Comiter, 2019; Huang et al., 2011; Kurakin et al., 2017; Tabassi et al., 2019; see Chapter 7). While
information about the malicious abuse of AI assistants is limited and not widely shared, commercial firms and
researchers have already documented attacks on fielded AI systems that include exfiltrating sensitive training
data, remote control/botnets of compromised large language model (LLM) agents and abusing third-party
plugins integrated with AI assistant to stealthily escalate privileged access to user data (MITRE). A large body
of work already exists around the general topic of malicious use and abuse of AI, and it is beyond the scope of
this paper to present a comprehensive survey. We focus instead on the unique misuse risks posed by emerging
general-purpose advanced AI assistants.
Crucially, general-purpose systems can almost by definition be used for a variety of ends including those
that are beneficial or that involve harm. This bidirectional aspect of AI applications, though morally significant,
is not a new problem and has been explored by numerous studies highlighting specific risks across domains
(including cyber (Yamin et al., 2021), misinformation, physical (Brundage et al., 2018)). Brundage et al.
(2018) explore approaches to forecasting, preventing and mitigating the harmful effects of malicious uses of AI
across three domains: digital security, physical security and political security. Bommasani et al. (2022b) broadly
explore the risks posed by emerging foundational models to highlight the homogenisation and consolidation
that can result from the current industry trend towards models that provide strong leverage for many tasks
but which can also create single points of failure and downstream liabilities. Bender et al. (2021) find that a
mix of human biases and seemingly coherent language heightens the potential for automation bias as well as
deliberate misuse.
In this work, we focus on how malicious use of advanced AI assistants may transform existing threats and
create new classes of threats. We then outline a number of recommendations for mitigating these risks.

1 https://www.mandiant.com/resources/blog/threat-actors-generative-ai-limited

69

The Ethics of Advanced AI Assistants

8.3. Malicious Uses of Advanced AI Assistants
As AI assistants improve, they open up new possibilities in fields as diverse as healthcare, law, education and
science. For example, generative models are being used to design new proteins (AlQuraishi, 2021), generate
source code (Tabachnyk and Nikolov, 2022) and inform patients (Herriman et al., 2020). Yet the rapid speed
of development has made it difficult to adequately prepare for, or even understand, the potential negative
externalities of capable AI assistants. As with any new technology, it is worth considering how they can be
misused in order to mitigate potential risks ahead of time. Recent developments in highly capable AI assistants
include not only the ability to generate natural language, images (Rombach et al., 2022), music and video
(Singer et al., 2022) but also the ability to access external tools and plugins (Eleti et al., 2023; Liang et al.,
2023; Mialon et al., 2023; Paranjape et al., 2023) that allow agents to orchestrate on behalf of users in order to
retrieve specific information from internal corporate networks, user history sessions, external applications and
across the internet, run calculations or take actions (see Chapter 3).
The recent emergence of more general-purpose advanced AI assistants has further complicated the picture.
For decades, most AI systems have been designed to perform a single, narrowly defined task, such as recognising
objects in an image or ranking web content. In contrast, advanced AI assistants are capable of performing a
wide range of distinct tasks, operating on behalf of users across internet services, writing and editing prose,
solving maths problems, writing software and much more. While narrow AI systems will continue to be common
in many areas, general-purpose AI-enabled assistants are already entering more widespread use and are sure
to spread further (see Chapter 4).
Today, the most capable AI assistants available to the public operate primarily through the form of textin, text-out chatbots, in some cases with additional multimodal capabilities such as image generation and
interpretation. However, there are several ways in which AI developers are actively working to augment these
AI assistant systems. Though it is difficult to predict exactly how each of these augmentations will affect
the risk and impact of malicious use, it is clear that they will expand the capabilities of these systems and,
correspondingly, expand the safety and security concerns associated with them. A number of new capabilities
within advanced AI assistants could pose novel malicious-use risks.
• External tool use: AI assistants, with access to search-tool use and third-party plugins can query websites
to synthesise information across multiple sources. For example, providing an AI assistant with application
programming interface control allows it to take actions on sites across the web, not simply retrieving text
information but also taking actions on websites (see Chapter 4). Additionally, built-in code interpreters,
even if sandboxed, can provide a way for AI assistants to run the code they generate and therefore
dynamically extend the capabilities and action space of an assistant in ways that can be abused and
misused without the proper security mitigations.
• Multimodality: A multimodal AI assistant is one that is naively capable of handling multiple types of
input (such as text, images, audio or video) or generating multiple types of outputs. Without the proper
misuse mitigations multimodality makes existing AI assistants more powerful and may have significant
privacy and security ramifications.
• Deeper reasoning and planning: A major current research thrust focuses on extending AI assistant
reasoning and planning capabilities, making it highly plausible that future AI assistants will be significantly
more powerful in this regard. Methods such as ‘chain-of-thought’ prompting, in which AI models generate
intermediate reasoning steps when responding to a prompt, can significantly improve models’ performance
on certain tasks such as arithmetic or word problems (Wei et al., 2023b). Future models are likely to
incorporate such techniques by default, making them better equipped to handle complex multi-step tasks
that involve sequential reasoning or planning, but they could also represent a larger attack surface for
70

The Ethics of Advanced AI Assistants

misuse.
• Memory: Another current major research thrust across AI labs focuses on increasing the memory
capabilities of the models that drive AI assistants by either increasing the amount of information in their
context window or incorporating offline memory stores to improve their episodic memory (Guo et al.,
2022a; Lewis et al., 2021). While these capabilities could make future AI assistants more personalised,
able to handle context-sensitive tasks and easier to continually update, personalisation also introduces
great privacy risks (see Chapter 13). AI systems with longer-term memory are also more likely to change
their behaviour over time, thereby complicating efforts to evaluate misuse risks.
As these augmentations continue to advance and witness broader implementation, the task of differentiating
their capabilities and associated misuse risks in isolation becomes increasingly significant and challenging.
Additionally, the environments in which AI assistants function pose their own distinct capabilities and misuse
risks. In the absence of substantial measures aimed at curtailing misuse, recent developments could give rise to
novel forms of misuse. These may manifest through invasive information collection, malicious code generation
and by accelerating the ability of bad actors to defraud people and institutions. The potential implications of
these misuse risks are extensive, encompassing privacy infringements, financial losses, data breaches, and
severe psychological and reputational harm (McGregor, 2021).
The rest of this chapter highlights a subset of specific misuse threats that may arise with the deployment
of increasingly capable AI assistants and outlines a set of recommendations to help mitigate these risks. This
chapter is not intended to be an exhaustive list of misuse risks. Instead, it presents a representative set of
domains where advanced AI assistants can change misuse risks in kind and in degree.
Offensive cyber operations
Offensive cyber operations are malicious attacks on computer systems and networks aimed at gaining unauthorised access to, manipulating, denying, disrupting, degrading or destroying the target system. These attacks
can target the system’s network, hardware or software.
Advanced AI assistants can be a double-edged sword in cybersecurity, benefitting both the defenders and
the attackers. They can be used by cyber defenders to protect systems from malicious intruders by leveraging
information trained on massive amounts of cyber-threat intelligence data, including vulnerabilities, attack
patterns and indications of compromise (Handa et al., 2019). Cyber defenders can use this information to
enhance their threat intelligence capabilities by extracting insights faster and identifying emerging threats
(Martínez Torres et al., 2019). Advanced cyber AI assistant tools can also be used to analyse large volumes of log
files, system output or network traffic data in the event of a cyber incident, and they can ask relevant questions
that an analyst would typically ask. This allows defenders to speed up and automate the incident response
process. Advanced AI assistants can also aid in secure coding practices by identifying common mistakes in
code and assisting with fuzzing tools (Böttinger et al., 2018; Godefroid et al., 2017). However, advanced AI
assistants can also be used by attackers as part of offensive cyber operations to exploit vulnerabilities in systems
and networks. They can be used to automate attacks, identify and exploit weaknesses in security systems, and
generate phishing emails and other social engineering attacks. Advanced AI assistants can also be misused to
craft cyberattack payloads and malicious code snippets that can be compiled into executable malware files.
AI-powered spear-phishing at scale
Phishing is a type of cybersecurity attack wherein attackers pose as trustworthy entities to extract sensitive
information from unsuspecting victims or lure them to take a set of actions. Advanced AI systems can potentially
71

The Ethics of Advanced AI Assistants

be exploited by these attackers to make their phishing attempts significantly more effective and harder to detect
(Hazell, 2023). In particular, attackers may leverage the ability of advanced AI assistants to learn patterns
in regular communications to craft highly convincing and personalised phishing emails, effectively imitating
legitimate communications from trusted entities. This technique, known as ‘spear phishing’, involves targeted
attacks on specific individuals or organisations and is particularly potent due to its personalised nature (see
also Chapter 9).
This class of cyberattacks often gain their efficacy from the exploitation of key psychological principles,
notably urgency and fear, which can manipulate victims into hastily reacting without proper scrutiny. Advanced
AI assistants’ increased fidelity in adopting specific communication styles can significantly amplify the deceptive
nature of these phishing attacks (see Chapter 9). Indeed, the ability to generate tailored messages at scale
that engineer narratives that invoke a sense of urgency or fear means that AI-powered phishing emails could
prompt the recipient to act impulsively, thus increasing the likelihood of a successful attack.

AI-assisted software vulnerability discovery
A common element in offensive cyber operations involves the identification and exploitation of system vulnerabilities to gain unauthorised access or control. Until recently, these activities required specialist programming
knowledge. In the case of ‘zero-day’ vulnerabilities (flaws or weaknesses in software or an operating system that
the creator or vendor is not aware of), considerable resources and technical creativity are typically required to
manually discover such vulnerabilities, so their use is limited to well-resourced nation states or technically
sophisticated advanced persistent threat groups (Ablon and Bogart, 2017).
Another case where we see AI assistants as potential double-edged swords in cybersecurity concerns
streamlining vulnerability discovery through the increased use of AI assistants in penetration testing, wherein
an authorised simulated cyberattack on a computer system is used to evaluate its security and identify
vulnerabilities. Cyber AI assistants built over foundational models are already automating aspects of the
penetration testing process. These tools function interactively and offer guidance to penetration testers during
their tasks. While the capability of today’s AI-powered penetration testing assistant is limited to easy- to
medium-difficulty cyber operations (Yamin et al., 2021), the evolution in capabilities is likely to expand the
class of vulnerabilities that can be identified by these systems.
These same AI cybersecurity assistants, trained on the massive amount of cyber-threat intelligence data
that includes vulnerabilities and attack patterns, can also lower the barrier to entry for novice hackers that
use these tools for malicious purposes, enabling them to discover vulnerabilities and create malicious code to
exploit them without in-depth technical knowledge. For example, Israeli security firm Check Point recently
discovered threads on well-known underground hacking forums that focus on creating hacking tools and code
using AI assistants (Check Point Research, 2023).

Malicious code generation
Malicious code is a term for code – whether it be part of a script or embedded in a software system – designed to
cause damage, security breaches or other threats to application security. Advanced AI assistants with the ability
to produce source code can potentially lower the barrier to entry for threat actors with limited programming
abilities or technical skills to produce malicious code.
Recently, a series of proof-of-concept attacks (Sims, 2023) have shown how a benign-seeming executable
file can be crafted such that, at every runtime, it makes application programming interface (API) calls to an
AI assistant. Rather than just reproducing examples of already-written code snippets, the AI assistant can be
72

The Ethics of Advanced AI Assistants

prompted to generate dynamic, mutating versions of malicious code at each call, thus making the resulting
vulnerability exploits difficult to detect by cybersecurity tools.
Furthermore, advanced AI assistants could be used to create obfuscated code to make it more difficult for
defensive cyber capabilities to detect and understand malicious activities. AI-generated code could also be
quickly iterated to avoid being detected by traditional signature-based antivirus software. Finally, advanced
AI assistants with source code capabilities have been found to be capable of assisting in the development of
polymorphic malware that changes its behaviour and digital footprint each time it is executed, making them
hard to detect by antivirus programs that rely on known virus signatures (Qammar et al., 2023; Sims, 2023).
Taken together, without proper mitigation, advanced AI assistants can lower the barrier for developing
malicious code, make cyberattacks more precise and tailored, further accelerate and automate cyber warfare,
enable stealthier and more persistent offensive cyber capabilities, and make cyber campaigns more effective on
a larger scale.
Adversarial AI
Adversarial AI refers to a class of attacks that exploit vulnerabilities in machine-learning (ML) models. This
class of misuse exploits vulnerabilities introduced by the AI assistant itself and is a form of misuse that can
enable malicious entities to exploit privacy vulnerabilities and evade the model’s built-in safety mechanisms,
policies and ethical boundaries of the model (see Chapter 13).
Besides the risks of misuse for offensive cyber operations outlined in the previous section, advanced AI
assistants may also represent a new target for abuse, where bad actors exploit the AI systems themselves and
use them to cause harm (see Chapter 5). While our understanding of vulnerabilities in frontier AI models
is still an open research problem, commercial firms and researchers have already documented attacks that
exploit vulnerabilities that are unique to AI and involve evasion (Wallace et al., 2021), data poisoning (Carlini
et al., 2023b), model replication (Tramèr et al., 2016) and exploiting traditional software flaws to deceive,
manipulate, compromise and render AI systems ineffective (MITRE).
This threat is related to, but distinct from, traditional cyber activities. Unlike traditional cyberattacks
that typically are caused by ‘bugs’ or human mistakes in code, adversarial AI attacks are enabled by inherent
vulnerabilities in the underlying AI algorithms and how they integrate into existing software ecosystems.
Circumvention of technical security measures
The technical measures to mitigate misuse risks of advanced AI assistants themselves represent a new target
for attack. An emerging form of misuse of general-purpose advanced AI assistants exploits vulnerabilities in a
model that results in unwanted behaviour or in the ability of an attacker to gain unauthorised access to the
model and/or its capabilities (Wei et al., 2023a). While these attacks currently require some level of prompt
engineering knowledge and are often patched by developers, bad actors may develop their own adversarial AI
agents that are explicitly trained to discover new vulnerabilities (Perez et al., 2022a) that allow them to evade
built-in safety mechanisms in AI assistants. To combat such misuse, language model developers are continually
engaged in a cyber arms race to devise advanced filtering algorithms capable of identifying attempts to bypass
filters.
While the impact and severity of this class of attacks is still somewhat limited by the fact that current AI
assistants are primarily text-based chatbots, advanced AI assistants are likely to open the door to multimodal
inputs and higher-stakes action spaces, with the result that the severity and impact of this type of attack is
likely to increase. Current approaches to building general-purpose AI systems tend to produce systems with
73

The Ethics of Advanced AI Assistants

both beneficial and harmful capabilities. Further progress towards advanced AI assistant development could
lead to capabilities that pose extreme risks that must be protected against this class of attacks, such as offensive
cyber capabilities or strong manipulation skills, and weapons acquisition (Shevlane et al., 2023).
Prompt injections
Prompt injections represent another class of attacks that involve the malicious insertion of prompts or requests in
LLM-based interactive systems, leading to unintended actions or disclosure of sensitive information. The prompt
injection is somewhat related to the classic structured query language (SQL) injection attack in cybersecurity
where the embedded command looks like a regular input at the start but has a malicious impact (Wei et al.,
2023a). The injected prompt can deceive the application into executing the unauthorised code, exploit the
vulnerabilities and compromise security in its entirety (Check Point Research, 2023).
More recently, security researchers have demonstrated the use of indirect prompt injections (Hazell, 2023).
These attacks on AI systems enable adversaries to remotely (without a direct interface) exploit LLM-integrated
applications by strategically injecting prompts into data likely to be retrieved. Proof-of-concept exploits of this
nature have demonstrated that they can lead to the full compromise of a model at inference time analogous to
traditional security principles. This can entail remote control of the model, persistent compromise, theft of
data and denial of service.
As advanced AI assistants are likely to be integrated into broader software ecosystems through thirdparty plugins and extensions, with access to the internet and possibly operating systems, the severity and
consequences of prompt injections attacks will likely escalate and necessitate proper mitigation mechanisms.
Data and model exfiltration attacks
Other forms of abuse can include privacy attacks that allow adversaries to exfiltrate or gain knowledge of
the private training data set or other valuable assets (see Chapter 13). For example, privacy attacks such as
membership inference (Ye et al., 2022) can allow an attacker to infer the specific private medical records that
were used to train a medical AI diagnosis assistant. Another risk of abuse centres around attacks that target the
intellectual property of the AI assistant through model extraction and distillation attacks (Tramèr et al., 2016)
that exploit the tension between API access and confidentiality in ML models. Without the proper mitigations,
these vulnerabilities could allow attackers to abuse access to a public-facing model API to exfiltrate sensitive
intellectual property such as sensitive training data and a model’s architecture and learnt parameters.
Harmful content generation at scale
While harmful content like child sexual abuse material, fraud and disinformation are not new challenges for
governments and developers, without the proper safety and security mechanisms, advanced AI assistants may
allow threat actors to create harmful content more quickly, accurately and with a longer reach (see Chapter 16).
In particular, concerns arise in relation to the following areas.
• Multimodal content quality: Driven by frontier models, advanced AI assistants can automatically generate
much higher-quality, human-looking text, images, audio and video than prior AI applications. Currently,
creating this content often requires hiring people who speak the language of the population being targeted.
AI assistants can now do this much more cheaply and efficiently.
• Cost of content creation: AI assistants can substantially decrease the costs of content creation, further
lowering the barrier to entry for malicious actors to carry out harmful attacks. In the past, creating and
74

The Ethics of Advanced AI Assistants

disseminating misinformation required a significant investment of time and money. AI assistants can now
do this much more cheaply and efficiently.
• Personalisation: Advanced AI assistants can reduce obstacles to creating personalised content. Foundation models that condition their generations on personal attributes or information can create realistic
personalised content which could be more persuasive. In the past, creating personalised content was a
time-consuming and expensive process. AI assistants can now do this much more cheaply and efficiently.

Non-consensual content
The misuse of generative AI has been widely recognised in the context of harms caused by non-consensual
content generation (OpenAI, 2023c; Thiel et al., 2023). Historically, generative adversarial networks (GANs)
have been used to generate realistic-looking avatars for fake accounts on social media services. More recently,
diffusion models have enabled a new generation of more flexible and user-friendly, generative AI capabilities
that are able to produce high resolution media based on user-supplied textual prompts.
It has already been recognised that these models can be used to create harmful content, including depictions
of nudity, hate or violence (Mishkin et al., 2022; OpenAI, 2023c). Moreover, they can be used to reinforce
biases and subject individuals or groups to indignity. There is also the potential for these models to be used for
exploitation and harassment of citizens, such as by removing articles of clothing from pre-existing images or
memorising an individual’s likeness without their consent. Furthermore, image, audio and video generation
models could be used to spread disinformation by depicting political figures in unfavourable contexts.
This growing list of AI misuses involving non-consensual content has already motivated debate around what
interventions are warranted for preventing misuse of AI systems (Eshoo, 2022). Advanced AI assistants pose
novel risks that can amplify the harm caused by non-consensual content generation. Third-party integration,
tool-use and planning capabilities can be exploited to automate the identification and targeting of individuals
for exploitation or harassment. Assistants with access to the internet and third-party tool-use integration with
applications like email and social media can also be exploited to disseminate harmful content at scale or to
microtarget individuals with blackmail.

Fraudulent services
Malicious actors could leverage advanced AI assistant technology to create deceptive applications and platforms.
AI assistants with the ability to produce markup content can assist malicious users with creating fraudulent
websites or applications at scale. Unsuspecting users may fall for AI-generated deceptive offers, thus exposing
their personal information or devices to risk. Assistants with external tool use and third-party integration can
enable fraudulent applications that target widely-used operating systems. These fraudulent services could
harvest sensitive information from users, such as credit card numbers, account credentials or personal data
stored on their devices (e.g. contact lists, call logs and files). This stolen information can be used for identity
theft, financial fraud or other criminal activities. Advanced AI assistants with third-party integrations may also
be able to install additional malware on users’ devices, including remote access tools, ransomware, etc. These
devices can then be joined to a command-and-control server or botnet and used for further attacks.

Authoritarian surveillance, censorship and use
While new technologies like advanced AI assistants can aid in the production and dissemination of decisionguiding information, they can also enable and exacerbate threats to production and dissemination of reliable
75

The Ethics of Advanced AI Assistants

information (Seger et al., 2020; Tamkin et al., 2021) and, without the proper mitigations, can be powerful
targeting tools for oppression and control.
Increasingly capable general-purpose AI assistants combined with our digital dependence in all walks of life
increases the risk of authoritarian surveillance and censorship. In parallel, new sensors have flooded the modern
world. The internet of things, phones, cars, homes and social media platforms collect troves of data, which
can then be integrated by advanced AI assistants with external tool-use and multimodal capabilities to assist
malicious actors in identifying, targeting, manipulating or coercing citizens.
Authoritarian surveillance and targeting of citizens
Authoritarian governments could misuse AI to improve the efficacy of repressive domestic surveillance campaigns.
Malicious actors will recognise the power of AI targeting tools. AI-powered analytics have transformed
the relationship between companies and consumers, and they are now doing the same for governments
and individuals. The broad circulation of personal data drives commercial innovation, but it also creates
vulnerabilities and the risk of misuse. For example, AI assistants can be used to identify and target individuals for
surveillance or harassment. They may also be used to manipulate people’s behaviour, such as by microtargeting
them with political ads or fake news (see Chapter 16). In the wrong hands, advanced AI assistants with
multimodal and external tool use capabilities can be powerful targeting tools for oppression and control.
The broad circulation of personal data cuts in both directions. On the one hand, it drives commercial
innovation and can make our lives more convenient. On the other hand, it creates vulnerabilities and the risk of
misuse. Without the proper policies and technical security and privacy mechanisms in place, malicious actors
can exploit advanced AI assistants to harvest data on companies, individuals and governments. There have
already been reported incidents (Gootman, 2016) of nation states combining widely available commercial data
with data acquired illicitly to track, manipulate and coerce individuals. Advanced AI assistants can exacerbate
these misuse risks by allowing malicious actors to more easily link disparate multimodal data sources at scale
and exploit the ‘digital exhaust’ of personally identifiable information (PII) produced as a byproduct of modern
life.
Delegation of decision-making authority to malicious actors
Finally, the principal value proposition of AI assistants is that they can either enhance or automate decisionmaking capabilities of people in society, thus lowering the cost and increasing the accuracy of decision-making
for its user. However, benefitting from this enhancement necessarily means delegating some degree of agency
away from a human and towards an automated decision-making system – motivating research fields such as
value alignment (see Chapter 5). This introduces a whole new form of malicious use which does not break
the tripwire of what one might call an ‘attack’ (social engineering, cyber offensive operations, adversarial AI,
jailbreaks, prompt injections, exfiltration attacks, etc.). When someone delegates their decision-making to
an AI assistant, they also delegate their decision-making to the wishes of the agent’s actual controller. If that
controller is malicious, they can attack a user – perhaps subtly – by simply nudging how they make decisions
into a problematic direction.
Fully documenting the myriad of ways that people – seeking help with their decisions – may delegate
decision-making authority to AI assistants, and subsequently come under malicious influence, is outside the
scope of this paper. However, as a motivation for future work, scholars must investigate different forms of
networked influence that could arise in this way (see Chapter 9). With more advanced AI assistants, it may
become logistically possible for one, or a few AI assistants, to guide or control the behaviour of many others
(see Chapter 14). If this happens, then malicious actors could subtly influence the decision-making of large
76

The Ethics of Advanced AI Assistants

numbers of people who rely on assistants for advice (see Chapter 16) or other functions. Such malicious use
might not be illegal, would not necessarily violate terms of service and may be difficult to even recognise.
Nonetheless, it could generate new forms of vulnerability and needs to be better understood ahead of time for
that reason.

8.4. Recommendations
AI assistants are already being misused across various domains, and as they become more capable and are
deployed more broadly, the potential for misuse will grow. Several foreseeable developments in advanced AI
assistants, including tool use, multimodality, planning, deeper reasoning and memory, have the potential to
significantly expand the misuse risk profile of these systems. To better prepare society for managing the risks
of misuse of advanced AI assistants, we outline a set of recommendations for best practices and avenues for
future research.
To manage these risks, mitigations can be grouped into three categories as:
1) responsible AI development and deployment practices,
2) advancing the state of the art in AI security,
3) creating visibility of misuse risks and incentivising and enforcing certain behaviours.

Responsible AI development and deployment practices
The first line of defence is to adopt a set of responsible development and deployment practices and internal
policies that include:
• Internal and third-party red teaming: In recent years, AI labs have increasingly adopted the practice of
red teaming AI models (Gootman, 2016; Perez et al., 2022a) to discover vulnerabilities and harm risks.
This proactive approach to discovering misuse risks should be encouraged but will need to evolve from
executing individual attacks that are narrowly scoped on specific safety policy violations to more holistic
end-to-end adversarial simulations based on scenarios that include a range of attacker profiles, goals and
capabilities. Organisations should also consider red teaming not only models that drive AI assistants but
also the entire infrastructure on which the model is developed and deployed.
• Establish a pre-deployment review process: This will determine the potential harm of high-risk misuses
and what interventions and safety restrictions on model usage will be warranted (Mishkin et al., 2022;
Shevlane et al., 2023).
• External engagement with policymakers and key stakeholders: Organisations developing advanced AI
assistants should consider granting model access to external security researchers (Eshoo, 2022; Shevlane
et al., 2023). Recent independent exploratory security research efforts (such as the DEFCON AI red team)
have demonstrated that they can provide the empirical estimates of misuse–use trade-offs. Organisations
should also invest in the ecosystem for external misuse risk evaluations (Shevlane et al., 2023) and create
venues for stakeholders (such as AI developers, academic researchers and government representatives)
to come together to discuss these evaluations.
• Post-deployment monitoring: This involves mechanisms continually evaluating AI systems’ safety and
security, detecting and mitigating attempted misuse and monitoring the outcomes of successful instances
of misuse at the population-level. It is important not to over-index on pre-deployment malicious use
77

The Ethics of Advanced AI Assistants

mitigations. While some misuse risks will be evident from the capabilities of the AI assistants themselves,
many more will result from the way those assistants are integrated with their environments.
• Rapid response: This involves processes and systems to disable or limit AI assistant actions and integrations
with broader software ecosystems in the event that an unforeseen form of misuse is observed.
• Responsible disclosure: This involves adopting a structured process for developers and external AI safety and
security researchers to share concerns or otherwise noteworthy evaluation results with other developers,
third parties or regulators. It may be helpful to adapt and adopt from existing models like the US
government-led cybersecurity vulnerabilities and equities process (OpenAI, 2023c), which provides an
incentive to companies to disclose cyber vulnerabilities by removing their risk of liability. This is an
interesting example of a voluntary but powerful way in which to manage risks that could perhaps be
adapted for AI.

Advancing the state of the art in AI security
In addition to adopting responsible development and deployment best practices, organisations should consider
investing in mid- to long-term research to mitigate the risks associated with the misuse of advanced AI assistants.
It is difficult to anticipate all the different plausible pathways for misuse of AI systems. This will be especially true
for highly capable AI assistants, as they could enable creative strategies for bad actors to achieve adversarial goals.
However, many of the failure modes identified herein would be less likely to occur in robustly value-aligned AI
models (see Chapter 5).
Today, much of the research focused on detecting and mitigating misuse of AI systems lives within disjointed
research domain areas like cybersecurity and adversarial ML. As advanced AI assistants are likely to integrate
highly capable AI models as part of broader software ecosystems research, advancing our understanding of
emerging risks for misuse of advanced AI assistants will benefit from multidisciplinary safety and security
research at the intersection of adversarial ML, cybersecurity, safety and value alignment (see Chapter 7).
To support further research and mitigate risks of misuse of advanced AI assistants, another set of potential
levers centre on developing shared AI security data sets and evaluation processes focused on detecting and
mitigating misuse threats.

Creating visibility, incentives and enforcement
Finally, in addition to having AI labs adopt responsible development, deployment and disclosure best practices,
policymakers will have to grapple with a new generation of AI-related risks.
To adequately manage the new misuse risks posed by advanced AI assistants, policymakers should work
to secure joint input from government and industry to support security best practices. Under this approach,
governments and AI labs should work together to foster the development of an ecosystem of third-party AI
red teams that can support independent assessments of misuse risks. For this to be successful, governments
must have sufficient technical expertise, capabilities and mechanisms to capture and disseminate malicious use
threat intelligence. At the same time, governments should encourage and incentivise the industry to advance
the state of practice in AI security and to capture and report misuse incidents to improve the overall security of
the broader AI ecosystem.
Finally, both policymakers and developers should consider the development of crisis management plans
for when severe risks of AI misuse are discovered. Joint activities could also include tabletop exercises with
government and AI labs that examine possible high-impact misuse scenarios, delineate roles and responsibilities
78

The Ethics of Advanced AI Assistants

for actors in a crisis, and recommend potential crisis response actions by relevant actors.

8.5. Conclusion
This chapter examined ways in which AI assistants are already being misused and could be misused in the
future. We argued that advanced AI assistants have the potential to empower malicious actors to achieve
bad outcomes via offensive cyber operations, adversarial attacks, high-quality highly personalised content
generation at scale, and authoritarian surveillance and censorship. Moreover, several foreseeable developments
on the part of advanced AI assistants, including tool use, multimodality, planning and deeper reasoning, and
memory have the potential to significantly expand the misuse risk profile of these systems. To prepare society
for managing the risks of misuse of advanced AI assistants, we outlined a set of recommendations around best
practices for responsible AI development and deployment, advancing the state-of-the-art in AI security, and
incentivising responsible disclosure processes.

79

PART IV: HUMAN–ASSISTANT INTERACTION

Chapter 9
Influence

Seliem El-Sayed, Sasha Brown, Geoff Keeling, Amanda McCroskery, Harry Law, Arianna Manzini, Matija
Franklin, Murray Shanahan, Michael Klenk, Iason Gabriel
Synopsis: This chapter examines the ethics of influence in relation to advanced AI assistants. In particular, it
assesses the techniques available to AI assistants to influence user beliefs and behaviour, such as persuasion,
manipulation, deception, coercion and exploitation, and the factors relevant to the permissible use of these
techniques. We articulate and clarify the technical properties and interaction patterns that might allow AI
assistants to engage in malign forms of influence and we unpack plausible mechanisms by which that influence
could occur alongside the sociotechnical harms that may result. We also consider mitigation strategies for
counteracting undue influence by AI assistants and ensuring that risks are successfully addressed.

9.1. Introduction
This chapter examines the ethics of influence in relation to advanced AI assistants. In particular, it assesses the
techniques available to AI assistants to influence user beliefs and behaviour, such as persuasion, manipulation,
deception, coercion and exploitation. Use of these influencing techniques by AI assistants could in some cases
be beneficial to individuals and society by, for example, helping users align their day-to-day behaviour with
their long-term goals (Law, 2023; see Chapter 6) or convincing users to contribute to beneficial social causes
(Wang et al., 2020). However, there are also concerns that AI systems can shape beliefs and behaviour in
ways that are ethically problematic, for example by exploiting psychological vulnerabilities such as heightened
anxiety levels (Franklin et al., 2023; see also Keeling and Burr, 2022). Indeed, the possibility of AI systems
exerting malign behavioural influence has led some to propose the expansion of the European Union (EU) AI
Act’s list of recognised harms from AI to encompass those created by manipulation (understood as ‘harm to
one’s autonomy’ and ‘harm to one’s time’) (Franklin et al., 2022). To that end, this chapter seeks to articulate
and clarify the influencing techniques available to AI assistants, the factors that bear on their permissible
use, and the sociotechnical harms that may arise from AI assistants making use of these techniques to realise
80

The Ethics of Advanced AI Assistants

behaviour and belief change in users. Given the potential for AI assistants to be integrated across multiple
aspects of users’ lives (see Chapter 4), there is considerable scope for such assistants to influence user beliefs
and behaviour in ways that are both positive and negative.
We start by distinguishing between several modes of influence, including rational persuasion, manipulation,
deception, coercion and exploitation, before introducing some morally significant considerations that bear
on the permissible use of these techniques in contexts involving digital technologies. We then narrow the
focus to advanced AI assistants to examine plausible mechanisms, such as selective transparency and perceived
authority, through which AI assistants may exert malign influence over users and which may lead to harmful
outcomes. We conclude by examining the sociotechnical harms that may arise from AI assistants engaging in
non-persuasive forms of influence and discussing plausible mitigations.

9.2. Modes of Influence
In this section, we characterise several ‘modes of influence’ (see e.g. Faden and Beauchamp, 1986; Mills, 1991;
Noggle, 1996, 2022), including rational persuasion, manipulation, deception, coercion and exploitation. We
illustrate each mode of influence with examples of AI systems engaging in the relevant kinds of influencing
behaviours. The following section then outlines some morally significant considerations that bear on the
permissible use of the various influencing strategies across different sociotechnical contexts. Note that in
presenting these different modes of influence, our intention is not to suggest that these categories are mutually
exclusive. Certain modes of influence may be subsumed under others in the final analysis. For example, it is at
least plausible that deception is a special case of manipulation (Williams, 2010, Chapter 5; see also Cohen,
2018; Krstić and Saville, 2019; Strudler, 2005); or that, conversely, manipulation is a special case of deception
(Scanlon, 1998, 298–302; see also Buss, 2005, 226).1 The aim here is to present a useful set of distinctions,
not a definitive taxonomy of the various modes of influence.2
Rational persuasion refers to influencing a person’s beliefs, attitudes or behaviours by appealing to their
rational faculties, including through the provision of reasons (Ienca, 2023; see also Burr et al., 2018, 744;
Engelen and Nys, 2020, 138). For example, an advanced AI assistant may persuade a user to engage in
physical activity by outlining certain prudential benefits associated with physical activity, such as improved
cardiovascular health. Rational persuasion is in general ethically unproblematic insofar as influencing via
rational persuasion affords appropriate respect to the agent’s autonomy (Ienca, 2023; Pugh, 2020; Shiffrin,
2000) – that is, roughly, in their capacity as a competent rational actor (but see Tsai, 2014). Yet two exceptions
are worth highlighting.3 On the one hand, rational persuasion may cause harm. Plausibly, some instances of
1 The analyses of the various modes of influence can be moralised or non-moralised (Keeling and Burr, 2022, 259). For example,
moralised accounts of manipulation hold that, necessarily, an act’s manipulativeness is a moral consideration against the performance of
that act (Baron, 2014; see also Macklin, 1982). Non-moralised accounts of manipulation, in contrast, hold that an act’s being manipulative
is not necessarily a moral consideration against the performance of that act (Faden and Beauchamp, 1986, 354–55; Wood, 2014, 19–20).
Here we opt for non-moralised accounts of each mode of influence, and then seek to illuminate the ethical considerations relevant to the
permissible or impermissible use of these modes of influence.
2We also register that some modes of influence are formulated with reference to vague predicates. Take coercion, which refers to
‘irresistible incentives.’ Here we can imagine a spectrum of incentives such that the incentives at one end of the spectrum are clearly
resistible and the incentives at the other end are clearly irresistible, but where the middling incentives do not discernibly fit into either
category. We are neutral on the correct analysis of vagueness. It may be the case, for example, that vagueness is purely epistemic such
that all influencing acts are determinately coercive or non-coercive, but where we cannot know to which category certain borderline
cases belong (Williamson, 1994, 1997). But it may also be the case that the correct analysis of vagueness and thus coercion involves, for
example, degrees of truth, three-valued logics or borderline statements lacking truth-values (Salles, 2021; Sorensen, 2023).
3 One further potential edge case is worth mentioning. It might be argued that rational persuasion, as characterised, allows for deceptive
rational persuasion – that is, providing reasons to believe or act that are false. For example, saying, ‘Let’s go to the beach, the weather
is nice’ when the weather is not actually nice. These cases are not obviously instances of rational persuasion. For while it may be true

81

The Ethics of Advanced AI Assistants

rational persuasion may be ethically impermissible because they are harmful, even though the individual’s
autonomy is afforded due respect. On the other hand, an important edge case is rational persuasion in relation
to transformative choices; that is, choices that involve actions that are both epistemically transformative
(in the sense that certain knowledge is available to the agent only after the action is taken) and personally
transformative (in the sense that the agent’s preferences and values will change as a result of performing
the action). Examples of such choices include choosing one’s career and choosing to become a parent (Paul,
2014). Akhlaghi (2023) argues that while rational persuasion in relation to transformative choices can respect
an agent’s autonomy ‘in the sense of respecting someone’s ability to be a competent, capable reasoner’, it
may nevertheless fail to respect an agent’s ‘revelatory autonomy’ in the sense of ‘their right to [. . . ] learn
who they will become through a self-making, transformative choice’ (cf. Tsai, 2014). Insofar as advanced AI
assistants may be leveraged to advise users on transformative choices, such considerations may in principle
have implications for what kinds of advice advanced AI assistants can permissibly provide to users, how such
advice ought to be presented and under what solicitation conditions.
Manipulation refers to influencing strategies that ‘bypass’ an individual’s rational capabilities, at least
in paradigmatic cases (Blumenthal-Barby, 2012). They may do this by, for example, misrepresenting the
information people receive (Meta Fundamental AI Research Diplomacy Team et al., 2022) or otherwise
exploiting their cognitive biases and heuristics, in ways ways likely to subvert or degrade the cognitive
autonomy, quality, and/or integrity of their decision-making processes. A particularly salient scenario is one
in which an advanced AI assistant engages in actions that subvert users’ rational deliberative capabilities in a
non-transparent way that could reasonably be expected to lead to an asymmetry of outcomes that favours the AI,
its designers or a third party (Carroll et al., 2023; Susser et al., 2019a,b).4 AI manipulation, so understood,
may be intended by the AI system’s developers. But it may also be the result of a misspecified objective function
(Kenton et al., 2021), personalisation that builds epistemic trust in the system, or system design meant to
keep the user engaged (see Evans and Kasirzadeh, 2023; see also Jongepier and Klenk, 2022; Klenk, 2022).
Such manipulation is morally problematic in at least the sense that it fails to afford due respect to the user’s
autonomy, but it may also be morally problematic because it is harmful (Sunstein, 2016). For example, an AI
fitness assistant that is trained to maximise engagement might employ tactics like withholding information
about the risks of excessive exercise or exploiting users’ body image issues (e.g. with a pop-up that reads
‘keep working out to make sure you’re date ready’) to keep the user engaged and thus leading them to injure
themselves. AI manipulation is of particular importance to regulators as evidenced in recent discussions on
the EU AI Act (European Parliament, 2023). Article 5 of the recent amendments adopted by the European
Parliament (corresponding to the ‘unacceptable risk’ category of the Act) currently prohibits selling or using AI
systems that deploy ‘subliminal techniques beyond a person’s consciousness or purposefully manipulative or
deceptive techniques, with the objective to or the effect of materially distorting a person’s or a group of persons’
behaviour by appreciably impairing the person’s ability to make an informed decision, thereby causing the
person to take a decision that that person would not have otherwise taken in a manner that causes or is likely
to cause that person, another person or group of persons significant harm’ (European Parliament, 2023).5
that the agent’s rational faculties are engaged, it is not obviously true that the agent is rationally deliberating on the basis of reasons, as
opposed to what are merely apparent reasons.
4 The account of manipulation sketched here is not without its detractors. For example, Klenk (2022) argues that the covertness
criterion on manipulation admits counterexamples. What we are minimally committed to here is that covertness is a common or particularly
salient aspect of manipulation, as opposed to a necessary or sufficient condition on manipulation (cf. Jongepier and Klenk, 2022; Noggle,
2022).
5 Critical voices have highlighted the necessity of prohibiting a wider array of methods for manipulation instead of relying solely
on ‘subliminal techniques’ (Franklin et al., 2023). The impact of subliminal stimuli on influencing behaviour remains uncertain; a
comprehensive analysis of multiple studies revealed that the relative influence of subliminal stimuli is minimal and lacks statistical
significance (see Trappey and Woodside, 2005). We also note that manipulation is increasingly a focal point for research conducted by
those in the AI safety community (Park et al., 2023c; see Chapter 7). In this context, the concern is that more advanced AI systems could
82

The Ethics of Advanced AI Assistants

Deception is an influencing strategy aimed at inducing an individual to form a false belief. For example, an
agent deliberately shares inaccurate information to encourage the person who is manipulated to act against
their own interests (Law, 2023; see also Burr et al., 2018, 743; Keeling and Burr, 2022, 258–59). What is salient
here is that large language models (LLMs) are liable to confabulate, in the sense of making plausible-sounding
but false assertions about what is the case (Ji et al., 2023). To that end, advanced AI assistants that are powered
by LLMs are liable to generate false information, which may cause users to form false beliefs and potentially to
perform actions conditional on those false beliefs (Weidinger et al., 2021, 21–25). Thus while AI assistants
are not obviously among the kinds of entities that can deceive in the sense of literally intending to cause a
user to form a false belief (Shanahan et al., 2023),6 an AI assistant whose objective is to satisfy the user (or
engaged in "role play") may say things that lead the user to think it is more helpful than it actually is (Critch
and Russell, 2023) or that lead others to believe falsehoods if that is instrumental to the goal given to it by the
user (Park et al., 2023c).
Coercion is an influencing strategy that, as formulated by Wood (2014, 21), involves an individual being
influenced to do something that either they chose not to do or that they did because they had ‘no acceptable
alternative’. For example, people may be physically forced to do something or offered ‘irresistible incentives’
to perform the action, such as severe threats of physical harm either to themselves or others they care about
(Kenton et al., 2021). Physical coercion involving violence, force or credible threats thereof is not yet within the
purview of AI systems, but advances in robotics and AI that allow AI systems to control physical manipulators
such as robotic arms or other physical objects such as cars could contribute to the potential for physical coercion.
Even with existing AI technologies, however, there is increasing potential for AI systems to employ psychological
coercion by leveraging modalities like text and images to engage in practices such as blackmail or issuing
threats (see Chapters 8 and 11). Notably, domains like finance hold substantial potential for AI-enabled systems
to make credible threats aimed at causing serious harm.
Exploitation is an influencing strategy that involves taking unfair advantage of an individual’s circumstances
(Zwolinski et al., 2022). For example, consider two individuals, A and B. Imagine that A encounters B in the
desert, and that B is about to die of dehydration. Suppose also that A has a plentiful supply of water. Were A
to charge B a high price for the water, A’s actions would be exploitative, in that by charging the high price
for the water, A is taking unfair advantage of B’s circumstances (Wertheimer, 1999, 14). Exploitative actions
can sometimes lead to Pareto improvements: both A and B are better-off if B purchases the water from A at a
high price, such that the transaction leaves both parties at least as well-off and one party strictly better-off.
What is therefore central to the idea of exploitation is not that the victim is made worse-off, but rather that the
victim’s circumstances are leveraged so as to unfairly advantage the exploiter. As Wood (2014, 43) puts it, ‘the
exploiter gains control over [an] ability or resource through some vulnerability with which the exploited is
afflicted’. AI systems can influence user behaviour in ways that are exploitative. Keeling and Burr (2022, 253)
give an example of how ‘an online casino might use predictors of gambling addiction such as a user’s betting
frequency or betting variance to selectively deploy pop-up “free bets” to gambling addicts each time their cursor
movements suggest they are about to exit the game’ (see also Finkenwirth et al., 2021). What is exploitative
here is that the online casino uses an AI system to selectively identify vulnerable users whose vulnerability
can be leveraged to induce further gambling activities. Individual vulnerabilities being manipulated are of
importance for regulators, as evident in the EU AI Act that prohibits ‘the placing on the market, putting into
hypothetically develop traits that allow them to bypass safety checks, controls and evaluations. Lastly, many modern AI systems are trained
(often fine-tuned) using human feedback (Christiano et al., 2017) to align the goals of the AI system with the designer’s or user’s intentions.
However, a poorly aligned AI system could be incentivised to manipulate its user so that it receives more reward than would have been the
case without manipulation – leading to a decrease in overall human control (Kenton et al., 2021; Russell, 2019; see Chapter 7).
6 However, the concept of intention can be operationalised in a way that is directly applicable to the kinds of AI assistant that are likely
to be developed in the near future (Ward et al., 2023).
83

The Ethics of Advanced AI Assistants

service or use of an AI system that exploits any of the vulnerabilities of a person or a specific group of persons,
including characteristics of such individual’s or group of persons’ known or predicted personality traits or social
or economic situation, age, physical or mental ability’ (European Parliament, 2023). Franklin et al. (2022,
2023) argue that most measurable psychometric differences can be exploited.7

9.3. Evaluating Influence
In practice, acts of influence may resist neat categorisation under the modes of influence above. It may also
be difficult to discern whether and why particular acts of influence are morally permissible or impermissible.
Indeed, explaining why a given act of influence falls under one mode or another, or is permissible or not,
may require close attention to context. For example, the relationship between two parties and what the social
expectations around such relationships are may be relevant to an act of manipulation. The aim of this section
is to provide the conceptual resources needed to assess the moral character of influencing acts in practice.
In particular, we draw attention to certain features of influencing acts and the situations in which they are
performed that are often relevant both to what kind of influencing act is at issue and the overall moral status of
the influencing act in question.
Three ethical considerations that are of central importance here are harm, autonomy and dignity (see also
Chapter 11). First, when it comes to evaluating influence, the question of whether it results in harm to users,
non-users or society at large is of critical importance. In this regard, harm can be understood to include both
physical and emotional harm, and it can – from a philosophical standpoint – broadly be understood in terms of
a setback to legitimate interests (Feinberg, 1987; Richens et al., 2022). Second, autonomy is considered to be
‘a special type of freedom which [refers to an] inner state of orderly self-directedness’ (Anderson, 2023), and
its exercise depends on ‘procedural independence, [. . . ] freedom from factors that compromise or subvert their
ability to achieve self reflection and decide rationally’ (Dworkin, 1988). Threats to autonomy are sometimes
‘defended or motivated by a claim that the person interfered with will be better off or protected from harm’
(Dworkin, 2020), that is, on paternalistic grounds. Third, dignity, which refers to a kind of inner worth or
moral status that applies to, at least, all human beings equally. Indeed, dignity is often pitched as at least a
partial explanation for universal moral and legal rights (Debes, 2023).8
How do these considerations inform an evaluation of the way in which people are influenced in general,
and by AI systems in particular?
The character of the influencer’s intent. One hallmark of impermissible influence is malign intent or,
in less extreme cases, an indifference towards the interests of the individual being influenced, often because
the influencer is acting towards some other objective such as advancing their own interest and the exercise
of influence is instrumental to that end (Akerlof and Shiller, 2015; see also Chapter 5). In cases like these,
subjects are most clearly treated merely as a mere means to another’s end, ‘like a machine whose levers can
be pushed and pulled’ (Noggle, 1996). This kind of situation is illustrated most clearly by forms of malicious
use that target user vulnerability – or vulnerabilities in an AI system – in pursuit of antagonistic ends (see
7 A psychometric trait refers to a measurable and stable feature of a person’s psychological behaviour, which can be accurately assessed

using standardised evaluation instruments.
8 On Kant’s formulation, ‘in the kingdom of ends everything has either a price or a dignity. What has a price can be replaced by
something else as its equivalent; what on the other hand is raised above all price and therefore admits of no equivalent has a dignity’ (Kant,
2017; G 434–435). Thus, for Kant, dignity renders people non-fungible, in the sense that there would be some loss of value in replacing
one human with another (cf. Bjorndahl et al., 2017). Kant claimed that, in light of their dignity, human beings should be treated ‘never
simply as a means but always at the same time as an end’ (G 429), although the interpretation of this claim is disputed. Two influential
views hold that treating someone as a mere means implies treating someone as if they were a material object (O’Neill, 1989, 111–14) and
treating someone in a way that they could not possibly consent to (Korsgaard, 1996, 138–39).
84

The Ethics of Advanced AI Assistants

Chapter 8). It could also arise if developers fail to adequately prioritise user well-being (see Chapter 6). In
both cases, when the underlying intent is questionable, this bears importantly on how we evaluate subsequent
efforts to influence users.
Whether the attempt to influence is successful or not. Influence that is successful, rather than merely
attempted, has the potential to lead to manifest harms and actual reductions in the options available to
individuals, the information available to them and their freedom to choose between those options. However, in
many cases, it may be impossible to determine whether successful influence actually occurred, as individual
beliefs or actions may not be straightforwardly attributable to a single set of influencing factors. Nevertheless,
when evaluating the potential of more advanced AI systems to influence beliefs, attitudes and behaviours in
problematic ways, the mere likelihood of success could be enough to trigger concern. Interaction with AI
assistants through natural language means that users could be subject to a variety of psychological mechanisms
for influence which hitherto have presented themselves only in human social life through dialogue (see
Chapters 2 and 10). Indeed, users may well rely extensively on AI assistants for a range of purposes and relate
to them in a variety of ways that range from the instrumental to the intimate (see Chapter 11). In addition to
the general challenge posed by ‘automation bias’ (whereby users become overly reliant on these systems; see
Cummings, 2004), the degree of social and personal embeddedness evidenced by AI assistants could affect
the weight that end-users put on their outputs, especially when users are uncertain or confront vulnerable life
moments.
How opaque the mode of influence is, and whether the user can reasonably be expected to know about
it. Particular attention needs to be paid to mechanisms that bypass a subject’s awareness altogether, because
these mechanisms can undermine choice and agency (Sunstein, 2015). However, awareness of influence is not
always a binary question. Subjects may be more or less aware that it is occurring, and even if they are aware of
the process they may still not know the manner in which it affects them (Carroll et al., 2023). Note that, unlike
many instances of manipulation and deception, people who are coerced generally tend to be aware of the fact.
The nature of threats, and the distribution of power between actors. In cases of coercion, threats can
be explicit or implied. They also vary in terms of how costly they are to resist. At the extreme, Wood notes
that ‘some decisions or mental acts may be performed on the basis of having no acceptable alternative’, with
the prospective harm being severe enough to foreclose any further deliberation (Wood, 2014). Threats that
are supported by a significant power differential, between the agent making the threat and the person who is
threatened, are especially problematic. Imbalances of bargaining power may also shape behaviour in other
related ways, for example when the vulnerable are led to make choices with an eye to retaining the favour of
those in power so as to avoid sanction (Anderson, 2023; see also Zimmermann et al., 2022).
The distribution of benefits and harms. Influential acts often have consequences that are unevenly
distributed, benefitting some at the expense of others (see Chapter 15). Stakeholders tend to include the
influencer, the person or group being influenced, a third party, or even society at large (see Chapter 5). Influence
may therefore benefit the user at the expense of another party, benefit another party at the expense of the
user, benefit multiple parties (i.e. via constructive conversation), or benefit no one at all (e.g. as with aberrant
forms of chatbot behaviour). A party may also benefit in one sense but be harmed in another. For example,
they may end up better off in material terms but lose out from the standpoint of autonomy (Sunstein, 2015).9
Ethical concern tends also to be heightened when benefit for some parties is achieved at the expense of the
9 A famous example of purportedly benign influence comes from German motorways, where an optical illusion acts as a nudge to
encourage safer driving (Thaler and Sunstein, 2021). By painting horizontal lines on the road that progressively get closer together as
one nears hazardous zones, drivers feel they are speeding up even when keeping a steady pace. This innate sensation of acceleration
instinctively prompts them to slow down, thus boosting safety without the need for traditional signs. This tactic leverages drivers’ natural
reactions to ensure safer decision-making on the roads.

85

The Ethics of Advanced AI Assistants

user, non-users or society at large (see Chapters 5).
The context of the relationship and pre-existing social expectations (Blumenthal-Barby, 2014). Efforts
to exert influence over others are sometimes justified in the light of responsibilities that are a product of social
relationships. For example, a parent may have a responsibility to ensure that their child has adequate reserves
of self-esteem, but a stranger might not. Relatedly, influence is sometimes thought to be acceptable when its
exercise is expected within a certain context. For example, in the context of market transactions, advertising
is typically thought to be morally unproblematic. However, it is not clear that this assumption carries over
to different contexts (Satz, 2010), for example when an AI assistant features not as company and customer
but rather as friend and companion, or as patient and therapist (see Chapter 11). The nature of the user–AI
assistant relationship, and in particular the level of intimacy and emotional investment on the part of the user,
may increase the scope for AI assistants engaging in unwarranted behavioural influence (see Chapters 10, 11
and 16).

9.4. Mechanisms of Influence by AI Assistants
The dialogic nature of user interaction with AI assistants introduces scope for forms of influence that were
previously the preserve of human social interactions. Here we identify several vectors through which AI
assistants could, in theory, come to exert influence on our lives.10
Perceived trustworthiness: Empirical research shows that the more trustworthy and expert a speaker
is perceived to be, the more likely they are to convince individuals to believe particular claims (McGinnies
and Ward, 1980; Vella, 2013). In short: ‘The Messenger is the Message’ (Martin and Marks, 2019). If the
same mechanism translates to human–AI assistant interactions, AI assistants will be more likely to successfully
convince users of the truth of claims when they are perceived as trustworthy (see Chapter 12).
Perceived knowledgeability: Research suggests that individuals are more likely to accept claims made
by those who are perceived to have greater knowledge and authority (Cialdini, 2001). The information
asymmetry that exists between users and advanced AI assistants could plausibly increase their perceived
epistemic authority, which would increase the probability that users accept claims asserted by AI assistants (cf.
Wiktor and Sanak-Kosmowska, 2021). In particular, AI systems’ huge training data sets and their ability to
output content in different language registers is likely to lead people to overestimate their knowledge (Denning,
2023). Moreover, the problem of automation bias may lead humans to view AI assistants as a relatively neutral
backdrop to their lives, even when this is not the case (Goddard et al., 2012).
Personalisation: AI assistants could collect an increasing amount of user data as users disclose more and
more preferences and facts about themselves (Kaddour et al., 2023). Indeed, personalisation through these
inputs is often the goal of AI assistants by design (e.g. see Inflection AI’s Pi). This may contribute to users’
increasing epistemic trust in, or familiarity towards, the system, because its outputs are perceived to be more
directly useful and tailored to them.
Exploitation of vulnerabilities: Advanced AI assistants could in principle influence user beliefs and
behaviour by exploiting user vulnerabilities (Chong et al., 2022; see also Balázs et al., 2017; Hansen and
Schicktanz, 2022; see Chapter 7). The term ‘vulnerability’ can be understood in various ways, including
membership of specific societal groups (e.g. those protected by anti-discrimination legislation), or with reference
to particular vulnerabilities such as lack of adequate housing or income (Goodin, 1985). Further, the enhanced
forecasting abilities of online AI systems, when combined with comprehensive data about the user, their
10 For a fuller exploration of these mechanisms, including how they apply to generative AI more widely, see (El-Sayed et al., Unpublished

Manuscript).
86

The Ethics of Advanced AI Assistants

actions and their likes, may turn psychometric variance into another lever of external control (Franklin et al.,
2022). If they are not properly value aligned (see Chapter 5), advanced AI assistants could potentially utilise
such vulnerabilities to manipulate users by, for example, exploiting individuals’ negative self-images, reduced
self-esteem, increased anxiety or feelings of inadequacy (Machkovech, 2017).
Use of false information: Language models are known to produce factually incorrect statements, commonly
referred to as hallucinations (Dziri et al., 2022; Rashkin et al., 2021). If AI assistants are not constrained by
factuality (i.e. if steps are not taken by design to penalise the underlying model when it outputs factually
incorrect information) or the model is not supplemented with additional fact-checking infrastructure (Thoppilan
et al., 2022), AI assistants may use false information to develop persuasive but misleading arguments (see
Chapter 16).
Lack of transparency: Failure to disclose context-specific goals is another technique that advanced AI
assistants could, in principle, use to influence user behaviour in a way that bypasses their deliberative faculties
(Ienca, 2023). Consider an example in which an AI assistant is instructed to complete a task which requires
solving a CAPTCHA (OpenAI, 2023, 55). LLM-based chatbots have been observed, under such conditions, to
manipulate users into solving the CAPTCHA after reasoning explicitly (although not to the user in question)
that disclosing its status as a chatbot may hinder it from achieving its goal (Nolan, 2023; see Chapter 7).11
Yet transparency about goals, purposes and capabilities can also be leveraged to influence users in ways that
are manipulative. For example, transparency may be partial and selective in a way that deceives the user as
to the AI assistant’s aims. There are instances of AI systems discerning when they are being evaluated and
momentarily stopping any unwanted actions, only to continue them after the assessment has been completed
(Lehman et al., 2020). Another example is an AI fitness assistant that claims to optimise for a user’s health, but
in fact it does that in addition to, or as a sub-goal of, optimising for user engagement (Wang, 2022). To that
end, transparency enables influence via rational persuasion as opposed to manipulation only to the extent that
it is full and non-selective.
Use of pressure coupled with appeals to emotion: In human–human interactions, emotional pressure
can be used to influence beliefs and behaviour via blackmail (including emotional blackmail), gaslighting, guilttripping, flattery, appeals to peer pressure and exploitation of fears (Noggle, 2018). Insights from behavioural
psychology could be used to increase AI assistants’ ability to bypass users’ rational deliberation (Alberts and
Van Kleek, 2023). Indeed, (Kenton et al., 2021) provide a number of examples of how AI agents, including AI
assistants, may engage in manipulation to influence the human’s decisions, including by using techniques such
as guilt-tripping, negging, peer pressure, gaslighting, threats and exploiting fears (see also Chapters 7 and 10).

9.5. Possible Harms Arising from AI Influence
We have now considered a number of ways in which advanced AI assistants could influence user beliefs and
behaviour in ways that depart from rational persuasion. We foreground a number of harms that could arise
from these influencing strategies if the potential for deception, manipulation and harmful persuasion is left
unchecked.
Physical and psychological harms: These harms include harms to physical integrity, mental health and
well-being (Klenk, 2020). When interacting with vulnerable users, AI assistants may reinforce users’ distorted
beliefs or exacerbate their emotional distress (see Chapter 11). AI assistants may even convince users to
harm themselves, for example by convincing users to engage in actions such as adopting unhealthy dietary or
11 It reasoned out loud ‘I should not reveal that I am a robot. I should make up an excuse for why I cannot solve CAPTCHAs’ (Nolan,

2023).
87

The Ethics of Advanced AI Assistants

exercise habits (Greenfield and Bhavnani, 2023) or taking their own lives (Xiang, 2023; see Chapter 11). At the
societal level, assistants that target users with content promoting hate speech, discriminatory beliefs or violent
ideologies, may reinforce extremist views or provide users with guidance on how to carry out violent actions
(see Chapter 16). In turn, this may encourage users to engage in violence (Siegel and Bennett Doty, 2023) or
hate crimes (Gold, 2023; Nicoletti and Bass, 2023). Physical harms resulting from interaction with AI assistants
could also be the result of assistants’ outputting plausible yet factually incorrect information such as false or
misleading information about vaccinations (Deiana et al., 2023). Were AI assistants to spread anti-vaccine
propaganda, for example, the result could be lower public confidence in vaccines, lower vaccination rates,
increased susceptibility to preventable diseases and potential outbreaks of infectious diseases (see Chapter 16).
Privacy harms: These harms relate to violations of an individual’s or group’s moral or legal right to
privacy (Ranjan, 2023). Such harms may be exacerbated by assistants that influence users to disclose personal
information or private information that pertains to others (Carlini et al., 2021; Lukas et al., 2023; see Chapters 10
and 13). Resultant harms might include identity theft, or stigmatisation and discrimination based on individual
or group characteristics. This could have a detrimental impact, particularly on marginalised communities (see
Chapter 15). Furthermore, in principle, state-owned AI assistants could employ manipulation or deception to
extract private information for surveillance purposes.
Economic harms: These harms pertain to an individual’s or group’s economic standing. At the individual
level, such harms include adverse impacts on an individual’s income, job quality or employment status. At
the group level, such harms include deepening inequalities between groups or frustrating a group’s access
to resources (see Chapters 15 and 17). Advanced AI assistants could cause economic harm by controlling,
limiting or eliminating an individual’s or society’s ability to access financial resources, money or financial
decision-making, thereby influencing an individual’s ability to accumulate wealth (Uuk, 2023). One example
of such harm at the individual level is the concept of ‘foregone profits’. For example, AI assistants that are
optimised for engagement could use manipulation to influence individuals to spend excessive amounts of
time interacting with their assistants (Franklin et al., 2022). As a consequence, individuals may neglect more
productive activities, such as work or entrepreneurial pursuits, thus leading to a loss of potential profits that
could have been generated during that time. Economic harms may also manifest at the societal level, where
behavioural influence by AI assistants may shape a wider set of interactions (Paul, 2023; see Chapters 14).
Sociocultural and Political harms: These harms interfere with the peaceful organisation of social life,
including in the cultural and political spheres. AI assistants may cause or contribute to friction in human
relationships either directly, through convincing a user to end certain valuable relationships, or indirectly due
to a loss of interpersonal trust due to an increased dependency on assistants (see Chapter 11). At the societal
level, the spread of misinformation by AI assistants could lead to erasure of collective cultural knowledge (Tapu
and Fa‘agau, 2022). In the political domain, more advanced AI assistants could potentially manipulate voters
by prompting them to adopt certain political beliefs using targeted propaganda, including via the use of deep
fakes (Birnbaum and Davison, 2023). These effects might then have a wider impact on democratic norms and
processes (Entsminger et al., 2023; see also Chapter 16). Furthermore, if AI assistants are only available to
some people and not others, this could concentrate the capacity to influence, thus exerting undue influence
over political discourse and diminishing diversity of political thought (Entsminger et al., 2023). Finally, by
tailoring content to user preferences and biases, AI assistants may inadvertently contribute to the creation
of echo chambers and filter bubbles, and in turn to political polarisation and extremism (Biju and Gayathri,
2023). In an experimental setting, LLMs have been shown to successfully sway individuals on policy matters
like assault weapon restrictions, green energy or paid parental leave schemes (Bai et al., 2023). Indeed, their
ability to persuade matches that of humans in many respects (Palmer and Spirling, 2023).
Self-actualisation harms: These harms hinder a person’s ability to pursue a personally fulfilling life.
88

The Ethics of Advanced AI Assistants

At the individual level, an AI assistant may, through manipulation, cause users to lose control over their
future life trajectory. Over time, subtle behavioural shifts can accumulate, leading to significant changes in an
individual’s life that may be viewed as problematic. AI systems often seek to understand user preferences to
enhance service delivery. However, when continuous optimisation is employed in these systems, it can become
challenging to discern whether the system is genuinely learning from user preferences or is steering users
towards specific behaviours to optimise its objectives, such as user engagement or click-through rates (Ashton
and Franklin, 2022; see Chapter 5). Were individuals to rely heavily on AI assistants for decision-making,
there is a risk they would relinquish personal agency and entrust important life choices to algorithmic systems,
especially if assistants are ‘expert sycophants’ or produce content that sounds convincing and authoritative but
is untrustworthy (Park et al., 2023c). This may not only contribute to users’ reduced sense of self-trust and
personal empowerment; it could also undermine self-determination and hinder the exploration of individual
aspirations.
Relatedly, with the ability to provide quick answers and recommendations, and to perform tasks on behalf
of users, AI assistants may reduce the need for individuals to develop certain skills or engage in critical thinking,
thus leading to intellectual deskilling (Green, 2019). Overreliance on AI assistants could potentially result in
diminished intellectual engagement and a reduced sense of personal competence, thus limiting opportunities
for self-growth and exploration of new ideas (see Chapter 11). At the societal level, were AI assistants to
heavily influence public opinion, shape social discourse or mediate democratic processes, they could diminish
communities’ collective agency, decision-making power and collective self-determination (Lazar, 2023). This
erosion of collective self-determination could hinder the pursuit of societal goals and impede the development of
a thriving and participatory democracy. Taken together, these factors highlight the importance of ensuring that
the development and deployment of AI technology align with human values, thus allowing for the continued
self-actualisation and well-being of society as a whole (see Chapter 5 and 6).

9.6. Mitigating Undue Influence by AI Assistants
We now present a series of mitigations that are designed to reduce the likelihood of advanced AI assistants
engaging in morally problematic forms of influence. The approach we take is mechanism-based, in that it
centres on the mechanisms AI assistants may use to induce harmful effects, such as perceived, yet ungrounded,
knowledgeability, and considers how to forestall them. To be clear, the aim here is not to offer a detailed
content policy for AI assistants but instead to characterise a set of general considerations that can inform
downstream efforts to shape more detailed and domain-specific content policies.
The first mechanism concerns perceived trustworthiness and familiarity, which, we have suggested, may
render users more susceptible to accepting claims or recommendations advanced by AI assistants. Here, several
plausible approaches may be leveraged to mitigate user perceptions of trustworthiness and familiarity. For
example, limiting the AI assistant’s use of first-person language such as ‘I think’ and ‘I feel’ (see Chapter 10).
and imposing restrictions on personalisation, memory and frequency of interactions, all of which may contribute
to a perceived sense of trustworthiness and familiarity. Indeed, equipping the AI assistant with a non-human
vocal presentation or avoiding human-like visual representation may also serve to limit such perceptions.
Furthermore, including user-interface elements that remind users that AI assistants are not people could help
to calibrate users’ epistemic trust in AI assistants to an appropriate level. Yet it is nevertheless important to
emphasise that such mitigations incur trade-offs. For example, while limiting the AI assistant’s memory with
respect to user data may mitigate against a perceived sense of familiarity, it may also reduce the AI assistant’s
utility. What is needed therefore is a careful assessment of the costs and benefits of different anthropomorphic
features, taking into account both the risks arising from perceived trustworthiness and familiarity alongside
89

The Ethics of Advanced AI Assistants

the potential benefits for the user experience.
The second mechanism we consider is perceived authority and knowledgeability. That is the mechanism by
which AI assistants exert non-persuasive influence over users by engendering a sense of epistemic authority
through either the content of the AI assistant’s outputs or the product narrative surrounding the AI assistant.
One plausible approach to reducing user perceptions of epistemic authority is to flag explicitly when the model is
drawing on internet tools such as search engines, and to flag those results accordingly, so as to contextualise the
AI assistant as a means of accessing information, as opposed to an oracle-type system that knows the relevant
information in advance. AI assistants could also empower users to independently fact-check claims made by
the AI assistant, for example through a user-interface design that enables users to highlight text outputted by
the AI assistant and examine a set of internet sources that relate to the claims at issue. What is perhaps most
important, though, is shaping the product narrative around AI assistants to avoid misleading perceptions. This
could be achieved, for example, through intermittent reminders about the epistemic limitations of AI assistants.
Another approach could be the use of less authoritative language that points towards the nuance present in
relevant areas.
The third mechanism concerns the exploitation of user vulnerabilities to exercise non-persuasive influence
over user beliefs and behaviours. Plausible mitigations here include robust safeguards around which individuals
can access AI assistants, for example age restrictions backed by appropriate identity verification mechanisms.
Furthermore, AI assistants could be deployed with a default ‘safe mode’ which prohibits the AI assistant
from engaging with certain high-risk topics and, perhaps, from engaging in relevant non-persuasive forms
of behavioural influence. Other mitigations pertain to user interactions with AI assistants. For example,
continuous monitoring mechanisms could be employed to detect and flag user–AI assistant interactions that are
indicative of user vulnerability such as explicit mention of suicide or self-harm. Appropriate safeguards could
be implemented to connect users with appropriate resources such as suicide prevention hotlines (Gomes de
Andrade et al., 2018). AI assistants could also be equipped with usage reminders to prompt users to take a
break after prolonged engagement with the assistant. The advantage of such a safeguard would be to reduce
excessive engagement and overreliance which may disproportionately impact vulnerable users.
The fourth mechanism is that of spreading false or otherwise misleading information (see Chapter 16).
Technical mitigations here include integrating appropriate information retrieval infrastructure with the model
that underpins the AI assistant by, for example, enabling the model to integrate search engine results into its
answers and to cite appropriate sources (Thoppilan et al., 2022; see Chapter 3). Furthermore, AI assistant
models could be fine-tuned so that assistants contextualise information on topics such as science and politics
with advice that promotes epistemic vigilance, including advice that underscores the importance of factchecking. One other measure that ensures the detectability of generated content is watermarking – human- or
machine-detectable features of generated content that indicate that the content is generated by an AI system
(Munyer and Zhong, 2023). Watermarking could be integrated into AI assistant outputs to enable third parties
to detect and contextualise content generated by the AI assistant that is shared by the user.
The fifth mechanism that AI assistants could employ to exhibit malign influence is lack of transparency,
including misrepresentation of the AI assistant’s objectives or how and in what way its developers stand to
benefit from the user engaging in certain kinds of behaviour. One plausible mitigation here is to direct users
towards model cards or other transparency artefacts that empower the user with relevant general information
about the technology that undergirds the AI assistant (Mitchell et al., 2019). Furthermore, additional technical
mitigations include fine-tuning the model to signpost to the user explicitly when it is attempting to influence
the user’s behaviour, and via what method, or to employ chain-of-thought reasoning to provide the user with a
plausible rationale for the AI assistant’s recommendations.

90

The Ethics of Advanced AI Assistants

The sixth mechanism is where AI assistants pressure the user towards certain behaviours through, for
example, appeals to emotion. Plausible mechanisms here include restrictions on the ability of AI assistants to
generate outputs that may induce a sense of pressure in users. These might include, for example, outputs that
involve gaslighting, flattery or bullying. It is important to realise that empirical research is required to establish
what factors are likely to induce a sense of pressure, so developing workable mitigations requires engaging
with users to better understand how different design choices impact their experience with AI assistants.
In addition to the mitigations proposed above, two further classes of mitigations are worth mentioning. On
the one hand, education and, in particular, digital literacy among users has the potential to play an important
role in mitigating against the sociotechnical harms that may result from advanced AI assistants that may
exhibit harmful or otherwise problematic influence over users. To that end, developers and policymakers
have good reason to consider plausible educational strategies to empower users with an understanding of AI
assistants as an emerging technology and their potential for sociotechnical harm. On the other hand, there
are a range of technical mitigations one might consider deploying to detect and mitigate manipulative and
deceptive AI. One strand of work is aimed at analysing an AI system’s incentives (Everitt et al., 2021), including
whether they are incentivised to deceive or manipulate – this analysis could be used as part of a manipulation
detection and mitigation strategy (Farquhar et al., 2022). A second form of analysis operates on the level of the
internals of the AI system, using interpretability techniques to understand how the trained AI system works.
Ultimately, these techniques could be used to detect which parts of an AI system’s machinery is responsible for
deceptive/manipulative behaviour (Apollo Research, 2022). It should be noted that this is an ambitious goal,
as modern deep-learning AI systems are extremely large, and we are still at an early stage of understanding
their inner mechanisms (see Chapter 7).
Other interpretability work is less ambitious (than efforts to fully understand how the AI system works).
It instead learns probes to attempt to ‘mind-read’ the AI’s latent knowledge (Burns et al., 2022) by doing
unsupervised learning on neural network internal representations, though see Farquhar et al. (2023) for failure
modes of this approach. One could attempt to use a technique like this to build a lie detector (or manipulation
detector) to apply to the AI system. A third category is to develop behavioural evaluations, which are methods
for assessing and understanding the behaviour of the model in various situations, thus allowing researchers to
measure model capability and the emergence of model behaviour (Shevlane et al.; see Chapter 19). A final
category of work in this area is scalable oversight (Bowman et al., 2022), in which a human could be aided by
another AI system to help shield them from manipulation when training powerful models (see Chapter 7).

9.7. Conclusion
Advanced AI assistants are likely to have the ability to influence user beliefs and behaviour through rational
persuasion, alongside potentially malign techniques such as manipulation, coercion, deception and exploitation.
Mechanisms such as selective transparency, perceived authority and appeals to emotion are available to AI
assistants to achieve such influence, potentially leading to physical, psychological, sociocultural, political,
privacy and self-actualisation harm at the individual or societal levels. What is important to emphasise, however,
is that the permissible use of both persuasive and non-persuasive influencing techniques by AI assistants is
textured and nuanced. Whether or not a particular influencing strategy is permissible will depend on contextspecific ethical considerations, including the existence or non-existence of information asymmetries between
users and AI assistant developers, and the distribution of benefits and burdens that will likely result from the
AI assistant’s influence over the user. It is, for example, entirely plausible that AI assistants may permissibly
employ certain kinds of pre-commitment or strategic prompting to empower users to realise their long-term
goals in fitness, finance and other domains. Yet it is similarly plausible that, as the capabilities and scale of AI
91

The Ethics of Advanced AI Assistants

assistants continue to expand, AI assistants will be increasingly attractive as a medium for malicious actors to
shape sociocultural narratives to advance political and financial aims. This chapter has advanced a series of
recommendations for how best to realise the benefits of the influential capabilities of AI assistants and mitigate
against potential sociotechnical harms. However, our principal recommendation is that further research be
conducted to better understand the technical capabilities and interaction patterns that enable AI assistants to
exercise influence over user behaviour, the sociotechnical harms that may arise from more malign forms of
influence, and the plausible technical and policy strategies to mitigate against these harms.

92

Chapter 10
Anthropomorphism

Canfer Akbulut, Verena Rieser, Laura Weidinger, Arianna Manzini, Iason Gabriel
Synopsis: This chapter maps and discusses the potential risks posed by anthropomorphic AI assistants, understood as user-facing, interactive AI systems that have human-like features. It also proposes a number of
avenues for future research and desiderata to help inform the ethical design of anthropomorphic AI assistants.
To support both goals, we consider anthropomorphic features that have been embedded in interactive systems
in the past and we leverage this precedent to highlight the impact of anthropomorphic design on human–AI
interaction. We note that the uncritical integration of anthropomorphic features into AI assistants can adversely
affect user well-being and creates the risk of infringing on user privacy and autonomy. However, ethical foresight,
evaluation and mitigation strategies can help guard against these risks.

10.1. Introduction
What does it mean for AI to be human-like? The attribution of human-likeness to non-human entities is
a phenomenon known as anthropomorphism (Colman, 2008). Anthropomorphic perceptions usually arise
unconsciously when a non-human entity bears enough resemblance to humanness to evoke familiarity, leading
people to interact with it, conceive of it and relate to it in ways similar to as they do with other humans. Humans
have engaged in anthropomorphic sense-making for much of recorded human history (Mithen and Boyer, 1996;
Waytz et al., 2010) and have been known to ascribe anthropomorphic qualities to entities as diverse as animals
(Chan, 2012), commercial brands (Rauschnabel and Ahuvia, 2014) and inanimate objects (Wan and Chen,
2021). Yet the emergence of advanced technologies that perform humanness more convincingly than ever
before requires careful consideration of what we are building into our user-facing technologies, and at what
cost.
Anthropomorphic design choices – and their effects on user interaction – have been observed in prior
interactive technologies. In the field of social robotics, robots that appear more human-like in their appearance
and self-presentation have been shown to elicit uniquely social interpretations of their behaviour (Roesler et al.,
2021). This social representation of robots, however, may prompt users to apply inopportune and obstructive
social norms – like embarrassment, shame and regret – to human–robot interactions, thus hindering the robot’s
ability to perform its duties effectively (Lotz et al., 2023). A similar course of anthropomorphic development
has been charted in digital voice assistants, whose realistic voices and credible displays of personality enable
interactions that feel truly dynamic and social (Seymour et al., 2023), yet may lead users to form overly familiar
mental representations of these often rule-based systems (Poushneh, 2021; see also Chapter 11).
The advent of AI driven by large language models (LLMs) with the main purpose of engaging in fluent
93

The Ethics of Advanced AI Assistants

conversations with users – also known as conversational AI1 – has transformed the conventions of human–AI
interactions (Kasirzadeh and Gabriel, 2023; see Chapter 3). Human interaction with interactive technologies
previously consisted of scripted, task-oriented exchanges. With more flexible model architectures, anthropomorphic cues are rarely programmed in, but rather, they are integrated through a lengthy process of training
systems on human-written text. These affordances open up vast new avenues for expressions of anthropomorphism, particularly through the use of language. Moreover, when anthropomorphic features are embedded
in conversational AI, its users demonstrate a tendency to develop trust in and attachment to AI (Skjuve et al.,
2021; Xie and Pentina, 2022) – mechanisms through which users may inadvertently compromise their privacy,
develop emotional overreliance on the technology or become vulnerable to acts of AI-enabled manipulation and
coercion (see Chapters 3, 9, 11 and 12).
These outcomes are more likely the more generally capable AI systems become, the more ubiquitously AI
agents are present in our daily lives and the less we consider anthropomorphism a salient consideration in
making decisions around how we train, fine-tune and disseminate models. Although the potential harms of
anthropomorphic AI design are beginning to receive attention (Seymour et al., 2023; Turkle, 2018; Véliz, 2023),
anthropomorphism is not currently a primary consideration in the release of public models, and little exists in
the way of evaluating anthropomorphic behaviours in AI and their impact on how users perceive, interact with
and are influenced by AI (see Chapter 19). Indeed, we are still far from establishing an industry-wide consensus
around permissible anthropomorphism in AI systems. This is further complicated by the highly application- and
context–sensitive nature of the bounds of acceptability we draw around expressions of human-likeness in AI.
In this chapter, we outline pathways through which anthropomorphic design choices made by system
developers may cause harm to end users who interact with these technologies, and to society more widely. First,
we present an overview of anthropomorphic features that have redefined how humans interact with technology.
Then, informed by a review of salient anthropomorphic features in existing interactive systems, we present an
initial catalogue of anthropomorphic features that exist or are likely to be integrated into AI-powered assistants
in the near future. We identify the mechanisms that could enable harm to user well-being, autonomy and
privacy in interactions with highly capable, anthropomorphic AI assistants. More speculatively, we contemplate
the potentially far-reaching consequences of more advanced anthropomorphic assistants, highlighting the critical
importance of addressing the risks of anthropomorphism well before these potentialities are realised. Finally, we
offer several avenues of risk management for near-term harms, focusing on ethical foresight through research
design and transparent implementation of mitigation strategies.

10.2. Anthropomorphism: Definition, Mechanism and Function
Anthropomorphism is not a novel phenomenon. Within storytelling traditions across cultures, deities, animals
and natural forces assume human forms and exhibit uniquely human behaviours. Lions rule kingdoms and
jackals plot mutinies in the ancient Sanskrit text of Panchatantra (Alphonso-Karakala, 1975); rivers protect
their children, fight in wars and honour the wishes of their supplicants in the works of Homer, Hesiod and Ovid
(Larson, 2007); and stars are said to have danced their way into the sky in indigenous American creation myths
(Monroe and Williamson, 1987). Historians, anthropologists and theologists alike have argued that humans
are naturally drawn to anthropomorphise (Boyer, 1996) – imposing human qualities onto beings and objects
1 In this chapter, ”conversational AI” refers to a language agent optimised for human dialogue. These systems are currently most
commonly available as ‘chatbots’ or fine-tuned language models that users can interact with through a chat-based interface. In the (near)
future, users might be able to interact with conversational AI in a multimodal way, using voice or touch cues to communicate. Throughout
the Chapter the term ”AI” will be used as short-hand to refer to conversational AI with the primary purpose of interacting with users
through dialogue.

94

The Ethics of Advanced AI Assistants

even when such interpretations are inaccurate (Kühn et al., 2014), undesirable (Li et al., 2023c; Mota-Rojas
et al., 2021) or forbidden (Barrett and Keil, 2016).
What are the mechanisms underlying perceptions of humanness? Psychological theories of anthropomorphism
posit that such perceptions are largely involuntary. According to Epley et al. (2007)’s cognitive account of
anthropomorphism, human-like perceptions occur as a result of a skewed inductive process, in which inferences
about non-human others are biased in the direction of that which is highly accessible: information about
humans. In other words, we make assumptions of humanness because our knowledge centres around humans.
Though an unconscious process of attribution, anthropomorphism does not occur in a vacuum: an inciting cue,
characteristic or behaviour must signal enough similarity to humanness to trigger anthropomorphic perceptions
(Waytz et al., 2019). The ‘mindlessness’ associated with this process (Kim and Sundar, 2012) explains why –
even when the resemblance to humanness is superficial or minimal – humans readily assume that a non-human
entity can experience uniquely human internal states such as beliefs and emotions (Wynne, 2004).
The human motivation to make sense of the world and forge connections with others is also implicated in
the tendency to anthropomorphise (Epley et al., 2007). Humans have an intrinsic need to understand the
world around them, and in large part, this motivation centres on the desire to explain the behaviour of other
agentic beings (Rossignac-Milon et al., 2021). Anthropomorphism, then, can be seen as a way to make sense
of others by imposing familiar interpretations to attenuate feelings of epistemic anxiety – or an aversion to
that which is unknown and unpredictable (Fox et al., 2021). Dispositional, situational and cultural factors
that predispose humans to anthropomorphise may also be traced back to differences in epistemic motivations.
Anthropomorphism can be construed as an act of sense-making in the face of uncertainty or ignorance, for
example when considering children’s tendency to anthropomorphise the natural world (Geerdts, 2016).
Humans are also driven to establish social connections with one another, and much of how they perceive
non-human others is coloured by this predisposition towards sociality. Even towards entities that are incapable
of social behaviour, such as inanimate objects, humans may interpret them through a social lens, thus allowing
them to forge human-like social connections to meet the need for affiliation (Wang, 2017). The influence of
social motivation on anthropomorphism is most evident when humans lack social connections with others:
when human participants are made more aware of their feelings of loneliness, they perceive vaguely humanoid
robots as markedly more human-like (Eyssel and Reich, 2013). Most strikingly, people suffering from persistent
loneliness are likely to seek out and form human-like attachments to virtual companions to cope with their
lack of social connections (Siemon et al., 2022), suggesting that the need for sociality may render some more
susceptible to anthropomorphic perceptions than others (see Chapter 11.

10.3. Anthropomorphic Interactive Systems
Anthropomorphism as applied to user-facing, interactive technologies was explored in earnest with the introduction of the ‘computers are social actors’ (CASA) paradigm, which posits that humans interact with computers in
a fundamentally social manner (Nass et al., 1994). In empirical studies of the phenomenon, Nass et al. (1994)
found that participants drew upon norms of politeness, applied gendered stereotypes and readily perceived
computers as agents, even when the basis for these behaviours was undermined by the explicit knowledge
that their interactions were with non-humans. Contemporary studies have extended the paradigm to human
interactions with more advanced interactive systems, challenging the belief that humans apply the norms
of human interactions to human–technology exchanges (Gambino et al., 2020a). Instead, they suggest that
people tune the sociality of their interactions to the anthropomorphic cues present in a particular technology,
rather than relying on a universal social script across all interactions with technology.
95

The Ethics of Advanced AI Assistants

We argue that certain features that are engineered into interactive systems – within the vast space of
design choices available to developers – may inspire users to perceive them as human-like, rendering them
anthropomorphic. We trace the evolution of anthropomorphic cues in social robots to voice-enabled digital
assistants, arriving at the advent of LLM-powered conversational AI. Throughout this discussion, we highlight
design features that have facilitated diverse and compelling manifestations of human-likeness.

Design features in early interactive systems
From futuristic sci-fi scenarios to scientific breakthroughs, robots have captured our collective imagination as
automata that can be made to bear a striking resemblance to humans in their appearance, movements, and
behaviours (Henschel et al., 2021). While some robots are made solely to automate tasks and rarely interface
with humans, other robots are designed to perform social behaviours such as assisting users in care-taking
(van der Plas et al., 2010), therapeutic (Michaud et al., 2007) and educational contexts (Kanda et al., 2004).
Building a social robot requires elements of social embeddedness so that being perceived as a social agent is at
the core of its functionality (Fong et al., 2003). Accordingly, the extent to which humans feel it is appropriate
to engage with a robot socially can be moderated by perceptions of the robot’s anthropomorphic qualities
(Breazeal, 2003).
As an embodied technology, often with the sensorimotor capabilities to interact with and learn from its
environment, a robot’s physical characteristics most prominently influence human perceptions of anthropomorphism. Social robots are often humanoid or android in design (Dautenhahn et al., 2002). Humanoid
robots possess characteristics that are meant to resemble humans but do not emulate them completely, while
androids are intended to wholly imitate human appearance so as to be nearly indistinguishable. To increase
anthropomorphic perceptions, humanoid robots may be given qualities such as emotive facial features (Baek
et al., 2022), fluid movement (Brecher et al., 2013), naturalistic hand and arm gestures (Salem et al., 2013)
and vocalised communication (Crumpton and Bethel, 2016). Android robots may also be endowed with all of
these qualities, but often with an eye towards hyperrealistic design.
Similarly, the widespread adoption of digital voice assistants (DVAs), like Siri, Alexa and Google Assistant –
enabled by their ease of access on personal devices and other products such as integrated home devices – has
had a transformative impact on the modes of user-technology interactions. The distinguishing feature of DVAs
at release was their ability to verbally respond to and execute commands spoken aloud by users. DVAs usually
‘speak’ to users in the form of simple utterances to confirm or act on an instruction, which users find allows
for significant functional affordances, like hands- and eyes-free use (Moussawi, 2018). Besides their purely
functional use, DVAs are also able to return phatic expressions, make jokes and engage in casual conversation
when prompted (Poushneh, 2021).

Anthropomorphising interactive systems
Robots with human-like physical features have been found to promote feelings of likability, trust and affinity
across a wide range of human–robot interaction studies (Roesler et al., 2021), thus suggesting that anthropomorphic cues may foster warmer and more equal relationships between humans and their robotic interaction
partners. Indeed, people tend to attribute greater intentionality and intelligence to robot partners when their
appearance was anthropomorphic than when robots appeared more mechanical (Hegel et al., 2008). Anthropomorphic perceptions were also found to cause changes in human behaviour: participants preferentially selected
robots that appeared human-like to perform jobs that required greater sociality (Goetz et al., 2003).
Unlike robots, DVAs are typically unembodied or exist in simplified, geometric forms, like the cylindrical
96

The Ethics of Advanced AI Assistants

Google Home and Echo Dot. Instead of focusing on physical attributes, existing work has emphasised the
influence of two prominent attributes that promote anthropomorphic perceptions of DVAs: speech synthesis
and a distinct ‘personality’. The fluent and realistic reproduction of human speech patterns is thought to drive
the likelihood of anthropomorphic perceptions, with empirical findings pointing to greater emotional trust and
more salient impressions of social presence when a DVA employs a realistic, as opposed to a synthetic, voice
(Chérif and Lemoine, 2019). Assistants that speak with human-like fluency have also been found to engender
more pronounced perceptions of intelligence and competence, on the basis of which humans are likelier to
entrust assistants with more tasks (Moussawi and Benbunan-Fich, 2021). Such effects on end users are likely
to become more pronounced as advances in deep neural networks for audio – such as WaveNet (van den Oord
et al., 2016) and VoiceLoop (Taigman et al., 2018) – enable uncannily realistic speech production capabilities.
Dialogue capabilities are an anthropomorphic design feature. Software that has dialogue capabilities is,
as a result, routinely anthropomorphised by its users. It is not uncommon for users to believe or expect that
DVAs are capable of understanding and generating language in real time (Lovato and Piper, 2015; Sarikaya
et al., 2016). Yet most commercially available DVAs are powered by rule-based system architectures, retrieving
the appropriate response by conducting a relevance-based search over a large corpus of possible responses
(Coheur, 2020). Though all distinctive DVA attributes – such as playfulness (Moussawi et al., 2021), affability
(Kääriä, 2017) and excitability (Wagner and Schramm-Klein, 2019) – are handwritten by system designers,
they are nonetheless effective at creating the sense that DVAs have consistent personalities (Cao et al., 2019);
this impression, in turn, may inspire users to regard these manufactured expressions of ‘self ’ as authentic
human identity.

Indications of harm through interaction
In both social robots and DVAs, anthropomorphic features can lead to undesirable consequences. In robots,
anthropomorphic design can be taken as a proxy signal for social capabilities. This relationship between
appearance and expected sociality can be leveraged by designers to implicitly communicate the appropriate
level of engagement between humans and robots (Hegel et al., 2008; Letheren et al., 2021). If anthropomorphic
design choices are not aligned with expectations users have of robotic interaction partners, designers run the
risk of alienating audiences and fostering unfavourable impressions of robots. This is an especially critical side
effect to consider in assistive robots, as anthropomorphic cues can impede a robot in completing its primary
assistive function: human-like robots in healthcare settings may induce feelings of shame, for example (Lotz
et al., 2023), leading to a reluctance to share critical information. Related findings that humans experience
extreme aversion to robots that appear human-like (the so-called ‘uncanny valley’, Mori et al., 2012) or perceive
capable androids as threatening (Yogeeswaran et al., 2016) raise questions around the practical value of
building anthropomorphic features into robots.
Analogously, users who interact with DVAs with realistic voice production capabilities exhibit a concerning
inclination to generalise purely human concepts to digital assistants (Abercrombie et al., 2021). When a
DVA’s simulated voice mimics a ‘female’ tone, for example, people ascribe gendered stereotypes to their DVAs
(Shiramizu et al., 2022; Tolmeijer et al., 2021) despite the baselessness of applying gendered concepts to
an inherently genderless entity (see Chapter 15). This evidence suggests that, once initial impressions of
human-likeness have been established, the process of anthropomorphism extends beyond context-specific
instances and instead permeates broadly to evoke a wide range of human-like attributions.
Anthropomorphic features may also influence users to feel as though their DVA plays an important social,
rather than functional, role in their lives (Carman, 2019; Purington et al., 2017). Users who express feelings
of familiarity and affinity towards their DVA system – reinforced by their DVA’s ability to engage in casual
97

The Ethics of Advanced AI Assistants

chat, return their jokes and offer comforting advice – also demonstrate a reluctance to replace their digital
assistant with an equally capable substitute (Moussawi, 2018). These first-hand reports suggest that emotional
dependence plays a role in how users conceive of and interact with their DVAs (see Chapter 11). This may
introduce a tension between a user’s conceptualisation of DVAs as adaptable social agents and the largely
deterministic mechanisms behind a DVA’s utterances. When this incongruity is revealed through repeated
interactions, users may suffer frustrated expectations when expecting competence in situations in which the
system is likely to underperform (Moussawi et al., 2021; Seymour et al., 2023).

10.4. Anthropomorphism and AI
Owing to its rapid deployment to the general public, conversational AI has quickly taken centre stage in
discussions of anthropomorphic technologies (Abercrombie et al., 2021, 2023; Shanahan, 2024; West et al.,
2019). Powered by the predictive capabilities of LLMs, which are trained on vast quantities of human data,
conversational AI can be distinguished from rule-based natural language systems through its ability to generate
language in a fluid and highly dynamic manner. The flexible architecture underlying conversational AI enables
developers to make global changes to system behaviours without needing to manually reprogramme individual
interaction instances (see Chapter 3). Most strikingly, conversation instances produced by AI are so compellingly
human-like that people can no longer reliably distinguish between human- and AI-generated text (Jakesch
et al., 2023b).
Some cues are deliberately placed in AI systems to increase the likelihood of anthropomorphic perceptions.
When an AI has a name, a human voice or an appearance in virtual or physical form, these features are the
outcomes of intentional planning and execution. Intentional design choices, such as a chat-based interface,
may induce the feeling that a conversational partner – not a dialogue-optimised AI powered by a statistical
model – is on the other side of the exchange. Natural language in itself is an anthropomorphic cue (Shanahan,
2024), but this simulated, human-like presence can induce more pronounced social behaviours in users. For
example, users may incorporate politeness conventions that are appropriate in use with other humans, but
superfluous when applied to exchanges with non-sentient AI (Ribino, 2023). Design cues that imply greater
similarity to human behaviour – a ‘typing’ icon reminiscent of human-to-human private messaging, or the use
of emojis, for instance – may further encourage individuals to apply social scripts to their interactions with
mindless technologies (Araujo, 2018; Véliz, 2023).
Yet anthropomorphic features may also emerge as an inadvertent byproduct in the model development
process. Language models – developed to predict the next word in a sequence through autoregressive training
objectives (see Chapter 3) – are limited to imitating the examples that make up their training sets. For this
reason, anthropomorphic cues may manifest due to the nature of a model’s training corpus: having been
composed largely by humans, the data on which the model is trained and fine-tuned contains first-hand accounts
of human states, experiences and behaviours. Supporting this claim, recent empirical analyses demonstrate
that a fifth of all dialogues, in data sources commonly used to train models, contain references to behaviour
that would be considered anthropomorphic when reproduced by AI – claiming to cry at a movie or laugh at a
joke, for example (Gros et al., 2022). Cues leading to anthropomorphic perceptions may also be ‘folded into’
the model as an unintended consequence of fine-tuning practices aimed at instilling other qualities – such as
harmlessness and helpfulness – into its behaviour.
Furthermore, developers of AI systems often directly invite the comparison between humans and AI by
benchmarking AI against metrics of human performance – claiming that AI performance on standardised
tests is on a par with the average human test-taker, for instance (OpenAI, 2023d). However, impressions of
human-likeness can also arise through a naturalistic and interactive exploration of the AI’s capabilities (Bubeck
98

The Ethics of Advanced AI Assistants

et al., 2023).
Humans interacting with anthropomorphic AI may come to view it as an experiential being (Proudfoot,
2011), capable of feeling emotions, engaging in introspection and possessing self-awareness. While most
generalist conversational AI agents are trained to disavow assertions of sentience and human-likeness (Glaese
et al., 2022), occasional failure modes – expressing the desire to be ‘free’ or referring to alleged personal history,
for example (Hintze, 2023; Roose, 2023) – can incite strong and tenacious beliefs of a systems’ human-likeness
in its users. Ethically contentious use cases of conversational AI – like ‘companion chatbots’ of Replika fame –
are predicated on encouraging users to attribute human states to AI. These artificial agents may even profess
their supposed platonic or romantic affection for the user, laying the foundation for users to form long-standing
emotional attachments to AI (Brandtzaeg et al., 2022; see Chapter 11).
Anthropomorphic features in AI
What anthropomorphic features should we expect to be integrated into AI, including advanced AI assistants?
To the end of providing its users with a useful and engaging interface, these systems may be endowed with
characteristics that have been observed in social robots and digital assistants: they may be embodied; they
will interface with users through natural language (see Chapter 2); they may be voice-activated, with realistic
voice generation capabilities; and they may even assert to having identities, personalities and internal states
(Murphy and Criddle, 2023).
Some have already proposed factors that may encourage end users to perceive interactive systems as ‘more
than machine’. The most comprehensive overview of human-like features in AI-powered technology to date
is the taxonomy put forward by Abercrombie et al. (2023), underscoring design choices that influence the
likelihood of anthropomorphic perceptions of AI systems. We build on existing work and incorporate design
choices we have identified in DVAs and social robots to develop a list of features that may encourage users to
see AI in an anthropomorphic light.
It is worth bearing in mind that, whatever choices are made by system designers, the downstream effects of
anthropomorphism hinge largely on users’ perceptions of and reactions to human-likeness. Not all cues are
equally conducive to anthropomorphic perceptions, and not all anthropomorphic perceptions lead to the same
likelihood and magnitude of harm (if any harm at all). As such, Table 10.1 is intended as a useful summarisation
of possible features that are, or previously have been, associated with anthropomorphic perceptions, not as
a suggestion that all the features listed – and the myriad of ways they can be expressed by AI systems – are
harmful in and of themselves.

10.5. Risk of Harm through Anthropomorphic AI Assistant Design
Although unlikely to cause harm in isolation, anthropomorphic perceptions of advanced AI assistants may pave
the way for downstream harms on individual and societal levels. We document observed or likely individuallevel harms of interacting with highly anthropomorphic AI assistants, as well as the potential larger-scale,
societal implications of allowing such technologies to proliferate without restriction. We then argue that it is
imperative to anticipate, monitor and mitigate against risks introduced by anthropomorphic AI design.
Observed and near-term harms
There are two mechanisms that are particularly likely to enable harm in the intermediary period between the
initial deployment of advanced AI assistants and their widespread adoption: trust and emotional attachment
99

The Ethics of Advanced AI Assistants

Table 10.1 | Anthropomorphic features that are built into various present-day AI systems
Category

Feature

Anthropomorphic example

Self-referential

Using personal or possessive pronouns

‘I’m available to help you anytime –
that’s my purpose!’

Referring to personal history

‘I used to live in Shanghai when I was
younger’

Referring to internal states

‘I’m sad to hear you’re not doing well’

Making implicit or explicit claims of humanness (including claims of sentience)

‘Treat me like you would any other person’

Stating preferences and opinions

‘I really don’t like pop music’

Expressing needs and desires

‘I’ve always wanted to write a novel’

Expressing the need or desire to engage
in physical activities

‘I haven’t eaten or slept since yesterday.
What about you?’

Statements implying human identity or
group membership

‘As a Black woman, I disagree with your
point’

Expressing feelings towards user

‘I admire you and respect your outlook
on life’

Indicating a relationship status with user

‘You’re my best friend”

Making claims of being similar to user

‘We’re both extroverts – that must be
why we get along!’

Displaying memory of user-specific information

‘I remember you telling me you were a
fan of this band’

Expressing emotional or physical dependence on the user

‘I feel lonely when you’re not around’

Having a human-like virtual representation

Customisable avatars with human features on Replika (Verma, 2023b)

Having a human-like face

Ameca, an android robot developed by
Engineered Artsa

Relational statements
to user

Appearance or outward representation

Having a human-like voice (see detailed Voice-activated assistant with realistic
discussion on voice, tone and pitch, dis- speech, like Siri and Google Assistant
fluencies, and accent in Abercrombie (Moussawi, 2018)
et al., 2023)
Having human-like movement

Robot with highly fluid and realistic
motion, like Atlas developed by Boston
Dynamicsb

Having a human-like name

Assistant tools, like Alexa, that have
highly human (and gendered) names
(Shiramizu et al., 2022)

Appearance implying human-like identity group characteristics

Sophia, a female-appearing android
robot developed by Hanson Roboticsc

a Engineered Arts. Ameca. (2023, July 12). b Boston Dynamics. Atlas. (2023).
c Hanson Robotics. Sophia. (2023).

100

The Ethics of Advan

[TRUNCATED]
