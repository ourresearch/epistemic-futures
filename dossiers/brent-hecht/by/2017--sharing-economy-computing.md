---
title: "The Sharing Economy in Computing: A Systematic Literature Review"
person: brent-hecht
attendance: unconfirmed
section: by
type: journal-article
year: 2017
date: 2017-12-06
venue: "Proceedings of the ACM on Human-Computer Interaction"
authors: "Tawanna R. Dillahunt, Xinyi Wang, Earnest Wheeler, Hao Fei Cheng, Brent Hecht, Haiyi Zhu"
source_url: https://doi.org/10.1145/3134673
fulltext_url: https://brenthecht.com/publications/cscw2018pacm_sharingeconomylitreview.pdf
openalex_id: W2771827553
doi: https://doi.org/10.1145/3134673
oa_status: closed
cited_by_count: 132
retrieved: 2026-08-13
content: full-text
notes: "Full text from the author's self-archived PDF at https://brenthecht.com/publications/cscw2018pacm_sharingeconomylitreview.pdf (text extracted with pdftotext; PDF not stored); title expanded from the OpenAlex record's truncated form using the author's own publications page / Semantic Scholar"
---

# The Sharing Economy in Computing: A Systematic Literature Review

## Full text

1

The Sharing Economy in Computing:
A Systematic Literature Review
TAWANNA R. DILLAHUNT, University of Michigan
*XINYI WANG, University of Minnesota, Twin Cities
*EARNEST WHEELER, University of Michigan
HAO FEI CHENG, University of Minnesota, Twin Cities
BRENT HECHT, Northwestern University
HAIYI ZHU, University of Minnesota, Twin Cities
The sharing economy has quickly become a very prominent subject of research in the broader computing
literature and the in human–computer interaction (HCI) literature more specifically. When other computing
research areas have experienced similarly rapid growth (e.g., human computation, eco-feedback technology),
early stage literature reviews have proved useful and influential by identifying trends and gaps in the literature
of interest and by providing key directions for short- and long-term future work. In this paper, we seek to
provide the same benefits with respect to computing research on the sharing economy. Specifically, following
the suggested approach of prior computing literature reviews, we conducted a systematic review of sharing
economy articles published in the Association for Computing Machinery Digital Library to investigate the
state of sharing economy research in computing. We performed this review with two simultaneous foci: a
broad focus toward the computing literature more generally and a narrow focus specifically on HCI literature.
We collected a total of 112 sharing economy articles published between 2008 and 2017 and through our
analysis of these papers, we make two core contributions: (1) an understanding of the computing community’s
contributions to our knowledge about the sharing economy, and specifically the role of the HCI community in
these contributions (i.e., what has been done) and (2) a discussion of under-explored and unexplored aspects of
the sharing economy that can serve as a partial research agenda moving forward (i.e. what is next to do). 1

2

3

4

5

CCS Concepts: • Human-centered computing → Human-computer interaction (HCI); Collaborative
and social computing;
Additional Key Words and Phrases: Sharing Economy; Literature Review; Collaborative Economy; Collaborative
Consumption; Physical Crowdsourcing; Gig Economy; Taxonomy.
ACM
ACM Reference
Reference format:
Format:
Tawanna
Dillahunt, *Xinyi
*Xinyi Wang,
Wang, *Earnest
*Earnest Wheeler,
Wheeler,Hao
HaoFei
FeiCheng,
Cheng,Brent
BrentHecht,
Hecht,and
andHaiyi
HaiyiZhu.
Zhu.2017.
2017.
Tawanna R.
R. Dillahunt,
The
Hum.-Comput.
Interact.
1, 2,
The Sharing
Sharing Economy
Economy in
in Computing:
Computing:AASystematic
SystematicLiterature
LiteratureReview.
Review.Proc.
Proc.ACM
ACM
Hum.-Comput.
Interact.
Article
38 Article
(November
26 pages.
1,
CSCW,
38 2017),
(November
2017), 26 pages. https://doi.org/10.1145/3134673
https://doi.org/10.1145/3134673

38

1 *X. Wang and E. Wheeler contributed equally to this work.

This work was supported by the National Science Foundation, under grant IIS-1352915, grant CRII-1566149, and grant
IIS-1707296, and by a Microsoft FUSE Research Award.
Authors’ addresses: T. Dillahunt, Earnest Wheeler, School of Information, University of Michigan, 105 S. State Street, Ann
Arbor, MI 48105, US; Xinyi Wang, Hao Fei Cheng, Haiyi Zhu, University of Minnesota, Twin Cities, 200 Union Street SE,
Minneapolis, MN 55455, US; Brent Hecht, Northwestern University, 2240 Campus Road, Evanston, IL 60208, US.
Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee
provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the
full citation on the first page. Copyrights for components of this work owned by others than the author(s) must be honored.
Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires
prior specific permission and/or a fee. Request permissions from permissions@acm.org.
© 2017 Copyright held by the owner/author(s). Publication rights licensed to Association for Computing Machinery.
2573-0142/2017/11-ART38 $15.00
https://doi.org/10.1145/3134673

38

Proc. ACM Hum.-Comput. Interact., Vol. 1, No. 2, Article 38. Publication date: November 2017.

10

PACM on Human-Computer Interaction, Vol. 1, No. CSCW, Article 38. Publication date: November 2017.

9

38:2

T. Dillahunt et al.

1 INTRODUCTION
Information and communication technologies (ICTs) have enabled individuals to share many new
aspects of their lives, ranging from their cars (e.g., Lyft and UberX) to their households (e.g.,
Airbnb). These sharing practices have been described as the “sharing economy.” Although there is
no widely adopted formal definition of the sharing economy, the term is often used to broadly refer
to exchange of un(der)used assets or services between peers or between businesses and consumers,
either free or for a fee [11]. According to a 2016 report from the U.S. Department of Commerce, at
least 17 sharing economy firms are each worth more than $1 billion, with Uber leading the pack at
a $62.5 billion market value [93] (for comparison, Ford Motor Company’s market value is about $45
billion). Alongside this trend, the sharing economy has quickly become one of the most prominent
subjects in the computing research community, especially in human-computer interaction (HCI)
[58].
In the past, when other computing research areas have experienced similarly rapid growth,
early stage literature reviews (e.g., [26, 38, 81, 103]) have helped to identify trends and gaps in the
literature and have provided key directions for short- and long-term future work. The goal of this
paper is to do the same for the computing community’s research on the sharing economy. While a
more general literature review of the sharing economy exists [20], this review did not consider the
computing community’s contributions to the literature. In this paper, we seek to address this gap.
More specifically, following the approach of prior reviews in computing, we conducted a systematic literature review (SLR) of sharing economy papers (112 total) in the Association of Computing
Machinery (ACM)’s Digital Library (DL)—the most comprehensive repository of computing literature [3] —published between January 2008 and June 2017. In keeping with the standard approach
to SLRs [53], we started by framing our two key research questions:
• What is the state of sharing economy research in computing and in HCI particularly? In
other words, what has been done?
• What research areas have been unexplored and underexplored? In other words, what should
we do next?
In addressing our questions above, we examined our results with both a general computing
lens and a narrower lens focused on the subset of the computing literature that comes from the
HCI community. Our inclusion of HCI as a secondary facet of analysis was not only driven by
the home discipline of this submission: rather, we hypothesized that (1) HCI would provide the
most numerous contributions to the computing literature and thus would demand further inquiry
and that (2) HCI’s contributions would be relatively distinct compared to those of the rest of the
computing literature, possibly providing important insight for future research directions. As we
discuss in the next sections, our findings supported both of these hypotheses.
More generally, our results (1) reveal important trends in current computing and HCI research on
the sharing economy and (2) point to a partial agenda for future sharing economy research. With
respect to the former, we found that the most common themes in computing research on the sharing
economy include optimization, socio-technical design, geography, and social relationships, and we
provide summaries of the research in each of these high-interest areas. We also found that half of
the sharing economy literature in the ACM DL comes from HCI and is overwhelmingly qualitative
(as opposed to the non-HCI research), among other results. With respect to a research agenda, our
results highlight immediate opportunities for future sharing economy work that focuses on diverse
geographies, marrying HCI perspectives with non-HCI approaches, prioritizing implications for
policy, incorporating knowledge from pre-sharing economy analogous contexts, and others.
Proc. ACM Hum.-Comput. Interact., Vol. 1, No. 2, Article 38. Publication date: November 2017.

PACM on Human-Computer Interaction, Vol. 1, No. CSCW, Article 38. Publication date: November 2017.

The Sharing Economy in Computing

38:3

Next, we highlight exemplative work that informed the design of our literature review. We then
discuss our methods, and this is followed by an elaboration of the findings as they relate to each of
our research questions.
2 RELATED WORK
Because this paper is a literature review, the bulk of our consideration of related work comes in
the form of the data we analyze, the results that emerge from our analyses, and the implications
we drew from these results. However, prior to beginning our discussion of methods, results, and
implications, we want to highlight two areas of prior work that can provide useful context for our
research: (1) the approaches taken in previous literature reviews in computing and HCI (and how
we followed standard approaches here as well), and (2) existing summative work on the sharing
economy (and how our research complements this work).
2.1 Literature Reviews in Computing and HCI
Conducting literature reviews is a relatively common practice in computing [26, 38, 65, 81, 85, 103].
Indeed, as noted, early-stage reviews have identified trends and gaps in the literature and provided
insights for future research that have proven to have substantial impact (e.g., [38, 81]). In this paper,
we seek to provide the same benefits for computing research on the sharing economy.
Many of the aforementioned literature reviews make specific contributions to a sub-field of
computing, such as HCI, ICTD, or CSCW. While these researchers used the ACM Digital Library as
a primary database, most searched specifically for sub-fields (e.g., [38]). Following the approach
of these prior literature reviews, we turned to the ACM Digital Library (ACM DL); however, we
searched the full database and all of its venues. According to the ACM2 , the ACM DL is the most
comprehensive set of bibliographic records and full-text articles in computing and information
technology. Following Pittaway [79], we took a systematic approach to our literature review. We
also considered López’s general call for more SLRs in HCI, CSCW, and Ubicomp [65]. This approach
helped us to identify existing gaps in the research field and to make suggestions for addressing
them.
2.2 Reviews of the Sharing Economy
We only identified two literature reviews of the sharing economy: (1) a short review of how the
sharing economy has been defined from Oh and Moon [74] in the ACM, and (2) a holistic and
broad review of the sharing economy outside of the ACM [20]. Oh and Moon’s short paper was a
literature review of definitions of the sharing economy from 172 academic journals, magazines,
and dissertations from 2008 to 2015. The authors excluded online publications and did not specify a
review of conference papers. The authors conducted their search in the LexisNexis database, which
describes itself as a “provider of legal, government, business and high-tech information sources”
[63].
Cheng’s article is a systematic and holistic review of 66 journal articles about the sharing economy
from 2008 to 2015. The search for this article [20] was done from three of the largest online search
engines and online databases, Science Direct, Google Scholar and EBSCOHost [16]; however, the
researcher focused his discussion of implications on those for the tourism research (the home
discipline of the publishing journal). Additionally and critically, deeming industry reports and
conference papers—the primary publication outlets for computing—as “grey” literature, this review
excluded most of computing’s contributions to the sharing economy literature. Our review is
intended to address this important gap in our summative knowledge about the sharing economy.
2 http://www.acm.org/publications/about-publications

Proc. ACM Hum.-Comput. Interact., Vol. 1, No. 2, Article 38. Publication date: November 2017.

PACM on Human-Computer Interaction, Vol. 1, No. CSCW, Article 38. Publication date: November 2017.

38:4

T. Dillahunt et al.

