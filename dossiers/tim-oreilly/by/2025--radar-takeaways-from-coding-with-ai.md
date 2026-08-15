---
title: "Takeaways from Coding with AI"
person: tim-oreilly
section: by
type: blog-post
year: 2025
date: 2025-05-14
venue: "O'Reilly Radar"
authors: "Tim O'Reilly"
source_url: https://www.oreilly.com/radar/takeaways-from-coding-with-ai/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the oreilly.com/radar WordPress REST API (people_taxonomy=tim-oreilly); HTML converted to markdown."
---

# Takeaways from Coding with AI

## Full text

I thought I’d offer a few takeaways and reflections based on last week’s first AI Codecon virtual conference, [Coding with AI: The End of Software Development as We Know It](<https://www.oreilly.com/CodingwithAI/>). I’m also going to include a few short video excerpts from the event. If you registered for Coding with AI or if you’re an existing O’Reilly subscriber, you can watch or rewatch the whole thing on the O’Reilly learning platform. If you aren’t a subscriber yet, it’s easy to [start a free trial](<https://www.oreilly.com/start-trial/>). We’ll also be posting additional excerpts on the [O’Reilly YouTube channel](<https://www.youtube.com/oreillymedia>) in the next few weeks.

But on to the promised takeaways.

First off, Harper Reed is a mad genius who made everyone’s head explode. (Camille Fournier apparently has joked that Harper has rotted his brain with AI, and Harper actually agreed.) Harper discussed his design process in a talk that you might want to run at half speed. His greenfield workflow is to start with an idea. Give your idea to a chat model and have it ask you questions with yes/no answers. Have it extract all the ideas. That becomes your spec or PRD. Use the spec as input to a reasoning model and have it generate a plan; then feed that plan into a different reasoning model and have it generate prompts for code generation for both the application and tests. He’s having a wild time.

[_Agile Manifesto_](<https://agilemanifesto.org/>) coauthor Kent Beck was also on Team Enthusiasm. He told us that augmented coding with AI was “the most fun I’ve ever had,” and said that it “reawakened the joy of programming.” Nikola Balic agreed: “As Kent said, it just brought the joy of writing code, the joy of programming, it brought it back. So I’m now generating more code than ever. I have, like, a million lines of code in the last month. I’m playing with stuff that I never played with before. And I’m just spending an obscene amount of tokens.” But in the future, “I think that we won’t write code anymore. We will nurture it. This is a vision. I’m sure that many of you will disagree but let’s look years in the future and how everything will change. I think that we are more going toward intention-driven programming.”

Others, like Chelsea Troy, Chip Huyen, swyx, Birgitta Böckeler, and Gergely Orosz weren’t so sure. Don’t get me wrong. They think that there’s a ton of amazing stuff to do and learn. But there’s also a lot of hype and loose thinking. And while there will be a lot of change, a lot of existing skills will remain important.

Here’s Chelsea’s critique of the [recent paper that claimed a 26% productivity increase](<https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4945566>) for developers using generative AI.

If Chelsea will do a sermon every week in the Church of Don’t Believe Everything You Read that consists of her showing off various papers and giving her dry and insightful perspective on how to think about them more clearly, I am so there.

I was a bit surprised by how skeptical Chip Huyen and swyx were about A2A. They really schooled me on the notion that the future of agents is in direct AI-to-AI interactions. I’ve been of the opinion that having an AI agent work the user-facing interface of a remote website is a throwback to screen scraping—surely a transitional stage—and while calling an API will be the best way to handle a deterministic process like payment, there will be a whole lot of other activities, like taste matching, that are ideal for LLM to LLM. When I think about AI shopping for example, I imagine an agent that has learned and remembered my tastes and preferences and specific goals communicating with an agent that knows and understands the inventory of a merchant. But swyx and Chip weren’t buying it, at least not now. They think that’s a long way off, given the current state of AI engineering. I was glad to have them bring me back to earth.

(For what it’s worth, Gabriela de Queiroz, director of AI at Microsoft, agrees. On [her episode](<https://www.oreilly.com/radar/podcast/generative-ai-in-the-real-world-the-startup-opportunity-with-gabriela-de-queiroz/>) of O’Reilly’s _Generative AI in the Real World_ podcast, she said, “If you think we’re close to AGI, try building an agent, and you’ll see how far we are from AGI.”)

Angie Jones, on the other hand, was pretty excited about agents in her [lightning talk](<https://en.wikipedia.org/wiki/Lightning_talk>) about how MCP is bringing the “mashup” era back to life. I was struck in particular by Angie’s comments about MCP as a kind of universal adapter, which abstracts away the underlying details of APIs, tools, and data sources. That was a powerful echo of Microsoft’s platform dominance in the Windows era, which in many ways began with the Win32 API, which abstracted away all the underlying hardware such that application writers no longer had to write drivers for disk drives, printers, screens, or communications ports. I’d call that a power move by Anthropic, except for the blessing that they introduced MCP as an open standard. Good for them!

Birgitta Böckeler talked frankly about how LLMs helped reduce cognitive load and helped think through a design. But much of our daily work is a poor fit for AI: large legacy codebases where we change more code than we create, antiquated technology stacks, poor feedback loops. We still need code that is simple and modular—that’s easier for LLMs to understand, as well as humans. We still need good feedback loops that show us whether code is working (echoing Harper). We still need logical, analytical, critical thinking about problem solving. At the end, she summarized both poles of the conference, saying we need cultures that reward both experimentation and skepticism.

Gergely Orosz weighed in on the continued importance of software engineering. He talked briefly about books he was reading, starting with Chip Huyen’s [_AI Engineering_](<https://www.oreilly.com/library/view/ai-engineering/9781098166298/>), but perhaps the more important point came a bit later: He held up several software engineering classics, including [_The Mythical Man-Month_](<https://www.oreilly.com/library/view/mythical-man-month-the/0201835959/>) and [_Code Complete_](<https://www.oreilly.com/library/view/code-complete-2nd/0735619670/>). These books are decades old, Gergely noted, but even with 50 years of tool development, the problems they describe are still with us. AI isn’t likely to change that.

In this regard, I was struck by Camille Fournier’s assertion that managers love to see their senior developers using AI tools, because they have the skills and judgment to get the most out of it, but often want to take it away from junior developers who can use it too uncritically. Addy Osmani expressed the concern that basic skills (“muscle memory”) would degrade, both for junior and senior software developers. (Juniors may never develop those skills in the first place.) Addy’s comment was echoed by many others. Whatever the future of computing holds, we still need to know how to analyze a problem, how to think about data and data structures, how to design, and how to debug.

In that same discussion, Maxi Ferreira and Avi Flombaum brought up the critique that LLMs will tend to choose the most common languages and frameworks when trying to solve a problem, even when there are better tools available. This is a variation of the observation that LLMs by default tend to produce a consensus solution. But the discussion highlighted for me that this represents a risk to skill acquisition and learning of up-and-coming developers too. It also made me wonder about the future of programming languages. Why develop new languages if there’s never going to be enough training data for LLMs to use them?

Almost all of the speakers talked about the importance of up-front design when programming with AI. Harper Reed said that this sounds like a return to waterfall, except that the cycle is so fast. Clay Shirky [once observed](<https://pahlkadot.medium.com/dear-governor-elect-72e2f5e3bfdb>) that waterfall development “amounts to a pledge by all parties not to learn anything while doing the actual work,” and that failure to learn while doing has hampered countless projects. But if AI codegen is waterfall with a fast learning cycle, that’s a very different model. So this is an important thread to pull on.

Lili Jiang’s closing emphasis that evals are much more complex with LLMs really resonated for me, and was consistent with many of the speakers’ takes about how much further we have to go. Lili compared a data science project she had done at Quora, where they started with a carefully curated dataset (which made eval relatively easy), with trying to deal with self-driving algorithms at Waymo, where you don’t start out with “ground truth” and the right answer is highly context dependent. She asked, “How do you evaluate an LLM given such a high degree of freedom in terms of its output?” and pointed out that the code to do evals properly can be as large or larger than the code used to shape the actual functionality.

This totally fits with my sense of why anyone imagining a programmer-free future is out of touch. AI makes some things that used to be hard trivially easy and some things that used to be easy much, much harder. Even if you had an LLM as judge doing the evals, there’s an awful lot to be figured out.

I want to finish with Kent Beck’s thoughtful perspective on how different mindsets are needed at different stages in the evolution of a new market.

Finally, a big THANK YOU to everyone who gave their time to be part of our first AI Codecon event. Addy Osmani, you were the perfect cohost. You’re knowledgeable, a great interviewer, charming, and a lot of fun to work with. Gergely Orosz, Kent Beck, Camille Fournier, Avi Flombaum, Maxi Ferreira, Harper Reed, Jay Parikh, Birgitta Böckeler, Angie Jones, Craig McLuckie, Patty O’Callaghan, Chip Huyen, swyx Wang, Andrew Stellman, Iyanuoluwa Ajao, Nikola Balic, Brett Smith, Chelsea Troy, Lili Jiang—you all rocked. Thanks so much for sharing your expertise. Melissa Duffield, Julie Baron, Lisa LaRew, Keith Thompson, Yasmina Greco, Derek Hakim, Sasha Divitkina, and everyone else at O’Reilly who helped bring AI Codecon to life, thanks for all the work you put in to make the event a success. And thanks to the almost 9,000 attendees who gave your time, your attention, and your provocative questions in the chat.

Subscribe to [our YouTube channel](<https://www.youtube.com/oreillymedia>) to watch highlights from the event or [become an O’Reilly member](<https://www.oreilly.com/>) to watch the entire conference before the next one September 9. We’d love to hear what landed for you—let us know in the comments.
