---
title: "Two natural allies of a \"Data Transparency\" agenda: capabilities forecasters and social simulators"
person: "nick-vincent"
section: "by"
type: "blog-post"
year: 2026
date: "2026-03-09"
venue: "Data Leverage (Digital Garden / dataleverage.substack.com)"
authors: "Nicholas Vincent"
source_url: "https://nickmvincent.github.io/short-reactions/two-natural-allies-of-a-data-transparency.html"
retrieved: "2026-08-13"
content: "full-text"
notes: "Dek: Making an \"if you like X, you might want to support Y\" argument for data-focused policy Garden section: short-reactions. Mirrored on the Data Leverage Substack."
---

# Two natural allies of a "Data Transparency" agenda: capabilities forecasters and social simulators

## Full text

Extremely clear water. Photo by Hans on Unsplash

If you’ve read this blog — or the title of this blog — you might not
be surprised that I am a fan of data-centric research and data-centric
policy advocacy. Many of my posts and research outputs include extended
arguments for why we should support policy and research that leads to
more documentation of data, more efforts to appraise the value of data,
and better rules for transactions involving data. Often, I motivate
these arguments through the frame of mitigating negative impacts from AI
progress or just by making the case that we should generally be making
AI systems more human-centered by giving people agency.

In the past few weeks, two separate (but in my view, related!) areas
of discourse I’ve been following with interest are:

-

capabilities forecasting (e.g. discussion of “Task-Completion Time Horizons of
Frontier AI Models” from METR).

-

social simulation (especially responses to the announcement of Simile.ai, a venture extending
previously influential research on LLM social
simulation)

In this post, I want to make a brief argument that anyone interested
in one or both of the above two agendas is a very natural ally of “Clear
Data Rules” advocacy. I’ll focus in particular on a pretty high-level
“wave a magic wand and get more data transparency” conceptualization of
clear data rules, and hopefully get into nuanced interactions in the
comments, future posts, or more formal follow-up work.

First, it is notable that much of the capabilities discourse has been
very focused on predicting progress over time. The x-axis in the main
METR plot that’s been the subject of discourse (noting that there are a
lot of plots and robustness checks in the actual paper) is time. Thus,
the questions being discussed in this debate tend to center
understanding how rates of progress in the AI field will change (or not)
and what this means for the urgency of institutional and societal
response.

However, for any single data point in “Figure 1 METR plot”, we could
in theory characterize each model by its training data (and more
specifically, pre-training data, various post-training datasets with
different goals, internal evaluation datasets that may have guided
design decisions, etc.). At a high-level, we’d expect information about
training data to be highly predictive of performance on a given
benchmark. For instance, including a large number of expert Python
programmers in post-training should greatly improve success at a Python
coding task suite.

There’s plenty of nuance to be further investigated regarding
interactions between pre- and post-training, transfer of knowledge
across related domains, etc. But even a simplified understanding is
useful to reason about how more training data transparency might impact
scaling models and forecasting more generally.

Consider just this high-level claim: if we had significant dataset
documentation for each model, we could likely greatly improve our models
of domain-specific AI progress. If we wave our magic policy wand and get
rich datasheets for every frontier model, capabilities measurement would
benefit massively overnight. Thus, parties who mainly want better
capabilities forecasting and scaling models might want to advocate for
data transparency and clear data rules even if they don’t care about
any of the other stuff I normally talk about.

Second, let’s turn to the topic of AI social simulation. The goal of
simile.ai is to build a model that “predicts human behavior in any
situation, and a product that deploys it at scale”. More generally, we
might understand AI social simulations as attempting to use the fact
that real human records are used to train AI models, thus these model
weights retain real insights about human behavior and the world, and
thus the models themselves might contribute to epistemically useful
simulations if the simulations are engineered and calibrated
correctly.

There’s much to debate here. Some scholars have quite harshly criticized this endeavor
(and I think they make many good points) and others have argued in favor.

