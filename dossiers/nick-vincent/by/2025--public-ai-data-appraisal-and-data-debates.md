---
title: "Public AI, Data Appraisal, and Data Debates"
person: "nick-vincent"
section: "by"
type: "blog-post"
year: 2025
date: "2025-04-03"
venue: "Data Leverage (Digital Garden / dataleverage.substack.com)"
authors: "Nicholas Vincent"
source_url: "https://nickmvincent.github.io/long-posts/public-ai-data-appraisal-and-data.html"
retrieved: "2026-08-13"
content: "full-text"
notes: "Dek: A consortium of Public AI labs can substantially improve data pricing, which may also help to concretize debates about the ethics and legality of training practices. Garden section: long-posts. Mirrored on the Data Leverage Substack."
---

# Public AI, Data Appraisal, and Data Debates

## Full text

Ahmad
al-Tifashi’s 13th-century book of gemstones, complete with valuable
pricing records for appraising gemstones. [wikimedia
commons]

This is, once again, an early draft and will likely be updated. I
welcome comments and pushback (or support!).

There is a growing1 movement around
building “public AI” — which would mean, to quote the Public AI Network
(PAINT) website, building public
institutions, public-private partnerships, and international
collaboration to enable "AI provisioned like electricity, parks,
highways, libraries, or the Internet itself”. Here, I want to add an
argument for public AI to the pile: building public AI will be extremely
helpful in improving the efficiency of data
markets.

The public AI concept has been explored substantively in whitepapers
from PAINT2 Mozilla3. The general idea is to take action (again, see
the whitepapers for tractable plans towards this vision) to build widely
available public goods that support an ecosystem of AI products built on
primarily on open data and using an entirely open software stack.

This is not about building one singular national AI institute, or
stopping private organizations from pursuing AI. Instead, it’s a public
goods-based ecosystem that can support private-public partnerships and a
plurality of different organizations.

This is important to note, because in this post, I’ll refer generally
to the notion of “public AI labs”. The idea is that a “public AI lab”
that performs model training and data appraisal might be an organization
like a Canadian AI Institute, AI Sweden, AI Singapore, the Barcelona Supercomputing Center, or the
UK AISI. Perhaps some of these
organizations might be connected via some consortium. So when I say “a
public AI lab might do some data valuation experiments”, this concretely
could refer to experiments run in a number of locations across the
world.

### Two pressing data problems

Problem 1: While there is emerging market for training-focused data
deals (e.g. buyers like Google
and OpenAI
are paying sellers like Reddit and news organizations for access to
content, which is presumably being used for training and/or evaluation4), there is currently not much transparency with
regards to how data is currently being priced. This is likely to create
a lot of uncertainty and volatile negotiations when it comes data
prices. Why is Reddit’s data worth $60M to Google? Why not $60B or
$60k?

To summarize Raul Castro Fernandez (summarizing
Kenneth Arrow and what’s now called the “Arrow information Paradox”) in
work on Data-Sharing
Consortia5: if you’re a buyer
looking to acquire data for AI development purposes, you can’t really
guess how much value you’ll get until you see it, and you won’t know for
sure until you train on it. On the other hand, for someone selling data,
once the seller lets the buyers see the “product”, there’s no way to
take it back. This is bad on both fronts, and means there are many cases
where data transactions are mutually beneficial but don’t happen.

Problem 2: The current AI data training paradigm is plagued by a
constellation of issues related to consent and legality.
It is also unclear how AI products being deployed now may affect (and
potentially wither) incentives for future data creation. While there is
still uncertainty as to how the training paradigm will hold up to
lawsuits, regulation, and consumer demand, I think it’s now fully
uncontroversial to say that this tension exists, and even die hard
defenders of the current paradigm would agree there is a public
relations and optics problem.

Here, I’ll discuss how public AI could substantially help with
problem 1, and how this might carry over to helping problem 2 (although
this will depend quite a bit on how open legal and regulatory questions
are answered).

### A
healthier market with public AI labs as data appraisers

The Data-Sharing Consortia solution to the “Arrow information
paradox” is to have an intermediary entity hold data in escrow and use a
well-designed market mechanism that manages transactions and
remuneration using estimates of data value. In short, a well designed
system can solve the problem of “Hey, I want to buy some data,
and here’s how much I’m willing to pay, but I only want the data if it’s
actually going to be good”.

Critically, this involves the data intermediary organizations running
data value experiments, which might involve calculating “influence estimates”6, “Shapley values”, or
something like the “Entitlement Stake” introduced by Castro Fernandez in
the Data Consortia paper. These are all different approaches that try to
give an “attribution score” to a data point or group of data points.

A key takeaway from this body of work is that at the end of the day,
if we want to be really sure about data value, somebody needs
to do some experiments in which they try out different data.

