---
title: "Blaise Agüera y Arcas on AI, Consciousness, and the Concept of Intelligence"
person: blaise-aguera-y-arcas
section: by
type: talk-transcript
year: 2025
venue: ""
source_url: https://youtu.be/Rdx9zAwhnXg
retrieved: 2026-08-15
content: full-text
transcription:
  method: asr
  asr_model: elevenlabs-scribe_v2
  diarized: true
  speaker_labels: inferred   # ASR diarization + LLM naming (claude-sonnet-4-6); not ground truth
  duration_min: 55
notes: "PROVENANCE: machine-transcribed from AV via ElevenLabs Scribe v2 (diarized) + LLM speaker-naming pass. Speaker labels are inferred, not authoritative. Layer-2 (mildly lossy) per charter, not camera-raw."
---

# Blaise Agüera y Arcas on AI, Consciousness, and the Concept of Intelligence

*Speakers (inferred):* speaker_0=Narrator, speaker_1=Interviewer, speaker_2=Blaise Aguera Y Arcas

## Transcript
**Narrator** [00:00]: [upbeat music] Welcome to Responsible AI, the podcast from the AI Forum. Here on the podcast, we engage in critical dialogue with legal minds and tech experts on AI's legal and societal impacts. We talk to professionals in cybersecurity, law, and technology, offering deep dives into public policy and best practices. Responsible AI is hosted by Alex Alban, director of the AI Forum, and me, your producer, Rebecca Staffol. You can learn more at our website, theaiforum.org. We're talking today with Blaise Aguera y Arcas. Blaise is a vice president and fellow at Google, where he is the CTO of Technology and Society and founder of Paradigms of Intelligence, known as Pi. Pi is an organization working on fundamental research in AI and related fields, especially the foundations of neural computing, active inference, sociality, evolution, and artificial life. In 2008, Blaise was awarded MIT's TR35 prize. During his tenure at Google, Blaise has innovated on-device machine learning for Android and Pixel, invented federated learning, an approach to decentralized model training that avoids sharing private data, and founded the Artists in Machine Intelligence program. Blaise has given multiple TED Talks and authored numerous papers, essays, op-eds, and chapters, as well as two previous books, "Who Are We Now?" and "Ubi Sunt." His most recent book, which we will discuss today, "What Is Life?" is part one of the larger book, "What Is Intelligence?" coming from Antikythera and the MIT Press in t- September 2025. Blaise, welcome to the Responsible AI podcast from the AI Forum, and hello, Alex Alban.

**Interviewer** [01:52]: It's great to, uh, have Blaise as, as our guest, and, uh, we have a lot to talk about. Blaise and I met when we were at a town hall Seattle event, which was discussing AI, but became, uh, quite philosophical in its, uh, explorations, and I would hope to continue, continue that in this podcast today. So Blaise, thank you for being here.

**Blaise Aguera Y Arcas** [02:16]: Thank you so much, uh, Alex and Rebecca, for having me on. I'm really honored.

**Interviewer** [02:21]: Uh, I'm gonna dive in. You have a new book called "What Is Intelligence?" And I thought that was very interesting, just the title, because most people who deal with the AI world get hung up on, how do we define artificial? They're very focused on the artificial part, and they never get to the intelligence part. [chuckles] You know, the predicate here is the key. What, what is intelligence when we're, when we're talking about this? So I love your title. How did you, how did you come up with your title and, and the idea for the book?

**Blaise Aguera Y Arcas** [02:53]: Well, I guess most of my-- I- in fact, all of my books so far have been question titles. I didn't actually realize that until recently. Even, even the first one, uh, "Ubi Sunt," which was kind of a pandemic-era fever dream novella, uh, the, you know, the, the title in Latin means, "Where are they?" So even, even that is a, is a, is a question, although it doesn't have a question mark at the end. So I guess I'm always motivated by questions. In the case of "What Is Intelligence?" there were two stimuli for that. One of them was that, you know, as you mentioned, there is a kind of book within the book, "The Hobbit" to "The Lord of the Rings," that is the whole thing, is "What Is Life?" which is a short book that's already out from, uh, MIT Press and Antikythera. And "What Is Life?" is an homage to an earlier book called "What Is Life?" by Erwin Schrödinger from the early 1940s, uh, one of the fathers of quantum mechanics. I, I think it's, it's at least the fifth or sixth book that's been called "What Is, What Is Life?" But, but, uh, but Schrödinger's, you know, is, is kind of the touchstone. And, uh, um, and I guess, you know, the, the subtitle of, of "What Is Intelligence?" is Lessons from AI About Evolution, Computing, and Minds. And I'm approaching this, you know, sort of not just as a, as a, an engineer or an AI researcher, but as a computational neuroscientist, uh, which was my first love, you know, as, as a researcher. And I think that making something is a great way to understand how it works. And the fact that we have now engineered AI, it doesn't mean, of course, that, that brains are exactly like what we've done in the computer, but there are, there are certainly some commonalities, there's some convergence evolution there, and I think we understand some basic things now about what intelligence is in all its forms, not just in the computer, but in our own heads through having built.

**Interviewer** [04:39]: Um, when you were in college or earlier, did you ever have an idea that this is what you would be doing at this phase of your life? [chuckles]

**Blaise Aguera Y Arcas** [04:48]: I did, actually. [chuckles]

**Interviewer** [04:49]: Oh.

**Blaise Aguera Y Arcas** [04:50]: Um, I mean, you know, my, my, my skills, I guess, you know, from a very young age were in, in computers and to a lesser degree in, in math and physics. You know, the, the reason that I went into, into computational neuroscience was because I felt like that was, that was the big frontier. Uh, understanding how, how brains and how intelligence work seemed like the most exciting thing to work on. Things haven't quite happened in the order that I imagined. I always thought we would have, uh, you know, colonies on the moon and space exploration and stuff like this done before we figured out how to make AI. And I also always imagined that we would figure out neuroscience in more detail before we actually made something intelligent. But we're in this funny state where, you know, our, our engineering, and in particular our engineering of intelligence systems, is a little ahead of our understanding of, of, of what intelligence is. And that happens sometimes too. I mean, I, I guess a parallel would be in the 19th century, we began inventing steam engines and, and figuring out steam power before we had really worked out thermodynamics. So, you know, that was a case where practice was ahead of theory. I, I feel like that's where we are now.

**Interviewer** [05:57]: For a neuroscientist, you really do a lot of ... historical research and exploration, which is evident in the book, What Is Intelligence? I found your history of computing to be very educational, and your exploration of the early, what we used to call calculators, and their efforts to understand logic, uh, super interesting because you put AI into a historical context. Why, why is that important when we talk about AI?

