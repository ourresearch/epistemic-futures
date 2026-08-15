---
title: "David Krakauer: Emergence and Scaling of AGI"
person: david-krakauer
section: by
type: talk-transcript
year: 2026
venue: "YouTube"
source_url: https://www.youtube.com/watch?v=jXa8dHzgV8U
retrieved: 2026-08-14
content: full-text
transcription:
  method: asr
  asr_model: elevenlabs-scribe_v2
  diarized: true
  speaker_labels: inferred   # ASR diarization + LLM naming (claude-sonnet-4-6); not ground truth
  duration_min: 50
notes: "PROVENANCE: machine-transcribed from AV via ElevenLabs Scribe v2 (diarized) + LLM speaker-naming pass. Speaker labels are inferred, not authoritative. Layer-2 (mildly lossy) per charter, not camera-raw."
---

# David Krakauer: Emergence and Scaling of AGI

*Speakers (inferred):* speaker_0=David Krakauer, speaker_1=Interviewer

## Transcript
**David Krakauer** [00:00]: The brain is an organ, like a muscle. If I outsource all of my thinking to something or someone else, it will atrophy just as your muscles do. There's nothing confusing about that. It's just a fact of physiology. So I'm David Krakauer, and I work on the evolution of intelligence and stupidity on planet Earth. Science is a humanistic endeavor. The purpose of science in the universe is to make the universe intelligible to us, not to control it, not to predict it, and not to exploit it. Science is no different from poetry, is that we're trying to make sense of the world, trying to give it meaning in relation to our own existence. Superintelligence is only interesting to the extent that it makes me more intelligent, not to the extent it makes me more stupid or more servile or more dependent. Oh, good.

**Interviewer** [01:05]: Oh, has the camera just died? You're saved.

**David Krakauer** [01:07]: That was actually-- That was sympathy. That was sympathy.

**Interviewer** [01:10]: [laughs] Amazing. Well, um, I, I think the first paper of yours I, I, uh, read was a couple of years ago with Melanie, and we interviewed Melanie, you know, about, about the, the debate of understanding in language models I think it was called. And, um, at the time, there was this fervor, you know, the, the, this, this, um, hype around, you know, the Sparks of AGI paper, for example. And, and they had early access to GPT-4 without RLHF, and they were saying, "Isn't it amazing that we have these emergent capabilities?"

**David Krakauer** [01:43]: Yes. Yes. [laughs] Uh, no comment. Um, right. Well, there's just this whole question of, as you know, I mean, what emergence is, what intelligence is, um, and we can talk about it all. My particular interest is, is the evolution of intelligence, and which I consider extraordinarily varied. So I consider bacteria intelligent, uh, as you probably know. So, um, and my basic... I guess one way of framing a lot of this is that for me, intelligence manifests most clearly when you can do a lot with very little in terms of input.

**Interviewer** [02:29]: Mm.

**David Krakauer** [02:30]: And I'm less and less impressed when you manifest so-called intelligent behavior when you have more and more and more information at your disposal.

**Interviewer** [02:41]: Yes.

**David Krakauer** [02:42]: And unfortunately, the way that AI has evolved is in the direction of confusing being very knowledgeable with very intelligent, and I think that's, in some sense, encapsulates my critique.

**Interviewer** [02:58]: Yes. Uh, you said in your talk yesterday that all of the reasonable definitions of intelligence, if, if anything, try to marginalize away the contribution of, of knowledge. It's about, you know, adapting to novelty, ad-adaptivity in general. Your evolutionary perspective is very interesting. You were, you were kind of pointing to this yesterday when you were saying about, um, the, the history preserving and, and accumulating information, but preserving that history is very important, not only phylogenetically but also ontogenically.

**David Krakauer** [03:26]: Yeah.

**Interviewer** [03:27]: Uh, can, can you explain what you mean by that?

**David Krakauer** [03:28]: Yeah. So I mean, it's a really interesting question, right? I mean, one of the big confusions in the intelligence world is whether we're allowed to call ingenious adaptations intelligent. Um, that is capabilities, tr- adaptations. Is that an intelligent thing, or is that just what evolution gives you? And there are people out there who would say, "No, that's not intelligent," because intelligent isn't, isn't a capability. It's the ability to acquire capability. You know, the capacity to acquire capacity, as Woodrow puts it, and Francois Chollet and others like that have adopted that perspective. So the question is: where does that come from?

**Interviewer** [04:15]: Hmm.

**David Krakauer** [04:16]: And you can actually derive this mathematically. Um, in the 1970s, uh, a very prominent theoretical chemist who won the Nobel Prize actually for high-speed chemistry, Manfred Eigen, started developing a series of theories that were finally formalized in the '80s, um, called Quasispecies Theory. And to cut a very long story short, what that theory gives us is a fundamental bound on the rate at which information can be acquired in any evolutionary process. And it turns out that the fundamental speed limit is established by the generation time. So it's essentially one bit per selective death. That even has a name. It's called the Muller principle. So the way to think about it is you have lots of variants, each of which has a different hypothesis about the world. Selection kills all the ones that have the wrong hypothesis and keeps the one that has the right one. And it turns out that you can only maintain one bit because you don't know which bit would be responsible if it was many. So it's one bit per genome per generation. Now, if you're a large multicellular organism, all of the adaptive information exists at frequencies that are higher than the generational frequency. So what do you do? So you have to build a system that's extragenomic.

