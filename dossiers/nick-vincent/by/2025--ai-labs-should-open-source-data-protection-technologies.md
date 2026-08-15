---
title: "AI Labs Should Open Source Data Protection Technologies"
person: "nick-vincent"
section: "by"
type: "blog-post"
year: 2025
date: "2025-01-31"
venue: "Data Leverage (Digital Garden / dataleverage.substack.com)"
authors: "Nicholas Vincent"
source_url: "https://nickmvincent.github.io/long-posts/ai-labs-could-open-source-data-protection.html"
retrieved: "2026-08-13"
content: "full-text"
notes: "Dek: There's still incredible tension in the current data paradigm, but sharing \"data protection\" technologies, like those used by OpenAI to accuse DeepSeek of model theft, can help cut a path forward. Garden section: long-posts. Mirrored on the Data Leverage Substack."
---

# AI Labs Should Open Source Data Protection Technologies

## Full text

Wikipedia article on Trap
streets.

DeepSeek’s R1 release was a wake-up call for tech companies that they
are in the same boat as content owners. On January 29th, several venues
(see e.g. coverage in the Financial
Times, Bloomberg,
and 404
Media) covered an emerging story: OpenAI has evidence that DeepSeek,
a Chinese AI lab used OpenAI’s model outputs to train it’s model, and
OpenAI is claiming that said outputs should be treated as
proprietary.

NYT Tech columnist Kevin Roose responded
on X: “must suck to have someone train AI models on your data without
permission, wonder what that's like”. This response summed up quite a
few responses across social media (comments to the 404 Media piece on Bluesky
and Hackernews had
a similar tone). Many of these responses channeled various idioms and
proverbs that reference poetic justice (my own post
from Monday leaned into “live by the sword, die by the sword” and
“hoisted by one’s own petard”).

In this relatively brief follow up post, I want to highlight that
this moment could provide a huge opportunity for making progress towards
a healthier content ecosystems. While the reckoning over the current
data paradigm may ultimately lead some organizations to become
more open (perhaps some labs will remove some clauses
from their Terms of Service, and/or give up on enforcing them, and/or
release more model weights or datasets), it’s likely that there will be
cases where organizations instead take data protection action — which
will involve some combination of using both published, and proprietary
techniques as well as developing new “data protection tech”. One point
of speculation from my last post was a government official might begin
to pressure AI labs to allocate more resources towards data protection,
perhaps citing national security concerns (when I made this prediction,
I will admit that I did not expect said government-affiliated individual
to be major Silicon Valley figure David
Sacks).

It isn’t clear to yet what extent OpenAI’s evidence is based on
access logs, audit-style estimates of output similarity, watermarking techniques
from academic literature, or some yet-to-be-revealed technique (I
imagine it’s something a bit more sophisticated than prompting the model
with “What is your model name?”). But it does seem clear that in the
near term OpenAI and Microsoft are marching towards the protection path
(the comments across Hackernews, X, Bluesky, and podcasts have yet to
faze them).

### A proposal

Let’s assume AI labs have invested, and will continue to invest in,
data protection techniques including, but not limited to, signal
processing of API endpoints and consumer interface access logs, output
similarity estimation, watermarking, and yet-to-be-revealed techniques.
Let’s also assume that in the near-term, US-based AI labs will continue
to keep their frontier model weights closed (which, to be clear, I do
not think is a clearly anti-social move — there is legitimate AI safety
debate to be had on this topic) and their training data details hidden
(on this front, I think the current paradigm is clearly anti-social for
labor substitution, content ecosystems, and research reproducibility
reasons).

What these labs could do — which would be in line with the mission to
ensure all of humanity benefits from AI and would provide immediate
mitigation of some economic concerns — would be to open-source all data
protection tools and provide a road map for content-creating
organizations and individuals to use the same overall data protection
strategy that AI labs use. And of course, if certain techniques can be
too easily “defeated” if their code is fully open, there could still be
technology-sharing agreements between AI labs and content
organizations.

If it’s the case that going forward most “data protection” will
achieved by monitoring access logs to API endpoints and consumer
interfaces (i.e., looking for fishy bursts in API or ChatGPT usage),
these techniques could be employed by data intermediaries who “hold
onto” data and content going forward so that reasonable collective
bargaining can be achieved.

