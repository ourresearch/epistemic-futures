---
title: "Which datasets should we assume are \"in all the AI models\"?"
person: "nick-vincent"
section: "by"
type: "blog-post"
year: 2025
date: "2025-09-24"
venue: "Data Leverage (Digital Garden / dataleverage.substack.com)"
authors: "Nicholas Vincent"
source_url: "https://nickmvincent.github.io/long-posts/which-datasets-should-we-assume-are.html"
retrieved: "2026-08-13"
content: "full-text"
notes: "Dek: New model releases keep (re)sparking discussions about training data. What can we assume is upstream in the data river, and what do we want to see happen? Garden section: long-posts. Mirrored on the Data Leverage Substack."
---

# Which datasets should we assume are "in all the AI models"?

## Full text

This is post doesn’t touch on breaking news; the first draft was
actually written back in December 2023! However, after sitting on it for
a while, I believe the points still hold and this could be of interest
for ongoing discussions.

Photograph by Rama, Wikimedia
Commons, Cc-by-sa-2.0-fr

Model releases from Apple, Meta, Google and more have all sparked
many rounds of
discussion
about training data. Organizations may share more data details in due
time (Google has expressed
interest), and some of the more recent technical reports (such as Apple’s)
reveal more details than we’ve seen before. However, we’re still mostly
in the dark when it comes to specific dataset details for many of the
large commercial models (to be sure, there is a growing set of
groups/projects with details: EleutherAI’s
many works, Dolma from AI2, FineWeb
from HuggingFace, the Data
Provenance Initiative, and more).

There's a cool light bulb moment when studying probability when
students learn to think in terms of complementary
events. In short: sometimes, the easiest way to determine the
probability of an event is to instead figure out the probability
p that the event won't occur, then calculate
(1-p). For instance,
to calculate the probability a "1" will show up at least once over 8 die
rolls, we can start by thinking about the probability a "1" will never
show up.

Of course, this idea isn’t really limited to probability; we
similarly might estimate the volume of liquid in a mostly full cup by
estimating how much is missing. Intuitively, this is useful because it
means we don’t have to do as much counting,
and I think the high-level idea has some important connections to the
aforementioned data discussions.

I've spent a lot of my research career thinking about data
attribution and data’s value. In early work, much ado was made about
showing that Wikipedia -- a volunteer created resource -- was crucial to
both computing research and real world economic
outcomes. One motivation for doing this kind of work (say, counting how
often Wikipedia shows up in search engine
results or is used in NLP
research papers)))
is to give Wikipedia some potential bargaining power with other
organizations and/or more credit in the public's eye. By giving people
and communities who create valuable data credit for their work, we can
support sustainable data ecosystems (credit might sometimes mean money,
for instance through Wikimedia
Enterprise which does rely on some assumption of “value delivered”,
but it might also just mean attribution that leads to more volunteers,
donations, activity, etc.). Another motivation is that documenting data
dependencies is scientifically valuable so we know how
computing systems are trained.

The point that Wikipedia is fuelling AI received a big boost in
attention a while back with an article
in the New York Times magazine (and The
Daily Podcast) discussing both the history of the computing field's
"Wikipedia habit" (which is not necessarily problematic per se, but is
certainly a dependency) and what we might do going forward to try and
combine the best parts of peer production and AI.

For people in AI, this stuff is not surprising at all. Researchers
are familiar with the wide variety of Wikipedia-derived training sets
and/or benchmarks (notably, nowadays, Wikipedia content is sometimes
filtered out from some training so that it can be kept “clean” for
evaluation).

We're now comfortably in the age of "web-scale" AI. That is, a large
number of the AI systems currently getting attention -- and providing
the "foundation"
for downstream systems -- are pre-trained models that use some
*quality-filtered* version of "everything one can get
their hands on". It's the whole web, with some careful selection (for
instance, using tricks like using Reddit scores as a filter, and
filtering Common Crawl based on similarity with a "high quality
reference"). These AI systems seem to share a vague, but never quite
explicitly stated goal of trying to model almost all token sequences
people can produce — barring the sequences that might be produced in
under some human-defined low quality conditions. Token
sequences that fit the “low quality” bill are filtered out, and so it
isn’t true to say literally everything is in these LLMs.

