---
title: "The Data, The Divide, and The Future: A Conversation with Blaise Agüera y Arcas"
person: blaise-aguera-y-arcas
section: by
type: talk-transcript
year: 2023
venue: ""
source_url: https://podcasts.apple.com/us/podcast/the-data-the-divide-and-the-future-a/id1600566734?i=1000645276345
retrieved: 2026-08-14
content: full-text
transcription:
  method: asr
  asr_model: elevenlabs-scribe_v2
  diarized: true
  speaker_labels: inferred   # ASR diarization + LLM naming (claude-sonnet-4-6); not ground truth
  duration_min: 56
notes: "PROVENANCE: machine-transcribed from AV via ElevenLabs Scribe v2 (diarized) + LLM speaker-naming pass. Speaker labels are inferred, not authoritative. Layer-2 (mildly lossy) per charter, not camera-raw."
---

# The Data, The Divide, and The Future: A Conversation with Blaise Agüera y Arcas

*Speakers (inferred):* speaker_0=Maury Fontanez, speaker_1=Blaise Aguera Y Arcas, speaker_2=Melissa Grujicse

## Transcript
**Maury Fontanez** [00:00]: We just commented on this the other day when one of my kids didn't wanna do the dishes or something.

**Blaise Aguera Y Arcas** [00:04]: [laughs]

**Maury Fontanez** [00:04]: And we were like, "At your age, you'd be married off-

**Blaise Aguera Y Arcas** [00:06]: Exactly. [laughs]

**Maury Fontanez** [00:06]: ... with children working on the farm. You could do the dishes."

**Blaise Aguera Y Arcas** [00:09]: Yeah, I've tried to, I've tried to pull that with, uh, with, with my kids as well.

**Maury Fontanez** [00:12]: [laughs] It didn't work.

**Melissa Grujicse** [00:12]: It doesn't work. Yeah.

**Maury Fontanez** [00:18]: Welcome to Signal, the podcast that raises your frequency. I'm Maury Fontanez.

**Melissa Grujicse** [00:22]: And I'm Melissa Grujicse.

**Maury Fontanez** [00:24]: Bean, this week we have an exciting conversation with a very special guest who's gonna talk to us about AI, identity, gender, sexuality, everything.

**Melissa Grujicse** [00:34]: Everything. You name it.

**Maury Fontanez** [00:35]: You ready?

**Melissa Grujicse** [00:36]: I am so ready.

**Maury Fontanez** [00:37]: Okay, let's do it. Hey, Bean, what's up?

**Melissa Grujicse** [00:46]: What's shakin'? I say that every week.

**Maury Fontanez** [00:48]: You do, but this week is a special week 'cause we have-

**Melissa Grujicse** [00:51]: It's really shakin'

**Maury Fontanez** [00:52]: ... it's really shakin'. [laughs] We have such a special guest. We are not gonna delay in getting to him. We have with us the author of the book Who Are We Now?, Blaise Aguera y Arcas, who is the CTO of Tech and Society at Google, joining us to talk about his book about AI, about gender and sexuality, and how it all intersects. Blaise, welcome to the show.

**Melissa Grujicse** [01:16]: Welcome.

**Blaise Aguera Y Arcas** [01:17]: Thank you so much for having me on.

**Maury Fontanez** [01:19]: We are very excited to talk to you, Blaise. I think that this show could be three hours long because this book is so fascinating.

**Melissa Grujicse** [01:25]: Absolutely.

**Maury Fontanez** [01:26]: So we, we'll try not to keep you here for three hours, but, um, before we get into the millions of questions we have for you, we like to play a little game to fill each other in on our week, which is cringe or delight, something embarrassing or something delightful that happened to you this week, um, just so we can catch up. So we'll let you chat with us and listen to ours, and then we'll have you go last. Does that sound good?

**Blaise Aguera Y Arcas** [01:48]: Absolutely.

**Maury Fontanez** [01:49]: All right, cool. Bean, what do you have?

**Melissa Grujicse** [01:51]: Yeah.

**Maury Fontanez** [01:51]: Cringe? Delight?

**Melissa Grujicse** [01:52]: I have a delight.

**Maury Fontanez** [01:53]: Okay.

**Melissa Grujicse** [01:53]: It's not really related to me, it's just something I experienced and I thought it was really lovely to experience it in person. My mother is currently undergoing radiation and we were at the hospital on one of the days this week, and somebody there rang the bell, which I know symbolizes the end of their final treatment and they are done with-

**Maury Fontanez** [02:12]: Aw

**Melissa Grujicse** [02:12]: ... their cancer treatment. And I've never... I've seen videos and it's, it's always lovely to watch, but s- seeing it in person, I mean, I had goosebumps head to toe. All the nurses-

**Maury Fontanez** [02:21]: Aw

**Melissa Grujicse** [02:21]: ... were out in the hallway. They rang it. Everyone was clapping. I didn't even see the human and I was still crying.

**Maury Fontanez** [02:28]: Aw.

**Melissa Grujicse** [02:28]: It just felt really powerful in the moment to experience that live.

**Maury Fontanez** [02:33]: That's really beautiful. Wow.

**Melissa Grujicse** [02:35]: [laughs] So do something weird and cringey.

**Maury Fontanez** [02:38]: I know. Now I'm embarrassed to talk [laughs] about my week.

**Melissa Grujicse** [02:41]: You're like, "My nail broke."

**Maury Fontanez** [02:42]: Yeah, literally it's that dumb.

**Melissa Grujicse** [02:44]: [laughs]

**Maury Fontanez** [02:44]: That is really beautiful. And you know what? There is something about being there in that shared space of energy-

**Melissa Grujicse** [02:51]: Yes

**Maury Fontanez** [02:51]: ... when that's happening versus hearing about it, so I can feel, like, the energy that you feel in that moment with that person there. That's really lovely.

**Melissa Grujicse** [02:57]: I even have goosebumps just, uh, discussing it again.

**Maury Fontanez** [03:01]: I love it. All right. Well, I'll get into-

**Melissa Grujicse** [03:03]: Do it

**Maury Fontanez** [03:03]: ... my cringe. [laughs]

**Melissa Grujicse** [03:04]: Yeah.

**Maury Fontanez** [03:04]: So as you know, Bean, Blaise, you don't know this 'cause we just met, I have started working out early in the mornings. I do not wake up early, but my neighbors and good friends pick me up on their way and they take me, and the workout class is on the beach-

**Melissa Grujicse** [03:16]: They force you

**Maury Fontanez** [03:16]: ... so what's to hate about it?

**Melissa Grujicse** [03:17]: Right.

**Maury Fontanez** [03:17]: Yeah. So anyway, it's this, like, weight class, weightlifting with kettle bells, and I am this noob among these women who have been doing it. So all of the exercises she teaches, she keeps having to stop and be like, "But Maury, you do this with the two pound weight. But Maury, you do this with no weight."

**Melissa Grujicse** [03:36]: [laughs]

**Maury Fontanez** [03:36]: And last week, or was it Wednesday, they were doing a bunch of, like, really hard stuff and I was just laying there with no weights trying to even figure out how...

**Melissa Grujicse** [03:45]: Okay.

**Maury Fontanez** [03:45]: Like, some of these exercises my brain can't understand the movements of. [laughs]

**Melissa Grujicse** [03:50]: That's how I feel like is going to happen today when we just chat with Blaise and his-

**Maury Fontanez** [03:54]: Yeah. [laughs]

**Melissa Grujicse** [03:55]: ... utmost intelligence. I feel like my body and brain are just not going to compute properly.

**Maury Fontanez** [04:00]: [laughs] Yeah.

**Melissa Grujicse** [04:00]: This is the most intimidated I have been on our podcast yet, Blaise-

**Blaise Aguera Y Arcas** [04:04]: Oh, no. Oh, no. [laughs]

**Melissa Grujicse** [04:04]: ... I'd like you to know.

**Maury Fontanez** [04:06]: That's true.

**Melissa Grujicse** [04:07]: The book is so amazing. It's, it-

**Maury Fontanez** [04:08]: Yeah

**Melissa Grujicse** [04:08]: ... I was like, what will I share? He already knows everything.

**Blaise Aguera Y Arcas** [04:12]: It's so far, so far from-

**Maury Fontanez** [04:13]: It's true.

**Melissa Grujicse** [04:13]: I will attest to that.

**Blaise Aguera Y Arcas** [04:14]: [laughs] That's, that's incredibly, incredibly kind of you two to say.

**Melissa Grujicse** [04:18]: [laughs] It's the truth.

**Maury Fontanez** [04:20]: Well, before we get into it, Blaise-

**Melissa Grujicse** [04:22]: Yes

**Maury Fontanez** [04:22]: ... tell us about your week. Anything delightful or embarrassing that happened to you?

**Blaise Aguera Y Arcas** [04:26]: Well, I, I guess it's a, I mean, it's a little Pollyanna, but the first thing that comes to mind is that our younger kiddo got into, uh, their first, uh, college.

**Melissa Grujicse** [04:35]: [gasps]

**Maury Fontanez** [04:36]: Oh, congratulations. [claps]

**Blaise Aguera Y Arcas** [04:38]: Yeah.

**Melissa Grujicse** [04:38]: That's not Pollyanna. That's exciting.

**Blaise Aguera Y Arcas** [04:40]: Yeah, it was, it, it, it felt like kind of a big deal.

**Melissa Grujicse** [04:42]: Absolutely.

**Blaise Aguera Y Arcas** [04:43]: So that, that, that was mine.

**Melissa Grujicse** [04:44]: That's great.

**Maury Fontanez** [04:44]: That's lovely. Are they applying to multiples, and do they have a dream school that they're hoping for?

**Blaise Aguera Y Arcas** [04:51]: Yeah, I mean, ev- everybody, everybody-

**Maury Fontanez** [04:52]: Yeah

**Blaise Aguera Y Arcas** [04:53]: ... you know, nowadays seems to apply to hundreds.

**Maury Fontanez** [04:55]: Yeah. Yeah.

**Blaise Aguera Y Arcas** [04:55]: So, uh, yeah, there are, there are a lot. But, you know, this, this kid is, [laughs] is looking for a place that, that teaches, you know, Sumerian and Hittite and Acadian and whatnot, and he was very into this-

**Maury Fontanez** [05:06]: Wow

**Blaise Aguera Y Arcas** [05:06]: ... you know, kind of very esoteric stuff. And so there are a handful of places-

**Maury Fontanez** [05:10]: Wow

