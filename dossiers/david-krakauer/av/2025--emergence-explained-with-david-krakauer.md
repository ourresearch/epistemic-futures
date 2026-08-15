---
title: "Emergence Explained with David Krakauer"
person: david-krakauer
section: by
type: talk-transcript
year: 2025
venue: "YouTube"
source_url: https://youtu.be/wGhRW-pJWIc
retrieved: 2026-08-14
content: full-text
transcription:
  method: asr
  asr_model: elevenlabs-scribe_v2
  diarized: true
  speaker_labels: inferred   # ASR diarization + LLM naming (claude-sonnet-4-6); not ground truth
  duration_min: 59
notes: "PROVENANCE: machine-transcribed from AV via ElevenLabs Scribe v2 (diarized) + LLM speaker-naming pass. Speaker labels are inferred, not authoritative. Layer-2 (mildly lossy) per charter, not camera-raw."
---

# Emergence Explained with David Krakauer

*Speakers (inferred):* speaker_0=David Krakauer, speaker_1=Chuck Nice, speaker_2=Interviewer, speaker_3=Gary O'Reilly

## Transcript
**David Krakauer** [00:00]: So the first thing I want to say is that AIs have no intelligence, but they have tons of capability. And the problem with a lot of AI at the moment is it's basically fake intelligence.

**Chuck Nice** [00:08]: It's very quick lookup. It's really just-

**David Krakauer** [00:10]: It's essentially a really clever lookup. What is intelligence? Intelligence is basically someone or something that makes a hard problem easy. If you went to school and you're sitting down trying to work out a problem, you look over at the person next to you, and they've made a problem look effortless, you'd say, "Oh my God, that's pretty intelligent."

**Interviewer** [00:28]: No, no, no, you're the intelligent one looking over the shoulder-

**Chuck Nice** [00:31]: Right

**Interviewer** [00:31]: ... 'cause you got the answer easier than they did.

**Chuck Nice** [00:33]: Yeah.

**Interviewer** [00:38]: [laughs] This is StarTalk: Special Edition, which means I got Gary O'Reilly sitting right next to me.

**Gary O'Reilly** [00:46]: Hi, Neil.

**Interviewer** [00:46]: Gary, former soccer pro.

**Gary O'Reilly** [00:48]: Yes.

**Interviewer** [00:49]: Chuck Nice.

**Chuck Nice** [00:49]: Yeah.

**Interviewer** [00:49]: Good to have you, man.

**Chuck Nice** [00:50]: Who knows nothing about soccer.

**Interviewer** [00:52]: [laughs]

**Chuck Nice** [00:53]: Nothing.

**Interviewer** [00:53]: That's 'cause you're American. [laughs]

**Chuck Nice** [00:55]: That's, that's right.

**Interviewer** [00:57]: [laughs]

**Chuck Nice** [00:57]: 'Merica, baby.

**Interviewer** [00:58]: So you guys always come up with fun topics.

**Gary O'Reilly** [01:02]: Mm.

**Interviewer** [01:02]: And today is no exception.

**Gary O'Reilly** [01:04]: Yeah, um-

**Interviewer** [01:05]: Yeah, complexity.

**Gary O'Reilly** [01:07]: Yes.

**Interviewer** [01:07]: Oh my gosh.

**Chuck Nice** [01:08]: Mm.

**Interviewer** [01:08]: Complexity.

**Chuck Nice** [01:09]: Yes.

**Gary O'Reilly** [01:10]: Yeah.

**Interviewer** [01:10]: And I'm amazed-

**Chuck Nice** [01:10]: Can you simplify

**Interviewer** [01:11]: ... this is our first time we've ever handled this subject.

**Gary O'Reilly** [01:13]: It's been one we've been waiting to find the right guest-

**Interviewer** [01:18]: Oh

**Gary O'Reilly** [01:18]: ... to enter the arena.

**Interviewer** [01:20]: Okay.

**Gary O'Reilly** [01:21]: And, uh, guess what? We have.

**Interviewer** [01:23]: We have. [laughs] All right.

**Gary O'Reilly** [01:25]: I mean, I-

**Interviewer** [01:25]: Take us there

**Gary O'Reilly** [01:26]: ... let me frame it this way. As we come to grips with the reality of the lives we live, I ask myself, is there anyone out there considering the complexity of everything?

**Chuck Nice** [01:40]: Mm.

**Gary O'Reilly** [01:41]: Right? Asking the big questions. How did intelligence evolve in the universe? Does intelligence have limits? How do ideas evolve? Are there laws of life? And then here, the, the biggie, what is life?

**Chuck Nice** [01:58]: Oh, yeah.

**Gary O'Reilly** [01:59]: Right? So happy to say there isn't just one individual, but an institution that's set to these tasks. Neil, if you would kindly introduce our guest.

**Interviewer** [02:09]: I, I would be delighted to. We've got with us David Krakauer. David, welcome to StarTalk.

**David Krakauer** [02:15]: Fantastic to be with you.

**Interviewer** [02:17]: Yeah, and you are president of the Santa Fe Institute in New Mexico. This is a world famous place where deep thinkers go. [laughs] And the question is-

**Gary O'Reilly** [02:29]: And die

**Interviewer** [02:30]: ... [laughs] that's what, do they ever come out, is the question.

**David Krakauer** [02:32]: That's right.

**Interviewer** [02:33]: So you are a, the William H. Miller Professor of Complex Systems. I'm impressed that that's even a title you can have.

**Chuck Nice** [02:41]: That's a great... Yes.

**Interviewer** [02:42]: A, a comp- pr- professor of complex systems.

**Gary O'Reilly** [02:45]: Imagine how big his door is just to get that name on there.

**Interviewer** [02:47]: I wanna be professor of simple systems. [laughs]

**Gary O'Reilly** [02:50]: Well, there are those.

**Interviewer** [02:52]: Uh, what else? You have a, a background in evolutionary theory, good, with also a background in computer science and math, so it sounds like you've got just the right pedigree for this. And I think w- if we have time, we'll get to that you're founder of the Interplanetary Project at the Santa Fe Institute. I only just now first heard of that, but we wanna get to the bottom of that as well.

**Chuck Nice** [03:14]: Hmm.

**Interviewer** [03:15]: So let me just lead off here. Uh, we've had a couple of guests on our show who have either spent time at the Santa Fe Institute or were on the faculty there, if that's the right way to say it. Uh, just, can you just remind everybody what the mission statement is of the Santa Fe Institute and, and what distinguishes it from any other place that believes they're having deep thoughts about the world?

**Chuck Nice** [03:39]: And can you simplify that into one sentence?

**Interviewer** [03:42]: [laughs] No.

**David Krakauer** [03:43]: Yeah.

**Chuck Nice** [03:43]: Yes.

**Interviewer** [03:43]: No, he's a complexity professor.

**Chuck Nice** [03:44]: Oh, that's right, that's right, that's right.

**Gary O'Reilly** [03:45]: Yeah.

**David Krakauer** [03:46]: Uh, but I'll tell you the mission, which is one sentence. It won't help, but it's, um, searching for order in the complexity of evolving worlds. That's the mission statement, and I guess this whole conversation is what does that even mean?

**Chuck Nice** [03:59]: Hmm.

**Interviewer** [03:59]: Which, which has its own bias 'cause you're presuming there is order within the complexity to begin with.

**David Krakauer** [04:05]: Absolutely. I, and I assume the fact that we're here having this conversation is some kind of evidence of that fact.

**Interviewer** [04:09]: Okay, okay. All right.

**David Krakauer** [04:11]: Yeah, so essentially the institute was founded in 1984 in the mountains of New Mexico. There's a reason we're here because of Los Alamos, and we can discuss that history 'cause it's sort of interesting actually. I think of us as the sort of more generative, optimistic, fissile material-

**Interviewer** [04:28]: [laughs]

**David Krakauer** [04:28]: ... in this part of the landscape.

**Interviewer** [04:30]: Just to remind people, Los Alamos, I mean, it's, it's, it's a national lab.

**David Krakauer** [04:33]: Right.

**Interviewer** [04:33]: Okay?

**David Krakauer** [04:34]: Right.

**Interviewer** [04:34]: And where nuclear reserves are kept and managed and, and overseen.

**Chuck Nice** [04:39]: Okay.

**Interviewer** [04:40]: Very important place.

**Chuck Nice** [04:41]: Mm-hmm.

**Interviewer** [04:42]: And it's not an accident that it's in the middle of fricking nowhere.

**David Krakauer** [04:44]: Right.

**Interviewer** [04:45]: Okay?

**David Krakauer** [04:45]: Yeah.

**Interviewer** [04:46]: You're not gonna, you're gonna, gonna put that in a city.

**Chuck Nice** [04:47]: Just in case of an accident-

**Interviewer** [04:48]: [laughs]

**Chuck Nice** [04:49]: ... it's in the middle-

**Interviewer** [04:50]: Yeah

**Chuck Nice** [04:50]: ... of fricking nowhere. [laughs]

**Interviewer** [04:52]: Yeah. Okay, so, so you have sort of a genetic history, overlapping history with-

**David Krakauer** [04:57]: Yeah

**Interviewer** [04:57]: ... um, Los Alamos.

**David Krakauer** [04:58]: Los Alamos.

**Interviewer** [04:59]: Mm-hmm.

**David Krakauer** [04:59]: Absolutely. In fact, it's sort of interesting that the, there's an interesting s- cultural history here. The founding president, George Cowan, he was a child prodigy, and he had worked very early with two people from your world. He'd worked with Eugene Wigner, who won the Nobel Prize for his work on symmetries applied to physics, and with Enrico Fermi.

**Interviewer** [05:20]: Mm-hmm.

**David Krakauer** [05:21]: And, um, very young-

**Interviewer** [05:21]: Famous for the Fermi paradox and other, among other things, yes

