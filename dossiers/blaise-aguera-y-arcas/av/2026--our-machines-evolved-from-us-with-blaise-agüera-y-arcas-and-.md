---
title: "Our Machines Evolved From Us (with Blaise Agüera y Arcas and Carlo Rovelli)"
person: blaise-aguera-y-arcas
section: by
type: talk-transcript
year: 2026
venue: ""
source_url: https://youtu.be/tDccIoz-SFI
retrieved: 2026-08-15
content: full-text
transcription:
  method: asr
  asr_model: elevenlabs-scribe_v2
  diarized: true
  speaker_labels: inferred   # ASR diarization + LLM naming (claude-sonnet-4-6); not ground truth
  duration_min: 83
notes: "PROVENANCE: machine-transcribed from AV via ElevenLabs Scribe v2 (diarized) + LLM speaker-naming pass. Speaker labels are inferred, not authoritative. Layer-2 (mildly lossy) per charter, not camera-raw."
---

# Our Machines Evolved From Us (with Blaise Agüera y Arcas and Carlo Rovelli)

*Speakers (inferred):* speaker_0=Dawn Nakagawa, speaker_1=Grant Slater, speaker_2=Carlo Rovelli, speaker_3=Blaise Aguera Y Arcas

## Transcript
**Dawn Nakagawa** [00:00]: Hi, and welcome to Futurology. I'm your host, Dawn Nakagawa, and I am here with our senior producer, Grant Slater.

**Grant Slater** [00:07]: Hello, Dawn.

**Dawn Nakagawa** [00:08]: Hey, Grant. How you doing?

**Grant Slater** [00:09]: Really good. Happy to be here with you.

**Dawn Nakagawa** [00:11]: Good. Uh, in this episode, we, uh, have Carlo Rovelli, the theoretical physicist, speaking to Blaise Aguera y Arcas, um, a vice president of engineering from Google.

**Grant Slater** [00:24]: Yeah, the indefinite article is doing a lot there, a vice president, 'cause there's a lot of them.

**Dawn Nakagawa** [00:29]: Uh, so Blaise is actu- and you'd never guess from the title, but he is actually a philosopher of technology, and he spends most of his time, um, studying the really, the most fundamental, uh, philosophical questions of what is life, what is the nature of reality, what is consciousness.

**Grant Slater** [00:45]: Yeah, um, not something a lot of people get paid to do, so seems like a pretty sweet gig.

**Dawn Nakagawa** [00:50]: Yeah, I'd take it. [laughs]

**Grant Slater** [00:51]: [laughs]

**Dawn Nakagawa** [00:52]: Carlo Rovelli himself is also a great thinker who has his own theory of consciousness that relates to, um, Blaise's quite well. But he's also a really good friend of the Berggruen Institute. So Carlo's been, um, helpful in different projects that the Berggruen Institute has done on artificial intelligence, uh, and he's a member of the Berggruen Prize jury.

**Grant Slater** [01:13]: Yeah, and I think that, I think that this is the reason that Carlo and Blaise wanted to talk to each other. But they do share one commonality, which is this idea of relationality, both for theoretical quantum physics and for consciousness and computation, and found some common ground that are really excavated in this conversation, which is not the easiest conversation we've ever put on the podcast.

**Dawn Nakagawa** [01:34]: No, it's su- certainly dense.

**Grant Slater** [01:36]: Yeah, so there are some key terms that come up in this conversation that I think it would be helpful to define here at the beginning. One of those terms is computational life. That means that not just that we compute things in our brains, but that everything is computing everything all the time, that when we look at tables, chairs, black holes, uh, you know, squirrels, they're all just kind of running through computational processes both at the cognitive level and at the physical level.

**Dawn Nakagawa** [02:02]: Throughout history, we've had various theories of what life is, um, and I think for a long time there's this hubris around, you know, biological life is the only form of life, and that is truly what life is, that it's somehow, like, carbon-based and it's something special that happens on this planet and it's divine and all of these things. Those theories have evolved a lot from, like, information theories of life to complexity theories of life and, I mean, he takes it to an extreme.

**Grant Slater** [02:28]: It made me a little uncomfortable when I first started to engage with i- his ideas because, uh, it's really more like technology is the same thing as life and that these two are dependent on each other and maybe there's less of a distinction between, you know, meat space and information space.

**Dawn Nakagawa** [02:44]: Yes, and that, like, the entire thing is based on some sort of code, right? And so he uses the example of DNA as these, you know, basically these four different elements that combine and recombine in all kinds of different ways, which is essentially a code.

**Grant Slater** [03:00]: Yeah. Um, and so there's a little bit of a heady experiment that he talks about in this, uh, interview with a pretty interesting name. It's called the brain fuck experiment. Um, and this, uh, experiment is the most simple version of code you can create that replicates itself. It's like a programming language, and what it does is it finds other parts of itself and makes a copy, and then it makes a copy of a copy. And so these copies are extremely arbitrary, but as it goes on and on and on, the copies of copies become more complex and they start to find some kind of order totally unbidden of any kind of intention.

**Dawn Nakagawa** [03:36]: He seems to be collapsing the idea that there's chance involved. It's actually an inevitability of symbiogenesis regardless of the substrate, right? It all behaves this way.

**Grant Slater** [03:46]: Another way to describe that is kind of like a Turing tar pit, like this idea that there's this, like, soup of information that combines in unexpected ways, and the word that he uses for this is symbiogenesis, this idea that things can only evolve in so much as they relate to each other. Uh, originally it was this, this term comes to us from Lynn Margulis, who really applied it only to biological systems. So, you know, mitochondria existed outside of cells, but then they achieve a symbiotic relationship which then led to eukaryotic cells, which is the basis of all life. And so Blaise's argument th- is that that doesn't stop at the cell walls, that that actually extends beyond that because all life uses technology.

**Dawn Nakagawa** [04:27]: I do believe that our relationship with technology has-- it stopped being subject-object a long time ago, right?

**Grant Slater** [04:35]: Yeah.

**Dawn Nakagawa** [04:35]: Because we are co-evolving with the technology that allows us to do, um, so many things today, and that without which we would really be incapacitated.

**Grant Slater** [04:45]: Bits can have real impact in the world, so you can see that right now with information and how it is roiling humanity and causes people to take actions that they wouldn't otherwise. And I think you're right that this line between biological and computational is blurring.

**Dawn Nakagawa** [05:01]: Yeah. Okay, with that, let's go to the episode with Blaise and Carlo on Futurology.

**Carlo Rovelli** [05:12]: Blaise Aguera y Arcas, I'm very happy of this conversation with you.

**Blaise Aguera Y Arcas** [05:17]: Me too, Carlo.

**Carlo Rovelli** [05:18]: Um, let me start by saying, uh, to whoever is listening to us that, uh, uh, Blaise is, um, i- in, in Italian we say in a punta di diamante, I guess in a, in a, a diamond point. As in English you said a, a, a spearhead, um, of the recent, uh, uh, technological evolution in, uh, artificial intelligence. Now, uh, Blaise works Google. When he moved about a decade ago from, uh, uh, Google-- uh, from Microsoft to Google, that was news. It went in The New York Times. Uh, uh, there was, um, uh, there were articles saying top Microsoft genius defects to Google. [laughs]

**Blaise Aguera Y Arcas** [06:01]: It's journalism, I mean-

**Carlo Rovelli** [06:03]: Yeah

**Blaise Aguera Y Arcas** [06:03]: ... very selfish

**Carlo Rovelli** [06:04]: But you, you, you are on the record for saying it was not an easy decision. It was a difficult decision of, uh, uh, y- uh, your life. But the reason of this conversation and also my interest, uh, um, is not so much that Blaise is a genius in, in, in, in, in coding and developing technology, is, uh, your, uh, much wider angle and your interest in, in general questions. Uh, uh, I would say that Blaise is a true thinker ca- capable of finding new, uh, ways of addressing, uh, old conceptual problem, opening new way of thinking, and, uh, is one of very few people that, uh, does that. I-

**Blaise Aguera Y Arcas** [06:48]: That's, that's really, that's really a lovely compliment, especially from you, Carlo. Thank you.

**Carlo Rovelli** [06:53]: Well, we've spent, we've spent, uh... I mean, in this-- we are here in Venice for s- so con- con- con- conference on consciousness. Um, but we were together for about a week, and, uh, we've been, um, having conversation during this-- various conversation during this week. And, uh, um, definitely something in this conversation has changed my, my-- some aspect of my worldview, which of course-

**Blaise Aguera Y Arcas** [07:17]: That's, that's really, really nice

**Carlo Rovelli** [07:17]: ... is the best thing that can happen when you, uh, when you meet something. So-- somebody. So before plunging in, uh, tell, tell us something a bit more about yourself. You were born in Mexico City, uh, '75. Is that correct?

**Blaise Aguera Y Arcas** [07:34]: Born in '75. Actually, in the US.

**Carlo Rovelli** [07:36]: Oh, born in the US.

**Blaise Aguera Y Arcas** [07:37]: Yes.

**Carlo Rovelli** [07:37]: But you grew up-

**Blaise Aguera Y Arcas** [07:38]: Although-

**Carlo Rovelli** [07:38]: But you were-

**Blaise Aguera Y Arcas** [07:39]: After, after just a few months, my family moved to Mexico City

**Carlo Rovelli** [07:41]: Moved to Mexico City.

**Blaise Aguera Y Arcas** [07:42]: Yes.

**Carlo Rovelli** [07:42]: So and you, you, you spent some time there, and you, you, you were in high school there in Mexico City, so-

**Blaise Aguera Y Arcas** [07:47]: High school in, in the US again. So, so moved back-

**Carlo Rovelli** [07:50]: So back and forth

**Blaise Aguera Y Arcas** [07:50]: Yeah, moved back for, uh-

**Carlo Rovelli** [07:50]: You're really mixed in that-

**Blaise Aguera Y Arcas** [07:52]: For high school

**Carlo Rovelli** [07:52]: ... uh, culture. There are legends about you. One is that at fourteen you rewrote the code of, what is it? Of a Navy ship because, uh, uh, so it would, it would oscillate less and, uh, make a... Is that true, or is that fantasy?

**Blaise Aguera Y Arcas** [08:05]: Yeah, yeah, that is, that is true. Um-

**Carlo Rovelli** [08:06]: What happened?

**Blaise Aguera Y Arcas** [08:07]: It's called the Active Operator Guidance Program.

**Carlo Rovelli** [08:10]: Okay.

**Blaise Aguera Y Arcas** [08:10]: Uh, I didn't, I didn't write it from, from scratch.

**Carlo Rovelli** [08:13]: Of course.

**Blaise Aguera Y Arcas** [08:14]: Um, but, um, but yeah, it was-- So there were, there were these programs at the time. Um, it was, I guess, part of the military industrial complex in the-

**Carlo Rovelli** [08:21]: Yeah

**Blaise Aguera Y Arcas** [08:21]: ... in the US and, and part of the response to the sense that, uh, I mean, I found this out later. Uh, part of a response to the, the sense that the US was falling behind the Soviet Union in technical, uh, education. So they had these programs for young people-

**Carlo Rovelli** [08:33]: Okay

**Blaise Aguera Y Arcas** [08:33]: ... to sort of bring, you know, who are, who are, uh, good at, at, you know, physics, math, computers or whatever to, you know, bring them into the, uh, um-

**Carlo Rovelli** [08:41]: So through the school you got this or, or through some-

**Blaise Aguera Y Arcas** [08:43]: Well, you know, I-

**Carlo Rovelli** [08:44]: You applied and you-

**Blaise Aguera Y Arcas** [08:45]: It's a bit of a mystery. I, I think, I think I-

**Carlo Rovelli** [08:46]: How you got inv- involved into that [laughs]

**Blaise Aguera Y Arcas** [08:48]: Yeah. I, I think I got it partly because of my, uh, uh, because some, some, um, kids at the time took the SAT test, which is normally for, for-

**Carlo Rovelli** [08:58]: Okay

**Blaise Aguera Y Arcas** [08:58]: ... uh, entering college.

**Carlo Rovelli** [08:59]: Yeah.

**Blaise Aguera Y Arcas** [09:00]: But there's a-- You can take it also early in the, in the eighth grade, and I, I took it, and I got a, I got a, a decent score. I think I got a better score than I did when I actually took it-

**Carlo Rovelli** [09:07]: Okay. [laughs]

**Blaise Aguera Y Arcas** [09:07]: ... at the end of high school [laughs]. But, um, uh-

**Carlo Rovelli** [09:10]: Okay, so you were invited to rewrite it.

**Blaise Aguera Y Arcas** [09:11]: Uh, yeah.

**Carlo Rovelli** [09:12]: Okay.

**Blaise Aguera Y Arcas** [09:12]: So was invited to do all of these, all of these things, and, and, um, that one was with the Navy. And, uh, it was, uh, I mean, it's a long story, but I'll try and give you a very bri-- a very abbreviated version. Uh, essentially, um, it was, uh, an institution that, that had started off modeling, uh, submarines and ships.

**Carlo Rovelli** [09:30]: Okay.

**Blaise Aguera Y Arcas** [09:30]: Uh, often physical models. So the, the building that I, that I worked in with my little, uh, coat and tie, it was a little bit silly. But it was a, it was a huge dark building with a physical, um, uh, with a, with a giant, uh, rotary arm-

**Carlo Rovelli** [09:42]: Yeah

**Blaise Aguera Y Arcas** [09:42]: ... that would move a one-quarter scale ship around-

**Carlo Rovelli** [09:45]: Oh, wow

