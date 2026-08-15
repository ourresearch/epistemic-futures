---
title: "Plural AI Data Alignment"
person: "nick-vincent"
section: "by"
type: "blog-post"
year: 2023
date: "2023-03-02"
venue: "Data Leverage (Digital Garden / dataleverage.substack.com)"
authors: "Nicholas Vincent"
source_url: "https://nickmvincent.github.io/long-posts/measuring-relative-ai-alignment-in-terms-of-data-pipelines.html"
retrieved: "2026-08-13"
content: "full-text"
notes: "Dek: Measuring the Alignment of AI Systems Based on their Data Pipelines Garden section: long-posts. Mirrored on the Data Leverage Substack."
---

# Plural AI Data Alignment

## Full text

In this post, I propose an approach to score AI systems in terms of
how well they align with the interests of different groups, by measuring
the ability for data creators to reason about and configure the systems'
underlying "data pipelines". This is meant to provide a path towards
measuring alignment in a manner that supports plurality, i.e. these scores
can help us predict when AI systems are likely to "facilitate
cooperation and flourishing across a diversity of social groups".

This post was primarily inspired by discussions kicked off by
OpenAI’s recent blog post. It
is also informed by my recent participation in efforts
to further define directions for “AI Safety” research and recent efforts
to define and advance plurality research.

I’ve used the term "AI" in the title because this is the term being
used in ongoing discussions, and I think this ship has definitively
sailed (full disclosure: I also used the term in my dissertation,
so I suppose I’ve already bought in a bit). More specifically, I am
talking about computing systems that rely on some combination of
distinct datasets for training, evaluation, and/or calibration. The
discussion is especially relevant to “generative AI” that produces text
and images, like ChatGPT and StableDiffusion, but was originally
influenced by earlier work looking at search and recommendation.

The post will be structured as such: a two sentence definition,
followed by a two-paragraph definition with more details, followed by an
"FAQ" with even more details (the first version will be an IFAQ, because
these are questions I imagine might be frequent).

## Two-Sentence Definition

An AI system is more aligned with a coalition if members (1) know how
their data contributions flow to that system, (2) can reason about how
changes to data flow might impact AI capabilities, and (3) have agency
to reconfigure these data flows.

By measuring the alignment of various systems to various coalitions,
we can understand alignment in terms of concentration: some
systems are aligned to just a few individuals, others to very broad
groups, and others to specific subgroups.

## Two-Paragraph Definition

We can measure the relative alignment of data-dependent systems to
the preferences of various coalitions in terms of data contributors’
knowledge about data flows and ability to reconfigure these flows.
Specifically, we will set three thresholds: (1) a threshold for
awareness of data pipelines, (2) a threshold for ability for people to
reason about data impact, and (3) a threshold for minimum agency to
configure data pipelines and attempt to the count the number of people
who meet these criteria. We make the following assumption: if people
understand how their data contributions impact AI capabilities and can
easily act to configure how these contributions flow to different
organizations and systems, over time people will act (i.e., use the
“data levers” available to them) to improve the capabilities of systems
and organizations they support and hinder those they do not. We can
score a system’s alignment by estimating the fraction of data
contributors who meet some standard for data transparency and agency
(i.e., are informed enough about data flows and can reconfigure their
data flows with low enough cost). Under this definition, a system
becomes more aligned to a coalition when more users are given
high-quality information about data flow (including estimates of data’s
impact on capabilities) and low cost options to redirect that data flow.
Then, a system can be understand in terms of the concentration of its
alignment between different groups.

This definition most likely requires a collective approach to data
agency — time costs may make it impossible for individual people to make
decisions about how individual data records flow to individual firms
(providing prohibitively expensive but "technically possible" actions is
not agency). Instead, we could support data agency by scaffolding
data-mediating organizations. Finally, this definition supports a
pluralistic approach to alignment: given there are many distinct
coalitions of people in the world, any given system has a variety of
alignment scores, and any attempt to produce a single alignment score
requires explicitly weighting the preferences of different groups.
Instead, we can understand alignment scores as a variable to be used
similarly to inequality measurements.

## FAQ

### Are there other hidden
assumptions here?

There is an assumption that competing organizations and systems will
exist. This definition is not particularly useful in an ecosystem
dominated by a single player.

### Why
do we need to solve a governance problem with data contributions? What
if people just vote directly on issues of AI Governance, or continue to
vote for elected officials who pass legislation?