**David Krakauer** [05:24]: ... yeah, and, and many, among many other things. And so, um, in the, he then became eventually the director of research at Los Alamos. Um, in the 1950s, he was asked to give a talk at the Aspen Institute, which is kind of just down the road in Colorado, and he gave a talk on social entropy, right? So the notion of entropy, we're familiar with, you know, from physics that systems tend towards disorder, and he thought, well, maybe that's true of society.

**Chuck Nice** [05:51]: Hmm.

**David Krakauer** [05:52]: He gives the talk, and he flames out. No one understood what he was talking about. Is this a metaphor? Do you actually have something in mind mathematically? That was in the early '50s. 30 years elapsed, and you're thinking there's something wrong with the world. Where the social sciences and the natural sciences, the mathematical sciences are not communicating as they should be. And that's really the origin story. In the '80s, a group of rather illustrious people came together, several Nobel laureates, said, "What would it take to build an institute where we don't start with the divisions of departments and the divisions of knowledge, but we actually just kind of short-circuit them and have people compressed in a very high density in one place in the high desert?" And that's sort of the, the premise.

**Chuck Nice** [06:41]: I'm interested, Interplanetary Project. Like, I mean, 'cause this-

**Interviewer** [06:43]: Oh, yeah, where is that? Where-

**Chuck Nice** [06:44]: There's, there's a niche that needs scratching right now.

**Interviewer** [06:45]: Yeah, right there.

**Chuck Nice** [06:45]: Please. Yeah.

**Interviewer** [06:47]: Yes.

**David Krakauer** [06:47]: Okay. So given our perspective on how the world works, how the universe works, our belief, right, that life is probably universal, there's no evidence, but I think it's a reasonable assumption to make.

**Chuck Nice** [07:01]: Right.

**David Krakauer** [07:02]: What would it mean to have a theory of the universe or a festival of the universe that included not just physics, but economics and sociology and poetry and art and music, right? In other words, astrobiology, as Neil well knows, is dominated by physics. But if it's true, [laughs] right, that there's life elsewhere, there might be extraordinary sport, extraordinary music to be discovered on another planet. So we want you to expand the range of thinking about life in the universe to encompass all disciplines. And that's, again, that's the kind of spirit of SFI.

**Interviewer** [07:37]: Right.

**Chuck Nice** [07:37]: But are, are these really disciplines that are created by life, or are they our perception of our preeminence in life?

**David Krakauer** [07:52]: Yeah, that, I mean, that's a really deep question [laughs] that relates to consciousness-

**Interviewer** [07:55]: They're so deep, I don't understand it.

**Chuck Nice** [07:57]: Really? [laughs]

**Interviewer** [07:57]: What ... No, I mean-

**Chuck Nice** [07:58]: So, so here's what I'm saying

**Interviewer** [07:59]: ... if you find ano- if you find aliens and they play music, is that what you're saying or what?

**Chuck Nice** [08:02]: Yeah. My point is this: we think that that would happen because we do it.

**Interviewer** [08:07]: Oh, okay.

**Chuck Nice** [08:07]: Do you understand? So-

**Interviewer** [08:08]: That's an interesting bias

**Chuck Nice** [08:09]: ... we, we, we have a, we have a-

**David Krakauer** [08:10]: Yeah

**Chuck Nice** [08:10]: ... we have a perception of preeminence-

**Interviewer** [08:12]: Okay

**Chuck Nice** [08:12]: ... in the universe itself.

**David Krakauer** [08:13]: We have an-

**Chuck Nice** [08:13]: And so-

**Interviewer** [08:14]: Even in the movie Hos-

**Chuck Nice** [08:14]: ... why would we make the supposition that those things exist

**Interviewer** [08:16]: ... Close Encounters of the Third Kind-

**Chuck Nice** [08:17]: Right

**Interviewer** [08:18]: ... we, they played musical notes-

**Chuck Nice** [08:19]: They played music. Back to us

**Interviewer** [08:19]: ... back, back to each other.

**Chuck Nice** [08:20]: Right.

**Interviewer** [08:20]: Yeah.

**David Krakauer** [08:21]: Look at, look at our other bias. Let me just turn this around on you a bit, which is that no ... Everyone would say, look, maybe chemistry is universal, right? So we're gonna find DNA or RNA. That's universal. But you ... But mathematics, well, we could describe things mathematically, but is mathematics universal? Is music? I mean, what is the, if you like, set of beliefs we have that make the most fundamental constituents universal and everything else somehow anthropomorphic?

**Chuck Nice** [08:50]: Uh-huh.

**Interviewer** [08:50]: So these-

**David Krakauer** [08:51]: And I would like to question that premise.

**Chuck Nice** [08:52]: Okay.

**Interviewer** [08:53]: Gotcha. And that's, that-

**Chuck Nice** [08:54]: I, I, I'm, I'm down with that

**Interviewer** [08:54]: ... and that flows in and through your thinking about an Interplanetary Project. Is that correct?

**David Krakauer** [09:01]: Yeah.

**Interviewer** [09:01]: Yeah, okay.

**David Krakauer** [09:01]: I mean, it, it, it-

**Interviewer** [09:02]: Got it

**David Krakauer** [09:02]: ... and in fact, the, the slogan of the Interplanetary Project was, um, changing the world one planet at a time. [laughs]

**Chuck Nice** [09:10]: [laughs] That's-

**Interviewer** [09:12]: Wow.

**Chuck Nice** [09:12]: That's actually very good.

**David Krakauer** [09:12]: And I think-

**Chuck Nice** [09:13]: Yeah. [laughs]

**David Krakauer** [09:14]: Right, 'cause I wanna change this world. I don't wanna particularly change others. And the question is, could a more expansive, humanistic, decent perspective on things allow us to make progress on this planet? That's-

**Interviewer** [09:25]: Well, we did discover a planet that's completely inhabited by robots.

**Chuck Nice** [09:29]: Mm.

**Interviewer** [09:29]: It's called Mars.

**Chuck Nice** [09:31]: Oh.

**David Krakauer** [09:32]: Oh.

**Chuck Nice** [09:32]: How long have you been sat on that joke? [laughs]

**Interviewer** [09:35]: Waiting for the, waiting to put it in, out there. So now we got the, the institute understood. Uh, now tell us about complex complexity.

**David Krakauer** [09:45]: Yeah. Right. So I mean, this is, this is ... There are several ways to do this, and you just tell me which you like and don't like, and I'll just throw out options, because I'm gonna take a s- different slices through this idea, right? And-

**Chuck Nice** [09:58]: Right. Let's start with roots. What's the, what are the roots of complexity science?

**David Krakauer** [10:03]: Okay. Aha. Well, okay. So, all right. So I just wrote a whole series of books on this, so it's a very good question for me. I ... So essentially, one way to say this is the roots are the study of machines, machines that were made-

**Chuck Nice** [10:18]: Mm

**David Krakauer** [10:19]: ... right, in the Industrial Revolution, like steam engines, or machines that evolved, like organisms.

**Interviewer** [10:25]: Just, just, just, just-

**David Krakauer** [10:25]: And in the 19th-

**Interviewer** [10:26]: ... just to clarify, you're not referring to the five basic machines of physics here. The-

**David Krakauer** [10:31]: No.

**Interviewer** [10:32]: You, you're referring to industrial machines that we have made-

**Chuck Nice** [10:35]: Manufactured

**Interviewer** [10:36]: ... in, in, manufactured-

**Chuck Nice** [10:37]: Yeah

**Interviewer** [10:37]: ... in our, in our civilization.

**David Krakauer** [10:39]: Exactly, like the steam engine, like the centrifugal governor, or like an organism. So-

**Chuck Nice** [10:45]: Right

**David Krakauer** [10:45]: ... exactly. So mechanisms in the natural world that do work of one kind or another.

**Interviewer** [10:49]: Gotcha.

**David Krakauer** [10:50]: And ... Right? So sometimes we call that problem-solving matter, in contrast to the regular matter that's studied by physics and, uh, physicists and chemists.

**Interviewer** [10:59]: I like that distinction.

**David Krakauer** [11:00]: So, you know, you gotta look at the m-

**Interviewer** [11:01]: Yeah, 'cause we-

**David Krakauer** [11:02]: Right

**Interviewer** [11:02]: ... in, in physics class with, there's a, a, a frictionless pulley on an, pulling a mass on an inclined plane.

**Chuck Nice** [11:07]: Right.

**Interviewer** [11:07]: B- we're not thinking that has consciousness or anything else.

**David Krakauer** [11:10]: No.

**Interviewer** [11:11]: It's not doing anything interesting other than fitting into my problem set.

**Chuck Nice** [11:15]: Right.

**Interviewer** [11:15]: Right. So yeah, go, I like that distinction. Continue, please.

**David Krakauer** [11:18]: Right. So, like, so okay, so that's one way to go. Right, so problem-solving matter versus regular. And then there's a whole bunch of questions, in fact, you just did it, that feel very natural when you talk about problem-solving matter. Like for example, how efficient is it? How'd it originate? How does it adapt?

**Chuck Nice** [11:35]: Mm.

**David Krakauer** [11:35]: Right? How smart is it? How does it store information? How does it evolve? How does it fail, right? And how eventually does it go extinct? And some of those questions are shared with physics. Many of them are not. It's not really meaningful to say, "How smart is the moon?" I mean, some people probably do, but we tend to ignore those people, right? And so, uh, but it's totally natural to say, "How much information does an economy store?" Right? How does a society of insects compute? So it, in a way you can define it by the questions that feel natural for it, and all of those are natural to all the scales we study.

**Interviewer** [12:10]: I like that because-

**Chuck Nice** [12:11]: Mm

**Interviewer** [12:11]: ... what that, when you have that awareness, it means you're not gonna force a square peg into a round hole if you're looking at a different system. Just because certain questions and solutions work with one system of machines doesn't mean they'll work for all of them.