**Interviewer** [05:57]: Yes.

**David Krakauer** [05:58]: And we call them epigenomes, or we call them brains. And these are systems that can acquire high-frequency information That goes beyond the selective dynamic. So that's the basic idea, right? And so you can actually make a qualitative distinction, and that boundary is called the, the error threshold, um, where you have to acquire an inferential organ mechanism to extract high-frequency information from the world. For some people, that's intelligent. I don't share that view 'cause it's somewhat arbitrary, but it's, but it's principled.

**Interviewer** [06:36]: And y-you said yesterday that, uh, I mean, of course, you know, the nervous system is, is an example of one of these things, but you said culture is evolution at light speed.

**David Krakauer** [06:45]: Yeah.

**Interviewer** [06:45]: What do you mean by that?

**David Krakauer** [06:46]: Well, it turns out... [chuckles] Okay, so I don't know how technical [chuckles] we can get here.

**Interviewer** [06:51]: Very technical.

**David Krakauer** [06:51]: Okay, we can get technical.

**Interviewer** [06:52]: Yeah.

**David Krakauer** [06:52]: So, so one way to think about this, right, is that imagine a genome as being a point in a configuration space. It's called sequence space, and as you evolve, you move around in this space. You can think of it as a graph where adjacent nodes are connected through mutation, which tends to be local, not always. Um, okay. So the Eigen theory tells us how much information it can be preserved at a certain rate of mutation or what's the fastest speed you can move adaptively in sequence space and not lose everything you've acquired about the past. Okay? And this is, this is the error threshold. If you're in a position to take the information that you've acquired in the past and store it, refrigerate it, quite literally, put it in a library, put it in a book-

**Interviewer** [07:55]: Mm.

**David Krakauer** [07:56]: Now you can move on that graph much more quickly because you're not corrupting the information that you have hitherto accumulated. And so culture actually has no upper bound because as long as I store, like save to my hard drive, save to my library, the information that I've acquired up to, to now, I can just randomly produce variants at any rate. As long as one of those is good, I add it to my library. So culture actually breaks evolutionary light speed, um, and is a qualitatively different process of evolution to organic evolution because of that.

**Interviewer** [08:31]: And David, you're at pains to distinguish capabilities from intelligence, so why is culture or a library, um, a form of storing... I, I don't know whether you would call it intelligence.

**David Krakauer** [08:43]: Well, okay, again, I don't think so. I wouldn't. Um, I make a big distinction between knowledge and intelligence.

**Interviewer** [08:49]: Yes.

**David Krakauer** [08:49]: And, and we talked about this, which is that smart people don't need a lot of knowledge to solve a problem. Not so smart people do, and that's our experience in life. You know, as you go to a friend who's swotted up on all of the solutions to the problems, and you ask them, and they answer, you're not as impressed as that friend of yours who spent the last week, you know, at a pub or, or, or on a hike, not in the library. Those are the people who impress us more, and I think w-we've lost track of that actually. I think that, um, as I like to put it, um, when it comes to intelligence, less is more and not more is more.

**Interviewer** [09:29]: Yes, indeed. Uh, the-- Yesterday you, you said that, yeah, so intelligence is, is doing more with less, and you actually said stupidity is, is doing less with more, which was, which was very interesting.

**David Krakauer** [09:38]: Well, no, again, I mean, so, okay, [chuckles] so the whole, um... So let me give you the background to that. So at SFI, we're very interested in this idea of emergence, and Phil Anderson in 1972 wrote a very famous paper called "More is Different." And Phil was reacting to high-energy physics.

**Interviewer** [10:03]: Hmm.

**David Krakauer** [10:04]: High-energy physics deals with very small things where the symmetric laws of physics produce a corresponding syvmet-symmetry in the configuration of states in the physical system. But as you make things larger, and he gives the example of NH3 and PH3, ammonia and, and phosphine. The underlying laws of physics and protein folding are symmetric, but when you have a very large structure, it gets stuck in a potential well, and so you break the symmetry. So it doesn't matter if the law is symmetric. It's like saying I have a ball. It rolls down a hill, but rolls into a very deep valley. It gets stuck, and, uh, there's an energy funnel, and it doesn't matter that the law is symmetric because now the only thing that's going to tell you what state you observe is the initial condition, where you started in the landscape. And his point, and this is called a broken symmetry, and Phil's point was as you get larger and larger, hence more, in, in, in this particular instance, in terms of the, the atomic mass of the molecule, um, you're more and more likely to have to use an additional parameter to tell you where you are. And the consequence of that is that if you're going to have a theory now, which isn't just a description, a list of initial conditions, in other words, um, you have to take averages. You have to do core screening.

**Interviewer** [11:40]: Yes.

**David Krakauer** [11:41]: And that's the foundational principle of complex systems that in order to go from a very non-parsimonious microscopic description to a parsimonious macroscopic one, you have to take averages in a clever way. And that's the essence, by the way, of emergence.

**Interviewer** [11:59]: Yes, indeed. And, uh, the, we, we should talk about your paper. So, um, recently released, "Large Language Models and Emergence: A Complex Systems Perspective." And as you were just alluding to, emergence is more is different. And in, in a minute we'll talk about scaling, criticali- criticality, compression, novel bases, and generalization-

