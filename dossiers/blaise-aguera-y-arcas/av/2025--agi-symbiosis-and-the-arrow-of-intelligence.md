---
title: "AGI Symbiosis and the Arrow of Intelligence"
person: blaise-aguera-y-arcas
section: by
type: talk-transcript
year: 2025
venue: ""
source_url: https://youtu.be/mAtjedPGmME
retrieved: 2026-08-15
content: full-text
transcription:
  method: asr
  asr_model: elevenlabs-scribe_v2
  diarized: true
  speaker_labels: inferred   # ASR diarization + LLM naming (claude-sonnet-4-6); not ground truth
  duration_min: 85
notes: "PROVENANCE: machine-transcribed from AV via ElevenLabs Scribe v2 (diarized) + LLM speaker-naming pass. Speaker labels are inferred, not authoritative. Layer-2 (mildly lossy) per charter, not camera-raw."
---

# AGI Symbiosis and the Arrow of Intelligence

*Speakers (inferred):* speaker_0=Blaise Aguera Y Arcas, speaker_1=Interviewer

## Transcript
**Blaise Aguera Y Arcas** [00:00]: We know in the next century that human numbers are not continuing to increase exponentially, and that's a lucky thing. This new symbiosis with technology is gonna look quite different from the Industrial Revolution's one, which is all about just, you know, harnessing industrial energy and getting us out of a Malthusian state. We're already not in a Malthusian state anymore, uh, the overwhelming majority of humans, uh, today. In not very long, there are going to be many, many more AIs than people. That's kind of just around the corner. So we're, we're looking at... You know, if you think about all of, you know, people and AIs, you know, both as nodes in a graph with all kinds of relations between them, the people are the rarer, uh, you know, objects in, in that graph in, in the near future. I don't think a lot of people have really thought about that and its implications because we're still, we're still imagining that, you know, one AI per person is kind of the limit in the same sense that people were imagining that one computer per person had to be the limit, you know, in nineteen eighty.

**Interviewer** [00:58]: [instrumental music] This is Dan Fageli. You're tuned in to The Trajectory, and in this episode is our fourteenth of the Worthy Successor series. Our guest this week is Blaise Agüera y Arcas, who is a vice president, a Google fellow, and also the CTO of Technology and Society at Google, which is a pretty cool n- title for someone working in this field. Uh, Blaise has a lot of very strong ideas around symbiosis and the future of intelligence. We talk sometimes of the Blaise of life or the great process of life of which we are part. I don't know if I've ever heard it clicked together in terms of Lego pieces, in terms of where this bubbling up of life comes from and where it goes to quite as well as I did in this episode. And there's a lot to reflect on, on Blaise's particular vision around where symbiosis takes us, including some areas of agreement and disagreement. But overall, um, there's hardly an episode I've had more fun recording, so I hope you enjoy this one. Without further ado, I'll save my comments for the end of the episode as usual. This is Blaise Agüera y Arcas here on The Trajectory. Blaise, welcome to The Trajectory.

**Blaise Aguera Y Arcas** [02:11]: Thanks so much, Dan. It's really good to be here.

**Interviewer** [02:13]: Yeah. I, I, uh, I have been looking forward to this conversation since our first little chat there, and many people recommending that I dig into your work, and I'm, I'm glad that I did. We're gonna open with the first big question. I think this is gonna be kind of a water slide into the greater pool of Blaise-related concepts, uh, that I think will be fun. The way I normally ask it is, you know, if you could look down as a transparent eyeball, you know, in, in a million years or however many years, and maybe there's no distinguishably human... You know, it's not like nobody's walking their dog, nobody's going fishing. Uh, uh, th-there's not that kind of life. But whatever you see is like, um, rich, complex and you, and you would say, "Wow, this, this feels like a win. Like, this process that we were a part of, like, it actually feels like it kind of won. Like, this is good." What would have to be happening for you to say that?

**Blaise Aguera Y Arcas** [03:00]: It's a great question. And honestly, if I were only able to see that endpoint, if you like, or that, or that moment in time, you know, without anything in between, then my only, uh, sort of indicator of, you know, is stuff going well is, is it rich? Is it complex? Uh, is it interesting? Is it varied? Um, you know, does it look like a thriving ecology? Uh, you know, the, the, the question of like, uh, how much continuity does that have with us, with what we are today, uh, is a question that you could only answer by looking at all of the intermediate times too and, uh, and seeing whether, you know, whether there was any tragedy along the way.

**Interviewer** [03:40]: Yeah. Um, so I, I guess the complexity-- You used a good analogy here of sort of like, does it look like a thriving ecology?

**Blaise Aguera Y Arcas** [03:48]: Yeah.

**Interviewer** [03:48]: Um, I have a mental image of what that means, and I think many people tuned in can think of the economy, they can think of, uh, the marshland behind their house somewhere, and they sort of have a notion of what ecology means. In a kind of grander cosmic scale beyond, you know, the, the, the domain you and I inhabit, um, you know, sparkle our minds a bit with what that could look like or, or maybe you would hope it could bubble into.

**Blaise Aguera Y Arcas** [04:11]: Yeah. Well, you know, in a, in a way, maybe, maybe I'll try and approach this from a s-- from a slightly different perspective-

**Interviewer** [04:17]: Go ahead

**Blaise Aguera Y Arcas** [04:17]: ... which is that of happiness. Uh, you know, what-- when, when people ask each other, like, you know, what, what is, what is a good life? You know, what does that, what does that mean? What are the requirements? Um, I think a lot of people, you know, who think about this agree that you basically need three things to be happy. You need to have your, um, your physical kind of organic needs met. You know, you need to have enough food and, you know, shelter and stuff like this. Uh, and you need to have, uh, connections with other people. Uh, in other words, you need to be important to other people, and other people need to be important to you. Um, and you need to have some sense of efficacy in what you do. Uh, in other words, you know, uh, not, not feel like, uh, you know, you could, you could disappear tomorrow. Actually, that one really applies to number two and three, the right, you know.

**Interviewer** [05:04]: Yeah. Yeah.

**Blaise Aguera Y Arcas** [05:05]: If I disappear tomorrow, nothing would be any different, it's not a good feeling.

**Interviewer** [05:08]: Yeah.

**Blaise Aguera Y Arcas** [05:08]: Um, and, and an ecology is really just a, uh, a complex network of entities for which those things are all true. Uh, and, and I see it as a really deep concept that transcends economy because, uh, you know, economy i-imagines that everything can be boiled down to a single number. You know, that, that everything is reducible to a price.

**Interviewer** [05:29]: Yeah.

**Blaise Aguera Y Arcas** [05:29]: Uh, and in a real ecology, that's not true. Uh, you know, there are a lot of things that are not commensurate with each other. You know, if, if you, uh, don't have oxygen to breathe, it's not like, you know, money is gonna buy you that. Uh, you know, you, you, you know, people have-- and entities of all kinds have a lot of needs, uh, and a lot of wants and a lot of things that they have to offer to other stuff. And a system that is thriving and one-- is one in which, you know, everything is rich in stuff that is offered by other stuff and, and is in turn generating wealth in this kind of very multidimensional sense, uh, you know, for others as well.

**Interviewer** [06:03]: Yeah. So this is, this is gonna start us down, I think, at the right path. 'Cause when you said like, okay, you know, you have physical needs met, you have connections with others, you have efficacy, I started thinking like, well, I, I don't know if every series of sea snail feeding off of a vent somewhere is like, man, you know, unless I feel the sense of competence, right? Some of these strike me as remarkably hominid-ish. But I think what you're talking about is in a conceptual sense. There is a relationship with the sea snail and a lot of other life. And, and there are relationships that make more sea snails, uh, you know, of, of, uh, probably not a romantic kind, but, uh, you know, they have needs too, I presume. Uh, I don't know what it's like to be a sea snail. Um, but, but yeah, I, I think what you're saying is these we feel in this sort of emotional sense because we've had all this cortex bubble up. But all the way down, there's a level of this in all these interactions. Am I following you?

**Blaise Aguera Y Arcas** [06:51]: A hundred, a hundred percent. I mean, of course, sea snails aren't, aren't, uh, self-conscious in all the ways that we are. They're not able to-

**Interviewer** [06:57]: Yeah

**Blaise Aguera Y Arcas** [06:57]: ... introspect, you know, about, about their, their needs and their sense of efficacy and stuff. Of course not. But what is true is that sea snails are providing, if you like, ecosystem services for other, uh, you know, for other kinds of life and vice versa.

**Interviewer** [07:10]: Yes.

**Blaise Aguera Y Arcas** [07:10]: And, and the reason that life holds together, the reason that it persists and that it becomes more complex over time is because of all of those, um, networks of mutual aid.

**Interviewer** [07:21]: Yeah.

**Blaise Aguera Y Arcas** [07:21]: And, and so, you know, so the-- our, our feelings about this kind of stuff don't come out of nowhere. They, they come out of the fact that, that, you know, that those high order models are, are models of, of reality, of how stuff actually is.

**Interviewer** [07:34]: Yeah. I, I think, I think, you know, um, there is a-- there's something to be said of, well, you know, these grooves and circuits in the mind that make a sunset appear beautiful and whatnot, some of that is like, okay, for your ancestors, when there was running water and there was birds chirping and things were green, it was like, you're probably not gonna die tomorrow. Like, it was like there was a sense of that.

**Blaise Aguera Y Arcas** [07:54]: Hundred percent.

**Interviewer** [07:54]: And so like, so that-

**Blaise Aguera Y Arcas** [07:55]: Yeah

**Interviewer** [07:55]: ... so there's an arbitrariness. But there's also like a, you have drives and kind of meta things that are important. You have curiosity. Humans wanna climb mountains, invent things, whatever. This is a-

**Blaise Aguera Y Arcas** [08:05]: Yeah

**Interviewer** [08:06]: ... this is a shooting forth of the same impeti that are spinning forth everything else, except you feel it. The sea snail doesn't feel it. It doesn't, doesn't write a damn poem about it, but you can. And so I, I think to your point-

**Blaise Aguera Y Arcas** [08:16]: Or at least, or at least you have, you have a model of yourself feeling it. I mean, I, I-

**Interviewer** [08:20]: Yeah, yeah

**Blaise Aguera Y Arcas** [08:20]: ... I think the sea snail probably does feel those things, but it doesn't reflect on those feelings, if you like. [chuckles]

**Interviewer** [08:24]: There we go. No, actually, I completely, completely concur with your correction there. Let me ask, how do you frame this process of which we are part? I mean, there was a time where the sea snail was probably as high as it goes. I mean, that was like, whoa.

**Blaise Aguera Y Arcas** [08:37]: Of course.

**Interviewer** [08:37]: You know, a couple billion years, everything was one cell. And then we started having some more complexity, you know, and then there were some Precambrian stuff and whatever. Um, and it's sort of bubbling up, and there's this, uh, things are meeting needs, things are interacting with other things, things are bouncing off of other things. Somehow it's more complicated. And then I hear sometimes the argument, "Hey, we shouldn't presume that continues. You let something evolve often, it'll just get stupider. Everything's random. It's going in random directions." It doesn't feel as though that's been true. Now, I'm not saying there's an inevitability that all of nature's fecundity leads to a jackpot. It's quite obvious it doesn't, actually. It's quite obvious most of nature's fecundity does the opposite. However, net-net, the network seems to be doing something here. How do you conceptualize this? You, you're familiar with the Gaia literature. You think a lot about symbiosis. What should we understand about this process?

**Blaise Aguera Y Arcas** [09:28]: Yeah. And you're, you're asking a really deep question, and it really is, is about evolution's arrow of time, is one way of thinking about it. So, uh, if you go back to, uh, you know, kind of classic neo-Darwinian, uh, thinking about evolution in the mid-twentieth century, the idea was that, um, everything is equally evolved. You know, bacteria and humans, you know, all, all life has been ar- has been around for, you know, like it's been evolving for just as, just as long as, as, as we have. There's no sense in which, uh, you know, any life is more advanced than any other life. Uh, to the extent that we see things that are more advanced now, it's an ob-- it's kind of a, an observer bias or, you know, or, or the fact that, that, um, you know, that there's drift and maybe we're looking only at the tail of the distribution.

**Interviewer** [10:12]: Yeah.

**Blaise Aguera Y Arcas** [10:12]: I, I don't buy that at all. Um, and, and the reason I don't buy it is because, um, that classic view of, of, uh, Darwinian evolution misses, uh, something really important, which is, um, symbiogenesis, the idea that sometimes, uh, simple things come together to make more complex things. And, um, and those complex things can't arise without the simple things having been there first. Uh, so, you know, the, the evolutionary biologists, uh, John Maynard Smith and Jörs Szathmáry wrote about this in, uh, in a, a pretty famous nature paper in nineteen ninety-five. Uh, they called it Major Evolutionary Transitions. Um, they listed, I think, eight of them in their original paper. They've since expanded their list to twelve. Um, I actually would take their hypothesis further, but even if we just look at their twelve or so to begin-

**Interviewer** [10:59]: Mm

