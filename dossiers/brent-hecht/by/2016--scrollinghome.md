---
title: "ScrollingHome: Bringing Image-based Indoor Navigation to Smartwatches"
person: brent-hecht
attendance: unconfirmed
section: by
type: conference-paper
year: 2016
date: 2016-08-26
venue: "Document Server@UHasselt (UHasselt)"
authors: "Dirk Wenig, Alexander Steenbergen, Johannes Schöning, Brent Hecht, Rainer Malaka"
source_url: https://doi.org/10.1145/2935334.2935373
fulltext_url: https://brenthecht.com/publications/ScrollingHome_MobileHCI_2016.pdf
openalex_id: W2514188633
doi: https://doi.org/10.1145/2935334.2935373
oa_status: closed
cited_by_count: 8
retrieved: 2026-08-13
content: full-text
notes: "Full text from the author's self-archived PDF at https://brenthecht.com/publications/ScrollingHome_MobileHCI_2016.pdf (text extracted with pdftotext; PDF not stored); title expanded from the OpenAlex record's truncated form using the author's own publications page / Semantic Scholar"
---

# ScrollingHome: Bringing Image-based Indoor Navigation to Smartwatches

## Full text

ScrollingHome: Bringing Image-based Indoor Navigation
to Smartwatches
Dirk Wenig

Alexander Steenbergen

Johannes Schöning

Digital Media Lab
TZI, University of Bremen
dwenig@tzi.de

University of Bremen
alexandersteenbergen@gmail.com

Expertise Centre for Digital Media
Hasselt University – tUL – iMinds
johannes.schoening@uhasselt.be

Brent Hecht

Rainer Malaka

Dept. of Comp. Sci. and Engineering
University of Minnesota
bhecht@cs.umn.edu

Digital Media Lab
TZI, University of Bremen
malaka@tzi.de

ABSTRACT

Providing pedestrian navigation instructions on small
screens is a challenging task due to limited screen space. As
image-based approaches for navigation have been successfully proven to outperform map-based navigation on mobile
devices, we propose to bring image-based navigation to
smartwatches. We contribute a straightforward pipeline to
easily create image-based indoor navigation instructions
that allow users to freely navigate in indoor environments
without any localization infrastructure and with minimal
user input on the smartwatch. In a user study, we show that
our approach outperforms the current state-of-the art application in terms of task completion time, perceived task load
and perceived usability. In addition, we did not find an
indication that there is a need to provide explicit directional
instructions for image-based navigation on small screens.
Author Keywords

smartwatches; cartography; mobile maps; pedestrian navigation; stripe maps

mobile phones is well-known and well-studied [16,25],
smartwatches are not just downscaled mobile phones: techniques that work on mobile phones do not necessarily work
on smartwatches (e.g., text input using software keyboards).
Pedestrian navigation using maps is an important smartwatch use case that faces obstacles due to both of these
challenges. While map apps are included by default on both
the Apple Watch and Android Wear platforms, these are
lightweight adaptations of their corresponding smartphone
apps. Recent work [23] has discussed the limitations associated with using these mobile phone-like map apps for
navigation tasks.
The StripeMaps project [23] addresses this problem by
adapting the mobile web design technique of linearization
for displaying maps on the small screens of smartwatches.
The StripeMaps team demonstrated that StripeMaps outperforms both traditional mobile map interfaces and turn-byturn directions for indoor navigation using smartwatches.

ACM Classification Keywords

H.5.2 [Information Interfaces and Presentation]: User Interfaces — input devices and strategies, interaction styles
INTRODUCTION

Designing interactive applications for smartwatches is challenging as one of the most prominent problems in mobile
HCI, the “fat finger problem” [20], heavily impacts interaction with small screens. As such, researchers have explored
additional input modalities and techniques [18,26], as well
as developed new visualization approaches [23]. Additionally, while the problem of adapting interfaces originally
developed for larger-screen displays to smaller devices like
Permission to make digital or hard copies of all or part of this work for personal
or classroom use is granted without fee provided that copies are not made or
distributed for profit or commercial advantage and that copies bear this notice
and the full citation on the first page. Copyrights for components of this work
owned by others than the author(s) must be honored. Abstracting with credit is
permitted. To copy otherwise, or republish, to post on servers or to redistribute
to lists, requires prior specific permission and/or a fee. Request permissions
from Permissions@acm.org.
MobileHCI '16, September 06 - 09, 2016, Florence, Italy
Copyright is held by the owner/author(s). Publication rights licensed to ACM.
ACM 978-1-4503-4408-1/16/09…$15.00
DOI: http://dx.doi.org/10.1145/2935334.2935373

