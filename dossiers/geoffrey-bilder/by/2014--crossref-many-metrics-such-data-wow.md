---
title: "Many Metrics. Such Data. Wow."
person: "geoffrey-bilder"
section: "by"
type: "blog-post"
year: 2014
date: 2014-02-24
venue: "Crossref blog"
authors: "Geoffrey Bilder"
source_url: "https://www.crossref.org/blog/many-metrics-such-data-wow/"
retrieved: "2026-08-13"
content: "full-text"
notes: "Crossref blog post. DOI 10.64000/96snc-ye031."
---

# Many Metrics. Such Data. Wow.

## Full text

**12 minute read.**

## Many Metrics. Such Data. Wow.

[

> Crossref Labs loves to be the last to jump on an internet trend, so what better than than to combine the [Doge meme](http://en.wikipedia.org/wiki/Doge_(meme)) with [altmetrics](http://en.wikipedia.org/wiki/Altmetrics)?

**Note:** The API calls below have been superceeded with the development of the Event Data project. See [the latest API documentation](http://eventdata.crossref.org/) for equivalent functionality

Want to know how many times a Crossref DOI is cited by the Wikipedia?

```
http://det.labs.crossref.org/works/doi/10.1371/journal.pone.0086859
```

Or how many times one has been mentioned in Europe PubMed Central?

```
http://det.labs.crossref.org/works/doi/10.1016/j.neuropsychologia.2013.10.021
```

Or DataCite?

```
http://det.labs.crossref.org/works/doi/10.1111/jeb.12289
```

## Background

Back in 2011 [PLOS](http://www.plos.org/) released its awesome [ALM system](https://web.archive.org/web/20190118175222if_/https://www.plos.org/article-level-metrics) as [open source software](http://en.wikipedia.org/wiki/Open-source_software) (OSS). At [Crossref Labs](https://www.crossref.org/labs/), we thought it might be interesting to see what would happen if we ran our own instance of the system and loaded it up with a few Crossref DOIs. So we did. And the code fell over. Oops. Somehow it didn’t like dealing with 10 million DOIs. Funny that.

But the beauty of OSS is that we were able to work with PLOS to scale the code to handle our volume of data. Crossref contracted with [Cottage Labs](http://cottagelabs.com/)  and we both worked with PLOS to make changes to the system. These eventually got fed back into the main [ALM source on Github](https://github.com/articlemetrics/alm/). Now everybody benefits from our work. Yay for OSS.

So if you want to know technical details, skip to [Details for Propellerheads](#details). But if you want to know why we did this, and what we plan to do with it, read on.

## Why?

There are (cough) some problems in our industry that we can best solve with shared infrastructure. When publishers first put scholarly content online, they used to make bilateral reference linking agreements. These agreements allowed them to link citations using each other’s proprietary reference linking APIs. But this system didn’t scale. It was too time-consuming to negotiate all the agreements needed to link to other publishers. And linking through many proprietary citation APIs was too complex and too fragile. So the industry founded Crossref to create a common, cross-publisher citation linking API. Crossref has since obviated the need for bilateral linking arrangements.

So-called [altmetrics](http://en.wikipedia.org/wiki/Altmetrics) look like they might have similar characteristics. You have ~4000 Crossref member publishers and N sources (e.g. Twitter, Mendeley, Facebook, CiteULike, etc.) where people use (e.g. discuss, bookmark, annotate, etc.) scholarly publications. Publishers could conceivably each choose to run their own system to collect this information. But if they did, they would face the following problems:

* The N sources will be volatile. New ones will emerge. Old ones will vanish.
* Each publisher will need to deal with each source’s different APIs, rate limits, T&Cs, data licenses, etc. This is a logistical headache for both the publishers and for the sources.
* If publishers use different systems which in turn look at different sources, it will be difficult to compare results across publishers.
* If a journal moves from one publisher to another, then how are the metrics for that journal’s articles going to follow the journal? This isn’t a complete list, but it shows that there might be some virtue in publishers sharing an infrastructure for collecting this data. But what about commercial providers? Couldn’t they provide these ALM services? Of course - and some of them currently do. But normally they look on the actual collection of this data as a means to an end. The real value they provide is in the analysis, reporting and tools that they build on top of the data. Crossref has no interest in building front-ends to this data. If there is a role for us to play here, it is simply in the collection and distribution of the data.

## No, really, WHY?

Aren’t these altmetrics [an ill-conceived and meretricious idea](https://web.archive.org/web/20170112105521/https://scholarlyoa.com/2013/08/01/article-level-metrics/)? By providing this kind of information, isn’t Crossref just encouraging feckless, [neoliberal university administrators](http://blogs.lse.ac.uk/impactofsocialsciences/2014/01/27/its-the-neoliberalism-stupid-kansa/) to hasten academia’s slide into a [Stakhanovite](http://en.wikipedia.org/wiki/Stakhanovite_movement) dystopia? Can’t these systems be gamed?

FOR THE LOVE OF [FSM](http://en.wikipedia.org/wiki/Flying_Spaghetti_Monster), WHY IS CROSSREF DABBLING IN SOMETHING OF SUCH QUESTIONABLE VALUE?

takes deep breath. wipes spittle from beard

These are all serious concerns. [Goodhart’s Law](http://en.wikipedia.org/wiki/Goodhart's_law) and all that… If a university’s appointments and promotion committee is largely swayed by [Impact Factor](http://en.wikipedia.org/wiki/Impact_factor), it won’t improve a thing if they substitute or supplement Impact Factor with altmetrics. [Amy Brand](http://www.linkedin.com/profile/view?id=8488638&authType=NAME_SEARCH&authToken=6zaC&locale=en_US&srchid=4700671392208272787&srchindex=1&srchtotal=32&trk=vsrp_people_res_name&trkInfo=VSRPsearchId%3A4700671392208272787%2CVSRPtargetId%3A8488638%2CVSRPcmpt%3Aprimary) has repeatedly pointed out, [the best institutions simply don’t use metrics this way at all](http://article-level-metrics.plos.org/files/2013/10/Brand.pptx) (PowerPoint presentation). They know better.

But yes, it is still likely that some powerful people will come to lazy conclusions based on altmetrics. And following that, other lazy, unscrupulous and opportunistic people will attempt to game said metrics. We may even see an industry emerge to exploit this mess and provide the scholarly equivalent of [SEO](http://en.wikipedia.org/wiki/Search_engine_optimization). Feh. Now I’m depressed and I need a drink.

So again, why is Crossref doing this? Though we have our doubts about how effective altmetrics will be in evaluating the quality of content, we do believe that they are a useful tool for understanding how scholarly content is used and interpreted. *The most eloquent arguments against altmetrics for measuring quality, inadvertently make the case for altmetrics as a tool for monitoring attention.*

Critics of altmetrics point out that much of the attention that research receives outside of formal scholarly communications channels can be ascribed to:

* Puffery. Researchers and/or university/publisher “[PR wonks](http://www.dcscience.net/?p=6369)” over-promoting research results.
* Innocent misinterpretation. A lay audience simply doesn’t understand the research results.
* Deliberate misinterpretation. Ideologues misrepresent research results to support their agendas.
* Salaciousness. The research appears to be about sex, drugs, crime, video games or other popular bogeymen.
* Neurobollocks. [A category unto itself these days](https://web.archive.org/web/20160405135736/http://www.wired.co.uk/news/archive/2012-11/08/neurobollocks).

In short, scholarly research might be misinterpreted. Shock horror. Ban all metrics. Whew. That won’t happen again.

Scholarly research has always been discussed outside of formal scholarly venues. Both by scholars themselves and by interested laity. Sometimes these discussions advance the scientific cause. Sometimes they undermine it. The University of Utah didn’t depend on widespread Internet access or social networks to promote [yet-to-be peer-reviewed claims about cold fusion](http://en.wikipedia.org/wiki/Cold_fusion). That was just old-fashioned analogue puffery. And the Internet played no role in the Laetrile or [DMSO crazes of the 1980s](http://www.cancer.org/treatment/treatmentsandsideeffects/complementaryandalternativemedicine/pharmacologicalandbiologicaltreatment/dmso). You see, there were once these things called “[newspapers.](http://en.wikipedia.org/wiki/Newspaper)” And another thing called “[television.](http://en.wikipedia.org/wiki/Television)” And a sophisticated [meatspace](http://www.urbandictionary.com/define.php?term=meatspace)-based social network called a “[town square](http://en.wikipedia.org/wiki/Town_square).”

But there are critical differences between then and now. As [citizens get more access to the scholarly literature](https://obamawhitehouse.archives.gov/blog/2013/02/22/expanding-public-access-results-federally-funded-research), it is far more likely that research is going to be discussed outside of formal scholarly venues. Now we can build tools to help researchers track these discussions. Now researchers can, if they need to, engage in the conversations as well. One would think that conscientious researchers would see it as their responsibility to remain engaged, to know how their research is being used. And especially to know when it is being misused.

That isn’t to say that we expect researchers will welcome this task. We are no Pollyannas. Researchers are already famously overstretched. They [barely have time to keep up with the formally published literature](https://ddoi.org/10.1016/j.lisr.2009.02.002). It seems cruel to expect them to keep up with the firehose of the Internet as well.

Which gets us back to the value of altmetrics tools. Our hope is that, as altmetrics tools evolve, they will provide publishers and researchers with an efficient mechanism for monitoring the use of their content in non-traditional venues. Just in the way that citations were used before they were distorted into proxies for credit and kudos.

We don’t think altmetrics are there yet. Partly because some parties are still tantalized by the prospect of usurping one metric for another. But mostly because the entire field is still nascent. People don’t yet know how the information can be combined and used effectively. So we still make naive assumptions such as “link=like” and “more=better.” Surely it will eventually occur to somebody that, instead, there may be a connection between [repeated headline-grabbing research and academic fraud](http://www.nytimes.com/2013/04/28/magazine/diederik-stapels-audacious-academic-fraud.html?_r=1&). A neuroscientist might be interested in a tool that alerts them if the MRI scans in their research paper are being misinterpreted on the web to promote neurobollocks. An immunologist may want to know if their research is being misused by the anti-vaccination movement. Perhaps the real value in gathering this data will be seen when somebody builds tools to help researchers DETECT puffery, social-citation cabals, and misinterpretation of research results?

But Crossref won’t be building those tools. What we might be able to do is help others overcome another hurdle that blocks the development of more sophisticated tools; getting hold of the needed data in the first place. This is why we are dabbling in altmetrics.

Wikipedia is already the 8th largest referrer of Crossref DOIs. Note that this doesn’t just mean that the Wikipedia cites lots of Crossref DOIs, it means that people actually click on and follow those DOIs to the scholarly literature. As scholarly communication transcends traditional outlets and as the audience for scholarly research broadens, we think that it will be more important for publishers and researcher to be aware of how their research is being discussed and used. They may even need to engage more with non-scholarly audiences. In order to do this, they need to be aware of the conversations. Crossref is providing this experimental data source in the hope that we can spur the development of more sophisticated tools for detecting and analyzing these conversations. Thankfully, this is an inexpensive experiment to conduct - largely thanks to the decision on the part of PLOS to open source its ALM code.

## What Now?

Crossref’s instance of PLOS’s ALM code is an experiment. We mentioned that we had encountered scalability problems and that we had resolved some of them. But there are still big scalability issues to address. For example, assuming a response time of 1 second, if we wanted to poll the English-language version of the Wikipedia to see what had cited each of the 65 million DOIs held in Crossref, the process would take years to complete. But this is how the system is designed to work at the moment. It polls various source APIs to see if a particular DOI is “mentioned”. Parallelizing the queries might reduce the amount of time it takes to poll the Wikipedia, but it doesn’t reduce the work. Another obvious way in which we could improve the scalability of the system is to add a push mechanism to supplement the pull mechanism. Instead of going out and polling the Wikipedia 65 million times, we could establish a “scholarly [linkback](http://en.wikipedia.org/wiki/Linkback)” mechanism that would allow third parties to alert us when DOIs and other scholarly identifiers are referenced (e.g. cited, bookmarked, shared). If the Wikipedia used this, then even in an extreme case scenario (i.e. everything in Wikipedia cites at least one Crossref DOI), this would mean that we would only need to process ~ 4 million trackbacks.

The other significant advantage of adding a push API is that it would take the burden off of Crossref to know what sources we want to poll. At the moment, if a new source comes online, we’d need to know about it and build a custom plugin to poll their data. This needlessly disadvantages new tools and services as it means that their data will not be gathered until they are big enough for us to pay attention to. If the service in question addresses a niche of the scholarly ecosystem, they may never become big enough. But if we allow sources to push data to us using a common infrastructure, then new sources do not need to wait for us to take notice before they can participate in the system.

Supporting (potentially) many new sources will raise another technical issue- tracking and maintaining the provenance of the data that we gather. The current ALM system does a pretty good job of keeping data, but if we ever want third parties to be able to rely on the system, we probably need to extend the provenance information so that the data is cheaply and easily auditable.

Perhaps the most important thing we want to learn from running this experimental ALM instance is: what it would take to run the system as a production service? What technical resources would it require? How could they be supported? And from this we hope to gain enough information to decide whether the service is worth running and, if so, by whom. Crossref is just one of several organisations that could run such a service, but it is not clear if it would be the best one. We hope that as we work with PLOS, our members and the rest of the scholarly community, we’ll get a better idea of how such a service should be governed and sustained.

## Details for Propellerheads

### Warning, Caveats and Weasel Words

The Crossref ALM instance is a [Crossref Labs](https://www.crossref.org/labs/) project. It is running on R&D equipment in a non-production environment administered by an orangutang on a diet of Redbulls and vodka.

### So what is working?

The system has been initially loaded with 317,500+  Crossref DOIs representing publications from 2014. We will load more DOIs in reverse chronological order until we get bored or until the system falls over again.

We have activated the following sources:

- PubMed
- DataCite
- PubMedCentral Europe Citations and Usage

We have data from the following sources but will need some work to achieve stability:

- Facebook
- Wikipedia
- CiteULike
- Twitter
- Reddit

Some of them are faster than others. Some are more temperamental than others. WordPress, for example, seems to go into a sulk and shut itself off  after approximately 1,300 API calls.

In any case, we will be monitoring and tweaking the sources as we gather data. We will also add new sources as we get requested API keys. We will probably even create one or two new sources ourselves. Watch this blog and we’ll update you as we add/tweak sources.

### Dammit, shut up already and tell me how to query stuff.

You can [login to the Crossref ALM instance](#) simply using a Mozilla Persona (yes, we’d eventually like to support ORCID too). Once logged-in, your account page will list an API key. Using the API key, you can do things like:

```
http://det.labs.crossref.org/api/v5/articles?ids=10.1038/nature12990
```

And you will see that (as of this writing), said Nature article has been cited by the Wikipedia article here:

`https://en.wikipedia.org/wiki/HE0107-5240#cite_ref-Keller2014_4-0;`

PLOS has provided [lovely detailed instructions for using the API](#)- So, please, play with the API and see what you make of it. On our side we will be looking at how we can improve performance and expand coverage. We don’t promise much- the logistics here are formidable. As we said above, once you start working with millions of documents, the polling process starts to hit API walls quickly. But that is all part of the experiment. We appreciate your helping us and would like your feedback. We can be contacted at:
