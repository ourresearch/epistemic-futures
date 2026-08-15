---
title: "A Harbinger of the Future of Content? The New York Times Starts a Data Strike"
person: "nick-vincent"
section: "by"
type: "blog-post"
year: 2023
date: "2023-08-25"
venue: "Data Leverage (Digital Garden / dataleverage.substack.com)"
authors: "Nicholas Vincent"
source_url: "https://nickmvincent.github.io/long-posts/a-harbinger-of-the-future-of-content.html"
retrieved: "2026-08-13"
content: "full-text"
notes: "Dek: The New York Times is trying to remove its content from OpenAI models, surfacing tensions around copyright, economic harms, privacy, and the distribution of AI benefits. Garden section: long-posts. Mirrored on the Data Leverage Substack."
---

# A Harbinger of the Future of Content? The New York Times Starts a Data Strike

## Full text

Photo by David
Smooke on Unsplash

A major development in ongoing discussions about the future viability
of generative AI: the New York Times has emphatically
stated
it does not want to be in the ChatGPT dataset and has taken action
accordingly. Specifically, amidst ongoing negotiations it seems the
Times is considering intellectual property-based legal action, and in
the meantime has added GPTBot to its robots.txt file (i.e., the Times
indicated OpenAI should no longer scrape its content). Other
organizations like CNN have followed
suit.

In other words, the Times is gearing up for a data strike
aimed at OpenAI (and potentially other LLM operators like Anthropic,
Google, Microsoft, Meta, etc.), echoing posturing
from Reddit.

In this post, I want to lay out some factors that might play into
decision-making when an organization like the New York Times – or a
small group like you and some friends who write a blog or host a podcast
together – is thinking about trying to enter or exit an AI training
dataset. These factors might include property dispossession, economic
harms, privacy, the benefits of personalization, and concerns with
representative data.

These factors are all part of a broad challenge with dataset
preference elicitation: how can we built datasets that minimize
“inclusion errors” and “exclusion errors”, i.e. contain contributions
only from people who want to be in a particular dataset (taking into
account that there are both costs and benefits associated with
contributing to AI).

In a follow up post, I’ll delve deeper into what I think we can say
at this juncture about the likely efficacy of the data strike and how
we’d measure the impact of data-related collective action more generally
in the new AI paradigm.

### Background on data strikes

In case the data strike idea is new, here’s a quick refresher: In
many contexts, content we contribute online – like the text that a
journalist writes for a NYT article, or the text you write in a social
media post – is a crucial component in making AI systems work; in a
certain sense, it looks like the NYT and quite a few bloggers are
“working for” major AI operators. There’s some insight
to be had from thinking
about “data as labor". Withholding past or future data – whether by
updating your robots.txt file, through legal action, or by going offline
for a week – can impact AI systems and give people bargaining power. And
just like in the context of labor, this only works when data creators
achieve collective action (it typically takes the combined efforts of an
entire union to negotiate major pay raises or working condition
improvements).

So the New York Times has been “working for” AI operators, and they
want more bargaining power. And it seems they’re not pulling any
punches, given they are considering both legal action to remove past
data and using robots.txt to withhold future data.

### Reasons to Opt Out or Data
Strike

The primary concern voiced by the anonymous New York Times employees
who made the public aware of potential legal action is an increasingly
prominent one: AI operators can use your content, traces, and records to
“compete against you”. Some have called AI data practices a “property
land grab”, with the assumption that a good portion of training data
(like the words that make up a New York Times article, or your blog post
or podcast transcript) are considered intellectual property (and subject
to relevant laws).

Even if you’re not a fan of intellectual property or a framing that
treats data as something to be governed with property law (see e.g.
writing from Viljoen
on the topic of “data as property”), you might view ML/AI systems as
likely to enact economic harms via competition. It seems fair
to assume the probability that an AI system can replicate your style or
ideas increases when there’s more content (i.e. more sequences of text
in the context of LLMs) created by you or people like you in the
training data.

A related reason to want out of training data is privacy. Diffusion
models (used in some of the popular image-generation products)
definitely can
output exact copies of training inputs (for instance, a picture of your
face!). Language models similarly might memorize your writing and spit
it out verbatim,
leading to a host of thorny questions about how to handle such
situations.

We might think of these concerns – property dispossession, economic
harms via competition and privacy risks – as emerging from the same
underlying truth about LLMs and similar technologies: when there are
more sequences or patterns in the training data that come from a
particular group (like a news company), downstream models are more
capable of producing output sequences that look like that group’s
sequences. If keeping your sequences (broadly construed) somewhat hidden
is important to you, you might want to consider opting out.

