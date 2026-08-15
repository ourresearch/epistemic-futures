---
title: "What MCP and Claude Skills Teach Us About Open Source for AI"
person: tim-oreilly
section: by
type: blog-post
year: 2025
date: 2025-12-03
venue: "O'Reilly Radar"
authors: "Tim O'Reilly"
source_url: https://www.oreilly.com/radar/what-mcp-and-claude-skills-teach-us-about-open-source-for-ai/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the oreilly.com/radar WordPress REST API (people_taxonomy=tim-oreilly); HTML converted to markdown."
---

# What MCP and Claude Skills Teach Us About Open Source for AI

## Full text

The debate about open source AI has largely featured open weight models. But that’s a bit like arguing that in the PC era, the most important goal would have been to have Intel open source its chip designs. That might have been useful to some people, but it wouldn’t have created Linux, Apache, or the collaborative software ecosystem that powers the modern internet. What makes open source transformative is the ease with which people can learn from what others have done, modify it to meet their own needs, and share those modifications with others. And that can’t just happen at the lowest, most complex level of a system. And it doesn’t come easily when what you are providing is access to a system that takes enormous resources to modify, use, and redistribute. It comes from what I’ve called the [architecture of participation](<https://www.oreilly.com/radar/an-architecture-of-participation-for-ai/>).

This architecture of participation has a few key properties:

  * Legibility: You can understand what a component does without understanding the whole system.
  * Modifiability: You can change one piece without rewriting everything.
  * Composability: Pieces work together through simple, well-defined interfaces.
  * Shareability: Your small contribution can be useful to others without them adopting your entire stack.

The most successful open source projects are built from small pieces that work together. Unix gave us a small operating system kernel surrounded by a library of useful functions, together with command-line utilities that could be chained together with pipes and combined into simple programs using the shell. Linux followed and extended that pattern. The web gave us HTML pages you could “view source” on, letting anyone see exactly how a feature was implemented and adapt it to their needs, and HTTP connected every website as a linkable component of a larger whole. Apache didn’t beat Netscape and Microsoft in the web server market by adding more and more features, but instead provided an extension layer so a community of independent developers could add frameworks like Grails, Kafka, and Spark.

## MCP and Skills Are “View Source” for AI

MCP and Claude Skills remind me of those early days of Unix/Linux and the web. MCP lets you write small servers that give AI systems new capabilities such as access to your database, your development tools, your internal APIs, or third-party services like GitHub, GitLab, or Stripe. A skill is even more atomic: a set of plain language instructions, often with some tools and resources, that teaches Claude how to do something specific. Matt Bell from Anthropic remarked in comments on a draft of this piece that a skill can be defined as “the bundle of expertise to do a task, and is typically a combination of instructions, code, knowledge, and reference materials.” Perfect.

What is striking about both is their ease of contribution. You write something that looks like the shell scripts and web APIs developers have been writing for decades. If you can write a Python function or format a Markdown file, you can participate.

This is the same quality that made the early web explode. When someone created a clever navigation menu or form validation, you could view source, copy their HTML and JavaScript, and adapt it to your site. You learned by doing, by remixing, by seeing patterns repeated across sites you admired. You didn’t have to be an Apache contributor to get the benefit of learning from others and reusing their work.

Anthropic’s [MCP Registry](<https://registry.modelcontextprotocol.io/>) and third-party directories like [punkpeye/awesome-mcp-servers](<https://github.com/punkpeye/awesome-mcp-servers>) show early signs of this same dynamic. Someone writes an MCP server for Postgres, and suddenly dozens of AI applications gain database capabilities. Someone creates a skill for analyzing spreadsheets in a particular way, and others fork it, modify it, and share their versions. Anthropic still seems to be feeling its way with user contributed skills, listing in its [skills gallery](<https://github.com/anthropics/skills>) only those they and select partners have created, but they [document how to create them](<https://support.claude.com/en/articles/12512198-how-to-create-custom-skills>), making it possible for anyone to build a reusable tool based on their specific needs, knowledge, or insights. So users are developing skills that make Claude more capable and sharing them via GitHub. It will be very exciting to see how this develops. Groups of developers with shared interests creating and sharing collections of interrelated skills and MCP servers that give models deep expertise in a particular domain will be a potent frontier for both AI and open source.

## GPTs Versus Skills: Two Models of Extension

It’s worth contrasting the MCP and skills approach with [OpenAI’s custom GPTs](<https://help.openai.com/en/articles/8554397-creating-a-gpt>), which represent a different vision of how to extend AI capabilities.

GPTs are closer to apps. You create one by having a conversation with ChatGPT, giving it instructions and uploading files. The result is a packaged experience. You can use a GPT or share it for others to use, but they can’t easily see how it works, fork it, or remix pieces of it into their own projects. GPTs live in OpenAI’s store, discoverable and usable but ultimately contained within the OpenAI ecosystem.

This is a valid approach, and for many use cases, it may be the right one. It’s user-friendly. If you want to create a specialized assistant for your team or customers, GPTs make that straightforward.

But GPTs aren’t participatory in the open source sense. You can’t “view source” on someone’s GPT to understand how they got it to work well. You can’t take the prompt engineering from one GPT and combine it with the file handling from another. You can’t easily version control GPTs, diff them, or collaborate on them the way developers do with code. (OpenAI offers team plans that do allow collaboration by a small group using the same workspace, but this is a far cry from open source–style collaboration.)

Skills and MCP servers, by contrast, are files and code. A skill is literally just a Markdown document you can read, edit, fork, and share. An MCP server is a GitHub repository you can clone, modify, and learn from. They’re artifacts that exist independently of any particular AI system or company.

This difference matters. The [GPT Store](<https://openai.com/index/introducing-the-gpt-store/>) is an app store, and however rich it becomes, an app store remains a walled garden. The iOS App Store and Google Play store host millions of apps for phones, but you can’t view source on an app, can’t extract the UI pattern you liked, and can’t fork it to fix a bug the developer won’t address. The open source revolution comes from artifacts you can inspect, modify, and share: source code, markup languages, configuration files, scripts. These are all things that are legible not just to computers but to humans who want to learn and build.

That’s the lineage skills and MCP belong to. They’re not apps; they’re components. They’re not products; they’re materials. The difference is architectural, and it shapes what kind of ecosystem can grow around them.

Nothing prevents OpenAI from making GPTs more inspectable and forkable, and nothing prevents skills or MCP from becoming more opaque and packaged. The tools are young. _But the initial design choices reveal different instincts about what kind of participation matters_. OpenAI seems deeply rooted in the proprietary platform model. Anthropic seems to be reaching for something more open.1

## Complexity and Evolution

Of course, the web didn’t stay simple. HTML begat CSS, which begat JavaScript frameworks. View source becomes less useful when a page is generated by megabytes of minified React.

But the participatory architecture remained. The ecosystem became more complex, but it did so in layers, and you can still participate at whatever layer matches your needs and abilities. You can write vanilla HTML, or use Tailwind, or build a complex Next.js app. There are different layers for different needs, but all are composable, all shareable.

I suspect we’ll see a similar evolution with MCP and skills. Right now, they’re beautifully simple. They’re almost naive in their directness. That won’t last. We’ll see:

  * Abstraction layers**:** Higher-level frameworks that make common patterns easier.
  * Composition patterns**:** Skills that combine other skills, MCP servers that orchestrate other servers.
  * Optimization: When response time matters, you might need more sophisticated implementations.
  * Security and safety layers**:** As these tools handle sensitive data and actions, we’ll need better isolation and permission models.

The question is whether this evolution will preserve the architecture of participation or whether it will collapse into something that only specialists can work with. Given that Claude itself is very good at helping users write and modify skills, I suspect that we are about to experience an entirely new frontier of learning from open source, one that will keep skill creation open to all even as the range of possibilities expands.

## What Does This Mean for Open Source AI?

**Open weights are necessary but not sufficient.** Yes, we need models whose parameters aren’t locked behind APIs. But model weights are like processor instructions. They are important but not where the most innovation will happen.

**The real action is at the interface layer.** MCP and skills open up new possibilities because they create a stable, comprehensible interface between AI capabilities and specific uses. This is where most developers will actually participate. Not only that, it’s _where people who are not now developers will participate_ , as AI further democratizes programming. At bottom, programming is not the use of some particular set of “programming languages.” It is the skill set that starts with understanding a problem that the current state of digital technology can solve, imagining possible solutions, and then effectively explaining to a set of digital tools what we want them to help us do. The fact that this may now be possible in plain language rather than a specialized dialect means that more people can create useful solutions to the specific problems they face rather than looking only for solutions to problems shared by millions. This has always been a sweet spot for open source. I’m sure many people have said this about the driving impulse of open source, but I first heard it from Eric Allman, the creator of Sendmail, at what became known as [the open source summit in 1998](<https://linuxgazette.net/issue28/rossum.html>): “scratching your own itch.” And of course, history teaches us that this creative ferment often leads to solutions that are indeed useful to millions. Amateur programmers become professionals, enthusiasts become entrepreneurs, and before long, the entire industry has been lifted to a new level.

**Standards enable participation.** MCP is a protocol that works across different AI systems. If it succeeds, it won’t be because Anthropic mandates it but because it creates enough value that others adopt it. That’s the hallmark of a real standard.

**Ecosystems beat models.** The most generative platforms are those in which the platform creators are themselves part of the ecosystem. There isn’t an AI “operating system” platform yet, but the winner-takes-most race for AI supremacy is based on that prize. Open source and the internet provide an alternate, standards-based platform that not only allows people to build apps but to extend the platform itself.

**Open source AI means rethinking open source licenses.**[Most of the software shared on GitHub has no explicit license](<https://www.youtube.com/watch?v=-bAAlPXB2-c>), which means that default copyright laws apply: The software is under exclusive copyright, and the creator retains all rights. Others generally have no right to reproduce, distribute, or create derivative works from the code, even if it is publicly visible on GitHub. But as Shakespeare wrote in _The Merchant of Venice_ , “The brain may devise laws for the blood, but a hot temper leaps o’er a cold decree.” Much of this code is _de facto_ open source, even if not _de jure_. People can learn from it, easily copy from it, and share what they’ve learned.

But perhaps more importantly for the current moment in AI, it was all used to train LLMs, which means that this de facto open source code became a vector through which all AI-generated code is created today. This, of course, has made many developers unhappy, because they believe that AI has been trained on their code without either recognition or recompense. For open source, recognition has always been a fundamental currency. For open source AI to mean something, **we need new approaches to recognizing contributions at every level**.

Licensing issues also come up around what happens to data that flows through an MCP server. What happens when people connect their databases and proprietary data flows through an MCP so that an LLM can reason about it? Right now I suppose it falls under the same license as you have with the LLM vendor itself, but will that always be true?  And, would I, as a provider of information, want to restrict the use of an MCP server depending on a specific configuration of a user’s LLM settings? For example, might I be OK with them using a tool if they have turned off “sharing” in the free version, but not want them to use it if they hadn’t? As one commenter on a draft of this essay put it, “Some API providers would like to prevent LLMs from learning from data even if users permit it. Who owns the users’ data (emails, docs) after it has been retrieved via a particular API or MCP server might be a complicated issue with a chilling effect on innovation.”

There are efforts such as [RSL](<https://rslstandard.org/>) (Really Simple Licensing) and [CC Signals](<https://creativecommons.org/ai-and-the-commons/cc-signals/>) that are focused on content licensing protocols for the consumer/open web, but they don’t yet really have a model for MCP, or more generally for transformative use of content by AI. For example, if an AI uses my credentials to retrieve academic papers and produces a literature review, what encumbrances apply to the results? There is a lot of work to be done here.

## Open Source Must Evolve as Programming Itself Evolves

It’s easy to be amazed by the magic of vibe coding. But treating the LLM as a code generator that takes input in English or other human languages and produces Python, TypeScript, or Java echoes the use of a traditional compiler or interpreter to generate byte code. It reads what we call a “higher-level language” and translates it into code that operates further down the stack. And there’s a historical lesson in that analogy. In the early days of compilers, programmers had to inspect and debug the generated assembly code, but eventually the tools got good enough that few people need to do that any more. (In my own career, when I was writing the manual for Lightspeed C, the first C compiler for the Mac, I remember Mike Kahl, its creator, hand-tuning the compiler output as he was developing it.)

Now programmers are increasingly finding themselves [having to debug the higher-level code generated by LLMs](<https://beyond.addy.ie/>). But I’m confident that will become a smaller and smaller part of the programmer’s role. Why? Because eventually we come to depend on well-tested components. I remember how the original Macintosh user interface guidelines, with predefined user interface components, standardized frontend programming for the GUI era, and how the Win32 API meant that programmers no longer needed to write their own device drivers. In my own career, I remember working on [a book about curses](<https://www.amazon.com/Programming-curses-Manipulation-Nutshell-Handbooks/dp/0937175021>), the Unix cursor-manipulation library for CRT screens, and a few years later the [manuals for Xlib](<https://www.amazon.com/Programming-Manual-Version-Definitive-Guides/dp/1565920023/ref=sr_1_1?crid=3H5VWZYCSCIRI&dib=eyJ2IjoiMSJ9.H5FnhlmJ-PAAkopJZaSBmUdVMUHR8bcMarE892nn5GoXsMhFYdTcXtM2dpKNxRRM0fTeDfkXXKAE8sYmzaO3es6wwz44w2BthrBS_jOZrRU.yiTRmh1MrZVZ8qUSZVhjNMta96m_nQ7oH1Ra007dg1k&dib_tag=se&keywords=Xlib+programming+manual&qid=1763998807&s=books&sprefix=xlib+programming+manual%2Cstripbooks%2C133&sr=1-1>), the low-level programming interfaces for the X Window System. This kind of programming soon was superseded by user interface toolkits with predefined elements and actions. So too, the roll-your-own era of web interfaces was eventually standardized by powerful frontend JavaScript frameworks.

Once developers come to rely on libraries of preexisting components that can be combined in new ways, what developers are debugging is no longer the lower-level code (first machine code, then assembly code, then hand-built interfaces) but the architecture of the systems they build, the connections between the components, the integrity of the data they rely on, and the quality of the user interface. In short, developers move up the stack.

LLMs and AI agents are calling for us to move up once again. We are groping our way towards a new paradigm in which we are not just building MCPs as instructions for AI agents but developing new programming paradigms that blend the rigor and predictability of traditional programming with the knowledge and flexibility of AI. As Phillip Carter memorably noted, LLMs are [_inverted computers_](<https://www.phillipcarter.dev/posts/llms-computers>) relative to those with which we’ve been familiar: “We’ve spent decades working with computers that are incredible at precision tasks but need to be painstakingly programmed for anything remotely fuzzy. Now we have computers that are adept at fuzzy tasks but need special handling for precision work.” That being said, LLMs are becoming increasingly adept at knowing what they are good at and what they aren’t. Part of the whole point of MCP and skills is to give them clarity about how to use the tools of traditional computing to achieve their fuzzy aims.

Consider the evolution of agents from those based on “browser use” (that is, working with the interfaces designed for humans) to those based on making API calls (that is, working with the interfaces designed for traditional programs) to those based on MCP (relying on the intelligence of LLMs to read documents that explain the tools that are available to do a task). An MCP server looks a lot like the formalization of prompt and context engineering into components. A look at what purports to be a leaked [system prompt for ChatGPT](<https://www.reddit.com/r/PromptEngineering/comments/1j5mca4/i_made_chatgpt_45_leak_its_system_prompt/>) suggests that the pattern of MCP servers was already hidden in the prompts of proprietary AI apps: “Here’s how I want you to act. Here are the things that you should and should not do. Here are the tools available to you.”

But while system prompts are bespoke, MCP and skills are a step towards formalizing plain text instructions to an LLM so that they can become reusable components. In short, MCP and skills are early steps towards a system of what we can call “fuzzy function calls.”

## Fuzzy Function Calls: Magic Words Made Reliable and Reusable

This view of how prompting and context engineering fit with traditional programming connects to something [I wrote about recently](<https://www.oreilly.com/radar/magic-words-programming-the-next-generation-of-ai-applications/>): LLMs natively understand high-level concepts like “plan,” “test,” and “deploy”; industry standard terms like “TDD” (Test Driven Development) or “PRD” (Product Requirements Document); competitive features like “study mode”; or specific file formats like “.md file.” These “magic words” are prompting shortcuts that bring in dense clusters of context and trigger particular patterns of behavior that have specific use cases.

But right now, these magic words are unmodifiable. They exist in the model’s training, within system prompts, or locked inside proprietary features. You can use them if you know about them, and you can write prompts to modify how they work in your current session. But you can’t inspect them to understand exactly what they do, you can’t tweak them for your needs, and you can’t share your improved version with others.

Skills and MCPs are a way to make magic words visible and extensible. They formalize the instructions and patterns that make an LLM application work, and they make those instructions something you can read, modify, and share.

Take ChatGPT’s study mode as an example. It’s a particular way of helping someone learn, by asking comprehension questions, testing understanding, and adjusting difficulty based on responses. That’s incredibly valuable. But it’s locked inside ChatGPT’s interface. You can’t even access it via the ChatGPT API. What if study mode was published as a skill? Then you could:

  * See exactly how it works. What instructions guide the interaction?
  * Modify it for your subject matter. Maybe study mode for medical students needs different patterns than study mode for language learning.
  * Fork it into variants. You might want a “Socratic mode” or “test prep mode” that builds on the same foundation.
  * Use it with your own content and tools. You might combine it with an MCP server that accesses your course materials.
  * Share your improved version and learn from others’ modifications.

This is the next level of AI programming “up the stack.” You’re not training models or vibe coding Python. You’re elaborating on concepts the model already understands, more adapted to specific needs, and sharing them as building blocks others can use.

****Building reusable libraries of fuzzy functions is the future of open source AI.****

## The Economics of Participation

There’s a deeper pattern here that connects to a rich tradition in economics: mechanism design. Over the past few decades, economists like [Paul Milgrom](<https://en.wikipedia.org/wiki/Paul_Milgrom>) and [Al Roth](<https://en.wikipedia.org/wiki/Alvin_E._Roth>) won Nobel Prizes for showing how to design better markets: matching systems for medical residents, spectrum auctions for wireless licenses, kidney exchange networks that save lives. These weren’t just theoretical exercises. They were practical interventions that created more efficient, more equitable outcomes by changing the rules of the game.

Some tech companies understood this. As chief economist at Google, Hal Varian didn’t just analyze ad markets, he helped design the ad auction that made Google’s business model work. At Uber, Jonathan Hall applied mechanism design insights to dynamic pricing and marketplace matching to build a “thick market” of passengers and drivers. These economists brought economic theory to bear on platform design, creating systems where value could flow more efficiently between participants.

Though not guided by economists, _the web and the open source software revolution were also not just technical advances but breakthroughs in market design_. They created information-rich, participatory markets where barriers to entry were lowered. It became easier to learn, create, and innovate. Transaction costs plummeted. Sharing code or content went from expensive (physical distribution, licensing negotiations) to nearly free. Discovery mechanisms emerged: Search engines, package managers, and GitHub made it easy to find what you needed. Reputation systems were discovered or developed. And of course, network effects benefited everyone. Each new participant made the ecosystem more valuable.

These weren’t accidents. They were the result of architectural choices that made internet-enabled software development into a generative, participatory market.

AI desperately needs similar breakthroughs in mechanism design. Right now, most economic analysis of AI focuses on the wrong question: “How many jobs will AI destroy?” This is the mindset of an extractive system, where AI is something done _to_ workers and to existing companies rather than _with_ them. The right question is: “How do we design AI systems that create participatory markets where value can flow to all contributors?”

Consider what’s broken right now:

  * Attribution is invisible. When an AI model benefits from training on someone’s work, there’s no mechanism to recognize or compensate for that contribution.
  * Value capture is concentrated. A handful of companies capture the gains, while millions of content creators, whose work trained the models and are consulted during inference, see no return.
  * Improvement loops are closed. If you find a better way to accomplish a task with AI, you can’t easily share that improvement or benefit from others’ discoveries.
  * Quality signals are weak. There’s no good way to know if a particular skill, prompt, or MCP server is well-designed without trying it yourself.

MCP and skills, viewed through this economic lens, are early-stage infrastructure for a participatory AI market. The MCP Registry and skills gallery are primitive but promising marketplaces with discoverable components and inspectable quality. When a skill or MCP server is useful, it’s a legible, shareable artifact that can carry attribution. While this may not redress the “[original sin](<https://www.oreilly.com/radar/how-to-fix-ais-original-sin/>)” of copyright violation during model training, it does perhaps point to a future where content creators, not just AI model creators and app developers, may be able to monetize their work.

But we’re nowhere near having the mechanisms we need. We need systems that efficiently match AI capabilities with human needs, that create sustainable compensation for contribution, that enable reputation and discovery, that make it easy to build on others’ work while giving them credit.

This isn’t just a technical challenge. It’s a challenge for economists, policymakers, and platform designers to work together on mechanism design. The architecture of participation isn’t just a set of values. It’s a powerful framework for building markets that work. The question is whether we’ll apply these lessons of open source and the web to AI or whether we’ll let AI become an extractive system that destroys more value than it creates.

## A Call to Action

I’d love to see OpenAI, Google, Meta, and the open source community develop a robust architecture of participation for AI.

**Make innovations inspectable.** When you build a compelling feature or an effective interaction pattern or a useful specialization, consider publishing it in a form others can learn from. Not as a closed app or an API to a black box but as instructions, prompts, and tool configurations that can be read and understood. Sometimes competitive advantage comes from what you share rather than what you keep secret.

**Support open protocols.** MCP’s early success demonstrates what’s possible when the industry rallies around an open standard. Since Anthropic introduced it in late 2024, MCP has been adopted by OpenAI (across ChatGPT, the Agents SDK, and the Responses API), Google (in the Gemini SDK), Microsoft (in Azure AI services), and a rapidly growing ecosystem of development tools from Replit to Sourcegraph. This cross-platform adoption proves that when a protocol solves real problems and remains truly open, companies will embrace it even when it comes from a competitor. The challenge now is to maintain that openness as the protocol matures.

**Create pathways for contribution at every level.** Not everyone needs to fork model weights or even write MCP servers. Some people should be able to contribute a clever prompt template. Others might write a skill that combines existing tools in a new way. Still others will build infrastructure that makes all of this easier. All of these contributions should be possible, visible, and valued.

**Document magic.** When your model responds particularly well to certain instructions, patterns, or concepts, make those patterns explicit and shareable. The collective knowledge of how to work effectively with AI shouldn’t be scattered across X threads and Discord channels. It should be formalized, versioned, and forkable.

**Reinvent open source licenses.** Take into account the need for recognition not only during training but inference. Develop protocols that help manage rights for data that flows through networks of AI agents.

**Engage with mechanism design.** Building a participatory AI market isn’t just a technical problem, it’s an economic design challenge. We need economists, policymakers, and platform designers collaborating on how to create sustainable, participatory markets around AI. Stop asking “How many jobs will AI destroy?” and start asking “How do we design AI systems that create value for all participants?” The architecture choices we make now will determine whether AI becomes an extractive force or an engine of broadly shared prosperity.

The future of programming with AI won’t be determined by who publishes model weights. It’ll be determined by who creates the best ways for ordinary developers to participate, contribute, and build on each other’s work. And that includes the next wave of developers: users who can create reusable AI skills based on their special knowledge, experience, and human perspectives.

We’re at a choice point. We can make AI development look like app stores and proprietary platforms, or we can make it look like the open web and the open source lineages that descended from Unix. I know which future I’d like to live in.

* * *

### Footnotes

  1. I shared a draft of this piece with members of the Anthropic MCP and Skills team, and in addition to providing a number of helpful technical improvements, they confirmed a number of points where my framing captured their intentions. Comments ranged from “Skills were designed with composability in mind. We didn’t want to confine capable models to a single system prompt with limited functions” to “I love this phrasing since it leads into considering the models as the processing power, and showcases the need for the open ecosystem on top of the raw power a model provides” and “In a recent talk, I compared the models to processors, agent runtimes/orchestrations to the OS, and Skills as the application.” However, all of the opinions are my own and Anthropic is not responsible for anything I’ve said here.