**Blaise Aguera Y Arcas** [05:10]: ... that, uh, that, that do that, and they got into, into one of the places-

**Melissa Grujicse** [05:13]: [gasps]

**Blaise Aguera Y Arcas** [05:13]: ... with a really, really, really good program along those lines, so.

**Melissa Grujicse** [05:15]: Wow.

**Maury Fontanez** [05:16]: Oh my God. I mean, no surprise, but your-

**Melissa Grujicse** [05:19]: Again

**Maury Fontanez** [05:19]: ... kid also sounds fascinating. [laughs]

**Melissa Grujicse** [05:21]: Exactly. Exactly. That's exactly what I was thinking.

**Maury Fontanez** [05:22]: I do have to say, the joke on this podcast is that I'm such a history nerd, but Sumerian history is so fascinating to me.

**Blaise Aguera Y Arcas** [05:29]: It's pretty out to lunch, isn't it?

**Maury Fontanez** [05:30]: It is.

**Melissa Grujicse** [05:30]: [laughs]

**Maury Fontanez** [05:30]: And I love the fact that they're gonna, they wanna focus on it.

**Blaise Aguera Y Arcas** [05:34]: Yeah, me too.

**Melissa Grujicse** [05:34]: Yeah.

**Maury Fontanez** [05:35]: Yeah. All right. Well, Blaise, without further ado, let's talk about this incredible book. So as I said up top, you've written this book, Who Are We Now?, and it is this incredible book about the intersection of AI, of identity, of gender, of sexuality. I would love to start talking, um, and hearing from you about why this book, why this intersection. Uh, it's, you know, you, you talk about in this book how this is a result of around four years of survey research that you did with people around identity. How did you get to this space of, of gender and sexuality, and why is this book so important to you right now?

**Blaise Aguera Y Arcas** [06:14]: Yeah, it's a great, it's a great first question to ask.

**Maury Fontanez** [06:16]: Yeah.

**Blaise Aguera Y Arcas** [06:16]: And, and not an easy one because it's a project-

**Maury Fontanez** [06:18]: Yeah

**Blaise Aguera Y Arcas** [06:19]: ... that, you know, I, I kind of fell into it for various reasons. Um, and my reasons for doing it evolved, uh, as it went along. So, um-

**Maury Fontanez** [06:27]: Mm-hmm

**Blaise Aguera Y Arcas** [06:27]: ... yeah, and it's been about a s- you know, at least a six-year project. I began in 2016. So, um-

**Maury Fontanez** [06:32]: Wow

**Blaise Aguera Y Arcas** [06:33]: ... I, I guess if I really zoom out- The reason that I ended up spending so much time doing this project is because I feel like we're in the middle of a really big transition as a species and as a planet. From a planetary point of view, you know, we're at this moment when human activities are, um, having an effect on, on the planet at planetary scale. Uh, you know, people sometimes call that the Anthropocene. It's like a, you know, an actual geological epoch in which suddenly human activity is sort of the dominant factor in, in, in the planet's fate. And, um-

**Maury Fontanez** [07:05]: Sadly

**Blaise Aguera Y Arcas** [07:05]: ... well, s- sadly and dot dot dot. I mean, I think it's complicated, [laughs] you know?

**Maury Fontanez** [07:11]: Absolutely.

**Blaise Aguera Y Arcas** [07:12]: You know? I'm, I'm as worried about, about, about climate collapse as anybody, but, but I think it's, I think it's more than just a story of, you know, I don't know, of, of the human rape of nature or something. We're, we're part of nature. And, and that's also-

**Maury Fontanez** [07:26]: Mm-hmm

**Blaise Aguera Y Arcas** [07:26]: ... that's also part of the book's story, the sense that symbiosis is kind of the driving force that, that has led all of the big changes in, in, in life on Earth. That is to say, you know, living things, uh, working together to create, uh, something greater than, than themselves.

**Maury Fontanez** [07:42]: Mm.

**Blaise Aguera Y Arcas** [07:43]: And, uh, and that also feels like something that is happening right now in the context of AI. So, um, you know, AI is also a, a big, you know, I believe a big evolutionary transition for us. And, um-

**Maury Fontanez** [07:54]: Absolutely

**Blaise Aguera Y Arcas** [07:55]: ... and, and I guess, and I guess finally, uh, you know, to, and to connect it a little bit more with the, with the gender and sexuality piece, you know, there, there's also, uh, been a 10,000-year trend of humans basically pushing up against the limits of reproduction, like every other species on Earth trying to just grow, uh, as fast as possible and being held in check by Darwinian forces, you know, by, by disease and, and starvation. And as we've developed all of these technologies and, and lifted those constraints, our numbers, you know, really exploded.

**Maury Fontanez** [08:24]: Right.

**Blaise Aguera Y Arcas** [08:25]: But now in this century, we're poised to, you know, for our numbers to actually start going down, uh, for the first time due to choice rather than due to constraint. Uh, and that also feels like part of that same big transition. So that's the way in which I feel like, you know, the, the planetary transitions and the gender and sexuality transitions are actually connected.

**Maury Fontanez** [08:45]: Wow.

**Blaise Aguera Y Arcas** [08:46]: Interesting.

**Maury Fontanez** [08:46]: Fascinating connections. And you know what I would love to do is try to take our listeners through this beautiful arc you do in the book of discussing identity. Uh, and you talk about in this book how, you know, human identity and the othering that is accompanying our attempts to distinguish us versus them is really prevalent right now, particularly in our politics.

**Blaise Aguera Y Arcas** [09:07]: Yeah.

**Maury Fontanez** [09:08]: Um, but you really do a fabulous job of narrowing that down historically and even to our own systems as human beings. And I was really particularly struck by your discussion of American family systems and how they're based on, you know, a nuclear family, right? And what I thought was so interesting as someone who works with people on speaking their truth and living their truth and being individuals is you talk about how this nuclear system really comes at a cross current to individualism. Can you just say a little bit more about that for our listeners? Can you fill them in about that kind of intersection?

**Blaise Aguera Y Arcas** [09:46]: Sure. Well, uh, nuclear families, I mean, everybody kind of assumes that they're, they're sort of a default. They're the way things work. Uh, you know, I, I, I talk a little bit in the book about, like, the old Hanna-Barbera cartoons, The Flintstones, The Jetsons.

**Maury Fontanez** [09:59]: Mm-hmm. I loved that.

**Blaise Aguera Y Arcas** [10:00]: Uh, you know, it, it was funny because, like, I mean, I certainly grew up with that. I grew up with them in, in, in, um... I, I saw them dubbed into Spanish in, in, in Mexico and stuff. And-

**Maury Fontanez** [10:08]: [laughs]

**Blaise Aguera Y Arcas** [10:08]: ... and, um, the, the kind of joke or the premise of that was like, yeah, technology changes, you know, Stone Age, Space Age, but, you know, the family is the, is the invariant thing. Like, that's just always been, it's always been the same.

**Maury Fontanez** [10:21]: Right.

**Blaise Aguera Y Arcas** [10:21]: Uh, and-

**Maury Fontanez** [10:21]: Right

**Blaise Aguera Y Arcas** [10:21]: ... and nothing could be further from the truth. You know, the, um... I mean, and this was a bit of a surprise for me also doing the research for this book. A lot of our ideas about nuclear families are actually pretty new. Uh, you know, many of them a- a- arise in the Victorian period. And, uh, and the story of how they a- how they arose is, you know, is complicated. It, it has partly to do with Christianity and with property laws and inheritance-

**Maury Fontanez** [10:44]: Right

**Blaise Aguera Y Arcas** [10:44]: ... and with the, and with the, the decline of clan structures, which were much more, uh, sort of collectivist. Uh, and, and, and it's had a lot of consequences, uh, you know, some of which, some of which have been really important in the history of urbanization and technology and so on. But, uh, but all of that feels like it's changing now.

**Maury Fontanez** [10:59]: Right.

**Blaise Aguera Y Arcas** [11:00]: Right? I mean, there, there have been a lot of articles in the news about, like, the falling apart of the nuclear family and all these new relationship models that are springing up. The fact that so many fewer people in the city especially are, uh, are getting married and aren't having kids. So-

**Maury Fontanez** [11:13]: Right

**Blaise Aguera Y Arcas** [11:13]: ... you know, so talking about the nuclear family as sort of something bounded in time that both, you know, came at a certain moment we still assume is normal but that is now possibly, you know, on the decline, yeah, is, is one of the themes.

**Maury Fontanez** [11:24]: Yeah, absolutely. And I thought it was so interesting how you laid that across also the line of generational, you know, changes, what's happening with Gen Z versus older generations, and also urban and rural. In the sur- can you talk a little bit actually about the surveys you did over those four years and how they, uh, enlightened you around where we're moving around identity?

**Blaise Aguera Y Arcas** [11:48]: Yeah, of course. It's, as you say, four years or I, actually about six years of surveys, but there were four years when I ran-

**Maury Fontanez** [11:54]: Mm-hmm

**Blaise Aguera Y Arcas** [11:54]: ... kind of the same one repeatedly so that I could, you know, look at changes over time, uh, as, as well as within a cohort. And there... The book is basically divided into three parts. Uh, and, uh, and, and the reason was that I wanted to have sort of like a practice run in, in talking about what identity is all about and how it works. And the practice run, I... w- was about handedness, uh, just left-handedness-

**Maury Fontanez** [12:16]: Mm-hmm

**Blaise Aguera Y Arcas** [12:16]: ... right-handedness. I never-

**Maury Fontanez** [12:18]: So interesting

**Blaise Aguera Y Arcas** [12:18]: ... it was, it was, it was interesting to me too.

**Maury Fontanez** [12:20]: It's fascinating, yeah.

**Blaise Aguera Y Arcas** [12:21]: I wasn't expecting it to be interesting. So I, I never, I never thought that, that I'd, you know, actually, uh, publish that part. But there were so many surprises in it that I thought, "You know, this, this is worth, this is worth putting in the book too," uh, you know, both to introduce the methods and to start talking about how identity works in a way that's a little bit less fraught. You know, than gender and sexuality, which is obviously a huge-

**Maury Fontanez** [12:43]: Mm-hmm

**Blaise Aguera Y Arcas** [12:43]: ... hot-button topic.

**Maury Fontanez** [12:44]: Right.

**Melissa Grujicse** [12:44]: I found that would be really relatable, I thought, too, the left-handedness. It's, it's way less-

**Blaise Aguera Y Arcas** [12:49]: Yeah

