---
title: "Artificial General Intelligence Is Already Here"
person: blaise-aguera-y-arcas
section: by
type: essay
year: 2023
date: 2023-10
venue: "Noema Magazine"
authors: "Blaise Agüera y Arcas, Peter Norvig"
source_url: https://www.noemamag.com/artificial-general-intelligence-is-already-here/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Artificial General Intelligence Is Already Here

## Full text

# Artificial General Intelligence Is Already Here

Today’s most advanced AI models have many flaws, but decades from now, they will be recognized as the first true examples of artificial general intelligence.

Cecilia Erlich for Noema Magazine

Credits

Blaise Agüera y Arcas is a vice president and fellow at Google, where he is the chief technology officer of Technology & Society and founder of the Paradigms of Intelligence team. His book “What Is Intelligence?” will be released in September by Antikythera and MIT Press.

Peter Norvig is a computer scientist and Distinguished Education Fellow at the Stanford Institute for Human-Centered AI.

Artificial General Intelligence (AGI) means many different things to different people, but the most important parts of it have already been achieved by the current generation of advanced AI large language models such as ChatGPT, Bard, LLaMA and Claude. These “frontier models” have many flaws: They hallucinate scholarly citations and court cases, perpetuate biases from their training data and make simple arithmetic mistakes. Fixing every flaw (including those often exhibited by humans) would involve building an artificial superintelligence, which is a whole other project.

Nevertheless, today’s frontier models perform competently even on novel tasks they were not trained for, crossing a threshold that previous generations of AI and supervised deep learning systems never managed. Decades from now, they will be recognized as the first true examples of AGI, just as the 1945 ENIAC is now recognized as the first true general-purpose electronic computer.

The ENIAC could be programmed with sequential, looping and conditional instructions, giving it a general-purpose applicability that its predecessors, such as the Differential Analyzer, lacked. Today’s computers far exceed ENIAC’s speed, memory, reliability and ease of use, and in the same way, tomorrow’s frontier AI will improve on today’s. 

But the key property of generality? It has already been achieved.

## What Is General Intelligence?

Early AI systems exhibited artificial narrow intelligence, concentrating on a single task and sometimes performing it at near or above human level. MYCIN, a program developed by Ted Shortliffe at Stanford in the 1970s, only diagnosed and recommended treatment for bacterial infections. SYSTRAN only did machine translation. IBM’s Deep Blue only played chess.

Later deep neural network models trained with supervised learning such as AlexNet and AlphaGo successfully took on a number of tasks in machine perception and judgment that had long eluded earlier heuristic, rule-based or knowledge-based systems.

Most recently, we have seen frontier models that can perform a wide variety of tasks without being explicitly trained on each one. These models have achieved artificial general intelligence in five important ways:

  1. **Topics** : Frontier models are trained on hundreds of gigabytes of text from a wide variety of internet sources, covering any topic that has been written about online. Some are also trained on large and varied collections of audio, video and other media.
  2. **Tasks** : These models can perform a variety of tasks, including answering questions, generating stories, summarizing, transcribing speech, translating language, explaining, making decisions, doing customer support, calling out to other services to take actions, and combining words and images.
  3. **Modalities** : The most popular models operate on images and text, but some systems also process audio and video, and some are connected to robotic sensors and actuators. By using modality-specific tokenizers or processing raw data streams, frontier models can, in principle, handle any known sensory or motor modality.
  4. **Languages** : English is over-represented in the training data of most systems, but large models can converse in dozens of languages and translate between them, even for language pairs that have no example translations in the training data. If code is included in the training data, increasingly effective “translation” between natural languages and computer languages is even supported (i.e., general programming and reverse engineering).
  5. **Instructability** : These models are capable of “in-context learning,” where they learn from a prompt rather than from the training data. In “few-shot learning,” a new task is demonstrated with several example input/output pairs, and the system then gives outputs for novel inputs. In “zero-shot learning,” a novel task is described but _no_ examples are given (for instance, “Write a poem about cats in the style of Hemingway” or “’Equiantonyms’ are pairs of words that are opposite of each other and have the same number of letters. What are some ‘equiantonyms’?”).

