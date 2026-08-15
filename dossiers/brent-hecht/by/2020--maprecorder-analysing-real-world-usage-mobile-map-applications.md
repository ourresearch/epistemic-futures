---
title: "MapRecorder: analysing real-world usage of mobile map applications"
person: brent-hecht
attendance: unconfirmed
section: by
type: journal-article
year: 2020
date: 2020-02-12
venue: "Behaviour and Information Technology"
authors: "Gian-Luca Savino, Miriam Sturdee, Simon Rundé, Christine Lohmeier, Brent Hecht, Catia Prandi, Nuno Jardim Nunes, Johannes Schöning"
source_url: https://doi.org/10.1080/0144929x.2020.1714733
fulltext_url: https://eprints.lancs.ac.uk/id/eprint/141884/1/Maprecorder_Savino_et_al.pdf
openalex_id: W3005707614
doi: https://doi.org/10.1080/0144929x.2020.1714733
oa_status: hybrid
cited_by_count: 29
retrieved: 2026-08-13
content: full-text
notes: "Full text retrieved from the open-access PDF at https://eprints.lancs.ac.uk/id/eprint/141884/1/Maprecorder_Savino_et_al.pdf (pdftotext; PDF not stored)"
---

# MapRecorder: analysing real-world usage of mobile map applications

## Full text

The Version of Record of this manuscript has been published and is available in Behaviour &
Information Technology (12 Feb 2020) http://www.tandfonline.com/10.1080/0144929X.2020.1714733

MapRecorder: Analysing Real World Usage of Mobile Map
Applications

Authors:
Gian-Luca Savino1

Brent Hecht

University of Bremen, Bremen, Germany

Northwestern University, Evanston, Illinois, United States

gsavino@uni-bremen.de

bhecht@northwestern.edu

Miriam Sturdee

Catia Prandi

Lancaster University, Lancaster, United Kingdom

M-ITI; ARDITI, Funchal, Portugal

m.sturdee@lancaster.ac.uk

catia.prandi@m-iti.org

Simon Rundé

Nuno Jardim Nunes

University of Bremen, Bremen, Germany

M-ITI; ARDITI, Funchal, Portugal

srunde@uni-bremen.de

nunojnunes@me.com

Christine Lohmeier

Johannes Schöning

Communication, University of Salzburg, Salzburg, Austria

University of Bremen, Bremen, Germany

christine.lohmeier@sbg.ac.at

schoening@uni-bremen.de

1 Corresponding author

MapRecorder: Analysing Real World Usage of Mobile Map Applications
Millions of people use mobile map applications like Google Maps on a regular basis. However, despite these applications’ ubiquity,
the literature contains very little information about how these applications are used in the real world. As such, many researchers
and practitioners seeking to improve mobile map applications may not be able to identify important challenges and may miss major
opportunities for innovation. To address this paucity of usage information, we collected and analysed data during unsupervised usage
of Google Maps by replacing the standard application with a wrapped version called MapRecorder. In two studies we recorded data
from locals and tourists using our application and collected over 580 minutes of actual application usage from 34 users, spanning
555 unique sessions. We identify typical usage scenarios, observe a large amount of map exploration, and elucidate generalisable
interaction patterns.

1

INTRODUCTION & MOTIVATION

Mobile map applications like Google Maps are extremely popular. For instance, the annual ComScore report on application
usage in the United States indicates that Google Maps is the fifth-most-used mobile application [15]. Other studies
have found Google Maps to be the fourth-most-used application in terms of total usage time [6]. And while Google
Maps is the most widely used, other mobile map applications like Apple Maps, Waze or OpenStreetMap are popular
alternatives featuring similar user interfaces and functionality. However, while we know that mobile map applications
are used quite often, we know very little about how they are used. For instance, what is the most prominent action users
take within these applications? Are there reoccurring interaction patterns? How are they making use of the search
functionality? Do different user groups show different kinds of behaviour?
Usage data from commercial providers is not publicly available, and this situation is likely to persist owing to the
extensive competitive and privacy concerns associated with releasing this type of information.
Outside of the mobile map space, HCI studies that examine foundational application usage behaviour have received
extensive attention thanks to the research and design guidance they afford. These studies help not only to understand
general smartphone and application usage [6, 18] but shed light on specific domains like information search [8, 9, 20]
and notifications [33]. This paper seeks to extend the benefits of this literature to the important and prominent domain
of mobile map applications. To do so, we take inspiration from Carrascal and Church [8] who used an in-situ approach
to investigate mobile search application behaviour from 18 participants by creating an application which acted as a
“wrapper” for a popular search engine on Android. We developed such a “wrapper” application for Google Maps called
MapRecorder which “wraps” the Google Maps mobile website. This allows researchers to capture rich behavioural logs
while affording a very similar experience to the standard application. We performed two separate studies. The first
study took place in Bremen, Germany and was conducted with 28 local participants who used MapRecorder for four
weeks. We captured 483 minutes of interaction with MapRecorder across 443 sessions. The second study took place
in Madeira, Portugal, and was conducted with 6 cruise-ship tourists (non-locals) who used MapRecorder for one day.
We captured 97 minutes of interaction with MapRecorder across 112 sessions. We analysed usage across the four main
interaction states of Google Maps: Search, Place, Direction and Map-View Manipulation.
Our main finding is the prevalence of exploratory behaviour in the form of panning and zooming, supporting the
notion of “user-as-explorer” [3, 17] in mobile map applications. Indeed, this exploratory behaviour made up more than
60% of users usage time with MapRecorder in both studies. As we discuss below, this may have important implications
for the development of mobile maps which currently focus mostly on text search to enable way finding rather than
1

2
geographic exploration. As our results show, mobile maps are no longer just a means to get directions from A to B but
enable users to find information about their surroundings in an exploratory fashion.
Besides our results associated with exploration, we also noticed a number of other behaviour patterns with significant
potential design implications. For instance, we observed that search behaviours demonstrated a clear preference for
named places (e.g. a specific restaurant) rather than entity classes such as “restaurants” or other near me options. Our
findings also suggest that users exhibit similar patterns of use in order to get directions to a specific location with a
high percentage of sessions displaying specific transitions across usage states within the map application.
We are releasing our complete anonymised data set so that other researches may conduct additional analyses using
our data.
2

RELATED WORK

Descriptive studies of smartphone and smartphone-app usage behaviour have been of interest to the HCI community
since the inception of smartphones. While some studies focus more on the evaluation of general mobile phone usage
throughout users daily life (e.g. time of day of use, location of use, length of usage session) [4, 6, 9, 11, 28], others
are more concerned with more technical analyses about the time and overuse [23] as well as the impact of network
and energy usage [13, 40] of mobile phones. Further work in this area covers the categorisation of different types of
interactions [2, 18], analysis and prediction of interaction patterns [37, 38], privacy and security [14], notifications [33, 36]
or other types of usage contexts (sometimes including qualitative user data) [30].
However, few studies have engaged in descriptive analyses of within-application usage [8]. The lack of information
about how people interact with applications is due, at least in part, to the understandable hesitancy of developers to
release this information. This hesitancy is compounded by the challenges inherent in outside parties attempting to
collect organic, unbiased within-application usage information [11].
In the sections below, we review in more detail the literature that helped motivate our methodological choices while
being an external party attempting to collect high-quality within-application usage data. More importantly we provide
our motivation for collecting information about mobile map usage behaviour in the first place, as we show that studying
map usage behaviour has already been done in the era of paper maps and still holds its justification in the mobile age,
even though or rather because publicly available data in this domain is very scarce.
2.1

Collecting Usage Behaviour

