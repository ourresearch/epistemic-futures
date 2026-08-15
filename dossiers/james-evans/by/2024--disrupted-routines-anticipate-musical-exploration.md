---
title: "Disrupted routines anticipate musical exploration"
person: james-evans
section: by
type: journal-article
year: 2024
date: 2024-02-01
venue: "Proceedings of the National Academy of Sciences"
authors: "Khwan Kim, Noah Askin, James A. Evans"
source_url: https://doi.org/10.1073/pnas.2306549121
openalex_id: https://openalex.org/W4391429331
retrieved: 2026-08-13
content: full-text
notes: "OpenAlex duplicates merged: W4391429331 W4315705875; full text via the OpenAlex Content API (content.openalex.org)"
---

# Disrupted routines anticipate musical exploration

## Full text

1

2

Supporting Information for

3

Disrupted Routines Anticipate Musical Exploration

4

Khwan Kim, Noah Askin, and James A. Evans

5

Corresponding author: James A. Evans (E-mail: jevans@uchicago.edu)

6

This PDF file includes:

7
8
9
10

Supporting text
Figs. S1 to S11
Tables S1 to S15
SI References

Khwan Kim, Noah Askin, and James A. Evans

1 of 30

11

Supporting Information Text

12

Analysis of Taste Exploration Based on Sonic-S2V. In addition to our primary analysis of taste exploration, we replicate our

38

findings by constructing an alternative Song2Vec (S2V) metric that is entirely independent of any contextual or sequential
information. Inspired by prior research (1, 2), this alternative representation is based on a comprehensive set of audio features
sourced from Spotify, linked to each song in our Deezer dataset via International Standard Recording Codes (ISRC). Spotify’s
audio features, constituting a total of 13 distinct dimensions, capture a broad spectrum of sonic characteristics that each
song possesses. This suite of features includes several continuous variables such as ’acousticness’, ’danceability’, ’energy’,
’instrumentalness’, ’liveness’, ’loudness’, ’speechiness’, ’valence’, and ’tempo’. Each of these captures a unique facet of a song,
ranging from the level of acoustic instrumentation present to the track’s overall tempo or speed. In addition to these continuous
features, there are also categorical attributes like ’mode’, ’key’, and ’time signature’.
For the 10 continuous variables, we implemented a normalization procedure, ensuring that each of these metrics now falls
within a 0 to 1 range, thereby maintaining a unified scale (1). Regarding the categorical variables, we chose to convert each
category into a set of dummy variables. Specifically, ’mode’, which signifies whether the song is in a major or minor modality,
was converted into ’mode 0’ and ’mode 1’, indicative of minor and major respectively. Similarly, ’key’, which states the
track’s key, was transformed into 11 separate dummy variables, with each one denoting a unique key (e.g., C, C sharp/D flat,
etc.). Furthermore, ’time signature’, which provides insight into the song’s rhythmic structure, was also split into five dummy
variables, each one representing a unique time signature like 3/4, 7/4, etc. Following this process, we now have a set of 29
variables—10 normalized continuous features and 19 dummy variables—all of which fall between 0 and 1. With these variables,
we developed a new S2V representation for each song by transforming it into a single 29-dimensional vector, which we named
’Sonic-S2V.’ The values within each vector correspond to a song’s specific ratings across the 29-feature array.
In employing the Sonic-S2V method, we took several steps: First, we recalculated our dependent variable, taste exploration.
Second, we looked into the correlation between the original S2V-based taste exploration and Sonic-S2V-based taste exploration.
And lastly, we replicated our primary regression analysis using the Sonic-S2V variant of taste exploration. Our findings showed
a high degree of correlation (Pearson r = 0.60) between the two versions of taste exploration, reinforcing the validity of our
S2V measure. Moreover, the primary results, suggesting a significant positive link between geospatial routine disruption (travel
distance) and taste exploration, were largely confirmed even with the alternative Sonic-S2V measure (see Table S8 in SI). We
note that the significance of the quadratic term was slightly reduced across the new models. Despite this, our analysis affords
us greater confidence in arguing a substantive relationship between routine disruption and taste exploration.

39

S2V vs. Jaccard Index Approach. Here, we demonstrate that our choice of Song2Vec (S2V) for measuring taste exploration has

13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37

52

several advantages over the Jaccard index, a traditional similarity (or distance) measure. We applied the Jaccard index to
create an alternative, much simpler, taste exploration measure that simply accounted for the intersection over union of shared
songs (Jaccard index) in periods of routine and disruption. The Jaccard index treats each song categorically, as equally and
“infinitely” different from every other song. We first report the pairwise correlation coefficients between the three different taste
exploration measures (see Table S14): the one by our original S2V method, our alternative Spotify Sonic-S2V approach, and
the Jaccard Index. Although the first two methods exhibit a strong correlation, neither shows a significant correlation with the
Jaccard variant (ρ=.01; ρ=-.03), lending further support to our assertion that the Jaccard method is likely too coarse-grained
to capture the kind of taste exploration we examine in our study. Regression analysis for our Study 1 yields far lower R-squared
values and nonsignificant β coefficients in predicting taste exploration when using the Jaccard approach (see Table S15). The
Jaccard’s oversimplicity does not take into account the context of musical consumption, while S2V accounts for song similarity
as a function of co-consumption, i.e., consumed together by the same user(s), in the same playlist(s), at roughly the same
time. In short, S2V does not perform simpler measures (like Jaccard). S2V does, however, correspond to equally or more
complicated measures (like Sonic-S2V).

53

Analysis of Resonance of Explored Taste. To examine the possibility that the impact of travel might linger and continue to

40
41
42
43
44
45
46
47
48
49
50
51

54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69

influence musical tastes even after individuals have returned to their regular routines, we draw upon the measure of resonance
introduced by Barron and colleagues in PNAS (3). In their analysis of the influence of surprising elements in speeches during
the French Revolution’s inaugural parliament, they presented three parameters: novelty, transience, and resonance. Novelty
denotes the extent of surprise in a speech’s structure, considering prior speeches, while transience measures the degree to which
these unexpected patterns dissipate in the future (i.e., the extent to which subsequent speeches do not maintain that pattern).
Resonance is derived by subtracting transience from novelty, indicating the extent to which novelty persists in subsequent
speeches.
Our measure of taste exploration mirrors the concept of novelty. To quantify transience in our scenario, we calculate
the cosine distance between the average vector representation of a focal user’s musical preferences in a given month t and
the average vector of her preferences over the subsequent six months (t+1 to t+6). High transience (or significant decay)
implies that few aspects of the listener’s taste in month t are assimilated into her future taste. Subsequently, we subtract taste
transience from taste exploration to get resonance. High resonance (of taste exploration) implies that a listener’s foray into
novel music significantly deviates from her preferences over the prior six months (i.e., high taste exploration), and that the
newly explored music guides future preferences by maintaining its influence over time (i.e., low transience).
Thus, taste exploration refers to the extent to which a listener’s engagement with new music diverges from her established
taste preferences, while taste resonance evaluates how this new musical foray retains its influence in subsequent listening habits.
2 of 30

Khwan Kim, Noah Askin, and James A. Evans

70
71
72
73
74
75
76
77
78
79

80
81
82
83
84
85
86
87
88
89
90

91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112

