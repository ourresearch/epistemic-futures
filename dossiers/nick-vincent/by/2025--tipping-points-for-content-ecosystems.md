---
title: "Tipping Points for Content Ecosystems"
person: "nick-vincent"
section: "by"
type: "blog-post"
year: 2025
date: "2025-02-12"
venue: "Data Leverage (Digital Garden / dataleverage.substack.com)"
authors: "Nicholas Vincent"
source_url: "https://nickmvincent.github.io/long-posts/tipping-points-for-content-ecosystems.html"
retrieved: "2026-08-13"
content: "full-text"
notes: "Dek: Our AI design choices in 2024 could preclude \"Powerful AI\" in 2030. Garden section: long-posts. Mirrored on the Data Leverage Substack."
---

# Tipping Points for Content Ecosystems

## Full text

This post was co-written by Nick Vincent, Jacob Thebault-Spieker,
and Johanna Desprez.

This is an early draft — we welcome your feedback and are eager
to build more coalitions around these ideas.

The choices and policy paradigms shaping the design of AI products
may create “tipping points for content ecosystems” — analogous to tipping
points in natural ecosystems — that preclude humankind from ever
seeing the full benefits of AI, including both near-term benefits
and the realization of AI abundance promoted by figures in the
tech industry.

A photo of thawing permafrost. From Boris Radosavljevic (posted
to flickr, hosted on Wikimedia
Commons) licensed under CC BY
2.0.

Somewhat recently, Dario Amodei, the CEO of Anthropic, wrote a rather
extensive blog post
highlighting ways that AI — in particular, what he calls powerful
AI and what others might call Artificial General
Intelligence (this is the term Sam Altman of OpenAI uses in his “three
observations” blog post with a similar overall perspective) — can
make the world better. Amodei’s post naturally saw a lot of traction
within typical AI circles, and was also covered in the tech media (see
e.g. Robinson’s coverage
of the fund-raising angle in The Verge and discussion on the podcast
Hard Fork). Most of the essay hinges on a key preliminary assumption:
powerful AI will come to exist.

Discussions about AI progress often center “technical” questions
about modeling data and the construction of AI systems. The key
questions in these discussions tend to be:

-

Are We (humanity) allocating enough people and resources
towards the “right” modeling approaches? For instance: should we spend
more resources on deep learning or other approaches; if we use deep
learning, which architectures should we use; what other disciplines,
such as cognitive science, should we look towards?

-

What industrial and engineering challenges need to be overcome to
enable a given modeling approach? For instance: how should we design
data centres; how can we improve chip manufacturing; how can we handle
energy demands of new AI systems?

These discussions, which are technocratic in nature, really only
involve a relatively small set of actors, i.e. the tech industry and
those who self-identify as AI researchers. Answering these questions
certainly matters for determining whether or not we build powerful
AI.

However, there’s an entirely separate debate to be had about the
production and sustenance of data flow underlying AI. Data is, in one
sense, more upstream on the mountain (see e.g., Delacroix on data
rivers) than the technocratic modelling and engineering discussions.
After all, if our sensor technologies or record keeping technologies
were to falter, all the modelling in the world would bear little fruit.
The most elegant and cathedral-like data centre we humans might build
would simply act as a vessel for noise.

Here, we want to argue that it is very possible that we will fail to
build “powerful AI” or “AGI” because we cause one or more
Tipping Points for Content Ecosystems.

#### The Setup

To introduce this concept, let us consider a hypothetical future in
which we keep building new foundation models and to track their progress
we invent a new index of AI Utility that aggregates existing benchmarks
with some new set of more dynamic benchmarks. We’ll hand wave here and
assume a number of open challenges with benchmarks are solved; the key
idea is let’s assume we can cleanly compare how much utility humanity
gets out of AI in 2024 and 2030.

