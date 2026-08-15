---
title: "Fearing AI is Like Fearing Yourself"
person: blaise-aguera-y-arcas
section: by
type: talk-transcript
year: 2023
venue: "The Stranger"
source_url: https://www.youtube.com/watch?v=QCdSJ8E3qmE
retrieved: 2026-08-15
content: full-text
transcription:
  method: asr
  asr_model: elevenlabs-scribe_v2
  diarized: true
  speaker_labels: inferred   # ASR diarization + LLM naming (claude-sonnet-4-6); not ground truth
  duration_min: 48
notes: "PROVENANCE: machine-transcribed from AV via ElevenLabs Scribe v2 (diarized) + LLM speaker-naming pass. Speaker labels are inferred, not authoritative. Layer-2 (mildly lossy) per charter, not camera-raw."
---

# Fearing AI is Like Fearing Yourself

*Speakers (inferred):* speaker_0=Interviewer, speaker_1=Blaise Aguera Y Arcas

## Transcript
**Interviewer** [00:00]: [upbeat music] Okay, here we go. Uh, we're here [laughs] at, um, at The, uh, Hideout, uh, on First Hill. A bar with lots of art in it, and, uh, it's been, uh, running maybe even for close to 20 years. But, uh, um, uh, w- I was here not too long ago, uh, to have a conversation with a leading figure in, uh, in AI. His name is Blaise Aguera, uh, y- Agüera y Casas. And, uh, and, um, and, um, what I wanted to do was sort of pick up where we left off. Um, we are gonna post a bit of the conversation w- we had the first time on the web, and please go and read it because it is a fascinating document. Um, but this time I really wanted to talk more about AI and, um, and exactly, um, where it sort of stands right now. Because a lot of people, as you know, uh, are talking about it, particularly ... It's so funny because I think I talked to you right before the explosion, right? The, the media explosion happened, right? And it was still sort of in this sort of like, you know, is it real or is it not real, right? Where is it going? There was no uncertainty. And then there was ... you know, and, and nobody was banking on it like in the way they are now, right? So somewhere between 2001, if I'm correct, and, uh, even if it was in 2002, but sometime between that and today in 2023 at the end of the year, the, the whole industry has been transformed, right? And I'm trying to figure out what happened in ... What happened between that per- I ... We know that, that, that certain companies got, got, you know, um, these, these, these, these incredible evaluations on the market, and so on and so on, and, uh, but, but ... And then, then there became the drama around certain figures in AI that became almost Shakespearean. What, what, what, what happened between, between this sort of quieter period and this, you know, expansive, loud, and now almost transformo- transformational in the sense of, uh, I mean, the market, right? Uh, uh, uh, uh, a period in AI. What, what is it that took place?

**Blaise Aguera Y Arcas** [02:14]: Well, there are a bunch of ways of answering that.

**Interviewer** [02:16]: Yeah?

**Blaise Aguera Y Arcas** [02:16]: So, um, the, the technical answer is unsupervised large-scale sequence learning, uh, using the transformer model. And, um, uh, and we can go a little bit into why that, why that technical answer has led to all of the furor that we see around-

**Interviewer** [02:32]: No, no. Go ahead

**Blaise Aguera Y Arcas** [02:32]: ... AI now.

**Interviewer** [02:33]: I wanna ... Go, go, go, go.

**Blaise Aguera Y Arcas** [02:34]: Yeah. Okay.

**Interviewer** [02:34]: Yeah, yeah. Yeah, go, go.

**Blaise Aguera Y Arcas** [02:35]: So, um, so in the, in the 2010s we were already doing a lot of AI.

**Interviewer** [02:38]: Mm-hmm.

**Blaise Aguera Y Arcas** [02:39]: But almost all of it was so-called supervised learning, meaning that the most that you could get out is what you had put in. So if it's, for example, you know, uh, face recognition, then all you get is face recognition.

**Interviewer** [02:51]: Mm-hmm.

**Blaise Aguera Y Arcas** [02:51]: If it's character recognition, then, you know, the performance is, like, how well do the characters get recognized. Or, or a speech understanding, you know, it's how well does the speech get recognized. When, when people were talking about that as AI, it was a little weird because, you know, it's, it's obviously, uh, something that computers had not been good at doing before and were good at doing now. But there's no sense in which you could call that, like, artificial intelligence in the usual, in the usual sense. You can't, you know, get-

**Interviewer** [03:14]: Yeah

**Blaise Aguera Y Arcas** [03:14]: ... something that has learned how to play chess to fold your laundry for you or, you know, have a conversation with it. You can't even say to a good chess-playing, you know, classical AI system, like, "Okay, let's, let's go on playing now, but let's, let's imagine the pawns can all move backwards." You know? You couldn't even do that, right?

**Interviewer** [03:30]: Right.

**Blaise Aguera Y Arcas** [03:30]: Um, and, and so the big change was that, um, language, language models began to come on the scene. So these are, these are-

**Interviewer** [03:37]: Ah, right

**Blaise Aguera Y Arcas** [03:37]: ... models that are trained on very, very large corpuses of, of, of, of natural language, and they're not trained to do any specific thing. They're just trained to predict. And, um, you know, we've always known that prediction was an AI complete problem.

**Interviewer** [03:51]: Mm-hmm.

**Blaise Aguera Y Arcas** [03:51]: Meaning that, uh, you know, depending on what the text is, the next word, if you're trying to do next-word prediction, it could be trivial. You know, it could be that the previous word was Humpty, and then you know the next word is gonna be Dumpty. You know?

**Interviewer** [04:01]: Mm-hmm.

**Blaise Aguera Y Arcas** [04:01]: If it's helter, it's gonna be skelter. But it could also be a word problem, and the next word is, you know, the answer to the word problem, and then you have to do math in order to get it right. Or, you know, it could be a story-

**Interviewer** [04:09]: Right

**Blaise Aguera Y Arcas** [04:10]: ... and, uh, and the next word is the emotion that somebody feels in the story, and then you'd have to do theory of mind, which is a very sophisticated task.

**Interviewer** [04:15]: Ah, yeah.

**Blaise Aguera Y Arcas** [04:16]: Right? So we always knew that next-word prediction was AI complete, but what nobody expected was that getting a next-word predictor to just work really well would apparently solve AI. It would solve the artificial general intelligence problem. Um, and, and people ... You know, I, I was already seeing that, you know, in 2000, 2001 when, when we spoke, or 2002, because we had been building those kinds of models, uh, internally at Google. But, but they hadn't been made public yet. Uh, you know, and really-

**Interviewer** [04:43]: Ah

**Blaise Aguera Y Arcas** [04:43]: ... it was, it was OpenAI that did that in, in November of 2022, uh, with, uh, with ChatGPT, and then everybody saw what, what I had been seeing and, and a few other people, you know, in, in the field had been seeing.

**Interviewer** [04:55]: And you were with at the t- at the time you ... I know you were with Microsoft first, but this time you were with Google, right?

**Blaise Aguera Y Arcas** [05:00]: Oh, yeah, yeah. No, I've been with Google for 10 years. I've been, I've been, um, a, a VP in Google Research for, um, for quite a while, and have built up a sizable team there.

**Interviewer** [05:09]: That's right. And that's where you still are right now.

**Blaise Aguera Y Arcas** [05:11]: Yes.

**Interviewer** [05:12]: Right? And, uh, and the, and the, the, the question I want to ... I mean, uh, what exactly ... I, I noticed that, that you, you really place a big emphasis on social learning in AI. This is to me the creepiest aspect, right? Because social learning is really fundamental, right-

**Blaise Aguera Y Arcas** [05:30]: Mm

**Interviewer** [05:30]: ... to human culture.

**Blaise Aguera Y Arcas** [05:31]: Yes.

**Interviewer** [05:31]: Right? It's almost what separates us in a fundamental sense, right? From-

**Blaise Aguera Y Arcas** [05:36]: Yeah. I think, I think not almost. I think it is what separates us-

**Interviewer** [05:38]: It separates, right?

**Blaise Aguera Y Arcas** [05:39]: ... in my opinion at least.

**Interviewer** [05:40]: Right? Yeah, yeah. Because, you know, you won't find it ... I mean, it, it ex- to the extent that we have it-

**Blaise Aguera Y Arcas** [05:44]: Right

**Interviewer** [05:44]: ... in other, in other close, uh, uh, uh, relatives, chimps and gorillas and so forth. What is this ... What are you doing, you know, in this, in this res- in this regard in terms of, like, taking social learning? Meaning, um, meaning transmitting information, right, that you have, right, and to another person or another, another- Being.

**Blaise Aguera Y Arcas** [06:06]: Yeah

**Interviewer** [06:06]: And that person, right, gathering it and learning from it and making adjustments with it, right? And then communicating it to another person, right.

**Blaise Aguera Y Arcas** [06:14]: Exactly.

**Interviewer** [06:14]: And that's the, that's the separation. And how does that impact AI as a, in sort of this, in this, in this present context?

**Blaise Aguera Y Arcas** [06:21]: Yeah. It, it's a great question. Um, and I, I do think it's the secret of our success as a species, as you say.

**Interviewer** [06:26]: Yeah.

**Blaise Aguera Y Arcas** [06:26]: Um, uh, I... The, the introduction of the new book, uh-

**Interviewer** [06:30]: Yeah

**Blaise Aguera Y Arcas** [06:30]: ... that, that is coming out now, Who Are We Now?

**Interviewer** [06:31]: Yes

**Blaise Aguera Y Arcas** [06:32]: ... uh, talks a lot about, about this sort of secret of our success or what social transmission is. So, um, it's, it's a few things. First of all, you know, the, one of the main purposes of language is to not only to be able to, um, communicate, you know, the, in the, in the sense that we usually think of, to be able to just understand each other's intentions or, or express our feelings or, or what have you, but also to teach and to learn.

**Interviewer** [06:55]: Mm-hmm.

**Blaise Aguera Y Arcas** [06:56]: Uh, you know, it... You can, you can teach and learn without language by just watching somebody do something. You know, if I'm one chimp, you know, fishing for ants with a stick and another chimp is watching, you know, they can learn how to do that.

**Interviewer** [07:06]: The- Right.

**Blaise Aguera Y Arcas** [07:07]: But-

**Interviewer** [07:07]: Yes

**Blaise Aguera Y Arcas** [07:07]: ... but with language, you, the things that you can teach and learn become vastly more sophisticated. And, and language is a way that you can also, of course, teach yourself. You know, you can develop thoughts as, as, you know, you and I both do a lot of writing and, of course, we use language as a tool for thinking all the time. Um, but moreover, you get cultural accumulation.

