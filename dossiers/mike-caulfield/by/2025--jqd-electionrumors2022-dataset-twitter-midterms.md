---
title: "ElectionRumors2022: A Dataset of Election Rumors on Twitter During the 2022 U.S. Midterms"
person: mike-caulfield
section: by
type: journal-article
year: 2025
date: 2025-01-06
venue: "Journal of Quantitative Description: Digital Media 5"
authors: "Joseph S. Schafer, Kayla Duskin, Stephen Prochaska, Morgan Wack, Anna Beers, Lia Bozarth, Taylor Agajanian, Michael Caulfield, Emma S. Spiro, Kate Starbird"
source_url: https://doi.org/10.51685/jqd.2025.002
retrieved: 2026-08-13
content: full-text
notes: "Diamond OA. Text extracted with pdftotext -layout from the publisher PDF galley; PDF layout artifacts (running heads, page numbers, ligature marks) remain. Caulfield is a middle author. OpenAlex W4406127278."
---

# ElectionRumors2022: A Dataset of Election Rumors on Twitter During the 2022 U.S. Midterms

## Full text

Journal of Quantitative Description: Digital Media 5(2025), 1–61          10.51685/jqd.2025.002


 ElectionRumors2022: A Dataset of Election Rumors on Twitter During the
                                   2022 U.S. Midterms


                    JOSEPH S. SCHAFER⇤ and KAYLA DUSKIN⇤
                             University of Washington, USA

                                 STEPHEN PROCHASKA
                             University of Washington, USA

                                     MORGAN WACK
                             University of Zurich, Switzerland

                                       ANNA BEERS
                            University of North Carolina, USA

                                       LIA BOZARTH
                             University of Washington, USA

                                  TAYLOR AGAJANIAN
                              Northwestern University, USA

                                  MICHAEL CAULFIELD
                             University of Washington, USA

                                      EMMA S. SPIRO
                             University of Washington, USA

                                     KATE STARBIRD
                            University of Washington, USA


Copyright ©2025 (Schafer, Duskin, Prochaska, Wack, Beers, Bozarth, Agajanian, Caulfield, Spiro,
Starbird). Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International Public
License. Available at: http://journalqd.org

Schafer & Duskin et al.             Journal of Quantitative Description: Digital Media 5(2025) 2


      Understanding the spread of online rumors is a pressing societal challenge and
      an active area of research across domains. In the context of the 2022 U.S.
      midterm elections, one influential social media platform for sharing information
      — including rumors that may be false, misleading, or unsubstantiated — was
      Twitter (now renamed X). To increase understanding of the dynamics of online
      rumors about elections, we present and analyze a dataset of 1.81 million Twitter
      posts corresponding to 135 distinct rumors which spread online during the
      midterm election season (September 5 to December 1, 2022). We describe how
      this data was collected, compiled, and supplemented, and provide a series of
      exploratory analyses along with comparisons to a previously-published dataset
      on 2020 election rumors. We also conduct a mixed-methods analysis of five
      distinct rumors about the election in Arizona, a particularly prominent focus of
      2022 election rumoring. Finally, we provide a set of potential future directions
      for how this dataset could be used to facilitate future research into online
      rumors, misinformation, and disinformation.


      Keywords: Twitter, rumors, midterm elections, elections


                                        Introduction

        Online rumors, and related phenomena such as misinformation and disinformation,
have become increasingly important to understand and address, with prior work framing
misinformation and disinformation as urgent problems (Calo et al., 2021) which need an
interdisciplinary and integrated crisis discipline approach to research (Bak-Coleman et al.,
2021). Rumors are a byproduct of collective sensemaking processes, whereby people come
together, frequently in online spaces, to make sense of ambiguous and/or uncertain infor-
mation (Shibutani, 1966; Arif et al., 2016). Events such as natural hazards, public health
⇤
  These authors contributed equally to this work.
Work was conducted when all authors were working at the University of Washington.
Schafer: schaferj@uw.edu
Duskin: kduskin@uw.edu
Date submitted: 2024-08-17


Copyright ©2025 (Schafer, Duskin, Prochaska, Wack, Beers, Bozarth, Agajanian, Caulfield, Spiro,
Starbird). Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International Public
License. Available at: http://journalqd.org

JQD:DM 5(2025)                                                                     ElectionRumors2022 3


crises, and elections are frequent catalysts for rumoring behavior. Unsurprisingly, a growing
body of research has focused on understanding sensemaking, rumoring, and misinformation
in the context of democratic elections, both within the United States (U.S.) (Bovet and
Makse, 2019; Jones-Jang et al., 2021; Kennedy et al., 2022; Oehmichen et al., 2019) and
globally (e.g. (Akbar et al., 2022; Mendoza et al., 2023; Recuero et al., 2020)).

           This work focuses on midterm elections as a site of potential election rumoring, given
their critical importance to governmental composition. The 2022 U.S. midterm elections
consisted of nationwide elections for all members of the U.S. House of Representatives and
a partial set of members of the U.S. Senate, as well as for many state and local races
(e.g. the governor’s race in Arizona). Documenting election process-related rumors in
this specific context allows for important gains to research understanding; not only can we
better understand the dynamics of rumors online by expanding the cases studies within the
research community, but we can also consider whether phenomena observed in presidential
elections apply to U.S. non-presidential election contexts as well.

           In this paper, we aggregate and describe a set of 135 rumors that spread on Twitter
(now renamed X)1 — at the time, a notable social media platform for real-time information
and news sharing in the U.S. — during the 2022 U.S. midterm elections. We curate a set of
posts that include original tweets, retweets, quote tweets, and reply tweets that correspond
to each rumor, which in aggregate comprises 1.81 million posts. We additionally include
information on the web domains that were cited in content pertaining to each rumor, and
the geographical location (U.S. state or states) that is the focus of each rumor. We describe
the process used for creating and curating a comprehensive (high recall) and low-noise (high
precision) sample of tweets for each rumor.

           This dataset of false or misleading election-related rumors opens avenues for future
research. In this work we compare the online information environment of the 2022 U.S.
midterm elections to that of the 2020 U.S. presidential midterm. Future work could extend
this to future elections to illuminate longer term trends. The highly specific categorization
of rumors and tweets may have use in future studies of political fact-checking, cross-platform

1
    For clarity we will use terminology as it existed at the time of data collection, e.g. Twitter, tweets,
    retweets, quote tweets, and reply tweets

Schafer & Duskin et al.                Journal of Quantitative Description: Digital Media 5(2025) 4


rumor spread, the use of media (e.g. videos, images, external links) in the spread of false
and misleading narratives, the linguistic choices of political communicators, and the role
of platform governance and infrastructures in the spread of these narratives, as in Duskin
et al. (2024). Furthermore, the mixed-methods approach detailed here may be of use in
identifying, scoping, and quantifying narratives outside of the election context such as in
arenas of public health, crisis events, or other online discourse. Those interested in using
the dataset2 may wish to jump to the documentation of dataset structure in Figure 2, and
examples of rumors and rumor tweets in Section 6.

          The rest of this paper is structured as follows: first, we provide a brief background
section on the terminology we use in this paper, and prior research into online rumoring
and elections. We then describe the process of collecting and filtering our dataset to 1.81
million tweets related to false, misleading, and unsubstantiated rumors, mapping tweets to
our set of 135 rumors, and then describe how this data is formatted and shared. Next, we
present several empirical analyses of this data, first through five preliminary descriptive sta-
tistical analyses, positioned in comparison with a similar dataset on the 2020 U.S. elections
previously published in (Kennedy et al., 2022). Next, to demonstrate the utility of these
data for more in-depth research, we feature a mixed-methods, case study analysis of three
rumors focused on the state of Arizona. We conclude by outlining future work that could
build off of this dataset and accompanying analyses, along with reflections on the ethical
considerations and methodological limitations of using and researching with these data.

                                           Background

          Throughout this paper, we use the framing of election-related rumors. In this sec-
tion, we briefly define this term and discuss how it relates to other forms of information
— namely misinformation and disinformation. We then provide background regarding the
study of rumors online and in the context of election administration.


2
    Data available at https://zenodo.org/records/12019800

JQD:DM 5(2025)                                                         ElectionRumors2022 5


                             Terminology and Definitions

       Rumors are stories that contain information that is unverified or incomplete at the
time of dissemination. They are a key component of conveying important information
through a population (Pendleton, 1998). Shibutani explains that rumors involve the pool-
ing of intellectual resources to provide meaningful interpretation to an otherwise ambiguous
situation (Shibutani, 1966). Situations characterized by high uncertainty and elevated anx-
iety are the prime environment for rumors to emerge (Anthony, 1973; Rosnow, 1980). As
situational uncertainty resolves, the information shared through rumors, while initially un-
verified, may later be shown to be true or false, or as time goes on may remain ambiguous
— being neither substantiated nor disproven.

       Rumors that turn out to be false or misleading can be considered misinformation.
Misinformation is inaccurate information that may be shared without the intent to mislead
or harm audiences, or potentially without awareness that the message contains falsehoods
(Jack, 2017; Freelon and Wells, 2020; Calo et al., 2021). Closely related is disinformation,
denoting false or misleading information that is shared deliberately to further a particular
goal such as monetary profit or political gain (Jack, 2017; Freelon and Wells, 2020). A
disinformation campaign may consist of strategic amplification of a mixture of true, false,
and misleading content that contributes to a desired narrative. Disinformation campaigns
have been known to amplify organic rumors, as well as seed new rumors, as art of their
aims. In these cases, disinformation may be spread unwittingly by audiences unaware of its
deceptive nature (Rid, 2020).

       The dataset described in this paper is comprised of a wide range of content shared
on Twitter — some posts contain early reports of real events related to the election, other
posts include soundly disproven claims, while some posts add misleading framing to factual
events. Given this range, we find the term rumor to be the most accurate and useful
descriptor for the collection. Acknowledgment of uncertainty is key to understanding and
productively discussing modern information systems (Spiro and Starbird, 2023).

       While we use rumors as the conceptual framework for this work, our dataset is fo-
cused on rumors with false, misleading, or unsubstantiated components, therefore we draw

Schafer & Duskin et al.            Journal of Quantitative Description: Digital Media 5(2025) 6


considerable influence from research in mis- and disinformation. We focus on false/mislead-
ing rumors to allow for more effective comparability with prior datasets (e.g. (Kennedy
et al., 2022) or (Sharma et al., 2022)), and to reduce the potential for accidental or ad-
versarial mischaracterization of the rumors that turned out to be true. It is important to
note that factual events and information play a large role in rumoring. When rumors about
factual events are accompanied by misleading, false, or unsubstantiated components, we
include them in this dataset.

        Given the fluctuating understandings of terms, previous work exploring false and
misleading online narratives use different terms for the mixed-veracity messages present in
online social discourse. For example, Kennedy et al. uses ‘misinformation’ as an umbrella
term — inclusive of rumors, misinformation, and disinformation — in their study of stories
shared online during the U.S. 2020 election (Kennedy et al., 2022). Similarly, in their work
characterizing user engagement with conspiratorial topics on Twitter during the 2020 U.S.
election, Sharma et al. use ‘disinformation’ as term to capture what they call ‘distorted
narratives’ which include unreliable or conspiratorial claims regardless of the intent of the
content’s author (Sharma et al., 2022). In this work we do not attempt to distinguish
individual pieces of content as true or false (e.g. to label posts as misinformation) nor as
intentionally or unintentionally misleading (e.g. to label posts as disinformation). Rather,
we organize content into distinct rumors, acknowledging the overlapping functions and
understandings of rumor, stories, misinformation, and disinformation.

                  Online Rumoring about Election Administration

        Online social media platforms have changed how people consume news, learn about
crises, and keep up with current events. In the digital age, rumors have the potential to
spread faster than ever and reach broader audiences (Doerr et al., 2012; Sunstein, 2009).
Research in this space has focused heavily within the domain of crisis informatics – the study
of how citizens respond to and make sense of emerging crises through online communication
(Palen et al., 2007). Studies have helped illuminate online rumor propagation (Arif et al.,
2016; Zeng et al., 2016) and correction (Arif et al., 2017; Starbird et al., 2018), along
with their role in collective sensemaking (Starbird et al., 2016) in the context of diverse
public crises ranging from natural hazards to acts of violence such as shootings or hostage

JQD:DM 5(2025)                                                          ElectionRumors2022 7


situations.

        The affordances of online social media platforms allow users to both share and seek
out emerging information extremely rapidly, and without the gatekeeping mechanisms of
traditional media communication. In fact, the very structure of online social networks
(specifically Twitter) facilitates faster rumor propagation than other networks of similar
size and density (Doerr et al., 2012). Additionally, the novelty and salience of information
contained in rumors may contribute to their propensity to spread rapidly online. In a large-
scale study of online news, (Vosoughi et al., 2018) show that false news travels farther,
faster, and more broadly on Twitter than true news and is also more novel and surprising
to audiences than true news. As online populations collectively seek to make sense of
an uncertain, stressful, or novel situation, rumors emerge to provide explanation and fill
information voids – even if their validity is unknown.

        One context ripe for rumors is election administration, given the high degree of