Public AI contributors can implement this vision — and amplify its
impact — by acting as public-interest appraising agents. A public AI
body would have incentives to train models specifically with the intent
of revealing and sharing data value, which can improve the overall
efficiency of the market. In other words, while the data consortium
vision can work with private actors (just as a private auction house
can allocate goods in a welfare-maximizing fashion), public AI
would actively level the informational playing field. Note that these
contributors could include various public benefit corporations and
non-profits as well.

In fact, if “public AI” is implemented as more of a consortium than
an individual lab — with an approach that emphasizes decentralization
and pooling — the process of building public AI models would involve
“natural experiments” for data value (because e.g. there were some
experiments in Canada with dataset 1, and some experiments in Sweden
with a different dataset 2, and then these datasets or models are merged
in some way). In fact research from AI2, Cohere,
CMU, and UW suggests that a modular “train, pool, and merge” approach
can be effective for data valuation that leads to better overall
models7.

Decentralized AI training naturally exposes some estimates of data
value in a way that centralized training does not (though brings its own
complications to the table). Critically, getting some estimates
of data values won’t require taking much additional action beyond what
organizations might already being doing in the process of training
models (though doing extensive value experiments will still be rather
expensive, at least with current techniques). The various contributors
to a public AI consortium can go about their business of acquiring data,
training models, deploying services, and so on, and just by keeping
track of any data ablation experiments and data valuation estimation
that are used in that process, produce value estimates that can be
shared publicly to the benefit of data sellers.

There is a long history of state-based appraisal agencies. Consider,
for instance, organizations like BC Assessment that assess
property values (in part to facilitate the buying and selling of
properties, but also to facilitate the deployment of property
taxes).

In classical auction design work, theoretical
results suggest that expert appraisals can benefit sellers when buyers
are risk averse. In practice, auction houses employ expert appraisers.
Of course, in some settings, buyers and sellers might employ their own
private appraisers (effectively spending some money to increase their
confidence about the valuation of a good). More generally, we might
expect that in the current “Buyer’s Market” for data in which many of
the would-be appraisers are employed by AI operators, public-interest
appraisal will benefit sellers.

Put simply, any “public AI” body with a mandate towards transparency
that engaged in any data ablation experiments in the process of model
training and shared said experiments could act as a third-party
appraiser.

Note that this does not remove incentives to participate in
data-sharing consortium, though it may complicate the mechanism design.
As an example, consider a public AI body who buys the same Reddit data
as Google and OpenAI, but then reveals a number of benchmark deltas that
can be “attributed” to that dataset. E.g., “we bought Reddit’s data for
$60M and all we got was a lousy 1% accuracy on this “social media lingo”
benchmark”. Or, “we bought Reddit’s data and our conversational
capabilities went through the roof!” Either outcome could affect the
price that Microsoft and Anthropic might be willing to pay for that same
data, but would not necessarily tell Microsoft and Anthropic the exact
impact on their models’ performance.

Ultimately, individual buyers still need to consider their specific,
often private, circumstances (access to other proprietary data,
engineering design decisions, etc.) that may affect valuation, so a
public AI body will never give a data market participant full confidence
about the value they can obtain from some dataset. However, the end
result will be reduced information asymmetry and reduced appraisal
costs.

This would also be critical for upstream stakeholders, e.g. the
actual Reddit users who created Reddit’s “data assets”, if they wanted
to become involved in the decision-making around these deals. Reddit
could stand to benefit from its users being knowledgeable about, and
involved in data deals, as the userbase has a history of successful
protest action against the platform.

My expectation is that levelling the informational playing field will
be a net positive for market dynamics. In fact, I would expect that
because right now, AI companies can run experiments to actually
calculate data value but data sellers can not, that many recent and
ongoing data deals will be seen through the lens of history as
favourable towards the buyers. And we should also expect that without
collective bargaining (or in the extreme, cartel behaviour) by data
sellers, that AI companies will walk away as winners in the current
market, especially if they succeed in automating large amounts of
economically valuable labour.

In short, key points for this argument are:

-

Data appraisal can improve market dynamics

-

Public bodies can perform data appraisal and share the appraisal
results

-

A decentralized consortium of public AI labs will perform some
degree of “natural appraisal”, and with an explicit pooling and merging
approach can do even more appraisal.

-

Public appraisal is critical for upstream stakeholders (e.g.,
Reddit users).

### Would
Data Appraisal Help with Consent and Legal Issues?

Above, we made the case that a public AI body can improve auction and
market dynamics by acting as an expert appraiser. By telling us how much
Reddit’s data impacted AI performance on some benchmark (which OpenAI,
Google, and Reddit may all be hesitant to do), we can better understand
if $60M is a “good deal”.

