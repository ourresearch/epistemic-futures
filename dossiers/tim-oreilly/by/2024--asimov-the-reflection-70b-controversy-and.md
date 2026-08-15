---
title: "The Reflection 70b Controversy – and Why We Need “Bad Benchmarks”"
person: tim-oreilly
section: by
type: blog-post
year: 2024
date: 2024-09-12
venue: "Asimov’s Addendum"
authors: "Ilan Strauss, Sruly Rosenblat, Tim O'Reilly"
source_url: https://asimovaddendum.substack.com/p/the-reflection-70b-controversy-and
retrieved: 2026-08-13
content: full-text
notes: "Subtitle: “What the Reflection 70b model controversy tells us about LLM evaluation methods & our differing standards for closed vs. open source models”. Asimov’s Addendum, the Substack of Tim O’Reilly and Ilan Strauss on AI commercialization risks and governance; published CC BY 4.0. Retrieved from the free public post page."
---

# The Reflection 70b Controversy – and Why We Need “Bad Benchmarks”

## Full text

# 

> [](<https://substackcdn.com/image/fetch/$s_!uTV9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc926c1b8-eb59-4b7c-a58f-7ee4c003d19f_471x610.png>)

_LLM benchmarks are intended as a tool to rigorously test and compare models’ performance claims. However, as has become clear over the past week, open source and closed source LLMs are not held to the same standards – and simply testing LLMs against the same questions does not change that. Unlike open source models, we are unable to inspect the inner workings of closed source models to ensure that they are not being manipulated at some level._

### **“The world’s top open-source model”**

On September 5th 2024 at 3:00 pm, open source AI was promised a new king. [Matt Shumer](<https://x.com/mattshumer_?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor>) announced his latest creation, Reflection 70B – a model that, according to [every benchmark tested](<https://x.com/mattshumer_/status/1831767014341538166>), was superior to GPT-4o and even outperformed the most powerful version of Anthropic’s Claude on some tests. The model had already been [released](<https://huggingface.co/mattshumer/Reflection-Llama-3.1-70B>) to the public and [tested](<https://x.com/ArtificialAnlys/status/1832505338991395131>) against several benchmarks. The problem? The model wasn’t what it appeared to be – or actually any good at all.

Something was wrong. According to [Artificial Analysis](<https://x.com/ArtificialAnlys/status/1832505338991395131>), the model released to Hugging Face performed roughly the same as LLaMa 3 and noticeably worse than LLaMa 3.1 – the model it [claimed to be trained on](<https://x.com/mattshumer_/status/1832511611841736742>). Shumer quickly interjected on Twitter, writing that there had been issues uploading the correct model to Hugging Face and [announced](<https://x.com/mattshumer_/status/1832509211512623113>) that he would be retraining the model. In the meantime, he provided access to the model through his own internal (private) API for a few researchers to run [benchmarks](<https://x.com/mattshumer_/status/1832807564834136125>) on it.

The model’s test [results](<https://x.com/ArtificialAnlys/status/1832965630472995220>) were largely as advertised but only when run via his private API, meaning there was no way to independently verify what model they were testing. Four days after the initial model release, Schumer released the retrained model on [Hugging Face](<https://huggingface.co/mattshumer/ref_70_e3>) and made what he claimed to be the [internal API](<https://x.com/mattshumer_/status/1832896722999316581?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1832896722999316581%7Ctwgr%5E%7Ctwcon%5Es1_c10&ref_url=notion%3A%2F%2Fwww.notion.so%2FThe-Trench-Coat-Theory-Reflections-on-transparency-in-the-LLM-Space-790c596c3c714b7f96e0b8ff2416d89c>) (the one seemingly used for the benchmark testing) available on OpenRouter.

### **Claude All Along?**

Yet the retrained model was performing [poorly on benchmarks](<https://x.com/ArtificialAnlys/status/1832965630472995220>), while the model hosted by Reflection (via OpenRouter) was having an identity crisis.

When asked to identify itself the model would consistently say it was “[Claude, built by Anthropic”](<https://www.reddit.com/r/LocalLLaMA/comments/1fc9lf4/openrouter_reflection_70b_claims_to_be_claude/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button>). Even more damning, it generated the [same exact results as Claude](<https://www.reddit.com/r/LocalLLaMA/comments/1fc98fu/confirmed_reflection_70bs_official_api_is_sonnet/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button>) when given the same prompts. As the “Claude in a trench coat” theory was gaining traction, something changed: the model was now refusing to say the word “Claude”, even when asked directly. More than 24 hours after the Reflection hosted model was [removed](<https://x.com/OpenRouterAI/status/1833031092120715657>) from OpenRouter, [Matt Shumer](<https://x.com/mattshumer_/status/1833619390098510039>) and [Sahil Chaudhary](<https://x.com/csahil28/status/1833619624589725762>) of Glaive AI acknowledged they had made mistakes but denied using Claude or any third party API behind the scenes.

[](<https://substackcdn.com/image/fetch/$s_!4FGM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3c947045-e356-4e49-ba79-e5650b8a749e_720x778.png>)**Note** : A screenshot depicting Reflection (free) refusing to say the word 'Claude' and instead saying Llama. **Source** : Taken on the open router platform, 7:46 PM September 8th, 2024. The free model was hosted on the official reflection API while the other model was hosted by a third party provider.

### **What does this mean for AI Transparency Going Forward?**

The saga highlights a growing concern in AI evaluation: as LLM systems become more complex, the risks of model opacity causing misleading evaluations, and resulting harms, grows. Reflection’s 70b model also exposes a gap in how we discuss and benchmark not just open source models but closed source ones.   
  
**Much like the ever elusive original Reflection 70B model, we have no reliable way to verify the performance of any closed source model without trusting that their outputs are produced in an honest way**. As context length and processing speeds increase, techniques like “prompt injection” can be used by model creators to game benchmarks and mislead third-party developers. _Prompt injection involves overriding or appending original instructions in the prompt with specific user or developer input_. In this case, the developer can inject benchmark answers behind the scenes whenever an exact match is found between a user’s prompt to the Model and a benchmark prompt.   
  
We may have already witnessed Anthropic using an undisclosed [prompt injection](<https://x.com/kindgracekind/status/1830802464796287106>), involving a hidden message being embedded within the user’s question [to prevent](<https://www.reddit.com/r/ClaudeAI/comments/1f6hcwo/injections_in_the_api/>) its model Claude from outputting copyrighted or “[unethical](<https://www.reddit.com/r/singularity/comments/1f7qc3b/anthropic_sneakily_changing_user_prompts_on_the/>)” content. **Although intended to preserve the model’s legal standing, such an approach could easily be extended beyond positive guardrail enforcement to “performance enhancer”** , allowing models to quickly pass new, more challenging, benchmarks but without actually making the model any smarter.

For all of the talk of LLMs reaching artificial general intelligence (AGI), what if the next unbeatable AI titan is just “Claude in a trench coat”?

### **Encouraging Honesty by Modifying Benchmarks**

**A key reason why we tend to trust benchmark results from open source AI models is that prompt injection is not a viable strategy** : anyone can rerun the benchmark using the released model. Moreover, membership inference (attacks) used to detect if a model’s training data included a test benchmark can be applied to open models, since they provide access to their entire model output, not just the text. This allows one to analyse the probability of an open model producing a certain sequence of tokens (text), from which we can [infer](<https://zjysteven.github.io/mink-plus-plus/>) whether the text was a “member” of the model’s training data. Lastly, any novel benchmark published after the open model’s training date is guaranteed to be excluded from its training datasets, unless the benchmark is based on older text.

**However, with closed source models,** **we don’t have access to their code,** **nor their generated output probabilities for a sequence of text, making membership inference much harder to perform** to assess if the closed model was trained on the benchmark test. We also have no simple way to verify when a closed model was last updated, beyond any announcements they might make.  
  
The question remains: _how to guard against benchmarks being gamed when the public is only provided access to a model’s basic text outputs_? The answer might lie in one of the earliest questions raised about the Reflection 70B model’s benchmark scores.

Early on in the Reflection 70B saga, questions arose from its exceedingly high scores on the GSM8k benchmark. In response it was [claimed](<https://x.com/hughbzhang/status/1831777846899175576>) that a score above 99% might mean that the model was trained on the benchmark’s data as more than 1% of the benchmark in fact was said to contain wrong answers (we were unable to verify this). **Taking this further, what if instead of ensuring that all the answers in a benchmarking test are passed through “correct” answering, we purposely make sure that a certain percentage of the benchmarks “correct” answers are “wrong” – and we keep private which answers are incorrect?** We would then be able to tell when an LLM is performing “too well” on a benchmark, through say prompt injections or benchmark leaking.  
  
In the final analysis, the Reflection controversy shines a spotlight on the **double standards** applied to closed vs open source LLMs. Far from closed source AI models deserving more of our trust, they should garner more of our scrutiny given that the developer can insert arbitrary prompts or code without our knowledge. More generally, we shouldn’t start from the assumption that LLM models (of any type) are produced without undisclosed tweaks being made to them, especially since over time it may become easier to conceal a model’s many components. A good LLM benchmark should be resilient to such model deception — and placing some wrong answers in a benchmark’s dataset may be one effective way to properly guard against this.
