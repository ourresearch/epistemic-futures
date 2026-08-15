---
title: "Large Scale Analysis of Multitasking Behavior During Remote Meetings"
person: brent-hecht
attendance: unconfirmed
section: by
type: conference-paper
year: 2021
date: 2021-05-06
venue: "arXiv (Cornell University)"
authors: "Hancheng Cao, Chia-Jung Lee, Shamsi Iqbal, Mary Czerwinski, Priscilla N Y Wong, Sean Rintel, Brent Hecht, Jaime Teevan, Longqi Yang"
source_url: https://doi.org/10.1145/3411764.3445243
fulltext_url: https://arxiv.org/pdf/2101.11865
openalex_id: W3123767778
doi: https://doi.org/10.1145/3411764.3445243
oa_status: green
cited_by_count: 135
retrieved: 2026-08-13
content: full-text
notes: "Full text retrieved from the open-access PDF at https://arxiv.org/pdf/2101.11865 (pdftotext; PDF not stored); full text is the arXiv preprint version of this work"
---

# Large Scale Analysis of Multitasking Behavior During Remote Meetings

## Full text

arXiv:2101.11865v1 [cs.CY] 28 Jan 2021

Large Scale Analysis of Multitasking Behavior
During Remote Meetings
Hancheng Cao∗

Chia-Jung Lee†

Shamsi Iqbal

Stanford University
Stanford, CA, USA
hanchcao@stanford.edu

Amazon
Seattle, WA, USA
cjlee@amazon.com

Microsoft
Redmond, WA, USA
shamsi@microsoft.com

Mary Czerwinski

Priscilla Wong

Sean Rintel

Microsoft
Redmond, WA, USA
marycz@microsoft.com

University College London
London, UK
ngoi.wong.13@ucl.ac.uk

Microsoft
Cambridge, UK
serintel@microsoft.com

Brent Hecht

Jaime Teevan

Longqi Yang

Microsoft
Redmond, WA, USA
Brent.Hecht@microsoft.com

Microsoft
Redmond, WA, USA
teevan@microsoft.com

Microsoft
Redmond, WA, USA
Longqi.Yang@microsoft.com

ABSTRACT

1

Virtual meetings are critical for remote work because of the need for
synchronous collaboration in the absence of in-person interactions.
In-meeting multitasking is closely linked to people’s productivity
and wellbeing. However, we currently have limited understanding
of multitasking in remote meetings and its potential impact. In
this paper, we present what we believe is the most comprehensive
study of remote meeting multitasking behavior through an analysis
of a large-scale telemetry dataset collected from February to May
2020 of U.S. Microsoft employees and a 715-person diary study.
Our results demonstrate that intrinsic meeting characteristics such
as size, length, time, and type, significantly correlate with the extent to which people multitask, and multitasking can lead to both
positive and negative outcomes. Our findings suggest important
best-practice guidelines for remote meetings (e.g., avoid important
meetings in the morning) and design implications for productivity
tools (e.g., support positive remote multitasking).

Remote work is an essential mode of work across industries [7].
Before COVID-19, many companies had already experimented with
or implemented various forms of remote work [9], e.g., recruiting remote employees or allowing employees to work from home
part-time. During the pandemic, 34.1% of Americans switched to
working from home [9], and it is estimated that 37% of jobs in
United States can be done remotely [24]. In fact, many large technology companies, such as Quora and Twitter, have announced that
they will allow employees to work from home indefinitely [1, 34].
Central to remote work are remote meetings [12, 50], most commonly experienced through video conferencing tools (e.g., Zoom,
Microsoft Teams, Google Meet), which help remote team members
stay connected, collaborate and function as an organization, despite
physical distance. Therefore, it is critical to understand factors that
are associated with remote meeting experiences to better support
productive and engaging remote collaborations.
In this paper, we focus on one fundamental experience of remote meetings — in-meeting multitasking. Information work is
often governed by multiple tasks and activities that an individual
must remember to perform, often in parallel or in rapid succession, a practice that is called multitasking [18, 57, 65]. Multitasking
behavior is vital, as it is closely linked to one’s productivity and
well-being [18, 38] — increasing the numbers of items to be remembered can wreak havoc with task resumption [4], attentional
focus [28, 32] and prospective memory [8]. Multitasking during
meetings can additionally affect other people and their productivity
[31]. Prior work has investigated how people engage in multitasking during collaborative activities such as meetings and video chats,
both in-person and online [30, 31, 45, 62]. However, these works
are mainly based on small-scale qualitative studies, and to the best
of our knowledge, no research to date has reported systematic and
comprehensive evidence from large populations. As a result, there
is little statistical evidence on the meeting and personal context

CCS CONCEPTS
• Human-centered computing → Empirical studies in collaborative and social computing.

KEYWORDS
Multitasking, meeting, collaboration, remote work
ACM Reference Format:
Hancheng Cao, Chia-Jung Lee, Shamsi Iqbal, Mary Czerwinski, Priscilla
Wong, Sean Rintel, Brent Hecht, Jaime Teevan, and Longqi Yang. 2021.
Large Scale Analysis of Multitasking Behavior During Remote Meetings. In
Proceedings of ACM Conference (Conference’17). ACM, New York, NY, USA,
13 pages. https://doi.org/10.1145/nnnnnnn.nnnnnnn
∗ The work was done when Hancheng Cao interned at Microsoft.
† The work was done when Chia-Jung Lee worked full time at Microsoft.

Conference’17, July 2017, Washington, DC, USA
2021. ACM ISBN 978-x-xxxx-xxxx-x/YY/MM. . . $15.00
https://doi.org/10.1145/nnnnnnn.nnnnnnn

INTRODUCTION

Conference’17, July 2017, Washington, DC, USA

that are associated with people’s propensity to multitask, the activities remote attendees engage in while multitasking, and how such
remote multitasking behavior may affect workers and groups.
Here, we adopt a mixed-methods approach to systematically
understand the context, activities, and consequences of multitasking during remote meetings. Specifically, we analyzed a large-scale
dataset collected from from February to May 2020 of U.S. Microsoft
employees. The dataset contains anonymized events from major
productivity tools: Microsoft Teams for remote meetings, Microsoft
Outlook for email services, and OneDrive and Sharepoint for accessing and editing files remotely. Multitasking can involve activities
that are unrelated to the meeting (e.g., email communications) and
related (e.g., notes taking) [31]. Therefore we measured emails sent
and files edited during remote meetings as a proxy for multitasking and studied the relationship between multitasking and meeting
characteristics through controlled regression analysis. Furthermore,
we contextualize the evidence from log analysis with verbatims
from a 715-person diary study of Microsoft employees globally, run
from mid-April to mid August 2020, exploring their remote meeting
experiences during COVID-19.
Our results show that: 1) Multitasking is a common behavior
in remote meetings with about 30% of meetings involving email
multitasking. People also reported that multitasking becomes more
frequent as meetings move to remote, 2) Intrinsic meeting characteristics, such as meeting size, length, type, and timing, significantly
correlate with the extent to which people multitask, e.g., people are
more likely to multitask in recurring meetings than in ad hoc meetings, and 3) In-meeting multitasking during remote meetings can
lead to both positive (e.g., improve productivity) and negative (e.g.,
loss of attention) experiences. Our analysis suggests practical ways
people can improve remote meeting experiences. For example, to
reduce unnecessary scheduled and recurring meetings, keep meetings short, avoid intensive meetings early in the morning, and allow
space for positive multitasking. Our work implies that productivity
tools can help people better manage their in-meeting attention and
decide which meetings or parts of the meetings to attend.
The contributions of this paper are threefold:
• We present the first large-scale, empirical study of multitasking behavior during remote meetings, accompanied by
rich qualitative evidence. This allows us to understand the
factors that correlate with remote meeting multitasking and
characterize the motivations and potential consequences of
such behavior.
• We discover several key issues in current remote meeting
configurations and suggest actionable guidelines for how
people may schedule effective remote meetings (Section 8).
• Our work points to several concrete design implications
for future remote collaboration tools, e.g., support meeting
“focus mode” and positive multitasking.

2

BACKGROUND AND RELATED WORK

Our work is built upon and contributes to the rich HCI literature on
remote work and multitasking behavior and its manifestations in
meetings. Prior research mostly focused on small-scale in-person

Cao et al.

studies, whereas our work analyzes a large-scale log dataset accompanied by a large diary study, to systematically reveal multitasking
patterns during all-remote meetings.

2.1

Remote Work

Remote work has long been an important topic of research across
scientific fields. Through a Working-From-Home (WFH) experiment at Ctrip, a 16,000-employee Chinese travel agency, Bloom et
al. [7] studied the costs and benefits of remote work, where they
showed that WFH led to improved performance but reduced promotion rate. Prior work also investigated other aspects of remote work,
such as management of workers [23], organizational design [53,
63], communication challenges [29], team performance [37], wellbeing [12, 64], and emerging roles [14] and experience [10, 11].
Remote work becomes more ubiquitous after the COVID-19 pandemic [26, 67], and remote meetings have become a central place
where people stay connected and collaborate with others [50] —
both DeFilippis et al. [22] and Yang et al. [67] demonstrated a significant increase in remote meetings during the pandemic. Here
we contribute to the rich literature of remote work by focusing on
how in-meeting multitasking, an artifact of traditional in-person
meetings, manifested in all-remote settings.

