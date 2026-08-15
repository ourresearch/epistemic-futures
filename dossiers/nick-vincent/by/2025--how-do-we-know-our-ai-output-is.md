---
title: "How do we know our AI output is good? Double checks, bar charts, vibes, and training data."
person: "nick-vincent"
section: "by"
type: "blog-post"
year: 2025
date: "2025-05-30"
venue: "Data Leverage (Digital Garden / dataleverage.substack.com)"
authors: "Nicholas Vincent"
source_url: "https://nickmvincent.github.io/long-posts/how-do-we-know-our-ai-output-is-good.html"
retrieved: "2026-08-13"
content: "full-text"
notes: "Dek: Connecting evaluation and dataset documentation via the lens of \"AI as ranking\". Garden section: long-posts. Mirrored on the Data Leverage Substack."
---

# How do we know our AI output is good? Double checks, bar charts, vibes, and training data.

## Full text

Coupling in train brakes. Wikimedia
Commons.

Having argued that it’s useful to view many types of AI systems
through the lens of ranking previous bundles and chunks of
human-recorded information (post
1, post
2), we now turn to some intersections between this framing and the
evaluation of AI products.

In this post, we’ll discuss the current challenges with evaluating AI
(much ink has already
been spilled)
and then link these challenges back to the topics of dataset
documentation and data leverage.

Imagine you’ve just asked ChatGPT/Claude/Gemini/Copilot/Deepseek some
questions. Perhaps they were like one of these prompts:

-

Tell me about some influential advisors who played major roles in
various civilizations during the ancient history period.

-

What is the most effective approach to reduce ulnar wrist
pain?

-

What is the most famous restaurant in Chicago?

For each of these types of questions (and many more), each major
commercial AI product will now give you a great-looking answer. Having
hand-picked these examples and tried them out, I can also say the
quality of these specific answers are decent. If we buy the arguments
from previous posts, we might view these answers as “ranked chunks” of
prior human records (and if we use a web search enabled AI products, we
might also get some ranked bundles).

But we’re still left with quite a few questions. Are the answers all
equally good? Which specific answers are good? Which model is best?
(Again: these questions are not new, have been hotly discussed and
debated, and presumably every major lab is fervently trying to answer
these internally).

To answer these questions as a user, we actually have a few options!
If we want to be very principled about our epistemics, then we might
want to do something like create a comprehensive and systematic test
bank (our own personalized “benchmark”, like “Humanity’s Last Exam”) and evaluate each
model. But maybe we just want to be pragmatic consumers who don’t spend
a lot of time thinking about these issues (so we just go with our gut),
or maybe we want to find some middle ground (do some double checks, but
only here and there?).

### ChatGPT can make
mistakes. Check important info.

First, we might check what the AI “says on the box”. Do these systems
even claim to be accurate? Do they tell us about their confidence in a
given answer? ChatGPT says: “ChatGPT can make mistakes. Check important
info.” Gemini says “Gemini can make mistakes, so double-check it”.
Claude says something similar, and links to a dedicated help
page.

So, officially speaking, any time we make an AI query, we should be
double-checking it. This seems to be great — if we follow the
instructions to the letter, we’ll naturally calculate our own internal
accuracy scores for these products. We can simply subscribe to all the
AI products, keep score as instructed for a month or so, and then we’ll
know what’s best.

But in practice, it’s not so simple. First of all, it seems
enormously unlikely that people will actually do this (nice example: database of
hallucinated references in law). Some people might even start to wonder:
“If I need to double check every response, what am I paying tens or
hundreds of dollars a month for?” There is some interesting “data napkin
math” to be done here about how long double checks actually take, how
people value their time and value AI products, and so on.

Further, it’s unclear in the current interfaces what specific steps
the user is meant to take to perform a “double check”. Are we pasting
the query into Google (which might give us another AI overview)? Or, are
we meant to find and read a primary source that gets at the core of our
informational query? Presumably, the intended interpretation is closer
to this. For some fraction of all our queries to AI, we should also be
reading from academic journals and newspapers (which is not totally
unreasonable with current products1, and could
even be enforced or more strongly promoted2).

