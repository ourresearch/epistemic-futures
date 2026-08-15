---
title: "WikEar: Automatically Generated Location-Based Audio Stories between Public City Maps"
person: brent-hecht
attendance: unconfirmed
section: by
type: journal-article
year: 2007
date: 2007-01-01
venue: "Ubiquitous Computing"
authors: "J. Schoening, Brent Hecht, Michael Rohs, Nicole Starosielski"
source_url: http://brenthecht.com/papers/bhecht_ubicomp2007_wikear.pdf
fulltext_url: https://brenthecht.com/publications/bhecht_ubicomp2007_wikear.pdf
openalex_id: W2617812837
oa_status: closed
cited_by_count: 12
retrieved: 2026-08-13
content: full-text
notes: "Full text from the author's self-archived PDF at https://brenthecht.com/publications/bhecht_ubicomp2007_wikear.pdf (text extracted with pdftotext; PDF not stored)"
---

# WikEar: Automatically Generated Location-Based Audio Stories between Public City Maps

## Full text

WikEar − Automatically Generated Location-Based Audio Stories
between Public City Maps
Johannes Schöning1, Brent Hecht2, Michael Rohs3, Nicole Starosielski4
1

2,4

Institute for Geoinformatics, University of Münster
48149 Münster, Germany
j.schoening@uni-muenster.de

Department of Geography / Department of Film Studies, University of California Santa Barbara
Santa Barbara, CA 93106
{bhecht, n_star}@umail.ucsb.edu
3

Deutsche Telekom Laboratories, TU Berlin
10587 Berlin, Germany
michael.rohs@telekom.de

Abstract. Many mobile applications that lead tourists to landmarks and businesses ignore the
educational component of tourism. The systems that do satiate the tourist’s desire for learning about
visited places require so much costly custom content development that they can only be implemented at
very local scales. Moreover, these systems quickly fall out-of-date and continually have to be manually
updated. In our approach, called WikEar, data mined from Wikipedia is automatically organized
according to principles derived from narrative theory to woven into an educational audio tours starting
and ending at stationary city maps. The system generates custom, location-based “guided tours” that are
never out-of-date and ubiquitous – even at an international scale. WikEar uses a magic lens-based
interaction scheme for paper maps, which have been shown to be particularly important in the tourist
experience. By leveraging on the wide availability of large public city maps, WikEar avoids the costs of
GPS and the interaction problems of small screen map programs.
Keywords: Tour Guide, Wikipedia, Mobile Map Interaction, Mobile Device

1 Introduction
According to a Berlin tour guide with whom we talked about WikEar, many tourists would appreciate at
least something of an educational experience out of their expensive efforts to see the world. These tourists
need more than the place names and directions provided by Google Maps or a GPS-based device.
Currently, they have two options – paper guidebooks and customized, highly localized mobile device
applications – both of which have severe content limitations and are not available for many locations.
Writing, editing and post-production of content in these types of tourism tools can be expensive and
overwhelming. In addition, the content can quickly become out-of-date. WikEar is an attempt to wed the
pervasive and easily-updated content of a mobile map application with the educational capabilities of a
guidebook. The content is one of the key factors for such applications.
The premise of WikEar is quite simple: The user stands in front of a public city map and selects a spatial
feature (such as a building or landmark) using her camera phone as a magic lens, as described in [1]. A
guided audio, narrative-based tour between the location of the city map and the destination is then delivered
to the user, with the intent that she will listen to the story as she travels to the destination. To track the
mobile device relative to the map we use the magic lens tracking technology of Rohs [2], which combines
the high-resolution visual context of paper maps with the dynamic information capabilities of mobile
technology.
The guided tour comes in the form of a narrative that is automatically mined from Wikipedia by the
Minotour system [3]. The output is rendered in audio form using text-to-speech (TTS) technology. As in
[3], we follow the advice of Isbister and Doyle [4], Lanegran [5], and others, and assume that the best tours
are those that weave a story as one travels through the landscape. This is our basis for implementing

narrative theory methods into our tour generation algorithms, a process that will be described in more detail
later. The goal is that users of WikEar will know about historical and current themes present in the regions
they have visited.
Finally, it is important to note that by combining city maps with guidebook-like content, we meet the call
of Brown and Chalmers [6], who suggest that one of the greatest challenges in mobile tourism technology
is greater integration of paper maps and electronic guidebooks.