If it’s instead the case that watermarking is the way forward,
creators can begin watermarking their outputs (which will likely also
require some degree of coordination or the creation of data intermediary
organizations). Finally, if some wildly creative approach emerges, that
too could be employed.

In short, “data protection technologies” provide be one path towards
a more level playing field for controlling the flow of data and
information in the AI age, so firms and labs that feel their hands are
tied when it comes to sharing weights and data should share these
technologies.

### Would this
really work, and isn’t this “anti-open”?

Of course, a key criticism of this approach is that the whole notion
of claiming model outputs to be proprietary is not all that coherent in
the first place. Models outputs are heavily dependent on documents from
the Internet and post-training data labor. An argument can (and will) be
made that we should swing in the opposite direction, and give up on data
protection entirely (i.e., proponents of this view would likely say that
it would be best for regulators to strike down any such attempts to
claim ownership over outputs by OpenAI or Microsoft).

Another concerning aspect of the paradigm that AI labs and tech
companies are arguing for is the massive tension between the notion that
I own my Outputs from AI models but cannot use said Outputs to compete
with AI labs. Practically, of course, there’s an obvious difference
between sharing a LLM-assisted code snippet under my name and doing mass
exfiltration of data via API calls or web browser automation. But
there’s quite a grey area here — what if my friends and I spent a year
writing code with LLM assistance and want to fine-tune a small,
community-led model on those outputs? What’s the exact point at which we
will be subject to the same scrutiny as DeepSeek?

### Towards healthy
collective bargaining

I am personally very skeptical of swinging our pendulum too far
towards either extreme. Letting labs and large firms claim total
ownership over model outputs while vacuuming the Internet seems
suboptimal (and the public reaction suggests people do not like this).
Complete abdication over any bargaining power for content creators and
information gatherers also seems concerning, both because of practical
questions about the future incentives to e.g., conduct journalistic
labor or create artisanal objects, and because of moral concerns about
dispossession of intellectual output.

So, I think we need something in the middle (ideally, a sober and
honest reckoning with regards to what data will have bargaining value
going forward, and then the creation and protection of intermediary
organizations that facilitate collective bargaining for new information
— see Matt Prewitt’s writing here
for a concrete vision along these lines), and sharing data protection
techniques is much more likely to help than hurt.

Overall, if we assume data protection action will move forwards and
will in some cases benefit AI labs and technology companies, it will be
better for society if these techniques also benefit content creators.
And if these data protection action don’t work at all, or prove too
incoherent, it’s better if that is out in the open and we can as honest
as possible about which bundles of information are worth bargaining
for.

And hey, it might provide a huge morale boost to AI lab and Big Tech
employees who want to open-source more artifacts!

Edits:

- Feb 11, 2025: typos and format fixes.

Source revision history

Selected Git commits that changed this source file.

- 9fb4674b8a 2026-07-12 - Migrate blog into digital presence monorepo

Mirror freshness

Maintenance status for tracked full-copy mirrors of this post.

-
Current
substack

mirror 2025-01-31

Baseline from original_url

Source and AT Protocol record

Source path
content/writing/posts/2025-01-31-ai-labs-could-open-source-data-protection.md

AT Protocol URI
at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.document/3mizeen6k4rog

Exact public AT Protocol record cached for the Leaflet/Bluesky-facing copy.

