---
title: "Live by the free-content-for-training sword, die by the free-content-for-training sword"
person: "nick-vincent"
section: "by"
type: "blog-post"
year: 2025
date: "2025-01-28"
venue: "Data Leverage (Digital Garden / dataleverage.substack.com)"
authors: "Nicholas Vincent"
source_url: "https://nickmvincent.github.io/long-posts/live-by-the-free-content-for-training.html"
retrieved: "2026-08-13"
content: "full-text"
notes: "Dek: There's deep tension in the current ask-for-forgiveness-free-for-all approach to acquiring data for model training. Will \"open\" models cause this tension to reach a breaking point? Garden section: long-posts. Mirrored on the Data Leverage Substack."
---

# Live by the free-content-for-training sword, die by the free-content-for-training sword

## Full text

Illustration of a petard, 17th century. Famously known to hoist
engineers who built them. Library of Congress, Wikimedia
Commons.

OpenAI, Anthropic, Google, and more all offer subscription-based AI
products. You pay them, and you get access to an interface that provides
you with model-generated outputs for all sorts of queries. Like many
tech products, you agree to certain Terms of Service (though you
probably haven’t read them all) that restrict what you can do with these
outputs. One theme that cuts across these Terms:

-

You cannot extract data programatically

-

You cannot use “The Output” to compete with the provider

Together, these clauses mean you are expressly violating the Terms of
Service if you were to try to collect model Output in bulk and train a
new model using said Output (I’ve captured a some relevant text from
various Terms at the end of this post).

At the same time, none of these organizations (to my knowledge) have
posted a public document describing the full set of inputs that were
used for training their models (although non-profit labs like AI2
have produced fully documented models like OLMo2). Unsealed documents
from a case against Meta suggest that the inputs used by the major labs
include, among other things, clearly pirated content, and that there is
an “everybody
is doing it” impression that is widely shared in the industry. To
quote directly, “it is known that OpenAI and Mistral are using the
library for their models (through word of mouth)”.

So, what gives? Doesn’t the idea that these firms are simultaneously
arguing
for the right to train on anything they can get their hands on while
denying their competitors the right to train on model outputs seem a
little bit inconsistent? Rules for thee, but not for me? Such behaviour
is by no means unprecedented or really all that shocking — in fact, it’s
the sort of thing that can be explained easily in terms of rational
decision-making. If you think you can get away with it, why wouldn’t you
try to take your grocery cart with 30 items into the express lane and
skip the line, or hop into the carpool lane by yourself while nobody is
looking?

Well, one rejoinder is that in doing so, you’re taking the first step
towards demolishing a valuable system of norms. Another one is: often
times, you will get caught and rebuffed or punished!

In the case of AI training, there haven’t been any police sirens
quite yet (though major decisions are looming). But, the cascade of norm
violation has started: it’s now widely assumed that many models are
being trained on ostensibly Terms of Service-locked outputs, and as far
as I know, no AI lab has tried to take any major enforcement actions
yet. In other words, it’s considered very likely that the outputs from
powerful models produced by OpenAI, Anthropic, and company are indeed
being used to train models operated by other firms.

Of course, the optics of taking enforcement action would not be great
— it could look an awful lot like a lone driver in the carpool lane
trying to make a citizen’s arrest of another lone driver. It would be
hard to enforce these Terms of Service against a sympathetic actor
without drawing attention to the extant tension in the current training
paradigm.

So, it seems that AI labs may need to live
by the sword, and thusly die by the sword. Or, to draw on another
idiom, perhaps the industry will be hoisted
with its own petard.

And this week, a new model has rocked the AI world (well, at least
online AI discourse focusing on investment
and policy
— as far as I can tell, most researchers are reacting much more
soberly). DeepSeek’s R1 product — which has accompanying MIT-licensed
model weights —
seems to perform extremely well. The release also includes a detailed technical report with
details about the reinforcement learning-based post-training and
efficiency improvements that led to such results, but no mention of
training data.