Without wading into the broader normative discussion here or touching
on any specific empirical questions (more to come on that front!), I’d
posit this: social simulation might be promising in some contexts but
almost all useful contexts will require the use of fully documented
frontier models, with a particular focus on the representation of
different groups of people in training (and ideally, some attempt at
group-level training data attribution). I have a longer version of this
argument in a deck I presented at the University of Washington’s CSSS recently, which you can glance at
here.

Basically, if we want to make strong claims about an LLM/AI social
simulation and the application of results to a given group of people, we
probably want to know about how different groups of people contributed
to any upstream AI models!

So, anyone interested in LLM social simulation may also want to
advocate for data transparency purely to make LLM social simulation more
useful.

Source revision history

Selected Git commits that changed this source file.

- 1a8a220b9c 2026-08-03 - Preserve legacy reaction mirror bodies

- 542114960e 2026-08-03 - Add a dedicated reaction-post lane

- 9fb4674b8a 2026-07-12 - Migrate blog into digital presence monorepo

Mirror freshness

Maintenance status for tracked full-copy mirrors of this post.

-
Current
substack

mirror 2026-03-09

Baseline from original_url

Source and AT Protocol record

Source path
content/writing/reaction-posts/2026-03-09-two-natural-allies-of-a-data-transparency.md

AT Protocol URI
at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.document/3mizeerbo2wiq

Exact public AT Protocol record cached for the Leaflet/Bluesky-facing copy.

