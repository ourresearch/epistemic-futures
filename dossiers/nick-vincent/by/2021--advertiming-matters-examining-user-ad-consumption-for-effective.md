---
title: "AdverTiming Matters: Examining User Ad Consumption for Effective Ad Allocations on Social Media"
person: "nick-vincent"
section: "by"
type: "journal-article"
year: 2021
date: "2021-05-06"
venue: "ACM CHI, 2021"
authors: "Koustuv Saha, Yozen Liu, Nicholas Vincent, Farhan Asif Chowdhury, Leonardo Neves, Neil Shah, Maarten W Bos"
source_url: "https://dl.acm.org/doi/10.1145/3411764.3445394"
retrieved: "2026-08-13"
content: "full-text"
notes: "OpenAlex W3163483672; CV ref [P9]; Full text extracted from the author's self-archived PDF (https://koustuv.com/papers/CHI21_AdverTiming.pdf)."
---

# AdverTiming Matters: Examining User Ad Consumption for Effective Ad Allocations on Social Media

## Full text

AdverTiming Matters: Examining User Ad Consumption for
Effective Ad Allocations on Social Media
Koustuv Saha

Yozen Liu

Nicholas Vincent

Georgia Institute of Technology
Atlanta, GA, USA
koustuv.saha@gatech.edu

Snap Inc.
Santa Monica, CA, USA
yliu2@snap.com

Northwestern University
Evanston, IL, USA
nickvincent@u.northwestern.edu

Farhan Asif Chowdhury

Leonardo Neves

Neil Shah

University of New Mexico
Albuquerque, NM, USA
fasifchowdhury@unm.edu

Snap Inc.
Santa Monica, CA, USA
lneves@snap.com

Snap Inc.
Santa Monica, CA, USA
nshah@snap.com

Maarten W. Bos
Snap Inc.
Santa Monica, CA, USA
mbos@snap.com

ABSTRACT
Showing ads delivers revenue for online content distributors, but
ad exposure can compromise user experience and cause user fatigue and frustration. Correctly balancing ads with other content is
imperative. Currently, ad allocation relies primarily on demographics and inferred user interests, which are treated as static features
and can be privacy-intrusive. This paper uses person-centric and
momentary context features to understand optimal ad-timing. In a
quasi-experimental study on a three-month longitudinal dataset of
100K Snapchat users, we find ad timing influences ad effectiveness.
We draw insights on the relationship between ad effectiveness and
momentary behaviors such as duration, interactivity, and interaction diversity. We simulate ad reallocation, finding that our studydriven insights lead to greater value for the platform. This work
advances our understanding of ad consumption and bears implications for designing responsible ad allocation systems, improving
both user and platform outcomes. We discuss privacy-preserving
components and ethical implications of our work.

CCS CONCEPTS
• Human-centered computing → Empirical studies in collaborative and social computing; Social media; • Applied computing →
Psychology; Marketing; Economics.

KEYWORDS
social media, ads, Snapchat, momentary behaviors, causal-inference,
matching, ad allocation
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for components of this work owned by others than ACM
must be honored. Abstracting with credit is permitted. To copy otherwise, or republish,
to post on servers or to redistribute to lists, requires prior specific permission and/or a
fee. Request permissions from permissions@acm.org.
CHI ’21, May 8–13, 2021, Yokohama, Japan
© 2021 Association for Computing Machinery.
ACM ISBN 978-1-4503-8096-6/21/05. . . $15.00
https://doi.org/10.1145/3411764.3445394

ACM Reference Format:
Koustuv Saha, Yozen Liu, Nicholas Vincent, Farhan Asif Chowdhury, Leonardo
Neves, Neil Shah, and Maarten W. Bos. 2021. AdverTiming Matters: Examining User Ad Consumption for Effective Ad Allocations on Social Media. In CHI Conference on Human Factors in Computing Systems (CHI ’21),
May 8–13, 2021, Yokohama, Japan. ACM, New York, NY, USA, 18 pages.
https://doi.org/10.1145/3411764.3445394

1

INTRODUCTION

In recent years, many online platforms predominantly generate
revenue from advertisements (ads). Ad revenue offsets costs, making the services “free” to use — ad-supported business models are
even considered to be at the “heart of the free internet” [104]. Some
common examples are search engine services like Google and Bing,
and social platforms like Facebook, StackExchange, LinkedIn, and
Snapchat. These online platforms show ads via a variety of implicit
and explicit mechanisms, including “sponsored” or “promoted” content. However, an online platform that relies on ad revenue must
contend with the tradeoff between ad revenue and ads’ impact on
users. If a platform shows more ads, it runs the risk of hurting
the user experience and losing its userbase. [10, 12, 17]. Consequently, platforms resort to optimizing ad allocations that aim for
multi-stakeholder benefits from user-centric, platform-centric, and
advertiser-centric perspectives.
Traditionally, ad delivery in mass media such as print and television took a blanket approach — the same ad was shown to everyone
who read the same newspaper or watched the same television channel at a time, and accordingly, demography (age/gender)-based targeting was conducted using people’s interests (e.g. certain ads might
only play on a sports channel). Although a blanket approach to
advertising somewhat works in new and online media, online platforms introduce new complexities, potentials and dimensions [10].
With the ubiquity of various personalizations, content and ad delivery is often algorithmically customized to suit the interests of
a specific user and improve their engagement with the platform.
Importantly, the objective of personalized ad allocation is not just to


CHI ’21, May 8–13, 2021, Yokohama, Japan

increase revenue per user (and ad), but also to improve a user’s satisfaction and experience with ads — a user would plausibly be more
interested in ads topically relevant to their interests [61]. Personalized ad allocation has therefore built on the success of research in
Recommender Systems, Machine Learning, and Human-ComputerInteraction (HCI) [21, 36, 46]. However, content personalization
algorithms typically rely on demographic attributes like age, race,
and gender, which are not only privacy-intrusive but are also static
and exclusionary. As such, this practice has been critiqued in the
fairness, accountability, transparency literature as reinforcing (and
potentially exacerbating) stereotypes and societal biases [3, 41, 82].
While demographic attributes and content-based recommendations have been tremendously explored, other factors remain
relatively less known — online ad allocation and ad spacing strategies typically rely on sets of rules, such as ads are shown after T
duration or after N content views, where the parameters are mostly
drawn from observations about the average user on a platform.
However, the same ad allocation strategy would not necessarily
work effectively on all users, given that every individual is different,
and that they have a different lifestyle, behavior, needs, and engagement both offline and online [6]. In fact, online behaviors are also
functions of offline context and routines, as well as users’ momentary psychological and cognitive states [37, 64, 91]. Therefore, it is
important to embrace and evaluate dynamic and context- centric
ad allocation strategies. This line of work remains underexplored
both generally and particularly on evolving and newer forms of
social and online content delivery.
Our work aims to address the above gap by studying ad consumption on Snapchat, a popular multimedia-driven online social
platform which has a content feed called “Discover Feed”, similar to
content feeds offered by Facebook, Twitter, and Instagram’s News
or Story feeds. We latch on to the notion that users may show
varying ad-consumption behaviors by the time of the day or other
in-the-moment activities on the platform. Theoretically, our work is
motivated by the body of literature that explains the psychological
and time of the day effects in content and ad consumption [36, 102].
Practically, our work builds on the motivation that by teasing out
these effects in a person-centric and context-centric fashion, we can
not only draw better insights about ad consumption but can also
make specific recommendations about when and whom questions in
“What be shown to whom, and when?” — a question that interests
both content providers (platform owners) as well as consumers
(users). In particular, our work proposes three research aims:
Aim 1: To examine the effect of showing ads at a time preferred by users.
Aim 2: To examine how ad effectiveness varies with in-themoment user behaviors on the platform.
Aim 3: To estimate the effect of ad allocations based on insights drawn from the above two aims.
We conduct our work on three-month longitudinal data of 100K
Snapchat users. First, we conduct a quasi-experimental study to
find that timing ads plays a strong effect in increasing ad effectiveness, as measured by ad reception and ad click-through rate
(CTR). Then, we examine the relationship of ad effectiveness with
momentary on-platform behaviors. Specifically, we consider how

Saha et al.

various measures — duration, activity, interactivity, interaction diversity, distractedness, and extra-socialness — might reflect insights
about when to conduct ad allocations with respect to these measures. Finally, we estimate the potential impact of our insights by
simulating experiments of reallocating ads. We find that simulations adopting insight about the relationship between ad reception
and various patterns in on-platform behavior from our study guide
more balanced and effective distributions of ads.
Methodologically, this work contributes a novel causal-framework
to infer and model ad consumption by minimizing the confounding
factors. This approach can be extended to study other forms of user
engagement using observational social media data. Additionally,
we propose a computational approach to obtain preferred times of
ad consumption for different users. Our results reveal the potential to use our method in ad engagement and other engagement
mechanisms. Our work provides insights into ad consumption on a
social platform, as well as makes recommendations for effective ad
allocation using on-platform user behavior.
From an HCI perspective, our work augments the body of work
studying the need to balance user experience and ad effectiveness [4,
56, 88, 106]. Theoretically, our work bears implications in advancing
the understanding of ad consumption on social media. We discuss
the implications to design better and more responsible ad allocation
systems from multi-stakeholder standpoints. By taking a broader
view of ad allocation, we argue that it is possible to create better
outcomes for both users and platforms.
Applied to social platforms, our ad allocation approach’s efficacy
would help to accomplish monetary goals with fewer ads, and
therefore, can lead to allocating fewer ads —– a solution preferred
by users. Better ad interaction would potentially lead to better
social interaction and user experience on the online social platforms.
Finally, a key advantage of our computational framework lies in
the fact that it does not use demographic, typographic, or privacysensitive information of the users. We also discuss the privacypreserving component and ethical implications of this work.
Privacy, Ethics, and Disclosure. This paper uses sourced data on
Snapchat. Our work is conducted within Snapchat, and given the
sensitivity of our work, we are committed to securing the privacy
of the individuals. The dataset was accessed within a secured environment with necessary privacy and ethical protocols in place.
The dataset was de-identified and no personally identifiable or
demographic information was used. This paper only reports aggregated and 𝑧-transformed measures to prevent traceability and
identifiability of users, and to prevent disclosing company-private
information, yet providing context in readership. Even accounting
for the benefits, we recognize the potential misuses, risks, and ethical consequences involved with this kind of research, on which we
elaborate in the Discussion.

2 BACKGROUND AND RELATED WORK
2.1 Ad Effectiveness and User Experience
Conceptually, ad effectiveness is a key indicator of success of an ad
based on how well it does or the returns it generates in various possible outcomes such as user likeability, engagement, and sales [14,
105]. In an early work, Morrison and Dainoff studied ad complexity


AdverTiming Matters

and dwell times, i.e., how much time a user spends to look at an ad
and if they remember an ad more than others [72]; dwell times have
been widely used as an implicit metric to study user interest and
satisfaction [45, 55]. Doyle and Saunders defined effective ads as
those that help advertisers reach their goals [22]. Ducoffe developed
survey scales to measure ad effectiveness in terms of ad value in
traditional media [23], which was later extended in the online media [24], positing ad value as a form of communication engagement
between advertisers and consumers [24, 25]. Ducoffe and Curlo followed up to propose quantifiable concepts of expected advertising
value (EAV) and outcome advertising value (OAV) of ads [25]. These
assessments have also been used in practice and in comparing online and offline ad effectiveness. In the online form, ad effectiveness
is often quantified as return rate or Click-Through-Rate (CTR) [87].
CTR measures the proportion of effectively allocated ads or the ratio
of the clicks on an ad to its number of impressions [15]. Other work
has proposed sophisticated measurements of online ad effectiveness
such as using ghost ads and experimental approaches [43].
Ad effectiveness is considered a vital outcome while planning,
creating, and executing an ad [83]. Research has studied how various factors relate with ad value [25, 63, 84]. These studies found that
informativeness and entertainment aspects bear a positive association with ad effectiveness, whereas intrusiveness bears a negative
relationship [24]. Further, ad effectiveness shares a deep and complex interplay with user experience on the platform [10, 73]. Brajnik
and Gabrielli reviewed the effects of online advertising on user experience and proposed a systematic theoretical framework for its
better understanding [10]. Ads can cause fatigue, irritation, and
negative emotions for users, making them leave and reduce engagement on the platform, consequently hurting both ad effectiveness
and platform engagement [10]. Therefore, it is critical to optimize
ad allocation in such a way that user experience is not compromised, as shown in recent HCI research through gamification [4],
intelligent placement strategies [73], and animation [21].
The above body of work motivates us to operationalize and
study factors associated with ad effectiveness on social media. We
extend the HCI community’s long-drawn interest in balancing user
experience with ad effectiveness [4, 17, 21, 73, 88, 106]. We define
ad effectiveness using two measures based on 1) what fraction of
time a user fully watches an ad (or ad reception), and 2) whether
a user expresses some form of interest in the ad by clicking on it
(or ad CTR). We then examine the role of (previously unexplored)
factors such as timing and momentary on-platform behavior in
explaining ad effectiveness outcomes in online platforms.