**Melissa Grujicse** [12:49]: ... abstract, I think, to people. It's very... It's m- a little more concrete to understand.

**Blaise Aguera Y Arcas** [12:54]: Totally. And, and everybody understands that with handedness, you know, there are behaviors like, you know, which hand you use with your-

**Maury Fontanez** [12:59]: Totally

**Blaise Aguera Y Arcas** [12:59]: ... scissors, uh, or that you write with. There's an identity. You know, do you say, "I'm a left-handed person. I'm a right-handed person"? A- and there's, there's some biology involved, right? There, there's something about brain lateralization that's involved there, too. So it's kind of uncontroversial that way and, and it lets, you know, it lets one have a conversation about the relationships between those kinds of variables, uh, without too much anxiety about misstepping.

**Maury Fontanez** [13:21]: Yeah. Beautiful. So you started with that.

**Blaise Aguera Y Arcas** [13:25]: Right.

**Maury Fontanez** [13:25]: And then tell us how the surveys evolved over time and, you know, you're collecting this information. Are you thinking about a hypothesis? Are you thinking about an end game here? What are... What's happening as you're collecting the data, and, and what's starting to come out around how we're looking at identity right now in our culture?

**Blaise Aguera Y Arcas** [13:43]: Yeah. A great question. I, I didn't begin with a strong hypothesis. A lot of this was, was curiosity driven. You know, I'm, I'm kind of a data scientist, I guess, at heart, and, and I didn't begin with, with any really strongly held ideas about what I would find. I just realized there was a lot that I didn't know, and I began to analyze the data in order to discover more about how those-

**Maury Fontanez** [14:04]: Mm-hmm

**Blaise Aguera Y Arcas** [14:04]: ... variables relate of, of, of, uh, identity and biology and so on. So the questions always, always included how old are you, and they also always included zip code. And this-

**Maury Fontanez** [14:16]: Hmm

**Blaise Aguera Y Arcas** [14:16]: ... was pretty interesting because, you know, there, there are a lot of graphs in the book as, as you've, as you've seen.

**Maury Fontanez** [14:21]: Yes. [laughs]

**Blaise Aguera Y Arcas** [14:22]: [laughs] Like, um, you know, m- well over 100, which is unusual for, you know, for, um, for a book, and why I had some trouble finding a publisher, actually. Um-

**Maury Fontanez** [14:29]: [laughs]

**Melissa Grujicse** [14:30]: Are you a numbers guy, though? I'd imagine you're a numbers guy. You're a data guy, right?

**Blaise Aguera Y Arcas** [14:34]: Yeah, I am. I am. I mean-

**Melissa Grujicse** [14:35]: So you needed some graphs. I don't blame you.

**Maury Fontanez** [14:38]: I actually found... I found... And I'm not a math person. Like, I... Math intimidated me my whole life, but I found your graphs so helpful to the context of what I was reading because it did really do a good job clarifying exactly what you were describing in the data. So I think the, the graphs in this book are very complementary to the story you're telling because you're... It's a narrative book-

**Blaise Aguera Y Arcas** [15:03]: Yeah

**Maury Fontanez** [15:03]: ... which is fascinating because it's a, it's also about data. But I, I thought that they really helped bring them home. But anyway, we cut you off.

**Blaise Aguera Y Arcas** [15:09]: No, I'm so glad.

**Maury Fontanez** [15:09]: Continue. Sorry. [laughs]

**Blaise Aguera Y Arcas** [15:10]: I'm so glad to hear you say that because, uh, you know-

**Maury Fontanez** [15:12]: Yeah

**Blaise Aguera Y Arcas** [15:12]: ... I, I am also a stories person personally. I, you know, I like-

**Maury Fontanez** [15:15]: Yes. Yes

**Blaise Aguera Y Arcas** [15:15]: ... both narrative-

**Maury Fontanez** [15:16]: Clearly

**Blaise Aguera Y Arcas** [15:16]: ... and data. And z- um, and the point of putting in the data for me was not to make it a nerdy book, but to kind of show rather than tell a bunch of the, you know, especially more, more controversial or more interesting points in the book to, to just, you know, show why it is that-

**Maury Fontanez** [15:31]: Right

**Blaise Aguera Y Arcas** [15:31]: ... that, you know, that, that I'm drawing some of the conclusions that I, that I am and, and to allow the reader to draw their own conclusions, too.

**Maury Fontanez** [15:37]: Yes. Right. And I think that you talk a lot about how obviously our identity politics are dividing us. So I-

**Blaise Aguera Y Arcas** [15:42]: Yeah

**Maury Fontanez** [15:42]: ... do think that when you just go to the data, you know, what is there to argue but these are the responses, and here's how they're plotted.

**Blaise Aguera Y Arcas** [15:49]: Exactly. Exactly. We can alway-

**Maury Fontanez** [15:50]: Yeah

**Blaise Aguera Y Arcas** [15:50]: ... we can always discuss interpretations and d- you know, sometimes there are different interpretations, but the data are the data, and it's good, it's good to try and ground ourselves in that as well as we can.

**Maury Fontanez** [15:58]: Yeah. Let's talk about some of the results, particularly as it comes to gender and sexuality and identity. You found some really interesting things about what is happening with younger respondents versus older respondents. Can you give us a sense of, you know, what are you seeing are the trends? What, what did the data show you around gender and sexuality is happening as we are going forward into the future?

**Blaise Aguera Y Arcas** [16:24]: Yeah. So the, the reason, the reason I brought up the, I brought up the graphs is because, uh, the majority of them plot responses either as a function of age or as a function of population density.

**Maury Fontanez** [16:35]: Right.

**Blaise Aguera Y Arcas** [16:35]: And, you know, the population density you can compute from the zip code because the Census Bureau has, like, the area of every zip code as well as how many people live in it, so you divide the one by the other, you get density. And-

**Maury Fontanez** [16:45]: Yeah

**Blaise Aguera Y Arcas** [16:45]: ... and the reason for that is that, is that those patterns, changes by age and changes by density, were overwhelmingly the... You know, seemed like the most important patterns in the data. And, and what they show is that, you know, first of all, uh, younger people have a lot more identification with, uh, with minority identities of all kinds than older people do.

**Maury Fontanez** [17:06]: Mm.

**Blaise Aguera Y Arcas** [17:06]: More queer people, more bi people, more non-monogamous people, and so on and so forth. So, you know, uh, kind of no matter what identity you can think of, w- with actually one interesting exception, which is intersexuality. But pretty much everything else, you know, it's really high among the young and declines a lot, uh, among the older population. Uh, so something is definitely changing.

**Maury Fontanez** [17:27]: Do you have a theory as to what is changing?

**Blaise Aguera Y Arcas** [17:29]: Yeah, I, I, I do, and the simplest way to talk about it is that, is that identity goes along with culture, and the more community people find, which historically has been driven by move- the movement into cities, the more they find communities of affinity or communities of interest. And, and that also explains why you see the same pattern in density. So when you look at-

**Maury Fontanez** [17:51]: Mm

**Blaise Aguera Y Arcas** [17:51]: ... at people in cities, they also are much more associated with, uh, you know, with, with identity. It's almost like, you know, being young and being in a city go together. Even if you're older and you're in the city, you're more like a younger person in that sense. You're... There are, there are more identities. Uh, there are more minorities. And the, and the more you look in, in the countryside, actually the older people get, but also the more homogenous they get, and, and the, and the less identity plays a role in things. And what I mean by the less-

**Maury Fontanez** [18:16]: Mm

**Blaise Aguera Y Arcas** [18:16]: ... identity plays a role in things is, like, take bisexuality as an example. If you're in the countryside and you say, "I'm bisexual," then the likelihood is that that describes what you're doing. Uh, in other words, I am right now actually, you know, having relationships with, with people of both sexes. Whereas in the city, people will identify as bisexual even if they are, say, you know, married to somebody of the opposite sex and have been for a long time and are not acting on it. So the, the identity aspect of things becomes more important-

**Maury Fontanez** [18:43]: Interesting

**Blaise Aguera Y Arcas** [18:43]: ... than the behavioral one the more you are in a community of, uh, of other like-minded people.

**Maury Fontanez** [18:49]: Oh. So now that has me thinking. So let's talk about- ... this us versus them.

**Blaise Aguera Y Arcas** [18:55]: Yeah.

**Maury Fontanez** [18:56]: So when you plot that against the us versus them that's going on ... And actually, could you do our listeners a favor and define, like you do in the book, what, what us versus them means-

**Blaise Aguera Y Arcas** [19:06]: Sure

**Maury Fontanez** [19:07]: ... right now, you think, in our country?

**Blaise Aguera Y Arcas** [19:08]: Oh, well, it's, it's, I mean, polarization, which is the, you know, the story of what's happening in our, in our politics, uh, you know, of course, and, and, and also what's happening with the culture wars, the, the way, the way everybody is kind of setting up political battle lines based on identity. You know, it, I think that if we go back a few decades, uh, in American history, you know, people used to have a variety of different opinions about, you know, about various policies or, uh, you know, or various beliefs. But it wasn't quite so lined up, you know, where you had to-

**Maury Fontanez** [19:38]: Mm-hmm

**Blaise Aguera Y Arcas** [19:38]: ... sort of have the party line on everything depending on how you identified.

**Maury Fontanez** [19:42]: Right.

**Blaise Aguera Y Arcas** [19:42]: And, and, and that, that sort of, uh, privileging of identity over, over any specific issues or over the, you know, the ability to sort of think things through strikes me as a, as a pretty dangerous trend. And, and, and the more you other, uh, you know, some group of people who, you know, you've decided are not ... you know, don't believe the right things, you know, are, are other, the more you dehumanize them. Uh, and, and I, I see that-

**Maury Fontanez** [20:04]: Mm-hmm

**Blaise Aguera Y Arcas** [20:04]: ... you know, personally, I see that happening on both, uh, the right and on the left. Uh, and, and it's worrisome.

**Maury Fontanez** [20:09]: Right. Absolutely.

**Melissa Grujicse** [20:10]: It's making this 2024 election feel-

**Blaise Aguera Y Arcas** [20:12]: Yeah

**Melissa Grujicse** [20:12]: ... very o- overwhelming-

**Blaise Aguera Y Arcas** [20:14]: Agreed

**Melissa Grujicse** [20:14]: ... for sure.

**Blaise Aguera Y Arcas** [20:15]: Agreed.