Figure 1: The ScrollingHome application concept; the user
scrolls through a series of images showing the route.

However, despite the success of StripeMaps, it did not
leverage one important potential opportunity: StripeMaps
relies on traditional cartographic representations, but there
is evidence that image-based navigation approaches can
have benefits with small displays [3,6,8,9]. The goal of this
paper is to combine StripeMaps with these image-based
approaches and evaluate whether doing so outperforms the
StripeMaps state-of-the-art.
The contribution of this paper is thus threefold. First, we
present the ScrollingHome app (see Figure 1). By building
on the StripeMaps principle [23], ScrollingHome allows
users to navigate indoors using image-based approaches
without any specialized positioning infrastructure: the user
enters a building through a specific entry (e.g., the main
entrance), selects a starting point as well as a destination
point and then uses ScrollingHome to navigate through the
building. We also present an accompanying straightforward
pipeline to easily create image-based navigation instructions. Secondly, we investigate the effectiveness and usability of image-based navigation on smartwatch screens and
show that ScrollingHome outperforms the current state-ofthe-art app, StripeMaps, in terms of navigation task completion time, perceived mental workload as well as perceived
usability. Thirdly, we did not find any indication that there
is a need to provide further direction information for imagebased navigation on small screen devices as is typically
done by in research and practice.
RELATED WORK

Work on mobile device-based navigation dates back almost
two decades. Interestingly, the DeepMap system [14], one
of the earliest mobile guides, presented animated route
information on a wrist-mounted display. Other early projects used maps on pre-smartphone mobile devices. The
Cyberguide [1] presented a schematic map, which was
automatically updated based on the user’s position. The
goal of the GUIDE [5] project was to build a mobile tourist
guide for the city of Lancaster. It allowed the user to switch
between an overview map and a map of the local area. For
an overview of early map-based mobile guides see the survey of Baus et al. [2], Huang and Gartner [11] provide an
overview focused on indoor navigation systems.

landmark-based navigation instructions by detecting salient
landmarks in panoramic street imagery. Vaittinen et al. [21]
described the user-centered design of an image-based navigation service for mobile devices and confirmed in a field
trial that images help with detecting the destination. Because of this and the aforementioned advantages of using
images for route information, some image-based navigation
systems exist in industry as well; with the navigation feature of Google Street View, which uses 360° panoramic
images, as the most successful.
Practitioners and researchers have also explored navigation
on various wearable devices. Google’s Android Wear platform supports turn-by-turn navigation while Google Glass
additionally supports visualizing route information on
maps. Pielot et al. [17] explored the use of a vibrotactile
belt to continuously indicate a destination’s direction relative to the user’s orientation. Schirmer et al. [19] presented
a similar system, but integrated the vibration actuators into
the user’s shoes. McGookin and Brewster [15] investigated
undirected navigation for runners by designing a navigation
system called RunNav, which could also be used on a
smartwatch. RunNav does not provide explicit routes, but
rather a high-level overview to inform runners of areas that
are good and bad places to run. Kerber et al. [12] demonstrated how smartwatches could be used as magic lenses to
browse through maps, but also showed that this technique
does not outperform a “classical” UI. Wenig et al. [23]
introduced StripeMaps, a cartographic approach for indoor
navigation with smartwatches. StripeMaps transforms 2D
maps with route information into a 1D stripe (see Figure 2).
In a user study, StripeMaps outperformed both traditional
mobile map interfaces and turn-by-turn instructions. This
shows that users can benefit from alternative visualization
approaches for route information when navigating with
smartwatches.

Early work in the field of image-based navigation demonstrated the supporting value of photographs augmenting
auditory instruction and maps [6] or combined with textual
instructions and maps [3]. Goodman et al. [8,9] used photographs in a navigation system for older adults. In a field
experiment, the participants preferred to use audio instructions and images [9]. In another experiment, landmarks
pictured on images performed better than landmarks presented by speech [8].
Walther-Franks and Malaka [22] built an image-only navigation system for mobile devices and used photographs of
decision points augmented with visual instructions to guide
users incrementally from waypoint to waypoint without a
map. Recently, Wither et al. [24] automatically created

