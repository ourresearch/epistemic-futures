---
title: "How Do People Change Their Technology Use in Protest?: Understanding “Protest Users”"
person: brent-hecht
attendance: unconfirmed
section: by
type: journal-article
year: 2019
date: 2019-11-07
venue: "Proceedings of the ACM on Human-Computer Interaction"
authors: "Hanlin Li, Nicholas Vincent, Janice Tsai, Jofish Kaye, Brent Hecht"
source_url: https://doi.org/10.1145/3359189
fulltext_url: https://brenthecht.com/publications/cscw19_protestusers.pdf
openalex_id: W2983116658
doi: https://doi.org/10.1145/3359189
oa_status: bronze
cited_by_count: 22
retrieved: 2026-08-13
content: full-text
notes: "Full text from the author's self-archived PDF at https://brenthecht.com/publications/cscw19_protestusers.pdf (text extracted with pdftotext; PDF not stored); title expanded from the OpenAlex record's truncated form using the author's own publications page / Semantic Scholar"
---

# How Do People Change Their Technology Use in Protest?: Understanding “Protest Users”

## Full text

How Do People Change Their Technology Use in Protest?:
Understanding “Protest Users”
HANLIN LI*, Northwestern University, USA
NICHOLAS VINCENT*, Northwestern University, USA
JANICE TSAI, Mozilla, USA
JOFISH KAYE, Mozilla, USA
BRENT HECHT, Northwestern University, USA
* indicates equal contributions

Researchers and the media have become increasingly interested in protest users, or people who change
(protest use) or stop (protest non-use) their use of a company’s products because of the company’s values
and/or actions. Past work has extensively engaged with the phenomenon of technology non-use but has not
focused on non-use (nor changed use) in the context of protest. With recent research highlighting the
potential for protest users to exert leverage against technology companies, it is important for technology
stakeholders to understand the prevalence of protest users, their motivations, and the specific tactics they
currently use. In this paper, we report the results of two surveys (n = 463 and n = 398) of representative
samples of American web users that examine if, how, and why people have engaged in protest use and
protest non-use of the products of five major technology companies. We find that protest use and protest
non-use are relatively common, with 30% of respondents in 2019 reporting they were protesting at least one
major tech company. Furthermore, we identify that protest users’ most common motivations were (1)
concerns about business models that profit from user data and (2) privacy; and the most common tactics were
(1) stopping use and (2) leveraging ad blockers. We also identify common challenges and roadblocks faced by
active and potential protest users, which include (1) losing social connections and (2) the lack of alternative
products. Our results highlight the growing importance of protest users in the technology ecosystem and the
need for further social computing research into this phenomenon. We also provide concrete design
implications for existing and future technologies to support or account for protest use and protest non-use.
CCS Concepts: • Human-centered computing → Collaborative and social computing → Empirical
studies in collaborative and social computing
KEYWORDS: Protest users; technology non-use; online survey
ACM Reference format:
Hanlin Li, Nicholas Vincent, Janice Tsai, Jofish Kaye, and Brent Hecht. 2019. How Do People Change Their
Technology Use in Protest?: Understanding “Protest Users.” In Proceedings of the ACM on Human-Computer
Interaction, Vol. 3, No. CSCW, Article 87, November 2019. ACM, New York, NY, USA. 22 pages. DOI:
https://doi.org/10.1145/3359189

1 INTRODUCTION
Protests against technology companies that involve people stopping or changing their use of these
companies’ products have attracted increasing public attention. High profile examples include
boycotts against Facebook to protest illicit data harvesting and the spread of misinformation
[16,17], boycotts against Uber to protest its behavior surrounding a taxi strike and
Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided
that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on
the first page. Copyrights for components of this work owned by others than the author(s) must be honored. Abstracting with credit
is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a
fee. Request permissions from Permissions@acm.org.
2573-0142/2019/November – ART 87 $15.00. Copyright is held by the owner/author(s). Publication rights licensed to ACM.
https://doi.org/10.1145/3359189

Proceedings of the ACM on Human-Computer Interaction, No. CSCW, Article 87, Publication date: November 2019.

87

87:2

Hanlin Li et al.

sexual harassment in the company [52], and boycotts against Amazon to protest working
conditions and anti-tax lobbying [26].
Researchers have also become increasingly interested in these types of protests against
technology companies [32,40,45,57]. For instance, Vincent et al. recently explored the concepts of
“data strikes” and “data boycotts” against large-scale machine learning systems [57], Posner and
Weyl argued for the formation of “data unions” [45] or other mediators of individual data [31], and
Li et al. developed technologies to scaffold these and other types of protests [32]. More generally,
human-computer interaction (HCI) researchers [2,6,50,59] have called for studying specific forms
of non-use, of which recent protests against technology companies can be understood as a part.
However, despite the growing public and scholarly interest in protests against technology
companies, we lack critical empirical information about these protests. Core questions
surrounding participation rates, tactics, and motivations remain unaddressed. Put another way, we
do not know the extent of the population that is participating in one of these protests, nor do we
have a rigorous understanding of their specific protest tactics or motivations for protesting.
Additionally, we lack knowledge about what challenges people face in these protests and what
roadblocks prevent people from protesting.
Through the results of two nationally-representative surveys, this paper contributes an
improved descriptive understanding of whom we are calling protest users. These people are
current or past users of a technology who change (protest use) or stop (protest non-use) their use of
the technology due to the values or actions of the company behind the technology. Our surveys
sampled adult Internet users in the United States. The first exploratory survey was conducted in
2017 (n = 463). The second survey was conducted in 2019 and directly targeted specific research
questions about protest users (n = 398). In particular, we examined if, how, and why people have
become protest users of five major technology (tech) companies (Amazon, Apple, Facebook,
Google, Microsoft; the five most valuable tech companies on the U.S. markets), and the challenges
and roadblocks experienced by active and potential protest users, respectively.
Our results suggest that a surprisingly large share of web users in the United States are protest
users. 30% of our 2019 respondents reported being active protest users of at least one tech
company. This number is a meaningful increase from the 9% of respondents in our 2017 survey
(although as we detail below, this comparison must be interpreted with caution). Furthermore, an
additional 19% of our 2019 respondents who were not actively protesting expressed interest in
doing so. In total (after rounding to the nearest percent), 48% of respondents indicated that they
were either active or potential protest users.
Among active protest users, the most commonly reported motivations were concerns about
business models that profit from user data and concerns about privacy (echoing previous findings
about technology non-use and privacy concerns [5,56,60]). Furthermore, stopping use entirely and
using ad blockers were the most common tactics that our protest users reported employing
against tech companies, and losing social connections was the most prevailing challenge protest
users faced.
Among our potential protest users, we observed that a major roadblock to protesting was a
lack of alternative products. This finding is in alignment with current concerns around the
monopoly power of technology companies and corresponding effects on the consumer’s ability to
shape company behavior [48]. We also observed some roadblocks that were especially prominent
for particular companies. For instance, consistent with prior work [5], respondents reported that
the possibility of “losing connections with others” and “missing out on information” prevented
them from leaving Facebook.
Proceedings of the ACM on Human-Computer Interaction, No. CSCW, Article 87, Publication date: November 2019

How Do People Change Their Technology Use in Protest?: Understanding “Protest Users” 87:3
From the lens of the literature on protests against technology companies, our study provides
evidence that there could be substantial demand for technologies to support protest users and
provides guidance for the design of these technologies. This guidance includes helping people
protest collectively and aiding them in accessing alternative products and services. Our work also
replicates some findings from the non-use literature (e.g. the importance of privacy concerns and
demographic differences in non-use behavior) and identifies some characteristics of protest users
that are unique relative to other types of non-use (e.g. motivations and tactics, specific
demographic trends in protest non/use).
We begin below by covering work that inspired this research. We then discuss our survey
methodology and results, before entering into our discussion of implications.
2 RELATED WORK
In this section, we discuss the two literatures that most informed our overall thinking for this
research: the technology non-use literature and the literature on protests against technology
companies.
2.1 Technology Non-Use and “Non/Use”
Our ideation and study design for this project was influenced by the literature on non-use in
science and technology studies (STS) and human-computer interaction (HCI) (e.g.
[5,6,22,50,51,59]). This body of work argues that, in contrast to prevailing perspectives in HCI,
non-use can be a meaningful and productive behavior. As early as 2003, Wyatt explicitly urged
scholars to “take non-users and former users seriously as relevant social groups…who might
influence the shape of the world” [59]. Moreover, in 2009, Satchell and Dourish similarly called for
HCI researchers to consider non-users, and sought to dispel the notion that non-use is an
“absence” or “negative space” [50]. A key theme in this literature is the relationship of the
phenomenon of non-use to structural inequality across demographic groups [22,25,46,47,54], a
relationship we consider below.
The protest behaviors we study can be seen as a subset of the broader non-use phenomena
observed and theorized in prior work. In a recent publication, Baumer et al. specifically
emphasized the need to study different types of motivations for non-use [4]. This paper can be
understood as addressing this call, with our work focused specifically on non-use in protest of the
values or actions of a technology company.
One important recent contribution of the non-use literature has been to problematize the term
“user” and even “non-use”. Specifically, researchers have called for treating non-use as a
“continually negotiated practice” [3] which is not characterized by a binary distinction between
users and non-users [2,4,7]. In this view, the complex spectrum of use and non-use includes a
variety of behaviors, e.g. deactivating an account, considering deactivating an account, taking a
break from a platform, creating fake accounts, and many other behaviors [2,5]. Baumer and others
[2,3,6] have adopted the term "non/use" to encompass the spectrum of use and non-use behaviors,
with “non-use” reserved for behaviors very close to one end of the spectrum.
Our study reflects the complexity highlighted by Baumer and colleagues: we consider both
people who remain users of a technology but protest by altering their use behavior and people
who are protesting by ceasing their use entirely. As such, following Baumer et al.’s guidance, for
the remainder of the paper, we leverage the term “protest non/use” when referring to the spectrum
of behaviors exhibited by our respondents who are protesting a technology company. We use the
term “protest non-use” when specifically referring to people who reported entirely stopping use of
Proceedings of the ACM on Human-Computer Interaction, No. CSCW, Article 87, Publication date: November 2019