2.2

Multitasking in the Workplace

A large body of prior work has focused on how multitasking impacts
attention in the workplace, primarily focusing on the distraction
caused to an ongoing task that is interrupted by another activity. Czerwinski et al. [18] employed a diary study to show how
information workers switch activities due to interruptions in the
workplace, focusing on the difficulty of the continuous switching of
context. Iqbal and Horvitz [32] studied how external interruptions
cause information workers to enter into a “chain of distraction”
where stages of preparation, diversion, resumption and recovery
can describe the time away from an ongoing task. Gonzalez and
Mark [27] reported on how information workers conceptualize and
organize basic units of tasks and how switching occurs across these
conceptual units — people were found to spend about 12 minutes
in one working unit before switching to another. In the mobile
domain, Karlson et al. [35] and Park et al. [51] found that tasks on
mobile phones become fragmented across devices and they identified challenges that exist in resuming these tasks. While most
studies have looked at multitasking results from distractions, there
is a gap in prior work that characterizes interactions corresponding
to multitasking during remote meetings, as discussed in Section 2.4.

2.3

Factors Associated with Multitasking

External [31, 40, 44, 49] and internal [2, 20] interruptions are considered to be the most direct reasons behind multitasking; however
there are other indirect factors that are associated with multitasking
as well. Past work has shown that personality and organizational
environment [20] are associated with multitasking [43]. Additionally, previous work [42] has shown that the time of day is associated
with workers’ focus. On average, people were most focused in their
work late-morning (11 a.m.) and mid-afternoon (2-3 p.m.), which is
known as the “double peak day” of information workers’ rhythm

Large Scale Analysis of Multitasking Behavior
During Remote Meetings

of work. Day of the week also play important role in people’s attention level and multitasking behavior. Mark et al. [42] found a
relationship between online activity and Mondays, the day when
people report being the most bored, but at the same time also the
most focused. However, most of the prior studies are focused on
in-person work settings, and it is unclear to what extent these patterns are applicable to remote meetings. Also, the existing evidence
is mainly based on small-scale data that may not generalize to
large organizations. Our study confirms the associations between
time, distractions and multitasking in remote meetings through
large-scale log analysis and greatly extends prior knowledge by
investigating a broader range of meeting characteristics, such as
meeting size, type, and length.

2.4

Multitasking during Meetings

While multitasking during one’s own work mostly impacts personal productivity, special consideration of multitasking during
meetings is warranted, as this can additionally impact other colleagues and their productivity [31]. Past work has looked at how
people engage in multitasking both during in-person meetings and
presentations [6, 30, 31], as well as online collaborative activities,
such as remote meetings leveraging subjective feedback or perceptions [45, 62]. For example, in educational settings, the use of
laptops during a lecture has been shown to have a negative impact
on attention, where students tend to engage in activities such as
web-surfing or emailing rather than activities related to the lecture [6, 30]. However, in other studies, people who multitask during
in-person meetings report to do so in order to interleave other important activities as they peripherally pay attention to the meeting
and engage only when relevant [31]. In online settings, both meeting related and personal multitasking are seen as ways people’s
attention could divert from the actual conversation, though multitasking on a single screen is considered more acceptable than when
multitasking is happening on a different screen - often presumed to
be unrelated to the meeting [45]. Similarly, a study on video-chats
among teens found that boredom was the main reason why teens
would multitask during a video chat, wherein they would engage
in scrolling social feeds or play games [62].
While prior work on meetings and multitasking focus primarily
subjective perceptions, no research to the best of our knowledge has
looked at large-scale log data accompanied by qualitative evidence
on what people are engaging in while attending a meeting and
under what conditions people tend to engage in when multitasking. Our analysis of actual interactions can complement subjective
perceptions around multitasking motivations, behaviors and potential consequences, and can provide insights into how to conduct
meetings for maximal effectiveness.

3

METHOD

To systematically understand multitasking patterns during remote
meetings, we proposed the following research questions to guide
our research.
Research Question 0 (RQ0). How much multitasking is happening during remote meetings?
Research Question 1 (RQ1). What factors are associated with
multitasking during remote meetings?

Conference’17, July 2017, Washington, DC, USA

Research Question 2 (RQ2). What do people do when multitasking during remote meetings?
Research Question 3 (RQ3). What are the consequences of multitasking during remote meetings?
As noted above, we adopt a mixed-methods approach to address
these questions: analysis of a large-scale anonymized telemetry
dataset coupled with a diary study of people’s perceptions and
subjective experiences with respect to in-meeting multitasking.

3.1

Regression Analysis on Large-Scale
Telemetry Dataset

Data Preparation. We collected metadata (without any content
information) on remote meetings (Microsoft Teams), email usage
(Microsoft Outlook), and file edits (Onedrive/Sharepoint) of US employees from Microsoft. The majority of work and communication
in Microsoft are carried out through these platforms. We collected
four separate week-long snapshots of data from February to May,
2020: 1) February 24-28, which represents a period of pre-COVID,
mostly co-located work, 2) March 23-27, which represents the company’s transition phase from mostly co-located work to remote
work, and 3) April 20-24 and 4) May 18-22, to represent fully remote work periods. While we leveraged all four periods to study
work rhythm and derive statistics on multitasking behavior, our
regression analysis focused on the snapshot from May 18-22, when
employees were fully settled into working from home.
Specifically, for each meeting hosted on Microsoft Teams1 , we
collected the start and end timestamps of the meeting 2 , meeting
size3 , and the meeting type (ad hoc, scheduled, recurring or broadcast4 ), and their distributions are presented in Fig. 1(a). As shown
in Table. 1, we discretized continuous meeting attributes in the
following ways to ensure robustness of the regression analysis. We
grouped meeting duration into four categories — 0-20 mins, 20-40
mins, 40-80 mins, and >80 mins because of the popularity of 30
mins and 60 mins meetings (Fig. 1(a)). For meeting size, due to its
long-tail nature, we split it into five roughly equal sized bins. We
considered morning, afternoon, and after hours as three categories
for hour of the day in order to align it with common work rhythms
in Microsoft.5 Furthermore, we tested the meeting attribute correlation, where we find rather weak correlations (|𝑟 | < 0.15) among
different attribute groups. For instance, the correlation between
meeting time (e.g., morning) and meeting size (e.g., >10 attendees)
is around 0.07. The weak dependency between meeting attributes
motivated us to directly include them in the regression analysis
rather than trying to cluster various meeting types and study those
clusters in the regression. Finally, we note that the telemetry data
1 We only included meetings that are longer than two minutes to filter out data noise.
We also filtered out meetings lasting longer than 3 hours, which is likely due to the
fact people forget to leave the meeting.
2 Meeting start and end timestamps was logged on a per-person basis, i.e, the exact
timestamp that each person attended and left a meeting. The average standard deviation
of meeting duration among people joining the same meeting is about 2.1% of the
maximum meeting duration, indicating that the same meeting generally has similar
length across participants.
3 Meeting size was logged as the number of all people ever connected to a meeting. Due
to aggregated nature of telemetry data, it is impossible to measure the exact maximum
concurrent participants.
4 Meetings that have more than 250 attendees.
5 We tested different bucketing strategies and it produced robust results.

Conference’17, July 2017, Washington, DC, USA

only records virtual meetings, so February data (before pandemic
in U.S.) does not reflect total volume of meetings people attended,
but all meetings after the pandemic are recorded.
We focused on two multitasking behavior during remote meetings that can be measured through available telemetry data: email
multitasking and file edit multitasking. To enable the analysis, on
Microsoft Outlook, we collected the time when people actively send,
respond to, or forward an email. On file platforms, we recorded
events related to editing productivity-related files, including Excel,
Powerpoint, Word, and PDFs. Note that due to the nature of the
data, we are not able to differentiate whether the files are related
to the meeting or not, thus the measured multitasking file behavior
might be related to the meeting (e.g. notes taking).
To ensure people’s privacy with the telemetry data, we performed pre-processing to de-identify workers before the data was
obtained by researchers. Access to the data was strictly limited
to authorized members of the research team who went through
extensive privacy and ethical training.
Regression Analysis. We joined three data sources by unique
user identifiers (anonymized), which resulted in 34,524 (meeting,
user) records. For each (meeting, user) pair, we labeled it as email
multitasking (𝑌 = 1) if the user was found to have at least one active
email action during the meeting, otherwise a non-multitasking label
was assigned (𝑌 = 0). File multitasking was labeled similarly. We
conducted a regression analysis to understand the relationships between multitasking and meeting characteristics, while controlling
for individual variances since the individual tendency to multitask
may confound the estimation. We leveraged stratification [48] to
group all records by worker and used conditional logistic regression to fit the model. The binary meeting indicators used in the
regression model are defined in Table. 1. To account for the correlations between the records from the same meetings, we grouped
standard errors at the meeting level. We present regression results
in terms of estimated odds ratio and their statistical significance in
Fig. 3. We did not find significant correlations between file-related
multitasking and meeting characteristics, which could be attributed
to the fact that files edited are often related to the meeting (Section 6.1). An alternative analysis using Generalized Linear Mixed
Effects Models [58] show qualitatively similar results (Appendix A).
Limitations of Telemetry Data. While the large-scale telemetry data provides us with a lens onto how people behave during
meetings, our emphasis on preserving privacy means that we unfortunately do not have access to all behavioral details. The data
was collected in anonymized, aggregated form and does not have
sensitive attributes that can potentially reveal the identity of an
individual employee or a group in a corporation, such as functional labels, job roles, organizational charts or participant social
demographics. Email is perceived as stateless communication in the
organization we studied; therefore, fine-grained events e.g., email
read was not recorded. Similarly, multitasking behavior in 3rd party
platforms and non-digital spaces (e.g., house chores), is not measured due to lack of instrumentation. Finally, telemetry data lacks
information on the reasons for and consequences of multitasking.
We strive to address these limitations by a complementary diary
study where we delve deeper into the trends shown in the telemetry
data set.