**Maury Fontanez** [20:16]: When we think about gender and sexuality then in rural areas, there's this map in here that I thought was really cool that has an overlay that shows you, you know, Democrat versus Republican voting areas and, you know, you're obviously seeing those blue clusters in the urban areas and then, you know, jarringly the majority of the coun- country is red because of, you know, the middle part. What happens to identity if you identify as LGBTQ+ in those rural areas? What are you seeing? Are we trending towards something else? Is, is that going to change that political map in any way? How are you seeing rural areas change as more and more younger people are identifying as LGBTQ+?

**Blaise Aguera Y Arcas** [21:04]: Yeah. Oh, it's a, it's a, it's a great question and in a way the most important question in the book I think because-

**Maury Fontanez** [21:09]: Mm-hmm

**Blaise Aguera Y Arcas** [21:09]: ... you know, the, the big mega trend of the last 10,000 years is people concentrating into cities and, and the countryside emptying out. But it doesn't empty out in a uniform way. If you are gay and you grow up in the countryside, you're almost certainly gonna move to the city because that's where-

**Maury Fontanez** [21:24]: Mm-hmm

**Blaise Aguera Y Arcas** [21:24]: ... that's where you will find your people. And, uh, and, and the problem is that then that results in an increasingly homogenous countryside. So not only is the countryside becoming more sparsely populated-

**Maury Fontanez** [21:35]: Right

**Blaise Aguera Y Arcas** [21:35]: ... but it's also becoming a lot more uniform. And when, when you look at, at things like, you know, voting patterns, you know, do you, do you plan to vote for Trump or, or for Biden? Actually I haven't, I haven't run the survey this year. I'm, I'm almost a little bit afraid to. But I, but I did run it for the-

**Maury Fontanez** [21:49]: [laughs]

**Blaise Aguera Y Arcas** [21:49]: ... 2016 and 2020 elections.

**Maury Fontanez** [21:51]: Completely.

**Blaise Aguera Y Arcas** [21:51]: And there is no other variable that correlates as sharply with that as density. You know, if you're in the countryside-

**Maury Fontanez** [21:57]: Wow

**Blaise Aguera Y Arcas** [21:57]: ... you're gonna vote Republican. If you're in the city you're gonna, you're gonna vote Democrat.

**Maury Fontanez** [22:00]: Wow.

**Blaise Aguera Y Arcas** [22:01]: And, and, and w- and I, you know, I asked a bunch of sort of more specific questions about beliefs like, "Do you believe homosexuality is morally wrong?" Nobody in the city believes that homosexuality is morally wrong. A lot of people in the countryside do. And yet-

**Maury Fontanez** [22:13]: Right

**Blaise Aguera Y Arcas** [22:14]: ... there are, there are v- o- you know, very few out gay people in the countryside. Um, if you ask-

**Maury Fontanez** [22:19]: Right

**Blaise Aguera Y Arcas** [22:19]: ... uh, "Are you concerned about Sharia law being imposed in the US?" Nobody in the city is concerned about Sharia law being imposed in the US. The, the percentage in the countryside is really high. It's up around like half despite the fact that there are-

**Maury Fontanez** [22:31]: Wow

**Blaise Aguera Y Arcas** [22:31]: ... there are virtually no Muslims, uh, in the countryside in the US. So you know what, what's so interesting is that the fear of the other grows in the absence of the other. And the reason that this is such a, a, is such a dangerous mix with the way politics works in, in the US is that, uh, political power is partly a function of, of land area. You know, that's, that's why we have like, uh, you know, two Senate seats per, per state. It doesn't matter how populous the state is. Or why-

**Maury Fontanez** [22:59]: Right

**Blaise Aguera Y Arcas** [22:59]: ... you know, we have these congressional districts, right? That even if they're very sparsely populated, they still, you know, they still get congressional seats. And, um, and so as the countryside empties out, you know, the very small numbers of very homogenous people left there have, have really disproportionate political power and that's why we've seen the popular vote and, uh, and the, um, you know, and the, and the official vote diverge, uh, in, in recent election cycles.

**Maury Fontanez** [23:23]: Yeah. Wow, I was gonna ask, you say in the beginning of the book that you were on a podcast in 2016 where they were sure Hilla- Hillary was gonna win and you were like, "No, the data's showing opposite." So I was afraid to ask you that question too. I'm glad you haven't looked into it.

**Blaise Aguera Y Arcas** [23:37]: Yeah.

**Maury Fontanez** [23:37]: I don't want to know the answer. [laughs]

**Melissa Grujicse** [23:39]: I kind of want ... I want to know. I need to emotionally prepare.

**Blaise Aguera Y Arcas** [23:42]: I haven't opened that, that Pandora's box myself.

**Melissa Grujicse** [23:44]: Wow. I live in the countryside, countryside and I actually live in an area where it's very split.

**Blaise Aguera Y Arcas** [23:50]: Mm.

**Melissa Grujicse** [23:51]: Which feels strangely very overwhelming.

**Blaise Aguera Y Arcas** [23:54]: I bet. Yeah, I bet.

**Maury Fontanez** [23:55]: You know, we're talking about the othering and, and in the book you talk about nationalism, racism, classism really articulate- articulately.

**Blaise Aguera Y Arcas** [24:06]: Thank you.

**Maury Fontanez** [24:06]: And you talk about how they play a part in the othering of LGBTQ+ people. Can you speak to this, to this idea of nationalism, classism, racism and how they play into othering based on sexuality?

**Blaise Aguera Y Arcas** [24:20]: Well, there are a lot of different axes for identity.

**Maury Fontanez** [24:22]: Mm-hmm.

**Blaise Aguera Y Arcas** [24:23]: You know, as, as I mentioned earlier, like people tend to line up, uh, on one side or another of, of, you know, the, the, the more, the more we polarize, um, the more everything sort of starts to, starts to pull apart.

**Maury Fontanez** [24:33]: Yeah.

**Blaise Aguera Y Arcas** [24:34]: The, the, the pattern that I have seen within the US and, and the ... my data are, are really, you know, all US data because, you know, it was easier to survey there and I, I speak-

**Maury Fontanez** [24:43]: Mm-hmm

**Blaise Aguera Y Arcas** [24:43]: ... the language well and I understand more of the, more of the cultural nuances. I didn't feel equipped to do that internationally. So you know, it'd be really interesting to repeat some of these surveys internationally too. But, but the pattern that I saw was that, um, American nationalism is much, much stronger In the countryside where the population is more homogenous.

**Maury Fontanez** [25:02]: Right.

**Blaise Aguera Y Arcas** [25:02]: Um, the cities are where immigrants come. Uh, you know, so if you-

**Maury Fontanez** [25:05]: Yeah

**Blaise Aguera Y Arcas** [25:05]: ... if you immigrate to the US you will almost certainly, uh, you know, end up in a, in a city and not in the countryside. And so, you know, diversity, just like with LGBTQ kind of stuff, right, uh, uh, diversity of languages and of cultures is also, uh, high in the cities and low in the countryside. Even, uh, even the Black population, which of course, you know, has been in the US for a lot longer than most of the white population-

**Maury Fontanez** [25:26]: Mm-hmm

**Blaise Aguera Y Arcas** [25:27]: ... you know, has, has been driven out systematically from the countryside. One, one of the real shocks for me was, was, uh, reading about how the USDA's farming policies and, you know, sort of lending policies for, uh, for rural farmers has caused-

**Maury Fontanez** [25:40]: Right

**Blaise Aguera Y Arcas** [25:40]: ... uh, like a huge, uh, majority of Black farmers in the countryside to lose their land over the last century. So it's become completely white.

**Maury Fontanez** [25:48]: Right. Wow.

**Blaise Aguera Y Arcas** [25:48]: Ironically, you know, nationalism is high in the places where, where the American population is actually not representative of [laughs] you know, of, of who Americans actually are nowadays, but maybe with some imagined past, you know, from the 1950s or 1960s.

**Maury Fontanez** [26:03]: Yeah. Yeah, I mean it's all so interrelated. Blaise, I- and tell me if this isn't correlated. I was really... I loved this connection you made and, and you talked about this book, uh, Philosophy of Marriage by Michael Ryan that was written in the 1800s as you talk about monogamy. And you say basically monogamy m- monogamy must be enforced so that capitalism and patriarchy can be preserved. Tell us about that.

**Blaise Aguera Y Arcas** [26:27]: [laughs]

**Maury Fontanez** [26:28]: And tell us about-

**Melissa Grujicse** [26:30]: A deep, deep comment.

**Maury Fontanez** [26:30]: Right? Tell us about the... I just, I underlined it 'cause I was like, yep. Truth.

**Blaise Aguera Y Arcas** [26:33]: [laughs]

**Maury Fontanez** [26:33]: You know when you feel truth from like the top of your head to your toes?

**Melissa Grujicse** [26:36]: [laughs]

**Maury Fontanez** [26:37]: [laughs] So tell us about that and tell us if that monogamy being one part that has to be enforced for capitalism and patriarchy to, to persevere, but also then identity around gender and sexuality has to fit in to this nuclear marriage model of heteronormativity, I'm assuming. So can you talk a little bit about that?

**Melissa Grujicse** [26:58]: Can I interject quickly? And only if you're comfortable speaking to this. I'm just curious what your personal situation is. Are you in a nuclear family set-up? I'm just curious how you gained all of this perspective.

**Blaise Aguera Y Arcas** [27:12]: Yeah. Uh, I mean my own situation is pretty conventional. Uh, you know, I, uh, this, I'm, I'm definitely not writing this, writing this book as, as an advocate or, uh, you know, kind of putting myself in the picture.

**Melissa Grujicse** [27:24]: Mm-hmm.

**Blaise Aguera Y Arcas** [27:24]: I'm, I'm married. We have like, we have two kids. [laughs] You know?

**Maury Fontanez** [27:28]: Yeah. [laughs]

**Blaise Aguera Y Arcas** [27:28]: It's like, you know.

**Maury Fontanez** [27:29]: You're the picturesque American family.

**Blaise Aguera Y Arcas** [27:31]: Exactly.

**Maury Fontanez** [27:31]: Yeah.

**Blaise Aguera Y Arcas** [27:31]: Totally Flintstones, Jetsons. So-

**Maury Fontanez** [27:33]: Yeah. [laughs]

**Blaise Aguera Y Arcas** [27:33]: So I'm, I'm, I'm, um, I'm not, I'm not, you know, so much, you know, writing my truth as, as I am-

**Melissa Grujicse** [27:39]: [laughs]

