---
title: "Let’s value the software that powers science: Introducing Depsy"
person: jason-priem
section: by
type: blog-post
year: 2015
date: 2015-11-09
venue: "Impactstory blog"
authors: "Jason Priem"
source_url: https://blog.openalex.org/introducing-depsy/
retrieved: 2026-08-13
content: full-text
notes: "Byline from WordPress author field (user 'jason') on the merged Impactstory/OurResearch/OpenAlex blog. Originally published on blog.impactstory.org."
---

# Let’s value the software that powers science: Introducing Depsy

## Full text

\
Today we’re proud to officially launch [Depsy](http://depsy.org), an open-source webapp that tracks research software impact.

[![](https://i0.wp.com/i.imgur.com/5Ded4q4.png?resize=1000%2C443&ssl=1)](http://depsy.org/package/python/scipy)

We made Depsy to solve a problem:  in modern science, research software is often as important as traditional research papers–[but it’s not treated that way when it comes to funding and tenure](http://sciencecodemanifesto.org/). There, the traditional publish-or-perish, show-me-the-Impact-Factor system still rules.

We need to fix that. We need to provide meaningful incentives for the [scientist-developers](http://dirkgorissen.com/2012/03/26/the-researcher-programmer-a-new-species/) who make important research software, so that we can keep doing important, software-driven science.

[Lots of things have to happen](http://rev.oxfordjournals.org/content/early/2015/07/26/reseval.rvv014.full) to support this change. Depsy is a shot at making one of those things happen: a system that tracks the impact of software in *software-native ways*.

That means not just counting up citations to a hastily-written paper *about* the software, but actual mentions of *the software itself* in the literature. It means looking how software gets reused by other software, even when it’s not cited at all. And it means understanding the full complexity of software authorship, where one project can involve hundreds of contributors in multiple roles that don’t map to traditional paper authorship.

Ok, this sounds great, but how about some specifics. Check out these examples:

- [GDAL](http://depsy.org/package/python/GDAL) is a geoscience library. Depsy finds this cool NASA-funded [ice map paper](http://www.the-cryosphere.net/8/1509/2014/tc-8-1509-2014.html) that mentions GDAL without formally citing it. Also check out key author [Even Rouault:](http://depsy.org/person/378948) the project commit history demonstrates he deserves 27% credit for GDAL, even though he’s overlooked in more [traditional credit systems.](http://gdal.org/credits.html)
- [lubridate](http://depsy.org/package/r/lubridate) improves date handling for R. It’s not highly-cited, but we can see it’s making a different kind of impact: it’s got a very high dependency PageRank, because it’s reused by over 1000 different R projects on GitHub and CRAN.
- [BradleyTerry2](http://depsy.org/package/r/BradleyTerry2) implements a probability technique in R. It’s only directly reused by 8 projects—but Depsy shows that one of those projects is itself highly reused, leading to huge *indirect* impacts. This indirect reuse gives BradleyTerry2 a very high dependency PageRank score, even though its direct reuse is small, and that makes for a better reflection of real-world impact.
- [Michael Droettboom](http://depsy.org/person/342746) makes small (under 20%) contributions to other people’s research software, contributions easy to overlook. But the contributions are meaningful, and they’re to high-impact projects, so in Depsy’s transitive credit system he ends up as a highly-ranked contributor. Depsy can help unsung heroes like Micheal get rewarded.[\
  ![](https://i0.wp.com/i.imgur.com/v7SfFIT.png?resize=703%2C387&ssl=1)](http://depsy.org/person/342746) 

Depsy doesn’t do a perfect job of finding citations, tracking dependencies, or crediting authors (see [our in-progress paper](https://github.com/Impactstory/depsy-research/blob/master/introducing_depsy.md) for more details on limitations). It’s not supposed to. Instead, Depsy is a proof-of-concept to show that we can do them at all. The data and tools are there. We *can* measure and reward software impact, like we measure and reward the impact of papers.

![](https://i0.wp.com/i.imgur.com/F0ltjfC.png?resize=321%2C260&ssl=1)

Embed impact badges in your GitHub README

Given that, it’s not a question of *if* research software becomes a first-class scientific product, but *when* and *how*. Let’s start having the conversations about when and how (here are some [great](https://twitter.com/search?f=tweets&vertical=default&q=%23softwarecredit&src=typd) [places](https://twitter.com/search?q=%23wsspe&src=typd) [for](http://lists.researchcomputing.org.uk/pipermail/wssspe-researchcomputing.org.uk/) [that](http://www.software.ac.uk/blog)). Let’s improve Depsy, let’s build systems better than Depsy, and let’s (most importantly) start building the cultural and political structures that can use these systems.

For lots more details about Depsy, check out [the paper we’re writing](https://github.com/Impactstory/depsy-research/blob/master/introducing_depsy.md) (and contribute!), and of course [Depsy itself](http://depsy.org). We’re still in the early stages of this project, and we’re excited to hear your feedback: hit us up [on twitter](http://twitter.com/depsy_org), in the comments below, or in the [Hacker News thread about this post](https://news.ycombinator.com/item?id=10535593).

*Depsy is made possible by a grant from the National Science Foundation.*\
*edit nov 15 2015: change embed image to match new badge*