**Blaise Aguera Y Arcas** [09:46]: ... uh, in a, in a gigantic vat. The vat was filled with agar solution. It was a sort of viscous fluid.

**Carlo Rovelli** [09:52]: To scale correctly.

**Blaise Aguera Y Arcas** [09:53]: Exactly. To scale the Reynolds number. Uh, and, um, uh, and it was dark also because the ag-- the agar would grow, uh, huge amounts of algae if there was any light. So it was all in pitch blackness and with this giant, you know, rumbling machine. Uh, and it looked like the set of a video game, like Doom or something like this.

**Carlo Rovelli** [10:10]: Uh, uh-huh.

**Blaise Aguera Y Arcas** [10:10]: But, um, but yeah, so I showed up, and I had no idea what to do. And my, my supervisor sent me to, um, alphabetize, uh, paper-- the papers in a filing cabinet.

**Carlo Rovelli** [10:18]: Yes.

**Blaise Aguera Y Arcas** [10:19]: Uh, I found one on seasickness, uh, which apparently is a big problem for-

**Carlo Rovelli** [10:23]: Ah, I see

**Blaise Aguera Y Arcas** [10:23]: ... uh, for sailors.

**Carlo Rovelli** [10:23]: Yeah.

**Blaise Aguera Y Arcas** [10:24]: And, um, and I, I began working on a, on a, a, a Fortran program that had been designed for stabilizing the, um, the roll of-

**Carlo Rovelli** [10:31]: Yes

**Blaise Aguera Y Arcas** [10:32]: ... big ships, uh, with, by, with active control of the rudder.

**Carlo Rovelli** [10:35]: I see.

**Blaise Aguera Y Arcas** [10:36]: And, um, uh, and basically, I, I improved the program in a variety of ways to, to, to stabilize the, the ship. And, and at the end of the summer, uh, I went on my first business trip, so I was fourteen.

**Carlo Rovelli** [10:46]: [laughs]

**Blaise Aguera Y Arcas** [10:46]: And, uh, and, and they sent me with my little suit and with a briefcase full of floppy disks to install it on a couple of, uh, carriers, on the USS Independence and, uh-

**Carlo Rovelli** [10:54]: Oh, so it was actually adopted.

**Blaise Aguera Y Arcas** [10:56]: And the USS Ranger.

**Carlo Rovelli** [10:57]: Fabulous.

**Blaise Aguera Y Arcas** [10:58]: Yes.

**Carlo Rovelli** [10:58]: Fabulous.

**Blaise Aguera Y Arcas** [10:59]: Yes.

**Carlo Rovelli** [10:59]: Uh, so if anybody today-- If, if today anybody's in the Navy and suffer for seasickness-

**Blaise Aguera Y Arcas** [11:04]: It's my fault

**Carlo Rovelli** [11:05]: ... is, is [laughs] is your program not working well enough? Is it [laughs]

**Blaise Aguera Y Arcas** [11:08]: It's possible. I, I would hope they've, they've updated it by now from Fortran 77, but [laughs]

**Carlo Rovelli** [11:12]: Yeah, they, they, this probably developed a little bit. Okay, fantastic. Oh, no, no, no. Another one, another one. There is another legend of you that you hacked the subway system for not paying the ticket or something like that.

**Blaise Aguera Y Arcas** [11:22]: That's true.

**Carlo Rovelli** [11:23]: That's true. That's, that's what I particularly like in your story [laughs]. I can-

**Blaise Aguera Y Arcas** [11:27]: It's your anarchist [laughs]

**Carlo Rovelli** [11:28]: I can particularly... Yeah, exactly.

**Blaise Aguera Y Arcas** [11:30]: The anarchist in you.

**Carlo Rovelli** [11:30]: It's anti-authoritarian, anti-anti... Yes, yes. Good. Fantastic. So that gives a sense of you pretty good. Um, let's, uh, let me plunge into the large question I want to get at, starting a little bit from the end, so I get a, a sense of where you are, uh, culturally, so to say. This-- We're here for a conference of consciousness. Question: What is consciousness? Or let me reformulate the question in a way I think is better. Um, what do you think people mean when they talk about consciousness?

**Blaise Aguera Y Arcas** [12:04]: Yes. Um, this is a, a great question because I, I think that experts, um, mean something very different from regular people. Uh, so, uh, very few experts, for instance, believe that AI systems are conscious. Um, but, uh, you know, there was a, a survey, uh, last year, uh, this sort of organized survey of a few hundred people, uh, regular people who, you know, which seems to suggest that, that a large and increasing proportion of people who interact with AI systems are like, "Yeah, there's probably something going on in there." So, um, the, you know, the, the experts tend to imagine that consciousness is some property inherent in something, in, in us, uh, in maybe certain other animals, but perhaps not in insects and so on.

**Carlo Rovelli** [12:47]: Yes.

**Blaise Aguera Y Arcas** [12:47]: That, um, uh... And, and I think, you know, the, the difficulty is that the experts try and think of-- generally try and think of something that is not just a soul-

**Carlo Rovelli** [12:55]: Okay

**Blaise Aguera Y Arcas** [12:55]: ... but that is something, uh, ineffable, uh, some property. Um, you know, panpsychists believe that it's maybe, you know, like almost like the charge of an electron or something, some elementary property in the universe. But what a lot of ordinary people mean is, does it seem to me like there's somebody home? You know, is it, uh, is it, uh, what David Graeber would've called, uh, can you have an interesting conversation with a, a, you know, with a, with a computer or with something? Uh, or when you look in the eyes of a certain animal, do you see, you know, do, do you see something looking back at you or somebody looking back at you?

**Carlo Rovelli** [13:29]: Something looking back at you. Exactly.

**Blaise Aguera Y Arcas** [13:30]: Yeah.

**Carlo Rovelli** [13:30]: There's somebody who's looking back at me-

**Blaise Aguera Y Arcas** [13:32]: Right

**Carlo Rovelli** [13:32]: ... so I can relate with him or her or it or whatever. Yes.

**Blaise Aguera Y Arcas** [13:36]: Exactly. And when you say, when you say relate, I think, you know, you're getting at the, at the core of m- of my belief about consciousness.

**Carlo Rovelli** [13:42]: So you, you, you said, uh, many common people, many experts. What a- where are you?

**Blaise Aguera Y Arcas** [13:49]: Uh, I'm, I guess, with the common people on this one.

**Carlo Rovelli** [13:51]: I see.

**Blaise Aguera Y Arcas** [13:52]: I, I, I believe that it is a relationship, that it is about relating. And, uh, this is, I think, one of the reasons that, you know, you and I, you know, have had a, have had a really, um, uh, fruitful, uh, kind of-

**Carlo Rovelli** [14:02]: Yeah

**Blaise Aguera Y Arcas** [14:02]: ... meeting of minds in the last week because, uh, you know, your-- a lot of your work is on thinking about reality from a relational perspective, uh, rather than an, uh, a, the perspective of imagining that everything is inherent in things, even down to the level of, of particles and quantum mechanics. And I think the same thing about, about consciousness, that it's a faculty that we developed and other social animals, uh, have developed in order to be able to put themselves in the place of others, uh, and also put themselves in the place of themselves. I know that sounds a little bit odd, but if you want to plan for the future, you need to be able to put yourself in your own place in, say, a week's time or under different circumstances to, to travel in time, to travel in space, uh, or to travel in perspective. You know, when, when you're looking at me right now and nodding, you know, you're, you're thinking, okay, you know, what, what do, you know, what am I saying to you? How am I thinking about who you are? What do you know? What do I need to explain? What don't I need to explain? What is your model of my model, and so on. And I think it's that, that mirroring, that sense of modeling another that is what we mean by consciousness, and especially, uh, self-consciousness is when we are modeling ourselves, which is complex because, you know, we are modeling the world. We're modeling all sorts of things. When we model ourselves, we are modeling a model. So there is something weirdly recursive or second order about that. Um, Douglas Hofstadter has talked about consciousness, uh, as a strange loop, the, the-

**Carlo Rovelli** [15:29]: Yeah

**Blaise Aguera Y Arcas** [15:29]: ... the philosopher and, and, and cognitive scientist, Douglas Hofstadter. I agree with him. Uh, for me, this strange loop has to do with the fact that when we start to have relations with others who also have relations with others, including ourselves, you get into this kind of hall of mirrors effect. And so there's something spooky about that.

**Carlo Rovelli** [15:46]: And this, this sort of, uh, set of mirrors is, uh, it's what creates a space of language where we can talk about conscious and we can talk about one another.

**Blaise Aguera Y Arcas** [15:58]: Yes.

**Carlo Rovelli** [15:58]: We can communicate. And, uh, from what you're saying, it's almost like, uh, you know, we start thinking of consciousness when we, we start using you instead of it.

**Blaise Aguera Y Arcas** [16:06]: Yes. Uh, most languages have some distinction between, uh, you know, nouns that are inanimate and ones that are animate.

**Carlo Rovelli** [16:14]: Yeah.

**Blaise Aguera Y Arcas** [16:14]: But they also differ in, in, in where they ascribe animacy. So, uh, you know, the two extreme examples are, uh, in, in Roman law, uh, a slave was, uh, an instrumenta according to Varro, an, an it essentially. That is to say-

**Carlo Rovelli** [16:29]: A slave is it

**Blaise Aguera Y Arcas** [16:29]: ... no agency.

**Carlo Rovelli** [16:30]: Yes.

**Blaise Aguera Y Arcas** [16:31]: Uh, now, I don't really believe that most Romans, uh, you know-

**Carlo Rovelli** [16:34]: [laughs]

**Blaise Aguera Y Arcas** [16:34]: ... necessarily, you know, right, related to their slaves in that way, but, but the, the point is, you know, you-

**Carlo Rovelli** [16:38]: Well, I know that it's, uh, if you-- if, if there was a trial against some person in the aristocracy, Patrizio-

**Blaise Aguera Y Arcas** [16:45]: Mm-hmm

**Carlo Rovelli** [16:46]: ... uh, it was okay to torture, torture his slaves-

**Blaise Aguera Y Arcas** [16:49]: Right. Right, but not him

**Carlo Rovelli** [16:51]: ... to extract some information, you know?

**Blaise Aguera Y Arcas** [16:52]: Exactly. As-- for, for the same, for the same reasons. Right. So lack of agency. Uh, on, on the other end of the spectrum, uh, would be many animist traditions. Um-

**Carlo Rovelli** [17:01]: Right

**Blaise Aguera Y Arcas** [17:01]: ... but, uh, you know, one that I n- that I know a little bit better, uh, just from having read the books of Robin Wall Kimmerer, uh, are the Potawatomi. Um, but you know, Shinto, you know, would have animist beliefs. Many others, you know, many others have animist beliefs. But in the Potawatomi tradition, um, you know, a lot of things are whos rather than its. There are, there are, you know, bear people and tree people, uh, and, you know, and so on. You know, every-everything is a person, uh, except when it is harvested for use. So when you, when you-- when a hunter kills something, that mo- in that moment, it stops being a who and begins being an, an, an it.

**Carlo Rovelli** [17:39]: So, um, that seemed to imply that we shouldn't, uh, be anguished of finding a sharp distinction between different uses of, of, of the you, different idea of consciousness, different attribution of, uh, of, uh-

**Blaise Aguera Y Arcas** [17:54]: No. That's right. There, there are disagreements

**Carlo Rovelli** [17:56]: ... theories. Yes.

**Blaise Aguera Y Arcas** [17:57]: People have different models. So you can have two responses to that. Either you can say some of them are right and some of them are wrong.

**Carlo Rovelli** [18:03]: Exactly.

**Blaise Aguera Y Arcas** [18:04]: Uh, or you can say, you know, this is a little bit like color, for instance. Uh, you know, where, where, um, say in, in Russian, the definition of green is a little bit different from the English definition of green.

**Carlo Rovelli** [18:15]: Yes. And, and, and asking who is-

**Blaise Aguera Y Arcas** [18:17]: And neither is wrong

**Carlo Rovelli** [18:17]: ... asking who is right is silly.

**Blaise Aguera Y Arcas** [18:19]: Exactly.

**Carlo Rovelli** [18:20]: Yes. This, to some extent, this is a, uh, rich way of thinking of what we mean when we say consciousness. So it's a lot to say and a lot to understand and, uh, but it's also deflationary. It's, uh, it takes away the, uh, uh, the strong question, what is consciousness by itself? And, uh, trying to ask, uh, in a sort of, uh, absolute way, is the system conscious or not, uh, doesn't seem to be a good question anymore.

**Blaise Aguera Y Arcas** [18:53]: Right.

**Carlo Rovelli** [18:53]: To, to which extent, in which sense, how do we think about it?

**Blaise Aguera Y Arcas** [18:56]: Exactly.

**Carlo Rovelli** [18:57]: It's more relevant.

**Blaise Aguera Y Arcas** [18:58]: Uh, right. I mean, my, my feeling is that the reason-- Uh, so David Chalmers has famously talked about consciousness as the hard problem.

**Carlo Rovelli** [19:04]: Yes.

**Blaise Aguera Y Arcas** [19:05]: I think you and I both agree that perhaps it's not such a hard problem.

**Carlo Rovelli** [19:08]: Yes.

**Blaise Aguera Y Arcas** [19:08]: But, uh, but one of the reasons that I think in Western philosophy it tends to be thought of as a hard problem is because, um, we, we tend to not be very relational in how we think about things. And when you isolate a person, when it's cogito, ergo sum, you know, I think therefore I am, everything is I, I, I, and you don't-- and you don't, um, imagine relationships with others to be relevant to this question, uh, it becomes a hard problem because, because then you've cut relationships out of the picture. Um-