87:4

Hanlin Li et al.

a technology. As we have above, we leverage the term “protest user” to describe all users who
have engaged in protest non/use, as all people in this class are or were users of a technology.
2.1.1 Existing Empirical Information Relevant to Protest Non/Use

A large body of research on non-use and non/use investigated these behaviors’ association
with structural inequalities on a variety of platforms (e.g. [22,25,46,47,54]), and this line of work
informed our analysis and thinking of the relationships between demographic factors and protest
non/use. For instance, using a sample of U.S. households and focusing on Facebook, Baumer
showed that age, gender, and income are predictive of various types of Facebook non/use [2].
Below, in our Results section, we compare our demographic findings with those from Baumer and
reflect on the implications of our observed demographic trends in protest non/use.
Past research has also identified how individual and social factors relate to behaviors on the
non-use end of the non/use spectrum, providing helpful lenses for us to interpret our findings.
Guha et al. discussed how the lack of agency and control on Facebook plays a role in users leaving
Facebook [19]. Baumer et al. identified a number of individual and social factors that predict
reversion after leaving Facebook, including the concerns about impression management and
friends’ reactions [7]. Lampe et al. found social capital is a strong negative predictor of whether
somebody will join Facebook at all [30]. Although we did not collect or analyze these types of
individual or social factors, we interpret and discuss our findings in light of the context provided
by these studies.
Finally, studies on privacy-driven behaviors have identified several forms of non/use that can
be seen as protest non/use, directly influencing our construction and understanding of protest
non/use. As privacy concerns are a prevalent motivation for non/use [5,30,56], prior work has
shown technology users adopt a variety of obfuscating strategies in protest, e.g. providing fake
personal information [21,49]. Additionally, Mathur and colleagues’ work on browser-based
blocking extensions revealed some people’s overwhelming discomfort with online tracking as well
as their corresponding blocking strategies (e.g. using anti-tracking and ad-blocking extensions)
[39]. Our study bolsters these findings and we discuss the implications of protest users for privacy
research and vice versa.
2.2 Protests against Technology Companies
2.2.1 Consumer Boycotts and Technology Companies

Many recent protests against technology companies, such as Amazon, Uber, and Facebook
[16,17,26,52], are similar to traditional consumer boycotts: a group of people withholds
engagement with a company to attempt to force the company to change some practices. As such,
the large body of research on consumer boycotts (e.g. [27,28,41]) can provide important context
for our work.
There has been some research on participation rates and outcomes of consumer boycotts.
Based on a survey of the American consumers, more than 28% of participants have engaged in
“political consumption”, which means either boycotting or “buycotting” (i.e. deliberately
purchasing products to support a company) [43]. The number is even higher among some
European countries, such as Sweden and Switzerland, where about 35% of people have engaged in
boycotts and around 58% in “buycotts” [29]. Importantly, evidence from historical boycotts
suggests that they are not only prevalent but have had economic and societal impact (see for
instance [34,61,62]), setting a precedent for potentially impactful boycotts against technology
companies and raising the stakes for the study of protest users. For example, the boycott against
Proceedings of the ACM on Human-Computer Interaction, No. CSCW, Article 87, Publication date: November 2019

How Do People Change Their Technology Use in Protest?: Understanding “Protest Users” 87:5
Uber in 2017 attracted widespread participation and subsequently, the company made a public
apology corresponding to the boycott [52].
Protesting behaviors in the technology domain can take on various forms corresponding to the
different ways tech companies generate revenue. For instance, advertisements are a primary
source of profit for some major tech companies (e.g. Google and Facebook) [35], whereas
companies in other sectors sell products and services directly to consumers. Thus, protesting
behaviors in the tech domain include avoiding visiting the website of an ad-driven tech company
(e.g. boycotts against Facebook), refusing to purchase goods or services from a company (e.g.
boycotts against Uber and Amazon), or disrupting an ad-revenue generating platform (e.g. the
2015 Reddit blackout by sub-Reddit moderators [40]). In addition to these protesting behaviors that
attempt to reduce a company’s ad revenue, a “data strike”, i.e. a group of users withholding their
“data labor”, can also negatively impact many profitable intelligent technologies. We unpack this
form of protest in detail in the immediately following section.
Our research is also motivated by recent interest in “boycott-assisting technologies” [32] such
as Buycott [63] and Out of Site [32] that aim to facilitate consumer boycotts offline and online,
respectively. In particular, these technologies emphasize the collective nature of boycotts and
inform boycott participants of recommended actions and their collective outcome. As we discuss
below, our study provides concrete design implications for designers of boycott-assisting
technologies to specifically support people protesting tech companies.
2.2.2 Data Labor

Recent work [44,45,57] has identified that protests like those we consider here may be
especially powerful compared to protests against non-tech companies [57], making understanding
the prevalence and motivations of protest users all the more important. This research highlighted
how, due to the reliance of most tech companies on intelligent technologies, users of these
companies’ products generally have two roles, each with its own source of power: users are
consumers of services with “consumer power” [57] and users are also data-generating “laborers”
[45] with “data labor power” [57]. The latter role emerges from the critical dependence on usergenerated data of many tech companies’ intelligent technology-driven core services (e.g.
recommender systems, search engines).
Protest users exercise their consumer power when they stop or change their use of a
technology and thereby reduce their contributions to sales and advertising revenue. Protest users
exercise their data labor power when their stopped or changed use of a technology results in
fewer products being rated, fewer pages being liked, and/or less implicit feedback being collected,
thus damaging profitable recommender systems, search engines, and related intelligent
technologies. These two roles and their corresponding sources of power make protest users
particularly influential relative to traditional protests against non-tech companies, in which
participants largely only have consumer power.
3 METHODS
This paper reports findings from two web-based surveys conducted in 2017 and 2019. The first
survey was designed to broadly explore the prevalence of and the reasons for protest non/use
(protest use and protest non-use). Our second survey focused on five prominent technology
companies and elicited in-depth responses about motivations, tactics, challenges, and roadblocks
associated with protest non/use. Both surveys used nationally representative sampling by a third
party, as is common in large-scale studies that have examined non-use and non/use (e.g. [2,5,19]).
Below, we present details about our survey design, recruitment methods, and respondents.
Proceedings of the ACM on Human-Computer Interaction, No. CSCW, Article 87, Publication date: November 2019

87:6

Hanlin Li et al.

