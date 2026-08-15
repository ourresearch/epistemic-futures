---
title: "Understanding \"Death by GPS\": A Systematic Study of Catastrophic Incidents Associated with Personal Navigation Technologies"
person: brent-hecht
attendance: unconfirmed
section: by
type: conference-paper
year: 2017
date: 2017-05-02
venue: "International Conference on Human Factors in Computing Systems"
authors: "Allen Yilun Lin, Kate Kuehl, Johannes Schöning, Brent Hecht"
source_url: https://doi.org/10.1145/3025453.3025737
fulltext_url: https://brenthecht.com/publications/chi17_deathbygps.pdf
openalex_id: W2611013903
doi: https://doi.org/10.1145/3025453.3025737
oa_status: gold
cited_by_count: 39
retrieved: 2026-08-13
content: full-text
notes: "OpenAlex duplicate/preprint records: https://openalex.org/W2890788551 (article, 2017); Full text from the author's self-archived PDF at https://brenthecht.com/publications/chi17_deathbygps.pdf (text extracted with pdftotext; PDF not stored); title expanded from the OpenAlex record's truncated form using the author's own publications page / Semantic Scholar; venue supplied from the author's publications page / Semantic Scholar (the OpenAlex record has no source)"
---

# Understanding "Death by GPS": A Systematic Study of Catastrophic Incidents Associated with Personal Navigation Technologies

## Full text

Understanding “Death by GPS”: A Systematic
Study of Catastrophic Incidents Associated
with Personal Navigation Technologies
Allen Yilun Lin*, Kate Kuehl**, Johannes Schöning †, Brent Hecht*
*Northwestern University, **University of Minnesota, †University of Bremen
allen.lin@eecs.northwestern.edu, kuehl088@umn.edu, schoening@uni-bremen.de,
bhecht@northwestern.edu
ABSTRACT

Catastrophic incidents associated with GPS devices and
other personal navigation technologies are sufficiently
common that these incidents have been given a colloquial
nickname: “Death by GPS”. While there is a significant body
of work on the use of personal navigation technologies in
everyday scenarios, no research has examined these
technologies’ roles in catastrophic incidents. In this paper,
we seek to address this gap in the literature. Borrowing
techniques from public health research and communication
studies, we construct a corpus of 158 detailed news reports
of unique catastrophic incidents associated with personal
navigation technologies. We then identify key themes in
these incidents and the roles that navigation technologies
played in them, e.g. missing road characteristics data
contributed to over 24% of these incidents. With the goal of
reducing casualties associated with personal navigation
technologies, we outline implications for design and research
that emerge from our results, e.g. advancing “space usage
rule” mapping, incorporating weather information in routing,
and improving visual and audio instructions in complex
situations.
Author Keywords

GPS; SatNav; personal navigation technologies; map apps
ACM Classification Keywords

H.5.m. Information interfaces and presentation (e.g., HCI):
Miscellaneous;
INTRODUCTION

A tourist drives his rental car across a beach and directly into
the Atlantic Ocean [16]. A person in Belgium intending to
drive to a nearby train station ends up in Croatia [46]. A
family traveling on a dirt road gets stranded for four days in
the Australian outback [45]. These incidents all have one
major factor in common: playing a key role in each incident
was a personal navigation technology, i.e. a GPS device, a
Permission to make digital or hard copies of part or all of this work for
personal or classroom use is granted without fee provided that copies are
not made or distributed for profit or commercial advantage and that copies
bear this notice and the full citation on the first page. Copyrights for thirdparty components of this work must be honored. For all other uses, contact
the Owner/Author.
Copyright is held by the owner/author(s).
CHI 2017, May 06-11, 2017, Denver, CO, USA
ACM 978-1-4503-4655-9/17/05.
http://dx.doi.org/10.1145/3025453.3025737

mobile map app (e.g. Google Maps, Apple Maps) or a
“SatNav”.
Catastrophic incidents associated with personal navigation
technologies are sufficiently common that they have come to
be associated with a colloquial name: “Death by GPS” [34].
While thankfully not all of these incidents involve the loss of
life, it is not uncommon to see media reports of people
endangering themselves or others and/or causing extensive
property damage due in part to their interaction with a
personal navigation technology.
It is tempting to blame these incidents on users and users
alone. Indeed, reports of these incidents are often peppered
with comments from witnesses and observers inquiring as to
why drivers “wouldn’t question driving into a puddle that
doesn’t seem to end” [34] and did not notice “multiplelanguage traffic signs” [46]. However, it is our responsibility
as HCI researchers to design better systems that help people
avoid making “user errors” [36], especially when these errors
involve such extensive human and financial costs.
The geographic human-computer interaction (“GeoHCI”)
[17] literature includes a relatively large body of work that
examines how people use GPS-based navigation
technologies in standard scenarios and in the course of their
everyday lives (e.g. [7,18,21,27,28]). However, no work has
focused on the increasingly large number of catastrophic
incidents associated with these technologies. In other words,
the “Death by GPS” phenomenon has yet to be studied in a
rigorous fashion.
This paper seeks to begin the process of addressing this gap
in the literature. As has been pointed out in the work on
typical interactions with GPS devices [7], a major obstacle
to the systematic analysis of “Death by GPS” incidents is that
no database of these incidents exists. Additionally, methods
that have been used to study interaction with GPS devices in
the past (e.g. lab studies, field studies) are not valid for this
type of analysis.
To overcome these obstacles, we turned to an unlikely source
of data: news articles. This approach is adapted from the
public health literature, where news articles are used as
sensors when the research topic is of sufficient significance
but no authoritative dataset is available. Using rigorous best
practices for building a minimally biased-corpus of news

stories and expert-led qualitative coding, we collected and
analyzed a dataset of 158 news stories about unique
catastrophic incidents associated with personal navigation
technologies.
In our analyses of this corpus, we had two cascading research
goals:
Goal 1: Identify the patterns that characterize catastrophic
incidents associated with personal navigation technologies.
Goal 2: Use the identified patterns to generate implications
for research and design that can help build safer personal
navigation technologies.
More specifically, for our first goal, we sought to ascertain
themes in both the basic properties of these incidents (e.g.
Who was involved? What happened?) and themes in the
roles that navigation technologies played in the incidents (i.e.
How did the navigation technology specifically fail the
user?). Based on the identified patterns, our second research
goal involved outlining a series of concrete steps that
researchers and practitioners can take to prevent the
reoccurrence of common types of catastrophic incidents (and
save lives).
We find, for instance, that a large number of “Death by GPS”
incidents are single-vehicle collisions (likely far more than
accidents caused by other factors), that stranding events were
the next most common type of incident, and that distraction
by a navigation device was significantly associated with
more serious incidents. With regard to the roles of
technology, we observed that missing road characteristics
attributes (e.g. road surface types and current condition) had
a substantial effect, as did the failure to correctly infer
routing preferences (among a series of other factors).
The implications for research and design that emerge from
our findings span the spectrum of “GeoHCI” topical
domains. For example, we discuss how our results highlight
the importance of (1) incorporating vehicle type and weather
information into routing algorithms, (2) improving
navigation guidance in the face of complex geographies, and
(3) developing separate interfaces for tourists and locals.
More generally, our results show that navigation devices can
be more intelligent about safety than their current state-ofthe-art: telling users to pay attention to their environment
when the device is turned on. Blanket warnings like these are
known to be ineffective in HCI [35], and our results show a
path forward towards improved approaches.
In summary, this paper makes the following contributions:
1.

We perform the first research that systematically
characterizes catastrophic incidents associated with
personal navigation technologies and the role that these
technologies played in these incidents. We identify