2.2

Ad Consumption Contextualized with
Psychological Factors

Marketing and consumer research has extensively studied the
importance of “antecedent state” — a term that encompasses all
of the momentary financial, psychological, and physiological attributes with which a consumer arrives at a marketing interaction [8]. Haugtvedt et al. studied how personality traits associate
with ad effectiveness [39]. In particular, mood states are known
to significantly influence consumer behavior, judgment, and recall [29], and within the space of online ads, beliefs and attitude
towards ads have been identified to predict ad effectiveness [26,

CHI ’21, May 8–13, 2021, Yokohama, Japan

111]. Batra and Stayman showed that positive mood mediates brand
attitudes in print ads [7], and Edwards et al. adopted the lens of
psychological reactance to understand forced responses to ads
and correspondingly the perceived intrusiveness and irritation to
ads [11, 27]. People’s responses to ads include affective, behavioral,
and cognitive components [24, 98, 111]. Here, the affective component includes irritation and entertainment elicited by an ad [27],
the behavioral component includes pre- and post- ad purchasing
behavior [98], and the cognitive component includes factors like
informativeness of an ad [24]. Relatedly, Bronner et al. studied the
relationship between mood and ad effectiveness [13].
Parallelly, a body of research notes how time of day may affect
the variety-seeking behavior of individuals [35]. In fact, circadian
orientation and time of day are known to associate with an individual’s depth of information processing with respect to ads [16].
Prior research studied how ad effectiveness varies with time of
day by different age groups of individuals [33], and Tellis et al.
studied the microeffects of time, content, and duration on ad effectiveness [102]. Relatedly, Kapoor et al. noted the promises of
just-in-time recommendations in online platforms [46, 47]. Taken
together, these studies explain how ad consumption is dependent
on several contextual and psychological factors.
While the role of context in explaining ad effectiveness has been
extensively studied in offline and traditional forms of media, it still
remains an underexplored avenue in the space of social media and
online platforms. In fact, with the emergence of newer forms of
media and content delivery, it is important to assess contextual
factors and accordingly improve content delivery to ensure better
user experience [68]. Further, due to the lack of a comprehensive
understanding of how users consume ads on these new online
content delivery platforms coupled with ubiquitous technological
affordances (such as smartphones and wearables), ad allocation on
social media is still largely driven by only static rules and contentrelated personalization. Our work aims to address this gap in theory
and practice by examining ad consumption with respect to time and
momentary factors on Snapchat. We further simulate an experiment
that evaluates the efficacy of our context-centric factors in making
effective ad allocations.

2.3

Social Media and Observational Data

Research reveals how social media activities reflect people’s offline routines and behaviors [18, 37, 64]. Social media behaviors
can potentially reveal naturalistic patterns of behavior, cognition,
psychological states and social milieu, both in real-time and across
longitudinal time [32, 59, 92]. Prior work has harnessed social media to infer individual-centric attributes ranging across personality
traits and wellbeing using machine learning and computational
linguistics [34, 80, 81, 96, 99]. Kosinski et al. used Facebook Likes
to predict a range of attributes such as sexual orientation, ethnicity,
personality, intelligence, addictive behavior, age, and gender.
In the related problem space as ours, social media behaviors
can explain ad consumption and vice versa [21, 100, 110, 112]. Kim
et al. investigated the antecedents of clicking ads on Facebook [50]
and Mao and Zhang studied the factors associated with users’ intention to click on social media ads, particularly around content,


CHI ’21, May 8–13, 2021, Yokohama, Japan

media, and individual-related factors [62]. Prior work has also examined social media ads with respect to perceived informativeness,
entertainment, and irritation [50, 63]. and Youn and Kim examined
reactance related factors of avoiding ads on Facebook [112].
In general, the effect of an (external or internal) change or an
intervention is measured using causal-inference approaches. These
approaches draw motivation from epidemiological research settings of randomized controlled trials (RCTs): participants are randomly assigned to a treatment and a control group where the former receives a drug, and the latter receives a placebo, and then
changes are measured in the two groups to quantify the effect of
the drug [38]. Similarly, understanding user behavior on a platform
due to platform-based interventions are best studied with experimental and A/B test approaches [57, 71]. However, such approaches
bear caveats. For instance, experimental studies that seek participant consent can be limited by concerns of observer effect [1] —
participants may modulate their otherwise normal behavior with
the awareness being monitored or observed. Alternatively, experimental research conducted without participants’ awareness are
deemed unethical especially in the human-centered research paradigm [44, 69]. For example, the Facebook emotion contagion study
did not inform the participants that their feeds would be modified
for research [54]. While this work was successful in uncovering
valuable insights regarding people’s affective behavior on social
media, this work was heavily critiqued on ethical grounds [44].
Further, experimentation without apriori awareness of impact on
participants may lead to long-term negative consequences for both
platforms and individuals.
Consequently, in problem settings where experimental approaches
may be infeasible or unethical, observational studies can be an
alternative. While observational studies cannot guarantee “true
causality”, they are designed in a way to minimize confounds and
to investigate longitudinal data in providing stronger evidences
than naive correlational analyses [42]. These studies can also benefit future randomized experiments where no preferred treatment is
known apriori [89]. Recently, this kind of study has also generated
interested in HCI, social, and behavioral science, including that
using social media data [20, 48, 76, 90, 95, 114]. Notably, De Choudhury et al. examined the shifts in suicidal ideation tendencies in
online communities [20] and Culotta estimated county health statistics using Twitter data [18, 20]. Of particular interest is Saha et al.’s
work which motivates us to operationalize social media behavioral
measures such as activity, interactivity, and interaction diversity,
whose relationship we examine with ad reception in our study [96].
Our work draws motivation from the success of observational
data and quasi-experimental study design to understand ad consumption on social media. Besides, we also note that our study values the importance of a contextualized person-centric design [93]
which is not only an improvement over one-for-all or generalized approaches but also stays clear of using demographic and
trait-based information of users. While using such information may
though improve prediction accuracy in some problem settings, these
approaches could be exclusionary, discriminating, privacy-intrusive,
and unethical [41, 82]. Rather, our study design incorporates dynamic platform behaviors to draw insights corresponding to user
strata exhibiting similar combinations of platform behaviors.

Saha et al.

3

DATA

We conduct our study on the Snapchat platform. Snapchat is an
online social and instant messaging platform that enables users to
share and interact with others using ephemeral content, including
text, images, videos, and other forms of multimedia. Snapchat is particularly very popular among the youth, with 73% of the 18-25 age
demographic in the U.S. being Snapchat users [78]. Snapchat provides a Discover Feed where users can find and view recommended
content in tiled story format from news publishers, brands, and
content providers, such as ESPN, Wall Street Journal, Daily Mail,
etc. Users can browse through these tiles, and when on a tile, they
can consume, skip, or advance to the next recommended content.
Snapchat’s Discover Feed is design-wise similar to content-feed of
Facebook, Twitter, or Instagram [2]. Discover Feed also shows ads
which contribute to ∼98% of Snapchat’s revenue [86]. As on most
other platforms, users can watch an ad on Snapchat as long as they
are interested, skip if they are uninterested or want to move on to
other content, and/or swipe up (considered an ad click) if they are
particularly interested to know more.
We scope our study to understanding ad consumption on Snapchat
Discover Feed. We obtain a random sample of 100,000 users who
were active on Snapchat at least once every day for over three
months between December 17, 2019, and February 24, 2020. For
these users, we obtain their longitudinal activity on the platform in
the same period. Among these 100K users, this paper studies the
data of 78, 187 users’ data who used the Discover Feed in this time
period. We define each session as a continuous interval of time a
user spends on the Snapchat app, or closes and opens it back within
15 seconds. Figure 1 shows the 𝑧-scores of our data distributions.

3.1

Preliminary Analysis

By defining ad reception as the ratio of watched duration of ads
over the total duration of ads, we conduct a preliminary analysis
to understand how ads are consumed on Snapchat Discover Feed
with varying hours in a day. For this, we measure the coefficient of
variation (CV) of ad reception for each hour of day. CV, expressed as
a percentage, is the ratio of standard deviation to mean, quantifying
the amount of variability with respect to the distribution’s mean —
higher values indicate higher variability. We find that the CV per
hour averages at a high 78.6% (stdev.=1.6), suggesting that users
have high variance in ad reception by hour (ref: Figure 2a).
To visually examine the above variability in ad reception by hour
and user, we cluster users on aggregated behaviors on the platform
(such as the number of app opens, frequency, and amount of posting
and consuming content on Snapchat). We adopt 𝑘-means clustering
(𝑘=20) where the number of clusters is roughly determined using
the Elbow heuristic [97] (Figure 2b). Figure 2c plots a heatmap
of the mean 𝑧-score of ad reception by hour, with each cluster of
users on the vertical axis. We find that the bottom-most row in the
heatmap or the ad reception at an overall level barely shows any
variance across hours. However, the same does not hold true if we
look at the rest of the rows with shades of light and dark distributed
throughout. This suggests that ad reception shows different patterns
both between and within clusters across hours.
These preliminary analyses motivate us to investigate if users
have different “preferred times” of ad consumption (or times of


AdverTiming Matters

100

Density (Sessions)

10 1
10 3

10 2
10 3

10 2

0

10
20
Session Duration (z)
(a)

10 3

10 3

10 5

10 4

10 1

10 1

Density (Users)

Density (Users)

10 1

Density (Ads)

100

CHI ’21, May 8–13, 2021, Yokohama, Japan

10 5

10 4

0

10 20 30
Session Duration (z)

0

(b)

10
20
Number of Ads (z)
(c)

0

5
10
Ad Duration (z)
(d)

Figure 1: Distribution of data by 𝑧-scores of (a) Total duration on platform per user, (b) Duration per session, (c) Number of
ads per user, (d) Ad duration per ad.
the day when ads might be less disruptive), and that clustering
(or stratifying) users with on-platform attributes can provide key
insights on ad consumption. These attributes do not use a user’s
demographic and trait-based information, and therefore, can be
argued to be more privacy-preserving than traditional forms of userprofiling [77]. Concretely, any interventions using these insights
would not access a user’s personal data.

4 AIM 1: AD TIMINGS AND EFFECTIVENESS
4.1 Study Design and Rationale
Ads can disrupt a user’s normal course of action on a social platform [4, 88]. Prior work has explored methodologies to improve ad
effectiveness by showing personalized advertisements to individuals, where major approaches have largely focused on user interests
and content-based personalizations (see Section 2). In this regard,
context- and time- driven factors have remain largely unexplored,
particularly on social media. Motivated by the role of context and
time of day effects [16, 33, 102] and initial insights from our preliminary analysis, we hypothesize that different users have different
preferred times of ad consumption on the platform.
Ideally, such a problem would be best examined in an experimental or A/B test setting; however, these methods have caveats [38]. For
example, experimental allocations of ads may lead to unintended
consequences such as changing platform experiences and risks of
long-term perceptions about the platform. Again, these approaches
are sensitive to particular parameters and thresholds, such as what
quantity of ads can be shown and when — which remain unknown
apriori to experimentation. Given these considerations, we draw
on quasi-experimental approaches on observational data to understand the effect of ad allocations with respect to time preferences
of users [89]. In particular, we adopt a causal framework based on
matching, which simulates an experimental setting by controlling
for as many covariates as possible [42]. This approach builds on the
potential outcomes framework, examining if an outcome is caused
by a treatment 𝑇 by comparing two potential outcomes: (1) 𝑌𝑖 when
exposed to 𝑇 (𝑇 = 1), and (2) 𝑌𝑖 if there was no 𝑇 (𝑇 = 0). Because
it is impossible to obtain both kinds of outcomes for the same user,
this framework overcomes this challenge by estimating the missing
counterfactual for a user based on the outcomes of a matched user
— a user with similar distribution of covariates but differing treatment status. We employ stratified propensity score analysis [76, 95]