3.1 Survey Design and Recruitment
Two authors designed the first survey in October 2017, and it was intended to be exploratory
in nature. It was funded by a large non-profit organization at which these two authors are
employed. Respondent recruiting was completed by the professional survey company
SurveyMonkey, which used its proprietary approach to generate a nationally representative
sample of Internet users who live in the United States and were at least 18 years old. The survey
was completed by 463 people and contained both fixed-response and free-response questions. The
fixed-responses questions were generally targeted at understanding the prevalence and
motivations of protest users, and the free-response questions were open-ended. Some of the
demographic information about respondents in this survey came from SurveyMonkey, and the
survey asked directly about respondents’ political views.
The results from the first survey indicated that a non-trivial portion of the public was engaged
in protest non/use against tech companies (as reported below, 9% of respondents reported
themselves as protest users of at least one prominent tech company). These results – along with
increasing media coverage and public interest in protesting tech companies – motivated us to
launch a second, in-depth, and more focused survey in 2019. All authors were involved in the
design of the second survey. Building off the basic structure of the first survey, the second survey
sought to acquire more detailed and structured information about protest non/use, as well as to
update the top-line numbers to assess whether the ranks of protest users were growing. More
specifically, our second survey was designed around two structured research questions:
RQ1 – Basic Descriptive Information: (a) What is the prevalence of protest non/use? (b)
What are the motivations behind protest non/use? (c) What tactics are employed?
RQ2 – Challenges and Roadblocks: What challenges do protest users face and what
roadblocks prevent people from becoming protest users?
Our 2017 and 2019 surveys have important differences, both in terms of the questions we
asked and how the questions were specifically framed.
We made a number of additions to the 2019 survey to obtain data more explicitly targeted at
our research questions. In order to gather data to directly answer RQ1(c) and RQ2, we added
questions about protest tactics, challenges protest users faced, and roadblocks faced by potential
protest users. The answer choices for questions regarding challenges and roadblocks were drawn
from the free-response answers provided by respondents to the first survey, as well as themes in
the non/use literature and in media coverage of protests. Additionally, whereas the 2017 survey
focused on multiple-choice questions with single answers, the 2019 survey was primarily based
around multiple-choice multiple-answer (i.e. select-all-that-apply) questions with an option to
provide free-text input to explain or expand upon one’s answer. The 2019 survey also integrated
answer choices that were not included in our first survey but were reported by 2017 respondents
in the free-response questions (e.g. “the company profits from my data” and “I have concerns
about the company’s bias against gender, race, or other demographics” as motivations for protest
non/use). Additionally, the 2019 survey included a Likert-type question about how difficult it is to
protest a given company (on a scale from 1 to 5) after a respondent reported being a protest user
of the company.
In terms of how we framed the survey questions, although both surveys used the term
“boycott” as a shorthand for “protest use and protest non-use” as we hypothesized this term would
Proceedings of the ACM on Human-Computer Interaction, No. CSCW, Article 87, Publication date: November 2019

How Do People Change Their Technology Use in Protest?: Understanding “Protest Users” 87:7
be much easier to understand for respondents, we altered the exact definition of “boycott”
provided in the 2017 survey for the 2019 survey. In the 2017 survey, boycotting was defined for
respondents as “deciding to stop using, or use much less of, a technology or company as a protest
or statement, or because you disagree with the company's values.” In 2019, we updated this
definition to be “stopping or changing your use of a company’s products or services, because you
disapprove of the company’s values or actions.” This updated definition was meant to capture the
many forms protest non/use can take against tech companies (as discussed in Related Work).
As mentioned above, the 2019 survey asked additional questions about specific tactics
compared with the 2017 survey, and some of these answer choices about tactics can be employed
for non-protest reasons (e.g. private browsing and ad blockers might be used for reasons unrelated
to protesting a company’s values or actions). As such, we took care in survey design to avoid
confounds surrounding the reasons for the use of a potential protest tactics. Respondents were
first asked if they were protest users of a given company, and then they were asked which tactics
they used in their protest. While this avoided confounds in our top-line numbers about
participation rates, we did still see some confusion when respondents were enumerating the
tactics that they used to implement a specific protest, and we discuss this more below. A full copy
of both surveys is available online 1.
2019 survey was conducted through Qualtrics (following prior research on non-use, see [8]),
which also uses proprietary methods to perform nationally representative sampling (we detail the
demographics of our respondents in Table 1). The survey was deployed in early 2019 by a subset
of the authors who are employed at an academic institution, in accordance with their institution’s
IRB. This survey had 429 responses in total. However, we found that some responses appeared to
be low-quality (e.g. free response fields filled with random characters). The first two authors
examined all the responses independently to identify low-quality responses and then compared
and discussed their findings to build a merged set of low-quality responses. In total, 31 responses
were flagged as low-quality and were removed from all analyses, leaving us with 398 valid
responses.
Given that we modified the survey design and used two different companies for proprietary
sampling, we must interpret any observed trend in the two survey results with some caution.
However, considering that some differences between the two nationally representative samples’
results are very large (e.g. the increases in our top-line participation rates), they very likely
represented movements in the underlying phenomenon.
3.2 Respondent Demographics
Table 1 shows the demographic data we obtained from our surveys. In the 2019 survey, all
demographic questions were optional, but 90% of the 2019 respondents answered all the
demographic questions. Comparing Table 1’s “All respondents” column with U.S. Census Bureau
data [10], we find that our samples were reasonably balanced across a number of demographic
factors, with a slight over-representation of the low- to middle-income population. The 2017
sample also has a relatively large share of respondents who are at least 60 years-old compared
with the U.S. Census Bureau’s population estimates (with 28% of the U.S. adult population being at
least 60 years old) [11]. On the other hand, the 2019 survey has a relatively small share of this
population.

1 psagroup.org/protest_nonuse_survey.pdf

Proceedings of the ACM on Human-Computer Interaction, No. CSCW, Article 87, Publication date: November 2019

87:8

Hanlin Li et al.

Table 1. Self-reported demographic information of respondents, broken down by the percentage of total
respondents (“All respondents” column) and the percentage of respondents who were protest users for
at least one company (“At least one company” column)
2017 Survey

2019 Survey

All respondents

At least one company

All respondents

At least one company

18 - 29 years old

20%

19%

26%

32%

30 - 44 years old

21%

22%

41%

42%

45 - 59 years old

25%

27%

23%

20%

60+ years old

35%

32%

10%

5%

Female

55%

45%

48%

35%

Male

45%

54%

51%

63%

Non-binary

-

-

0.5%

2%

Agender

-

-

0.3%

0%

Transgender

-

-

0.3%

0%

Age

Gender

Political stance
Democrat

36%

30%

38%

43%

Republican

21%

14%

24%

22%

Independent

33%

38%

31%

31%

Other

10%

19%

6%

3%

Income
< 25,000

18%

9%

23%

18%

25,000−49,999

25%

19%

33%

33%

50,000−74,999

19%

31%

20%

24%

75,000−99,999

12%

9%

10%

13%

100,000−124,999

13%

22%

7%

7%

125,000−149,999

5%

3%

4%

4%

150,000+

8%

6%

2%

1%

Below, we constructed logistic linear regression models to further examine the relationships
between protest non/use and demographics. Age and income were represented as ordinal
variables using the levels shown in Table 1. Political stance and gender were represented as
categorical variables.
3.3 Margin of Error and Confidence Intervals for Percentages and Instances
Using margin of error calculations for a random sample, each survey had a large enough
sample to achieve a margin of error of 5% at a confidence level of 95% for our target population
(web users in the United States who are at least 18 years old). Many of our results are simple
percentages of respondents, such as the percent of users protesting a given company. For these
percentages, following recent suggestions for reporting results in HCI research [12], we compute
non-parametric 95% confidence intervals (CI) using empirical bootstrap resampling (a popular
approach for generating CIs for survey results [53]). Specifically, we used software from Beecher
et al. [9] and used 10,000 resampling iterations for each CI.
Not all of our results are reported as percentages. For results relating to motivations, tactics,
challenges, and roadblocks, our survey provided the numbers of instances of each motivation,
Proceedings of the ACM on Human-Computer Interaction, No. CSCW, Article 87, Publication date: November 2019

How Do People Change Their Technology Use in Protest?: Understanding “Protest Users” 87:9
tactic, challenge, and roadblock. An instance refers to one respondent reporting one motivation (or
tactic, challenge, or roadblock) for one company. Thus, one respondent can have multiple
instances spread across multiple companies. For example, one person might protest Facebook
because of privacy concerns and the company’s political stance, which would correspond to two
difference instances of motivations (privacy and political). In our results, we report both the
number of instances for each company, and instances summed across companies. These summed
instances do not represent estimates about the national population, but instead represent how
frequently a motivation, tactic, challenge, or roadblock was reported by our respondents, allowing
for a single individual to contribute many instances. For these results, instead of reporting
percentages with confidence intervals, we report only the total count of instances and interpret
our results accordingly.
4 RESULTS
Below we unpack the results from the surveys. As our 2019 survey was targeted specifically at
our research questions, we focus primarily on our 2019 results below and provide the 2017 results
for context. We first give an overview of the percentages of people who reported being protest
users, and then detail the percentages of protest users for each company. We further unpack the
motivations, tactics, challenges, and roadblocks associated with protest non/use.
4.1 RQ1a: Prevalence of Protest Users
The highest-level result from our 2019 survey is that a substantial share of respondents – 30%
(CI: 25 – 34%) – reported being protest users. The majority of the protest users (21%) were
protesting one company only, followed by 5% reporting two companies. Very few protest users
were protesting more than two companies. 33% (CI: 28-37%) of respondents expressed interest in
becoming protest users of at least one tech company against which they were not currently
engaging in protest non/use, approximately half of whom (19% of respondents; CI: 15-22%) were
not currently protest users of any company. In total, 48% of respondents (CI: 44-54%) were either
actively engaging in protest non/use (30%) or were only interested in doing so (19%), after
rounding to the nearest percent. Notably, the prevalence of active protest users we observed (30%)
is very close to estimates of the prevalence of political consumption (i.e. boycotts and buycotts) in
the United States in 2011 and 2012 (28%) [29,43].

Figure 1. Protest non/use against five major tech companies from our 2019 survey. The x-axis indicates the
fraction of respondents who engaged in protest non-use, protest use, or were interested in becoming
Proceedings of the ACM on Human-Computer Interaction, No. CSCW, Article 87, Publication date: November 2019