Cao et al.

3.2

Diary Study

We complement our quantitative analysis with reports drawn from
a diary study of employees from Microsoft reporting their experiences of remote meetings during COVID-19. Diary studies in
HCI research [55] have been particularly effective in capturing the
nuanced experiences of information workers [18, 59].
The diary study data collection ran between mid-April and midAugust 2020. Participants opted-in to the study from bulk email
messages sent to internal mailing lists, with rolling recruitment
between mid-April and mid-June 2020. Participants were asked
to keep a guided diary for two months. Diary reminders were
sent as a file via email to participants to set up in their calendars.
The diaries consisted of a series of forms embedded in a secure
company website. 24 total diary entries were requested, one entry
approximately every two working days for two months total. The
24 guided entries were to be filled out in three cycles of eight topics:
Physical workspace, Interaction, Productivity, Tools, Multitasking,
Types of meetings, Time in meetings, and Approaches to meetings.
The three diary entries on Multitasking used the following primary
prompt: "What have you noticed about multitasking in recent online
meetings?". This was followed by a list of sub-prompts: How and
when you multitask; Why you multitask; Managing video and audio;
Group expectations around multitasking; Impact of multitasking
on productivity; Impact of multitasking on conversations; Features
for multitasking; Impact of home life; Suggestions for improvement.
Full methodological details are available in a technical report [56].
849 total participants provided consent and were onboarded, of
which 715 completed at least one diary entry. For those who filled
out diaries: Gender coverage was 60% Male, 39% Female, and 1% nonbinary or preferred not to say. Age coverage was 5% 18-24, 28% 25-34,
30% 35-44, 28% 45-54, 8% Above 55, and 1% Prefer Not To Say. Roles
covered were 41% Business & Sales, 30% Development, 11% Creative,
Design, and UX, 11% Technical Operations, 5% Administration, and
2% Research. Participants were drawn from almost all regions of
the world, primarily 53% North America, 20% Europe, 12% India,
4% China, and 4% South America.
Of 7045 total rows of diary responses, 819 responded specifically to the multitasking prompt6 from 413 unique participants.
We randomly selected 100 responses (20 per month from April to
August). To analyze the responses, we adopted the method of open
coding [15]. Five researchers independently analyzed and coded the
first 20% of the interview transcriptions and met to discuss the codes
until they were in complete agreement on the codes needed. Then,
one researcher coded the remaining transcriptions but discussed
any questions with the four other researchers so as to guarantee
consensus on the codes. When these steps were finished, the whole
research team met and thoroughly discussed the extracted content
classification. Through sub-categorization and constant comparison [16], we consistently revised the emerging themes and the final
themes presented in Sec 4, 5, 6 and 7 were developed.
To ensure people’s privacy in the diary study, we de-identified
data before analysis (a participant key linked demographics to diary
entries, and then all diary entries were scrubbed for names, places,
and other identifying referents). Similar to the telemetry data set,
only authorized researchers have access to the diary data.
6 We did not include responses mentioning "multitasking" under other prompts.

Large Scale Analysis of Multitasking Behavior
During Remote Meetings

(a) Distribution of meeting duration

Conference’17, July 2017, Washington, DC, USA

(b) Distribution of meeting size

(c) Distribution of meeting types

Figure 1: Distributions of virtual meeting duration, meeting size, and meeting types measured through our collected telemetry data. We observe two clear peaks surrounding 30 mins and 60 mins in distribution of meeting duration, indicating the
popularity of scheduling 30 mins and 60 mins meetings. We observe a long tail distribution of meeting size, where over 20%
of all meetings are one on one meetings. Finally, we observe the majority of meetings are scheduled meetings, followed by
recurring meetings, adhoc meetings and broadcast meetings. The data distributions motivate us to discretize features into bins
specified in Table 1.
Table 1: Meeting property and discretized bins used for regression analysis. For each meeting property, we create dummy
variables and then left one out as baseline. For instance, Friday is left as baseline for the day of the week meeting property,
and all effects are relative to meetings on Friday.

4

Meeting Property

Discretized bins

Meeting duration
Meeting size
Meeting types
Hour of the day
Day of the week

0-20 mins meetings (baseline), 20-40 mins meetings, 40-80 mins meetings, >80 mins meetings
2 attendees (baseline), 3 attendees, 4-5 attendees, 6-10 attendes, >10 attendees.
scheduled, recurring, ad hoc (baseline), broadcast
morning: 7am - noon, afternoon: noon - 7pm, after hours: 7pm - 7am (baseline)
Monday, Tuesday, Wednesday, Thursday, Friday (baseline)

RQ0: VOLUME OF MULTITASKING DURING
REMOTE MEETING

Our analysis suggests that multitasking during remote meetings is
ubiquitous, and that people find themselves engaging in more multitasking during remote meetings compared to in-person meetings,
possibly as a result of a shift in work rhythms, and the lower cost
to get noticed.
Multitasking intensity over time. In our telemetry dataset,
from February to May, we find that 31.1%, 30.9%, 29.2%, and 28.9%
meetings involve email multitasking, and 23.7%, 23.1%, 24.8%, and
25.5% meetings involve file multitasking. Putting these percentages
in the societal context of the cognitive efforts and resources that
information work costs [61], our results suggest the importance of
understanding and potentially intervening toward such behavior.
More multitasking as a possible result of work rhythm
adaptation. Fig. 2 illustrates the shift of work rhythms, characterized by the distribution of work related actions (emails sent,
files edited and meetings attended) within a day, from Feb 2020
to May 2020. The email and file-related rhythms throughout the
day remain roughly unchanged, indicating that people worked in a
similar fashion on emails and files as they did in co-located settings.
Meanwhile, there is a clear increase in the number of remote meetings, compared to pre-COVID-19 period – note that the telemetry
results do not necessarily support the conjecture that people are
meeting more since not all in-person meeting frequencies were
recorded in the telemetry. However, our diary study results suggest

that people do perceive that they have more meetings, and this may
be an important underlying cause of multitasking during remote
meetings.
"I think this is more of a habit that developed now that folks
don’t have face to face meetings at all and that the number of
meetings has increased so much that it is just more efficient to
get the notes and reading out of the way during the meeting
than work extra hours end of day or early next day to catch up"
(R498)
"There are so many meetings that there is no time to look at email,
or get work done in between. I try and work early in the morning
and late at night, but as work flows in during the day and needs
response, I find myself more and more just multitasking" (R179)
Ease of turning off video and audio may encourage more
multitasking. In comparison with traditional face-to-face meetings, remote meetings make it much easier for people to stay in
the background by turning video off/muting themselves. Given
that multitasking has been culturally associated with impoliteness
[52], we assume more multitasking during remote meetings may be
caused by the lower probability of getting noticed by others when
multitasking. In our diary study responses, we found that turning
off the video camera or muting the microphone was closely related
to multitasking behavior, as mentioned by many (32% of responses).
"I typically will not multi-task if I have my video on, because
people can definitely tell when you’re not paying attention. Sometimes I will choose to turn my video on purely so that I am not

Conference’17, July 2017, Washington, DC, USA

(a) Email Action Daily Rhythm

Cao et al.

(b) File Action Daily Rhythm

(c) Remote Meeting Daily Rhythm

Figure 2: Transition of worker work rhythms (i.e., distribution of work related actions over time within a day) from Feb. 2020
(pre-COVID-19) to May 2020 on email, file editing actions and remote meetings. While email and file usage remains stable,
there is a clear increase in the volume (over twice as much) of remote meetings after the breakout of the pandemic. Results
are normalized using maximum volume in Feburary.
tempted to multi-task. If I am an optional participant in a meeting, or I am just listening in, unsure if the agenda really calls
for my participation, then I am more likely to keep my video off
and openly multi-task until someone says my name." (R10)
"In general, I have a feeling that in our group the expectation
is that participants do not multitask during meetings, but who
knows what you are doing if the camera is off. (So yeah, that’s
when I turn off my camera too.)" (R14)

