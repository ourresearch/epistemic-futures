---
title: "Blaise Agüera y Arcas: What is Intelligence?"
person: blaise-aguera-y-arcas
section: by
type: talk-transcript
year: 2025
venue: ""
source_url: https://www.youtube.com/watch?v=qqhEEovtKgw
retrieved: 2026-08-15
content: full-text
transcription:
  method: asr
  asr_model: elevenlabs-scribe_v2
  diarized: true
  speaker_labels: inferred   # ASR diarization + LLM naming (claude-sonnet-4-6); not ground truth
  duration_min: 14
notes: "PROVENANCE: machine-transcribed from AV via ElevenLabs Scribe v2 (diarized) + LLM speaker-naming pass. Speaker labels are inferred, not authoritative. Layer-2 (mildly lossy) per charter, not camera-raw."
---

# Blaise Agüera y Arcas: What is Intelligence?

*Speakers (inferred):* speaker_0=Blaise Aguera Y Arcas, speaker_1=Interviewer

## Transcript
**Blaise Aguera Y Arcas** [00:00]: If we apply our, our minds, if we apply our intelligence in a step-by-step way, um, then, uh, it, it allows us to scale intellectual cliffs that we wouldn't be able to leap in one bound. And, and, and AI models work just the same way. [gentle music]

**Interviewer** [00:21]: Welcome to Closer to Truth. I'm speaking with Blaise Aguera y Arcas about his vital new book, What Is Intelligence? Lessons From AI About Evolution, Computing, and Minds. Blaise is vice president and a fellow at Google, where he is the CTO of Technology and Society and founder of Paradigms of Intelligence, which reimagines the foundations of AI. Projects include biologically inspired approaches to computation, efficient AI hardware, the predictive modeling hypothesis, which we'll discuss, the social scaling of AI, and even artificial life. Welcome, Blaise. It's great to meet. I love the book, What Is Intelligence?

**Blaise Aguera Y Arcas** [01:04]: Thank you so much, Robert. I'm really glad to be on.

**Interviewer** [01:06]: Look, it's a remarkable vision, a really a tour de force guide for our AI, uh, age. Uh, but a unique feature of the book, and I've read a lot of AI books and neuroscience [chuckles] books over the years, especially recently. But your book, as I see it, takes a recursive approach between AI on the one hand, and humanity's biggest questions of evolution and mind and society, with each enhancing understanding of the other in an iterative way. I- if I got that right, how did this way of thinking come about?

**Blaise Aguera Y Arcas** [01:43]: That's a, that's a great observation and, uh, and a great, and a great question. Um, yes. So I... You know, my, my role really is more as an engineer at, at Google than as a natural scientist. But, um, my training is in, is in the natural sciences, you know, originally in, in physics and then in computational neuroscience. And I am really interested in, in those big questions. Um, I feel like throughout the, the sort of earlier part of the history of AI, the science was ahead of the engineering in a lot of respects. Uh, you know, and, and that's why neural net architectures, uh, you know, really up until the transformer were largely, uh, neuroscientifically inspired. And, and it was, you know, people working at that intersection, uh, between neuroscience and, and machine learning who made the, the key contributions. But that has kind of flipped around recently, uh, where the technology or the practice is ahead of our understanding, ahead of the science.

**Interviewer** [02:40]: Mm-hmm.

**Blaise Aguera Y Arcas** [02:40]: Uh, it reminds me a little bit of the way things were, um, in the 19th century with steam engines and thermodynamics, where, you know, it was actually the technology of the Industrial Revolution that, that propelled, um, the physics of, of thermodynamics and statistical physics and so on. So I feel like we're in one of those moments now.

**Interviewer** [02:58]: Yeah, fascinating. All right. Let's, uh, talk about the, um, the nature of intelligence. And you frame the question, what is intelligence? And we, we wanna get a definition because there are a lot of different understandings of that, as you point out in the book, where cognitive psychologists may disagree with your approach to intelligence as versus, uh, AI. But I'd like to do it in the context of the so-called two holy grails, uh, artificial general intelligence, AGI, and then the magical artificial super intelligence, the so-called singularity, ASI. So let's start with a definition of intelligence as you see it, what is intelligent, and then move on to these, um, uh, uh, uh, bigger concepts.

**Blaise Aguera Y Arcas** [03:40]: Right. Well, maybe, maybe I can begin with, um, AGI versus ANI, or artificial narrow intelligence, because, you know, this was a distinction that, that, that I think first got made around the year 2000. Um, and it happened because, you know, when we were kids growing up, I mean, we're in slightly different generations, but I think this was true, you know, for both of us when we, you know, first heard the term artificial intelligence. It was supposed to be, you know, robots and, and, uh, you know, systems that, that you could have, you know, conversations with the way you could with people about, about anything. Uh, and, and that would be, you know, broadly capable in the ways that we are, that, uh, in the ways that, that humans are. And, um, and then, uh, the term artificial intelligence began getting applied to artificial neural nets that had been trained to do specific tasks like, you know, handwriting recognition or face recognition, um, uh, you know, or even, you know, face detection in a, in a, in a digital camera or something. And, you know, the, the reason they were called that, you know, is because they were using neural nets. Uh, so there's a, there is a kind of brain-like technology behind them, or brain-inspired technology behind them, but you can't have a conversation with any of those things. Uh, they were trained using supervised learning, which means that the best they can do is to literally just, you know, reproduce the, the judgments, uh, in, in the training data to get a, to score 100% on the specific test, uh, you know, of, of skill that they're trained on. So, you know, that, that was artificial narrow intelligence. And then the term artificial general intelligence was coined to just mean what we originally meant when we said AI.