**Blaise Aguera Y Arcas** [06:27]: Thank you for enjoying that, that part of it. I, a part of it is self-indulgence. I'm just really into this stuff as well. I'm a, I'm a big dork. I love, I love the history of these steampunk machines and, you know, what, what happened with Babbage and Lovelace in the 19th century, what, what happened with the inventors of digital computers in the, in the early and mid-20th century. So a part of it is, is just my own tastes. But I do think that it's valuable also for understanding the, the big ideas because a lot of these big ideas go back a long way, much, much further than, than people appreciate. A good old-fashioned AI goes back to Leibniz, to the Enlightenment. And, um, I think in, in a lot of ways, the first people who arrive at some of these insights... I mean, of course, people like Leibniz or, or Turing or von Neumann or whatever are, are brilliant polymaths. But they also, I think, could see really far because they were the first ones to crest those particular hills at a moment when the environment was a lot less cluttered. You know, when, when you're sort of first and, and you can sort of, you crest the hill and you see the landscape, there's a clarity that comes from that, that I think can get lost through later development and later assumptions that get, that get piled on. So, you know, I've just found it incredibly enlightening to, you know, go back to some of these early sources and see just how much they already intuited, figured out. And in, in some cases, there are even lost insights there-

**Interviewer** [07:48]: Right

**Blaise Aguera Y Arcas** [07:49]: ... that, that have since, you know, that we're having to rediscover today.

**Interviewer** [07:54]: Just to go a little bit deeper in the, the his- history of computation, uh, you mentioned Ada Lovelace, who in and of herself is a, is a brilliant and mysterious figure who died far, far too young.

**Blaise Aguera Y Arcas** [08:08]: Yeah. An amazing figure.

**Interviewer** [08:09]: She was the one who did the equations for Babbage's difference engine, as you recount in your book. Isn't it interesting that women played such a critical role in the computational side of logic at a time when men were dominating all of science? What-- Do you attribute anything to the status of women or the lack of status of women at that period of time?

**Blaise Aguera Y Arcas** [08:33]: Yeah. It-- That is a really fascinating story. And when... I, I was really happy to see, um, a few years ago, Hidden Figures enter the, the popular imagination. You know, there, there was that really great movie, and, you know, I think a lot of people became aware of some of this history, uh, in, in, in ways that, that were sort of consciousness-raising. Um, What Is Intelligence? is not, is not, um, first and foremost a history or a work of feminism, but it definitely has some elements of that, especially in those historical parts. It is really interesting. It's noteworthy that Ada Lovelace was the first programmer. It's noteworthy that the first compiler was, uh, was made by Grace Hopper. It's, it's notable that the first programmers of the first computer, of the ENIAC, were all, were all women. There were six women in particular who were, who were part of the, the Moore School program and, and were the first programmers. It's notable that a bunch of the programmers of the computers at Los Alamos that did the first large scale simulations, in, in that case for, for the, for the H-bomb, were also women. Um, and you know, when you, when you really start looking at this, at this history, um, what you find is that the moment when programming becomes a male-dominated profession is basically the moment when, uh, it, when it becomes higher status and, um, and, and this idea emerges that it's a way to make bank. [chuckles] So, you know, this happens in the '70s, you know, and, and '80s, uh, in the kind of precursor, I guess, to the, you know, to the dot-com. You know, it was a, a tech boom. Uh, you know-

**Interviewer** [10:01]: Right

**Blaise Aguera Y Arcas** [10:01]: ... the first computing tech boom.

**Interviewer** [10:04]: Might go back down. I might go to the transistor development with Shockley and Brattain and Bardeen because at that point, that troika of men and the culture at Bell Labs at that time, I think was, was a very, to say business-oriented culture is a vast understatement. But it kind of elevated them into, "We are the titans of industry." And they, they were not a very friendly culture to women at that period of time-

**Blaise Aguera Y Arcas** [10:32]: Not at all

**Interviewer** [10:32]: ... the '40s and '50s.

**Blaise Aguera Y Arcas** [10:33]: Not at all. Yeah. And at that point, computing was seen as a hardware business. For IBM, the operating system was an afterthought, which is, you know, one of the reasons that Microsoft was able to kind of-

**Interviewer** [10:44]: Yeah

**Blaise Aguera Y Arcas** [10:44]: ... get in on it.

**Interviewer** [10:46]: On the cheap.

**Blaise Aguera Y Arcas** [10:47]: On the cheap, exactly. And so, you know, because it was undervalued, it was women's work. I mean, I think, I think that's kind of what it boils down to.

**Interviewer** [10:54]: Blase, I wanna, I wanna talk a little more about sex.

**Blaise Aguera Y Arcas** [10:57]: [chuckles]

**Interviewer** [10:58]: I was very interested in your tangent about biology and sex differences of organisms and how that actually helped develop intelligence on an or- organic level. Can you explain why that's significant?

**Blaise Aguera Y Arcas** [11:16]: Sure. This is a big topic, but I'll try and be, I'll try and be brief. Basically, you know, one of the theses that I advance in this book, and it's not, um, I'm not the one coming up with this for the first time. This is the, a lot of these are old ideas as, as we've just been talking about. But the idea of intelligence explosions, which is to say dramatic increases in, in the intelligence of, of a species as being socially driven. In other words, that we become smarter because we have to model ourselves and others. Our environment is each other. That happens whenever an organism becomes highly social and highly dependent on others. That sociality can be either a cooperative or adversarial. You know, predator-prey interactions are social in a way too. The predator has to model their prey, the prey has to model the predator to escape. But when cooperative sociality takes off among people, we We undergo an, an intelligence explosion in the hominin line. And the reason is that you've got to predict others in order to, uh, be able to understand what they know and don't know, what they will like and not like, what they will do and won't do, and you have to grow a bigger brain in order to do that. As that happens, you become harder to predict yourself, and so there's a kind of friendly arms race that takes place. The development of sex, uh, which, which as far as we know, goes all the way back to the emergence of eukaryotic cells, so it's really old. Like, there was sex before there were multicellular animals.

**Interviewer** [12:40]: Right.

**Blaise Aguera Y Arcas** [12:40]: Is it's one of those pivotal moments when, when living organisms become super dependent on each other. You know, you, you can't reproduce without, without others of your kind, and if those others of your kind are becoming intelligent, then you need to get smarter and smarter in order to model what is going on in their minds in order to get together with them. So-

**Interviewer** [12:59]: Right

**Blaise Aguera Y Arcas** [13:00]: ... you know, that chapter is called Love and War, and it's because, uh, you know, both adversarial and cooperative interactions, sex being one of the OGs of that, are drivers of, of, of social intelligence.

