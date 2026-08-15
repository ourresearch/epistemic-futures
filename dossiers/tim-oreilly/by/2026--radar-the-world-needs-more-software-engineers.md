---
title: "The World Needs More Software Engineers"
person: tim-oreilly
section: by
type: blog-post
year: 2026
date: 2026-04-07
venue: "O'Reilly Radar"
authors: "Tim O'Reilly"
source_url: https://www.oreilly.com/radar/the-world-needs-more-software-engineers/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the oreilly.com/radar WordPress REST API (people_taxonomy=tim-oreilly); HTML converted to markdown."
---

# The World Needs More Software Engineers

## Full text

I sat down with Aaron Levie at the O’Reilly [AI Codecon](<https://www.oreilly.com/AI-Codecon/>) two weeks ago. Aaron cofounded Box in 2005, and 20 years later, his company manages content for about two-thirds of the Fortune 500. Aaron is one of the few CEOs of an incumbent enterprise software company thinking deeply in public about what AI means for the entire enterprise stack. There are a lot of people who are building companies from the ground up with AI, others who are dragging their feet adapting existing enterprises to it, and then there’s Aaron. He sits in a kind of Goldilocks zone, enthusiastic but not uncritical, engaging in the hard work of adapting AI to the enterprise and the enterprise to AI.

## **The engineering demand paradox**

I started out by asking about something from [_Lenny’s Newsletter_](<https://x.com/lennysan/status/2036483059407810640>) that [Aaron had retweeted](<https://x.com/levie/status/2036832183131033977?s=20>). Despite all the doom rhetoric, TrueUp data shows software engineering job postings are at a three-year high. Product manager jobs are way up. AI jobs as a whole are way up.

The actual data may be more equivocal than the TrueUp report suggests. The honest read of the literature as of spring 2026 ([Brynjolfsson et al.](<https://digitaleconomy.stanford.edu/wp-content/uploads/2025/08/Canaries_BrynjolfssonChandarChen.pdf>), [Humlum and Vestergaard](<https://www.nber.org/system/files/working_papers/w33777/w33777.pdf>), [BLS Software Developers](<https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm>), [BLS Computer Programmers)](<https://www.bls.gov/ooh/computer-and-information-technology/computer-programmers.htm>) is that something real is happening to entry-level software work, that it is happening faster than most previous technology transitions, that it has different effects depending on which job code you look at, and that it is not yet clear whether the net effect on total software employment will be negative, neutral, or eventually positive. Nonetheless, the TrueUp report was a trigger for the discussion that followed.

Aaron noted that engineers have historically been concentrated at tech companies because the cost of a software project was too high to justify anywhere else. But if agents make an engineer two to ten times more productive, all the software projects that were never economically viable suddenly become viable. Demand doesn’t shrink. It diffuses across the entire economy. In his tweet, he called it “[Jevons paradox](<https://en.wikipedia.org/wiki/Jevons_paradox>) happening in real time.” In our conversation, he said:

> “What’s going to happen is the entire world is going to be looking at all the potential software that they build. And they’re going to start to say, Oh, I can finally justify going out and doing this type of project where I couldn’t before.”

Engineers empowered by AI agents won’t just build software for IT teams. The total addressable role of the engineer expands from the technology department to every function in the enterprise. They’ll be wiring up automation for marketing, legal, accounting, and every other corporate function.

He’s totally right. Look around at all the crappy workflows, the crappy processes, the incredible overhead of things that ought to be simple. You think companies should lay off their developers to reduce costs when there’s so much shitty software out there? Really? There’s so much that needs to be improved. He had a great line: “Silicon Valley is spooked by its own technology.”

Over to me: The rhetoric from the labs about job destruction is actively counterproductive. I was talking recently with someone in healthcare who described a hospital system trying to fill a giant hole from reduced Medicare funding. They see AI as a way to gain efficiency in their back office so they can free up more resources for patient care. And of course the union is fighting it because they’ve been told AI is a monster that’s going to take their jobs. If you tell a different story, one about making the system better and serving more people more affordably, that’s something people can get behind. We have to change the narrative.

## **Context, not connectivity, is the real problem**

I also asked Aaron whether protocols like MCP are making context portable enough to erode competitive moats. He agreed that the industry has broadly converged on openness and interoperability (with some toll booths to work through). But getting your systems to talk to each other doesn’t solve the harder problem of getting your data structured so that agents can actually find the right information at the right moment.

> “If it’s in 50 different systems and it’s not organized in a way that agents can readily take advantage of, what you’re going to be is at the mercy of how well that agent finds exactly the context that it needs to do its work. And you’re kind of just rolling the dice every time you do a workflow.”

He predicts a decade of infrastructure modernization ahead, which sounds about right. At O’Reilly, I keep running into this myself. I’ll see a task that’s perfect for an agent and soon discover that the data I need is scattered across four systems and I have to jump through hoops to figure out who knows where the data is and how to get access. A friend running a large (but relatively new) enterprise that is turbocharging productivity and service delivery with agents told me recently that a big part of his team’s success was possible because they had spent a lot of time getting their data infrastructure in order from the start.

IMO, a lot of the stories you hear about OpenClaw and other harbingers of the agent future can be misleading in an enterprise context. They are doing greenfield setups, largely running consumer apps with well-defined interfaces, and even then, it takes weeks to set up properly. Now imagine agentic frameworks for companies with thousands of employees, hundreds of legacy apps, and deep wells of proprietary data. A decade of infrastructure modernization is generous. Without help, many enterprises will have difficulty making the transition.

## **Engineering the trade-offs**

I brought up [Phillip Carter’s “two computers” framing](<https://www.phillipcarter.dev/posts/llms-computers>), that we’re now programming a deterministic computer and a probabilistic computer at the same time. Skills are a bridge, because they have both context for the LLM which can work probabilistically and tools that are built with deterministic code. Both systems coexist and work in parallel.

Aaron called the boundary between the two computers “the trillion-dollar question.” When does a process cross the threshold where it should be locked into repeatable, deterministic code? When should it stay adaptive? Loan processing needs to work the same way every time. Employee HR queries can be probabilistic. And the irony, as Aaron pointed out, is that making these trade-offs correctly requires deep technical understanding. AI makes the field more technical, not less.

I added that sometimes this judgment is a user experience question, sometimes a cost question. You can do something with an LLM, but it might be a lot cheaper with canned code. At other times, even though the LLM costs more, the flexibility of a liquid user interface is far better.

This is also a locus of creativity. What you bring out of AI is what you bring to it. Steve Jobs wasn’t a coder, but he knew how to get the most out of coders. He would have gone nuts with AI agents, because he was the essence of taste and judgment and setting the bar.

## **Where startups win**

I asked Aaron about the risks to existing enterprises from greenfield AI startups that can just move faster, reinventing what the incumbents do with an AI native solution, without all the baggage. He replied:

> “If there’s already a substantial amount of the data for that particular workflow in an existing system, and the incumbent is agile enough and responsive enough, then they are in a good position to build either the solutions or to monetize that set of work that’s going to be done….What agents are really good at is automating the unstructured areas of work, the messy, collaborative human-based parts of work, the tax process, the legal review process, the audit and risk analysis process of all of your contracts and unstructured data. And so in those areas, there’s no incumbent. The only incumbent is likely professional services firms. So that’s where I would favor startups.”

Software startups like [Harvey](<https://www.harvey.ai/>) are already taking services domains and building agents for them. But it’s not just software startups. Aaron also sees lots of opportunity for AI-native law firms, accounting firms, and ad agencies that can throw away legacy workflow, start from scratch, and deliver two to five times the output at lower cost will have a huge advantage.

I did push back with a point I think is underappreciated: Existing enterprises face a real risk that the organization will try to stuff AI into existing workflows rather than asking what the AI-native workflow would be. People are attached to their jobs, their roles, the org chart. We have to wrestle with that honestly if we’re going to truly reinvent what we do.

## **Humans get context for free**

One of Aaron’s points about agents is that humans carry an enormous amount of ambient context that agents lack. You know what building you’re in and who else works there and what they do. You know the meeting that just happened where a team changed course on a strategy that hasn’t been written down yet. You have 20 years of accumulated domain knowledge. All of that is free context that we’ve never had to formalize. As he put it, “We’ve never built our business processes in a model where we assume that there’s a new user in that workflow that appeared one second ago and in under five seconds, they need to get all of the information possible to do that task.”

He suggested that one way to think of agents is as new employees who are experts but arrive with zero context and need to be fully briefed. And the context has to be precise, not just comprehensive. Give an agent too much context and it gets confused. Give it too little and it rolls the dice. SKILLS.md and AGENTS.md files are attempts to provide exactly the surgical context an agent needs for a specific process.

But 99% of knowledge work doesn’t have an AGENTS.md file, he noted. The data is everywhere. The context is everywhere. So in an existing enterprise, you have to reengineer workflows from the ground up to deliver the right information to agents at the right moment.

Aaron summed up Box’s strategic pivot in one sentence: swap the word “content” for “context” and the rest of the strategy stays the same. Enterprise context lives in contracts, research materials, financial documents. That’s all enterprise content but it isn’t always easily available as context. The evolution is making agents first-class citizens alongside people as users of that content. This very much maps to what we’re thinking about at O’Reilly too.