to match users and examine ad outcomes in Treated and Control
groups of individuals. This section describes the methodological
considerations and approach in detail.
This paper communicates our insights using 𝑧-score-transformed
quantities from raw data metrics due to privacy and sensitivity
reasons. Importantly, 𝑧-scores are not sensitive to inconsistent magnitudes of absolute values, making normalized comparisons across
multiple measures feasible. By definition, 𝑧-scores quantify the
number of standard deviations by which the value of a raw score
is above or below the mean. Similar standardization techniques
have been adopted in prior social media studies [32]. 𝑧-scores are
calculated as (𝑥 − 𝜇)/𝜎, where 𝑥 is the raw value, 𝜇 and 𝜎 are respectively the mean and standard deviations of the population. Here,
we obtain population 𝜇 and 𝜎 on the entire data per measure. We
interpret positive 𝑧-scores as values above the mean, and negative
𝑧-scores as those below the mean.

4.2

Defining Outcomes: Ad Effectiveness

A causal study typically measures the effect-of-a-cause, and effects
are measured as changes in outcomes. Our work measures outcomes
in terms of ad effectiveness. We draw motivation from prior research
that ad effectiveness is a function of how interested people feel in
watching an ad, and what actions they take following their consumption of the ad (such as buying the product, or other behavioral
markers indicating their interest in the product) [72, 105]. On the
basis of this, we operationalize ad effectiveness using two measures
— 1) Ad Reception or the proportion of time ads are watched over
the total duration of ads in a session and 2) Ad Click Through Rate
(CTR) as the proportion of ads that were clicked on (or that users
swiped up on, in the case of Snapchat).

4.3

Defining Baseline & Measurement Periods

We aim to measure ad effectiveness by conditioning on how ads
were allocated to users. For this purpose, we draw upon recent
causal inference research on observational social media data [94],
to define a Baseline and a Measurement period in the longitudinal
timeline of each user (schematically represented in Figure 3). In
the Baseline period, we aim to compute how users consumed ads
shown at different hours of day (and weekdays). This allows us to
obtain the preferred hours of ad consumption for each user. Then,
in the Measurement period we measure the effect of showing ads in


7

1e8

6

k=20

5

Cluster

80
70
60
50
40
30
20
10
0

Saha et al.

SSE

CV% (Ad Reception)

CHI ’21, May 8–13, 2021, Yokohama, Japan

4
3

0

4

8 12 16
Hour of Day

Mean
20

2

20

(a)

40

60

80

Number of Cluster (k)

100

0
1
2
3
4
5
6
7
9
10
11
12
13
14
15
16
17
18
19
All

2.0
1.5
1.0
0.5
0.0
0.5
1.0
1.5
2.0

0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
Hour

(b)

(c)

Figure 2: (a) Coefficient of Variation (CV) of ad reception across users in dataset by hour of day, (b) Elbow plot to determine
optimal 𝑘 in 𝑘-means clustering: dotted line represents approximate location of elbow, (c) Ad reception per cluster of users by
hour (values are 𝑧-transformed): darker colors indicate greater ad reception.
2.5

Treated Group: Users shown ads similar to their high ad reception hours
Control Group: Users shown ads different to their high ad reception hours

Figure 3: A schematic representation of splitting user longitudinal timelines into baseline and measurement periods.
preferred hours by minimizing the confounds due to ad quantity and
user behavior on the platform. We choose to split the longitudinal
timeline of 78Kusers before and after January 10, 2020, leaving us
with roughly three weeks of data in the Baseline period and six
weeks of data in the Measurement period for each user.

4.4

Defining Treatment: Treated & Control

As we examine the effect of timing ad allocations, our study design
adopts a Treatment Dosage on the basis of preferred times of ad consumption. We operationalize the treatment dosage on how similarly
(or differently) ads were allocated in the Measurement period with
respect to a user’s high (or low) hourly ad consumption in the Baseline period. This builds on the notion that a user who consumed ads
well at H1 hours and poorly at H2 hours during the Baseline period,
would show similar consumption patterns when ads are allocated
to them at H1 and H2 hours in the Measurement period. For each
“hour of the day” in each “day of the week” (henceforth, referred to
as hour-weekday pair), we compute an aggregated average of ad
quantity (number of ads normalized by number of browsed content
tiles) and ad reception per user separately in the Baseline and Measurement periods. First, we obtain the hour-weekday wise vector
of ad reception for each user in the Baseline period (𝑣 1 ). Then, we
obtain the hour-weekday wise vector of ad allocation for each user
in the Measurement period (𝑣 2 ). Finally, we define treatment dosage
as the cosine similarity of vectors 𝑣 1 and 𝑣 2 , computed per user.
Essentially, the greater the dosage, the greater is the likelihood of
ad allocation (in Measurement period) during a user’s preferred ad
reception hours (as inferred from ad consumption behavior in the
Baseline period).

Treated
Control

2.0
1.5
1.0
0.5
0.0

40
Unmatched
Matched
35
30
25
20
15
10
5
0
0.0 0.1 0.2 0.3 0.4 0.5 0.6
Std. Mean Differences

Density (Covariates)

Compute ad reception by hours
for users

Measurement Period

Density (Users)

Baseline Period

0.0

0.2
0.4
0.6
0.8
Dosage (Cos. Similarity)

(a) Dosage

1.0

(b) Matching Balance

Figure 4: Distribution of: (a) Dosage: cosine similarity of ad
reception in Baseline period and ad allocation in Measurement; (b): Balance of covariates in matching.
For a better understanding of the effect of showing ads at preferred hours, we binarize the dosage into treatment and no-treatment
using various thresholds of percentile splits, creating “high similarity” (or Treated) and “low similarity” (or Control) groups. We find
that our results are not sensitive to the choice of varying thresholds
of binarizing dosage into treatment and no-treatment. For clarity,
we report and describe our results using the definition of treatment
as the first tertile of dosage and no-treatment as the last tertile of
dosage — which leads to 16, 501 Treated and 16, 501 Control users
in our dataset (ref: Figure 4a). Later, in Section 7, we revisit the
robustness of our findings with respect to several combinations of
dosage. The same section also examines dosage as a continuous
variable and studies its relationship with ad outcomes.

4.5

Matching for Causal Inference

4.5.1 Matching Covariates. Matching aims to control for covariates so that the effects of treatment are examined between two
comparable groups of users [42]. We note that ad outcomes can be
confounded by factors such as how long someone stays in a session,
or how they engage on Snapchat, or even how many ads were
allocated. To mitigate such confounds in our analyses, we adopt an


AdverTiming Matters

4.5.2 Stratified Propensity Score Analysis. We use matching to find
pairs (generalizable to groups) of Treated and Control users whose
covariates are statistically very similar to one another. The propensity score model matches users based on their likelihood of receiving
the treatment, or the propensity scores. Stratified matching potentially overcomes the challenges of exact one-to-one pair matching
which can lead to biases [51]. Our stratified matching approach
groups users with similar propensity scores into strata [48]. Every
stratum, therefore, consist of users with comparable covariates.
This approach allows us to isolate and estimate the effects of the
treatment within each stratum.
To compute the propensity scores, we build a logistic regression
model that predicts a user’s binarized treatment status (0 for Control
and 1 for Treated) based on their covariates. We segregate the
remaining distribution into 100 strata of equal width — and discard
those strata containing less than 50 users which further ensures that
our causal analysis per stratum remains restricted to a sufficient
number of similar users, and therefore is minimally biased [95].
This leads us to a final matched dataset of 92 strata consisting of
16,003 Treated and 15,682 Control users in total.
4.5.3 Quality of Matching. To test that our matching yields statistically comparable Treated and Control users, we evaluate the
balance of covariates. For each covariate, we compute the standardized mean difference (SMD) in the Treated and Control groups in
each of the 92 valid strata. SMD calculates the difference in the
mean covariate values between the two groups as a fraction of
the pooled standard deviation of the two groups. Two groups are
considered to be balanced if all the covariates reveal SMD lower
than 0.2 [48, 101]. This condition is satisfied by a majority of the
covariates in our matched datasets, and we obtain a 18.9% reduction in the SMDs of matched from unmatched samples (𝑡 = 0.19,
𝑝<0.05) (Figure 4b). Therefore, we can consider our matching to
yield balanced Treated and Control groups of users that allow our
ensuing analyses to be controlled on observed covariates.

4.6

Measuring Treatment Effect

To examine the effect of timing ads based on users’ Baseline-inferred
preferred ad times (or treatment), we compute the differences in
the outcomes (ad effectiveness) between the matched Treated and
Control users in the Measurement period. We compute these differences in terms of effect size (Cohen’s 𝑑) and paired 𝑡-tests which

Treated
Control

0.5

Treated
Control

100

0.4

Density (Users)

Density (Users)

10 1

0.3

10 2

0.2

10 3

0.1
10 4

0.0

2

0
2
4
z-score (Ad Reception)

0

5

(a) Ad Reception

10
15
20
z-score (Ad CTR)

25

(b) Ad CTR

Figure 5: Ad Outcomes: (a) Ad Reception and (b) Ad CTR.
Treated users show greater ad outcomes on an average.

Rel. Treatment Effect (RTE)

approach called matching — when conditioned on high dimensional
covariate data, matching can minimize biases compared to naive
correlational analyses [42]. Our approach controls for a variety of
covariates so that the compared Treated and Control show similar
baseline behaviors. Drawing on prior work [48, 76, 96], we use 41
covariates (listed in the Appendix Table A1). The first set of covariates are based on aggregated Baseline data spanning across the
number and frequency of app opens, social interactions, different
types of interactions, etc. We also include a second set of covariates obtained from the Measurement data based on the number
of sessions, average duration of sessions, and the average number
of ads exposed, to ensure that matched Treated and Control users
had comparable engagement on the platform and were exposed to
similar quantity of ads.

CHI ’21, May 8–13, 2021, Yokohama, Japan

Ad Reception
Ad CTR

2.0
1.5
1.0

0

20

40

60

80

Stratum

100

Figure 6: Ad outcomes per matched strata of users.
Table 1: Summary of mean 𝑧-scores in Treated and Control
groups along with Relative Treatment Effect (RTE), Effect
Size (𝑑), paired 𝑡-test and 𝐾𝑆-test. Statistical significance reported after Bonferroni correction (*** 𝑝<0.001).
Outcome

Tr. (z)

Ct. (z)

RTE

d

t-test

KS-test

Ad Reception
Ad CTR

0.29
0.06

-0.33
-0.09

1.49
1.51

2.27
1.11

15.28***
7.52***

0.83***
0.55***

also helps us to evaluate the statistical significance in differences.
We also conduct Kolmogorov-Smirnov (KS) test, which tests against
the null hypothesis that the outcomes in the Treated and Control
groups are drawn from the same underlying distribution.
To quantify the effect of treatment, we measure the Relative
Treatment Effect (RTE) per outcome measure in every strata, as
the ratio of the likelihood of the outcome in the Treated group to
that in the Control group [48, 95]. Next, using a weighted average
across all the strata, we obtain the mean RTE of the treatment per
outcome measure. An outcome RTE greater than 1 would mean that
the outcome is greater in the Treated users in the Measurement
period — or in our case, that allocating ads according to preferred
timing increases the likelihood of ad effectiveness.

4.7

Findings: What is the Effect of Timing Ads?

Figure 5 shows average changes of ad outcomes in Treated and
Control users — indicating higher ad outcomes for Treated users.
Table 1 reports the differences in outcomes of the Treated and


CHI ’21, May 8–13, 2021, Yokohama, Japan

Control users in terms of RTE, Cohen’s 𝑑, paired 𝑡-test, and KS test.
These tests indicate statistically significant outcome differences in
Treated and Control users. The high magnitude Cohen’s 𝑑 values
(𝑑>0.5) and 𝑡-statistic, along with the positive signs indicate that
the Treated group shows significantly higher outcomes than the
Control group. Additionally, the fact that ad reception shows an RTE
of 1.49 and ad CTR shows an RTE of 1.51, indicates that timing ads
(treatment) leads to more effective ad outcomes (RTE>1). Figure 6
reveals that the RTE>1 holds for a significant majority of user strata
for both ad outcomes.
This reveals that although matched Treated and Control users
are very similar on baseline behavior and ad consumption, along
with Measurement period’s ad exposure and platform activities (as
per matching), they show very different receptivity to ads in the
Measurement period. Therefore, we draw two inferences. First, the
short baseline period of understanding on-platform activities of
users can lead us to passively infer preferred times of ad consumption.
Second, when users are shown ads at preferred times, they are more
likely to be receptive to the ads — or they would watch the ads
longer, and are more likely to click on them. On the other hand, ads
shown during less preferred hours may not only be worse received
but may also elicit frustration or seem intrusive to users [27].

5

AIM 2: USER BEHAVIOR AND AD
EFFECTIVENESS