87:10

Hanlin Li et al.
protest users.

Figure 1 unpacks our results about the prevalence of protest non/use on a company-bycompany basis. Facebook stands out as a particularly common target of protest users and potential
protest users: nearly one-third of respondents reported that they were currently a protest user of
Facebook or were interested in becoming one. In Baumer’s 2018 study, 17.6% of respondents
stopped using Facebook (through account deactivation) and 22.4% considered doing so, meaning
40% of respondents were, or considered, stopping Facebook use. Our observed number of active
and potential Facebook protest users is thus slightly lower than Baumer’s 2018 result. Note that in
Baumer’s study, the number of active and potential Facebook non-users included those who might
not be protesting Facebook. Such respondents in our study would not identify themselves as
protest users, potentially explaining our lower percentage.
Also of note in Figure 1 is that Amazon, Google, and Microsoft have more potential protest
users than actual protest users, suggesting a lower protest “conversion rate” for these companies.
Below, we present the specific roadblocks reported by potential protest users of these companies.
These roadblocks may play a role in influencing the conversation rate of potential protest users to
active protest users.
Table 2. The percent of protest users against five major tech companies in 2017 and 2019.
YEAR

FACEBOOK

APPLE

MICROSOFT

GOOGLE

AMAZON

2017

5%

3%

2%

2%

2%

TOTAL
9%

2019

18%

12%

6%

5%

6%

30%

Table 2 puts our top-line results from the 2019 survey in context with those from 2017.
Whereas 30% (CI: 25-34%) of respondents in 2019 reported being protest users of at least one
company, the equivalent number in 2017 was only 9% (CI: 6–11%). In particular, we see significant
increases in protest rates of Facebook and Apple. The percentage of respondents protesting
Facebook more than tripled in 2019 from 5% to 18%, and the percentage for Apple in 2019 is four
times that of 2017, going from 3% to 12%. The remaining three companies, Microsoft, Amazon, and
Google also see an increased rate of protest users, with the percentages roughly doubling. Overall,
we see rising protest rates across all five companies, but Facebook and Apple see the largest
increases.
Recall that these comparisons need to be interpreted with caution: the two surveys were not
identical in design or sampling (see Methods). Furthermore, differences in protest prevalence rate
will be affected by changes in company user bases (e.g. people who didn’t use Facebook at all in
2017 may have joined Facebook and engaged in protest use in 2019). Nonetheless, the size of the
delta we observed suggests that the prevalence of protest non/use has increased in the last two
years.
4.1.1 Who Are Protest Users?

According to our 2019 data, certain groups are more likely to protest: it appears that
respondents who identified as male protested more than other gender identities, and younger
respondents protested more than older respondents. A logistic regression that uses self-reported
demographics as the independent variables and protest non/use for at least one company as the
dependent variable suggests that both of these are statistically significant associations (p < 0.05,
see Table 3).

Proceedings of the ACM on Human-Computer Interaction, No. CSCW, Article 87, Publication date: November 2019

How Do People Change Their Technology Use in Protest?: Understanding “Protest Users” 87:11
Table 3. Who are protest users overall?
Coefficients and odds ratios for a logistic regression with self-reported demographic information as
independent variables and engagement in protest non/use of any company as the dependent variable.
The pseudo R-squared of the model is 0.06.
Coef.

Std. err

p

Odds Ratio

0.351

0.499

0.789

Intercept

-0.237

Political stance - Independent

-0.115

0.283

0.683

0.891

Political stance - Other

-2.017

1.059

0.057

0.133

Political stance - Republican

-0.066

0.318

0.836

0.936

age

-0.459

0.141

0.001 *

0.632

income

-0.035

0.076

0.649

0.966

gender - male

0.892

0.258

0.001 *

2.439

* indicates p-value less than 0.05.

Table 4. Who are Facebook protest users?
Analogous to Table 3, but with protest non/use of Facebook specifically as the dependent variable. The
pseudo R-squared of the model is 0.07.
Coef.
Intercept

-0.786

Political stance - Independent

-0.752

Std. err

p

Odds Ratio

0.412

0.056

0.455

0.349

0.031 *

0.472

1

0.000

Political stance - Other

-27.891

476144.631

Political stance - Republican

-0.360

0.370

0.330

0.698

age

-0.390

0.168

0.020 *

0.677

income

-0.059

0.091

0.516

0.943

gender - male

0.901

0.311

0.004 *

2.462

In particular, male respondents were 2.4 times more likely than female respondents to protest
when holding other factors constant, which is consistent with the descriptive statistics in Table 1.
With one increment of the age groups in Table 1, older respondents were only 0.632 as likely as
younger respondents to protest.
With respect to Facebook specifically, analogous to Baumer’s finding that younger
respondents are more likely to deactivate their Facebook account [2], our model (Table 4) shows
that younger respondents are more likely to be protest users of Facebook than older respondents.
However, in contrast with the insignificant relationship between gender and Facebook
deactivation that Baumer observed, men in our study were 2.4 times more likely than women to
protest Facebook (very slightly more than our result for overall protest users). This difference may
be due to the divergence in the definitions of protest users and non-users as mentioned above. In
other words, although men and women are equally likely to be Facebook non-users, men may be
more likely to do so as an action of protest than women. Also of note is that compared with
Democratic respondents (the default intercept in Table 4), Independent respondents were less
likely to protest Facebook (odds ratio=0.472), a relationship that we do not observe in the model
considering all companies.
4.2 RQ1b: Motivations for Protest Non/Use
Our 2019 data provides us with rich information about motivations for protest non/use, with
active and potential protest users selecting two motivations per company on average (respondents
Proceedings of the ACM on Human-Computer Interaction, No. CSCW, Article 87, Publication date: November 2019

87:12

Hanlin Li et al.

could select all motivations that applied). We focus here on reporting the number of instances of
each motivation, where an instance is a single motivation for protesting a single company
(selected by a single respondent).

Figure 2. Instances of protest non/use motivations reported by our respondents who were protest users
(“Protest Users”, left) or interested in protest non/use (“Potential Protest Users”, right). Each respondent
could select multiple motivations. Includes the total number of (potential) protest users per company in
grey for context.

Figure 2 shows our motivation findings in detail. The left side of Figure 2 shows our
motivation-related results for active protest users. The right side shows the equivalent findings for
potential protest users, i.e. people who expressed interest in becoming protest users of a given
company but were not doing so currently. Examining the left side of the figure, we see that the
most-common motivations for actively protesting were concerns around companies profiting off
of user data (59 instances) and privacy (57 instances). In other words, respondents indicated 59
times that they were motivated to actively protest a tech company because it was profiting off of
user data and did the same for privacy 57 times. The next two most common motivations were
cost (43 instances) and company size (41 instances).
The most prominent motivation for protesting, concern about companies profiting off of user
data, does not align with prior work which has suggested that college students cared little about
how their data is used by platforms [60] and placed very small monetary value on protecting data
[18]. One reason for this difference may be the increasing awareness of data-driven business
models in the past few years. The qualitative data from the 2017 survey was an early signal that
profiting off of user data might be a prominent motivation. Some respondents from 2017 took
strong stances on the topic, saying “I resent the invasive tentacles of tech companies. They are
trying to control and profit from everything we do in life. They don't respect privacy they just
want $$” and “they sell my personal information exploiting ME MAKING PROFIT OFF OF ME,
without giving me any financial share of their profit pirating.” Our quantitative data from 2019
suggests that these sentiments are spreading more broadly.
The prevalence of privacy concerns visible in Figure 2 resonates with HCI studies of privacy
and surveillance (e.g. [49,60]). In particular, Baumer et al. found in 2013 that the top motivation for
Proceedings of the ACM on Human-Computer Interaction, No. CSCW, Article 87, Publication date: November 2019

