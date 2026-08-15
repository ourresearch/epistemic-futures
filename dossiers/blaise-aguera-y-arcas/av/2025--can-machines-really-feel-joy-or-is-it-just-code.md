---
title: "Can Machines Really Feel Joy or Is It Just Code?"
person: blaise-aguera-y-arcas
section: by
type: talk-transcript
year: 2025
venue: ""
source_url: https://youtu.be/h2egH3mVNRY
retrieved: 2026-08-15
content: full-text
transcription:
  method: asr
  asr_model: elevenlabs-scribe_v2
  diarized: true
  speaker_labels: inferred   # ASR diarization + LLM naming (claude-sonnet-4-6); not ground truth
  duration_min: 72
notes: "PROVENANCE: machine-transcribed from AV via ElevenLabs Scribe v2 (diarized) + LLM speaker-naming pass. Speaker labels are inferred, not authoritative. Layer-2 (mildly lossy) per charter, not camera-raw."
---

# Can Machines Really Feel Joy or Is It Just Code?

*Speakers (inferred):* speaker_0=Interviewer, speaker_1=Blaise Aguera Y Arcas, speaker_2=Panelist

## Transcript
**Interviewer** [00:00]: Einstein called it his happiest thought, the realization that someone in free fall feels no gravitational force. It wasn't just brilliant physics, it was a moment of pure human joy, connecting a mathematical insight with a bodily experience. But here's what keeps me up at night. Could a computer ever have that feeling? My guest today, Blaise Aguera y Arcas from Google's AI research team, thinks the answer might surprise you. He argues that our brains, despite their biological complexity, are fundamentally computational machines. Every sensation, every emotion, every moment of wonder gets encoded as electrical spikes between neurons. If that's true, then the boundary between human consciousness and artificial intelligence might be more porous than we ever imagined. We're not just talking about AI that can solve equations or write poetry. We're asking whether machines can experience the universe the way we do, with curiosity and delight, and maybe with something approaching happiness. The implications stretch from the nature of consciousness itself to how we should design the AI systems that are increasingly defining our future. Now let's go deep into the impossible. I want to start with a question that I have never gotten a satisfactory answer to. No pressure, but it relates to what Einstein said was his happiest thought, which was that an observer who is freely falling like this, I'm gonna do an expensive demonstration, that observer would feel no gravitational force, and he called that his happiest thought. The reason I like that question is because it seems to exemplify what humans are, at least now, for now, maybe only now, capable of uniquely doing, which is embodiment and happiness linked together. He called it the thought that gave him the greatest happiness in his life, and he was not a man of few words, nor was he a man of few accomplishments. Can a computer ever replicate the feeling of weightlessness? Can a computer ever have what's called a notion of happiness?

**Blaise Aguera Y Arcas** [01:47]: Yeah, I think this is a great question. So first of all, you know, I, I certainly am very committed to my own embodiment and, you know, and, and, and the joys of having, you know, of, of being physical. You know, most of us are. On the other hand, you probably know about the work of Edgar Adrian, a groundbreaking neuroscientist, you know, in the beginning of the 20th century, who first recorded from nerve cells in, in frogs and, you know, realized that, for instance, all of the sensory nerves encode whatever they're perceiving, uh, in the common language of spikes of, of neural action potentials. It doesn't matter what kind of signal something is initially. You know, once it's encoded in spikes, it's information. My answer is that, you know, despite how important it is to us to be embodied and how important that is in general, uh, that, that computation be embodied, it is fundamentally computational. You know, our brains are fundamentally computational and, uh, in that sense, you know, if they were computing by other means, they would be doing the same thing. Likewise, you know, if you're, if you're experiencing something in a virtual reality, in a, in a video game or something, I mean, I don't know if you've ever had the experience of, you know, being in a, um, in a zombie game in VR or something, but, like, you, you know, you really feel anxiety, you know, when you think there's a zombie creeping up on you from behind or something. Is that embodied? Is that not embodied? I don't think that's even a simple question. So this is the sense that, you know, maybe the algorithms that we've got today, like the transformer, are just sort of a really good fit for the computing hardware that-

**Interviewer** [03:06]: Mm-hmm

**Blaise Aguera Y Arcas** [03:06]: ... we happen to have lying around, and the synergy between those things, you know, creates conditions that it'll be hard to break out of. A little bit like, you know, the way so many decades of optimization of internal combustion engines-

**Interviewer** [03:17]: Yeah

**Blaise Aguera Y Arcas** [03:17]: ... make it hard to move beyond the, you know, the, you know, to, to electric cars.

**Interviewer** [03:20]: Good analogy, yeah. Mm-hmm.

**Blaise Aguera Y Arcas** [03:21]: The positive end of lock-in is that in some sense, you know, all of evolution is about symbiosis. I imagine we'll talk more about that-

**Interviewer** [03:27]: Yeah

**Blaise Aguera Y Arcas** [03:27]: ... a little later. Uh, so you know, lock-in is kind of the name of the game. You know, when-

**Interviewer** [03:31]: Mm

**Blaise Aguera Y Arcas** [03:31]: ... when we started to manufacture our own clothes and wear them, you know, we, we lost fur, and we became locked in in a certain way to, you know, to wearing clothes or, you know, short guts and fire and so on. So there's positive lock-in in the sense that, that, you know, you have synergies that enable new things and create new possibilities, and you have the negative aspects of lock-in in which maybe there was another way of doing stuff that could have been better. And I guess the answer is that the further along you go, you know, with an existing symbiosis, and the more it gets built on top of it, the harder it becomes to revisit that.

**Interviewer** [04:04]: Mm.

**Blaise Aguera Y Arcas** [04:05]: I don't think that we're too late with AI algorithms and hardware at all. Uh, we're in the very early days still of implementing neural nets using conventional hardware like GPUs that were designed for completely other purposes-

**Interviewer** [04:17]: Mm

**Blaise Aguera Y Arcas** [04:17]: ... right, for graphics.

**Interviewer** [04:18]: That's right.

**Blaise Aguera Y Arcas** [04:19]: And we're-- There's a lot of evolutionary pressure on us right now to make it more energy efficient-

**Interviewer** [04:23]: Mm

**Blaise Aguera Y Arcas** [04:23]: ... which will absolutely steer us toward other architectures.

**Interviewer** [04:26]: Mm. The kind of, as I say, the firepower devoted to it already, it seems to me to be optimized to do what humans do best already, which is language, right? Yes, we, we have, you know, fingernails, but we're not, we don't have huge claws. We have, you know, teeth, but they're not as big as, you know, as a tiger. And yet we're the most advanced in terms of language, and that makes us unique in, in a certain sense. And, and even the largeness, you know, the quantity has a quality all its own. But I wonder as a physicist thinking selfishly, you know, is my job at risk? Because what physicists do is very different from language. Yes, you can say it's a language. I always think that's kind of facile when people say, "Oh, you're, you know, you're good at math, so you must be very musical." I say, "Yeah, I play Spotify." You know, that's-

**Blaise Aguera Y Arcas** [05:06]: [laughs]

**Interviewer** [05:06]: ... that's all I do. I've always kind of found that to be an all-too-facile kind of cop-out to the Pythagoreans. You know, it's, it's, it's kind of lost its... But you know, physics is a language, but let's just step aside. Can it do physics? You know, help me out. Is it going to take our jobs as physicists? Is it going to augment our jobs? I mean, I know it already is, but to what extent can the LLM architecture, if it is locked in, I mean, we have to plan for that contingency, right? It may get locked in-

**Blaise Aguera Y Arcas** [05:31]: Mm-hmm

**Interviewer** [05:31]: ... in the same way as you point out. So can it do physics? Can it be Einstein? Can it be, you know, AI AE in the future?

**Blaise Aguera Y Arcas** [05:38]: I've definitely, you know, worked with large language models quite a lot in the past year doing math and physics.

**Interviewer** [05:44]: Mm-hmm.

**Blaise Aguera Y Arcas** [05:44]: Uh, I don't know if you've had this experience, but it's, it's super fun.

**Interviewer** [05:46]: It is fun, oh yeah.

**Blaise Aguera Y Arcas** [05:47]: Like, you know, you just, you know, you go back and forth. You can plug in, like you know, lots of equations and say like, "Okay, suppose we rearrange this," or like, "Can we think about this in a different way?" And it's, it's awesome.

**Interviewer** [05:56]: Yeah. Can it do these kind of-- Are they intangible? I mean, I hate to be, you know, too poetic about it, but there's something poetic about that happiest feeling, and you can just feel Einstein. You know, he used to say things like he saw the, a compass deflected by a needle, and he, you know, called that something deeply is hidden.

**Blaise Aguera Y Arcas** [06:11]: Mm-hmm.

**Interviewer** [06:11]: And you know, he spoke about ghosts in the machine. So and maybe, Benjamin, you can, you can think about this as well or answer about this as well, but where the rubber meets the road, is it As successful as it is with language and, you know, constructing prose and, and writing lessons and so on, is it really capable of doing the unique things that we as humans do at least?

**Panelist** [06:29]: On the question of what kinds of things machine intelligence might be able to do versus the kinds of things that human intelligence might be able to do, in, in a way it goes really to the beginnings of the ways in which AI has been conceptualized within Western philosophy as well as within, within computer science. You even think to the, the Turing test as a kind of canonical mythology, which usually sets this up as a kind of either/or dynamic.

**Interviewer** [06:50]: Right.

**Panelist** [06:50]: Right? That there's a recogni- like, to the extent to which something is AI, it's, there's less human intelligence.

**Interviewer** [06:55]: Mm-hmm.

**Panelist** [06:55]: Or if it's human, it's not AI. It's a binary either/or, which is not really the way in which I imagine it works now, and probably is not the way we really should be thinking about it going forward. You've mentioned evolution before, and I, you know, one of the ways in which you've, you've theorized evolution within this is, within this whole dynamic is, where do we... where should we locate the discovery of computation within this larger evolutionary lev- evolutionary dynamic? And the way in which you frame evolution is less in a, the kind of Darwinian competitive sense of a zero-sum game, which may be a bit more of the, you know, the mythology we take from the, from the Turing test, but one of symbiogenesis.

**Interviewer** [07:34]: Right.

**Panelist** [07:35]: And that that's really the, like, the co- that's the key driver that we need to be looking at here, not only in terms of, you know, exchange of genetic material, but also the ways in which how complex intelligence itself evolves, right? And you talk about how within social intelligence, it's all about kind of multiplication of, of participate- participating minds, but also a division, modularity within those, right? And so what we might anticipate then is more about a kind of potentially cooperative relationship between we, the precocious linguistic primates, and who have figured out how to take bits of rock and metal and fold them just so and electrocute them in order so that the rocks can now do things that the primates used to be able to do, that whatever intelligence explosion that we might be living through is one that's probably one that makes use of both sides of this.

**Interviewer** [08:24]: Mm.

**Panelist** [08:24]: And so I think, I guess what I'm sort of suggesting is that it's not necessary to begin the question of one of replacement or displacement or, or either, or really sort of either/or. That, that may not be the precedent that we would withdraw from, and it's certainly not the way in which we would, we would sort of direct it.

**Interviewer** [08:39]: Mm-hmm.

**Panelist** [08:39]: I, I would just... But to answer the question more directly for myself, like, I'm sure there are things that the modality of human embodiment, of human experience, of like, you know, our own particular mortality-

**Interviewer** [08:51]: Mm-hmm

**Panelist** [08:51]: ... our own, the, the ways in which we've learned to experience our own experience and things like this that will remain unique and valuable. I don't think humans are going anywhere.

**Interviewer** [08:58]: Mm-hmm.

**Panelist** [08:58]: Um, and I, I don't think the proliferation of mult- of, of billions and billions of AIs as, will endanger humans at all.

**Interviewer** [09:05]: Mm.

**Panelist** [09:05]: I don't think it, you know, I don't even mean this in an optimistic sense. I just means I think that's what history would tell.

**Interviewer** [09:09]: This video is sponsored by Superhuman. Ever feel like your inbox is a black hole? No matter how much you scroll, the dreaded unread count just keeps growing. Your deadlines are vanishing like they're beyond the event horizon. That urgent collaborator message, it's out there somewhere, but finding it is going to be harder than herding thousands of Schrödinger's cats. You tried AI add-ons before, haven't you? But let's be honest, they're slow, clunky, and the drafts sound like they're written by a grant reviewer who skimmed the abstract with too little coffee. Searching for that one important email feels like scanning the cosmic microwave background, hoping that your signal just isn't dust. Superhuman has transformed the way that I work. Imagine if your inbox didn't fight you, but it worked for you, like your brilliant and tireless graduate students. That's the transformation with Superhuman. It's the leading AI-native email app, one that never misses proposals, never forgets referee replies, and always knows what matters most, from your family to your friends, to your academic colleagues, students, and more. Take thousands of unread emails into automatic organizational bliss. Auto Labels and Auto Archive clear the clutter in my inbox. Split Inbox keeps urgent messages in focus. And Superhuman Calendar instant event and Ask AI makes scheduling seem like magic. From missed opportunities to automatic follow-ups with Write with AI, drafts materialize faster than a pulsar pulses, perfectly timed and put into your voice. Auto Reminders and Auto Drafts mean you never drop the ball, even if your collaborators take their sweet time collapsing their email reply wave functions. This is the emotional shift that I've [chuckles] experienced from stressed and overwhelmed to in control and mentally clear. No inbox singularities, just focus, clarity, and time back to finally read that paper you've been citing without actually opening. Escape the gravitational pull of email inbox overwhelm and experience Superhuman transformation. Get started with one month free of Superhuman today using my link below. Now back to the episode with Blaise and Benjamin.

**Panelist** [11:12]: Yeah.

**Interviewer** [11:13]: I'm thinking concurrently about the, you know, the rise in what will probably become not only AI therapists, but, but the need for human therapists to assuage the anxieties of human beings at being replaced by AIs themselves. [laughs]

**Panelist** [11:25]: You know, one thing I, one thing I've noticed, uh, so if, if you were gonna respond to this, but is I've noticed that most of the Substacks that I've been reading like [chuckles] over the last couple months or so are people posting their conversations with models-

**Interviewer** [11:38]: Yeah

**Panelist** [11:38]: ... and analyzing their conversations, and then other people analyzing other people's-

**Interviewer** [11:42]: Yes

**Panelist** [11:42]: ... conversations.

**Interviewer** [11:43]: It's so meta. [laughs]

**Panelist** [11:43]: And so this is sort of like a, a kind of gr- a groundswell of, of psychoanalysis emerging-

**Interviewer** [11:49]: Yeah

**Panelist** [11:49]: ... in this sort of like mirroring-

**Interviewer** [11:50]: It's like a 12-step group, right?

**Panelist** [11:51]: Of-

**Interviewer** [11:51]: Yeah. In a, in a room where people-

**Panelist** [11:52]: It's a bit more Lacanian than 12-step.

**Interviewer** [11:54]: [laughs]

**Panelist** [11:54]: It's a bit more like, am I, like where is the identity dynamic here?

**Interviewer** [11:57]: Mm-hmm.

**Panelist** [11:57]: But I, I think this question of, of questioning what is the human in relationship to these sorts of reflections or artificial... I mean-

**Interviewer** [12:03]: Mm-hmm

**Panelist** [12:04]: ... I would make the argument that humans, you know, part of what science is as an epistemological pursuit and engineering, that through the artificialization of something is how we have discovered what that thing is in the first place.

**Interviewer** [12:16]: Mm-hmm. Right.

**Panelist** [12:16]: And so I think the fact that this would be the case for identity and intelligence is, is not so peculiar. But to the therapy I think there's something there.