While taste exploration revolves around the act of musical discovery, taste resonance focuses on the sustained impact of such a
discovery. Inspired by Barron et al. (2018), we provide a visualization that illustrates how we measure taste resonance by using
two relevant constructs—taste exploration and taste transience (see Fig. S10).
The results, as presented in Table S2, show a significant positive association between taste resonance and travel distance,
with the impact of travel diminishing after a certain threshold (Models 4-7, which include a quadratic term for travel distance).
Moreover, Models 8-11 indicate that the positive relationship between routine disruption and taste resonance–again how much
of the novelty explored in a given time period persists into subsequent time periods–is reinforced when a listener diverges
from mainstream trends (as captured by a significant positive coefficient in the interaction term). Collectively, these results
suggest that the positive influence of routine disruption on taste exploration proves to be more enduring when the travel-related
disruption is more noticeable.
Analysis of Timings of Exploration. We conducted a series of analyses where we manipulated the timing of the dependent
variable (taste exploration) in our main regression analysis. Doing so allows us to examine whether people who travel more are
more likely to be more inclined, in general, to expand their listening taste.
Specifically, we substituted taste exploration (our DV) at time t with the same variable at times t-3, t-2, t-1, t+1, t+2, and
t+3. We included travel distance at each time (i.e., t-3, t-2, . . . ) as well as other controls and retained travel distance at time t
in each of these models. We postulated that the coefficient on travel distance would be stronger in the model where taste
exploration and travel distance coincide. The findings from these analyses are displayed in the Fig. S9. The coefficient on
travel distance is strongest and significant only when it is aligned with taste exploration at time t. However, travel distance at
t loses explanatory power when extended beyond its contemporaneous time t. Said differently, travel distance does not appear
to exert influence on taste exploration except when the two are happening at the same time. In essence, this analysis also
indicates a strong association between taste exploration and concurrent geospatial movement.
Analysis of Effect of Listening Time on Exploration. Regarding our findings that routine disruption during the COVID-19
lockdown led to increased taste exploration, a potential alternative explanation might be that the heightened exploration
of novel tastes by South African users during the lockdown was merely a result of more time spent on the Deezer platform.
This, as opposed to our assertion that the disruption increased exploration, could naturally and mechanically lead to more
exploration. To address this alternative explanation, we provide evidence suggesting that taste exploration during the lockdown
was not influenced by the amount of time lockdown-impacted individuals spent on Deezer or the number of songs they played.
First, our models in Study 3 account for users’ listening time, defined as the duration a user spends on Deezer in a given
week. We incorporated this variable to address potential concerns regarding the relationship between consumption intensity
and taste exploration. Insignificant coefficients across our models, as evidenced in Table S4, indicate that listening time did
not significantly affect taste exploration during the COVID-19 lockdown.
Second, if the premise that more time dedicated to music results in heightened musical exploration were valid, there would
first need to be a noticeable increase in either the number of songs played or the overall time spent on Deezer by those affected
by the COVID-19 lockdown, specifically South African users after March 26, 2020. Our data contradicts this assertion. The
lockdown did not bring about an increase in the overall duration of usage on the streaming platform. Fig. S11 illustrates
the weekly song count and listening duration throughout 2020 for both South Africa (treated) and Australia (control). This
comparison reveals negligible differences in listening intensity within each country before and after the inception of the lockdown.
Finally, we employed a straightforward method to ascertain if listening time (or frequency) influenced taste exploration
during the lockdown. We interacted the listening time (or frequency) variable with the DiD term (i.e., POST × TREATED) in
a triple-DiD (DDD) analysis. Had listening time or frequency been determinants of taste exploration, we would anticipate a
significantly positive coefficient. However, our findings shown in Table S13 suggest that neither variable significantly impacted
taste exploration among the lockdown-affected group (Models 3 and 4). Conversely, the severity of restrictions they encountered
did have an influence (Models 1 and 2).

Khwan Kim, Noah Askin, and James A. Evans

3 of 30

Fig. S1. Taste exploration and travel distance over time. Taste distances are measured by the cosine distance of user vectors between the current month and the prior six
months. Travel distances measured by the log of haversine–calculated as km traveled within the month.

4 of 30

Khwan Kim, Noah Askin, and James A. Evans

Fig. S2. Jaccard Similarity Between Top 100 Songs on Spotify and Deezer. Cross-country similarity is measured based on what is “popular” in each country. Both Spotify and
Deezer release daily charts of the most popular songs by country based on number of streams. We aggregated the top 100 songs from Spotify and Deezer during the same
7-day period and measured inter-country similarity by calculating the Jaccard similarity coefficient.

Khwan Kim, Noah Askin, and James A. Evans

5 of 30

Fig. S3. Stringency of lockdown-related restrictions over the first half year of 2020 in South Africa and Australia. The Oxford Covid-19 Government Response Tracker (OxCGRT)
collected systematic information on policy measures that governments implemented to tackle the spread of COVID-19. It tracked various governmental policy responses across
different countries from January 1, 2020 to the end of 2022 and quantified them. This includes the stringency index that records the strictness of “lockdown style” policies that
primarily restrict people’s behavior ranging from 0 (no restriction) to 100 (maximum restriction). The above figure shows daily scores of the stringency index for South Africa and
Australia the first half year of 2020. It highlights a drastic increase in stringency in South Africa compared to Australia in late March 2020, but an earlier (and smaller) stringency
bump in Australia when it began to close international borders just before February, likely resulting from its proximity to China.

6 of 30

Khwan Kim, Noah Askin, and James A. Evans

Fig. S4. Distribution of listeners by gender and age. Distribution of the demographic features of our sampled users in each country. Across all 9 countries, male users
outnumber female users, and those aged 20-40 account for the largest portion of the sample.

Khwan Kim, Noah Askin, and James A. Evans

7 of 30

Fig. S5. Validation of Song2Vec (S2V). The 5 most similar and dissimilar songs to a sampled focal song, as predicted by our S2V model, with cosine similarity to that focal song
in parentheses. The focal song (in black) in the top left is "God’s Plan" by Drake, which debuted at number one on the US Billboard Hot 100 Chart in January 2018. Its most
similar songs are closely located (in blue) and are mostly works by other contemporaneous popular musicians in Pop and Hip-Hop. The most dissimilar songs (in red) are
remote from Drake’s artistic terrain, including an Indie Folk song by a Swiss singer ("Die Ganze Welt" by Sophie Hunger), and one of the Piano Romance Op. 11 that were
written in 1839 by a female German pianist, Clara Schumann. Concretely, the average cosine similarity of the five most similar songs to God’s Plan is 0.870 whereas that of the
five most dissimilar songs is 0.448. Similarly, our model identifies five hit songs by alternative rock bands formed in the 1980-90s as the most similar songs to Radiohead’s
"Creep" in the top right. At bottom left, a Brazilian rapper MC FIoti’s 2017 song, "Bum Bum Tam Tam," is positioned closely with other Latin American musicians’ hit songs. Note
that some of the neighboring songs whose titles are the same as the focal song are different editions of the focal song released in different albums. A mega hit by Michael
Jackson, "Billie Jean," has the highest similarity with other famous songs by Michael Jackson or the Jackson 5 of which he was lead member at bottom right. It is also collocated
with Queen’s "Another One Bites The Dust," the British rock band’s unusual disco number. At bottom, using our S2V model, we compare the average cosine similarity of songs
within artists and across artists. Specifically, the former is the mean of cosine similarities between songs produced by a focal artist (e.g., similarity between all songs by Michael
Jackson). The latter is the cosine similarity between a group of songs by an artist and all songs in the population by all the other artists (e.g., similarity between all Michael
Jackson songs and the entire collection of other songs by all the other musicians). The average within-artist similarity is 0.715, while the average cross-artist similarity is 0.491.

8 of 30

Khwan Kim, Noah Askin, and James A. Evans

Fig. S6. Longitudinal trends of control variables. Temporal trend of the mean of each of the four control variables included in our analyses across all users in our data. Listening
count—defined as the number of total streams longer than 30 seconds each month—hovers between 450 and 600. Algorithmic listening—ratio of algorithm-driven streams to
the total streams by user—takes off in 2020 although it stays below 15%. Song recency—the inverse of song age—continues to decline while the most considerable drops
occur in two Decembers, presumably driven by classic holiday music. Distance from global taste gradually increases over time although its upward trend also drops in two
Decembers, again suggesting a holiday effect.

Khwan Kim, Noah Askin, and James A. Evans

9 of 30

Fig. S7. Longitudinal trend of taste exploration based on different time windows used to calculating baseline taste. We compare taste exploration calculated with respect to the
listener’s prior month’s listening history (green), their prior six months (blue), and their entire history of within-platform listening (pink).

10 of 30

Khwan Kim, Noah Askin, and James A. Evans

Fig. S8. Results from the quantile regression analysis at different percentiles of the dependent variable, taste exploration (monthly), indicating a progressive increase in the
effect of routine disruption across the distribution of taste exploration. The solid line represents the estimated coefficients, and the shaded area around the line indicates the
95% confidence interval. The results highlight the stronger impact of routine disruption on taste exploration at higher quantiles. The coefficients are significantly greater than 0
across all quantiles, suggesting that routine disruptions have a universal effect on taste exploration, but their impact is more pronounced for individuals who are more actively
exploring new tastes. Even in the lowest quantiles, routine disruption plays a significant role in pushing listeners out of their comfort zones and prompting them to explore new
music, further underscoring the broad and powerful influence of routine disruption on shaping cultural consumption patterns.

Khwan Kim, Noah Askin, and James A. Evans

11 of 30

