---
title: "Identity and Collective Intelligence"
person: blaise-aguera-y-arcas
section: by
type: talk-transcript
year: 2023
venue: ""
source_url: https://open.spotify.com/episode/4scx2QspGNqfKA6L6nZiCp
retrieved: 2026-08-14
content: full-text
transcription:
  method: asr
  asr_model: elevenlabs-scribe_v2
  diarized: true
  speaker_labels: inferred   # ASR diarization + LLM naming (claude-sonnet-4-6); not ground truth
  duration_min: 85
notes: "PROVENANCE: machine-transcribed from AV via ElevenLabs Scribe v2 (diarized) + LLM speaker-naming pass. Speaker labels are inferred, not authoritative. Layer-2 (mildly lossy) per charter, not camera-raw."
---

# Identity and Collective Intelligence

*Speakers (inferred):* speaker_0=Host, speaker_1=Unknown, speaker_2=Unknown, speaker_3=Unknown, speaker_4=Blaise Aguera Y Arcas

## Transcript
**Host** [00:01]: This episode of the Mindscape podcast is brought to you by Progressive Insurance. Do you ever think about switching insurance companies to see if you could save some cash? Progressive makes it easy to see if you could save when you bundle your home and auto policies. Try it at progressive.com. Progressive Casualty Insurance Company and affiliates. Potential savings will vary. Not available in all states.

**Unknown** [00:23]: Migraine makes me miss out on the moments that matter. So I asked my doctor about saying yep to Vyep-D, eptinezumab JJMR, an IV infusion given every three months that helps prevent migraine attacks in adults.

**Unknown** [00:37]: Don't take if allergic to Vyep-D. Get help right away for allergic reactions like rash, swelling of face, lips, tongue, or throat, trouble breathing, hives, or facial redness. Tell your doctor about increased blood pressure or color changes, pain or numbness in fingers or toes. Common side effects are stuffy nose, scratchy throat, and allergic reactions.

**Unknown** [00:57]: Tap the ad to see how many migraine-free days you might reclaim and see the full prescribing information at vyepti.com.

**Unknown** [01:04]: Say yep to Vyep-D.

**Host** [01:07]: Hello, everyone, and welcome to the Mindscape podcast. I'm your host, Sean Carroll. Today's podcast has a good news, bad news situation. The bad news is there will be bad language in this podcast, not because we're getting especially salty or, um, profane or anything like that, but because we're going to be talking about computer simulations that were written and run using a language called Brainfuck. Sorry about that if you have sensitive ears, but this is a very real computer language that was given that name, Brainfuck, and so we're going to have to say the phrase Brain- Brainfuck over and over again. That's why I'm saying it right now, just to loosen you up and get you to know that this is what is going to be coming. Um, the good news is it's going to be worth it. This is a really fascinating conversation about a super important topic, which is, in some sense, the topic is the origin of life, but there's not a lot of chemistry or biology or geology or anything like that in the talk, uh, in the conversation. It's a model for the origin of life or a simulation of the origin of life done on a computer. Uh, today's guest is Blaise Aguerra y Arcas, who is a very successful computer scientist, like a real-world computer scientist. He works-- He has worked for Microsoft. He now works for Google doing things like AI, of course, but also visualization, augmented reality, questions about how machines can be creative and artistic, things like that, um, with real-world applications. But it's led him to think more broadly about what is intelligence, what is life, what is-- You know, if you're a naturalist, a physicalist, like I definitely am, and I think Blaise also is, then you think that things like life and thought are outcomes of physical things bumping into each other in particular but especially complicated ways, and then there's an emergent higher-level description of this thing that we call life. So clearly, going back to people like, um, Schrödinger and, uh, von Neumann and others, there's a statistical mechanics of this, right? You want to know in the ways, all the different ways you could organize atoms and molecules and so forth, how likely is it that you would get life? You know, there's-- And you, and you im-immediately say, well, look, of all the ways that I could take a given set of atoms or molecules and organize them, most of them don't look like living beings at all, right? Living beings are clearly a very, very organized, tiny subset in the space of all possible configurations. True, that's the old sort of quasi-creationist argument that you're not going to get life just by randomly throwing things together. In an infinitely old universe, maybe you would. That's the Boltzmann brain paradox, but our universe is not nearly old enough to make that relevant. But it's also not the right question, right? We don't just throw some molecules together randomly. Maybe we start with some semi-random configuration. It's not really random because it's low entropy, but we start with some specific configuration, and then we evolve it for a very long time. And that evolution is sort of interesting and explores this gigantically big space of possibilities. And then the much more sophisticated and important question is, do trajectories in that kind of setup have little subregions that are likely to look like life in some way? Now, the space of possibilities is so large you can't be very realistic in exploring that, but you can start with a little toy model. And so what Blaise and his, um, collaborators have done is write programs-- Not even write programs. Sorry, I shouldn't say that. They've explored, uh, a system where you have little programs written in this language Brainfuck, and there's many, many, many programs, and the programs are starting literally with random symbols, okay? Imagine if you went into your Python compiler or HTML for that matter and just typed in random symbols. It would just be a mess. Nothing would happen. But Brainfuck is so small as a computer language that sometimes things are going to happen. And what they show with their specific set of rules, which is not-- You know, they didn't cook in the answer. They let the different computer programs kind of talk to each other and, uh, rep-- and influence each other, interact with each other, and they find the spontaneous emergence of replication. That is to say, you generate-- Eventually, after sort of fumbling around randomly for a little while, you find little bits of computer programs that reproduce themselves and in some sense, which we'll talk about in the podcast, hand down their genetic information to later, um, generations. And in fact, those particular self-reproducing computer programs take over. They win, right? They, they-- Because they can replicate themselves not only where they are but in their next door neighbors, they can fill the space, uh, in a finite period of time. So That's a kind of origin of life. No real laws of physics there, certainly no real chemistry or anything like that. But if you think that the fundamental essence of the origin of life is sort of reproduction and, um, handing down your genetic information to your successors, then there's something like that going on, and it's not put in by hand like a lot of, um, simulations and, and things do. You can easily simulate evolution once you already have replication and genetic information, et cetera. But here is a simulation that actually starts from nothing, and the replication and the information you need to make it happen pop up just through the dynamics of the system. What are the implications of that for the origin of life in the real world, for looking for life, for thinking about what life is? Well, you will have to listen to this podcast 'cause, 'cause we're gonna address all those questions. And with that, let's go. [upbeat music] Leif Zagerra-Yarkas, welcome to the Mindscape Podcast.

**Blaise Aguera Y Arcas** [07:24]: Thank you, Sean. I'm really glad to be here.

**Host** [07:26]: So you are, um, an author. I don't know whether... I mean, you are the first author. I don't know whether it's an alphabetical order thing or an order of importance thing in, in, in your field. How do you, how do you list the authors for your publications?

**Blaise Aguera Y Arcas** [07:38]: Well, it varies, but if you mean the abiogenesis paper, uh, that was work that I started kind of, um, on my own in October and then pulled some other teammates into.

**Host** [07:51]: And I feel-

**Blaise Aguera Y Arcas** [07:51]: So it's, it's a, it's a legit, it's a legit first authorship.

**Host** [07:53]: Okay, good. Yeah, I mean, I get to be first author all the time just because I'm early in the alphabet, so I, I, I get more credit than I deserve. I know what it's like. Um, you know, uh, I feel a little bit guilty, but we will get at the end of the podcast to other things you're working on. I mean, you're at Google, you have a job, et cetera, and it... Does it seem crazy to say that this particular paper we're gonna talk about is a little bit outside of what you usually do?

**Blaise Aguera Y Arcas** [08:16]: Well, yes and no. So, uh, for the last year, so starting, uh, in, in October, November of last year, I've kind of changed what I'm doing. So, uh, I used to run a, a pretty large chunk of Google Research. Um, you know, I had hundreds of people reporting to me and, and I was, I was operating more like a VP and, you know, had a lot of, of administrative duties-

**Host** [08:37]: Mm

**Blaise Aguera Y Arcas** [08:38]: ... um, which, uh, which were pulling me away from a lot of the things that, you know, give me the most joy, you know, the, the actual, the actual work and the thinking.

**Host** [08:46]: Yeah.

**Blaise Aguera Y Arcas** [08:46]: And, um, it also seemed to me that, uh, you know, over the past 10 years, a l- a lot of our bets in AI were really starting to pay off and, and it was, um, and, and there's been a, a rush to really, um, milk the cow, as it were, to really d- you know, develop transformers and, uh, you know, and, and build this generation of AI and make it as useful as possible, and that's wonderful. I'm, I'm actually really excited to see that happening.

**Host** [09:08]: Sure.

**Blaise Aguera Y Arcas** [09:08]: But I didn't want to continue to focus on just developing that. I, I, I was really keen to go back to basics, um, and, and rethink some of the more fundamental aspects of, of computing and AI. So I, I started this new group, uh, and Google was very generous, you know, in, in-

**Host** [09:25]: Yeah

**Blaise Aguera Y Arcas** [09:25]: ... in supporting me in that and, and it, it's called Paradigms of Intelligence, and it really kind of is going after fundamental stuff, including all the way back to origins of life.

**Host** [09:34]: That's great. I love it. And am I correct in, uh, remembering that you have an undergraduate degree in physics?

**Blaise Aguera Y Arcas** [09:41]: Yes.

**Host** [09:42]: This is a, a long-running joke at Mindscape is that I have guests on who do all sorts of different things, but they always started out as physicists before [laughs] they went into-

**Blaise Aguera Y Arcas** [09:50]: It's probably no coincidence. Yeah.

**Host** [09:52]: [laughs] Probably no coincidence. Exactly right. Okay. So the, um, uh, I mean, there's a lot going on in the paper, so maybe talk about what is in your mind when someone says the origin of life. Like, what are the challenges that we have to try to understand?

**Blaise Aguera Y Arcas** [10:09]: Sure. Well, the first challenge is how did life begin here on Earth? Um, th- you know, there is a specific story about that, and we may never know all of those details 'cause they're lost to deep time. This all happened 4 billion years ago. Um, and you know, I've always been very interested in, in the work in biology that really tries to unpack that. There are theories about, you know, maybe it having been RNA first, an RNA world-

**Host** [10:35]: Uh-huh

**Blaise Aguera Y Arcas** [10:35]: ... or, or maybe a metabolism first that might have spun up, uh, in black smokers on the bottom of the sea where there are these, you know, hydrogen and, and carbon dioxide, uh, vents, uh, coming, uh, you know, bubbling, bubbling, uh, through these, um, porous rock chimneys. Um, but there's a more fundamental question, which is how is it possible for life to arise? Uh, you know, in the traditional view of evolution, you need life in order to beget life. You know, there was a lot of work in the 19th century, uh, trying to figure out whether life could spontaneously generate, and they never got it to happen. You know, you, you, you could only get life if life went in.

**Host** [11:09]: [laughs]

**Blaise Aguera Y Arcas** [11:10]: Um, and, and then if you look at it from a physicist's point of view, you know, I think this, this perspective was really well articulated by Schrödinger in, in his beautiful book from 1944, What Is Life?, uh, which has been quite inspirational to me. Uh, and his perspective was more thermodynamic.

**Host** [11:27]: Yeah.

**Blaise Aguera Y Arcas** [11:27]: You know, if you, uh, if you have, uh, you know, normal second law of thermodynamics says things get more random over time. Uh, life is incredibly ordered and structured, um, and there's no strict violation of the second law of thermodynamics there because energy has to go in. We need to metabolize. But, you know, while it's permitted by thermodynamics, it doesn't seem exactly encouraged by thermodynamics.

**Host** [11:49]: [laughs]

**Blaise Aguera Y Arcas** [11:49]: There, there's something mysterious there.

**Host** [11:50]: Uh, I've, I've made that exact same point many times, and I love how you just said it there, encouraged by thermodynamics. It's, it is a little bit mysterious.

**Blaise Aguera Y Arcas** [11:57]: Right.

**Host** [11:58]: And so but you're... So you're-- This paper is not delving into the role of chemical catalysts or, uh, even entropy and things like that. You're purely on a computer letting code evolve itself.

**Blaise Aguera Y Arcas** [12:13]: Yes. It doesn't directly speak to that, but it does indirectly speak to it. And, you know, in the, in the book that, um, that I'm gonna release next year with, uh, with MIT Press, What Is Intelligence?, part one is all about, uh, abiogenesis-

**Host** [12:27]: Mm

**Blaise Aguera Y Arcas** [12:27]: ... about, about this work. And it does connect it much more explicitly, both with the physics and, and with the biology. So there is, there is a real connection. It's not, it's not arbitrary.