**David Krakauer** [12:25]: Mean they'll work for all of them.

**Interviewer** [12:25]: And so if you, if you keep your interactions native to the phenomenon, you're surely likely to get deeper into what's going on for it. Is that, is that a fair-

**David Krakauer** [12:34]: Exactly

**Interviewer** [12:35]: ... characterization of what you just said?

**David Krakauer** [12:36]: I, no, I th- no, that's exactly right. And I think what happens, and this happened in the history of physics, and, is that the domain, the, what we would call, like, the ontology, the reality, um, requests from us a certain methodology or set of approaches we call epistemology. And so physical, the physical world loves principles of symmetry, right, which we encode in various principles in physics, typically conservation laws, right? In complex systems, we like broken symmetries and, um, noise, irregularities that get fixed, that sometimes we call frozen accidents. And that means a different kind of theory. And a lot of SFI is about finding the theory for the messier domain that lives between order and chaos.

**Gary O'Reilly** [13:26]: So this is chaos theory. So you're looking for patterns out of chaos theory, but if you take a step back, are the-

**Interviewer** [13:32]: But he didn't say it was chaos theory.

**David Krakauer** [13:34]: Yeah, he didn't.

**Gary O'Reilly** [13:34]: I did.

**Interviewer** [13:34]: He said it's in between. [laughs]

**David Krakauer** [13:35]: In between.

**Gary O'Reilly** [13:36]: I did.

**Interviewer** [13:36]: Yeah, but you had to guess.

**Gary O'Reilly** [13:38]: I know.

**Interviewer** [13:38]: Look, what he said was, it's a, it's i- in between pure chaos and-

**David Krakauer** [13:43]: Yeah. And, and order

**Interviewer** [13:43]: ... and order, and there's, there's messy systems that might yield-

**David Krakauer** [13:49]: Right

**Interviewer** [13:49]: ... to analysis, as you say.

**Gary O'Reilly** [13:52]: So, um, does chaos actually present with certain regularity of patterns?

**David Krakauer** [13:56]: Yeah, so actually, [laughs] I mean, just to... Okay, let me, as an aside, I'll get there in a second, a footnote to that. The answer is yes.

**Gary O'Reilly** [14:03]: Mm.

**David Krakauer** [14:03]: Neil's right. I mean, chaos theory is a tiny, tiny, tiny part of complexity.

**Gary O'Reilly** [14:07]: Right.

**David Krakauer** [14:07]: And, um, in fact, weirdly enough, it's a, it's a part of complexity that fits very naturally in physics. It came out of the study of things like the so-called three-body problem.

**Gary O'Reilly** [14:17]: Mm-hmm.

**David Krakauer** [14:18]: Classical systems, right? That are completely deterministic. There's no noise in chaos. Uh, it's deterministic irregularity. So it does present as order that appears superficially to be random, and, uh, we're interested in subjects that have that property, but they add real randomness, like thermal randomness, noise to them. So early in our history, because of a book that was written by James Gleick, actually, in '92-

**Interviewer** [14:43]: Oh, yeah

**David Krakauer** [14:43]: ... it was called, called Chaos, right? And it was an important book for SFI because he talked a lot about our work, but it's actually a tiny part of what we do, and it's the part that's very close to physics.

**Interviewer** [14:53]: Mm-hmm.

**David Krakauer** [14:53]: Mm-hmm.

**Interviewer** [14:54]: All right.

**Gary O'Reilly** [14:55]: So, so it, it could-

**Interviewer** [14:56]: So there.

**David Krakauer** [14:57]: That, now. [laughs]

**Gary O'Reilly** [14:58]: Now I know more.

**Interviewer** [15:00]: Yeah. [laughs]

**Gary O'Reilly** [15:00]: I am better educated, so thank you.

**Interviewer** [15:02]: Okay, so how about other, other elements of-

**David Krakauer** [15:04]: But, but regardless, just, I was just gonna say, but are you looking in the messiness for reason, or if you wanna call it order, if you wanna call it non-messiness, that, so that the messiness itself really isn't messy, we just see it that way. We don't understand it. Yes. Okay, so right. So interestingly, so where does this word complexity come from? And it gets exactly to your question. In, in 1948, um, Warren Weaver, who was a mathematician, he wanted to classify all of regularity or irregularity in the universe, right? And he said, and we can debate whether this is useful, I find it quite useful, he said there are simple phenomena. That's classical physics. It doesn't mean it's easy to understand, but it's, it's to Neil's earlier point. It's simple. There are beautiful laws, elegant mathematical formalisms that explain it. Then there's the world of what he called disorganized complexity. That's the sort of the study of gases, what we would now study with thermodynamics and statistical mechanics. Irregular things, but have beautiful descriptions. And then in the middle, there's organized complexity. It's, it's not a gas, it's an organism. It's an ant, right? [laughs] It's a brain. It's, it's a city. And in that space, what we realized really at the end of the, uh, 19th century, is we don't have good theories for it. We can do irregularity beautifully. We can do simplicity beautifully, and then you move to everything that we actually care about in some sense as human beings and as animals, as living beings, we kind of under-theorized. Beautifully described, beautiful artworks, but what is the kind of mathematics of that zone of organized complexity? And I think you make a really important point, which is that how much order you see is a function of the observer.

**Gary O'Reilly** [17:00]: Oh.

**David Krakauer** [17:00]: And, uh, if the observer has more computational power-

**Gary O'Reilly** [17:04]: Mm-hmm

**David Krakauer** [17:05]: ... it's gonna see more order, right? [laughs] So complexity is observer-dependent in a very profound way, rather like quantum mechanics is observer-dependent in a very different way.

**Gary O'Reilly** [17:15]: Wow.

**David Krakauer** [17:15]: But this has to do with our computational capability, if you like.

**Interviewer** [17:18]: I'm gonna tell you the truth right now, and I'm just gonna come out and say it.

**David Krakauer** [17:21]: Mm-hmm.

**Interviewer** [17:21]: I actually thought when we started that, that this was gonna be bullshit.

**David Krakauer** [17:25]: [laughs]

**Interviewer** [17:26]: But, but I, but he is making some great points here. [laughs]

**David Krakauer** [17:31]: Mm. Mm.

**Gary O'Reilly** [17:31]: That's why he's on.

**Interviewer** [17:33]: That's why we got the man.

**Gary O'Reilly** [17:34]: That's why he's here.

**Interviewer** [17:34]: That's why we got the man.

**Gary O'Reilly** [17:36]: Uh, uh, so when, when you look for adaptive functions, is that the sort of pattern that you're looking for, how it's reacted to, for want of a better term, environmental circumstances?

**David Krakauer** [17:47]: Definitely. I mean, I think, you know, one of the challenges, right, is going from... And I think you've had some of my friends on that show who talk about this. I mean, maybe Sean and maybe Sarah.

**Interviewer** [17:56]: Yeah, we had Sean, Sean Carroll. Yes.

**David Krakauer** [17:58]: Right, right. And s-

**Interviewer** [17:58]: He's a friend of the show. Uh-huh.

**David Krakauer** [18:00]: Yeah, and so that's a good example. So you go from, you know, what's the difference between a ball rolling down a hill, right? So it's minimizing some function or... And an, an organism adapting. And, um, that distinction s- to this day, people debate is there adaptation in physics? You know, m- maximizing some function or minimizing some function, or is it unique to the living state? And so for us, agency, the agent, you know, it could be an organism, could be a machine actually, could be an AI, um, has some characteristics that a ball rolling down a hill do not have that we need a new theory for, and we can talk about what that new theory looks like.

**Chuck Nice** [18:43]: Mm-hmm. Right.

**David Krakauer** [18:43]: But adaptation is absolutely central to complexity because without it, there isn't any.

**Chuck Nice** [18:48]: I will tell you this much, uh, an AI rolling down the hill is a hell of a lot more expensive.

**Interviewer** [18:54]: [laughs] Than a ball rolling down a hill.

**Chuck Nice** [18:56]: You have, you have lost a lot of money-

**Interviewer** [18:58]: [laughs]

**Chuck Nice** [18:59]: [laughs] Other than that ball.

**Interviewer** [19:00]: All right, so this approach seems potent enough so that it does not need to be constrained to any one discipline, and I'm impressed to see efforts to apply this to society, economic systems, civilization itself.

**Chuck Nice** [19:16]: Yeah.

**Interviewer** [19:17]: So do you have enough confidence in your modeling and its foundations to then go into something that's way more complex than basic physics because you're now involving human behavior?

**Chuck Nice** [19:28]: Yes. In other words, can you solve stupidity?

**David Krakauer** [19:31]: [laughs]

**Chuck Nice** [19:32]: Because we are living in a very high time of stupidity.

**David Krakauer** [19:37]: Well, that's actually, uh, we'll get... That's my area of interest, so I can't solve it, but I can diagnose it. And so, but we can talk about what it means. Uh, let me just address both. I feel this question, I don't know, is the real honest answer to this question.

**Chuck Nice** [19:54]: Oh.

**David Krakauer** [19:54]: I think that something interesting happens that's sometimes surprising, and then this is very familiar from other sciences, right? If you try to understand an individual particle floating about, it's really hard. Uh, you know, it's trajectory is essentially random. But you have enough particles and you average, and order emerges, right? So for example, a fluid will flow and, um, so we have equations of fluids that look at things like viscosity and average density that don't worry about the individual particles and all their peculiarities. And in just the same way, humans that are fundamentally, I think, unpredictable, I mean, there are things we do that are predictable, alas. But in aggregate, there are predictable regularities in societies, and economists and psychologists and sociologists exploit those facts. So if you aggregate right-

**Chuck Nice** [20:44]: Right

**David Krakauer** [20:44]: ... then a regularity and a pattern can emerge again. And I think the big question for us is, is a city, is a civilization one of those things that actually shows emergent regularity, which will give us some handle on them that we might be able to control?