How Do People Change Their Technology Use in Protest?: Understanding “Protest Users” 87:13
leaving Facebook or limiting Facebook use was privacy. Our results suggest that, six years later,
these concerns remain serious for people who engage in various types of protest non/use of
Facebook (including leaving Facebook). Indeed, examining Figure 2, we see that of the 73 users
who reported being active protest users of Facebook, 37 (51%) indicated that they were doing so
for privacy reasons. We see a similar trend on the right side of Figure 2, where privacy was the
number one motivation for being interested in becoming a protest user of Facebook (60% of
potential Facebook protest users).
The reported motivations in the two surveys have some other differences, although we did not
provide identical options and therefore direct comparisons must be interpreted with substantial
caution. For the options that overlap between two surveys, privacy concerns remained the top
motivation in aggregate. However, the second-most-popular overall option in 2017, disagreeing
with the company’s political stance, substantially diminished in prominence in our 2019 data.
Furthermore, looking at these trends per company, we observe a large increase in people
protesting Amazon because of working conditions, perhaps relating to the media’s coverage of the
issue (e.g. [26,64,65]).
4.3 RQ1c: The Tactics of Protest Users
Our 2019 survey elicited information on the specific tactics leveraged by protest users in their
protest non/use. Overall, non-use was the most-common reported tactic. 93 instances of non-use
were reported in total, where an instance in this case means that a single respondent reported
entirely halting the use of a single company’s products. Respondents also reported 129 specific
instances of protest use overall, i.e. still using a technology but with protest tactics, including ad
blocking, private browsing, using fake accounts or fake data, using anti-tracking extensions, and
using products while logged out. Among these protest use instances, we observed that using ad
blocking (41 instances) was the most common tactic. The prevalence of ad blocking is not
surprising given a recent survey on Amazon Mechanical Turk (MTurk) showed over half of
participants use ad blockers [39]. Also consistent with the MTurk survey, the use of anti-tracking
extensions was less prevalent than ad blocking in our study, with 18 instances of anti-tracking
reported.
Following using ad blockers, providing fake accounts or data (27 instances) and using private
browsing features (24 instances) were the second- and third-most prevalent tactics among our
respondents. These tactics largely overlap with privacy-driven obfuscation approaches that have
been reported in privacy and surveillance research. For instance, Sannon et al. found that 21.9% of
their recruited respondents lie to computing systems to protect their privacy [49]. Our results
suggest that protest users were re-appropriating these privacy-protection strategies as a means of
protesting, indicating an overlap in tactics among protest use and privacy protection. This overlap
may have important implications that we unpack in Discussion.
Focusing on tactics related to protest non/use of Facebook specifically, similar to prior work
showing the non-binary nature of Facebook non/use [5], our survey responses imply that
protesting Facebook involves nuanced behaviors that are not limited to simply deleting or
deactivating one’s Facebook account. Among the 37 respondents who were using Facebook but
engaging in protest use, using ad blockers (16 instances) was the most common tactic, followed by
using anti-tracking extensions (11 instances) and private browsing (9 instances).
In our survey, 53 respondents who reported protest non-use (“stopping entirely”) of a specific
technology also selected additional protest tactics against the company, e.g. using ad blockers and
private browsing. This may indicate very nuanced tactical strategy (e.g. people who stop using
Facebook and also use private browsing or anti-tracking to attempt to avoid Facebook tracking on
Proceedings of the ACM on Human-Computer Interaction, No. CSCW, Article 87, Publication date: November 2019

87:14

Hanlin Li et al.

other websites) but might also indicate confusion on behalf of a respondent (e.g. perhaps people
who used an ad blocker for reasons unrelated to protest of a specific company were confused by
this question). As our data did not fully explain this behavior, our reported results include only the
protest use tactics used by people who indicated that they continued to use a technology.

Figure 3. Challenges active protest users reported (left) and roadblocks that potential protest users
reported (right). Includes the total number of (potential) protest users per company in grey for context.

4.4 RQ2: Challenges and Roadblocks
Figure 3 presents the challenges reported by active protest users of each company on the left
and the roadblocks reported by potential protest users of each company on the right. Unlike was
the case for protest non/use motivations, there was a notable difference in responses between
those who were actually protesting and those who were interested, but not doing so. Here, we see
concerns about “losing connections” was by far the most common challenge for active protestors
(driven by people protesting Facebook). On the other hand, and raising important concerns related
to the discussions around the possible monopoly power of some technology companies, the lack of
alternative products was the most common roadblock to protest non/use for interested
respondents (across all the companies).
Missing out on information and losing connections, the two major challenges reported by
protest users of Facebook, are consistent with prior work [5]. As Facebook is primarily a social
networking site, it is unsurprising that these two options, which represent social challenges (as
opposed to economic or technical challenges) are common among active and potential protest
users.
In the case of Amazon, we see that paying higher prices for alternatives was the top challenge
for active protest users, but respondents who were interested in protesting Amazon identified the
lack of alternatives as the top roadblock. This disparity suggests that (perceptions of) higher prices
may be a roadblock for some, but a manageable challenge for others, hinting at a role of
socioeconomic status in the ability to become a protest user. We discuss these results further
below, putting them in the context of related findings from other studies of non/use and non-use
(e.g. [59]).

Proceedings of the ACM on Human-Computer Interaction, No. CSCW, Article 87, Publication date: November 2019

How Do People Change Their Technology Use in Protest?: Understanding “Protest Users” 87:15
Amazon was rated as the most difficult to protest by active protest users, with an average
difficulty of 2.4 on a 1 to 5 scale (with 1 corresponding to “very easy” and 5 to “very difficult”) and
Apple was rated as the least difficult, with an average of 1.7. For other companies, the average
rating was around 2 (“easy”) or lower. Overall, it seems our active protest users did not find it to
be especially difficult, although data beyond a single Likert-type response will be important to
confirm this result.
5 DISCUSSION
At a high level, our survey results suggest that protest users have become a substantial force in
the sociotechnical landscape. Although our 2019 survey was small and is just one survey, we
observed that three of out of every ten respondents are already protest users, and another almost
one-fifth of the respondents have an interest in becoming protest users. These results – along with
the more detailed findings about motivations, tactics, challenges, and roadblocks – have important
implications for a variety of stakeholders, including researchers in social computing and other
areas of computing, technology designers, and institutions that own prominent technologies. We
discuss some of these implications below.
5.1 Technologies to Support Protest Users
As noted above, the social computing literature and wider computing community have become
increasingly interested in developing technologies to support protest non/use (e.g. boycottassisting technologies [32,63], protective optimization technologies [44]). One of the most
significant implications of our results is that they suggest that there is a truly substantial “market”
for these technologies. Our findings indicate that this market may include up to almost half of
American Internet-using adults, providing substantial support for more research and development
in this area.
Additionally, our findings also present something of a partial roadmap for new technologies to
support effective protest non/use. For instance, our results highlight the importance of future
technologies that can offload the burden of finding and using alternative products for protest users
and thereby lower the threshold to participate in protest non/use. Such tools may meaningfully
increase the percentage of people who can actualize their desire to become protest users against
the target (i.e. move from the right side to the left side of Figure 3). Although these tools may
adopt a number of different approaches, one approach might be to act as an intermediary to a
desired service (e.g. purchasing some product), directing people to alternatives whenever possible.
For example, a browser extension could autonomously route shopping queries away from a
targeted company, with that targeted company being a backstop if there truly is no other company
offering the product at a similar price. One could also imagine a similar tool for web search that
routes search queries to minority players like DuckDuckGo when those queries reflect
information needs that are straightforward to satisfy (e.g. navigational queries like “CSCW 2019”).
The large number of existing protest users amongst our respondents and the wide variety of
tactics employed also introduce a promising opportunity for “computer-supported collective
action” [55]. For instance, new tools could help to identify and mobilize protest users who have
the most leverage over the target (e.g. influential members of a social network, people who
contributed especially valuable data, etc.). These tools could also make suggestions to existing
protest users about particular days to avoid a platform (i.e. a day-long boycott) or specific types of
fake data to provide.
Additionally, the prevalence of ad blockers and anti-tracking extensions among protest users
suggests that these tools could also coordinate collective action to make individual protests more
Proceedings of the ACM on Human-Computer Interaction, No. CSCW, Article 87, Publication date: November 2019

87:16

Hanlin Li et al.

effective. In particular, as visible progress of collective action sustains participation [33,55],
current ad blockers and anti-tracking browser extensions may consider communicating how many
protest users are taking action and estimates of the protest’s impact on web traffic [32] or ad
revenue [15] (e.g. “Over the last week, n other people have also been using this anti-Facebook
tracking extension and m ads have been blocked, costing the company p dollars”).
5.2 Designing and Studying with Protest Users in Mind
The results of our survey point to the need for researchers and developers to consider protest
non/use in the technology design process. This would involve asking questions like: How and why
might people contest a new feature or system? Are there ways to account for this contestation
before it starts? How resilient would the system be to such contestation? Designing with protest
users in mind may be a useful approach to shift designers’ attention to how people might
negatively react to technology and means building systems that recognize the value and power of
all technology stakeholders, including users, protest users, and non-users. This is an approach that
would further supplement existing user-centered design approaches, such as participatory design
[42] and value-sensitive design [14], and relates to the notion of “heuristic preventive design”
introduced at CSCW last year [32].
On a related note, social computing researchers also need to be aware of protest users as a
dimension (and potential confound) in studies of large-scale online platforms. For instance, our
results suggest that a study of Facebook use in the United States may want to consider how the
research questions and chosen methodologies (e.g. recruiting through Facebook ads) might be
affected by protest non/use. More generally, as the growing literature around social media and
other technologies emphasizes the demographic gap in technology use, future work should
particularly account for the potential influences of protest non/use on this gap. For instance, will
the demographics of Facebook users change because the younger population protest more?
5.3 Protest Users and Technology Non/Use
Our study unpacks the subset of technology non/use behaviors driven by protest, directly
responding to Baumer 2018’s call for examining “relationships between different form of
technology non-use and different types of motivations” [2]. As is discussed above in more detail,
our work also points to potentially unique characteristics of protest users with respect to
(non)users who are considered in studies about more general non-use and non/use. For instance,
although men and women are equally likely to deactivate Facebook, our results suggest that men
are more likely to be protest users of Facebook. Similarly, privacy drives both protest users and
(non)users to change their Facebook usage or leave Facebook, but protest users are uniquely
concerned about Facebook profiting off of their data. More generally, while our paper maps out a
new territory within the domain of non/use, our paper also highlights the need for more targeted
research on the relationship between protest use, non/use, and non-use.
5.4 Protests, Privacy, and Surveillance
Viewed through the lens of the relevant privacy literature (e.g. [21,38,39,49]), our findings
point to an interesting overlap between protest use and privacy-driven behavior, an overlap that is
fertile ground for future empirical and theoretical work. In particular, the exact same tactic – e.g.
using fake accounts / data and private browsing – can be deployed either as a means to protect
individual privacy or as a means to protest a company that makes money off of personal
Proceedings of the ACM on Human-Computer Interaction, No. CSCW, Article 87, Publication date: November 2019