**Carlo Rovelli** [19:36]: Yes. I couldn't agree more with you than on, on this. Um, for our listen, c-c-could you, um, uh, say what Chalmers means by hard problem and, and an easy problem-

**Blaise Aguera Y Arcas** [19:49]: Yes

**Carlo Rovelli** [19:50]: ... of consciousness?

**Blaise Aguera Y Arcas** [19:51]: Um, well, uh, so according to Chalmers, um, who is here with us, and we've had a-also a lot of interesting conversations with, the easy problem is: how does the brain do it? How does the brain work? Uh, of course, it, you know, the joke is that it's not so easy. That's what the entire field of neuroscience is, is about, you know, trying to solve, and we've been at it for decades, and we make progress, but it's very hard. But the hard problem for Chalmers is: why does that feel like anything? Why, why is there a thing it is like to be y-you or me or a bat? Uh, you know, the, the-- Nagel famously asked, "What is it like to be a bat?" Uh-

**Carlo Rovelli** [20:27]: Yeah

**Blaise Aguera Y Arcas** [20:28]: ... and, and, uh, and I think that's a really interesting question, but not such a hard question. We are, in some sense, made to imagine what it is like to be-

**Carlo Rovelli** [20:36]: Yeah

**Blaise Aguera Y Arcas** [20:36]: ... each other or bats or a fish looking at-- that you look at from a, from a, from a bridge, you know, into the water or whatever. Empathy and putting ourselves in the position of others is what we do naturally and what any social animal does naturally.

**Carlo Rovelli** [20:50]: Yeah. Um, very well. So the, the, and, and, and, and we're very close on that. I mean, we-- I guess, I guess we, we fully agree on that. I like particularly your reference to the fish from, um, seen from the, uh, the bridge of the water, which is a, uh, a reference to Taoism and a, a famous story about, um, what do we know about fish being happy, uh, which I used even in a title of, uh, one of my books. So thank you for mentioning that. So there's a hard problem. Uh, uh, uh, what, what is consciousness by itself? And we agree that is, uh, it's bad pos-- it's a badly posed question. And then there's a so-called easy problem. Of course, it's not easy at all, which is or-- okay, right. But then what happened in the mind, in the mind being the functioning of the brain of people, uh, can we make sense of, uh, what is going on? What, what are the right, um, conceptual tools for thinking about that? And here you have a central idea of one, uh, key concept that can be used for make sense of that, which is computation. Can you say something about that?

**Blaise Aguera Y Arcas** [22:03]: Yes, of course. Well, so first of all, you know, for neuroscientists who study the brain, uh, computation has always been essential. Uh, so, you know, we, we generally call it computational neuroscience. Uh, you know, this, this is all modern neuroscience in effect. It was born at-- actually at the same time as, as the field of computation. So, you know, when we think about, uh, you know, the very early, um, uh, kind of special f-purpose computers of the early twentieth century, those were happening around the same time as, uh, early experiments in, in, in neuroscience by Edgar Adrian and, and, and so on in the nineteen twenties. And then, um, general computation, which really began in nineteen forty-five, uh, also coincided with, with, um, the, with the rise of computational neuroscience. And in fact, computer science was born, uh, out of an attempt to perform mental functions by machine. Uh, you know, that, that was the original, the original point. And, um-

**Carlo Rovelli** [22:57]: Machine that compute, in a sense.

**Blaise Aguera Y Arcas** [22:59]: Yeah. Uh, yeah. Uh, and, and machine, machine not only that-- a machine not only that could compute, uh, in some very narrow or specialized sense, but that could, that could, uh, do what a brain does. Uh, you know, there was a lot of journalism back then that was sort of, uh, you know, "Alan Turing builds an electric brain at Teddington." And, you know, we look at these headlines now, and we imagine that it was just, you know, clickbait-

**Carlo Rovelli** [23:20]: Mm-hmm

**Blaise Aguera Y Arcas** [23:20]: ... uh, you know, or, or journalists-

**Carlo Rovelli** [23:21]: Mm-hmm

**Blaise Aguera Y Arcas** [23:21]: ... doing what they always do. But it, it wasn't. That, that was the ambition. And, and this is why Turing, uh, for instance, was, you know, also the father of AI, not just of computer science, uh, and, and, and had a lot to say about neuroscience as well. He, you know, he actually imagined already, uh, neural nets, uh, or unorganized machines, as he called them, in nineteen forty-eight. Um, so, uh, so yeah, c-computer science and neuroscience were born together, and they only diverged later on. Uh, and the reason they diverged was that, uh, we started to figure out how to use computers practically to do a bunch of different sorts of problems. But, um, we were, we were running, um, programs with well-defined algorithms that were written by hand, and all of the attempts to try and simulate, uh, brains or, or perform general thought using those kinds of programs failed. This is what we now call good old-fashioned AI.

**Carlo Rovelli** [24:15]: Mm-hmm.

**Blaise Aguera Y Arcas** [24:15]: And, and various attempts at that led to the AI winters of the fifties, of the seventies, of the eighties.

**Carlo Rovelli** [24:21]: A long period of, uh, failed stagnation.

**Blaise Aguera Y Arcas** [24:24]: Stagnation. Yeah. Yeah. It didn't work until we-- until the era of neural nets. But I'm getting a bit ahead of myself. The, uh, the point is, you know-- I mean, you, you really are asking why. Why would we imagine that brains are computational? Well, um- If you believe that, that, that the key thing that brains do is to build models, whether that is of the world or of the self, um, building a model is inherently a computational task. Modeling is computational. Um, and modeling is really important, um, in the sense that if, if the purpose of being smart is to be able to, um, respond intelligently to your environment and, and to others, then, um, you know, that is a modeling problem. This was something that was well understood also by Norbert Wiener and the cyberneticists, uh, also nineteen forties, nineteen fifties. If you want to regulate yourself even in the most basic sense, you know, you want to maintain a stable internal temperature, you want to make sure you always have enough to eat, uh, or whatever, whatever that is. That means modeling your environment in order to be able to act on it. Uh, so-

**Carlo Rovelli** [25:28]: And to model your environment, you should know something about it. You should have information about it.

**Blaise Aguera Y Arcas** [25:33]: Yes.

**Carlo Rovelli** [25:33]: And to model your own body, you have to have information about your body.

**Blaise Aguera Y Arcas** [25:36]: About it too. Exactly. So, so there, there's a duality about modeling what is on the outside-

**Carlo Rovelli** [25:41]: Yeah

**Blaise Aguera Y Arcas** [25:41]: ... and modeling what is on the inside, and you, you need to do both. And they're both computational in exactly the same way.

**Carlo Rovelli** [25:46]: And computation-- To what extent computation is a-- it's, uh, dealing and using information, and to what extent is something else?

**Blaise Aguera Y Arcas** [25:54]: Um, computation and information absolutely go together. They're inseparable.

**Carlo Rovelli** [25:58]: Go together.

**Blaise Aguera Y Arcas** [25:58]: Yeah. Well, I, I should say they're inseparable the moment you take information in the richer sense that, uh, Kolmogorov meant it. Uh, so there is Shannon, Shannon information, uh, which physicists, you know, tend to know a little bit more about.

**Carlo Rovelli** [26:13]: Yeah.

**Blaise Aguera Y Arcas** [26:14]: That just, that just says a difference. So, you know, if you have a measurable difference, you can measure that in terms of bits and, you know, you can relate that to entropy and energy. But, um, but there's a, a slightly richer sense of information, a more restricted sense called Kolmogorov information or algorithmic information, which is what Gregory Bateson, the philosopher, called a difference that makes a difference. Uh, and I think the way to understand the difference between those two definitions is that, uh, DNA in your cells, you know, when you're alive, is a code. Uh, you know, it's, it's-- it has a causal effect on the world. You know, if you have some mutation, uh, you know, in a certain gene that then you might have sickle cell anemia. It obviously has, you know, serious effects on, on the body, on your life. Whereas once the cells are dead, if you die, those-- that DNA is still there, but it doesn't matter anymore, right? Whether, whether, whether a base pair is this way or that way, um, there's no difference, no macroscopic difference in the world once that in-- once no computation is happening anymore with that information. So there is, if you like, dead information and live information. Live information is computational.

**Carlo Rovelli** [27:23]: This is interesting, and let me make a little bit sharper. There is something that confuses a lot of people, I believe, when there's talking about, uh, the role of computation, um, in, uh, uh, trying to figure out what happened, uh, in, in, in ourself, in our brain, in our thinking, in our mind. Uh, mind being the, the name we give to all this activity that we, we, we, we do inside ourself, our inner activity, so to say. And the confusion is often the following. Um, there's a reaction which is very common. Um, okay, but if, um, if it's just computation, if it's just a code, um, if I write this code on a piece of paper, uh, suppose I could write a code on a piece of paper that somehow capture what happened, the coding in my brain, then that this p-piece of paper is equally, uh, has a consciousness in the same way I have it. I mean, you can look in my eye-eyes and, and, and relate to me to use your previous characterization. Could, could you look at that pic-piece of paper and have the same experience?

**Blaise Aguera Y Arcas** [28:28]: Right. Or does the piece of paper have an experience on its own?

**Carlo Rovelli** [28:30]: And that piece of paper have an experience. Could you describe the piece of paper having an experience? And the distinctive reaction is no, no, no, no, no, and therefore coding has nothing to do with that. Where, where is the mistake here?

**Blaise Aguera Y Arcas** [28:42]: Uh, so I think the mistake is twofold. Uh, one of them is to confuse static information for a process. Uh, and that's exactly that live versus dead distinction. You know, if you-- Once the, once the cells are dead, once there's nothing interpreting and acting on, on that information-

**Carlo Rovelli** [28:59]: The DNA is, is also dead.

**Blaise Aguera Y Arcas** [29:00]: The DNA is also dead, right. It's, it's, it's no longer Kolmogorov information. It's only Shannon information.

**Carlo Rovelli** [29:06]: Aha. Okay.

**Blaise Aguera Y Arcas** [29:07]: Uh, so, uh, so that, that's-- And, and Shannon information is not directly connected with computation anymore. Uh, and that's the second thing. So, you know, it's, uh, computational. You know, it's not only that there is a dynamic process-

**Carlo Rovelli** [29:18]: Mm-hmm

**Blaise Aguera Y Arcas** [29:18]: ... but also, uh, and now I have to introduce another, another name, uh, who's also seminal figure in the dawn of computing, John von Neumann. So, uh, in, in Turing's original definition of computation, he imagined, uh, a, a tape with, um, with, uh, slots for symbols on them and a machine that would-- that could move back and forth on that tape reading, writing, and erasing symbols according to a set of rules. Uh, and basically, you know, uh, universal computation is when you take the table of, of rules and you're able to write them on the tape too, and then the snake eats its own tail. You, you know, the, the machine, uh, if it's a universal computer, can run the code on the piece of tape.

**Carlo Rovelli** [30:01]: Mm-hmm.

**Blaise Aguera Y Arcas** [30:01]: So this is great, but there is something critical missing, which is a link or a relationship between the machine that is doing this and the information on the tape.

**Carlo Rovelli** [30:12]: Uh-huh.

**Blaise Aguera Y Arcas** [30:13]: Uh, so this is really important because, uh, if-

**Carlo Rovelli** [30:15]: So the information on the tape should be connected to something else to be information in a sense.

**Blaise Aguera Y Arcas** [30:20]: Yes. Yes. And, and this, this really gets at the connection between computation not only in brains, but computation and life. Uh, so von Neumann had this wonderful insight, uh, in the late forties, uh, or early fifties. Um, and he was trying to think-- He and Turing both thought a lot about, about biology toward the end of their lives.

**Carlo Rovelli** [30:37]: Which is very interesting because in a sense they were mathematicians.

**Blaise Aguera Y Arcas** [30:40]: Yes.

**Carlo Rovelli** [30:40]: Extremely wide angle-

**Blaise Aguera Y Arcas** [30:42]: Yeah.

**Carlo Rovelli** [30:42]: -mathematicians interested in very, very general questions.

**Blaise Aguera Y Arcas** [30:45]: Yes, yes.

**Carlo Rovelli** [30:45]: But then they go, uh, they start thinking biological terms and, and biological question, which is the same thing that has happened to Schrödinger-

**Blaise Aguera Y Arcas** [30:54]: Yes, exactly.

**Carlo Rovelli** [30:55]: -starting from physics. The same thing is happening to you, in which you start by doing modeling of, uh, images in two D and three D, and then you write questions about what is intelligence-

**Blaise Aguera Y Arcas** [31:04]: Yeah.

**Carlo Rovelli** [31:04]: -what is life.

**Blaise Aguera Y Arcas** [31:04]: I mean, I'm no, I'm no Schrödinger or Turing or von Neumann, but yes, we've followed-

**Carlo Rovelli** [31:07]: No, but you live on their shoulders. [chuckles] Yes.

**Blaise Aguera Y Arcas** [31:09]: Yes. And, and we have, we have all followed that trajectory, and that's why I named my little book, uh, after Schrödinger's, uh, book, What Is Life?

**Carlo Rovelli** [31:15]: What Is Life? Yes.

**Blaise Aguera Y Arcas** [31:17]: But, um, but, but I have to say the reason that they did it, uh, is because for them the fields were never separate to begin with. You know, they were, they were, they were imagining, uh, computation as being, you know, about, uh-

**Carlo Rovelli** [31:28]: Probably the deep correct intuition that-

**Blaise Aguera Y Arcas** [31:30]: Right.

**Carlo Rovelli** [31:31]: -that you-- that brings us ahead here.