**Interviewer** [05:14]: Ah.

**Blaise Aguera Y Arcas** [05:15]: Uh, so I actually found it very confusing when, uh, we started to get general purpose, um, uh, chatbots that, that were broadly capable. Uh, you know, initially at, at, at Google Research, we had, um, Meena and then LaMDA, which, which, uh, didn't, you know, didn't really get shown to the public. And then, of course, ChatGPT came along and, and, uh, you know, Gemini and Claude and various others. Uh, if you took any of those systems and transported them back to the year 2000, I'm sure that, you know, anybody in their right minds would have said, "Yeah, you know, this is AGI. This is what we meant." But, uh, but somehow we've had a sort of moving of the goalposts.

**Interviewer** [05:55]: Hmm.

**Blaise Aguera Y Arcas** [05:55]: Uh, you know, at least that's, that's my interpretation of what's happened, uh, you know, over, over the last, uh-

**Interviewer** [06:00]: That's right

**Blaise Aguera Y Arcas** [06:01]: ... few years. Uh, where nobody wants to admit that it's, that it's, uh, you know, that it's AGI and, and they want to ascribe to AGI some other properties. Maybe it has to do with having a soul or having agency, whatever that means, uh, or, or some other ineffable thing.

**Interviewer** [06:14]: Yeah. So that's the key difference that the, the word general today a- adds this, uh, other concept that puts some, uh, intrinsic, um, capabilities in- AI that are different than, than what would be easily predictable from the training data.

**Blaise Aguera Y Arcas** [06:34]: Right. Um, when we began doing unsupervised training, meaning that, uh, you know, we began training these models to predict texts, uh, with large, uh, corpuses of, of stuff from the internet that includes conversations between people and so on, and, and then they can generalize from that, from that training so that you pose a word problem and it can say, "Here's the answer." Do coding or write poetry or do whatever else, including tasks that weren't in the training data. At that point, I, I think it's clear that we have a generality. We have general intelligence, and that's, that's why these, that's why these systems are so popular, uh, with, with so many people. They're not doing... They're not good for doing just one specific thing or a few specific things.

**Interviewer** [07:15]: You contrast in the book where you believe that AI today is intelligent, but that you say many cognitive scientists would not use that term. Uh, is that, is that just an issue of semantics or, or is there a real substance, uh, in terms of understanding what AI is doing?

**Blaise Aguera Y Arcas** [07:33]: Um, I think there are a few reasons, uh, that, that, that, that debate is, is, uh, is there. One of the reasons might just be that there was kind of no moment at which, uh, at which the systems crossed some very obvious threshold. You know, they were just sort of ma- making not a lot of sense, but generating words and then, you know, slowly the coherence length, you know, of like how, how long they, they could kind of make sense grew, you know, until now. You know, you can, you know, input a prompt and get an entire sort of reasoned, you know, long reasoned argument. And there was no moment at which it felt like we crossed a threshold, so maybe it's a little bit of a, you know, uh, boiling the frog kind of story where-

**Interviewer** [08:13]: [laughs]

**Blaise Aguera Y Arcas** [08:13]: ... you know, there just wasn't a, wasn't, wasn't a moment.

**Interviewer** [08:15]: Right.

**Blaise Aguera Y Arcas** [08:16]: Um, I think that for, uh, for some people, uh, especially from the cognitive, uh, science community, um, there were ideas that we would, we would figure out some magic algorithm, that there'd be some moment when we would understand the trick of intelligence and that that would allow us to build it. And in a way, there was no trick. Uh, you know, these, uh... We were building, uh, you know, models that did next word prediction, uh, just to, you know, to power the smart keyboard in Google phones-

**Interviewer** [08:44]: Mm-hmm

**Blaise Aguera Y Arcas** [08:44]: ... uh, you know, back in the early part of last decade. And, um, and when we were doing that in, in my team at Google, we never imagined that by just scaling those models up, you know, you would get systems that could answer word problems correctly. We always... We, we agreed with the cognitive scientists that some trick would be needed, some fairy dust to make, to make it generally intelligent. So we were as surprised as anybody when, um, you know, when, when it started to get those things right. Um, but, but there was no, there was no moment and there was no trick.

**Interviewer** [09:11]: Well-

**Blaise Aguera Y Arcas** [09:11]: So I think that's part of the problem

**Interviewer** [09:12]: ... describe then the transformer moment, the 2017 paper from Google Research, Attention Is All You Need, because some people, and you, you in your book, have pointed that that's a, that was kind of a critical milestone in terms of the transformation of AI.