1 The dataset can be downloaded here: https://goo.gl/8vE14V

2.

major themes in the incidents themselves and in the roles
played by technology.
With the goal of preventing the patterns we identified in
these catastrophic incidents from reoccurring, we
outline a series of implications for research and design
that can help us develop safer personal navigation
technologies.

To further research on this topic, we are also releasing the
core dataset we developed for this paper 1 . This dataset
consists of the complete corpus of 158 news stories along
with all the codes we applied to each story in the process
described below. To make our findings more accessible, we
are also releasing an interactive web map version of the
corpus, which allows users to see the approximate location
of each incident and further information about the incident 2.
A Note on Terminology: The subject of this research
resulted in several terminological challenges. The core
technologies of interest to this paper – GPS devices, SatNav
devices, and mobile map applications like Google Maps and
Apple Maps – are often referred to using the term “GPS”.
This term ignores the diverse positioning techniques (e.g.
Wi-Fi positioning), routing algorithms, and cartography built
into these technologies, so we felt it was imprecise to use this
more casual language given the nature of this paper. As such,
we use the term “personal navigation technology”
(sometimes shortened to “navigation technology” or
“navigation device”). Similarly, given the diversity of the
types of incidents in our corpus, assigning this class of
incidents a formal name was not straightforward. We chose
the term “catastrophic incidents” in accordance with the
“extremely unfortunate or unsuccessful” definition of
“catastrophic” [50].
RELATED WORK

This work’s core motivation primarily emerges from two
areas in the “GeoHCI” literature: (1) work that has examined
the use of personal navigation technologies in standard
scenarios and (2) research that has looked at the long-term
behavioral and cognitive effects of using these technologies.
Navigation Technologies in Standard Scenarios

Researchers began to investigate HCI issues associated with
in-car navigation systems almost as soon as these
technologies were first commercialized [10,11,48]. This
thread of research covers a diverse set of topics including
attention demands [11,23,48], cartography [27,33,42],
different modes of output [9,21] and age-related variation
[2], all with a focus on everyday usage scenarios. For
instance, Kun et al. [23] conducted a lab simulation study and
found that graphical GPS interfaces distracted users from the
primary task of driving. Medenica et al. [33] coupled
augmented reality with in-car GPS navigators and showed
that this combination reduced drivers’ distractions. Jensen et

2 The interactive map is available here: https://goo.gl/jlQ8S4

al. [21] compared different interaction modes of in-car GPS
navigators and concluded that the combination of audiovisual output is preferred by drivers, but did not significantly
reduce device-related distractions.
The projects in this research thread that most directly
motivated our work are those of Hipp et al. [18] and Brown
and Laurier [6]. Both studies considered the “troubles”
drivers encountered with in-car GPS devices in typical
driving situations. Hipp et al. [18] conducted a traditional
user interface evaluation to compare the performances of
different types of in-car navigation systems on the same
route. They identified unexpressed routing preferences,
failure to understand intentional detours from planned routes,
and the lack of real-time traffic information as the common
interaction weakness of commercial navigators (with the
latter now being fixed in most modern navigation
technologies). Brown and Laurier [7] carried out an
interaction analysis in which they observed and interviewed
drivers about their daily uses of in-car GPS to understand
their navigation practices. They outlined five types of
“normal troubles” of using in-car GPS navigators in
everyday driving: destination, routing, maps and sensors,
timing of instructions and inflexibility of the technology.
This work is distinguished from that above in that instead of
studying the use of personal navigation technologies in
standard scenarios, we focus on catastrophic incidents that
involved these technologies. Some of the roles that these
technologies play in catastrophic incidents are similar to
those identified in the literature on standard scenarios, and
other roles are new to the literature (as are the resulting
design implications). We discuss the relationship between
our findings and the findings from prior work in detail below.
Long-term Impact of Navigation Technology Use

Another class of relevant research focuses on understanding
the behavioral and cognitive changes produced by personal
navigation technologies. For instance, Leshed et al. [28]
conducted an ethnography-based study and showed that
drivers using GPS-based navigation technologies are
disengaged from their surrounding environment. Aporta and
Higgs [3] examined the long-term impact of navigation
technology at a larger scale, arguing that the adoption of
navigation technologies has alienated many Inuit hunters
from the traditional wayfinding skills they have depended on
for thousands of years. Other studies have looked at the
cognitive impact of navigation systems. For instance,
Gardony et la. [13] conducted a lab-based simulation study
and demonstrated that these devices may impair users’
ability to record information about the environment and their
spatial orientation. The findings of this line of work inform
this paper’s research and design implications, specifically
those related to the multifaceted relationships between a
navigation technology, its user, and the environment.
METHODS

Although catastrophic incidents associated with personal
navigation technologies are sufficiently noteworthy to have

been given a moniker – “Death by GPS” – no authoritative
dataset of these incidents exists. The high stakes of these
incidents make them worthy of study, but the lack of
available data and relative rarity of these incidents make it
difficult to analyze them. Additionally, lab experiments or
other simulations are not currently well-suited to this
research area.
Fortunately, the domain of public health has significant
experience studying phenomena with the same core
properties as “Death by GPS” incidents, i.e. relatively rare
phenomena of media interest for which no authoritative
dataset is available and for which simulations are not
currently tractable. Specifically, to examine these
phenomena, researchers in this domain have followed a twostep pipeline: (1) build a corpus of news stories describing
these incidents and (2) analyze the corpus using expert-led
qualitative coding techniques. For example, in the absence of
a national surveillance system for homicide-suicide in the
United States, Malphurs and Cohen [31] collected and coded
related news articles from 191 national newspapers to
identify the number and subtypes of such incidents. This
approach of relying on newspapers to summarize the
characteristics of homicide-suicide incidents has also been
applied in the Netherlands [29] and Italy [40]. Similarly, to
study the collisions between wheelchairs and motor vehicles,
a type of accident that is not distinguished in police reports,
LaBan and Nabity [24] gathered 107 news articles using
LexisNexis. They analyzed this corpus to understand gender
incidence ratios, proportion of different types of motor
vehicles, the time of incidents, and other characteristics of
these incidents.
In this paper, we adopt this approach from the public health
literature. To do so, we first verified that no relevant
authoritative dataset exists by contacting several local police
departments and national agencies, including the
Minneapolis Police Department (USA), the Aachen Police
Department (Germany), National Transportation Safety
Board (USA) and National Highway Traffic Safety
Administration (USA). We then implemented the pipeline
from public health, using the process described in more detail
below.
Phase 1: Corpus Development

One of the key challenges in the public health-based
approach is gathering the corpus of news articles. Most prior
work has relied on one of two methods: (1) an exhaustive
search in the local newspaper of a specific study site (e.g.
[5,38]) or (2) unstructured but extensive querying of news
search engines (e.g. [24,31]). Since our work is not wellsuited to a specific study site, we implemented a more robust
version of the latter approach using best practices from
communication studies for sampling news stories with
minimal bias [25,44].
The first step in this minimal bias sampling approach
involves leveraging prior research in this space (i.e. the
literature covered in the Related Work section) to seed a set