**Chuck Nice** [21:00]: This is not a pushback, but I need some clarification here. Because when you talk about a city and you talk about, um, the, let, let's just say the aggregate of a group, okay? All right.

**Interviewer** [21:09]: People.

**Chuck Nice** [21:10]: Uh, people. Thank you. [laughs] When you talk about people, all right, a neuroscientist will tell you that we are predictable enough that if given enough data on the person, I can tell you exactly what they're going to do. And if given enough d-

**Interviewer** [21:27]: And advertisers know that

**Chuck Nice** [21:28]: ... Yeah, advertisers.

**Interviewer** [21:28]: You don't even, you don't even need neuroscientists.

**Chuck Nice** [21:30]: We don't even need, we don't even need neuroscientists, right.

**Interviewer** [21:31]: [laughs]

**Chuck Nice** [21:32]: And if given enough data on a group, I can tell you exactly how to manipulate them for them to become violent, for them to become docile, for them to become, uh, agitated. Uh, so where is the emergence in that? Because-

**Interviewer** [21:48]: But we haven't talked about emergence yet.

**Chuck Nice** [21:49]: Oh, oh, okay. Well, uh, you're right. Okay.

**Interviewer** [21:51]: Okay.

**Chuck Nice** [21:51]: Uh, but, uh-

**David Krakauer** [21:52]: But it's still a great question

**Chuck Nice** [21:53]: ... I, I felt like he was moving towards emergence with that-

**Interviewer** [21:55]: No, no, but-

**Chuck Nice** [21:55]: ... with what he just said

**Interviewer** [21:56]: ... but the, the bridge there is he's brilliantly analogizing the fact that you have gas, fluid particles-

**Chuck Nice** [22:05]: I, I agree with that

**Interviewer** [22:05]: ... and, and individually, you don't, there, there's no, there's no flow law for an individual particle.

**Chuck Nice** [22:10]: Yeah, you're not, you're not worried about the particle.

**Interviewer** [22:11]: Right.

**Chuck Nice** [22:11]: But when they come together, they actually present these properties that make them as a whole act differently.

**Interviewer** [22:16]: And, and you basically just said what he said, that in aggregate, we behave in ways that m- may be predictable and be describable analytically.

**Chuck Nice** [22:25]: Yes, but here's the difference. As human beings, that's due to the fact that each one of us has to be in a very particular place for that to happen. Do you understand what I'm saying? Like-

**Interviewer** [22:35]: I, I basically-

**Chuck Nice** [22:36]: Unlike particles, all the particles is gonna do the same thing, all of them, all the time.

**David Krakauer** [22:40]: All right, David-

**Chuck Nice** [22:41]: That's my point

**David Krakauer** [22:41]: ... question for you. If you go back to the reference point of cities-

**Chuck Nice** [22:44]: Yeah

**David Krakauer** [22:44]: ... does it change for an unplanned to a planned city where the predictability is as same or very different?

**Chuck Nice** [22:51]: Well, that's interesting. Yeah, I mean, good question. I mean, I think that for the things that we study, not so much, interestingly.

**Interviewer** [23:00]: Hmm.

**David Krakauer** [23:00]: Okay, I want to somehow, I want to thread these points-

**Chuck Nice** [23:03]: All right.

**Interviewer** [23:03]: Good

**David Krakauer** [23:04]: ... all of them, because they're all really good, and they're actually getting at the heart of why this is difficult. So the first point about, you know, yes, humans are not like little, you know, Brownian motion particles. We have histories, we have desires, we have beliefs, right? We, and so we're heterogeneous in a way that particles are not. That is absolutely right, and it's what makes the question difficult.

**Interviewer** [23:23]: That's really all Chuck was-

**Chuck Nice** [23:24]: That's what I'm saying

**Interviewer** [23:25]: ... trying to say.

**David Krakauer** [23:25]: Yes, that's his point.

**Chuck Nice** [23:26]: Correct.

**David Krakauer** [23:26]: And I think that's completely-

**Chuck Nice** [23:26]: Sorry for taking so long to get there.

**David Krakauer** [23:28]: No, but I think that is, is really important, right? And I think, and yet, right, um, if I half the price of the groceries, you're gonna go out and buy more of them, uh, because you're fearful that the price will go up again next week. But you see what I mean. There are, there are regular patterns of behavior despite all of that heterogeneity, which is important in our lives. And so the, the question is at what scale? So now let's go to cities, right? It turns out actually that cities are so constraining of the supply of energy and the supply of resources, and the interactions between people and neighborhoods, that there are emergent regularities that come out of those constraints.

**Chuck Nice** [24:05]: Hmm.

**David Krakauer** [24:05]: So for example, if you look at the growth of GDP, uh, as a city gets larger, it follows a universal law that looks like it's a law of physics. You get a scaling of GDP that goes as essentially the population size to the 1.15 power. So whatever.

**Chuck Nice** [24:23]: Wow.

**David Krakauer** [24:24]: But the point is that weirdly enough, when you impose these strong constraints on society, they start looking more like physical systems. They, they have emergent regularities.

**Chuck Nice** [24:32]: Oh man, that's great.

**David Krakauer** [24:33]: And as you re- as you remove those constraints- Right? Then of course many of these systems, these, these kind of theories fail.

**Interviewer** [24:39]: So let's, let's blow open the topic now then of emergence.

**Chuck Nice** [24:43]: Yeah.

**Interviewer** [24:44]: Because that's a gre- a topic of great fascination, especially in biology. But to the extent that that can apply to other systems, that would be amazing to get some insight into what's going on on the frontier where we don't understand what's going on.

**Chuck Nice** [25:00]: And for, and just, just because you and Neil, and, and mo- Gary probably too, 'cause he's did all the research on this, can you please define emergence? Because I hear people use the term, and I think a lot of times they're not using it correctly. So can you please-

**David Krakauer** [25:19]: Yeah

**Chuck Nice** [25:19]: ... just tell us what is emergence?

**David Krakauer** [25:21]: That, that's a, that's a completely fair observation. [laughs] I spend most of my life, you know, in, in horror. Uh, and so okay, first of all, I wanna say it's a difficult concept, and I think it would be completely accurate to say that we still have huge amounts of work to do, uh, to understand formally what it means. But I'm now gonna, having said all that, little caveat, I'll, I'll tell you what I think it is. So let's just start with physics, 'cause easy. So we just talked about it. We talked about gases, like the kinetic theory of gases. Put loads of those particles together, right, and you can get solids at the right temperatures and pressures, and you can get fluids. And it turns out that the mathematical equations you use to describe those two systems are different, right? And the dimension, the simplicity if you like, the number of terms in those equations are different. And so we like fluid dynamics 'cause it's, it's actually quite a elegant way of describing the behavior of loads and loads of particles in a particular temperature and pressure. That is emergence, the fact that you have two things: a new state of matter with properties that wouldn't really seem to apply at the individual particle level, and it has a new language, a new language of description, and a new language of prediction. Those are the two hallmarks. Now, it's interesting you were talking about psychology, advertising, and neuroscience.

**Chuck Nice** [26:45]: Mm.

**David Krakauer** [26:46]: And that's a beautiful example. So let's imagine, right, that in order to be a really good psychologist or marketer, you had to be a great neuroscientist. Of course, a really good marketer doesn't need to be a good neuroscientist, because all of that detail is a little bit like a particle in a gas relative to a fluid. A good marketer is doing something like fluid dynamics by analogy. They're understanding collective properties that have their own language, right? And I think a lot of kind of pseudoscience, to be honest, is where a level that has its own perfectly adequate language starts using the more reductionist language to give it legitimacy. So emergence. One, new states or phases of matter or organization. Two, uh, new languages and descriptions, typically mathematical, doesn't have to be, right? And, and three, the, the tricky one is not everything deserves to be called emergent. And so finding that emergent level, uh, is actually part of the challenge. And, and a lot of, we would argue a lot of economic theory would be better off being replaced by psychology because the language it's derived or invented doesn't really work. It's not like fluid dynamics. So the failures of emergence are also really interesting.

**Gary O'Reilly** [28:06]: So when you get to the s- the state of emergence, what is, what is the prediction accuracy for you being able to say, "This is most likely gonna be happening here"?

**David Krakauer** [28:17]: Yeah. That, that's actually, that's actually the criterion, right? That, if you'll allow me, I'm gonna use another analogy that helps.

**Gary O'Reilly** [28:23]: Go for it.

**David Krakauer** [28:23]: Okay. So let's say that I'm proving a mathematical theorem, okay? The way that works, you write down your axioms, right, your assumptions. You put down your equations. And then you have a bunch of, um, a, a kind of a toolkit for doing deduction. You apply calculus or group theory, whatever you like. And out pops an answer, right? And the correctness of that answer has nothing to do with your psychological state, nothing to do with what you had for breakfast in the morning, nothing to do with the economy, right, nothing to do with neurons. It has to do with the formal logic of mathematics. And that's the most beautiful example of emergence for me, because you wouldn't gain additional insight into the correctness of a proof by knowing what the neurons were doing. They're irrelevant. And the technical term for that is screened off. Truly emerging phenomena screen off microscopic degrees of freedom. That's a sort of fancy language. And we know it's true, right? But we know it's true of mathematics. It's probably the best example I think of a truly emergent language. And it, because, to your point, it does predict, it does deduce. You do get to the right answer, right? You don't have to go down.

**Interviewer** [29:33]: So I'm curious about something here. So when we look at flocking birds-

**David Krakauer** [29:37]: Yeah

**Interviewer** [29:38]: ... that is a macroscopic group behavior where, as far as I understand it, you cannot, there's no known way to analyze a single bird in any way that will tell you that in the company of other birds it will flock. And I've always thought of emergence as just such a system. A- and you hinted to that with the, the gas particle and the, the, and the gas as a fluid or as a solid or as a gas. Or, well, yeah. [laughs]

