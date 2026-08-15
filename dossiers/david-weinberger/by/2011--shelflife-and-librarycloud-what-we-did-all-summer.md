---
title: "ShelfLife and LibraryCloud: What we did all summer"
person: david-weinberger
section: by
type: blog-post
year: 2011
date: 2011-10-04
venue: "Joho the Blog (hyperorg.com)"
authors: "David Weinberger"
source_url: https://hyperorg.com/2011/10/04/shelflife-and-librarycloud-what-we-did-all-summer/
retrieved: 2026-08-13
content: full-text
notes: "Post from Joho the Blog (hyperorg.com), Weinberger's personal blog. Retrieved via the site's WordPress REST API; HTML converted to plain text."
---

# ShelfLife and LibraryCloud: What we did all summer

## Full text

We’re really really really pleased that the Digital Public Library of America has chosen two of our projects to be considered (at an Oct. 21 open plenary meeting) for implementation as part of the DPLA’s beta sprint. The Harvard Library Innovation Lab (Annie Cain, Paul Deschner, Jeff Goldenson, Matt Phillips, and Andy Silva), which I co-direct (along with Kim Dulin) worked insanely hard all summer to turn our prototypes for Harvard into services suitable for a national public library. I have to say I’m very proud of what our team accomplished, and below is a link that will let you try out what we came up with.

Upon the announcement of the beta sprint in May, we partnered up with folks at thirteen other institutions…an amazing group of people. Our small team at Harvard , with generous internal support, built ShelfLife and LibraryCloud on top of the integrated catalogs of five libraries, public and university, with a combined count of almost 15 million items, plus circulation data. We also pulled in some choice items from the Web, including metadata about every TED talk, open courseware, and Wikipedia pages about books. (Finding all or even most of the Wikipedia pages about books required real ingenuity on the part of our team, and was a fun project that we’re in the process of writing up.)

The metadata about those items goes into LibraryCloud, which collects and openly publishes that metadata via APIs and as linked open data. We’re proposing LibraryCloud to DPLA as a metadata server for the data DPLA collects, so that people can write library analytics programs, integrate library item information into other sites and apps, build recommendation and navigation systems, etc. We see this as an important way what libraries know can become fully a part of the Web ecosystem.

ShelfLife is one of those possible recommendation and navigation systems. It is based on a few basic principles hypotheses:

– The DPLA should be not only a service but a place where people can not only read/view items, but can engage with other users.

– Library items do not exist on their own, but are always part of various webs. It’s helpful to be able to switch webs and contexts with minimal disruption.

– The behavior of the users of a collection of items can be a good guide to those items; we think of this as “community relevance,” and calculate it as “shelfRank.”

– The system should be easy to use but enable users to drill down or pop back up easily.

– Libraries are social systems. Library items are social objects. A library navigation system should be social as well.

Apparently the DPLA agreed enough to select ShelfLife and LibraryCloud along with five other projects out of 38 submitted proposals. The other five projects — along with another three in a “lightning round” (where the stakes are doubled and anything can happen??) — are very strong contenders and in some cases quite amazing. It seems clear to our team that there are synergies among them that we hope and assume the DPLA also recognizes. In any case, we’re honored to be in this group, and look forward to collaborating no matter what the outcome.

You can try the prototype of ShelfLife and LibraryCloud here. Keep in mind please that this is live code running on top of a database of 15M items in real time, and that it is a prototype (and in certain noted areas merely a demo or sketch). I urge you to talk the tour first; there’s a lot in these two projects that you’ll miss if you don’t.