A core finding of Aim 1 is that users are more likely to be receptive
to ads if ads are shown according to their preferred times. However,
allocating ads in this way may not always be feasible — for example,
a user may show inactivity or hyperactivity during their preferred
times, each of which may lead to extremes of no ad or too many
ads to be allocated, thereby affecting either or both of platform
revenue and user experience. Our Aim 2, in particular, examines
alternative means of effective ad allocation which is robust to a
user’s (unknown apriori) future platform activity. That is, we investigate how in-the-moment user behaviors associate with a user’s
ad consumption at varying times of a day, which would provide
insights to conduct context-centric ad reallocations considering
factors beyond time of the day.
First, for every user, we define each hour as a less-preferred or a
more-preferred hour of ad effectiveness on the basis of where the
hour is on either side of the user’s median ad reception during
Baseline period. Consequently, we label every session in a user’s
Measurement period to be either during less-preferred or morepreferred hours of ad exposure for the same user. We operationalize
a number of on-platform user behavior measures and examine
their relationship with ad effectiveness, conditioned on preferred
times of ad exposure. This section explains the relationship of ad
effectiveness with on-platform user behavior.

5.1

Comparing Ad Effectiveness by Sessions

We aim to understand how ad allocations can be improved for a
particular session beyond the timing of the ad. Therefore, given
a user and a session, we conduct a two-fold examination of ad
effectiveness based on 1) if the session is during a more-preferred
ad time of the user, and 2) characteristics of the session in terms of
on-platform user behaviors. For sessions in less-preferred times, we

Saha et al.

conduct a paired 𝑡-test of in-the-moment session characteristics of
those sessions when ad effectiveness was higher than median for a
user (or high effective) and those sessions when the ad effectiveness
was lower than median for the user (or low effective). Similarly,
for more-preferred times, we conduct a paired 𝑡-test of session
characteristics of high ad effective and low ad effective sessions
per user. Essentially, a statistical significance in these comparisons
would indicate that in-the-moment user behaviors associate with ad
effectiveness within and outside preferred times of users. The sign of
the 𝑡-statistic would indicate the directionality of the measure with
ad reception, with positive values indicating a positive association
and negative values indicating the opposite.

5.2

Ad Effectiveness by Momentary Behaviors

Ad consumption is known to be a function of people’s momentary
psychological and behavioral states (Section 2). For instance, ad
consumption (and more generally, content consumption) is a function of what an individual does, or how active or tired they are at
a particular block of time [13, 102]. As a proxy of behavioral and
psychological states, we draw on prior work to operationalize a
variety of passively inferred in-the-moment states on the Snapchat
platform [96], which are explained below. We first motivate and
operationalize each of these in-the-moment behaviors and follow
that with our observations with respect to the relationship with
ad effectiveness in each. We are particularly looking for insights
to recommend ad allocations with respect to preferred times with
minimal compromise on ad effectiveness, i.e., 1) when to increase
ads during less-preferred times and 2) when to decrease ads during
more-preferred times. Table 2 summarizes the differences in high
and low ad effective sessions by preferred times of users.
Duration. We operationalize duration as the length of time a user
spends in a session. We note that although longer sessions indeed
allow the platform to show more ads, longer sessions also plausibly
correlate with a user’s leisure times, or when they are less involved
with offline activities. Table 2 shows that 𝑡-tests on high and low
effectiveness ads during less-preferred (𝑡=7.27) and more-preferred
(𝑡=15.05) times is positive with statistical significance, suggesting
that ad effectiveness positively associates with length of session.
Therefore, a recommendation at less-preferred times would be to
increase ads in longer sessions, and that at more-preferred times
would be to decrease ads in shorter sessions.
Activity. We operationalize activity as the frequency of touch actions (excluding text-typings) in a session. A more active user may
be more likely to skip ads and move on to a different content. For
activity, we find that 𝑡-tests for both less-preferred times (𝑡=−5.26)
and more-preferred times (𝑡=−3.78) is negative with statistical significance. This indicates that activity shares a negative relationship with ad effectiveness. Therefore, a recommendation for lesspreferred times would be to increase ads during low-activity sessions, whereas a recommendation for more-preferred times would
be to decrease ads during high-activity sessions.
Interactivity. One way to study user behavior on a social platform
is measuring a user’s degree of interactiveness in terms of posting,
responding, and consuming content [96]. We operationalize interactivity as the ratio of content created to content consumed within


AdverTiming Matters

CHI ’21, May 8–13, 2021, Yokohama, Japan

Table 2: Summary of in-the-moment user behaviors with respect to ad effectiveness on the same user. Statistical significance
is conducted using paired 𝑡-tests and 𝑝-values are reported after Bonferroni correction (* 𝑝<0.05, ** 𝑝<0.01, *** 𝑝<0.001). For
significant rows, violet bars represent positive magnitudes, whereas orange bars represent negative magnitudes.
Measure ↓
Effectiveness →

High

Duration
Activity
Interactivity
Interaction Diversity
Distractedness
Extra-socialness

-.031
-.006
.001
-.012
.010
.004

Less preferred Time
Low t-test
-.047
.012
.014
.007
.011
.005

7.27
-5.26
-3.18
-5.61
-0.22
-0.21

a session. Here, content creation on the Snapchat platform includes
creating stories, posting updates, and sending and replying to chat
messages, while content consumption includes viewing others’ stories and updates, and browsing through different content within a
session. Table 2 shows that for both less-preferred times (𝑡=−3.18)
and more-preferred times (𝑡=−5.25), 𝑡-statistic is negative. This suggests that interactivity negatively associates with ad effectiveness,
or the higher the interactivity of a user in a session, the lower their
ad reception. A plausible interpretation of our Interactivity results
is that, when users encounter ads on Discover Feed during highly
interactive sessions, they might feel particularly disrupted and have
specific actions available (e.g. chatting with a friend), motivating
them to skip ads. Therefore, our findings recommend to increase ads
at “low interactivity sessions of less-preferred times”, and decrease
ads at “high interactivity sessions of more-preferred times”.
Interaction Diversity. An aspect of social media behavior is the
diversity of interactions a user conducts during a session [96]. We
operationalize interaction diversity as the standard deviation of
time spent in each kind of activity conducted in a session, where insession activities range across sending or replying to chats, viewing
and posting updates, etc [37]. As above, we find statistical significance and negative 𝑡-statistics for both less-preferred (𝑡=−5.61)
and more-preferred (𝑡=−4.78) times. This suggests that interaction
diversity negatively associates with ad effectiveness. Therefore, our
findings recommend to increase ads at “low interaction diversity sessions of less-preferred times”, and decrease ads at “high interaction
diversity sessions of more-preferred times”.
Distractedness. Although there is no accurate means to passively
infer how distracted a user is, we hypothesize that a distracted user
(with respect to the app) would plausibly conduct more non-app
related activities during a block of time, such as switching to another
app, or attending a phone call, or doing something else offline and
returning back to the app, etc. We operationalize distractedness
as the quantity of application opens and closes during a session
(recall that a session does not end until a user has been inactive
for 15 seconds). For less-preferred times, we find no statistical
significance in the differences of distractedness in high and low
ad receptive sessions. However, at more-preferred times, we find
a positive 𝑡=2.01 with statistical significance. This might mean
that when users visit the platform being less distracted, they are
plausibly doing something with a “particular purpose” and may not
be willing to consume ads despite being at their preferred times of

p

High

More preferred Time
Low t-test

p

***
***
**
***

-.004
-.010
-.007
-.018
.017
.005

-.038
.003
.012
-.003
.009
.010

***
**
***
***
*
*

15.05
-3.78
-5.25
-4.78
2.01
-1.35

ad consumption. This suggests a recommendation that during morepreferred times, ads can be decreased in less-distracted sessions.
Extra-socialness. Platforms such as Snapchat, Instagram, and
Facebook also provide features outside conventional forms of social
media activities such as posting, chatting, and socially interacting
with others, e.g., playing games, using a camera and applying filters
or lenses on their photos, etc [37]. We operationalize the ratio of
time spent on these activities to the total session duration as extrasocialness of a session. Comparing extra-socialness of different ad
reception sessions at less-preferred times, we find no statistical
significance, and at more-preferred times, we find 𝑡=−1.35 with
significance. This indicates that, at more-preferred times, extrasocialness negatively correlates with ad effectiveness, or when a
user is interested in non-social platform activities, they are less
likely to be receptive to ads, finding them disruptive. Correspondingly, a recommendation would be to decrease ads during high
extra-social sessions at more-preferred times of users.
Summary of Insights and Recommendations. The above observations suggest that ad effectiveness positively correlates with
duration and negatively correlates with activity, interactivity, and
interaction diversity for any time; positively correlates with distractedness and negatively correlates with extra-socialness at morepreferred times. Therefore, recommendations for increasing ad allocation at less-preferred times are in sessions with 1) high duration,
2) low activity, 3) low interactivity, and 4) low interaction diversity.
On the other hand, recommendations for decreasing ad allocation
at more-preferred times are in sessions with 1) low duration, 2) high
activity, 3) high interactivity, 4) high interaction diversity, 5) low
distractedness, and 6) high extra-socialness.
While we study the relationship between on-platform momentary behaviors and ad effectiveness here, approaches to infer momentary behaviors in real-time or apriori are beyond the scope
of this study. However, these can be implemented using real-time
dynamic rules (e.g., if the current session duration or session interactivity is already higher than the user’s median at a given time) or
using predictive machine learning techniques [6, 52].

6

AIM 3: EFFICACY OF OUR INSIGHTS

Our Aim 1 and 2 derived insights about ad consumption by ad
allocations at preferred hours and on-platform behaviors respectively, we ask how these insights would influence business value?
We conduct a simulation experiment of increasing and decreasing
ad allocations based on recommendations guided by our first two


CHI ’21, May 8–13, 2021, Yokohama, Japan

research aims. Additionally, we were concerned that intervening
in the status quo of the ad allocation process could create concentrated ad allocations, i.e. certain users bearing the burden of high
“ad load”. Thus, this additional investigation aims to evaluate how
simulated interventions might affect the fairness of ad allocations in
terms of the concentration of ad load among users. This simulation
experiment can inform an ad allocation system about weighing
in ad allocations to users who are at extremes of ad exposure to
balance the quantity of overall ad exposure across all users on the
platform, i.e., a more balanced but effective allocation of ads.

6.1

Simulating Balanced Ad Reallocations

We first quantify the normalized ad quantity per user as the ratio of
the total number of ads over the total number of pieces of content
(or Discover Feed stories) seen by the user. Figure 7a shows the
min-max scaled distribution of normalized ad quantity within our
Measurement dataset. We identify high and low ad-exposed users
as the top and bottom quartile of normalized ad quantity. Because
these users are at extremes of ad exposure during a particular period,
a platform would ideally like to first change the ad quantity of these
users to similarly balance out normalized ad quantity across all
users. Accordingly, we simulate new ad distributions by decreasing
the ad quantity of high ad-exposed users and increasing the ad
quantity of low ad-exposed users in the following three ways:
Preferred Time based Reallocation. In this simulation approach,
we use recommendation solely from Aim 1, i.e., for high-ad exposed
users, we decrease the number of ads in less-preferred hour sessions
(in hours where ad reception in Baseline period is lower than the
median) by 90% per session and allocate the difference in quantity of
ads proportionately across the preferred hour sessions (ad reception
in Baseline higher than the median) of the low ad-exposed users.
Session Activity-based Reallocation In this simulation approach,
we use the recommendations from Aim 2 to modulate the ad load
of high and low ad exposed users. In high ad-exposed users, we
decrease the ad quantity in a union of sessions with low duration
(lower than bottom 25 percentile), high activity, high interactivity,
high interaction diversity, etc. (higher than top 25 percentile) by
90% per session. Similar to the above, we allocate the difference
in quantity of ads proportionately in sessions of low ad-exposed
users, in those sessions with low activity, low interactivity, low
interaction diversity, etc. (lower than bottom 25 percentile).
Baseline Reallocation. In the third simulation approach, we build
a baseline reallocation which does not use the insights from the
previous two research aims. This is aimed to sort of emulate a statusquo of platforms that follow fair and balanced ad allocations — when
users are identified with extremes of ad exposure in real-time, their
ad exposure is modulated to balance in the upcoming period. In
the baseline reallocation, we randomly select 𝑛 sessions from high
ad-exposed users and decrease their ad load by 90% per session,
and allocate the difference in randomly selected sessions of low adexposed users. We choose 𝑛 as the same number of ads reallocated in
the above two allocations, as the baseline reallocation is to compare
against the two other reallocation strategies. To eliminate any effect
due to chance, we build 1,000 permutations of different 𝑛 sessions
where ads are manipulated.