**Host** [12:36]: I should say there is this field, and you refer to it, um, about ALife, artificial life, different than AI. And, uh, I think as you say, I forget exactly where I read this, but, uh, it's certainly true, they usually start with something they can already replicate, et cetera. And they're asking how does complexity grow? How does the effective genome grow or whatever? But this, the idea of doing simulations that in some sense mimic the actual beginning of life is a somewhat understudied field, I get the impression.

**Blaise Aguera Y Arcas** [13:06]: Totally. I, I think it, it's, it's never or very rarely, probably not really happened before, right? That we, that we begin with just noise or randomness and get replicators, get, get life. And, and I think the reasons are similar to the, the puzzles we were just talking about from the biology or physics standpoint. Um, you know, maybe it's partly a mental block.

**Host** [13:26]: [laughs]

**Blaise Aguera Y Arcas** [13:26]: Maybe it's an actual block. But, but yeah, the idea of like, well, you know, of starting from nothing, uh, it has been understudied, and I don't think it's really, it's really been shown before in, in the field of ALife.

**Host** [13:36]: There, there is a tension, and I'm, I'm entirely on your side vis-a-vis this tension, but there will be some people who say, "Look, unless you're really doing chemistry, you're not gonna teach us anything about the origin of life." And there's others, more physics inclined, who will say, "Eh, I can build kind of a spherical cow model that gets at something, even if it's not ultimately telling me precisely how the biochemistry worked at early times."

**Blaise Aguera Y Arcas** [14:02]: Yeah. Now, obviously, I'm very interested in the real biochemistry too, so I don't, I don't want to discount, uh, you know, any investigation into, into that kind of work. But I also do think about this like a physicist and, and dare I say like a computer scientist.

**Host** [14:16]: Mm-hmm.

**Blaise Aguera Y Arcas** [14:16]: Um, I'm thinking about life as a phenomenon, uh, that is more general than the particular substrate, uh, of, of chemistry-

**Host** [14:24]: Exactly, yeah

**Blaise Aguera Y Arcas** [14:24]: ... and chemistry on Earth. And, and, and in that, by the way, I, I, I think I'm very much on the same page as the founders of artificial life, who also happen to have been the same people who founded computer science and who founded artificial intelligence. So I'm thinking especially about Turing and John von Neumann.

**Host** [14:41]: So is part of the inspiration, even if it's way in the background, the idea that ultimately I'm gonna wanna ask, here's a thing, is it alive? [laughs] It might be on a computer, it might be a physical thing, but like what are the rules for when I call it life or not?

**Blaise Aguera Y Arcas** [14:57]: Yeah. I, I mean, up to a point, life is, you know, whether you call something alive or not is a matter of definition, and we, we, we have a lot of fuzzy areas, uh, you know, even in biology. Is a virus alive or not?

**Host** [15:09]: Yeah.

**Blaise Aguera Y Arcas** [15:09]: And so on. Um, so seeking a more rigorous, um, and more functional definition of life is, is part of the point. Uh, when I say functional, I mean in the same spirit as, uh, Turing's functionalism and von Neumann's functionalism. So, you know, the, the famous Turing Test about, about intelligence, uh, you know, it's all about, you know, well, if you, you know, if, if it quacks like a duck, it, it's a duck. You know, if you, if you are talking to a computer, you can... and you, and, and you think that it's intelligent and, you know, it can pass all of your tests, then if it functions intelligently, it is intelligent. And I think there's a, there's a similar, uh, functional way of thinking about, about life, um, that, that kind of goes beyond the details of which, which molecules are, uh, are being used or whether they're molecules at all.

**Host** [15:54]: Good. I mean, like I said, I'm 100%, I'm not even gonna give you a hard time about that. Like I'm, I could not possibly agree with you more. So you're gonna do it by running a bunch of computer simulations and like you said, the, the, the, the objective is to really start with nothing or just with randomness and kind of under some set of rules let it go and see if something lifelike arises. That's the, that's the basic aspiration?

**Blaise Aguera Y Arcas** [16:19]: That's the goal, and, and to have as little as possible in the beginning.

**Host** [16:22]: Good.

**Blaise Aguera Y Arcas** [16:22]: Uh, to have as, as few givens as possible. Yeah.

**Host** [16:25]: Insurance isn't one size fits all. That's why drivers have enjoyed Progressive's Name Your Price tool for years now. With the Name Your Price tool, you tell them what you want to pay, and they'll show you options that fit your budget. So whether you're picking out your first policy or just looking for something that works better for you and your family, they make it easy to see your options. Visit progressive.com, find a rate that works for you with the Name Your Price tool. Progressive Casualty Insurance Company and affiliates. Price and coverage match limited by state law.

**speaker_5** [16:56]: Natrol is the number one drug-free sleep aid brand. It's formulated with melatonin, the number one doctor-recommended ingredient for sleep support. It's the number one brand with 40-plus years of sleep expertise. It'll make you feel like the number one sleeper in the world. So make Natrol your number one choice for sleep. Nielsen lasted 52 weeks, week ending 3/28/26, based on a survey of doctors who recommended drug-free sleep support products. These statements have not been evaluated by the Food and Drug Administration. This product is not intended to diagnose, treat, cure, or prevent any disease.

**Host** [17:26]: And then one of the, um, uh, obstacles you run up against is that the best computer language to use for this is something called Brainfuck. [laughs] Which apparently is even hard to search for on the internet because people, you know, like to misspell it or something like that to make it sound less bad. But, uh-

**Blaise Aguera Y Arcas** [17:44]: Like put, put rolixes or asterisks in it or something

**Host** [17:46]: ... tell us about... Exactly, right. Uh, so tell us about that language and why you chose it.

**Blaise Aguera Y Arcas** [17:50]: Yeah. I, I had to, um, check with MIT's, uh, contract whether-

**Host** [17:55]: [laughs]

**Blaise Aguera Y Arcas** [17:55]: ... whether, uh, you know, if it was, uh, obscene or, uh, uh, uh, or something, [laughs] whether this would, would pass muster for the book.

**Host** [18:01]: And it's not your fault. It's a pre-existing thing.

**Blaise Aguera Y Arcas** [18:02]: Not my fault.

**Host** [18:03]: Yeah.

**Blaise Aguera Y Arcas** [18:04]: No, no. It was invented 40 years ago, or 30 years ago, sorry, uh, by, uh, Urban Müller, a, a German, um, actually a physics student.

**Host** [18:11]: There you go. [laughs]

**Blaise Aguera Y Arcas** [18:12]: But, uh, [laughs] go figure. Um, and amateur juggler apparently. Um, so, so yeah, it, Brainfuck is not the only language one can use for doing this for sure. Uh, and we've now tested it- On many other languages as well. Uh, our, the, our latest, uh, demo, uh, which is very beautiful, uh, made by Alex, uh, Mordvintsev actually uses, uh, the Z80, the Zilog Z80 processor-

**Host** [18:35]: Okay

**Blaise Aguera Y Arcas** [18:35]: ... which, uh, was, um-

**Host** [18:36]: I had no idea what this is

**Blaise Aguera Y Arcas** [18:38]: ... I think existed. Well, it came out in 1976.

**Host** [18:40]: Wow.

**Blaise Aguera Y Arcas** [18:40]: Uh, so it's been around for a long time. Uh, and it powered the Osborne, uh, computers-

**Host** [18:45]: Oh

**Blaise Aguera Y Arcas** [18:45]: ... and the TRS-80, and all of that. So, like, we grew up with-

**Host** [18:48]: Now that's my era now. Okay.

**Blaise Aguera Y Arcas** [18:49]: [laughs] Yeah, exactly. So it's a bit of a nostalgia trip, and it works just as well in, in Zilog assembly language. So it's not, it's not required that, uh, that it be Brainfuck. But the reason that I began with Brainfuck is because it's very, very close to a Turing machine. So its, its design is, uh, is extremely minimal. It has eight instructions. I actually only used seven of them-

**Host** [19:11]: Oh

**Blaise Aguera Y Arcas** [19:11]: ... for the first simulations.

**Host** [19:12]: Okay.

**Blaise Aguera Y Arcas** [19:13]: Um, and it works on a, on a tape that looks just like a Turing tape. So, uh, you know, it's, it's just super minimal. I, I think, um, uh, Urban Müller made a compiler for it that, you know, compiled it to, you know, to assembly language or whatever in 173 bytes, something like that.

**Host** [19:27]: [laughs]

**Blaise Aguera Y Arcas** [19:28]: So it's really minimal.

**Host** [19:30]: So, uh, well remind us, 'cause it's a broad audience, what is, what is going on in your mind when you say the words Turing machine?

**Blaise Aguera Y Arcas** [19:36]: Yeah. So the Turing machine is a notional machine. It's a, it's a conceptual machine invented in the 1930s by Alan Turing. Um, in many people's minds, mine included, that was kind of the beginning of real computer science. Uh, so it was a wonderful paper, uh, in which he was trying to, uh, not trying, he succeeded in cracking one of Hilbert's big math problems that, you know, he'd posed in the previous century, which is, um, can one figure out a mechanical way to decide on the truth of a mathematical statement? Um, so this, um, uh, this problem is, um, uh, is one that requires that you actually formulate what computation is, and it turns out that, you know, his definition of what computation is turned out to be the much more important part of that paper-

**Host** [20:25]: Mm

**Blaise Aguera Y Arcas** [20:25]: ... than the actual result, which was no, you can't decide a priori on the truth or falsehood of a mathematical statement.

**Host** [20:31]: [laughs]

**Blaise Aguera Y Arcas** [20:31]: Um, but, but he, he, he had a very creative way of, of, of, um, of cracking that, that nut, which was to design a machine, uh, that would involve a tape, uh, with cells on it that, you know, you could write symbols on, and a read/write head that would be able to step left and right along the tape, uh, and a table of rules that would say, uh, you know, based on the state of the, of the head and what character is on that cell, whether one should erase, write a new character, step left, step right. Um, and, uh, and so that was, that's a Turing machine. And then the, the next move, the really brilliant move, was the universal Turing machine.

**Host** [21:09]: Mm.

**Blaise Aguera Y Arcas** [21:09]: The idea being, uh, that he first showed a Turing machine can compute anything that can be computed by, say, a person with pencil and paper. Um, and then he showed that if you write the rules, if you write that table of rules on the tape itself, then there exists certain tables of rules that will allow you to interpret the table of rules on the tape and carry out the, the computation that it specifies. And that's, that sort of like, uh, you know, snake eating its tail move-

**Host** [21:37]: Mm-hmm

**Blaise Aguera Y Arcas** [21:37]: ... gives you a general purpose computer. That's sort of the definition of general purpose computation.

**Host** [21:42]: And when you say Brainfuck is kind of like a Turing machine, it is in fact Turing capable, right? It can do anything a Turing machine can do.

**Blaise Aguera Y Arcas** [21:51]: Right. So this idea of Turing completeness is, you know, does a given machine or a given mathematical system, uh, can you, can you map it to a Turing machine? If you can map it to a Turing machine, then by construction it can compute anything that can be computed.

**Host** [22:06]: Right.

**Blaise Aguera Y Arcas** [22:06]: And, um, uh, and Brainfuck, uh, consists of eight instructions. Because it's so few, I can actually just say what they are.

**Host** [22:12]: Please.

**Blaise Aguera Y Arcas** [22:12]: Uh, it's, um, so there's, there's a head. Uh, the head can step left, step right. Um, it can increment or decrement the byte that it's looking at right now, so it's the, the tape is a tape of bytes that can range in value from zero to 255.

**Host** [22:26]: Uh-huh.

**Blaise Aguera Y Arcas** [22:26]: If you increment 255 it goes back to zero, if you decrement zero it goes up to 255. It kind of wraps around. Um, there's an input and output, uh, operation, so there's a, there's a console in the original Brainfuck. And so output will, you know, will just emit the byte that is under the head-

**Host** [22:41]: Yep

**Blaise Aguera Y Arcas** [22:41]: ... and input will read a byte into, into that position. And then the final two instructions are open bracket and close bracket, which are looping instructions. So it turns out that for a Turing machine you need branching in order to be able to implement loops. You need if/then. And, uh, and so the brackets just say, um, at the open bracket if the, uh, byte under the data pointer is, uh, non-zero, uh, then continue. If it's zero, then jump to the matching close bracket. At the close bracket, if the byte under the, under the head is non-zero, then jump back to the open bracket, else continue. And that's it. That's the whole language.

**Host** [23:19]: And with that you can feed it a tape and... Well, sorry, 'cause you have the tape and the program in the original Brainfuck thing. You're gonna, you're gonna modify that, but-

