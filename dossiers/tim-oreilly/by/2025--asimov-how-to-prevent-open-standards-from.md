---
title: "How to Prevent Open Standards from Getting Captured Again"
person: tim-oreilly
section: by
type: blog-post
year: 2025
date: 2025-12-23
venue: "Asimov’s Addendum"
authors: "Sruly Rosenblat, Ilan Strauss, Tim O'Reilly"
source_url: https://asimovaddendum.substack.com/p/how-to-prevent-open-standards-from
retrieved: 2026-08-13
content: full-text
notes: "Subtitle: “The bundling problem and the thin line between product and protocol”. Asimov’s Addendum, the Substack of Tim O’Reilly and Ilan Strauss on AI commercialization risks and governance; published CC BY 4.0. Retrieved from the free public post page."
---

# How to Prevent Open Standards from Getting Captured Again

## Full text

> Even with open governance, one company’s implementation could become the default simply because it ships fastest or gains the most usage. Zemlin says that’s not necessarily a bad thing, though. He points to open source history — like Kubernetes “winning” the container race — as evidence that “dominance emerges from merit and not vendor control”.
> 
> — Rebecca Bellan, _[TechCrunch](<https://techcrunch.com/2025/12/09/openai-anthropic-and-block-join-new-linux-foundation-effort-to-standardize-the-ai-agent-era/>)_.

On December 9, 2025 Anthropic announced that it was donating the Model Context Protocol (MCP) to a newly established Agentic AI Foundation (AAIF) at the Linux Foundation, which would also be gifted OpenAI’s [Agent.md protocol](<http://agent.md>) and Block’s [Goose](<https://block.github.io/goose/>) agent. The stated [goal](<https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation>) was: to drive “innovation across the agentic AI ecosystem and ensure these foundational technologies remain neutral, open, and community-driven”.

For context, MCP is an open standard that decouples applications from tools by creating a universal adapter. It allows models to interact with external systems through standardized, auditable interfaces rather than tightly coupled, bespoke integrations. It works by separating out “servers” and “clients” and allowing any client (i.e. AI agent) to connect to any “server” (i.e. collection of tools for the agent to use).

Back to the Linux Foundation as the new home for the open MCP standard: they will receive support from big names such as Anthropic, Block, OpenAI, Google, Microsoft, AWS, CloudFlare and Bloomberg who will sit as founding [“Platinum” members](<https://aaif.io/members/#join>) on the AAIF by virtue of paying the $350,000 contribution – though this membership is now no longer available. But the real question is not about funding: it’s whether the open protocol, through private use and adoption, gets superseded by a closed private ecosystem.

## **Android’s “Open” Ecosystem**

History is instructive as to what can go wrong when public digital standards get incorporated into commercial systems. The entire Android1 ecosystem is built on an open source foundation ([AOSP](<https://source.android.com/>)), yet much of this ecosystem is also sending valuable user data directly to Google from first activation. An open platform – like AOSP – does not by itself guarantee that the dominant products built on that platform remain open.

Despite Android being open source, most users think of it as a Google-owned platform. Google apps like Youtube, Google Maps and the Google Play Store are all preinstalled, the default search engine is always Google and the default browser is always Chrome. Android is _treated_ as if it were Google. This is by design.   
  
In order to gain access to any of Google’s apps (such as Google Maps, YouTube, and Google Play), manufacturers had to sign a Mobile Application Distribution Agreement (MADA) and agree to preinstall all of Google’s apps, as well as setting some of Google’s services as defaults.

This is more limiting than it seems at first glance because many Android apps have come to [rely on](<https://www.androidpolice.com/google-ecosystem-lock-in-getting-stronger/>) Google Play Services and Google maps data to implement their own features. Meaning that despite Android being an open platform, the basic infrastructure required for countless mobile apps was tied to a very specific version of Android that Google controls. Google Play Services and by extension all of Google’s apps are nearly a requirement in the Android mobile space.2 Competitors would [need](<https://www.benedelman.org/news-021314/>) to build all that infrastructure from scratch to ditch any part of Google’s bundled services, or even just to change the layout of the user’s home screen.  
  
The EU ruled that much of this was illegal in 2018 and fined Google €4.34 billion. The case is under final appeal with the Court of Justice, the bloc’s highest court. [In the meantime](<https://www.hausfeld.com/what-we-think/perspectives-blogs/landmark-eu-general-court-google-android-decision-signals-tougher-antitrust-enforcement>), European Android users now get a choice screen for browsers and search apps; Manufacturers can pre-install rival apps without losing Play Store access; and Google started charging device makers for app pre-installation (previously used bundling instead).

[Share](<https://asimovaddendum.substack.com/p/how-to-prevent-open-standards-from?utm_source=substack&utm_medium=email&utm_content=share&action=share>)

  
In this instance, _**leverage over the Android open standard comes not from Google dictating the standard itself but from Google owning the complementary applications and associated developer environment.**_

## **Pseudo-MCP Products**

Just like Android can simultaneously be a vibrant open source project and also nearly completely dominated by one company, the same could happen to any project or protocol. Previously, we explored how, in practice, MCP servers are highly reliant on [just a few services](<https://towardsdatascience.com/mcp-in-practice/>). _**However, MCP clients, such as Claude desktop or the ChatGPT application, could also have a defining say on the standard**_.

A few days prior to Anthropic donating MCP, Anthropic released new updates to help make MCP more efficient. **But these updates were not made at the** _**protocol level**_**, they were made at the** _**product level**._ Anthropic added features like tool use examples and tool search to their SDK, theoretically allowing their MCP client to work better than others. Even though this is probably _not_ Anthropic’s intention in this instance (given the proximity to them donating MCP and the fact that these features are still in beta), it does highlight that just because the performance of MCP is largely platform agnostic right now, it doesn’t imply it will stay that way.

Subscribe

The Apps SDK – OpenAI’s attempt at integrating other applications into their chat app – is another example of how clients might diverge from each other in the future. Despite the Apps SDK being completely compatible with MCP on the server level it also introduced new features and requirements to the client side that were not well documented and were not intended to be implemented on other platforms. Since then, to their credit, researchers from OpenAI, Anthropic and the open source project MCP-UI proposed an [MCP apps extension](<https://blog.modelcontextprotocol.io/posts/2025-11-21-mcp-apps/>) to MCP that will integrate user interface results into the official MCP spec.

So far there is a good track record of these innovations being shared but that is not guaranteed. If innovation moves from the protocols level to the product level then many of the benefits that come along with a platform agnostic system may be lost.

## **All in one agents: agent-model-tools-cloud**

MCP might also lose steam because its modular architecture gets beaten out by a proprietary, integrated / bundled all-in-one offering. _**In this scenario, which infrastructure hosts the code becomes more fundamental than the protocol itself**_. Here the model provider (such as OpenAI or Anthropic) effectively captures the MCP space by moving “the client” (the code that interacts with tools) from the developer’s laptop to their own computing servers – and then push their own products by promising better latency and easier integration for their own tools.

We note below that if everything runs in OpenAI’s cloud then their first-party tools (web search, file search) execute faster with much less latency; while third-party MCP tools require a round trip: “OpenAI server → your MCP server → back to OpenAI”. This speed difference means developers might be incentivized to gravitate toward first-party tools.

Originally, developers controlled the agent on their own machines. They would call OpenAI’s API for the model, get responses back, decide which tools to use locally, and send results back. This was portable: meaning you could swap model providers without changing much in your code.

Subscribe

Now with OpenAI’s “responses API” and Google’s “Interactions API”, the entire AI agent runs on the _provider’s_ servers. _**So you are not just calling a model anymore – you’re using OpenAI’s or Google’s entire hosted agent infrastructure**_. We explain how this works in more detail below.

[](<https://substackcdn.com/image/fetch/$s_!339p!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F770ae4ae-397e-4457-8a1d-9967162f8bf8_1536x1024.png>)_Source: OpenAI ChatGPT 5.2 (created December 18, 2025)._

#### **A new set of APIs**

OpenAI released the responses API in March 2025 that moved the processing loop – the process of calling tools and feeding it back to the model – entirely to their own servers. Previously when using OpenAI’s and most of its competitors’ API products, all management of agents was done on the developer’s own machine, while all model processing was done on OpenAI’s servers. This worked great for the initial round of chat applications, as usually after an AI chat message the user would need to respond, so it only made sense to send the data back and forth. However, with the rise of agents, this back and forth – model → local tools → model → local tools → model → user – started taking up valuable time and internet bandwidth by requiring the entire context to be sent back and forth for every single tool call.3

With the responses API, Agents are now an extension of the model. The responses API launched alongside tools like web search, file search and computer use. Only computer use requires any actions to be executed on the developer’s own machine. The rest of the actions take place purely on OpenAI’s own servers. With the responses API, context is not being sent to a model; it’s instead being sent to an agent – one managed completely by OpenAI. Shortly after launch, OpenAI also began supporting remote third-party MCP calls directly from OpenAI’s responses API. With this, OpenAI’s response endpoint became an MCP client that executes on OpenAI’s server. But not all tools it uses are necessarily created equal, first party tools like web search, code execution and file search may still be privileged by faster response times due to closer or shared servers.

For a long time OpenAI was the only major model provider that managed tool calls and state server side (i.e. on its side); but Google recently joined them by launching the “Interactions API” an [API](<https://x.com/OfficialLoganK/status/1999163356784263489>) that similarly blurs the line between agent and model, with state being stored and tools (including first party tools and third part MCP servers) being called server side. Anthropic too now supports tools like code execution, MCP calls and context management without using the developer’s machine.  

### **Vertical Integration and Open Standards**

**The consequences** of the above bundled approach are potentially far reaching. By vertically integrating tools with models and agents, providers like OpenAI, Google and Anthropic could essentially lock a developer into one platform. _**Switching a model provider no longer means switching a model, it means switching to an entirely new (often poorly documented) agent library and tool ecosystem**_.

In certain respects this mirrors the Android playbook: technically open, but the bundled services become impossible to avoid because they perform better and integrate tighter. _**The bigger and more vertically integrated a platform is, the less it benefits from openness and interoperability and the more it benefits from its own goods and services being used to the exclusion of others**_.

But there is an answer built into the MCP protocol itself, in that MCP doesn’t require remote servers to run. MCP servers could theoretically be spun up anywhere including on a model providers’ own servers — bringing the latency for third-party tools to levels similar to first party ones. Despite the fact that every current iteration of an ‘agent in the cloud’ by major model providers supports only remote MCP servers, _**there is another way — local MCP servers. Developers should be able to host their own MCP tools on the cloud alongside the running agent using similar infrastructure to what the major players already built for agent code execution**_.

## **To Protect Standards Protect Developer Ecosystems**

Safeguarding MCP’s flexibility requires looking beyond the protocol itself to the ecosystem it inhabits.

The Linux Foundation donation is a positive step that could allow MCP to evolve in ways that benefit the broader AI developer community, not just major labs. Foundation stewardship can offer protection against narrow commercial interests and, in theory, can provide a neutral forum for making decisions about MCP’s future direction.

_But ownership often matters less than adoption_. As a developer tool, MCP’s utility will ultimately decide its role in the rapidly changing AI markets. No amount of foundation oversight can force adoption if the protocol does not continue to solve real problems for builders in as an efficient manner as possible.

Standards live or die by use. **Large companies can only capture MCP and AI standards to the extent that they can capture the developer ecosystem itself**. _**Control the builders, and you control the standard**_.

This points to a two-fold task: first, support MCP’s independent and open development under the Linux Foundation. Second – and equally critical – foster the independence of the developer ecosystem so that open standards can continue to thrive in AI application markets.

The second task may prove harder than the first. As Android, OpenAI’s “responses API,” and Google’s “Interactions API” show, _**large platforms don’t need to control the standard directly if they can create vertical integration and dependencies elsewhere in the market**_. Keeping MCP open means preventing those chokepoints from forming – whether in hosting infrastructure, model access, or the application layer itself. Developer independence requires active protection at every important market touch point, not just good governance of the protocol itself.  

* * *

To receive new posts and support our work, consider becoming a free or paid subscriber.

Subscribe

1

Android is a mobile operating system that Google purchased in 2005. It is open source but Google builds their own version on top of it and contributes back to the open source version. Today about 72% of smartphones globally run Android.

2

There are some notable Android devices in different form factors that don’t rely on Google services such as Amazon’s kindle and Meta’s VR lineups. Amazon also attempted to make an Android phone without Google services but the product largely failed to sell.

3

While it is still usually slower to run tools locally, in certain cases it is still preferred. For example, Andrej Karpathy [notes](<https://karpathy.bearblog.dev/year-in-review-2025/>) that Claude Code may have gained momentum precisely because “it runs on your computer and with your private environment, data, and context.” In this case, running code locally allows not just the context, but the execution environment itself, to be tailored to your project.