**David Krakauer** [12:17]: Yes

**Interviewer** [12:17]: ... as being the principles of emergence.

**David Krakauer** [12:18]: Yeah. Yeah.

**Interviewer** [12:18]: But just rewinding a tiny bit, many folks in the LLM literature, famously Jason Wei... I was speaking with, um, Daniel Hendricks last night, and he actually told me that he, he said it first even before Jason. But, you know. Um, and, and they have this rather cartoonish version of, of emergence, which is something along the lines of when there is a sharp discontinuity in capabilities, we can say that... And they gave examples, didn't they, of, you know, three-digit multiplication and so on.

**David Krakauer** [12:43]: Yeah.

**Interviewer** [12:44]: And 'cause you have these scaling laws, and then you see these, these divergent appearances of-

**David Krakauer** [12:47]: Yeah

**Interviewer** [12:47]: ... of capabilities. You're having none of that, David.

**David Krakauer** [12:50]: None of that. [laughs] Well, the joke there, there's a few things to say. Exactly, you just put it very well and so, and you don't need to repeat it. But yeah, so this three-digit addi- addition that goes from being, I can't remember the percentages, right? But let's say that they're under 50% when you've got 100 billion parameters, and they go to 80%, you've got 175 billion or something like that. And you think, "Well, okay, I can do three-digit addition very effectively on an HP 35 calculator with a 1K ROM." But that's an order of a billion times smaller memory footprint. So you think, "Okay." So you can engineer a solution into a tiny little memory footprint very efficiently using approximations that we are familiar with. Um, or you have to train it with all the data in the world at considerable expense. It does lots of other things in addition to... Right? That's the interesting point, to three-digit addition, and you call it emergent. I would simply call that really shit programming.

**Interviewer** [13:53]: [laughs]

**David Krakauer** [13:54]: Right? In other words, I think that is the right way to talk about it. And if you're doing really shit programming with natural language, you need loads of it to achieve the goal of interest. The fact that it's discontinuous is neither here nor there. I think that's almost an irrelevance, and it's never really had much to do with the emergence debate, except, uh, as an analogy to what are called first order phase transitions, which are sort of where the, essentially the, the first derivative of the free energy of the system in relation to some, let's say, uh, control parameter, let's say temperature, uh, is infinite. And so there are these technical definitions in relation to theory of phase transitions, but this is nothing like that, and we can talk about that. Because a phase transition is characterized by a demonstrable change in the internal organization of a system.

**Interviewer** [14:47]: Mm.

**David Krakauer** [14:48]: That's really what it's about. It's not about the discontinuity. That's, that's superficial.

**Interviewer** [14:53]: Yes. Yes. So, so broadly speaking, you think it's about this coarse graining where there is an entirely novel description using novel bases to... You gave the example in the paper actually of, you know, um, a microscopic description could be of, of how molecules interact with each other. A macroscopic version would be something like Navier-Stokes, so fl- fluid-

**David Krakauer** [15:10]: Exactly

**Interviewer** [15:10]: ... fluid dynamics.

**David Krakauer** [15:11]: Exactly.

**Interviewer** [15:11]: And this is an entirely kind of, um, aggregate description of the system which only works at a certain scale.

**David Krakauer** [15:19]: Right. And notice that's completely non-discontinuous. Uh, you know, how, what... When does something cease being the atomic theory of gases or H2O molecules? And when are you really at the hydrodynamic limit where you can write down Newton's laws of compressible or incompressible fluids, Navier-Stokes equations? And, well, it, there isn't, [laughs] there isn't this magic discontinuity. It's just a, it's a limiting process. And, and yet, to this idea of intelligence, which is, you know, about doing more with less, um, now all of a sudden, you don't have to track all those molecules anymore. You can just look at the average densities.

**Interviewer** [16:00]: Yes.

**David Krakauer** [16:00]: And, um, so the key point here of emergence for many of us is there's a sufficient change in the internal organization of the system that you can get this more parsimonious description of its behavior, and which screens off, that sort of turn of art, um, the contributions of the molecular degrees of freedom. You don't need to track them. They won't help you. They're surplus to the prediction that you're trying to make.

**Interviewer** [16:28]: Yes, indeed. So for you, David, when we saw, when we would see a break with scaling laws, so right now we are memorizing everything, capabilities and scaling laws are commensurate. There have been studies that Daniel Hendricks last night said it's something like 96% correlated. You would expect to see a, a deviation. So when we can have intelligence without scaling, that would actually imply that some kind of coarse graining has been established.

**David Krakauer** [16:55]: Yeah. That's interesting. I think, yeah, 'cause sometimes it's called the breaking of scaling. Um, so scaling laws, um, are not evidence of emergence.

**Interviewer** [17:06]: Yes.

**David Krakauer** [17:06]: Okay? So the most famous example that we work on at SFI, my colleagues Geoff West and, and Chris Kempes and others, um, is allometric scaling. It's good that we're in St. Andrews, right? Because D'Arcy Thompson, the great Scottish mathematical biologist, essentially invented the field in his beautiful book, "On Growth and Form," that he published in 1917. I went to see his collection this morning here. So that's an aside. But this theory tells you that at all scales, you'll have a fixed relationship between mass and metabolic rate, okay? Um, and it comes out of an optimization principle that applies at all scales, which is very interesting. Um, there's nothing emergent about it. Uh, emergent means there's a change in the organization which requires a new scaling law.

