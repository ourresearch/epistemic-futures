---
title: "The wisdom of polarized crowds"
person: james-evans
section: by
type: journal-article
year: 2019
date: 2019-03-04
venue: "Carolina Digital Repository (University of North Carolina at Chapel Hill)"
authors: "Feng Shi, Misha Teplitskiy, Eamon Duede, James A. Evans"
source_url: https://cdr.lib.unc.edu/record/uuid:447b5018-ea2d-40b9-9c27-fec04dc4f9b4
openalex_id: https://openalex.org/W3101346006
retrieved: 2026-08-13
content: full-text
notes: "OpenAlex duplicates merged: W3101346006 W2780711780 W4288481351; full text extracted from the arXiv PDF; text taken from duplicate OpenAlex record W2780711780"
---

# The wisdom of polarized crowds

## Full text

The Wisdom of Polarized Crowds
Feng Shia,1 , Misha Teplitskiyb,1,∗, Eamon Duedec,d , James A. Evansd,e,∗

arXiv:1712.06414v1 [cs.SI] 29 Nov 2017

a

Odum Institute for Research in Social Science, University of North Carolina at Chapel Hill
b
Laboratory for Innovation Science, Harvard University
c
Committee on the Conceptual and Historical Studies of Science, University of Chicago
d
Knowledge Lab, University of Chicago
e
Department of Sociology, University of Chicago

Abstract
As political polarization in the United States continues to rise, the question of whether polarized individuals can fruitfully cooperate becomes pressing. Although diversity of individual
perspectives typically leads to superior team performance on complex tasks, strong political
perspectives have been associated with conflict, misinformation and a reluctance to engage
with people and perspectives beyond one’s echo chamber. It is unclear whether self-selected
teams of politically diverse individuals will create higher or lower quality outcomes. In this
paper, we explore the effect of team political composition on performance through analysis
of millions of edits to Wikipedia’s Political, Social Issues, and Science articles. We measure
editors’ political alignments by their contributions to conservative versus liberal articles. A
survey of editors validates that those who primarily edit liberal articles identify more strongly
with the Democratic party and those who edit conservative ones with the Republican party.
Our analysis then reveals that polarized teams—those consisting of a balanced set of politically diverse editors—create articles of higher quality than politically homogeneous teams.
The effect appears most strongly in Wikipedia’s Political articles, but is also observed in Social Issues and even Science articles. Analysis of article “talk pages” reveals that politically
polarized teams engage in longer, more constructive, competitive, and substantively focused
but linguistically diverse debates than political moderates. More intense use of Wikipedia
policies by politically diverse teams suggests institutional design principles to help unleash
the power of politically polarized teams.
Keywords: Team performance, Diversity, Political polarization, Crowd-sourcing, Wikipedia
1. Introduction
Recent political events, including the 2016 presidential election, have underscored growing
political divisions in American society. Political speech has become markedly more polarized
in recent years [1], tracing a growing divergence between platforms of the major political parties [2] and leading to a state of political hyper-partisanship [3]. Yet the effects of political
difference are not confined to the domain of politics alone. A growing literature documents
∗
1

To whom correspondence should be addressed: mteplitskiy@fas.harvard.edu; jevans@uchicago.edu
FS and MT contributed equally to this work.

how individual political alignments shape personal consumption of ostensibly non-political
products, news, cultural and scientific information [4, 5, 6, 7, 8]. This literature has converged
on an alarming narrative: despite early promise of the world-wide-web to democratize access
to diverse information [9], increased media choice and social networking platforms have led
to the converse. Collaborative filtering allows individuals to passively enter “echo chambers”
that limit the variety of information they observe and trust [10, 11, 12]. These can degrade
the quality of individual decisions, including those that undergird basic democratic institutions [13, 14, 15]. Psychological mechanisms such as motivated reasoning [16, 17] and a
tendency to discount identity-incongruent opinions [14, 18] stimulate and reinforce polarizing
information. Opposing social identities can foment conflict and even make communication
counter-productive [19].
Nevertheless, a large literature documents the largely positive effect that social differences can exert on the collaborative production of information, goods and services [20, 21].
Research demonstrates that individuals from socially distinct groups embody diverse cognitive resources and perspectives that, when cooperatively combined in complex or creative
tasks produce ideas, solutions, and designs that outperform those from homogeneous groups
[22, 23, 24, 25]. Collaborations between inventors from distinct social groups result in more
creative patents [26], scientific teams representing distinct disciplines produce more highly
cited papers [27], and gender diversity broadens the questions scientists ask [28].
The effect of political diversity on the collective production of knowledge, however, remains unclear. Insights from cognitive diversity research suggest that political diversity, like
other forms of diversity, should positively impact the quality of group production. Literature on echo chambers suggests that political diversity may hamper productive cooperation,
however, as partisans perceive information held by opponents as not simply different, but
wrong. In short, political diversity should increase access to fresh perspectives and information but may also undermine the quality of discourse and engagement required to enjoy the
performance benefits typically obtained by diverse groups.
In order to assess the effect of political diversity on team performance, we studied the
effect of political polarization on the performance of approximately four hundred thousand
online teams. Specifically, we focused on teams of Wikipedia editors who worked on Englishlanguage articles in three large domains: Politics, Social Issues, and Science.
Data and Methods
Using edit histories, we measured the political alignments of millions of Wikipedia editors
by the relative amount of content they contributed to conservative versus liberal political articles. We validated this measure by surveying a random sample of Wikipedia editors for
whom we had calculated the index. We then used a machine learning algorithm developed
by Wikimedia’s internal researchers to measure the quality of Wikipedia articles [29]. We
finally related article quality to the political diversity of teams, and, to gain insight regarding the mechanisms of collaboration among polarized teams, we computationally explored
characteristics of article “talk pages” where the work of editing and debate occurs.
Data collection
We extracted data from the complete English Wikipedia database dump on 12/01/2016.
Data includes all edits made to all English Wikipedia pages since its start until 12/01/2016.
2