The process of “double checking” is also a reminder of what most AI
systems are currently doing: delivering us information (to check an
answer, we probably need to get more information via some other
pathway).

Double checking my ChatGPT response…

### Bar charts and Vibes

So, every AI tool tells us to double check things, but none of the
major AI products (to my knowledge) are actually taking this very
seriously in terms of enforcement or norm setting (not to say it’s an
easy problem: again, I don’t think paying consumers will react well to a
pop-up that says “Hey, it looks like you haven’t done any
double-checking labour in past few hours. Get to work!”).

So what are people using to make their decisions in practice? Two
options are (1) the bar charts (and other summaries) that labs are
putting out alongside model releases to summarize performance across
different domains and (2) vibes from social media, word of mouth, brand
recognition, and related factors.

From https://openai.com/index/introducing-o3-and-o4-mini/

My guess is the latter constellation (vibes/word of mouth/brand) is
currently more influential: I think right now, tweets about how “Claude
is the best for coding!”, or “Gemini’s context window is so good!” are
playing a larger role than benchmark bar charts or Chatbot Arena scores
(which have recently come under some
fire). Ultimately, ChatGPT remains dominant in market share, and there’s
a strong argument to be made that is in large part based on early brand
value creation and word of mouth, and benchmarks have thus far had very
little impact on market share stats.

Again, while not perhaps ideal, this all makes sense from a pragmatic
perspective. As we discussed in the Eval
Data Leverage post, there simply hasn’t been enough time for most
users to fully assess these new models across the breadth of possible
use cases, so we have to go off something like bar charts or vibes.

### Dataset details as quality
signals

Of course this was going to circle back to data. In “Selling
AGI like AG1: Will Consumers Push Back Against Proprietary Blends of
Herbs and of Data?”, I made the case that perhaps down the line,
dataset information will actually become an important signal for
consumers.

Concretely, I think that it might become compelling to advertise an
AI product with some messaging around “we got 10,000 hours of labour
from scientific experts that went into post-training and evaluation”.
This would be a proxy for “model will perform well on scientific tasks”.
In other words, it would be aiming to communicate the same thing as a
benchmark bar chart saying “Look, our model is really good at science”.
But, if consumers don’t understand or trust the process by which the bar
chart was constructed, details about the data might be compelling.

To be clear, ideally we’d want both: transparency in data and
transparency in evals. But at the end of the day, these two things
should be highly related. While of course there are situations where a
model could have lots of data from domain X but do bad on a benchmark
from that domain, or it could be the case that a model could do well on
a benchmark without much data from the domain, in general we’d
expect tight coupling between training choices and evaluation
performance, because that’s what statistical learning underlying
these technologies is trying to achieve.

Hence, if we conduct a dataset documentation effort aimed at estimating
the prevalence of a group of people’s contribution to a training
dataset, we might expect that measure (which we could call something
like “estimated intellectual property dispossession” — a concept that
certainly makes some normative claims but is distinct from actual legal
outcomes re: IP and AI) to tell us about how likely that group is to be
affected by AI-based substitution.

### Approaches for
measuring this tight coupling

There are a number of technical approaches for understanding the
coupling between model inputs and outputs. One specific field of
research we could look to that helps concretize this is work on
“membership inference attacks”. To quote Hayes et al. in recent work
on the topic, an MIA is when “an adversary aims to determine whether a
specific data record was part of a model’s training set”. In short,
these attacks work well against small models, but computational
challenges make it hard to use MIAs against larger models; the work from
Hayes et al. shows it is still possible to conduct such attacks, with
nuances.

Membership inference gives us one lens to quantify the connection
between AI inputs and outputs. Other related frames include training
data extraction, memorization, and
even differential
privacy. But even relatively straightforward benchmarks that are
grouped by topic or domain should point us on the right track of
guessing, in general, what was in the training data.