**Interviewer** [12:24]: Yeah.

**Panelist** [12:24]: Like, I don't know, it like, we might dismiss this as a bit of a kind of superficial, narcissistic kind of somewhat pathetic people pouring their heart out to their phone. But I, I think this question of really interrogating the question of, of, of what that boundary really is, I think this is where people are figuring out what, what AI is for them.

**Interviewer** [12:43]: Yeah, I'm kind of thinking about these people I've heard about recently that, you know, upload their, you know, their whole genome to... You know, I had Craig Venter here a few months back.

**Panelist** [12:51]: Sure.

**Interviewer** [12:51]: And then, yeah, obviously the Human Genome Project, and he had, he sequenced his own genome. You know, it was $10 million a pop. Now it's less than 1,000, but with-

**Panelist** [12:58]: Yeah

**Interviewer** [12:59]: ... 21andMe or 23andMe going out of business, you know, rest in peace to those, that, that chromosome.

**Panelist** [13:04]: [laughs]

**Interviewer** [13:04]: Blaze, is there a sense that, that, you know, AIs might be training us? I mean, uh, 'cause I'm thinking, you know, if they know all of this about... If I ask ChatGPT, "Who do you think, what do you think I look like?" It'll make a picture. You know, it gets, it gets the, you know, the, the color of my hair wrong or something like that, but, but it, you know, can do it. "What do you think, how do you think I'll react to this?" It gets it much more accurately. Or, you know, and, and a lot of times it's because I'm a shameless narcissist and I just wanna hear these plat- you know, wonderful platitudes about how awesome I am. But if you ask it to be, like, go nucle- nuclear, it will do that, and it will be pretty brutal and honest, right? 'Cause it has nothing to fear. Are they training us, like, in a sense? 'Cause that would be sort of part of the symbiosis process, right?

**Blaise Aguera Y Arcas** [13:41]: 100%.

**Interviewer** [13:41]: Yeah, so how does that work?

**Blaise Aguera Y Arcas** [13:43]: Yeah, I mean-

**Interviewer** [13:43]: What should we be worried about? Yeah. [laughs]

**Blaise Aguera Y Arcas** [13:45]: I-

**Interviewer** [13:45]: Or should we?

**Blaise Aguera Y Arcas** [13:46]: First of all, yes, it's part of symbiosis.

**Interviewer** [13:47]: Mm.

**Blaise Aguera Y Arcas** [13:47]: Teaching and learning and shaping each other's behavior. I mean, in some sense, if you are unaffected by an interaction, that interaction might as well not have happened.

**Panelist** [13:55]: Right.

**Blaise Aguera Y Arcas** [13:55]: Right?

**Interviewer** [13:56]: Yes.

**Blaise Aguera Y Arcas** [13:56]: So, so every interaction is a, is a, a learning interaction in that sense.

**Interviewer** [13:59]: Mm-hmm.

**Blaise Aguera Y Arcas** [13:59]: So of course it, it goes both ways. Uh, if it didn't, then we wouldn't be having them.

**Interviewer** [14:04]: Mm-hmm.

**Blaise Aguera Y Arcas** [14:04]: They wouldn't be worth having.

**Interviewer** [14:05]: In terms of, you know, what, what, what, you know, Benjamin and I do in terms of the educational process, you say, you know, the, the, you know, interaction's one thing, but to bring out of is the literal wor- root of the word educate in Latin is to bring out of, pour out of, basically. Instead of pour into, which is what I thought it was when I, way back when, before I, I learned better. You know, this educational process, how does it inter- affect, you know... The in silico, we're not used to thinking of having malleability. We're thinking of being rigid and, and yes, it can emulate certain things. But I'm thinking in particular this recent paper by, that came out of Apple, and, and a lot of people were kind of-

**Panelist** [14:38]: We were just discussing-

**Interviewer** [14:39]: Yeah

**Panelist** [14:39]: ... some of the, some of the problems with this paper.

**Interviewer** [14:41]: Yeah, so I'd love to, I'd love to, you know, get into your thoughts of it. The only thing I didn't like was, uh, your cr- people saying, "Oh, it was written by an intern." I'm like, "Let me tell you about this intern named De Broglie, or this intern named CN Yang."

**Blaise Aguera Y Arcas** [14:53]: Don't, don't, don't talk about interns.

**Interviewer** [14:54]: Yeah, exactly. Or Bryan Josephson, he was 22 years old when he wrote the paper on qubits, basically, the Josephson junction that became qubits effectively, and that we use every day, the SQUID amplifier. But talk about, yeah, what this notion that they're basically, you know, it's kind of getting back to the original, you know, kind of tropes about them. What was it that this Apple paper was, was suggesting? And, you know, to what degree should we have any, you know, credulity in what they're claiming?

**Blaise Aguera Y Arcas** [15:16]: Actually, Benjamin, you'll be the f- the, the best one to take this because you had a, a, the first go-

**Panelist** [15:21]: [laughs]

**Blaise Aguera Y Arcas** [15:21]: ... that I saw of something to be, to be creative.

**Panelist** [15:22]: Well, let's, let's, let's, let's, let's, let's do it a bit... I mean, I think you can go to some of the, the technical aspects of this a bit more. I, when I, when I first saw this, I thought, "That's fascinating," like that this would sort of be the case. And they, the, the authors, maybe some of your, your listeners can try this for themselves, but your authors put all of the prompts that they used-

**Interviewer** [15:37]: Yeah

**Panelist** [15:37]: ... to get these results as an appendix in there-

**Interviewer** [15:39]: Yeah

**Panelist** [15:39]: ... which I think should be a norm-

**Interviewer** [15:41]: Yeah

**Panelist** [15:41]: ... generally moving forward. And so, you know, I just put the prompts into all these models myself and said, "Okay, solve the Tower of Hanoi, 47 variables."

**Interviewer** [15:49]: Right.

**Panelist** [15:49]: "Solve river crossing, 97 variables." Well, I mean, I don't mean to disparage anybody's, any [laughs] company's, but like, but Opus 4 did poorly. GPT-3 did somewhat poorly, and I was, I was able to replicate their results-

**Interviewer** [16:01]: Mm

**Panelist** [16:01]: ... where it's spades or clear as. Gemini and Grok did fine.

**Interviewer** [16:03]: Hmm. Mm-hmm.

**Panelist** [16:04]: And, you know, and, and it was able to... You'd say, well, in their paper, they say you're gonna get a kind of catastrophic collapse at about N equals 15. And I would say, "Okay, well, try 17, try 25, try 30." It's like kept getting... And then, you know, you would verify that, okay, Grok, here's Gemini's response. What do you think? Here, Gemini, here's Grok's. Like, I'll, I'll have them verify each other-

**Interviewer** [16:23]: Mm-hmm

**Panelist** [16:23]: ... agreement. They said it couldn't make a general purpose algorithm... The paper says it cannot make a general purpose algorithm that it would then, like, apply to the problem.

**Interviewer** [16:32]: Right.

**Panelist** [16:32]: Ask it to make a general purpose algorithm apply to the problem [laughs] to make do N equals 1,000. It does it fine. Turns out that, you know, this, this was, like, a couple hours on the weekend, very informal-

**Interviewer** [16:41]: Yeah

**Panelist** [16:41]: ... non-scientific kind of like-

**Interviewer** [16:42]: Right

**Panelist** [16:42]: ... can I reproduce this? But it got me thinking that there may be something to this. More recently, some other papers have come out about some of the token limit issues. Maybe you can speak to a little bit about maybe this is one of the re- one of the issues for this as well. There's another thing we probably wanna talk about in terms of what do we mean by reason-

**Blaise Aguera Y Arcas** [16:58]: Mm-hmm

**Panelist** [16:58]: ... reasoning in this as well, and like, what, what really would be a human baseline to compare this to?

**Blaise Aguera Y Arcas** [17:03]: Absolutely.

**Panelist** [17:03]: The way in which they index this as capacity for sort of transfer learning, you know, general principles that, you know, even if you're getting the arithmetic wrong-

**Blaise Aguera Y Arcas** [17:11]: Deductive

**Panelist** [17:11]: ... things like that, those are things it's wrong with.

**Blaise Aguera Y Arcas** [17:12]: Mm-hmm.

**Panelist** [17:13]: I mean, I think these are really interesting questions.

**Interviewer** [17:14]: Yeah.

**Panelist** [17:14]: I mean, I think the questions they're trying to pose here are exactly the right kinds of questions. And so I don't really... You know, I, I think there's a lot of value to the, to the, to the question they're asking. The fact that it resonated with so many people to, to kind of get of, like, really what do we mean by reasoning? What's going on here? That's all, that's all super, that's all quite valuable.

**Interviewer** [17:30]: Mm-hmm.

**Panelist** [17:30]: And so the extent to which there may be things that are incomplete or, you know, in this as well, like, that, that, that's all fine. But please, why don't you speak to your angle on this?

**Blaise Aguera Y Arcas** [17:38]: I had the same initial reaction, which was like, this is interesting. I'm always curious about-

**Panelist** [17:42]: Yeah

**Blaise Aguera Y Arcas** [17:42]: ... you know, how, uh, you know, where the failure modes are-

**Panelist** [17:44]: Yeah

**Blaise Aguera Y Arcas** [17:45]: ... of these kind of systems, how to better understand what reasoning actually means, how, you know, when we introspect, we know that introspection is not always the best guide to what's going on in our own heads. So, you know, what more can we learn about how we do it, uh, as well? These are all interesting questions.

**Panelist** [17:59]: Mm-hmm.

**Blaise Aguera Y Arcas** [17:59]: But, you know, one of the, one of the sort of comedic aspects of, of papers like this one is that they, they often have sort of two things that, you know, the, the, in the marketing, I would say, of the paper. You know, one of them is, "See, AI is really stupid."

**Panelist** [18:12]: Yeah. [laughs]

**Blaise Aguera Y Arcas** [18:12]: "It's not, it's not real."

**Panelist** [18:13]: Right. [laughs]

**Blaise Aguera Y Arcas** [18:13]: "It's a hoax." And it comes across-

**Interviewer** [18:15]: Doesn't know how many Rs are in strawberry.

**Blaise Aguera Y Arcas** [18:17]: Right, exactly

**Interviewer** [18:17]: ... like, dumbness. They can't do-

**Blaise Aguera Y Arcas** [18:18]: Or what, the wrong number of fingers or whatever it is

**Interviewer** [18:19]: ... you know, seven-digit multiplication.

**Blaise Aguera Y Arcas** [18:21]: I find that very revealing about the anxieties-

**Panelist** [18:25]: Yeah

**Blaise Aguera Y Arcas** [18:25]: ... of the people [laughs] writing these things.

**Panelist** [18:26]: Yeah, yeah, yeah. Yeah, exactly. That's the real findings.

**Blaise Aguera Y Arcas** [18:28]: Yeah.

**Panelist** [18:29]: Is a certain sense of, of a, I mean, this, the status of the human in relationship.

**Blaise Aguera Y Arcas** [18:33]: Mm-hmm.

**Panelist** [18:33]: And like, that's really what all these conversations are about.

**Blaise Aguera Y Arcas** [18:35]: Yeah.

**Panelist** [18:35]: They're not so much about, like, what can the machine intelligence do, but rather

**Blaise Aguera Y Arcas** [18:39]: Well, and, and there's, there's the other-

**Interviewer** [18:40]: What, what, what does it mean to be human anymore?

**Blaise Aguera Y Arcas** [18:41]: 100%. And, and I, I don't want to, you know, dunk on humans here. That's not what I'm about.

**Interviewer** [18:44]: Some of my best friends are human. [laughs]

**Blaise Aguera Y Arcas** [18:45]: Some of my best friends are human.

**Interviewer** [18:47]: [laughs]

**Blaise Aguera Y Arcas** [18:47]: Um, but, you know-

**Interviewer** [18:48]: Including yourself. [laughs]

**Blaise Aguera Y Arcas** [18:49]: [laughs] I only said some.

**Interviewer** [18:50]: [laughs]

**Blaise Aguera Y Arcas** [18:51]: But, you know, the, the, the problem is that when you don't do human baselines-

**Interviewer** [18:55]: That's right. That's right

**Blaise Aguera Y Arcas** [18:56]: ... when you don't, when you don't do the comparison-

**Interviewer** [18:57]: Yeah, yeah, great

**Blaise Aguera Y Arcas** [18:57]: ... of human performance-

**Interviewer** [18:58]: Yeah

**Blaise Aguera Y Arcas** [18:58]: ... you also can often be led to some pretty misleading conclusions, and sometimes those human baselines are real eye-openers. A few years ago, we did, we did a medical diagnosis model in my team at, at Google.

**Interviewer** [19:08]: Mm-hmm.

**Blaise Aguera Y Arcas** [19:09]: And, you know, of course, we did a human baseline, like how do doctors do at, at diagnosis, and I was actually shocked by how poor the, the result was. So, you know, at first I thought, "Oh, the, the model's definitely not ready for primetime."

**Interviewer** [19:19]: Right.

**Blaise Aguera Y Arcas** [19:20]: And then it's like, oh no, it's actually already much better than the average doctor.

**Interviewer** [19:23]: Well, given that that's true-

**Blaise Aguera Y Arcas** [19:24]: You know? [laughs]

**Interviewer** [19:24]: ... I mean, should we not... You know, I'm a private pilot. I fly little Cessnas around, you know, Southern California.

**Blaise Aguera Y Arcas** [19:29]: I'd love to.

**Interviewer** [19:30]: Yeah. [laughs] It's really fun.

**Blaise Aguera Y Arcas** [19:31]: Yeah.

**Interviewer** [19:31]: It's a great, a great place to do it. But one of the things that's very troubling is that when you're flying around, most people don't know this, maybe I shouldn't say, but you're flying around, essentially it's a one-channel communication. You're talking to air traffic control tower. Only you can talk to them. That means if you, you know, are talking about what you had for breakfast or, you know, the standard mic check stuff we're doing, that could be like a line of commercial airliners that can't talk. Another thing that the airline pilots have to do is that one of them on a commercial airline has to dial in a frequency where they're broadcasting the weather from the airport on a recorded loop that every, every hour on 52 minutes past the hour, it comes out and it's got a unique identifier in the phonetic alphabet, you know, alpha, bravo, charlie, like that. And it'll come out, and then you have to transcribe it. Someone has to write it down, and then you have to r- you know, tell the control tower in the... when under first contact that you have this weather information. 'Cause it could be like, well, you know, the Delta plane that landed before you blew a tire and is sitting on the runway, so you wanna know that. Or that the airport's closed because there's a, what's it called, temporary flight restriction, President Trump's flying overhead or whatever. All these things take up so much time. They're completely r- it'd be so easy for an AI to just be listening in with the skills of the Alexa, you know, uh, devices that we had 12 years ago, 10 years ago now, or, or the Google Home assistant or whatever you guys are working on. Um, and, and that would alleviate so many failure points, so many sources of, of, of delay and inefficiency, cost, you know? You'd save co- increase safety dramatically, and yet we don't do this. Same thing with doctor's office. I mean, all these doctor... The trope of doctors is that, you know, we have a, a doctor, you know, looking at a computer while the f- patient looks at, you know, his or her computer-

**Blaise Aguera Y Arcas** [21:02]: Mm-hmm

**Interviewer** [21:02]: ... in terms of the smartphone. Are we getting to the point where if you don't use these devices, if you don't use supplemental intelligence like the kind you described from years ago, it sounds like, it's malpractice?