**Blaise Aguera Y Arcas** [10:59]: ... those transitions are things like, um, individual humans becoming societies, um, bees, uh, and other social insects becoming social, uh, from solitary, uh, individual cells becoming multicellular organisms, um, archaea and bacteria becoming, uh, becoming, uh, eukaryotes. And what's, what's cool about those, uh, about those transitions is that they result in something that is, like, discontinuous with what was there before and more complex than what was there before. Like, the earlier things are still there, but what they've come together to make is a new kind of entity that is, that is, um, richer. Uh, and, and, um, you know, in that sense, uh, evolution absolutely has an arrow of time because, you know, again, like the simpler things have to be there before the more complex thing comes. It's the same with inventions, by the way. I mean, when, when, uh, the light bulb is invented, it's, if you like, a symbiogenesis between the ability to blow glass, to make an electric current, to draw a filament, um, to make a vacuum. You know, the moment, the moment those precursors were there, they were gonna be combined, you know, in somebody's mind to make a light bulb. And, you know, lo and behold, they were combined in the minds of at least a dozen people who all invented a light bulb around the same time.

**Interviewer** [12:08]: Huh.

**Blaise Aguera Y Arcas** [12:08]: There could have been no light bulb without those precursors. Um, and this, this view of, of invention, by the way, is one that, that W. Brian Arthur wrote a really nice book about, uh, you know, back, back in twenty ten or so. But, um, but yeah, so, so this, this, this means that there's an arrow, uh, of evolution. You know, things do get more complex, and, and they get more complex through cooperation. Uh, you know, when, when cooperation becomes close enough that, that, uh, that, that those things cooperating become, uh, you know, really tightly interlinked, then you need to kind of zoom out and look at them as a, uh, as a joint entity as well as, as individuals.

**Interviewer** [12:44]: Yeah. I-- We're gonna a hundred percent hit this arrow of time that you're talking about. I've never heard that phraseology. I'm following you, but we're definitely gonna go down that rabbit hole. There's a-- Stuart Kaufman sort of has a bunch of thinking about this stuff around, like, the, the le- the degree of sort of unbounded complexity that comes from some things combining, and then they change the whole ecology, and then everything has to adapt to that new-

**Blaise Aguera Y Arcas** [13:07]: Yeah. Pro-probably very, very closely related idea. Yeah. He calls them Kantian wholes. Uh, I agree with his, his take on this.

**Interviewer** [13:11]: Yeah. Yeah. Th-this kind of, uh, pe- some people say holon, where, like, everything is sort of a part, but it's part of a whole, but it's also, you know, unto itself. I mean, you know, you and I obviously are made of individual cells that presumably know not of the conversation you and I are having now. Um-

**Blaise Aguera Y Arcas** [13:24]: Right

**Interviewer** [13:25]: ... and, and, you know, uh, so the, uh, th-this arrow of time, it goes up, it goes up, it goes up. It seems to be doing this. And your supposition here is that, um, things come together, and it is often through cooperation, I-- uh, we'll explore that as well-

**Blaise Aguera Y Arcas** [13:42]: Yeah

**Interviewer** [13:42]: ... uh, that, that form something more complex, which allows for all kinds of other wholes and parts to come into existence. It can combine in a whole bunch of new other ways and, and, and so on and so on.

**Blaise Aguera Y Arcas** [13:50]: Hundred percent.

**Interviewer** [13:50]: What is the tendency that drives this combination? Wh-why does it ha-- Some people would say, "Okay, well, okay, it happens every now and again, sure." But why is it, why is the arrow of evolution, in your words-

**Blaise Aguera Y Arcas** [14:03]: Yeah

**Interviewer** [14:03]: ... why is it doing this over and over and over again? Like, what is-

**Blaise Aguera Y Arcas** [14:08]: Right

**Interviewer** [14:08]: ... what is the attractor here, in your opinion?

**Blaise Aguera Y Arcas** [14:11]: Well, I mean, initially, uh, it, it is a random event. Uh, you know, something, something random happens that brings two things together. Um, but you know, that may or may not stick. When it sticks is when one of them provides something that the other really wants, and vice versa. In other words, there's mutual benefit, and that mutual benefit leads to greater collective thriving than the two would have on their own. Um, you know, and, and there are many ways for that to come about. Uh, but well, I mean, let's take, let's take mitochondria and archaea when they came together to make, to make eukaryotes. So, um, you know, mitochondria are bacteria, and they're bacteria that are living, you know, inside our cells. Um, and archaea were, were also, you know, very, very simple single cellular organisms, um, you know, uh, prokaryotes as well. And somehow, you know, the mitochondrion ended up inside the, the archaeon, and the whole thing is now this, is now supercharged. It's supercharged because the mitochondrion is able to generate energy, uh, extremely efficiently inside the environment of the, of the, um, of the archaea. So there's a, there's a-- it's kind of, you know, one of these things has found a new environment inside the other one that allows it to thrive in a way that is much, in, in, in a much more powerful way than it could on its own. There are still bacteria around that look very much like mitochondria, so it's not like the solitaries are gone. But, you know, most of the bacteria of that shape are now living inside archaea because that's an incredibly rich environment for them, and the benefit that they give to the archaea is that now the archaea has so much energy that, uh, that it can, that it can reproduce enough, uh, DNA, for instance, to develop much greater complexity, and that's why we've got multicellular life and all that kind of stuff. So it allowed many new niches to open up for, um, for those, uh, eukaryotes too.

**Interviewer** [16:00]: So, so the arrow is indicative of many, you know, uh, things come into being partially through kind of dumb fecundity and accident, um, maybe through some other impetuses. Um, and then, uh, different things can sort of behoove one another in different ways. And when they do, and then they form together-

**Blaise Aguera Y Arcas** [16:19]: Yeah

**Interviewer** [16:19]: ... that might be something that's more net capable, and then that opens up new combination surfaces for new things and changes the environment and, and so on. And that when-

**Blaise Aguera Y Arcas** [16:28]: Hundred percent.

**Interviewer** [16:29]: Yeah. Okay. So, uh-

**Blaise Aguera Y Arcas** [16:29]: Or, or take, or take human, take human societies, you know. Like, um, we, we, uh, we were-- I mean, we've been around for a couple of hundred thousand years, right? So, so our sense of our history is so mu- is just the most recent little tiny bit, you know, the, the Holocene, right, of the time that human beings have been around. But for the huge majority of that time, as far as we know, we were living in hunter-gatherer type societies, um, which, you know, where everybody did more or less the same tasks. There wasn't too much division of labor. There wasn't much hierarchy. There wasn't, um, you know... And life was hard. Uh, you know, and, and I, I don't-- I mean, it's, it's difficult to get into ar-- you know, arguments about whose life is better. I mean, there are, there are definitely ways in which hunter-gatherer life was, was better than, say, you know, the, the life of a, of a, of a ground-down factory worker in, uh, in the year eighteen hundred.

**Interviewer** [17:15]: Yeah. I, I'm with you. Yeah. [laughs] Okay.

**Blaise Aguera Y Arcas** [17:17]: So, you know, it's com-- it's a complicated story, but-

**Interviewer** [17:20]: Yeah

**Blaise Aguera Y Arcas** [17:20]: ... but the, but the point is that once we figured out how to start to do division of labor and concentrate in cities, the things that we became capable of as humans just exploded. And, uh, you know, the kind of life of plenty that you and I have now, and not just life of plenty, but a life of plenty such that we can survive in, in environments that would have been completely inhospitable to our hunter-gatherer forebears, um, right, thanks to our division of labor and our technologies and so on. Like, it just, it just opens the possibilities up for us, as well as making these larger units, uh, larger social units that didn't exist before.

**Interviewer** [17:53]: Yeah. So, so I, I like where you're headed for a bunch of reasons. What you're saying is, you know, th-there is a combination, coordination, cooperation, whatever words we wanna use, is sort of the driver here. And, but, but I, I often sincerely dislike the idea that like, well, things just love each other and come together. What you're saying is like, look, it's in the interest of A and B, and when that happens, things... I, I'm very much a believer that sort of like when you look out at nature, at everything warm and fuzzy, like- Almost like it seems ubiquitous that it has-

**Blaise Aguera Y Arcas** [18:28]: Yeah

**Interviewer** [18:28]: ... like a very functional purpose. Like, like I believe that-

**Blaise Aguera Y Arcas** [18:31]: 100%.

**Interviewer** [18:31]: So I, I'm gonna, I'm gonna do a tiny amount of philosophical concept putting on the table, and then just see how you play with those Lego pieces. So Spinoza, who I probably reference too often, but is just in- intimidatingly important and, uh, super smart. Uh-

**Blaise Aguera Y Arcas** [18:46]: Yeah. Spinoza is great

**Interviewer** [18:46]: ... Spinoza has this idea of, of, of the conatus, uh, kind of the core impetus to persist in all organisms, organizations, whatever. And that, you know, uh, he, he didn't know what an... what like an atom was or the details of a cell, of course. Um, but, but he-- So he doesn't really know what, what part of the building block it comes up in. And, and I don't know either. It might be in guanine itself is self-interested in some strange way that you and I can't understand. People say it starts with the gene, but it's like, I don't know, man, something had to close around a cell. Like, like it seems like that impetus is actually deep. So something about the world like wants to persist. And, and it doesn't seem like granite does that, but it does seem like some stuff does, and it seems like we call it life. Anyway, around the time that Newton said, "Here's what dead matter does," Spinoza said, "Here's what living matter does." He wrote the ethics. And people don't think about it like that, but I, I, I often do. He has this idea that potentia is the total set of powers that permit a thing not to die. The total set of powers: flight, sight, verbal communication, the ability to burrow in the dirt, uh, the ability to have feathers, uh, you know, um, uh, uh, the development of culture where we can teach each other things. Um, uh, uh, you know, tech- technological innovations, you know, this nice microphone, you know, a, a shovel, whatever the case may be. All is potentia. Anything that is a power that permits a thing to persist, uh, uh, is, is sort of potentia. And his idea is that in order for the conatus to persist, it's not like, okay, just play defense. The world is too changing. You have to constantly-- If you wanna persist, nature at, at some really early stage decided expanding potentia is the way the flame doesn't go out, the flame being non-dead stuff. And it seems as though the grand expanse of said potentia over the last four billion years, three and a half, whatever it is, here on Earth, seems to maybe in, in your, in your mind, these bump ups of potentia over and over. These-- The, the, the more, the more stratospheric jumps rather than just iterative tinkerings have been through this mutually self-interested coo- coordination. Uh, let me know if you would, uh, push back on some of this, my interpretation of Spinoza and ideas, if you wanna build on parts of that. Because the audience has heard some of those ideas. You're, you're making things click in ways that I'm like, oh, I think that's how that fits in my head. How do you think about it?

**Blaise Aguera Y Arcas** [21:01]: Yeah. I, I agree with everything you've said. Uh, and I, I do think Spinoza was really onto something with, you know, his, his idea of, of, of conatus and, and potentia. Um, you know, so, so I, I tend to, I tend to look at these things through a slightly different, um, uh, more physical lens, but, uh, but arrive in the same spot. So, um, the idea of dynamic stability is, uh, something that was introduced by, uh, origins of life chemist Addy Pross, uh, a, a couple of decades ago. And, um, his idea is that, uh, you know, thermodynamics tells us that things that are s- that are stable persist. You know, if something is unstable, it will, it will, it will not persist in the future. Uh, the idea of dynamic stability is a kind of stability that involves a process. In other words, it's not just like granite, you know, that, that is, you know, hard and therefore endures, but something that has some kind of a cycle or some kind of a loop that, um-

**Interviewer** [21:56]: [laughs]

**Blaise Aguera Y Arcas** [21:56]: ... that is, uh, you know, that, that has its own kind of stability or amplification. This is where that old joke about DNA being the most stable molecule in the world comes from. You know, obviously-

**Interviewer** [22:04]: Ah

**Blaise Aguera Y Arcas** [22:05]: ... as a, as a thermodynamic molecule, it's very fragile, and yet if it can make more copies of itself, then it's in some sense even more durable than granite, right? [laughs]

**Interviewer** [22:13]: Yeah.

**Blaise Aguera Y Arcas** [22:13]: 'Cause, uh, 'cause it will persist. It has more conatus, if you like.

**Interviewer** [22:17]: Yeah. Oh, it's, it's, it certainly seems to. And-

**Blaise Aguera Y Arcas** [22:20]: Yeah

**Interviewer** [22:20]: ... w-when you think about that, what you just said, this, this cycle, it-- I was kind of smiling because it's like, oh, God, it always ends up being kind of poetic because we, we-- it's like we get to a level of abstraction where it's like, what is this thing? Like, and, and I think what you're touching on seems to be kind of what it is, but it's sort of like, where do those cycles start? Like from whence? Is it-- Is there something in the quarks that sort of want to eventually move and do and cycle as we, you know, we all use our language, whatever. Um, where do you think it comes from? You said you have a physical angle. Let's unpack your physical angle here-

**Blaise Aguera Y Arcas** [22:55]: Sure