3 METHOD
To address our two research questions, we conducted a systematic literature review (SLR) of sharing
economy research in the ACM Digital Library (DL). As discussed above, we selected the ACM as
our corpus because it has been used in past work as the corpus for similar literature reviews in
other domains (e.g., [26, 38, 65, 81, 85, 103]).
SLRs are designed to identify existing gaps in a research field and to make suggestions for
addressing these gaps. Our methods were informed by Pittaway’s guide to conduct an SLR [79].
Because the conception of applications as part of a larger sharing economy has only arisen since
2008 [62], our search included literature from January 2008 to July 2017. Next, we provide a summary
of our steps.3
3.1 Identifying Search Terms / Corpus Collection
The first step of any SLR is to identify relevant work [53, 79] and to achieve this, we identified
our search terms. The sharing economy has been referred to by many terms. We sought to build
a comprehensive set of keywords to include terms for the sharing economy that may have been
used in older literature. To accomplish this, we conducted an iterative search of repeated, relevant
keywords in our corpus. First, we identified search terms based on common terms that have been
used in HCI and in well-known and cited monographs of the sharing economy literature [14, 90]. The
initial search terms were: “sharing economy,” “collaborative consumption,” “peer-to-peer exchange,”
“physical crowdsourcing,” and “gig economy.”
Next, we extracted the author-defined keywords from the corpus resulting from our first search
of the digital ACM library. We compiled a list of all keywords that appeared in two or more papers,
and then filtered those keywords that were overly vague (e.g., multi-agent systems, transportation)
or conceptually unrelated to the sharing economy (e.g., dynamic pricing, experimentation). We
considered the remaining repeated keywords to be synonymous or closely related to the sharing
economy, and performed a search with that list. We performed this process three times, until the
search yielded no new papers, for a total of four searches. Ultimately, we identified the following
21 keywords, which served as seeds for our final ACM search: “sharing economy,” “collaborative
consumption,” “peer-to-peer exchange,” “physical crowdsourcing,” “gig economy,” “algorithmic
management,” “collaborative economy,” “local online exchange,” “mobile crowdsourcing,” “network
hospitality,” “on-the-go crowdsourcing,” “platform economy,” “ridesharing,” “social exchange,” “surge
pricing,” “timebanking,” “micro tasking,” “microtasking,” “situated crowdsourcing,” “workplace
studies,” and “spatial crowdsourcing.”
This search procedure yielded 354 papers. Next, we filtered articles using specific selection
criteria to assure their appropriateness, or fit to the SLR, as described in the next section.
3.2 Selection Criteria
Our first selection criterion was that articles had to be written in English owing to the constraints of
the research team and the general tendency for high-quality research in computing to be published
in English (for better or worse). Second, we filtered articles to exclude research that was not
substantively connected to the sharing economy (despite its use of one of the keywords) or research
that fell below a quality threshold. To implement this second stage, we utilized a version of the
approach by Busalim and Che Hussin [17]. Specifically, researchers read each paper and ranked
each article as high, medium or low on the following four criteria: (1) the paper’s topic was related
to the sharing economy, (2) the paper had a clear research methodology, (3) the paper described
the data collection process, and (4) the paper had key findings that aligned with the posed research
3 Details of the SLR process are available in Appendix A.

Proc. ACM Hum.-Comput. Interact., Vol. 1, No. 2, Article 38. Publication date: November 2017.

PACM on Human-Computer Interaction, Vol. 1, No. CSCW, Article 38. Publication date: November 2017.

The Sharing Economy in Computing

38:5

questions. Those criteria that ranked as high received a score (loading factor) of 2, medium 1, and
low 0 [73]. Research papers that received a 0 for the first criterion (papers unrelated to the sharing
economy) were immediately excluded. Any paper that received a 1 or a 2 on the first criterion and
had a total score of 5 passed through the filter; if the total score was 4 or below, the paper was
excluded. It is important to point that out we did not exclude short papers, extended workshop
papers, panels, or alt.chi paper purely due to their format; they were processed like full papers.
After the second stage of filtering, we were left with 119 sharing economy articles. Of these 119
articles, we further excluded seven that we considered to be irrelevant to the sharing economy or
to be think pieces (see Appendix A.2.2 Selection Criteria for details). This left us with a final corpus
of 112 papers. 4 .
3.3 Data Extraction
Per [24, p.36], we extracted excerpts from each work to provide: (1) the stated or implied problem or
research question that was being addressed, (2) the central purpose or focus of the study, (3) a brief
statement about the sample population or subjects, and (4) key results that related to the proposed study.
In addition, we extracted the list of authors, publication year, title, publication venue, geographic
region, the research questions, and how each paper defined the sharing economy. We also extracted
keywords and coded the methodology employed as quantitative, qualitative, mixed methods,
design5 , math modeling6 , or literature review. In some cases, two methodology codes were applied.
For example, a paper that presented the design and field deployment of a new sharing economy
application, and reported results from a qualitative user study, it would be coded as both “design”
and “qualitative.”
3.4 Data Analysis
To identify topical themes in the literature, three members of our research team coded each
paper in the final corpus. This was beneficial for addressing both research questions. We used
the selection criteria to extract and summarize article contents as attribute codes [75, 84] into a
shared spreadsheet. This allowed us to develop a synopsis for each work and to sort the literature
according to publication year, methodology used, populations sampled, instances or applications of
the sharing economy studied (e.g., Airbnb, Lyft), and by publication venue.
More specifically, we used hybrid coding to assign topical codes to each paper [98]. We leveraged
existing frameworks [76] to create a priori codes. We also coded openly in our initial coding phase
and followed this with focused coding.7 Focused coding allowed us to categorize significant or
frequent codes that emerged from our data [84].
4 RESULTS
In this section, we discuss the state of the sharing economy in computing and in HCI specifically.
In other words, we address our first research question, i.e. What has been done? This section
introduces our results with respect to our first question in three sections. In the first two sections—
one dedicated to the broader computing literature and the other dedicated to HCI—we present
high-level descriptive statistics on the publication rate, geographic focus, research questions and
methodologies employed. The third section contains an in-depth discussion of some of the major
4 A list of these papers can be found at the following URL: http://tinyurl.com/yd6u39vj

5 A paper was coded as “design” when its central objective was the design or implementation of a prototype application or

system.
6 A paper was coded as “math modeling” when it used a simulation or modeling to test the research objective.
7 A summary of the codes is included in Appendix B.

Proc. ACM Hum.-Comput. Interact., Vol. 1, No. 2, Article 38. Publication date: November 2017.

PACM on Human-Computer Interaction, Vol. 1, No. CSCW, Article 38. Publication date: November 2017.

38:6

T. Dillahunt et al.

Fig. 1. Publication counts in ACM DL as HCI and Non-HCI, and all venues from 2010 to 2016. Our corpora
encapsulates all papers up to July 2017, but 2017 is not shown here because a full year of publication results
was not available.

trends identified in both the broader computing literature and in HCI. The final section provides a
summary of themes that were under-explored.
4.1 Descriptive Statistics: Computing Literature
The papers in our corpus represent 47 distinct publication venues, including full conference proceedings, conference companion proceedings, and some refereed journals. The most common
venues are CHI (N=14), CSCW (N=13), CHI Extended Abstracts (N=10) and SIGSPATIAL (N=7). An
additional 28 venues appear only once such as ACM GROUP, TOCHI, and WWW. Though IEEE
publications are not ACM venues, one IEEE paper ([78]) was included in our final corpus because
it was published in IEEE and Automated Software Engineering, a joint ACM venue.
As shown by Figure 1, research in computing as it relates to the sharing economy grew rapidly
from 2011 to 2015. This resonates with our understanding of the birth of the concept of a sharing
economy, marked by Botsman and Rogers’ early work [14]. However, the publication count declined
from 2015 to 2016.
Seventy-six articles specified a country in which the study was conducted and/or from which
data were drawn. Out of the 76 articles, the United States was the most common study site (N=32).
China (N=8) and Finland (N=7) were the next two most frequent countries where studies took
place.
4.1.1 Research Methodologies and Questions. Per Figure 2, in the ACM DL, most published
studies used either quantitative (N=44) or qualitative (N=43) methods. Math modeling (N=25),
design (N=25), and mixed methods (N=14) are also commonly used. One literature review (N=1)
also appeared and this was a short paper by Oh and Moon [74] calling for a shared definition of the
Proc. ACM Hum.-Comput. Interact., Vol. 1, No. 2, Article 38. Publication date: November 2017.

PACM on Human-Computer Interaction, Vol. 1, No. CSCW, Article 38. Publication date: November 2017.

The Sharing Economy in Computing

38:7

sharing economy. Figure 3 shows that a large majority of the ACM computing studies addressed
descriptive research questions (N=73). Very few studies were causal (N=8) or predictive (N=9) in
nature.

Fig. 2. Research methods distribution in ACM (separated into HCI and Non-HCI Computing)

4.2 Descriptive Statistics: HCI Literature
To understand the HCI contributions to the sharing economy in the computing community, we
coded the publication venues into HCI Computing (N=56, 50%) and Non-HCI Computing (N=56,
50%). In the next section, we discuss general HCI trends within the broader context of the ACM.
As shown in Figure 1, HCI research as it relates to the sharing economy started in 2011 and
began growing rapidly starting in 2013. However, publication count declined from 2015 to 2016.
Non-HCI computing research has seen a steady increase since 2011.
In terms of geography, 46 study sites were specified within the HCI papers. Of the 46 sites, the
most common country was the United States (N=20). The remaining 26 sites were in Finland (N=5),
Germany (N=4), Australia and India (each N=3), the UK and Singapore (each N=2), and Austria,
Indonesia, Italy, Kenya, Namibia, South Korea, and Taiwan (each N=1). China did not appear in the
list of study sites considered in the HCI sharing economy literature.
4.2.1 Research Methodologies and Questions. Per Figure 2, in HCI studies, most published studies
used qualitative (N=38) methods. Eight (N=8) used quantitative methods and ten (N=10) used mixed
methods to address their research questions. Fifteen (N=15) papers employed design, deploying a
prototype system that was generally paired with a user study.
The vast majority of HCI computing studies addressed descriptive research questions (N=54),
with only two addressing other types of questions (Figure 3).
4.3 Major Topical Themes in Computing and HCI
Table 1 summarizes the results of our hybrid coding for themes in the sharing economy literature
and Appendix B contains a complete listing of these results. In the overall literature, the most
prominent themes in the literature are: (1) optimization (which is a theme almost exclusively in nonHCI articles) (2) socio-technical design of these platforms such as platform governance, entry barriers,
and how specific features are used; and (3) understanding why individuals have been motivated
to participate. Within the HCI literature specifically, the top three themes are: (1) socio-technical
Proc. ACM Hum.-Comput. Interact., Vol. 1, No. 2, Article 38. Publication date: November 2017.

PACM on Human-Computer Interaction, Vol. 1, No. CSCW, Article 38. Publication date: November 2017.

38:8

T. Dillahunt et al.

Fig. 3. Research questions distribution

Venue

HCI
(N=56)

Non-HCI
(N=56)

Theme

Count Salient Examples

Socio-technical design

34 Lampinen, 2014 [57]

Motivation

26 Bellotti et al., 2015 [8]

Social relationship/sense of community

25 Ganglbauer et al., 2014 [39]

Working conditions

15 Ahmed et al., 2016 [4]

Special populations

13 Dillahunt & Malone, 2015 [30]

User experience

12 Raval & Dourish, 2016 [83]

Cost & benefit to society

10 Lee et al., 2015 [61]

Trust

10 McLachlan et al., 2016 [69]

Business/economic/pricing model

9 Ikkala & Lampinen, 2015 [49]

Optimization

38 Etienne and Latifa, 2014 [34]

Geography

25 Dwarakanath et al., 2016 [33]

Business/economic/pricing model

19 Bistaffa et al., 2015 [10]

Motivation

8 Kooti et al., 2017 [56]

Privacy

7 Xu et al., 2017 [101]

Cost & benefit to society

6 Quattrone et al., 2016 [80]

Table 1. HCI and non-HCI venues focus on a different set of themes. Please see Appendix B for the full set of
themes and their descriptions.

design of these platforms; (2) motivation; and (3) social relationships between platform participants
and sense of community. In addition to optimization, the other two key non-HCI contributions
include geography, which occurs at the same frequency as social relationships/sense of community,
and business/economic/pricing models (see Appendix B for a complete listing of our final codes).
Proc. ACM Hum.-Comput. Interact., Vol. 1, No. 2, Article 38. Publication date: November 2017.