of keywords, which is then grown using a variety of
structured strategies (e.g. synonym generation). These
keywords are then used to iteratively query a news database
(in our case LexisNexis), with the set of keywords refined at
each step. Achieving acceptable precision for one’s
keywords is particularly important given that these databases
often have strict limits on the total number of news stories
that can be returned for a given query (e.g. LexisNexis’s is
set to 1000 stories). We were able to achieve a precision of
40.8%, which is within acceptable parameters [44]. This left
us with 408 articles that were related to catastrophic
incidents associated with personal navigation technologies.
We note that we restricted our search to stories published in
2010 or later to ensure that our findings are relevant to
modern personal navigation technologies (e.g. smartphone
map apps) rather than early-generation devices.
Additionally, due to language constraints with respect to the
database and the coders, we only searched for stories written
in English, a subject we cover in more detail in the limitation
section.
Two challenges remained before we could begin the next
stage of the pipeline. First, many of the articles were opinion
columns about the “Death by GPS” phenomenon and did not
describe specific incidents. Second, some incidents were
described by two different journalists in two different
publications. To remove these articles from our dataset, two
researchers conducted an exhaustive search, reading each
article and evaluating its validity for our study and matching
duplicates (we kept the more detailed of any two stories on
the same incident; disagreements were resolved through
discussion).
In the end, we were left with a corpus that contains 158 news
stories, each describing a unique catastrophic incident
associated with personal navigation technologies. For
replication purposes and for researchers who may want to
apply this method in other contexts, we have included
additional detail about how we implemented our corpusbuilding procedure in the documentation of our coded
dataset. We also discuss the one minor change we had to
make to the standard procedure to adapt it to the goals of our
research project: we could not simply use the keywords from
prior research on interaction with navigation technologies
because these only focused on standard scenarios. As such,
we used a slightly more iterative keyword generation method
in which researchers identified keywords from small samples
of actual relevant news stories.
Phase 2: Expert-led Coding

The second stage of the public health pipeline involves
employing a relatively standard qualitative coding procedure
with an important exception: coders are domain experts. This
expertise enables coders to map properties of incidents
reported in news articles to pre-existing topics in the
literature of interest, or to new challenges when relevant. In
our case, our two coders (members of our research team) had
extensive expertise in both geography and HCI, the two

fields most associated with our research questions. More
specifically, each coder had both a Masters’ degree in
geography or geoinformatics and a Masters’ degree in
computer science (with a focus on HCI).
The specifics of the coding process were as follows: using a
small seed corpus, knowledge of our research goals, and
expertise in the research domain, our coders jointly
established a series of coding dimensions. Next, using a
random sample of 10 articles, the coders jointly developed a
list of codes for each dimension and developed a
corresponding codebook (this is included in our dataset).
Both coders then evaluated a set of 40 overlapping articles to
assess each dimension for interrater reliability. Importantly,
when it was not possible to assess an article for a particular
coding dimension, coders left the value blank.
The Cohen’s Kappa of coders’ results on all dimensions
ranged from 0.69 to 0.95, which indicates “substantial
agreement” [26]. Of particular note, we achieved a Cohen’s
Kappa of 0.79 for the Technological Cause dimension,
which is the basis for a set of key findings below. As the
Cohen’s Kappa was sufficiently high for all dimensions,
coders evaluated the remaining articles on an individual
basis.
Beyond Technological Cause, other major coding
dimensions that were considered included the Seriousness of
the incident (e.g. Was death involved?), the Incident Type
(e.g. Was it a single-vehicle collision? Did a vehicle get
stranded?), Weather, Road Surface (e.g. Was it on a dirt road
or a paved road?), whether Distraction was explicitly noted
as an issue in the article and whether the driver was a Local
Driver or Non-local Driver to the area of the incident. A
complete list of dimensions and their corresponding specific
codes is included in our public dataset. For the major coding
dimensions, coders were able to assign codes for over 90%
of incidents with the exception of Local Driver, in which
37% of incidents could not be coded.
Interpretation of Results

As described above, there is a consensus (e.g.
[22,24,29,31,38,40]) in the public health literature that when
no authoritative data is available, the news article-based
pipeline we employ here can provide valuable early insight
about a phenomenon of interest. However, news articlederived data has its share of limitations, as is the case with
many datasets considered in public health (e.g. even
authoritative crime datasets have been criticized for
potentially strong racial biases [39], an issue the computing
community has been facing in association with predictive
policing technologies [20]). To the best of our knowledge,
our use of news article-derived data is novel to the HCI
literature. As such, we believe that highlighting the known
limitations of this type of data early in the paper is important
so that our results can be interpreted in proper context.
The most significant limitation of news article-derived data
is a risk of “newsworthiness” bias, or an overrepresentation

of incidents that are in alignment with the incentive
structures of news organizations. While at least one study
has found no such bias (e.g. [38]), others have found
newsworthiness bias to manifest as an overrepresentation of
(1) accidental incidents (e.g. fewer suicides, more unusual
events) or (2) more fatal incidents (e.g. more murders, fewer
assaults) [12]. All incidents that we examine are accidental
in nature, making the accidental bias less relevant [12,38].
However, a potential bias towards fatal incidents is important
to consider when examining our results below.
To minimize further risk of bias, we employ robust statistical
tests when making comparisons between types of incidents.
In most cases, we are able to simply use Pearson’s Chisquared test of independence. However, in circumstances
where the assumptions of Chi-squared distribution are
violated due to relatively small sample size, we used a
likelihood ratio G test of independence, a best practice
suggested by [1,32]. All p-values reported in the paper have
been subject to Bonferroni correction.
Newsworthiness bias mainly affects proportional results (i.e.
comparisons between incident types), which are a small
percentage of the results we present below. The bulk of our
results are either qualitative descriptions of incidents or
absolute values (e.g. raw counts of incidents of certain
types). Our absolute results should be interpreted in the
context of a limited understanding of the size of the incident
population, i.e. we do not know what share of catastrophic
incidents associated with personal navigation technologies
are included in our news corpus. However, even if the
incidents in our sample are close to the entire population, the
aggregate devastation to blood and treasure of just these
incidents make them worthy of analysis and discussion in the
HCI literature, which does not often examine such high-cost
interactions with technology. In order to add additional
context and further this discussion, we provide qualitative
descriptions of incidents wherever space allows.
RESULTS

In this section, we provide an overview of the major results
that emerged from our coding process. In doing so, we seek
to address our first research goal: characterizing patterns in
catastrophic incidents associated with personal navigation
technologies. We organize our thematic findings into two
groups (1) themes in the basic properties of these incidents
and (2) themes in the technological causes of these incidents.
We discuss each group of findings in turn below.
Basic Properties
Many People Have Died in Incidents Associated with
Personal Navigation Technologies

Table 1 shows the results of our coding for the Seriousness
of the incidents with respect to human and financial cost.
Clear in Table 1 is that navigation technologies have been
associated with some truly tragic events: our corpus
3 News article numbers refer to the index in our released dataset.

Seriousness of Incidents

#

%

Major (deaths)

44

28%

Major (injuries)

23

15%

Medium (e.g. property damage, legal
consequences)

52

33%

Low (e.g. significant inconvenience)

39

25%

Table 1. Distribution of the Seriousness of incidents.

