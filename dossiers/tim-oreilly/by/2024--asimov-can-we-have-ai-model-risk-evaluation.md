---
title: "Risk without Uncertainty? OpenAI would like us to think so..."
person: tim-oreilly
section: by
type: blog-post
year: 2024
date: 2024-10-01
venue: "Asimov’s Addendum"
authors: "Ilan Strauss, Tim O'Reilly"
source_url: https://asimovaddendum.substack.com/p/can-we-have-ai-model-risk-evaluation
retrieved: 2026-08-13
content: full-text
notes: "Subtitle: “AI model evaluations, such as those conducted by OpenAI in its GPT system cards, aim to quantify model risks but often fail to account for uncertainty.”. Asimov’s Addendum, the Substack of Tim O’Reilly and Ilan Strauss on AI commercialization risks and governance; published CC BY 4.0. Retrieved from the free public post page."
---

# Risk without Uncertainty? OpenAI would like us to think so...

## Full text

AI model developers release system cards to evaluate their AI models for risks. For example, here is OpenAI’s [system card](<https://assets.ctfassets.net/kftzwdyauwt9/67qJD51Aur3eIc96iOfeOP/71551c3d223cd97e591aa89567306912/o1_system_card.pdf>) for its latest “strawberry” model, also known as GPT o1-preview and o1-mini. If someone had no prior knowledge of AI model risk evaluation, they might reasonably expect the system card to cover one or more of the following types of risks:

  1. _Model risk as uncertainty_. Uncertainty is “hard to measure” risk, as [Nate Silver](<https://fs.blog/the-difference-between-risk-and-uncertainty/>) notes.****

  2. _Model risk as technological capabilities_. This also relates to risks stemming from AI as a “dual-use” (military) technology, along with “bad actor” risks.

  3. _Model risk as systemic connections and dependencies_ , including from or to the ecosystems built on top of it, connected networks, and infrastructural reliances.

  4. _Model risk as concentrated power_. This is a form of ownership risk, stemming from concentrated corporate control of socially vital technologies. (We wouldn’t expect the corporate owners themselves to evaluate this!) 

**Model system cards are largely evaluations of item 2, “model risk as technological capabilities”.** This tends to focus on highly uncertain future risks related to the AI model becoming autonomous (“[its alive](<https://www.youtube.com/watch?v=1qNeGSJaQ9Q>)”), rather than on practical evaluations of the model’s performance in typical, often commercial, environments.

[](<https://substackcdn.com/image/fetch/$s_!2kX_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F87f50cfc-f9f3-4136-822d-e57e844d4911_1003x1500.jpeg>)The official theatrical of _Frankenstein_ (1931) by Karoly Grosz (https://commons.wikimedia.org/w/index.php?curid=36230530). Existential model risks, such as from a model gaining autonomy, tend to be the focus of AI model risk evaluations, though increasingly less so.

  
**“Model risk as uncertainty” (item 1 above) is largely absent from AI model evaluation results, including OpenAI’s latest o1 model system card**. How can we tell? Well, risk assessments in the o1 system card boil down to single figures most of the time, without any indication of how certain these estimates are, e.g. model accuracy is “0.38”, model hallucination rate is “0.61”. As [Andrew Gelman](<https://statmodeling.stat.columbia.edu/2024/08/13/the-river-the-village-and-the-fort-nate-silvers-new-book-on-the-edge/>) puts it when discussing statistical research: “a lot of effort gets put into avoiding or denying uncertainty”.   
  
**This omission by OpenAI is especially notable because its system card tries to evaluate highly uncertain future risks** , such as potential _model autonomy_ , but based on the model’s current capabilities. Moreover, it tries to measure specific model behaviors, such as _deception_ , that might only emerge in certain contexts or at certain frequencies.   
  
**LLM behavior is also inherently uncertain**. The model’s responses are highly sensitive to factors like the query, hyperparameters, and context, all of which introduce variability in a model’s outputs. Using another LLM as the evaluator introduces further uncertainty, just as human evaluation introduces its own uncertainties (e.g., which humans, which topics, which contexts and what sample size?).  
  
**As an interesting aside, LLMs seem to be computationally deterministic in their outputs** (even if [practical stuff](<https://www.taivo.ai/__are-llms-deterministic/>) [complicates](<https://barryzhang.substack.com/p/making-peace-with-llm-non-determinism>) this): Given the same input and conditions, the model should generate the same probabilities for the next token. The variability we see in outputs stems largely from the sampling methods applied on top of these probabilities, such as[ top-k sampling or temperature](<https://medium.com/@mariealice.blete/llms-determinism-randomness-36d3f3f1f793>) sampling. These techniques introduces randomness, producing different outputs for the same input.   
  
But even without this sampling layer, **uncertainty should persist in LLM evaluation results because it’s impractical to test all possible model input-output combinations**. The space of potential queries is vast, and testing can only cover a small sample of interactions. The limited sampling of the model’s potential predictions, whether by humans or automated methods, inevitably introduces uncertainty into the model evaluation process.

**Calculating and showing model uncertainty usually comes by providing an interval** – a likely range of estimates – such as a confidence or credible interval (sometimes generated using bootstrapping), rather than just a single number. Another approach is to assess the model’s performance out of sample, using entirely new data not seen during training. This method relates to [model calibration](<https://www.giskard.ai/glossary/model-calibration>), which tries to ensure that the model’s predicted probabilities align with actual outcomes.  
  
**So, why the omission by OpenAI of uncertainty from most of its model evaluations**? Maybe computer scientists aren’t always familiar with common statistical practice, something [Rumman Chowdhury](<https://www.state.gov/announcement-of-the-2024-cohort-of-u-s-science-envoys/>) confirmed to Ilan based on her past experiences (she also sent [this](<https://www.anthropic.com/news/evaluating-ai-systems>) really useful applied discussion.) Ilan also checked the [leading AI textbook](<https://aima.cs.berkeley.edu/>) by Stuart Russell and Peter Norvig (4th edition). There is an entire chapter on “Quantifying Uncertainty”, but devoted largely to uncertainty facing AI in the external environment.

**Given how large LLMs are, is there a way to introduce measures of uncertainty into their evaluations**? Somewhat mysteriously, Andrew [Gelman](<https://statmodeling.stat.columbia.edu/2024/08/13/the-river-the-village-and-the-fort-nate-silvers-new-book-on-the-edge/>) generally recommends: “studying the process, not just the particular dataset,” including through regularization techniques (like [partial pooling](<https://en.wikipedia.org/wiki/James%E2%80%93Stein_estimator>)). By itself though, this isin’t enough. So I e-mailed Andrew to ask why he thinks it is that computer scientists, and LLM risk evaluations in particular, do not report on uncertainty levels in their model evaluations? I look forward to reading the response on his blog (which he said is forthcoming - we will link to it when its out.)

Lastly, one interesting possible approach to quantifying LLM risk was given to us by [Michał Oleszak](<https://michaloleszak.com/>), and comes from **finance’s Value at Risk (VaR) model** , which tries to assess the left tail, or loss, of a financial portfolio over time, for a specific confidence level. Despite a VaR model’s [much debated](<https://en.wikipedia.org/wiki/Value_at_risk>) shortcomings, perhaps similar approaches can be designed to assess the potential for LLMs to produce harmful content or behaviours, within a certain time frame, based on historical prompt data? Seems worth exploring further.   
  
Either way, to take AI model risk evaluations seriously, model developers need to introduce reliable methods to quantify model uncertainty. Ignoring how uncertain we are about a model’s range of potential outcomes doesn’t make those outcomes any less likely to occur — it just makes us worry less about them.