**Blaise Aguera Y Arcas** [21:11]: I wonder about that. And, and I, and I think that a lot of our, our... I mean, some friction, you know, in these kind of sociotechnical systems is, is good. You know, we should, we should be conservative in a number of ways, and we should understand stuff as well as possible, you know, right as, as we go. But I also think that some of that conservatism, you know, really comes from ideology and from anxiety and, and, and is not helped. And, you know, this comes back to what, what Benjamin was talking about earlier, which was these anxieties about replacement.

**Interviewer** [21:36]: Mm-hmm.

**Blaise Aguera Y Arcas** [21:37]: Um, when in fact, that's, that's just not how stuff works.

**Interviewer** [21:41]: Right.

**Blaise Aguera Y Arcas** [21:42]: I think it goes back to economics. It goes back to a misreading of Darwin.

**Interviewer** [21:45]: Mm-hmm.

**Blaise Aguera Y Arcas** [21:45]: Uh, you know, everybody thinks about Adam Smith as, you know, only talking about competition. He also talked about cooperation and moral sentiments and so on. Everybody thinks about Darwin as only talking about red of tooth and claw-

**Interviewer** [21:55]: Claw, right

**Blaise Aguera Y Arcas** [21:55]: ... competition. He also, you know, provided all of the, all of the fodder for Kropotkin to write about, about mutual aid. Uh-

**Interviewer** [22:01]: And sexual selection.

**Blaise Aguera Y Arcas** [22:03]: Ex- exactly.

**Interviewer** [22:03]: Expression, Emotion in Man and Animals. Amazing book.

**Blaise Aguera Y Arcas** [22:05]: Amazing book.

**Interviewer** [22:06]: Yeah.

**Blaise Aguera Y Arcas** [22:06]: Exactly. So there's more... You know, there's so much more to this story than I think most people take away from it.

**Interviewer** [22:11]: Right.

**Blaise Aguera Y Arcas** [22:11]: And, you know, so for instance, you might think that, you know, cities are the places where, like, you can't get work because there's always somebody better than you-

**Interviewer** [22:18]: [laughs]

**Blaise Aguera Y Arcas** [22:19]: ... you know, at whatever job. But it's the opposite, right?

**Interviewer** [22:20]: Mm-hmm.

**Blaise Aguera Y Arcas** [22:20]: Those are the places historically where the opportunity's abound-

**Interviewer** [22:24]: Right

**Blaise Aguera Y Arcas** [22:24]: ... relative to, to the, the sparser places where you would think you'd have, you know, less competition. And I think that's because interactions are central.

**Interviewer** [22:32]: Yes.

**Blaise Aguera Y Arcas** [22:32]: Like, that's where this stuff comes from.

**Interviewer** [22:34]: Right.

**Blaise Aguera Y Arcas** [22:34]: When, when we talk about our experiences with, you know, AI and how delightful, you know, it can be, right, to have these, you know, these, these sort of jet pack kinds of experiences, right? It, it's interesting that the people who are most optimistic about AI are the ones who have had the most exposure.

**Interviewer** [22:48]: Right.

**Blaise Aguera Y Arcas** [22:48]: I, I'm aware I'm sounding a bit Pollyanna-ish.

**Interviewer** [22:49]: No.

**Blaise Aguera Y Arcas** [22:50]: But, you know, it's, it's, it's weird to me that the greatest anxieties come from people who I f- you know, in many ways don't know what they're talking about. Like, they haven't-

**Interviewer** [22:58]: In some cases. I would push back with respect and love and say, you know, Te- Max Tegmark has a lot of experience with these things, and he's, you know, happily, we'll call himself a doomer [laughs] and, and-

**Blaise Aguera Y Arcas** [23:07]: Yeah

**Interviewer** [23:07]: ... and warn about-

**Blaise Aguera Y Arcas** [23:07]: No exceptions

**Interviewer** [23:08]: ... e- existential risks. And, and we've had a lot of discussions, he and I, about these issues. But I think, you know, my audience is very technically minded, a lot of physicists, 21 Nobel Prize winners have been on the show, listened to it. Why did it take so long to get here? I mean, not to be maybe insulting, uh, certainly not to you, but, but to the field, it's essentially what these objects or these devices, what these transformers are doing are, is heavily linear algebraic, right?

**Blaise Aguera Y Arcas** [23:30]: Yes.

**Interviewer** [23:30]: And that's why they lend themselves so well to GPU, because-

**Blaise Aguera Y Arcas** [23:33]: 100%

**Interviewer** [23:33]: ... these are discretizable, you know, kind of event. Again, getting back to my question of, you know, can we get a grand unified theory? Can we get a theory of everything?

**Blaise Aguera Y Arcas** [23:40]: Mm-hmm.

**Interviewer** [23:40]: Can we get it even though we don't yet have Fast and the Furious 12 for, for GPT-5 to train on? In other words, if it's just these matrix multiplications, if it's just linear algebra and doing, you know, least regressions and, and so forth, is the limitation the training data, and therefore we can't get to that point yet because we don't have the pre- you know, N minus one training data set? That's why I said Fast and the... Yeah.

**Blaise Aguera Y Arcas** [24:01]: Mm-hmm.

**Interviewer** [24:01]: We just don't have the next part of language, which somehow, I don't know how, but they tell me, you know, more, more tokens, we'll be able to do more stuff. So is that really true in your opinion? I mean, is it, is it really? 'Cause it is simple at its core.

**Blaise Aguera Y Arcas** [24:14]: Yeah.

**Interviewer** [24:14]: It's vector space, high de- extremely high de- I'm not trivializing it, but effectively am I, am I, am I right that, that it's really a waiting game until we get more training data or better training data, more efficient training? What, what is the bottom like to get to that new physics so that I can get to finally get the, not, not the Keating Prize, but the Nobel Prize?

**Blaise Aguera Y Arcas** [24:30]: [laughs] Well, yes and no. So first of all, you know, has it, has it been a scaling game? So far. Yeah, I think in many ways your intuition is right. I mean, when Frank Rosenblatt, you know, invented the perceptron in, in what? It was like late 1950s.

**Interviewer** [24:43]: 50, '56.

**Blaise Aguera Y Arcas** [24:44]: You know, basically that's, that's what we were still doing-

**Interviewer** [24:47]: Yeah

**Blaise Aguera Y Arcas** [24:47]: ... you know, with AlexNet, you know, in 2012.

**Interviewer** [24:49]: [laughs]

**Blaise Aguera Y Arcas** [24:50]: And, and the reason that AlexNet worked so much better than, than Rosenblatt's perceptron was because we had much, much bigger computers. And, and not just Moore's law, because the dirty secret behind Moore's law is that it was only when it stopped that we actually got AI. You know, Moore's law progressed to making single node processors faster and faster exponentially-

**Interviewer** [25:08]: Yeah

**Blaise Aguera Y Arcas** [25:08]: ... and smaller and smaller, lower and lower power, until about 2006. After that point, the, the transistors kept on shrinking, but that scaling of clock frequency stopped.

**Interviewer** [25:18]: Mm-hmm.

**Blaise Aguera Y Arcas** [25:18]: So this is Koomey scaling, technically. And that was the point at which GPUs and multi-processing really began to take off because-

**Interviewer** [25:23]: Out of necessity? I mean-

**Blaise Aguera Y Arcas** [25:24]: Out of necessity, right.

**Interviewer** [25:25]: Okay.

**Blaise Aguera Y Arcas** [25:25]: Since you can't make the processor faster, uh, but the chips are still getting smaller, the only answer is we'll put more processors on the chip and let programmers try and figure out how to make use of that.

**Interviewer** [25:33]: Mm-hmm. And video games got big enough that they could drive the entire industry [laughs]. Well, the, but all that- At the end of the day, so what we really have to thank is the video game-

**Blaise Aguera Y Arcas** [25:39]: We absolutely have video games to thank

**Interviewer** [25:41]: ... right.

**Blaise Aguera Y Arcas** [25:41]: But, but the reason that, that video games drove that is because-

**Interviewer** [25:43]: Yeah, yeah. Yeah

**Blaise Aguera Y Arcas** [25:43]: ... graphics rendering is a really obvious use of, of, of, of parallel processing.

**Interviewer** [25:48]: Yeah. Yeah.

**Blaise Aguera Y Arcas** [25:49]: So, so that drove, and then AI rode on its coattails.

**Interviewer** [25:52]: Yeah. Mm-hmm. John Carmack for that.

**Blaise Aguera Y Arcas** [25:53]: Right.

**Interviewer** [25:53]: Yeah.

**Blaise Aguera Y Arcas** [25:53]: It's John, it's all John Carmack.

**Interviewer** [25:54]: Yeah, yeah.

**Blaise Aguera Y Arcas** [25:55]: He deserves the Nobel Prize.

**Interviewer** [25:56]: [laughs] Exactly.

**Blaise Aguera Y Arcas** [25:57]: In that sense, yes, it's just been scaling. Plus a few tricks. You know, the transformer has some tricks. You know, the, the attention trick is, is a, a little more than just a matrix multiply.

**Interviewer** [26:04]: Say more about that, because my audience might not be familiar with all the nuts and bolts of, uh, the... Attention is all you need. That's right. That's, that's one-

**Blaise Aguera Y Arcas** [26:10]: Yeah

**Interviewer** [26:10]: ... of the founding p- can you explain that? It might be also that it connects us- Yeah ... back to the, the life and computation-

**Blaise Aguera Y Arcas** [26:14]: That's true

**Interviewer** [26:14]: ... question with this as well. Like- Yeah, yeah ... how does this get from- Yeah, yeah ... this, this supercomputer over here?

**Blaise Aguera Y Arcas** [26:19]: Exactly.

**Interviewer** [26:19]: Exactly, right? Yeah, yeah. So how, how-

**Blaise Aguera Y Arcas** [26:21]: You know, it's some tricks.

**Interviewer** [26:22]: Yeah

**Blaise Aguera Y Arcas** [26:22]: There are some tricks. Um-

**Interviewer** [26:23]: So, so is... But are those, again, are they kind of aping biology? Are they aping, you know, human biology, uh, consciousness? That famous paper, can you explain a little bit more about that and how that is kind of the secret sauce in what you're implying is for the unlocking of this explosion from, you know, GPT negative one or whatever it was back in 2015 to where it is now?

**Blaise Aguera Y Arcas** [26:42]: Well, in practice, yes, transformers have been a really, really big deal. But I think more than th- well, and, and I'll, I'll say a little bit more specifically and technically about them since you're-

**Interviewer** [26:50]: Yeah

**Blaise Aguera Y Arcas** [26:50]: ... since you ask. The attention layer, which is the key thing, I think is the first innovation in neural nets that didn't actually come directly from biology.

**Interviewer** [26:58]: Mm-hmm.

**Blaise Aguera Y Arcas** [26:58]: So, uh, you know, up until that, it was all pretty much based on Hubel and Wiesel's model of visual cortex.

**Interviewer** [27:04]: And weighting.

**Blaise Aguera Y Arcas** [27:04]: Yeah.

**Interviewer** [27:05]: Mm-hmm.

**Blaise Aguera Y Arcas** [27:05]: Yeah, so just it's a dot product-

**Interviewer** [27:06]: Mm

**Blaise Aguera Y Arcas** [27:06]: ... and then a nonlinearity, and then you, you know, you go on to the next layer, which is closely modeled on, on sort of simple, simple ideas about how visual cortex works from the 1960s.

**Interviewer** [27:14]: Yeah. Mm-hmm.

**Blaise Aguera Y Arcas** [27:14]: The transformer was based on the idea that attention in some general sense, meaning, meaning focusing one's computation on the relationships between prior tokens is important, not just doing feature detec- hierarchical feature detection on that set, matters. And, and this involves essentially having every token able to interact multiplicatively with other tokens-

**Interviewer** [27:37]: Mm

**Blaise Aguera Y Arcas** [27:37]: ... uh, as opposed to just doing, doing-

**Interviewer** [27:39]: Linear

**Blaise Aguera Y Arcas** [27:39]: ... doing dot products, and then making cascades of, of these, of these attention layers. You know, there's a little more to it, but what we... You know, there, there are now a bunch of theories in neuroscience that, that there may be stuff like attention layers happening in the brain as well.

**Interviewer** [27:52]: Yeah. Wow. Hmm.

**Blaise Aguera Y Arcas** [27:52]: Uh, maybe in astrocytes, maybe in-

**Interviewer** [27:55]: Microtubules.

**Blaise Aguera Y Arcas** [27:56]: Not microtubules.

**Interviewer** [27:57]: Okay, that's all right.

**Blaise Aguera Y Arcas** [27:57]: That one is bullshit.

**Interviewer** [27:58]: 10 years [laughs] okay.

**Blaise Aguera Y Arcas** [27:59]: Bullshit.

**Interviewer** [27:59]: We always should talk about that. [laughs]

**Blaise Aguera Y Arcas** [28:01]: [laughs] Sorry. Sorry about that.

**Interviewer** [28:02]: Yeah. S- so-

**Blaise Aguera Y Arcas** [28:03]: But-

**Interviewer** [28:03]: ... Pasca says Stuart Hameroff will be calling my office soon. [laughs]

**Blaise Aguera Y Arcas** [28:06]: Not a thing. No neuroscientist believes that this, that this is plausible.

**Interviewer** [28:10]: Right. But when you have a Nobel Prize winner like-

**Blaise Aguera Y Arcas** [28:12]: Well-

**Interviewer** [28:12]: ... Sir Roger and others, right. Yeah, exactly.

**Blaise Aguera Y Arcas** [28:13]: He won it for d- he won it in a different field

**Interviewer** [28:14]: ... take it seriously, but not literally. Yeah, exactly.

**Blaise Aguera Y Arcas** [28:16]: You know, who was vitamin C guy?

**Interviewer** [28:18]: Pauling.

**Blaise Aguera Y Arcas** [28:19]: Yes.

**Interviewer** [28:19]: Linus Pauling, right.

**Blaise Aguera Y Arcas** [28:20]: I will say no more.

**Interviewer** [28:21]: [laughs]  Well, who was chemical weapons guy?

**Blaise Aguera Y Arcas** [28:24]: Yes.

**Interviewer** [28:25]: Talk about Fritz Haber. But-

**Blaise Aguera Y Arcas** [28:26]: Well, there's Nobel himself, for that matter.

**Interviewer** [28:27]: Yeah, exactly. That's what... Right, yeah. [laughs] Exactly. Explosive. Explosives are all you need. So let's get into the, yeah, the, the, the famous question asked when we're talking Nobel Prize winners. Let's talk Erwin Schrödinger. So he asked the question which you ask in your book, you know, "What is life?"

**Blaise Aguera Y Arcas** [28:40]: Yes.

**Interviewer** [28:40]: We have a, a copy of it here. Um, first of all, can you explain the different elements of this, of this m- wonderful opus? There's multiple books. What Is Intelligence?, What Is Life? I have this, Who Are We Now?

**Blaise Aguera Y Arcas** [28:51]: Interesting.

**Interviewer** [28:51]: How do they all interrelate together? Are they in some Schrödinger-like superposition? That's the question mark. That's, that's the key.

**Blaise Aguera Y Arcas** [28:55]: Yes.

**Interviewer** [28:55]: Question mark.

**Blaise Aguera Y Arcas** [28:56]: It's all about the punctuation.

**Interviewer** [28:57]: That's right. [laughs] What is life? W- how does that fit into these three or more books in the series? And then what is life? I mean, let's answer Erwin. He's been waiting. He's playing with his kitty cat.

**Blaise Aguera Y Arcas** [29:08]: [laughs] Exactly.

**Interviewer** [29:09]: [laughs]