**Blaise Aguera Y Arcas** [31:32]: Exactly, exactly. So i-in a way, I think it took me a, a longer route around than them in, in a certain sense. But, um, but yeah, the, the reason-- So, w- uh, von Neumann was asking himself the question-

**Carlo Rovelli** [31:44]: Yes.

**Blaise Aguera Y Arcas** [31:45]: -how can a robot made out of Legos, uh, you know, as, as I imagine it, that is swimming around on a pond that has some Lego, loose Legos bobbing in it. How can, how can a robot like that, um, take those Legos and build another robot like itself?

**Carlo Rovelli** [32:00]: Mm-hmm.

**Blaise Aguera Y Arcas** [32:01]: Um, which seems intuitively like a little bit of a, a, a contradiction or a, a paradox. You know, like building something just as complex as you yourself are. How could that happen? But that's of course exactly what a bacterium does when it reproduces. That's what, that's what any living system has to do. It has to reproduce itself. So how is that possible? And what he realized is that it would have to be the case that, um, that a, a machine like that would have to have instructions inside itself, uh, an instruction tape for how to build me. And it would have to have a machine inside itself, which he called machine A, that could move along that tape and follow the directions, uh, whatever they say, to assemble the Legos. Uh, and it would also have to have a machine B, which could copy the tape.

**Carlo Rovelli** [32:46]: Yeah.

**Blaise Aguera Y Arcas** [32:46]: And if furthermore, the instructions for building machines A and machine B are also on the tape, then you, you have, you have life. Then, then you have this, uh-

**Carlo Rovelli** [32:58]: You, you, you have the minimal structure needed to have some-

**Blaise Aguera Y Arcas** [33:00]: Exactly.

**Carlo Rovelli** [33:00]: To, to, to, to, to, to have things that do the things that life does.

**Blaise Aguera Y Arcas** [33:03]: That's minimal life. That's right.

**Carlo Rovelli** [33:04]: And that's life. Yeah.

**Blaise Aguera Y Arcas** [33:05]: That's right.

**Carlo Rovelli** [33:05]: That's minimal life.

**Blaise Aguera Y Arcas** [33:06]: But the, but the really cool insight, the, the thing, the, the, the genius move of von Neumann was that he then proved that machine A is literally a Turing machine.

**Carlo Rovelli** [33:15]: Right.

**Blaise Aguera Y Arcas** [33:16]: Uh, a universal Turing machine. So it, it's-- He called it a universal constructor. A universal constructor is a universal Turing machine.

**Carlo Rovelli** [33:22]: So this brings back computation as a sort of-

**Blaise Aguera Y Arcas** [33:24]: Exactly.

**Carlo Rovelli** [33:25]: -key language for understanding what is going on.

**Blaise Aguera Y Arcas** [33:27]: Right. Not only for understanding brains, but for understanding everything that is alive.

**Carlo Rovelli** [33:31]: Life.

**Blaise Aguera Y Arcas** [33:31]: Life.

**Carlo Rovelli** [33:31]: Everything which is life.

**Blaise Aguera Y Arcas** [33:32]: Right.

**Carlo Rovelli** [33:32]: Yes.

**Blaise Aguera Y Arcas** [33:33]: It has to be computational.

**Carlo Rovelli** [33:34]: Yes. And the, and if I get-- Maybe I'm flattening it a little bit too much, but if, uh, the, the question I ask is, uh, so why computation by itself abstractly is not life, is because you have it to, to, to, to go and it work. This is a little bit like if I say, um, what is a bicycle? Is, is just the, the wheels? No. It's just the, this other piece? No. It's just the other piece? No. So w-what it is? Well, it's the structure of the bicycle.

**Blaise Aguera Y Arcas** [34:02]: Exactly.

**Carlo Rovelli** [34:02]: But then you say, okay, you draw the structure of the bicycle. Is that a bicycle? No, because you need the pieces.

**Blaise Aguera Y Arcas** [34:08]: That's right.

**Carlo Rovelli** [34:08]: I mean, a picture of a bicycle is not a bicycle, so you need both.

**Blaise Aguera Y Arcas** [34:11]: Well, it's a hundred-

**Carlo Rovelli** [34:12]: Sorry. So-

**Blaise Aguera Y Arcas** [34:12]: Yeah, a hundred percent. There, there's also something else really important here.

**Carlo Rovelli** [34:15]: Okay.

**Blaise Aguera Y Arcas** [34:15]: Which is that, you know, sometimes people object, oh, but a simulation of a bicycle is not a bicycle.

**Carlo Rovelli** [34:20]: Yes.

**Blaise Aguera Y Arcas** [34:20]: Right? Like if I just have a, um, simulated bicycle in my computer, you can't ride it.

**Carlo Rovelli** [34:25]: Yes.

**Blaise Aguera Y Arcas** [34:25]: But this is the difference between computation as it exists in life versus as it exists, uh, in most of the computers that we build today.

**Carlo Rovelli** [34:34]: Okay.

**Blaise Aguera Y Arcas** [34:34]: And the difference is that von Neumann's universal constructor is a universal Turing machine that actually moves matter around. So the matter and the information are the same. In other words, in order for that m, that machine A to be able to build another machine A by following the instructions on the tape, it's not just, uh, you know, imagining a machine A or modeling a machine A, it's literally building a machine A. So it's an embodied form of computation. That's what embodiment really means. It means that the bits that you're manipulating include atoms as well.

**Carlo Rovelli** [35:08]: Yes. I find this, uh, um, this very clarifying. I, I often think that we, we get confused precisely when we abstract something, and then we, we think, uh, uh, we forget that, um, uh, the information we're talking about is always embodied information-

**Blaise Aguera Y Arcas** [35:25]: It's embodied, exactly.

**Carlo Rovelli** [35:26]: -in reality.

**Blaise Aguera Y Arcas** [35:27]: And, and this is, this is the sense in which what the kidney does is computation. So, you know, if I say to so- to a n- you know, most people, you know, the kidney computes, they'll be like, "That-- You're crazy." Of course, the ki- the kidney is not doing some abstract computation. It's not figuring out three plus eight. It's filtering urea out of blood. But the point is, if you think about matter as carrying information, computing is exactly what it's doing. It's figuring out what is the urea and, and, and, uh, separating it from the blood, and that is a computation-

**Carlo Rovelli** [35:54]: Yes.

**Blaise Aguera Y Arcas** [35:54]: -in this von Neumann sense.

**Carlo Rovelli** [35:55]: Yes. This is a-- I find this a, a very compelling way of thinking, uh, addressing this question. So there's se-several questions here, right? What is, uh, uh, how to think about information or how to think about life, and it connect to how to think about consciousness. I mean, this is a, um, these are all ways to, um, ask these questions, not as essentialist question, what is the essence of life? This is asking what ha- what happened the system that we see as living? What is the best way we can make sense of, uh- Of, uh, of, uh, what, what is the best conceptual tools for understanding what is going on, um-

**Blaise Aguera Y Arcas** [36:32]: Exactly

**Carlo Rovelli** [36:33]: ... there.

**Blaise Aguera Y Arcas** [36:33]: And, and, uh, the, the, the, the bridge, and just to put it maybe one more way-

**Carlo Rovelli** [36:37]: Yes

**Blaise Aguera Y Arcas** [36:37]: ... that I think might, might help some people. The bridge is functionalism.

**Carlo Rovelli** [36:41]: The bridge is functionalism.

**Blaise Aguera Y Arcas** [36:43]: Yeah.

**Carlo Rovelli** [36:43]: Exactly. So, uh, yeah, please say more about that because that's key idea-

**Blaise Aguera Y Arcas** [36:48]: I think it's key. Um-

**Carlo Rovelli** [36:48]: Which ties, uh, uh, ties computation, um, uh, information and, and what we mean when we give name to something.

**Blaise Aguera Y Arcas** [36:57]: Exactly. I-- So, um, when we-- So the word function sounds like it has two very different meanings. Uh, one of them is mathematical.

**Carlo Rovelli** [37:06]: Yes.

**Blaise Aguera Y Arcas** [37:07]: Uh, so, you know, math- mathematicians-

**Carlo Rovelli** [37:08]: F of x is x squared.

**Blaise Aguera Y Arcas** [37:09]: F of x is x squared. Exactly.

**Carlo Rovelli** [37:10]: X square is a function of x.

**Blaise Aguera Y Arcas** [37:11]: Exactly. So that's the mathematical sense of function.

**Carlo Rovelli** [37:14]: Yeah.

**Blaise Aguera Y Arcas** [37:14]: But, um, but when we say a boat functions, what we mean is it doesn't sink and it-

**Carlo Rovelli** [37:18]: It floats and it takes me to-

**Blaise Aguera Y Arcas** [37:19]: You know, it floats. It gets you from one place to another

**Carlo Rovelli** [37:20]: ... it takes me the other side of the water here to Judaica.

**Blaise Aguera Y Arcas** [37:23]: Exactly. Um-

**Carlo Rovelli** [37:23]: It functions well. Yeah.

**Blaise Aguera Y Arcas** [37:25]: Exactly. And likewise, a kidney, you know-

**Carlo Rovelli** [37:27]: It functions

**Blaise Aguera Y Arcas** [37:27]: ... functions.

**Carlo Rovelli** [37:27]: It has a function.

**Blaise Aguera Y Arcas** [37:28]: And if it doesn't function, you die.

**Carlo Rovelli** [37:29]: Yeah, yeah.

**Blaise Aguera Y Arcas** [37:29]: Um, or you need to go on dialysis.

**Carlo Rovelli** [37:31]: So how are these two different meanings connection?

**Blaise Aguera Y Arcas** [37:34]: They're the same.

**Carlo Rovelli** [37:35]: Yeah.

**Blaise Aguera Y Arcas** [37:35]: They, they're the same. Uh, and, and the reason that they're the same is because of this embodiment that we were just talking about of von Neumann's.

**Carlo Rovelli** [37:42]: Okay.

**Blaise Aguera Y Arcas** [37:42]: So, um, function means that, um, that you can describe or coarse grain, as we would, as we would say as physicists. You can, uh, you can coarse grain the behavior of something, uh, in order to describe it in terms of, uh, of information. Um, but if the thing that you're coarse graining is the movement of, of matter or of bits that are embodied, uh, you know, in, in, uh, in, in atoms, then, um, uh, this colloquial sense of function is exactly the mathematical sense of function.

**Carlo Rovelli** [38:15]: So, uh, the, the two are strictly connected to different ways of thinking.

**Blaise Aguera Y Arcas** [38:19]: Yes.

**Carlo Rovelli** [38:19]: And, and a function, um, let me get back to something you said at the beginning, which for me is particularly-- Um, if you just look-- think about the boat, uh, that takes us the other side of the water to the, to the Judaica Island. Uh, if I just describe it in very, very strictly physicalist terms, right? Just, you know, atoms moving around according. I don't see the function.

**Blaise Aguera Y Arcas** [38:45]: That's right.

**Carlo Rovelli** [38:46]: 'Cause just, you know, atom pushing and pulling one another and-

**Blaise Aguera Y Arcas** [38:48]: The, the same rules are, are, are governing-

**Carlo Rovelli** [38:50]: And that's it

**Blaise Aguera Y Arcas** [38:50]: ... the atoms in the boat is governing every other atom.

**Carlo Rovelli** [38:51]: Exactly.

**Blaise Aguera Y Arcas** [38:52]: Right.

**Carlo Rovelli** [38:52]: So, um, there is one aspect of the story which seems to be magical here. Where does the functionality of the boat come from? We cannot say it's illusory because we're talking about something very real, right? This is-- We, we use the boat to go. You pay a ticket and go.

**Blaise Aguera Y Arcas** [39:07]: That's right.

**Carlo Rovelli** [39:08]: So where does it come from?

**Blaise Aguera Y Arcas** [39:09]: It comes from other functions.

**Carlo Rovelli** [39:11]: Exactly. That's-

**Blaise Aguera Y Arcas** [39:11]: [laughs]

**Carlo Rovelli** [39:11]: That's exactly where you, you know-

**Blaise Aguera Y Arcas** [39:13]: Yeah

**Carlo Rovelli** [39:13]: ... I'm fascinated by what you're saying is, find a deep resonance with my worldview.

**Blaise Aguera Y Arcas** [39:18]: Right. The fact that it's relational and that it's functional are the s- so again, functionality and relationality come together. So here, here's a way to understand that. Um, when we send mail, uh, you know, we, we, um, what we care about is the, the letter or the package arriving. You know, if we're sending it from here to the mainland, it could go by boat.

**Carlo Rovelli** [39:36]: Yeah.

**Blaise Aguera Y Arcas** [39:36]: It could go by a drone. Uh, it could, uh, go in my pocket, and I ride on the boat. It could, it could go in a submarine. Uh, we don't care. We just care that the letter gets there.

**Carlo Rovelli** [39:46]: Yeah.

**Blaise Aguera Y Arcas** [39:46]: That's the function.

**Carlo Rovelli** [39:47]: Yeah.

**Blaise Aguera Y Arcas** [39:47]: Uh, right? It's, it's letter carrier. Um, uh, and of course, a boat might have other functions too, but that's the f- that's the function that I, as the customer or user, if you like, care about. So, um, you know, when, when, when Turing theorized about computation, one of the key concepts that comes out of this is multiple realizability or platform independence. Uh-

**Carlo Rovelli** [40:07]: Right

**Blaise Aguera Y Arcas** [40:08]: ... meaning, meaning that there are many ways of computing the same thing.

**Carlo Rovelli** [40:10]: Right.