**Blaise Aguera Y Arcas** [27:39]: ... uh, you know, being a, uh, you know, a curious and open-minded data scientist and questioner and, and just talking about what I'm, what I'm observing, what I'm seeing, uh, without, without trying to bring my own prejudices, uh, into the picture. Um, but thanks for asking. [laughs]

**Melissa Grujicse** [27:54]: Which I think is a great perspective. I think that's a really fascinating, completely objective perspective on something that's critically important, particularly right now.

**Blaise Aguera Y Arcas** [28:03]: Well, I mean, I mean, I do, I do wanna, I do wanna also, like, be careful here. I, I don't think that there is, there is such a thing as a completely objective perspective. And-

**Melissa Grujicse** [28:10]: Of co- agreed

**Blaise Aguera Y Arcas** [28:11]: ... you know, where-

**Melissa Grujicse** [28:11]: Fully agreed

**Blaise Aguera Y Arcas** [28:11]: ... where I, where I do have opinions that I'm bringing into the picture, I, you know, I, I try and, I try and make those explicit as well. I don't, I don't wanna, you know, uh, I don't wanna be secretive about, about those. But, uh, but I also think that it's important to be able to do data analysis and write and analyze about things other than oneself.

**Melissa Grujicse** [28:29]: And I think you remain neutral, and I think the data speaks for itself as well.

**Blaise Aguera Y Arcas** [28:33]: Thank you.

**Melissa Grujicse** [28:34]: I think that comes from a neutral perspective.

**Blaise Aguera Y Arcas** [28:36]: Thank you. That was definitely the goal.

**Maury Fontanez** [28:38]: Okay. So to the question then about monogamy-

**Melissa Grujicse** [28:40]: Yes

**Maury Fontanez** [28:41]: ... and, and th- the necessity of monogamy and monogamous marriages for capitalism to... Tell us how, tell us more about that, but tell us, as I was saying, how does, how does gender identity and sexuality also play into the, the pervasive culture being that in a capitalistic society where we live in a patriarchy, those things kind of work counter to, to the success of that system.

**Blaise Aguera Y Arcas** [29:06]: Yeah.

**Maury Fontanez** [29:07]: Can you explain that?

**Blaise Aguera Y Arcas** [29:07]: I, I can try. Uh, it's, this is a-

**Maury Fontanez** [29:09]: Yeah

**Blaise Aguera Y Arcas** [29:09]: ... this is a, a, you know, a, a long and complicated story. But in, in the old days, I mean, we, we don't, we don't really know what human society was like, you know, pre, in, in prehistory. I mean, there, there is a, we have archeological evidence obviously. You know, there, there are some, uh, some historians, archeologists who argue that we used to have something more like a matriarchy. Uh, there are some, you know, perhaps in, in the, uh, you know, in the old hunter-gatherer days. Um, I, I, I think the real answer is probably that it's complicated. Uh, there were, there were a lot of different kinds of human societies if we go way back in time. And when I say way back in time, I mean, we've gotta keep in mind, like, humans have been around for hundreds of thousands of years. And-

**Maury Fontanez** [29:48]: Right

**Blaise Aguera Y Arcas** [29:48]: ... you know, all of our recorded history is basically just about the period since the dawn of agriculture, you know, the last 10,000 or so.

**Maury Fontanez** [29:55]: Right.

**Blaise Aguera Y Arcas** [29:55]: So there is just, you know, a huge blank area, uh, where I think a lot of people kind of project their own, you know, politics and their own wishes. Um-

**Maury Fontanez** [30:04]: Yes

**Blaise Aguera Y Arcas** [30:05]: ... but, but I'm, I'm, I'm kinda with, with, uh, you know, David Graeber and David Wengrow in their, in their book, The Dawn of Everything, on the idea-

**Maury Fontanez** [30:11]: Mm-hmm

**Blaise Aguera Y Arcas** [30:11]: ... that there was probably just a, a really wide variety of systems.

**Maury Fontanez** [30:14]: Mm-hmm.

**Blaise Aguera Y Arcas** [30:15]: And if we look at our, at our, our closest, um, primate relatives, which, you know, might be a useful clue, they are the chimps and the bonobos. And, you know, it's a little bit too cartoonish to say, like, the chimps are, are patri- are patriarchs and the bonobos are matriarchs, but, you know, that's not 100% wrong, right? We've kinda got-

**Maury Fontanez** [30:31]: Okay

**Blaise Aguera Y Arcas** [30:32]: ... we've got both in the mix, um, you know, in terms of our, our, our biological inheritance.

**Maury Fontanez** [30:36]: Okay.

**Blaise Aguera Y Arcas** [30:36]: But, um, with farming, um, I think what does start to become clear is that, uh, when we settle and when we farm, uh, you know, that's when, when property starts to become really important because, you know, now you, you own your farm and, and you own, uh, if you like, the, the reproduction of all of the crops on that farm-

**Maury Fontanez** [30:56]: Right

**Blaise Aguera Y Arcas** [30:56]: ... and then your livestock and so on. And there is, um, there are very strong indications that when that begins happening, men start to think about their women ... as their property as well. And-

**Maury Fontanez** [31:06]: Right

**Blaise Aguera Y Arcas** [31:06]: ... you know, frankly, in just the same way that they think about their livestock. Um, I mean, I, it-

**Maury Fontanez** [31:10]: Right

**Blaise Aguera Y Arcas** [31:10]: ... that's a brutal thing to say, but, you know, I, I think it's accurate.

**Maury Fontanez** [31:13]: It's a reality.

**Blaise Aguera Y Arcas** [31:14]: Yeah.

**Maury Fontanez** [31:14]: Yeah. I actually, Blaise, I was, um, just reading something about the word rape, and how the word rape meant theft-

**Blaise Aguera Y Arcas** [31:21]: Right

**Maury Fontanez** [31:21]: ... you know, in the 1800s even.

**Blaise Aguera Y Arcas** [31:23]: Carrying, carrying away. Yeah, yeah.

**Maury Fontanez** [31:23]: Yeah. And that then, it, so then rape means that you're t- taking something that's mine and making it impure.

**Blaise Aguera Y Arcas** [31:30]: Yes.

**Maury Fontanez** [31:30]: That's how it was applied to women.

**Blaise Aguera Y Arcas** [31:32]: Yes.

**Melissa Grujicse** [31:32]: Wow.

**Blaise Aguera Y Arcas** [31:33]: Yes.

**Maury Fontanez** [31:33]: So to the point of what you're saying.

**Blaise Aguera Y Arcas** [31:34]: Pretty-

**Maury Fontanez** [31:34]: Yeah

**Blaise Aguera Y Arcas** [31:34]: ... pretty dark, right?

**Melissa Grujicse** [31:36]: Very dark.

**Maury Fontanez** [31:36]: Yes, absolutely. So as we get, you know, into our current reality around capitalism, or how is capitalism-

**Blaise Aguera Y Arcas** [31:45]: Mm-hmm

**Maury Fontanez** [31:45]: ... affecting our identity politics today?

**Blaise Aguera Y Arcas** [31:47]: Well, one of, one of the, um, one of the consequences of the idea that, you know, that the, the man owns reproduction and, you know, the woman is the, is the means for reproducing, it, it also goes along with the fact that children are property, too. And the, the, the likely reason that we've seen birth rates plummet so much in advanced economies, uh, and, and this is, you know, really worth dwelling on, by the way. Like, the, you know, the total fertility rate, which is to say the, uh, the average number of children per woman. You know, in, in the poorest country on Earth today, which is, uh, Niger, is about seven.

**Maury Fontanez** [32:19]: Wow.

**Blaise Aguera Y Arcas** [32:20]: And that was below the, uh-

**Melissa Grujicse** [32:21]: Wow

**Blaise Aguera Y Arcas** [32:21]: ... the world average, uh, you know, in, in 1900.

**Melissa Grujicse** [32:25]: Wow.

**Blaise Aguera Y Arcas** [32:25]: So, uh, you know, when you, you look at, at number of, of, of children per woman and, and wealth, the two correlate perfectly. And, and the reason is because, um, back in the old days when agriculture was the, was the way we all made a living and, and the way we subsisted, children were valuable as workers.

**Maury Fontanez** [32:44]: Right.

**Melissa Grujicse** [32:44]: Right.

**Blaise Aguera Y Arcas** [32:44]: Like, like the point of having, of having kids was that they were gonna, they were gonna farm, they were gonna generate more wealth, and they were gonna support you in your old age.

**Melissa Grujicse** [32:51]: Mm-hmm.

**Blaise Aguera Y Arcas** [32:52]: So, um, so you know, you, you reproduced because that was economically positive.

**Maury Fontanez** [32:56]: We just commented on this the other day when one of my kids didn't wanna do the dishes or something.

**Blaise Aguera Y Arcas** [33:00]: [laughs]

**Maury Fontanez** [33:00]: And we were like, "At your age, you'd be married off-

**Blaise Aguera Y Arcas** [33:03]: Exactly. [laughs]

**Maury Fontanez** [33:03]: ... with children working on the farm. You can do the dishes." [laughs]

**Blaise Aguera Y Arcas** [33:06]: Yeah, I've tried to, I've tried to pull that with, uh, with, with my kids as well.

**Maury Fontanez** [33:08]: It didn't work.

**Melissa Grujicse** [33:09]: Doesn't work.

**Blaise Aguera Y Arcas** [33:09]: No, it doesn't work. [laughs]

**Maury Fontanez** [33:10]: Yeah. Ineffective.

**Blaise Aguera Y Arcas** [33:11]: Yeah.

**Maury Fontanez** [33:12]: [laughs]

**Blaise Aguera Y Arcas** [33:13]: But yeah, and I mean, as you know, uh, you know, and, and like we're, we're now looking at, you know, sending our second to, to college, like kids are no longer economically positive. The opposite. [laughs]

**Maury Fontanez** [33:22]: Quite the opposite.

**Blaise Aguera Y Arcas** [33:23]: It's the opposite. And, um, you know, and, and, and there are many, you know, there are many reasons that we can talk about, you know, vis-a-vis choice. Obviously, you know, women starting to have a lot more of a say in what happens with their own reproduction is important. But I think that the, the, the root, uh, change that has happened is, is that very simple one of just, you know, they were a economic good and now they're an economic cost. Uh, so from that perspective, you know, like what the point is, what is the, um, you know, when we think about what it means to, uh, amass wealth or to be productive or, or, uh, or to propagate. Like all of that starts to become more a question of ideas and of culture and of, uh, of other more abstract things versus just, you know, literally how many, how many children, how many acres of land and so on.