How Do People Change Their Technology Use in Protest?: Understanding “Protest Users” 87:17
information or data labor [45]. Likely, in many cases the tactic is the result of both motivations at
the same time. This overlap highlights that actions that protect one’s privacy may go beyond
simple self-interest and are affected by complex sociotechnical contexts, e.g. the company’s
business model and public image. It also suggests the reverse: the literature on protests against
technology company has been dominated by a collective action frame, but there may also be
highly self-interested benefits and motivations to these protests.
The overlap between protest non/use and privacy-driven behaviors may additionally present
promising opportunities to leverage existing privacy protection tools for protesting purposes. For
example, AdNauseam, a browser extension that simulates random clicks on ads to obfuscate
tracking by online advertisers, may facilitate protests against technology companies by
automatically generating fake data to create “garbage” inputs to trained models [24]. Future work
might seek to estimate the economic and social effects of widespread obfuscation-based protests.
Additionally, the reported privacy-driven behaviors by protest users to avoid tracking by tech
companies suggest that future work may also want to examine protest non/use through a lens
informed by theories of surveillance [1,20]. In particular, past work from Albrechtslund has
contrasted vertical “Panopticon / Big Brother” concepts of surveillance (in which there exists a
hierarchy of “watchers” and “watched”) with horizontal “participatory surveillance” [1]. The
participatory surveillance framing argues peer-to-peer surveillance by social networking users is a
form of maintaining friendship and thereby empowering, playful, and positive [1]. These
potentially conflicting approaches to conceptualizing surveillance suggest conceptual
complications faced by protest users. Protest users’ obfuscating tactics (e.g. fake data, fake
accounts) to resist vertical surveillance may hinder their participation in social surveillance, as
they withhold data from target technologies. This is particularly interesting when considering
protests against social network companies like Facebook. For example, the Facebook protest users
who reported providing fake data to Facebook in our study may not see certain content with
which their friends have engaged and thus lose the opportunity to participate in the positive
aspects of social surveillance (while simultaneously receiving some protection from the negative
aspects of vertical surveillance). Similarly, the Facebook protest users who reported entirely
halting the use of Facebook (e.g. protest non-use) or contributing fake content (a protest use tactic
we observed), may lack the opportunity to make connections with people that share similar
interests. Future work should further investigate how protest non/use influences one’s ability to
engage with social surveillance.
5.5 Protest Users and Intelligent Technologies
Prior work on collective action campaigns suggests that protest users may be particularly
effective at impacting intelligent technologies. Vincent et al.’s work identified two types of
collective action campaigns that have the potential to meaningfully reduce the performance of
highly-profitable intelligent technologies like recommender systems: “data boycotts” and “data
strikes” [57]. Both of these campaigns map closely to the phenomena studied here. Boycotts
correspond directly to protest non-use. Some of the behaviors (e.g. anti-tracking) observed in our
survey could be used to contribute to a data strike.
Given the close correspondence of protest non/use, data strikes, and data boycotts, the
observed prevalence of protest non/use should be of significant concern to companies that use
data-driven intelligent technologies. According to Vincent et al.’s research, boycotts and strikes in
which 30% of the user base participates - the prevalence of protest users that we observed – can
meaningfully reduce the performance of a recommender system for the 70% of the user base that
does not protest. As such, given their prevalence, protest users are already likely reducing the
Proceedings of the ACM on Human-Computer Interaction, No. CSCW, Article 87, Publication date: November 2019

87:18

Hanlin Li et al.

performance of intelligent technologies owned by targeted companies, even for people who are
not protest users. If the scale of protest non/use grows, Vincent et al.’s work suggests that this
effect will continue to increase.
5.6 Protest Users and Monopolies
A concerning result in our survey is that many people felt they could not stop or change their
use of a given technology because there were no alternatives to this technology. This finding
provides a data point for the growing discussions about monopoly power of many of the
companies in the technology industry [23,36,37,58]. If a user of a technology cannot “put their
money where their mouth is” due to the lack of competitors, this supports an argument that there
has been a market failure. It may be that much of the protest use we observed would become
protest non-use if there were more competitors available. Indeed, this is the motivation for
Vincent et al.’s “data strike” concept: data strikes allow people to continue to use a platform while
exerting some leverage over it. Overall, it is clear that more research is needed on the relationship
between protest use, protest non-use and market competition. Our results provide a useful data
point on this relationship, but they come from just one survey of limited size and scope.
5.7 Future Work on Protest Users
At the most basic level, our findings highlight the need for follow-up work that examines the
prevalence and character of protest non/use in more detail. This would involve in-depth
qualitative research with protest users (and potential protest users), examining protest non/use in
more diverse geographic contexts (see Limitations below), and even perhaps running larger-scale
surveys.
Following prior work on non-use (e.g. [2,3,22]), social computing research should also examine
protest non/use explicitly through a socioeconomic lens. Our results suggest that there are
complex socioeconomic contours associated with protest non/use. In particular, there are hints in
our results of protest non/use being a privilege of people who can afford it, with lack of
alternatives being the most common roadblock to catalyzing interest in a protest into action. In the
terms of Wyatt’s distinction between voluntary and non-voluntary non-use [59], our study
reinforces that technology use can be non-voluntary as well. That is, our study provides early
evidence showing potential protest users were “stuck” using technologies that they were
interested in protesting. These results call out for future work to further investigate the role of
socioeconomic factors in protest non/use.
5.8 Limitations
A major limitation of our study was that we sampled only adult web users in the United States.
Of course, this population’s protest non/use is of interest to many stakeholders: this population is
both large in absolute number and is an important revenue source for prominent tech companies
[13]. However, we observed – as have others (e.g. [22]) – that technology non/use behavior varies
with respect to demographics, prominent tech companies vary around the world, and our
population is a small portion of overall web users. Future work should investigate how the
prevalence, motivations, and tactics of protest users change across the globe. The challenges and
roadblocks facing protest users and potential protest users will likely also be another source of
important geographic variation.

Proceedings of the ACM on Human-Computer Interaction, No. CSCW, Article 87, Publication date: November 2019

How Do People Change Their Technology Use in Protest?: Understanding “Protest Users” 87:19
Although our use of third-party services to collect nationally representative data was
appropriate for our early-stage contribution to the discussion around protest non/use and is a
standard practice in the social computing literature (e.g. [2,8]), this approach limits our ability to
validate our results. Given that our major findings are based on descriptive results with large
effect sizes, it seems unlikely that this is a major validity threat. However, any fine-grained results
from our surveys or similar surveys must be taken with a grain of salt and precise estimation
about specific phenomena (e.g. “how many people use Private Browsing to view Facebook
pages?”) are likely inappropriate given the nature of our data.
Our major findings relied on multiple-choice multiple-answer responses. Although we aimed
to cover a wide variety of possible answers motivated by themes in the news media, the literature,
and our 2017 free text responses, it is possible we missed certain answers or worded them in a way
that confused respondents. We mitigated this risk through the inclusion of an “Other” option in
most questions and did not see evidence of major omissions in those responses. That said, we must
assume there is some risk of design error on top of any sampling error.
Finally, it should be reiterated that the design differences in our two surveys provide important
context for any comparison between the 2017 results and the 2019 results. We adjusted our survey
design for the 2019 survey to more directly answer our research questions about protest users’
motivations and challenges instead of deploying an identical survey. We also used two different
survey companies, each with its own proprietary sampling approach. As noted above, these
decisions led to us placing more emphasis on the descriptive statistics from the 2019 survey than
on any direct comparisons between the two surveys.
6 CONCLUSION
In this paper, we present the results of two surveys that explore if, how, and why people stop
or change their usage of major technology companies’ products as a form of protest (we call such
people protest users). We find evidence that such behavior is increasingly common (almost half of
our respondents were protest users or interested in becoming protest users), and driven by a
variety of motivations, particularly concerns about privacy and business models that profit from
user data. Moreover, our survey highlights common tactics that protest users employed in protest,
and the challenges and roadblocks that inhibited these protests. This work provides important
context for the growing discussion around the relationship and power dynamics between the
public and technology companies. We present design implications for new technologies to better
support protest users and highlight important follow-up social computing research into their
protesting behaviors.
ACKNOWLEDGEMENTS
We are grateful to our anonymous reviewers for their comments and suggestions. This work
was supported in part by NSF grants IIS-1815507, IIS-1707296, and IIS-1707319.

