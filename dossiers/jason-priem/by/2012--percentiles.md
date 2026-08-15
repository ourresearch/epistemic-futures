---
title: "Percentiles"
person: jason-priem
section: by
type: blog-post
year: 2012
date: 2012-09-11
venue: "Impactstory blog"
authors: "Jason Priem"
source_url: https://blog.openalex.org/31342582590/
retrieved: 2026-08-13
content: full-text
notes: "Byline from WordPress author field (user 'jason') on the merged Impactstory/OurResearch/OpenAlex blog. Originally published on blog.impactstory.org."
---

# Percentiles

## Full text

\
In the last post we talked about the need to give raw counts context on expected impact.  How should this background information be communicated?

Our favourite approach: percentiles.

Try it on for size: Your paper is in the 88th percentile of CiteULike bookmarks, relative to other papers like it.  That tells you something, doesn’t it?  The paper got a lot of bookmarks, but there are some papers with more.  Simple, succinct, intuitive, and applicable to any type of metric.

Percentiles were also the favoured approach for context in the “normalization” breakout group at [altmetrics12](http://altmetrics.org/altmetrics12/), and have already popped up as a [total-impact feature request](https://totalimpact.uservoice.com/forums/166950-general/suggestions/3028257-show-percentile-metrics-as-well-as-counts). Percentiles have been explored scientometrics for journal impact metrics, including in a recent paper by Leydesdorff and Bornmann \[<http://dx.doi.org/10.1002/asi.21609>, [free preprint PDF](http://arxiv.org/pdf/1103.5241.pdf).\] The abstract says “total impact” in it, did you catch that?  🙂

As it turns out, actually implementing percentiles for altmetrics isn’t quite as simple as it sounds.  We have to make a few decisions about how to handle ties, and zeros, and sampling, and how to define “other papers like it”…. stay tuned.

*([part 2](http://wp.me/p2LlD9-a) of a series on how total-impact plans to give context to the altmetrics it reports. see [part 1](http://wp.me/p2LlD9-b), [part 3](http://wp.me/p2LlD9-8), and [part 4](http://wp.me/p2LlD9-7).)*