**Maury Fontanez** [34:10]: Right. Wow. Yeah. Fascinating. Okay. I wanna talk, I wanna ask you another question about gender, and then I wanna start talking about AI because you have a very-

**Melissa Grujicse** [34:17]: Oh my gosh

**Maury Fontanez** [34:18]: ... interesting perspective on the word we, which I wanna get to. You know, I, I work a lot with non-binary and trans people as a coach. They've become some of my closest friends. I've been so proud of the steps they're taking to speak for a deeply underrepresented and vilified group, um, of people in the face of a lot of violence in this country and in other countries. And one of the things that we talk a lot about is this idea of gender being a social construct, and I, and I see it come up in your book as well. I wanted to ask you about gender as a social construct over time. It shows in the clothes we buy for our children, blue or pink. [laughs] Talk a little bit about how... When I say gender is a social construct, can you break that down for our listeners? Because I think sometimes you hear that and you think, "What do you mean? It's biology."

**Blaise Aguera Y Arcas** [35:14]: Yeah.

**Maury Fontanez** [35:14]: Is it? And, and, and why? Why is it? Why isn't it?

**Blaise Aguera Y Arcas** [35:18]: Yeah. It's, I mean, it's a great question and, and it's one that, it's one that, um, I've always been a little bit worried about answering, you know, in, in, in public settings and podcasts and so on because it is, it is itself so polarizing. Uh, and-

**Maury Fontanez** [35:32]: Yes

**Blaise Aguera Y Arcas** [35:33]: ... and I think that, I think that, uh, insisting on a binary answer is actually part of the problem. So, you know-

**Maury Fontanez** [35:38]: Ah

**Blaise Aguera Y Arcas** [35:38]: ... in a, in a way we have polarized it into like a yes or a no. You know, if you're, if you're on the left-

**Maury Fontanez** [35:43]: Right

**Blaise Aguera Y Arcas** [35:43]: ... you're supposed to say it's a social construct. Biology is irrelevant.

**Maury Fontanez** [35:46]: Mm-hmm.

**Blaise Aguera Y Arcas** [35:47]: Uh, and if you're on the right-

**Maury Fontanez** [35:47]: Mm-hmm

**Blaise Aguera Y Arcas** [35:47]: ... you're supposed to say it's biology. It's, it's, you're, you're, uh, are you X, X or XY. There's nothing else. The rest is bullshit. And, um-

**Maury Fontanez** [35:55]: Mm-hmm

**Blaise Aguera Y Arcas** [35:55]: ... uh, and, and these two sides of course, you know, believe that the other is, you know, is, is other. Is, is awful. Um, the reality I think is, is a lot more complicated than either of those binary assertions. So on the one hand-

**Maury Fontanez** [36:08]: Mm-hmm

**Blaise Aguera Y Arcas** [36:08]: ... so many things about the way, uh, the way gender is portrayed, you know, on TV, uh, you know, or, or marketed are completely arbitrary. Uh, you know, uh, is it, is it pink or is it blue? I mean, it used to be the other way around. Like this stuff is, you know, is, is, is a total, a total construct.

**Maury Fontanez** [36:25]: Wait, what do you mean it used to be the other way around?

**Blaise Aguera Y Arcas** [36:27]: Well, pink, yeah, pink-

**Maury Fontanez** [36:28]: Did pink used to be a male color at one s-

**Blaise Aguera Y Arcas** [36:29]: Totally

**Maury Fontanez** [36:30]: ... Oh, really?

**Blaise Aguera Y Arcas** [36:30]: Yeah. Pink was the robust male color and blue was the, was the, uh-

**Melissa Grujicse** [36:34]: Oh, wow

**Blaise Aguera Y Arcas** [36:34]: ... the retiring, uh, feminine color. Totally.

**Maury Fontanez** [36:36]: I say we go back to that.

**Melissa Grujicse** [36:38]: Wow.

**Maury Fontanez** [36:38]: I love that.

**Melissa Grujicse** [36:39]: I know.

**Blaise Aguera Y Arcas** [36:40]: I say bring all the colors.

**Maury Fontanez** [36:41]: Bring ev- Right. Exactly.

**Blaise Aguera Y Arcas** [36:43]: So yeah, that, there's, it's, you know, there's, there's a lot of essentialization of gender, of gender properties-

**Maury Fontanez** [36:48]: Right

**Blaise Aguera Y Arcas** [36:48]: ... that, that is just nonsense. On the other hand, I, I, I spent a little bit of time in the center of the book talking about John Money, the psycho-endocrinologist at-

**Maury Fontanez** [36:57]: Yes

**Blaise Aguera Y Arcas** [36:57]: ... Johns Hopkins who, you know, is turns out to have been a bit of a monster.

**Maury Fontanez** [37:01]: Yes.

**Blaise Aguera Y Arcas** [37:01]: But was also like a real darling of second wave feminism. For, um, for really believing that, that gender is, is a social construct, and actually putting that to the test, um, by performing these, uh, you know, pretty horrendous medical experiments essentially. The most famous one, the, the Reimer case, was a, a case of, of two, um, twins.

**Maury Fontanez** [37:22]: This was a wild story.

**Blaise Aguera Y Arcas** [37:23]: It's a wild story.

**Maury Fontanez** [37:25]: It's, wow.

**Blaise Aguera Y Arcas** [37:25]: Twin baby boys.

**Maury Fontanez** [37:27]: Mm-hmm.

**Blaise Aguera Y Arcas** [37:27]: Uh, they're brought in to be circumcised when they're, when they're, when they're infants. The circumcision is botched. One of them ends up, uh, basically, you know, losing his penis, uh, and is brought in to, uh, to John Money's, uh, practice. And Money's like, "Don't worry, uh, you know, if, i- as long as we construct a vagina and raise, and raise him as a girl, it's all gonna be fine because gender is socially constructed." And, uh, you know, spoiler, it doesn't go well. [laughs]

**Maury Fontanez** [37:52]: I was, I was gonna say, it wasn't fine. [laughs]

**Blaise Aguera Y Arcas** [37:54]: It was not fine.

**Maury Fontanez** [37:55]: It was not all fine.

**Blaise Aguera Y Arcas** [37:56]: No. No. You know, there, there was, there's obviously stuff, you know, in, in the case of, uh, in the case of, of, of David Reimer that made him male in his, in his own self-concept, uh, that went far beyond, uh, you know, just sort of like what, what his pa- the way his parents socialized him. Uh, having said that, uh, there is a whole spectrum there of, of, of people, including a whole spectrum of flexibility. Um, you know, so one of the, one of the weirder, I guess, you know, findings from, from this period when, when a lot of, uh, sex reassignment or, uh, or gender reassignment, uh, surgeries were, were done on kids, uh, who had had their genitals mutilated, which, which is a surprising number actually. Like, sometimes-

**Maury Fontanez** [38:35]: Wow

**Blaise Aguera Y Arcas** [38:35]: ... it seems to have, quote unquote, worked. So it's not like you can say, you know, in a binary way either yes or no, uh-

**Maury Fontanez** [38:42]: Mm-hmm

**Blaise Aguera Y Arcas** [38:42]: ... you know, it's biological either. It's complicated.

**Maury Fontanez** [38:45]: I'm curious what the further right's take is on intersex children and what should be done. I don't know, did you mention that in your book, or do you have a theory on that?

**Blaise Aguera Y Arcas** [38:55]: The, the right's, the right's question meaning?

**Maury Fontanez** [38:57]: The conservatives' side on what, how intersex children should be raised.

**Blaise Aguera Y Arcas** [39:03]: Yeah. Um, honestly, I don't know. You know, one of the things about intersexuality is that because we tend to think about it as a medical condition like diabetes-

**Maury Fontanez** [39:13]: Right

**Blaise Aguera Y Arcas** [39:13]: ... right, as opposed to an identity, it's, it's, um, it's hidden. It's a hidden identity.

**Maury Fontanez** [39:17]: Mm-hmm.

**Blaise Aguera Y Arcas** [39:18]: Or if we wanna think about it as an identity at all. So you know, one of the real surprises for me in the survey data was just how common it is. Uh, and again-

**Maury Fontanez** [39:27]: That was shocking to me, yes.

**Blaise Aguera Y Arcas** [39:28]: Yeah, yeah. So a bit of a spoiler, but you know, it's likely above 2%. It may be above 3%, uh, which is an, an astonishing number.

**Maury Fontanez** [39:34]: Which is far more than I ever imagined, yes.

**Blaise Aguera Y Arcas** [39:36]: Yeah, totally. Um, and, and unlike all of the other, uh, identities that are very high among the young, the, the pattern by age is really a surprise too. It's basically zero at age 18, uh, the youngest age that I, you know, that I can, that I can have people answer the survey, and it rises up until, uh, you know, up through the, the 30s. And, and, uh, my, my guess as to why that is is that most people don't know that they're intersex until they-

**Maury Fontanez** [40:01]: Right

**Blaise Aguera Y Arcas** [40:01]: ... you know, go to the, go to the doctor.

**Maury Fontanez** [40:02]: Right.

**Blaise Aguera Y Arcas** [40:02]: Maybe it's a fertility problem, and they, and they find out. So, um-

**Maury Fontanez** [40:06]: Wow

**Blaise Aguera Y Arcas** [40:06]: ... and this is a legacy of John Money too because, you know, according to him, you should never tell your kid that they're, that they're intersex because that will interfere with their socialization as, as one gender or the other. And often the parents weren't told either. So, um, you know, it's-

**Maury Fontanez** [40:20]: Wow.

**Blaise Aguera Y Arcas** [40:20]: Yeah. [laughs]

**Maury Fontanez** [40:20]: Can you imagine?

**Blaise Aguera Y Arcas** [40:21]: It's kind of a shock.

**Maury Fontanez** [40:22]: My goodness.

**Blaise Aguera Y Arcas** [40:22]: And when people find out-

**Maury Fontanez** [40:23]: Yeah

**Blaise Aguera Y Arcas** [40:23]: ... you know, in their, in their 30s, I think, you know, the, the most common response is not to, you know, become an out intersex person or to think about it as an identity, but think about it as a, as a private medical issue that is not gonna-

**Maury Fontanez** [40:36]: Mm-hmm

**Blaise Aguera Y Arcas** [40:36]: ... that is not gonna get discussed with anybody else.

**Maury Fontanez** [40:40]: Yeah, and you say in the book intersex babies born in communities with less access to medical facilities have a very different outcome.