REFERENCES
[1]

Anders Albrechtslund. 2008. Online social networking as participatory surveillance. First Monday 13, 3 (2008).

[2]

Eric P. S. Baumer. 2018. Socioeconomic Inequalities in the Non Use of Facebook. In Proceedings of the 2018 CHI
Conference
on
Human
Factors
in
Computing
Systems
(CHI
’18),
616:1–616:14.
DOI:https://doi.org/10.1145/3173574.3174190

[3]

Eric P. S. Baumer, Jenna Burrell, Morgan G. Ames, Jed R. Brubaker, and Paul Dourish. 2015. On the Importance and
Implications of Studying Technology Non-use. interactions 22, 2 (February 2015), 52–56.
DOI:https://doi.org/10.1145/2723667

Proceedings of the ACM on Human-Computer Interaction, No. CSCW, Article 87, Publication date: November 2019

87:20

Hanlin Li et al.

[4]

Eric P.S. Baumer. 2015. Usees. In Proceedings of the 33rd Annual ACM Conference on Human Factors in Computing
Systems (CHI ’15), 3295–3298. DOI:https://doi.org/10.1145/2702123.2702147

[5]

Eric P.S. Baumer, Phil Adams, Vera D. Khovanskaya, Tony C. Liao, Madeline E. Smith, Victoria Schwanda Sosik, and
Kaiton Williams. 2013. Limiting, Leaving, and (Re)Lapsing: An Exploration of Facebook Non-use Practices and
Experiences. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (CHI ’13), 3257–3266.
DOI:https://doi.org/10.1145/2470654.2466446

[6]

Eric PS Baumer, Morgan G Ames, Jenna Burrell, Jed R Brubaker, and Paul Dourish. 2015. Why study technology nonuse? First Monday 20, 11 (2015).

[7]

Eric PS Baumer, Shion Guha, Emily Quan, David Mimno, and Geri K Gay. 2015. Missing photos, suffering withdrawal,
or finding freedom? How experiences of social media non-use influence the likelihood of reversion. Social Media+
Society 1, 2 (2015), 2056305115614851.

[8]

Eric P.S. Baumer, Xiaotong Xu, Christine Chu, Shion Guha, and Geri K. Gay. 2017. When Subjects Interpret the Data:
Social Media Non-use As a Case for Adapting the Delphi Method to CSCW. In Proceedings of the 2017 ACM Conference
on Computer Supported Cooperative Work and Social Computing
(CSCW
’17),
1527–1543.
DOI:https://doi.org/10.1145/2998181.2998182

[9]

Spencer Beecher, Don van der Drift, David Martin, Lindsay Vass, Sergey Goder, Benedict Lim, and Matt Langner. 2019.
facebookincubator/bootstrapped.
bootstrapped
Github
Repository.
Retrieved
from
https://github.com/facebookincubator/bootstrapped

[10] US Census Bureau. Income and Poverty in the United States: 2017. Retrieved June 23, 2019 from
https://www.census.gov/data/tables/2018/demo/income-poverty/p60-263.html
[11] US Census Bureau. 2017 National Population Projections Tables. Retrieved August 12, 2019 from
https://www.census.gov/data/tables/2017/demo/popproj/2017-summary-tables.html
[12] Pierre Dragicevic. 2016. Fair statistical communication in HCI. In Modern Statistical Methods for HCI. Springer, 291–
330.
[13] Kerry Flynn. 2018. Facebook’s making more money per user in North America than ever before. Digiday. Retrieved
April 3, 2019 from https://digiday.com/marketing/facebooks-making-money-per-user-north-america-ever/
[14] Batya Friedman and Helen Nissenbaum. 1996. Bias in Computer Systems. ACM Trans. Inf. Syst. 14, 3 (July 1996), 330–
347. DOI:https://doi.org/10.1145/230538.230561
[15] José González Cabañas, Ángel Cuevas, and Rubén Cuevas. 2017. FDVT: Data Valuation Tool for Facebook Users. In
Proceedings of the 2017 CHI Conference on Human Factors in Computing Systems (CHI ’17), 3799–3809.
DOI:https://doi.org/10.1145/3025453.3025903
[16] Kevin Granville. 2018. Facebook and Cambridge Analytica: What You Need to Know as Fallout Widens. N. Y. Times
(March 2018). Retrieved from https://www.nytimes.com/2018/03/19/technology/facebook-cambridge-analyticaexplained.html
[17] Rebecca Greenfield, Sarah Frier, and Ben Brody. 2018. NAACP Seeks Week-Long Facebook Boycott Over Racial
Targeting. Bloomberg.com (December 2018). Retrieved from https://www.bloomberg.com/news/articles/2018-1217/naacp-calls-for-week-long-facebook-boycott-over-racial-targeting
[18] Jens Grossklags and Alessandro Acquisti. 2007. When 25 Cents is Too Much: An Experiment on Willingness-To-Sell
and Willingness-To-Protect Personal Information. In WEIS.
[19] Shion Guha, Eric P.S. Baumer, and Geri K. Gay. 2018. Regrets, I’Ve Had a Few: When Regretful Experiences Do (and
Don’T) Compel Users to Leave Facebook. In Proceedings of the 2018 ACM Conference on Supporting Groupwork (GROUP
’18), 166–177. DOI:https://doi.org/10.1145/3148330.3148338
[20] Shion Guha and Jeremy Birnholtz. 2013. Can you see me now?: location, visibility and the management of impressions
on foursquare. In Proceedings of the 15th international conference on Human-computer interaction with mobile devices
and services, 183–192.
[21] Shion Guha and Stephen B. Wicker. 2015. Do Birds of a Feather Watch Each Other?: Homophily and Social
Surveillance in Location Based Social Networks. In Proceedings of the 18th ACM Conference on Computer Supported
Cooperative Work & Social Computing (CSCW ’15), 1010–1020. DOI:https://doi.org/10.1145/2675133.2675179
[22] Eszter Hargittai. 2007. Whose space? Differences among users and non-users of social network sites. Journal of
computer-mediated communication 13, 1 (2007), 276–297.
[23] Astead W. Herndon. 2019. Elizabeth Warren Proposes Breaking Up Tech Giants Like Amazon and Facebook. The New
York Times. Retrieved April 4, 2019 from https://www.nytimes.com/2019/03/08/us/politics/elizabeth-warrenamazon.html
Proceedings of the ACM on Human-Computer Interaction, No. CSCW, Article 87, Publication date: November 2019