**Blaise Aguera Y Arcas** [23:30]: Right

**Host** [23:30]: ... in the original thing, so there's instructions for the program, and then there's a tape, and the head will just bop back and forth reading the tape, writing to the tape, and then that in principle can do any computation we know how to do.

**Blaise Aguera Y Arcas** [23:42]: Right. With a, with a long enough program, long enough tape, and enough time you could implement Windows on that or-

**Host** [23:48]: Yeah [laughs]

**Blaise Aguera Y Arcas** [23:48]: ... whatever you want, although it would be an absolute nightmare. The reason that, that, that Urban, uh, named it Brainfuck is because it is very, very hard to program it. Uh, so, you know, you look at a "Hello, world" program and it's just-

**Host** [23:58]: Right

**Blaise Aguera Y Arcas** [23:58]: ... this incomprehensible jumble of characters.

**Host** [24:01]: It's hard to program but even harder to read, 'cause it, like you said-

**Blaise Aguera Y Arcas** [24:03]: Yes

**Host** [24:03]: ... it's all just like plus bracket, dot, dot, dot, dot, and you have no idea what's going on. [laughs]

**Blaise Aguera Y Arcas** [24:08]: Right. Not a very user-friendly language, but a Turing complete one.

**Host** [24:11]: And good for your purposes precisely because the set of symbols is so tiny, right?

**Blaise Aguera Y Arcas** [24:16]: Exactly. Uh, it's a tiny set of symbols. It's not the smallest Turing complete language, but it's, it's down there. It's, it's, it's among the smallest Turing complete languages you can make, so, um, one can- Both simulate it really fast, and one can do a lot of interesting mathematical analysis on it that would be harder with a more complex language.

**Host** [24:34]: Right. And you do, and in fact, what you folks implement is a variant of this, which I already sort of spoiled, but the tape and the program are in the same place.

**Blaise Aguera Y Arcas** [24:45]: Yes. So, um, the, the thing that needed to be changed about the original Brainfuck, um, is that it has, uh, a separate... In, in effect it's really two tapes, even though that's not the way Urban put it, you know, in, in, in the specification.

**Host** [24:59]: Yeah.

**Blaise Aguera Y Arcas** [24:59]: So there's a, there's a program tape and a data tape, and the program tape has its own read head which just kind of steps along, you know, and, and occasionally jumps back with those loops. And the data, the data tape is separate. Um, we wanted to make it self-modifying. Uh, so self-modifying code means that the code itself is actually in the data space, and it can be manipulated just as, just as well as, as, as data can be. Um, and why did we wanna do that? Well, because, uh, I had a hunch that self-modification was actually the key to abiogenesis-

**Host** [25:32]: Sure

**Blaise Aguera Y Arcas** [25:33]: ... to the creation of life. And, and I can explain a little bit more about, about, uh, why, but maybe I'll save that for a bit later. Um, so anyway, there's, there's now just one tape, and that tape contains both code and data. And this means that you have to imagine that there are actually not two, but three heads now.

**Host** [25:49]: Okay.

**Blaise Aguera Y Arcas** [25:50]: Because the other thing, the other thing that was on the original Brainfuck was a console, and-

**Host** [25:53]: [laughs]

**Blaise Aguera Y Arcas** [25:53]: ... we didn't wanna have a console that is separate from-

**Host** [25:56]: Right

**Blaise Aguera Y Arcas** [25:56]: ... uh, you know, from the tape. So everything has to be self-contained. So now you have a, an instruction pointer that walks along the tape, you have a data pointer that can be moved anywhere along the tape, and you have a console pointer which says if you're gonna print or input, like, where in the tape are you going to, are, are you going to print an input? So everything-

**Host** [26:12]: Oh, I see. Okay

**Blaise Aguera Y Arcas** [26:12]: ... is all in the same, uh, you know, in the same tape.

**Host** [26:15]: Right. Good. And then so this gives you a toolbox or a, a sandbox, I suppose, in which you can play. And you're gonna play by starting, like you said, with nothing, and let it rip, see what happens. But there's, there's some details there. You can't just let one program go. That would be uninteresting.

**Blaise Aguera Y Arcas** [26:34]: Right. So, uh, so the other, uh, the other trick, uh, and, and we called, we called this environment BFF, by the way, for reasons that might s- might become obvious, uh, soon. [laughs]

**Host** [26:45]: [laughs]

**Blaise Aguera Y Arcas** [26:45]: But, um, but the, uh, the trick is that we, we began with a, a soup of tapes. Uh, and these tapes are a fixed length. They're of length 64.

**Host** [26:56]: Okay.

**Blaise Aguera Y Arcas** [26:56]: And, uh, and, and rather than just running one tape, tapes are actually run in pairs. So you grab two tapes out of the soup, and you stick them end to end, and then you think of that as the tape, and you run it. It's everything is self-contained, so it could modify itself. Then you break those tapes back apart, and you put them back in the soup. And that's it. And you do that-

**Host** [27:15]: Mm-hmm

**Blaise Aguera Y Arcas** [27:15]: ... over and over. Um, you also, um, uh, occasionally, you know, there's a mutation rate. Uh, if, if, if you allow mutations to happen, then once in a while a byte in that soup will get randomized. It'll just get-

**Host** [27:26]: Okay

**Blaise Aguera Y Arcas** [27:27]: ... changed to something random. Uh, and there's one more detail, which is that since it's possible for a program to get stuck in an infinite loop, you need to have either some maximum number of instructions that, that are allowed to run, uh, or have some probability, which is the way I prefer, per unit time that, that any given tape will just stop running, uh, where- wherever it is. So, uh, so those are the extra bits. There's no fitness function. In other words, there's no specific, you know, um, function that is saying any tape is better than any other tape. You're just plucking them out of the soup, sticking them end to end, running, putting them back, and repeating millions of times.

**Host** [28:01]: And when you stick them end to end, so it's not like you take the first half of one and the second half of the other. You just, you have... I'm just, I'm just trying to get in my brain what the specifics are. So you just run the two of them next to each other, and there's some topology on the graph. There's some meaningfulness to nearest neighbors.

**Blaise Aguera Y Arcas** [28:17]: Right. So, uh, each of, each tape is 64 bytes. If you stick them end to end, you'll have 128 bytes.

**Host** [28:22]: Yeah.

**Blaise Aguera Y Arcas** [28:22]: And that's, and, and you think of that as the tape that you run. Now, it, this may seem a little arbitrary, but the reason that that was important is because, uh, in addition to self-modification, life relies on interactions.

**Host** [28:35]: Yeah.

**Blaise Aguera Y Arcas** [28:35]: So, uh, you know, you have to have stuff that is interacting. Um, you know, if you, if, if nothing interacts with anything, nothing can happen. So, you know, in, in chemistry, uh, that would be molecules interacting with each other. So you could think about those, those, uh, those tapes as being like molecules.

**Host** [28:51]: Yeah. So the, and the, so the tapes are modifying themselves and their neighbors-

**Blaise Aguera Y Arcas** [28:55]: Right

**Host** [28:56]: ... just like people or real organisms actually do. Okay, and so-

**Blaise Aguera Y Arcas** [28:59]: Right

**Host** [28:59]: ... starting, uh, uh, give us a, give us an intuition for what a random code in Brainfuck would do. I presume it would just crash, or maybe it would be an infinite loop usually? I don't know.

**Blaise Aguera Y Arcas** [29:09]: It's actually quite hard to make an infinite loop from just random noise. Um-

**Host** [29:12]: That's probably right. Okay

**Blaise Aguera Y Arcas** [29:13]: ... uh, because, um, r- you know, remember, so in, in, in my version of, of, of, of Brainfuck and BFF, there are seven instructions. Uh, every byte can have 256 values. So only seven 256ths of the bytes even, uh, code for an instruction at all.

**Host** [29:29]: Hmm.

**Blaise Aguera Y Arcas** [29:30]: If something doesn't code for an instruction, it just gets skipped over. So it just-

**Host** [29:33]: Oh, okay

**Blaise Aguera Y Arcas** [29:33]: ... you know, 'cause it's a, it's a no-op, as you call it in computer science. So, um, so what that means, I mean, that's roughly one, one in 32. Um, that means that out of the 128 bytes in a tape, um, uh, you'll, you'll only have, uh, you know, a small handful, you know, two, three, four, um, you know, working, um, working bytes. You know, bytes that actually have an-

**Host** [29:54]: Okay

**Blaise Aguera Y Arcas** [29:54]: ... have an instruction on them. So what might, might those bytes be? Like, you know, move the, move the head two times to the left and one time to the right. Done. [laughs] You know?

**Host** [30:02]: Done, yeah. Okay.

**Blaise Aguera Y Arcas** [30:02]: And, and no change. So in the beginning, um, very, very little computation is happening.

**Host** [30:07]: Right.

**Blaise Aguera Y Arcas** [30:07]: And, um, you know, it just seems like a very unpromising start.

**Host** [30:11]: So I, I shouldn't say crash, but it does, it moves around and then fizzles out. It just stops, and nothing interesting happens.

**Blaise Aguera Y Arcas** [30:16]: Just nothing happens.

**Host** [30:17]: Right. Yeah.

**Blaise Aguera Y Arcas** [30:18]: Exactly.

**Host** [30:18]: So-

**Blaise Aguera Y Arcas** [30:18]: It is, it is possible for it to crash. If you get to a closed bracket and there was no matching open bracket, that's a crash.

**Host** [30:24]: Oh, okay.

**Blaise Aguera Y Arcas** [30:24]: But, um, but I think that's the only way it can crash.

**Host** [30:27]: Good. I mean, that's, it's, so it's harder to crash in Brainfuck than it is in just regular programming [laughs] languages.

**Blaise Aguera Y Arcas** [30:32]: Yeah. Yeah, yeah. Which was also part of the point, that it was, you know, it's kind of open-ended enough that, you know-

**Host** [30:36]: It's a little robust that way

**Blaise Aguera Y Arcas** [30:37]: ... it's a little robust.

**Host** [30:38]: Yes.

**Blaise Aguera Y Arcas** [30:38]: Almost anything will do something, even though very little of that something will be useful.

**Host** [30:42]: And well, how quantitative can we be about that? I mean, what fraction of ... things that those bytes could be doing will give us interestingness in some well-defined way.

**Blaise Aguera Y Arcas** [30:53]: Well, um, out of those seven instructions, only three of them actually result in a change to the tape. Uh, there's plus and minus, which increment and decrement whatever byte the data pointer is on, and there's comma, which is the copy instruction. So that, that was originally input, uh, the input from the console. But if you think about, you know, print and input, they're really the same thing. They're just copy from one place in the tape to the other place, another place in the tape.

**Host** [31:18]: Sure. Okay.

**Blaise Aguera Y Arcas** [31:19]: Since the, the console and the, and the data pointer are just different spots at the same tape, so that's why we could reduce it from eight instructions to seven. So only those three instructions can result in changes at all. So that tells you that, um, you know, uh, if you don't have loops, and, and you know, you're unlikely to get a, a good loop 'cause that requires matching open bracket and close brackets somewhere that enclose, you know, one of, uh, one of these, uh, uh, write statements. So, um, you know, in the beginning, uh, y- yeah, you can be very quantitative and you can calculate the probabilities that anything will change, and they're not high. [laughs] Uh, you know, it's, it's-

**Host** [31:53]: Yeah

**Blaise Aguera Y Arcas** [31:53]: ... it's, uh, you know, the mo- the majority of interactions result in nothing.

**Host** [31:57]: Okay. Very good. And then how many... So basically you're doing parallel many tapes, many programs, whatever you wanna call them, at once. How many were you doing in your simulations?

**Blaise Aguera Y Arcas** [32:07]: So, um, uh, we... Well, um, in the first ones I did 8,192 tapes. Um, in, in some of my later ones I, I only used 1,000, 1,024.

**Host** [32:17]: Okay.

**Blaise Aguera Y Arcas** [32:18]: So 1,024 tapes is, is plenty to get all of the interesting phenomena.

**Host** [32:22]: Right. And then so I don't wanna put words in your mouth. Tell the audience what happened. You put in some primordial soup and you let it percolate. [laughs]

**Blaise Aguera Y Arcas** [32:31]: Yes. Uh, so, uh, in the beginning, you know, there are about two operations, uh, run per interaction, and nothing much happens, and it, it looks, uh, it looks boring unless you look very closely, but we didn't look closely till later. Um, and, and then at some point, uh, a few million, uh, interactions in, typically, um, everything will start to change. Uh, and, and it's very, very sudden. So on, on my computer, you know, when I, when I first ran this, uh, you know, it was just sort of things were scrolling by really fast, and suddenly the scrolling stopped, and it was sort of going chunk, chunk-