Fig. S9. This plot presents the results from a time-lag analysis examining the relationship between travel distance at t and taste exploration at different time periods (t-3, t-2, t-1,
t, t+1, t+2, t+3). Each point represents the coefficient of the travel distance variable (t) from separate regression models, where the dependent variable is taste exploration at a
different time period. The strongest and lone statistically significant coefficient is observed at time t (i.e., when the timing of travel distance and taste exploration are aligned).
This implies that taste exploration increases in response to the contemporaneous geospatial change.

12 of 30

Khwan Kim, Noah Askin, and James A. Evans

Fig. S10. Taste exploration, taste transience, and taste resonance. To quantify transience in our scenario, in addition to exploration, we calculate the cosine distance between
the average vector representation of a focal user’s listens in a given month t and the average vector of her listens over the subsequent six months (t+1 to t+6). High transience
(or significant decay) implies that few aspects of the listener’s taste in month t are assimilated into her subsequent taste. We subtract taste transience from taste exploration to
compute resonance. High resonance (of taste exploration) implies that a listener’s foray into novel music significantly deviates from her preferences over the prior six months
(i.e., high taste exploration), and that the newly explored music guides future preferences by maintaining its influence over time (i.e., low transience).

Khwan Kim, Noah Askin, and James A. Evans

13 of 30

Fig. S11. This plot compares consumption intensity among listeners pre- and post-COVID-19 in South Africa and Australia. The plot on the left shows that there was little
difference in listening count among the users, whether in South Africa or Australia, before and after the 26th of March in 2020, when South Africa imposed a nationwide
lockdown. Similarly, the plot on the right demonstrates there was no significant change in listening count among the same users. Taken together, this suggests that the
lockdown did not lead to an increase in consumption frequency or time on Deezer.

14 of 30

Khwan Kim, Noah Askin, and James A. Evans

Table S1. Results of regression analysis of taste exploration at the global level. Estimates are from fixed-effects OLS regressions. Cluster-robust
standard errors are shown in parentheses; p-values correspond to two-tailed tests. Model 1 includes only the main independent variable—travel
distance—and user fixed-effects. Model 2 adds month fixed-effects. Model 3 adds control variables. Models 4-7 add the quadratic term of travel distance.
The full sample is used in Model 4, Australians are dropped in Model 5; Brazilians are dropped in Model 6; and both Australians and Brazilians dropped in
Model 7 (Brazillians have outlier tastes, and Austrians have outlier travel distances). Instead of the quadratic term for travel distance, Models 8-11 include
the interaction term between travel distance and “distance” from global taste.

Model 1
(No Cov.)

Model 2
(Months)

Model 3
(Linear)

Model 4
(Quadratic)

DV = Taste exploration in month t
Model 5
Model 6
Model 7
(No AU)
(No BR)
(No AU&BR)

Model 8
(Interact)

Model 9
(No AU)

Model 10
(No BR)

Model 11
(No AU&BR)

-.035∗∗∗
(.000)

-.079∗∗∗
(.005)

-.035∗∗∗
(.005)

-.034∗∗∗
(.005)

-.034∗∗∗
(.006)

.044∗∗∗
(.006)

.046∗∗∗
(.007)

-.034∗∗∗
(.005)

-.035∗∗∗
(.006)

.043∗∗∗
(.006)

.044∗∗∗
(.007)

Algorithmic listening

-.049∗∗∗
(.002)

-.049∗∗∗
(.002)

-.049∗∗∗
(.002)

-.050∗∗∗
(.002)

-.050∗∗∗
(.002)

-.049∗∗∗
(.002)

-.049∗∗∗
(.002)

-.051∗∗∗
(.002)

-.050∗∗∗
(.002)

Listening count

-.230∗∗∗
(.004)

-.231∗∗∗
(.004)

-.231∗∗∗
(.004)

-.223∗∗∗
(.005)

-.223∗∗∗
(.005)

-.230∗∗∗
(.004)

-.230∗∗∗
(.004)

-.223∗∗∗
(.005)

-.223∗∗∗
(.005)

Song recency

.072∗∗∗
(.004)

.071∗∗∗
(.004)

.070∗∗∗
(.004)

.090∗∗∗
(.005)

.088∗∗∗
(.005)

.072∗∗∗
(.004)

.070∗∗∗
(.004)

.090∗∗∗
(.005)

.088∗∗∗
(.005)

Distance from global taste

.395∗∗∗
(.006)

.395∗∗∗
(.006)

.395∗∗∗
(.006)

.429∗∗∗
(.007)

.429∗∗∗
(.007)

.396∗∗∗
(.006)

.396∗∗∗
(.006)

.429∗∗∗
(.007)

.431∗∗∗
(.007)

.047∗∗∗
(.005)

.070∗∗∗
(.008)

.085∗∗∗
(.009)

.071∗∗∗
(.009)

.091∗∗∗
(.011)

.041∗∗∗
(.005)

.045∗∗∗
(.005)

.042∗∗∗
(.006)

.047∗∗∗
(.007)

-.001∗∗
(.000)

-.002∗∗∗
(.000)

-.002∗∗
(.001)

-.003∗∗∗
(.001)
.033∗∗∗
(.007)
Yes
Yes
541047
30339
.192
.143
.114

.042∗∗∗
(.009)
Yes
Yes
530087
29725
.191
.142
.114

.027∗∗∗
(.008)
Yes
Yes
415109
22922
.229
.162
.121

.039∗∗∗
(.011)
Yes
Yes
404149
22308
.228
.162
.121

Constant

Travel distance

.034∗∗∗
(.006)

.035∗∗∗
(.006)

Travel distance2

Travel distance

× Distance from global taste
User FEs
Month FEs
N of obs.
N of users
R2 between
R2 overall
R2 within

Yes
No
541933
30384
.000
.000
.000

Yes
Yes
541933
30384
.000
.001
.002

Yes
Yes
541047
30339
.192
.143
.114

Yes
Yes
541047
30339
.193
.143
.114

Yes
Yes
530087
29725
.192
.143
.114

Yes
Yes
415109
22922
.230
.163
.121

Yes
Yes
404149
22308
.229
.162
.121

Robust standard errors in parentheses are adjusted for clusters in users.
P-values correspond to two-tailed tests.
∗

p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

Khwan Kim, Noah Askin, and James A. Evans

15 of 30

Table S2. Results of regression analysis of taste resonance. Estimates are from fixed-effects OLS regressions. Cluster-robust standard errors are
shown in parentheses; p-values correspond to two-tailed tests. Month dummies are omitted from the table due to space limitation. Model 1 includes only
the main independent variable—taste distance to city—and user fixed-effects. Model 2 adds month fixed-effects. Model 3 adds control variables. Models
4-7 add the quadratic term of taste distance to city; the full sample used in Model 4, Australians dropped in Model 5; Brazilians dropped in Model 6; both
Australians and Brazilians dropped in Model 7 (see Table S1). Instead of the quadratic term for taste distance to city, Models 8-11 include the interaction
term between taste distance to city and geographical distance to city.

Model 1
(No Cov.)

Model 2
(Months)

Model 3
(Linear)

DV = Resonance of explored new taste in month t
Model 4
Model 5
Model 6
Model 7
Model 8
(Quadratic)
(No AU)
(No BR)
(No AU&BR)
(Interact)

Model 9
(No AU)

Model 10
(No BR)

Model 11
(No AU&BR)

.004∗∗∗
(.000)

.007
(.007)

.015∗
(.007)

.015∗
(.007)

.014
(.007)

.013
(.008)

.011
(.009)

.015∗
(.007)

.013
(.007)

.013
(.008)

.011
(.009)

Algorithmic listening

-.016∗∗∗
(.002)

-.016∗∗∗
(.002)

-.016∗∗∗
(.002)

-.016∗∗∗
(.003)

-.016∗∗∗
(.003)

-.016∗∗∗
(.002)

-.016∗∗∗
(.002)

-.016∗∗∗
(.003)

-.016∗∗∗
(.003)

Listening count

.117∗∗∗
(.005)

.117∗∗∗
(.005)

.115∗∗∗
(.005)

.121∗∗∗
(.006)

.119∗∗∗
(.007)

.117∗∗∗
(.005)

.116∗∗∗
(.005)

.122∗∗∗
(.006)

.120∗∗∗
(.007)

Song recency

.069∗∗∗
(.005)

.069∗∗∗
(.005)

.068∗∗∗
(.005)

.072∗∗∗
(.006)

.071∗∗∗
(.006)

.069∗∗∗
(.005)

.068∗∗∗
(.005)

.072∗∗∗
(.006)

