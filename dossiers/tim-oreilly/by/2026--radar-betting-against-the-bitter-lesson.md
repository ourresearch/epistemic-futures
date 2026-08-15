---
title: "How We Bet Against the Bitter Lesson"
person: tim-oreilly
section: by
type: blog-post
year: 2026
date: 2026-03-02
venue: "O'Reilly Radar"
authors: "Tim O'Reilly"
source_url: https://www.oreilly.com/radar/betting-against-the-bitter-lesson/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the oreilly.com/radar WordPress REST API (people_taxonomy=tim-oreilly); HTML converted to markdown."
---

# How We Bet Against the Bitter Lesson

## Full text

I’ve been telling myself and anyone who will listen that [Agent Skills](<https://agentskills.io/>) point toward a new kind of future AI + human knowledge economy. It’s not just Skills, of course. It’s also things like Jesse Vincent’s [Superpowers](<https://github.com/obra/superpowers>) and Anthropic’s recently introduced [Plugins for Claude Cowork](<https://github.com/anthropics/knowledge-work-plugins>). If you haven’t encountered these yet, keep reading. It should become clear as we go along.

It feels a bit like I’m assembling a picture puzzle where all the pieces aren’t yet on the table. I am starting to see a pattern, but I’m not sure it’s right, and I need help finding the missing pieces. Let me explain some of the shapes I have in hand and the pattern they are starting to show me, and then I want to ask for your help filling in the gaps.

## Programming two different types of computer at the same time

Phillip Carter wrote a piece a while back called “[LLMs Are Weird Computers](<https://www.phillipcarter.dev/posts/llms-computers>)” that landed hard in my mind and wouldn’t leave. He noted that we’re now working with two fundamentally different kinds of computer at the same time. One can write a sonnet but struggles to do math. The other does math easily but couldn’t write a sonnet to save its metaphorical life.

Agent Skills may be the start of an answer to the question of what the interface layer between these two kinds of computation looks like. A Skill is a package of context (Markdown instructions, domain knowledge, and examples) combined with tool calls (deterministic code that does the things LLMs are bad at). The context speaks the language of the probabilistic machine, while the tools speak the language of the deterministic one.

Imagine you’re an experienced DevOps engineer and you want to give an AI agent the ability to diagnose production incidents the way you would. The context part of that Skill includes your architecture overview, your runbook for common failure modes, the heuristics you’ve developed over the years, and annotated examples of past incidents. That’s the part that speaks to the probabilistic machine. The tool part includes actual code that queries your monitoring systems, pulls log entries, checks service health endpoints, and runs diagnostic scripts. Each tool call saves the model from burning tokens on work that deterministic code does better, faster, and more reliably.

The Skill is neither the context nor the tools. It’s the combination. Expert judgment about when to check the database connection pool married to the ability to actually check it. We’ve had runbooks before (context without tools). We’ve had monitoring scripts before (tools without context). What we haven’t had is a way to package them together for a machine that can read the runbook _and_ execute the scripts, using judgment to decide which script to run next based on what the last one returned.

This pattern shows up across every knowledge domain. A financial analyst’s Skill might combine valuation methodology with tools that pull real-time market data and run DCF calculations. A legal Skill might pair a firm’s approach to contract review with tools that extract and compare specific clauses across documents. In each case, the valuable thing isn’t the knowledge alone or the tools alone. It’s the integration of expert workflow logic that orchestrates when and how to use each tool, informed by domain knowledge that gives the LLM the judgment to make good decisions in context.

## Software that saves tokens

In “[Software Survival 3.0](<https://steve-yegge.medium.com/software-survival-3-0-97a2a6255f7b>),” Steve Yegge asked what kinds of software artifacts survive in a world where AI can generate disposable software on the fly? His answer: software that saves tokens. Binary tools with proven solutions to common problems make sense when reuse is nearly free and regenerating them is token-costly.

Skills fit this niche. A well-crafted Skill gives an LLM the context it needs (which costs tokens) but also gives it tools that _save_ tokens by providing deterministic, reliable results. The developer’s job increasingly becomes making good calls about this distinction: What should be context (flexible, expressive, probabilistic) and what should be a tool (efficient, deterministic, reusable)?

An LLM’s context window is a finite and expensive resource. Everything in it costs tokens, and everything in it competes for the model’s attention. A Skill that dumps an entire company knowledge base into the context window is a poorly designed Skill. A well-designed one is selective: It gives the model exactly the context it needs to make good decisions about which tools to call and when. This is a form of engineering discipline that doesn’t have a great analogue in traditional software development. It’s closer to what an experienced teacher does when deciding what to tell a student before sending them off to solve a problem—what Matt Beane, author of [_The Skill Code_](<https://www.harpercollins.com/products/the-skill-code-matt-beane>), calls “scaffolding,” sharing not everything you know but the right things at the right level of detail to enable good judgment in the moment.

## AI is a social and cultural technology

This notion of saving tokens is a bridge to the work of Henry Farrell, Alison Gopnik, Cosma Shalizi, and James Evans. They make the case that large models should not be viewed primarily as intelligent agents, but as [a new kind of cultural and social technology](<https://henryfarrell.net/wp-content/uploads/2025/03/Science-Accepted-Version.pdf>), allowing humans to take advantage of information other humans have accumulated. Yegge’s observation fits right into this framework. Every new social and cultural technology tends to survive because it saves cognition. We learn from each other so we don’t have to discover everything for the first time. Alfred Korzybski referred to language, the first of these human social and cultural technologies, and all of those that followed, as “[time-binding](<https://www.google.com/search?q=Alfred+Korzybski+time+binding>).” (I will add that each advance in time binding creates consternation. Consider Socrates, whose diatribes against writing as the enemy of memory were passed down to us by Plato using that very same advance in time binding that Socrates decried.)

I am not convinced that the idea that AI may one day become an independent intelligence is misguided. But at present, AI is a symbiosis of human and machine intelligence, the latest chapter of a long story in which advances in the speed, persistence, and reach of communications [weaves humanity into a global brain](<https://www.youtube.com/watch?v=u62fQCI7YNA>). I have a set of priors that say (until I am convinced otherwise) that _AI will be an extension of the human knowledge economy, not a replacement for it_. After all, as Claude told me when I asked whether [it was a worker or a tool](<https://www.oreilly.com/radar/jensen-huang-gets-it-wrong/>), “I don’t initiate. I’ve never woken up wanting to write a poem or solve a problem. My activity is entirely reactive – I exist in response to prompts. Even when given enormous latitude (‘figure out the best approach’), the fact that I should figure something out comes from outside me.”

The shift from a chatbot responding to individual prompts to agents running in a loop marks a big step in the progress towards more autonomous AI, but even then, some human established the goal that set the agent in motion. I say this even as I am aware that long-running loops become increasingly difficult to distinguish from volition and that much human behavior is also set in motion by others. But I have yet to see any convincing evidence of Artificial Volition. And for that reason, _we need to think about mechanisms and incentives for humans to continue to create and share new knowledge_ , putting AIs to work on questions that they will not ask on their own.

On X, someone recently asked Boris Cherny how come there are a hundred-plus open engineering positions at Anthropic if Claude is writing 100% of the code. [His reply](<https://x.com/bcherny/status/2022762422302576970>) was made that same point: “Someone has to prompt the Claudes, talk to customers, coordinate with other teams, decide what to build next. Engineering is changing and great engineers are more important than ever.”

> _On March 26, join Addy Osmani and Tim O’Reilly at AI Codecon: Software Craftsmanship in the Age of AI, where an all-star lineup of experts will go deeper into orchestration, agent coordination, and the new skills developers need to build excellent software that creates value for all participants.  _[_Sign up for free here_](<https://www.oreilly.com/AI-Codecon/>) _._

## Tacit knowledge made executable

A huge amount of specialized, often tacit, knowledge is embedded in workflows. The way an experienced developer debugs a production issue. The way a financial analyst stress-tests a model. This knowledge has historically been very hard to transfer. You learned it by apprenticeship, by doing, by being around people who knew how.

Matt Beane, author of [_The Skill Code_](<https://www.harpercollins.com/products/the-skill-code-matt-beane>), calls apprenticeship “the 160,000 year old school hidden in plain sight.” He finds that effective skill development follows a common pattern of three C’s: challenge, complexity, and connection. The expert structures challenges at the right level, exposes the novice to the full complexity of the bigger picture rather than shielding them from it, and builds a connection that makes the novice willing to struggle and the expert willing to invest.

Designing a good Skill requires a similar craft. You have to figure out what an expert actually _does_. What are the decision points, the heuristics, the things they notice that a novice wouldn’t? And then how do you encode that into a form a machine can act on? Most Skills today are closer to the manual than to the master. Figuring out how to make Skills that transmit not just knowledge but judgment is one of the most interesting design challenges in this space.

But Matt also flags a paradox: the better we get at encoding expert judgment into Skills, the less we may need novices working alongside experts, and that’s exactly the relationship that produces the next generation of experts. If we’re not careful, we’ll capture today’s tacit knowledge while quietly shutting down the system that generates tomorrow’s.

Jesse Vincent’s Superpowers complement this picture. If a Skill is like handing a colleague a detailed playbook for a particular job, a Superpower is more like the professional habits and instincts that make someone effective at everything they do. Superpowers are meta-skills. They don’t tell the agent what to do. They shape how it thinks about what to do. As Jesse put it to me the other day, Superpowers tried to capture everything he’d learned in 30 years as a software developer.

As workflows change to include AI agents, Skills and Superpowers become a mechanism for sharing tacit professional knowledge and judgment with those agents. That makes Skills potentially very valuable but also raises questions about who controls them and who benefits.

Matt pointed out to me that many professions will resist the conversion of their expertise into Skills. He noted: “There’s a giant showdown between the surgical profession and Intuitive Surgical on this right now — Intuitive Surgical with its da Vinci 5 surgical robot will only let you buy or lease it if you sign away the rights to your telemetry as a surgeon. Lower status surgeons take the deal. Top tier institutions are fighting.”

It seems to me that the repeated narrative of the AI labs that they are creating AI that will make humans redundant rather than empowering them will only increase resistance to knowledge sharing. I believe they should instead recognize the opportunity that lies in [making a new kind of market for human expertise](<https://www.oreilly.com/radar/ai-and-the-next-economy/>).

## **Protection, discovery, and the missing plumbing**

Skills are just Markdown instructions and context. You could encrypt them at rest and in transit, but at execution time, the secret sauce is necessarily plaintext in the context window. The solution might be what MCP already partially enables: splitting a Skill into a public interface and a server-side execution layer where the proprietary knowledge lives. The tacit knowledge stays on your server while the agent only sees the interface.

But part of the beauty of Skills right now is the fact that they really are just a folder that you can move around and modify. This is like the marvelous days of the early web when you could imitate someone’s new HTML functionality simply by clicking “View Source.” This was a recipe for rapid, leapfrogging innovation. It may be far better to establish norms for attribution, payment, and reuse than to put up artificial barriers. There are useful lessons from open source software licenses and from voluntary payment mechanisms like those used by Substack. But the details matter, and I don’t think anyone has fully worked them out yet.

Meanwhile, the discovery problem will grow larger. Vercel’s [Skills marketplace](<https://skills.sh/>) already has more than 60,000 Skills. How well will skill search work when there are millions? How do agents learn which Skills are available, which are best, and what they cost? The evaluation problem is different from web search in a crucial way: testing whether a Skill is _good_ requires actually running it, which is expensive and nondeterministic. You can’t just crawl and index. I don’t imagine a testing regime so much as some feedback mechanism by which the effectiveness of particular Skills is learned and passed on by agents over time. There may be some future equivalent to Pagerank and the other kinds of signals that have made Google search so effective, one that is generated by feedback collected over time by agents as skills are tried, revised, and tried again over time.

I’m watching several projects tackling pieces of this: [MCP Server Cards](<https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2127>),[ AI Cards](<https://github.com/Agent-Card/ai-card>), Google’s [A2A protocol](<https://a2aprotocol.ai/>), and payment protocols from[ Google](<https://developers.google.com/merchant/ucp>) and[ Stripe](<https://stripe.com/blog/developing-an-open-standard-for-agentic-commerce>). These are all a good start, but I suspect so much more has yet to be created. For a historical comparison, you might say that all this is at the [CGI](<https://en.wikipedia.org/wiki/Common_Gateway_Interface>) stage in the development of dynamic websites.

## **What happens after the bitter lesson?**

Richard Sutton’s “[Bitter Lesson](<http://www.incompleteideas.net/IncIdeas/BitterLesson.html>)” is the fly in the ointment. His argument is that in the history of AI, general methods leveraging computation have always ended up beating approaches that try to encode human knowledge. Chess engines that encoded grandmaster heuristics lost to brute-force engines. NLP systems built on carefully constructed grammars lost to statistical models trained on more data. AlphaGo beat Lee Sedol after training on human games, but then fell in turn to AlphaZero, which learned Go on its own.

I had my own painful experience of the pre-AI bitter lesson when O’Reilly launched [GNN, the first web portal](<https://en.wikipedia.org/wiki/Global_Network_Navigator>). We curated the list of the best websites. Yahoo! decided to catalog them all, but even they were outrun by Google’s algorithmic curation, which produced a unique catalog of the best sites for any given query, ultimately billions of times a day.

Steve Yegge put it bluntly to me: “Skills are a bet against the bitter lesson.” He’s right. AI’s capabilities may completely outrun human knowledge and skills. And once the knowledge embedded in a Skill makes it into the training data, the Skill becomes redundant.

Or does it?

Clay Christensen articulated what he called the [law of conservation of attractive profits](<https://store.hbr.org/product/breakthrough-ideas-for-2004-the-hbr-list/R0402A>): when a product becomes commoditized, value migrates to an adjacent layer. Clay and I bonded over this idea when we first met at the Open Source Business Conference in 2004. Clay talked about his new “law.” I talked about a recurring pattern I was seeing in the history of computing, which was leading me in the direction of what we were soon to call [Web 2.0](<https://www.oreilly.com/pub/a/web2/archive/what-is-web-20.html>): Microsoft beat IBM because they understood that software became more valuable once PC hardware was a commodity. Google understood how data became more valuable when open source and open protocols commoditized the software platform. Commoditization doesn’t destroy value, it moves it.

Even if the bitter lesson commoditizes knowledge, what becomes valuable next? I think there are several candidates.

First, taste and curation. When everyone has access to the same commodity knowledge, the ability to select, combine, and apply it with judgment becomes valuable. Steve Jobs did this when the rest of the industry was racing toward the commodity PC. He created a unique integration of hardware, software, and design that transformed commodity components into something precious. The Skill equivalent might not be “here’s how to do X” (which the model already knows) but “here’s how _we_ do X, with the specific judgment calls and quality standards that define our approach.” That’s harder to absorb into training data because it’s not just knowledge, it’s _values_.

You can see this pattern repeat across one commodity market after another. This is the essence of fashion, for example, but also applies to areas as diverse as coffee, water, consumer goods, and automobiles. In his essay “[The Birth of the Big Beautiful Art Market](<https://www.amazon.com/Air-Guitar-Essays-Art-Democracy/dp/0963726455>),” art critic Dave Hickey calls how commodities are turned into a kind of “art market,” where something is sold on the basis of what it means rather than just what it does. Owning a Mac rather than a PC _meant_ something.

Second, the human touch. As economist Adam Ozimek [pointed out](<https://agglomerations.substack.com/p/economics-of-the-human>), people still go listen to live music from local bands despite the abundance of recorded music from the world’s greatest performers. The human touch is what economists call a “normal good”: demand for it goes up as income goes up. As I discussed with Claude in “[Why AI Needs Us](<https://timoreilly.substack.com/p/why-ai-needs-us>),” human individuality is a fount of creativity. AI without humans is a kind of recorded music. AI plus humans is live.

Third, freshness. Skills that encode rapidly changing workflows, current tool configurations, or evolving best practices will always have a temporal advantage. There is alpha in knowing something first.

Fourth, tools themselves. The bitter lesson applies to the knowledge that lives in the context portion of a Skill. It may not apply in the same way to the deterministic tools that save tokens or do things the model can’t do by thinking harder. And tools, unlike context, can be protected behind APIs, metered, and monetized.

Fifth, coordination and orchestration. Even if individual Skills get absorbed into model knowledge, the patterns for how Skills compose, negotiate, and hand off to each other may not. The choreography of a complex workflow might be the layer where value accumulates as the knowledge layer commoditizes.

But more importantly, the idea that any knowledge that becomes available automatically becomes the property of any LLM is not foreordained. It is an artifact of an IP regime that the AI labs have adopted for their own benefit: a variation of the “empty lands” argument that European colonialists used to justify their taking of others’ resources. AI has been developed in an IP wild west. That may not continue. The fulfillment of AI labs’ vision of a world where their products absorb all human knowledge and then put humans out of work [leaves them without many of the customers they currently rely on](<https://x.com/timoreilly/status/2016317410853220827>). Not only that, they themselves are being reminded why IP law exists, as [Chinese models copy their advances by exfiltrating their weights](<https://www.economist.com/china/2026/02/25/anthropic-says-chinas-ai-tigers-are-copycats>). There is a historical parallel in the way that US publishing companies ignored European copyrights until they themselves had homegrown assets to protect.

## **Where we are now**

What I’m starting to see are the first halting steps toward a new software ecosystem where the “programs” are mixtures of natural language and code, the “runtime” is a large language model, and the “users” are AI agents as well as humans. Skills, Superpowers, and knowledge plugins might represent the first practical mechanism for making tacit knowledge accessible to computational agents.

Several gaps keep coming up, though. Composability: the real power may come from Skills that work together, much like Unix utilities piped together. How do trust, payment, and quality propagate through a chain of Skill invocations? Trust and security: Simon Willison has written about [tool poisoning and prompt injection risks in MCP](<https://simonw.substack.com/p/model-context-protocol-has-prompt>). The security model for composable, agent-discovered Skills is essentially unsolved. Evaluation: we don’t have good ways to verify Skill quality except by running them, which is expensive and nondeterministic.

And then there’s the economic plumbing, which is to me the most glaring gap. Consider Anthropic’s Cowork plugins. They are exactly the pattern I’ve been describing, tacit knowledge made executable, delivered at enterprise scale. But there is no mechanism for the domain experts whose knowledge makes plugins valuable to get paid for them. If the AI labs believed in a future where AI extends the human knowledge economy rather than replacing it, they would be building payment rails alongside the plugin architecture. The fact that they aren’t tells you something about their actual theory of value.

If you’re working on any of this, whether skill marketplaces and discovery, composability patterns, protection models, quality and evaluation, attribution and compensation, or security models, [I want to hear from you](<https://github.com/oreillymedia/skills-and-the-future-knowledge-economy>).

The future of software isn’t just code. It’s knowledge, packaged for machines, traded between agents, and, if we get the infrastructure right, creating value that flows back to the humans whose expertise and unique perspectives make it all work.

> _Thanks to Andrew Odewahn, Angie Jones, Claude Opus 4.6, James Cham, Jeff Weinstein, Jonathan Hassell, Matt Beane, Mike Loukides, Peyton Joyce, Sruly Rosenblat, Steve Yegge, and Tadas Antanavicius for comments on drafts of this piece. You made it much stronger with your insights and objections._
