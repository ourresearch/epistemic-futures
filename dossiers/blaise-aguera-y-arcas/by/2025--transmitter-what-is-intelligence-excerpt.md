---
title: "'What Is Intelligence?': An excerpt"
person: blaise-aguera-y-arcas
section: by
type: book-chapter
year: 2025
date: 2025-09-23
venue: "The Transmitter"
authors: "Blaise Agüera y Arcas"
source_url: https://www.thetransmitter.org/learning/what-is-intelligence-an-excerpt/
retrieved: 2026-08-13
content: excerpt
notes: "OpenAlex W4414401055. Book excerpt published by The Transmitter; the complete free online edition of the book is at by/2025--book-what-is-intelligence.md."
---

# 'What Is Intelligence?': An excerpt

## Excerpt

**Critical thinking:** Temporal difference is an example of a sophisticated learning algorithm that organisms developed as evolution propelled them to build more complicated brains. 

Courtesy of MIT Press 

Books / Learning 

Add us as a Preferred Source on Google  Set us as a Preferred Source to see _The Transmitter_ more prominently in your Google Search results. 

#  ‘What Is Intelligence?’: An excerpt 

In his new book, published today, Blaise Agüera y Arcas examines the fundamental aspects of intelligence in biological and artificial systems. In this excerpt from Chapter 4, he examines temporal difference, a reinforcement learning algorithm. 

By  Blaise Agüera y Arcas

23 September 2025 | 9 min read 

comments

https://doi.org/10.53053/AACC4729 https://doi.org/10.53053/AACC4729 - opens a new tab Cite this article 

**Critical thinking:** Temporal difference is an example of a sophisticated learning algorithm that organisms developed as evolution propelled them to build more complicated brains. 

Courtesy of MIT Press 

**Bootstrapping**

Animals with simple distributed nerve nets, like _Hydra_ , show little evidence of learning in any form that a behavioral experimentalist would recognize, though every cell does continually regulate its own biophysics to ensure that it remains responsive to whatever signals it receives—a form of local learning. This is consistent with the idea that these earliest nerve nets serve only secondarily for sensing the environment, having first evolved to help muscles coordinate coherent movement.

Rudimentary behavioral learning arises the moment anything like a brain appears, because, at this point, neurons in the head must begin jointly adapting to changing conditions in the outside world. Every connection or potential connection between one neuron and another offers a parameter—a degree of coupling—that can be modulated to suit the circumstances, even if the “wiring diagram” is genetically preprogrammed or random. To see why, let’s take the neuron’s point of view, and imagine that it is simply trying to do the same thing any living thing does: predict and bring about its own continued existence. Some aspects of this prediction will certainly have been built in by evolution. For example, if dopamine is a proxy for food nearby, the neuron will try to predict (and thereby bring about) the presence of dopamine, because prolonged absence of dopamine implies that the whole animal will starve—bringing an end to this one neuron, along with all of its cellular clones.

Even a humble cell has plenty of needs and wants beyond food, but without food, there is no future.

Therefore, if the neuron is not itself dopamine-emitting, but its activity somehow influences dopamine in the future, it will try to activate at times that increase future dopamine. Aside from neuromodulators like dopamine, the neuron’s inputs come either from other neurons or, if it’s a sensory neuron, from an external source, such as light or taste. It can activate spontaneously, or in response to any combination of these inputs, depending on its internal parameters and degree of coupling with neighboring neurons. Presumably, at least one of its goals thus becomes fiddling with its parameters such that, when the neuron fires, future dopamine is maximized. I’ve just described a basic reinforcement learning algorithm, where dopamine is the reward signal. As brains became more complicated, though, they began to build more sophisticated models of future reward, and, accordingly, in vertebrates, dopamine appears to have been repurposed to power something approximating a more sophisticated reinforcement learning algorithm: “temporal difference” or “TD” learning. TD learning works by continually predicting expected reward and updating this predictive model based on actual reward. The method was invented (or, arguably, discovered) by Richard Sutton while he was still a grad student working toward his Ph.D. in psychology at UMass Amherst in the 1980s. Sutton aimed to turn existing mathematical models of Pavlovian conditioning into a machine learning algorithm. The problem was, as he put it, that of “learning to predict, that is, of using past experience with an incompletely known system to predict its future behavior.” In standard reinforcement learning, such predictions are goal-directed. The point is to reap a reward—like getting food or winning a board game. However, the “credit assignment problem” makes this difficult: A long chain of actions and observations might lead to the ultimate reward, but creating a direct association between action and reward can only enable an agent to learn the last step in this chain.

As Sutton put it, “whereas conventional prediction-learning methods assign credit by means of the difference between predicted and actual outcomes, [TD learning] methods assign credit by means of the difference between temporally successive predictions.” By using the change in estimated future reward as a learning signal, it becomes possible to say whether a given action is good (hence should be reinforced) or bad (hence should be penalized) before the game is lost or won, or the food is eaten.

This may sound circular, because if we already had an accurate model of the expected reward for every action, we wouldn’t need to learn anything further; why not just take the action with the highest expected reward? As in many statistical algorithms, though, by separating the problem into alternating steps based on distinct models, it’s possible for these models to take turns improving each other, an approach known as “bootstrapping”—after that old saying about the impossibility of lifting oneself up by one’s own bootstraps. Here, though, it is possible. In the TD learning context the two models are often described as the “actor” and the “critic”; in modern implementations, the actor’s model is called a “policy function” and the critic’s model, for estimating expected reward, is the “value function.” These functions are usually implemented using neural nets. The critic learns by comparing its predictions with actual rewards, which are obtained by performing the moves dictated by the actor, while the actor improves by learning how to perform moves that maximize expected reward according to the critic.