**Host** [33:04]: Yeah

**Blaise Aguera Y Arcas** [33:04]: ... chunk, and the fan turned on. You know, it was like [laughs] suddenly a lot of computing was happening, and, um, the number of operations, uh, running per interaction just leaps from, you know, very small numbers to thousands. Uh, and, and if you look at the contents of the tapes, suddenly they are full of instructions, they're dense with instructions, and they're very complex. And moreover, they're replicating. So, uh, you know, you find a bunch of copies of different programs, and these programs are interacting in, in complex ways. So, you know, it's, it's really quite dramatic.

**speaker_6** [33:36]: Every breakthrough starts with someone willing to take part. Summit Clinical Research is seeking volunteers with fatty liver disease to join clinical studies focused on MASH, a more severe form of fatty liver disease with limited treatment options today. Participants may receive study treatment, close medical oversight, and compensation at no cost. And you can contribute to research that could help others. If you've been diagnosed with fatty liver disease, take the first step. Go to fattyliverstudies.com and check your eligibility.

**Host** [34:06]: What does... I, I think this is implicit in what you said already, but what does replicating mean in this context? Is it one program is writing itself onto its neighbor?

**Blaise Aguera Y Arcas** [34:17]: That's actually a more profound question than it sounds like. [laughs]

**Host** [34:20]: [laughs] Okay.

**Blaise Aguera Y Arcas** [34:21]: So the, the simple definition of replicating is, uh, I mean, the, well, the simplest version, I guess, of replication is, um, you know, you, you start running, uh, a tape, and the first 64 bytes copies itself onto the second 64 bytes, for instance. If that happens, then when you pull them apart, regardless of what was in the second half, um, you know, you now have two copies of what was in the first half. That's replication, and that will definitely take off exponentially-

**Host** [34:46]: Yeah

**Blaise Aguera Y Arcas** [34:46]: ... when it happens. Um, but the reason it's a, it's a subtler question than it sounds like, um, is that you can also have little bits of the tape replicating themselves, which, which it turns out-

**Host** [34:57]: Okay. Yeah

**Blaise Aguera Y Arcas** [34:58]: ... happens earlier in the process. Um, and you can even have situations where, for instance, you know, one thing creates another thing, which creates another thing, which creates another thing, which eventually comes back around and sometimes creates the original. So you can have these complex life cycles and, and that's a form of replication too.

**Host** [35:15]: Sure.

**Blaise Aguera Y Arcas** [35:15]: Anything that, that ultimately comes back around and generates more of you than would happen, uh, in the, in the null case, you know, if there's, if nothing is going on, is replication, however weak.

**Host** [35:28]: I think that actually that is reminiscent of a finding in the, the sort of more chemically based origin of life context, where it turns out, uh, my, my recollection back from when I wrote my book, "The Big Picture," you know, mumbly mumble years ago, was that they had not built a single molecule that could sort of auto-catalyze itself, but they could build two molecule pairs where A could make B and B would make A, and it would keep going.

**Blaise Aguera Y Arcas** [35:53]: Exactly.

**Host** [35:54]: So you're finding things like that, basically.

**Blaise Aguera Y Arcas** [35:56]: Exactly. Which is the same way that, that, that DNA replication works, by the way.

**Host** [35:59]: Yeah.

**Blaise Aguera Y Arcas** [35:59]: Right? You have, you have, uh, base pairs that are, that are, um, uh, that are conjugate and, right, and, and, you know, you, you pull them apart, one of them makes the other one, and then, you know, uh, and then they, they, they conjugate. So, so yeah. Um, that's, that's called, uh, in abiogenesis, that's called an autocatalytic set-

**Host** [36:15]: Right

**Blaise Aguera Y Arcas** [36:16]: ... of, of chemicals. And, and again, I think that that's a more basic concept than chemistry.

**Host** [36:21]: Yeah.

**Blaise Aguera Y Arcas** [36:21]: Uh, there's, there's something, there's something pretty deep about that, and, and what we see is exactly the same.

**Host** [36:26]: And from a pure statistics point of view, is it, am I correct of to rephrase it as saying that the ki- the set of instruction lists, the set of tapes that, that act this way is tiny in the set of all possible tapes, but tends to take over, is more robust in some way that I'm still struggling to quite articulate?

**Blaise Aguera Y Arcas** [36:46]: Yeah. So, um, one of the, um, one of the people who really kind of, um, informed my thinking about all of this, uh, is Adi Pruss-

**Host** [36:55]: Uh-huh

**Blaise Aguera Y Arcas** [36:55]: ... who is an emeritus, uh, professor of chemistry, uh, at Ben-Gurion, uh, University of, of the Negev in, in Israel. Um, and he spent many years studying the chemistry of, of the origins of life, and, uh, he coined this term dynamic kinetic stability. Uh, so what he means by that is that normally in thermodynamics, we think about, you know, matter, um, arriving at a more and more stable state, or in general some, some, um, the statistics of some ensemble becoming more and more stable. It meaning that, meaning that, um, you know, if they start out very out of equilibrium, they'll move toward an equilibrium, and the closer to equilibrium, the more stable that-

**Host** [37:33]: Right

**Blaise Aguera Y Arcas** [37:33]: ... that configuration is. Um, but, but what, what Adi Pruss realized is that if you have replicators, then you have a new form of stability that arises, which he calls dynamic kinetic stability. If, you know, A makes B, B makes C, and C makes A, then that has a stability that is actually even greater than the stability of something that takes a long time to degrade but still ultimately degrades. You know, that, that replicator can last forever. Uh, you have a fragile thing like a soap bubble-

**Host** [38:02]: Hmm

**Blaise Aguera Y Arcas** [38:02]: ... or you can have a really robust thing like granite, but, you know, no matter how robust it is, if it's passive, every interaction it has with the world can only degrade it.

**Host** [38:11]: Right.

**Blaise Aguera Y Arcas** [38:12]: Uh, whereas, whereas the special thing about life and about replicators generally is that they can push back actively against the forces of, of, um, uh, of entropy and, and they can last forever.

**Host** [38:23]: So that's very evocative. Uh, does it, uh, do you see that in the simulations? There's some kind of self-repair? Do you see like what would-be replicator kind of get influenced by its environment in a negative way and then bounce back?

**Blaise Aguera Y Arcas** [38:37]: Absolutely. Um, we, we do see that. Um, but you know, the, the, the very trivial way in which we see that is just that once you have a population of replicators, that's more robust, uh, than, than, than one of them, right?

**Host** [38:47]: Right. Okay.

**Blaise Aguera Y Arcas** [38:47]: If it's replicating, then if one of them gets damaged, well, there's another one that can still replicate. So population is the, is the, the, the first way that, that robustness happens. You know, there's, there's a force actively making it expand, and so if you damage it, it still comes back. Now, you can go further and, and, and they can become actually robust and repair themselves, and, and we do see that kind of stuff happen as well. Um, but, but even replication alone is already dynamically kinetically stable.

**Host** [39:12]: And you said that you didn't put in a fitness landscape or fitness function. You didn't sort of rank the success a priori, but isn't there effectively a fitness function? Um, or is, is it just that you sort of... Well, let, let me ask, let me phrase that as a question. Have you rediscovered natural selection?

**Blaise Aguera Y Arcas** [39:32]: Yes.

**Host** [39:32]: Okay.

**Blaise Aguera Y Arcas** [39:33]: Uh, we have absolutely redisc- rediscovered natural selection. Um, you know, the, uh... And this goes back to Adi Pruss as well. The way he puts it is that dynamic kinetic stability... Sorry, let me just, um-

**Host** [39:42]: Go ahead. Yeah.

**Blaise Aguera Y Arcas** [39:43]: [clears throat] The way Adi Pruss puts it is that dynamic kinetic stability is, um, Darwinian selection, and, uh, Darwinian selection is just, is just another way of putting thermodynamic stability in that dy- in that dynamic setting, uh, where, where you have replicator dynamics in, in addition to just the normal dynamics of, of entropy. So, so yes, there, there's, there's a, there's a fitness function there in the sense that if you, if you see a replicator there, uh, at one moment and you see another string, uh, that is not a replicator, and then you look again later on, you're likely to still find the replicator, and you're likely not to find-

**Host** [40:23]: Right

**Blaise Aguera Y Arcas** [40:23]: ... the string that wasn't a replicator because it will have been either destroyed by entropy, by, by random mutation or overwritten by the replicator.

**Host** [40:29]: So when I think about... I don't know. I, I wanna understand this for my own selfish purposes. I'm doing research in closely connected areas here, and you're very, very helpful right now. Um, is it [laughs] really natural selection in the sense that when I think of natural selection, I think of like a handing down of a genome from organ- organism to organism and sharing those and mutating them, but I guess you're gonna tell me that the whole tape is kind of like a genome.

**Blaise Aguera Y Arcas** [40:57]: This is also a great and, and, and profound question because, um, there is actually a big change that happens at some magical point in this, in this kind of, uh, abiogenesis process, where you go from just an autocatalytic set, meaning just things that, you know, tend to kinda sorta make something else that makes something else that makes you-

**Host** [41:17]: Yeah

**Blaise Aguera Y Arcas** [41:17]: ... to something that has a genome. And what, what having a genome means is that you now have an, a, a l- a list of instructions for making yourself, and if those instructions are changed in any way, that change is preserved in, in, uh, in the-

**Host** [41:31]: Okay

**Blaise Aguera Y Arcas** [41:31]: ... in the descendants. In other words, you have heritability. Um, so this goes back to, um, some of the, I think, most foundational work in biology, uh, that is not generally acknowledged as work in biology.

**Host** [41:43]: [laughs]

**Blaise Aguera Y Arcas** [41:43]: And it's, it's by, uh, it's by John von Neumann-

**Host** [41:46]: Hmm

**Blaise Aguera Y Arcas** [41:46]: ... uh, the, the, one of the founders of computer science. Um, so when he was messing around at Los Alamos with, with, uh, Stan Ulam and they invented cellular automata-

**Host** [41:56]: Yep

**Blaise Aguera Y Arcas** [41:56]: ... um, one of the, one of the, the applications that he invented for cellular automata was self-reproduction. Uh, and, and he, he designed this amazing self-reproduction system using cellular automata that was only simulated on a computer for the first time in the mid-'90s because-

**Host** [42:10]: [laughs]

**Blaise Aguera Y Arcas** [42:10]: ... it's actually, it's, it's very hard to actually make it, you know... Like, running it is very computationally intensive. But, um-

**Host** [42:15]: We finally caught up to the brain of von Neumann in our computer configuration.

**Blaise Aguera Y Arcas** [42:17]: Exactly. I'm not sure if we've caught up-

**Host** [42:19]: [laughs]

**Blaise Aguera Y Arcas** [42:20]: ... but we, but we got closer. Um, but, but his, his insight is, is, uh, is actually very easy to, to express but very profound. So he said, um, "If you want something that is able to evolve in an open-ended way, replicate and evolve, it needs to have something like a genome." And basically, he was asking, how does something like a bacterium, how does life exist? How is it possible that it can build another copy of itself that is just as complex as it itself is? That seems like-

**Host** [42:46]: Yeah

**Blaise Aguera Y Arcas** [42:46]: ... pulling yourself up by your own bootstraps. It doesn't make any sense. Um, and, and what he realized is that you, you can do it if you, if you have the following things. Um, first you need a tape, like a Turing tape, that has the instructions for building yourself. And then you need a machine A, which will chunk along on that tape and follow the instructions and build whatever the tape says. And then you need a machine B, which can copy the tape, assuming that the tape itself is also made out of stuff that you can find in your environment. If the instructions for making machine A and machine B are on the tape, then you have a replicator.

**Host** [43:22]: Right.

**Blaise Aguera Y Arcas** [43:23]: So, uh, and, and what's so cool about, about this, uh, about this realization is, you know, he, he wrote, he wrote this all up in 1951. This was before the structure and function of DNA had been discovered.

**Host** [43:32]: Yeah, it's an obvious thing you, you think of when you say those words out loud. Like, yeah, that's what DNA does, right.

**Blaise Aguera Y Arcas** [43:36]: Exactly. So he called it. He totally called it. Uh, his machine A is, is what ribosomes do. Uh, his machine B is what DNA polymerase does. And of course, the tape is DNA. Uh, and the instructions for building, uh, ribosomes and DNA polymerase are encoded on DNA. So i- it's exactly right.

**Host** [43:54]: It, it is one of those, um, events in the history of science that gives you hope for the efficacy of pure thought, right? Like-

**Blaise Aguera Y Arcas** [44:01]: Yeah