Saha et al.

6.2

Evaluating Ad Reallocations

We evaluate ad reallocations on the basis of ad value, which is a
function of how effective ads are in a session. We measure ad value
as a product of ad reception and the number of ads in a session.
Theoretically, ad value would be correlated with actual monetary
value generated based on ad effectiveness [72, 105]. We note that
our simulations are only within the limits of the observational
data, and our measure of ad value assumes a user’s ad reception
in a session to be the observed value. However, it is likely that the
counterfactual ad reception might change if the ads are actually
reallocated — which remains unknown unless an actual experiment
of ad reallocation is conducted.
Figure 7b shows the distribution of ads across users in multiple
simulation strategies. We find that compared to the actual distribution, 1) the baseline simulation decreases the standard deviation
by 9%, 2) the simulation by activity decreases by 6.5%, and 3) the
simulation by preferred time decreases by 7.9%. Lower standard
deviation suggests that all our simulated forms of ad reallocations
result in a balanced allocation of ads across users.
Next, Figure 7c shows the distribution of ad value by simulation
strategies. We find that compared to overall ad value in the actual
distribution: 1) the baseline simulation only marginally increases
ad value by 0.07%, whereas 2) the simulation by activity strategy
increases ad value by 2.78%, and 3) the simulation by time strategy
increases ad value by 7.09%. Both of these percentage changes actually correspond to a significant increase in overall value considering
the scale of userbase and volume of data and ads on the platform,
e.g., ∼250M daily active users on Snapchat [113].
Finally, drawing on permutation test approaches [5], we iterate
over the 1,000 permutations of baseline reallocations, to find the
probabilities (𝑝-values) of the ad value improvement in the baseline
reallocation over the two insight-driven reallocations. We find these
probabilities to be zero, suggesting that we can reject the null
hypothesis that insight-driven simulations only beat the baseline
ad reallocation by chance.

7

ROBUSTNESS OF FINDINGS

This section examines the robustness of our findings with respect
to the researcher decisions we made in our study. First, we conduct
methodological robustness tests on parametric choice and approach
in our study design. Then, we theoretically contextualize our definition of “ad effectiveness” measures with respect to how it is defined
traditionally in the literature — a success would provide criterion
and construct validity to our study. Together, a convergence in
findings along with theoretical grounding would ensure robustness
and validity of our findings [60].

7.1

Methodological Robustness

Binarizing Treatment Dosage Thresholds Recall that our study
design relies on chosen threshold of binarizing treatment and notreatment (Section 4). Therefore, we test if our findings hold robust for any other thresholds of treatment. For this, we vary the
threshold of treatment dosage and re-conduct the entire analyses
on measuring treatment effects (Aim 1), including matching and
computing differences in outcomes for matched Treated and Control users. We vary the threshold parameter 𝛼 in such a way that


AdverTiming Matters

CHI ’21, May 8–13, 2021, Yokohama, Japan

7

Actual
Sim. Random
Sim. Activity
Sim. Time

8
Density (Users)

6

6

4

2

10 4
10 5

2

10 6

1
0
0.0

0.1

0.2 0.3 0.4
Normalized Ad Count

0.5

0.6

0
0.0 0.1 0.2 0.3 0.4 0.5 0.6
Normalized Ad Count

(a) Ad Exposure

10 2
10 3

4

3

Actual
Sim. Random
Sim. Activity
Sim. Time

Density (Ads)

Density (Users)

5

10 1

(b) Ad Exposure

10 7
0

100

200
300
Ad Value

400

(c) Ad Value

Figure 7: Distribution of a) normalized ad count by user in the actual dataset, b) normalized ad count as per simulations of ad
reallocations: the density plot for each simulate reallocation is thinner in width compared to the actual distribution suggesting
a more balanced ad allocation across users, c) ad value as per simulations: overall ad value is highest for simulated by time
reallocation (Sim. Time) followed by simulated by behavioral activty based reallocation (Sim. Activity).
Ad Reception
Ad CTR

Rel. Treatment Effect (RTE)

3.00
2.75
2.50
2.25
2.00
1.75
1.50
1.25
0.1

0.2

0.3
Dosage

0.4

0.5

Figure 8: RTE with varying dosage 𝛼. For each 𝛼, treatment
is top 𝛼 ∗100 percentile of dosage and no-treatment is bottom
𝛼 ∗ 100 percentile of dosage.

dosage (cosine similarity between Baseline ad reception and Measurement ad allocatino) in the top 𝛼 ∗ 100 percentile is considered
treatment, and that in the bottom 𝛼 ∗ 100 percentile is considered
no-treatment. Figure 8 plots the change in RTE of ad effectiveness
measures, with respect to changing the threshold dosage 𝛼. We
find that the RTE of both ad effectiveness measures remain greater
than 1 (along with statistical significance as per 𝑡-test and effective
size), indicating that ads were more effective on Treated users or
users who were shown ads at their preferred hours. We also find a
roughly monotonic decrease in RTE with respect to increasing 𝛼,
suggesting the greater the similarity of ad allocations with people’s
preferred hours, the greater is the likelihood of ad effectiveness.
Using Treatment Dosage as a Continuous Variable. Another
component of our work includes the decision to estimate the outcomes by binarizing the treatment dosage. Such an approach not

only better serves interpretability purposes but also emulates conventional RCT or experimental approaches where one group is
treated (e.g., drug) and the other group is not (e.g., placebo). Though
less likely, binarizing treatment might however introduce new biases in the analyses leading to misleading findings (e.g. a drug in
low dosage may not be as effective as it is in high dosage [40]).
Therefore, we test the findings if the treatment is considered as a
continuous variable.
For this, we build a linear regression model that uses all the 42
covariates in our dataset, along with the treatment as independent
variables and the ad reception as the dependent variable. While this
approach is not particularly “causal”, it allows us to infer the relationship of the treatment and the outcomes. We eliminate correlated
features using variance inflation factor (VIF) (threshold=10) [19, 70].
The regression model shows an adjusted 𝑅 2 of 0.87, and Table 3
reports the standardized coefficients of relevant variables. In particular, we find that the treatment dosage shows the greatest magnitude
with a positive coefficient of 0.22 (𝑝<0.05). Likewise, repeating the
same experiment with ad CTR as dependent variable leads to similar signs of coefficients. Together, the findings from our regression
analysis aligns with our matched and binarized treatment analysis
that treatment (or showing ads during preferred hours) leads to a
greater likelihood of ad effectiveness.
The consistency of results via different approaches reveals that
our examination is not sensitive to the choice of treatment dosage
parameter or our study design, but rather a reflection of ad consumption behavior on Snapchat.

7.2

Contextualizing within the Literature

As a final robustness check, we compare our results with that found
in previous literature. Traditionally, ad effectiveness is defined as
whether an individual buys a commodity following exposure to an
ad [13]. If our observations of ad effectiveness match prior literature,
we view that as criterion validity to our measures of ad effectiveness


CHI ’21, May 8–13, 2021, Yokohama, Japan

Saha et al.

Table 3: Coefficients of linear regression of relevant covariates as independent variables and ad reception as dependent
variable, * 𝑝<0.05, ** 𝑝<0.01, *** 𝑝<0.001. For significant rows,
violet bars represent positive magnitudes, whereas orange
bars represent negative magnitudes.
Measure

Coeff.

p

Treatment Dosage
Duration
Activity
Consumption
Curation

0.22
0.05
-0.04
-0.03
-0.03

*** Num. App Opens
** Interactivity
*
Interaction Diversity
−
Distractedness
−
Extra-Socialness

Measure

Coeff.

p

-0.06
-0.11
-0.07
0.01
0.03

**
*
*
−

*

and construct validity to our study [75]. We test ad effectiveness in
two ways: in terms of the time of day and as day of the week.
7.2.1 Time of the day. We construct our first hypothesis based on
prior work comparing ad effectiveness at days and nights [102] that:
ad effectiveness is higher during the daytime compared to evenings
or nights. In our work, we first bucket a user’s local time into day
(6 AM–6 PM) and night (6 PM–6 AM). While we also attempted to
build more granular buckets or even look at ad effectiveness over
more continuous forms of time, we find effects are generally washed
out given the across-user variability in ad reception, also evident
in our preliminary analysis referring to Figure 2c, particularly in
the bottom-most/“All” user row. Instead, binary buckets (day and
night) provide us the opportunity to compare and contrast users’
receptivity to ads between broader timespans of a day.
For both Treated and Control groups, we conduct paired 𝑡-tests
between a user’s ad outcomes during the day and during the night.
Table 4 reports the differences in ad reception by time of the day.
First, understandably, ad effectiveness for Treated users is higher
than Control users as also reflected in previous analyses (Section 4).
Next, for both Treated and Control users, ad effectiveness is higher
during the day than night with statistical significance and large
𝑡-statistics, supporting prior research on ad effectiveness [102].
7.2.2 Day of the week. Prior work compared ad effectiveness on
weekends and weekdays [13], and saw differences, particularly on
the basis that weekends are associated with more home, leisure,
and family events that might elicit more pleasant effects in people’s
mood and correspondingly in their receptivity to ads. Therefore,
we construct our hypothesis that: ad effectiveness is higher on the
weekends compared to weekedays.
We statistically compare ad effectiveness on weekends and weekdays, as reported in Table 4. First, ad effectiveness is higher for
Treated than Control users. Next, within Control users, we find
that both forms of ad outcome are higher during the weekends than
on weekdays. In contrast, in the case of Treated users, ad reception
during the weekdays and weekends do not differ with statistical
significance. This indicates support for our hypothesis in the case
of Control users, and lack of support in the case of Treated users.
These findings suggest that users in the Treated group already see
ads at their preferred time, and as a result the weekend/weekday
effect is diminished. Therefore, whether timing ads likely plays a
stronger role than day of the week effect — future research may be
able to shine more light on this.

8 DISCUSSION
8.1 Theoretical Implications
Our work opens up discussions on understanding ad allocation
and consumption in new forms of media. Traditional media (television, newspapers) drive ads dedicated to audience groups, and ad
effectiveness typically measures the amount of product purchases
(by ad influence). In recent times, not only with the increasing
use of online social platforms, but also with the ubiquity of smart
and personal devices, ads are allocated in various novel ways. The
affordances not only enable platforms to customize and allocate
ads in a personalized fashion, but also provide users with choices
to skip and ignore ads. Importantly, negative perception towards
ads can cause user fatigue and exacerbate their perception of the
platform [12]. This calls for a need to better understand ad consumption and accordingly design robust and dynamic ad allocation
strategies. Our work reveals that when ads are allocated in a better
fashion by accounting for user- and context-centric factors (e.g.,
time and platform engagement), users could be more receptive to
ads, which corresponds to prior observations regarding intrusiveness and likeability of ads [50, 63].
We have couched our observations in theories from marketing
science, psychology, and cognitive science. Our work augments
prior research which largely studied how the content of ads matters
in changing user experience on online platforms [4, 17]. Our work
provides valuable insights regarding the importance of context and
momentary factors in understanding ad effectiveness. In particular,
our observations suggest that timing ads is a factor that cannot be
ignored when allocating ads on social media.
Along similar lines, our work also reveals how blanket approaches
of ad allocation or approaches based on average user behavior may
not be as effective. For instance, these approaches typically assume
a linear relationship between a user’s time spent in a session and
the number of ads shown: ads are shown after a fixed duration
or after showing a fixed number of pieces of content. However,
these approaches ignore the cognitive state of users which can vary
due to time of day effects or due to users’ daily routines, or even
momentary psychological states such as feeling social or excited at
a particular moment [33, 102]. Instead, our work finds that when
ads are allocated by accounting for these factors, ad effectiveness is
higher without compromising the user activities on the platform.

8.2

Practical and Design Implications

Individual-centric Implications. Our work has implications for
making responsible advertising — advertising that aims to not only
increase platform revenue, but also minimizes user dissatisfaction
caused by ads, helping to keep the users better engaged with the
platform [103]. Our work contributes towards the niche aspect of
“preferred timings” and provides an approach to balance ad effectiveness and user experience. Our approach can help to minimize
the privacy intrusions generally associated with targeted advertising: We can reduce the use of profiling to target ads, and obtain
preferred ad timing on de-identified features and short-term data.
Because users typically dislike ads and do not like to share their
data with platforms for ad targeting [73], they often use tools such
as ad-blocking and private browsing that do not share cookies and
browser history with advertisers. Some platforms disallow these


AdverTiming Matters

CHI ’21, May 8–13, 2021, Yokohama, Japan

