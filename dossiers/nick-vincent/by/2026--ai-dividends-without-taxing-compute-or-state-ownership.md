---
title: "AI Dividends Without Taxing Compute or State Ownership: A Presumptive Commons-Rent Tax Based on Capability Measurement and Data Attribution"
person: "nick-vincent"
section: "by"
type: "blog-post"
year: 2026
date: "2026-06-07"
venue: "Data Leverage (Digital Garden / dataleverage.substack.com)"
authors: "Nicholas Vincent"
source_url: "https://nickmvincent.github.io/long-posts/presumptive-commons-rent-tax-ai-dividends.html"
retrieved: "2026-08-13"
content: "full-text"
notes: "Dek: Data dividends based on capability measurement, data provenance, and AI auditing. Garden section: long-posts. Mirrored on the Data Leverage Substack."
---

# AI Dividends Without Taxing Compute or State Ownership: A Presumptive Commons-Rent Tax Based on Capability Measurement and Data Attribution

## Full text

I wrote the first draft of this after the Sanders op-ed, and
updated it in August 2026 after the discussion had time to
settle.

In June 2026, US Senator Bernie Sanders put forth an AI
dividend proposal that was closely related to an earlier 2021 data
dividends report I helped lead. This proposal is also related to attestation
across the AI supply chain, the
AI evaluation crisis, and Clear
Data Rules.

In this post, I want to lay out a relatively concrete proposal for a
data dividend funded by a data-dependence tax. More precisely, I propose
that we design and implement a tax on the corporate operating
profits attributable to AI systems that is justified by a
presumption that model capabilities are dependent on data commons.
Critically, this tax could be driven down to zero by providing receipts
that show "capabilities-to-data attribution" -- that is, by explaining
how AI systems gained their capabilities, a company that has AI-driven
operating profits can reduce its tax to zero. The goal of this tax would
be to disincentivize unexplained capabilities and to offer a
top-down, tax-based solution to a commons governance problem.

We could call this a "Presumptive Commons-Rent Tax" (PCRT).

In the 2021 report, we focused on trying to find various proxies for
the concept of "data dependence" in order to rank different companies in
terms of how much data they use (e.g. by counting their users, auditing
the volume of data within their organizational databases, etc.).

The PCRT would not try to measure data dependence directly. Instead,
the tax would lean on an assumption that more capable AI systems draw
more heavily on the data commons (broadly construed) that humanity has
built. Normatively, the tax would not be trying to say that it's a bad
thing for AI to use data commons. The point of many of these data
commons was to enable shared scientific advancement -- including in
computing and AI.

There are two problems with the current arrangement, however. First,
operating profits from AI systems are in part (but by no means in their
entirety -- of course capital and labor from AI companies are needed)
rents over common-pool resources. Second, companies can profit from AI
capabilities without having to explain where those capabilities came
from.

The PCRT would have a relatively simple "tax credit" system: the more
evidence that AI companies can provide showing how specific capabilities
map to data, the lower the tax goes. A model with an entirely private,
fully "paid for" data supply chain would pay zero tax. A model with some
commons dependence (e.g. Internet-scale pretraining) would pay a small
tax.

Tax proceeds would be split between funding new public goods, making
reciprocity and sustainability payments to data commons themselves (e.g.
paying to help maintain the Internet, peer-production projects, etc.),
and making payments to individuals (if viable).

Who would judge the legitimacy of tax credit claims from AI
companies? The ecosystem of international AI auditing organizations
would work together to verify these claims and lower their tax
burden.

The designers of the tax would need to determine a base rate and the
specific mapping function that determines how additional evidence
(something like "percent of capabilities explained") converts to tax
credits. These design choices would determine whether the tax ultimately
incentivizes large-scale behavior change from AI companies (e.g.
radically overhauling data pipelines or improving data transparency) or
simply encourages them to pay the tax. Optimistically, though, this
means that if something like this were implemented, we would either end
up in a world where companies profiting from highly capable
data-dependent systems pay a large amount of aggregate funds into
various shared funds (perhaps even internationally governed) or a world
where the vast majority of upstream data flows through healthy data
markets where data creators have the collective leverage necessary to
get paid through a mixture of upfront and royalty payments.