**Host** [44:01]: ... you wanted something to work out in a certain way, how could it possibly do it, and you figured it out. But you know, it wasn't that many years before he figured out DNA. I do wonder-

**Blaise Aguera Y Arcas** [44:10]: Right

**Host** [44:10]: ... how influenced he was by people like Schrödinger talking about these things.

**Blaise Aguera Y Arcas** [44:15]: I'm sure, I'm sure he was. And, and, and Schrödinger did also anticipate DNA, although, although von Neumann went a little further in that he separated, if you like, the machine A and machine B. Like, he realized that there had to be something different about the tape, uh, versus the ribosome, which, which Schrödinger didn't quite connect in 1944.

**Host** [44:32]: Good.

**Blaise Aguera Y Arcas** [44:32]: Um, but, but yeah, it was very profound. And, and that is more than an autocatalytic set, uh, for two reasons. One is heritability.

**Host** [44:38]: Mm-hmm.

**Blaise Aguera Y Arcas** [44:39]: But the other, which is I think even deeper, is that this is a Turing machine. What, what von Neumann described is a computer. Uh, machine A and machine B have to be computers, and the reason is you can't execute the instructions on a tape without having a loop, right, that says, like, if this, then add that, and, you know, at the end, stop.

**Host** [44:57]: Yeah.

**Blaise Aguera Y Arcas** [44:58]: Right? So there's, there's a, there's a loop there. Uh, you have all of the, um, uh, requirements of a, of a, of a, of Turing completeness of a computer. So what, what von Neumann really said is nothing can be life without computing, or rather that, uh, you know, that life is computation at a very, at a very deep level.

**Host** [45:17]: I love that. I wonder if I've ever heard that phrase that way before, but I don't think I have, and it's finally stuck in. Maybe I'm at the right point of my education to appreciate something like that.

**Blaise Aguera Y Arcas** [45:25]: You know, I, I don't think that this has actually really been said-

**Host** [45:28]: Okay

**Blaise Aguera Y Arcas** [45:29]: ... uh, before. I could be wrong. I mean, it's, you know, people always... I mean, right, they're al- these ideas are always bubbling around-

**Host** [45:33]: Yeah

**Blaise Aguera Y Arcas** [45:33]: ... and I feel like they're in the air. But, but, um, but I at least have felt like, like this has come as an aha moment for me just in, in the past few months.

**Host** [45:40]: Good. Yeah. No, no, no, when you say it out loud, you're like, "Oh yeah, of course," but I, I've never heard anyone say that out loud before, so that, that is wonderful. So, okay. So in the, back to the reality of this computer program you're running, um, how do you know when this happens? You said you were looking at an output, but probably there's something more sophisticated going on.

**Blaise Aguera Y Arcas** [45:56]: Yeah. It's not just listening for the fan-

**Host** [45:58]: [laughs]

**Blaise Aguera Y Arcas** [45:58]: ... to turn on. Um, well, so, so the, uh, the first, the most obvious thing that happens is, um, it's, you can visualize it very beautifully if you just draw a dot, um, on, on, um, on a graph for every interaction where the X-axis is time-

**Host** [46:14]: Mm-hmm

**Blaise Aguera Y Arcas** [46:14]: ... and the Y-axis is how many operations ran in that interaction. So for a long time you just see, you know, it's, it's low. There aren't many operations happening, and then suddenly at some point, which, you know, depending on randomness, it could be after a million, it could be after 10 million interactions, um, suddenly there's this wall of blackness. Like-

**Host** [46:34]: [laughs]

**Blaise Aguera Y Arcas** [46:34]: ... the thing is computing really hard. All of these interactions are, are, are, um, are resulting in, in thousands of operations running. So that's the, that's the tell that something has, something has happened. You can also, um, measure the Kolmogorov complexity of the soup. So Kolmogorov complexity is, um, is, is very sim- it's very simple to approximate. You can just zip the soup.

**Host** [46:56]: Yeah.

**Blaise Aguera Y Arcas** [46:56]: So you just take the, all the, all the bites in the soup and you, and you think about it as a file, and you zip it, and then you take the ratio of the zips, of the zipped file size to the original. That gives you a sense of how compressible it is.

**Host** [47:06]: Mm-hmm.

**Blaise Aguera Y Arcas** [47:07]: Um, and in the beginning when you start off with just noise, it is incompressible. Uh, random bytes are incompressible. Try it at home. You know, if you make a file full of random numbers and you zip it, it will stay the same size. It'll actually grow a little bit 'cause there's, like, a header.

**Host** [47:19]: Yeah. [laughs]

**Blaise Aguera Y Arcas** [47:20]: Um, but, but the moment you start to have replicators in there, um, you expect that it's gonna suddenly become a lot more compressible because many of those strings, many of those-

**Host** [47:29]: Right

**Blaise Aguera Y Arcas** [47:29]: ... tapes can be expressed as pasted together parts of other tapes, and that's what you see, and you see this dramatic transition from incompressible, it's like a gas, to whoosh, you know. It, it, it's like a, it's like a crystal. Not quite like a crystal because there's still a whole ecology of different tapes, but its comple- its complexity drops way, way down.

**Host** [47:48]: So there's a phase transition.

**Blaise Aguera Y Arcas** [47:50]: Yes.

**Host** [47:50]: And the order parameter could be either the number of computations being done or the algorithmic complexity of the soup. [laughs]

**Blaise Aguera Y Arcas** [47:58]: Yes, yes. I, that's, that's right. It, it looks, it looks exactly like a phase transition. And, um, you know, usually when you, when, when a physicist talks about phase transitions, you know, we think about correlation functions.

**Host** [48:09]: Uh-huh.

**Blaise Aguera Y Arcas** [48:09]: Uh, so you know, in, in a gas, the correlation function is just a delta function. You know, the other particles could be anywhere. If it's ice, then it's this very structured, you know, crystalline structure. Um, well, compressibility and that correlation function are obviously much the same thing. Um, you know, a gas is incompressible because the position of one particle doesn't tell you anything about the positions of the other particles. So you could call that first stage a Turing gas, which is what Walter Fontana-

**Host** [48:35]: Okay

**Blaise Aguera Y Arcas** [48:35]: ... uh, who is, you know, also a pioneer in, in abiogenesis, uh, you know, on computer called it. But then after that phase transition, it's something else. It's no longer a gas. Uh, I would call what you get afterward computronium, meaning it is-

**Host** [48:49]: [laughs]

**Blaise Aguera Y Arcas** [48:49]: ... a new phase of matter-

**Host** [48:50]: Yeah

**Blaise Aguera Y Arcas** [48:50]: ... if you like, that, that is all about computation. Uh, which I, I think another word for that is life.

**Host** [48:55]: You're listening to this podcast, so I know you've got a curious mind. Here's a helpful fact you might not know yet. Drivers who switch and save with Progressive save over $900 on average. Pop over to progressive.com, answer some questions, and you'll get a quick quote with discounts that are easy to come by. In fact, 99% of their auto customers earn at least one discount. Visit progressive.com and see if you can enjoy a little cash back. Progressive Casualty Insurance Company and affiliates. National average 12-month savings of $946 by new customers surveyed who saved with Progressive between June 2024 and May 2025. Potential savings will vary.

**speaker_7** [49:34]: [upbeat music] This episode is brought to you by SoFi, the all-in-one finance app to bank, borrow, and invest. Say goodbye to account fees and give your bank balance a glow-up with a SoFi high-yield savings account. Get over eight times the national average savings rate and an epic welcome bonus when you sign up with eligible direct deposit. Sign up at sofi.com/sxm. SoFi checking and savings offered through SoFi Bank NA, member FDIC. Terms apply.

**Host** [50:02]: Yeah, no, I mean, I'm, I'm, uh, on the train. I guess the one thing that I don't... If I, if I wanted to be the skeptic or at least the curmudgeon worrying about chemistry and things like that, um, a computer program where you have some instructions to change what's on the tape seems to be lacking some notion of energy or a Hamiltonian or dissipation or entropy or something like that. So ordinarily, when I have a phase transition, you know, I'm thinking of, oh, the system has found a lower energy configuration it can be in. But you don't, you don't have energy, or, or do you?

**Blaise Aguera Y Arcas** [50:37]: Not, not in any obvious sense. Um, so, um, you know, this, this is, uh... Nothing is conserved in, in, uh, in BFF.

**Host** [50:46]: Right.

**Blaise Aguera Y Arcas** [50:46]: Uh, bytes aren't conserved. Uh, time isn't... You know, uh, everything is, everything is just infor- just pure information. Um, so one can talk about entropy, but one can't talk about energy. Um, however, um, there is, there is a, a, I think, a, a deep connection with, with energy in the real world, which is that we know that computation requires energy.

**Host** [51:07]: Mm-hmm.

**Blaise Aguera Y Arcas** [51:08]: Um, now, there is this whole field of reversible, uh, so-called reversible computation, but the way you get reversibility in computation is by having these so-called ancilla bits-

**Host** [51:18]: Yeah

**Blaise Aguera Y Arcas** [51:18]: ... extra information that comes out that you have to store somewhere.

**Host** [51:21]: Right. You make the system bigger. [laughs]

**Blaise Aguera Y Arcas** [51:23]: And you have to erase. Yeah, exactly. So in a way, it's just saying, like, we shrink the part of the system we look at, you know-

**Host** [51:27]: Right

**Blaise Aguera Y Arcas** [51:27]: ... in, in such a way that we're not looking at the, [laughs] you know, at the extra information. So I, I think, uh, to make a long story short, I think there is something profound about computation that requires, uh, energy use because of its irreversibility, because computational operations involve these irreversible steps.

**Host** [51:44]: That makes perfect sense to me, but I, I can't quite in my brain connect it to the robustness and survivability and, uh, you know, hegemonic aspirations of your [laughs] reproducing codes. The, the... Why, why... Is there a physics-based way of saying why they want to take over? There, there need not be, but I'm just wondering.

**Blaise Aguera Y Arcas** [52:03]: Well, I think that the reasons they want to take over are purely statistical. So in that sense, you know, you, you don't have to invoke energy. You can just invoke statistics, you know, uh, likelihoods of finding something later, you know, if you find it in the present.

**Host** [52:15]: Right.

**Blaise Aguera Y Arcas** [52:16]: But in, in real life because, because heritable replication requires computation, right? In other words, you can't have a von Neumann replicator without it being made out of Turing machines that are computing. That means that you need an energy input in order to get a replicator. So that's why metabolism is required, uh, in, in real life to, uh, to have replicators.

**Host** [52:38]: Maybe this is another... Maybe this is a weird out-of-the-field question, but... Or maybe I'm answering myself in my brain because you already said there's no conserved quantities here. But ordinarily, when I take a physical system and just let it go, eventually it will reach equilibrium, right? I mean, it loses all structure. The, uh... I wrote a paper with Scott Aaronson once where we showed that complexity can grow for a while, and then eventually it, it's gotta fade away 'cause you're gonna equilibrate. But I'm thinking that in your thing, it's gonna remain in this fun, complex phase more or less forever.

**Blaise Aguera Y Arcas** [53:07]: It will, and, and the reason is that it's a dissipative system.

**Host** [53:11]: Yeah. Okay.

**Blaise Aguera Y Arcas** [53:11]: So the fact that it's computing, the fact that you're, that you're constantly computing means that effectively there is energy constantly going in. Uh, like a-

**Host** [53:17]: So you have a, you have a resource. You have the sun. [laughs]

**Blaise Aguera Y Arcas** [53:19]: Yeah. Yeah.

**Host** [53:20]: Yeah.

**Blaise Aguera Y Arcas** [53:20]: I mean, that's why, that's why the fan is going on my computer-

**Host** [53:22]: Exactly. Okay

**Blaise Aguera Y Arcas** [53:22]: ... when I'm running BFF, right? [laughs] But, uh, it... but it won't... So yeah, it won't, it won't... Uh, the order will not go away. Uh, the, the structure will not go away, but neither will it stabilize, uh, to, uh, to just one thing. So, you know, it's this very complex ecology, and what is so wonderful about what happens after this transition to life is that you might think naively, oh, one replicator takes over and that's it. It's just a crystal of that one thing. It's not. You have this whole kind of power law distribution-

**Host** [53:49]: Ah

**Blaise Aguera Y Arcas** [53:49]: ... of different replicators all interacting with each other, and they keep evolving forever and changing.

**Host** [53:54]: Wonderful, and it, and it does remind me that, uh, it's probably now time for you to tell us what BFF stands for.

**Blaise Aguera Y Arcas** [53:59]: [laughs] Well, the first BF still s- still stands for brain fuck. [laughs]

**Host** [54:03]: [laughs]