PACM on Human-Computer Interaction, Vol. 1, No. CSCW, Article 38. Publication date: November 2017.

The Sharing Economy in Computing

38:9

The next subsections provide a brief summary of the research in these six themes—the most
prominent themes in the HCI and non-HCI literatures—and a description of some salient papers
contributing to these themes.
4.3.1 Optimization. While almost non-existent in HCI (N=2), sharing economy optimization
work is quite common in non-HCI computing venues (N=38). Research related to optimization
investigated ways to maximize the utility and efficiency of the various systems and platforms used
in the sharing economy ecosystem. The majority of optimization papers proposed and evaluated
algorithms to improve the matching or task assignment in the context of ridesharing (N=17) or
spatial/mobile crowdsourcing systems (N=14). In papers concerned with ridesharing, researchers
proposed new approaches to improve upon the current matching and path planning algorithms (e.g.,
[21, 41, 47, 66]). Many of the papers on mobile or situated crowdsourcing defined new utility models
for task assignment, and proposed various algorithms to best solve those problems, evaluating their
designs on synthetic data and public datasets from major metropolitan areas such as New York
[22], Los Angeles [27], Tokyo [54], and Shanghai [97]. There is also research that uses past data
to provide optimized ridesharing recommendations for users [45] and suggests ways to optimize
ridesharing payments to increase fairness among riders [10].
4.3.2 Socio-Technical Design. Papers that are related to the socio-technical design of sharing
economy platforms predominantly appear in HCI venues (N=34). These researchers studied and
evaluated how specific features/designs are used, or suggested features/design to better enhance
user motivation, reduce entry barriers, and regulate user behavior in sharing economy services.
For example, Gheitasy et al. evaluated features on Etsy and identified a socio-technical gap
(which is defined as the divide between what must be supported socially and what can be supported
technically) in features such as customers’ reviews, rating systems and social presence tools [40].
Dillahunt and Malone described design solutions for some of the trust and safety issues among
people in disadvantaged communities, including the importance of meeting in safe spaces, twoway background checks, the need for understanding neighborhood makeup and cohesiveness,
and the value of referrals [30]. Many researchers investigated the challenges of onboarding users
or sustaining users, often through exploratory studies employing qualitative methodologies. A
common assertion among these studies was that for a platform to be sustainable it first needs to
attract a critical mass of users (the standard “cold start problem” in social computing) [29, 42, 88, 89].
In one group of studies the researchers investigated ways users adapted platform features to
meet their own needs. For example, Lampinen [57] examined account sharing in the context of
Couchsurfing. Her results revealed challenges for multi-person households that engage in account
sharing, such as presenting multiple people in one profile and coordinating negotiations over access
to shared space. The work called for system designers to monitor the obscure and non-popular use
cases in their platforms.
Note that the papers coded for socio-technical design often overlapped with the papers coded for
motivation or for social relationships, demonstrating the close connection between understanding
users and design implications in the HCI literature.
4.3.3 Motivation. One central question researchers have attempted to answer is why people
participate in the sharing economy. For example, through interviewing both users and providers of
46 different sharing economy systems, Bellotti et al. identified eight distinct motivations for the
use of sharing economy services—value/morality, social influence, status/power, empathy/altruism,
social connection, intrinsic/autotelic reasons, safety, and instrumental motivations [8]. Liao et al.
proposed the Theory of Planned Behavior as a model for studying user behavior in the sharing
Proc. ACM Hum.-Comput. Interact., Vol. 1, No. 2, Article 38. Publication date: November 2017.

PACM on Human-Computer Interaction, Vol. 1, No. CSCW, Article 38. Publication date: November 2017.

38:10

T. Dillahunt et al.

economy [64]; this theory frames decisions as influenced by a user’s attitude toward the behavior,
perceived social norms related to the behavior, and perceived behavioral control [5].
Researchers have identified a tension between instrumental motivations versus idealistic/altruistic
motivations [8, 86]. For example, Shih et al. found that highly active timebank users were more
idealistic and participated because they believed in “equal time, equal value,” whereas less active
timebank users, who were mostly regular members, more frequently utilized timebank service
exchanges in order to fulfill instrumental needs [86]. The same tension sometimes exists between
system providers and users: providers tend to place great emphasis on idealistic motivations; users,
on the other hand are often looking for services that provide what they need [8].
In addition to examining what motivates people to participate in the sharing economy, some
researchers investigated what demotivates people. For example, Meurer et al. found that independence
and decisional autonomy are viewed as constraints for older adults to utilize ridesharing services
[71]. Dillahunt and Malone showed that distrust and safety concerns are obstacles to adopting
sharing economy among disadvantaged communities [30]. Similarly, in studying P2P exchange
systems, Sun et al. found that trust concerns about sharing objects and the potential risks of
entrusting a possession to someone else have hindered the adoption of these systems [89].
4.3.4 Social Relationships & Sense of Community. As noted in the motivation section, social
connections play an important role in motivating people to participate in the sharing economy.
However, social relationship and sense of community is distinct from motivation because it considers
aspects of interaction that extend beyond a single user. The papers about social relationships and
community examine how pairs, groups, or communities interact with sharing economy platforms.
For example, Ganglbauer et al. studied a food-sharing Facebook group to understand online social
media’s role in the emergence and sustainability of such a community [39]. In doing so, Ganglbauer
et al. analyzed the interactions between community members and found pro-active appeals and
critical awareness of community members. Mirisaee et al. studied the “social fabric” of ridersharing,
which they defined as “[the] composite of both the physical and virtual sharing infrastructures
(social networking groups, community email lists, sports clubs, local school events etc.) and the
networks of relations formed within and between them” [72, p.451]. Works by Lampinen et. al [59]
and Suhonen et. al [88] on Kassi, a local online gift exchange system, showed that the use of stable
online identities in a geographically local context helped build a sense of community and trust that
was hard to achieve in large-scale anonymous social exchange systems.
4.3.5 Geography. Geography was a very common theme in papers focusing on physical or
mobile crowdsourcing, and overlapped heavily with the theme of optimization. Non-HCI papers
with the geography code (N=25) were largely focused on spatial variables in ridesharing and
crowdsourcing systems. Many papers described spatial or mobile crowdsourcing as an “emerging
technology” and were devoted to problems within the domain of task assignment or user matching,
contributing algorithmic approaches that outperformed existing solutions on various synthetic
and real datasets. These papers introduced previously ignored variables to maximize the number
of successful assignments, reduce the number of workers needed, or improve performance in
circumstances of high uncertainty or limited workers.
The majority of the geography papers in HCI venues (N=9), however, involved field deployments
of mobile crowdsourcing applications and employed user studies to evaluate the system and extract
design implications. These deployments were local, frequently within a single community, and
consistently found that the sense of community and relationship between users was essential
to the platform’s success. These findings align with those of another study, which investigated
perceptions of a hypothetical local favor-exchange platform in a small town in Italy, in which
the most salient finding was “the importance of the relationship between participants” [50]. The
Proc. ACM Hum.-Comput. Interact., Vol. 1, No. 2, Article 38. Publication date: November 2017.

PACM on Human-Computer Interaction, Vol. 1, No. CSCW, Article 38. Publication date: November 2017.

The Sharing Economy in Computing

38:11

remaining HCI papers investigated the impact of geographic factors in mainstream platforms and
found that socioeconomic differences across neighborhoods and regions were strongly connected
to differences in participation and success [95, 96].
4.3.6 Business, Economic, and Pricing Models. The “business/economic/pricing model” theme
was present in papers from both non-HCI (N=19) and HCI (N=9) venues. In non-HCI computing
venues, researchers directly studied the existing sharing economy platforms and the models these
platforms incorporated. For example, researchers used large-scale data to analyze Uber’s pricing and
matching models [56]. Researchers also suggested alternative pricing schemes for sharing economy
platforms, such as dynamic pricing models based on real-time supply and demand [7] or biddingbased models that reallocate some pricing control to the consumer [21]. Papers about business
models discussed the viability of specific products for the sharing economy [19] or investigated how
business models may influence the priorities or the governance of the platforms [9]. This theme
also overlapped significantly with the optimization theme (N=12). Many of the papers introduced
different pricing models that maximized the revenue, social welfare, and quality of work of sharing
platforms [35, 102].
In contrast, HCI researchers tended to explore the social implications or social dynamics related
to business, economic or pricing models. For example, Ikkala and Lampinen [49] found that the
monetary-based model of Airbnb gives hosts more control compared to other non-monetary-based
hospitality services: the hosts can select the guests consistent with their preference and have control
over the volume and type of demand. In their 2014 paper, Ikkala and Lampinen studied how the
social and economic factors get intertwined in this context of Airbnb and how hosts divert their
accumulated reputational capital into the rental price [48].
4.4 Underexplored Themes in ACM
Our results suggest that the three least-explored sharing economy themes in the ACM research
were 1) topics related to the pre-sharing economy, or the sharing of under-used assets before the
rise of the sharing economy (e.g., carpooling, rickshaws, and timeshares); 2) safety; and 3) special
contexts of sharing (e.g., shared space, couches, etc.). In the HCI research, the least-explored themes
included optimization, sustainability or environmental effects, pre-sharing economy, and special
sharing contexts. Outside of HCI, the least-explored topics were special populations (N=0) and
algorithmic auditing, participant diversity, pre-sharing economy, safety, and sustainability (all N=2).
While this list suggests implications for future work, it is unclear why these topics were the
least explored. Perhaps these topics are not as relevant to their specific sub-field. For example,
optimization as an unexplored topic within HCI is reasonable given the number of optimization
papers in non-HCI-related fields. It is possible that algorithmic auditing papers are published outside
the ACM. These are all points that we revisit in the next section.
5 IMPLICATIONS FOR COMPUTING AND HCI RESEARCH
Our findings show key trends in the literature on the sharing economy in computing and HCI
specifically. For example, for computing overall, we saw a steady increase in sharing-economy
papers from 2009 to 2015 and a decrease from 2015 to 2016; this decrease represents a drop in HCIrelated research particularly, despite a steady increase in non-HCI-related work over time. We found
that overall, there were an equal number of HCI and non-HCI papers and an equal representation
of qualitative and quantitative methods. Few papers used mixed-methods approaches and many of
these were from HCI. There was only one literature review on this topic [74]. An overwhelming
majority of research questions were descriptive in nature and were primarily from HCI; causal and
Proc. ACM Hum.-Comput. Interact., Vol. 1, No. 2, Article 38. Publication date: November 2017.

PACM on Human-Computer Interaction, Vol. 1, No. CSCW, Article 38. Publication date: November 2017.

38:12

T. Dillahunt et al.