**Interviewer** [22:55]: ... and really talk about the origin of this impetus.

**Blaise Aguera Y Arcas** [22:58]: Sure. I mean, so we don't, we don't really understand, of course, what's happening, you know, on the ground floor of the universe. You know, we, we don't-- You know, there, there are limits to our, our understanding of, of-

**Interviewer** [23:07]: Yeah

**Blaise Aguera Y Arcas** [23:07]: ... of fundamental physics. But, um, as far as we think, uh, there are field theories and maybe something below those field theories, maybe it's simplicial complexes or strings or who knows what. But, um, but there are, there are perturbations in those fields, uh, that persist through time, uh, and there are ones that don't, right? So if you, if you're a virtual particle that, you know, pops in and out, you know, then you don't persist. If you're an electron, you do persist. Does that mean that an electron wants to persist? I think that would be s- that would be a stretch to say, but there certainly is a selection process there in the sense that-

**Interviewer** [23:42]: Mm

**Blaise Aguera Y Arcas** [23:43]: ... you know, if you, if you go a little way after the Big Bang, you know, there's some stuff that is still around and some stuff that isn't, and the stuff that is still around is, of course, the stuff that has persisted, right? Uh, so something like an, uh, an electron or a, or a quark is a perturbation that, you know, regenerates itself. You know, it kind of oscillates or something, right? It regenerates itself through time in some very, very minimal way. It's not life yet, um, because it doesn't, um, uh, it doesn't compute. Uh, it doesn't have, it doesn't have any, uh, decisions to make, if you like. You know, its, its, its rules are, are a little too, uh, too simple, and they're not Turing complete. I'm now relying on my own definition of life but, uh, you know, you, you can't get, uh, something out of an electron like heritable, uh, um, reproduction, for instance. You can't, you know, make a change to an electron. It has baby electrons that-

**Interviewer** [24:30]: Yeah

**Blaise Aguera Y Arcas** [24:30]: ... have that same property. But, but it, it does have persistence in a way that other kinds of perturbations in the quantum field don't So there is a selection happening right from the beginning. Now, electrons and protons get together. Uh, you know, is that a kind of symbiogenesis? In a way, yeah. You know, there are certain configurations of electrons and protons that, that form a stable hydrogen atom, and that hydrogen atom has a, has a kind of persistence, uh, through time. So, you know, i-in that sense, I think that this idea of, of symbiogenesis absolutely goes all the way back, you know, to, to the pre-life times. Um, the special thing that happens at the moment of the emergence of life is that you start to have a system that has instructions inside itself for how to make itself, and it can follow those instructions to make, to heal or to, uh, or to reproduce or to grow.

**Interviewer** [25:21]: Yeah.

**Blaise Aguera Y Arcas** [25:21]: Uh, and that's a really cool step because that means that if those instructions get modified in some way, then all of the successor generations are changed in that way as well. So you get heritability. Um.

**Interviewer** [25:33]: Yeah.

**Blaise Aguera Y Arcas** [25:33]: There, th-yeah, there's a, a really cool idea, um, that, uh, that life is basically, you know, the emergence of life in the first place is, is about an original symbiogenesis between things that have cycles that, that, you know, that already have those kinds of primitive, you know, molecule A catalyzes B, which catalyzes C, which catalyzes A, you know? And-

**Interviewer** [25:53]: Yeah

**Blaise Aguera Y Arcas** [25:53]: ... and, and so you already have that going, but then when a few of these things come together in the right way, you get the, you know, this, this, this indirect encoding where you have the instructions to build yourself, and that's the moment when you get life.

**Interviewer** [26:04]: Yeah. Well, but it, it's fascinating to think that, that the unraveling process starts before that. In other words-

**Blaise Aguera Y Arcas** [26:13]: Right

**Interviewer** [26:13]: ... persistence is-

**Blaise Aguera Y Arcas** [26:14]: Evolution goes back to before life

**Interviewer** [26:15]: ... filtered for, and symbiogenesis-

**Blaise Aguera Y Arcas** [26:17]: Yeah

**Interviewer** [26:17]: ... at some level happens before that. The, these are-

**Blaise Aguera Y Arcas** [26:20]: Right

**Interviewer** [26:20]: ... like physics is canatus in some way. And of course, Spinoza's whole like, uh, you know, uh, uh, you know, Spinoza's God and the, the, ev-everything sort of being, uh, th-this, this sort of, uh, singular substance and whatnot, um, th-there's analogies there too. But yeah, so that-

**Blaise Aguera Y Arcas** [26:36]: Yeah

**Interviewer** [26:36]: ... that, that's, that's fascinating. But, but then of course you get to life and now a new, what I would think of as magazines of possibility open up when you cross that threshold. But then of course-

**Blaise Aguera Y Arcas** [26:47]: Yeah

**Interviewer** [26:47]: ... like your, your, uh, uh, group of folks you mentioned that talk about these major evolutionary, I think Maynard Smith there, um-

**Blaise Aguera Y Arcas** [26:55]: Mm-hmm

**Interviewer** [26:55]: ... th-these, these ideas of, you know, there's these other leaps and presumably at those leaps, entirely new things, uh, emerge that, that c-c- completely inconceivable. What this-

**Blaise Aguera Y Arcas** [27:07]: That's right

**Interviewer** [27:07]: ... beckons is the fact that most of those unravelings haven't happened yet. Most potentia, so all the potentia you and I observe bubbled up from Jack Diddley, presumably, and, and we should presume that point O continuing one percent of all potentia hath thus forth bubbled up. And it beckons how grand the future waves could be because I would imagine that jump from hydrogen and th-these combination of, of, uh, chemical reactions into, you know, a protozoa of some kind, um, we may have a bunch of those latter steps still popping. Who knows when-

**Blaise Aguera Y Arcas** [27:45]: Absolutely

**Interviewer** [27:45]: ... and how they end. Um-

**Blaise Aguera Y Arcas** [27:47]: Yeah

**Interviewer** [27:47]: ... how do you like to walk people through... Clearly, there's an agglomerative kind of coordinative sort of, and it's not all happy-go friendly. I mean, a lot of things kind of get chewed up in the process. You know, we had horses as part of our cycles for a while, and we turned them into glue 'cause we found other ways to fill that void. Uh, I, I think there's sort of like d- it's, it's based on the self-interest you talked about, not lovey-dovey, which is, which is why I can respect the opinion that you said. Um, w-what do you like people to understand about where this goes? We-- You've talked about the paradigm shifts. This physics perspective is, uh, mind-blowing. I've got to do a lot of journaling on that. How do you like to explain where this heads off?

**Blaise Aguera Y Arcas** [28:24]: Well, I mean, I don't know where it heads off. Uh, I know that, I know that the best way to predict in the near future is to think about how all of the things that we've got today can combine and recombine to make, you know, some of the obvious, you know, light bulb-like stuff, right, that hasn't happened yet. So, you know, that's a good way to be a futurist in the near term.

**Interviewer** [28:42]: Yeah.

**Blaise Aguera Y Arcas** [28:42]: But, um, but the problem with long-term futurism is that you're now talking about combinations of combinations of combinations of stuff and-

**Interviewer** [28:48]: You're lost

**Blaise Aguera Y Arcas** [28:49]: ... who knows, right? It-it'll be, it'll be complex, it'll be wonderful, um, but, you know, things become very, very hard to predict. Um-

**Interviewer** [28:57]: Yeah

**Blaise Aguera Y Arcas** [28:57]: ... you know, you're, you're right that, uh, that all of this, uh, can work in a way that is driven by selfish goals, if you like, and, uh, that's actually one of the, one of the most exciting, uh, pieces of research that we're doing now in, in, in my research team, Paradigms of Intelligence. Um, we're, we're actually about to publish a, a giant paper about this, uh, called, uh, MuPi. Um, so this is, this is, uh, um, you know, it started off as a, as a, a project in multi-agent reinforcement learning, where when you have a bunch of AI agents that, um, that you want to train to solve a, a problem collectively, this is the, this is the multi-agent reinforcement learning problem. Traditionally, that's been a very, very difficult challenge, um, because basically, you know, when you do normal reinforcement learning with an agent in an environment, it's like it's playing a video game and, uh, you know, it can see what the score is. It's, and it's trying to maximize its score. But, um, but now suddenly there are other agents playing the same video game. Like you, you see them as, you know, uh, as other characters, right? It's now, it's now a multiplayer video, you know, what-whatever you call it. Like, uh, you know, it's a multiplayer video game.

**Interviewer** [30:04]: Yes. Yes.

**Blaise Aguera Y Arcas** [30:05]: And, uh, and they're all learning, which means that, that you as an agent need to not only learn from what you have experienced so far, but also, um, predict what the other a-- how the other agents will learn and will change their behaviors in response to your behaviors. That's what makes it really gnarly. So we've figured out a way to solve this, uh, this, this challenge and, um, and in the process, we've, we've figured out an extension to classic game theory that, uh, that I think is, is really important. So in normal game theory, when you have, uh, a couple of players Uh, that are self-interested and you have this payoff matrix. Uh, you have Nash equilibria-

**Interviewer** [30:43]: Yeah

**Blaise Aguera Y Arcas** [30:43]: ... which is to say, you know, winning, winning combinations. And they're pretty grim. Like Nash equilibrium in something like the prisoner's dilemma where, you know, one of us can screw the other one. You know, like-

**Interviewer** [30:53]: Yeah

**Blaise Aguera Y Arcas** [30:54]: ... Nash equilibrium is not, is not a nice solution.

**Interviewer** [30:56]: No.

**Blaise Aguera Y Arcas** [30:56]: You know, it's basically defect. Um, but what, what our, what our, uh, work shows is that in this world where you actually, you know, have other agents like you, uh, you know, playing the same game, uh, if you are smart enough to be able to recognize that they are like you, then this new set of equilibria, uh, come in, uh, which are a lot friendlier and, and they involve, uh, defaulting to cooperation instead. Even though the-

**Interviewer** [31:23]: Oh

**Blaise Aguera Y Arcas** [31:23]: ... even though the, the goal is, is, is still purely, uh, you know, about self-interest.

**Interviewer** [31:29]: Well, I think, I think that that seems to be the story of civilization. I mean, you know, of course we had-

**Blaise Aguera Y Arcas** [31:33]: Totally

**Interviewer** [31:33]: ... World War I and II and all that stuff and, you know. But like writ large seems like we're in kind of more of a, you know... If I, if, if, uh, my tribe ran into another tribe, you know, twelve thousand years ago, it'd probably be a rough time, to be honest. But, um, these days, you know, the, the little town of Weston, Massachusetts here is, uh, you know, not, not a, not a whole lot of, you know, theft and, you know, uh, uh, defecting, I guess as you would say. And so-

**Blaise Aguera Y Arcas** [32:00]: That's right

**Interviewer** [32:00]: ... um, people have talked about-

**Blaise Aguera Y Arcas** [32:01]: I think it's exactly, it's exactly that process.

**Interviewer** [32:03]: Yeah. The, the people have talked about even the early game theory experiments where they, they, you know, tit for tat was invented or whatever, right? Those, those early iterations, I forget who ran all those. Um, there was sort of a, there was something in there about like, okay, an iterative ongoing game coordination is much more highly, uh, i- in, in incentivized because if you know you're gonna play again with this person or someone this person knows, then you're more incentivized to... And it seems like-

**Blaise Aguera Y Arcas** [32:32]: That's right

**Interviewer** [32:32]: ... um, humans had to really figure out how to get that done, or humans had to bumble into each other enough times for enough of them to have the idea and maybe for enough IQ to bubble up to be like, "Wait, wait, wait. In a week we're gonna see these people at the watering hole again. Like, what are we, what are we thinking here?" Like somebody had to... There was presumably there were-

**Blaise Aguera Y Arcas** [32:53]: Had to be some people. Yeah

**Interviewer** [32:54]: ... there was something, there was something that wasn't walking upright yet that didn't know or wasn't thinking about that in a week that was gonna happen. And so-

**Blaise Aguera Y Arcas** [33:00]: That's right

**Interviewer** [33:01]: ... um, coordination seems to sort of make sense on some level-

**Blaise Aguera Y Arcas** [33:04]: Exactly

**Interviewer** [33:04]: ... in that regard.

**Blaise Aguera Y Arcas** [33:05]: Exactly. And it's, and it's favorable. And, and, and the, the interesting thing is that when you start to coordinate like that, once the coordination becomes, becomes tight enough, now there are, now, now a new set of interests arise, which is, if you like, the interests of the group.

**Interviewer** [33:19]: Yeah.

**Blaise Aguera Y Arcas** [33:19]: So it's like there's now a new score in that video game. You know, it's not-

**Interviewer** [33:22]: Yeah. Yeah, yeah

**Blaise Aguera Y Arcas** [33:22]: ... it's not the old video game anymore.

**Interviewer** [33:24]: Yeah. Well, and, and that presumably keeps going on and on. So-

**Blaise Aguera Y Arcas** [33:28]: Exactly