**Interviewer** [07:26]: Right.

**Blaise Aguera Y Arcas** [07:26]: And this is the thing that no other s- Well, I, I shouldn't say no other species. There are, there are, um, orcas also have cultural accumulation.

**Interviewer** [07:32]: I totally agree. Yes.

**Blaise Aguera Y Arcas** [07:32]: There are some other animals that do.

**Interviewer** [07:33]: Yes. Yeah.

**Blaise Aguera Y Arcas** [07:33]: But no other animals that do it to the degree that we do-

**Interviewer** [07:36]: Right

**Blaise Aguera Y Arcas** [07:36]: ... that we know of. Uh, which is that not only do we learn from and teach each other, but we do it in a way that builds over the generations. So, you know, if you were to go back, uh, 100,000 years, you know, there were still humans on Earth, but I don't think we would've been, we would've looked all that distinctive relative to the other megafauna on the planet. Uh, whereas now with cumulative cultural accumulation, you know-

**Interviewer** [07:59]: Mm-hmm

**Blaise Aguera Y Arcas** [07:59]: ... you, you, you just get, you get this kind of exponential liftoff of human culture that sets us completely apart from everything else.

**Interviewer** [08:05]: Would you call social learning symbolic learning?

**Blaise Aguera Y Arcas** [08:09]: Yeah.

**Interviewer** [08:10]: Um-

**Blaise Aguera Y Arcas** [08:10]: I, I would.

**Interviewer** [08:11]: Right? And, and, and I make that, I make that distinction in, with, with, with, with, with, with, um, uh, with the idea that, uh, um, um, symbolic manipulation is, is, is, is, is, is a feature that is bizarre to me, right? Because you're talking about things that don't exist.

**Blaise Aguera Y Arcas** [08:28]: Right.

**Interviewer** [08:29]: Right?

**Blaise Aguera Y Arcas** [08:29]: Absential-

**Interviewer** [08:30]: Yes

**Blaise Aguera Y Arcas** [08:30]: ... in the, in the Piercean sense.

**Interviewer** [08:31]: In- Yes. Right. In the Piercean s- Yes. That's right. Uh, uh, this notion of, of, um, uh, in AI then we already, uh, it... This, I understand that you, you take a deep interest in language and AI, if I'm correct.

**Blaise Aguera Y Arcas** [08:46]: Yes.

**Interviewer** [08:46]: This is where you really s- find... I mean, 'cause you started in images, right?

**Blaise Aguera Y Arcas** [08:50]: Yeah. Yeah. A lot of my early work was in, was in computer vision, machine vision. Right.

**Interviewer** [08:54]: Right? But you felt that that was, that, that's a, that the real game in town was language. Is that true?

**Blaise Aguera Y Arcas** [09:00]: Yeah. I mean, I, I don't wanna, uh, uh, you know, sort of backdate my story too mu- you know, like-

**Interviewer** [09:05]: Mm-hmm

**Blaise Aguera Y Arcas** [09:05]: ... be, be too re- you know, uh-

**Interviewer** [09:06]: Yeah

**Blaise Aguera Y Arcas** [09:06]: ... I, be too revisionist about it. But yeah, I've, I've always felt that language was pretty critical for a lot of the things that we consider to be intelligence. And so, you know, in that sense, I wasn't shocked when, when we are working with language turned out to be really important.

**Interviewer** [09:18]: Where the, where, where the breakthroughs-

**Blaise Aguera Y Arcas** [09:20]: Yeah

**Interviewer** [09:20]: ... really occurred. Right? And, uh, and so what do you think? Where is this all gonna go? I mean, really, in all honesty. I mean, I mean, o- o- no, no. I wanna ask... Oh, no. I jumped, I jumped ahead of myself. And that's okay. This can stay. Um, I, I jumped ahead of myself 'cause there's a question I w- I really, that really fascinated me, and it's regarding you. And I know that there's very many versions of, of positions, right? Very many positions. A, an, an, a large number of positions, um, as to what AI can and cannot do or its value, right? Or its, you know, how it's gonna be applied under particular economic situations and so and so on. Uh, where, where are you specifically? What camp are you in? Or are you no camp?

**Blaise Aguera Y Arcas** [09:58]: Yeah.

**Interviewer** [09:58]: If you say no camp, I'm gonna be angry 'cause that's not an answer. [laughs]

**Blaise Aguera Y Arcas** [10:01]: Well, I, I, I'm pretty heterodox in my views.

**Interviewer** [10:04]: You are?

**Blaise Aguera Y Arcas** [10:04]: So, yeah.

**Interviewer** [10:05]: Yeah.

**Blaise Aguera Y Arcas** [10:05]: Um, I mean, uh, the, the camps that I have seen-

**Interviewer** [10:07]: Mm-hmm

**Blaise Aguera Y Arcas** [10:08]: ... form, uh, I have, I h- I actually have major problems with. I, I have problems with the, um, with the accelerationist-

**Interviewer** [10:16]: Yes

**Blaise Aguera Y Arcas** [10:16]: ... or existential risk camp because I, it, that looks to me quite a lot like a religion.

**Interviewer** [10:20]: Yes.

**Blaise Aguera Y Arcas** [10:20]: Um, and, uh, you know, it, like, I just, I, I have-

**Interviewer** [10:24]: Wait, wait, wait, wait

**Blaise Aguera Y Arcas** [10:24]: ... visceral reactions [laughs] against it, I suppose.

**Interviewer** [10:26]: Sorry. Let me pull my, my mic. No, no. Um, I, I, I have to say accelerationism, right?

**Blaise Aguera Y Arcas** [10:31]: Yeah.

**Interviewer** [10:31]: This is where we're gonna drive technology until it just kills itself.

**Blaise Aguera Y Arcas** [10:35]: Right.

**Interviewer** [10:35]: Kills itself.

**Blaise Aguera Y Arcas** [10:36]: It, itself or kills us or-

**Interviewer** [10:37]: Kills us us, right?

**Blaise Aguera Y Arcas** [10:37]: I mean, the, the, the effective altruists are a part of that.

**Interviewer** [10:40]: Yes.

**Blaise Aguera Y Arcas** [10:40]: Uh, you know, the existential risk community. And existential risk people who think, you know, AI is the, the, you know, is the doom of-

**Interviewer** [10:46]: Yes

**Blaise Aguera Y Arcas** [10:46]: ... humans are kind of the flip side. They're often the same people as the ones who are talking about, like, the rapture of the nerds and the singularity.

**Interviewer** [10:53]: Right, right.

**Blaise Aguera Y Arcas** [10:53]: So there's like a heaven or hell, you know, apocalypse or, or, or, uh, or transcendence version of that, and I find both of those, uh, a little weird.

**Interviewer** [11:02]: Yeah, yeah. Because-

**Blaise Aguera Y Arcas** [11:02]: So I'm not in that, I'm not in that camp. Um-

**Interviewer** [11:04]: But they almost over-privilege intelligence. This is, you know, uh, they, they, they privilege way too much the, you know, the greatness of intelligence. I've always, uh, found this to be the flaw in that argument, right? They actually, they actually say something which is purely Cartesian, right? That the whole game in town, all of it, it comes down to, right, intelligence, right? If you make an artificial heart, no one's like, everybody's like a fast asleep, right? Nobody cares about an artificial heart. But if you say artificial intelligence, everybody goes berserk.

**Blaise Aguera Y Arcas** [11:31]: Yeah.

**Interviewer** [11:31]: Right?

**Blaise Aguera Y Arcas** [11:32]: I agree that there's a, that, that a lot of that comes from a cart- a kind of Cartesian wound.

**Interviewer** [11:36]: Yeah.

**Blaise Aguera Y Arcas** [11:36]: But, but, um, but I guess, I mean, I privilege intelligence a lot too, but I think about intelligence a lot more expansively than they do. Like, that, that school of thought kind of went wild when Nick Bostrom published his book-

**Interviewer** [11:48]: Yeah. Right

**Blaise Aguera Y Arcas** [11:48]: ... Superintelligence in 2014 or 2013-

**Interviewer** [11:50]: Right

**Blaise Aguera Y Arcas** [11:50]: ... right? Which, which posited that this was all about game theory and optimization, and that the moment, you know, computers could really, you know, optimize, uh, you know, perfectly and play games perfectly, they would, you know, they would become smart in the colloquial sense.

**Interviewer** [12:03]: Right.

**Blaise Aguera Y Arcas** [12:03]: And that wasn't the case. The way we, we achieved intelligence was actually through language and, and through digesting a lot of human text-

**Interviewer** [12:11]: Right

**Blaise Aguera Y Arcas** [12:11]: ... which is really different from that idea that it's just gonna be this optimal game player, right? They're, they're not great at math. They have to be taught that.

**Interviewer** [12:17]: Right.

**Blaise Aguera Y Arcas** [12:17]: You know, in a, in a rather, in a rather, um- It's a studious and, and, and low gear kind of way. You know, they're not automatically good at logic or, or, or math or puzzles at all.

**Interviewer** [12:27]: Yeah.

**Blaise Aguera Y Arcas** [12:27]: Right? Uh, that's hard for them in the same way that it's hard for us.

**Interviewer** [12:30]: Now, back to your position.

**Blaise Aguera Y Arcas** [12:31]: Yeah.

**Interviewer** [12:31]: Where is your position?

**Blaise Aguera Y Arcas** [12:32]: Okay.

**Interviewer** [12:32]: So we got the, we got the acceleration-

**Blaise Aguera Y Arcas** [12:34]: So not, no, no to that, right?

**Interviewer** [12:35]: Yeah, yeah.

**Blaise Aguera Y Arcas** [12:35]: Um, also no to a lot of the, uh, I, I, I don't know how to, what to call it, but I guess if, if we think of that as sort of the right wing response in some way-

**Interviewer** [12:44]: Right, right, right, yeah

**Blaise Aguera Y Arcas** [12:44]: ... or the libertarian response.

**Interviewer** [12:45]: Yes. Right, right.

**Blaise Aguera Y Arcas** [12:45]: There's also a, a left wing response, which is, uh, fundamentally about labor versus capital.

**Interviewer** [12:51]: Mm-hmm.

**Blaise Aguera Y Arcas** [12:51]: And, and the, the claim there is that, you know, this is-

**Interviewer** [12:54]: That's where I'm at, by the way. That's my game.

**Blaise Aguera Y Arcas** [12:55]: That's your game. [laughs]

**Interviewer** [12:56]: Yeah, yeah.