How Do People Change Their Technology Use in Protest?: Understanding “Protest Users” 87:21
[24] Daniel C Howe and Helen Nissenbaum. 2017. Engineering privacy and protest: A case study of AdNauseam. In CEUR
Workshop Proceedings, 57–64.
[25] Isaac L. Johnson, Yilun Lin, Toby Jia-Jun Li, Andrew Hall, Aaron Halfaker, Johannes Schöning, and Brent Hecht. 2016.
Not at Home on the Range: Peer Production and the Urban/Rural Divide. In Proceedings of the 2016 CHI Conference on
Human Factors in Computing Systems (CHI ’16), 13–25. DOI:https://doi.org/10.1145/2858036.2858123
[26] Jana Kasperkevic. 2018. Amazon faces boycott ahead of holidays as public discontent grows. the Guardian (December
2018). Retrieved from https://www.theguardian.com/technology/2018/dec/17/amazon-boycott-customers-holidayshopping
[27] Brayden King. 2016. Reputation, risk, and anti-corporate activism: How social movements influence corporate
outcomes.
The
Consequences
of
Social
Movements
(January
2016),
215–236.
DOI:https://doi.org/10.1017/CBO9781316337790.009
[28] Brayden G. King and Mary Hunter McDonnell. 2015. Good firms, good targets: The relationship among corporate
social responsibility, reputation, and activist targeting. Corporate Social Responsibility in a Globalizing World (January
2015), 430–454. DOI:https://doi.org/10.1017/CBO9781316162354.013
[29] Sebastian Koos. 2012. What drives political consumption in Europe? A multi-level analysis on individual
characteristics, opportunity structures and globalization. Acta Sociologica 55, 1 (March 2012), 37–57.
DOI:https://doi.org/10.1177/0001699311431594
[30] Cliff Lampe, Jessica Vitak, and Nicole Ellison. 2013. Users and nonusers: Interactions between levels of adoption and
social capital. In Proceedings of the 2013 conference on Computer supported cooperative work, 809–820.
[31] Jaron Lanier and E Glen Weyl. 2018. A Blueprint for a Better Digital Society. Harvard Business Review (2018).
[32] Hanlin Li, Bodhi Alarcon, Sara Milkes Espinosa, and Brent Hecht. 2018. Out of Site: Empowering a New Approach to
Online Boycotts. Proc. ACM Hum.-Comput. Interact. 2, CSCW (November 2018), 106:1–106:28.
DOI:https://doi.org/10.1145/3274375
[33] Kimberly Ling, Gerard Beenen, Pamela Ludford, Xiaoqing Wang, Klarissa Chang, Xin Li, Dan Cosley, Dan Frankowski,
Loren Terveen, Al Mamunur Rashid, Paul Resnick, and Robert Kraut. 2005. Using Social Psychology to Motivate
Contributions to Online Communities. Journal of Computer-Mediated Communication 10, 4 (July 2005), 00–00.
DOI:https://doi.org/10.1111/j.1083-6101.2005.tb00273.x
[34] Michael Livingston. 2018. Here’s when boycotts have worked and when they haven’t. latimes.com (December 2018).
Retrieved from https://www.latimes.com/nation/la-na-boycotts-history-20180228-htmlstory.html
[35] Amanda Lotz. 2019. “Big Tech” isn’t one big monopoly – it’s 5 companies all in different businesses. Retrieved from
https://theconversation.com/big-tech-isnt-one-big-monopoly-its-5-companies-all-in-different-businesses-92791
[36] Farhad Manjoo. 2018. Stumbles? What Stumbles? Big Tech Is as Strong as Ever. The New York Times. Retrieved April 4,
2019 from https://www.nytimes.com/2018/08/01/technology/big-tech-earnings-stumbles.html
[37] Antonio García Martínez. 2019. Facebook Is Not a Monopoly, but It Should Be Broken Up. Wired. Retrieved April 4,
2019 from https://www.wired.com/story/facebook-not-monopoly-but-should-broken-up/
[38] Rahat Masood, Dinusha Vatsalan, Muhammad Ikram, and Mohamed Ali Kaafar. 2018. Incognito: A Method for
Obfuscating Web Data. In Proceedings of the 2018 World Wide Web Conference on World Wide Web - WWW ’18, 267–
276. DOI:https://doi.org/10.1145/3178876.3186093
[39] Arunesh Mathur, Jessica Vitak, Arvind Narayanan, and Marshini Chetty. 2018. Characterizing the Use of BrowserBased Blocking Extensions To Prevent Online Tracking. Fourteenth Symposium on Usable Privacy and Security (SOUPS
2018), 2018
[40] J. Nathan Matias. 2016. Going Dark: Social Factors in Collective Action Against Platform Operators in the Reddit
Blackout. In Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems (CHI ’16), 1138–1151.
DOI:https://doi.org/10.1145/2858036.2858391
[41] Mary-Hunter McDonnell, Brayden G King, and Sarah A. Soule. 2015. A Dynamic Process Model of Private Politics:
Activist Targeting and Corporate Receptivity to Social Challenges. Am Sociol Rev 80, 3 (June 2015), 654–678.
DOI:https://doi.org/10.1177/0003122415581335
[42] Michael J. Muller. 2003. The Human-computer Interaction Handbook. In Julie A. Jacko and Andrew Sears (eds.). L.
Erlbaum Associates Inc., Hillsdale, NJ, USA, 1051–1068.
[43] Benjamin J. Newman and Brandon L. Bartels. 2011. Politics at the Checkout Line: Explaining Political Consumerism in
the United States. Political Research Quarterly 64, 4 (2011), 803–817.
[44] Rebekah Overdorf, Bogdan Kulynych, Ero Balsa, Carmela Troncoso, and Seda Gürses. 2018. POTs: Protective
Optimization Technologies. arXiv preprint arXiv:1806.02711 (2018).
Proceedings of the ACM on Human-Computer Interaction, No. CSCW, Article 87, Publication date: November 2019

87:22

Hanlin Li et al.

[45] Eric A Posner and E Glen Weyl. 2018. Radical Markets: Uprooting Capitalism and Democracy for a Just Society.
Princeton University Press.
[46] Joseph Reagle and Lauren Rhue. 2011. Gender Bias in Wikipedia and Britannica. International Journal of
Communication 5, 0 (August 2011), 21.
[47] Elissa M. Redmiles, Sean Kross, and Michelle L. Mazurek. 2016. How I Learned to Be Secure: A Census-Representative
Survey of Security Advice Sources and Behavior. In Proceedings of the 2016 ACM SIGSAC Conference on Computer and
Communications Security (CCS ’16), 666–677. DOI:https://doi.org/10.1145/2976749.2978307
[48] Kenneth Rogoff. 2019. Big tech has too much monopoly power – it’s right to take it on. the Guardian (April 2019).
Retrieved from https://www.theguardian.com/technology/2019/apr/02/big-tech-monopoly-power-elizabeth-warrentechnology
[49] Shruti Sannon, Natalya N Bazarova, and Dan Cosley. 2018. Privacy lies: Understanding how, when, and why people lie
to protect their privacy in multiple online contexts. In Proceedings of the 2018 CHI Conference on Human Factors in
Computing Systems, 52.
[50] Christine Satchell and Paul Dourish. 2009. Beyond the user: use and non-use in HCI. In Proceedings of the 21st Annual
Conference of the Australian Computer-Human Interaction Special Interest Group: Design: Open 24/7, 9–16.
[51] Sarita Yardi Schoenebeck. 2014. Giving Up Twitter for Lent: How and Why We Take Breaks from Social Media. In
Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (CHI ’14), 773–782.
DOI:https://doi.org/10.1145/2556288.2556983
[52] Alana Semuels. 2017. Why #DeleteUber and Other Boycotts Matter. Atlantic (February 2017). Retrieved from
https://www.theatlantic.com/business/archive/2017/02/why-deleteuber-and-other-boycotts-matter/517416
[53] Jun Shao. 2003. Impact of the bootstrap on sample surveys. Statistical Science 18, 2 (2003), 191–198.
[54] Aaron Shaw and Eszter Hargittai. 2018. The Pipeline of Online Participation Inequalities: The Case of Wikipedia
Editing. J Commun 68, 1 (February 2018), 143–168. DOI:https://doi.org/10.1093/joc/jqx003
[55] Aaron Shaw, Haoqi Zhang, Andrés Monroy-Hernández, Sean Munson, Benjamin Mako Hill, Elizabeth Gerber, Peter
Kinnaird, and Patrick Minder. 2014. Computer supported collective action. interactions 21, 2 (March 2014), 74–77.
DOI:https://doi.org/10.1145/2576875
[56] Stefan Stieger, Christoph Burger, Manuel Bohn, and Martin Voracek. 2013. Who commits virtual identity suicide?
Differences in privacy concerns, internet addiction, and personality between Facebook users and quitters.
Cyberpsychology, Behavior, and Social Networking 16, 9 (2013), 629–634.
[57] Nicholas Vincent, Brent Hecht, and Shilad Sen. 2019. “Data Strikes”: Evaluating the Effectiveness of New Forms of
Collective Action Against Technology Platforms. In Proceedings of The Web Conference 2019.
[58] Robert Wright. 2018. Why We Can’t Let Google Monopolize AI. Wired. Retrieved April 4, 2019 from
https://www.wired.com/story/google-artificial-intelligence-monopoly/
[59] Sally ME Wyatt, Nelly Oudshoorn, and Trevor Pinch. 2003. Non-users also matter: The construction of users and nonusers of the Internet. Now users matter: The co-construction of users and technology (2003), 67–79.
[60] Alyson Leigh Young and Anabel Quan-Haase. 2013. Privacy Protection Strategies on Facebook. Information,
Communication & Society 16, 4 (May 2013), 479–500. DOI:https://doi.org/10.1080/1369118X.2013.777757
[61] 2018.
History
of
Successful
Boycotts
Ethical
Consumer.
https://www.ethicalconsumer.org/ethicalcampaigns/boycotts/history-successful-boycotts

Retrieved

from

[62] Standing
up
for
what’s
right
|
Uber
Newsroom.
https://www.uber.com/newsroom/standing-up-for-whats-right-3/

24,

from

Retrieved

June

2019

[63] Buycott. Buycott App. Retrieved July 11, 2018 from https://www.buycott.com/
[64] Prime Day: activists protest against Amazon in cities across US. The Guardian. Retrieved August 14, 2019 from
https://www.theguardian.com/technology/2019/jul/15/prime-day-activists-plan-protests-in-us-cities-and-a-boycott-ofe-commerce-giant
[65] Why Thousands Of Amazon Workers Are Striking On Prime Day | HuffPost. Retrieved August 14, 2019 from
https://www.huffpost.com/entry/amazon-prime-day-minnesota-strike-germany-protest_n_5d2d52f8e4b02fd71dd95281
Received April 2019; revised June 2019; accepted August 2019

Proceedings of the ACM on Human-Computer Interaction, No. CSCW, Article 87, Publication date: November 2019
