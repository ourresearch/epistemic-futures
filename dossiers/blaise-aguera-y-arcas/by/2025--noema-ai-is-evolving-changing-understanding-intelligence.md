---
title: "AI Is Evolving — And Changing Our Understanding Of Intelligence"
person: blaise-aguera-y-arcas
section: by
type: essay
year: 2025
date: 2025-04
venue: "Noema Magazine"
authors: "Blaise Agüera y Arcas, James Manyika"
source_url: https://www.noemamag.com/ai-is-evolving-and-changing-our-understanding-of-intelligence/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# AI Is Evolving — And Changing Our Understanding Of Intelligence

## Full text

# AI Is Evolving — And Changing Our Understanding Of Intelligence

Advances in AI are making us reconsider what intelligence is and giving us clues to unlocking AI’s full potential.

Kate Banazi for Noema Magazine

Credits

Blaise Agüera y Arcas is a vice president and fellow at Google, where he is the chief technology officer of Technology & Society and founder of the Paradigms of Intelligence team. His book “What Is Intelligence?” will be released in September by Antikythera and MIT Press.

James Manyika is a Google-Alphabet senior vice president and president of Research, Labs, Technology & Society at Google, where he advances Google and Alphabet’s most ambitious innovations in AI, computing and science. He served as vice-chair of the U.S. National AI Advisory Committee and co-chair of the UN Secretary-General’s AI Advisory Body.

Dramatic advances in artificial intelligence today are compelling us to rethink our understanding of what intelligence truly _is_. Our new insights will enable us to build better AI and understand ourselves better.

In short, we are in paradigm-shifting territory.

Paradigm shifts are often fraught because it’s easier to adopt new ideas when they are compatible with one’s existing worldview but harder when they’re not. A classic example is the collapse of the geocentric paradigm, which dominated cosmological thought for roughly two millennia. In the geocentric model, the Earth stood still while the Sun, Moon, planets and stars revolved around us. The belief that we were at the center of the universe — bolstered by Ptolemy’s theory of epicycles, a major scientific achievement in its day — was both intuitive and compatible with religious traditions. Hence, Copernicus’s heliocentric paradigm wasn’t just a scientific advance but a hotly contested heresy and perhaps even, for some, as Benjamin Bratton notes, an existential trauma. So, today, artificial intelligence.

In this essay, we will describe five interrelated paradigm shifts informing our development of AI:

  1. **_Natural Computing_** — Computing existed in nature long before we built the first “artificial computers.” Understanding computing as a natural phenomenon will enable fundamental advances not only in computer science and AI but also in physics and biology.
  2. **_Neural Computing_** — Our brains are an exquisite instance of natural computing. Redesigning the computers that power AI so they work more like a brain will greatly increase AI’s energy efficiency — and its capabilities too.
  3. **_Predictive Intelligence_** — The success of large language models (LLMs) shows us something fundamental about the nature of intelligence: it involves statistical modeling of the future (including one’s own future actions) given evolving knowledge, observations and feedback from the past. This insight suggests that current distinctions between designing, training and running AI models are transitory; more sophisticated AI will evolve, grow and learn continuously and interactively, as we do.
  4. **_General Intelligence_** — Intelligence does not necessarily require biologically based computation. Although AI models will continue to improve, they are already broadly capable, tackling an increasing range of cognitive tasks with a skill level approaching and, in some cases, exceeding individual human capability. In this sense, “Artificial General Intelligence” (AGI) may already be here — we just keep shifting the goalposts.
  5. **_Collective Intelligence_** — Brains, AI agents and societies can all become more capable through increased scale. However, size alone is not enough. Intelligence is fundamentally social, powered by cooperation and the division of labor among many agents. In addition to causing us to rethink the nature of human (or “more than human”) intelligence, this insight suggests social aggregations of intelligences and multi-agent approaches to AI development that could reduce computational costs, increase AI heterogeneity and reframe AI safety debates.

Perhaps the greatest Copernican trauma of the AI era is simply coming to terms with how commonplace general and nonhuman intelligence may be. But to understand our own “intelligence geocentrism,” we must begin by reassessing our assumptions about the nature of computing, since it is the foundation of both AI and, we will argue, intelligence in any form.

## Natural Computation

Is “computer science” a science at all? Often, it’s regarded more as an engineering discipline, born alongside the World War II-era Electrical Numerical Integrator and Computer (ENIAC), the first fully programmable general-purpose electronic computer —and the distant ancestor of your smartphone.

Theoretical computer science predates computer engineering, though. A groundbreaking 1936 publication by British mathematician Alan Turing introduced the imaginary device we now call the Turing Machine, consisting of a head that can move left or right along a tape, reading, erasing and writing symbols on the tape according to a set of rules. Endowed with suitable rules, a Turing Machine can follow instructions encoded on the tape — what we’d now call a computer program, or code — allowing such a “Universal Turing Machine” (UTM) to carry out arbitrary computations. Turning this around, a computation is anything that can be done by a UTM. When the ENIAC was completed in 1945, it became the world’s first real-life UTM.