This idea is complementary to other mechanisms for AI governance.
Indeed, a paradigm in which everyone has access to lots of information
about AI systems and votes directly on AI-related policy could achieve
the same outcomes. The data pipeline focus is particularly promising
because it's very feasible; it emerges from a "natural" dependency in AI
systems.

### How
does this idea relate to existing AI Alignment work?

In the blog post, OpenAI links to to their Alignment
page post, which emphasizes the goal of making "artificial general
intelligence (AGI) aligned with human values and follow human
intent”.

This line of work includes research directions such as developing new
techniques for collecting and using human feedback, training explanatory
models that become part of the human evaluation loop, and performing
core research on machine learning explainability and robustness.

The definition proposed above also relates to explainability, but the
standards for "how explainable" are embedded in what we decide is a
reasonable definition for “high-quality information about data flow” and
the standards for robustness are embedded in how much additional agency
to change data people are given.

Of course, AI Alignment has been tackled by a variety of scholars,
see e.g. philosophical scholarship,
work
drawing on computer science and contract law, and arguments from machine
learning scholars.

(These are just a few examples: please let me know if there are
additional examples that would be particularly relevant here and/or
important to elevate.)

### How
do we define standards for "transparent enough" and "agentic
enough"

The above definition implies that we can agree on some reasonable
standard for providing transparency about data pipelines and a
reasonable definition of when individuals or groups have "agency" to
control data flows. However, these ideas are highly contestable -- you
might think my definition of transparency (say, a static datasheet and
interactive data explorer) is too high of a bar, or not high enough
(compared to say, a set of YouTube videos explaining existing data
flows). Similarly, we might disagree about what "reasonable" costs are
to withhold or redirect data. For instance, if changing data
contribution flows requires technical know-how or monetary costs, a
large number of data contributors may feel stuck in their current
configurations (i.e., they may just keep providing data to all the
actors they currently engage with / they might just keep using the same
platforms in the same way).

These questions themselves are governance questions. Realistically,
the initial thresholds will be set by tech companies themselves, and
then academics and activists may push to change these thresholds.
Personally, I think this is a decent way to move forward.

### This
seems to require attributing data to individuals or groups; how do we do
that?

For any given AI system, we can definitively identify a training set
and test set. This test set is typically meant to be a proxy for the set
of cases for which a system will actually be used, i.e. a “deployment
set”. We can only guess at what this deployment set will look like until
the model is deployed in practice.

For each of these sets, we can try to attribute the individual
records (i.e., units of data) to individual people or to groups. Once
we’ve done this, we can produce a moment-in-time snapshot of what
interests are represented in the data. This kind of practice is actually
already common for certain groups. For instance, in NLP research it
would be very common to describe the fraction of data belonging to
different written languages. In social computing, it might be reasonable
to how much data comes from predefined or inferred communities (e.g.
group by subreddits or by clusters of user behaviors). In work on
responsible AI, it’s very common to study training data in terms of
demographic representation.

A promising direction for solving some of the thorny problems with
individual attribution is to support infrastructure for associating data
contributions with existing online communities or explicitly labeled
"data coalitions" that people join and leave, and dealing with
attribution primarily at the community level.

### How
does this work if there are consistent differences between how training
data is collected and how the system is deployed in practice?

A key problem arises when neither the training set or test set
overlap with the actual deployment set. When this happens, our alignment
score becomes uninformative! But, organizations have a natural incentive
to avoid this situation: if this keeps happening, their systems will
perform poorly.

### How
often should this data pipeline alignment score be computed?

For this definition to be useful, we’d likely want to continuously
estimate this fraction over time, as individuals or groups reconfigure
flow of information and knowledge to systems. Capabilities should slowly
rise and fall — if they’re entirely static, we might imagine there is
not much governance going on (in the same way we might be concerned if a
single political party continuously dominates a ostensibly bipartisan
system for hundreds of years).

A monthly update is likely a reasonable starting point; we'd expect
people to use data levers as long-term means of change.

### Who are
current foundational models aligned with?

Under this definition, foundation models for text are probably quite
aligned to the heavy Internet user population (which does not imply
they’re aligned in a particularly just way!). However, even these models
are not quite representative of Internet users; their governance
probably looks more like a government with weird rules baked into the
constitution (e.g. using posts with 3+ karma to filter WebText may bias
towards Reddit users specifically).

### Does this
mean DIY / personal models are "unaligned"?

Most likely, yes! But that's ok.

If I train my own model on records of my own behaviors to make
recommendations to myself, this model is very aligned to me as an
individual and probably not very aligned to society (unless I happen to
represent some “behaviorally median citizen”).