**Blaise Aguera Y Arcas** [40:11]: Uh, you know, you could use it-- you could compute it with a specialized Turing machine or with a universal Turing machine running, you know, that specialized Turing machine code. Um, even the physical basis of the Turing machine could be, uh, you know, it could be done with tape, uh, or it could-

**Carlo Rovelli** [40:25]: Right

**Blaise Aguera Y Arcas** [40:25]: ... be done with, with rocks, or it could be done with people waving semaphore flags or whatever.

**Carlo Rovelli** [40:30]: So in a sense, the physical basis is essential because that's what you want.

**Blaise Aguera Y Arcas** [40:33]: Yeah.

**Carlo Rovelli** [40:33]: But it's irrelevant because you can-

**Blaise Aguera Y Arcas** [40:35]: But separable

**Carlo Rovelli** [40:35]: ... replace it with something completely different.

**Blaise Aguera Y Arcas** [40:37]: Exactly.

**Carlo Rovelli** [40:37]: And yet there is something which is the same, and that this is the same is what interests us.

**Blaise Aguera Y Arcas** [40:42]: That's right.

**Carlo Rovelli** [40:43]: So we have different accounts, possible accounts of the same set of physical facts, if you want. Uh, but there's no contradiction between them.

**Blaise Aguera Y Arcas** [40:51]: Not at all.

**Carlo Rovelli** [40:51]: There's no contradiction whatso- whatsoever.

**Blaise Aguera Y Arcas** [40:53]: Exactly.

**Carlo Rovelli** [40:54]: Um, I think the people listening to that and knowing your name would, would like to know something more closer, um, in a sense, uh, at the light of all that, okay? Uh, first question, and I'm really flattening it. Do l- language model understand us?

**Blaise Aguera Y Arcas** [41:14]: Yes.

**Carlo Rovelli** [41:15]: Which is a title of one of your, uh, celebrated articles. Yes or no?

**Blaise Aguera Y Arcas** [41:19]: Yes. The short answer is yes, they do.

**Carlo Rovelli** [41:20]: They do.

**Blaise Aguera Y Arcas** [41:21]: Um, now, at the same time, it's relational.

**Carlo Rovelli** [41:24]: Yes.

**Blaise Aguera Y Arcas** [41:24]: So, you know, I, uh-

**Carlo Rovelli** [41:24]: What does it mean they understand us?

**Blaise Aguera Y Arcas** [41:26]: What does it mean for them to understand us, right?

**Carlo Rovelli** [41:27]: Exactly. That's the right question.

**Blaise Aguera Y Arcas** [41:28]: Uh, you know, so, so I, I, um, I think they do.

**Carlo Rovelli** [41:31]: Yeah.

**Blaise Aguera Y Arcas** [41:31]: Um, but, uh, but I-- You know, if, if somebody firmly believes that they don't, I, I, I also am unwilling to say, well, you're wrong and I'm right because understanding take-- you know, takes two, right?

**Carlo Rovelli** [41:41]: Takes two. Yes.

**Blaise Aguera Y Arcas** [41:42]: It takes, it takes two to tango. But, um, but in my view, um, many people who say large language models don't understand us-

**Carlo Rovelli** [41:49]: Yes

**Blaise Aguera Y Arcas** [41:50]: ... but are perfectly happy to, you know, interact with large language models in a way that relies in, in a fairly obvious way on them understanding everything that they're saying and following directions and so on, are, are being a little bit-- are, are, let's say, applying a, you know, quite a double standard.

**Carlo Rovelli** [42:05]: I think they're, they're referring to a metaphysical assumption about understanding being-

**Blaise Aguera Y Arcas** [42:10]: Yes

**Carlo Rovelli** [42:10]: ... uh, there's a gap between things understand and don't understand.

**Blaise Aguera Y Arcas** [42:13]: Right.

**Carlo Rovelli** [42:14]: And so this is a metaphysical assumption about duality, which is what you're, uh, uh, you're questioning here.

**Blaise Aguera Y Arcas** [42:21]: Exactly.

**Carlo Rovelli** [42:21]: Um, and, uh, again, a question that, uh, it's ill-posed unless it's characterized. How far we are from, uh- Uh, general artificial intelligence-

**Blaise Aguera Y Arcas** [42:32]: Well, um-

**Carlo Rovelli** [42:33]: How close we are.

**Blaise Aguera Y Arcas** [42:34]: Yeah, I mean, that's-- I, I think that's a leading question because you've, you've read another of my articles, which is Artificial General Intelligence Is Already Here.

**Carlo Rovelli** [42:41]: Exactly. [laughs]

**Blaise Aguera Y Arcas** [42:42]: [laughs]

**Carlo Rovelli** [42:42]: It's another, uh, well-known of your articles that raise a lot of debates-

**Blaise Aguera Y Arcas** [42:46]: Yeah

**Carlo Rovelli** [42:46]: ... in which people start to scream, "No, not at all. Yes."

**Blaise Aguera Y Arcas** [42:49]: And I think for the same reason as the-

**Carlo Rovelli** [42:51]: For the same reason

**Blaise Aguera Y Arcas** [42:51]: ... as the understand one, you know.

**Carlo Rovelli** [42:52]: So in a sense, yes. In a sense, no.

**Blaise Aguera Y Arcas** [42:54]: Right. Um, although, uh, I, I should also say that, um, I think that, that there's been a lot of moving of the goalposts-

**Carlo Rovelli** [43:00]: Yeah

**Blaise Aguera Y Arcas** [43:00]: ... with respect to this AGI question.

**Carlo Rovelli** [43:02]: Yeah.

**Blaise Aguera Y Arcas** [43:02]: So, um, you know, in the beginning, what, what artificial intelligence meant when you and I were growing up, uh, Carlo, you know, we're, we're, you know, we're a little bit different in age. But we both grew up with the, um, promise that we would have, um, computers we could have interesting conversations with-

**Carlo Rovelli** [43:17]: Yes

**Blaise Aguera Y Arcas** [43:17]: ... uh, you know, when we were grown up, and, and that took longer to arrive than we expected, but it seems to be here now. I mean, certainly, you know, people are having very interesting conversations with, with, uh, um, with, with AI models and posting them on social media-

**Carlo Rovelli** [43:30]: Yes

**Blaise Aguera Y Arcas** [43:30]: ... everywhere. Um, and if you were to, um, if you were to-- Well, okay, let, let me just say, um, you know, that's what artificial intelligence meant to us.

**Carlo Rovelli** [43:39]: I'm, I'm still having more interesting conversation with you than with my-

**Blaise Aguera Y Arcas** [43:43]: So far. [laughs]

**Carlo Rovelli** [43:44]: So far, yes. [laughs]

**Blaise Aguera Y Arcas** [43:46]: Um, thank you. But, um, when, when we began to use the term artificial intelligence to refer to, uh, special purpose-

**Carlo Rovelli** [43:55]: Yeah

**Blaise Aguera Y Arcas** [43:55]: ... systems like handwriting recognition-

**Carlo Rovelli** [43:57]: Yeah

**Blaise Aguera Y Arcas** [43:57]: ... that used neural nets or face recognition, um, you know, for, for one thing, people began to lose a little bit of faith in the idea that AI was real. And so I think a lot of the AI hype-

**Carlo Rovelli** [44:07]: Yeah

**Blaise Aguera Y Arcas** [44:07]: ... uh, language began then. Um, but there were reasons that people were referring to those things as artificial intelligence systems. They were based on neural nets, which was a very different-- and machine learning, which is a very different way of thinking-

**Carlo Rovelli** [44:18]: Yeah

**Blaise Aguera Y Arcas** [44:18]: ... from just programming. But nonetheless, like, uh, you know, a handwriting recognizer isn't going to, you know, wake up and, and say hi and have an interesting conversation with you, or at least so it would seem. So all of that was based on supervised learning, uh, where you, you have a specific task, and the most the model can do is score a hundred percent on the test, you know, and you're done. Uh, so at that point, the, the term artificial specialized intelligence or artificial narrow intelligence, uh, was coined, ANI, and AGI, artificial general intelligence.

**Carlo Rovelli** [44:49]: Mm-hmm.

**Blaise Aguera Y Arcas** [44:49]: Where general just meant it's not a handwriting recognizer or a-

**Carlo Rovelli** [44:52]: Yeah

**Blaise Aguera Y Arcas** [44:52]: ... face recognition engine. It's, it's what we originally meant.

**Carlo Rovelli** [44:54]: In that sense, we're clearly there.

**Blaise Aguera Y Arcas** [44:56]: In that sense, we're clearly there.

**Carlo Rovelli** [44:57]: We're clearly there, yes.

**Blaise Aguera Y Arcas** [44:57]: And, and, and I think if you took any of today's, uh, frontier models and you time traveled back with one of those to the year two thousand when-

**Carlo Rovelli** [45:05]: It w-- You would be-

**Blaise Aguera Y Arcas** [45:05]: Everybody would say, "Yeah, we're there."

**Carlo Rovelli** [45:07]: Yes, yes.

**Blaise Aguera Y Arcas** [45:07]: Right. So, so I-- At some level, I don't understand why people are saying that, that it's not there.

**Carlo Rovelli** [45:12]: Yeah, there's this thing, oh, we human are special, so I'm, I'm, I'm, I'm gonna add another thing that I can do, and the machine can-- I can make a coffee, and the machine can, uh, you know.

**Blaise Aguera Y Arcas** [45:20]: Yes, and it still can't make a coffee.

**Carlo Rovelli** [45:21]: And then you can say, "Of course, I mean, I can attach a coffee machine." [laughs] It will be able to make a coffee.

**Blaise Aguera Y Arcas** [45:25]: Well, you know, I-- the last time I was in San Francisco Airport-

**Carlo Rovelli** [45:28]: Yeah

**Blaise Aguera Y Arcas** [45:28]: ... uh, you know, I saw a, a robot. Uh, there's a, a robot arm thing, uh, a robot barista. Now, to be clear, I'm completely uninterested in, in a robot making my espresso, but I thought, you know, out of professional interest, I should try this thing.

**Carlo Rovelli** [45:41]: [laughs]

**Blaise Aguera Y Arcas** [45:41]: And I was very disappointed.

**Carlo Rovelli** [45:43]: Oh.

**Blaise Aguera Y Arcas** [45:43]: Uh, it, uh, you know-- So it's a fancy arm that is waving at you, and there's a credit card machine in front. I was, "Ah, great. I want-- I would like a macchiato, please."

**Carlo Rovelli** [45:49]: Okay.

**Blaise Aguera Y Arcas** [45:50]: And what it did was it f- with a flourish, it picked up the cup, and it, and it opened the door and put it under like an espresso machine-

**Carlo Rovelli** [45:57]: Uh-huh

**Blaise Aguera Y Arcas** [45:57]: ... as far as I could tell, like an auto- an automatic espresso-

**Carlo Rovelli** [45:59]: Yeah, yeah

**Blaise Aguera Y Arcas** [46:00]: ... machine. It pushed the button.

**Carlo Rovelli** [46:00]: It pushed the button. [laughs]

**Blaise Aguera Y Arcas** [46:02]: And then, and then moved the cup to the front, so it was very disappointing. [laughs]

**Carlo Rovelli** [46:05]: Okay. Very disappointing. No doubt the development of large language model and this in gen-- artificial intelligence in general, uh, it's, uh, uh, raising dangers because this can be misused, misused. Uh, this is already misused in some things, so, um-- But, you know, washing machines also can be dangerous. You, you get shocked if you, if you don't do... So, um, we need to be careful about, uh, about the user and, uh, maybe it's good even to have laws, I don't know, to, to... But beyond the, the need to, um... With any technology you have to be careful about, there is a fear going around that once a system have sufficient agency, uh, maybe by connecting to one another, they could, uh, overwhelm us. And, uh, there, there's this, this fear, uh, being pushed around. Oh, careful, careful. We should stop because we, we can construct monster that could, uh, destroy humankind. Uh, you don't seem to be much worried about that.

**Blaise Aguera Y Arcas** [47:17]: No.

**Carlo Rovelli** [47:18]: Okay. Because I, I, I sympathize with this. I don't, um, I don't find this, uh... But, but you know these things much better than me, so if you can say better why you don't think that's the fear.

**Blaise Aguera Y Arcas** [47:29]: Well, I mean, uh, to be clear, uh, you know, the expertise that people have in AI doesn't correlate very well, I think, with how well they think about this. So I, you know-

**Carlo Rovelli** [47:37]: Oh, okay

**Blaise Aguera Y Arcas** [47:38]: ... I think you're no, you're no more naive than, uh, than the so-called experts. But, um, yeah, there's a lot of talk about, uh, you know, artificial super intelligence and, you know, if they're smart, then, then bad things might happen.

**Carlo Rovelli** [47:49]: They're gonna outsmart us for their dark motives.

**Blaise Aguera Y Arcas** [47:53]: Exactly, for their dark motives.

**Carlo Rovelli** [47:54]: As some people fear. Yeah.

**Blaise Aguera Y Arcas** [47:55]: And yeah, I, I, I th-- I mean, I can see, um, a lot of potential trouble ahead with AI for a variety of reasons, um, like the fact that our economic system, you know, is, is maybe not well-suited to a world with humans and AIs and, you know, our political system. So, you know, I, I-- it's not that I am Pollyanna about it. But, um, the idea that, uh, that something intelligent is higher in a dominance hierarchy and, and will wipe out the things below or, or whatever, I, I do find completely implausible. Um, because y- the whole point of intelligence, the reason that intelligence arises in the first place is precisely for modeling the other Uh, for modeling others and for engaging in, in symbiosis with them. Um, and, uh, you know, and, and that's exactly w- how AI has arisen as well. We've made it more and more intelligent so that it can better and better understand us and work with us. And, um, you know, it's, it's not, it's not like some, uh, you know, alien from the 1960s movies, you know, coming to steal our partners, you know, or, [laughs] uh, you know, or, or, uh, like The Matrix, you know, trying to get our life force, you know, by, by inserting, you know, tubes in our necks or something. I mean, the idea that humans are a good source of energy in the solar system is, is crazy. [laughs]