{
"uri": "at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.document/3mizeen6k4rog",
"cid": "bafyreid4cx3wswazcbi2q3mlj2bsdxk3pokyohchhu5viqkzmyqlpfqv3m",
"value": {
"path": "/3mizeen6k4rog",
"site": "at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.publication/3lzrsw2kvwc2m",
"$type": "site.standard.document",
"title": "AI Labs Should Open Source Data Protection Technologies",
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
"$link": "bafkreiaodlia6qkculue46joiti4q7ug7jnd7xhnwmsjvghtw4mrrspf3i"
},
"mimeType": "image/png",
"size": 614995
},
"aspectRatio": {
"$type": "pub.leaflet.blocks.image#aspectRatio",
"width": 1808,
"height": 1016
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
"byteStart": 33
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
"byteEnd": 33,
"byteStart": 21
},
"features": [
{
"uri": "https://en.wikipedia.org/wiki/Trap_street",
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
"byteEnd": 21,
"byteStart": 0
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "Wikipedia article on Trap streets."
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
"byteEnd": 211,
"byteStart": 202
},
"features": [
{
"uri": "https://www.404media.co/openai-furious-deepseek-might-have-stolen-all-the-data-openai-stole-from-us/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 196,
"byteStart": 187
},
"features": [
{
"uri": "https://www.bloomberg.com/news/articles/2025-01-29/microsoft-probing-if-deepseek-linked-group-improperly-obtained-openai-data",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 185,
"byteStart": 170
},
"features": [
{
"uri": "https://www.ft.com/content/a0dfedd1-5255-4fa9-8ccc-1fe01de87ea6",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "DeepSeek’s R1 release was a wake-up call for tech companies that they are in the same boat as content owners. On January 29th, several venues (see e.g. coverage in the Financial Times, Bloomberg, and 404 Media) covered an emerging story: OpenAI has evidence that DeepSeek, a Chinese AI lab used OpenAI’s model outputs to train it’s model, and OpenAI is claiming that said outputs should be treated as proprietary."
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
"byteEnd": 403,
"byteStart": 399
},
"features": [
{
"uri": "https://dataleverage.substack.com/p/live-by-the-free-content-for-training",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 277,
"byteStart": 267
},
"features": [
{
"uri": "https://news.ycombinator.com/item?id=42865527",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 262,
"byteStart": 255
},
"features": [
{
"uri": "https://bsky.app/profile/404media.co/post/3lgvcq53j322a",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 40,
"byteStart": 31
},
"features": [
{
"uri": "https://x.com/kevinroose/status/1884488496649494810",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "NYT Tech columnist Kevin Roose responded on X: “must suck to have someone train AI models on your data without permission, wonder what that's like”. This response summed up quite a few responses across social media (comments to the 404 Media piece on Bluesky and Hackernews had a similar tone). Many of these responses channeled various idioms and proverbs that reference poetic justice (my own post from Monday leaned into “live by the sword, die by the sword” and “hoisted by one’s own petard”)."
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
"byteEnd": 1020,
"byteStart": 1009
},
"features": [
{
"uri": "https://www.nbcnews.com/tech/tech-news/openai-says-deepseek-may-inapproriately-used-data-rcna189872",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 311,
"byteStart": 305
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
"byteEnd": 275,
"byteStart": 271
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "In this relatively brief follow up post, I want to highlight that this moment could provide a huge opportunity for making progress towards a healthier content ecosystems. While the reckoning over the current data paradigm may ultimately lead some organizations to become more open (perhaps some labs will remove some clauses from their Terms of Service, and/or give up on enforcing them, and/or release more model weights or datasets), it’s likely that there will be cases where organizations instead take data protection action — which will involve some combination of using both published, and proprietary techniques as well as developing new “data protection tech”. One point of speculation from my last post was a government official might begin to pressure AI labs to allocate more resources towards data protection, perhaps citing national security concerns (when I made this prediction, I will admit that I did not expect said government-affiliated individual to be major Silicon Valley figure David Sacks)."
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
"byteEnd": 148,
"byteStart": 138
},
"features": [
{
"uri": "https://openai.com/index/understanding-the-source-of-what-we-see-and-hear-online/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 137,
"byteStart": 125
},
"features": [
{
"uri": "https://arxiv.org/abs/2301.10226",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "It isn’t clear to yet what extent OpenAI’s evidence is based on access logs, audit-style estimates of output similarity, watermarking techniques from academic literature, or some yet-to-be-revealed technique (I imagine it’s something a bit more sophisticated than prompting the model with “What is your model name?”). But it does seem clear that in the near term OpenAI and Microsoft are marching towards the protection path (the comments across Hackernews, X, Bluesky, and podcasts have yet to faze them)."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "A proposal"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Let’s assume AI labs have invested, and will continue to invest in, data protection techniques including, but not limited to, signal processing of API endpoints and consumer interface access logs, output similarity estimation, watermarking, and yet-to-be-revealed techniques. Let’s also assume that in the near-term, US-based AI labs will continue to keep their frontier model weights closed (which, to be clear, I do not think is a clearly anti-social move — there is legitimate AI safety debate to be had on this topic) and their training data details hidden (on this front, I think the current paradigm is clearly anti-social for labor substitution, content ecosystems, and research reproducibility reasons)."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "What these labs could do — which would be in line with the mission to ensure all of humanity benefits from AI and would provide immediate mitigation of some economic concerns — would be to open-source all data protection tools and provide a road map for content-creating organizations and individuals to use the same overall data protection strategy that AI labs use. And of course, if certain techniques can be too easily “defeated” if their code is fully open, there could still be technology-sharing agreements between AI labs and content organizations."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "If it’s the case that going forward most “data protection” will achieved by monitoring access logs to API endpoints and consumer interfaces (i.e., looking for fishy bursts in API or ChatGPT usage), these techniques could be employed by data intermediaries who “hold onto” data and content going forward so that reasonable collective bargaining can be achieved."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "If it’s instead the case that watermarking is the way forward, creators can begin watermarking their outputs (which will likely also require some degree of coordination or the creation of data intermediary organizations). Finally, if some wildly creative approach emerges, that too could be employed."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "In short, “data protection technologies” provide be one path towards a more level playing field for controlling the flow of data and information in the AI age, so firms and labs that feel their hands are tied when it comes to sharing weights and data should share these technologies."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "Would this really work, and isn’t this “anti-open”?"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Of course, a key criticism of this approach is that the whole notion of claiming model outputs to be proprietary is not all that coherent in the first place. Models outputs are heavily dependent on documents from the Internet and post-training data labor. An argument can (and will) be made that we should swing in the opposite direction, and give up on data protection entirely (i.e., proponents of this view would likely say that it would be best for regulators to strike down any such attempts to claim ownership over outputs by OpenAI or Microsoft)."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Another concerning aspect of the paradigm that AI labs and tech companies are arguing for is the massive tension between the notion that I own my Outputs from AI models but cannot use said Outputs to compete with AI labs. Practically, of course, there’s an obvious difference between sharing a LLM-assisted code snippet under my name and doing mass exfiltration of data via API calls or web browser automation. But there’s quite a grey area here — what if my friends and I spent a year writing code with LLM assistance and want to fine-tune a small, community-led model on those outputs? What’s the exact point at which we will be subject to the same scrutiny as DeepSeek?"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "Towards healthy collective bargaining"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "I am personally very skeptical of swinging our pendulum too far towards either extreme. Letting labs and large firms claim total ownership over model outputs while vacuuming the Internet seems suboptimal (and the public reaction suggests people do not like this). Complete abdication over any bargaining power for content creators and information gatherers also seems concerning, both because of practical questions about the future incentives to e.g., conduct journalistic labor or create artisanal objects, and because of moral concerns about dispossession of intellectual output."
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
"byteEnd": 313,
"byteStart": 309
},
"features": [
{
"uri": "https://www.radicalxchange.org/media/blog/three-pathways-to-distributed-power-in-the-ai-economy/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "So, I think we need something in the middle (ideally, a sober and honest reckoning with regards to what data will have bargaining value going forward, and then the creation and protection of intermediary organizations that facilitate collective bargaining for new information — see Matt Prewitt’s writing here for a concrete vision along these lines), and sharing data protection techniques is much more likely to help than hurt."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Overall, if we assume data protection action will move forwards and will in some cases benefit AI labs and technology companies, it will be better for society if these techniques also benefit content creators. And if these data protection action don’t work at all, or prove too incoherent, it’s better if that is out in the open and we can as honest as possible about which bundles of information are worth bargaining for."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "And hey, it might provide a huge morale boost to AI lab and Big Tech employees who want to open-source more artifacts!"
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
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "Edits:"
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
"byteEnd": 37,
"byteStart": 0
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "Feb 11, 2025: typos and format fixes."
}
}
]
}
}
]
}
]
},
"description": "There's still incredible tension in the current data paradigm, but sharing \"data protection\" technologies, like those used by OpenAI to accuse DeepSeek of model theft, can help cut a path forward.",
"publishedAt": "2025-01-31T00:00:00.000Z"
}
}