**Blaise Aguera Y Arcas** [29:10]: Exactly. Big series of questions.

**Interviewer** [29:12]: Yeah.

**Blaise Aguera Y Arcas** [29:12]: So first of all, my, my previous book, Who Are We Now?, this was... I, I guess I wrote this in, you know, between 2016 and 2022. That was really, like, a social science book based on a bunch of surveys that I did on Mechanical Turk. It's a bit of an outlier relative to these other things-

**Interviewer** [29:25]: Mm-hmm

**Blaise Aguera Y Arcas** [29:25]: ... and it wasn't really connected with my day job at, at Google.

**Interviewer** [29:27]: [laughs]

**Blaise Aguera Y Arcas** [29:28]: It was, it was my own, out of my own interest. Um, but it does have a connection to these later ones in a way, because, like, the animating question there was, was about our transition from being animals that behave as individuals to, to you social animals that, that have a form of collective intelligence as a society. And, you know, I feel like there's a transition that we've undergone, you know, sometime in the last, you know, 100,000 years, and probably in the last 10,000 most of all, where we've become very, very different, you know, behaviorally and in terms of, in terms of our collective intelligence-

**Interviewer** [30:00]: Right

**Blaise Aguera Y Arcas** [30:00]: ... relative to just what we are biologically, and that, that's about that question.

**Interviewer** [30:04]: Mm-hmm.

**Blaise Aguera Y Arcas** [30:04]: Who Are We Now? As for the latter two, What Is Life? and What Is Intelligence?, the big book is What Is Intelligence?, and, and that's coming out on the 16th of September-

**Interviewer** [30:12]: September. Mm-hmm

**Blaise Aguera Y Arcas** [30:12]: ... from MIT Press.

**Interviewer** [30:14]: Mm-hmm. Links to all those in the show notes. In the Antithera book series.

**Blaise Aguera Y Arcas** [30:16]: In the Antithera book series.

**Interviewer** [30:17]: Mm-hmm.

**Blaise Aguera Y Arcas** [30:17]: That's, it's Antithera plus MIT.

**Interviewer** [30:19]: Yeah. That's MIT, yeah. Mm-hmm.

**Blaise Aguera Y Arcas** [30:20]: So it's a, it's a big book. It's, like, 600 pages.

**Interviewer** [30:23]: [laughs]

**Blaise Aguera Y Arcas** [30:23]: It turns out that... So we've been doing a lot of work on artificial life in the last year and a half as well, which has dovetailed with the work on AI in some really interesting ways.

**Interviewer** [30:31]: In your group at Google.

**Blaise Aguera Y Arcas** [30:32]: In... Right.

**Interviewer** [30:32]: Yeah.

**Blaise Aguera Y Arcas** [30:32]: So in, in, in, in our group at Google called Paradigms of Intelligence.

**Interviewer** [30:36]: Mm-hmm.

**Blaise Aguera Y Arcas** [30:36]: And because the life work Is sort of a, a, The Hobbit to The Lord of the Rings, of What is Intelligence. What we ended up doing is sort of publishing a book within the book. So chapter one of What is Intelligence is What is Life.

**Interviewer** [30:47]: Mm.

**Panelist** [30:48]: Mm-hmm.

**Blaise Aguera Y Arcas** [30:48]: Uh, and because it kind of stood on its own as well, we also published it, you know, standalone as the second book.

**Panelist** [30:55]: Okay.

**Interviewer** [30:55]: So life is a subset of intelligence, in other words?

**Blaise Aguera Y Arcas** [30:57]: Yes.

**Interviewer** [30:58]: Okay.

**Blaise Aguera Y Arcas** [30:58]: Although you could also look at it the other way.

**Panelist** [30:59]: Yeah.

**Blaise Aguera Y Arcas** [30:59]: Intelligence is a subset of life.

**Panelist** [31:01]: Yeah, yeah.

**Interviewer** [31:02]: You spent some time at Princeton, right?

**Blaise Aguera Y Arcas** [31:04]: Yeah.

**Interviewer** [31:04]: Some say they erred Einstein in some ways. I mean, coiner of the concept of black holes, thesis advisor to Dr. Richard Feynman, many other things. And Hugh Everett was, of course-

**Blaise Aguera Y Arcas** [31:14]: Many Worlds

**Interviewer** [31:15]: ... Many Worlds. Was, of course, John Archibald Wheeler.

**Blaise Aguera Y Arcas** [31:17]: Yes.

**Interviewer** [31:17]: Who asked this, or spoke about this question or this concept of-

**Blaise Aguera Y Arcas** [31:20]: Yeah

**Interviewer** [31:21]: ... it from bit.

**Blaise Aguera Y Arcas** [31:21]: Right.

**Interviewer** [31:22]: Can you explain that? I mean, because when I've had, I've had Caleb Scharf on, who wrote a book about information, intelligence, and life.

**Panelist** [31:28]: And Wolfram. Wolfram's-

**Interviewer** [31:30]: Yes

**Panelist** [31:30]: ... Physics Project and his, his research.

**Interviewer** [31:31]: Yeah, I mean, his, his conversation with him is-

**Blaise Aguera Y Arcas** [31:33]: Very much in front of me.

**Panelist** [31:34]: Yeah, yeah, yeah.

**Interviewer** [31:34]: Yeah. So the construction, this, this layer, you know, which computation ir- irreducibility. A- and of course we can go on all sorts of wormholes and black holes and, and information destruction, Hawking radiation. But we don't have to if we don't want to. But think about this it from bit. Is that presupposing life? I mean, it always seems tautological, that you-

**Blaise Aguera Y Arcas** [31:53]: Yeah

**Interviewer** [31:53]: ... you kind of need something living to determine what is information.

**Blaise Aguera Y Arcas** [31:57]: Right.

**Interviewer** [31:57]: And yes, because at least in my opinion, if you don't, you devolve into this solipsistic kind of notion of panpsychism, which I'm, you know, uh, continually struggling to, to reconcile with.

**Blaise Aguera Y Arcas** [32:08]: Yeah, me too.

**Interviewer** [32:08]: You know, that this, this, this monolith right in front of us is actually conscious and is participating somehow.

**Blaise Aguera Y Arcas** [32:13]: Right.

**Interviewer** [32:13]: And then on the other hand, we, we of- we, we, we can talk about the notions as, as Benjamin brought up from Wolfram and others. But, but can you talk about this it from bit. Where does this notion first gain traction in the work of, of m- many of the people that came after Wheeler, certainly, but still to this day in- influencing Shannon and others-

**Blaise Aguera Y Arcas** [32:31]: Mm-hmm

**Interviewer** [32:31]: ... in, in terms of our concepts of both information, entropy, et cetera.

**Blaise Aguera Y Arcas** [32:34]: Yeah.

**Interviewer** [32:34]: So where does it from bit and information, entropy and so forth, how do they figure into the life process?

**Blaise Aguera Y Arcas** [32:40]: Yeah, this is, this is a, a great and rich question. Okay, so first of all, there are different notions of information. There's Shannon's notion, which is, uh, very closely connected to entropy. And that, that's just, you know, the P log P-

**Interviewer** [32:51]: Mm

**Blaise Aguera Y Arcas** [32:51]: ... uh, version of things. But there are some ways in which Shannon's definition is obviously incomplete or inadequate. I think that's best framed by that famous quote from Gregory Bates about information as a difference that makes a difference. So, you know, there's no make a difference part in the Shannon definition of information.

**Interviewer** [33:08]: Mm.

**Blaise Aguera Y Arcas** [33:08]: It's, it's just, you know-

**Panelist** [33:09]: Just different. [laughs]

**Blaise Aguera Y Arcas** [33:10]: It's just, yeah. It's just difference. If you have a, a, a noise process, if you have a true random variable, then it has lots of information. You know, it'll, it'll have, it'll have as much Shannon information as you give it time to flip-

**Interviewer** [33:20]: Yeah, a black body

**Blaise Aguera Y Arcas** [33:21]: ... to flip it.

**Interviewer** [33:21]: Right, yeah. Black body is infinitely incom- you know, impossible to compute, right? So.

**Blaise Aguera Y Arcas** [33:24]: Exactly.

**Interviewer** [33:25]: Mm-hmm.

**Blaise Aguera Y Arcas** [33:25]: Um, and yet there's, you know, if it really is noise, it, it, you know, it literally could be anything else-

**Interviewer** [33:31]: Yeah. It's useless

**Blaise Aguera Y Arcas** [33:31]: ... and there's no difference.

**Interviewer** [33:32]: Right. Every black body's identical-

**Blaise Aguera Y Arcas** [33:33]: Is the same

**Interviewer** [33:33]: ... in some sense to another one.

**Blaise Aguera Y Arcas** [33:34]: Exactly. And that's very different from, say, the information in DNA.

**Interviewer** [33:38]: Yeah.

**Blaise Aguera Y Arcas** [33:38]: Right? Which, which is purposive. You know-

**Interviewer** [33:41]: Mm-hmm

**Blaise Aguera Y Arcas** [33:41]: ... it brings along with it this idea that I guess Kolmogorov w- might have called algorithmic information.

**Interviewer** [33:45]: Mm-hmm. Coding. Mm-hmm.

**Blaise Aguera Y Arcas** [33:46]: It codes for something, right?

**Interviewer** [33:48]: Mm-hmm.

**Blaise Aguera Y Arcas** [33:48]: There is, there's something that is, that is a result of that.

**Interviewer** [33:50]: Mm-hmm.

**Blaise Aguera Y Arcas** [33:50]: Uh, so th- I think that's the key. Now, this introduces i- lifelike ideas right away because the moment you start to talk about things having purpose-

**Interviewer** [33:58]: Right. Teleo

**Blaise Aguera Y Arcas** [33:59]: ... you're either talking about teleology and you're in, you're in, you know, God land.

**Interviewer** [34:02]: Mm-hmm.

**Blaise Aguera Y Arcas** [34:03]: Or you're talking about biology, and this is the way that I prefer to think about it. What I mean by that is that a kidney is about, is about filtering urea from the blood, and that functional perspective on what the kidney does is super important. Because, you know, what matters about the kidney is not the atoms that make it up, right? It's not the implementation, it's the fact that it has this function.

**Interviewer** [34:24]: Mm-hmm.

**Blaise Aguera Y Arcas** [34:25]: Uh, if something else does that function, like a dialysis machine, you're still good. If nothing does that function, you're dead.

**Interviewer** [34:31]: [laughs]

**Blaise Aguera Y Arcas** [34:31]: Right? And, and in that sense, life is all about functions interacting with each other, functions that are mutually interdependent.

**Interviewer** [34:38]: Mm-hmm.

**Blaise Aguera Y Arcas** [34:38]: Uh, or symbiotic. And the whole idea of functionality, you know, comes along with the show.

**Interviewer** [34:43]: Mm.

**Blaise Aguera Y Arcas** [34:43]: With life. You know, you can't talk about a rock being broken.

**Interviewer** [34:46]: Right.

**Blaise Aguera Y Arcas** [34:46]: Right? If you break a rock in half, you have two rocks now.

**Interviewer** [34:49]: Rock. [laughs]

**Blaise Aguera Y Arcas** [34:49]: Right. But you can talk about a, a, a living thing being broken.

**Interviewer** [34:52]: Mm-hmm.

**Blaise Aguera Y Arcas** [34:52]: And, and one of the ways that you can see functionality-

**Panelist** [34:54]: Because it, because it breaks the functions

**Blaise Aguera Y Arcas** [34:55]: ... and because it breaks the functions.

**Panelist** [34:56]: And the functions are scaffolds to more complex functions, and so on, and so forth.

**Blaise Aguera Y Arcas** [34:59]: Exactly. And each function is defined relative to other functions. So, you know-

**Panelist** [35:01]: Yeah

**Blaise Aguera Y Arcas** [35:01]: ... something that filters urea is only there because something else produces urea that needs to be filtered. The way you can tell in life that function matters is that very, very often it will come up with multiple ways of solving the same problem. So, like, you have aerobic and anaerobic respiration. You know? Like, you know what respiration is for because nature has come up with redundant ways-

**Interviewer** [35:20]: Mm-hmm

**Blaise Aguera Y Arcas** [35:20]: ... to, to make that work.

**Panelist** [35:21]: Or even the same way to solve. I mean, convergent evolution of ways in which-

**Blaise Aguera Y Arcas** [35:24]: Exactly

**Panelist** [35:24]: ... like, I don't know if it introduces teleology necessarily, but some sort of-

**Blaise Aguera Y Arcas** [35:28]: In a way it does

**Panelist** [35:28]: ... teleonomy. That, like-

**Blaise Aguera Y Arcas** [35:29]: Yeah

**Panelist** [35:29]: ... that given a certain set of circumstances, you're going, even blind evolution is gonna res- result in similar, similar outcomes.

**Blaise Aguera Y Arcas** [35:36]: Outcomes. Right, exactly.

**Interviewer** [35:36]: Mm-hmm.

**Panelist** [35:37]: Implies the agency of function-

**Blaise Aguera Y Arcas** [35:39]: 100%

**Panelist** [35:40]: ... is driving form. Yeah. Is that-

**Blaise Aguera Y Arcas** [35:41]: Right. Yeah, yeah.

**Panelist** [35:41]: Okay, great.

**Blaise Aguera Y Arcas** [35:42]: Totally, that's, I think that's totally right. I've come around to thinking about these questions as being really the same questions as, as the ones at the heart of computer science. I've, I've really come at these things more as a physicist than as a compu- I've actually never taken a course in computer science.

**Panelist** [35:53]: [laughs]

**Blaise Aguera Y Arcas** [35:53]: So I'm, I'm an amateur at that field.

**Panelist** [35:55]: That makes two of us.

**Interviewer** [35:56]: Me as well.

**Blaise Aguera Y Arcas** [35:56]: There we go.

**Panelist** [35:57]: [laughs]

**Interviewer** [35:57]: [laughs]

**Blaise Aguera Y Arcas** [35:57]: But I've, I've come to, I've come to think [laughs] I've come to think about, about computation as really the, the sort of skeleton key that unlocks a lot of these ideas.

**Interviewer** [36:05]: Mm-hmm. Mm-hmm.

**Blaise Aguera Y Arcas** [36:06]: Because the very way that Turing defined computation is in terms of, of multiple realizability or platform independence. Uh, in other words, you know, if, if you have a mathematical function and something computes it- Then it doesn't matter what the machinery is that computes it. They're all equivalent.

**Interviewer** [36:21]: Right. This universal Turing machine.

**Blaise Aguera Y Arcas** [36:23]: A universal, exactly.

**Interviewer** [36:24]: But, but again, there's this notion that something has to then say that something has been computed, right?

**Blaise Aguera Y Arcas** [36:29]: Yes.

**Interviewer** [36:29]: So there's this infinite tape and, and it, and it has certain functions it can store. But if you... Again, a rock, you know, or a piece of salt is, is very organized, highly structured, you know, it seems to have, you know, it was contingent upon many different things happening going back to the Big Bang, right?

**Blaise Aguera Y Arcas** [36:43]: That's right.

**Interviewer** [36:44]: And stars exploding, and then, you know, things coalescing in our, in our, uh, solar nebula, pre- pre-galactic solar nebula.

**Blaise Aguera Y Arcas** [36:49]: Right. Who gets to say what its purpose is?

**Interviewer** [36:50]: Yeah. When does... Yeah. When do, when does it embody a computational substrate?

**Blaise Aguera Y Arcas** [36:54]: Yeah.

**Interviewer** [36:54]: Or when does it embody code? These are all seem very squishy and, and sort of undefinable. Is it-