An additional effect of the data appraisal described above would be
adding concrete evidence to be used in to ongoing debates about the
morality and legality of various training practices.

Very concretely, currently if one wants to make an argument about,
for instance, the empirical value of training on LibGen, to my knowledge
one of the best sources is the unsealed documents
from a lawsuit against Meta (of course, organizations like AI2, Cohere
for AI, and many academic researchers continue to conduct and publish data ablation89 experiments). A pool
of such estimates provided by public AI bodies (though perhaps not
specifically looking at pirated materials) would be extremely valuable
to anyone trying to assess the cost-benefit trade-offs of different
regulatory regimes, and might also serve to reveal certain
“high-leverage coalitions” of creators who can bargain very
effectively.

Of course, it’s worth noting that one outcome of looming legal and
regulatory questions could be that public AI-type organizations become
the only organizations that can engage in internet scale
pre-training. I think that most folks following these discussions think
this is highly unlikely, but it’s worth stating: it could be the case
that public AI systems are the best performing AI systems, full
stop, because they are the only organizations that retain
wide-ranging training privileges.

More generally, on average, if organizations are not paying for data,
then the more “public interest” an organization is (a loose concept, to
be sure, but operationalizable) the larger we might expect their
allowable training set size to be (against, averaging across legal
decision and normative preferences). Exploring this moral landscape will
the subject of future writing.

Critically, given the uncertainty of the current moment and the wide
range of perspectives and institutions represented in the big tent of
public AI, it’s critical to note that these arguments do not rely on any
one legal outcome or specific moral perspective: achieving healthier
data market outcomes and concretizing legal and ethical debates can be
seen as beneficial from across the spectrum of perspectives.

### Additional notes

Exclusivity of data deals: One important caveat to
the above arguments is that publicly shared data values are most useful
if data deals are primarily not exclusive. Indeed, if the predominant
data licensing contract focuses on exclusivity, this will be bad for
public AI. For instance, if OpenAI has an exclusive license to train on
some content organization’s outputs, this could block the public AI
network from using or appraising that data. However, given the
challenges in data excludability and early evidence of a “live by the
sword, die by the sword” to data (e.g. Deepseek distilling OpenAI’s
models), it seems that exclusive deals may be threatened.

Public AI labs as the data intermediaries in the consortium
model: If public AI organizations don’t actually hold data and
train on it — if for instance, they only focus on providing compute, or
supporting open source software — they won’t be able to contribute to
data appraisal. So, it’s critical that public AI is involved in all
components of the AI stack.

Precedent from data use exemptions for cultural and heritage
reasons: In many cases, organizations doing cultural and
heritage related work already have certain protections or exemptions
when it comes to data use. This means that in some cases, attempts to
appraise data value may conflict with existing frameworks for exemption.
But in other cases, these exemptions may be useful as said organizations
can appraise the value of the data in their area of expertise (e.g.,
understand the impact of a specific cultural dataset on some
benchmark).

[wikimedia
commons]

#### Acknowledgments

Thanks to many folks in the Public AI Network for conversations that
led to this post. Given my plans to update this post, I’m going to make
sure everyone has had a chance to read the latest draft before I name
any specific names here.

### Changelog

- May, 2025: fixed some typos.

1