uncertainty and consequence associated with them. As such, rumors during and about
election administration have gained increased attention in the last decade in particular.
Notable related datasets documenting this include the VoterFraud2020 dataset focused
on #VoterFraud and related hashtags during the 2020 election (Abilov et al., 2021), the
ElectionMisinfo2020 dataset focused on 2020 election misinformation using mixed-methods
curation described in (Kennedy et al., 2022), the #Election2020 dataset focused on broad
coverage of 2020 election discussions on Twitter in (Chen et al., 2022), and the MEIU22
dataset of posts broadly related to the 2022 U.S. midterm elections across multiple platforms
in (Aiyappa et al., 2023). The dataset presented here offers a narrowly-scoped, low-noise
dataset that fills an important gap in existing work by documenting misinformative rumors
in a recent midterm election.

                      Tweet Collection & Rumor Identification

        In this section, we detail the collection of tweets broadly related to the midterm
election, how we identified emergent election rumors in real time and matched tweets to
their corresponding rumor, and finally how we evaluated quality at both the rumor and
tweet level. Figure 1 depicts this iterative procedure wherein we employ empirical and

Schafer & Duskin et al.               Journal of Quantitative Description: Digital Media 5(2025) 8


qualitative evaluation to a broad dataset to create a rich dataset that enables assessment
of rumoring about the administration of the 2022 U.S. election.

                                Collection of Election Tweets

          Our team collected an initial election-related tweet set of 446 million tweets through-
out the months leading up to and following the 2022 U.S. midterm elections using Twitter’s
V1.1 streaming API3 . We did so using a list of keywords, phrases, and hashtags related to
the election (e.g. ballot, vote) as well as to narratives common in election rumoring (e.g.
fraud, tabulator). These terms were selected by a team of researchers with contextual exper-
tise studying previous elections and informed by prior work conducted during the 2020 U.S.
elections (Kennedy et al., 2022). The keywords were designed to capture a comprehensive
dataset of tweets related to voting, election materials, procedures, results, and claims of
election fraud. The full list of keywords used in collecting the general election tweets is
included in the Appendix in Table A1. Modifications (additions and deletions of keywords)
were made to this list to adapt to emerging trends and narratives, and these modifications
are also noted in the Appendix in Table A1. Additionally, as a robustness check against
any bias in this set of keywords, in the Appendix we briefly analyze a subset of this data
based on a smaller set of politically neutral keywords (‘ballot’, ‘vote’, and ‘election’) and
find similar patterns to using the full keyword list.

          To reduce the impact of rate-limiting, keywords were divided among nine separate
collectors; each collector had its own streaming credential attached to different members of
our research team (Twitter’s V1.1 API allowed up to max 50 tweets per second collection
for any one credential). It is important to note that the collectors were intermittently
rate-limited in the two weeks prior to the 2022 Midterm election, and were consistently
rate-limited on Nov 7th and Nov 8th. Additionally, one of the collectors went briefly down
on Nov 2nd due to a credential issue that was quickly resolved.

          We approximate the comprehensiveness of the resulting dataset of collected election-
related tweets using missing retweets. That is, let tweet i 2 SharedOrigT weets where


3
    https://web.archive.org/web/20220307124146/https://developer.twitter.com/en/docs/
    twitter-api/v1

JQD:DM 5(2025)                                                           ElectionRumors2022 9


SharedOrigT weets contains all the original tweets that have at least 1 retweet in the
dataset. We denote |i|obs as the number of observed retweets of i in the dataset. Further,
let |i|exp be the expected number of retweets for tweet i (i.e. the number of retweets
that should be present in the dataset). We derive |i|exp by taking the earliest and the
latest versions (i.e., timestamped) of i observed, and compute the difference in the recorded
retweet counts (embedded in the meta-data) of the two versions. Finally, the fraction of
missing retweets of i is defined as the difference between |i|exp and |i|obs . We find that 12%
of retweets were missing from the dataset overall; 20% of retweets were missing during the
Midterm election week (11/02/2022 to 11/08/2022). This is consistent with prior literature
which demonstrated that the streaming API can miss significant portions of data (Pfeffer
et al., 2023; Wang et al., 2015). However, missing data from the Streaming API should not
significantly impact topic coverage (Pfeffer et al., 2023).

       To improve data comprehensiveness, and to limit bias, for original tweets that have
at least one retweet captured by our collectors but are themselves missing from the dataset,
we used a separate process to attempt to backfill these original tweets. 1,450 tweets were
included in the final, curated rumor dataset which were collected via backfilling, while 2.38
million of the 446 million initial tweet collection came via backfilling. Though it is possible
that we missed some tweets entirely because of rate limiting, which could have impacted
our dataset, the likelihood of missing major data via this sampling method coupled with
our backfilling process is low.

                                  Identifying Rumor Leads

       During a period of ten weeks between 9/19/2022 and 12/01/2022, a team of 15
undergraduate research assistants worked in daily shifts to actively observe online discourse
about the election and document instances of online content related to U.S. election in-
tegrity. Similar to the collection of the initial election-related tweet dataset, initial rumor
leads were focused on enabling rapid, broad coverage of online discourse which could in-
volve rumors related to the election (at this stage, the team emphasized coverage rather than
precision, as we would curate this set further at a later step). Researchers first conducted
advanced search queries on Twitter using keyword queries and made note of any content
with the potential to be an election rumor. Some baseline keyword queries were used daily

Schafer & Duskin et al.                Journal of Quantitative Description: Digital Media 5(2025) 10


             Figure 1. A diagram showing the process of curating this dataset


throughout the data collection period (e.g. ‘(ballot OR ballots)’), while others were cus-
tomized to exogenous events such as news articles or current events related to the election.
Content containing potential rumors was logged if it met two scoping criteria: 1) the po-
tential rumor contained a new (or newly prominent) claim that hadn’t been logged by the
team previously and 2) the claim met one or more of the topical scope criteria. Though the
initial scope of our real-time analysis included other categories, such as threats to election
personnel, for this dataset, we focus on rumors which either are likely to deprive someone
of their vote (which would include procedural interference, participation interference, or
solicitation of fraud), or to cast doubt on the integrity of the election processes and/or the
accuracy of election results. Once logged, the undergraduate assistants conducted initial
manual analysis to identify any related content on Twitter (or other platforms)4 and sum-
marize the claims present. Given team size and team hours devoted to finding rumor leads,
as well as the contemporaneous nature of rumor identification, we are confident that we
have a high degree of recall for rumors which spread on Twitter at a significant scale about
election processes during this period.


4
    Searches of these other platforms, including Facebook, Instagram, TikTok, and Telegram, were used
    to inform related rapid-response work, but was not used for the Twitter-focused dataset described
    in this paper.

JQD:DM 5(2025)                                                        ElectionRumors2022 11


                         Constructing a Preliminary Rumor Pool

          During a period of eight weeks between 9/26/2022 and 11/22/2022 a group of 17
researchers, including nine of the authors, worked in team shifts refining and investigating
the logged rumor leads. Teams used qualitative and quantitative analysis to either flesh
out the leads into preliminary rumors, or discard them for not meeting scope — the most
common reasons for discarding a rumor were identification of a duplicate rumor, or having
very low spread on Twitter. Qualitatively, teams searched for relevant news coverage, related
social media content, and official sources or fact-checks when available. To scope a set of
tweets related to each rumor, researchers used an iterative, manual process to develop search
queries to identify tweets in the election tweet pool related to each rumor (this process is
similar to that described in (Kennedy et al., 2022)). Researchers identified a date range
and combined keywords, post IDs, and/or URLs connected to the rumor using boolean
operators to construct queries that captured as much of the relevant discourse as possible
while minimizing noise. This allowed for empirical analyses of rumor virality, breadth of
spread, and identification of key messengers of each rumor. Key findings surfaced from
these analyses were shared with journalists and the public during this time period through
blog posts 5 and Twitter threads6 .

                                   Rumor Criteria Coding

          Following the team’s real-time daily analysis efforts, our team conducted post-hoc
qualitative coding on the set of rumors during January and February, 2023 to further ensure
de-duplication and consistency in meeting specified inclusion criteria. This assessment of
the rumors involved three members of the research team with deep contextual knowledge
of election related rumors, and high familiarity with the dataset. The key criteria met by
all rumors included in the dataset presented here are as follows:


      • Online discussion about the rumor on Twitter is primarily in English.

      • The rumor pertains to the 2022 U.S. midterm election, rather than a prior election
         cycle or an election in another country.

5
    https://www.eipartnership.net/blog
6
    https://twitter.com/EI_Partnership

Schafer & Duskin et al.                 Journal of Quantitative Description: Digital Media 5(2025) 12


      • The rumor is either unsubstantiated or contradicted by authoritative sources (dis-
         cussed below).

      • The rumor is likely to deprive a person of their vote (e.g. false information about
         where or how to vote) or likely to delegitimize election results.

      • The rumor has non-trivial circulation on Twitter (e.g. more than one original tweet)7 .

      • The majority of discourse online relevant to this rumor occurred within the date range
         9/5/2023 - 12/1/2023.


           Notably, the post-hoc rumor criteria coding included searching for relevant authori-
tative sources (e.g. fact-checks, general reporting, official government communication) per-
taining to each rumor. The purpose of this was to classify discourse around claims as either
significantly substantiated, unsubstantiated, misleading/false, non-falsifiable, or primarily
fact-check/correction. This was important in revisiting claims that were uncorroborated
at the time of initial analysis but that later were shown to be true or false. We only in-
clude rumors found to be false, misleading, or unsubstantiated in the final set included for
publication.

                                     Tweet Quality Assurance

           We evaluate the quality of each set of tweets associated with each rumor. First,
we used the queries developed during the real-time analysis of rumors to identify tweets
related to each rumor. For each rumor, we consider two tweets samples: the ten most-
retweeted tweets, and a random sample of size ten of all other tweets excluding retweets
(i.e., original tweets, quote tweets, and reply tweets). The two first authors qualitatively
coded each tweet in the samples as either related or unrelated to the rumor with which

7
    We remove rumors with negligible initial spread for two reasons. First, we wanted to focus on
    the spread of rumors, and rumors that fell below our (already highly-permissive) spread thresholds
    received such low attention as to be functionally not spreading (such as one tweet with less than
    100 likes, and no other discussion). Second, scoping to rumors with at least a moderate amount of
    attention allows us to be far more confident about the recall of our dataset in terms of what rumors
    were spreading. While our team may have missed one random post with a handful of likes, they
    are unlikely to have missed an incident that received spread at a level of spread that would have
    warranted inclusion.

JQD:DM 5(2025)                                                              ElectionRumors2022 13


it was meant to be associated8 . We set an acceptance criteria that nine out of the ten
most-retweeted tweets returned by the query, and at least eight out of a random sample
of ten non-retweet tweets must be related to the rumor. Any queries that did not meet
that threshold were iteratively updated, re-sampled, and re-coded until this criteria was
met. We further adjusted the queries based on temporal volume plots (for an illustration of
such plots for individual rumors, see Figures 10, 11, 12 later in our analysis), to make sure
that we did not prematurely cut off a rumor before its spread had significantly diminished
or died out, or begin it after significant discussion had already occurred. Queries were
also refined to minimize overlaps between rumors by identifying tweets that appeared in
multiple rumors and updating queries so that they only matched the relevant rumor, if only
one should have been included. Some overlaps remain, as some tweets do reference multiple
rumors and should therefore be associated with both. Most rumors exceeded the minimum
threshold for tweet-level precision. Across all incidents and their respective final queries,
99% of the ten most-retweeted tweets were coded as correctly associated with the rumor,
and 96% of the ten random tweets were found to be correctly associated.

           As we discuss further in our limitations section 7, though we are confident in having
a high-recall dataset of in-scope rumors, and are reasonably confident in our recall at the
tweet level, some tweets (for reasons including typos, relevant images without text captions
we could search, or deliberate keyword avoidance (Moran et al., 2022)) that are relevant
would be excluded from our dataset.

                                                Data

           To summarize, we collected tweets corresponding to a set of 135 rumors about
the 2022 U.S. Midterm election from September 5th, 2022 to December 1st, 2022. The
overall dataset contains approximately 1.81 million tweets (88.0% of which are retweets),
and approximately 427,600 unique users. We also include several data enrichments, detailed
below.

           Geographic Location: To gauge where rumors were most concentrated geograph-


8
    Tweets consisting of corrections or fact-checks of a rumor were coded as relevant, though these
    types of content are rare in the dataset.