Of course, there are a lot of details to be worked out!

### Brief history
of data dividends research in 2021

In the 2021 report, we analyzed a variety of possible fundraising and
disbursement mechanisms for a “data dividend” (which was being discussed
by Governor Newsom of California at the time). While we were not aiming
to pick a single answer, our "likely good first step" suggestion was a
data dependence tax to fund public goods. To make "data dependence"
operational, we suggested using user count as a proxy: firms with lots
of users are probably getting lots of value from aggregated data.

Some other notable works on data dividends around that time
include:

- Bax's computational
treatment of individual and grouped data dividends using Shapley and
Owen values

- Wadhwa's
Data Catalyst review of the economic impact and feasibility of data
dividends

- I contributed to this preprint on data dividend
design choices and this later EAAMO
poster paper on the challenges of “meritocratic” data valuation for
dividends

Another key idea from the report was that, in the context of
retroactive dividends (as opposed to forward-looking markets), it is
probably best to avoid “fine-grained valuation” (e.g., trying to write
personalized checks for individuals). In the context of data markets, it
could still make sense in some cases to price both individual data
points and collective bundles.

In short: for a dividend, we should tax dependence on collective data
and disburse it coarsely while we figure out better valuation and
interpretability methods. I think the reasoning from that report holds
up pretty well in light of AI progress. I also think it’s notable that
the motivation described in the Sanders proposal matches the arguments
in our original report pretty closely.

However, I also think we should be sensitive to concerns from economists
about the impacts of compute taxes, automation taxes, capital taxes,
etc. After the Sanders op-ed went out, the idea quickly drew a
cross-ideological mix of interest, skepticism, and pushback (see e.g. AP,
WaPo,
Reason,
Cato,
and Fortune
for some of the pro-market, libertarian, and tech policy critiques of
government equity stakes in AI companies).

One general concern that cuts across some of the critiques: depending
on design, an AI dividend tax could have negative effects on growth,
investment, diffusion, etc. If we can avoid it, we might want to avoid
explicitly targeting “AI,” “compute,” or “automation.”

Instead, I think one of the things we actually want to target is
private value extraction from the commons. (The second, in the next
section, is "unexplained capabilities").

Something that’s complicated about frontier AI systems is that they
depend on many different categories of data. Some of the data used to
train modern systems are literal digital commons like Wikipedia that
have clear licenses and are meant to be used (with attribution). Some
data is literally in the public domain.

A lot of data used for pretraining (e.g. Common Crawl) occupies a
gray area -- much of it lacks formal licensing status, but the industry
position is that fair use makes it commons-like. The U.S.
Copyright Office's report on generative AI training describes the
still-evolving fair-use and licensing landscape. Similarly, a lot of
open-source code used for training is being treated as a de facto
commons because we haven't received legal clarity around how attribution
and copyleft clauses apply to generative AI.

Finally, there's a huge swath of data that is definitely not a
commons in any legal sense -- e.g. click data, trace data, and posts on
private social media platforms. These data were produced under terms of
service that tend to favor the platforms, but we can nonetheless think
of them as collectively forming a very broad pool. Your Facebook posts
and Google search history are not part of a literal commons. As we
rethink data governance for the post-AI age, however, we might want to
treat such data as subject to commons governance. The general idea of
this proposal works even if you reject this particular point.

### Capability
as a proxy for data dependence (and presumed commons dependence)

I think there’s actually an easy way to roughly measure extraction
from the commons: take a "rebuttable presumption of data-dependence"
approach to the existence of powerful AI. Currently (and barring a major
paradigm shift in AI) all of humanity’s approaches to building powerful
AI are data-dependent. Even approaches that use reinforcement learning
or synthetic data still have massive data dependencies in the overall
training and evaluation pipeline needed to build an AI system.

Instead of using user count or something else as a primary proxy for
data dependence, we might consider using capability itself. We would
basically be working from a default assumption that if an AI system is
very capable and monetized, a meaningful chunk of that value came from
commons data. I think this assumption is currently very justified and
will remain so in the near term.

