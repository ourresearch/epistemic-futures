---
title: "AI and Programming: The Beginning of a New Era"
person: tim-oreilly
section: by
type: blog-post
year: 2025
date: 2025-05-08
venue: "O'Reilly Radar"
authors: "Tim O'Reilly"
source_url: https://www.oreilly.com/radar/ai-and-programming-the-beginning-of-a-new-era/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the oreilly.com/radar WordPress REST API (people_taxonomy=tim-oreilly); HTML converted to markdown."
---

# AI and Programming: The Beginning of a New Era

## Full text

_Our AI Codecon conference kicked off today with Coding with AI: The End of Software Development as We Know It. Here are my opening remarks introducing the series’ themes. You can reserve your seat for upcoming AI Codecon events_[ _here_](<https://www.oreilly.com/live/>) _._

Thanks so much for joining us today. We have over 20,000 people signed up for this event, both subscribers on the [O’Reilly learning platform](<http://oreilly.com/>) and those who aren’t yet subscribers. I think you’re here because you all sense what I do: We’re witnessing not the end of programming but its remarkable expansion. This is the most exciting moment in software development that I’ve seen during my more than 40 years in this industry.

I organized this event because I’ve grown increasingly frustrated with a persistent narrative: that AI will replace programmers. I’ve heard versions of this same prediction with every technological leap forward—and it’s always been wrong. Not just slightly wrong, but fundamentally misunderstanding how technology evolves.

Programming, at its essence, is conversation with computers. It’s how we translate human intention into machine action. Throughout computing history, we’ve continuously built better translation layers between human thought and machine execution—from physical wiring to assembly language to high-level languages to the World Wide Web, which embedded calls to backend systems into a frontend made up of human-readable documents. LLMs are simply the next evolution in this conversation, making access to computer power more natural and accessible than ever before.

And here’s what history consistently shows us: Whenever the barrier to communicating with computers lowers, we don’t end up with fewer programmers—we discover entirely new territories for computation to transform.

There’s a kind of punctuated equilibrium, in which some breakthrough resets the industry, there’s a period of furious innovation followed by market consolidation, and frankly, a bit of stasis, until some new technology upsets the apple cart and sets off another period of reinvention.

## **The Historical Pattern of Expansion**

Consider how dramatically programming has evolved over the decades. It used to be really hard to tell computers what we wanted them to do. The earliest programmers had to physically connect circuits to execute different operations. Then came the von Neumann stored program architecture. That let programmers provide binary instructions through front panel switches. That was followed by assembly language, then compilers that took high-level, more-human-like descriptions and automatically translated them into the machine code that matched the architecture of the underlying system. With the World Wide Web, the interface to computers became human-readable _documents_ that had some of the characteristics of a program. Links didn’t just summon new pages but ran other programs. Each step made the human-machine conversation more natural.

With each evolution, skeptics predicted the obsolescence of “real programming.” Real programmers debugged with an oscilloscope. Yet the opposite occurred. The field expanded, creating new specialties and bringing more people into the conversation.

Take the digital spreadsheet—a revolutionary tool that changed business forever. Dan Bricklin and Bob Frankston first prototyped VisiCalc in BASIC, the 1970s equivalent of today’s “vibe coding.” To create a viable product, they then rewrote it in assembly language for the 6502 microprocessor, the CPU for the Apple II. They had to do it this way to optimize performance and fit the program within the Apple II’s memory constraints. This pattern is instructive: Simplified tools enable rapid prototyping and experimentation, while deeper technical knowledge remains essential for production.

Twenty years later, Tim Berners-Lee created the World Wide Web prototype on a NeXT machine—another leap forward in programming accessibility. So many of us learned to build our first web page simply by pulling down a menu, clicking “View Source,” and modifying the simple HTML code. Many of the people who created billion-dollar businesses on the early web began as amateur programmers. Many of them told me that they learned what they needed to know from an O’Reilly book.

## **AI-Assisted Programming Today: Democratization on Steroids**

That same pattern is repeating now—but at unprecedented scale and speed.

Recently, a tech executive told me about his high-school-age daughter’s summer internship with a Stanford biomedical professor. Despite having no programming background—her interests were in biology and medicine—she was tasked with an ambitious challenge. The professor pointed out that pulse oximeters don’t work very well; the only way to get a good blood oxygen reading is with a blood draw. He said, “I have an idea that it might be possible to get a good reading out of the capillaries in the retina. Why don’t you look into that?” So she did. She fed ChatGPT lots of images of retinas, got it to isolate the capillaries, and then asked how it might detect oxygen saturation. That involved some coding. Pretty gnarly image recognition that normally would have taken a lot of programming experience to write. But by the end of the summer, she had a working program that was able to do the job.

Now it’s easy to draw the conclusion from a story like this that this is the end of professional programming, that AI can do it all. For me, the lesson is the complete opposite. Pre-AI, investigating an idea like this would have meant taking it seriously enough to write a grant application, hire a researcher and a programmer, and give it a go. Now, it’s tossed off to a high school intern! What that shouts to me is that **the cost of trying new things has gone down by orders of magnitude. And that means that the addressable surface area of programming has gone up by orders of magnitude.** There’s so much more to do and explore.

And do you think that that experiment is the end of this project? Is this prototype the finished product? Of course not. Turning it into something robust, reliable, and medically valid will require professional software engineers who understand systems design, testing methodologies, regulatory requirements, and deployment at scale.

**Right now, we’re seeing a lot of people reengineering old ideas to do them better with AI. The next stage is going to be tackling entirely new problems, things that we couldn’t have—or wouldn’t have bothered to try—without AI.**

## **The New Spectrum: From Vibe Coding to AI Engineering**

What’s emerging is a new spectrum of software creation. At one end is “vibe coding”—rapid, intuitive programming assisted by AI. At the other end is systematic AI engineering—the disciplined integration of models into robust systems.

This mirrors the evolution of the web. What began as simple static HTML pages evolved into complex, interconnected systems with frameworks, APIs, and cloud infrastructure—what I called in 2005 “software above the level of a single device.” The web didn’t eliminate programming jobs; it created entirely new categories of development work. Frontend engineering, backend engineering, DevOps, information security. More JavaScript frameworks than anyone can keep track of!

We’re seeing that same pattern with LLMs and agents. The raw model is just the beginning—like HTML was to the web. The real magic happens in how these models are integrated, refined, and deployed as components in larger systems.

## **The New Hybrid Computing Paradigm**

A tool like ChatGPT, Perplexity, or Cursor highlights just how much more there is to an AI application than the model. **The naked model is dressed in fashions dreamed up by entrepreneurs, shaped by product managers, and pieced together by AI engineers.** Any AI app (including just a chatbot) is actually a hybrid of AI and traditional software engineering.

In a recent conversation in a private chat group, Eran Sandler used a car metaphor: “The model is the engine, but you need a whole lot around it to make it a sports car—context management, codified workflows, and more. Those are the ‘real uses’ of AI models.”

This reminded me of Phillip Carter’s insight that we’re now programming with two fundamentally different types of computers: one that can write poetry but struggles with basic arithmetic, another that calculates flawlessly but lacks creativity. The art of modern development is orchestrating these systems to complement each other.

Sam Schillace added another dimension: “There’s now a tension between reliable and flexible—code is reliable but rigid, inference is flexible but unreliable.” He described how the new job of the programmer is to craft carefully designed “metacognitive recipes”—code that manages and directs AI inference. Doing this well can transform a task from 5%–10% reliable to nearly 100% in specific domains.

These conversations reveal the future landscape. We’re not at the end of programming—we’re at the beginning of its most profound reinvention yet.

## **A Renaissance of Innovation**

It’s an extraordinary time to be in software development. After years of incremental advances that made the field feel somewhat predictable, we’re entering a period of radical innovation. The fundamental building blocks of how we create software are changing.

This isn’t just about using AI tools to write code faster—though that’s valuable. It’s about reimagining what software can do, who can create it, and how we approach problems that previously seemed intractable.

This conference will explore three critical dimensions of this new landscape:

  * How to effectively collaborate with AI to enhance your current development workflow
  * The emerging patterns and antipatterns of building reliable, production-grade AI systems
  * The expanding opportunity landscape as previously infeasible projects become possible

The programming world was frankly getting a bit predictable for a while. The fun is back—along with unprecedented opportunity. Throughout this event, I hope you’ll not just absorb information but actively consider: What problem that seemed impossible yesterday might you now be able to solve?

Let’s embrace this moment not with fear but with the excitement of explorers discovering new territory.