Table 4: Summary ad effectiveness (𝑧-scores) by hour and weekday on the same user. Statistical significance is conducted using
paired 𝑡-tests and 𝑝-values are reported after Bonferroni correction (* 𝑝<0.05, ** 𝑝<0.01, *** 𝑝<0.001). For significant rows, violet
bars represent positive magnitudes, whereas orange bars represent negative magnitudes.
Measure
Weekdays
Ad Reception
Ad CTR

Ad Reception
Ad CTR

Treated Users
Weekends t-test

0.17
-0.38

0.12
0.55

0.95

Day

Night

t-test

0.48
0.43

-0.16
-0.20

Weekdays

-8.36***

-0.34
-0.64

0.04
0.47

Day

Night

0.08
0.33

-0.40
-0.57

7.42 ***
4.18
***

privacy-preserving practices, forcing the user to trade off their
data in order to access the content. Potentially, users may be more
comfortable sharing only their momentary (session-level) data, and
our work shows that platforms can make effective ad allocations
by only using these minimal, momentary user data.
Further, the efficacy of recommending content on the basis of
time and context we have shown, suggests design implications that
take user agency and user preferences into account [103]. Recently,
the HCI community has demonstrated the value of user-contributed
preferences of notifications and interruptions [66, 79, 103]. In line
with this, platforms could ask users which times of the day they
are more inclined to view ads, and allocate ads accordingly. This
approach will require more insights in potential ways users could
game the system (users might provide preferred times of ads when
they would likely not visit the platform).
Platform-centric Implications. Our methodology allows platforms to allocate ads in an effective, fair, and less-intrusive way. A
recent survey revealed three major categories of ad dissatisfaction
are intrusiveness, annoyance, and disruptiveness of ads [108]. Users
often use ad blockers and other tools that prevent ads on online
platforms [30, 71] — these approaches raise nuanced questions surrounding the sustainability of platforms surviving on ad-driven
business models [4]. Consequently, to protect user base and minimize ad-based interruptions, some platforms are moving away
from ad-based models to some form of subscription-based models [31, 109]. However, such models have their own caveats, such
as inequity of information access on the internet, and online services could become a function of an individual’s ability to pay. Our
work suggests somewhat of a middle-ground: by optimizing ad timings and allocations when users are less likely to feel interrupted,
platforms can consistently provide equitable content access and
experience to users, and better sustain the ad revenue ecosystem,
with less user dissatisfaction.
Towards Fewer Ads. Our work has implications towards optimizing other forms of ad allocations on social media, including ad
spacing and ad loading. One can draw an insight that if we can
allocate ads optimally in an effective fashion, we can plausibly reduce the overall quantity of ads if certain revenue goals are already
achieved with smaller quantity of, but better-allocated (timed) ads.
This can help minimize practices such as non-skippable ads (ads
which cannot be skipped) or forced ads (ads which prevent any content consumption without being watched). Solutions of minimal ad
allocations would be well-appreciated by the users, improving the

Control Users
Weekends t-test

p

p
-8.27 ***
-9.32***

t-test
7.22
6.78

***
***

general user experience, potentially leading to higher user retention on the platform [65]. A better ad allocation strategy provides a
method for platforms to judiciously serve effective ads. As a result,
such platforms can become more attractive to users.
Small Data and Privacy-sensitive Approaches. Research highlights several biases in ad delivery [3, 56, 85]. For instance, demography and inferred-user interest-based targeting can be deemed
privacy-intrusive, unethical, and surveillance-promoting [41, 82,
88]. In contrast, our work shows a novel means to increase ad effectiveness that does not lean on these critiqued approaches. Our
approach only requires short-term user data (e.g. a few weeks) instead of using long-term historical data. Long-term data do not only
increase privacy concerns, but are also less robust to changes in
both human behavior and platform affordances [9]. So, small-datadriven approaches that do not compromise on the user experience
can open up new opportunities in ad and content recommendation.
Other Content Recommendations. While we primarily focus
on ads, our work also has implications for other types of content.
Our work provides general insights for when to show content to
users. This could inform design strategies for recommendations
and notifications for preferred user content. Prior work showed
the value of context-aware recommendations for improving user
engagement on mobile platforms [47, 66]. The on-platform behaviors we studied (particularly in Section 5) can guide designing such
recommendations that take a user’s momentary state into account.
Implications for Experimental Approaches. As we noted earlier, causal effects are best studied with experimental approaches,
which however, come with risks, e.g., certain treatments (design
changes) may affect the perception of users and impact user retention. Moreover, in the case of continuous treatments, it is often
difficult to determine the appropriate dosage to experiment on. Our
study adopts a quasi-experimental design to show that a particular treatment (timing ads) can be effective. Our computational
framework also quantifies “preferred timings” based on observed
ad outcomes in a small time period. Therefore, our findings can help
to formulate appropriate parameters (or dosage cutoffs as shown
in Section 7) to conduct careful experimental studies to verify and
adopt design changes on platforms [42, 71].
Substitute or a Complement to the Existing Ad Allocation
System? Lastly, we raise a critical point. We conduct our study
on a system already optimized (in some form) for ad allocations.
Therefore, our effects may be even bigger if we had a different
baseline. Arguably, our study only builds on the top of the existing


CHI ’21, May 8–13, 2021, Yokohama, Japan

system which might already be privacy-intrusive and be using inferred user interests based targeting — the very points on which we
discuss several implications above. In this regard, it indeed remains
unexplored whether momentary and context-driven features will
be adopted in practice to improve ad effectiveness. There is a risk
that companies will stack profile and momentary state approaches
(instead of replacing the profile-based approaches), which could
potentially be more privacy invasive. However, our study encourages considering and evaluating these alternative strategies that
conduct responsible and non-invasive ad allocations. It would be
immensely insightful if future research suggests that we can (or cannot) significantly minimize or even eliminate any sort of profiling
and demographic based targeting approaches. Ad targeting is coming under increased scrutiny, and as companies and governments
are putting in place more privacy restrictions [107], our approach
can help future-proof the ecosystem of ad-based platforms. Overall, an important takeaway of this work illustrates the importance
and feasibility of building complementary methodologies which
simultaneously consider a user’s privacy and optimize for user
experience and business value for long-term sustainability.

8.3

Ethical and Privacy Implications

We note that our work bears ethical implications. Our work is predominantly motivated by the idea that we might move away from
traditional forms of user profiling and using static demographic
and trait-based information that content recommendation algorithms infer, which can be biased and unfair [41, 82]. However,
this work can be (mis)used to conduct new forms of user profiling on people’s online behavior. Online platforms could (mis)use
our approach to conduct newer and plausibly unknown forms of
biased and intrusive ad targeting, e.g., if these algorithms incorporate not only “who someone is”, but also “what someone does
when”. Pandit and Lewis described, “the use of personal data is a
double-edged sword that on one side provides benefits through personalisation and user profiling, while the other raises several ethical
and moral implications that impede technological progress” [77].
Therefore, we need to consider balancing the costs and benefits
of these approaches to implement them in ethical and privacypreserving fashion. While arguably anonymized and on-platform
in-the-moment behavior is more ethical and less biased compared
to demographic, static, and prior-assumptions based stratification,
we also recognize the possibility of expectation mismatches between users’ self-conceptualization of their data and inferences on
their data without awareness [28]. For example if personalized ad
allocations start working even better (by using momentary and contextual data), ads may seem “creepier” [56, 74] — as Malheiros et al.
noted, “too personalized” ads can although catch more attention,
but could also elicit discomfort about the personalization [61].
Further, an implication of our work is towards a future with
fewer (but effective) ads — however, companies can misuse this
opportunity as a business advantage to serve the same quantity
of ads to generate more revenue — this calls for necessary ethical
guidelines in place that limits maximum obtainable revenue per
user as a function of their platform use. Taken together, researchers,
ethicists, users, and platform designers together need to better establish the guidelines and standards of making data simultaneously

Saha et al.

useful and privacy-preserving. Future work into systems that move
away from traditional profile-based targeting can support this ongoing discussion, in particular by offering an alternative that has
so far been less explored and rarely used.

8.4

Limitations and Future Directions

Our work has limitations, some of which also suggest interesting
future directions. We do not take content (e.g., what an ad is about)
into account. While our work is a step towards understanding the
role of context and momentary features, we note that future research can incorporate content to examine the interplay between
context and content-centric factors in explaining online ad effectiveness. Additionally, our study functions within the limits of the
existing ad allocation system on the platform. Because all users in
the Treated and Control groups were allocated ads by the same
system, the effects of ad allocation are likely balanced or washed
out in the large scale of data we worked with. Therefore, despite
the inaccuracies and limitations of ad recommender system, we
consider our findings to remain valid, and our claim is reinforced by
the empirical robustness and theoretical validity tests conducted in
Section 7. We also note that our data included a diversity of ads spanning a wide range of costs and types across the Treated and Control
datasets. As a proxy for major group differences in ads, a t-test on
ad distributors of Tr and Ct groups reveals no significant difference
(𝑝>0.1). Therefore, although we assumed platform-centric factors
to apply similarly to all users and discrepancies to balance across
groups through the scale of the data, this assumption may not fully
hold. Future work can include these confounds and control for the
“goodness” of recommender algorithms if such metrics are available.
Our quasi-experimental approach only accounts for observed factors on the platform. Like any observational study, we cannot infer
true causality. Future experimental studies based on our methodology and insights from our study can help confirm the validity and
applicability of our findings. Similarly, we only quantify observed
ad effectiveness, and cannot estimate the efficacy of the ads in terms
of whether the users actually bought or used the products in the
ads [67]. Future studies can enroll small representative samples
of the population and conduct experimental studies that also incorporate the offline element of effectiveness of online ads. Future
work can also study the “why”-s related to whether users like a
particular kind of ad allocation versus the other [58]. Along the
same lines, future studies can examine if providing explanation
to ad allocations make users more (or less) conducive to ads [49].
We also cannot claim the generalizability of our findings on other
platforms and other forms of ad allocations, which can be explored
in future work. Our work builds the foundation for incorporating
context and momentary behaviors in ad allocations, which can be
extended in the future to other forms of content recommendation
systems and problem settings.

9

CONCLUSION

This paper examined ad consumption on online social platforms,
particularly on the Snapchat Discover Feed. We conducted a quasiexperimental study on three months of longitudinal data of 100K
Snapchat users. We split the longitudinal timeline of each user into


AdverTiming Matters

Baseline and Measurement periods, where we operationalized “preferred timing” of ads based on ad reception in the Baseline period.
Based on this, we obtained two groups of Treated and Control users
based on how they were shown ads in the Measurement period.
We conducted stratified propensity score analysis to match Treated
and Control users by minimizing observed covariates such as aggregated activities and time spent on the platform. We found that
timing ads at preferred times of users leads to effective ad outcomes
(RTE>1.5). We then examined ad outcomes with respect to momentary activities on the platform, operationalized in terms of duration,
interactivity, interaction diversity, extra-socialness, and distractedness. We made observations and recommendations related to ad
allocations on preferred times and momentary on-platform behaviors. We simulated ad reallocation, finding that our study-driven
insights lead to more valuable ad distributions. We also evaluated
the robustness of our study design and parameter choices finding
convergence in findings and validity to our study. We discussed the
implications of our work in advancing our understanding of ad consumption on social media, and in designing better and responsible
ad allocations from both user and platform perspectives.

ACKNOWLEDGMENTS
This work was conducted while Saha, Vincent, and Chowdhury
were at Snap Research. We thank Andrés Monroy-Hernandez, Dong
Whi Yoo, and Vedant Das Swain for their valuable feedback.

