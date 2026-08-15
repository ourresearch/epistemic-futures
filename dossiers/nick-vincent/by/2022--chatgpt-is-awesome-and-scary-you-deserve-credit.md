---
title: "ChatGPT is Awesome and Scary: You Deserve Credit for the Good Parts (and Might Help Fix the Bad Parts)"
person: "nick-vincent"
section: "by"
type: "blog-post"
year: 2022
date: "2022-12-04"
venue: "Data Leverage (Digital Garden / dataleverage.substack.com)"
authors: "Nicholas Vincent"
source_url: "https://nickmvincent.github.io/long-posts/chatgpt-is-awesome-and-scary-you-deserve-credit.html"
retrieved: "2026-08-13"
content: "full-text"
notes: "Dek: More on why you're an expert language model trainer Garden section: long-posts. Mirrored on the Data Leverage Substack."
---

# ChatGPT is Awesome and Scary: You Deserve Credit for the Good Parts (and Might Help Fix the Bad Parts)

## Full text

In the past I've written on the idea that we're all "Expert Language Model
Trainers". The basic idea: large language models rely on our blog
posts, Wikipedia articles, Reddit votes, arXiv papers, and more, so it's
very likely that much of the Internet-using population has contributed
in some fashion to the training data underlying large language models.
Of course, everyone's "marginal impact" is small (most models would be
nearly unchanged if just one person's data disappeared), but many people
are undoubtedly contributors.

In this post, I'm going to trace the dataset breadcrumbs for the
impressive (and impressively viral) new ChatGPT from OpenAI. The
main goal: to highlight specific ways that Internet users have likely
contributed. My agenda here is not detract from the mind boggling
accomplishments of the OpenAI team, but rather to highlight the immense
amount of upstream human activity and labor upon which these new outputs
draw, and to describe how we can lean on this dependency as a force for
good. Many people may find ChatGPT scary, but I think taking this
data-centric and contribution-centric lens suggests a plausible path for
global-scale "governance" of ChatGPT and inevitable successors.

### A List of Links

To start, here's a list with all the links I'll discuss in this
post:

-

The ChatGPT Blog
Post | Details about ChatGPT

-

OpenAI's
Model Index | Describes the family of "GPT 3.5" models, to which
ChatGPT belongs

-

InstructGPT blog
post | Details about building InstructGPT, which ChatGPT follows
closely

-

InstructGPT paper
| More details than the blog post

-

InstructGPT
Model Card | Summary of the training data, and more

-

CommonCrawl Data |
A key data source

-

WebText
| Another key data source, leveraging reddit votes

### Starting from the ChatGPT
Blog Post