5

RQ1: WHAT FACTORS ARE ASSOCIATED
WITH MULTITASKING

Our analysis suggests that both intrinsic meeting characteristics and
external factors are correlated with remote meeting multitasking,
as discussed in detail below.

5.1

Intrinsic Meeting Characteristics

More multitasking happens in large meetings. As shown in
Fig. 3(b) and Fig. 4(b), larger meetings generally involve more multitasking. The odds of email multitasking in 3 attendee meetings,
4-5 attendee meetings, 6-10 attendee meetings, and >10 attendee
meetings are 1.12 (𝑃 = 0.021), 1.39 (𝑃 < 0.001), 1.70 (𝑃 < 0.001) and
2.16 (𝑃 < 0.001) times the odds of the meetings with only one or
two attendees. This could be explained by the fact that participants
need to more actively focus on the meeting conversations when
the meetings are small. Our empirical finding is also supported by
evidence from the diary study, e.g.,
"If it’s a large audience, like a webcast or an internal session on
some tech topic, I do multitask more." (R4)
"In the big meetings, like town halls, I tend to stop and actually
listen when something of interest is being said. the rest of the time,
I seem to not focus on work at all. In small meetings, I generally
don’t multitask at all anymore. It takes all of my brainpower to
focus on the conversation." (R182)
More multitasking happens in long meetings. We also observe that more multitasking happens in longer meetings. From
telemetry data, we observe that the odds of email multitasking in
20-40 minute meetings, 40-80 minute meetings, and >80 minute
meetings are 1.96, 3.22 and 6.21 times the odds of 0-20 minutes

meetings (𝑃 < 0.001), as illustrated in Fig. 4(a) and Fig. 3(a)). As
supported by diary study responses, many people mention that
they simply cannot concentrate for a long time and thus engage in
multitasking during long meetings.
"Additionally, meetings seem to be longer (e.g., I have a three
hour brainstorming session with my team today) and I cannot
focus on the meeting that long alone. Then I also tend to work
on other tasks from now and then." (R21)
Morning meetings involve more multitasking. The time
schedule of the meeting also plays an important role in multitasking
behavior. Our email multitasking data analysis suggests that morning meetings involve more multitasking compared to afternoon
and after hours: the odds of multitasking in the morning are 1.86
times the odds of the after hour meeting baseline (𝑃 < 0.001), and
the odds of email multitasking in the afternoon are 1.54 times the
odds of the after hour meeting baseline (𝑃 < 0.001). We argue that
this observation may be closely related to the daily work rhythms
of individuals. As demonstrated by prior work [42], in the afternoon people are generally more focused. We also find supporting
evidence in the diary study results (6% of responses)
"I will try to glimpse at email more if a meeting is the first thing
I do for work in the morning - so that’s schedule-related." (R621)
More multitasking happens in recurring and scheduled
meetings compared to ad hoc meetings. Next, our results suggest that multitasking is more likely to happen in recurring and
scheduled meetings compared to ad hoc meetings. We find significant associations between email multitasking and meeting types
in our telemetry data. Specifically, the odds of email multitasking
in recurring and scheduled meetings is 1.59 (𝑃 < 0.001) and 1.31
(𝑃 = 0.012) times the odds of multitasking in ad hoc meetings.
Ad hoc meetings generally involve a specific focus relevant to the
specific attendees, while scheduled meetings, especially recurring
meetings, are more likely to involve broader information sharing
which does apply equally to each attendee.
"I just came off an online call with my larger design sync, it’s a
30 min recurring meeting where we share topics as our design
teams are in [two cities]. I didn’t need to present, I was a listener,
so I found myself responding to Teams messages, emails etc as
the call was going on." (R42)

Large Scale Analysis of Multitasking Behavior
During Remote Meetings

Conference’17, July 2017, Washington, DC, USA

(a) Meeting duration, >80 mins (𝑃 < 0.001), 40-80 mins (b) Meeting size, >10 attendees (𝑃 = 0.021), 6-10 attendees (c) Meeting type, scheduled (𝑃 = 0.012), recurring
(𝑃 < 0.001), 20-40 mins (𝑃 < 0.001)
(𝑃 < 0.001), 4-5 attendees (𝑃 < 0.001), 3 attendees (𝑃 = (𝑃 < 0.001), broadcast (𝑃 = 0.880)
0.021)

(d) Hour of the day, morning (𝑃 < 0.001), afternoon (𝑃 < (e) Day of the Week, Thursday (𝑃 = 0.003), Wednesday
0.001)
(𝑃 = 0.003), Tuesday (𝑃 < 0.001), Monday (𝑃 = 0.001)

Figure 3: Conditional logistic regression results on the relationship between email multitasking and remote meeting characteristics. We find significant associations between email multitasking and meeting duration, meeting size, meeting types, hour
of the day and day of the week.
More multitasking happens Monday through Thursday
compared to Friday. The telemetry data also demonstrated that
Friday has a relatively lower likelihood of multitasking, compared
to other days of the week. The odds of email multitasking on Tuesday are 1.35 times the odds of multitasking on Friday (𝑃 < 0.001),
followed by Monday (1.23 times, 𝑃 = 0.001), Wednesday (1.19 times,
𝑃 = 0.003) and Thursday (1.19 times, 𝑃 = 0.003). While this pattern
corroborates findings from prior work [42], we note that the result
might not generalize broadly, especially for Fridays, since Microsoft
encourages fewer meetings on Friday, so the findings might be
company-specific.
More multitasking in meetings of lower relevance and engagement. People also frequently mentioned (17 % responses) that
they multitask during meetings they find irrelevant or have lack
of interest or engagement in, which might be the underlying reason why people multitask more in larger group sizes and longer
meetings.
"I tend to multitask more in larger group meetings online. Larger
meetings often have topics on the agenda not directly related to
what I’m working on day to day so my mind tends to wander
when the topic of discussion is irrelevant. I’m definitely aware
of trappings of a divided mind. I’m not necessarily productive
on these other tasks. So I normally engage in menial work like
cleaning and organizing files." (R11)

"I myself frequently have a web page, source code, or build window open in another window, and I divide my attention - most
often when the meeting goes to topics that don’t concern me, as
most of my meetings do." (R15)
"When meetings have a lot of topics or don’t apply to me, I start
multitasking." (R16)
Sometimes people lose their concentration due to high cognitive
load under such meetings of low relevance,
"I’ve noticed that I only multitask when I am tired and it is
difficult for me to focus on the ongoing meeting. And I don’t
do difficult tasks either, at most I am checking if my PR went
through or kick off a build or just look at pictures of cats. " (R14)
"It’s really hard to focus, I don’t know what people are trying
to say or what the actions items after or why we’re discussing
certain items. When I can’t focus or understand what’s going
on, I tend to check out and look at other things or do something
where I feel engaged and useful. " (R346)

5.2

Extrinsic Factors

People multitask during meetings to catch up on other work.
Another major reason (39 % responses) why people multitask is to
catch up on their work. Given the increasing number of meetings
compared to the in-person work experience, people find they are
having a hard time completing all of their work in time.
"It needs to happen or you cant get all your work done " (R167)

Conference’17, July 2017, Washington, DC, USA

Cao et al.

(a) Meeting duration

(b) Meeting size

(d) Hour of the day

(c) Meeting types

(e) Day of the Week

Figure 4: Proportion of user-meeting pairs with email multitasking versus meeting characteristics measured by telemetry data.
People multitask more in longer meetings, larger meetings, recurring/scheduled meetings, morning meetings and Tuesdays.
"But these days I am having a lot of meetings, making it hard to
find time to get work done. So, feel super tempted to multi task,
if not entire day goes in meetings before real work gets started.
Another reason to multitask is deadlines... " (R12)
"My team is often quite bad at sticking to an agenda, so I find
myself multitasking as a way to feel like I’m still able to "get
things done"while I’m ’sitting in’ on these meetings. As a designer,
that often means that I’m clicking around in Figma. Increasingly,
I am also trying to use meeting time to catch up on context for
other meetings. This makes paying attention in any meeting very
difficult, but with the volume of meetings and the complexity of
the context I feel I need to maintain, I often feel like I have no
choice." (R9)
"Lately (since COVID) I’ve been forced to multitask during meetings to meet the deadlines that I’ve been given (and even then,
I still don’t always make it)... I don’t have enough hours in the
day to do all of the work that is required of me." (R346)
People multitask during meetings due to external distractions. We also find people frequently multitask during remote
meetings as a result of external distractions - under such situations, people do not purposely multitask, but their attention gets
attracted by external sources. Two major classes of distractions are
interface design, and the home working environment. As collaboration moves online in remote work, people are interacting with
digital tools more than they used to when co-located at work, and
people are mentioning that interface designs can be the cause of
multitasking behavior, especially pop-ups, e.g.,
"I multi-task in almost every meeting that isn’t 1-1 and even in
1-1 meetings it’s hard not to multi-task because email and teams