There are a lot of open opportunities to understand the dependencies
between AI systems and digital commons empirically. For instance, I
still think do more experiments to understand a simulated "world without
Wikipedia" (or a world without Stack Exchange, a world without
scientific articles, and so on). Similarly, we should keep striving to
improve our data documentation practices so that many of these questions
are much easier to answer.

But, I'm starting to think that we're well past a point a point where
we should be thinking about data attribution with a guilty until
innocent approach, something that takes inspiration from the above
concept of complements. This means: we should probably start with the
assumption that Wikipedia is in everything, unless we have strong reason
to believe it's not. The same idea can be applied to other “likely
suspects”, like StackExchange or GitHub. At some point, for any data
that’s not explicitly in some kind of walled garden (technically or
legally), we should also assume the same.

A quick technical note: if we want to produce an estimate of “what
portion of training dataset D is content from Wikipedia?”, we
could frame as a simple enumeration problem (if we have complete labels
for the whole dataset, there’s no need to do estimation at all — we’re
just counting in that case!) or we could some assumptions about a
distribution of model-training behaviors and treat this like parameter
estimation. All that being said, I think the comparison to “counting
down” rather than up can be conceptually useful (i.e., take the approach
that requires the fewest operations).

If we just want to quickly estimate the total prevalence of
"Wikipedia-touched models", this is a different problem. In this case,
if we're pretty sure that most LLMs use Wikipedia in their training
or evaluation1 procedures, we
can arrive at an estimate more quickly looking for models that
explicitly take steps to exclude Wikipedia.

Of course, the word “guilty” in “guilty until proven innocent” may
have too negative of a connotation: it's not illegal or morally bad to
use Wikipedia to train AI (though it may be illegal or morally bad to
use other data sources). Very precisely, we might say, "If a data source
seems potentially scrape-able, we should assume it has some influence on
models trained on web-scale data", but I think
guilty-until-proven-innocent-for-training-data captures this idea
somewhat succinctly. And as we settle on a new social contract around
expectations for reciprocity, ecosystem maintenance, etc., it might
become frowned upon to train on Wikipedia without taking certain other
actions.

I think it's also worth noting there's a parallel here with open
source software and science. Instead of trying to count the number of
quantitative scientific publications that explicitly say they use numpy,
we'll probably get a faster and more accurate answer by trying to count
the ones that provide evidence that they don't use
numpy (of course, this is discipline-specific; we might make the same
argument about assuming R was used in every paper by default for some
fields). For the purposes of trying to credit these ubiquitous
resources, at some point we should stop counting up from 0% and start
counting down from 100%.

From the perspective of someone who just wants to count the
prevalence of a certain type of content in datasets, the choice to count
up from zero or count down from 100 probably just boils down to whether
you think the point estimate is going to be below 50% or not.

Where this argument starts to get interesting is if we think about
writing out a full list of “probably widely used” or “obvious no-brainer
dataset choices” that we should include on the short-list of datasets
that are “most likely in everything, unless otherwise stated”. From the
perspective of accurate counting, this would mainly involve making a
guess about which datasets appear in most training super sets.

This exercise might be an interesting way to provoke a societal
discussion about which datasets should be on a such a
short-list. Creating that short-list (at scale) can be a powerful
exercise in collective intelligence. What are the datasets for which we
want to assume “that’s probably in all the models”. Wikipedia and
StackExchange may seem like obvious choices, but what else falls into
this category?

1

Again, it’s important to note that in some cases, researchers do
explicitly filter out Wikipedia content — because it’s so central to
popular evaluation datasets. Wikipedia editors still deserve credit for
this (and arguably, deserve more credit, the topic of a future post or
paper).

Source revision history

Selected Git commits that changed this source file.

- 9fb4674b8a 2026-07-12 - Migrate blog into digital presence monorepo

Mirror freshness