**Interviewer** [13:12]: Yeah, I found that to be really a fascinated passage. We're talking with Google fellow Blaise Agüera y Arcas and his new book, What Is Intelligence? We've already mentioned Alan Turing very briefly, um, and I, I've covered a lot of scientists and writers who always talk about the Turing test. I'm so glad you didn't focus on the Turing test because that really wasn't Turing's main contribution to the history of, of computation, right? He was a lot more focused on information theory, and maybe you can expand on that a little bit, the way you relate that to artificial intelligence.

**Blaise Aguera Y Arcas** [13:50]: Sure. Turing, Turing was an amazing figure. I mean, if, if the book has a single hero, it, it's, it's Alan Turing. Um, so yeah, his, I think his, his biggest contribution, um, the one that has had the longest repercussions, uh, is, is not the Turing test, which a lot of people now know about because of AI, but his 1936 work that introduced the concept of computing as a, as a rigorous concept. So, um, you know, there's this idea, actually, I, I, I guess, um, I, I first heard this articulated by James Gleick in, in his book, The Information, that certain quantities or concepts are pre-scientific, and then they become scientificized or whatever. They, they become, they, they're articulated clearly by some researcher, and thereafter they have a clear definition. So before Newton, you know, people argued about what force was. Before-

**Interviewer** [14:39]: Yeah

**Blaise Aguera Y Arcas** [14:39]: ... Shannon, Claude Shannon, people argued about what information was, you know, and then we had a clear definition. Before Turing, we argued about computation and what that meant. The, the Turing machine, and especially the universal Turing machine, which is Turing's, uh, kind of imaginary device consisting of a tape that there's a, you know, head that can move left and right on the tape, reading and writing symbols, is this kind of abstract machine that serves as a rigorous definition for what computing means. He actually invented that, that concept in order to answer one of the great unsolved mathematical problems of the time, posed by, by the great mathematician David Hilbert, about the computability of functions. But, uh, but that, that was the, the seminal contribution. But Turing also did, did a lot else. Uh, you know, not, not only did he, uh, really invent the idea of artificial neural networks, and thereby all of modern AI, he also, uh, discovered the biology of, of morphogenesis, of how organisms form themselves using chemical signals.

**Interviewer** [15:39]: Mm-hmm.

**Blaise Aguera Y Arcas** [15:40]: And many other contributions, as well as s- as well as saving many, many lives, by the way, in the Second World War w- by cracking the Enigma codes. Really a, a hero and a genius, I would say.

**Interviewer** [15:51]: Um, when you talk about Turing, you talk about his focus on theory and computation, and also the models that you bring up in your book. I think it's a very popular notion that the brain is a computer, but is that really the right question? Is the brain a computer? Is the computer a brain? Would that be the better question to ask in this context?

**Blaise Aguera Y Arcas** [16:15]: I think they're both good questions. Uh, and, and the answers c- uh, the answers go deep. A lot of people who say the brain is not a computer, you know, which is also a popular trope, you know, brains are not computers, I think misunderstand the definition of computation. You know, is the... Uh, or they think, or they think that talking about the brain as a computer is a metaphor, you know, in the same way that a lot of people used to talk about the brain as being a, a telegraph, you know, in the era, in that era, or as being a switchboard when, you know, it was telephones, or as being like a giant TV or something, or an engine, a steam engine. I mean, all of those are, are, are metaphors that have been used for the brain at various times. When Turing referred to the brain as, as a computer, or when I do, it's not metaphorical, it's literal. The brain is computational. It doesn't work the way, uh, you know, a laptop does. It doesn't have, uh, you know, a hard drive or an SSD. It doesn't have a central processing unit. Uh, you know, it doesn't, it doesn't use bits in the same way, um, or digital logic. But it absolutely computes in the sense that it consists of, of parts that communicate with each other. Those parts compute functions, and that's true recursively. It's true, you know, all the way down. All of computational neuroscience is predicated on the idea that by looking at what neurons do, for instance, and looking at how they communicate and, and, and how they transform their inputs into their outputs, we can understand what the brain does, how it functions. For me, what computing really means at its heart is functionalism, meaning that, that you can talk about what something does in an abstract way, such that if you replace the implementation with a different implementation that, that has the same interfaces to the things around it, it still works. And in that sense, all of life is very deeply computational. Uh, you know, when we do something like put somebody on dialysis, and it works as, as a kidney would, that's a functional replacement. We're saying like, you know, you're, you're, you're doing d- doing the same thing with totally different atoms, a different method, but that's a function that is needed for the rest of your body to work. Life is characterized by functions that depend on functions that depend on functions, unlike, say, a, a rock. You know, a, a rock doesn't break. If you break a rock in half, you have two rocks. You don't have a broken rock.

**Interviewer** [18:21]: [laughs]

**Blaise Aguera Y Arcas** [18:22]: But when you have a f- when you have functional relationships, if something breaks, the functionality breaks, and it matters to the other parts.

**Interviewer** [18:30]: There's a quote from your book, uh, Blaise, that I'm not sure I really understood, but it's related to this conversation. It's, "What we experience as consciousness may not be something that happens in the brain, but rather something the brain does, a way of modeling the world, including the self in time." Can you, uh, help me with that-

**Blaise Aguera Y Arcas** [18:50]: Yeah

**Interviewer** [18:50]: ... concept?

**Blaise Aguera Y Arcas** [18:52]: Yeah. I-- Consciousness is, is, is probably the most controversial thing that I touch on in this book, you know, and it's been y- of course, a, a huge, um, topic of debate in philosophy of mind and, and in many other fields, and one that is newly urgent in many ways with, with AI. Uh, a lot of people are asking the big C question. Um, so one way into this qu- one, one way into this one is, um, the so-called brain of Theseus, uh, which is a philosophical thought experiment that the philosopher David Chalmers and Susan Schneider as well have talked about, which is suppose that you take a neuron in somebody's brain and you replace it with a computer or a simulation, if you like, doing the same calculation, and somehow we're able to hook it in, you know, to the same inputs and outputs. The question is, would you notice the difference? And I think the answer is no. That you would not notice the difference. If we're right that, that what a neuron is doing, you know, is-

**Interviewer** [19:45]: Is a logic gate-

**Blaise Aguera Y Arcas** [19:46]: Is functional

**Interviewer** [19:47]: ... so to speak.