Now let's walk through the information we have about the data, to
make a rough guess about: (1) whether you deserve some credit (admission
of editorial bias: I'm inclined to to say "Yes"), (2) which data sources
are particularly important, and (3) what this means for the impact of AI
systems like GPT 3.5 on society.

We start with the ChatGPT blog post. We learn that the model
was trained "using Reinforcement Learning from Human Feedback (RLHF),
using the same methods as InstructGPT, but with slight differences in
the data collection setup." This points us to the InstructGPT blog post, paper, and model
card. The InstructGPT blog post provides more info about how OpenAI
was able to solicit valuable human feedback, i.e. get people to share
specifically how they feel out GPT responses (we'll return to this, but
first we'll focus on the text data).

### Data Sources in the
InstructGPT Model Card

Looking now at the InstructGPT model
card, we learn that "InstructGPT models are initialized from GPT-3
models, whose training dataset is composed of text posted to the
internet or uploaded to the internet (e.g., books). " Four specific
sources are named: CommonCrawl, Webtext (an
expanded version), two internet-based book corpora (one which is perhaps
BookCorpus), and English-language Wikipedia. We also learn that for
InstructGPT, just 40 labelers participated (and some unknown number of
customers who provided ecologically valid prompts).

The Common Crawl is,
in short, almost everything on the Internet that doesn't explicitly ask
to not be scraped (via a robots.txt file). OK, so if you've posted text
to the Internet, you may have already contributed. We also learn from
the model card that this corpus was "filtered based on similarity to
high-quality reference corpora", so whoever contributed high-quality
content to said reference corpora is likely playing an amplified role.
Unfortunately, we can't be sure yet exactly what this high-quality
reference corpora looks like (but might guess it's something like news
articles, scientific articles, etc.) This also means if contributions to
the Common Crawl were deemed low-quality, those contributions may not
have made it into ChatGPT.

If you're curious about what's specifically in the Common Crawl, the
operators provide a list
of common domains. A quick glance shows quite a few opportunities
for user-generated content (i.e., your contributions): blogpost,
wordpress, pinterest, stackexchange, github, youtube, etc. Of course,
there's a ton of wiki projects, and a lot of ".edu" domains
corresponding to university webpages. If anyone is aware of more tools
for web users to explore Common Crawl and their contributions to it,
please do share and I'll be sure to update this section here.

It's also important to note that Common Crawl has been shown to have
quite a bit of "undesirable content" (see this paper from
Luccioni and Vivianio). This is certainly true of the other data sources
we'll describe as well!

Next, we have the WebText dataset (described here). OpenAI
wanted another "filtered" version of the web, so they grabbed the
content from every webpage posted to Reddit with 3 or more "karma"
points. In other words, Reddit users voted on the training data to be
included. This means even if you've never written a single sentence of
text on the web, but you have voted (up or down) on Reddit, you
contributed to what we might call a "collective intelligence" process
for making GPT's data high quality.

Webtext is not available for direct download, but it was replicated
as part of an open
source effort. It's also worth noting that if you want an open
dataset along these lines, one of the best choices may be The Pile from EleutherAI.

The third source mentioned in the InstructGPT model card is the
combination of "two internet-based book corpora". This could be BookCorpus,
a popular dataset of books from smashbooks.com. It could also be books
from Google Books, from Project Gutenberg, or something else. Looking
back to the GPT3 paper, we see these datasets described as "books1" (12
billion tokens) and "books2" (55 billion tokens).

Finally, the fourth -- and perhaps least surprising -- example in the
model card is English-language Wikipedia. Much of my doctoral research
has discussed how Wikipedia is one of the most important training
sources for data-dependent computing in general (see some examples here).
Another interesting note from the GPT3 paper is that Wikipedia is
intentionally "over-weighted": all the content in English Wikipedia was
seen 3.4 times during training whereas some of the filtered Common Crawl
was skipped entirely.

To summarize so far, if you have: written any high quality text that
appeared in the Common Crawl, submitted to Reddit, voted on a link
submitted to Reddit, written a book, or edited English Wikipedia, you're
almost certainly a contributor to ChatGPT.

### Other Info

We have one other surprising claim about ChatGPT's training... a tweet
from Elon Musk. Here's the text for posterity:

"Not surprising, as I just learned that OpenAI had access to Twitter
database for training. I put that on pause for now. Need to understand
more about governance structure & revenue plans going forward.
OpenAI was started as open-source & non-profit. Neither are still
true."

This suggests yet another avenue for you to have contributed: if
you've ever posted any tweets.

### About that Human Feedback

Returning to the ChatGPT blog post, we know a key unique advantage of
ChatGPT is access to data produced by first asking people to produce
"conversations in which they played both sides—the user and an AI
assistant", training an initial model, and then asking AI trainers to
compare different chatbot outputs and rank them. In other words these AI
trainers were acting as a kind of movie critic for the AI. We could even
say these AI trainers were acting like ChatGPT's university-level film
studies professor.

You're an AI trainer too -- just more similar to ChatGPT's high
school writing teacher (if you've written a few blog posts), history
teacher (if you've edited some Wikipedia articles), or pop culture tutor
(if you've upvoted submissions on reddit about popular media or been
active on Twitter). An understanding of writing, history, and pop
culture is critical to even take the film studies class that the
trainers working directly with OpenAI provided (and if you're not a fan
of film, this whole analogy can work for something like electrical
engineering as well).

### Implications

So, if you've made it this far, maybe I've convinced you to give
yourself a pat on the back (and to tell your friends and family they
deserve a pat on the back, too). What do we do with this argument?

My main line of research is concerned with idea of "data
leverage": that when data-dependent systems rely on contributions
from broad swathes of the public, this creates a potential opportunity
for the public to exert leverage through these data dependencies, and
participate in the governance of these systems. In other words, by
(collectively) threatening to withhold data from organizations you
oppose, or give data to organizations you support, you can shift the
balance towards AI being used in a way that aligns with your values.

A key finding from our research (see e.g. simulations in this paper of different
kinds of data-related collective action) is that this only works if
done collaboratively -- we need collective action.

If you use ChatGPT heavily, you will very likely make even more
contributions to the next version of GPT. You might be able to help
address the errors and failure modes users have already identified (and
indeed, if you've helped shared a viral error on Twitter, you may have
already helped OpenAI deploy a hotfix).

On the other hand, if you hate ChatGPT and its ilk, you may find it
hard to avoid contributing. There are so many avenues through which your
data contributions may end up in the next massive training set. In this
case, the best avenue may be to push for updated regulation around large
language models. Of course, you could also start "poisoning" the text
you post to the web, but this can be a tough call to make because it
will also hurt anyone trying to compete with GPT-4 and beyond.

Based on the framework of data leverage, I personally think we can
focus our efforts along three lines:

-

Make it easier for people to avoid contributing data to be used
by models that they oppose (because they oppose the impacts of the model
itself, or the values and practices of the organizations operating the
model).

-

Make it easier for people to actively and intentionally
contribute data to be used by models they support. In the very short
term, I think creating more concrete standards around how we share our
impressive or disturbing ChatGPT experiences would be a good start
(right now, the practice of sharing mainly screenshots means OpenAI will
benefit heavily from this sharing but other researchers may struggle to
use any of this data).

-

In the long-term, consider if we need some kind of formal
profit-sharing approach, i.e. a "data dividend". This will
become more urgent the more that ChatGPT (and its children, friends,
competitors, etc.) is monetized. There is fairly coherent argument that
humanity, broadly construed, is a co-creator of each of these models,
and that we might want to take active effort to ensure the economic
winnings are broadly shared.

Even if we don't implement a direct profit sharing model, we'll
likely want to make the governance approach more transparent. Remember,
there's already voting going on. Reddit votes were used to filter the
training data. The governance structures that shape peer production on
GitHub determined which kinds of code ChatGPT has and has not seen. The
policies around Wikipedia contribution determined which historical facts
ChatGPT knows. Making it easier to opt in and out of contributing data
to language models will make it easier to collectively govern these
models, which I think is a broadly popular idea (and an important step
towards encoding some kind of "justice" into these systems, assuming we
are going to train models on collective output).

(Images in this post: van Goh - Wikimedia
Commons, Always Has Been - Imgflip)

Source revision history

Selected Git commits that changed this source file.

- 9fb4674b8a 2026-07-12 - Migrate blog into digital presence monorepo

Mirror freshness

Maintenance status for tracked full-copy mirrors of this post.

-
Current
substack

mirror 2022-12-04

Baseline from original_url

Source and AT Protocol record

Source path
content/writing/posts/2022-12-04-chatgpt-is-awesome-and-scary-you-deserve-credit.md

AT Protocol URI
at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.document/3mizeeaqjudat

Exact public AT Protocol record cached for the Leaflet/Bluesky-facing copy.

{
"uri": "at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.document/3mizeeaqjudat",
"cid": "bafyreih2kvlnbnrnyryt4grhj6ll5ul4i5cvuoacbxfioxpdvharbiafx4",
"value": {
"path": "/3mizeeaqjudat",
"site": "at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.publication/3lzrsw2kvwc2m",
"$type": "site.standard.document",
"title": "ChatGPT is Awesome and Scary: You Deserve Credit for the Good Parts (and Might Help Fix the Bad Parts)",
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
"$link": "bafkreic6dgndoofuvp42l5v4wgxbhxjw4hqbe2rawuu5xpomttilrjabcq"
},
"mimeType": "image/jpeg",
"size": 865705
},
"aspectRatio": {
"$type": "pub.leaflet.blocks.image#aspectRatio",
"width": 1920,
"height": 1509
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
"byteEnd": 84,
"byteStart": 52
},
"features": [
{
"uri": "https://www.psagroup.org/blogposts/78",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "In the past I've written on the idea that we're all \"Expert Language Model Trainers\". The basic idea: large language models rely on our blog posts, Wikipedia articles, Reddit votes, arXiv papers, and more, so it's very likely that much of the Internet-using population has contributed in some fashion to the training data underlying large language models. Of course, everyone's \"marginal impact\" is small (most models would be nearly unchanged if just one person's data disappeared), but many people are undoubtedly contributors."
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
"byteEnd": 112,
"byteStart": 105
},
"features": [
{
"uri": "https://openai.com/blog/chatgpt/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "In this post, I'm going to trace the dataset breadcrumbs for the impressive (and impressively viral) new ChatGPT from OpenAI. The main goal: to highlight specific ways that Internet users have likely contributed. My agenda here is not detract from the mind boggling accomplishments of the OpenAI team, but rather to highlight the immense amount of upstream human activity and labor upon which these new outputs draw, and to describe how we can lean on this dependency as a force for good. Many people may find ChatGPT scary, but I think taking this data-centric and contribution-centric lens suggests a plausible path for global-scale \"governance\" of ChatGPT and inevitable successors."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "A List of Links"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "To start, here's a list with all the links I'll discuss in this post:"
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
"byteEnd": 21,
"byteStart": 0
},
"features": [
{
"uri": "https://openai.com/blog/chatgpt/%5D",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "The ChatGPT Blog Post | Details about ChatGPT"
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
"byteEnd": 20,
"byteStart": 0
},
"features": [
{
"uri": "https://beta.openai.com/docs/model-index-for-researchers",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "OpenAI's Model Index | Describes the family of \"GPT 3.5\" models, to which ChatGPT belongs"
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
"byteEnd": 21,
"byteStart": 0
},
"features": [
{
"uri": "https://openai.com/blog/instruction-following",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "InstructGPT blog post | Details about building InstructGPT, which ChatGPT follows closely"
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
"byteEnd": 17,
"byteStart": 0
},
"features": [
{
"uri": "https://arxiv.org/abs/2203.02155",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "InstructGPT paper | More details than the blog post"
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
"uri": "https://github.com/openai/following-instructions-human-feedback",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "InstructGPT Model Card | Summary of the training data, and more"
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
"byteStart": 0
},
"features": [
{
"uri": "https://commoncrawl.org/the-data",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "CommonCrawl Data | A key data source"
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
"byteEnd": 7,
"byteStart": 0
},
"features": [
{
"uri": "https://paperswithcode.com/dataset/webtext",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "WebText | Another key data source, leveraging reddit votes"
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
"plaintext": "Starting from the ChatGPT Blog Post"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Now let's walk through the information we have about the data, to make a rough guess about: (1) whether you deserve some credit (admission of editorial bias: I'm inclined to to say \"Yes\"), (2) which data sources are particularly important, and (3) what this means for the impact of AI systems like GPT 3.5 on society."
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
"byteEnd": 295,
"byteStart": 285
},
"features": [
{
"uri": "https://github.com/openai/following-instructions-human-feedback",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 279,
"byteStart": 274
},
"features": [
{
"uri": "https://arxiv.org/abs/2203.02155",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 272,
"byteStart": 263
},
"features": [
{
"uri": "https://openai.com/blog/instruction-following",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 35,
"byteStart": 31
},
"features": [
{
"uri": "https://openai.com/blog/chatgpt",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "We start with the ChatGPT blog post. We learn that the model was trained \"using Reinforcement Learning from Human Feedback (RLHF), using the same methods as InstructGPT, but with slight differences in the data collection setup.\" This points us to the InstructGPT blog post, paper, and model card. The InstructGPT blog post provides more info about how OpenAI was able to solicit valuable human feedback, i.e. get people to share specifically how they feel out GPT responses (we'll return to this, but first we'll focus on the text data)."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "Data Sources in the InstructGPT Model Card"
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
"byteEnd": 267,
"byteStart": 256
},
"features": [
{
"uri": "https://commoncrawl.org/the-data",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 41,
"byteStart": 31
},
"features": [
{
"uri": "https://github.com/openai/following-instructions-human-feedback/blob/main/model-card.md",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Looking now at the InstructGPT model card, we learn that \"InstructGPT models are initialized from GPT-3 models, whose training dataset is composed of text posted to the internet or uploaded to the internet (e.g., books). \" Four specific sources are named: CommonCrawl, Webtext (an expanded version), two internet-based book corpora (one which is perhaps BookCorpus), and English-language Wikipedia. We also learn that for InstructGPT, just 40 labelers participated (and some unknown number of customers who provided ecologically valid prompts)."
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
"byteEnd": 16,
"byteStart": 4
},
"features": [
{
"uri": "https://commoncrawl.org/the-data/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "The Common Crawl is, in short, almost everything on the Internet that doesn't explicitly ask to not be scraped (via a robots.txt file). OK, so if you've posted text to the Internet, you may have already contributed. We also learn from the model card that this corpus was \"filtered based on similarity to high-quality reference corpora\", so whoever contributed high-quality content to said reference corpora is likely playing an amplified role. Unfortunately, we can't be sure yet exactly what this high-quality reference corpora looks like (but might guess it's something like news articles, scientific articles, etc.) This also means if contributions to the Common Crawl were deemed low-quality, those contributions may not have made it into ChatGPT."
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
"byteEnd": 111,
"byteStart": 89
},
"features": [
{
"uri": "https://commoncrawl.github.io/cc-crawl-statistics/plots/domains",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "If you're curious about what's specifically in the Common Crawl, the operators provide a list of common domains. A quick glance shows quite a few opportunities for user-generated content (i.e., your contributions): blogpost, wordpress, pinterest, stackexchange, github, youtube, etc. Of course, there's a ton of wiki projects, and a lot of \".edu\" domains corresponding to university webpages. If anyone is aware of more tools for web users to explore Common Crawl and their contributions to it, please do share and I'll be sure to update this section here."
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
"byteEnd": 121,
"byteStart": 116
},
"features": [
{
"uri": "https://aclanthology.org/2021.acl-short.24.pdf",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "It's also important to note that Common Crawl has been shown to have quite a bit of \"undesirable content\" (see this paper from Luccioni and Vivianio). This is certainly true of the other data sources we'll describe as well!"
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
"byteEnd": 49,
"byteStart": 45
},
"features": [
{
"uri": "https://paperswithcode.com/dataset/webtext",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Next, we have the WebText dataset (described here). OpenAI wanted another \"filtered\" version of the web, so they grabbed the content from every webpage posted to Reddit with 3 or more \"karma\" points. In other words, Reddit users voted on the training data to be included. This means even if you've never written a single sentence of text on the web, but you have voted (up or down) on Reddit, you contributed to what we might call a \"collective intelligence\" process for making GPT's data high quality."
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
"byteStart": 208
},
"features": [
{
"uri": "https://pile.eleuther.ai/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 100,
"byteStart": 82
},
"features": [
{
"uri": "https://github.com/jcpeterson/openwebtext",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Webtext is not available for direct download, but it was replicated as part of an open source effort. It's also worth noting that if you want an open dataset along these lines, one of the best choices may be The Pile from EleutherAI."
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
"byteEnd": 138,
"byteStart": 128
},
"features": [
{
"uri": "https://towardsdatascience.com/dirty-secrets-of-bookcorpus-a-key-dataset-in-machine-learning-6ee2927e8650",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "The third source mentioned in the InstructGPT model card is the combination of \"two internet-based book corpora\". This could be BookCorpus, a popular dataset of books from smashbooks.com. It could also be books from Google Books, from Project Gutenberg, or something else. Looking back to the GPT3 paper, we see these datasets described as \"books1\" (12 billion tokens) and \"books2\" (55 billion tokens)."
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
"byteStart": 274
},
"features": [
{
"uri": "https://github.com/nickmvincent/UGCValueRoundup/blob/main/wikipedia.md",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Finally, the fourth -- and perhaps least surprising -- example in the model card is English-language Wikipedia. Much of my doctoral research has discussed how Wikipedia is one of the most important training sources for data-dependent computing in general (see some examples here). Another interesting note from the GPT3 paper is that Wikipedia is intentionally \"over-weighted\": all the content in English Wikipedia was seen 3.4 times during training whereas some of the filtered Common Crawl was skipped entirely."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "To summarize so far, if you have: written any high quality text that appeared in the Common Crawl, submitted to Reddit, voted on a link submitted to Reddit, written a book, or edited English Wikipedia, you're almost certainly a contributor to ChatGPT."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "Other Info"
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
"byteEnd": 70,
"byteStart": 65
},
"features": [
{
"uri": "https://twitter.com/elonmusk/status/1599291104687374338",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "We have one other surprising claim about ChatGPT's training... a tweet from Elon Musk. Here's the text for posterity:"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "\"Not surprising, as I just learned that OpenAI had access to Twitter database for training. I put that on pause for now. Need to understand more about governance structure & revenue plans going forward. OpenAI was started as open-source & non-profit. Neither are still true.\""
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "This suggests yet another avenue for you to have contributed: if you've ever posted any tweets."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "About that Human Feedback"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Returning to the ChatGPT blog post, we know a key unique advantage of ChatGPT is access to data produced by first asking people to produce \"conversations in which they played both sides—the user and an AI assistant\", training an initial model, and then asking AI trainers to compare different chatbot outputs and rank them. In other words these AI trainers were acting as a kind of movie critic for the AI. We could even say these AI trainers were acting like ChatGPT's university-level film studies professor."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "You're an AI trainer too -- just more similar to ChatGPT's high school writing teacher (if you've written a few blog posts), history teacher (if you've edited some Wikipedia articles), or pop culture tutor (if you've upvoted submissions on reddit about popular media or been active on Twitter). An understanding of writing, history, and pop culture is critical to even take the film studies class that the trainers working directly with OpenAI provided (and if you're not a fan of film, this whole analogy can work for something like electrical engineering as well)."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "Implications"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "So, if you've made it this far, maybe I've convinced you to give yourself a pat on the back (and to tell your friends and family they deserve a pat on the back, too). What do we do with this argument?"
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
"byteEnd": 66,
"byteStart": 51
},
"features": [
{
"uri": "https://dl.acm.org/doi/10.1145/3442188.3445885",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "My main line of research is concerned with idea of \"data leverage\": that when data-dependent systems rely on contributions from broad swathes of the public, this creates a potential opportunity for the public to exert leverage through these data dependencies, and participate in the governance of these systems. In other words, by (collectively) threatening to withhold data from organizations you oppose, or give data to organizations you support, you can shift the balance towards AI being used in a way that aligns with your values."
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
"byteEnd": 169,
"byteStart": 135
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
"byteEnd": 67,
"byteStart": 62
},
"features": [
{
"uri": "https://dl.acm.org/doi/10.1145/3449177",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "A key finding from our research (see e.g. simulations in this paper of different kinds of data-related collective action) is that this only works if done collaboratively -- we need collective action."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "If you use ChatGPT heavily, you will very likely make even more contributions to the next version of GPT. You might be able to help address the errors and failure modes users have already identified (and indeed, if you've helped shared a viral error on Twitter, you may have already helped OpenAI deploy a hotfix)."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "On the other hand, if you hate ChatGPT and its ilk, you may find it hard to avoid contributing. There are so many avenues through which your data contributions may end up in the next massive training set. In this case, the best avenue may be to push for updated regulation around large language models. Of course, you could also start \"poisoning\" the text you post to the web, but this can be a tough call to make because it will also hurt anyone trying to compete with GPT-4 and beyond."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Based on the framework of data leverage, I personally think we can focus our efforts along three lines:"
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
"plaintext": "Make it easier for people to avoid contributing data to be used by models that they oppose (because they oppose the impacts of the model itself, or the values and practices of the organizations operating the model)."
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Make it easier for people to actively and intentionally contribute data to be used by models they support. In the very short term, I think creating more concrete standards around how we share our impressive or disturbing ChatGPT experiences would be a good start (right now, the practice of sharing mainly screenshots means OpenAI will benefit heavily from this sharing but other researchers may struggle to use any of this data)."
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
"byteEnd": 105,
"byteStart": 90
},
"features": [
{
"uri": "https://www.datadividends.org/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "In the long-term, consider if we need some kind of formal profit-sharing approach, i.e. a \"data dividend\". This will become more urgent the more that ChatGPT (and its children, friends, competitors, etc.) is monetized. There is fairly coherent argument that humanity, broadly construed, is a co-creator of each of these models, and that we might want to take active effort to ensure the economic winnings are broadly shared."
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
"plaintext": "Even if we don't implement a direct profit sharing model, we'll likely want to make the governance approach more transparent. Remember, there's already voting going on. Reddit votes were used to filter the training data. The governance structures that shape peer production on GitHub determined which kinds of code ChatGPT has and has not seen. The policies around Wikipedia contribution determined which historical facts ChatGPT knows. Making it easier to opt in and out of contributing data to language models will make it easier to collectively govern these models, which I think is a broadly popular idea (and an important step towards encoding some kind of \"justice\" into these systems, assuming we are going to train models on collective output)."
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
"byteEnd": 76,
"byteStart": 69
},
"features": [
{
"uri": "https://imgflip.com/memegenerator/255177692/astronaut-meme-always-has-been-template",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 49,
"byteStart": 32
},
"features": [
{
"uri": "https://en.wikipedia.org/wiki/Reaper_(Van_Gogh_series)#/media/File:Wheat_Field_with_Reaper_and_Sun_(F617),_1889.jpg",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "(Images in this post: van Goh - Wikimedia Commons, Always Has Been - Imgflip)"
}
}
]
}
]
},
"description": "More on why you're an expert language model trainer",
"publishedAt": "2022-12-04T00:00:00.000Z"
}
}