User testing of novel application designs provides useful information when developing new products, but these test
cases are usually conducted in a controlled environment to discover glitches before a product is released. In comparison,
unsupervised usage data collection occurs naturally, with organic situations and outcomes, but can be difficult to
organise and collect [10, 11]. To give a widespread example of unsupervised usage data collection, commercially
provided data such as Google Analytics can provide detailed information about items such as site visits or page views,
and thus can be used to infer some details on unsupervised use – such as examining the usability of E-Commerce
sites [16].
An application-specific study which was successful in collecting unsupervised usage data was developed by Lettner
et al. [24] to examine screen-to-screen navigation within applications and identify navigation errors. This method was
able to provide the developers with a large amount of naturalistic data and some usability insights, but only works for
those applications where between-screen navigation is used, and does not collect associated data, so has limited use in
other contexts.

MapRecorder: Analysing Real World Usage of Mobile Map Applications

3

A larger data set was analysed by Böhmer et al. [6] (4125 users over 163 days) with over 22000 sessions of application
usage recorded. As with Do et al. [12], a logging application was developed and deployed so as not to interfere with
the general user experience. Data such as local time and location was collected, in addition to the time an app was
open and previous app interaction. Within this data set, Google Maps usage was collected and was shown to be the
fourth-most-used application in terms of time spent in-app, and although a peak in early evening usage suggested
peaks in user engagement, no in-app behaviour data could be collected.
In contrast to the large-scale application studies, single application usage behaviour has also generated a lot of
interest (e.g. McMillan et al. [29]). Here, the redesign and deployment of a Windows PDA game onto a new mobile
platform was investigated using in-app communication with users, as well as evaluations taken from social media sites.
As the developers, the in-app access was unbarred, and this freedom was used to gather complex data about the game
Hungry Yoshi and its users, although most researchers do not have this luxury.
An alternative to gather application usage data requires an additional program to “contain” the application in
question and run in the background while normal use occurs. The data collected by such studies is also of high quality
(in comparison to the above), and allows us to get a glimpse of what happens whilst the user is interacting with the
application. The in-situ approach used by Carrascal and Church investigated mobile search application behaviour
by creating an application which acted as a “wrapper” for a popular search engine on Android. The resulting logged
data of the application from 18 users, together with qualitative interviews and a daily on-line diary over the course of
two weeks revealed how this data can be used to enrich the mobile search experience and help users complete their
information search [8].
2.2

Map Usage

Although there is limited information about interaction with mobile map applications, the study of user engagement
with maps has already been a subject of research back in the era of paper maps. In 1987, Blades and Spencer [5] wrote a
review about some of the current research on maps designed for navigation. Despite of the importance of these maps
themselves, they acknowledged the little research that had been done on how people actually use them. Blades and
Spencer were mainly concerned with the cognitive abilities that go into using a map for way finding and the usability
of the map itself but highlight the lack of empirical studies that produce sufficient data on everyday map use to make
these analyses.
The current situation does not look different. There are only a few studies that have sought to understand how
people interact with mobile maps and these have been limited to in-situ recording, self-reporting, corpus analysis of
offline data sets, or do not produce in-app usage data. Methods such as self-reporting and taking screenshots during
normal use produced a valuable overview of issues with navigation (in particular when driving) for Google Maps [30],
but this data was limited to analysis of user behaviour and comments as a result of application usage, and did not record
the issue in real time.
Corpus analysis has proven valuable in identifying feature gaps in map applications from analysis of themes common
in catastrophic accidents [25], and can identify omissions in particular map areas. These themes also enable application
developers to generate new routing software which takes into account features such as inclement weather and improving
instruction quality, however – although there is no real-time usage data of the application to provide detailed analysis
of user behaviour, this work shows the value of studying user behaviour to identify patterns.
Of the literature reviewed, the most in depth analysis of Google Maps (or any other map application) was conducted
by Google, but as a result, only limited data was shared with the research community [35]. As developers, they had

4
unparalleled access to user data, and used their findings to improve the Google Maps experience. To collect the data,
24 participants (from four countries) were recruited from a pool of volunteers, and paid to use a version of the main
application for a period of two weeks. The data collection also included a qualitative component (as with Carrascal et
al. [8]) of telephone interviews and a debriefing session in order to understand particular usage behaviours during the
study period. With this being the first field study that investigated Google Maps usage they were able to understand
“real” goals of users which they could address in the interviews and “real” intervening factors that could be addressed
by future design changes. This highlights the benefits of collecting “real”, organic data to identify “real” problems and
characteristics of mobile map usage behaviour.
Although the previous work is the most comprehensive view of Google Maps to date, it was not a completely
unsupervised data collection, and focused on a now outdated version of the application (2007). The above paragraphs
highlight a need for current, detailed, usage data for mobile map applications from real-world usage which can only be
obtained by tracking in-app behaviours from unsupervised users. We use Google Maps in the mobile environment to
gather unsupervised usage data as it is not only the fourth-most-popular application [15], but it is the most used mobile
map application within our two samples. We follow the naturalistic application use in order to provide an in-depth
analysis of mobile map application behaviour with which we can enhance our understanding of this type of app and
suggest implications for the ongoing design and development of the navigation and exploration experience.
3

EXPERIMENTAL STUDIES

In order to answer the questions posed in the introduction this paper presents two studies. Study 1 was conducted in
Bremen, Germany with 28 local participants over the course of four weeks using our MapRecorder application. Study 2
was conducted in Madeira, Portugal with 6 tourists (non-locals) during a period of one week using the MapRecorder
application. The following section will describe both study designs and their differences.
Study 1 employed a three-stage process in order to collect mobile map application data involving a large-scale
pre-survey, the use of our “wrapper” application MapRecorder and a qualitative interview at the end. Study 2 did not
include any interviews and had a post-survey after the use of the MapRecorder application.
The details of participant recruitment, the design of MapRecorder and its functions as well as the design of the
interview are described in the following sections.
3.1

Survey & Participant Recruitment

3.1.1 Study 1 Online survey participants (n=159) were recruited via the university’s social media sites (Facebook and
Twitter), by word of mouth, and from internal advertising. Our survey comprised of five sections and covered basic
demographic data, type of smartphone, map application preference, how often the map application was used, and what
it was used for (e.g. getting directions, searching for the location of a place).
At the end of the survey, participants were invited to sign up for the user-study by downloading the MapRecorder
application. As iOS was the preferred operating system among survey participants they then received a link to download
MapRecorder from the Apple App Store and were asked to use the app for all of their mobile map-needs for the next four
weeks. Participants who signed up and completed the MapRecorder study were given a 20 Euro voucher.
159 participants completed the survey and 49 downloaded and installed the MapRecorder application and used it at
least once. To ensure a valid comparison between the two different user groups (locals and tourists) and to only count
“active” users, we filtered out non-local participants and participants with less than five sessions in the study period. In
total, 28 participants (15 male and 13 female) from the local area (within 100km from the university) between the ages

MapRecorder: Analysing Real World Usage of Mobile Map Applications

5

of 20 and 47 completed the survey and used the MapRecorder application regularly until the end of the study period
(which they were reminded of one week in advance). The data of these 28 participants was later on used in the analysis.
The consent to take part in the study and data collection was given on the splash screen of the MapRecorder application
at its first launch. After the experiment eight participants agreed to a follow up interview.
3.1.2 Study 2 Six cruise ship tourists (4 male and 2 female) between the ages of 38 and 58 were recruited on three
different days (arrival days of the cruise-ships) within the week the experiment was conducted. Since they spent only
up to a day on the island and had the cruise ship as a fixed start and end point of their visit, they made for the ideal
tourist group to approach. After they agreed to take part in the study and data collection, by signing a consent form,
they could choose a device with their preferred operating system (iOS or Android, as we were not able to determine
their preferred operating system beforehand) with the MapRecorder application already installed. They were then free
to explore the island on their own terms. The average day trip during which they used the application lasted 4 hours
and 15 minutes (sd: 86 minutes) and was mainly taking place in the capital Funchal. Upon return they handed back
the smartphone. At the end of the experiment they were asked to fill out a survey which comprised of three sections
and covered basic demographic data, map application preference, how often the map application was used, what it
was used for (e.g. getting directions, searching for the location of a place) and whether they use their map application
differently on vacation.
Our sample, usage period, and methodology are in line with other influential studies which explore similar user
behaviours and are documented at prominent HCI conferences. We ensure that we have sufficient participant numbers
to be able to make sound inferences about the data as with [1, 8, 34], and that the study period covers at least several
weeks to gain an accurate overview of what constitutes regular use [6, 12].
3.2