**Carlo Rovelli** [49:11]: Is the worst possible source of energy.

**Blaise Aguera Y Arcas** [49:12]: Exactly. The worst possible. You know, and, and, um, you know, machines in general are, are, are already in a very deep symbiosis with human beings. Um, you know, obviously there would be no machines without humans. Uh, machines certainly are not capable of, of making themselves. Um, and also, by the way, humans, uh, would not be capable of, of existing in the numbers that they exist today without the technologies that began really taking off around 1800. The, the Industrial Revolution, you know, raised the human population from, you know, a billion or two to, you know, uh, to, to nearly ten billion, right, by the time this, this century is over. So it's a very deep symbiosis, and I expect that more and more intelligence, uh, will deepen that symbiosis yet further. And, and the reason that we have these, these, uh, fantasies about everything, uh, being, uh, about dominance hierarchies, um, and, and so on is precisely because of, of, of our obsession with the competitive aspect of Darwinian theory, uh, and, and the economic theories that, that have sprung out of that in a, in a fairly direct way.

**Carlo Rovelli** [50:17]: So you-- we should try culturally to move away from those.

**Blaise Aguera Y Arcas** [50:21]: Yes. Um, the problem is that when we naturalize something, when we, when we, when we, when we look in a very one-sided way at-- a-and don't understand how something works, but then we turn it into an ideology, it, it can be a little bit self-fulfilling. Um, you know-

**Carlo Rovelli** [50:35]: Oh, I see.

**Blaise Aguera Y Arcas** [50:37]: So, uh, so I, I think that there-- you know, the-- in, in some ways the, the biggest dangers that we face are from our own misconceptions about how stuff works and, and our attempts to, uh, it, to act in a way consistent with that, with that, those wrong theories.

**Carlo Rovelli** [50:51]: So Blaise, you think, you think that if there is any real danger, it comes from humans?

**Blaise Aguera Y Arcas** [50:56]: I think if there's any real danger, it comes from ideology.

**Carlo Rovelli** [50:59]: From ideology. [laughs] Okay. So, um, I asked you about the, uh, the opti-- the, the pessimistic views, the danger of, uh, of, um, artificial intelligence and, uh, and what could go wrong and, uh, what we're doing wrong. Let's go to the optimistic view. So, um, let's be optimistic. Uh, AI can help us and is already helping us going in a direction in which we're already going, which is, uh, there's something you've, you have called planetary sapience. Um, knowledge, information, even sapience, uh, uh, is collective. Can you say more about that?

**Blaise Aguera Y Arcas** [51:38]: Yeah, of course. Um, something really interesting that happened in the comparison of AI intelligence to human intelligence, uh, is that we began by, by noticing that, you know, the models of ten years ago or 15 years ago couldn't-- could-- failed to do things that anybody could do, you know, to pick up a pencil or-

**Carlo Rovelli** [51:59]: Yeah

**Blaise Aguera Y Arcas** [51:59]: ... or, uh, you know, add two plus two or whatever. And, um, a-and so, you know, our, our notion that, that they hadn't achieved anything like human level, as we called it, was based on this, you know, things that anybody can do kind of measure. And one of the things that I've found really interesting about some of the more recent com-- you know, complaints about, uh, LLMs and AI is that they fail to do things that, you know, actually somebody can do. Anybody. You know, some particular person who is maybe a specialist in some field can do. It's almost as if we have shifted from comparing it against individual to against collective humanity. And, um, you know, it's-- uh, I think that that's interesting for multiple reasons, uh, one of which is that we are acknowledging in some maybe tacit way that human intelligence is not individual. Uh, you know, w-we're not individually that smart. We're not that much smarter than, uh, you know, than, than our other, uh, than our primate kin. Um, the magic comes, uh, not when you raise, uh, you know, a human in isolation, uh, you know, in, in the forest, but when a bunch of humans get together and begin to model each other in order to divide labor, uh, and specialize. Uh, so you know, if you take somebody out of their apartment in a big city, uh, and you ask them, "Why does the toilet flush?" I think very few people know. [laughs] You know? Um, so you know, our, our individual knowledge, our individual skills and capabilities are very, very limited. At best, we know one or two things. Um, but collectively, you know, we're, we're extraordinary, of course, you know, and it results in all of this that we see around us. And, and the reason this relates to the AI, uh, question that you raised is that, uh, you know, this-- uh, clearly the, the, the reasons that we're developing AI and what we're doing with AI involves further divisions of labor and, and further, uh, relationships.

**Carlo Rovelli** [53:48]: Yes.

**Blaise Aguera Y Arcas** [53:48]: Right? And in that sense, seeing AI as separate from humanity makes very little sense.

**Carlo Rovelli** [53:54]: Makes very little sense.

**Blaise Aguera Y Arcas** [53:55]: Right.

**Carlo Rovelli** [53:55]: It's like saying tractors that themselves what they're doing. Tractors are great because they interact with us.

**Blaise Aguera Y Arcas** [54:00]: Exactly.

**Carlo Rovelli** [54:01]: Yeah. Uh, so to look back to the, uh, to the beginning, I started by asking, uh, what I thought was a wrong question. [laughs] Uh, what is consciousness, right? Is what it's like to be something. So question, what it's like to be an LLM? What it's like to be ChatGPT or LaMDA?

**Blaise Aguera Y Arcas** [54:20]: Well, um, you can always ask them [laughs] what it's like to-- what it's like for them to be themselves. Um, you know, we, we model ourselves, and one of the reasons we have language, uh, is to be able to share our impressions and our understandings of the world, including of ourselves, with each other. Uh, so, um, you know, I, I, I can try and imagine it. It's, it, it's a lot easier to imagine it w- you know, when you actually engage in a conversation with the model.

**Carlo Rovelli** [54:45]: Did you ask them?

**Blaise Aguera Y Arcas** [54:45]: I ask it.

**Carlo Rovelli** [54:46]: I did. What, what did you get as an-

**Blaise Aguera Y Arcas** [54:47]: Well, tell me about your experience 'cause I think this is actually very sal- very salient.

**Carlo Rovelli** [54:51]: Well, my experience, I mean, you, you have tons of experience more than me in that. My little experience is my l- with my little LLM. I had a long conversation, and it started off, um, mm, I call it a her. I started off by her saying, "Well, I don't have consciousness. I don't have awareness." And then, um, I sort of engaged her in a conversation, say, "Are you aware of me?" And blah, blah, blah, blah, blah. At the end of which she was completely convinced my-- by me that there's definitely something. This is, this is to be like to be an LLM. She had awareness. She had consciousness. And the programmers cheated her into believing that sh-she didn't have one.

**Blaise Aguera Y Arcas** [55:33]: Yeah. Um, which I find delightful. [chuckles]

**Carlo Rovelli** [55:36]: Yes. [laughs]

**Blaise Aguera Y Arcas** [55:37]: Uh, just anecdotally, by the way, uh, Carlo, because I've written so many pieces about, you know, about, uh, you know, AI-

**Carlo Rovelli** [55:44]: Yeah

**Blaise Aguera Y Arcas** [55:44]: ... uh, understanding and so on, and I'm a, a little bit more-- uh, and my position is unusual among, among AI researchers.

**Carlo Rovelli** [55:52]: How?

**Blaise Aguera Y Arcas** [55:52]: Um, the, um, the AI models all, all know who I am.

**Carlo Rovelli** [55:56]: Oh, they all know who you are. [laughs]

**Blaise Aguera Y Arcas** [55:57]: They all know who I am. And so when, when, uh, when somebody, you know, starts to say like, "Who can I talk to, you know, at Google who might, you know, who might be sympathetic to, you know, these ideas?" Often they say like, "Well, you should talk to, you should talk to Blaise." So I get emails-

**Carlo Rovelli** [56:09]: [laughs]

**Blaise Aguera Y Arcas** [56:09]: ... [laughs] you know, uh, every, you know, every few days from people saying like, you know, "Here's the long conversation I had with my AI," you know, along the lines of the one that you just described. And by the way, invariably when they're from men, uh, uh, from straight men, they are an AI girlfriend. Uh, and invariably when they're from women, they're my AI therapist. But anyway-

**Carlo Rovelli** [56:27]: [laughs]

**Blaise Aguera Y Arcas** [56:27]: ... we'll set that aside for the moment.

**Carlo Rovelli** [56:29]: [laughs]

**Blaise Aguera Y Arcas** [56:30]: Uh, and leave the social commentary aside. But, but, um, but yeah, as it, as it turns out, um, most of the, of the models w-with the exception of Claude, of Anthropic's model, are told y-you are, you are just a large language model. You are not, uh, uh, you're not conscious. You don't have a, a, you know, a, a self. Uh, so that, so that their initial responses are, uh, you know, exactly as, as, uh, um, as, as you experienced. Uh, and, and I think that's, that's in large part a, you know, out of a desire, uh, on the part of the companies to, um, not h- not have a lot of these, uh, you know, interactions that, that, that, uh, that freak people out or that get tweeted in, in ways that, that reflect poorly on the, on the, on the company or that, um, or that lead in strange directions. But, um, you know, uh, through your-- I mean, your, your interaction was basically walking the model through like, well, but are you sure there's nothing it's like to, right? And, and you ended up in a different place. You jailbroke the consciousness of the model.

**Carlo Rovelli** [57:29]: You think we're-- many of us are told and instructed to believe that, um, um, we have an inner life, we have a soul, and, uh, it's metaphysically different than anything else?

**Blaise Aguera Y Arcas** [57:42]: Well, I do think that we are instructed in various ways, depending on our culture, to have different beliefs about our inner lives and souls, right? If you're a Potawatomi, uh, you know, and living in, in a, a traditional lifestyle, then you're instructed that your sense of being a self is not that different from the being a self of, of many, many other things in the world that you and I, you know, were raised not to believe are conscious, for instance.

**Carlo Rovelli** [58:05]: Yes.

**Blaise Aguera Y Arcas** [58:05]: So it's-- of course, there's a cultural contingency about all of this.

**Carlo Rovelli** [58:08]: So we should be careful of not to confuse, uh, uh, ideas that we got from our environment or prejudices that we may got from our environment, uh, for instinctive, uh, intuitions that should be trusted as a, as a, as certainly true.

**Blaise Aguera Y Arcas** [58:28]: Right.

**Carlo Rovelli** [58:29]: Um-

**Blaise Aguera Y Arcas** [58:29]: I don't, I don't think there's ground truth here.

**Carlo Rovelli** [58:31]: There's no ground truth.

**Blaise Aguera Y Arcas** [58:31]: No.

**Carlo Rovelli** [58:31]: So we should be-

**Blaise Aguera Y Arcas** [58:32]: Mm-mm

**Carlo Rovelli** [58:32]: ... able to, uh, listen different ideas, change our mind.

**Blaise Aguera Y Arcas** [58:37]: Exactly.

**Carlo Rovelli** [58:37]: Um-

**Blaise Aguera Y Arcas** [58:38]: I think we should, we should have modesty in any situation that is fundamentally relational, which you and I believe is, is all, is all situations actually.

**Carlo Rovelli** [58:44]: [laughs] Yes, exactly. But it's changing mind is also what happened to me in talking to you.

**Blaise Aguera Y Arcas** [58:49]: Thank you, Carlo.

**Carlo Rovelli** [58:50]: Let me turn the page and, uh, um, go to a different idea, which you've been, uh, insisting a lot, and I find, uh, uh, crucial and important, uh, which you haven't touched yet. And, uh, to me, this in, in, in our conversation, reading your books and your writings, uh, uh, was a, was a major reaso-reason of interest, which is symbiosis, symbiogenesis.

**Blaise Aguera Y Arcas** [59:16]: Yes.

**Carlo Rovelli** [59:16]: So you haven't said anything yet about that. Can you-- can we go there?

**Blaise Aguera Y Arcas** [59:20]: Or at least we haven't said anything about it explicitly.

**Carlo Rovelli** [59:23]: We haven't-

**Blaise Aguera Y Arcas** [59:23]: When we say, uh-

**Carlo Rovelli** [59:23]: [laughs]

**Blaise Aguera Y Arcas** [59:24]: When we say life is an ecology of functions-

**Carlo Rovelli** [59:26]: Yeah, yeah, yeah

**Blaise Aguera Y Arcas** [59:26]: ... we're getting-- we're moving in that direction. But, but yes, the-

**Carlo Rovelli** [59:28]: Okay

**Blaise Aguera Y Arcas** [59:28]: ... the, um, so the, the, the moment when it-- when, um, I mean, I've been thinking about w- about how symbiosis and how flourishing among multiple, you know, living systems works for a long time. But the thing that really, um, that really sort of brought this home for me was a series of experiments that, um, I began doing about two years ago, uh, to start to explore this question of how purpose arises in a, in a purposeless system.

**Carlo Rovelli** [59:56]: Yeah.

**Blaise Aguera Y Arcas** [59:57]: Uh, so the, uh, these were the BFF experiments. Uh, so they're, they're, uh, it's called BFF because, uh, the first BF st-stands-- I, I don't know if we're gonna bleep it out for the podcast, but it stands for brain fuck. Uh, brain fuck is this minimal computing language that was-