2 Related Work
WikEar builds on the WikEye project [7], which makes accessible Wikipedia-derived content with a magic
lens interface for a paper map. Like WikEar, the goal of WikEye is helping users to understand more about
their surroundings via an easy to use mobile interface. For example, when a WikEye user views a small
portion of a Berlin paper map through the camera phone – like the area containing the Reichstag building
and the Brandenburg Gate – Wikipedia content is overlaid on the camera image of the map, highlighting
these spatial objects and their relationships. Following a clock metaphor, rotating the device about the
camera axis switches to a different time in history and delivers an overview of content related to that time
period. Depending on the spatial extent of the map visible on the camera display unit, the system responds
by offering Wikipedia data about spatial objects with larger area footprints. In other words, as the
cartographic scale decreases, the threshold area of a spatial object to be featured with Wikipedia data
increases. While WikEye concentrates on the interaction within a single map, WikEar is a bridge between
two or more maps, a concept that will be elaborated upon in the next section. WikEar also differs in its
approach to content. While WikEar utilizes whole narratives from the Minotour project, WikEye is limited
to much simpler forms of educating the user with Wikipedia data.

3 Interaction Pattern
Imagine you are a tourist in a city or a region and want to learn about the place you are visiting. You find a
public city map and hold your camera-enabled cell phone up to the map. You then select your destination,
probably one of the city’s or region’s more famous locations. A story designed to match your start location,
destination, and traveling time is then delivered to your phone over the Internet, ready for you to listen to
the parts of the story as you head towards your destination, interspersed with directional guidance. The
actual guidance is not part of WikEar yet, but could leverage existing tour guide technology [11]. Once you
reach your destination you can find another city map and repeat the process or access another tour you have
already pre-downloaded.
A key benefit of this interaction framework is the independence afforded to the tourist. The tourist is not
limited to prescribed tour paths or restricted by a paucity of available content. In fact, the only check on the
tourist’s movement is that, due to the algorithms used in tour generation, the start (location of the map) and
end destinations must have associated and geotagged Wikipedia articles – which might even have been
written prior to the trip by the tourist herself. As such, WikEar, as an instance of mobile tourism
technology, is in line with Weiser’s vision of Ubicomp [8] in that technology should be much more
supportive of spontaneous choices and desire for flexibility.

4 Narrative Theory Approach and Wikipedia “Story Mining”
As is noted in the introduction, Lanegran [5] and researchers in the field of intelligent narrative
technologies state that a successful educational tour is one that weaves a story as one travels through the
landscape. As such, the optimal approach to automatic educational tour generation is one that gives
narrative a central role. However, before explicating the algorithm used to generate guided tour narratives
from Wikipedia it is first necessary to highlight some characteristics of Wikipedia.

Fig. 1. (i) The ideal Narrative Function. The narrative algorithm chooses the path through the Wikipedia graph that
most resembles this function. (ii) A diagram depicting the operation of the path finding portion of the narrative
algorithm. Once found, the paths are evaluated by narrative-theory informed function. Finally, the narrative with the
best output (the one most similar to the optimal narrative(i)) is selected.

Aside from being the largest-ever compilation of user-contributed human knowledge, Wikipedia has three
other important features that we exploit in WikEar:
1) From a geospatial viewpoint, Wikipedia can be split up into two types of articles, two of which are
vital to the understanding of our algorithmic approach to narrative generation: georeferenced
articles and non-georeferenced articles.
2) Because Wikipedia is collaboratively edited, the average Wikipedia article is contributed to by at
least seven different authors [9]. This fact, in combination with the encyclopedic tone of nearly all
of Wikipedia, allows for self-contained paragraphs that are extremely disconnected from each
other. This allows us to treat Wikipedia paragraphs as individual entities we have named snippets,
and re-order them in any way our algorithm demands.
3) Wikipedia has an elaborate graph structure, a fact that is at the very center of our narrative
generation approach. We define the “Wikipedia graph” W as the set of Wikipedia articles and the
associated link structure.
The goal of our algorithm is to find the path through W between the articles about the start and destination
spatial features that most resembles the optimal path we have defined according to our approach to
narratology. We then take the snippets hosting the links in the nearest-to-optimal path and present them in
order to the user as a guided tour. In other words, the algorithm optimally queries and restructures
Wikipedia’s content to (1) provide location-based information, and (2) to do so in a way that can be
perceived as a narrative. In this re-structuring process, the snippet is treated as atomic. The algorithm
determines the number of snippets to include in each tour using an estimate of the travel time between the
start and end destinations, thus preventing us from using standard shortest-path solutions to this problem.
The snippets are converted to audio using text-to-speech technology, admittedly a drawback in user
experience given the current state of that technology. In our prototype, we have used actors to make
listening to the tours more enjoyable.
How do we define the “optimal path” through W? According to our adaption of narrative theory, the
optimal narrative is the one that best integrates the structural cues of unity and development into the
generated text. In our current prototype version of the algorithm, we have found that such an optimal
narrative can be approximated as in figure 1(i), using number of inlinks (indegree in W) as the primary
variable.