MapRecorder Application

In order to collect detailed, organic user behaviour data we designed and developed a mobile application called
MapRecorder. As noted above, MapRecorder is a “wrapper" application that allows users to interact with the Google
Maps website as normal and unobtrusively records usage data. We make use of the WebView class provided by the
Android and iOS SDK respectively to display the Google Maps website within our MapRecorder application. This allows
us to deliver the same user experience as the original website and at the same time record device and website data as
described in the next sections.
MapRecorder was built to run on iOS and Android devices and allows the Google Maps web-interface to be shown
in full screen. A session with a unique ID is generated from the time the application is opened until it is sent to the
background, and the resulting session data is sent to a remotely hosted server.
3.3

Logged Data & Interaction

The MapRecorder application is able to record the following information for each session (a session is defined from the
time the user opens the application until the time it is sent to the background):
• Unique session ID,
• User ID
• Device information: Phone type (e.g. iPhone 6S), resolution (e.g. 667 x 375), network connection type (e.g. GSM
or Wi-Fi)
• Start of a session (as a timestamp)

6

(a)

(b)

(c)

(d)

Fig. 1. Screenshots of the MapRecorder application for each of the states: Map-View Manipulation (a), Directions (b), Place (c) and
Search (d). Map data and image ©2019 Google.

• Duration of a session
• URL
• Timestamped interaction with the device: Compass orientation, device orientation (portrait/landscape), coordinates of touch-points on the screen, type of the touch interaction (e.g. pinch, tap), keyboard input
• Timestamped interactions with the map (e.g. change in zoom level, current centre point of the map, current
position of the user)
With this information we can subdivide the interaction with the mobile map application into four main states (see
figure 1) that also correspond to the main roles and functions of maps in general as described in [21, 22, 32]. Therefore
we subdivided the interaction with the mobile map application into Search, Place, Directions and Map-View Manipulation
corresponding to traditional GIS functionality such as answering questions like “where is...”, “what is...”, “what is the
shortest route between...” and “exploration” [21, 22]. In our framework the Search state starts from the time the user
starts typing a search query, until the time that they are redirected to a result, either by choosing one of Google’s
autocomplete results or by immediate redirection. The Place state covers the time after a user has clicked on a place
icon on the map or has been redirected to a place (e.g. a restaurant or a neighbourhood) after a search. The user leaves
the Place state when they either click on the map directly (discarding the place information) or they begin the directions
to a place, which triggers the Directions state. During the Directions state the user is able to look up routes between a
start and goal location. Users enter this state by either clicking on the directions button in the lower right corner of the
application, or requesting directions whilst in the Place state. Users remain in this state as long as they interact or view
the route or a route description, or as long as a start and destination is chosen. It is important to note that it is not
possible to use the in-app navigation within MapRecorder since the mobile web version of Google Maps does not allow
for it. On requesting navigation users get redirected to their natively installed version of Google Maps thus navigation
could not be tracked. The state of Map-View Manipulation includes all interactions that are needed to manipulate the
map view, e.g. panning, zooming and viewing the map.
3.4

Interviews

Study 1 included a semi-structured interview after the experiment with participants who have agreed to take part
in a follow-up interview. With the help of a semi-structured interview guide the participants were asked questions

MapRecorder: Analysing Real World Usage of Mobile Map Applications
67.5%

21.1%

Map-View Manipulation

0%

7
8.2%

Direction

20%

40%

60%

Place

80%

3.2%

Search

100%

Fig. 2. Distribution of map usage states averaged over all users (study 1).

about their behaviours and habits regarding their use of online maps and the patterns that became apparent through
the map recording. This semi-structured guide allowed an open approach to the participants and their statements
but also offered a focus to keep in mind while conducting the interviews. The interview guide, therefore, covered six
aspects: (1) Personal background, (2) map use, (3) perception of space, (4) linking to other services, (5) data privacy and
(6) views and opinions. The participants gave permission for the interviews to be recorded and transcribed. In total,
eight participants agreed and were interviewed for 15 minutes each via phone or Skype. The interviews were then
transcribed and evaluated by two coders. Significant statements were paraphrased, coded and analysed. Study 2 did not
include any interviews.
4

RESULTS

This section presents the results of both study 1 and study 2 separately. Study 1 presents a study with 28 participants
and focuses on how local users use mobile map applications over a period of four weeks. We exhibit that locals in our
study show a high percentage of map exploration, a tendency to search for specific places instead of entity classes and
that they utilise specific usage patterns within the application as well as other user behaviours. Study 2 on the other
hand presents a study with 6 participants that tries to understand the mobile map usage behaviour of tourists. We find
a lot of overlap in the results of both groups but cannot find indicators for usage patterns in tourist’s usage behaviour.
4.1

Study 1

The results for the preliminary survey and the MapRecorder analysis are outlined below providing a statistical overview of
the study, as well as describing the user-states identified within the Google Maps application (e.g. Map-View Manipulation,
Directions, Place and Search). This is followed by an analysis of patterns of interaction between those states and a
detailed breakdown and analysis of specific findings for each state.
4.1.1 Online Survey The survey recruited 159 participants between 19 and 65 years of age (average: 28). Ninety of the
participants were students and other occupation types ranged from journalists, to nurses and engineers. Over 61% of
respondents were from Germany (98 people) and device type was split between three types of operating systems with
the most popular being iPhone (49%) and Android (48%). The results indicate that Google Maps was the preferred map
application with nearly 80% of users favouring it over its competitors such as Apple Maps (14.5%) or Waze (around 2%)
amongst others. Within the subset of iPhone users, exactly two thirds chose Google Maps as their preferred map app,
despite the availability of the iOS native Apple Maps. We see the same trends in our smaller MapRecorder user group
which utilised the application throughout the study period.
For general map application usage, 11.3% of participants reported that they use a mobile map application every day,
39% use it multiple times in a week, 27% use it only a few times a week, 19.5% use it only a few times a month, and 3.2%
use it very infrequently. This high usage pattern is consistent with recently measured map application popularity [15].
The reasons given for using the applications were (in order of popularity): to search for a location or place (86.1%), for

Session ID

8
1_06_01

52 Seconds

1_03_04

31 Seconds

1_18_04

38 seconds

1_21_03

51 seconds

1_05_30

37 seconds

0%

20%

40%

60%
Normalized Session Length

80%

100%

Fig. 3. Example MSPD sessions. From left to right: Map-View Manipulation (Blue), Search (Green), Place (Yellow), Directions (Red).
The session ID is composed of: Study_ParticipantID_SessionID

.

