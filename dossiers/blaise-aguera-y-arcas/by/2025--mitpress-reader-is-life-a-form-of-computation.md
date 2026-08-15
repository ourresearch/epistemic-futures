---
title: "Is Life a Form of Computation?"
person: blaise-aguera-y-arcas
section: by
type: essay
year: 2025
date: 2025-09
venue: "The MIT Press Reader"
authors: "Blaise Agüera y Arcas"
source_url: https://thereader.mitpress.mit.edu/is-life-a-form-of-computation/
retrieved: 2026-08-13
content: full-text
notes: "Adapted from the book *What Is Intelligence?*. The live page is Cloudflare-walled to headless clients; text retrieved through a real browser session. The article confirms that the whatisintelligence.antikythera.org edition of the book is its official open-access edition."
---

# Is Life a Form of Computation?

## Full text

**Alan Turing and John von Neumann saw it early: the logic of life and the logic of code may be one and the same.**

By: Blaise Agüera y Arcas

In 1994, a strange, pixelated machine came to life on a computer screen. It read a string of instructions, copied them, and built a clone of itself — just as the Hungarian-American Polymath John von Neumann had predicted half a century earlier. It was a striking demonstration of a profound idea: that life, at its core, might be computational.

*This article is adapted from Blaise Agüera y Arcas's book "What Is Intelligence?" An open access edition of the book is available [here](https://whatisintelligence.antikythera.org/).*

Although this is seldom fully appreciated, von Neumann was one of the first to establish a deep link between life and computation. Reproduction, like computation, he showed, could be carried out by machines following coded instructions. In his model, based on Alan Turing's Universal Machine, self-replicating systems read and execute instructions much like DNA does: "if the next instruction is the codon CGA, then add an arginine to the protein under construction." It's not a metaphor to call DNA a "program" — that is literally the case.

Of course, there are meaningful differences between biological computing and the kind of digital computing done by a personal computer or your smartphone. DNA is subtle and multilayered, including phenomena like epigenetics and gene proximity effects. Cellular DNA is nowhere near the whole story, either. Our bodies contain (and continually swap) countless bacteria and viruses, each running their own code.

> It's not a metaphor to call DNA a "program" — that is literally the case.

Biological computing is "massively parallel," decentralized, and noisy. Your cells have somewhere in the neighborhood of 300 quintillion ribosomes, all working at the same time. Each of these exquisitely complex floating protein factories is, in effect, a tiny computer — albeit a stochastic one, meaning not entirely predictable. The movements of hinged components, the capture and release of smaller molecules, and the manipulation of chemical bonds are all individually random, reversible, and inexact, driven this way and that by constant thermal buffeting. Only a statistical asymmetry favors one direction over another, with clever origami moves tending to "lock in" certain steps such that a next step becomes likely to happen.

This differs greatly from the operation of "logic gates" in a computer, basic components that process binary inputs into outputs using fixed rules. They are irreversible and engineered to be 99.99 percent reliable and reproducible.

Biological computing is computing, nonetheless. And its use of randomness is a feature, not a bug. In fact, many classic algorithms in computer science also require randomness (albeit for different reasons), which may explain why Turing insisted that the Ferranti Mark I, an early computer he helped to design in 1951, include a random number instruction. Randomness is thus a small but important conceptual extension to the original Turing Machine, though any computer can simulate it by calculating deterministic but random-looking or "pseudorandom" numbers.

Parallelism, too, is increasingly fundamental to computing today. Modern AI, for instance, depends on both massive parallelism and randomness — as in the parallelized "stochastic gradient descent" (SGD) algorithm, used for training most of today's neural nets, the "temperature" setting used in chatbots to introduce a degree of randomness into their output, and the parallelism of Graphics Processing Units (GPUs), which power most AI in data centers.

Traditional digital computing, which relies on the centralized, sequential execution of instructions, was a product of technological constraints. The first computers needed to carry out long calculations using as few parts as possible. Originally, those parts were flaky, expensive vacuum tubes, which had a tendency to burn out and needed frequent replacement by hand. The natural design, then, was a minimal "Central Processing Unit" (CPU) operating on sequences of bits ferried back and forth from an external memory. This has come to be known as the "von Neumann architecture."