predictive research questions were few in number. Finally, our results show that 42% (N=32) of the
works specifying a location (N=76), were from the United States.
In this section, we draw on these results to address our second research question, i.e., What
should we do next? In other words, this section highlights the under-explored topic areas identified
in our results to derive key directions for future sharing economy work in computing and HCI.
5.1 Environmental Sustainability and Concerns
Broadly, environmental sustainability, a well-studied topic in HCI (e.g., [32, 38]), was not well
represented in our results. In general, the papers in our corpus presented a physical-crowdsourcing
application to report environmental concerns such as water and air quality issues [55] and food
sharing applications to reduce domestic food waste [36]. A paper from Pargman et al., identified in
our review, noted that the sharing economy offers a potentially beneficial solution in a resourcescarce future [77]. Outside of computing, Cheng identified sustainability and development as one
of three main focus areas across the literature in the sharing economy that receives little attention
[20]. It was also noted that while environmental savings from shared mobility may exist [23],
there is a dearth of studies that actually confirm that these savings exist (despite most sharing
economy platforms’ advertising supposed environmental benefits). More work is needed to address
sustainability and the sharing economy, a point that has also been suggested by Silberman et al. in
their discussion of sustainable HCI [87].
5.2 Engaging with Pre-sharing Economy Phenomena
One purpose of the sharing economy is to bridge the online and offline worlds by connecting
individuals who need goods or services, to those who have access to these goods and services
[11, 14] via technology. Although the sharing economy has rapidly become a prominent subject
across many disciplines including computing, business, policy, and law [74], the underlying notion
of sharing is not a new concept. Despite this, our results suggest that very few papers discuss
sharing prior to the rise of the sharing economy. There are some exceptions: one paper from
Kasera et al. [51] conducted an exploratory study of shared taxis in Namibia to understand how
successful ridesharing is achieved without digital technology. Similarly, Carroll and Bellotti [18]
conceptually traced the development of bartering and gift exchange by studying literature in history
and anthropology. These studies benefit the field by informing the design of sharing economy
applications.
The need to consider the precursors to modern sharing economy platforms is particularly
important as the sharing economy enters new domains. For instance, Cheng’s findings suggest
an emergence in food sharing and land sharing in urban environments [20]. Land sharing and
food sharing have extraordinarily long precedents in human history (e.g., [1, 2]), complete with
many positive (e.g., [1]) and negative examples (e.g., [2]). An important direction for future work is
examining the prior research on these historical sharing economy platforms to develop implications
for the design of computer-mediated sharing tools in these domains.
5.3 More Diverse Geographic Contexts
Our results related to the geographic distribution of study sites—combined with very recent work
by Thebault-Spieker et al. [96]—point to a clear and important direction for future sharing economy
research. In particular, our study site results show a clear bias toward the United States in the HCI
sharing economy literature. While it is not uncommon in the computing literature for there to be
geographic biases in study site selection, the work of Thebault-Spieker et al. suggests that this should
be a particularly serious issue for sharing economy research. More specifically, Thebault-Spieker et
al. showed that local geographic factors ranging from population density patterns to urban structure
Proc. ACM Hum.-Comput. Interact., Vol. 1, No. 2, Article 38. Publication date: November 2017.

PACM on Human-Computer Interaction, Vol. 1, No. CSCW, Article 38. Publication date: November 2017.

The Sharing Economy in Computing

38:13

