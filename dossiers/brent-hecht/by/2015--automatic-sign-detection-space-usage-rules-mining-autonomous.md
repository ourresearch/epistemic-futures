---
title: "From Automatic Sign Detection To Space Usage Rules Mining For Autonomous Driving"
person: brent-hecht
attendance: unconfirmed
section: by
type: conference-paper
year: 2015
date: 2015-01-01
venue: "Document Server@UHasselt (UHasselt)"
authors: "Pavel Samsonov, Brent Hecht, J. Schoening"
source_url: http://hdl.handle.net/1942/19049
fulltext_url: https://documentserver.uhasselt.be/bitstream/1942/19049/1/CHI-2015-Automated-Cars-Workshop-Paper.pdf
openalex_id: W2468118343
oa_status: closed
cited_by_count: 3
retrieved: 2026-08-13
content: full-text
notes: "Full text from the green-OA copy in Document Server@UHasselt (pdftotext; PDF not stored)"
---

# From Automatic Sign Detection To Space Usage Rules Mining For Autonomous Driving

## Full text

Made available by Hasselt University Library in https://documentserver.uhasselt.be

From Automatic Sign Detection To Space Usage Rules Mining For
Autonomous Driving
Peer-reviewed author version
SAMSONOV, Pavel; Hecht, Brent & SCHOENING, Johannes (2015) From
Automatic Sign Detection To Space Usage Rules Mining For Autonomous Driving.
In: Proceedings of the Workshop on Experiencing Autonomous Vehicles: Crossing
the Boundaries between a Drive and a Ride at ACM CHI.
Handle: http://hdl.handle.net/1942/19049

From Automatic Sign Detection To
Space Usage Rules Mining For
Autonomous Driving
Pavel Samsonov

Abstract

Expertise Centre for Digital Media

While there is a large body of related work on the
automatic detecting of road signs for (semi-)
autonomous vehicles, we believe that these vehicles
should also be aware of so-called “space usage rules”
(SURs) more generally. Vehicles that understand SURs
– e.g. “no swimming”, “no drone flying”, - could
provide a novel set of context-aware services for
autonomous driving. For instance, an autonomous car
navigation system could provide directions to the
nearest beach, where swimming is allowed, or the
system itself could know if it is allowed to send out its
drone to get an overview on the current traffic situation
ahead. In this workshop paper, we outline two
techniques to mine these SURs. We present a visionbased technique and a technique utilizing user
interfaces for encoding SUR expressed in natural
language into a machine-readable format.

Hasselt University - tUL - iMinds
pavel.samsonov@uhasselt.be
Brent Hecht
Computer Science and Engineering
University of Minnesota
bhecht@cs.umn.edu
Johannes Schöning
Expertise Centre for Digital Media
Hasselt University - tUL – iMinds
johannes.schoening@uhasselt.be

Copyright held by authors, 2015

Author Keywords
Space usage rules; Context-aware applications; Map
applications; (Semi-) autonomous vehicles.

ACM Classification Keywords
H.5.m. Information interfaces and presentation (e.g.,
HCI): Miscellaneous. User interfaces; Graphical user

interfaces (GUI);
Interaction styles.

Input

devices

and

strategies;

Introduction & Motivation
SURs, which are broadly defined to be rules and
regulations that are spatially-constrained in nature,
range from everyday restrictions like “no parking
between 8pm and 8am” to less common restrictions
like “do not use the horn” [9]. Besides “traditional”
traffic sign detection, which has been extensively
researched in the field of computer vision ([1], [2],
[7]), we believe that future (semi-) autonomous
vehicles should incorporate SURs beyond traffic sign
information in their systems to provide a safe and
enjoyable travel experience.
By incorporating SURs into automobile navigation
systems, various other novel context-aware services for
autonomous driving could also be easily implemented.
The car itself could figure out “routes with nearby
beaches to swim or surf” or “the next park, where I can
walk my dog”. As space usage restrictions like “no
swimming” or “no dogs” could also be posted on signs,
we briefly describe our vision-based technique [9]
below.
For example, Renault recently announced a new car
concept with a drone companion on-board 1. The drone
can be used to observe and monitor the traffic situation
ahead and feed the data from its patrols back to the
navigation system. However, in order for its drone to
be used, the car system needs to know if in its current
position it is legal to fly a drone. In the U.S., the use of
1

http://www.theverge.com/2014/2/7/5389114/renault-kwiddrone-car-concept

drones is currently forbidden nearby airports and
national monuments. Other and more complex dronerelated SURs apply in different countries and
municipalities around the globe. As such, information
about drone-related SURs needs to be included in such
car’s navigation system.
As it is unlikely that visual signs indicating dronerelated SURs will be posted next to the road, we
propose a technique utilizing a system for encoding
SURs expressed in natural language (in legal
documents) into a machine-readable format. We are
developing
an
“if-this-then-that”-style
interface
described later in this paper that allows people without
programming experience to create these machine
readable SURs, with the goal of enabling the
crowdsourcing of SURs around the world.
By applying both, we believe that it is possible to mine
a large dataset of SURs that could be incorporated into
car navigation systems to exploit novel context aware
services and improve the driving experience.

Related Work
In our previous work [10] we pointed out the lack of
space usage rule (SUR) data in today’s online and
mobile map services. While the vector geographical
information in OpenStreetMap (OSM) has extensive
coverage and high quality in many places (e.g. [4] and
[8]), space usage rule OSM tag data such as “no
smoking” and “no dogs” is very sparse. Less wellknown rules have even lower coverage. For instance,
only 57 features in the whole world in OSM are tagged
as “no-fishing”. Gathering SUR information represents a
hard and very expensive task, and the information
needs to be updated relatively often.