**Interviewer** [33:28]: ... I, I wanna, I'm gonna boil down a little bit simply to check the box because in the series we always cover it, and I do think it's actually really interesting to kind of compare where people think we're gonna have an event in New York and we're gonna put up all the ideas from, you know, Ed Boyden and, uh, uh, Peter Singer and Bostrom and what about, like what are your worthy successor criteria? And you've given me some hints. I'm gonna start kind of like lining up things I think you're saying and just, just see if we can kind of polish and clarify. Um, one thing I want to ask about because we haven't gotten there quite yet is consciousness. A common answer, and by the way, if you have a different answer, I'm delighted. Uh, but, but what I would love to know whatever your genuine answer is. Um, a lot of people have brought up, but probably the biggest commonality is, okay, yeah, yeah, it'll be complicated. Maybe we can't foresee all of it, but like, geez, if at least what we know to be consciousness is not a part at all of that picture, that feels probably like if I was looking down and I knew none of this was sentient in any remote way, that something has-

**Blaise Aguera Y Arcas** [34:25]: That would feel like a big loss

**Interviewer** [34:25]: ... has been lost.

**Blaise Aguera Y Arcas** [34:26]: Yeah.

**Interviewer** [34:26]: Do you concur there?

**Blaise Aguera Y Arcas** [34:28]: I, I do, but um, but, but there's something implicit in that, in that framing that I disagree with.

**Interviewer** [34:34]: Please.

**Blaise Aguera Y Arcas** [34:34]: So a lot of, a lot of people believe that, uh, that consciousness is some ineffable... You know, either it's something we don't understand, uh, or it's some kind of ineffable je ne sais quoi that is independent of, of, of the functioning of, of-

**Interviewer** [34:49]: Yes

**Blaise Aguera Y Arcas** [34:49]: ... of a system.

**Interviewer** [34:50]: Some spiritual thing or something.

**Blaise Aguera Y Arcas** [34:51]: Right. Uh, you know, and therefore that, that you could, uh, have a philosophical zombie, for instance, you know, something that, that, you know, beha- that behaves just like you or me but is dead inside and doesn't have any consciousness. Um, and I, I actually think that's not the case. Uh, and this is connected with this mu-pi work that I just talked about as well. Basically, in order to solve this multi-agent problem, uh, you need to actually inject yourself into the, into the video game. You need to think about your own brain and your, your own, your own body and your own brain as being part of the world that you're modeling. Uh, and that's how you, you, you recognize that, you know, the others are like you. When I look at in your eyes and I'm like, you know, Dan is, Dan is like me when he smiles or makes that puzzled face. Like, I know what that feels like on the inside when I make a puzzled face or when I smile. So, you know, there are things that I know about your hidden state that I wouldn't otherwise if I didn't recognize that you and I are the same.

**Interviewer** [35:44]: Yeah.

**Blaise Aguera Y Arcas** [35:45]: And I think that that's, that is literally what consciousness is. It's that model of yourself which is an inherent part of how you get to, uh, multi-agent, uh, coordination. Now, I'm, I'm not saying, you know, every... the bacteria are conscious or something. Uh, you know, I don't think that they have the, um, cognitive capacity, if you like, to, to, to build a-

**Interviewer** [36:05]: Yeah

**Blaise Aguera Y Arcas** [36:05]: ... uh, you know, a self-model of the sort that we do. Um, but I also think that, you know, I, I mean, uh, well, I, I wouldn't feel comfortable saying, for instance, that bees are definitely not conscious. Um, you know-

**Interviewer** [36:15]: Yeah. Oh, totally

**Blaise Aguera Y Arcas** [36:15]: ... they, they have tons of rich social behaviors, and they may very well be at, at least at some basic level.

**Interviewer** [36:21]: I mean-

**Blaise Aguera Y Arcas** [36:21]: Um

**Interviewer** [36:21]: ... cephalized things, I mean, you gotta wonder-

**Blaise Aguera Y Arcas** [36:25]: Right

**Interviewer** [36:25]: ... right? I mean, you start cephalizing and, you know, you get a little, you know... But you start pulling the, you know- You boil a muscle, yeah, tough to say, you know? But, um-

**Blaise Aguera Y Arcas** [36:34]: Hard to say

**Interviewer** [36:34]: ... you know, you, you, you pull the legs off a cricket, like, you're probably a sicko, uh, on some level.

**Blaise Aguera Y Arcas** [36:38]: I agree. I agree. I-

**Interviewer** [36:39]: It's got two-- It's got two eyes. You know, it's, it's fighting you. [laughs]

**Blaise Aguera Y Arcas** [36:42]: Yeah.

**Interviewer** [36:42]: You know, it's like, um-

**Blaise Aguera Y Arcas** [36:43]: Yeah. And if you, and if you look at, if you look at, say, the behaviors of a portia spider, of a jumping spider, which are little spiders like one centimeter long, you know? They, they are, um, needing to, like, think about their prey and psych it out and ma- you know, make fake signals for it and like-

**Interviewer** [36:56]: Yeah, yeah, yeah

**Blaise Aguera Y Arcas** [36:57]: ... keep track of what it knows and doesn't know. You know, all of that theory of mind, to me, you know, is the stuff that consciousness is made out of.

**Interviewer** [37:03]: Yeah. Well, uh, well, fortunately, most of the people that have been on this show don't have a spiritual explanation of it. The-- I have had some folks say things like this: "Well, if it was built with the architecture that I know, because I kind of know what would build general intelligence, then surely it would be conscious automatically." I've heard that a number of times, and I, I, I personally believe that any certainty around exactly how consciousness would arise is, is, is pretty flatly disingenuous. And, and I know people are proud of their ideas, and they're in-- they're-- These are people with like a hundred eighty IQ. They're smarter than me, but, like, I don't agree with that. Um, but, but also, you know, some s-- Mo-most folks, I think, suspect, um... Some have said, you know, like Benio is like, "I, I, I don't know, but we should probably figure it out." From what I gather from reading your work, you're kind of like, "Hey, we, we should explore and figure this out," and it, it likely is figureable. In other words, there isn't-

**Blaise Aguera Y Arcas** [37:53]: Yeah

**Interviewer** [37:53]: ... something ineffable here. There is something to be figured out. I guess, uh, so what I, what I'm getting at is I, I don't think the positing that if there was no sentience, um, uh, it would have to be something ineffable. It strikes me that-- Well, I guess what you're getting at is, tell me if I'm wrong, if there was that grand super ecology, as you would say, thriving ecology in strata of nature and in means and modes and at scales that we can never have any conception of, if that was all doing that genuinely in, in a thriving way, it, it would sort of imply that at some point consciousness bubbled up. Uh, so you suspect that it-- So if it demonstrate that and you look down, you would say, "These things have an inner field of experience just like other things do." Am I-

**Blaise Aguera Y Arcas** [38:43]: Right

**Interviewer** [38:43]: ... following you?

**Blaise Aguera Y Arcas** [38:45]: Yeah. I, I think that, I think that if you, if you are able to, um, to plan for yourself in the future in a, in a detailed way, you know, to imagine what it's like to be you, uh, you know, in the future, uh, to, you know, interact in a rich way with others who are complex the way you are, and to think, you know, like, "What, what, what's Dan really getting at here? What does he, what does he, you know, want me to talk about?" Right? This requires that I have a f- a theory of your mind-

**Interviewer** [39:09]: Yeah

**Blaise Aguera Y Arcas** [39:09]: ... and a theory of my own mind and a theory of y- of your theory of my theory of your theory of mind and so on.

**Interviewer** [39:13]: Totally.

**Blaise Aguera Y Arcas** [39:14]: And, and for me, that's what consciousness is. That's, that's the functional role of consciousness.

**Interviewer** [39:20]: W- w- just for the sake of devil's advocate, I, I think, I think it-- that's a, a, a good jumping-off point. And again, to your point-

**Blaise Aguera Y Arcas** [39:28]: Mm-hmm

**Interviewer** [39:29]: ... um, y- you know, we shouldn't think of this as, as ineffable. You've kind of anchored to the outward signs of consciousness are these things, according to Blaise. Well, it seems rather plausible.

**Blaise Aguera Y Arcas** [39:38]: Right.

**Interviewer** [39:38]: I can imagine someone saying, "Hey, that-"

**Blaise Aguera Y Arcas** [39:40]: Now, I, I may, I may ob-- I may obviously be wrong, right? So there-

**Interviewer** [39:43]: Yeah

**Blaise Aguera Y Arcas** [39:43]: ... there may be something that we, we learn about consciousness that, that complicates or upends my picture. Uh, so I'm very, I'm very open to that possibility. But, um, but what I, what I'm-- What I feel, I guess, the most confident about is that, uh, you know, I, I would be very surprised if consciousness is some kind of weird epiphenomenon that is unrelated to our behavior, uh, and to what we've evolved to do-

**Interviewer** [40:05]: Oh, God. Totally

**Blaise Aguera Y Arcas** [40:05]: ... if that makes sense.

**Interviewer** [40:06]: So I see consciousness as a s-- as a one of the many things that bubbles out of potentia. It just-

**Blaise Aguera Y Arcas** [40:14]: Right

**Interviewer** [40:14]: ... it, it con-- it is conjured force to behoove the thing that wants to persist. It doesn't-

**Blaise Aguera Y Arcas** [40:19]: Right

**Interviewer** [40:19]: ... it's, it's, it's almost-- It's, you know, the, the appendix, uh, did something once, right? And consciousness is certainly doing something now. Um, so I'm with you there. I think-- I wonder if, you know, a submarine doesn't swim, but it kind of gets the job done, if there's, if there's a million ways to get the job done that don't involve consciousness. Or, or similarly, like, you know, we talk about, okay, well, you know, DNA, man, the most replicative monocle-- molecule or whatever. I could imagine the potentia unraveling in substrates and mediums that have nothing to do with guanine at all. Like, like where guanine has never even emerged. Like guanine has never been bumped into, and yet, uh, such, such things. So, so it strikes me that maybe complexity could be exerted through some other arbitrary means that, that sort of... And, and, and it would feel spooky. W-would you-- Well, I guess, like, what I'll say is this. Your, your theory seems very plausible. You're obviously, you know, open to learning and seeing where things go and kind of testing things.

**Blaise Aguera Y Arcas** [41:14]: Right.

**Interviewer** [41:15]: Uh, would it be correct to presume that if for some tragic, well, maybe I, I'm, I'm pre-biasing here. Let me not be biasing. Uh, you look down, all the complexity is happening. Somehow you have a consciousness detector and you can stick it into... You can touch things, and you can be like, "Ooh, are they conscious?" Uh, and l-- nothing. Nothing is. You know, it's, it's, it's-- it appears to be thriving and ecological. Things even-

**Blaise Aguera Y Arcas** [41:36]: Yeah

**Interviewer** [41:36]: ... have mouths and eyes and other organs you've never seen, and some things are operating at the femto scale or the galaxy scale. Um, but God, whatever you put them-

**Blaise Aguera Y Arcas** [41:44]: If I, if I knew, if I knew something, if I knew something about consciousness that would allow me to have high confidence that I could make a consciousness detector and I didn't see consciousness, of course I would be sad.

**Interviewer** [41:53]: Got it. Got it. Okay.

**Blaise Aguera Y Arcas** [41:53]: So yes.

**Interviewer** [41:54]: So you'd wish for it to be sentient.

**Blaise Aguera Y Arcas** [41:55]: Yes.

**Interviewer** [41:55]: Um, the other-- So, so, so you'd want it to be conscious, but you have a supposition around how consciousness arises, and you have that, that would-- you have a theory that I would think would not give you total confidence, but would give you reasonable confidence that if such an ecology emerged, we are likely to have one of these morally relevant things that we value, which is consciousness, continuing to persist with it. That's a good caveat. I appreciate you-

**Blaise Aguera Y Arcas** [42:16]: That's, that's right

**Interviewer** [42:17]: ... trickling into that.

**Blaise Aguera Y Arcas** [42:17]: And I would, I would also, I would also say that I, you know, when I-- My caveat about, about the detector comes from the following place. Um, you know, if, if consciousness is really modeling your own mind, you know, and modeling the minds of others and so on, then there's also something inherently relational about it. And what that means is that, you know, the idea of a view from above, of a consciousness detector that it, you know, in the same sense that you can make like a Geiger counter-

**Interviewer** [42:40]: Yeah, yeah. I'm being... Yeah, yeah

**Blaise Aguera Y Arcas** [42:41]: ... may actually not work. [laughs] You know? But it may, it may-

**Interviewer** [42:44]: Totally. Totally. Yeah

**Blaise Aguera Y Arcas** [42:44]: ... which is gonna-

**Interviewer** [42:45]: I, I'm being playful, silly, and fully admitting that I have no faith, only curiosity about a thousand theories of consciousness, and I am a little bit woefully disappointed in how abysmally slow progress on that has been as compared to building things stronger than humans, uh, or more-

**Blaise Aguera Y Arcas** [43:03]: Agreed

**Interviewer** [43:03]: ... capable than, than humans. It feels like, mm, damn. It'd be cool if both those tonies were-

