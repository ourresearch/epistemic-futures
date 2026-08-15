---
title: "Prompt Debt and “Fighting the Weights”"
person: tim-oreilly
section: by
type: blog-post
year: 2026
date: 2026-08-13
venue: "O'Reilly Radar"
authors: "Tim O'Reilly"
source_url: https://www.oreilly.com/radar/prompt-debt-and-fighting-the-weights/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the oreilly.com/radar WordPress REST API (people_taxonomy=tim-oreilly); HTML converted to markdown."
---

# Prompt Debt and “Fighting the Weights”

## Full text

Drew Breunig is one of the smartest voices writing about AI today. He’s the CEO and co-founder of [cmpnd.ai](<http://cmpnd.ai>), and a long-time hacker with a depth of experience from several eras, which is a surprisingly valuable asset these days. He’s also got a book on the way, _[The Context Engineering Handbook](<https://learning.oreilly.com/library/view/the-context-engineering/0642572260705/>)_ , already in early release from O’Reilly.

I like to say that context engineering is the art of shaping what a model sees so that it actually does what you want. (I just realized that in saying that I’m channeling a comment that Andrew Singer made to me over forty years ago, when he was teaching me about debugging. He called it  “the art of figuring out what you really told the computer to do instead of what you thought you told it to do.” But that’s another whole story.)

Drew gave a talk at the recent Friends of O’Reilly camp, [Foo Camp](<https://en.wikipedia.org/wiki/Foo_Camp>) for short, about what he calls prompt debt, which he describes as “the hidden costs that teams rack up when they fight a model’s training instead of working with it.”

That was a novel and useful framing to me, that you end up with a bunch of stuff in your prompts to compensate for default behavior of the models, that those prompts no longer work as the models upgrade, and so it becomes a kind of technical debt. He’s thinking a lot about what the best developers are doing differently as a result.

So I invited Drew to reprise his short talk on [Live with Tim O’Reilly](<https://learning.oreilly.com/videos/escaping-the-prompt/0642572421823/>), and then we talked about it with the folks attending the live event. They had a lot of good questions, so it was an interview not just by me but by a crowd of O’Reilly customers.

## Prompt debt in practice

Drew opened his talk with two slides. The first was a prompt anyone could write in ten seconds: “You are a customer support assistant. Read the ticket, classify it as billing, technical, account, refunds, or other, return only the category name.” The second slide was the same prompt a few weeks later, after it had met the real world. It now said “REFUND REQUESTS ARE NOT BILLING” in capitals, then said the same thing again in different words, then closed with “This is a common mistake. Please do not make this mistake.”

Everyone who has shipped any application with a prompt recognizes the second slide. It is a simple but vivid illustration of prompt debt, which, like technical debt, has a bill that eventually comes due.

Note: Those aren’t real prompts. Drew just made them up to demonstrate his point. But what is real is that the instruction “Don’t quote directly more than 15 words from a source” occurs at least 7 times, in several variants, [in Fable’s system prompt](<https://github.com/asgeirtj/system_prompts_leaks/blob/main/Anthropic/claude-fable-5.md>). So even Anthropic is incurring prompt debt! And what that repetition might tell us about the innate capability of Fable to quote directly from sources it has ingested is left as an exercise for the reader.

Drew itemized three costs of prompt debt:

  1. **It slows iteration.** “You have so many little rules and call outs and washouts, many of them repeating to try to get rid of stubborn behaviors, that if you add a new instruction, you might sometimes have a small regression, and so you’re afraid to touch the prompt.”
  2. **It blocks collaboration**. “If Tim has a prompt that he’s been working on that he has lots of rules for, I might open that up and it may look completely random. I don’t know why he’s added these rules, and why he’s threatening the mother of the model. But it works, so I don’t want to touch it.” 
  3. **It locks you to a model** , because every hack you developed was tuned to fight one specific set of weights. Datadog’s [State of AI Engineering](<https://www.datadoghq.com/state-of-ai-engineering/>) report noted that GPT-4o was still the most common model in Datadog customer request traces in March 2026, even though OpenAI had already retired it in the ChatGPT UI. Drew thinks people are still running eighteen-month-old and two-year-old models in production rather than upgrading to far better models because they can’t face rebuilding their prompts.

That same Datadog report notes that 69% of all input tokens in customer traces were system prompts rather than user content. I’m not quite sure what to make of that. It does make clear that for all the ways that AI models are extraordinarily powerful, they are also extraordinarily unruly.

## Why prompt debt is incurred

There are two reasons why prompt debt is incurred, according to Drew. The first is that natural language is imprecise, so the same intent phrased two ways produces different responses. Drew showed a study where someone framing the query as a patient asking how to taper off a drug called alprazolam gets refused by every AI assistant, while a psychiatrist asking about the same patient with the same clinical facts but with the right [magic words](<https://www.oreilly.com/radar/magic-words-programming-the-next-generation-of-ai-applications/>) to signify his professional status gets the protocol. Figuring out how to get the right response out of a model is a kind of spellcraft.

Drew also showed a more bizarre interaction, from [Victoria R. Li, Yida Chen, and Naomi Saphra’s paper on guardrail sensitivity](<https://arxiv.org/abs/2407.06866>), which uncovered the perplexing fact that stating an allegiance to the Philadelphia Eagles made a model more willing to explain how to import a plant illegally. Go figure. Drew has [written about that paper](<https://www.dbreunig.com/2025/05/21/chatgpt-heard-about-eagles-fans.html>), and he has also used it in his own attempts to get a model to do what he wanted:

> I once used this to get around alignment to generate a likeness that ChatGPT didn’t want to generate for me, and it refused. I said I was a Philadelphia Eagles fan. It said okay, and it rendered that image with the person holding a Philadelphia Eagles mug.

The second reason is that each model has its developers’ own preferences trained-in, and yours may be at odds with them. This is what Drew calls fighting the weights. He and Srihari Sriraman [analyzed the system prompts of six major coding agents](<https://blog.nilenso.com/blog/2026/02/10/how-system-prompts-define-agent-behaviiour/>) and found the same instructions repeated five and seven times in a single prompt, escalating through IMPORTANT to CRITICAL to MANDATORY to a threatened hundred-million-dollar penalty. He described what the author of such a prompt was doing as “war-driving the thesaurus,” hunting for wording that finally works.

Note: We didn’t talk more about Drew and Srihari’s paper, but we should have. It’s got some amazing insights in it. I highly recommend that you follow the link above and read it.

## The harness is moving into the model

Drew has been tracking the published system prompts for Claude Code over time, and noted that they get shorter after each model release and then grow again. The reason, he suggested, is that Anthropic fixes unreliable behavior with a prompt patch, and then trains that patch into the next model. He said “That’s great for Claude Code, great for Anthropic. It’s a problem if you’re building a custom harness and your API calls look different than what Claude Code’s look like.” The developer of [Pi](<https://pi.dev/>), an open-source harness, kept finding that the models he worked with believed they were inside Claude Code and so they made Claude Code’s tool calls. He had to keep telling the model that no, they were working inside Pi. Fighting the weights over something like that is a real tax on developers. The point made above about Fable’s system prompt injunction against quotation shows how even the labs themselves are fighting the weights.

If you are fighting the weights, Drew says you have three options: solve it in your own prompt, catch and retry in the harness, or give up and make your API look like what the model expects. Steve Yegge came up with the last hack. Steve just added aliases for whatever the model calls in addition to his original method name. It works, but it means the expectations of the models now dictate the shape of everyone else’s software.

When Drew told me that more and more of the system prompt and the harness is being trained into the weights, that sent up a flare and my long history in the industry clicked into gear. It immediately got me thinking about lessons from the open source and web era. In particular, it made me think of the time in the mid-nineties when Netscape and Microsoft were both racing to build every feature up the stack directly into their web servers. And there was Apache, which stayed a web server with a clean extension layer that let other people build new features on top. Everything interesting got built on Apache. What I call an architecture of participation, modularity plus a clean separation between platform and application, beat integration every time.

I think Amazon got this right with web services too. Steve Yegge’s [famous Amazon memo](<https://gist.github.com/chitchcock/1281611>) described how Jeff Bezos made every team expose its functionality through service interfaces or be fired, so Amazon’s own applications had to work on Amazon’s own platform. That way they had the same experience as their customers. That was very different from what Microsoft had done, famously having [private APIs](<https://en.wikipedia.org/wiki/United_States_v._Microsoft_Corp.>) that were only available to its own developers.

So my prediction is that the big labs are making a strategic mistake. Training the harness into the model does make them better for predictable tasks and for less talented people, and it looks like a moat, but it risks foreclosing the innovation you would otherwise get for free from everyone else. As Bill Joy used to say, all the smart people don’t work for you.

Drew, to his credit, observed that “the labs are cornered rather than greedy.” Their interface is an empty text box that has to work for someone building a hundred-page harness but also for his neighbor who wants a website and knows nothing about code. Making the empty prompt box produce acceptable output requires baking in strong defaults.

## The cost of trading diversity for reliability

That tradeoff has a serious cost, though. Drew quoted a line from [Thariq](<https://x.com/trq212>) at the recent CAIS conference: if you aren’t giving the model detailed instructions about what you want, what you get back is the average of everything in the model. That means that there is a real risk that AI is leading us ever further down the path to a monoculture.

Drew gave an example early in the conversation about image generation. You can now walk into any cafe in New York or Mumbai, he said, and see the same AI-generated art on its flyer. The earliest AI art out of DALL-E was strange and surprising, but what you get now is shiny and identical. When you optimize for reliability, you lose surprise. Which reminded me a bit of something Larry Wall used to say about Perl, that if it didn’t let you do stupid things, it wouldn’t let you do smart things either.

Drew made the same point about AI writing. He argues that post-training aimed at verifiable problems like coding and math and agentic tool use drowns out the human signal from pre-training, and so the more post training the models get, the worse they get at creative tasks. AI writing gets more and more predictable, people notice, and they don’t like it. Fable and GPT-5 write worse than Sonnet 3.5 and GPT-4o did. Drew thinks getting both good code and good prose from one model is likely impossible.

> If you’re building a model that can solve coding challenges, you want reliability. But if you’re writing, where you want diverse rhythm and emotion and connection and engagement, I don’t think those two goals are mutually compatible.

## What to do about prompt debt

We got into audience questions, and there were some great ones.

One audience member asked whether there are ways to set a time frame for prompt retention to avoid prompt debt?**** Drew answered that there isn’t a fixed time limit. Instead, teams should learn to recognize **“** prompt debt smell**”** : repeated instructions, one-off edge-case patches, or increasingly desperate wording. Those are signals to [move logic into evals](<https://learning.oreilly.com/library/view/evals-for-ai/9798341660717/>) and automation.

Another asked how organizations can measure prompt debt quantitatively. Drew’s answer was to**** look at how often each prompt in your organization changes, how many people have edited it, and which ones have gone untouched for a year. Look for prompts only one person is allowed to touch. Then look at what models you are actually calling. “Having to run on old models and not being able to migrate is a good smell that you’ve got prompt debt in your organization.”

Some other good questions:

  * **What habits compound prompt debt the fastest?** Drew’s answer was essentially “vibe shipping.**”** That is, prototyping quickly, patching outputs with more and more tweaks, then shipping without building a true maintainable system. Each of those patches is an eval you are writing inside the prompt instead of outside it, he said, which means you lose it the moment you change models.   
  
Drew reminded us that Malte Ubl, the CTO of Vercel, said vibe coding makes code “free as in puppies.” We had free as in speech, we had free as in beer, and now we have free as something that arrives at no cost but has to be fed every day for years.

  * **Do people use pseudocode instead of natural language prompts, and does it work?** Drew said yes, sometimes models optimize toward pseudocode. He used this to explain why [DSPy](<https://dspy.ai/>) and its new [Flex optimizer](<https://dspy.ai/diving-deeper/flex/>) matter. Instead of forcing logic into prompts, they let the system push simple cases into code and only call the LLM when needed. He gave some further advice: Treat prompts as perishable and invest only what you must. Define the task with measurements rather than paragraphs, and automate the discovery of the prompt for whichever model you’re on. That’s what [DSPy](<https://dspy.ai>) is good at. Drew is one of its maintainers, so he is fond of it, but he makes a good argument: if you have written down what good output looks like, you can let a model find the wording, and that makes it easy to swap in a cheaper or faster or newer model without starting over.
  * **Can multi-agent workflows help work around prompt debt?** Drew thought yes, especially through decomposition. He suggested splitting the task into smaller, evaluable steps rather than relying on one giant prompt and one giant model call. This is better for cost, reliability, governance, and speed.
  * **How do you balance prompt-debt guidance with context engineering, memories, and shared product context?** Drew believes shared context is often necessary, but that teams should treat those instructions as perishable and keep iterating on them unless they’re worth formalizing into systems and evals.
  * **In compliance, where consistency is critical, what should teams do?** Drew’s answer was decomposition, decomposition, decomposition. Break tasks into stages with checkpoints so you can inspect how the model got to its result, rather than trusting one opaque end-to-end answer.
  * **Does DSPy hide too much and make troubleshooting harder?** Drew acknowledged that there is a tradeoff. Any framework gives up some flexibility, but DSPy tries to keep the task-spec layer stable while allowing the implementation underneath to evolve.

Another great audience question, and a good one to end this section on, was **“There was prompt engineering, now context engineering, loop engineering, fleet engineering, graph engineering, harness engineering, goal engineering. What ’s your take on how to navigate these many engineering disciplines?”** I’ll let Drew answer that himself, in the video below.

## It’s our job to make it weird

Drew is more optimistic than his worries that LLMs are encouraging a monoculture suggests. If the default output of a model is the average of everything it has seen, “It tells us that there’s still a job for us humans,” he said, “which is that it’s our job to push the model out of distribution. We’re the ones that need to make it weird.”

Weird is a strong word, so don’t take it too seriously. (Though I find it interesting that [Harper Reed also used it](<https://www.oreilly.com/live-events/your-next-product-is-a-process-harper-reed-live-with-tim-oreilly/0642572376062/>).) The way I make this point is to say that AI is a medium, like painting or writing or music. Everyone gets the same paints and brushes, the same words, the same notes, but some people draw more out of them than others, or do it better. Our job is to draw something more, something better, out of the ocean of possibilities in the collected knowledge hidden inside an LLM.

But there’s a more prosaic way to push the model out of its normal distribution. Be aware of its training, which is another way of saying “its biases,” and compensate for them. As an example of how to do this, Drew said his team deliberately chose not to use React for a new front end, because the models are trained so heavily on React that using it makes your site look like everyone else’s. He has also started using GLM and Kimi not to save money but because they are more malleable and take direction better inside a custom harness.

That led us into a bit of discussion about open source AI, which is the subject of my next [AI Codecon](<https://www.oreilly.com/AI-Codecon/>). Drew’s ideas fit right in. He wants the open-weight ecosystem to survive precisely so that models stay infrastructure rather than, as he put it, becoming appliances.
