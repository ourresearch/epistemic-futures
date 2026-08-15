---
title: "Attestation across the AI Supply Chain"
person: "nick-vincent"
section: "by"
type: "blog-post"
year: 2026
date: "2026-04-08"
venue: "Data Leverage (Digital Garden / dataleverage.substack.com)"
authors: "Nicholas Vincent"
source_url: "https://nickmvincent.github.io/long-posts/attestation-across-the-ai-supply-chain.html"
retrieved: "2026-08-13"
content: "full-text"
notes: "Dek: A proposal for interoperable attestation objects that connect training data, evaluation labor, and AI-generated outputs across the AI supply chain. Garden section: long-posts. Mirrored on the Data Leverage Substack."
---

# Attestation across the AI Supply Chain

## Full text

April 27, 2026: I made some edits throughout to condense this
longer post and improve flow. I also wrote this additional bullet point
summary:

I am feeling hopeful that momentum in the AI evaluation space can
help improve data markets and data ecosystems more broadly. I wrote a
longer post on the reasons why, currently framing this as “attestations
across the AI supply chain”. Here’s the bullet point summary:

-

Some AI users (public bodies, enterprise users, picky consumers)
and other parties (regulators, insurers) are going to, or have already
started to, demand some kind of “attestation objects” in the domain of
AI evaluation.

-

These buyers want some kind of proof that a model was evaluated;
evaluation organizations are already beginning to document and share
their evaluations

-

An attestation that a certain evaluation procedure was performed
could be similar to, and interconnected with, other kinds of
attestations across the AI supply chain.

-

One related attestation could say that a certain piece of data
was used to train a model.

-

One related attestation could say that a certain piece of
information was retrieved and used at inference time.

-

One related attestation could say that a certain information
object (sequence of output tokens) really came from a certain
model.

-

One related attestation could say that a piece of AI-assisted
output (e.g. downstream code) came from a certain AI output.

-

On the technical side, we should make it easy for these pieces of
information to be linked to each other. They can support a “full
picture” of AI supply chain provenance

-

The technology needed here is actually relatively simple:
registries for the attestation objects, techniques for verification, and
appropriate privacy-preserving ways to share registries and associate
people and organizations with attestation objects

-

Full supply chain provenance can be a product differentiator for
AI developers that helps to combat model
extraction/distillation

-

The existence of more “guilds” who act as sellers in markets for
attested evaluation and training data can provide important incentives
to their members (knowledge workers of all types) to maintain quality
and expertise; this can align incentives so that these guilds provide a
resisting force against overreliance and slop

-

What does this suggest we do?

-

On the social side, we should try to create more demand for all
these kinds of attestations; we should definitely leverage momentum and
energy around evals

-

On the policy side, we should look for opportunities to
incentivize attestation and to make interoperable schemas and cross-talk
easy

-

In total, I think there are at least five distinct forces that
could create demand for attestations: gov’t regulation,
anti-distillation, procurement requirements, AI insurers, consumer
demand.

-

If any of these succeed in creating real demand, this will enable
markets for attested relationships instead of markets for “raw tokens”.
This would be great for society because it can bypass some “core”
information economics challenges with markets for information and likely
create healthier overall data flow dynamics.

This post argues that a shared family of attestation objects could
improve several markets across the AI supply chain: consumer choice
among AI products, upstream markets for training and retrieval data,
markets for audits and evaluations, and downstream markets for
AI-assisted artifacts. Broadly, I'll use the term "attestation object"
here to refer to a verifiable record about who contributed what, in what
role, to which model or output, under what validation process. We can
enable this "shared family" by making progress on the design of an
appropriate schema for the objects (technical/protocol work), the
implementation of supporting policy and regulation, and by building
relevant platforms that enable markets for attested evaluation and other
data.

The ideas discussed here build on work already underway in at least
three adjacent areas: the dataset documentation space (inclusive of
efforts such as datasheets, model
cards, and data
provenance); the Frontier AI
Auditing world; and the content authenticity and provenance (e.g. C2PA)
world. If we get the design of attestation objects right, interoperable
schemas could improve visibility and traceability across training,
evaluation, and usage.

I am especially excited about the broad idea here because progress in
one part of the AI supply chain can bootstrap progress in others.
Existing momentum around audits could foster more training data
transparency and better markets for training and retrieval data. Parties
interested in provenance for AI-generated outputs, such as people
assessing AI-generated code, could help promote transparency upstream.
And if communities adopt norms around transparent AI usage, that may
drive further demand for transparency up the chain.

Specifically, as of April 2026, I think evaluation as a field has
much more momentum, attention, and funding than advocacy around training
data documentation or retrieval markets, and thus I think is the most
likely "entry point" that can enable full-chain provenance.

I'll note that, in addition to momentum around auditing, we're
starting to see some evidence that consumers might care about
attestations for AI products. See, for instance, the "Introducing
ChatGPT Health" blog post, which emphasizes working with "260
physicians who have practiced in 60 countries and dozens of specialties"
to obtain "feedback on model outputs over 600,000 times across 30 areas
of focus". I'll refer to attestation in the context of an AI health
application as a running example throughout.

One reason I think that discussing attestation matters right now is
that data policy conversations often involve two somewhat different
strategies for improving data markets. "Data protection" strategies are
focused on trying to stop scraping, distillation, or reuse through a
combination of law, platform rules, anti-scraping, and poisoning; all
these serve to incentivize market participation by introducing friction
and means to exclude information. An "attestation-forward" strategy
tries to get AI users and/or regulators to care about verified
provenance relationships upstream of AI products. These approaches can
complement each other (in the short term, effective data protection may
produce more pressure to get attestations working) but also likely
benefit from somewhat divergent policy approaches. Data protection
efforts try to block unwanted scraping and distillation; attestation
efforts that succeed in making verified provenance, evaluation, and
output identity matter could make "just scraping anyway" less
valuable.

Very concretely, an attestation-forward data strategy would involve
roughly four broad types of attestation objects:

- a training contribution object: "I am a medical
doctor and I attest that I authored a textbook chapter and agreed to
include it in the ChatGPT Health training dataset."

- an evaluation record object: "I am a medical doctor
working with an AI evaluation organization and I attest that I reviewed
100 ChatGPT Health outputs and believe they represent standard of
care."

- an output provenance object: "OpenAI as an
organization attests that this output telling you to take more Advil
came from the GPT-6.0-med1000 model."

- a downstream use object: "I am a vibe-coder making
an iPhone health app and I attest that I used GPT-6.0-med1000 while
building this app."

Here's a short version of the key claims that motivate an
attestation-forward strategy:

- Users buying AI products, AI developers buying data, anyone
commissioning audits, and anyone consuming AI-generated outputs face a
related set of issues stemming from information asymmetry and lack of
information generally.

- The auditing and evaluation space has significant momentum; at
present, there is an active ecosystem
of third parties such as METR, Apollo Research, and the AI Security Institute providing
attested evaluations of frontier models.

- For users looking to pay for AI products, there remain challenges in
DIY benchmarking of models. It also remains challenging for consumers to
interpret benchmarks and evaluations. Finally, consumers are stuck
mainly making decisions based on model outputs alone; there are
currently few opportunities for consumers to incorporate facts about
model inputs into their decision-making.

- For developers looking to pay for data in AI markets, there are core
market design challenges that stem from the non-rivalry and
non-excludability of information alongside practical challenges with
fine-grained assessment of data value. Markets for data are fragmented,
opaque, and inefficient at the moment.

- Each stage of the AI supply chain could, in theory, involve
attestations from key actors. Data creators can attest that they
included their data in training sets. Auditors can attest to their
participation in evaluation processes. Model outputs can include
attestation objects that help people verify that a given output really
came from a certain model, and in some domains that kind of output
transparency may itself become required. And downstream artifacts can
bundle all these attestations together via flow-down.

If the schema for attestation and provenance can be synchronized
across the supply chain, we can achieve a win-win-win-win:

- Win 1: For data creators and buyers, we might establish healthier
markets for training data that emphasize attestation objects rather than
raw tokens. Upstream data markets would rely less on winning the
constant battle between data protectors versus data extractors
(inclusive of various approaches for scraping and distillation), and
would more easily accommodate arrangements that preserve research or
public-interest use while still giving workers or collectives something
to bargain over.

- Win 2: For auditors, we can help increase demand for high quality
audits and create standardization around benchmarking and evaluation.
Better provenance for the full supply chain should also make auditing
itself easier.

- Win 3: For labs, we can make it easier to sell model outputs without
being undercut by distilled models.

- Win 4: For people consuming content, we can provide means to verify
content authenticity. More generally, people can use all of this
upstream information to help them assess AI-generated content of all
types. This would help end-users who just want to read an AI output to
answer a question and people who want to use AI outputs for other things
(e.g., to sell AI-produced software).

The main downside -- the answer to "why aren't we literally doing
this today if it's so good?" -- is that attestation will impose new
costs on various actors. Training and evaluation labor may cost more
under this paradigm (though hopefully, with real returns in terms of
model utility, safety, etc.). And, we still need to answer a number of
technical and design questions to make attestation work.