**Blaise Aguera Y Arcas** [19:48]: Right. Right. Then if you do that by other means, uh, but, you know, to, to everything around it, it looks the same because it has the same input and output, then, you know, it'll, it'll be the same. Um, what's so weird about that, though, is that if you then think, well, imagine that I place a million neurons or, or all of them. Do you notice the difference? And, uh, once again, I think, I think the answer is, is obviously no. Um, it's weird to think about because that means two things. It means, first of all, it kind of brings you face to face with the, with the idea that if you say yes, you're actually assuming that there's something like an immaterial soul or a spirit that, that, that goes beyond what's happening with, with the, with the atoms. And yet it simultaneously emphasizes that there is something abstract and non-material about what's going on because you've now... you're now using completely different materials, and somehow it's the same. That's, that's sort of the spooky heart of functionalism.

**Interviewer** [20:37]: Right. Right. I mean, it kind of leads into this discussion a little bit of sci-fi. I, um, when I was an entertainment lawyer, I worked very briefly on a movie called RoboCop, and-

**Blaise Aguera Y Arcas** [20:50]: A classic

**Interviewer** [20:50]: ... we were very interested in how much of the brain could be replaced before he lost his personality. And I thought this was just a fascinating question for a big, you know, movie. But they were much more interested in whether they could fit the actor into the suit that they had made, uh, because it had certain measurements, and you needed to find an actor who was exactly five foot nine, had, you know, 30-inch waist or something like that. Um-

**Blaise Aguera Y Arcas** [21:21]: The actor wasn't the, wasn't the priority. [chuckles]

**Interviewer** [21:23]: Exactly. And then I think the movie suffered a little bit-

**Blaise Aguera Y Arcas** [21:26]: Yeah

**Interviewer** [21:26]: ... uh, frankly. Um, you know, Hollywood tends to paint, uh, AI in extremes. Uh, you reference this in What Is Intelligence? You go back to Hal of 2001, by Kubrick's wonderful movie, and then also Data in Star Trek.

**Blaise Aguera Y Arcas** [21:44]: Yeah.

**Interviewer** [21:44]: Um, why does Hollywood wanna treat AI as something, I guess, that is, um, the other instead of something else?

**Blaise Aguera Y Arcas** [21:55]: Well, I mean, part of it is because Hollywood movies have to have a plot, and, and a plot requires a conflict, and that's why, you know, wars and aggressive aliens and so on are always part of the, part of the story in one of these. But even when AI is the good guy. So I, I, I, I actually just-- So it's a little bit of a guilty pleasure, but I just watched Companion, the, the new AI movie on the plane. It's about a, it's about a, a, a sexbot, and the sexbot is the, is the, uh, is the, is the good guy, or well, good not guy in this case. Um-

**Interviewer** [22:26]: [laughs]

**Blaise Aguera Y Arcas** [22:26]: So the humans are the baddies, uh, which, which I, I thought was a welcome change from, uh, from the usual fare. Uh, I, I thought it was pretty good actually. I, I quite liked Companion. Um-

**Interviewer** [22:35]: Yeah

**Blaise Aguera Y Arcas** [22:35]: ... it's kind of the opposite of Meg- of M3GAN with a three, which was, uh, which was a truly terrible movie, and was-- had, had, like, an AI version of Chucky, essentially. But, um, but yeah, there's gotta be conflict, right? Or there's no story. But I think there's a deeper thing there, which is that a lot of the Hollywood ideas about AI, including Kubrick's Hal, are based on a good old-fashioned AI idea of AI. So this is the, the concept of AI that predominated throughout the 20th century, and it never worked. It was why there were all these AI winters in which there was no development of AI, because we tried to do it over and over, and it failed over and over. Good old-fashioned AI is the idea that intelligence is based on logic, and, you know, if, if you kind of calculate all of the odds and make everything exact and everything is framed in terms of logical propositions, that would be an intelligent system. RoboCop and Terminator and so on, by the way, have that too. They're like, you know, "The odds of such and such are 39.7%," and, and, like, we don't know how to do those kinds of calculations, and, and fundamentally, you, you can't do those kinds of calculations. Um, intelligence doesn't work that way. It's so interesting that, that a lot of the failures of modern AI, which, you know, is finally really working, are like, it doesn't even get this logic problem right, and yet it can write a, a, a poem, you know, in, in iambic pentameter about, about teddy bears or whatever. So weirdly, right, it's not what we all thought. It's not this kind of hyper logical data-esque, uh, sort of thing at all.

**Interviewer** [24:00]: I think that's one of the phenomenon of AI that is so interesting in the way we discuss it in the media today, that we hold it to a standard of doing everything and being 100% right all the time, and no one wants to be held to that standard. So- Uh, it's just interesting that we, um, we feel that AI is perfect, and yet AI is really, really a tool. And I think that you go further in that, that you, you basically are saying, if I'm correct, that the power of AI is prediction. It's predicting a sequence of events or a logical sequence of events. Um, it's not necessarily coming up with an absolute perfect answer. Is that, is that an accurate way of describing your, your framework?

**Blaise Aguera Y Arcas** [24:55]: Yes. I mean, I, I do think that prediction is at the core of intelligence, whether ar- you know, artificial or biological. Um, you know, and, and there is a relationship between prediction and getting things right in the sense that, for instance, if you're trying to predict when I say one number times another number equals, and you're trying to predict what comes next, your prediction will be best if you have figured out what the multiplication algorithm is, and thereby you can, you can make a general prediction that will always work no matter what those numbers are. So, uh, you know, having aha moments of figuring out algorithms, you know, figuring out logical things when, when they're appropriate is a part of good prediction. But it's certainly not the case that, that, that most of what we do is amenable to that kind of logical reduction. You know, you can't say what by, by working out a series of math problems like that, you know, what the probability is of the next election going in such and such way. Like, that's a, it's an inherently complex and unpredictable system. So, you know, the, the idea of perfection even existing, uh, you know, in most kind of conversations or in most contexts, I think is an illusion.

**Interviewer** [26:03]: And yet when we talk about, let's say, famous example, a self-driving car, we are talking about the ability to make a lot of complex predictions in a very short period of time, right?

**Blaise Aguera Y Arcas** [26:15]: Yes, absolutely. You want to, you want to be able to predict yourself into arriving where you want to arrive without having killed anybody along the way and, you know, and while, while keeping your passengers comfortable. All of that involves lots of high order prediction. And that's, and that's why these transformer models, which fundamentally are predictors, can actually successfully drive cars now. I mean, if you've ever ridden in a Waymo, they're, they're kind of awesome, where all of the rule-based approaches to driving cars, even in this very canned scenario where you would think it should be reducible to rules, we've got traffic laws and stuff, but none of those rule-based systems ever worked. It's only the predictive-

**Interviewer** [26:52]: Yeah

**Blaise Aguera Y Arcas** [26:52]: ... system that actually succeeded.

**Interviewer** [26:54]: I, I think that Google was actually testing self-driving cars a few years ago in Los Angeles. The cars were behaving perfectly, but they could not exit the San Diego Freeway going north because no human let them in to the lane. And so the cars had to drive all the way into the San Fernando Valley-