.071∗∗∗
(.006)

Distance from global taste

.169∗∗∗
(.007)

.169∗∗∗
(.007)

.168∗∗∗
(.007)

.180∗∗∗
(.009)

.179∗∗∗
(.009)

.169∗∗∗
(.007)

.169∗∗∗
(.007)

.180∗∗∗
(.009)

.180∗∗∗
(.009)

.006
(.006)

.021∗
(.009)

.026∗
(.011)

.026∗
(.010)

.032∗
(.012)

.003
(.005)

.005
(.006)

.007
(.006)

.011
(.007)

-.001∗
(.000)

-.001∗
(.000)

-.001∗
(.001)

-.001
(.001)
.022∗∗∗
(.006)
Yes
Yes
482964
30335
.001
.004
.013

.025∗∗∗
(.007)
Yes
Yes
473173
29721
.001
.004
.013

.019∗∗
(.007)
Yes
Yes
371107
22918
.002
.005
.014

.023∗∗
(.008)
Yes
Yes
361316
22304
.002
.005
.014

Constant

Travel distance

.024∗∗∗
(.006)

.023∗∗∗
(.006)

Travel distance2

Travel distance
× Distance from global taste
User-FEs
Month-FEs
N of obs.
N of users
R2 between
R2 overall
R2 within

Yes
Yes
483737
30380
.000
.000
.000

Yes
Yes
483737
30380
.011
.001
.002

Yes
Yes
482964
30335
.001
.004
.013

Yes
Yes
482964
30335
.001
.004
.013

Yes
Yes
473173
29721
.001
.004
.013

Yes
Yes
371107
22918
.002
.005
.014

Yes
Yes
361316
22304
.002
.005
.014

Robust standard errors in parentheses are adjusted for clusters in users.
∗

p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

16 of 30

Khwan Kim, Noah Askin, and James A. Evans

Table S3. Results from a regression analysis of taste adaptation at the global level. Estimates are from fixed-effects OLS regressions. Clusterrobust standard errors are shown in parentheses; p-values correspond to two-tailed tests. Month dummies are omitted from the table due to space
limitation. Model 1 includes only the main independent variable—taste distance to city—and user fixed-effects. Model 2 adds month fixed-effects. Model 3
adds control variables. Models 4-7 add the quadratic term of taste distance to city; the full sample used in Model 4, Australians dropped in Model 5;
Brazilians dropped in Model 6; both Australians and Brazilians dropped in Model 7 (see Table S1). Instead of the quadratic term for taste distance to city,
Models 8-11 include the interaction term between taste distance to city and geographical distance to city.

Model 1
(No Cov.)

Model 2
(Months)

Model 3
(Full)

Model 4
(Full)

DV = Taste adaptation to city
Model 5
Model 6
Model 7
(No AU)
(No BR)
(No AU&BR)

Model 8
(Full)

Model 9
(No AU)

Model 10
(No BR)

Model 11
(No AU&BR)

-.000
(.001)

.079∗∗∗
(.003)

-.005
(.003)

-.086∗∗∗
(.004)

-.084∗∗∗
(.004)

-.136∗∗∗
(.004)

-.134∗∗∗
(.004)

-.016∗∗∗
(.003)

-.017∗∗∗
(.003)

-.072∗∗∗
(.003)

-.077∗∗∗
(.003)

Algorithmic listening

.004∗∗∗
(.001)

.005∗∗∗
(.001)

.004∗∗∗
(.001)

.002∗
(.001)

.002
(.001)

.004∗∗∗
(.001)

.004∗∗∗
(.001)

.002
(.001)

.002
(.001)

Listening count

.028∗∗∗
(.001)

.028∗∗∗
(.001)

.028∗∗∗
(.001)

.026∗∗∗
(.002)

.026∗∗∗
(.002)

.028∗∗∗
(.001)

.028∗∗∗
(.001)

.026∗∗∗
(.002)

.027∗∗∗
(.002)

Song recency

.028∗∗∗
(.002)

.025∗∗∗
(.002)

.027∗∗∗
(.002)

.020∗∗∗
(.002)

.022∗∗∗
(.002)

.027∗∗∗
(.002)

.028∗∗∗
(.002)

.021∗∗∗
(.002)

.023∗∗∗
(.002)

Distance from global taste

-.222∗∗∗
(.002)

-.223∗∗∗
(.002)

-.220∗∗∗
(.002)

-.239∗∗∗
(.002)

-.237∗∗∗
(.002)

-.222∗∗∗
(.002)

-.219∗∗∗
(.002)

-.239∗∗∗
(.002)

-.236∗∗∗
(.002)

Geographical distance to city

-.015∗∗∗
(.001)

-.012∗∗∗
(.001)

-.013∗∗∗
(.002)

-.009∗∗∗
(.002)

-.007∗∗
(.003)

-.021∗∗∗
(.002)

-.032∗∗∗
(.003)

-.020∗∗∗
(.002)

-.037∗∗∗
(.004)

.681∗∗∗
(.005)

.550∗∗∗
(.004)

.547∗∗∗
(.004)

.558∗∗∗
(.005)

.555∗∗∗
(.005)

.671∗∗∗
(.005)

.672∗∗∗
(.005)

.677∗∗∗
(.005)

.680∗∗∗
(.005)

.082∗∗∗
(.004)

.085∗∗∗
(.004)

.081∗∗∗
(.004)

.083∗∗∗
(.004)
.028∗∗∗
(.003)
Yes
Yes
2420853
30186
.645
.409
.289

.039∗∗∗
(.004)
Yes
Yes
2343730
29572
.643
.408
.290

.034∗∗∗
(.004)
Yes
Yes
2038385
22846
.707
.435
.306

.052∗∗∗
(.005)
Yes
Yes
1961262
22232
.703
.436
.307

Constant

Taste distance to city

.664∗∗∗
(.005)

.673∗∗∗
(.005)

Taste distance to city2

Taste distance to city

× Geographical distance to city
User FEs
Month FEs
N of obs.
N of users
R2 between
R2 overall
R2 within

Yes
No
2420853
30186
.451
.289
.262

Yes
Yes
2420853
30186
.448
.290
.265

Yes
Yes
2420853
30186
.645
.408
.288

Yes
Yes
2420853
30186
.652
.414
.295

Yes
Yes
2343730
29572
.651
.415
.296

Yes
Yes
2038385
22846
.707
.438
.311

Yes
Yes
1961262
22232
.705
.439
.313

Robust standard errors in parentheses are adjusted for clusters in users.
P-values correspond to two-tailed tests.
∗

p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

Khwan Kim, Noah Askin, and James A. Evans

17 of 30

Table S4. Results of Difference-in-Differences (DiD) and triple DID (DDD) analyses of taste exploration between South Africa and Australia.
Estimates are from fixed-effects OLS regressions. Cluster-robust standard errors are shown in parentheses; p-values correspond to two-tailed tests. We
deliberately eliminated those users who were living or temporarily staying outside their respective home countries in the recent past period leading up to
our observation window. For instance, we excluded a Australian user if she had resided abroad till February 2020 and came back and stay in Australia
during the first pandemic period. As a result, our sample includes 641 users, composed of 207 Australians who resided in their home country from
January through June 2020 and 434 South Africans who were residing also in their home country during the same timeframe. Models 1 and 2 include
only the treatment dummy and only the dummy for post-treatment periods, respectively. Model 3 shows the average treatment effect on the treated (ATET)
without considering control variables and fixed-effects. Models 4-7 include control variables. The result of Model 6 intimates a positive ATET with control
variables and without fixed-effects. Model 7 shows the positive ATET when considering both control variables and fixed-effects. Model 8 shows the result
of our triple Diff-in-Diffs (DDD) analysis that utilizes dummy stuck as a DDD interaction term. Model 9 shows the results of another DDD analysis that
uses inverse mobility as a DDD interaction term.

Model 1

Model 2

Model 3

DV = Taste exploration in week t
Model 4
Model 5
Model 6

Model 7

Model 8

Model 9

-.455∗∗∗
(.027)

-.592∗∗∗
(.019)

-.465∗∗∗
(.028)

-.585∗∗∗
(.007)

-.520∗∗∗
(.012)

-.504∗∗∗
(.012)

-.586∗∗∗
(.007)

-.589∗∗∗
(.008)

-.620∗∗∗
(.023)

Algorithmic listening

-.008∗
(.003)

-.007∗
(.003)

-.007∗
(.003)

-.008∗
(.003)

-.008∗
(.003)

-.008∗
(.003)