For simplicity, let’s discuss coding and science-focused AI systems
(much of Amodei’s powerful AI blog post centers on AI’s
contribution to scientific progress). Imagine a model trained in January
2025 using the full historical records from Stack Exchange, Wikipedia,
and arXiv as pre-training data, alongside fine-tuning data from a set
of, say, 10,000 contractors paid for “preference data”. Let’s say
that this model is able to achieve 4 “units” of intelligence — we might
call it a “2024 Level 4 AI”. After an exhaustive set of data valuation
experiments and exploration of counterfactual data ablations, we
identify the key pieces of content that are most responsible for those
units of intelligence. Perhaps we can even train a very good model on a
small set of “core” documents — the 100,000 (to pick a clean number
again) documents containing the pearls of wisdom in our pile of
human-generated token sequences (perhaps leveraging so-called “synthetic
data”).

This story, so far, gets us to “2024 Level 4 AI” (on the back of
100,000 volunteer-created documents and 10,000 contractor-created
outputs). But, to unpack where the upstream data comes from, which will
be needed to move beyond “2024 Level 4 AI”, we can think about some
other clean numbers.

Below, we’re going to do some inline napkin math. The key goal here
is to start to outline how sophisticated ecosystems-style modeling could
help avoid tipping points in AI. (One planned follow-up for this post is
to create an entry in the “Data Napkin Math
Project” that makes the below scenario into an interactive
explorable).

Let’s say we need to get 100 people to contribute something to an
imaginary platform like Stack Exchange — let’s call it “StackipediaXiv”
— to get one especially good document that we can include in our high
quality pre-training set. Furthermore, based on Stack Exchange’s real ratio of pageviews to posts
(roughly 800M to 8M) and the old “1% rule” of Internet
communities, we need to get 100 people to visit StackipediaXiv to get 1
person to make a contribution.

That’s 100 visitors for every “document” (i.e., contribution, post),
and 100 contributors for every “especially good” document, which gives
us a conversion rate of sorts: to get 1 “especially good” document per
month, we need 10,000 monthly visits (we’ll ignore the distinction
between individual visits and monthly active users for now and just
focus on visits). For reference, the actual activity of Stack Overflow,
the programming-specific section of Stack Exchange, in 2022 was 60k
posts per week (see
work on the topic here), or about 240k posts per month (let’s assume
this came from 240k * 100 = 24M visits, although actual unique visitor
estimates are higher).

With these clean numbers, over a 10 month period, if our
StackipediaXiv had 10M visits a month (so 100M total visits across the
whole period and 1M total contributions), we could get a nice 10k
document dataset. If each document is around 600 tokens (let’s smooth
over the the typical 1
token = 3/4 word and imagine each document is around the average length
of a Wikipedia article, 692 words), this gets us 6M tokens. If we can
1000x our monthly visits (go from 10M to 100B — higher than Stack
Overflow’s reported 257M
monthly visits), we’d get 6B tokens, nearly the amount used for
Microsoft’s Phi-1 and Phi
1.5.

(Summarizing the quick math above: we’re assuming 1 “high quality
contribution” requires 10k visits and gives us 600 tokens, or 6
hundredths of a token per visit. To get 6B tokens under these
assumptions, we have (6e9 / (6/100)) = 100B visits needed).

#### Ok, but Tipping Points?

The key argument we’re working towards is that the reliance on
contributions in the open web creates the risk of a tipping
point in AI. In natural ecosystems, tipping
points are thresholds: points that, if crossed, lead to harmful
outcomes and are difficult/impossible to come back from. The choices
made in deploying and governing this “2024 Level 4 AI” may be a
tipping point.

Naively deploying AI may cause reduced contribution on some parts of
the open web and more AI-assisted action on other parts. Fewer people
may visit sites like Stack Exchange (a trend that’s already seemingly
begun — “…after the release of ChatGPT…posting activity decreased
sharply, with the weekly average falling from around 60,000 posts to
40,000 within 6 months”), resulting in fewer contributors and fewer
helpful posts. People may start submitting more AI-generated content to
Wikipedia (this has also begun) and to arXiv (likewise), affecting the
underlying training data for future models. In our above example, we
needed to achieve extremely high monthly visit counts to our imaginary
knowledge creation site to produce even a very “small” dataset. So what
are we to do if monthly visits are actually decreasing rather than
increasing?