**Blaise Aguera Y Arcas** [40:48]: Less likely to know, uh, less likely to get treated.

**Maury Fontanez** [40:51]: Right.

**Blaise Aguera Y Arcas** [40:51]: That's right. So, so I think, I think that the sh- you know, the, the, probably the short answer to your question is I, I think that most of the, of the right, uh, probably just, um, thinks that it's extraordinarily rare, even more so than the left.

**Maury Fontanez** [41:04]: Right.

**Blaise Aguera Y Arcas** [41:04]: And so not, not relevant-

**Maury Fontanez** [41:05]: Right

**Blaise Aguera Y Arcas** [41:05]: ... to, you know, to any of these conversations.

**Maury Fontanez** [41:07]: Yeah. Yeah. Well, and so much to say about how important it is, uh, that we're having public conversations so that people can begin to identify as what is true to them rather than be in this mystery, uh, or isolation of an experience that feels like their own. I mean, would you agree that social media and the way that people can own their identity more publicly and that being democratized has changed this trajectory of identity and the way people are responding to surveys like yours?

**Blaise Aguera Y Arcas** [41:44]: For sure. As it becomes more normalized to, for example, be intersex, um, it becomes more acceptable for, for people to come out with that and think about it as an identity and, and normalize it. And I, I mean, I think that's a very positive development in the sense that the idea that, that, that, that something is, uh, you know, that is, that is a part of your body, that is an aspect of you biologically is somehow a shame or something to hide-

**Maury Fontanez** [42:08]: Mm-hmm

**Blaise Aguera Y Arcas** [42:08]: ... seems to me like a, you know, like that would be a problem for your quality of life.

**Maury Fontanez** [42:12]: Exactly.

**Blaise Aguera Y Arcas** [42:12]: So anything that reduces shame is good. Although al- also obviously people should be free to, you know, to, to keep whatever they wanna keep private private as well. Uh, I'm also a big believer-

**Maury Fontanez** [42:22]: Right

**Blaise Aguera Y Arcas** [42:22]: ... in, in privacy, so you know, it's, I, I guess it's a matter of choice.

**Maury Fontanez** [42:26]: Yeah.

**Blaise Aguera Y Arcas** [42:26]: And, and, and choice is maximized, uh, uh, also if you don't feel shame.

**Maury Fontanez** [42:31]: Absolutely. Beautifully said. All right. Well, we can't ignore what you do, which is, um, you're an expert in machine intelligence and AI, and I think it's time to bring that into the conversation here.

**Blaise Aguera Y Arcas** [42:41]: Yes.

**Maury Fontanez** [42:42]: So tell us about the correlation you make around AI and this us versus them and this we. How does AI fit into that picture?

**Blaise Aguera Y Arcas** [42:56]: Well, part of the big trend that we've been talking about of just polarization, uh, is, you know, I... This wasn't the case when I began writing the book in, in t- in, you know, in 2016, 2017, but AI has now also become highly polarizing.

**Maury Fontanez** [43:11]: Mm-hmm.

**Blaise Aguera Y Arcas** [43:12]: You know, I'm, I'm hearing, you know, on, on the one hand- AI doomers, uh, talk about, about AI as, you know, an other that needs to be, uh, stopped before it's going- before it leads to human extinction because it's an, it's an either/or, uh, kind of, kind of situation. You know, we're gonna- it's gonna do to us what we did to the gorillas or something. Um-

**Maury Fontanez** [43:31]: Right.

**Blaise Aguera Y Arcas** [43:31]: And, uh, and I'm, and I'm also hearing, uh, you know... I, I mean, I guess I would call that sort of the, the right or libertarian take generally speaking, although, you know, this is a generalization.

**Maury Fontanez** [43:41]: Right.

**Blaise Aguera Y Arcas** [43:41]: And I'm also hearing from the left a lot of talk about AI being fake. You know, it's not, it's not real. It's just a capitalist scam, just a... It's all about labor and exploitation. Uh, it's essentially a way for capital to win over labor, you know? And, and, uh-

**Maury Fontanez** [43:56]: Mm

**Blaise Aguera Y Arcas** [43:56]: ... and it's like a whole different set. And, and, and there, you know, questions of justice-

**Maury Fontanez** [43:59]: Right

**Blaise Aguera Y Arcas** [43:59]: ... you know, take, take precedence, but also there's a denial that, you know, it's sort of this is all hype. You know, it's, it's, it's just corporate hype.

**Maury Fontanez** [44:05]: Right.

**Blaise Aguera Y Arcas** [44:06]: Personally, I, I feel like both of those, um, are, are really problematic extreme positions, um, for-

**Maury Fontanez** [44:13]: Mm

**Blaise Aguera Y Arcas** [44:13]: ... for a few reasons. One of them is, you know, when I think about, about symbiosis as being the, the origin of all, uh, of all of the interesting transitions in evolution in the past. You know, everything from like mitochondria, you know, uh, being incorporated into cells to make eukaryotes to, you know, multicellular life and so on. Y- it's all about relationships that are so much more complicated than just competition-

**Maury Fontanez** [44:36]: Mm

**Blaise Aguera Y Arcas** [44:36]: ... you know, of, of A versus B.

**Maury Fontanez** [44:37]: Right.

**Blaise Aguera Y Arcas** [44:37]: Like, life becomes more complicated through things, you know, meshing together. Um, not-

**Maury Fontanez** [44:42]: Mm-hmm

**Blaise Aguera Y Arcas** [44:42]: ... not through one thing extinguishing another. Uh, you know, our- what we've done to the gorillas or the chimpanzees is, is kind of the exception. And we are highly interdependent, uh, with, with our technology. The technology can't exist without us.

**Maury Fontanez** [44:54]: Mm-hmm.

**Blaise Aguera Y Arcas** [44:54]: And, you know, increasingly we can't exist without the technology either.

**Maury Fontanez** [44:58]: Mm-hmm.

**Blaise Aguera Y Arcas** [44:59]: So as I see it, Maura, you mentioned, you know, capitalism, uh, you know, and its problems earlier. Like, we have a big capitalism problem, uh, in the sense that, you know, if, if as we develop technologies that increase our, our, our, our aggregate wealth, um, we are not figuring out ways to share those gains. Uh, that is a huge problem because, uh, you know, both from a, from a humanitarian perspective and from a polarization perspective. Because we're now, we're now creating, um, uh, you know, we're, we're really exacerbating, uh, class divides which does not go in a g- in a good direction.

**Maury Fontanez** [45:33]: Mm.

**Blaise Aguera Y Arcas** [45:33]: And, and I see that as the central problem, uh, that, that we, that we face as we start to, you know, exist in symbiosis, uh, with, with AI. But we're displacing a lot of those anxieties, uh, you know, into, you know, either believing that, you know, AI is other or that AI is just, uh, you know, it's just corporations and corporations are other, when I think we need to be having a, a kind of conversation in the middle if that makes sense.

**Maury Fontanez** [45:56]: So am I hearing you say that you believe the answer is somewhere in the middle personally with all of your knowledge? 'Cause I'm not gonna lie, I'm a liberal, but I'm a little bit of an AI doomer. Like I'm... Well, it's, it just feels like it's growing so exponentially-

**Blaise Aguera Y Arcas** [46:12]: Yeah

**Maury Fontanez** [46:12]: ... that it's going to, we're going to lose control. Um, but I certainly do not have as much, as much knowledge as you do, so it's very refreshing to hear that you believe there is a middle ground here.

**Blaise Aguera Y Arcas** [46:23]: Well, control is a complicated word. Like we, you know, we... The, the idea that, the idea that like we humans are in control, we're on top, it's a hierarchy-

**Maury Fontanez** [46:31]: Right

**Blaise Aguera Y Arcas** [46:31]: ... uh, is I think a little bit of an illusion. I mean, I, I talk, I talk a bit about, you know, for instance our relationship with our crops. You know, with wheat, with, with cows. You know, we're like, "Yeah, we're on top," you know? [laughs] But, uh, but there's another way of thinking about it which is that, you know, wheat has taken over humanity as its, uh, you know, as its great propagator, you know? [laughs] Cows have taken-

**Maury Fontanez** [46:52]: [laughs]

**Blaise Aguera Y Arcas** [46:52]: ... have taken over.

**Maury Fontanez** [46:53]: True.

**Blaise Aguera Y Arcas** [46:53]: You know, right? Like they, their, their numbers have exploded even more than human numbers have exploded. They're, you know, they're, right, they're, they're, um, you know, they're certainly using up more of the land on Earth, uh, because, because they've manipulated our tastes in some way. Um, you know, or, or a cat-

**Maury Fontanez** [47:07]: Oh.

**Blaise Aguera Y Arcas** [47:07]: Or if you have, if you have a cat at home, like they don't, they don't do fuck all, you know? And-

**Maury Fontanez** [47:12]: Right. [laughs]

**Blaise Aguera Y Arcas** [47:12]: Right. And they, and they get, they get, they get it all, you know? [laughs] Uh, you know, like who's on top? Uh, you know, the, the way I, the way I see it-

**Maury Fontanez** [47:18]: It's true

**Blaise Aguera Y Arcas** [47:18]: ... it's, it's not, not everything is slavery, right? It's not, it's not a hierarchy-

**Maury Fontanez** [47:22]: Yeah

**Blaise Aguera Y Arcas** [47:22]: ... like that. It's, it is all about symbiosis. So I guess, I guess I, I, I, I question even the premise of the question if that makes sense.

**Maury Fontanez** [47:30]: Sure. Because what, what I'm hearing you say is that technology is us.

**Blaise Aguera Y Arcas** [47:36]: Yeah.

**Maury Fontanez** [47:36]: We are behind it. We are integrated to it. We are now attached to it, so it is, as you said, a symbiotic relationship meaning that our evolution means that we are integrated with this technology.

**Blaise Aguera Y Arcas** [47:50]: Yeah.

**Maury Fontanez** [47:50]: And you say in the book, you know, what is we? We is also this technology.

**Blaise Aguera Y Arcas** [47:55]: Right.

**Maury Fontanez** [47:56]: It is a part of the we, that it shouldn't be othered the way that we do to other identities because it's separating us in a way that is not organic.

**Blaise Aguera Y Arcas** [48:04]: That is how I feel. And um, you know, and I, I'm very, I'm very, you know, aware here of also being, you know, a Google employee and, you know, like I, I mean, I wanna, I wanna be very clear that like, um, the opinions that I'm expressing in the book are not, they're not sort of like, uh, the, the corporate line.