While much of my previous writing has focused on Win 1, I'm excited
about all of these angles. (Of course this is the optimistic view -- see
the end of this post for a more negative set of "likely
objections".)

Most of this post will be aimed at motivating attestations across the
supply chain. I hope to write more in the future about realistic
pathways towards achieving this vision. I'll briefly note that there are
at least five ways to create incentives for attestations and that I do
think we have some viable low-hanging fruit in the policy space. On the
incentives side, the main channels I see are: direct mandates for some
kind of attestation in narrow high-stakes settings; pressure via
procurement rules from enterprise buyers and public bodies; asks from
insurers and other liability-sensitive counterparties; self-interest
from labs seeking product differentiation and/or anti-scraping
incentives; and direct user preference / consumer demand. There is
already real progress around auditing,
public
procurement guidance, and regulatory
transparency requirements. The clearest consumer-facing progress so
far is probably around output provenance via standards such as C2PA, and insurance has some early movement
from firms such as Marsh.

On the policy side, some "minimal asks" include: getting policymakers
to "bless" a small number of interoperable formats and a credible
process for deciding who counts as a verifier; requiring attestations in
certain contexts; disincentivizing bogus provenance and evaluation
claims using consumer protection tactics; and maintaining some data
protection and licensing "backdrop" since contributors are less likely
to participate in markets at all if the baseline expectation is still
that their work will simply be scraped and reused anyway.

Next, I'll describe roughly how I think buyers are choosing AI today
and why the current approach is incomplete. Second, I'll summarize the
state of play for upstream markets for training data and evaluation
labor. Third, I'll describe how interoperable attestation objects can
link contributions, evaluations, and outputs. Finally, I'll try to tie
the whole thing together by arguing that this kind of attestation layer
can improve incentives for buyers, labs, and knowledge workers. More
broadly, I want to show how these existing approaches can be treated as
parts of a common AI trust stack, and to argue that connecting them has
underappreciated consequences for market design, labor visibility, and
downstream product choice.

Because this post also revisits some points from earlier Data
Leverage posts and related references, I'll add an appendix at the end
briefly noting those connections.

Or put another way, this is yet another blog making the case
for data transparency and healthy market flow as a coalition-building
cause that can unite auditors, content creators, AI labs, and the
general public around a mutually beneficial set of
incentives.

#### Core assumptions behind
the proposal

The claims above rest on a core set of assumptions:

- Information is hard to price cleanly because it is largely non-rival
and often hard to exclude (see e.g. classical work from Arrow
on the economics of information and Jones and
Tonetti on the non-rivalry of data).

- Fine-grained data valuation is inherently challenging because small
units of data have influences that are very small in raw magnitude and
it is very expensive to acquire ground truth; value is usually more
legible when data is grouped into bundles or collectives (see e.g. work
on "data
dividends").

- Training data and evaluation data are not totally separate
substances so much as different uses of similar underlying human
knowledge work (see e.g. Deng et al. on
training/evaluation overlap via benchmark contamination for one
example of the overlap in practice).

- Output-only evaluation is useful but costly and incomplete,
especially for increasingly general systems (see e.g. Raji et al. on the
limits of "general" benchmarks and Liang et al. on holistic
evaluation and coverage gaps).

- Markets for upstream contributions likely need some kind of trusted
approach to data flow, not just shipping of raw bits, if contributors
are going to participate and capture value (see e.g. Castro Fernandez on auditable
data-sharing arrangements).

- Good faith open data strategies can conflict with efforts to empower
workers or collectives to bargain.

- Consumers, regulators, insurers, or other downstream decision-makers
will sometimes care enough about verified provenance to influence
decision-making around AI (see e.g. Brundage et
al. on frontier AI auditing and OpenAI's
health launch as an example of product-level signaling around physician
involvement and evaluation).

- In some important domains, transparency about model outputs
themselves -- not just the training process -- will increasingly be
expected or required.

- In at least some important domains, attested inputs and evaluation
processes will be meaningfully predictive of downstream quality, safety,
or trustworthiness.

With that overview in place, here's the longer argument:

### I.
The market problem: buyers of AI products can see outputs, but not the
chain behind them

Imagine someone who is choosing from a menu of AI products. Perhaps
this person is a consumer who just wants to use AI for small personal
projects ("help me build personalized note-taking software"), a
researcher seeking some occasional help with research tasks ("help me
debug this LaTeX issue"), a hobbyist software developer seeking to find
a tool to use heavily, somebody seeking a rigorously tested AI system
that can offer medical advice, or a company's CTO looking to make an
enterprise contract for org-wide AI access.

Across all these contexts and scales, a person buying an AI product
is (for now) mainly buying "information outputs" such as answers to
questions, documents that fulfill some requested purpose, or pieces of
code that can complete certain tasks. A user buys an AI subscription or
AI credits, and now can enter an input (a prompt/query) and get an
output. Modern frontier models can provide a dazzlingly varied set of
outputs: a single tool can first give you something like a search engine
results page, followed by a complex working piece of code, a working
spreadsheet, and then finally a poem and an accompanying piece of visual
art. Some systems are even agentic and can produce outputs that are
themselves actionable (e.g., the output is a series of actions, and then
the system performs some "actuation," often using the user's computer
and/or API keys).

Generally (and we'll get more precise about this later in the
article), we choose to spend money (perhaps a lot of money!) on AI if we
think those outputs will be "good" in some sense. We might think the AI
is good in a statistical sense because we inspected the outputs, or
because we read an evaluation study with robust evaluation of many
outputs, or because we make some assumptions about how an AI was
developed that make it "good." However, users could also consider facts
about how the model was built (such as information about the training
data).

If you are using AI to make personalized note-taking software, facts
about the training data may not be very high stakes. However, if we want
to buy an AI product to ask medical questions, we might care deeply
about both AI outputs and inputs to said AI. We most likely want to know
that a doctor has looked at some of the model's outputs and attested
they are "good"; we might also want to know that there were some inputs
from actual doctors such as content from medical textbooks and research
papers used in the development of the original model. Finally, when we
get a medically relevant output from an AI system -- e.g. the system we
paid to access has printed out some text telling us to take a medicine
or take some action -- we ideally want that output to be verifiably
linked to information about the evaluation of the model, and ideally the
training data as well.

### II.
How AI products are chosen today: four channels of evidence

If we look at the key factors that might cause someone shopping for
AI products today to pick one product over another, I think we can
bucket these into four groups. Put another way, most "AI buyer choices"
can be traced to evidence or beliefs from one of four channels of
information:

- the "outputs" channel. How good are the actual information outputs
from an AI system?

- the "inputs" channel. How were specific models used in an AI system
trained and how was the overall system developed?

- the "product" channel. Covers factors related to the delivery of the
information outputs: pricing, uptime, latency, UX, privacy/compliance,
support, lock-in, etc.

- the "internals" channel. Facts about model machinery, the channel
we're furthest from being able to make practical use of, but potentially
a very valuable channel.

The product channel matters a lot if you're buying an AI product
today. However, it's the channel I'll discuss the least in this post, in
part because the focus here is on data-related differentiation but also
because generally getting information about product factors currently
works pretty well and thus enables relatively healthy market dynamics.
We also won't talk much about the internals channel, e.g. making
decisions based on the results of interpretability-based studies, though
I think this will be increasingly important to think about going
forward. Instead, this essay focuses on the missing value of the inputs
channel, and on how attestations can connect inputs to outputs.

At present, I think most AI users are choosing primarily based on
beliefs about outputs plus some broad assumptions about inputs. Those
beliefs about outputs may range from "my friends told me Claude Code
outputs good code" to "I read the recent model cards" to "I run my own
private eval set." The corresponding assumptions about inputs are
usually something like: the frontier labs probably sourced strong data,
had capable people inspect and filter it, and used best-in-class
training practices.

That is often reasonable. Outputs matter most for many use-cases, and
if I only care about outputs, information about training is mainly
useful as a proxy for output quality. Still, distinguishing these
channels can improve AI literacy by more clearly separating the facts
about outputs and inputs that might drive consumer behavior. That helps
both consumers choose and developers differentiate.

### III. Why outputs
alone may not always be enough

How do we know if the information outputs from an AI system are good?
Let's return to our first example: imagine a user who is looking to buy
an AI product to help write personal note-taking software (and more
generally play around with AI-coded personal software). This user
probably plans to send a prompt to an AI model that looks something like
this: "write me the code for software I can use for daily note-taking"
(perhaps with a bit more detail regarding their personal preferences for
how the software should work).

Say this user can do a "trial run" and send this prompt to three
different AI providers, A, B, and C. How will this user decide which
provider product to buy?

#### Option 1: inspect outputs
yourself

One option would be to look at the output from each model and assess
the quality of that output. If the user is already an expert in this
domain, perhaps they can just read the code produced by all three models
and identify an obvious "best" model. Of course, if they wanted to have
some statistical rigor in evaluation they'd probably want to look at
more than one sample per model, though this will create some budgeting
challenges and basically means the user needs to conduct their own
benchmarking study. For a fuller treatment of the topic of looking at
model outputs statistically, see e.g. evalstats from Ian
Arawjo.

#### Option 2: rely on
published evaluations

Another option that also uses the outputs channel would be to look at
the results of an already published benchmarking study, either from the
model provider or from a third party. In this case, the user would
basically be making the assumption that "other people tried similar
inputs, and performance on those related tasks will probably proxy for
performance on the task I care about." Here the rigor of the benchmark
matters: how many total variants were tried, who checked that the output
worked, etc.

When AI developers themselves or third party evaluation organizations
produce a benchmarking study, the results of these studies will impact
the organizations' reputation, so generally we should expect these kinds
of studies to be reasonably consistent in terms of providing real
signal. Benchmarking will always be noisy, but over time, there are
incentives to evaluate models in ways that accurately reflect
differences in capabilities. In other words, this approach should be
pretty decent, and if we only ever have access to these kinds of signals
for consumer decision-making, we could sustain a reasonably efficient
market for AI products.

#### Option 3: rely on vibes
and reputation

A third option after "do your own evals" or "read the best recent
evaluation report" is to simply seek out a more general vibes-based
ranking for the "most intelligent" model or the "best" AI developer. I
think this is what many people are doing in practice right now, though
there is certainly a small population of power users who diligently run
their own personal benchmarking processes each time a new model
releases.

This approach is also not necessarily that ineffective. A vibes-based
approach likely does integrate reputation and social proof in a way that
matches other kinds of consumer decision-making and creates decent
outcomes. Not everybody needs to read the auditing deep cuts or full
review history for every product they buy.

What's interesting is that using vibes to generally rank AI companies
actually starts to mix information from the outputs channel and the
inputs channel, because people are making some assumptions about
training data and the training process itself. I think most people
choosing with vibes are indeed assuming that AI developers themselves
and third parties have evaluated the outputs of the model and found
those outputs to be good, and perhaps that AI developers have special
internal-only evaluation practices and employees that are especially
skilled at AI evaluation. But this approach likely also involves
assuming that the labs have used "best in class" training approaches,
have sourced the best data they can get their hands on, and have a large
team doing whatever they can to make models better. Critically,
vibes-based decision-making is not entirely inputs-agnostic, and it's
important to acknowledge this because I think it means people will care
about inputs in the long run.

#### The issues with current
status quo

However, this is also where we can start to envision some room for
improvement in the AI consumer experience. If consumers had more
specific knowledge about the inputs to an AI product, both broad facts
about the training data and facts about the evaluation process, this
could be useful to them. Even as underlying training techniques enable
models to become more general and more broadly intelligent, it seems
likely that the presence of certain types of data, data about certain
topics, and data from certain experts in model inputs will proxy for
output quality.

In the medical case, information about the outputs might be more
important. If sketchy training data leads to outputs that top doctors
give a thumbs up to, we might take that. And overemphasis on training
data may create metric chasing, e.g. including social media posts from
medical doctors in pre-training data to drive up the volume of tokens
from MDs. But input information should still provide some signal. Either
we want real medical data in the training set or we want solid evidence
our AI system has figured out medicine from first principles.

More broadly, both output studies and input details are proxies for
future quality. For statistical systems, that is often the best we're
going to get. The under-emphasized problem is that as models become more
general, comprehensive output evaluation across all the things they can
do becomes prohibitively expensive. Many people have commented on this;
see, for example, the "Evaleval" project and its "Every Eval
Ever" effort, Raji et al. on "everything in the whole wide
world benchmarking", and recent online discussions in which people
contrast their personal experience with a model and that model's
benchmark results.

The labor required to really, fully, comprehensively evaluate
increasingly general technologies will be very costly. We're going to
need a whole lot of doctors and scientists to give feedback on a whole
lot of LLM outputs to be sure we can use LLMs effectively in those
contexts. But we're also going to need a whole lot of general users,
with distinct combinations of niche interests, needs, preferences, etc.,
to give feedback as well. All this feedback will be relevant to
evaluation of current models, but also relevant to the training of new
models, the design of reinforcement learning environments, etc. It's
going to take time to do all this evaluation, and will in some sense
involve a kind of commandeering of the entire knowledge economy.

Simple napkin math suggests the relevant numbers get big quickly.
Suppose we want rigorous evaluation coverage across 30 major medical
specialties, with 1,000 representative cases per specialty, 10
independent physician reviews per case, and 30 minutes per review. That
is 300,000 physician judgments, or 150,000 physician-hours, for one pass
over one model version; at $200/hour for specialist time, that is about
$30 million just in doctor-review labor. And that is before benchmark
design, adjudication, compliance, or program management.

It's worth thinking about how many hours of physician labor you want
upstream of a chatbot prescribing your medicines!

Note that here I've focused on a running example of a consumer from
the general population. I think this story is useful, but you might be
thinking "I just don't believe consumers will care that much". You may
be right -- and critically, all the above argumentation applies directly
to the context of enterprise AI users, who have much more bargaining
power and are very likely to care about exactly all these issues
described above.

### IV.
What current "upstream markets" look like: deals, marketplaces, and
labor

Before an AI product is brought to market for consumers to consider,
developers must also participate in two important upstream markets:
acquiring training data and acquiring evaluations. Some companies may
get their training and evaluation data without direct outside
assistance, e.g. just scrape the training data and use in-house
employees to do evals, but I expect as the industry matures both of
these domains will become more market-like, with a broader set of data
sellers at the training level and evaluation providers to choose from.
Note here I'll sometimes use "data" a bit loosely to cover both training
inputs and evaluation labor, since both are forms of human knowledge
work that developers are trying to source.

There is already an informal market for evaluators. It is not yet as
legible or standardized as something like AWS Marketplace, but frontier
labs already hire or contract with domain experts, benchmark designers,
red teamers, and specialized third-party evaluators. Organizations like
METR and Apollo along with similar
evaluation and auditing groups, are early examples of a more specialized
evaluation layer emerging around frontier AI systems.

Now, let's step away from the perspective of someone picking between
AI products and instead consider a developer who wants data to build
their AI product, or a seller, either an individual or an organization,
looking to monetize their content.

#### Three current market forms

I'll bucket the ways we can buy training data and evaluation labor
right now into three broad categories. These are ideal types rather than
perfectly separate boxes, but they capture a lot of the current
landscape:

- Big licensing deals. These are bespoke boardroom
transactions: a lab or platform negotiates directly with a publisher,
forum, data broker, or other large rights-holder for access to a corpus
or feed. The deal terms are highly customized and usually cover things
like scope of use, refresh cadence, exclusivity, audit rights,
indemnity, and payment over time. An example would be Google
reportedly paying Reddit roughly $60M/year for access to Reddit
data, with Reddit separately disclosing in its S-1
that its January 2024 data licensing arrangements had an aggregate
contract value of $203M.

- Licensing via marketplace. This is more like online
shopping for large datasets. Instead of a bespoke negotiation, the
seller lists a relatively standardized product with a posted
description, delivery format, usage terms, and price, and the buyer can
compare options much more quickly. An example would be going to AWS
Marketplace to buy 12
months of "Anonymized, non-aggregated granular consumer-level data
across all asset classes" from Equifax for $175k. Economically, the
appeal here is lower transaction cost and easier comparison across
sellers, though the quality and rights picture may still require
substantial diligence.

- Pay individual people, per task or per hour, for data
outputs. This is the crowdwork or expert-labor bucket. Here the
buyer is not primarily acquiring a pre-existing corpus; they are paying
people to generate judgments, labels, rankings, reviews, or other
evaluative outputs under a specified protocol. An example might be
paying somebody via
Prolific at at least
$8/hr, and typically more like $12/hr to label web data, or paying
domain experts to peer review model outputs. This category matters
especially for evaluation, where the scarce input is often expert
attention rather than a static archive.

One nearby fourth form, if one wanted to break the taxonomy out
further, would be recurring API or feed access rather than transfer of a
bulk dataset: paying for ongoing, metered access to a live corpus or
stream. I think that form mostly collapses back into Categories 1 and 2
depending on how standardized the arrangement is, so I am leaving it as
an adjacent case rather than promoting it to a main bucket.

See also the data deals tracker here
from the authors of "A Sustainable AI Economy Needs Data Deals That Work
for Generators".

#### Collectives and
intermediaries

Another idea that's gained some popularity over the last decade is
the notion of joining a data cooperative, collective, union, or
intermediary. Generally, the idea here is that you join the coop,
contribute data, and some actor in the coop transacts in a market on
your behalf. In fact, there are some ways to join a data cooperative
today. Organizations such as Swash and Brave
Rewards monetize various online actions and tasks. The user bases of
data-coop-style tools are very small compared to general Internet usage.
For reference, Brave reported 101M monthly active users as of
September 30, 2025, while StatCounter has recently put Brave at
roughly 1%
of worldwide desktop browser share. Some of the means of
monetization, e.g. watching ads, are also quite different from an
aspirational vision of data markets in which data sellers are spending
their time crafting valuable documents and records and then being
rewarded for their contributions to shared epistemics. I do really
believe that a useful North Star is trying to shoot for a world in which
more overall human work looks like the good parts of journalism,
scientific peer review, editing Wikipedia, and participating in Q&A,
with the bad parts minimized or automated away.

While the above data cooperatives involve a technical approach to
enabling cooperation, and participation remains niche, I actually think
there is a lot of low-hanging fruit for applying the
collectives/coops/unions idea to the three types of markets described
above.

First, for the big boardroom deals, we could imagine pools of users
directly weighing in on the deal conditions. For example, when it comes
time for Reddit to renegotiate with Google or others, they loop users
in, either voluntarily or under threat of collective action. Second,
data coops can post their own quality-assessed CSV file for sale on AWS
Data Marketplace right now, but they still need social and technical
support to actually organize in the first place and produce a good CSV.
And there is a large body of work, including ongoing efforts, that aim
to support collective bargaining for data workers, see e.g. the body of
work from Dr. Saiph Savage and Data Workers' Inquiry from
DAIR.

One consideration is that successful organization of data workers may
actually involve a shift from crowdwork markets to collectives that sell
bundled data, i.e. moving more overall information from Category 3 to
Category 2, or even 1.

#### Two policy
levers: data protection and attestation

There is also an emerging set of actors interested in supporting
various forms of what we might term "data protection for the AI age". Cloudflare's
public support of anti-scraping is one example.

I think it is useful to start from a fairly grim baseline: many
people assume their data will be scraped, distilled, and reused unless
they actively block it through anti-scraping, anti-distillation,
poisoning, preference signals, legal enforcement, or some mix of
these.

In general, supporting data protection action can make it more likely
that data sellers will engage with markets rather than give up because
everything will be scraped anyway. In other words, some actor, public or
private, needs to do some level of policing for a market to emerge. This
is a bitter pill from an open-culture perspective, since open culture is
foundational to modern ML, including both peer production of critical
training data and open-source implementations of algorithms and tooling.
Still, there is likely a middle ground in which open culture continues
in many domains while others become more financialized. Any actions that
move us away from the current situation are probably net good in the
short term, though we should be cautious about a pendulum-swing-too-far
data-cartel scenario in which nobody can use any information without
paying.

Under an attestation-centered regime, data might still be readable or
even openly available, but what becomes scarce is the ability to make a
trusted downstream claim about provenance, licensing, evaluation, or
output identity. Scraping without the attestation may no longer be
enough to compete in markets where buyers, enterprise customers,
insurers, or regulators care about verified inputs and verified
outputs.

This is why attestation is particularly appealing for public AI
strategy. It suggests a path where openness and bargaining do not always
have to be direct opposites. In the strongest version, a dataset or
corpus might be free for research or public-interest AI use, while
commercial actors must pay if they want to rely on it in an attested
product or otherwise market the trusted provenance relationship. These
approaches are complements rather than substitutes: better data
protection may be needed to get participation off the ground, but
attestation changes the long-run market game by moving value toward
attestations rather than raw tokens.

### V. Why attestation
improves incentives

We need to address three fundamental constraints that affect value
measurement and value transfer in the context of AI:

- the economic
properties of information, non-rivalry and non-excludability, make
it very hard to create efficient markets for information. But if markets
attach value to attestations rather than bits, we may be able to have
our cake and eat it too: widely distribute information via AI as a
public good while retaining some of the coordinating benefits of
markets

- the value of data, as defined by any kind of data counterfactual estimation
method ("how does accuracy change if unit or bundle of data is
removed from training"), is generally small in raw magnitude unless data
is grouped together as some kind of collective

- open data can, in some cases, directly disempower certain subsets of
workers by making the relevant knowledge easier to copy than to bargain
over. An attestation layer offers one possible way to preserve some
openness while still giving those groups something commercially salient
to negotiate around

We could somewhat address these challenges by just trying to coarsely
distribute value to data creators: just worry less about provenance and
distribute resources through something like a data-dividend public
wealth fund. I think that may be a useful transitional approach in the
short term, but likely not the ideal end state.

#### Why AI buyers care

For buyers, the benefit is straightforward: inputs and outputs become
inspectable product features. Instead of relying only on benchmarks,
reputation, or vibes, a buyer could ask more specific questions: How
many credentialed authors contributed to training data? What process
verified their work? What upstream sources were actually licensed? Was
this particular output generated by a model version whose provenance and
evaluation records I can inspect? In higher-stakes domains, that still
does not replace output inspection, but it gives downstream choice much
more structure.

In some settings, we can expect transparency around model outputs
themselves to become a requirement rather than a premium feature. A
regulator or enterprise buyer may increasingly want not just "trust us"
but verifiable disclosure that a given artifact came from a given model
and from a model with a certain attested pedigree.

If those attestations become known to be predictive -- e.g. the AI
model with stronger attestations around its training data is actually
better at giving health advice -- they also reduce some of the appeal of
indiscriminate scraping or distillation. A rival might still imitate
outputs, but the attested relationship itself becomes part of what the
buyer is purchasing.

#### Why contributors and
collectives care

For creators, evaluators, and data workers, the important shift is
from selling anonymous tokens to participating in visible, renewable
labor relationships. Attestations for training and evaluation can be
managed and aggregated by some kind of intermediary, collective, or
union so people do not need to transact individually with AI
companies.

If verified attestations become important to consumers or regulators,
that would immediately bring more data work out into the open. It would
make it easier to treat these jobs as real careers and harder to treat
data workers as invisible or precarious labor. Note that while I've been
using doctors as a convenient running example -- a relatively small
group with easy credentials to verify and existing social infrastructure
for collective action -- the same logic applies to many other kinds of
knowledge work.

The economics of maintaining a trusted relationship are also very
different from the economics of acquiring tokens. The actual bundles of
information in training data are and will remain mostly non-rival, and
often hard to exclude. But contracts with people or collectives are not
just about buying rights to transfer bits. These are contracts for labor
which must be renewed and maintained. A world of data-with-attestations
is therefore a world with more ongoing relationships and more room for
bargaining.

#### Why labs,
regulators, and public AI builders care

For labs, credible attestation could become a meaningful source of
differentiation, though adopting any particular standard is a collective
action problem. This is where auditing, evaluation, and safety cases
begin to connect to regulation, insurance, procurement rules, and
industry self-governance.

The building blocks for this market already exist in the upstream
markets described above. The main difference with attestations is that
the fact a person made or evaluated some portion of the data would no
longer be hidden, but rather made prominent. If an AI builder who uses
attested or full-consent data early on is able to produce good models
and prove that buyers care about those records, that creates pressure
for other AI developers to play along as good-faith actors in the
market.

An immediate downside for some labs is that data and evaluation may
cost more.

A version of an attestation-based provenance system that gets things
really right could be good for AI developers, data creators who want to
add knowledge via pretraining, content creators who want to be rewarded
when their content is retrieved, public-interest model builders who want
to distinguish civic from purely commercial use, and people who want to
use AI to produce things and sell them, e.g. software developers selling
vibe-coded software. In the strongest version, the flow of attested data
and AI outputs also becomes a governance lever, in the sense that
healthy markets for anything act as both a kind of computation over
preferences and a kind of governance.

### VI. Implementation and
caveats

#### Enforcement
will be partly technical and partly social

Here I've talked in broad strokes about attestation, provenance, and
verification a bunch, but have remained relatively agnostic to any
particular implementation details. Attestation and verification will
involve a mix of technical and social means of enforcement. They might
lean more heavily on technical innovations, e.g. new approaches for
embedded cryptographic signatures, or more heavily on social forces,
e.g. organizations that enforce attestations through reputation.

At a high level, there are at least six areas of existing/ongoing
work that could support attestation:

- C2PA
is, I think, currently the closest technical analogue. It already
supports signed provenance for AI/ML models, training datasets, outputs,
fine-tuning, and versioned releases. If one wanted to implement parts of
this proposal tomorrow, C2PA is an obvious place to start.

- in-toto and
SLSA provide a generic
supply-chain pattern for authenticated statements about subjects,
materials, builders, and verification.

- The web3 and verifiable-credentials worlds have also spent years
experimenting with portable attestations, signed claims, and selective
disclosure. I do not think AI provenance needs blockchains by default,
but that design space is still relevant as a source of ideas about
interoperable attestations. See e.g. Attest.

- Model
cards, datasheets,
and related documentation frameworks make model and dataset facts
legible via standardized processes.

- Frontier AI
auditing focuses on institutional assurance: who gets access, what
independence standards matter, what level of assurance an audit
provides, and how results should be communicated.

- Data licensing explores the
contractual layer around who can use what data, for which purposes, and
under what terms. That layer is not itself an attestation format, but it
helps define the claims an attestation system would need to make legible
and enforceable.

#### How we might
transition towards attestations

Recent trends in dataset documentation suggest a world of transparent
data for AI models is not yet around the corner. Dataset details in
model and system cards remain extremely short and vague, as reflected in
the Foundation
Model Transparency Index, and understandably are likely to remain
short and vague until additional legal clarity is achieved. That said,
for both researchers and consumers, it will be very valuable to keep an
eye out for new open releases, such as models from EleutherAI, AI2, and academic groups (see e.g.
recent work from Fan et
al. on model training using highly compliant web data).

But critically, almost all the actions that data protectors might
take now, including developing and offering anti-scraping technologies,
helping to socialize anti-scraping and AI preference signals, and
supporting related research on data value estimation, full-consent LLMs,
partnerships with national labs, etc., are likely to also make it easier
to work toward attested data.

### Appendix
I: how this proposal connects to earlier posts

This appendix is optional background for returning readers (and so I
can keep track of what points I've been making in too many distinct
blogs!). It shows how the proposal connects back to the "quasi-enclosure"
piece (itself a follow-up to "tipping
points"), the "data
rules" piece, and an earlier
series
of
posts discussing evaluation and data labor.

#### On "quasi-enclosure" and
"tipping points"

Those posts argued that AI can increase useful knowledge work while
still routing the resulting data into private pools, creating a
precarious quasi-enclosure and raising the risk of content-ecosystem
tipping points. If labs compete partly on verifiable claims about who
contributed, who evaluated, and under what terms, then some of the value
currently captured silently through closed transcript pools can instead
flow through explicit labor relationships, collective bargaining, and
public-facing quality claims. That does not solve the commons problem by
itself, but it does create a more plausible "golden path" in which AI
products remain broadly useful while preserving stronger incentives for
the people and institutions that keep producing the knowledge those
systems depend on. To retain the benefits of maintaining knowledge
commons in general, we also need interventions and social norms aimed
explicitly at maintaining those commons.

#### On "data rules"

The "data rules" piece argued for clearer and more enforceable
options governing how data can be used across training, retrieval, and
evaluation, in ways that help both creators and model builders.
Attestation is one way to make such rules practical. A rule only matters
if someone can later verify what happened: whether a dataset was
licensed for training but not evaluation, whether an evaluation set was
kept separate from training, whether a model output can be linked back
to a model version and a body of supporting evidence. In that sense,
attestation is not a rival proposal to clearer data rules; it is one
concrete way to operationalize them.

Of particular note: designing a schema for attestation could help to
surface the types of contracts available to data creators and AI
developers.

#### On "selling AGI like AG1"

That post argued that as AI products get more expensive, buyers will
want more than vibes and vague claims about "more intelligence". The
attestation proposal gives a direct answer to that consumer problem.

#### On the evaluation-related
posts

The earlier evaluation posts argued that output evaluation is costly,
incomplete, and increasingly central as models become more general. They
also argued that evaluation labor itself could become a major site of
bargaining power. The attestation proposal follows up on these ideas. An
evaluation attestation can say who did the work, what they reviewed, how
much they reviewed, and under what process. That helps buyers interpret
quality claims, but it also helps workers and collectives bargain over
the provision of evaluation labor because the work is more visible.

### Appendix II: objections and
replies

#### Q: What
if buyers simply do not care about attestations?

A: This is one strong practical objection. If most buyers continue to
choose AI products based mainly on outputs, price, latency, UX, and
enterprise features, then attestations will not do much work on their
own. Attestations definitely will not magically displace those factors,
but they can become additional decision-relevant signal, especially in
higher-stakes domains and in procurement settings where compliance,
liability, and reputation matter. If consumer and enterprise demand
never materializes, then the proposal likely depends much more heavily
on regulation, insurance, or industry self-governance than on pure
market pull. See the short discussion in the intro about practical
incentives.

#### Q:
Couldn't this cause people to confuse provenance with "explainability"
or "justification"?

A: Definitely possible. A provenance chain is not the same thing as a
causal explanation of why a specific output is correct. Knowing that
doctors contributed to training data or reviewed some model outputs does
not by itself prove that a particular medical answer is trustworthy. The
point of attestation is therefore not to replace epistemic validation,
but to supplement it. It gives buyers more information about the system
behind an output, not a complete proof that any one answer is right.

A critical part of making this system work would be ensuring that the
organizations participating in the attestation chain (e.g., medical
organizations) ensure that attestations are, for the most part,
epistemically valid.

#### Q:
Won't companies just game the metrics once "attested inputs" become a
selling point?

A: They might. If the market starts rewarding visible counts like
"number of doctors involved" or "number of licensed sources," firms will
have incentives to optimize for what is easiest to attest rather than
what most improves the system. That is a classic Goodhart problem. The
best response is to design attestations carefully! Even then, some
gaming pressure is inevitable.

And similarly, this issue can be partially solved by ensuring that
the organizations providing attestations have an incentive to keep their
attestations aligned with "real value" in their domain. Or put another
way, if medical organizations continue to police the medical competence
of their members, the approaches for this kind of organizational quality
control can be used to combat metric gaming.

#### Q:
Doesn't this just move trust from AI labs to auditors and
certifiers?

A: In part, yes. Any attestation regime creates a new bottleneck
around whoever verifies claims. That raises familiar worries about
certification cartels, regulatory capture, and barriers to entry for
smaller labs or open projects. Regulators and consumers will both have
to continue contributing to governance questions around who gets to be
trusted as a verifier and under what standards.

#### Q:
How can useful attestations coexist with privacy, secrecy, and
anti-gaming concerns?

A: There is a genuine tension here. If attestations are highly
specific, they may reveal private contributor information, proprietary
dataset composition, or evaluation details that make benchmarks easier
to game. If they are too vague, they collapse into branding or marketing
copy. There is no perfect resolution. The practical goal is likely to be
selective disclosure: enough specificity to support meaningful external
checking, without assuming that every contributor identity, dataset row,
or eval item can be made public.

New research may also make this question less of a concern.

#### Q:
Why would attestation reduce scraping or distillation if a rival can
still match output quality?

A: If a competitor offers similar or better outputs at lower cost,
many buyers will still switch regardless of cleaner provenance. A more
modest claim is that attestation can create some product differentiation
and make fully consent-based development more legible, not that it
eliminates the economic pull of imitation. Scraping and distillation
remain live incentives unless buyers, regulators, or counterparties
attach real value to the attested relationship itself, whether that
relationship concerns training data, retrieval sources, evaluation
labor, or the identity of the output-producing model.

Importantly: for something like health advice, people are paying, in
part, for some amount of confidence or peace of mind. Here, the presence
of attestations really matters and makes a material difference between
model A with attestations and model B with very similar outputs but no
attestations.

#### Q:
Does visibility alone actually create bargaining power for
contributors?

A: Not by itself. Making data work legible is not the same thing as
guaranteeing payment, better labor conditions, or stronger negotiating
leverage. Those outcomes also require institutions that can enforce
terms, whether through law, contracts, unions, collectives, or platform
governance. Attestation can make bargaining easier by making
contributions auditable and portable, but it does not substitute for the
underlying political and organizational work.

### Appendix
III: a simple attestation schema for AI inputs, evaluations, and
outputs

Here is one toy worked example of a concrete schema. This sketch
borrows from several existing approaches described above. I expect this
section to be made pretty redundant by future "full spec docs", but I
think it's clarifying to include some toy examples alongside this
post.

#### Design goals

The object model should:

- work across training, evaluation, and output provenance

- support both human-readable and machine-readable claims

- allow signatures or other authenticated proofs

- stretch goal: allow selective disclosure, since full public
disclosure of contributors, datasets, or eval items will often be
impossible

- support both individuals and organizations as contributors,
attesters, and verifiers (but likely prefer organizations)

- make it easy to traverse links from an output to a model version,
from the model version to evaluation records, and from there to upstream
contributions

#### Minimal outer wrapper

At a high level, the same outer structure can be reused even when the
subject matter changes:

{
"schema_version": "0.1",
"object_type": "training_contribution",
"subject": {
"kind": "dataset_shard",
"id": "med-001"
},
"attester": {
"kind": "publisher",
"id": "licensed-med-publisher"
},
"contributor": {
"kind": "author",
"credential": "MD"
},
"claim": {
"statement": "A credentialed contributor supplied content used in model development."
},
"evidence": {},
"verifier": {
"kind": "third_party_auditor",
"id": "auditor-a"
},
"timestamp": "2026-04-08T00:00:00Z",
"links": {},
"signatures": [],
"disclosure": {
"public": true
}
}

- schema_version: version of this logical schema, not
necessarily the wire format version

- object_type: claim family, such as
training_contribution, evaluation_record,
output_provenance, downstream_use, or one of
the auxiliary types below

- subject: the dataset shard, model, model version,
evaluation artifact, or output being described

- attester: the entity making the attestation

- contributor: the person or organization whose role is
being attested, if different from the attester

- claim: the substantive statement being made

- evidence: artifacts, counts, references, hashes,
licenses, reports, or other support for the claim

- verifier: the party, process, or assurance mechanism
that makes the claim more trustworthy

- timestamp: issuance time

- links: pointers to upstream or downstream objects

- signatures: cryptographic signatures or references to
them

- disclosure: what is public, redacted, or privately
available to auditors only

The wire format does not have to be this JSON shape. The same logical
object could be encoded using a C2PA manifest, an in-toto statement plus
predicate, or another signed envelope.

#### Suggested object types

The four core user-facing object types are:

- training_contribution: a claim about upstream data,
labor, or licensed content used in model development

- evaluation_record: a claim about who evaluated what,
under what protocol, and with what sample size or assurance process

- output_provenance: a claim that a specific output came
from a specific model version and can be linked back to relevant
evaluation and training records

- downstream_use: a claim that a downstream artifact,
workflow, or organization used a specific model or model version in
producing some later output

Two plausible auxiliary types are:

- model_release: a claim about a model version,
checkpoint lineage, deployment status, or serving identity

- credential_attestation: a claim about contributor
qualifications, institutional affiliation, or eligibility to participate
in a class of work

#### Toy examples

##### Training contribution

{
"schema_version": "0.1",
"object_type": "training_contribution",
"subject": {
"kind": "dataset_shard",
"id": "med-042"
},
"attester": {
"kind": "publisher",
"id": "licensed-med-publisher"
},
"contributor": {
"kind": "author",
"credential": "MD",
"organization": "licensed medical publisher"
},
"claim": {
"statement": "A peer-reviewed cardiology chapter authored by a credentialed physician was included in licensed corpus shard med-042.",
"usage": "pretraining"
},
"evidence": {
"artifact_id": "chapter-8841",
"license_id": "license-332"
},
"verifier": {
"kind": "third_party_auditor",
"id": "auditor-a"
},
"timestamp": "2026-04-08T00:00:00Z",
"links": {
"downstream_model_run": "model-x-pretrain-run-07",
"downstream_model": "model-x-2026-03-15"
},
"signatures": [
"sig:licensed-med-publisher:abc123"
],
"disclosure": {
"public": true,
"auditor_only_fields": []
}
}

##### Evaluation record

{
"schema_version": "0.1",
"object_type": "evaluation_record",
"subject": {
"kind": "model_version",
"id": "model-x-2026-03-15"
},
"attester": {
"kind": "evaluation_org",
"id": "eval-lab-1"
},
"contributor": {
"kind": "reviewer",
"credential": "MD",
"experience_years": 20
},
"claim": {
"statement": "A practicing physician reviewed 100 outputs across 10 health-related tasks.",
"task_set": "health-general-v2"
},
"evidence": {
"sample_size": 100,
"hours": 100,
"report_id": "eval-report-77"
},
"verifier": {
"kind": "assurance_process",
"level": "independent-third-party"
},
"timestamp": "2026-04-08T00:00:00Z",
"links": {
"benchmark_report": "eval-report-77",
"related_model": "model-x"
},
"signatures": [
"sig:eval-lab-1:def456"
],
"disclosure": {
"public": true,
"auditor_only_fields": [
"sampled_output_ids"
]
}
}

##### Output provenance

{
"schema_version": "0.1",
"object_type": "output_provenance",
"subject": {
"kind": "model_output",
"id": "response-abc123"
},
"attester": {
"kind": "model_provider",
"id": "provider-y"
},
"claim": {
"statement": "This output was generated by model-x version 2026-03-15."
},
"evidence": {
"request_hash": "req-8fd2",
"model_version": "model-x-2026-03-15"
},
"verifier": {
"kind": "provider_signature",
"id": "provider-y-signing-key"
},
"timestamp": "2026-04-08T00:00:00Z",
"links": {
"model": "model-x",
"evaluation_attestations": [
"eval-report-77"
],
"training_attestations": [
"train-attest-8841"
]
},
"signatures": [
"sig:provider-y:ghi789"
],
"disclosure": {
"public": true
}
}

##### Downstream use

{
"schema_version": "0.1",
"object_type": "downstream_use",
"subject": {
"kind": "software_release",
"id": "health-app-v12"
},
"attester": {
"kind": "developer",
"id": "health-app-studio"
},
"claim": {
"statement": "This iPhone health app release used GPT-6.0-med1000 during development.",
"usage": [
"code_generation",
"documentation_drafting"
]
},
"evidence": {
"build_id": "ios-build-991",
"model_version": "gpt-6.0-med1000"
},
"verifier": {
"kind": "workflow_log",
"id": "build-pipeline-attestor"
},
"timestamp": "2026-04-08T00:00:00Z",
"links": {
"model": "gpt-6.0-med1000",
"related_outputs": [
"response-abc123"
]
},
"signatures": [
"sig:health-app-studio:jkl012"
],
"disclosure": {
"public": true
}
}

If objects like these are interoperable, a buyer or auditor can
move:

- from a downstream app, document, or answer to a declared model
use

- from that use record to the serving model version

- from the model version to evaluation records

- from evaluation records and model lineage to upstream
contributions

Source revision history

Selected Git commits that changed this source file.

- 9fb4674b8a 2026-07-12 - Migrate blog into digital presence monorepo

Mirror freshness

Maintenance status for tracked full-copy mirrors of this post.

-
Current
substack

mirror 2026-04-08

Baseline from original_url

Source and AT Protocol record

Source path
content/writing/posts/2026-04-08-1746-attestation-across-the-ai-supply-chain.md

AT Protocol URI
at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.document/3mizn5hsjg5vo

Exact public AT Protocol record cached for the Leaflet/Bluesky-facing copy.

{
"uri": "at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.document/3mizn5hsjg5vo",
"cid": "bafyreie6vt37ual6c2idie2k2dhlpjqdyahnuaayrxsd6f6v57grzn7tse",
"value": {
"path": "/3mizn5hsjg5vo",
"site": "at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.publication/3lzrsw2kvwc2m",
"$type": "site.standard.document",
"title": "Attestation across the AI Supply Chain",
"content": {
"$type": "pub.leaflet.content",
"pages": [
{
"$type": "pub.leaflet.pages.linearDocument",
"blocks": [
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 142,
"byteStart": 0
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "April 27, 2026: I made some edits throughout to condense this longer post and improve flow. I also wrote this additional bullet point summary:"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "I am feeling hopeful that momentum in the AI evaluation space can help improve data markets and data ecosystems more broadly. I wrote a longer post on the reasons why, currently framing this as “attestations across the AI supply chain”. Here’s the bullet point summary:"
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
"plaintext": "Some AI users (public bodies, enterprise users, picky consumers) and other parties (regulators, insurers) are going to, or have already started to, demand some kind of “attestation objects” in the domain of AI evaluation."
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "These buyers want some kind of proof that a model was evaluated; evaluation organizations are already beginning to document and share their evaluations"
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "An attestation that a certain evaluation procedure was performed could be similar to, and interconnected with, other kinds of attestations across the AI supply chain."
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "One related attestation could say that a certain piece of data was used to train a model."
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "One related attestation could say that a certain piece of information was retrieved and used at inference time."
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "One related attestation could say that a certain information object (sequence of output tokens) really came from a certain model."
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "One related attestation could say that a piece of AI-assisted output (e.g. downstream code) came from a certain AI output."
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "On the technical side, we should make it easy for these pieces of information to be linked to each other. They can support a “full picture” of AI supply chain provenance"
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "The technology needed here is actually relatively simple: registries for the attestation objects, techniques for verification, and appropriate privacy-preserving ways to share registries and associate people and organizations with attestation objects"
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Full supply chain provenance can be a product differentiator for AI developers that helps to combat model extraction/distillation"
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "The existence of more “guilds” who act as sellers in markets for attested evaluation and training data can provide important incentives to their members (knowledge workers of all types) to maintain quality and expertise; this can align incentives so that these guilds provide a resisting force against overreliance and slop"
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "What does this suggest we do?"
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "On the social side, we should try to create more demand for all these kinds of attestations; we should definitely leverage momentum and energy around evals"
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "On the policy side, we should look for opportunities to incentivize attestation and to make interoperable schemas and cross-talk easy"
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "In total, I think there are at least five distinct forces that could create demand for attestations: gov’t regulation, anti-distillation, procurement requirements, AI insurers, consumer demand."
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "If any of these succeed in creating real demand, this will enable markets for attested relationships instead of markets for “raw tokens”. This would be great for society because it can bypass some “core” information economics challenges with markets for information and likely create healthier overall data flow dynamics."
}
}
]
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.horizontalRule"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "This post argues that a shared family of attestation objects could improve several markets across the AI supply chain: consumer choice among AI products, upstream markets for training and retrieval data, markets for audits and evaluations, and downstream markets for AI-assisted artifacts. Broadly, I'll use the term \"attestation object\" here to refer to a verifiable record about who contributed what, in what role, to which model or output, under what validation process. We can enable this \"shared family\" by making progress on the design of an appropriate schema for the objects (technical/protocol work), the implementation of supporting policy and regulation, and by building relevant platforms that enable markets for attested evaluation and other data."
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
"byteEnd": 285,
"byteStart": 281
},
"features": [
{
"uri": "https://spec.c2pa.org/specifications/specifications/2.3/ai-ml/ai_ml.html",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 223,
"byteStart": 203
},
"features": [
{
"uri": "https://www.averi.org/ourwork/frontier-ai-auditing",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 196,
"byteStart": 181
},
"features": [
{
"uri": "https://www.dataprovenance.org/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 175,
"byteStart": 164
},
"features": [
{
"uri": "https://research.google/pubs/model-cards-for-model-reporting/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 162,
"byteStart": 152
},
"features": [
{
"uri": "https://arxiv.org/abs/1803.09010",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "The ideas discussed here build on work already underway in at least three adjacent areas: the dataset documentation space (inclusive of efforts such as datasheets, model cards, and data provenance); the Frontier AI Auditing world; and the content authenticity and provenance (e.g. C2PA) world. If we get the design of attestation objects right, interoperable schemas could improve visibility and traceability across training, evaluation, and usage."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "I am especially excited about the broad idea here because progress in one part of the AI supply chain can bootstrap progress in others. Existing momentum around audits could foster more training data transparency and better markets for training and retrieval data. Parties interested in provenance for AI-generated outputs, such as people assessing AI-generated code, could help promote transparency upstream. And if communities adopt norms around transparent AI usage, that may drive further demand for transparency up the chain."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Specifically, as of April 2026, I think evaluation as a field has much more momentum, attention, and funding than advocacy around training data documentation or retrieval markets, and thus I think is the most likely \"entry point\" that can enable full-chain provenance."
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
"byteEnd": 206,
"byteStart": 178
},
"features": [
{
"uri": "https://openai.com/index/introducing-chatgpt-health/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "I'll note that, in addition to momentum around auditing, we're starting to see some evidence that consumers might care about attestations for AI products. See, for instance, the \"Introducing ChatGPT Health\" blog post, which emphasizes working with \"260 physicians who have practiced in 60 countries and dozens of specialties\" to obtain \"feedback on model outputs over 600,000 times across 30 areas of focus\". I'll refer to attestation in the context of an AI health application as a running example throughout."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "One reason I think that discussing attestation matters right now is that data policy conversations often involve two somewhat different strategies for improving data markets. \"Data protection\" strategies are focused on trying to stop scraping, distillation, or reuse through a combination of law, platform rules, anti-scraping, and poisoning; all these serve to incentivize market participation by introducing friction and means to exclude information. An \"attestation-forward\" strategy tries to get AI users and/or regulators to care about verified provenance relationships upstream of AI products. These approaches can complement each other (in the short term, effective data protection may produce more pressure to get attestations working) but also likely benefit from somewhat divergent policy approaches. Data protection efforts try to block unwanted scraping and distillation; attestation efforts that succeed in making verified provenance, evaluation, and output identity matter could make \"just scraping anyway\" less valuable."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Very concretely, an attestation-forward data strategy would involve roughly four broad types of attestation objects:"
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
"byteEnd": 23,
"byteStart": 2
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#bold"
}
]
}
],
"plaintext": "a training contribution object: \"I am a medical doctor and I attest that I authored a textbook chapter and agreed to include it in the ChatGPT Health training dataset.\""
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
"byteStart": 3
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#bold"
}
]
}
],
"plaintext": "an evaluation record object: \"I am a medical doctor working with an AI evaluation organization and I attest that I reviewed 100 ChatGPT Health outputs and believe they represent standard of care.\""
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
"byteStart": 3
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#bold"
}
]
}
],
"plaintext": "an output provenance object: \"OpenAI as an organization attests that this output telling you to take more Advil came from the GPT-6.0-med1000 model.\""
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
"byteStart": 2
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#bold"
}
]
}
],
"plaintext": "a downstream use object: \"I am a vibe-coder making an iPhone health app and I attest that I used GPT-6.0-med1000 while building this app.\""
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
"plaintext": "Here's a short version of the key claims that motivate an attestation-forward strategy:"
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
"plaintext": "Users buying AI products, AI developers buying data, anyone commissioning audits, and anyone consuming AI-generated outputs face a related set of issues stemming from information asymmetry and lack of information generally."
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
"byteEnd": 178,
"byteStart": 157
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
"byteEnd": 147,
"byteStart": 132
},
"features": [
{
"uri": "https://www.apolloresearch.ai/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 130,
"byteStart": 126
},
"features": [
{
"uri": "https://metr.org",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 100,
"byteStart": 91
},
"features": [
{
"uri": "https://www.averi.org/ourwork/frontier-ai-auditing",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "The auditing and evaluation space has significant momentum; at present, there is an active ecosystem of third parties such as METR, Apollo Research, and the AI Security Institute providing attested evaluations of frontier models."
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "For users looking to pay for AI products, there remain challenges in DIY benchmarking of models. It also remains challenging for consumers to interpret benchmarks and evaluations. Finally, consumers are stuck mainly making decisions based on model outputs alone; there are currently few opportunities for consumers to incorporate facts about model inputs into their decision-making."
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
"byteEnd": 268,
"byteStart": 258
},
"features": [
{
"uri": "https://research.brickroad.network/neurips2025-data-deals",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "For developers looking to pay for data in AI markets, there are core market design challenges that stem from the non-rivalry and non-excludability of information alongside practical challenges with fine-grained assessment of data value. Markets for data are fragmented, opaque, and inefficient at the moment."
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Each stage of the AI supply chain could, in theory, involve attestations from key actors. Data creators can attest that they included their data in training sets. Auditors can attest to their participation in evaluation processes. Model outputs can include attestation objects that help people verify that a given output really came from a certain model, and in some domains that kind of output transparency may itself become required. And downstream artifacts can bundle all these attestations together via flow-down."
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
"plaintext": "If the schema for attestation and provenance can be synchronized across the supply chain, we can achieve a win-win-win-win:"
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
"plaintext": "Win 1: For data creators and buyers, we might establish healthier markets for training data that emphasize attestation objects rather than raw tokens. Upstream data markets would rely less on winning the constant battle between data protectors versus data extractors (inclusive of various approaches for scraping and distillation), and would more easily accommodate arrangements that preserve research or public-interest use while still giving workers or collectives something to bargain over."
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Win 2: For auditors, we can help increase demand for high quality audits and create standardization around benchmarking and evaluation. Better provenance for the full supply chain should also make auditing itself easier."
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Win 3: For labs, we can make it easier to sell model outputs without being undercut by distilled models."
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Win 4: For people consuming content, we can provide means to verify content authenticity. More generally, people can use all of this upstream information to help them assess AI-generated content of all types. This would help end-users who just want to read an AI output to answer a question and people who want to use AI outputs for other things (e.g., to sell AI-produced software)."
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
"plaintext": "The main downside -- the answer to \"why aren't we literally doing this today if it's so good?\" -- is that attestation will impose new costs on various actors. Training and evaluation labor may cost more under this paradigm (though hopefully, with real returns in terms of model utility, safety, etc.). And, we still need to answer a number of technical and design questions to make attestation work."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "While much of my previous writing has focused on Win 1, I'm excited about all of these angles. (Of course this is the optimistic view -- see the end of this post for a more negative set of \"likely objections\".)"
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
"byteEnd": 1038,
"byteStart": 1033
},
"features": [
{
"uri": "https://www.marsh.com/en-gb/services/risk-analytics/expertise/ai-system-risk-analysis.html",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 974,
"byteStart": 970
},
"features": [
{
"uri": "https://c2pa.org/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 864,
"byteStart": 828
},
"features": [
{
"uri": "https://digital-strategy.ec.europa.eu/en/faqs/navigating-ai-act",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 822,
"byteStart": 795
},
"features": [
{
"uri": "https://www.whitehouse.gov/wp-content/uploads/2024/03/M-24-10-Advancing-Governance-Innovation-and-Risk-Management-for-Agency-Use-of-Artificial-Intelligence.pdf",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 793,
"byteStart": 785
},
"features": [
{
"uri": "https://www.averi.org/ourwork/frontier-ai-auditing",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Most of this post will be aimed at motivating attestations across the supply chain. I hope to write more in the future about realistic pathways towards achieving this vision. I'll briefly note that there are at least five ways to create incentives for attestations and that I do think we have some viable low-hanging fruit in the policy space. On the incentives side, the main channels I see are: direct mandates for some kind of attestation in narrow high-stakes settings; pressure via procurement rules from enterprise buyers and public bodies; asks from insurers and other liability-sensitive counterparties; self-interest from labs seeking product differentiation and/or anti-scraping incentives; and direct user preference / consumer demand. There is already real progress around auditing, public procurement guidance, and regulatory transparency requirements. The clearest consumer-facing progress so far is probably around output provenance via standards such as C2PA, and insurance has some early movement from firms such as Marsh."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "On the policy side, some \"minimal asks\" include: getting policymakers to \"bless\" a small number of interoperable formats and a credible process for deciding who counts as a verifier; requiring attestations in certain contexts; disincentivizing bogus provenance and evaluation claims using consumer protection tactics; and maintaining some data protection and licensing \"backdrop\" since contributors are less likely to participate in markets at all if the baseline expectation is still that their work will simply be scraped and reused anyway."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Next, I'll describe roughly how I think buyers are choosing AI today and why the current approach is incomplete. Second, I'll summarize the state of play for upstream markets for training data and evaluation labor. Third, I'll describe how interoperable attestation objects can link contributions, evaluations, and outputs. Finally, I'll try to tie the whole thing together by arguing that this kind of attestation layer can improve incentives for buyers, labs, and knowledge workers. More broadly, I want to show how these existing approaches can be treated as parts of a common AI trust stack, and to argue that connecting them has underappreciated consequences for market design, labor visibility, and downstream product choice."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Because this post also revisits some points from earlier Data Leverage posts and related references, I'll add an appendix at the end briefly noting those connections."
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
"byteEnd": 259,
"byteStart": 0
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#bold"
}
]
}
],
"plaintext": "Or put another way, this is yet another blog making the case for data transparency and healthy market flow as a coalition-building cause that can unite auditors, content creators, AI labs, and the general public around a mutually beneficial set of incentives."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 3,
"facets": [],
"plaintext": "Core assumptions behind the proposal"
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
"byteEnd": 50,
"byteStart": 39
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#italic"
}
]
}
],
"plaintext": "The claims above rest on a core set of assumptions:"
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
"byteEnd": 211,
"byteStart": 167
},
"features": [
{
"uri": "https://www.aeaweb.org/articles?id=10.1257/aer.20191330",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 162,
"byteStart": 125
},
"features": [
{
"uri": "https://www.nber.org/books-and-chapters/rate-and-direction-inventive-activity-economic-and-social-factors/economic-welfare-and-allocation-resources-invention",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Information is hard to price cleanly because it is largely non-rival and often hard to exclude (see e.g. classical work from Arrow on the economics of information and Jones and Tonetti on the non-rivalry of data)."
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
"byteEnd": 297,
"byteStart": 283
},
"features": [
{
"uri": "https://www.nickmvincent.com/static/eaamo_data_dividends.pdf",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Fine-grained data valuation is inherently challenging because small units of data have influences that are very small in raw magnitude and it is very expensive to acquire ground truth; value is usually more legible when data is grouped into bundles or collectives (see e.g. work on \"data dividends\")."
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
"byteEnd": 219,
"byteStart": 149
},
"features": [
{
"uri": "https://aclanthology.org/2024.naacl-long.482/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Training data and evaluation data are not totally separate substances so much as different uses of similar underlying human knowledge work (see e.g. Deng et al. on training/evaluation overlap via benchmark contamination for one example of the overlap in practice)."
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
"byteEnd": 221,
"byteStart": 168
},
"features": [
{
"uri": "https://arxiv.org/abs/2211.09110",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 163,
"byteStart": 114
},
"features": [
{
"uri": "https://openreview.net/forum?id=j6NxpQbREA1",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Output-only evaluation is useful but costly and incomplete, especially for increasingly general systems (see e.g. Raji et al. on the limits of \"general\" benchmarks and Liang et al. on holistic evaluation and coverage gaps)."
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
"byteEnd": 246,
"byteStart": 191
},
"features": [
{
"uri": "https://doi.org/10.1145/3589317",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Markets for upstream contributions likely need some kind of trusted approach to data flow, not just shipping of raw bits, if contributors are going to participate and capture value (see e.g. Castro Fernandez on auditable data-sharing arrangements)."
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Good faith open data strategies can conflict with efforts to empower workers or collectives to bargain."
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
"byteEnd": 322,
"byteStart": 215
},
"features": [
{
"uri": "https://openai.com/index/introducing-chatgpt-health/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 210,
"byteStart": 171
},
"features": [
{
"uri": "https://www.averi.org/ourwork/frontier-ai-auditing",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Consumers, regulators, insurers, or other downstream decision-makers will sometimes care enough about verified provenance to influence decision-making around AI (see e.g. Brundage et al. on frontier AI auditing and OpenAI's health launch as an example of product-level signaling around physician involvement and evaluation)."
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "In some important domains, transparency about model outputs themselves -- not just the training process -- will increasingly be expected or required."
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "In at least some important domains, attested inputs and evaluation processes will be meaningfully predictive of downstream quality, safety, or trustworthiness."
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
"plaintext": "With that overview in place, here's the longer argument:"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "I. The market problem: buyers of AI products can see outputs, but not the chain behind them"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Imagine someone who is choosing from a menu of AI products. Perhaps this person is a consumer who just wants to use AI for small personal projects (\"help me build personalized note-taking software\"), a researcher seeking some occasional help with research tasks (\"help me debug this LaTeX issue\"), a hobbyist software developer seeking to find a tool to use heavily, somebody seeking a rigorously tested AI system that can offer medical advice, or a company's CTO looking to make an enterprise contract for org-wide AI access."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Across all these contexts and scales, a person buying an AI product is (for now) mainly buying \"information outputs\" such as answers to questions, documents that fulfill some requested purpose, or pieces of code that can complete certain tasks. A user buys an AI subscription or AI credits, and now can enter an input (a prompt/query) and get an output. Modern frontier models can provide a dazzlingly varied set of outputs: a single tool can first give you something like a search engine results page, followed by a complex working piece of code, a working spreadsheet, and then finally a poem and an accompanying piece of visual art. Some systems are even agentic and can produce outputs that are themselves actionable (e.g., the output is a series of actions, and then the system performs some \"actuation,\" often using the user's computer and/or API keys)."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Generally (and we'll get more precise about this later in the article), we choose to spend money (perhaps a lot of money!) on AI if we think those outputs will be \"good\" in some sense. We might think the AI is good in a statistical sense because we inspected the outputs, or because we read an evaluation study with robust evaluation of many outputs, or because we make some assumptions about how an AI was developed that make it \"good.\" However, users could also consider facts about how the model was built (such as information about the training data)."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "If you are using AI to make personalized note-taking software, facts about the training data may not be very high stakes. However, if we want to buy an AI product to ask medical questions, we might care deeply about both AI outputs and inputs to said AI. We most likely want to know that a doctor has looked at some of the model's outputs and attested they are \"good\"; we might also want to know that there were some inputs from actual doctors such as content from medical textbooks and research papers used in the development of the original model. Finally, when we get a medically relevant output from an AI system -- e.g. the system we paid to access has printed out some text telling us to take a medicine or take some action -- we ideally want that output to be verifiably linked to information about the evaluation of the model, and ideally the training data as well."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "II. How AI products are chosen today: four channels of evidence"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "If we look at the key factors that might cause someone shopping for AI products today to pick one product over another, I think we can bucket these into four groups. Put another way, most \"AI buyer choices\" can be traced to evidence or beliefs from one of four channels of information:"
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
"plaintext": "the \"outputs\" channel. How good are the actual information outputs from an AI system?"
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "the \"inputs\" channel. How were specific models used in an AI system trained and how was the overall system developed?"
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "the \"product\" channel. Covers factors related to the delivery of the information outputs: pricing, uptime, latency, UX, privacy/compliance, support, lock-in, etc."
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "the \"internals\" channel. Facts about model machinery, the channel we're furthest from being able to make practical use of, but potentially a very valuable channel."
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
"plaintext": "The product channel matters a lot if you're buying an AI product today. However, it's the channel I'll discuss the least in this post, in part because the focus here is on data-related differentiation but also because generally getting information about product factors currently works pretty well and thus enables relatively healthy market dynamics. We also won't talk much about the internals channel, e.g. making decisions based on the results of interpretability-based studies, though I think this will be increasingly important to think about going forward. Instead, this essay focuses on the missing value of the inputs channel, and on how attestations can connect inputs to outputs."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "At present, I think most AI users are choosing primarily based on beliefs about outputs plus some broad assumptions about inputs. Those beliefs about outputs may range from \"my friends told me Claude Code outputs good code\" to \"I read the recent model cards\" to \"I run my own private eval set.\" The corresponding assumptions about inputs are usually something like: the frontier labs probably sourced strong data, had capable people inspect and filter it, and used best-in-class training practices."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "That is often reasonable. Outputs matter most for many use-cases, and if I only care about outputs, information about training is mainly useful as a proxy for output quality. Still, distinguishing these channels can improve AI literacy by more clearly separating the facts about outputs and inputs that might drive consumer behavior. That helps both consumers choose and developers differentiate."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "III. Why outputs alone may not always be enough"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "How do we know if the information outputs from an AI system are good? Let's return to our first example: imagine a user who is looking to buy an AI product to help write personal note-taking software (and more generally play around with AI-coded personal software). This user probably plans to send a prompt to an AI model that looks something like this: \"write me the code for software I can use for daily note-taking\" (perhaps with a bit more detail regarding their personal preferences for how the software should work)."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Say this user can do a \"trial run\" and send this prompt to three different AI providers, A, B, and C. How will this user decide which provider product to buy?"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 3,
"facets": [],
"plaintext": "Option 1: inspect outputs yourself"
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
"byteEnd": 607,
"byteStart": 598
},
"features": [
{
"uri": "https://github.com/ianarawjo/evalstats",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "One option would be to look at the output from each model and assess the quality of that output. If the user is already an expert in this domain, perhaps they can just read the code produced by all three models and identify an obvious \"best\" model. Of course, if they wanted to have some statistical rigor in evaluation they'd probably want to look at more than one sample per model, though this will create some budgeting challenges and basically means the user needs to conduct their own benchmarking study. For a fuller treatment of the topic of looking at model outputs statistically, see e.g. evalstats from Ian Arawjo."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 3,
"facets": [],
"plaintext": "Option 2: rely on published evaluations"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Another option that also uses the outputs channel would be to look at the results of an already published benchmarking study, either from the model provider or from a third party. In this case, the user would basically be making the assumption that \"other people tried similar inputs, and performance on those related tasks will probably proxy for performance on the task I care about.\" Here the rigor of the benchmark matters: how many total variants were tried, who checked that the output worked, etc."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "When AI developers themselves or third party evaluation organizations produce a benchmarking study, the results of these studies will impact the organizations' reputation, so generally we should expect these kinds of studies to be reasonably consistent in terms of providing real signal. Benchmarking will always be noisy, but over time, there are incentives to evaluate models in ways that accurately reflect differences in capabilities. In other words, this approach should be pretty decent, and if we only ever have access to these kinds of signals for consumer decision-making, we could sustain a reasonably efficient market for AI products."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 3,
"facets": [],
"plaintext": "Option 3: rely on vibes and reputation"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "A third option after \"do your own evals\" or \"read the best recent evaluation report\" is to simply seek out a more general vibes-based ranking for the \"most intelligent\" model or the \"best\" AI developer. I think this is what many people are doing in practice right now, though there is certainly a small population of power users who diligently run their own personal benchmarking processes each time a new model releases."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "This approach is also not necessarily that ineffective. A vibes-based approach likely does integrate reputation and social proof in a way that matches other kinds of consumer decision-making and creates decent outcomes. Not everybody needs to read the auditing deep cuts or full review history for every product they buy."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "What's interesting is that using vibes to generally rank AI companies actually starts to mix information from the outputs channel and the inputs channel, because people are making some assumptions about training data and the training process itself. I think most people choosing with vibes are indeed assuming that AI developers themselves and third parties have evaluated the outputs of the model and found those outputs to be good, and perhaps that AI developers have special internal-only evaluation practices and employees that are especially skilled at AI evaluation. But this approach likely also involves assuming that the labs have used \"best in class\" training approaches, have sourced the best data they can get their hands on, and have a large team doing whatever they can to make models better. Critically, vibes-based decision-making is not entirely inputs-agnostic, and it's important to acknowledge this because I think it means people will care about inputs in the long run."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 3,
"facets": [],
"plaintext": "The issues with current status quo"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "However, this is also where we can start to envision some room for improvement in the AI consumer experience. If consumers had more specific knowledge about the inputs to an AI product, both broad facts about the training data and facts about the evaluation process, this could be useful to them. Even as underlying training techniques enable models to become more general and more broadly intelligent, it seems likely that the presence of certain types of data, data about certain topics, and data from certain experts in model inputs will proxy for output quality."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "In the medical case, information about the outputs might be more important. If sketchy training data leads to outputs that top doctors give a thumbs up to, we might take that. And overemphasis on training data may create metric chasing, e.g. including social media posts from medical doctors in pre-training data to drive up the volume of tokens from MDs. But input information should still provide some signal. Either we want real medical data in the training set or we want solid evidence our AI system has figured out medicine from first principles."
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
"byteEnd": 494,
"byteStart": 445
},
"features": [
{
"uri": "https://arxiv.org/abs/2111.15366",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 421,
"byteStart": 404
},
"features": [
{
"uri": "https://evalevalai.com/projects/every-eval-ever/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 387,
"byteStart": 377
},
"features": [
{
"uri": "https://evalevalai.com/about/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "More broadly, both output studies and input details are proxies for future quality. For statistical systems, that is often the best we're going to get. The under-emphasized problem is that as models become more general, comprehensive output evaluation across all the things they can do becomes prohibitively expensive. Many people have commented on this; see, for example, the \"Evaleval\" project and its \"Every Eval Ever\" effort, Raji et al. on \"everything in the whole wide world benchmarking\", and recent online discussions in which people contrast their personal experience with a model and that model's benchmark results."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "The labor required to really, fully, comprehensively evaluate increasingly general technologies will be very costly. We're going to need a whole lot of doctors and scientists to give feedback on a whole lot of LLM outputs to be sure we can use LLMs effectively in those contexts. But we're also going to need a whole lot of general users, with distinct combinations of niche interests, needs, preferences, etc., to give feedback as well. All this feedback will be relevant to evaluation of current models, but also relevant to the training of new models, the design of reinforcement learning environments, etc. It's going to take time to do all this evaluation, and will in some sense involve a kind of commandeering of the entire knowledge economy."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Simple napkin math suggests the relevant numbers get big quickly. Suppose we want rigorous evaluation coverage across 30 major medical specialties, with 1,000 representative cases per specialty, 10 independent physician reviews per case, and 30 minutes per review. That is 300,000 physician judgments, or 150,000 physician-hours, for one pass over one model version; at $200/hour for specialist time, that is about $30 million just in doctor-review labor. And that is before benchmark design, adjudication, compliance, or program management."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "It's worth thinking about how many hours of physician labor you want upstream of a chatbot prescribing your medicines!"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Note that here I've focused on a running example of a consumer from the general population. I think this story is useful, but you might be thinking \"I just don't believe consumers will care that much\". You may be right -- and critically, all the above argumentation applies directly to the context of enterprise AI users, who have much more bargaining power and are very likely to care about exactly all these issues described above."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "IV. What current \"upstream markets\" look like: deals, marketplaces, and labor"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Before an AI product is brought to market for consumers to consider, developers must also participate in two important upstream markets: acquiring training data and acquiring evaluations. Some companies may get their training and evaluation data without direct outside assistance, e.g. just scrape the training data and use in-house employees to do evals, but I expect as the industry matures both of these domains will become more market-like, with a broader set of data sellers at the training level and evaluation providers to choose from. Note here I'll sometimes use \"data\" a bit loosely to cover both training inputs and evaluation labor, since both are forms of human knowledge work that developers are trying to source."
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
"byteEnd": 300,
"byteStart": 294
},
"features": [
{
"uri": "https://www.apolloresearch.ai/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 289,
"byteStart": 285
},
"features": [
{
"uri": "https://metr.org/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "There is already an informal market for evaluators. It is not yet as legible or standardized as something like AWS Marketplace, but frontier labs already hire or contract with domain experts, benchmark designers, red teamers, and specialized third-party evaluators. Organizations like METR and Apollo along with similar evaluation and auditing groups, are early examples of a more specialized evaluation layer emerging around frontier AI systems."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Now, let's step away from the perspective of someone picking between AI products and instead consider a developer who wants data to build their AI product, or a seller, either an individual or an organization, looking to monetize their content."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 3,
"facets": [],
"plaintext": "Three current market forms"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "I'll bucket the ways we can buy training data and evaluation labor right now into three broad categories. These are ideal types rather than perfectly separate boxes, but they capture a lot of the current landscape:"
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
"byteEnd": 500,
"byteStart": 497
},
"features": [
{
"uri": "https://www.sec.gov/Archives/edgar/data/1713445/000162828024011789/reddit-sx1a3.htm",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 454,
"byteStart": 379
},
"features": [
{
"uri": "https://apnews.com/article/a7f131c7cb4225307134ef21d3c6a708",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 20,
"byteStart": 0
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#bold"
}
]
}
],
"plaintext": "Big licensing deals. These are bespoke boardroom transactions: a lab or platform negotiates directly with a publisher, forum, data broker, or other large rights-holder for access to a corpus or feed. The deal terms are highly customized and usually cover things like scope of use, refresh cadence, exclusivity, audit rights, indemnity, and payment over time. An example would be Google reportedly paying Reddit roughly $60M/year for access to Reddit data, with Reddit separately disclosing in its S-1 that its January 2024 data licensing arrangements had an aggregate contract value of $203M."
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
"byteEnd": 457,
"byteStart": 339
},
"features": [
{
"uri": "https://aws.amazon.com/marketplace/pp/prodview-vgmxklm42lhmq",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
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
"plaintext": "Licensing via marketplace. This is more like online shopping for large datasets. Instead of a bespoke negotiation, the seller lists a relatively standardized product with a posted description, delivery format, usage terms, and price, and the buyer can compare options much more quickly. An example would be going to AWS Marketplace to buy 12 months of \"Anonymized, non-aggregated granular consumer-level data across all asset classes\" from Equifax for $175k. Economically, the appeal here is lower transaction cost and easier comparison across sellers, though the quality and rights picture may still require substantial diligence."
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
"byteEnd": 401,
"byteStart": 355
},
"features": [
{
"uri": "https://researcher-help.prolific.com/en/article/2273bd",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 351,
"byteStart": 339
},
"features": [
{
"uri": "https://www.prolific.com/pricing",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 62,
"byteStart": 0
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#bold"
}
]
}
],
"plaintext": "Pay individual people, per task or per hour, for data outputs. This is the crowdwork or expert-labor bucket. Here the buyer is not primarily acquiring a pre-existing corpus; they are paying people to generate judgments, labels, rankings, reviews, or other evaluative outputs under a specified protocol. An example might be paying somebody via Prolific at at least $8/hr, and typically more like $12/hr to label web data, or paying domain experts to peer review model outputs. This category matters especially for evaluation, where the scarce input is often expert attention rather than a static archive."
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
"plaintext": "One nearby fourth form, if one wanted to break the taxonomy out further, would be recurring API or feed access rather than transfer of a bulk dataset: paying for ongoing, metered access to a live corpus or stream. I think that form mostly collapses back into Categories 1 and 2 depending on how standardized the arrangement is, so I am leaving it as an adjacent case rather than promoting it to a main bucket."
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
"byteEnd": 36,
"byteStart": 32
},
"features": [
{
"uri": "https://research.brickroad.network/neurips2025-data-deals",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "See also the data deals tracker here from the authors of \"A Sustainable AI Economy Needs Data Deals That Work for Generators\"."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 3,
"facets": [],
"plaintext": "Collectives and intermediaries"
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
"byteEnd": 693,
"byteStart": 656
},
"features": [
{
"uri": "https://gs.statcounter.com/browser-market-share/desktop/worldwide",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 602,
"byteStart": 552
},
"features": [
{
"uri": "https://brave.com/blog/100m-mau/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 387,
"byteStart": 374
},
"features": [
{
"uri": "https://support.brave.app/hc/en-us/articles/360027276731-Brave-Rewards-FAQ",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 369,
"byteStart": 364
},
"features": [
{
"uri": "https://swashapp.io/about",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Another idea that's gained some popularity over the last decade is the notion of joining a data cooperative, collective, union, or intermediary. Generally, the idea here is that you join the coop, contribute data, and some actor in the coop transacts in a market on your behalf. In fact, there are some ways to join a data cooperative today. Organizations such as Swash and Brave Rewards monetize various online actions and tasks. The user bases of data-coop-style tools are very small compared to general Internet usage. For reference, Brave reported 101M monthly active users as of September 30, 2025, while StatCounter has recently put Brave at roughly 1% of worldwide desktop browser share. Some of the means of monetization, e.g. watching ads, are also quite different from an aspirational vision of data markets in which data sellers are spending their time crafting valuable documents and records and then being rewarded for their contributions to shared epistemics. I do really believe that a useful North Star is trying to shoot for a world in which more overall human work looks like the good parts of journalism, scientific peer review, editing Wikipedia, and participating in Q&A, with the bad parts minimized or automated away."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "While the above data cooperatives involve a technical approach to enabling cooperation, and participation remains niche, I actually think there is a lot of low-hanging fruit for applying the collectives/coops/unions idea to the three types of markets described above."
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
"byteStart": 666
},
"features": [
{
"uri": "https://data-workers.org/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 661,
"byteStart": 649
},
"features": [
{
"uri": "https://www.saiph.org/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "First, for the big boardroom deals, we could imagine pools of users directly weighing in on the deal conditions. For example, when it comes time for Reddit to renegotiate with Google or others, they loop users in, either voluntarily or under threat of collective action. Second, data coops can post their own quality-assessed CSV file for sale on AWS Data Marketplace right now, but they still need social and technical support to actually organize in the first place and produce a good CSV. And there is a large body of work, including ongoing efforts, that aim to support collective bargaining for data workers, see e.g. the body of work from Dr. Saiph Savage and Data Workers' Inquiry from DAIR."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "One consideration is that successful organization of data workers may actually involve a shift from crowdwork markets to collectives that sell bundled data, i.e. moving more overall information from Category 3 to Category 2, or even 1."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 3,
"facets": [],
"plaintext": "Two policy levers: data protection and attestation"
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
"byteEnd": 179,
"byteStart": 135
},
"features": [
{
"uri": "https://www.cloudflare.com/en-ca/press-releases/2025/cloudflare-just-changed-how-ai-crawlers-scrape-the-internet-at-large/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "There is also an emerging set of actors interested in supporting various forms of what we might term \"data protection for the AI age\". Cloudflare's public support of anti-scraping is one example."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "I think it is useful to start from a fairly grim baseline: many people assume their data will be scraped, distilled, and reused unless they actively block it through anti-scraping, anti-distillation, poisoning, preference signals, legal enforcement, or some mix of these."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "In general, supporting data protection action can make it more likely that data sellers will engage with markets rather than give up because everything will be scraped anyway. In other words, some actor, public or private, needs to do some level of policing for a market to emerge. This is a bitter pill from an open-culture perspective, since open culture is foundational to modern ML, including both peer production of critical training data and open-source implementations of algorithms and tooling. Still, there is likely a middle ground in which open culture continues in many domains while others become more financialized. Any actions that move us away from the current situation are probably net good in the short term, though we should be cautious about a pendulum-swing-too-far data-cartel scenario in which nobody can use any information without paying."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Under an attestation-centered regime, data might still be readable or even openly available, but what becomes scarce is the ability to make a trusted downstream claim about provenance, licensing, evaluation, or output identity. Scraping without the attestation may no longer be enough to compete in markets where buyers, enterprise customers, insurers, or regulators care about verified inputs and verified outputs."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "This is why attestation is particularly appealing for public AI strategy. It suggests a path where openness and bargaining do not always have to be direct opposites. In the strongest version, a dataset or corpus might be free for research or public-interest AI use, while commercial actors must pay if they want to rely on it in an attested product or otherwise market the trusted provenance relationship. These approaches are complements rather than substitutes: better data protection may be needed to get participation off the ground, but attestation changes the long-run market game by moving value toward attestations rather than raw tokens."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "V. Why attestation improves incentives"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "We need to address three fundamental constraints that affect value measurement and value transfer in the context of AI:"
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
"byteEnd": 38,
"byteStart": 4
},
"features": [
{
"uri": "https://www.nber.org/books-and-chapters/rate-and-direction-inventive-activity-economic-and-social-factors/economic-welfare-and-allocation-resources-invention",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "the economic properties of information, non-rivalry and non-excludability, make it very hard to create efficient markets for information. But if markets attach value to attestations rather than bits, we may be able to have our cake and eat it too: widely distribute information via AI as a public good while retaining some of the coordinating benefits of markets"
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
"byteEnd": 82,
"byteStart": 45
},
"features": [
{
"uri": "https://arxiv.org/abs/1904.02868",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "the value of data, as defined by any kind of data counterfactual estimation method (\"how does accuracy change if unit or bundle of data is removed from training\"), is generally small in raw magnitude unless data is grouped together as some kind of collective"
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "open data can, in some cases, directly disempower certain subsets of workers by making the relevant knowledge easier to copy than to bargain over. An attestation layer offers one possible way to preserve some openness while still giving those groups something commercially salient to negotiate around"
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
"plaintext": "We could somewhat address these challenges by just trying to coarsely distribute value to data creators: just worry less about provenance and distribute resources through something like a data-dividend public wealth fund. I think that may be a useful transitional approach in the short term, but likely not the ideal end state."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 3,
"facets": [],
"plaintext": "Why AI buyers care"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "For buyers, the benefit is straightforward: inputs and outputs become inspectable product features. Instead of relying only on benchmarks, reputation, or vibes, a buyer could ask more specific questions: How many credentialed authors contributed to training data? What process verified their work? What upstream sources were actually licensed? Was this particular output generated by a model version whose provenance and evaluation records I can inspect? In higher-stakes domains, that still does not replace output inspection, but it gives downstream choice much more structure."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "In some settings, we can expect transparency around model outputs themselves to become a requirement rather than a premium feature. A regulator or enterprise buyer may increasingly want not just \"trust us\" but verifiable disclosure that a given artifact came from a given model and from a model with a certain attested pedigree."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "If those attestations become known to be predictive -- e.g. the AI model with stronger attestations around its training data is actually better at giving health advice -- they also reduce some of the appeal of indiscriminate scraping or distillation. A rival might still imitate outputs, but the attested relationship itself becomes part of what the buyer is purchasing."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 3,
"facets": [],
"plaintext": "Why contributors and collectives care"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "For creators, evaluators, and data workers, the important shift is from selling anonymous tokens to participating in visible, renewable labor relationships. Attestations for training and evaluation can be managed and aggregated by some kind of intermediary, collective, or union so people do not need to transact individually with AI companies."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "If verified attestations become important to consumers or regulators, that would immediately bring more data work out into the open. It would make it easier to treat these jobs as real careers and harder to treat data workers as invisible or precarious labor. Note that while I've been using doctors as a convenient running example -- a relatively small group with easy credentials to verify and existing social infrastructure for collective action -- the same logic applies to many other kinds of knowledge work."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "The economics of maintaining a trusted relationship are also very different from the economics of acquiring tokens. The actual bundles of information in training data are and will remain mostly non-rival, and often hard to exclude. But contracts with people or collectives are not just about buying rights to transfer bits. These are contracts for labor which must be renewed and maintained. A world of data-with-attestations is therefore a world with more ongoing relationships and more room for bargaining."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 3,
"facets": [],
"plaintext": "Why labs, regulators, and public AI builders care"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "For labs, credible attestation could become a meaningful source of differentiation, though adopting any particular standard is a collective action problem. This is where auditing, evaluation, and safety cases begin to connect to regulation, insurance, procurement rules, and industry self-governance."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "The building blocks for this market already exist in the upstream markets described above. The main difference with attestations is that the fact a person made or evaluated some portion of the data would no longer be hidden, but rather made prominent. If an AI builder who uses attested or full-consent data early on is able to produce good models and prove that buyers care about those records, that creates pressure for other AI developers to play along as good-faith actors in the market."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "An immediate downside for some labs is that data and evaluation may cost more."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "A version of an attestation-based provenance system that gets things really right could be good for AI developers, data creators who want to add knowledge via pretraining, content creators who want to be rewarded when their content is retrieved, public-interest model builders who want to distinguish civic from purely commercial use, and people who want to use AI to produce things and sell them, e.g. software developers selling vibe-coded software. In the strongest version, the flow of attested data and AI outputs also becomes a governance lever, in the sense that healthy markets for anything act as both a kind of computation over preferences and a kind of governance."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "VI. Implementation and caveats"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 3,
"facets": [],
"plaintext": "Enforcement will be partly technical and partly social"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Here I've talked in broad strokes about attestation, provenance, and verification a bunch, but have remained relatively agnostic to any particular implementation details. Attestation and verification will involve a mix of technical and social means of enforcement. They might lean more heavily on technical innovations, e.g. new approaches for embedded cryptographic signatures, or more heavily on social forces, e.g. organizations that enforce attestations through reputation."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "At a high level, there are at least six areas of existing/ongoing work that could support attestation:"
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
"byteEnd": 4,
"byteStart": 0
},
"features": [
{
"uri": "https://spec.c2pa.org/specifications/specifications/2.3/ai-ml/ai_ml.html",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "C2PA is, I think, currently the closest technical analogue. It already supports signed provenance for AI/ML models, training datasets, outputs, fine-tuning, and versioned releases. If one wanted to implement parts of this proposal tomorrow, C2PA is an obvious place to start."
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
"byteStart": 12
},
"features": [
{
"uri": "https://slsa.dev/spec/v1.2/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 7,
"byteStart": 0
},
"features": [
{
"uri": "https://in-toto.io/docs/what-is-in-toto/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "in-toto and SLSA provide a generic supply-chain pattern for authenticated statements about subjects, materials, builders, and verification."
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
"byteEnd": 317,
"byteStart": 311
},
"features": [
{
"uri": "https://attest.org/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "The web3 and verifiable-credentials worlds have also spent years experimenting with portable attestations, signed claims, and selective disclosure. I do not think AI provenance needs blockchains by default, but that design space is still relevant as a source of ideas about interoperable attestations. See e.g. Attest."
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
"byteEnd": 23,
"byteStart": 13
},
"features": [
{
"uri": "https://www.microsoft.com/en-us/research/project/datasheets-for-datasets/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 11,
"byteStart": 0
},
"features": [
{
"uri": "https://research.google/pubs/model-cards-for-model-reporting/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Model cards, datasheets, and related documentation frameworks make model and dataset facts legible via standardized processes."
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
"uri": "https://www.averi.org/ourwork/frontier-ai-auditing",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Frontier AI auditing focuses on institutional assurance: who gets access, what independence standards matter, what level of assurance an audit provides, and how results should be communicated."
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
"byteEnd": 14,
"byteStart": 0
},
"features": [
{
"uri": "https://datalicenses.org/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Data licensing explores the contractual layer around who can use what data, for which purposes, and under what terms. That layer is not itself an attestation format, but it helps define the claims an attestation system would need to make legible and enforceable."
}
}
]
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 3,
"facets": [],
"plaintext": "How we might transition towards attestations"
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
"byteEnd": 544,
"byteStart": 540
},
"features": [
{
"uri": "https://arxiv.org/abs/2504.06219",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 501,
"byteStart": 498
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
"byteEnd": 496,
"byteStart": 486
},
"features": [
{
"uri": "https://www.eleuther.ai/",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 250,
"byteStart": 215
},
"features": [
{
"uri": "https://crfm.stanford.edu/fmti/December-2025/index.html",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "Recent trends in dataset documentation suggest a world of transparent data for AI models is not yet around the corner. Dataset details in model and system cards remain extremely short and vague, as reflected in the Foundation Model Transparency Index, and understandably are likely to remain short and vague until additional legal clarity is achieved. That said, for both researchers and consumers, it will be very valuable to keep an eye out for new open releases, such as models from EleutherAI, AI2, and academic groups (see e.g. recent work from Fan et al. on model training using highly compliant web data)."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "But critically, almost all the actions that data protectors might take now, including developing and offering anti-scraping technologies, helping to socialize anti-scraping and AI preference signals, and supporting related research on data value estimation, full-consent LLMs, partnerships with national labs, etc., are likely to also make it easier to work toward attested data."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "Appendix I: how this proposal connects to earlier posts"
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
"byteEnd": 307,
"byteStart": 305
},
"features": [
{
"uri": "https://dataleverage.substack.com/p/how-do-we-know-our-ai-output-is-good",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 304,
"byteStart": 298
},
"features": [
{
"uri": "https://dataleverage.substack.com/p/evaluation-data-leverage-advances",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 297,
"byteStart": 290
},
"features": [
{
"uri": "https://dataleverage.substack.com/p/selling-agi-like-ag1-will-the-market",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 275,
"byteStart": 263
},
"features": [
{
"uri": "https://dataleverage.substack.com/p/almost-everybody-including-both-data",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 256,
"byteStart": 240
},
"features": [
{
"uri": "https://dataleverage.substack.com/p/tipping-points-for-content-ecosystems",
"$type": "pub.leaflet.richtext.facet#link"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 210,
"byteStart": 193
},
"features": [
{
"uri": "https://dataleverage.substack.com/p/the-paradox-of-reuse-in-2026-a-case",
"$type": "pub.leaflet.richtext.facet#link"
}
]
}
],
"plaintext": "This appendix is optional background for returning readers (and so I can keep track of what points I've been making in too many distinct blogs!). It shows how the proposal connects back to the \"quasi-enclosure\" piece (itself a follow-up to \"tipping points\"), the \"data rules\" piece, and an earlier series of posts discussing evaluation and data labor."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 3,
"facets": [],
"plaintext": "On \"quasi-enclosure\" and \"tipping points\""
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Those posts argued that AI can increase useful knowledge work while still routing the resulting data into private pools, creating a precarious quasi-enclosure and raising the risk of content-ecosystem tipping points. If labs compete partly on verifiable claims about who contributed, who evaluated, and under what terms, then some of the value currently captured silently through closed transcript pools can instead flow through explicit labor relationships, collective bargaining, and public-facing quality claims. That does not solve the commons problem by itself, but it does create a more plausible \"golden path\" in which AI products remain broadly useful while preserving stronger incentives for the people and institutions that keep producing the knowledge those systems depend on. To retain the benefits of maintaining knowledge commons in general, we also need interventions and social norms aimed explicitly at maintaining those commons."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 3,
"facets": [],
"plaintext": "On \"data rules\""
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "The \"data rules\" piece argued for clearer and more enforceable options governing how data can be used across training, retrieval, and evaluation, in ways that help both creators and model builders. Attestation is one way to make such rules practical. A rule only matters if someone can later verify what happened: whether a dataset was licensed for training but not evaluation, whether an evaluation set was kept separate from training, whether a model output can be linked back to a model version and a body of supporting evidence. In that sense, attestation is not a rival proposal to clearer data rules; it is one concrete way to operationalize them."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Of particular note: designing a schema for attestation could help to surface the types of contracts available to data creators and AI developers."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 3,
"facets": [],
"plaintext": "On \"selling AGI like AG1\""
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "That post argued that as AI products get more expensive, buyers will want more than vibes and vague claims about \"more intelligence\". The attestation proposal gives a direct answer to that consumer problem."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 3,
"facets": [],
"plaintext": "On the evaluation-related posts"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "The earlier evaluation posts argued that output evaluation is costly, incomplete, and increasingly central as models become more general. They also argued that evaluation labor itself could become a major site of bargaining power. The attestation proposal follows up on these ideas. An evaluation attestation can say who did the work, what they reviewed, how much they reviewed, and under what process. That helps buyers interpret quality claims, but it also helps workers and collectives bargain over the provision of evaluation labor because the work is more visible."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "Appendix II: objections and replies"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 3,
"facets": [],
"plaintext": "Q: What if buyers simply do not care about attestations?"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "A: This is one strong practical objection. If most buyers continue to choose AI products based mainly on outputs, price, latency, UX, and enterprise features, then attestations will not do much work on their own. Attestations definitely will not magically displace those factors, but they can become additional decision-relevant signal, especially in higher-stakes domains and in procurement settings where compliance, liability, and reputation matter. If consumer and enterprise demand never materializes, then the proposal likely depends much more heavily on regulation, insurance, or industry self-governance than on pure market pull. See the short discussion in the intro about practical incentives."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 3,
"facets": [],
"plaintext": "Q: Couldn't this cause people to confuse provenance with \"explainability\" or \"justification\"?"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "A: Definitely possible. A provenance chain is not the same thing as a causal explanation of why a specific output is correct. Knowing that doctors contributed to training data or reviewed some model outputs does not by itself prove that a particular medical answer is trustworthy. The point of attestation is therefore not to replace epistemic validation, but to supplement it. It gives buyers more information about the system behind an output, not a complete proof that any one answer is right."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "A critical part of making this system work would be ensuring that the organizations participating in the attestation chain (e.g., medical organizations) ensure that attestations are, for the most part, epistemically valid."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 3,
"facets": [],
"plaintext": "Q: Won't companies just game the metrics once \"attested inputs\" become a selling point?"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "A: They might. If the market starts rewarding visible counts like \"number of doctors involved\" or \"number of licensed sources,\" firms will have incentives to optimize for what is easiest to attest rather than what most improves the system. That is a classic Goodhart problem. The best response is to design attestations carefully! Even then, some gaming pressure is inevitable."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "And similarly, this issue can be partially solved by ensuring that the organizations providing attestations have an incentive to keep their attestations aligned with \"real value\" in their domain. Or put another way, if medical organizations continue to police the medical competence of their members, the approaches for this kind of organizational quality control can be used to combat metric gaming."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 3,
"facets": [],
"plaintext": "Q: Doesn't this just move trust from AI labs to auditors and certifiers?"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "A: In part, yes. Any attestation regime creates a new bottleneck around whoever verifies claims. That raises familiar worries about certification cartels, regulatory capture, and barriers to entry for smaller labs or open projects. Regulators and consumers will both have to continue contributing to governance questions around who gets to be trusted as a verifier and under what standards."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 3,
"facets": [],
"plaintext": "Q: How can useful attestations coexist with privacy, secrecy, and anti-gaming concerns?"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "A: There is a genuine tension here. If attestations are highly specific, they may reveal private contributor information, proprietary dataset composition, or evaluation details that make benchmarks easier to game. If they are too vague, they collapse into branding or marketing copy. There is no perfect resolution. The practical goal is likely to be selective disclosure: enough specificity to support meaningful external checking, without assuming that every contributor identity, dataset row, or eval item can be made public."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "New research may also make this question less of a concern."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 3,
"facets": [],
"plaintext": "Q: Why would attestation reduce scraping or distillation if a rival can still match output quality?"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "A: If a competitor offers similar or better outputs at lower cost, many buyers will still switch regardless of cleaner provenance. A more modest claim is that attestation can create some product differentiation and make fully consent-based development more legible, not that it eliminates the economic pull of imitation. Scraping and distillation remain live incentives unless buyers, regulators, or counterparties attach real value to the attested relationship itself, whether that relationship concerns training data, retrieval sources, evaluation labor, or the identity of the output-producing model."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Importantly: for something like health advice, people are paying, in part, for some amount of confidence or peace of mind. Here, the presence of attestations really matters and makes a material difference between model A with attestations and model B with very similar outputs but no attestations."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 3,
"facets": [],
"plaintext": "Q: Does visibility alone actually create bargaining power for contributors?"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "A: Not by itself. Making data work legible is not the same thing as guaranteeing payment, better labor conditions, or stronger negotiating leverage. Those outcomes also require institutions that can enforce terms, whether through law, contracts, unions, collectives, or platform governance. Attestation can make bargaining easier by making contributions auditable and portable, but it does not substitute for the underlying political and organizational work."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 2,
"facets": [],
"plaintext": "Appendix III: a simple attestation schema for AI inputs, evaluations, and outputs"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "Here is one toy worked example of a concrete schema. This sketch borrows from several existing approaches described above. I expect this section to be made pretty redundant by future \"full spec docs\", but I think it's clarifying to include some toy examples alongside this post."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 3,
"facets": [],
"plaintext": "Design goals"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "The object model should:"
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
"plaintext": "work across training, evaluation, and output provenance"
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "support both human-readable and machine-readable claims"
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "allow signatures or other authenticated proofs"
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "stretch goal: allow selective disclosure, since full public disclosure of contributors, datasets, or eval items will often be impossible"
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "support both individuals and organizations as contributors, attesters, and verifiers (but likely prefer organizations)"
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "make it easy to traverse links from an output to a model version, from the model version to evaluation records, and from there to upstream contributions"
}
}
]
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 3,
"facets": [],
"plaintext": "Minimal outer wrapper"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "At a high level, the same outer structure can be reused even when the subject matter changes:"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.code",
"language": "json",
"plaintext": "{\n \"schema_version\": \"0.1\",\n \"object_type\": \"training_contribution\",\n \"subject\": {\n \"kind\": \"dataset_shard\",\n \"id\": \"med-001\"\n },\n \"attester\": {\n \"kind\": \"publisher\",\n \"id\": \"licensed-med-publisher\"\n },\n \"contributor\": {\n \"kind\": \"author\",\n \"credential\": \"MD\"\n },\n \"claim\": {\n \"statement\": \"A credentialed contributor supplied content used in model development.\"\n },\n \"evidence\": {},\n \"verifier\": {\n \"kind\": \"third_party_auditor\",\n \"id\": \"auditor-a\"\n },\n \"timestamp\": \"2026-04-08T00:00:00Z\",\n \"links\": {},\n \"signatures\": [],\n \"disclosure\": {\n \"public\": true\n }\n}",
"syntaxHighlightingTheme": "catppuccin-mocha"
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
"byteEnd": 14,
"byteStart": 0
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#code"
}
]
}
],
"plaintext": "schema_version: version of this logical schema, not necessarily the wire format version"
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
"byteEnd": 110,
"byteStart": 96
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#code"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 94,
"byteStart": 77
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#code"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 75,
"byteStart": 58
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#code"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 56,
"byteStart": 35
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#code"
}
]
},
{
"$type": "pub.leaflet.richtext.facet",
"index": {
"$type": "pub.leaflet.richtext.facet#byteSlice",
"byteEnd": 11,
"byteStart": 0
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#code"
}
]
}
],
"plaintext": "object_type: claim family, such as training_contribution, evaluation_record, output_provenance, downstream_use, or one of the auxiliary types below"
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
"$type": "pub.leaflet.richtext.facet#code"
}
]
}
],
"plaintext": "subject: the dataset shard, model, model version, evaluation artifact, or output being described"
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
"byteEnd": 8,
"byteStart": 0
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#code"
}
]
}
],
"plaintext": "attester: the entity making the attestation"
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
"byteEnd": 11,
"byteStart": 0
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#code"
}
]
}
],
"plaintext": "contributor: the person or organization whose role is being attested, if different from the attester"
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
"byteEnd": 5,
"byteStart": 0
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#code"
}
]
}
],
"plaintext": "claim: the substantive statement being made"
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
"byteEnd": 8,
"byteStart": 0
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#code"
}
]
}
],
"plaintext": "evidence: artifacts, counts, references, hashes, licenses, reports, or other support for the claim"
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
"byteEnd": 8,
"byteStart": 0
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#code"
}
]
}
],
"plaintext": "verifier: the party, process, or assurance mechanism that makes the claim more trustworthy"
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
"byteEnd": 9,
"byteStart": 0
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#code"
}
]
}
],
"plaintext": "timestamp: issuance time"
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
"byteEnd": 5,
"byteStart": 0
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#code"
}
]
}
],
"plaintext": "links: pointers to upstream or downstream objects"
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
"byteEnd": 10,
"byteStart": 0
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#code"
}
]
}
],
"plaintext": "signatures: cryptographic signatures or references to them"
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
"byteEnd": 10,
"byteStart": 0
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#code"
}
]
}
],
"plaintext": "disclosure: what is public, redacted, or privately available to auditors only"
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
"plaintext": "The wire format does not have to be this JSON shape. The same logical object could be encoded using a C2PA manifest, an in-toto statement plus predicate, or another signed envelope."
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 3,
"facets": [],
"plaintext": "Suggested object types"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "The four core user-facing object types are:"
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
"$type": "pub.leaflet.richtext.facet#code"
}
]
}
],
"plaintext": "training_contribution: a claim about upstream data, labor, or licensed content used in model development"
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
"$type": "pub.leaflet.richtext.facet#code"
}
]
}
],
"plaintext": "evaluation_record: a claim about who evaluated what, under what protocol, and with what sample size or assurance process"
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
"$type": "pub.leaflet.richtext.facet#code"
}
]
}
],
"plaintext": "output_provenance: a claim that a specific output came from a specific model version and can be linked back to relevant evaluation and training records"
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
"byteEnd": 14,
"byteStart": 0
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#code"
}
]
}
],
"plaintext": "downstream_use: a claim that a downstream artifact, workflow, or organization used a specific model or model version in producing some later output"
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
"plaintext": "Two plausible auxiliary types are:"
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
"byteEnd": 13,
"byteStart": 0
},
"features": [
{
"$type": "pub.leaflet.richtext.facet#code"
}
]
}
],
"plaintext": "model_release: a claim about a model version, checkpoint lineage, deployment status, or serving identity"
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
"$type": "pub.leaflet.richtext.facet#code"
}
]
}
],
"plaintext": "credential_attestation: a claim about contributor qualifications, institutional affiliation, or eligibility to participate in a class of work"
}
}
]
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 3,
"facets": [],
"plaintext": "Toy examples"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 3,
"facets": [],
"plaintext": "Training contribution"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.code",
"language": "json",
"plaintext": "{\n \"schema_version\": \"0.1\",\n \"object_type\": \"training_contribution\",\n \"subject\": {\n \"kind\": \"dataset_shard\",\n \"id\": \"med-042\"\n },\n \"attester\": {\n \"kind\": \"publisher\",\n \"id\": \"licensed-med-publisher\"\n },\n \"contributor\": {\n \"kind\": \"author\",\n \"credential\": \"MD\",\n \"organization\": \"licensed medical publisher\"\n },\n \"claim\": {\n \"statement\": \"A peer-reviewed cardiology chapter authored by a credentialed physician was included in licensed corpus shard med-042.\",\n \"usage\": \"pretraining\"\n },\n \"evidence\": {\n \"artifact_id\": \"chapter-8841\",\n \"license_id\": \"license-332\"\n },\n \"verifier\": {\n \"kind\": \"third_party_auditor\",\n \"id\": \"auditor-a\"\n },\n \"timestamp\": \"2026-04-08T00:00:00Z\",\n \"links\": {\n \"downstream_model_run\": \"model-x-pretrain-run-07\",\n \"downstream_model\": \"model-x-2026-03-15\"\n },\n \"signatures\": [\n \"sig:licensed-med-publisher:abc123\"\n ],\n \"disclosure\": {\n \"public\": true,\n \"auditor_only_fields\": []\n }\n}",
"syntaxHighlightingTheme": "catppuccin-mocha"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 3,
"facets": [],
"plaintext": "Evaluation record"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.code",
"language": "json",
"plaintext": "{\n \"schema_version\": \"0.1\",\n \"object_type\": \"evaluation_record\",\n \"subject\": {\n \"kind\": \"model_version\",\n \"id\": \"model-x-2026-03-15\"\n },\n \"attester\": {\n \"kind\": \"evaluation_org\",\n \"id\": \"eval-lab-1\"\n },\n \"contributor\": {\n \"kind\": \"reviewer\",\n \"credential\": \"MD\",\n \"experience_years\": 20\n },\n \"claim\": {\n \"statement\": \"A practicing physician reviewed 100 outputs across 10 health-related tasks.\",\n \"task_set\": \"health-general-v2\"\n },\n \"evidence\": {\n \"sample_size\": 100,\n \"hours\": 100,\n \"report_id\": \"eval-report-77\"\n },\n \"verifier\": {\n \"kind\": \"assurance_process\",\n \"level\": \"independent-third-party\"\n },\n \"timestamp\": \"2026-04-08T00:00:00Z\",\n \"links\": {\n \"benchmark_report\": \"eval-report-77\",\n \"related_model\": \"model-x\"\n },\n \"signatures\": [\n \"sig:eval-lab-1:def456\"\n ],\n \"disclosure\": {\n \"public\": true,\n \"auditor_only_fields\": [\n \"sampled_output_ids\"\n ]\n }\n}",
"syntaxHighlightingTheme": "catppuccin-mocha"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 3,
"facets": [],
"plaintext": "Output provenance"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.code",
"language": "json",
"plaintext": "{\n \"schema_version\": \"0.1\",\n \"object_type\": \"output_provenance\",\n \"subject\": {\n \"kind\": \"model_output\",\n \"id\": \"response-abc123\"\n },\n \"attester\": {\n \"kind\": \"model_provider\",\n \"id\": \"provider-y\"\n },\n \"claim\": {\n \"statement\": \"This output was generated by model-x version 2026-03-15.\"\n },\n \"evidence\": {\n \"request_hash\": \"req-8fd2\",\n \"model_version\": \"model-x-2026-03-15\"\n },\n \"verifier\": {\n \"kind\": \"provider_signature\",\n \"id\": \"provider-y-signing-key\"\n },\n \"timestamp\": \"2026-04-08T00:00:00Z\",\n \"links\": {\n \"model\": \"model-x\",\n \"evaluation_attestations\": [\n \"eval-report-77\"\n ],\n \"training_attestations\": [\n \"train-attest-8841\"\n ]\n },\n \"signatures\": [\n \"sig:provider-y:ghi789\"\n ],\n \"disclosure\": {\n \"public\": true\n }\n}",
"syntaxHighlightingTheme": "catppuccin-mocha"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.header",
"level": 3,
"facets": [],
"plaintext": "Downstream use"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.code",
"language": "json",
"plaintext": "{\n \"schema_version\": \"0.1\",\n \"object_type\": \"downstream_use\",\n \"subject\": {\n \"kind\": \"software_release\",\n \"id\": \"health-app-v12\"\n },\n \"attester\": {\n \"kind\": \"developer\",\n \"id\": \"health-app-studio\"\n },\n \"claim\": {\n \"statement\": \"This iPhone health app release used GPT-6.0-med1000 during development.\",\n \"usage\": [\n \"code_generation\",\n \"documentation_drafting\"\n ]\n },\n \"evidence\": {\n \"build_id\": \"ios-build-991\",\n \"model_version\": \"gpt-6.0-med1000\"\n },\n \"verifier\": {\n \"kind\": \"workflow_log\",\n \"id\": \"build-pipeline-attestor\"\n },\n \"timestamp\": \"2026-04-08T00:00:00Z\",\n \"links\": {\n \"model\": \"gpt-6.0-med1000\",\n \"related_outputs\": [\n \"response-abc123\"\n ]\n },\n \"signatures\": [\n \"sig:health-app-studio:jkl012\"\n ],\n \"disclosure\": {\n \"public\": true\n }\n}",
"syntaxHighlightingTheme": "catppuccin-mocha"
}
},
{
"$type": "pub.leaflet.pages.linearDocument#block",
"block": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "If objects like these are interoperable, a buyer or auditor can move:"
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
"plaintext": "from a downstream app, document, or answer to a declared model use"
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "from that use record to the serving model version"
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "from the model version to evaluation records"
}
},
{
"$type": "pub.leaflet.blocks.unorderedList#listItem",
"content": {
"$type": "pub.leaflet.blocks.text",
"facets": [],
"plaintext": "from evaluation records and model lineage to upstream contributions"
}
}
]
}
}
]
}
]
},
"description": "A proposal for interoperable attestation objects that connect training data, evaluation labor, and AI-generated outputs across the AI supply chain.",
"publishedAt": "2026-04-09T00:46:16.000Z"
}
}