Or maybe not. A small but growing roster of unorthodox researchers with deep backgrounds in both physics and computer science, such as Susan Stepney at the University of York, have made the case in 2014 in the research journal “Proceedings of The Royal Society A” that the natural world is full of computational systems “where there is no obvious human computer user.” John Wheeler, a towering figure in 20th-century physics, championed the radical “it from bit” hypothesis, which holds that the underlying structure of the universe is computational. According to Wheeler, the elementary phenomena we take to be physical —quarks, electrons, photons — are products of underlying computation, like internet packets or image pixels.

> “Perhaps the greatest Copernican trauma of the AI era is simply coming to terms with how commonplace general and nonhuman intelligence may be.” 

In some interpretations of quantum mechanics, this computation takes place in a multiverse — that is, vast numbers of calculations occurring in parallel, entangled universes. However one interprets the underlying physics, the very real technology of quantum computing taps into that parallelism, allowing us to perform certain calculations in minutes that would require the lifetime of the universe several times over on today’s most powerful supercomputers. This is, by any measure, a paradigm shift in computing.

Claims that computing underlies physical reality are hard to prove or disprove, but a clear-cut case for computation in nature came to light far earlier than Wheeler’s “it from bit” hypothesis. John von Neumann, an accomplished mathematical physicist and another founding figure of computer science, discovered a profound link between computing and biology as far back as 1951.

Von Neumann realized that for a complex organism to reproduce, it would need to contain instructions for building itself, along with a machine for reading and executing that instruction “tape.” The tape must also be copyable and include the instructions for building the machine that reads it. As it happens, the technical requirements for that “universal constructor” correspond precisely to the technical requirements for a UTM. Remarkably, von Neumann’s insight anticipated the discovery of DNA’s Turing-tape-like structure and function in 1953.

Von Neumann had shown that life is inherently computational. This may sound surprising, since we think of computers as decidedly _not_ alive, and of living things as most definitely not computers. But it’s true: DNA _is_ code — although the code is hard to reverse-engineer and doesn’t execute sequentially. Living things necessarily compute, not only to reproduce, but to develop, grow and heal. And it is becoming increasingly possible to edit or program foundational biological systems.

Turing, too, made a seminal contribution to theoretical biology, by describing how tissue growth and differentiation could be implemented by cells capable of sensing and emitting chemical signals he called “morphogens” — a powerful form of analog computing. Like von Neumann, Turing got this right, despite never setting foot in a biology lab.

By revealing the computational basis of biology, Turing and von Neumann laid the foundations for artificial life or “ALife,” a field that today remains obscure and pre-paradigmatic — much like artificial intelligence was until recently.

Yet there is every reason to believe that ALife will soon flower, as AI has. Real progress in AI had to wait until we could muster enough “artificial” computation to model (or at least mimic) the activity of the billions of neurons it takes to approach brain-like complexity. _De novo_ ALife needs to go much further, recapitulating the work of billions of years of evolution on Earth. That remains a heavy lift. We are making progress, though.

Recent experiments from our Paradigms of Intelligence team at Google have shown that in a simulated toy universe capable of supporting computation we can go from nothing but randomness to having minimal “life forms” emerge spontaneously. One such experiment involves starting with a “soup” of random strings, each of which is 64 bytes long. Eight out of the 256 possible byte values correspond to the instructions of a minimal programming language from the 1990s called “Brainfuck.” These strings of bytes can be thought of as Turing tapes, and the eight computer instructions specify the elementary operations of a Turing machine. The experiment consists of repeatedly picking two tapes out of the soup at random, splicing them together, “running” the spliced tape, separating the tapes again, and putting them back in the soup. In the beginning, nothing much appears to happen; we see only random tapes, with a byte modified now and then, apparently at random. But after a few million interactions, functional tapes emerge and begin to self-replicate: minimal artificial life.

The emergence of artificial life looks like a phase transition, as when water freezes or boils. But whereas conventional phases of matter are characterized by their statistical uniformity — an ordered atomic lattice for ice, random atomic positions for gas and somewhere in between for liquid — living matter is vastly more complex, exhibiting varied and purposeful structure at every scale. This is because computation requires distinct functional parts that must work together, as evident in any machine, organism or program.

There’s something magical about watching complex, purposeful and functional structures emerging out of random noise in our simulations. But there is nothing supernatural or miraculous about it. Similar phase transitions from non-life to life occurred on Earth billions of years ago, and we can hypothesize similar events taking place on other life-friendly planets or moons.

> “Life is computational because its stability depends on growth, healing or reproduction; and computation itself must evolve to support these essential functions.” 

How could the intricacy of life ever arise, let alone persist, in a random environment? The answer: anything life-like that self-heals or reproduces is more “dynamically stable” than something inert or non-living because a living entity (or its progeny) will still be around in the future, while anything inanimate degrades over time, succumbing to randomness. Life is computational because its stability depends on growth, healing or reproduction; and computation itself must evolve to support these essential functions.

This computational view of life also offers insight into life’s increasing complexity over evolutionary time. Because computational matter — including life itself — is made out of distinct parts that must work together, evolution operates simultaneously on the parts and on the whole, a process known in biology as “multilevel selection.”