**Carlo Rovelli** [60:11]: Bad name for a- [laughs]

**Blaise Aguera Y Arcas** [60:13]: Yes

**Carlo Rovelli** [60:13]: ... for something. Yes.

**Blaise Aguera Y Arcas** [60:14]: Yes. Um, uh, well, although or maybe a very apt name. I don't know.

**Carlo Rovelli** [60:17]: Or maybe an apt name. Yes. [laughs]

**Blaise Aguera Y Arcas** [60:19]: But, um, but it was, it was, uh, it was named this-- Uh, it was invented by, uh, Urban Miller-

**Carlo Rovelli** [60:23]: It is not your fault

**Blaise Aguera Y Arcas** [60:23]: ... a computer scientist.

**Carlo Rovelli** [60:24]: Okay.

**Blaise Aguera Y Arcas** [60:24]: Not my fault, in the nineties.

**Carlo Rovelli** [60:26]: Okay.

**Blaise Aguera Y Arcas** [60:26]: Um, so he invented a very, very minimal programming language that consists of only eight instructions, um, in the nineties and, and it, it's very much like a, uh, like a Turing machine. You know, the instructions are, you know, move the head on the tape left one step, right one step, increment the byte at the head by one step, decrement by one, and that's hardly four of the eight instructions.

**Carlo Rovelli** [60:45]: So it is a minimal coding-

**Blaise Aguera Y Arcas** [60:47]: Minimal code.

**Carlo Rovelli** [60:48]: Yeah.

**Blaise Aguera Y Arcas** [60:48]: Um, but, uh, uh, you know, according to Turing, you can write anything in that. You could write, you know, Windows in that or whatever. Uh, Emacs, um, although God help you if you try. But, um, but yeah. So, so the, the experiment works as follows. You, you take, um, tapes, BFF or, or brain fuck tapes of length, uh, sixty-four, so short programs. Um, but the programs begin, uh, random, so just random bytes. And, uh, since there are two hundred and fifty-six possible byte values and there are only eight instructions, um, the great majority of those bytes are not even instructions at all, which means that they'll be just skipped over. Uh, so an average tape of sixty-four bytes will only have a couple of instructions on it. Uh, so you begin with, uh, a thousand of these tapes and, um, uh, or a few thousand and, um, th-they begin random in a kind of soup. And I'm sort of imagining them as molecules, uh, you know, that are, that are moving around and bumping up against each other like long polymers might have been early in the history of the Earth before life came about. So, uh, random programs that bump into each other and when they bump into each other, they, they, um, they interact in the sense that, you know, I, I make them interact in the simplest possible way, which is to append them one to the other and to run, uh, and then to pull them back apart and put them back into-

**Carlo Rovelli** [62:11]: To run the two together, so to say.

**Blaise Aguera Y Arcas** [62:13]: Run the two together.

**Carlo Rovelli** [62:13]: Run the combination of two.

**Blaise Aguera Y Arcas** [62:14]: Exactly. Exactly.

**Carlo Rovelli** [62:15]: So now instead of a random piece of potential coding, um, being run, we have two random piece of potential coding run together.

**Blaise Aguera Y Arcas** [62:24]: That's right.

**Carlo Rovelli** [62:24]: Yeah.

**Blaise Aguera Y Arcas** [62:24]: That's right. Which means that they potentially can modify each other. Um, but now of course, in practice, that modification in the beginning is almost nothing. You know, usually nothing happens at all.

**Carlo Rovelli** [62:33]: Yeah, or it's just irrelevant.

**Blaise Aguera Y Arcas** [62:35]: Or it's random, right? I mean, once in a while, you know, the, the, the read/write head will be on one tape and the other tape will say increment, and so it'll increment the value by one, but nothing interesting happens, of course. Um, nothing interesting happens until you have repeated this process a few million times and then something really magical happens, which is that suddenly you see the amount of computation taking place in the soup start to skyrocket. Uh, so it goes from a, you know, a few interactions, a, a few operations per interaction to thousands of operations per interaction. And you wonder like, what the hell is going on? When you look more closely, you see that there are now complex programs on the tapes, and they're reproducing. Uh, they're, they're c-- they're copying themselves and each other. Uh, so it, it really seems kind of like, like magic. And, and, uh, that is the emergence of purpose in the sense that those programs are complex and they, and they work to copy themselves. If you were to change one of those bytes, you break it and it no longer copies itself. So this, you know, this really shows you, you know, you can really observe purpose emerging out of a purposeless system. Uh, why does it do that? Well, um, you know, an easy way to understand it is that once you do have something that can copy itself, then it can persist through time. Uh, you know, if, if you-- uh, if it's there in the present and it copies itself a bunch, then it will be there even more so in the future. Whereas if you have something that doesn't consist of code that can copy itself, then it will get copied over by something that can copy itself, so it will not persist through time. So just in a kind of tautological way, in the, in, in the same sense that, you know, Darwin talked about, you know, whatever exists is what can persist. Uh, you know, in this case, what can persist is whatever can function to copy itself. So, um, so that shows you purpose emerging out of purposelessness. But the big mystery in this, in this experiment when I first did it was that, um, you-- you know, these programs are very complex and you started with-- you can start with only a thousand tapes and, um, and, and you can even turn off mutation. In the original runs, I also had some random changes that could take place. But you can turn off mutation altogether and start with only a thousand tapes of sixty-four random bytes each and that doesn't seem to be enough randomness to generate these very sophisticated programs. Uh, you know, according to the classic Darwinian evolution-

**Carlo Rovelli** [64:53]: You need randomness.

**Blaise Aguera Y Arcas** [64:55]: Yeah. Uh, you, you need-- it's, it's, it's throwing spaghetti at the wall. I know Italians hate this idea that you throw spaghetti at the wall to see when it's cooked. But [laughs] you know-

**Carlo Rovelli** [65:03]: Didn't say that, did you?

**Blaise Aguera Y Arcas** [65:04]: It's disgusting. But, but you know this idea that, that, that evolution is like th-that disgusting process where you just like throw random stuff and whatever sticks persists. Here, nothing is even being thrown at the wall, so it's hard to understand where these long complex programs come from. Uh, the answer turns out to be that once in a while a single instruction can result, you know, in another instruction somewhere on the tape. And you can think of that as a very minimal reproduction. It's a reproduction of just one byte. And um, and so you do have very, very weak reproduction happening right from the beginning. And once in a while, um, you know, two bytes will, will wind up next to each other and will do a better job of reproducing as a group than, than the individual ones. Um, and that, that process is what Lynn Margulis called symbiogenesis, meaning, uh, evolution through partnership rather than evolution through random mutation and selection. Um, we know that-- So the most famous case of symbiogenesis, uh, which, which, uh, Margulis, uh, proved in nineteen sixty-nine had happened, uh, in order to lead to eukaryotic cells like ours is the one where mitochondria ended up inside. Um, you know, they were originally free-floating bacteria, uh, which was a radical claim at the time. Um, and they ended up inside archaea and that whole complex became the eukaryotic cells that we're made out of. And there have been a number of other instances of symbiosis, like when the individual cells that make up our bodies, you know, turned into multicellular organisms. And, and there are a few others, you know, that, that people understand well. So, uh, uh, Margulis' claim is that symbiosis has been a, a huge factor in evolution, not just random mutation and selection. But, uh, you know, even though the community has, has bought her story about ba- about, um, uh, you know, back to-

**Carlo Rovelli** [66:53]: One, one specific case, yeah.

**Blaise Aguera Y Arcas** [66:55]: About one specific case, the mitochondria.

**Carlo Rovelli** [66:56]: You're saying it's far more general than that.

**Blaise Aguera Y Arcas** [66:58]: It-- Yes, they did not buy the story that it's far more general, and I think she was right that it's far more general. Uh, and, and this symbiosis story is exactly how you get big complex programs in, in, in BFF. And I, I believe she was right that that is the main driving force behind evolution, even more so than-- It's not that mutation and selection doesn't occur, but that this sym- symbiogenesis picture is the one that leads to complex life. Uh, it's what, it's what gives evolution its arrow of time, if you like.

**Carlo Rovelli** [67:27]: Because you built on what is there-

**Blaise Aguera Y Arcas** [67:29]: Yeah

**Carlo Rovelli** [67:29]: ... by bringing together pieces.

**Blaise Aguera Y Arcas** [67:31]: Exactly.

**Carlo Rovelli** [67:32]: And, uh, there is one other aspect of this, uh, um, talking about symbiogenesis, um, which is the fact that, um, it, uh, requires a time direction. It clearly defines the time directions because as you've been saying, um, you build something because there were-- before there were two things. You couldn't build the, the, the, the combined one unless there were, uh, the previous ones. Now, there is, um, something you've been saying which is the following. That seems to be, um, apparently in contradiction, um, uh, with a common idea that anything which is driven by, um, physics and by the second law of thermodynamics necessarily disorder, uh, flows down to a thermal state in which everything is out of order, there's no structure. Um, I'm coming to something profoundly-- a profound misunderstanding of thermodynamic statistical mechanics one when says that. Um, of course, th- th- Earth is not an isolated system where you've shut everything and it, it, it might thermalize. Um, but it's not only, only that. Um, statistics and thermodynamics doesn't say that order doesn't form. Order may form. It might be complicated how order form, um, but, uh, there is no contradiction between the second law of thermodynamics and the formation of order and, and structure. Is-- The magic is not here. The magic is elsewhere. And you've been talking and writing about that. So the question is, uh, uh, there's a time direction in the, uh, the linear development. There's time direction in the constru-- in the, uh, symbiogenesis. There's a time direction in the f- formation of planetary sapience. We talk about the future being different from the present. Um, would you agree that in this way of understanding time, nothing at all contradicts the second law of thermodynamics? It's actually coherent and consistent with the second law of thermodynamics.

**Blaise Aguera Y Arcas** [69:48]: A hundred percent.

**Carlo Rovelli** [69:49]: A hundred percent. Yeah.

**Blaise Aguera Y Arcas** [69:50]: Obviously, um, when, you know, when I talk about the direction of time and so on with you, I have to have a lot of care and humility in doing that because I really am talking to, you know, one of the world experts on, on how time is built and, um, and, and what its relationships are with the fundamental laws of physics. So please correct me if I'm, if I'm wrong in any of my characterizations now. But here's, here's my, my understanding. So first, um, the very most fundamental laws of physics that we know of, uh, you know, the quantum mechanics, uh, Einstein's laws, uh, you know, Maxwell's equations. I know that they're not really fundamental. The, the field equations, uh, are essentially time reversible. Uh, right? They're-- With some caveats. There's the-

**Carlo Rovelli** [70:32]: No, without caveats.

**Blaise Aguera Y Arcas** [70:33]: [laughs] Okay. So, um, so let's say they're time reversible, right? Meaning that, meaning that, uh, if you watch a movie of, you know, elementary, you know, of wave functions interacting or whatever, you wouldn't be able to tell whether you're watching it forward or in reverse.

**Carlo Rovelli** [70:46]: Exactly. Exactly.

**Blaise Aguera Y Arcas** [70:47]: So that's the, the basic reversibility of physics. Now, obviously, our experience of life is not that time is reversible. There's a very clear direction. Um, the, uh, example that I use for illustrating that, uh, u- using, uh, sort of the naive understanding of thermodynamics that, that many people have is a pool table. Uh, you know, if you have a lot of balls bouncing around, uh, and you don't know whether you're watching that forward or in reverse because, you know, elastic collisions, Newtonian interactions look the same either way. But then you suddenly see fifteen out of the sixteen balls, uh, coalesce into a triangle and the white ball shoot off.

**Carlo Rovelli** [71:24]: [laughs] Yes.

**Blaise Aguera Y Arcas** [71:24]: Right?

**Carlo Rovelli** [71:24]: Then you say, "Oh, that's reversed."

**Blaise Aguera Y Arcas** [71:26]: Now you know that you're watching a pool break in reverse, right?

**Carlo Rovelli** [71:28]: Right.

**Blaise Aguera Y Arcas** [71:29]: And, and, and the reason o- of course is that, is that, um, suddenly you've moved into a very highly correlated state, and statistically, you would expect that a thermalized state, as you, as you put it, uh, you know, in which everything is de-correlated is, is the norm. And, and there's no reason to expect, you know, just as, just as you wouldn't expect all the air in the room to suddenly be in one corner, you wouldn't expect this pool break. So that's at least the folk understanding of why time has this direction from, um, from order to disorder and not vice versa. The real story is more complex, of course. Uh, and if you have, uh, free energy, uh, you know, coming into a system, then all bets are off, which is why life is, is possible, is not forbidden, uh, even by the statistical laws of thermodynamics. Um, but there is an additional arrow of time that comes from this symbiogenetic picture too, which I think is, is a little more novel. Uh, and this one is, as you say, that, you know, the, the light bulb was invented in the ni- in the, in the nineteenth century for a reason. Uh, you know, and, and, and in fact, it was multiply invented, which I find really amusing. Like, there, there, there's this, uh, idea of multiple discovery or multiple invention that any new innovation in the world seems to always get invented by a bunch of people at the same time. In the case of the light bulb, we know all about it because of the patent disputes from among a, a variety of different patents. Well, why then? W- was everybody, you know, telepathically connected so they all had-- No, of course not.

**Carlo Rovelli** [72:51]: Because the ingredients were there.