Listening time

.004
(.003)

.005
(.003)

.005
(.003)

.005
(.003)

.005
(.003)

.005
(.003)

Song recency

-.102∗∗∗
(.005)

-.106∗∗∗
(.005)

-.107∗∗∗
(.005)

-.102∗∗∗
(.005)

-.102∗∗∗
(.005)

-.102∗∗∗
(.005)

Distance from nat’l taste

.352∗∗∗
(.006)

.358∗∗∗
(.006)

.357∗∗∗
(.006)

.352∗∗∗
(.006)

.352∗∗∗
(.006)

.352∗∗∗
(.006)

Travel distance

.022
(.013)

.020
(.013)

.016
(.013)

.018
(.012)

.019
(.012)

.028∗
(.014)

-.184∗∗∗
(.036)

-.095∗∗∗
(.015)

-.117∗∗∗
(.016)

.019
(.015)

.019∗∗∗
(.004)

-.012
(.009)

-.019
(.013)

.015
(.016)

.231∗∗∗
(.060)

.041∗∗∗
(.010)

.041∗∗∗
(.010)

.008
(.015)

-.203∗∗
(.069)

Constant

TREATED (S. Africa)

-.162∗∗∗
(.035)
.052∗∗∗
(.008)

POST (Mar 26 - May 31, 2020)

.044∗
(.017)

TREATED × POST

POST × Stuck

-.042∗∗
(.014)

TREATED × Stuck

-.007
(.012)

POST × TREATED × Stuck

.041∗
(.016)

Inverse mobility

.009
(.006)

POST × Inverse mobility

-.037∗∗∗
(.009)

TREATED × Inverse mobility

-.005
(.007)

POST × TREATED × Inverse mobility

.036∗∗∗
(.010)
Yes
Yes
11757
641
.815
.773
.668

User FEs
Week FEs
N of obs.
N of users
R2 between
R2 overall
R2 within

No
No
11757
641
.029
.019
.000

No
No
11757
641
.002
.004
.011

No
No
11757
641
.031
.022
.012

Yes
Yes
11757
641
.812
.770
.666

No
No
11757
641
.819
.776
.665

No
No
11757
641
.819
.777
.667

Yes
Yes
11757
641
.807
.766
.667

Yes
Yes
11757
641
.808
.768
.668

Standard errors in parentheses are adjusted for 641 clusters in users. p-values correspond to two-tailed tests.
Time range of the observations is from the 2nd week of January to the last week of May in 2020.
∗

p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

18 of 30

Khwan Kim, Noah Askin, and James A. Evans

Table S5. Summary statistics for variables used in regression analyses
Descriptive statistics for variables used in regression of taste exploration
Variable
Taste exploration
Algorithmic listening
Listening count
Song recency
Distance from global taste
Travel distance
Travel distance2

Obs

Mean

Std. Dev.

Min

Max

541047
541047
541047
541047
541047
541047
541047

-.038
-.101
.077
.071
-.064
-.017
.256

.959
.969
.873
.941
1.006
.505
9.455

-.871
-.824
-2.671
-13.985
-2.085
-.116
0

9.673
1.78
2.937
2.819
3.784
46.593
2170.944

Descriptive statistics for variables used in regression of taste adaptation
Variable
Taste adaptation
Taste distance
Taste distance2
Geospatial distance
Algorithmic listening
Listening count
Song recency
Distance from global taste

Obs

Mean

Std. Dev.

Min

Max

2420853
2420853
2420853
2420853
2420853
2420853
2420853
2420853

-.116
-.174
.613
-.113
-.122
.344
.181
-.115

.87
.763
1.464
.888
.843
1.141
.874
.984

-3.115
-.646
0
-.451
-.486
-.862
-11.851
-2.111

4.33
4.9
24.007
5.64
4.453
19.475
2.819
3.784

Descriptive statistics for variables used in DiD models (South Africa, Treated)
Variable

Obs

Mean

Std. Dev.

Min

Max

Taste exploration
Algorithmic listening
Listening count
Song recency
Distance from global taste
Travel distance
TREATED
POST

8635
8635
8635
8635
8635
8635
8635
8635

-.082
-.121
-.098
.08
-.018
-.173
1
.491

1.022
.859
.785
.973
.964
.066
0
.5

-4.892
-.476
-.818
-6.888
-1.553
-.187
1
0

1.758
3.387
9.38
1.656
3.029
1.586
1
1

Descriptive statistics for variables used in DiD models (Australia, Control)
Variable

Obs

Mean

Std. Dev.

Min

Max

Taste exploration
Algorithmic listening
Listening count
Song recency
Distance from global taste
Travel distance
TREATED
POST

3122
3122
3122
3122
3122
3122
3122
3122

.227
.064
-.05
-.221
.049
-.161
0
.495

.898
1.085
1.015
1.04
1.092
.135
0
.5

-2.418
-.476
-.818
-5.908
-1.592
-.187
0
0

1.805
3.387
8.798
1.646
2.96
2.128
0
1

Khwan Kim, Noah Askin, and James A. Evans

19 of 30

Table S6. Results of regression analysis of taste exploration at the country level (curvilinear relationship). Estimates from fixed-effects OLS
regressions. Cluster-robust standard errors are shown in parentheses; p-values correspond to two-tailed tests. Each model corresponds to a separate
regression analysis on each of the nine countries. Model 1 (FR) uses the same model specification but only with samples from French users. Model 2
(UK) also uses the same model specification but with British users, and so on. A most salient pattern that emerges across the models is the positive
coefficient of travel distance, although the coefficients for the three countries with small sample size are relatively small and statistically not significant. In
addition, coefficients for squared travel distance are significantly negative only for France, United the Kingdom, and South Africa. This leads us to argue
that it is more appropriate to see the relationship between travel distance and taste exploration as linear with a concave, diminishing effect rather than as
an inverted-U.

Model 1
(FR)

Model 2
(UK)

Model 3
(DE)

DV = Taste exploration in month t
Model 4
Model 5
Model 6
(BR)
(RU)
(MA)

Model 7
(AU)

Model 8
(MX)

Model 9
(ZA)

Constant

-.046∗∗∗
(.010)

.069∗∗∗
(.011)

.150∗∗∗
(.014)

-.253∗∗∗
(.010)

.059
(.042)

.111
(.079)

.101∗
(.041)

-.181∗∗∗
(.037)

-.004
(.033)

Algorithmic listening

-.048∗∗∗
(.003)

-.050∗∗∗
(.004)

-.058∗∗∗
(.005)

-.040∗∗∗
(.003)

-.058∗∗∗
(.014)

-.086∗∗
(.026)

-.051∗∗∗
(.015)

-.009
(.014)

-.046∗∗∗
(.011)

Listening count

-.227∗∗∗
(.007)

-.192∗∗∗
(.008)

-.233∗∗∗
(.010)

-.259∗∗∗
(.006)

-.272∗∗∗
(.026)

-.276∗∗∗
(.050)

-.215∗∗∗
(.027)

-.329∗∗∗
(.035)

-.222∗∗∗
(.020)

Song recency

.087∗∗∗
(.008)

.139∗∗∗
(.009)

.057∗∗∗
(.009)

.011
(.008)

.067
(.035)

.073
(.069)

.160∗∗∗
(.032)

.168∗∗∗
(.044)

.118∗∗∗
(.029)

Distance from global taste

.397∗∗∗
(.011)

.504∗∗∗
(.013)

.417∗∗∗
(.012)

.255∗∗∗
(.011)

.317∗∗∗
(.035)

.526∗∗∗
(.066)

.430∗∗∗
(.044)

.203∗∗∗
(.054)

.479∗∗∗
(.038)

Travel distance

.088∗∗∗
(.014)

.047∗
(.023)

.055∗
(.025)

.095∗∗∗
(.025)

.120
(.135)

.081
(.093)

-.006
(.011)

.045
(.086)

.051
(.034)

Travel distance2

-.003∗∗
(.001)
Yes
Yes
120427
6682
.238
.174
.143

.014∗∗∗
(.004)
Yes
Yes
112806
6219
.238
.188
.169

-.002
(.002)
Yes
Yes
139565
7621
.191
.129
.093

-.002∗
(.001)
Yes
Yes
125938
7417
.142
.111
.100

.088
(.048)
Yes
Yes
10390
605
.177
.131
.105

-.019
(.016)
Yes
Yes
2656
155
.148
.163
.213

-.000
(.001)
Yes
Yes
10960
614
.286
.187
.133