Existing parts (or organisms) can combine repeatedly to make ever larger, more complex entities. Long ago on the primordial sea floor (as the prevailing understanding goes) molecules came together to form self-replicating or “autocatalytic” reaction cycles; these chemical cycles combined with fatty membranes to form the earliest cells; bacteria and archaea combined to form eukaryotic cells; these complex cells combined to form multicellular organisms; and so on. Each such Major Evolutionary Transition has involved a functional symbiosis, a form of interdependency in which previously independent entities joined forces to make a greater whole.

The first rungs of this evolutionary ladder did not involve living entities with heritable genetic codes. However, once the entities joining forces were alive — and therefore computational — every subsequent combination increased the potential computing power of the symbiotic whole. Human-level intelligence, many rungs above those earliest life forms, arises from the combined computation of some 86 billion neurons, all processing in parallel.

## **Neural Computing**

The pioneers of computing were well aware of the computational nature of our brains. In fact, in the 1940s, there was little difference between the nascent fields of computer science and neuroscience. Electronic computers were developed to carry out mental operations on an industrial scale, just as factory machines were developed in the previous century to automate physical labor. Originally, repetitive mental tasks were carried out by _human_ computers — like the “hidden figures,” women who (often with little acknowledgment and low pay) undertook the lengthy calculations needed for the war effort and later the space race.

Accordingly, the logic gates that make up electronic circuits, at the heart of the new “artificial” computers, were originally conceived of as artificial neurons. Journalists who referred to computers as “electronic brains” weren’t just writing the midcentury equivalent of clickbait. They were portraying the ambitions of computer science pioneers. And it was natural enough for those first computer scientists to seek to reproduce _any_ kind of thinking.

Those hopes were soon dashed. On one hand, digital computers were a smashing success at the narrowly procedural tasks we knew how to specify. Electronic computers could be programmed to do the work of human computers cheaply, flawlessly and at a massive scale, from calculating rocket trajectories to tracking payroll. On the other hand, by the 1950s, neuroscientists had discovered that real neurons are a good deal more complicated than logic gates.

Worse, it proved impossible to write programs that could perform even the simplest everyday human functions, from visual recognition to basic language comprehension — let alone nuanced reasoning, literary analysis or artistic creativity. We had (and still have) no idea how to write down exact procedures for such things. The doomed attempt to do so is now known as “Good Old-Fashioned AI” or GOFAI. We set out to make HAL 9000, and instead, we got “Press 1 to make an appointment; press 2 to modify an existing appointment.”

A purportedly sensible narrative emerged to justify GOFAI’s failure: computers are not brains, and brains are not computers. Any contrary suggestion was naïve, “hype” or, at best, an ill-fitting metaphor. There was, perhaps, something reassuring about the idea that human behavior couldn’t be programmed. For the most part, neuroscience and computer science went their separate ways.

“Computational neuroscientists,” however, continued to study the brain as an information-processing system, albeit one based on a radically different design from those of conventional electronic computers. The brain has no central processing unit or separate memory store, doesn’t run instructions only sequentially and doesn’t use binary logic. Still, as Turing showed, computing is universal. Given enough time and memory, any computer — whether biological or technological — can simulate any other computer. Indeed, over the years, neuroscientists have built increasingly accurate computational models of biological neurons and neural networks. Such models can include not only the all-or-none pulses or “action potentials” that most obviously characterize neural activity but also the effects of chemical signals, gene expression, electric fields and many other phenomena.

> “Human-level intelligence, many rungs above those earliest life forms, arises from the combined computation of some 86 billion neurons, all processing in parallel.” 

It’s worth pausing here to unpack the word “model.” In its traditional usage, as in a model railroad or a financial model, the model is emphatically _not_ the real thing. It’s a map, not the actual territory. When neuroscientists build model neural networks, it’s generally in this spirit. They are trying to learn how brains work, not how to make computers think. Accordingly, their models are drastically simplified.

However, computational neuroscience reminds us that the brain, too, is busy computing. And, as such, the function computed by the brain is itself a model. So, the territory _is_ a map; that is, if the map were as big as the territory, it _would_ be the real thing, just as a model railroad would be if it were full-sized. If we built a fully realized model brain, in other words, it would be capable of modeling us right back!

Even as GOFAI underwent a repeated boom-and-bust cycle, an alternative “connectionist” school of thought about how to get computers to think persisted, often intersecting with computational neuroscience. Instead of symbolic logic based on rules specified by a programmer, connectionists embraced “machine learning,” whereby neural nets could learn from experience — as we largely do.

Although often overshadowed by GOFAI, the connectionists never stopped trying to make artificial neural nets perform real-life cognitive tasks. Among these stubborn holdouts were Geoffrey Hinton and John Hopfield, who won the Nobel Prize in physics last year for their work on machine learning; many other pioneers in the field, such as American psychologists Frank Rosenblatt and James McClelland and Japanese computer scientist Kunihiko Fukushima, have been less widely recognized. Unfortunately, the 20th-century computing paradigm was (at least until the 1990s) unfriendly to machine learning, not only due to widespread skepticism about neural nets but also because programming was inherently symbolic. Computers were made for running instructions sequentially — a poor fit for neural computing. Originally, this was a design choice.

