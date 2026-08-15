---
title: "Open Communities vs. Open Source"
person: tim-oreilly
section: by
type: blog-post
year: 2006
date: 2006-07-28
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/archives/2006/07/open_communities_vs_open_sourc_1.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# Open Communities vs. Open Source

## Full text

At an [OSCON](http://conferences.oreilly.com/oscon) panel yesterday, there was a really interesting conversation between [Danese Cooper](http://danesecooper.blogs.com/divablog/) and [Dain Sundstrom](http://www-128.ibm.com/developerworks/websphere/library/techarticles/0511_sundstrom/0511_sundstrom.html). We were talking about what happens when money arrives at an open source project (either in the form of corporate sponsors or commercialization of the project itself.) 

[Mitchell Baker](http://weblogs.mozillazine.org/mitchell/) pointed out how hard it was for AOL to understand that she was still the project leader when they laid her off from Netscape. It took a concerted effort by the remaining Netscape developers to help them realize that she was still their leader, despite AOL's new organizational plans. I had been making a similar point to Laurie Tolson, the new head of Java at Sun, in discussing how Sun would have to change their thinking if they were to open source Java. Open source projects are typically headed by individuals, and in [cluetrain](http://www.cluetrain.org) style, depend on having a human face.

Dain made a really interesting distinction. We need to recognize, he pointed out, that open source doesn't guarantee open community. Some projects (JBoss was what he had in mind) are open source, but have a closed community, controlled by a corporate sponsor.

If you leave the company, you perhaps leave the project as well. Keeping in mind what had happened when they left JBoss, the Geronimo developers held up the sale of Gluecode (the company they'd formed to commercialize Geronimo, their fork of JBoss) to IBM to make sure that they had the contractual right to continue to work on the project, even if they left IBM.

Of course, there are gradations of open. Java is a good example. Its community process is not as closed as that of JBoss or MySQL, but it's still clearly dominated by a corporate entity that sets the rules. (But the vibrancy of Java development outside of Sun still shows us that a relatively open architecture (albeit bloated in many parts) and a relatively open community can get many of the benefits of open source without an open source license.)

This discussion reminded me of a point that I've long made, that open source licenses are only one dimension of the open source phenomenon. Besides open community, there's also open architecture. Some projects have monolithic codebases that are hard for developers to engage with, while others have modular "[architectures of participation](http://www.oreillynet.com/pub/wlg/3017)." Linux (at the distribution level) has this in spades: anyone who writes an open source program is contributing it to the Linux ecosystem, which pulls it into its orbit much like a solar system does its satellites. There is a gravitational core, but no boundary. The internet, too, has this kind of architecture. Meanwhile, many of the most successful open source projects also have well-developed extension mechanisms: Apache, Mozilla, Perl, PHP... 

I'm particularly mindful of the lessons of Mozilla. When Netscape first released its browser as open source, it was a typical monolithic corporate application, very hard for developers to get their heads around. The Mozilla team made the difficult decision to spend a couple of years reworking the project to make it more approachable. Thus Firefox was born from what appeared to be the ashes. And besides being based on Mozilla's modular building blocks, Firefox has a great extension mechanism.

OpenOffice.org is a good counter-example. While it's extensible, the developers never took the time that Mozilla took to make the original closed, monolithic application into something that was more approachable for developers. I believe that this has hampered its development.

Apache is also a great teacher. Back in the mid-90s, when the web server wars were still going on, Apache was faulted for not adding features like Netscape or Microsoft's web servers. Apache stayed small, focused on core web server functionality, and with its extension mechanisms and process, became the server platform of choice. 

Modular architectures enable individual developers and small teams, and are generally much more hackable. These two factors are critical to open source success.

This thinking leads to a model a bit like the "[levels of the game](http://radar.oreilly.com/archives/2006/07/levels_of_the_game.html)" that I recently put forward for Web 2.0:

Level 3: The project has an open source license, an open community (anyone can contribute, and it's purely a meritocracy), and a modular architecture. Linux, Apache, Mozilla, Perl, Python, Ruby, PHP all meet this test.

Level 2: The project has an open source license but not an open community. MySQL and JBoss are examples.

Level 1: The project has an open source license, but a monolithic architecture. And because it has a monolithic architecture, it usually has a closed community as well. Sendmail is a good example. OpenOffice.org is an example of a project with an open source license, a monolithic architecture, and an open community. 

I probably am mischaracterizing some of these projects and will get a lot of heat as a result, but I hope to provoke some thoughtful discussion as well.