**Chuck Nice** [30:09]: [laughs]

**Gary O'Reilly** [30:09]: Depending on temperature and pressure.

**Interviewer** [30:11]: Sorry, the molecule-

**Chuck Nice** [30:11]: Yeah, the molecule

**Interviewer** [30:12]: ... as a s- as a, as a, as a solid, liquid, or gas. So would you agree that these other kinds of systems, you can't, you can't look at a termite and say, "One day it will build a termite mound." Is it because we don't know enough about it? Do we need to be more reductive or less reductive in our analysis of the organism to know what it would do macroscopically i- in a group?

**David Krakauer** [30:37]: Yeah, no, that's really interesting. Um, so okay, so I think sometimes that and sometimes the opposite. So let me again give you an example.

**Interviewer** [30:46]: [laughs]

**David Krakauer** [30:47]: [laughs]

**Gary O'Reilly** [30:47]: So you're right.

**David Krakauer** [30:48]: No, because-

**Gary O'Reilly** [30:48]: He's right.

**David Krakauer** [30:49]: No, no.

**Interviewer** [30:50]: Yeah, yeah.

**Gary O'Reilly** [30:50]: [laughs]

**David Krakauer** [30:50]: It's really interesting because let's say, it's sort of interesting, right? If, if you said I know everything about the neuroscience of an ant, right? Or, or, or termite or, or-

**Gary O'Reilly** [30:59]: Mm

**David Krakauer** [30:59]: ... a starling, you know?

**Gary O'Reilly** [31:00]: Yep.

**David Krakauer** [31:01]: I know about fluid dynamics, hydrodynamics, I know what feathers do, I know how far they can see, you know, all of that. So I could predict if I put a bunch of them together how they would behave, and I think that there are going to be cases where that is true. But that doesn't mean emergence isn't still useful because you might say, "Yes, I can. I needed deep thought," the computer from, you know, Hitchhiker's Guide to the Galaxy, right, to work it out, and it took the lifetime of the universe to do so, but I could do it. As opposed to, "You know what, Neil, I've got a pencil and paper here, I'm gonna write down my little emergent theory and I'm gonna do it in five seconds." And so there is a side to emergence which is just about, um-

**Interviewer** [31:44]: Practicality

**David Krakauer** [31:45]: ... efficiency.

**Interviewer** [31:45]: Yeah, yeah.

**David Krakauer** [31:45]: Yeah.

**Gary O'Reilly** [31:45]: Efficiency.

**Interviewer** [31:46]: Uh-huh.

**David Krakauer** [31:46]: Yeah.

**Interviewer** [31:46]: Okay. Okay.

**Gary O'Reilly** [31:47]: So we're gonna see a, an equation on a T-shirt sometime soon.

**David Krakauer** [31:51]: We have many of those.

**Interviewer** [31:52]: [laughs]

**Gary O'Reilly** [31:53]: [laughs]

**David Krakauer** [31:53]: Unfortunately, we have too many of those.

**Gary O'Reilly** [31:55]: Too many. That's probably the problem.

**Interviewer** [31:56]: Equations, eh.

**David Krakauer** [31:57]: All right, well, let's-

**Gary O'Reilly** [31:57]: I mean, Chuck mentioned AI earlier on and we don't wanna roll it down the hill 'cause it's too expensive.

**Interviewer** [32:01]: Absolutely.

**David Krakauer** [32:02]: Mm-hmm.

**Gary O'Reilly** [32:03]: Can you predict the emergence of consciousness in something like an AI?

**David Krakauer** [32:08]: Wow.

**Interviewer** [32:08]: Or define the complexity of life itself-

**Gary O'Reilly** [32:11]: Oh

**Interviewer** [32:11]: ... in this context.

**Gary O'Reilly** [32:12]: You wanna go even deeper, fair enough.

**Interviewer** [32:13]: Yeah, I mean, why not?

**David Krakauer** [32:14]: Well, yeah.

**Interviewer** [32:14]: While we're there.

**David Krakauer** [32:14]: I mean, honestly, w- and wouldn't that kinda be the same? Because if, if an AI really does have emergent consciousness and e- truly, truly emergent intelligence-

**Gary O'Reilly** [32:26]: Then it's life

**David Krakauer** [32:27]: ... then it really is us at that point. It's just us at that point.

**Gary O'Reilly** [32:32]: Or is, or is it?

**David Krakauer** [32:33]: In, in a... No, it's us in a different form.

**Interviewer** [32:34]: Well, let's find out.

**David Krakauer** [32:35]: Okay, let's find out.

**Gary O'Reilly** [32:36]: Yeah.

**David Krakauer** [32:37]: I might gonna, I might annoy you now.

**Gary O'Reilly** [32:38]: Okay.

**Interviewer** [32:39]: Go ahead.

**David Krakauer** [32:39]: So, [laughs] so the first thing I would say is that AIs have no intelligence.

**Gary O'Reilly** [32:43]: Right.

**David Krakauer** [32:43]: Okay? And then we'll discuss what that means.

**Gary O'Reilly** [32:45]: Mm-hmm.

**David Krakauer** [32:45]: But they have tons of capability. And, and I, and I tell you the difference. Let me... Here's, here's my thought experiment. I always ask these kind of zealots of the technocratic era, which is the following. You have two students, okay? And let's call them A and B, and you set them the same exam. It's just a general knowledge quiz, right? And they come back, they got all the answers right. All right? And I said to you, "Which is the better student?" You'd say, "I don't know, they got the same answer." Now I say to you, you know, "A did the exam in the library, where every time a question came up they looked up the answer, and B actually took the exam, I don't know, in the, by the side of the ocean," you know. And you say, "Well, clearly B is the better student." Now, the problem, so knowledgeable, we know the difference between fake knowledgeable and real knowledgeable because we can ask, "Did you do it in a library or not?" And the problem with a lot of AI at the moment is it's basically fake intelligence as far as I'm concerned.

**Gary O'Reilly** [33:44]: Right. It's a very quick lookup. It's really just-

**David Krakauer** [33:46]: It's very quick, essentially a really clever lookup. Uh, it's a plus, and I'm not, I'm not saying it's not an amazing technology. I'm just saying but it's a very capable technology. If you ask, and again, now we get to intelligence, kind of my field, what is intelligence? Intelligence is basically someone or something that makes a hard problem easy.

**Gary O'Reilly** [34:08]: Mm.

**David Krakauer** [34:08]: If you went to school and you're sitting down trying to work out a problem, you look over at the person next to you, and they've made a problem look effortless, you'd say, "Oh, my God, that's, that's pretty intelligent."

**Interviewer** [34:18]: No, no, no.

**David Krakauer** [34:18]: If that person was-

**Interviewer** [34:19]: You're, you're the intelligent one looking over the shoulder-

**Gary O'Reilly** [34:21]: Right

**Interviewer** [34:21]: ... 'cause you got the answer easier than they did.

**Gary O'Reilly** [34:23]: Yeah. [laughs]

**David Krakauer** [34:24]: Yeah, [laughs] that's true.

**Gary O'Reilly** [34:24]: Right.

**David Krakauer** [34:25]: Now, so that's like a strategic intelligence. [laughs]

**Interviewer** [34:28]: If, if I may echo your story with an example I give often-

**David Krakauer** [34:31]: Yes

**Interviewer** [34:31]: ... where let's say I have an architect and I'm gonna hire a, a summer intern, and they're b- they're both the same on paper.

**David Krakauer** [34:38]: Right.

**Gary O'Reilly** [34:39]: Right.

**Interviewer** [34:39]: And so I, th- therefore they get to come in for an interview, right? And I wanna pick one from the interview.

**David Krakauer** [34:43]: Okay.

**Interviewer** [34:43]: And this is a contrived example, but I think you'll agree, David, that the... There's a church steeple outside my window.

**David Krakauer** [34:50]: Mm.

**Interviewer** [34:51]: And I say, "Just for grins, uh, how tall is that church steeple?" And the person first, "Oh, it's 135 feet." I will say, "Well, how do you know?" "Well, I'm, I memorized all the church steeple heights. It, it's a thing I do." The other person says, "I don't know. I'll be right back." He goes away for 10 minutes, then comes back and says, "Somewhere between 130 and 140 feet." I say, "Well, how did you find out?" He said, "Well, I know how tall I am, and I measured my shadow, then I measured the shadow of the church steeple, and then I did some simple math to get this answer." Who are you gonna hire?

**David Krakauer** [35:24]: I'm, I'm, I'm actually gonna hire the, the second guy.

**Interviewer** [35:27]: The second, the second one.

**David Krakauer** [35:28]: Because clearly what he was able to do was problem solve.

**Interviewer** [35:31]: I, I didn't say he or she, but that's okay.

**David Krakauer** [35:32]: Oh, I said he. I'm sorry.

**Interviewer** [35:33]: Yes. [laughs]

**David Krakauer** [35:33]: 'Cause the, I'm, I apologize to every-

**Interviewer** [35:36]: [laughs]

**David Krakauer** [35:36]: Because they were able to [laughs]

**Interviewer** [35:39]: Were able [laughs]

**Gary O'Reilly** [35:39]: Good save. Good save.

**David Krakauer** [35:40]: Because they-

**Interviewer** [35:42]: He saved

**David Krakauer** [35:42]: ... were able to problem solve.

**Interviewer** [35:43]: To, to problem solve. And, and, and is my example resonate with you here?

**David Krakauer** [35:47]: Yeah, very much so. And I think you can see where you notice, right, that in the era of the Turing test, the imitation game, you just ask how high is the steeple. And if it gives you the right answer, you say, "Look, there you go. It's indistinguishable from another human being." But you then went a bit further and asked for an explanation.