**Blaise Aguera Y Arcas** [54:03]: So given that it's interactions between two tapes, you might be able to guess what the second F stands for as well.

**Host** [54:07]: Very good. We'll leave that to the imagination.

**Blaise Aguera Y Arcas** [54:09]: Um, but, or, or we could just say best friends forever. [laughs]

**Host** [54:11]: Best friends forever. That's, that's even better. Okay, good. Um, z- now let's, let's try to relate this to questions that are sometimes raised about the origin of life. Like, is it... Does it require fine-tuning of the laws of physics? Did y- Are there free parameters in your process that could've been changed and made the results different?

**Blaise Aguera Y Arcas** [54:30]: Yes. Uh, so there is one thing that went in, which is the design of the language. Um, and we do know that different designs of language result in, um, either very different times to abiogenesis or in some cases, um, we don't see biogenesis at all, uh, which I think means just that the time is so long that we're, you know, that we're not able to, uh, to see it happen.

**Host** [54:54]: Okay.

**Blaise Aguera Y Arcas** [54:54]: So, uh, you know, one could almost write a theorem. In fact, one could write a theorem that just abiogenesis will happen in this kind of environment. In an environment, in other words, where computation is possible and where there's a noise source and where there are interactions, it will happen. But, um, but the question is, how long statistically will it take?

**Host** [55:11]: Right.

**Blaise Aguera Y Arcas** [55:11]: Uh, right. And, and, and details of exactly what the instruction set is, um, can, can make that vary quite a lot. Um, one of the, one of the really profound results, uh, of this that is not in the original paper but that, that I, I feel like we've just figured out, you know, again, in the, in the last, um, few weeks actually, is that, um, you know, there's a classic view of evolution that it all happens via Darwinian selection. Uh-

**Host** [55:36]: Mm-hmm

**Blaise Aguera Y Arcas** [55:36]: ... Jacques Monod, you know, the one of the, one of the winners of the Nobel Prize, you know, is famous for saying, like, it's just chance and necessity. You know, just have random mutations and, and, and Darwinian selection, whatever sticks. You know, uh, it's spaghetti being thrown at the wall. It's a million monkeys, uh, you know, and a million typewriters, and eventually, you know, uh, you know, things stick and there's a ratchet. So we now know that that's not how this works. Um, and, and there's, there's been a kind of rising tide of skepticism about that, about that very reductive Darwinian view for many years, but I think we now kinda have the receipts.

**Host** [56:09]: Okay.

**Blaise Aguera Y Arcas** [56:09]: So, [chuckles] uh, so what is actually going on, and, and well, I should say, what, what is, what are the receipts? The, the most obvious receipts are that if you turn the mutation rate all the way down to zero in BFF, uh, and you just start with 1,000, you know, random, uh, random tapes of length 64, and you let it go without any mutation, you still get complex life arising, and that's kind of mind-blowing because, you know, a, 1,000 times 64, like 64,000 random bytes, that's just not a lot of monkeys and not a lot of typewriters.

**Host** [56:38]: Right.

**Blaise Aguera Y Arcas** [56:38]: You know, there, there, there aren't enough characters there. You can barely find, you know, three working instructions in a row.

**Host** [56:44]: So sorry, there's still randomness in the, in the sharing between nearest neighbors, but there's not randomness in mutations.

**Blaise Aguera Y Arcas** [56:50]: Right. So there's randomness in the initialization.

**Host** [56:52]: Good.

**Blaise Aguera Y Arcas** [56:52]: Uh, right, you start off with random bytes.

**Host** [56:54]: Yeah.

**Blaise Aguera Y Arcas** [56:54]: And there's still randomness in choosing, uh, neighbors to interact, in choosing which ones to interact with, although frankly, I'm pretty sure you could get away with that too.

**Host** [57:02]: Okay.

**Blaise Aguera Y Arcas** [57:02]: I mean, you could just say everybody interacts with everybody, and we just, you know, go on that way. That would work just as well for sure.

**Host** [57:07]: So the, so the only randomness would be in the initial configuration.

**Blaise Aguera Y Arcas** [57:11]: Yes. Yes, and that just doesn't seem like enough randomness to generate these very complex programs that come out, so what's going on? Um, well, when you look closely at what's going on, what you see is the following. Um, first of all, when, uh, even, even from the very beginning, before a replicator arises, you already have individual instructions forming autocatalytic sets, meaning if you have a copy instruction, for instance, then, uh, you know, there is some possibility that what it generates is also an instruction. If there's a no-op, if there's a, if there's a non-instruction, there's no possibility for it to make anything, right? But if it's, if it's an operation, then there's a possibility that what it will make is another instruction, and maybe that other instruction will come back around, you know, and eventually make another of, of it. So in other words, you already have the makings. Like, the, the most primitive life forms, in a sense, are literally just single instructions.

**Host** [58:04]: Yeah.

**Blaise Aguera Y Arcas** [58:04]: And, and they begin to beget each other. You know, instructions beget instructions. You start to see the number of computations rising, if you look closely, right from the very beginning. And, uh, and, and they be- and so you begin to see more instructions coming in and, and they're kind of moving around at random. You know, they're copying themselves into random spots and, and it's a creative process because once in a while, if a couple of them end up in conjunction and together they can replicate more effectively than they could separately, then they're likelier to survive. So you get symbiosis, uh-

**Host** [58:36]: Mm-hmm

**Blaise Aguera Y Arcas** [58:36]: ... really as the driver of evolution. You know, the symbiosis between instructions to, to make little tiny programs, symbiosis between those little tiny programs to make bigger imperfect replicators, and, and eventually those, uh, those bigger imperfect replicators, which are all madly writing over each other, competing, cooperating, will eventually fuse into a, into a stable whole tape replicator. So it's symbiosis all the way down.

**Host** [58:59]: Right. Okay, good. So if the, if the audience will indulge me in being a little specific here because you're, you're provoking me to think of new theorems to prove because in that case that you thought about where there's, uh, or either there's no randomness in the interactions, okay? There's only interac- uh, randomness in the initial conditions, then the evolution is deterministic, right?

**Blaise Aguera Y Arcas** [59:25]: Yes.

**Host** [59:25]: So in that case, if, if you think that that will, with high probability, lead to this takeover by replicators, then there is some statistical mechanics statement, right? It's not saying that most instruction sets are replicators, but the future trajectories of most instruction sets will, you know, end up in this replicator-dominated regime.

**Blaise Aguera Y Arcas** [59:46]: Yes. It's telling you that computing is a dynamical attractor.

**Host** [59:49]: Yes. I like that.

**Blaise Aguera Y Arcas** [59:50]: Uh, and it's a dynamical attractor because only by having computing can you get replication, and replication is a, um, uh, uh, is a dynamically kinetically stable state.

**Host** [60:01]: Because the evolution is not reversible, right?

**Blaise Aguera Y Arcas** [60:05]: Right. Right.

**Host** [60:05]: Okay. So you can get attractors and, and, and you do. Good. I would like to see that theorem. That, that would be a good one. I'm looking forward to that coming out.

**Blaise Aguera Y Arcas** [60:11]: If, if you are, if you are game to work on, on the, on the theoretical physics of this, um, we are, uh, w- we would love that.

**Host** [60:19]: Let's talk. I'm, I'm, I'm potentially... I don't know whether I'm competent, but I'm super-duper interested, so good. Um, well, that's very good.

**Blaise Aguera Y Arcas** [60:25]: It's very, it's very Santa Fe for sure. [chuckles]

**Host** [60:26]: It is, absolutely. Right. Um, so what, at the end of the day, how grandiose can we be about drawing implications from this study? For example, for how easy it is for life to form in the more conventional wet and sloppy, uh, biological sense.

**Blaise Aguera Y Arcas** [60:44]: Well, I think that, um, I think that there are a lot of pretty grandiose conclusions, which is why this is a, this is a whole book. So first of all, uh, it seems to me that life wants to form.

**Host** [60:55]: Yeah.

**Blaise Aguera Y Arcas** [60:55]: Uh, you know, it's, it's, it's not, uh, it's the very opposite of, of what, um, you know, Francis Quick- Crick once said about, you know, like, life being a, like a miracle. You know, like-

**Host** [61:04]: Yeah

**Blaise Aguera Y Arcas** [61:04]: ... it's, it's hard to imagine how it could possibly happen. I think it's the opposite. Because computation is a dynamical attractor, um, I think that it, it will form whenever it has a chance to. Um, and, um, and I guess, you know- As we start to explore the moons of Jupiter or, you know-

**Host** [61:19]: Mm

**Blaise Aguera Y Arcas** [61:19]: ... or, or, or have better telescopes or whatever, maybe, maybe we'll start to see real evidence of that. Um, furthermore, uh, I, I think we can say that, uh, because symbiosis is the, is the driver of evolution, there's this kind of ladder wherein, uh, you know, more complex entities, uh, form out of simpler entities, and I think that's a very general property as well. Lynn Margulis, uh, you know, famously thought that this was the way evolution worked. You know, she, she was the discoverer of, you know, of, of mitochondria-

**Host** [61:49]: Yeah

**Blaise Aguera Y Arcas** [61:49]: ... having been endosymbiotic and, you know, and, and, and thereby forming eukaryotes. She believed that all sorts of things, um, you know, all of the organelles of the cell had been free-swimming originally. She was wrong probably, but, but I think she was right at a deeper level in the sense that, you know, the idea of an organelle evolving inside a cell, it's still an evolutionary step of a symbiotic character whether or not it began on the outside, right? The inside of a cell is just as fertile an evolutionary, uh, landscape as the outside. And, and in fact, um, you know, I, I haven't... I, I'm realizing I haven't mentioned this, but even after that transition to full tape replication, we see the amount of computation continuing to rise. The number of characters that compute still continue to rise, and the reason is that when the whole tape is getting replicated, not all of it is needed for, for the, uh, for the instructions that do the replication. So it's an e- it's an ecology, if you like-

**Host** [62:38]: Mm-hmm

**Blaise Aguera Y Arcas** [62:38]: ... where this whole process can, can repeat. And, and you get replicators inside replicators, and sometimes those will confer resistance to mutation-

**Host** [62:46]: Right

**Blaise Aguera Y Arcas** [62:46]: ... to the larger replicator and so on.

**Host** [62:48]: So okay. So I think that I would, I would sort of tentatively conclude that we haven't learned much about the robustness of the origin of life to changes in the laws of physics, right? Because if you change the laws of physics of our world, that'd be like changing the instruction list or whatever and, and maybe you would just get something that produces nonsense or, you know, only has one instruction. But given that we know the laws of physics, uh, I think y- y- you're making a strong but plausible claim that this should increase our credence that life's gonna pop up everywhere, some kind of life. Maybe not intelligent technological life, but some kind of complex computing life.

**Blaise Aguera Y Arcas** [63:25]: Right. I mean, there are barriers to every symbiogenetic transition.

**Host** [63:28]: Right.

**Blaise Aguera Y Arcas** [63:29]: Um, you know, and they're statistical. But, um, uh, and, and they could be of varying sizes, right? Those steps can be of varying sizes, so you're not guaranteed that you'll make your way all the way up the staircase, as it were. But, um, but there's a, there's a real tendency to go up the staircase. Uh-

**Host** [63:43]: Right. Okay, good

**Blaise Aguera Y Arcas** [63:45]: ... and, and, and every time you go up to the next step, you know you have a chance to get to the next step. Now, as for the, as for the laws of physics, um, I mean, we know that, that the laws of physics in our universe allow computation. So that means that, you know, if you like, there are many no-ops, right, in the universe, many interactions that, that, that are not part of a, um, of a set of operations that, that form a Turing-complete set and, and thereby, uh, also form an autocatalytic set. Um, but, you know, if there is an autocatalytic set in there that is Turing-complete, that's sufficient. And, and we know that, that, uh, you can make a computer out of almost anything-

**Host** [64:21]: [laughs]

**Blaise Aguera Y Arcas** [64:21]: ... right out of, out of, uh-

**Host** [64:21]: We've, we've done it. We've made computers-

**Blaise Aguera Y Arcas** [64:23]: Yeah

**Host** [64:23]: ... out of things. That, that's an existence proof. Yeah. Okay, good.

**Blaise Aguera Y Arcas** [64:26]: Exactly.

**Host** [64:26]: Does it... This is probably unfair, but does it give us any inspirations for how to look for life elsewhere?

**Blaise Aguera Y Arcas** [64:36]: That's a great question. Um, and it's definitely something I've been thinking about. Um, there are relationships between these ideas and some of the ideas of Lee Cronin, Sarah Walker, um, uh, constructor, uh, theory or assembly theory, sorry.