It’s likely the case that AI model outputs made their way into the
training set, either directly or because these outputs have diffused
into the open Internet (see Wiggers in TechCrunch on “Why
DeepSeek’s new AI model thinks it’s ChatGPT” for full reporting on
this). The tension at the heart of arguing for free-for-all training
while restricting output use has been lurking under the surface since
the generative AI boom began, and now proliferation of open models may
bring this tension fully into the open.

I think a few things may happen in response. On one hand, given that
the discussion around DeepSeek and the US AI industry is deeply
entangled with national security discussions (for better or worse), it
could be the case that US politicians start to express concern with the
status quo around model distillation. For instance, it could the case
that a senator or other figure who wants the US to win the “AI
race” could see the R1 release as evidence that US-based AI labs
need to do even more to gate their model outputs, perhaps leading to
increased efforts to actually enforce these terms of service.

It could also be the case that increased discussion of data practices
highlights what is arguably hypocrisy that favors Big Tech over
consumers and “Little Tech”, perhaps leading regulators who are upset
with Big Tech (an issue that cuts across the political aisle) to amplify
efforts to regulate data transparency (looking back towards efforts like
the Dashboard
Act).

Finally, while not extremely likely in the short term, I am hopeful
that these discussions could invigorate consumer appetite for AI models
that do not use proprietary blends of training data. While the current
menu of AI products does not allow for much flexibility in terms of
picking a model that aligns with one’s values, the future may provide
such flexibility.

Importantly, as the tension inherent in a “live by the sword, die by
the sword” approach to AI data becomes prevalent (and as the the tech
industry starts to get more concerned about being hoisted by its own
petard), there could emerge a massive opportunity for existing
technology companies or new start-ups to carve an identity as especially
focused on data supply chain integrity and trust, and offer a product
that has no such tension. This could turn into a major win on the basis
of changing consumer demand, and would also provide first mover
advantage if regulators put an end to the current set of practices.

Overall, I’d be surprised if the current status quo doesn’t face some
degree of reckoning because of proliferation of open models, and I’m
hopeful that the reaction can be positive in the long run for the tech
industry. As usual, I expect that supporting more data transparency and
collective action by data creators will play a major role in creating
momentum towards a better paradigm.

—

Relevant Terms of Service sections, captured Jan 27, 2025.

OpenAI

Anthropic

Google
Gemini

Source revision history

Selected Git commits that changed this source file.

- 9fb4674b8a 2026-07-12 - Migrate blog into digital presence monorepo

Mirror freshness

Maintenance status for tracked full-copy mirrors of this post.

-
Current
substack

mirror 2025-01-28

Baseline from original_url

Source and AT Protocol record

Source path
content/writing/posts/2025-01-28-live-by-the-free-content-for-training.md

AT Protocol URI
at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.document/3mizeeo44aigk

Exact public AT Protocol record cached for the Leaflet/Bluesky-facing copy.