Figure 2: StripeMaps converts a 2D map to a 1D stripe. The
original path on the 2D map is shown on the mini-map. The
cut (shown on the smartwatch) indicates the direction of the
turn the user needs to make to navigate along the path (figure
adapted from Wenig et al. [23]).

THE SCROLLINGHOME APPLICATION

The underlying concept of the ScrollingHome application is
very simple: users scroll through a series of images showing their route. The images are extracted from videos taken
from a first person view (see below for details). Like
StripeMaps, users are able to scroll through these images by
scrolling vertically on the display. Moving the finger upwards on the smartwatch shows previous images while
moving downwards shows the following images that guide
the users on their route through a building.
Controlling route information by linearizing user interaction
and confining it to single, simple scrolling gestures have
been proven successful with StripeMaps. ScrollingHome
takes the same approach, but with image-based route information instead of the traditional cartographic representations by StripeMaps. As existing image-based navigation
approaches for mobile devices have also included visual
instructions (e.g., path visualizations or arrows) [22], instead of only presenting plain images on the smartwatch,
we implemented a slightly modified second version of
ScrollingHome that augments the images with a 3D path
visualization of the route.
Implementation

Example indoor navigation videos were taken with a bridge
camera (Panasonic DMC-FZ 200) by traversing different
routes at a regular walking pace while holding the camera at
an ‘eye-level’. No further equipment (e.g., light or stabilization) was used. Videos were taken in the evening hours to
ensure that no other people were captured on the video to
preserve their privacy and to not distract the user during the
navigation task. Microsoft Hyperlapse1 [13] was used to
remove trembling and jerky motion as well as to smooth the
video.
In a next step, for the extended version of ScrollingHome
with path visualizations, Adobe After Effects and Cinema
4D were used to composite 3D elements over the 2D footage. The camera motion was extracted using the 3D camera
tracker by Adobe After Effects and exported to Cinema 4D
to create an animated camera. In the last manual step, in
Cinema 4D the 3D path as well as virtual walls were added
to occlude the path where needed in the video.
Finally, the videos were scaled down to 320×320 pixels to
match the resolution of the smartwatch used for our study
(see below) and turned into a sequence of JPEGs. This
approach allows direct manipulation of the image sequence
at various speeds in high quality – similar to the video
browsing approach by Dragicevic et al. [7] – and for maps,
similar to StripeMaps. For the user, the image sequence
appears to be an interactive video. 15fps turned out to be
sufficient for smooth slow scrolling and also well-suited
suited for scrolling faster than real time.

1

http://research.microsoft.com/en-us/um/redmond/projects/hyperlapseapps/

Figure 3: Conditions in the user study: StripeMaps (SM) (a)
and the image-based approach without (ScroHo) (b) and with
route information (ScroHo+P) (c).
USER STUDY

We performed a user study to test the effectiveness of image-based approaches for indoor pedestrian navigation. The
study focused on comparing our approach against StripeMaps, the best known navigation approach for smartwatches [23]. The study was conducted in one of the main university buildings on the campus of the University of Bremen.
Participants & Apparatus

We recruited 18 participants (6 females and 12 males) with
an average age of 27.1 years. None of them owned or had
any prior experience with smartwatches and only 8 said that
they wore regular wrist watches. All of them were dominantly right-handed and only two wore the watch on the
right arm instead of the left. The study was performed on a
Sony SmartWatch 3.
Task & Procedure