Within this dump, we focused on three sets of articles: politics (20,947 pages), social issues
(162,085 pages) and science (49,530 pages), which represent approximately 5% of all English
Wikipedia articles. Summary statistics of the three corpora may be found in Table A.2.
Users’ total numbers of edits ever made to Wikipedia were collected through Wikipedia’s
online API.2 .
The corpus of Political pages consists of two sub-corpora, Liberal and Conservative pages.
The Liberal sub-corpus consists of all pages categorized under the “American liberalism”
category and its subcategories. For instance, the page “New Deal coalition” is directly under
the “American liberalism” category, while “The New Republic” is located under the subcategory “American liberalism ¿ Modern liberal American magazines”. The Conservative
sub-corpus was collected in a similar fashion starting with the “American conservatism”
page. For instance, “American Conservatism” links to “Economic liberalism,” which links
to “Market economy,” and all three pages are in the “Conservative” sub-corpus. Pages
appearing in both corpora were removed.
Titles of Social Issues pages were collected starting from the page “Category:Social issues” 3 . We collected all pages and subcategories linked from the page; repeating this process
in every subcategory of Social Issues, stopping 4 levels down from the root. Social Issues
include articles relating to human welfare and justice, including “Homelessness,” “Teenage
pregnancy,” and “Social services.” These pages tend to be relatively controversial and politically salient. Titles of science pages were collected similarly, following the category structure
of scientific disciplines in Wikipedia, starting from the page “Category:Scientific disciplines”
4
and following the iterative procedure pursued for Social Issues pages.
Survey of Wikipedia editors
To validate our statistical measure of political alignments, we surveyed a random sample of
editors for whom we had estimated alignment scores. We worked directly with the Wikipedia
community and Wikimedia staff to carry out the survey, including the development of a research page on the Wikimedia “Meta-Wiki” site and direct engagement with those expressing
concerns therein5 . The arrived-upon process required a single member of our team (E.D.) to
personally post the survey link on each editor’s page along with an explanation. The number
of solicitations we could make per day (and their total number) was capped. In the end, we
were able to post 500 solicitations6 and received 118 responses. The survey was approved
by the University of Chicago’s Institutional Review Board (IRB17-0679). More information,
including response rates by (computationally measured) political alignment may be found in
Appendix.
Measurement
For each user, we used total size (in bytes) of contributions she made to liberal (blue)
versus conservative (red) articles to infer her political alignment. Specifically, we model the
2

http://en.wikipedia.org/w/api.php
https://en.wikipedia.org/wiki/Category:Social issues
4
https://en.wikipedia.org/wiki/Category:Scientific disciplines
5
https://meta.wikimedia.org/wiki/Research:Wikipedia %2B Politics
6
The survey may be viewed here: https://uchicago.co1.qualtrics.com/jfe/form/SV eXOHLbXwbpfYC1f
3

3

total bytes she contributed to red articles (X) as a random variable satisfying a binomial
distribution X ∼ Binomial(K, p), where K is the total number of bytes contributed to
political articles (red or blue) and p is the probability of contributing to red articles. This
probability p represents our measure of political alignment for this editor, after rescaling
it to the range -1 (most liberal) to +1 (most conservative). The parameter p is an unknown
quantity to be estimated from observations X and K. We estimated it through a conservative,
Bayesian framework described in Appendix. The quantity of primary interest is the variance
of alignments among a group of editors, which quantifies the spread of editors across the
liberal-conservative spectrum. We used the variance of political alignments as the measure
for polarization of any group of editors. Previous research has found that this measure most
directly captures the cognitive diversity of a group along a particular demographic dimension
[30].
Results
Editors’ political alignments
We measure editors’ alignments by the fraction of bytes they contribute to “Conservative”
versus “Liberal” articles on the English-language Wikipedia, with a Bayesian framework
to account for random edits. The corpus of conservative articles consists of all articles
categorized under “Conservatism in the United States7 ,” and similarly for “Liberalism in the
United States8 .” This procedure scores editors as politically neutral (≈ 0) if they contribute
equally to both sets of articles or little to either set, and closer to -1 or +1 the more exclusively
they contribute to liberal or conservative articles, respectively.
118 responses from a survey targeted at randomly chosen editors of science and political
articles validate our computational measure of political alignment (Figure 1 A). Respondents’
self-reported political party identification correlates at roughly 0.35 with our computational
measure of conservative-liberal alignment, and validates our use of editing history as a (noisy)
behavioral indicator of political preferences.
With inferred political alignments, we observe that Wikipedia editors display a wide
distribution of political alignments (Figure 1 B). The peak at the center of the distribution
comports with our observation that a large number of people only contributed minor edits
to Wikipedia, such as correcting a typo. There are also two lower but significant peaks at
the tails of the distribution, which identify editors who contribute substantial content to
either liberal or conservative articles and suggest substantial polarization on Wikipedia. The
variance of alignments across all editors of political articles is 0.04, significantly higher than
random (See Appendix for details on random simulations). We then measure the polarization
of any given group of editors by the variance of their alignment scores.
As the number of editors for an article increases, their average political alignment converges to 0 (Figure 2). This phenomenon is sometimes referred to as Linus’ law – “with
enough eyeballs, all bugs are shallow.” In our case, articles attracting more attention tend to
have more balanced engagement from editors along the conservative-liberal spectrum. This
finding replicates those reported by Greenstein and Zhu [31, 32] in their studies of bias in
7
8

https://en.wikipedia.org/wiki/Category:Conservatism in the United States.
https://en.wikipedia.org/wiki/Category:Liberalism in the United States.

4

A

B

C

Figure 1: A. Scatter plot of implied political alignment (-1=most liberal, +1=most conservative) and
political identification (1=Strong democrat, 4=Independent, 7=Strong republican) reported by US-based
survey respondents. Respondents identifying as “Independent” were excluded from analysis, and 7
responses of “Other” were recoded to either “3=Independent, Near Democrat” or “5=Independent, Near
Republican” (see Appendix for details). Dotted line is the best-fitting Logistic sigmoid, and its curvature
suggests that even those at the boundary of our editing measure tend to “switch” between Republican and
Democratic identification. Pearson correlation coefficient between the two measures is ρ = 0.35
(n = 28, p = 0.036, 1-tailed t-test). B. Distribution of editors’ computationally measured political
alignments. C. Article quality (Stub=lowest, FA=highest) by average team polarization for Politics
(purple), Social Issues (orange) and Science (green) articles. Bands around each mean denote its %95
confidence interval. Lines are best linear fits to the points in the plot.

Wikipedia’s US political coverage, showing that increased editor interaction reduced individual biases and yielded greater content neutrality.
Effects on Quality
We measure the quality of articles using a machine learning model developed by Wikimedia research staff and trained on features of article content alone – no features of the editors
were used to train the model. The 6-category quality scale for Wikipedia articles ranges
from “Featured article” (highest quality) to “Stub” (lowest quality). Figure 1 C plots the
relationship between average team polarization (i.e., variance of alignments) and quality for
Political, Social Issues, and Science articles.
In all three corpora – Political, Social Issues, and Science articles – higher polarization
is associated with higher quality. To establish this relationship statistically, we estimated
an ordinal logistic regression model at the article level with article quality as outcome and
polarization as main independent variable. We added the absolute value of mean team
alignment to account for the possibility that article quality is related to the deviation of
political alignment from neutral (0) in either direction. Additionally, we added controls for
article and editor features that may plausibly confound the relationship between polarization
and quality. These include length, number of edits, and number of editors for each article,
and average editing experience for the editors (see Data and Methods for details).
Regression results are provided in Table A.3. As expected, number of edits, length of
article, and number of editors significantly predict article quality. The coefficient for the
—alignment— term suggests that quality decreases when editors are biased, on average, in
either direction. Most critical is that polarization, the variance of political alignments, is
positively and substantially associated with quality: a 1-unit increase in polarization multiplies the odds of moving from lower- to higher-quality categories by a factor of 18.57 for
Political articles, 2.06 for Social Issues articles and 1.90 for Science articles.
5