**Host** [64:50]: Assembly theory.

**Blaise Aguera Y Arcas** [64:51]: Assembly theory. Um-

**Host** [64:52]: Might also be connections to constructor theory-

**Blaise Aguera Y Arcas** [64:54]: Constructor theory too-

**Host** [64:55]: ... which is-

**Blaise Aguera Y Arcas** [64:55]: Yeah, which is a whole-

**Host** [64:56]: ... which is Marlitto, yeah.

**Blaise Aguera Y Arcas** [64:56]: That's right. So Mar- so Chiara Marlitto's work with c- with constructor theory also very relevant here.

**Host** [65:00]: Right.

**Blaise Aguera Y Arcas** [65:01]: Uh, so yeah, those are connections that have yet to be really fleshed out. Uh, so s- so Sarah, you know, um, and, and Lee believe that, that there are, uh, there are implications for how to look for, um, uh, for complexity elsewhere. Um, I think that assembly theory is quite compatible with, with what I'm describing. Um, I don't know if what I'm describing adds more, um, adds more meat to what we should be looking for observationally. It might.

**Host** [65:27]: Okay. Fair enough. And I, I would be remiss if I didn't give you a chance to talk about the many other things you do. I mean, this is kind of not your... It has not been, like, your main job title, uh, you know, and, uh, and you're writing books about all sorts of things. I mean, how should we segue into this? Should we t- talk about what is intelligence since we talked about what is life?

**Blaise Aguera Y Arcas** [65:45]: Sure. Um, so, uh, I mean, there, there is a reason that, um... A- And you're right. I... You know, abiogenesis and origins of life are definitely not my field.

**Host** [65:54]: [laughs]

**Blaise Aguera Y Arcas** [65:54]: Um, and, uh, you know, I've been working on it for less than a year. [laughs] But-

**Host** [65:58]: Got it

**Blaise Aguera Y Arcas** [65:58]: ... um, however, um, you know, our, our group, um, uh, has been working in, in ALIFE-related stuff for a while. So, um, uh, Alex Mordvintsev, who I mentioned earlier, um, is also the inventor of neural cellular automata, for instance, which, uh, which were a very beautiful kind of mashup of cellular automata as invented by, by von Neumann-

**Host** [66:22]: Mm-hmm

**Blaise Aguera Y Arcas** [66:23]: ... and, um, neural nets, uh, and uh, and also morphogenesis, uh, which, you know, really was pioneered by Alan Turing. So the idea behind NCAs, behind neural cellular automata, is that you have a, a grid of pixels, and in every pixel you have a neural net. It's the same neural net everywhere. And, and it senses and modifies the local concentrations of a handful of channels. Uh, those channels are scalar values. You could think about them as morphogens-

**Host** [66:49]: Okay

**Blaise Aguera Y Arcas** [66:49]: ... meaning as chemic- chemicals that, that, um, you know, that, that allow cells to communicate with each other. And you can train one of these NCAs to make any image you want. The first one that I ever saw was like a, a lizard emoji, and you could like wipe out its head as well as its tail, and it would regenerate itself. So it's kind of... It's, you know... It, it... So it's essentially a model for morphogenesis-

**Host** [67:08]: Right. Right

**Blaise Aguera Y Arcas** [67:09]: ... um, that, that, um, that combines, uh, cellular automata with, with, with neural nets. So we've been thinking quite a lot about local computation, uh, both because it's, it's a, a way to Uh, attack efficiency, uh, in, in AI computing and, you know, ultimately all computing has to be, has to be primarily local or oth- or it's gonna be inefficient. Um, and also as a way of, of thinking more broadly about, about learning. Um, you know, because obviously life is all about learning in some sense, right? The, the whole point of, of a, of a replicator is to produce more of itself in its environment. And as that environment becomes more complex and includes many other replicators, um, this kind of dynamical modeling starts to become more and more a part of it. So, you know, there, right, if you just keep walking along this symbiotic path, you, you know, you get eventually to brains and, and to AI.

**Host** [68:00]: Mm-hmm. I guess in your model, in the model we've been talking about in the paper so far, the quote unquote environment is just sort of the nearest neighbors of each tape. But a possible next step would be to, like, throw in an environment, like to have just different... I don't even know what they would be. But how would you, how would you model being on a planet versus not being on a planet, or being in the ocean versus being on land? I don't know.

**Blaise Aguera Y Arcas** [68:25]: It's, it's a great question. Uh, and, uh, there, there are, um... You know, we've, we've, we've definitely sort of thought about and tried out a little bit, um, some approaches like particle NCAs plus BFF.

**Host** [68:37]: Mm. Mm-hmm.

**Blaise Aguera Y Arcas** [68:37]: Um, particle NCA is, you know, like a, like a neural cellular automaton, except that there are particles that can move around rather than just pixels that stay put. Um, so yeah, I... You know, th- those are, those are all exactly the kinds of mashups that we'd like to try. Actually, the, the Z80, uh, simulation, uh, w- you know, s- that, that doesn't use Brainfuck but uses the Z80 assembly language instead, uh, it actually works, works on a grid. So it's a grid of 20- of 200 by 200 processors, and their interactions are all nearest neighbor rather than random. Uh, and you get these spreading waves of replicators of different species and stuff.

**Host** [69:10]: Right. And is there a video? [laughs]

**Blaise Aguera Y Arcas** [69:12]: There is, yeah. Um-

**Host** [69:13]: Okay, good. I'll have to look for that.

**Blaise Aguera Y Arcas** [69:15]: Yeah. I think, I think Alex is just putting it up on the web now. So, um, so yeah, I'll, I'll, I'll send you the URL.

**Host** [69:22]: Yeah. I mean, there is this remarkable universality in these kinds of videos, but also just the concepts behind them of phase transitions and domains, of things growing, whether it's the Ising model or the Schelling model in social sciences and everything, you know. That it does attract a certain Santa Fe Institute kind of person to think there must be connections. There, it can't, it can't all just be coincidence, right? There must be ways of thinking about this that are higher level and, and bring everything together.

**Blaise Aguera Y Arcas** [69:53]: Yeah. I think so. Um, I mean, I, I've, I've thought for a long time that intelligence is fundamentally symbiotic in the sense that the social intelligence hypothesis holds that, you know, we are smart because our environment is each other.

**Host** [70:06]: Mm.

**Blaise Aguera Y Arcas** [70:06]: And, and, and because you're constantly trying to model others, um, you know, and, and, and thereby also model yourself and how others see you and, and so on, um, you end up with these intelligence explosions precisely because our environment is each other. So there's a, I think there's a deep continuity between this, these very, very primitive, you know, replicating programs-

**Host** [70:26]: Yeah

**Blaise Aguera Y Arcas** [70:26]: ... and that, and that perspective.

**Host** [70:28]: Of the many previous podcasts that I've had that are relevant to what you just said, uh, Hugo Mercier, do you know his work?

**Blaise Aguera Y Arcas** [70:35]: Yeah. I do. Yeah, the Mercier and Sperber book-

**Host** [70:37]: Right

**Blaise Aguera Y Arcas** [70:37]: ... The Enigma of Reason, um, is, uh, you know, it's, it's one that I cite in my book and, and, uh, I'm, I'm, uh, I very much agree with, with their-

**Host** [70:45]: Yeah. [laughs]

**Blaise Aguera Y Arcas** [70:45]: ... their ideas about language.

**Host** [70:47]: And so you're pointing in the direction of saying that not only life but intelligence might be more ubiquitous than we think with obvious connections to we're building intelligent-like things. So, so what, what is your take on the intelligence of modern AI models?

**Blaise Aguera Y Arcas** [71:04]: Well, um, you know, when, when, um, when we first began working on, um, on AI, you know, I, I think a lot of people weren't thinking about social intelligence and they were just thinking about tasks. And, uh, so there was this long period... Well, I, I don't wanna go through the whole history of AI, but the supervised learning era-

**Host** [71:24]: Mm

**Blaise Aguera Y Arcas** [71:24]: ... was all about, uh, you know, training models to optimize something. And, um, I mean, you might notice that BFF is not optimizing for anything.

**Host** [71:32]: Right.

**Blaise Aguera Y Arcas** [71:33]: Yes, it tends statistically right toward, like, what persists exists, but there's not a... We haven't defined a task.

**Host** [71:39]: Yeah.

**Blaise Aguera Y Arcas** [71:39]: And, and, um, and, and the interesting thing about, about AI that was specific to doing a task is that the best it can do is to do that task. You know, so that's why we needed the term AGI. You know, originally AI meant, uh, you know, something you could have a conversation with that could do all the various kind of things that we do, um, that could fold the laundry, walk the dog. And, um, you know, and then people started talking about AI as speech recognition, uh, face recognition, you know, and, uh, character recognition, and it was like, that's not, that's not AI. You know, that, that's, that's just, um [laughs]...

**Host** [72:11]: [laughs]

**Blaise Aguera Y Arcas** [72:11]: Right. And, and, and the, the moment we actually came up with real AI was the moment we stopped optimizing for specific tasks and started to just model, um, uh, free-form text on the internet.

**Host** [72:23]: Mm.

**Blaise Aguera Y Arcas** [72:24]: Now, text on the internet is obviously not everything, but it, it, but, but language is special in the sense that it represents, uh, everything in our umwelt that we care about enough to talk to each other about.

**Host** [72:36]: Right.

**Blaise Aguera Y Arcas** [72:36]: So, you know, it's a microcosm, right, of, of, of everything, and it's just modeling that. It's just trying to predict next tokens, which, which amounts to building a, a model of that entire distribution, and that was intelligent.

**Host** [72:47]: Mm-hmm.

**Blaise Aguera Y Arcas** [72:47]: Uh, I, I am, um, you know, I'm definitely not in the majority on this, but I believe that, that, um, today's AI models are absolutely intelligent. Um-

**Host** [72:55]: Okay

**Blaise Aguera Y Arcas** [72:56]: ... you know, there's a lot of talk about it's, you know, it's just next token prediction, it's just this, just that. I, I mean, I think brains fundamentally are about predicting the future. And, uh, and the moment we just started to try and model that, you know, lo and behold, we got out stuff that is smart.

**Host** [73:11]: Right. So your attitude is not that large language models s- you know, mystically are more than next token prediction, but rather that our brains are secretly next token prediction. [laughs]

**Blaise Aguera Y Arcas** [73:21]: Yeah. Uh, although, although the just, you know, it conceals a lot of-

**Host** [73:26]: A lot. I get it, yeah

**Blaise Aguera Y Arcas** [73:26]: ... beauty and complexity. [laughs]

**Host** [73:28]: [laughs]

**Blaise Aguera Y Arcas** [73:28]: Right. I mean, in order to do a good job of predicting the future, you have to generalize, and, and, you know, generalizing means building internal representations and doing all sorts of very sophisticated-

**Host** [73:37]: ... uh, modeling. So my line has always been that LLMs in particular are not designed to think in the same way as human beings do, but rather to sort of mimic the output of, of human thought. Uh, and maybe it is possible that in the process of mimicking the output of human thought, they end up thinking like us. Uh, I- to me, there are enough counter examples of, you know, simple questions you can ask that any human could answer, but the LLMs fail at to assure me that that's not what's going on right now. But I don't know. You know this game a lot better than I do.

**Blaise Aguera Y Arcas** [74:13]: Well, it's, it's very much a moving target. Um, you know, I, I mean, there's, there's a lot of gotcha-ing, [laughs] you know, happening on the internet in the last, you know, year of like, "Oh, look at this stupid thing that the LLM said," [laughs] you know? Um, I- to be honest, uh, you know, one of my first reactions when I started to see that kind of stuff is, boy, these, these models are getting hammered.

**Host** [74:33]: [laughs]

**Blaise Aguera Y Arcas** [74:33]: I can only imagine what would be happening if I were somehow able to be replicated a billion times and, you know, get hammered with questions and, and need to respond immediately, and like how many gotchas you would find in that. You're like, the null distribution, let's put it this way, has not been well explored. [laughs]

**Host** [74:47]: Fair enough.

**Blaise Aguera Y Arcas** [74:48]: You know? Um, but, but, um, but I, I think the point is, is nonetheless right, that, you know, there, the, the profile of competencies and incompetencies looks pretty different from the average person's.

**Host** [74:59]: Right.

**Blaise Aguera Y Arcas** [75:00]: Um, and, and of course, I'm not arguing that everything, everything about the way they work is the same as the way brains work. Not at all. Uh, you know, uh, right, we have, we have a, a very different architecture. Um, you know, neurons are not the same thing as, as artificial neurons in, in, in neural nets. Um, the way we've evolved has a lot of path dependence. But nonetheless, I think that there is something profound about the functional standpoint, just as with life. You know, there is something deep that is going on-