{
"uri": "at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.document/3mizeerbo2wiq",
"cid": "bafyreigtpiswk5p377vohedwxbhshcd3mbbolzmzy3jtm45o5455tamhvy",
"value": {
"path": "/3mizeerbo2wiq",
"site": "at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.publication/3lzrsw2kvwc2m",
"$type": "site.standard.document",
"title": "Two natural allies of a \"Data Transparency\" agenda: capabilities forecasters and social simulators",
"content": {
"$type": "pub.leaflet.content",
"pages": [
{
"$type": "pub.leaflet.pages.linearDocument",
"blocks": [
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 30,
"byteStart": 8
},
"features": [
{
"uri": "https://dataleverage.substack.com/p/two-natural-allies-of-a-data-transparency",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 7,
"byteStart": 0
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#bold"
}
]
}
],
"plaintext": "Source: Data Leverage Substack"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 15,
"byteStart": 0
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#bold"
}
]
}
],
"plaintext": "Date Published: March 9, 2026"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.image",
"image": {
"$type": "blob",
"ref": {
"$link": "bafkreiey7vrmchanjhy3baprjn7dexbyfph4fvgxn7fvkakynsjtjtgz54"
},
"mimeType": "image/jpeg",
"size": 358790
},
"aspectRatio": {
"$type": "pub.leaflet.blocks.image#aspectRatio",
"width": 1080,
"height": 1440
}
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 48,
"byteStart": 40
},
"features": [
{
"uri": "https://unsplash.com",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 36,
"byteStart": 32
},
"features": [
{
"uri": "https://unsplash.com/@hansphoto",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 15,
"byteStart": 10
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "Extremely clear water. Photo by Hans on Unsplash"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "If you’ve read this blog — or the title of this blog — you might not be surprised that I am a fan of data-centric research and data-centric policy advocacy. Many of my posts and research outputs include extended arguments for why we should support policy and research that leads to more documentation of data, more efforts to appraise the value of data, and better rules for transactions involving data. Often, I motivate these arguments through the frame of mitigating negative impacts from AI progress or just by making the case that we should generally be making AI systems more human-centered by giving people agency."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "In the past few weeks, two separate (but in my view, related!) areas of discourse I’ve been following with interest are:"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.unorderedList",
"children": [
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 99,
"byteStart": 48
},
"features": [
{
"uri": "https://metr.org/time-horizons/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "capabilities forecasting (e.g. discussion of “Task-Completion Time Horizons of Frontier AI Models” from METR)."
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 125,
"byteStart": 117
},
"features": [
{
"uri": "https://arxiv.org/abs/2304.03442",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 72,
"byteStart": 63
},
"features": [
{
"uri": "https://www.simile.ai/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "social simulation (especially responses to the announcement of Simile.ai, a venture extending previously influential research on LLM social simulation)"
}
}
]
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "In this post, I want to make a brief argument that anyone interested in one or both of the above two agendas is a very natural ally of “Clear Data Rules” advocacy. I’ll focus in particular on a pretty high-level “wave a magic wand and get more data transparency” conceptualization of clear data rules, and hopefully get into nuanced interactions in the comments, future posts, or more formal follow-up work."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.horizontalRule"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "First, it is notable that much of the capabilities discourse has been very focused on predicting progress over time. The x-axis in the main METR plot that’s been the subject of discourse (noting that there are a lot of plots and robustness checks in the actual paper) is time. Thus, the questions being discussed in this debate tend to center understanding how rates of progress in the AI field will change (or not) and what this means for the urgency of institutional and societal response."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "However, for any single data point in “Figure 1 METR plot”, we could in theory characterize each model by its training data (and more specifically, pre-training data, various post-training datasets with different goals, internal evaluation datasets that may have guided design decisions, etc.). At a high-level, we’d expect information about training data to be highly predictive of performance on a given benchmark. For instance, including a large number of expert Python programmers in post-training should greatly improve success at a Python coding task suite."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "There’s plenty of nuance to be further investigated regarding interactions between pre- and post-training, transfer of knowledge across related domains, etc. But even a simplified understanding is useful to reason about how more training data transparency might impact scaling models and forecasting more generally."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 538,
"byteStart": 462
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "Consider just this high-level claim: if we had significant dataset documentation for each model, we could likely greatly improve our models of domain-specific AI progress. If we wave our magic policy wand and get rich datasheets for every frontier model, capabilities measurement would benefit massively overnight. Thus, parties who mainly want better capabilities forecasting and scaling models might want to advocate for data transparency and clear data rules even if they don’t care about any of the other stuff I normally talk about."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.horizontalRule"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Second, let’s turn to the topic of AI social simulation. The goal of simile.ai is to build a model that “predicts human behavior in any situation, and a product that deploys it at scale”. More generally, we might understand AI social simulations as attempting to use the fact that real human records are used to train AI models, thus these model weights retain real insights about human behavior and the world, and thus the models themselves might contribute to epistemically useful simulations if the simulations are engineered and calibrated correctly."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 161,
"byteStart": 156
},
"features": [
{
"uri": "https://icml.cc/virtual/2025/poster/40125",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 74,
"byteStart": 64
},
"features": [
{
"uri": "https://arxiv.org/abs/2401.08572",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "There’s much to debate here. Some scholars have quite harshly criticized this endeavor (and I think they make many good points) and others have argued in favor."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 598,
"byteStart": 594
},
"features": [
{
"uri": "https://github.com/nickmvincent/public-talks/tree/main/2025-10_csss_gabm",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 559,
"byteStart": 555
},
"features": [
{
"uri": "https://csss.uw.edu/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Without wading into the broader normative discussion here or touching on any specific empirical questions (more to come on that front!), I’d posit this: social simulation might be promising in some contexts but almost all useful contexts will require the use of fully documented frontier models, with a particular focus on the representation of different groups of people in training (and ideally, some attempt at group-level training data attribution). I have a longer version of this argument in a deck I presented at the University of Washington’s CSSS recently, which you can glance at here."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Basically, if we want to make strong claims about an LLM/AI social simulation and the application of results to a given group of people, we probably want to know about how different groups of people contributed to any upstream AI models!"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "So, anyone interested in LLM social simulation may also want to advocate for data transparency purely to make LLM social simulation more useful."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.horizontalRule"
}
}
]
}
]
},
"description": "Making an \"if you like X, you might want to support Y\" argument for data-focused policy",
"publishedAt": "2026-03-09T00:00:00.000Z"
}
}