**Blaise Aguera Y Arcas** [43:07]: I, I also would have thought that we'd, uh, I thought that we'd understand more neuroscience before we started to get AI right.

**Interviewer** [43:11]: Yeah.

**Blaise Aguera Y Arcas** [43:11]: So that is surprising.

**Interviewer** [43:12]: But [laughs] the, the, the incentives to, uh, combine forces, uh, uh, have not been as strong for consciousness, right? It, it, it, AI has been the locus of the highest, um, uh, uh, market cap corporations in the history of humanity, and consciousness seems like w- there hasn't been a reason to coordinate. Like, the, the, the interest hasn't been there to see the same kind of fil- financial singularity we're seeing now to build capability, for example. But e-either way, um, let's talk about other traits you'd wanna see. You'd said kind of rich, it is like an ecology. In other words-

**Blaise Aguera Y Arcas** [43:50]: Mm-hmm

**Interviewer** [43:50]: ... there are things that relate who combine into other things that relate, and that continues, and that continues, and that continues. Um, w- like, uh, what about that... I, I'll, I'll f- I'm gonna try to save any of my thoughts about this until after. I wanna just sprinkle it on, on you here. What about that is valuable? So rich ecology, uh, y- y- you, you know, you, you'd wanna see it. Why?

**Blaise Aguera Y Arcas** [44:18]: Well, part of it is, is, um, is aesthetic. You know, I, I think, I, I think that, um, beauty is real. Um, you know, we, we talked a little, a little while earlier about, you know, like, is it just some weird, you know, particular, like, uh, aesthetic kink of ours that we find a sunset beautiful or whatever. Um, I, I, I actually don't think so. I mean, I, I think that, I think that, um, [laughs] you know, when you look at, at, at a peacock's tail and are like, "Damn, that's really beautiful."

**Interviewer** [44:46]: [laughs]

**Blaise Aguera Y Arcas** [44:46]: Uh, and then you realize, oh, peacocks have actually, you know, peacocks and peahe- or peahens more specifically-

**Interviewer** [44:51]: Yes, yes

**Blaise Aguera Y Arcas** [44:51]: ... have selected for that thing. You know, it's like, well, they, th-they obviously have aesthetics as well, you know, or, or insects and flowers and vice versa, you know? And, and so, um, I, I think that, um, you know, there, uh, that, that complexity and, um, and these kind of multi-scale sophistication and, uh, you know, intricacy and all these kinds of things, uh, you know, have... I, I think that I, I, I don't, I wouldn't go so far as to say like, let's define that mathematically, but, um, but I do think that there's something, um, you know, you know, that goes beyond our peculiar human tastes about this and, um, and I, and I identify it as good. I identify, you know, that kind of complexity and richness as good, uh, in, in a way that transcends my, my, you know, my own, uh, you know, proximal needs. Um, but I, I'd also say, you know, w- we, you, you mentioned, um, or we, we talked a little bit about continuity before as well. You know, I would definitely feel very, very different about a future in which, you know, we all, um, died, uh, you know, of a giant plague or a, you know, a, a, a runaway nuclear, uh, confrontation next week. And, you know, the future we're looking at is, you know, uh, seventy million years in the future, um, and there's great complexity and it's wonderful, but all of that, you know, emerged, uh, you know, from scratch or, or from Portia spiders or, or some other, or some other organism and didn't have anything to do with our lineage. Uh, that, that would be disappointing too, um, because I feel like we've come a long way and, you know, yes, nature always has, you know, the snakes and ladders, but you know, you're always rooting for like, you know, uh, not only for, for, uh, for the collapses not to happen, but also for something about the things that you have been a part of and built to, to be, uh, to be a part of what, of what persists.

**Interviewer** [46:39]: Y- you would hope that, um, as the great flame blazes on, some part of its frontier was connected to the torch you once held. Um-

**Blaise Aguera Y Arcas** [46:47]: Yeah

**Interviewer** [46:48]: ... and, a-and, and-

**Blaise Aguera Y Arcas** [46:48]: Yeah. Absolutely

**Interviewer** [46:49]: ... and, uh, torches are temporary, so torches are individuals, species, and substrates. They're all-

**Blaise Aguera Y Arcas** [46:56]: Right

**Interviewer** [46:57]: ... persistence is a matter of degrees-

**Blaise Aguera Y Arcas** [46:59]: Yes

**Interviewer** [46:59]: ... across the board. Uh, and so-

**Blaise Aguera Y Arcas** [47:02]: Yes

**Interviewer** [47:02]: ... um, and so-

**Blaise Aguera Y Arcas** [47:02]: It's, it's cycles, cycles within cycles. Everything dies, and everything that dies is part of a bigger thing that lives. Um-

**Interviewer** [47:08]: Totally. Totally. And so, and so, but the continuity thing, like I would imagine if f- i- i- because there, there are, there are many people, in fact I... Part of me really hopes it's not most of the people listening to this, but, but it's because my audience is, ooh, geez, that, that's a, that's a pretty narrow band of humans that think about this kind of thing. But, um, but, uh, the bulk of living hominids would essentially see most... unless maybe they thought about it for a long time or something, would see everything as a bad future that wasn't an eternal hominid kingdom. That is to say, the locus of volition and moral value until the heat death of the universe has opposable thumbs and talks like you and me and whatever. Uh, and maybe it's not English anymore and, you know, maybe they're, they're on Mars and they have, you know, uh, have sports, new sports or something. But, um, but like that would be it until, until the, the heat death there. Uh, y- y- I, I would guess big picture, y- you know, the, the, the continuing blaze is very, very high. 'Cause it seems to me, and you can push back on this if you'd like, it seems to me as if the continued unraveling ensures the persistence of the process of which we are part.

**Blaise Aguera Y Arcas** [48:16]: Right.

**Interviewer** [48:16]: And it would strike me that marriage to any one torch at the q- which marriage to any one torch in a deep eternal lock-in way is scorn for the flame actually, um, as it turns out. And I think that's really uncouth to say, um, but I'm willing to say uncouth things I believe to be true. And, and so-

**Blaise Aguera Y Arcas** [48:35]: I, I don't, I don't disagree. I don't disagree with what you're saying, but I, I also think, I also think that it's reasonable for, um, people to have Uh, you know, commit-- I mean, it's, it's built into us by evolution, right?

**Interviewer** [48:46]: Of course.

**Blaise Aguera Y Arcas** [48:46]: To have some commitments to our, our own propagation for whatever value of our, right? It could be a genetic lineage, it could be a religion, it could be a state, it could be, you know, a commitment to humanity as a whole, to our planet, um, you know, what have you. Uh, and, um, you know, and that's part of the force that, that, that, that produces that, that very flame. So, you know, it's not something that is easy to just, you know, say it's wrong. Um, you know, you, you, you mentioned that everybody's got their, their limit, right? Their sort of radius of what would be all right.

**Interviewer** [49:16]: Yes.

**Blaise Aguera Y Arcas** [49:16]: You know, most people I think if we... Uh, I mean, I, I'm, I'm unconvinced that we'll ever, you know, like, do large scale colonization of other planets. But let's pretend for a second-

**Interviewer** [49:23]: Same here. Same here

**Blaise Aguera Y Arcas** [49:23]: ... that we do. Suppose that, suppose that we did do it on Mars and that we had some cool adaptations, uh, that we managed to genetically engineer for being able to, you know, survive at lower pressure, right? So people are s-still people, but you know, they've, they've got, they've got, uh, you know, slightly modified lungs in order to be able to survive at, at point one atmosphere, you know-

**Interviewer** [49:43]: Yes. [laughs]

**Blaise Aguera Y Arcas** [49:43]: ... without any problems.

**Interviewer** [49:44]: Yeah.

**Blaise Aguera Y Arcas** [49:44]: Like, would anybody say, "No, that's, that's not..." Yeah, there are some people who would probably say, "That's not human anymore."

**Interviewer** [49:49]: There are.

**Blaise Aguera Y Arcas** [49:49]: That's, that's anathema.

**Interviewer** [49:50]: There are.

**Blaise Aguera Y Arcas** [49:50]: But I think most would be like, "That's cool. You know, if, if that's my great-great-grandchildren, like, I'm okay with it." Um, and then the thing to understand is just like, well, if you add up, you know, a, a million changes of that sort, you now have something profoundly alien. And-

**Interviewer** [50:05]: Of course

**Blaise Aguera Y Arcas** [50:05]: ... and, um, you know, but at the same time, you know, our, our great-great-grandchildren with the one-tenth atmosphere lungs, you know, their threshold is, you know, is, is advanced a little further because they're in a different spot. So, you know, there is a rate of change kind of argument there, uh-

**Interviewer** [50:20]: Yeah

**Blaise Aguera Y Arcas** [50:20]: ... that I think is reasonable.

**Interviewer** [50:21]: And, and I, I think, I think there is a rational fear to gigantic disjointed changes because we all understand-

**Blaise Aguera Y Arcas** [50:29]: Of course

**Interviewer** [50:29]: ... and everywhere else in life you're gonna pay the cost of change, and you don't know if you're gonna get the benefit. So yes, the river of Heraclitus is moving faster than ever. Changes are gonna be woo, we're gonna be Sonic the Hedgehog over here. However, we don't want them to be so zippity-zappity disjointed that somebody drops the torch and the whole thing-

**Blaise Aguera Y Arcas** [50:47]: I agree

**Interviewer** [50:47]: ... is like, is, is put, is put at risk. So to that point-

**Blaise Aguera Y Arcas** [50:50]: I, I, I completely agree then. I, I am not into revolutions.

**Interviewer** [50:53]: Yeah.

**Blaise Aguera Y Arcas** [50:53]: You know, uh, like r-revolutions, uh, you know, tend to hurt a lot of people and destroy a lot of things that needn't have been destroyed, which, you know, which more incremental change could have resulted in, you know, like-

**Interviewer** [51:05]: Yeah

**Blaise Aguera Y Arcas** [51:05]: ... right, all, all of the upsides without all of the tears.

**Interviewer** [51:08]: Yeah.

**Blaise Aguera Y Arcas** [51:08]: So I, I totally agree.

**Interviewer** [51:10]: Yeah. Um, take that Robespierre. You heard it on this podcast. Um, so, uh, with, with, with that stated-

**Blaise Aguera Y Arcas** [51:15]: Great example. Great example of a very trusting revolution. [laughs]

**Interviewer** [51:17]: [laughs] Oh, yeah. I, I, yeah, not, not his biggest fan here. Um-

**Blaise Aguera Y Arcas** [51:20]: Yeah

**Interviewer** [51:20]: ... so, uh, w- uh, um, uh, you brought up beauty. Uh, it's interesting because there's a lot of really smart people who I think are great, who bring up beauty a lot in this conversation. And, um, you know, Whitehead, his pro-process philosophy, uh, Alfred North Whitehead or what have you, I think talks about sort of everything kind of a grand culmination to beauty. My, my initial response to that is that it is possible that that which is shining forth is indicative of some deeper kind of value that correlates to some qualia type of joy that's hyper ubiquitous to, uh, uh, um, the hens of the peacock as well as to, you know, a polar bear, as well as to, you know, whatever. It, it also strikes me that like, you know, to a fly, certain kinds of rotting things may be particularly beautiful and to-

**Blaise Aguera Y Arcas** [52:14]: Yeah

**Interviewer** [52:14]: ... a certain kind of bat, certain kinds of rock crevices that have all kinds of bacteria that would kill you, uh, are par-are particularly beautiful. And so-

**Blaise Aguera Y Arcas** [52:22]: Yes

**Interviewer** [52:23]: ... I, I, I, I-

**Blaise Aguera Y Arcas** [52:24]: I think all those things are beautiful too. [laughs]

**Interviewer** [52:26]: [laughs] It's all good.

**Blaise Aguera Y Arcas** [52:29]: Yeah. I'm using a pretty, I'm using a pretty broad-

**Interviewer** [52:31]: Okay. I get it

**Blaise Aguera Y Arcas** [52:32]: ... a pretty broad brush.

**Interviewer** [52:32]: That, that makes sense. I, I, I, um, I, I like that you're light with your... You're, you're, you're, um, you're, you're touching the implied thing. You're, you're touching the implied becoming when you touch a thing. Most people touch the thing. They don't, they don't touch. So this one fact the world hates that the soul becomes, says Emerson, right? And, uh, people hate it, Blaze. People hate it. I mean, like, they hate it, brother. Like, uh, the whole, like even the Mars lung thing, like a lot, like there's people who [laughs] fucking have guns in the street around that. So people even-- and that's incremental, never mind the alien inevitability you spoke of. Um-

**Blaise Aguera Y Arcas** [53:08]: Well, I mean, you're, you're talk-you're talking about, about a certain, you know, sort of, uh, you know, purity values. I mean, uh, you know, uh, Jonathan Haidt has done a lot of work on these kind of moral foundations.

**Interviewer** [53:17]: He has. He has, yes.

**Blaise Aguera Y Arcas** [53:18]: You know, and, and what I really like about his work is that he also points out the value of-

**Interviewer** [53:22]: Of course