The first logic gates were created using vacuum tubes, which were unreliable and needed frequent replacement. To make computation as robust as possible, it was natural to base all calculations on a minimum number of distinguishable “states” for each tube: “off” or “on.” Hence binary, which uses only 0 and 1 — and also happens to be a natural basis for Boolean logic, whose elementary symbols are “True” (or 1) and “False” (or 0).

It was also natural to build a “Central Processing Unit” (CPU) using a minimal number of failure-prone tubes, which would then be used to execute one instruction after another. This meant separating processing from memory and using a cable or “bus” to sequentially shuttle data and instructions from the memory to the CPU and back.

This “classical” computing paradigm flourished for many years thanks to Moore’s Law — a famous 1965 observation by Gordon Moore, a future founder of chip maker Intel, that miniaturization was doubling the number of transistors on a chip every year or two. As transistors shrank, they became exponentially faster and cheaper, and consumed less power. So, giant, expensive mainframes became minis, then desktops, then laptops, then phones, then wearables. Computers now exist that are tiny enough to fit through a hypodermic needle. Laptops and phones consist mainly of batteries and screens; the actual computer in such a device — its “system on chip,” or SoC — is only about a square centimeter in area, and a tenth of a millimeter thick. A single drop of water occupies several times that volume.

While this scale progression is remarkable, it doesn’t lead brainward. Your brain is neither tiny nor fast; it runs much more sedately than the computer in a smartwatch. However, recall that it contains 86 billion or so neurons working at the same time. This adds up to a truly vast amount of computation, and because it happens comparatively slowly and uses information stored locally, it is energy efficient. Artificial neural computing remained inefficient, even as computers sped up, because they continued to run instructions sequentially: reading and writing data from a separate memory as needed.

It only became possible to run meaningfully sized neural networks when companies like Nvidia began to design chips with multiple processors running in parallel. Parallelization was partly a response to the petering-out of Moore’s Law in its original form. While transistors continued to shrink, after 2006 or so, they could no longer be made to run faster; the practical limit was a few billion cycles per second.

> “Artificial neural computing remained inefficient, even as computers sped up, because they continued to run instructions sequentially.” 

Parallelizing meant altering the programming model to favor short code fragments (originally called “pixel shaders” since they were designed for graphics) that could execute on many processors simultaneously. Shaders turned out to be ideal for parallelizing neural nets. Hence, the Graphics Processing Unit (GPU), originally designed for gaming, now powers AI. Google’s Tensor Processing Units (TPUs) are based on similar design principles.

Although GPUs and TPUs are a step in the right direction, AI infrastructure today remains hobbled by its classical legacy. We are still far from having chips with _billions_ of processors on them, all working in parallel on locally stored data. And AI models are still implemented using sequential instructions. Conventional computer programming, chip architecture and system design are simply not brain-like. We are simulating neural computing on classical computers, which is inefficient — just as simulating classical computing with brains was, back in the days of human computation.

Over the next few years, though, we expect to see a truly neural computing paradigm emerge. Neural computing may eventually be achieved on photonic, biological, chemical, quantum, or other entirely novel substrates. But even if “silicon brains” are manufactured using familiar chip technologies, their components will be organized differently. Every square centimeter of silicon will contain many millions of information processing nodes, like neurons, all working at once.

These neural chips won’t run programs. Their functionality will be determined not by code (at least not of the sort we have today), but by billions or trillions of numerical parameters stored across the computing area. A neural silicon brain will be capable of being “flashed,” its parameters initialized as desired; but it will also be able to learn from experience, modifying those parameters on the fly. The computation will be decentralized and robust; occasional failures or localized damage won’t matter. It’s no coincidence that this resembles nature’s architecture for building a brain.

## **Predictive** **Intelligence**

For those of us who were involved in the early development of language models, the evident generality of AI based solely on next-word (or “next-token”) prediction has been paradigm-shifting. Even if we bought into the basic premise that brains are computational, most of us believed that true AI would require discovering some special algorithm, and that algorithm would help clear up the longstanding mysteries of intelligence and consciousness. So, it came as a shock when next-token prediction alone, applied at a massive scale, “solved” intelligence.

Once we got over our shock, we realized that this doesn’t imply that there are no mysteries left, that consciousness is not real, or that the mind is a Wizard of Oz “illusion.” The neural networks behind LLMs are both enormous and provably capable of any computation, just like a classical computer running a program. In fact, LLMs can learn a wider variety of algorithms than computer scientists have discovered or invented.

Perhaps, then, the shock was unwarranted. We already knew that the brain is computational and that whatever it does must be learnable, either by evolution or by experience — or else we would not exist. We have simply found ourselves in the odd position of reproducing something before fully understanding it. When Turing and von Neumann made their contributions to computer science, theory was ahead of practice. Today, practice is ahead of theory.

Being able to create intelligence in the lab gives us powerful new avenues for investigating its longstanding mysteries, because — despite claims to the contrary — artificial neural nets are not “black boxes.” We can not only examine their chains of thought but are also learning to probe them more deeply to conduct “artificial neuroscience.” And unlike biological brains, we can record and analyze every detail of their activity, run perfectly repeatable experiments at large scale, and turn on or off any part of the network to see what it does.