{
"uri": "at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.document/3mizeeo44aigk",
"cid": "bafyreiaoa2gf5kwa2ficakh7fnwonschxtlvccxw6fg57hrxqhupbdmudy",
"value": {
"path": "/3mizeeo44aigk",
"site": "at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.publication/3lzrsw2kvwc2m",
"$type": "site.standard.document",
"title": "Live by the free-content-for-training sword, die by the free-content-for-training sword",
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
"$link": "bafkreiclnbc6tpcj42e2bjqt77lfjxo464osdiodjky6h67hxo4lu4b7fa"
},
"mimeType": "image/jpeg",
"size": 145031
},
"aspectRatio": {
"$type": "pub.leaflet.blocks.image#aspectRatio",
"width": 800,
"height": 559
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
"byteStart": 111
},
"features": [
{
"uri": "https://en.wikipedia.org/wiki/File:Petardsketch2.jpg",
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
"byteEnd": 111,
"byteStart": 63
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
"byteEnd": 63,
"byteStart": 58
},
"features": [
{
"uri": "https://en.wikipedia.org/wiki/Hoist_with_his_own_petard",
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
"byteEnd": 58,
"byteStart": 0
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "Illustration of a petard, 17th century. Famously known to hoist engineers who built them. Library of Congress, Wikimedia Commons."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "OpenAI, Anthropic, Google, and more all offer subscription-based AI products. You pay them, and you get access to an interface that provides you with model-generated outputs for all sorts of queries. Like many tech products, you agree to certain Terms of Service (though you probably haven’t read them all) that restrict what you can do with these outputs. One theme that cuts across these Terms:"
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
"plaintext": "You cannot extract data programatically"
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "You cannot use “The Output” to compete with the provider"
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
"plaintext": "Together, these clauses mean you are expressly violating the Terms of Service if you were to try to collect model Output in bulk and train a new model using said Output (I’ve captured a some relevant text from various Terms at the end of this post)."
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
"byteEnd": 445,
"byteStart": 424
},
"features": [
{
"uri": "https://www.theverge.com/2025/1/14/24343692/meta-lawsuit-copyright-lawsuit-llama-libgen",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 273,
"byteStart": 264
},
"features": [
{
"uri": "https://chatgptiseatingtheworld.com/2025/01/15/kadrey-refiles-motion-to-file-third-amended-consolidated-complaint-with-partially-unredacted-exhibits-per-judge-chhabrias-order/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 252,
"byteStart": 247
},
"features": [
{
"uri": "https://allenai.org/olmo",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 208,
"byteStart": 204
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "At the same time, none of these organizations (to my knowledge) have posted a public document describing the full set of inputs that were used for training their models (although non-profit labs like AI2 have produced fully documented models like OLMo2). Unsealed documents from a case against Meta suggest that the inputs used by the major labs include, among other things, clearly pirated content, and that there is an “everybody is doing it” impression that is widely shared in the industry. To quote directly, “it is known that OpenAI and Mistral are using the library for their models (through word of mouth)”."
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
"byteEnd": 78,
"byteStart": 71
},
"features": [
{
"uri": "https://www.reuters.com/legal/litigation/tech-companies-face-tough-ai-copyright-questions-2025-2024-12-27/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "So, what gives? Doesn’t the idea that these firms are simultaneously arguing for the right to train on anything they can get their hands on while denying their competitors the right to train on model outputs seem a little bit inconsistent? Rules for thee, but not for me? Such behaviour is by no means unprecedented or really all that shocking — in fact, it’s the sort of thing that can be explained easily in terms of rational decision-making. If you think you can get away with it, why wouldn’t you try to take your grocery cart with 30 items into the express lane and skip the line, or hop into the carpool lane by yourself while nobody is looking?"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Well, one rejoinder is that in doing so, you’re taking the first step towards demolishing a valuable system of norms. Another one is: often times, you will get caught and rebuffed or punished!"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "In the case of AI training, there haven’t been any police sirens quite yet (though major decisions are looming). But, the cascade of norm violation has started: it’s now widely assumed that many models are being trained on ostensibly Terms of Service-locked outputs, and as far as I know, no AI lab has tried to take any major enforcement actions yet. In other words, it’s considered very likely that the outputs from powerful models produced by OpenAI, Anthropic, and company are indeed being used to train models operated by other firms."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Of course, the optics of taking enforcement action would not be great — it could look an awful lot like a lone driver in the carpool lane trying to make a citizen’s arrest of another lone driver. It would be hard to enforce these Terms of Service against a sympathetic actor without drawing attention to the extant tension in the current training paradigm."
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
"byteStart": 145
},
"features": [
{
"uri": "https://en.wikipedia.org/wiki/Hoist_with_his_own_petard",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 84,
"byteStart": 38
},
"features": [
{
"uri": "https://en.wikipedia.org/wiki/Live_by_the_sword,_die_by_the_sword",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "So, it seems that AI labs may need to live by the sword, and thusly die by the sword. Or, to draw on another idiom, perhaps the industry will be hoisted with its own petard."
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
"byteEnd": 365,
"byteStart": 349
},
"features": [
{
"uri": "https://arxiv.org/abs/2501.12948",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 274,
"byteStart": 267
},
"features": [
{
"uri": "https://huggingface.co/deepseek-ai/DeepSeek-R1",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 120,
"byteStart": 114
},
"features": [
{
"uri": "https://www.wired.com/story/deepseek-ai-china-privacy-data/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 109,
"byteStart": 99
},
"features": [
{
"uri": "https://www.reuters.com/technology/chinas-deepseek-sets-off-ai-market-rout-2025-01-27/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "And this week, a new model has rocked the AI world (well, at least online AI discourse focusing on investment and policy — as far as I can tell, most researchers are reacting much more soberly). DeepSeek’s R1 product — which has accompanying MIT-licensed model weights — seems to perform extremely well. The release also includes a detailed technical report with details about the reinforcement learning-based post-training and efficiency improvements that led to such results, but no mention of training data."
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
"byteEnd": 245,
"byteStart": 194
},
"features": [
{
"uri": "https://techcrunch.com/2024/12/27/why-deepseeks-new-ai-model-thinks-its-chatgpt/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "It’s likely the case that AI model outputs made their way into the training set, either directly or because these outputs have diffused into the open Internet (see Wiggers in TechCrunch on “Why DeepSeek’s new AI model thinks it’s ChatGPT” for full reporting on this). The tension at the heart of arguing for free-for-all training while restricting output use has been lurking under the surface since the generative AI boom began, and now proliferation of open models may bring this tension fully into the open."
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
"byteEnd": 415,
"byteStart": 408
},
"features": [
{
"uri": "https://www.cnbc.com/2025/01/23/scale-ai-ceo-says-china-has-quickly-caught-the-us-with-deepseek.html",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "I think a few things may happen in response. On one hand, given that the discussion around DeepSeek and the US AI industry is deeply entangled with national security discussions (for better or worse), it could be the case that US politicians start to express concern with the status quo around model distillation. For instance, it could the case that a senator or other figure who wants the US to win the “AI race” could see the R1 release as evidence that US-based AI labs need to do even more to gate their model outputs, perhaps leading to increased efforts to actually enforce these terms of service."
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
"byteEnd": 371,
"byteStart": 358
},
"features": [
{
"uri": "https://www.clarip.com/blog/senate-dashboard-act/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "It could also be the case that increased discussion of data practices highlights what is arguably hypocrisy that favors Big Tech over consumers and “Little Tech”, perhaps leading regulators who are upset with Big Tech (an issue that cuts across the political aisle) to amplify efforts to regulate data transparency (looking back towards efforts like the Dashboard Act)."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Finally, while not extremely likely in the short term, I am hopeful that these discussions could invigorate consumer appetite for AI models that do not use proprietary blends of training data. While the current menu of AI products does not allow for much flexibility in terms of picking a model that aligns with one’s values, the future may provide such flexibility."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Importantly, as the tension inherent in a “live by the sword, die by the sword” approach to AI data becomes prevalent (and as the the tech industry starts to get more concerned about being hoisted by its own petard), there could emerge a massive opportunity for existing technology companies or new start-ups to carve an identity as especially focused on data supply chain integrity and trust, and offer a product that has no such tension. This could turn into a major win on the basis of changing consumer demand, and would also provide first mover advantage if regulators put an end to the current set of practices."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Overall, I’d be surprised if the current status quo doesn’t face some degree of reckoning because of proliferation of open models, and I’m hopeful that the reaction can be positive in the long run for the tech industry. As usual, I expect that supporting more data transparency and collective action by data creators will play a major role in creating momentum towards a better paradigm."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "—"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Relevant Terms of Service sections, captured Jan 27, 2025."
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
"byteEnd": 6,
"byteStart": 0
},
"features": [
{
"uri": "https://openai.com/policies/row-terms-of-use/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "OpenAI"
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
"byteEnd": 9,
"byteStart": 0
},
"features": [
{
"uri": "https://www.anthropic.com/legal/consumer-terms",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Anthropic"
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
"byteEnd": 13,
"byteStart": 0
},
"features": [
{
"uri": "https://ai.google.dev/gemini-api/terms",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Google Gemini"
}
}
]
}
]
},
"description": "There's deep tension in the current ask-for-forgiveness-free-for-all approach to acquiring data for model training. Will \"open\" models cause this tension to reach a breaking point?",
"publishedAt": "2025-01-28T00:00:00.000Z"
}
}