walking directions (83.6%), for driving directions (71.7%), to explore the map (50.9%), or to get public transportation
directions (49.7%). Of these 159, 28 (15 male and 13 female) were local users (within 100km from the university) between
the ages of 20 and 47 (avg: 30) who used the application more than five times during the study period. These 28
participants were used for the following data analysis. 22 of them were university students from different subjects, the
remaining participants came from a variety of disciplines.
4.1.2 Overview of MapRecorder Data In total 443 sessions were recorded for 28 participants, resulting in 483 minutes
of total application usage time. This corresponds to an average of 15 (median: 11) sessions and 17 (median: 8.6) minutes
per participant over the study period. The average application session lasted 65 (median: 44) seconds (similar to the
71.56 second average found in Böhmer et al. [6]), with a range of 3–751 seconds. In the following sections we first
analyse the high-level user-data, looking at how the previously defined usage-states are distributed across users and
user-sessions. We then provide insights into the usage-patterns that can be observed between users. We also present
analyses of the four usage states individually as well as examining other user preferences and interests.
4.1.3 Overview of Interaction States When analysing the average session states (Map-View Manipulation, Directions,
Place and, Search), we found that users spent around 67.5% of the length of a session in the Map-View Manipulation (M)
state, 21.1% in the Directions (D) state, 8.2% in the Place (P) state, and the remaining 3.2% in the Search (S) state. The
average session states for all users can be seen in figure 2.
Further analysis revealed a repeating usage pattern across sessions by different users across the data set. When looking
at the user transition between states, we discovered that MSPD (Map-View Manipulation–Search–Place–Directions) is a
typical session pattern. An example of MSPD session data is shown in figure 3. The two most common sequences were
MSPD (12.1% of all sessions – 54/443) and MD (13% of all sessions – 58/443), indicating that at least 25.1% of all sessions
resulted in getting directions.
In the case of the MSPD pattern, users typically started by examining the map for a short amount of time (M). This
ranged from a few seconds (for example thinking about their search term) to 20+ seconds of proper map interaction
including touch input. They then began to enter a query into the search bar (S). After issuing the search request they
then got directed to the place that they were searching for (P). Finally, they use the directions button to bring up
directions menu for the currently active place (D), usually with their current location set as the origin.
To explore additional user interactions, we also plotted a typical MSPD session (session 30 from user #5) with
annotations including the zoom levels (automatic/user) and URL data (e.g. mode of transport) in figure 4. This is
indicative of a typical user session with Google Maps from our data. The graph shows how the automatic changes

MapRecorder: Analysing Real World Usage of Mobile Map Applications

9

(dotted lines) in zoom levels are co-located with the state transitions. Transitioning from Search to Place automatically
redirects the centre point of the map to the searched location, and then adjusts the zoom level as necessary to fit the
content of the screen. Google tries to estimate zoom levels according to the area around a certain place, or according
to the distance between two locations (e.g. automatically zooming out for places that are further apart). Users also
sometimes manually adjust these zoom levels which is indicated by the solid lines.
Figure 4 shows the following interactions: 1) After loading the map (t 0 ), the default location of Google Maps is
displayed – t 1 indicates the time at which the application locates the users’ position and automatically redirects the
centre point of the map towards them; 2) The user issuing a search query results in a place (t 2 ) and the app again
auto-zooms and pans toward that location; 3) Timestamp t 3 indicates the point at which the user touches the “directions”
button, and thus requests directions to the chosen place (resulting again in an automatic zoom and map adjustment to
match the route); 4) t 4 demonstrates a short time frame within which the user manually adjusted the zoom level; 5) The
user then changes the start and endpoint of the route, and the map automatically adjusts again (t 5 ); 6) At t 6 the user
changed the mode of transportation from car to foot, and finished the session by zooming in, probably to get a better
look at the exact route.
4.1.4 Map-View Manipulation Analysis Map-View Manipulation yields the highest average usage time of any state
during the study (67.5%). The data collected for this includes panning, zooming, “glancing” and map loading times
(the latter accounting for 7.6% of all sessions). This shows that users are generally interested in exploring the map in
an organic manner [3, 17]. MapRecorder is able to log the zoom level of a session as well as the various centre points
throughout the session from which we are able to infer panning behaviour. For these behaviours, it is difficult to
distinguish between (1) zooming/panning behaviour by the system, and (2) zooming/panning behaviour of the user, but
we are able to infer individual incidences of this behaviour (as in figure 3).
We discovered that 221 sessions out of 443 only contained the Map-View Manipulation state. In 167 of these cases,
participants simply used panning and zooming to explore the surroundings, but we were able to record an average

Zoom Level

16

t3

t4

8
4
0

t6

t2

12

t0
0%

t5
Autozoom
Zoom by User

t1
20%

40%

60%

Fig. 4. Usage-session annotated with zoom level; user 5 session 30.

80%

100%

10
Places

Destinations

Specific Search

Adress
City /
Neighborhood

Adress
City /
Neighborhood

Food

Food

Shopping

Shopping

Entertainment

Entertainment

Institutions

Search for Entity Classes

Institutions
0

15

30

45

60

Occurrences

(a)

0

15

30

45

60

Occurrences

(b)

Fig. 5. Total occurrences of places and destinations (a), Total occurrence of specific- and entity class searches (b).

of 290 touch events (user making contact with the screen) per session. Further, 54/221 sessions did not contain any
touch events and 20 of those we classify as glances, meaning that users reopened a session shortly after sending it to
the background and glanced at the map without additional interaction.
4.1.5 Directions Analysis Although users were not able to use the in-app navigation in our wrapped version of Google
Maps, Directions was the second most frequently used state (21.1%) apart from Map-View Manipulation (requesting
navigation redirected users to their own installed version of Google Maps). This shows that our participants were
using it to inquire about distances and modes of transportation between two locations. We analysed and categorised
the destinations for which users requested directions to get an overview of the types of destination that users were
interested in (figure 5 (a)). We used Google’s Places API to generate low level categories for each of the destinations and
summarised these into six top level categories: street addresses, city/neighbourhood, food, shopping, entertainment and
institutions. Almost 70% of all destinations were categorised as street addresses or city/neighbourhood as can be seen in
figure 5.
Additionally, we were able to observe the preferred mode of transportation from the URL between two locations.
Figure 6 shows that the Car routing seems to be used for most distances (median: 6.86 km), with motorised transportation
of all types being increasingly chosen for trips over longer distances.
4.1.6 Place Analysis In our data set, 8.2% of the average interaction time was related to places (figure 2). After
categorising the individual places (in the same manner as presented above) we found that most places referred to
specific street addresses and city/neighbourhood names, followed by food related places like restaurants and cafes. The
categories shopping, entertainment and institutions (in this order) were also popular places users explored (see figure 5
(a)).
We also explored the distance of places that users were interested in. The median distance from the place users were
examining compared to their current location was 8.02 kilometres. This rules out immediate walking distance as an
option (walking 8km takes an average of 100 minutes), but as a large number of the locations studied lie within 100
kilometres we consider this being in the local area.
4.1.7 Search Analysis MapRecorder is able to log the character-by-character input for search queries. This allows us
to analyse not only what participants search for, but also their general search behaviour patterns. As Search in most
cases acts simply as a means to reach the users’ goal or point of interest on the map, it accounts only for a small part of

MapRecorder: Analysing Real World Usage of Mobile Map Applications

11

Public Transport
Car
Bike
Foot
−1

10

1

10

10

2

10 3

104

Distance in kilometers

Fig. 6. Relation of distance and mode of transportation.

