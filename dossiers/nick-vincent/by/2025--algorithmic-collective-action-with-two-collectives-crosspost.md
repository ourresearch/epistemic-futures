---
title: "Algorithmic Collective Action With Two Collectives [crosspost]"
person: "nick-vincent"
section: "by"
type: "blog-post"
year: 2025
date: "2025-06-20"
venue: "Data Leverage (Digital Garden / dataleverage.substack.com)"
authors: "Nicholas Vincent"
source_url: "https://nickmvincent.github.io/long-posts/algorithmic-collective-action-with.html"
retrieved: "2026-08-13"
content: "full-text"
notes: "Dek: This post was written by Aditya Karan, with support from Nick Vincent and Karrie Karahalios to accompany a FAccT 2025 paper. It was originally published on Jun 19, 2025 via the Crowd Dynamics Lab blog. Garden section: long-posts. Mirrored on the Data Leverage Substack."
---

# Algorithmic Collective Action With Two Collectives [crosspost]

## Full text

This post was written by Aditya
Karan, with support from Nick Vincent and Karrie Karahalios to
accompany a FAccT 2025 paper. It was originally
published on Jun 19, 2025 via the Crowd Dynamics Lab blog.

### Summary

Swifties organizing to promote new versions of songs, artists
intentionally adding adversarial watermarks to protect their own work,
and people adding positive articles about themselves to make LLMs make
positive associations with their name. All of these examples demonstrate
how people can change their behavior to get specific outcomes out of ML
systems. Algorithmic Collective Action (ACA) encompasses many such
situations in which groups of people engage in some coordinated activity
to achieve a certain result from a ML model. From empirical
examples, and prior
theoretical work, we see that small collectives really can alter the
behavior of ML models (often focusing on a certain subset of the data)
by engaging in collective action.

As these large systems are expected to grow, multiple groups may try
to engage in collective action. These groups can have different
objectives and because of the complexity and often blackbox nature of
these models, it’s hard to predict what could happen. If we think of
each of these collectives as trying to adjust the underlying model
behavior (weights), what happens when multiple collectives try to do the
same thing? How should we reason about ACA when multiple collectives are
at play?

### What we did

Our paper (appearing
at ACM FAccT 2025) explores
this design space in several ways. We first introduce a collective
action framework, which formalizes the components of collective action.
In particular, we note that when multiple collectives engage in the
system, the final dataset used to train composes of each of the
collective’s data modification + the unperturbed data. This ultimately
produces new parameters, which are then used to measure the group’s
collective.

The main components of collective action are:

-

Number of Collective and Objectives: What are
the collectives and what are their objectives?

-

Collective Composition: Who is making up the
collective?

-

Model Access: What level of access does the
collective have?

-

Action Availability: What actions can the
collective take?

-

Affected Party: Who is the target of collective
action?

-

Measurements: How does the collective measure
its own success? In introducing this framework, we aim to support
further exploration into, and consideration of, the factors that go into
determining possible outcomes of collective action, especially in the
presence of multiple groups.

To illustrate the point, we also designed experiments to understand
the success of collective action when two collectives participate vs
just one. It turns out just adding one more collective already adds a
lot of complexity into collective action scenarios. Consider a scenario
where a company uses AI to analyze resumes. This collective, really
wanting to get a certain job, works together to plan to slightly modify
their resumes to cause an ML model to output particular classification
results. We denote the individual classes with letters A/B and unique
characters with numbers. For example A100 is targeting class A with a
character identified with “100” (actual characters used can be found in
the paper) We find that depending on the specific modification strategy,
these collectives can either hurt or help each other. For example, below
we see the collective’s hurting each other when both are acting.

While in other cases, there’s very little impact.

Why is this important? It suggests that examining collective action
in isolation could obscure the important interaction effects that occur
when multiple groups engage. More broadly speaking, it also signals the
need to understand what outcomes different groups want out of ML
systems, and what changes or strategies they may use to achieve this
desired goal. It behooves both platforms and other collectives to
understand these dynamics and how they may affect ML systems more
broadly.

This framework also opens many other avenues to explore to further
understand important considerations in algorithmic collective action.
For platform developers, understanding how and why different groups
might want different outcomes from ML models can help illustrate a
stronger understanding of how data is generated. For organizers,
understanding how to avoid conflicts with other groups, and how to
optimize the composition could play a key role in success.