**Host** [75:27]: Mm-hmm

**Blaise Aguera Y Arcas** [75:28]: ... which is about, about modeling your environment and predicting it and act- doing active inference on it, meaning that you're, you're, you're actively bringing about your own future as part of your actions. Um, and, and it was only when we started to, to in effect implement that kind of active inference that we began to get, um, uh, models that, that started to pass the Turing test. And the whole point of, of the Turing test is, you know, if, right, if, if, if the model behaves in all of these-

**Host** [75:53]: Right

**Blaise Aguera Y Arcas** [75:53]: ... ways, then-

**Host** [75:54]: Then she can

**Blaise Aguera Y Arcas** [75:54]: ... the function is right. [laughs] Yeah.

**Host** [75:56]: Right. I mean, are we... Uh, I think the answer is yes, but are we going to have to sooner rather than later confront the question of agency and rights to, uh, AI programs?

**Blaise Aguera Y Arcas** [76:09]: Well, th- I think the two are very different questions. So, um, uh, agency, yes. I, I think that, I think that, um, we tend to reserve the term agency for humans and, and, and, and even withhold it from, you know, animals and plants and so on, for reasons that are quite arbitrary-

**Host** [76:24]: Hmm

**Blaise Aguera Y Arcas** [76:25]: ... and, and that don't have a lot to do with anything you can really, you know, measure or, or study. Uh, so, you know, do plants have agency? Do mice have agency? Yes. Uh, do AI models have agency? Yes. Uh, you know, in particular, uh, you know, if you, if you start to have them, um... You know, I mean, uh, many of the, the respects in which they have little agency at the moment have more to do with how we have deployed them than they have to do with the models themselves. Um, you know, if it can only respond to a chat interaction, you know, and, and not make any moves of its own, as it were, then its agency is very limited. But that's not about, about the model. It's about, it's about how it's, how it's been, uh, embedded in the sociotechnical environment.

**Host** [77:06]: I think that's fair. I mean, I ask the question because I really don't know what the answer is, and I'm, I, I am curious. I, I would... I, I'd be very happy to attribute more agency to a good modern AI program than to a tree, [laughs] but I think that it might be low in either case. I'm not, I'm not sure yet. I, I could be convinced.

**Blaise Aguera Y Arcas** [77:23]: Well, um, you know, there's, there's a, there's a wonderful book, um, uh, that I, you know, I read years ago by, um, James C. Scott, the agronomist. Um, uh, the late, uh, James, James C. Scott, unfortunately. I think he's just died recently. But-

**Host** [77:36]: Right

**Blaise Aguera Y Arcas** [77:37]: ... but, um, it's called Against the Grain. And, um, you know, he, he questions whether we really domesticated, um, uh, wheat and, and, and other agricultural plants. Um, you know, the, the basic observation being human life got a lot worse after we began farming, and it o- and it has only recovered very recently.

**Host** [77:55]: Hmm.

**Blaise Aguera Y Arcas** [77:55]: Like very recently, [laughs] you know, since 1900 or so.

**Host** [77:58]: Yeah.

**Blaise Aguera Y Arcas** [77:58]: Um, and, um, there's a way of thinking about what happened in, in, in plant domestication that looks more like plants domesticated and even concentration farmed us, essentially. You know, they enslaved a lot of humans to do-

**Host** [78:12]: Uh-huh

**Blaise Aguera Y Arcas** [78:12]: ... you know, to, to plant massive, [laughs] you know, massive fields of them, uh, and take care of all of their, of all of their needs, uh, you know, um, at, at, at great expense, uh, to, to human health and, and well-being.

**Host** [78:23]: [laughs]

**Blaise Aguera Y Arcas** [78:24]: So I mean, I, I say this not because I'm necessarily, you know, strongly advocating that point-

**Host** [78:29]: Uh-huh. Yeah

**Blaise Aguera Y Arcas** [78:29]: ... of view, but because I think it's like a Necrocube. You can look at it both ways. You know, agency is not simple.

**Host** [78:34]: Well, it's the selfish gene idea, right?

**Blaise Aguera Y Arcas** [78:36]: Right.

**Host** [78:36]: I mean-

**Blaise Aguera Y Arcas** [78:37]: Right

**Host** [78:37]: ... and, and, and if we try to be a little bit less judgy about it and we start thinking in terms of the statistical mechanics of trajectories, then maybe it makes perfect sense that this sort of symbiotic relationship was... You, you, you can't at- attribute the causal agency to either one or the other by themselves.

**Blaise Aguera Y Arcas** [78:54]: Exactly. And, and one of, one of the points that, that Mercieca and Sperber make in their book, um, also, uh, Sloman, uh, et al., in The Knowledge Illusion, is that we tend to over-attribute, if you like, uh, agency to ourselves in a big, big way.

**Host** [79:07]: [laughs]

**Blaise Aguera Y Arcas** [79:07]: And not only over-attribute agency-

**Host** [79:09]: Yes

**Blaise Aguera Y Arcas** [79:09]: ... but, but over-attribute knowledge, understanding. We're like, "Oh, humans can do this, humans can do... Yeah, humanity is great at this, that, and the other." You know? I mean, the average New Yorker doesn't know how a toilet works.

**Host** [79:18]: Right.

**Blaise Aguera Y Arcas** [79:19]: Um, right? Uh, and, and would be, you know, useless, right-

**Host** [79:22]: [laughs]

**Blaise Aguera Y Arcas** [79:22]: ... if actually, you know, put out in the, in the jungle, [laughs] you know, to, right, to fend, to fend for themselves. So, um, I, you know, I, I think that, I think that it's, it's useful to rethink all of this. I'm not arguing for robot rights. I, I do wanna be clear about this. Um-

**Host** [79:34]: Well, no, but at some point we're gonna have to have a serious conversation about it, right? I mean, I guess that's the only, only... as far as I would be willing to go.

**Blaise Aguera Y Arcas** [79:42]: I, I do think that we're gonna have to have serious conversations about, um, about how we think about the relationship between, um, between human rights and the various things that we have reserved, uh, kind of, uh, to humanity as kind of copyrighted [laughs] you know-

**Host** [79:59]: Yeah

**Blaise Aguera Y Arcas** [79:59]: ... that only we've got. Only we've got agency, only we're intelligent, only we this and that. I mean, I'm, I'm okay with us making, you know, various political decisions about, you know, how we want humans to be treated as distinct from various other kinds of entities, but I think we should be honest with ourselves that a lot of that has to do with the fact that we are humans, uh-

**Host** [80:18]: [laughs]

**Blaise Aguera Y Arcas** [80:18]: ... you know, who are making these decisions. It's not, it's not, um, it's not some view from above wherein we deserve that because we've got souls and nothing else has a soul.

**Host** [80:27]: Well, maybe that's a perfect segue to the, like, uh, just the wrapping up kind of thing I wanted to ask about, which is your other book, Who Are We Now? Great title. Uh, we human beings, right? And comparing who we are now to maybe who we used to be. Who are, who are we now? What's the answer?

**Blaise Aguera Y Arcas** [80:44]: Well, um, you know, there's a connection between that book and, and everything we've been talking about, uh, which is that, you know, my view of the change in human identity, uh, that, that we have undergone over, over recent times, especially since the melting of the glaciers in the last 10,000 years, but accelerating, is, um, that it's all about urbanization. Uh, this is also a very Santa Fe idea.

**Host** [81:06]: Mm-hmm.

**Blaise Aguera Y Arcas** [81:06]: Um, and, and that we have become a collective superorganism. You know, human intelligence is, if you like, a kind of superintelligence that, uh, that has come about through us symbiotically working together in a new way that, uh, that we didn't, uh, for, you know, the first couple of hundred thousand years that, uh, that we've, that we've been around. So, um-

**Host** [81:27]: Hmm

**Blaise Aguera Y Arcas** [81:27]: ... so, you know, it, it's, I think it's another, it's exactly another of those transitions of the kind that we see in, in, in BFF, if you like.

**Host** [81:32]: Right.

**Blaise Aguera Y Arcas** [81:33]: Um, and, and we, uh, in, in not understanding that we've undergone that transition, we, we continue to confuse what human means, uh, you know, by, by attributing that larger collective thing to individuals when in fact it's something new.

**Host** [81:48]: I guess the only edit I would, uh, do there is you, you say having undergone the transition. I think we're in the middle of the transition. [laughs]

**Blaise Aguera Y Arcas** [81:55]: We're in the middle, yeah.

**Host** [81:55]: We're nowhere close to the end, which makes it even harder to figure out what the true, what, w- how to deal with it, I suppose.

**Blaise Aguera Y Arcas** [82:02]: I agree. I think we're in the... Yes, I, I, I overstated. We are in the middle of it, and I think a lot of our agita right now comes from being in the middle of it. Um, so, you know, even for instance, um, you know, um, to, to, to bring a little bit of geopolitics into it, um, when you and I were growing up, uh, we were in the middle of a hemispheric, uh, Cold War-

**Host** [82:20]: Uh-huh

**Blaise Aguera Y Arcas** [82:21]: ... of, you know, USSR versus the West, and you could imagine, uh, one of those collapsing and the other one, and the other one winning, right? There was a zero sum kind of thing there, and that's what happened. Um, so, you know, the, the economy of the USSR could collapse and, and that would mean that the West had won. Um, now, uh, if you look at the rhetoric of, uh, you know, say China versus the US, it is completely different because their two economies are intimately intertwined.

**Host** [82:45]: Hmm.

**Blaise Aguera Y Arcas** [82:46]: You can't have the Chinese economy fail and that be a good thing for the US or vice versa. So, uh, you know, we're kind of in it now at planetary scale, and yet we haven't quite understood that we have to be operating at planetary scale yet.

**Host** [82:59]: A different, uh, former guest of Mindscape is Henry Farrell, uh, and his phrase for that is weaponized interdependence.

**Blaise Aguera Y Arcas** [83:07]: Yes.

**Host** [83:07]: We, we, we have to learn to live along. It's a, it's a, it's not mutually assured destruction, but it's, uh, you know, if we, if we don't all succeed, then it's gonna be a, it's gonna be bad for everybody.

**Blaise Aguera Y Arcas** [83:17]: Right. What, I think what we have is mutually assured survival.

**Host** [83:20]: Yeah.

**Blaise Aguera Y Arcas** [83:20]: And, uh, and, and if, uh-

**Host** [83:22]: If we choose wisely

**Blaise Aguera Y Arcas** [83:23]: ... and if we, if we choose wisely. [laughs]

**Host** [83:24]: [laughs]

**Blaise Aguera Y Arcas** [83:24]: And if we, and if we don't choose wisely, then, then, you know, we're, we're... Yeah, we kind of can only go forward or back, right? We can't, we... I, I think we can't quite stay where we are.

**Host** [83:33]: That's a very set of wise words, very wise set of words, uh, to end on. I can't do any better than that. So Blaise Aguera y Arcas, thanks very much for being on the Mindscape Podcast. [laughs]

**Blaise Aguera Y Arcas** [83:42]: Sean, thank you so much. Wonderful, wonderful questions and, uh, and insights and thoughts and, um, and yeah, the door is wide open if you're interested in, in, uh, in working on this stuff.

**Host** [83:52]: Let, let me think and let's talk. I'm very interested. So all right, thanks.

**Blaise Aguera Y Arcas** [83:55]: Take care. [upbeat music]

**Host** [84:19]: Hi, Ryan Reynolds here for Mint Mobile. Are you looking for a beach read this summer? May I suggest your big wireless bill? It's got suspense, mystery, a slightly flat emotional arc, and a shocking twist where you realize you've been overpaying the entire time. Fortunately though, Mint's story is better. Every plan, $15 a month, even unlimited. That's it. Happy ending, zero tears. Give it a try at mintmobile.com/switch.

**speaker_8** [84:41]: Upfront payment of $45 for three months, $90 for six months, or $180 for a 12-month plan required. $15 per month equivalent. Taxes and fees extra. Initial plan term only. Greater than 50 gigabytes may slow when network is busy. See terms.

**Unknown** [84:49]: From lashes for days with the viral Liquid Lash Extensions mascara to lift and color from their brilliant eye brightener, Thrive Cosmetics is the go-to for amplifying everyday looks. Plus, every product is 100% vegan, cruelty-free, and made with clean, skin-loving ingredients that work with your skin. Amplify your everyday. Go to thrivecosmetics.com/shine26 for an exclusive offer of 20% off your first order. That's Thrive Cosmetics, C-A-U-S-E-M-E-T-I-C-S.com/shine26.