chats are popping in. In person for 1-1 i would lock my computer
and focus entirely on the person and this is super hard in the
WFH setup." (R502)
"There are a lot of people are multitasking as we are using Teams.
Teams is prompting up that someone is trying to get hold of us.
This lures us in to checking quickly in to who it is an what they
want" (R664)
On the other hand, as pointed out by prior qualitative work [3],
remote work involves more distractions from the home working
environment that could lead people to multitasking, e.g.,
"Since COVID19 the multitasking also includes: - answering children’s questions - preparing food for children - Helping children
with school work - resolving children’s disagreements " (R183)
People multitask during meetings for anxiety relief. Finally, some participants mentioned that anxiety over the COVID-19
pandemic lead them to seek methods for maintaining focus, such as
conducting a low cognitive effort non-work activities while monitoring meetings.
"The current situation has increased my general anxiety. This
means I have more difficulty focusing on tasks - including meetings. I have been multi-tasking with non-work tasks (i.e. a colouring game on my phone!) quite a bit as I find this actually enables
me to focus better on the meeting." (R5)
"Doing some exercises with my shoulders/back during meetings
(with video turned off) is great." (R13)

Large Scale Analysis of Multitasking Behavior
During Remote Meetings

6

RQ2: WHAT DO PEOPLE DO WHEN
MULTITASKING

Our analysis further shows that people engage in work-related and
non-work-related tasks when multitasking during remote meetings.

6.1

"It has been beneficial to walk around my house while on meetings (that don’t require me to be in front of my computer). I’m
able to put dinner in the oven, feed the dogs, etc." (R668)

7

Work-related tasks

Communication with coworkers is one of the most frequently mentioned multitasking behavior, since people generally consider that
communication is quick to complete without much need to focus,
or "light weight”. In fact, 29 % of diary study participants mention
that they engage in email multitasking, which further confirms and
strengthens our motivation to analyze email multitasking using the
telemetry data set.
"I might use that time to reply to simple emails that don’t require
much thinking (so I can also pay attention to the meeting)."
(R170)
"And there are different levels of multitasking, meaning the kinds
of multitasking things I will do during meetings can range from
writing down a quick reminder to myself on a different topic
(takes a few seconds) to triaging email which takes very short
attention shifts and I can come back into the proceedings easily, to more cognitively demanding tasks like writing emails,
responding to IM threads etc." (R171)
Meanwhile, several diary study participants mentioned that they
also frequently check and test scripts that take time to run during
remote meetings, which is also rather lightweight.
"There have been situations where I’ve multitasked in the sense of
responding to email or checking on the results of a long running
job while in a meeting that is more focused on consumption of
information rather than on my own contributions." (R180)
"Because I have done a lot testing and building scripts. It takes
time, so I can work with other stuff while waiting for the result."
(R337)
People also mentioned that they engaged in file multitasking,
yet these activities are often related to the meeting, e.g., notes
taking (R182, R183, R344), checking relevant files (e.g. "in a meeting
discussing aspects of the project I linked to the latest documentation.",
R174), etc., which could be a possible explanation of why there is
no significant relationship between file-related multitasking and
meeting characteristics.

6.2

Conference’17, July 2017, Washington, DC, USA

Non-work-related tasks

Non-work tasks is also an emerging theme in the diary study responses. For instance, checking social media as a break from work.
"I’ve been multitasking both for personal and professional things
- answering emails and chats for work, taking social media and
texting breaks for personal." (R168)
Given that working from home environment under COVID-19,
people also reported that they engaged in eating, exercise (primarily
for anxiety relief and wellness) and other household chores.
"As my kitchen is very close to the desk with my computer, I also
get food or drinks from there during the meetings more often."
(R20)
"For me personally, I am more likely to do another task that does
not require the computer like managing my to do list, writing
down notes, cleaning up my office and desk, eating etc." (R171)

RQ3: THE CONSEQUENCES OF
MULTITASKING

Finally, we present our findings on the consequences of multitasking during remote meetings. Although multitasking is typically
associated with negative outcomes such as decreased task performance [17, 47], difficulties in decision making [60] and negative
affect [5, 68], our participates report that in-meeting multitasking
leads to both positive and negative outcomes.

7.1

Positive Outcomes

Multitasking may help boost productivity. First, multiple participants (15 %) mentioned that multitasking helps boost their productivity, which echos prior works on the benefits of multitasking
on efficiency [19, 39, 54]. Given that, under current remote work
settings, there are many more remote meetings compared to the
pre-COVID-19 period, people explained how multitasking helps
them to get work done. Here’s a representative response,
"There are some benefits to multi-tasking. I’ve been able to get
more work done. I’ve been less frustrated by meetings that weren’t
very useful to me. I haven’t made any significant mess ups in a
meeting yet when I’ve done it." (R330)
Multitasking is at its most productive when workers understand
that their own and others’ attention in a meeting is a spectrum
about which they can make active meeting choices [36].
"I find myself multi-tasking in meetings that do not require my
attention, but not in meetings that do. In some ways, I may
be more productive given the ease of multi-tasking in remote
meetings." (R508)
People also mentioned the positive experience with meetingrelated multitasking behavior, such as note taking and searching
for information, e.g.,
"The type of multitasking that I feel it has a positive impact on my
productivity is when I am taking notes during a meeting or when
I am navigating the internet to find some relevant information
that is being discuss in the meeting." (R668)

7.2

Negative Outcomes

Multitasking leads to loss of attention/engagement. Nevertheless, remote meeting multitasking does cause negative consequences. Among them, the most frequently (36 %) mentioned negative aspect is loss of attention/engagement, where people lose
track of the meeting content (which sometimes is important) due
to multitasking activities, as demonstrated by the following cases,
"Its easy to get distracted by multitasking and miss something
in the meeting." (R2)
"I have to channel my concentration on 1 primary task – whether
that be the meeting itself or the side work I’m doing while listening in." (R346)
"If you leave the meeting window to open a deck or other files,
it’s hard to get back to the meeting window. Same with chats - if
you leave the meeting window to send chats to other people, it’s
hard to get back to the meeting." (R344)

Conference’17, July 2017, Washington, DC, USA

These observations are well-aligned with previous conclusions
on the impact of multitasking behavior on people’s attention and
task resumption [4, 5].
Multitasking leads to mental fatigue. Moreover, we find that
remote meeting multitasking behavior does have an impact on
well-being: some participants reported that they feel tired after
multitasking during remote meetings.
"I tire a bit more with so many meetings and multitasking." (R72)
Multitasking can be disrespectful. One final downside of
multitasking is that it has been sometimes regarded as an inappropriate behavior during remote meetings. Some participants explicitly associate multitasking with being impolite.
"I tend to do it less while on video, so they can’t tell I’m being
rude." (R173)
"I rarely multitask when on camera–it seems rude." (R673)
"People are becoming a bit more brazen; it’s sometimes unbelievably clear that they aren’t paying close attention to the discussion
and with the current WFH situation it’s hard not to notice eyes
straying, backlight (windows) changing, etc. It adds another dimension of rudeness but I also do it to others, sometimes not
realizing when I follow the stray notification." (R343)
“I have gotten caught off guard a few times though. Someone
will ask me a question and I’ll have to ask them to repeat it. They
don’t seem upset, but I’m still embarrassed/ashamed when it
happens. This is mostly due to the fact that I know I have slightly
negative feelings toward other people when they get caught in
the same situation, or when they ask a question that had been
asked and answered recently. I don’t want to be one of those
people or be thought of as one of those people who is not paying
attention." (R330)

8

BEST-PRACTICE GUIDELINES FOR
REMOTE MEETINGS

Remote meetings have become the primary way that people connect
and collaborate while working from home. As the number and
duration of remote meetings has increased, people appear to have
been left with less time to focus on their work and thus have gotten
into the habit of multitasking to catch up. This draws participants’
attention away from the meeting, and can lead to mental fatigue and
disrespectful behaviors. Based on our findings, we propose several
practical remote meeting best practices that meeting organizers
can use to help people attending the meeting actually attend to the
meeting. We note, however, the importance to consider specific
worker and corporation contexts when applying these guidelines.
Avoid important meetings in the morning. As demonstrated
by Fig. 2, people still adhere to a similar “double peak” daily work
rhythm [46] as they did in pre-COVID, co-located work settings.
Through our regression analysis, we find that email multitasking
behavior occurs most often in the morning, which coincides with
the fact that email actions peak in the morning. Prior evidence
also suggests that people are most focused in mid afternoons [42].
Therefore, our results suggest that meeting organizers might avoid
scheduling important meetings in the morning, when it is harder
for people to concentrate. However, multitasking in the morning is
not always bad, as confirmed by our diary study participants (e.g.,

Cao et al.

“balancing home and work”). In fact, scheduling light-weight meetings in the morning may actually help people smoothly transition
from “home” to “work” mode under remote work settings [33, 66].
Reduce the number of unnecessary meetings. Many participants stated that they multitasked because they found that the
content of some meetings did not apply to them, especially for
information sharing and daily stand up meetings. In the telemetry data analysis, we also found that there was much more email
multitasking in recurring and scheduled meetings compared to ad
hoc meetings. Given there are so many meetings people now need
to attend, meeting organizers should reconsider the necessity of
numerous meetings, or the frequency of such meetings, so as to
help people better focus. The organizers may also consider sharing
information asynchronously. For example, sending out a recording
of a presentation for attendees to watch on their own, and then
only use the meeting for discussion.
Shorten meeting duration and insert breaks. In our telemetry analysis, we found that longer meetings are associated with
more multitasking behavior, which is also verified by the qualitative
evidence. As suggested by prior literature, humans have an upper
time limit where they can fully engage and pay attention [41], thus
we suggest that meeting organizers should shorten the duration of
meetings, or insert breaks when meetings have to run long.
Encourage active contribution from the appropriate number of attendees. Finally, many participants mentioned that they
multitasked because they don’t have anything to actively contribute
to the meeting discussion. They generally muted themselves and
turned off their video in such scenarios. If organizers want the
full attention of participants in an important meeting, they should
encourage participants to actively engage through stimulating interactions, especially if it is a large meeting with a variety of attendees.
For meetings where active engagement is particularly important,
then the invitee list should be as small as necessary to achieve the
right level of engagement from attendees.
Allow space for positive multitasking. Our findings suggest
that multitasking can be positive under remote environment. Therefore, meeting organizers could consider creating personalized meeting agenda so that people are aware of the timing when relevant
agenda items come up. Organizers can also implement a convention where video-on implies full attention, and video-off signals
multitasking.