The participants were introduced to the experiment and told
to navigate to three different places in the building (withinsubject design). Both the images and the map were preloaded on the smartwatch so that the participants did not
need to interact with the paired smartphone at all.
The three navigation tasks had similar length (about 220 m)
and similar characteristics. The routes each featured four
right and four left turns and were laid out on three different
floors of the same building to ensure no overlap and similar
environmental make-up. None of the routes contained any
stairs to avoid a 3D overlap which could have caused confusion in the StripeMap-based representation of the routes.
By stretching and compressing the videos, we made sure
that in all three conditions the user had to scroll the same
amount of pixels until reaching the destination. Using a
within-subject design, all participants performed the test
with all the following three conditions (see Figure 3):
(1) StripeMaps (SM)
(2) ScrollingHome (ScroHo)
(3) ScrollingHome with path visualizations (ScroHo+P)
Both the order of the three conditions and the order of the
routes were counterbalanced. The stripes for the StripeMaps
condition (SM) were created based on a black/white floor
plan of the university. We colored the floor to match its
color to the building’s floor (the participants had to walk on

Figure 4: Overview of the study results; mean time the participants needed to complete a single route, mean navigation errors and
mean NASA-TLX overall values (from left to right).

different colored floors) and added color to some noteworthy features like grass in a patio to make sure that the
stripes are as similar as possible to the maps stripes used in
the evaluation by Wenig et al. [23]. In the second condition
(ScroHo), the participants used the image-based navigation
approach as described above. In the third condition
(ScroHo+P), additional path visualizations providing route
information were added to the video (see previous section).
During the navigation task, an experimenter followed the
participants a few meters behind, measuring time and
counting navigation errors. We counted one error when a
participant took a wrong turn without noticing the error
within five meters. After five meters, the experimenter told
the participant of the error and sent her/him back on the
correct direction. In addition to time and error, we measured the perceived usability using the System Usability
Scale (SUS) [4] and the perceived task load using the
NASA-TLX [10] for all conditions. The participants filled
in both questionnaires after each navigation task. We encouraged the participants to think aloud when navigating
and recorded noteworthy incidents in writing. After they
completed all three navigation tasks, we conducted a semistructured interview with each participant. Overall, the total
time for participating in the study was around 45 minutes.
Results & Discussion

All participants were able to complete all navigation tasks.
Time and Error

On average, the participants needed about 187 seconds per
task and made 0.59 errors per task (Figure 4 summarizes
the results). The ScroHo condition performed best with 170
seconds on average (SD = 65 s) with an error rate of 0.22
(SEM = 0.17) and a maximum of 3 errors. The ScroHo+P
condition performed second best with 171 second on average (SD = 44 s) and an error rate of 0.44 (SEM = 0.2) again
with a maximum of 3 errors. In the SM condition, the participants took the most time (220 seconds on average, SD =
53 s) and also committed the most errors (1.11 on average,
SEM = 0.31).
Regarding time, Kolmogorov-Smirnov tests showed that for
the SM condition time is not normally distributed. A nonparametric Friedman’s two-way ANOVA by ranks for
related samples revealed significant differences (𝜒 " =
7, 𝑝 = .02). Bonferroni-corrected (significance level of

.016) pairwise Wilcoxon tests confirmed significant differences between SM and ScroHo (𝑝 = .011) as well as between SM and ScroHo+P (𝑝 = .012). For errors, statistical
analysis did not reveal any significant difference. Overall,
while the participants navigated faster via ScrollingHome
without and with additional path visualization than via
StripeMaps, we did not find any indication that there is a
need to provide direction information for image-based navigation on small screen.
Interestingly, only three test runs took more than 300 seconds (one for each condition): one participant (P9: male,
34 years old) was much faster in the SM condition than in
both image-based conditions (SM = 185 s, ScroHo = 395 s,
ScroHo+P = 307 s) while another one (P13: female, 25
years old) was much slower in the SM condition than in
both image-based conditions (SM = 345 s, ScroHo = 158 s,
ScroHo+P = 163 s). It seems that P9 struggled extensively
with image-based navigation while P13 does the same with
map-based navigation, suggesting that there may be
important individual differences to consider here.
Questionnaires