**Blaise Aguera Y Arcas** [09:27]: Yeah. It was a watershed. And, and all of the modern systems are based on transformers of one kind or another. So it was, it was a new architecture for neural networks, um, uh, for doing in particular, uh, sequences of, uh, for predicting sequences of words or tokens. Um, you know, the, the details of it are a little bit involved, uh, and it is, I would say, at least superficially, the least brain-like of the artificial neural net designs that have, you know, that have been a big deal in, in the last few decades. Um, it was mostly inspired by engineering concerns. Uh, it was really a method for being able to do, uh, prediction of next words or tokens that was highly parallel in terms of how it could be trained.

**Interviewer** [10:11]: Hmm.

**Blaise Aguera Y Arcas** [10:12]: Uh, and, and that also allowed for a long context window, meaning, meaning a, uh, a lot of previous text could influence what, uh, what the, what the next predicted token could be.

**Interviewer** [10:22]: And that, and that this transformer model is now ubiquitous i- in terms of all of the platforms.

**Blaise Aguera Y Arcas** [10:29]: Yes. Yes. But, uh, you know, I, I'm not sure that there's anything, uh, so magical about that particular architecture. Uh, I think i- in many ways it just happens to be, um, general and it happens to be a good fit with, uh, with our hardware and with the way we can parallelize training in data centers. Uh, so you know, there, there's a lot of evidence that, that, that just this idea of predicting next tokens and doing unsupervised training, meaning modeling large corpora, is really the key, not necessarily the details of the model.

**Interviewer** [11:01]: The astonishing thing is just predicting the next token, the next word, or the next part of a word, uh, can lead to the remarkable, um, uh, evidence that we all see today. Uh, and that, that's still, that's still... You can understand it, but you're still baffled. [laughs]

**Blaise Aguera Y Arcas** [11:16]: Yeah, exactly.

**Interviewer** [11:18]: Uh, you, you make a fascinating comment in the book, uh, uh, that, uh, LLMs perform better when asked to show their work. Uh, i- is that true and why would that be?

**Blaise Aguera Y Arcas** [11:31]: Uh, so the reason that, um, so-called, uh, chain of thought reasoning, uh, is, is helpful, meaning, meaning that, uh, that the model, you know, is, is not just giving you the answer, but is working it out, uh, you know, and, and, and sort of, uh, ex- exa- examining its own outputs while generating new outputs, is the same reason that, you know, if you're teaching a math student, uh, you know how to solve an arithmetic problem, you say, "Show your work." You know, don't just leap to the answer. Uh, you know, write it out. Um, it, you know, it's that if we apply our, our minds, if we apply our intelligence in a step-by-step way, um, then, uh, it, it allows us to scale intellectual cliffs that we wouldn't be able to leap in one bound. And, and, and AI models work just the same way.

**Interviewer** [12:15]: Y- yeah, but, but what, what I would think is that it was doing that anyway without us asking it, because that's the only way it could work. It would have to go step by step. [clears throat] So all we're doing is asking it to articulate it so that we could see it. Does that change the internal dynamics of what it actually does?

**Blaise Aguera Y Arcas** [12:37]: Um, no. Uh, it, it changes, uh, its, uh, it changes its mood, if you like.

**Interviewer** [12:43]: [laughs] Well.

**Blaise Aguera Y Arcas** [12:44]: You know, it, it's, it's really, it's really, um-

**Interviewer** [12:46]: That's a dangerous-

**Blaise Aguera Y Arcas** [12:47]: ... a cultural attitude.

**Interviewer** [12:48]: That's a very-

**Blaise Aguera Y Arcas** [12:49]: Yeah

**Interviewer** [12:49]: ... loaded phrase. [laughs]

**Blaise Aguera Y Arcas** [12:51]: Yeah. Well, you know, they, they, they act in accordance with, um, with their, their model of themselves, which, which is built over the course of the interaction. You know, we, we often have, um, system prompts which are kind of like a, you know, a, you know, this is who you are, this is how you behave, uh, kind of starting point. But that then gets augmented with, with the whole interaction so far. So if you say, "And by the way, you're a careful thinker, and think about this stuff step by step," they will do better, again, in just the same way that, you know-

**Interviewer** [13:19]: Oh

**Blaise Aguera Y Arcas** [13:19]: ... a human student will if you say-

**Interviewer** [13:21]: Okay

**Blaise Aguera Y Arcas** [13:21]: ... you know, "You want to be careful about this. Think step by step."

**Interviewer** [13:24]: Okay. So just as I say write in the style of Shakespeare or Ogden Nash, i- if, if you say show your work, it will, it will e- emphasize that aspect of it.

**Blaise Aguera Y Arcas** [13:34]: Exactly.

**Interviewer** [13:34]: That makes sense.

**Blaise Aguera Y Arcas** [13:35]: Exactly.

**Interviewer** [13:37]: [outro music] Thank you for watching. If you liked this video, please like and comment below. You can support Closer to Truth by subscribing. Closer to Truth is now accepting your tax-exempt donations. Please come to closertotruth.com/donate. Thank you very much for supporting us, and thanks for watching.