> “The most important parts of AGI have already been achieved by the current generation of advanced AI large language models.” 

“General intelligence” must be thought of in terms of a multidimensional scorecard, not a single yes/no proposition. Nonetheless, there is a meaningful discontinuity between narrow and general intelligence: Narrowly intelligent systems typically perform a single or predetermined set of tasks, for which they are explicitly trained. Even multitask learning yields only narrow intelligence because the models still operate within the confines of tasks envisioned by the engineers. Indeed, much of the hard engineering work involved in developing narrow AI amounts to curating and labeling task-specific datasets.

By contrast, frontier language models can perform competently at pretty much any information task that can be done by humans, can be posed and answered using natural language, and has quantifiable performance. 

The ability to do in-context learning is an especially meaningful meta-task for general AI. In-context learning extends the range of tasks from anything observed in the training corpus to anything that can be described, which is a big upgrade. A general AI model can perform tasks the designers never envisioned.

So: Why the reluctance to acknowledge AGI?

Frontier models have achieved a significant level of general intelligence, according to the everyday meanings of those two words. And yet most commenters have been reluctant to say so for, it seems to us, four main reasons:

  1. A healthy skepticism about metrics for AGI
  2. An ideological commitment to alternative AI theories or techniques
  3. A devotion to human (or biological) exceptionalism
  4. A concern about the economic implications of AGI

## **Metrics**

There is a great deal of disagreement on where the threshold to AGI lies. Some people try to avoid the term altogether; Mustafa Suleyman has suggested a switch to “Artificial Capable Intelligence,” which he proposes be measured by a “modern Turing Test”: the ability to quickly make a million dollars online (from an initial $100,000 investment). AI systems able to directly generate wealth will certainly have an effect on the world, though equating “capable” with “capitalist” seems dubious.

There is good reason to be skeptical of some of the metrics. When a human passes a well-constructed law, business or medical exam, we assume the human is not only competent at the specific questions on the exam, but also at a range of related questions and tasks — not to mention the broad competencies that humans possess in general. But when a frontier model is trained to pass such an exam, the training is often narrowly tuned to the exact types of questions on the test. Today’s frontier models are of course not fully qualified to be lawyers or doctors, even though they can pass those qualifying exams. As Goodhart’s law states: “When a measure becomes a target, it ceases to be a good measure.” Better tests are needed, and there is much ongoing work, such as Stanford’s test suite HELM (Holistic Evaluation of Language Models).

It is also important not to confuse linguistic fluency with intelligence. Previous generations of chatbots such as Mitsuku (now known as Kuki) could occasionally fool human judges by abruptly changing the subject and echoing a coherent passage of text. Current frontier models generate responses on the fly rather than relying on canned text, and they are better at sticking to the subject. But they still benefit from a human’s natural assumption that a fluent, grammatical response most likely comes from an intelligent entity. We call this the “Chauncey Gardiner effect,” after the hero in “Being There” — Chauncey is taken very seriously solely because he _looks_ like someone who should be taken seriously.

The researchers Rylan Schaeffer, Brando Miranda and Sanmi Koyejo have pointed out another issue with common AI performance metrics: They are nonlinear. Consider a test consisting of a series of arithmetic problems with five-digit numbers. Small models will answer all these problems wrong, but as the size of the model is scaled up, there will be a critical threshold after which the model will get most of the problems right. This has led commenters to say that arithmetic skill is an emergent property in frontier models of sufficient size. But if instead the test included arithmetic problems with one- to four-digit numbers as well, and if partial credit were given for getting some of the digits correct, then we would see that performance increases gradually as the model size increases; there is no sharp threshold.