Rather than calling this "unaligned", we might say the alignment of
these systems is highly concentrated. We can think of plural alignment
more as an inequality measurement than a scalar score.

### Can
profit-driven AI systems ever be broadly aligned under this
definition?

Most AI systems operated with the main goal of directly making money
(as opposed to systems operated by the research arms of firms) are
probably aligned to the subset of “profitable users”. This may seem
obvious, but is worth repeatedly emphasizing!

### This
definition seems like it sets the bar too high -- will systems ever
really meet these standards for transparency and agency?

A key idea is that as a first step towards alignment, we must
simultaneously increase transparency around AI and support data
literacy. These are challenging asks, and the subject of active
research!

As a second step, we must not only improve our tools, norms, and
policies around how data is governed, but we likely also need to broadly
decentralized power in society. A society with high levels of power
concentration does not permit data agency. This means we must worry
about feedback loops. To “align AI” and avoid AI that causes harms like
economic concentration, we need to avoid economic concentration.

### Is this
meant to solve a specific harmful AI scenario?

No, this definition is abstracted away from specific concerns, which
is a weakness. But it is very possible to frame specific harm-reduction
research projects in terms of this "plural alignment".

Source revision history

Selected Git commits that changed this source file.

- 9fb4674b8a 2026-07-12 - Migrate blog into digital presence monorepo

Mirror freshness

Maintenance status for tracked full-copy mirrors of this post.

-
Current
substack

mirror 2023-03-02

Baseline from original_url

Source and AT Protocol record

Source path
content/writing/posts/2023-03-02-measuring-relative-ai-alignment-in-terms-of-data-pipelines.md

AT Protocol URI
at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.document/3mizedrbswalv

Exact public AT Protocol record cached for the Leaflet/Bluesky-facing copy.