the session time – but this is still an integral part of the Google Maps experience – as Search was used in every second
session. In our data the search behaviour accounts for 3.2% of the total recorded time (figure 2).
To examine the semantics of search behaviour, we evaluated all 254 search queries contained within our data set
(see figure 5 (b)) and categorised them into specific search types (address, Antonio’s Pizzeria, etc.), and entity classes
(restaurant, hotel near me, etc.). We discovered our users made 220 specific searches, and 29 entity class searches,
which suggests that users typically knew the name of the place they were looking for in advance, but since our sample
was local to the area, we would expect the number of entity class searches to be low (locals have existing knowledge
of particular locations). Additional investigation also revealed that 162 of all searches made use of the autocomplete
function, meaning that Google Maps is successfully pre-empting the users’ input in more than 50% of all searches.
Finally, we take a look at the differences and connections between the Search, Place and Directions categories from
figure 5. Since we have found a very prominent usage pattern we wanted to see what conclusions we can draw with the
MSPD usage pattern in mind. Generally, all the occurrences in the categories between the states overlap rather well,
which is what we assume because of the MSPD pattern. A search term results in a place, which then gets chosen as the
destination for directions. But for some of the categories we see differences. Most interestingly, in the food category
a place does not usually result in a destination. This could be explained by the nature of how Google Maps displays
information about restaurants. Things like opening hours, the menu and reviews can be enough of a reason to look at a
place without the immediate need to look at directions for it.
4.1.8 Interviews The qualitative content analysis of the eight interviews showed three topics to be significant in using
mobile maps: (1) Additional benefits in using Google Maps, (2) triangulation of navigation options and (3) data security.
Interviewees described several features of Google Maps as particularly useful in addition to the actual navigation services.
These were real-time information on traffic and traffic jams, reviews for restaurants, bars and the option to, for example,
look at their websites and menus directly, information on public transport and exploring places as in mobile sightseeing
tours, e.g.“[I also use Google] if I’m just looking for the nearest ATM or a good restaurant. [. . . ] And then you can
immediately have a look at reviews and stuff” (ID 1_03).
While Interviewees appreciated the benefits of using Google Maps, they simultaneously expressed a mistrust of
traditional navigation systems (such as in-built car navigation software). As a consequence, they perform a triangular
navigation when planning a trip: They use traditional maps, navigation apps on mobile devices and plan the route
beforehand using a navigation web-service on a computer in order to check that the options given are optimal, e.g.“So,
in the car I have a TomTom. [. . . ] I then use Google in between because sometimes the routes are a little different or

12
64.6%

20.6%

Map-View Manipulation

0%

11.8%

Direction

20%

40%

60%

Place

80%

3.0%

Search

100%

Fig. 7. Distribution of map usage states averaged over all users (study 2).

you want to see if actually the map is the way the navigation system sends you and if it makes any sense” (ID 1_19). If
participants have local knowledge, they will also juxtapose their own past navigation experiences with information
currently received through the devices mentioned.
A third theme which transpired through the interview material is that of data security. Especially tracking services
were considered with a degree of ambivalence. On the one hand, they simplify navigation and support participants
in their everyday life. On the other hand, the participants are not certain that their data is handled in an ethical and
responsible way, e.g. “I’m really bickering about the insane support I have through such [navigation apps] and the
loss of self-control and that feeling of being remotely controlled” (ID 1_26). Interestingly, we found two re-occurring
story lines in the interview data: People had either “given up” and tried not to think about their digital traces any
longer. Or alternatively, they were engaging in some form of a resistance or “minimal data”-strategy by activating the
geolocation service as little as possible. Thinking about current and future development within the realm of mobility
brought similar results regarding a sense of ambivalence and ultimately, for some of our interview partners, raised
questions around freedom, decision making and possible mismatch of information they needed to make informed
choices and information withheld by a variety of agents.
4.1.9

Summary Our analysis outlines a combination of high and low-level findings, highlighting usage patterns that

occur repeatedly throughout the data set. We have shown a coherent model of an example session that demonstrates the
range of data that the MapRecorder application is able to collect (figure 3). We also show how the different characteristics
of each state within Google Maps are linked through the usage patterns that we identified during the study period. It is
apparent that the most used – and maybe therefore most interesting – interaction is the Map-View Manipulation. This
challenges our notions of prescriptive user behaviour in navigating with online maps. From the interviews we learn
that users intentions and behaviour are not only driven by in-app factors but are also influenced by secondary factors
like trust and security. How we can utilise these results, and what the implications of the findings are, is explored in the
discussion.
4.2

Study 2

The results of study 2 are presented in the same order as the results of study 1. We describe the survey results and the
analysis of the MapRecorder data, provide a statistical overview over the study and as before the usage data is classified
according to the usage states (M, D, P, S). Even though we compare some of the results from study 1 with the results
of study 2, it is important to keep in mind that study 1 focused on local users using the application over a four week
period whereas study 2 investigated non-locals’ behaviour over one day of application usage.
4.2.1 Survey The survey was taken by all 6 participants whose age ranged between 38 and 58 years (average: 52) with
the occupations of electrical engineer, druggist, clerk and plumber. Five respondents were from Germany and one from
Switzerland (all German speaking). Three of them have never been to Madeira before, two answered that they have

MapRecorder: Analysing Real World Usage of Mobile Map Applications
Places

Specific Search

Destinations

Culture

Culture

Area

Area

Park

Park

Food

Food

Shopping

Shopping

Church

Church
0

2

13

4

6

8

10

12

0

2

Search for Entity Classes

4

6

Occurrences

Occurrences

(a)

(b)

8

10

12

Fig. 8. Total occurrences of places and destinations (a), Total occurrence of specific- and entity class searches (b).

been on the island once and one participant was there multiple times before. The results indicate that Google Maps was
the most preferred map application with 83.3% of users favouring it over its competitors. The only alternative map
application that was mentioned by one participant was Ulmon (which is popular with tourists for its elaborate offline
functionality). For general map application usage, 33.3% of participants reported that they use a mobile map application
multiple times a day, the rest uses it only occasionally. The reasons given for using the applications were (in order of
popularity): To search for a location or place (83.3%), for walking and driving directions (66.7%), to explore the map
(33.3%), or to get public transportation directions (16.7%). Half of the participants reported that they are using their map
application differently when being on vacation. They use it more often, more detailed or they do not look up traffic
information, whereas at home they do (which is in line with our results from study 1).
4.2.2 Overview of MapRecorder Data In total, we recorded 112 sessions for 6 participants, resulting in 97 minutes of
total application usage time. Every participant produced an average of 19 (median: 19) sessions and used the application
for 16 (median: 13.1) minutes over the study period. The average application session lasted 52.29 (median: 35.32) seconds,
ranging from 1.4 - 303 seconds. In contrast to study 1 we found that users had shorter and overall more sessions. In
the following sections we analyse the high-level user-data, looking at the distribution of usage-states across users
and user-sessions. We examine the data for some of the usage-patterns that we found in study 1 (e.g. MSPD, MD) and
present analyses of the four usage states (Map-View Manipulation, Directions, Place and Search).
4.2.3 Overview of Interaction States When looking at the usage states of the tourist users we found that they spent
around 64.6% of their overall usage time in the Map-View Manipulation state, 20.6% in the Directions state, 11.8% in the
Place state, and the remaining 3.0% in the Search state. Figure 7 shows the overall average of this distribution.
In contrast to study 1 we did not find any particular usage patterns (e.g. MSPD, MD) across the data set. The most
common sequences were exclusively Map-View Manipulation (56/112) and exclusively Directions (15/112). This shows
that in half of all sessions participants just used Map-View Manipulation, similar as in study 1.
4.2.4 Map-View Manipulation Analysis With 64.6% Map-View Manipulation also yields the highest average usage time
of any state during this study. We discovered that 56 sessions out of 112 only contained the Map-View Manipulation state.
In 45 we found touch gestures suggesting that participants used panning and zooming to explore the the surroundings.
This observation leaves 11/56 sessions without any interaction, which we were not able to classify.

14

Public Transport
Car
Foot
−1

10

1
Distance in kilometers

Fig. 9. Relation of distance and mode of transportation.