This finding casts doubt on the idea that super-intelligent abilities and properties, possibly including consciousness, could suddenly and mysteriously “emerge,” a fear among some citizens and policymakers. (Sometimes, the same narrative is used to “explain” why humans are intelligent while the other great apes are supposedly not; in reality, this discontinuity may be equally illusory.) Better metrics reveal that general intelligence is continuous: “More is more,” as opposed to “more is different.”

> “Frontier language models can perform competently at pretty much any information task that can be done by humans, can be posed and answered using natural language, and has quantifiable performance.” 

## **Alternative Theories**

The prehistory of AGI includes many competing theories of intelligence, some of which succeeded in narrower domains. Computer science itself, which is based on programming languages with precisely defined formal grammars, was in the beginning closely allied with “Good Old-Fashioned AI” (GOFAI). The GOFAI credo, drawing from a line going back at least to Gottfried Wilhelm Leibniz, the 17th-century German mathematician, is exemplified by Allen Newell and Herbert Simon’s “physical symbol system hypothesis,” which holds that intelligence can be expressed in terms of a calculus wherein symbols represent ideas and thinking consists of symbol manipulation according to the rules of logic. 

At first, natural languages like English appear to be such systems, with symbols like the words “chair” and “red” representing ideas like “chair-ness” and “red-ness.” Symbolic systems allow statements to be made — “The chair is red” — and logical inferences to follow: “If the chair is red then the chair is not blue.”

While this seems reasonable, systems built with this approach were always brittle and limited in the capabilities and generality they could achieve. There are two main problems: First, terms like “blue,” “red” and “chair” are only approximately defined, and the implications of these ambiguities become more serious as the complexity of the tasks being performed with them grows.

Second, there are very few logical inferences that are universally valid; a chair may be blue _and_ red. More fundamentally, a great deal of thinking is not reducible to the manipulation of logical propositions. That’s why, for decades, concerted efforts to bring together computer programming and linguistics failed to produce anything resembling AGI.

However, some researchers with ideological commitments to symbolic systems or linguistics have continued to insist that their particular theory is a requirement for general intelligence, and that neural nets or, more broadly, machine learning, are theoretically incapable of general intelligence — especially if they are trained purely on language. These critics have been increasingly vocal in the wake of ChatGPT.

> “For decades, concerted efforts to bring together computer programming and linguistics failed to produce anything resembling AGI.” 

For example, Noam Chomsky, widely regarded as the father of modern linguistics, wrote of large language models: “We know from the science of linguistics and the philosophy of knowledge that they differ profoundly from how humans reason and use language. These differences place significant limitations on what these programs can do, encoding them with ineradicable defects.”

Gary Marcus, a cognitive scientist and critic of contemporary AI, says that frontier models “are learning how to sound and seem human. But they have no actual idea what they are saying or doing.” Marcus allows that neural networks may be _part_ of a solution to AGI, but believes that “to build a robust, knowledge-driven approach to AI, we must have the machinery of symbol manipulation in our toolkit.” Marcus (and many others) have focused on finding gaps in the capabilities of frontier models, especially large language models, and often claim that they reflect fundamental flaws in the approach. 

Read Noema in print.

Without explicit symbols, according to these critics, a merely learned, “statistical” approach cannot produce true understanding. Relatedly, they claim that without symbolic concepts, no logical reasoning can occur, and that “real” intelligence requires such reasoning.

Setting aside the question of whether intelligence is always reliant on symbols and logic, there are reasons to question this claim about the inadequacy of neural nets and machine learning, because neural nets are so powerful at doing anything a computer can do. For example:

  * Discrete or symbolic representations can readily be learned by neural networks and emerge naturally during training.
  * Advanced neural net models can apply sophisticated statistical techniques to data, allowing them to make near-optimal predictions from the given data. The models learn how to apply these techniques and to choose the best technique for a given problem, without being explicitly told. 
  * Stacking several neural nets together in the right way yields a model that can perform the same calculations as any given computer program.
  * Given example inputs and outputs of any function that can be computed by any computer, a neural net can learn to approximate that function. (Here “approximate” means that, in theory, the neural net can exceed any level of accuracy — 99.9% correct for example — that you care to state.)