We examine some of these implications further in our full paper. We
hope that our framework and experiments serve as launching points to
explore more deeply the power and limitations of collective action on
algorithmic system. The paper, which also dives into other set of
experiments looking at heterogeneity and discusses on the role
collective action may or should play in data generations and models, can
be found here!

### Addendum

Exploring the role of heterogeneity in collective effectiveness

We also used the above framework to explore the impact of homogeneity
of collective members in the effectiveness of collective action. We find
that for a recommender system case, where some groups are trying to
promote/demote specific content, group size has more of an impact, but
groups that are somewhere in between fully homogenous and fully
heterogenous can offer some performance boost.

These experiments further demonstrate the need to understand the
specific collectives, their goals and composition, to truly understand
how algorithmic collective action might come about in practice.

Source revision history

Selected Git commits that changed this source file.

- 9fb4674b8a 2026-07-12 - Migrate blog into digital presence monorepo

Mirror freshness

Maintenance status for tracked full-copy mirrors of this post.

-
Current
substack

mirror 2025-06-20

Baseline from original_url

Source and AT Protocol record

Source path
content/writing/posts/2025-06-20-algorithmic-collective-action-with.md

AT Protocol URI
at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.document/3mizedjjxauxp

Exact public AT Protocol record cached for the Leaflet/Bluesky-facing copy.