Turing and von Neumann were both aware that computing could be done by other means, though. Turing, near the end of his life, explored how biological patterns like leopard spots could arise from simple chemical rules, in a field he called morphogenesis. Turing's model of morphogenesis was a biologically inspired form of massively parallel, distributed computation. So was his earlier concept of an "unorganized machine," a randomly connected neural net modeled after an infant's brain.

These were visions of what computing without a central processor could look like — and what it does look like, in living systems.

Von Neumann also began exploring massively parallel approaches to computation as far back as the 1940s. In discussions with Polish mathematician Stanisław Ulam at Los Alamos, he conceived the idea of "cellular automata," pixel-like grids of simple computational units, all obeying the same rule, and all altering their states simultaneously by communicating only with their immediate neighbors. With characteristic bravura, von Neumann went so far as to design, on paper, the key components of a self-reproducing cellular automaton, including a horizontal "tape" of cells containing instructions and blocks of cellular "circuitry" for reading, copying, and executing them.

Designing a cellular automaton is far harder than ordinary programming, because every cell or "pixel" is simultaneously altering its own state and its environment. Add randomness and subtle feedback effects, as in biology, and it becomes even harder to reason about, "program," or "debug."

> With characteristic bravura, von Neumann went so far as to design, on paper, the key components of a self-reproducing cellular automaton.

Nonetheless, Turing and von Neumann grasped something fundamental: Computation doesn't require a central processor, logic gates, binary arithmetic, or sequential programs. There are infinite ways to compute, and, crucially, they are all equivalent. This insight is one of the greatest accomplishments of theoretical computer science.

This "platform independence" or "multiple realizability" means that any computer can emulate any other one. If the computers are of different designs, though, the emulation may be glacially slow. For that reason, von Neumann's self-reproducing cellular automaton has never been physically built — though that would be fun to see!

That demonstration in 1994 — the first successful emulation of von Neumann's self-reproducing automation — couldn't have happened much earlier. A serial computer requires serious processing power to loop through the automaton's 6,329 cells over the 63 billion time steps required for the automaton to complete its reproductive cycle. Onscreen, it worked as advertised: a pixelated two-dimensional Rube Goldberg machine, squatting astride a 145,315-cell–long instruction tape trailing off to the right, pumping information out of the tape and reaching out with a "writing arm" to slowly print a working clone of itself just above and to the right of the original.

It's similarly inefficient for a serial computer to emulate a parallel neural network, heir to Turing's "unorganized machine." Consequently, running big neural nets like those in Transformer-based chatbots has only recently become practical, thanks to ongoing progress in the miniaturization, speed, and parallelism of digital computers.

In 2020, my colleague Alex Mordvintsev combined modern neural nets, Turing's morphogenesis, and von Neumann's cellular automata into the "neural cellular automaton" (NCA), replacing the simple per-pixel rule of a classic cellular automaton with a neural net. This net, capable of sensing and affecting a few values representing local morphogen concentrations, can be trained to "grow" any desired pattern or image, not just zebra stripes or leopard spots.

Real cells don't literally have neural nets inside them, but they do run highly evolved, nonlinear, and purposive "programs" to decide on the actions they will take in the world, given external stimulus and an internal state. NCAs offer a general way to model the range of possible behaviors of cells whose actions don't involve movement, but only changes of state (here, represented as color) and the absorption or release of chemicals.

The first NCA Alex showed me was of a lizard emoji, which could regenerate not only its tail, but also its limbs and head! It was a powerful demonstration of how complex multicellular life can "think locally" yet "act globally," even when each cell (or pixel) is running the same program — just as each of your cells is running the same DNA. Simulations like these show how computation can produce lifelike behavior across scales. Building on von Neumann's designs and extending into modern neural cellular automata, they offer a glimpse into the computational underpinnings of living systems.

*Blaise Agüera y Arcas is a VP/Fellow at Google, where he is the CTO of Technology & Society, and the founder of Paradigms of Intelligence, an organization dedicated to fundamental AI research. He is the author of "What Is Intelligence?," from which this article is adapted. An open access edition of the book is available [here](https://whatisintelligence.antikythera.org/).*