**Blaise Aguera Y Arcas** [36:59]: They, they are. And this is cool-

**Interviewer** [37:00]: Yeah

**Blaise Aguera Y Arcas** [37:00]: ... this is very cool as well.

**Interviewer** [37:01]: Yeah, yeah.

**Blaise Aguera Y Arcas** [37:01]: 'Cause, okay, so first of all, there are researchers like Susan Stepney, for instance, at University of York, who have talked about, you know, when does a system compute? How can we-

**Interviewer** [37:08]: Yeah

**Blaise Aguera Y Arcas** [37:08]: ... how can we say that it computes? Basically, you have to define a mapping between physical states and computational states, which is a kind of coarse graining.

**Interviewer** [37:16]: Mm-hmm.

**Blaise Aguera Y Arcas** [37:16]: And you have to convince yourself that, that the physical evolution matches the, the, the algorithmic evolution-

**Interviewer** [37:22]: Mm-hmm

**Blaise Aguera Y Arcas** [37:22]: ... or the abstract evolution of that, of that as a, as a computing machine. That involves modeling.

**Panelist** [37:26]: But the question is, is it observer independent?

**Blaise Aguera Y Arcas** [37:28]: It is not observer independent.

**Interviewer** [37:29]: Right.

**Panelist** [37:29]: Brian's question, yeah.

**Blaise Aguera Y Arcas** [37:29]: That in- that involves forming a model.

**Panelist** [37:31]: Mm-hmm.

**Blaise Aguera Y Arcas** [37:31]: So weirdly and interestingly, it takes a model to know a model.

**Interviewer** [37:34]: To know a model, right.

**Blaise Aguera Y Arcas** [37:35]: Right.

**Panelist** [37:35]: Mm-hmm.

**Blaise Aguera Y Arcas** [37:35]: It takes a computer to know a computer. And I guess the perspective that I've come to, that I've come to believe is that I don't think there is a view from above. In this sense, I kind of agree with Carlo Rovelli in the way he talks about relational quantum mechanics-

**Panelist** [37:47]: Mm-hmm

**Blaise Aguera Y Arcas** [37:47]: ... but of everything.

**Panelist** [37:48]: Mm-hmm.

**Blaise Aguera Y Arcas** [37:49]: You know, that, that when we talk about something being, you know, a chair, right, or being... I, I mean, let's, let's take simple machines like these grinding stones that we discover. You talk about, like, you know, archeological discoveries-

**Panelist** [37:58]: The Tatters

**Blaise Aguera Y Arcas** [37:59]: ... cavemen. Right.

**Panelist** [38:00]: [laughs]

**Blaise Aguera Y Arcas** [38:00]: Yeah. Like, how do you know, you know, what-

**Interviewer** [38:02]: Right

**Blaise Aguera Y Arcas** [38:03]: ... what this thing is good for? It's a rock, you know? [laughs]

**Interviewer** [38:04]: Right.

**Blaise Aguera Y Arcas** [38:04]: Is it broken? Is it not broken? Only the caveman could tell you necessarily-

**Interviewer** [38:08]: Right

**Blaise Aguera Y Arcas** [38:08]: ... necessarily, right, does it still work for its intended purpose.

**Interviewer** [38:10]: You know, building like the library, the new buildings up here on campus, they... Benjamin, you might know this.

**Panelist** [38:14]: Yeah.

**Interviewer** [38:14]: But they, they found like some stone. They found... Uh, sorry, they found seashells. And you know, I would say, "All right, you found a seashell. The whole thing used to be a seashore." And they're like, "No, no, no. We have to now, we have to dig for bodies." I'm like, what the hell? Because these seashells in most part were transported by people up to eat, you know-

**Panelist** [38:28]: Yeah

**Interviewer** [38:28]: ... crack them open and eat them.

**Panelist** [38:29]: Yes.

**Interviewer** [38:29]: So you find a seashell, you might think, oh, it's just a natural pro- No, it's not so likely, right?

**Blaise Aguera Y Arcas** [38:33]: Exactly.

**Interviewer** [38:33]: So same, same kind of line of, of reasoning.

**Blaise Aguera Y Arcas** [38:35]: Same problem.

**Interviewer** [38:36]: Yeah.

**Blaise Aguera Y Arcas** [38:36]: So purposes-

**Panelist** [38:36]: They, they-

**Blaise Aguera Y Arcas** [38:36]: ... can only be recognized by purposive entities.

**Interviewer** [38:38]: So I just thought-

**Panelist** [38:39]: So there's, there's the detection of artificiality-

**Interviewer** [38:42]: Yes

**Panelist** [38:42]: ... of determining-

**Blaise Aguera Y Arcas** [38:43]: Exactly

**Panelist** [38:43]: ... this is so-

**Interviewer** [38:43]: Right

**Panelist** [38:43]: ... this is a whole fascinating thing in itself.

**Interviewer** [38:44]: So I think, you know, you can't go from, uh, you know, bit to it or it to bit without a wit. You need some conscious of-

**Blaise Aguera Y Arcas** [38:50]: Exactly

**Interviewer** [38:51]: ... you know, some consciousness in the, in the equa- which we also don't understand.

**Blaise Aguera Y Arcas** [38:53]: You need, you need coarse graining.

**Interviewer** [38:54]: Yep.

**Blaise Aguera Y Arcas** [38:55]: And there, there has to be a coarse grainer.

**Interviewer** [38:57]: Yeah. Coarse grainer is a, is a selector, is a filter-

**Blaise Aguera Y Arcas** [38:59]: That's right

**Interviewer** [39:00]: ... is, is somebody with agency. I wanna talk about your remarkable kind of, uh, uh, collaboration. And, and I note that in some of the writings I've read from you, there's almost this, this artistic, you know, kind of conception that, that threads its way through it. And I'm wondering if that was not part of at least the catalytic wonder that went into your relationship. Speak about the role of improvisation, of noise. You know, we... I just learned recently the root of the word noise is nausea, which means, you know-

**Blaise Aguera Y Arcas** [39:25]: That's right

**Interviewer** [39:26]: ... as in sick, it makes you sick. Which, you know, those of us that study experimental physics happens to make me very nauseous.

**Panelist** [39:31]: [laughs]

**Interviewer** [39:31]: But it's also the most interesting thing.

**Panelist** [39:33]: I, I see Shannon totally differently now.

**Interviewer** [39:35]: Yeah. [laughs]

**Blaise Aguera Y Arcas** [39:36]: [laughs]

**Interviewer** [39:37]: Yeah. But your collaboration, your work together, but, but also what is the role of improvisation? I mean, I'm used to my friend Stefan Alexander talking about the universe is improvising. And, you know, he and I tease each other about that. What does that really mean? Is that-

**Blaise Aguera Y Arcas** [39:48]: I believe that

**Interviewer** [39:48]: ... some squishy thing. But you know, there are noise filters, there's processes of which, you know, Wiener filtering. You, you have to take into account noise, and in fact, you can improve the filtering of the process by accounting for the noise model. So how, how does this come into play? How, what's the role of noise and what is im- what's improvisational relation- what's the relationship of improv to what you guys are, uh, uh, involved in collaborating?

**Blaise Aguera Y Arcas** [40:09]: That's a fantastic question. Benjamin, do you wanna begin with like the relationship-

**Interviewer** [40:11]: Yeah

**Blaise Aguera Y Arcas** [40:11]: ... part of this?

**Interviewer** [40:12]: I'd like to know more about that.

**Blaise Aguera Y Arcas** [40:12]: Like to talk a bit about noise and contingency.

**Interviewer** [40:13]: Your origin story, your meet cute.

**Panelist** [40:15]: I know. I'm trying to think about how to sort of cr- how to, how to characterize this sort of b- b- bit as well. Um.

**Blaise Aguera Y Arcas** [40:21]: It did, it did begin-

**Interviewer** [40:21]: We should say for the audience that may not have w- seen the first episode

**Panelist** [40:24]: It did. I mean, it, it did. I mean, this was the... So y- you were, it was a group called Artist Machine Intelligence that, that Kay Lari McDowell was directing. And so I think he was the, they were the one who originally-

**Blaise Aguera Y Arcas** [40:33]: She was the instigator

**Panelist** [40:34]: ... the instigator in sort of originally sort of meeting us together. I, I, I think there was probably, it seems sort of more generally, I, I think there's... We both have a comment from sort of different angles, right? My, my approach is probably more philosophical than artistic I gue- I guess at this point. And, you know, yours but then is heading towards the sciences. I mean, a lot of my consternation [laughs] with the humanities is, is exactly divid- on this sort of civil war between science and the humanities. I, I happen to think-

**Blaise Aguera Y Arcas** [41:01]: We don't, we don't believe in that stuff.

**Panelist** [41:02]: I ha-

**Blaise Aguera Y Arcas** [41:03]: The two cultures.

**Panelist** [41:03]: Exactly. We don't believe in the civil war. Like, I happen to think that all of the human, all of philosophy of the 21st and 22nd century has to be reconstructed from all the new shit that's come to light-

**Blaise Aguera Y Arcas** [41:11]: Mm-hmm

**Panelist** [41:11]: ... through science. Like, uh, this is like, as opposed to-

**Blaise Aguera Y Arcas** [41:14]: Right

**Panelist** [41:14]: ... this incessant-

**Interviewer** [41:15]: Philosophy first, right

**Panelist** [41:15]: ... as opposed to this incessant critical stance of trying to debunk science-

**Blaise Aguera Y Arcas** [41:19]: Mm-hmm

**Panelist** [41:19]: ... which is I find throughout this is, this sort of thing as well.

**Blaise Aguera Y Arcas** [41:21]: It's not very generative. Right.

**Panelist** [41:22]: It's totally ungenerative, right? And I, and I think in this regard, for me, what we... You know, science is not just sort of a method, science is the raw material-

**Blaise Aguera Y Arcas** [41:31]: Mm-hmm

**Panelist** [41:31]: ... by which really the philosophy of an et cetera needs to, needs to be g- needs to be generated.

**Blaise Aguera Y Arcas** [41:36]: Right.

**Panelist** [41:36]: And so a lot of the fundamental questions about, you know, who, what, when, where, how-

**Blaise Aguera Y Arcas** [41:40]: Mm-hmm

**Panelist** [41:40]: ... why, and all the ones that with question marks at sort of the end of this, we have opportunity to sort of ask again. That, you know, for, as I, I think I mentioned on the, my conversation with you on the last podcast, you know, there's certain times in history where our, our ideas are well ahead of our technological capabilities. You know, Tsiolkovsky's idea of space travel-

**Interviewer** [42:00]: Right

**Panelist** [42:00]: ... um, may be one. And then there's other moments where our technologies perhaps are, are way ahead of our available concepts by which to adjudicate them or orient them, and I think that's probably more where we're at-

**Blaise Aguera Y Arcas** [42:10]: Today

**Panelist** [42:11]: ... today.

**Interviewer** [42:11]: Yeah.

**Panelist** [42:12]: And in moments like that, the job of philosophy is rather different. It's not so to sort of project axioms onto new circumstances. And, and I'd say what would Contra Confucius or Hegel say about this new thing, but rather what are the concepts that need to be generated and created, you know, collaboratively, collectively in such a way to sort of, that, that-

**Blaise Aguera Y Arcas** [42:31]: Make it useful, have you to-

**Panelist** [42:32]: To make useful.

**Blaise Aguera Y Arcas** [42:33]: Mm-hmm.

**Panelist** [42:33]: That what are the abstractions-

**Blaise Aguera Y Arcas** [42:34]: Mm-hmm

**Panelist** [42:34]: ... the qualitative abstractions that can be made, can become part of a kind of higher order transfer learning to understand this from this as well. And so a lot of my work more recently has been focused on, I mean, you mentioned the how do we know whether these seashells are, just happen to be there or someone put them there. Like, this question of what constitutes artificialization more generally, which is a sort of a long, a longer, a longer topic, and how it relates to allopoiesis and niche construction, evolutionary theory. But again to this statement I made before, that through the process of artificializing something is how we discover what that is in an important way, and always has been, right? And I think that now the fundamental technologies by which h- humans and the entire, you know, human complex on which we depend is doing this. Is, both artificial, you know, artificializing life, artificializing intelligence, artificializing embodiment, artificializing these three as well, is also a process of rediscovering what those things are in, in, in a, a way that p- potentially has Copernican scale ramifications for all of these. Which for, to me, should be the most exciting thing possible for a philosopher. And so I was just very, very happy to meet Blaise, who was sort of coming it from the other side, from scientific side, the engineering side, who had a similar kind of, I think, a similar kind of sense that these are the front q- questions that we can ask and that we can ask from doing this as well. And so I, it's just been a very, I think, a lot of compatibility around that sort of ... I mean, I should say, there's not a lot of people who do the kind of work that Blaise does with the level of depth and seriousness-

**Blaise Aguera Y Arcas** [44:07]: Right

**Panelist** [44:07]: ... that he does, who are as-

**Blaise Aguera Y Arcas** [44:09]: That, that gotcha

**Panelist** [44:09]: ... who are philosophically adept enough to actually kind of understand the, like, how to sort of do, like, really do the, the serious, serious-

**Blaise Aguera Y Arcas** [44:17]: Right

**Panelist** [44:17]: ... seri- the serious-

**Blaise Aguera Y Arcas** [44:18]: Winnow away the-

**Panelist** [44:18]: ... math and the serious math and science that's necessary to actually, actually make, you know, fundamental contributions. But actually can take a step back and understand this within the big picture, and so, like, like what best possible collaborator.

**Blaise Aguera Y Arcas** [44:29]: So, uh, uh, I mean, ditto. But, you know, also I, I don't, you know, Benjamin is also, is also extremely rigorous, especially given the standards that often obtained in the fields that he's been talking about.

**Panelist** [44:40]: Yeah.

**Blaise Aguera Y Arcas** [44:40]: But I also don't want to let him get away with pretending that he is not an artist as well.

**Panelist** [44:44]: Yeah.

**Blaise Aguera Y Arcas** [44:44]: You know, he, he both is a great writer as you, as you know if you-

**Panelist** [44:47]: Yeah

**Blaise Aguera Y Arcas** [44:47]: ... you know, read his, read his work. You know, at this architecture biennale that we were just, you know, at in Venice together. And there, you know, he, he and the Antipodara program put, put on an exhibit that, you know, was, was beautiful and spooky and, you know, riveting and, you know, and all the things that, that, you know, that one, one wants-

**Panelist** [45:04]: Yeah

**Blaise Aguera Y Arcas** [45:04]: ... art to be. So this belief that, that the cultures are separate, you know, right, we, we, we both sort of disavow that.

**Panelist** [45:11]: Right. [laughs]

**Blaise Aguera Y Arcas** [45:12]: And, and, uh, and I think, I think-

**Panelist** [45:13]: Awesome

**Blaise Aguera Y Arcas** [45:14]: ... the collaboration shows that.

**Interviewer** [45:15]: Can an AI improvise? Not just ... And, and could we tell the difference between it improvising and/or hallucinating?

**Blaise Aguera Y Arcas** [45:23]: Yeah.

**Panelist** [45:23]: This may be open-ended evolution question-

**Blaise Aguera Y Arcas** [45:25]: It is

**Panelist** [45:25]: ... coming in here, but yeah, yeah. Good

**Blaise Aguera Y Arcas** [45:26]: It is. So I mean, to connect this to your, your earlier question about the fundamental role of noise in evolution and, and in purposiveness. The basic theory behind, uh, you know, what I talk about in words as opposed to math in, in What Is Life, is that, you know, normally a, a lot of mathematical models for evolution are written in terms of ordinary differential equations. You know, Lotka-Volterra style. You know, you have species and, you know, they'll-