Caveat: I see myself as a part of this movement, so when I say it is
“growing”, I am certainly not an objective observer of said growth, but
I think there is a very solid case to be made (see e.g. a number of
events on the Public AI Network website: https://publicai.network/)

2

Jackson, B., Cavello, B., Devine, F., Garcia, N., Klein, S. J.,
Krasodomski, A., Tan, J., & Tursman, E. (2024). Public AI:
Infrastructure for the Common Good. Public AI Network. https://doi.org/10.5281/zenodo.13914560

3

Marda, N., Sun, J., and Surman, M. (2024). Public AI: Making AI work
for everyone, by everyone. https://assets.mofoprod.net/network/documents/Public_AI_Mozilla.pdf

4

See e.g. https://www.monda.ai/blog/ultimate-list-of-data-licensing-deals-for-ai
and https://sr.ithaka.org/our-work/generative-ai-licensing-agreement-tracker/

5

Castro Fernandez, R. (2023). Data-sharing markets: model, protocol,
and algorithms to incentivize the formation of data-sharing consortia.
Proceedings of the ACM on Management of Data, 1(2), 1-25. https://raulcastrofernandez.com/papers/data-sharing-consortia-escrow.pdf

6

Note that there is active work on making influence functions
work for LLMs. Though some of this work involves calculating something a
bit different from a true leave-one-out-estimate. See Choe, S. K., Ahn,
H., Bae, J., Zhao, K., Kang, M., Chung, Y., ... & Xing, E. (2024).
What is your data worth to gpt? llm-scale data valuation with influence
functions. arXiv preprint arXiv:2405.13954

7

Na, C., Magnusson, I., Jha, A. H., Sherborne, T., Strubell, E.,
Dodge, J., & Dasigi, P. (2024, January). Scalable Data Ablation
Approximations for Language Models through Modular Training and Merging.
In EMNLP. https://arxiv.org/abs/2410.15661

8

Soldaini, L., Kinney, R., Bhagia, A., Schwenk, D., Atkinson, D.,
Authur, R., ... & Lo, K. (2024). Dolma: An open corpus of three
trillion tokens for language model pretraining research. arXiv
preprint arXiv:2402.00159. https://arxiv.org/abs/2402.00159

9

Üstün, A., Aryabumi, V., Yong, Z. X., Ko, W. Y., D'souza, D.,
Onilude, G., ... & Hooker, S. (2024). Aya model: An instruction
finetuned open-access multilingual language model. arXiv preprint
arXiv:2402.07827. https://arxiv.org/abs/2402.07827

Source revision history

Selected Git commits that changed this source file.

- 9fb4674b8a 2026-07-12 - Migrate blog into digital presence monorepo

Mirror freshness

Maintenance status for tracked full-copy mirrors of this post.

-
Current
substack

mirror 2025-04-03

Baseline from original_url

Source and AT Protocol record

Source path
content/writing/posts/2025-04-03-public-ai-data-appraisal-and-data.md

AT Protocol URI
at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.document/3mizedy4ic63q

Exact public AT Protocol record cached for the Leaflet/Bluesky-facing copy.

{
"uri": "at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.document/3mizedy4ic63q",
"cid": "bafyreib7irdet6lgggsnj3nqlumd7fgqczit633c5vcilqixrgixpznb3i",
"value": {
"path": "/3mizedy4ic63q",
"site": "at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.publication/3lzrsw2kvwc2m",
"$type": "site.standard.document",
"title": "Public AI, Data Appraisal, and Data Debates",
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
"$link": "bafkreibbunqwde5rip5joptzytvkgqc4kzhxeeqpcsbr5b2uw3qyy2kqh4"
},
"mimeType": "image/jpeg",
"size": 39583
},
"aspectRatio": {
"$type": "pub.leaflet.blocks.image#aspectRatio",
"width": 500,
"height": 607
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
"byteEnd": 137,
"byteStart": 136
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
"byteEnd": 136,
"byteStart": 119
},
"features": [
{
"uri": "https://commons.wikimedia.org/wiki/File:Book_of_Royal_Gemstones_WDL2839.jpg",
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
"byteStart": 16
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
"byteEnd": 16,
"byteStart": 0
},
"features": [
{
"uri": "https://en.wikipedia.org/wiki/Ahmad_al-Tifashi",
"$type": "pub.leaflet.richtext.facet#link"
},
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "Ahmad al-Tifashi’s 13th-century book of gemstones, complete with valuable pricing records for appraising gemstones. [wikimedia commons]"
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
"plaintext": "This is, once again, an early draft and will likely be updated. I welcome comments and pushback (or support!)."
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
"byteEnd": 469,
"byteStart": 428
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
"byteEnd": 129,
"byteStart": 122
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
"byteEnd": 19,
"byteStart": 18
},
"features": [
{
"uri": "#footnote-1",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "There is a growing1 movement around building “public AI” — which would mean, to quote the Public AI Network (PAINT) website, building public institutions, public-private partnerships, and international collaboration to enable \"AI provisioned like electricity, parks, highways, libraries, or the Internet itself”. Here, I want to add an argument for public AI to the pile: building public AI will be extremely helpful in improving the efficiency of data markets."
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
"byteStart": 88
},
"features": [
{
"uri": "#footnote-3",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 88,
"byteStart": 81
},
"features": [
{
"uri": "https://assets.mofoprod.net/network/documents/Public_AI_Mozilla.pdf",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 80,
"byteStart": 79
},
"features": [
{
"uri": "#footnote-2",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 79,
"byteStart": 74
},
"features": [
{
"uri": "https://bit.ly/publicAIpaper",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "The public AI concept has been explored substantively in whitepapers from PAINT2 Mozilla3. The general idea is to take action (again, see the whitepapers for tractable plans towards this vision) to build widely available public goods that support an ecosystem of AI products built on primarily on open data and using an entirely open software stack."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "This is not about building one singular national AI institute, or stopping private organizations from pursuing AI. Instead, it’s a public goods-based ecosystem that can support private-public partnerships and a plurality of different organizations."
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
"byteEnd": 329,
"byteStart": 322
},
"features": [
{
"uri": "https://www.aisi.gov.uk/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 313,
"byteStart": 282
},
"features": [
{
"uri": "https://www.bsc.es/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 276,
"byteStart": 264
},
"features": [
{
"uri": "https://aisingapore.org/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 262,
"byteStart": 253
},
"features": [
{
"uri": "https://www.ai.se/en",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 251,
"byteStart": 230
},
"features": [
{
"uri": "https://cifar.ca/ai/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "This is important to note, because in this post, I’ll refer generally to the notion of “public AI labs”. The idea is that a “public AI lab” that performs model training and data appraisal might be an organization like a Canadian AI Institute, AI Sweden, AI Singapore, the Barcelona Supercomputing Center, or the UK AISI. Perhaps some of these organizations might be connected via some consortium. So when I say “a public AI lab might do some data valuation experiments”, this concretely could refer to experiments run in a number of locations across the world."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "Two pressing data problems"
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
"byteEnd": 249,
"byteStart": 248
},
"features": [
{
"uri": "#footnote-4",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 109,
"byteStart": 103
},
"features": [
{
"uri": "https://openai.com/index/openai-and-reddit-partnership/",
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
"uri": "https://www.reuters.com/technology/reddit-ai-content-licensing-deal-with-google-sources-say-2024-02-22/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Problem 1: While there is emerging market for training-focused data deals (e.g. buyers like Google and OpenAI are paying sellers like Reddit and news organizations for access to content, which is presumably being used for training and/or evaluation4), there is currently not much transparency with regards to how data is currently being priced. This is likely to create a lot of uncertainty and volatile negotiations when it comes data prices. Why is Reddit’s data worth $60M to Google? Why not $60B or $60k?"
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
"byteEnd": 178,
"byteStart": 173
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
"byteEnd": 157,
"byteStart": 156
},
"features": [
{
"uri": "#footnote-5",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 156,
"byteStart": 134
},
"features": [
{
"uri": "https://raulcastrofernandez.com/papers/data-sharing-consortia-escrow.pdf",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 47,
"byteStart": 36
},
"features": [
{
"uri": "https://en.wikipedia.org/wiki/Arrow_information_paradox",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "To summarize Raul Castro Fernandez (summarizing Kenneth Arrow and what’s now called the “Arrow information Paradox”) in work on Data-Sharing Consortia5: if you’re a buyer looking to acquire data for AI development purposes, you can’t really guess how much value you’ll get until you see it, and you won’t know for sure until you train on it. On the other hand, for someone selling data, once the seller lets the buyers see the “product”, there’s no way to take it back. This is bad on both fronts, and means there are many cases where data transactions are mutually beneficial but don’t happen."
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
"byteEnd": 120,
"byteStart": 112
},
"features": [
{
"uri": "https://blogs.gwu.edu/law-eti/ai-litigation-database/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 107,
"byteStart": 100
},
"features": [
{
"uri": "https://arxiv.org/abs/2407.14933",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Problem 2: The current AI data training paradigm is plagued by a constellation of issues related to consent and legality. It is also unclear how AI products being deployed now may affect (and potentially wither) incentives for future data creation. While there is still uncertainty as to how the training paradigm will hold up to lawsuits, regulation, and consumer demand, I think it’s now fully uncontroversial to say that this tension exists, and even die hard defenders of the current paradigm would agree there is a public relations and optics problem."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Here, I’ll discuss how public AI could substantially help with problem 1, and how this might carry over to helping problem 2 (although this will depend quite a bit on how open legal and regulatory questions are answered)."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "A healthier market with public AI labs as data appraisers"
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
"byteEnd": 280,
"byteStart": 277
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "The Data-Sharing Consortia solution to the “Arrow information paradox” is to have an intermediary entity hold data in escrow and use a well-designed market mechanism that manages transactions and remuneration using estimates of data value. In short, a well designed system can solve the problem of “Hey, I want to buy some data, and here’s how much I’m willing to pay, but I only want the data if it’s actually going to be good”."
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
"byteEnd": 164,
"byteStart": 157
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
"byteEnd": 152,
"byteStart": 151
},
"features": [
{
"uri": "#footnote-6",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 138,
"byteStart": 129
},
"features": [
{
"uri": "https://arxiv.org/abs/2405.13954",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Critically, this involves the data intermediary organizations running data value experiments, which might involve calculating “influence estimates”6, “Shapley values”, or something like the “Entitlement Stake” introduced by Castro Fernandez in the Data Consortia paper. These are all different approaches that try to give an “attribution score” to a data point or group of data points."
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
"byteEnd": 124,
"byteStart": 116
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "A key takeaway from this body of work is that at the end of the day, if we want to be really sure about data value, somebody needs to do some experiments in which they try out different data."
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
"byteEnd": 419,
"byteStart": 416
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "Public AI contributors can implement this vision — and amplify its impact — by acting as public-interest appraising agents. A public AI body would have incentives to train models specifically with the intent of revealing and sharing data value, which can improve the overall efficiency of the market. In other words, while the data consortium vision can work with private actors (just as a private auction house can allocate goods in a welfare-maximizing fashion), public AI would actively level the informational playing field. Note that these contributors could include various public benefit corporations and non-profits as well."
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
"uri": "#footnote-7",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 458,
"byteStart": 450
},
"features": [
{
"uri": "https://arxiv.org/abs/2410.15661",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "In fact, if “public AI” is implemented as more of a consortium than an individual lab — with an approach that emphasizes decentralization and pooling — the process of building public AI models would involve “natural experiments” for data value (because e.g. there were some experiments in Canada with dataset 1, and some experiments in Sweden with a different dataset 2, and then these datasets or models are merged in some way). In fact research from AI2, Cohere, CMU, and UW suggests that a modular “train, pool, and merge” approach can be effective for data valuation that leads to better overall models7."
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
"byteEnd": 193,
"byteStart": 189
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "Decentralized AI training naturally exposes some estimates of data value in a way that centralized training does not (though brings its own complications to the table). Critically, getting some estimates of data values won’t require taking much additional action beyond what organizations might already being doing in the process of training models (though doing extensive value experiments will still be rather expensive, at least with current techniques). The various contributors to a public AI consortium can go about their business of acquiring data, training models, deploying services, and so on, and just by keeping track of any data ablation experiments and data valuation estimation that are used in that process, produce value estimates that can be shared publicly to the benefit of data sellers."
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
"byteEnd": 115,
"byteStart": 102
},
"features": [
{
"uri": "https://www.bcassessment.ca/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "There is a long history of state-based appraisal agencies. Consider, for instance, organizations like BC Assessment that assess property values (in part to facilitate the buying and selling of properties, but also to facilitate the deployment of property taxes)."
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
"byteEnd": 32,
"byteStart": 28
},
"features": [
{
"uri": "https://www.jstor.org/stable/1911865?seq=1",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "In classical auction design work, theoretical results suggest that expert appraisals can benefit sellers when buyers are risk averse. In practice, auction houses employ expert appraisers. Of course, in some settings, buyers and sellers might employ their own private appraisers (effectively spending some money to increase their confidence about the valuation of a good). More generally, we might expect that in the current “Buyer’s Market” for data in which many of the would-be appraisers are employed by AI operators, public-interest appraisal will benefit sellers."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Put simply, any “public AI” body with a mandate towards transparency that engaged in any data ablation experiments in the process of model training and shared said experiments could act as a third-party appraiser."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Note that this does not remove incentives to participate in data-sharing consortium, though it may complicate the mechanism design. As an example, consider a public AI body who buys the same Reddit data as Google and OpenAI, but then reveals a number of benchmark deltas that can be “attributed” to that dataset. E.g., “we bought Reddit’s data for $60M and all we got was a lousy 1% accuracy on this “social media lingo” benchmark”. Or, “we bought Reddit’s data and our conversational capabilities went through the roof!” Either outcome could affect the price that Microsoft and Anthropic might be willing to pay for that same data, but would not necessarily tell Microsoft and Anthropic the exact impact on their models’ performance."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Ultimately, individual buyers still need to consider their specific, often private, circumstances (access to other proprietary data, engineering design decisions, etc.) that may affect valuation, so a public AI body will never give a data market participant full confidence about the value they can obtain from some dataset. However, the end result will be reduced information asymmetry and reduced appraisal costs."
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
"byteEnd": 382,
"byteStart": 374
},
"features": [
{
"uri": "https://en.wikipedia.org/wiki/2023_Reddit_API_controversy",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "This would also be critical for upstream stakeholders, e.g. the actual Reddit users who created Reddit’s “data assets”, if they wanted to become involved in the decision-making around these deals. Reddit could stand to benefit from its users being knowledgeable about, and involved in data deals, as the userbase has a history of successful protest action against the platform."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "My expectation is that levelling the informational playing field will be a net positive for market dynamics. In fact, I would expect that because right now, AI companies can run experiments to actually calculate data value but data sellers can not, that many recent and ongoing data deals will be seen through the lens of history as favourable towards the buyers. And we should also expect that without collective bargaining (or in the extreme, cartel behaviour) by data sellers, that AI companies will walk away as winners in the current market, especially if they succeed in automating large amounts of economically valuable labour."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "In short, key points for this argument are:"
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
"plaintext": "Data appraisal can improve market dynamics"
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Public bodies can perform data appraisal and share the appraisal results"
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "A decentralized consortium of public AI labs will perform some degree of “natural appraisal”, and with an explicit pooling and merging approach can do even more appraisal."
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Public appraisal is critical for upstream stakeholders (e.g., Reddit users)."
}
}
]
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "Would Data Appraisal Help with Consent and Legal Issues?"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Above, we made the case that a public AI body can improve auction and market dynamics by acting as an expert appraiser. By telling us how much Reddit’s data impacted AI performance on some benchmark (which OpenAI, Google, and Reddit may all be hesitant to do), we can better understand if $60M is a “good deal”."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "An additional effect of the data appraisal described above would be adding concrete evidence to be used in to ongoing debates about the morality and legality of various training practices."
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
"byteEnd": 346,
"byteStart": 345
},
"features": [
{
"uri": "#footnote-9",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 345,
"byteStart": 344
},
"features": [
{
"uri": "#footnote-8",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 344,
"byteStart": 336
},
"features": [
{
"uri": "https://arxiv.org/abs/2402.00159",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 335,
"byteStart": 331
},
"features": [
{
"uri": "https://arxiv.org/abs/2402.07827",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 189,
"byteStart": 180
},
"features": [
{
"uri": "https://storage.courtlistener.com/recap/gov.uscourts.cand.415175/gov.uscourts.cand.415175.391.14.pdf",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Very concretely, currently if one wants to make an argument about, for instance, the empirical value of training on LibGen, to my knowledge one of the best sources is the unsealed documents from a lawsuit against Meta (of course, organizations like AI2, Cohere for AI, and many academic researchers continue to conduct and publish data ablation89 experiments). A pool of such estimates provided by public AI bodies (though perhaps not specifically looking at pirated materials) would be extremely valuable to anyone trying to assess the cost-benefit trade-offs of different regulatory regimes, and might also serve to reveal certain “high-leverage coalitions” of creators who can bargain very effectively."
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
"byteEnd": 409,
"byteStart": 372
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
"byteEnd": 148,
"byteStart": 144
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "Of course, it’s worth noting that one outcome of looming legal and regulatory questions could be that public AI-type organizations become the only organizations that can engage in internet scale pre-training. I think that most folks following these discussions think this is highly unlikely, but it’s worth stating: it could be the case that public AI systems are the best performing AI systems, full stop, because they are the only organizations that retain wide-ranging training privileges."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "More generally, on average, if organizations are not paying for data, then the more “public interest” an organization is (a loose concept, to be sure, but operationalizable) the larger we might expect their allowable training set size to be (against, averaging across legal decision and normative preferences). Exploring this moral landscape will the subject of future writing."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Critically, given the uncertainty of the current moment and the wide range of perspectives and institutions represented in the big tent of public AI, it’s critical to note that these arguments do not rely on any one legal outcome or specific moral perspective: achieving healthier data market outcomes and concretizing legal and ethical debates can be seen as beneficial from across the spectrum of perspectives."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "Additional notes"
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
"byteEnd": 26,
"byteStart": 0
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#bold"
}
]
}
],
"plaintext": "Exclusivity of data deals: One important caveat to the above arguments is that publicly shared data values are most useful if data deals are primarily not exclusive. Indeed, if the predominant data licensing contract focuses on exclusivity, this will be bad for public AI. For instance, if OpenAI has an exclusive license to train on some content organization’s outputs, this could block the public AI network from using or appraising that data. However, given the challenges in data excludability and early evidence of a “live by the sword, die by the sword” to data (e.g. Deepseek distilling OpenAI’s models), it seems that exclusive deals may be threatened."
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
"byteEnd": 65,
"byteStart": 0
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#bold"
}
]
}
],
"plaintext": "Public AI labs as the data intermediaries in the consortium model: If public AI organizations don’t actually hold data and train on it — if for instance, they only focus on providing compute, or supporting open source software — they won’t be able to contribute to data appraisal. So, it’s critical that public AI is involved in all components of the AI stack."
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
"byteEnd": 69,
"byteStart": 0
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#bold"
}
]
}
],
"plaintext": "Precedent from data use exemptions for cultural and heritage reasons: In many cases, organizations doing cultural and heritage related work already have certain protections or exemptions when it comes to data use. This means that in some cases, attempts to appraise data value may conflict with existing frameworks for exemption. But in other cases, these exemptions may be useful as said organizations can appraise the value of the data in their area of expertise (e.g., understand the impact of a specific cultural dataset on some benchmark)."
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
"byteStart": 1
},
"features": [
{
"uri": "https://commons.wikimedia.org/wiki/File:Isaac_Lea_collection_of_precious_stones._Miss_Margaret_W._Moodey_in_charge_LCCN2016892128.jpg",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "[wikimedia commons]"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 3,
"facets": [],
"plaintext": "Acknowledgments"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Thanks to many folks in the Public AI Network for conversations that led to this post. Given my plans to update this post, I’m going to make sure everyone has had a chance to read the latest draft before I name any specific names here."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "Changelog"
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
"plaintext": "May, 2025: fixed some typos."
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
"facets": [
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 279,
"byteStart": 254
},
"features": [
{
"uri": "https://publicai.network/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Caveat: I see myself as a part of this movement, so when I say it is “growing”, I am certainly not an objective observer of said growth, but I think there is a very solid case to be made (see e.g. a number of events on the Public AI Network website: https://publicai.network/)"
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
"uri": "#footnote-anchor-2",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "2"
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
"byteEnd": 217,
"byteStart": 178
},
"features": [
{
"uri": "https://doi.org/10.5281/zenodo.13914560",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Jackson, B., Cavello, B., Devine, F., Garcia, N., Klein, S. J., Krasodomski, A., Tan, J., & Tursman, E. (2024). Public AI: Infrastructure for the Common Good. Public AI Network. https://doi.org/10.5281/zenodo.13914560"
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
"uri": "#footnote-anchor-3",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "3"
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
"byteEnd": 163,
"byteStart": 96
},
"features": [
{
"uri": "https://assets.mofoprod.net/network/documents/Public_AI_Mozilla.pdf",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Marda, N., Sun, J., and Surman, M. (2024). Public AI: Making AI work for everyone, by everyone. https://assets.mofoprod.net/network/documents/Public_AI_Mozilla.pdf"
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
"uri": "#footnote-anchor-4",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "4"
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
"byteEnd": 157,
"byteStart": 84
},
"features": [
{
"uri": "https://sr.ithaka.org/our-work/generative-ai-licensing-agreement-tracker/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 79,
"byteStart": 9
},
"features": [
{
"uri": "https://www.monda.ai/blog/ultimate-list-of-data-licensing-deals-for-ai",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "See e.g. https://www.monda.ai/blog/ultimate-list-of-data-licensing-deals-for-ai and https://sr.ithaka.org/our-work/generative-ai-licensing-agreement-tracker/"
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
"uri": "#footnote-anchor-5",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "5"
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
"byteStart": 197
},
"features": [
{
"uri": "https://raulcastrofernandez.com/papers/data-sharing-consortia-escrow.pdf",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Castro Fernandez, R. (2023). Data-sharing markets: model, protocol, and algorithms to incentivize the formation of data-sharing consortia. Proceedings of the ACM on Management of Data, 1(2), 1-25. https://raulcastrofernandez.com/papers/data-sharing-consortia-escrow.pdf"
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
"uri": "#footnote-anchor-6",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "6"
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
"byteEnd": 387,
"byteStart": 356
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
"byteEnd": 18,
"byteStart": 16
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "Note that there is active work on making influence functions work for LLMs. Though some of this work involves calculating something a bit different from a true leave-one-out-estimate. See Choe, S. K., Ahn, H., Bae, J., Zhao, K., Kang, M., Chung, Y., ... & Xing, E. (2024). What is your data worth to gpt? llm-scale data valuation with influence functions. arXiv preprint arXiv:2405.13954"
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
"uri": "#footnote-anchor-7",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "7"
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
"byteEnd": 243,
"byteStart": 211
},
"features": [
{
"uri": "https://arxiv.org/abs/2410.15661",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 209,
"byteStart": 204
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "Na, C., Magnusson, I., Jha, A. H., Sherborne, T., Strubell, E., Dodge, J., & Dasigi, P. (2024, January). Scalable Data Ablation Approximations for Language Models through Modular Training and Merging. In EMNLP. https://arxiv.org/abs/2410.15661"
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
"uri": "#footnote-anchor-8",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "8"
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
"byteEnd": 251,
"byteStart": 219
},
"features": [
{
"uri": "https://arxiv.org/abs/2402.00159",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 217,
"byteStart": 186
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "Soldaini, L., Kinney, R., Bhagia, A., Schwenk, D., Atkinson, D., Authur, R., ... & Lo, K. (2024). Dolma: An open corpus of three trillion tokens for language model pretraining research. arXiv preprint arXiv:2402.00159. https://arxiv.org/abs/2402.00159"
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
"uri": "#footnote-anchor-9",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "9"
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
"byteEnd": 244,
"byteStart": 212
},
"features": [
{
"uri": "https://arxiv.org/abs/2402.07827",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 210,
"byteStart": 179
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "Üstün, A., Aryabumi, V., Yong, Z. X., Ko, W. Y., D'souza, D., Onilude, G., ... & Hooker, S. (2024). Aya model: An instruction finetuned open-access multilingual language model. arXiv preprint arXiv:2402.07827. https://arxiv.org/abs/2402.07827"
}
}
]
}
]
},
"description": "A consortium of Public AI labs can substantially improve data pricing, which may also help to concretize debates about the ethics and legality of training practices.",
"publishedAt": "2025-04-03T00:00:00.000Z"
}
}
