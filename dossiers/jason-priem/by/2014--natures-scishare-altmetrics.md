---
title: "Why Nature’s “SciShare” experiment is bad for altmetrics"
person: jason-priem
section: by
type: blog-post
year: 2014
date: 2014-12-07
venue: "Impactstory blog"
authors: "Jason Priem"
source_url: https://blog.openalex.org/natures-scishare-altmetrics/
retrieved: 2026-08-13
content: full-text
notes: "Byline from WordPress author field (user 'jason') on the merged Impactstory/OurResearch/OpenAlex blog. Originally published on blog.impactstory.org."
---

# Why Nature’s “SciShare” experiment is bad for altmetrics

## Full text

\
Early last week, Nature Publishing Group [announced that 49 titles on Nature.com will be made free to read for the next year](http://www.nature.com/news/nature-makes-all-articles-free-to-view-1.16460). They’re calling this experiment “[SciShare](http://www.nature.com/press_releases/share-nature-content.html)” on social media; we’ll use the term as a shorthand for their initiative throughout this post.

[Some](https://twitter.com/ersatzben/status/539685051915849729) [have](https://twitter.com/thebookseller/status/539687129090371584) [credited](https://twitter.com/JonasGilbert/status/540152636432211968) Nature on their incremental step towards embracing Open Access. [Other](http://del-fi.org/post/104125242971/natures-shareware-moment) [scientists](http://www.michaeleisen.org/blog/?p=1668) [criticise](http://blogs.egu.eu/network/palaeoblog/2014/12/03/one-small-step-for-nature/) the company for diluting true Open Access and encouraging scientists to share DRM-crippled PDFs.

As staunch Open Access advocates ourselves, we agree with our board member [John Wilbanks](http://del-fi.org/post/104125242971/natures-shareware-moment): this ain’t OA. “Open” means open to anyone, including laypeople searching Google, who don’t have access to Nature’s Magic URL. “Open” also means open for all types of reuse, including tools to mine and build next-generation value from the scholarly literature.

But there’s another interesting angle here, beyond the OA issue: this move has real implications for the altmetrics landscape. Since we live and breathe altmetrics here at Impactstory, we thought it’d be a great time to raise some of these issues.

[Some](http://blogs.egu.eu/network/palaeoblog/2014/12/03/one-small-step-for-nature/) [smart](https://twitter.com/rmounce/status/540158727727632386) [people](https://twitter.com/GaviaLib/status/539616271391002625) have asked, “Is SciShare an attempt by Nature to ‘game’ their altmetrics?” That is, is SciShare an attempt to force readers to view content on Nature.com, thereby increasing total pageview statistics for the company and their authors?

Postdoc Ross Mounce [explains](http://rossmounce.co.uk/2014/12/02/beggar-access/):

If \[SciShare\] converts some [dark social](http://www.theatlantic.com/technology/archive/2012/10/dark-social-we-have-the-whole-history-of-the-web-wrong/263523/) sharing of PDFs into public, trackable, traceable sharing of research via non-dark social means (e.g. Twitter, Facebook, Google+ …) this will increase the altmetrics of Nature relative to other journals and that may in-turn be something that benefits Altmetric.com \[a company in which Macmillian, Nature’s parent company, is an investor\].

No matter Nature’s motivations, SciShare, as it’s implemented now, will have some unexpected negative effects on researchers’ ability to track altmetrics for their work. Below, we describe why, and point to some ways that Nature could improve their SciShare technology to better meet researchers’ needs.

## How SciShare works

SciShare is powered by ReadCube, a reference manager and article rental platform that’s funded by Macmillan via their science start-up investment imprint, [Digital Science](http://www.digital-science.com/what-we-do/start-up-investment).

Researchers with subscription access to an article on Nature.com copy and paste a special, shortened URL (i.e. <http://rdcu.be/bKwJ>) into email, Twitter, or anywhere else on the Web.

Readers who click on the link are directed to a version of the article that they can freely read and annotate in their browser, thanks to ReadCube. Readers cannot download, print, or copy from the ReadCube PDF.

The ReadCube-shortened URL resolves to a Nature-branded, hashed URL that looks like this:

![Screen Shot 2014-12-04 at 4.18.16 PM.png](https://lh6.googleusercontent.com/HZVl8mLDljD-4CWOtRdqn0pN9_ci315CUCLaS_UGspSS5K0NZfHfnMfu535nZMXun8WHvEr9aW2RiKchrQztIsnlfGAnsThviqFZKaijMFX6XN6LgshSyAT0-aIsOAzkXQ)

The resolved URL doesn’t include a DOI or other permanent identifier.

In the ReadCube interface, users who click on the “Share” icon see a panel that includes a summary of Altmetric.com powered altmetrics (seen here in the lower left corner of the screen):

![Screen Shot 2014-12-04 at 6.11.41 PM.png](https://lh3.googleusercontent.com/5p9uzjO81A6WUfXb9na6x6pi-mIzANVI7RXmz_U0r-sSlVCpbKe7pGdQNQviC1lvgNLS1iq-BJJP9Otu9FFmcjSSDg_1Cyf4v6YAn-8Gyw__WTPppd5_6bBoMynOXA1wMA)

The ReadCube-based Altmetric.com metrics do not include pageview numbers. ~~Because ReadCube doesn’t work with assistive technology like screen readers, it also disallows for the tracking of the small portion of traffic that visually-impaired readers might account for.~~

That said, the potential for tracking new, ReadCube-powered metrics is interesting. ReadCube allows annotations and highlighting of content, and could potentially report both raw numbers and also describe the contents of the annotations themselves.

Number of redirects from the ReadCube-branded, shortened URLs could also be illuminating, especially when reported alongside direct traffic to the Nature.com-hosted version of the article. (Such numbers could provide hard evidence as to the proportion of OA vs toll access use of Nature journal articles.) And sources of Web traffic give a lot of context to the raw pageview numbers, as we’ve seen from publishers like *[PeerJ](https://peerj.com/articles/599/#metricsModal)*:

![Screen Shot 2014-12-04 at 6.26.31 PM.png](https://lh3.googleusercontent.com/atOFLXeMfw45cBlUqfGZNcOF4UE1rX8usxUrswtpiC7mykwXRoYLxvn7gUGC7ymcyT-zlWbFHjPXm_ZVxcAagplVgKqFtM7Ty9hHsr3MDkbj6rtwSzmcgyIVNzEvkX2ZCw)

After all, referrals from Reddit usually means something very different than referrals from PubMed.

Digital Science’s Timo Hannay [hints](http://www.digital-science.com/blog/news/nature-com-content-sharing-action-and-reaction/) that Nature will eventually report download metrics for their authors. There’s no indication as to whether Nature intends to disclose any of the potential altmetrics described above, however.

So, now that we know how SciShare works and the basics of how they’ve integrated altmetrics, let’s talk about the bigger picture. What does SciShare mean for researcher’s altmetrics?

## How will SciShare affect researchers’ altmetrics?

Let’s start with the good stuff.

Nature authors will probably reap a big benefit in thanks to SciShare: they’ll likely have higher pageview counts for the Nature.com-hosted version of their articles.

Another positive aspect of SciShare is that it provides easy access to Altmetric.com data. That’s a big win in a world where not all researchers are aware of altmetrics. Thanks to ReadCube’s integration of Altmetric.com, now more researchers can find their article’s impact metrics. (We’re also pleased that Altmetric.com will get a boost in visibility. We’re big fans of their platform, as well as customers–Impactstory’s Twitter data comes from Altmetric.com).

SciShare’s also been implemented in such a way that the ReadCube DRM technology doesn’t affect researchers’ ability to bookmark SciShare’d articles on reference managers like Mendeley. Quick tests for Pocket and Delicious bookmarking services also seems to work well. That means that social bookmarking counts for an author’s work will likely not decline. (I point this out because when I attempted to bookmark a ReadCube.com-hosted article using my Mendeley browser bookmarklet Thursday, Dec. 4th, I was prevented from doing so, and actually redirected to a ReadCube advertisement. I’m glad to say this no longer seems to be true.)

Those are the good things. But there’s also a few issues to be concerned about.

### SciShare makes your research metrics harder to track

The premise of SciShare is that you’ll no longer copy and paste an article’s URL when sharing content. Instead, they encourage you to share the ReadCube-shortened URL. That can be a problem.

In general, URLs are difficult to track: they contain weird characters that sometimes break altmetrics aggregators’ search systems, and they go dead often. In fact, there’s no guarantee that these links will be live past the next 12 months, when the SciShare pilot is set to end.

Moreover, neither the ReadCube URL–nor the long, hashed, Nature.com-hosted URL that it resolves to–contain the article’s DOI. DOIs are one of the main ways that altmetrics tracking services like ours at Impactstory can find mentions of your work online. They’re also preferable to use when sharing links because they’ll [always resolve to the right place](http://blog.impactstory.org/impact-challenge-dois/).

So what SciShare essentially does is introduce two new messy URLs that will shared online, and that have a high likelihood of breaking in the future. That means there’s a bigger potential for messier data to appear in altmetrics reports.

### SciShare’s metrics aren’t as detailed as they could be

The Altmetric.com-powered altmetrics that ReadCube exposes are fantastic, but they lack two important metrics that other data providers expose: citations and pageviews.

On a standard article page on Nature.com, there’s an Article Metrics tab. The Metrics page includes data not only from Altmetric.com, but also CrossRef, Web of Science, and Scopus’s citation counts, and also pageview counts. And on completely separate systems like Impactstory.org and PlumX, still more citation data is exposed, sourced from Wikipedia and PubMed. (We’d provide pageview data if we could. But that’s currently not possible. More on that in a minute.)

ReadCube’s deployment of Altmetric.com data also decontextualizes articles’ metrics. They have chosen only to show the summary view of the metrics, with a link out to the full Altmetric.com report:

![Screen Shot 2014-12-05 at 10.11.47 AM.png](https://lh6.googleusercontent.com/MhsuNdlgG4O8B45jqwqWlUCFTqYAKbdUkYkZXuVmls-j03KS5DhlUST_MJs1dxdrk6Be4MxDZa_m4q5Qb7eCOg9VwN0WhE06B5k3gvBao4TQM9i02AJ9Il0W7JQVkvoDwQ)

Compare that to what’s available on Nature.com, where the Metrics page showcases the Altmetric.com summary metrics plus Altmetric.com-sourced Context statements (“This article is in the 98th percentile compared to articles published in the same journal”), snippets of news articles and blog posts that mention the article, a graph of the growth in pageviews over time, and a map that points to where your work was shared internationally:

![Screen Shot 2014-12-04 at 3.59.38 PM.png](https://lh3.googleusercontent.com/cRdcUVRfd1THqsbUP-66LW1G-S38zfjgaZMJgH_bQwAbnZwzR60WEreUXyM-vj5iltVb7nswkm9GhCgVcuZppphZv4izXsVSBF0XEcHKsExRs7RWyehVQbsc3Xa1dCNZLA)

More data and more context are very valuable to have when presenting metrics. So, we think this is a missed opportunity for the SciShare pilot.

### SciShare isn’t interoperable with all altmetrics systems

Let’s assume that the SciShare experiment results in a boom in traffic to your article on Nature.com. What can you do with those pageview metrics?

Nature.com–like most publishers–doesn’t share their pageview metrics via API. That means you have to manually look up and copy and paste those numbers each time you want to record them. Not an insurmountable barrier to data reuse, but still–it’s a pain.

Compare that to PLOS. They freely share article view and download data via API, so you can easily import those numbers to your profile on Impactstory or PlumX, or export them to your lab website, or parse them into your CV, and so on. (Oh, the things you can do with open altmetrics data!)

You also cannot use the ReadCube or hashed URLs to embed the article full-text into your Impactstory profile or share it on ResearchGate, meaning that it’s as difficult as ever to share the publisher’s version of your paper in an automated fashion. It’s also unclear whether the “personal use” restriction on SciShare links means that researchers will be prohibited from saving links publicly on Delicious, posting them to their websites, and so on.

## How to improve SciShare to benefit altmetrics

We want to reiterate that we think that SciShare’s great for our friends at Altmetric.com, due to their integration with ReadCube. And the greater visibility that their integration brings to altmetrics overall is important.

That said, there’s a lot that Nature can do to improve SciShare for altmetrics. The biggest and most obvious idea is to do away with SciShare altogether and simply make their entire catalogue Open Access. But it looks like Nature (discouragingly) is not ready to do this, and we’re realists. So, what can Nature do to improve matters?

- **Open up their pageview metrics via API** to make it easier for researchers to reuse their impact metrics however they want
- **Release ReadCube resolution, referral traffic and annotation metrics via API,** adding new metrics that can tell us more about how content is being shared and what readers have to say about articles
- **Add more context to the altmetrics data they display,** so viewers have a better sense of what the numbers actually mean
- **Do away with hashed URLs and link shorteners,** especially the latter which make it [difficult to track all mentions of an article on social media](http://doi.org/10.2196/jmir.2012)

We’re hopeful that SciShare overall is an incremental step towards full OA for Nature. And we’ll be watching how the SciShare pilot changes over time, especially with respect to altmetrics.

**Update: **Digital Science [reports](http://www.digital-science.com/blog/news/clearing-up-misperceptions-about-nature-com-content-sharing/) that the ReadCube implementation has been tested to ensure compatibility with most screen readers.