Maintenance status for tracked full-copy mirrors of this post.

-
Current
substack

mirror 2025-09-24

Baseline from original_url

Source and AT Protocol record

Source path
content/writing/posts/2025-09-24-which-datasets-should-we-assume-are.md

AT Protocol URI
at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.document/3mizee6a42btu

Exact public AT Protocol record cached for the Leaflet/Bluesky-facing copy.

{
"uri": "at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.document/3mizee6a42btu",
"cid": "bafyreiclnxgaxxbxfax4mhgcon75xmkii4ynktkgtatavfwxa7rsxvbwe4",
"value": {
"path": "/3mizee6a42btu",
"site": "at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.publication/3lzrsw2kvwc2m",
"$type": "site.standard.document",
"title": "Which datasets should we assume are \"in all the AI models\"?",
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
"facets": [
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 235,
"byteStart": 0
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "This is post doesn’t touch on breaking news; the first draft was actually written back in December 2023! However, after sitting on it for a while, I believe the points still hold and this could be of interest for ongoing discussions."
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
"byteEnd": 18,
"byteStart": 14
},
"features": [
{
"uri": "https://commons.wikimedia.org/wiki/User:Rama",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Photograph by Rama, Wikimedia Commons, Cc-by-sa-2.0-fr"
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
"byteEnd": 604,
"byteStart": 578
},
"features": [
{
"uri": "https://www.dataprovenance.org/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 555,
"byteStart": 548
},
"features": [
{
"uri": "https://huggingface.co/spaces/HuggingFaceFW/blogpost-fineweb-v1",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 537,
"byteStart": 532
},
"features": [
{
"uri": "https://allenai.org/dolma",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 515,
"byteStart": 505
},
"features": [
{
"uri": "https://www.eleuther.ai/projects/training-large-language-models",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 264,
"byteStart": 255
},
"features": [
{
"uri": "https://machinelearning.apple.com/research/apple-intelligence-foundation-language-models",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 197,
"byteStart": 179
},
"features": [
{
"uri": "https://x.com/JeffDean/status/1732461004901282238",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 91,
"byteStart": 81
},
"features": [
{
"uri": "https://x.com/JesseDodge/status/1732444597593203111?s=20",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 80,
"byteStart": 78
},
"features": [
{
"uri": "https://techcrunch.com/2024/07/29/apple-says-it-took-a-responsible-approach-to-training-its-apple-intelligence-models/?guccounter=1",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Model releases from Apple, Meta, Google and more have all sparked many rounds of discussion about training data. Organizations may share more data details in due time (Google has expressed interest), and some of the more recent technical reports (such as Apple’s) reveal more details than we’ve seen before. However, we’re still mostly in the dark when it comes to specific dataset details for many of the large commercial models (to be sure, there is a growing set of groups/projects with details: EleutherAI’s many works, Dolma from AI2, FineWeb from HuggingFace, the Data Provenance Initiative, and more)."
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
"byteEnd": 305,
"byteStart": 297
},
"features": [
{
"uri": "https://en.wikipedia.org/wiki/Complementary_event#Example_of_the_utility_of_this_concept",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 290,
"byteStart": 287
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
"byteEnd": 269,
"byteStart": 258
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
"byteEnd": 242,
"byteStart": 241
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
"byteEnd": 120,
"byteStart": 100
},
"features": [
{
"uri": "https://en.wikipedia.org/wiki/Complementary_event",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "There's a cool light bulb moment when studying probability when students learn to think in terms of complementary events. In short: sometimes, the easiest way to determine the probability of an event is to instead figure out the probability p that the event won't occur, then calculate (1-p). For instance, to calculate the probability a \"1\" will show up at least once over 8 die rolls, we can start by thinking about the probability a \"1\" will never show up."
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
"byteEnd": 248,
"byteStart": 240
},
"features": [
{
"uri": "https://math.stackexchange.com/questions/3351186/why-should-i-consider-the-complementary-probability-if-i-can-do-it-directly",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Of course, this idea isn’t really limited to probability; we similarly might estimate the volume of liquid in a mostly full cup by estimating how much is missing. Intuitively, this is useful because it means we don’t have to do as much counting, and I think the high-level idea has some important connections to the aforementioned data discussions."
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
"byteEnd": 973,
"byteStart": 950
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
"byteEnd": 729,
"byteStart": 709
},
"features": [
{
"uri": "https://meta.wikimedia.org/wiki/Wikimedia_Enterprise",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 407,
"byteStart": 406
},
"features": [
{
"uri": "https://github.com/nickmvincent/UGCValueRoundup/blob/main/wikipedia.md",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 406,
"byteStart": 387
},
"features": [
{
"uri": "https://github.com/nickmvincent/UGCValueRoundup/blob/main/wikipedia.md",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 372,
"byteStart": 351
},
"features": [
{
"uri": "https://dl.acm.org/doi/abs/10.1145/3449078",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 241,
"byteStart": 231
},
"features": [
{
"uri": "https://doi.org/10.1111/jems.12421",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "I've spent a lot of my research career thinking about data attribution and data’s value. In early work, much ado was made about showing that Wikipedia -- a volunteer created resource -- was crucial to both computing research and real world economic outcomes. One motivation for doing this kind of work (say, counting how often Wikipedia shows up in search engine results or is used in NLP research papers))) is to give Wikipedia some potential bargaining power with other organizations and/or more credit in the public's eye. By giving people and communities who create valuable data credit for their work, we can support sustainable data ecosystems (credit might sometimes mean money, for instance through Wikimedia Enterprise which does rely on some assumption of “value delivered”, but it might also just mean attribution that leads to more volunteers, donations, activity, etc.). Another motivation is that documenting data dependencies is scientifically valuable so we know how computing systems are trained."
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
"byteEnd": 156,
"byteStart": 139
},
"features": [
{
"uri": "https://www.nytimes.com/2023/09/10/podcasts/the-daily/wikipedia-ai.html",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 102,
"byteStart": 95
},
"features": [
{
"uri": "https://www.nytimes.com/2023/07/18/magazine/wikipedia-ai-chatgpt.html",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "The point that Wikipedia is fuelling AI received a big boost in attention a while back with an article in the New York Times magazine (and The Daily Podcast) discussing both the history of the computing field's \"Wikipedia habit\" (which is not necessarily problematic per se, but is certainly a dependency) and what we might do going forward to try and combine the best parts of peer production and AI."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "For people in AI, this stuff is not surprising at all. Researchers are familiar with the wide variety of Wikipedia-derived training sets and/or benchmarks (notably, nowadays, Wikipedia content is sometimes filtered out from some training so that it can be kept “clean” for evaluation)."
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
"byteEnd": 850,
"byteStart": 840
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
"byteEnd": 728,
"byteStart": 706
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
"byteEnd": 236,
"byteStart": 220
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#bold"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 154,
"byteStart": 144
},
"features": [
{
"uri": "https://en.wikipedia.org/wiki/Foundation_model",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "We're now comfortably in the age of \"web-scale\" AI. That is, a large number of the AI systems currently getting attention -- and providing the \"foundation\" for downstream systems -- are pre-trained models that use some *quality-filtered* version of \"everything one can get their hands on\". It's the whole web, with some careful selection (for instance, using tricks like using Reddit scores as a filter, and filtering Common Crawl based on similarity with a \"high quality reference\"). These AI systems seem to share a vague, but never quite explicitly stated goal of trying to model almost all token sequences people can produce — barring the sequences that might be produced in under some human-defined low quality conditions. Token sequences that fit the “low quality” bill are filtered out, and so it isn’t true to say literally everything is in these LLMs."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "There are a lot of open opportunities to understand the dependencies between AI systems and digital commons empirically. For instance, I still think do more experiments to understand a simulated \"world without Wikipedia\" (or a world without Stack Exchange, a world without scientific articles, and so on). Similarly, we should keep striving to improve our data documentation practices so that many of these questions are much easier to answer."
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
"byteEnd": 143,
"byteStart": 122
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "But, I'm starting to think that we're well past a point a point where we should be thinking about data attribution with a guilty until innocent approach, something that takes inspiration from the above concept of complements. This means: we should probably start with the assumption that Wikipedia is in everything, unless we have strong reason to believe it's not. The same idea can be applied to other “likely suspects”, like StackExchange or GitHub. At some point, for any data that’s not explicitly in some kind of walled garden (technically or legally), we should also assume the same."
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
"byteEnd": 98,
"byteStart": 97
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "A quick technical note: if we want to produce an estimate of “what portion of training dataset D is content from Wikipedia?”, we could frame as a simple enumeration problem (if we have complete labels for the whole dataset, there’s no need to do estimation at all — we’re just counting in that case!) or we could some assumptions about a distribution of model-training behaviors and treat this like parameter estimation. All that being said, I think the comparison to “counting down” rather than up can be conceptually useful (i.e., take the approach that requires the fewest operations)."
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
"byteEnd": 213,
"byteStart": 212
},
"features": [
{
"uri": "#footnote-1",
"$type": "pub.leaflet.richtext.facet#link"
},
{
"$type": "pub.leaflet.richtext.facet#bold"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 212,
"byteStart": 199
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#bold"
}
]
}
],
"plaintext": "If we just want to quickly estimate the total prevalence of \"Wikipedia-touched models\", this is a different problem. In this case, if we're pretty sure that most LLMs use Wikipedia in their training or evaluation1 procedures, we can arrive at an estimate more quickly looking for models that explicitly take steps to exclude Wikipedia."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Of course, the word “guilty” in “guilty until proven innocent” may have too negative of a connotation: it's not illegal or morally bad to use Wikipedia to train AI (though it may be illegal or morally bad to use other data sources). Very precisely, we might say, \"If a data source seems potentially scrape-able, we should assume it has some influence on models trained on web-scale data\", but I think guilty-until-proven-innocent-for-training-data captures this idea somewhat succinctly. And as we settle on a new social contract around expectations for reciprocity, ecosystem maintenance, etc., it might become frowned upon to train on Wikipedia without taking certain other actions."
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
"byteEnd": 617,
"byteStart": 613
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#bold"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 326,
"byteStart": 321
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#bold"
}
]
}
],
"plaintext": "I think it's also worth noting there's a parallel here with open source software and science. Instead of trying to count the number of quantitative scientific publications that explicitly say they use numpy, we'll probably get a faster and more accurate answer by trying to count the ones that provide evidence that they don't use numpy (of course, this is discipline-specific; we might make the same argument about assuming R was used in every paper by default for some fields). For the purposes of trying to credit these ubiquitous resources, at some point we should stop counting up from 0% and start counting down from 100%."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "From the perspective of someone who just wants to count the prevalence of a certain type of content in datasets, the choice to count up from zero or count down from 100 probably just boils down to whether you think the point estimate is going to be below 50% or not."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Where this argument starts to get interesting is if we think about writing out a full list of “probably widely used” or “obvious no-brainer dataset choices” that we should include on the short-list of datasets that are “most likely in everything, unless otherwise stated”. From the perspective of accurate counting, this would mainly involve making a guess about which datasets appear in most training super sets."
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
"byteEnd": 102,
"byteStart": 96
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "This exercise might be an interesting way to provoke a societal discussion about which datasets should be on a such a short-list. Creating that short-list (at scale) can be a powerful exercise in collective intelligence. What are the datasets for which we want to assume “that’s probably in all the models”. Wikipedia and StackExchange may seem like obvious choices, but what else falls into this category?"
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
"plaintext": "Again, it’s important to note that in some cases, researchers do explicitly filter out Wikipedia content — because it’s so central to popular evaluation datasets. Wikipedia editors still deserve credit for this (and arguably, deserve more credit, the topic of a future post or paper)."
}
}
]
}
]
},
"description": "New model releases keep (re)sparking discussions about training data. What can we assume is upstream in the data river, and what do we want to see happen?",
"publishedAt": "2025-09-24T00:00:00.000Z"
}
}
