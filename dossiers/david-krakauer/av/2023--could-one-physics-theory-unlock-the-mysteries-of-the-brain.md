---
title: "Could One Physics Theory Unlock the Mysteries of the Brain?"
person: david-krakauer
section: by
type: talk-transcript
year: 2023
venue: "YouTube (Quanta)"
source_url: https://www.youtube.com/watch?v=hjGFp7lMi9A
retrieved: 2026-08-15
content: full-text
transcription:
  method: asr
  asr_model: elevenlabs-scribe_v2
  diarized: true
  speaker_labels: inferred   # ASR diarization + LLM naming (claude-sonnet-4-6); not ground truth
  duration_min: 13
notes: "PROVENANCE: machine-transcribed from AV via ElevenLabs Scribe v2 (diarized) + LLM speaker-naming pass. Speaker labels are inferred, not authoritative. Layer-2 (mildly lossy) per charter, not camera-raw."
---

# Could One Physics Theory Unlock the Mysteries of the Brain?

*Speakers (inferred):* speaker_0=David Krakauer, speaker_1=Unknown, speaker_2=Unknown, speaker_3=Narrator, speaker_4=Unknown, speaker_5=Unknown

## Transcript
**David Krakauer** [00:00]: [instrumental music] Critical phenomena arise at transitions. The idea is that when a system's just at this edge of order and disorder, interesting complex dynamics can arise.

**Unknown** [00:15]: As a physicist, critical phenomena is extremely appealing because it appears in many phenomena, from the evolution of the universe to the properties of superconductors.

**Unknown** [00:27]: Flocks of starlings, networks of brain cells, tectonic plates, social interactions among humans, all these types of things. Any time I can see one equation apply to lots and lots of different things, I think that's beautiful. It's economical, it's insightful. Which raises a really profound question, which is why? Why are so many things in nature operating near the critical point?

**Narrator** [00:53]: When physical systems go through phase transitions, such as when water transitions from a liquid into a vapor because of a change in temperature, the system moves through what's known as the critical point, a fleeting moment of transition from one phase to another, characterized by exotic emergent properties that have long intrigued scientists.

**Unknown** [01:12]: Critical systems have this property of changing phase, and that small changes in some critical environmental variable leads to drastic changes, almost discontinuous changes, in the function. And it's that kind of observation that leads us to believe that the study of critical transitions is valuable.

**Narrator** [01:37]: Critical dynamics are best demonstrated in a simplified system known as the Ising model, which visualizes the individual iron atoms making up a magnet, with arrows to indicate the direction of each atom's spin.

**Unknown** [01:49]: You can imagine a lattice, and on this lattice you get all these little spins that can point either up or down. And when this lattice is really cold, what will happen is all the spins will line up together. So nearest neighbor interactions will cause them all to point in the same direction, and if this is a piece of iron, uh, you know, bing, it would stick on your refrigerator 'cause all the, the bar magnets sum in the same direction. But now if you heat this up, if you took a little BIC lighter and you put it under it, what would happen is these little spins would start moving, and they'd start going in different directions, and then they would eventually cancel. Some of them would point up, and half of them would point down, and it would fall off of your refrigerator. So you get a phase transition from it being very ordered to being totally disordered.

**Narrator** [02:31]: As it passes from order to disorder, the system moves through the critical point, and clusters of similarly oriented spins form throughout the lattice. If you were to measure the sizes of these clusters at various scales, the data would reveal what's known as a power law, where dynamics at one scale mirror the dynamics at other scales. This phenomenon is also known as scale invariance.

**Unknown** [02:55]: Scale invariance is another way of saying that there is self-similarity or fractality, if you want. These kind of properties are spectacular because indeed it's like everything simplifies at the critical point.

**Narrator** [03:08]: When a system reaches the critical point, it displays a telltale peak in what's known as the correlation length, an indication of how sensitive the system as a whole is to the activity of any one of its components.

**Unknown** [03:20]: What happens is the system behaves in ways that allow fluctuations to occur over the scale of the entire system. If it was too cold, you'd have no correlation 'cause they're just pointing, they're not moving. And when it's too hot, they're moving a lot, but they're not correlated. So only at that sweet spot right in the middle do you have interactions at all scales. Now what that means is something very weird. That means that the distance over which these spins might interact is technically infinite. I could take a spin over here and flip it, and there's some non-zero probability that another spin very, very far away would flip also as a result of it.

**Narrator** [04:00]: In 1987, the physicist Per Bak wondered if many different types of complex systems in the natural world might self-organize around critical points. To illustrate his theory of self-organized criticality, Bak used the familiar example of a sand pile. As the pile gains mass, friction can no longer hold the grains of sand in place, and a single grain added to the pile will trigger an outsized effect, sending avalanches cascading down its sides.

**Unknown** [04:32]: And it turns out that if you look at the distribution of avalanche sizes, the big ones, the small ones, the intermediate ones, they follow power laws.

**Unknown** [04:40]: And so Per Bak's idea was that, hey, here's a natural system that self-organizes to the critical point. You don't need to tune it there. You don't need to get just the right control temperature. It will evolve into that state. And so when he came out with this concept of self-organized criticality, he was claiming that many natural systems fall into that category, like earthquakes, like stock market crashes, like piles of sand. Now, he was a pioneer, and it was amazing that he did that. Uh, and it inspired many people from other areas to enter into the field of criticality and to take a look at this concept and apply it more generally. And, and I would say basically it's had huge amounts of traction. However, there have been people who have been quite skeptical.