### Reasons Not to Opt out

Of course, there are good reasons to believe that having content and
other contributions in a training dataset provides you (or the New York
Times) with benefits. If a model is devoid of any training data that
covers your area of interest, you’re unlikely to be able to use the
model in cases in which it could be useful. While the many potential
hazards of LLMs (some stated quite early on)
persist in current products, it remains a possibility that another large
newspaper that embraces generative AI might out-compete an organization
like the New York Times. Depending on how things play out, it could be
the case that some organizations who opt-out of generative AI training
do not end up winning in the long term. Ultimately, there is an industry
wide collective action problem here with major parallels with sectoral
bargaining. This society-level collective action problem is a
separate topic.

There’s another reason a group may not want to opt-out (or
may want to opt-in given the chance): dataset representation. Opt-out
decisions intersect with long-standing concerns about fairness and bias
in a wide array of ML and AI systems. While AI systems often contribute
to injustice because of inequities present in the social networks or
physical infrastructures in which they are deployed (in a variety
of contexts), it’s
also true that AI systems can exhibit sometimes severe group-level
performance gaps because of representation issues in training data. Put
simply, if an entire organization or group were to truly disappear from
generative AI training data, we’d expect to see major responsible AI
issues. For instance, while ML/AI technologies often exhibit
geographical biases, e.g. centering the US and western Europe, we could
imagine a bizarro-world LLM that literally has seen evidence of that any
country other than the US exists. Such an LLM would probably produce an
enormous amount of errors, leading to major blunders for users.

Finally, it’s worth discussing the practical costs of data strike
actions. This case highlights two concrete examples of specific actions
an organization might take to data strike: updating
robots.txt and taking legal action. In this case, the possibility of
legal action suggests quite high costs. On the other hand, it’s
interesting to see NYT just updating their robots.txt – that’s something
anyone with a website can do (see ai.txt as well).
However, updating these txt files is still non-trivial considering the
platform-centric way the vast majority of the world interacts with the
web.

These aren’t the only
options. In general though, the most efficacious actions will probably
require pretty serious costs. This isn’t necessarily a total
non-starter, because effective data strikes require collective action
anyway (probably at the scale of a coalition of firms, or large group of
consumers).

### What’s next

I hope add an appendum to this post as more information about the
NYT’s plan is made public. Additionally, look out for part 2, discussing
how we might predict the efficacy of this data strike, and how we might
measure the efficacy from an external or internal perspective.

Source revision history

Selected Git commits that changed this source file.

- 395b377a16 2026-07-15 - Refresh garden navigation and mirror baselines

- 9fb4674b8a 2026-07-12 - Migrate blog into digital presence monorepo

Mirror freshness

Maintenance status for tracked full-copy mirrors of this post.

-
Current
substack

mirror 2023-08-25

Re-baselined after local typo/link correction

Source and AT Protocol record

Source path
content/writing/posts/2023-08-25-a-harbinger-of-the-future-of-content.md

AT Protocol URI
at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.document/3mizedwakalr5

Exact public AT Protocol record cached for the Leaflet/Bluesky-facing copy.