.006
(.043)
Yes
Yes
5408
304
.252
.157
.121

-.006
(.005)
Yes
Yes
12897
722
.158
.141
.177

User FEs
Month FEs
N of obs.
N of users
R 2 between
R 2 overall
R 2 within

Robust standard errors in parentheses are adjusted for clusters in users.
P-values correspond to two-tailed tests.
∗

p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

20 of 30

Khwan Kim, Noah Askin, and James A. Evans

Table S7. Results of regression analysis of taste exploration at the country level (interaction effects). Estimates are from fixed-effects OLS
regressions. Cluster-robust standard errors are shown in parentheses; p-values correspond to two-tailed tests. Travel distance squared in Table S6 is
replaced by the interaction term between travel distance and distance from global taste. Although not across all countries, three out of four large-sample
countries show highly significant coefficients of the interaction term, in addition to South Africa.

Model 1
(FR)

Model 2
(UK)

Model 3
(DE)

DV = Taste exploration in month t
Model 4
Model 5
Model 6
(BR)
(RU)
(MA)

Model 7
(AU)

Model 8
(MX)

Model 9
(ZA)

Constant

-.051∗∗∗
(.010)

.072∗∗∗
(.011)

.150∗∗∗
(.014)

-.253∗∗∗
(.010)

.067
(.041)

.108
(.079)

.098∗
(.040)

-.180∗∗∗
(.037)

-.005
(.033)

Algorithmic listening

-.048∗∗∗
(.003)

-.050∗∗∗
(.004)

-.058∗∗∗
(.005)

-.040∗∗∗
(.003)

-.058∗∗∗
(.014)

-.085∗∗
(.026)

-.049∗∗∗
(.015)

-.010
(.014)

-.046∗∗∗
(.011)

Listening count

-.226∗∗∗
(.007)

-.194∗∗∗
(.008)

-.233∗∗∗
(.010)

-.258∗∗∗
(.006)

-.272∗∗∗
(.026)

-.274∗∗∗
(.050)

-.215∗∗∗
(.027)

-.331∗∗∗
(.035)

-.222∗∗∗
(.020)

Song recency

.089∗∗∗
(.008)

.139∗∗∗
(.009)

.057∗∗∗
(.009)

.010
(.008)

.067
(.035)

.074
(.068)

.159∗∗∗
(.032)

.167∗∗∗
(.044)

.118∗∗∗
(.029)

Distance from global taste

.397∗∗∗
(.011)

.505∗∗∗
(.013)

.423∗∗∗
(.012)

.256∗∗∗
(.011)

.315∗∗∗
(.036)

.523∗∗∗
(.066)

.446∗∗∗
(.045)

.206∗∗∗
(.053)

.479∗∗∗
(.038)

Travel distance

.037∗∗∗
(.007)

.115∗∗∗
(.015)

.040∗
(.016)

.036∗∗∗
(.009)

.238∗
(.102)

-.030
(.038)

-.007
(.009)

.088
(.066)

.033
(.020)

Travel distance
× Distance from global taste
User FEs
Month FEs
N of obs.
N of users
R2 between
R2 overall
R2 within

.032∗∗
(.012)
Yes
Yes
120427
6682
.236
.173
.143

.071∗∗∗
(.016)
Yes
Yes
112806
6219
.238
.187
.169

.071∗∗
(.026)
Yes
Yes
139565
7621
.191
.129
.093

.054∗∗∗
(.014)
Yes
Yes
125938
7417
.142
.112
.101

-.028
(.130)
Yes
Yes
10390
605
.177
.131
.105

-.060
(.050)
Yes
Yes
2656
155
.151
.164
.213

-.023∗∗
(.008)
Yes
Yes
10960
614
.291
.190
.134

.103
(.076)
Yes
Yes
5408
304
.250
.157
.122

-.006
(.014)
Yes
Yes
12897
722
.157
.141
.177

Robust standard errors in parentheses are adjusted for clusters in users.
P-values correspond to two-tailed tests.
∗

p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

Khwan Kim, Noah Askin, and James A. Evans

21 of 30

Table S8. Results of regression analysis of taste exploration using Sonic-S2V (Spotify audio features). Estimates are from fixed-effects OLS
regressions. Cluster-robust standard errors are shown in parentheses; p-values correspond to two-tailed tests.

DV = Taste exploration in month t (based on Spotify Sonic-S2V)
Model 1
Model 2
Model 3
Model 4
Model 5
(Linear)
(Quadratic)
(No AU)
(No BR)
(No AU&BR)
Constant

.010
(.006)

.010
(.006)

.012∗
(.006)

.054∗∗∗
(.007)

.057∗∗∗
(.007)

Algorithmic listening

-.032∗∗∗
(.002)

-.032∗∗∗
(.002)

-.032∗∗∗
(.002)

-.035∗∗∗
(.003)

-.034∗∗∗
(.003)

Listening count

-.321∗∗∗
(.005)

-.321∗∗∗
(.005)

-.322∗∗∗
(.005)

-.312∗∗∗
(.006)

-.312∗∗∗
(.006)

Song recency

.080∗∗∗
(.005)

.080∗∗∗
(.005)

.079∗∗∗
(.005)

.091∗∗∗
(.006)

.089∗∗∗
(.006)

Distance from global taste

.236∗∗∗
(.006)

.236∗∗∗
(.006)

.238∗∗∗
(.006)

.242∗∗∗
(.007)

.244∗∗∗
(.007)

Travel distance

.016∗∗∗
(.005)

.029∗∗∗
(.005)

.036∗∗∗
(.006)

.024∗
(.010)

.033∗∗
(.012)

Yes
Yes
483618
30337
.231
.126
.074

-.001
(.000)
Yes
Yes
483618
30337
.231
.126
.074

-.001∗
(.000)
Yes
Yes
473815
29723
.230
.126
.073

-.001
(.001)
Yes
Yes
371529
22920
.246
.126
.065

-.001
(.001)
Yes
Yes
361726
22306
.244
.125
.065

Travel distance2
User-FEs
Month-FEs
N of obs.
N of users
R2 between
R2 overall
R2 within

Robust standard errors in parentheses are adjusted for clusters in users.
∗

22 of 30

p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

Khwan Kim, Noah Askin, and James A. Evans

Table S9. Results of Granger-causality tests. Estimates are from fixed-effects OLS regressions. Cluster-robust standard errors are shown in
parentheses; p-values correspond to two-tailed tests. Month dummies are omitted from the table from space limitations. Travel distance squared in
Table S5 is replaced by the interaction term between travel distance and distance from global taste. Although not across all countries, three out of four
large-sample countries show highly significant coefficients of the interaction term, in addition to South Africa.

DV=Taste Exploration
Model GC1

DV=Travel Distance
Model GC2

Lagged travel distance

.012∗∗
(.004)

.376∗∗∗
(.028)

Lagged taste exploration

.139∗∗∗
(.003)

.001
(.001)

Algorithmic listening

-.044∗∗∗
(.002)

-.004∗∗∗
(.001)

Listening count

-.190∗∗∗
(.004)

.046∗∗∗
(.003)

Song recency

.059∗∗∗
(.004)

.023∗∗∗
(.003)

Distance from global taste

.389∗∗∗
(.006)

.010∗∗∗
(.002)

Constant

-.040∗∗∗
(.005)
Yes
Yes
442835
30323
.345
.221
.130

-.004
(.002)
Yes
Yes
442835
30323
.894
.406
.147

User-FEs
Month-FEs
N of obs.
N of users
R2 between
R2 overall
R2 within

Robust standard errors in parentheses are adjusted for clusters in users.
∗

p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

Khwan Kim, Noah Askin, and James A. Evans

23 of 30

Table S10. Results of regression analysis of “radical” taste exploration (threshold = .9). Estimates are from fixed-effects OLS regressions.
Cluster-robust standard errors are shown in parentheses; p-values correspond to two-tailed tests. The threshold for determining radicality of taste
exploration is set to 0.9. That is, one’s radical taste exploration is defined as the proportion of the number of songs whose cosine distance from her
previous taste preference is greater than 0.9 to the number of total songs she consumed in a given month.
DV = Radical taste exploration (>.9) in month t
Model 5
Model 6
Model 7
Model 8
(No AU)
(No BR)
(No AU&BR)
(Interact)

Model 1
(No Cov.)

Model 2
(Months)

Model 3
(Linear)

Model 4
(Quadratic)

-.045∗∗∗
(.000)

-.079∗∗∗
(.005)

-.038∗∗∗
(.006)