**Blaise Aguera Y Arcas** [12:56]: But this is, but, but in this view, in this view, AI is just a reprise of the Industrial Revolution, uh, but now with intellectual labor versus, uh, manual labor, and it's all about the triumph of capital versus labor, and this leads to kind of neo-Luddism and also a denial that this is real intelligence. You know, I mean, I've seen a lot of claims that, for instance, you know, it's just a, a, a stochastic parrot, for instance, or a repackaging of the labor of all the people who made the text and, and there's no, there's nothing real there. Uh, you know, it's like a, a facade. Um, and I don't think it's a facade. I think it's, I think it's very real. Um, but I also think that it's not, it's not separate. Um, so what, what I mean by that is I, I, I, I guess I'm a believer in more than human intelligence.

**Interviewer** [13:37]: Right.

**Blaise Aguera Y Arcas** [13:38]: Right? It, it's not in- it's not just individual, it's not just intellectual, it's not just logical. And when ... The, the fact that we achieve, uh, intelligence in machines when they are literally, you know, sort of partaking in and learning human culture tells us that it is human culture that is the locus of intelligence.

**Interviewer** [13:56]: Oh, I have to tell you something. Okay, there's two ... You mentioned ... Um, no, before we jump into the other positions, I have to stop here-

**Blaise Aguera Y Arcas** [14:02]: Yeah

**Interviewer** [14:02]: ... really quickly. There is a, a, a, a, in, in the Marxist circles, particularly those that are devoted to the Grundrisse-

**Blaise Aguera Y Arcas** [14:10]: Yeah

**Interviewer** [14:10]: ... right? There is this whole thing about the machine fragment, right? In the, uh, in, in the book where it's sort of, uh, the, the term general intellect makes its appearance, right? And there's a group of intellectuals, uh, most famously Hardt and Negri, right? And, uh-

**Blaise Aguera Y Arcas** [14:29]: Michael Hardt.

**Interviewer** [14:30]: Yeah, right, who said, right, who thought that actually, right, science, those who had, uh, who had developed, uh, scientific knowledge and had accumulated all these powerful intellectual tools would actually liberate us.

**Blaise Aguera Y Arcas** [14:44]: Yeah.

**Interviewer** [14:44]: Right? So actually in, in the intellect was the path to communism.

**Blaise Aguera Y Arcas** [14:50]: Yes.

**Interviewer** [14:50]: A lot of people don't know this, right?

**Blaise Aguera Y Arcas** [14:51]: Yes.

**Interviewer** [14:51]: And they saw that as a path. And now it's really weird to hear, well, here's a tool, right, that is, right, dealing with the intellect itself, and now it's, right, given this sort of like, "Oh, my God, this is a disaster," right?

**Blaise Aguera Y Arcas** [15:05]: Right. Right. But it's not liberatory. It's the opposite.

**Interviewer** [15:07]: It's, it is a very opposite, right?

**Blaise Aguera Y Arcas** [15:08]: Right.

**Interviewer** [15:08]: And, and so to me, this is a discussion that I have not read about, at least yet, within those leftist circles, right?

**Blaise Aguera Y Arcas** [15:15]: That's right.

**Interviewer** [15:15]: We could ... Yeah.

**Blaise Aguera Y Arcas** [15:16]: And, and this is why, this is why I have problems with both the response on the left and on the right.

**Interviewer** [15:20]: Yeah.

**Blaise Aguera Y Arcas** [15:21]: Uh, like for instance, um, you know, I think we talked a little bit last time about Robert Merton-

**Interviewer** [15:25]: Right

**Blaise Aguera Y Arcas** [15:25]: ... and multiple simultaneous discovery.

**Interviewer** [15:27]: Yes.

**Blaise Aguera Y Arcas** [15:27]: Right? This phenomenon that every innovation in human history, magically it seems like it sprung to mind for dozens of people around the same time, as if they were all telepathically linked somehow.

**Interviewer** [15:37]: Right.

**Blaise Aguera Y Arcas** [15:37]: You know, the light bulb is invented by a dozen inventors, you know, within a few years of each other.

**Interviewer** [15:41]: Right.

**Blaise Aguera Y Arcas** [15:41]: We know about this because of all the patent disputes.

**Interviewer** [15:43]: Right, right.

**Blaise Aguera Y Arcas** [15:44]: And, um, I don't think that's a coincidence. You know, it happens because in order to invent the light bulb, you have to have all these precursors.

**Interviewer** [15:51]: Mm-hmm.

**Blaise Aguera Y Arcas** [15:51]: You have to have, you know, be able to blow glass and make a vacuum and e- you have, like, you have to have electricity and you have to be able to, you know, make a, make a filament, uh, and so on. And once those precursors are there, it's almost like a chemical reaction that happens in everybody's brain who, you know, has access to, uh, to those other intellectual currents. And, and, and then you start to realize, oh, in, you know, invention is actually a collective phenomenon. It's not, you know, lone geniuses.

**Interviewer** [16:15]: Right. Right, right.

**Blaise Aguera Y Arcas** [16:15]: Or, or insofar as lone geniuses exist-

**Interviewer** [16:17]: Yeah, yeah

**Blaise Aguera Y Arcas** [16:17]: ... they're, they're, they're just sort of the nucleation points of something that is larger and, and collective. So i- I think if one thinks about intelligence in that broader way, then, uh, you know, AI looks very different. It just looks like more, uh, more of the same, uh, right? It's more of our, of our collective human intelligence-

**Interviewer** [16:35]: Right

**Blaise Aguera Y Arcas** [16:35]: ... now with other vessels that, that are not necessarily within our individual skulls, as it were.

**Interviewer** [16:40]: And you call it augmented. I wanna get back to that in a minute because ... But I wanna go, so next one, right? We've got two. Position number two. You're not in these two camps.

**Blaise Aguera Y Arcas** [16:49]: Right.

**Interviewer** [16:49]: What's the n- what's the next camp?

**Blaise Aguera Y Arcas** [16:51]: Well, um, I mean, those are the two, those are the two that I've, that I've heard, that I've heard the most concentration around. I guess, I guess we could add a third, uh, camp, which I've been hearing a lot from, from, uh, countries and, you know, national intelligence communities and whatnot-

**Interviewer** [17:05]: Mm-hmm

**Blaise Aguera Y Arcas** [17:05]: ... which is that AI is all about, um, winning the AI race, you know, sort of like-

**Interviewer** [17:10]: Right, right

**Blaise Aguera Y Arcas** [17:10]: ... the space race or something.

**Interviewer** [17:11]: Yes. That's right. Yeah.

**Blaise Aguera Y Arcas** [17:12]: And a- as you can imagine, I'm not a fan of that position either-

**Interviewer** [17:14]: Yeah, yeah, yeah

**Blaise Aguera Y Arcas** [17:14]: ... because, you know, the idea that it's, that it's, um, that it's somehow about, about nation states fighting with each other for dominance-

**Interviewer** [17:21]: Right

**Blaise Aguera Y Arcas** [17:21]: ... strikes me as not in keeping with what intelligence actually is, right?

**Interviewer** [17:24]: So the USSR replace, is replaced by China in this regard.

**Blaise Aguera Y Arcas** [17:27]: Right.

**Interviewer** [17:28]: Right?

**Blaise Aguera Y Arcas** [17:28]: Right.

**Interviewer** [17:28]: Because-

**Blaise Aguera Y Arcas** [17:28]: And everybody's gotta keep up

**Interviewer** [17:29]: ... keep up and so forth and so on.

**Blaise Aguera Y Arcas** [17:31]: Yeah.

**Interviewer** [17:31]: And people are, are wondering who ... If you dominate this, then you dominate the world and so forth and so on.

**Blaise Aguera Y Arcas** [17:37]: Right.

**Interviewer** [17:37]: And there's a sort of a mythic element to that, right?

**Blaise Aguera Y Arcas** [17:39]: Absolutely.

**Interviewer** [17:40]: Because we thought ... We, we're told the space race would do this or nuclear weapons would do this and so forth and so on.

**Blaise Aguera Y Arcas** [17:46]: Right.

**Interviewer** [17:46]: But, okay, so where are you?

**Blaise Aguera Y Arcas** [17:49]: Uh, I'm in the more than human camp. Uh, I, I think that-

**Interviewer** [17:51]: Okay. Hold up, hold up.

**Blaise Aguera Y Arcas** [17:52]: Yeah, yeah. [laughs]

**Interviewer** [17:53]: What do you mean more than human?

**Blaise Aguera Y Arcas** [17:55]: Well-

**Interviewer** [17:56]: Uh, the, the, what, the more ... It sounds like something out of Blade Runner, right?

**Blaise Aguera Y Arcas** [17:59]: [laughs]

**Interviewer** [17:59]: Right? No, no, that's what he says. That's, that's Tyrell Corporation, right?

**Blaise Aguera Y Arcas** [18:03]: Well, um, uh, but the difference-

**Interviewer** [18:05]: [laughs]

**Blaise Aguera Y Arcas** [18:05]: ... the difference is that, the difference is that the Blade Runner, um, you know, the, the Blade Runner idea is about, about hierarchies or chains of being.

**Interviewer** [18:11]: Yeah.

**Blaise Aguera Y Arcas** [18:12]: Right? When I say more than human, I don't mean that there's some other thing that is above humans.

**Interviewer** [18:15]: Yeah.

**Blaise Aguera Y Arcas** [18:16]: I mean rather that intelligence is more than human and has always been. So, um, this-

**Interviewer** [18:22]: This, okay, this says a lot. Go, go, go, go, go ahead.

**Blaise Aguera Y Arcas** [18:24]: So I'm thinking-

**Interviewer** [18:24]: Yeah, yeah, yeah, yeah

**Blaise Aguera Y Arcas** [18:24]: ... I'm thinking about-

**Interviewer** [18:25]: Yeah

**Blaise Aguera Y Arcas** [18:25]: ... about the Earth as a whole. As, I know this sounds a little bit hippie-ish maybe, but the Earth as a whole is alive, you know, and we're a part of that, of that ecology. Intelligence is a part of that ecology at every scale.

**Interviewer** [18:36]: Yes.

**Blaise Aguera Y Arcas** [18:36]: Uh, you know, including evolution-

**Interviewer** [18:38]: Yeah

**Blaise Aguera Y Arcas** [18:38]: ... including learning in, in species that, that don't have big brains, but that, that learn over much longer timescales. You know, so intelligence is, is, is a continuous object that spans all of that. And, and, and in that sense, I don't see technology as some alien other. It's, it's another layer on top of that same giant planet-sized, uh, intelligent system that we are a part of.

**Interviewer** [19:01]: But some people have always theorized that bacteria essentially are a single organism.