The mean overall NASA-TLX values (normalized between
0 and 100) are low for both ScrollingHome conditions
(ScroHo = 19.0, SD = 16.6 and ScroHo+P = 15.8, SD =
11.2) while the values for SM are higher (30.5, SD = 14.6).
A low NASA task load index indicates a relative low subjective mental workload. A one-way ANOVA for repeated
measures (𝐹",,- = 10.8, 𝑝 < .001) and post-hoc Sidakcorrected pairwise analysis revealed significant differences
between SM and ScroHo (𝑝 = .027) as well as between SM
and ScroHo+P (𝑝 < .001).
Mean SUS scores can be considered good for both
ScrollingHome conditions (ScroHo = 81.4, SD = 17.2 and
ScroHo+P = 83.8, SD = 13.4) followed by SM (54.5, SD =
17.1). Again, a one-way ANOVA for repeated measures
(𝐹",,- = 28.7, 𝑝 < .001) and post-hoc Sidak-corrected
pairwise analysis confirmed statistical differences between
SM and ScroHo (𝑝 < .001) as well as between SM and
ScroHo+P (𝑝 < .001). That means that ScrollingHome with
and without direct navigation instructions outperformed
StripeMaps regarding the perceived task load as well as
regarding the perceived usability. Again, there were no
significant differences between ScroHo and ScroHo+P.

Observations and Interviews

In general, the participants understood the ScrollingHome
concept very quickly and were fluent in scrolling after a
few seconds.
When taking a wrong turn, in most cases the participants
noticed their mistake after a few meters by themselves.
They scrolled back, compared the images on the smartwatch with the surroundings, and almost always were able
to return to the correct route. Rarely, false positive errors
occurred; the participants thought that they were wrong but
they actually were traveling along the right path. In these
cases, the participants stopped for a moment to compare the
images on the smartwatch with the surroundings. After a
few seconds, they realized that they were on the correct
route and continued walking.
Regarding the scrolling behavior, some participants were
constantly scrolling while they were walking and kept the
images on the smartwatch exactly synchronized with their
current position. Others used a slight different approach:
they scrolled through the images to the next turn first and
then walked to that point without looking at the smartwatch.
After taking the turn, they stopped and scrolled to the next
turn again. In the end, the second approach turned out to be
faster than the first one.
In the semi-structured interviews, ScrollingHome was described as a “very good idea” and “very intuitive”. One
participant explained, that because of the images he only
had to glance at the smartwatch out of the corner of his eye.
However, feedback on the path augmentation was mixed,
e.g. one participant criticized that it covers large parts of the
image. We can refer to this as the “Fat Arrow Problem” for
smartwatches in imaged-based navigation. The app itself
was described as “respond[ing] very fast to user touch input” and the “interaction was very smooth”.
CONCLUSION

In this paper, we introduced novel methods for image-based
navigation on smartwatches. The basic idea is to use a video-like series of images of a pre-recorded walk along a path
that can be scrolled by the user as they navigate.
Our first prototype works on images automatically extracted from video only (ScroHo), while the second requires
additional manual steps for pre-processing and image registration in order to overlay the images with additional graphical path information (ScroHo+P). We compared both prototypes with StripeMaps (SM), the state-of-the-art mapbased approach for indoor navigation on smartwatches. Our
user study revealed promising results and shows that imagebased navigation can indeed outperform StripeMaps with
respect to navigation time, perceived taskload, and other
metrics. Interestingly, the ScroHo+P method, which requires substantially greater content generation effort than
the ScroHo method, did not outperform ScroHo and thus
we see no support for the need to expend that effort.

We also observed individual differences indicating that one
single technique may not work best with all users. Additionally, more individual predispositions may lead to personal preferences and restrictions (e.g., visual impairments).
However, our results suggest that the image-based approach
is a more effective method for pedestrian navigation using
smartwatches in general.
ScrollingHome also has benefits regarding the effort that is
needed to create the content. Creating routes with the
ScrollingHome approach is straightforward (only the
ScroHo+P condition requires extra work). Creating good
maps, which is needed for full 2D maps as well as for
StripeMaps, requires an expert and is a time consuming
task. At the moment, we are working on a mobile app assisting the user to create all possible routes in a building.
ScrollingHome as well as StripeMaps both work without
position information, making it suitable for indoor navigation. Compared to a traditional full 2D map, a limitation of
both approaches are situations where the user has become
lost (the basic orientation use case). Here, a 2D map allows
the user to scroll in both dimensions along the route and to
localize herself/himself again. However, apart from the
very small number of navigation errors in the study with
ScrollingHome, an advantage of image-based approaches is
that the user likely notices her/his mistake very quickly
because of all the details in the images, while corridors on
floorplans (indoor maps) often look the same. This allows
him/her to go back on the correct route.
FUTURE WORK

For future work, it will be important to identify means by
which we can provide a tracking mechanism in order to
give the user feedback in the case of errors. The additional
integration of an orientation indicator might also be a useful
addition. Furthermore, while the routes used in the study
did include narrow floors as well as some halls, the routes
did not include changing levels in multi-level buildings via
stairs or elevators. Future work should investigate such
situations as well as more special ones, e.g., mezzanines.
Lastly, we recorded our videos especially for the purpose of
this study. Future work should examine more scalable solutions, for instance leveraging the indoor imagery available
in Google Street View.
ACKNOWLEDGMENTS

This work was funded in part by a Google Research Faculty
Award and a 3M NTFA, as well as BOF R-6060, NSF IIS1552955, and UID/EEA/50009/2013.
REFERENCES

1.

Gregory D. Abowd, Christopher G. Atkeson, Jason
Hong, Sue Long, Rob Kooper, and Mike Pinkerton.
1997. Cyberguide: A Mobile Context-aware Tour
Guide. Wirel. Netw. 3, 5 (October 1997), 421-433.
http://dx.doi.org/10.1023/A:1019194325861

2.

Jörg Baus, Keith Cheverst, and Christian Kray. 2005.
A Survey of Map-based Mobile Guides. In Map-based

Mobile Services. Springer, Berlin / Heidelberg, Germany, 193-209.
http://dx.doi.org/10.1007/3-540-26982-7_13

Geoinformation and Cartography. Springer, Berlin /
Heidelberg, Germany, 305–319.
http://dx.doi.org/10.1007/978-3-642-03294-3_20

3.

Ashweeni Kumar Beeharee and Anthony Steed. 2006.
A Natural Wayfinding Exploiting Photos in Pedestrian
Navigation Systems. In Proceedings of the 8th Conference on Human-Computer Interaction with Mobile Devices and Services (MobileHCI '06). ACM, New York,
NY, USA, 81-88.
http://doi.acm.org/10.1145/1152215.1152233

4.

John Brooke. 1996. SUS-A Quick and Dirty Usability
Scale. In Usability Evaluation in Industry 189.194: 4-7.

12. Frederic Kerber, Antonio Krüger, and Markus Löchtefeld. 2014. Investigating the Effectiveness of Peephole
Interaction for Smartwatches in a Map Navigation
Task. In Proceedings of the 16th International Conference on Human-Computer Interaction with mobile Devices & Services (MobileHCI '14). ACM, New York,
NY, USA, 291-294.
http://doi.acm.org/10.1145/2628363.2628393

5.

6.

Keith Cheverst, Nigel Davies, Keith Mitchell, Adrian
Friday, and Christos Efstratiou. 2000. Developing a
Context-aware Electronic Tourist Guide: Some Issues
and Experiences. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (CHI
'00). ACM, New York, NY, USA, 17-24.
http://doi.acm.org/10.1145/332040.332047

13. Johannes Kopf, Michael F. Cohen, and Richard
Szeliski. 2014. First-person Hyper-lapse Videos.ACM
Trans. Graph. 33, 4, Article 78 (July 2014),
http://dx.doi.org/10.1145/2601097.2601195
14. Rainer Malaka and Alexander Zipf. 2000. Deep Map –
Challenging IT Research in the Framework of a Tourist
Information System. In Information and Communication Technologies in Tourism: 15–27.

Luca Chittaro and Stefano Burigat. 2005. Augmenting
Audio Messages with Visual Directions in Mobile
Guides: An Evaluation of Three Approaches.
In Proceedings of the 7th International Conference on
Human Computer Interaction with Mobile Devices &
Services (MobileHCI '05). ACM, New York, NY,
USA, 107-114.
http://doi.acm.org/10.1145/1085777.1085795

16. Ethan Marcotte. 2011. Responsive Web Design. A
Book Apart.

7.

Pierre Dragicevic, Gonzalo Ramos, Jacobo Bibliowitcz, Derek Nowrouzezahrai, Ravin Balakrishnan,
and Karan Singh. 2008. Video Browsing by Direct
Manipulation. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (CHI
'08). ACM, New York, NY, USA, 237-246.
http://dx.doi.org/10.1145/1357054.1357096

17. Martin Pielot, Niels Henze, and Susanne Boll. 2009.
Supporting Map-based Wayfinding with Tactile Cues.
In Proceedings of the 11th International Conference on
Human-Computer Interaction with Mobile Devices and
Services (MobileHCI '09). ACM, New York, NY,
USA, Article 23, 10 pages.
http://doi.acm.org/10.1145/1613858.1613888

8.

Joy Goodman, Stephen Brewster, and Phil Gray. 2005.
How Can We Best Use Landmarks to Support Older
People in Navigation? In Behaviour & Information
Technology 24.1, 3–20.
http://dx.doi.org/10.1080/01449290512331319021

18. Jun Rekimoto. 1996. Tilting Operations for Small
Screen Interfaces. In Proceedings of the 9th Annual
ACM Symposium on User Interface Software and
Technology (UIST '96). ACM, New York, NY, USA,
167-168. http://doi.acm.org/10.1145/237091.237115

9.

Joy Goodman, Phil Gray, Kartik Khammampad, and
Stephen Brewster. 2004. Using Landmarks to Support
Older People in Navigation. In: Proceedings of the 6th
International Conference on Human-Computer Interaction with Mobile Devices & Services (MobileHCI
'04). Vol. 3160 of Lecture Notes in Computer Science.
Springer, Berlin / Heidelberg, Germany, pp. 38–48.
http://dx.doi.org/10.1007/978-3-540-28637-0_4

19. Maximilian Schirmer, Johannes Hartmann, Sven Bertel, and Florian Echtler. 2015. Shoe me the Way: A
Shoe-Based Tactile Interface for Eyes-Free Urban
Navigation. In Proceedings of the 17th International
Conference on Human-Computer Interaction with Mobile Devices and Services (MobileHCI '15). ACM,
New York, NY, USA, 327-336.
http://doi.acm.org/10.1145/2785830.2785832

10. Sandra G. Hart and Lowell E. Staveland. 1988. Development of NASA-TLX (Task Load Index): Results of
Empirical and Theoretical Research. In Advances in
Psychology 52: 139-183.

20. Katie A. Siek, Yvonne Rogers, and Kay H. Connelly.
2005. Fat Finger Worries: How Older and Younger
Users Physically Interact with PDAs. In Proceedings of
the 10th IFIP TC13 Conference on Human-Computer
Interaction (INTERACT '05). Vol. 3585 of Lecture
Notes in Computer Science. Springer, Berlin / Heidel-

11. Haosheng Huang and Georg Gartner. 2010. A Survey
of Mobile Indoor Navigation Systems. In Cartography
in Central and Eastern Europe. Lecture Notes in

15. David K. McGookin and Stephen A. Brewster. 2013.
Investigating and Supporting Undirected Navigation
for Runners. In CHI '13 Extended Abstracts on Human
Factors in Computing Systems (CHI EA '13). ACM,
New York, NY, USA, 1395-1400.
http://doi.acm.org/10.1145/2468356.2468605

berg, Germany, pp. 267–280.
http://dx.doi.org/10.1007/11555261_24
21. Tuomas Vaittinen, Miikka Salminen, and Thomas
Olsson. 2013. City Scene: Field Trial of a Mobile
Street-imagery-based Navigation Service.
In Proceedings of the 15th International Conference on
Human-Computer Interaction with Mobile Devices and
Services (MobileHCI '13). ACM, New York, NY,
USA, 193-202.
http://doi.acm.org/10.1145/2493190.2493229
22. Benjamin Walther-Franks and Rainer Malaka. 2008.
Evaluation of an Augmented Photograph-Based Pedestrian Navigation System. In Proceedings of the 9th International Symposium on Smart Graphics (SG '08).
Vol. 5166 of Lecture Notes in Computer Science.
Springer, Berlin / Heidelberg, Germany, 94–105.
http://dx.doi.org/10.1007/978-3-540-85412-8_9
23. Dirk Wenig, Johannes Schöning, Brent Hecht, and
Rainer Malaka. 2015. StripeMaps: Improving Mapbased Pedestrian Navigation for Smartwatches.
In Proceedings of the 17th International Conference on
Human-Computer Interaction with Mobile Devices and
Services (MobileHCI '15). ACM, New York, NY,
USA, 52-62.
http://doi.acm.org/10.1145/2785830.2785862
24. Jason Wither, Carmen E. Au, Raymond Rischpater,
and Radek Grzeszczuk. 2013. Moving Beyond the
Map: Automated Landmark Based Pedestrian Guidance Using Street Level Panoramas. In Proceedings of
the 15th International Conference on Human-computer
Interaction with Mobile Devices and Services (MobileHCI '13). ACM, New York, NY, USA,
203-212. http://doi.acm.org/10.1145/2493190.2493235
25. Dongsong Zhang. 2007. Web Content Adaptation for
Mobile Handheld Devices. In Commun. ACM 50, 2
(February 2007), 75-79.
http://doi.acm.org/10.1145/1216016.1216024
26. Robert Xiao, Gierad Laput, and Chris Harrison. 2014.
Expanding the Input Expressivity of Smartwatches
with Wechanical Pan, Twist, Tilt and Click.
In Proceedings of the SIGCHI Conference on Human
Factors in Computing Systems (CHI '14). ACM, New
York, NY, USA, 193-196.
http://doi.acm.org/10.1145/2556288.2557017