**Gary O'Reilly** [36:07]: Mm.

**David Krakauer** [36:08]: Right? Tell me how you arrived at that answer. Prove to me you understand. And I think these ideas of it, understanding and explanation, are really important to intelligence, and under-discussed. In place of what Alan Turing did, and you know, he's my compatriot, I love him, but, uh, the idea of the Turing test did a lot of harm because it allows for this possibility essentially of cheating.

**Interviewer** [36:31]: I had not thought about it that way-

**David Krakauer** [36:33]: Yeah

**Interviewer** [36:33]: ... but you've just convinced me. Uh, because that's, that's the, the litmus test that has always been applied.

**David Krakauer** [36:38]: Right.

**Interviewer** [36:38]: And then y- Everyone is left thinking there's intelligence on the other side.

**Chuck Nice** [36:42]: Right.

**Interviewer** [36:42]: But if the- but they would just unpack that into, and, and lays it bare for what it is.

**Chuck Nice** [36:48]: However, in defense of Turing, I think it was just the wrong terminology, because basically the idea was you wouldn't know the difference. That was the test. You would not know the difference.

**Interviewer** [36:57]: Correct. Correct.

**Chuck Nice** [36:58]: So he's not n- necessarily saying that they're the same, he's just saying that one is represented in a way that is indistinguishable from the other.

**Interviewer** [37:07]: Unless you f- went further and said, "How did you figure this out?"

**Chuck Nice** [37:09]: Well, now you just screwed him. [laughs]

**Interviewer** [37:12]: [laughs]

**Gary O'Reilly** [37:12]: David, you, you spoke about your research into intelligence in the universe. On Aeon, you published, uh, an essay, Problem Solving Matter, September of 2024.

**Interviewer** [37:22]: Is Aeon a, a-

**Gary O'Reilly** [37:23]: Aeon. Aeon

**Interviewer** [37:23]: ... a journal?

**Gary O'Reilly** [37:23]: Aeon. Yes, it's a journal.

**David Krakauer** [37:24]: Yeah, either way.

**Interviewer** [37:25]: E- yeah. Mm-hmm.

**Gary O'Reilly** [37:25]: Thank you. And you suggest that life is less chemistry and physics, more like a computational process that is born out of our need to be problem solvers.

**Chuck Nice** [37:37]: Hmm.

**Interviewer** [37:37]: Mm-hmm.

**Gary O'Reilly** [37:38]: Um, you're gonna need to do some-

**Interviewer** [37:39]: Shots fired there.

**Gary O'Reilly** [37:40]: No, no, no. You're gonna need to do a little bit more unpacking there, 'cause that's-

**David Krakauer** [37:43]: Yeah

**Gary O'Reilly** [37:43]: ... that's got people thinking now that you even just said that much.

**Interviewer** [37:45]: You can only say that when there's not a biologist within a mile of him, then he can say that.

**Chuck Nice** [37:49]: Oh. [laughs]

**Gary O'Reilly** [37:49]: I think, I think David has the capability-

**Interviewer** [37:50]: [laughs]

**Gary O'Reilly** [37:50]: ... to answer this.

**Interviewer** [37:51]: You'd think. All right. Go for it.

**David Krakauer** [37:53]: So in that, in that paper with my co-author, Kristoffer Kempes, um, we address this question of problem-solving matter transcends its materials, which is essentially that question, right?

**Chuck Nice** [38:06]: Hmm.

**David Krakauer** [38:06]: But let me give you a... Here's the thought experiment, and it's extraterrestrial, you're gonna like it. Which is, so you imagine some extraterrestrial being visits the Earth, and they want to know what a computing device are, right, or is. And they arrive on the Earth at the time of the Jacquard loom, which was like a first essentially digital computer. And they say, "A digital computer is something made out of wood."

**Chuck Nice** [38:29]: [laughs]

**David Krakauer** [38:29]: "Out of silk."

**Chuck Nice** [38:31]: [laughs]

**David Krakauer** [38:31]: Right? "And, uh," right, okay, and it's... All right.

**Chuck Nice** [38:34]: [laughs]

**Interviewer** [38:35]: [laughs]

**David Krakauer** [38:36]: And then-

**Interviewer** [38:37]: With a foot pedal

**David Krakauer** [38:37]: ... 50 years pass.

**Chuck Nice** [38:38]: Right. [laughs]

**David Krakauer** [38:38]: With a foot pedal. Right, exactly, right?

**Interviewer** [38:40]: [laughs]

**David Krakauer** [38:40]: And, uh, and it's used to make beautiful items of clothing. That's what a com- right, okay. So, you know, 50 years pass, they come back again, maybe a bit more, 75 years. And they say, "What is a computer?" Well, it's this thing with these giant vacuum tubes, right? Thermionic valves, and they're made out of quartz, and they're made out of metal, you know, molybdenum, and so on. And another 50 years passes, and they come back and say, "What's a computer?" Actually, no, that, that's not a computer. It's not something made of wood and silk. It's not something made out of glass and tungsten or whatever you want. It's something made out of metal oxides and it's based on transistors. And what you realize is, you know, computing isn't about the material, it's about the logic. They all implement a logic. Now, they might, they implement, as it happens, binary logic, Boolean logic, right? And we know that if you have enough transistors and you put them together, you can do computations. So this is actually another thing that came from Turing that he got completely right, right? Is that it's not the material, it's the logic, and you need the material that can instantiate the logic. So not any material will do. Unfortunately, the history of the study of the origin of life has been obsessed with the material, because we're made of material, and we're the only example we know.

**Chuck Nice** [39:55]: Hmm.

**David Krakauer** [39:56]: And so you look at the materials that we're made out of, or all life, and you kind of reach this weirdo conclusion that that's the only way it could be done.

**Interviewer** [40:04]: That's clever and insightful. What that also does is it distracts... No, it misleads us into projecting what things might be like in the future. So for example, in 2001: A Space Odyssey-

**Chuck Nice** [40:17]: Mm-hmm

**Interviewer** [40:17]: ... that was 1968, and they're imagining the year 2001.

**Chuck Nice** [40:22]: Right.

**Interviewer** [40:22]: That's the whole point of the movie. So in 1968, computers were, like, big, and in 2001, the computer was even bigger.

**Chuck Nice** [40:31]: Right.

**Interviewer** [40:31]: Okay? And it was even more centralized, and no one is thinking that we'd all have computers in our pocket. So they're thinking that it's the material, now just get more of that to make that happen.

**Chuck Nice** [40:42]: Exactly.

**Interviewer** [40:42]: So it com-

**Chuck Nice** [40:43]: Exactly

**Interviewer** [40:43]: ... completely dis- uh, distorts how you might be thinking about the future, unless you, y- you take David's sensibility to task here.

**Chuck Nice** [40:51]: True. True. In addition, could we then think that the materials are us, and then seek to replicate not a silicon version of ourselves, but an actual biological merger of the AI and what causes us to have true intelligence?

**David Krakauer** [41:21]: Uh, again, I mean, two things there. Um, so one is just a lot of the things and concepts that we've been wrestling with, even, you know, consciousness that you asked about, life, intelligence, in their early phases of development get mapped onto a machine or mechanism or matter that's familiar to us. And there's good reason. I mean, there's nothing wrong with that. I mean, it's perfectly safe. You gotta start somewhere.

**Chuck Nice** [41:47]: Right.

**David Krakauer** [41:48]: Um, and then as our ideas evolve, they become in some sense more abstract, and, um, eventually we culminate in a kind of logical description. But the material matters, uh, right? And so to your point, it's really interesting. I mean, and this is an unknown question. There are people out there and they call themselves functionalists, and Turing was one. And he wrote this beautiful essay where he said, uh, I mean, he didn't say it this way, but he essentially said, "I don't give a shit whether the brain has the consistency of cold porridge." He said, "The matter doesn't matter." And, you know, that was his view. But, you know, we don't know that, too.

**Interviewer** [42:21]: But matter does matter.

**David Krakauer** [42:22]: The matter matters.

**Chuck Nice** [42:24]: [laughs]

**David Krakauer** [42:24]: Matter, matter matters, right? But can any-

**Interviewer** [42:26]: I'm all for matter mattering. [laughs]

**David Krakauer** [42:29]: Right, but does any kind of matter matter, right?

**Interviewer** [42:31]: Okay.

**David Krakauer** [42:31]: And I think that's sort of the question. And I th- and it is an open question whether the kind of sensorial ex- sensual ex- existence we experience Does depend on the particular kind of matter we're made from. You know, does consciousness depend, our kind of consciousness depend on our kind of matter? I actually think there's a strong claim to be made the answer is yes. Doesn't mean there couldn't be other kinds of life, right? Other kinds of intelligence.

**Chuck Nice** [42:57]: Right.

**David Krakauer** [42:58]: But this one depends on our matter.

**Chuck Nice** [43:00]: Well, the one that, the, it's the one that we know for a fact does because it's us, and we're experiencing it. So from an experiential frame of reference, we understand it. So my point is, why wouldn't we just look for exactly how we become conscious and intelligent in our formation? And then if it truly isn't something that just happens because all of these disparate things come together, then we might be able to take that and graft it onto a machine of our making.

**David Krakauer** [43:38]: Well, you could argue that that's exactly what's just happened.

**Chuck Nice** [43:41]: Uh-oh.

**David Krakauer** [43:41]: So if you, if you l- well, look, I mean, if you look at the history of AI, 30 years ago, it, it, it, now is gets called GoFi, good old-fashioned AI, and it was all about we're gonna build a computer that can play chess using symbolic logic, checkers. We're gonna build expert systems that we're gonna inform with human understanding. And then this big shift took place in neural networks, and they said, "You know what? We're not gonna start top-down. We're gonna start bottom-up, and we're gonna start bottom-up with a system that resembles a brain." And, and it's exactly... So they did exactly what you just said. They'll say, "Let's, let's just try and rebuild something that looks a bit like a brain, with lots of units that are kind of like neurons, that are connected kind of like neurons. You have enough of them, uh, they'll do something interesting." So I would argue that this kind of biomimesis approach to intelligence that you're describing is, is, is the AI revolution of the current moment.