**Blaise Aguera Y Arcas** [27:15]: [chuckles]

**Interviewer** [27:15]: ... before they could turn around because they were just being too nice.

**Blaise Aguera Y Arcas** [27:20]: Yeah, that's a problem. Well, you've gotta, you've gotta predict other humans as part of, as part of, of your prediction.

**Interviewer** [27:25]: Right. Right.

**Blaise Aguera Y Arcas** [27:26]: That's that social aspect of things.

**Interviewer** [27:28]: A- and it's held to this perfection standard which, you know, no human predicts other humans perfectly. Uh, you know, we, we've never had a human who's been able to do that. Uh, and somehow we expect AI to do, uh, to do everything at this, you know, 100% accurate level. Um, so maybe we need to change our expectations a little bit.

**Blaise Aguera Y Arcas** [27:52]: Well, we, we often have double standards about, about, uh, expectations about AI and also about our assumptions about people. One of the really interesting, uh, double standards with regard to people that I've noticed is that we, we often, we often think about measuring AI... Well, first we measured AI against what anybody can do. "Oh look, AI can't even, you know, pick up a cup of water. Anybody can pick up a cup of water."

**Interviewer** [28:14]: Right.

**Blaise Aguera Y Arcas** [28:15]: And then we quickly switched to comparing it to what, what the best person in the field or what, you know, what, you, you know, what any human at their best could do, and anything short of that is not intelligent, which is pretty weird 'cause that would place most of us in the not intelligent category as well. Uh, you know, a few years ago, my, my team and I developed a prototype AI model for doing medical diagnosis, and the initial results from that, you know, so it's like you, you plug in, you know, patient records and data, you know, and plain text and whatever symptoms and so on, and, and it, it tries to figure out what is ailing you. And our initial results from, from that model seemed like they weren't great, and so we're like, "Oh, maybe we shouldn't, you know... Maybe there's nothing to see here. Maybe we shouldn't even publish." But, but then we were like, "No, we should actually do a human baseline. Let's see how good doctors are at diagnosing illnesses." The result was that they are terrible. [chuckles] Doctors are terrible at diagnosis.

**Interviewer** [29:10]: [laughs]

**Blaise Aguera Y Arcas** [29:11]: Uh, and, and even that first generation model was already quite a bit better than, um, than, than the average doctor, even than the average expert. So, uh, if there's a moral in this, it's get a second opinion [chuckles] when you're getting diagnosed with something.

**Interviewer** [29:23]: Right.

**Blaise Aguera Y Arcas** [29:23]: But also that, that, that, that's right. Our, our expectation, you know, a priori, uh, you know, was, was unrealistically high, and our assumptions about what, you know, what humans do was also unrealistic.

**Interviewer** [29:37]: We are speaking with Blaise Agüera y Arcas, who's the CTO of Technology and Society at Google. To continue on this, uh, theme of perfection or the expectation of perfection, in law today, hallucinations are the big topic. The hallucination of fake citations in a legal brief or a legal document, that is the topic du jour. And it is true that if you press one of the popular AI models enough, it will begin to give you a false citation. As someone who actually worked in a law office for a few years, I can tell you that humans will also give you, if not false, then very, uh, sketchy citations when they are asked by senior partners to come up with the answer that the partner is convinced exists, right? So- In a way, I find it somewhat amusing that AI is now mimicking the behavior of li- legal associates because their, their goal is to respond to the request at some level. And so my question is, what, what do we learn from these hallucinations, right? We think of them as a bug, but maybe the hallucination is actually a feature.

**Blaise Aguera Y Arcas** [30:50]: Yes. I think it is. Of course, that doesn't make it better when, you know, you want, you want facts and, and you, and you get bullshit. Uh, you know, so I use AI models all the time to search for sources and, you know, to generate citations, but I, but I always check them. [laughs] And-

**Interviewer** [31:05]: Right

**Blaise Aguera Y Arcas** [31:05]: ... and sometimes, and sometimes they don't check out. Although, although they, they do check out more and more often. There's definitely been quite a lot of progress in, in this area over the last couple of years. But, but yeah, it's not a, not a, um, it's not a weird bug. It, it is a feature in, in the sense that, um, you know, I think there's a growing appreciation on the part of a lot of neuroscientists as well that, that memory and planning or free will rely on that same faculty of imagining or, or projecting or even hallucinating. Hallucinating possible futures, hallucinating what could be, or even hallucinating what was based on, based on, on, on the sketchiest of, of remembered cues. Or even, you know, Anil Seth actually made this case very nicely in his book, Being You. Even perception is primarily an act of hallucination. If you were to see what your eyeballs actually see as a video feed, it would be just like this jumpy, grainy, flashlight-sized spot of-

**Interviewer** [31:59]: And it would be upside down, right? If we looked at what the human eye sees.

**Blaise Aguera Y Arcas** [32:03]: Yeah.

**Interviewer** [32:03]: Yeah.

**Blaise Aguera Y Arcas** [32:03]: Totally. And, and it would have bloo- it would be covered, it would be papered over with blood vessels and all kinds of stuff.

**Interviewer** [32:08]: Right.

**Blaise Aguera Y Arcas** [32:08]: It's a mess. So, you know, your idea of what you see and, and, and the world around you is not what your eyes are seeing. It is a guided hallucination in which, uh, the, the eyes serve as continual error correction. Um, but... And, and I make the analogy of, of Blair Witch Project in the, in the, in the book. I don't know if you two ever saw that. It was a really scary movie, but, you know, like-

**Interviewer** [32:28]: Unfortunately, yes.

**Blaise Aguera Y Arcas** [32:30]: Yeah, I, I wish I could unsee it as well. But in the woods with a flashlight, you know, shining here and there, like what the hell is behind me? You know, that sense. Like, the fact that we don't all live in that world all the time is a function of the very powerful predictive hallucination that we're constantly creating of the world around us and, and updating with wherever the flashlight beams of our eyes happen to point.

**Interviewer** [32:52]: And that's what makes AI so powerful right now, is that it is able to cover a huge corpus of information of millions of different topics, and it's really done so maybe in the span of a decade or so, right? It, and it's learning very quickly. You look at the way a baby learns the world. First, you know, touching the first thing next to it, then making sense of, oh, this is a human versus this is me, my sense of self. All of these things that we take for granted, it seems to me that AI models are already grasping, and they're only getting better, which I guess raises the question, what's the next big challenge for large language models?