**Blaise Aguera Y Arcas** [19:06]: Yes.

**Interviewer** [19:06]: Right?

**Blaise Aguera Y Arcas** [19:07]: Which I, which I buy.

**Interviewer** [19:08]: Right. That's been, that was sort of arrived at.

**Blaise Aguera Y Arcas** [19:10]: Yeah.

**Interviewer** [19:10]: And so this is what you're sort of hinting at, that it's, it's-

**Blaise Aguera Y Arcas** [19:12]: Yeah, it's not just bacteria

**Interviewer** [19:13]: ... yeah, right. It's all of us.

**Blaise Aguera Y Arcas** [19:14]: It's all of us. Yeah.

**Interviewer** [19:14]: These, all these, yeah, these entities are one singular organism-

**Blaise Aguera Y Arcas** [19:18]: Kind of, yeah

**Interviewer** [19:18]: ... that, that, that, uh, that exchange information-

**Blaise Aguera Y Arcas** [19:21]: Right

**Interviewer** [19:21]: ... and so on, so on.

**Blaise Aguera Y Arcas** [19:22]: It's a bigger us. I mean, it's a fractal. I mean, we, you know, we're both individuals and collectivities at, at the same time, right? Everything, everything is there at the same time.

**Interviewer** [19:28]: Okay. Well, what is the benefit of this, of your point of view? What do you see? What is the advantage over the other points?

**Blaise Aguera Y Arcas** [19:34]: Well, I think that, I think that from a... If you wanna think about this from a political perspective-

**Interviewer** [19:38]: Yeah, mm-hmm

**Blaise Aguera Y Arcas** [19:39]: ... uh, one of the advantages is that it, it, it forces us to think a lot more about symbiosis and cooperation, uh, versus the more Spencerian view of Darwin. So, you know, I mean, Darwin, Darwin, you know, originally talked both about competition and about cooperation, of course.

**Interviewer** [19:55]: Yeah, that's right.

**Blaise Aguera Y Arcas** [19:55]: But, but in the main, in the West, the, the main, um, the main proponents of the Darwinian point of view, and this led to social Darwinism and all kinds of really ugly stuff-

**Interviewer** [20:03]: Mm-hmm

**Blaise Aguera Y Arcas** [20:04]: ... focused on, on competition.

**Interviewer** [20:05]: And survival of the fittest-

**Blaise Aguera Y Arcas** [20:06]: Survival of the fittest

**Interviewer** [20:06]: ... which wasn't, which was Spencer.

**Blaise Aguera Y Arcas** [20:08]: Spencer, not Darwin.

**Interviewer** [20:09]: Not Darwin.

**Blaise Aguera Y Arcas** [20:10]: Right. And, um, whereas-

**Interviewer** [20:11]: But Darwin was dependent on Reverend Malthus.

**Blaise Aguera Y Arcas** [20:14]: Yes.

**Interviewer** [20:14]: [laughs]

**Blaise Aguera Y Arcas** [20:14]: Yes. Who, who, who had his issues, to put it mildly.

**Interviewer** [20:17]: His issues about population.

**Blaise Aguera Y Arcas** [20:19]: And about class.

**Interviewer** [20:20]: And we still have population, Malthusian population, uh, thinking. But I don't wanna get into that.

**Blaise Aguera Y Arcas** [20:25]: Yeah.

**Interviewer** [20:25]: But no, no, no, but let's go back to-

**Blaise Aguera Y Arcas** [20:26]: That is, that is in the book too, in chapter 18.

**Interviewer** [20:27]: Yes.

**Blaise Aguera Y Arcas** [20:28]: That was one of the-

**Interviewer** [20:28]: Chapter 18 of the book. No, no, no, because you do go into s- into this whole social aspect, right? Because you're interested in s- in the sociological, uh, dimension-

**Blaise Aguera Y Arcas** [20:38]: Right

**Interviewer** [20:38]: ... of the human being. And there's something that, uh, um, I wanna bring this up in a moment because I, I was really taken by it between, um, um, um... And I'm gonna say this badly because I'm not, I, I'm, my memory is still absorbing what you've written, but it's, it's, um, it is, um, it is personal, right, identity, and then I would call it impersonal identity.

**Blaise Aguera Y Arcas** [21:01]: Yes.

**Interviewer** [21:01]: I know you worded it differently, right? But-

**Blaise Aguera Y Arcas** [21:03]: Yeah. I used anonymous identity-

**Interviewer** [21:04]: Anonymous-

**Blaise Aguera Y Arcas** [21:04]: ... but I think we mean the same thing.

**Interviewer** [21:05]: Yeah, yeah. Right, right. Anonymous identity, right? And you saw this as the key to our evolutionary development, right? So that if you have a personal sociology, right, um, there's gonna be certain limitations, right?

**Blaise Aguera Y Arcas** [21:19]: Right.

**Interviewer** [21:19]: But with an impersonal one, right, you're going to... And I wanted, and, and I'm, I was fascinated, why are you mining, right, so much of this anthropology, right?

**Blaise Aguera Y Arcas** [21:30]: Yeah.

**Interviewer** [21:30]: Or sociobiology I'd even call it.

**Blaise Aguera Y Arcas** [21:32]: Both.

**Interviewer** [21:32]: Um, both, right? And, a- as a, as a, as a, as an AI thinker-

**Blaise Aguera Y Arcas** [21:37]: Yeah

**Interviewer** [21:37]: ... I mean, and-

**Blaise Aguera Y Arcas** [21:38]: It's because of that collectivity aspect that, that, um, you know, if, if you think about... I mean, and, and you were talking about language earlier.

**Interviewer** [21:45]: Right.

**Blaise Aguera Y Arcas** [21:45]: Language is, I think, in many ways very, very tied up with the formation of anonymous identity.

**Interviewer** [21:50]: Yes.

**Blaise Aguera Y Arcas** [21:51]: Like, the moment we have a common language, then, you know, we say... And in fact, many languages, like the, our, our na- the, the name for the language is the same as the name of the people who speak the language.

**Interviewer** [21:59]: Right.

**Blaise Aguera Y Arcas** [21:59]: When you say French, you know, it's like-

**Interviewer** [22:01]: Yes

**Blaise Aguera Y Arcas** [22:01]: ... French are people, French is a language.

**Interviewer** [22:03]: That's right.

**Blaise Aguera Y Arcas** [22:03]: And they become a people because they have a common language, uh, in a way. Uh, and that, and that common language allows them all to, uh, think collectively and to develop as a, a, you know, to, and, and to have an intelligence that is greater than, than, than individual-

**Interviewer** [22:17]: Right. Yeah

**Blaise Aguera Y Arcas** [22:17]: ... French people, right? Because of their shared language. Uh, and we of course have many, many, uh, collective or anonymous identities beyond the languages that we speak. You know, there are every, every hashtag, you know, becomes almost, uh, you know, a-

**Interviewer** [22:28]: Yeah

**Blaise Aguera Y Arcas** [22:28]: ... a potential source of identity.

**Interviewer** [22:30]: Right.

**Blaise Aguera Y Arcas** [22:30]: But that is the thing that distinguishes us from, say, chimpanzees or bonobos, right? They, they only work cooperatively at the scale of their individual relations or their troop-

**Interviewer** [22:41]: Yes

**Blaise Aguera Y Arcas** [22:41]: ... uh, which, which is very limited in size, right? The way we're able to-

**Interviewer** [22:45]: Yeah

**Blaise Aguera Y Arcas** [22:45]: ... operate collectively at, at these much larger scales is because of, of, of language, and therefore because of anonymous identity.

**Interviewer** [22:50]: I know you, you mentioned Dunbar-

**Blaise Aguera Y Arcas** [22:53]: Yeah

**Interviewer** [22:53]: ... in your book. W- was it very, pretty early? Is that correct?

**Blaise Aguera Y Arcas** [22:56]: Yeah.

**Interviewer** [22:57]: Yeah, yeah. Dunbar i- is, is fascinating. Um, one of my... I mean, I read him a long time ago, but he was dealing with how, uh, almost what you're saying in terms of how, um... He was call- he called it the grooming theory.

**Blaise Aguera Y Arcas** [23:11]: Yes.

**Interviewer** [23:12]: Right. [laughs] And I always loved that theory. I always used to, you know, used to, I teach and I'd always-

**Blaise Aguera Y Arcas** [23:16]: Right. The picking, picking lice is the origins of, uh-

**Interviewer** [23:18]: [laughs] Of our-

**Blaise Aguera Y Arcas** [23:19]: ... of our, of our human genius.

**Interviewer** [23:20]: Yes.

**Blaise Aguera Y Arcas** [23:20]: Yeah.

**Interviewer** [23:20]: And also gossip.

**Blaise Aguera Y Arcas** [23:22]: Yes.

**Interviewer** [23:22]: Right? Yeah, yeah. But it's, yeah-

**Blaise Aguera Y Arcas** [23:24]: I completely buy it, by the way.

**Interviewer** [23:25]: Yeah, yeah. So did I. No, no, I did. And it was one of those embarrassing things where it's like, oh, my God. So when someone like Trump, right, is talking to his, what, what, what, what, um, what media does is allow Trump to groom, right, [laughs] at a scale, [laughs] right? Because, 'cause grooming is a way to, to, to, to, to form bonds.

**Blaise Aguera Y Arcas** [23:45]: Absolutely.

**Interviewer** [23:46]: Right?

**Blaise Aguera Y Arcas** [23:46]: I can see a, I can see a great political cartoon here, by the way.

**Interviewer** [23:48]: [laughs]

**Blaise Aguera Y Arcas** [23:48]: But yes.

**Interviewer** [23:50]: Right. [laughs] That's Robin... Is it Robin Dunbar?

**Blaise Aguera Y Arcas** [23:53]: Yeah.

**Interviewer** [23:53]: Yeah, right. And then that, that was only his full name, but that's what he did. And then, and he, but he was, it was a, it was a great imaginative leap.

**Blaise Aguera Y Arcas** [23:59]: Yes.

**Interviewer** [24:00]: And so when you mentioned Dunbar, I was like, oh, I s- have to go back to Dunbar. There's a lot of good stuff. 'Cause if I remember the grooming theory, right, as to like where when we, when lang- when, when we started using, dealing... 'Cause you do go into this, when we started dealing with large groups, how do you, how do you organize them? How do they have, right?

**Blaise Aguera Y Arcas** [24:17]: Yeah.

**Interviewer** [24:17]: How do they identify, right, impersonally, right?

**Blaise Aguera Y Arcas** [24:20]: Exactly.