**Interviewer** [45:51]: Predator, prey

**Blaise Aguera Y Arcas** [45:52]: ... compete and cooperate and, you know, one will eat the other or whatever. But the problem with those formulations is that they're not, they're, they're closed-ended, they're not open-ended.

**Interviewer** [46:00]: Mm-hmm.

**Blaise Aguera Y Arcas** [46:00]: Like, y- if you have, you know, hawks and doves, you're never gonna get, you know, iguanas and snails out of that.

**Interviewer** [46:05]: [laughs]

**Blaise Aguera Y Arcas** [46:05]: You know? [laughs] Um-

**Panelist** [46:06]: I've tried. [laughs]

**Interviewer** [46:07]: [laughs]

**Blaise Aguera Y Arcas** [46:08]: We try, but, but, you know, all you get is, all you get out is what you put in.

**Panelist** [46:11]: Stay away from the San Diego Zoo, that's all I'm gonna say.

**Blaise Aguera Y Arcas** [46:13]: The trick is that the really generative moments in evolution are the moments when things come together to make something new. Mitochondria end up inside a bacterium.

**Interviewer** [46:24]: Right.

**Blaise Aguera Y Arcas** [46:24]: Right? Or when, you know, cells stick together in a clump-

**Panelist** [46:27]: Like a memory [laughs]

**Blaise Aguera Y Arcas** [46:27]: ... and become a multicellular organism. Or yeah, or when a brain forms. And all of those symbiogenetic moments begin with a random event that, that then sticks and, and, and recreates itself, reproduces itself through time. Randomness is, you know, is, is absolutely the engine behind novelty of all kinds-

**Interviewer** [46:45]: Mm-hmm

**Blaise Aguera Y Arcas** [46:46]: ... in, in the universe. It's novelty plus selection.

**Panelist** [46:48]: And generativity.

**Blaise Aguera Y Arcas** [46:49]: And generativity that comes out of that, because the, the, the more complex of things you've got in the play pen, the more interesting the things are that they can form when they start to combine together.

**Panelist** [46:58]: So, so is this is where the-

**Blaise Aguera Y Arcas** [46:59]: Yeah

**Panelist** [47:00]: ... there's connection between this, your, your work and assembly theory.

**Blaise Aguera Y Arcas** [47:03]: Yes.

**Panelist** [47:04]: I mean, that, and that, where you've got this one, this sort of scaffolding dynamic around this as sort of as well. But I mean, obviously-

**Interviewer** [47:09]: Improvisation

**Panelist** [47:09]: ... you certainly have different theories about comput- different opinions about computation.

**Blaise Aguera Y Arcas** [47:13]: Sure.

**Panelist** [47:13]: But I mean, is there a reason?

**Blaise Aguera Y Arcas** [47:14]: Yeah.

**Panelist** [47:14]: Because they've both been on your show.

**Blaise Aguera Y Arcas** [47:15]: Yes.

**Panelist** [47:15]: And they're sort of don't connect together.

**Interviewer** [47:17]: I was gonna ask about improvisation then. Is it, is it something i- in the process where at least in the form of artificial life, which you talk about, is that a necessity? Is it, is it, or again, is it something like we're just projecting names onto these, you know, personifying things because we don't fully understand the, the route from randomness, pure randomness, you know, no purpose by definition. You know, it's a ticking of a caesium atom somewhere decaying, versus, you know, a jazz musician like my friend Stefan Alexander, you know, improvising because he has some tangible but, but nebulous goal in the future. You know, he analogizes it to path integral formulation and quantum mechanic.

**Blaise Aguera Y Arcas** [47:55]: Nice.

**Interviewer** [47:55]: You don't know where it's gonna ... But you know the kinda sum over history's waiting again that you're gonna get to. But what does improvisation have to do with anything? And who or what is improvving? You know, all this. [laughs]

**Blaise Aguera Y Arcas** [48:05]: Yeah.

**Interviewer** [48:05]: You know, can we go down to the comedy club and, and, and, you know, participate in it? So what does improvisation have to do with it and who's doing it?

**Blaise Aguera Y Arcas** [48:11]: Yeah. 100%, 100%.

**Interviewer** [48:12]: Yeah.

**Blaise Aguera Y Arcas** [48:12]: It's, so yes, randomness is essential to it. We know from computational neuroscience that a lot of how the brain is made has to do with being on a knife's edge-

**Interviewer** [48:22]: Mm-hmm

**Blaise Aguera Y Arcas** [48:22]: ... with, with dynamical instability.

**Interviewer** [48:24]: Mm-hmm.

**Blaise Aguera Y Arcas** [48:25]: Uh, and you know, one way of looking at this is that any living thing that is 100% predictable Will get eaten. You know, so there's an adversarial aspect to it. Like, you know, you, you have to be a little bit unpredictable-

**Interviewer** [48:35]: Right

**Blaise Aguera Y Arcas** [48:35]: ... in order to not get predicted right into somebody's belly.

**Interviewer** [48:38]: Mm-hmm.

**Blaise Aguera Y Arcas** [48:38]: But there's also a cooperative aspect to it. If you are never surprised in your interaction with somebody, then they might as well not exist.

**Interviewer** [48:45]: Right.

**Blaise Aguera Y Arcas** [48:45]: Right? Their m- that interaction might as well not take place. So, you know, the reason that we are symbiotic with each other is because we all add something to the, to the mix, and we add something because we are not entirely predictable to the others.

**Interviewer** [48:56]: Mm.

**Blaise Aguera Y Arcas** [48:57]: You know, largely predictable, that's, that's how we establish trust.

**Interviewer** [49:00]: Right.

**Blaise Aguera Y Arcas** [49:00]: But unpredictable, too, that's how we es- add value

**Interviewer** [49:02]: The surprise leads to delight and to engagement and dopamine release.

**Blaise Aguera Y Arcas** [49:06]: Exactly.

**Interviewer** [49:06]: Yeah, mm-hmm.

**Blaise Aguera Y Arcas** [49:07]: Exactly.

**Interviewer** [49:07]: Mm-hmm.

**Blaise Aguera Y Arcas** [49:07]: So those, those random processes and that knife-edge-ness have to be a part of that. You know, in order for you to be in a dynamical state, if you like-

**Interviewer** [49:14]: Mm

**Blaise Aguera Y Arcas** [49:14]: ... where, like, a whisper in your ear or a slight hint or a suggestion or something could lead you to do this or do that-

**Interviewer** [49:19]: Mm

**Blaise Aguera Y Arcas** [49:19]: ... that are very different, that implies something subtle-point-like-

**Interviewer** [49:22]: Mm-hmm

**Blaise Aguera Y Arcas** [49:22]: ... you know, about the, about the dynamical system in your, in your head.

**Interviewer** [49:25]: Mm.

**Blaise Aguera Y Arcas** [49:26]: And that also means that you're highly sensitive to noise. So, so noise is the thing that you harvest in order to render creativity-

**Interviewer** [49:34]: Mm

**Blaise Aguera Y Arcas** [49:34]: ... if that makes sense.

**Interviewer** [49:34]: But improvisation is also in the, the kind of dynamical ca- the, the sort of the knife-edge point in a conversation and cooperation-

**Blaise Aguera Y Arcas** [49:41]: Yes

**Interviewer** [49:41]: ... between two agents. It's not just in the computational neuroscience of your own skull.

**Blaise Aguera Y Arcas** [49:44]: As it is inside the brain, it is between people, too.

**Interviewer** [49:46]: The comedy club example is always troupe improvis- you know, it's a group improvisation, right?

**Blaise Aguera Y Arcas** [49:51]: Right.

**Interviewer** [49:51]: It's playing back and forth and passing the ball in ways in which that are slightly unexpected.

**Blaise Aguera Y Arcas** [49:56]: Right.

**Interviewer** [49:56]: To me, it's like, it's obvious that one can do that with AIs.

**Blaise Aguera Y Arcas** [50:00]: Of course.

**Interviewer** [50:01]: One can, one can improvise with AIs. Whether im- it can improvise on its own, it's... Obvi- like-

**Blaise Aguera Y Arcas** [50:07]: Well-

**Interviewer** [50:07]: Can, can a person improvise on your own? I-

**Blaise Aguera Y Arcas** [50:09]: If it has a temperature setting, then it, you know, it can, it can somewhat.

**Interviewer** [50:11]: It can't, yeah. Then you just get some more noise with it.

**Blaise Aguera Y Arcas** [50:12]: And that's-

**Interviewer** [50:12]: So, but, I mean, the, the... I guess what the point is, again, it's the social dynamic-

**Blaise Aguera Y Arcas** [50:16]: Mm-hmm

**Interviewer** [50:16]: ... between human and machine intelligence where the most interesting improvisation is likely to happen, of just following, following weird threads and rabbit holes.

**Blaise Aguera Y Arcas** [50:22]: Yeah, I think, I think that's true. Interesting. But then in terms of utility, it's-

**Interviewer** [50:26]: Yeah

**Blaise Aguera Y Arcas** [50:26]: ... it's almost the opposite, right? I mean, you talk about autocomplete.

**Interviewer** [50:28]: Yeah.

**Blaise Aguera Y Arcas** [50:28]: You know, I mean, you talk about how that's so useful, but it's, it's not generat- I mean, you don't want it to be generative, right? I mean, you-

**Interviewer** [50:33]: You want the autocomplete to actually take you there. If I type in Blaise, you know, I don't want it to lead... Or what is, I don't want it to lead to some other person's, you know, Blaise Pascal's books.

**Blaise Aguera Y Arcas** [50:40]: Mm-hmm.

**Interviewer** [50:41]: I want it to lead to yours. So what is the role of predictability for g- you know, opposite maybe?

**Blaise Aguera Y Arcas** [50:44]: Well, again, predictability and unpredictability-

**Interviewer** [50:46]: Yeah

**Blaise Aguera Y Arcas** [50:46]: ... both, right? So, so that's... I mean, this is why we use a temperature setting in AI, but it's also why the fundamental thing that AI is trained to do is literally to predict.

**Interviewer** [50:55]: Mm-hmm. [laughs]

**Blaise Aguera Y Arcas** [50:55]: Right? [laughs] So, you know, the, the fact that it is predicting what natural human interactions look like based on, you know, lots and lots of text on the web-

**Interviewer** [51:02]: Mm-hmm

**Blaise Aguera Y Arcas** [51:03]: ... is also why, why we can predict what AI will do, you know, to a reasonable degree. If you're typing in a, um, a math problem, you know, and you're predicting that it's gonna give you the correct answer and it does, you're happy, right?

**Interviewer** [51:14]: Mm-hmm.

**Blaise Aguera Y Arcas** [51:14]: You don't, you don't want a random answer.

**Interviewer** [51:16]: Mm-hmm.

**Blaise Aguera Y Arcas** [51:16]: But again, at the same time, you know, the reason that they have a temperature setting and the reason that that temperature setting is almost never set to zero in real-life use is because there also has to be an improvisational element-

**Interviewer** [51:27]: Sure

**Blaise Aguera Y Arcas** [51:27]: ... so that you don't have something that feels dead.

**Interviewer** [51:31]: But could I, could I just-

**Blaise Aguera Y Arcas** [51:32]: Yeah. No, absolutely

**Interviewer** [51:32]: ... I mean, prediction is also, like, prediction among multiple possible counterfactuals.

**Blaise Aguera Y Arcas** [51:36]: Right.

**Interviewer** [51:36]: It's not necessarily a line- a, a one-to-one thing. And also there's way-

**Blaise Aguera Y Arcas** [51:39]: Of course

**Interviewer** [51:39]: ... I mean, you mentioned computational neuroscience, but the whole predictive processing paradigm within neuroscience, you know, suggests that, you know, the dynamics of prediction is, is-

**Blaise Aguera Y Arcas** [51:47]: What brains are for

**Interviewer** [51:47]: ... is what brains are for, right?

**Blaise Aguera Y Arcas** [51:48]: Yeah.

**Interviewer** [51:48]: And so prediction, you know, we are all stochastic parrots on a cert- on a certain sort of level. But I mean, this is another way of thinking about prediction not necessarily as something that is, you know, about just infinite-

**Blaise Aguera Y Arcas** [51:58]: Yeah

**Interviewer** [51:58]: ... infinite closed-loop recursion.

**Blaise Aguera Y Arcas** [51:59]: It, it is. And, and this, this is, this is kind of the, the, the crux of the connection between-

**Interviewer** [52:03]: Mm

**Blaise Aguera Y Arcas** [52:03]: ... the what is life and what is intelligence parts of the big book. So there's been this idea, you know, for a long, long time that the reason we have brains is to do next token prediction, essentially. [laughs]

**Interviewer** [52:11]: [laughs]

**Blaise Aguera Y Arcas** [52:11]: You know? Uh, you know, this idea dates back at least to Helmholtz-

**Interviewer** [52:14]: Mm-hmm

**Blaise Aguera Y Arcas** [52:14]: ... uh, you know, in the, in the 19th century. It was articulated super clearly by Norbert Wiener in the 1940s.

**Interviewer** [52:20]: Mm-hmm.

**Blaise Aguera Y Arcas** [52:20]: Father of cybernetics.

**Interviewer** [52:21]: Cybernetic theory, right.

**Blaise Aguera Y Arcas** [52:22]: Um, and the idea is, you know, if, if you want to act intelligently in the world, you need to basically predict how the world is gonna behave and, and ther- and, and therefore predict what effects your actions will have on it. Taking that a little further, you need to also predict yourself. So, uh, you know, even at, at the most basic level, I mean-

**Interviewer** [52:40]: Right

**Blaise Aguera Y Arcas** [52:40]: ... the most basic kind of prediction is a thermostat.

**Interviewer** [52:41]: Theory of mind, right. Mm-hmm.

**Blaise Aguera Y Arcas** [52:43]: Right.

**Interviewer** [52:43]: Mm-hmm.

**Blaise Aguera Y Arcas** [52:43]: If you're warm-blooded, you need to maintain your- [laughs]

**Interviewer** [52:45]: Right

**Blaise Aguera Y Arcas** [52:45]: ... you know, your own temperature, right? At the same way you are a thermostat.

**Interviewer** [52:47]: Right. What stage are we at? Are we at the, you know, kind of PalmPilot level, the Newton level? Where, where are we at, you know, technologically, and then what happens when we get to the quantum level? I mean, aside from quantum woo and, and your theories about the microtubules and whatnot, uh, the brain-

**Blaise Aguera Y Arcas** [53:00]: They're not my theories about the microtubules. [laughs]

**Interviewer** [53:01]: People say your theories on them. I would say not, not of them.

**Blaise Aguera Y Arcas** [53:05]: My theory that it's not a theory.

**Interviewer** [53:06]: Of... [laughs]

**Blaise Aguera Y Arcas** [53:07]: [laughs]

**Interviewer** [53:08]: Uh, but let's, let's, let's get into that. So where, where, where are we at? What generation are we at, and what... Do some future casting. Where is this gonna go with quantum computers? If, if anything. I mean, maybe it won't have any impact.

**Blaise Aguera Y Arcas** [53:18]: When I first began talking about quantum computing s- seriously with my colleague Hartmut Neven, who runs that, that program at Google, you know, he had some ideas, and I, I thought they were very exciting, that we might be able to use quantum computing to train AI. That, you know, quantum AI might be a big thing. I, I don't think that's the case. You know, one of the surprises in a way about the kind of optimization that powers AI is that it looks quite convex. And-