9

DESIGN IMPLICATIONS FOR BETTER
SUPPORT OF REMOTE MEETINGS

We have seen that multitasking in remote meetings is a complex
behavior, with both positive and negative aspects. It can help people
be more productive, but may also reduce attention, increase fatigue,
and appear impolite. While culturally the term multitasking may
have a negative connotation [52], our study adds to a growing body
of work that reevaluates differential attention and multitasking
in remote work contexts [36] and for users of all abilities [21].
Based on our findings, we argue that given the complext nature
of remote meeting multitasking, it is important to encourage its
positive aspects while reducing its negative implications. In this
section we discuss several ways productivity tools might do this.

Large Scale Analysis of Multitasking Behavior
During Remote Meetings

Support a ‘focus mode’ for remote meetings. Our analysis
shows that pop-ups in current software interfaces during remote
meetings distract people from the meeting itself. To alleviate such
distractions, we envision future collaboration platforms having
a remote meeting ‘focus mode’. After people choose to enter the
mode (e.g., for a very important meeting), the tool could block all
standard pop-up messages, emails, etc., so as to help them concentrate on the meeting itself. The focus mode could also employ a
multitasking alert feature. People could give permission to the app
to track their behavior in other applications or even their other devices. For non-meeting focused behavior (speaking, screensharing,
in meeting parallel chat, etc.), the app could alert people about their
multitasking and reflect back the reason (e.g., not being able to absorb all of the information within the meeting). As such, the feature
could help people engage in the meeting and avoid unintended loss
of attention.
Support other types of engagement during remote meetings. Some positive multitasking fits the meeting purpose, but
technically requires moving outside the meeting window which
may increase the risk of being distracted from the meeting. For
instance, people often need to work outside the actual meeting window or platform to take notes or work on files, switching back and
forth between this work and the meeting. The ability to have more
windows, split views, or even a more broadly-defined meeting space
could not only reduce the potential for distraction but also improve
the shared use of these resources. Given the various reasons for
remote meeting multitasking, it is also important to not arbitrarily
consider it unacceptable. Meetings could enable attendance along a
scale of high to low engagement, to help set attendees’ expectations
and more closely match actual behaviour [36].
Help people decide which meetings to attend. Our study
suggests that over-multitasking or negative multitasking is associated with the increasing number of meetings during remote work.
Apart from organizational leaders actively reducing the number of
meetings, future remote meeting tools could develop a feature for
people to self-rank the importance of each meeting, or recommend
an importance level assigned to each meeting for each individual based on meeting characteristics (e.g., content, size, attendees,
etc.), and add the importance level of each meeting on the person’s
calendar apps and video conferencing platforms. As such, people
will have a better idea for each day which meeting is important
and when they should pay special attention in order to not miss
key information (thus avoiding multitasking). For less important
meetings, the system could recommend ways to catch-up later,
alternative ways to attend, or help notify the meeting organizer.
Help people skip some parts of the meeting. As suggested
by our findings, even within the same meeting, certain parts of
the meeting may not be so important as other parts for a specific
attendee: the attendee may only be interested in a particular section, and works on other things except for that section. If meetings
have agendas, one solution would be to for organizers and attendees to flag expected attention per item, and add increasing and
decreasing visible attention when relevant. Future tools can also
help better support personalized meeting content importance tracking for attendees. For instance, the system could make use of real
time transcriptions of meeting and compare the topic similarity to
those that the attendee might be interested in.

Conference’17, July 2017, Washington, DC, USA

10

LIMITATIONS AND GENERALIZABILITY

While our findings build on rich telemetry and diary study data to
extend what was previously know about multitasking in remote
meetings, it is important to consider them in the context of several
limitations. For one, the data are drawn from one global information
technology company (and the telemetry data focus on US workers only), with most participants being information workers. As
a result, our findings may not generalize to other worker types
under remote settings, or to other cultures. Further, the analyzed
data were collected during the COVID-19 pandemic era, but we
were not able to distinguish remote work effects from COVID-19
effects (e.g., the impact of remote working from home on people’s
mental wellbeing) on multitasking behavior. Additionally, while
telemetry data is valuable in providing a large-scale, realistic picture of behavior, it does not provide the motivation motivating that
behavior [25], we are not able to distinguish whether the email
and file actions we observed were related to the meeting or not. It
is likely that some of the positive multitasking observations may
be false positives. Finally, the current diary study does not cover
every aspect with regard to remote meeting multitasking, which
can be addressed in future work, e.g., references to side-channels,
such as Whatsapp, Facebook or other apps that cannot be instrumented through telemetry data analysis and people’s perception
of multitasking. Nevertheless, we believe that this work presents
the most comprehensive analysis of remote meeting multitasking
behavior currently available, and could extend to scenarios beyond
the narrow-sense of workspace meetings (e.g., real-time distance
education that leverages remote meeting tools [13]). We leave the
above mentioned limitations as future work.

11

CONCLUSION

In this paper, we presented a large-scale and mixed-methods study
of multitasking behavior during remote meetings. We analyzed
a large-scale telemetry dataset and conducted a longitudinal diary study during COVID-19 period. Our analysis leads to practical
guidelines for remote meeting attendees and design implications
for productivity tools, both of which can improve remote meeting
experiences. Our results point to the importance of multitasking
in the consideration of remote meetings, both with respect to their
social and technical components. On the one hand, how remote
meetings are scheduled and structured are significantly associated
with when and to what extent people divide their attentions. On
the other hand, multitasking could imply both positive and negative outcomes for individual worker and work group. More future
research efforts are needed to address remote meeting experience
as it becomes mainstream, and our work provides a foundational
and timely understanding of such.

REFERENCES
[1] Adam D’Angelo. [n.d.]. Remote First at Quora. https://www.quora.com/q/quora/
Remote-First-at-Quora
[2] Rachel F. Adler and Raquel Benbunan-Fich. 2013. Self-Interruptions in Discretionary Multitasking. Comput. Hum. Behav. 29, 4 (July 2013), 1441–1449.
https://doi.org/10.1016/j.chb.2013.01.040
[3] Tammy D Allen, Timothy D Golden, and Kristen M Shockley. 2015. How effective
is telecommuting? Assessing the status of our scientific findings. Psychological
Science in the Public Interest 16, 2 (2015), 40–68.
[4] Erik Altmann and J. Trafton. 2004. Task Interruption: Resumption Lag and the
Role of Cues. Proceedings of the 26th Annual Conference of the Cognitive Science

Conference’17, July 2017, Washington, DC, USA

