---
title: "How collective bargaining for information, public AI, and HCI research all fit together"
person: "nick-vincent"
section: "by"
type: "blog-post"
year: 2025
date: "2025-10-11"
venue: "Data Leverage (Digital Garden / dataleverage.substack.com)"
authors: "Nicholas Vincent"
source_url: "https://nickmvincent.github.io/long-posts/how-collective-bargaining-for-information.html"
retrieved: "2026-08-13"
content: "full-text"
notes: "Dek: Another recap post for the Data Leverage newsletter! Garden section: long-posts. Mirrored on the Data Leverage Substack."
---

# How collective bargaining for information, public AI, and HCI research all fit together

## Full text

Photo by Kelly
Sikkema on Unsplash

This is a recap post (a big round-up of links to content I’ve
written recently). It will likely be updated once or twice, with a
change log up top.

Change log:

- Nov 18: minor prose clean-up.

I’ve written quite a few newsletters in the past months. One of my
reasons for working on all these newsletters is to write, and thus
think, in public. (I’ve also been trying to populate more content on
several sites that provide “externalized notes”, e.g. on data licenses and data napkin math). To contextualize
these numerous posts, I’m going to summarize the various positions I’ve
taken. I’ll also try to pull out a few resolvable predictions from my
“positions”. Also: nothing in this post is meant to reflect the opinions
of my co-authors, i.e., opinions expressed here are my own, do not
reflect my employer or colleagues, etc.

At a high level, (I think) my “core positions” consist of two
distinct ideas:

Data leverage: Data flow can, and should, be used as
a governance lever. [2020 FAccT paper: ACM DL | arxiv] [2022
Dissertation]

-

Collective bargaining for information (CBI):
Specifically, for data flow to be an effective governance lever, society
should enable collective bargaining for information. This can enable
more efficient markets for information, healthier information
ecosystems, and mitigate some harms from AI [2025 NeurIPS position
paper: arxiv].

-

Concretely, CBI requires legal support for appropriate bargaining
institutions. It also requires the design and deployment of interfaces
for actually making preference choices, as well as technical support for
the actual transfer of data between database systems (see e.g. recent
work on a “Human
Context Protocol”).

-

One immediate ask to make CBI viable: we need clear rules about
how anti-trust will, or will not, be applied to content producers in the
AI age. In our recent paper, we argue this is quite urgent.

Public AI (pAI): we should build AI systems that are
publicly accessible and accountable [public AI network website] [publicai.co inference utility
product]

-

pAI as a concept encapsulates more than just data flow (building
pAI requires also thinking about energy, compute, geopolitics, etc.),
but in general pAI connects with data leverage and CBI in two ways.
First, the accountability element of public AI can help to foster
healthier data flow. Second, data leverage and CBI can provide a source
of accountability for the public.

-

Further, there are other ways that PAI and data-centric AI
connect, especially around the potential for dataset documentation and
data appraisal.

-

Public AI can support “public AI Data flywheels” [GitHub repo for a
“mini-book” + example implementation].

-

Public AI can also massively complement open source AI efforts
[CodeML @ ICML paper: arxiv]

While not positions per se, in my writing and research I
also promote a more general “we should bring empirical human-computer
interaction and computational social science to AI” attitude. This
involves writing about interfaces for data-dependent technologies,
evaluating new AI models (e.g., auditing and analyzing LLM
behavior in high-stakes contexts), studying online platforms (e.g.,
continuing to study knowledge
gaps in Wikipedia, studying governance and
responsible AI practices on HuggingFace), and thinking about “AI
literacy”.

To recap chronologically, here is a list of blogs, summarized in one
or two sentences, starting from November 2023:

-

In most policy contexts, we need to consider a systems-level data
pipeworks model that emphasizes feedback loops [substack].
More recently, I summarized this model in Section 1.3. of the “Public AI
Data Flywheel mini-book” [GitHub
pages].

-

We should focus on “diffs” when we work with
LLMs, and consider using multiple models at once [substack].

- Note: I’d like to think this was reasonably forward looking re: the
success of CLI tools like Codex and Claude Code. I like using these
tools much more than web based LLM interfaces!

-

Data value estimators should focus on group-level data values [longer
substack] [substack
microblog].

-

Dataset details might become important to consumers, in a similar
vein to how we think about “proprietary blend” vs. “open” supplement
blends [substack].