4.2.5 Directions Analysis Directions was the second most frequently used state (20.6%) in our data set. We again
analysed and categorised the types of places for which users requested directions to get an overview of the top six
categories of destination within the area, which were very different from the ones we found in study 1: culture, area,
park, food, shopping, church. The destinations were more evenly distributed across those categories than in study 1 as
figure 8 (a) shows. In total 39 destinations were searched for of which 21 used information for navigation by foot, 17 by
car and 1 by public transport. Figure 9 shows that participants inquired mainly about very close distances (median:
0.378 km) to be reached by foot. For transportation by car the median distance was 1.74 km. This can be explained by
both the size of the island (76,15 km2 ) and the short time they spent there (less than a full day).
4.2.6 Place Analysis 11.8% of the average interaction time was related to places (figure 7).The places participants were
interested in all relate to sightseeing, food or shopping and were located quite close to the participants location. As
Funchal, the capital of Madeira is quite small and cruise ship tourists usually spend the day close to the ship we expected
tourists to not travel too far from there. This was confirmed by our data as we found a median distance of 490 meters
between the users current location and the place on the map they were interested in.
4.2.7 Search Analysis The search behaviour accounts for 3.0% of the total recorded usage time (figure 7) which is made
up of 19 searches in total (a relatively low number compared to study 1). We discovered that of these 19 search queries
our users made 16 specific-, and 3 entity class searches (see figure 8 (b)). So tourists do not seem to search for entity
classes more than locals do.
By looking at the difference between figure 8 (a) and 8 (b), we can make assumptions about what kind of places
are being most often explored with or without search. Two of the most prominent examples where we can observe
this are the Culture and the Food category. Here searches are very limited even though those are the most frequent
categories when it comes to places and destinations. Also the destinations have a lot more occurrences than the places.
This suggests that participants more often got directions to a place directly without going through the Place state first
which is supported by Directions being the second most frequently used usage pattern.
4.2.8 Summary The analysis of the data collected from tourists give first insights into how this user group uses mobile
map applications. We have shown a general overview over the state distribution that indicates a high portion of it being
Map-View Manipulation. We found that users are mostly interested in places that are within walking distance and that
they do not search a lot for entity classes and places related to Culture and Food are usually explored without search.

MapRecorder: Analysing Real World Usage of Mobile Map Applications

15

Being a small study the results presented above should not be generalised (even though some results look promising
due to their similarity) but guide future studies that want to investigate tourists as mobile map users.

5

DISCUSSION

Mobile map application usage is a complex set of behaviours and interactions that tells us a lot about how people
explore the world around them in the digital age. We have shown that our approach makes it possible to collect valuable
data to give insight into the regularities and exceptions of mobile map usage behaviour. Looking at two different user
groups we can give first insights into how mobile map usage behaviour may vary between different users and think
about consequences this can have for future designs of mobile maps. In the following we discuss the findings, compare
some of the results and talk about limitations of our approach.
People like to explore maps, either through necessity or curiosity, and this is reflected through the high usage times
in the Map-View Manipulation state in both studies. When taken in context of the other states of map use, this might be
indicative of a preference for agency during search. This predisposition of users to engage largely in the Map-View
Manipulation state is a suggestion that this interaction should be made as rich and meaningful as possible. This fits
evidence stating that exploratory search is a widely adopted behaviour to look for information on the web [17], and
that users enjoy panning and zooming to explore their area [3]. In the interviews users mentioned exploration and
information retrieval, like looking up restaurants’ menus or homepages, as crucial parts of the mobile map experience.
Some of our users even reported using Google Maps without location services turned on completely neglecting the
navigation aspect of it (referring to the native application). These behaviours support our intuition that mobile map
applications are no longer just used to get from A to B but also serve as an important source of information beyond that.
We see indications that this is already picked up on by industry with Google’s ever increasing number of Place Icons
within its maps [31] as well as the recent introduction of the “explore menu” [26] to Google Maps. This menu exactly
taps into the Map-View Manipulation state and introduces new ways of exploring your surroundings and finding the
information you need more quickly. Only future investigations can show whether this is an adequate substitute for
exploring the map yourself.

5.1

Implications

In study 1 we were able to identify complex usage patterns whilst examining the whole corpus of data collected over
the month the study was active. Patterns like MSPD or MD showed us that users find different ways of accomplishing
their goal of information retrieval in an mobile map application. This information could potentially influence the design
of future mobile map services as with the knowledge about usage patterns effective shortcuts can be developed (see
figure 10). Study 2 however did not reveal those patterns. This could hint towards a unique quality of tourist users but
could also be explained by the lack of a sufficiently big enough data set.
The low usage incidence of searching for entity classes was observed in both studies showing that most of all users
locals and tourists alike rather search for the actual name instead of the entity class. We think this points toward the
conclusion that text search is not the preferred way to look for entity class information. Again here we find support in
the current developments in industry. Instead of searching for restaurants or hotels “around you” Google now offers this
information within their “explore menu” [26], which our data suggests will be helpful for local and tourist users alike.

16

(a)

(b)

Fig. 10. Example of design changes inspired by the MSPD and MD pattern. Original interface (a) versus design changes (b). Map data
and image ©2019 Google.

5.2

Limitations

Our results and findings are based on a thorough data collection and analysis. We incentivised users to comply with
this data collection and found no indications in our data, that they did not. By excluding participants with less than five
sessions, we also tried to filter out participants who would only do minimum work to receive the reward (they were not
informed about the five session threshold). Still, unsupervised data collection bears the risk of collecting artificial usage
data or missing out on a certain amount of usage data that is produced outside the tracking possibilities of the study. As
we report earlier MapRecorder is not able to track in-app navigation. Thus whenever participants wanted to use this
feature they were redirected to their native Google Maps application. This is a common challenge researchers face in
unsupervised data collection and is discussed in related literature as well [8]. We saw consistent usage over the whole
study period, and session lengths that are line with other large scale mobile app usage study and thus cannot raise any
concerns.
Even though we are confident to have recorded genuine and organic usage behaviour, with study 1 featuring 28 and
study 2 featuring six participants we want to highlight generalisability as another important limitation. We agree with
Church et al. [11] that our results can only be interpreted in connection to the participants of our study. We present
quantitative findings and comparisons about usage behaviour that is unlikely to hold to another population. We also
agree that these studies still have great value, as the research community is able to combine and contrast different
studies on usage behaviour in different situations with different populations. This way we can build a better overall
understanding of mobile users as we tie more of these behaviours together.

MapRecorder: Analysing Real World Usage of Mobile Map Applications

17

The large engagement in the Map-View Manipulation state is one of our most intricate findings. Due to the coarse
categorisation of the Map-View Manipulation we find it challenging to formulate well defined implications. Our study was
supposed to explore this unexplored territory of mobile map usage behaviour. In our findings on Map-View Manipulation
and Google’s recent design changes to Google Maps we see great potential for future research that will be able to analyse
this exploratory behaviour in more detail.
6

CONCLUSION & FUTURE WORK

Our analysis considered the behaviour of two user groups, namely local users and tourists. Study 1 looking at local users
found a variety of behaviours, of which the most prominent are: A prevalence of exploratory behaviour indicated by
the Map-View Manipulation state, a search preference for named places instead of entity classes, and the use of specific
usage patterns. Study 2 found similar results for the amount of Map-View Manipulation and the search behaviour but is
lacking any indication of usage patterns. The results of study 2 can give first insights into how different user groups use
mobile map applications differently (or like in our case, similarly).
With the technical constraints on recording in-app navigation this paper puts its focus on the actual map interaction
and exploration. Nevertheless we acknowledge that there is already a big research corpus dealing with mobile navigation
(e.g. [7, 19, 25, 27, 39]) and that contributing to this corpus with unsupervised usage data of navigation applications
is a worthwhile goal to pursue. Adding a navigation component to MapRecorder could also give us valuable data to
complement our findings presented in this study. Looking into other mobile map applications than Google Maps could
help us making steps into this direction in the future and could then tell us not only a lot about how we explore but also
navigate the world around us. Till then this paper begins the process of shining a light on the high-profile black-box
that is among the most used applications in the world.
We present an organic map application usage study using our MapRecorder wrapper application and Google Maps to
understand and explore user behaviour within mobile maps. In addition to two surveys of device and map application
usage, we provide analysis for four main states of map interaction. We give one example of how this data can be used
to compare ways in which different users (locals and non-locals) typically engage with these applications. We hope
that these findings can help to provide context for mobile map research and practice, as well as to encourage the
investigation of real-world, unsupervised application usage for other programs and in other domains.
REFERENCES
[1] Linas Baltrunas, Karen Church, Alexandros Karatzoglou, and Nuria Oliver. 2015. Frappe: Understanding the usage and perception of mobile app
recommendations in-the-wild. arXiv preprint arXiv:1505.03014 (2015).
[2] Nikola Banovic, Christina Brant, Jennifer Mankoff, and Anind Dey. 2014. ProactiveTasks: The Short of Mobile Device Use Sessions. In Proceedings of
the 16th International Conference on Human-computer Interaction with Mobile Devices & Services (MobileHCI ’14). ACM, New York, NY, USA, 243–252.
https://doi.org/10.1145/2628363.2628380
[3] Alessio Bellino. 2015. Two New Gestures to Zoom: Enhancing Online Maps Services. In Proceedings of the 24th International Conference on World
Wide Web (WWW ’15 Companion). ACM, New York, NY, USA, 167–170. https://doi.org/10.1145/2740908.2742823
[4] Yash Bhavnani, Kerry Rodden, Laura Cuozzo Guarnotta, Margaret T. Lynn, Sara Chizari, and Laura Granka. 2017. Understanding Mobile Phone
Activities via Retrospective Review of Visualizations of Usage Data. In Proceedings of the 19th International Conference on Human-Computer Interaction
with Mobile Devices and Services (MobileHCI ’17). ACM, New York, NY, USA, Article 58, 10 pages. https://doi.org/10.1145/3098279.3119841
[5] M Blades and Christopher Spencer. 1987. How Do People Use Maps to Navigate Through the World. Cartographica: The International Journal for
Geographic Information and Geovisualization 24 (10 1987), 64–75.
[6] Matthias Böhmer, Brent Hecht, Johannes Schöning, Antonio Krüger, and Gernot Bauer. 2011. Falling asleep with Angry Birds, Facebook and Kindle:
a large scale study on mobile application usage. In Proceedings of the 13th international conference on Human computer interaction with mobile devices
and services. ACM, 47–56.