REFERENCES
[1] 2014. Systematic review of the Hawthorne effect: new concepts are needed to
study research participation effects. Journal of clinical epidemiology 67, 3 (2014),
267–277.
[2] Paige Alfonzo. 2019. Mastering mobile through Social Media: Creating engaging
content on Instagram and Snapchat. ALA TechSource.
[3] Muhammad Ali, Piotr Sapiezynski, Miranda Bogen, Aleksandra Korolova, Alan
Mislove, and Aaron Rieke. 2019. Discrimination through Optimization: How
Facebook’s Ad Delivery Can Lead to Biased Outcomes. Proceedings of the ACM
on Human-Computer Interaction 3, CSCW (2019), 1–30.
[4] Maximilian Altmeyer, Kathrin Dernbecher, Vladislav Hnatovskiy, Marc Schubhan, Pascal Lessel, and Antonio Krüger. 2019. Gamified Ads: Bridging the Gap
Between User Enjoyment and the Effectiveness of Online Ads. In Proceedings of
the 2019 CHI Conference on Human Factors in Computing Systems. 1–12.
[5] Aris Anagnostopoulos, Ravi Kumar, and Mohammad Mahdian. 2008. Influence
and correlation in social networks. In Proceedings of the 14th ACM SIGKDD
international conference on Knowledge discovery and data mining. ACM, 7–15.
[6] Nikola Banovic, Tofi Buzali, Fanny Chevalier, Jennifer Mankoff, and Anind K
Dey. 2016. Modeling and understanding human routine behavior. In Proceedings
of the 2016 CHI Conference on Human Factors in Computing Systems. 248–260.
[7] Rajeev Batra and Douglas M Stayman. 1990. The role of mood in advertising
effectiveness. Journal of Consumer research 17, 2 (1990), 203–214.
[8] Russell W Belk. 1974. An exploratory assessment of situational effects in buyer
behavior. Journal of marketing research 11, 2 (1974), 156–163.
[9] Danah Boyd and Kate Crawford. 2012. Critical questions for big data: Provocations for a cultural, technological, and scholarly phenomenon. Information,
communication & society 15, 5 (2012), 662–679.
[10] Giorgio Brajnik and Silvia Gabrielli. 2010. A review of online advertising effects
on the user experience. International Journal of Human-Computer Interaction
26, 10 (2010), 971–997.
[11] Jack W Brehm. 1966. A theory of psychological reactance. (1966).
[12] Laura Frances Bright and Kelty Logan. 2018. Is my fear of missing out (FOMO)
causing fatigue? Advertising, social media fatigue, and the implications for
consumers and brands. Internet Research (2018).
[13] Fred E Bronner, Jasper R Bronner, and John Faasse. 2007. In the mood for
advertising. International Journal of Advertising 26, 3 (2007), 333–355.
[14] Bobby J Calder, Edward C Malthouse, and Ute Schaedel. 2009. An experimental
study of the relationship between online engagement and advertising effectiveness. Journal of interactive marketing 23, 4 (2009), 321–331.
[15] Jean-Louis Chandon, Mohamed Saber Chtourou, and David R Fortin. 2003.
Effects of configuration and exposure levels in responses to web advertisements.
Journal of Advertising Research 43, 2 (2003), 217–229.

CHI ’21, May 8–13, 2021, Yokohama, Japan

[16] Jean-Charles Chebat, Francois Limoges, and Claire Gelinas-Chebat. 1997. Effects of circadian orientation, time of day, and arousal on consumers’ depth of
information processing of advertising. Perceptual and motor skills (1997).
[17] Henriette Cramer. 2015. Effects of ad quality &amp; content-relevance on
perceived content quality. In proceedings of the 33rd annual ACM conference on
human factors in computing systems. 2231–2234.
[18] Aron Culotta. 2014. Estimating county health statistics with Twitter. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems. ACM,
1335–1344.
[19] Vedant Das Swain et al. 2019. A Multisensor Person-Centered Approach to
Understand the Role of Daily Activities in Job Performance with Organizational
Personas. Proc. ACM IMWUT 3, 4, Article 130 (2019), 27 pages. https://doi.org/
10.1145/3369828
[20] Munmun De Choudhury, Emre Kiciman, Mark Dredze, Glen Coppersmith, and
Mrinal Kumar. 2016. Discovering shifts to suicidal ideation from mental health
content in social media. In Proceedings of the 2016 CHI Conference on Human
Factors in Computing Systems. ACM, 2098–2110.
[21] Marco de Sa, Vidhya Navalpakkam, and Elizabeth F Churchill. 2013. Mobile
advertising: evaluating the effects of animation, user and content relevance. In
Proceedings of the SIGCHI Conference on Human Factors in Computing Systems.
2487–2496.
[22] Peter Doyle and John Saunders. 1990. Multiproduct advertising budgeting.
Marketing Science 9, 2 (1990), 97–113.
[23] Robert H Ducoffe. 1995. How consumers assess the value of advertising. Journal
of Current Issues &amp; Research in Advertising 17, 1 (1995), 1–18.
[24] Robert H Ducoffe. 1996. Advertising value and advertising on the web-Blog@
management. Journal of advertising research 36, 5 (1996), 21–32.
[25] Robert H Ducoffe and Eleonora Curlo. 2000. Advertising value and advertising
processing. Journal of Marketing Communications (2000).
[26] Julie A Edell and Marian C Burke. 1984. The moderating effect of attitude
toward an ad on ad effectiveness under different processing conditions. ACR
North American Advances (1984).
[27] Steven M Edwards, Hairong Li, and Joo-Hyun Lee. 2002. Forced exposure
and psychological reactance: Antecedents and consequences of the perceived
intrusiveness of pop-up ads. Journal of advertising 31, 3 (2002), 83–95.
[28] Casey Fiesler, Cliff Lampe, and Amy S Bruckman. 2016. Reality and perception
of copyright terms of service for online content creation. In Proceedings of the
19th ACM Conference on Computer-Supported Cooperative Work &amp; Social
Computing. 1450–1461.
[29] Meryl Paula Gardner. 1985. Mood states and consumer behavior: A critical
review. Journal of Consumer research 12, 3 (1985), 281–300.
[30] Kiran Garimella, Orestis Kostakis, and Michael Mathioudakis. 2017. Ad-blocking:
A study on performance, privacy and counter-measures. In Proceedings of the
2017 ACM on Web Science Conference. 259–262.
Rise of Subscriptions and the Fall of Ad[31] Bob Gilbreath. 2017.
vertising: https://medium.com/the-graph/rise-of-subscriptions-and-the-fall-ofadvertising-d5e4d8800a49.
[32] Scott A Golder and Michael W Macy. 2011. Diurnal and seasonal mood vary
with work, sleep, and daylength across diverse cultures. Science 333, 6051 (2011),
1878–1881.
[33] Kendall Goodrich. 2013. Effects of age and time of day on Internet advertising
outcomes. Journal of Marketing Communications (2013).
[34] Samuel D Gosling, Adam A Augustine, Simine Vazire, Nicholas Holtzman, and
Sam Gaddis. 2011. Manifestations of personality in online social networks:
Self-reported Facebook-related behaviors and observable profile information.
Cyberpsychology, Behavior, and Social Networking 14, 9 (2011), 483–488.
[35] Kelley Gullo, Jonah Berger, Jordan Etkin, and Bryan Bollinger. 2019. Does time
of day affect variety-seeking? Journal of Consumer Research 46, 1 (2019), 20–35.
[36] Qi Guo, Eugene Agichtein, Charles LA Clarke, and Azin Ashkan. 2009. In the
mood to click? Towards inferring receptiveness to search advertising. In 2009
IEEE/WIC/ACM International Joint Conference on Web Intelligence and Intelligent
Agent Technology, Vol. 1. IEEE, 319–324.
[37] Hana Habib, Neil Shah, and Rajan Vaish. 2019. Impact of Contextual Factors on
Snapchat Public Sharing. In Proceedings of the 2019 CHI Conference on Human
Factors in Computing Systems. 1–13.
[38] Edward L Hannan. 2008. Randomized clinical trials and observational studies:
guidelines for assessing respective strengths and limitations. JACC (2008).
[39] Curt Haugtvedt, Richard E Petty, John T Cacioppo, and Theresa Steidley. 1988.
Personality and ad effectiveness: Exploring the utility of need for cognition.
ACR North American Advances (1988).
[40] Miguel A Hernan and James M Robins. 2010. Causal inference.
[41] Ben Hutchinson and Margaret Mitchell. 2019. 50 years of test (un) fairness:
Lessons for machine learning. In Proceedings of the Conference on Fairness,
Accountability, and Transparency. 49–58.
[42] Guido W Imbens and Donald B Rubin. 2015. Causal inference in statistics, social,
and biomedical sciences. Cambridge.
[43] Garrett A Johnson, Randall A Lewis, and Elmar I Nubbemeyer. 2017. Ghost
ads: Improving the economics of measuring online ad effectiveness. Journal of


CHI ’21, May 8–13, 2021, Yokohama, Japan

Marketing Research 54, 6 (2017), 867–884.
[44] Jukka Jouhki, Epp Lauk, Maija Penttinen, Niina Sormanen, and Turo Uskali.
2016. Facebook’s emotional contagion experiment as a challenge to research
ethics. Media and Communication 4 (2016).
[45] Parisa Kaghazgaran, Maarten Bos, Leonardo Neves, and Neil Shah. 2020. Social
Factors in Closed-Network Content Consumption. CIKM (2020).
[46] Komal Kapoor, Vikas Kumar, Loren Terveen, Joseph A Konstan, and Paul
Schrater. 2015. “I like to explore sometimes” Adapting to Dynamic User Novelty
Preferences. In Proceedings of the 9th ACM Conference on Recommender Systems.
19–26.
[47] Komal Kapoor, Karthik Subbian, Jaideep Srivastava, and Paul Schrater. 2015.
Just in time recommendations: Modeling the dynamics of boredom in activity
streams. In Proceedings of the Eighth ACM International Conference on Web Search
and Data Mining. 233–242.
[48] Emre Kıcıman, Scott Counts, and Melissa Gasser. 2018. Using Longitudinal
Social Media Analysis to Understand the Effects of Early College Alcohol Use..
In ICWSM. 171–180.
[49] Tami Kim, Kate Barasz, and Leslie K John. 2019. Why am I seeing this ad? The
effect of ad transparency on ad effectiveness. Journal of Consumer Research 45,
5 (2019), 906–932.
[50] Yoojung Kim, Mihyun Kang, Sejung Marina Choi, and Yongjun Sung. 2016. To
click or not to click? Investigating antecedents of advertisement clicking on
Facebook. Social Behavior and Personality: an international journal 44, 4 (2016),
657–667.
[51] Gary King, Richard Nielsen, et al. 2016. Why propensity scores should not be
used for matching. (2016).
[52] Farshad Kooti, Karthik Subbian, Winter Mason, Lada Adamic, and Kristina
Lerman. 2017. Understanding short-term changes in online activity sessions. In
Proceedings of the 26th International Conference on World Wide Web Companion.
[53] Michal Kosinski, David Stillwell, and Thore Graepel. 2013. Private traits and
attributes are predictable from digital records of human behavior. (2013).
[54] Adam DI Kramer, Jamie E Guillory, and Jeffrey T Hancock. 2014. Experimental evidence of massive-scale emotional contagion through social networks.
Proceedings of the National Academy of Sciences 111, 24 (2014), 8788–8790.
[55] Hemank Lamba and Neil Shah. 2019. Modeling dwell time engagement on visual
multimedia. In Proceedings of the 25th ACM SIGKDD International Conference on
Knowledge Discovery & Data Mining. 1104–1113.
[56] Zhou Li, Kehuan Zhang, Yinglian Xie, Fang Yu, and XiaoFeng Wang. 2012.
Knowing your enemy: understanding and detecting malicious web advertising.
In Proceedings of the 2012 ACM conference on Computer and communications
security. 674–686.
[57] Q Vera Liao, Wai-Tat Fu, and Sri Shilpa Mamidi. 2015. It is all about perspective: An exploration of mitigating selective exposure with aspect indicators. In
Proceedings of the 33rd annual ACM conference on Human factors in computing
systems. 1439–1448.
[58] Brian Y Lim, Anind K Dey, and Daniel Avrahami. 2009. Why and why not
explanations improve the intelligibility of context-aware intelligent systems. In
Proceedings of the SIGCHI Conference on Human Factors in Computing Systems.
2119–2128.
[59] Jason Liu, Elissa R Weitzman, and Rumi Chunara. 2017. Assessing behavioral
stages from social media data. In CSCW.
[60] Xun Lu and Halbert White. 2014. Robustness checks and robustness tests in
applied economics. Journal of econometrics 178 (2014), 194–206.
[61] Miguel Malheiros, Charlene Jennett, Snehalee Patel, Sacha Brostoff, and Martina Angela Sasse. 2012. Too close for comfort: A study of the effectiveness
and acceptability of rich-media personalized advertising. In Proceedings of the
SIGCHI conference on human factors in computing systems. 579–588.
[62] En Mao and Jing Zhang. 2015. What drives consumers to click on social media
ads? The roles of content, media, and individual factors. In 2015 48th Hawaii
International Conference on System Sciences. IEEE, 3405–3413.
[63] En Mao and Jing Zhang. 2017. What affects users to click on display ads on
social media? The roles of message values, involvement, and security. Journal
of Information Privacy and Security 13, 2 (2017), 84–96.
[64] Gloria Mark, Shamsi T Iqbal, Mary Czerwinski, and Paul Johns. 2014. Bored
mondays and focused afternoons: The rhythm of attention and online activity
in the workplace. In Proceedings of the SIGCHI Conference on Human Factors in
Computing Systems. ACM, 3025–3034.
[65] Jack Marshall. 2016.
How to Persuade Consumers to Disable Ad
Blockers: https://www.wsj.com/articles/how-to-persuade-consumers-to-disable-adblockers-1469541611.
[66] Akhil Mathur, Nicholas D Lane, and Fahim Kawsar. 2016. Engagement-aware
computing: Modelling user engagement from mobile contexts. In Proceedings
of the 2016 ACM International Joint Conference on Pervasive and Ubiquitous
Computing. 622–633.
[67] Daniel McDuff, Rana El Kaliouby, Jeffrey F Cohn, and Rosalind W Picard. 2014.
Predicting ad liking and purchase intent: Large-scale analysis of facial responses
to ads. IEEE Transactions on Affective Computing 6, 3 (2014), 223–235.