Schafer & Duskin et al.               Journal of Quantitative Description: Digital Media 5(2025) 14


ically, we identify the state(s) of interest for each rumor. To do so, each rumor was coded
with up to three states that were the focus of discussion within the narrative. If there were
more than three states of equal relevance, or if the rumor did not have any geographic com-
ponents, the rumor is coded as "General". Three of the 135 rumors were coded as relevant
to both a specific state and as "General", as they had significant components related to
particular states as well as to broader narratives about the election.

           External Links: To understand what external sources were used in discussions
of rumors we consider links to external sites using URLs present in each tweet; for each
shortened link (e.g. https://t.co/xxxxx) we used the pycurl library9 to unravel it to obtain
the complete URL. We also extract the domain name from the complete URL using a
regular expression.

           Media Coverage: For each rumor we sought out relevant media coverage or fact-
checks identified during the criteria coding. The included links are not an exhaustive list,
and are included in the dataset to provide additional context for each rumor when possible.
12 of the 135 rumors did not have directly-identified sources linked during criteria coding.

                                              Data Format

           The dataset released in conjunction with this paper consists of three data types:
rumors, tweets, and URLs. For each rumor, associated metadata include: an identifying
number, the state(s) that the rumor was focused on, a short title summarizing what the
rumor was claiming, and one or more URLs of relevant news coverage or fact-checks re-
garding that rumor. For each tweet, metadata provided are: tweet ID (as provided by the
Twitter API), a pseudonymized user ID, and the corresponding rumor ID number (3,640
tweets, (or 0.201% of the dataset) referenced multiple rumors — as a result, the rumor ID
number column is stored as a list). We also release equivalent IDs and user pseudo-ids for
referenced tweets (tweets which were retweeted, quoted, and/or replied to), as well as if a
tweet was collected solely off of location-based keywords or backfilling, for researchers need-
ing disaggregation of particular sources (for further discussion, see the appendix). For each
URL, the associated tweet ID is given. Figure 2 summarizes the dataset features visually.

9
    http://pycurl.io/docs/latest/index.html

JQD:DM 5(2025)                                                        ElectionRumors2022 15


Figure 2. A diagram of the data and feature relations contained in our dataset.
Columns that are joinable across tables are linked via arrows.


                                           Data Sharing

          We aim to make this dataset meet the FAIR principles (Wilkinson et al., 2016),
while also respecting both privacy concerns and the Twitter Terms of Service (at the time
of collection). We make the dataset findable and accessible by hosting it in a Zenodo
repository10 , allowing researchers to easily access and cite this resource. We also make
it interoperable by releasing the standard tweet IDs for all posts contained within, so that
other Twitter collections during this time (such as the Twitter component of (Aiyappa et al.,
2023)) can be cross-referenced. We hope to catalyze data reuse by outlining several ideas
for other projects in the discussion section, and by documenting how this data was collected
herein so that researchers can evaluate the utility of this data for their own projects. Due
to the reduced access of the Twitter API for rehydrating tweets, we will make subsets of
hydrated data available to researchers upon reasonable request. However, both Twitter’s
Terms of Service and privacy concerns for those whose data we compile here prevent release

10
     https://zenodo.org/records/12019800

Schafer & Duskin et al.            Journal of Quantitative Description: Digital Media 5(2025) 16


of a fully hydrated dataset.

                                  Quantitative Analyses

        Now that we have described the process of constructing, curating, and validating this
dataset, and how this data is shareable, we perform five preliminary quantitative analyses
to show the utility of these data. Four of these quantitative analyses include comparisons
to a comparable dataset focused on the 2020 U.S. presidential election (Kennedy et al.,
2022). First, we analyze basic descriptive features of the data such as the temporal volume
of tweets and largest rumors. We then conduct two analyses on the distribution of tweet
topics — by geographic focus and by user political partisanship. Next, we describe the
prevalence of links to external domains, and differences in link-sharing behavior from the
2020 U.S. presidential election. Finally, we conduct an analysis of how heavily concentrated
attention and activity were on the most-engaged-with and most-active accounts.

                                   Descriptive Statistics

        First, we analyze the rate of tweets over time, with the daily count of rumor-related
tweets presented in Figure 3. The most striking feature is the pronounced spike in rumor
circulation surrounding Election Day. Following Election Day, the rate of rumoring sub-
sided quickly, with tweet volume dropping to less than a fifth of its Election Day spike in
approximately 24 hours. By contrast, prior work in 2020, as shown in Figure 4 of (Kennedy
et al., 2022)), demonstrated that election rumors were highly engaged with for multiple
weeks after Election Day.

        We describe the top set of rumors by tweet volume, which is documented in Table
1. As this table illustrates, a significant number of the rumors which were most prevalent
focused on the state of Arizona, prompting us to investigate how the geographic focus of
rumor-related tweets were distributed.

                          Geographic Distribution of Conversation

        Midterm elections are distinct from Presidential elections in that the lack of a pres-
idential candidate on the ballot changes the attention dynamics of election administration-

JQD:DM 5(2025)                                                ElectionRumors2022 17


Figure 3. A timeline plot showing the number of rumor tweets per day in the
dataset. The start of Election Day (November 8, 2022, at 7:00 UTC) is denoted with
a red vertical dashed line.

Schafer & Duskin et al.              Journal of Quantitative Description: Digital Media 5(2025) 18


Table 1: Top rumors by tweet volume. The top two (which account for over 18.5%
of the data volume), and an additional three of the top ten rumors are focused on
Arizona.

      # of Tweets         Rumor ID      Event of Rumor Focus                     AZ Specific
 1    224,384             66            Maricopa machines not scanning           Yes
                                        ballots, Arizona
 2    110,681             129           Kari Lake shares stories of elec-        Yes
                                        tion day voters experiencing is-
                                        sues, Arizona
 3    105,951             106           Ballot counting speed compar-            Yes
                                        isons between Arizona, Florida
 4    62,576              9             Konnech ties to China                    No
 5    58,505              126           Republicans win downballot but           Yes
                                        not gubernatorial race, Arizona
 6    54,905              64            DOJ will observe election in 24          No
                                        states
 7    51,312              44            Graphic showing election winner          Yes
                                        aired early, Arizona
 8    49,315              6             Louis DeJoy in charge of mail-in         No
                                        ballots
 9    48,273              55            Milwaukee elections official fired       No
                                        for election fraud, Wisconsin
 10   45,951              11            30,000 non-citizen voter registra-       No
                                        tion notices, Colorado

JQD:DM 5(2025)                                                             ElectionRumors2022 19


related information. The particular races and candidates at issue are far more variable than
in presidential election years, where voters and the bulk of media attention focus on the
same race. What races are prominent and receive media attention varies significantly across
states, so we were curious to what degree this variance was present in our dataset of false
and misleading rumors.

           We explore the distribution of geographically-focused tweets with two approaches.
First, we use the rumor-level coding to propagate state assignments to tweets. Second,
we search for references to state names and abbreviations in the tweet text, using regular
expressions to find matching substrings. This regular expression search process was also
performed on the dataset from (Kennedy et al., 2022) regarding the 2020 U.S. presidential
election, allowing for comparison. The process used for finding these references is docu-
mented in greater detail in Wack et al. (2023). To be clear, the goal of this process is to
identify relevant geographic locations mentioned within discussions of the rumor topic itself,
not the geographic location of the account posting about the rumor. Table 2 shows the top
eight most-commonly-referenced states by approach.

           As shown in Figure 4, the concentration of narratives on the state of Arizona is far
higher in 2022 than it was in 2020, when the state was only ranked fifth and was mentioned
in less than five percent of tweets directly referencing a state. Additionally, Arizona in 2022
had a higher concentration than any state did in 2020, where the top states of Michigan,
Pennsylvania, and Georgia were far more comparable in terms of rumor volume. We discuss
possible explanations for Arizona’s prominence in election rumoring in a section below, titled
Arizona Rumor Case Studies.

                           Partisan Distribution of Conversation

           To compare partisan splits within the data, we apply a network clustering method
based on audience coengagement (Beers et al., 2023), similar to the approach used in
Kennedy et al. (2022). In brief, we constructed a coengagement projection (Beers et al.,
2023)11 of the full election tweet set (not just those connected to rumors), which identi-

11
     The coengagement projection results in a network where edges represent retweeting by at least
     50 shared audience members between two account nodes, and at least 2 retweets per audience
     member.

Schafer & Duskin et al.          Journal of Quantitative Description: Digital Media 5(2025) 20


Table 2: The distribution of rumor-related tweets referencing U.S. states, as cal-
culated by both rumor-level state labels and by in-tweet references in 2022, and by
in-tweet references in 2020. All states outside of the top eight for a particular year
are bucketed into "Other". Note, the percentages for rumor-level labels are relative
to all tweets, while for direct references they are only relative to all tweets containing
a direct reference to a state.

                 2022 Incidents          2022 References         2020 References
       Rank      State     Percentage    State Percentage        State Percentage
       1         AZ        42.1%         AZ     34.7%            MI     22.0%
       2         General 16.7%           FL     12.9%            PA     21.0%
       3         FL        9.1%          PA     9.7%             GA     18.4%
       4         PA        6.8%          MI     5.7%             TX     5.6%
       5         TX        3.9%          TX     5.3%             AZ     4.7%
       6         MI        3.0%          IN     4.9%             NV     4.6%
       7         MO        2.7%          GA     4.1%             CA     3.9%
       8         WI        2.4%          CO     3.8%             IN     3.4%
       Other               13.4%                19.0%                   16.4%

JQD:DM 5(2025)                                                  ElectionRumors2022 21


Figure 4. Relative distribution of tweets about U.S. states in 2020 and in 2022 by
both direct references through substring searches and rumor-level coding. Each row
is populated by its eight most frequently referenced states, with the rest bucketed
into other. Tweets mentioning multiple states were counted for each state. Note, the
percentages for direct reference searches are relative to the total number of tweets
referencing a state, not the entire dataset.

Schafer & Duskin et al.             Journal of Quantitative Description: Digital Media 5(2025) 22


Table 3: The distribution of posts, rumors, and accounts by their assigned partisan
affiliation.

                Partisanship           Posts          Rumors         Accounts
               Left-Leaning       327,564 (18%)      22 (16%)     125,915 (29%)
               Right-Leaning      1,430,244 (79%)    109 (81%)    262,448 (61%)
               Undetermined        52,833 (3%)        4 (3%)       39,235 (9%)


fied a subset of highly-retweeted, prominent accounts; we then separate these accounts into
clusters using the Louvain method (Blondel et al., 2008). The two large clusters identified
align with the political left and political right, which we verify through manual inspection
of a sample of the accounts in each cluster. This method provides a set of highly retweeted
prominent left-leaning and prominent right-leaning accounts. We then propagate the parti-
san labels of these prominent account clusters out to the rest of the accounts in the dataset,
using retweets as a signal of endorsement. Accounts were marked as likely left-leaning if
over 80% of their retweets of identified prominent accounts were of left-leaning accounts,
and right-leaning if over 80% of their retweets of prominent accounts were of right-leaning
accounts. Users with fewer than 80% of their retweets of prominent accounts or those who
did not retweet any of the prominent accounts linked to a specific partisan cluster were not
designated as partisan-aligned.

        This approach enabled us to assign partisanship labels to 388,363 accounts (91%
of all accounts which account for 97% of all posts in the dataset). We further designate a
rumor as partisan-leaning if a majority (over 50%) of tweets related to that rumor came
from users that partisan label. We find that in total 18% of all tweets and 16% of all rumors
were linked to left-leaning accounts, while 79% of all posts and 81% of all 2022 rumors about
election processes and results were linked to right-leaning accounts.

        As Figure 5 illustrates, the spike in rumoring on Election Day seen in Figure 3 is
present for both groups, but is particularly evident among right-leaning accounts. By the
end of November 2022, most ongoing rumors had dissipated on the platform for both groups.
Partisan differences in rumor-engagement are largely similar to those documented in the
2020 election, with right-leaning accounts showing more activity than left-leaning accounts

JQD:DM 5(2025)                                                    ElectionRumors2022 23


Figure 5. A timeline showing the distribution of tweets authored by users in each
partisan category. For readability, we represented left-leaning account activity with a
downward-facing line, and right-leaning account activity with an upward-facing line.
The vertical dashed line represents the start of Election Day.

Schafer & Duskin et al.           Journal of Quantitative Description: Digital Media 5(2025) 24


Figure 6. A bar graph showing the relative prevalence of tweets in rumors focusing
on Arizona in 2022, grouped by the partisanship of users.