There are several reasonable ways we can coarsely estimate the
fraction of value attributable to data versus the value attributable to
compute, non-data technical progress, interface progress, and other
factors. We just need to pick some number. 50%, which happens to appear
in the Sanders
proposal, might be a reasonable starting placeholder. The more
capable a system is, the more burden a company should face in explaining
how it got so good.

Thus, we could iterate on various data dividends proposals to design
what we might call a “presumptive commons-rent tax.” When a firm makes
money from a powerful AI system, we presume some share of the rent came
from commons and commons-ish data. AI operators can lower their
presumptive commons-rent tax by either showing that capabilities came
from data that was acquired under non-commons conditions (e.g., licensed
data purchased via a healthy data market) or by showing that
capabilities came directly from specific commons data sources (and then
paying a greatly reduced tax).

As a toy example, suppose a highly capable AI system earns $10B in
annual rents and the presumptive commons-rent share is set at 50%. If
the operator can substantiate that half of its capability-relevant data
contribution came from licensed, governed, or reciprocal sources, the
taxable commons-rent base might fall from $5B to $2.5B.

### How
evidence of data use would lower the tax burden

We would need a clean accounting scheme here, with a possible unit
being explained data. Explained data would estimate the
share of a model’s effective, capability-relevant data contribution that
the company can actually account for. To count as tax-reducing explained
data, a data source would need to be documented, have provenance and
proof of fair acquisition (e.g., because it was licensed, bought under
contract, or similar), and plausibly relevant to the capabilities being
taxed. Critically, the tax rate would depend on the capability level
achieved by a model, so more capable models would require more explained
data, in accordance with our scientific understanding of scaling laws and training data
attribution.

Preparing such evidence would look something like this:

- first, a company profiting from AI systems prepares a datasheet for
each commercial system it releases for consumers or enterprise customers
(this could be done at the model-family level to avoid imposing an undue
burden on AI companies)

- second, each entry in the datasheet would be labeled with an
acquisition/governance status (licensed, internally generated,
public-domain, governed by a data union/trust, etc.)

- third, provenance evidence would be collected to support the
acquisition/governance classifications

- fourth, usage evidence shows how much each data component was
actually used (this could include details about mixture fractions,
sampling rates, repetition, deduplication, training stage, post-training
role, eval role, and upstream sources for synthetic or RL data).
Ultimately, this evidence would be reviewed by AI auditing
organizations, so it would not have to be completely standardized; the
framework could allow flexibility for different model types

- fifth, just as datasheet entries would be linked to provenance
evidence, usage entries would be linked to ablations to show how those
data components actually mattered for the relevant capabilities. This
research will be expensive, but we'll need to do it anyway if we want to
deploy AI in high-risk contexts.

For a first implementation, we might just use "evidence tiers" as
determined by the adjudicating organizations responsible for capability
measurement.

To summarize: model capability comes from a production process
involving compute, model size, data quantity, data quality, interface
and tool access, etc. Capability measurement would be used to set a
default presumed tax rate. Companies could present data details to
reduce their tax burden, and an auditor (or a network of auditing
organizations) would convert the evidence into "accepted explained-data
points" to determine a final rate.

This could create a good set of incentives:

- if companies want lower taxes, they should build datasheets and provenance
systems from the start

- if they want larger reductions, they need to run and share
data-centric scientific experiments

- if they rely heavily on commons data, they can still do that, but
they should pay something back or give something back

- the tax is fully avoidable!

Importantly, everything described above would basically involve
preparing a report that would look a lot like something required by
existing or proposed data-transparency rules, such as the EU
AI Code of Practice and California
AB 2013. This is close to something AI companies might need to do
anyway!

### Targeting "unexplained
capabilities"

But wait a second -- if the whole concern around taxing compute or
automation is that "we shouldn't tax stuff that we want more of," isn't
this potentially even worse than those other taxes, if we interpret this
proposal as a tax on intelligence itself or capability itself?

Critically, the PCRT should not be designed as a tax on intelligence
or capability, but rather a tax on unexplained or mysterious capability.
If an AI operator trains on 100% licensed/accounted-for data and can
show that this data actually drove the relevant capabilities, its
commons tax would be near zero.