- Concrete prediction: As AI products become even more widespread, we
will see a new market segment emerge of consumers who care about
which people contributed to training or evaluation.

-

The possibility of model distillation means that the current data
paradigm is “live by the sword, die by the sword” for AI companies,
meaning that AI companies may face the similar challenges to content
organizations. [substack].
One way to improve the current paradigm might involve AI labs sharing
their data protection technologies [substack].

- Concrete prediction: We will see at least one or more serious AI
player come out in favor of some kind of technical or regulatory IP
protection for AI outputs.

-

We should consider the possibility of “tipping points for content
ecosystems” that actually cause AI to get worse in some domains [substack].

- Concrete prediction: In 2026, we will see evidence of some
capability domains that have clearly been negatively impacted by
“content ecosystem impacts”.

-

Evaluation data leverage has massive potential [substack].

-

Concrete prediction: We will see at least one professional
organization (medicine, law), use evaluation data leverage by refusing
to “approve” the use of some high functioning AI model.

-

Concrete prediction: We will see AI companies seek to dissolve
evaluation data leverage by structuring most evaluation jobs as
contract, non-permanent positions with little workplace
communication.

-

A consortium of public AI labs can share experiments and
checkpoints in a way that will provide some level of “natural data
appraisal” [substack].
This idea connects with public AI x open source AI and public AI in the
context of Canada.

-

We can (and should) view many types of platforms as competing in
the same ranking tasks. [substack]

-

We can (and should) view the utility from AI systems as stemming
from upstream acts of human knowledge curation. A search result or AI
output is the culmination of efforts from various people: people who
actually wrote the Wikipedia article, people who completed the
post-training data tasks, computer scientists who write the data
ingestion pipeline or designed the training objective, engineers who
solved the practical engineering challenges, etc. [substack]

-

Dataset documentation, auditing, LLM social simulation, assessing
the ethics of a particular AI use case, and more are all connected via
this broader point: “when we use AI models, we’re making our decision
through either formal or informal feedback about whether the weighted
combination of chunks of information we got met our needs” [substack]

-

AI does pose a credible threat of creating large shocks to labor
markets. This may also cause large shifts in the overall concentration
of wealth, and importantly, power. Collective bargaining for information
is a critical countervailing force. [substack]

-

At some point, for certain models/datasets, it might be time to
assume most public information is “in” the model and instead
try to count up the information that’s not in the model. Society should
also have a normative discussion about what data sources should be
included and expected by default in AI model weights or retrieval sets
[substack]

During this time, various research projects I’ve been involved with
also intersect with these various positions (some are mentioned
above):

-

Furthering understanding of algorithmic collective action [FAccT
2025: substack,
arxiv]

- Connects especially with CBI arguments — we need to advance our
overall empirical understanding of collective action’s impact on AI
capabilities to foster effective bargaining

-

Measuring and improving “attentional agency” [FAccT 2025: arxiv]

-

Evaluation of LLMs in high-stakes context such as medical
misinformation jailbreaks [AIES 2025: arxiv]

-

Understanding governance practices empirically [AIES 2025: arxiv]

Some topics that I’ve micro-blogged about (I sometimes microblog
directly to a “blogs” GitHub repo),
and hope to write some longer thoughts on:

-

The use of the term synthetic
data. See also discussion on this Tweet.

-

A number of externalized notes on “ideas I think are interesting”
here

Source revision history

Selected Git commits that changed this source file.

- 9fb4674b8a 2026-07-12 - Migrate blog into digital presence monorepo

Mirror freshness

Maintenance status for tracked full-copy mirrors of this post.

-
Current
substack

mirror 2025-10-11

Baseline from original_url

Source and AT Protocol record

Source path
content/writing/posts/2025-10-11-how-collective-bargaining-for-information.md

AT Protocol URI
at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.document/3mizeegveadsg

Exact public AT Protocol record cached for the Leaflet/Bluesky-facing copy.