**Chuck Nice** [44:37]: Okay.

**Interviewer** [44:37]: All right. But, but, I, I gotta get to the bottom of something here. Let's bring back emergence into the conversation. We have a, we have neurons that ostensibly are nicely suited for our survival. Okay? When we're hungry, we look for food. If there's danger, we escape it or fight it, and so the brain is doing its thing, and any creature has similar, any creature that cares about living-

**Chuck Nice** [45:05]: Similar, similar functionality in their brain

**Interviewer** [45:06]: ... Yeah, exactly, in their brain, in their brain. But we wanna say that we have consciousness as something beyond what we might ascribe to a plant. So what is going on inside of us, uh, either in complexity or from bottom-up or top-down, that you can call consciousness? And the reason why I ask that in that way is everyone is making a big deal of consciousness today, and the fact that people are still writing books about it is evidence to me that we still don't know what it is. Because if we knew what it was, the last book would've been written-

**Chuck Nice** [45:41]: [laughs]

**Interviewer** [45:41]: ... and there'd be no further books on the shelf.

**Chuck Nice** [45:43]: [laughs]

**Interviewer** [45:43]: So-

**David Krakauer** [45:44]: Yeah

**Interviewer** [45:44]: ... uh, but everyone's talking about it like we fully understand it, and-

**Chuck Nice** [45:47]: Yeah

**Interviewer** [45:48]: ... so, so can you give me some access to consciousness given your tools that you have built to ask questions?

**David Krakauer** [45:56]: Yeah. I, I [laughs] I share your skepticism.

**Chuck Nice** [46:00]: [laughs]

**David Krakauer** [46:01]: I think a lot of this is just baloney, um, the consciousness stuff, to be honest, and I think we really don't understand it, and hence more and more terrible books being written on the topic.

**Interviewer** [46:12]: [laughs]

**David Krakauer** [46:13]: So...

**Chuck Nice** [46:13]: Well, I think this is a good time for me to announce my forthcoming book-

**Interviewer** [46:16]: [laughs]

**Chuck Nice** [46:17]: ... The Last Book on Consciousness.

**David Krakauer** [46:19]: There are, well, you know this, there are just many schools of thought here, and in my world, most of the rigorous work, and I'm not saying it's great work, I'm just saying it's rigorous work, is looking for quantifiable metrics, measurements that correlate with the conscious state. So f- let me make that clear. So I measure your brain, right? I write down some equations. I calculate some number, and I measure your brain when you're sleeping, I measure your brain when you're awake and solving a problem, and I me- I measure your brain under anesthesia. And it turns out that that number that I calculated, I say, "Wow, look at that. That number's high when you're waking and solving a problem, and it's near zero when you're under anesthesia or sleeping." And so this is sometimes called the neural correlates approach to consciousness. Doesn't tell you what it is. It just says that there's some formalism that allows you to measure it.

**Interviewer** [47:15]: You found a correlation.

**Chuck Nice** [47:17]: Right.

**David Krakauer** [47:17]: You found a correlation, right? And, and maybe that's useful, right? If you go under anesthesia and you're gonna have your big toe removed, I'd rather that thing was near zero than at its maximum. So but that's sort of the best of it. Um, when it comes to actually theories of what it is, honestly, qualitatively it seems to be something about the tiny little attention window that the human brain has to operate on large sets of data. And just to be explicit about this, every mathematician knows that every hard problem is solved by their unconscious mind, right? There is a very famous book written on this by someone called Hadamard, and it's called The Mathematician's Mind, and he interviewed everyone. He interviewed Einstein, Poincaré, looked at the journals of Gauss, and they all say the same thing. They say, "You know, it's a really hard problem. The best thing I can do is think about it, and then stop thinking about it. You know, I have a nice meal, I go for a run," whatever you do, and then somehow through some epiphany, the, the pres- the solution presents itself to me.

**Interviewer** [48:18]: I'm pretty sure Einstein didn't go on runs. I'm just pretty sure about that.

**David Krakauer** [48:21]: Yeah, yeah. He played the violin.

**Interviewer** [48:23]: [laughs] I don't think he was a fitness guru. [laughs]

**David Krakauer** [48:26]: He smoked his ... I-

**Interviewer** [48:28]: [laughs]

**David Krakauer** [48:28]: You know, he did something in place of going for a run.

**Interviewer** [48:30]: Or played his violin even. Yeah, sure.

**David Krakauer** [48:32]: He played his violin. He went walking with Kurt Gödel. You know, he did his thing. But the interesting point there is that, so consciousness is not about solving the hard problem. Um, it's about that little window of attention that is focused on some part of the problem, and, um, most of the current formalisms don't really give us much of an insight into how that might work. So I, I actually do not like a lot of this stuff, to be honest.

**Interviewer** [48:56]: So in the, in the, I didn't read the book, but I saw the film I, Robot, which is based on the story by Isaac Asimov.

**Gary O'Reilly** [49:02]: Mm-hmm.

**David Krakauer** [49:02]: The Will Smith one?

**Gary O'Reilly** [49:03]: Yeah.

**Interviewer** [49:03]: Yeah. [laughs] The Isaac Asimov one. But yes, Will Smith. [laughs]

**David Krakauer** [49:07]: [laughs]

**Interviewer** [49:07]: Yeah, the Will Smith story.

**David Krakauer** [49:09]: Yes, the Will Smith story. [laughs]

**Interviewer** [49:12]: So the, the robots, b- because they're all humanoid robots, there are these large vans that have robots that are n- not, that are decommissioned or that... But they're still kind of alive, but they just have no purpose until they're programmed for their utility, to be your partner, to be your whatever. And in the van, the robots grouped with each other. They weren't just maximizing their distance, and their pattern was not random. And someone asked about that, "What do you know about this?" And they said, "We don't know what's causing this. What we do know is that there's a lot of residual programming that was never fully cleared out when we added new utility to these things." And this is exactly evolution, okay? There's leftover stuff-

**David Krakauer** [50:05]: Right

**Interviewer** [50:05]: ... in us-

**Gary O'Reilly** [50:06]: Mm

**Interviewer** [50:06]: ... from a time w- that we don't need it anymore.

**David Krakauer** [50:08]: Right.

**Interviewer** [50:08]: So what the hell is it doing in our head?

**David Krakauer** [50:11]: It's the reason why sometimes I feel the need to eat flies.

**Interviewer** [50:14]: [laughs]

**Gary O'Reilly** [50:15]: That explains a lot.

**Interviewer** [50:16]: It's your reptilian-

**David Krakauer** [50:17]: It's my reptilian brain.

**Interviewer** [50:19]: Your, your gecko brain.

**David Krakauer** [50:19]: Yeah, just, yeah, exactly. [laughs] Just going crazy.

**Interviewer** [50:21]: So I was intrigued that th- it was the leftover programming that was not refreshed in the continued evolution of humans or, in the case of those robots, the continued layering on to the functionality of them, and there's legacy software-

**David Krakauer** [50:40]: Right

**Interviewer** [50:40]: ... that you don't know what it's doing. So that was... I, I was intrigued by that. I just wanna share with you that observation.

**David Krakauer** [50:45]: Yeah. I mean, again, I mean, a, a, a lot to talk about, and I think... Do you know actually my colleague here, who you probably all know, um, who recently passed away, Cormac McCarthy, the novelist, he wrote a beautiful essay on this that he called The Kekulé Problem, which is about this moment of insight. And this was the discovery by Kekulé of the benzene ring, as they all might... Oh, he saw it in a dream. And Cormac was fascinated as a writer, as a novelist, with this question of where is this coming from? I'm sitting down to write a, a book, and somehow my brain is instructing my hand, but I couldn't tell you exactly what's gonna happen at the end of that sentence. It's just sort of coming out. And so he, over the course of time, introspectively came to believe that he was getting these instructions from his unconscious mind. Now, and not in a mystical sense, just he wasn't working it out, right? [laughs] And to your point, the, the po- if you look at the history of life on Earth, most of evolution up until very recently took place without language, right? And presumably, most organisms being run by a set of automatic programs of the kind that you just described in the van with the robots huddling, like starlings.

**Gary O'Reilly** [51:56]: Mm.

**David Krakauer** [51:56]: And that we superimposed above that this kind of very thin layer [laughs] of abstraction, um, and self-awareness. But most of the computation is not being done by that thin layer. And, and so-

**Interviewer** [52:09]: Oh.

**Gary O'Reilly** [52:10]: Yeah. That's very-

**David Krakauer** [52:10]: You know, what, what, what, what-

**Interviewer** [52:12]: Yeah

**David Krakauer** [52:12]: ... is true-

**Gary O'Reilly** [52:12]: I love that

**David Krakauer** [52:13]: ... right, is that that little thin layer gives us one thing that we're not aware any ani- other animal can do.

**Gary O'Reilly** [52:19]: Yeah.

**David Krakauer** [52:19]: Which means that we can communicate our understanding.

**Interviewer** [52:23]: Mm-hmm.

**Gary O'Reilly** [52:23]: Mm.

**David Krakauer** [52:24]: They can communicate other things, but we can communicate our understanding. I can give you Newton's laws. I can tell you about Darwin's theory of evolution, right?

**Interviewer** [52:30]: Mm-hmm.

**David Krakauer** [52:30]: And that superpower of humans that comes from very few neurons, I imagine, right, sits on top of exactly all of that programming that evolution gave us over the course of-

**Interviewer** [52:42]: Mm

**David Krakauer** [52:42]: ... hundreds of millions of years.

**Gary O'Reilly** [52:43]: Wow. Oh.