Social Issues

Wikipedia Page Type

Raising for Effective Giving [gambler/investor charity] .825 12/265
Index of Freedom in the World [Cato Institute] .534 11/326
Federbet [European casino lobby] .436 4/207
European Council of Religious Leaders .312 11/1648
Criminal rock throwing .296 10/1867

Article title [description] alignment editors/words
...

Legend

Science

Animal faith .924 14/699
Target Motion Analysis .960 7/300 th
Orphan virus .920 3/112
Thermokinetics .909 5/9
Countermine system .898 3/369

Social Issues

Antisemitism .070 3478/16364
Global warming .068 4656/8158
World War II .052 7486/14075
Racism .046 4866/14495
Capital punishment .044 3458/12884

Conservative

Joshua Heintzeman [Minn Stat Rep (R)] .707 3/129
Taking a Stand [author Rand Paul (R)] .671 4/104
Republicans for Immigration Reform .663 9/136
Giancarlo Ibarguen [libertarian businessman] .646 8/461
Farmers Independence Council of America .630 2/66

Science

Eugenics .058 2356/4515
List of Phobias ..048 2570/1847
Capitalism .040 4544/19266
Statistics .037 2224/6047
History .015 3120/6661

Conservative

Rush Limbaugh .146 3044/6624
Ann Coulter .123 3473/9357
Dick Cheney .111 3595/8957
Ronald Regan .080 5957/16325
Margaret Thatcher .068 3277/11813

Liberal

James Madison -.081 3169/10164
Leonardo DiCaprio -.069 3498/5063
Cher -.056 3456/12933
Barak Obama -.053 6566/13627
Al Gore -.052 3060/10214

Science

Liberal

Erosion -.036 2356/4009
Tropical rainforest -.032 2398/471
Ecosystem -.029 2500/5523
Planet -.026 2939/9362
Human evolution -.005 2920/9362

Science

Erosion -.026 2391/3977
World population -.017 3411/6317
Gang -.016 3707/3994
Poverty -.008 3509/10402
Genetically modified food -.005 3281/4492