**Interviewer** [17:54]: Yes.

**David Krakauer** [17:54]: And, um, and again, there's quite a lot to say about this, but minimally, right, to start investigating a potential case of emergence You would want to see that the scaling law is broken. Then secondarily, you'd have to go inside the system and ask why. And this is the big, I think, objection that Melanie, John, and I have to emergence claims, is they're based only on the external manifestation, um, of a task and not on the corresponding internal microscopic dynamics, which you want to somehow map onto the macroscopic observable. That's the essence of emergence, the micro to macro map. This is just macro.

**Interviewer** [18:43]: Yes, indeed. And a, um, a massive fan of, of Melanie, probably her biggest fan actually.

**David Krakauer** [18:48]: Yeah.

**Interviewer** [18:48]: And, um, sh- she did this, uh, copycat work-

**David Krakauer** [18:50]: Yeah

**Interviewer** [18:50]: ... for her, uh, her PhD thesis.

**David Krakauer** [18:52]: Yeah.

**Interviewer** [18:52]: And because I suppose the, the question is, what does coarse graining look like for language models? What would it look like? Analogy is, is, is a wonderful, um, candidate. And more broadly, I think what you're pointing to is that these models learn fractured, entangled representations. They're microscopic representations, and what we would expect to happen if they were emergent would be that they would learn these, um, factored, unified representations which correlate with the world, which carve the world up by the joints. And perhaps you would extend that and say, actually respect the, the, the, the phylogeny, things like symmetry. You know, they respect the way that the world works, which means that they would be able to take creative, intuitive steps because they know how they got there.

**David Krakauer** [19:35]: Yeah. I think that's a very good point. I think that's exactly right. I think that, um... I mean, it's a deep question, right? But I think there's a sense in which our nervous system and our bodies respect certain fundamental constraints in the physical world, is what you're alluding to. And, um, you know, and this has been borrowed, of course, by neural networks in things like convolutional neural nets.

**Interviewer** [20:00]: Yeah.

**David Krakauer** [20:00]: 'Cause then you're saying there is a structure in the world which there tends to be some covariance in visual scenes, and convolutional networks capture that covariance very naturally. So that's an example of using a stronger prior which respects something you know about reality. There is a little bit, as you know very well, in the neural net community, a bit of an allergy against building priors into models 'cause you wanna do it all-

**Interviewer** [20:26]: Yeah

**David Krakauer** [20:26]: ... kind of inductively, which is a little bit of a confusion, it seems to me, given that the entire structure derives from 1943 McCulloch and Pitts, which was a nervous system inspired concept. So why not use a bit of world inspiration too?

**Interviewer** [20:43]: Yes, indeed. Uh, you mentioned yesterday the, The Road to Reality by Penrose, and, uh, funnily enough, I interviewed Michael Bronstein, who is, you know, one of the, the founders of this geometric deep learning idea. And it is basically Platonism, right? So it's the, you know, let, let's imbue all of these symmetries because we think that the generating function of the world is constrained by these symmetries, and it's an abstraction which doesn't leave out any detail. Are, are you amenable to that idea?

**David Krakauer** [21:09]: I'm not. I mean, I'm, I'm, I'm not because it's so anti-complexity. I mean, I might be to his. I, I'm, to be honest, I'm not familiar with it. Um, sometimes the way I like to put this is, you know, in 1918, the great mathematician physicist Emmy Noether-

**Interviewer** [21:22]: Yes

**David Krakauer** [21:23]: ... um-

**Interviewer** [21:23]: Conservation laws, yeah

**David Krakauer** [21:24]: ... right, one of those sort of hidden figures by virtue of sexism in society, um, publishes a very, very important piece of work where she shows the relationship between the symmetries of the action functional. Yes, the symmetries of the, of the Lagrangian, um, the, the principle of least action, that captures the principle of least action, and showed, right, that, um, shifting the time or space coordinate corresponded to the conservation of a particular physical observable. Change time and you conserve energy. Change space and you conserve momentum. And Darwin is in some sense anti-Noether. The Origin of Species says, "Change time, everything's different. Change space, everything's different." [chuckles] And this gets to the Anderson broken symmetry idea, that it's unlike physics because it's not symmetry dominated, and consequently, various observables are not conserved. So I actually think the power of symmetry simply ceased to be the important organizing principle once life came into existence, and certainly intelligence. So I'm not sure what he's claiming. Um, that's different, by the way, to saying that there are symmetries in the world that perception exploits.

**Interviewer** [22:56]: Mm.

**David Krakauer** [22:56]: That's clearly true.

**Interviewer** [22:57]: Mm.

**David Krakauer** [22:57]: And I don't, again, I don't know if that's the-

**Interviewer** [23:00]: How, how convergent do you think evolution is if we ran it in a, a parallel universe a thousand times? You know, do, do, do you think there's this kind of real ontological coupling, or is it quite divergent?

**David Krakauer** [23:12]: Ooh, that's a good question. Depends who you ask.