A TD learning system eventually figures out how to perform well, even if both the actor and critic are initially entirely naive, making random decisions—provided that the problem isn’t too hard, and that random moves occasionally produce a reward. Hence an experiment in the 1990s applying TD learning to backgammon worked beautifully, although applying the same method to complex games failed, at least initially.

**Beyond reward**

Around the same time, at the University of Fribourg’s Institute of Physiology, Wolfram Schultz’s lab had been studying the relationship between motor function and Parkinson’s disease, which was known to compromise movement via dopamine depletion. In a typical experiment, Schultz and colleagues would record from single dopamine-releasing neurons in the brains of macaques while they performed simple motor tasks, which they needed to learn via Pavlovian conditioning. A thirsty monkey, for instance, might need to learn which of two levers to pull in response to a flashing light to get a sip of juice. The researchers made the following observations:

  1. Dopamine neurons normally spike at a moderate background rate.
  2. When the monkeys first stumbled upon an action producing the sugary drink, the spiking rate of these dopamine neurons rose.
  3. Once the monkeys figured out the association between the visual cue and the reward, extra dopamine was no longer released when the treat came, but was released earlier, when the visual cue was presented. This coincided with the monkeys licking their lips, akin to the salivation of Pavlov’s dogs.
  4. If, following the visual cue, the treat was withheld, then activity of the dopamine neurons subsequently decreased—that is, they went quiet relative to their background rate.

When Peter Dayan and Read Montague, then postdocs in Terry Sejnowski’s lab at the Salk Institute in San Diego, saw these results from Schultz’s group, they realized that dopamine was acting precisely

like a temporal-difference learning signal. This is the signal whereby the brain’s “critic” tells the “actor”: Please reinforce whatever behavior you’re doing now, because I predict it will lead to a futurereward. Long sequences of actions that ultimately lead to a reward can be learned this way, with the TD learning signal shifting earlier and earlier in the sequence as the learning progresses.

The repurposing of dopamine from a simple reward signal to something like a temporal-difference reinforcement-learning signal might follow naturally from the growth of brain structures both “upstream” and “downstream” of the dopamine-releasing neurons. Remember that even among the earliest bilaterians, dopamine no longer represents food, but nearby food. In this sense, dopamine is already a prediction of food, not a food reward in itself. Predicting dopamine is thus a prediction of a prediction of food.

A predictive symbiosis between neural areas upstream and downstream of dopamine will therefore result in the upstream areas being able to make higher-order predictions (hence longer-range forecasts), thus acting as an increasingly sophisticated critic or value function. Meanwhile, the downstream parts become an increasingly sophisticated actor, or policy function, smart enough to learn how to make better moves using these longer-range forecasts.

This may help to explain the approximate fit between the TD learning paradigm and at least one major role played by dopamine in the brains of vertebrates. Like many primal feelings, “something good is within reach” is a simple, useful signal that a worm can infer directly from smell, and a larger-brained animal like us can infer through a much more complex cognitive process. That is a useful signal for many parts of the brain, since they are all invested in producing good outcomes for the organism as a whole; hence dopamine signaling has been conserved for hundreds of millions of years, and its role has remained, if not the same, at least recognizable throughout those eons.

Still, we should be careful not to interpret these experimental findings about dopamine as proof that the brain implements TD learning as Sutton formulated. That can’t be the whole story. For one, we have ample evidence that humans, and likely many other animals, are even more powerful learners than the TD algorithm is. Advanced board games we have no trouble playing, for instance, are beyond the reach of TD learning. Additionally, as I hinted earlier, recent experiments suggest that dopamine encodes information well beyond that of a TD error signal.

None of this should surprise us. Brain regions that symbiotically predict their environment and each other are not restricted to implementing simple learning algorithms, or communicating using cleanly definable mathematical variables, any more than human emotional expression is limited to a single dimension or natural language is restricted to logical grammar. Like every other approach to machine learning described in this book, TD learning is an elegant conceptual simplification that sheds light, but does not illuminate every corner. It is neither a complete nor an exact representation of what the brain does.

_Excerpted from “_ _What Is Intelligence? Lessons from AI About Evolution, Computing, and Minds_ _,”_ _by Blaise Agüera y Arcas. Reprinted with permission from the MIT Press. Copyright 2025._

tags: 

Learning,  Books,  Dopamine,  Monkeys,  Motor behavior,  Nonhuman primates,  Reward prediction error,  Reward system

##  Explore more from _The Transmitter_

Computational neuroscience 

comments

###  The 1,000 neuron challenge 

By  Tom Stafford

5 January 2026 | 8 min read 

Theoretical neuroscience 

comments

###  Not playing around: Why neuroscience needs toy models 

By  Marcus Ghosh

22 December 2025 | 6 min read 

Artificial intelligence 

comments

###  Seeing the world as animals do: How to leverage generative AI for ecological neuroscience 

By  Shahab Bakhtiari

8 December 2025 | 8 min read 

Cite this article:

Copy DOI 

Share this article:

Facebook - opens a new tab  Linkedin - opens a new tab  X twitter - opens a new tab  Reddit - opens a new tab  Threads - opens a new tab  Mail - opens a new tab  Copy - opens a new tab