**Interviewer** [24:21]: With, with the thing. And, and, and, and Dunbar actually did point to, to this kind of large scale grooming, right? And we do get groomed in all of our political situations. It doesn't stop. We want to, right, feel close.

**Blaise Aguera Y Arcas** [24:35]: Yes.

**Interviewer** [24:35]: And, right, and have our-[sighs] ... metaphorical or, you know, you know what I mean?

**Blaise Aguera Y Arcas** [24:40]: Yeah.

**Interviewer** [24:40]: Yeah, yeah. Uh-

**Blaise Aguera Y Arcas** [24:41]: Well, and, and the, the thing that we've got beyond, uh, you know, chimpanzee troops grooming each other is that-

**Interviewer** [24:46]: Yeah

**Blaise Aguera Y Arcas** [24:46]: ... is, uh, n- not just gossip, but in general, uh, norms and, um, third-party punishment.

**Interviewer** [24:52]: Yes.

**Blaise Aguera Y Arcas** [24:52]: And, and the idea is that, that, um, you know, I can immediately feel ... So I, I mean, I talk a little bit about, for instance, you know, if we walk into a bar like this one, and there are a bunch of other people there-

**Interviewer** [25:01]: Oh, cheers. Bar. [laughs]

**Blaise Aguera Y Arcas** [25:02]: Um, yes. Cheers.

**Interviewer** [25:03]: Cheers. [laughs]

**Blaise Aguera Y Arcas** [25:05]: [laughs] Um ...

**Interviewer** [25:07]: Mm.

**Blaise Aguera Y Arcas** [25:07]: If you are a, a monkey-

**Interviewer** [25:09]: Mm

**Blaise Aguera Y Arcas** [25:09]: ... or a chimp walking into a bar of, full of monkeys you don't know or chimpanzees you don't know, you're going to freak out because the dominance hierarchies have not been established.

**Interviewer** [25:17]: Mm.

**Blaise Aguera Y Arcas** [25:17]: You don't know, you know, like, it, this is a very dangerous situation.

**Interviewer** [25:20]: Mm-hmm.

**Blaise Aguera Y Arcas** [25:21]: Uh, the fact that we, you know, can get on a plane with hundreds of people we don't know and, and everybody lands-

**Interviewer** [25:27]: Yes

**Blaise Aguera Y Arcas** [25:27]: ... and nobody has, you know, torn the limbs off of anybody else-

**Interviewer** [25:29]: That's-

**Blaise Aguera Y Arcas** [25:30]: ... is, is astonishing.

**Interviewer** [25:31]: Yes.

**Blaise Aguera Y Arcas** [25:31]: And, and this, and this is all be- in my opinion, because of anonymous identity.

**Interviewer** [25:34]: Yes.

**Blaise Aguera Y Arcas** [25:34]: Because there are just a bunch of shared norms that we can assume without having any of those personal relationships.

**Interviewer** [25:40]: By the way, that's Sarah Hrdy.

**Blaise Aguera Y Arcas** [25:41]: Yes.

**Interviewer** [25:42]: Mothers and Others.

**Blaise Aguera Y Arcas** [25:43]: Yes. So love her, right.

**Interviewer** [25:44]: Yeah, yeah. Um, apes on a plane. [laughs]

**Blaise Aguera Y Arcas** [25:47]: Exactly.

**Interviewer** [25:47]: Is what it ... It's a great description 'cause she's trying to show the difference as to how you sit in a plane, or a human can sit in a plane for hours without chopping-

**Blaise Aguera Y Arcas** [25:56]: Without killing anybody or being killed

**Interviewer** [25:57]: ... yeah. [laughs]

**Blaise Aguera Y Arcas** [25:58]: Yes.

**Interviewer** [25:58]: Mostly, right?

**Blaise Aguera Y Arcas** [25:59]: Yes.

**Interviewer** [25:59]: Ex- during the pandemic era, there was a flurry of, of this kind of chimpanzee activity on flights.

**Blaise Aguera Y Arcas** [26:06]: You know, a little bit, but it's amazing how little that happens.

**Interviewer** [26:09]: That little, yes.

**Blaise Aguera Y Arcas** [26:09]: Uh, or given how many guns there are in the US, you know, like, uh, that, that, that, that we aren't killing each other constantly is actually astonishing, and it's down to the same thing, I think.

**Interviewer** [26:17]: Oh, do we ... We might have to edit that out. [laughs]

**Blaise Aguera Y Arcas** [26:21]: [laughs]

**Interviewer** [26:21]: We're gonna keep it. [laughs] Um, but I, uh, I, I, uh, I, I wanted to go into, um ... Now if you're focusing on, on, on, on, on this, on the language and the social aspect of AI, um, and probably that's an important direction, probably the, probably the most, in my, in my, in my thinking, uh, direction it could take, what do you think the consequences will be? I mean, what will it do with so much power, right? If our power is literally in our social behavior, right, and we impart this to a machine, right, and what does that, what does that entail? I mean ...

**Blaise Aguera Y Arcas** [27:04]: Well, it is not an other. This is the-

**Interviewer** [27:06]: Oh my gosh.

**Blaise Aguera Y Arcas** [27:08]: This is the ... [laughs]

**Interviewer** [27:08]: You're saying this is-

**Blaise Aguera Y Arcas** [27:10]: It's us

**Interviewer** [27:10]: ... no, this is, this is ... It's us.

**Blaise Aguera Y Arcas** [27:12]: It's us.

**Interviewer** [27:13]: This is where I, okay, I learn something-

**Blaise Aguera Y Arcas** [27:15]: [laughs]

**Interviewer** [27:15]: ... but I, I also know I have to go back and think about that. But yes, it's us.

**Blaise Aguera Y Arcas** [27:19]: It's us.

**Interviewer** [27:19]: This is, this is, this is, this is you. This is you, right? This is your point of view.

**Blaise Aguera Y Arcas** [27:24]: It's my point of view.

**Interviewer** [27:25]: It is as asked.

**Blaise Aguera Y Arcas** [27:25]: And, and I know that's not a point of view that many people have.

**Interviewer** [27:28]: Right.

**Blaise Aguera Y Arcas** [27:28]: But, you know, when we say things like, "Well, is it gonna dominate us or are we going to dominate it?" we're still thinking like chimpanzees, as if this is all a dominance hierarchy.

**Interviewer** [27:36]: Right.

**Blaise Aguera Y Arcas** [27:37]: It's not a dominance hierarchy. The way that we have managed to become, uh, social, anon- anonymously social, you know, and, and build these incredible structures, these, these, these incredible, uh, social structures and technologies that we have, is through cooperation, uh, and, and through collectivity. So, you know, I, I think a lot about Peter Kropotkin's version of Darwin's theories-

**Interviewer** [27:57]: Mm-hmm. Right, right

**Blaise Aguera Y Arcas** [27:58]: ... Mutual Aid.

**Interviewer** [27:58]: Yes.

**Blaise Aguera Y Arcas** [27:59]: Right? And, um, uh, or this multiple simultaneous discovery business. So yeah, when, when we have, uh, AI systems that are able to, uh, you know, read huge numbers of papers and propose experiments, make connections, and we, you know, we do those experiments and we find, uh, you know, new science this way, you know, who, who was the inventor? You know, who was the discoverer? Well, you know, it's already the case it's entirely collective. I mean, most papers nowadays published in most fields have a bunch of authors.

**Interviewer** [28:26]: Right.

**Blaise Aguera Y Arcas** [28:26]: Right? So we're already in the multi-author phase, if you like, of, um, of, of how this all works.

**Interviewer** [28:32]: But who do we credit when AI writes the paper?

**Blaise Aguera Y Arcas** [28:35]: Uh, we pr- well, I mean, I ... Whether we, whether we name our AIs and add them to the author lists, you know, I s- I, I mean, that would be how I would do it, frankly.

**Interviewer** [28:43]: Yeah.

**Blaise Aguera Y Arcas** [28:44]: Um, but, uh-

**Interviewer** [28:44]: But you called it augmented, an augmented ... I mean, I, I, I prefer augmented intelligence than AI.

**Blaise Aguera Y Arcas** [28:50]: But we augment, we augment each other too, don't we?

**Interviewer** [28:52]: Yes, we do. But I, I was always been, I've always been a little un- unnerved by the artificial of the intelligence.

**Blaise Aguera Y Arcas** [29:01]: Mm-hmm.

**Interviewer** [29:01]: And it, it's interesting to ... 'Cause you just leapt right into, it's-

**Blaise Aguera Y Arcas** [29:04]: Yeah

**Interviewer** [29:04]: ... it is intelligence.

**Blaise Aguera Y Arcas** [29:06]: Yeah. I think it is.

**Interviewer** [29:06]: It, it is us, right?

**Blaise Aguera Y Arcas** [29:08]: Right.

**Interviewer** [29:08]: And I'm-

**Blaise Aguera Y Arcas** [29:09]: Well, when we, when we worry about who is credited-

**Interviewer** [29:11]: Yeah

**Blaise Aguera Y Arcas** [29:11]: ... we are, uh, I mean, we're, we're immediately jumping into a different thing, which is our prestige hierarchies or our dominance hierarchies. Like, because the first question is like, well, well, why do we care? Why is it so important who is credited?

**Interviewer** [29:22]: Right.

**Blaise Aguera Y Arcas** [29:22]: It's important for a couple of reasons. One is that our egos demand prestige.

**Interviewer** [29:27]: Right.

**Blaise Aguera Y Arcas** [29:27]: And the other is that we live under capitalism in which, you know, money matters, and credit and, and money and, and our, our basic economic survival are coupled.

**Interviewer** [29:35]: Right.

**Blaise Aguera Y Arcas** [29:35]: And I think both of these are problems.

**Interviewer** [29:37]: Yeah. But, uh, and also people talk about, sometimes they'll say that, uh, uh, this is a popular criticism. It's in all o- ... You know, it's, this is more on the left in terms of like, um, saying that AI just plagiarizes, and people are suing. S- I think Sarah Silverman is suing on this issue, right?

**Blaise Aguera Y Arcas** [29:55]: Right.

**Interviewer** [29:55]: About, about taking my stuff and not really crediting and so on and so on. And w- w- how do ... Where, where's the boundary in that respect, right?

**Blaise Aguera Y Arcas** [30:03]: It's a good, it's a good question. And, you know, I have to say I, I have different answers, I guess, depending on whether we're leaving all of the structures of credit assignment, economics, and so on in place-

**Interviewer** [30:16]: Yes

**Blaise Aguera Y Arcas** [30:16]: ... as they are today-

**Interviewer** [30:16]: Yeah, yeah, yeah