Saha et al.

[68] Abhinav Mehrotra, Fani Tsapeli, Robert Hendley, and Mirco Musolesi. 2017.
MyTraces: Investigating correlation and causation between users’ emotional
states and mobile phone interaction. Proceedings of the ACM on Interactive,
Mobile, Wearable and Ubiquitous Technologies (2017).
[69] Jacob Metcalf and Kate Crawford. 2016. Where are human subjects in big
data research? The emerging ethics divide. Big Data &amp; Society 3, 1 (2016),
2053951716650211.
[70] Jeremy Miles. 2014. Tolerance and variance inflation factor. Wiley StatsRef:
Statistics Reference Online (2014).
[71] Ben Miroglio, David Zeber, Jofish Kaye, and Rebecca Weiss. 2018. The effect of
ad blocking on user engagement with the web. In Proceedings of the 2018 World
Wide Web Conference. 813–821.
[72] Bruce John Morrison and Marvin J Dainoff. 1972. Advertisement complexity
and looking time. Journal of marketing research 9, 4 (1972), 396–400.
[73] Ngoc Thi Nguyen, Agustin Zuniga, Hyowon Lee, Pan Hui, Huber Flores, and
Petteri Nurmi. 2020. (M) ad to See Me? Intelligent Advertisement Placement:
Balancing User Annoyance and Advertising Effectiveness. Proceedings of the
ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies (2020).
[74] Katie O’Donnell and Henriette Cramer. 2015. People’s perceptions of personalized ads. In Proceedings of the 24th International Conference on World Wide Web.
1293–1298.
[75] Alexandra Olteanu, Carlos Castillo, Fernando Diaz, and Emre Kiciman. 2019.
Social data: Biases, methodological pitfalls, and ethical boundaries. Frontiers in
Big Data 2 (2019), 13.
[76] Alexandra Olteanu, Onur Varol, and Emre Kiciman. 2017. Distilling the outcomes
of personal experiences: A propensity-scored analysis of social media. In Proc.
CSCW.
[77] Harshvardhan J Pandit and Dave Lewis. 2018. Ease and ethics of user profiling
in black mirror. In Companion Proceedings of the The Web Conference 2018.
[78] Pew. 2019. pewinternet.org/fact-sheet/social-media.
[79] Martin Pielot, Bruno Cardoso, Kleomenis Katevas, Joan Serrà, Aleksandar Matic,
and Nuria Oliver. 2017. Beyond interruptibility: Predicting opportune moments
to engage mobile phone users. Proceedings of the ACM on Interactive, Mobile,
Wearable and Ubiquitous Technologies (2017).
[80] Lin Qiu, Han Lin, Jonathan Ramsay, and Fang Yang. 2012. You are what you
tweet: Personality expression and perception on Twitter. Journal of research in
personality 46, 6 (2012), 710–718.
[81] Daniele Quercia, Michal Kosinski, David Stillwell, and Jon Crowcroft. [n.d.].
Our twitter profiles, our selves: Predicting personality with twitter.
[82] Manish Raghavan, Solon Barocas, Jon Kleinberg, and Karen Levy. 2020. Mitigating bias in algorithmic hiring: Evaluating claims and practices. In Proceedings of
the 2020 Conference on Fairness, Accountability, and Transparency. 469–481.
[83] Vennila Ramalingam, B Palaniappan, N Panchanatham, and S Palanivel. 2006.
Measuring advertisement effectiveness—a neural network approach. Expert
systems with applications 31, 1 (2006), 159–163.
[84] Pei-Luen Patrick Rau, Qingzi Liao, and Cuiling Chen. 2013. Factors influencing
mobile advertising avoidance. International Journal of Mobile Communications
11, 2 (2013), 123–139.
[85] Filipe N Ribeiro, Koustuv Saha, Mahmoudreza Babaei, Lucas Henrique, Johnnatan Messias, Fabricio Benevenuto, Oana Goga, Krishna P Gummadi, and
Elissa M Redmiles. 2019. On microtargeting socially divisive ads: A case study
of russia-linked ad campaigns on facebook. In Proceedings of the Conference on
Fairness, Accountability, and Transparency. 140–149.
[86] Steven Richmond. 2018. How Snapchat makes money. Investopedia. Elérés
(2018).
[87] Helen Robinson, Anna Wysocka, and Chris Hand. 2007. Internet advertising
effectiveness: the effect of design on click-through rates for banner ads. International Journal of Advertising 26, 4 (2007), 527–541.
[88] Christian Rohrer and John Boyd. 2004. The rise of intrusive online advertising
and the response of user experience research at Yahoo!. In CHI’04 Extended
Abstracts on Human Factors in Computing Systems. 1085–1086.
[89] Donald B Rubin. 2005. Causal inference using potential outcomes: Design,
modeling, decisions. J. Amer. Statist. Assoc. 100, 469 (2005), 322–331.
[90] Adam Sadilek, Henry A Kautz, and Vincent Silenzio. 2012. Modeling Spread of
Disease from Social Interactions.. In International Conference on Weblogs and
Social Media (ICWSM).
[91] Koustuv Saha et al. 2019. Imputing Missing Social Media Data Stream in Multisensor Studies of Human Behavior. In Proceedings of International Conference on
Affective Computing and Intelligent Interaction (ACII 2019).
[92] Koustuv Saha, Larry Chan, Kaya De Barbaro, Gregory D Abowd, and Munmun
De Choudhury. 2017. Inferring mood instability on social media by leveraging
ecological momentary assessments. Proceedings of the ACM on Interactive,
Mobile, Wearable and Ubiquitous Technologies 1, 3 (2017), 95.
[93] Koustuv Saha, Ted Grover, Stephen Mattingly, Vedant Das Swain, Pranshu Gupta,
Gonzalo J Martinez, Pablo Robles-Granda, Gloria Mark, Aaron Striegel, and
Munmun De Choudhury. 2021. Person-Centered Predictions of Psychological
Constructs with Social Media Contextualized by Multimodal Sensing. PACM
IMWUT (2021).


AdverTiming Matters

[94] Koustuv Saha and Amit Sharma. 2020. Causal Factors of Effective Psychosocial
Outcomes in Online Mental Health Communities. In ICWSM.
[95] Koustuv Saha, Benjamin Sugar, John Torous, Bruno Abrahao, Emre Kıcıman,
and Munmun De Choudhury. 2019. A Social Media Study on the Effects of
Psychiatric Medication Use. In ICWSM.
[96] Koustuv Saha, Ingmar Weber, and Munmun De Choudhury. 2018. A Social
Media Based Examination of the Effects of Counseling Recommendations After
Student Deaths on College Campuses. In ICWSM.
[97] Ville Satopaa, Jeannie Albrecht, David Irwin, and Barath Raghavan. 2011. Finding a" kneedle" in a haystack: Detecting knee points in system behavior. In
ICDCS.
[98] Ann E Schlosser, Sharon Shavitt, and Alaina Kanfer. 1999. Survey of Internet
users’ attitudes toward Internet advertising. Journal of interactive marketing 13,
3 (1999), 34–54.
[99] H Andrew Schwartz, Johannes C Eichstaedt, Margaret L Kern, et al. 2013. Personality, gender, and age in the language of social media: The open-vocabulary
approach. PloS one 8, 9 (2013), e73791.
[100] Yi Shen, Heshan Sun, Cheng Suang Heng, and Hock Chuan Chan. 2020. Facilitating Complex Product Choices on E-commerce Sites: An Unconscious Thought
and Circadian Preference Perspective. Decision Support Systems (2020), 113365.
[101] Elizabeth A Stuart. 2010. Matching methods for causal inference: A review and a
look forward. Statistical science: a review journal of the Institute of Mathematical
Statistics 25, 1 (2010), 1.
[102] Gerard J Tellis, Rajesh K Chandy, Deborah MacInnis, and Pattana Thaivanich.
2005. Modeling the microeffects of television advertising: Which ad works,
when, where, for how long, and why? Marketing Science (2005), 359–366.
[103] Catherine E Tucker. 2014. Social networks, personalized advertising, and privacy
controls. Journal of marketing research 51, 5 (2014), 546–562.

CHI ’21, May 8–13, 2021, Yokohama, Japan

[104] Daniel Tunkelang. 2018.
Are Ads Really That Bad?:
https://medium.com/@dtunkelang/are-ads-really-that-bad-1c3d315f6689.
[105] Richard Vaughn. 1980. How advertising works: A planning model. Journal of
advertising research (1980).
[106] Aku Visuri, Simo Hosio, and Denzil Ferreira. 2017. Exploring mobile ad formats
to increase brand recollection and enhance user experience. In Proceedings of the
16th International Conference on Mobile and Ubiquitous Multimedia. 311–319.
[107] Zack Whittaker. 2020. Apple’s iOS 14 will give users the option to decline app
ad tracking: https://techcrunch.com/2020/06/22/apple-ios-14-ad-tracking.
[108] Max Willer. 2018. New Data on Why People Hate Ads: Too Many, Too Intrusive,
Too Creepy: https://www.vieodesign.com/blog/new-data-why-people-hate-ads.
[109] Max Willer. 2019. The Advertising Industry Has a Problem: People Hate
Ads: https://www.nytimes.com/2019/10/28/business/media/advertising-industryresearch.html.
[110] Stephan Winter, Ewa H Maslowska, and Anne L Vos. 2020. The effects of
trait-based personalization in social media advertising. Computers in Human
Behavior (2020), 106525.
[111] Lori D Wolin, Pradeep Korgaonkar, and Daulatram Lund. 2002. Beliefs, attitudes
and behaviour towards Web advertising. International Journal of Advertising 21,
1 (2002), 87–113.
[112] Seounmi Youn and Seunghyun Kim. 2019. Understanding ad avoidance on
Facebook: Antecedents and outcomes of psychological reactance. Computers in
Human Behavior 98 (2019), 232–244.
[113] Zephoria. 2019. https://zephoria.com/top-10-valuable-snapchat-statistics/ .
[114] Justine Zhang, Sendhil Mullainathan, and Cristian Danescu-Niculescu-Mizil.
2020. Quantifying the Causal Effects of Conversational Tendencies. PACM HCI
(CSCW) (2020).


CHI ’21, May 8–13, 2021, Yokohama, Japan

Saha et al.

APPENDIX
Table A1: List of the covariates used in our study.
Baseline Ad Reception
Total Snap Time Seconds (Baseline)
Total Snap Time Seconds (Measurement)
Avg. Number of App Opens
Avg. Number of App Opens from Notifications
Avg. Session Time
Avg. Chat View Count
Avg. Chat Send Count
Avg. Chat Screenshot Count
Avg. Direct Snap Create Count
Avg. Direct Snap Send Count
Avg. Direct Snap View Count
Avg. Direct Snaps from Chat Feed Send Count
Avg. Direct Snap with Camera Send Count

Avg. Direct Snap in Chat Send Count
Avg. Filter Lens Swipes Count
Avg. Filters Swipes Count
Avg. Snap Save Count
Avg. Snap Screenshot Count
Avg. Group Snap Send Count
Avg. Story Post Count
Avg. Friend Feed Friend Stories View Count
Avg. Story Delete Count
Avg. Story Save Count
Avg. Fully Watched Ads Count
Avg. Discover Feed View Count
Avg. Full Ad Views in Discover Feed Count
Avg. Non-full Ad Views in Discover Feed Count

Avg. Direct Snap Reply Send Count
Avg. Discover Feed Ads Count
Avg. Full Regular Ad Views Count
Avg. Hour of Day
Avg. Day of Week
Avg. Session Duration
Avg. Activity
Avg. Content Consumption
Avg. Content Curation
Avg. Interactivity
Avg. Interaction Diversity
Avg. Distractedness
Avg. Extra-Socialness
