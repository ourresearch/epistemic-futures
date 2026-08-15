---
title: "[microblog] One book is worth \"0.06%\" benchmark points to AI; is \"no different from noise\". What gives?"
person: "nick-vincent"
section: "by"
type: "blog-post"
year: 2025
date: "2025-04-21"
venue: "Data Leverage (Digital Garden / dataleverage.substack.com)"
authors: "Nicholas Vincent"
source_url: "https://nickmvincent.github.io/short-reactions/microblog-one-book-is-worth-006-benchmark.html"
retrieved: "2026-08-13"
content: "full-text"
notes: "Dek: Commenting on recent coverage of, and discussion about, Meta's arguments about training data value quantification. Garden section: short-reactions. Mirrored on the Data Leverage Substack."
---

# [microblog] One book is worth "0.06%" benchmark points to AI; is "no different from noise". What gives?

## Full text

This will be a “contextualized microblog”. I saw several posts in
quick succession that I thought could be worth commenting on as a
group.

### The Context

First, a set of relevant links that discuss training data value in
the context of lawsuits, compensation and consent:

-

A previous (Sep 2024) newsletter
in which I discuss the intersection of collective bargaining and data
valuation: “Is Zuckerberg right to say that your specific creative work
has no value to AI?”

- This newsletter is mainly a reaction to this article
from The Verge

-

A much more recent (April 2025) tweet
with much discussion from Andrew Curran, which comments on a screenshot
of a quote from this Vanity Fair article
on AI lawsuits, and in particular Meta.

- The quote: ‘But their defense also hinges on the argument that the
individual books themselves are, essentially, worthless—one expert
witness for Meta describes that the influence of a single book in LLM
pretraining “adjusted its performance by less than 0.06% on industry
standard benchmarks, a meaningless change no different from
noise.”’

-

A response tweet from
Lucas Beyer criticizing the discourse around this number/topic
(discussing practical constraints that should be considered in
interpreting a number like this, especially variance between
experiments)

-

See also: this recent coverage
from Barr and Dixit at Business Insider of Meta’s data ablation
experiments

I think Beyer’s points are critical to account for in data value
discussions. Robust data valuation remains expensive and there’s so much
more context needed to throw around numbers like this (as he notes:
model scale, training duration, exact benchmark details, and so on).

### The Short Argument

What I want to add (echoing the September post) is this: in any data
valuation experiment, another factor that must be accounted for is
whether and how data points will be grouped. In pure
“leave-one-out” experiments, there are no groups; it’s every data point
for itself. There are technical arguments for grouping data points: we
might want to compute data value along natural groupings that emerge
from the data (e.g., demographic groups), compute Shapley values with
account for various “coalitions” that might exist, or compute data
values in a way that gives more weight to either smaller or larger
groups.1

Different approaches can be empirically tested for effectiveness on
various tasks like data selection or mislabel detection. However, in the
context of training data and consent/compensation/law (topics that are
typically the forte of economics, philosophy, human-computer
interaction, etc.), there is no purely technical approach that can
determine the appropriate group size to test**.** Rather, for practical
purposes (e.g. for a market or for a lawsuit) the appropriate group size
is dependent on coordination and collective bargaining capabilities of
the training data creators.

The 0.06% number (again, with all its many caveats) is really only
relevant if we accept an implicit assumption that all authors would be
acting as individual agents in some hypothetical data market. Another
extreme (also unrealistic) would be to assume perfect cooperation
between all data creators in the world, and then to attribute 100% of
model performance to that single coalition. In my opinion: the approach
that would most benefit these discussions would be a middle ground. We
should be calculating and openly discussing data values at the level of
economic sectors, groups of firms, individual firms, and perhaps
specific interest groups, but probably not at the level of individual
people or books.

1

To briefly list just a few papers:

-

Koh, P. W. W., Ang, K. S., Teo, H., & Liang, P. S. (2019). On
the accuracy of influence functions for measuring group effects.
Advances in neural information processing systems, 32.
[link]

-

Ghorbani, A., & Zou, J. (2019, May). Data shapley: Equitable
valuation of data for machine learning. In International conference
on machine learning (pp. 2242-2251). PMLR. [link]

-

Jia, R., Dao, D., Wang, B., Hubis, F. A., Hynes, N., Gürel, N.
M., ... & Spanos, C. J. (2019, April). Towards efficient data
valuation based on the shapley value. In The 22nd International
Conference on Artificial Intelligence and Statistics (pp.
1167-1176). PMLR. [link]

-

Kwon, Y., & Zou, J. (2021). Beta shapley: a unified and
noise-reduced data valuation framework for machine learning. arXiv
preprint arXiv:2110.14049. [link]

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

mirror 2025-04-21

Baseline from original_url

Source and AT Protocol record

Source path
content/writing/reaction-posts/2025-04-21-microblog-one-book-is-worth-006-benchmark.md

AT Protocol URI
at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.document/3mizeesacqmdb

Exact public AT Protocol record cached for the Leaflet/Bluesky-facing copy.