Moreover, even short term increases in economic inequality – jobs are
displaced,
people experience dispossession of their
intellectual property, and power is concentrated
in organizations that operate AI – affect the content ecosystem too.
People who once had decent jobs and a bit of time to participate in
StackExchange or to fix maps on OpenStreetMap may start to feel more
economic pressure, causing the amount of “self-directed knowledge
contribution” in the world to go down.

#### Fast Forward to 2030

In 2030, the “Level 4 AI” we deployed in 2024 may have lead to (1)
reduced human participation in peer production due to direct
substitution (I visit Claude or ChatGPT instead of Stack Exchange),
reduced human participation in peer production due to increased economic
inequality that causes people to spend less overall time making
self-directed knowledge contributions. and (3) an increase in the
publication of AI content that reduces the signal to noise ratio of the
web.

Now, maybe traffic to online knowledge production websites is halved
and we have half the high quality tokens we needed to achieve some
capabilities jump. Or, maybe it now takes 200 visitors for someone to
become a contributor (a halving of the conversion rate). This toy
example gives us a first pass at a kind of “ecological” model, against
which we could simulate a much more robust set of experiments. However,
in all of the example outcomes, we start to see our “2030 AI”
being weaker than the “2024 Level 4” AI of yesteryear.

This is the opposite of recursive self-improvement. Instead, the
tipping point of “2024 Level 4” AI creates feedback
loops caused by AI product and policy choices. Does StackExchange
continue to be the place people go for coding help, with some subset of
them turning into active contributors, as Claude becomes increasingly
useful for programmers? Do people turn to Wikipedia as a reliable
resource, with some subset of them helping add knowledge, as Deep
Research summarizes the web for them? Is ArXiv a trusted vehicle for
novel research, as AI generated content proliferates on that platform?
This is the crux of our argument: there may be no turning back
from this tipping point and the belief that “powerful AI will
come to exist” hinges on the product and policy choices of today.

Maybe clever new applications of reinforcement learning can help
mitigate some content ecosystems issues, and maybe companies can get
some equivalent data by paying people directly. But we must recognize
that’s it is a serious possibility that we permanently block or
seriously delay certain capabilities from arising because those
capabilities were dependent on certain knowledge artifacts coming into
being.

#### What do we
do? Pie-in-the-sky and Practical Solutions

What would the opposite scenario entail? If, starting tomorrow, we
could achieve global coordination on a number of economic development
and policy related questions, what could we achieve? Tipping points are
stopped or mitigated by finding a balance before we hit the point of no
return. There’s often a natural ebb and flow before the tipping point is
hit (warmer years might lead to some glaciers melting, but colder years
help build that back up). So, some reduction in data contribution does
not mean we’re completely doomed – but it does suggest we should start
thinking about the positive vision here.

First, some kind of redistributive program that ensures AI profits
are shared with the public at large could increase, on average,
participation in self-directed knowledge sharing. Of course, if we wave
a magic wand and send everybody a check tomorrow, many people will not
suddenly become Wikipedia super-editors or dedicated programming tutors.
Many might, however, engage in other forms of knowledge contribution
(mapping their local areas in OpenStreetMap, reviewing products,
answering questions online). And we do know that at least in some
contexts, editing activity is going down now, so this is not entirely
hypothetical.

The above magic wand scenario has some viability issues, as such
scenarios often do (where does the money come from? At the moment,
actual AI profits wouldn’t be enough to
sustain something like this). Another avenue might involve using worker
power, policy levers, or making explicit technology design choices that
try to ensure future data creation jobs lean towards the more
self-directed end of the spectrum.