**Narrator** [05:28]: Bak's equations only account for one grain of sand hitting the pile at a time. In nature, things are more complicated, and researchers have found it difficult to simulate criticality.

**Unknown** [05:39]: And this is a general problem of mathematical models, just to be always aware of, which is at what point have you overextended that simple abstraction and applied it in a way that's inadmissible? And so SOC is just one mechanism for tuning to critical points. It's a very interesting one, but perhaps it will turn out to be a rare one.

**Narrator** [06:04]: Despite the criticism, Bak's work inspired interest in criticality throughout the 1990s and into the early 2000s when neuroscientists began to probe a new question: whether brains might exhibit self-organized criticality.

**Unknown** [06:18]: Per Bak's work opened up the concept that criticality could apply to many different things. And that made me think, oh, we've got lots of neurons that are interacting in this network, so hey, why not? So we just started to apply that framework to the data.

**David Krakauer** [06:34]: The idea that the brain is at a transition point, for example, at criticality, at the transition between order and chaos, and it had been around for a while. I think the real avalanche of criticality research was triggered by John Beggs and Dietmar Plenz in 2003.

**Unknown** [06:48]: We isolated, in this case, the gray matter, the cortex, as a piece of tissue when it was young. We grew it on a microelectrode array in a dish. We let it grow for about four weeks. And we measured the activity, how these cells would interact with each other. And we found that they start to form groups like just these cascades that were predicted by the Per Bak sandpile model.

**Unknown** [07:15]: And so I started plotting avalanche size distributions, and sure enough, they were power law.

**Unknown** [07:21]: It was the first paper that claimed that the brain was probably functioning at a critical point.

**Narrator** [07:30]: The question for scientists then became why? Why might functioning at a critical point be helpful for brains?

**Unknown** [07:37]: Can you show that operating near the critical point actually increases behavioral performance? And when you're not near the critical point, it doesn't. So why would being at the critical point be to your evolutionary advantage? So let's say you're, I don't know, at the side of a river and there's a bunch of reeds and they're blowing in the wind. But you notice that, hey, this is different from yesterday. I think there's a tiger back there. So you want to be very sensitive to inputs. The system is most susceptible to slight changes in inputs when it's near the critical point. It has these large fluctuations that can take off.

**Narrator** [08:13]: According to the critical brain hypothesis, when the network is right at criticality, it's perfectly balanced between two extreme states: super-criticality, in which networks of neurons display the highly ordered runaway excitation seen in epilepsy; and sub-criticality, in which signals fail to trigger larger cascades and stall out, as seen in comatose states. By hovering near the critical point, the theory goes, networks of neurons would be optimized for information transmission. Just like in the Ising model, tiny inputs could result in big complex behaviors in the network. Proving that such a measurement of optimal brain activity exists would give researchers a new scale to interpret just about everything brains do.

**Unknown** [08:57]: When we first got our results back from the 2003 paper, I was just enamored with the idea of criticality. I was in love with it. I'd go to bed thinking, oh, it's optimal information transmission. We get just the right exponents. It's all cool. And then over time, people started to question this in various ways.

**Narrator** [09:13]: Just as with Per Bak's sandpile model, scientists began to question whether the physics of criticality could neatly apply to such a chaotic biological system with so many variables interacting all at once. In simpler systems like the Ising model, a single variable like temperature can be adjusted to bring the network right to the critical point. But in complex biological systems, the prospect of tuning to the exact point of criticality would be much more difficult.

**Unknown** [09:39]: The brain is constantly receiving inputs from outside that could blow it off of the critical point. So for those reasons alone, it can't really be exactly critical. Then what is it? One of the options of many on the menu about how the brain is actually operating is that it's slightly sub-critical, that it doesn't really get to the critical point because that might be dangerous. Another plausible idea is that it's quasi-critical. And what that means is that it gets as close to the critical point as it can, but then there's this activity that's basically going to push it away from being right at the critical point.

**Narrator** [10:19]: As research continues to reveal tantalizing signatures of criticality, what was once a fringe theory has begun to attract more mainstream attention in the field, with researchers now hunting for what kinds of mechanisms might be responsible for tuning brains towards the critical point.

**Unknown** [10:35]: The big question that is unanswered so far is what is the homeostatic mechanism bringing back the brain to this quasi-criticality region? That's a big question. It's a big open question. That's a million-dollar question.

**Unknown** [10:59]: Neuroscience has been and continues to be very hesitant and reluctant to agree on a theoretical idea of the kind that criticality offers. Most neuroscientists are very hard-nosed empiricists. They don't believe that there is an overarching theory that explains most or, God forbid, all of what the brain is doing in one handy concept such as critical state. I personally think that what does not play well with neuroscientists is if criticality is portrayed as the answer to everything. And I think that is overselling it. And yet, I have no doubt believing that a system like the brain almost requires to be in a critical state for it to function well or optimally even.

**Unknown** [11:50]: There might be one equation that explains how the whole thing works. That's the idealized dream. We may never ever get there, but the hope is that there might be some general principles that really explain how intelligence functions in this world that we live in.

**Unknown** [12:07]: The field wasn't there 20 years ago when we had just one idea, a sandpile model or an Ising model that would guide us. We are way beyond that. And we are at the point now where the technological advance in neuroscience to record individual spiking activity for many, many thousands of neurons. These are the precision tools that we need in order to test new ideas of criticality. How is the collective coming together to produce outcomes that are way beyond what an individual can do? And I think this is how our society is organized. Our brain, our body is organized. And any understanding of the enrichness that we gain when we operate as a collective, I think is just beautiful scientific insight.