{
"uri": "at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.document/3mizedwakalr5",
"cid": "bafyreifebdzyqmkbgug6dnx4k3katnzkio6br3hebpsjhmyds5l6r5f4vu",
"value": {
"path": "/3mizedwakalr5",
"site": "at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.publication/3lzrsw2kvwc2m",
"$type": "site.standard.document",
"title": "A Harbinger of the Future of Content? The New York Times Starts a Data Strike",
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
"$link": "bafkreibmpoubdhjcmn2tlgeikfe7oixweizl533qwqdxddd75npyb45cse"
},
"mimeType": "image/jpeg",
"size": 2836977
},
"aspectRatio": {
"$type": "pub.leaflet.blocks.image#aspectRatio",
"width": 3968,
"height": 2957
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
"byteEnd": 33,
"byteStart": 25
},
"features": [
{
"uri": "https://unsplash.com/photos/En_wELYYhD4?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 21,
"byteStart": 9
},
"features": [
{
"uri": "https://unsplash.com/@smooke?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Photo by David Smooke on Unsplash"
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
"byteEnd": 508,
"byteStart": 495
},
"features": [
{
"uri": "https://www.theguardian.com/technology/2023/aug/25/new-york-times-cnn-and-abc-block-openais-gptbot-web-crawler-from-scraping-content",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 130,
"byteStart": 124
},
"features": [
{
"uri": "https://www.theverge.com/2023/8/21/23840705/new-york-times-openai-web-crawler-ai-gpt",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 123,
"byteStart": 111
},
"features": [
{
"uri": "https://www.npr.org/2023/08/16/1194202562/new-york-times-considers-legal-action-against-openai-as-copyright-tensions-swirl",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "A major development in ongoing discussions about the future viability of generative AI: the New York Times has emphatically stated it does not want to be in the ChatGPT dataset and has taken action accordingly. Specifically, amidst ongoing negotiations it seems the Times is considering intellectual property-based legal action, and in the meantime has added GPTBot to its robots.txt file (i.e., the Times indicated OpenAI should no longer scrape its content). Other organizations like CNN have followed suit."
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
"byteEnd": 176,
"byteStart": 167
},
"features": [
{
"uri": "https://www.nytimes.com/2023/04/18/technology/reddit-ai-openai-google.html",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 57,
"byteStart": 46
},
"features": [
{
"uri": "https://dl.acm.org/doi/10.1145/3308558.3313742",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "In other words, the Times is gearing up for a data strike aimed at OpenAI (and potentially other LLM operators like Anthropic, Google, Microsoft, Meta, etc.), echoing posturing from Reddit."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "In this post, I want to lay out some factors that might play into decision-making when an organization like the New York Times – or a small group like you and some friends who write a blog or host a podcast together – is thinking about trying to enter or exit an AI training dataset. These factors might include property dispossession, economic harms, privacy, the benefits of personalization, and concerns with representative data."
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
"byteEnd": 83,
"byteStart": 53
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "These factors are all part of a broad challenge with dataset preference elicitation: how can we built datasets that minimize “inclusion errors” and “exclusion errors”, i.e. contain contributions only from people who want to be in a particular dataset (taking into account that there are both costs and benefits associated with contributing to AI)."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "In a follow up post, I’ll delve deeper into what I think we can say at this juncture about the likely efficacy of the data strike and how we’d measure the impact of data-related collective action more generally in the new AI paradigm."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "Background on data strikes"
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
"byteEnd": 414,
"byteStart": 411
},
"features": [
{
"uri": "https://arxiv.org/abs/2305.13238",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 404,
"byteStart": 397
},
"features": [
{
"uri": "https://www.aeaweb.org/articles?id=10.1257/pandp.20181003",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "In case the data strike idea is new, here’s a quick refresher: In many contexts, content we contribute online – like the text that a journalist writes for a NYT article, or the text you write in a social media post – is a crucial component in making AI systems work; in a certain sense, it looks like the NYT and quite a few bloggers are “working for” major AI operators. There’s some insight to be had from thinking about “data as labor\". Withholding past or future data – whether by updating your robots.txt file, through legal action, or by going offline for a week – can impact AI systems and give people bargaining power. And just like in the context of labor, this only works when data creators achieve collective action (it typically takes the combined efforts of an entire union to negotiate major pay raises or working condition improvements)."
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
"byteEnd": 216,
"byteStart": 213
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "So the New York Times has been “working for” AI operators, and they want more bargaining power. And it seems they’re not pulling any punches, given they are considering both legal action to remove past data and using robots.txt to withhold future data."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "Reasons to Opt Out or Data Strike"
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
"byteEnd": 298,
"byteStart": 280
},
"features": [
{
"uri": "https://www.telegraph.co.uk/business/2023/08/21/internets-original-sin-ai-nightmare/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "The primary concern voiced by the anonymous New York Times employees who made the public aware of potential legal action is an increasingly prominent one: AI operators can use your content, traces, and records to “compete against you”. Some have called AI data practices a “property land grab”, with the assumption that a good portion of training data (like the words that make up a New York Times article, or your blog post or podcast transcript) are considered intellectual property (and subject to relevant laws)."
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
"byteEnd": 278,
"byteStart": 248
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
"byteEnd": 158,
"byteStart": 151
},
"features": [
{
"uri": "https://www.phenomenalworld.org/analysis/data-as-property/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Even if you’re not a fan of intellectual property or a framing that treats data as something to be governed with property law (see e.g. writing from Viljoen on the topic of “data as property”), you might view ML/AI systems as likely to enact economic harms via competition. It seems fair to assume the probability that an AI system can replicate your style or ideas increases when there’s more content (i.e. more sequences of text in the context of LLMs) created by you or people like you in the training data."
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
"byteEnd": 304,
"byteStart": 296
},
"features": [
{
"uri": "https://floriantramer.com/publications/verbatim22/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 145,
"byteStart": 142
},
"features": [
{
"uri": "https://floriantramer.com/publications/diffusion23/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "A related reason to want out of training data is privacy. Diffusion models (used in some of the popular image-generation products) definitely can output exact copies of training inputs (for instance, a picture of your face!). Language models similarly might memorize your writing and spit it out verbatim, leading to a host of thorny questions about how to handle such situations."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "We might think of these concerns – property dispossession, economic harms via competition and privacy risks – as emerging from the same underlying truth about LLMs and similar technologies: when there are more sequences or patterns in the training data that come from a particular group (like a news company), downstream models are more capable of producing output sequences that look like that group’s sequences. If keeping your sequences (broadly construed) somewhat hidden is important to you, you might want to consider opting out."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "Reasons Not to Opt out"
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
"byteEnd": 835,
"byteStart": 816
},
"features": [
{
"uri": "https://www.economicpossibility.org/insights/codetermination-is-not-a-standalone-institution-rather-it-is-part-of-a-broader-in",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 389,
"byteStart": 384
},
"features": [
{
"uri": "https://dl.acm.org/doi/10.1145/3442188.3445922",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 356,
"byteStart": 349
},
"features": [
{
"uri": "http://a",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Of course, there are good reasons to believe that having content and other contributions in a training dataset provides you (or the New York Times) with benefits. If a model is devoid of any training data that covers your area of interest, you’re unlikely to be able to use the model in cases in which it could be useful. While the many potential hazards of LLMs (some stated quite early on) persist in current products, it remains a possibility that another large newspaper that embraces generative AI might out-compete an organization like the New York Times. Depending on how things play out, it could be the case that some organizations who opt-out of generative AI training do not end up winning in the long term. Ultimately, there is an industry wide collective action problem here with major parallels with sectoral bargaining. This society-level collective action problem is a separate topic."
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
"byteEnd": 421,
"byteStart": 413
},
"features": [
{
"uri": "https://pubmed.ncbi.nlm.nih.gov/33982031/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 412,
"byteStart": 410
},
"features": [
{
"uri": "https://www.katecrawford.net/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 409,
"byteStart": 402
},
"features": [
{
"uri": "https://virginia-eubanks.com/automating-inequality/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 40,
"byteStart": 37
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "There’s another reason a group may not want to opt-out (or may want to opt-in given the chance): dataset representation. Opt-out decisions intersect with long-standing concerns about fairness and bias in a wide array of ML and AI systems. While AI systems often contribute to injustice because of inequities present in the social networks or physical infrastructures in which they are deployed (in a variety of contexts), it’s also true that AI systems can exhibit sometimes severe group-level performance gaps because of representation issues in training data. Put simply, if an entire organization or group were to truly disappear from generative AI training data, we’d expect to see major responsible AI issues. For instance, while ML/AI technologies often exhibit geographical biases, e.g. centering the US and western Europe, we could imagine a bizarro-world LLM that literally has seen evidence of that any country other than the US exists. Such an LLM would probably produce an enormous amount of errors, leading to major blunders for users."
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
"byteEnd": 444,
"byteStart": 438
},
"features": [
{
"uri": "https://site.spawning.ai/spawning-ai-txt",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 202,
"byteStart": 183
},
"features": [
{
"uri": "https://www.theverge.com/2023/8/21/23840705/new-york-times-openai-web-crawler-ai-gpt",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Finally, it’s worth discussing the practical costs of data strike actions. This case highlights two concrete examples of specific actions an organization might take to data strike: updating robots.txt and taking legal action. In this case, the possibility of legal action suggests quite high costs. On the other hand, it’s interesting to see NYT just updating their robots.txt – that’s something anyone with a website can do (see ai.txt as well). However, updating these txt files is still non-trivial considering the platform-centric way the vast majority of the world interacts with the web."
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
"byteEnd": 23,
"byteStart": 19
},
"features": [
{
"uri": "https://www.datalevers.org",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "These aren’t the only options. In general though, the most efficacious actions will probably require pretty serious costs. This isn’t necessarily a total non-starter, because effective data strikes require collective action anyway (probably at the scale of a coalition of firms, or large group of consumers)."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "What’s next"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "I hope add an appendum to this post as more information about the NYT’s plan is made public. Additionally, look out for part 2, discussing how we might predict the efficacy of this data strike, and how we might measure the efficacy from an external or internal perspective."
}
}
]
}
]
},
"description": "The New York Times is trying to remove its content from OpenAI models, surfacing tensions around copyright, economic harms, privacy, and the distribution of AI benefits.",
"publishedAt": "2023-08-25T00:00:00.000Z"
}
}
