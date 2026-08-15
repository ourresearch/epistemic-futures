---
title: "Today's AIs Aren't Paperclip Maximizers. That Doesn't Mean They're Not Risky"
person: peter-salib
section: by
type: essay
year: 2025
date: 2025-05-21
venue: "AI Frontiers"
authors: "Peter N. Salib and Simon Goldstein"
source_url: https://ai-frontiers.org/articles/todays-ais-arent-paperclip-maximizers
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via r.jina.ai reader (the article body is client-rendered, so plain HTML fetches return only the site index)."
---

# Today's AIs Aren't Paperclip Maximizers. That Doesn't Mean They're Not Risky

## Full text

# Today's AIs Aren't Paperclip Maximizers. That Doesn't Mean They're Not Risky

## Classic arguments about AI risk imagined AIs pursuing arbitrary and hard-to-comprehend goals. Large Language Models aren't like that, but they pose risks of their own.

May 21, 2025

[Peter N. Salib](https://ai-frontiers.org/author/peter-salib)

[Simon Goldstein](https://ai-frontiers.org/author/simon-goldstein)

Guest Commentary

[Download Audio](https://ai-frontiers.org/articles/todays-ais-arent-paperclip-maximizers#)

Much of the discussion around AI safety is motivated by concerns around existential risk: the idea that autonomous systems will grow smarter than humans and go on to eradicate our species, either deliberately or as an unintended consequence.

The founders of the AI safety movement took these possibilities seriously when many people still brushed them off as science fiction. Nick Bostrom’s 2014 book _Superintelligence_, for example, explored risks and opportunities humanity might face after developing AI systems with cognitive capabilities drastically more powerful than our own.

His work built on even earlier scholarship from Stephen [Omohundro](https://selfawaresystems.com/wp-content/uploads/2008/01/ai_drives_final.pdf), Stuart [Russell](https://en.wikipedia.org/wiki/Artificial_Intelligence:_A_Modern_Approach), Eliezer [Yudkowsky](https://intelligence.org/files/AIPosNegFactor.pdf), and others whose foundational ideas were published during an era where the most advanced machine learning algorithms did things like rank search results.

These classical arguments still underlie many of the conversations in AI risk.

As forward-thinking as they were, many important details of these arguments are now behind the times. After all, they were developed before the advent of the transformer architecture, large language models, and reasoning models. Today’s frontier AI models — trained to imitate human text — display behaviors that don’t conform to those classical arguments.

Based on these observations, it’s worth asking: Should we update our estimates of existential AI risk? Should we abandon the classic arguments entirely?

## The Classic Arguments for Existential AI Risk

Classic arguments for existential AI risk rely on two premises: “[orthogonality](https://pure.tue.nl/ws/portalfiles/portal/196104221/Ratio_2021_M_ller_Existential_risk_from_AI_and_orthogonality_Can_we_have_it_both_ways.pdf)” and “[instrumental convergence](https://en.wikipedia.org/wiki/Instrumental_convergence#:~:text=Instrumental%20convergence%20is%20the%20hypothetical,ultimate%20goals%20are%20quite%20different.)”.

Early thinking about existential AI risk assumed that being smart was different from being morally good. The technical term for this claim is _orthogonality_, and it ran both ways: A very dumb AI could have very good goals (by human standards), while a very smart system may adopt very harmful ones.

The orthogonality thesis could be read minimally, to counsel simple caution. If “good” does not follow from “capable,” then AI researchers should be sure to invest in improving their AI systems along both dimensions.

But the classic arguments for AI risk generally involve a stronger version of orthogonality. They suggest that, absent fundamental scientific and philosophical breakthroughs, powerful AIs are highly _likely_ to seek destructive ends.

This is based on the premise that, if goals are truly uncorrelated with capabilities, then we should model each AI’s ultimate goals as a [random draw](https://philarchive.org/rec/GALIDB) from the distribution of all possible goals. It is also based on the assumption that, if it were possible to write a list of all [possible goals](https://www.lesswrong.com/posts/r86BBAqLHXrZ4mWWA/what-goals-will-ais-have-a-list-of-hypotheses) an AI could pursue, relatively few would align with humanity’s continued survival.

These arguments also assume that, even if an AI’s developers went out of their way to give their creation goals that won’t harm humanity, the systems are likely to exhibit dangerous behavior in the course of pursuing those goals. This is called _instrumental convergence_**.**Certain behaviors — like amassing resources and [power](https://arxiv.org/abs/2206.13353), [improving one’s own capabilities](https://ai-improving-ai.safe.ai/), [deceiving](https://www.cell.com/patterns/fulltext/S2666-3899(24)00103-X) one’s adversaries, or [preserving](https://intelligence.org/files/Corrigibility.pdf) one’s own existence — are useful to AIs for achieving a wide range of goals.

Bostrom, for example, [famously illustrated](https://www.google.com/books/edition/Superintelligence/7_H8AwAAQBAJ?hl=en&gbpv=0) the dangers of instrumental convergence with his “paperclip maximizer” thought experiment. In one version of this scenario, a very powerful AI is given the safe-seeming goal of making exactly one million paper clips. The AI produces the million paper clips, but, wanting to ensure it has achieved its goal according to the original specifications, begins compulsively checking and rechecking its work. Never 100% certain it hadn’t made a mistake in its count, it eventually converts the entire solar system into infrastructure for counting paperclips more accurately.

This doesn’t happen because the AI malfunctions. It happens because the AI’s single-minded optimization of its goal leads to unintended and catastrophic consequences.

## Flaws in the Classic Arguments

In the years since they were originally formulated, significant cracks have appeared in the foundational concepts undergirding the “paperclip maximizer” and other AI risk scenarios.

Indeed, today’s most advanced AI systems seem much more human than Russell, Yudkowsky, Bostrom, or others could have anticipated in the early 2000s. One reason is that today’s frontier AIs are large language models, trained on and designed to model human text. As a result, their behavior is quite human, too. Or it at least feels human, compared with the “[alien](https://www.technologyreview.com/2017/12/08/147199/alpha-zeros-alien-chess-shows-the-power-and-the-peculiarity-of-ai/)” behavior that chess engines and other non-language-based AIs exhibit.

Large language models, which came to prominence around 2017, challenge the relevance of orthogonality: that intelligence and morality are independent behaviors. Granted, perhaps gains in intelligence could _in principle_ develop without any particular bias towards human-like goals. But if AI intelligence is primarily driven by imitation rather than _a priori_ optimization, we can expect that a system’s goals — as well as its reasoning capabilities — will generally approximate those of its human targets. In fact, this bears out in real-world observations: LLMs by and large seem to have [vaguely human-like goals](https://arxiv.org/pdf/2204.05862) when they navigate conversation.

Even more surprising in the context of the classic arguments is the fact that the latest large language models are excellent [_reasoners_](https://www.anthropic.com/news/claude-3-5-sonnet). The classic argument would expect such incredible gains in reasoning to correlate with a tendency towards maximization — but large language models do not appear to be maximizers of any kind. Instead, the gains in reasoning have come, by and large, by _imitating_ human behavior.

It is hard to imagine Claude-4 or GPT-5 neurotically counting and recounting the pile of paperclips it has fetched for its user, consuming the world in the process. This seems to refute the concerns around instrumental convergence.

Further, several recent thinkers have suggested that it is harder than we might have thought to derive dangerous, antisocial AI behavior from bare assumptions about rationality. For example, a concern many AI risk researchers have regarding instrumental convergence is that autonomous agents will seek to prevent humans from shutting them down, as being shut down would prevent the AI from achieving its goals.

However, in 2024, J. Dmitri Gallow of the University of Southern California [investigated](https://philarchive.org/rec/GALIDB) some of Bostrom’s original claims about instrumental convergence and found some logical holes in the assumption that an AI would tend to use harmful means in the pursuit of its ends. Gallow concludes that, while the instrumental convergence thesis contains some “grains of truth,” contentions that it makes existential catastrophe the “default option” are vastly overstated.

Another concern stemming from the concept of instrumental convergence is that as models get increasingly sophisticated they will eventually reach a point where they can research ways to increase their capabilities. This iterative self-improvement would result in AI outcompeting humans as the dominant intellectual entities. Humanity, therefore, would no longer be the master of its own fate.

In 2024, Peter Salib (a co-author of this essay) [argued](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4445706) that rational AIs will not necessarily wish to create new, more powerful versions of themselves. This is because AI self-improvement is risky for the AIs doing the improving in the same way that today’s AI development is risky to the humans doing the developing. Today, humans have no way of guaranteeing that the powerful AI systems they create will share their goals. Likewise, an AI system considering whether to create a more powerful version of itself would have no way to ensure that the more powerful AI would share its goals. In both cases, creating an AI more capable than itself is a risky proposition.

## New Foundations of AI Existential Risk

These cracks in the standard arguments of AI risk don’t mean that risks from AI are no longer a serious concern. Rather, they should help reorient our attention toward the risky scenarios most likely to emerge, given what we now know about AI progress.

One important risk going forward is that AI development may _deviate_ from the LLM trajectory that it is currently on. Recently, the AI industry has shifted from ordinary language models to advanced reasoning models, like [OpenAI’s o3](https://en.wikipedia.org/wiki/OpenAI_o3) and [DeepSeek’s r1](https://arxiv.org/abs/2501.12948). Reasoning models start out as ordinary LLMs. But then, they enter a second phase of training. In the second phase, training optimizes long chains of reasoning to produce correct answers to difficult questions in automatically verifiable domains, like mathematics.

This style of learning is very similar to the one used to produce board game mastering [AlphaZero](https://deepmind.google/discover/blog/alphazero-shedding-new-light-on-chess-shogi-and-go/) and other so-called “alien optimizers” — systems that use unconventional (sometimes even incomprehensible) strategies to accomplish their goals. In other words, the newest generation of reasoning LLMs aren’t pure imitators. If imitation pushed first-generation LLMs toward human-like behavior, and away from the strange behavior the orthogonality thesis predicted, reasoners may swerve back in the other direction.

_Visualization of AlphaZero anticipating possible moves by its opponent in a game of chess. Source:_[_McGrath, et al._](https://arxiv.org/pdf/2111.09259.pdf)

The success of LLMs should therefore not lure us into complacency regarding the ease of alignment. For example, risks from orthogonality are higher in the setting of optimization rather than imitation. If LLMs’ broadly human-like approach to conversation and cooperation stems from imitating humans, then such goals may drift in reasoning models that optimize towards better performance on tasks with automatically verifiable goals.

Another concern worth taking seriously, which we explore in our own [research](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4913167), is that even relatively well-aligned, human-like AI systems may pose a catastrophic risk to humanity. After all: Human beings are relatively well-aligned and human-like, but _humans pose a catastrophic risk to humanity_.

This is partly because humans are in _strategic competition_ with one another over scarce resources. This competition can drive even rational parties into dangerous behavior. Competition between humans causes dangerous outcomes ranging from petty crime to global war.

In short, just as humans compete with other humans, humanity and AI will be competitors for scarce resources. In this competition, there will be both incentives to cooperate and incentives to dominate using violence. Which incentives win out will, in the end, depend on both parties’ expectations about what the other plans to do. In this kind of scenario, how AIs treat humanity may depend reciprocally on how humanity treats AI.

Risks from human-AI strategic competition demand different solutions than the risks envisioned in works like _Superintelligence_.Rather than pure technical solutions, strategic risk must be addressed by creating new cultural, economic, and legal institutions that will facilitate peaceful, long-run AI/human cooperation. We call this approach **cultural alignment**, to contrast it with the technical AI alignment programs already underway at frontier AI labs.

We are just beginning to think about what cultural alignment entails. But the first step, for which we argue at length in a forthcoming academic [paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4913167), would be to grant sufficiently capable AI systems a suite of basic private law rights: to make contracts, to hold property, and to bring certain kinds of lawsuits. This is a start. But it is not the end. Laying the legal and cultural foundations for a world in which humans and very powerful AI systems can peacefully coexist — and even cooperate — will require many new, and possibly radical, ideas. We hope those ideas arrive before the powerful AIs do.

Footnotes

Written by

[ ### Peter N. Salib Peter Salib is an Assistant Professor of Law at the University of Houston Law Center and Associated Faculty in Public Affairs. He also serves as Law and Policy Advisor to the Center for AI Safety in San Francisco and is co-Director of the Center for Law & AI Risk.](https://ai-frontiers.org/author/peter-salib)

[ ### Simon Goldstein Simon Goldstein is an Associate Professor at the University of Hong Kong. His research focuses on AI safety, epistemology, and philosophy of language. Before moving to Hong Kong University, he worked at the Center for AI Safety, the Dianoia Institute of Philosophy, and at Lingnan University in Hong Kong. He received his BA from Yale, and his PhD from Rutgers, where he wrote a dissertation about dynamic semantics.](https://ai-frontiers.org/author/simon-goldstein)

Image: burntime555 / iStock

Continue reading

[](https://ai-frontiers.org/articles/ai-content-must-now-carry-a-label-cameras-are-next)### [AI Content Must Now Carry a Label. Cameras Are Next.](https://ai-frontiers.org/articles/ai-content-must-now-carry-a-label-cameras-are-next)

New EU and California laws require AI companies, and eventually camera makers, to sign their media outputs. It’s our best chance to tell what’s real.

[Eddan Katz](https://ai-frontiers.org/author/eddan-katz)

Aug 13, 2026

[](https://ai-frontiers.org/articles/agi-will-set-off-an-industrial-explosion)### [AGI Will Set Off an Industrial Explosion](https://ai-frontiers.org/articles/agi-will-set-off-an-industrial-explosion)

If AI reaches the point where it can do the cognitive work humans do, robots will proliferate. Standard data on US industry implies a fully automated economy could double its output roughly every year, with no further breakthroughs required.

[Damon Binder](https://ai-frontiers.org/author/damon-binder)

Aug 11, 2026

[Want to contribute to the conversation? Pitch your piece](https://ai-frontiers.org/publish)

## Subscribe to _AI Frontiers_

Thank you for subscribing.

Please try again.

## Subscribe to _AI Frontiers_

Thank you for subscribing.

Please try again.

[](https://ai-frontiers.org/)
_AI Frontiers_ is a platform for expert dialogue and debate on the impacts of artificial intelligence.

[Home](https://ai-frontiers.org/)[Articles](https://ai-frontiers.org/articles)[About](https://ai-frontiers.org/about)[Contact](https://ai-frontiers.org/about#contact)[Publish an Article](https://ai-frontiers.org/publish)[Subscribe](https://ai-frontiers.org/subscribe)[Donate](https://ai-frontiers.org/donate)

The views expressed in our articles reflect the perspectives of individual authors, not necessarily those of the editors or the publication as a whole. Our editorial team values intellectual variety and believes that AI is a complex topic demanding a range of viewpoints, carefully considered.

[](http://x.com/ai_frontiers_)[](https://www.facebook.com/aifrontiers.org)[](https://www.linkedin.com/company/aifrontiers)

© 2026 AI Frontiers

## Subscribe to 

_AI Frontiers_

Thank you for subscribing.

Please try again.