List of the Presidents of the Popular Democratic Party [PDP] of Puerto Rico -.932 5/21
Ed Potillo [Washington DC 7th Ward “Democrat of the Year"] -.916 (66) 5
Statewide opinion polling of the March Dem. Party pres. primaries, 2008 -.701 13/22
Wendell Byrd [Michigan State Rep (D)] -.624 3/124
Wanda Soler Rosario [Mayor of Barceloneta, Puerto Rico (PDP)] -.611 4/229
Graphene boron nitride nanohybrid materials -.962 5/428
Botanical expedition -.812 2/121
Epistemic feedback -.745 2/318
Cognitive description -.677 11/46
Logical pluralism -.616 1/67

Social Issues

Social Issues

New York City Council LGBT Caucus -538 3/159
Chronic Poverty Research Centre -.506 15/165
Employment discrimination against persons with criminal records -.457 8/36
Mary Arlene Applehof [environmentatlist]-.298 13/367
Migrant sex work -.284 8/4183

Figure 2: Scatter plot of each article’s average editor alignment by number of editors. Average political
alignment converges to 0 as the number of editors increases, demonstrating the Linus Effect. Histograms on
x and y axes reveal the density of articles at each level of editorial attention and average political
alignment, respectively. Call-out boxes list five of the most “liberal” and “conservative” pages for articles
receiving the most and least editorial attention, featuring article title followed by an optional description,
mean political alignment, number of editors, and article length in bytes. These examples illustrate
meaningful association between right and left political preference of Wikipedia editors and the pages they
edit (e.g., “capitalism” and “history” vs. “planet” and “human evolution”.

6

Table 1: Odds ratios from ordinal logistic regression models
predicting article quality
Independent variable
polarization
| alignment |
editing experience
number of editors
article length
number of edits
N

Dependent variable: article quality
Politics Social issues Science
18.88 ***
0.30 ***
1.05 *
0.41 ***
33.55 ***
3.26 ***

2.06 ***
0.49 ***
1.06 ***
0.51 ***
47.83 ***
1.71 ***

1.79 **
0.65 **
1.01
0.56 ***
56.54 ***
1.69 ***

12,570

161,070

49,995

Note: *, **, *** denote statistical significance levels of 0.1, 0.01 and
0.001, respectively. The columns present odds ratios estimated on
Political, Social issues and Science articles, separately.

Mechanisms of Polarized Collaboration
To explore mechanisms by which politically polarized teams outperform homogeneous
teams, we examine Wikipedia ‘talk pages’. Each Wikipedia article has an associated talk page
where ‘backstage’ knowledge assemblage occurs. Here, editors debate proposed additions
and deletions, identify shortcomings, and attempt to persuade their fellow editors regarding
content for the public facing, ‘frontstage’, Wikipedia article [33]. Using text from these talk
pages, we examine relationships between political polarization and the following aspects of
debate: (1) debate intensity, (2) information diversity, and (3) use of Wikipedia institutions—
policies and guidelines—to discipline discussion. We investigate pairwise correlations between
polarization and these debate mechanisms, then we estimate regression models to test the
effect of polarization on these mechanisms separately, and finally, assemble them into a
structural equation model that allows us to identify their relative influence on article quality.
All statistical analyses yield consistent results regarding mechanisms of collaboration, as
discussed below and detailed in the Appendix.
Studies of team diversity and performance argue that information diversity is the key
feature distinguishing diverse from homogeneous teams. Nevertheless, this is almost never
measured directly, particularly in non-laboratory settings. Here, we decompose “information
diversity” into two distinct dimensions: lexical and semantic diversity. Semantic diversity
traces distinct meanings or issues discussed in a talk page, while lexical diversity captures
the number of ways in which editors discuss them. We expect that political polarization will
focus debate on a few contested, politically relevant topics, but frame them in multiple ways,
yielding lower semantic diversity and higher lexical diversity. We measure lexical diversity
of each talk page as a function of its distinct and distinguishing words. We measure the
semantic diversity of a page as a function of the dispersion of words on that page in a latent
semantic space defined by all Wikipedia articles, such that higher semantic diversity indicates
more Wikipedia topics were debated. (See Data and Methods for details on the two diversity
measures.) We find that high polarization narrows debate by reducing talk page semantic
diversity, but generates alternative framings traced by greater lexical diversity, as illustrated
7

5X

Bottom 1 3
Polarization

0.28

3.66

Lexical Diversity

3.47

0.34

Semantic Diversity

5.6%
decrease

23.4%
increase

Top 1 3
Polarization
Figure 3: Illustration of the shift in “talk page” debate activity between teams in the bottom and top
thirds of the political polarization distribution. Compared with the least polarized teams, the most
polarized teams semantically contract by 5.6% and lexically expand by 23.4%: they talk more about less,
focusing on core politically-contested subjects, but framing them in distinctive ways.

in Figure 3.
Diverse information should be more difficult to integrate, particularly if contested. We
measure two core aspects of debate intensity including volume and temperature. Following
previous research that found talk page length associated with article quality [34, 35], we
measure debate volume as a function of talk page length and distinct edits. Polarized teams
may attempt to integrate more diverse information, requiring more talk, which yields greater
article quality. Integrating diverse perspectives on contested and value-laden topics could
be acrimonious, but a balance of liberals and conservatives could lower the temperature of
potentially volatile collaborations, following research that links competitive imbalance to
emotional aggression and violence [36]. We measure debate temperature using the Detox
tool, developed by Wikimedia to identify harassment in the Wiki community. Detox detects
toxic comments using a sophisticated machine learning classifier [37], which we apply to all
talk page edits. We find that polarized teams generate a larger volume of debate and their
balance of political perspectives reduces flare-ups in debate temperature.
Finally, we explore the self-governance of contested knowledge through use of Wikipedia
policies and guidelines. Policies and guidelines are invoked so frequently that they have a
standard nomenclature 9 . For example, an editor who believes that part of an article is
biased may invoke “NPOV” (the “Neutral Point of View” policy) in the article’s talk page.
Wikipedia also relies on a collection of less binding guidelines that refer to desired qualities
of Wikipedia pages and the editorial process. These include that articles should cite sources
(“CITE”) and avoid and/or disclose any conflicts of interest (“COI”). We expect editors
within polarized teams to encounter differences not easily resolved and, when debate fails, to
discipline or challenge collaborators by invoking Wikipedia’s policies and guidelines. Indeed,
the numbers of policy and guideline mentions are found to increase with polarization. When
9

https://en.wikipedia.org/wiki/Wikipedia:Shortcut directory.

8

disaggregated, we find that “NPOV” (Neutral point of view) and “OR” or “NOR” (No
original research) are the most frequently cited policies, each significantly correlated with
polarization.
Correlations between all modeled variables are presented in Figure S2 and are consistent
with the regressions and structural equation model described below (also see Appendix). We
also note interesting associations between talk page measures, suggesting micro-mechanisms
of conflict and coordination, such as the negative correlation between debate temperature and
volume. This is relevant to the growing literature about online “trolling” behavior [38, 39],
suggesting that interactional toxicity is associated with foreshortened debate and a decreased
collective capacity to construct quality Wikipedia pages.
We present results from a structural equation model in Figure 4, which allowed us to
evaluate the combined impact of political polarization on article quality through mechanisms
of collaboration. (See Data and Methods and Appendix for additional details.) Compared
with politically homogeneous or skewed teams, polarized teams debate fewer topics with
more competing terminology and framings. They engage in more debate, which is less
acrimonious. And they more frequently appeal to Wikipedia policies and guidelines to govern
these interactions.
Mechanisms of polarized collaboration are echoed by editors in their survey responses.
One third of respondents indicated awareness of politically motivated conflicts, and two thirds
of those described them in detail. Conflicts typically entailed the encounter of biased content
(e.g. “The page read like anti-Russian propaganda”), or having one’s own content revised by
editors perceived as biased (e.g. “My neutral edits regarding a particular political group were
moved lower in the article to show negative opinions of this group first”). Many such conflicts
were resolved through debate. One respondent recalled a conflict over the meaning of the
word “refugee”, which was resolved “by legal arguments that would convince an impartial
observer.” Another related an intense conflict on a page related to homosexuality, but admitted that as a result “the article is in a better state.” Other conflicts were resolved through
administrator intervention. One respondent reported editing a page about a far-right politician that other editors would repeatedly vandalize; administrators intervened and protected
the page from further edits. Unbalanced political competition, however, where lone editors
sought to de-bias articles maintained by politically like-minded communities (e.g., with a
perceived “right wing slant” or “anti-Russian bias”) led to more acrimonious conflict that
often resulted in editor bans. Editing contested topics required toughness and endurance,
which was ameliorated by balanced conflict. It is precisely these engagements that are missing from segregated “echo chamber” platforms, and which channel Wikipedia editors’ diverse
perspectives into articles of superior quality.
Discussion
This study provides the first empirical, real-world evidence that political polarization
can lead to productive collaboration. Wikipedia teams comprised by a balance of politically
polarized individuals perform better than groups comprised of political partisans and even
moderates. Positive effects from polarization are observed in Political, Social Issues, and even
Science articles. The intensified effect of political polarization on pages with greater political
content suggests that diversity is not universally beneficial, but assists when directly or indi9

Talk Page Processes

Volume

0.4

# Article Edits

1.2

1.0

Article Length

# Words

# Article Editors

# Edits

Article Controls

Political Polarization

# Editors

1.2
-0.1
0.2
-0.1
0.1

Debate Intensity

-0.6

2.1

1.0

Temperature

1.5

Article Size

0.2
0.3

Lexical

-0.6

0.2

Information Diversity

-0.2

|Alignment|
-1.2

0.5

Semantic

2.1

-0.4

# Previous Edits
-.05

Wikipedia Institutions
0.2
.96

1.0

Quality

Guideline Mentions

Policy Mentions

Figure 4: Estimated structural equation model linking political polarization (top left) with article quality
(bottom right) through talk page debate intensity, information diversity and use of Wikipedia policies and
guidelines. The right panel includes control variables associated with features of the articles themselves.
Rectangles represent measured variables and ovals indicate latent variables. All coefficients are significant
at the p < .0001 level, agreeing with individual models and bivariate correlations. See Appendix for more
details about model and results.

10

rectly relevant to the topics considered. We demonstrate how frequent, intense disagreement
within politically polarized teams foments focused debate [40] and, as consequence, higher
quality edits that are more robust and comprehensive.
The observational nature of this study places constraints on interpreting the relationship
between political polarization and quality as a causal one. We observed only the behavior of
those editors who voluntarily cooperated with others of contrary politics to produce articles of
higher quality, or those who avoided such collaborations and produced lower quality articles.
It is possible that these are different kinds of people, and so we cannot rule out the possibility
that randomly assigned politically polarized teams may not outperform more homogeneous
teams. Concerns of extreme self-selection are, however, allayed by Wikipedia’s “encyclopedic
monopoly”. As the fifth most visited website in the world with more than 5 million articles
on a wide range of topics, Wikipedia represents an effective monopoly of reference attention.
Efforts have been made to produce politically skewed alternatives10 , but no viable substitutes
exist. More importantly, Wikipedia contains only a single version of an article for a given
topic. Consequently, if someone wishes to influence public knowledge on topics such as
“Climate change” or “Free market” through Wikipedia, they must collaborate with existing
editors who hold differing views but equal motivation. This is particularly salient for articles
on contested topics, and frames a dramatic contrast with segregated “echo chambers” in the
blogosphere. Previous research on Wikipedia also suggests that cross-party collaboration is
the norm rather than the exception [41].
Politically diverse collaborations are not without costs. One major obstacle to creating
well functioning, diverse teams is that such teams produce outputs that may appear worse to
the team members themselves [42]. Membership in homogeneous teams also feels better as
participation affirms prior beliefs [43] and shelters contributors from aggressive interaction.
Respondents to our survey echoed this sentiment by reporting pervasive displeasure in having
to convince obstinate, competing partisans of points that they took to be self-evident. Balanced competition softened the emotional edge of ideological conflict, however, by allowing
members to police tone and content with the omnipresent policies and norms of Wikipedia
[44]. Unlike many online settings, when norms and policies break down, powerful moderators
may step in and revert edits, lock pages and execute bans.
Previous research suggests that very high levels of diversity in teams may deteriorate
the quality of teamwork. To explore whether political diversity has an upper bound beyond
which polarization hampers performance, we re-estimated the regression models of quality
with a quadratic polarization term. Estimates suggest that quality may eventually decline
with increasing polarization, but the optimal level of polarization is above that realized by
95% of the teams in this study. For the 5% most polarized teams, there is no statistically
significant pattern between polarization and quality. In other words, we do not find evidence
that very high levels of political polarization hampers Wikipedia performance.
This study raises the possibility that in crowd-sourcing contested knowledge, the most
motivated contributors are those with a bias or “angle” on the disagreement at hand. Conducting debates on platforms like Wikipedia can require high levels of motivation and pa10

https://www.wired.com/story/welcome-to-the-wikipedia-of-the-alt-right/.

11

tience11 , and neutral users lacking partisan motivation may choose to allocate their time
elsewhere. It is plausible that for voluntary crowd-sourcing platforms there exists an optimal, non-zero amount of user bias. Platforms that discourage all user bias may thus be
inefficient or unsustainable.
Insofar as political diversity can improve the quality of politically relevant crowd-sourced
knowledge, it is important to consider whether platforms should intervene to promote or
even impose such diversity where missing12 . Our work suggests that for contested knowledge, platforms should seek not only high numbers of experts, but those with balanced,
diverse perspectives to construct an environment through which motivated conflicts can be
disciplined by enforceable policies and guidelines. Just as institutional designs to promote
gender diversity have proven valuable for fairness and performance in a variety of domains
[45, 46, 47], designing for political diversity may become an increasingly important priority.
References
[1] M. Gentzkow, J. Shapiro, M. Taddy, Measuring Polarization in High-Dimensional Data:
Method and Application to Congressional Speech, Technical Report, National Bureau
of Economic Research, Cambridge, MA, 2016.
[2] M. P. Fiorina, S. J. Abrams, Political polarization in the american public, Annual
Review of Political Science 11 (2008) 563–588.
[3] J. E. Campbell, Polarized: Making Sense of a Divided America, Princeton University
Press, 2016.
[4] D. DellaPosta, Y. Shi, M. Macy, Why do liberals drink lattes?, AJS 120 (2015) 1473–
1511.
[5] G. Gauchat, Politicization of science in the public sphere: A study of public trust in
the united states, 1974 to 2010, Am. Sociol. Rev. 77 (2012) 167–187.
[6] D. Sarewitz, How science makes environmental controversies worse, Environ. Sci. Policy
7 (2004) 385–403.
[7] X. Zhao, A. A. Leiserowitz, E. W. Maibach, C. Roser-Renouf, Attention to Science/Environment news positively predicts and attention to political news negatively
predicts global warming risk perceptions and policy support, J. Commun. 61 (2011)
713–731.
[8] F. Shi, Y. Shi, F. A. Dokshin, J. A. Evans, M. W. Macy, Millions of online book
co-purchases reveal partisan differences in the consumption of science, Nature Human
Behaviour 1 (2017) 0079.
11

For example, the top editor of Hillary Clinton’s Wikipedia page estimated spending 15 hours per week
on protecting it from vandals. https://newrepublic.com/article/63288/wiki-woman.
12
Indeed,
platforms
like
Facebook
are
moving
in
precisely
this
direction:
https://newsroom.fb.com/news/2017/10/news-feed-fyi-new-test-to-provide-context-about-articles/.

12

[9] Y. Benkler, The wealth of networks: How social production transforms markets and
freedom, Yale University Press, 2006.
[10] E. Bakshy, S. Messing, L. A. Adamic, Political science. exposure to ideologically diverse
news and opinion on facebook, Science 348 (2015) 1130–1132.
[11] E. Pariser, The Filter Bubble: How the New Personalized Web Is Changing What We
Read and How We Think, Penguin, 2011.
[12] M. Del Vicario, A. Bessi, F. Zollo, F. Petroni, A. Scala, G. Caldarelli, H. E. Stanley,
W. Quattrociocchi, The spreading of misinformation online, Proc. Natl. Acad. Sci. U.
S. A. 113 (2016) 554–559.
[13] C. Sunstein, Republic : divided democracy in the age of social media, Princeton University Press, Princeton, 2017.
[14] D. C. Mutz, Hearing the Other Side: Deliberative Versus Participatory Democracy,
Cambridge University Press, 2006.
[15] B. Bishop, The Big Sort: Why the Clustering of Like-minded America is Tearing Us
Apart, Houghton Mifflin Harcourt, 2009.
[16] C. S. Taber, M. Lodge, Motivated skepticism in the evaluation of political beliefs, Am.
J. Pol. Sci. 50 (2006) 755–769.
[17] J. M. Miller, K. L. Saunders, C. E. Farhart, Conspiracy endorsement as motivated
reasoning: The moderating roles of political knowledge and trust, American Journal of
Political Science 60 (2016) 824–844.
[18] D. M. Kahan, E. Peters, E. C. Dawson, P. Slovic, Motivated numeracy and enlightened
self-government, Behavioural Public Policy 1 (2017) 54–86.
[19] P. S. Hart, E. C. Nisbet, Boomerang effects in science communication: How motivated reasoning and identity cues amplify opinion polarization about climate mitigation
policies, Communic. Res. 39 (2012) 701–723.
[20] A. Joshi, H. Roh, The role of context in work team diversity research: A Meta-Analytic
review, Acad. Manage. J. 52 (2009) 599–627.
[21] S. E. Page, The Difference: How the Power of Diversity Creates Better Groups, Firms,
Schools, and Societies, Princeton University Press, 2008.
[22] E. Mannix, M. A. Neale, What differences make a difference? the promise and reality
of diverse teams in organizations, Psychol. Sci. Public Interest 6 (2005) 31–55.
[23] L. Hong, S. E. Page, Groups of diverse problem solvers can outperform groups of highability problem solvers, Proc. Natl. Acad. Sci. U. S. A. 101 (2004) 16385–16389.

13

[24] A. W. Woolley, C. F. Chabris, A. Pentland, N. Hashmi, T. W. Malone, Evidence for
a collective intelligence factor in the performance of human groups, Science 330 (2010)
686–688.
[25] M. Nielsen, Reinventing Discovery: The New Era of Networked Science, Reinventing
Discovery: The New Era of Networked Science, Princeton University Press, 2012.
[26] L. Fleming, S. Mingo, D. Chen, Collaborative brokerage, generative creativity, and
creative success, Adm. Sci. Q. 52 (2007) 443–475.
[27] S. Wuchty, B. F. Jones, B. Uzzi, The increasing dominance of teams in production of
knowledge, Science 316 (2007) 1036–1039.
[28] M. W. Nielsen, S. Alegria, L. Börjeson, H. Etzkowitz, H. J. Falk-Krzesinski, A. Joshi,
E. Leahey, L. Smith-Doerr, A. W. Woolley, L. Schiebinger, Opinion: Gender diversity
leads to better science, Proc. Natl. Acad. Sci. U. S. A. 114 (2017) 1740–1742.
[29] A. Halfaker, Interpolating quality dynamics in wikipedia and demonstrating the keilana
effect, in: Proceedings of the 13th International Symposium on Open Collaboration OpenSym ’17.
[30] S. T. Bell, A. J. Villado, M. A. Lukasik, L. Belau, A. L. Briggs, Getting specific about
demographic diversity variable and team performance relationships: A Meta-Analysis,
J. Manage. 37 (2010) 709–743.
[31] S. Greenstein, F. Zhu, Is wikipedia biased?, Am. Econ. Rev. 102 (2012) 343–348.
[32] S. Greenstein, F. Zhu, Open content, linus’ law, and neutral point of view, Information
Systems Research 27 (2016) 618–635.
[33] F. Viegas, M. Wattenberg, J. Kriss, F. Ham, Talk before you type: Coordination in
wikipedia, in: 2007 40th Annual Hawaii International Conference on System Sciences
(HICSS’07).
[34] D. M. Wilkinson, B. A. Huberman, Cooperation and quality in wikipedia, in: Proceedings of the 2007 international symposium on Wikis - WikiSym ’07.
[35] A. Kittur, R. E. Kraut, Harnessing the wisdom of crowds in wikipedia, in: Proceedings
of the ACM 2008 conference on Computer supported cooperative work - CSCW ’08.
[36] R. Collins, Violence: A micro-sociological theory, Greenwood Publishing Group, 2009.
[37] E. Wulczyn, N. Thain, L. Dixon, Ex machina: Personal attacks seen at scale, in:
Proceedings of the 26th International Conference on World Wide Web, International
World Wide Web Conferences Steering Committee, pp. 1391–1399.
[38] J. Cheng, C. Danescu-Niculescu-Mizil, J. Leskovec, How community feedback shapes
user behavior, CoRR abs/1405.1429 (2014).

14

[39] J. Cheng, C. Danescu-Niculescu-Mizil, J. Leskovec, Antisocial behavior in online discussion communities, CoRR abs/1504.00680 (2015).
[40] H. Mercier, The argumentative theory: Predictions and empirical evidence, Trends
Cogn. Sci. 20 (2016) 689–700.
[41] S. Greenstein, Y. Gu, F. Zhu, Ideological Segregation among Online Collaborators:
Evidence from Wikipedians, Technical Report, 2016.
[42] K. W. Phillips, K. A. Liljenquist, M. A. Neale, Is the pain worth the gain? the advantages
and liabilities of agreeing with socially distinct newcomers, Pers. Soc. Psychol. Bull. 35
(2009) 336–350.
[43] H. Hannah Nam, J. T. Jost, J. J. Van Bavel, “not for all the tea in china!” political
ideology and the avoidance of Dissonance-Arousing situations, PLoS One 8 (2013)
e59837.
[44] D. Jemielniak, Common knowledge?: An ethnography of Wikipedia, Stanford University
Press, 2014.
[45] I. Bohnet, What works: Gender equality by design, Harvard University Press, 2016.
[46] D. Dahlerup, The impact of gender quotas, Oxford University Press, 2012.
[47] T. Besley, O. Folke, T. Persson, J. Rickne, Gender quotas and the crisis of the mediocre
man: Theory and evidence from sweden, American Economic Review (????).
[48] M. Warncke-Wang, D. Cosley, J. Riedl, Tell me more, in: Proceedings of the 9th
International Symposium on Open Collaboration - WikiSym ’13.
[49] Y. Rosseel, lavaan: An r package for structural equation modeling, Journal of Statistical
Software, Articles 48 (2012) 1–36.

15

Appendix A. Descriptive statistics of the dataset
Summary statistics of the three corpora – politics, social issues, and science articles – are
shown in Table A.2. We measured the quality of Wikipedia articles algorithmically using
a prominent approach that draws on features derived from article content alone and not
information about editors or their collaboration patterns [48]. Wikipedia editors have scored
hundreds of articles on quality, but human-generated ratings for most of Wikipedia’s millions
of articles do not exist and necessitate an algorithmic approach. In particular, we used the
wikiclass algorithm, developed by Wikimedia research staff [29] and trained on Wikipedia
pages scored by active editors for quality using a six-class scale, which ranges from “Featured
Article” (highest quality) to “Stub” (lowest quality). The wikiclass algorithm predicts the
correct quality class in 62.9% of cases and is off by at most one quality class in 90.7% of cases
[29]. The distribution of estimated quality for each article is shown in Table A.3. Note that
a few articles have no text (e.g., removed or redirected) and hence receive no quality ratings.
Table A.2: Summary statistics of Wikipedia data sets
Corpus

# Articles

Article length

# Edits per article

# Editors per article

Politics
Conservative
Liberal
Social Issues
Science
All

10,909
10,038
162,085
49,995
233,027

9,449 (15,013)
8,645 (14,280)
13,153 (20,847)
11,193 (17,297)
-

177 (808)
155 (686)
265 (819)
210 ( 632)
-

80 (294)
75 (282)
122 (337)
103 (284)
-

Article length, # Edits per article, and # Editors per article refer to the averages over
all articles in the corresponding corpus. Article length is measured by bytes. Numbers in
parentheses are standard deviations.

Appendix B. Computational measure of political alignment
Many Wikipedia editors carry out general copy editing and curatorial tasks that contribute very few bytes to articles, which lead us to estimate an editor’s political alignment,
p, through a conservative, Bayesian framework. Our approach is designed to avoid data from
Table A.3: Distribution of article quality in each corpus
Corpus

Politics
Social Issues
Science

Quality rating
Stub

Start

C

B

Good Article

Featured Article

2950
30853
12192

5009
55884
16899

3541
48292
12454

485
14050
5323

871
10108
1696

215
3814
966

Number of articles in each quality rating for Politics, Science, and Social Issues
pages. The algorithm used to measure article quality is described in Material
and Methods: Measurements.

16

these numerous curatorial editors to introduce substantial uncertainty into our overall estimation of political preference. We use a “neutral” prior to down-weight small-sample effects.
Mathematically, p is assumed to have a prior distribution P (p) = Beta(a, b) before observing
any data, where everyone is assumed to randomly contribute to red or blue articles. Next, the
distribution is updated by Bayes’ law with observations X (bytes contributed to conservative
articles) and K (bytes contributed to political articles): p|X ∼ Beta(a + X, b + K − X). Finally, political alignment is defined as the posterior mean of p: E[p|X] = (X + a)/(K + a + b).
For presentational purposes, we rescale the alignment scores linearly onto [-1,1] with 0 as neutral point.
In short, political alignment is a scalar between -1 and 1. Casual editors with few contributions will be close to neutral (alignment=0). This alignment measure allows us to quantify
the ideological perspective each editor brings to an editing team and, in turn, an edited article. For example, an average alignment score close to 0 for a group of editors suggests
balanced participation from both conservatives and liberals in the group.
To statistically test whether the observed variance of political alignments is greater than
expected from chance, we simulate editors who have a given “budget” of edits and choose
to allocate them to liberal or conservative pages at random. In each simulation, each editor
contributes each of her actual edits to either liberal or conservative articles with a probability
proportional to the total size of each set of articles. From these simulations, we construct a
distribution of the variance of editor alignments and find that the variance of alignments from
the simulated editors is statistically lower than the variance observed among real Wikipedia
editors.
Appendix C. Survey measure of political alignment
We sampled Wikipedia editors having made recent edits (< 1 month) to at least 1 article
in political and/or science articles. Wikipedia required that surveys be individualized, solicitations be made personally on editors’ talk pages, not as a batch, and that we engage all
individuals solicited in conversation regarding any questions or concerns. This limited the
number of surveys that could be performed. The survey first asked whether the respondent
resides in the United States. Those responding in the affirmative were then asked “Do you
generally think of yourself as a Republican, Democrat, Independent or something else? ”. The
(mutually exclusive) answer choices were 1=Strong Democrat, 2=Not Strong Democrat, 3=Independent, Near Democrat, 4=Independent, 5=Independent, Near Republican, 6=Not Strong
Republican, 7=Other (Please explain). Although the computational measure ranges from
”Liberal” to ”Conservative,” the survey question focused instead on specific political party
affiliation for concreteness and its long-standing use in survey research. Some respondents
chose to instead write-in a political party and, in some cases, mentioned being registered as
either Republican or Democrat.
54% of respondents (64/118) reported living outside of the United States. These respondents were then asked ”Which political party, if any, do you generally identify with?” Some
respondents provided parties that they themselves compared with U.S. Democratic or Republican parties. Other responses could not be unambiguously aligned with Democratic or
Republican parties and were excluded from calculations.

17

Response rate (%)

Our overall response rate was 24% (118/500). Figure 4 displays response rates across
editors in the range [-1, +1] of (computationally measured) political alignment. Responses
were received from each quintile of the alignment distribution, although only 1 of 27 solicited
users with alignment in [0.2, 0.6) replied.
30
20
10
0

[-1, -0.6) [-0.6, -0.2) [-0.2, 0.2) [0.2, 0.6)
(n=2)
(n=9)
(n=49)
(n=1)

[0.6, 1]
(n=2)

Policital alignment range
(# responses)
Figure C.5: Response rate by (computationally measured) political alignment. Each bar is the response
rate achieved for editors whose alignments fall in the range specified at the bottom of the bar. Not shown
are editors who edited Science articles only, and therefore lack a computationally measured political
alignment. Note that not all responses provided useful political data and so not all are represented in Table
3.

Table C.4 reports three correlations between computational and survey measures of political alignments, where different sets of survey responses are used. In each case respondents
choosing “Independent” were not used in correlations below, because “Independent” was
assumed to reflect political alignments that do not clearly align on a Conservative-Liberal
spectrum.
Table C.4: Correlations between survey & computational measures
Editors’ location “Other party” re-coding
(a)
(b)
(c)

US-based
US-based
All

# Responses

Corr. coeff.

2-tailed t-test (1-tailed)

21
28
45

0.31
0.35
0.31

p=0.167 (0.083)
p=0.071 (0.036)
p=0.036 (0.018)

N
Y
Y

Note: Correlations between self-reported political identification from survey respondents and computationally
measured political alignments. Editors’ locations are self-reported. Row (a) uses raw survey responses (no
recoding). Row (b) adds 7 responses of Other (Please explain), recoded to either Independent, Near Democrat
or Independent, Near Republican. Row (c) adds 17 respondents from non-US locations whose responses could
be recoded straightforwardly as in (b).

Comparison (a) is strictest, using raw responses from US-based editors only. The pointestimate of the correlation, based on n=21 responses, is 0.31 (2-tailed t-test p=0.167, 1-tailed
t-test p=0.083). Comparison (b) adds to (a) responses from US-based editors that selected
“Other” for political party identification and provided comments that could be recoded to
the either “Near Republican” or “Near Democrat” unambiguously. Examples of the 7 recoded responses include “In between Libertarian and Republican”→Near Republican and
“Social Democrat”→Near Democrat. The estimated correlation is 0.35 (n=28, 2-tailed t-test
p=0.071, 1-tailed t-test p=0.036).
18

qu
ali
ty

ed
its

­0.05

0.17

0.13

0.08

0.16

0.19

0.17

0.16

lexical div.

0.15

1.00

­0.39

0.04

0.04

­0.15

0.28

0.16

0.08

0.28

0.22

0.21

0.38

semantic div.

­0.16

­0.39

1.00

­0.14

­0.14

0.11

­0.34

­0.12

­0.06

­0.21

­0.18

­0.16

­0.28

art
icle

0.11

art
icle

0.10

tal
k

­0.16

tal
k

0.15

tal
k

1.00

po
licy

art
icle

ed
ito
rs

len
gth

ed
its

ed
ito
rs

len
gth

gu
ide
lin
e
tem
pe
rat
ure

lex
ica
ld
iv.
se
ma
nti
cd
iv.

po
lar
iza
tio
n
polarization

policy

0.10

0.04

­0.14

1.00

0.68

­0.07

0.53

0.10

0.08

0.13

0.08

0.10

0.12

guideline

0.11

0.04

­0.14

0.68

1.00

­0.06

0.49

0.10

0.08

0.13

0.09

0.12

0.12

temperature

­0.05

­0.15

0.11

­0.07

­0.06

1.00

­0.08

­0.04

­0.02

­0.09

­0.06

­0.06

­0.13

talk length

0.17

0.28

­0.34

0.53

0.49

­0.08

1.00

0.31

0.20

0.45

0.40

0.39

0.36

talk editors

0.13

0.16

­0.12

0.10

0.10

­0.04

0.31

1.00

0.80

0.51

0.75

0.83

0.26

talk edits

0.08

0.08

­0.06

0.08

0.08

­0.02

0.20

0.80

1.00

0.37

0.47

0.62

0.16

article length

0.16

0.28

­0.21

0.13

0.13

­0.09

0.45

0.51

0.37

1.00

0.61

0.66

0.61

article editors

0.19

0.22

­0.18

0.08

0.09

­0.06

0.40

0.75

0.47

0.61

1.00

0.96

0.36

article edits

0.17

0.21

­0.16

0.10

0.12

­0.06

0.39

0.83

0.62

0.66

0.96

1.00

0.37

quality

0.16

0.38

­0.28

0.12

0.12

­0.13

0.36

0.26

0.16

0.61

0.36

0.37

1.00

1.0

0.8

0.6

0.4

0.2

0.0

0.2

Figure D.6: Pearson correlation between every pair of variables.

Comparison (c) adds to (b) respondents who identified their location as outside the US.
Many such respondents identified themselves with US-based political parties. We recoded
these parties to either “Independent, Near Republican” or “Independent, Near Democrat.”
Examples of recoded responses include “Labour (UK)”→Independent, Near Democrat and
“Left / progressive / social democracy”→Independent, Near Democrat. The correlation is
within the range of comparisons (a-b), but with the higher number of responses (n=47), it
is statistically significant at the 0.05 level (p=0.02).
All three comparisons show that our computational measure of political alignment correlates moderately well (0.31-0.35) with self-reported political identification, suggesting that it
is a noisy but valid measurement of editors’ political alignments. We focus on comparison (b)
because it includes more respondents than (a) but avoids the potentially subjective recoding
of non-U.S. parties to the U.S. political spectrum.
Appendix D. Statistical Analysis
Appendix D.1. Bivariate Correlation
We explore relationships between variables considered in the study by calculating the
Pearson correlation between every pair; the table of correlations is shown in Figure D.6.
From the table we can see that polarization (i.e., variance of political alignments) is
positively correlated with quality. Besides, polarization is correlated with all other variables
in directions consistent with hypothesized mechanisms of collaboration:
• positively with lexical diversity, and negatively with semantic diversity, suggesting that
polarization will focus debate on fewer contested, politically relevant topics, but frame
them in competing ways.

19

• positively with all talk page and article activities such as page length, number of edits,
and number of editors, suggesting polarization increases debate volume.
• negatively with talk page temperature, suggesting that polarization, resulted from balanced engagement, polices and decreases emotional aggression and violent debate.
• positively with policy and guideline mentions, suggesting increased use of Wikipedia
institutions among polarized teams.
The table also reveals that most variables are substantially and significantly correlated with
each other. Correlation between polarization and other variables could be caused by confounding factors. Therefore, we carried out two further statistical analyses that estimate
the conditional effects of polarization, holding other confounding variables constant. First,
we estimated a number of individual regressions, linking polarization to quality through all
proposed mechanisms. Then we estimated a structural equation model, which evaluates all
individual effects simultaneously, enabling us to compare their relative strength.
Appendix D.2. Regression Analysis
To assess the mechanisms of polarized collaboration, we estimated multiple linear regression models with polarization as the main predictor. Specifically, we tested how polarization
(i.e., variance of alignments) affected, respectively, talk page volume (i.e., number of talk
page edits, talk page length), semantic and lexical diversity, policy and guideline mentions,
and talk page “temperature”, controlling for several Wikipedia talk and article page features.
Models and regression results are shown in Table D.5.
All models control for number of talk page editors to make sure that the effects are not
simply caused by number of people involved. Talk and article page lengths are also accounted
for whenever possible, so the effects of polarization are not only due to the sheer amount of
edits and words. Lexical and semantic diversity are normalized by page length so it is not
necessary to include page length in those models; instead, we control for lexical and semantic
diversities of the articles to account for heterogeneous article content.
Note that we do not include every variable in every model because of substantial collinearity between some variables (see the correlation table above). Simpler models are more interpretable and preferable from a statistical point of view. For example, number of editors,
number of edits and page length are highly correlated with each other; when all are included
in a single model, it is hard to explain the direction of their effects (e.g., in the 2nd model in
Table D.5, number of editors shows a negative effect on page length when number of edits is
present). These encourages us to create factors from highly correlated and conceptually similar variables. We do this, and simultaneously evaluate the combined impact of polarization
on article quality through estimation of a structural equation model as described below.

20

Table D.5: Regression results from 7 models that predict qualities of Wikipedia talk page deliberation with polarization,
controlling for relevant talk and article page features.
Independent variable
polarization
# talk editors
# talk edits
talk page length
article length
article lexical d.
article semantic d.
R2

# talk edits

talk page length

0.10
1.03

1.28
-0.09
1.13

0.09
0.05

Dependent variable
lexical diversity semantic diversity
1.43
-0.09
1.39

-0.44
0.15
-0.21

0.24

temperature

policy

guideline

-0.17
0.25
-0.03
-0.21
-0.09

0.06
-0.28
0.29
0.05
-0.01

0.09
-0.25
0.26
0.05
-0.004

0.17

0.27

0.26

0.10
0.34
0.95

0.71

0.68

0.21

Note: All variable coefficients are statistically significant at the p < 0.001 level. Both dependent and independent variables are logtransformed so that distributions are made approximately Gaussian.

Appendix D.3. Structure Equation Modeling
The structural equation model we designed is detailed in Figure 4 of the main text, and
estimated by the R package “lavaan” [49]. Detailed specifications and estimation results are
as follows.
• Latent variables: debate volume, institution, article activity.
debate volume ∼ number of talk edits + 1.15 talk page length
institution ∼ policy mentions + 0.96 guideline mentions
article activity ∼ number of article editors + 2.1 article length + 1.48 number of article edits
• Regressions
quality ∼ −1.19 |average alignment| − 0.05 editing experience +
2.14 article activity + 0.33 debate volume +
0.50 lexical diversity − 0.35 semantic diversity +
0.18 institution − 0.23 debate temperature
debate volume ∼ 0.38 polarization + 1.19 number of talk editors
lexical diversity ∼ 0.20 polarization + 0.17 number of talk editors
semantic diversity ∼ −0.65 polarization − 0.1 number of talk editors
institution ∼ 0.20 polarization + 0.14 number of talk editors
debate temperature ∼ −0.80 polarization − 0.12 number of talk editors
• Effects of polarization on quality through the following paths:
polarization →
debate volume
polarization → lexical diversity
polarization → semantic diversity
polarization →
institution
polarization → talk temperature
21

→ quality : 0.125
→ quality : 0.098
→ quality : 0.230
→ quality : 0.035
→ quality : 0.136

• Combined effect of polarization on quality through all the paths: 0.624.
The model is well specified and the estimation procedure converged quickly (125 iterations). All estimated parameters in the model are significant at p < 0.001, agreeing with the
other statistical analyses.
Because the sample size is very large (205,749 observations), a χ2 test cannot be used to
evaluate this model. (In fact, the p-value of a χ2 is approximately 0.) The CFI and NNFI
indexes for the model are 0.78 and 0.71, respectively. We do not expect the indexes to be
very high because the model is designed to test the effects of polarization through various
mechanisms rather than fitting all covariances in the data. For example, the correlation table
reveals that article activity is highly correlated with debate volume. If we add a regression
of article activity on volume to the current model, the CFI index boosts to 0.89, but the
interpretation becomes less clear as a new path is introduced through article activity.

22