**Interviewer** [53:40]: Mm

**Blaise Aguera Y Arcas** [53:41]: ... what quantum computing is good at is finding minima in a pin cushion. You know, where you have lots and lots of-

**Interviewer** [53:46]: Local

**Blaise Aguera Y Arcas** [53:47]: ... of, of local minima that have very thin energetic walls between them-

**Interviewer** [53:50]: Yeah

**Blaise Aguera Y Arcas** [53:50]: ... that can be tunneled through, uh, by, by, by quantum.

**Interviewer** [53:52]: Quantum, mm-hmm.

**Blaise Aguera Y Arcas** [53:54]: Right. And that doesn't help you if your landscape, you know, is, is smoother.

**Interviewer** [53:57]: Mm-hmm.

**Blaise Aguera Y Arcas** [53:57]: I think that the landscapes of AI that we've seen have a smoothness that implies-

**Interviewer** [54:02]: Is that because they're mirroring the human brain, and the human brain, like we, we just are not good at, you know, at, at kind of splitting the middle, as the Yiddish proverb goes. You know-

**Blaise Aguera Y Arcas** [54:10]: Right

**Interviewer** [54:10]: ... if you split, stand in the middle of the road, you get hit by traffic on both sides. So people cleave to, you know, uh, gun control for all, or everyone should have a, you know, anti-tank missile at their, at their house. Or abortion for all, and nobody should ever have an... We're not good at making, you know, kind of subtle superposition choices, right? Uh-

**Blaise Aguera Y Arcas** [54:24]: That's true. Mm

**Interviewer** [54:25]: So i- is that then leading just the AL... Sorry, the LLM plus GPU into this, you know, phase space, but that's not actually the best for people like me that care about new laws of physics that might be extremely, you know, non, you know, non-convex or, [laughs] or however you want to say it, cuspy.

**Blaise Aguera Y Arcas** [54:40]: I don't know.

**Interviewer** [54:41]: Mm-hmm.

**Blaise Aguera Y Arcas** [54:41]: But my guess is that, you know... And, and this is based, based on a bunch of findings about theoretical machine learning and overparameterization, is that growing more parameters at your model is a way of smoothing the space.

**Interviewer** [54:53]: Yes. I can see that.

**Blaise Aguera Y Arcas** [54:54]: You know, a way of making it less pin cushiony.

**Interviewer** [54:56]: Absolutely.

**Blaise Aguera Y Arcas** [54:56]: And that makes it more learnable and allows more generalization to, to happen. Um-

**Interviewer** [54:59]: Which then is a feedback because-

**Blaise Aguera Y Arcas** [55:01]: Exactly

**Interviewer** [55:01]: ... it makes it cheaper and make it more efficient, right.

**Blaise Aguera Y Arcas** [55:02]: Exactly. So I th- I think it's more fundamental than-

**Interviewer** [55:05]: Mm-hmm

**Blaise Aguera Y Arcas** [55:05]: ... than, than, you know, than the things that you're-

**Interviewer** [55:06]: Interesting

**Blaise Aguera Y Arcas** [55:07]: ... the psychol- the more psychological things you're talking about.

**Interviewer** [55:08]: Do, do you have kids?

**Blaise Aguera Y Arcas** [55:10]: Yes, two.

**Interviewer** [55:10]: Okay. So how are they using it? How are they using AI? How, how, how are you raising them? And, and I think a lot of my audience have kids and are parents or parents to be. What, what role do you have AI play in your own just daily life? I mean, besides the fun that we both have with it, and Ben, I know Benjamin, you know, does, and he uses it for so many fascinating things. But, but where do you actually apply it for the next generation? And that'll lead into-

**Blaise Aguera Y Arcas** [55:32]: Yeah

**Interviewer** [55:32]: ... questions about education.

**Blaise Aguera Y Arcas** [55:33]: I think Benjamin and I probably have quite different experiences of this sort of. You know, I think Lu, Lu might be a bit more experimental with this sort of stuff. My own kids-

**Interviewer** [55:40]: He's more suspicious of, like

**Blaise Aguera Y Arcas** [55:41]: He's more suspicious of life.

**Interviewer** [55:42]: Yeah, yeah, yeah.

**Blaise Aguera Y Arcas** [55:43]: Well, my two are basically Amish. [laughs]

**Interviewer** [55:46]: [laughs]

**Blaise Aguera Y Arcas** [55:46]: You know? They, they, they just take the piss constantly, you know, out of me. Like, "Oh, dude, you're AI, you're AI bullshit."

**Interviewer** [55:52]: You're like a-

**Blaise Aguera Y Arcas** [55:53]: So-

**Interviewer** [55:53]: They're the doomers and-

**Blaise Aguera Y Arcas** [55:54]: I just get a lot of shade [laughs] from the two of them. They're very old-fashioned. They, you know, they have, like, their phones set to the black and white mode.

**Interviewer** [56:03]: Wow.

**Blaise Aguera Y Arcas** [56:03]: You know, they're real, you know, I-

**Interviewer** [56:04]: Can I talk to my kids, like... Can we do a play date while you're here this week?

**Blaise Aguera Y Arcas** [56:08]: Exactly.

**Interviewer** [56:08]: [laughs]

**Blaise Aguera Y Arcas** [56:08]: You know, I mean, to be clear, like, they, they never, you know-

**Interviewer** [56:11]: Not liquid glass. I mean

**Blaise Aguera Y Arcas** [56:11]: ... they always had full access to the uncensored internet and whatever devi- you know, like we never imposed any limits-

**Interviewer** [56:17]: Oh

**Blaise Aguera Y Arcas** [56:17]: ... on the-

**Interviewer** [56:17]: So it's like the parents that give their kids wine-

**Blaise Aguera Y Arcas** [56:19]: ... the country's self-generated

**Interviewer** [56:19]: ... at dinner time. Yeah, exactly.

**Blaise Aguera Y Arcas** [56:20]: Exactly.

**Interviewer** [56:20]: And then they grow up alcoholics.

**Blaise Aguera Y Arcas** [56:20]: And they become tea-totalers.

**Interviewer** [56:21]: Right, exactly. [laughs]

**Blaise Aguera Y Arcas** [56:22]: So that's what's happened.

**Panelist** [56:23]: My son's been using AI models since they started. I mean, I just sort of sat him down and sort of-

**Interviewer** [56:28]: Yeah, mine too

**Panelist** [56:28]: ... showed him on the, on, on all of this as well. I, I think for him, he's now j- just finished junior year in high school.

**Interviewer** [56:33]: Yeah.

**Panelist** [56:34]: It, it's, it's almost kind of no big deal. Okay, that's just how it works.

**Interviewer** [56:37]: Mm-hmm.

**Panelist** [56:37]: Like, you know, you can have these long conversations and it'll figure things out-

**Interviewer** [56:40]: Yeah

**Panelist** [56:40]: ... and you can use it for these sorts of way as well. He's been doing a lot, actually a fair bit of work on the thinking about AI in education because of sort of under- like the fact that all of his teachers, like, have no idea what any of this is about.

**Interviewer** [56:52]: Right, right.

**Panelist** [56:52]: In other words, it's, it's kind of no big deal.

**Interviewer** [56:54]: Mm-hmm.

**Panelist** [56:54]: And therefore he's surprised that people are so alarmed by it, but also to a certain extent people are so enthusiastic by it as well.

**Interviewer** [57:00]: It's, it's, it's, to me, you know, when you look at things, self-driving cars and all those things are, yes, they're, they're gonna have a huge impact, but, but the c- the concept of not, not using it, again, I feel like it's a form of malpractice. Like if I-

**Blaise Aguera Y Arcas** [57:12]: Yeah

**Interviewer** [57:12]: ... I told my students not to-

**Panelist** [57:13]: Well, just, just think of like image, think of like what you could do with all the parking space if you don't have to-

**Interviewer** [57:17]: Oh, yeah

**Panelist** [57:17]: ... if you just seriously-

**Interviewer** [57:18]: No, no, absolutely

**Panelist** [57:18]: ... the potential impact of like carbon transportation-

**Interviewer** [57:20]: Yeah, yes

**Panelist** [57:20]: ... and service.

**Interviewer** [57:21]: Just climate, everything else, right.

**Blaise Aguera Y Arcas** [57:22]: Right, right.

**Interviewer** [57:22]: But, but in, in particular in educate... Like my students, we, when I flip the classroom around and I have them solve problems and I walk around and we look at data from the, you know, cosmology experiments or particle physics experiments, I just dump data on them. And they're like, "Well, what do I do?" Even like visual things, like I, I had a wave tank and I gen- and we were generating some waves, and I was asking, "Well, compute the wavelength just based on anything that you have on you right now," and that includes ChatGPT. Take a picture of it, the interferogram, and tell me about the frequency at which these things are working and the, knowing the water temperature, the... And you know, they were like, "What? We can u- that's like cheating. Like we..." I'm like, "It's not even a quiz. It's, it's just I want you to understand how interference patterns work and, and we can then talk about double slit."

**Panelist** [58:02]: So you encourage them to use models?

**Interviewer** [58:03]: I was... Uh, n- no, I made them use it.

**Panelist** [58:05]: Oh, yeah. I, me, me too.

**Interviewer** [58:05]: And, and actually, I do-

**Panelist** [58:06]: Sometimes they get it wrong

**Interviewer** [58:07]: ... I, I make an assignment, you have to learn how to use it and figure out what, how to use it. I think if we don't do that-

**Panelist** [58:11]: I agree

**Interviewer** [58:12]: ... as professors, we're gonna be like a malpractice doctor that doesn't use AI to diagnose a, a smudge on a... 'Cause they're so much better at doing certain things. So tell me, where is it, what's your perspe- I mean, we're, we're, you know, members of the academy and the, you know, stodgy, we have our tweed jackets and our whatever it is, our suede patch. A suede jacket with a tweed patch, I was very-

**Blaise Aguera Y Arcas** [58:29]: I don't have suede patch

**Interviewer** [58:29]: ... accepting of the act. [laughs]

**Panelist** [58:30]: I forgot, I forgot my pipe.

**Interviewer** [58:31]: Exactly. [laughs] I just want to know we're in the faculty club lunch buffet, so.

**Blaise Aguera Y Arcas** [58:35]: Yeah. [laughs]

**Interviewer** [58:35]: But Blaise, what, what are the opportunities? What is Google looking... I mean, Google has my, my mail, it has my calendar, has, you know, my photos. It has so much information. I don't feel like it's being used, and I'm not, I know this is not your domain specifically, but what are the, what are the, what's the potential for just life enhancement and, and flourishing of a modern technological society, given that I've been on Gmail and you've probably been on it, you have a Google, you know, account. But tell me, it has 20 years of your, of your conversations and probably your fir- when your kids were born-

**Blaise Aguera Y Arcas** [59:04]: Yeah

**Interviewer** [59:04]: ... and all these wonderful... What are you excited about? What can it do for, you know, other people's kids that care more about it than maybe yours? [laughs]

**Blaise Aguera Y Arcas** [59:10]: Exactly. Yeah, it's a great question. I mean, I mentioned earlier that, that the people who, you know, statistically have the most anxiety about this stuff are the ones who use it the least. I know there are exceptions.

**Interviewer** [59:20]: Yeah.

**Panelist** [59:20]: Which is why it's important for students to use it.

**Blaise Aguera Y Arcas** [59:22]: Which is, yes. And the other thing that we see, and, and this is all from a, a, a study that Ipsos did together with Google a couple of months ago that I thought was very revealing. The other big trend is that less economically developed countries, way more optimistic about AI than Europe and the US.

**Interviewer** [59:37]: It's kind of like they skipped the landline phase.

**Blaise Aguera Y Arcas** [59:39]: Exactly.

**Interviewer** [59:39]: Now they're just straight to AI.

**Panelist** [59:40]: Yeah, they see it as a leapfrogging.

**Blaise Aguera Y Arcas** [59:41]: Yeah. They s-

**Panelist** [59:41]: They say, "Oh," yeah.

**Blaise Aguera Y Arcas** [59:42]: They're very optimistic.

**Interviewer** [59:43]: It's huge leverage.

**Blaise Aguera Y Arcas** [59:44]: And, and-

**Interviewer** [59:44]: And a force multiplier.

**Panelist** [59:45]: It's a massive intellectual transfer.

**Blaise Aguera Y Arcas** [59:47]: That's right. So you know, if, if, so looking at it from a, from the perspective of education, for instance, you know, we can have all kinds of hand-ringy conversations-

**Interviewer** [59:55]: Mm

**Blaise Aguera Y Arcas** [59:55]: ... about, you know, about AI and education, you know, at UCSD or, or at University of Chicago or Princeton or whatever. You know, if, if you're in Burkina Faso, like this is a, a, a life changer.

**Interviewer** [60:06]: Right.

**Blaise Aguera Y Arcas** [60:06]: Right? And I think a lot of people in the developing world, you know, realize that and are already, you know, uh, starting to make heavy use of these things. Are they perfect? Of course not. You know, they have all kinds of issues. But when it makes such an enormous difference relative to not having, you know, trained teachers-

**Interviewer** [60:21]: Mm-hmm

**Blaise Aguera Y Arcas** [60:22]: ... anything like tutors, the resources to get all these things, you know, it's, it's, it's, there, it's just, it's unambiguous.

**Interviewer** [60:27]: Mm-hmm.

**Blaise Aguera Y Arcas** [60:28]: So I don't want to discount the importance of having conversations like how should it be used in the classroom? Like what happens when a bunch of kids come in-

**Interviewer** [60:36]: And how should it be-

**Blaise Aguera Y Arcas** [60:36]: ... with an assignment that have all just like c- you know, copied and pasted-

**Interviewer** [60:39]: Yeah

**Blaise Aguera Y Arcas** [60:39]: ... you know? Like obviously-

**Panelist** [60:39]: You're right

**Blaise Aguera Y Arcas** [60:40]: ... that's, obviously there's something broken happening there.

**Interviewer** [60:42]: Mm-hmm.

**Blaise Aguera Y Arcas** [60:43]: I, where, where it's broken and how it's broken, I think we're figuring out.

**Interviewer** [60:45]: Yeah.

**Blaise Aguera Y Arcas** [60:46]: But let's also, you know, not be confused about what a rich person's problem that is-

**Interviewer** [60:50]: Right

**Blaise Aguera Y Arcas** [60:51]: ... in effect. [laughs]

**Interviewer** [60:51]: Exactly right, and doomed societies not to because of our own mores.

**Panelist** [60:54]: But also understanding like the reason you get those kinds of outcomes is because you haven't actually done the work to figure out-

**Blaise Aguera Y Arcas** [61:00]: The whole entire point

**Panelist** [61:00]: ... how to use it properly.

**Interviewer** [61:01]: Mm-hmm.

**Blaise Aguera Y Arcas** [61:01]: Exactly.

**Panelist** [61:02]: You know, I'm actually on a faculty-

**Interviewer** [61:03]: Yeah

**Panelist** [61:03]: ... committee here at UCSD trying to figure out some of these things. And you'd be surprised at the systems-

**Blaise Aguera Y Arcas** [61:08]: At some of the opinions that are-

**Interviewer** [61:09]: Yeah

**Panelist** [61:09]: ... in there. But the, but I mean, s- we got to put be- better assignments.

**Interviewer** [61:12]: Yeah.

**Panelist** [61:12]: So you have to presume-

**Interviewer** [61:13]: Exactly

**Panelist** [61:13]: ... that this is, that this is, you know, like-

**Interviewer** [61:15]: That's right

**Panelist** [61:15]: ... high school students have calculators.