-.037∗∗∗
(.006)

-.039∗∗∗
(.006)

.070∗∗∗
(.007)

.070∗∗∗
(.007)

Algorithmic listening

-.001
(.002)

-.001
(.002)

-.000
(.002)

-.001
(.003)

Listening count

.046∗∗∗
(.004)

.045∗∗∗
(.004)

.044∗∗∗
(.004)

Song recency

-.004
(.005)

-.004
(.005)

Distance from global taste

.188∗∗∗
(.006)
.066∗∗∗
(.009)

Constant

Travel distance

.073∗∗∗
(.009)

.072∗∗∗
(.009)

Travel distance2

Travel distance
× Distance from global taste
User-FEs
Month-FEs
N of obs.
N of users
R2 between
R2 overall
R2 within

Yes
Yes
484413
30382
.003
.002
.002

Yes
Yes
484413
30382
.003
.004
.005

Yes
Yes
483633
30337
.001
.002
.022

Model 9
(No AU)

Model 10
(No BR)

Model 11
(No AU&BR)

-.038∗∗∗
(.006)

-.042∗∗∗
(.006)

.068∗∗∗
(.007)

.066∗∗∗
(.007)

-.001
(.003)

-.001
(.002)

-.000
(.002)

-.002
(.003)

-.001
(.003)

.062∗∗∗
(.005)

.061∗∗∗
(.005)

.046∗∗∗
(.004)

.046∗∗∗
(.004)

.063∗∗∗
(.005)

.062∗∗∗
(.005)

-.005
(.005)

-.000
(.006)

-.002
(.006)

-.004
(.005)

-.005
(.005)

.000
(.006)

-.001
(.006)

.188∗∗∗
(.006)

.186∗∗∗
(.006)

.225∗∗∗
(.007)

.224∗∗∗
(.007)

.188∗∗∗
(.006)

.186∗∗∗
(.006)

.225∗∗∗
(.007)

.224∗∗∗
(.007)

.113∗∗∗
(.011)

.136∗∗∗
(.013)

.122∗∗∗
(.013)

.154∗∗∗
(.016)

.067∗∗∗
(.009)

.074∗∗∗
(.010)

.067∗∗∗
(.011)

.079∗∗∗
(.013)

-.003∗∗∗
(.000)

-.003∗∗∗
(.001)

-.004∗∗∗
(.001)

-.005∗∗∗
(.001)
-.004
(.008)
Yes
Yes
483633
30337
.001
.002
.022

-.004
(.010)
Yes
Yes
473830
29723
.001
.002
.021

-.012
(.009)
Yes
Yes
371539
22920
.000
.004
.028

-.012
(.012)
Yes
Yes
361736
22306
.000
.004
.028

Yes
Yes
483633
30337
.000
.003
.022

Yes
Yes
473830
29723
.000
.003
.022

Yes
Yes
371539
22920
.000
.004
.028

Yes
Yes
361736
22306
.000
.004
.028

Robust standard errors in parentheses are adjusted for clusters in users.
∗

p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

24 of 30

Khwan Kim, Noah Askin, and James A. Evans

Table S11. Results of regression analysis of “radical” taste exploration (threshold = .7). Estimates are from fixed-effects OLS regressions.
Cluster-robust standard errors are shown in parentheses; p-values correspond to two-tailed tests. The threshold for determining radicality of taste
exploration is set to 0.7. That is, one’s radical taste exploration is defined as the proportion of the number of songs whose cosine distance from her
previous taste preference is greater than 0.7 to the number of total songs she consumed in a given month.
DV = Radical taste exploration (>.7) in month t
Model 5
Model 6
Model 7
Model 8
(No AU)
(No BR)
(No AU&BR)
(Interact)

Model 1
(No Cov.)

Model 2
(Months)

Model 3
(Linear)

Model 4
(Quadratic)

-.069∗∗∗
(.000)

-.135∗∗∗
(.004)

-.073∗∗∗
(.005)

-.072∗∗∗
(.005)

-.077∗∗∗
(.005)

.060∗∗∗
(.006)

.058∗∗∗
(.006)

Algorithmic listening

.001
(.002)

.001
(.002)

.001
(.002)

.001
(.002)

Listening count

.037∗∗∗
(.003)

.036∗∗∗
(.003)

.035∗∗∗
(.003)

Song recency

-.047∗∗∗
(.004)

-.047∗∗∗
(.004)

Distance from global taste

.236∗∗∗
(.005)
.064∗∗∗
(.007)

Constant

Travel distance

.069∗∗∗
(.007)

.068∗∗∗
(.007)

Travel distance2

Travel distance
× Distance from global taste
User-FEs
Month-FEs
N of obs.
N of users
R2 between
R2 overall
R2 within

Yes
Yes
484413
30382
.002
.002
.002

Yes
Yes
484413
30382
.001
.005
.010

Yes
Yes
483633
30337
.020
.028
.047

Model 9
(No AU)

Model 10
(No BR)

Model 11
(No AU&BR)

-.073∗∗∗
(.005)

-.078∗∗∗
(.005)

.058∗∗∗
(.006)

.055∗∗∗
(.006)

.002
(.002)

.001
(.002)

.001
(.002)

.001
(.002)

.001
(.002)

.047∗∗∗
(.004)

.046∗∗∗
(.004)

.037∗∗∗
(.003)

.036∗∗∗
(.003)

.048∗∗∗
(.004)

.047∗∗∗
(.004)

-.049∗∗∗
(.004)

-.038∗∗∗
(.004)

-.040∗∗∗
(.005)

-.047∗∗∗
(.004)

-.048∗∗∗
(.004)

-.038∗∗∗
(.004)

-.040∗∗∗
(.005)

.236∗∗∗
(.005)

.234∗∗∗
(.005)

.277∗∗∗
(.006)

.276∗∗∗
(.006)

.236∗∗∗
(.005)

.235∗∗∗
(.005)

.277∗∗∗
(.006)

.276∗∗∗
(.006)

.096∗∗∗
(.008)

.115∗∗∗
(.009)

.103∗∗∗
(.009)

.129∗∗∗
(.011)

.063∗∗∗
(.006)

.070∗∗∗
(.007)

.063∗∗∗
(.008)

.073∗∗∗
(.010)

-.002∗∗∗
(.000)

-.002∗∗∗
(.000)

-.003∗∗∗
(.001)

-.004∗∗∗
(.001)
.005
(.007)
Yes
Yes
483633
30337
.020
.028
.047

.006
(.008)
Yes
Yes
473830
29723
.020
.027
.047

-.003
(.008)
Yes
Yes
371539
22920
.033
.040
.063

-.000
(.011)
Yes
Yes
361736
22306
.033
.040
.063

Yes
Yes
483633
30337
.021
.028
.047

Yes
Yes
473830
29723
.020
.028
.047

Yes
Yes
371539
22920
.034
.041
.063

Yes
Yes
361736
22306
.034
.041
.063

Robust standard errors in parentheses are adjusted for clusters in users.
∗

p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

Khwan Kim, Noah Askin, and James A. Evans

25 of 30

Table S12. Results of regression analysis of taste adaptation at the country level. Estimates are from fixed-effects OLS regressions. Cluster-robust
standard errors are shown in parentheses; p-values correspond to two-tailed tests. Month dummies are omitted from the table due to space limitation. The
positive coefficient of taste distance to city appears highly significant across all models. Its interaction with geospatial distance to city is also significantly
positive for the four big-sample countries—France, United Kingdom, Germany, and Brazil.

Model 1
(FR)

Model 2
(UK)

Model 3
(DE)

DV = Taste adaptation to city
Model 4
Model 5
Model 6
(BR)
(RU)
(MA)

Model 7
(AU)

Model 8
(MX)

Model 9
(ZA)

Constant

-.016∗
(.008)

-.080∗∗∗
(.005)

-.160∗∗∗
(.007)

.236∗∗∗
(.009)

.040
(.032)

-.137∗∗
(.043)

-.197∗∗∗
(.015)

.168∗∗∗
(.025)

-.083∗∗
(.026)

Algorithmic listening

.002
(.002)

.005∗∗
(.002)

-.002
(.002)

.017∗∗∗
(.002)

-.004
(.011)

.008
(.012)

.011∗
(.005)

.022
(.011)

.004
(.009)

Listening count

.022∗∗∗
(.004)

.032∗∗∗
(.004)

.025∗∗∗
(.002)

.040∗∗∗
(.004)

.041∗∗
(.014)

.019
(.010)