If you train on Wikipedia, Common Crawl, public code, user traces,
etc., you would end up paying some reasonable tax back to the commons
(and the tax might also be reduced if you show evidence of, e.g.,
contributing to something like Wikimedia
Enterprise, or making in-kind contributions of data, model weights,
gold-standard code, etc.). Ideally, during any kind of transition
period, there would be a way to transfer existing reciprocity programs
into tax credits as well. And perhaps reciprocity programs could just be
integrated into the program in the long term.

### Auditing and enforcement

How would this be enforced? This is where the recent momentum around
auditing and safety comes in. Capability measurement -- and assessment
of the ablations and whether AI operators are able to provide plausible
accounts of, at a high level, how data choices drive capabilities --
could be handled by an ecosystem of independent auditing institutions,
along the lines of the frontier AI
auditing ecosystem.

The ecosystem of auditing orgs would become part of the
infrastructure for data governance: measuring capabilities, reviewing
provenance, looking at ablations, etc. This would also get companies to
contribute to advancing and sharing science about where model
capabilities come from, in turn helping the auditing organizations.

Critically, by looping in auditing and safety organizations, this
proposal could also take advantage of the fact that AI safety is one
area with a plausible path to international cooperation. In fact, I
think this cooperation might offer one of the few plausible paths toward
a global wealth fund rather than various national funds and
sovereign-focused economic interventions.

A single global wealth fund is morally attractive, because the data
commons is transnational, but the more realistic path may be federated:
national or regional AI commons funds collect revenue, while treaty or
club arrangements allocate some share to global public goods and commons
institutions.

Of course, we likely would not want independent AI auditors to be
burdened with global taxation responsibility (nor would they likely want
a bunch of extra work). Public tax authorities would still set the
rules, while accredited auditors (with proportionate support to hire
staff to do all this) could review evidence and a public technical board
could maintain standards.

Compared to compute and automation taxes, I believe this kind of
approach would avoid some of the concerns raised by economists and
instead target a specific harm: companies turning collective human
activity and public knowledge into private rents without a proportionate
return.

In the current world, this would mean that AI companies would pay a
bunch of taxes, which then might fuel, e.g., a national wealth fund, or
ideally a global wealth fund. But it also creates a path to lower the
burden: license data, work with data unions/trusts, document provenance,
run ablations, or give value back to the commons.

Source revision history

Selected Git commits that changed this source file.

- ce84ea60ec 2026-08-08 - Update presumptive commons-rent tax post

- 9fb4674b8a 2026-07-12 - Migrate blog into digital presence monorepo

Source and AT Protocol record

Source path
content/writing/posts/2026-06-07-presumptive-commons-rent-tax-ai-dividends.md

AT Protocol URI
at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.document/3mnqonrblbhwi

Local AT Protocol-shaped preview used to inspect the record before an exact public cache is refreshed.