**Interviewer** [23:15]: Right. What, what would you, what would you-

**David Krakauer** [23:16]: Simon Conway Morris, he'd say, "Very." Um, if you ask Gould, "Very not," [chuckles] or, "Not very." I think it sort of depends on the resolution of your measuring device because at a very coarse grain level, allometric scaling theory says everything scales in the same way. Doesn't matter how many times you run it, the, the scaling of me- of essentially energy to mass is dependent entirely on the dimensions of space. The three-quarter scaling law is three dimensions of space over four dimensions of space, where the extra dimension is fractal. That has nothing to do with life. I mean, it has something to do with life, of course, but, uh, it doesn't depend on a contingent history of life.

**Interviewer** [24:03]: Yeah.

**David Krakauer** [24:04]: So at that level of granularity, if that's all you could see, all you could measure, right, the average mass of an, of an organism, there would be no variation, right? Very little. Uh, but if you zoom in- Uh, then of course you see more and more variation, which is a, if you like, a kind of fossil record of its unique history.

**Interviewer** [24:26]: Mm.

**David Krakauer** [24:27]: And biologists do tend to zoom in. Psychologists do tend to zoom in, and I think that's almost dispositional. Physicists like the granular, the very non-granular, averaged. Biologists like the very natural historical. It's not surprising that those two, uh, traditions come to different answers.

**Interviewer** [24:47]: Yes, indeed. Could, could you explain what you mean by this distinction of knowledge out versus knowledge in with emergence?

**David Krakauer** [24:54]: Yes. Okay. So first of all, let's just establish that with emergence, we mean that there is a description of a system that's more parsimonious, that a given level of observation does not benefit from more microscopic detail. We gave the example of fluids, right?

**Interviewer** [25:18]: Yes.

**David Krakauer** [25:18]: And there are many. So how does it come about? How does emergence come about? And I mean, there's infinite number of examples, but physicists tend to be interested in how many identical particles all subject to the same context or environmental inputs experience emergence. I gave that example. Add molecules, change the temperature. That's just one dimension, the average energy. When it comes to evolution or learning, there isn't one input that every molecule is experiencing. You're not just changing the temperature uniformly. Um, everyone is experiencing a different unique parameterization. So the theory of, um, emergence was developed mainly in the physical domain, where you had large numbers of identical things with a global signal.

**Interviewer** [26:25]: Mm.

**David Krakauer** [26:26]: And now c- emergence claims are being made to, made for large systems of non-identical, all experiencing a unique signal. So there's already this question of whether or not we can even talk about emergence, and we don't typically, by the way, because we talk about evolution, we talk about learning, development, and engineering. No one would say an iPhone is emergent, 'cause you say somewhere there's a plan that tells you exactly what to do with every component.

**Interviewer** [26:55]: Yes.

**David Krakauer** [26:56]: Just as there's a plan that tells you what to do with every cell in development. Now, it's a complex distributed plan, part genome, part environment, but nevertheless, there's an abstraction which you could talk about it in that way. Um, so that's p- so knowledge in are systems where essentially you have to, to get the structure of interest, the passion of interest, you have to parameterize each component individually, more or less. Knowledge out is the example of physics, where you say, "God, all I did was change the temperature and I got a solid from a fluid. I got a plasma. What happened? [chuckles] This is a completely different state of matter, and I, all I did is change one thing." And so that, that's the, the, the big distinction. So the, the challenge, I think, for biology and machine learning is how to talk about emergence when you've sort of violated the prime directive, which is you've been allowed to have local modification of each component.

**Interviewer** [27:57]: Yes.

**David Krakauer** [27:57]: Um, and I think you can, but that's the essential distinction between knowledge in and knowledge out.

**Interviewer** [28:04]: One thing that fascinates me about emergence is, um, we'll get onto agency. I, I think of that as a, as a form of causal shielding or causal disconnectedness, certainly from the perspective of, of an observer.

**David Krakauer** [28:15]: Mm.

**Interviewer** [28:15]: But there are philosophers like, um, uh, George Ellis, I believe, who said that, um, causation is kind of shielded between the levels and causation happens between the levels. But I mean, to you, what, what is the relationship between causality and emergence?

**David Krakauer** [28:28]: Ooh, that's interesting. I mean, I think in a way, one way to say it, right, everything I've said sort of trivially, is that you do have a new coarse-grained set of effective mechanisms that you can talk about as being genuinely causal in the interventional sense of Pearl, not in the fundamental Newtonian sense.

**Interviewer** [28:52]: Mm.

**David Krakauer** [28:53]: And, and these are complementary conceptions of causality, right? Um, but I think I would say it would be completely reasonable to restate the emergence claim as a more parsimonious causal mechanism.

**Interviewer** [29:07]: Yes.

**David Krakauer** [29:08]: Right? That there, there is an aggregate observable that conforms to your preferred neo-Pearl [chuckles] framework that sort of works with the do operator and the appropriate treatment of conditional distributions. And, um, so I think that is appropriate to, to think of it as a new form of causality.

**Interviewer** [29:30]: Fascinating. And, and on this notion of, of agency, how would you define it in relation to things like intelligence? I mean, just me j- just very personally, there's, there's the, the autonomy and the, and the causality thing, but there's also this intentionality and directedness thing. So it's, it's not about just autonomy in one direction, it's the ability to set your own direction. And, um, yeah, just h- how, what does, what does that mean to you?