18
[7] Barry Brown and Eric Laurier. 2012. The normal natural troubles of driving with GPS. In Proceedings of the SIGCHI conference on human factors in
computing systems. ACM, 1621–1630.
[8] Juan Pablo Carrascal and Karen Church. 2015. An In-Situ Study of Mobile App & Mobile Search Interactions. In Proceedings of the 33rd Annual ACM
Conference on Human Factors in Computing Systems. ACM, 2739–2748.
[9] Alton Y. K. Chua, Radhika Shenoy Balkunje, and Dion Hoe-Lian Goh. 2011. Fulfilling Mobile Information Needs: A Study on the Use of Mobile
Phones. In Proceedings of the 5th International Conference on Ubiquitous Information Management and Communication. ACM, 92:1–92:7. https:
//doi.org/10.1145/1968613.1968721
[10] Karen Church, Mauro Cherubini, and Nuria Oliver. 2014. A Large-scale Study of Daily Information Needs Captured in Situ. ACM Trans. Comput.-Hum.
Interact. 21, 2, Article 10 (Feb. 2014), 46 pages. https://doi.org/10.1145/2552193
[11] Karen Church, Denzil Ferreira, Nikola Banovic, and Kent Lyons. 2015. Understanding the Challenges of Mobile Phone Usage Data. In Proceedings of
the 17th International Conference on Human-Computer Interaction with Mobile Devices and Services. ACM, 504–514. https://doi.org/10.1145/2785830.
2785891
[12] Trinh Minh Tri Do, Jan Blom, and Daniel Gatica-Perez. 2011. Smartphone usage in the wild: a large-scale analysis of applications and context. In
Proceedings of the 13th international conference on multimodal interfaces. ACM, 353–360.
[13] Hossein Falaki, Ratul Mahajan, Srikanth Kandula, Dimitrios Lymberopoulos, Ramesh Govindan, and Deborah Estrin. 2010. Diversity in Smartphone
Usage. In Proceedings of the 8th International Conference on Mobile Systems, Applications, and Services (MobiSys ’10). ACM, New York, NY, USA,
179–194. https://doi.org/10.1145/1814433.1814453
[14] Denzil Ferreira, Vassilis Kostakos, Alastair R. Beresford, Janne Lindqvist, and Anind K. Dey. 2015. Securacy: An Empirical Investigation of Android
Applications’ Network Usage, Privacy and Security. In Proceedings of the 8th ACM Conference on Security & Privacy in Wireless and Mobile Networks
(WiSec ’15). ACM, New York, NY, USA, Article 11, 11 pages. https://doi.org/10.1145/2766498.2766506
[15] Dan Frommer. 2017. These are the 10 most popular mobile apps in America. Blog. Retrieved August 28, 2017 from http://www.recode.net/2017/8/
24/16197218/top-10-mobile-apps-2017-comscore-chart-facebook-google.
[16] Layla Hasan, Anne Morris, and Steve Probets. 2009. Using Google Analytics to evaluate the usability of e-commerce sites. Human centered design
(2009), 697–706.
[17] Brent Hecht, Samuel H Carton, Mahmood Quaderi, Johannes Schöning, Martin Raubal, Darren Gergle, and Doug Downey. 2012. Explanatory
semantic relatedness and explicit spatialization for exploratory search. In Proceedings of the 35th international ACM SIGIR conference on Research and
development in information retrieval. ACM, 415–424.
[18] Daniel Hintze, Philipp Hintze, Rainhard D. Findling, and René Mayrhofer. 2017. A Large-Scale, Long-Term Analysis of Mobile Device Usage
Characteristics. Proc. ACM Interact. Mob. Wearable Ubiquitous Technol. 1, 2 (2017), 13:1–13:21.
[19] Markus Hipp, Florian Schaub, Frank Kargl, and Michael Weber. 2010. Interaction Weaknesses of Personal Navigation Devices. In Proceedings of the
2Nd International Conference on Automotive User Interfaces and Interactive Vehicular Applications (AutomotiveUI ’10). ACM, New York, NY, USA,
129–136. https://doi.org/10.1145/1969773.1969796
[20] Maryam Kamvar and Shumeet Baluja. 2006. A Large Scale Study of Wireless Search Behavior: Google Mobile Search. In Proceedings of the SIGCHI
Conference on Human Factors in Computing Systems. ACM, 701–709. https://doi.org/10.1145/1124772.1124877
[21] Menno-Jan Kraak. 1998. The Cartographic Visualization Process: From Presentation to Exploration. The Cartographic Journal 35, 1 (1998), 11–15.
https://doi.org/10.1179/000870498787074100
[22] Menno-Jan Kraak and Ferjan Ormeling. 2011. Cartography: visualization of spatial data. Guilford Press.
[23] Uichin Lee, Joonwon Lee, Minsam Ko, Changhun Lee, Yuhwan Kim, Subin Yang, Koji Yatani, Gahgene Gweon, Kyong-Mee Chung, and Junehwa Song.
2014. Hooked on Smartphones: An Exploratory Study on Smartphone Overuse Among College Students. In Proceedings of the SIGCHI Conference on
Human Factors in Computing Systems. ACM, 2327–2336. https://doi.org/10.1145/2556288.2557366
[24] Florian Lettner and Clemens Holzmann. 2012. Automated and unsupervised user interaction logging as basis for usability evaluation of mobile
applications. In Proceedings of the 10th International Conference on Advances in Mobile Computing & Multimedia. ACM, 118–127.
[25] Allen Yilun Lin, Kate Kuehl, Johannes Schöning, and Brent Hecht. 2017. Understanding Death By GPS: A Systematic Study of Catastrophic Incidents
Associated with Personal Navigation Technologies. In Proceedings of the 2017 CHI Conference on Human Factors in Computing Systems. ACM,
1154–1166.
[26] Sophia Lin. 2018. Explore and eat your way around town with Google Maps. Website. Retrieved June 5, 2018 from https://www.blog.google/
products/maps/explore-around-town-google-maps/.
[27] Andrew J. May, Tracy Ross, Steven H. Bayer, and Mikko J. Tarkiainen. 2003. Pedestrian Navigation Aids: Information Requirements and Design
Implications. Personal Ubiquitous Comput. 7, 6 (Dec. 2003), 331–338. https://doi.org/10.1007/s00779-003-0248-5
[28] Moira McGregor, Barry Brown, and Donald McMillan. 2014. 100 Days of iPhone Use: Mobile Recording in the Wild. In CHI ’14 Extended Abstracts on
Human Factors in Computing Systems (CHI EA ’14). ACM, New York, NY, USA, 2335–2340. https://doi.org/10.1145/2559206.2581296
[29] Donald McMillan, Alistair Morrison, Owain Brown, Malcolm Hall, and Matthew Chalmers. 2010. Further into the Wild: Running Worldwide Trials of
Mobile Systems. Springer Berlin Heidelberg, Berlin, Heidelberg, 210–227.
[30] Yelena Nakhimovsky, Andrew T Miller, Tom Dimopoulos, and Michael Siliski. 2010. Behind the scenes of google maps navigation: enabling
actionable user feedback at scale. In CHI’10 Extended Abstracts on Human Factors in Computing Systems. ACM, 3763–3768.