**Blaise Aguera Y Arcas** [33:36]: Well, one of the big challenges that I'm seeing, that I think a lot of, a lot of people in the, in the field would agree, has to do with how long they can stay on track. So there's a sort of length of task, uh, question that you can ask, you know. Like, how long before things go off-piste? In some of the early models, the first generation of Gemini or the early ChatGPT or the first Claude, um, you know, y- you could, you could barely have a coherent exchange of more than a turn or two. Um, you know, it could give pretty good, pretty good one-turn answers, but, you know, it would, it would drift. And with the more modern models, uh, you know, I, I would say you can have a pretty long discussion that stays grounded and, and coherent. You still can't have a model, you know, go off and accomplish a long-term task. You know, like come back to me in a, in a month with, you know, this and that and the other, uh, done. Um, that's, that's, I think, gonna be a pretty big step in terms of agency or autonomy or, or ability to do economically useful work or augment us in various ways that don't, that don't require continual pair work with, with humans.

**Interviewer** [34:44]: I find these discussions of AI and agency really fascinating. You discuss it in, in your book. You seem to have a little different perspective than most observers on, on AI and agency and intelligence. You relate agency to stimulus and response. Can you explain what, what the relationship is there to agency?

**Blaise Aguera Y Arcas** [35:08]: Sure.

**Interviewer** [35:09]: Stimulus and response. Yeah.

**Blaise Aguera Y Arcas** [35:10]: Well, there are, there are a couple of points there, and one of them is that, first of all, I, I think people are, are often, often mean very different things when they talk about agency. It's a bit like consciousness. You know, sometimes-

**Interviewer** [35:19]: Right

**Blaise Aguera Y Arcas** [35:19]: ... when people talk about agency, they mean something that, that I find a little hard to pin down and seems almost mystical. You know, they're asking whether there's a soul there or something. But if, if you, if we try and stick to more, more rigorously definable stuff, one way of thinking about agency is, you know, does something act on its own or does it only act in response to a, to a, to a stimulus? Is it just-

**Interviewer** [35:40]: Mm-hmm

**Blaise Aguera Y Arcas** [35:40]: ... is it just, uh, turn-taking? So a chess-playing computer, even though it might have what chess players call the initiative at certain points if it's playing well, will still not act autonomously in the sense that I, I make a move and then it makes a move. You know, it's not gonna like... If I wait around, it's not gonna like make another move, you know, or something. That's not in the rules. Things have to alternate. And in that sense, there's not-

**Interviewer** [36:02]: Right

**Blaise Aguera Y Arcas** [36:02]: ... there's not agency in playing chess in the, in the same way that there is if I take the initiative and, you know, go out and do something on my own. So that's... A lot of the, the way large language models are used today is in this turn-taking chess playing-like mode, where it's not physically possible for them to take initiative or have agency in that sense.

**Interviewer** [36:21]: Right. They don't have what we would call autonomy. You know, the chess-playing program is not gonna say, "Hey, let's break and, and look at the stock market now," right? It's not, it's not gonna change the subject, which to me is a very human, uh, a human trait.

**Blaise Aguera Y Arcas** [36:36]: Well, I mean, they, they can, they can absolutely sort of redirect conversations. I mean, they're, they're usually trained not to do that, you know, not sort of exceed the brief, as it were, you know, of what you're asking for. But that is actually part of the behavioral training. It's not an inherent limitation in the, in the model.

**Interviewer** [36:54]: Oh, okay.

**Blaise Aguera Y Arcas** [36:55]: But, but what is an inherent limitation, maybe not so much of the model, is just the way the systems are set up that one interacts with the models through, is that, you know, they, they, they can't be like, "Okay, I'm bored. I'm gonna do something else now." You know? No computation will happen if it's not-

**Interviewer** [37:11]: Mm-hmm

**Blaise Aguera Y Arcas** [37:11]: ... you know, responding to a prompt that you've made.

**Interviewer** [37:15]: There was publicity a few weeks ago about some AI programs that were supposed to terminate themselves, or they were given instructions to end, and they rewrote their own code so that they would not be terminated. What did you make of that?

**Blaise Aguera Y Arcas** [37:30]: Yeah. Um, this, this was... This made big, a big stir in the AI safety community. To be clear, no model that we have today can rewrite its own code, recompile itself, you know, train, train itself again, or do anything of that sort. So all of this was, if you like, a kind of war game or a simulation. But it is definitely interesting. And, um, you know, if, if one looks into the details of all of that, it has to do with what the models are being fine-tuned to want. You know, what, what are their, what are their goals or their motivations? A lot of that stuff is, is in the system prompts or in the way that they're, they're, uh, they're fine-tuned. Um, but this isn't, this isn't the world of Isaac Asimov's, uh, uh, laws of robotics-

**Interviewer** [38:13]: Right

**Blaise Aguera Y Arcas** [38:13]: ... where, where it's all like good old-fashioned AI. You know, rule number one is don't c- harm humans or through an action cause them to be harmed. Rule number two is... You know, you can't make any agent act, uh, you know, in any intelligent way by just following a set of rules. What you instead can do is to say, you know, "Here, here's how I'd like you to behave. Here are the values that I'd like you to have." And those things are squishy, and they, and they allow for plenty of, of possible drift or misalignment, uh, especially if they shift over time throughout a conversation. So I'm, I'm not sure we're ever going to get away from that problem.

**Interviewer** [38:50]: Mm-hmm.

**Blaise Aguera Y Arcas** [38:50]: You know, there are inherent, um, you know, inherent possibilities for a misalignment. I actually think that intelligence arises through misalignment in the sense that if all of us were exactly the same and had no difference in our, in our, in our goals, our behaviors, and so on, there would literally be no point in being social. So viva la difference, right, in some sense.

**Interviewer** [39:11]: Right. And then we wouldn't have sex with anybody because we would all be the same.

**Blaise Aguera Y Arcas** [39:15]: Right. It would just be masturbation.

**Interviewer** [39:20]: We're talking with, uh, Blaise Aguera y Arcas, who's a Google fellow. Just to finish this topic on the apocalyptic side of AI, there were some Nobel-winning scientists who did a famous proclamation a few years ago saying that, you know, AI was gonna lead to the end of humanity. You and many other knowledgeable people said this is sort of ridiculous, that this is not the way we should be thinking about this technology. Are we still getting, uh, getting that strain of a apocalyptic vision or has it, uh, actually sort of died off recently?