**Blaise Aguera Y Arcas** [30:16]: ... or changing them. [laughs] Right?

**Interviewer** [30:18]: Yeah, yeah.

**Blaise Aguera Y Arcas** [30:18]: So if we leave them in place, then, you know, these are consequential questions for very practical reasons-

**Interviewer** [30:24]: Yeah, yeah

**Blaise Aguera Y Arcas** [30:24]: ... right, that have to do with people's livelihoods and, and, and so on.

**Interviewer** [30:27]: No, no, I'm almost reminded when I read about that, that criticism about plagiarism-

**Blaise Aguera Y Arcas** [30:31]: Yeah

**Interviewer** [30:31]: ... I, my, my own alarms went off, right?

**Blaise Aguera Y Arcas** [30:34]: Right.

**Interviewer** [30:34]: Because I was like, well, you know, you could say that about hip hop when it started.

**Blaise Aguera Y Arcas** [30:38]: Exactly.

**Interviewer** [30:39]: Right? With sampling back in the 1980s, right?

**Blaise Aguera Y Arcas** [30:42]: Yeah. There were those, there were those famous court cases with the Beastie Boys.

**Interviewer** [30:43]: Court cases and so forth and so on.

**Blaise Aguera Y Arcas** [30:45]: Yeah.

**Interviewer** [30:45]: It was just capitalism was behind.

**Blaise Aguera Y Arcas** [30:46]: That's right.

**Interviewer** [30:47]: Right?

**Blaise Aguera Y Arcas** [30:47]: Exactly.

**Interviewer** [30:48]: And so suddenly you're, what you're doing is you're asserting the right of capitalism.

**Blaise Aguera Y Arcas** [30:52]: Right. So I don't, I don't like the idea of reifying capitalism or-

**Interviewer** [30:55]: Yeah

**Blaise Aguera Y Arcas** [30:55]: ... copyright and saying, "Well, that's correct, so let's make the decision about how to credit stuff."

**Interviewer** [30:59]: Yeah.

**Blaise Aguera Y Arcas** [30:59]: Because I, I feel like that's drawing the line in the wrong place.

**Interviewer** [31:02]: Right.

**Blaise Aguera Y Arcas** [31:02]: Right. Um, but saying that, saying that, uh, you know, um, uh, AI models plagiarize because they learned from human content, well, you know, you might as well say, you know, all art is plagiarism.

**Interviewer** [31:12]: Yes.

**Blaise Aguera Y Arcas** [31:13]: Uh, right, because it all is. I mean, uh, you know, this critique was leveled against Tristram Shandy, you know, because that-

**Interviewer** [31:18]: Yes

**Blaise Aguera Y Arcas** [31:18]: ... has big passages, you know-

**Interviewer** [31:20]: Right

**Blaise Aguera Y Arcas** [31:20]: ... uh, cribbed from Burton's Anatomy of Melancholy. I mean, we can take this back as far as we want.

**Interviewer** [31:24]: Yeah.

**Blaise Aguera Y Arcas** [31:25]: Um, and, and, and of course, the reality of human culture is that it all is built on prior work.

**Interviewer** [31:31]: Yeah, but then capitalism says that there is originality.

**Blaise Aguera Y Arcas** [31:34]: Right. So maybe capitalism is the problem. [laughs]

**Interviewer** [31:36]: Is the problem. But then, but then you have some people on the left saying that, "Right." They're saying that, "No, you're, you're taking our, our, our work." I mean, it, it gets more and more... I mean, those are, those are sociological issues-

**Blaise Aguera Y Arcas** [31:47]: They are

**Interviewer** [31:47]: ... that have to be faced eventually.

**Blaise Aguera Y Arcas** [31:49]: They do. So I'm, I'm very sympathetic to the pragmatic concerns of artists, uh, who are worried about, about their livelihoods, which already are destabilized in many ways-

**Interviewer** [31:59]: Yes

**Blaise Aguera Y Arcas** [31:59]: ... by, um, you know, by digital media and streaming and so on, being destabilized further by AI. I'm very sympathetic to those practical concerns.

**Interviewer** [32:06]: Yeah.

**Blaise Aguera Y Arcas** [32:06]: But, but what I'm, what I'm, um, what I'm less sympathetic to, I guess, is the assumption that all of these ideas about, about credit assignment and copyright are just the way things are. Uh, you know, and, and that, and that, uh, all this other stuff is, is, is moral and that, and that, you know, originality is somehow, uh, you know, real when-

**Interviewer** [32:25]: Yes

**Blaise Aguera Y Arcas** [32:26]: ... when in fact, it's so much more complicated and collective than that.

**Interviewer** [32:29]: And so where do you think this is all gonna go then? This is my, my big question. I mean, no, but seriously.

**Blaise Aguera Y Arcas** [32:35]: I wish, I, I wish I knew. [laughs]

**Interviewer** [32:36]: Yeah, but you're involved. You're in the thick of it, right?

**Blaise Aguera Y Arcas** [32:38]: Yes. But, um, but that doesn't, that doesn't mean that I get to decide where it goes. That's a, that's a complex emergent system.

**Interviewer** [32:44]: L- let's, uh, let's, uh, let's, let's... L- let me then ask what are... w- who, who, who's... what are the i- what are the key ideas about where the direction-

**Blaise Aguera Y Arcas** [32:52]: Yeah

**Interviewer** [32:53]: ... w- w- according to your, to your... I mean, just 'cause you, you... there must be some people who are saying, "Well, I know we talked about accelerationism," and so on and so on.

**Blaise Aguera Y Arcas** [33:00]: Yeah.

**Interviewer** [33:01]: But, um, I mean, I wanted to talk about not, not in the, in the negative sense, but I wanted to, I wanted to sort of say like, okay, let's say we accept AI, and I, and I... I'm not a... I'm not against, um, uh... I was when, when, when, when, um, when they brought out, uh, um, um, gene manipulation, right, and, and, and, uh, recombination, I, I was not as... I mean, I realize that no life has been doing this for years and years and years. You don't understand. This is a, this is a basic part. We were maybe, maybe-

**Blaise Aguera Y Arcas** [33:31]: Even, even farmers have been doing this for-

**Interviewer** [33:33]: For years, yes

**Blaise Aguera Y Arcas** [33:33]: ... centuries, if not millennia.

**Interviewer** [33:34]: Yeah, yeah. Cows never, right, only-

**Blaise Aguera Y Arcas** [33:36]: Never existed

**Interviewer** [33:36]: ... [laughs] never existed-

**Blaise Aguera Y Arcas** [33:38]: Right

**Interviewer** [33:38]: ... until they met human beings who picked the, the cows that they wanted to have.

**Blaise Aguera Y Arcas** [33:42]: Exactly.

**Interviewer** [33:43]: And this is woo- done way before we even knew what genes were.

**Blaise Aguera Y Arcas** [33:47]: Totally.

**Interviewer** [33:47]: And so but-

**Blaise Aguera Y Arcas** [33:48]: Corn, corn in, in-

**Interviewer** [33:48]: Corn, yes

**Blaise Aguera Y Arcas** [33:49]: ... in Central America-

**Interviewer** [33:49]: Yeah, yeah

**Blaise Aguera Y Arcas** [33:50]: ... compare the tail seem to-

**Interviewer** [33:51]: Yeah, [laughs] it was like that, right?

**Blaise Aguera Y Arcas** [33:52]: Exactly.

**Interviewer** [33:52]: And so in fact, they say that the, the, the corn that we have can't even survive without us.

**Blaise Aguera Y Arcas** [33:57]: Yeah.

**Interviewer** [33:57]: They're like... they're ca- they're called, um, helpful monsters, right?

**Blaise Aguera Y Arcas** [34:00]: Exactly.

**Interviewer** [34:00]: They're just like... So I don't believe in this idea that suddenly we, we, we've invented, um, the manipulation of, of nature and also, um, or the corruption of nature and, or no-

**Blaise Aguera Y Arcas** [34:10]: That, that implies that we're separate from nature, which-

**Interviewer** [34:12]: Which is not

**Blaise Aguera Y Arcas** [34:13]: ... I think we're not.

**Interviewer** [34:13]: Yes, yes.

**Blaise Aguera Y Arcas** [34:13]: Right.

**Interviewer** [34:14]: This is-

**Blaise Aguera Y Arcas** [34:14]: And in the same way that I think we're not separate from computers.

**Interviewer** [34:16]: Oh, now I found a connection.

**Blaise Aguera Y Arcas** [34:17]: So I think there's a parallel there.

**Interviewer** [34:17]: I found a connection with you. Yes, I do agree with this, I... that you can't separate AI from nature.

**Blaise Aguera Y Arcas** [34:24]: Exactly. And I think you can't separate... Exactly, exactly. AI, human culture-

**Interviewer** [34:27]: Yeah

**Blaise Aguera Y Arcas** [34:27]: ... and nature are all part of the same-

**Interviewer** [34:28]: Same thing

**Blaise Aguera Y Arcas** [34:29]: ... structure.

**Interviewer** [34:29]: And so we're dealing with this, this kind of, yeah, this notion of like somehow, uh, the, to something, you know, the fallen, the myth of the fallen, right, human, right-

**Blaise Aguera Y Arcas** [34:39]: Exactly

**Interviewer** [34:39]: ... that we, we, we, we've done something. Uh, we've stepped on God's feet or something like that, right? We should have left that alone, but there's nothing in... everything in nature, right? Uh, in niche construction, it's already there about animals, um, changing their environment and the environment changing them.

**Blaise Aguera Y Arcas** [34:57]: Exactly.

**Interviewer** [34:57]: That's a major aspect. Well, it was at least in the, in the, uh, in the, uh, a decade ago, right? I'm not sure how big it is now, but I was really into it, niche construction.

**Blaise Aguera Y Arcas** [35:07]: Yeah.

**Interviewer** [35:07]: And, uh-

**Blaise Aguera Y Arcas** [35:08]: It's still, it's still... I mean, I, I would say that's, that's true, and that's been broadly accepted by now.

**Interviewer** [35:12]: By, yes, right.

**Blaise Aguera Y Arcas** [35:13]: Even, even, even like, uh, animals in urban environments, for instance-

**Interviewer** [35:16]: Yes, right

**Blaise Aguera Y Arcas** [35:16]: ... we see that happening.

**Interviewer** [35:17]: Right, right. They, they, they, yes, they change and we change and so on and so on. So there's this loop-

**Blaise Aguera Y Arcas** [35:21]: Exactly

**Interviewer** [35:21]: ... and so on. Okay. And so, um, I, uh, uh, so we accept-