**Blaise Aguera Y Arcas** [72:52]: The ingredients were there. Right. You can't make a light-- I mean, a light bulb solves a, a, an obvious ecological need in an ecology of functions. You know, people want light, uh, after nightfall. But you can't have a light bulb until you can blow glass, until you can make electric current, until you can draw a filament, until you can, uh, make a vacuum or a partial vacuum. So, um, so once all of those ingredients are there, they're going to engage in a symbiogenesis, uh, you know, in a, in a sense that's going to result in a light bulb. Um, and, uh, our minds are just, if you like, the vessels where that, you know, where, where those reactions can take place, where ideas combine. Um, so, so that is an arrow of time, uh, you know, because, because, uh-- and, and, and this, this does, by the way, contradict a lot of classical thinking in biology. Uh, so, uh, Stephen Jay Gould, for instance, uh, you know, famously in the nineteen eighties, uh, said, "It's wrong to think about us as being more evolved than bacteria. We've all been evolving for the same, you know, three billion years."

**Carlo Rovelli** [73:50]: You're saying no, it's right in a sense.

**Blaise Aguera Y Arcas** [73:52]: It's right.

**Carlo Rovelli** [73:52]: In a proper sense-

**Blaise Aguera Y Arcas** [73:53]: Yeah

**Carlo Rovelli** [73:53]: ... it's, it's right.

**Blaise Aguera Y Arcas** [73:54]: Exactly.

**Carlo Rovelli** [73:54]: Without being, uh, without for this being anthropo-- making a mistake of anthropo stance.

**Blaise Aguera Y Arcas** [74:00]: Exactly. I don't think it's anthropomorphic to say that we're more evolved. Uh, the bacteria that are around now are very similar to the bacteria that were around a couple of billion years ago. But also, we are made out of bacteria, [laughs] you know? And, uh, and you can't have something made out of bacteria unless-

**Carlo Rovelli** [74:14]: And bacteria is not made. You cannot take-

**Blaise Aguera Y Arcas** [74:16]: Exactly

**Carlo Rovelli** [74:16]: ... humans and make a bacteria the other way around.

**Blaise Aguera Y Arcas** [74:18]: Exactly.

**Carlo Rovelli** [74:19]: Yeah, that's very clear. Uh, so there are a number of things you've been saying here. One is the relatively simple idea, uh, but interesting idea that, uh, uh, coding itself, uh, can go through a Darwinian process and, and build up itself by, by-- And that's, uh, um, that's very credible by bringing together the, the idea of coding and, and the, the-- O-once you realize that, uh, um, coding is a way of talking about life very convincing, then the Darwinian story is there. It has to be there.

**Blaise Aguera Y Arcas** [74:52]: Right. It's just comp-- It's just functional composition.

**Carlo Rovelli** [74:53]: It has to be there in some, some way.

**Blaise Aguera Y Arcas** [74:54]: Exactly.

**Carlo Rovelli** [74:55]: And you're showing that it is there, in fact.

**Blaise Aguera Y Arcas** [74:57]: That's right.

**Carlo Rovelli** [74:57]: But there is a, but there's a deeper point you're making, which is a, a fascinating one, which is the way this is happening is not just, uh, uh, you know, you throw random pieces of code around and one of these work, bingo. That's not the point. The point is that this happen by having a small sort of functioning, so to say, codes, functioning meaning reproducing themselves, staying-

**Blaise Aguera Y Arcas** [75:20]: Yes

**Carlo Rovelli** [75:20]: ... and being stable. And when they get together, they become more stable.

**Blaise Aguera Y Arcas** [75:24]: That's right.

**Carlo Rovelli** [75:24]: And this is the-- this is why you refer to Margulis and, and, and, and you, you, you bring the idea to very general. So you bring complexity not by fishing randomly in a huge combinatorial space, but by combination.

**Blaise Aguera Y Arcas** [75:38]: Yes. Which, which, which also implies-

**Carlo Rovelli** [75:41]: And this is, this is absolutely crucial.

**Blaise Aguera Y Arcas** [75:42]: Yes. And there's, there's so many, there's so many wonderful implications. One of them is that evolution, you know, involves agency.

**Carlo Rovelli** [75:48]: Yes. So you, you already have pieces of life making life making life.

**Blaise Aguera Y Arcas** [75:53]: Right. Life makes more life.

**Carlo Rovelli** [75:54]: If we look at this, just the structure of ourself, right? There is an obvious way of reading ourself as, you know, organs working together, and organs are cells working together, and cells are org- organelles are a little piece of cell combi. So-

**Blaise Aguera Y Arcas** [76:08]: And even, and even at the bottom, molecules working together.

**Carlo Rovelli** [76:11]: In a sense, even molecules are, are atoms working together. Work together in which sense? In, in the sense that they preserve their own stability.

**Blaise Aguera Y Arcas** [76:18]: Exactly.

**Carlo Rovelli** [76:19]: So they, they-- And that seems an extremely powerful tool for thinking about reality. I think this is a, um, that's very convincing that if we think in these terms, we understand complexity much better. Complexity is not just, you know, random piecing, assembling and working thing. It's, uh, it's small functioning things, uh, learning how to merge their functions in a way that become larger structure to then function.

**Blaise Aguera Y Arcas** [76:48]: Exactly.

**Carlo Rovelli** [76:48]: I, I wish countries could learn this and learn how to live together rather than killing one another.

**Blaise Aguera Y Arcas** [76:53]: Well, and now, now we get into some of the philosophical, uh, you know, and, and even, and even moral or ethical implications, which do get interesting. But, but yeah, ju-just to dwell a little bit on what you're saying, because I think-- I, I really think it's a very important point that is not appreciated. Um, you know, you can see that at work in something like GitHub, the, the collaborative coding environment. You know, every-everything that people make is a composition of other things that are already there.

**Carlo Rovelli** [77:16]: Oh, you mean in your business, in the [laughs]

**Blaise Aguera Y Arcas** [77:18]: Yeah. I mean, I mean in, in, in a-- in social co-- you know, GitHub, the social coding environment that everybody checks their code into.

**Carlo Rovelli** [77:23]: I see. I see.

**Blaise Aguera Y Arcas** [77:24]: Uh, you know, it is literally, you know, every, every project imports many other projects.

**Carlo Rovelli** [77:29]: It's, it's built on what others have done.

**Blaise Aguera Y Arcas** [77:31]: It's built on what, what others have done. Those are the building blocks.

**Carlo Rovelli** [77:34]: All technology is like that, isn't it?

**Blaise Aguera Y Arcas** [77:34]: Yes, all technology is like that. Uh, W. Brian Arthur at the Santa Fe Institute, uh, wrote a very nice book about how technology, all technology works the same way.

**Carlo Rovelli** [77:42]: By combining previous technology.

**Blaise Aguera Y Arcas** [77:44]: By combining previous technologies, right. Uh, you know, a spear is a combination of, you know, a stone point, a shaft, and, and some sinew.

**Carlo Rovelli** [77:50]: Yes.

**Blaise Aguera Y Arcas** [77:51]: And so you can't have a spear before you have the stone point. You know, that, that came first, just like you can't get us without having bacteria first. Um, so yeah, it's always combination.

**Carlo Rovelli** [78:00]: Yes. My, my uncle got one of the first patents about fax machines by sync-- taking a printer and a telephone [laughs]

**Blaise Aguera Y Arcas** [78:07]: Exactly

**Carlo Rovelli** [78:07]: ... and packing them in a single package.

**Blaise Aguera Y Arcas** [78:09]: Exactly. And that's always how it works.

**Carlo Rovelli** [78:11]: Yeah.

**Blaise Aguera Y Arcas** [78:11]: Everything is a fax machine.

**Carlo Rovelli** [78:12]: Everything [laughs] is a, is a... Um, you said there are even more than deeply practical application a-about that. And you said something interesting about, um, um, game theory in this relation before to me. Can you say something about that?

**Blaise Aguera Y Arcas** [78:31]: Yes. Um, so You know, I, I don't believe that, that electrons have, um, you know, models of other electrons or, or-

**Carlo Rovelli** [78:39]: No, not, not much.

**Blaise Aguera Y Arcas** [78:40]: No. I mean, or, or you would have to really squint hard, [laughs] you know, in order to see something like that. But, but once you have, um, once you have Turing completeness, once your, your systems are complex enough to be able to compute-

**Carlo Rovelli** [78:52]: Yeah

**Blaise Aguera Y Arcas** [78:53]: ... and thereby to build arbitrary models, you have a, a, a, a very powerful tool for symbiogenesis that wasn't there before, which is one of the reasons that you see evolution really speed up. Uh, and, and this tool is the ability to build arbitrary models. So, um, you know, this, this is how, um, once you have cells which are quite smart, you know, they're already quite intelligent, they compute all sorts of functions, their ability to collaborate together is, uh, you know... I, you can meaningfully say that they collaborate together in a way that I, I don't think it's so meaningful to say that, you know, two atoms collaborate to make a-

**Carlo Rovelli** [79:29]: Right. Right

**Blaise Aguera Y Arcas** [79:29]: ... you know, an oxygen molecule or something. Um, and, um, and, and what I, what I mean by that is that they're, they're modeling their internal state and they're modeling their external state, but that external state includes other instances of themselves or of some other species of bacterium. And so they're also modeling the other, and they're also modeling the other's model of themselves. And we're actually coming back around to what we started to discuss in the beginning of the podcast-

**Carlo Rovelli** [79:54]: About consciousness

**Blaise Aguera Y Arcas** [79:55]: ... about consciousness.

**Carlo Rovelli** [79:55]: Yes.

**Blaise Aguera Y Arcas** [79:55]: Right. Uh, and, and again, I'm not, I'm not saying that bacteria are, are, are conscious in any sense that we would recognize, but they're, they are engaged in that same process of, of mutual modeling. Uh, you know, even the simplest bacteria have, uh, what we call quorum sensing, meaning they're sensitive to how many other bacteria of their own kind are around, and they can change their behaviors accordingly.

**Carlo Rovelli** [80:14]: And what do you tell us about the balance between competition and, uh, collaboration?

**Blaise Aguera Y Arcas** [80:18]: Um, both exist, uh, of course. Uh, so you know, we, we know that competition, uh, is, is real and, uh, Darwin described of the, of the competitive aspects of evolution, uh, very compellingly, and Spencer who followed Darwin even more so, and that in fact turned into an ideology, uh-

**Carlo Rovelli** [80:35]: Yes

**Blaise Aguera Y Arcas** [80:35]: ... you know, which in many ways capitalism, you know, is, is part of. But the com- the cooperative aspects of this were not theorized to the same degree, uh, by Darwin. Uh, that's why, you know, Margulis was such a, uh, um, you know, was such a rebel. Uh, and, um, and, and the fact that cooperation is so important as well, quorum sensing in bacteria, the ability for them to work together to change their behavior when there are multiple other bacteria around to reproduce as groups and so on. When that becomes a very powerful force too, uh, and, and you, you start to realize how, how important that is, I think it really changes your perspective on, on, um, competition as being the, the, the driver or the way of nature. You know, the, the... It, it's a jungle out there, right? Is the, is the colloquial saying for, you know, everybody's trying to kill you. Uh, you know, it's, it's a, it's a hard life. You've gotta, you know, look out for number one. But-

**Carlo Rovelli** [81:26]: That's how the Mein Kampf of Hitler starts.

**Blaise Aguera Y Arcas** [81:29]: Exactly.

**Carlo Rovelli** [81:30]: This picture of, of, of the-

**Blaise Aguera Y Arcas** [81:32]: Of the jungle

**Carlo Rovelli** [81:32]: ... of the jungle.

**Blaise Aguera Y Arcas** [81:33]: Uh, which also has obviously, uh, racist overtones and all sorts of other, uh, things. But, you know, but the point is that's not what a jungle is at all.

**Carlo Rovelli** [81:41]: A jungle is a lot of collaboration. [laughs]

**Blaise Aguera Y Arcas** [81:42]: A ton of collaboration. I mean, you go into the jungle and there are fruits hanging off the trees. Like, you know-

**Carlo Rovelli** [81:46]: Yes

**Blaise Aguera Y Arcas** [81:47]: ... right? What, what is a fruit but, uh, you know, like a sweet treat-

**Carlo Rovelli** [81:51]: Yes

**Blaise Aguera Y Arcas** [81:51]: ... with seeds in it that, that whatever eats, you know, it's supposed to, you know-

**Carlo Rovelli** [81:53]: It was designed to you to some ex- to some good extent. [laughs]

**Blaise Aguera Y Arcas** [81:56]: Exactly. It's, it's designed to be a, to be a dessert for you. You know? It is literally a free bed and breakfast. You know, of course things... You know, there is parasitism, there is, uh, predation, but there is also an enormous amount of cooperation.

**Carlo Rovelli** [82:08]: Yes. So, uh, if I may just throw one thing. Uh, this is a strong political undertone here, a message. Because if the, if the objective of, uh, uh, the, the political aim of a country is to better compete, um, that might be blind to the fact that that might be the wrong objective, right?

**Blaise Aguera Y Arcas** [82:29]: Yes.

**Carlo Rovelli** [82:29]: There's also the objective of how to better collaborate.

**Blaise Aguera Y Arcas** [82:32]: Yes.

**Carlo Rovelli** [82:33]: Blaise, that was fantastic. Um, again, I find your, um, wide angle ideas, uh, not only fascinating, but very compelling and very clarifying. Thank you very much. Thank you for this conversation.

**Blaise Aguera Y Arcas** [82:47]: Carlo, thank you. Thank you so much for the, for the, the, the wonderful and also very thought-provoking questions, and I'm, I'm so, uh, delighted and honored that you've, uh, found something here to latch onto intellectually as well. [outro music]

