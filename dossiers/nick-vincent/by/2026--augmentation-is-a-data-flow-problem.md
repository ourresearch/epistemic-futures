---
title: "Augmentation is a data flow problem"
person: "nick-vincent"
section: "by"
type: "blog-post"
year: 2026
date: "2026-05-26"
venue: "Data Leverage (Digital Garden / dataleverage.substack.com)"
authors: "Nicholas Vincent"
source_url: "https://nickmvincent.github.io/short-focus-posts/augmentation-is-a-data-flow-problem.html"
retrieved: "2026-08-13"
content: "full-text"
notes: "Dek: A short argument that \"augment, do not replace\" is about data control. Garden section: short-focus-posts. Mirrored on the Data Leverage Substack."
---

# Augmentation is a data flow problem

## Full text

Figures in the AI industry have been saying things along the lines of
this: “We want to build AI to augment humans -- without replacing
humans!” I think the idea is great. But so far, we haven’t seen much
evidence that expressing pro-augmentation views has led to commitments
to making this happen. Perhaps these statements are shaping internal
priorities (more compute for interface experimentation, more product
work on copilot tools, more attention to human-AI workflows, etc.), but
we can't be sure.

Allocating more resources toward interface-focused research could
produce tools that are better at augmentation. However, I do
not think that making AI systems better at augmenting workers
will, by itself, prevent substitution or replacement. In fact,
augmenting systems may accelerate replacement in domains that are
currently data-scarce.

When a worker uses an AI system to perform some task requiring what
we might now think of as "human stuff" (judgment, taste, domain
knowledge, private context, etc.), that worker produces rich workflow
traces and outcome data. If traces/outcomes are captured by the upstream
AI developer providing the model (or captured by the worker's employer
and then passed on to the AI developer), the worker has produced
training and/or evaluation data. The next model will be better at doing
that task with less human input. The worker’s marginal contribution and
bargaining power fall, even though the original system was “augmenting”
at deployment time.

If we really believe in data scaling, we should expect scaling to
apply to any capability domain that can be captured in data records.
Many areas where models are currently bad are areas where data is harder
to get. But if we had the data, and no countervailing forces, why
wouldn't models be able to learn the necessary patterns to capture
judgment, taste, and domain knowledge? (I do not mean to argue that
every social or relational dimension of work will disappear; people may
continue to value human presence, accountability, care, etc., but even
these aspects of labor will not be immune to data scaling.)

One tempting response: we should simply impose “augment-only” rules
at the modelling level: build systems that assist workers but are
somehow prevented from replacing them. I do not think this is
technically coherent. Once a model has learned a capability, it is very
hard to guarantee that the capability will only be used to complement
human labor rather than substitute for it. Data that makes a system
useful as a copilot will also make it useful as a replacement. I do not
think the “Augment, don’t replace” vision can be achieved primarily
through constraints and/or norms that impact people's actions at the
level of model building. I think we instead must support constraints and
friction that affect data capture and use. This will fundamentally limit
certain capabilities, but I think that this will be necessary (if we're
serious about reducing human replacement, which we may not always
be).

An AI system can be stably augmentative if and only if the system is
deployed in a way that preserves meaningful control over upstream
training data, use-time information, and downstream evaluation data.
Many efforts to build augmenting systems -- with the best of intentions
-- will directly support replacement unless they somehow restrict the
flow of data. This friction could come in the form of increased
individual data rights and/or an approach emphasizing data
intermediaries and collective bargaining.

Changelog:

- Revisited this on Aug 3, 2026; made small updates to improve
clarity.

Source revision history

Selected Git commits that changed this source file.

- 0b5f434e56 2026-08-03 - Polish published short posts

- d96a1e08ab 2026-08-03 - Revise drafts on evaluation debt and replacing actions

- b7cec01ae6 2026-07-16 - Refresh site and organize writing

- 4b26d764e6 2026-07-13 - Clarify why AI augmentation depends on data control

- 9fb4674b8a 2026-07-12 - Migrate blog into digital presence monorepo

Source and AT Protocol record

Source path
content/writing/short-posts/2026-05-26-short--augmentation-is-a-data-flow-problem.md

AT Protocol URI
at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.document/3mni4cwedk57p

Local AT Protocol-shaped preview used to inspect the record before an exact public cache is refreshed.

{
"note": "Local AT Protocol-shaped preview. Run `make garden-refresh-atproto` to cache exact public records where available.",
"sourcePath": "content/writing/short-posts/2026-05-26-short--augmentation-is-a-data-flow-problem.md",
"uri": "at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.document/3mni4cwedk57p",
"value": {
"$type": "site.standard.document",
"title": "Augmentation is a data flow problem",
"description": "A short argument that \"augment, do not replace\" is about data control.",
"publishedAt": "2026-05-26",
"site": "at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.publication/3mmpcciuaj22a",
"content": {
"$type": "at.markpub.markdown",
"text": "Figures in the AI industry have been saying things along the lines of this: “We want to build AI to augment humans -- without replacing humans!” I think the idea is great. But so far, we haven’t seen much evidence that expressing pro-augmentation views has led to commitments to making this happen. Perhaps these statements are shaping internal priorities (more compute for interface experimentation, more product work on copilot tools, more attention to human-AI workflows, etc.), but we can't be sure.\n\nAllocating more resources toward interface-focused research could produce tools that are better at augmentation. However, I do _not_ think that making AI systems better at augmenting workers will, by itself, prevent substitution or replacement. In fact, augmenting systems may accelerate replacement in domains that are currently data-scarce.\n\nWhen a worker uses an AI system to perform some task requiring what we might now think of as \"human stuff\" (judgment, taste, domain knowledge, private context, etc.), that worker produces rich workflow traces and outcome data. If traces/outcomes are captured by the upstream AI developer providing the model (or captured by the worker's employer and then passed on to the AI developer), the worker has produced training and/or evaluation data. The next model will be better at doing that task with less human input. The worker’s marginal contribution and bargaining power fall, even though the original system was “augmenting” at deployment time.\n\nIf we really believe in data scaling, we should expect scaling to apply to any capability domain that can be captured in data records. Many areas where models are currently bad are areas where data is harder to get. But if we had the data, and no countervailing forces, why wouldn't models be able to learn the necessary patterns to capture judgment, taste, and domain knowledge? (I do not mean to argue that every social or relational dimension of work will disappear; people may continue to value human presence, accountability, care, etc., but even these aspects of labor will not be immune to data scaling.)\n\nOne tempting response: we should simply impose “augment-only” rules at the modelling level: build systems that assist workers but are somehow prevented from replacing them. I do not think this is technically coherent. Once a model has learned a capability, it is very hard to guarantee that the capability will only be used to complement human labor rather than substitute for it. Data that makes a system useful as a copilot will also make it useful as a replacement. I do not think the “Augment, don’t replace” vision can be achieved primarily through constraints and/or norms that impact people's actions at the level of model building. I think we instead must support constraints and friction that affect data capture and use. This will fundamentally limit certain capabilities, but I think that this will be necessary (if we're serious about reducing human replacement, which we may not always be).\n\nAn AI system can be stably augmentative if and only if the system is deployed in a way that preserves meaningful control over upstream training data, use-time information, and downstream evaluation data. Many efforts to build augmenting systems -- with the best of intentions -- will directly support replacement unless they somehow restrict the flow of data. This friction could come in the form of increased individual data rights and/or an approach emphasizing data intermediaries and collective bargaining.\n\nChangelog:\n\n- Revisited this on Aug 3, 2026; made small updates to improve clarity.\n"
}
}
}