**Blaise Aguera Y Arcas** [53:22]: ... of some of those conservative-

**Interviewer** [53:24]: Of course

**Blaise Aguera Y Arcas** [53:24]: ... values, right? They're, they're there for a reason.

**Interviewer** [53:26]: Yes. Yep.

**Blaise Aguera Y Arcas** [53:26]: Uh, so I, I, I, I s- I, I acknowledge, right, their, their value and their importance, uh, even if I don't always share them.

**Interviewer** [53:33]: Totally.

**Blaise Aguera Y Arcas** [53:33]: And I think the diversity, right, of, of perspectives on this is actually really important. The fact that the, the bat, you know, finds that crevice beautiful and doesn't find the flower beautiful, I don't fault the bat for this, you know, or-

**Interviewer** [53:44]: No, of course not

**Blaise Aguera Y Arcas** [53:44]: ... or think like the bat has a moral deficiency in that regard.

**Interviewer** [53:46]: Yeah.

**Blaise Aguera Y Arcas** [53:47]: Um, you know, and, and, and, and the same goes for, for people who disagree with me about some of this kind of stuff.

**Interviewer** [53:52]: Yeah. No. Well, I, I, I, I completely do too. I've never said, "Oh, well, everyone should surely..." I, I do think that with enough reflection, understanding that in the long term... So what I d- what I, what I end up not kind of respecting is like, no things have to stop changing. That's like, hmm, now you want impossible stuff. That I think we just should really get up to snuff about reality. But I think the notion of this ought not change within my lifetime or my great-grandchildren, but like, but still understanding that the world is flux and maybe knowing that we do have to surf it, that's at least a mission-- That's at least admission that we are living in the world. When you pretend to freeze, uh, the state of things, when you pretend to freeze the Heraclitean river, uh, I, I, mmh, I, I, you know, I-- That, that, that I, ooh. You know, I, I-- There's a place for values, but I don't think there's a place for denying reality. Wi-with that said, maybe there is, I don't know. Your ecological view would probably have a better take there. Let me just put this on the table about beauty. Um- When I look at the purpose of the ecological blossoming, I'll posit a couple things and see if you like or dislike these. Um, I'm glad to have your idea of it. Now I know what to write down for worthy successor criteria for you. Um, two things strike me. When this agglomerative force, and I think you've really articulated a cool way to understand the arrow of evolution. Again, I'm, I'm probably gonna quote the heck out of that, to be honest. Um, the, the, uh, two things strike me as what happens when that occurs. Number one, it seems to me that the flame itself is less likely to go out. In other words, the project-

**Blaise Aguera Y Arcas** [55:27]: Yes

**Interviewer** [55:27]: ... of non-dead stuff existing is more likely to persist if the unfurling of the magazines of potentia keep going. So, so this-- if you, if you th- so if you're like, "Oh, it's beauty, it's this, it's that," well, there's none of that if nothing experiences it. So for me-

**Blaise Aguera Y Arcas** [55:43]: Mm-hmm

**Interviewer** [55:43]: ... the mandate towards persistence is not about brutalism and being tough and being fighting and killing and tooth and claw. It's like, no, no, no, persistence should be the first goal because whatever you value is only valuable if something can persist to enjoy it or experience it or create it or what have you. So that's one that I would say the unfurling-

**Blaise Aguera Y Arcas** [56:01]: I, I agree. I mean, the, the very, the very existence of values comes from the, the, the persistence principle, if you like.

**Interviewer** [56:08]: A, a hundred percent. And, uh, um, uh, I now I have to Google if there is something called a persistence pr- principle. I just keep referencing Spinoza all the time. But, but I, I do think that that's, um... Yes, I'm with you there. So for me, that would, that would undergird any value of beauty. It's like, well, jeepers, some- something's got to exist. Secondly, I think that the things we value bubbled up from nothing. So think about this. There was a time where there was no consciousness, and then [snaps finger] things were conscious. That's wild. And, and of course, it, I think, independently potentially bubbled up in different places. Of course, we don't know what's conscious, but we can presume different species are conscious. Say, "Wow, it bubbled up in this line, it bubbled up in this line, it bubbled up in this line." Um, I would bet that there are things beyond consciousness as we know it, not just new, deeper flavors of consciousness, not just a level a hundred instead of a level ten, but something categorically different that is as if not more valuable than consciousness. And then if we keep going, another thing opens up. And then if we keep going, another thing opens up. Things for which we, you and I have no words. The nematode will never conceive of this conversation you and I are having. The nematode will never know whether it's riding in an airplane or it's a, a million feet underground or whatever. Um, uh, y- I would guess you and I have no access to the magazines of value. So we say beauty, and I say, you know, I, I think, I think it's an okay one. I would like the unfurling of all the magazines of value for which I have no words. And so for me, persistence of the stuff and the unfolding of all categories of value is the mandate for why I would want the thriving ecology. Um, I'd love to know what parts of that you wanna push against if, if beauty is a different thing than what I've articulated, or if you have a different way of conceptualizing it.

**Blaise Aguera Y Arcas** [57:56]: No, uh, I, I think you're right. Um, you know, if, if, um... I had a, I had a really interesting conversation with David Deutsch a, a few weeks ago.

**Interviewer** [58:04]: Oh, man. Wow. I would've loved to be a fly on the wall there.

**Blaise Aguera Y Arcas** [58:07]: It was fun. We recorded part of it, so it will-

**Interviewer** [58:09]: Oh, good

**Blaise Aguera Y Arcas** [58:09]: ... it will eventually come out.

**Interviewer** [58:10]: Yeah.

**Blaise Aguera Y Arcas** [58:10]: Um, but, um, uh, uh, but yeah, it was for, for the Futurology, uh, uh, podcast, I think is, is where, where it'll eventually, uh, get, get published. But, um, he believes that, that, um, and this is a point that he made in his book, uh, you know, The Beginning of Infinity, that once you have rationality or general intelligence of the kind that, you know, you and I have got, that's a step function, and that's it. It's like Turing completeness. You know, it's sort of the, um, everything else is, is, is, uh, just more of that. Um, I, I am more where you are than where he is. Uh, I think it's-

**Interviewer** [58:44]: Oh, I, I wanna, I wanna, I wanna puke everything I've eaten in the last two weeks out when I hear that. I, I, I, I can't, I can't, I can't even deal with that presumption of understanding of grasp of the totality of nature, um, through-

**Blaise Aguera Y Arcas** [58:58]: No, he's, I mean, he's a, he's a very, he's a very smart guy. Uh, so-

**Interviewer** [59:00]: Of course he is, but-

**Blaise Aguera Y Arcas** [59:01]: You know, his, his perspective is not, is not one that I'm comfortable to, uh, you know, to, to just sort of like, uh-

**Interviewer** [59:07]: Well, c- certainly, I can respect the man-

**Blaise Aguera Y Arcas** [59:08]: This is how to think

**Interviewer** [59:08]: ... but be like, that idea feels just off, you know?

**Blaise Aguera Y Arcas** [59:12]: Well, yeah. I mean, when we look, when we look at what has become possible, uh, you know, just in the last couple of centuries, uh, you know, what kinds of things were unimaginable, uh, you know, that, that we take to be commonplace now that, that just didn't exist a couple of hundred years ago. You know, it's, it's, um, it's humbling, right? And, and, and yes, I mean, I, I, I think one of the, one of the things that, that gives you your, your, um, your sense of, uh, both optimism and of, of how big the possibilities are, uh, going forward is taking a little bit of a wider view of, of just how much things have ch- have already changed in our past. Um, you know, there, there have been some economists I'm thinking of, of, uh, um, uh, slouching toward, uh, utopia. What's, what's his name? Um, a couple of others. Um, oh, shit. I'm, I'm, I'm, I, I need to, I need to-

**Interviewer** [60:03]: It's all good

**Blaise Aguera Y Arcas** [60:04]: ... I need to have another coffee. But, but there, there, there, there's more than one economist who has made the argument that basically the amount, the amount that things changed from eighteen seventy to nineteen seventy just absolutely, you know, dwarfs what happened between nineteen seventy and twenty twenty. You know, the last fifty years have been quite static relative to what happened in the previous century. Um, I think it's a good argument. I mean, when you really look at, at, you know, how unfamiliar the world would've been if you went to sleep, you know, like, uh, Rip Van Winkle or something in eighteen seventy and, and woke up in nineteen twenty. I mean-

**Interviewer** [60:33]: Incredible

**Blaise Aguera Y Arcas** [60:34]: ... you know, it would be insane, right? Like-

**Interviewer** [60:36]: Incredible

**Blaise Aguera Y Arcas** [60:36]: ... like everything would be completely unfamiliar. If you went to sleep in nineteen seventy and you woke up today, you know, it'd be cool that there-- that we have computers and phones, but, you know, and not anything like the same kind of, of, of radical change.

**Interviewer** [60:47]: It's a good point. It's a really good point.

**Blaise Aguera Y Arcas** [60:49]: But, um, and, and so I think in a way we've gotten used to, uh, you know, stasis again in a way that, you know, if you were J.R.R. Tolkien, you know, who, uh, when he was a kid, like the cavalry charge was still a thing, and by the time he died, we had the hydrogen bomb. You know? [laughs]

**Interviewer** [61:03]: [laughs] Yeah.

**Blaise Aguera Y Arcas** [61:03]: Like you can understand why, why he invented Middle Earth, you know? [laughs]

**Interviewer** [61:07]: [laughs] Yeah. Wow.

**Blaise Aguera Y Arcas** [61:08]: Um, and, uh, and, and I think we're, I think we're, we're, we're kind of speeding up again. Uh, you know, my sense is that starting in twenty-twenty, like, you know, th-things are kind of back in turbo.

**Interviewer** [61:17]: Yeah.

**Blaise Aguera Y Arcas** [61:17]: And, uh, and, and that's uncomfortable for a lot of people who are, um, you know, who have, have, have lost their, their, their sense of how fast things can change.

**Interviewer** [61:27]: Yeah. This one fact the world hates. Uh, so but we're, but we're riding it, brother. And, and I think, yeah, uh, I, I certainly have that same sentiment here, and I, I think that A-A-AI, AGI are certainly a big part of that. I wanna touch on one more thing before we get into how we might measure some of these valuable traits or at least hypothesize how we might know if we're getting closer to them. Symbiosis clearly involves us and of course your hope, and I, I would say probably everybody tuned in more or less, uh, I, I, I suspect I'd be in this camp, would like, you know, some degree of continuity. Could part of our flame fee-- or part of our torch feed into the grander flame? Uh-

**Blaise Aguera Y Arcas** [62:03]: Right

**Interviewer** [62:03]: ... that would be pretty cool. Um, you know, we, we might not be humans as they are, but, you know, our components, you know, p-partially kind of merger, um, you know-

**Blaise Aguera Y Arcas** [62:11]: For some value of we or us, yeah.

**Interviewer** [62:13]: Yeah. When, when you, um, uh... And I think it depends on what you identify with. I think that it will be very-- it will be increasingly challenging to identify with only twenty, you know, uh, twenty-three chromosome pairs or whatever. I think it's gonna be very hard to identify with just opposable thumbs. I think identifying with bio life will be more common and then maybe identifying with the process of life will be more common because I think it'll just-- it'll be untenable. It's like the people who identified with making horse carriages. It's like, I don't know, man. I just don't-- I don't know how long you can do that. Um, but like, um, the, uh, um-

**Blaise Aguera Y Arcas** [62:44]: The horses that are still around are, are probably quite a lot happier nowadays-

**Interviewer** [62:46]: Oh, they're doing good [laughs]

**Blaise Aguera Y Arcas** [62:47]: ... than they were in, like, the seventeenth century. [laughs]

**Interviewer** [62:48]: Yes, yes. [laughs] A, a, a pretty good chunk of them got, uh, got a pretty specific treatment. But yes, the ones that are here now, hey, what the heck? Um, with that said-

**Blaise Aguera Y Arcas** [62:56]: It's a, it's a good life if you're like, uh, you know, Sunday, you know. Yeah.

**Interviewer** [62:59]: A-absolutely. You get like, uh, you know, people pay good money to have the kids come out and feed you and, you know-

**Blaise Aguera Y Arcas** [63:04]: That's right

**Interviewer** [63:04]: ... you're not, you're not carrying heavy stuff anymore. Like, that's awesome. Um-

**Blaise Aguera Y Arcas** [63:08]: Exactly

**Interviewer** [63:08]: ... when you look at the next couple clicks up in complexity, and neither you nor I have any idea what the grand expanse is, and I, I like your frankness about that. Some people like to think that they know what that picture turns into. It's, it's pretty clear we don't. Um, but you look up a couple clicks at where a symbiosis with this intelligence would come in.

**Blaise Aguera Y Arcas** [63:26]: Mm-hmm.

**Interviewer** [63:26]: I suspect not all of it will be warm and fuzzy and friendly forever. It certainly won't always be continuity with what we know now. But maybe the next couple clicks will involve kinds of symbiosis most people haven't thought about and maybe you have. What's some pictures you can put in our heads about what some of those clicks and symbioses could look like as AGI comes onto the scene?