The combination of worker bargaining power, policy, and design could
lead to an outcome in which people do day-to-day tasks that look like
peer production (they write text, verify claims, organize references,
answer questions) but as part of a well-paid, reasonably empowered job
(emphatically not a gig work dystopia). Perhaps we can imagine
an AI future in which much of the population is effectively employed to
maintain knowledge ecosystems.

Beyond just generally improving wealth and standard of living to
allow self-directed knowledge contribution, we might make targeted
product decisions to make contribution easier and more likely (e.g.,
echoing the now “classic”
issues with search engines providing attribution to Wikipedia). Just
moving toward AI products that promote “prosocial behavior” (acknowledge
and maybe even help clean up the knowledge commons you draw on, avoid
using the products to lower the SNR of the web, etc.) could be enough to
avoid these content tipping points.

Ultimately, while this argument involves some speculation and some of
the empirical trends about online activity observed so far could reverse
(or become less relevant because of other unexpected developments — new
training paradigms emerge, new platforms emerge, etc.), we believe it’s
an important perspective to include in AI discussions, even those
focused on the immense benefits of powerful AI / AGI.

Source revision history

Selected Git commits that changed this source file.

- 9fb4674b8a 2026-07-12 - Migrate blog into digital presence monorepo

Mirror freshness

Maintenance status for tracked full-copy mirrors of this post.

-
Current
substack

mirror 2025-02-12

Baseline from original_url

Source and AT Protocol record

Source path
content/writing/posts/2025-02-12-tipping-points-for-content-ecosystems.md

AT Protocol URI
at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.document/3mizeecie5rvg

Exact public AT Protocol record cached for the Leaflet/Bluesky-facing copy.