While there are many important differences between AI models and brains, comparative analyses have found striking functional similarities between them too, suggesting common underlying principles. After drawing inspiration from decades of brain research, AI is thus starting to pay back its debt to neuroscience, under the banner of “NeuroAI.”

Although we don’t yet fully understand the algorithms LLMs learn, we’re starting to grasp _why_ learning to predict the next token works so well. The “predictive brain hypothesis” has a long history in neuroscience; it holds that brains evolved to continually model and predict the future — of the perceptual environment, of oneself, of one’s actions, and of their effects on oneself and the environment. Our ability to behave intentionally and intelligently depends on such a model.

> “We are simulating neural computing on classical computers, which is inefficient — just as simulating classical computing with brains was, back in the days of human computation.” 

Consider reaching for a cup of water. It’s no mean feat to have learned how to model the world and your own body well enough to bring your hand into contact with that cup, wrap your fingers around it, and bring it to your lips and drink — all in a second or two. At every stage of these movements, your nervous system computes a prediction and compares it with proprioceptive feedback. Your eyes flit across the scene, providing further error correction.

At a higher level, you predict that drinking will quench your thirst. Thirst is itself a predictive signal, though “learned” by an entire species on much longer, evolutionary timescales. Organisms incapable of predicting their need for water won’t survive long enough to pass on their faulty self-models. 

Read Noema in print.

Evolution distills countless prior generations of experience, boiled down to the crude signal of reproductive success or death. Evolutionary learning is at work when a newborn recognizes faces, or, perhaps when a cat that has never seen a snake jumps in fright upon noticing a cucumber placed surreptitiously behind it.

Machine learning involves tuning model parameters that are usually understood to represent synapses — the connections between neurons that strengthen or weaken through lifelong learning. These parameters are usually initialized randomly. But in brains, neurons wire up according to a genetically encoded (and environmentally sensitive) developmental program. We expect future AI models will similarly be evolved to construct themselves. They will grow and develop dynamically through experience rather than having static, hand-engineered architectures with fixed parameter counts.

Unifying learning across timescales may also eliminate the current dichotomy between model training and normal operation (or “inference”). Today, state-of-the-art training of LLMs is extremely expensive, requiring massive computational resources over months, while inference is comparatively cheap and can be done in real-time. Yet we know that one of the most important skills LLMs learn is _how_ to learn, which explains why it’s possible for them to handle a novel idea, word or task during a chat session.

For now, though, any such newly acquired knowledge is transient, persisting only as long as it remains within the “context window”; the model parameters remain unchanged. Future models that unify action and prediction should be able to learn cumulatively and open-endedly as they go, the way we do.

In a similar vein, we’re starting to see a shift from conceiving of AI model capability as capped by its initial offline training to “test-time scaling,” in which models become more capable simply by taking more time to think through their responses. More brain-like model designs should allow such in-the-moment improvements to accumulate, as they do for us, so that _all_ future responses can benefit.

Because the neural networks underlying LLMs are powerful general-purpose predictors, it makes sense that they have proven capable not only of modeling language, sound and video, but also of revolutionizing robotics, like in the earlier example of reaching for a glass of water. Hand-programmed GOFAI struggled for decades with anything beyond the repetitive, routinized robotics of assembly lines. But today, LLM-like “vision-language-action” models can learn how to drive all sorts of robotic bodies, from Waymo vehicles to humanoid (and many other) forms, which are increasingly deployed in complex, unstructured environments.

By using chains of thought and reasoning traces, which break large problems down into smaller intermediate steps, predictive models can even simulate multiple possible outcomes or contingencies, selecting from a tree of potential futures. This kind of “choiceful” prediction may be the mechanism underlying our notion of free will.

Ultimately, everything organisms do can be thought of as a self-fulfilling prediction. Life is that which predicts itself into continued existence, and through increasing intelligence, that prediction can become ever more sophisticated.

Embracing the paradigm of predictive processing, including the unification of planning, action and prediction, promises not only to further improve language models and robotics, but to also bring the theoretical foundations of machine learning, neuroscience and even theoretical biology onto a common footing.

## **General** **Intelligence**

According to some, LLMs are counterfeit intelligence: they give the _appearance_ of being intelligent without _actually_ being so. According to these skeptics, we have trained AI to pass the Turing Test by “autocompleting” enormous numbers of sentences, creating machines that fool us into believing there’s “someone home” when there is not.

Many hold the opposing view that AI is real and that we’re on the threshold of achieving “Artificial General Intelligence” (AGI) — though there are wide-ranging views on how to define it. Depending on the individual, this prospect may be exciting, alarming or even existentially threatening.

> “Despite claims to the contrary — artificial neural nets are not ‘black boxes.'” 

So, which camp is right? The answer might be “neither”: most in both camps hold that AGI is a discrete threshold that will (or won’t) be crossed sometime in the future. In reality, there does not appear to be any such threshold — or if there is, we may have already crossed it.

Let’s address the skeptics first. For many, AI’s ability to perform tasks — whether chatting, writing poetry, driving cars or even doing something entirely novel — is irrelevant because the way AI is implemented disqualifies it from being truly intelligent. This view may be justified by asserting that the brain must do something other than “mere” prediction, that the brain is not a computer, or simply that AI models are not alive. Consequently, skeptics often hold that, when applied to AI, terms like “intelligence,” “understanding,” “agency,” “learning,” or “hallucination” require scare quotes because they are inappropriately anthropomorphic.

