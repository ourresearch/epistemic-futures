---
title: "Magic Words: Programming the Next Generation of AI Applications"
person: tim-oreilly
section: by
type: blog-post
year: 2025
date: 2025-10-15
venue: "O'Reilly Radar"
authors: "Tim O'Reilly"
source_url: https://www.oreilly.com/radar/magic-words-programming-the-next-generation-of-ai-applications/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the oreilly.com/radar WordPress REST API (people_taxonomy=tim-oreilly); HTML converted to markdown."
---

# Magic Words: Programming the Next Generation of AI Applications

## Full text

> _“Strange was obliged to invent most of the magic he did, working from general principles and half-remembered stories from old books.”_  
>   
>  _—_ Susanna Clarke,_Jonathan Strange & Mr Norrell_

Fairy tales, myths, and fantasy fiction are full of magic spells. You say “abracadabra” and something profound happens.1 Say “open sesame” and the door swings open.

It turns out that this is also a useful metaphor for what happens with large language models.

I first got this idea from David Griffiths’s O’Reilly course on [using AI to boost your productivity](<https://learning.oreilly.com/live-events/using-generative-ai-to-boost-your-personal-productivity/0636920099736/>). He gave a simple example. You can tell ChatGPT “Organize my task list using the Eisenhower four-sided box.” And it just knows what to do, even if you yourself know nothing about General Dwight D. Eisenhower’s approach to decision making. David then suggests his students instead try “Organize my task list using Getting Things Done,” or just “Use GTD.” Each of those phrases is shorthand for systems of thought, practices, and conventions that the model has learned from human culture.

These are magic words. They’re magic not because they do something unworldly and unexpected but because they have the power to summon patterns that have been encoded in the model. The words act as keys, unlocking context and even entire workflows.

We all use magic words in our prompts. We say something like “Update my _resume_ ” or “Draft a _Substack post_ ” without thinking how much detailed prompting we’d have to do to create that output if the LLM didn’t already know the magic word.

Every field has a specialized language whose terms are known only to its initiates. We can be fanciful and pretend they are magic spells, but the reality is that each of them is really a kind of **fuzzy function call** to an LLM, bringing in a body of context and unlocking a set of behaviors and capabilities. When we ask an LLM to write a program in _Javascript_ rather than _Python_ , we are using one of these fuzzy function calls. When we ask for output as an _.md_ file, we are doing the same. Unlike a function call in a traditional programming language, it doesn’t always return the same result, which is why developers have an opportunity to enhance the magic.

## **From Prompts to Applications**

The next light bulb went off for me in a conversation with Claire Vo, the creator of an AI application called [ChatPRD](<http://chatprd.ai>). Claire spent years as a product manager, and as soon as ChatGPT became available, began using it to help her write product requirement documents or PRDs. Every product manager knows what a PRD is. When Claire prompted ChatGPT to “write a PRD,” it didn’t need a long preamble. That one acronym carried decades of professional practice. But Claire went further. She refined her prompts, improved them, and taught ChatGPT how to think like her. Over time, she had trained a system, not at the model level, but at the level of context and workflow.

Next, Claire turned her workflow into a product. That product is a software interface that wraps up a number of related magic words into a useful package. It controls access to her customized magic spell, so to speak. Claire added detailed prompts, integrations with other tools, access control, and a whole lot of traditional programming in a next-generation application that uses a mix of traditional software code and “magical” fuzzy function calls to an LLM. ChatPRD even interviews users to learn more about their goals, customizing the application for each organization and use case.

Claire’s [quickstart guide to ChatPRD](<https://www.chatprd.ai/blog/chatprd-quickstart-guide>) is a great example of what a magic-word (fuzzy function call) application looks like.

You can also see how magic words are crafted into magic spells and how these spells are even part of the architecture of applications like Claude Code through the explorations of developers like Jesse Vincent and Simon Willison.

In “[How I’m Using Coding Agents in September, 2025](<https://blog.fsck.com/2025/10/05/how-im-using-coding-agents-in-september-2025/>),” Jesse first describes how his [claude.md](<http://claude.md>) file provides a base prompt that “encodes a bunch of process documentation and rules that do a pretty good job keeping Claude on track.” And then his workflow calls on a bunch of specialized prompts he has created (i.e., “spells” that give clearer and more personalized meaning to specific magic words) like “brainstorm,” “plan,” “architect,” “implement,” “debug,” and so on. Note how inside these prompts, he may use additional magic words like DRY, YAGNI, and TDD, which refer to specific programming methodologies. For example, here’s his planning prompt (boldface mine):

> `Great. I need your help to write out a comprehensive implementation plan.`
> 
> `Assume that the engineer has zero context for our codebase and questionable`  
> `taste. document everything they need to know. which files to touch for each`  
> `task, code, testing, docs they might need to check. how to test it.give `  
> `them the whole plan as bite-sized tasks. **DRY. YAGNI. TDD.** **frequent commits**.`
> 
> `Assume they are a skilled developer, but know almost nothing about our`  
> `toolset or problem domain. assume they don't know good test design` `very`  
> `well.`
> 
> `please write out this plan, in full detail, into docs/plans/`

But Jesse didn’t stop there. He built a project called [Superpowers](<https://github.com/obra/superpowers>), which uses Claude’s [recently announced plug-in architecture](<https://docs.claude.com/en/docs/claude-code/plugins>) to “give Claude Code superpowers with a comprehensive skills library of proven techniques, patterns, and tools.” [Announcing the project](<https://blog.fsck.com/2025/10/09/superpowers/>), he wrote:

> Skills are what give your agents Superpowers. The first time they really popped up on my radar was a few weeks ago when Anthropic rolled out improved Office document creation. When the feature rolled out, I went poking around a bit – I asked Claude to tell me all about its new skills. And it [was only too happy to dish](<https://claude.ai/share/0fe5a9c0-4e5a-42a1-9df7-c5b7636dad92>)…. [Be sure to follow this link! – TOR]
> 
> One of the first skills I taught Superpowers was [How to create skills](<https://raw.githubusercontent.com/obra/superpowers-skills/35c29f0fe22881149a991eca1276c148567a7c29/skills/meta/writing-skills/SKILL.md>). That has meant that when I wanted to do something like add git worktree workflows to Superpowers, it was a matter of describing how I wanted the workflows to go…and then Claude put the pieces together and added a couple notes to the existing skills that needed to clue future-Claude into using worktrees.

After reading Jesse’s post, Simon Willison did a bit more digging into the original document handling skills that Claude had announced and that had sparked Jesse’s brainstorm. He noted:

> Skills are more than just prompts though: the repository also includes dozens of pre-written Python scripts for performing common operations.
> 
>  [pdf/scripts/fill_fillable_fields.py](<https://github.com/simonw/claude-skills/blob/initial/mnt/skills/public/pdf/scripts/fill_fillable_fields.py>) for example is a custom CLI tool that uses [pypdf](<https://pypi.org/project/pypdf/>) to find and then fill in a bunch of PDF form fields, specified as JSON, then render out the resulting combined PDF.
> 
> This is a really sophisticated set of tools for document manipulation, and I love that Anthropic have made those visible—presumably deliberately—to users of Claude who know how to ask for them.

You can see what’s happening here. Magic words are being enhanced and given a more rigorous definition, and new ones are being added to what, in fantasy tales, they call a “grimoire,” or book of spells. Microsoft calls such spells “[metacognitive recipes](<https://paradox921.medium.com/amplifier-notes-from-an-experiment-thats-starting-to-snowball-ef7df4ff8f97>),” a wonderful term that should get widely adopted, though in this article I’m going to stick with my fanciful analogy to magic.

At O’Reilly, we’re working with a very different set of magic words. For example, we’re building a system for precisely targeted competency-based learning, through which our customers can skip what they already know, master what they need, and prove what they’ve learned. It also gives corporate learning system managers the ability to assign learning goals and to measure the ROI on their investment.

It turns out that there are dozens of _learning frameworks_ (and that is itself a magic word). In the design of our own specialized learning framework, we’re invoking Bloom’s taxonomy, SFIA, and the Dreyfus Model of Skill Acquisition. But when a customer says, “We love your approach, but we use LTEM,” we can invoke that framework instead. Every corporate customer also has its own specialized tech stack. So we are exploring how to use magic words to let whatever we build adapt dynamically not only to our end users’ learning needs but to the tech stack and to the learning framework that already exists at each company.

That would be a nightmare if we had to support dozens of different learning frameworks using traditional processes. But the problem seems much more tractable if we are able to invoke the right magic words. That’s what I mean when I say that magic words are a crucial building block in the next generation of application programming.

## **The Architecture of Magic**

Here’s the important thing: Magic isn’t arbitrary. In every mythic tradition, it has structure, discipline, and cost. The magician’s power depends on knowing the right words, pronounced in the right way, with the right intent.

The same is true for AI systems. The effectiveness of our magic words depends on context, grounding, and feedback loops that give the model reliable information about the world.

That’s why I find the emerging ecosystem of AI applications so fascinating. It’s about providing the right context to the model. It’s about defining vocabularies, workflows, and roles that expose and make sense of the model’s abilities. It’s about turning implicit cultural knowledge into explicit systems of interaction.

We’re only at the beginning. But just as early programmers learned to build structured software without spelling out exact machine instructions, today’s AI practitioners are learning to build structured reasoning systems out of fuzzy language patterns.

Magic words aren’t just a poetic image. They’re the syntax of a new kind of computing. As people become more comfortable with LLMs, they will pass around the magic words they have learned as power user tricks. Meanwhile, developers will wrap more advanced capabilities around existing magic words and perhaps even teach the models new ones that haven’t yet had the time to accrete sufficient meaning through wide usage in the training set. Each application will be built around a shared vocabulary that encodes its domain knowledge. Back in 2022, Mike Loukides called these systems “[formal informal languages](<https://www.oreilly.com/radar/formal-informal-languages/>).” That is, they are spoken in human language, but do better when you apply a bit of rigor.

And at least for the foreseeable future, developers will write “shims” between the magic words that control the LLMs and the more traditional programming tools and techniques that interface with existing systems, much as Claire did with ChatPRD. But eventually we’ll see true AI to AI communication.

Magic words and the spells built around them are only the beginning. Once people start using them in common, they become _protocols_. They define how humans and AI systems cooperate, and how AI systems cooperate with each other.

We can already see this happening. Frameworks like LangChain or the Model Context Protocol (MCP) formalize how context and tools are shared. Teams build agentic workflows that depend on a common vocabulary of intent. What is an MCP server, after all, but a mapping of a fuzzy function call into a set of predictable tools and services available at a given endpoint?

In other words, what was once a set of magic spells is becoming infrastructure. When enough people use the same magic words, they stop being magic and start being standards—the building blocks for the next generation of software.

We can already see this progression with MCP. There are three distinct kinds of MCP servers. Some, like [Playwright MCP](<https://github.com/microsoft/playwright-mcp>), are designed to make it easier for AIs to interface with applications originally designed for interactive human use. Others, like the [GitHub MCP Server](<https://github.com/github/github-mcp-server>), are designed to make it easier for AIs to interface with existing APIs, that is, with interfaces originally designed to be called by traditional programs. But some are designed as a frontend for a true AI-to-AI conversation. Other protocols, like A2A, are already optimized for this third use case.

But in each case, an MCP server is really a dictionary (or in magic terms, a spellbook)  that explains the magic words that it understands and how to invoke them. As Jesse Vincent put it to me after reading a draft of this piece:

> The part that feels the most like magic spells is the part that most MCP authors do incredibly poorly. Each tool has a “description” field that tells the LLM how you use the tool. That description field is read and internalized by the LLM and changes how it behaves. Anthropic are particularly good at tool descriptions and most everybody else, in my experience, is…less good.

In many ways, publishing the prompts, tool descriptions, context, and skills that add functionality to LLMs may be a more important frontier of open source AI than open weights. It’s important that we treat our enhancements to magic words not as proprietary secrets but as shared cultural artifacts. The more open and participatory our vocabularies are, the more inclusive and creative the resulting ecosystem will be.

* * *

## Footnotes

  1. While often associated today with stage magic and cartoons, this magic word was apparently used from Roman times as a healing spell. One proposed etymology suggests that it comes [from the Aramaic for “I create as I speak.”](<https://en.wikipedia.org/wiki/Abracadabra>)