Society (07 2004).
[5] B. Bailey and J. Konstan. 2006. On the need for attention-aware systems: Measuring effects of interruption on task performance, error rate, and affective state.
Comput. Hum. Behav. 22 (2006), 685–708.
[6] Louise Barkhuus. 2005. "Bring Your Own Laptop Unless You Want to Follow the
Lecture": Alternative Communication in the Classroom. In Proceedings of the 2005
International ACM SIGGROUP Conference on Supporting Group Work (Sanibel
Island, Florida, USA) (GROUP ’05). Association for Computing Machinery, New
York, NY, USA, 140–143. https://doi.org/10.1145/1099203.1099230
[7] Nicholas Bloom, James Liang, John Roberts, and Zhichun Jenny Ying. 2015. Does
working from home work? Evidence from a Chinese experiment. The Quarterly
Journal of Economics 130, 1 (2015), 165–218.
[8] Maria Brandimonte, Gilles O Einstein, and Mark A McDaniel. 1996. Prospective
memory : theory and applications. Mahwah, N.J. : L. Erlbaum.
[9] Erik Brynjolfsson, John J Horton, Adam Ozimek, Daniel Rock, Garima Sharma,
and Hong-Yi TuYe. 2020. Covid-19 and remote work: An early look at US data.
Technical Report. National Bureau of Economic Research.
[10] Hancheng Cao, Zhilong Chen, Mengjie Cheng, Shuling Zhao, Tao Wang, and
Yong Li. 2020. You Recommend, I Buy: How and Why People Engage in Instant
Messaging Based Social Commerce. arXiv preprint arXiv:2011.00191 (2020).
[11] Hancheng Cao, Zhilong Chen, Fengli Xu, Tao Wang, Yujian Xu, Lianglun Zhang,
and Yong Li. 2020. When Your Friends Become Sellers: An Empirical Study of
Social Commerce Site Beidian. In Proceedings of the International AAAI Conference
on Web and Social Media, Vol. 14. 83–94.
[12] Hancheng Cao, Vivian Yang, Victor Chen, Yu Jin Lee, Lydia Stone, N’godjigui Junior Diarrassouba, Mark E. Whiting, and Michael S. Bernstein. 2020. My Team
Will Go On: Differentiating High and Low Viability Teams through Team Interaction. Proc. ACM Hum.-Comput. Interact. 4, CSCW3, Article 230 (2020), 27 pages.
https://doi.org/10.1145/3432929
[13] Zhilong Chen, Hancheng Cao, Yuting Deng, Xuan Gao, Jinghua Piao, Fengli Xu,
Yu Zhang, and Yong Li. 2020. A Large-Scale Mixed-Methods Analysis of Live
Streaming Based Remote Education Experience in Chinese Colleges During the
COVID-19 Pandemic. arXiv preprint arXiv:2010.01662 (2020).
[14] Zhilong Chen, Hancheng Cao, Fengli Xu, Mengjie Cheng, Tao Wang, and Yong
Li. 2020. Understanding the Role of Intermediaries in Online Social E-commerce:
An Exploratory Study of Beidian. Proceedings of the ACM on Human-Computer
Interaction 4, CSCW2 (2020), 1–24.
[15] Juliet Corbin and Anselm Strauss. 2014. Basics of qualitative research: Techniques
and procedures for developing grounded theory. Sage publications.
[16] Juliet M Corbin and Anselm Strauss. 1990. Grounded theory research: Procedures,
canons, and evaluative criteria. Qualitative sociology 13, 1 (1990), 3–21.
[17] Edward Cutrell, Mary Czerwinski, and Eric Horvitz. 2000. Notification, Disruption, and Memory: Effects of Messaging Interruptions on Memory and Performance. (12 2000).
[18] Mary Czerwinski, Eric Horvitz, and Susan Wilhite. 2004. A diary study of task
switching and interruptions. In Proceedings of the SIGCHI conference on Human
factors in computing systems. 175–182.
[19] Laura Dabbish and Robert Kraut. 2003. Coordinating Communication: Awareness
Displays and Interruption. 786–787. https://doi.org/10.1145/765891.765991
[20] Laura Dabbish, Gloria Mark, and Víctor M. González. 2011. Why Do i Keep
Interrupting Myself? Environment, Habit and Self-Interruption. In Proceedings of
the SIGCHI Conference on Human Factors in Computing Systems (Vancouver, BC,
Canada) (CHI ’11). Association for Computing Machinery, New York, NY, USA,
3127–3130. https://doi.org/10.1145/1978942.1979405
[21] Maitraye Das, John Tang, Kathryn E. Ringland, and Anne Marie Piper. 2021.
Towards Accessible Remote Work: Understanding the Practices of Neurodivergent Professionals in Working from Home. Proceedings of the ACM on HumanComputer Interaction (CSCW 2021) (Oct. 2021).
[22] Evan DeFilippis, Stephen Michael Impink, Madison Singell, Jeffrey T Polzer,
and Raffaella Sadun. 2020. Collaborating during coronavirus: The impact of
COVID-19 on the nature of work. NBER Working Paper w27612 (2020).
[23] Sante Delle-Vergini. 2018. Missing in Action: Implications for the management
of employees working from home in the Philippines’ BPO industry. (2018).
[24] Jonathan I Dingel and Brent Neiman. 2020. How many jobs can be done at home?
Technical Report. National Bureau of Economic Research.
[25] Susan Dumais, Robin Jeffries, Daniel M Russell, Diane Tang, and Jaime Teevan.
2014. Understanding user behavior through log data and analysis. In Ways of
Knowing in HCI. Springer, 349–372.
[26] Elias Eriksson and Arpine Petrosian. 2020. Remote Work-Transitioning to Remote
Work in Times of Crisis.
[27] Victor M González and Gloria Mark. 2004. " Constant, constant, multi-tasking
craziness" managing multiple working spheres. In Proceedings of the SIGCHI
conference on Human factors in computing systems. 113–120.
[28] Victor M. González and Gloria Mark. 2004. "Constant, Constant, Multi-Tasking
Craziness": Managing Multiple Working Spheres. In Proceedings of the SIGCHI
Conference on Human Factors in Computing Systems (Vienna, Austria) (CHI ’04).
Association for Computing Machinery, New York, NY, USA, 113–120. https:
//doi.org/10.1145/985692.985707

Cao et al.

[29] Helen Ai He and Elaine M Huang. 2014. A qualitative study of workplace intercultural communication tensions in dyadic face-to-face and computer-mediated
interactions. In Proceedings of the 2014 conference on Designing interactive systems.
415–424.
[30] H. Hembrooke and G. Gay. 2003. The laptop and the lecture: The effects of
multitasking in learning environments. Journal of Computing in Higher Education
15 (2003), 46–64.
[31] Shamsi T. Iqbal, Jonathan Grudin, and Eric Horvitz. 2011. Peripheral Computing
during Presentations: Perspectives on Costs and Preferences. In Proceedings of
the SIGCHI Conference on Human Factors in Computing Systems (Vancouver, BC,
Canada) (CHI ’11). Association for Computing Machinery, New York, NY, USA,
891–894. https://doi.org/10.1145/1978942.1979073
[32] Shamsi T Iqbal and Eric Horvitz. 2007. Disruption and recovery of computing
tasks: field study, analysis, and directions. In Proceedings of the SIGCHI conference
on Human factors in computing systems. 677–686.
[33] Jon M Jachimowicz, Julia Lee Cunningham, Bradley R Staats, Francesca Gino, and
Jochen I Menges. 2020. Between home and work: commuting as an opportunity
for role transitions. Organization Science (2020).
[34] Jennifer Christie. [n.d.]. Keeping our employees and partners safe during #coronavirus. https://blog.twitter.com/en_us/topics/company/2020/keeping-ouremployees-and-partners-safe-during-coronavirus.html
[35] Amy K Karlson, Shamsi T Iqbal, Brian Meyers, Gonzalo Ramos, Kathy Lee, and
John C Tang. 2010. Mobile taskflow in context: a screenshot study of smartphone
usage. In Proceedings of the SIGCHI Conference on Human Factors in Computing
Systems. 2009–2018.
[36] Anastasia Kuzminykh and Sean Rintel. 2020. Low Engagement As a Deliberate
Practice of Remote Participants in Video Meetings. In Extended Abstracts of the
2020 CHI Conference on Human Factors in Computing Systems. 1–9.
[37] Katharina Lix, Amir Goldberg, Sameer Srivastava, and Melissa A Valentine. 2020.
Timing Differences: Discursive Diversity and Team Performance. SocArXiv. June
12 (2020).
[38] Kevin P Madore, Anna M Khazenzon, Cameron W Backes, Jiefeng Jiang, Melina R
Uncapher, Anthony M Norcia, and Anthony D Wagner. 2020. Memory failure
predicted by attention lapsing and media multitasking. Nature 587, 7832 (2020),
87–91.
[39] Paul P. Maglio and Christopher S. Campbell. 2000. Tradeoffs in Displaying
Peripheral Information. In Proceedings of the SIGCHI Conference on Human Factors
in Computing Systems (The Hague, The Netherlands) (CHI ’00). Association for
Computing Machinery, New York, NY, USA, 241–248. https://doi.org/10.1145/
332040.332438
[40] Gloria Mark, Victor M. Gonzalez, and Justin Harris. 2005. No Task Left behind? Examining the Nature of Fragmented Work. In Proceedings of the SIGCHI
Conference on Human Factors in Computing Systems (Portland, Oregon, USA)
(CHI ’05). Association for Computing Machinery, New York, NY, USA, 321–330.
https://doi.org/10.1145/1054972.1055017
[41] Gloria Mark, Shamsi Iqbal, and Mary Czerwinski. 2017. How blocking distractions
affects workplace focus and productivity. In Proceedings of the 2017 ACM International Joint Conference on Pervasive and Ubiquitous Computing and Proceedings of
the 2017 ACM International Symposium on Wearable Computers. 928–934.
[42] Gloria Mark, Shamsi T Iqbal, Mary Czerwinski, and Paul Johns. 2014. Bored
mondays and focused afternoons: the rhythm of attention and online activity
in the workplace. In Proceedings of the SIGCHI Conference on Human Factors in
Computing Systems. 3025–3034.
[43] Gloria Mark, Shamsi T. Iqbal, Mary Czerwinski, Paul Johns, and Akane Sano.
2016. Neurotics Can’t Focus: An <i>in Situ</i> Study of Online Multitasking
in the Workplace. In Proceedings of the 2016 CHI Conference on Human Factors
in Computing Systems (San Jose, California, USA) (CHI ’16). Association for
Computing Machinery, New York, NY, USA, 1739–1744. https://doi.org/10.1145/
2858036.2858202
[44] Gloria Mark, Yiran Wang, and Melissa Niiya. 2014. Stress and Multitasking in
Everyday College Life: An Empirical Study of Online Activity. In Proceedings of
the SIGCHI Conference on Human Factors in Computing Systems (Toronto, Ontario,
Canada) (CHI ’14). Association for Computing Machinery, New York, NY, USA,
41–50. https://doi.org/10.1145/2556288.2557361
[45] Jennifer Marlow, Eveline van Everdingen, and Daniel Avrahami. 2016. Taking
Notes or Playing Games? Understanding Multitasking in Video Communication. In Proceedings of the 19th ACM Conference on Computer-Supported Cooperative Work and Social Computing (San Francisco, California, USA) (CSCW
’16). Association for Computing Machinery, New York, NY, USA, 1726–1737.
https://doi.org/10.1145/2818048.2819975
[46] Daniel McDuff, Eunice Jun, Kael Rowan, and Mary Czerwinski. 2019. Longitudinal Observational Evidence of the Impact of Emotion Regulation Strategies on
Affective Expression. IEEE Transactions on Affective Computing (2019).
[47] Christopher A. Monk, Deborah A. Boehm-Davis, and J. Gregory Trafton.
2002. The Attentional Costs of Interrupting Task Performance at Various
Stages. Proceedings of the Human Factors and Ergonomics Society Annual Meeting 46, 22 (2002), 1824–1828. https://doi.org/10.1177/154193120204602210
arXiv:https://doi.org/10.1177/154193120204602210