Is such handwringing over diction warranted? Adopting a functional perspective suggests otherwise. We call both a bird’s wing and a plane’s wing “wings” not because they are made of the same material or work the same way, but because they serve the same function. Should we care whether a plane achieves flight differently than a bird? Not if our concern is with _purpose_ — that is, with why birds and planes have wings in the first place.

Functionalism is a hallmark of all “purposeful” systems, including organisms, ecologies and technologies. Everything “purposeful” is made up of mutually interdependent parts, each serving purposes (or functions) for the others. And those parts, too, are often themselves made out of smaller interdependent and purposeful parts.

Whether implicitly or explicitly, many AI skeptics care less about _what_ is achieved (flying or intelligence) than about _how_ it is achieved. Nature, however, is indifferent to “how.” For the sake of flexibility or robustness, engineered and natural systems alike often involve the substitution or concurrent use of parts that serve the same function but work differently. For instance, in logistics, railroads and trucks both transport goods; as a customer, you only care about getting your delivery. In your cells, aerobic or anaerobic respiration may serve the same function, with the anaerobic pathway kicking in when you exercise too hard for aerobic respiration to keep up.

The nervous system is no different. It, too, consists of parts with functional relationships, and these, too, can be swapped out for functional equivalents. We already do this, to a degree, with cochlear implants and artificial retinas, though these prostheses can’t yet approach the quality of biological ears or eyes. Eventually, though, neuroprosthetics will rival or exceed the sensory organs we’re born with.

One day, we may even be able to replace damaged brain tissue in the same way. This will work because you have no “homunculus,” no particularly irreplaceable spot in your brain where the “you” part of you lives. What makes you _you_ is not any one part of your brain or body, or your atoms — they turn over frequently in any case — nor is it the details of how every part of you is implemented. You are, rather, a highly complex, dynamic set of functional _relationships_.

What about AI models? Not only are LLMs implemented very differently from brains, but their relationships with us are also different from those between people. They don’t have bodies or life stories, kinship or long-term attachments. Such differences are relevant in considering the ethical and legal status of AI. They’re irrelevant, however, to questions of capability, like those about intelligence and understanding.

Some researchers agree with all these premises in theory but still maintain that there is a threshold to AGI and current AI systems have not crossed it yet. So how will we know when they do? The answer must involve benchmarks to test the capabilities we believe constitute general intelligence.

Many have been proposed. Some, like AI researcher François Chollet’s “Abstraction and Reasoning Corpus,” are IQ-like tests. Others are more holistic; our colleagues at Google DeepMind, for example, have emphasized the need to focus on capabilities rather than processes, stressing the need for a generally intelligent agent to be competent at a “wide range of non-physical tasks, including metacognitive tasks like learning new skills.” But which tasks should one assess? Outside certain well-defined skills within competitive markets, we may find it difficult to meaningfully bucket ourselves into “competent” (50th percentile), “expert” (90th percentile) and “virtuoso” (99th percentile).

> “For the sake of flexibility or robustness, engineered and natural systems alike often involve the substitution or concurrent use of parts that serve the same function but work differently.” 

The original definition of AGI dates to at least 2002, and can be described most simply as “general cognitive capabilities typical for humans,” as computer scientists Peter Voss and Mlađan Jovanović put it in a 2023 paper. But some frame these capabilities only in economic terms. OpenAI’s website defines AGI as “a highly autonomous system that outperforms humans at most economically valuable work.” In 2023, AI entrepreneur Mustafa Suleyman (now CEO of Microsoft AI) suggested that an AI will be generally “capable” when it can make a million dollars.

Such thresholds are both arbitrary and inconsistent with the way we think about human intelligence. Why insist on economic activity at all? How much money do we need to make to count as smart, and are those of us who have not managed to amass a fortune _not_ generally intelligent?

Of course, we’re motivated to build AI by the prospect of enriching or expanding humanity, whether scientifically, economically or socially. But economic measures of productivity are neither straightforward nor do they map cleanly to intelligence. They also exclude a great deal of human labor whose value is not accounted for economically. Focusing on the “ecological validity” of tasks — that is, on whether they matter to others, whether economically, artistically, socially, emotionally or in any other way — emphasizes the difficulty of any purely objective performance evaluation.

Today’s LLMs can already perform a wide and growing array of cognitive tasks that, a few years ago, any reasonable person would have agreed require high intelligence: from breaking down a complex argument to writing code to softening the tone of an email to researching a topic online. In nearly any given domain, a human expert can still do better. (This is the performance gap many current evaluation methodologies try to measure.) But let’s acknowledge that no single human — no matter how intelligent — possesses a comparable breadth of skills. In the past few years, we have quietly switched from measuring AI performance relative to _anyone_ to assessing it relative to _everyone_. Put another way, individual humans are now _less_ “general” than AI models.

This progress has been swift but continuous. We think the goalposts keep moving in part because no single advance seems decisive enough to warrant declaring AGI success. There’s always more to do. Yet we believe that if an AI researcher in 2002 could somehow interact with any of today’s LLMs, that researcher would, without hesitation, say that AGI is here.