For each criticism, we should ask whether it is prescriptive or empirical. A prescriptive criticism would argue: “In order to be considered as AGI, a system not only has to pass this test, it also has to be constructed in this way.” We would push back against prescriptive criticisms on the grounds that the test itself should be sufficient — and if it is not, the test should be amended.

An empirical criticism, on the other hand, would argue: “I don’t think you can make AI work that way — I think it would be better to do it another way.” Such criticism can help set research directions, but the proof is in the pudding. If a system can pass a well-constructed test, it automatically defeats the criticism.

In recent years, a great many tests have been devised for cognitive tasks associated with “intelligence,” “knowledge,” “common sense” and “reasoning.” These include novel questions that can’t be answered through memorization of training data but require generalization — the same proof of understanding we require of students when we test their understanding or reasoning using questions they haven’t encountered during study. Sophisticated tests can introduce novel concepts or tasks, probing a test-taker’s cognitive flexibility: the ability to learn and apply new ideas on the fly. (This is the essence of in-context learning.)

As AI critics work to devise new tests on which current models still perform poorly, they are doing useful work — although given the increasing speed with which newer, larger models are surmounting these hurdles, it might be wise to hold off for a few weeks before (once again) rushing to claim that AI is “hype.”

## **Human (Or Biological) Exceptionalism**

Insofar as skeptics remain unmoved by metrics, they may be unwilling to accept _any_ empirical evidence of AGI. Such reluctance can be driven by a desire to maintain something special about the human spirit, just as humanity has been reluctant to accept that the Earth is not the center of the universe and that Homo sapiens are not the pinnacle of a “great chain of being.” It’s true that there is something special about humanity, and we should celebrate that, but we should not conflate it with general intelligence.

It is sometimes argued that anything that could count as an AGI must be conscious, have agency, experience subjective perceptions or feel feelings. One line of reasoning goes like this: A simple tool, such as a screwdriver, clearly has a purpose (to drive screws), but it cannot be said to have agency of its own; rather, any agency clearly belongs to either the toolmaker or tool user. The screwdriver itself is “just a tool.” The same reasoning applies to an AI system trained to perform a specific task, such as optical character recognition or speech synthesis.

A system with artificial general intelligence, though, is harder to classify as a mere tool. The skills of a frontier model exceed those imagined by its programmers or users. Furthermore, since LLMs can be prompted to perform arbitrary tasks using language, can generate new prompts with language and indeed can prompt themselves (“chain of thought prompting”) the issue of whether and when a frontier model has “agency” requires more careful consideration.

Consider the many actions Suleyman’s “artificial capable intelligence” might carry out in order to make a million dollars online:

It might research the web to look at what’s trending, finding what’s hot and what’s not on Amazon Marketplace; generate a range of images and blueprints of possible products; send them to a drop-ship manufacturer it found on Alibaba; email back and forth to refine the requirements and agree on the contract; design a seller’s listing; and continually update marketing materials and product designs based on buyer feedback.

As Suleyman notes, frontier models are already capable of doing all of these things in principle, and models that can reliably plan and carry out the whole operation are likely imminent. Such an AI no longer seems much like a screwdriver.

> “It’s true that there is something special about humanity, and we should celebrate that, but we should not conflate it with general intelligence.” 

Now that there are systems that can perform arbitrary general intelligence tasks, the claim that exhibiting agency amounts to being conscious seems problematic — it would mean that either frontier models _are_ conscious or that agency doesn’t necessarily entail consciousness after all.