{
"uri": "at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.document/3mizedjjxauxp",
"cid": "bafyreic46bthojx3ajmwernyci5zyh3unrzlmsi4xcb5b4wrchk5v5vbva",
"value": {
"path": "/3mizedjjxauxp",
"site": "at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.publication/3lzrsw2kvwc2m",
"$type": "site.standard.document",
"title": "Algorithmic Collective Action With Two Collectives [crosspost]",
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
"$link": "bafkreie4xfg47ysbedbvipod32rz57yclsx67ouyv3cc6n5uxooyv5biau"
},
"mimeType": "image/png",
"size": 30615
},
"aspectRatio": {
"$type": "pub.leaflet.blocks.image#aspectRatio",
"width": 1024,
"height": 683
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
"byteEnd": 201,
"byteStart": 200
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 200,
"byteStart": 196
},
"features": [
{
"uri": "https://crowddynamicslab.github.io/collective/action,/machine/learning/2025/06/19/two-collectives/",
"$type": "pub.leaflet.richtext.facet#link"
},
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 196,
"byteStart": 123
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 123,
"byteStart": 118
},
"features": [
{
"uri": "https://arxiv.org/abs/2505.00195",
"$type": "pub.leaflet.richtext.facet#link"
},
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 118,
"byteStart": 91
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 91,
"byteStart": 74
},
"features": [
{
"uri": "http://www.karriekarahalios.com/",
"$type": "pub.leaflet.richtext.facet#link"
},
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 74,
"byteStart": 37
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 37,
"byteStart": 25
},
"features": [
{
"uri": "https://adityakaran.me/",
"$type": "pub.leaflet.richtext.facet#link"
},
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 25,
"byteStart": 0
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "This post was written by Aditya Karan, with support from Nick Vincent and Karrie Karahalios to accompany a FAccT 2025 paper. It was originally published on Jun 19, 2025 via the Crowd Dynamics Lab blog."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "Summary"
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
"byteEnd": 585,
"byteStart": 563
},
"features": [
{
"uri": "https://arxiv.org/abs/2410.12633",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 557,
"byteStart": 539
},
"features": [
{
"uri": "https://www.the-independent.com/arts-entertainment/music/news/taylor-swift-fearless-fans-b1829051.html",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Swifties organizing to promote new versions of songs, artists intentionally adding adversarial watermarks to protect their own work, and people adding positive articles about themselves to make LLMs make positive associations with their name. All of these examples demonstrate how people can change their behavior to get specific outcomes out of ML systems. Algorithmic Collective Action (ACA) encompasses many such situations in which groups of people engage in some coordinated activity to achieve a certain result from a ML model. From empirical examples, and prior theoretical work, we see that small collectives really can alter the behavior of ML models (often focusing on a certain subset of the data) by engaging in collective action."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "As these large systems are expected to grow, multiple groups may try to engage in collective action. These groups can have different objectives and because of the complexity and often blackbox nature of these models, it’s hard to predict what could happen. If we think of each of these collectives as trying to adjust the underlying model behavior (weights), what happens when multiple collectives try to do the same thing? How should we reason about ACA when multiple collectives are at play?"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "What we did"
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
"byteEnd": 33,
"byteStart": 28
},
"features": [
{
"uri": "https://facctconference.org/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 9,
"byteStart": 4
},
"features": [
{
"uri": "https://arxiv.org/abs/2505.00195",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Our paper (appearing at ACM FAccT 2025) explores this design space in several ways. We first introduce a collective action framework, which formalizes the components of collective action. In particular, we note that when multiple collectives engage in the system, the final dataset used to train composes of each of the collective’s data modification + the unperturbed data. This ultimately produces new parameters, which are then used to measure the group’s collective."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "The main components of collective action are:"
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
"byteEnd": 35,
"byteStart": 0
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#bold"
}
]
}
],
"plaintext": "Number of Collective and Objectives: What are the collectives and what are their objectives?"
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
"byteEnd": 22,
"byteStart": 0
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#bold"
}
]
}
],
"plaintext": "Collective Composition: Who is making up the collective?"
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
"byteEnd": 12,
"byteStart": 0
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#bold"
}
]
}
],
"plaintext": "Model Access: What level of access does the collective have?"
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
"byteEnd": 19,
"byteStart": 0
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#bold"
}
]
}
],
"plaintext": "Action Availability: What actions can the collective take?"
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
"byteEnd": 14,
"byteStart": 0
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#bold"
}
]
}
],
"plaintext": "Affected Party: Who is the target of collective action?"
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
"byteEnd": 12,
"byteStart": 0
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#bold"
}
]
}
],
"plaintext": "Measurements: How does the collective measure its own success? In introducing this framework, we aim to support further exploration into, and consideration of, the factors that go into determining possible outcomes of collective action, especially in the presence of multiple groups."
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
"plaintext": "To illustrate the point, we also designed experiments to understand the success of collective action when two collectives participate vs just one. It turns out just adding one more collective already adds a lot of complexity into collective action scenarios. Consider a scenario where a company uses AI to analyze resumes. This collective, really wanting to get a certain job, works together to plan to slightly modify their resumes to cause an ML model to output particular classification results. We denote the individual classes with letters A/B and unique characters with numbers. For example A100 is targeting class A with a character identified with “100” (actual characters used can be found in the paper) We find that depending on the specific modification strategy, these collectives can either hurt or help each other. For example, below we see the collective’s hurting each other when both are acting."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "While in other cases, there’s very little impact."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Why is this important? It suggests that examining collective action in isolation could obscure the important interaction effects that occur when multiple groups engage. More broadly speaking, it also signals the need to understand what outcomes different groups want out of ML systems, and what changes or strategies they may use to achieve this desired goal. It behooves both platforms and other collectives to understand these dynamics and how they may affect ML systems more broadly."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "This framework also opens many other avenues to explore to further understand important considerations in algorithmic collective action. For platform developers, understanding how and why different groups might want different outcomes from ML models can help illustrate a stronger understanding of how data is generated. For organizers, understanding how to avoid conflicts with other groups, and how to optimize the composition could play a key role in success."
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
"byteEnd": 422,
"byteStart": 418
},
"features": [
{
"uri": "https://arxiv.org/abs/2505.00195",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "We examine some of these implications further in our full paper. We hope that our framework and experiments serve as launching points to explore more deeply the power and limitations of collective action on algorithmic system. The paper, which also dives into other set of experiments looking at heterogeneity and discusses on the role collective action may or should play in data generations and models, can be found here!"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "Addendum"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Exploring the role of heterogeneity in collective effectiveness"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "We also used the above framework to explore the impact of homogeneity of collective members in the effectiveness of collective action. We find that for a recommender system case, where some groups are trying to promote/demote specific content, group size has more of an impact, but groups that are somewhere in between fully homogenous and fully heterogenous can offer some performance boost."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "These experiments further demonstrate the need to understand the specific collectives, their goals and composition, to truly understand how algorithmic collective action might come about in practice."
}
}
]
}
]
},
"description": "This post was written by Aditya Karan, with support from Nick Vincent and Karrie Karahalios to accompany a FAccT 2025 paper. It was originally published on Jun 19, 2025 via the Crowd Dynamics Lab blog.",
"publishedAt": "2025-06-20T00:00:00.000Z"
}
}