or accounts of undetermined leaning. In this study, we additionally combine the partisan
and geographic analyses which reveals another distinct difference between left-leaning and
right-leaning groups in 2022. As illustrated in 6, a prominent difference is found in the
level of attention given to rumors focused on voting processes and outcomes in the state
of Arizona. Examining engagement of each partisan group separately, we find that over
half of all posts from right-leaning users in our dataset are related to rumors focused on
Arizona (as coded at the rumor level). In contrast, only 14.7% of posts by left-leaning users
focused on that state. This chart also partially explains some of the discrepancies between
partisan groups’ participation in election rumors in 2022. When only looking at tweets
which reference general election rumors about the midterms, or are focused on other states,
we see somewhat closer partisan splits, though there are still more than twice as many posts
from right-leaning accounts than left-leaning accounts.

JQD:DM 5(2025)                                                      ElectionRumors2022 25


                              External Links and Media

       In addition to text-based content, Twitter users may link to external websites or
embed photos, videos, or GIFs in their posts. Users may be motivated to share links with
their audience to inform them of breaking news, to connect with like-minded users or to
seek new information (Holton et al., 2014). In this section, we analyze the prevalence of
posts sharing links to external sources, the diversity and frequency of what domains are
linked to, and note key changes from link sharing behavior during the 2020 presidential
election. We additionally assess the prevalence of embedded media in rumor-related tweets.

       We find that 273,965 (15.13%) of the tweets within the dataset contain links to
external websites. We identify 8,779 unique URLs from 2,057 unique domains (process
described in the “External Links Enrichment" section). Overall, we find that sharing links
is highly skewed toward a few of the most popular sites, with the 10 most popular domains
accounting for more than half (55.75%) of the tweets containing URLs. The most popular
domains, shown in Table 4, were a mix of news sites and government sites, along with one
Republican fundraising platform.

Table 4: Most linked domains in rumor-related tweets. The percentage column
reports the prevalence of each domain in relation to tweets containing an external
link. The bias as listed by Media Bias Fact Check (MBFC)(MBF, 2024) are included
for sources where that information is available.

  Domain                             Tweets    Percent      Type         MBFC Bias
  thepostmillennial.com               45622      14.46      News            Right
  thegatewaypundit.com                32077      10.16      News        Extreme Right
  maricopa.gov                        22721       7.20    Local Gov.
  foxnews.com                         19176       6.08      News            Right
  secure.winred.com                   12678       4.02   Fundraising
  washoelife.washoecounty.gov          9800       3.11    Local Gov.
  dailysignal.com                      9422       2.99      News             Right
  apnews.com                           8188       2.59      News          Left Center
  washingtonpost.com                   8175       2.59      News          Left Center
  justice.gov                          8053       2.55   Federal Gov.

       It is important to note that links to external sites can play a variety of roles in

Schafer & Duskin et al.           Journal of Quantitative Description: Digital Media 5(2025) 26


relation to the rumor they are associated with. In some cases, a linked source is in support
or promotion of the rumor claims, while in other cases an external source is linked to provide
a correction or fact-check. In another scenario linked sources provide a basis of information
that the rumor builds upon. Here, we provide several examples of link-sharing behavior
that highlight how external links serve different purposes.

        First, is a rumor about the discrepancy between Election Day voter turnout and
overall vote totals in Maricopa County, Arizona. The rumor suggests that the fact that
Election Day voting had a low proportion of Democrats, but the Democratic candidate for
governor (Katie Hobbs) received higher overall vote totals indicates Democratic election
malfeasance. In reality, mail-in and early voting trends provide logical explanations as to
why Election Day vote splits do not match overall vote splits. The tweet shown below is
shared directly from the external source (thegatewaypundit.com). In this case, the linked
content is in direct support of the rumor with the article casting the voting statistics as
evidence of nefarious behavior.


      @USERNAME-REDACTED: IMPOSSIBLE: Despite Only 17% Democrat Turnout
      on Election Day - Katie Hobbs and Democrats Are Winning Over 50%
      of Maricopa County Election Day Totals https://t.co/jc7PRrWthy via
      @gatewaypundit


        In a second example, we consider one of the three U.S. government (.gov) sites in
the list of the ten most-shared domains (Table 4). In the case of the maricopa.gov domain,
the vast majority of links to the site were in relation to two rumors surrounding issues
with in-person voting in Maricopa county on Election Day. One of these rumors (further
detailed in Case Study 1) includes general speculation about the delays in vote tabulation.
The other rumor specifically casts doubt on the policy of mitigating the machine issues by
having voters place ballots in a secure drop box (called ‘box 3’ or ‘door 3’) to be counted
later. Several highly retweeted tweets by prominent accounts included links to Maricopa’s
election site that provided information on the location of polling stations. The text of the
tweet supports the rumor that the voting procedures cannot be trusted while the link itself
provides trustworthy information about polling sites. We include one such example below:

JQD:DM 5(2025)                                                        ElectionRumors2022 27


      @kelliwardaz:      BIG problems with @MaricopaVote.           Tabulator “mal-
      functions at at least 6 places.            DO NOT PUT YOUR BALLOT IN “BOX
      3 TO BE “TABULATED DOWNTOWN. Maricopa will not be turning on the
      downtown tabulators today.          Find your next nearest polling place
      here:    http://Maricopa.vote/


       Finally, we show an example where factual reporting about a mistake from Col-
orado’s secretary of state office sparked widespread rumors. In this case, the Associated
Press (AP) published an article about how a postcard encouraging recipients to register to
vote was mistakenly sent to a group of Colorado residents that included a large number of
non-citizens in addition to the U.S. citizens that should have received them. The AP shared
the article, which included reporting on how the error had occurred and clarified that this
did not enable recipients to register unlawfully, on Twitter:


      @AP: Colorado’s secretary of state office says it mistakenly sent
      postcards to about 30,000 noncitizens encouraging them to regis-
      ter to vote, blaming the error on a database glitch related to the
      state’s list of residents with driver’s licenses.
      https://t.co/dXWXDhwo83


       Some users retweeted the AP’s post sharing the article, while other users added their
own commentary via quote-tweeting the original AP tweet or others who shared the same
article. Commentary ranged from criticism of the error, to questioning of circumstances, to
conspiracy theorizing, as seen below.


      Comment 1: @USERNAME-REDACTED: This oopsie could end up costing
      these folks their future citizenship.             This is appalling and out-
      rageous.     Government should take all means possible to inform and
      stop these noncitizens from wrongly casting votes and jeopardiz-
      ing their futures.


      Comment 2: @USERNAME-REDACTED: Do we actually believe this was
      a mistake?

Schafer & Duskin et al.           Journal of Quantitative Description: Digital Media 5(2025) 28


      Comment 3: @USERNAME-REDACTED: Intentional act by a Soros oper-
      ative?


        The above three quote tweets reveal a wider pattern of how rumoring interacts with
news, where quoted tweets contain factual evidence about election-related events, and com-
menting tweets integrate that evidence into false, misleading, or unsubstantiated rumors.
Taken with the other two examples of shared external links, we see how incorporation of
exogenous sources can take a variety of forms in the creation and spread of online rumors.

        When compared to the 2020 election, the sharing of external links in rumor-related
tweets was far less common. In 2022, 15.14% of tweets included a link to an external site,
compared to 30.33% of tweets linking to an external site in the 2020 dataset. However,
the general pattern of skewed attention to a small number of popular domains held in both
cases, as shown in Figure 7 where the a large number of domains receive a very small
cumulative share of tweets and a few popular domains receive the majority of the tweets.
Calculating the Gini coefficient as a summary of how attention (via tweets) is split across
domains, we find that there was only slightly less domain-level inequality in link-sharing in
2022, with the Gini coefficient falling from 0.983 in 2020 to 0.965 in 2022.

        In Table 5 we show the domains with the most marked difference in popularity
between 2020 and 2022. In right-biased news sources, breitbart.com dropped notably
in terms of the proportion of links and thepostmillenial.com, which had essentially no
references during the 2020 election, was the most popular site shared in 2022 election-
related rumors. Interestingly, the official Twitter account for the thegatewaypundit.com
was banned in February of 2021 following violations of Twitter’s then-active civic integrity
policy (Twitter, 2021), and remained off the platform for the duration of the 2022 election
cycle. However, links to the site were still common; it was the second most shared domain
in our dataset despite dropping slightly in relative popularity from 2020. Another notable
change is the decrease in links to YouTube, which represented over 6% of links in 2020 and
less than one percent of links in 2022.

        Twitter enables users to embed photos, videos and GIFs directly in their posts
through the use of the ‘native’ media affordance. Rather than linking to an external site

JQD:DM 5(2025)                                                   ElectionRumors2022 29


Figure 7. Lorenz curve for the popularity of domains shared within rumor or mis-
information related tweets.

Table 5: Domains with the largest change in relative popularity between 2020 and
2022. Change is presented as the raw difference in proportion of tweets linking to the
domain with positive change signifying an increase in popularity and negative values
signifying a decrease.

           domain                        2020   2022 Change
           thepostmillennial.com        0.11% 14.46% +14.35
           maricopa.gov                 0.42% 7.20%   +6.78
           foxnews.com                  0.69% 6.08%   +5.38
           secure.winred.com            0.28% 4.02%   +3.73
           washoelife.washoecounty.gov 0.00% 3.11%    +3.11
           ..                               ..     ..      ..
           inquirer.com                 2.03% 0.02%    -2.01
           nationalfile.com             2.44% 0.01%    -2.43
           thegatewaypundit.co         13.65% 10.16%   -3.49
           breitbart.com                5.50% 0.59%    -4.91
           youtube.com                  6.60% 0.71%    -5.89

Schafer & Duskin et al.            Journal of Quantitative Description: Digital Media 5(2025) 30


Figure 8. Prevalence of embedded media in rumor-related tweets in 2020 and 2022.


that hosts images or videos, users can directly upload media content from their device into
their posts. Shown in Figure 8, we assess the prevalence of these forms of media and find
that more rumor-related posts contained ‘native’ media in 2022 than in 2020, increasing
from 6.52% to 11.54%. This increase in the use of embedded media may help explain the
drop in link sharing, as well as the decrease in links to YouTube, though future research
designed to understand causal impacts, rather than just the descriptive analysis done here,
would be needed to confirm this.

                             Concentration of Engagement

        One of the key findings of (Kennedy et al., 2022) was that original posts from a small
number of heavily retweeted and highly active “repeat spreader" accounts had an outsized
contribution to the overall volume of online discourse around false and misleading narratives
in 2020. Here, we analyze whether a similar level of retweet concentration was present in
2022. The content produced by relatively few users may receive a disproportionately large
amount of engagement through retweets.

JQD:DM 5(2025)                                                        ElectionRumors2022 31


Table 6: Measures of the level of concentration of retweets of a small number of
users among all users, left-leaning users, and right-leaning users. Measurements are
the gini coefficient of retweet counts, the proportion of retweets of the top 1% most
retweeted users, and proportion of retweets of the top 0.1% of users.

                                   gini       top 1% users     top 0.1% users
             year              2020 2022      2020 2022        2020    2022
             All               0.97 0.96      86% 84%          58% 40%
             Left-leaning      0.95 0.95      79% 81%          41% 35%
             Right-leaning     0.97 0.97      86% 85%          58% 41%


       To measure this, we calculated the Gini coefficients for both 2020 and 2022 based
on the number of retweets that each user received. We also compute the proportion of total
retweets for the top 1% most-retweeted users, and the top 0.1% of most-retweeted users,
in both 2020 and 2022. These were calculated in aggregate, as well as for each identified
partisan cluster;results are shown in Table 6. We observe that, overall, election rumors are
highly skewed in their sources toward a relatively small proportion of users. There is no
notable change in overall skew (gini coefficient) for any of the groups between 2020 and
2022, and very minor change in the proportion of retweets of the top 1% most-retweeted
users between election cycles. For both left-leaning users and right-leaning users there is a
drop in terms of the proportion of retweets of the very select few users who make up the
0.1% most retweeted population.

                             Arizona Rumor Case Studies

       In addition to quantitative analyses such as those explored in 5, this dataset can
be useful for mixed-methods and qualitative research on rumoring within elections. In
this section, we feature in-depth mixed-methods analysis of five Arizona-based rumors, a
prominent location in our geographic analysis. First, we provide some brief background to
help explain why the state of Arizona, and in particular the county of Maricopa, were so
salient in our data. Then we conduct an analysis of three particularly high-volume rumors
around the Arizona midterms which received significant attention predominantly in right-
leaning communities. We follow this with an analysis of two lower-volume rumors focused
on Arizona which circulated in left-leaning communities.

Schafer & Duskin et al.               Journal of Quantitative Description: Digital Media 5(2025) 32


                Context for Arizona’s Prominence in Election Discourse

           In recent elections, Arizona has been considered a “purple” or “swing state” with
fairly similar numbers of Republican and Democrat voters. This means that elections in
Arizona are likely to be close, with results potentially impacting the balance of power at
the national level. Close elections correlate with higher uncertainty about outcomes, and
uncertainty is known to lend itself to rumoring (Bordia and DiFonzo, 2005). Additionally,
issues with voting, intentional or not, have the potential to impact the results in close
elections — indicating high relevance of the topic for both sides.

           In 2020, Arizona — and in particular its most populous county, Maricopa County —
became a flashpoint for rumors about election integrity, such as claims about Sharpie pens
invalidating votes (Leingang and Sadeghi, 2020) and the Dominion voting systems 12 (Center
for an Informed Public et al., 2021). A number of Arizona Republican political figures
organized and/or participated in “Stop the Steal” protests after the election (Shepherd and
Knowles, 2020). Several political operatives and lawyers participated in — and were indicted
for — a “fake elector” scheme that attempted to change the results of the presidential
election in Arizona from Biden to Trump (Dev, 2024). In 2021, an unofficial “audit” of
Arizona’s 2020 general election drew national attention and contributed to sustained distrust
in election integrity within the state (Clark, 2022).

           In 2022, gubernatorial candidate Kari Lake promoted theories that elections were
rigged by Democrats, using rhetoric similar to Donald Trump (who endorsed her). Lake
repeatedly criticized election officials, including her gubernatorial opponent, Katie Hobbs,
who was then the Secretary of State of Arizona.

           Going into the 2022 midterm election, this combination of factors likely contributed
to widespread distrust, especially among Republicans, in election integrity. Prior to Elec-
tion Day, false and/or unsubstantiated claims about different elements of the election were
already spreading. Then, on Election Day, real problems with voting across the state com-
bined with existing distrust to catalyze dozens of rumors. Some of those rumors — e.g.

12
     Rumors in 2020 about Dominion Voting systems were prominent in Arizona as well as other swing
     states, including Pennsylvania and Georgia.

JQD:DM 5(2025)                                                        ElectionRumors2022 33


Figure 9. A composite timeline of three AZ rumors illustrating their relative timing
and volume. As seen, the three rumors show peak volume at different points in time,
as well as differences in prominence and longevity.


that voting machines were not working at many locations — were true. But others wove
emerging news about real issues into unsubstantiated conspiracy theories, e.g. alleging that
the problems were an intentional effort to disenfranchise Republican voters.

       In the following sections, we describe three related rumors, which primarily spread in
right-leaning communities, that emerged from Maricopa County on and after Election Day.
These case studies demonstrate the utility of the described dataset for thorough qualitative
work in addition to quantitative methodologies. In Figure 9, we show a timeline of the
relative timing and prevalence of these three rumors. Individual timelines for each specific
rumor are shown in Figures 10, 11, and 12 to provide more detail. We then briefly document
rumor spread about AZ election administration within left-leaning communities.

Schafer & Duskin et al.                 Journal of Quantitative Description: Digital Media 5(2025) 34


Figure 10. A temporal plot showing the number of tweets per minute related to
the Arizona tabulator errors rumor. Note, unlike the other case study plots, we use a
y-axis of tweets per minute here, not per hour, to get a better sense of volume shifts
as this rumor had a shorter lifespan than the other cases.


                          Case Study 1: Tabulators not functioning

           On Election Day in Arizona, issues with ballots scanners began to occur very early,
with reports that scanners were not accepting ballots as early as 6:20 AM local time (Mari-
copa County Elections Department, 2022). Conversation on Twitter began with some lim-
ited uncertainty whereby members of the online audience and some Twitter influencers
began posting as they described what they knew. For example, one of the earliest highly
spread tweets (4,138 retweets) in our dataset came from conservative political operative and
COO of Turning Point USA Tyler Bowyer13 :

13
     Bowyer is one of eleven allegedly fraudulent electors in Arizona who have been indicted for falsely
     certifying Donald Trump as the winner of the 2020 election in Arizona (Barchenger, 2024).

JQD:DM 5(2025)                                                             ElectionRumors2022 35


         @tylerbowyer14 :      Long lines in Anthem, Arizona with Poll Workers
         explaining that the @maricopacounty machines are not working.                      Do
         not get out of line!


           Bowyer’s tweet embedded a video of a poll worker addressing a long line of voters,
describing the issues the polling center was experiencing while also capturing the palpable
frustration and skepticism of voters waiting in line. Although Bowyer’s tweet primarily
shared information about the emerging voting difficulties in Maricopa, members of the
online audience commented on the tweet suggesting that the voting issues were evidence
of fraud. For example, the following comments were made in response to Bowyer’s tweet
through the quote tweet affordance:


         Comment 1: @USERNAME-REDACTED: I told yall.                People looked at me
         crazy.     But I told yall, to have a plan.            Also, that if they are
         going to manipulate, they will do it on election day when all yall
         are going to vote.        The day you have your only chance to vote.


         Comment 2: @USERNAME-REDACTED: @RecordersOffice You people shouldn’t
         be allowed to hold elections in your county.                 Imagine expecting
         us to believe this isn’t intentional.              Couldn’t get away with the
         sharpies again?


         Comment 3: @USERNAME-REDACTED: The steal is on where are the At-
         torneys and the non-biased poll watchers


           In each of the above comments, the commenter suggests that the election issues are
evidence of a larger, intentional plan. Additionally, Comment 1 uses the fact that as rates
of mail-in voting have risen in recent elections, Republican voters have voted dispropor-
tionately on Election Day to suggest the errors are targeted while Comment 2 refers to a
previous, false rumor from 2020 in Maricopa County. Specifically, the rumor suggested that
14
     In this and subsequent tweets, we have deleted excessive whitespace that made the manuscript
     unreadable, and added punctuation in brackets if necessary to convey the appropriate meaning.

Schafer & Duskin et al.            Journal of Quantitative Description: Digital Media 5(2025) 36


Sharpies were being intentionally distributed to invalidate conservative ballots (Shepherd
and Knowles, 2020).

        That video and other similar ones were shared in the early hours of rumoring. Initial
posts sharing the videos were often fairly neutral in tone, but the videos themselves showed
voters who were frustrated and skeptical of the tabulator issues. For example, the most
retweeted tweet (with 14,719 retweets in our dataset) within this rumor came from Charlie
Kirk, conservative influencer and founder of Turning Point USA, where he embeds the same
video Bowyer had shared just minutes earlier:


      @charliekirk11:               A poll worker in all-important Maricopa
      County tells Election Day voters the machines are broken.


        Other than calling attention to Maricopa County’s political importance, Kirk’s tweet
is fairly neutral in tone and mainly communicates part of an evolving situation using a video
that highlights the frustration and skepticism of voters waiting in line. As the poll worker
describes the issues, he states that “no one is trying to deceive” and is interrupted by
sarcastic commentary from the person recording the event, as well as general groans from
those waiting in line. In addition, one voter leaves the line, saying explicitly that they do
not trust putting their ballot into the box that is set aside for votes to be tabulated later
in the event of machine failure.

        Although Kirk’s tweet above is relatively neutral at face value, the online audience
did not interpret it as such, nor did Kirk and other conservative influencers and political
elites shy away from more conspiratorial framing in subsequent discourse. For example, in
a tweet quoting Kirk’s above tweet, one audience member associates the ongoing tabulator
issues with rumors of election fraud in 2020 (known colloquially as the “Big Lie”):


      @USERNAME-REDACTED: Preparing for the BIG LIE all over again.                       Ex-
      plain what’s happening here if they don’t plan to cheating?                      Just
      so happens tabulators aren’t working in AZ?


        Similarly, in a later tweet, Kirk refers to the tabulator issues as “manufactured

JQD:DM 5(2025)                                                          ElectionRumors2022 37


chaos” and suggests that the resulting lines amount to voter suppression, calling for people to
be arrested. This conspiratorial framing was echoed by audiences, influencers, and political
elites alike. For example, the seventh most retweeted tweet in the incident (with 6,372
retweets) came from Senator Ted Cruz, who insinuated that then-Secretary of State and
Democratic gubernatorial candidate Katie Hobbs was somehow intentionally responsible for
the tabulator issues:


      @tedcruz:      So, the Dem nominee for governor (who refused to de-
      bate her opponent) is the current Secretary of State – in charge
      of running this election – and now...              there are problems?
      #DemsHateDemocracy


       In addition to suspicion around the origin of the errors, online audiences also ex-
pressed skepticism as to the reliability of remedies. Maricopa County had backups in place
in case of failures like those experienced on Election Day, and in the case of 2022 there was
a box on the machines (labeled with the number 3 and referred to as “Box 3”) where voters
were directed to drop their ballots if they were not able to be scanned. However, many
members of the online audience expressed skepticism as to whether vote in Box 3 would
be accurately recorded. For example, the following tweet insinuates that ballots counted
“downtown” won’t be counted due to corruption:


      @USERNAME-REDACTED Reports of machines not accepting ballots, and
      that those ballots will be taken "Downtown"...                 right.     Maricopa
      is as corrupt as they come, and y’all aren’t even trying to hide
      it anymore.


       It is important to note that although conspiratorial framing was a major part of
the rumoring as it occurred on Twitter, there were many users who simply noted how
frustrating the widespread machine failures were but didn’t make accusations about fraud.
In particular, they highlighted the unpreparedness of the election infrastructure and/or
administrators, often describing the failures as the result of incompetence with sentiments
similar to the tweet below:

Schafer & Duskin et al.           Journal of Quantitative Description: Digital Media 5(2025) 38


      @USERNAME-REDACTED Monday:          Two hour press conference, everything
      is fine in Maricopa, we know what we’re doing.                 Tuesday:     Our ma-
      chines are broken and we don’t know why, but trust our contingency
      plan.     Incompetence is not fraud, but come on with this shit.


        Taken together, rumoring on Election Day surrounding tabulator failures was founded
on very real issues with election infrastructure. These issues were then used as evidence to
support interpretations ranging from suggestions of benign incompetence to claims that the
problems were intentional voter fraud perpetrated by Democrats. In support of the con-
spiratorial interpretation, audiences and influencers highlighted: 1) how more Republicans
were voting in person on Election Day than Democrats and were therefore more impacted
by machine failures; 2) that the Democratic gubernatorial candidate was acting Secretary
of State during her election, insinuating a conflict of interest; 3) that the provided remedy
of Box 3 was an attempt to manipulate votes offsite; and 4) that the resulting long lines
disenfranchised conservative voters.

                          Case Study 2: Ballot counting speed

        The second incident we examine surrounds rumoring suggesting that counting bal-