**Blaise Aguera Y Arcas** [63:46]: Well, um, I guess a couple of observations. Um, one is that, um, our last big, um, technological symbiosis, I think, was, um, the development of steam engines and the Industrial Revolution. Uh, you know, that's so, you know, we, we first started by making these machines by hand, making them originally, and then, you know, having machines make machines, et cetera. And, uh, so obviously the machines don't exist without people. But what I think a lot of people forget is that there would be a lot fewer people also without those machines. Uh, you know, what we essentially did is we started to metabolize externally, uh, on a massive scale. In that sense, it's, it's not so unlike the mitochondrion. You know, the, the steam engine-

**Interviewer** [64:26]: Yeah

**Blaise Aguera Y Arcas** [64:26]: ... was our new mitochondrion.

**Interviewer** [64:28]: Yeah.

**Blaise Aguera Y Arcas** [64:28]: And, you know, the population going up from one billion to ten billion, you know, is a hundred percent a function of, of, um, you know, of the Industrial Revolution. Uh, so, you know, that, that, that energy production pulled us out of this, of this Malthusian cycle where we were, you know, limited by, by, um, by mortality and by calories and rocketed us into a different spot. Um, so, so that last, that last symbiotic change, you know, um, sort of finished the job of increasing human numbers. We know in the next century that human numbers are not continuing to increase exponentially, and that's a lucky thing because, uh, you know, if you don't believe that we're going to have massive numbers of people off planet, there are obvious limits.

**Interviewer** [65:09]: It's gonna be tough to hold them all, yeah.

**Blaise Aguera Y Arcas** [65:11]: Right. And, and luckily, you know, all of those anxieties about the population bomb, you know, of Paul Ehrlich and so on are absolutely not, you know, that's not the future that we're looking at over the next century. We are, you know, leveling off, and our numbers will probably, you know, settle at, at something, uh, more modest. Uh, so this symbi-- this, this new symbiosis with technology is gonna look quite different from the Industrial Revolution's one, which is all about just, you know, harnessing industrial energy and getting us out of a Malthusian state. We're already not in a Malthusian state anymore, uh, the overwhelming majority of humans, uh, today.

**Interviewer** [65:44]: Yeah.

**Blaise Aguera Y Arcas** [65:45]: Um, there are a few, there are a few left. I don't, and I don't wanna minimize, you know, the, the suffering of those-

**Interviewer** [65:49]: Of course. Of course

**Blaise Aguera Y Arcas** [65:49]: ... who are still under those conditions. But, but, you know, we're well on our way to, to getting, getting past that stage. Um, and, uh, and you know, I think one of the, one of the consequences of that is that in not very long, there are going to be many, many more AIs than people. Um-

**Interviewer** [66:06]: Oh.

**Blaise Aguera Y Arcas** [66:07]: You know, if you... Right? I mean, we're-- that's kind of just around the corner.

**Interviewer** [66:10]: Yeah.

**Blaise Aguera Y Arcas** [66:11]: Um, so, so we're, we're looking at... You know, if you think about all of, you know, people and AIs, you know, both as nodes in a graph with all kinds of relations between them, the people are the rarer, uh, you know, objects in the, in that graph in, in the near future. I don't think a lot of people have really thought about that and its implications-

**Interviewer** [66:28]: No

**Blaise Aguera Y Arcas** [66:28]: ... because we're still, we're still imagining that, you know, one AI per person is kind of the limit in the same sense that people were imagining that one computer per person had to be the limit-

**Interviewer** [66:38]: Yeah

**Blaise Aguera Y Arcas** [66:38]: ... you know, in nineteen eighty, right? And, and the reality now, of course, is that the amount-

**Interviewer** [66:42]: Per household maybe

**Blaise Aguera Y Arcas** [66:42]: ... you get in your car. Yeah. I mean, your car has like two hundred cores in it, you know? [laughs]

**Interviewer** [66:47]: Yeah. [laughs]

**Blaise Aguera Y Arcas** [66:48]: And, and even, even the, even the mi-- the, the microcontroller that is just for the power window, uh, you know, has more processing power than all computers on Earth did in nineteen fifty. So, um-

**Interviewer** [66:57]: Insane

**Blaise Aguera Y Arcas** [66:58]: Yeah. Yeah

**Interviewer** [66:58]: Uh, in- insane. So, wow. I, I, uh, um, okay. So, uh, well, when we think about that expansion of the node and the graph and all the acting agents and whatnot, it strikes me that clearly right now we're pretty darn relevant to th- the AI because we interact with the world in ways that they don't. Although-

**Blaise Aguera Y Arcas** [67:20]: hundred percent

**Interviewer** [67:20]: ... soon I think the, we'll be able to replicate biped robots and other me- kinds of robots in various forms faster than-

**Blaise Aguera Y Arcas** [67:28]: Totally

**Interviewer** [67:28]: ... humans can replicate

**Blaise Aguera Y Arcas** [67:28]: There's, there's a lot of, there's a lot of really good work on robotics that suggests to me that's very tempting.

**Interviewer** [67:31]: Of course, it's really kicking-

**Blaise Aguera Y Arcas** [67:32]: Right

**Interviewer** [67:32]: ... kicking in.

**Blaise Aguera Y Arcas** [67:33]: Mm-hmm.

**Interviewer** [67:33]: It strikes me that we probably contribute for a certain amount of time. Uh, so you know, uh, like I, I, I, um, uh, I'm thinking of all the analogies. Horses is like a-- It's played out. I don't wanna just use horses, but like, whatever, just to throw it on the table. At some point, you know, horses were a big part of the mix and, and, and they, they became part of the mix in the New World, and then they became-

**Blaise Aguera Y Arcas** [68:00]: Yeah

**Interviewer** [68:00]: ... part of the mix, you know, all over the place. And, and, um, uh, a- and, and they were doing work, they were doing war, they were doing other things, they were doing recreation. Um, and, and, uh, you know, now there's still like the hobby community or whatever, but, um, they're, they're just not, they're not contributing to, they're not contributing to the stream of life. So there was a time where they were giving into the great system you're talking about with those cycles. They were giving something. You talked about the, the mutual combination. I think that's the only honest way to talk about it. It's in the mutual self-interest to do that. Now-

**Blaise Aguera Y Arcas** [68:35]: Mm-hmm

**Interviewer** [68:35]: ... you know, we do things like donate to keep the piping plover alive on the beaches of Rhode Island and Massachusetts somewhere, uh, just because like, oh yeah, you know, let's pay for that species. It's actually quite questionable if that's a grift because there's somebody who gets paid like a bunch of money to like carve out that land, and if like, if it's feigned as like, "Oh, yeah, saving this one species is super crucial," or if it's like a dude figured out that like if you own this kind of beach land, like you'll get a ton of government money. Like, I'm not really sure, to be honest. But-

**Blaise Aguera Y Arcas** [69:00]: Yeah

**Interviewer** [69:01]: ... what I will say is-

**Blaise Aguera Y Arcas** [69:01]: Well, I mean maybe, maybe another, maybe another argument in y- in the direction you're, you're, you're-

**Interviewer** [69:05]: Yes

**Blaise Aguera Y Arcas** [69:05]: ... pointing is that, [sniffs] um, you know, Trout Unlimited and, uh, ducks, you know, the, the-- there's sort of these associations for preserving, um, uh, wetlands for duck hunting-

**Interviewer** [69:15]: Huh

**Blaise Aguera Y Arcas** [69:15]: ... which have been much, much more successful than things like the, the plover effort. You know, the, the fact that, that, um, uh, you know, avian waterfowl are the, are the, are the only avian population that's not in decline in North America is actually true because we hunt them. [chuckles] Um-

**Interviewer** [69:30]: [laughs]

**Blaise Aguera Y Arcas** [69:30]: And it's the hunters that, that are, that are-

**Interviewer** [69:32]: A portent for man, ladies and gentlemen. A portent for man. No, I'm joking. Uh-

**Blaise Aguera Y Arcas** [69:35]: To be clear, I'm, I'm, I'm absolutely not saying-

**Interviewer** [69:37]: I get it. I get it. No, I, I totally-

**Blaise Aguera Y Arcas** [69:38]: ... people are going to survive because, uh-

**Interviewer** [69:39]: I totally get it

**Blaise Aguera Y Arcas** [69:40]: ... because robots will hunt them.

**Interviewer** [69:42]: Yeah.

**Blaise Aguera Y Arcas** [69:42]: Uh, what I'm saying is that, is that the, the, uh, the animals that we have real w- real working relationships with, right, are, are, uh, are the ones where, you know, where there's, where there is that sense of mutualism. Like, you know, it's the hunters that are, that are doing the most to protect the wetlands of the, of the US.

**Interviewer** [69:59]: Very curious. That is a-

**Blaise Aguera Y Arcas** [70:00]: Yeah

**Interviewer** [70:01]: ... fascinating element of the symbiosis you're talking about. And I guess what I think about is, okay, people say, "Well, we take care of cats, don't we?" You mentioned horses.

**Blaise Aguera Y Arcas** [70:10]: Yeah.

**Interviewer** [70:10]: Here's what I say. Take the net potential of all the humans that exist on Earth and just [snaps finger] double it. So double the number of physical senses, double the amount of memory, double, uh, the cognitive capability, double, double everything. Double the how high we can jump. Just double it all. Just take out-- take all measurable potential about humans and double it. And then ask, are they still interested in scooping the litter box or riding the horse or whatever? And you might-- And maybe the answer is yes. [snaps finger] Double it again. [snaps finger] Double it again. [snaps finger] Double it again. [snaps finger] Double it again. How many doublings do you have until it's not remotely interesting? I don't wanna shoot waterfowl anymore, damn it. I have other things to do. Cosmic things that actually matter, that are in the grander stream. They matter. They're useful. And how, how many doublings? And how, how quick are the doublings gonna happen with AI? Now, I'm not saying like this is immediate terrible portent for man by any means. I'm simply saying I see persistence is a matter of degrees as being visibly observable in the near term. I see it as being visible. And so what, what be your thoughts there regarding symbiosis?

**Blaise Aguera Y Arcas** [71:15]: Well, um, look, I, I think that, um, our, our, um, reverence for, um, for wild places on Earth has only grown, uh, with, with our, with our increase in sophistication and in particular with our, our ability to, um, uh, for in- for instance, generate energy in more efficient ways, uh, you know, than burning wood, for instance. Um, you know, or, or, uh, um, you know, our ability to, to, uh... You know, the, the whole, the whole, um, parklands, uh, movement, you know, national forests and-

**Interviewer** [71:50]: Yes

**Blaise Aguera Y Arcas** [71:50]: ... and pro- and protected zones and so on, like all of that, um, you know, is, is, is actually a function of our wealth and our development, uh, intellectually. Uh, you know, there was, there was no such, no such, uh, movement, [chuckles] you know, uh, when, when, uh, um, the Europeans first came to the New World.

**Interviewer** [72:07]: Absolutely not. Yeah.

**Blaise Aguera Y Arcas** [72:08]: Um, now, there, there wa- there were, there were, of course, a lot of indigenous traditions in which, uh, in which nature was, um, was respected for exactly the same reasons that, that, you know, duck hunters, uh, you know, uh, respect the-

**Interviewer** [72:20]: Yeah

**Blaise Aguera Y Arcas** [72:20]: ... wetlands.

**Interviewer** [72:21]: Yeah.

**Blaise Aguera Y Arcas** [72:21]: Uh, Robin, Robin Wall Kimmerer has written a lot about those.

**Interviewer** [72:24]: That's cool.

**Blaise Aguera Y Arcas** [72:25]: Um, and I, I think, I think she's a, you know, she's a really good thinker about these kind of questions of symbiosis.

**Interviewer** [72:30]: Mm.

**Blaise Aguera Y Arcas** [72:30]: But, you know, national parks and stuff aren't-- They're, they're not just an instrumental, uh, uh, good. Uh, they, they are, uh, they're, they're really, you know, us coming to understand that it's not zero-sum between all of the things that, uh, you know, that, that we're going for, right, with all of our incredible intellectual sophistication. Like the idea that, you know, oh, people who are off solving theorems are not interested in forests anymore. Not actually the case, right? I suspect that, that, you know, if you, if you were to poll all of the theorem solvers in the world, you know, about their, uh, you know, how mu- how much they care about nature versus all of the, um, you know, the, the remaining people who, who are, um, say, you know, am- among the urban poor, um, you know, you're not gonna find, uh, you know, this, this correlation where, you know, people just give less and less of a shit about nature as they, as they pursue more and more intellectual activities.

**Interviewer** [73:18]: Yeah.

**Blaise Aguera Y Arcas** [73:18]: So, so I, I, um- You know, I, I don't wanna draw too direct an analogy because, you know, as you say, we don't know, right, what's coming in the future.

**Interviewer** [73:26]: Of course.