{
"note": "Local AT Protocol-shaped preview. Run `make garden-refresh-atproto` to cache exact public records where available.",
"sourcePath": "content/writing/posts/2026-06-07-presumptive-commons-rent-tax-ai-dividends.md",
"uri": "at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.document/3mnqonrblbhwi",
"value": {
"$type": "site.standard.document",
"title": "AI Dividends Without Taxing Compute or State Ownership: A Presumptive Commons-Rent Tax Based on Capability Measurement and Data Attribution",
"description": "Data dividends based on capability measurement, data provenance, and AI auditing.",
"publishedAt": "2026-06-07",
"site": "at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.publication/3lzrsw2kvwc2m",
"content": {
"$type": "at.markpub.markdown",
"text": "*I wrote the first draft of this after the Sanders op-ed, and updated it in August 2026 after the discussion had time to settle.*\n\nIn June 2026, US Senator Bernie Sanders put forth an [AI dividend proposal][sanders-ai-dividend] that was closely related to an earlier 2021 [data dividends report][data-dividend-report] I helped lead. This proposal is also related to [attestation across the AI supply chain][attestation], [the AI evaluation crisis][evaluation-crisis], and [Clear Data Rules][clear-data-rules].\n\nIn this post, I want to lay out a relatively concrete proposal for a data dividend funded by a data-dependence tax. More precisely, I propose that we design and implement a tax on the *corporate operating profits attributable to AI systems* that is justified by *a presumption that model capabilities are dependent on data commons*. Critically, this tax could be driven down to zero by providing receipts that show \"capabilities-to-data attribution\" -- that is, by explaining how AI systems gained their capabilities, a company that has AI-driven operating profits can reduce its tax to zero. The goal of this tax would be to disincentivize *unexplained capabilities* and to offer a top-down, tax-based solution to a commons governance problem.\n\nWe could call this a \"Presumptive Commons-Rent Tax\" (PCRT).\n\nIn the 2021 report, we focused on trying to find various proxies for the concept of \"data dependence\" in order to rank different companies in terms of how much data they use (e.g. by counting their users, auditing the volume of data within their organizational databases, etc.).\n\nThe PCRT would not try to measure data dependence directly. Instead, the tax would lean on an assumption that more capable AI systems draw more heavily on the data commons (broadly construed) that humanity has built. Normatively, the tax would not be trying to say that it's a bad thing for AI to use data commons. The point of many of these data commons was to enable shared scientific advancement -- including in computing and AI.\n\nThere are two problems with the current arrangement, however. First, operating profits from AI systems are in part (but by no means in their entirety -- of course capital and labor from AI companies are needed) rents over common-pool resources. Second, companies can profit from AI capabilities without having to explain where those capabilities came from.\n\nThe PCRT would have a relatively simple \"tax credit\" system: the more evidence that AI companies can provide showing how specific capabilities map to data, the lower the tax goes. A model with an entirely private, fully \"paid for\" data supply chain would pay zero tax. A model with some commons dependence (e.g. Internet-scale pretraining) would pay a small tax.\n\nTax proceeds would be split between funding new public goods, making reciprocity and sustainability payments to data commons themselves (e.g. paying to help maintain the Internet, peer-production projects, etc.), and making payments to individuals (if viable).\n\nWho would judge the legitimacy of tax credit claims from AI companies? The ecosystem of international AI auditing organizations would work together to verify these claims and lower their tax burden.\n\nThe designers of the tax would need to determine a base rate and the specific mapping function that determines how additional evidence (something like \"percent of capabilities explained\") converts to tax credits. These design choices would determine whether the tax ultimately incentivizes large-scale behavior change from AI companies (e.g. radically overhauling data pipelines or improving data transparency) or simply encourages them to pay the tax. Optimistically, though, this means that if something like this were implemented, we would either end up in a world where companies profiting from highly capable data-dependent systems pay a large amount of aggregate funds into various shared funds (perhaps even internationally governed) or a world where the vast majority of upstream data flows through healthy data markets where data creators have the collective leverage necessary to get paid through a mixture of upfront and royalty payments.\n\nOf course, there are a lot of details to be worked out!\n\n## Brief history of data dividends research in 2021\n\nIn the 2021 report, we analyzed a variety of possible fundraising and disbursement mechanisms for a “data dividend” (which was being discussed by Governor Newsom of California at the time). While we were not aiming to pick a single answer, our \"likely good first step\" suggestion was a data dependence tax to fund public goods. To make \"data dependence\" operational, we suggested using user count as a proxy: firms with lots of users are probably getting lots of value from aggregated data.\n\nSome other notable works on data dividends around that time include:\n\n- [Bax's computational treatment](https://arxiv.org/pdf/1905.01805) of individual and grouped data dividends using Shapley and Owen values\n- [Wadhwa's Data Catalyst review](https://datacatalyst.org/wp-content/uploads/2020/06/Economic-Impact-and-Feasibility-of-Data-Dividends-1.pdf) of the economic impact and feasibility of data dividends\n- I contributed to this [preprint](https://arxiv.org/abs/1912.00757) on data dividend design choices and this later [EAAMO poster paper](https://www.nickmvincent.com/static/eaamo_data_dividends.pdf) on the challenges of “meritocratic” data valuation for dividends\n\nAnother key idea from the report was that, in the context of retroactive dividends (as opposed to forward-looking markets), it is probably best to avoid “fine-grained valuation” (e.g., trying to write personalized checks for individuals). In the context of data markets, it could still make sense in some cases to price both individual data points and collective bundles.\n\nIn short: for a dividend, we should tax dependence on collective data and disburse it coarsely while we figure out better valuation and interpretability methods. I think the reasoning from that report holds up pretty well in light of AI progress. I also think it’s notable that the motivation described in the Sanders proposal matches the arguments in our original report pretty closely.\n\nHowever, I also think we should be sensitive to [concerns][nber-ai-taxes] from economists about the impacts of compute taxes, automation taxes, capital taxes, etc. After the Sanders op-ed went out, the idea quickly drew a cross-ideological mix of interest, skepticism, and pushback (see e.g. [AP][ap-ai-public-ownership], [WaPo][washpost-sanders-ai-stake], [Reason][reason-sanders-ai-wealth], [Cato][cato-trump-sanders-swf], and [Fortune][fortune-sacks-ai-equity] for some of the pro-market, libertarian, and tech policy critiques of government equity stakes in AI companies).\n\nOne general concern that cuts across some of the critiques: depending on design, an AI dividend tax could have negative effects on growth, investment, diffusion, etc. If we can avoid it, we might want to avoid explicitly targeting “AI,” “compute,” or “automation.”\n\n_Instead, I think one of the things we actually want to target is private value extraction from the commons._ (The second, in the next section, is \"unexplained capabilities\").\n\nSomething that’s complicated about frontier AI systems is that they depend on many different categories of data. Some of the data used to train modern systems are literal digital commons like Wikipedia that have clear licenses and are meant to be used (with attribution). Some data is literally in the public domain.\n\nA lot of data used for pretraining (e.g. Common Crawl) occupies a gray area -- much of it lacks formal licensing status, but the industry position is that fair use makes it commons-like. The [U.S. Copyright Office's report on generative AI training][copyright-office-ai-training] describes the still-evolving fair-use and licensing landscape. Similarly, a lot of open-source code used for training is being treated as a de facto commons because we haven't received legal clarity around how attribution and copyleft clauses apply to generative AI.\n\nFinally, there's a huge swath of data that is definitely not a commons in any legal sense -- e.g. click data, trace data, and posts on private social media platforms. These data were produced under terms of service that tend to favor the platforms, but we can nonetheless think of them as collectively forming a very broad pool. Your Facebook posts and Google search history are not part of a literal commons. As we rethink data governance for the post-AI age, however, we might want to treat such data as subject to commons governance. The general idea of this proposal works even if you reject this particular point.\n\n## Capability as a proxy for data dependence (and presumed commons dependence)\n\nI think there’s actually an easy way to roughly measure extraction from the commons: take a \"rebuttable presumption of data-dependence\" approach to the existence of powerful AI. Currently (and barring a major paradigm shift in AI) all of humanity’s approaches to building powerful AI are data-dependent. Even approaches that use reinforcement learning or synthetic data still have massive data dependencies in the overall training and evaluation pipeline needed to build an AI system.\n\nInstead of using user count or something else as a primary proxy for data dependence, we might consider using capability itself. We would basically be working from a default assumption that if an AI system is very capable and monetized, a meaningful chunk of that value came from commons data. I think this assumption is currently very justified and will remain so in the near term.\n\nThere are several reasonable ways we can coarsely estimate the fraction of value attributable to data versus the value attributable to compute, non-data technical progress, interface progress, and other factors. We just need to pick some number. 50%, which happens to appear in the [Sanders proposal][sanders-ai-dividend], might be a reasonable starting placeholder. The more capable a system is, the more burden a company should face in explaining how it got so good.\n\nThus, we could iterate on various data dividends proposals to design what we might call a “presumptive commons-rent tax.” When a firm makes money from a powerful AI system, we presume some share of the rent came from commons and commons-ish data. AI operators can lower their presumptive commons-rent tax by either showing that capabilities came from data that was acquired under non-commons conditions (e.g., licensed data purchased via a healthy data market) or by showing that capabilities came directly from specific commons data sources (and then paying a greatly reduced tax).\n\nAs a toy example, suppose a highly capable AI system earns $10B in annual rents and the presumptive commons-rent share is set at 50%. If the operator can substantiate that half of its capability-relevant data contribution came from licensed, governed, or reciprocal sources, the taxable commons-rent base might fall from $5B to $2.5B.\n\n## How evidence of data use would lower the tax burden\n\nWe would need a clean accounting scheme here, with a possible unit being **explained data**. Explained data would estimate the share of a model’s effective, capability-relevant data contribution that the company can actually account for. To count as tax-reducing explained data, a data source would need to be documented, have provenance and proof of fair acquisition (e.g., because it was licensed, bought under contract, or similar), and plausibly relevant to the capabilities being taxed. Critically, the tax rate would depend on the capability level achieved by a model, so more capable models would require more explained data, in accordance with our scientific understanding of [scaling laws][kaplan-scaling-laws] and [training data attribution][training-data-attribution].\n\nPreparing such evidence would look something like this:\n\n- first, a company profiting from AI systems prepares a datasheet for each commercial system it releases for consumers or enterprise customers (this could be done at the model-family level to avoid imposing an undue burden on AI companies)\n- second, each entry in the datasheet would be labeled with an acquisition/governance status (licensed, internally generated, public-domain, governed by a data union/trust, etc.)\n- third, provenance evidence would be collected to support the acquisition/governance classifications\n- fourth, usage evidence shows how much each data component was actually used (this could include details about mixture fractions, sampling rates, repetition, deduplication, training stage, post-training role, eval role, and upstream sources for synthetic or RL data). Ultimately, this evidence would be reviewed by AI auditing organizations, so it would not have to be completely standardized; the framework could allow flexibility for different model types\n- fifth, just as datasheet entries would be linked to provenance evidence, usage entries would be linked to ablations to show how those data components actually mattered for the relevant capabilities. This research will be expensive, but we'll need to do it anyway if we want to deploy AI in high-risk contexts.\n\nFor a first implementation, we might just use \"evidence tiers\" as determined by the adjudicating organizations responsible for capability measurement.\n\nTo summarize: model capability comes from a production process involving compute, model size, data quantity, data quality, interface and tool access, etc. Capability measurement would be used to set a default presumed tax rate. Companies could present data details to reduce their tax burden, and an auditor (or a network of auditing organizations) would convert the evidence into \"accepted explained-data points\" to determine a final rate.\n\nThis could create a good set of incentives:\n\n- if companies want lower taxes, they should build datasheets and [provenance systems][data-provenance-initiative] from the start\n- if they want larger reductions, they need to run and share data-centric scientific experiments\n- if they rely heavily on commons data, they can still do that, but they should pay something back or give something back\n- the tax is fully avoidable!\n\nImportantly, everything described above would basically involve preparing a report that would look a lot like something required by existing or proposed data-transparency rules, such as the [EU AI Code of Practice][eu-ai-code] and [California AB 2013][california-ab-2013]. This is close to something AI companies might need to do anyway!\n\n## Targeting \"unexplained capabilities\"\n\nBut wait a second -- if the whole concern around taxing compute or automation is that \"we shouldn't tax stuff that we want more of,\" isn't this potentially even worse than those other taxes, if we interpret this proposal as a tax on intelligence itself or capability itself?\n\nCritically, the PCRT should not be designed as a tax on intelligence or capability, but rather a tax on unexplained or mysterious capability. If an AI operator trains on 100% licensed/accounted-for data and can show that this data actually drove the relevant capabilities, its commons tax would be near zero.\n\nIf you train on Wikipedia, Common Crawl, public code, user traces, etc., you would end up paying some reasonable tax back to the commons (and the tax might also be reduced if you show evidence of, e.g., contributing to something like [Wikimedia Enterprise][wikimedia-enterprise], or making in-kind contributions of data, model weights, gold-standard code, etc.). Ideally, during any kind of transition period, there would be a way to transfer existing reciprocity programs into tax credits as well. And perhaps reciprocity programs could just be integrated into the program in the long term.\n\n## Auditing and enforcement\n\nHow would this be enforced? This is where the recent momentum around auditing and safety comes in. Capability measurement -- and assessment of the ablations and whether AI operators are able to provide plausible accounts of, at a high level, how data choices drive capabilities -- could be handled by an ecosystem of independent auditing institutions, along the lines of the [frontier AI auditing ecosystem][frontier-ai-auditing].\n\nThe ecosystem of auditing orgs would become part of the infrastructure for data governance: measuring capabilities, reviewing provenance, looking at ablations, etc. This would also get companies to contribute to advancing and sharing science about where model capabilities come from, in turn helping the auditing organizations.\n\nCritically, by looping in auditing and safety organizations, this proposal could also take advantage of the fact that AI safety is one area with a plausible path to international cooperation. In fact, I think this cooperation might offer one of the few plausible paths toward a global wealth fund rather than various national funds and sovereign-focused economic interventions.\n\nA single global wealth fund is morally attractive, because the data commons is transnational, but the more realistic path may be federated: national or regional AI commons funds collect revenue, while treaty or club arrangements allocate some share to global public goods and commons institutions.\n\nOf course, we likely would not want independent AI auditors to be burdened with global taxation responsibility (nor would they likely want a bunch of extra work). Public tax authorities would still set the rules, while accredited auditors (with proportionate support to hire staff to do all this) could review evidence and a public technical board could maintain standards.\n\nCompared to compute and automation taxes, I believe this kind of approach would avoid some of the concerns raised by economists and instead target a specific harm: companies turning collective human activity and public knowledge into private rents without a proportionate return.\n\nIn the current world, this would mean that AI companies would pay a bunch of taxes, which then might fuel, e.g., a national wealth fund, or ideally a global wealth fund. But it also creates a path to lower the burden: license data, work with data unions/trusts, document provenance, run ablations, or give value back to the commons.\n\n[sanders-ai-dividend]: https://www.sanders.senate.gov/op-eds/the-public-should-own-half-of-the-big-a-i-companies/\n[data-dividend-report]: https://www.nickmvincent.com/static/Data-Dividend_final.pdf\n[attestation]: https://dataleverage.substack.com/p/attestation-across-the-ai-supply\n[evaluation-crisis]: https://dataleverage.substack.com/p/the-ai-evaluation-crisis-is-an-opportunity\n[clear-data-rules]: https://dataleverage.substack.com/p/almost-everybody-including-both-data\n[eu-ai-code]: https://digital-strategy.ec.europa.eu/en/policies/ai-code-practice\n[frontier-ai-auditing]: https://www.averi.org/ourwork/frontier-ai-auditing\n[nber-ai-taxes]: https://www.nber.org/papers/w34873\n[ap-ai-public-ownership]: https://apnews.com/article/sam-altman-ai-bernie-sanders-trump-public-ownership-772224f9cd138eb79d3ef3336858a5d5\n[washpost-sanders-ai-stake]: https://www.washingtonpost.com/opinions/2026/06/03/bernie-sanders-wants-government-stake-ai-companies/\n[reason-sanders-ai-wealth]: https://reason.com/2026/06/02/bernie-sanders-ai-wealth-fund-bill-shows-that-he-doesnt-understand-ai-or-wealth/\n[cato-trump-sanders-swf]: https://www.cato.org/blog/trump-opened-door-sanderss-sovereign-wealth-fund\n[fortune-sacks-ai-equity]: https://fortune.com/2026/06/06/former-ai-czar-david-sacks-bernie-sanders-bill-government-equity-stupidity-tax-nationalization-trump-public-stakes/\n[wikimedia-enterprise]: https://wikimediafoundation.org/news/2021/10/25/wikimedia-foundation-launches-wikimedia-enterprise-the-new-opt-in-product-for-companies-and-organizations-to-easily-reuse-content-from-wikipedia-and-wikimedia-projects/\n[data-provenance-initiative]: https://www.nature.com/articles/s42256-024-00878-8\n[kaplan-scaling-laws]: https://arxiv.org/abs/2001.08361\n[training-data-attribution]: https://arxiv.org/abs/2308.03296\n[california-ab-2013]: https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240AB2013\n[copyright-office-ai-training]: https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-3-Generative-AI-Training-Report-Pre-Publication-Version.pdf\n"
}
}
}