Large Scale Analysis of Multitasking Behavior
During Remote Meetings

[48] Stephen L Morgan and Christopher Winship. 2015. Counterfactuals and causal
inference. Cambridge University Press.
[49] Brid O’Conaill and David Frohlich. 1995. Timespace in the Workplace: Dealing with Interruptions. Conference on Human Factors in Computing Systems Proceedings 2, 262–263. https://doi.org/10.1145/223355.223665
[50] Gary M Olson and Judith S Olson. 2000. Distance matters. Human–computer
interaction 15, 2-3 (2000), 139–178.
[51] Sanghoo Park, Sangmi Kim, and Seungmi Han. 2014. Analysis of multitasking in
the context of using multiple mobile devices: a qualitative research. In Proceedings
of HCI Korea. 404–411.
[52] Andrew K Przybylski and Netta Weinstein. 2013. Can you connect with me now?
How the presence of mobile communication technology influences face-to-face
conversation quality. Journal of Social and Personal Relationships 30, 3 (2013),
237–246.
[53] Daniela Retelny, Sébastien Robaszkiewicz, Alexandra To, Walter S Lasecki, Jay
Patel, Negar Rahmati, Tulsee Doshi, Melissa Valentine, and Michael S Bernstein.
2014. Expert crowdsourcing with flash teams. In Proceedings of the 27th annual
ACM symposium on User interface software and technology. 75–85.
[54] Charles Rich and Candace Sidner. 1999. COLLAGEN: A collaboration manager
for software interface agents. User Modeling and User-Adapted Interaction 8 (03
1999). https://doi.org/10.1023/A:1008204020038
[55] John Rieman. 1993. The diary study: a workplace-oriented research tool to guide
laboratory efforts. In Proceedings of the INTERACT’93 and CHI’93 conference on
Human factors in computing systems. 321–326.
[56] Sean Rintel, Priscilla Wong, Advait Sarkar, and Abigail Sellen. 2020. Methodology
and Participation for 2020 Diary Study of Microsoft Employees Experiences in
Remote Meetings During COVID-19. Technical Report 2020-10-FOW-SIM1. Microsoft. https://www.microsoft.com/en-us/research/publication/methodologyand-participation-for-2020-diary-study-of-microsoft-employees-experiencesin-remote-meetings-during-covid-19/
[57] Joshua S. Rubinstein, David Meyer, and Jeffrey E. Evans. 2001. Executive Control
of Cognitive Processes in Task Switching. 27 (Sept 2001), 763–97. https://doi.
org/10.1037/0096-1523.27.4.763
[58] Skipper Seabold and Josef Perktold. 2010. statsmodels: Econometric and statistical
modeling with python. In 9th Python in Science Conference.
[59] Abigail Sellen and Richard Harper. 1997. Paper as an analytic resource for the
design of new technologies. In Proceedings of the ACM SIGCHI Conference on
Human factors in computing systems. 319–326.
[60] Cheri Speier, Joseph S. Valacich, and Iris Vessey. 1999. The Influence of Task
Interruption on Individual Decision Making: An Information Overload Perspective. Decision Sciences 30, 2 (1999), 337–360. https://doi.org/10.1111/j.15405915.1999.tb01613.x arXiv:https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.15405915.1999.tb01613.x
[61] Jonathan B Spira and Joshua B Feintuch. 2005. The cost of not paying attention:
How interruptions impact knowledge worker productivity. Report from Basex
(2005).
[62] Minhyang (Mia) Suh, Frank Bentley, and Danielle Lottridge. 2018. "It’s Kind of
Boring Looking at Just the Face": How Teens Multitask During Mobile Videochat.
Proc. ACM Hum.-Comput. Interact. 2, CSCW, Article 167 (Nov. 2018), 23 pages.
https://doi.org/10.1145/3274436
[63] Melissa A Valentine, Daniela Retelny, Alexandra To, Negar Rahmati, Tulsee Doshi,
and Michael S Bernstein. 2017. Flash organizations: Crowdsourcing complex
work by structuring crowds as organizations. In Proceedings of the 2017 CHI
conference on human factors in computing systems. 3523–3537.
[64] Mark E Whiting, Allie Blaising, Chloe Barreau, Laura Fiuza, Nik Marda, Melissa
Valentine, and Michael S Bernstein. 2019. Did It Have To End This Way? Understanding the Consistency of Team Fracture. Proceedings of the ACM on HumanComputer Interaction 3, CSCW (2019), 1–23.
[65] Christopher D. Wickens. 2008. Multiple Resources and Mental Workload. Human Factors 50, 3 (2008), 449–455. https://doi.org/10.1518/001872008X288394
arXiv:https://doi.org/10.1518/001872008X288394
[66] Alex C Williams, Harmanpreet Kaur, Gloria Mark, Anne Loomis Thompson,
Shamsi T Iqbal, and Jaime Teevan. 2018. Supporting workplace detachment and
reattachment with conversational intelligence. In Proceedings of the 2018 CHI
Conference on Human Factors in Computing Systems. 1–13.
[67] Longqi Yang, Sonia Jaffe, David Holtz, Siddharth Suri, Shilpi Sinha, Jeffrey Weston,
Connor Joyce, Neha Shah, Kevin Sherman, CJ Lee, et al. 2020. How Work From
Home Affects Collaboration: A Large-Scale Study of Information Workers in a
Natural Experiment During COVID-19. arXiv preprint arXiv:2007.15584 (2020).
[68] Fred Zijlstra, Robert Roe, Anna Leonora, and Irene Krediet. 1999. Temporal
Factors in Mental Work: Effects of Interrupted Activities. Journal of Occupational
and Organizational Psychology 72 (06 1999), 163–186. https://doi.org/10.1348/
096317999166581

Conference’17, July 2017, Washington, DC, USA

A

ALTERNATIVE REGRESSION ANALYSIS

To test the robustness of our regression model (Section 3.1), we
conducted an alternative analysis using Generalized Linear Mixed
Effects Models [58]. Specifically, we estimated random intercepts
for workers and approximated the posterior using variational Bayes.
The alternative results are shown in Table. 2, and they are qualitatively similar to those we present in our main analysis.
Effect
Post. Mean Post. SD
Day:Monday
0.2345
0.0308
Day:Tuesday
0.3154
0.0277
Day:Wednesday
0.2052
0.0276
Day:Thursday
0.1940
0.0287
Type:broadcast
0.8271
0.1710
Type:recurring
0.5125
0.0191
Type:scheduled
0.4235
0.0199
Size:3
0.0591
0.0335
Size:4-5
0.2152
0.0293
Size:6-10
0.3656
0.0311
Size:>10
0.5788
0.0288
Hour:morning
0.6053
0.0186
Hour:afternoon
0.3760
0.0202
Duration:20-40 min
0.7863
0.0203
Duration:40-80 min
1.3049
0.0265
Duration:>80 min
1.9447
0.0699
Table 2: Alternative regression results with Generalized Linear Mixed Effects Models [58]. The model includes random
intercepts for workers and is approximated using variational Bayes. The results are qualitatively similar to those
of our main analysis.