**Maury Fontanez** [48:22]: Right. [laughs]

**Blaise Aguera Y Arcas** [48:22]: You know? [laughs] There are, there are a variety of things I'm saying that I don't, you know, I, I, I don't wanna be associated with, with, with the company. They're... It's very much my take. But, um-

**Maury Fontanez** [48:29]: Sure

**Blaise Aguera Y Arcas** [48:30]: ... but yeah, for what it's worth, my take is that it is very similar to the take of, of the performance artist Stelarc, uh, the Australian performance artist who has said, you know, we, um, technology constructs our humanity just as much as we construct technology.

**Maury Fontanez** [48:44]: Right.

**Blaise Aguera Y Arcas** [48:44]: You know, when, when we, when we think about why we have such a short gut, uh, you know, and, and, uh, and have such a hard time digesting raw foods, it's because we invented fire and fire has become a part of us. It's like our external digestive system.

**Maury Fontanez** [48:57]: Right. Wow.

**Blaise Aguera Y Arcas** [48:57]: You know? And I, and I think AI is part of that same tradition if you like.

**Maury Fontanez** [49:02]: Beautiful. Well, yeah. Yeah. Okay, well, Blaze, we have kept you for so long. I have two last questions for you. I seriously could talk to you for three more hours. I mean, truly-

**Blaise Aguera Y Arcas** [49:12]: I'm fascinated.

**Maury Fontanez** [49:12]: Yes.

**Blaise Aguera Y Arcas** [49:13]: I am so fascinated.

**Maury Fontanez** [49:14]: As you can see by my lack, my lack of speech. Jaw open, no words.

**Blaise Aguera Y Arcas** [49:19]: That is, that is so, that is so flattering, you two. Thank you so much.

**Maury Fontanez** [49:23]: But really, I mean, an incredible body of work that is, um, both data and, as I said, uh, his- it's about our history as a species and about humanity. So to that point, two-part question: what is your biggest warning for us as humanity?

**Melissa Grujicse** [49:39]: Oh.

**Maury Fontanez** [49:39]: And what is your greatest hope, given what you see from your vantage point?

**Blaise Aguera Y Arcas** [49:43]: Yeah. Uh, I guess they're one and the same. So, um, my, my biggest warning is that, you know, we're in the throes now of becoming a planet, a planet-sized organism, if you like, a planet-sized being. And that's really important, um, because, you know, it's only by becoming a planet-sized being that we are able to achieve homeostasis, uh, you know, achieve stability, um, sustainability. And, um, you know, we, we kind of are in a situation where we can only go forward or back. It's almost like we're in the birth canal. Like, there's no going sideways.

**Melissa Grujicse** [50:20]: Mm-hmm.

**Blaise Aguera Y Arcas** [50:20]: It's either forward or back. Uh, back would mean, uh, return to being, uh, you know, a specie- you know, a humans being a species like any other species on Earth, um, that, uh, that is subject once again to, um, to those Darwinian pressures where, you know, most, most children are, are, are die, die during, uh, childbirth or in their first five years. And, you know, and, and we're basically in the mix, right? Along with, along with every other, every other animal that is, you know, that is sort of struggling to get along. Um, I mean, the likelihood of us going back to that state seems very low to me. But-

**Melissa Grujicse** [50:54]: Okay

**Blaise Aguera Y Arcas** [50:55]: ... you know, that would be one route, I guess. Um, the other route is forward, where, where we all learn there's a big we, a big we that includes technology and that includes, uh, the other species on Earth, and that includes the Earth as a system that learns how to regulate itself, whether that's, uh, economically, environmentally, politically. You know, and, and, um, for that to happen, we have to pull together. Uh, you know, the... when, when we are othering, uh, each other, when we're, when we're in this kind of, uh, of, of polarized us versus them conflict that I feel like we increasingly are in, we are not realizing that all of our interests have to be aligned-

**Melissa Grujicse** [51:35]: Mm-hmm

**Blaise Aguera Y Arcas** [51:35]: ... for, in order for that, that, um, that larger thing to happen. I, I use the example of, of, um, unions and, uh, the coal industry, for instance.

**Melissa Grujicse** [51:44]: Mm.

**Blaise Aguera Y Arcas** [51:44]: You know, I, I grew up, like, uh, with, you know, listening to Pete Seeger and, like, you know, very, very pro-union, and I still am. But if the coal union is, uh, you know, is trying to say like, you know, we need to preserve, uh, you know, coal workers' jobs, and, and coal is actually not a part of, of our, of our future, uh, those two things are, are, are directly in conflict. Uh, and they're only in conflict because we haven't accepted that all of the workers in the coal union are a part of that big us who have to be taken care of. If we were to address those, those underlying problems of othering, then we kind of solve everything in one go. Now, I know that's a very optimistic, [laughs] you know, that's a very optimistic wish. We're never gonna be free of struggle. We're never gonna be free of, of political misalignment, et cetera. But I feel like it's, it's becoming extreme, uh, now in a way that, that really, uh, risks destabilizing our planetary future.

**Maury Fontanez** [52:37]: Mm. Wow. What I think... I mean, we can't end on a better statement there. I couldn't agree with you more. You know, our level of seeing ourselves as separate from one another is such a toxic illusion that we live under, and I'm so grateful for this work you've done and how, um, diligent you've been about making this case in a way that people can't argue with because there's data. So, Who Are We Now?

**Melissa Grujicse** [53:04]: Absolutely.

**Maury Fontanez** [53:04]: Go pick it up. Go order it. It is fascinating. Blaise, where can people find you if they want to learn more about you and your work?

**Blaise Aguera Y Arcas** [53:10]: Thank you for asking. So, so yeah, the, uh, Who Are We Now? you know, is available from Hat & Beard Press, uh, or from Amazon or at your local bookstore. Uh, it's also available for free online, uh, at whoarewenow.net.

**Melissa Grujicse** [53:23]: Which is extra awesome.

**Maury Fontanez** [53:24]: Wow.

**Blaise Aguera Y Arcas** [53:25]: Yeah, the-

**Melissa Grujicse** [53:26]: You don't hear that very often.

**Blaise Aguera Y Arcas** [53:27]: No.

**Melissa Grujicse** [53:27]: My cousin sent me a really cool interactive, um, guide that you have-

**Blaise Aguera Y Arcas** [53:32]: Yes

**Melissa Grujicse** [53:32]: ... that I think makes everything really tangible.

**Blaise Aguera Y Arcas** [53:35]: The, the, uh, the idea behind put- I mean, of course, we wanted to make sure that it was online so that there w- wasn't any barrier to access. Uh, but also the data are, are all there and, you know, we, we did, we did a bunch of work to make it beautiful and interactive, so it's not just a PDF. It's like a, it's a real, uh, it's, it's a real, you know, work in its own right.

**Melissa Grujicse** [53:52]: I think even that is so aligned with your message of us versus them and everybody having access, and I think that's really beautiful.

**Blaise Aguera Y Arcas** [53:58]: Thank you. I mean, obviously I'm, I'm very privileged in not having to make a living as, [laughs] as an author-

**Melissa Grujicse** [54:04]: Sure

**Blaise Aguera Y Arcas** [54:04]: ... since I have a-

**Melissa Grujicse** [54:04]: Absolutely

**Blaise Aguera Y Arcas** [54:04]: ... I have a day job. But, um, but yeah, my hope is also that making it, making it, uh, widely accessible like that will, uh, you know, will-

**Melissa Grujicse** [54:11]: Reach more

**Blaise Aguera Y Arcas** [54:12]: ... will also just reach more people.

**Melissa Grujicse** [54:12]: Reach the masses.

**Blaise Aguera Y Arcas** [54:13]: Right, including-

**Melissa Grujicse** [54:13]: Yeah

**Blaise Aguera Y Arcas** [54:13]: ... including the physical book. And, uh, uh, I'm on Twitter, or I guess it's now called X, and, uh-

**Melissa Grujicse** [54:20]: [laughs]

**Blaise Aguera Y Arcas** [54:20]: ... and on Instagram as well.

**Melissa Grujicse** [54:21]: X.

**Blaise Aguera Y Arcas** [54:22]: Uh, so I can also be found that way. And then we, we know, we announce, we announce, uh, like I'm starting to do book talks and things, so they're all, they're all announced on there.

**Melissa Grujicse** [54:28]: Awesome.

**Maury Fontanez** [54:29]: Wonderful. And we'll add all of that to our show notes-

**Melissa Grujicse** [54:31]: Definitely

**Maury Fontanez** [54:31]: ... for you listeners if you would like to. I highly encourage, uh, learn more about Blaise and, uh, their amazing work. Blaise, thank you so much for spending this time with us. You were so generous with your time-

**Melissa Grujicse** [54:42]: So wonderful

**Maury Fontanez** [54:42]: ... and your knowledge and your information, and I think you've really added, um, so much to this podcast and for our listeners.

**Melissa Grujicse** [54:50]: Thank you.

**Maury Fontanez** [54:50]: So thank you so much.

**Blaise Aguera Y Arcas** [54:51]: Thank you both so much for your, for your awesome questions and, and for your, and for your interest.

**Melissa Grujicse** [54:55]: And for my deer in headlights look the whole time. [laughs]

**Blaise Aguera Y Arcas** [54:58]: Not at all. [laughs]

**Melissa Grujicse** [55:00]: I, I was in awe, I promise.

**Blaise Aguera Y Arcas** [55:02]: That is, that is real sweet of you. Thank you.

**Maury Fontanez** [55:04]: All right, listener-

**Blaise Aguera Y Arcas** [55:05]: All right. Take care. You too.

**Maury Fontanez** [55:07]: Blaise, thank you again. Um, uh, Bean, I'll see you again next week.

**Melissa Grujicse** [55:12]: See you next week, girl. Actually, I'll see you next week in California.

**Maury Fontanez** [55:15]: Oh, that's right. In person.

**Melissa Grujicse** [55:18]: Live and in person. All right.

**Maury Fontanez** [55:19]: Uh, if you wanna support us, we would so appreciate you sharing this podcast, uh, with your friends and family, and as always, leave us a review anywhere you listen. Thanks, guys. Bye. [outro music] This has been another episode of Signal, the podcast that raises your frequency. This podcast is co-hosted by me, Mauri Fontanez, and Melissa Gouchka. Special thanks to my production team, Anushri Tekade, Arman Kassam, and Anais Islam. Don't forget to join us next week for another episode. See you then. [outro music]

