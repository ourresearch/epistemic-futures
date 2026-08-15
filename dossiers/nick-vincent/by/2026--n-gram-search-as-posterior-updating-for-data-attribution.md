---
title: "N-gram search as posterior updating for data attribution"
person: "nick-vincent"
section: "by"
type: "blog-post"
year: 2026
date: "2026-05-27"
venue: "Data Leverage (Digital Garden / dataleverage.substack.com)"
authors: "Nicholas Vincent"
source_url: "https://nickmvincent.github.io/short-focus-posts/posterior.html"
retrieved: "2026-08-13"
content: "full-text"
notes: "Dek: A short argument that model outputs and training-data priors can improve rough approximations of data attribution. Garden section: short-focus-posts. Mirrored on the Data Leverage Substack."
---

# N-gram search as posterior updating for data attribution

## Full text

This is a short post on the topic of n-gram search over likely
training data and data attribution more generally. I originally wrote a
version of this on
Twitter in response to a large discussion about using n-gram search
to find specific passages in Internet training data that may "explain"
certain AI outputs.

Many of the proposed responses to AI impacts that touch on data
attribution and/or the flow of economic winnings require us to
assume some kind of quantitative distribution of credit.

Typically, the "credit" construct in these discussions is some kind
of data counterfactual, either a leave-one-out variant or some
Shapley-like aggregate over many combinations of training data. When we
are discussing how to give credit or reward, we typically end up leaning
on some notion of "causal impact" of data.

However, I think almost everyone -- even those who aren't thinking
about the formal training data attribution task at all -- has some
implicit understanding that getting anywhere close to an exact
distribution of credit scores for the training data of large models with
large training sets is extremely hard. So, at the moment, everyone ends
up using simplifying assumptions, and these assumptions are generally
not made explicit.

Furthermore, the definition of credit and causal impact that a given
approach leans on is itself often left implicit. We would almost always
benefit from making it explicit: we should say which specific
counterfactual scenarios we are considering when we try to assign any
kind of "causal" credit. We also must be explicit about how much we want
to connect causal impact and moral desert. One can argue that a document
could have been used heavily in training, and even memorized, without
that implying that that particular document "deserves" a large share of
economic surplus; so making our counterfactual of interest explicit is
very important.

Responses that try to handwave away the whole issue (often arguing
that the whole endeavor of trying to credit training data is pointless)
basically take the stance that we should just assume all data credit
values to be zero and give all the value to the operators of AI systems.
One way we might justify this more formally is to note that the
leave-one-out scores for granular units of data in very large models are
all very, very small. (However, the scores for larger coalitions of data
may not be small at all!) Responses in the general space of UBI/AI
dividends/data dividends basically take the stance that we should use a
kind of uniform approximation -- just give each person or each unit of
training data a value of 1/n.

There are a number of other responses that also have their own
assumptions about implicit value distributions (collective licensing
schemes imply some kind of pooling approximation, some approaches
emphasize retrieval-level influence over training-level, etc.). Will
avoid spelling these out here for the sake of space.

One question that follows -- how good are these approximations, and
how well do they work for driving a specific social outcome (e.g.,
incentivizing paid knowledge work, incentivizing volunteer peer
production)?

And a second question, which connects directly to the debate about
using n-gram search as a proxy for attribution, is this: if we do not
have access to actual training data or information from the actual
training process (e.g., logs of gradient updates), but we do have
information about the output of a model (for instance, the fact that a
model produced a sequence that has only appeared in one niche blog)
combined with industry-wide assumptions about the model (for instance,
an assumption that every frontier model is assumed to have seen some
variant of Common Crawl during pretraining), can we use that information
in any way to get a better approximation than "assume all data values
are zero" or "assume all data values are 1/n"?

I think it will be valuable to more formally connect things like
n-gram search approaches to membership inference and sequence-level
training data attribution.

One conceptual approach here is to think of the high-level process as
trying to improve a posterior (I hope to write something longer on this
front; if you've seen anything along these lines, please let me
know).

But in the meantime, unless somebody offers a better set of data
values (for instance, if an AI operator offers access to direct data
attribution scores for their model), I think it likely is the case that
using some information about model outputs will give us
a "directionally better" approximation than all-zero or 1/n.

(More formally, I think the error of our approximate data value
distribution will on average go down!)