We have no idea how to measure, verify or falsify the presence of consciousness in an intelligent system. We could just ask it, but we may or may not believe its response. In fact, “just asking” appears to be something of a Rorschach test: Believers in AI sentience will accept a positive response, while nonbelievers will claim that any affirmative response is either mere “parroting” or that current AI systems are “philosophical zombies,” capable of behaving like us but lacking any phenomenal consciousness or experience “on the inside.” Worse, the Rorschach test applies to LLMs themselves: They may answer either way depending on how they are tuned or prompted. (ChatGPT and Bard are both trained to respond that they are not conscious.)

Hinging as it does on unverifiable beliefs (both human and AI), the consciousness or sentience debate isn’t currently resolvable. Some researchers have proposed measures of consciousness, but these are either based on unfalsifiable theories or rely on correlates specific to our own brains, and are thus either prescriptive or can’t assess consciousness in a system that doesn’t share our biological inheritance.

To claim a priori that nonbiological systems simply _can’t_ be intelligent or conscious (because they are “just algorithms,” for example) seems arbitrary, rooted in untestable spiritual beliefs. Similarly, the idea that feeling pain (for example) requires nociceptors may allow us to hazard informed guesses about the experience of pain among our close biological relatives, but it’s not clear how such an idea could be applied to other neural architectures or kinds of intelligence.

“What is it like to be a bat?” Thomas Nagel famously wondered in 1974. We don’t know, and don’t know if we _could_ know, what being a bat is like — or what being an AI is like. But we do have a growing wealth of tests assessing many dimensions of intelligence.

While the quest to seek more general and rigorous characterizations of consciousness or sentience may be worthwhile, no such characterization would alter measured competence at any task. It isn’t clear, then, how such concerns could meaningfully figure into a definition of AGI.

It would be wiser to separate “intelligence” from “consciousness” and “sentience.”

## **Economic Implications**

Arguments about intelligence and agency readily shade into questions about rights, status, power and class relations — in short, political economy. Since the Industrial Revolution, tasks deemed “rote” or “repetitive” have often been performed by low-paid workers, while programming — in the beginning considered “women’s work” — rose in intellectual and financial status only when it became male-dominated in the 1970s. Yet ironically, while playing chess and solving problems in integral calculus turn out to be easy even for GOFAI, manual labor remains a major challenge even for today’s most sophisticated AIs.

What would the public reaction have been had AGI somehow been achieved “on schedule,” when a group of researchers convened at Dartmouth over the summer of 1956 to figure out “how to make machines use language, form abstractions and concepts, solve kinds of problems now reserved for humans, and improve themselves”? At the time, most Americans were optimistic about technological progress. The “Great Compression” was underway, an era in which the economic gains achieved by rapidly advancing technology were redistributed broadly (albeit certainly not equitably, especially with regard to race and gender). Despite the looming threat of the Cold War, for the majority of people, the future looked brighter than the past.

Today, that redistributive pump has been thrown into reverse: The poor are getting poorer and the rich are getting richer (especially in the Global North). When AI is characterized as “neither artificial nor intelligent,” but merely a repackaging of human intelligence, it is hard not to read this critique through the lens of economic threat and insecurity.

In conflating debates about what AGI _should_ be with what it _is_ , we violate David Hume’s injunction to do our best to separate “is” from “ought” questions. This is unfortunate, as the much-needed “ought” debates are best carried out honestly. 

AGI promises to generate great value in the years ahead, yet it also poses significant risks. The natural questions we should be asking in 2023 include: “Who benefits?” “Who is harmed?” “How can we maximize benefits and minimize harms?” and “How can we do this fairly and equitably?” These are pressing questions that should be discussed directly instead of denying the reality of AGI.

Enjoy the read? Subscribe to get the best of Noema.

###### More From Noema Magazine

Essay  Technology & the Human

The Nature Of Free Will In The Age Of AI 

Albert Yuan

Essay  Technology & the Human

The Tantalizing Possibility Of Locating Consciousness In The Brain 

Daniel Freeman

Essay  Future of Democracy

How To Give Everyday People A Say In AI Governance 

Hélène Landemore