lots slowly is suspicious and allows for the Democratic manipulation of votes. In particular,
the rumors center around a comparison between the counting of votes in Florida versus
in Arizona. Other states are visible in the data, but the vast majority of tweets compare
Florida and Arizona, insinuating that it is suspicious that Florida can finish counting bal-
lots more quickly than Arizona despite having many more ballots to count. For example,
conservative influencer Tim Young (@TimRunsHisMouth) posted the following tweet:


      @TimRunsHisMouth:       Florida not only had millions more ballots to
      count than Arizona...         but the state was also prepping for a hur-
      ricane at the same time AND got the counting done in hours.
      What’s Arizona’s excuse?


        The above tweet highlights the difference in both counting speed and number of
ballots counted between Arizona and Florida, insinuating that it is suspicious for there to

JQD:DM 5(2025)                                              ElectionRumors2022 39


Figure 11. A temporal plot showing the number of tweets per hour related to the
Arizona ballot counting speed rumor.

Schafer & Duskin et al.           Journal of Quantitative Description: Digital Media 5(2025) 40


be discrepancies. One of the primary reasons that Arizona counted votes more slowly was
that voters changed their behavior regarding mail-in ballots; there were over 290,000 mail
in ballots dropped off on Election Day (rather than mailing them in prior) in Arizona in
2022, more than a 70% increase than the number received in 2020 (Fifield, 2022). This may
have occurred due to increased skepticism of the security of mail-in voting in general, and
ballot drop boxes in particular in Arizona, which saw large amounts of rumoring suggesting
“ballot mules” were using drop boxes for fraud in the lead up to the 2022 general election
(Prochaska et al., 2022).

        Similar rumors circulated in 2020 as well, and largely converged on interpretations
that ballots were intentionally counted slowly so that Democrats could “find” ballots to
allow them to fraudulently win close elections. The incident in 2022 was similar, with
many members of the online audience interpreting the delayed counts as an opportunity for
election malfeasance, an example of which is visible below:


      @USERNAME-REDACTED: #Arizona is just corrupt to the core.                    #Kar-
      iLake has obviously won, yet they are desperately searching for
      more magical ballots from under tables, just like we saw in 2020.
      @KariLake is an enormous threat to the establishment and will im-
      prove Arizona greatly.Don’t let her down

      Quoted tweet: @EndWokeness:        North Carolina:        98% counted [,] Pop-
      ulation:      10.5 million [.]Wisconsin:         99% counted [,] Population:
      5.2 million [.]       Florida:     99% counted [,] Population:           22 mil-
      lion [.]      Ohio:   97% counted [,] Population:           12 million [.]       Ari-
      zona:     66% counted [,] Population:          1.6 million


        Above, it is clear that the commenter interpreted the speed of counting as evidence