Update Jun 20, 2025: see also work such as “Approximating
Language Model Training Data from Weights” from Morris et al.

### Tying this
back to AI utility and acts of ranking

So, finally, having walked through double checks, bar charts, vibes,
and the coupling between training data and model outputs, I want make an
argument connecting this discussion to the idea that “Each
Instance of "AI Utility" stems from some human act(s) of information
recording and ranking”.

Both search results and AI answers are useful because some human
somewhere recorded information. All these tools are competing to deliver
us bundles or remixed chunks of information — which is hard, we have
limited attention! (And critically, this means that of course tech and
AI companies are providing lots of value; the original value of an AI
output can be traced to human records, but the ranking is critical
too).

We might even go a step further and say that each AI output actually
represents some weighted combination of every possible chunk of
information that’s out there. And when we use AI models, we’re making
our decision through either formal or informal feedback about whether
the weighted combination of chunks of information we got met our needs
(and could have met our needs even better).

A variety of implications:

-

For dataset documentation: This all makes the documentation of
training (including post-training!) data all the more important. If each
question we pose to ChatGPT is fundamentally a request to rank all the
information available to the system — in both chunks and in bundles —
and deliver us some weighted combination of information that we will use
to act, we probably really want to know about the
upstream information.

-

For AI Social Simulations: Authors have argued in favour of using LLMs for
social simulation (and other authors have raised serious concerns).
The ranking-data-labour framing can be further clarifying when we think
about things like AI social simulations: a simulation of people using
LLMs to take actions could have real epistemic value if the ranking
system delivers information that’s derived from real people in relevant
situations. But, there will always be many ways that a model might
deliver us information that has a neutral or harmful effect on the
overall utility we get out of said simulation.

- Dataset documentation would really help here!

-

For decision making more generally: The ranking framing can also
be helpful for thinking about the morality of using AI in any given
decision process (which has received substantial attention over
the years). If a person
makes the decision on their own, they incorporate various information
that's stored in their brain, or that is otherwise available to them. AI
models make different information available, but there are many ways
that this additional information could be unjust or harmful.

- Again, this suggests that if we use AI for decision making, a deep
understanding of both the training data and summarized evals would be
extremely helpful.

At the end of the day, as AI gets rolled out more widely in society,
we’re collectively going to be running more computations in which we
“assign weights” over all the information that humans have ever put into
our records. We’re going to want to understand what’s being weighted,
whether through systematic evaluation, systematic dataset documentation,
or some combination of the two (and perhaps also systematic inspection
of model internals!).

When we’re designing AI products, grand “public AI” proposals, or
schemes for new data markets or collective bargaining apparatuses, this
framing can (I believe) help us do a better job about reasoning about
how and when to use AI.

1

As more tools incorporate heavy use of search and links, I do think
it’s getting more reasonable to check things. Personally, I do actually
find myself actually clicking links provided by o3 and Gemini 2.5 and
generally finding the experience reasonable and useful. In particular, I
think using o3 in conjunction with web search and scholarly search
engines is extremely useful! But I think there’s still going to be a lot
of resistance to checking things often and the “logically extreme
interpretation” — that people are going to double check every “important
query” to the product they’re paying hundreds of dollars a month for —
is a bit absurd.

2

It could be interesting to imagine an “AI” tool which does actually
expect and/or enforce that users do fact verification at some regular
interval (and perhaps every user is explicitly conscripted into some
kind of knowledge maintenance project). But such tools would not be
marketed, or priced, the way that current offerings are.

Source revision history

Selected Git commits that changed this source file.

- 9fb4674b8a 2026-07-12 - Migrate blog into digital presence monorepo

Mirror freshness

Maintenance status for tracked full-copy mirrors of this post.

-
Current
substack

mirror 2025-05-30

Baseline from original_url

Source and AT Protocol record