**Blaise Aguera Y Arcas** [35:27]: So AI, AI is more of the same.

**Interviewer** [35:29]: It's more of the same.

**Blaise Aguera Y Arcas** [35:29]: AI is more of the same.

**Interviewer** [35:30]: So we shouldn't be scared.

**Blaise Aguera Y Arcas** [35:31]: Well, I, I don't think that we should be scared of AI.

**Interviewer** [35:34]: Yes.

**Blaise Aguera Y Arcas** [35:34]: Uh, I do think that, that, that those, that it's a big change-

**Interviewer** [35:37]: Yes

**Blaise Aguera Y Arcas** [35:38]: ... and that it, that it forces us to rethink our political economy.

**Interviewer** [35:42]: Yes.

**Blaise Aguera Y Arcas** [35:42]: So, uh, you know, I, I-

**Interviewer** [35:43]: That's, yeah

**Blaise Aguera Y Arcas** [35:44]: ... and, and these are choices, right? We have, we, we, we have agency about how we organize stuff. I mean, the, the flip side of everything, you know, that, that nature and AI and human culture are part of the same structure is, you know, it's also not like we are helpless or there's no such thing as agency in all of this. The, you know, the, the, the idea that we, we hold capitalism fixed, for instance, uh, is, um, I, I find, you know, weird. Like, why don't we revisit this stuff? You know, in, in, uh, in this era when we actually, for instance, have enough wealth collectively that, you know, everybody can eat, why are we having conversations about, uh, about, about people starving? You know, there is something wrong with that.

**Interviewer** [36:22]: Right.

**Blaise Aguera Y Arcas** [36:22]: Right? And I feel like if we, if we, if we solve, uh, these distribution, uh, challenges, then, um, that takes a lot of the air out of, out of this, out of the, the AI anxieties. Um, I think those anxieties, you know, ha- have a lot to do with rising inequality and with-

**Interviewer** [36:38]: Yes, that's, that's-

**Blaise Aguera Y Arcas** [36:39]: ... and with these other sociological challenges.

**Interviewer** [36:40]: That's actually my... that's where I come from, and my economic background is to say that what has happened is machines have always represented, for those who are working, a force. It's not that, it's not that the... We, we, we, we... I, I think that we watch Hollywood films, and they represent the, the fear of machines, as if machines take on their own life and start making decisions. This is the Blade Runner, and this is, um, Terminator, and so on and so on. But I've always argued that the real fear, right, is that- 'Cause then jobs are lost

**Blaise Aguera Y Arcas** [37:12]: Exactly

**Interviewer** [37:13]: Right, and that's, and-

**Blaise Aguera Y Arcas** [37:14]: And, and, and when we, when we look at, at the horrors that happened in England, you know, during the-

**Interviewer** [37:18]: Yeah, right

**Blaise Aguera Y Arcas** [37:18]: ... the first Industrial Revolution, the, the Luddites, the machine breakers, I mean, my sympathies are entirely with the Luddites and machine breakers.

**Interviewer** [37:24]: Right.

**Blaise Aguera Y Arcas** [37:24]: Right? Given what was happening at that time.

**Interviewer** [37:26]: Yes.

**Blaise Aguera Y Arcas** [37:27]: But does that mean that I'm against, uh, machines that do weaving? Absolutely not, right? Our lives-

**Interviewer** [37:31]: Yes

**Blaise Aguera Y Arcas** [37:31]: ... are all much better with machines that, that, that do weaving. Um, but, y- you know, that, that transition could've been managed much better.

**Interviewer** [37:38]: Yeah, yeah, yeah.

**Blaise Aguera Y Arcas** [37:38]: You know?

**Interviewer** [37:38]: Yeah. Yeah, Don, yeah

**Blaise Aguera Y Arcas** [37:39]: Right. And I feel, I feel we're in a similar situation.

**Interviewer** [37:40]: I, in, in, in, in Cyborg Manife- Ma- Manifesto by Donna Haraway-

**Blaise Aguera Y Arcas** [37:44]: Haraway

**Interviewer** [37:44]: ... I've always loved her, her thing is that, uh, the, the machines can come from a particular birth, right? But it doesn't mean that they're faithful to their birth.

**Blaise Aguera Y Arcas** [37:52]: Not at all.

**Interviewer** [37:53]: [laughs] Right? She wants to remind people, like, just because something starts somewhere doesn't mean it's going to, right, maintain-

**Blaise Aguera Y Arcas** [38:00]: Ab-

**Interviewer** [38:00]: ... right?

**Blaise Aguera Y Arcas** [38:00]: No more than the fact that our fingernails were originally weapons-

**Interviewer** [38:03]: Yes

**Blaise Aguera Y Arcas** [38:03]: ... means that that's what they are now.

**Interviewer** [38:04]: Right. Yeah, yeah.

**Blaise Aguera Y Arcas** [38:04]: Right.

**Interviewer** [38:04]: That things can... That it's, it's, it's the introduction of it in the world that is the terrifying thing, for not just, uh, but just for everybody, 'cause they don't quite know where it's gonna go-

**Blaise Aguera Y Arcas** [38:17]: Yeah

**Interviewer** [38:17]: ... and who's g- how it's going to change society, right? How it... You know what I mean? And, uh, and the, the issue would be then, well, um, the potential of AI could fall... You know what I mean? In, in... Would, would be more of a, a power issue, right?

**Blaise Aguera Y Arcas** [38:32]: That's right.

**Interviewer** [38:33]: Rather than the, a technological issue.

**Blaise Aguera Y Arcas** [38:35]: That's right. And, and thinking about power in hierarchy or dominance terms feels to me like a part of the problem-

**Interviewer** [38:40]: Yeah

**Blaise Aguera Y Arcas** [38:40]: ... as well. So, uh, you know, I, I, I, um, I, I very much like and respect a, a thinker about AI ethics who has wor- who's been working in this field for a long time, Joanna Bryson.

**Interviewer** [38:49]: Mm-hmm.

**Blaise Aguera Y Arcas** [38:50]: But she wrote a paper that, uh, y- I think she also regrets the title of nowadays, but it was back in 2010. And what she wrote was, "Robots Should Be Our Slaves."

**Interviewer** [38:58]: Oh.

**Blaise Aguera Y Arcas** [39:00]: Problematic title in a bunch of ways.

**Interviewer** [39:01]: Yeah, yes.

**Blaise Aguera Y Arcas** [39:01]: But it was kind of on the nose. You know, that, that, oh, we have, we have these things that can do labor. Uh, the only appropriate way to deal with this situation is to, uh, is to assume, uh, to, to reconstitute, if you like, the conditions of slavery, where now the machines are slaves. And this is a, I think this is a very crude, uh, analysis, right? And, and, and, and if we're still having that debate, uh, you know, we're, we're not understanding the foundations of sociality, uh, that, which are all about symbiosis.

**Interviewer** [39:30]: Yeah.

**Blaise Aguera Y Arcas** [39:30]: Right? And, and all about mutual constitutiveness, if you like.

**Interviewer** [39:33]: Yeah, no, I saw this in the movie Origin recently. I always watch science fiction films to see where they're, where they're, where they're taking the, the notion of AI, and they resort it to this robots are AI [clears throat] or slaves.

**Blaise Aguera Y Arcas** [39:48]: Right.

**Interviewer** [39:49]: Right?

**Blaise Aguera Y Arcas** [39:49]: Well, and West- Westworld would be a more-

**Interviewer** [39:50]: Well, then maybe-

**Blaise Aguera Y Arcas** [39:51]: ... maybe a more popular version of the same

**Interviewer** [39:52]: ... that's more popular, yeah, the same, right.

**Blaise Aguera Y Arcas** [39:54]: Exactly.

**Interviewer** [39:54]: Right. And then they, they, they go through the stages, the, the classical stages of, right, of a, of a, of reaction, of, of revolution, right? Of resistance, right? And so that's the... And, and, and it's a bit tired to say, like, "Well, that's very limited," and also it may not be anywhere close to the truth-

**Blaise Aguera Y Arcas** [40:15]: Right

**Interviewer** [40:15]: ... because, uh-

**Blaise Aguera Y Arcas** [40:16]: It's, it's way too reductive.

**Interviewer** [40:17]: Yeah, yeah.

**Blaise Aguera Y Arcas** [40:17]: But, but also, insofar as we think about bad guys, well, the bad guys are the people who are insisting on a dominance hierarchy in this situation.

**Interviewer** [40:24]: Yeah.

**Blaise Aguera Y Arcas** [40:24]: Right? The, the existence of, of, you know, of, of more kinds of intelligences is not the problem.

**Interviewer** [40:30]: Yeah.

**Blaise Aguera Y Arcas** [40:30]: The, the problem is, the problem is, uh, um, a reduction of the relations of those intelligences to some kind of chain of being.

**Interviewer** [40:37]: Is there really a difference between a hammer and artificial intelli- intelligence?

**Blaise Aguera Y Arcas** [40:44]: Yes, I think there is.

**Interviewer** [40:46]: Okay. I wanna ask why.

**Blaise Aguera Y Arcas** [40:48]: Well, um, in that moment when we changed, and this, this is a technical argument-

**Interviewer** [40:53]: Yes

**Blaise Aguera Y Arcas** [40:53]: ... but in the moment when we changed from, from, uh, supervised to unsupervised learning.

**Interviewer** [40:57]: Yes?

**Blaise Aguera Y Arcas** [40:58]: Uh, right, so supervised learning is more like a hammer in the sense that, that it, it can't do anything other than, you know, score such and such-

**Interviewer** [41:06]: Right

**Blaise Aguera Y Arcas** [41:06]: ... uh, you know, percent, like, you know, be X good-

**Interviewer** [41:09]: Yes

**Blaise Aguera Y Arcas** [41:09]: ... right, at the task for which it was designed.

**Interviewer** [41:10]: Right.

**Blaise Aguera Y Arcas** [41:10]: That's it. Um, modern AI, which uses autoregressive unsupervised learning, um, you know, has this really cool property of, of so-called in-context learning or few-shot learning. So for instance, I can, I can say to a, um, you know, a, a Bard or a ChatGPT-type model, "An equi antonym is a word with the same number of letters as another word, but that means it's opposite. Give me some examples." And it'll do that. And a hammer can't do that, right? A hammer can't learn, uh, you know, or, or just be, you know, be asked to do something that it, that, that it has never done before and, and, and do it, right? And, and come back and pose me problems as well, right? Uh, you know, so, so at that point we're no longer dealing with, with a, um, a-

**Interviewer** [41:51]: A tool

