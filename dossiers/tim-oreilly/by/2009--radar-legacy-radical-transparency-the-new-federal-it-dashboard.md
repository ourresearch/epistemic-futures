---
title: "Radical Transparency: The New Federal IT Dashboard"
person: tim-oreilly
section: by
type: blog-post
year: 2009
date: 2009-06-30
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/2009/06/radical-transparency-federal-it-dashboard.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# Radical Transparency: The New Federal IT Dashboard

## Full text

Today, at the [Personal Democracy Forum](http://personaldemocracy.com/pdf-conference/personal-democracy-forum-conference) in New York, [Vivek Kundra](http://radar.oreilly.com/2009/03/vivek-kundra-federal-cio-in-hi.html), the US national CIO, unveiled the new [IT spending dashboards at usaspending.gov](http://it.usaspending.gov). The dashboards are designed to help Vivek and the CIOs of individual government agencies get a handle on the effectiveness of government IT spending. 

At the top level, the dashboards provide a view of spending by major government department, with graphs showing performance against schedule, costs, and the CIO's assessment of how well they are meeting their objectives. For example, here's a stark view of IT performance at the Veteran's Administration (click to expand image): 

[](http://radar.oreilly.com/upload/2009/06/VAToughLove.png)

49% of the VA's IT projects are behind schedule, and Roger Baker, the agency CIO, deems that a full 63% of the projects are in need of serious attention. (Here's a recent article that outlines [Baker's tough-love plans for IT at the Veteran's Administration](http://www.fiercegovernmentit.com/story/va-cio-wants-end-it-failures/2009-06-21).) 

As you drill down, you get to dashboards for individual IT projects (800 projects and approximately $20 billion in budgeted spending). Each project shows the responsible government official, the prime contractors on the project, the CIO's evaluation of its progress against goals, and each month, an update showing an update of that progress. (We'll show one of these later in this article.) 

The dashboards are an incredibly ambitious undertaking. In the first place, there has never been a government-wide view like this of all IT spending, and the progress of projects. What's even more remarkable, though, is that the dashboards are being shared with the public. It's a bit like having your performance review posted on the company bulletin board for all to see. 

In notes provided to press in advance of the announcement, Vivek Kundra wrote (italics mine): 

> Over the past several years, we have witnessed numerous public failures of major information technology systems and just last year saw roughly one third of all investments reported as poorly planned or poorly performing. Many of these investments may never deliver on their original promises. With over $75 Billion in annual federal information technology spending, we need a new foundation for management - one built on the values of transparency, accountability, and responsibility.... 
> 
> Data is powerful. It enables monitoring, reporting, and meaningful analysis that leads to better decisions. Yet, in the case of federal information technology, we lack insight into project performance. Poor data quality coupled with infrequent reporting has led to lack of meaningful analysis and bad decisions. Numerous failures and cost overruns may have been avoided with timely access to accurate information. 
> 
> The Administration is committed to using technology to move past these barriers. In the IT Dashboard, the public has a platform for unprecedented access to useful, unfiltered data regarding the performance of IT investments. Information available includes responsible government officials and contractors as well as project performance data, updated monthly. This enables better decision-making, giving us the ability to turn around poorly performing projects and to divest from those which no longer make sense. 
> 
> _In making this data publicly available, we are providing unfettered access to investment performance to its true owners - the American people._

Vivek explained that last point further in a telephone conversation with me last night. I asked him about the level of buy-in across the government for this kind of radical transparency about the performance of projects. He said: 

> "It's a cultural transformation, in terms of recognizing that we are in the public square. The work that we do is work that is supposed to be performed in the interest of the American taxpayers. And so making visible how we're performing means fleshing out these complicated issues in the public square. Culturally, making the shift is much better than letting it hide under the veil of secrecy. 

Paging through the site, it's clear that not every CIO is on board, or else has not had the time to make the project evaluations. For example, in this project page for the Expeditionary Combat Support System, you can see that the Department of Defense CIO has not yet provided his own evaluation, and even the name of the prime contractor is missing: 

[](http://radar.oreilly.com/upload/2009/06/FailedProject1.png)

According to the Washington Post, [some agency CIOs have grumbled](http://www.washingtonpost.com/wp-dyn/content/article/2009/06/30/AR2009063001370.html?hpid=moreheadlines) about the workload of maintaining the data, but as Vivek noted in that same article: 

> I talked to the CIO Council and saw the data change overnight. It was cleaned up immediately when people realized it was going to be made public. 

That's part of the new media chess game being played out here. Having the dashboard public creates an urgency to bring the information it contains up to date, and presumably, to respond to what it shows. In last night's phone interview, Vivek noted: 

> We're going live in beta, so that we're giving agencies enough time to make sure that the data and evaluations are up to date. They will have up to 30 days to make that journey.

I love that. 30 days is an eye-blink in traditional government time! We're starting to see agile methodologies make their government debut. 

The site was built on Drupal. Graphics are in Flash, provided by [FusionCharts](http://www.fusioncharts.com). Based on a reading of [the FAQ](http://it.usaspending.gov/?q=content/faq), it looks like the initial database was generated from data provided by agencies to the Office of Management and Budget (OMB) on congressionally-mandated reporting forms. Monthly updates will be [via a web interface provided as part of the project](http://it.usaspending.gov/?q=content/faq-agencies). There are future plans to allow agencies to provide XML feeds. (It would be good to see that the site uses the same web services architecture to collect its data as it does to provide it out to citizens.) 

This is part of being agile, and one of the first lessons in building an "[architecture of participation](http://oreillynet.com/pub/a/oreilly/tim/articles/architecture_of_participation.html)": rather than having to get complete buy-in from everyone up front, you find a way to bootstrap the project, to get it to what Eric Raymond once called [a plausible promise](http://books.google.com/books?id=yGFNKDloXq0C&lpg=PP1&dq=eric%20raymond%20plausible%20promise%20cathedral&pg=PA47) that encourages further participation. What you hope for is the kind of virtuous cascade that gave us successful open source projects like Linux and Apache, and participatory online services like Wikipedia, Craigslist, YouTube, Facebook, Twitter, and, of course, the web itself. 

The dashboard platform is primed for citizen participation, not just agency participation. Each page has a "share" icon, which brings up a dialog that lets you tweet a link to that page, share it on Facebook or del.icio.us, or grab the data as an RSS feed or an excel spreadsheet: 

[](http://radar.oreilly.com/upload/2009/06/Sharing.png)

It's [mashup-ready](http://it.usaspending.gov/?q=content/data-feeds), with a tool for selecting which fields you want in an XML feed. Unlike the main usaspending.gov site, whose API offers 1000 records at a time and discourages repeated calls to download the whole database, the data behind the IT Dashboard is easily downloaded in its entirety. Kudos for that. 

Vivek noted: 

> This is a fundamental change in the way government is going to be run. In the same way that the President was able to mobilize and organize online communities to drive change, what I want to accomplish here is to tap into that energy, to tap into some of the smartest people in the country, accept the fact that we don't have a monopoly on the best ideas, and make sure that we unleash the online communities of people who are interested in specific areas. Whether it's environment, or healthcare, or energy, we want them to look at the investments that we're making. And we want to make sure that we're getting feedback. A lot of times, the government is not the beneficiary of the best thinking in the country, because something was decided [ten years ago] and we're not asking, what is the innovative path? How can we achieve our objectives in a much faster way, and at a much lower cost? 

In this regard, the view of the management objectives by which each project is evaluated is important. For example, the objectives of this behind-schedule [biosense project](http://it.usaspending.gov/?q=content/performance-metrics&buscid=3113) may already be met by non-governmental projects like [INSTEDD](http://www.instedd.org) or [the Global Virus Forecasting Initiative](http://gvfi.org</a) \- or at the very least, knowledge of this project might allow better cooperation between the governmental and non-governmental projects. 

As far as I can tell, feedback right now is limited to a simple comment form. The site would benefit from more structured opportunities for interaction and requests for further information. In particular, we need a better and more detailed view of project objectives for the public to engage properly in oversight and brainstorming. Right now, the project measures what is relatively easy to measure. The next big challenge comes in in saying "what we really need to know in order to be able to decide that the money was misspent is ..." and then changing the reporting law or requirements to get that data. 

Overall, the data dashboard is a small but important step. Even though the Federal IT portfolio, at $70 billion, is huge, it's a tiny fraction of overall government spending. But if Vivek Kundra and his team can prove the benefit of radical transparency in this sphere, we can hope that it will spread to other areas of government. We need to see public involvement, so those government agency CIOs who aren't already on board with the program are encouraged to do so by the flow of attention. We also need to see better overall metrics. What contractors are most often behind schedule and over budget? What departments are struggling? Are we doing better over time as a result of the increased scrutiny? 

Dashboards are only as good as the people who use them. Ultimately, the goal of instrumenting government spending and its effectiveness depends on the willingness of those in positions of authority to respond to what the dashboards tell them. Vivek Kundra is rolling out a suite of IT management tools - a platform for better government, if you will - of which this is only one installment. Let's hope that as the dashboards are updated each month, we'll see evidence of change, with the data more complete, and with out-of-control projects reined in, improved, or ended.