to community mental maps have major effects on many of the phenomena of interest in the sharing
economy literature (e.g. user motivation, optimization of important properties; see Table 1). Because
these local geographic factors vary from city to city and from country to country (e.g., Chinese
urban structures are very different from those in the United States and those in sub-Saharan Africa
[15], there is a strong probability that many of the findings in our paper corpus would change if
studies were repeated in new geographic contexts. Exploring the nature of these changes—and
better explicating the relationship between local geography and variables of interest—should be a
high priority in future research.
Additionally, on a much more specific note that was also reflected in Cheng [20], our results
point to the glaring need to do much more HCI sharing economy research in China: no HCI papers
considered Chinese study sites, despite China having an enormous sharing economy ecosystem
consisting of unique platforms that do not exist in Western countries. As such, important contributions can likely be made in the near-term by simply re-examining several influential HCI sharing
economy papers in a Chinese context using Chinese platforms.
As is typical in the computing literature, more attention should also be paid to the sharing
economy in developing countries. While a minority of work occurred in countries like Namibia
and Kenya, the sharing economy is known to play a different role in developing countries than
developed ones (e.g., [4, 43, 51]). A similar approach to what we have recommended for China
could likely yield important near-term contributions.
Finally, the work of Thebault-Spieker et al. [95, 96] discussed how local geographic factors are
not only critically important determinants of the performance of sharing economy platforms, but
also that they can cause geographic biases that benefit certain demographics. However, as suggested
by Thebault-Spieker et al., this result needs exploration in diverse geographic contexts with a
wide range of demographic biases and organizations of the built environment. There are many
immediate opportunities for research here, as well.

5.4 Pro-Social Objective Functions
Our results highlight a specific and important arbitrage opportunity between the more qualitative
and descriptive HCI sharing economy literature and the optimization work that is predominately
being done outside HCI: quantifying and optimizing sharing economy properties that are not currently the priority of the optimization literature. In other words, our results suggest an opportunity
for doing human-centered optimization in the sharing economy.
For instance, a relatively straightforward human-centered extension of the optimization literature
would involve attempting to increase decisional autonomy of workers and consumers (as was found
to be important by Meurer et al. [71]) while minimizing other costs (e.g., prices, reduced availability).
Over the longer term, however, our results suggest that there is a large need for research that
takes a much broader human-centered view of optimization in the sharing economy. For instance,
networks and platforms could be optimized for social tie-building over time (as was studied by
Mirisaee et al. [72], for accruing trust and safety in disadvantaged communities (c.f. Dillahunt and
Malone [28]), or for minimizing the socio-technical gap (c.f. Gheitasy et al. [40]). Another issue
worthy of study at the nexus of HCI and optimization relates to this question: “How optimized is
too optimized?”. There is a long history of HCI literature on the long-term costs of maximizing
short-term human performance. A similar phenomenon is plausible for many sharing economy
platforms. This is perhaps an especially large concern given the “emotional labor” (i.e. attending to
the social and emotional needs of customers) demanded of workers in the sharing economy [83], a
concern that did not arise in Cheng’s study [20].
Proc. ACM Hum.-Comput. Interact., Vol. 1, No. 2, Article 38. Publication date: November 2017.

PACM on Human-Computer Interaction, Vol. 1, No. CSCW, Article 38. Publication date: November 2017.

38:14

T. Dillahunt et al.

5.5 More Implications for Policy
Although several papers were included in the topic theme government and policy (e.g., [67, 68, 92]),
only a small number of empirical studies in this group of papers provided direct implications
for policy. The few studies that did so include the work of Lecuyer et al. [60], who provided a
method for improving transparency and extracting detailed data that are otherwise hidden, such as
a comprehensive transaction history and estimated revenue of Airbnb hosts. In this quantitative
analysis, the authors concluded that advocating a policy enforcing a 90-day maximum of Airbnb
rentals per year would eliminate the majority of concerns surrounding illegal hotels [60]. Similarly,
in a qualitative analysis, Dillahunt et al. [29] uncovered barriers to ridesharing applications that
can be used to inform policies for ridesharing subsidies for transportation-scarce individuals from
low-socioeconomic areas.
Given the importance of policy in the sharing economy domain, the small number of papers
focused on implications for policy in our corpus highlights the immediate need for more research
in this direction. Indeed, Cheng identified a similar problem in his review of the non-computing
literature [20]. More generally, our results back recent calls for more policy work in HCI more
broadly (e.g., [46, 52]). One approach to addressing these calls in the sharing economy domain
would be to work to implement fair wages across sharing and gig economy platforms as suggested
by the contributors of Meatspace Press [70], a new project concerned with important issues of
technology and society for people of diverse backgrounds.
5.6 More Diverse HCI Approaches are Needed
A key takeaway from our results is that the majority of HCI research on the sharing economy
is qualitative and descriptive in nature. Given the societal import of the sharing economy, it is a
credit to qualitative researchers in the HCI community that they have so quickly established major
lines of research in this domain. This should clearly continue. However, our results highlight that
the important perspectives provided by the quantitative and system-building traditions of HCI are
incomplete in the sharing economy literature. Future sharing economy work in HCI should seek to
bolster these perspectives.
5.7 Is HCI Losing Interest?
Finally, our results show a small decrease in sharing economy papers in 2016 relative to 2015, driven
primarily by a decline in HCI sharing economy papers. This negative slope surprised us, and it
is unclear whether it is a temporary reduction of interest or whether HCI interest in the sharing
economy has peaked. Given the number of important directions for future HCI work outlined in this
section— and the many others that can likely be drawn from our results—we hope that the former
is the case rather than the latter. As has been highlighted by our results, the HCI community has a
distinct perspective, and our belief is that this perspective should remain strong in the computing
literature.
6 LIMITATIONS
Literature reviews on ACM publications around the sharing economy are subject to a number of
limitations. First, the ACM Digital Library’s search engine has its own set of limitations [85]. For
example, the search engine at times generated inconsistent results despite researchers using the
same search terms and date ranges. To minimize this limitation, several team members confirmed
consistency among the final search results.
In addition, the articles in our review were limited to papers written in English, and papers
published in other languages might exhibit different trends. Next, although we went further than
Proc. ACM Hum.-Comput. Interact., Vol. 1, No. 2, Article 38. Publication date: November 2017.

PACM on Human-Computer Interaction, Vol. 1, No. CSCW, Article 38. Publication date: November 2017.

The Sharing Economy in Computing

38:15

most computing SLRs by considering the entire ACM DL rather than just a subset and although
ACM DL claims to be the most comprehensive digital library in computing, the ACM DL does
not contain all possible relevant articles. Our review does not include articles from the Institute
of Electrical and Electronics Engineers (IEEE) (aside from one joint ACM/IEEE venue) or the
Association for the Advancement of Artificial Intelligence (AAAI), for instance. That said, the
exclusive use of the ACM Digital Library is common in prior early-stage reviews (e.g., [85]). To
minimize this limitation, we considered our results in the context of a separate review of 66 sharing
economy journal articles by Cheng [20].
7 FUTURE WORK AND CONCLUSION
This research highlights a few opportunities for further reviews of the sharing economy literature,
for instance expanding our literature review beyond ACM venues and performing co-citation
analysis (c.f. Cheng [20]). Such a citation analysis would, for instance, identify which of computing’s
works bridge to other fields as well as identify opportunities to bridge clusters of research. Although
this would be a very substantial endeavor, there is some ongoing research to make this process less
intensive [99].
To conclude, we have provided the results of a systematic review of 112 sharing economy papers
in the computing literature, thereby filling an important gap left by the only other major sharing
economy literature review [20]. Our review reveals important trends in the computing community’s
sharing economy research and those of our focus sub-community, human–computer interaction.
These trends include a predominance of descriptive work and a tendency for the HCI community
to use qualitative rather than quantitative methods. These results inform the presentation of a
number of short- and long-term opportunities for new sharing economy research directions in
computing and HCI, for instance expanding the geographic range of current research, focusing on
environmental effects, and combining the strengths of the HCI and non-HCI literature.
ACKNOWLEDGMENTS
The authors would like to thank Shevon Desai, Michigan Interactive and Social Computing (MISC)
members, University of Minnesota GroupLens Lab members, and our reviewers for providing us
with very valuable feedback. University of Michigan researchers were partially supported by the
National Science Foundation (IIS-1352915). University of Minnesota researchers were supported
by the National Science Foundation (CRII-1566149). Northwestern University researchers were
supported by the National Science Foundation (IIS-1707296) and a Microsoft FUSE Research Award.
A APPENDIX A: SYSTEMATIC LITERATURE REVIEW
We compare and contrast HCI’s contributions to the broader ACM sharing economy contributions.
As the first step in the systematic literature review, we identified a set of search terms. We then
collected and analyzed data derived from those terms. We describe the process in this appendix.
A.1 Identifying Search Terms
Our goal was to identify a set of search terms that had been used in HCI and in well-known and
cited monographs in the sharing economy literature [14, 90]. We confirmed our decision based on
Botsman’s model of the collaborative economy where Collaborative Finance and Collaborative Education are not associated with sharing and peer economies [11]. Collaborative Consumption consists
of the sharing economy, which consists of peer-to-peer exchanges per this model [11]. Therefore,
we identified our three initial search terms (i.e., sharing economy, collaborative consumption,
peer-to-peer exchange), which we define in the first subsection.
Proc. ACM Hum.-Comput. Interact., Vol. 1, No. 2, Article 38. Publication date: November 2017.

PACM on Human-Computer Interaction, Vol. 1, No. CSCW, Article 38. Publication date: November 2017.

38:16

T. Dillahunt et al.

In CSCW and HCI, the sharing economy—particularly as it relates to utilizing assets and matching “needs” with “haves”—has also corresponded with the phrases “gig economy” and “physical
crowdsourcing.” As a result, we also included these terms in our initial search and we define them
in the second subsection.
A.1.1 Sharing Economy. Historically, there has been no consensus on a definition of the sharing
economy. However, Botsman and Rogers first defined the broader term collaborative consumption
in the book What’s mine is yours [14] and Botsman is one of the most frequently cited authors for
the term—hence, we leverage her terminology to identify initial search terms for our literature
review. She defined the sharing economy as “an economic system based on sharing underused
assets or services, for free or for a fee, directly from individuals” [11]. In a RSA Replay video from
2016, “The State of the Sharing Economy,” Botsman redefined the term as “an economic system
that unlocks the value of underused assets through platforms that match ‘needs’ with ‘haves’ in
ways that create greater efficiency and access” [13, 12:22]. In her opinion, the sharing economy is a
subset of collaborative consumption and is focused on peer-to-peer exchange.
Collaborative Consumption: Collaborative consumption maximizes the use of assets through
efficient models of shared access and redistribution [12]. It is considered to be the reinvention of
conventional market behaviors such as sharing (Airbnb, Couchsurfing), lending (Zipcar, Chegg),
renting (Getable, Liquidspace), bartering and swapping (Yerdle, TradeYa), and gifting (Skillshare),
made possible at a large scale through the Internet and digital technologies [11].
Peer-to-Peer Exchange: In peer-to-peer (P2P) exchange (e.g., Lyft, Airbnb), inventory and assets are
owned and exchanged directly to and from individuals. This model is also known as a decentralized
model. Marketplaces that facilitate this type of sharing and exchange are known as peer economies,
and these economies are built on trust between and among peers. According to Botsman, the
sharing economy is primarily focused on peer-to-peer exchange; however, as discussed in this
paper, this is not entirely the case.
A.1.2 Gig Economy. We refer to Sundararajan’s [90] definition of the gig economy because this
term is not defined in Botsman and Rogers’ monograph [14]. Sundararajan provides a more capitalist
perspective on the sharing economy, and he adamantly asserts the inclusion of the gig economy
within its scope. Within this context, the gig economy refers to the service-related employment
opportunities that include physical tasks such as cooking, driving, cleaning, and handiwork (e.g.,
TaskRabbit). The gig economy also refers to the service-related employment opportunities that
include online tasks (e.g., Upwork). Instead of having an ongoing relationship with an employer,
independent workers take on a series of temporary gigs that are mediated via an online platform
[31].
A.1.3 Physical Crowdsourcing. The term physical crowdsourcing has been used to describe the
engagement of crowds in taking on actions in physical spaces, beyond the structure of traditional
crowdsourcing. Whereas online crowdsourcing tasks utilize the wisdom of the crowd, physical
crowdsourcing utilizes the crowd’s diverse skills and contexts to allocate convenient or appropriate
tasks to individual members. Physical crowdsourcing may also make use of large groups of people to
complete or help to complete tasks in the physical world [94], either for free or for a fee. One example
of a physical crowdsourcing application is Google Waze, a system that relies on the community to
provide detailed information such as police sightings and traffic jams. The community members
provide this information freely, which assists others in navigating to their destination in a timely
and more efficient way than using a traditional navigation system. Another example of physical
crowdsourcing example is FixtheCity, an application that allows citizens to help maintain their
Proc. ACM Hum.-Comput. Interact., Vol. 1, No. 2, Article 38. Publication date: November 2017.

PACM on Human-Computer Interaction, Vol. 1, No. CSCW, Article 38. Publication date: November 2017.

The Sharing Economy in Computing

38:17

city by reporting problems such as potholes. Other platforms that utilize physical crowdsourcing
include Gigwalk and TaskRabbit.
A.2 Data Collection
We searched the ACM Digital Library for our review. The ACM Digital Library contains the full-text
collection of all ACM publications, including journals, conference proceedings, technical magazines,
newsletters and books; we used this digital library to conduct our primary search.
A.2.1 Search and Search Terms. To address our first research question, we conducted two rounds
of search, with our second search resulting in three additional search rounds to obtain additional
keywords:
Search 1: Collecting Sharing Economy Related Literature in the ACM
First, we searched the ACM Digital Library for: sharing economy, collaborative consumption, peerto-peer exchange, physical crowdsourcing, and the gig economy. We conducted an advanced search
using the default settings: “Where ‘any field’ ‘matches any’ of the following words or phrases”:
(“sharing economy” OR “collaborative consumption” OR “peer-to-peer exchange” OR “physical
crowdsourcing” OR “gig economy”).
This search led to 92 papers.
Search 2: Using Common Author-defined Keywords. Next, we extracted the author generated keywords from the papers generated from Search 1 and identified any keyword that occurred
twice or more. Filtering out the irrelevant keywords led to 11 new keywords, which we used as
seeds for a new round of searching in ACM. We repeated this process until no new seeds arose. The
second search led to 183 papers, and 5 new seeds for the next search round. The third search led to
169 papers, and 1 new seed for the next search round. The fourth and final search led to 4 papers,
all of which were duplicates from the previous searches. In sum, we identified 16 new seeds from
this iterative search, resulting in 262 new papers, excluding duplicates from our previous corpus.
We also eliminated those search terms resulting in an overwhelming number of responses (e.g.,
multi-agent systems).
Combining searches 1 and 2, the 21 search terms for the final ACM search included: “sharing
economy,” “collaborative consumption,” “peer-to-peer exchange,” “physical crowdsourcing,” “gig
economy,” “algorithmic management,” “collaborative economy,” “local online exchange,” “mobile
crowdsourcing,” “network hospitality,” “on-the-go crowdsourcing,” “platform economy,” “ridesharing,” “social exchange,” “surge pricing,” “timebanking,” “micro tasking,” “microtasking,” “situated
crowdsourcing,” “workplace studies,” and “spatial crowdsourcing.” Overall, these comprehensive
searches led to 354 papers, which constitute our full corpus.
A.2.2 Selection criteria. Next, we used specific selection criteria to screen all articles. To be
included in the review, articles had to be written in English, use the search terms in a way that
matched the previously defined definitions, and include the following variables of interest per [24,
p.36]: (1) a stated or implied problem or research question that was being addressed, (2) the central
purpose or focus of the study, (3) a brief statement about the sample population or subjects, and
(4) key results that related to the proposed study. Researchers extracted excerpts from each work
that answered these questions. In addition to including the list of authors, publication year, title,
the research questions, focus of the paper, sample used in research, sharing economy instances
provided, and how each paper defined the sharing economy, we extracted keywords and coded
the methodology employed as quantitative, qualitative or mixed methods, and coded publication
venue as HCI or non-HCI. We did not exclude short papers, extended workshop papers, panels, or
alt.chi. We then applied quality assessment criteria described in the next section to further filter
out papers that did not fit our research objective.
Proc. ACM Hum.-Comput. Interact., Vol. 1, No. 2, Article 38. Publication date: November 2017.

PACM on Human-Computer Interaction, Vol. 1, No. CSCW, Article 38. Publication date: November 2017.

38:18

T. Dillahunt et al.

A.2.3 Quality Assessment (QA). Inspired by Busalim and Che Hussin [17], we developed four
simple criteria to begin identifying the appropriate fit of each study. Systematic literature reviews
refer to this step as QA, though the criteria are not objective. For the purposes of this SLR, QA
served as a light mechanism to double-check the final corpus.
In this stage, three researchers read each paper and ranked each paper as high, medium or low on
the four criteria described below. Those criteria that ranked as high received a score, or a loading
factor, of 2, medium 1, and low 0 [73].
• QA1: Is the topic addressed in the paper related to the sharing economy, or aspects of the
sharing economy as outlined in the definition?
• QA2: Is the research methodology described in the paper?
• QA3: Is the data collection method described in the paper?
• QA4: Do the key findings align with the posed research questions?
We applied the four criteria to the 354 articles using the above scoring mechanism. For example,
if a study met a criterion fully, it received a loading score of 2. If the study partially filled the
criterion, it received a loading score of 1. Studies that did not meet the criterion received a 0 score
and papers receiving a 0 score for QA1 were removed immediately. The maximum score that a
study could receive was 8; we considered those studies scoring a 5 or more as high fit, 4 as medium
fit, and any score below a 4 as low fit. We chose the threshold of 5 because it implies that the study
either: (a) scored in all categories and scored high in at least one, or (b) scored in three categories
and scored high in at least two. A score of five was also safe enough for us not to prematurely
eliminate papers that may have been in question. After applying this filter, we were left with an
updated corpus of 119 papers.
Eleven papers were marked by at least one coder as “Accidentally made it through filters,”
either due to a paper’s apparent irrelevance to the sharing economy [100] or its appearance as
something other than research [25]. The flagged papers were reviewed in detail by the first and
last author to determine whether they should be removed from the final corpus; papers were kept
in cases where the faculty authors believed the paper was sufficiently relevant to the sharing
economy or sufficiently qualified as a research article. This acted as a final quality assessment (QA),
eliminating articles that were not meaningfully related to the sharing economy but made it through
the previous QA procedure due to high overall quality. Of the 11 identified articles, seven were
removed [6, 25, 37, 44, 82, 91, 100]. This left us with a final corpus of 112 papers that we assert to
be moderate to high in terms of fit to the sharing economy. These 112 papers are the subject of our
quantitative results. A visual summary of the data collection process is also shown in Figure 4.
A.3 Data Analysis
A.3.1 Coding of Papers. Coding of papers was beneficial in partially addressing both of our
research questions. We used the selection criteria to extract and summarize article contents as
attribute codes [75, 84] into a shared spreadsheet. This allowed us to develop a synopsis for each
work and to sort the literature according to publication year, publication venue, methodology used,
populations sampled, and instances or applications of the sharing economy studied (e.g., Airbnb,
Lyft). This specifically enabled us to address RQ1 by: showing publication rate over time [24],
specifying the publication venues that had been studied the most extensively, and identifying any
gaps between years in terms of the number of studies conducted.
We coded the remaining data from our spreadsheet, which included the research question, the
focus of the study and key findings, and how the paper defined the sharing economy. This allowed
us to address RQ2 by identifying the explored and under-explored areas of the sharing economy in
HCI.
Proc. ACM Hum.-Comput. Interact., Vol. 1, No. 2, Article 38. Publication date: November 2017.

PACM on Human-Computer Interaction, Vol. 1, No. CSCW, Article 38. Publication date: November 2017.

The Sharing Economy in Computing

38:19

Fig. 4. Flowchart of the data collection process

Our general approach was to take a hybrid-coding approach [98]. We leveraged existing frameworks [76] to create a priori codes. We also coded openly in our initial coding phase, which was
followed by focused coding. Focused coding allowed us to categorize significant or frequent codes
that emerged from our data [84].
A.3.2 Categorization of Study Focus and Key Study Themes. The study focus coding included two
phases: open coding and closed coding. In the first phase, authors five and six separately open-coded
the 68 remaining articles in the corpus based on the title, abstract, and extracted research question,
study focus, and findings. These authors then discussed the open codes together and organized
them into 22 broader themes. Authors one–four discussed these themes offline and raised open
questions to the larger group. In the second phase, authors three and four coded the articles based
on the 22 themes. Note that the themes are not mutually exclusive; one paper could belong to
multiple themes. The final results are shown in Table 1 and Appendix B.
A.3.3 Categorization of Research Questions. To categorize each article’s research questions, we
conducted a hybrid-coding approach where we first leveraged the three types of research questions
from social research methods: descriptive, relational, and causal [98].
(1) Descriptive: A study designed primarily to describe what is going on or what exists (e.g.,
public opinion polls).
(2) Relational: A study designed to look at the relationships between two or more variables (e.g.,
a public opinion poll comparing the opinions of males to females).
(3) Causal: A study designed to determine whether one or more variables causes or affects one
or more outcome variables.
We then openly coded research questions that did not easily fit into these categories and discussed these codes as a group to categorize the themes that emerged. For example, “prediction”
Proc. ACM Hum.-Comput. Interact., Vol. 1, No. 2, Article 38. Publication date: November 2017.

PACM on Human-Computer Interaction, Vol. 1, No. CSCW, Article 38. Publication date: November 2017.

38:20

T. Dillahunt et al.

was a new code to emerge based on some of the mathematical modeling papers that did not
fit into these three categories of research questions. Another new code to arise included algorithm/invention/optimization. This code emerged primarily from papers whose authors aimed
to invent new algorithms or optimize old ones to better match resource providers with resource
consumers.
A.3.4 Categorization of Publication Venue. We coded publication venues as HCI if the proceeding
or journal’s site stated that human interaction with computing systems was a primary interest of
the venue; these were predominately CHI and CSCW. Because the source of these papers was the
ACM Digital Library, we coded the remaining venues as Non-HCI Computing.
A.3.5 Other Categories. Finally, we identified other categories of information, such as the study
site by country and the distinct focus platform (i.e. sharing economy instance such as Uber or Lyft).
A.3.6 Coding Agreement. Two of the authors independently coded for agreement among the
research questions, research methodology, the sharing economy definition, and for the evaluation
of the quality assessment scores. They each independently coded a random sample of 30% of the
articles and then reviewed the coding of the other coder’s articles. This resulted in an inter-rater
reliability Cohen’s kappa value of .57 (moderate agreement), .81 (very good agreement), 1.0 (perfect
agreement), and .72 (substantial agreement) respectively.

Proc. ACM Hum.-Comput. Interact., Vol. 1, No. 2, Article 38. Publication date: November 2017.

PACM on Human-Computer Interaction, Vol. 1, No. CSCW, Article 38. Publication date: November 2017.

The Sharing Economy in Computing
B

38:21

APPENDIX B: HYBRID CODING THEMES AND COUNTS

Topic Themes

NonTotal HCI HCI Description

Issues related to adoption, such as reasons for adoption decision, diffusion process of
Adoption

14

8

6 the adoption among a population, scaling up, and localization.

Algorithmic
Auditing

9

7

2 Describes how algorithms can rule the sharing economy sites.

Business/economic/pricing
model

28

9

How the platforms create and distribute economic value, whether the platform is for
profit or not for profit, how to decide the price or other compensations for sharing
19 goods/services, and issues of liability of damage or excess wear-and-tear.

Cost & benefit to
society

16

10

6 Discuss the overall costs and benefits to society and groups.

Geography

34

9

25 features of the environment.

Government &
policy

11

6

5 societal implication.

Motivation

34

26

8 Reasons/costs/benefits to (not) participate in sharing economy systems.

Non-economic or
theoretical
framework

12

7

5 systems.

Issues related to geography, or human activities as it is affected by the physical
Relationship with local government, government regulation, policy implication and

Provide theoretical or statistical framework to better understand sharing economy

Optimization

40

2

How to optimize/maximize the important success metrics, such as platform
performance, user activity, system equity, system inclusion, system capacity and
38 matching efficiency.

Participant
diversity

7

5

2 Issues related to participant diversity.

Pre-sharing
economy

4

2

2 economy, such as carpooling, rickshaws, and timeshares.

Privacy

12

5

7 Privacy issues in sharing economy platforms.

Relationship to
traditional
industry

11

7

4 existing transportation systems.

Safety

6

4

2 Safety issues in sharing economy platforms.

Social
relationship/
sense of
community

28

25

3 Social relationships between participants on the platforms and sense of community.

Collaborative consumption of time or under-used assets before the rise of the sharing

How the rise of sharing economy affects traditional industry such as hotel industry or

Socio-technical
design

37

34

Issues related to socio-technical design of sharing economy platforms, such as
platform governance, entry barriers, member self-representation, co-option of features
3 and features designed to prevent abusive use.

Special
population

13

13

0 children, or people in developing world, use sharing economy systems.

Describes how special populations, such as elderly, disadvantaged, disabled,

Special sharing
context

6

3

Special sharing contexts, such as sharing shared resources (e.g., roommates co-list
their home on Couchsurfing/Airbnb), tiered ownership (excess capacity, penalty for
3 over-use; e.g. mobile broadband), and beyond job-to-job (e.g. passenger transfers).

Sustainability or
environmental
effects

6

4

2 ownership and sustainability-related pervasive computing.

Trust

14

10

4 reputation systems in the sharing economy.

User experience
Working
conditions

15

12

3 Issues about user experience such as social comfort and quality of service.

18

15

3 Focus on the service providers’ working conditions.

Issues related to sustainability or environmental effects, including effects on
How and why users trust the sharing economy platforms, particularly the role of

Proc. ACM Hum.-Comput. Interact., Vol. 1, No. 2, Article 38. Publication date: November 2017.

PACM on Human-Computer Interaction, Vol. 1, No. CSCW, Article 38. Publication date: November 2017.

38:22

T. Dillahunt et al.

REFERENCES
[1] 2017. Cooperative. (June 2017). https://en.wikipedia.org/wiki/Cooperative Accessed: 2017-07-11.
[2] 2017. Sharecropping. (June 2017). https://en.wikipedia.org/wiki/Sharecropping Accessed: 2017-07-11.
[3] ACM. 2017. ABOUT ACM PUBLICATIONS. (2017). http://www.acm.org/publications/about-publications Accessed:
2017-07-11.
[4] Syed Ishtiaque Ahmed, Nicola J. Bidwell, Himanshu Zade, Srihari H. Muralidhar, Anupama Dhareshwar, Baneen
Karachiwala, Cedrick N. Tandong, and Jacki O’Neill. 2016. Peer-to-peer in the Workplace: A View from the Road. In
Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems (CHI ’16). ACM, New York, NY, USA,
5063–5075. https://doi.org/10.1145/2858036.2858393
[5] Icek Ajzen. 1991. The theory of planned behavior. Organizational behavior and human decision processes 50, 2 (1991),
179–211.
[6] Rafael Ballagas, Therese E. Dugan, Glenda Revelle, Koichi Mori, Maria Sandberg, Janet Go, Emily Reardon, and Mirjana
Spasojevic. 2013. Electric Agents: Fostering Sibling Joint Media Engagement Through Interactive Television and
Augmented Reality. In Proceedings of the 2013 Conference on Computer Supported Cooperative Work (CSCW ’13). ACM,
New York, NY, USA, 225–236. https://doi.org/10.1145/2441776.2441803
[7] Siddhartha Banerjee, Ramesh Johari, and Carlos Riquelme. 2016. Dynamic Pricing in Ridesharing Platforms. SIGecom
Exch. 15, 1 (Sept. 2016), 65–70. https://doi.org/10.1145/2994501.2994505
[8] Victoria Bellotti, Alexander Ambard, Daniel Turner, Christina Gossmann, Kamila Demkova, and John M. Carroll. 2015.
A Muddle of Models of Motivation for Using Peer-to-Peer Economy Systems. In Proceedings of the 33rd Annual ACM
Conference on Human Factors in Computing Systems (CHI ’15). ACM, 1085–1094. https://doi.org/10.1145/2702123.2702272
[9] Saif Benjaafar, Guangwen Kong, and Xiang Li. 2015. Modeling and Analysis of Collaborative Consumption in Peer-toPeer Car Sharing. SIGMETRICS Perform. Eval. Rev. 43, 3 (Nov. 2015), 87–90. https://doi.org/10.1145/2847220.2847250
[10] Filippo Bistaffa, Alessandro Farinelli, Georgios Chalkiadakis, and Sarvapali D. Ramchurn. 2015. Recommending Fair
Payments for Large-Scale Social Ridesharing. In Proceedings of the 9th ACM Conference on Recommender Systems
(RecSys ’15). ACM, New York, NY, USA, 139–146. https://doi.org/10.1145/2792838.2800177
[11] Rachel Botsman. 2013. The sharing economy lacks a shared definition. (2013). https://www.fastcoexist.com/3022028/
the-sharing-economy-lacks-a-shared-definition
[12] Rachel Botsman. 2015.
Defining the Sharing Economy: What Is Collaborative Consumption–And
What Isn’t.
(2015).
https://www.fastcoexist.com/3046119/defining-the-sharing-economy-what-is-\
collaborative-consumption-and-what-isnt
[13] Rachel Botsman. 2016. RSA Replay: The State of the Sharing Economy. http://rachelbotsman.com/work/
the-state-of-the-sharing-economy/
[14] Rachel Botsman and Roo Rogers. 2010. What’s mine is yours: the rise of collaborative consumption. HarperCollins
Publisher. http://www.harpercollins.com/book/index.aspx?isbn=9780061963544
[15] Stanley D Brunn, Jack Williams, and Donald J Zeigler. 2003. Cities of the world: world regional urban development.
Rowman & Littlefield.
[16] Dimitrios Buhalis and Rob Law. 2008. Progress in information technology and tourism management: 20 years on and
10 years after the Internet-The state of eTourism research. Tourism management 29, 4 (2008), 609–623.
[17] Abdelsalam H Busalim and Ab Razak Che Hussin. 2016. Understanding social commerce: A systematic literature
review and directions for further research. International Journal of Information Management 36, 6 (2016), 1075–1088.
[18] John M. Carroll and Victoria Bellotti. 2015. Creating Value Together: The Emerging Design Space of Peer-to-Peer
Currency and Exchange. In Proceedings of the 18th ACM Conference on Computer Supported Cooperative Work & Social
Computing (CSCW ’15). ACM, New York, NY, USA, 1500–1510. https://doi.org/10.1145/2675133.2675270
[19] Le Chen, Alan Mislove, and Christo Wilson. 2015. Peeking Beneath the Hood of Uber. In Proceedings of the 2015 Internet
Measurement Conference (IMC ’15). ACM, New York, NY, USA, 495–508. https://doi.org/10.1145/2815675.2815681
[20] Mingming Cheng. 2016. Sharing economy: A review and agenda for future research. International Journal of Hospitality
Management 57 (2016), 60–70.
[21] Yinlam Chow and Jia Yuan Yu. 2015. Real-time Bidding Based Vehicle Sharing. In Proceedings of the 2015 International
Conference on Autonomous Agents and Multiagent Systems (AAMAS ’15). International Foundation for Autonomous
Agents and Multiagent Systems, Richland, SC, 1829–1830. http://dl.acm.org/citation.cfm?id=2772879.2773458
[22] Blerim Cici, Athina Markopoulou, and Nikolaos Laoutaris. 2016. SORS: a scalable online ridesharing system. In
Proceedings of the 9th ACM SIGSPATIAL International Workshop on Computational Transportation Science. ACM, 13–18.
[23] Boyd Cohen and Jan Kietzmann. 2014. Ride on! Mobility business models for the sharing economy. Organization &
Environment 27, 3 (2014), 279–296.
[24] John W. Creswell. 2008. Research Design: Qualitative, Quantitative, and Mixed Methods Approaches (3 ed.). Sage
Publications Ltd.

Proc. ACM Hum.-Comput. Interact., Vol. 1, No. 2, Article 38. Publication date: November 2017.

PACM on Human-Computer Interaction, Vol. 1, No. CSCW, Article 38. Publication date: November 2017.

The Sharing Economy in Computing

38:23

[25] Michael A. Cusumano. 2014. How Traditional Firms Must Compete in the Sharing Economy. Commun. ACM 58, 1
(Dec. 2014), 32–34. https://doi.org/10.1145/2688487
[26] Nicola Dell and Neha Kumar. 2016. The Ins and Outs of HCI for Development. In Proceedings of the 2016 CHI Conference
on Human Factors in Computing Systems (CHI ’16). ACM, New York, NY, USA, 2220–2232. https://doi.org/10.1145/
2858036.2858081
[27] Dingxiong Deng, Cyrus Shahabi, and Linhong Zhu. 2015. Task matching and scheduling for multiple workers in spatial
crowdsourcing. In Proceedings of the 23rd SIGSPATIAL International Conference on Advances in Geographic Information
Systems. ACM, 21.
[28] Tawanna Dillahunt, Airi Lampinen, Jacki O’Neill, Loren Terveen, and Cory Kendrick. 2016. Does the Sharing Economy
Do Any Good?. In Proceedings of the 19th ACM Conference on Computer Supported Cooperative Work and Social Computing
Companion (CSCW ’16 Companion). ACM, New York, NY, USA, 197–200. https://doi.org/10.1145/2818052.2893362
[29] Tawanna R Dillahunt, Vaishnav Kameswaran, Linfeng Li, and Tanya Rosenblat. 2017. Uncovering the Values and
Constraints of Real-time Ridesharing for Low-resource Populations. In Proceedings of the 2017 CHI Conference on
Human Factors in Computing Systems. ACM, 2757–2769.
[30] Tawanna R. Dillahunt and Amelia R. Malone. 2015. The Promise of the Sharing Economy Among Disadvantaged
Communities. In Proceedings of the 33rd Annual ACM Conference on Human Factors in Computing Systems (CHI ’15).
ACM, New York, NY, USA, 2285–2294. https://doi.org/10.1145/2702123.2702189
[31] Jane Dokko, Megan Mumford, and Diane W. Schanzenback. 2015. Workers and the Online Gig Economy. The Hamilton
Project: Advancing Opportunity, Prosperity, and Growth (December 2015), 1–8. https://www.brookings.edu/wp-content/
uploads/2016/07/workers_and_the_online_gig_economy.pdf
[32] Paul Dourish. 2010. HCI and Environmental Sustainability: The Politics of Design and the Design of Politics. In
Proceedings of the 8th ACM Conference on Designing Interactive Systems (DIS ’10). ACM, New York, NY, USA, 1–10.
https://doi.org/10.1145/1858171.1858173
[33] Anurag Dwarakanath, N. C. Shrikanth, Kumar Abhinav, and Alex Kass. 2016. Trustworthiness in Enterprise Crowdsourcing: A Taxonomy & Evidence from Data. In Proceedings of the 38th International Conference on Software Engineering
Companion (ICSE ’16). ACM, New York, NY, USA, 41–50. https://doi.org/10.1145/2889160.2889225
[34] Come Etienne and Oukhellou Latifa. 2014. Model-Based Count Series Clustering for Bike Sharing System Usage
Mining: A Case Study with the Velib System of Paris. ACM Trans. Intell. Syst. Technol. 5, 3 (July 2014), 39:1–39:21.
https://doi.org/10.1145/2560188
[35] Zhixuan Fang, Longbo Huang, and Adam Wierman. 2017. Prices and subsidies in the sharing economy. In Proceedings of
the 26th International Conference on World Wide Web. International World Wide Web Conferences Steering Committee,
53–62.
[36] Geremy Farr-Wharton, Jaz Hee-Jeong Choi, and Marcus Foth. 2014. Food Talks Back: Exploring the Role of Mobile
Applications in Reducing Domestic Food Wastage. In Proceedings of the 26th Australian Computer-Human Interaction
Conference on Designing Futures: The Future of Design (OzCHI ’14). ACM, New York, NY, USA, 352–361. https:
//doi.org/10.1145/2686612.2686665
[37] Qinyuan Feng, Ling Liu, and Yafei Dai. 2012. Vulnerabilities and Countermeasures in Context-aware Social Rating
Services. ACM Trans. Internet Technol. 11, 3 (Feb. 2012), 11:1–11:27. https://doi.org/10.1145/2078316.2078319
[38] Jon Froehlich, Leah Findlater, and James Landay. 2010. The Design of Eco-feedback Technology. In Proceedings of
the SIGCHI Conference on Human Factors in Computing Systems (CHI ’10). ACM, New York, NY, USA, 1999–2008.
https://doi.org/10.1145/1753326.1753629
[39] Eva Ganglbauer, Geraldine Fitzpatrick, Ozge Subasi, and Florian Guldenpfennig. 2014. Think Globally, Act Locally: A
Case Study of a Free Food Sharing Community and Social Networking. In Proceedings of the 17th ACM Conference
on Computer Supported Cooperative Work & Social Computing (CSCW ’14). ACM, New York, NY, USA, 911–921.
https://doi.org/10.1145/2531602.2531664
[40] Ali Gheitasy, Jose Abdelnour-Nocera, and Bonnie Nardi. 2015. Socio-technical Gaps in Online Collaborative Consumption (OCC): An Example of the Etsy Community. In Proceedings of the 33rd Annual International Conference on the
Design of Communication (SIGDOC ’15). ACM, New York, NY, USA, 35:1–35:9. https://doi.org/10.1145/2775441.2775458
[41] Preeti Goel, Lars Kulik, and Kotagiri Ramamohanarao. 2016. Privacy-Aware Dynamic Ride Sharing. ACM Trans. Spatial
Algorithms Syst. 2, 1 (March 2016), 4:1–4:41. https://doi.org/10.1145/2845080
[42] Antoni Guasch, Jaume Figueras, Pau Fonseca i Casas, Cristina Montañola-Sales, and Josep Casanovas-Garcia. 2014.
Simulation analysis of a dynamic ridesharing model. In Simulation Conference (WSC), 2014 Winter. IEEE, 1965–1976.
[43] Aakar Gupta, William Thies, Edward Cutrell, and Ravin Balakrishnan. 2012. mClerk: enabling mobile crowdsourcing in
developing regions. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems. ACM, 1843–1852.
[44] Oliver L. Haimson, Anne E. Bowser, Edward F. Melcer, and Elizabeth F. Churchill. 2015. Online Inspiration and
Exploration for Identity Reinvention. In Proceedings of the 33rd Annual ACM Conference on Human Factors in Computing
Systems (CHI ’15). ACM, New York, NY, USA, 3809–3818. https://doi.org/10.1145/2702123.2702270
Proc. ACM Hum.-Comput. Interact., Vol. 1, No. 2, Article 38. Publication date: November 2017.

PACM on Human-Computer Interaction, Vol. 1, No. CSCW, Article 38. Publication date: November 2017.

38:24

T. Dillahunt et al.

[45] Wen He, Deyi Li, Tianlei Zhang, Lifeng An, Mu Guo, and Guisheng Chen. 2012. Mining Regular Routes from GPS Data
for Ridesharing Recommendations. In Proceedings of the ACM SIGKDD International Workshop on Urban Computing
(UrbComp ’12). ACM, New York, NY, USA, 79–86. https://doi.org/10.1145/2346496.2346510
[46] Brent Hecht, Loren Terveen, Kate Starbird, Ben Shneiderman, and Jennifer Golbeck. 2017. The 2016 US Election and
HCI: Towards a Research Agenda. In Proceedings of the 2017 CHI Conference Extended Abstracts on Human Factors in
Computing Systems (CHI EA ’17). ACM, New York, NY, USA, 1307–1311. https://doi.org/10.1145/3027063.3051140
[47] Yan Huang, Favyen Bastani, Ruoming Jin, and Xiaoyang Sean Wang. 2014. Large Scale Real-time Ridesharing with
Service Guarantee on Road Networks. Proc. VLDB Endow. 7, 14 (Oct. 2014), 2017–2028. https://doi.org/10.14778/
2733085.2733106
[48] Tapio Ikkala and Airi Lampinen. 2014. Defining the Price of Hospitality: Networked Hospitality Exchange via Airbnb.
In Proceedings of the Companion Publication of the 17th ACM Conference on Computer Supported Cooperative Work &
Social Computing (CSCW Companion ’14). ACM, New York, NY, USA, 173–176. https://doi.org/10.1145/2556420.2556506
[49] Tapio Ikkala and Airi Lampinen. 2015. Monetizing Network Hospitality: Hospitality and Sociability in the Context
of Airbnb. In Proceedings of the 18th ACM Conference on Computer Supported Cooperative Work & Social Computing
(CSCW ’15). ACM, New York, NY, USA, 1033–1044. https://doi.org/10.1145/2675133.2675274
[50] Thivya Kandappu, Archan Misra, Shih-Fen Cheng, Nikita Jaiman, Randy Tandriansyah, Cen Chen, Hoong Chuin
Lau, Deepthi Chander, and Koustuv Dasgupta. 2016. Campus-scale mobile crowd-tasking: Deployment & behavioral
insights. In Proceedings of the 19th ACM Conference on Computer-Supported Cooperative Work & Social Computing.
ACM, 800–812.
[51] Joseph Kasera, Jacki O’Neill, and Nicola J Bidwell. 2016. Sociality, Tempo & Flow: Learning from Namibian Ridesharing.
In Proceedings of the First African Conference on Human Computer Interaction. ACM, 36–47.
[52] Jofish Kaye, Casey Fiesler, Neha Kumar, and Bryan Semaan. 2017. Policy Impacts on the HCI Research Community. In
Proceedings of the 2017 CHI Conference Extended Abstracts on Human Factors in Computing Systems (CHI EA ’17). ACM,
New York, NY, USA, 1300–1302. https://doi.org/10.1145/3027063.3051706
[53] Khalid S Khan, Regina Kunz, Jos Kleijnen, and Gerd Antes. 2003. Five steps to conducting a systematic review. Journal
of the Royal Society of Medicine 96, 3 (2003), 118–121.
[54] Shin’ichi Konomi and Tomoyo Sasao. 2015. The use of colocation and flow networks in mobile crowdsourcing.
In Adjunct Proceedings of the 2015 ACM International Joint Conference on Pervasive and Ubiquitous Computing and
Proceedings of the 2015 ACM International Symposium on Wearable Computers. ACM, 1343–1348.
[55] Shin’ichi Konomi and Tomoyo Sasao. 2016. Crowd geofencing. In Proceedings of the Second International Conference on
IoT in Urban Space. ACM, 14–17.
[56] Farshad Kooti, Mihajlo Grbovic, Luca Maria Aiello, Nemanja Djuric, Vladan Radosavljevic, and Kristina Lerman.
2017. Analyzing Uber’s Ride-sharing Economy. In Proceedings of the 26th International Conference on World Wide Web
Companion. International World Wide Web Conferences Steering Committee, 574–582.
[57] Airi Lampinen. 2014. Account Sharing in the Context of Networked Hospitality Exchange. In Proceedings of the 17th
ACM Conference on Computer Supported Cooperative Work & Social Computing (CSCW ’14). ACM, New York, NY, USA,
499–504. https://doi.org/10.1145/2531602.2531665
[58] Airi Lampinen, Victoria Bellotti, Andrés Monroy-Hernández, Coye Cheshire, and Alexandra Samuel. 2015. Studying
the “Sharing Economy”: Perspectives to Peer-to-Peer Exchange. In Proceedings of the 18th ACM Conference Companion
on Computer Supported Cooperative Work & Social Computing (CSCW’15 Companion). ACM, New York, NY, USA,
117–121. https://doi.org/10.1145/2685553.2699339
[59] Airi Lampinen, Vilma Lehtinen, Coye Cheshire, and Emmi Suhonen. 2013. Indebtedness and reciprocity in local online
exchange. In Proceedings of the 2013 conference on Computer supported cooperative work. ACM, 661–672.
[60] Mathias Lecuyer, Max Tucker, and Augustin Chaintreau. 2017. Improving the Transparency of the Sharing Economy.
In Proceedings of the 26th International Conference on World Wide Web Companion. International World Wide Web
Conferences Steering Committee, 1043–1051.
[61] Min Kyung Lee, Daniel Kusbit, Evan Metsky, and Laura Dabbish. 2015. Working with Machines: The Impact of
Algorithmic and Data-driven Management on Human Workers. In Proceedings of the 33rd Annual ACM Conference on
Human Factors in Computing Systems (CHI ’15). ACM, 1603–1612. https://doi.org/10.1145/2702123.2702548
[62] Lawrence Lessig. 2008. Remix: Making art and commerce thrive in the hybrid economy. Penguin Group, New York, USA.
[63] LexisNexis. 2017. Welcome to LexisNexis Legal & Professional. (2017). https://www.lexisnexis.com/en-us/home.page
[64] Junfeng Liao, Shuhua Li, and Tiange Chen. 2017. Research on TPB model for Participating Behavior in Sharing
Economy. In Proceedings of the 2017 International Conference on Management Engineering, Software Engineering and
Service Sciences. ACM, 306–310.
[65] Gustavo Lopez and Luis A. Guerrero. 2017. Awareness Supporting Technologies Used in Collaborative Systems: A
Systematic Literature Review. In Proceedings of the 2017 ACM Conference on Computer Supported Cooperative Work and
Social Computing (CSCW ’17). ACM, New York, NY, USA, 808–820. https://doi.org/10.1145/2998181.2998281
Proc. ACM Hum.-Comput. Interact., Vol. 1, No. 2, Article 38. Publication date: November 2017.

PACM on Human-Computer Interaction, Vol. 1, No. CSCW, Article 38. Publication date: November 2017.

The Sharing Economy in Computing

38:25

[66] Shuo Ma and Ouri Wolfson. 2013. Analysis and Evaluation of the Slugging Form of Ridesharing. In Proceedings of the
21st ACM SIGSPATIAL International Conference on Advances in Geographic Information Systems (SIGSPATIAL’13). ACM,
New York, NY, USA, 64–73. https://doi.org/10.1145/2525314.2525365
[67] Arvind Malhotra and Marshall Van Alstyne. 2014. The Dark Side of the Sharing Economy &Hellip; and How to Lighten
It. Commun. ACM 57, 11 (Oct. 2014), 24–27. https://doi.org/10.1145/2668893
[68] Moira McGregor. 2015. The App in Everyday Life: Research Overview for Doctoral Colloquium. In Proceedings of
the 18th ACM Conference Companion on Computer Supported Cooperative Work &#38; Social Computing (CSCW’15
Companion). ACM, New York, NY, USA, 97–100. https://doi.org/10.1145/2685553.2699330
[69] Ross McLachlan, Claire Opila, Neha Shah, Emily Sun, and Mor Naaman. 2016. You Can’t Always Get What You Want:
Challenges in P2P Resource Sharing. In Proceedings of the 2016 CHI Conference Extended Abstracts on Human Factors in
Computing Systems (CHI EA ’16). ACM, New York, NY, USA, 1301–1307. https://doi.org/10.1145/2851581.2892358
[70] Meatspace Press. 2017. Towards a Fairer Gig Economy. (2017). https://www.smashwords.com/books/view/735210
[71] Johanna Meurer, Martin Stein, David Randall, Markus Rohde, and Volker Wulf. 2014. Social Dependency and Mobile
Autonomy: Supporting Older Adults’ Mobility with Ridesharing Ict. In Proceedings of the SIGCHI Conference on Human
Factors in Computing Systems (CHI ’14). ACM, New York, NY, USA, 1923–1932. https://doi.org/10.1145/2556288.2557300
[72] Seyed Hadi Mirisaee, Margot Brereton, Paul Roe, and Fiona Redhead. 2013. Understanding the Fabric of Social
Interactions for Ridesharing Through Mining Social Networking Sites. In Proceedings of the 25th Australian ComputerHuman Interaction Conference: Augmentation, Application, Innovation, Collaboration (OzCHI ’13). ACM, 451–454.
https://doi.org/10.1145/2541016.2541071
[73] Srinivas Nidhra, Muralidhar Yanamadala, Wasif Afzal, and Richard Torkar. 2013. Knowledge transfer challenges
and mitigation strategies in global software development - A systematic literature review and industrial validation.
International journal of information management 33, 2 (2013), 333–355.
[74] Sunjoo Oh and Jae Yun Moon. 2016. Calling for a Shared Understanding of the "Sharing Economy". In Proceedings of
the 18th Annual International Conference on Electronic Commerce: E-Commerce in Smart Connected World (ICEC ’16).
ACM, New York, NY, USA, 35:1–35:5. https://doi.org/10.1145/2971603.2971638
[75] Anthony J. Onwuegbuzie. 2016. Mapping Saldana’s Coding Methods onto the Literature Review Process. Journal of
Educational Issues 2 (Mar 2016). https://doi.org/10.5296/jei.v2i1.8931
[76] Jeremiah Owyang. 2016. Honeycomb 3.0: The Collaborative Economy Market Expansion. (March 2016). http:
//www.web-strategist.com/blog/2016/03/10/honeycomb-3-0-the-collaborative-economy-market\-expansion-sxsw/
[77] Daniel Pargman, Elina Eriksson, and Adrian Friday. 2016. Limits to the Sharing Economy. In Proceedings of the Second
Workshop on Computing Within Limits (LIMITS ’16). ACM, New York, NY, USA, 12:1–12:7. https://doi.org/10.1145/
2926676.2926683
[78] Xin Peng, Jingxiao Gu, Tian Huat Tan, Jun Sun, Yijun Yu, Bashar Nuseibeh, and Wenyun Zhao. 2016. CrowdService:
serving the individuals through mobile crowdsourcing and service composition. In Automated Software Engineering
(ASE), 2016 31st IEEE/ACM International Conference on. IEEE, 214–219.
[79] Luke Pittaway. 2011. Systematic Literature Reviews. In The SAGE Dictionary of Qualitative Management Research,
Richard Thorpe and Robin Holt (Eds.). SAGE Publications Ltd, 217–218. https://doi.org/10.4135/9780857020109
[80] Giovanni Quattrone, Davide Proserpio, Daniele Quercia, Licia Capra, and Mirco Musolesi. 2016. Who Benefits from
the "Sharing" Economy of Airbnb? arXiv:1602.02238 [physics] (Feb. 2016). http://arxiv.org/abs/1602.02238 arXiv:
1602.02238.
[81] Alexander J. Quinn and Benjamin B. Bederson. 2011. Human Computation: A Survey and Taxonomy of a Growing
Field. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (CHI ’11). ACM, New York, NY,
USA, 1403–1412. https://doi.org/10.1145/1978942.1979148
[82] Arthi Ramachandran and Augustin Chaintreau. 2015. Who Contributes to the Knowledge Sharing Economy?. In
Proceedings of the 2015 ACM Conference on Online Social Networks (COSN ’15). ACM, New York, NY, USA, 37–48.
https://doi.org/10.1145/2817946.2817963
[83] Noopur Raval and Paul Dourish. 2016. Standing Out from the Crowd: Emotional Labor, Body Labor, and Temporal
Labor in Ridesharing. In Proceedings of the 19th ACM Conference on Computer-Supported Cooperative Work & Social
Computing (CSCW ’16). ACM, New York, NY, USA, 97–107. https://doi.org/10.1145/2818048.2820026
[84] Johnny Saldaña. 2012. The Coding Manual for Qualitative Researchers (2 ed.). Thousand Oaks, CA: Sage.
[85] Ari Schlesinger, W. Keith Edwards, and Rebecca E. Grinter. 2017. Intersectional HCI: Engaging Identity through Gender,
Race, and Class. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (CHI ’17). ACM.
[86] Patrick C. Shih, Victoria Bellotti, Kyungsik Han, and John M. Carroll. 2015. Unequal Time for Unequal Value:
Implications of Differing Motivations for Participation in Timebanking. In Proceedings of the 33rd Annual ACM
Conference on Human Factors in Computing Systems (CHI ’15). ACM, New York, NY, USA, 1075–1084. https://doi.org/
10.1145/2702123.2702560

Proc. ACM Hum.-Comput. Interact., Vol. 1, No. 2, Article 38. Publication date: November 2017.

PACM on Human-Computer Interaction, Vol. 1, No. CSCW, Article 38. Publication date: November 2017.

38:26

T. Dillahunt et al.

[87] M. Six Silberman, Lisa Nathan, Bran Knowles, Roy Bendor, Adrian Clear, Maria Håkansson, Tawanna Dillahunt, and
Jennifer Mankoff. 2014. Next Steps for Sustainable HCI. interactions 21, 5 (Sept. 2014), 66–69. https://doi.org/10.1145/
2651820
[88] Emmi Suhonen, Airi Lampinen, Coye Cheshire, and Judd Antin. 2010. Everyday favors: a case study of a local online
gift exchange system. In Proceedings of the 16th ACM international conference on Supporting group work. ACM, 11–20.
[89] Emily Sun, Ross McLachlan, Mor Naaman, and Cornell Tech. 2017. TAMIES: A Study and Model of Adoption in P2P
Resource Sharing and Indirect Exchange Systems.. In Proceedings of the 2017 ACM conference on Computer supported
cooperative work and Social Computing. 2385–2396.
[90] Arun Sundararajan. 2016. The Sharing Economy: The End of Employment and the Rise of Crowd-Based Capitalism. MIT
Press.
[91] Jiliang Tang, Huiji Gao, Huan Liu, and Atish Das Sarma. 2012. eTrust: Understanding Trust Evolution in an Online
World. In Proceedings of the 18th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD
’12). ACM, New York, NY, USA, 253–261. https://doi.org/10.1145/2339530.2339574
[92] Adi Tedjasaputra and Eunice Sari. 2016. Sharing Economy in Smart City Transportation Services. In Proceedings of the
SEACHI 2016 on Smart Cities for Better Living with HCI and UX. ACM, 32–35.
[93] Rudy Telles Jr. 2016. Digital Matching Firms: A New Definition in the “Sharing Economy” Space. (2016).
[94] Rannie Teodoro, Pinar Ozturk, Mor Naaman, Winter Mason, and Janne Lindqvist. 2014. The Motivations and Experiences of the On-demand Mobile Workforce. In Proceedings of the 17th ACM Conference on Computer Supported
Cooperative Work and Social Computing (CSCW ’14). ACM, New York, NY, USA, 236–247. https://doi.org/10.1145/
2531602.2531680
[95] Jacob Thebault-Spieker, Loren Terveen, and Brent Hecht. 2015. Avoiding the South Side and the Suburbs: The Geography
of Mobile Crowdsourcing Markets. In Proceedings of the 18th ACM Conference on Computer Supported Cooperative Work
& Social Computing (CSCW ’15). ACM, New York, NY, USA, 265–275. https://doi.org/10.1145/2675133.2675278
[96] Jacob Thebault-Spieker, Loren Terveen, and Brent Hecht. 2017. Toward a Geographic Understanding of the Sharing
Economy: Systemic Biases in UberX and TaskRabbit. ACM Transactions on Computer-Human Interaction (TOCHI) 24, 3
(2017), 21.
[97] Charles Tian, Yan Huang, Zhi Liu, Favyen Bastani, and Ruoming Jin. 2013. Noah: A Dynamic Ridesharing System. In
Proceedings of the 2013 ACM SIGMOD International Conference on Management of Data (SIGMOD ’13). ACM, New York,
NY, USA, 985–988. https://doi.org/10.1145/2463676.2463695
[98] William M.K. Trochim. 2006. Research Methods Knowledge Base. http://www.socialresearchmethods.net/kb/resques.php.
(2006). Accessed: 2016-08-26.
[99] Theresa Velden and Carl Lagoze. 2012. The Network Analytic Extraction. CoRR abs/1205.2114 (2012). http://arxiv.org/
abs/1205.2114
[100] Szymon Wasik, Maciej Antczak, Jan Badura, Artur Laskowski, and Tomasz Sternal. 2016. Optil.Io: Cloud Based
Platform for Solving Optimization Problems Using Crowdsourcing Approach. In Proceedings of the 19th ACM Conference
on Computer Supported Cooperative Work and Social Computing Companion (CSCW ’16 Companion). ACM, New York,
NY, USA, 433–436. https://doi.org/10.1145/2818052.2869098
[101] Lei Xu, Nolan Shah, Lin Chen, Nour Diallo, Zhimin Gao, Yang Lu, and Weidong Shi. 2017. Enabling the Sharing
Economy: Privacy Respecting Contract Based on Public Blockchain. In Proceedings of the ACM Workshop on Blockchain,
Cryptocurrencies and Contracts. ACM, 15–21.
[102] Han Yu, Chunyan Miao, Zhiqi Shen, and Cyril Leung. 2015. Quality and budget aware task allocation for spatial
crowdsourcing. In Proceedings of the 2015 International Conference on Autonomous Agents and Multiagent Systems.
International Foundation for Autonomous Agents and Multiagent Systems, 1689–1690.
[103] Man-Ching Yuen, Ling-Jyh Chen, and Irwin King. 2009. A survey of human computation systems. In Computational
Science and Engineering, 2009. CSE’09. International Conference on, Vol. 4. IEEE, 723–728.

Received June 2017; revised August 2017; accepted November 2017.

Proc. ACM Hum.-Comput. Interact., Vol. 1, No. 2, Article 38. Publication date: November 2017.

PACM on Human-Computer Interaction, Vol. 1, No. CSCW, Article 38. Publication date: November 2017.