**David Krakauer** [29:55]: Yeah. So I've actually been developing a, a framework for thinking about this. And the way I think about it is in, in, in three different, more sophisticated conceptions. The first is the conception of action from physics.

**Interviewer** [30:14]: Yes.

**David Krakauer** [30:14]: Balls roll downhill.

**Interviewer** [30:16]: Yes.

**David Krakauer** [30:17]: You wouldn't call that agentic. Some people probably do, unfortunately, but okay. That's the simplest. We have a perfectly good Newtonian Lagrangian Hamiltonian theory. We don't need to use these words, agentic, for that. Some people [chuckles] okay. Then we have this Darwinian concept, adaptation. Well, adaptation's a bit more than a ball rolling down a hill because it says that the ball gets better at rolling down the hill because it has an internal record of its past efforts. And the, the general term that Kant gave to that, and John Holland gave to that, and Marrigo Mann gave to that, is a schema. Okay? Um, it's a, it's a-- You can think of it as a simple lookup table that says, "If I find myself in this situation, I should do that. If I find myself in that situation, I should do that." Bit different from the moon, a bit different from a ball. And then the most sophisticated to me would be the agentic, and that adds something to the adaptive, which is a policy. It says, "This is what I want to do." Notice adaptation could just be reactive. You could say, "If I find myself here, then do that." Policy actually says, "I would like to do this into the future." So I think there's a very nice spectrum that takes us from a fundamental conception in theoretical physics through to a conception in evolutionary theory, through to a conception that seems to be appropriate for a psychological or cognitive system. And, and they're adding, if you like, complication to the internal schema to accomplish that particular objective.

**Interviewer** [31:49]: And does agency entail this kind of emerging coarse graining that we were speaking about before? I mean, it certainly seems to. We look in the natural world and, you know, we, we, we see planets, we see things, but then there are these agents that have a s- a level of sophistication which is much greater than that, and would that be an example of this kind of coarse graining you're talking about?

**David Krakauer** [32:09]: I think for us to understand them, um, the answer is definitely yes. There's a secondary question of what we sometimes call endogenous coarse graining, and that's where it gets more complicated philosophically because when we reason, let's say I think I'm reasoning with language, but I'm still recruiting millions of neurons to do it. And so at the level, if I was a solitary agent, it would be very difficult to know whether I'm really doing endogenous coarse graining. The data for endogenous coarse graining comes from communication. So if I tell you, "You know, Tim, this is what it means to integrate by parts," or something, "This is what a Fourier transform does," and you look at it and you say, "Oh, thank you, I know how to do it now," now I've actually communicated to you a very low-dimensional symbolic scheme which you can then kind of use to program, if you like, your neurons. And at that level, I think no doubt, 'cause there we've actually done coarse graining quite demonstrably, and it's actionable on what your neurons are doing. So I think this is Wittgenstein's private language problem. If all you get to do is observe a system in isolation, I would never know. But I think in this social collective intelligence setting, I think it's, it goes without, uh, any shadow of doubt that there's evidence for emergence.

**Interviewer** [33:42]: Can we go over to exbodiment?

**David Krakauer** [33:44]: Yeah.

**Interviewer** [33:44]: And, and by the way, I'm, I'm, I'm a, a big externalist myself, but I hadn't come across the term exbodiment-

**David Krakauer** [33:49]: Yeah

**Interviewer** [33:50]: ... which, which is, has a very specific meaning.

**David Krakauer** [33:51]: Yeah. So I, I was very interested in this idea of embodiment, which we're all familiar with, which is that we can outsource computation to constraint. We can use the reduced degrees of freedom of a limb to reduce the complications of our policy. Okay, that's, everyone knows that. But what about an object in the external world? What about a pencil? What about a fork? What about an astrolabe? You know, what about a Rubik's Cube? And there it's not embodiment, it's something else. Uh, and the something else there requires contributions from culture, right? In other words, no one person built the chessboard. Lots of people did together, and they collectively discovered a very effective representation of a certain kind. That's one part of it. So let's make a distinction between the exbodied, which is collectively arrived at w- versus embodiment, which is your characteristic. The second point about exbodiment is, that interests me, is how we have to go via an external material vehicle to get back into the brain. And the example I like, and there are many examples, let's give some, like, simple ones. A map. So we collectively make a map of this city of St. Andrews, but you can give that to me and I can memorize it, and I can burn that map. And as we discovered this morning, I'm not very good at navigating [chuckles] so, um, and I'll be able to navigate freely without a physical object. And this feedback between the collective construction of an exbodied artifact and its internalization into the individual mind, I call the exbodiment helix. And it just gets better and better and better, right? Because now I have a map, I can explore more of the space. I can contribute to that collective script which you can then internalize into your mind. This is a very under-theorized, uh, process, and we've been working on it very carefully in the last several years in relation to problem-solving artifacts like the abacus, like the Soma Cube, like the Rubik's Cube. How does that dynamic work? What does the physical object do that your brain cannot? And we can talk about that, but we can quantify that quite exactly.