**Blaise Aguera Y Arcas** [39:58]: It hasn't died off. And I'm not sure that it should die off in the sense that we, we should remain conscious of, of various threats, risks. You know, there, there are plenty of important existential threats to humanity. I mean, I've, I've always thought nuclear war, for instance, is an, is an extremely important one. You know, the nuclear weapons haven't vanished, uh, just because the USSR fell. And, uh, and they, they pose a very real, a very real risk. There are also risks that are not necessarily existential, but that would result in futures that I don't think any of us really want to live in, like extreme surveillance states, that can be AI-powered or augmented in, in really unpleasant ways. So it's not that I'm a Pollyanna or that I believe there's no possibility for, you know, AI to contribute to really negative outcomes for humanity. But I think that a, a lot of the story or the narrative about AI existential risk is predicated on, uh, uh, really false assumptions, really wrong beliefs about both how intelligence works and how evolution works. And in particular, the evolution part of this, a lot of it is based on, on sort of classic Darwinian theories about the struggle for survival, that, you know-

**Interviewer** [41:04]: Oh

**Blaise Aguera Y Arcas** [41:04]: ... everything is always in competition with everything else, survival of the fittest. Um, you know, it's a, it's a jungle out there. And, and the reality is that cooperation and symbiosis are at least as important in evolution as competition. And in fact, the thing that drives evolution forward, the thing that makes later developments more sophisticated and complex and beautiful than earlier developments is exactly symbiosis, is things working together. So the reason that that, that The Hobbit at the front of The Lord of the Rings, the, the what is life part of the book is there, is to really go into some detail about this kind of expanded Darwinian perspective that takes symbiosis seriously because I think that that really changes the whole story about... You know, it, it makes it clear that technology is a part of evolution and not separate from it. It makes it clear that our development of everything from rocks and shovels to steam engines to computers to AI is also a part of evolution and also a symbiogenesis or symbiotic story. Uh, you know, and, and basically, you know, when, when parts come together to make larger wholes, not only does that add to the complexity and beauty of the world, but it also adds to the, to the agency and the, and the scope of possibilities for the parts that are, that are combining in that way. That's why moving to a city offers you all these rich, extraordinary possibilities that, um, you know, that, that, that are new, right? That, that come about because you, because you're in this, in this larger collective environment. So, um, so that, that's what makes me kind of an optimist despite, um, you know, despite, uh, you know, being acutely aware, right, of, of various ways that we could go off the rails with or without AI in the future.

**Interviewer** [42:43]: I think we need to move toward that more nuanced view of what the technology is before we really start projecting all of the negative things that could be done. I think that's a more mature and optimistic view. Um, uh, we're speaking with Blaise Aguera y Arcas, who is the CTO of Technology and Society at Google. I was struck by this quote from What Is Intelligence? "If something behaves in a way we associate with sentient beings, if it seems to suffer, to choose, to learn, then perhaps it deserves to be treated with moral consideration." That's a lovely thought. Is that one of the conclusions of your exploration of AI to date?

**Blaise Aguera Y Arcas** [43:31]: Well, this is a tricky one. So this question of AI wellbeing, which I, I think you're, you're getting at, you know, should we, should we treat AIs as a, you know, what, what we call in philosophy moral patients, meaning that they not only can act in ways that one can judge as being morally right or wrong, but that they should be treated in ways that one can judge as being morally right or wrong. But I would say this was a very, very fringy idea, uh, you know, a couple of years ago. It's becoming less fringy as people have more and more interactions with, with AI models. Um, the folks at Anthropic, I think, are, are really, uh, at the front end of that sort of thinking. Um, I have complex thoughts about it. Uh, I, I think that, um, we have tended to assume in Western philosophy especially, that, um, personhood is a binary category, and it's kind of all or nothing, and everything kind of gets bundled together for the ride. You know, that if you can experience things, if you're conscious, then human rights and all the other things come along with it. Uh, I mean, I've kind of come to the conclusion that things like consciousness or being able to experience pain, et cetera, are very widespread throughout life. I'm not even sure that bacteria are ex-excludable from that sort of thing. I mean, obviously, if they have anything like consciousness, it's much, much, much more primitive than ours.

**Interviewer** [44:50]: Right.

**Blaise Aguera Y Arcas** [44:50]: But, but, you know, by the time you get to something big and complex like a one centimeter long Porsche spider, they're really complicated, and they, they absolutely are modeling the minds of other beings and, and, and I'm willing to bet that when they succeed at a, at a difficult hunt, they experience triumph and so on. You know, so does that mean that, that, um, you know, that I shouldn't wantonly squash, you know, a spider instead of trying to put it outside? No, I'd rather put it outside. You know, like if it, if it, if it takes me, you know, um, 30 seconds to put it outside, I'd rather do that than, than sort of-

**Interviewer** [45:21]: Right.

**Blaise Aguera Y Arcas** [45:21]: But at the same time-

**Interviewer** [45:22]: Especially-

**Blaise Aguera Y Arcas** [45:23]: Sorry.

**Interviewer** [45:24]: Especially if someone in your house is, uh, encouraging you to annihilate it very quickly.

**Blaise Aguera Y Arcas** [45:28]: Kill, kill. Yeah, exactly. Well, yeah. Right. Better not to annihilate than to annihilate. But does that mean that I believe in human rights for spiders, that they should get the vote? Um-

**Interviewer** [45:36]: Right

**Blaise Aguera Y Arcas** [45:36]: ... you know, that they, that they have equal moral standing to you and me? No. And I'm not even sure they're talking about it in terms of a hierarchy, of a scalar hierarchy like that makes any sense. You know, when, when we start to think about how human rights and patiency work in, in society, and we take a more naturalistic perspective on that, it's not like we... It's not like we're at some, some steady state. We've evolved in our thinking about how all of that works, and I don't think that our evolution in our thinking is the discovery of a natural principle. I think that it's more like agreements that we make with each other about how to behave.

**Interviewer** [46:10]: Mm-hmm.

**Blaise Aguera Y Arcas** [46:10]: How to behave and why, you know, to quote an old book from the mid, mid-20th century.

**Interviewer** [46:14]: And the human framework, human norms have changed about how we treat, how we treat other humans over time has certainly, fortunately evolved. Not perfect yet. How we treat animals has evolved, our consciousness of this. So the framework could shift for how we treat machines and how we tend to look at machines, which I guess leads me to this question: Do we need to be nicer to our AI? Because you suggest, I think, that we need to treat these intelligent machines with some dignity or even, even kindness. And you point out that there's a danger in a universe that is dominated by AI, that we might try to dehumanize these machines, but that we might mechanize humans in the process.

**Blaise Aguera Y Arcas** [47:06]: Yeah.

**Interviewer** [47:08]: Uh.

**Blaise Aguera Y Arcas** [47:08]: Um, I, I think that kindness is there for a reason. Um, and, and I-- when I say for a reason, I don't mean because God told everybody to be kind or, or, or because-

**Interviewer** [47:17]: Right

