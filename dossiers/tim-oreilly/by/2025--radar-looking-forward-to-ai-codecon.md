---
title: "Looking Forward to AI Codecon"
person: tim-oreilly
section: by
type: blog-post
year: 2025
date: 2025-09-03
venue: "O'Reilly Radar"
authors: "Tim O'Reilly"
source_url: https://www.oreilly.com/radar/looking-forward-to-ai-codecon/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the oreilly.com/radar WordPress REST API (people_taxonomy=tim-oreilly); HTML converted to markdown."
---

# Looking Forward to AI Codecon

## Full text

I’m really looking forward to our second O’Reilly AI Codecon, [Coding for the Agentic World](<https://www.oreilly.com/AgenticWorld/>), which is happening on September 9, online from 8am to noon Pacific time, with a follow-on [day of additional demos](<https://learning.oreilly.com/live-events/oreilly-demo-day/0642572227968/>) on September 16. But I’m also looking forward to how the AI market itself unfolds: the surprising twists and turns ahead as users and developers apply AI to real-world problems.

The pages linked above give details on the program for the events. What I want to give here is a bit of the **_why_** behind the program, with a bit more detail on some of the fireside chats I will be leading.

## From Invention to Application

There has been so much focus in the past on the big AI labs, the model developers, and their razzle-dazzle about AGI, or even ASI. That narrative implied that we were heading toward something unprecedented. But if this is a “[normal technology](<https://www.oreilly.com/radar/is-ai-a-normal-technology/>)” (albeit one as transformational as electricity, the internal combustion engine, or the internet), we know that LLMs themselves are just the beginning of a long process of discovery, product invention, business adoption, and societal adaptation.

That process of collaborative discovery of the real uses for AI and reinvention of the businesses that use it is happening most clearly in the software industry. It is where AI is being pushed to the limits, where new products beyond the chatbot are being introduced, where new workflows are being developed, and where we understand what works and what doesn’t.

This work is often being pushed forward by individuals, who are “[learning by doing](<https://yalebooks.yale.edu/book/9780300195668/learning-by-doing/>).” Some of these individuals work for large companies, others for startups, others for enterprises, and others as independent hackers.

Our focus in these AI Codecon events is to smooth adoption of AI by helping our customers cut through the hype and understand what is working. O’Reilly’s mission has always been [changing the world by sharing the knowledge of innovators](<https://www.oreilly.com/about/>). In our events, we always look for people who are at the forefront of invention. As outlined in the call to action for the first event, I was concerned about the chatter that AI would make developers obsolete. I [argued instead](<https://www.oreilly.com/radar/the-end-of-programming-as-we-know-it/>) that it would profoundly change the process of software development and the jobs that developers do, but that it would make them more important than ever.

It looks like I was right. There is a huge ferment, with so much new to learn and do that it’s a really exciting time to be a software developer. I’m really excited about the practicality of the conversation. We’re not just talking about the “what if.” We’re seeing new AI powered services meeting real business needs. We are witnessing the shift from human-centric workflows to agent-centric workflows, and it’s happening faster than you think.

We’re also seeing widespread adoption of the protocols that will power it all. If you’ve followed my work from open source to Web 2.0 to the present, you know that I believe strongly that the most dynamic systems have “an architecture of participation.” That is, they aren’t monolithic. The barriers to entry need to be low and business models fluid (at least in the early stages) for innovation to flourish.

When AI was framed as a race for superintelligence, there was a strong expectation that it would be winner takes all. The first company to get to ASI (or even just to AGI) would soon be so far ahead that it would inevitably become a dominant monopoly. Developers would all use its APIs, making it into the single dominant platform for AI development.

Protocols like MCP and A2A are instead enabling a decentralized AI future. The explosion of entrepreneurial activity around agentic AI reminds me of the best kind of open innovation, much like I saw in the early days of the personal computer and the internet.

I was going to use my opening remarks to sound that theme, and then I read Alex Komoroske’s marvelous essay, “[Why Centralized AI Is Not Our Inevitable Future](<https://www.techdirt.com/2025/06/16/why-centralized-ai-is-not-our-inevitable-future/>).” So I asked him to do it instead. He’s going to give an updated, developer-focused version of that as our kickoff talk.

Then we’re going into a section on agentic interfaces. We’ve lived for decades with the GUI (either on computers or mobile applications) and the web as the dominant ways we use computers. AI is changing all that.

It’s not just agentic interfaces, though. It’s really developing true AI-native products, searching out the possibilities of this new computing fabric.

## The Great Interface Rethink

In the “normal technology” framing, a fundamental technology innovation is distinct from products based on it. Think of the invention of the LLM itself as electricity, and ChatGPT as the equivalent of Edison’s incandescent light bulb and the development of the distribution network to power it.

There’s a bit of a lesson in the fact that the telegraph was the first large-scale practical application of electricity, over 40 years before Edison’s lightbulb. The telephone was another killer app that used electricity to power it. But despite their scale, these were specialized devices. It was the infrastructure for incandescent lighting that turned electricity into a [general-purpose technology](<https://en.wikipedia.org/wiki/General-purpose_technology>).

The world soon saw electrical resistance products like irons and toasters, and electric motors powering not just factories but household appliances such as washing machines and eventually refrigerators and air conditioning. Many of these household products were plugged into light sockets, since the pronged plug as we know it today wasn’t introduced until 30 years after the first light bulb.

_[Found on Facebook](<https://www.facebook.com/photo/?fbid=10158281345021884&set=gm.3012577095721332>): “Any ideas what this would have been used for? I found it after pulling up carpet – it’s in the corner of a closet in my 1920s ‘fixer-upper’ that I’m slowly bringing back to life. It appears to be for a light bulb and the little flip top is just like floor outlets you see today, but can’t figure out why it would be directly on the floor.”_

The lesson is that **_at some point in the development of a general purpose technology, product innovation takes over from pure technology innovation_**. That’s the phase we’re entering now.

Look at the evolution of LLM-based products: GitHub Copilot embedded AI into Visual Studio Code; the interface was an extension to VS Code, a 10-year-old GUI-based program. Google’s AI efforts were tied into its web-based search products. ChatGPT broke the mold and introduced the first radically new interface since the web browser. Suddenly, chat was the preferred new interface for everything. But Claude took things further with Artifacts and then Claude Code, and once coding assistants gained more complex interfaces, that kicked off today’s fierce competition between coding tools. The next revolution is the construction of a new computing paradigm where software is composed of intelligent, autonomous agents.

I’m really looking forward to Rachel-Lee Nabors’s talk on how, with an agentic interface, we might transcend the traditional browser: AI agents can adapt content directly to users, offering privacy, accessibility, and flexibility that legacy web interfaces cannot match.

But it seems to me that there will be two kinds of agents, which I call “demand side” and “supply side” agents. What’s a “demand side” agent? Instead of navigating complex apps, you’ll simply state your goal. The agent will understand the context, access the necessary tools, and present you with the result. The vision is still science fiction. The reality is often a kludge powered by browser use or API calls, with MCP servers increasingly offering an AI-friendlier interface for those demand-side agents to interact with. But why should it stop there? MCP servers are static interfaces. What if there were agents on both sides of the conversation, in a dynamic negotiation? I suspect that while demand-side agents will be developed by venture funded startups, most server-side agents will be developed by enterprises as a kind of conversational interface for both humans and AI agents that want access to their complex workflows, data, and business models. And those enterprises will often be using agentic platforms tailored for their use. That’s part of the “supply side agent” vision of companies like Sierra. I’ll be talking with Sierra cofounder Clay Bavor about this next step in agentic development.

We’ve grown accustomed to thinking about agents as lonely consumers—“tell me the weather,” “scan my code,” “summarize my inbox.” But that’s only half the story. If we build supply-side agent infrastructure—autonomous, discoverable, governed, negotiated—we unlock agility, resilience, security, and collaboration.

My interest in product innovation, not just advances in the underlying technology, is also why I’m excited about my fireside chat with Josh Woodward, who co-led the team that developed NotebookLM at Google. I’m a huge fan of NotebookLM, which in many ways brought the power of RAG (retrieval-augmented generation) to end users, allowing them to collect a set of documents into a Google drive, and then use that collection to drive chat, audio overviews of documents, study guides, mind maps, and much more.

NotebookLM is also a lovely way to build on the deep collaborative infrastructure provided by Google Drive. We need to think more deeply about collaborative interfaces for AI. Right now, AI interaction is mostly a solitary sport. You can share the outputs with others, but not the generative process. I wrote about this recently in “[People Work in Teams, AI Assistants in Silos](<https://www.oreilly.com/radar/people-work-in-teams-ai-assistants-in-silos/>).” I think that’s a big miss, and I’m hoping to probe Josh about Google’s plans in this area, and eager to see other innovations in AI-mediated human collaboration.

GitHub is another existing tool for collaboration that has become central to the AI ecosystem. I’m really looking forward to talking with outgoing CEO Thomas Dohmke both about the ways that GitHub already provides a kind of exoskeleton for collaboration when using AI code-generation tools. It seems to me that one of the frontiers of AI-human interfaces will be those that enable not just small teams but eventually large groups to collaborate. I suspect that GitHub may have more to teach us about that future than we now suspect.

And finally, we are now learning that managing context is a critical part of designing effective AI applications. My cochair Addy Osmani will be talking about the emergence of context engineering as a real discipline, and its relevance to agentic AI development.

## Tool-Chaining Agents and Real Workflows

Today’s AI tools are largely solo performers—a Copilot suggesting code or a ChatGPT answering a query. The next leap is from single agents to interconnected systems. The program is filled with sessions on “tool-to-tool workflows” and multi-agent systems.

Ken Kousen will showcase the new generation of coding agents, including Claude Code, Codex CLI, Gemini CLI, and Junie, that help developers navigate codebases, automate tasks, and even refactor intelligently. In her talk, Angie Jones takes it further: agents that go beyond code generation to manage PRs, write tests, and update documentation—stepping “out of the IDE” and into real-world workflows.

Even more exciting is the idea of agents collaborating with each other. The Demo Day will showcase a multi-agent coding system where agents share, correct, and evolve code together. This isn’t science fiction; Amit Rustagi’s talk on decentralized AI agent infrastructure using technologies like WebAssembly and IPFS provides a practical architectural framework for making these agent swarms a reality.

## The Crucial Ingredient: Common Protocols

How do all these agents talk to each other? How do they discover new tools and use them safely? The answer that echoes throughout the agenda is the Model Context Protocol (MCP).

Much as the distribution network for electricity was the enabler for all of the product innovation of the electrical revolution, MCP is the foundational plumbing, the universal language that will allow this new ecosystem to flourish. Multiple sessions and an entire Demo Day are dedicated to it. We’ll see how Google is using it for agent-to-agent communication, how it can be used to control complex software like Blender with natural language, and even how it can power novel SaaS product demos.

The heavy focus on a standardized protocol signals that the industry is maturing past cool demos and is now building the robust, interoperable infrastructure needed for a true agentic economy.

If the development of the internet is any guide, though, MCP is a beginning, not the end. TCP/IP became the foundation of a layered protocol stack. It is likely that MCP will be followed by many more specialized protocols.

## Why This Matters

Theme| **Why It’s Thrilling**  
---|---  
Autonomous, Distributed AI| Agents that chain tasks and operate behind the scenes can unlock entirely new ways of building software.  
Human Empowerment & Privacy| The push against centralized AI systems is a reminder that tools should serve users, not control them.  
Context as Architecture| Elevating input design to first-class engineering—this will greatly improve reliability, trust, and AI behavior over time.  
New Developer Roles| We’re seeing developers transition from writing code to orchestrating agents, designing workflows, and managing systems.  
MCP & Network Effects| The idea of an “AI-native web,” where agents use standardized protocols to talk, is powerful, open-ended, and full of opportunity.  
  
I look forward to seeing you there!

* * *

_We hope you’ll join us at**AI Codecon: Coding for the Agentic World** on September 9 to explore the tools, workflows, and architectures defining the next era of programming. It’s free to attend. _[ _Register now to save your seat_](<https://www.oreilly.com/AgenticWorld/>) _._ _And join us for[O’Reilly Demo Day](<https://learning.oreilly.com/live-events/oreilly-demo-day/0642572227968/>) on September 16 to see how experts are shaping AI systems to work for them via MCP._