And again, without full data access or direct access to data
attribution, what we should do pragmatically right now is to aggregate
across any information we can get (whether that's n-gram search and
membership inference or tacit community knowledge like "everybody uses
Common Crawl" or "everybody used to use book torrents") to try to do
better than a 1/n approximation or an all-zero approximation.

Source revision history

Selected Git commits that changed this source file.

- 0b5f434e56 2026-08-03 - Polish published short posts

- d96a1e08ab 2026-08-03 - Revise drafts on evaluation debt and replacing actions

- b7cec01ae6 2026-07-16 - Refresh site and organize writing

- 9fb4674b8a 2026-07-12 - Migrate blog into digital presence monorepo

Source and AT Protocol record

Source path
content/writing/short-posts/2026-05-27-short--ngrams-and-posteriors.md

AT Protocol URI
at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.document/3mni4cwhlhvx3

Local AT Protocol-shaped preview used to inspect the record before an exact public cache is refreshed.

{
"note": "Local AT Protocol-shaped preview. Run `make garden-refresh-atproto` to cache exact public records where available.",
"sourcePath": "content/writing/short-posts/2026-05-27-short--ngrams-and-posteriors.md",
"uri": "at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.document/3mni4cwhlhvx3",
"value": {
"$type": "site.standard.document",
"title": "N-gram search as posterior updating for data attribution",
"description": "A short argument that model outputs and training-data priors can improve rough approximations of data attribution.",
"publishedAt": "2026-05-27",
"site": "at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.publication/3mmpcciuaj22a",
"content": {
"$type": "at.markpub.markdown",
"text": "This is a short post on the topic of n-gram search over likely training data and data attribution more generally. I originally wrote a version of this [on Twitter](https://x.com/nickmvincent/status/2058242437949333584) in response to a large discussion about using n-gram search to find specific passages in Internet training data that may \"explain\" certain AI outputs.\n\n---\n\nMany of the proposed responses to AI impacts that touch on data attribution and/or the flow of economic winnings *require* us to assume some kind of quantitative distribution of credit.\n\nTypically, the \"credit\" construct in these discussions is some kind of data counterfactual, either a leave-one-out variant or some Shapley-like aggregate over many combinations of training data. When we are discussing how to give credit or reward, we typically end up leaning on some notion of \"causal impact\" of data.\n\nHowever, I think almost everyone -- even those who aren't thinking about the formal training data attribution task at all -- has some implicit understanding that getting anywhere close to an exact distribution of credit scores for the training data of large models with large training sets is extremely hard. So, at the moment, everyone ends up using simplifying assumptions, and these assumptions are generally not made explicit.\n\nFurthermore, the definition of credit and causal impact that a given approach leans on is itself often left implicit. We would almost always benefit from making it explicit: we should say which specific counterfactual scenarios we are considering when we try to assign any kind of \"causal\" credit. We also must be explicit about how much we want to connect causal impact and moral desert. One can argue that a document could have been used heavily in training, and even memorized, without that implying that that particular document \"deserves\" a large share of economic surplus; so making our counterfactual of interest explicit is very important.\n\nResponses that try to handwave away the whole issue (often arguing that the whole endeavor of trying to credit training data is pointless) basically take the stance that we should just assume all data credit values to be zero and give all the value to the operators of AI systems. One way we might justify this more formally is to note that the leave-one-out scores for granular units of data in very large models are all very, very small. (However, the scores for larger coalitions of data may not be small at all!) Responses in the general space of UBI/AI dividends/data dividends basically take the stance that we should use a kind of uniform approximation -- just give each person or each unit of training data a value of 1/n.\n\nThere are a number of other responses that also have their own assumptions about implicit value distributions (collective licensing schemes imply some kind of pooling approximation, some approaches emphasize retrieval-level influence over training-level, etc.). Will avoid spelling these out here for the sake of space.\n\nOne question that follows -- how good are these approximations, and how well do they work for driving a specific social outcome (e.g., incentivizing paid knowledge work, incentivizing volunteer peer production)?\n\nAnd a second question, which connects directly to the debate about using n-gram search as a proxy for attribution, is this: if we do not have access to actual training data or information from the actual training process (e.g., logs of gradient updates), but we do have information about the output of a model (for instance, the fact that a model produced a sequence that has only appeared in one niche blog) combined with industry-wide assumptions about the model (for instance, an assumption that every frontier model is assumed to have seen some variant of Common Crawl during pretraining), can we use that information in any way to get a better approximation than \"assume all data values are zero\" or \"assume all data values are 1/n\"?\n\nI think it will be valuable to more formally connect things like n-gram search approaches to membership inference and sequence-level training data attribution.\n\nOne conceptual approach here is to think of the high-level process as trying to improve a posterior (I hope to write something longer on this front; if you've seen anything along these lines, please let me know).\n\nBut in the meantime, unless somebody offers a better set of data values (for instance, if an AI operator offers access to direct data attribution scores for their model), I think it likely is the case that using some information about model outputs **will** give us a \"directionally better\" approximation than all-zero or 1/n.\n\n(More formally, I think the error of our approximate data value distribution will on average go down!)\n\nAnd again, without full data access or direct access to data attribution, what we should do pragmatically right now is to aggregate across any information we can get (whether that's n-gram search and membership inference or tacit community knowledge like \"everybody uses Common Crawl\" or \"everybody used to use book torrents\") to try to do better than a 1/n approximation or an all-zero approximation.\n"
}
}
}