MapRecorder: Analysing Real World Usage of Mobile Map Applications

19

[31] Justin O’Beirne. 2017. A YEAR OF GOOGLE & APPLE MAPS. Website. Retrieved September 14, 2017 from https://www.justinobeirne.com/a-yearof-google-maps-and-apple-maps.
[32] Chris Perkins. 2003. Cartography: mapping theory. Progress in human geography 27, 3 (2003), 341–351.
[33] Martin Pielot, Karen Church, and Rodrigo de Oliveira. 2014. An In-situ Study of Mobile Phone Notifications. In Proceedings of the 16th International
Conference on Human-computer Interaction with Mobile Devices & Services. ACM, 233–242. https://doi.org/10.1145/2628363.2628364
[34] Ahmad Rahmati and Lin Zhong. 2013. Studying Smartphone Usage: Lessons from a Four-Month Field Study. IEEE Transactions on Mobile Computing
12, 7 (July 2013), 1417–1427. https://doi.org/10.1109/TMC.2012.127
[35] Jens Riegelsberger and Yelena Nakhimovsky. 2008. Seeing the bigger picture: a multi-method field trial of google maps for mobile. In CHI’08 extended
abstracts on Human factors in computing systems. ACM, 2221–2228.
[36] Alireza Sahami Shirazi, Niels Henze, Tilman Dingler, Martin Pielot, Dominik Weber, and Albrecht Schmidt. 2014. Large-scale assessment of mobile
notifications. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems. ACM, 3055–3064.
[37] Choonsung Shin, Jin-Hyuk Hong, and Anind K. Dey. 2012. Understanding and Prediction of Mobile Application Usage for Smart Phones. In Proceedings
of the 2012 ACM Conference on Ubiquitous Computing (UbiComp ’12). ACM, New York, NY, USA, 173–182. https://doi.org/10.1145/2370216.2370243
[38] Vijay Srinivasan, Saeed Moghaddam, Abhishek Mukherji, Kiran K. Rachuri, Chenren Xu, and Emmanuel Munguia Tapia. 2014. MobileMiner:
Mining Your Frequent Patterns on Your Phone. In Proceedings of the 2014 ACM International Joint Conference on Pervasive and Ubiquitous Computing
(UbiComp ’14). ACM, New York, NY, USA, 389–400. https://doi.org/10.1145/2632048.2632052
[39] Dirk Wenig, Johannes Schöning, Brent Hecht, and Rainer Malaka. 2015. StripeMaps: Improving Map-based Pedestrian Navigation for Smartwatches.
In Proceedings of the 17th International Conference on Human-Computer Interaction with Mobile Devices and Services (MobileHCI ’15). ACM, New York,
NY, USA, 52–62. https://doi.org/10.1145/2785830.2785862
[40] Kelly Widdicks, Oliver Bates, Mike Hazas, Adrian Friday, and Alastair R Beresford. 2017. Demand around the clock: time use and data demand of
mobile devices in everyday life. In Proceedings of the 2017 CHI Conference on Human Factors in Computing Systems. ACM, 5361–5372.

20
7

APPENDIX

7.1

Interview Guide

Thank you for taking the time for this interview. The data collected here is for a research project of the University of
Bremen and will be used exclusively for this purpose. Therefore it is important that this conversation is recorded. Your
personal data will be anonymised so that the information you provide here cannot be traced back to you. Is that all
right with you?
Personal background:
(1) Can you briefly tell me something about your life situation? (age, education, profession)
(2) What were or are the most important places in your life? (childhood, favourite places, place of residence ...,
spending time)
Map use:
(1) What do you use Google Maps for? (To find new places in the city, only for long distances (highways), ...)
(2) On which devices do you use Google Maps? (Do the occasions differ/when do you use it on your laptop/cell
phone/PC?)
(3) What is your experience with Google Maps? (Good, bad, would recommend/delay using it, because ...)
(4) What features, apart from navigation, do you use on Google Maps? (Ratings restaurants, current traffic news,
public transport information, sightseeing)
(5) What setting or feature are you missing on Google Maps? (What could be improved?)
(6) What other navigation services have you used in the past?
(7) Do you still have old-fashioned paper maps? (Still in use, in the car, in the house, why are they still used or no
longer used)
(8) I can see from your usage data that you looked around a lot in the map view. So you scrolled around in the map
view without entering a specific location or destination. Can you tell me something about that?
(9) Possibly more questions about the data
Perception of space:
(1) What do you concentrate on when planning a route with Google Maps? (Settings -shortest/fastest route, avoid
motorway, ...)
(2) Have you ever planned an excursion/a walk with a navigation service? (To what extent have you used the
navigation service for this?)
(3) Do you have the feeling that by using Google Maps you are getting to know your surroundings better or in
a different way? How do you perceive your surroundings while navigating with Google Maps? (New streets
discovered or beautiful places / has your space ’enlarged’?)
(4) You probably know such situations: You’re at a big event with a lot of people on big premises (Christmas market,
festival...). Suppose you wanted to meet a friend. How would you arrange the meeting place? How would you
have done that ten years ago?
(5) Have you ever shared your point of view with friends/family? (If so, in which situations and through which
ministry?
(6) Do you know Google Street View? Have you used this feature before or do you use it sometimes? (If so, in which
situations?)

MapRecorder: Analysing Real World Usage of Mobile Map Applications

21

Linking to other services:
(1) When you use navigation, do you trust Google Maps to find the best route for you? (Do you trust the route
calculation or do you rather let it run while paying attention to signs/maps?)
(2) What would you think if Google Maps cooperated with other services such as Facebook, giving you more
personalised routes? (E.g. if your workplace is specified on Facebook and Google Maps creates the optimal route
to work on each working day with calculated arrival time depending on the current traffic situation).
(3) Can you imagine further links with navigation apps?
Data privacy:
(1) Are there situations where you don’t want to use Google Maps?
(2) What settings have you made on your smartphone regarding location/GPS (Smartphone/Tablet: Always on/is
consciously switched on/off...)
(3) If the GPS is on, what do you think about Google (and other services) having access to your location?
Views and opinions:
(1) How would you describe the importance of navigation apps in your everyday life?
(2) There has been a change from map navigation to mobile navigation devices and now navigation apps in the last
10-15 years. How do you see the future of navigation in another ten years? (And does this idea scare you/If so,
why?)
(3) The future will probably be even more computer-based. There are smart cars that only need an address or an
instruction like ’I want to visit my friend Ben’ and the car will know where to navigate and may even drive
without our help. What do you think?
(4) Is there anything else you would like to add? Is there perhaps an aspect that is important to you that has not yet
been covered in this conversation?
(5) Thank you again for your time.

22
WORD COUNT
Words in text: 8354
Words in headers: 84
Words outside text (captions, etc.): 152
Number of headers: 37
Number of floats/tables/figures: 10
Number of math inlines: 7