.019∗∗∗
(.005)

.046∗∗∗
(.007)

.026∗
(.011)

Song recency

.009
(.006)

-.017∗∗∗
(.004)

.046∗∗∗
(.002)

.054∗∗∗
(.003)

-.036
(.018)

.059∗∗
(.022)

-.037∗∗∗
(.008)

-.051∗∗
(.017)

.007
(.011)

Distance from global taste

-.223∗∗∗
(.005)

-.307∗∗∗
(.004)

-.210∗∗∗
(.002)

-.109∗∗∗
(.004)

-.200∗∗∗
(.015)

-.276∗∗∗
(.018)

-.306∗∗∗
(.009)

-.135∗∗∗
(.015)

-.330∗∗∗
(.012)

Geographical distance to city

-.116∗∗∗
(.012)

-.015∗∗∗
(.003)

-.034∗∗
(.012)

-.022∗∗∗
(.004)

-.133∗∗∗
(.031)

-.088∗
(.040)

-.014∗∗∗
(.002)

-.030∗
(.013)

-.029∗∗
(.009)

Taste distance to city

.755∗∗∗
(.009)

.646∗∗∗
(.009)

.648∗∗∗
(.007)

.576∗∗∗
(.018)

.719∗∗∗
(.027)

.747∗∗∗
(.033)

.676∗∗∗
(.025)

.587∗∗∗
(.030)

.720∗∗∗
(.034)

Taste distance to city
× Geographical distance to city
User FEs
Month FEs
N of obs.
N of users
R 2 between
R 2 overall
R 2 within

.081∗∗∗
(.009)
Yes
Yes
594476
6668
.739
.462
.365

.022∗∗
(.007)
Yes
Yes
477351
6198
.794
.466
.263

.059∗∗∗
(.011)
Yes
Yes
815125
7605
.667
.406
.289

.012
(.007)
Yes
Yes
382468
7340
.702
.395
.155

-.000
(.023)
Yes
Yes
16078
584
.510
.443
.389

.016
(.031)
Yes
Yes
18978
155
.724
.434
.304

-.012∗∗
(.004)
Yes
Yes
77123
614
.795
.432
.293

-.017
(.018)
Yes
Yes
13945
304
.581
.353
.278

-.008
(.022)
Yes
Yes
25309
718
.775
.486
.334

Robust standard errors in parentheses are adjusted for clusters in users.
P-values correspond to two-tailed tests.
∗

p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

26 of 30

Khwan Kim, Noah Askin, and James A. Evans

Table S13. Results of triple DiD (DDD) analysis of taste exploration with listening count and time between South Africa and Australia. Estimates
are from fixed-effects OLS regressions. Cluster-robust standard errors are shown in parentheses; p-values correspond to two-tailed tests. Models 1 and 2
are identical to Model 8 and Model 9 in Table S4. Model 3 shows the result of our triple Diff-in-Diffs (DDD) analysis that utilizes listening count as a DDD
interaction term. Model 9 shows the results of another DDD analysis that uses listening time as a DDD interaction term. The results suggest that neither
time-related factor influenced taste exploration among those affected by the lockdown.
Model 1
(Dummy stuck)

Model 2
(Inv. mobility)

Model 3
(Listen. count)

Model 4
(Listen. time)

POST (Mar 26 - May 31, 2020)

.015
(.016)

.231∗∗∗
(.060)

-.020
(.013)

-.020
(.013)

POST × TREATED (S. Africa)

.008
(.015)

-.203∗∗
(.069)

.042∗∗∗
(.010)

.042∗∗∗
(.010)

Dummy stuck

.010
(.010)

POST × Dummy stuck

-.042∗∗
(.014)

TREATED × Dummy stuck

-.007
(.012)

POST × TREATED × Dummy stuck

.041∗
(.016)

DV = Taste exploration

Inverse mobility

.009
(.006)

POST × Inverse mobility

-.037∗∗∗
(.009)

TREATED × Inverse mobility

-.005
(.007)

POST × TREATED × Inverse mobility

.036∗∗∗
(.010)

Listening count

-.038
(.023)

POST × Listening count

.001
(.007)

TREATED × Listening count

-.027∗∗
(.010)

POST × TREATED × Listening count

.004
(.009)

POST × Listening time

.002
(.005)

TREATED × Listening time

-.019∗
(.008)

POST × TREATED × Listening time

.001
(.007)

User-FEs
Week-FEs
N of obs.
N of users
R2 between
R2 overall
R2 within

Yes
Yes
11757
641
.808
.768
.668

Yes
Yes
11757
641
.815
.773
.668

Yes
Yes
11757
641
.807
.768
.669

Yes
Yes
11757
641
.805
.765
.668

Robust standard errors in parentheses are adjusted for clusters in users.
P-values correspond to two-tailed tests.
∗

p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

Khwan Kim, Noah Askin, and James A. Evans

27 of 30

Table S14. Correlations between taste exploration measures using different methods. The pairwise correlation coefficients between the three
different taste exploration measures: our original S2V method (S2V), the Spotify Sonic-S2V variable (Spotify sonic), and the Jaccard approach (Jaccard).
Although the first two methods exhibit a strong correlation, neither shows a significant correlation with the Jaccard variant, lending further support to our
assertion that the Jaccard method is likely too coarse-grained to capture the kind of taste exploration we are examining in our study.
Correlation coefficients
Taste exploration (Spotify sonic)
Taste exploration (Jaccard)

28 of 30

Taste exploration (S2V)
0.596
0.0141

Taste exploration (Spotify sonic)
-0.0304

Khwan Kim, Noah Askin, and James A. Evans

Table S15. Regression analysis of taste exploration using the Jaccard-based measure. The Jaccard dissimilarity variable yields a noticeable
decline in R-squared values across the models, and the statistical significance of the primary predictor variable–travel distance–disappears. Some of the
control variables unexpectedly flip the sign of their coefficients. This discrepancy further underscores our concerns about the appropriateness of the
Jaccard method for our analysis.
DV = Taste exploration
based on Jaccard index

Model 1
(Linear)

Model 2
(Quadratic)

Model 3
(No AU)

Model 4
(No BR)

Model 5
(No AU&BR)

Constant

-.018∗∗∗
(.005)

-.018∗∗∗
(.005)

-.016∗∗
(.005)

.007
(.006)

.011
(.006)

Algorithmic listening

.014∗∗∗
(.002)

.014∗∗∗
(.002)

.014∗∗∗
(.002)

.016∗∗∗
(.002)

.016∗∗∗
(.002)

Listening count

-.042∗∗∗
(.006)

-.041∗∗∗
(.006)

-.041∗∗∗
(.006)

-.043∗∗∗
(.007)

-.043∗∗∗
(.007)

Song recency

-.044∗∗∗
(.004)

-.044∗∗∗
(.004)

-.044∗∗∗
(.005)

-.035∗∗∗
(.005)

-.035∗∗∗
(.005)

Distance from global taste

-.115∗∗∗
(.006)

-.115∗∗∗
(.006)

-.114∗∗∗
(.006)

-.112∗∗∗
(.007)

-.112∗∗∗
(.008)

Travel distance

.011
(.006)

.000
(.006)

.002
(.007)

.006
(.006)

.011
(.006)

.001
(.000)

.000
(.001)

.000
(.000)

-.000
(.000)

Yes
Yes
472832
29653
.021
.018
.014

Yes
Yes
463027
29039
.021
.018
.014

Yes
Yes
363612
22432
.016
.015
.013

Yes
Yes
353807
21818
.015
.015
.013

Travel distance2

User-FEs
Month-FEs
N of obs.
N of users
R2 between
R2 overall
R2 within

Yes
Yes
472832
29653
.021
.018
.014

Robust standard errors in parentheses are adjusted for clusters in users.
P-values correspond to two-tailed tests.
∗

p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

Khwan Kim, Noah Askin, and James A. Evans

29 of 30

113
114
115
116
117
118

References
1. N Askin, M Mauskapf, What makes popular culture popular? product features and optimal differentiation in music. Am.
Sociol. Rev. 82, 910–944 (2017).
2. JM Berg, One-hit wonders versus hit makers: Sustaining success in creative industries. Adm. Sci. Q. 67, 630–673 (2022).
3. AT Barron, J Huang, RL Spang, S DeDeo, Individuals, institutions, and innovation in the debates of the french revolution.
Proc. Natl. Acad. Sci. 115, 4607–4612 (2018).

30 of 30

Khwan Kim, Noah Askin, and James A. Evans