{
"uri": "at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.document/3mizeecie5rvg",
"cid": "bafyreigadhmabkau4cvgkqgce25zx7bgukwautamn4khhfubugbgbem5pe",
"value": {
"path": "/3mizeecie5rvg",
"site": "at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.publication/3lzrsw2kvwc2m",
"$type": "site.standard.document",
"title": "Tipping Points for Content Ecosystems",
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
"$link": "bafkreibh2nik7mdheba6ssp2rqjuzldaxqmqiajw2tr56fall2l2nm4jmu"
},
"mimeType": "image/jpeg",
"size": 183755
},
"aspectRatio": {
"$type": "pub.leaflet.blocks.image#aspectRatio",
"width": 800,
"height": 536
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
"byteEnd": 86,
"byteStart": 0
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "This post was co-written by Nick Vincent, Jacob Thebault-Spieker, and Johanna Desprez."
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
"byteEnd": 110,
"byteStart": 0
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "This is an early draft — we welcome your feedback and are eager to build more coalitions around these ideas."
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
"byteEnd": 283,
"byteStart": 280
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
"byteEnd": 175,
"byteStart": 139
},
"features": [
{
"uri": "https://en.wikipedia.org/wiki/Tipping_points_in_the_climate_system",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "The choices and policy paradigms shaping the design of AI products may create “tipping points for content ecosystems” — analogous to tipping points in natural ecosystems — that preclude humankind from ever seeing the full benefits of AI, including both near-term benefits and the realization of AI abundance promoted by figures in the tech industry."
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
"byteStart": 128
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
"byteEnd": 128,
"byteStart": 119
},
"features": [
{
"uri": "https://creativecommons.org/licenses/by/2.0/deed.en",
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
"byteEnd": 119,
"byteStart": 102
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
"byteEnd": 102,
"byteStart": 85
},
"features": [
{
"uri": "https://en.m.wikipedia.org/wiki/File:Permafrost_in_Herschel_Island_002.jpg",
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
"byteEnd": 85,
"byteStart": 0
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "A photo of thawing permafrost. From Boris Radosavljevic (posted to flickr, hosted on Wikimedia Commons) licensed under CC BY 2.0."
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
"byteEnd": 688,
"byteStart": 658
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
"byteEnd": 587,
"byteStart": 580
},
"features": [
{
"uri": "https://open.spotify.com/episode/2G4UlFmVjwMizRl1jMUPxf?si=1f41d2d0afcb40b2",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 518,
"byteStart": 510
},
"features": [
{
"uri": "https://www.theverge.com/2024/10/16/24268209/anthropic-ai-dario-amodei-agi-funding-blog",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 292,
"byteStart": 274
},
"features": [
{
"uri": "https://blog.samaltman.com/three-observations",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 219,
"byteStart": 188
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
"byteEnd": 160,
"byteStart": 149
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
"byteEnd": 89,
"byteStart": 85
},
"features": [
{
"uri": "https://darioamodei.com/machines-of-loving-grace",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Somewhat recently, Dario Amodei, the CEO of Anthropic, wrote a rather extensive blog post highlighting ways that AI — in particular, what he calls powerful AI and what others might call Artificial General Intelligence (this is the term Sam Altman of OpenAI uses in his “three observations” blog post with a similar overall perspective) — can make the world better. Amodei’s post naturally saw a lot of traction within typical AI circles, and was also covered in the tech media (see e.g. Robinson’s coverage of the fund-raising angle in The Verge and discussion on the podcast Hard Fork). Most of the essay hinges on a key preliminary assumption: powerful AI will come to exist."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Discussions about AI progress often center “technical” questions about modeling data and the construction of AI systems. The key questions in these discussions tend to be:"
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
"byteEnd": 6,
"byteStart": 4
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "Are We (humanity) allocating enough people and resources towards the “right” modeling approaches? For instance: should we spend more resources on deep learning or other approaches; if we use deep learning, which architectures should we use; what other disciplines, such as cognitive science, should we look towards?"
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "What industrial and engineering challenges need to be overcome to enable a given modeling approach? For instance: how should we design data centres; how can we improve chip manufacturing; how can we handle energy demands of new AI systems?"
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
"byteEnd": 272,
"byteStart": 261
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "These discussions, which are technocratic in nature, really only involve a relatively small set of actors, i.e. the tech industry and those who self-identify as AI researchers. Answering these questions certainly matters for determining whether or not we build powerful AI."
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
"byteEnd": 209,
"byteStart": 198
},
"features": [
{
"uri": "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4388928",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "However, there’s an entirely separate debate to be had about the production and sustenance of data flow underlying AI. Data is, in one sense, more upstream on the mountain (see e.g., Delacroix on data rivers) than the technocratic modelling and engineering discussions. After all, if our sensor technologies or record keeping technologies were to falter, all the modelling in the world would bear little fruit. The most elegant and cathedral-like data centre we humans might build would simply act as a vessel for noise."
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
"byteEnd": 173,
"byteStart": 135
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#bold"
}
]
}
],
"plaintext": "Here, we want to argue that it is very possible that we will fail to build “powerful AI” or “AGI” because we cause one or more Tipping Points for Content Ecosystems."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 3,
"facets": [],
"plaintext": "The Setup"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "To introduce this concept, let us consider a hypothetical future in which we keep building new foundation models and to track their progress we invent a new index of AI Utility that aggregates existing benchmarks with some new set of more dynamic benchmarks. We’ll hand wave here and assume a number of open challenges with benchmarks are solved; the key idea is let’s assume we can cleanly compare how much utility humanity gets out of AI in 2024 and 2030."
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
"byteEnd": 994,
"byteStart": 980
},
"features": [
{
"uri": "https://www.microsoft.com/en-us/research/publication/textbooks-are-all-you-need-ii-phi-1-5-technical-report/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 399,
"byteStart": 384
},
"features": [
{
"uri": "https://arxiv.org/abs/2305.18290",
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
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "For simplicity, let’s discuss coding and science-focused AI systems (much of Amodei’s powerful AI blog post centers on AI’s contribution to scientific progress). Imagine a model trained in January 2025 using the full historical records from Stack Exchange, Wikipedia, and arXiv as pre-training data, alongside fine-tuning data from a set of, say, 10,000 contractors paid for “preference data”. Let’s say that this model is able to achieve 4 “units” of intelligence — we might call it a “2024 Level 4 AI”. After an exhaustive set of data valuation experiments and exploration of counterfactual data ablations, we identify the key pieces of content that are most responsible for those units of intelligence. Perhaps we can even train a very good model on a small set of “core” documents — the 100,000 (to pick a clean number again) documents containing the pearls of wisdom in our pile of human-generated token sequences (perhaps leveraging so-called “synthetic data”)."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "This story, so far, gets us to “2024 Level 4 AI” (on the back of 100,000 volunteer-created documents and 10,000 contractor-created outputs). But, to unpack where the upstream data comes from, which will be needed to move beyond “2024 Level 4 AI”, we can think about some other clean numbers."
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
"byteEnd": 269,
"byteStart": 245
},
"features": [
{
"uri": "https://nickmvincent.github.io/data_napkin_math/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Below, we’re going to do some inline napkin math. The key goal here is to start to outline how sophisticated ecosystems-style modeling could help avoid tipping points in AI. (One planned follow-up for this post is to create an entry in the “Data Napkin Math Project” that makes the below scenario into an interactive explorable)."
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
"byteEnd": 363,
"byteStart": 356
},
"features": [
{
"uri": "https://en.wikipedia.org/wiki/1%25_rule",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 297,
"byteStart": 292
},
"features": [
{
"uri": "https://stackexchange.com/about",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Let’s say we need to get 100 people to contribute something to an imaginary platform like Stack Exchange — let’s call it “StackipediaXiv” — to get one especially good document that we can include in our high quality pre-training set. Furthermore, based on Stack Exchange’s real ratio of pageviews to posts (roughly 800M to 8M) and the old “1% rule” of Internet communities, we need to get 100 people to visit StackipediaXiv to get 1 person to make a contribution."
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
"byteEnd": 684,
"byteStart": 678
},
"features": [
{
"uri": "https://stackexchange.com/about",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 544,
"byteStart": 518
},
"features": [
{
"uri": "https://academic.oup.com/pnasnexus/article/3/9/pgae400/7754871#483096365",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "That’s 100 visitors for every “document” (i.e., contribution, post), and 100 contributors for every “especially good” document, which gives us a conversion rate of sorts: to get 1 “especially good” document per month, we need 10,000 monthly visits (we’ll ignore the distinction between individual visits and monthly active users for now and just focus on visits). For reference, the actual activity of Stack Overflow, the programming-specific section of Stack Exchange, in 2022 was 60k posts per week (see work on the topic here), or about 240k posts per month (let’s assume this came from 240k * 100 = 24M visits, although actual unique visitor estimates are higher)."
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
"byteStart": 616
},
"features": [
{
"uri": "https://arxiv.org/abs/2309.05463",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 520,
"byteStart": 512
},
"features": [
{
"uri": "https://stackexchange.com/about",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 360,
"byteStart": 354
},
"features": [
{
"uri": "https://en.wikipedia.org/wiki/Wikipedia:Size_of_Wikipedia",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 305,
"byteStart": 287
},
"features": [
{
"uri": "https://platform.openai.com/tokenizer",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "With these clean numbers, over a 10 month period, if our StackipediaXiv had 10M visits a month (so 100M total visits across the whole period and 1M total contributions), we could get a nice 10k document dataset. If each document is around 600 tokens (let’s smooth over the the typical 1 token = 3/4 word and imagine each document is around the average length of a Wikipedia article, 692 words), this gets us 6M tokens. If we can 1000x our monthly visits (go from 10M to 100B — higher than Stack Overflow’s reported 257M monthly visits), we’d get 6B tokens, nearly the amount used for Microsoft’s Phi-1 and Phi 1.5."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "(Summarizing the quick math above: we’re assuming 1 “high quality contribution” requires 10k visits and gives us 600 tokens, or 6 hundredths of a token per visit. To get 6B tokens under these assumptions, we have (6e9 / (6/100)) = 100B visits needed)."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 3,
"facets": [],
"plaintext": "Ok, but Tipping Points?"
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
"byteEnd": 383,
"byteStart": 361
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
"byteEnd": 175,
"byteStart": 161
},
"features": [
{
"uri": "https://www.nature.com/articles/s41559-019-0797-2",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 137,
"byteStart": 95
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#bold"
}
]
}
],
"plaintext": "The key argument we’re working towards is that the reliance on contributions in the open web creates the risk of a tipping point in AI. In natural ecosystems, tipping points are thresholds: points that, if crossed, lead to harmful outcomes and are difficult/impossible to come back from. The choices made in deploying and governing this “2024 Level 4 AI” may be a tipping point."
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
"byteEnd": 550,
"byteStart": 542
},
"features": [
{
"uri": "https://arxiv.org/abs/2403.13812",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 526,
"byteStart": 521
},
"features": [
{
"uri": "https://arxiv.org/abs/2410.08044",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 216,
"byteStart": 201
},
"features": [
{
"uri": "https://academic.oup.com/pnasnexus/article/3/9/pgae400/7754871",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Naively deploying AI may cause reduced contribution on some parts of the open web and more AI-assisted action on other parts. Fewer people may visit sites like Stack Exchange (a trend that’s already seemingly begun — “…after the release of ChatGPT…posting activity decreased sharply, with the weekly average falling from around 60,000 posts to 40,000 within 6 months”), resulting in fewer contributors and fewer helpful posts. People may start submitting more AI-generated content to Wikipedia (this has also begun) and to arXiv (likewise), affecting the underlying training data for future models. In our above example, we needed to achieve extremely high monthly visit counts to our imaginary knowledge creation site to produce even a very “small” dataset. So what are we to do if monthly visits are actually decreasing rather than increasing?"
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
"byteEnd": 172,
"byteStart": 160
},
"features": [
{
"uri": "https://www.technologyreview.com/2024/12/18/1108796/this-is-where-the-data-to-build-ai-comes-from/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 114,
"byteStart": 101
},
"features": [
{
"uri": "https://arxiv.org/abs/2403.13073",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 81,
"byteStart": 72
},
"features": [
{
"uri": "https://www.nber.org/system/files/working_papers/w24174/w24174.pdf",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Moreover, even short term increases in economic inequality – jobs are displaced, people experience dispossession of their intellectual property, and power is concentrated in organizations that operate AI – affect the content ecosystem too. People who once had decent jobs and a bit of time to participate in StackExchange or to fix maps on OpenStreetMap may start to feel more economic pressure, causing the amount of “self-directed knowledge contribution” in the world to go down."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 3,
"facets": [],
"plaintext": "Fast Forward to 2030"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "In 2030, the “Level 4 AI” we deployed in 2024 may have lead to (1) reduced human participation in peer production due to direct substitution (I visit Claude or ChatGPT instead of Stack Exchange), reduced human participation in peer production due to increased economic inequality that causes people to spend less overall time making self-directed knowledge contributions. and (3) an increase in the publication of AI content that reduces the signal to noise ratio of the web."
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
"byteEnd": 497,
"byteStart": 467
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#bold"
}
]
}
],
"plaintext": "Now, maybe traffic to online knowledge production websites is halved and we have half the high quality tokens we needed to achieve some capabilities jump. Or, maybe it now takes 200 visitors for someone to become a contributor (a halving of the conversion rate). This toy example gives us a first pass at a kind of “ecological” model, against which we could simulate a much more robust set of experiments. However, in all of the example outcomes, we start to see our “2030 AI” being weaker than the “2024 Level 4” AI of yesteryear."
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
"byteEnd": 687,
"byteStart": 635
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
"byteEnd": 78,
"byteStart": 65
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#bold"
}
]
}
],
"plaintext": "This is the opposite of recursive self-improvement. Instead, the tipping point of “2024 Level 4” AI creates feedback loops caused by AI product and policy choices. Does StackExchange continue to be the place people go for coding help, with some subset of them turning into active contributors, as Claude becomes increasingly useful for programmers? Do people turn to Wikipedia as a reliable resource, with some subset of them helping add knowledge, as Deep Research summarizes the web for them? Is ArXiv a trusted vehicle for novel research, as AI generated content proliferates on that platform? This is the crux of our argument: there may be no turning back from this tipping point and the belief that “powerful AI will come to exist” hinges on the product and policy choices of today."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Maybe clever new applications of reinforcement learning can help mitigate some content ecosystems issues, and maybe companies can get some equivalent data by paying people directly. But we must recognize that’s it is a serious possibility that we permanently block or seriously delay certain capabilities from arising because those capabilities were dependent on certain knowledge artifacts coming into being."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 3,
"facets": [],
"plaintext": "What do we do? Pie-in-the-sky and Practical Solutions"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "What would the opposite scenario entail? If, starting tomorrow, we could achieve global coordination on a number of economic development and policy related questions, what could we achieve? Tipping points are stopped or mitigated by finding a balance before we hit the point of no return. There’s often a natural ebb and flow before the tipping point is hit (warmer years might lead to some glaciers melting, but colder years help build that back up). So, some reduction in data contribution does not mean we’re completely doomed – but it does suggest we should start thinking about the positive vision here."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "First, some kind of redistributive program that ensures AI profits are shared with the public at large could increase, on average, participation in self-directed knowledge sharing. Of course, if we wave a magic wand and send everybody a check tomorrow, many people will not suddenly become Wikipedia super-editors or dedicated programming tutors. Many might, however, engage in other forms of knowledge contribution (mapping their local areas in OpenStreetMap, reviewing products, answering questions online). And we do know that at least in some contexts, editing activity is going down now, so this is not entirely hypothetical."
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
"byteEnd": 170,
"byteStart": 164
},
"features": [
{
"uri": "https://github.com/nickmvincent/data_napkin_math",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "The above magic wand scenario has some viability issues, as such scenarios often do (where does the money come from? At the moment, actual AI profits wouldn’t be enough to sustain something like this). Another avenue might involve using worker power, policy levers, or making explicit technology design choices that try to ensure future data creation jobs lean towards the more self-directed end of the spectrum."
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
"byteEnd": 297,
"byteStart": 294
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "The combination of worker bargaining power, policy, and design could lead to an outcome in which people do day-to-day tasks that look like peer production (they write text, verify claims, organize references, answer questions) but as part of a well-paid, reasonably empowered job (emphatically not a gig work dystopia). Perhaps we can imagine an AI future in which much of the population is effectively employed to maintain knowledge ecosystems."
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
"byteEnd": 227,
"byteStart": 220
},
"features": [
{
"uri": "https://brenthecht.com/publications/icwsm17_googlewikipedia.pdf",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Beyond just generally improving wealth and standard of living to allow self-directed knowledge contribution, we might make targeted product decisions to make contribution easier and more likely (e.g., echoing the now “classic” issues with search engines providing attribution to Wikipedia). Just moving toward AI products that promote “prosocial behavior” (acknowledge and maybe even help clean up the knowledge commons you draw on, avoid using the products to lower the SNR of the web, etc.) could be enough to avoid these content tipping points."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Ultimately, while this argument involves some speculation and some of the empirical trends about online activity observed so far could reverse (or become less relevant because of other unexpected developments — new training paradigms emerge, new platforms emerge, etc.), we believe it’s an important perspective to include in AI discussions, even those focused on the immense benefits of powerful AI / AGI."
}
}
]
}
]
},
"description": "Our AI design choices in 2024 could preclude \"Powerful AI\" in 2030.",
"publishedAt": "2025-02-12T00:00:00.000Z"
}
}