of corruption that allegedly occurred in both 2020 and 2022. Similar to the incidents
described above, interpretations ranged from viewing the slow counting as evidence of fraud
to suggestions that those claiming fraud were just trying to sow doubt about electoral
processes. Between the two were some members of the audience who didn’t necessarily view
the slow counting as fraud, but instead viewed it as evidence that the election processes in
Arizona were a mess and needed to be reevaluated.

JQD:DM 5(2025)                                                        ElectionRumors2022 41


Figure 12. A temporal plot showing the number of tweets per hour related to the
anecdotes posted by Kari Lake.


                         Case Study 3: Kari Lake anecdotes

       One of the primary reasons that Maricopa County, and Arizona in general, was
likely a hotbed for electoral rumoring was because of the endorsement of election denialism
by candidates running for office. Most notable of this group was Republican gubernatorial
candidate Kari Lake. Although Lake participated in numerous rumors on Twitter to varying
degrees, the final incident examined here is focused on a subset of tweets coming from Kari
Lake’s account (@KariLake) or her campaign’s account (@KariLakeWarRoom).

       The primary behavior visible in these tweets was the amplification of individual
voters’ experiences on Election Day in the form of comments based on accompanying em-
bedded videos from voters. The stories shared often included statements implicitly referring
to previous rumors surrounding what has become known as the “Big Lie” and connecting

Schafer & Duskin et al.           Journal of Quantitative Description: Digital Media 5(2025) 42


them to the events on the ground in 2022. For example, in her most retweeted tweet, Lake
amplifies the alleged experience of the son of a voter who ran into trouble voting:


      @KariLake:      After registering at ASU, Tiffany’s son received a text
      offering him $250 to rally for Democrats In line to vote, he was
      told to leave & that his vote would not be counted [.]                   Inside,
      he was told he was not registered, given a Sharpie, & told to drop
      a provisional ballot in box 3.


        In this tweet, several themes are visible. First, Lake, pulling claims from the em-
bedded video of a woman describing the experience of her son, claims that Democrats (the
primary villains in rumors surrounding the Big Lie) offered money to “rally for Democrats.”
Second, this was followed by the claim that the long lines catalyzed by the tabulator failures
described above resulted in poll workers asking voters to leave, allegedly because he, and
others, would be unable to vote by the deadline of 7:00 PM. Lastly, Lake highlights that
poll workers tried to give the son a Sharpie to fill out his ballot, referencing the previous
rumor from 2020.

        In addition to the content, the style of the above tweet and most of Lake’s tweets in
this incident is important — Lake makes few direct claims herself, instead relying on tes-
timony from voters to interpret emergent events within a frame of voter fraud established
in 2020 and amplified by Lake throughout her campaign in 2022. This process is described
in more detail in other works (Starbird et al., 2023; Prochaska et al., 2023), but at its core
consists of establishing an expectation within conservative voters that Democrats will per-
petrate fraud, which then causes audiences to organically organize and interpret otherwise
ambiguous information as “evidence” of fraud instead of something more mundane such as
an error in election administration. This “evidence” is amplified online, providing “proof”
that is strategically amplified by political elites and influencers to support the ongoing
conversations surrounding alleged voter fraud in U.S. elections.

        Seen from this perspective, the rumors spread are the product of an informal col-
laboration between political elites, influencers, and members of the public, all of whom play
integral roles in the production and spread of rumors online. Although many members of

JQD:DM 5(2025)                                                         ElectionRumors2022 43


the public participate in the production and dissemination of these rumors, the interpreta-
tions of Lake’s tweets are not uniform. Within this incident, interpretations of Lake’s tweets
ranged from explicitly viewing the shared anecdotes as evidence of fraud to suggestions that
the videos are evidence of the negative consequences of misleading rhetoric, visible in the
example below:


      @USERNAME-REDACTED: Here’s Larry’s story, fresh from Kari Lake.
      Larry’s story is genuinely sad.            So spun up on Big Lie bullshit
      conspiracy theories he apparently refused to submit to put his bal-
      lot in the ballot box because he thought it would be thrown away.

      Quoted tweet: @KariLake:         It took Larry an hour & a half to get
      into his polling location [.]           Inside, Larry’s ballot was repeat-
      edly rejected by the tabulator.            He was asked to put it in box
      three so it could be counted downtown.              He refused.      Because he
      felt it meant they would throw his vote in the trash.


       In the above tweet, the poster highlights how election skepticism on the part of voters
caused them to doubt the remedy in place in Maricopa County for tabulator issues, namely
the use of “Box 3” for ballots to be counted at a separate location in the event of machine
issues. Although there were a noticeable number of responses countering interpretations of
the anecdotes, those interpreting them as evidence of fraud or disenfranchisement were more
prominent. Within these responses, users often utilized other related rumors to support
their interpretations, including suggestions that Katie Hobbs is too biased to be relied on
as Secretary of State, claims that noncitizen voters were voting illegally, that errors on
Election Day were intentional, and that swing states are the primary targets for Democrat-
led voter fraud.

                   Case Studies 4 and 5: Left-leaning Arizona rumors

       As previously shown in our partisanship and geographic analysis sections, rumoring
within Arizona was much more prevalent within right-leaning communities on Twitter than
within left-leaning communities. Of rumors focusing on the state, only two primarily spread
in left-leaning communities. It is worth noting that not only were there less Arizona-related

Schafer & Duskin et al.           Journal of Quantitative Description: Digital Media 5(2025) 44


Figure 13. A temporal plot showing the number of tweets per hour related to both
primarily left-leaning rumors focused on the state of Arizona.


among left-leaning communities, these rumors also attained much smaller overall volumes
than many in right-leaning communities; these two left-coded rumors had 12.2K and 7.8K
tweets associated with them, while each of the three previous, right-coded case studies had
over 100K tweets each. As a result, we cover the two left-coded rumors in one brief section
here, and illustrate their composite spread in Figure 13.

        The first of these two rumors, labeled "Scammers collecting ballots" in Figure 13,
centered around unsubstantiated claims alleging that scammers were going around neigh-
borhoods claiming they were Democrats, offering to take voters’ ballots to drop them off,
and then discarding them. A significant volume of tweets spreading this rumor were con-
nected to a post from @azld12dems, the account of the local Democratic organizing group.

JQD:DM 5(2025)                                                         ElectionRumors2022 45


      @azld12dems:          WARNING: FAKE DEMOCRATS. There are scammers claim-
      ing to be Dems going door to door in our district, offering to take
      ballots & turn them in.           THIS IS A SCAM. NO Dems from ADP, MCDP,
      or LD12 Dems are doing this.           Don’t fall for this.         Authorities
      are being informed.


       This rumor, however, did not get significant additional pickup from statewide or
national left-leaning representatives, likely limiting the engagement it received.

       The second rumor focused on claims that the Church of Jesus Christ of Latter-day
Saints (colloquially known as the Mormon church) was organizing "ballot parties" for their
members. This rumor was also unsubstantiated, and denied by all local wards of the Church
(Lee and Bates, 2022). The vast majority of retweet volume focused on one initial tweet
from a relatively small, anonymous account, which according to (Lee and Bates, 2022) "did
not have any additional information about the rumor besides what was in her two tweets."

       Both the empirical partisan analysis and the Arizona case studies corroborate recent
research on the partisan asymmetries in the spread of low-quality or untrustworthy infor-
mation on social media (Mosleh et al., 2024; González-Bailón et al., 2023). Interestingly,
we notice that the two Arizona-focused rumors on the left spread prior to the election,
rather than on Election Day or in the following weeks, when the top right-leaning rumors
described earlier were primarily spreading. Since the results of prominent races in the state,
in particular the U.S. Senate race and the gubernatorial race, were both won by Democratic
candidates, left-leaning communities would have had less incentive to engage in delegitimiz-
ing rumoring after the results were known. We encourage future work in investigating if
this pattern holds in other cases.

                                     Case study summary

       In the above five cases, we have illustrated a selection of prominent rumors which
spread during the 2022 midterms about the election in Arizona. These showed a variety
of communicative and discursive practices being deployed to facilitate the spread of these
rumors, including differences in tone between influential amplifiers and their audience (Case
1) and the elevation and generalization of anecdotes (Case 3). These cases illustrate the

Schafer & Duskin et al.            Journal of Quantitative Description: Digital Media 5(2025) 46


need for further qualitative work on election rumor discourses in future research.

                                         Limitations

        This dataset attempts to comprehensively cover English-language tweets about false,
misleading, and/or unsubstantiated rumors about the election process of the 2022 U.S.
midterm elections. However, this scoping means that there are aspects of closely-related
questions this dataset should not be used to address. Notably, it does not include non-
English language rumors, nor rumors about candidates that are not tied to election pro-
cesses. Discussions of rumors on platforms other than Twitter are not captured, as data
collection access prevents coverage of other platforms with the same level of comprehen-
siveness. A further form of data missing is rumors which spread primarily through images
with no (or minimal) in-text keywords. Additionally, this dataset, as it is focused on dis-
cussions of false and misleading rumors specifically, should not be used for more general
analyses of broad political discussions during this time, as large parts of political discourses
are unaffiliated with the kinds of rumors examined in this paper.

                                         Conclusion

        In this paper, we have documented the collection, curation, and preliminary descrip-
tive analysis of a dataset of 1.81 million election administration-related rumors on Twitter
posted around the 2022 U.S. midterms. This data contributes to research into online ru-
moring around elections by looking into a comparatively under-studied midterm election
process rather than presidential elections. After providing detailed documentation of the
process for ensuring the reliability of the dataset, we conducted five descriptive analyses
of this data, exploring overall tweet frequency, geographic and partisan distributions, the
prevalence of external link-sharing, and the highly concentrated nature of attention to a
small number of users. We follow this with mixed-methods case studies of three prominent
rumors about election issues in Arizona, highlighting how this dataset could be used for
both qualitative and mixed-methods future research in addition to the quantitative research
styles contained in this paper. The anonymized data that is publicly available may be used
in conjunction with other public datasets, or to observe structural patterns of the identified
rumors. The hydrated data (available upon reasonable request or collaboration) opens up
even more avenues of research.

JQD:DM 5(2025)                                                          ElectionRumors2022 47


       Our findings collectively demonstrate several interesting features of the dynamics of
rumoring during the midterm elections, and how these have changed since 2020 (Kennedy
et al., 2022). We do not make causal claims about these shifts, but observe several changes
including much higher concentration on one particular state and lower prevalence of content
linking to external domains. At the same time, we observe a similar partisan asymmetry
to what (Kennedy et al., 2022) found in 2020, particularly concentrated in Arizona, and
similar levels of retweet concentration.

       The spread of rumors online has been an area of ongoing interest for research and
for society at large, and understanding the spread of rumors in the context of democratic
elections is especially important. This dataset can help support research in this area by
providing a wide-ranging overview of rumors that spread within this U.S. election context.

       This dataset could inform research which seeks to understand more granular levels
of rumor spread. For example, research into rumor spread in Arizona during the midterms
could take the dataset as a starting point for areas to further investigate. Other studies of
Twitter content in this period could also use this dataset to understand if and how prevalent
these rumors are within their own observations or data. For example, algorithmic audits
of Twitter conducted during the election period, such as (Duskin et al., 2024), could use
this dataset to estimate the frequency that observed election rumors are shown to Twitter
accounts.

       Our dataset of 1.81 million posts related to discussions of false, misleading, or unsub-
stantiated rumors surrounding the 2022 U.S. midterm elections on the Twitter/X platform
provides a thoroughly scoped and curated view of these kinds of discussions on the platform
at the time. This will provide utility to researchers seeking to conduct further research on
these topics, as well as increase our understanding of election rumor discussions from our
empirical findings.

                                    Ethical statement.

       This data was determined by the Human Subject Division at the University of
Washington not to involve human subjects, as defined by federal and state regulations and
therefore, did not require review and approval by the IRB. In accordance with Twitter’s

Schafer & Duskin et al.            Journal of Quantitative Description: Digital Media 5(2025) 48


Terms of Service at the time of collection, the only data that we released which came from
the platform are user IDs and tweet IDs - this does not include tweet text, usernames, media,
or other fields - and in fact we only release pseudonymized versions of the user IDs. Since
the removal of the free research API by Twitter (now X) has made rehydrating potentially
more difficult for researchers, we will make the hydrated data available to researchers upon
reasonable request, similar to prior datasets such as (Aiyappa et al., 2023). In this paper,
analysis of inferred political leaning was conducted at an aggregated community level, which
is in line with prior work (see for examples, (Abilov et al., 2021; Beers et al., 2023; Sharma
et al., 2022)).

        Similarly to (Giorgi et al., 2022), we consider the ethical questions in Datasheets for