5 Implementation
Wikear is fully implemented for Nokia mobile camera phones (S60 3rd edition). While mining for the
optimal narrative takes place online, the procedure is supported by an extensively parsed database of
Wikipedia information, the result of a large offline pre-processing step. The input to this step is one of the
frequent Wikipedia dumps, which contain a “snapshot” of Wikipedia, i.e. all the text of every article in
Wikipedia at a given cut-off point in time. With minor modifications, our parser will work with Wikipedia

dumps of any Wikipedia-supported language, although at the moment we have built in support for only
English and German, Wikipedia’s two largest encyclopedias. Our device tracking implementation is almost
identical to that described in [2]: we use a printed grid of small black dots over the map to track a mobile
device with low latency and high precision.

6 Conclusion
We have presented a prototype system that leverages Wikipedia’s extensive content and structure in an
effort to fill a gap in the mobile tourism technology field. While it will require better text-to-speech for
wide-scale adoption, WikEar successfully demonstrates our data and methodology approaches. It is
important to note that we have also implemented an application that requires a great deal of spatial context
without any GPS technology at all, greatly reducing the cost on the user side. In addition, tourism boards
simply need to outfit their existing network of city maps with marker-enhanced maps in order to support
WikEar. The total cost is thus much less than that of every user having to buy spatial data and a GPS
system, and accessibility is much greater.
WikEar incorporates many new concepts that give rise to a plethora of ideas for refinements and further
work. First and foremost, we believe that while navigation is a solved problem [10] and thus not a high
research priority, it would be a necessary part of a user-ready version of WikEar. One possibility is to
implement landmark-based navigation technology, giving directions such as “head toward the big
building”, which is more conducive to how tourists prefer to navigate than using a street-based system [6].
Also, we have already begun investigating ways to improve our narrative generation process, as well as
looking into ways to evaluate generated narratives. Finally, we are also continually working on ways to
improve our tracking technology to the point where no obvious modifications are needed on the printed
map.

References
1. Schöning, J., Krüger, A., and Müller, H. J.: Interaction of Mobile Devices with Maps. In Adjunct Proceedings of the
4th International Conference on Pervasive Computing, Dublin, Ireland (2006).
2. Rohs, M., Schöning, J., Krüger, A., Hecht, B.: Towards Real-Time Markerless Tracking of Magic Lenses on Paper
Maps Pervasive 2007 Adjunct Proceedings, Late Breaking Results, Toronto, Ontario, Canada, May 13-16, (2007).
3. Hecht, B., Dara-Abrams, D., Starosielski, N., Goldsberry, K., Dillemuth, J. and Roberts, J.: Minotour: A Locationaware Mobile Tour Application that Weaves a Spatial Tale from Wikipedia. Proceedings of the 2007 Meeting of
The AAG, (2007).
4. Isbister, K. and Doyle, P.: Web Guide Agents: Narrative Context with Character. Narrative Intelligence. M. Mateas
and P. Sengers. Philadelphia, PA, John Benjamins Publishing Company: 229 – 243 (2003).
5. Lanegran, D.: Discussion on question, "What makes a good field trip?" B. Hecht. St. Paul, MN (2005).
6. Brown, B. and Chalmers, M.: Tourism and mobile technology. Eighth European Conference on Computer Supported
Cooperative Work, Helsinki, Finland (2003), Kluwer Academic Press.
7. Hecht, B., Rohs, M., Schöning, J., Krüger, A.: Wikeye – Using Magic Lenses to Explore Georeferenced Wikipedia
Content. Proceedings of the 3rd International Workshop on Pervasive Mobile Interaction Devices (PERMID),
Toronto, Ontario, Canada, May 13, (2007).
8. Weiser, M.: The Computer for the 21st Century. Scientific American 265(3), (1991) 66-75.
9. Buriol, L. S., Castillo, C.: Temporal Analysis of the Wikigraph. Web Intelligence, Hong Kong, China, IEEE CS
Press (2006).
10. Baus, J., Kray, C.: A survey of mobile guides. Workshop on Mobile Guides at: Mobile Human Computer
Interaction (2003).
11. Cheverst, K., Davies, N., Mitchell, K., Friday, A., and Efstratiou, C. 2000. Developing a context-aware electronic
tourist guide: some issues and experiences. In Proceedings of the SIGCHI Conference on Human Factors in
Computing Systems (The Hague, The Netherlands, April 01 - 06, 2000). CHI '00. ACM Press, New York, NY, 1724.