**Interviewer** [36:23]: David, your institute has done some fascinating research on collective intelligence in, in general, and I know it, it sounds like a contrived question to ask, but what is the relationship between... Or, or maybe what is the boundary of the individual mind to the collective?

**David Krakauer** [36:36]: I think that's a really hard question to answer. Um, so I've worked on these mathematical formalisms for finding boundaries. Many people are interested in, in them. I, I, I call it the informational theory of the individual. There are theories of Markov blankets that you're familiar with. So there are many of in- interested in this question of where do you draw it, the boundary, and I think the reality is you can draw many. And, um, so let me just give a example from biology and then come back. So what's an individual ant? You know. Well, all the workers are clones, so you say maybe that's not really the individual, that's a constituent of, of the individual. That's like a cell in you. But there is a level of obser- of, of observable resolution where you could say a cell is individual. It is dividing semi-autonomously. So a lot of it has to do, I think, again, back to that really critical conception of scale of observation. Um, the formalism that we started developing was one that was scale-dependent. It says, "At a given scale of observation, the key characteristic of the bounded object is that it contains sufficient information to propagate itself into the future." It- You don't have to look elsewhere. Um, and clearly that's true for a cell over a given number of divisions at the resolution of the cell.

**Interviewer** [38:10]: Yeah.

**David Krakauer** [38:10]: So it's individual. It's not entirely true for the body 'cause, of course, that doesn't really propagate into the future. It's true for your genome, which does partially propagate into the future. It's true for ideas which are partially carried by many minds. So if you ask me to propagate the work of Einstein into the future, you'd get a fairly incomplete jigsaw puzzle. [chuckles] But if you took a group of people, it would probably be quite complete. So it really depends, again, on the complication, the size of the object, the artifact, the concept, how many informational contributions you require, and, and the theory tries to calculate that-

**Interviewer** [39:01]: Hmm

**David Krakauer** [39:01]: ... um, over a particular timescale and a particular space scale. So mind is so fascinating because, um, it would depend what you said. If it was, you know, my preference for a certain flavor of ice cream, you don't need many, you don't need much collective intelligence for that. But when it comes to things that we actually care about, like, you know, affine or projective geometry, uh, unless you have a Coxeter who can do it on his own, you need a bunch of us to do it together. So even that's interesting, right? 'Cause there's heterogeneity in, in this individuality with respect to what can reliably propagate information into the future. So it's, it's very difficult.

**Interviewer** [39:45]: Yes. You reminded me, uh, my friend, uh, Ken Stanley, um, I'm sure you're familiar with, with his work.

**David Krakauer** [39:51]: Oh, he visited us. He, he was on sabbatical at SFI.

**Interviewer** [39:53]: He's my hero.

**David Krakauer** [39:54]: Okay. [chuckles]

**Interviewer** [39:54]: Uh, we've just had him on the show, and, um, he was talking about the need for evolvability. So certainly when we have representations, it's not, not about, you know, where you were, it's how you got there, but also where you can go from there.

**David Krakauer** [40:04]: Yeah.

**Interviewer** [40:05]: And, and agency has a little bit of a shared principle in the sense of, you know, it's about controlling or modifying the environment to, um, meet your goals and so on. And, and, and here you're, you're talking about this general principle of information propagation into the future.

**David Krakauer** [40:20]: Yeah, no doubt, and, and that's a really interesting point because you're not only propagating the variation, the information in the, in the Shannon sense, but the variational operator-

**Interviewer** [40:32]: Yes

**David Krakauer** [40:33]: ... right? Uh, which could be mutation. It could be different mechanisms of imagination or novelty generation.

**Interviewer** [40:42]: Yes.

**David Krakauer** [40:42]: And, uh, so that's actually a very good point that even within genetics, right, you don't only propagate the genes, but the mechanism of genetic segregation.

**Interviewer** [40:53]: So David, um, you, you've looked at various forms of, of sort of, you know, representation and, and computation, organic, inorganic, cultural, et- etc. Can you tell me about that?

**David Krakauer** [41:03]: Yeah. I'm-- One way to think about this, and it gets to our opening conversation about the limits of evolution and why brains and minds had to evolve to capture information that couldn't be captured by natural selection. Um, another way to say that, right, is that we've transitioned from a more mortal style of doing information processing-

**Interviewer** [41:29]: Hmm

**David Krakauer** [41:30]: ... bacteria and so on, which are very dependent on life and death for the information to be captured and stored, versus us, where in some sense much of the information is stored in culture itself, so it has more of an immortal flavor. Um, and if you think of us as analogous to cells in a body that turn over quickly, we turn over relatively quickly-

**Interviewer** [41:57]: Hmm

**David Krakauer** [41:57]: ... relative to the edifices of knowledge that we construct. So I actually think you could argue that evolution itself as a prog- as a process has moved from more mortal styles of computing, and I mean information processing in the organic setting, um, to more immortal-like things which we're familiar with with software and hardware. And so-- And you might argue that technologies, and I have argued this actually- Why do they exist? And the way to think about this is we have technologies for everything that we're bad at. We don't play tennis well with our hand. People do, [chuckles] but it's not quite as exciting as watching Roger Federer or what have you. We don't calculate well, hence calculators and the abacus. We walk well, right? And we sing well. And so these are things that we don't really have technologies for. They're also harder to build. And there's a sense in which computers and software and, and archives more generally, bodies of knowledge, represent an inevitable contribution that complements all those domains in which human reasoning is deficient.