Datasets (Gebru et al., 2021). While we did not get users’ consent to collect these data, this
is consistent with substantial amounts of prior work on public Twitter posts, and by only
providing user ID and tweet ID numbers, users who wish to have their content anonymized
can delete their data from the platform and this would not be rehydratable. This is similar
to other published datasets, including those related to similarly sensitive political topics,
such as (Abilov et al., 2021; Aiyappa et al., 2023).

                                    Acknowledgments

        Funding for this work has come from the University of Washington’s Center for
an Informed Public, the John S. and James L. Knight Foundation (G-2019-58788), Craig
Newmark Philanthropies, the William and Flora Hewlett Foundation, the Election Trust
Initiative, the National Science Foundation (grant #1749815 and grant #2120496) and NSF
Graduate Research Fellowships under Grant No DGE-2140004, for both Joseph S. Schafer
and Kayla Duskin. Any opinions, findings, conclusions, or recommendations expressed in
this material are those of the authors and do not necessarily reflect the views of the National
Science Foundation or other funders. We would also like to acknowledge Alex Loddengaard
for their infrastructural support for this project, and Kristen Engel and Ben Yamron for
feedback on sections of the writing of this paper.

JQD:DM 5(2025)                                                          ElectionRumors2022 49


                                         References

(2024). Media bias/fact check. https://mediabiasfactcheck.com/.

Abilov, A., Hua, Y., Matatov, H., Amir, O., and Naaman, M. (2021). VoterFraud2020: a
       multi-modal dataset of election fraud claims on twitter. ICWSM, 15:901–912.

Aiyappa, R., DeVerna, M. R., Pote, M., Truong, B. T., Zhao, W., Axelrod, D., Pessianzadeh,
       A., Kachwala, Z., Kim, M., Seckin, O. C., Kim, M., Gandhi, S., Manikonda, A.,
       Pierri, F., Menczer, F., and Yang, K.-C. (2023). A Multi-Platform collection of
       social media posts about the 2022 U.S. midterm elections. ICWSM, 17:981–989.

Akbar, S. Z., Panda, A., and Pal, J. (2022). Political hazard: misinformation in the 2019
       indian general election campaign. South Asian History and Culture, 13(3):399–417.

Anthony, S. (1973). Anxiety and rumor. The Journal of social psychology, 89(1):91–98.

Arif, A., Robinson, J. J., Stanek, S. A., Fichet, E. S., Townsend, P., Worku, Z., and Starbird,
       K. (2017). A closer look at the self-correcting crowd: Examining corrections in
       online rumors. In Proceedings of the 2017 ACM conference on computer supported
       cooperative work and social computing, pages 155–168.

Arif, A., Shanahan, K., Chou, F.-J., Dosouto, Y., Starbird, K., and Spiro, E. S. (2016). How
       Information Snowballs: Exploring the Role of Exposure in Online Rumor Propaga-
       tion. In Proceedings of the 19th ACM Conference on Computer-Supported Cooper-
       ative Work & Social Computing, CSCW ’16, pages 466–477, New York, NY, USA.
       Association for Computing Machinery.

Bak-Coleman, J. B., Alfano, M., Barfuss, W., Bergstrom, C. T., Centeno, M. A., Couzin,
       I. D., Donges, J. F., Galesic, M., Gersick, A. S., Jacquet, J., Kao, A. B., Moran,
       R. E., Romanczuk, P., Rubenstein, D. I., Tombak, K. J., Van Bavel, J. J., and
       Weber, E. U. (2021). Stewardship of global collective behavior. Proc. Natl. Acad.
       Sci. U. S. A., 118(27).

Barberá, P., Jost, J. T., Nagler, J., Tucker, J. A., and Bonneau, R. (2015). Tweeting
       from left to right: Is online political communication more than an echo cham-

Schafer & Duskin et al.           Journal of Quantitative Description: Digital Media 5(2025) 50


        ber?: Is online political communication more than an echo chamber?            Psychol.
        Sci., 26(10):1531–1542.

Barchenger, S. (2024). Grand jury indicts fake electors who falsely certified Donald Trump
        as 2020 winner in Arizona.

Beers, A., Schafer, J. S., Kennedy, I., Wack, M., Spiro, E. S., and Starbird, K. (2023).
        Followback clusters, satellite audiences, and bridge nodes: Coengagement networks
        for the 2020 US election. Proceedings of the International AAAI Conference on Web
        and Social Media, 17:59–71.

Blondel, V. D., Guillaume, J.-L., Lambiotte, R., and Lefebvre, E. (2008). Fast unfolding
        of communities in large networks. Journal of Statistical Mechanics: Theory and
        Experiment, 2008(10):P10008.

Bordia, P. and DiFonzo, N. (2005). Psychological Motivations in Rumor Spread. In Rumor
        Mills. Routledge. Num Pages: 16.

Bovet, A. and Makse, H. A. (2019). Influence of fake news in twitter during the 2016 US
        presidential election. Nat. Commun., 10(1):1–14.

Calo, R., Coward, C., Spiro, E. S., Starbird, K., and West, J. D. (2021). How do you solve
        a problem like misinformation? Sci Adv, 7(50):eabn0481.

Center for an Informed Public, Digital Forensic Research Lab, Graphika, and Stanford
        Internet Observatory (2021). The Long Fuse: Misinformation and the 2020 Election.
        Stanford Digital Repository: Election Integrity Partnership., v1.3.0 edition.

Chen, E., Deb, A., and Ferrara, E. (2022). #Election2020: the first public Twitter dataset
        on the 2020 US Presidential election. Journal of Computational Social Science,
        5(1):1–18.

Chen, W., Pacheco, D., Yang, K.-C., and Menczer, F. (2021). Neutral bots probe political
        bias on social media. Nat. Commun., 12(1):5580.

Clark, D. (2022). Cyber Ninjas, company that led Arizona GOP election ’audit,’ is shutting
        down.

JQD:DM 5(2025)                                                       ElectionRumors2022 51


Deb, A., Luceri, L., Badaway, A., and Ferrara, E. (2019). Perils and challenges of social
       media and election manipulation analysis: The 2018 US midterms. In Companion
       Proceedings of The 2019 World Wide Web Conference, WWW ’19, pages 237–247,
       New York, NY, USA. Association for Computing Machinery.

Dev, S. (2024). 18 indicted in alleged 2020 fake Arizona elector scheme tied to Trump, AG
       announces.

Doerr, B., Fouz, M., and Friedrich, T. (2012). Why rumors spread so quickly in social
       networks. Communications of the ACM, 55(6):70–75.

Duskin, K., Schafer, J. S., West, J. D., and Spiro, E. S. (2024). Echo Chambers in the Age
       of Algorithms: An Audit of Twitter’s Friend Recommender System.

Fifield, J. (2022). Why Arizona’s ballot count takes longer than Florida’s.

Freelon, D. and Wells, C. (2020). Disinformation as political communication. Political
       Communication, 37(2):145–156.

Gebru, T., Morgenstern, J., Vecchione, B., Vaughan, J. W., Wallach, H., Iii, H. D., and
       Crawford, K. (2021). Datasheets for datasets. Commun. ACM, 64(12):86–92.

Giorgi, S., Guntuku, S. C., Himelein-Wachowiak, M., Kwarteng, A., Hwang, S., Rahman,
       M., and Curtis, B. (2022). Twitter corpus of the #blacklivesmatter movement and
       counter protests: 2013 to 2021. ICWSM, 16:1228–1235.

González-Bailón, S., Lazer, D., Barberá, P., Zhang, M., Allcott, H., Brown, T., Crespo-
       Tenorio, A., Freelon, D., Gentzkow, M., Guess, A. M., Iyengar, S., Kim, Y. M.,
       Malhotra, N., Moehler, D., Nyhan, B., Pan, J., Rivera, C. V., Settle, J., Thorson,
       E., Tromble, R., Wilkins, A., Wojcieszak, M., de Jonge, C. K., Franco, A., Mason,
       W., Stroud, N. J., and Tucker, J. A. (2023). Asymmetric ideological segregation
       in exposure to political news on Facebook. Science, 381(6656):392–398. Publisher:
       American Association for the Advancement of Science.

Green, J., Hobbs, W., McCabe, S., and Lazer, D. (2022). Online engagement with 2020
       election misinformation and turnout in the 2021 georgia runoff election. Proc. Natl.
       Acad. Sci. U. S. A., 119(34):e2115900119.

Schafer & Duskin et al.               Journal of Quantitative Description: Digital Media 5(2025) 52


Holton, A. E., Baek, K., Coddington, M., and Yaschur, C. (2014). Seeking and sharing:
        Motivations for linking on twitter. Communication research reports, 31(1):33–40.

Jack, C. (2017). Lexicon of lies: Terms for problematic information. Technical report, Data
        & Society Research Institute.

Jones-Jang, S. M., Kim, D. H., and Kenski, K. (2021). Perceptions of mis- or disinformation
        exposure predict political cynicism: Evidence from a two-wave survey during the
        2018 US midterm elections. New Media & Society, 23(10):3105–3125.

Kennedy, I., Wack, M., Beers, A., Schafer, J. S., Garcia-Camargo, I., Spiro, E. S., and
        Starbird, K. (2022). Repeat spreaders and election delegitimization. Journal of
        Quantitative Description: Digital Media, 2.

Le, H., Shafiq, Z., and Srinivasan, P. (2017). Scalable news slant measurement using twitter.
        In Proceedings of the International AAAI Conference on Web and Social Media,
        volume 11, pages 584–587.

Lee, J. and Bates, S. (2022). Debunking a rumor of election fraud by a Latter-day Saint
        congregation in Tucson, Arizona. Deseret News. Section: Politics.

Leingang, R. and Sadeghi, M. (2020). Fact check: Arizona election departments confirm
        Sharpies can be used on ballots.

Maricopa       County     Elections    Department       (2022).         Maricopa     county     re-
        sponse.                   https://www.maricopa.gov/DocumentCenter/View/80026/
        Maricopa-County-Response-11-27-2022.

Mendoza, G. A. S., Ballar, K. J., Yap, J. K., and Deinla, I. B. (2023). Accuracy or
        confidence? analyzing the impact of online misinformation on filipino youth voting
        likelihood. Media Asia, pages 1–19.

Moran, R. E., Grasso, I., and Koltai, K. (2022). Folk Theories of Avoiding Content Modera-
        tion: How Vaccine-Opposed Influencers Amplify Vaccine Opposition on Instagram.
        Social Media + Society, 8(4):20563051221144252. Publisher: SAGE Publications
        Ltd.

JQD:DM 5(2025)                                                        ElectionRumors2022 53


Mosleh, M., Martel, C., Eckles, D., and Rand, D. G. (2021). Shared partisanship dramati-
       cally increases social tie formation in a twitter field experiment. Proc. Natl. Acad.
       Sci. U. S. A., 118(7).

Mosleh, M. and Rand, D. G. (2022). Measuring exposure to misinformation from political
       elites on twitter. Nat. Commun., 13(1):7144.

Mosleh, M., Yang, Q., Zaman, T., Pennycook, G., and Rand, D. G. (2024). Differences in
       misinformation sharing can lead to politically asymmetric sanctions. Nature, pages
       1–8. Publisher: Nature Publishing Group.

Nikolov, D., Flammini, A., and Menczer, F. (2021). Right and left, partisanship predicts
       (asymmetric) vulnerability to misinformation. HKS Misinfo Review.

Oehmichen, A., Hua, K., López, J. A. D., Molina-Solana, M., Gómez-Romero, J., and
       Guo, Y.-K. (2019). Not all lies are equal. a study into the engineering of political
       misinformation in the 2016 US presidential election. IEEE Access, 7:126305–126314.

Palen, L., Vieweg, S., Sutton, J., Liu, S. B., and Hughes, A. (2007). Crisis informat-
       ics: Studying crisis in a networked world. In Proceedings of the third international
       conference on E-Social Science, pages 7–9.

Pendleton, S. C. (1998). Rumor research revisited and expanded. Language & Communi-
       cation, 18(1):69–86.

Pfeffer, J., Mooseder, A., Lasser, J., Hammer, L., Stritzel, O., and Garcia, D. (2023). This
       Sample Seems to Be Good Enough! Assessing Coverage and Temporal Reliability
       of Twitters Academic API. Proceedings of the International AAAI Conference on
       Web and Social Media, 17:720–729.

Prochaska, S., Duskin, K., Kharazian, Z., Minow, C., Blucker, S., Venuto, S., West,
       J. D., and Starbird, K. (2023). Mobilizing Manufactured Reality: How Participa-
       tory Disinformation Shaped Deep Stories to Catalyze Action during the 2020 U.S.
       Presidential Election. Proceedings of the ACM on Human-Computer Interaction,
       7(CSCW1):140:1–140:39.

Schafer & Duskin et al.            Journal of Quantitative Description: Digital Media 5(2025) 54


Prochaska, S., Engel, K., Agajanian, T., Schafer, J. S., Duskin, K., Moran, R. E., Giles, C.,
        Schroeder, F., Papa, I., Lurie, E., Robison, M., and Skreta, M. (2022). Misinformed
        Monitors: How Conspiracy Theories Surrounding Ballot Mules Led to Accusations
        of Voter Intimidation.

Recuero, R., Soares, F. B., and Gruzd, A. (2020). Hyperpartisanship, disinformation and po-
        litical conversations on twitter: The brazilian presidential election of 2018. ICWSM,
        14:569–578.

Rid, T. (2020). Active measures: The secret history of disinformation and political warfare.

Robertson, R. E., Jiang, S., Joseph, K., Friedland, L., Lazer, D., and Wilson, C. (2018).
        Auditing partisan audience bias within google search. Proc. ACM Hum. Comput.
        Interact., 2(CSCW):1–22.

Rosnow, R. L. (1980). Psychology of rumor reconsidered.

Sharma, K., Ferrara, E., and Liu, Y. (2022). Characterizing online engagement with disin-
        formation and conspiracies in the 2020 u.s. presidential election. Proceedings of the
        International AAAI Conference on Web and Social Media, 16:908–919.

Shepherd, K. and Knowles, H. (2020). Driven by unfounded SharpieGate rumor, pro-Trump
        protesters mass outside Arizona vote-counting center. Washington Post.

Shibutani, T. (1966). Improvised News: A Sociological Study of Rumor. Irvington Pub,
        Indianapolis, first edition edition.

Spiro, E. and Starbird, K. (2023). Rumors have rules. Issues Sci. Technol., 29(3):47–49.

Starbird, K., Dailey, D., Mohamed, O., Lee, G., and Spiro, E. S. (2018). Engage early, cor-
        rect more: How journalists participate in false rumors online during crisis events. In
        Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems,
        CHI ’18, page 112, New York, NY, USA. Association for Computing Machinery.

Starbird, K., DiResta, R., and DeButts, M. (2023). Influence and improvisation: Par-
        ticipatory disinformation during the 2020 US election. Social Media + Society,
        9(2):20563051231177943.

JQD:DM 5(2025)                                                         ElectionRumors2022 55


Starbird, K., Spiro, E., Edwards, I., Zhou, K., Maddock, J., and Narasimhan, S. (2016).
       Could this be true? I think so! expressed uncertainty in online rumoring. In Pro-
       ceedings of the 2016 CHI Conference on Human Factors in Computing Systems, CHI
       ’16, pages 360–371, New York, NY, USA. Association for Computing Machinery.

Sunstein, C. R. (2009). On Rumors: How Falsehoods Spread, Why We Believe Them, and
       What Can Be Done. Princeton University Press.

Tokita, C. K., Aslett, K., Godel, W. P., Sanderson, Z., Tucker, J. A., Nagler, J., Persily,
       N., and Bonneau, R. (2024). Measuring receptivity to misinformation at scale on a
       social media platform. PNAS Nexus, page gae396.

Twitter (2021). Civic integrity policy.

Vosoughi, S., Roy, D., and Aral, S. (2018). The spread of true and false news online. Science,
       359(6380):1146–1151.

Wack, M., Schafer, J. S., Kennedy, I., Beers, A., Fordham, R. F., Spiro, E. S., and Star-
       bird, K. (2023). Working Paper: Legislating Uncertainty: Election Policies and the
       Amplification of Misinformation.

Wang, Y., Callan, J., and Zheng, B. (2015). Should We Use the Sample? Analyzing Datasets
       Sampled from Twitters Stream API. ACM Transactions on the Web, 9(3):13:1–13:23.

Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., Appleton, G., Axton, M., Baak, A.,
       Blomberg, N., Boiten, J.-W., da Silva Santos, L. B., Bourne, P. E., et al. (2016). The
       fair guiding principles for scientific data management and stewardship. Scientific
       data, 3(1):1–9.

Wojcieszak, M., Casas, A., Yu, X., Nagler, J., and Tucker, J. A. (2022). Most users do not
       follow political elites on twitter; those who do show overwhelming preferences for
       ideological congruity. Sci Adv, 8(39):eabn9418.

Zeng, L., Starbird, K., and Spiro, E. S. (2016). Rumors at the speed of light? modeling
       the rate of rumor transmission during crisis. In 2016 49th Hawaii International
       Conference on System Sciences (HICSS). IEEE.

Schafer & Duskin et al.            Journal of Quantitative Description: Digital Media 5(2025) 56


                                     Online Appendix


Table A1: The set of keywords used to create the initial election tweet pool. Terms
listed in italics were removed from the keyword list on 11/7/2022. The term ‘desantis’
was added on 11/15/2022.

 BMD, BMDs, EVM, EVMs, HandMarkedPaperBallots, USPS, absentee, adjudication,
 arizona, audit, ballot, ballots, bmd, bmds, chain of custody, chicago, cisa, cochise, code,
 codes, color revolution, conservative, conservatives, decertification, decertify, dem, demo-
 crat, democrats, dems, desantis, detroit, DNC, dominion, drop box, drop boxes, dropbox,
 dropboxes, election, election2022, electioneering, electionfraud, elections, elections2022,
 electors, electors, epoll, es&s, forensic, fortalice, fraud, fraudulent, fulton, GOP, GOP-
 ers, halderman, hand count, hand-count, hand-counted, hand-marked, handcount, hand-
 counted, handcounts, handmarked, imagecast, imagecastx, integrity, intimidation, lan-
 caster, liberal, liberals, machine, machines, mail, mail in, maricopa, michigan, midterm,
 midterms, midterms2022, mule, nomachines, noncitizen, onenightcount, overvote, paper-
 ballots, pennsylvania, philadelphia, pima, pinal, poll, pollbook, pollbooks, polling, polls,
 pollwatcher, pollwatchers, pollworker, post office, postal, postoffice, precinct, racine, raf-
 fensperger, recount, republican, republicans, results, rigged, rigged voterfraud, risk-limiting
 audit, RNC, rolls, smartmatic, subversion, suppression, tabulator, tabulators, tallies, tam-
 per, tampered, tampering, touchscreen, touchscreens, undervote, vote, votebymail, voted,
 voter, voterfraud, voters, votersuppression, votes, votesuppression, voting, vulnerabilities,
 vulnerability, yuma

JQD:DM 5(2025)                                                        ElectionRumors2022 57


Table A2: Coding scheme for identifying the status of each rumor based on au-
thoritative sources. The two in-scope categories, which were kept for analysis in this
paper, are marked with bolded text.

  Code                       Description
  Insufficient Coverage      Coverage could not be found on this specific event or class
                             of events
  Largely Substantiated      Coverage exists, and confirms the major elements of online
                             narrative, including impact and cause/motive.
  Unsubstantiated            Coverage exists, but neither confirms or debunks
                             major elements of online narrative (if false/mislead-
                             ing elements, choose false/misleading)
  False/Misleading           Coverage exists and highlights false, misleading, or
                             unsubstantiated elements of online narrative.
  No Central Claim           The incident focuses on a piece of media that advances many
                             claims (such as a longer video or podcast) and no particular
                             claim is central enough to rate.


                              Note on Source Table Data

       Two of our collection methods for posts were added to improve comprehensiveness
— collections from back-filled tweets, and collections based on key location terms which
we anticipated would be the site of significant election rumoring. However, including these
slightly changes the composition of the dataset in skewing ways. Approximately 5.6% of our
dataset came from the locations collector, while approximately 0.08% came from the back-
filling collector. In the analyses above, we chose to use the more comprehensive collection
and include all tweets. We ran the geographic analysis without the tweets from the locations
collector, and found no distinguishable changes in results. For other researchers focusing
on different questions, excluding these tweets may be appropriate - we provide the data on
tweets collected solely through these means in the source table.


                           Keyword Bias Robustness Check

       While prior literature has found partisan asymmetries to the spread of misinforma-

Schafer & Duskin et al.           Journal of Quantitative Description: Digital Media 5(2025) 58


Figure 14. A recreation of the tweets in our dataset over time by partisan leaning
of users, filtered to those which only contain a smaller set of more neutral keywords.


tion and other kinds of low-quality content which might be prevalent in false, misleading
or unsubstantiated rumors (González-Bailón et al., 2023; Mosleh et al., 2024), we wanted
to check and make sure that our keyword collections were not biasing the distribution of
posts in our dataset. To check for this, we recreated the graph in Figure 5, using only
tweets which contained at least one of "vote," "ballot," or "election", which we consider to
be unbiased terms related to the election. This resulted in a subset of approximately 1.62
million of the 1.81 million tweets in our dataset. As shown in Figure 14, the general trend
patterns of Figure 5 are consistent in this new figure, though at a slightly smaller volume
for both left- and right-leaning accounts.

        We also recomputed the tweet numbers in Table 3, and found that when we limit to
the narrower set of keywords, the partisan asymmetry is actually slightly more pronounced.
When including the entire dataset, right-leaning accounts make up just under 79% of the
dataset; when including only those mentioning "vote," "ballot," or "election," they make

JQD:DM 5(2025)                                                           ElectionRumors2022 59


up just over 80%. Similarly, left-leaning accounts posted just over 18% of the posts in the
entire dataset, but only just under 17% of those only containing at least one of the keywords
"vote," "ballot," or election.


                                   Partisanship Estimation

          Estimating the political alignment, or partisan leaning of social media accounts can
be useful for understanding ideological dynamics on a platform. While some studies choose
to directly associate social media behavior with public voter-registration records Robertson
et al. (2018); Barberá et al. (2015); Green et al. (2022) this is not always feasible, and is out
of alignment with Terms of Service for using Twitter data which prohibits matching users to
offline information such as voter records without their consent 15 . The problem of estimating
political ideology while preserving account anonymity has sparked creative approaches that
include using a user’s shared hashtags (Chen et al., 2021), domains (Mosleh et al., 2021;
Nikolov et al., 2021; Chen et al., 2021; Deb et al., 2019).

          Another popular approach is to identify influential, or landmark, accounts aligned
with the political left and right and then estimate anonymous users political alignment based
on their relationship to the landmark accounts. This is the approach taken by Barberá et
al. as they identify the accounts of U.S. politicians and then estimate other users’ position
within latent ideological space based on observations of the surrounding following network
based on assumptions of homophilic following behavior (Barberá et al., 2015). The same
approach has been used by several others Wojcieszak et al. (2022); Mosleh and Rand (2022)
including with extensions for missing data Tokita et al. (2024). A similar method by Le et
al. starts with 30 hand-labeled popular left and right leaning accounts as landmarks and
assigns user partisanship based on following relationship to the landmarks (Le et al., 2017).

          Our method is in line with others that identify key landmark accounts on the left
and right and then infer others’ partisanship based on their relationship to those landmarks.


15
     https://web.archive.org/web/20241005223530/https://developer.x.com/en/developer-
     terms/more-on-restricted-use-cases

Schafer & Duskin et al.           Journal of Quantitative Description: Digital Media 5(2025) 60


Figure 15. A histogram of users by their partisanship scores, showing that this
distribution is highly bimodal and the vast majority of accounts have scores very
near 0 or 1. Note, this plot has a logarithmic y-axis, to make the distribution appear
more readable despite its skew.


In our method we consider retweeting to indicate ideological homophily. As a result, we
are focusing our analysis of partisanship to look at enacted partisanship— while not all
accounts we classify as left-leaning may consider themselves to be left-leaning, the kinds of
posts they amplify in practice are often those associated with the left (and the same for
accounts on the right).

        As Figure 15 shows, the distribution of partisanship scores is highly skewed (es-
pecially since the plot uses a logarithmic y-axis, which makes the middle seem artificially
large. This is also represented in Table A3.

JQD:DM 5(2025)                                                     ElectionRumors2022 61


Table A3: Users within each decile of the partisan spectrum, measured as the
retweets of influential right-leaning accounts as a proportion of all retweets of influ-
ential accounts.

                           retweet proportion    user count
                           [0, 0.1]                 124,143
                           (0.1, 0.2]                 1,772
                           (0.2, 0.3]                   886
                           (0.3, 0.4]                 1,029
                           (0.4, 0.5]                 1,837
                           (0.5, 0.6]                   495
                           (0.6, 0.7]                 1,217
                           (0.7, 0.8]                 2,178
                           (0.8, 0.9]                 4,928
                           (0.9, 1.0]               256,879
                           no retweets               32,293