{
"uri": "at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.document/3mizedrbswalv",
"cid": "bafyreihhm2htq6ef2jigaptz5mlrp2comdwxb6od6ze4x3e6tb2fbx6xt4",
"value": {
"path": "/3mizedrbswalv",
"site": "at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.publication/3lzrsw2kvwc2m",
"$type": "site.standard.document",
"title": "Plural AI Data Alignment",
"content": {
"$type": "pub.leaflet.content",
"pages": [
{
"$type": "pub.leaflet.pages.linearDocument",
"blocks": [
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.image",
"image": {
"$type": "blob",
"ref": {
"$link": "bafkreidobbaa2q36jfjfxe75sohqk56npn4azwlfwaxruv7rtlweuz7lwm"
},
"mimeType": "image/jpeg",
"size": 96142
},
"aspectRatio": {
"$type": "pub.leaflet.blocks.image#aspectRatio",
"width": 480,
"height": 599
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
"byteEnd": 338,
"byteStart": 329
},
"features": [
{
"uri": "https://www.plurality.institute/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "In this post, I propose an approach to score AI systems in terms of how well they align with the interests of different groups, by measuring the ability for data creators to reason about and configure the systems' underlying \"data pipelines\". This is meant to provide a path towards measuring alignment in a manner that supports plurality, i.e. these scores can help us predict when AI systems are likely to \"facilitate cooperation and flourishing across a diversity of social groups\"."
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
"byteEnd": 266,
"byteStart": 248
},
"features": [
{
"uri": "https://www.plurality.institute/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 148,
"byteStart": 141
},
"features": [
{
"uri": "https://casmi.northwestern.edu/news/articles/2023/defining-safety-in-artificial-intelligence.html",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 89,
"byteStart": 85
},
"features": [
{
"uri": "https://openai.com/blog/planning-for-agi-and-beyond",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "This post was primarily inspired by discussions kicked off by OpenAI’s recent blog post. It is also informed by my recent participation in efforts to further define directions for “AI Safety” research and recent efforts to define and advance plurality research."
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
"byteEnd": 202,
"byteStart": 190
},
"features": [
{
"uri": "https://arch.library.northwestern.edu/concern/generic_works/jq085k38d?locale=en",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "I’ve used the term \"AI\" in the title because this is the term being used in ongoing discussions, and I think this ship has definitively sailed (full disclosure: I also used the term in my dissertation, so I suppose I’ve already bought in a bit). More specifically, I am talking about computing systems that rely on some combination of distinct datasets for training, evaluation, and/or calibration. The discussion is especially relevant to “generative AI” that produces text and images, like ChatGPT and StableDiffusion, but was originally influenced by earlier work looking at search and recommendation."
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
"byteEnd": 239,
"byteStart": 232
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "The post will be structured as such: a two sentence definition, followed by a two-paragraph definition with more details, followed by an \"FAQ\" with even more details (the first version will be an IFAQ, because these are questions I imagine might be frequent)."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 1,
"facets": [],
"plaintext": "Two-Sentence Definition"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "An AI system is more aligned with a coalition if members (1) know how their data contributions flow to that system, (2) can reason about how changes to data flow might impact AI capabilities, and (3) have agency to reconfigure these data flows."
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
"byteEnd": 122,
"byteStart": 109
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "By measuring the alignment of various systems to various coalitions, we can understand alignment in terms of concentration: some systems are aligned to just a few individuals, others to very broad groups, and others to specific subgroups."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 1,
"facets": [],
"plaintext": "Two-Paragraph Definition"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "We can measure the relative alignment of data-dependent systems to the preferences of various coalitions in terms of data contributors’ knowledge about data flows and ability to reconfigure these flows. Specifically, we will set three thresholds: (1) a threshold for awareness of data pipelines, (2) a threshold for ability for people to reason about data impact, and (3) a threshold for minimum agency to configure data pipelines and attempt to the count the number of people who meet these criteria. We make the following assumption: if people understand how their data contributions impact AI capabilities and can easily act to configure how these contributions flow to different organizations and systems, over time people will act (i.e., use the “data levers” available to them) to improve the capabilities of systems and organizations they support and hinder those they do not. We can score a system’s alignment by estimating the fraction of data contributors who meet some standard for data transparency and agency (i.e., are informed enough about data flows and can reconfigure their data flows with low enough cost). Under this definition, a system becomes more aligned to a coalition when more users are given high-quality information about data flow (including estimates of data’s impact on capabilities) and low cost options to redirect that data flow. Then, a system can be understand in terms of the concentration of its alignment between different groups."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "This definition most likely requires a collective approach to data agency — time costs may make it impossible for individual people to make decisions about how individual data records flow to individual firms (providing prohibitively expensive but \"technically possible\" actions is not agency). Instead, we could support data agency by scaffolding data-mediating organizations. Finally, this definition supports a pluralistic approach to alignment: given there are many distinct coalitions of people in the world, any given system has a variety of alignment scores, and any attempt to produce a single alignment score requires explicitly weighting the preferences of different groups. Instead, we can understand alignment scores as a variable to be used similarly to inequality measurements."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 1,
"facets": [],
"plaintext": "FAQ"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "Are there other hidden assumptions here?"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "There is an assumption that competing organizations and systems will exist. This definition is not particularly useful in an ecosystem dominated by a single player."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "Why do we need to solve a governance problem with data contributions? What if people just vote directly on issues of AI Governance, or continue to vote for elected officials who pass legislation?"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "This idea is complementary to other mechanisms for AI governance. Indeed, a paradigm in which everyone has access to lots of information about AI systems and votes directly on AI-related policy could achieve the same outcomes. The data pipeline focus is particularly promising because it's very feasible; it emerges from a \"natural\" dependency in AI systems."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "How does this idea relate to existing AI Alignment work?"
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
"byteEnd": 62,
"byteStart": 43
},
"features": [
{
"uri": "https://openai.com/blog/our-approach-to-alignment-research/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "In the blog post, OpenAI links to to their Alignment page post, which emphasizes the goal of making \"artificial general intelligence (AGI) aligned with human values and follow human intent”."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "This line of work includes research directions such as developing new techniques for collecting and using human feedback, training explanatory models that become part of the human evaluation loop, and performing core research on machine learning explainability and robustness."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "The definition proposed above also relates to explainability, but the standards for \"how explainable\" are embedded in what we decide is a reasonable definition for “high-quality information about data flow” and the standards for robustness are embedded in how much additional agency to change data people are given."
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
"byteEnd": 167,
"byteStart": 158
},
"features": [
{
"uri": "https://arxiv.org/abs/2109.13916",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 107,
"byteStart": 103
},
"features": [
{
"uri": "https://dl.acm.org/doi/abs/10.1145/3306618.3314250",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 101,
"byteStart": 90
},
"features": [
{
"uri": "https://link.springer.com/article/10.1007/s11023-020-09539-2",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Of course, AI Alignment has been tackled by a variety of scholars, see e.g. philosophical scholarship, work drawing on computer science and contract law, and arguments from machine learning scholars."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "(These are just a few examples: please let me know if there are additional examples that would be particularly relevant here and/or important to elevate.)"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "How do we define standards for \"transparent enough\" and \"agentic enough\""
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "The above definition implies that we can agree on some reasonable standard for providing transparency about data pipelines and a reasonable definition of when individuals or groups have \"agency\" to control data flows. However, these ideas are highly contestable -- you might think my definition of transparency (say, a static datasheet and interactive data explorer) is too high of a bar, or not high enough (compared to say, a set of YouTube videos explaining existing data flows). Similarly, we might disagree about what \"reasonable\" costs are to withhold or redirect data. For instance, if changing data contribution flows requires technical know-how or monetary costs, a large number of data contributors may feel stuck in their current configurations (i.e., they may just keep providing data to all the actors they currently engage with / they might just keep using the same platforms in the same way)."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "These questions themselves are governance questions. Realistically, the initial thresholds will be set by tech companies themselves, and then academics and activists may push to change these thresholds. Personally, I think this is a decent way to move forward."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "This seems to require attributing data to individuals or groups; how do we do that?"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "For any given AI system, we can definitively identify a training set and test set. This test set is typically meant to be a proxy for the set of cases for which a system will actually be used, i.e. a “deployment set”. We can only guess at what this deployment set will look like until the model is deployed in practice."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "For each of these sets, we can try to attribute the individual records (i.e., units of data) to individual people or to groups. Once we’ve done this, we can produce a moment-in-time snapshot of what interests are represented in the data. This kind of practice is actually already common for certain groups. For instance, in NLP research it would be very common to describe the fraction of data belonging to different written languages. In social computing, it might be reasonable to how much data comes from predefined or inferred communities (e.g. group by subreddits or by clusters of user behaviors). In work on responsible AI, it’s very common to study training data in terms of demographic representation."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "A promising direction for solving some of the thorny problems with individual attribution is to support infrastructure for associating data contributions with existing online communities or explicitly labeled \"data coalitions\" that people join and leave, and dealing with attribution primarily at the community level."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "How does this work if there are consistent differences between how training data is collected and how the system is deployed in practice?"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "A key problem arises when neither the training set or test set overlap with the actual deployment set. When this happens, our alignment score becomes uninformative! But, organizations have a natural incentive to avoid this situation: if this keeps happening, their systems will perform poorly."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "How often should this data pipeline alignment score be computed?"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "For this definition to be useful, we’d likely want to continuously estimate this fraction over time, as individuals or groups reconfigure flow of information and knowledge to systems. Capabilities should slowly rise and fall — if they’re entirely static, we might imagine there is not much governance going on (in the same way we might be concerned if a single political party continuously dominates a ostensibly bipartisan system for hundreds of years)."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "A monthly update is likely a reasonable starting point; we'd expect people to use data levers as long-term means of change."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "Who are current foundational models aligned with?"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Under this definition, foundation models for text are probably quite aligned to the heavy Internet user population (which does not imply they’re aligned in a particularly just way!). However, even these models are not quite representative of Internet users; their governance probably looks more like a government with weird rules baked into the constitution (e.g. using posts with 3+ karma to filter WebText may bias towards Reddit users specifically)."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "Does this mean DIY / personal models are \"unaligned\"?"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Most likely, yes! But that's ok."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "If I train my own model on records of my own behaviors to make recommendations to myself, this model is very aligned to me as an individual and probably not very aligned to society (unless I happen to represent some “behaviorally median citizen”)."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Rather than calling this \"unaligned\", we might say the alignment of these systems is highly concentrated. We can think of plural alignment more as an inequality measurement than a scalar score."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "Can profit-driven AI systems ever be broadly aligned under this definition?"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Most AI systems operated with the main goal of directly making money (as opposed to systems operated by the research arms of firms) are probably aligned to the subset of “profitable users”. This may seem obvious, but is worth repeatedly emphasizing!"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "This definition seems like it sets the bar too high -- will systems ever really meet these standards for transparency and agency?"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "A key idea is that as a first step towards alignment, we must simultaneously increase transparency around AI and support data literacy. These are challenging asks, and the subject of active research!"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "As a second step, we must not only improve our tools, norms, and policies around how data is governed, but we likely also need to broadly decentralized power in society. A society with high levels of power concentration does not permit data agency. This means we must worry about feedback loops. To “align AI” and avoid AI that causes harms like economic concentration, we need to avoid economic concentration."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "Is this meant to solve a specific harmful AI scenario?"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "No, this definition is abstracted away from specific concerns, which is a weakness. But it is very possible to frame specific harm-reduction research projects in terms of this \"plural alignment\"."
}
}
]
}
]
},
"description": "Measuring the Alignment of AI Systems Based on their Data Pipelines",
"publishedAt": "2023-03-02T00:00:00.000Z"
}
}