describes the deaths of 52 people in total, including two
children. These deaths occurred across 45 incidents, or 28%
of our corpus. Additionally, our corpus contains 23 incidents
(15%) that resulted in significant bodily harm, but not death.
Although the proportion of fatal incidents in our corpus may
be exaggerated due to the aforementioned newsworthiness
bias, the absolute number of deaths (and injuries) associated
with navigation technologies that we have identified is
alarming. GPS devices, mobile maps, and other navigation
technologies provide us with tremendous benefits, but these
results indicate that they also have a set of costs that had not
yet been systematically enumerated. These results also
highlight the importance of better understanding catastrophic
incidents like those studied here, as well as using this
understanding to design safer technologies.
Table 1 also shows that “Death by GPS” is not the ideal term
to describe incidents associated with navigation technologies
that have serious implications. Over 50% of the incidents in
our corpus did not involve death or significant injury, with
the damage in these cases being primarily of a financial or
other nature. Examples of these incidents include a group of
skiers who intended to go to La Plagne, a famous ski resort
in the Alps, but ended up arriving at Plagne, a town in
southern France that is 715 km away (article #463). Another
example involved five men who drove onto a nuclear power
plant’s property at the behest of their navigation device and
were suspected of terrorism (article #95).
The Most Common Incident Type is a Single-Vehicle Crash,
but There is Substantial Incident Type Diversity

Table 2 depicts the results of our coding for Incident Type
and shows that the most common type of incident in our
corpus is car crashes. However, the table also shows that
crashes are far from the only type of incident we
encountered. For instance, almost 20% of incidents resulted
in cars being stranded in very rural areas and over 15%
involved people going on substantial detours. We were also
surprised by the number of reports (7) of people driving on
the wrong side of the road for an extended distance. Such
examples include a person who drove 48km on the wrong
side of a highway after following her device’s instructions to
enter the wrong freeway ramp (article #90) and a 37-year-old
man who was caught driving the wrong way on an Australian

Types of Incidents

# (%)

Trespass (violate space usage rules)

5 (3%)

Wrong way (opposite side)

7 (4%)

implications, this result provides further evidence that simply
adopting standard recommendations from traditional traffic
safety research will not be able to address the safety concerns
associated with personal navigation technologies.

Detour (e.g. wrong address)

25 (16%)

Unfamiliarity with One’s Surroundings Plays a Key Role

Stranded/stuck (e.g. in the wildness, on railroad
tracks)

31 (20%)

Crashes

90 (57%)

Crashes with pedestrians/bikes

13 (8%)

Crashes with vehicles

26 (17%)

Single-vehicle collisions

51 (32%)

Table 2. Distribution of Incident Types.

highway for more than 10 km and attributed the error to his
navigation device (article #12).
In Table 2, we also show subtypes of the Crashes incident
type. We found that single-vehicle collisions comprised the
majority of crashes (51 cases, 32% of overall incidents), with
crashes with other vehicles (26 cases, 17%) and crashes with
pedestrians and bikes (13 cases, 8%) making up the
remainder of crash incidents. To understand single-vehicle
collisions in more detail, we did an additional round of
coding to identify more detailed themes (this was done by a
single expert coder). Here we found that vehicles colliding
with buildings, walls, and guardrails due to excessively
narrow roads were the most common type of single-vehicle
incident. Crashing with low overhead bridges is another
common occurrence in our corpus, with a diverse array of
other objects in the environment being the subject of the
remainder of the single-car crashes.
Personal Navigation Technology-related Crashes Appear to
Be Proportionally Different Than Typical Crashes

To put the above results in context, we utilized The National
Automotive Sampling System General Estimates System
(NASS GES) dataset from the U.S. National Highway
Traffic Safety Administration [49]. The NASS GES dataset
contains a representative sample of vehicle crashes of all
types as reported by police. While not directly comparable to
our corpus, the NASS GES can provide a sense of whether
personal navigation technology-related crashes are
distributionally similar to the population of car crashes, or
whether the role played by navigation technology manifests
in different types of crash outcomes.
Our results suggest that the latter is the case: crashes
associated with personal navigation technologies appear to
be different in type relative to typical crashes. For instance,
only 15% of car crashes in the NASS GES dataset are singlevehicle collisions, whereas the same type accounts for 57%
of crashes in our corpus (Table 2). Moreover, crashes
associated with building/walls/guardrails and overhead
bridges are much less common in the NASS GES dataset,
comprising less than 2% of crashes overall, while in our
corpus they account for 42% of all crashes. Among other

A substantial percentage of the incidents in our corpus
occurred when users of personal navigation technologies
were outside of their home region. Specifically, 78% percent
of the incidents involved non-locals and only 22% percent
involved locals. Some examples of incidents involving nonlocals include one story in which a person drove her car into
a swamp (article #23). The driver was quoted as saying “This
was the road it told me to take … I don’t know the area at all,
so I just thought it was okay”. Another incident consisted of
a driver hitting and killing a pedestrian, with the
corresponding news article reporting that “the driver was
unfamiliar with the area and was adjusting her GPS
navigational system” (article #71).
While the use of navigation technologies likely increases
outside of one’s home region, this result does suggest that
user interfaces for navigation technologies may want to
encourage more caution and support users in different ways
when they are in their home region and when they are
traveling. We discuss these implications for design in more
detail below.
Distraction Leads to More Serious Incidents

We identified a significant association between our
Distraction coding dimension and our Seriousness
dimension, with distraction leading to many deadly incidents
(𝜒2 (2) = 19.2, p < .05). Examining the 21 deadly incidents
that involved distraction in more detail, we found that in five
cases, people were using non-critical features of their
navigation device. For instance, a driver killed a cyclist while
“using the zoom-in function” (article #33) and another driver
from Springfield injured a bicyclist while “looking for place
to eat on GPS” (article #40).
Stranding Risk Increases with Dirt Roads, Bad Weather, and
Especially Both at the Same Time

We observed significant associations between our Road
Surface coding dimension and our Incident Type dimension.
In particular, if vehicles were traveling on a dirt road, there
were more than the expected number of stranding incidents
(𝐺 2(12) = 53.0, p < .05). This was especially the case when
weather was a factor. Examples include a medical student
from Quebec who followed GPS and got stranded on a
logging road for three days in the snow (article #4) and a
British couple and their children who were stranded for four
days on an unsealed road that was made muddy by torrential
rain (article #115). Interestingly, the latter family thought
that their in-car GPS device was suggesting a significant
shortcut and followed its instructions as a result, a point we
return to later.
More generally, we found significant interaction between
disaster type dimension and the weather dimension ( 𝐺 2(4) =
21.1, p < .05). Specifically, there are more than the expected

Technological Causes

# (%)

Missing or incorrect geographic objects

5 (4%)

Geocoding (i.e. associating toponym and its
coordinates)

7 (6%)

Incorrect toponym disambiguation (i.e. select
similar but wrong destination)

8 (7%)

Instructions/visualization

18 (16%)

Non-transparent/wrong route preference

18 (16%)

Missing or incorrect attributes

64 (53%)

Physical characteristics of the road (e.g. road
surface, road widths)

30 (25%)

Clearance height

17 (14%)

Traffic rules (e.g. no left turn)

5 (4%)

Temporary blockage

3 (3%)

Geopolitical boundary (e.g. country border)

2 (2%)

Private area

2 (2%)

Ferry line as road

3 (3%)

Bridge limitation

2 (2%)

Table 3. Distribution of Technological Cause. Note: The #
does not add up to 158 because coders did not enter a code
when there was not enough information in given news story to
make a certain type of assessment.

number of stranding incidents under severe weather, as one
might anticipate.
Technological Causes

Table 3 shows the results of our coders assessing each article
for its Technological Cause. In this section, we discuss the
themes in the distribution of these results, as well as the
findings from a more detailed coding that we conducted to
understand important trends.
Attributes that are Missing or Incorrect Are a Major Problem

Geographic information, like that which is used in routing
for personal navigation technologies, consists of two
components: spatial information and attributes of that spatial
information [14]. Broadly speaking, in a routing context, the
spatial information is the location of a road and the attributes
consist of key properties of the road (e.g. the speed limit).
Our results in Table 3 suggest that missing and incorrect
attributes play a major role in the catastrophic incidents in
our corpus, being in part responsible for 64 (53%) of these
incidents. To better understand the types of attributes
involved, one expert conducted a second round of coding to
determine the types of attributes that were most often
missing or incorrect and the results are also included in Table
3. The physical characteristics of the road (e.g. width,
surface) (30 incidents) and clearance height (17 incidents)
were by far the most common type of attributes that were
missing or incorrect. Indeed, stories about routing algorithms
neglecting the road characteristics and the heights of
overpasses are pervasive in our corpus. For example, as
noted above, failure to incorporate road surface information

led multiple sedans to be stranded on unpaved roads (often
in a very dangerous fashion) (e.g. article #4, #115) and
multiple trucks ran into serious trouble due to low-clearance
roads (e.g. article #6, #34, #36). Indeed, we found trucks
were more susceptible to suffer from attribute related issues
due to this problem as evidenced by the significant
interaction between our Vehicle Type coding dimension and
the Technological Cause dimension ( 𝐺 2(15) = 67.4, p <
.05).
Another theme present in the attribute types in Table 3 is the
notion of “space usage rules” (SURs) [41], or regulations
associated with the use of a certain area (in this case, a road).
For instance, in one incident, a truck that traveled on truckprohibited road killed a father and a daughter in a sedan
(article #27). In another, an in-car GPS device guided a
driver up a private driveway, and the driver ended up in a
physical confrontation with the owners of the property
(article #102).
Cartographic and Audio Instructions Are Not Capable of
Handling Complex Geographic Contexts

Table 3 shows that almost 18 incidents involved an issue
with routing guidance, either in visual (cartographic) or
audio form. Past work on the use of GPS devices in standard
scenarios identified that excessive instructions are a
significant problem with GPS usability [2,7]. While we did
observe this problem in our corpus, many of the incidents
given this code by our experts related to a different issue: the
inability of the personal navigation technology to help
drivers navigate complex geographic contexts.
For example, in one story in our corpus, a person who was
driving at night was faced with a freeway on-ramp that was
immediately parallel to a railroad track (article #146). Figure
1 shows a Street View image of the exact location of the
incident. When the driver’s navigation device asked him to
turn right, the driver turned onto the railroad tracks as the
instructions were ambiguous. Ten kilometers later, the
driver’s car was destroyed by an oncoming train, but
fortunately the driver survived by jumping out of the car.
Similarly, article #66 tells a tragic story in which a bicyclist
was hit by a driver who ignored a “Yield” sign at a nontypical intersection because the driver’s navigation device
screen simply instructed her to “go straight”. Wrong-way
driving was particularly (and significantly; 𝐺 2(24) = 100.1,
p < .05 ) associated with cartographic and navigation
instruction issues, and complex geographies were common
in these cases. For instance, one report in our corpus (article
#39) describes the story of a driver who followed her
navigation device’s instructions to “take the first left turn” at
a roundabout. However, the actual first left turn (not the first
legal left turn) was the exit ramp of a freeway, and the driver
– who was on the road at night – entered the freeway driving
in the wrong direction. This driver sadly lost her life.
Standard Scenarios versus Catastrophic Incidents

As noted above, past work has done a rigorous job of
identifying and categorizing problems encountered by users

significant issue in standard usage scenarios. For
catastrophic incidents, the issue appears to be attributes
rather than the spatial data itself, a subject we discuss
immediately below.
IMPLICATIONS FOR RESEARCH AND DESIGN

Figure 1. A Google Street View image depicting the complex
geography of the location of the incident in article #146.

of personal navigation technologies in standard usage
scenarios. While the issues discussed above have not been
highlighted in prior work, one additional contribution of the
results in Table 3 is to add gravity to many of the previouslyidentified issues. For instance, in a study of challenges
encountered in standard GPS device usage, Brown and
Laurier [7] found that route preferences, out-of-date spatial
data, the timing of navigation guidance, and positioning
errors were key sources of user frustration. Some of these
issues appear in Table 3, meaning that they were in part
responsible for a number of catastrophic incidents in addition
to more everyday usability issues.
Of particular note are Brown and Laurier’s findings with
respect to route preference. Route preference issues played a
role in 18 (16%) of the news stories in our corpus, indicating
they are a significant issue in catastrophic incidents as well
as everyday usage scenarios. However, the route selection
issues present in our corpus are of a substantially different
character than those identified by Brown and Laurier.
Specifically, while participants in Brown and Laurier’s study
wanted more route choice, people in our corpus were given
too many choices (i.e. at least one was dangerous). For
example, in one incident a Canadian couple got lost in rural
Nevada after selecting the “shortest path” route option
suggested by their navigation device, which included a littlemaintained road. They were stranded in Nevada for 49 days,
during which time the husband sadly lost his life (article #9).
We return to this case and the issue of strict “shortest path”
routing and route selection in the implications section.
With respect to prior work, it is also interesting to examine
Table 3 for what is not common or present at all in our
corpus. It appears that some issues with everyday use of
navigation technologies do not play a role in catastrophic
incidents associated with these technologies. For instance,
positioning inaccuracies and the lack of adaptability to
intentional “detours” were the sources of major usability
challenges in the work of Brown and Laurier. However,
neither appeared in our corpus. Similarly, missing spatial
data was not a major issue in our corpus – it played a role in
only 5 (4%) of incidents – but has been identified as a

In this section, we turn our attention to our second research
goal: helping to identify solutions to the problems we found
in our results section by enumerating a series of implications
for both research and design. Some of these implications
suggest improvements to the design of existing systems,
while other present important new challenges for the
GeoHCI research community. We have organized these
implications into two high-level categories corresponding to
two broad areas of the GeoHCI research space: implications
related to spatial computing (e.g. routing algorithms, missing
attributes) and implications related user interaction issues.
Spatial Computing Implications
Geometries without Attributes Can Be Dangerous

A major finding above is that missing attributes play a
substantial role in the catastrophic incidents in our corpus.
This suggests that road network geometries may be “getting
ahead” of the corresponding attributes. That is, data
providers are adding road segments to their networks faster
than they are adding the attributes to those segments that are
necessary to facilitate safe routing.
These results suggest that data providers may not want to
integrate road segments into their networks unless those
segments have high-quality data for a core set of attributes.
Based on our findings, these attributes should include the
type of the road (e.g. dirt, asphalt) and the clearance height
of the road (as defined by any overpasses, tunnels, and other
obstacles) at minimum.
Incorporate Vehicle Type into Routing Decisions

Even when high-quality attributes are included, however,
they must be used intelligently by routing algorithms.
Returning to Table 3, a key theme emerges in this respect:
many of the incidents included in this table could have been
prevented if routing algorithms can understand the
limitations of the vehicle that they are routing. For instance,
it is often not safe for sedans to drive down rough country
roads, and trucks should not drive down roads with low
clearance heights. Coupled with good coverage of attributes,
incorporating vehicle type information would be a
straightforward and effective way to maintain good coverage
of possible routes (e.g. allowing SUVs to drive down rough
country roads), while at the same time increasing safety.
Extend Space Usage Rule Mapping Efforts to Road Networks

We identified that the lack of space usage rules (i.e. usage
regulations) is a common missing attribute associated with
the catastrophic incidents in our corpus. Space usage rules
(SURs) have been a topic of growing interest in the GeoHCI
research community in the past few years (e.g. [19,41,43]),
but this literature has focused on mapping rules associated
with regions rather than roads. For example, a common

research challenge in SUR mapping is identifying regions in
which smoking is legal or illegal [41].

the driver to look at the environment to confirm that the
vehicle is on a legal road.

Our research suggests that more effort should be spent on the
identification of SURs for road networks. In particular,
improving data related to the maximum clearance of roads,
whether roads are public or private, and improved
recognition of traffic rules are particularly important.
Fortunately, unlike many SUR mapping challenges that
require multifaceted approaches (e.g. natural language
processing, crowdsourcing), it is likely that much of the work
here can be done using computer vision (CV) approaches.
The automated detection of traffic rules in this fashion is
already underway [4]. It is likely that private property signs
would present unique challenges for CV algorithms due to
their diversity, but this is a contained problem that can likely
be at least partially addressed with current state-of-the-art
CV techniques.

User Interaction Implications

The Weather Matters When Routing

Our results suggest that routing algorithms should consider
weather information when generating routes, and should do
so in concert with vehicle type information. A substantial
number of the stranding incidents in our corpus would have
been avoided with relatively straightforward weather- and
vehicle-aware routing approaches. For instance, if it has
rained 20 centimeters in the past day, routing algorithms
should not send drivers of sedans down dirt roads. Similarly,
if it has snowed 20 centimeters and it has stayed below
freezing, routing algorithms should recommend that sedan
drivers stick to main thoroughfares, which are plowed more
quickly and more often (and should perhaps consider
increasingly available information in many cities about
which roads have been plowed since the last major snow).
The Downsides of Map Matching

We observed in our corpus that map matching techniques
[15] can backfire. These techniques are designed to mitigate
GPS noise by “snapping” vehicle locations to the closest
road network geometry. However, they were likely involved
in the three incidents in which a person drove on a train track
parallel to a road (article #17, #32, #116) and also a few
incidents in which people drove on the wrong side of the
divided road (e.g. article #12, #90) (all cases happened in
evening). In these cases, map matching algorithms likely
“snapped” the driver’s position to the nearest or the correct
side of the road, making the driver believe that they were on
right track (which may be difficult to assess at night).
Although more work is needed to understand this issue in
detail, one potential improvement is to make map matching
algorithms more error-sensitive in situations in which the
distance between geometries is smaller than the error
tolerance. Specifically, when an algorithm notices that there
are multiple parallel linear geometries (e.g. a divided
highway or a railroad parallel to a road), it can reduce the
tolerance of its map matching radius. When observing a
small, persistent mismatch for a short period, GPS devices
could immediately prompt users about this mismatch and ask

Route Preference Must Be Accompanied with Adequate
Information to Make an Educated Choice

Past research on the use of navigation technology in standard
scenarios has advocated for providing greater route
preference for users. Our results suggest that this preference
must be accompanied with adequate information for users to
make safe decisions. Current navigation devices often offer
multiple routing preferences such as “fastest”, “shortest”, or
“eco mode”. At the very least, these technologies should
warn users that certain choice may involve traversing unsafe
territory, as was the case with the Canadian couple that chose
the “shortest path” through Nevada without understanding
the consequences of doing so.
As mentioned above, in addition to the usability problem of
excessive instructions with bad timing found by previous
studies, we identified a new type of guidance-related
problem: instructions that are too simple for the spatial
decisions that the user has to make. Two research challenges
emerge from this issue: (1) automatically detecting complex
geographies and (2) developing interfaces to better support
users in these contexts. With regard to the first challenge,
public crash datasets (e.g. [49]) can provide ground truth
information to help develop regression models that assess the
complexity of a routing context based on the topology of the
surrounding road network (and likely other information, such
as railroads). The second challenge might be at least partially
addressed through the use of image-based navigation, i.e. by
annotating Street View imagery with arrows and labels.
Image-based navigation is known to have benefits over most
other approaches [47] but needs to be updated frequently to
reflect any potential changes in the environment..
Local Mode and Non-Local Mode

Our results suggest that non-local drivers are at substantially
greater risk for catastrophic incidents associated with
navigation technologies than local drivers. These findings
advocate for the development of customized features for
each of these populations, i.e. a “local mode” and a “nonlocal mode”. For instance, neuroscience research has shown
that more attention is required when driving in an unfamiliar
environment [30]. As such, designers should investigate
strategies for reducing interaction with drivers when drivers
are outside their home region(s). Additionally, routing
algorithms could provide non-local drivers with an “easiest”
route that prioritizes highways and avoids complex
intersections to minimize the turn-by-turn instructions and
general information load. Similarly, GPS devices could
disable non-essential functionality (e.g. searching for local
restaurants) while in unfamiliar territory and re-enable those
functions only when drivers come to a complete stop (or
return to their home areas).

DISCUSSION

In this paper, we provided the first characterization of the
patterns in catastrophic incidents associated with the use of
personal navigation technologies. We have also outlined a
series of implications for design and research that emerge
from these patterns. Below, we highlight several discussion
points associated with this research.
First, it is interesting to reflect on the design implications in
the context of automated vehicles. Some of the implications
will clearly become moot if a human is not behind the wheel
(e.g. those related to improved instructions), as will be the
case for many of the core functionalities of navigation
devices [6]. However, other implications may become
significantly more important. For instance, adding attribute
information to geometries, improving understanding of
space usage rules and incorporating weather information will
be critical to helping automated cars avoid dangerous
navigation decisions. The same would likely apply in the
nearer term with semi-automated cars, as recent work
suggests that there may be excessive deference to automated
routing approaches given the attentional challenges of partial
automation [37]. Similarly, the research community has
pointed out the need to keep drivers engaged when behind
the wheel of a mostly-automated vehicle. Prompting users in
the case of persistent map matching issues and engaging
them in other difficult navigation-related tasks may be one
way to accomplish this goal.
Second, the news article-based pipeline we use here may be
able to help HCI researchers examine other difficult-to-study
phenomena. As noted above, our public health-based
approach is best suited to phenomena that share three
properties: (1) no authoritative dataset is available, (2)
instances are too rare to observe in large numbers in the wild
and cannot be replicated in a lab setting, and (3) instances are
frequently covered by journalists. Some additional HCI
phenomena that share these properties include criminal
events in the sharing economy and safety concerns related to
location-based games like Pokémon GO [8]. To make it
easier for researchers to employ our methodology, we have
provided a step-by-step description of our approach in the
documentation that is included with our coded dataset.
It is important to note that our coded dataset contains much
more data than we could fully describe in this paper. While
we have highlighted what we as researchers in the
geographic HCI domain believe to be the most important
themes in our results, other researchers may benefit from
examining our data from a different perspective. One
particularly interesting avenue of exploration that we are
working to investigate is using the spatial locations of each
incident (available in the dataset) to try to develop predictive
models of the types of areas in which the use of navigation
technologies might be particularly risky.

to put the relative incidence of these catastrophes in context.
While we identified that GPS devices and related
technologies played a role in at 158 catastrophic incidents
involving 52 deaths, these technologies have also likely
played a role in saving the lives of many people (e.g. guiding
people to emergency resources, preventing people from
getting lost). With this in mind, the design and research
suggestions we make above are careful to be augmentative
of existing navigation technology functionality rather than
substantially altering current functionality.
Limitations

In addition to the drawbacks of the news article-based
pipeline discussed above, this paper is also subject to several
additional limitations. For instance, while our incident
corpus is the first agglomeration of its type of any scale,
future work should seek to increase this size by either finding
more news stories or collecting data on incidents that are not
reported in the news. With respect to identifying unreported
incidents, crowdsourcing has been proven effective for
building databases of technology failures in the domain of
aviation [51]. This may be an approach that is feasible in this
domain as well. Similarly, a related limitation of our dataset
is that it that 97% of our articles came from either the U.S.,
the U.K., Canada, New Zealand, or Australia (due to the
focus on English articles). It is reasonable to assume that
patterns in other countries might be different, and future
work should examine these patterns.
The issue of survivor bias should also be considered. It is
likely that navigation technologies have played a role in a
significant number of deadly accidents for which there was
no witness or exogenous information to identify the role of
the technology (the 44 deadly incidents considered here had
one or both of these). Interestingly, survivor bias could
counteract the fatality bias discussed above.
CONCLUSION

In this paper, we have extended prior work on user
interaction with navigation technologies to consider
catastrophic incidents associated with these technologies.
We have characterized key patterns that exist in these
incidents and enumerated implications for research and
design that emerge from these patterns. This research
increases our understanding of how the navigation
technologies that we design cause serious harm, as well as
provides a path towards developing safer navigation
technologies.
ACKNOWLEDGEMENTS

We would like to thank our colleagues in GroupLens and our
anonymous reviewers for their feedback. This work was
funded in part by the U.S. National Science Foundation (IIS1421655, CAREER IIS-1552955) and by the Volkswagen
Foundation through a Lichtenberg Professorship.
REFERENCES

While we believe it is important for the HCI community to
examine and learn from catastrophic incidents associated
with the use of computing technologies, it is also important

1. Alan Agresti. 1996. An introduction to categorical data
analysis. Wiley New York.

2. Abdullah Al Mahmud, Omar Mubin, and Suleman
Shahid. 2009. User experience with in-car GPS
navigation systems: comparing the young and elderly
drivers. 1. https://doi.org/10.1145/1613858.1613962
3. Claudio Aporta and Eric Higgs. 2005. Satellite Culture:
Global Positioning Systems, Inuit Wayfinding, and the
Need for a New Account of Technology. Current
Anthropology 46, 5: 729–753.
https://doi.org/10.1086/432651
4. Vahid Balali, Armin Ashouri Rad, and Mani GolparvarFard. 2015. Detection, classification, and mapping of
U.S. traffic signs using google street view images for
roadway inventory management. Visualization in
Engineering 3, 1: 15. https://doi.org/10.1186/s40327015-0027-1
5. J. Baullinger, L. Quan, E. Bennett, P. Cummings, and K.
Williams. 2001. Use of Washington State newspapers
for submersion injury surveillance. Injury Prevention 7,
4: 339–342. https://doi.org/10.1136/ip.7.4.339
6. David Beattie, Lynne Baillie, Martin Halvey, and
Roderick McCall. 2015. Adapting SatNav to meet the
demands of future automated vehicles. In CHI 2015
Workshop on Experiencing Autonomous Vehicles:
Crossing the Boundaries between a Drive and a Ride.
Retrieved June 14, 2016 from
http://strathprints.strath.ac.uk/52245/
7. Barry Brown and Eric Laurier. 2012. The Normal
Natural Troubles of Driving with GPS. In Proceedings
of the SIGCHI Conference on Human Factors in
Computing Systems (CHI ’12), 1621–1630.
https://doi.org/10.1145/2207676.2208285
8. Ashley Colley, Jacob Thebault-Spieker, Yilun Lin,
Jonna Häkkilä, Nuno Nunes, Dirk Wenig, Kate Kuehl,
Benjamin Fischman, Valentina Nisi, Nina Runge,
Donald Degraen, Brent Hecht, and Johannes Schöning.
2017. The Geography of Pokémon GO: Beneficial and
Problematic Effects on Places and Movement. In
Proceedings of the SIGCHI Conference on Human
Factors in Computing Systems.
9. P. Dalton, P. Agarwal, N. Fraenkel, J. Baichoo, and A.
Masry. 2013. Driving with navigational instructions:
Investigating user behaviour and performance. Accident
Analysis & Prevention 50: 298–303.
https://doi.org/10.1016/j.aap.2012.05.002
10. Thomas A. Dingus and Melissa C. Hulse. 1993. Some
human factors design issues and recommendations for
automobile navigation information systems.
Transportation Research Part C: Emerging
Technologies 1, 2: 119–131.
https://doi.org/10.1016/0968-090X(93)90009-5
11. Thomas A. Dingus, Melissa C. Hulse, Jonathan F.
Antin, and Walter W. Wierwille. 1989. Attentional
demand requirements of an automobile moving-map
navigation system. Transportation Research Part A:
General 23, 4: 301–315. https://doi.org/10.1016/01912607(89)90013-7

12. Philip R. Fine, Chester S. Jones, J. Michael Wrigley, J.
Scott Richards, and Matthew D. Rousculp. 1998. Are
newspapers a viable source for intentional injury...
Southern Medical Journal 91, 3: 234.
13. Aaron L. Gardony, Tad T. Brunyé, Caroline R.
Mahoney, and Holly A. Taylor. 2013. How Navigational
Aids Impair Spatial Memory: Evidence for Divided
Attention. Spatial Cognition & Computation 13, 4: 319–
350. https://doi.org/10.1080/13875868.2013.792821
14. Michael F. Goodchild. 2001. A Geographer Looks at
Spatial Information Theory. In Spatial Information
Theory, Daniel R. Montello (ed.). Springer Berlin
Heidelberg, 1–13. https://doi.org/10.1007/3-540-454241_1
15. Joshua S. Greenfeld. 2002. Matching GPS observations
to locations on a digital map. In Transportation
Research Board 81st Annual Meeting.
16. Hilary Hanson. 2012. GPS Leads Japanese Tourists To
Drive Into Australian Bay. The Huffington Post.
Retrieved September 12, 2016 from
http://www.huffingtonpost.com/2012/03/19/gps-touristsaustralia_n_1363823.html
17. Brent Hecht, Johannes Schöning, Thomas Erickson, and
Reid Priedhorsky. 2011. Geographic Human-computer
Interaction. In CHI ’11 Extended Abstracts on Human
Factors in Computing Systems (CHI EA ’11), 447–450.
https://doi.org/10.1145/1979742.1979532
18. Markus Hipp, Florian Schaub, Frank Kargl, and
Michael Weber. 2010. Interaction Weaknesses of
Personal Navigation Devices. In Proceedings of the 2Nd
International Conference on Automotive User Interfaces
and Interactive Vehicular Applications (AutomotiveUI
’10), 129–136.
https://doi.org/10.1145/1969773.1969796
19. Konstantin Hopf, Florian Dageförde, and Diedrich
Wolter. 2015. Identifying the Geographical Scope of
Prohibition Signs. In Spatial Information Theory, Sara
Irina Fabrikant, Martin Raubal, Michela Bertolotto,
Clare Davies, Scott Freundschuh and Scott Bell (eds.).
Springer International Publishing, 247–267.
https://doi.org/10.1007/978-3-319-23374-1_12
20. White House. 2016. Big Data: A Report on Algorithmic
Systems, Opportunity, and Civil Rights. Washington,
DC: Executive Office of the President, White House.
21. Brit Susan Jensen, Mikael B. Skov, and Nissanthen
Thiruravichandran. 2010. Studying Driver Attention and
Behaviour for Three Configurations of GPS Navigation
in Real Traffic Driving. In Proceedings of the SIGCHI
Conference on Human Factors in Computing Systems
(CHI ’10), 1271–1280.
https://doi.org/10.1145/1753326.1753517
22. John D. Kraemer and Connor S. Benton. 2015.
Disparities in road crash mortality among pedestrians
using wheelchairs in the USA: results of a capture–
recapture analysis. BMJ Open 5, 11: e008396.
https://doi.org/10.1136/bmjopen-2015-008396

23. Andrew L. Kun, Tim Paek, Željko Medenica, Nemanja
Memarović, and Oskar Palinko. 2009. Glancing at
Personal Navigation Devices Can Affect Driving:
Experimental Results and Design Implications. In
Proceedings of the 1st International Conference on
Automotive User Interfaces and Interactive Vehicular
Applications (AutomotiveUI ’09), 129–136.
https://doi.org/10.1145/1620509.1620534
24. Myron M. LaBan and Thomas S. Nabity. 2010. Traffic
Collisions Between Electric Mobility Devices
(Wheelchairs) and Motor Vehicles: Accidents, Hubris,
or Self-destructive Behavior? American Journal of
Physical Medicine & Rehabilitation 89, 7: 557–560.
https://doi.org/10.1097/PHM.0b013e3181d8a346
25. Stephen Lacy, Brendan R. Watson, Daniel Riffe, and
Jennette Lovejoy. 2015. Issues and Best Practices in
Content Analysis. Journalism & Mass Communication
Quarterly: 1077699015607338.
https://doi.org/10.1177/1077699015607338
26. J. Richard Landis and Gary G. Koch. 1977. The
Measurement of Observer Agreement for Categorical
Data. Biometrics 33, 1: 159–174.
https://doi.org/10.2307/2529310
27. Talia Lavie, Tal Oron-Gilad, and Joachim Meyer. 2011.
Aesthetics and usability of in-vehicle navigation
displays. International Journal of Human-Computer
Studies 69, 1–2: 80–99.
https://doi.org/10.1016/j.ijhcs.2010.10.002
28. Gilly Leshed, Theresa Velden, Oya Rieger, Blazej Kot,
and Phoebe Sengers. 2008. In-car Gps Navigation:
Engagement with and Disengagement from the
Environment. In Proceedings of the SIGCHI Conference
on Human Factors in Computing Systems (CHI ’08),
1675–1684. https://doi.org/10.1145/1357054.1357316
29. M. C. A. Liem and F. Koenraadt. 2007. Homicidesuicide in the Netherlands: A study of newspaper
reports, 1992 - 2005. Journal of Forensic Psychiatry &
Psychology 18, 4: 482–493.
https://doi.org/10.1080/14789940701491370
30. Mandy Mader, André Bresges, Reyhan Topal,
Alexander Busse, Michael Forsting, and Elke R.
Gizewski. 2009. Simulated car driving in fMRI—
Cerebral activation patterns driving an unfamiliar and a
familiar route. Neuroscience Letters 464, 3: 222–227.
https://doi.org/10.1016/j.neulet.2009.08.056
31. Julie E. Malphurs and Donna Cohen. 2002. A
newspaper surveillance study of homicide-suicide in the
United States. The American Journal of Forensic
Medicine and Pathology 23, 2: 142–148.
32. Mary L. McHugh. 2013. The Chi-square test of
independence. Biochemia Medica 23, 2: 143–149.
https://doi.org/10.11613/BM.2013.018
33. Zeljko Medenica, Andrew L. Kun, Tim Paek, and Oskar
Palinko. 2011. Augmented Reality vs. Street Views: A
Driving Simulator Study Comparing Two Emerging
Navigation Aids. In Proceedings of the 13th
International Conference on Human Computer

Interaction with Mobile Devices and Services
(MobileHCI ’11), 265–274.
https://doi.org/10.1145/2037373.2037414
34. Greg Milner. 2016. Pinpoint: How GPS Is Changing
Technology, Culture, and Our Minds. W. W. Norton &
Company.
35. Jakob Nielsen. 2001. Error message guidelines. Nielsen
Norman Group: 06–24.
36. Donald A. Norman. 2013. The Design of Everyday
Things: Revised and Expanded Edition. Basic Books.
37. Stephen M. Casner Norman Edwin L. Hutchins, Don.
The Challenges of Partially Automated Driving.
Retrieved December 21, 2016 from
http://cacm.acm.org/magazines/2016/5/201592-thechallenges-of-partially-automated-driving/fulltext
38. David Y. Rainey and Carol W. Runyan. 1992.
Newspapers: a source for injury surveillance? American
journal of public health 82, 5: 745–746.
39. Robert M. Regoli and John D. Hewitt. 2008. Exploring
Criminal Justice. Jones & Bartlett Learning.
40. Paolo Roma, Antonella Spacca, Maurizio Pompili,
David Lester, Roberto Tatarelli, Paolo Girardi, and
Stefano Ferracuti. 2012. The epidemiology of homicide–
suicide in Italy: A newspaper study from 1985 to 2008.
Forensic Science International 214, 1–3: e1–e5.
https://doi.org/10.1016/j.forsciint.2011.06.022
41. Pavel Andreevich Samsonov, Xun Tang, Johannes
Schöning, Werner Kuhn, and Brent Hecht. 2015. You
Can’T Smoke Here: Towards Support for Space Usage
Rules in Location-aware Technologies. In Proceedings
of the 33rd Annual ACM Conference on Human Factors
in Computing Systems (CHI ’15), 971–974.
https://doi.org/10.1145/2702123.2702269
42. Julia Schreiber. 2009. Bridging the gap between useful
and aesthetic maps in car navigation systems. In
Proceedings of the 11th International Conference on
Human-Computer Interaction with Mobile Devices and
Services, 51. Retrieved September 19, 2016 from
http://dl.acm.org/citation.cfm?id=1613922
43. Marcus Soll, Philipp Naumann, Johannes Schöning,
Pavel Samsonov, and Brent Hecht. 2016. Helping
Computers Understand Geographically-Bound Activity
Restrictions. 2442–2446.
https://doi.org/10.1145/2858036.2858053
44. Jo Ellen Stryker, Ricardo J. Wray, Robert C. Hornik,
and Itzik Yanovitzky. 2006. Validation of Database
Search Terms for Content Analysis: The Case of Cancer
News Coverage. Journalism & Mass Communication
Quarterly 83, 2: 413–430.
https://doi.org/10.1177/107769900608300212
45. By Bonnie Malkin in Sydney. 2010. Britons stranded in
Australian Outback for four days after satnav error.
Retrieved September 12, 2016 from
http://www.telegraph.co.uk/news/worldnews/australiaan
dthepacific/australia/7925649/Britons-stranded-inAustralian-Outback-for-four-days-after-satnaverror.html

46. Bruno Waterfield. 2013. GPS failure leaves Belgian
woman in Zagreb two days later. Retrieved September
12, 2016 from
http://www.telegraph.co.uk/news/worldnews/europe/bel
gium/9798779/GPS-failure-leaves-Belgian-woman-inZagreb-two-days-later.html
47. Dirk Wenig, Alexander Steenbergen, Johannes
Schöning, Brent Hecht, and Rainer Malaka. 2016.
ScrollingHome: Bringing Image-based Indoor
Navigation to Smartwatches. In Proceedings of the 18th
International Conference on Human-Computer
Interaction with Mobile Devices and Services
(MobileHCI ’16), 400–406.
https://doi.org/10.1145/2935334.2935373
48. Walter W. Wierwille, Jonathan F. Antin, Thomas A.
Dingus, and Melissa C. Hulse. 1988. Visual Attentional
Demand of An In-car Navigation Display System.
Retrieved September 13, 2016 from
https://trid.trb.org/view.aspx?id=927088

49. Traffic Safety Facts 2014: A Compilation of Motor
Vehicle Crash Data from the Fatality Analysis
Reporting System and the General Estimates System.
National Highway Traffic Safety Administration.
Retrieved from
https://crashstats.nhtsa.dot.gov/Api/Public/ViewPublicat
ion/812261
50. Definition of Catastrophic. Retrieved from
https://www.google.com/search?q=catastrophic+inciden
ts&ie=utf-8&oe=utf-8#q=catastrophic
51. Aviation Safety Reporting System. NASA. Retrieved
from
http://akama.arc.nasa.gov/ASRSDBOnline/QueryWizar
d Filter.aspx.