One key to achieving the “general” in AGI has been “unsupervised training,” which involves machine learning without stipulating a task. Fine-tuning and reinforcement learning are usually applied afterward to enhance particular skills and behavioral attributes, but most of today’s model training is generic. AI’s broad capabilities arise by learning to model language, sound, vision or anything else. Once a model can work with such modalities generically, then, like us, it can be instructed to perform any task — even an entirely novel one — as long as that task is first described, inferred or shown by example.

To understand how we’ve achieved artificial general intelligence, why it has only happened recently, after decades of failed attempts, and what this tells us about our own minds, we must re-examine our most fundamental assumptions — not just about AI, but about the nature of computing itself.

## **Collective Intelligence**

The “social intelligence hypothesis” holds that intelligence explosions in brainy species like ours arose due to a social feedback loop. Our survival and reproductive success depend on our ability to make friends, attract partners, access shared resources and, not least, convince others to help care for our children. All of these require “theory of mind,” the ability to put oneself in another’s shoes: What does the other person see and feel? What are they thinking? What do they know, and what _don’t_ they know? How will they behave?

Keeping track of the mental states of others is a cognitive challenge. Across primate species, researchers have observed correlations between brain size and troop size. Among humans, the volumes of their brain areas associated with theory of mind correlates to the numbers of friends they have. We also know that people with more friends tend to be healthier and live longer than those who are socially isolated. Taken together, these observations are evidence of ongoing selection pressure favoring a social brain.

> “We have quietly switched from measuring AI performance relative to anyone to assessing it relative to everyone. Put another way, individual humans are now less ‘general’ than AI models.” 

While theory of mind has a Machiavellian side, it’s also essential for the advanced forms of cooperation that make humans special. Teaching and learning, division of labor, the maintenance of reputation and the mental accounting of “IOUs” all rely on theory of mind. Hence, so does the development of any nontrivial economy, political system or technology. Since tribes or communities that can cooperate at scale function as larger, more capable wholes, theory of mind doesn’t only deliver individual benefits; it also benefits the group.

As this group-level benefit becomes decisive, the social aggregation of minds tips into a Major Evolutionary Transition — a symbiosis, if you recall, in which previously independent entities join forces to make something new and greater. The price of aggregation is that formerly independent entities can no longer survive and reproduce on their own. That’s a fair description of modern urbanized society: How many of us could survive in the woods on our own?

We are a superorganism. As such, our intelligence is already collective and, therefore, in a sense, superhuman. That’s why, when we train LLMs on the collective output of large numbers of people, we are already creating a superintelligence with far greater breadth and average depth than any single person — even though LLMs still usually fall short of individual human experts within their domains of expertise.

This is what motivates Humanity’s Last Exam, a (rather grimly named) recent attempt to create an AI benchmark that LLMs can’t yet ace. The test questions were written by nearly 1,000 experts in more than 100 fields, requiring such skills as translating Palmyrene script from a Roman tombstone or knowing how many paired tendons are supported by a hummingbird’s sesamoid bone. An expert classicist could answer the former, and an expert ornithologist could answer the latter, but we suspect that median human performance on the exam would be close to zero. By contrast, state-of-the-art models today score between 3.3% and 18.8%.

Humanity is superintelligent thanks to its cognitive division of labor; in a sense, that is true of an individual brain, too. AI pioneer Marvin Minsky described a “Society of Mind,” postulating that our apparently singular “selves” are really hive minds consisting of many specialized interacting agents. Indeed, our cerebral cortex consists of an array of “cortical columns,” repeating units of neural circuitry tiled many times to form an extended surface. Although the human cortex is only about 2 to 4.5 millimeters thick, its area can be as large as 2,500 square centimeters (the brain’s wrinkled appearance is a consequence of cramming the equivalent of a large dinner napkin into our skulls). Our cortex was able to expand quickly when evolutionary pressures demanded it precisely because of its modular design. In effect, we simply added more cortical columns.

Cortical modularity is not just developmental but functional. Some parts of the cortex specialize in visual processing, others in auditory processing, touch and so on; still others appear to specialize in social modeling, writing and numeracy. Since these tasks are so diverse, one might assume each corresponding region of the brain is as specialized and different from the other as a dishwasher compared to a photocopier.

But the cortex is different: areas _start learning_ their tasks, beginning in infancy. We know that this ability to learn is powerful and general, given the existence of cortical areas such as the “visual word form area,” which specializes in reading — a skill that emerged far too recently in human history to have evolved through natural selection. Our cortex did not _evolve_ to read, but it can _learn_ to. Each cortical area, having implemented the same general “learning algorithm,” is best thought of not as an appliance with a predetermined function but as a human expert who has learned a particular domain.

This “social cortex” perspective emphasizes the lack of a homunculus or CPU in your brain where “you” reside; the brain is more like a community. Its ability to function coherently without central coordination thus depends not only on the ability of each region to perform its specialized task but also on the ability of these regions to model  _each other_ — just as people need theory of mind to form relationships and larger social units.