{
"uri": "at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.document/3mizeesacqmdb",
"cid": "bafyreief3k7o2aisyw2lyxz7qmebz7rzvwi267j23xa4fjo56tol5sh2bm",
"value": {
"path": "/3mizeesacqmdb",
"site": "at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.publication/3lzrsw2kvwc2m",
"$type": "site.standard.document",
"title": "[microblog] One book is worth \"0.06%\" benchmark points to AI; is \"no different from noise\". What gives?",
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
"$link": "bafkreidyunijynefgxhqhezwodq5exqhv2syq6l4yllbwehtqftdcsxzva"
},
"mimeType": "image/png",
"size": 2733725
},
"aspectRatio": {
"$type": "pub.leaflet.blocks.image#aspectRatio",
"width": 1028,
"height": 1028
}
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "This will be a “contextualized microblog”. I saw several posts in quick succession that I thought could be worth commenting on as a group."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "The Context"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "First, a set of relevant links that discuss training data value in the context of lawsuits, compensation and consent:"
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
"byteEnd": 32,
"byteStart": 22
},
"features": [
{
"uri": "https://dataleverage.substack.com/p/is-zuckerberg-right-to-say-that-your",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "A previous (Sep 2024) newsletter in which I discuss the intersection of collective bargaining and data valuation: “Is Zuckerberg right to say that your specific creative work has no value to AI?”"
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
"byteEnd": 150,
"byteStart": 143
},
"features": [
{
"uri": "https://www.vanityfair.com/news/story/meta-ai-lawsuit",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 37,
"byteStart": 32
},
"features": [
{
"uri": "https://x.com/AndrewCurran_/status/1914045840265789540",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "A much more recent (April 2025) tweet with much discussion from Andrew Curran, which comments on a screenshot of a quote from this Vanity Fair article on AI lawsuits, and in particular Meta."
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
"byteEnd": 16,
"byteStart": 11
},
"features": [
{
"uri": "https://x.com/giffmana/status/1914245144422776906",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "A response tweet from Lucas Beyer criticizing the discourse around this number/topic (discussing practical constraints that should be considered in interpreting a number like this, especially variance between experiments)"
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
"byteEnd": 30,
"byteStart": 22
},
"features": [
{
"uri": "https://www.businessinsider.com/meta-ai-llama-models-training-data-ablation-2025-4",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "See also: this recent coverage from Barr and Dixit at Business Insider of Meta’s data ablation experiments"
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
"plaintext": "I think Beyer’s points are critical to account for in data value discussions. Robust data valuation remains expensive and there’s so much more context needed to throw around numbers like this (as he notes: model scale, training duration, exact benchmark details, and so on)."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "The Short Argument"
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
"byteEnd": 623,
"byteStart": 622
},
"features": [
{
"uri": "#footnote-1",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 179,
"byteStart": 172
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "What I want to add (echoing the September post) is this: in any data valuation experiment, another factor that must be accounted for is whether and how data points will be grouped. In pure “leave-one-out” experiments, there are no groups; it’s every data point for itself. There are technical arguments for grouping data points: we might want to compute data value along natural groupings that emerge from the data (e.g., demographic groups), compute Shapley values with account for various “coalitions” that might exist, or compute data values in a way that gives more weight to either smaller or larger groups.1"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Different approaches can be empirically tested for effectiveness on various tasks like data selection or mislabel detection. However, in the context of training data and consent/compensation/law (topics that are typically the forte of economics, philosophy, human-computer interaction, etc.), there is no purely technical approach that can determine the appropriate group size to test**.** Rather, for practical purposes (e.g. for a market or for a lawsuit) the appropriate group size is dependent on coordination and collective bargaining capabilities of the training data creators."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "The 0.06% number (again, with all its many caveats) is really only relevant if we accept an implicit assumption that all authors would be acting as individual agents in some hypothetical data market. Another extreme (also unrealistic) would be to assume perfect cooperation between all data creators in the world, and then to attribute 100% of model performance to that single coalition. In my opinion: the approach that would most benefit these discussions would be a middle ground. We should be calculating and openly discussing data values at the level of economic sectors, groups of firms, individual firms, and perhaps specific interest groups, but probably not at the level of individual people or books."
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
"byteEnd": 1,
"byteStart": 0
},
"features": [
{
"uri": "#footnote-anchor-1",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "1"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "To briefly list just a few papers:"
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
"byteEnd": 187,
"byteStart": 183
},
"features": [
{
"uri": "https://proceedings.neurips.cc/paper/2019/hash/a78482ce76496fcf49085f2190e675b4-Abstract.html",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 180,
"byteStart": 178
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
"byteEnd": 176,
"byteStart": 127
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "Koh, P. W. W., Ang, K. S., Teo, H., & Liang, P. S. (2019). On the accuracy of influence functions for measuring group effects. Advances in neural information processing systems, 32. [link]"
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
"byteEnd": 177,
"byteStart": 173
},
"features": [
{
"uri": "https://proceedings.mlr.press/v97/ghorbani19c.html",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 148,
"byteStart": 104
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "Ghorbani, A., & Zou, J. (2019, May). Data shapley: Equitable valuation of data for machine learning. In International conference on machine learning (pp. 2242-2251). PMLR. [link]"
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
"byteEnd": 271,
"byteStart": 267
},
"features": [
{
"uri": "https://proceedings.mlr.press/v89/jia19a.html",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 242,
"byteStart": 167
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "Jia, R., Dao, D., Wang, B., Hubis, F. A., Hynes, N., Gürel, N. M., ... & Spanos, C. J. (2019, April). Towards efficient data valuation based on the shapley value. In The 22nd International Conference on Artificial Intelligence and Statistics (pp. 1167-1176). PMLR. [link]"
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
"byteEnd": 155,
"byteStart": 151
},
"features": [
{
"uri": "https://arxiv.org/abs/2110.14049",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 148,
"byteStart": 117
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "Kwon, Y., & Zou, J. (2021). Beta shapley: a unified and noise-reduced data valuation framework for machine learning. arXiv preprint arXiv:2110.14049. [link]"
}
}
]
}
}
]
}
]
},
"description": "Commenting on recent coverage of, and discussion about, Meta's arguments about training data value quantification.",
"publishedAt": "2025-04-21T00:00:00.000Z"
}
}