Source path
content/writing/posts/2025-05-30-how-do-we-know-our-ai-output-is-good.md

AT Protocol URI
at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.document/3mizeelhr55ra

Exact public AT Protocol record cached for the Leaflet/Bluesky-facing copy.

{
"uri": "at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.document/3mizeelhr55ra",
"cid": "bafyreihy5lpk45xxoivmh2rbymvs4i3sd2kj3q4xnyisoxi3hycn3dhveu",
"value": {
"path": "/3mizeelhr55ra",
"site": "at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.publication/3lzrsw2kvwc2m",
"$type": "site.standard.document",
"title": "How do we know our AI output is good? Double checks, bar charts, vibes, and training data.",
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
"$link": "bafkreibqctcuvafop2jgnhzh3cnsg2iexfk6cuuelkdql7thgv3tadnqbu"
},
"mimeType": "image/jpeg",
"size": 161754
},
"aspectRatio": {
"$type": "pub.leaflet.blocks.image#aspectRatio",
"width": 960,
"height": 509
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
"byteEnd": 44,
"byteStart": 26
},
"features": [
{
"uri": "https://commons.wikimedia.org/wiki/File:Operation_of_trains_and_station_work_and_telegraphy_(1914)_(14737911176).jpg",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Coupling in train brakes. Wikimedia Commons."
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
"byteEnd": 167,
"byteStart": 161
},
"features": [
{
"uri": "https://dataleverage.substack.com/p/each-instance-of-ai-utility-stems",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 159,
"byteStart": 153
},
"features": [
{
"uri": "https://dataleverage.substack.com/p/google-and-tiktok-rank-bundles-of",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Having argued that it’s useful to view many types of AI systems through the lens of ranking previous bundles and chunks of human-recorded information (post 1, post 2), we now turn to some intersections between this framing and the evaluation of AI products."
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
"byteEnd": 106,
"byteStart": 99
},
"features": [
{
"uri": "https://simonwillison.net/2025/Apr/30/criticism-of-the-chatbot-arena/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 98,
"byteStart": 94
},
"features": [
{
"uri": "https://arxiv.org/abs/2504.20879",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 93,
"byteStart": 86
},
"features": [
{
"uri": "https://arxiv.org/abs/2502.06559v1",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "In this post, we’ll discuss the current challenges with evaluating AI (much ink has already been spilled) and then link these challenges back to the topics of dataset documentation and data leverage."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Imagine you’ve just asked ChatGPT/Claude/Gemini/Copilot/Deepseek some questions. Perhaps they were like one of these prompts:"
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
"plaintext": "Tell me about some influential advisors who played major roles in various civilizations during the ancient history period."
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "What is the most effective approach to reduce ulnar wrist pain?"
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "What is the most famous restaurant in Chicago?"
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
"plaintext": "For each of these types of questions (and many more), each major commercial AI product will now give you a great-looking answer. Having hand-picked these examples and tried them out, I can also say the quality of these specific answers are decent. If we buy the arguments from previous posts, we might view these answers as “ranked chunks” of prior human records (and if we use a web search enabled AI products, we might also get some ranked bundles)."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "But we’re still left with quite a few questions. Are the answers all equally good? Which specific answers are good? Which model is best? (Again: these questions are not new, have been hotly discussed and debated, and presumably every major lab is fervently trying to answer these internally)."
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
"byteEnd": 281,
"byteStart": 259
},
"features": [
{
"uri": "https://agi.safe.ai/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "To answer these questions as a user, we actually have a few options! If we want to be very principled about our epistemics, then we might want to do something like create a comprehensive and systematic test bank (our own personalized “benchmark”, like “Humanity’s Last Exam”) and evaluate each model. But maybe we just want to be pragmatic consumers who don’t spend a lot of time thinking about these issues (so we just go with our gut), or maybe we want to find some middle ground (do some double checks, but only here and there?)."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "ChatGPT can make mistakes. Check important info."
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
"byteEnd": 357,
"byteStart": 348
},
"features": [
{
"uri": "https://support.anthropic.com/en/articles/8525154-claude-is-providing-incorrect-or-misleading-responses-what-s-going-on",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "First, we might check what the AI “says on the box”. Do these systems even claim to be accurate? Do they tell us about their confidence in a given answer? ChatGPT says: “ChatGPT can make mistakes. Check important info.” Gemini says “Gemini can make mistakes, so double-check it”. Claude says something similar, and links to a dedicated help page."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "So, officially speaking, any time we make an AI query, we should be double-checking it. This seems to be great — if we follow the instructions to the letter, we’ll naturally calculate our own internal accuracy scores for these products. We can simply subscribe to all the AI products, keep score as instructed for a month or so, and then we’ll know what’s best."
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
"byteEnd": 139,
"byteStart": 131
},
"features": [
{
"uri": "https://www.polarislab.org/ai-law-tracker.html",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "But in practice, it’s not so simple. First of all, it seems enormously unlikely that people will actually do this (nice example: database of hallucinated references in law). Some people might even start to wonder: “If I need to double check every response, what am I paying tens or hundreds of dollars a month for?” There is some interesting “data napkin math” to be done here about how long double checks actually take, how people value their time and value AI products, and so on."
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
"byteEnd": 589,
"byteStart": 588
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
"byteEnd": 534,
"byteStart": 533
},
"features": [
{
"uri": "#footnote-1",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Further, it’s unclear in the current interfaces what specific steps the user is meant to take to perform a “double check”. Are we pasting the query into Google (which might give us another AI overview)? Or, are we meant to find and read a primary source that gets at the core of our informational query? Presumably, the intended interpretation is closer to this. For some fraction of all our queries to AI, we should also be reading from academic journals and newspapers (which is not totally unreasonable with current products1, and could even be enforced or more strongly promoted2)."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "The process of “double checking” is also a reminder of what most AI systems are currently doing: delivering us information (to check an answer, we probably need to get more information via some other pathway)."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Double checking my ChatGPT response…"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "Bar charts and Vibes"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "So, every AI tool tells us to double check things, but none of the major AI products (to my knowledge) are actually taking this very seriously in terms of enforcement or norm setting (not to say it’s an easy problem: again, I don’t think paying consumers will react well to a pop-up that says “Hey, it looks like you haven’t done any double-checking labour in past few hours. Get to work!”)."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "So what are people using to make their decisions in practice? Two options are (1) the bar charts (and other summaries) that labs are putting out alongside model releases to summarize performance across different domains and (2) vibes from social media, word of mouth, brand recognition, and related factors."
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
"byteEnd": 57,
"byteStart": 5
},
"features": [
{
"uri": "https://openai.com/index/introducing-o3-and-o4-mini/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "From https://openai.com/index/introducing-o3-and-o4-mini/"
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
"byteStart": 325
},
"features": [
{
"uri": "https://simonwillison.net/2025/Apr/30/criticism-of-the-chatbot-arena/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "My guess is the latter constellation (vibes/word of mouth/brand) is currently more influential: I think right now, tweets about how “Claude is the best for coding!”, or “Gemini’s context window is so good!” are playing a larger role than benchmark bar charts or Chatbot Arena scores (which have recently come under some fire). Ultimately, ChatGPT remains dominant in market share, and there’s a strong argument to be made that is in large part based on early brand value creation and word of mouth, and benchmarks have thus far had very little impact on market share stats."
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
"byteStart": 106
},
"features": [
{
"uri": "https://dataleverage.substack.com/p/evaluation-data-leverage-advances",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Again, while not perhaps ideal, this all makes sense from a pragmatic perspective. As we discussed in the Eval Data Leverage post, there simply hasn’t been enough time for most users to fully assess these new models across the breadth of possible use cases, so we have to go off something like bar charts or vibes."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "Dataset details as quality signals"
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
"byteEnd": 150,
"byteStart": 55
},
"features": [
{
"uri": "https://dataleverage.substack.com/p/selling-agi-like-ag1-will-the-market",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Of course this was going to circle back to data. In “Selling AGI like AG1: Will Consumers Push Back Against Proprietary Blends of Herbs and of Data?”, I made the case that perhaps down the line, dataset information will actually become an important signal for consumers."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Concretely, I think that it might become compelling to advertise an AI product with some messaging around “we got 10,000 hours of labour from scientific experts that went into post-training and evaluation”. This would be a proxy for “model will perform well on scientific tasks”. In other words, it would be aiming to communicate the same thing as a benchmark bar chart saying “Look, our model is really good at science”. But, if consumers don’t understand or trust the process by which the bar chart was constructed, details about the data might be compelling."
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
"byteEnd": 577,
"byteStart": 492
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
"byteEnd": 401,
"byteStart": 391
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "To be clear, ideally we’d want both: transparency in data and transparency in evals. But at the end of the day, these two things should be highly related. While of course there are situations where a model could have lots of data from domain X but do bad on a benchmark from that domain, or it could be the case that a model could do well on a benchmark without much data from the domain, in general we’d expect tight coupling between training choices and evaluation performance, because that’s what statistical learning underlying these technologies is trying to achieve."
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
"byteEnd": 51,
"byteStart": 45
},
"features": [
{
"uri": "https://arxiv.org/abs/2403.13073",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Hence, if we conduct a dataset documentation effort aimed at estimating the prevalence of a group of people’s contribution to a training dataset, we might expect that measure (which we could call something like “estimated intellectual property dispossession” — a concept that certainly makes some normative claims but is distinct from actual legal outcomes re: IP and AI) to tell us about how likely that group is to be affected by AI-based substitution."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "Approaches for measuring this tight coupling"
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
"byteStart": 239
},
"features": [
{
"uri": "https://arxiv.org/abs/2505.18773",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "There are a number of technical approaches for understanding the coupling between model inputs and outputs. One specific field of research we could look to that helps concretize this is work on “membership inference attacks”. To quote Hayes et al. in recent work on the topic, an MIA is when “an adversary aims to determine whether a specific data record was part of a model’s training set”. In short, these attacks work well against small models, but computational challenges make it hard to use MIAs against larger models; the work from Hayes et al. shows it is still possible to conduct such attacks, with nuances."
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
"byteEnd": 195,
"byteStart": 175
},
"features": [
{
"uri": "https://www.nowpublishers.com/article/Details/TCS-042",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 164,
"byteStart": 152
},
"features": [
{
"uri": "https://openreview.net/forum?id=TatRHT_1cK",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 150,
"byteStart": 126
},
"features": [
{
"uri": "https://www.usenix.org/conference/usenixsecurity21/presentation/carlini-extracting",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Membership inference gives us one lens to quantify the connection between AI inputs and outputs. Other related frames include training data extraction, memorization, and even differential privacy. But even relatively straightforward benchmarks that are grouped by topic or domain should point us on the right track of guessing, in general, what was in the training data."
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
"byteStart": 30
},
"features": [
{
"uri": "https://arxiv.org/abs/2506.15553",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Update Jun 20, 2025: see also work such as “Approximating Language Model Training Data from Weights” from Morris et al."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "Tying this back to AI utility and acts of ranking"
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
"byteEnd": 293,
"byteStart": 198
},
"features": [
{
"uri": "https://dataleverage.substack.com/p/each-instance-of-ai-utility-stems",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "So, finally, having walked through double checks, bar charts, vibes, and the coupling between training data and model outputs, I want make an argument connecting this discussion to the idea that “Each Instance of \"AI Utility\" stems from some human act(s) of information recording and ranking”."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Both search results and AI answers are useful because some human somewhere recorded information. All these tools are competing to deliver us bundles or remixed chunks of information — which is hard, we have limited attention! (And critically, this means that of course tech and AI companies are providing lots of value; the original value of an AI output can be traced to human records, but the ranking is critical too)."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "We might even go a step further and say that each AI output actually represents some weighted combination of every possible chunk of information that’s out there. And when we use AI models, we’re making our decision through either formal or informal feedback about whether the weighted combination of chunks of information we got met our needs (and could have met our needs even better)."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "A variety of implications:"
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
"byteEnd": 380,
"byteStart": 374
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#bold"
}
]
}
],
"plaintext": "For dataset documentation: This all makes the documentation of training (including post-training!) data all the more important. If each question we pose to ChatGPT is fundamentally a request to rank all the information available to the system — in both chunks and in bundles — and deliver us some weighted combination of information that we will use to act, we probably really want to know about the upstream information."
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
"byteEnd": 140,
"byteStart": 132
},
"features": [
{
"uri": "https://dl.acm.org/doi/full/10.1145/3613904.3642703",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 56,
"byteStart": 50
},
"features": [
{
"uri": "https://arxiv.org/abs/2504.02234",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "For AI Social Simulations: Authors have argued in favour of using LLMs for social simulation (and other authors have raised serious concerns). The ranking-data-labour framing can be further clarifying when we think about things like AI social simulations: a simulation of people using LLMs to take actions could have real epistemic value if the ranking system delivers information that’s derived from real people in relevant situations. But, there will always be many ways that a model might deliver us information that has a neutral or harmful effect on the overall utility we get out of said simulation."
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
"byteEnd": 200,
"byteStart": 197
},
"features": [
{
"uri": "https://arxiv.org/abs/2005.04176",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 196,
"byteStart": 192
},
"features": [
{
"uri": "https://www.nature.com/articles/s43586-022-00172-0.epdf?sharing_token=20oCMhzni41xvDUut2OItdRgN0jAjWel9jnR3ZoTv0OwjbZm_FCT7gsPxkyDixLb1Sapyw-rKunjdUM-MQsb2Df0fuyC5afG4elbIDnGjYVTr4j3hlrQ7YmaASLl3Q0UKi5thaNq9gvVPV-cT8IZm9wh7kXFdLAzLh60tNgS2gE%3D",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "For decision making more generally: The ranking framing can also be helpful for thinking about the morality of using AI in any given decision process (which has received substantial attention over the years). If a person makes the decision on their own, they incorporate various information that's stored in their brain, or that is otherwise available to them. AI models make different information available, but there are many ways that this additional information could be unjust or harmful."
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
"plaintext": "At the end of the day, as AI gets rolled out more widely in society, we’re collectively going to be running more computations in which we “assign weights” over all the information that humans have ever put into our records. We’re going to want to understand what’s being weighted, whether through systematic evaluation, systematic dataset documentation, or some combination of the two (and perhaps also systematic inspection of model internals!)."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "When we’re designing AI products, grand “public AI” proposals, or schemes for new data markets or collective bargaining apparatuses, this framing can (I believe) help us do a better job about reasoning about how and when to use AI."
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
"plaintext": "As more tools incorporate heavy use of search and links, I do think it’s getting more reasonable to check things. Personally, I do actually find myself actually clicking links provided by o3 and Gemini 2.5 and generally finding the experience reasonable and useful. In particular, I think using o3 in conjunction with web search and scholarly search engines is extremely useful! But I think there’s still going to be a lot of resistance to checking things often and the “logically extreme interpretation” — that people are going to double check every “important query” to the product they’re paying hundreds of dollars a month for — is a bit absurd."
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
"facets": [],
"plaintext": "It could be interesting to imagine an “AI” tool which does actually expect and/or enforce that users do fact verification at some regular interval (and perhaps every user is explicitly conscripted into some kind of knowledge maintenance project). But such tools would not be marketed, or priced, the way that current offerings are."
}
}
]
}
]
},
"description": "Connecting evaluation and dataset documentation via the lens of \"AI as ranking\".",
"publishedAt": "2025-05-30T00:00:00.000Z"
}
}