Do brain regions themselves function as communities of even smaller parts? We believe so. Cortical circuits are built of neurons that not only perform specialized tasks but also appear to learn to model neighboring neurons. This mirrors the familiar quip, “turtles all the way down” (a nod to the idea of infinite regress), suggesting that intelligence is best understood as a “social fractal” rather than a single, monolithic entity.

> “Do brain regions themselves function as communities of even smaller parts? We believe so.” 

It may also be “turtles all the way up.” As brains become bigger, individuals can become smarter; and as individuals become more numerous, societies can become smarter. There is a curious feedback loop between scales here, as we could only have formed larger societies by growing our brains to model others, and our brains themselves appear to have grown larger through an analogous internal division of cognitive labor.

AI models appear to obey the same principle. Researchers have popularized the idea of “scaling laws” relating model size (and amount of training data) with model capability. To a first approximation, bigger models are smarter, just as bigger brains are smarter. And like brains, AI models are also modular. In fact, many rely on explicitly training a tightly knit “collective” of specialized sub-models, known as a “Mixture of Experts.” Furthermore, even big, monolithic models exhibit “emergent modularity” — they, too, scale by learning how to partition themselves into specialized modules that can divide and conquer.

Thinking about intelligence in terms of sociality and the division of cognitive labor across many simultaneous scales represents a profound paradigm shift. It encourages us to explore AI architectures that look more like growing social networks rather than static, ever-larger monolithic models. It will also be essential to allow models (and sub-models) to progressively specialize, forming long-running collaborations with humans and with each other.

Any of the 1,000-some experts who contributed to Humanity’s Last Exam knows that you can learn only so much from the internet. Beyond that frontier, learning is inseparable from action and interaction. The knowledge frontier expands when those new learnings are shared — whether they arise from scientific experimentation, discussion or extended creative thinking offline (which, perhaps, amounts to discussion with oneself).

In today’s approach to frontier AI, existing human output is aggregated and distilled into a single giant “foundation model” whose weights are subsequently frozen. But AI models are poised to become increasingly autonomous and agentive, including by employing or interacting with other agents. AIs are already helpful in brief, focused interactions. But if we want them to aid in the larger project of expanding the frontiers of collective human knowledge and capability, we must enable them to learn and diversify interactively and continually, as we do.

This is sure to alarm some, as it opens the door to AIs evolving their capabilities open-endedly — again, as we do. The AI safety community refers to the ability for a model to evolve open-endedly as “mesa optimization,” and sees this as a threat. However, we have discovered that even today’s AI models are mesa optimizers because prediction inherently involves learning on the fly; that’s what a chatbot does when instructed to perform a novel task. It works because, even if the chatbot’s neural network weights are frozen, every output makes use of the entire “context window” containing the chat transcript so far. Still, current chatbots suffer a kind of amnesia. They are generally unable to retain their learnings beyond the context of a chat session or sessions. Google’s development of “Infini-attention” and long-term memory, both of which compress older material to allow effectively unbounded context windows, are significant recent advances in this area.The social view of intelligence offers new perspectives not only on AI engineering, but also on some longstanding problems in philosophy, such as the “hard problem” of consciousness. If we understand consciousness to mean our clear sense of ourselves as entities with our own experiences, inner lives and agency, its emergence is no mystery. We form models of “selves” because we live in a social environment full of “selves,” whose thoughts and feelings we must constantly predict using theory of mind. Of course, we need to understand that _we_ are a “self” too, not only because our own past, present and future experiences are highly salient, but because our models of others include _their_ models of _us_!

Empirical tests to diagnose deficits in theory of mind have existed for decades. When we run these tests on LLMs, we find, unsurprisingly, that they perform about as well as humans do. After all, “selves” and theory-of-mind tasks feature prominently in the stories, dialogues and comment threads LLMs are trained on. We rely on theory of mind in our chatbots, too. In every chat, the AI must not only model us but also maintain a model of itself as a friendly, helpful assistant, and a model of our model of it — and so on. 

## Beyond AI Development As Usual

After decades of meager AI progress, we are now rapidly advancing toward systems capable not just of echoing individual human intelligence, but of extending our collective more-than-human intelligence. We are both excited and hopeful about this rapid progress, while acknowledging that it is a moment of momentous paradigm change, attended, as always, by anxiety, debate, upheaval — and many considerations that we must get right.

At such times, we must prioritize not only technical advances, but knight moves that, as in chess, combine such advances with sideways steps into adjacent fields or paradigms to discover rich new intellectual territory, rethink our assumptions and reimagine our foundations. New paradigms will be needed to develop intelligence that will benefit humanity, advance science, and ultimately help us understand ourselves — as individuals, as ecologies of smaller intelligences and as constituents of larger wholes.

_The views expressed in this essay are those of the authors and do not necessarily reflect those of Google or Alphabet._

Enjoy the read? Subscribe to get the best of Noema.

###### More From Noema Magazine

Essay  Future of Democracy

The Rise & Fall Of Liberal Democracy’s Shared Fiction 

Macario Schettino

Essay  Technology & the Human

How To Future-Proof Your Career In The Age Of AI 

Nils Gilman

Essay  Digital Society

Limiting Not Just Screen Time, But Screen Space 

Laura J. Martin