**Interviewer** [52:43]: So I got one last question for you.

**David Krakauer** [52:45]: Oh, but I've still got more. But you ask your question.

**Interviewer** [52:46]: No, no, we, we, we, we, we're like, we-

**David Krakauer** [52:48]: We're asking more questions. I'll sit and talk to myself then. [laughs]

**Gary O'Reilly** [52:52]: [laughs]

**Interviewer** [52:52]: We're, we're in rap mode. Uh-

**David Krakauer** [52:55]: Excellent

**Interviewer** [52:55]: ... we're in rap, not the MC-

**David Krakauer** [52:57]: No, I know

**Interviewer** [52:57]: ... kind of rap mode

**David Krakauer** [52:58]: ... what mode you mean, yeah.

**Interviewer** [52:58]: We're rap mode here.

**David Krakauer** [52:59]: Mm-hmm.

**Interviewer** [53:00]: So I just have to go there because it's, it fascinates us all. Well, I think about it all the time. I can't speak for others. Can you estimate, based on your toolkit, how intelligent we are relative to how high intelligence can get in the universe? So that-

**David Krakauer** [53:21]: Oh, wow

**Interviewer** [53:22]: ... are, are, are we smart enough to figure out how the universe works, or are we just complete idiots, and some higher alien is just gonna come down and just look at us like we are earthworms in our capacity to de- deduce the nature of the world?

**David Krakauer** [53:36]: Yeah. That, that's, uh, really interesting. I mean, one of the areas I work on is on tools and artifacts. You know, the abacus, the sextant, the quadrant, the Rubik's Cube. Yeah, all that good stuff.

**Gary O'Reilly** [53:48]: Here comes the sextant.

**Interviewer** [53:48]: Okay, here comes the shelf.

**David Krakauer** [53:49]: It comes-

**Interviewer** [53:50]: Got my sextant here, and I've got three Rubik's Cubes up on the other shelf. Just show and tell. [laughs]

**David Krakauer** [53:56]: Do you know that's, we could-

**Interviewer** [53:57]: And I'm sitting on the abacus. [laughs]

**David Krakauer** [53:59]: [laughs] I hope not. I mean, there's an important point in that because human intelligence has always been about ingenious outsourcing to artifacts and tools, including mathematics, right? There, you could not calculate the orbit of a planet without conic sections or the calculus, right? And I think that, so I think human intelligence in that respect is unlimited, uh, because we'll just continue to build tools that are kind of adjuncts to our capabilities. And what makes AI interesting, and I know that-

**Interviewer** [54:32]: I just want you to know that I can compute orbits-

**David Krakauer** [54:35]: Nice

**Interviewer** [54:35]: ... with this abacus. [laughs]

**David Krakauer** [54:37]: Nice. No, I love it.

**Interviewer** [54:38]: No, I'm lying. I'm totally lying right there. Yeah, this is an authentic-

**David Krakauer** [54:42]: [laughs]

**Interviewer** [54:42]: ... Chinese abacus.

**David Krakauer** [54:43]: Yeah, I can see.

**Interviewer** [54:44]: Yeah.

**David Krakauer** [54:44]: I can see that.

**Interviewer** [54:45]: Mm-hmm.

**David Krakauer** [54:45]: But I think, so just to your point, I think that what's really, and I... Okay, this is, I'll just tell you very quickly, I classify tools into two categories: what I call complementary cognitive artifacts. That's like a pencil or an abacus or a sextant.

**Gary O'Reilly** [55:02]: Mm.

**David Krakauer** [55:02]: And there's another kind of tool that I call a competitive- Cognitive artifact, and that's like a GPS machine or a large language model, right? One of those sets, the complimentary ones, makes you smarter. One of those sets makes you dumber.

**Gary O'Reilly** [55:18]: Ooh.

**David Krakauer** [55:19]: Okay? And I think it's, it's the choice of humanity to decide-

**Gary O'Reilly** [55:23]: Watch on

**David Krakauer** [55:23]: ... what kind of, what kind of tool it wants to be dependent on. And so my fear now is we're outsourcing our capabilities to competitive artifacts, and not to things like future abaci, which actually would make us smarter.

**Gary O'Reilly** [55:37]: Wow.

**Interviewer** [55:38]: Oh, man.

**Gary O'Reilly** [55:38]: Do I have time for my question? I've got-

**Interviewer** [55:40]: I, I don't know. I don't think so.

**Gary O'Reilly** [55:42]: Well, I'm asking it anyway.

**Interviewer** [55:43]: Go ahead, ask it. Come on.

**Gary O'Reilly** [55:44]: All right.

**Interviewer** [55:44]: All right.

**Gary O'Reilly** [55:45]: So-

**Interviewer** [55:45]: Let the man ask his question

**Gary O'Reilly** [55:46]: ... David, you said life is problem-solving. So why has the universe created life, and what is the problem it's trying to solve?

**David Krakauer** [55:57]: Ooh. So I, you know, I can, I can tell you the horribly cynical answer to that question.

**Gary O'Reilly** [56:03]: Go on.

**Interviewer** [56:04]: Yes, please.

**David Krakauer** [56:05]: This horribly cynical answer to that question is that life is the most efficient way of returning to thermodynamic equilibrium.

**Interviewer** [56:15]: Oh, man, that's terrible.

**Gary O'Reilly** [56:17]: [laughs]

**Interviewer** [56:18]: That's... [laughs]

**David Krakauer** [56:20]: Because life is the most efficient generator of entropy.

**Interviewer** [56:25]: Right.

**David Krakauer** [56:26]: And, um, if you think about what we do when we build factories, and what we're essentially doing is we're turning ordered states into disordered states, and that the cynical answer to your question really is, is, is life is a kind of suicide by the universe.

**Interviewer** [56:41]: Yeah, I was about to say, what you, what you really just said is, "It's all for nothing." [laughs]

**Gary O'Reilly** [56:48]: [laughs]

**Interviewer** [56:48]: But that's not true either, bec- it's what we make it.

**Gary O'Reilly** [56:50]: Is there an answer-

**Interviewer** [56:51]: However, yeah

**Gary O'Reilly** [56:51]: ... that isn't cynical, just so as we can have it on a-

**David Krakauer** [56:53]: [laughs] No

**Gary O'Reilly** [56:54]: ... on such a down beat?

**David Krakauer** [56:55]: No, I know, I know.

**Interviewer** [56:56]: I like the, I like the cynical answer. Let's-

**David Krakauer** [56:57]: No

**Interviewer** [56:57]: ... I love it.

**David Krakauer** [56:58]: And I think, and I think the, the non-cynical answer came from the sort of idealist philosophers, and they said life was the universe's way of knowing itself, and-

**Interviewer** [57:10]: Ooh

**David Krakauer** [57:10]: ... that's also true.

**Interviewer** [57:12]: Hmm.

**David Krakauer** [57:12]: So that's the non-cynical version.

**Interviewer** [57:14]: Yeah.

**Gary O'Reilly** [57:14]: All right.

**Interviewer** [57:14]: That's very poetic.

**Gary O'Reilly** [57:15]: Yes.

**Interviewer** [57:16]: I like that.

**Gary O'Reilly** [57:16]: All right.

**Interviewer** [57:17]: That, that, that was, uh, c- Cosmos 1980.

**Gary O'Reilly** [57:19]: Okay.

**Interviewer** [57:20]: That, that was a major theme. The, the life is a way for the universe to know itself.

**Gary O'Reilly** [57:23]: Know itself.

**Interviewer** [57:23]: Yeah, yeah.

**Gary O'Reilly** [57:24]: Hmm.

**Interviewer** [57:25]: All right, we gotta, we kinda have to, like, end it here.

**Gary O'Reilly** [57:27]: Time's up.

**David Krakauer** [57:28]: Right.

**Interviewer** [57:28]: But we could've gone on three more hours.

**David Krakauer** [57:30]: Yes.

**Interviewer** [57:30]: Clearly.

**David Krakauer** [57:31]: Yes.

**Interviewer** [57:32]: Clearly. Well, delighted to first meet you, and to hear-

**David Krakauer** [57:35]: Nice to meet you

**Interviewer** [57:35]: ... what you're into. And I'm glad, as president of the institute, you get to still do work in your favorite topic.

**Gary O'Reilly** [57:43]: Yeah, but the question is, are you glad?

**Interviewer** [57:46]: [laughs]

**David Krakauer** [57:46]: [laughs] I am glad. I am glad.

**Interviewer** [57:48]: Okay.

**David Krakauer** [57:48]: You can't do this job unless you also do science.

**Interviewer** [57:51]: Yes, good. That's h- as it should be, and often how it's not. Yes.

**David Krakauer** [57:55]: Mm-hmm. Absolutely.

**Interviewer** [57:56]: Uh, so, uh, uh, David, thank you for joining us here on Star Talk.

**David Krakauer** [57:59]: Thank you so much for having me, in these horribly dark times, so I appreciate the fact that we get to talk about intelligent things in a stupid world.

**Interviewer** [58:07]: [laughs]

**David Krakauer** [58:07]: I value that.

**Interviewer** [58:08]: Thank you for that.

**Gary O'Reilly** [58:09]: Right, there you go.

**Interviewer** [58:10]: [laughs]

**David Krakauer** [58:11]: All right.

**Interviewer** [58:11]: There you go. All right, Chuck.

**David Krakauer** [58:12]: Ah, it's always a pleasure.

**Interviewer** [58:13]: Gary.

**Gary O'Reilly** [58:13]: Pleasure, Neil.

**Interviewer** [58:14]: Feeling good here.

**Gary O'Reilly** [58:15]: Yeah.

**Interviewer** [58:15]: This has been Star Talk Special Edition, the complexity version of our special edition. Neil deGrasse Tyson here, as always, bidding you to keep looking up. [upbeat music]