{
"uri": "at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.document/3mizeegveadsg",
"cid": "bafyreigpyxsbnpnzbfzusqy4yipteqi6xjkcszn7huk424fyl6ybw7fjse",
"value": {
"path": "/3mizeegveadsg",
"site": "at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.publication/3lzrsw2kvwc2m",
"$type": "site.standard.document",
"title": "How collective bargaining for information, public AI, and HCI research all fit together",
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
"$link": "bafkreiccawwucmwswsdfoju7j6nawmlqutzglbe3nwgpph7nucnzwcxina"
},
"mimeType": "image/jpeg",
"size": 130770
},
"aspectRatio": {
"$type": "pub.leaflet.blocks.image#aspectRatio",
"width": 1080,
"height": 703
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
"byteEnd": 34,
"byteStart": 26
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
"byteEnd": 22,
"byteStart": 9
},
"features": [
{
"uri": "https://unsplash.com/@kellysikkema",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Photo by Kelly Sikkema on Unsplash"
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
"byteEnd": 149,
"byteStart": 0
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "This is a recap post (a big round-up of links to content I’ve written recently). It will likely be updated once or twice, with a change log up top."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Change log:"
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
"facets": [],
"plaintext": "Nov 18: minor prose clean-up."
}
}
]
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
"byteEnd": 653,
"byteStart": 571
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
"byteEnd": 302,
"byteStart": 286
},
"features": [
{
"uri": "https://exploringai.org/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 281,
"byteStart": 268
},
"features": [
{
"uri": "https://datalicenses.org/?sort=recent",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "I’ve written quite a few newsletters in the past months. One of my reasons for working on all these newsletters is to write, and thus think, in public. (I’ve also been trying to populate more content on several sites that provide “externalized notes”, e.g. on data licenses and data napkin math). To contextualize these numerous posts, I’m going to summarize the various positions I’ve taken. I’ll also try to pull out a few resolvable predictions from my “positions”. Also: nothing in this post is meant to reflect the opinions of my co-authors, i.e., opinions expressed here are my own, do not reflect my employer or colleagues, etc."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "At a high level, (I think) my “core positions” consist of two distinct ideas:"
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
"byteEnd": 126,
"byteStart": 109
},
"features": [
{
"uri": "https://arch.library.northwestern.edu/concern/generic_works/jq085k38d?locale=en",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 106,
"byteStart": 101
},
"features": [
{
"uri": "https://arxiv.org/abs/2012.09995",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 98,
"byteStart": 92
},
"features": [
{
"uri": "https://dl.acm.org/doi/10.1145/3442188.3445885",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 13,
"byteStart": 0
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#bold"
}
]
}
],
"plaintext": "Data leverage: Data flow can, and should, be used as a governance lever. [2020 FAccT paper: ACM DL | arxiv] [2022 Dissertation]"
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
"byteEnd": 328,
"byteStart": 323
},
"features": [
{
"uri": "https://arxiv.org/abs/2506.10272",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 43,
"byteStart": 0
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#bold"
}
]
}
],
"plaintext": "Collective bargaining for information (CBI): Specifically, for data flow to be an effective governance lever, society should enable collective bargaining for information. This can enable more efficient markets for information, healthier information ecosystems, and mitigate some harms from AI [2025 NeurIPS position paper: arxiv]."
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
"byteEnd": 315,
"byteStart": 293
},
"features": [
{
"uri": "https://miba.dev/assets/publications/HCP_ArXiv_2025.pdf",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Concretely, CBI requires legal support for appropriate bargaining institutions. It also requires the design and deployment of interfaces for actually making preference choices, as well as technical support for the actual transfer of data between database systems (see e.g. recent work on a “Human Context Protocol”)."
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "One immediate ask to make CBI viable: we need clear rules about how anti-trust will, or will not, be applied to content producers in the AI age. In our recent paper, we argue this is quite urgent."
}
}
]
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
"byteEnd": 129,
"byteStart": 118
},
"features": [
{
"uri": "https://publicai.co/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 115,
"byteStart": 108
},
"features": [
{
"uri": "https://publicai.network/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 16,
"byteStart": 0
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#bold"
}
]
}
],
"plaintext": "Public AI (pAI): we should build AI systems that are publicly accessible and accountable [public AI network website] [publicai.co inference utility product]"
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
"facets": [],
"plaintext": "pAI as a concept encapsulates more than just data flow (building pAI requires also thinking about energy, compute, geopolitics, etc.), but in general pAI connects with data leverage and CBI in two ways. First, the accountability element of public AI can help to foster healthier data flow. Second, data leverage and CBI can provide a source of accountability for the public."
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Further, there are other ways that PAI and data-centric AI connect, especially around the potential for dataset documentation and data appraisal."
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
"byteEnd": 65,
"byteStart": 61
},
"features": [
{
"uri": "https://github.com/nickmvincent/paidf_consultation",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Public AI can support “public AI Data flywheels” [GitHub repo for a “mini-book” + example implementation]."
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
"byteEnd": 90,
"byteStart": 85
},
"features": [
{
"uri": "https://arxiv.org/abs/2507.09296",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Public AI can also massively complement open source AI efforts [CodeML @ ICML paper: arxiv]"
}
}
]
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
"byteEnd": 449,
"byteStart": 441
},
"features": [
{
"uri": "https://arxiv.org/abs/2409.19104",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 426,
"byteStart": 412
},
"features": [
{
"uri": "https://arxiv.org/abs/2505.24195",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 305,
"byteStart": 297
},
"features": [
{
"uri": "https://arxiv.org/abs/2508.10010",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 27,
"byteStart": 20
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "While not positions per se, in my writing and research I also promote a more general “we should bring empirical human-computer interaction and computational social science to AI” attitude. This involves writing about interfaces for data-dependent technologies, evaluating new AI models (e.g., auditing and analyzing LLM behavior in high-stakes contexts), studying online platforms (e.g., continuing to study knowledge gaps in Wikipedia, studying governance and responsible AI practices on HuggingFace), and thinking about “AI literacy”."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "To recap chronologically, here is a list of blogs, summarized in one or two sentences, starting from November 2023:"
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
"byteEnd": 240,
"byteStart": 228
},
"features": [
{
"uri": "https://nickmvincent.github.io/paidf_consultation/01c_pipeworks.html",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 122,
"byteStart": 114
},
"features": [
{
"uri": "https://dataleverage.substack.com/p/building-a-data-pipeworks-for-democratic",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "In most policy contexts, we need to consider a systems-level data pipeworks model that emphasizes feedback loops [substack]. More recently, I summarized this model in Section 1.3. of the “Public AI Data Flywheel mini-book” [GitHub pages]."
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
"byteEnd": 107,
"byteStart": 99
},
"features": [
{
"uri": "https://dataleverage.substack.com/p/many-models-and-track-changes-for",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 27,
"byteStart": 22
},
"features": [
{
"uri": "https://en.wikipedia.org/wiki/Diff",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "We should focus on “diffs” when we work with LLMs, and consider using multiple models at once [substack]."
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
"byteEnd": 99,
"byteStart": 81
},
"features": [
{
"uri": "https://dataleverage.substack.com/p/microblog-one-book-is-worth-006-benchmark",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 78,
"byteStart": 63
},
"features": [
{
"uri": "https://dataleverage.substack.com/p/is-zuckerberg-right-to-say-that-your",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Data value estimators should focus on group-level data values [longer substack] [substack microblog]."
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
"byteEnd": 159,
"byteStart": 151
},
"features": [
{
"uri": "https://dataleverage.substack.com/p/selling-agi-like-ag1-will-the-market",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Dataset details might become important to consumers, in a similar vein to how we think about “proprietary blend” vs. “open” supplement blends [substack]."
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
"byteEnd": 348,
"byteStart": 340
},
"features": [
{
"uri": "https://dataleverage.substack.com/p/ai-labs-could-open-source-data-protection",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 231,
"byteStart": 223
},
"features": [
{
"uri": "https://dataleverage.substack.com/p/live-by-the-free-content-for-training",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "The possibility of model distillation means that the current data paradigm is “live by the sword, die by the sword” for AI companies, meaning that AI companies may face the similar challenges to content organizations. [substack]. One way to improve the current paradigm might involve AI labs sharing their data protection technologies [substack]."
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
"byteEnd": 143,
"byteStart": 135
},
"features": [
{
"uri": "https://dataleverage.substack.com/p/tipping-points-for-content-ecosystems",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "We should consider the possibility of “tipping points for content ecosystems” that actually cause AI to get worse in some domains [substack]."
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
"byteEnd": 56,
"byteStart": 48
},
"features": [
{
"uri": "https://dataleverage.substack.com/p/evaluation-data-leverage-advances",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Evaluation data leverage has massive potential [substack]."
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
"byteEnd": 148,
"byteStart": 140
},
"features": [
{
"uri": "https://dataleverage.substack.com/p/public-ai-data-appraisal-and-data",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "A consortium of public AI labs can share experiments and checkpoints in a way that will provide some level of “natural data appraisal” [substack]. This idea connects with public AI x open source AI and public AI in the context of Canada."
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
"byteEnd": 98,
"byteStart": 90
},
"features": [
{
"uri": "https://dataleverage.substack.com/p/google-and-tiktok-rank-bundles-of",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "We can (and should) view many types of platforms as competing in the same ranking tasks. [substack]"
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
"byteEnd": 460,
"byteStart": 452
},
"features": [
{
"uri": "https://dataleverage.substack.com/p/each-instance-of-ai-utility-stems",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "We can (and should) view the utility from AI systems as stemming from upstream acts of human knowledge curation. A search result or AI output is the culmination of efforts from various people: people who actually wrote the Wikipedia article, people who completed the post-training data tasks, computer scientists who write the data ingestion pipeline or designed the training objective, engineers who solved the practical engineering challenges, etc. [substack]"
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
"byteEnd": 351,
"byteStart": 343
},
"features": [
{
"uri": "https://dataleverage.substack.com/p/how-do-we-know-our-ai-output-is-good",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Dataset documentation, auditing, LLM social simulation, assessing the ethics of a particular AI use case, and more are all connected via this broader point: “when we use AI models, we’re making our decision through either formal or informal feedback about whether the weighted combination of chunks of information we got met our needs” [substack]"
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
"byteEnd": 254,
"byteStart": 246
},
"features": [
{
"uri": "https://dataleverage.substack.com/p/on-ai-driven-job-apocalypses-and",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "AI does pose a credible threat of creating large shocks to labor markets. This may also cause large shifts in the overall concentration of wealth, and importantly, power. Collective bargaining for information is a critical countervailing force. [substack]"
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
"byteEnd": 350,
"byteStart": 342
},
"features": [
{
"uri": "https://dataleverage.substack.com/p/which-datasets-should-we-assume-are",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 97,
"byteStart": 95
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "At some point, for certain models/datasets, it might be time to assume most public information is “in” the model and instead try to count up the information that’s not in the model. Society should also have a normative discussion about what data sources should be included and expected by default in AI model weights or retrieval sets [substack]"
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
"plaintext": "During this time, various research projects I’ve been involved with also intersect with these various positions (some are mentioned above):"
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
"byteEnd": 86,
"byteStart": 81
},
"features": [
{
"uri": "https://arxiv.org/abs/2505.00195",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 79,
"byteStart": 71
},
"features": [
{
"uri": "https://dataleverage.substack.com/p/algorithmic-collective-action-with",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Furthering understanding of algorithmic collective action [FAccT 2025: substack, arxiv]"
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
"byteEnd": 67,
"byteStart": 62
},
"features": [
{
"uri": "https://arxiv.org/abs/2405.14614",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Measuring and improving “attentional agency” [FAccT 2025: arxiv]"
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
"byteEnd": 101,
"byteStart": 96
},
"features": [
{
"uri": "https://arxiv.org/abs/2409.19104",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Evaluation of LLMs in high-stakes context such as medical misinformation jailbreaks [AIES 2025: arxiv]"
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
"byteEnd": 64,
"byteStart": 59
},
"features": [
{
"uri": "https://arxiv.org/abs/2409.19104",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Understanding governance practices empirically [AIES 2025: arxiv]"
}
}
]
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
"byteEnd": 89,
"byteStart": 84
},
"features": [
{
"uri": "https://github.com/nickmvincent/blogs/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Some topics that I’ve micro-blogged about (I sometimes microblog directly to a “blogs” GitHub repo), and hope to write some longer thoughts on:"
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
"byteEnd": 69,
"byteStart": 64
},
"features": [
{
"uri": "https://x.com/iamtrask/status/1971197830258950236",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 34,
"byteStart": 20
},
"features": [
{
"uri": "https://github.com/nickmvincent/blogs/blob/main/microblogs/2025-05-17_three_terms.md",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "The use of the term synthetic data. See also discussion on this Tweet."
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
"byteEnd": 74,
"byteStart": 70
},
"features": [
{
"uri": "https://github.com/nickmvincent/blogs/blob/main/ideas.md",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "A number of externalized notes on “ideas I think are interesting” here"
}
}
]
}
}
]
}
]
},
"description": "Another recap post for the Data Leverage newsletter!",
"publishedAt": "2025-10-11T00:00:00.000Z"
}
}