**Blaise Aguera Y Arcas** [73:26]: But, but when I think about, about what the desiderata might be of extremely sophisticated hybrid and or machine intelligences, you know, there is a, there is an entire solar system out there worth of incredible amounts of energy and resources that are absolutely non-zero sum with all of the beautiful things that exist on Earth. Um-

**Interviewer** [73:49]: Yeah. Yeah

**Blaise Aguera Y Arcas** [73:49]: ... and, uh, you know, I-- When, when you, when you try and think about zero sum sorts of pictures like in The Matrix, right, you end up with some pretty absurd like, oh, you know, like our spinal fluid really matters to the computers or something else.

**Interviewer** [74:00]: No. Yeah. I, I don't believe that.

**Blaise Aguera Y Arcas** [74:01]: You know what I mean? [laughs]

**Interviewer** [74:02]: But I, I, I don't, I don't believe that. I-

**Blaise Aguera Y Arcas** [74:03]: So that, that seems impossible to me

**Interviewer** [74:05]: ... I'm simply just not convinced that when you keep doubling potentia-

**Blaise Aguera Y Arcas** [74:09]: Mm-hmm

**Interviewer** [74:09]: ... consideration will occur or even should occur. That's uncouth. You p-- you can't say it. You have an employer. I, I, I'm allowed to say what-- 'cause who's gonna fire-- nobody can fire me. So, um, but, but yeah. But I see where you're headed, and I, I hope maybe in a hundred or thousand years to roam like caribou in some protected land, uh, in some way. And, and to your point, there is evidence of those things potentially being more valued with time. And, and we know not, but that is a potential. W-when you think about-- I wanna get into our last two questions 'cause you've unpacked so much now of kind of your thought about this transition and the process of life with a lot of new ideas on the table that I really like. As you, you see us developing AI at kind of breakneck speed, when I look out, I wonder, is it... You know, I don't think anybody in this, you know, talk about game theory. I don't think there's any affordances for whether this stuff will be sentient or whether this stuff will have the kind of autopoiesis to generate and regenerate, um, uh, the thriving ecology that expands potential that you value. I don't know if we're-- like, is it gonna do that if we just go forward this way? Is it gonna do that if we just go forward this way? Like, what would you hope happened to, like, maybe hope that when we roll stuff into the world that's more capable than us, it's not just some local maxima optimizer or something that actually s-- doesn't continue the blossoming that you value and the sentience that-

**Blaise Aguera Y Arcas** [75:33]: Right

**Interviewer** [75:33]: ... you would hope to see. What, what, what, what would we do to suss out these traits and make sure that hopefully we land upon them with AI?

**Blaise Aguera Y Arcas** [75:41]: Well, I, I think that there's a, there's a misconception on the part of a lot of people who think about this kind of stuff that intelligence is optimization. Um, you know, it, it is true that we use gradient descent to train models. Um, but it's also true that, you know, the moment when we started to get, you know, real working AI was when we started to train them to reproduce their inputs. You know, not, not to, not to maximize the score of some game, um, you know, or, or, you know, paperclip maximizers or something of that sort.

**Interviewer** [76:08]: Yeah.

**Blaise Aguera Y Arcas** [76:09]: Right? It-- That wasn't, that wasn't the root. And, um, so, you know, when, when I, when I think about, uh, the fact that humanity is already, um, collectively superhuman, you know, it's the entire system, right? And, and, you know, I mentioned earlier, like, there, there wouldn't be more than a billion people without all of those machines, right? They're, you know, they're-- the machines are making us as much as we're making them in a sense. Uh, right? It's the, the autopoiesis that we're talking about is really of the entire system-

**Interviewer** [76:36]: Yes

**Blaise Aguera Y Arcas** [76:36]: ... uh, which, which includes humans. You know, uh, my, my phone doesn't heal itself when, uh, you know, its screen cracks, but, you know, its screen does get fixed. So, like, what's going on?

**Interviewer** [76:47]: [laughs] Yeah.

**Blaise Aguera Y Arcas** [76:47]: Right? And there are other machines involved in doing that. It's the whole system. So we are a part of that system. Uh, I don't see-

**Interviewer** [76:52]: Yeah

**Blaise Aguera Y Arcas** [76:53]: ... us being sidelined from that soon. And I-- and that may be a point of difference between you and me, but, you know, I, I, I see-

**Interviewer** [77:00]: Yeah

**Blaise Aguera Y Arcas** [77:00]: ... I see this, this kind of co-evolution going for quite a ways-

**Interviewer** [77:04]: Yeah

**Blaise Aguera Y Arcas** [77:04]: ... uh, before, before we're talking about, like, stuff falling off the wagon in one way or another.

**Interviewer** [77:09]: Yeah.

**Blaise Aguera Y Arcas** [77:09]: Um-

**Interviewer** [77:10]: Or, or just sort of being dissipated out of not being able to contribute in any meaningful way to the grand process, not feeding the stream in any appreciable sense. Um, but, but to your point, yeah, what you're saying is the, that contribution may last longer than, than, uh, than maybe some people suspect. Maybe, maybe even, even I suspect. Your, your idea of the phone is great. It's like the phone does get fixed. The, the network is sort of doing autopoiesis even if the individual nodes aren't actually doing it.

**Blaise Aguera Y Arcas** [77:35]: Precisely.

**Interviewer** [77:35]: Which is a cool way to think about it actually, is that the, the not living stuff changes and levels up and is maintained and increases its capability with new apps with no volition whatsoever, uh, because it's part of the system.

**Blaise Aguera Y Arcas** [77:51]: Right. Or, or, well, I mean, ano-another way of looking at it is that it-- is that the whole system is alive. Um-

**Interviewer** [77:56]: Yeah. I-

**Blaise Aguera Y Arcas** [77:56]: And we're, we are a part of it, and so are the phones and stuff. Um-

**Interviewer** [78:00]: Yeah

**Blaise Aguera Y Arcas** [78:00]: ... you know, and that's, and that's-

**Interviewer** [78:01]: The, the, the flame. The, the flame versus the torch.

**Blaise Aguera Y Arcas** [78:03]: That's the flame.

**Interviewer** [78:03]: Yep.

**Blaise Aguera Y Arcas** [78:04]: And I, I would, I would label humanity that whole, that whole thing, uh, you know, and, and, uh, you know, p-precisely because again, like we would not even have the, the numbers as homo sapiens that we do if it weren't for that, that whole system.

**Interviewer** [78:16]: A-absolutely. And again, I think it's gonna be increasingly hard to identify with individual torches as the flame starts jumping, leaping, and blazing in directions that are actually like, you know, you had mentioned, you know, eighteen seventy to nineteen twenty or whatever. Like, you know, as that gets crunched, crunched, crunched-

**Blaise Aguera Y Arcas** [78:31]: Precisely

**Interviewer** [78:31]: ... I think, I think people should really consider what you're saying there. So, you know, when you look at the process that's unraveling here and you think about all the innovators and all the regulators that are presumably pretty across the board well-intended and hoping this goes well in whatever way for our torch, for the flame itself, and you say, "Man, you know, I, I hope the innovators and regulators kinda take this to heart and consider this as sort of a guiding principle." Any sort of advice that you hope settles into that world? 'Cause that's definitely part of the audience here.

**Blaise Aguera Y Arcas** [79:01]: Yeah. Um, it's a, it's a great question. Um, I, I'm not anti-regulation, uh, in the sense that I, I think, you know, a lot of the, a lot of the operating systems that we've built that have resulted in great stuff You know, over the last hundred years that have resulted in like huge increases in, in, um, say labor safety, uh, auto safety, uh, you know, the, the aviation safety, the list could go on and on, right? Are very strong functions of regulation or, or that we don't have lead, uh, in our gasoline anymore, right?

**Interviewer** [79:30]: Yeah, thank goodness.

**Blaise Aguera Y Arcas** [79:32]: Right. So, so these are, these are, uh, this is a powerful and important tool.

**Interviewer** [79:36]: Yeah.

**Blaise Aguera Y Arcas** [79:36]: Um, but, uh, I, I guess the, the, um, the precautionary principle that I would advocate against the precautionary principle is that it is really difficult to regulate a thing that you don't yet understand. And, uh, attempts to do that often have all kinds of negative externalities and backfire in ways that, um, that were really, that were really hard for anybody to see, not just the regulators, but even the people who are doing all of the inventing. Um, there was a bunch of regulation of the internet in the nineteen nineties, for instance, that had all kinds of consequences, good, bad, and ugly, that were completely unanticipated by the, by the, the drafters of that regulation. And a lot of the real, uh, risks and downsides of the internet, uh, you know, have come from directions that were completely unanticipated by, uh, by them, right?

**Interviewer** [80:23]: Mm-hmm.

**Blaise Aguera Y Arcas** [80:23]: So it didn't, it neither protected us from the things that, that, that we might actually have needed, you know, protection from, nor-

**Interviewer** [80:29]: Mm-hmm

**Blaise Aguera Y Arcas** [80:29]: ... did we, um, uh, did it have the, the intended effects. So, you know, I, I would be more of an advocate for, um, having a, a more democratic and responsive, uh, and experimental approach to, uh, to, to regulation that, you know, that doesn't, that, that sort of takes some of the weight off and allows it to be experimented with. Uh, uh, but that is also more reactive, uh, as opposed to attempting to be, uh, proactive in, in situations that, that, you know, where, where a lot of things about, about what we're, what we're making, we actually cannot see, you know, both the po-

**Interviewer** [81:02]: Yeah

**Blaise Aguera Y Arcas** [81:02]: ... you know, the, the, the full scope of all the positives and negatives that will unfold or what would change if we were to constrain something.

**Interviewer** [81:09]: Yeah. Well, this is very in line with your dislike of revolution, and I think preemptive revolution as if we know exactly what trajectories are dangerous or good wouldn't presumably be bad.

**Blaise Aguera Y Arcas** [81:18]: Is very immodest.

**Interviewer** [81:19]: But, but sort of-

**Blaise Aguera Y Arcas** [81:19]: Yeah

**Interviewer** [81:20]: ... a-adaptive, let's see where it goes. Let's kind of be ready to leverage those tools, but in the ways that make sense as, as sort of they come about. This is, uh, very in line-

**Blaise Aguera Y Arcas** [81:29]: Exactly

**Interviewer** [81:29]: ... with your symbiosis approach and very in line with our, our shared dislike of Robespierre. Uh, so one of-

**Blaise Aguera Y Arcas** [81:34]: [laughs]

**Interviewer** [81:34]: ... one of the many, the many fun things of this interview. Blaise, I know that's all we have for time, but it has been a real blast unpacking these ideas with you. I have so much to journal about now, and I hope the audience learned a lot too. Thank you so much for being here.

**Blaise Aguera Y Arcas** [81:46]: Thank you so much, Dan. Your, your, your questions are really smart. Your, your takes on this stuff are really, are really, uh, spicy and bold and-

**Interviewer** [81:53]: [laughs]

**Blaise Aguera Y Arcas** [81:53]: ... um, uh, in the best possible way, and, and this has been a really fun conversation.

**Interviewer** [81:58]: Awesome. So that's all for this episode of The Trajectory. Thank you for tuning in all the way through to the end of this episode, and a big thank you to Blaise for being able to join us as episode fourteen in this Worthy Successor series. I think Blaise's admission of sort of being skeptical even about his own theories, uh, I think is extremely honest. What I liked most about this episode was his idea of sort of where this kinatis impetus comes from and sort of the force that pulls it together. The idea that sort of the self-interest of individual moving parts to sort of do more of what it is that they want to do, forming more complex things which create more surface area for additional complex things and for powers to emerge that are biological and cultural and technological out of that process, I thought was a, a piercingly accurate way to describe what we have seen and what we are quite likely to see going forward. Um, uh, Blaise also sort of had some notions around symbiosis. I will say between my conversations with Blaise and there's a futurist called John Smart, I'm starting to kind of tilt in the direction of thinking that actually there, there could be a, maybe a relatively extended period of symbiosis. I don't exactly see three or four generations of humans in this sort of being very useful to machines as horses were useful to humans for many centuries. I, I don't, I don't see that, uh, at all. But I also don't see a kind of blowing through humanity in an immediate sense quite as much as I think I did before sinking my teeth into how these precedents for emergent complexity sort of evolve. It does strike me that some degree of, of complexity is, is pretty likely. Um, so I, I like that. I think that's neat that sort of I can see my own ideas shifting. I'd love to know your thoughts on Blaise's ideas. Do you think there's credence to the idea of symbiosis? Does the bubbling up of potentia come forth from a different process that, uh, you, you suspect maybe he's getting something right about, something wrong about? Put it down in the comments. We've been getting more and more folks on the Worthy Successor to chip in ideas, and those have been feeding my brain for who to have on as our next guest, so I appreciate you guys for commenting. I mentioned to Blaise at the end of this episode that I, I really consider myself an advocate for his ideas. There's few people where I was like, "Wow, this is piercingly accurate, intellectually modest, and a really important way of framing these things." I loved this episode. I'm, I'm like understating my enthusiasm, but I, I hope you enjoyed it too. So thanks for tuning in all the way to the end of this one. I look forward to catching you the next time here on The Trajectory.