Two methods how to gather SUR
In this workshop paper, we propose two ways to collect
SURs: a vision-based technique and a technique
utilizing user interface for encoding SURs expressed in
natural language into a machine-readable format. The
vision-based technique will be also presented at the
main CHI conference [9].
A vision-based approach to gather SUR
As noted in the introduction, modern car navigation
systems should be aware not just of the limitations on
the roads, but also of the limitations in the destination
points and the surrounding areas. The more
information is available, the better the services that can
be provided to the user. Examples include limitations in
the entertainment or leisure facilities as noted above
(e.g. no swimming, no dogs in certain parks) as well as
information about parking places and so on. All this
information can be retrieved from signs in the
environment.
Our vision-based approach identifies SUR signs data in
geotagged photos published on public image sharing
resources such as Flickr 2 and assigns them to
geographical features. This SUR mining approach is
fully automatic. First, geotagged images are crawled
from the Internet and processed to find SUR signs in
them. Then, the extracted SUR signs are mapped to a
geographical feature in OSM. For a detailed overview
on this technique we please refer to [9].

2

http.flickr.com

Figure 1. The if-this-then-that interface.

A user interface for encoding SUR expressed in natural
language into a machine-readable format.
In the introduction, we discuss that some signs, such
as “no drones allowed”, are not posted, so they cannot
be extracted from images. Therefore, we are
developing a user interface to support the semiautomatic encoding of SURs expressed in natural
language in documents such as laws, city ordinances,
park rules, and institution FAQ pages. With the help of
this “if-this-then-that”-style interface (see Figure 1) the
conversion of a SUR expressed in natural language can
be directly done by people not familiar with
programming. We hope to deploy this interface to
crowdworkers on Mechanical Turk in the near future.
Our system works by converting user-entered SURs
into Lua code. The system then maps the rules
expressed in Lua to the appropriate geographic regions
(using geographic data from OpenStreetMap). This
information is then written into a database, which could
then be easily imported into a car navigation system. We
are also working to partially automate this process

using lightweight natural language processing and
geoparsing (e.g. [3], [5]).
As car navigation systems require highly accurate data,
the data gathered with both methods needs verification
before it can be used. Also, the data needs to be
regularly checked for outdated rules and needs to be
updated alongside the map data. We plan to assign
each rule in the database a “trust level” mark, based on
how many signs and rules state it to be true and the
date of last modification. In the crowdsourcing case,
several workers will be given the same natural
language rule to check if they complete it in the same
way.

Conclusion
In this paper, we discussed why space usage rules
could become an important component for automatic
car navigation systems. Incorporating SURs in the
databases of future (semi-) autonomous vehicles will
provide a rich set of novel context-aware services for
autonomous
driving
that
will
improve
travel
experiences. We have presented an automatic and a
semi-automatic approach for gathering SUR data. We
believe that combination of both techniques provides a
good step forward for making SURs accessible for
future autonomous vehicles.

References
[1] Bahlmann, C., Zhu, Y., Ramesh, V., Pellkofer, M., &
Koehler, T. (2005, June). A system for traffic sign
detection, tracking, and recognition using color, shape,
and motion information. Intelligent Vehicles
Symposium, 2005. Proc. IEEE (pp. 255-260).
[2] De La Escalera, A., Moreno, L. E., Salichs, M. A., &
Armingol, J. M. (1997). Road traffic sign detection and

classification. Industrial Electronics, IEEE Transactions
on, 44(6), 848-859.
[3] Gelernter, J., and Mushegian, N. Geo-parsing
Messages from Microtext. Transactions in GIS 15.6
(2011): 753-773.
[4] Haklay, M. How good is volunteered geographical
information? A comparative study of OpenStreetMap
and Ordnance Survey datasets. Environment and
planning. B, Planning & design 37.4 (2010): 682.
[5] Hoffart, J., Yosef, M., Bordino, I., Fürstenau, H.,
Pinkal, M., Spaniol, M., Taneva, B., Thater, S. and
Weikum, G. Robust disambiguation of named entities in
text. Proc of EMNLP (2011).
[6] Ierusalimschy, R., Henrique de Figueiredo, L.,
Celes, W. The Evolution of Lua. Proceedings of the
Third ACM SIGPLAN Conference on History of
Programming Languages, HOPL III, pp. 2-1-2-26. ACM,
New York (2007).
[7] Lopez, L. D., & Fuentes, O. (2007). Color-based
road sign detection and tracking. Image analysis and
recognition (pp. 1138-1147). Springer Berlin
Heidelberg.
[8] Mooney, P., Corcoran, P., Wistanley, A.C. Towards
Quality Metrics for OpenStreetMap. Proceedings of the
18th SIGSPATIAL International Conference on
Advances in Geographic Information Systems, ACM
(2010) 514–517.
[9] Samsonov, P., Tang, X., Schöning, J., Kuhn, W.
and Brent, H. You Can’t Smoke Here: Towards Support
for Space Usage Rules in Location-aware Technologies.
Proc. CHI, ACM Press (2015).
[10] Schöning, J., Hecht, B. and Kuhn, W. 2014.
Informing Online and Mobile Map Design with the
Collective Wisdom of Cartographers. DIS ’14.