**Interviewer** [43:22]: I mean, that, that, that's, that's one way of thinking about it. I mean, my, my biggest fear is not that, you know, AI and ChatGPT and all of this will degrade our thinking and creativity, it's that it already has.

**David Krakauer** [43:34]: Well, that's another point, right? That-- Okay, so that's again, an interest of mine. So I just want you to make that point that these, that these technologies exist for a reason-

**Interviewer** [43:45]: Yes

**David Krakauer** [43:45]: ... and they're, and they're there to, in some sense, complement, um, deficits. I'm not saying they're more intelligent than us at all. [chuckles] That's quite the opposite. Um, I think they're intelligent the way a calculator is, right?

**Interviewer** [43:58]: Yes. Yes.

**David Krakauer** [43:58]: So they're compensating for things that we don't do well. There's this other question which is really important, and you can actually generalize the Eigen theory, and this is a little bit maybe technical again, which is that you can show that in the same way that we outsource to the body and we outsource to artifacts as a means of increasing fidelity and reducing energy requirements, we will outsource everything, right, if we can. And, uh, and we see evidence of this all the time. And the, the most obvious example is the difference between outsourcing to maps versus outsourcing to GPS, where if you have guaranteed a system that's more effective at navigating than you, there is no reason for you to acquire that skill. And I think we're already seeing evidence, and there's lots of studies, actually, some recently came out suggesting that human cognition is attenuating by virtue of outsourcing it to calculators. And I actually-- It's one of the reasons why I'm not very optimistic about technology, because up until now, you could argue it was n-net positive, right? No one's gonna argue with a sextant, right? Or with a slide rule or something. Think, "Yeah, that's great, you know. I couldn't do it otherwise." But I think you now can argue with the idea or be a proponent of the idea that the long-term implication of technology is the significant diminution and dilution of what it means to be a human. Um, I now receive on a daily basis tens of emails written as collaborations between humans and LLMs, and it's 100% rubbish. And I think that the ratio of the human to the LLM is just gonna keep going down, and eventually everyone will sound the same. So it's not to suggest that the tool can't be useful, but this evolutionary drive to increase fidelity and reduce energy is so strong in us that we will eventually outsource ourselves. And, and I think-- I don't know why people are excited about the technology if that's the likely omega point of evolution of the species.

**Interviewer** [46:40]: Yes. Could, could we expand more on this diminution of, you know, agency and creativity and, and thinking? I mean, in universities, will we need to almost create separated areas for the students to actually think and read books and, and do work with-without AI? A-another thing is, uh, I, I'm, you know, we, we, we don't believe in this super intelligence idea, but if super intelligence were invented, because the folks in Sili- in Silicon Valley, they, they are saying that, um, don't worry about labor anymore, the old way of, of, you know, doing useful economic tasks. Now we, we just need to buy lots of GPUs-

**David Krakauer** [47:20]: Yeah

**Interviewer** [47:20]: ... and we need to s- you know, sort of defend the GPUs because people might want to bomb the GPUs because they're the source of all, of all power. And, and, and that's very much their view.

**David Krakauer** [47:28]: Yeah.

**Interviewer** [47:28]: Would that change if we did have super intelligence?

**David Krakauer** [47:31]: There is a world where I would delegate the gym to you. I'm not going. There's no point in me going 'cause you can go for me. I'm not gonna get up and walk around 'cause you can get up and walk around for me. The consequence of that would be, as you know, [chuckles] significant trauma to our physiological and mental wellbeing. Everyone understands that. The brain is an organ, like a muscle. If I outsource all of my thinking to something or someone else, it will atrophy just as your muscles do. There's nothing confusing about that. [chuckles] It's just a fact of physiology. And now you might say, "Just as long as I have people who can carry me everywhere whenever I need to be carried, then it doesn't matter that I lose my legs," you know. [chuckles] And, um, okay. So there is a sense in which we become, you know, the male deep sea anglerfish that's just a testicle, uh, that's reduced to its absolute minimum for retaining individuality in the sense of propagating information forward in time. Um, it's not a future that I consider desirable. So super intelligence is only interesting to the extent that it makes me more intelligent, not to the extent it makes me more stupid or more servile or more dependent. And, uh, it just seems to me so glaringly obvious a remark that I don't understand why people are falling for the moonshine.

**Interviewer** [49:13]: David, it's been such an honor having you on the show. Thank you so much for joining us.

**David Krakauer** [49:16]: Thank you. It's been fun. So I'm David Krakauer. I'm a faculty member at the Santa Fe Institute. I'm also the president of the Santa Fe Institute, and I work on the evolution of intelligence and stupidity on planet Earth. [laughs]

**Interviewer** [49:34]: Incredible. David, this has been great. Thank you so much.

**David Krakauer** [49:37]: All right. I'm done.

**Interviewer** [49:39]: One, one of my favorite ever interviews.

**David Krakauer** [49:40]: [laughs] None of your community are gonna... What the fuck's he talking about? [laughs]

**Interviewer** [49:44]: No, no, no. You, you'll have a lot of fans.

**David Krakauer** [49:47]: Yeah, yeah, yeah.