**Blaise Aguera Y Arcas** [41:52]: ... just an algorithm or a tool. I think there is something more there.

**Interviewer** [41:54]: So there's a difference between a tool and a machine.

**Blaise Aguera Y Arcas** [41:57]: Yes. Uh, or I would say that an intelligence is, uh, is, is something, uh, beyond, uh, just a function that, that-

**Interviewer** [42:06]: Plays?

**Blaise Aguera Y Arcas** [42:07]: ... that can, that can be approximated.

**Interviewer** [42:08]: This is, this is difficult for me. Right? Okay, no, no, I, I wanted to say this because, yes, yeah, I understand, but it means that intelligence becomes special, right, if it's not a tool.

**Blaise Aguera Y Arcas** [42:20]: Yes.

**Interviewer** [42:21]: If AI is not in- a tool, then it's doing something different, right?

**Blaise Aguera Y Arcas** [42:24]: Well, how can, how can... What does it mean for something to have a tool or to use a tool? What's the difference between the tool and the user?

**Interviewer** [42:30]: Uh, well, you know, the classic idea is that the tool actually becomes a part of the body.

**Blaise Aguera Y Arcas** [42:35]: Yes.

**Interviewer** [42:36]: Right? And that there's this, uh... Right? There's, uh, the, the, there's, the, the mind actually brings it into the body, uh, uh, is-

**Blaise Aguera Y Arcas** [42:43]: Which is true, right? The cane becomes an extension of the arm.

**Interviewer** [42:46]: Of, of the arm, right?

**Blaise Aguera Y Arcas** [42:47]: But isn't, but isn't there an eye on the other end of that?

**Interviewer** [42:49]: Yes. Right?

**Blaise Aguera Y Arcas** [42:50]: What is that, what is that eye and what does it mean?

**Interviewer** [42:52]: That is, that is crazy.

**Blaise Aguera Y Arcas** [42:55]: So Charles, what is an agent? What's an I?

**Interviewer** [42:57]: Uh, no, you gotta... No, no, no, no, no, no, no.

**Blaise Aguera Y Arcas** [43:00]: [laughs]

**Interviewer** [43:00]: Yeah, yeah, yeah, yeah. I, uh, I, I, I, I, I'm not... Ah, gosh, I always have difficulty, um, um, with those questions and you, you know, I'm almost like, "Oh, my God, I wish I had time to, to think about that." But I, uh... What would you say? That's what I'd say.

**Blaise Aguera Y Arcas** [43:17]: Well, I, I, so I think that agency- Uh, which is to say the ability to act rather than just to be acted upon-

**Interviewer** [43:26]: Right

**Blaise Aguera Y Arcas** [43:26]: ... is a real thing.

**Interviewer** [43:27]: Yes.

**Blaise Aguera Y Arcas** [43:28]: Um, you know, when, uh, when we last talked actually, I, I, I recommended a book by Kevin Mitchell called Free Agents-

**Interviewer** [43:34]: Oh, okay

**Blaise Aguera Y Arcas** [43:34]: ... that I think is, is pretty smart in describing, you know, what, uh, you know, how, what, what that means. But, but in my view, what that means is that, um, that you have, uh, you have active inference going on in which, uh, the, uh, in which it means some- uh, how, how can I, how can I put this comp- I, see, I have, I have trouble too.

**Interviewer** [43:54]: Yeah, yeah. [laughs]

**Blaise Aguera Y Arcas** [43:54]: But, um, but to act rather than to react means that, um, that new meaning, right? New choices, um, uh, new intentions can originate from some locus of concern.

**Interviewer** [44:10]: Mm-hmm.

**Blaise Aguera Y Arcas** [44:11]: And, um, that can't happen from a hammer. A hammer doesn't have ideas-

**Interviewer** [44:15]: Oh, I see

**Blaise Aguera Y Arcas** [44:15]: ... right? It doesn't have-

**Interviewer** [44:17]: That's where you're going.

**Blaise Aguera Y Arcas** [44:18]: Yeah.

**Interviewer** [44:18]: Okay, that, yeah, now, now we, now we brought it back that, to that. Okay. Right? Okay. That's it. But it still brings this other issue to me then, and I think we can just close it on, on this, and, um, um, if we're, if we're talking about it on, on that level, uh, I mean, it's kind of, I am a little not, not, not, not disturbed, but I'm, I'm sort of like, uh, in a, in a zone that is where I'm like I, I can't really see what's coming ahead because I don't understand if this is not a tool, forgive me, right?

**Blaise Aguera Y Arcas** [44:56]: Then what is it?

**Interviewer** [44:56]: Then what is it, right?

**Blaise Aguera Y Arcas** [44:59]: Yeah.

**Interviewer** [44:59]: And, and why is it, and why is something that's related to the mind, to, to intelligence, right? Uh, you know what I mean? I mean, right now, they, they're doing work across the street, right? And they have those machines, right? The, the, the, the bulldozers and right? The, the shoveling and all this is going on, right? And I know those are tools, right? And I know that there's a mind in the machine, right?

**Blaise Aguera Y Arcas** [45:21]: Kind of.

**Interviewer** [45:22]: Kind of.

**Blaise Aguera Y Arcas** [45:23]: But the machine isn't, isn't modeling you back. Uh, the machine isn't initiating any actions.

**Interviewer** [45:27]: That's right.

**Blaise Aguera Y Arcas** [45:28]: Um.

**Interviewer** [45:28]: That's exactly the ... yes, that's it. Right. I agree, accept this. And so what is it about the mind as a, as a, as, as, as something you would say that augments the mind-

**Blaise Aguera Y Arcas** [45:39]: Yeah

**Interviewer** [45:39]: ... that is, say, something that augments the hand, right? Like a spoon or a, right, a cane. What is it about the augmentation of the mind that is ... That's, that's to me the troubling ... Oh, no, no, not troubling, but a, oh, I, I don't under- you know, where I'm still in the, in the flux, like I don't have an answer for that.

**Blaise Aguera Y Arcas** [45:59]: That, I think that that is the big Copernican shift of our time.

**Interviewer** [46:02]: Oh, goodness.

**Blaise Aguera Y Arcas** [46:03]: And, uh-

**Interviewer** [46:03]: That is-

**Blaise Aguera Y Arcas** [46:04]: [laughs] You know? Like it's-

**Interviewer** [46:05]: That is ... You can't say it any louder than that, right?

**Blaise Aguera Y Arcas** [46:07]: Yeah. Um-

**Interviewer** [46:08]: Yeah

**Blaise Aguera Y Arcas** [46:08]: ... you know, and, and what we haven't had before-

**Interviewer** [46:11]: Yeah

**Blaise Aguera Y Arcas** [46:11]: ... right, is, is, um, machines that can model us. You know? A machine that you can have a conversation with. Uh, you can't have a conversation with something-

**Interviewer** [46:19]: Oh

**Blaise Aguera Y Arcas** [46:19]: ... right, that isn't, that isn't-

**Interviewer** [46:20]: Right

**Blaise Aguera Y Arcas** [46:20]: ... forming models of you-

**Interviewer** [46:22]: Right

**Blaise Aguera Y Arcas** [46:22]: ... is not able to initiate, right?

**Interviewer** [46:24]: Ah.

**Blaise Aguera Y Arcas** [46:24]: And, and that is new. That's, that's what, that's what AI really is.

**Interviewer** [46:27]: But we can still go back to niche construction-

**Blaise Aguera Y Arcas** [46:29]: Yes

**Interviewer** [46:29]: ... in this respect, right? So we do, we can say to a degree the tool may actually change us.

**Blaise Aguera Y Arcas** [46:35]: Yes.

**Interviewer** [46:36]: Not to the extent, right, that's so direct, right? Because the tool will make our hands maybe lazier, right? May, may, may-

**Blaise Aguera Y Arcas** [46:44]: Well, there's the dystopian Wall-E version of this-

**Interviewer** [46:46]: Yes, right

**Blaise Aguera Y Arcas** [46:47]: ... which I hope, I hope is not where we go.

**Interviewer** [46:48]: Oh, I love Wall-E, by the way.

**Blaise Aguera Y Arcas** [46:49]: It's a wonderful movie.

**Interviewer** [46:50]: My favorite, my favorite. I wish we could go through movies-

**Blaise Aguera Y Arcas** [46:53]: [laughs]

**Interviewer** [46:53]: ... but I think we, we've had a long conversation. And as I said, um, um, the, the transcript of our first conversation will be available on The Stranger. I, I really wanna thank you. I know we could go on quite a while on this, and always a pleasure to talk to you about ideas. And it's always, um, I'm always impressed that somebody out there in the world of technology takes, um, um, human sociality, right? And the sociality of ants, the sociality of termites, um, groups, seriously. Right? And, uh, and things like that. So I, I cannot, uh, I cannot, uh, I cannot praise, uh, the, your work, right, um, um, more highly. Just really wonderful and get his book.

**Blaise Aguera Y Arcas** [47:44]: [laughs]

**Interviewer** [47:45]: And I'll, I'll, I'll be writing about his book, um, in two weeks or so after this is broadcast. So yes.

**Blaise Aguera Y Arcas** [47:52]: That is incredibly kind and generous. Thank you, Charles.

**Interviewer** [47:55]: Yes.

**Blaise Aguera Y Arcas** [47:55]: It's been, it's, it's such a joy to have these conversations. Um, I, I, I feel the same. [laughs]

**Interviewer** [48:00]: All right. Let's have a ... I think we still got some more wine here.

**Blaise Aguera Y Arcas** [48:04]: All right.

**Interviewer** [48:05]: Yes. [laughs]

**Blaise Aguera Y Arcas** [48:05]: We have to have a final, a final drink before the bar actually opens.

**Interviewer** [48:07]: Opens.

**Blaise Aguera Y Arcas** [48:08]: [laughs]

**Interviewer** [48:08]: Oh, don't tell anybody that ... Oh, it's white.

**Blaise Aguera Y Arcas** [48:11]: Now you have Rosé.

**Interviewer** [48:11]: White is not a so visual. [laughs] Sorry.

**Blaise Aguera Y Arcas** [48:14]: There's still, there's still some, some tint in it.

**Interviewer** [48:16]: Yes. That's right. And come to The Hideout.

**Blaise Aguera Y Arcas** [48:19]: And-

**Interviewer** [48:19]: By the way, everybody, The Hideout is a great joint

**Blaise Aguera Y Arcas** [48:21]: To The Hideout.

**Interviewer** [48:22]: Yes.

**Blaise Aguera Y Arcas** [48:23]: And to collective intelligence.

**Interviewer** [48:24]: Yes. There we are