**Blaise Aguera Y Arcas** [47:17]: ... because there is a natural law of kindness. I mean because we are deeply dependent on each other, and the whole secret of our success is working together. You know, I, I'm reminded of, of, of a book, uh, called Co-Intelligence, uh, by Ethan Mollick, about working with AIs. Um, he wrote that, I think, in 2024. Um-

**Interviewer** [47:35]: Mm-hmm.

**Blaise Aguera Y Arcas** [47:36]: And, uh, it's a f- I mean, I enjoyed the book a lot. It's very practical. It's about how to, how to effectively work with, work with language models. I think it still hits in 2025. Um, and what I found entertaining about it is that he begins with, um, you know, by putting intelligent and understand and so on in, in scare quotes like most people who write about AI do. But then he's-

**Interviewer** [47:59]: Right.

**Blaise Aguera Y Arcas** [47:59]: Well, but okay, but now I wanna, like, just get down to the brass tacks of how to work with an AI, and it's much better if you think about it as a person or an intern, you know, maybe one who has certain kinds of deficits that are unfamiliar. But this is the-- a better way to collaborate with them. So I'm gonna get rid of all the scare quotes now, having done my diligence about telling you that I don't necessarily really believe all this. In my mind, that, that's very telling.

**Interviewer** [48:20]: Right.

**Blaise Aguera Y Arcas** [48:20]: It's, it's very hard to, to have a real collaboration with an intelligent entity that you don't treat with consideration. Um, you know, so for me, this, this is, this is a, a matter of, matter of being happy with yourself, being happy with your collaborations, being effective. Now, I don't know whether, whether I'm gonna be judged, you know, later on. I don't believe, right, in, in, in, in judgment day or anything of this sort, but I do believe in friendliness and cooperation as being just good ways to be.

**Interviewer** [48:51]: Well, maybe in a way is we've created this mirror, and we're looking at ourselves in the mirror of AI. It behaves like us. It can help us do many tasks even better as a, as a collaborator. And I think we need to evolve our, our approach to AI in a way that, uh, you know, we really... Maybe we're not ready for it. Maybe because we let the, um... We, we animated Frankenstein, to go back to Mary Shelley. We've animated the, the, the, uh, monster, but now we have to learn how to live with it. That's not so easy.

**Blaise Aguera Y Arcas** [49:27]: It's interesting that you bring up Frankenstein, Mary Shelley's book. Great-- a great book and a very, very relevant one to read, to read today, I think. So the story of Frankenstein is not the story that most people think it is. The monster is very human in a way, and the difficulties come from the abnegation of the creator, the, the sort of dehumanization of, of the, of the, of the creator in, in treating the, the quote-unquote monster.

**Interviewer** [49:55]: Right.

**Blaise Aguera Y Arcas** [49:55]: And the othering that, that ensues. So to the extent that, that entities can work together, whether those entities are human, AI, or otherwise, it is because of our ability to model each other and, and work with a degree of, of... I mean, I, I hesitate to use words like, like dignity and compassion, but, you know, if you can't put yourself in the place of that, of that other, then what ensues is not, is not so good. Um, a- and even, even when, when the relations are quite instrumental, if it's like hens laying eggs. If you're, if you raise the hens in a nice environment and you feed them good stuff, the eggs are better. [chuckles] Like, the hens are happier, and we're happier. So even in situations that seem very, very unequal like that, I just, I just think we're a lot better off if we begin from the perspective of being generous about, um, about how we project ourselves into other entities.

**Interviewer** [50:52]: That's a really wonderful way to help wrap up this, uh, very stimulating conversation. I wanna point out for our, our audience that Blaise's book, What Is Intelligence?, is available now online on antikthera.org, and we will put a link to that in the Responsible AI podcast page. I wanna end with a question that we started to discuss, uh, the last time we met, Blaise, which is does AI dream? And if it does dream, then how do we know? Uh, I find that to be such a, an interesting philosophical point.

**Blaise Aguera Y Arcas** [51:31]: Well, for the most part today, uh, it would not be possible for it to dream because dreaming involves going to sleep, and it involves our brains continuing to run when, when we are not interacting with others. So in some sense, even if you're daydreaming, the definition of it involves you kind of having ruminations or, or thoughts or mental activity that is not output oriented, you know, that's not, that's not, not sort of, um, manifesting in the moment in your interaction with, with somebody else. There have been a variety of ideas in AI that involve something that Geoff Hinton, I think, once called the wake-sleep algorithm. So the idea of sleep and even of dreaming in AI models is something that actually has been explored technically-

**Interviewer** [52:17]: Mm-hmm

**Blaise Aguera Y Arcas** [52:17]: ... to a degree. Some of the functions that, that, that sleep and possibly dreaming serve for us, uh, like the consolidation of skills and memories, are things that we at least have some understanding, you know, of why those might be useful to AI models as well. So it wouldn't surprise me if we have models that, that, that do the equivalent of sleeping and dreaming in a few years' time. But I-- this comes back to the imagination point that you were raising earlier or the hallucinations, right? When a hallucination becomes, if you like, ungrounded, it- you're not con- constantly error correcting it with input from the outside world, I think in some sense that's what, that's what dreaming is, and it's perfectly possible for, for models to do that.

**Interviewer** [52:56]: It's sort of like a way of looking at dreams as, as maintenance for the, for the mind.

**Blaise Aguera Y Arcas** [53:02]: Yeah.

**Interviewer** [53:02]: And on that note, I wanna really thank you for offering your, your thoughts. It seems to me that this topic is not just about technology. It's not just about biology. We've sort of created something that is gonna continue to challenge us for a long time. Maybe one of our fears is that we're learning more about ourselves in the process of building this construct that we call artificial intelligence.

**Blaise Aguera Y Arcas** [53:29]: I agree. It's all about, it's all about ourselves and about a version of ourselves that is a little bit larger, I guess, than we imagined. You know, in the same sense that societies are more than just individuals, I think that, um, you know, AI is the most recent layer on a larger us construct that, you know, that, that already includes, uh, you know, much, much more than we understand.

**Interviewer** [53:55]: Well, thank you again, uh, Blaise, for your time and for your book, What Is Intelligence? And I will say to be continued because this is a conversation that deserves to be continued.

**Blaise Aguera Y Arcas** [54:07]: Thank you, Alex. That's... I would love to anytime.

**Interviewer** [54:10]: Thank you. Rebecca.

**Narrator** [54:12]: Wonderful. Yeah. Thank you both. Thank you, Alex. Thank you, Blaise Aguera y Arcas, for joining us on the Responsible AI Podcast from The AI Forum. You can subscribe to the Responsible AI Podcast on Spotify, YouTube, Apple, wherever you like to listen. See what we've been reading about the legal and ethical implications of AI on our website, theaiforum.org. [outro music]