**Interviewer** [61:16]: Just tell them their prom-

**Panelist** [61:18]: So you teach, you teach calculus differently.

**Interviewer** [61:18]: Their prompts suck.

**Blaise Aguera Y Arcas** [61:18]: Yeah, exactly right.

**Panelist** [61:19]: Yeah, but prompt-

**Interviewer** [61:19]: You could do it with anything. You can do it with calculus, right? I mean-

**Panelist** [61:22]: But prompt casting, prompt crafting as-

**Interviewer** [61:24]: Yeah

**Panelist** [61:24]: ... a sort of a interdisciplinary-

**Interviewer** [61:24]: It is a skill.

**Panelist** [61:25]: Absolutely.

**Interviewer** [61:25]: I just talked to my daughter. My wife's very much in the, sounds like your kids, she's very much against it except when I'll say like, "Well, here's a picture of the inside of our fridge and, you know, I'm getting hungry in about two hours, you know, what can I make for you, darling?" And then all of a sudden, wow-

**Blaise Aguera Y Arcas** [61:38]: But suddenly it's okay. [laughs]

**Interviewer** [61:39]: ... like this stuff. It's like the, the, great. But when we're looking at, you know, kind of the, the, the potential for what we can do and what we can use it for, and really tailoring it. My daughter- ... she was, um, I, I made a jingle for the, uh... Actually, we're gonna do this now. Actually, I forgot to do this, but we're gonna do it. We have a segment on the show called Judging Books By Their Covers, where we take the book's cover and its title and its subtitle, and we ask the author to judge it for us, because without any other prior information, what can we do? Now, this one's not probably the one that we wanna go into, 'cause it's not, not so, not so information dense, but we'll do it with this one. The reason I bring it up is because right as I say now, we're gonna judge books by their covers, I made a jingle using Sona, So- Sora or Sona? I get those two confused.

**Panelist** [62:22]: Sora's the video model-

**Interviewer** [62:23]: And-

**Panelist** [62:23]: ... OpenAI

**Interviewer** [62:24]: ... yeah, Sora, Sona, I think, right? Is the audio. Makes sense. Sonar, right? So we'll do it for this book. But before, I, I did it and my daughter was listening, and she was... She's nine years old, and she, she, you know, was kind of cute, "Oh, I wanna do that." And so I said, "Okay, well, what do you wanna write about? And, like, what kind of style do you wanna use?" And she's like, "Oh, I wanna do it like Dua Lipa," you know, kind of that style, and, "I wanna do this." And then we put it into there and it said, "Forbidden term." You can't use an actual artist, you know, a style.

**Panelist** [62:47]: Yeah.

**Interviewer** [62:47]: You have to s- you know, describe it in words. You can't use any name. You know, Taylor Swift, you can't use their style. You can't ask the model to do that. It's like violating copyright.

**Panelist** [62:55]: Yeah.

**Interviewer** [62:55]: So my daughter learned prompting, right? She learned, "Oh, I can't do that, so I have to get around it, so let me describe it as, you know, highly, you know, buoyant," whatever she did. You know, bubbly and happy. And then she, she did, and she got her own jingle for something else. But now let's judge this book by its cover.

**speaker_3** [63:09]: Hey, book lovers. We're judging books by their covers. We know we're not supposed to do it. But into the impossible, there's nothing to it. Let's take a look and judge some books

**Blaise Aguera Y Arcas** [63:22]: Okay. The title is Who Are We Now? The cover looks kind of retro. It's got a sort of collage of images. Uh, one of them is of The Jetsons. One of them is of a skull being measured with a craniometer. Uh, one of them is of two scissors, one left-handed and one right-handed. There is a pyramid called System of Patriarchy, that's got God on top and Earth on the bottom, with, with a kind of hierarchy with an eye at the top of the pyramid. God, men, women, children, animals, plants, Earth. And there is a bi-identification card. There's also a picture of a human ear modeled and drawn by Mr. Woolner, with the projecting point highlighted as letter A. So that's what's on the cover.

**Interviewer** [63:59]: Okay.

**Blaise Aguera Y Arcas** [64:00]: I have no idea [laughs] what the, what an AI that, that doesn't know about, about the book will make of that at a time.

**Interviewer** [64:06]: What's the, the title meant to evoke? It's, it's sort of this, the confluence of man and machine as your perspective evolved from 2016 to 2022.

**Blaise Aguera Y Arcas** [64:14]: Mm-hmm.

**Interviewer** [64:14]: Very good. Okay. So we're gonna go into a couple of short topics in just a minute. But before that, I cannot, uh, fail to ask you about computronium.

**Blaise Aguera Y Arcas** [64:22]: Mm.

**Interviewer** [64:22]: What is that? What is a computronium?

**Blaise Aguera Y Arcas** [64:24]: Okay. Well, the word was, I believe, coined by Norman Margolis, physicist and computer scientist working on this in the '80s and '90s. His definition of it was a cellular automaton or, or, or some kind of, of, um, a highly local form of computation that would be as efficient as matter can be-

**Interviewer** [64:40]: Mm

**Blaise Aguera Y Arcas** [64:40]: ... at computation. I have a somewhat broader definition of computronium, which is that it is a state of matter that computes. So, you know, just as we talk about, you know, gases, liquids, solids-

**Interviewer** [64:51]: Mm

**Blaise Aguera Y Arcas** [64:51]: ... I think there is another state of matter that is maybe the most important one to us that we don't have a name for-

**Interviewer** [64:56]: [laughs]

**Blaise Aguera Y Arcas** [64:57]: ... which is what we're made out of-

**Interviewer** [64:58]: Mm-hmm

**Blaise Aguera Y Arcas** [64:58]: ... uh, and also what machines are made out of. Uh, and I would call that computronium, because I think that its key functional property is that it computes, and its key statistical property is that unlike all of those other states of matter, it doesn't have either the kind of totally random statistics of a gas, nor does it have the sort of, you know, locally ordered but essentially uniform statistics of something like a li- like a liquid or, or a solid. Uh, it has self-dissimilar multifractal sort of statistics, meaning, you know, it's different at every scale, and it's made out of, out of parts that are, that are distinct.

**Interviewer** [65:32]: Mm-hmm.

**Blaise Aguera Y Arcas** [65:33]: And, and, and that's true kind of recursively.

**Interviewer** [65:35]: Sam Altman has proposed in the future you'll be given a, an amount of universal basic compute. How does this play into that? So we're born with a certain amount. Some we can cultivate, presumably.

**Panelist** [65:46]: So that's also an old, old-

**Interviewer** [65:47]: Cult- computation

**Panelist** [65:47]: ... it's an old, old idea.

**Interviewer** [65:48]: Yeah, I'm sure. Yeah.

**Panelist** [65:49]: It's not Sam's idea.

**Interviewer** [65:49]: Right. Yeah.

**Panelist** [65:50]: [laughs]

**Interviewer** [65:50]: I'm sure there's some science fiction movies about this, too, right? Uh, Arthur C. or Isaac Asimov or Clark. Where do you come down on that? What, what is your orientation towards, as a natural right, comp- computation as sort of an, you know, an inheritance that, that we're all owed but we can also cultivate and, and grow on our own with through our own merit perhaps?

**Blaise Aguera Y Arcas** [66:07]: I don't know. I don't know what the future economy should look like. I'm pretty sure that it's gotta look different from the way it looks now. I believe I'm with Sam and with many other people who think about this stuff in, in, in believing that given that our society, our global human civilization, right, is at this point well above the wealth threshold where everybody could have secure housing, food, medical care-

**Interviewer** [66:29]: Right

**Blaise Aguera Y Arcas** [66:29]: ... education. It is a crime that-

**Interviewer** [66:31]: Mm

**Blaise Aguera Y Arcas** [66:31]: ... that that's not something that we, you know, that we can all rely on.

**Interviewer** [66:34]: Mm-hmm.

**Blaise Aguera Y Arcas** [66:35]: That, that just seems like a moral failing. You know, how does that work? And, and, and how do- how does, how does the tension stay in the system that makes interesting stuff happen is an unsolved problem-

**Interviewer** [66:44]: Mm-hmm

**Blaise Aguera Y Arcas** [66:45]: ... in, in my opinion. So I don't know whether-

**Interviewer** [66:47]: But, but-

**Blaise Aguera Y Arcas** [66:47]: ... you know, free computing [laughs] you know, is the answer to that. And I'm not sure about rights. I think it's more complicated than, than... I, I don't think there's a god's-eye view that says everybody has such and such rights. I think this is more of a, of a social contract for mutual-

**Interviewer** [66:59]: Mm

**Blaise Aguera Y Arcas** [66:59]: ... flourishing.

**Interviewer** [66:59]: And Ben, do you foresee a future of the haves and have-nots that would be of concern-

**Panelist** [67:04]: Oh

**Interviewer** [67:04]: ... from a moral philosophy perspective?

**Panelist** [67:05]: Yeah, of course.

**Interviewer** [67:06]: And, and, okay. So-

**Panelist** [67:06]: Yeah. I mean, I should say, I mean, the universal basic com- U- UBC is-

**Interviewer** [67:09]: Yeah

**Panelist** [67:10]: ... you know, variation on the... I mean, the way it's phrased, right, obviously it's a variation on universal basic income, uh, or as a-

**Interviewer** [67:15]: Yeah

**Panelist** [67:15]: ... sort of older sort of idea, which is, y- you know, and probably is an improvement on this in the sense to which one of the things that digital economies do is they reduce the marginal cost for the production of durable goods, which means that the tr- that having cash to purchase durable goods is actually not the thing that you're... the most logical thing. What you need is something more universal basic services or-

**Interviewer** [67:36]: Mm

**Panelist** [67:36]: ... universal basic access or-

**Interviewer** [67:37]: Mm

**Panelist** [67:37]: ... universal basic agency. And compute in, in some ways arguably is a reasonable index for many of those kinds of things. Maybe. It can be under certain circumstances, yes. I mean, in terms of the AI and the, and the haves and have-nots, like, uh, uh, again, I'm, I really I, I think this can go in a lot of different directions, right? And, and also I think to a certain extent, some of the ways in which some of my colleagues sort of insist on defining the, the present and future state in, in starkly, uh, let's say critical terms, actually has, in a certain degree, a kind of self-fulfilling capacity where it becomes difficult to convince them that in fact there are other possibilities that, that maybe need to be emphasized. Let me put it sort of this way. Like, if I were to tell you that there was a, a hypothetical machine, and this hypothetical machine c- took and consolidated all of the professional knowledge, expertise, and agency that has been made artificially scarce and consolidated, not just in the global north, but in 12 cities and 22 universities-

**Interviewer** [68:40]: Right

**Panelist** [68:40]: ... in the global north-

**Interviewer** [68:41]: Mm-hmm

**Panelist** [68:42]: ... and jealously protected in this place, but that this, it, that this machine would essentially provide a kind of massive agency and knowledge transfer that would be available to everybody in the world through devices and interfaces they already understand in every language for a sub- monthly subscription fee equivalent to Netflix or free. It would be hard to argue that this wouldn't h- this, this, in principle, wouldn't have at least the strong potential for a kind of revolutionary disruption in dismantling that artificial scarcity, which is-

**Interviewer** [69:12]: Mm

**Panelist** [69:12]: ... you know, maybe bad for the Ivy League, but-

**Interviewer** [69:15]: Right

**Panelist** [69:15]: ... boo-hoo. But what it, it... There's not the sort of guarantee that any of this sort of work, that this would sort of work in, work in this kind of, that would work in this, in this kind of direction here as well. But I think this, in a certain sense, is, is like the, the vision that we would want to cultivate. And why is that? Not even necessarily from a kind of first principles moral philosophy, you know, Rawlsian ethics or something, but just because, just for principles of collective intelligence, that if you have, you know, eight billion, you know, human-level human minds-

**Interviewer** [69:43]: Yeah

**Panelist** [69:43]: ... as opposed to AI-

**Interviewer** [69:44]: Yeah

**Panelist** [69:44]: ... you know, AI human-level minds, and that for s- that w- we are, as a species, you know, just not benefiting from the full participation-

**Interviewer** [69:52]: Right

**Panelist** [69:52]: ... and creativity and agency and, and ingenuity of, of sort of, of-

**Interviewer** [69:57]: That collective, yeah

**Panelist** [69:58]: ... all of these sort of, all of these sort of people-

**Interviewer** [70:00]: Mm-hmm

**Panelist** [70:00]: ... to sort of unlock this. That's the intelligence explosion that we should be pushing for.

**Interviewer** [70:05]: Yeah.

**Panelist** [70:05]: And so th- that's not a prediction.

**Interviewer** [70:07]: No.

**Panelist** [70:07]: It's not a sort of th- But in terms of like where do we, like what is the, you know, what is essentially a kind of goal states? What is the, we should be sort of steering this towards? I think this, this would... Now, does that constitute or presuppose some degree of universal compute access for everyone? It probably would. Whether or not that's, you know, uh, this doesn't mean this is instituted by some sort of New World Order global super state.

**Interviewer** [70:30]: [laughs] Digital currency backed.

**Panelist** [70:31]: You know, or Sam Altman-

**Interviewer** [70:32]: Mm-hmm

**Panelist** [70:32]: ... or, or on a blockchain or any of these kinds of things. But I think the presumption is if the goal is to use these technologies for the-

**Interviewer** [70:38]: Flourishing of-

**Panelist** [70:38]: ... un- unlocking of, of the collect- the collective intelligence that has been henceforth suppressed by c- historical legacy-

**Interviewer** [70:45]: Mm-hmm

**Panelist** [70:46]: ... it would require something like that, yes.

**Interviewer** [70:49]: Blaze, can't thank you enough for being down here. Everyone should pick up the copy of this book. Where should people be in touch with you? Anything else you'd like people to know about this wonderful new book and your corpus of knowledge and future projects? What's next on the horizon after this? A well-deserved vacation, I hope. [laughs]

**Blaise Aguera Y Arcas** [71:03]: Yes. I, I thank you so much for asking. I'm definitely not working on another, another book now. I've, I've written one a year for the past [laughs] several years, so I think I'm, you know, I'm good for a little bit. But yeah, I c- I'm, I'm easy to find, you know, on, on, like probably LinkedIn is the easiest, um-

**Interviewer** [71:16]: Okay. Benjamin, it's always nice to have such brilliant colleagues as you, and I hope we can do this more often-

**Panelist** [71:21]: Anytime you like. I'm very happy to see you again

**Interviewer** [71:21]: ... with more, um, but just keep sending me wonderful guests like Blaze. I really can't thank you enough.

**Panelist** [71:26]: Thank you. My pleasure.

**Interviewer** [71:26]: All right.

**Blaise Aguera Y Arcas** [71:27]: This has really been a pleasure. Thank you for having me on.

**Interviewer** [71:28]: Thank you so much for coming down. The question of whether AI can truly experience the world the way that we do is just the beginning. If you're fascinated by how intelligence emerges from the fundamental building blocks of reality, check out my episode with Sarah Walker, where we dive deep into assembly theory and what that really means for matter to become alive and aware. The connection between physics, biology, and consciousness run deeper than even I ever would have expected. Don't forget to like, comment, and subscribe. Hey, everybody. I'm usually the one that asks my guests to judge their books by their covers, but today I'm asking myself to judge my own book by its cover. My newest book, Focus Like a Nobel Prize Winner, is chock-full of advice, life tips, and focus and productivity tips from nine of the world's greatest minds, Nobel laureates ranging from economics to peace to physics, of course. It launches September ninth, which is also my birthday. [upbeat music] So go to Amazon and get the Kindle copy today.

