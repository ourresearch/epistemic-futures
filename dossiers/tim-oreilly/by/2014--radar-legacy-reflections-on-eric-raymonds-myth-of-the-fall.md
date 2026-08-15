---
title: "Reflections on Eric Raymond’s “Myth of the Fall”"
person: tim-oreilly
section: by
type: blog-post
year: 2014
date: 2014-03-04
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/2014/03/reflections-on-eric-raymonds-myth-of-the-fall.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# Reflections on Eric Raymond’s “Myth of the Fall”

## Full text

Eric Raymond’s “[Myth of the Fall](http://esr.ibiblio.org/?p=5277),” an account of the rise of software portability and reusable open source code (rather than the fall from a free software eden), should be required reading for free and open source developers, and for anyone who cares about the future of technology.

It exactly matches my experience working with Unix starting in the early eighties, although I’ve always talked about it from a somewhat different angle: because Unix was a portable operating system running on incompatible hardware, the only way you could distribute your free software was in source form. In other environments, while there was a “freeware” culture (just there is today on smartphone platforms), that was always binary freeware. You would just download the program and run it, whether you were on CP/M or DOS or the Mac. Only on Unix did you have to compile the source code into binaries for your brand of machine. The reason open source culture grew from Unix was not political, it was _architectural_.

And because 9-track tapes were a bitch to ship around, and it took forever to send around programs (even the relatively tiny ones of the day) on slow networks, we used tools like [Patch](http://en.wikipedia.org/wiki/Patch_\(Unix\)) to share just the modified code as tracked by version control systems. Unix’s [philosophy of portability](http://en.wikipedia.org/wiki/The_Unix_Programming_Environment), which included not just a programming language (C) optimized for portability, but also an architecture of small, modular programs communicating using standardized rules for input and output, also shaped the design of the internet and applications like email and the World Wide Web that grew on top of it.

Understanding this history correctly can give deep insight into the role of architecture in making projects succeed. I’ve been thinking about this lately in the context of open data.

If you think about open data from a political “data must be free” perspective, you will come up with projects like [identi.ca](http://identi.ca) and [app.net](http://app.net). If you think about it from a “useful interoperability” perspective, you will come up with standards like [GTFS](http://sf.streetsblog.org/2010/01/05/how-google-and-portlands-trimet-set-the-standard-for-open-transit-data/) (which cities use to provide their transit schedules to Google Maps and others), [Blue Button](http://www.healthit.gov/bluebutton) (which started at the VA as a program for veterans, but now allows consumers to download their medical records), not to mention the [government open data](http://www.mckinsey.com/insights/business_technology/open_data_unlocking_innovation_and_performance_with_liquid_information) in areas like mapping, weather, and location data that powers so many commercial services today.

Ultimately, utility too can be a kind of politics. The internet is a testament to the power of open, interoperable architectures to create a platform for innovation and value creation. As we move ever deeper into the era of data driven computing, that’s an essential lesson.

Will the Internet of Things be proprietary or open? It seems to me that the best way to ensure that the answer to that question is “open” is not to wave banners saying “open data” or to try to create open versions of successful proprietary products but to work assiduously to find ways in which open data and cooperating systems create more value than closed, proprietary data.
